##
# File: SparkyPKParserListener.py
# Date: 04-Dec-2024
#
# Updates:
""" ParserLister class for SPARKY PK files.
    @author: Masashi Yokochi
"""
import sys
import numpy as np

from antlr4 import ParseTreeListener

try:
    from wwpdb.utils.nmr.pk.SparkyPKParser import SparkyPKParser
    from wwpdb.utils.nmr.pk.BasePKParserListener import BasePKParserListener
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (REPRESENTATIVE_MODEL_ID,
                                                       REPRESENTATIVE_ALT_ID,
                                                       getPkRow)

except ImportError:
    from nmr.pk.SparkyPKParser import SparkyPKParser
    from nmr.pk.BasePKParserListener import BasePKParserListener
    from nmr.mr.ParserListenerUtil import (REPRESENTATIVE_MODEL_ID,
                                           REPRESENTATIVE_ALT_ID,
                                           getPkRow)


# This class defines a complete listener for a parse tree produced by SparkyPKParser.
class SparkyPKParserListener(ParseTreeListener, BasePKParserListener):

    __has_volume = False

    def __init__(self, verbose=True, log=sys.stdout,
                 representativeModelId=REPRESENTATIVE_MODEL_ID,
                 representativeAltId=REPRESENTATIVE_ALT_ID,
                 mrAtomNameMapping=None,
                 cR=None, caC=None, ccU=None, csStat=None, nefT=None,
                 reasons=None):
        super().__init__(verbose, log, representativeModelId, representativeAltId,
                         mrAtomNameMapping, cR, caC, ccU, csStat, nefT, reasons)

        self.file_type = 'nm-pea-spa'
        self.software_name = 'SPARKY'

    # Enter a parse tree produced by SparkyPKParser#sparky_pk.
    def enterSparky_pk(self, ctx: SparkyPKParser.Sparky_pkContext):  # pylint: disable=unused-argument
        self.enter()

    # Exit a parse tree produced by SparkyPKParser#sparky_pk.
    def exitSparky_pk(self, ctx: SparkyPKParser.Sparky_pkContext):  # pylint: disable=unused-argument

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

    # Enter a parse tree produced by SparkyPKParser#data_label.
    def enterData_label(self, ctx: SparkyPKParser.Data_labelContext):
        if ctx.W1_LA():
            self.num_of_dim = max(self.num_of_dim, 1)
        if ctx.W2_LA():
            self.num_of_dim = max(self.num_of_dim, 2)
        if ctx.W3_LA():
            self.num_of_dim = max(self.num_of_dim, 3)
        if ctx.W4_LA():
            self.num_of_dim = max(self.num_of_dim, 4)

        self.__has_volume = False

        if ctx.Volume_LA():
            self.__has_volume = True

        self.initSpectralDim()

    # Exit a parse tree produced by SparkyPKParser#data_label.
    def exitData_label(self, ctx: SparkyPKParser.Data_labelContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by SparkyPKParser#data_label_wo_assign.
    def enterData_label_wo_assign(self, ctx: SparkyPKParser.Data_label_wo_assignContext):
        if ctx.W1_LA():
            self.num_of_dim = max(self.num_of_dim, 1)
        if ctx.W2_LA():
            self.num_of_dim = max(self.num_of_dim, 2)
        if ctx.W3_LA():
            self.num_of_dim = max(self.num_of_dim, 3)
        if ctx.W4_LA():
            self.num_of_dim = max(self.num_of_dim, 4)

        self.__has_volume = False

        if ctx.Volume_LA():
            self.__has_volume = True

        self.initSpectralDim()

    # Exit a parse tree produced by SparkyPKParser#data_label_wo_assign.
    def exitData_label_wo_assign(self, ctx: SparkyPKParser.Data_label_wo_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by SparkyPKParser#peak_2d.
    def enterPeak_2d(self, ctx: SparkyPKParser.Peak_2dContext):  # pylint: disable=unused-argument
        self.peaks2D += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by SparkyPKParser#peak_2d.
    def exitPeak_2d(self, ctx: SparkyPKParser.Peak_2dContext):

        try:

            if len(self.numberSelection) == 0:
                self.peaks2D -= 1
                return

            index = self.peaks2D

            ass = str(ctx.Assignment_2d_ex())
            if '?' in ass:
                ass = None

            x_ppm = float(str(ctx.Float(0)))
            y_ppm = float(str(ctx.Float(1)))

            height = self.originalNumberSelection[0]
            if self.__has_volume:
                volume = self.originalNumberSelection[1]

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            if x_ppm is None or y_ppm is None:
                self.peaks2D -= 1
                return

            dstFunc = self.validatePeak2D(index, x_ppm, y_ppm, None, None, None, None,
                                          None, None, None, None, height, None, volume if self.__has_volume else None, None)

            if dstFunc is None:
                self.peaks2D -= 1
                return

            cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

            cur_spectral_dim[1]['freq_hint'].append(x_ppm)
            cur_spectral_dim[2]['freq_hint'].append(y_ppm)

            has_assignments = False

            if ass is not None:
                assignments = self.extractPeakAssignment(self.num_of_dim, ass, index)

                if assignments is not None:

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
                            has_assignments &= self.fillAtomTypeInCase(1, a1['atom_id'][0])
                            has_assignments &= self.fillAtomTypeInCase(2, a2['atom_id'][0])

            if self.createSfDict__:
                sf = self.getSf()

            if self.debug:
                print(f"subtype={self.cur_subtype} id={self.peaks2D} (index={index}) "
                      f"{ass} -> {self.atomSelectionSet[0] if has_assignments else None} {self.atomSelectionSet[1] if has_assignments else None} {dstFunc}")

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
                               ambig_code1=ambig_code1, ambig_code2=ambig_code2, details=ass)
                sf['loop'].add_data(row)

        finally:
            self.numberSelection.clear()
            self.originalNumberSelection.clear()

    # Enter a parse tree produced by SparkyPKParser#peak_3d.
    def enterPeak_3d(self, ctx: SparkyPKParser.Peak_3dContext):  # pylint: disable=unused-argument
        self.peaks3D += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by SparkyPKParser#peak_3d.
    def exitPeak_3d(self, ctx: SparkyPKParser.Peak_3dContext):

        try:

            if len(self.numberSelection) == 0:
                self.peaks3D -= 1
                return

            index = self.peaks3D

            ass = str(ctx.Assignment_3d_ex())
            if '?' in ass:
                ass = None

            x_ppm = float(str(ctx.Float(0)))
            y_ppm = float(str(ctx.Float(1)))
            z_ppm = float(str(ctx.Float(2)))

            height = self.originalNumberSelection[0]
            if self.__has_volume:
                volume = self.originalNumberSelection[1]

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            if x_ppm is None or y_ppm is None or z_ppm is None:
                self.peaks3D -= 1
                return

            dstFunc = self.validatePeak3D(index, x_ppm, y_ppm, z_ppm, None, None, None, None, None, None,
                                          None, None, None, None, None, None, height, None, volume if self.__has_volume else None, None)

            if dstFunc is None:
                self.peaks3D -= 1
                return

            cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

            cur_spectral_dim[1]['freq_hint'].append(x_ppm)
            cur_spectral_dim[2]['freq_hint'].append(y_ppm)
            cur_spectral_dim[3]['freq_hint'].append(z_ppm)

            has_assignments = False

            if ass is not None:
                assignments = self.extractPeakAssignment(self.num_of_dim, ass, index)

                if assignments is not None:

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
                            has_assignments &= self.fillAtomTypeInCase(1, a1['atom_id'][0])
                            has_assignments &= self.fillAtomTypeInCase(2, a2['atom_id'][0])
                            has_assignments &= self.fillAtomTypeInCase(3, a3['atom_id'][0])

            if self.createSfDict__:
                sf = self.getSf()

            if self.debug:
                print(f"subtype={self.cur_subtype} id={self.peaks3D} (index={index}) "
                      f"{ass} -> {self.atomSelectionSet[0] if has_assignments else None} {self.atomSelectionSet[1] if has_assignments else None} "
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
                               ambig_code3=ambig_code3, details=ass)
                sf['loop'].add_data(row)

        finally:
            self.numberSelection.clear()
            self.originalNumberSelection.clear()

    # Enter a parse tree produced by SparkyPKParser#peak_4d.
    def enterPeak_4d(self, ctx: SparkyPKParser.Peak_4dContext):  # pylint: disable=unused-argument
        self.peaks4D += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by SparkyPKParser#peak_4d.
    def exitPeak_4d(self, ctx: SparkyPKParser.Peak_4dContext):

        try:

            if len(self.numberSelection) == 0:
                self.peaks4D -= 1
                return

            index = self.peaks4D

            ass = str(ctx.Assignment_4d_ex())
            if '?' in ass:
                ass = None

            x_ppm = float(str(ctx.Float(0)))
            y_ppm = float(str(ctx.Float(1)))
            z_ppm = float(str(ctx.Float(2)))
            a_ppm = float(str(ctx.Float(3)))

            height = self.originalNumberSelection[0]
            if self.__has_volume:
                volume = self.originalNumberSelection[1]

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            if x_ppm is None or y_ppm is None or z_ppm is None or a_ppm is None:
                self.peaks4D -= 1
                return

            dstFunc = self.validatePeak4D(index, x_ppm, y_ppm, z_ppm, a_ppm, None, None, None, None, None, None, None, None,
                                          None, None, None, None, None, None, None, None, height, None, volume if self.__has_volume else None, None)

            if dstFunc is None:
                self.peaks4D -= 1
                return

            cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

            cur_spectral_dim[1]['freq_hint'].append(x_ppm)
            cur_spectral_dim[2]['freq_hint'].append(y_ppm)
            cur_spectral_dim[3]['freq_hint'].append(z_ppm)
            cur_spectral_dim[4]['freq_hint'].append(a_ppm)

            has_assignments = False

            if ass is not None:
                assignments = self.extractPeakAssignment(self.num_of_dim, ass, index)

                if assignments is not None:

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
                            has_assignments &= self.fillAtomTypeInCase(1, a1['atom_id'][0])
                            has_assignments &= self.fillAtomTypeInCase(2, a2['atom_id'][0])
                            has_assignments &= self.fillAtomTypeInCase(3, a3['atom_id'][0])
                            has_assignments &= self.fillAtomTypeInCase(4, a4['atom_id'][0])

            if self.createSfDict__:
                sf = self.getSf()

            if self.debug:
                print(f"subtype={self.cur_subtype} id={self.peaks4D} (index={index}) "
                      f"{ass} -> {self.atomSelectionSet[0] if has_assignments else None} {self.atomSelectionSet[1] if has_assignments else None} "
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
                               atom1, atom2, atom3, atom4, asis1=asis1, asis2=asis2, asis3=asis3, asis4=asis4,
                               ambig_code1=ambig_code1, ambig_code2=ambig_code2,
                               ambig_code3=ambig_code3, ambig_code4=ambig_code4, details=ass)
                sf['loop'].add_data(row)

        finally:
            self.numberSelection.clear()
            self.originalNumberSelection.clear()

    # Enter a parse tree produced by SparkyPKParser#peak_wo_assign.
    def enterPeak_wo_assign(self, ctx: SparkyPKParser.Peak_wo_assignContext):  # pylint: disable=unused-argument
        if self.num_of_dim == 2:
            self.peaks2D += 1
        elif self.num_of_dim == 3:
            self.peaks3D += 1
        elif self.num_of_dim == 4:
            self.peaks4D += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by SparkyPKParser#peak_wo_assign.
    def exitPeak_wo_assign(self, ctx: SparkyPKParser.Peak_wo_assignContext):  # pylint: disable=unused-argument

        try:

            if len(self.numberSelection) == 0:
                if self.num_of_dim == 2:
                    self.peaks2D -= 1
                elif self.num_of_dim == 3:
                    self.peaks3D -= 1
                elif self.num_of_dim == 4:
                    self.peaks4D -= 1
                return

            if self.num_of_dim == 2:

                try:

                    index = self.peaks2D
                    x_ppm = self.numberSelection[0]
                    y_ppm = self.numberSelection[1]
                    height = self.originalNumberSelection[2]
                    if self.__has_volume:
                        volume = self.originalNumberSelection[3]

                    if not self.hasPolySeq and not self.hasNonPolySeq:
                        return

                    if x_ppm is None or y_ppm is None:
                        self.peaks2D -= 1
                        return

                    dstFunc = self.validatePeak2D(index, x_ppm, y_ppm, None, None, None, None,
                                                  None, None, None, None, height, None, volume if self.__has_volume else None, None)

                    if dstFunc is None:
                        self.peaks2D -= 1
                        return

                    cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

                    cur_spectral_dim[1]['freq_hint'].append(x_ppm)
                    cur_spectral_dim[2]['freq_hint'].append(y_ppm)

                    if self.createSfDict__:
                        sf = self.getSf()

                    if self.debug:
                        print(f"subtype={self.cur_subtype} id={self.peaks2D} (index={index}) {dstFunc}")

                    if self.createSfDict__ and sf is not None:
                        sf['index_id'] += 1

                        row = getPkRow(self.cur_subtype, sf['id'], sf['index_id'],
                                       sf['list_id'], self.entryId, dstFunc,
                                       self.authToStarSeq, self.authToOrigSeq, self.offsetHolder)
                        sf['loop'].add_data(row)

                except IndexError:
                    self.peaks2D -= 1
                    return

            elif self.num_of_dim == 3:

                try:

                    index = self.peaks3D
                    x_ppm = self.numberSelection[0]
                    y_ppm = self.numberSelection[1]
                    z_ppm = self.numberSelection[2]
                    height = self.originalNumberSelection[3]
                    if self.__has_volume:
                        volume = self.originalNumberSelection[4]

                    if not self.hasPolySeq and not self.hasNonPolySeq:
                        return

                    if x_ppm is None or y_ppm is None or z_ppm is None:
                        self.peaks3D -= 1
                        return

                    dstFunc = self.validatePeak3D(index, x_ppm, y_ppm, z_ppm, None, None, None, None, None, None,
                                                  None, None, None, None, None, None, height, None, volume if self.__has_volume else None, None)

                    if dstFunc is None:
                        self.peaks3D -= 1
                        return

                    cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

                    cur_spectral_dim[1]['freq_hint'].append(x_ppm)
                    cur_spectral_dim[2]['freq_hint'].append(y_ppm)
                    cur_spectral_dim[3]['freq_hint'].append(z_ppm)

                    if self.createSfDict__:
                        sf = self.getSf()

                    if self.debug:
                        print(f"subtype={self.cur_subtype} id={self.peaks3D} (index={index}) {dstFunc}")

                    if self.createSfDict__ and sf is not None:
                        sf['index_id'] += 1

                        row = getPkRow(self.cur_subtype, sf['id'], sf['index_id'],
                                       sf['list_id'], self.entryId, dstFunc,
                                       self.authToStarSeq, self.authToOrigSeq, self.offsetHolder)
                        sf['loop'].add_data(row)

                except IndexError:
                    self.peaks3D -= 1
                    return

            elif self.num_of_dim == 4:

                try:

                    index = self.peaks4D
                    x_ppm = self.numberSelection[0]
                    y_ppm = self.numberSelection[1]
                    z_ppm = self.numberSelection[2]
                    a_ppm = self.numberSelection[3]
                    height = self.originalNumberSelection[4]
                    if self.__has_volume:
                        volume = self.originalNumberSelection[5]

                    if not self.hasPolySeq and not self.hasNonPolySeq:
                        return

                    if x_ppm is None or y_ppm is None or z_ppm is None or a_ppm is None:
                        self.peaks4D -= 1
                        return

                    dstFunc = self.validatePeak4D(index, x_ppm, y_ppm, z_ppm, a_ppm, None, None, None, None, None, None, None, None,
                                                  None, None, None, None, None, None, None, None, height, None, volume if self.__has_volume else None, None)

                    if dstFunc is None:
                        self.peaks4D -= 1
                        return

                    cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

                    cur_spectral_dim[1]['freq_hint'].append(x_ppm)
                    cur_spectral_dim[2]['freq_hint'].append(y_ppm)
                    cur_spectral_dim[3]['freq_hint'].append(z_ppm)
                    cur_spectral_dim[4]['freq_hint'].append(a_ppm)

                    if self.createSfDict__:
                        sf = self.getSf()

                    if self.debug:
                        print(f"subtype={self.cur_subtype} id={self.peaks4D} (index={index}) {dstFunc}")

                    if self.createSfDict__ and sf is not None:
                        sf['index_id'] += 1

                        row = getPkRow(self.cur_subtype, sf['id'], sf['index_id'],
                                       sf['list_id'], self.entryId, dstFunc,
                                       self.authToStarSeq, self.authToOrigSeq, self.offsetHolder)
                        sf['loop'].add_data(row)

                except IndexError:
                    self.peaks4D -= 1
                    return

        finally:
            self.numberSelection.clear()
            self.originalNumberSelection.clear()

    # Enter a parse tree produced by SparkyPKParser#number.
    def enterNumber(self, ctx: SparkyPKParser.NumberContext):
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

    # Exit a parse tree produced by SparkyPKParser#number.
    def exitNumber(self, ctx: SparkyPKParser.NumberContext):  # pylint: disable=unused-argument
        pass


# del SparkyPKParser
