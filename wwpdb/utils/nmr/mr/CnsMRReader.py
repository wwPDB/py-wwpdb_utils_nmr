##
# CnsMRReader.py
#
# Update:
##
""" A collection of classes for parsing CNS MR files.
"""
import sys
import os
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker

from wwpdb.utils.nmr.mr.LexerErrorListener import LexerErrorListener
from wwpdb.utils.nmr.mr.ParserErrorListener import ParserErrorListener
from wwpdb.utils.nmr.mr.CnsMRLexer import CnsMRLexer
from wwpdb.utils.nmr.mr.CnsMRParser import CnsMRParser
from wwpdb.utils.nmr.mr.CnsMRParserListener import CnsMRParserListener
from wwpdb.utils.nmr.mr.ParserListenerUtil import checkCoordinates
from wwpdb.utils.nmr.io.CifReader import CifReader
from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
from wwpdb.utils.nmr.NEFTranslator.NEFTranslator import NEFTranslator


class CnsMRReader:
    """ Accessor methods for parsing CNS MR files.
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
        """ Parse CNS MR file.
            @return: CnsMRParserListener for success or None otherwise.
        """

        try:

            if not os.access(mrFilePath, os.R_OK):
                if self.__verbose:
                    self.__lfh.write(f"CnsMRReader.parse() {mrFilePath} is not accessible.\n")
                return None

            if not os.access(cifFilePath, os.R_OK):
                if self.__verbose:
                    self.__lfh.write(f"CnsMRReader.parse() {cifFilePath} is not accessible.\n")
                return None

            if self.__cR is None:
                self.__cR = CifReader(self.__verbose, self.__lfh)
                if not self.__cR.parse(cifFilePath):
                    return None

            with open(mrFilePath) as ifp:

                ifs = InputStream(ifp.read())

                lexer = CnsMRLexer(ifs)
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
                parser = CnsMRParser(stream)
                parser.removeErrorListeners()
                parser_error_listener = ParserErrorListener(mrFilePath)
                parser.addErrorListener(parser_error_listener)
                tree = parser.cns_mr()

                walker = ParseTreeWalker()
                listener = CnsMRParserListener(self.__verbose, self.__lfh, self.__cR, self.__polySeqModel,
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
                self.__lfh.write(f"+CnsMRReader.parse() ++ Error - {str(e)}\n")
            return None


if __name__ == "__main__":
    reader = CnsMRReader(False)
    reader.parse('../../tests-nmr/mock-data-pdbstat/atom_sel_expr_example.txt',
                 '../../tests-nmr/mock-data-pdbstat/6pvr.cif')