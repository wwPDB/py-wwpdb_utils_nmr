##
# CyanaMRReader.py
#
# Update:
##
""" A collection of classes for parsing CYANA MR files.
"""
import sys
import os
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker

from wwpdb.utils.nmr.mr.LexerErrorListener import LexerErrorListener
from wwpdb.utils.nmr.mr.ParserErrorListener import ParserErrorListener
from wwpdb.utils.nmr.mr.CyanaMRLexer import CyanaMRLexer
from wwpdb.utils.nmr.mr.CyanaMRParser import CyanaMRParser
from wwpdb.utils.nmr.mr.CyanaMRParserListener import CyanaMRParserListener
from wwpdb.utils.nmr.mr.ParserListenerUtil import checkCoordinates
from wwpdb.utils.nmr.io.CifReader import CifReader
from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
from wwpdb.utils.nmr.NEFTranslator.NEFTranslator import NEFTranslator


class CyanaMRReader:
    """ Accessor methods for parsing CYANA MR files.
    """

    def __init__(self, verbose=True, log=sys.stdout, cR=None, polySeqModel=None,
                 ccU=None, csStat=None, nefT=None):
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

        # NEFTranslator
        self.__nefT = NEFTranslator(verbose, log, self.__ccU, self.__csStat) if nefT is None else nefT

    def parse(self, mrFilePath, cifFilePath):
        """ Parse CYANA MR file.
            @return: CyanaMRParserListener for success or None otherwise.
        """

        try:

            if not os.access(mrFilePath, os.R_OK):
                if self.__verbose:
                    self.__lfh.write(f"CyanaMRReader.parse() {mrFilePath} is not accessible.\n")
                return None

            if not os.access(cifFilePath, os.R_OK):
                if self.__verbose:
                    self.__lfh.write(f"CyanaMRReader.parse() {cifFilePath} is not accessible.\n")
                return None

            if self.__cR is None:
                self.__cR = CifReader(self.__verbose, self.__lfh)
                if not self.__cR.parse(cifFilePath):
                    return None

            with open(mrFilePath) as ifp:

                ifs = InputStream(ifp.read())

                lexer = CyanaMRLexer(ifs)
                lexer.removeErrorListeners()

                lexer_error_listener = LexerErrorListener(mrFilePath)
                lexer.addErrorListener(lexer_error_listener)

                messageList = lexer_error_listener.getMessageList()

                if messageList is not None:
                    for description in messageList:
                        self.__lfh.write(f"[Syntax error] line {description['line_number']}:{description['column_position']} {description['message']}\n")
                        if 'input' in description:
                            self.__lfh.write(f"{description['input']}\n")
                            self.__lfh.write(f"{description['marker']}\n")

                stream = CommonTokenStream(lexer)
                parser = CyanaMRParser(stream)
                parser.removeErrorListeners()
                parser_error_listener = ParserErrorListener(mrFilePath)
                parser.addErrorListener(parser_error_listener)
                tree = parser.cyana_mr()

                walker = ParseTreeWalker()
                listener = CyanaMRParserListener(self.__verbose, self.__lfh, self.__cR, self.__polySeqModel,
                                                 self.__ccU, self.__csStat, self.__nefT)
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
                self.__lfh.write(f"+CyanaMRReader.parse() ++ Error - {str(e)}\n")
            return None


if __name__ == "__main__":
    reader = CyanaMRReader(False)
    reader.parse('../../tests-nmr/mock-data-daother-5829/D_1000249951_mr-upload_P1.cyana.V1',
                 '../../tests-nmr/mock-data-daother-5829/D_800467_model_P1.cif.V3')