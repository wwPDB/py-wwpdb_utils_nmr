##
# AmberMRReader.py
#
# Update:
##
""" A collection of classes for parsing AMBER MR files.
"""
import sys
import os

from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker

try:
    from wwpdb.utils.nmr.mr.LexerErrorListener import LexerErrorListener
    from wwpdb.utils.nmr.mr.ParserErrorListener import ParserErrorListener
    from wwpdb.utils.nmr.mr.AmberMRLexer import AmberMRLexer
    from wwpdb.utils.nmr.mr.AmberMRParser import AmberMRParser
    from wwpdb.utils.nmr.mr.AmberMRParserListener import AmberMRParserListener
    from wwpdb.utils.nmr.mr.AmberPTReader import AmberPTReader
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (checkCoordinates,
                                                       REPRESENTATIVE_MODEL_ID)
    from wwpdb.utils.nmr.io.CifReader import CifReader
    from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
    from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from wwpdb.utils.nmr.NEFTranslator.NEFTranslator import NEFTranslator
except ImportError:
    from nmr.mr.LexerErrorListener import LexerErrorListener
    from nmr.mr.ParserErrorListener import ParserErrorListener
    from nmr.mr.AmberMRLexer import AmberMRLexer
    from nmr.mr.AmberMRParser import AmberMRParser
    from nmr.mr.AmberMRParserListener import AmberMRParserListener
    from nmr.mr.AmberPTReader import AmberPTReader
    from nmr.mr.ParserListenerUtil import (checkCoordinates,
                                           REPRESENTATIVE_MODEL_ID)
    from nmr.io.CifReader import CifReader
    from nmr.ChemCompUtil import ChemCompUtil
    from nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from nmr.NEFTranslator.NEFTranslator import NEFTranslator


class AmberMRReader:
    """ Accessor methods for parsing AMBER MR files.
    """

    def __init__(self, verbose=True, log=sys.stdout,
                 representativeModelId=REPRESENTATIVE_MODEL_ID,
                 cR=None, cC=None, ccU=None, csStat=None, nefT=None,
                 atomNumberDict=None):
        self.__verbose = verbose
        self.__lfh = log
        self.__debug = False

        self.__representativeModelId = representativeModelId

        if cR is not None and cC is None:
            cC = checkCoordinates(verbose, log, representativeModelId, cR, None, testTag=False)

        self.__cR = cR
        self.__cC = cC

        # CCD accessing utility
        self.__ccU = ChemCompUtil(verbose, log) if ccU is None else ccU

        # BMRB chemical shift statistics
        self.__csStat = BMRBChemShiftStat(verbose, log, self.__ccU) if csStat is None else csStat

        # NEFTranslator
        self.__nefT = NEFTranslator(verbose, log, self.__ccU, self.__csStat) if nefT is None else nefT

        # AmberPTParserListener.getAtomNumberDict()
        self.__atomNumberDict = atomNumberDict

    def setDebugMode(self, debug):
        self.__debug = debug

    def parse(self, mrFilePath, cifFilePath=None, ptFilePath=None):
        """ Parse AMBER MR file.
            @return: AmberMRParserListener for success or None otherwise, ParserErrorListener, LexerErrorListener.
        """

        try:

            if not os.access(mrFilePath, os.R_OK):
                if self.__verbose:
                    self.__lfh.write(f"AmberMRReader.parse() {mrFilePath} is not accessible.\n")
                return None, None, None

            if cifFilePath is not None:
                if not os.access(cifFilePath, os.R_OK):
                    if self.__verbose:
                        self.__lfh.write(f"AmberMRReader.parse() {cifFilePath} is not accessible.\n")
                    return None, None, None

                if self.__cR is None:
                    self.__cR = CifReader(self.__verbose, self.__lfh)
                    if not self.__cR.parse(cifFilePath):
                        return None, None, None

            if ptFilePath is not None and self.__atomNumberDict is None:
                ptR = AmberPTReader(self.__verbose, self.__lfh,
                                    self.__representativeModelId,
                                    self.__cR, self.__cC,
                                    self.__ccU, self.__csStat)
                ptPL, _, _ = ptR.parse(ptFilePath, cifFilePath)
                if ptPL is not None:
                    self.__atomNumberDict = ptPL.getAtomNumberDict()

            while True:

                with open(mrFilePath) as ifp:

                    ifs = InputStream(ifp.read())

                    lexer = AmberMRLexer(ifs)
                    lexer.removeErrorListeners()

                    lexer_error_listener = LexerErrorListener(mrFilePath)
                    lexer.addErrorListener(lexer_error_listener)

                    messageList = lexer_error_listener.getMessageList()

                    if messageList is not None and self.__verbose:
                        for description in messageList:
                            self.__lfh.write(f"[Syntax error] line {description['line_number']}:{description['column_position']} {description['message']}\n")
                            if 'input' in description:
                                self.__lfh.write(f"{description['input']}\n")
                                self.__lfh.write(f"{description['marker']}\n")

                    stream = CommonTokenStream(lexer)
                    parser = AmberMRParser(stream)
                    parser.removeErrorListeners()
                    parser_error_listener = ParserErrorListener(mrFilePath)
                    parser.addErrorListener(parser_error_listener)
                    tree = parser.amber_mr()

                    walker = ParseTreeWalker()
                    listener = AmberMRParserListener(self.__verbose, self.__lfh,
                                                     self.__representativeModelId,
                                                     self.__cR, self.__cC,
                                                     self.__ccU, self.__csStat, self.__nefT,
                                                     self.__atomNumberDict)
                    listener.setDebugMode(self.__debug)
                    walker.walk(listener, tree)

                    messageList = parser_error_listener.getMessageList()

                    if messageList is not None and self.__verbose:
                        for description in messageList:
                            self.__lfh.write(f"[Syntax error] line {description['line_number']}:{description['column_position']} {description['message']}\n")
                            if 'input' in description:
                                self.__lfh.write(f"{description['input']}\n")
                                self.__lfh.write(f"{description['marker']}\n")

                    if self.__verbose:
                        if listener.warningMessage is not None:
                            print(listener.warningMessage)

                    if self.__atomNumberDict is not None:
                        if self.__verbose:
                            print(listener.getContentSubtype())
                        break

                    sanderAtomNumberDict = listener.getSanderAtomNumberDict()
                    if len(sanderAtomNumberDict) > 0:
                        self.__atomNumberDict = sanderAtomNumberDict
                    else:
                        break

            return listener, parser_error_listener, lexer_error_listener

        except IOError as e:
            if self.__verbose:
                self.__lfh.write(f"+AmberMRReader.parse() ++ Error - {str(e)}\n")
            return None, None, None


if __name__ == "__main__":
    reader = AmberMRReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-daother-7421/amber_rdc.test',
                 '../../tests-nmr/mock-data-daother-7421/D_800450_model_P1.cif.V1',
                 '../../tests-nmr/mock-data-daother-7421/D_1292118884_mr-upload_P1.dat.V1')

    reader = AmberMRReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-daother-7421/D_1292118884_mr-upload_P1.amber.V1',
                 '../../tests-nmr/mock-data-daother-7421/D_800450_model_P1.cif.V1',
                 '../../tests-nmr/mock-data-daother-7421/D_1292118884_mr-upload_P1.dat.V1')
