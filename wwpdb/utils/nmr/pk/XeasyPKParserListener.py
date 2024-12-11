##
# File: XeasyPKParserListener.py
# Date: 04-Dec-2024
#
# Updates:
""" ParserLister class for XEASY PK files.
    @author: Masashi Yokochi
"""
import sys
import re

from antlr4 import ParseTreeListener

try:
    from wwpdb.utils.nmr.pk.XeasyPKParser import XeasyPKParser
    from wwpdb.utils.nmr.pk.BasePKParserListener import BasePKParserListener
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS,
                                                       REPRESENTATIVE_MODEL_ID,
                                                       REPRESENTATIVE_ALT_ID,
                                                       getPkRow)
    from wwpdb.utils.nmr.AlignUtil import emptyValue

except ImportError:
    from nmr.pk.XeasyPKParser import XeasyPKParser
    from nmr.pk.BasePKParserListener import BasePKParserListener
    from nmr.mr.ParserListenerUtil import (ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS,
                                           REPRESENTATIVE_MODEL_ID,
                                           REPRESENTATIVE_ALT_ID,
                                           getPkRow)
    from nmr.AlignUtil import emptyValue


# This class defines a complete listener for a parse tree produced by XeasyPKParser.
class XeasyPKParserListener(ParseTreeListener, BasePKParserListener):

    __index = None
    __labels = None
    __atomNumberDict = None

    def __init__(self, verbose=True, log=sys.stdout,
                 representativeModelId=REPRESENTATIVE_MODEL_ID,
                 representativeAltId=REPRESENTATIVE_ALT_ID,
                 mrAtomNameMapping=None,
                 cR=None, caC=None, ccU=None, csStat=None, nefT=None,
                 atomNumberDict=None, reasons=None):
        super().__init__(verbose, log, representativeModelId, representativeAltId,
                         mrAtomNameMapping, cR, caC, ccU, csStat, nefT, reasons)

        self.file_type = 'nm-pea-xea'
        self.software_name = 'XEASY'

        self.__atomNumberDict = atomNumberDict

    # Enter a parse tree produced by XeasyPKParser#xeasy_pk.
    def enterXeasy_pk(self, ctx: XeasyPKParser.Xeasy_pkContext):  # pylint: disable=unused-argument
        self.enter()

    # Exit a parse tree produced by XeasyPKParser#xeasy_pk.
    def exitXeasy_pk(self, ctx: XeasyPKParser.Xeasy_pkContext):  # pylint: disable=unused-argument
        self.exit()

    # Enter a parse tree produced by XeasyPKParser#dimension.
    def enterDimension(self, ctx: XeasyPKParser.DimensionContext):
        if ctx.Integer_ND():
            self.num_of_dim = int(str(ctx.Integer_ND()))
            self.acq_dim_id = 1
        self.__index = None
        self.__labels = {}

    # Exit a parse tree produced by XeasyPKParser#dimension.
    def exitDimension(self, ctx: XeasyPKParser.DimensionContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XeasyPKParser#format.
    def enterFormat(self, ctx: XeasyPKParser.FormatContext):
        if ctx.Simple_name_FO():
            if self.num_of_dim == -1:
                val = str(ctx.Simple_name_FO())
                if '2D' in val:
                    self.num_of_dim = 2
                if '3D' in val:
                    self.num_of_dim = 3
                if '4D' in val:
                    self.num_of_dim = 4

    # Exit a parse tree produced by XeasyPKParser#format.
    def exitFormat(self, ctx: XeasyPKParser.FormatContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XeasyPKParser#iname.
    def enterIname(self, ctx: XeasyPKParser.InameContext):
        if ctx.Integer_IN():
            _dim_id = int(str(ctx.Integer_IN()))
            self.num_of_dim = max(self.num_of_dim, _dim_id)
        if ctx.Simple_name_IN():
            _axis_code = str(ctx.Simple_name_IN())
            if _axis_code not in emptyValue:
                self.__labels[_dim_id] = _axis_code

    # Exit a parse tree produced by XeasyPKParser#iname.
    def exitIname(self, ctx: XeasyPKParser.InameContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XeasyPKParser#cyana_format.
    def enterCyana_format(self, ctx: XeasyPKParser.Cyana_formatContext):
        if ctx.Simple_name_CY():
            _axis_codes = str(ctx.Simple_name_CY())
            if self.num_of_dim == -1:
                self.num_of_dim = max(self.num_of_dim, len(_axis_codes))

            for _dim_id, _axis_code in enumerate(_axis_codes, start=1):
                if _dim_id not in self.__labels:
                    if _axis_code not in emptyValue:
                        self.__labels[_dim_id] = _axis_code

    # Exit a parse tree produced by XeasyPKParser#cyana_format.
    def exitCyana_format(self, ctx: XeasyPKParser.Cyana_formatContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XeasyPKParser#spectrum.
    def enterSpectrum(self, ctx: XeasyPKParser.SpectrumContext):
        _dim_id = 0
        if ctx.Simple_name_SP(_dim_id):
            _dim_id += 1
            while ctx.Simple_name_SP(_dim_id):
                self.num_of_dim = max(self.num_of_dim, _dim_id)
                if _dim_id not in self.__labels:
                    _axis_code = str(ctx.Simple_name_SP(_dim_id))
                    if _axis_code not in emptyValue:
                        self.__labels[_dim_id] = _axis_code
                _dim_id += 1

    # Exit a parse tree produced by XeasyPKParser#spectrum.
    def exitSpectrum(self, ctx: XeasyPKParser.SpectrumContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XeasyPKParser#tolerance.
    def enterTolerance(self, ctx: XeasyPKParser.ToleranceContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XeasyPKParser#tolerance.
    def exitTolerance(self, ctx: XeasyPKParser.ToleranceContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XeasyPKParser#peak_list_2d.
    def enterPeak_list_2d(self, ctx: XeasyPKParser.Peak_list_2dContext):  # pylint: disable=unused-argument
        self.num_of_dim = 2
        self.initSpectralDim()
        self.fillSpectralDimWithLabels()

    # Exit a parse tree produced by XeasyPKParser#peak_list_2d.
    def exitPeak_list_2d(self, ctx: XeasyPKParser.Peak_list_2dContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XeasyPKParser#peak_2d.
    def enterPeak_2d(self, ctx: XeasyPKParser.Peak_2dContext):  # pylint: disable=unused-argument
        self.peaks2D += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by XeasyPKParser#peak_2d.
    def exitPeak_2d(self, ctx: XeasyPKParser.Peak_2dContext):

        try:

            if len(self.numberSelection) == 0 or len(self.assignmentSelection) == 0:
                self.peaks2D -= 1
                return

            index = self.__index = int(str(ctx.Integer(0)))
            x_ppm = float(str(ctx.Float(0)))
            y_ppm = float(str(ctx.Float(1)))
            # color_code = int(str(ctx.Integer(1)))
            # spectrum_type = str(ctx.Simple_name(0))
            vol = self.originalNumberSelection[0]
            vol_err = self.originalNumberSelection[1]
            # integral_method = str(ctx.Simple_name(1))
            type = int(str(ctx.Integer(2)))

            x_ass = self.assignmentSelection[0]
            y_ass = self.assignmentSelection[1]
            if len(self.assignmentSelection) > self.num_of_dim:  # ignore multiple assignments for a peak
                x_ass = y_ass = None

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            if x_ppm is None or y_ppm is None or type != 0:
                self.peaks2D -= 1
                return

            dstFunc = self.validatePeak2D(index, x_ppm, y_ppm, None, None, None, None,
                                          None, None, None, None, None, None, vol, vol_err)

            if dstFunc is None:
                self.peaks2D -= 1
                return

            cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

            cur_spectral_dim[1]['freq_hint'].append(x_ppm)
            cur_spectral_dim[2]['freq_hint'].append(y_ppm)

            has_assignments = False

            asis1 = asis2 = None

            if x_ass is not None and y_ass is not None:
                assignments = [{}] * self.num_of_dim

                assignment0 = self.extractPeakAssignment(1, x_ass, index)
                if assignment0 is not None:
                    assignments[0] = assignment0[0]
                assignment1 = self.extractPeakAssignment(1, y_ass, index)
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
                            has_assignments &= self.fillAtomTypeInCase(1, a1['atom_id'][0])
                            has_assignments &= self.fillAtomTypeInCase(2, a2['atom_id'][0])

            if self.createSfDict__:
                sf = self.getSf()

            if self.debug:
                print(f"subtype={self.cur_subtype} id={self.peaks2D} (index={index}) "
                      f"{x_ass}, {y_ass} -> {self.atomSelectionSet[0] if has_assignments else None} {self.atomSelectionSet[1] if has_assignments else None} {dstFunc}")

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
                               ambig_code1=ambig_code1, ambig_code2=ambig_code2)
                sf['loop'].add_data(row)

        finally:
            self.numberSelection.clear()
            self.originalNumberSelection.clear()
            self.assignmentSelection.clear()

    # Enter a parse tree produced by XeasyPKParser#peak_list_3d.
    def enterPeak_list_3d(self, ctx: XeasyPKParser.Peak_list_3dContext):  # pylint: disable=unused-argument
        self.num_of_dim = 3
        self.initSpectralDim()
        self.fillSpectralDimWithLabels()

    # Exit a parse tree produced by XeasyPKParser#peak_list_3d.
    def exitPeak_list_3d(self, ctx: XeasyPKParser.Peak_list_3dContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XeasyPKParser#peak_3d.
    def enterPeak_3d(self, ctx: XeasyPKParser.Peak_3dContext):  # pylint: disable=unused-argument
        self.peaks3D += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by XeasyPKParser#peak_3d.
    def exitPeak_3d(self, ctx: XeasyPKParser.Peak_3dContext):

        try:

            if len(self.numberSelection) == 0 or len(self.assignmentSelection) == 0:
                self.peaks3D -= 1
                return

            index = self.__index = int(str(ctx.Integer(0)))
            x_ppm = float(str(ctx.Float(0)))
            y_ppm = float(str(ctx.Float(1)))
            z_ppm = float(str(ctx.Float(2)))
            # color_code = int(str(ctx.Integer(1)))
            # spectrum_type = str(ctx.Simple_name(0))
            vol = self.originalNumberSelection[0]
            vol_err = self.originalNumberSelection[1]
            # integral_method = str(ctx.Simple_name(1))
            type = int(str(ctx.Integer(2)))

            x_ass = self.assignmentSelection[0]
            y_ass = self.assignmentSelection[1]
            z_ass = self.assignmentSelection[2]
            if len(self.assignmentSelection) > self.num_of_dim:  # ignore multiple assignments for a peak
                x_ass = y_ass = z_ass = None

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            if x_ppm is None or y_ppm is None or z_ppm is None or type != 0:
                self.peaks3D -= 1
                return

            dstFunc = self.validatePeak3D(index, x_ppm, y_ppm, z_ppm, None, None, None, None, None, None,
                                          None, None, None, None, None, None, None, None, vol, vol_err)

            if dstFunc is None:
                self.peaks3D -= 1
                return

            cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

            cur_spectral_dim[1]['freq_hint'].append(x_ppm)
            cur_spectral_dim[2]['freq_hint'].append(y_ppm)
            cur_spectral_dim[3]['freq_hint'].append(z_ppm)

            has_assignments = False

            asis1 = asis2 = asis3 = None

            if x_ass is not None and y_ass is not None and z_ass is not None:
                assignments = [{}] * self.num_of_dim

                assignment0 = self.extractPeakAssignment(1, x_ass, index)
                if assignment0 is not None:
                    assignments[0] = assignment0[0]
                assignment1 = self.extractPeakAssignment(1, y_ass, index)
                if assignment1 is not None:
                    assignments[1] = assignment1[0]
                assignment2 = self.extractPeakAssignment(1, z_ass, index)
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
                            has_assignments &= self.fillAtomTypeInCase(1, a1['atom_id'][0])
                            has_assignments &= self.fillAtomTypeInCase(2, a2['atom_id'][0])
                            has_assignments &= self.fillAtomTypeInCase(3, a3['atom_id'][0])

            if self.createSfDict__:
                sf = self.getSf()

            if self.debug:
                print(f"subtype={self.cur_subtype} id={self.peaks3D} (index={index}) "
                      f"{x_ass}, {y_ass}, {z_ass} -> {self.atomSelectionSet[0] if has_assignments else None} {self.atomSelectionSet[1] if has_assignments else None} "
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
                               ambig_code1=ambig_code1, ambig_code2=ambig_code2,
                               ambig_code3=ambig_code3)
                sf['loop'].add_data(row)

        finally:
            self.numberSelection.clear()
            self.originalNumberSelection.clear()
            self.assignmentSelection.clear()

    # Enter a parse tree produced by XeasyPKParser#peak_list_4d.
    def enterPeak_list_4d(self, ctx: XeasyPKParser.Peak_list_4dContext):  # pylint: disable=unused-argument
        self.num_of_dim = 4
        self.initSpectralDim()
        self.fillSpectralDimWithLabels()

    # Exit a parse tree produced by XeasyPKParser#peak_list_4d.
    def exitPeak_list_4d(self, ctx: XeasyPKParser.Peak_list_4dContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XeasyPKParser#peak_4d.
    def enterPeak_4d(self, ctx: XeasyPKParser.Peak_4dContext):  # pylint: disable=unused-argument
        self.peaks4D += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by XeasyPKParser#peak_4d.
    def exitPeak_4d(self, ctx: XeasyPKParser.Peak_4dContext):

        try:

            if len(self.numberSelection) == 0 or len(self.assignmentSelection) == 0:
                self.peaks4D -= 1
                return

            index = self.__index = int(str(ctx.Integer(0)))
            x_ppm = float(str(ctx.Float(0)))
            y_ppm = float(str(ctx.Float(1)))
            z_ppm = float(str(ctx.Float(2)))
            a_ppm = float(str(ctx.Float(3)))
            # color_code = int(str(ctx.Integer(1)))
            # spectrum_type = str(ctx.Simple_name(0))
            vol = self.originalNumberSelection[0]
            vol_err = self.originalNumberSelection[1]
            # integral_method = str(ctx.Simple_name(1))
            type = int(str(ctx.Integer(2)))

            x_ass = self.assignmentSelection[0]
            y_ass = self.assignmentSelection[1]
            z_ass = self.assignmentSelection[2]
            a_ass = self.assignmentSelection[3]
            if len(self.assignmentSelection) > self.num_of_dim:  # ignore multiple assignments for a peak
                x_ass = y_ass = z_ass = a_ass = None

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            if x_ppm is None or y_ppm is None or z_ppm is None or a_ppm is None or type != 0:
                self.peaks4D -= 1
                return

            dstFunc = self.validatePeak4D(index, x_ppm, y_ppm, z_ppm, a_ppm, None, None, None, None, None, None, None, None,
                                          None, None, None, None, None, None, None, None, None, None, vol, vol_err)

            if dstFunc is None:
                self.peaks4D -= 1
                return

            cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

            cur_spectral_dim[1]['freq_hint'].append(x_ppm)
            cur_spectral_dim[2]['freq_hint'].append(y_ppm)
            cur_spectral_dim[3]['freq_hint'].append(z_ppm)
            cur_spectral_dim[4]['freq_hint'].append(a_ppm)

            has_assignments = False

            asis1 = asis2 = asis3 = asis4 = None

            if x_ass is not None and y_ass is not None and z_ass is not None and a_ass is not None:
                assignments = [{}] * self.num_of_dim

                assignment0 = self.extractPeakAssignment(1, x_ass, index)
                if assignment0 is not None:
                    assignments[0] = assignment0[0]
                assignment1 = self.extractPeakAssignment(1, y_ass, index)
                if assignment1 is not None:
                    assignments[1] = assignment1[0]
                assignment2 = self.extractPeakAssignment(1, z_ass, index)
                if assignment2 is not None:
                    assignments[2] = assignment2[0]
                assignment3 = self.extractPeakAssignment(1, a_ass, index)
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
                            has_assignments &= self.fillAtomTypeInCase(1, a1['atom_id'][0])
                            has_assignments &= self.fillAtomTypeInCase(2, a2['atom_id'][0])
                            has_assignments &= self.fillAtomTypeInCase(3, a3['atom_id'][0])
                            has_assignments &= self.fillAtomTypeInCase(4, a4['atom_id'][0])

            if self.createSfDict__:
                sf = self.getSf()

            if self.debug:
                print(f"subtype={self.cur_subtype} id={self.peaks4D} (index={index}) "
                      f"{x_ass}, {y_ass}, {z_ass}, {a_ass} -> {self.atomSelectionSet[0] if has_assignments else None} {self.atomSelectionSet[1] if has_assignments else None} "
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
                               ambig_code1=ambig_code1, ambig_code2=ambig_code2,
                               ambig_code3=ambig_code3, ambig_code4=ambig_code4)
                sf['loop'].add_data(row)

        finally:
            self.numberSelection.clear()
            self.originalNumberSelection.clear()
            self.assignmentSelection.clear()

    # Enter a parse tree produced by XeasyPKParser#number.
    def enterNumber(self, ctx: XeasyPKParser.NumberContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XeasyPKParser#number.
    def exitNumber(self, ctx: XeasyPKParser.NumberContext):
        if ctx.Float():
            value = str(ctx.Float())
            self.numberSelection.append(float(value))
            self.originalNumberSelection.append(value)

        elif ctx.Real():
            value = str(ctx.Real())
            self.numberSelection.append(float(value))
            self.originalNumberSelection.append(value)

        elif ctx.Integer():
            value = str(ctx.Integer())
            self.numberSelection.append(int(value))
            self.originalNumberSelection.append(value)

        else:
            self.numberSelection.append(None)
            self.originalNumberSelection.append(None)

    # Enter a parse tree produced by XeasyPKParser#assign.
    def enterAssign(self, ctx: XeasyPKParser.AssignContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XeasyPKParser#assign.
    def exitAssign(self, ctx: XeasyPKParser.AssignContext):
        if ctx.Simple_name() and ctx.Integer():
            self.assignmentSelection.append(f'{str(ctx.Integer())} {str(ctx.Simple_name())}')
        elif ctx.Simple_name():
            assignment = self.extractPeakAssignment(1, str(ctx.Simple_name()),
                                                    self.__index - 1 if isinstance(self.__index, int) else 1)
            if assignment is None:
                self.assignmentSelection.append(None)
            else:
                factor = assignment[0]
                self.assignmentSelection.append(f"{factor['chain_id'] if 'chain_id' in factor else ''} "
                                                f"{factor['seq_id'] if 'seq_id' in factor else ''} "
                                                f"{factor['comp_id'] if 'comp_id' in factor else ''} "
                                                f"{factor['atom_id']}")
        else:
            ai = int(str(ctx.Integer()))
            if ai == 0 or self.__atomNumberDict is None or ai not in self.__atomNumberDict:
                self.assignmentSelection.append(None)
            else:
                factor = self.__atomNumberDict[ai]
                self.assignmentSelection.append(f"{factor['chain_id']} {factor['seq_id']} "
                                                f"{factor['comp_id']} {factor['auth_atom_id']}")

    def fillSpectralDimWithLabels(self):
        if self.__labels is None or len(self.__labels) == 0:
            return
        for _dim_id, _axis_code in self.__labels.items():
            cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id][_dim_id]

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


# del XeasyPKParser
