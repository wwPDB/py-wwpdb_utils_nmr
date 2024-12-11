##
# File: TopSpinPKParserListener.py
# Date: 05-Dec-2024
#
# Updates:
""" ParserLister class for TOPSPIN PK files.
    @author: Masashi Yokochi
"""
import sys

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
        self.exit()

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
            self.initSpectralDim()

        elif self.__cur_path == '/PeakList/PeakList3D':
            self.num_of_dim = 3
            self.initSpectralDim()

        elif self.__cur_path == '/PeakList/PeakList4D':
            self.num_of_dim = 4
            self.initSpectralDim()

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
                sf['id'] = index
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
                sf['id'] = index
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
                sf['id'] = index
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
