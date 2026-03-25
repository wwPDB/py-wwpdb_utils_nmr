##
# File: PippCSParserListener.py
# Date: 11-Apr-2025
#
# Updates:
""" ParserLister class for PIPP CS files.
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
    from wwpdb.utils.nmr.nef.NEFTranslator import NEFTranslator
    from wwpdb.utils.nmr.cs.PippCSParser import PippCSParser
    from wwpdb.utils.nmr.cs.BaseCSParserListener import BaseCSParserListener
except ImportError:
    from nmr.nef.NEFTranslator import NEFTranslator
    from nmr.cs.PippCSParser import PippCSParser
    from nmr.cs.BaseCSParserListener import BaseCSParserListener


class PippCSParserListener(ParseTreeListener, BaseCSParserListener):
    """ This class defines a complete listener for a parse tree produced by PippCSParser.
    """
    __slots__ = ()

    __seq_id = None
    __comp_id = None
    __number = None

    def __init__(self, verbose: bool = True, log: IO = sys.stdout,
                 polySeq: List[dict] = None, entityAssembly: Optional[dict] = None,
                 nefT: NEFTranslator = None,
                 reasons: Optional[dict] = None) -> None:
        super().__init__(verbose, log, polySeq, entityAssembly, nefT, reasons)

        self.file_type = 'nm-shi-pip'
        self.software_name = 'PIPP'

    def enterPipp_cs(self, ctx: PippCSParser.Pipp_csContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by PippCSParser#pipp_cs.
        """

    def exitPipp_cs(self, ctx: PippCSParser.Pipp_csContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by PippCSParser#pipp_cs.
        """

        self.exit()

    def enterPipp_format(self, ctx: PippCSParser.Pipp_formatContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by PippCSParser#pipp_format.
        """

        self.cur_list_id = max(self.cur_list_id, 0)
        self.cur_list_id += 1

        self.chemShifts = 0
        self.offset = {}

        self.cur_subtype = 'chem_shift'

        self.predictSequenceNumberOffsetByFirstResidue(None, int(str(ctx.Integer())), None)

    def exitPipp_format(self, ctx: PippCSParser.Pipp_formatContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by PippCSParser#pipp_format.
        """

    def enterExt_peak_pick_tbl(self, ctx: PippCSParser.Ext_peak_pick_tblContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by PippCSParser#ext_peak_pick_tbl.
        """

    def exitExt_peak_pick_tbl(self, ctx: PippCSParser.Ext_peak_pick_tblContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by PippCSParser#ext_peak_pick_tbl.
        """

    def enterExt_peak_pick_tbl_row(self, ctx: PippCSParser.Ext_peak_pick_tbl_rowContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by PippCSParser#ext_peak_pick_tbl_row.
        """

    def exitExt_peak_pick_tbl_row(self, ctx: PippCSParser.Ext_peak_pick_tbl_rowContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by PippCSParser#ext_peak_pick_tbl_row.
        """

    def enterResidue_list(self, ctx: PippCSParser.Residue_listContext):
        """ Enter a parse tree produced by PippCSParser#residue_list.
        """

        self.__seq_id = int(str(ctx.Integer(0)))
        self.__comp_id = str(ctx.Simple_name())

    def exitResidue_list(self, ctx: PippCSParser.Residue_listContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by PippCSParser#residue_list.
        """

    def enterShift_list(self, ctx: PippCSParser.Shift_listContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by PippCSParser#shift_list.
        """

    def exitShift_list(self, ctx: PippCSParser.Shift_listContext):
        """ Exit a parse tree produced by PippCSParser#shift_list.
        """

        index = self.chemShifts + 1

        value = self.__number

        if value is None:
            return

        self.atomSelectionSets.clear()

        dstFunc = self.validateCsValue(index, value, None)

        if dstFunc is None:
            return

        auth_seq_id_map = {}

        seq_id = self.__seq_id
        if None in self.offset:
            seq_id += self.offset[None]
            auth_seq_id_map[seq_id] = self.__seq_id

        atom_ids = str(ctx.Simple_name(0)).split('|')

        max_ambig_code = None

        if len(atom_ids) > 1:
            max_ambig_code = 0

            for atom_id in atom_ids:

                L = f'{seq_id}:{self.__comp_id}:{atom_id}'

                assignment = self.extractAssignment(1, L, index, with_compid=self.__comp_id)

                if assignment is None:
                    continue

                _atom = assignment[0]  # pylint: disable=unsubscriptable-object
                ambig_code = self.csStat.getMaxAmbigCodeWoSetId(_atom['comp_id'], _atom['atom_id'])
                max_ambig_code = max(max_ambig_code, ambig_code)
                if max_ambig_code < 2:
                    max_ambig_code = 4

        L = f'{seq_id}:{self.__comp_id}:{atom_ids[0]}'

        assignment = self.extractAssignment(1, L, index, with_compid=self.__comp_id)

        if assignment is None:
            return

        has_assignments, has_multiple_assignments = self.checkAssignment(index, assignment)

        self.addCsRow(index, dstFunc, has_assignments, has_multiple_assignments, auth_seq_id_map,
                      f'{L} -> ', None, max_ambig_code)

        self.chemShifts += 1

    def enterNumber(self, ctx: PippCSParser.NumberContext):
        """ Enter a parse tree produced by PippCSParser#number.
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

    def exitNumber(self, ctx: PippCSParser.NumberContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by PippCSParser#number.
        """
