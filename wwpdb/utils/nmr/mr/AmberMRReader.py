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

from wwpdb.utils.nmr.mr.LexerErrorListener import LexerErrorListener
from wwpdb.utils.nmr.mr.ParserErrorListener import ParserErrorListener
from wwpdb.utils.nmr.mr.AmberMRLexer import AmberMRLexer
from wwpdb.utils.nmr.mr.AmberMRParser import AmberMRParser
from wwpdb.utils.nmr.mr.AmberMRParserListener import AmberMRParserListener
from wwpdb.utils.nmr.io.CifReader import CifReader


class AmberMRReader:
    """ Accessor methods for parsing AMBER MR files.
    """

    def __init__(self, verbose=True, log=sys.stdout):
        self.__verbose = verbose
        self.__lfh = log

        self.__mrFilePath = None
        self.__cifFilePath = None

        # CIF reader
        self.__cR = CifReader(verbose, log)

    def parse(self, mrFilePath, cifFilePath):
        """ Parse AMBER MR file.
            @return: True for success or False otherwise.
        """

        self.__mrFilePath = mrFilePath
        self.__cifFilePath = cifFilePath

        try:

            if not os.access(mrFilePath, os.R_OK):
                if self.__verbose:
                    self.__lfh.write(f"AmberMRReader.parse() {mrFilePath} is not accessible.\n")
                return False

            if not os.access(cifFilePath, os.R_OK):
                if self.__verbose:
                    self.__lfh.write(f"AmberMRReader.parse() {cifFilePath} is not accessible.\n")
                return False

            if not self.__cR.parse(cifFilePath):
                return False

            with open(mrFilePath) as ifp:

                ifs = InputStream(ifp.read())

                lexer = AmberMRLexer(ifs)
                lexer.removeErrorListeners()

                lexer_error_listener = LexerErrorListener(self.__mrFilePath)
                lexer.addErrorListener(lexer_error_listener)

                messageList = lexer_error_listener.getMessageList()

                if messageList is not None:
                    for description in messageList:
                        self.__lfh.write(f"[Syntax error] line {description['line_number']}:{description['column_position']} {description['message']}\n")
                        if 'input' in description:
                            self.__lfh.write(f"{description['input']}\n")
                            self.__lfh.write(f"{description['marker']}\n")

                stream = CommonTokenStream(lexer)
                parser = AmberMRParser(stream)
                parser.removeErrorListeners()
                parser_error_listener = ParserErrorListener(self.__mrFilePath)
                parser.addErrorListener(parser_error_listener)
                tree = parser.amber_mr()

                walker = ParseTreeWalker()
                listener = AmberMRParserListener(self.__verbose, self.__lfh, self.__cR)
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
                self.__lfh.write(f"+AmberMRReader.parse() ++ Error - {str(e)}\n")
            return False


if __name__ == "__main__":
    reader = AmberMRReader(False)
    reader.parse('../../tests-nmr/mock-data-daother-7421/D_1292118884_mr-upload_P1.amber.V1',
                 '../../tests-nmr/mock-data-daother-7421/D_800450_model_P1.cif.V1')
