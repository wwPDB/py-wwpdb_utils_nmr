##
# File: BarePKParserListener.py
# Date: 05-Mar-2025
#
# Updates:
""" ParserLister class for Bare PK files.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "1.0.0"

import sys

from antlr4 import ParseTreeListener
from typing import IO, List, Optional

try:
    from wwpdb.utils.nmr.io.CifReader import CifReader
    from wwpdb.utils.nmr.pk.BarePKParser import BarePKParser
    from wwpdb.utils.nmr.pk.BasePKParserListener import BasePKParserListener
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (REPRESENTATIVE_MODEL_ID,
                                                       REPRESENTATIVE_ALT_ID)
    from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
    from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from wwpdb.utils.nmr.nef.NEFTranslator import NEFTranslator
except ImportError:
    from nmr.io.CifReader import CifReader
    from nmr.pk.BarePKParser import BarePKParser
    from nmr.pk.BasePKParserListener import BasePKParserListener
    from nmr.mr.ParserListenerUtil import (REPRESENTATIVE_MODEL_ID,
                                           REPRESENTATIVE_ALT_ID)
    from nmr.ChemCompUtil import ChemCompUtil
    from nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from nmr.nef.NEFTranslator import NEFTranslator


# This class defines a complete listener for a parse tree produced by BarePKParser.
class BarePKParserListener(ParseTreeListener, BasePKParserListener):

    def __init__(self, verbose: bool = True, log: IO = sys.stdout,
                 representativeModelId: int = REPRESENTATIVE_MODEL_ID,
                 representativeAltId: str = REPRESENTATIVE_ALT_ID,
                 mrAtomNameMapping: Optional[List[dict]] = None,
                 cR: Optional[CifReader] = None, caC: Optional[dict] = None, ccU: Optional[ChemCompUtil] = None,
                 csStat: Optional[BMRBChemShiftStat] = None, nefT: Optional[NEFTranslator] = None,
                 reasons: Optional[dict] = None):
        super().__init__(verbose, log, representativeModelId, representativeAltId,
                         mrAtomNameMapping, cR, caC, ccU, csStat, nefT, reasons)

        self.file_type = 'nm-pea-bar'

    def setInternalMode(self, internal: bool):
        self.internal = internal

    # Enter a parse tree produced by BarePKParser#ccpn_pk.
    def enterBare_pk(self, ctx: BarePKParser.Bare_pkContext):  # pylint: disable=unused-argument
        self.enter()

    # Exit a parse tree produced by BarePKParser#ccpn_pk.
    def exitBare_pk(self, ctx: BarePKParser.Bare_pkContext):  # pylint: disable=unused-argument
        self.exit()

    # Enter a parse tree produced by BarePKParser#peak_list_2d.
    def enterPeak_list_2d(self, ctx: BarePKParser.Peak_list_2dContext):  # pylint: disable=unused-argument
        self.num_of_dim = 2
        self.initSpectralDim()

    # Exit a parse tree produced by BarePKParser#peak_list_2d.
    def exitPeak_list_2d(self, ctx: BarePKParser.Peak_list_2dContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by BarePKParser#peak_2d.
    def enterPeak_2d(self, ctx: BarePKParser.Peak_2dContext):  # pylint: disable=unused-argument
        self.peaks2D += 1

        self.atomSelectionSets.clear()
        self.asIsSets.clear()

    # Exit a parse tree produced by BarePKParser#peak_2d.
    def exitPeak_2d(self, ctx: BarePKParser.Peak_2dContext):

        try:

            index = self.peaks2D

            try:

                P1 = float(str(ctx.Float(0)))
                P2 = float(str(ctx.Float(1)))

            except (TypeError, ValueError):
                self.peaks2D -= 1
                return

            L1 = f'{str(ctx.Simple_name(0))}:{str(ctx.Integer(0))}:{str(ctx.Simple_name(1))}:{str(ctx.Simple_name(2))}'
            L2 = f'{str(ctx.Simple_name(3))}:{str(ctx.Integer(1))}:{str(ctx.Simple_name(4))}:{str(ctx.Simple_name(5))}'

            height = self.originalNumberSelection[0] if len(self.numberSelection) > 0 else None
            volume = self.originalNumberSelection[1] if len(self.numberSelection) > 1 else None
            details = None

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            dstFunc = self.validatePeak2D(index, P1, P2, None, None, None, None,
                                          None, None, None, None, height, None, volume, None)

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
                                    details if details is not None or None in (L1, L2) or (has_assignments and not has_multiple_assignments)
                                    else f'{L1} {L2}')

        finally:
            self.numberSelection.clear()
            self.originalNumberSelection.clear()

    # Enter a parse tree produced by BarePKParser#peak_list_3d.
    def enterPeak_list_3d(self, ctx: BarePKParser.Peak_list_3dContext):  # pylint: disable=unused-argument
        self.num_of_dim = 3
        self.initSpectralDim()

    # Exit a parse tree produced by BarePKParser#peak_list_3d.
    def exitPeak_list_3d(self, ctx: BarePKParser.Peak_list_3dContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by BarePKParser#peak_3d.
    def enterPeak_3d(self, ctx: BarePKParser.Peak_3dContext):  # pylint: disable=unused-argument
        self.peaks3D += 1

        self.atomSelectionSets.clear()
        self.asIsSets.clear()

    # Exit a parse tree produced by BarePKParser#peak_3d.
    def exitPeak_3d(self, ctx: BarePKParser.Peak_3dContext):

        try:

            index = self.peaks3D

            try:

                P1 = float(str(ctx.Float(0)))
                P2 = float(str(ctx.Float(1)))
                P3 = float(str(ctx.Float(2)))

            except (TypeError, ValueError):
                self.peaks3D -= 1
                return

            L1 = f'{str(ctx.Simple_name(0))}:{str(ctx.Integer(0))}:{str(ctx.Simple_name(1))}:{str(ctx.Simple_name(2))}'
            L2 = f'{str(ctx.Simple_name(3))}:{str(ctx.Integer(1))}:{str(ctx.Simple_name(4))}:{str(ctx.Simple_name(5))}'
            L3 = f'{str(ctx.Simple_name(6))}:{str(ctx.Integer(2))}:{str(ctx.Simple_name(7))}:{str(ctx.Simple_name(8))}'

            height = self.originalNumberSelection[0] if len(self.numberSelection) > 0 else None
            volume = self.originalNumberSelection[1] if len(self.numberSelection) > 1 else None
            details = None

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            dstFunc = self.validatePeak3D(index, P1, P2, P3, None, None, None, None, None, None,
                                          None, None, None, None, None, None, height, None, volume, None)

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
                                    details if details is not None or None in (L1, L2, L3) or (has_assignments and not has_multiple_assignments)
                                    else f'{L1} {L2} {L3}')

        finally:
            self.numberSelection.clear()
            self.originalNumberSelection.clear()

    # Enter a parse tree produced by BarePKParser#peak_list_4d.
    def enterPeak_list_4d(self, ctx: BarePKParser.Peak_list_4dContext):  # pylint: disable=unused-argument
        self.num_of_dim = 4
        self.initSpectralDim()

    # Exit a parse tree produced by BarePKParser#peak_list_4d.
    def exitPeak_list_4d(self, ctx: BarePKParser.Peak_list_4dContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by BarePKParser#peak_4d.
    def enterPeak_4d(self, ctx: BarePKParser.Peak_4dContext):  # pylint: disable=unused-argument
        self.peaks4D += 1

        self.atomSelectionSets.clear()
        self.asIsSets.clear()

    # Exit a parse tree produced by BarePKParser#peak_4d.
    def exitPeak_4d(self, ctx: BarePKParser.Peak_4dContext):

        try:

            index = self.peaks4D

            try:

                P1 = float(str(ctx.Float(0)))
                P2 = float(str(ctx.Float(1)))
                P3 = float(str(ctx.Float(2)))
                P4 = float(str(ctx.Float(3)))

            except (TypeError, ValueError):
                self.peaks4D -= 1
                return

            L1 = f'{str(ctx.Simple_name(0))}:{str(ctx.Integer(0))}:{str(ctx.Simple_name(1))}:{str(ctx.Simple_name(2))}'
            L2 = f'{str(ctx.Simple_name(3))}:{str(ctx.Integer(1))}:{str(ctx.Simple_name(4))}:{str(ctx.Simple_name(5))}'
            L3 = f'{str(ctx.Simple_name(6))}:{str(ctx.Integer(2))}:{str(ctx.Simple_name(7))}:{str(ctx.Simple_name(8))}'
            L4 = f'{str(ctx.Simple_name(9))}:{str(ctx.Integer(3))}:{str(ctx.Simple_name(10))}:{str(ctx.Simple_name(11))}'

            height = self.originalNumberSelection[0] if len(self.numberSelection) > 0 else None
            volume = self.originalNumberSelection[1] if len(self.numberSelection) > 1 else None
            details = None

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            dstFunc = self.validatePeak4D(index, P1, P2, P3, P4, None, None, None, None, None, None, None, None,
                                          None, None, None, None, None, None, None, None, height, None, volume, None)

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
                                    details if details is not None or None in (L1, L2, L3, L4) or (has_assignments and not has_multiple_assignments)
                                    else f'{L1} {L2} {L3} {L4}')

        finally:
            self.numberSelection.clear()
            self.originalNumberSelection.clear()

    # Enter a parse tree produced by BarePKParser#peak_list_wo_chain_2d.
    def enterPeak_list_wo_chain_2d(self, ctx: BarePKParser.Peak_list_wo_chain_2dContext):  # pylint: disable=unused-argument
        self.num_of_dim = 2
        self.initSpectralDim()

    # Exit a parse tree produced by BarePKParser#peak_list_wo_chain_2d.
    def exitPeak_list_wo_chain_2d(self, ctx: BarePKParser.Peak_list_wo_chain_2dContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by BarePKParser#peak_wo_chain_2d.
    def enterPeak_wo_chain_2d(self, ctx: BarePKParser.Peak_wo_chain_2dContext):  # pylint: disable=unused-argument
        self.peaks2D += 1

        self.atomSelectionSets.clear()
        self.asIsSets.clear()

    # Exit a parse tree produced by BarePKParser#peak_wo_chain_2d.
    def exitPeak_wo_chain_2d(self, ctx: BarePKParser.Peak_wo_chain_2dContext):

        try:

            index = self.peaks2D

            try:

                P1 = float(str(ctx.Float(0)))
                P2 = float(str(ctx.Float(1)))

            except (TypeError, ValueError):
                self.peaks2D -= 1
                return

            L1 = f'{str(ctx.Integer(0))}:{str(ctx.Simple_name(0))}:{str(ctx.Simple_name(1))}'
            L2 = f'{str(ctx.Integer(1))}:{str(ctx.Simple_name(2))}:{str(ctx.Simple_name(3))}'

            height = self.originalNumberSelection[0] if len(self.numberSelection) > 0 else None
            volume = self.originalNumberSelection[1] if len(self.numberSelection) > 1 else None
            details = None

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            dstFunc = self.validatePeak2D(index, P1, P2, None, None, None, None,
                                          None, None, None, None, height, None, volume, None)

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
                                    details if details is not None or None in (L1, L2) or (has_assignments and not has_multiple_assignments)
                                    else f'{L1} {L2}')

        finally:
            self.numberSelection.clear()
            self.originalNumberSelection.clear()

    # Enter a parse tree produced by BarePKParser#peak_list_wo_chain_3d.
    def enterPeak_list_wo_chain_3d(self, ctx: BarePKParser.Peak_list_wo_chain_3dContext):  # pylint: disable=unused-argument
        self.num_of_dim = 3
        self.initSpectralDim()

    # Exit a parse tree produced by BarePKParser#peak_list_wo_chain_3d.
    def exitPeak_list_wo_chain_3d(self, ctx: BarePKParser.Peak_list_wo_chain_3dContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by BarePKParser#peak_wo_chain_3d.
    def enterPeak_wo_chain_3d(self, ctx: BarePKParser.Peak_wo_chain_3dContext):  # pylint: disable=unused-argument
        self.peaks3D += 1

        self.atomSelectionSets.clear()
        self.asIsSets.clear()

    # Exit a parse tree produced by BarePKParser#peak_wo_chain_3d.
    def exitPeak_wo_chain_3d(self, ctx: BarePKParser.Peak_wo_chain_3dContext):

        try:

            index = self.peaks3D

            try:

                P1 = float(str(ctx.Float(0)))
                P2 = float(str(ctx.Float(1)))
                P3 = float(str(ctx.Float(2)))

            except (TypeError, ValueError):
                self.peaks3D -= 1
                return

            L1 = f'{str(ctx.Integer(0))}:{str(ctx.Simple_name(0))}:{str(ctx.Simple_name(1))}'
            L2 = f'{str(ctx.Integer(1))}:{str(ctx.Simple_name(2))}:{str(ctx.Simple_name(3))}'
            L3 = f'{str(ctx.Integer(2))}:{str(ctx.Simple_name(4))}:{str(ctx.Simple_name(5))}'

            height = self.originalNumberSelection[0] if len(self.numberSelection) > 0 else None
            volume = self.originalNumberSelection[1] if len(self.numberSelection) > 1 else None
            details = None

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            dstFunc = self.validatePeak3D(index, P1, P2, P3, None, None, None, None, None, None,
                                          None, None, None, None, None, None, height, None, volume, None)

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
                                    details if details is not None or None in (L1, L2, L3) or (has_assignments and not has_multiple_assignments)
                                    else f'{L1} {L2} {L3}')

        finally:
            self.numberSelection.clear()
            self.originalNumberSelection.clear()

    # Enter a parse tree produced by BarePKParser#peak_list_wo_chain_4d.
    def enterPeak_list_wo_chain_4d(self, ctx: BarePKParser.Peak_list_wo_chain_4dContext):  # pylint: disable=unused-argument
        self.num_of_dim = 4
        self.initSpectralDim()

    # Exit a parse tree produced by BarePKParser#peak_list_wo_chain_4d.
    def exitPeak_list_wo_chain_4d(self, ctx: BarePKParser.Peak_list_wo_chain_4dContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by BarePKParser#peak_wo_chain_4d.
    def enterPeak_wo_chain_4d(self, ctx: BarePKParser.Peak_wo_chain_4dContext):  # pylint: disable=unused-argument
        self.peaks4D += 1

        self.atomSelectionSets.clear()
        self.asIsSets.clear()

    # Exit a parse tree produced by BarePKParser#peak_wo_chain_4d.
    def exitPeak_wo_chain_4d(self, ctx: BarePKParser.Peak_wo_chain_4dContext):

        try:

            index = self.peaks4D

            try:

                P1 = float(str(ctx.Float(0)))
                P2 = float(str(ctx.Float(1)))
                P3 = float(str(ctx.Float(2)))
                P4 = float(str(ctx.Float(3)))

            except (TypeError, ValueError):
                self.peaks4D -= 1
                return

            L1 = f'{str(ctx.Integer(0))}:{str(ctx.Simple_name(0))}:{str(ctx.Simple_name(1))}'
            L2 = f'{str(ctx.Integer(1))}:{str(ctx.Simple_name(2))}:{str(ctx.Simple_name(3))}'
            L3 = f'{str(ctx.Integer(2))}:{str(ctx.Simple_name(4))}:{str(ctx.Simple_name(4))}'
            L4 = f'{str(ctx.Integer(3))}:{str(ctx.Simple_name(6))}:{str(ctx.Simple_name(7))}'

            height = self.originalNumberSelection[0] if len(self.numberSelection) > 0 else None
            volume = self.originalNumberSelection[1] if len(self.numberSelection) > 1 else None
            details = None

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            dstFunc = self.validatePeak4D(index, P1, P2, P3, P4, None, None, None, None, None, None, None, None,
                                          None, None, None, None, None, None, None, None, height, None, volume, None)

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
                                    details if details is not None or None in (L1, L2, L3, L4) or (has_assignments and not has_multiple_assignments)
                                    else f'{L1} {L2} {L3} {L4}')

        finally:
            self.numberSelection.clear()
            self.originalNumberSelection.clear()

    # Enter a parse tree produced by BarePKParser#number.
    def enterNumber(self, ctx: BarePKParser.NumberContext):

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

    # Exit a parse tree produced by BarePKParser#number.
    def exitNumber(self, ctx: BarePKParser.NumberContext):  # pylint: disable=unused-argument
        pass


# del BarePKParser
