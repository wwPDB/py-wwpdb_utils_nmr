##
# CharmmCRDReader.py
#
# Update:
##
""" A collection of classes for parsing CHARMM CRD files.
"""
import sys
import os

from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker, PredictionMode

try:
    from wwpdb.utils.nmr.mr.LexerErrorListener import LexerErrorListener
    from wwpdb.utils.nmr.mr.ParserErrorListener import ParserErrorListener
    from wwpdb.utils.nmr.mr.CharmmCRDLexer import CharmmCRDLexer
    from wwpdb.utils.nmr.mr.CharmmCRDParser import CharmmCRDParser
    from wwpdb.utils.nmr.mr.CharmmCRDParserListener import CharmmCRDParserListener
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (coordAssemblyChecker,
                                                       MAX_ERROR_REPORT,
                                                       REPRESENTATIVE_MODEL_ID,
                                                       REPRESENTATIVE_ALT_ID)
    from wwpdb.utils.nmr.io.CifReader import CifReader
    from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
    from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
except ImportError:
    from nmr.mr.LexerErrorListener import LexerErrorListener
    from nmr.mr.ParserErrorListener import ParserErrorListener
    from nmr.mr.CharmmCRDLexer import CharmmCRDLexer
    from nmr.mr.CharmmCRDParser import CharmmCRDParser
    from nmr.mr.CharmmCRDParserListener import CharmmCRDParserListener
    from nmr.mr.ParserListenerUtil import (coordAssemblyChecker,
                                           MAX_ERROR_REPORT,
                                           REPRESENTATIVE_MODEL_ID,
                                           REPRESENTATIVE_ALT_ID)
    from nmr.io.CifReader import CifReader
    from nmr.ChemCompUtil import ChemCompUtil
    from nmr.BMRBChemShiftStat import BMRBChemShiftStat


class CharmmCRDReader:
    """ Accessor methods for parsing CHARMM CRD files.
    """

    def __init__(self, verbose=True, log=sys.stdout,
                 representativeModelId=REPRESENTATIVE_MODEL_ID,
                 representativeAltId=REPRESENTATIVE_ALT_ID,
                 mrAtomNameMapping=None,
                 cR=None, caC=None, ccU=None, csStat=None):
        self.__verbose = verbose
        self.__lfh = log

        self.__maxLexerErrorReport = MAX_ERROR_REPORT
        self.__maxParserErrorReport = MAX_ERROR_REPORT

        self.__representativeModelId = representativeModelId
        self.__representativeAltId = representativeAltId
        self.__mrAtomNameMapping = mrAtomNameMapping

        if cR is not None and caC is None:
            caC = coordAssemblyChecker(verbose, log, representativeModelId, representativeAltId,
                                       cR, None, None, fullCheck=False)

        self.__cR = cR
        self.__caC = caC

        # CCD accessing utility
        self.__ccU = ChemCompUtil(verbose, log) if ccU is None else ccU

        # BMRB chemical shift statistics
        self.__csStat = BMRBChemShiftStat(verbose, log, self.__ccU) if csStat is None else csStat

    def setLexerMaxErrorReport(self, maxErrReport):
        self.__maxLexerErrorReport = maxErrReport

    def setParserMaxErrorReport(self, maxErrReport):
        self.__maxParserErrorReport = maxErrReport

    def parse(self, ptFilePath, cifFilePath=None, isFilePath=True):
        """ Parse CHARMM CRD file.
            @return: CharmmCRDParserListener for success or None otherwise, ParserErrorListener, LexerErrorListener.
        """

        ifh = None

        try:

            if isFilePath:
                ptString = None

                if not os.access(ptFilePath, os.R_OK):
                    if self.__verbose:
                        self.__lfh.write(f"CharmmCRDReader.parse() {ptFilePath} is not accessible.\n")
                    return None, None, None

                ifh = open(ptFilePath, 'r')  # pylint: disable=consider-using-with
                input = InputStream(ifh.read())

            else:
                ptFilePath, ptString = None, ptFilePath

                if ptString is None or len(ptString) == 0:
                    if self.__verbose:
                        self.__lfh.write("CharmmCRDReader.parse() Empty string.\n")
                    return None, None, None

                input = InputStream(ptString)

            if cifFilePath is not None:
                if not os.access(cifFilePath, os.R_OK):
                    if self.__verbose:
                        self.__lfh.write(f"CharmmCRDReader.parse() {cifFilePath} is not accessible.\n")
                    return None, None, None

                if self.__cR is None:
                    self.__cR = CifReader(self.__verbose, self.__lfh)
                    if not self.__cR.parse(cifFilePath):
                        return None, None, None

            lexer = CharmmCRDLexer(input)
            lexer.removeErrorListeners()

            lexer_error_listener = LexerErrorListener(ptFilePath, maxErrorReport=self.__maxLexerErrorReport)
            lexer.addErrorListener(lexer_error_listener)

            messageList = lexer_error_listener.getMessageList()

            if messageList is not None and self.__verbose:
                for description in messageList:
                    self.__lfh.write(f"[Syntax error] line {description['line_number']}:{description['column_position']} {description['message']}\n")
                    if 'input' in description:
                        self.__lfh.write(f"{description['input']}\n")
                        self.__lfh.write(f"{description['marker']}\n")

            stream = CommonTokenStream(lexer)
            parser = CharmmCRDParser(stream)
            # try with simpler/faster SLL prediction mode
            parser._interp.predictionMode = PredictionMode.SLL  # pylint: disable=protected-access
            parser.removeErrorListeners()
            parser_error_listener = ParserErrorListener(ptFilePath, maxErrorReport=self.__maxParserErrorReport)
            parser.addErrorListener(parser_error_listener)
            tree = parser.charmm_crd()

            walker = ParseTreeWalker()
            listener = CharmmCRDParserListener(self.__verbose, self.__lfh,
                                               self.__representativeModelId,
                                               self.__representativeAltId,
                                               self.__mrAtomNameMapping,
                                               self.__cR, self.__caC,
                                               self.__ccU, self.__csStat)
            walker.walk(listener, tree)

            messageList = parser_error_listener.getMessageList()

            if messageList is not None and self.__verbose:
                for description in messageList:
                    self.__lfh.write(f"[Syntax error] line {description['line_number']}:{description['column_position']} {description['message']}\n")
                    if 'input' in description:
                        self.__lfh.write(f"{description['input']}\n")
                        self.__lfh.write(f"{description['marker']}\n")

            if self.__verbose:
                if listener.warningMessage is not None and len(listener.warningMessage) > 0:
                    print('\n'.join(listener.warningMessage))
                if isFilePath:
                    print(listener.getContentSubtype())

            return listener, parser_error_listener, lexer_error_listener

        except IOError as e:
            if self.__verbose:
                self.__lfh.write(f"+CharmmCRDReader.parse() ++ Error - {str(e)}\n")
            return None, None, None
            # pylint: disable=unreachable
            """ debug code
        except Exception as e:
            if self.__verbose and isFilePath:
                self.__lfh.write(f"+CharmmCRDReader.parse() ++ Error - {ptFilePath!r} - {str(e)}\n")
            return None, None, None
            """
        finally:
            if isFilePath and ifh is not None:
                ifh.close()


if __name__ == "__main__":
    reader = CharmmCRDReader(True)
    reader.parse('../../tests-nmr/mock-data-remediation/6wfn/6wfn.crd',
                 '../../tests-nmr/mock-data-remediation/6wfn/6wfn.cif')