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
import numpy as np

from antlr4 import ParseTreeListener

try:
    from wwpdb.utils.nmr.pk.XMLParser import XMLParser
    from wwpdb.utils.nmr.pk.BasePKParserListener import BasePKParserListener
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (REPRESENTATIVE_MODEL_ID,
                                                       REPRESENTATIVE_ALT_ID,
                                                       getPkRow)

except ImportError:
    from nmr.pk.XMLParser import XMLParser
    from nmr.pk.BasePKParserListener import BasePKParserListener
    from nmr.mr.ParserListenerUtil import (REPRESENTATIVE_MODEL_ID,
                                           REPRESENTATIVE_ALT_ID,
                                           getPkRow)


# This class defines a complete listener for a parse tree produced by XMLParser.
class AriaPKParserListener(ParseTreeListener, BasePKParserListener):

    __cur_path = None

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

        self.enter()

    # Exit a parse tree produced by XMLParser#document.
    def exitDocument(self, ctx: XMLParser.DocumentContext):  # pylint: disable=unused-argument

        if len(self.spectral_dim) > 0:
            for d, v in self.spectral_dim.items():
                for _id, _v in v.items():
                    self.acq_dim_id = 1
                    for __d, __v in _v.items():
                        if 'freq_hint' in __v:
                            if len(__v['freq_hint']) > 0:
                                center = np.mean(np.array(__v['freq_hint']))

                                if __v['atom_isotope_number'] is None:
                                    if 125 < center < 130:
                                        __v['atom_type'] = 'C'
                                        __v['atom_isotope_number'] = 13
                                        __v['axis_code'] = 'C_aro'
                                    elif 115 < center < 125:
                                        __v['atom_type'] = 'N'
                                        __v['atom_isotope_number'] = 15
                                        __v['axis_code'] = 'N_ami'
                                    elif 170 < center < 180:
                                        __v['atom_type'] = 'C'
                                        __v['atom_isotope_number'] = 13
                                        __v['axis_code'] = 'CO'
                                    elif 6 < center < 9:
                                        __v['atom_type'] = 'H'
                                        __v['atom_isotope_number'] = 1
                                        __v['axis_code'] = 'H_ami_or_aro'
                                    elif 4 < center < 6:
                                        __v['atom_type'] = 'H'
                                        __v['atom_isotope_number'] = 1
                                        __v['axis_code'] = 'H'
                                    elif 2 < center < 4:
                                        __v['atom_type'] = 'H'
                                        __v['atom_isotope_number'] = 1
                                        __v['axis_code'] = 'H_ali'
                                    elif 60 < center < 90:
                                        __v['atom_type'] = 'C'
                                        __v['atom_isotope_number'] = 13
                                        __v['axis_code'] = 'C'
                                    elif 30 < center < 50:
                                        __v['atom_type'] = 'C'
                                        __v['atom_isotope_number'] = 13
                                        __v['axis_code'] = 'C_ali'

                                isotope_number = __v['atom_isotope_number']

                                if isotope_number is not None:
                                    __v['acquisition'] = 'yes' if __d == self.acq_dim_id\
                                        and (isotope_number == 1 or (isotope_number == 13 and self.exptlMethod == 'SOLID-STATE NMR')) else 'no'

                                    if __d == 1 and __v['acquisition'] == 'no':
                                        self.acq_dim_id = self.num_of_dim

                                    __v['under_sampling_type'] = 'not observed' if __v['acquisition'] == 'yes' else 'aliased'

                            if __v['spectral_region'] is None and len(__v['freq_hint']) > 0:
                                atom_type = __v['atom_type']
                                if 125 < center < 130 and atom_type == 'C':
                                    __v['spectral_region'] = 'C_aro'
                                elif 115 < center < 125 and atom_type == 'N':
                                    __v['spectral_region'] = 'N_ami'
                                elif 170 < center < 180 and atom_type == 'C':
                                    __v['spectral_region'] = 'CO'
                                elif 6 < center < 9 and atom_type == 'H':
                                    __v['spectral_region'] = 'H_ami_or_aro'
                                elif 4 < center < 6 and atom_type == 'H':
                                    __v['spectral_region'] = 'H_all'
                                elif 2 < center < 4 and atom_type == 'H':
                                    __v['spectral_region'] = 'H_ali'
                                elif 60 < center < 90 and atom_type == 'C':
                                    __v['spectral_region'] = 'C_all'
                                elif 30 < center < 50 and atom_type == 'C':
                                    __v['spectral_region'] = 'C_ali'

                            if len(__v['freq_hint']) > 0 and d > 2 and __d >= 2\
                               and self.exptlMethod != 'SOLID-STATE NMR' and __v['atom_isotope_number'] == 13:
                                max_ppm = max(__v['freq_hint'])
                                min_ppm = min(__v['freq_hint'])
                                width = max_ppm - min_ppm
                                if center < 100.0 and width < 50.0:
                                    __v['under_sampling_type'] = 'fold'

                            del __v['freq_hint']

                    for __v in _v.values():
                        if __v['axis_code'] == 'H_ami_or_aro':
                            has_a = any(___v['spectral_region'] == 'C_aro' for ___v in _v.values())
                            __v['axis_code'] = 'H_aro' if has_a else 'H_ami'
                        if __v['spectral_region'] == 'H_ami_or_aro':
                            has_a = any(___v['spectral_region'] == 'C_aro' for ___v in _v.values())
                            __v['spectral_region'] = 'H_aro' if has_a else 'H_ami'

                    if self.debug:
                        print(f'num_of_dim: {d}, list_id: {_id}')
                        for __d, __v in _v.items():
                            print(f'{__d} {__v}')

        self.exit()

        self.__cur_path = None

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

        elif self.__cur_path == '/spectrum/peak':
            if self.num_of_dim == -1:
                self.num_of_dim = 0
                if self.__proton1_ppm is not None:
                    self.num_of_dim += 1
                if self.__proton2_ppm is not None:
                    self.num_of_dim += 1
                if self.__hetero1_ppm is not None:
                    self.num_of_dim += 1
                if self.__hetero2_ppm is not None:
                    self.num_of_dim += 1
                self.fillCurrentSpectralDim()

            if self.num_of_dim == 2:
                self.peaks2D += 1

                ppm = [None] * self.num_of_dim
                ppm_error = [None] * self.num_of_dim
                ass = [None] * self.num_of_dim

                idx = 0
                if self.__proton1_ppm is not None:
                    ppm[idx] = self.__proton1_ppm
                    ppm_error[idx] = self.__proton1_ppm_error
                    if self.__proton1_atoms is not None and len(self.__proton1_atoms) == 1:
                        ass[idx] = self.__proton1_atoms
                    idx += 1
                if self.__proton2_ppm is not None:
                    ppm[idx] = self.__proton2_ppm
                    ppm_error[idx] = self.__proton2_ppm_error
                    if self.__proton2_atoms is not None and len(self.__proton2_atoms) == 1:
                        ass[idx] = self.__proton2_atoms
                    idx += 1
                if self.__hetero1_ppm is not None:
                    ppm[idx] = self.__hetero1_ppm
                    ppm_error[idx] = self.__hetero1_ppm_error
                    if self.__hetero1_atoms is not None and len(self.__hetero1_atoms) == 1:
                        ass[idx] = self.__hetero1_atoms
                    idx += 1
                if self.__hetero2_ppm is not None:
                    ppm[idx] = self.__hetero2_ppm
                    ppm_error[idx] = self.__hetero2_ppm_error
                    if self.__hetero2_atoms is not None and len(self.__hetero2_atoms) == 1:
                        ass[idx] = self.__hetero2_atoms

                if not all(a is not None and len(a) == 1 and 'seq_id' in a[0] and 'atom_id' in a[0] for a in ass):
                    ass = [None] * self.num_of_dim

                if None in (ppm[0], ppm[1])\
                   or (self.__intensity is None and self.__volume is None):
                    self.peaks2D -= 1
                    return

                index = self.__index

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

                has_assignments = False
                L1 = L2 = None

                if ass[0] is not None and ass[1] is not None:
                    assignments = [{}] * self.num_of_dim

                    _a1, _a2 = ass[0][0], ass[1][0]
                    L1 = f"{_a1['chain_id']} {_a1['seq_id']} {_a1['atom_id']}" if 'chain_id' in _a1 else f"{_a1['seq_id']} {_a1['atom_id']}"
                    L2 = f"{_a2['chain_id']} {_a2['seq_id']} {_a2['atom_id']}" if 'chain_id' in _a2 else f"{_a2['seq_id']} {_a2['atom_id']}"

                    assignment0 = self.extractPeakAssignment(1, L1, index)
                    if assignment0 is not None:
                        assignments[0] = assignment0[0]
                    assignment1 = self.extractPeakAssignment(1, L2, index)
                    if assignment1 is not None:
                        assignments[1] = assignment1[0]

                    if all(len(a) > 0 for a in assignments):

                        self.retrieveLocalSeqScheme()

                        hasChainId = all(a['chain_id'] is not None for a in assignments)
                        hasCompId = all(a['comp_id'] is not None for a in assignments)

                        a1 = assignments[0]
                        a2 = assignments[1]

                        if hasChainId and hasCompId:
                            chainAssign1, asis1 = self.assignCoordPolymerSequenceWithChainId(a1['chain_id'], a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                            chainAssign2, asis2 = self.assignCoordPolymerSequenceWithChainId(a2['chain_id'], a2['seq_id'], a2['comp_id'], a2['atom_id'], index)

                        elif hasChainId:
                            chainAssign1 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a1['chain_id'], a1['seq_id'], a1['atom_id'], index)
                            chainAssign2 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a2['chain_id'], a2['seq_id'], a2['atom_id'], index)
                            asis1 = asis2 = False

                        elif hasCompId:
                            chainAssign1, asis1 = self.assignCoordPolymerSequence(a1['chain_id'], a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                            chainAssign2, asis2 = self.assignCoordPolymerSequence(a2['chain_id'], a2['seq_id'], a2['comp_id'], a2['atom_id'], index)

                        else:
                            chainAssign1 = self.assignCoordPolymerSequenceWithoutCompId(a1['seq_id'], a1['atom_id'], index)
                            chainAssign2 = self.assignCoordPolymerSequenceWithoutCompId(a2['seq_id'], a2['atom_id'], index)
                            asis1 = asis2 = False

                        if len(chainAssign1) > 0 and len(chainAssign2) > 0:
                            self.selectCoordAtoms(chainAssign1, a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                            self.selectCoordAtoms(chainAssign2, a2['seq_id'], a2['comp_id'], a2['atom_id'], index)

                            if len(self.atomSelectionSet) == self.num_of_dim:
                                has_assignments = True

                if self.createSfDict__:
                    sf = self.getSf()

                if self.debug:
                    print(f"subtype={self.cur_subtype} id={self.peaks2D} (index={index}) "
                          f"{L1}, {L2} -> {self.atomSelectionSet[0] if has_assignments else None} {self.atomSelectionSet[1] if has_assignments else None} {dstFunc}")

                if self.createSfDict__ and sf is not None:
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
                                   ambig_code1=ambig_code1, ambig_code2=ambig_code2)
                    sf['loop'].add_data(row)

            elif self.num_of_dim == 3:
                self.peaks3D += 1

                ppm = [None] * self.num_of_dim
                ppm_error = [None] * self.num_of_dim
                ass = [None] * self.num_of_dim

                idx = 0
                if self.__proton1_ppm is not None:
                    ppm[idx] = self.__proton1_ppm
                    ppm_error[idx] = self.__proton1_ppm_error
                    if self.__proton1_atoms is not None and len(self.__proton1_atoms) == 1:
                        ass[idx] = self.__proton1_atoms
                    idx += 1
                if self.__proton2_ppm is not None:
                    ppm[idx] = self.__proton2_ppm
                    ppm_error[idx] = self.__proton2_ppm_error
                    if self.__proton2_atoms is not None and len(self.__proton2_atoms) == 1:
                        ass[idx] = self.__proton2_atoms
                    idx += 1
                if self.__hetero1_ppm is not None:
                    ppm[idx] = self.__hetero1_ppm
                    ppm_error[idx] = self.__hetero1_ppm_error
                    if self.__hetero1_atoms is not None and len(self.__hetero1_atoms) == 1:
                        ass[idx] = self.__hetero1_atoms
                    idx += 1
                if self.__hetero2_ppm is not None:
                    ppm[idx] = self.__hetero2_ppm
                    ppm_error[idx] = self.__hetero2_ppm_error
                    if self.__hetero2_atoms is not None and len(self.__hetero2_atoms) == 1:
                        ass[idx] = self.__hetero2_atoms

                if not all(a is not None and len(a) == 1 and 'seq_id' in a[0] and 'atom_id' in a[0] for a in ass):
                    ass = [None] * self.num_of_dim

                if None in (ppm[0], ppm[1], ppm[2])\
                   or (self.__intensity is None and self.__volume is None):
                    self.peaks3D -= 1
                    return

                index = self.__index

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

                has_assignments = False
                L1 = L2 = L3 = None

                if ass[0] is not None and ass[1] is not None and ass[2] is not None:
                    assignments = [{}] * self.num_of_dim

                    _a1, _a2, _a3 = ass[0][0], ass[1][0], ass[2][0]
                    L1 = f"{_a1['chain_id']} {_a1['seq_id']} {_a1['atom_id']}" if 'chain_id' in _a1 else f"{_a1['seq_id']} {_a1['atom_id']}"
                    L2 = f"{_a2['chain_id']} {_a2['seq_id']} {_a2['atom_id']}" if 'chain_id' in _a2 else f"{_a2['seq_id']} {_a2['atom_id']}"
                    L3 = f"{_a3['chain_id']} {_a3['seq_id']} {_a3['atom_id']}" if 'chain_id' in _a3 else f"{_a3['seq_id']} {_a3['atom_id']}"

                    assignment0 = self.extractPeakAssignment(1, L1, index)
                    if assignment0 is not None:
                        assignments[0] = assignment0[0]
                    assignment1 = self.extractPeakAssignment(1, L2, index)
                    if assignment1 is not None:
                        assignments[1] = assignment1[0]
                    assignment2 = self.extractPeakAssignment(1, L3, index)
                    if assignment2 is not None:
                        assignments[2] = assignment2[0]

                    if all(len(a) > 0 for a in assignments):

                        self.retrieveLocalSeqScheme()

                        hasChainId = all(a['chain_id'] is not None for a in assignments)
                        hasCompId = all(a['comp_id'] is not None for a in assignments)

                        a1 = assignments[0]
                        a2 = assignments[1]
                        a3 = assignments[2]

                        if hasChainId and hasCompId:
                            chainAssign1, asis1 = self.assignCoordPolymerSequenceWithChainId(a1['chain_id'], a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                            chainAssign2, asis2 = self.assignCoordPolymerSequenceWithChainId(a2['chain_id'], a2['seq_id'], a2['comp_id'], a2['atom_id'], index)
                            chainAssign3, asis3 = self.assignCoordPolymerSequenceWithChainId(a3['chain_id'], a3['seq_id'], a3['comp_id'], a3['atom_id'], index)

                        elif hasChainId:
                            chainAssign1 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a1['chain_id'], a1['seq_id'], a1['atom_id'], index)
                            chainAssign2 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a2['chain_id'], a2['seq_id'], a2['atom_id'], index)
                            chainAssign3 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a3['chain_id'], a3['seq_id'], a3['atom_id'], index)
                            asis1 = asis2 = asis3 = False

                        elif hasCompId:
                            chainAssign1, asis1 = self.assignCoordPolymerSequence(a1['chain_id'], a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                            chainAssign2, asis2 = self.assignCoordPolymerSequence(a2['chain_id'], a2['seq_id'], a2['comp_id'], a2['atom_id'], index)
                            chainAssign3, asis3 = self.assignCoordPolymerSequence(a3['chain_id'], a3['seq_id'], a3['comp_id'], a3['atom_id'], index)

                        else:
                            chainAssign1 = self.assignCoordPolymerSequenceWithoutCompId(a1['seq_id'], a1['atom_id'], index)
                            chainAssign2 = self.assignCoordPolymerSequenceWithoutCompId(a2['seq_id'], a2['atom_id'], index)
                            chainAssign3 = self.assignCoordPolymerSequenceWithoutCompId(a3['seq_id'], a3['atom_id'], index)
                            asis1 = asis2 = asis3 = False

                        if len(chainAssign1) > 0 and len(chainAssign2) > 0 and len(chainAssign3) > 0:
                            self.selectCoordAtoms(chainAssign1, a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                            self.selectCoordAtoms(chainAssign2, a2['seq_id'], a2['comp_id'], a2['atom_id'], index)
                            self.selectCoordAtoms(chainAssign3, a3['seq_id'], a3['comp_id'], a3['atom_id'], index)

                            if len(self.atomSelectionSet) == self.num_of_dim:
                                has_assignments = True

                if self.createSfDict__:
                    sf = self.getSf()

                if self.debug:
                    print(f"subtype={self.cur_subtype} id={self.peaks3D} (index={index}) "
                          f"{L1}, {L2}, {L3} -> {self.atomSelectionSet[0] if has_assignments else None} {self.atomSelectionSet[1] if has_assignments else None} "
                          f"{self.atomSelectionSet[2] if has_assignments else None} {dstFunc}")

                if self.createSfDict__ and sf is not None:
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
                                   ambig_code1=ambig_code1, ambig_code2=ambig_code2,
                                   ambig_code3=ambig_code3)
                    sf['loop'].add_data(row)

            elif self.num_of_dim == 4:
                self.peaks4D += 1

                ppm = [None] * self.num_of_dim
                ppm_error = [None] * self.num_of_dim
                ass = [None] * self.num_of_dim

                idx = 0
                if self.__proton1_ppm is not None:
                    ppm[idx] = self.__proton1_ppm
                    ppm_error[idx] = self.__proton1_ppm_error
                    if self.__proton1_atoms is not None and len(self.__proton1_atoms) == 1:
                        ass[idx] = self.__proton1_atoms
                    idx += 1
                if self.__proton2_ppm is not None:
                    ppm[idx] = self.__proton2_ppm
                    ppm_error[idx] = self.__proton2_ppm_error
                    if self.__proton2_atoms is not None and len(self.__proton2_atoms) == 1:
                        ass[idx] = self.__proton2_atoms
                    idx += 1
                if self.__hetero1_ppm is not None:
                    ppm[idx] = self.__hetero1_ppm
                    ppm_error[idx] = self.__hetero1_ppm_error
                    if self.__hetero1_atoms is not None and len(self.__hetero1_atoms) == 1:
                        ass[idx] = self.__hetero1_atoms
                    idx += 1
                if self.__hetero2_ppm is not None:
                    ppm[idx] = self.__hetero2_ppm
                    ppm_error[idx] = self.__hetero2_ppm_error
                    if self.__hetero2_atoms is not None and len(self.__hetero2_atoms) == 1:
                        ass[idx] = self.__hetero2_atoms

                if not all(a is not None and len(a) == 1 and 'seq_id' in a[0] and 'atom_id' in a[0] for a in ass):
                    ass = [None] * self.num_of_dim

                if None in (ppm[0], ppm[1], ppm[2], ppm[3])\
                   or (self.__intensity is None and self.__volume is None):
                    self.peaks4D -= 1
                    return

                index = self.__index

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

                has_assignments = False
                L1 = L2 = L3 = L4 = None

                if ass[0] is not None and ass[1] is not None and ass[2] is not None and ass[3] is not None:
                    assignments = [{}] * self.num_of_dim

                    _a1, _a2, _a3, _a4 = ass[0][0], ass[1][0], ass[2][0], ass[3][0]
                    L1 = f"{_a1['chain_id']} {_a1['seq_id']} {_a1['atom_id']}" if 'chain_id' in _a1 else f"{_a1['seq_id']} {_a1['atom_id']}"
                    L2 = f"{_a2['chain_id']} {_a2['seq_id']} {_a2['atom_id']}" if 'chain_id' in _a2 else f"{_a2['seq_id']} {_a2['atom_id']}"
                    L3 = f"{_a3['chain_id']} {_a3['seq_id']} {_a3['atom_id']}" if 'chain_id' in _a3 else f"{_a3['seq_id']} {_a3['atom_id']}"
                    L4 = f"{_a4['chain_id']} {_a4['seq_id']} {_a4['atom_id']}" if 'chain_id' in _a4 else f"{_a4['seq_id']} {_a4['atom_id']}"

                    assignment0 = self.extractPeakAssignment(1, L1, index)
                    if assignment0 is not None:
                        assignments[0] = assignment0[0]
                    assignment1 = self.extractPeakAssignment(1, L2, index)
                    if assignment1 is not None:
                        assignments[1] = assignment1[0]
                    assignment2 = self.extractPeakAssignment(1, L3, index)
                    if assignment2 is not None:
                        assignments[2] = assignment2[0]
                    assignment3 = self.extractPeakAssignment(1, L4, index)
                    if assignment3 is not None:
                        assignments[3] = assignment3[0]

                    if all(len(a) > 0 for a in assignments):

                        self.retrieveLocalSeqScheme()

                        hasChainId = all(a['chain_id'] is not None for a in assignments)
                        hasCompId = all(a['comp_id'] is not None for a in assignments)

                        a1 = assignments[0]
                        a2 = assignments[1]
                        a3 = assignments[2]
                        a4 = assignments[3]

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
                            asis1 = asis2 = asis3 = asis4 = False

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
                            asis1 = asis2 = asis3 = asis4 = False

                        if len(chainAssign1) > 0 and len(chainAssign2) > 0 and len(chainAssign3) > 0 and len(chainAssign4) > 0:
                            self.selectCoordAtoms(chainAssign1, a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                            self.selectCoordAtoms(chainAssign2, a2['seq_id'], a2['comp_id'], a2['atom_id'], index)
                            self.selectCoordAtoms(chainAssign3, a3['seq_id'], a3['comp_id'], a3['atom_id'], index)
                            self.selectCoordAtoms(chainAssign4, a4['seq_id'], a4['comp_id'], a4['atom_id'], index)

                            if len(self.atomSelectionSet) == self.num_of_dim:
                                has_assignments = True

                if self.createSfDict__:
                    sf = self.getSf()

                if self.debug:
                    print(f"subtype={self.cur_subtype} id={self.peaks4D} (index={index}) "
                          f"{L1}, {L2}, {L3}, {L4} -> {self.atomSelectionSet[0] if has_assignments else None} {self.atomSelectionSet[1] if has_assignments else None} "
                          f"{self.atomSelectionSet[2] if has_assignments else None} {self.atomSelectionSet[3] if has_assignments else None} {dstFunc}")

                if self.createSfDict__ and sf is not None:
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
                                   atom1, atom2, atom3, atom4,
                                   asis1=asis1, asis2=asis2, asis3=asis3, asis4=asis4,
                                   ambig_code1=ambig_code1, ambig_code2=ambig_code2,
                                   ambig_code3=ambig_code3, ambig_code4=ambig_code4)
                    sf['loop'].add_data(row)

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

            if self.__cur_path == '/spectrum/peak':

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
    def exitAttribute(self, ctx: XMLParser.AttributeContext):
        pass

    # Enter a parse tree produced by XMLParser#chardata.
    def enterChardata(self, ctx: XMLParser.ChardataContext):
        pass

    # Exit a parse tree produced by XMLParser#chardata.
    def exitChardata(self, ctx: XMLParser.ChardataContext):
        pass

    # Enter a parse tree produced by XMLParser#misc.
    def enterMisc(self, ctx: XMLParser.MiscContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XMLParser#misc.
    def exitMisc(self, ctx: XMLParser.MiscContext):  # pylint: disable=unused-argument
        pass
