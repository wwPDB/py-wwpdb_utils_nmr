##
# File: XwinNmrPKParserListener.py
# Date: 05-Dec-2024
#
# Updates:
""" ParserLister class for XWINNMR PK files.
    @author: Masashi Yokochi
"""
import sys
import numpy as np

from antlr4 import ParseTreeListener

try:
    from wwpdb.utils.nmr.pk.XwinNmrPKParser import XwinNmrPKParser
    from wwpdb.utils.nmr.pk.BasePKParserListener import BasePKParserListener
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (REPRESENTATIVE_MODEL_ID,
                                                       REPRESENTATIVE_ALT_ID,
                                                       getPkRow)

except ImportError:
    from nmr.pk.XwinNmrPKParser import XwinNmrPKParser
    from nmr.pk.BasePKParserListener import BasePKParserListener
    from nmr.mr.ParserListenerUtil import (REPRESENTATIVE_MODEL_ID,
                                           REPRESENTATIVE_ALT_ID,
                                           getPkRow)


# This class defines a complete listener for a parse tree produced by XwinNmrPKParser.
class XwinNmrPKParserListener(ParseTreeListener, BasePKParserListener):

    __f1_ppm_col = -1
    __f2_ppm_col = -1
    __f3_ppm_col = -1
    __f4_ppm_col = -1
    __intensity_col = -1
    __volume_col = -1

    def __init__(self, verbose=True, log=sys.stdout,
                 representativeModelId=REPRESENTATIVE_MODEL_ID,
                 representativeAltId=REPRESENTATIVE_ALT_ID,
                 mrAtomNameMapping=None,
                 cR=None, caC=None, ccU=None, csStat=None, nefT=None,
                 reasons=None):
        super().__init__(verbose, log, representativeModelId, representativeAltId,
                         mrAtomNameMapping, cR, caC, ccU, csStat, nefT, reasons)

        self.file_type = 'nm-pea-xwi'
        self.software_name = 'XWINNMR'

    # Enter a parse tree produced by XwinNmrPKParser#xwinnmr_pk.
    def enterXwinnmr_pk(self, ctx: XwinNmrPKParser.Xwinnmr_pkContext):  # pylint: disable=unused-argument
        self.enter()

    # Exit a parse tree produced by XwinNmrPKParser#xwinnmr_pk.
    def exitXwinnmr_pk(self, ctx: XwinNmrPKParser.Xwinnmr_pkContext):  # pylint: disable=unused-argument

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

    # Enter a parse tree produced by XwinNmrPKParser#comment.
    def enterComment(self, ctx: XwinNmrPKParser.CommentContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XwinNmrPKParser#comment.
    def exitComment(self, ctx: XwinNmrPKParser.CommentContext):
        comment = []
        for col in range(20):
            if ctx.Any_name(col):
                text = str(ctx.Any_name(col))
                comment.append(text)
            else:
                break

        self.__f1_ppm_col = -1
        self.__f2_ppm_col = -1
        self.__f3_ppm_col = -1
        self.__f4_ppm_col = -1
        self.__intensity_col = -1
        self.__volume_col = -1

        if 'F1[ppm]' in comment:
            self.__f1_ppm_col = comment.index('F1[ppm]')
        if 'F2[ppm]' in comment:
            self.__f2_ppm_col = comment.index('F2[ppm]')
        if 'F3[ppm]' in comment and self.num_of_dim >= 3:
            self.__f3_ppm_col = comment.index('F3[ppm]')
        if 'F4[ppm]' in comment and self.num_of_dim >= 4:
            self.__f4_ppm_col = comment.index('F4[ppm]')
        if 'Intensity' in comment:
            self.__intensity_col = comment.index('Intensity')
        if 'Volume' in comment:
            self.__volume_col = comment.index('Volume')

    # Enter a parse tree produced by XwinNmrPKParser#dimension.
    def enterDimension(self, ctx: XwinNmrPKParser.DimensionContext):
        if ctx.Integer_ND():
            self.num_of_dim = int(str(ctx.Integer_ND()))
            self.fillCurrentSpectralDim()

    # Exit a parse tree produced by XwinNmrPKParser#dimension.
    def exitDimension(self, ctx: XwinNmrPKParser.DimensionContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XwinNmrPKParser#peak_2d.
    def enterPeak_2d(self, ctx: XwinNmrPKParser.Peak_2dContext):  # pylint: disable=unused-argument
        self.peaks2D += 1

    # Exit a parse tree produced by XwinNmrPKParser#peak_2d.
    def exitPeak_2d(self, ctx: XwinNmrPKParser.Peak_2dContext):

        if -1 in (self.__f1_ppm_col, self.__f2_ppm_col)\
           or (self.__intensity_col == -1 and self.__volume_col == -1):
            self.peaks2D -= 1
            return

        index = int(str(ctx.Integer()))

        if ctx.Float(self.__f1_ppm_col):
            f1_ppm = float(str(ctx.Float(self.__f1_ppm_col)))
        else:
            self.peaks2D -= 1
            return

        if ctx.Float(self.__f2_ppm_col):
            f2_ppm = float(str(ctx.Float(self.__f2_ppm_col)))
        else:
            self.peaks2D -= 1
            return

        intensity = None
        if self.__intensity_col != -1 and ctx.Float(self.__intensity_col):
            intensity = float(str(ctx.Float(self.__intensity_col)))

        volume = None
        if self.__volume_col != -1 and ctx.Float(self.__volume_col):
            volume = float(str(ctx.Float(self.__volume_col)))

        annotation = None
        if ctx.Annotation(0):
            annotation = []
            i = 0
            while ctx.Annotation(i):
                annotation.append(str(ctx.Annotation(i)))
                i += 1
            annotation = ' '.join(annotation)

        dstFunc = self.validatePeak2D(index, f1_ppm, f2_ppm, None, None, None, None,
                                      None, None, None, None, intensity, None, volume, None)

        if dstFunc is None:
            self.peaks2D -= 1
            return

        cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

        cur_spectral_dim[1]['freq_hint'].append(f1_ppm)
        cur_spectral_dim[2]['freq_hint'].append(f2_ppm)

        if self.createSfDict__:
            sf = self.getSf()

        if self.debug:
            print(f"subtype={self.cur_subtype} id={self.peaks2D} (index={index}) {dstFunc}")

        if self.createSfDict__ and sf is not None:
            sf['index_id'] += 1

            row = getPkRow(self.cur_subtype, sf['id'], sf['index_id'],
                           sf['list_id'], self.entryId, dstFunc,
                           self.authToStarSeq, self.authToOrigSeq, self.offsetHolder,
                           details=annotation)
            sf['loop'].add_data(row)

    # Enter a parse tree produced by XwinNmrPKParser#peak_3d.
    def enterPeak_3d(self, ctx: XwinNmrPKParser.Peak_3dContext):  # pylint: disable=unused-argument
        self.peaks3D += 1

    # Exit a parse tree produced by XwinNmrPKParser#peak_3d.
    def exitPeak_3d(self, ctx: XwinNmrPKParser.Peak_3dContext):

        if -1 in (self.__f1_ppm_col, self.__f2_ppm_col, self.__f3_ppm_col)\
           or (self.__intensity_col == -1 and self.__volume_col == -1):
            self.peaks3D -= 1
            return

        index = int(str(ctx.Integer()))

        if ctx.Float(self.__f1_ppm_col):
            f1_ppm = float(str(ctx.Float(self.__f1_ppm_col)))
        else:
            self.peaks3D -= 1
            return

        if ctx.Float(self.__f2_ppm_col):
            f2_ppm = float(str(ctx.Float(self.__f2_ppm_col)))
        else:
            self.peaks3D -= 1
            return

        if ctx.Float(self.__f3_ppm_col):
            f3_ppm = float(str(ctx.Float(self.__f3_ppm_col)))
        else:
            self.peaks3D -= 1
            return

        intensity = None
        if self.__intensity_col != -1 and ctx.Float(self.__intensity_col):
            intensity = float(str(ctx.Float(self.__intensity_col)))

        volume = None
        if self.__volume_col != -1 and ctx.Float(self.__volume_col):
            volume = float(str(ctx.Float(self.__volume_col)))

        annotation = None
        if ctx.Annotation(0):
            annotation = []
            i = 0
            while ctx.Annotation(i):
                annotation.append(str(ctx.Annotation(i)))
                i += 1
            annotation = ' '.join(annotation)

        dstFunc = self.validatePeak3D(index, f1_ppm, f2_ppm, f3_ppm, None, None, None, None, None, None,
                                      None, None, None, None, None, None, intensity, None, volume, None)

        if dstFunc is None:
            self.peaks3D -= 1
            return

        cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

        cur_spectral_dim[1]['freq_hint'].append(f1_ppm)
        cur_spectral_dim[2]['freq_hint'].append(f2_ppm)
        cur_spectral_dim[3]['freq_hint'].append(f3_ppm)

        if self.createSfDict__:
            sf = self.getSf()

        if self.debug:
            print(f"subtype={self.cur_subtype} id={self.peaks3D} (index={index}) {dstFunc}")

        if self.createSfDict__ and sf is not None:
            sf['index_id'] += 1

            row = getPkRow(self.cur_subtype, sf['id'], sf['index_id'],
                           sf['list_id'], self.entryId, dstFunc,
                           self.authToStarSeq, self.authToOrigSeq, self.offsetHolder,
                           details=annotation)
            sf['loop'].add_data(row)

    # Enter a parse tree produced by XwinNmrPKParser#peak_4d.
    def enterPeak_4d(self, ctx: XwinNmrPKParser.Peak_4dContext):  # pylint: disable=unused-argument
        self.peaks4D += 1

    # Exit a parse tree produced by XwinNmrPKParser#peak_4d.
    def exitPeak_4d(self, ctx: XwinNmrPKParser.Peak_4dContext):

        if -1 in (self.__f1_ppm_col, self.__f2_ppm_col, self.__f3_ppm_col, self.__f4_ppm_col)\
           or (self.__intensity_col == -1 and self.__volume_col == -1):
            self.peaks4D -= 1
            return

        index = int(str(ctx.Integer()))

        if ctx.Float(self.__f1_ppm_col):
            f1_ppm = float(str(ctx.Float(self.__f1_ppm_col)))
        else:
            self.peaks4D -= 1
            return

        if ctx.Float(self.__f2_ppm_col):
            f2_ppm = float(str(ctx.Float(self.__f2_ppm_col)))
        else:
            self.peaks4D -= 1
            return

        if ctx.Float(self.__f3_ppm_col):
            f3_ppm = float(str(ctx.Float(self.__f3_ppm_col)))
        else:
            self.peaks4D -= 1
            return

        if ctx.Float(self.__f4_ppm_col):
            f4_ppm = float(str(ctx.Float(self.__f4_ppm_col)))
        else:
            self.peaks4D -= 1
            return

        intensity = None
        if self.__intensity_col != -1 and ctx.Float(self.__intensity_col):
            intensity = float(str(ctx.Float(self.__intensity_col)))

        volume = None
        if self.__volume_col != -1 and ctx.Float(self.__volume_col):
            volume = float(str(ctx.Float(self.__volume_col)))

        annotation = None
        if ctx.Annotation(0):
            annotation = []
            i = 0
            while ctx.Annotation(i):
                annotation.append(str(ctx.Annotation(i)))
                i += 1
            annotation = ' '.join(annotation)

        dstFunc = self.validatePeak4D(index, f1_ppm, f2_ppm, f3_ppm, f4_ppm, None, None, None, None, None, None, None, None,
                                      None, None, None, None, None, None, None, None, intensity, None, volume, None)

        if dstFunc is None:
            self.peaks4D -= 1
            return

        cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

        cur_spectral_dim[1]['freq_hint'].append(f1_ppm)
        cur_spectral_dim[2]['freq_hint'].append(f2_ppm)
        cur_spectral_dim[3]['freq_hint'].append(f3_ppm)
        cur_spectral_dim[4]['freq_hint'].append(f4_ppm)

        if self.createSfDict__:
            sf = self.getSf()

        if self.debug:
            print(f"subtype={self.cur_subtype} id={self.peaks4D} (index={index}) {dstFunc}")

        if self.createSfDict__ and sf is not None:
            sf['index_id'] += 1

            row = getPkRow(self.cur_subtype, sf['id'], sf['index_id'],
                           sf['list_id'], self.entryId, dstFunc,
                           self.authToStarSeq, self.authToOrigSeq, self.offsetHolder,
                           details=annotation)
            sf['loop'].add_data(row)


# del XwinNmrPKParser
