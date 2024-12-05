##
# File: TopSpinPKParserListener.py
# Date: 05-Dec-2024
#
# Updates:
""" ParserLister class for TOPSPIN PK files.
    @author: Masashi Yokochi
"""
import sys
import numpy as np

from antlr4 import ParseTreeListener

try:
    from wwpdb.utils.nmr.pk.XMLParser import XMLParser
    from wwpdb.utils.nmr.pk.BasePKParserListener import BasePKParserListener
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (REPRESENTATIVE_MODEL_ID,
                                                       REPRESENTATIVE_ALT_ID,
                                                       getPkRow)

except ImportError:
    from nmr.pk.XMLParser import XMLParser
    from nmr.pk.BasePKParserListener import BasePKParserListener
    from nmr.mr.ParserListenerUtil import (REPRESENTATIVE_MODEL_ID,
                                           REPRESENTATIVE_ALT_ID,
                                           getPkRow)


# This class defines a complete listener for a parse tree produced by XMLParser.
class TopSpinPKParserListener(ParseTreeListener, BasePKParserListener):

    __cur_path = None

    __f1_ppm = None
    __f2_ppm = None
    __f3_ppm = None
    __f4_ppm = None
    __intensity = None
    __volume = None
    __annotation = None

    def __init__(self, verbose=True, log=sys.stdout,
                 representativeModelId=REPRESENTATIVE_MODEL_ID,
                 representativeAltId=REPRESENTATIVE_ALT_ID,
                 mrAtomNameMapping=None,
                 cR=None, caC=None, ccU=None, csStat=None, nefT=None,
                 reasons=None):
        super().__init__(verbose, log, representativeModelId, representativeAltId,
                         mrAtomNameMapping, cR, caC, ccU, csStat, nefT, reasons)

        self.file_type = 'nm-pea-top'
        self.software_name = 'TOPSPIN'

    # Enter a parse tree produced by XMLParser#document.
    def enterDocument(self, ctx: XMLParser.DocumentContext):  # pylint: disable=unused-argument
        self.__cur_path = ''

        self.enter()

    # Exit a parse tree produced by XMLParser#document.
    def exitDocument(self, ctx: XMLParser.DocumentContext):  # pylint: disable=unused-argument

        if len(self.spectral_dim) > 0:
            for d, v in self.spectral_dim.items():
                for _id, _v in v.items():
                    self.acq_dim_id = 1
                    for __d, __v in _v.items():
                        if 'freq_hint' in __v:
                            if len(__v['freq_hint']) > 0:
                                center = np.mean(np.array(__v['freq_hint']))

                                if __v['atom_isotope_number'] is None:
                                    if 125 < center < 130:
                                        __v['atom_type'] = 'C'
                                        __v['atom_isotope_number'] = 13
                                        __v['axis_code'] = 'C_aro'
                                    elif 115 < center < 125:
                                        __v['atom_type'] = 'N'
                                        __v['atom_isotope_number'] = 15
                                        __v['axis_code'] = 'N_ami'
                                    elif 170 < center < 180:
                                        __v['atom_type'] = 'C'
                                        __v['atom_isotope_number'] = 13
                                        __v['axis_code'] = 'CO'
                                    elif 6 < center < 9:
                                        __v['atom_type'] = 'H'
                                        __v['atom_isotope_number'] = 1
                                        __v['axis_code'] = 'H_ami_or_aro'
                                    elif 4 < center < 6:
                                        __v['atom_type'] = 'H'
                                        __v['atom_isotope_number'] = 1
                                        __v['axis_code'] = 'H'
                                    elif 2 < center < 4:
                                        __v['atom_type'] = 'H'
                                        __v['atom_isotope_number'] = 1
                                        __v['axis_code'] = 'H_ali'
                                    elif 60 < center < 90:
                                        __v['atom_type'] = 'C'
                                        __v['atom_isotope_number'] = 13
                                        __v['axis_code'] = 'C'
                                    elif 30 < center < 50:
                                        __v['atom_type'] = 'C'
                                        __v['atom_isotope_number'] = 13
                                        __v['axis_code'] = 'C_ali'

                                isotope_number = __v['atom_isotope_number']

                                if isotope_number is not None:
                                    __v['acquisition'] = 'yes' if __d == self.acq_dim_id\
                                        and (isotope_number == 1 or (isotope_number == 13 and self.exptlMethod == 'SOLID-STATE NMR')) else 'no'

                                    if __d == 1 and __v['acquisition'] == 'no':
                                        self.acq_dim_id = self.num_of_dim

                                    __v['under_sampling_type'] = 'not observed' if __v['acquisition'] == 'yes' else 'aliased'

                            if __v['spectral_region'] is None and len(__v['freq_hint']) > 0:
                                atom_type = __v['atom_type']
                                if 125 < center < 130 and atom_type == 'C':
                                    __v['spectral_region'] = 'C_aro'
                                elif 115 < center < 125 and atom_type == 'N':
                                    __v['spectral_region'] = 'N_ami'
                                elif 170 < center < 180 and atom_type == 'C':
                                    __v['spectral_region'] = 'CO'
                                elif 6 < center < 9 and atom_type == 'H':
                                    __v['spectral_region'] = 'H_ami_or_aro'
                                elif 4 < center < 6 and atom_type == 'H':
                                    __v['spectral_region'] = 'H_all'
                                elif 2 < center < 4 and atom_type == 'H':
                                    __v['spectral_region'] = 'H_ali'
                                elif 60 < center < 90 and atom_type == 'C':
                                    __v['spectral_region'] = 'C_all'
                                elif 30 < center < 50 and atom_type == 'C':
                                    __v['spectral_region'] = 'C_ali'

                            if len(__v['freq_hint']) > 0 and d > 2 and __d >= 2\
                               and self.exptlMethod != 'SOLID-STATE NMR' and __v['atom_isotope_number'] == 13:
                                max_ppm = max(__v['freq_hint'])
                                min_ppm = min(__v['freq_hint'])
                                width = max_ppm - min_ppm
                                if center < 100.0 and width < 50.0:
                                    __v['under_sampling_type'] = 'fold'

                            del __v['freq_hint']

                    for __v in _v.values():
                        if __v['axis_code'] == 'H_ami_or_aro':
                            has_a = any(___v['spectral_region'] == 'C_aro' for ___v in _v.values())
                            __v['axis_code'] = 'H_aro' if has_a else 'H_ami'
                        if __v['spectral_region'] == 'H_ami_or_aro':
                            has_a = any(___v['spectral_region'] == 'C_aro' for ___v in _v.values())
                            __v['spectral_region'] = 'H_aro' if has_a else 'H_ami'

                    if self.debug:
                        print(f'num_of_dim: {d}, list_id: {_id}')
                        for __d, __v in _v.items():
                            print(f'{__d} {__v}')

        self.exit()

        self.__cur_path = None

    # Enter a parse tree produced by XMLParser#prolog.
    def enterProlog(self, ctx: XMLParser.PrologContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XMLParser#prolog.
    def exitProlog(self, ctx: XMLParser.PrologContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XMLParser#content.
    def enterContent(self, ctx: XMLParser.ContentContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XMLParser#content.
    def exitContent(self, ctx: XMLParser.ContentContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XMLParser#element.
    def enterElement(self, ctx: XMLParser.ElementContext):
        self.__cur_path += '/' + str(ctx.Name(0))

        if self.__cur_path == '/PeakList/PeakList2D':
            self.num_of_dim = 2
            self.fillCurrentSpectralDim()

        elif self.__cur_path == '/PeakList/PeakList3D':
            self.num_of_dim = 3
            self.fillCurrentSpectralDim()

        elif self.__cur_path == '/PeakList/PeakList4D':
            self.num_of_dim = 4
            self.fillCurrentSpectralDim()

        elif self.__cur_path == '/PeakList/PeakList2D/Peak2D':
            self.peaks2D += 1

            self.__f1_ppm = None
            self.__f2_ppm = None
            self.__intensity = None
            self.__volume = None
            self.__annotation = None

        elif self.__cur_path == '/PeakList/PeakList3D/Peak3D':
            self.peaks3D += 1

            self.__f1_ppm = None
            self.__f2_ppm = None
            self.__f3_ppm = None
            self.__intensity = None
            self.__volume = None
            self.__annotation = None

        elif self.__cur_path == '/PeakList/PeakList4D/Peak4D':
            self.peaks4D += 1

            self.__f1_ppm = None
            self.__f2_ppm = None
            self.__f3_ppm = None
            self.__f4_ppm = None
            self.__intensity = None
            self.__volume = None
            self.__annotation = None

    # Exit a parse tree produced by XMLParser#element.
    def exitElement(self, ctx: XMLParser.ElementContext):  # pylint: disable=unused-argument

        if self.__cur_path == '/PeakList/PeakList2D/Peak2D':

            if None in (self.__f1_ppm, self.__f2_ppm)\
               or (self.__intensity is None and self.__volume is None):
                self.peaks2D -= 1
                return

            index = self.peaks2D

            dstFunc = self.validatePeak2D(index, self.__f1_ppm, self.__f2_ppm, None, None, None, None,
                                          None, None, None, None, self.__intensity, None, self.__volume, None)

            if dstFunc is None:
                self.peaks2D -= 1
                return

            cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

            cur_spectral_dim[1]['freq_hint'].append(self.__f1_ppm)
            cur_spectral_dim[2]['freq_hint'].append(self.__f2_ppm)

            if self.createSfDict__:
                sf = self.getSf()

            if self.debug:
                print(f"subtype={self.cur_subtype} id={self.peaks2D} (index={index}) {dstFunc}")

            if self.createSfDict__ and sf is not None:
                sf['index_id'] += 1

                row = getPkRow(self.cur_subtype, sf['id'], sf['index_id'],
                               sf['list_id'], self.entryId, dstFunc,
                               self.authToStarSeq, self.authToOrigSeq, self.offsetHolder,
                               details=self.__annotation)
                sf['loop'].add_data(row)

        elif self.__cur_path == '/PeakList/PeakList3D/Peak3D':

            if None in (self.__f1_ppm, self.__f2_ppm, self.__f3_ppm)\
               or (self.__intensity is None and self.__volume is None):
                self.peaks3D -= 1
                return

            index = self.peaks3D

            dstFunc = self.validatePeak3D(index, self.__f1_ppm, self.__f2_ppm, self.__f3_ppm, None, None, None, None, None, None,
                                          None, None, None, None, None, None, self.__intensity, None, self.__volume, None)

            if dstFunc is None:
                self.peaks3D -= 1
                return

            cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

            cur_spectral_dim[1]['freq_hint'].append(self.__f1_ppm)
            cur_spectral_dim[2]['freq_hint'].append(self.__f2_ppm)
            cur_spectral_dim[3]['freq_hint'].append(self.__f3_ppm)

            if self.createSfDict__:
                sf = self.getSf()

            if self.debug:
                print(f"subtype={self.cur_subtype} id={self.peaks3D} (index={index}) {dstFunc}")

            if self.createSfDict__ and sf is not None:
                sf['index_id'] += 1

                row = getPkRow(self.cur_subtype, sf['id'], sf['index_id'],
                               sf['list_id'], self.entryId, dstFunc,
                               self.authToStarSeq, self.authToOrigSeq, self.offsetHolder,
                               details=self.__annotation)
                sf['loop'].add_data(row)

        elif self.__cur_path == '/PeakList/PeakList4D/Peak4D':

            if None in (self.__f1_ppm, self.__f2_ppm, self.__f3_ppm, self.__f4_ppm)\
               or (self.__intensity is None and self.__volume is None):
                self.peaks4D -= 1
                return

            index = self.peaks4D

            dstFunc = self.validatePeak4D(index, self.__f1_ppm, self.__f2_ppm, self.__f3_ppm, self.__f4_ppm, None, None, None, None, None, None, None, None,
                                          None, None, None, None, None, None, None, None, self.__intensity, None, self.__volume, None)

            if dstFunc is None:
                self.peaks4D -= 1
                return

            cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

            cur_spectral_dim[1]['freq_hint'].append(self.__f1_ppm)
            cur_spectral_dim[2]['freq_hint'].append(self.__f2_ppm)
            cur_spectral_dim[3]['freq_hint'].append(self.__f3_ppm)
            cur_spectral_dim[4]['freq_hint'].append(self.__f4_ppm)

            if self.createSfDict__:
                sf = self.getSf()

            if self.debug:
                print(f"subtype={self.cur_subtype} id={self.peaks4D} (index={index}) {dstFunc}")

            if self.createSfDict__ and sf is not None:
                sf['index_id'] += 1

                row = getPkRow(self.cur_subtype, sf['id'], sf['index_id'],
                               sf['list_id'], self.entryId, dstFunc,
                               self.authToStarSeq, self.authToOrigSeq, self.offsetHolder,
                               details=self.__annotation)
                sf['loop'].add_data(row)

        self.__cur_path = self.__cur_path[:-(1 + len(str(ctx.Name(0))))]

    # Enter a parse tree produced by XMLParser#reference.
    def enterReference(self, ctx: XMLParser.ReferenceContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XMLParser#reference.
    def exitReference(self, ctx: XMLParser.ReferenceContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XMLParser#attribute.
    def enterAttribute(self, ctx: XMLParser.AttributeContext):

        if ctx.Name() and ctx.STRING():
            name = str(ctx.Name())
            string = str(ctx.STRING())[1:-1]

            if self.__cur_path == '/PeakList/PeakList2D/Peak2D':

                if name == 'F1':
                    self.__f1_ppm = float(string)
                elif name == 'F2':
                    self.__f2_ppm = float(string)
                elif name == 'intensity':
                    self.__intensity = string
                elif name == 'volume':
                    self.__volume = string
                elif name == 'annotation':
                    self.__annotation = string

            elif self.__cur_path == '/PeakList/PeakList3D/Peak3D':

                if name == 'F1':
                    self.__f1_ppm = float(string)
                elif name == 'F2':
                    self.__f2_ppm = float(string)
                elif name == 'F3':
                    self.__f3_ppm = float(string)
                elif name == 'intensity':
                    self.__intensity = string
                elif name == 'volume':
                    self.__volume = string
                elif name == 'annotation':
                    self.__annotation = string

            elif self.__cur_path == '/PeakList/PeakList4D/Peak4D':

                if name == 'F1':
                    self.__f1_ppm = float(string)
                elif name == 'F2':
                    self.__f2_ppm = float(string)
                elif name == 'F3':
                    self.__f3_ppm = float(string)
                elif name == 'F4':
                    self.__f4_ppm = float(string)
                elif name == 'intensity':
                    self.__intensity = string
                elif name == 'volume':
                    self.__volume = string
                elif name == 'annotation':
                    self.__annotation = string

    # Exit a parse tree produced by XMLParser#attribute.
    def exitAttribute(self, ctx: XMLParser.AttributeContext):
        pass

    # Enter a parse tree produced by XMLParser#chardata.
    def enterChardata(self, ctx: XMLParser.ChardataContext):
        pass

    # Exit a parse tree produced by XMLParser#chardata.
    def exitChardata(self, ctx: XMLParser.ChardataContext):
        pass

    # Enter a parse tree produced by XMLParser#misc.
    def enterMisc(self, ctx: XMLParser.MiscContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XMLParser#misc.
    def exitMisc(self, ctx: XMLParser.MiscContext):  # pylint: disable=unused-argument
        pass
