##
# RosettaMRReader.py
#
# Update:
##
""" A collection of classes for parsing ROSETTA MR files.
"""
import sys
import os
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker

try:
    from wwpdb.utils.nmr.mr.LexerErrorListener import LexerErrorListener
    from wwpdb.utils.nmr.mr.ParserErrorListener import ParserErrorListener
    from wwpdb.utils.nmr.mr.RosettaMRLexer import RosettaMRLexer
    from wwpdb.utils.nmr.mr.RosettaMRParser import RosettaMRParser
    from wwpdb.utils.nmr.mr.RosettaMRParserListener import RosettaMRParserListener
    from wwpdb.utils.nmr.mr.ParserListenerUtil import checkCoordinates
    from wwpdb.utils.nmr.io.CifReader import CifReader
    from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
    from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from wwpdb.utils.nmr.NEFTranslator.NEFTranslator import NEFTranslator
except ImportError:
    from nmr.mr.LexerErrorListener import LexerErrorListener
    from nmr.mr.ParserErrorListener import ParserErrorListener
    from nmr.mr.RosettaMRLexer import RosettaMRLexer
    from nmr.mr.RosettaMRParser import RosettaMRParser
    from nmr.mr.RosettaMRParserListener import RosettaMRParserListener
    from nmr.mr.ParserListenerUtil import checkCoordinates
    from nmr.io.CifReader import CifReader
    from nmr.ChemCompUtil import ChemCompUtil
    from nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from nmr.NEFTranslator.NEFTranslator import NEFTranslator


class RosettaMRReader:
    """ Accessor methods for parsing ROSETTA MR files.
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

    def parse(self, mrFilePath, cifFilePath=None):
        """ Parse ROSETTA MR file.
            @return: RosettaMRParserListener for success or None otherwise.
        """

        try:

            if not os.access(mrFilePath, os.R_OK):
                if self.__verbose:
                    self.__lfh.write(f"RosettaMRReader.parse() {mrFilePath} is not accessible.\n")
                return None

            if cifFilePath is not None:
                if not os.access(cifFilePath, os.R_OK):
                    if self.__verbose:
                        self.__lfh.write(f"RosettaMRReader.parse() {cifFilePath} is not accessible.\n")
                    return None

                if self.__cR is None:
                    self.__cR = CifReader(self.__verbose, self.__lfh)
                    if not self.__cR.parse(cifFilePath):
                        return None

            with open(mrFilePath) as ifp:

                ifs = InputStream(ifp.read())

                lexer = RosettaMRLexer(ifs)
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
                parser = RosettaMRParser(stream)
                parser.removeErrorListeners()
                parser_error_listener = ParserErrorListener(mrFilePath)
                parser.addErrorListener(parser_error_listener)
                tree = parser.rosetta_mr()

                walker = ParseTreeWalker()
                listener = RosettaMRParserListener(self.__verbose, self.__lfh, self.__cR, self.__polySeqModel,
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
                self.__lfh.write(f"+RosettaMRReader.parse() ++ Error - {str(e)}\n")
            return None


if __name__ == "__main__":
    reader = RosettaMRReader(False)
    reader.parse('../../tests-nmr/mock-data-daother-7690/Sa1_v90t_30C_noe.txt',
                 '../../tests-nmr/mock-data-daother-7690/pdb_extract_17960.cif')
