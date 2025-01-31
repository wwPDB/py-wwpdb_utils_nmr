##
# File: NmrViewPKParserListener.py
# Date: 03-Dec-2024
#
# Updates:
""" ParserLister class for NMRVIEW PK files.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "1.0.0"

import sys
import re
import copy

from antlr4 import ParseTreeListener
from typing import IO, List, Optional

try:
    from wwpdb.utils.nmr.io.CifReader import CifReader
    from wwpdb.utils.nmr.pk.NmrViewPKParser import NmrViewPKParser
    from wwpdb.utils.nmr.pk.BasePKParserListener import BasePKParserListener
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS,
                                                       REPRESENTATIVE_MODEL_ID,
                                                       REPRESENTATIVE_ALT_ID,
                                                       SPECTRAL_DIM_TEMPLATE)
    from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
    from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from wwpdb.utils.nmr.nef.NEFTranslator import NEFTranslator
    from wwpdb.utils.nmr.AlignUtil import emptyValue
except ImportError:
    from nmr.io.CifReader import CifReader
    from nmr.pk.NmrViewPKParser import NmrViewPKParser
    from nmr.pk.BasePKParserListener import BasePKParserListener
    from nmr.mr.ParserListenerUtil import (ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS,
                                           REPRESENTATIVE_MODEL_ID,
                                           REPRESENTATIVE_ALT_ID,
                                           SPECTRAL_DIM_TEMPLATE)
    from nmr.ChemCompUtil import ChemCompUtil
    from nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from nmr.nef.NEFTranslator import NEFTranslator
    from nmr.AlignUtil import emptyValue


# This class defines a complete listener for a parse tree produced by NmrViewPKParser.
class NmrViewPKParserListener(ParseTreeListener, BasePKParserListener):

    __cur_label_type = None

    __labels = None
    __jcouplings = None
    __enclose_data = []

    def __init__(self, verbose: bool = True, log: IO = sys.stdout,
                 representativeModelId: int = REPRESENTATIVE_MODEL_ID,
                 representativeAltId: str = REPRESENTATIVE_ALT_ID,
                 mrAtomNameMapping: Optional[List[dict]] = None,
                 cR: Optional[CifReader] = None, caC: Optional[dict] = None, ccU: Optional[ChemCompUtil] = None,
                 csStat: Optional[BMRBChemShiftStat] = None, nefT: Optional[NEFTranslator] = None,
                 reasons: Optional[dict] = None):
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
                if _spectral_width not in emptyValue:
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

        try:

            if 0 in (len(self.numberSelection), len(self.assignmentSelection)):
                self.peaks2D -= 1
                return

            index = int(str(ctx.Integer(0)))

            L1 = self.__enclose_data[0]
            P1 = self.numberSelection[0]
            W1 = self.numberSelection[1]
            B1 = self.numberSelection[2]
            # E1 = str(ctx.Simple_name(0))
            # J1 = self.__jcouplings[0]
            # U1 = self.__enclose_data[1]

            L2 = self.__enclose_data[2]
            P2 = self.numberSelection[3]
            W2 = self.numberSelection[4]
            B2 = self.numberSelection[5]
            # E2 = str(ctx.Simple_name(1))
            # J2 = self.__jcouplings[1]
            # U2 = self.__enclose_data[3]

            vol = self.originalNumberSelection[6]
            _int = self.originalNumberSelection[7]
            # try:
            #     stat = int(str(ctx.Integer(1)))
            # except ValueError:
            #     stat = None
            if len(self.__enclose_data) > 4:
                comment = self.__enclose_data[4]
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

            if None in (P1, P2):  # or stat not in (0, None):
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

            if None not in (L1, L2):
                assignments = [None] * self.num_of_dim
                if L1 is not None:
                    ext = self.extractPeakAssignment(1, L1, index)
                    if ext is not None:
                        assignments[0] = ext
                if L2 is not None:
                    ext = self.extractPeakAssignment(1, L2, index)
                    if ext is not None:
                        assignments[1] = ext

                has_assignments, has_multiple_assignments, asis1, asis2 =\
                    self.checkAssignments2D(index, assignments)

            self.addAssignedPkRow2D(index, dstFunc, has_assignments, has_multiple_assignments,
                                    asis1, asis2,
                                    f'{L1} {L2} -> ', comment)

        finally:
            self.__enclose_data.clear()
            self.numberSelection.clear()
            self.originalNumberSelection.clear()

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

        try:

            if 0 in (len(self.numberSelection), len(self.assignmentSelection)):
                self.peaks3D -= 1
                return

            index = int(str(ctx.Integer(0)))

            L1 = self.__enclose_data[0]
            P1 = self.numberSelection[0]
            W1 = self.numberSelection[1]
            B1 = self.numberSelection[2]
            # E1 = str(ctx.Simple_name(0))
            # J1 = self.__jcouplings[0]
            # U1 = self.__enclose_data[1]

            L2 = self.__enclose_data[2]
            P2 = self.numberSelection[3]
            W2 = self.numberSelection[4]
            B2 = self.numberSelection[5]
            # E2 = str(ctx.Simple_name(1))
            # J2 = self.__jcouplings[1]
            # U2 = self.__enclose_data[3]

            L3 = self.__enclose_data[4]
            P3 = self.numberSelection[6]
            W3 = self.numberSelection[7]
            B3 = self.numberSelection[8]
            # E3 = str(ctx.Simple_name(2))
            # J3 = self.__jcouplings[2]
            # U3 = self.__enclose_data[5]

            vol = self.originalNumberSelection[9]
            _int = self.originalNumberSelection[10]
            # try:
            #     stat = int(str(ctx.Integer(1)))
            # except ValueError:
            #     stat = None
            if len(self.__enclose_data) > 6:
                comment = self.__enclose_data[6]
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

            if None in (P1, P2, P3):  # or stat not in (0, None):
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

            if None not in (L1, L2, L3):
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

                has_assignments, has_multiple_assignments, asis1, asis2, asis3 =\
                    self.checkAssignments3D(index, assignments)

            self.addAssignedPkRow3D(index, dstFunc, has_assignments, has_multiple_assignments,
                                    asis1, asis2, asis3,
                                    f'{L1} {L2} {L3} -> ', comment)

        finally:
            self.__enclose_data.clear()
            self.numberSelection.clear()
            self.originalNumberSelection.clear()

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

        try:

            if 0 in (len(self.numberSelection), len(self.assignmentSelection)):
                self.peaks4D -= 1
                return

            index = int(str(ctx.Integer(0)))

            L1 = self.__enclose_data[0]
            P1 = self.numberSelection[0]
            W1 = self.numberSelection[1]
            B1 = self.numberSelection[2]
            # E1 = str(ctx.Simple_name(0))
            # J1 = self.__jcouplings[0]
            # U1 = self.__enclose_data[1]

            L2 = self.__enclose_data[2]
            P2 = self.numberSelection[3]
            W2 = self.numberSelection[4]
            B2 = self.numberSelection[5]
            # E2 = str(ctx.Simple_name(1))
            # J2 = self.__jcouplings[1]
            # U2 = self.__enclose_data[3]

            L3 = self.__enclose_data[4]
            P3 = self.numberSelection[6]
            W3 = self.numberSelection[7]
            B3 = self.numberSelection[8]
            # E3 = str(ctx.Simple_name(2))
            # J3 = self.__jcouplings[2]
            # U3 = self.__enclose_data[5]

            L4 = self.__enclose_data[6]
            P4 = self.numberSelection[9]
            W4 = self.numberSelection[10]
            B4 = self.numberSelection[11]
            # E4 = str(ctx.Simple_name(3))
            # J4 = self.__jcouplings[3]
            # U4 = self.__enclose_data[7]

            vol = self.originalNumberSelection[12]
            _int = self.originalNumberSelection[13]
            # try:
            #     stat = int(str(ctx.Integer(1)))
            # except ValueError:
            #     stat = None
            if len(self.__enclose_data) > 8:
                comment = self.__enclose_data[8]
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

            if None in (P1, P2, P3, P4):  # or stat not in (0, None):
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

            if None not in (L1, L2, L3, L4):
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

                has_assignments, has_multiple_assignments, asis1, asis2, asis3, asis4 =\
                    self.checkAssignments4D(index, assignments)

            self.addAssignedPkRow4D(index, dstFunc, has_assignments, has_multiple_assignments,
                                    asis1, asis2, asis3, asis4,
                                    f'{L1} {L2} {L3} {L4} -> ', comment)

        finally:
            self.__enclose_data.clear()
            self.numberSelection.clear()
            self.originalNumberSelection.clear()

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

        try:

            if 0 in (len(self.numberSelection), len(self.assignmentSelection)):
                self.peaks2D -= 1
                return

            index = int(str(ctx.Integer(0)))

            L1 = self.__enclose_data[0]
            P1 = self.numberSelection[0]
            W1 = self.numberSelection[1]
            B1 = self.numberSelection[2]

            L2 = self.__enclose_data[1]
            P2 = self.numberSelection[3]
            W2 = self.numberSelection[4]
            B2 = self.numberSelection[5]

            vol = self.originalNumberSelection[6]
            _int = self.originalNumberSelection[7]
            # try:
            #     stat = int(str(ctx.Integer(1)))
            # except ValueError:
            #     stat = None
            if len(self.__enclose_data) > 2:
                comment = self.__enclose_data[2]
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

            if None in (P1, P2):  # or stat not in (0, None):
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

            if None not in (L1, L2):
                assignments = [None] * self.num_of_dim
                if L1 is not None:
                    ext = self.extractPeakAssignment(1, L1, index)
                    if ext is not None:
                        assignments[0] = ext
                if L2 is not None:
                    ext = self.extractPeakAssignment(1, L2, index)
                    if ext is not None:
                        assignments[1] = ext

                has_assignments, has_multiple_assignments, asis1, asis2 =\
                    self.checkAssignments2D(index, assignments)

            self.addAssignedPkRow2D(index, dstFunc, has_assignments, has_multiple_assignments,
                                    asis1, asis2,
                                    f'{L1} {L2} -> ', comment)

        finally:
            self.__enclose_data.clear()
            self.numberSelection.clear()
            self.originalNumberSelection.clear()

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

        try:

            if 0 in (len(self.numberSelection), len(self.assignmentSelection)):
                self.peaks3D -= 1
                return

            index = int(str(ctx.Integer(0)))

            L1 = self.__enclose_data[0]
            P1 = self.numberSelection[0]
            W1 = self.numberSelection[1]
            B1 = self.numberSelection[2]

            L2 = self.__enclose_data[1]
            P2 = self.numberSelection[3]
            W2 = self.numberSelection[4]
            B2 = self.numberSelection[5]

            L3 = self.__enclose_data[2]
            P3 = self.numberSelection[6]
            W3 = self.numberSelection[7]
            B3 = self.numberSelection[8]

            vol = self.originalNumberSelection[9]
            _int = self.originalNumberSelection[10]
            # try:
            #     stat = int(str(ctx.Integer(1)))
            # except ValueError:
            #     stat = None
            if len(self.__enclose_data) > 3:
                comment = self.__enclose_data[3]
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

            if None in (P1, P2, P3):  # or stat not in (0, None):
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

            if None not in (L1, L2, L3):
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

                has_assignments, has_multiple_assignments, asis1, asis2, asis3 =\
                    self.checkAssignments3D(index, assignments)

            self.addAssignedPkRow3D(index, dstFunc, has_assignments, has_multiple_assignments,
                                    asis1, asis2, asis3,
                                    f'{L1} {L2} {L3} -> ', comment)

        finally:
            self.__enclose_data.clear()
            self.numberSelection.clear()
            self.originalNumberSelection.clear()

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

        try:

            if 0 in (len(self.numberSelection), len(self.assignmentSelection)):
                self.peaks4D -= 1
                return

            index = int(str(ctx.Integer(0)))

            L1 = self.__enclose_data[0]
            P1 = self.numberSelection[0]
            W1 = self.numberSelection[1]
            B1 = self.numberSelection[2]

            L2 = self.__enclose_data[1]
            P2 = self.numberSelection[3]
            W2 = self.numberSelection[4]
            B2 = self.numberSelection[5]

            L3 = self.__enclose_data[2]
            P3 = self.numberSelection[6]
            W3 = self.numberSelection[7]
            B3 = self.numberSelection[8]

            L4 = self.__enclose_data[3]
            P4 = self.numberSelection[9]
            W4 = self.numberSelection[10]
            B4 = self.numberSelection[11]

            vol = self.originalNumberSelection[12]
            _int = self.originalNumberSelection[13]
            # try:
            #     stat = int(str(ctx.Integer(1)))
            # except ValueError:
            #     stat = None
            if len(self.__enclose_data) > 4:
                comment = self.__enclose_data[4]
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

            if None in (P1, P2, P3, P4):  # or stat not in (0, None):
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

            if None not in (L1, L2, L3, L4):
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

                has_assignments, has_multiple_assignments, asis1, asis2, asis3, asis4 =\
                    self.checkAssignments4D(index, assignments)

            self.addAssignedPkRow4D(index, dstFunc, has_assignments, has_multiple_assignments,
                                    asis1, asis2, asis3, asis4,
                                    f'{L1} {L2} {L3} {L4} -> ', comment)

        finally:
            self.__enclose_data.clear()
            self.numberSelection.clear()
            self.originalNumberSelection.clear()

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
    def enterJcoupling(self, ctx: NmrViewPKParser.JcouplingContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by NmrViewPKParser#jcoupling.
    def exitJcoupling(self, ctx: NmrViewPKParser.JcouplingContext):  # pylint: disable=unused-argument
        if ctx.Float():
            self.__jcouplings.append(float(str(ctx.Float())))
        elif ctx.Simple_name():
            self.__jcouplings.append(str(ctx.Simple_name()))
        else:
            value = self.__enclose_data[-1].strip()
            try:
                _value = float(value)
                self.__jcouplings.append(_value)
            except ValueError:
                self.__jcouplings.append(value)

    # Enter a parse tree produced by NmrViewPKParser#number.
    def enterNumber(self, ctx: NmrViewPKParser.NumberContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by NmrViewPKParser#number.
    def exitNumber(self, ctx: NmrViewPKParser.NumberContext):
        if ctx.Float():
            value = str(ctx.Float())
            self.numberSelection.append(float(value))
            self.originalNumberSelection.append(value)

        elif ctx.Integer():
            value = str(ctx.Integer())
            self.numberSelection.append(float(value))
            self.originalNumberSelection.append(value)

        else:
            self.numberSelection.append(None)
            self.originalNumberSelection.append(None)

    # Enter a parse tree produced by NmrViewPKParser#enclose_data.
    def enterEnclose_data(self, ctx: NmrViewPKParser.Enclose_dataContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by NmrViewPKParser#enclose_data.
    def exitEnclose_data(self, ctx: NmrViewPKParser.Enclose_dataContext):
        comment = []
        for col in range(20):
            if ctx.Any_name(col):
                comment.append(str(ctx.Any_name(col)))
            else:
                break
        last_comment = None if len(comment) == 0 else ' '.join(comment)
        self.__enclose_data.append(last_comment)


# del NmrViewPKParser
