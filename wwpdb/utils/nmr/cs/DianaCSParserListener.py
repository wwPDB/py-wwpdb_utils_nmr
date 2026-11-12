##
# File: DianaCSParserListener.py
# Date: 05-Nov-2026
#
# Updates:
""" ParserLister class for DIANA CS files.
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
    from wwpdb.utils.nmr.cs.DianaCSParser import DianaCSParser
    from wwpdb.utils.nmr.cs.BaseCSParserListener import BaseCSParserListener
except ImportError:
    from nmr.nef.NefTranslator import NefTranslator
    from nmr.cs.DianaCSParser import DianaCSParser
    from nmr.cs.BaseCSParserListener import BaseCSParserListener


class DianaCSParserListener(ParseTreeListener, BaseCSParserListener):
    """ This class defines a complete listener for a parse tree produced by DianaCSParser.
    """
    __slots__ = ()

    __atom_cs_dict = []

    def __init__(self, verbose: bool = True, log: IO = sys.stdout,
                 polySeq: List[dict] = None, entityAssembly: Optional[dict] = None,
                 nefT: NefTranslator = None,
                 reasons: Optional[dict] = None) -> None:
        super().__init__(verbose, log, polySeq, entityAssembly, nefT, reasons)

        self.file_type = 'nm-shi-dia'

    def enterDiana_cs(self, ctx: DianaCSParser.Diana_csContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by DianaCSParser#diana_cs.
        """

        self.cur_list_id = max(self.cur_list_id, 0)
        self.cur_list_id += 1

        self.cur_line_num = 0

        self.chemShifts = 0
        self.offset = {}

    def exitDiana_cs(self, ctx: DianaCSParser.Diana_csContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by DianaCSParser#diana_cs.
        """

        self.exit()

    def enterComment(self, ctx: DianaCSParser.CommentContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by DianaCSParser#comment.
        """

    def exitComment(self, ctx: DianaCSParser.CommentContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by DianaCSParser#comment.
        """

    def enterChemical_shifts(self, ctx: DianaCSParser.Chemical_shiftsContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by DianaCSParser#chemical_shifts.
        """

        self.cur_subtype = 'csp' if self.csp else 'chem_shift'
        self.cur_line_num += 1

    def exitChemical_shifts(self, ctx: DianaCSParser.Chemical_shiftsContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by DianaCSParser#chemical_shifts.
        """

    def enterChemical_shift(self, ctx: DianaCSParser.Chemical_shiftContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by DianaCSParser#chemical_shift.
        """

    def exitChemical_shift(self, ctx: DianaCSParser.Chemical_shiftContext):
        """ Exit a parse tree produced by DianaCSParser#chemical_shift.
        """

        try:

            comp_id = str(ctx.Simple_name(0))
            seq_id = int(str(ctx.Integer(0)))

            if len(self.__atom_cs_dict) == 0:
                return

            for atom_id, values in self.__atom_cs_dict:

                dstFunc = self.validateCsValue(self.cur_line_num, values[0], None)

                if dstFunc is None:
                    return

                len_vals = len(values)

                dstFunc2 = None

                if len_vals > 1:
                    dstFunc2 = self.validateCsValue(self.cur_line_num, values[1], None)

                    if dstFunc2 is None:
                        return

                self.atomSelectionSets.clear()

                L = f'{seq_id}:{comp_id}:{atom_id}'

                assignment = self.extractChemShiftAssignment(1, L, self.cur_line_num,
                                                             with_compid=comp_id, with_atomid=atom_id)

                if assignment is None:
                    continue

                has_assignments, has_multiple_assignments = self.checkAssignment(self.cur_line_num, assignment)

                len_atom_sel = len(self.atomSelectionSets[0][0]) if has_assignments else 0

                if dstFunc2 is None or not has_assignments and len_atom_sel == 1:
                    self.addCsRow(self.cur_line_num, dstFunc, has_assignments, has_multiple_assignments, {}, f'{L} -> ')

                else:

                    ambig_code = self.csStat.getMaxAmbigCodeWoSetId(comp_id, self.atomSelectionSets[0][0][0]['atom_id'])\
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

        finally:
            self.__atom_cs_dict.clear()

    def enterAtom_chemical_shift(self, ctx: DianaCSParser.Atom_chemical_shiftContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by DianaCSParser#atom_chemical_shift.
        """

    def exitAtom_chemical_shift(self, ctx: DianaCSParser.Atom_chemical_shiftContext):
        """ Exit a parse tree produced by DianaCSParser#atom_chemical_shift.
        """

        atom_id = str(ctx.Simple_name())

        values = [float(str(ctx.Float(0)))]
        if ctx.Float(1):
            values.append(float(str(ctx.Float(1))))

        self.__atom_cs_dict.append((atom_id, values))
