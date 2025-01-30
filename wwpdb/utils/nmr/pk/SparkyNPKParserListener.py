##
# File: SparkyNPKParserListener.py
# Date: 30-Jan-2025
#
# Updates:
""" ParserLister class for SPARKY NPK files.
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

        index = self.peaks2D

        ass = str(ctx.Assignment_2d_ex())
        if '?' in ass:
            ass = None

        x_ppm = float(str(ctx.Float(0)))
        y_ppm = float(str(ctx.Float(1)))

        if not self.hasPolySeq and not self.hasNonPolySeq:
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
                                None if has_assignments and not has_multiple_assignments else ass)

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

        index = self.peaks3D

        ass = str(ctx.Assignment_3d_ex())
        if '?' in ass:
            ass = None

        x_ppm = float(str(ctx.Float(0)))
        y_ppm = float(str(ctx.Float(1)))
        z_ppm = float(str(ctx.Float(2)))

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
                                None if has_assignments and not has_multiple_assignments else ass)

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

        index = self.peaks4D

        ass = str(ctx.Assignment_4d_ex())
        if '?' in ass:
            ass = None

        x_ppm = float(str(ctx.Float(0)))
        y_ppm = float(str(ctx.Float(1)))
        z_ppm = float(str(ctx.Float(2)))
        a_ppm = float(str(ctx.Float(3)))

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
                                None if has_assignments and not has_multiple_assignments else ass)


# del SparkyNPKParser
