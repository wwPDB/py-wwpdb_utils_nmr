##
# File: SparkyNPKParserListener.py
# Date: 30-Jan-2025
#
# Updates:
""" ParserLister class for SPARKY PK files.
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
    from wwpdb.utils.nmr.pk.SparkyNPKParser import SparkyNPKParser
    from wwpdb.utils.nmr.pk.BasePKParserListener import BasePKParserListener
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (REPRESENTATIVE_MODEL_ID,
                                                       REPRESENTATIVE_ALT_ID)
    from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
    from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from wwpdb.utils.nmr.nef.NEFTranslator import NEFTranslator
except ImportError:
    from nmr.io.CifReader import CifReader
    from nmr.pk.SparkyNPKParser import SparkyNPKParser
    from nmr.pk.BasePKParserListener import BasePKParserListener
    from nmr.mr.ParserListenerUtil import (REPRESENTATIVE_MODEL_ID,
                                           REPRESENTATIVE_ALT_ID)
    from nmr.ChemCompUtil import ChemCompUtil
    from nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from nmr.nef.NEFTranslator import NEFTranslator


# This class defines a complete listener for a parse tree produced by SparkyNPKParser.
class SparkyNPKParserListener(ParseTreeListener, BasePKParserListener):

    __has_hz = False
    __has_dev = False
    __has_height = False
    __has_volume = False
    __has_lw_hz = False
    __has_note = False

    __has_real_vol = False
    __real_vol = None

    __noteSelection = []

    def __init__(self, verbose: bool = True, log: IO = sys.stdout,
                 representativeModelId: int = REPRESENTATIVE_MODEL_ID,
                 representativeAltId: str = REPRESENTATIVE_ALT_ID,
                 mrAtomNameMapping: Optional[List[dict]] = None,
                 cR: Optional[CifReader] = None, caC: Optional[dict] = None, ccU: Optional[ChemCompUtil] = None,
                 csStat: Optional[BMRBChemShiftStat] = None, nefT: Optional[NEFTranslator] = None,
                 reasons: Optional[dict] = None):
        super().__init__(verbose, log, representativeModelId, representativeAltId,
                         mrAtomNameMapping, cR, caC, ccU, csStat, nefT, reasons)

        self.file_type = 'nm-pea-spa'
        self.software_name = 'SPARKY'

        if reasons is not None and 'has_real_vol' in reasons:
            self.__has_real_vol = True

    def setInternalMode(self, internal: bool):
        self.internal = internal

    # Enter a parse tree produced by SparkyNPKParser#sparky_npk.
    def enterSparky_npk(self, ctx: SparkyNPKParser.Sparky_npkContext):  # pylint: disable=unused-argument
        self.enter()

    # Exit a parse tree produced by SparkyNPKParser#sparky_npk.
    def exitSparky_npk(self, ctx: SparkyNPKParser.Sparky_npkContext):  # pylint: disable=unused-argument
        self.exit()

    # Enter a parse tree produced by SparkyNPKParser#data_label.
    def enterData_label(self, ctx: SparkyNPKParser.Data_labelContext):
        if ctx.W2_LA():
            self.num_of_dim = max(self.num_of_dim, 2)
        if ctx.W3_LA():
            self.num_of_dim = max(self.num_of_dim, 3)
        if ctx.W4_LA():
            self.num_of_dim = max(self.num_of_dim, 4)

        self.__has_hz = False
        if ctx.W2_Hz_LA():
            self.__has_hz = True

        self.__has_dev = False
        if ctx.Dev_w2_LA():
            self.__has_dev = True

        self.__has_height = False
        if ctx.Height_LA():
            self.__has_height = True

        self.__has_volume = False
        if ctx.Volume_LA():
            self.__has_volume = True

        self.__has_lw_hz = False
        if ctx.Lw2_Hz_LA():
            self.__has_lw_hz = True

        self.__has_note = False
        if ctx.Note_LA():
            self.__has_note = True

        self.initSpectralDim()

    # Exit a parse tree produced by SparkyNPKParser#data_label.
    def exitData_label(self, ctx: SparkyNPKParser.Data_labelContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by SparkyNPKParser#peak_2d.
    def enterPeak_2d(self, ctx: SparkyNPKParser.Peak_2dContext):  # pylint: disable=unused-argument
        if self.cur_subtype != 'peak2d':
            self.num_of_dim = 2
            self.initSpectralDim()

        self.peaks2D += 1

        self.atomSelectionSets.clear()
        self.asIsSets.clear()

    # Exit a parse tree produced by SparkyNPKParser#peak_2d.
    def exitPeak_2d(self, ctx: SparkyNPKParser.Peak_2dContext):

        try:

            index = self.peaks2D

            ass = _ass_ = str(ctx.Assignment_2d_ex())
            if '?' in ass:
                ass = None
            if _ass_ == 'A1H-H' and not self.isFirstResidueAla:
                ass = _ass_ = None

            try:

                x_ppm = float(str(ctx.Float(0)))
                y_ppm = float(str(ctx.Float(1)))

            except ValueError:
                self.peaks2D -= 1
                return

            offset = 0

            x_hz = y_hz = None
            if self.__has_hz:
                if len(self.numberSelection) > offset:
                    x_hz = self.numberSelection[offset]
                    offset += 1
                if len(self.numberSelection) > offset:
                    y_hz = self.numberSelection[offset]
                    offset += 1

            x_dev = y_dev = None
            if self.__has_dev:
                if len(self.numberSelection) > offset:
                    x_dev = self.numberSelection[offset]
                    offset += 1
                if len(self.numberSelection) > offset:
                    y_dev = self.numberSelection[offset]
                    offset += 1

            height = volume = None
            if self.__has_height and len(self.originalNumberSelection) > offset:
                height = self.originalNumberSelection[offset]
                offset += 1
            if self.__has_volume and len(self.originalNumberSelection) > offset:
                if self.__has_real_vol:
                    volume = self.__real_vol
                    if volume == self.originalNumberSelection[offset]:
                        offset += 1
                else:
                    volume = self.originalNumberSelection[offset]
                    offset += 1

            x_lw_hz = y_lw_hz = None
            if self.__has_lw_hz:
                if len(self.numberSelection) > offset:
                    x_lw_hz = self.numberSelection[offset]
                    offset += 1
                if len(self.numberSelection) > offset:
                    y_lw_hz = self.numberSelection[offset]
                    offset += 1

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            if None in (x_ppm, y_ppm):
                self.peaks2D -= 1
                return

            dstFunc = self.validatePeak2D(index, x_ppm, y_ppm, x_dev, y_dev, None, None,
                                          x_hz, y_hz, x_lw_hz, y_lw_hz, height, None, volume, None)

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
                hint = None
                for _ass in ass.split('-'):
                    assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                    hint = assignments[-1] if assignments[-1] is not None else None

                has_assignments, has_multiple_assignments, asis1, asis2 =\
                    self.checkAssignments2D(index, assignments)

            self.addAssignedPkRow2D(index, dstFunc, has_assignments, has_multiple_assignments,
                                    asis1, asis2,
                                    f'{ass} -> ',
                                    None if (has_assignments and not has_multiple_assignments)
                                    or _ass_ == '?-?' else _ass_)

        finally:
            self.numberSelection.clear()
            self.originalNumberSelection.clear()
            self.__real_vol = None
            self.__noteSelection.clear()

    # Enter a parse tree produced by SparkyNPKParser#peak_3d.
    def enterPeak_3d(self, ctx: SparkyNPKParser.Peak_3dContext):  # pylint: disable=unused-argument
        if self.cur_subtype != 'peak3d':
            self.num_of_dim = 3
            self.initSpectralDim()

        self.peaks3D += 1

        self.atomSelectionSets.clear()
        self.asIsSets.clear()

    # Exit a parse tree produced by SparkyNPKParser#peak_3d.
    def exitPeak_3d(self, ctx: SparkyNPKParser.Peak_3dContext):

        try:

            index = self.peaks3D

            ass = _ass_ = str(ctx.Assignment_3d_ex())
            if '?' in ass:
                ass = None
            if _ass_ == 'A1H-H-H' and not self.isFirstResidueAla:
                ass = _ass_ = None

            try:

                x_ppm = float(str(ctx.Float(0)))
                y_ppm = float(str(ctx.Float(1)))
                z_ppm = float(str(ctx.Float(2)))

            except ValueError:
                self.peaks3D -= 1
                return

            offset = 0

            x_hz = y_hz = z_hz = None
            if self.__has_hz:
                if len(self.numberSelection) > offset:
                    x_hz = self.numberSelection[offset]
                    offset += 1
                if len(self.numberSelection) > offset:
                    y_hz = self.numberSelection[offset]
                    offset += 1
                if len(self.numberSelection) > offset:
                    z_hz = self.numberSelection[offset]
                    offset += 1

            x_dev = y_dev = z_dev = None
            if self.__has_dev:
                if len(self.numberSelection) > offset:
                    x_dev = self.numberSelection[offset]
                    offset += 1
                if len(self.numberSelection) > offset:
                    y_dev = self.numberSelection[offset]
                    offset += 1
                if len(self.numberSelection) > offset:
                    z_dev = self.numberSelection[offset]
                    offset += 1

            height = volume = None
            if self.__has_height and len(self.originalNumberSelection) > offset:
                height = self.originalNumberSelection[offset]
                offset += 1
            if self.__has_volume and len(self.originalNumberSelection) > offset:
                if self.__has_real_vol:
                    volume = self.__real_vol
                    if volume == self.originalNumberSelection[offset]:
                        offset += 1
                else:
                    volume = self.originalNumberSelection[offset]
                    offset += 1

            x_lw_hz = y_lw_hz = z_lw_hz = None
            if self.__has_lw_hz:
                if len(self.numberSelection) > offset:
                    x_lw_hz = self.numberSelection[offset]
                    offset += 1
                if len(self.numberSelection) > offset:
                    y_lw_hz = self.numberSelection[offset]
                    offset += 1
                if len(self.numberSelection) > offset:
                    z_lw_hz = self.numberSelection[offset]
                    offset += 1

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            if None in (x_ppm, y_ppm, z_ppm):
                self.peaks3D -= 1
                return

            dstFunc = self.validatePeak3D(index, x_ppm, y_ppm, z_ppm, x_dev, y_dev, z_dev, None, None, None,
                                          x_hz, y_hz, z_hz, x_lw_hz, y_lw_hz, z_lw_hz, height, None, volume, None)

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
                hint = None
                for _ass in ass.split('-'):
                    assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                    hint = assignments[-1] if assignments[-1] is not None else None

                has_assignments, has_multiple_assignments, asis1, asis2, asis3 =\
                    self.checkAssignments3D(index, assignments)

            self.addAssignedPkRow3D(index, dstFunc, has_assignments, has_multiple_assignments,
                                    asis1, asis2, asis3,
                                    f'{ass} -> ',
                                    None if (has_assignments and not has_multiple_assignments)
                                    or _ass_ == '?-?-?' else _ass_)

        finally:
            self.numberSelection.clear()
            self.originalNumberSelection.clear()
            self.__real_vol = None
            self.__noteSelection.clear()

    # Enter a parse tree produced by SparkyNPKParser#peak_4d.
    def enterPeak_4d(self, ctx: SparkyNPKParser.Peak_4dContext):  # pylint: disable=unused-argument
        if self.cur_subtype != 'peak4d':
            self.num_of_dim = 4
            self.initSpectralDim()

        self.peaks4D += 1

        self.atomSelectionSets.clear()
        self.asIsSets.clear()

    # Exit a parse tree produced by SparkyNPKParser#peak_4d.
    def exitPeak_4d(self, ctx: SparkyNPKParser.Peak_4dContext):

        try:

            index = self.peaks4D

            ass = _ass_ = str(ctx.Assignment_4d_ex())
            if '?' in ass:
                ass = None
            if _ass_ == 'A1H-H-H-H' and not self.isFirstResidueAla:
                ass = _ass_ = None

            try:

                x_ppm = float(str(ctx.Float(0)))
                y_ppm = float(str(ctx.Float(1)))
                z_ppm = float(str(ctx.Float(2)))
                a_ppm = float(str(ctx.Float(3)))

            except ValueError:
                self.peaks4D -= 1
                return

            offset = 0

            x_hz = y_hz = z_hz = a_hz = None
            if self.__has_hz:
                if len(self.numberSelection) > offset:
                    x_hz = self.numberSelection[offset]
                    offset += 1
                if len(self.numberSelection) > offset:
                    y_hz = self.numberSelection[offset]
                    offset += 1
                if len(self.numberSelection) > offset:
                    z_hz = self.numberSelection[offset]
                    offset += 1
                if len(self.numberSelection) > offset:
                    a_hz = self.numberSelection[offset]
                    offset += 1

            x_dev = y_dev = z_dev = a_dev = None
            if self.__has_dev:
                if len(self.numberSelection) > offset:
                    x_dev = self.numberSelection[offset]
                    offset += 1
                if len(self.numberSelection) > offset:
                    y_dev = self.numberSelection[offset]
                    offset += 1
                if len(self.numberSelection) > offset:
                    z_dev = self.numberSelection[offset]
                    offset += 1
                if len(self.numberSelection) > offset:
                    a_dev = self.numberSelection[offset]
                    offset += 1

            height = volume = None
            if self.__has_height and len(self.originalNumberSelection) > offset:
                height = self.originalNumberSelection[offset]
                offset += 1
            if self.__has_volume and len(self.originalNumberSelection) > offset:
                if self.__has_real_vol:
                    volume = self.__real_vol
                    if volume == self.originalNumberSelection[offset]:
                        offset += 1
                else:
                    volume = self.originalNumberSelection[offset]
                    offset += 1

            x_lw_hz = y_lw_hz = z_lw_hz = a_lw_hz = None
            if self.__has_lw_hz:
                if len(self.numberSelection) > offset:
                    x_lw_hz = self.numberSelection[offset]
                    offset += 1
                if len(self.numberSelection) > offset:
                    y_lw_hz = self.numberSelection[offset]
                    offset += 1
                if len(self.numberSelection) > offset:
                    z_lw_hz = self.numberSelection[offset]
                    offset += 1
                if len(self.numberSelection) > offset:
                    a_lw_hz = self.numberSelection[offset]
                    offset += 1

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            if None in (x_ppm, y_ppm, z_ppm, a_ppm):
                self.peaks4D -= 1
                return

            dstFunc = self.validatePeak4D(index, x_ppm, y_ppm, z_ppm, a_ppm, x_dev, y_dev, z_dev, a_dev, None, None, None, None,
                                          x_hz, y_hz, z_hz, a_hz, x_lw_hz, y_lw_hz, z_lw_hz, a_lw_hz, height, None, volume, None)

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
                hint = None
                for _ass in ass.split('-'):
                    assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                    hint = assignments[-1] if assignments[-1] is not None else None

                has_assignments, has_multiple_assignments, asis1, asis2, asis3, asis4 =\
                    self.checkAssignments4D(index, assignments)

            self.addAssignedPkRow4D(index, dstFunc, has_assignments, has_multiple_assignments,
                                    asis1, asis2, asis3, asis4,
                                    f'{ass} -> ',
                                    None if (has_assignments and not has_multiple_assignments)
                                    or _ass_ == '?-?-?-?' else _ass_)

        finally:
            self.numberSelection.clear()
            self.originalNumberSelection.clear()
            self.__real_vol = None
            self.__noteSelection.clear()

    # Enter a parse tree produced by SparkyNPKParser#peak_2d_po.
    def enterPeak_2d_po(self, ctx: SparkyNPKParser.Peak_2d_poContext):  # pylint: disable=unused-argument
        if self.cur_subtype != 'peak2d':
            self.num_of_dim = 2
            self.initSpectralDim()

        self.peaks2D += 1

        self.atomSelectionSets.clear()
        self.asIsSets.clear()

    # Exit a parse tree produced by SparkyNPKParser#peak_2d_po.
    def exitPeak_2d_po(self, ctx: SparkyNPKParser.Peak_2d_poContext):

        try:

            index = self.peaks2D

            ass = _ass_ = None
            if ctx.Assignment_2d_ex():
                ass = _ass_ = str(ctx.Assignment_2d_ex())
                if '?' in ass:
                    ass = None
                if _ass_ == 'A1H-H' and not self.isFirstResidueAla:
                    ass = _ass_ = None
            elif ctx.Assignment_3d_ex():
                _ass_ = str(ctx.Assignment_3d_ex())
            elif ctx.Assignment_4d_ex():
                _ass_ = str(ctx.Assignment_4d_ex())
            if _ass_ == '?-?' and self.__has_note and len(self.__noteSelection) > 0:
                _ass_ = ' '.join(self.__noteSelection)

            try:

                x_ppm = float(str(ctx.Float(0)))
                y_ppm = float(str(ctx.Float(1)))

            except ValueError:
                self.peaks2D -= 1
                return

            if None in (x_ppm, y_ppm):
                self.peaks2D -= 1
                return

            dstFunc = self.validatePeak2D(index, x_ppm, y_ppm, None, None, None, None,
                                          None, None, None, None, None, None, None, None)

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
                hint = None
                for _ass in ass.split('-'):
                    assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                    hint = assignments[-1] if assignments[-1] is not None else None

                has_assignments, has_multiple_assignments, asis1, asis2 =\
                    self.checkAssignments2D(index, assignments)

            self.addAssignedPkRow2D(index, dstFunc, has_assignments, has_multiple_assignments,
                                    asis1, asis2,
                                    f'{ass} -> ',
                                    None if (has_assignments and not has_multiple_assignments)
                                    or _ass_ == '?-?' else _ass_)

        finally:
            self.__noteSelection.clear()

    # Enter a parse tree produced by SparkyNPKParser#peak_3d_po.
    def enterPeak_3d_po(self, ctx: SparkyNPKParser.Peak_3d_poContext):  # pylint: disable=unused-argument
        if self.cur_subtype != 'peak3d':
            self.num_of_dim = 3
            self.initSpectralDim()

        self.peaks3D += 1

        self.atomSelectionSets.clear()
        self.asIsSets.clear()

    # Exit a parse tree produced by SparkyNPKParser#peak_3d_po.
    def exitPeak_3d_po(self, ctx: SparkyNPKParser.Peak_3d_poContext):

        try:

            index = self.peaks3D

            ass = _ass_ = None
            if ctx.Assignment_3d_ex():
                ass = _ass_ = str(ctx.Assignment_3d_ex())
                if '?' in ass:
                    ass = None
                if _ass_ == 'A1H-H-H' and not self.isFirstResidueAla:
                    ass = _ass_ = None
            if ctx.Assignment_4d_ex():
                _ass_ = str(ctx.Assignment_4d_ex())
            if _ass_ == '?-?-?' and self.__has_note and len(self.__noteSelection) > 0:
                _ass_ = ' '.join(self.__noteSelection)

            try:

                x_ppm = float(str(ctx.Float(0)))
                y_ppm = float(str(ctx.Float(1)))
                z_ppm = float(str(ctx.Float(2)))

            except ValueError:
                self.peaks3D -= 1
                return

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            if None in (x_ppm, y_ppm, z_ppm):
                self.peaks3D -= 1
                return

            dstFunc = self.validatePeak3D(index, x_ppm, y_ppm, z_ppm, None, None, None, None, None, None,
                                          None, None, None, None, None, None, None, None, None, None)

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
                hint = None
                for _ass in ass.split('-'):
                    assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                    hint = assignments[-1] if assignments[-1] is not None else None

                has_assignments, has_multiple_assignments, asis1, asis2, asis3 =\
                    self.checkAssignments3D(index, assignments)

            self.addAssignedPkRow3D(index, dstFunc, has_assignments, has_multiple_assignments,
                                    asis1, asis2, asis3,
                                    f'{ass} -> ',
                                    None if (has_assignments and not has_multiple_assignments)
                                    or _ass_ == '?-?-?' else _ass_)

        finally:
            self.__noteSelection.clear()

    # Enter a parse tree produced by SparkyNPKParser#peak_4d_po.
    def enterPeak_4d_po(self, ctx: SparkyNPKParser.Peak_4d_poContext):  # pylint: disable=unused-argument
        if self.cur_subtype != 'peak4d':
            self.num_of_dim = 4
            self.initSpectralDim()

        self.peaks4D += 1

        self.atomSelectionSets.clear()
        self.asIsSets.clear()

    # Exit a parse tree produced by SparkyNPKParser#peak_4d_po.
    def exitPeak_4d_po(self, ctx: SparkyNPKParser.Peak_4d_poContext):

        try:

            index = self.peaks4D

            ass = _ass_ = None
            if ctx.Assignment_4d_ex():
                ass = _ass_ = str(ctx.Assignment_4d_ex())
                if '?' in ass:
                    ass = None
                if _ass_ == 'A1H-H-H-H' and not self.isFirstResidueAla:
                    ass = _ass_ = None
            if _ass_ == '?-?-?-?' and self.__has_note and len(self.__noteSelection) > 0:
                _ass_ = ' '.join(self.__noteSelection)

            try:

                x_ppm = float(str(ctx.Float(0)))
                y_ppm = float(str(ctx.Float(1)))
                z_ppm = float(str(ctx.Float(2)))
                a_ppm = float(str(ctx.Float(3)))

            except ValueError:
                self.peaks4D -= 1
                return

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            if None in (x_ppm, y_ppm, z_ppm, a_ppm):
                self.peaks4D -= 1
                return

            dstFunc = self.validatePeak4D(index, x_ppm, y_ppm, z_ppm, a_ppm, None, None, None, None, None, None, None, None,
                                          None, None, None, None, None, None, None, None, None, None, None, None)

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
                hint = None
                for _ass in ass.split('-'):
                    assignments.append(self.extractPeakAssignment(1, _ass, index, hint))
                    hint = assignments[-1] if assignments[-1] is not None else None

                has_assignments, has_multiple_assignments, asis1, asis2, asis3, asis4 =\
                    self.checkAssignments4D(index, assignments)

            self.addAssignedPkRow4D(index, dstFunc, has_assignments, has_multiple_assignments,
                                    asis1, asis2, asis3, asis4,
                                    f'{ass} -> ',
                                    None if (has_assignments and not has_multiple_assignments)
                                    or _ass_ == '?-?-?-?' else _ass_)

        finally:
            self.__noteSelection.clear()

    # Enter a parse tree produced by SparkyNPKParser#number.
    def enterNumber(self, ctx: SparkyNPKParser.NumberContext):

        try:

            if ctx.Float():
                value = str(ctx.Float())
                self.numberSelection.append(float(value))
                self.originalNumberSelection.append(value)

            elif ctx.Real():
                value = str(ctx.Real())
                self.numberSelection.append(float(value))
                self.originalNumberSelection.append(value)

            elif ctx.Real_vol():
                self.__has_real_vol = True
                if self.reasons is None and 'has_real_vol' not in self.reasonsForReParsing:
                    self.reasonsForReParsing['has_real_vol'] = True
                value = str(ctx.Real_vol())
                if ' ' in value:
                    value = value.split()[0]
                    self.__real_vol = value
                self.numberSelection.append(float(value))
                self.originalNumberSelection.append(value)

            else:
                value = str(ctx.Integer())
                self.numberSelection.append(int(value))
                self.originalNumberSelection.append(value)

        except ValueError:
            self.numberSelection.append(None)
            self.originalNumberSelection.append(None)

    # Exit a parse tree produced by SparkyNPKParser#number.
    def exitNumber(self, ctx: SparkyNPKParser.NumberContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by SparkyNPKParser#note.
    def enterNote(self, ctx: SparkyNPKParser.NoteContext):
        if ctx.Simple_name():
            self.__noteSelection.append(str(ctx.Simple_name()))

        elif ctx.Float():
            self.__noteSelection.append(str(ctx.Float()))

        elif ctx.Integer():
            self.__noteSelection.append(str(ctx.Integer()))

        elif ctx.Note_2d_ex():
            self.__noteSelection.append(str(ctx.Note_2d_ex()))

        elif ctx.Note_3d_ex():
            self.__noteSelection.append(str(ctx.Note_3d_ex()))

        elif ctx.Note_4d_ex():
            self.__noteSelection.append(str(ctx.Note_4d_ex()))

    # Exit a parse tree produced by SparkyNPKParser#note.
    def exitNote(self, ctx: SparkyNPKParser.NoteContext):  # pylint: disable=unused-argument
        pass


# del SparkyNPKParser
