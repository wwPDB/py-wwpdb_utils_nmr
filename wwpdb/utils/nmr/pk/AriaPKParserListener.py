##
# File: AriaPKParserListener.py
# Date: 05-Dec-2024
#
# Updates:
""" ParserLister class for ARIA PK files.
    @author: Masashi Yokochi
    @see: https://aria-test.pasteur.fr/documentation/input-format/version-2.1/spectrum
"""
import sys
import copy

from itertools import zip_longest
from antlr4 import ParseTreeListener

try:
    from wwpdb.utils.nmr.pk.XMLParser import XMLParser
    from wwpdb.utils.nmr.pk.BasePKParserListener import BasePKParserListener
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (REPRESENTATIVE_MODEL_ID,
                                                       REPRESENTATIVE_ALT_ID,
                                                       getPkRow,
                                                       getPkGenCharRow,
                                                       getPkCharRow,
                                                       getPkChemShiftRow)

except ImportError:
    from nmr.pk.XMLParser import XMLParser
    from nmr.pk.BasePKParserListener import BasePKParserListener
    from nmr.mr.ParserListenerUtil import (REPRESENTATIVE_MODEL_ID,
                                           REPRESENTATIVE_ALT_ID,
                                           getPkRow,
                                           getPkGenCharRow,
                                           getPkCharRow,
                                           getPkChemShiftRow)


# This class defines a complete listener for a parse tree produced by XMLParser.
class AriaPKParserListener(ParseTreeListener, BasePKParserListener):

    __cur_path = None

    __spectrum_names = None
    __spectrum_name = None

    __index = None
    __proton1_ppm = None
    __proton1_ppm_error = None
    __proton1_ass = None
    __proton1_atoms = None
    __proton2_ppm = None
    __proton2_ppm_error = None
    __proton2_ass = None
    __proton2_atoms = None
    __hetero1_ppm = None
    __hetero1_ppm_error = None
    __hetero1_ass = None
    __hetero1_atoms = None
    __hetero2_ppm = None
    __hetero2_ppm_error = None
    __hetero2_ass = None
    __hetero2_atoms = None
    __intensity = None
    __intensity_error = None
    __volume = None
    __volume_error = None

    __proton1_active = False
    __proton2_active = False
    __hetero1_active = False
    __hetero2_active = False

    def __init__(self, verbose=True, log=sys.stdout,
                 representativeModelId=REPRESENTATIVE_MODEL_ID,
                 representativeAltId=REPRESENTATIVE_ALT_ID,
                 mrAtomNameMapping=None,
                 cR=None, caC=None, ccU=None, csStat=None, nefT=None,
                 reasons=None):
        super().__init__(verbose, log, representativeModelId, representativeAltId,
                         mrAtomNameMapping, cR, caC, ccU, csStat, nefT, reasons)

        self.file_type = 'nm-pea-ari'
        self.software_name = 'ARIA'

    # Enter a parse tree produced by XMLParser#document.
    def enterDocument(self, ctx: XMLParser.DocumentContext):  # pylint: disable=unused-argument
        self.__cur_path = ''
        self.__spectrum_names = {}

        self.enter()

    # Exit a parse tree produced by XMLParser#document.
    def exitDocument(self, ctx: XMLParser.DocumentContext):  # pylint: disable=unused-argument
        self.exit(self.__spectrum_names)

    # Enter a parse tree produced by XMLParser#prolog.
    def enterProlog(self, ctx: XMLParser.PrologContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XMLParser#prolog.
    def exitProlog(self, ctx: XMLParser.PrologContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XMLParser#content.
    def enterContent(self, ctx: XMLParser.ContentContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XMLParser#content.
    def exitContent(self, ctx: XMLParser.ContentContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XMLParser#element.
    def enterElement(self, ctx: XMLParser.ElementContext):
        self.__cur_path += '/' + str(ctx.Name(0))

        if self.__cur_path == '/spectrum':
            self.num_of_dim = -1
            self.__spectrum_name = None

        elif self.__cur_path == '/spectrum/peak':
            self.__volume = None
            self.__volume_error = None
            self.__intensity = None
            self.__intensity_error = None

        elif self.__cur_path == '/spectrum/peak/proton1':
            self.__proton1_ppm = None
            self.__proton1_ppm_error = None
            self.__proton1_atoms = None

        elif self.__cur_path == '/spectrum/peak/proton2':
            self.__proton2_ppm = None
            self.__proton2_ppm_error = None
            self.__proton2_atoms = None

        elif self.__cur_path == '/spectrum/peak/hetero1':
            self.__hetero1_ppm = None
            self.__hetero1_ppm_error = None
            self.__hetero1_atoms = None

        elif self.__cur_path == '/spectrum/peak/hetero2':
            self.__hetero2_ppm = None
            self.__hetero2_ppm_error = None
            self.__hetero2_atoms = None

        elif self.__cur_path == '/spectrum/peak/proton1/assignment':
            self.__proton1_atoms = []

        elif self.__cur_path == '/spectrum/peak/proton2/assignment':
            self.__proton2_atoms = []

        elif self.__cur_path == '/spectrum/peak/hetero1/assignment':
            self.__hetero1_atoms = []

        elif self.__cur_path == '/spectrum/peak/hetero2/assignment':
            self.__hetero2_atoms = []

        elif self.__cur_path == '/spectrum/peak/proton1/assignment/atom':
            self.__proton1_ass = {}

        elif self.__cur_path == '/spectrum/peak/proton2/assignment/atom':
            self.__proton2_ass = {}

        elif self.__cur_path == '/spectrum/peak/hetero1/assignment/atom':
            self.__hetero1_ass = {}

        elif self.__cur_path == '/spectrum/peak/hetero2/assignment/atom':
            self.__hetero2_ass = {}

    # Exit a parse tree produced by XMLParser#element.
    def exitElement(self, ctx: XMLParser.ElementContext):  # pylint: disable=unused-argument

        if self.__cur_path == '/spectrum':
            self.num_of_dim = -1
            self.__proton1_active, self.__proton2_active, self.__hetero1_active, self.__hetero2_active =\
                False, False, False, False

        elif self.__cur_path == '/spectrum/peak':
            if self.num_of_dim == -1:
                self.num_of_dim = 0
                if self.__proton1_ppm is not None:
                    self.num_of_dim += 1
                    self.__proton1_active = True
                if self.__proton2_ppm is not None:
                    self.num_of_dim += 1
                    self.__proton2_active = True
                if self.__hetero1_ppm is not None:
                    self.num_of_dim += 1
                    self.__hetero1_active = True
                if self.__hetero2_ppm is not None:
                    self.num_of_dim += 1
                    self.__hetero2_active = True
                self.initSpectralDim()
                if self.num_of_dim not in self.__spectrum_names:
                    self.__spectrum_names[self.num_of_dim] = {}
                if self.cur_list_id not in self.__spectrum_names[self.num_of_dim]:
                    self.__spectrum_names[self.num_of_dim][self.cur_list_id] = self.__spectrum_name

            index = self.__index

            ppm = [None] * self.num_of_dim
            ppm_error = [None] * self.num_of_dim
            assignments = [None] * self.num_of_dim

            idx = 0
            if self.__proton1_active:
                ppm[idx] = self.__proton1_ppm
                ppm_error[idx] = self.__proton1_ppm_error
                if self.__proton1_atoms is not None:
                    assignments[idx] = self.__proton1_atoms
                    if len(self.__proton1_atoms) > 1:
                        if self.createSfDict__ and self.use_peak_row_format:
                            sf = self.getSf()
                            sf['peak_row_format'] = self.use_peak_row_format = False
                idx += 1
            if self.__proton2_active:
                ppm[idx] = self.__proton2_ppm
                ppm_error[idx] = self.__proton2_ppm_error
                if self.__proton2_atoms is not None:
                    assignments[idx] = self.__proton2_atoms
                    if len(self.__proton2_atoms) > 1:
                        if self.createSfDict__ and self.use_peak_row_format:
                            sf = self.getSf()
                            sf['peak_row_format'] = self.use_peak_row_format = False
                idx += 1
            if self.__hetero1_active:
                ppm[idx] = self.__hetero1_ppm
                ppm_error[idx] = self.__hetero1_ppm_error
                if self.__hetero1_atoms is not None:
                    assignments[idx] = self.__hetero1_atoms
                    if len(self.__hetero1_atoms) > 1:
                        if self.createSfDict__ and self.use_peak_row_format:
                            sf = self.getSf()
                            sf['peak_row_format'] = self.use_peak_row_format = False
                idx += 1
            if self.__hetero2_active:
                ppm[idx] = self.__hetero2_ppm
                ppm_error[idx] = self.__hetero2_ppm_error
                if self.__hetero2_atoms is not None:
                    assignments[idx] = self.__hetero2_atoms
                    if len(self.__hetero2_atoms) > 1:
                        if self.createSfDict__ and self.use_peak_row_format:
                            sf = self.getSf()
                            sf['peak_row_format'] = self.use_peak_row_format = False

            if not all(a is not None and len(a) >= 1 and 'seq_id' in a[0] and 'atom_id' in a[0] for a in assignments):
                assignments = [None] * self.num_of_dim

            if self.num_of_dim == 2:
                self.peaks2D += 1

                if None in (ppm[0], ppm[1])\
                   or (self.__intensity is None and self.__volume is None):
                    self.peaks2D -= 1
                    return

                dstFunc = self.validatePeak2D(index, ppm[0], ppm[1],
                                              ppm_error[0], ppm_error[1],
                                              None, None, None, None, None, None,
                                              self.__intensity, self.__intensity_error, self.__volume, self.__volume_error)

                if dstFunc is None:
                    self.peaks2D -= 1
                    return

                cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

                cur_spectral_dim[1]['freq_hint'].append(ppm[0])
                cur_spectral_dim[2]['freq_hint'].append(ppm[1])

                has_assignments = has_multiple_assignments = False
                asis1 = asis2 = None

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
                              f"None None {dstFunc}")
                    for idx, atomSelectionSet in enumerate(self.atomSelectionSets, start=1):
                        if has_multiple_assignments:
                            print(f"subtype={self.cur_subtype} id={self.peaks2D} (index={index}) combination_id={idx} "
                                  f"{atomSelectionSet[0]} "
                                  f"{atomSelectionSet[1]} {dstFunc}")
                        else:
                            print(f"subtype={self.cur_subtype} id={self.peaks2D} (index={index}) "
                                  f"{atomSelectionSet[0]} "
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
                                   ambig_code1=ambig_code1, ambig_code2=ambig_code2)
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
                                                            atom, asis, ambig_code)
                                    sf['alt_loop'][2].add_data(row)
                                    uniqAtoms.append(atom)

            elif self.num_of_dim == 3:
                self.peaks3D += 1

                if None in (ppm[0], ppm[1], ppm[2])\
                   or (self.__intensity is None and self.__volume is None):
                    self.peaks3D -= 1
                    return

                dstFunc = self.validatePeak3D(index, ppm[0], ppm[1], ppm[2],
                                              ppm_error[0], ppm_error[1], ppm_error[2],
                                              None, None, None, None, None, None, None, None, None,
                                              self.__intensity, self.__intensity_error, self.__volume, self.__volume_error)

                if dstFunc is None:
                    self.peaks3D -= 1
                    return

                cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

                cur_spectral_dim[1]['freq_hint'].append(ppm[0])
                cur_spectral_dim[2]['freq_hint'].append(ppm[1])
                cur_spectral_dim[3]['freq_hint'].append(ppm[2])

                has_assignments = has_multiple_assignments = False
                asis1 = asis2 = asis3 = None

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
                              f"None None None {dstFunc}")
                    for idx, atomSelectionSet in enumerate(self.atomSelectionSets, start=1):
                        if has_multiple_assignments:
                            print(f"subtype={self.cur_subtype} id={self.peaks3D} (index={index}) combination_id={idx} "
                                  f"{atomSelectionSet[0]} "
                                  f"{atomSelectionSet[1]} "
                                  f"{atomSelectionSet[2]} {dstFunc}")
                        else:
                            print(f"subtype={self.cur_subtype} id={self.peaks3D} (index={index}) "
                                  f"{atomSelectionSet[0]} "
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
                                   ambig_code3=ambig_code3)
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
                                                            atom, asis, ambig_code)
                                    sf['alt_loop'][2].add_data(row)
                                    uniqAtoms.append(atom)

            elif self.num_of_dim == 4:
                self.peaks4D += 1

                if None in (ppm[0], ppm[1], ppm[2], ppm[3])\
                   or (self.__intensity is None and self.__volume is None):
                    self.peaks4D -= 1
                    return

                dstFunc = self.validatePeak4D(index, ppm[0], ppm[1], ppm[2], ppm[3],
                                              ppm_error[0], ppm_error[1], ppm_error[2], ppm_error[3],
                                              None, None, None, None, None, None, None, None, None, None, None, None,
                                              self.__intensity, self.__intensity_error, self.__volume, self.__volume_error)

                if dstFunc is None:
                    self.peaks4D -= 1
                    return

                cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

                cur_spectral_dim[1]['freq_hint'].append(ppm[0])
                cur_spectral_dim[2]['freq_hint'].append(ppm[1])
                cur_spectral_dim[3]['freq_hint'].append(ppm[2])
                cur_spectral_dim[4]['freq_hint'].append(ppm[3])

                has_assignments = has_multiple_assignments = False
                asis1 = asis2 = asis3 = asis4 = None

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
                              f"None None None None {dstFunc}")
                    for idx, atomSelectionSet in enumerate(self.atomSelectionSets, start=1):
                        if has_multiple_assignments:
                            print(f"subtype={self.cur_subtype} id={self.peaks4D} (index={index}) combination_id={idx} "
                                  f"{atomSelectionSet[0]} "
                                  f"{atomSelectionSet[1]} "
                                  f"{atomSelectionSet[2]} "
                                  f"{atomSelectionSet[3]} {dstFunc}")
                        else:
                            print(f"subtype={self.cur_subtype} id={self.peaks4D} (index={index}) "
                                  f"{atomSelectionSet[0]} "
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
                                   ambig_code3=ambig_code3, ambig_code4=ambig_code4)
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
                                                            atom, asis, ambig_code)
                                    sf['alt_loop'][2].add_data(row)
                                    uniqAtoms.append(atom)

        elif self.__cur_path == '/spectrum/peak/proton1/assignment/atom':
            if len(self.__proton1_ass) > 0:
                self.__proton1_atoms.append(self.__proton1_ass)

        elif self.__cur_path == '/spectrum/peak/proton2/assignment/atom':
            if len(self.__proton2_ass) > 0:
                self.__proton2_atoms.append(self.__proton2_ass)

        elif self.__cur_path == '/spectrum/peak/hetero1/assignment/atom':
            if len(self.__hetero1_ass) > 0:
                self.__hetero1_atoms.append(self.__hetero1_ass)

        elif self.__cur_path == '/spectrum/peak/hetero2/assignment/atom':
            if len(self.__hetero2_ass) > 0:
                self.__hetero2_atoms.append(self.__hetero2_ass)

        self.__cur_path = self.__cur_path[:-(1 + len(str(ctx.Name(0))))]

    # Enter a parse tree produced by XMLParser#reference.
    def enterReference(self, ctx: XMLParser.ReferenceContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XMLParser#reference.
    def exitReference(self, ctx: XMLParser.ReferenceContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XMLParser#attribute.
    def enterAttribute(self, ctx: XMLParser.AttributeContext):

        if ctx.Name() and ctx.STRING():
            name = str(ctx.Name())
            string = str(ctx.STRING())[1:-1].strip()

            if self.__cur_path == '/spectrum':

                if name == 'name':
                    self.__spectrum_name = string

            elif self.__cur_path == '/spectrum/peak':

                if name == 'number':
                    self.__index = int(string)

            elif self.__cur_path == '/spectrum/peak/volume':

                if name == 'value':
                    self.__volume = string

                elif name == 'error' and len(string) > 0:
                    self.__volume_error = string

            elif self.__cur_path == '/spectrum/peak/intensity':

                if name == 'value':
                    self.__intensity = string

                elif name == 'error' and len(string) > 0:
                    self.__intensity_error = string

            elif self.__cur_path == '/spectrum/peak/proton1/shift' and len(string) > 0:

                if name == 'value':
                    self.__proton1_ppm = float(string)

                elif name == 'error':
                    self.__proton1_ppm_error = float(string)

            elif self.__cur_path == '/spectrum/peak/proton2/shift' and len(string) > 0:

                if name == 'value':
                    self.__proton2_ppm = float(string)

                elif name == 'error':
                    self.__proton2_ppm_error = float(string)

            elif self.__cur_path == '/spectrum/peak/hetero1/shift' and len(string) > 0:

                if name == 'value':
                    self.__hetero1_ppm = float(string)

                elif name == 'error':
                    self.__hetero1_ppm_error = float(string)

            elif self.__cur_path == '/spectrum/peak/hetero2/shift' and len(string) > 0:

                if name == 'value':
                    self.__hetero2_ppm = float(string)

                elif name == 'error':
                    self.__hetero2_ppm_error = float(string)

            elif self.__cur_path == '/spectrum/peak/proton1/assignment/atom' and len(string) > 0:

                if name == 'segid':
                    self.__proton1_ass['chain_id'] = string

                elif name == 'residue':
                    self.__proton1_ass['seq_id'] = string

                elif name == 'name':
                    self.__proton1_ass['atom_id'] = string

            elif self.__cur_path == '/spectrum/peak/proton2/assignment/atom' and len(string) > 0:

                if name == 'segid':
                    self.__proton2_ass['chain_id'] = string

                elif name == 'residue':
                    self.__proton2_ass['seq_id'] = string

                elif name == 'name':
                    self.__proton2_ass['atom_id'] = string

            elif self.__cur_path == '/spectrum/peak/hetero1/assignment/atom' and len(string) > 0:

                if name == 'segid':
                    self.__hetero1_ass['chain_id'] = string

                elif name == 'residue':
                    self.__hetero1_ass['seq_id'] = string

                elif name == 'name':
                    self.__hetero1_ass['atom_id'] = string

            elif self.__cur_path == '/spectrum/peak/hetero2/assignment/atom' and len(string) > 0:

                if name == 'segid':
                    self.__hetero2_ass['chain_id'] = string

                elif name == 'residue':
                    self.__hetero2_ass['seq_id'] = string

                elif name == 'name':
                    self.__hetero2_ass['atom_id'] = string

    # Exit a parse tree produced by XMLParser#attribute.
    def exitAttribute(self, ctx: XMLParser.AttributeContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XMLParser#chardata.
    def enterChardata(self, ctx: XMLParser.ChardataContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XMLParser#chardata.
    def exitChardata(self, ctx: XMLParser.ChardataContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XMLParser#misc.
    def enterMisc(self, ctx: XMLParser.MiscContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XMLParser#misc.
    def exitMisc(self, ctx: XMLParser.MiscContext):  # pylint: disable=unused-argument
        pass
