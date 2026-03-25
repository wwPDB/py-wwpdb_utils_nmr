##
# File: PpmCSParserListener.py
# Date: 11-Apr-2025
#
# Updates:
""" ParserLister class for PPM CS files.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "1.1.1"

import sys
from typing import IO, List, Optional

from antlr4 import ParseTreeListener

try:
    from wwpdb.utils.nmr.nef.NefTranslator import NefTranslator
    from wwpdb.utils.nmr.cs.PpmCSParser import PpmCSParser
    from wwpdb.utils.nmr.cs.BaseCSParserListener import BaseCSParserListener
except ImportError:
    from nmr.nef.NefTranslator import NefTranslator
    from nmr.cs.PpmCSParser import PpmCSParser
    from nmr.cs.BaseCSParserListener import BaseCSParserListener


class PpmCSParserListener(ParseTreeListener, BaseCSParserListener):
    """ This class defines a complete listener for a parse tree produced by PpmCSParser.
    """
    __slots__ = ()

    __number = None

    def __init__(self, verbose: bool = True, log: IO = sys.stdout,
                 polySeq: List[dict] = None, entityAssembly: Optional[dict] = None,
                 nefT: NefTranslator = None,
                 reasons: Optional[dict] = None) -> None:
        super().__init__(verbose, log, polySeq, entityAssembly, nefT, reasons)

        self.file_type = 'nm-shi-ppm'

    def enterPpm_cs(self, ctx: PpmCSParser.Ppm_csContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by PpmCSParser#ppm_cs.
        """

        self.cur_list_id = max(self.cur_list_id, 0)
        self.cur_list_id += 1

        self.cur_line_num = 0

        self.chemShifts = 0
        self.offset = {}

    def exitPpm_cs(self, ctx: PpmCSParser.Ppm_csContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by PpmCSParser#ppm_cs.
        """

        self.exit()

    def enterPpm_list(self, ctx: PpmCSParser.Ppm_listContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by PpmCSParser#ppm_list.
        """

        self.cur_subtype = 'chem_shift'
        self.cur_line_num += 1

    def exitPpm_list(self, ctx: PpmCSParser.Ppm_listContext):
        """ Exit a parse tree produced by PpmCSParser#ppm_list.
        """

        chain_id = None

        if ctx.Simple_name():
            L = str(ctx.Simple_name())
        elif ctx.Atom_selection_2d_ex():
            L = str(ctx.Atom_selection_2d_ex())
        else:
            L = str(ctx.Atom_selection_3d_ex())
            chain_id = L.split(':', maxsplit=1)[0]

        value = self.__number

        if value is None:
            return

        self.atomSelectionSets.clear()

        dstFunc = self.validateCsValue(self.cur_line_num, value, None)

        if dstFunc is None:
            return

        assignment = self.extractAssignment(1, L, self.cur_line_num, chain_id)

        if assignment is None:
            return

        has_assignments, has_multiple_assignments = self.checkAssignment(self.cur_line_num, assignment)

        self.addCsRow(self.cur_line_num, dstFunc, has_assignments, has_multiple_assignments, {}, f'{L} -> ')

        self.chemShifts += 1

    def enterNumber(self, ctx: PpmCSParser.NumberContext):
        """ Enter a parse tree produced by PpmCSParser#number.
        """

        try:

            if ctx.Float():
                self.__number = float(str(ctx.Float()))

            elif ctx.Integer():
                self.__number = float(str(ctx.Integer()))

            else:
                self.__number = None

        except ValueError:
            self.__number = None

    def exitNumber(self, ctx: PpmCSParser.NumberContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by PpmCSParser#number.
        """
