##
# File: NmrViewCSParserListener.py
# Date: 04-Nov-2026
#
# Updates:
""" ParserLister class for NMRVIEW CS files.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "1.2.0"

import copy
import sys
from typing import IO, List, Optional

from antlr4 import ParseTreeListener

try:
    from wwpdb.utils.nmr.nef.NefTranslator import NefTranslator
    from wwpdb.utils.nmr.cs.NmrViewCSParser import NmrViewCSParser
    from wwpdb.utils.nmr.cs.BaseCSParserListener import BaseCSParserListener
except ImportError:
    from nmr.nef.NefTranslator import NefTranslator
    from nmr.cs.NmrViewCSParser import NmrViewCSParser
    from nmr.cs.BaseCSParserListener import BaseCSParserListener


class NmrViewCSParserListener(ParseTreeListener, BaseCSParserListener):
    """ This class defines a complete listener for a parse tree produced by NmrViewCSParser.
    """
    __slots__ = ()

    __seq_id = None
    __comp_id = None

    def __init__(self, verbose: bool = True, log: IO = sys.stdout,
                 polySeq: List[dict] = None, entityAssembly: Optional[dict] = None,
                 nefT: NefTranslator = None,
                 reasons: Optional[dict] = None) -> None:
        super().__init__(verbose, log, polySeq, entityAssembly, nefT, reasons)

        self.file_type = 'nm-shi-vie'

    def enterNmrview_cs(self, ctx: NmrViewCSParser.Nmrview_csContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by NmrViewCSParser#nmrview_cs.
        """

        self.cur_list_id = max(self.cur_list_id, 0)
        self.cur_list_id += 1

        self.cur_line_num = 0

        self.chemShifts = 0
        self.offset = {}

    def exitNmrview_cs(self, ctx: NmrViewCSParser.Nmrview_csContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by NmrViewCSParser#nmrview_cs.
        """

        self.exit()

    def enterRes_def_list(self, ctx: NmrViewCSParser.Res_def_listContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by NmrViewCSParser#res_def_list.
        """

    def exitRes_def_list(self, ctx: NmrViewCSParser.Res_def_listContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by NmrViewCSParser#res_def_list.
        """

    def enterRes_id_def(self, ctx: NmrViewCSParser.Res_id_defContext):
        """ Enter a parse tree produced by NmrViewCSParser#res_id_def.
        """

        self.__seq_id = int(str(ctx.Integer()))

    def exitRes_id_def(self, ctx: NmrViewCSParser.Res_id_defContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by NmrViewCSParser#res_id_def.
        """

    def enterRes_type_def(self, ctx: NmrViewCSParser.Res_type_defContext):
        """ Enter a parse tree produced by NmrViewCSParser#res_type_def.
        """

        self.__comp_id = str(ctx.Simple_name())

    def exitRes_type_def(self, ctx: NmrViewCSParser.Res_type_defContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by NmrViewCSParser#res_type_def.
        """

    def enterPrev_type_def(self, ctx: NmrViewCSParser.Prev_type_defContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by NmrViewCSParser#prev_type_def.
        """

    def exitPrev_type_def(self, ctx: NmrViewCSParser.Prev_type_defContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by NmrViewCSParser#prev_type_def.
        """

    def enterSpin_system_def(self, ctx: NmrViewCSParser.Spin_system_defContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by NmrViewCSParser#spin_system_def.
        """

    def exitSpin_system_def(self, ctx: NmrViewCSParser.Spin_system_defContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by NmrViewCSParser#spin_system_def.
        """

    def enterHeterogeneity_def(self, ctx: NmrViewCSParser.Heterogeneity_defContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by NmrViewCSParser#heterogeneity_def.
        """

    def exitHeterogeneity_def(self, ctx: NmrViewCSParser.Heterogeneity_defContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by NmrViewCSParser#heterogeneity_def.
        """

    def enterShift_list(self, ctx: NmrViewCSParser.Shift_listContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by NmrViewCSParser#shift_list.
        """

        self.cur_subtype = 'csp' if self.csp else 'chem_shift'
        self.cur_line_num += 1

    def exitShift_list(self, ctx: NmrViewCSParser.Shift_listContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by NmrViewCSParser#shift_list.
        """

        L = f'{self.__seq_id}:{self.__comp_id}:{str(ctx.Simple_name())}'

        values = [float(str(ctx.Float(0)))]
        if ctx.Float(1):
            values.append(float(str(ctx.Float(1))))

        self.atomSelectionSets.clear()

        dstFunc = self.validateCsValue(self.cur_line_num, values[0], None)

        if dstFunc is None:
            return

        len_vals = len(values)

        dstFunc2 = None

        if len_vals > 1:
            dstFunc2 = self.validateCsValue(self.cur_line_num, values[1], None)

            if dstFunc2 is None:
                return

        assignment = self.extractChemShiftAssignment(1, L, self.cur_line_num, with_compid=self.__comp_id)

        if assignment is None:
            return

        has_assignments, has_multiple_assignments = self.checkAssignment(self.cur_line_num, assignment)

        len_atom_sel = len(self.atomSelectionSets[0][0]) if has_assignments else 0

        if dstFunc2 is None or not has_assignments and len_atom_sel == 1:
            self.addCsRow(self.cur_line_num, dstFunc, has_assignments, has_multiple_assignments, {}, f'{L} -> ')

        else:

            ambig_code = self.csStat.getMaxAmbigCodeWoSetId(self.__comp_id, self.atomSelectionSets[0][0][0]['atom_id'])\
                if has_assignments else None

            atomSelectionSet1 = atomSelectionSet2 = None

            if len_atom_sel > 0:
                atomSelectionSet1 = copy.copy(self.atomSelectionSets[0][0][0:len_atom_sel // 2])
                atomSelectionSet2 = copy.copy(self.atomSelectionSets[0][0][len_atom_sel // 2:])

                self.atomSelectionSets[0][0] = atomSelectionSet1

            self.addCsRow(self.cur_line_num, dstFunc, has_assignments, has_multiple_assignments, {}, f'{L} -> ',
                          default_ambig_code=ambig_code)

            if has_assignments:
                self.chemShifts += 1

                self.atomSelectionSets[0][0] = atomSelectionSet2

                self.addCsRow(self.cur_line_num, dstFunc2, has_assignments, has_multiple_assignments, {}, f'{L} -> ',
                              default_ambig_code=ambig_code)

        self.chemShifts += 1
