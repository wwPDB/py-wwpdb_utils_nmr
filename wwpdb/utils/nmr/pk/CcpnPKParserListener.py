##
# File: CcpnPKParserListener.py
# Date: 26-Feb-2025
#
# Updates:
""" ParserLister class for CCPN PK files.
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
                                               REPRESENTATIVE_MODEL_ID,
                                               REPRESENTATIVE_ALT_ID)
    from wwpdb.utils.nmr.nef.NefTranslator import NefTranslator
    from wwpdb.utils.nmr.io.CifReader import CifReader
    from wwpdb.utils.nmr.pk.CcpnPKParser import CcpnPKParser
    from wwpdb.utils.nmr.pk.BasePKParserListener import BasePKParserListener
    from wwpdb.utils.nmr.mr.ParserListenerUtil import getPkRow
except ImportError:
    from nmr.NmrDpConstant import (EMPTY_VALUE,
                                   REPRESENTATIVE_MODEL_ID,
                                   REPRESENTATIVE_ALT_ID)
    from nmr.nef.NefTranslator import NefTranslator
    from nmr.io.CifReader import CifReader
    from nmr.pk.CcpnPKParser import CcpnPKParser
    from nmr.pk.BasePKParserListener import BasePKParserListener
    from nmr.mr.ParserListenerUtil import getPkRow


class CcpnPKParserListener(ParseTreeListener, BasePKParserListener):
    """ This class defines a complete listener for a parse tree produced by CcpnPKParser.
    """
    __slots__ = ()

    __has_number = False
    __has_id = False
    __has_height = False
    __has_volume = False
    __has_lw_hz = False
    __has_merit = False
    __has_details = False

    __noteSelection = []

    def __init__(self, verbose: bool = True, log: IO = sys.stdout,
                 representativeModelId: int = REPRESENTATIVE_MODEL_ID,
                 representativeAltId: str = REPRESENTATIVE_ALT_ID,
                 mrAtomNameMapping: Optional[List[dict]] = None,
                 cR: Optional[CifReader] = None, caC: Optional[dict] = None,
                 nefT: NefTranslator = None,
                 reasons: Optional[dict] = None) -> None:
        super().__init__(verbose, log, representativeModelId, representativeAltId,
                         mrAtomNameMapping, cR, caC, nefT, reasons)

        self.file_type = 'nm-pea-ccp'
        self.software_name = 'CCPN'

    def enterCcpn_pk(self, ctx: CcpnPKParser.Ccpn_pkContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by CcpnPKParser#ccpn_pk.
        """

    def exitCcpn_pk(self, ctx: CcpnPKParser.Ccpn_pkContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by CcpnPKParser#ccpn_pk.
        """

        self.exit()

    def enterPeak_list_2d(self, ctx: CcpnPKParser.Peak_list_2dContext):
        """ Enter a parse tree produced by CcpnPKParser#peak_list_2d.
        """

        self.num_of_dim = 2
        self.initSpectralDim()

        self.__has_number = False
        if ctx.Num():
            self.__has_number = True

        self.__has_id = False
        if ctx.Id() or ctx.Id_():
            self.__has_id = True

        self.__has_height = False
        if ctx.Height():
            self.__has_height = True

        self.__has_volume = False
        if ctx.Volume():
            self.__has_volume = True

        self.__has_lw_hz = False
        if ctx.Line_width_F1():
            self.__has_lw_hz = True

        self.__has_merit = False
        if ctx.Merit():
            self.__has_merit = True

        self.__has_details = False
        if ctx.Details():
            self.__has_details = True

    def exitPeak_list_2d(self, ctx: CcpnPKParser.Peak_list_2dContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by CcpnPKParser#peak_list_2d.
        """

    def enterPeak_2d(self, ctx: CcpnPKParser.Peak_2dContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by CcpnPKParser#peak_2d.
        """

        self.peaks2D += 1

        self.atomSelectionSets.clear()
        self.asIsSets.clear()

    def exitPeak_2d(self, ctx: CcpnPKParser.Peak_2dContext):
        """ Exit a parse tree produced by CcpnPKParser#peak_2d.
        """

        try:

            if 0 in (len(self.positionSelection), len(self.numberSelection)):
                self.peaks2D -= 1
                return

            try:

                if self.__has_id:
                    index = int(str(ctx.Integer(1 if self.__has_number else 0)))
                elif self.__has_number:
                    index = int(str(ctx.Integer(0)))
                else:
                    index = self.peaks2D

                float_offset = 0

                P1 = self.positionSelection[float_offset]
                P2 = self.positionSelection[float_offset + 1]
                float_offset += 2

                W1 = W2 = merit = None

                if self.__has_lw_hz:
                    W1 = self.positionSelection[float_offset]
                    W2 = self.positionSelection[float_offset + 1]
                    float_offset += 2

                if self.__has_merit:
                    merit = self.positionSelection[float_offset]

            except (IndexError, ValueError):
                self.peaks2D -= 1
                return

            L1 = str(ctx.Simple_name(0))
            L2 = str(ctx.Simple_name(1))

            if L1 in EMPTY_VALUE:
                L1 = None
            if L2 in EMPTY_VALUE:
                L2 = None

            height = self.originalNumberSelection[0] if self.__has_height else None
            volume = self.originalNumberSelection[1 if self.__has_height else 0] if self.__has_volume else None

            details = None
            if self.__has_details:
                details = self.__noteSelection[0]
                if details in EMPTY_VALUE:
                    details = None

            # fit_method = self.__noteSelection[1]
            # vol_method = self.__noteSelection[2]
            # if len(self.__noteSelection) > 3:
            #     vol_method += f' {self.__noteSelection[3]}'

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            if None in (P1, P2):
                self.peaks2D -= 1
                return

            dstFunc = self.validatePeak2D(index, P1, P2, None, None, None, None,
                                          None, None, W1, W2, height, None, volume, None, merit)

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
                        status, _L1 = self.testAssignment(1, ext, L1)
                        if status:
                            assignments[0] = ext
                        elif _L1 is not None:
                            if details is None:
                                details = f'Assign 1:{L1} -> {_L1}'
                            ext = self.extractPeakAssignment(1, _L1, index)
                            if ext is not None:
                                assignments[0] = ext
                if L2 is not None:
                    ext = self.extractPeakAssignment(1, L2, index)
                    if ext is not None:
                        status, _L2 = self.testAssignment(2, ext, L2)
                        if status:
                            assignments[1] = ext
                        elif _L2 is not None:
                            if details is None:
                                details = f'Assign 2:{L2} -> {_L2}'
                            ext = self.extractPeakAssignment(1, _L2, index)
                            if ext is not None:
                                assignments[1] = ext

                has_assignments, has_multiple_assignments, asis1, asis2 =\
                    self.checkAssignments2D(index, assignments, dstFunc)

            self.addAssignedPkRow2D(index, dstFunc, has_assignments, has_multiple_assignments,
                                    asis1, asis2,
                                    f'{L1} {L2} -> ',
                                    details if details is not None or None in (L1, L2)
                                    or (has_assignments and not has_multiple_assignments)
                                    else f'{L1} {L2}')

        finally:
            self.positionSelection.clear()
            self.numberSelection.clear()
            self.originalNumberSelection.clear()
            self.__noteSelection.clear()

    def enterPeak_list_3d(self, ctx: CcpnPKParser.Peak_list_3dContext):
        """ Enter a parse tree produced by CcpnPKParser#peak_list_3d.
        """

        self.num_of_dim = 3
        self.initSpectralDim()

        self.__has_number = False
        if ctx.Num():
            self.__has_number = True

        self.__has_id = False
        if ctx.Id() or ctx.Id_():
            self.__has_id = True

        self.__has_height = False
        if ctx.Height():
            self.__has_height = True

        self.__has_volume = False
        if ctx.Volume():
            self.__has_volume = True

        self.__has_lw_hz = False
        if ctx.Line_width_F1():
            self.__has_lw_hz = True

        self.__has_merit = False
        if ctx.Merit():
            self.__has_merit = True

        self.__has_details = False
        if ctx.Details():
            self.__has_details = True

    def exitPeak_list_3d(self, ctx: CcpnPKParser.Peak_list_3dContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by CcpnPKParser#peak_list_3d.
        """

    def enterPeak_3d(self, ctx: CcpnPKParser.Peak_3dContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by CcpnPKParser#peak_3d.
        """

        self.peaks3D += 1

        self.atomSelectionSets.clear()
        self.asIsSets.clear()

    def exitPeak_3d(self, ctx: CcpnPKParser.Peak_3dContext):
        """ Exit a parse tree produced by CcpnPKParser#peak_3d.
        """

        try:

            if 0 in (len(self.positionSelection), len(self.numberSelection)):
                self.peaks3D -= 1
                return

            try:

                if self.__has_id:
                    index = int(str(ctx.Integer(1 if self.__has_number else 0)))
                elif self.__has_number:
                    index = int(str(ctx.Integer(0)))
                else:
                    index = self.peaks3D

                float_offset = 0

                P1 = self.positionSelection[float_offset]
                P2 = self.positionSelection[float_offset + 1]
                P3 = self.positionSelection[float_offset + 2]
                float_offset += 3

                W1 = W2 = W3 = merit = None

                if self.__has_lw_hz:
                    W1 = self.positionSelection[float_offset]
                    W2 = self.positionSelection[float_offset + 1]
                    W3 = self.positionSelection[float_offset + 2]
                    float_offset += 3

                if self.__has_merit:
                    merit = self.positionSelection[float_offset]

            except (IndexError, ValueError):
                self.peaks3D -= 1
                return

            L1 = str(ctx.Simple_name(0))
            L2 = str(ctx.Simple_name(1))
            L3 = str(ctx.Simple_name(2))

            if L1 in EMPTY_VALUE:
                L1 = None
            if L2 in EMPTY_VALUE:
                L2 = None
            if L3 in EMPTY_VALUE:
                L3 = None

            height = self.originalNumberSelection[0] if self.__has_height else None
            volume = self.originalNumberSelection[1 if self.__has_height else 0] if self.__has_volume else None

            details = None
            if self.__has_details:
                details = self.__noteSelection[0]
                if details in EMPTY_VALUE:
                    details = None

            # fit_method = self.__noteSelection[1]
            # vol_method = self.__noteSelection[2]
            # if len(self.__noteSelection) > 3:
            #     vol_method += f' {self.__noteSelection[3]}'

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            if None in (P1, P2, P3):
                self.peaks3D -= 1
                return

            dstFunc = self.validatePeak3D(index, P1, P2, P3, None, None, None, None, None, None,
                                          None, None, None, W1, W2, W3, height, None, volume, None, merit)

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
                        status, _L1 = self.testAssignment(1, ext, L1)
                        if status:
                            assignments[0] = ext
                        elif _L1 is not None:
                            if details is None:
                                details = f'Assign 1:{L1} -> {_L1}'
                            ext = self.extractPeakAssignment(1, _L1, index)
                            if ext is not None:
                                assignments[0] = ext
                if L2 is not None:
                    ext = self.extractPeakAssignment(1, L2, index)
                    if ext is not None:
                        status, _L2 = self.testAssignment(2, ext, L2)
                        if status:
                            assignments[1] = ext
                        elif _L2 is not None:
                            if details is None:
                                details = f'Assign 2:{L2} -> {_L2}'
                            ext = self.extractPeakAssignment(1, _L2, index)
                            if ext is not None:
                                assignments[1] = ext
                if L3 is not None:
                    ext = self.extractPeakAssignment(1, L3, index)
                    if ext is not None:
                        status, _L3 = self.testAssignment(3, ext, L3)
                        if status:
                            assignments[2] = ext
                        elif _L3 is not None:
                            if details is None:
                                details = f'Assign 3:{L3} -> {_L3}'
                            ext = self.extractPeakAssignment(1, _L3, index)
                            if ext is not None:
                                assignments[2] = ext

                has_assignments, has_multiple_assignments, asis1, asis2, asis3 =\
                    self.checkAssignments3D(index, assignments, dstFunc)

            self.addAssignedPkRow3D(index, dstFunc, has_assignments, has_multiple_assignments,
                                    asis1, asis2, asis3,
                                    f'{L1} {L2} {L3} -> ',
                                    details if details is not None or None in (L1, L2, L3)
                                    or (has_assignments and not has_multiple_assignments)
                                    else f'{L1} {L2} {L3}')

        finally:
            self.positionSelection.clear()
            self.numberSelection.clear()
            self.originalNumberSelection.clear()
            self.__noteSelection.clear()

    def enterPeak_list_4d(self, ctx: CcpnPKParser.Peak_list_4dContext):
        """ Enter a parse tree produced by CcpnPKParser#peak_list_4d.
        """

        self.num_of_dim = 4
        self.initSpectralDim()

        self.__has_number = False
        if ctx.Num():
            self.__has_number = True

        self.__has_id = False
        if ctx.Id() or ctx.Id_():
            self.__has_id = True

        self.__has_height = False
        if ctx.Height():
            self.__has_height = True

        self.__has_volume = False
        if ctx.Volume():
            self.__has_volume = True

        self.__has_lw_hz = False
        if ctx.Line_width_F1():
            self.__has_lw_hz = True

        self.__has_merit = False
        if ctx.Merit():
            self.__has_merit = True

        self.__has_details = False
        if ctx.Details():
            self.__has_details = True

    def exitPeak_list_4d(self, ctx: CcpnPKParser.Peak_list_4dContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by CcpnPKParser#peak_list_4d.
        """

    def enterPeak_4d(self, ctx: CcpnPKParser.Peak_4dContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by CcpnPKParser#peak_4d.
        """

        self.peaks4D += 1

        self.atomSelectionSets.clear()
        self.asIsSets.clear()

    def exitPeak_4d(self, ctx: CcpnPKParser.Peak_4dContext):
        """ Exit a parse tree produced by CcpnPKParser#peak_4d.
        """

        try:

            if 0 in (len(self.positionSelection), len(self.numberSelection)):
                self.peaks4D -= 1
                return

            try:

                if self.__has_id:
                    index = int(str(ctx.Integer(1 if self.__has_number else 0)))
                elif self.__has_number:
                    index = int(str(ctx.Integer(0)))
                else:
                    index = self.peaks4D

                float_offset = 0

                P1 = self.positionSelection[float_offset]
                P2 = self.positionSelection[float_offset + 1]
                P3 = self.positionSelection[float_offset + 2]
                P4 = self.positionSelection[float_offset + 3]
                float_offset += 4

                W1 = W2 = W3 = W4 = merit = None

                if self.__has_lw_hz:
                    W1 = self.positionSelection[float_offset]
                    W2 = self.positionSelection[float_offset + 1]
                    W3 = self.positionSelection[float_offset + 2]
                    W4 = self.positionSelection[float_offset + 3]
                    float_offset += 4

                if self.__has_merit:
                    merit = self.positionSelection[float_offset]

            except (IndexError, ValueError):
                self.peaks4D -= 1
                return

            L1 = str(ctx.Simple_name(0))
            L2 = str(ctx.Simple_name(1))
            L3 = str(ctx.Simple_name(2))
            L4 = str(ctx.Simple_name(3))

            if L1 in EMPTY_VALUE:
                L1 = None
            if L2 in EMPTY_VALUE:
                L2 = None
            if L3 in EMPTY_VALUE:
                L3 = None
            if L4 in EMPTY_VALUE:
                L4 = None

            height = self.originalNumberSelection[0] if self.__has_height else None
            volume = self.originalNumberSelection[1 if self.__has_height else 0] if self.__has_volume else None

            details = None
            if self.__has_details:
                details = self.__noteSelection[0]
                if details in EMPTY_VALUE:
                    details = None

            # fit_method = self.__noteSelection[1]
            # vol_method = self.__noteSelection[2]
            # if len(self.__noteSelection) > 3:
            #     vol_method += f' {self.__noteSelection[3]}'

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            if None in (P1, P2, P3, P4):
                self.peaks4D -= 1
                return

            dstFunc = self.validatePeak4D(index, P1, P2, P3, P4, None, None, None, None, None, None, None, None,
                                          None, None, None, None, W1, W2, W3, W4, height, None, volume, None, merit)

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
                        status, _L1 = self.testAssignment(1, ext, L1)
                        if status:
                            assignments[0] = ext
                        elif _L1 is not None:
                            if details is None:
                                details = f'Assign 1:{L1} -> {_L1}'
                            ext = self.extractPeakAssignment(1, _L1, index)
                            if ext is not None:
                                assignments[0] = ext
                if L2 is not None:
                    ext = self.extractPeakAssignment(1, L2, index)
                    if ext is not None:
                        status, _L2 = self.testAssignment(2, ext, L2)
                        if status:
                            assignments[1] = ext
                        elif _L2 is not None:
                            if details is None:
                                details = f'Assign 2:{L2} -> {_L2}'
                            ext = self.extractPeakAssignment(1, _L2, index)
                            if ext is not None:
                                assignments[1] = ext
                if L3 is not None:
                    ext = self.extractPeakAssignment(1, L3, index)
                    if ext is not None:
                        status, _L3 = self.testAssignment(3, ext, L3)
                        if status:
                            assignments[2] = ext
                        elif _L3 is not None:
                            if details is None:
                                details = f'Assign 3:{L3} -> {_L3}'
                            ext = self.extractPeakAssignment(1, _L3, index)
                            if ext is not None:
                                assignments[2] = ext
                if L4 is not None:
                    ext = self.extractPeakAssignment(1, L4, index)
                    if ext is not None:
                        status, _L4 = self.testAssignment(4, ext, L4)
                        if status:
                            assignments[3] = ext
                        elif _L4 is not None:
                            if details is None:
                                details = f'Assign 4:{L4} -> {_L4}'
                            ext = self.extractPeakAssignment(1, _L4, index)
                            if ext is not None:
                                assignments[3] = ext

                has_assignments, has_multiple_assignments, asis1, asis2, asis3, asis4 =\
                    self.checkAssignments4D(index, assignments, dstFunc)

            self.addAssignedPkRow4D(index, dstFunc, has_assignments, has_multiple_assignments,
                                    asis1, asis2, asis3, asis4,
                                    f'{L1} {L2} {L3} {L4} -> ',
                                    details if details is not None or None in (L1, L2, L3, L4)
                                    or (has_assignments and not has_multiple_assignments)
                                    else f'{L1} {L2} {L3} {L4}')

        finally:
            self.positionSelection.clear()
            self.numberSelection.clear()
            self.originalNumberSelection.clear()
            self.__noteSelection.clear()

    def enterPeak_list_wo_assign_2d(self, ctx: CcpnPKParser.Peak_list_wo_assign_2dContext):
        """ Enter a parse tree produced by CcpnPKParser#peak_list_wo_assign_2d.
        """

        self.num_of_dim = 2
        self.initSpectralDim()

        self.__has_number = False
        if ctx.Num():
            self.__has_number = True

        self.__has_id = False
        if ctx.Id() or ctx.Id_():
            self.__has_id = True

        self.__has_height = False
        if ctx.Height():
            self.__has_height = True

        self.__has_volume = False
        if ctx.Volume():
            self.__has_volume = True

        self.__has_lw_hz = False
        if ctx.Line_width_F1():
            self.__has_lw_hz = True

        self.__has_merit = False
        if ctx.Merit():
            self.__has_merit = True

        self.__has_details = False
        if ctx.Details():
            self.__has_details = True

    def exitPeak_list_wo_assign_2d(self, ctx: CcpnPKParser.Peak_list_wo_assign_2dContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by CcpnPKParser#peak_list_wo_assign_2d.
        """

    def enterPeak_wo_assign_2d(self, ctx: CcpnPKParser.Peak_wo_assign_2dContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by CcpnPKParser#peak_wo_assign_2d.
        """

        self.peaks2D += 1

    def exitPeak_wo_assign_2d(self, ctx: CcpnPKParser.Peak_wo_assign_2dContext):
        """ Exit a parse tree produced by CcpnPKParser#peak_wo_assign_2d.
        """

        try:

            if 0 in (len(self.positionSelection), len(self.numberSelection)):
                self.peaks2D -= 1
                return

            try:

                if self.__has_id:
                    index = int(str(ctx.Integer(1 if self.__has_number else 0)))
                elif self.__has_number:
                    index = int(str(ctx.Integer(0)))
                else:
                    index = self.peaks2D

                float_offset = 0

                P1 = self.positionSelection[float_offset]
                P2 = self.positionSelection[float_offset + 1]
                float_offset += 2

                W1 = W2 = merit = None

                if self.__has_lw_hz:
                    W1 = self.positionSelection[float_offset]
                    W2 = self.positionSelection[float_offset + 1]
                    float_offset += 2

                if self.__has_merit:
                    merit = self.positionSelection[float_offset]

            except (IndexError, ValueError):
                self.peaks2D -= 1
                return

            height = self.originalNumberSelection[0] if self.__has_height else None
            volume = self.originalNumberSelection[1 if self.__has_height else 0] if self.__has_volume else None

            details = None
            if self.__has_details:
                details = self.__noteSelection[0]
                if details in EMPTY_VALUE:
                    details = None

            # fit_method = self.__noteSelection[1]
            # vol_method = self.__noteSelection[2]
            # if len(self.__noteSelection) > 3:
            #     vol_method += f' {self.__noteSelection[3]}'

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            if None in (P1, P2):
                self.peaks2D -= 1
                return

            dstFunc = self.validatePeak2D(index, P1, P2, None, None, None, None,
                                          None, None, W1, W2, height, None, volume, None, merit)

            if dstFunc is None:
                self.peaks2D -= 1
                return

            cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

            cur_spectral_dim[1]['freq_hint'].append(P1)
            cur_spectral_dim[2]['freq_hint'].append(P2)

            if self.createSfDict:
                sf = self.getSf()

                if sf is not None:
                    sf['id'] = index
                    sf['index_id'] += 1

                    row = getPkRow(self.cur_subtype, sf['id'], sf['index_id'],
                                   sf['list_id'], self.entryId, dstFunc,
                                   None, None, None,
                                   details=details)
                    sf['loop'].add_data(row)

        finally:
            self.positionSelection.clear()
            self.numberSelection.clear()
            self.originalNumberSelection.clear()
            self.__noteSelection.clear()

    def enterPeak_list_wo_assign_3d(self, ctx: CcpnPKParser.Peak_list_wo_assign_3dContext):
        """ Enter a parse tree produced by CcpnPKParser#peak_list_wo_assign_3d.
        """

        self.num_of_dim = 3
        self.initSpectralDim()

        self.__has_number = False
        if ctx.Num():
            self.__has_number = True

        self.__has_id = False
        if ctx.Id() or ctx.Id_():
            self.__has_id = True

        self.__has_height = False
        if ctx.Height():
            self.__has_height = True

        self.__has_volume = False
        if ctx.Volume():
            self.__has_volume = True

        self.__has_lw_hz = False
        if ctx.Line_width_F1():
            self.__has_lw_hz = True

        self.__has_merit = False
        if ctx.Merit():
            self.__has_merit = True

        self.__has_details = False
        if ctx.Details():
            self.__has_details = True

    def exitPeak_list_wo_assign_3d(self, ctx: CcpnPKParser.Peak_list_wo_assign_3dContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by CcpnPKParser#peak_list_wo_assign_3d.
        """

    def enterPeak_wo_assign_3d(self, ctx: CcpnPKParser.Peak_wo_assign_3dContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by CcpnPKParser#peak_wo_assign_3d.
        """

        self.peaks3D += 1

    def exitPeak_wo_assign_3d(self, ctx: CcpnPKParser.Peak_wo_assign_3dContext):
        """ Exit a parse tree produced by CcpnPKParser#peak_wo_assign_3d.
        """

        try:

            if 0 in (len(self.positionSelection), len(self.numberSelection)):
                self.peaks3D -= 1
                return

            try:

                if self.__has_id:
                    index = int(str(ctx.Integer(1 if self.__has_number else 0)))
                elif self.__has_number:
                    index = int(str(ctx.Integer(0)))
                else:
                    index = self.peaks3D

                float_offset = 0

                P1 = self.positionSelection[float_offset]
                P2 = self.positionSelection[float_offset + 1]
                P3 = self.positionSelection[float_offset + 2]
                float_offset += 3

                W1 = W2 = W3 = merit = None

                if self.__has_lw_hz:
                    W1 = self.positionSelection[float_offset]
                    W2 = self.positionSelection[float_offset + 1]
                    W3 = self.positionSelection[float_offset + 2]
                    float_offset += 3

                if self.__has_merit:
                    merit = self.positionSelection[float_offset]

            except (IndexError, ValueError):
                self.peaks3D -= 1
                return

            height = self.originalNumberSelection[0] if self.__has_height else None
            volume = self.originalNumberSelection[1 if self.__has_height else 0] if self.__has_volume else None

            details = None
            if self.__has_details:
                details = self.__noteSelection[0]
                if details in EMPTY_VALUE:
                    details = None

            # fit_method = self.__noteSelection[1]
            # vol_method = self.__noteSelection[2]
            # if len(self.__noteSelection) > 3:
            #     vol_method += f' {self.__noteSelection[3]}'

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            if None in (P1, P2, P3):
                self.peaks3D -= 1
                return

            dstFunc = self.validatePeak3D(index, P1, P2, P3, None, None, None, None, None, None,
                                          None, None, None, W1, W2, W3, height, None, volume, None, merit)

            if dstFunc is None:
                self.peaks3D -= 1
                return

            cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

            cur_spectral_dim[1]['freq_hint'].append(P1)
            cur_spectral_dim[2]['freq_hint'].append(P2)
            cur_spectral_dim[3]['freq_hint'].append(P3)

            if self.createSfDict:
                sf = self.getSf()

                if sf is not None:
                    sf['id'] = index
                    sf['index_id'] += 1

                    row = getPkRow(self.cur_subtype, sf['id'], sf['index_id'],
                                   sf['list_id'], self.entryId, dstFunc,
                                   None, None, None,
                                   details=details)
                    sf['loop'].add_data(row)

        finally:
            self.positionSelection.clear()
            self.numberSelection.clear()
            self.originalNumberSelection.clear()
            self.__noteSelection.clear()

    def enterPeak_list_wo_assign_4d(self, ctx: CcpnPKParser.Peak_list_wo_assign_4dContext):
        """ Enter a parse tree produced by CcpnPKParser#peak_list_wo_assign_4d.
        """

        self.num_of_dim = 4
        self.initSpectralDim()

        self.__has_number = False
        if ctx.Num():
            self.__has_number = True

        self.__has_id = False
        if ctx.Id() or ctx.Id_():
            self.__has_id = True

        self.__has_height = False
        if ctx.Height():
            self.__has_height = True

        self.__has_volume = False
        if ctx.Volume():
            self.__has_volume = True

        self.__has_lw_hz = False
        if ctx.Line_width_F1():
            self.__has_lw_hz = True

        self.__has_merit = False
        if ctx.Merit():
            self.__has_merit = True

        self.__has_details = False
        if ctx.Details():
            self.__has_details = True

    def exitPeak_list_wo_assign_4d(self, ctx: CcpnPKParser.Peak_list_wo_assign_4dContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by CcpnPKParser#peak_list_wo_assign_4d.
        """

    def enterPeak_wo_assign_4d(self, ctx: CcpnPKParser.Peak_wo_assign_4dContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by CcpnPKParser#peak_wo_assign_4d.
        """

        self.peaks4D += 1

    def exitPeak_wo_assign_4d(self, ctx: CcpnPKParser.Peak_wo_assign_4dContext):
        """ Exit a parse tree produced by CcpnPKParser#peak_wo_assign_4d.
        """

        try:

            if 0 in (len(self.positionSelection), len(self.numberSelection)):
                self.peaks4D -= 1
                return

            try:

                if self.__has_id:
                    index = int(str(ctx.Integer(1 if self.__has_number else 0)))
                elif self.__has_number:
                    index = int(str(ctx.Integer(0)))
                else:
                    index = self.peaks4D

                float_offset = 0

                P1 = self.positionSelection[float_offset]
                P2 = self.positionSelection[float_offset + 1]
                P3 = self.positionSelection[float_offset + 2]
                P4 = self.positionSelection[float_offset + 3]
                float_offset += 4

                W1 = W2 = W3 = W4 = merit = None

                if self.__has_lw_hz:
                    W1 = self.positionSelection[float_offset]
                    W2 = self.positionSelection[float_offset + 1]
                    W3 = self.positionSelection[float_offset + 2]
                    W4 = self.positionSelection[float_offset + 3]
                    float_offset += 4

                if self.__has_merit:
                    merit = self.positionSelection[float_offset]

            except (IndexError, ValueError):
                self.peaks4D -= 1
                return

            height = self.originalNumberSelection[0] if self.__has_height else None
            volume = self.originalNumberSelection[1 if self.__has_height else 0] if self.__has_volume else None

            details = None
            if self.__has_details:
                details = self.__noteSelection[0]
                if details in EMPTY_VALUE:
                    details = None

            # fit_method = self.__noteSelection[1]
            # vol_method = self.__noteSelection[2]
            # if len(self.__noteSelection) > 3:
            #     vol_method += f' {self.__noteSelection[3]}'

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            if None in (P1, P2, P3, P4):
                self.peaks4D -= 1
                return

            dstFunc = self.validatePeak4D(index, P1, P2, P3, P4, None, None, None, None, None, None, None, None,
                                          None, None, None, None, W1, W2, W3, W4, height, None, volume, None, merit)

            if dstFunc is None:
                self.peaks4D -= 1
                return

            cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

            cur_spectral_dim[1]['freq_hint'].append(P1)
            cur_spectral_dim[2]['freq_hint'].append(P2)
            cur_spectral_dim[3]['freq_hint'].append(P3)
            cur_spectral_dim[4]['freq_hint'].append(P4)

            if self.createSfDict:
                sf = self.getSf()

                if sf is not None:
                    sf['id'] = index
                    sf['index_id'] += 1

                    row = getPkRow(self.cur_subtype, sf['id'], sf['index_id'],
                                   sf['list_id'], self.entryId, dstFunc,
                                   None, None, None,
                                   details=details)
                    sf['loop'].add_data(row)

        finally:
            self.positionSelection.clear()
            self.numberSelection.clear()
            self.originalNumberSelection.clear()
            self.__noteSelection.clear()

    def enterPosition(self, ctx: CcpnPKParser.PositionContext):
        """ Enter a parse tree produced by CcpnPKParser#position.
        """

        try:

            if ctx.Float():
                value = str(ctx.Float())
                self.positionSelection.append(float(value))

            elif ctx.Real():
                value = str(ctx.Real())
                self.positionSelection.append(float(value))

            elif ctx.Integer():
                value = str(ctx.Integer())
                self.positionSelection.append(float(value))

            else:
                self.positionSelection.append(None)

        except ValueError:
            self.positionSelection.append(None)

    def exitPosition(self, ctx: CcpnPKParser.PositionContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by CcpnPKParser#position.
        """

    def enterNumber(self, ctx: CcpnPKParser.NumberContext):
        """ Enter a parse tree produced by CcpnPKParser#number.
        """

        try:

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

        except ValueError:
            self.numberSelection.append(None)
            self.originalNumberSelection.append(None)

    def exitNumber(self, ctx: CcpnPKParser.NumberContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by CcpnPKParser#number.
        """

    def enterNote(self, ctx: CcpnPKParser.NoteContext):
        """ Enter a parse tree produced by CcpnPKParser#note.
        """

        if ctx.Float():
            self.__noteSelection.append(str(ctx.Float()))

        elif ctx.Real():
            self.__noteSelection.append(str(ctx.Real()))

        elif ctx.Integer():
            self.__noteSelection.append(str(ctx.Integer()))

        elif ctx.Simple_name():
            self.__noteSelection.append(str(ctx.Simple_name()))

        else:
            self.__noteSelection.append(str(ctx.Any_name()))

    def exitNote(self, ctx: CcpnPKParser.NoteContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by CcpnPKParser#note.
        """
