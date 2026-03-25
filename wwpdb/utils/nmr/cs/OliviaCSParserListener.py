##
# File: OliviaCSParserListener.py
# Date: 22-Aug-2025
#
# Updates:
""" ParserLister class for OLIVIA CS files.
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
    from wwpdb.utils.nmr.NmrDpConstant import (EMPTY_VALUE,
                                               STD_MON_DICT)
    from wwpdb.utils.nmr.nef.NEFTranslator import NEFTranslator
    from wwpdb.utils.nmr.cs.OliviaCSParser import OliviaCSParser
    from wwpdb.utils.nmr.cs.BaseCSParserListener import BaseCSParserListener
except ImportError:
    from nmr.NmrDpConstant import (EMPTY_VALUE,
                                   STD_MON_DICT)
    from nmr.nef.NEFTranslator import NEFTranslator
    from nmr.cs.OliviaCSParser import OliviaCSParser
    from nmr.cs.BaseCSParserListener import BaseCSParserListener


class OliviaCSParserListener(ParseTreeListener, BaseCSParserListener):
    """ This class defines a complete listener for a parse tree produced by OliviaCSParser.
    """
    __slots__ = ()

    __polySeq = None
    __entityAssembly = None

    def __init__(self, verbose: bool = True, log: IO = sys.stdout,
                 polySeq: List[dict] = None, entityAssembly: Optional[dict] = None,
                 nefT: NEFTranslator = None,
                 reasons: Optional[dict] = None) -> None:
        super().__init__(verbose, log, polySeq, entityAssembly, nefT, reasons)

        self.file_type = 'nm-shi-oli'
        self.software_name = 'Olivia'

    def enterOlivia_cs(self, ctx: OliviaCSParser.Olivia_csContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by OliviaCSParser#olivia_cs.
        """

    def exitOlivia_cs(self, ctx: OliviaCSParser.Olivia_csContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by OliviaCSParser#olivia_cs.
        """

        self.exit()

    def enterSequence(self, ctx: OliviaCSParser.SequenceContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by OliviaCSParser#sequence.
        """

        self.__polySeq = []
        self.__entityAssembly = {}
        self.offset = {}

    def exitSequence(self, ctx: OliviaCSParser.SequenceContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by OliviaCSParser#sequence.
        """

        if not self.hasPolySeq:

            self.polySeq = self.__polySeq
            self.entityAssembly = self.__entityAssembly
            self.hasPolySeq = True

            self.labelToAuthSeq = {}
            for ps in self.polySeq:
                chainId = ps['chain_id']
                for seqId in ps['seq_id']:
                    self.labelToAuthSeq[(chainId, seqId)] = (chainId, seqId)
            self.authToLabelSeq = {v: k for k, v in self.labelToAuthSeq.items()}

            self.chainIdSet = set(ps['chain_id'] for ps in self.polySeq)
            self.compIdSet = set()

            def is_data(array: list) -> bool:
                return not any(True for d in array if d in EMPTY_VALUE)

            for ps in self.polySeq:
                self.compIdSet.update(set(filter(is_data, ps['comp_id'])))

            for compId in self.compIdSet:
                if compId in STD_MON_DICT:
                    if len(compId) == 3:
                        self.polyPeptide = True
                    elif len(compId) == 2 and compId.startswith('D'):
                        self.polyDeoxyribonucleotide = True
                    elif len(compId) == 1:
                        self.polyRibonucleotide = True

    def enterResidue(self, ctx: OliviaCSParser.ResidueContext):
        """ Enter a parse tree produced by OliviaCSParser#residue.
        """

        chain_id = str(ctx.Simple_name(0))
        comp_id = str(ctx.Simple_name(1))
        seq_id = int(str(ctx.Integer()))

        ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chain_id), None)

        if ps is None:
            self.__polySeq.append({'chain_id': chain_id, 'seq_id': [], 'comp_id': []})
            ps = self.__polySeq[-1]
            entity_assembly_id = len(self.__polySeq)
            self.__entityAssembly[str(entity_assembly_id)] = {'entity_id': entity_assembly_id, 'auth_asym_id': chain_id}
            self.predictSequenceNumberOffsetByFirstResidue(chain_id, seq_id, comp_id)

        ps['seq_id'].append(seq_id)
        ps['comp_id'].append(comp_id)

    def exitResidue(self, ctx: OliviaCSParser.ResidueContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by OliviaCSParser#residue.
        """

    def enterChemical_shifts(self, ctx: OliviaCSParser.Chemical_shiftsContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by OliviaCSParser#chemical_shifts.
        """

        self.cur_list_id = max(self.cur_list_id, 0)
        self.cur_list_id += 1

        self.chemShifts = 0

        self.cur_subtype = 'chem_shift'

    def exitChemical_shifts(self, ctx: OliviaCSParser.Chemical_shiftsContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by OliviaCSParser#chemical_shifts.
        """

    def enterChemical_shift(self, ctx: OliviaCSParser.Chemical_shiftContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by OliviaCSParser#chemical_shift.
        """

        self.chemShifts += 1

    def exitChemical_shift(self, ctx: OliviaCSParser.Chemical_shiftContext):
        """ Exit a parse tree produced by OliviaCSParser#chemical_shift.
        """

        try:

            if len(self.anySelection) == 0:
                self.chemShifts -= 1
                return

            index = self.chemShifts

            try:

                chain_id = str(ctx.Simple_name(0))
                comp_id = str(ctx.Simple_name(1))
                atom_id = str(ctx.Simple_name(2))
                seq_id = int(str(ctx.Integer()))

                value = self.anySelection[0]
                val_err = self.anySelection[1]

            except (IndexError, ValueError):
                self.chemShifts -= 1
                return

            if value is None:
                self.chemShifts -= 1
                return

            if len(comp_id) == 1 and not self.polyRibonucleotide and not self.polyDeoxyribonucleotide and self.polyPeptide:
                comp_id = next((_comp_id for _comp_id in self.compIdSet
                                if _comp_id in STD_MON_DICT and STD_MON_DICT[_comp_id] == comp_id), comp_id)

            self.atomSelectionSets.clear()

            dstFunc = self.validateCsValue(index, value, val_err)

            if dstFunc is None:
                self.chemShifts -= 1
                return

            _seq_id = seq_id

            auth_seq_id_map = {}

            self.predictSequenceNumberOffsetByFirstResidue(chain_id, _seq_id, comp_id)

            if chain_id in self.offset:
                seq_id += self.offset[chain_id]
                auth_seq_id_map[seq_id] = _seq_id

            L = f'{chain_id}:{seq_id}:{comp_id}:{atom_id}'

            assignment = self.extractAssignment(1, L, index, chain_id, comp_id)

            if assignment is None:
                self.chemShifts -= 1
                return

            has_assignments, has_multiple_assignments = self.checkAssignment(index, assignment)

            self.addCsRow(index, dstFunc, has_assignments, has_multiple_assignments, auth_seq_id_map,
                          f'{L} -> ')

        finally:
            self.anySelection.clear()

    def enterNumber(self, ctx: OliviaCSParser.NumberContext):
        """ Enter a parse tree produced by OliviaCSParser#number.
        """

        if ctx.Float():
            self.anySelection.append(float(str(ctx.Float())))

        elif ctx.Real():
            self.anySelection.append(float(str(ctx.Real())))

        elif ctx.Integer():
            self.anySelection.append(float(str(ctx.Integer())))

        else:
            self.anySelection.append(None)

    def exitNumber(self, ctx: OliviaCSParser.NumberContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by OliviaCSParser#number.
        """

    def enterComment(self, ctx: OliviaCSParser.CommentContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by OliviaCSParser#comment.
        """

    def exitComment(self, ctx: OliviaCSParser.CommentContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by OliviaCSParser#comment.
        """
