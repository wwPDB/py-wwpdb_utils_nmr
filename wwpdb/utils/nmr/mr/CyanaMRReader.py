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
from wwpdb.utils.nmr.io.CifReader import CifReader


class CyanaMRReader:
    """ Accessor methods for parsing CYANA MR files.
    """

    def __init__(self, verbose=True, log=sys.stdout):
        self.__verbose = verbose
        self.__lfh = log

        # CIF reader
        self.__cR = CifReader(verbose, log)

    def parse(self, mrFilePath, cifFilePath):
        """ Parse CYANA MR file.
            @return: True for success or False otherwise.
        """

        try:

            if not os.access(mrFilePath, os.R_OK):
                if self.__verbose:
                    self.__lfh.write(f"CyanaMRReader.parse() {mrFilePath} is not accessible.\n")
                return False

            if not os.access(cifFilePath, os.R_OK):
                if self.__verbose:
                    self.__lfh.write(f"CyanaMRReader.parse() {cifFilePath} is not accessible.\n")
                return False

            if not self.__cR.parse(cifFilePath):
                return False

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
                listener = CyanaMRParserListener(self.__verbose, self.__lfh, self.__cR)
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

            return True

        except IOError as e:
            if self.__verbose:
                self.__lfh.write(f"+CyanaMRReader.parse() ++ Error - {str(e)}\n")
            return False


if __name__ == "__main__":
    reader = CyanaMRReader(False)
    reader.parse('../../tests-nmr/mock-data-daother-5829/D_1000249951_mr-upload_P1.cyana.V1',
                 '../../tests-nmr/mock-data-daother-5829/D_800467_model_P1.cif.V3')
