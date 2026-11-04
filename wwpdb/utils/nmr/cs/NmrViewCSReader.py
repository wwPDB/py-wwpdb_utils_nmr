##
# NmrViewCSReader.py
#
# Update:
##
""" A collection of classes for parsing NMRVIEW CS files.
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "1.2.0"

import os
import sys
from typing import IO, List, Optional, Tuple

from antlr4 import ParseTreeWalker

try:
    from wwpdb.utils.nmr.NmrDpConstant import MAX_ERROR_REPORT
    from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
    from wwpdb.utils.nmr.BmrbChemShiftStat import BmrbChemShiftStat
    from wwpdb.utils.nmr.nef.NefTranslator import NefTranslator
    from wwpdb.utils.nmr.AntlrParseUtil import parseAntlr
    from wwpdb.utils.nmr.cs import sa_nmrviewcs
    from wwpdb.utils.nmr.mr.LexerErrorListener import LexerErrorListener
    from wwpdb.utils.nmr.mr.ParserErrorListener import ParserErrorListener
    from wwpdb.utils.nmr.cs.NmrViewCSLexer import NmrViewCSLexer
    from wwpdb.utils.nmr.cs.NmrViewCSParser import NmrViewCSParser
    from wwpdb.utils.nmr.cs.NmrViewCSParserListener import NmrViewCSParserListener
except ImportError:
    from nmr.NmrDpConstant import MAX_ERROR_REPORT
    from nmr.ChemCompUtil import ChemCompUtil
    from nmr.BmrbChemShiftStat import BmrbChemShiftStat
    from nmr.nef.NefTranslator import NefTranslator
    from nmr.AntlrParseUtil import parseAntlr
    from nmr.cs import sa_nmrviewcs
    from nmr.mr.LexerErrorListener import LexerErrorListener
    from nmr.mr.ParserErrorListener import ParserErrorListener
    from nmr.cs.NmrViewCSLexer import NmrViewCSLexer
    from nmr.cs.NmrViewCSParser import NmrViewCSParser
    from nmr.cs.NmrViewCSParserListener import NmrViewCSParserListener


class NmrViewCSReader:
    """ Accessor methods for parsing NRMVIEW CS files.
    """
    __slots__ = ('__class_name__',
                 '__version__',
                 '__verbose',
                 '__log',
                 '__debug',
                 '__csp',
                 '__csLoops',
                 '__maxLexerErrorReport',
                 '__maxParserErrorReport',
                 '__polySeq',
                 '__entityAssembly',
                 '__ccU',
                 '__caC',
                 '__csStat',
                 '__nefT',
                 '__reasons')

    def __init__(self, verbose: bool = True, log: IO = sys.stdout,
                 polySeq: List[dict] = None, entityAssembly: Optional[dict] = None,
                 ccU: Optional[ChemCompUtil] = None, csStat: Optional[BmrbChemShiftStat] = None,
                 nefT: Optional[NefTranslator] = None,
                 reasons: Optional[dict] = None) -> None:
        self.__class_name__ = self.__class__.__name__
        self.__version__ = __version__

        self.__verbose = verbose
        self.__log = log
        self.__debug = False

        self.__csp = False
        self.__csLoops = None

        self.__maxLexerErrorReport = MAX_ERROR_REPORT
        self.__maxParserErrorReport = MAX_ERROR_REPORT

        self.__polySeq = polySeq
        # key=Entity_assembly_ID (str), value=dictionary of 'entity_id' (int) and 'auth_asym_id' (str)
        self.__entityAssembly = entityAssembly

        # CCD accessing utility
        self.__ccU = ChemCompUtil(verbose, log) if ccU is None else ccU

        # BMRB chemical shift statistics
        self.__csStat = BmrbChemShiftStat(verbose, log, self.__ccU) if csStat is None else csStat

        # NefTranslator
        self.__nefT = NefTranslator(verbose, log, self.__ccU, self.__csStat) if nefT is None else nefT
        if nefT is None:
            self.__nefT.set_remediation_mode(True)

        # reasons for re-parsing request from the previous trial
        self.__reasons = reasons

    def setDebugMode(self, debug: bool) -> None:
        """ Set debug mode.
        """

        self.__debug = debug

    def setCspMode(self, csp: bool) -> None:
        """ Set chemical shift perturbation mode.
        """

        self.__csp = csp

    def setCsloops(self, csLoops: Optional[List[dict]]) -> None:
        """ Set reference assigned chemical shifts for chemical shift perturbation mode.
        """

        self.__csLoops = csLoops

    def setLexerMaxErrorReport(self, maxErrReport: int) -> None:
        """ Set the maximum number of lexer error messages to save.
        """

        self.__maxLexerErrorReport = maxErrReport

    def setParserMaxErrorReport(self, maxErrReport: int) -> None:
        """ Set the maximum number of parser error messages to save.
        """

        self.__maxParserErrorReport = maxErrReport

    def parse(self, csFilePath: str, isFilePath: bool = True,
              createSfDict: bool = False, originalFileName: Optional[str] = None, listIdCounter: Optional[dict] = None,
              reservedListIds: Optional[dict] = None, entryId: Optional[str] = None
              ) -> Tuple[Optional[NmrViewCSParserListener], Optional[ParserErrorListener], Optional[LexerErrorListener]]:
        """ Parse NMRVIEW CS file.
            @return: NmrViewCSParserListener for success or None otherwise, ParserErrorListener, LexerErrorListener.
        """

        ifh = None

        try:

            if isFilePath:
                csString = None

                if not os.access(csFilePath, os.R_OK):
                    if self.__verbose:
                        self.__log.write(f"+{self.__class_name__}.parse() {csFilePath} is not accessible.\n")
                    return None, None, None

                ifh = open(csFilePath, 'r', encoding='utf-8', errors='ignore')  # pylint: disable=consider-using-with
                csText = ifh.read()

            else:
                csFilePath, csString = None, csFilePath

                if csString is None or len(csString) == 0:
                    if self.__verbose:
                        self.__log.write(f"+{self.__class_name__}.parse() Empty string.\n")
                    return None, None, None

                csText = csString

            tree, parser_error_listener, lexer_error_listener =\
                parseAntlr(NmrViewCSLexer, NmrViewCSParser, 'nmrview_cs', csText,
                           filePath=csFilePath, saModule=sa_nmrviewcs,
                           maxLexerErrorReport=self.__maxLexerErrorReport,
                           maxParserErrorReport=self.__maxParserErrorReport,
                           ignoreCodicError=True)

            messageList = lexer_error_listener.getMessageList()

            if messageList is not None and self.__verbose:
                for description in messageList:
                    self.__log.write(f"[Syntax error] line {description['line_number']}:{description['column_position']} "
                                     f"{description['message']}\n")
                    if 'input' in description:
                        self.__log.write(f"{description['input']}\n")
                        self.__log.write(f"{description['marker']}\n")

            walker = ParseTreeWalker()
            listener = NmrViewCSParserListener(self.__verbose, self.__log,
                                               self.__polySeq, self.__entityAssembly,
                                               self.__nefT,
                                               self.__reasons)
            listener.debug = self.__debug
            listener.csp = self.__csp
            listener.csLoops = self.__csLoops
            listener.createSfDict = createSfDict
            if createSfDict:
                if originalFileName is not None:
                    listener.originalFileName = originalFileName
                if listIdCounter is not None:
                    listener.listIdCounter = listIdCounter
                if reservedListIds is not None:
                    listener.reservedListIds = reservedListIds
                if entryId is not None:
                    listener.entryId = entryId
            walker.walk(listener, tree)

            messageList = parser_error_listener.getMessageList()

            if messageList is not None and self.__verbose:
                for description in messageList:
                    self.__log.write(f"[Syntax error] line {description['line_number']}:{description['column_position']} "
                                     f"{description['message']}\n")
                    if 'input' in description:
                        self.__log.write(f"{description['input']}\n")
                        self.__log.write(f"{description['marker']}\n")

            if self.__verbose and self.__debug:
                if listener.warningMessage is not None and len(listener.warningMessage) > 0:
                    self.__log.write(f"+{self.__class_name__}.parse() ++ Info  -\n" + '\n'.join(listener.warningMessage) + '\n')
                if isFilePath:
                    self.__log.write(f"+{self.__class_name__}.parse() ++ Info  - {listener.getContentSubtype()}\n")

            return listener, parser_error_listener, lexer_error_listener

        except IOError as e:
            if self.__verbose:
                self.__log.write(f"+{self.__class_name__}.parse() ++ Error  - {str(e)}\n")
            return None, None, None
        finally:
            if isFilePath and ifh is not None:
                ifh.close()


if __name__ == "__main__":
    nmr_poly_seq = [
                {
                  "chain_id": "1",
                  "auth_chain_id": "A",
                  "seq_id": [
                    101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113
                  ],
                  "comp_id": [
                    "DC", "DA", "DG", "DT", "DG", "DA", "DT", "DA", "DG", "DA", "DG", "DA", "DC"
                  ]
                },
                {
                  "chain_id": "2",
                  "auth_chain_id": "B",
                  "seq_id": [
                    114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126
                  ],
                  "comp_id": [
                    "DG", "DT", "DC", "DT", "DC", "DT", "DA", "DT", "DC", "DA", "DC", "DT", "DG"
                  ]
                },
                {
                  "chain_id": "3",
                  "auth_chain_id": "C",
                  "seq_id": [
                    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                    21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                    41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
                    61, 62, 63, 64, 65, 66
                  ],
                  "comp_id": [
                    "MET", "LYS", "ASN", "GLY", "GLU", "GLN", "ASN", "GLY", "PRO", "THR",
                    "THR", "CYS", "THR", "ASN", "CYS", "PHE", "THR", "GLN", "THR", "THR",
                    "PRO", "VAL", "TRP", "ARG", "ARG", "ASN", "PRO", "GLU", "GLY", "GLN",
                    "PRO", "LEU", "CYS", "ASN", "ALA", "CYS", "GLY", "LEU", "PHE", "LEU",
                    "LYS", "LEU", "HIS", "GLY", "VAL", "VAL", "ARG", "PRO", "LEU", "SER",
                    "LEU", "LYS", "THR", "ASP", "VAL", "ILE", "LYS", "LYS", "ARG", "ASN",
                    "ARG", "ASN", "SER", "ALA", "ASN", "SER"
                  ]
                }
              ]
    entity_assembly = {'1': {'entity_id': 1, 'auth_asym_id': 'A'},
                       '2': {'entity_id': 2, 'auth_asym_id': 'B'},
                       '3': {'entity_id': 3, 'auth_asym_id': 'C'}}
    reader = NmrViewCSReader(True, polySeq=nmr_poly_seq, entityAssembly=entity_assembly)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/6gat/nmrview_cs.txt')
