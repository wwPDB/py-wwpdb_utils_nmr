##
# AmberPTReader.py
#
# Update:
##
""" A collection of classes for parsing AMBER PT files.
"""
import sys
import os
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker

from wwpdb.utils.nmr.mr.LexerErrorListener import LexerErrorListener
from wwpdb.utils.nmr.mr.ParserErrorListener import ParserErrorListener
from wwpdb.utils.nmr.mr.AmberPTLexer import AmberPTLexer
from wwpdb.utils.nmr.mr.AmberPTParser import AmberPTParser
from wwpdb.utils.nmr.mr.AmberPTParserListener import AmberPTParserListener
from wwpdb.utils.nmr.mr.ParserListenerUtil import checkCoordinates
from wwpdb.utils.nmr.io.CifReader import CifReader
from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat


class AmberPTReader:
    """ Accessor methods for parsing AMBER PT files.
    """

    def __init__(self, verbose=True, log=sys.stdout, cR=None, polySeqModel=None,
                 ccU=None, csStat=None):
        self.__verbose = verbose
        self.__lfh = log

        if cR is not None and polySeqModel is None:
            dict = checkCoordinates(verbose, log, cR, polySeqModel, False)
            polySeqModel = dict['polymer_sequence']

        self.__cR = cR
        self.__polySeqModel = polySeqModel

        # CCD accessing utility
        self.__ccU = ChemCompUtil(verbose, log) if ccU is None else ccU

        # BMRB chemical shift statistics
        self.__csStat = BMRBChemShiftStat(verbose, log, self.__ccU) if csStat is None else csStat

    def parse(self, ptFilePath, cifFilePath):
        """ Parse AMBER PT file.
            @return: AmberPTParserListener for success or None otherwise.
        """

        try:

            if not os.access(ptFilePath, os.R_OK):
                if self.__verbose:
                    self.__lfh.write(f"AmberPTReader.parse() {ptFilePath} is not accessible.\n")
                return None

            if not os.access(cifFilePath, os.R_OK):
                if self.__verbose:
                    self.__lfh.write(f"AmberPTReader.parse() {cifFilePath} is not accessible.\n")
                return None

            if self.__cR is None:
                self.__cR = CifReader(self.__verbose, self.__lfh)
                if not self.__cR.parse(cifFilePath):
                    return None

            with open(ptFilePath) as ifp:

                ifs = InputStream(ifp.read())

                lexer = AmberPTLexer(ifs)
                lexer.removeErrorListeners()

                lexer_error_listener = LexerErrorListener(ptFilePath)
                lexer.addErrorListener(lexer_error_listener)

                messageList = lexer_error_listener.getMessageList()

                if messageList is not None:
                    for description in messageList:
                        self.__lfh.write(f"[Syntax error] line {description['line_number']}:{description['column_position']} {description['message']}\n")
                        if 'input' in description:
                            self.__lfh.write(f"{description['input']}\n")
                            self.__lfh.write(f"{description['marker']}\n")

                stream = CommonTokenStream(lexer)
                parser = AmberPTParser(stream)
                parser.removeErrorListeners()
                parser_error_listener = ParserErrorListener(ptFilePath)
                parser.addErrorListener(parser_error_listener)
                tree = parser.amber_pt()

                walker = ParseTreeWalker()
                listener = AmberPTParserListener(self.__verbose, self.__lfh, self.__cR, self.__polySeqModel,
                                                 self.__ccU, self.__csStat)
                walker.walk(listener, tree)

                messageList = parser_error_listener.getMessageList()

                if messageList is not None:
                    for description in messageList:
                        self.__lfh.write(f"[Syntax error] line {description['line_number']}:{description['column_position']} {description['message']}\n")
                        if 'input' in description:
                            self.__lfh.write(f"{description['input']}\n")
                            self.__lfh.write(f"{description['marker']}\n")

                if listener.warningMessage is not None:
                    print(listener.warningMessage)
                print(listener.getContentSubtype())

            return listener

        except IOError as e:
            if self.__verbose:
                self.__lfh.write(f"+AmberPTReader.parse() ++ Error - {str(e)}\n")
            return None


if __name__ == "__main__":
    reader = AmberPTReader(False)
    reader.parse('../../tests-nmr/mock-data-daother-7421/D_1292118884_mr-upload_P1.dat.V1',
                 '../../tests-nmr/mock-data-daother-7421/D_800450_model_P1.cif.V1')