##
# CcpnPKReader.py
#
# Update:
##
""" A collection of classes for parsing CCPN PK files.
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "1.0.0"

import sys
import os

from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from typing import IO, List, Tuple, Optional

try:
    from wwpdb.utils.nmr.mr.LexerErrorListener import LexerErrorListener
    from wwpdb.utils.nmr.mr.ParserErrorListener import ParserErrorListener
    from wwpdb.utils.nmr.pk.CcpnPKLexer import CcpnPKLexer
    from wwpdb.utils.nmr.pk.CcpnPKParser import CcpnPKParser
    from wwpdb.utils.nmr.pk.CcpnPKParserListener import CcpnPKParserListener
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (coordAssemblyChecker,
                                                       MAX_ERROR_REPORT,
                                                       REPRESENTATIVE_MODEL_ID,
                                                       REPRESENTATIVE_ALT_ID)
    from wwpdb.utils.nmr.io.CifReader import CifReader
    from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
    from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from wwpdb.utils.nmr.nef.NEFTranslator import NEFTranslator
except ImportError:
    from nmr.mr.LexerErrorListener import LexerErrorListener
    from nmr.mr.ParserErrorListener import ParserErrorListener
    from nmr.pk.CcpnPKLexer import CcpnPKLexer
    from nmr.pk.CcpnPKParser import CcpnPKParser
    from nmr.pk.CcpnPKParserListener import CcpnPKParserListener
    from nmr.mr.ParserListenerUtil import (coordAssemblyChecker,
                                           MAX_ERROR_REPORT,
                                           REPRESENTATIVE_MODEL_ID,
                                           REPRESENTATIVE_ALT_ID)
    from nmr.io.CifReader import CifReader
    from nmr.ChemCompUtil import ChemCompUtil
    from nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from nmr.nef.NEFTranslator import NEFTranslator


class CcpnPKReader:
    """ Accessor methods for parsing CCPN PK files.
    """

    def __init__(self, verbose: bool = True, log: IO = sys.stdout,
                 representativeModelId: int = REPRESENTATIVE_MODEL_ID,
                 representativeAltId: str = REPRESENTATIVE_ALT_ID,
                 mrAtomNameMapping: Optional[List[dict]] = None,
                 cR: Optional[CifReader] = None, caC: Optional[dict] = None, ccU: Optional[ChemCompUtil] = None,
                 csStat: Optional[BMRBChemShiftStat] = None, nefT: Optional[NEFTranslator] = None,
                 reasons: Optional[dict] = None):
        self.__class_name__ = self.__class__.__name__
        self.__version__ = __version__

        self.__verbose = verbose
        self.__lfh = log
        self.__debug = False

        self.__maxLexerErrorReport = MAX_ERROR_REPORT
        self.__maxParserErrorReport = MAX_ERROR_REPORT

        self.__representativeModelId = representativeModelId
        self.__representativeAltId = representativeAltId
        self.__mrAtomNameMapping = mrAtomNameMapping

        # CCD accessing utility
        self.__ccU = ChemCompUtil(verbose, log) if ccU is None else ccU

        if cR is not None and caC is None:
            caC = coordAssemblyChecker(verbose, log, representativeModelId, representativeAltId,
                                       cR, self.__ccU, None, None, fullCheck=False)

        self.__cR = cR
        self.__caC = caC

        # BMRB chemical shift statistics
        self.__csStat = BMRBChemShiftStat(verbose, log, self.__ccU) if csStat is None else csStat

        # NEFTranslator
        self.__nefT = NEFTranslator(verbose, log, self.__ccU, self.__csStat) if nefT is None else nefT
        if nefT is None:
            self.__nefT.set_remediation_mode(True)

        # reasons for re-parsing request from the previous trial
        self.__reasons = reasons

    def setDebugMode(self, debug: bool):
        self.__debug = debug

    def setLexerMaxErrorReport(self, maxErrReport: int):
        self.__maxLexerErrorReport = maxErrReport

    def setParserMaxErrorReport(self, maxErrReport: int):
        self.__maxParserErrorReport = maxErrReport

    def parse(self, pkFilePath: str, cifFilePath: Optional[str] = None, isFilePath: bool = True,
              createSfDict: bool = False, originalFileName: Optional[str] = None, listIdCounter: Optional[dict] = None,
              reservedListIds: Optional[dict] = None, entryId: Optional[str] = None, csLoops: Optional[List[dict]] = None
              ) -> Tuple[Optional[CcpnPKParserListener], Optional[ParserErrorListener], Optional[LexerErrorListener]]:
        """ Parse CCPN PK file.
            @return: CcpnPKParserListener for success or None otherwise, ParserErrorListener, LexerErrorListener.
        """

        ifh = None

        try:

            if isFilePath:
                pkString = None

                if not os.access(pkFilePath, os.R_OK):
                    if self.__verbose:
                        self.__lfh.write(f"+{self.__class_name__}.parse() {pkFilePath} is not accessible.\n")
                    return None, None, None

                ifh = open(pkFilePath, 'r', encoding='utf-8', errors='ignore')  # pylint: disable=consider-using-with
                input = InputStream(ifh.read())

            else:
                pkFilePath, pkString = None, pkFilePath

                if pkString is None or len(pkString) == 0:
                    if self.__verbose:
                        self.__lfh.write(f"+{self.__class_name__}.parse() Empty string.\n")
                    return None, None, None

                input = InputStream(pkString)

            if cifFilePath is not None:
                if not os.access(cifFilePath, os.R_OK):
                    if self.__verbose:
                        self.__lfh.write(f"+{self.__class_name__}.parse() {cifFilePath} is not accessible.\n")
                    return None, None, None

                if self.__cR is None:
                    self.__cR = CifReader(self.__verbose, self.__lfh)
                    if not self.__cR.parse(cifFilePath):
                        return None, None, None

            lexer = CcpnPKLexer(input)
            lexer.removeErrorListeners()

            lexer_error_listener = LexerErrorListener(pkFilePath, maxErrorReport=self.__maxLexerErrorReport, ignoreCodicError=True)
            lexer.addErrorListener(lexer_error_listener)

            messageList = lexer_error_listener.getMessageList()

            if messageList is not None and self.__verbose:
                for description in messageList:
                    self.__lfh.write(f"[Syntax error] line {description['line_number']}:{description['column_position']} {description['message']}\n")
                    if 'input' in description:
                        self.__lfh.write(f"{description['input']}\n")
                        self.__lfh.write(f"{description['marker']}\n")

            stream = CommonTokenStream(lexer)
            parser = CcpnPKParser(stream)
            # try with simpler/faster SLL prediction mode
            # parser._interp.predictionMode = PredictionMode.SLL  # pylint: disable=protected-access
            parser.removeErrorListeners()
            parser_error_listener = ParserErrorListener(pkFilePath, maxErrorReport=self.__maxParserErrorReport, ignoreCodicError=True)
            parser.addErrorListener(parser_error_listener)
            tree = parser.ccpn_pk()

            walker = ParseTreeWalker()
            listener = CcpnPKParserListener(self.__verbose, self.__lfh,
                                            self.__representativeModelId,
                                            self.__representativeAltId,
                                            self.__mrAtomNameMapping,
                                            self.__cR, self.__caC,
                                            self.__ccU, self.__csStat, self.__nefT,
                                            self.__reasons)
            listener.setDebugMode(self.__debug)
            listener.createSfDict(createSfDict)
            if createSfDict:
                if originalFileName is not None:
                    listener.setOriginaFileName(originalFileName)
                if listIdCounter is not None:
                    listener.setListIdCounter(listIdCounter)
                if reservedListIds is not None:
                    listener.setReservedListIds(reservedListIds)
                if entryId is not None:
                    listener.setEntryId(entryId)
                if csLoops is not None:
                    listener.setCsLoops(csLoops)
            walker.walk(listener, tree)

            messageList = parser_error_listener.getMessageList()

            if messageList is not None and self.__verbose:
                for description in messageList:
                    self.__lfh.write(f"[Syntax error] line {description['line_number']}:{description['column_position']} {description['message']}\n")
                    if 'input' in description:
                        self.__lfh.write(f"{description['input']}\n")
                        self.__lfh.write(f"{description['marker']}\n")

            if self.__verbose and self.__debug:
                if listener.warningMessage is not None and len(listener.warningMessage) > 0:
                    self.__lfh.write(f"+{self.__class_name__}.parse() ++ Info  -\n" + '\n'.join(listener.warningMessage) + '\n')
                if isFilePath:
                    self.__lfh.write(f"+{self.__class_name__}.parse() ++ Info  - {listener.getContentSubtype()}\n")

            return listener, parser_error_listener, lexer_error_listener

        except IOError as e:
            if self.__verbose:
                self.__lfh.write(f"+{self.__class_name__}.parse() ++ Error  - {str(e)}\n")
            return None, None, None
        finally:
            if isFilePath and ifh is not None:
                ifh.close()


if __name__ == "__main__":
    reader = CcpnPKReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/5ug3/bmr30225/work/data/D_1000225655_nmr-peaks-upload_P2.dat.V2',
                 '../../tests-nmr/mock-data-remediation/5ug3/5ug3.cif')

    reader = CcpnPKReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/5ug5/bmr30226/work/data/D_1000225737_nmr-peaks-upload_P1.dat.V4',
                 '../../tests-nmr/mock-data-remediation/5ug5/5ug5.cif')

    reader = CcpnPKReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/5ug5/bmr30226/work/data/D_1000225737_nmr-peaks-upload_P2.dat.V2',
                 '../../tests-nmr/mock-data-remediation/5ug5/5ug5.cif')

    reader = CcpnPKReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/6ffr/bmr34228/work/data/D_1200008232_nmr-peaks-upload_P1.dat.V3',
                 '../../tests-nmr/mock-data-remediation/6ffr/6ffr.cif')

    reader = CcpnPKReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/6h0q/bmr34301/work/data/D_1200010858_nmr-peaks-upload_P1.dat.V1',
                 '../../tests-nmr/mock-data-remediation/6h0q/6h0q.cif')

    reader = CcpnPKReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/8aou/bmr34748/work/data/D_1292124790_nmr-peaks-upload_P1.dat.V1',
                 '../../tests-nmr/mock-data-remediation/8aou/8aou.cif')

    reader = CcpnPKReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/6h0j/bmr34299/work/data/D_1200010843_nmr-peaks-upload_P1.dat.V1',
                 '../../tests-nmr/mock-data-remediation/6h0j/6h0j.cif')

    reader = CcpnPKReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/6nom/bmr30561/work/data/D_1000238062_nmr-peaks-upload_P1.dat.V3',
                 '../../tests-nmr/mock-data-remediation/6nom/6nom.cif')

    reader = CcpnPKReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/6r28/bmr34380/work/data/D_1292101294_nmr-peaks-upload_P1.dat.V1',
                 '../../tests-nmr/mock-data-remediation/6r28/6r28.cif')

    reader = CcpnPKReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/6vla/bmr30717/work/data/D_1000246592_nmr-peaks-upload_P1.dat.V1',
                 '../../tests-nmr/mock-data-remediation/6vla/6vla.cif')
