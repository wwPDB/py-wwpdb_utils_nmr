##
# File: NmrViewPKParserListener.py
# Date: 03-Dec-2024
#
# Updates:
""" ParserLister class for NMRVIEW PK files.
    @author: Masashi Yokochi
"""
import sys
import re
import copy

from itertools import zip_longest
from antlr4 import ParseTreeListener

try:
    from wwpdb.utils.nmr.pk.NmrViewPKParser import NmrViewPKParser
    from wwpdb.utils.nmr.pk.BasePKParserListener import BasePKParserListener
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS,
                                                       REPRESENTATIVE_MODEL_ID,
                                                       REPRESENTATIVE_ALT_ID,
                                                       SPECTRAL_DIM_TEMPLATE,
                                                       getPkRow,
                                                       getPkGenCharRow,
                                                       getPkCharRow,
                                                       getPkChemShiftRow)
    from wwpdb.utils.nmr.AlignUtil import emptyValue

except ImportError:
    from nmr.pk.NmrViewPKParser import NmrViewPKParser
    from nmr.pk.BasePKParserListener import BasePKParserListener
    from nmr.mr.ParserListenerUtil import (ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS,
                                           REPRESENTATIVE_MODEL_ID,
                                           REPRESENTATIVE_ALT_ID,
                                           SPECTRAL_DIM_TEMPLATE,
                                           getPkRow,
                                           getPkGenCharRow,
                                           getPkCharRow,
                                           getPkChemShiftRow)
    from nmr.AlignUtil import emptyValue


# This class defines a complete listener for a parse tree produced by NmrViewPKParser.
class NmrViewPKParserListener(ParseTreeListener, BasePKParserListener):

    __cur_label_type = None

    __labels = None
    __jcouplings = None

    def __init__(self, verbose=True, log=sys.stdout,
                 representativeModelId=REPRESENTATIVE_MODEL_ID,
                 representativeAltId=REPRESENTATIVE_ALT_ID,
                 mrAtomNameMapping=None,
                 cR=None, caC=None, ccU=None, csStat=None, nefT=None,
                 reasons=None):
        super().__init__(verbose, log, representativeModelId, representativeAltId,
                         mrAtomNameMapping, cR, caC, ccU, csStat, nefT, reasons)

        self.file_type = 'nm-pea-vie'
        self.software_name = 'NMRVIEW'

    # Enter a parse tree produced by NmrViewPKParser#nmrview_pk.
    def enterNmrview_pk(self, ctx: NmrViewPKParser.Nmrview_pkContext):  # pylint: disable=unused-argument
        self.enter()

    # Exit a parse tree produced by NmrViewPKParser#nmrview_pk.
    def exitNmrview_pk(self, ctx: NmrViewPKParser.Nmrview_pkContext):  # pylint: disable=unused-argument
        self.exit()

    # Enter a parse tree produced by NmrViewPKParser#data_label.
    def enterData_label(self, ctx: NmrViewPKParser.Data_labelContext):  # pylint: disable=unused-argument
        self.__labels = {}
        self.__cur_label_type = None

    # Exit a parse tree produced by NmrViewPKParser#data_label.
    def exitData_label(self, ctx: NmrViewPKParser.Data_labelContext):  # pylint: disable=unused-argument
        self.__labels = None
        self.__cur_label_type = None

    # Enter a parse tree produced by NmrViewPKParser#labels.
    def enterLabels(self, ctx: NmrViewPKParser.LabelsContext):  # pylint: disable=unused-argument:
        if self.__cur_label_type is None:
            self.__cur_label_type = 'label'
        elif self.__cur_label_type == 'label':
            self.__cur_label_type = 'sw'
        elif self.__cur_label_type == 'sw':
            self.__cur_label_type = 'sf'
        else:
            self.__cur_label_type = None
            return
        if self.__cur_label_type not in self.__labels:
            self.__labels[self.__cur_label_type] = []

    # Exit a parse tree produced by NmrViewPKParser#labels.
    def exitLabels(self, ctx: NmrViewPKParser.LabelsContext):  # pylint: disable=unused-argument:

        labels = self.__labels[self.__cur_label_type]

        if self.__cur_label_type == 'label':

            self.num_of_dim = len(labels)

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

        elif self.__cur_label_type == 'sw':

            for _dim_id, _spectral_width in enumerate(labels, start=1):
                self.cur_spectral_dim[_dim_id]['sweep_width'] = float(_spectral_width)
                self.cur_spectral_dim[_dim_id]['sweep_width_units'] = 'Hz'

        elif self.__cur_label_type == 'sf':

            for _dim_id, _freq in enumerate(labels, start=1):
                self.cur_spectral_dim[_dim_id]['spectrometer_frequency'] = float(_freq)

    # Enter a parse tree produced by NmrViewPKParser#peak_list_2d.
    def enterPeak_list_2d(self, ctx: NmrViewPKParser.Peak_list_2dContext):  # pylint: disable=unused-argument
        self.initSpectralDim()
        self.__jcouplings = []

    # Exit a parse tree produced by NmrViewPKParser#peak_list_2d.
    def exitPeak_list_2d(self, ctx: NmrViewPKParser.Peak_list_2dContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by NmrViewPKParser#peak_2d.
    def enterPeak_2d(self, ctx: NmrViewPKParser.Peak_2dContext):  # pylint: disable=unused-argument
        self.peaks2D += 1

        self.atomSelectionSets.clear()
        self.asIsSets.clear()
        self.__jcouplings.clear()

    # Exit a parse tree produced by NmrViewPKParser#peak_2d.
    def exitPeak_2d(self, ctx: NmrViewPKParser.Peak_2dContext):

        index = int(str(ctx.Integer(0)))

        L1 = str(ctx.ENCLOSE_DATA(0))[1:-1]
        P1 = float(str(ctx.Float(0)))
        W1 = float(str(ctx.Float(1)))
        B1 = float(str(ctx.Float(2)))
        # E1 = str(ctx.Simple_name(0))
        # J1 = self.__jcouplings[0]
        # U1 = str(ctx.ENCLOSE_DATA(1))[1:-1]

        L2 = str(ctx.ENCLOSE_DATA(2))[1:-1]
        P2 = float(str(ctx.Float(3)))
        W2 = float(str(ctx.Float(4)))
        B2 = float(str(ctx.Float(5)))
        # E2 = str(ctx.Simple_name(1))
        # J2 = self.__jcouplings[1]
        # U2 = str(ctx.ENCLOSE_DATA(3))[1:-1]

        vol = str(ctx.Float(6))
        _int = str(ctx.Float(7))
        stat = int(str(ctx.Integer(1)))
        if ctx.ENCLOSE_DATA(4):
            comment = str(ctx.ENCLOSE_DATA(4))[1:-1]
            if comment in emptyValue:
                comment = None
        else:
            comment = None
        # flag0 = int(str(ctx.Integer(2)))

        if L1 in emptyValue:
            L1 = None
        if L2 in emptyValue:
            L2 = None

        if not self.hasPolySeq and not self.hasNonPolySeq:
            return

        if P1 is None or P2 is None or stat != 0:
            self.peaks2D -= 1
            return

        dstFunc = self.validatePeak2D(index, P1, P2, B1, B2, W1, W2,
                                      None, None, None, None, _int, None, vol, None)

        if dstFunc is None:
            self.peaks2D -= 1
            return

        cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

        cur_spectral_dim[1]['freq_hint'].append(P1)
        cur_spectral_dim[2]['freq_hint'].append(P2)

        has_assignments = has_multiple_assignments = False
        asis1 = asis2 = None

        if L1 is not None and L2 is not None:
            assignments = [None] * self.num_of_dim
            if L1 is not None:
                ext = self.extractPeakAssignment(1, L1, index)
                if ext is not None:
                    assignments[0] = ext
            if L2 is not None:
                ext = self.extractPeakAssignment(1, L2, index)
                if ext is not None:
                    assignments[1] = ext

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
                      f"{L1} {L2} -> None None {dstFunc}")
            for idx, atomSelectionSet in enumerate(self.atomSelectionSets, start=1):
                if has_multiple_assignments:
                    print(f"subtype={self.cur_subtype} id={self.peaks2D} (index={index}) combination_id={idx} "
                          f"{L1} {L2} -> {atomSelectionSet[0]} "
                          f"{atomSelectionSet[1]} {dstFunc}")
                else:
                    print(f"subtype={self.cur_subtype} id={self.peaks2D} (index={index}) "
                          f"{L1} {L2} -> {atomSelectionSet[0]} "
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
                           details=comment)
            sf['loop'].add_data(row)

            row = getPkGenCharRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc)
            sf['alt_loop'][0].add_data(row)
            for idx in range(self.num_of_dim):
                row = getPkCharRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, idx + 1)
                sf['alt_loop'][1].add_data(row)
            if has_assignments:
                for atomSelectionSet, asIsSet in zip(self.atomSelectionSets, self.asIsSets):
                    uniqAtoms = []
                    for idx in range(self.num_of_dim):
                        atom = atomSelectionSet[idx]
                        if atom not in uniqAtoms:
                            asis = asIsSet[idx]
                            ambig_code = None
                            if len(atomSelectionSet) > 1:
                                ambig_code = self.csStat.getMaxAmbigCodeWoSetId(atom['comp_id'], atom['atom_id'])
                                if ambig_code == 0:
                                    ambig_code = None
                            row = getPkChemShiftRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, idx + 1,
                                                    self.authToStarSeq, self.authToOrigSeq, self.offsetHolder,
                                                    atom, asis, ambig_code, details=comment)
                            sf['alt_loop'][2].add_data(row)
                            uniqAtoms.append(atom)

    # Enter a parse tree produced by NmrViewPKParser#peak_list_3d.
    def enterPeak_list_3d(self, ctx: NmrViewPKParser.Peak_list_3dContext):  # pylint: disable=unused-argument
        self.initSpectralDim()
        self.__jcouplings = []

    # Exit a parse tree produced by NmrViewPKParser#peak_list_3d.
    def exitPeak_list_3d(self, ctx: NmrViewPKParser.Peak_list_3dContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by NmrViewPKParser#peak_3d.
    def enterPeak_3d(self, ctx: NmrViewPKParser.Peak_3dContext):  # pylint: disable=unused-argument
        self.peaks3D += 1

        self.atomSelectionSets.clear()
        self.asIsSets.clear()
        self.__jcouplings.clear()

    # Exit a parse tree produced by NmrViewPKParser#peak_3d.
    def exitPeak_3d(self, ctx: NmrViewPKParser.Peak_3dContext):

        index = int(str(ctx.Integer(0)))

        L1 = str(ctx.ENCLOSE_DATA(0))[1:-1]
        P1 = float(str(ctx.Float(0)))
        W1 = float(str(ctx.Float(1)))
        B1 = float(str(ctx.Float(2)))
        # E1 = str(ctx.Simple_name(0))
        # J1 = self.__jcouplings[0]
        # U1 = str(ctx.ENCLOSE_DATA(1))[1:-1]

        L2 = str(ctx.ENCLOSE_DATA(2))[1:-1]
        P2 = float(str(ctx.Float(3)))
        W2 = float(str(ctx.Float(4)))
        B2 = float(str(ctx.Float(5)))
        # E2 = str(ctx.Simple_name(1))
        # J2 = self.__jcouplings[1]
        # U2 = str(ctx.ENCLOSE_DATA(3))[1:-1]

        L3 = str(ctx.ENCLOSE_DATA(4))[1:-1]
        P3 = float(str(ctx.Float(6)))
        W3 = float(str(ctx.Float(7)))
        B3 = float(str(ctx.Float(8)))
        # E3 = str(ctx.Simple_name(2))
        # J3 = self.__jcouplings[2]
        # U3 = str(ctx.ENCLOSE_DATA(5))[1:-1]

        vol = str(ctx.Float(9))
        _int = str(ctx.Float(10))
        stat = int(str(ctx.Integer(1)))
        if ctx.ENCLOSE_DATA(6):
            comment = str(ctx.ENCLOSE_DATA(6))[1:-1]
            if comment in emptyValue:
                comment = None
        else:
            comment = None
        # flag0 = int(str(ctx.Integer(2)))

        if L1 in emptyValue:
            L1 = None
        if L2 in emptyValue:
            L2 = None
        if L3 in emptyValue:
            L3 = None

        if not self.hasPolySeq and not self.hasNonPolySeq:
            return

        if P1 is None or P2 is None or P3 is None or stat != 0:
            self.peaks3D -= 1
            return

        dstFunc = self.validatePeak3D(index, P1, P2, P3, B1, B2, B3, W1, W2, W3,
                                      None, None, None, None, None, None, _int, None, vol, None)

        if dstFunc is None:
            self.peaks3D -= 1
            return

        cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

        cur_spectral_dim[1]['freq_hint'].append(P1)
        cur_spectral_dim[2]['freq_hint'].append(P2)
        cur_spectral_dim[3]['freq_hint'].append(P3)

        has_assignments = has_multiple_assignments = False
        asis1 = asis2 = asis3 = None

        if L1 is not None and L2 is not None and L3 is not None:
            assignments = [None] * self.num_of_dim
            if L1 is not None:
                ext = self.extractPeakAssignment(1, L1, index)
                if ext is not None:
                    assignments[0] = ext
            if L2 is not None:
                ext = self.extractPeakAssignment(1, L2, index)
                if ext is not None:
                    assignments[1] = ext
            if L3 is not None:
                ext = self.extractPeakAssignment(1, L3, index)
                if ext is not None:
                    assignments[2] = ext

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
                      f"{L1} {L2} {L3} -> None None None {dstFunc}")
            for idx, atomSelectionSet in enumerate(self.atomSelectionSets, start=1):
                if has_multiple_assignments:
                    print(f"subtype={self.cur_subtype} id={self.peaks3D} (index={index}) combination_id={idx} "
                          f"{L1} {L2} {L3} -> {atomSelectionSet[0]} "
                          f"{atomSelectionSet[1]} "
                          f"{atomSelectionSet[2]} {dstFunc}")
                else:
                    print(f"subtype={self.cur_subtype} id={self.peaks3D} (index={index}) "
                          f"{L1} {L2} {L3} -> {atomSelectionSet[0]} "
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
                           ambig_code3=ambig_code3, details=comment)
            sf['loop'].add_data(row)

            row = getPkGenCharRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc)
            sf['alt_loop'][0].add_data(row)
            for idx in range(self.num_of_dim):
                row = getPkCharRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, idx + 1)
                sf['alt_loop'][1].add_data(row)
            if has_assignments:
                for atomSelectionSet, asIsSet in zip(self.atomSelectionSets, self.asIsSets):
                    uniqAtoms = []
                    for idx in range(self.num_of_dim):
                        atom = atomSelectionSet[idx]
                        if atom not in uniqAtoms:
                            asis = asIsSet[idx]
                            ambig_code = None
                            if len(atomSelectionSet) > 1:
                                ambig_code = self.csStat.getMaxAmbigCodeWoSetId(atom['comp_id'], atom['atom_id'])
                                if ambig_code == 0:
                                    ambig_code = None
                            row = getPkChemShiftRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, idx + 1,
                                                    self.authToStarSeq, self.authToOrigSeq, self.offsetHolder,
                                                    atom, asis, ambig_code, details=comment)
                            sf['alt_loop'][2].add_data(row)
                            uniqAtoms.append(atom)

    # Enter a parse tree produced by NmrViewPKParser#peak_list_4d.
    def enterPeak_list_4d(self, ctx: NmrViewPKParser.Peak_list_4dContext):  # pylint: disable=unused-argument
        self.initSpectralDim()
        self.__jcouplings = []

    # Exit a parse tree produced by NmrViewPKParser#peak_list_4d.
    def exitPeak_list_4d(self, ctx: NmrViewPKParser.Peak_list_4dContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by NmrViewPKParser#peak_4d.
    def enterPeak_4d(self, ctx: NmrViewPKParser.Peak_4dContext):  # pylint: disable=unused-argument
        self.peaks4D += 1

        self.atomSelectionSets.clear()
        self.asIsSets.clear()
        self.__jcouplings.clear()

    # Exit a parse tree produced by NmrViewPKParser#peak_4d.
    def exitPeak_4d(self, ctx: NmrViewPKParser.Peak_4dContext):

        index = int(str(ctx.Integer(0)))

        L1 = str(ctx.ENCLOSE_DATA(0))[1:-1]
        P1 = float(str(ctx.Float(0)))
        W1 = float(str(ctx.Float(1)))
        B1 = float(str(ctx.Float(2)))
        # E1 = str(ctx.Simple_name(0))
        # J1 = self.__jcouplings[0]
        # U1 = str(ctx.ENCLOSE_DATA(1))[1:-1]

        L2 = str(ctx.ENCLOSE_DATA(2))[1:-1]
        P2 = float(str(ctx.Float(3)))
        W2 = float(str(ctx.Float(4)))
        B2 = float(str(ctx.Float(5)))
        # E2 = str(ctx.Simple_name(1))
        # J2 = self.__jcouplings[1]
        # U2 = str(ctx.ENCLOSE_DATA(3))[1:-1]

        L3 = str(ctx.ENCLOSE_DATA(4))[1:-1]
        P3 = float(str(ctx.Float(6)))
        W3 = float(str(ctx.Float(7)))
        B3 = float(str(ctx.Float(8)))
        # E3 = str(ctx.Simple_name(2))
        # J3 = self.__jcouplings[2]
        # U3 = str(ctx.ENCLOSE_DATA(5))[1:-1]

        L4 = str(ctx.ENCLOSE_DATA(6))[1:-1]
        P4 = float(str(ctx.Float(9)))
        W4 = float(str(ctx.Float(10)))
        B4 = float(str(ctx.Float(11)))
        # E4 = str(ctx.Simple_name(3))
        # J4 = self.__jcouplings[3]
        # U4 = str(ctx.ENCLOSE_DATA(7))[1:-1]

        vol = str(ctx.Float(12))
        _int = str(ctx.Float(13))
        stat = int(str(ctx.Integer(1)))
        if ctx.ENCLOSE_DATA(8):
            comment = str(ctx.ENCLOSE_DATA(8))[1:-1]
            if comment in emptyValue:
                comment = None
        else:
            comment = None
        # flag0 = int(str(ctx.Integer(2)))

        if L1 in emptyValue:
            L1 = None
        if L2 in emptyValue:
            L2 = None
        if L3 in emptyValue:
            L3 = None
        if L4 in emptyValue:
            L4 = None

        if not self.hasPolySeq and not self.hasNonPolySeq:
            return

        if P1 is None or P2 is None or P3 is None or P4 is None or stat != 0:
            self.peaks4D -= 1
            return

        dstFunc = self.validatePeak4D(index, P1, P2, P3, P4, B1, B2, B3, B4, W1, W2, W3, W4,
                                      None, None, None, None, None, None, None, None, _int, None, vol, None)

        if dstFunc is None:
            self.peaks4D -= 1
            return

        cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

        cur_spectral_dim[1]['freq_hint'].append(P1)
        cur_spectral_dim[2]['freq_hint'].append(P2)
        cur_spectral_dim[3]['freq_hint'].append(P3)
        cur_spectral_dim[4]['freq_hint'].append(P4)

        has_assignments = has_multiple_assignments = False
        asis1 = asis2 = asis3 = asis4 = None

        if L1 is not None and L2 is not None and L3 is not None and L4 is not None:
            assignments = [None] * self.num_of_dim
            if L1 is not None:
                ext = self.extractPeakAssignment(1, L1, index)
                if ext is not None:
                    assignments[0] = ext
            if L2 is not None:
                ext = self.extractPeakAssignment(1, L2, index)
                if ext is not None:
                    assignments[1] = ext
            if L3 is not None:
                ext = self.extractPeakAssignment(1, L3, index)
                if ext is not None:
                    assignments[2] = ext
            if L4 is not None:
                ext = self.extractPeakAssignment(1, L4, index)
                if ext is not None:
                    assignments[3] = ext

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
                      f"{L1} {L2} {L3} {L4} -> None None None None {dstFunc}")
            for idx, atomSelectionSet in enumerate(self.atomSelectionSets, start=1):
                if has_multiple_assignments:
                    print(f"subtype={self.cur_subtype} id={self.peaks4D} (index={index}) combination_id={idx} "
                          f"{L1} {L2} {L3} {L4} -> {atomSelectionSet[0]} "
                          f"{atomSelectionSet[1]} "
                          f"{atomSelectionSet[2]} "
                          f"{atomSelectionSet[3]} {dstFunc}")
                else:
                    print(f"subtype={self.cur_subtype} id={self.peaks4D} (index={index}) "
                          f"{L1} {L2} {L3} {L4} -> {atomSelectionSet[0]} "
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
                           ambig_code3=ambig_code3, ambig_code4=ambig_code4, details=comment)
            sf['loop'].add_data(row)

            row = getPkGenCharRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc)
            sf['alt_loop'][0].add_data(row)
            for idx in range(self.num_of_dim):
                row = getPkCharRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, idx + 1)
                sf['alt_loop'][1].add_data(row)
            if has_assignments:
                for atomSelectionSet, asIsSet in zip(self.atomSelectionSets, self.asIsSets):
                    uniqAtoms = []
                    for idx in range(self.num_of_dim):
                        atom = atomSelectionSet[idx]
                        if atom not in uniqAtoms:
                            asis = asIsSet[idx]
                            ambig_code = None
                            if len(atomSelectionSet) > 1:
                                ambig_code = self.csStat.getMaxAmbigCodeWoSetId(atom['comp_id'], atom['atom_id'])
                                if ambig_code == 0:
                                    ambig_code = None
                            row = getPkChemShiftRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, idx + 1,
                                                    self.authToStarSeq, self.authToOrigSeq, self.offsetHolder,
                                                    atom, asis, ambig_code, details=comment)
                            sf['alt_loop'][2].add_data(row)
                            uniqAtoms.append(atom)

    # Enter a parse tree produced by NmrViewPKParser#peak_list_wo_eju_2d.
    def enterPeak_list_wo_eju_2d(self, ctx: NmrViewPKParser.Peak_list_wo_eju_2dContext):  # pylint: disable=unused-argument
        self.enterPeak_list_2d(ctx)

    # Exit a parse tree produced by NmrViewPKParser#peak_list_wo_eju_2d.
    def exitPeak_list_wo_eju_2d(self, ctx: NmrViewPKParser.Peak_list_wo_eju_2dContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by NmrViewPKParser#peak_wo_eju_2d.
    def enterPeak_wo_eju_2d(self, ctx: NmrViewPKParser.Peak_wo_eju_2dContext):  # pylint: disable=unused-argument
        self.enterPeak_2d(ctx)

    # Exit a parse tree produced by NmrViewPKParser#peak_wo_eju_2d.
    def exitPeak_wo_eju_2d(self, ctx: NmrViewPKParser.Peak_wo_eju_2dContext):

        index = int(str(ctx.Integer(0)))

        L1 = str(ctx.ENCLOSE_DATA(0))[1:-1]
        P1 = float(str(ctx.Float(0)))
        W1 = float(str(ctx.Float(1)))
        B1 = float(str(ctx.Float(2)))

        L2 = str(ctx.ENCLOSE_DATA(1))[1:-1]
        P2 = float(str(ctx.Float(3)))
        W2 = float(str(ctx.Float(4)))
        B2 = float(str(ctx.Float(5)))

        vol = str(ctx.Float(6))
        _int = str(ctx.Float(7))
        stat = int(str(ctx.Integer(1)))
        if ctx.ENCLOSE_DATA(2):
            comment = str(ctx.ENCLOSE_DATA(2))[1:-1]
            if comment in emptyValue:
                comment = None
        else:
            comment = None
        # flag0 = int(str(ctx.Integer(2)))

        if L1 in emptyValue:
            L1 = None
        if L2 in emptyValue:
            L2 = None

        if not self.hasPolySeq and not self.hasNonPolySeq:
            return

        if P1 is None or P2 is None or stat != 0:
            self.peaks2D -= 1
            return

        dstFunc = self.validatePeak2D(index, P1, P2, B1, B2, W1, W2,
                                      None, None, None, None, _int, None, vol, None)

        if dstFunc is None:
            self.peaks2D -= 1
            return

        cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

        cur_spectral_dim[1]['freq_hint'].append(P1)
        cur_spectral_dim[2]['freq_hint'].append(P2)

        has_assignments = False

        asis1 = asis2 = None

        if L1 is not None and L2 is not None:
            assignments = [{}] * self.num_of_dim

            assignment0 = self.extractPeakAssignment(1, L1, index)
            if assignment0 is not None:
                a1 = assignment0[0]
            assignment1 = self.extractPeakAssignment(1, L2, index)
            if assignment1 is not None:
                a2 = assignment1[0]

            if all(len(a) > 0 for a in assignments):

                self.retrieveLocalSeqScheme()

                hasChainId = all(a['chain_id'] is not None for a in assignments)
                hasCompId = all(a['comp_id'] is not None for a in assignments)

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

        if self.createSfDict__:
            sf = self.getSf()

        if self.debug:
            print(f"subtype={self.cur_subtype} id={self.peaks2D} (index={index}) "
                  f"{L1}, {L2} -> {self.atomSelectionSet[0] if has_assignments else None} {self.atomSelectionSet[1] if has_assignments else None} {dstFunc}")

        if self.createSfDict__ and sf is not None:
            sf['id'] = index
            sf['index_id'] += 1
            ambig_code1 = ambig_code2 = None
            if has_assignments:
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
                           details=comment)
            sf['loop'].add_data(row)

    # Enter a parse tree produced by NmrViewPKParser#peak_list_wo_eju_3d.
    def enterPeak_list_wo_eju_3d(self, ctx: NmrViewPKParser.Peak_list_wo_eju_3dContext):  # pylint: disable=unused-argument
        self.enterPeak_list_3d(ctx)

    # Exit a parse tree produced by NmrViewPKParser#peak_list_wo_eju_3d.
    def exitPeak_list_wo_eju_3d(self, ctx: NmrViewPKParser.Peak_list_wo_eju_3dContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by NmrViewPKParser#peak_wo_eju_3d.
    def enterPeak_wo_eju_3d(self, ctx: NmrViewPKParser.Peak_wo_eju_3dContext):  # pylint: disable=unused-argument
        self.enterPeak_3d(ctx)

    # Exit a parse tree produced by NmrViewPKParser#peak_wo_eju_3d.
    def exitPeak_wo_eju_3d(self, ctx: NmrViewPKParser.Peak_wo_eju_3dContext):

        index = int(str(ctx.Integer(0)))

        L1 = str(ctx.ENCLOSE_DATA(0))[1:-1]
        P1 = float(str(ctx.Float(0)))
        W1 = float(str(ctx.Float(1)))
        B1 = float(str(ctx.Float(2)))

        L2 = str(ctx.ENCLOSE_DATA(1))[1:-1]
        P2 = float(str(ctx.Float(3)))
        W2 = float(str(ctx.Float(4)))
        B2 = float(str(ctx.Float(5)))

        L3 = str(ctx.ENCLOSE_DATA(2))[1:-1]
        P3 = float(str(ctx.Float(6)))
        W3 = float(str(ctx.Float(7)))
        B3 = float(str(ctx.Float(8)))

        vol = str(ctx.Float(9))
        _int = str(ctx.Float(10))
        stat = int(str(ctx.Integer(1)))
        if ctx.ENCLOSE_DATA(3):
            comment = str(ctx.ENCLOSE_DATA(3))[1:-1]
            if comment in emptyValue:
                comment = None
        else:
            comment = None
        # flag0 = int(str(ctx.Integer(2)))

        if L1 in emptyValue:
            L1 = None
        if L2 in emptyValue:
            L2 = None
        if L3 in emptyValue:
            L3 = None

        if not self.hasPolySeq and not self.hasNonPolySeq:
            return

        if P1 is None or P2 is None or P3 is None or stat != 0:
            self.peaks3D -= 1
            return

        dstFunc = self.validatePeak3D(index, P1, P2, P3, B1, B2, B3, W1, W2, W3,
                                      None, None, None, None, None, None, _int, None, vol, None)

        if dstFunc is None:
            self.peaks3D -= 1
            return

        cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

        cur_spectral_dim[1]['freq_hint'].append(P1)
        cur_spectral_dim[2]['freq_hint'].append(P2)
        cur_spectral_dim[3]['freq_hint'].append(P3)

        has_assignments = False

        asis1 = asis2 = asis3 = None

        if L1 is not None and L2 is not None and L3 is not None:
            assignments = [{}] * self.num_of_dim

            assignment0 = self.extractPeakAssignment(1, L1, index)
            if assignment0 is not None:
                a1 = assignment0[0]
            assignment1 = self.extractPeakAssignment(1, L2, index)
            if assignment1 is not None:
                a2 = assignment1[0]
            assignment2 = self.extractPeakAssignment(1, L3, index)
            if assignment2 is not None:
                a3 = assignment2[0]

            if all(len(a) > 0 for a in assignments):

                self.retrieveLocalSeqScheme()

                hasChainId = all(a['chain_id'] is not None for a in assignments)
                hasCompId = all(a['comp_id'] is not None for a in assignments)

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

        if self.createSfDict__:
            sf = self.getSf()

        if self.debug:
            print(f"subtype={self.cur_subtype} id={self.peaks3D} (index={index}) "
                  f"{L1}, {L2}, {L3} -> {self.atomSelectionSet[0] if has_assignments else None} {self.atomSelectionSet[1] if has_assignments else None} "
                  f"{self.atomSelectionSet[2] if has_assignments else None} {dstFunc}")

        if self.createSfDict__ and sf is not None:
            sf['id'] = index
            sf['index_id'] += 1
            ambig_code1 = ambig_code2 = ambig_code3 = None
            if has_assignments:
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
                           ambig_code1=ambig_code1, ambig_code2=ambig_code2, ambig_code3=ambig_code3,
                           details=comment)
            sf['loop'].add_data(row)

    # Enter a parse tree produced by NmrViewPKParser#peak_list_wo_eju_4d.
    def enterPeak_list_wo_eju_4d(self, ctx: NmrViewPKParser.Peak_list_wo_eju_4dContext):  # pylint: disable=unused-argument
        self.enterPeak_list_4d(ctx)

    # Exit a parse tree produced by NmrViewPKParser#peak_list_wo_eju_4d.
    def exitPeak_list_wo_eju_4d(self, ctx: NmrViewPKParser.Peak_list_wo_eju_4dContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by NmrViewPKParser#peak_wo_eju_4d.
    def enterPeak_wo_eju_4d(self, ctx: NmrViewPKParser.Peak_wo_eju_4dContext):  # pylint: disable=unused-argument
        self.enterPeak_4d(ctx)

    # Exit a parse tree produced by NmrViewPKParser#peak_wo_eju_4d.
    def exitPeak_wo_eju_4d(self, ctx: NmrViewPKParser.Peak_wo_eju_4dContext):

        index = int(str(ctx.Integer(0)))

        L1 = str(ctx.ENCLOSE_DATA(0))[1:-1]
        P1 = float(str(ctx.Float(0)))
        W1 = float(str(ctx.Float(1)))
        B1 = float(str(ctx.Float(2)))

        L2 = str(ctx.ENCLOSE_DATA(1))[1:-1]
        P2 = float(str(ctx.Float(3)))
        W2 = float(str(ctx.Float(4)))
        B2 = float(str(ctx.Float(5)))

        L3 = str(ctx.ENCLOSE_DATA(2))[1:-1]
        P3 = float(str(ctx.Float(6)))
        W3 = float(str(ctx.Float(7)))
        B3 = float(str(ctx.Float(8)))

        L4 = str(ctx.ENCLOSE_DATA(3))[1:-1]
        P4 = float(str(ctx.Float(9)))
        W4 = float(str(ctx.Float(10)))
        B4 = float(str(ctx.Float(11)))

        vol = str(ctx.Float(12))
        _int = str(ctx.Float(13))
        stat = int(str(ctx.Integer(1)))
        if ctx.ENCLOSE_DATA(4):
            comment = str(ctx.ENCLOSE_DATA(4))[1:-1]
            if comment in emptyValue:
                comment = None
        else:
            comment = None
        # flag0 = int(str(ctx.Integer(2)))

        if L1 in emptyValue:
            L1 = None
        if L2 in emptyValue:
            L2 = None
        if L3 in emptyValue:
            L3 = None
        if L4 in emptyValue:
            L4 = None

        if not self.hasPolySeq and not self.hasNonPolySeq:
            return

        if P1 is None or P2 is None or P3 is None or P4 is None or stat != 0:
            self.peaks4D -= 1
            return

        dstFunc = self.validatePeak4D(index, P1, P2, P3, P4, B1, B2, B3, B4, W1, W2, W3, W4,
                                      None, None, None, None, None, None, None, None, _int, None, vol, None)

        if dstFunc is None:
            self.peaks4D -= 1
            return

        cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

        cur_spectral_dim[1]['freq_hint'].append(P1)
        cur_spectral_dim[2]['freq_hint'].append(P2)
        cur_spectral_dim[3]['freq_hint'].append(P3)
        cur_spectral_dim[4]['freq_hint'].append(P4)

        has_assignments = False

        asis1 = asis2 = asis3 = asis4 = None

        if L1 is not None and L2 is not None and L3 is not None and L4 is not None:
            assignments = [{}] * self.num_of_dim

            assignment0 = self.extractPeakAssignment(1, L1, index)
            if assignment0 is not None:
                a1 = assignment0[0]
            assignment1 = self.extractPeakAssignment(1, L2, index)
            if assignment1 is not None:
                a2 = assignment1[0]
            assignment2 = self.extractPeakAssignment(1, L3, index)
            if assignment2 is not None:
                a3 = assignment2[0]
            assignment3 = self.extractPeakAssignment(1, L4, index)
            if assignment3 is not None:
                a4 = assignment3[0]

            if all(len(a) > 0 for a in assignments):

                self.retrieveLocalSeqScheme()

                hasChainId = all(a['chain_id'] is not None for a in assignments)
                hasCompId = all(a['comp_id'] is not None for a in assignments)

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

                if len(chainAssign1) > 0 and len(chainAssign2) > 0 and len(chainAssign3) > 0 and len(chainAssign4):
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

        if self.createSfDict__:
            sf = self.getSf()

        if self.debug:
            print(f"subtype={self.cur_subtype} id={self.peaks4D} (index={index}) "
                  f"{L1}, {L2}, {L3}, {L4} -> {self.atomSelectionSet[0] if has_assignments else None} {self.atomSelectionSet[1] if has_assignments else None} "
                  f"{self.atomSelectionSet[2] if has_assignments else None} {self.atomSelectionSet[3] if has_assignments else None} {dstFunc}")

        if self.createSfDict__ and sf is not None:
            sf['id'] = index
            sf['index_id'] += 1
            ambig_code1 = ambig_code2 = ambig_code3 = ambig_code4 = None
            if has_assignments:
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
                           atom1, atom2, atom3, atom4, asis1=asis1, asis2=asis2, asis3=asis3, asis4=asis4,
                           ambig_code1=ambig_code1, ambig_code2=ambig_code2, ambig_code3=ambig_code3, ambig_code4=ambig_code4,
                           details=comment)
            sf['loop'].add_data(row)

    # Enter a parse tree produced by NmrViewPKParser#label.
    def enterLabel(self, ctx: NmrViewPKParser.LabelContext):
        if ctx.Float_LA():
            self.__labels[self.__cur_label_type].append(float(str(ctx.Float_LA())))
        elif ctx.Simple_name_LA():
            self.__labels[self.__cur_label_type].append(str(ctx.Simple_name_LA()))
        else:
            value = str(ctx.ENCLOSE_DATA_LA())[1:-1].strip()
            if self.__cur_label_type == 'label':
                self.__labels[self.__cur_label_type].append(value)
            else:
                self.__labels[self.__cur_label_type].append(float(value))

    # Exit a parse tree produced by NmrViewPKParser#label.
    def exitLabel(self, ctx: NmrViewPKParser.LabelContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by NmrViewPKParser#jcoupling.
    def enterJcoupling(self, ctx: NmrViewPKParser.JcouplingContext):
        if ctx.Float():
            self.__jcouplings.append(float(str(ctx.Float())))
        elif ctx.Simple_name():
            self.__jcouplings.append(str(ctx.Simple_name()))
        else:
            value = str(ctx.ENCLOSE_DATA())[1:-1].strip()
            try:
                _value = float(value)
                self.__jcouplings.append(_value)
            except ValueError:
                self.__jcouplings.append(value)

    # Exit a parse tree produced by NmrViewPKParser#jcoupling.
    def exitJcoupling(self, ctx: NmrViewPKParser.JcouplingContext):  # pylint: disable=unused-argument
        pass


# del NmrViewPKParser
