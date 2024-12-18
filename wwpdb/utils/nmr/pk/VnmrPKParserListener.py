##
# File: VnmrPKParserListener.py
# Date: 16-Dec-2024
#
# Updates:
""" ParserLister class for VNMR PK files.
    @author: Masashi Yokochi
"""
import sys
import copy
import re

from itertools import zip_longest
from antlr4 import ParseTreeListener

try:
    from wwpdb.utils.nmr.pk.VnmrPKParser import VnmrPKParser
    from wwpdb.utils.nmr.pk.BasePKParserListener import BasePKParserListener
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (REPRESENTATIVE_MODEL_ID,
                                                       REPRESENTATIVE_ALT_ID,
                                                       SPECTRAL_DIM_TEMPLATE,
                                                       ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS,
                                                       getPkRow,
                                                       getPkGenCharRow,
                                                       getPkCharRow,
                                                       getPkChemShiftRow)
    from wwpdb.utils.nmr.AlignUtil import emptyValue

except ImportError:
    from nmr.pk.VnmrPKParser import VnmrPKParser
    from nmr.pk.BasePKParserListener import BasePKParserListener
    from nmr.mr.ParserListenerUtil import (REPRESENTATIVE_MODEL_ID,
                                           REPRESENTATIVE_ALT_ID,
                                           SPECTRAL_DIM_TEMPLATE,
                                           ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS,
                                           getPkRow,
                                           getPkGenCharRow,
                                           getPkCharRow,
                                           getPkChemShiftRow)
    from nmr.AlignUtil import emptyValue


# This class defines a complete listener for a parse tree produced by VnmrPKParser.
class VnmrPKParserListener(ParseTreeListener, BasePKParserListener):

    __spectrum_names = None
    __has_volume = False
    __has_line_width = False
    __has_assign = False

    def __init__(self, verbose=True, log=sys.stdout,
                 representativeModelId=REPRESENTATIVE_MODEL_ID,
                 representativeAltId=REPRESENTATIVE_ALT_ID,
                 mrAtomNameMapping=None,
                 cR=None, caC=None, ccU=None, csStat=None, nefT=None,
                 reasons=None):
        super().__init__(verbose, log, representativeModelId, representativeAltId,
                         mrAtomNameMapping, cR, caC, ccU, csStat, nefT, reasons)

        self.file_type = 'nm-pea-vnm'
        self.software_name = 'VNMR'

    # Enter a parse tree produced by VnmrPKParser#vnmr_pk.
    def enterVnmr_pk(self, ctx: VnmrPKParser.Vnmr_pkContext):  # pylint: disable=unused-argument
        self.__spectrum_names = {}

        self.enter()

    # Exit a parse tree produced by VnmrPKParser#vnmr_pk.
    def exitVnmr_pk(self, ctx: VnmrPKParser.Vnmr_pkContext):  # pylint: disable=unused-argument
        self.exit(self.__spectrum_names if len(self.__spectrum_names) > 0 else None)

    # Enter a parse tree produced by VnmrPKParser#comment.
    def enterComment(self, ctx: VnmrPKParser.CommentContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by VnmrPKParser#comment.
    def exitComment(self, ctx: VnmrPKParser.CommentContext):
        comment = []
        for col in range(20):
            if ctx.Any_name(col):
                text = str(ctx.Any_name(col))
                if text[0] in ('#', '!'):
                    break
                if text[0] in ('>', '<'):
                    continue
                comment.append(str(ctx.Any_name(col)))
            else:
                break
        last_comment = None if len(comment) == 0 else ' '.join(comment)

        if last_comment is None:
            return

        if last_comment.startswith('Spectrum: '):
            self.spectrum_name = last_comment.split()[1]

        elif last_comment.startswith('X-Axis: '):
            axis_names = last_comment.split(',')

            self.num_of_dim = len(axis_names)
            labels = [n.split()[1] for n in axis_names]

            for _dim_id, _axis_code in enumerate(labels, start=1):

                if _dim_id not in self.cur_spectral_dim:
                    cur_spectral_dim = copy.copy(SPECTRAL_DIM_TEMPLATE)
                else:
                    cur_spectral_dim = self.cur_spectral_dim[_dim_id]

                cur_spectral_dim['axis_code'] = _axis_code

                digits = re.findall(r'\d+', _axis_code)
                for digit in digits:
                    num = int(digit)
                    nuc = next((k for k, v in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS.items() if num == v[0]), None)
                    if nuc is not None:
                        cur_spectral_dim['atom_type'] = nuc
                        cur_spectral_dim['atom_isotope_number'] = num
                        break
                if cur_spectral_dim['atom_type'] is None:
                    for a in _axis_code:
                        a = a.upper()
                        if a in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS:
                            cur_spectral_dim['atom_type'] = a
                            cur_spectral_dim['atom_isotope_number'] = ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS[a][0]
                            break

                isotope_number = cur_spectral_dim['atom_isotope_number']

                cur_spectral_dim['acquisition'] = 'yes' if _dim_id == self.acq_dim_id\
                    and (isotope_number == 1 or (isotope_number == 13 and self.exptlMethod == 'SOLID-STATE NMR')) else 'no'

                if _dim_id == 1 and cur_spectral_dim['acquisition'] == 'no':
                    self.acq_dim_id = self.num_of_dim

                cur_spectral_dim['under_sampling_type'] = 'not observed' if cur_spectral_dim['acquisition'] == 'yes' else 'aliased'

                self.cur_spectral_dim[_dim_id] = cur_spectral_dim

    # Enter a parse tree produced by VnmrPKParser#format.
    def enterFormat(self, ctx: VnmrPKParser.FormatContext):
        if ctx.A_ppm():
            self.num_of_dim = 4
            self.initSpectralDim()
        elif ctx.Z_ppm():
            self.num_of_dim = 4
            self.initSpectralDim()
        elif ctx.Y_ppm():
            self.num_of_dim = 4
            self.initSpectralDim()

        if self.spectrum_name is not None:
            if self.num_of_dim not in self.__spectrum_names:
                self.__spectrum_names[self.num_of_dim] = {}
            if self.cur_list_id not in self.__spectrum_names[self.num_of_dim]:
                self.__spectrum_names[self.num_of_dim][self.cur_list_id] = self.spectrum_name

        self.__has_volume = bool(ctx.Volume())
        self.__has_line_width = bool(ctx.Linewidth_X())
        self.__has_assign = bool(ctx.Comment())

    # Exit a parse tree produced by VnmrPKParser#format.
    def exitFormat(self, ctx: VnmrPKParser.FormatContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by VnmrPKParser#peak_ll2d.
    def enterPeak_ll2d(self, ctx: VnmrPKParser.Peak_ll2dContext):  # pylint: disable=unused-argument
        self.peaks2D += 1

        self.atomSelectionSets.clear()
        self.asIsSets.clear()

    # Exit a parse tree produced by VnmrPKParser#peak_ll2d.
    def exitPeak_ll2d(self, ctx: VnmrPKParser.Peak_ll2dContext):

        try:

            if len(self.numberSelection) == 0:
                self.peaks2D -= 1
                return

            index = int(str(ctx.Integer()))

            ass = None
            if self.__has_assign and ctx.Double_quote_string():
                ass = str(ctx.Double_quote_string())[1:-1].strip()
                if ass in emptyValue:
                    ass = None

            x_ppm = float(str(ctx.Float(0)))
            y_ppm = float(str(ctx.Float(1)))

            height = self.originalNumberSelection[0]

            offset = 1

            volume = None
            if self.__has_volume:
                volume = self.originalNumberSelection[offset]
                offset += 1

            if self.__has_line_width:
                x_lw_hz = self.numberSelection[offset]
                y_lw_hz = self.numberSelection[offset + 1]

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            if x_ppm is None or y_ppm is None:
                self.peaks2D -= 1
                return

            dstFunc = self.validatePeak2D(index, x_ppm, y_ppm, None, None, None, None,
                                          None, None, x_lw_hz, y_lw_hz, height, None, volume, None)

            if dstFunc is None:
                self.peaks2D -= 1
                return

            cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

            cur_spectral_dim[1]['freq_hint'].append(x_ppm)
            cur_spectral_dim[2]['freq_hint'].append(y_ppm)

            has_assignments = has_multiple_assignments = False
            asis1 = asis2 = None

            if ass is not None:
                assignments = []
                if len(ass.split('-')) == self.num_of_dim:
                    hint = None
                    for _ass in ass.split('-'):
                        assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                        hint = assignments[-1] if assignments[-1] is not None else None
                elif len(ass.split(':')) == self.num_of_dim:
                    hint = None
                    for _ass in ass.split(':'):
                        assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                        hint = assignments[-1] if assignments[-1] is not None else None
                elif len(ass.split(';')) == self.num_of_dim:
                    hint = None
                    for _ass in ass.split(';'):
                        assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                        hint = assignments[-1] if assignments[-1] is not None else None
                elif len(ass.split(',')) == self.num_of_dim:
                    hint = None
                    for _ass in ass.split(','):
                        assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                        hint = assignments[-1] if assignments[-1] is not None else None
                else:
                    assignments = [None] * self.num_of_dim
                    _assignments = self.extractPeakAssignment(self.num_of_dim, ass, index)
                    if _assignments is not None and len(_assignments) == self.num_of_dim:
                        for idx in range(self.num_of_dim):
                            assignments[idx] = [_assignments[idx]]  # pylint: disable=unsubscriptable-object

                if all(assignment is not None for assignment in assignments):

                    self.retrieveLocalSeqScheme()

                    hasChainId = all(a[0]['chain_id'] is not None for a in assignments)
                    hasCompId = all(a[0]['comp_id'] is not None for a in assignments)

                    has_multiple_assignments = any(len(assignment) > 1 for assignment in assignments)

                    for a1, a2 in zip_longest(assignments[0], assignments[1]):

                        self.atomSelectionSet.clear()
                        asis1 = asis2 = None

                        if hasChainId and hasCompId:
                            chainAssign1, asis1 = self.assignCoordPolymerSequenceWithChainId(a1['chain_id'], a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                            chainAssign2, asis2 = self.assignCoordPolymerSequenceWithChainId(a2['chain_id'], a2['seq_id'], a2['comp_id'], a2['atom_id'], index)

                        elif hasChainId:
                            chainAssign1 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a1['chain_id'], a1['seq_id'], a1['atom_id'], index)
                            chainAssign2 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a2['chain_id'], a2['seq_id'], a2['atom_id'], index)

                        elif hasCompId:
                            chainAssign1, asis1 = self.assignCoordPolymerSequence(a1['chain_id'], a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                            chainAssign2, asis2 = self.assignCoordPolymerSequence(a2['chain_id'], a2['seq_id'], a2['comp_id'], a2['atom_id'], index)

                        else:
                            chainAssign1 = self.assignCoordPolymerSequenceWithoutCompId(a1['seq_id'], a1['atom_id'], index)
                            chainAssign2 = self.assignCoordPolymerSequenceWithoutCompId(a2['seq_id'], a2['atom_id'], index)

                        if len(chainAssign1) > 0 and len(chainAssign2) > 0:
                            self.selectCoordAtoms(chainAssign1, a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                            self.selectCoordAtoms(chainAssign2, a2['seq_id'], a2['comp_id'], a2['atom_id'], index)

                            if len(self.atomSelectionSet) == self.num_of_dim:
                                has_assignments = True
                                has_assignments &= self.fillAtomTypeInCase(1, self.atomSelectionSet[0][0]['atom_id'][0])
                                has_assignments &= self.fillAtomTypeInCase(2, self.atomSelectionSet[1][0]['atom_id'][0])
                                if has_assignments:
                                    self.atomSelectionSets.append(copy.copy(self.atomSelectionSet))
                                    self.asIsSets.append([asis1, asis2])
                                else:
                                    break
                            else:
                                has_assignments = False
                                break

            if self.createSfDict__:
                sf = self.getSf()

            if self.debug:
                if not has_assignments:
                    print(f"subtype={self.cur_subtype} id={self.peaks2D} (index={index}) "
                          f"{ass} -> None None {dstFunc}")
                for idx, atomSelectionSet in enumerate(self.atomSelectionSets, start=1):
                    if has_multiple_assignments:
                        print(f"subtype={self.cur_subtype} id={self.peaks2D} (index={index}) combination_id={idx} "
                              f"{ass} -> {atomSelectionSet[0]} "
                              f"{atomSelectionSet[1]} {dstFunc}")
                    else:
                        print(f"subtype={self.cur_subtype} id={self.peaks2D} (index={index}) "
                              f"{ass} -> {atomSelectionSet[0]} "
                              f"{atomSelectionSet[1]} {dstFunc}")

            if self.createSfDict__ and sf is not None:
                sf['id'] = index
                sf['index_id'] += 1
                ambig_code1 = ambig_code2 = None
                if has_assignments and not has_multiple_assignments:
                    atom1 = self.atomSelectionSet[0][0]
                    atom2 = self.atomSelectionSet[1][0]
                    if len(self.atomSelectionSet[0]) > 1:
                        ambig_code1 = self.csStat.getMaxAmbigCodeWoSetId(atom1['comp_id'], atom1['atom_id'])
                        if ambig_code1 == 0:
                            ambig_code1 = None
                    if len(self.atomSelectionSet[1]) > 1:
                        ambig_code2 = self.csStat.getMaxAmbigCodeWoSetId(atom2['comp_id'], atom2['atom_id'])
                        if ambig_code2 == 0:
                            ambig_code2 = None
                else:
                    atom1 = atom2 = None

                row = getPkRow(self.cur_subtype, sf['id'], sf['index_id'],
                               sf['list_id'], self.entryId, dstFunc,
                               self.authToStarSeq, self.authToOrigSeq, self.offsetHolder,
                               atom1, atom2, asis1=asis1, asis2=asis2,
                               ambig_code1=ambig_code1, ambig_code2=ambig_code2,
                               details=None if has_assignments and not has_multiple_assignments else ass)
                sf['loop'].add_data(row)

                row = getPkGenCharRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc)
                sf['alt_loops'][0].add_data(row)
                for idx in range(self.num_of_dim):
                    row = getPkCharRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, idx + 1)
                    sf['alt_loops'][1].add_data(row)
                if has_assignments:
                    for atomSelectionSet, asIsSet in zip(self.atomSelectionSets, self.asIsSets):
                        uniqAtoms = []
                        for idx in range(self.num_of_dim):
                            atom = atomSelectionSet[idx]
                            atom0 = atom[0]
                            if atom0 not in uniqAtoms:
                                asis = asIsSet[idx]
                                ambig_code = None
                                if len(atom) > 1:
                                    ambig_code = self.csStat.getMaxAmbigCodeWoSetId(atom0['comp_id'], atom0['atom_id'])
                                    if ambig_code == 0:
                                        ambig_code = None
                                row = getPkChemShiftRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, idx + 1,
                                                        self.authToStarSeq, self.authToOrigSeq, self.offsetHolder,
                                                        atom0, asis, ambig_code)
                                sf['alt_loops'][2].add_data(row)
                                uniqAtoms.append(atom0)

        finally:
            self.numberSelection.clear()
            self.originalNumberSelection.clear()

    # Enter a parse tree produced by VnmrPKParser#peak_ll3d.
    def enterPeak_ll3d(self, ctx: VnmrPKParser.Peak_ll3dContext):  # pylint: disable=unused-argument
        self.peaks3D += 1

        self.atomSelectionSets.clear()
        self.asIsSets.clear()

    # Exit a parse tree produced by VnmrPKParser#peak_ll3d.
    def exitPeak_ll3d(self, ctx: VnmrPKParser.Peak_ll3dContext):

        try:

            if len(self.numberSelection) == 0:
                self.peaks3D -= 1
                return

            index = int(str(ctx.Integer()))

            ass = None
            if self.__has_assign and ctx.Double_quote_string():
                ass = str(ctx.Double_quote_string())[1:-1].strip()
                if ass in emptyValue:
                    ass = None

            x_ppm = float(str(ctx.Float(0)))
            y_ppm = float(str(ctx.Float(1)))
            z_ppm = float(str(ctx.Float(2)))

            height = self.originalNumberSelection[0]

            offset = 1

            volume = None
            if self.__has_volume:
                volume = self.originalNumberSelection[offset]
                offset += 1

            if self.__has_line_width:
                x_lw_hz = self.numberSelection[offset]
                y_lw_hz = self.numberSelection[offset + 1]
                z_lw_hz = self.numberSelection[offset + 2]

            if x_ppm is None or y_ppm is None or z_ppm is None:
                self.peaks3D -= 1
                return

            dstFunc = self.validatePeak3D(index, x_ppm, y_ppm, z_ppm, None, None, None, None, None, None,
                                          None, None, None, x_lw_hz, y_lw_hz, z_lw_hz, height, None, volume, None)

            if dstFunc is None:
                self.peaks3D -= 1
                return

            cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

            cur_spectral_dim[1]['freq_hint'].append(x_ppm)
            cur_spectral_dim[2]['freq_hint'].append(y_ppm)
            cur_spectral_dim[3]['freq_hint'].append(z_ppm)

            has_assignments = has_multiple_assignments = False
            asis1 = asis2 = asis3 = None

            if ass is not None:
                assignments = []
                if len(ass.split('-')) == self.num_of_dim:
                    hint = None
                    for _ass in ass.split('-'):
                        assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                        hint = assignments[-1] if assignments[-1] is not None else None
                elif len(ass.split(':')) == self.num_of_dim:
                    hint = None
                    for _ass in ass.split(':'):
                        assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                        hint = assignments[-1] if assignments[-1] is not None else None
                elif len(ass.split(';')) == self.num_of_dim:
                    hint = None
                    for _ass in ass.split(';'):
                        assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                        hint = assignments[-1] if assignments[-1] is not None else None
                elif len(ass.split(',')) == self.num_of_dim:
                    hint = None
                    for _ass in ass.split(','):
                        assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                        hint = assignments[-1] if assignments[-1] is not None else None
                else:
                    assignments = [None] * self.num_of_dim
                    _assignments = self.extractPeakAssignment(self.num_of_dim, ass, index)
                    if _assignments is not None and len(_assignments) == self.num_of_dim:
                        for idx in range(self.num_of_dim):
                            assignments[idx] = [_assignments[idx]]  # pylint: disable=unsubscriptable-object

                if all(assignment is not None for assignment in assignments):

                    self.retrieveLocalSeqScheme()

                    hasChainId = all(a[0]['chain_id'] is not None for a in assignments)
                    hasCompId = all(a[0]['comp_id'] is not None for a in assignments)

                    has_multiple_assignments = any(len(assignment) > 1 for assignment in assignments)

                    for a1, a2, a3 in zip_longest(assignments[0], assignments[1], assignments[2]):

                        self.atomSelectionSet.clear()
                        asis1 = asis2 = asis3 = None

                        if hasChainId and hasCompId:
                            chainAssign1, asis1 = self.assignCoordPolymerSequenceWithChainId(a1['chain_id'], a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                            chainAssign2, asis2 = self.assignCoordPolymerSequenceWithChainId(a2['chain_id'], a2['seq_id'], a2['comp_id'], a2['atom_id'], index)
                            chainAssign3, asis3 = self.assignCoordPolymerSequenceWithChainId(a3['chain_id'], a3['seq_id'], a3['comp_id'], a3['atom_id'], index)

                        elif hasChainId:
                            chainAssign1 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a1['chain_id'], a1['seq_id'], a1['atom_id'], index)
                            chainAssign2 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a2['chain_id'], a2['seq_id'], a2['atom_id'], index)
                            chainAssign3 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a3['chain_id'], a3['seq_id'], a3['atom_id'], index)

                        elif hasCompId:
                            chainAssign1, asis1 = self.assignCoordPolymerSequence(a1['chain_id'], a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                            chainAssign2, asis2 = self.assignCoordPolymerSequence(a2['chain_id'], a2['seq_id'], a2['comp_id'], a2['atom_id'], index)
                            chainAssign3, asis3 = self.assignCoordPolymerSequence(a3['chain_id'], a3['seq_id'], a3['comp_id'], a3['atom_id'], index)

                        else:
                            chainAssign1 = self.assignCoordPolymerSequenceWithoutCompId(a1['seq_id'], a1['atom_id'], index)
                            chainAssign2 = self.assignCoordPolymerSequenceWithoutCompId(a2['seq_id'], a2['atom_id'], index)
                            chainAssign3 = self.assignCoordPolymerSequenceWithoutCompId(a3['seq_id'], a3['atom_id'], index)

                        if len(chainAssign1) > 0 and len(chainAssign2) > 0 and len(chainAssign3) > 0:
                            self.selectCoordAtoms(chainAssign1, a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                            self.selectCoordAtoms(chainAssign2, a2['seq_id'], a2['comp_id'], a2['atom_id'], index)
                            self.selectCoordAtoms(chainAssign3, a3['seq_id'], a3['comp_id'], a3['atom_id'], index)

                            if len(self.atomSelectionSet) == self.num_of_dim:
                                has_assignments = True
                                has_assignments &= self.fillAtomTypeInCase(1, self.atomSelectionSet[0][0]['atom_id'][0])
                                has_assignments &= self.fillAtomTypeInCase(2, self.atomSelectionSet[1][0]['atom_id'][0])
                                has_assignments &= self.fillAtomTypeInCase(3, self.atomSelectionSet[2][0]['atom_id'][0])
                                if has_assignments:
                                    self.atomSelectionSets.append(copy.copy(self.atomSelectionSet))
                                    self.asIsSets.append([asis1, asis2, asis3])
                                else:
                                    break
                            else:
                                has_assignments = False
                                break

            if self.createSfDict__:
                sf = self.getSf()

            if self.debug:
                if not has_assignments:
                    print(f"subtype={self.cur_subtype} id={self.peaks3D} (index={index}) "
                          f"{ass} -> None None None {dstFunc}")
                for idx, atomSelectionSet in enumerate(self.atomSelectionSets, start=1):
                    if has_multiple_assignments:
                        print(f"subtype={self.cur_subtype} id={self.peaks3D} (index={index}) combination_id={idx} "
                              f"{ass} -> {atomSelectionSet[0]} "
                              f"{atomSelectionSet[1]} "
                              f"{atomSelectionSet[2]} {dstFunc}")
                    else:
                        print(f"subtype={self.cur_subtype} id={self.peaks3D} (index={index}) "
                              f"{ass} -> {atomSelectionSet[0]} "
                              f"{atomSelectionSet[1]} "
                              f"{atomSelectionSet[2]} {dstFunc}")

            if self.createSfDict__ and sf is not None:
                sf['id'] = index
                sf['index_id'] += 1
                ambig_code1 = ambig_code2 = ambig_code3 = None
                if has_assignments and not has_multiple_assignments:
                    atom1 = self.atomSelectionSet[0][0]
                    atom2 = self.atomSelectionSet[1][0]
                    atom3 = self.atomSelectionSet[2][0]
                    if len(self.atomSelectionSet[0]) > 1:
                        ambig_code1 = self.csStat.getMaxAmbigCodeWoSetId(atom1['comp_id'], atom1['atom_id'])
                        if ambig_code1 == 0:
                            ambig_code1 = None
                    if len(self.atomSelectionSet[1]) > 1:
                        ambig_code2 = self.csStat.getMaxAmbigCodeWoSetId(atom2['comp_id'], atom2['atom_id'])
                        if ambig_code2 == 0:
                            ambig_code2 = None
                    if len(self.atomSelectionSet[2]) > 1:
                        ambig_code3 = self.csStat.getMaxAmbigCodeWoSetId(atom3['comp_id'], atom3['atom_id'])
                        if ambig_code3 == 0:
                            ambig_code3 = None
                else:
                    atom1 = atom2 = atom3 = None

                row = getPkRow(self.cur_subtype, sf['id'], sf['index_id'],
                               sf['list_id'], self.entryId, dstFunc,
                               self.authToStarSeq, self.authToOrigSeq, self.offsetHolder,
                               atom1, atom2, atom3, asis1=asis1, asis2=asis2, asis3=asis3,
                               ambig_code1=ambig_code1, ambig_code2=ambig_code2,
                               ambig_code3=ambig_code3,
                               details=None if has_assignments and not has_multiple_assignments else ass)
                sf['loop'].add_data(row)

                row = getPkGenCharRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc)
                sf['alt_loops'][0].add_data(row)
                for idx in range(self.num_of_dim):
                    row = getPkCharRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, idx + 1)
                    sf['alt_loops'][1].add_data(row)
                if has_assignments:
                    for atomSelectionSet, asIsSet in zip(self.atomSelectionSets, self.asIsSets):
                        uniqAtoms = []
                        for idx in range(self.num_of_dim):
                            atom = atomSelectionSet[idx]
                            atom0 = atom[0]
                            if atom0 not in uniqAtoms:
                                asis = asIsSet[idx]
                                ambig_code = None
                                if len(atom) > 1:
                                    ambig_code = self.csStat.getMaxAmbigCodeWoSetId(atom0['comp_id'], atom0['atom_id'])
                                    if ambig_code == 0:
                                        ambig_code = None
                                row = getPkChemShiftRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, idx + 1,
                                                        self.authToStarSeq, self.authToOrigSeq, self.offsetHolder,
                                                        atom0, asis, ambig_code)
                                sf['alt_loops'][2].add_data(row)
                                uniqAtoms.append(atom0)

        finally:
            self.numberSelection.clear()
            self.originalNumberSelection.clear()

    # Enter a parse tree produced by VnmrPKParser#peak_ll4d.
    def enterPeak_ll4d(self, ctx: VnmrPKParser.Peak_ll4dContext):  # pylint: disable=unused-argument
        self.peaks4D += 1

        self.atomSelectionSets.clear()
        self.asIsSets.clear()

    # Exit a parse tree produced by VnmrPKParser#peak_ll4d.
    def exitPeak_ll4d(self, ctx: VnmrPKParser.Peak_ll4dContext):

        try:

            if len(self.numberSelection) == 0:
                self.peaks4D -= 1
                return

            index = int(str(ctx.Integer()))

            ass = None
            if self.__has_assign and ctx.Double_quote_string():
                ass = str(ctx.Double_quote_string())[1:-1].strip()
                if ass in emptyValue:
                    ass = None

            x_ppm = float(str(ctx.Float(0)))
            y_ppm = float(str(ctx.Float(1)))
            z_ppm = float(str(ctx.Float(2)))
            a_ppm = float(str(ctx.Float(3)))

            height = self.originalNumberSelection[0]

            offset = 1

            volume = None
            if self.__has_volume:
                volume = self.originalNumberSelection[offset]
                offset += 1

            if self.__has_line_width:
                x_lw_hz = self.numberSelection[offset]
                y_lw_hz = self.numberSelection[offset + 1]
                z_lw_hz = self.numberSelection[offset + 2]
                a_lw_hz = self.numberSelection[offset + 3]

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            if x_ppm is None or y_ppm is None or z_ppm is None or a_ppm is None:
                self.peaks4D -= 1
                return

            dstFunc = self.validatePeak4D(index, x_ppm, y_ppm, z_ppm, a_ppm, None, None, None, None, None, None, None, None,
                                          None, None, None, None, x_lw_hz, y_lw_hz, z_lw_hz, a_lw_hz, height, None, volume, None)

            if dstFunc is None:
                self.peaks4D -= 1
                return

            cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

            cur_spectral_dim[1]['freq_hint'].append(x_ppm)
            cur_spectral_dim[2]['freq_hint'].append(y_ppm)
            cur_spectral_dim[3]['freq_hint'].append(z_ppm)
            cur_spectral_dim[4]['freq_hint'].append(a_ppm)

            has_assignments = has_multiple_assignments = False
            asis1 = asis2 = asis3 = asis4 = None

            if ass is not None:
                assignments = []
                if len(ass.split('-')) == self.num_of_dim:
                    hint = None
                    for _ass in ass.split('-'):
                        assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                        hint = assignments[-1] if assignments[-1] is not None else None
                elif len(ass.split(':')) == self.num_of_dim:
                    hint = None
                    for _ass in ass.split(':'):
                        assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                        hint = assignments[-1] if assignments[-1] is not None else None
                elif len(ass.split(';')) == self.num_of_dim:
                    hint = None
                    for _ass in ass.split(';'):
                        assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                        hint = assignments[-1] if assignments[-1] is not None else None
                elif len(ass.split(',')) == self.num_of_dim:
                    hint = None
                    for _ass in ass.split(','):
                        assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                        hint = assignments[-1] if assignments[-1] is not None else None
                else:
                    assignments = [None] * self.num_of_dim
                    _assignments = self.extractPeakAssignment(self.num_of_dim, ass, index)
                    if _assignments is not None and len(_assignments) == self.num_of_dim:
                        for idx in range(self.num_of_dim):
                            assignments[idx] = [_assignments[idx]]  # pylint: disable=unsubscriptable-object

                if all(assignment is not None for assignment in assignments):

                    self.retrieveLocalSeqScheme()

                    hasChainId = all(a[0]['chain_id'] is not None for a in assignments)
                    hasCompId = all(a[0]['comp_id'] is not None for a in assignments)

                    has_multiple_assignments = any(len(assignment) > 1 for assignment in assignments)

                    for a1, a2, a3, a4 in zip_longest(assignments[0], assignments[1], assignments[2], assignments[3]):

                        self.atomSelectionSet.clear()
                        asis1 = asis2 = asis3 = asis4 = None

                        if hasChainId and hasCompId:
                            chainAssign1, asis1 = self.assignCoordPolymerSequenceWithChainId(a1['chain_id'], a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                            chainAssign2, asis2 = self.assignCoordPolymerSequenceWithChainId(a2['chain_id'], a2['seq_id'], a2['comp_id'], a2['atom_id'], index)
                            chainAssign3, asis3 = self.assignCoordPolymerSequenceWithChainId(a3['chain_id'], a3['seq_id'], a3['comp_id'], a3['atom_id'], index)
                            chainAssign4, asis4 = self.assignCoordPolymerSequenceWithChainId(a4['chain_id'], a4['seq_id'], a4['comp_id'], a4['atom_id'], index)

                        elif hasChainId:
                            chainAssign1 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a1['chain_id'], a1['seq_id'], a1['atom_id'], index)
                            chainAssign2 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a2['chain_id'], a2['seq_id'], a2['atom_id'], index)
                            chainAssign3 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a3['chain_id'], a3['seq_id'], a3['atom_id'], index)
                            chainAssign4 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a4['chain_id'], a4['seq_id'], a4['atom_id'], index)

                        elif hasCompId:
                            chainAssign1, asis1 = self.assignCoordPolymerSequence(a1['chain_id'], a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                            chainAssign2, asis2 = self.assignCoordPolymerSequence(a2['chain_id'], a2['seq_id'], a2['comp_id'], a2['atom_id'], index)
                            chainAssign3, asis3 = self.assignCoordPolymerSequence(a3['chain_id'], a3['seq_id'], a3['comp_id'], a3['atom_id'], index)
                            chainAssign4, asis4 = self.assignCoordPolymerSequence(a4['chain_id'], a4['seq_id'], a4['comp_id'], a4['atom_id'], index)

                        else:
                            chainAssign1 = self.assignCoordPolymerSequenceWithoutCompId(a1['seq_id'], a1['atom_id'], index)
                            chainAssign2 = self.assignCoordPolymerSequenceWithoutCompId(a2['seq_id'], a2['atom_id'], index)
                            chainAssign3 = self.assignCoordPolymerSequenceWithoutCompId(a3['seq_id'], a3['atom_id'], index)
                            chainAssign4 = self.assignCoordPolymerSequenceWithoutCompId(a4['seq_id'], a4['atom_id'], index)

                        if len(chainAssign1) > 0 and len(chainAssign2) > 0 and len(chainAssign3) > 0 and len(chainAssign4) > 0:
                            self.selectCoordAtoms(chainAssign1, a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                            self.selectCoordAtoms(chainAssign2, a2['seq_id'], a2['comp_id'], a2['atom_id'], index)
                            self.selectCoordAtoms(chainAssign3, a3['seq_id'], a3['comp_id'], a3['atom_id'], index)
                            self.selectCoordAtoms(chainAssign4, a4['seq_id'], a4['comp_id'], a4['atom_id'], index)

                            if len(self.atomSelectionSet) == self.num_of_dim:
                                has_assignments = True
                                has_assignments &= self.fillAtomTypeInCase(1, self.atomSelectionSet[0][0]['atom_id'][0])
                                has_assignments &= self.fillAtomTypeInCase(2, self.atomSelectionSet[1][0]['atom_id'][0])
                                has_assignments &= self.fillAtomTypeInCase(3, self.atomSelectionSet[2][0]['atom_id'][0])
                                has_assignments &= self.fillAtomTypeInCase(4, self.atomSelectionSet[3][0]['atom_id'][0])
                                if has_assignments:
                                    self.atomSelectionSets.append(copy.copy(self.atomSelectionSet))
                                    self.asIsSets.append([asis1, asis2, asis3, asis4])
                                else:
                                    break
                            else:
                                has_assignments = False
                                break

            if self.createSfDict__:
                sf = self.getSf()

            if self.debug:
                if not has_assignments:
                    print(f"subtype={self.cur_subtype} id={self.peaks4D} (index={index}) "
                          f"{ass} -> None None None None {dstFunc}")
                for idx, atomSelectionSet in enumerate(self.atomSelectionSets, start=1):
                    if has_multiple_assignments:
                        print(f"subtype={self.cur_subtype} id={self.peaks4D} (index={index}) combination_id={idx} "
                              f"{ass} -> {atomSelectionSet[0]} "
                              f"{atomSelectionSet[1]} "
                              f"{atomSelectionSet[2]} "
                              f"{atomSelectionSet[3]} {dstFunc}")
                    else:
                        print(f"subtype={self.cur_subtype} id={self.peaks4D} (index={index}) "
                              f"{ass} -> {atomSelectionSet[0]} "
                              f"{atomSelectionSet[1]} "
                              f"{atomSelectionSet[2]} "
                              f"{atomSelectionSet[3]} {dstFunc}")

            if self.createSfDict__ and sf is not None:
                sf['id'] = index
                sf['index_id'] += 1
                ambig_code1 = ambig_code2 = ambig_code3 = ambig_code4 = None
                if has_assignments and not has_multiple_assignments:
                    atom1 = self.atomSelectionSet[0][0]
                    atom2 = self.atomSelectionSet[1][0]
                    atom3 = self.atomSelectionSet[2][0]
                    atom4 = self.atomSelectionSet[3][0]
                    if len(self.atomSelectionSet[0]) > 1:
                        ambig_code1 = self.csStat.getMaxAmbigCodeWoSetId(atom1['comp_id'], atom1['atom_id'])
                        if ambig_code1 == 0:
                            ambig_code1 = None
                    if len(self.atomSelectionSet[1]) > 1:
                        ambig_code2 = self.csStat.getMaxAmbigCodeWoSetId(atom2['comp_id'], atom2['atom_id'])
                        if ambig_code2 == 0:
                            ambig_code2 = None
                    if len(self.atomSelectionSet[2]) > 1:
                        ambig_code3 = self.csStat.getMaxAmbigCodeWoSetId(atom3['comp_id'], atom3['atom_id'])
                        if ambig_code3 == 0:
                            ambig_code3 = None
                    if len(self.atomSelectionSet[3]) > 1:
                        ambig_code4 = self.csStat.getMaxAmbigCodeWoSetId(atom4['comp_id'], atom4['atom_id'])
                        if ambig_code4 == 0:
                            ambig_code4 = None
                else:
                    atom1 = atom2 = atom3 = atom4 = None

                row = getPkRow(self.cur_subtype, sf['id'], sf['index_id'],
                               sf['list_id'], self.entryId, dstFunc,
                               self.authToStarSeq, self.authToOrigSeq, self.offsetHolder,
                               atom1, atom2, atom3, atom4,
                               asis1=asis1, asis2=asis2, asis3=asis3, asis4=asis4,
                               ambig_code1=ambig_code1, ambig_code2=ambig_code2,
                               ambig_code3=ambig_code3, ambig_code4=ambig_code4,
                               details=None if has_assignments and not has_multiple_assignments else ass)
                sf['loop'].add_data(row)

                row = getPkGenCharRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc)
                sf['alt_loops'][0].add_data(row)
                for idx in range(self.num_of_dim):
                    row = getPkCharRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, idx + 1)
                    sf['alt_loops'][1].add_data(row)
                if has_assignments:
                    for atomSelectionSet, asIsSet in zip(self.atomSelectionSets, self.asIsSets):
                        uniqAtoms = []
                        for idx in range(self.num_of_dim):
                            atom = atomSelectionSet[idx]
                            atom0 = atom[0]
                            if atom0 not in uniqAtoms:
                                asis = asIsSet[idx]
                                ambig_code = None
                                if len(atom) > 1:
                                    ambig_code = self.csStat.getMaxAmbigCodeWoSetId(atom0['comp_id'], atom0['atom_id'])
                                    if ambig_code == 0:
                                        ambig_code = None
                                row = getPkChemShiftRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, idx + 1,
                                                        self.authToStarSeq, self.authToOrigSeq, self.offsetHolder,
                                                        atom0, asis, ambig_code)
                                sf['alt_loops'][2].add_data(row)
                                uniqAtoms.append(atom0)

        finally:
            self.numberSelection.clear()
            self.originalNumberSelection.clear()

    # Enter a parse tree produced by VnmrPKParser#data_label.
    def enterData_label(self, ctx: VnmrPKParser.Data_labelContext):
        if ctx.Dim_0_ppm():
            self.num_of_dim = max(self.num_of_dim, 1)
        if ctx.Dim_1_ppm():
            self.num_of_dim = max(self.num_of_dim, 2)
        if ctx.Dim_2_ppm():
            self.num_of_dim = max(self.num_of_dim, 3)
        if ctx.Dim_3_ppm():
            self.num_of_dim = max(self.num_of_dim, 4)

        self.__has_volume = bool(ctx.Volume_LA())
        self.__has_assign = bool(ctx.Assignment())

        self.initSpectralDim()

    # Exit a parse tree produced by VnmrPKParser#data_label.
    def exitData_label(self, ctx: VnmrPKParser.Data_labelContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by VnmrPKParser#peak_2d.
    def enterPeak_2d(self, ctx: VnmrPKParser.Peak_2dContext):  # pylint: disable=unused-argument
        if self.cur_subtype != 'peak2d':
            self.num_of_dim = 2
            self.initSpectralDim()

        self.peaks2D += 1

        self.atomSelectionSets.clear()
        self.asIsSets.clear()
        self.spectrum_name = None

    # Exit a parse tree produced by VnmrPKParser#peak_2d.
    def exitPeak_2d(self, ctx: VnmrPKParser.Peak_2dContext):

        try:

            if len(self.numberSelection) == 0:
                self.peaks2D -= 1
                return

            index = int(str(ctx.Integer()))

            ass = None
            if self.__has_assign and ctx.Assignment_2d_ex():
                ass = str(ctx.Assignment_2d_ex())
                if '?' in ass:
                    ass = None

            x_ppm = float(str(ctx.Float(0)))
            x_dev = abs(float(str(ctx.Float(1))))
            y_ppm = float(str(ctx.Float(2)))
            y_dev = abs(float(str(ctx.Float(3))))

            height = self.originalNumberSelection[0]
            volume = None
            if self.__has_volume:
                volume = self.originalNumberSelection[1]

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            if x_ppm is None or y_ppm is None:
                self.peaks2D -= 1
                return

            dstFunc = self.validatePeak2D(index, x_ppm, y_ppm, x_dev, y_dev, None, None,
                                          None, None, None, None, height, None, volume, None)

            if dstFunc is None:
                self.peaks2D -= 1
                return

            cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

            cur_spectral_dim[1]['freq_hint'].append(x_ppm)
            cur_spectral_dim[2]['freq_hint'].append(y_ppm)

            has_assignments = has_multiple_assignments = False
            asis1 = asis2 = None

            if ass is not None:
                assignments = []
                if len(ass.split('-')) == self.num_of_dim:
                    hint = None
                    for _ass in ass.split('-'):
                        assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                        hint = assignments[-1] if assignments[-1] is not None else None
                elif len(ass.split(':')) == self.num_of_dim:
                    hint = None
                    for _ass in ass.split(':'):
                        assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                        hint = assignments[-1] if assignments[-1] is not None else None
                elif len(ass.split(';')) == self.num_of_dim:
                    hint = None
                    for _ass in ass.split(';'):
                        assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                        hint = assignments[-1] if assignments[-1] is not None else None
                elif len(ass.split(',')) == self.num_of_dim:
                    hint = None
                    for _ass in ass.split(','):
                        assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                        hint = assignments[-1] if assignments[-1] is not None else None
                else:
                    assignments = [None] * self.num_of_dim
                    _assignments = self.extractPeakAssignment(self.num_of_dim, ass, index)
                    if _assignments is not None and len(_assignments) == self.num_of_dim:
                        for idx in range(self.num_of_dim):
                            assignments[idx] = [_assignments[idx]]  # pylint: disable=unsubscriptable-object

                if all(assignment is not None for assignment in assignments):

                    self.retrieveLocalSeqScheme()

                    hasChainId = all(a[0]['chain_id'] is not None for a in assignments)
                    hasCompId = all(a[0]['comp_id'] is not None for a in assignments)

                    has_multiple_assignments = any(len(assignment) > 1 for assignment in assignments)

                    for a1, a2 in zip_longest(assignments[0], assignments[1]):

                        self.atomSelectionSet.clear()
                        asis1 = asis2 = None

                        if hasChainId and hasCompId:
                            chainAssign1, asis1 = self.assignCoordPolymerSequenceWithChainId(a1['chain_id'], a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                            chainAssign2, asis2 = self.assignCoordPolymerSequenceWithChainId(a2['chain_id'], a2['seq_id'], a2['comp_id'], a2['atom_id'], index)

                        elif hasChainId:
                            chainAssign1 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a1['chain_id'], a1['seq_id'], a1['atom_id'], index)
                            chainAssign2 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a2['chain_id'], a2['seq_id'], a2['atom_id'], index)

                        elif hasCompId:
                            chainAssign1, asis1 = self.assignCoordPolymerSequence(a1['chain_id'], a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                            chainAssign2, asis2 = self.assignCoordPolymerSequence(a2['chain_id'], a2['seq_id'], a2['comp_id'], a2['atom_id'], index)

                        else:
                            chainAssign1 = self.assignCoordPolymerSequenceWithoutCompId(a1['seq_id'], a1['atom_id'], index)
                            chainAssign2 = self.assignCoordPolymerSequenceWithoutCompId(a2['seq_id'], a2['atom_id'], index)

                        if len(chainAssign1) > 0 and len(chainAssign2) > 0:
                            self.selectCoordAtoms(chainAssign1, a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                            self.selectCoordAtoms(chainAssign2, a2['seq_id'], a2['comp_id'], a2['atom_id'], index)

                            if len(self.atomSelectionSet) == self.num_of_dim:
                                has_assignments = True
                                has_assignments &= self.fillAtomTypeInCase(1, self.atomSelectionSet[0][0]['atom_id'][0])
                                has_assignments &= self.fillAtomTypeInCase(2, self.atomSelectionSet[1][0]['atom_id'][0])
                                if has_assignments:
                                    self.atomSelectionSets.append(copy.copy(self.atomSelectionSet))
                                    self.asIsSets.append([asis1, asis2])
                                else:
                                    break
                            else:
                                has_assignments = False
                                break

            if self.createSfDict__:
                sf = self.getSf()

            if self.debug:
                if not has_assignments:
                    print(f"subtype={self.cur_subtype} id={self.peaks2D} (index={index}) "
                          f"{ass} -> None None {dstFunc}")
                for idx, atomSelectionSet in enumerate(self.atomSelectionSets, start=1):
                    if has_multiple_assignments:
                        print(f"subtype={self.cur_subtype} id={self.peaks2D} (index={index}) combination_id={idx} "
                              f"{ass} -> {atomSelectionSet[0]} "
                              f"{atomSelectionSet[1]} {dstFunc}")
                    else:
                        print(f"subtype={self.cur_subtype} id={self.peaks2D} (index={index}) "
                              f"{ass} -> {atomSelectionSet[0]} "
                              f"{atomSelectionSet[1]} {dstFunc}")

            if self.createSfDict__ and sf is not None:
                sf['id'] = index
                sf['index_id'] += 1
                ambig_code1 = ambig_code2 = None
                if has_assignments and not has_multiple_assignments:
                    atom1 = self.atomSelectionSet[0][0]
                    atom2 = self.atomSelectionSet[1][0]
                    if len(self.atomSelectionSet[0]) > 1:
                        ambig_code1 = self.csStat.getMaxAmbigCodeWoSetId(atom1['comp_id'], atom1['atom_id'])
                        if ambig_code1 == 0:
                            ambig_code1 = None
                    if len(self.atomSelectionSet[1]) > 1:
                        ambig_code2 = self.csStat.getMaxAmbigCodeWoSetId(atom2['comp_id'], atom2['atom_id'])
                        if ambig_code2 == 0:
                            ambig_code2 = None
                else:
                    atom1 = atom2 = None

                row = getPkRow(self.cur_subtype, sf['id'], sf['index_id'],
                               sf['list_id'], self.entryId, dstFunc,
                               self.authToStarSeq, self.authToOrigSeq, self.offsetHolder,
                               atom1, atom2, asis1=asis1, asis2=asis2,
                               ambig_code1=ambig_code1, ambig_code2=ambig_code2,
                               details=None if has_assignments and not has_multiple_assignments else ass)
                sf['loop'].add_data(row)

                row = getPkGenCharRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc)
                sf['alt_loops'][0].add_data(row)
                for idx in range(self.num_of_dim):
                    row = getPkCharRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, idx + 1)
                    sf['alt_loops'][1].add_data(row)
                if has_assignments:
                    for atomSelectionSet, asIsSet in zip(self.atomSelectionSets, self.asIsSets):
                        uniqAtoms = []
                        for idx in range(self.num_of_dim):
                            atom = atomSelectionSet[idx]
                            atom0 = atom[0]
                            if atom0 not in uniqAtoms:
                                asis = asIsSet[idx]
                                ambig_code = None
                                if len(atom) > 1:
                                    ambig_code = self.csStat.getMaxAmbigCodeWoSetId(atom0['comp_id'], atom0['atom_id'])
                                    if ambig_code == 0:
                                        ambig_code = None
                                row = getPkChemShiftRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, idx + 1,
                                                        self.authToStarSeq, self.authToOrigSeq, self.offsetHolder,
                                                        atom0, asis, ambig_code)
                                sf['alt_loops'][2].add_data(row)
                                uniqAtoms.append(atom0)

        finally:
            self.numberSelection.clear()
            self.originalNumberSelection.clear()

    # Enter a parse tree produced by VnmrPKParser#peak_3d.
    def enterPeak_3d(self, ctx: VnmrPKParser.Peak_3dContext):  # pylint: disable=unused-argument
        if self.cur_subtype != 'peak3d':
            self.num_of_dim = 3
            self.initSpectralDim()

        self.peaks3D += 1

        self.atomSelectionSets.clear()
        self.asIsSets.clear()
        self.spectrum_name = None

    # Exit a parse tree produced by VnmrPKParser#peak_3d.
    def exitPeak_3d(self, ctx: VnmrPKParser.Peak_3dContext):

        try:

            if len(self.numberSelection) == 0:
                self.peaks3D -= 1
                return

            index = int(str(ctx.Integer()))

            ass = None
            if self.__has_assign and ctx.Assignment_3d_ex():
                ass = str(ctx.Assignment_3d_ex())
                if '?' in ass:
                    ass = None

            x_ppm = float(str(ctx.Float(0)))
            x_dev = abs(float(str(ctx.Float(1))))
            y_ppm = float(str(ctx.Float(2)))
            y_dev = abs(float(str(ctx.Float(3))))
            z_ppm = float(str(ctx.Float(4)))
            z_dev = abs(float(str(ctx.Float(5))))

            height = self.originalNumberSelection[0]
            volume = None
            if self.__has_volume:
                volume = self.originalNumberSelection[1]

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            if x_ppm is None or y_ppm is None or z_ppm is None:
                self.peaks3D -= 1
                return

            dstFunc = self.validatePeak3D(index, x_ppm, y_ppm, z_ppm, x_dev, y_dev, z_dev, None, None, None,
                                          None, None, None, None, None, None, height, None, volume, None)

            if dstFunc is None:
                self.peaks3D -= 1
                return

            cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

            cur_spectral_dim[1]['freq_hint'].append(x_ppm)
            cur_spectral_dim[2]['freq_hint'].append(y_ppm)
            cur_spectral_dim[3]['freq_hint'].append(z_ppm)

            has_assignments = has_multiple_assignments = False
            asis1 = asis2 = asis3 = None

            if ass is not None:
                assignments = []
                if len(ass.split('-')) == self.num_of_dim:
                    hint = None
                    for _ass in ass.split('-'):
                        assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                        hint = assignments[-1] if assignments[-1] is not None else None
                elif len(ass.split(':')) == self.num_of_dim:
                    hint = None
                    for _ass in ass.split(':'):
                        assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                        hint = assignments[-1] if assignments[-1] is not None else None
                elif len(ass.split(';')) == self.num_of_dim:
                    hint = None
                    for _ass in ass.split(';'):
                        assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                        hint = assignments[-1] if assignments[-1] is not None else None
                elif len(ass.split(',')) == self.num_of_dim:
                    hint = None
                    for _ass in ass.split(','):
                        assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                        hint = assignments[-1] if assignments[-1] is not None else None
                else:
                    assignments = [None] * self.num_of_dim
                    _assignments = self.extractPeakAssignment(self.num_of_dim, ass, index)
                    if _assignments is not None and len(_assignments) == self.num_of_dim:
                        for idx in range(self.num_of_dim):
                            assignments[idx] = [_assignments[idx]]  # pylint: disable=unsubscriptable-object

                if all(assignment is not None for assignment in assignments):

                    self.retrieveLocalSeqScheme()

                    hasChainId = all(a[0]['chain_id'] is not None for a in assignments)
                    hasCompId = all(a[0]['comp_id'] is not None for a in assignments)

                    has_multiple_assignments = any(len(assignment) > 1 for assignment in assignments)

                    for a1, a2, a3 in zip_longest(assignments[0], assignments[1], assignments[2]):

                        self.atomSelectionSet.clear()
                        asis1 = asis2 = asis3 = None

                        if hasChainId and hasCompId:
                            chainAssign1, asis1 = self.assignCoordPolymerSequenceWithChainId(a1['chain_id'], a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                            chainAssign2, asis2 = self.assignCoordPolymerSequenceWithChainId(a2['chain_id'], a2['seq_id'], a2['comp_id'], a2['atom_id'], index)
                            chainAssign3, asis3 = self.assignCoordPolymerSequenceWithChainId(a3['chain_id'], a3['seq_id'], a3['comp_id'], a3['atom_id'], index)

                        elif hasChainId:
                            chainAssign1 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a1['chain_id'], a1['seq_id'], a1['atom_id'], index)
                            chainAssign2 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a2['chain_id'], a2['seq_id'], a2['atom_id'], index)
                            chainAssign3 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a3['chain_id'], a3['seq_id'], a3['atom_id'], index)

                        elif hasCompId:
                            chainAssign1, asis1 = self.assignCoordPolymerSequence(a1['chain_id'], a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                            chainAssign2, asis2 = self.assignCoordPolymerSequence(a2['chain_id'], a2['seq_id'], a2['comp_id'], a2['atom_id'], index)
                            chainAssign3, asis3 = self.assignCoordPolymerSequence(a3['chain_id'], a3['seq_id'], a3['comp_id'], a3['atom_id'], index)

                        else:
                            chainAssign1 = self.assignCoordPolymerSequenceWithoutCompId(a1['seq_id'], a1['atom_id'], index)
                            chainAssign2 = self.assignCoordPolymerSequenceWithoutCompId(a2['seq_id'], a2['atom_id'], index)
                            chainAssign3 = self.assignCoordPolymerSequenceWithoutCompId(a3['seq_id'], a3['atom_id'], index)

                        if len(chainAssign1) > 0 and len(chainAssign2) > 0 and len(chainAssign3) > 0:
                            self.selectCoordAtoms(chainAssign1, a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                            self.selectCoordAtoms(chainAssign2, a2['seq_id'], a2['comp_id'], a2['atom_id'], index)
                            self.selectCoordAtoms(chainAssign3, a3['seq_id'], a3['comp_id'], a3['atom_id'], index)

                            if len(self.atomSelectionSet) == self.num_of_dim:
                                has_assignments = True
                                has_assignments &= self.fillAtomTypeInCase(1, self.atomSelectionSet[0][0]['atom_id'][0])
                                has_assignments &= self.fillAtomTypeInCase(2, self.atomSelectionSet[1][0]['atom_id'][0])
                                has_assignments &= self.fillAtomTypeInCase(3, self.atomSelectionSet[2][0]['atom_id'][0])
                                if has_assignments:
                                    self.atomSelectionSets.append(copy.copy(self.atomSelectionSet))
                                    self.asIsSets.append([asis1, asis2, asis3])
                                else:
                                    break
                            else:
                                has_assignments = False
                                break

            if self.createSfDict__:
                sf = self.getSf()

            if self.debug:
                if not has_assignments:
                    print(f"subtype={self.cur_subtype} id={self.peaks3D} (index={index}) "
                          f"{ass} -> None None None {dstFunc}")
                for idx, atomSelectionSet in enumerate(self.atomSelectionSets, start=1):
                    if has_multiple_assignments:
                        print(f"subtype={self.cur_subtype} id={self.peaks3D} (index={index}) combination_id={idx} "
                              f"{ass} -> {atomSelectionSet[0]} "
                              f"{atomSelectionSet[1]} "
                              f"{atomSelectionSet[2]} {dstFunc}")
                    else:
                        print(f"subtype={self.cur_subtype} id={self.peaks3D} (index={index}) "
                              f"{ass} -> {atomSelectionSet[0]} "
                              f"{atomSelectionSet[1]} "
                              f"{atomSelectionSet[2]} {dstFunc}")

            if self.createSfDict__ and sf is not None:
                sf['id'] = index
                sf['index_id'] += 1
                ambig_code1 = ambig_code2 = ambig_code3 = None
                if has_assignments and not has_multiple_assignments:
                    atom1 = self.atomSelectionSet[0][0]
                    atom2 = self.atomSelectionSet[1][0]
                    atom3 = self.atomSelectionSet[2][0]
                    if len(self.atomSelectionSet[0]) > 1:
                        ambig_code1 = self.csStat.getMaxAmbigCodeWoSetId(atom1['comp_id'], atom1['atom_id'])
                        if ambig_code1 == 0:
                            ambig_code1 = None
                    if len(self.atomSelectionSet[1]) > 1:
                        ambig_code2 = self.csStat.getMaxAmbigCodeWoSetId(atom2['comp_id'], atom2['atom_id'])
                        if ambig_code2 == 0:
                            ambig_code2 = None
                    if len(self.atomSelectionSet[2]) > 1:
                        ambig_code3 = self.csStat.getMaxAmbigCodeWoSetId(atom3['comp_id'], atom3['atom_id'])
                        if ambig_code3 == 0:
                            ambig_code3 = None
                else:
                    atom1 = atom2 = atom3 = None

                row = getPkRow(self.cur_subtype, sf['id'], sf['index_id'],
                               sf['list_id'], self.entryId, dstFunc,
                               self.authToStarSeq, self.authToOrigSeq, self.offsetHolder,
                               atom1, atom2, atom3, asis1=asis1, asis2=asis2, asis3=asis3,
                               ambig_code1=ambig_code1, ambig_code2=ambig_code2,
                               ambig_code3=ambig_code3,
                               details=None if has_assignments and not has_multiple_assignments else ass)
                sf['loop'].add_data(row)

                row = getPkGenCharRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc)
                sf['alt_loops'][0].add_data(row)
                for idx in range(self.num_of_dim):
                    row = getPkCharRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, idx + 1)
                    sf['alt_loops'][1].add_data(row)
                if has_assignments:
                    for atomSelectionSet, asIsSet in zip(self.atomSelectionSets, self.asIsSets):
                        uniqAtoms = []
                        for idx in range(self.num_of_dim):
                            atom = atomSelectionSet[idx]
                            atom0 = atom[0]
                            if atom0 not in uniqAtoms:
                                asis = asIsSet[idx]
                                ambig_code = None
                                if len(atom) > 1:
                                    ambig_code = self.csStat.getMaxAmbigCodeWoSetId(atom0['comp_id'], atom0['atom_id'])
                                    if ambig_code == 0:
                                        ambig_code = None
                                row = getPkChemShiftRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, idx + 1,
                                                        self.authToStarSeq, self.authToOrigSeq, self.offsetHolder,
                                                        atom0, asis, ambig_code)
                                sf['alt_loops'][2].add_data(row)
                                uniqAtoms.append(atom0)

        finally:
            self.numberSelection.clear()
            self.originalNumberSelection.clear()

    # Enter a parse tree produced by VnmrPKParser#peak_4d.
    def enterPeak_4d(self, ctx: VnmrPKParser.Peak_4dContext):  # pylint: disable=unused-argument
        if self.cur_subtype != 'peak4d':
            self.num_of_dim = 4
            self.initSpectralDim()

        self.peaks4D += 1

        self.atomSelectionSets.clear()
        self.asIsSets.clear()
        self.spectrum_name = None

    # Exit a parse tree produced by VnmrPKParser#peak_4d.
    def exitPeak_4d(self, ctx: VnmrPKParser.Peak_4dContext):

        try:

            if len(self.numberSelection) == 0:
                self.peaks4D -= 1
                return

            index = int(str(ctx.Integer()))

            ass = None
            if self.__has_assign and ctx.Assignment_4d_ex():
                ass = str(ctx.Assignment_4d_ex())
                if '?' in ass:
                    ass = None

            x_ppm = float(str(ctx.Float(0)))
            x_dev = abs(float(str(ctx.Float(1))))
            y_ppm = float(str(ctx.Float(2)))
            y_dev = abs(float(str(ctx.Float(3))))
            z_ppm = float(str(ctx.Float(4)))
            z_dev = abs(float(str(ctx.Float(5))))
            a_ppm = float(str(ctx.Float(6)))
            a_dev = abs(float(str(ctx.Float(7))))

            height = self.originalNumberSelection[0]
            volume = None
            if self.__has_volume:
                volume = self.originalNumberSelection[1]

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            if x_ppm is None or y_ppm is None or z_ppm is None or a_ppm is None:
                self.peaks4D -= 1
                return

            dstFunc = self.validatePeak4D(index, x_ppm, y_ppm, z_ppm, a_ppm, x_dev, y_dev, z_dev, a_dev, None, None, None, None,
                                          None, None, None, None, None, None, None, None, height, None, volume, None)

            if dstFunc is None:
                self.peaks4D -= 1
                return

            cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

            cur_spectral_dim[1]['freq_hint'].append(x_ppm)
            cur_spectral_dim[2]['freq_hint'].append(y_ppm)
            cur_spectral_dim[3]['freq_hint'].append(z_ppm)
            cur_spectral_dim[4]['freq_hint'].append(a_ppm)

            has_assignments = has_multiple_assignments = False
            asis1 = asis2 = asis3 = asis4 = None

            if ass is not None:
                assignments = []
                if len(ass.split('-')) == self.num_of_dim:
                    hint = None
                    for _ass in ass.split('-'):
                        assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                        hint = assignments[-1] if assignments[-1] is not None else None
                elif len(ass.split(':')) == self.num_of_dim:
                    hint = None
                    for _ass in ass.split(':'):
                        assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                        hint = assignments[-1] if assignments[-1] is not None else None
                elif len(ass.split(';')) == self.num_of_dim:
                    hint = None
                    for _ass in ass.split(';'):
                        assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                        hint = assignments[-1] if assignments[-1] is not None else None
                elif len(ass.split(',')) == self.num_of_dim:
                    hint = None
                    for _ass in ass.split(','):
                        assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                        hint = assignments[-1] if assignments[-1] is not None else None
                else:
                    assignments = [None] * self.num_of_dim
                    _assignments = self.extractPeakAssignment(self.num_of_dim, ass, index)
                    if _assignments is not None and len(_assignments) == self.num_of_dim:
                        for idx in range(self.num_of_dim):
                            assignments[idx] = [_assignments[idx]]  # pylint: disable=unsubscriptable-object

                if all(assignment is not None for assignment in assignments):

                    self.retrieveLocalSeqScheme()

                    hasChainId = all(a[0]['chain_id'] is not None for a in assignments)
                    hasCompId = all(a[0]['comp_id'] is not None for a in assignments)

                    has_multiple_assignments = any(len(assignment) > 1 for assignment in assignments)

                    for a1, a2, a3, a4 in zip_longest(assignments[0], assignments[1], assignments[2], assignments[3]):

                        self.atomSelectionSet.clear()
                        asis1 = asis2 = asis3 = asis4 = None

                        if hasChainId and hasCompId:
                            chainAssign1, asis1 = self.assignCoordPolymerSequenceWithChainId(a1['chain_id'], a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                            chainAssign2, asis2 = self.assignCoordPolymerSequenceWithChainId(a2['chain_id'], a2['seq_id'], a2['comp_id'], a2['atom_id'], index)
                            chainAssign3, asis3 = self.assignCoordPolymerSequenceWithChainId(a3['chain_id'], a3['seq_id'], a3['comp_id'], a3['atom_id'], index)
                            chainAssign4, asis4 = self.assignCoordPolymerSequenceWithChainId(a4['chain_id'], a4['seq_id'], a4['comp_id'], a4['atom_id'], index)

                        elif hasChainId:
                            chainAssign1 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a1['chain_id'], a1['seq_id'], a1['atom_id'], index)
                            chainAssign2 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a2['chain_id'], a2['seq_id'], a2['atom_id'], index)
                            chainAssign3 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a3['chain_id'], a3['seq_id'], a3['atom_id'], index)
                            chainAssign4 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a4['chain_id'], a4['seq_id'], a4['atom_id'], index)

                        elif hasCompId:
                            chainAssign1, asis1 = self.assignCoordPolymerSequence(a1['chain_id'], a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                            chainAssign2, asis2 = self.assignCoordPolymerSequence(a2['chain_id'], a2['seq_id'], a2['comp_id'], a2['atom_id'], index)
                            chainAssign3, asis3 = self.assignCoordPolymerSequence(a3['chain_id'], a3['seq_id'], a3['comp_id'], a3['atom_id'], index)
                            chainAssign4, asis4 = self.assignCoordPolymerSequence(a4['chain_id'], a4['seq_id'], a4['comp_id'], a4['atom_id'], index)

                        else:
                            chainAssign1 = self.assignCoordPolymerSequenceWithoutCompId(a1['seq_id'], a1['atom_id'], index)
                            chainAssign2 = self.assignCoordPolymerSequenceWithoutCompId(a2['seq_id'], a2['atom_id'], index)
                            chainAssign3 = self.assignCoordPolymerSequenceWithoutCompId(a3['seq_id'], a3['atom_id'], index)
                            chainAssign4 = self.assignCoordPolymerSequenceWithoutCompId(a4['seq_id'], a4['atom_id'], index)

                        if len(chainAssign1) > 0 and len(chainAssign2) > 0 and len(chainAssign3) > 0 and len(chainAssign4) > 0:
                            self.selectCoordAtoms(chainAssign1, a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                            self.selectCoordAtoms(chainAssign2, a2['seq_id'], a2['comp_id'], a2['atom_id'], index)
                            self.selectCoordAtoms(chainAssign3, a3['seq_id'], a3['comp_id'], a3['atom_id'], index)
                            self.selectCoordAtoms(chainAssign4, a4['seq_id'], a4['comp_id'], a4['atom_id'], index)

                            if len(self.atomSelectionSet) == self.num_of_dim:
                                has_assignments = True
                                has_assignments &= self.fillAtomTypeInCase(1, self.atomSelectionSet[0][0]['atom_id'][0])
                                has_assignments &= self.fillAtomTypeInCase(2, self.atomSelectionSet[1][0]['atom_id'][0])
                                has_assignments &= self.fillAtomTypeInCase(3, self.atomSelectionSet[2][0]['atom_id'][0])
                                has_assignments &= self.fillAtomTypeInCase(4, self.atomSelectionSet[3][0]['atom_id'][0])
                                if has_assignments:
                                    self.atomSelectionSets.append(copy.copy(self.atomSelectionSet))
                                    self.asIsSets.append([asis1, asis2, asis3, asis4])
                                else:
                                    break
                            else:
                                has_assignments = False
                                break

            if self.createSfDict__:
                sf = self.getSf()

            if self.debug:
                if not has_assignments:
                    print(f"subtype={self.cur_subtype} id={self.peaks4D} (index={index}) "
                          f"{ass} -> None None None None {dstFunc}")
                for idx, atomSelectionSet in enumerate(self.atomSelectionSets, start=1):
                    if has_multiple_assignments:
                        print(f"subtype={self.cur_subtype} id={self.peaks4D} (index={index}) combination_id={idx} "
                              f"{ass} -> {atomSelectionSet[0]} "
                              f"{atomSelectionSet[1]} "
                              f"{atomSelectionSet[2]} "
                              f"{atomSelectionSet[3]} {dstFunc}")
                    else:
                        print(f"subtype={self.cur_subtype} id={self.peaks4D} (index={index}) "
                              f"{ass} -> {atomSelectionSet[0]} "
                              f"{atomSelectionSet[1]} "
                              f"{atomSelectionSet[2]} "
                              f"{atomSelectionSet[3]} {dstFunc}")

            if self.createSfDict__ and sf is not None:
                sf['id'] = index
                sf['index_id'] += 1
                ambig_code1 = ambig_code2 = ambig_code3 = ambig_code4 = None
                if has_assignments and not has_multiple_assignments:
                    atom1 = self.atomSelectionSet[0][0]
                    atom2 = self.atomSelectionSet[1][0]
                    atom3 = self.atomSelectionSet[2][0]
                    atom4 = self.atomSelectionSet[3][0]
                    if len(self.atomSelectionSet[0]) > 1:
                        ambig_code1 = self.csStat.getMaxAmbigCodeWoSetId(atom1['comp_id'], atom1['atom_id'])
                        if ambig_code1 == 0:
                            ambig_code1 = None
                    if len(self.atomSelectionSet[1]) > 1:
                        ambig_code2 = self.csStat.getMaxAmbigCodeWoSetId(atom2['comp_id'], atom2['atom_id'])
                        if ambig_code2 == 0:
                            ambig_code2 = None
                    if len(self.atomSelectionSet[2]) > 1:
                        ambig_code3 = self.csStat.getMaxAmbigCodeWoSetId(atom3['comp_id'], atom3['atom_id'])
                        if ambig_code3 == 0:
                            ambig_code3 = None
                    if len(self.atomSelectionSet[3]) > 1:
                        ambig_code4 = self.csStat.getMaxAmbigCodeWoSetId(atom4['comp_id'], atom4['atom_id'])
                        if ambig_code4 == 0:
                            ambig_code4 = None
                else:
                    atom1 = atom2 = atom3 = atom4 = None

                row = getPkRow(self.cur_subtype, sf['id'], sf['index_id'],
                               sf['list_id'], self.entryId, dstFunc,
                               self.authToStarSeq, self.authToOrigSeq, self.offsetHolder,
                               atom1, atom2, atom3, atom4,
                               asis1=asis1, asis2=asis2, asis3=asis3, asis4=asis4,
                               ambig_code1=ambig_code1, ambig_code2=ambig_code2,
                               ambig_code3=ambig_code3, ambig_code4=ambig_code4,
                               details=None if has_assignments and not has_multiple_assignments else ass)
                sf['loop'].add_data(row)

                row = getPkGenCharRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc)
                sf['alt_loops'][0].add_data(row)
                for idx in range(self.num_of_dim):
                    row = getPkCharRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, idx + 1)
                    sf['alt_loops'][1].add_data(row)
                if has_assignments:
                    for atomSelectionSet, asIsSet in zip(self.atomSelectionSets, self.asIsSets):
                        uniqAtoms = []
                        for idx in range(self.num_of_dim):
                            atom = atomSelectionSet[idx]
                            atom0 = atom[0]
                            if atom0 not in uniqAtoms:
                                asis = asIsSet[idx]
                                ambig_code = None
                                if len(atom) > 1:
                                    ambig_code = self.csStat.getMaxAmbigCodeWoSetId(atom0['comp_id'], atom0['atom_id'])
                                    if ambig_code == 0:
                                        ambig_code = None
                                row = getPkChemShiftRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, idx + 1,
                                                        self.authToStarSeq, self.authToOrigSeq, self.offsetHolder,
                                                        atom0, asis, ambig_code)
                                sf['alt_loops'][2].add_data(row)
                                uniqAtoms.append(atom0)

        finally:
            self.numberSelection.clear()
            self.originalNumberSelection.clear()

    # Enter a parse tree produced by VnmrPKParser#number.
    def enterNumber(self, ctx: VnmrPKParser.NumberContext):
        if ctx.Float():
            value = str(ctx.Float())
            self.numberSelection.append(float(value))
            self.originalNumberSelection.append(value)

        elif ctx.Real():
            value = str(ctx.Real())
            self.numberSelection.append(float(value))
            self.originalNumberSelection.append(value)

        else:
            value = str(ctx.Integer())
            self.numberSelection.append(int(value))
            self.originalNumberSelection.append(value)

    # Exit a parse tree produced by VnmrPKParser#number.
    def exitNumber(self, ctx: VnmrPKParser.NumberContext):  # pylint: disable=unused-argument
        pass


# del VnmrPKParser
