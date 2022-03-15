##
# File: XplorMRParserListener.py
# Date: 09-Feb-2022
#
# Updates:
# Generated from XplorMRParser.g4 by ANTLR 4.9
""" ParserLister class for XPLOR-NIH MR files.
    @author: Masashi Yokochi
"""
import sys
import re
import itertools

import numpy as np

from antlr4 import ParseTreeListener
from rmsd.calculate_rmsd import (int_atom, ELEMENT_WEIGHTS)  # noqa: F401 pylint: disable=no-name-in-module, import-error

try:
    from wwpdb.utils.nmr.mr.XplorMRParser import XplorMRParser
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (toNpArray,
                                                       toRegEx,
                                                       checkCoordinates,
                                                       getTypeOfDihedralRestraint,
                                                       REPRESENTATIVE_MODEL_ID,
                                                       DIST_RESTRAINT_RANGE,
                                                       DIST_RESTRAINT_ERROR,
                                                       ANGLE_RESTRAINT_RANGE,
                                                       ANGLE_RESTRAINT_ERROR,
                                                       RDC_RESTRAINT_RANGE,
                                                       RDC_RESTRAINT_ERROR,
                                                       XPLOR_RDC_PRINCIPAL_AXIS_NAMES)

    from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
    from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from wwpdb.utils.nmr.NEFTranslator.NEFTranslator import (NEFTranslator,
                                                             isotopeNumsOfNmrObsNucs)
except ImportError:
    from nmr.mr.XplorMRParser import XplorMRParser
    from nmr.mr.ParserListenerUtil import (toNpArray,
                                           toRegEx,
                                           checkCoordinates,
                                           getTypeOfDihedralRestraint,
                                           REPRESENTATIVE_MODEL_ID,
                                           DIST_RESTRAINT_RANGE,
                                           DIST_RESTRAINT_ERROR,
                                           ANGLE_RESTRAINT_RANGE,
                                           ANGLE_RESTRAINT_ERROR,
                                           RDC_RESTRAINT_RANGE,
                                           RDC_RESTRAINT_ERROR,
                                           XPLOR_RDC_PRINCIPAL_AXIS_NAMES)

    from nmr.ChemCompUtil import ChemCompUtil
    from nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from nmr.NEFTranslator.NEFTranslator import (NEFTranslator,
                                                 isotopeNumsOfNmrObsNucs)


DIST_RANGE_MIN = DIST_RESTRAINT_RANGE['min_inclusive']
DIST_RANGE_MAX = DIST_RESTRAINT_RANGE['max_inclusive']

DIST_ERROR_MIN = DIST_RESTRAINT_ERROR['min_exclusive']
DIST_ERROR_MAX = DIST_RESTRAINT_ERROR['max_exclusive']


ANGLE_RANGE_MIN = ANGLE_RESTRAINT_RANGE['min_inclusive']
ANGLE_RANGE_MAX = ANGLE_RESTRAINT_RANGE['max_inclusive']

ANGLE_ERROR_MIN = ANGLE_RESTRAINT_ERROR['min_exclusive']
ANGLE_ERROR_MAX = ANGLE_RESTRAINT_ERROR['max_exclusive']


RDC_RANGE_MIN = RDC_RESTRAINT_RANGE['min_exclusive']
RDC_RANGE_MAX = RDC_RESTRAINT_RANGE['max_exclusive']

RDC_ERROR_MIN = RDC_RESTRAINT_ERROR['min_exclusive']
RDC_ERROR_MAX = RDC_RESTRAINT_ERROR['max_exclusive']


# This class defines a complete listener for a parse tree produced by XplorMRParser.
class XplorMRParserListener(ParseTreeListener):

    __verbose = None
    __lfh = None
    __debug = False

    distRestraints = 0      # XPLOR-NIH: Distance restraints
    dihedRestraints = 0     # XPLOR-NIH: Dihedral angle restraints
    rdcRestraints = 0       # XPLOR-NIH: Residual dipolar coupling restraints
    planeRestraints = 0     # XPLOR-NIH: Planality restraints
    adistRestraints = 0     # XPLOR-NIH: Antidiatance restraints
    jcoupRestraints = 0     # XPLOR-NIH: Scalar J-coupling restraints
    hvycsRestraints = 0     # XPLOR-NIH: Carbon chemical shift restraints
    procsRestraints = 0     # XPLOR-NIH: Proton chemical shift restraints
    ramaRestraints = 0      # XPLOR-NIH: Dihedral angle database restraints
    radiRestraints = 0      # XPLOR-NIH: Radius of gyration restraints
    diffRestraints = 0      # XPLOR-NIH: Diffusion anisotropy restraints
    nbaseRestraints = 0     # XPLOR-NIH: Residue-residue position/orientation database restraints
    csaRestraints = 0       # XPLOR-NIH: (Pseudo) Chemical shift anisotropy restraints
    angRestraints = 0       # XPLOR-NIH: Angle database restraints
    preRestraints = 0       # XPLOR-NIH: Paramagnetic relaxation enhancement restraints
    pcsRestraints = 0       # XPLOR-NIH: Paramagnetic pseudocontact shift restraints
    prdcRestraints = 0      # XPLOR-NIH: Paramagnetic residual dipolar coupling restraints
    pangRestraints = 0      # XPLOR-NIH: Paramagnetic orientation restraints
    pccrRestraints = 0      # XPLOR-NIH: Paramagnetic cross-correlation rate restraints
    hbondRestraints = 0     # XPLOR-NIH: Hydrogen bond geometry restraints

    distStatements = 0      # XPLOR-NIH: Distance statements
    dihedStatements = 0     # XPLOR-NIH: Dihedral angle statements
    rdcStatements = 0       # XPLOR-NIH: Residual dipolar coupling statements
    planeStatements = 0     # XPLOR-NIH: Planality statements
    adistStatements = 0     # XPLOR-NIH: Antidiatance statements
    jcoupStatements = 0     # XPLOR-NIH: Scalar J-coupling statements
    hvycsStatements = 0     # XPLOR-NIH: Carbon chemical shift statements
    procsStatements = 0     # XPLOR-NIH: Proton chemical shift statements
    ramaStatements = 0      # XPLOR-NIH: Dihedral angle database statements
    radiStatements = 0      # XPLOR-NIH: Radius of gyration statements
    diffStatements = 0      # XPLOR-NIH: Diffusion anisotropy statements
    nbaseStatements = 0     # XPLOR-NIH: Residue-residue position/orientation database statements
    csaStatements = 0       # XPLOR-NIH: (Pseudo) Chemical shift anisotropy statements
    angStatements = 0       # XPLOR-NIH: Angle database statements
    preStatements = 0       # XPLOR-NIH: Paramagnetic relaxation enhancement statements
    pcsStatements = 0       # XPLOR-NIH: Paramagnetic pseudocontact shift statements
    prdcStatements = 0      # XPLOR-NIH: Paramagnetic residual dipolar coupling statements
    pangStatements = 0      # XPLOR-NIH: Paramagnetic orientation statements
    pccrStatements = 0      # XPLOR-NIH: Paramagnetic cross-correlation rate statements
    hbondStatements = 0     # XPLOR-NIH: Hydrogen bond geometry statements

    # CCD accessing utility
    __ccU = None

    # BMRB chemical shift statistics
    __csStat = None

    # NEFTranslator
    __nefT = None

    # CIF reader
    __cR = None
    __hasCoord = False

    # data item name for model ID in 'atom_site' category
    __modelNumName = None

    # data item names for auth_asym_id, auth_seq_id, auth_atom_id in 'atom_site' category
    __authAsymId = None
    __authSeqId = None
    __authAtomId = None
    # __altAuthAtomId = None

    # polymer sequences in the coordinate file generated by NmrDpUtility.__extractCoordPolymerSequence()
    __hasPolySeq = False
    __polySeq = None
    # __altPolySeq = None
    __coordAtomSite = None
    __coordUnobsRes = None
    __labelToAuthSeq = None
    __preferAuthSeq = True

    # current restraint subtype
    __cur_subtype = None

    depth = 0

    stackSelections = None  # stack of selection
    stackTerms = None  # stack of term
    stackFactors = None  # stack of factor

    factor = None

    # disntace
    noePotential = 'biharmonic'
    squareExponent = 2.0
    squareOffset = 0.0
    rSwitch = 10.0
    scale = 1.0
    symmTarget = None
    symmDminus = None
    symmDplus = None

    # 3D vectors in point clause
    inVector3D = False
    inVector3D_columnSel = -1
    inVector3D_tail = None
    inVector3D_head = None
    vector3D = None

    # RDC
    potential = 'square'
    average = 'average'

    # collection of atom selection
    atomSelectionSet = None

    warningMessage = ''

    def __init__(self, verbose=True, log=sys.stdout, cR=None, polySeq=None,
                 coordAtomSite=None, coordUnobsRes=None, labelToAuthSeq=None,
                 ccU=None, csStat=None, nefT=None):
        self.__verbose = verbose
        self.__lfh = log
        self.__cR = cR
        self.__hasCoord = cR is not None

        if self.__hasCoord:
            ret = checkCoordinates(verbose, log, cR, polySeq,
                                   coordAtomSite, coordUnobsRes, labelToAuthSeq)
            self.__modelNumName = ret['model_num_name']
            self.__authAsymId = ret['auth_asym_id']
            self.__authSeqId = ret['auth_seq_id']
            self.__authAtomId = ret['auth_atom_id']
            # self.__altAuthAtomId = ret['alt_auth_atom_id']
            self.__polySeq = ret['polymer_sequence']
            # self.__altPolySeq = ret['alt_polymer_sequence']
            self.__coordAtomSite = ret['coord_atom_site']
            self.__coordUnobsRes = ret['coord_unobs_res']
            self.__labelToAuthSeq = ret['label_to_auth_seq']

        self.__hasPolySeq = self.__polySeq is not None and len(self.__polySeq) > 0

        # CCD accessing utility
        self.__ccU = ChemCompUtil(verbose, log) if ccU is None else ccU

        # BMRB chemical shift statistics
        self.__csStat = BMRBChemShiftStat(False, log, self.__ccU) if csStat is None else csStat

        # NEFTranslator
        self.__nefT = NEFTranslator(verbose, log, self.__ccU, self.__csStat) if nefT is None else nefT

    # Enter a parse tree produced by XplorMRParser#xplor_nih_mr.
    def enterXplor_nih_mr(self, ctx: XplorMRParser.Xplor_nih_mrContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#xplor_nih_mr.
    def exitXplor_nih_mr(self, ctx: XplorMRParser.Xplor_nih_mrContext):  # pylint: disable=unused-argument
        if len(self.warningMessage) == 0:
            self.warningMessage = None
        else:
            self.warningMessage = self.warningMessage[0:-1]
            self.warningMessage = '\n'.join(set(self.warningMessage.split('\n')))

    # Enter a parse tree produced by XplorMRParser#distance_restraint.
    def enterDistance_restraint(self, ctx: XplorMRParser.Distance_restraintContext):  # pylint: disable=unused-argument
        self.distStatements += 1

        self.noePotential = 'biharmonic'  # default potential
        self.squareExponent = 2.0
        self.squareOffset = 0.0
        self.rSwitch = 10.0
        self.scale = 1.0
        self.symmTarget = None
        self.symmDminus = None
        self.symmDplus = None

    # Exit a parse tree produced by XplorMRParser#distance_restraint.
    def exitDistance_restraint(self, ctx: XplorMRParser.Distance_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#dihedral_angle_restraint.
    def enterDihedral_angle_restraint(self, ctx: XplorMRParser.Dihedral_angle_restraintContext):  # pylint: disable=unused-argument
        self.dihedStatements += 1

        self.scale = 1.0

    # Exit a parse tree produced by XplorMRParser#dihedral_angle_restraint.
    def exitDihedral_angle_restraint(self, ctx: XplorMRParser.Dihedral_angle_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#rdc_restraint.
    def enterRdc_restraint(self, ctx: XplorMRParser.Rdc_restraintContext):  # pylint: disable=unused-argument
        self.rdcStatements += 1

        self.potential = 'square'  # default potential
        self.scale = 1.0

    # Exit a parse tree produced by XplorMRParser#rdc_restraint.
    def exitRdc_restraint(self, ctx: XplorMRParser.Rdc_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#planar_restraint.
    def enterPlanar_restraint(self, ctx: XplorMRParser.Planar_restraintContext):  # pylint: disable=unused-argument
        self.planeStatements += 1

    # Exit a parse tree produced by XplorMRParser#planar_restraint.
    def exitPlanar_restraint(self, ctx: XplorMRParser.Planar_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#antidistance_restraint.
    def enterAntidistance_restraint(self, ctx: XplorMRParser.Antidistance_restraintContext):  # pylint: disable=unused-argument
        self.adistStatements += 1

    # Exit a parse tree produced by XplorMRParser#antidistance_restraint.
    def exitAntidistance_restraint(self, ctx: XplorMRParser.Antidistance_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#coupling_restraint.
    def enterCoupling_restraint(self, ctx: XplorMRParser.Coupling_restraintContext):  # pylint: disable=unused-argument
        self.jcoupStatements += 1

    # Exit a parse tree produced by XplorMRParser#coupling_restraint.
    def exitCoupling_restraint(self, ctx: XplorMRParser.Coupling_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#carbon_shift_restraint.
    def enterCarbon_shift_restraint(self, ctx: XplorMRParser.Carbon_shift_restraintContext):  # pylint: disable=unused-argument
        self.hvycsStatements += 1

    # Exit a parse tree produced by XplorMRParser#carbon_shift_restraint.
    def exitCarbon_shift_restraint(self, ctx: XplorMRParser.Carbon_shift_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#proton_shift_restraint.
    def enterProton_shift_restraint(self, ctx: XplorMRParser.Proton_shift_restraintContext):  # pylint: disable=unused-argument
        self.procsStatements += 1

    # Exit a parse tree produced by XplorMRParser#proton_shift_restraint.
    def exitProton_shift_restraint(self, ctx: XplorMRParser.Proton_shift_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#dihedral_angle_db_restraint.
    def enterDihedral_angle_db_restraint(self, ctx: XplorMRParser.Dihedral_angle_db_restraintContext):  # pylint: disable=unused-argument
        self.angStatements += 1

    # Exit a parse tree produced by XplorMRParser#dihedral_angle_db_restraint.
    def exitDihedral_angle_db_restraint(self, ctx: XplorMRParser.Dihedral_angle_db_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#radius_of_gyration_restraint.
    def enterRadius_of_gyration_restraint(self, ctx: XplorMRParser.Radius_of_gyration_restraintContext):  # pylint: disable=unused-argument
        self.radiStatements += 1

    # Exit a parse tree produced by XplorMRParser#radius_of_gyration_restraint.
    def exitRadius_of_gyration_restraint(self, ctx: XplorMRParser.Radius_of_gyration_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#diffusion_anisotropy_restraint.
    def enterDiffusion_anisotropy_restraint(self, ctx: XplorMRParser.Diffusion_anisotropy_restraintContext):  # pylint: disable=unused-argument
        self.diffStatements += 1

    # Exit a parse tree produced by XplorMRParser#diffusion_anisotropy_restraint.
    def exitDiffusion_anisotropy_restraint(self, ctx: XplorMRParser.Diffusion_anisotropy_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#orientation_db_restraint.
    def enterOrientation_db_restraint(self, ctx: XplorMRParser.Orientation_db_restraintContext):  # pylint: disable=unused-argument
        self.nbaseStatements += 1

    # Exit a parse tree produced by XplorMRParser#orientation_db_restraint.
    def exitOrientation_db_restraint(self, ctx: XplorMRParser.Orientation_db_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#csa_restraint.
    def enterCsa_restraint(self, ctx: XplorMRParser.Csa_restraintContext):  # pylint: disable=unused-argument
        self.csaStatements += 1  # either CSA or pseudo CSA

    # Exit a parse tree produced by XplorMRParser#csa_restraint.
    def exitCsa_restraint(self, ctx: XplorMRParser.Csa_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#pcsa_restraint.
    def enterPcsa_restraint(self, ctx: XplorMRParser.Pcsa_restraintContext):  # pylint: disable=unused-argument
        self.csaStatements += 1  # either CSA or pseudo CSA

    # Exit a parse tree produced by XplorMRParser#pcsa_restraint.
    def exitPcsa_restraint(self, ctx: XplorMRParser.Pcsa_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#one_bond_coupling_restraint.
    def enterOne_bond_coupling_restraint(self, ctx: XplorMRParser.One_bond_coupling_restraintContext):  # pylint: disable=unused-argument
        """
        @deprecated: This restraint has not been useful in practice, but has been preserved for historical reasons.
        """

    # Exit a parse tree produced by XplorMRParser#one_bond_coupling_restraint.
    def exitOne_bond_coupling_restraint(self, ctx: XplorMRParser.One_bond_coupling_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#angle_db_restraint.
    def enterAngle_db_restraint(self, ctx: XplorMRParser.Angle_db_restraintContext):  # pylint: disable=unused-argument
        """
        @deprecated:  This term has not proved useful in practice and is only here for historical reasons.
        """

    # Exit a parse tree produced by XplorMRParser#angle_db_restraint.
    def exitAngle_db_restraint(self, ctx: XplorMRParser.Angle_db_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#pre_restraint.
    def enterPre_restraint(self, ctx: XplorMRParser.Pre_restraintContext):  # pylint: disable=unused-argument
        self.preStatements += 1

    # Exit a parse tree produced by XplorMRParser#pre_restraint.
    def exitPre_restraint(self, ctx: XplorMRParser.Pre_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#pcs_restraint.
    def enterPcs_restraint(self, ctx: XplorMRParser.Pcs_restraintContext):  # pylint: disable=unused-argument
        self.pcsStatements += 1

    # Exit a parse tree produced by XplorMRParser#pcs_restraint.
    def exitPcs_restraint(self, ctx: XplorMRParser.Pcs_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#prdc_restraint.
    def enterPrdc_restraint(self, ctx: XplorMRParser.Prdc_restraintContext):  # pylint: disable=unused-argument
        self.prdcStatements += 1

    # Exit a parse tree produced by XplorMRParser#prdc_restraint.
    def exitPrdc_restraint(self, ctx: XplorMRParser.Prdc_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#porientation_restraint.
    def enterPorientation_restraint(self, ctx: XplorMRParser.Porientation_restraintContext):  # pylint: disable=unused-argument
        self.prdcStatements += 1

    # Exit a parse tree produced by XplorMRParser#porientation_restraint.
    def exitPorientation_restraint(self, ctx: XplorMRParser.Porientation_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#pccr_restraint.
    def enterPccr_restraint(self, ctx: XplorMRParser.Pccr_restraintContext):  # pylint: disable=unused-argument
        self.pccrStatements += 1

    # Exit a parse tree produced by XplorMRParser#pccr_restraint.
    def exitPccr_restraint(self, ctx: XplorMRParser.Pccr_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#hbond_restraint.
    def enterHbond_restraint(self, ctx: XplorMRParser.Hbond_restraintContext):  # pylint: disable=unused-argument
        self.hbondStatements += 1

    # Exit a parse tree produced by XplorMRParser#hbond_restraint.
    def exitHbond_restraint(self, ctx: XplorMRParser.Hbond_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#noe_statement.
    def enterNoe_statement(self, ctx: XplorMRParser.Noe_statementContext):
        if ctx.Noe_potential():
            code = str(ctx.Noe_potential()).upper()
            if code.startswith('BIHA'):
                self.noePotential = 'biharmonic'
            elif code.startswith('LOGN'):
                self.noePotential = 'lognormal'
            elif code.startswith('SQUA'):
                self.noePotential = 'square'
            elif code.startswith('SOFT'):
                self.noePotential = 'softsquare'
            elif code.startswith('SYMM'):
                self.noePotential = 'symmetry'
            elif code.startswith('HIGH'):
                self.noePotential = 'high'
            else:  # 3DPO
                self.noePotential = '3dpo'

        elif ctx.SqExponent():
            self.squareExponent = float(ctx.Real())
            if self.squareExponent <= 0.0:
                self.warningMessage += f"[Invalid data] "\
                    "The exponent value of square-well or soft-square function "\
                    f"NOE {str(ctx.SqExponent())} {str(ctx.Simple_names())} {self.squareExponent} END' must be a positive value.\n"

        elif ctx.SqOffset():
            self.squareOffset = float(ctx.Real())
            if self.squareOffset < 0.0:
                self.warningMessage += f"[Invalid data] "\
                    "The offset value of square-well or soft-square function "\
                    f"NOE {str(ctx.SqOffset())} {str(ctx.Simple_names())} {self.squareOffset} END' must not be a negative value.\n"

        elif ctx.Rswitch():
            self.rSwitch = float(ctx.Real())
            if self.rSwitch < 0.0:
                self.warningMessage += f"[Invalid data] "\
                    "The smoothing parameter of soft-square function "\
                    f"NOE {str(ctx.Rswitch())} {str(ctx.Simple_names())} {self.rSwitch} END' must not be a negative value.\n"

        elif ctx.Scale():
            self.scale = float(ctx.Real())
            if self.scale <= 0.0:
                self.warningMessage += f"[Invalid data] "\
                    f"The scale value 'NOE {str(ctx.Scale())} {str(ctx.Simple_names())} {self.scale} END' must be a positive value.\n"

        elif ctx.Reset():
            self.noePotential = 'biharmonic'  # default potential
            self.squareExponent = 2.0
            self.squareOffset = 0.0
            self.rSwitch = 10.0
            self.scale = 1.0
            self.symmTarget = None
            self.symmDminus = None
            self.symmDplus = None

    # Exit a parse tree produced by XplorMRParser#noe_statement.
    def exitNoe_statement(self, ctx: XplorMRParser.Noe_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#noe_assign.
    def enterNoe_assign(self, ctx: XplorMRParser.Noe_assignContext):  # pylint: disable=unused-argument
        self.distRestraints += 1
        self.__cur_subtype = 'dist'

        self.atomSelectionSet = []

    # Exit a parse tree produced by XplorMRParser#noe_assign.
    def exitNoe_assign(self, ctx: XplorMRParser.Noe_assignContext):
        target = float(str(ctx.Real(0)))
        dminus = float(str(ctx.Real(1)))
        dplus = float(str(ctx.Real(2)))

        target_value = None
        lower_limit = None
        upper_limit = None
        lower_linear_limit = None
        upper_linear_limit = None

        if self.noePotential == 'biharmonic':
            target_value = target
            lower_limit = target - dminus
            upper_limit = target + dplus
        elif self.noePotential == 'lognormal':
            target_value = target
        elif self.noePotential == 'square':
            target_value = target
            if abs(self.squareExponent - 2.0) < abs(self.squareExponent - 1.0):
                lower_linear = target - dminus
                upper_linear = target + dplus - self.squareOffset
            else:
                lower_linear_limit = target - dminus
                upper_linear_limit = target + dplus - self.squareOffset
        elif self.noePotential == 'softsquare':
            target_value = target
            if abs(self.squareExponent - 2.0) < abs(self.squareExponent - 1.0):
                lower_linear = target - dminus
                upper_linear = target + dplus - self.squareOffset
                upper_linear_limit = target + dplus - self.squareOffset + self.rSwitch
            else:
                lower_linear_limit = target - dminus
                upper_linear_limit = target + dplus - self.squareOffset
        elif self.noePotential == 'symmetry':
            if target == 0.0:
                target = self.symmTarget
                dminus = self.symmDminus
                dplus = self.symmDplus
            else:
                self.symmTarget = target
                self.symmDminus = dminus
                self.symmDplus = dplus
            target_value = target
            if abs(self.squareExponent - 2.0) < abs(self.squareExponent - 1.0):
                lower_linear = target - dminus
                upper_linear = target + dplus - self.squareOffset
                upper_linear_limit = target + dplus - self.squareOffset + self.rSwitch
            else:
                lower_linear_limit = target - dminus
                upper_linear_limit = target + dplus - self.squareOffset
        elif self.noePotential == 'high':
            target_value = target
            lower_linear = target - dminus
            upper_linear = target + dplus
            lower_linear_limit = lower_linear - 0.1
            upper_linear_limit = upper_linear + 0.1
        else:  # 3dpo
            if target == 0.0:
                target = self.symmTarget
                dminus = self.symmDminus
                dplus = self.symmDplus
            else:
                self.symmTarget = target
                self.symmDminus = dminus
                self.symmDplus = dplus
            target_value = target
            lower_limit = target - dminus
            upper_limit = target + dplus

        validRange = True
        dstFunc = {'weight': self.scale}

        if target_value is not None:
            if DIST_ERROR_MIN < target_value < DIST_ERROR_MAX:
                dstFunc['target_value'] = f"{target_value:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The target value='{target_value}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if lower_limit is not None:
            if DIST_ERROR_MIN < lower_limit < DIST_ERROR_MAX:
                dstFunc['lower_limit'] = f"{lower_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower limit value='{lower_limit}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if upper_limit is not None:
            if DIST_ERROR_MIN < upper_limit < DIST_ERROR_MAX:
                dstFunc['upper_limit'] = f"{upper_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if lower_linear_limit is not None:
            if DIST_ERROR_MIN < lower_linear_limit < DIST_ERROR_MAX:
                dstFunc['lower_linear_limit'] = f"{lower_linear_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower linear limit value='{lower_linear_limit}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if upper_linear_limit is not None:
            if DIST_ERROR_MIN < upper_linear_limit < DIST_ERROR_MAX:
                dstFunc['upper_linear_limit'] = f"{upper_linear_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper linear limit value='{upper_linear_limit}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if not validRange:
            return

        if target_value is not None:
            if DIST_RANGE_MIN <= target_value <= DIST_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The target value='{target_value}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        if lower_limit is not None:
            if DIST_RANGE_MIN <= lower_limit <= DIST_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower limit value='{lower_limit}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        if upper_limit is not None:
            if DIST_RANGE_MIN <= upper_limit <= DIST_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        if lower_linear_limit is not None:
            if DIST_RANGE_MIN <= lower_linear_limit <= DIST_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower linear limit value='{lower_linear_limit}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        if upper_linear_limit is not None:
            if DIST_RANGE_MIN <= upper_linear_limit <= DIST_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper linear limit value='{upper_linear_limit}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        for i in range(0, len(self.atomSelectionSet), 2):
            for atom1, atom2 in itertools.product(self.atomSelectionSet[i],
                                                  self.atomSelectionSet[i + 1]):
                if self.__verbose:
                    print(f"subtype={self.__cur_subtype} id={self.distRestraints} "
                          f"atom1={atom1} atom2={atom2} {dstFunc}")

    # Enter a parse tree produced by XplorMRParser#predict_statement.
    def enterPredict_statement(self, ctx: XplorMRParser.Predict_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#predict_statement.
    def exitPredict_statement(self, ctx: XplorMRParser.Predict_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#dihedral_statement.
    def enterDihedral_statement(self, ctx: XplorMRParser.Dihedral_statementContext):
        if ctx.Scale():
            self.scale = float(ctx.Real())
            if self.scale <= 0.0:
                self.warningMessage += f"[Invalid data] "\
                    f"The scale value 'RESTRAINT DIHEDRAL {str(ctx.Scale())} {self.scale} END' must be a positive value.\n"

        elif ctx.Reset():
            self.scale = 1.0

    # Exit a parse tree produced by XplorMRParser#dihedral_statement.
    def exitDihedral_statement(self, ctx: XplorMRParser.Dihedral_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#dihedral_assign.
    def enterDihedral_assign(self, ctx: XplorMRParser.Dihedral_assignContext):  # pylint: disable=unused-argument
        self.dihedRestraints += 1
        self.__cur_subtype = 'dihed'

        self.atomSelectionSet = []

    # Exit a parse tree produced by XplorMRParser#dihedral_assign.
    def exitDihedral_assign(self, ctx: XplorMRParser.Dihedral_assignContext):
        energyConst = float(str(ctx.Real(0)))
        target = float(str(ctx.Real(1)))
        delta = abs(float(str(ctx.Real(2))))
        exponent = int(str(ctx.Integer()))

        if exponent not in (1, 2):
            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                f"The exponent value of dihedral angle restraint 'ed={exponent}' must be one (linear well) or two (square well).\n"
            return

        target_value = None
        lower_limit = None
        upper_limit = None
        lower_linear_limit = None
        upper_linear_limit = None

        if exponent == 2:
            target_value = target
            lower_limit = target - delta
            upper_limit = target + delta
        else:
            target_value = target
            lower_linear_limit = target - delta
            upper_linear_limit = target + delta

        validRange = True
        dstFunc = {'weight': self.scale}

        if target_value is not None:
            if ANGLE_ERROR_MIN < target_value < ANGLE_ERROR_MAX:
                dstFunc['target_value'] = f"{target_value:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The target value='{target_value}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"

        if lower_limit is not None:
            if ANGLE_ERROR_MIN < lower_limit < ANGLE_ERROR_MAX:
                dstFunc['lower_limit'] = f"{lower_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower limit value='{lower_limit}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"

        if upper_limit is not None:
            if ANGLE_ERROR_MIN < upper_limit < ANGLE_ERROR_MAX:
                dstFunc['upper_limit'] = f"{upper_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"

        if lower_linear_limit is not None:
            if ANGLE_ERROR_MIN < lower_linear_limit < ANGLE_ERROR_MAX:
                dstFunc['lower_linear_limit'] = f"{lower_linear_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower linear limit value='{lower_linear_limit}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"

        if upper_linear_limit is not None:
            if ANGLE_ERROR_MIN < upper_linear_limit < ANGLE_ERROR_MAX:
                dstFunc['upper_linear_limit'] = f"{upper_linear_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper linear limit value='{upper_linear_limit}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"

        if not validRange:
            return

        if target_value is not None:
            if ANGLE_RANGE_MIN <= target_value <= ANGLE_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The target value='{target_value}' should be within range {ANGLE_RESTRAINT_RANGE}.\n"

        if lower_limit is not None:
            if ANGLE_RANGE_MIN <= lower_limit <= ANGLE_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower limit value='{lower_limit}' should be within range {ANGLE_RESTRAINT_RANGE}.\n"

        if upper_limit is not None:
            if ANGLE_RANGE_MIN <= upper_limit <= ANGLE_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit}' should be within range {ANGLE_RESTRAINT_RANGE}.\n"

        if lower_linear_limit is not None:
            if ANGLE_RANGE_MIN <= lower_linear_limit <= ANGLE_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower linear limit value='{lower_linear_limit}' should be within range {ANGLE_RESTRAINT_RANGE}.\n"

        if upper_linear_limit is not None:
            if ANGLE_RANGE_MIN <= upper_linear_limit <= ANGLE_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper linear limit value='{upper_linear_limit}' should be within range {ANGLE_RESTRAINT_RANGE}.\n"

        compId = self.atomSelectionSet[0][0]['comp_id']
        peptide, nucleotide, carbohydrate = self.__csStat.getTypeOfCompId(compId)

        if not self.areUniqueCoordAtoms('a dihedral angle'):
            return

        for atom1, atom2, atom3, atom4 in itertools.product(self.atomSelectionSet[0],
                                                            self.atomSelectionSet[1],
                                                            self.atomSelectionSet[2],
                                                            self.atomSelectionSet[3]):
            if self.__verbose:
                angleName = getTypeOfDihedralRestraint(peptide, nucleotide, carbohydrate,
                                                       [atom1, atom2, atom3, atom4])
                print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} angleName={angleName} "
                      f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} {dstFunc} "
                      f"energy_const={energyConst}")

    def areUniqueCoordAtoms(self, subtype_name):
        """ Check whether atom selection sets are uniquely assigned.
        """

        for _atomSelectionSet in self.atomSelectionSet:

            if len(_atomSelectionSet) < 2:
                continue

            for atom1, atom2 in itertools.combinations(_atomSelectionSet, _atomSelectionSet):
                if atom1['chain_id'] != atom2['chain_id']:
                    continue
                if atom1['seq_id'] != atom2['seq_id']:
                    continue
                self.warningMessage += f"[Invalid atom selection] {self.__getCurrentRestraint()}"\
                    f"Ambiguous atom selection '{atom1['chain_id']}:{atom1['seq_id']}:{atom1['atom_id']} or "\
                    f"{atom2['atom_id']}' is not allowed as {subtype_name} restraint.\n"
                return False

        return True

    # Enter a parse tree produced by XplorMRParser#sani_statement.
    def enterSani_statement(self, ctx: XplorMRParser.Sani_statementContext):
        if ctx.Rdc_potential():
            code = str(ctx.Rdc_potential()).upper()[0:4]
            if code == 'SQUA':
                self.potential = 'square'
            if code == 'HARM':
                self.potential = 'harmonic'

    # Exit a parse tree produced by XplorMRParser#sani_statement.
    def exitSani_statement(self, ctx: XplorMRParser.Sani_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#sani_assign.
    def enterSani_assign(self, ctx: XplorMRParser.Sani_assignContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1
        self.__cur_subtype = 'rdc'

        self.atomSelectionSet = []

    # Exit a parse tree produced by XplorMRParser#sani_assign.
    def exitSani_assign(self, ctx: XplorMRParser.Sani_assignContext):
        target = float(str(ctx.Real(0)))
        delta = abs(float(str(ctx.Real(1))))

        target_value = None
        lower_limit = None
        upper_limit = None

        if self.potential == 'square':
            target_value = target
            lower_limit = target - delta
            upper_limit = target + delta
            if ctx.Real(2):
                error_grater = delta
                error_less = abs(float(str(ctx.Real(2))))
                lower_limit = target - error_less
                upper_limit = target + error_grater
        else:
            target_value = target

        validRange = True
        dstFunc = {'weight': self.scale}

        if target_value is not None:
            if RDC_ERROR_MIN < target_value < RDC_ERROR_MAX:
                dstFunc['target_value'] = f"{target_value:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The target value='{target_value}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if lower_limit is not None:
            if RDC_ERROR_MIN < lower_limit < RDC_ERROR_MAX:
                dstFunc['lower_limit'] = f"{lower_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower limit value='{lower_limit}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if upper_limit is not None:
            if RDC_ERROR_MIN < upper_limit < RDC_ERROR_MAX:
                dstFunc['upper_limit'] = f"{upper_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if not validRange:
            return

        if target_value is not None:
            if RDC_RANGE_MIN < target_value < RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The target value='{target_value}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        if lower_limit is not None:
            if RDC_RANGE_MIN < lower_limit < RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower limit value='{lower_limit}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        if upper_limit is not None:
            if RDC_RANGE_MIN < upper_limit < RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        if not self.areUniqueCoordAtoms('an RDC'):
            return

        chain_id_1 = self.atomSelectionSet[4][0]['chain_id']
        seq_id_1 = self.atomSelectionSet[4][0]['seq_id']
        comp_id_1 = self.atomSelectionSet[4][0]['comp_id']
        atom_id_1 = self.atomSelectionSet[4][0]['atom_id']

        chain_id_2 = self.atomSelectionSet[5][0]['chain_id']
        seq_id_2 = self.atomSelectionSet[5][0]['seq_id']
        comp_id_2 = self.atomSelectionSet[5][0]['comp_id']
        atom_id_2 = self.atomSelectionSet[5][0]['atom_id']

        if (atom_id_1[0] not in isotopeNumsOfNmrObsNucs) or (atom_id_2[0] not in isotopeNumsOfNmrObsNucs):
            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                f"Non-magnetic susceptible spin appears in RDC vector; "\
                f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
            return

        if chain_id_1 != chain_id_2:
            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                f"Found inter-chain RDC vector; "\
                f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
            return

        if abs(seq_id_1 - seq_id_2) > 1:
            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                f"Found inter-residue RDC vector; "\
                f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
            return

        if abs(seq_id_1 - seq_id_2) == 1:

            if self.__csStat.peptideLike(comp_id_1) and self.__csStat.peptideLike(comp_id_2) and\
               ((seq_id_1 < seq_id_2 and atom_id_1 == 'C' and atom_id_2 in ('N', 'H')) or (seq_id_1 > seq_id_2 and atom_id_1 in ('N', 'H') and atom_id_2 == 'C')):
                pass

            else:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    "Found inter-residue RDC vector; "\
                    f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                return

        elif atom_id_1 == atom_id_2:
            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                "Found zero RDC vector; "\
                f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
            return

        else:

            if self.__ccU.updateChemCompDict(comp_id_1):  # matches with comp_id in CCD

                if not any(b for b in self.__ccU.lastBonds
                           if ((b[self.__ccU.ccbAtomId1] == atom_id_1 and b[self.__ccU.ccbAtomId2] == atom_id_2)
                               or (b[self.__ccU.ccbAtomId1] == atom_id_2 and b[self.__ccU.ccbAtomId2] == atom_id_1))):

                    if self.__nefT.validate_comp_atom(comp_id_1, atom_id_1) and self.__nefT.validate_comp_atom(comp_id_2, atom_id_2):
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            "Found an RDC vector over multiple covalent bonds in the 'SANIsotropy' statement; "\
                            f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                        return

        for atom1, atom2 in itertools.product(self.atomSelectionSet[4],
                                              self.atomSelectionSet[5]):
            if self.__verbose:
                print(f"subtype={self.__cur_subtype} id={self.rdcRestraints} "
                      f"atom1={atom1} atom2={atom2} {dstFunc}")

    # Enter a parse tree produced by XplorMRParser#xdip_statement.
    def enterXdip_statement(self, ctx: XplorMRParser.Xdip_statementContext):
        if ctx.Rdc_potential():
            code = str(ctx.Rdc_potential()).upper()
            if code.startswith('SQUA'):
                self.potential = 'square'
            elif code.startswith('HARM'):
                self.potential = 'harmonic'

        elif ctx.Rdc_avr_methods():
            code = str(ctx.Rdc_avr_methods()).upper()
            if code.startswith('SUMD'):
                 self.average = 'sum_diff'
            elif code == 'SUM':
                self.average = 'sum'
            elif code.startswith('AVER'):
                self.average = 'average'

    # Exit a parse tree produced by XplorMRParser#xdip_statement.
    def exitXdip_statement(self, ctx: XplorMRParser.Xdip_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#xdip_assign.
    def enterXdip_assign(self, ctx: XplorMRParser.Xdip_assignContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1
        self.__cur_subtype = 'rdc'

        self.atomSelectionSet = []

    # Exit a parse tree produced by XplorMRParser#xdip_assign.
    def exitXdip_assign(self, ctx: XplorMRParser.Xdip_assignContext):
        target = float(str(ctx.Real(0)))
        delta = abs(float(str(ctx.Real(1))))

        dstFunc = {'weight': self.scale, 'average': self.average}

        if ctx.Real(3):
            target_value_1 = float(str(ctx.Real(0)))
            target_value_2 = float(str(ctx.Real(3)))
            error_grater_1 = abs(float(str(ctx.Real(1))))
            error_less_1 = abs(float(str(ctx.Real(2))))
            error_grater_2 = abs(float(str(ctx.Real(4))))
            error_less_2 = abs(float(str(ctx.Real(5))))
            lower_limit_1 = target_value_1 - error_less_1
            upper_limit_1 = target_value_1 + error_grater_1
            lower_limit_2 = target_value_2 - error_less_2
            upper_limit_2 = target_value_2 + error_grater_2

            validRange = True

            if RDC_ERROR_MIN < target_value_1 < RDC_ERROR_MAX:
                dstFunc['target_value_1'] = f"{target_value_1:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The target value(1)='{target_value_1}' must be within range {RDC_RESTRAINT_ERROR}.\n"

            if RDC_ERROR_MIN < lower_limit_1 < RDC_ERROR_MAX:
                dstFunc['lower_limit_1'] = f"{lower_limit_1:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower limit value(1)='{lower_limit_1}' must be within range {RDC_RESTRAINT_ERROR}.\n"

            if RDC_ERROR_MIN < upper_limit_1 < RDC_ERROR_MAX:
                dstFunc['upper_limit_1'] = f"{upper_limit_1:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper limit value(1)='{upper_limit_1}' must be within range {RDC_RESTRAINT_ERROR}.\n"

            if RDC_ERROR_MIN < target_value_2 < RDC_ERROR_MAX:
                dstFunc['target_value_2'] = f"{target_value_2:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The target value(2)='{target_value_2}' must be within range {RDC_RESTRAINT_ERROR}.\n"

            if RDC_ERROR_MIN < lower_limit_2 < RDC_ERROR_MAX:
                dstFunc['lower_limit_2'] = f"{lower_limit_2:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower limit value(2)='{lower_limit_2}' must be within range {RDC_RESTRAINT_ERROR}.\n"

            if RDC_ERROR_MIN < upper_limit_2 < RDC_ERROR_MAX:
                dstFunc['upper_limit_2'] = f"{upper_limit_2:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper limit value(2)='{upper_limit_2}' must be within range {RDC_RESTRAINT_ERROR}.\n"

            if not validRange:
                return

            if RDC_RANGE_MIN < target_value_1 < RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The target value(1)='{target_value_1}' should be within range {RDC_RESTRAINT_RANGE}.\n"

            if RDC_RANGE_MIN < lower_limit_1 < RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower limit value(1)='{lower_limit_1}' should be within range {RDC_RESTRAINT_RANGE}.\n"

            if RDC_RANGE_MIN < upper_limit_1 < RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper limit value(1)='{upper_limit_1}' should be within range {RDC_RESTRAINT_RANGE}.\n"

            if RDC_RANGE_MIN < target_value_2 < RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The target value(2)='{target_value_2}' should be within range {RDC_RESTRAINT_RANGE}.\n"

            if RDC_RANGE_MIN < lower_limit_2 < RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower limit value(2)='{lower_limit_2}' should be within range {RDC_RESTRAINT_RANGE}.\n"

            if RDC_RANGE_MIN < upper_limit_2 < RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper limit value(2)='{upper_limit_2}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        else:
            lower_limit = None
            upper_limit = None

            if self.potential == 'square':
                target_value = target
                lower_limit = target - delta
                upper_limit = target + delta
                if ctx.Real(2):
                    error_grater = delta
                    error_less = abs(float(str(ctx.Real(2))))
                    lower_limit = target - error_less
                    upper_limit = target + error_grater
            else:
                target_value = target

            validRange = True

            if target_value is not None:
                if RDC_ERROR_MIN < target_value < RDC_ERROR_MAX:
                    dstFunc['target_value'] = f"{target_value:.3f}"
                else:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The target value='{target_value}' must be within range {RDC_RESTRAINT_ERROR}.\n"

            if lower_limit is not None:
                if RDC_ERROR_MIN < lower_limit < RDC_ERROR_MAX:
                    dstFunc['lower_limit'] = f"{lower_limit:.3f}"
                else:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower limit value='{lower_limit}' must be within range {RDC_RESTRAINT_ERROR}.\n"

            if upper_limit is not None:
                if RDC_ERROR_MIN < upper_limit < RDC_ERROR_MAX:
                    dstFunc['upper_limit'] = f"{upper_limit:.3f}"
                else:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The upper limit value='{upper_limit}' must be within range {RDC_RESTRAINT_ERROR}.\n"

            if not validRange:
                return

            if target_value is not None:
                if RDC_RANGE_MIN < target_value < RDC_RANGE_MAX:
                    pass
                else:
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The target value='{target_value}' should be within range {RDC_RESTRAINT_RANGE}.\n"

            if lower_limit is not None:
                if RDC_RANGE_MIN < lower_limit < RDC_RANGE_MAX:
                    pass
                else:
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower limit value='{lower_limit}' should be within range {RDC_RESTRAINT_RANGE}.\n"

            if upper_limit is not None:
                if RDC_RANGE_MIN < upper_limit < RDC_RANGE_MAX:
                    pass
                else:
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The upper limit value='{upper_limit}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        if not self.areUniqueCoordAtoms('an RDC'):
            return

        chain_id_1 = self.atomSelectionSet[4][0]['chain_id']
        seq_id_1 = self.atomSelectionSet[4][0]['seq_id']
        comp_id_1 = self.atomSelectionSet[4][0]['comp_id']
        atom_id_1 = self.atomSelectionSet[4][0]['atom_id']

        chain_id_2 = self.atomSelectionSet[5][0]['chain_id']
        seq_id_2 = self.atomSelectionSet[5][0]['seq_id']
        comp_id_2 = self.atomSelectionSet[5][0]['comp_id']
        atom_id_2 = self.atomSelectionSet[5][0]['atom_id']

        if (atom_id_1[0] not in isotopeNumsOfNmrObsNucs) or (atom_id_2[0] not in isotopeNumsOfNmrObsNucs):
            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                f"Non-magnetic susceptible spin appears in 1H-1H dipolar coupling vector; "\
                f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
            return

        if chain_id_1 != chain_id_2:
            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                f"Found inter-chain 1H-1H dipolar coupling vector; "\
                f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
            return

        if abs(seq_id_1 - seq_id_2) > 1:
            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                f"Found inter-residue 1H-1H dipolar coupling vector; "\
                f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
            return

        if abs(seq_id_1 - seq_id_2) == 1:

            if self.__csStat.peptideLike(comp_id_1) and self.__csStat.peptideLike(comp_id_2) and\
               ((seq_id_1 < seq_id_2 and atom_id_1 == 'C' and atom_id_2 in ('N', 'H')) or (seq_id_1 > seq_id_2 and atom_id_1 in ('N', 'H') and atom_id_2 == 'C')):
                pass

            else:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    "Found inter-residue 1H-1H dipolar coupling vector; "\
                    f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                return

        elif atom_id_1 == atom_id_2:
            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                "Found zero 1H-1H dipolar coupling vector; "\
                f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
            return

        else:
            if atom_id_1[0] != 'H' or atom_id_2[0] != 'H':
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    "Not an 1H-1H dipolar coupling vector in the 'XDIPolar' statement; "\
                    f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                return

        for atom1, atom2 in itertools.product(self.atomSelectionSet[4],
                                              self.atomSelectionSet[5]):
            if self.__verbose:
                print(f"subtype={self.__cur_subtype} id={self.rdcRestraints} "
                      f"atom1={atom1} atom2={atom2} {dstFunc}")

    # Enter a parse tree produced by XplorMRParser#vean_statement.
    def enterVean_statement(self, ctx: XplorMRParser.Vean_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#vean_statement.
    def exitVean_statement(self, ctx: XplorMRParser.Vean_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#vean_assign.
    def enterVean_assign(self, ctx: XplorMRParser.Vean_assignContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1
        self.__cur_subtype = 'rdc'

        self.atomSelectionSet = []

    # Exit a parse tree produced by XplorMRParser#vean_assign.
    def exitVean_assign(self, ctx: XplorMRParser.Vean_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#tens_statement.
    def enterTens_statement(self, ctx: XplorMRParser.Tens_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#tens_statement.
    def exitTens_statement(self, ctx: XplorMRParser.Tens_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#tens_assign.
    def enterTens_assign(self, ctx: XplorMRParser.Tens_assignContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1
        self.__cur_subtype = 'rdc'

        self.atomSelectionSet = []

    # Exit a parse tree produced by XplorMRParser#tens_assign.
    def exitTens_assign(self, ctx: XplorMRParser.Tens_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#anis_statement.
    def enterAnis_statement(self, ctx: XplorMRParser.Anis_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#anis_statement.
    def exitAnis_statement(self, ctx: XplorMRParser.Anis_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#anis_assign.
    def enterAnis_assign(self, ctx: XplorMRParser.Anis_assignContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1
        self.__cur_subtype = 'rdc'

        self.atomSelectionSet = []

    # Exit a parse tree produced by XplorMRParser#anis_assign.
    def exitAnis_assign(self, ctx: XplorMRParser.Anis_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#planar_statement.
    def enterPlanar_statement(self, ctx: XplorMRParser.Planar_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#planar_statement.
    def exitPlanar_statement(self, ctx: XplorMRParser.Planar_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#group_statement.
    def enterGroup_statement(self, ctx: XplorMRParser.Group_statementContext):  # pylint: disable=unused-argument
        self.planeRestraints += 1
        self.__cur_subtype = 'plane'

    # Exit a parse tree produced by XplorMRParser#group_statement.
    def exitGroup_statement(self, ctx: XplorMRParser.Group_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#antidistance_statement.
    def enterAntidistance_statement(self, ctx: XplorMRParser.Antidistance_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#antidistance_statement.
    def exitAntidistance_statement(self, ctx: XplorMRParser.Antidistance_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#xadc_assign.
    def enterXadc_assign(self, ctx: XplorMRParser.Xadc_assignContext):  # pylint: disable=unused-argument
        self.adistRestraints += 1
        self.__cur_subtype = 'adist'

    # Exit a parse tree produced by XplorMRParser#xadc_assign.
    def exitXadc_assign(self, ctx: XplorMRParser.Xadc_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#coupling_statement.
    def enterCoupling_statement(self, ctx: XplorMRParser.Coupling_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#coupling_statement.
    def exitCoupling_statement(self, ctx: XplorMRParser.Coupling_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#coup_assign.
    def enterCoup_assign(self, ctx: XplorMRParser.Coup_assignContext):  # pylint: disable=unused-argument
        self.jcoupRestraints += 1
        self.__cur_subtype = 'jcoup'

    # Exit a parse tree produced by XplorMRParser#coup_assign.
    def exitCoup_assign(self, ctx: XplorMRParser.Coup_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#carbon_shift_statement.
    def enterCarbon_shift_statement(self, ctx: XplorMRParser.Carbon_shift_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#carbon_shift_statement.
    def exitCarbon_shift_statement(self, ctx: XplorMRParser.Carbon_shift_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#carbon_shift_assign.
    def enterCarbon_shift_assign(self, ctx: XplorMRParser.Carbon_shift_assignContext):  # pylint: disable=unused-argument
        self.hvycsRestraints += 1
        self.__cur_subtype = 'hvycs'

    # Exit a parse tree produced by XplorMRParser#carbon_shift_assign.
    def exitCarbon_shift_assign(self, ctx: XplorMRParser.Carbon_shift_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#carbon_shift_rcoil.
    def enterCarbon_shift_rcoil(self, ctx: XplorMRParser.Carbon_shift_rcoilContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#carbon_shift_rcoil.
    def exitCarbon_shift_rcoil(self, ctx: XplorMRParser.Carbon_shift_rcoilContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#proton_shift_statement.
    def enterProton_shift_statement(self, ctx: XplorMRParser.Proton_shift_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#proton_shift_statement.
    def exitProton_shift_statement(self, ctx: XplorMRParser.Proton_shift_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#observed.
    def enterObserved(self, ctx: XplorMRParser.ObservedContext):  # pylint: disable=unused-argument
        self.procsRestraints += 1
        self.__cur_subtype = 'procs'

    # Exit a parse tree produced by XplorMRParser#observed.
    def exitObserved(self, ctx: XplorMRParser.ObservedContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#proton_shift_rcoil.
    def enterProton_shift_rcoil(self, ctx: XplorMRParser.Proton_shift_rcoilContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#proton_shift_rcoil.
    def exitProton_shift_rcoil(self, ctx: XplorMRParser.Proton_shift_rcoilContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#proton_shift_anisotropy.
    def enterProton_shift_anisotropy(self, ctx: XplorMRParser.Proton_shift_anisotropyContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#proton_shift_anisotropy.
    def exitProton_shift_anisotropy(self, ctx: XplorMRParser.Proton_shift_anisotropyContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#proton_shift_amides.
    def enterProton_shift_amides(self, ctx: XplorMRParser.Proton_shift_amidesContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#proton_shift_amides.
    def exitProton_shift_amides(self, ctx: XplorMRParser.Proton_shift_amidesContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#proton_shift_carbons.
    def enterProton_shift_carbons(self, ctx: XplorMRParser.Proton_shift_carbonsContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#proton_shift_carbons.
    def exitProton_shift_carbons(self, ctx: XplorMRParser.Proton_shift_carbonsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#proton_shift_nitrogens.
    def enterProton_shift_nitrogens(self, ctx: XplorMRParser.Proton_shift_nitrogensContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#proton_shift_nitrogens.
    def exitProton_shift_nitrogens(self, ctx: XplorMRParser.Proton_shift_nitrogensContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#proton_shift_oxygens.
    def enterProton_shift_oxygens(self, ctx: XplorMRParser.Proton_shift_oxygensContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#proton_shift_oxygens.
    def exitProton_shift_oxygens(self, ctx: XplorMRParser.Proton_shift_oxygensContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#proton_shift_ring_atoms.
    def enterProton_shift_ring_atoms(self, ctx: XplorMRParser.Proton_shift_ring_atomsContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#proton_shift_ring_atoms.
    def exitProton_shift_ring_atoms(self, ctx: XplorMRParser.Proton_shift_ring_atomsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#proton_shift_alphas_and_amides.
    def enterProton_shift_alphas_and_amides(self, ctx: XplorMRParser.Proton_shift_alphas_and_amidesContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#proton_shift_alphas_and_amides.
    def exitProton_shift_alphas_and_amides(self, ctx: XplorMRParser.Proton_shift_alphas_and_amidesContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#ramachandran_statement.
    def enterRamachandran_statement(self, ctx: XplorMRParser.Ramachandran_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#ramachandran_statement.
    def exitRamachandran_statement(self, ctx: XplorMRParser.Ramachandran_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#rama_assign.
    def enterRama_assign(self, ctx: XplorMRParser.Rama_assignContext):  # pylint: disable=unused-argument
        self.ramaRestraints += 1
        self.__cur_subtype = 'rama'

    # Exit a parse tree produced by XplorMRParser#rama_assign.
    def exitRama_assign(self, ctx: XplorMRParser.Rama_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#collapse_statement.
    def enterCollapse_statement(self, ctx: XplorMRParser.Collapse_statementContext):  # pylint: disable=unused-argument
        self.radiRestraints += 1
        self.__cur_subtype = 'radi'

    # Exit a parse tree produced by XplorMRParser#collapse_statement.
    def exitCollapse_statement(self, ctx: XplorMRParser.Collapse_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#diffusion_statement.
    def enterDiffusion_statement(self, ctx: XplorMRParser.Diffusion_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#diffusion_statement.
    def exitDiffusion_statement(self, ctx: XplorMRParser.Diffusion_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#dani_assign.
    def enterDani_assign(self, ctx: XplorMRParser.Dani_assignContext):  # pylint: disable=unused-argument
        self.diffRestraints += 1
        self.__cur_subtype = 'diff'

    # Exit a parse tree produced by XplorMRParser#dani_assign.
    def exitDani_assign(self, ctx: XplorMRParser.Dani_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#orientation_statement.
    def enterOrientation_statement(self, ctx: XplorMRParser.Orientation_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#orientation_statement.
    def exitOrientation_statement(self, ctx: XplorMRParser.Orientation_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#orie_assign.
    def enterOrie_assign(self, ctx: XplorMRParser.Orie_assignContext):  # pylint: disable=unused-argument
        self.nbaseRestraints += 1
        self.__cur_subtype = 'nbase'

    # Exit a parse tree produced by XplorMRParser#orie_assign.
    def exitOrie_assign(self, ctx: XplorMRParser.Orie_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#csa_statement.
    def enterCsa_statement(self, ctx: XplorMRParser.Csa_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#csa_statement.
    def exitCsa_statement(self, ctx: XplorMRParser.Csa_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#csa_assign.
    def enterCsa_assign(self, ctx: XplorMRParser.Csa_assignContext):  # pylint: disable=unused-argument
        self.csaRestraints += 1
        self.__cur_subtype = 'csa'

    # Exit a parse tree produced by XplorMRParser#csa_assign.
    def exitCsa_assign(self, ctx: XplorMRParser.Csa_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#pcsa_statement.
    def enterPcsa_statement(self, ctx: XplorMRParser.Pcsa_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#pcsa_statement.
    def exitPcsa_statement(self, ctx: XplorMRParser.Pcsa_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#one_bond_coupling_statement.
    def enterOne_bond_coupling_statement(self, ctx: XplorMRParser.One_bond_coupling_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#one_bond_coupling_statement.
    def exitOne_bond_coupling_statement(self, ctx: XplorMRParser.One_bond_coupling_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#one_bond_assign.
    def enterOne_bond_assign(self, ctx: XplorMRParser.One_bond_assignContext):  # pylint: disable=unused-argument
        """
        @deprecated: This restraint has not been useful in practice, but has been preserved for historical reasons.
        """

    # Exit a parse tree produced by XplorMRParser#one_bond_assign.
    def exitOne_bond_assign(self, ctx: XplorMRParser.One_bond_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#angle_db_statement.
    def enterAngle_db_statement(self, ctx: XplorMRParser.Angle_db_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#angle_db_statement.
    def exitAngle_db_statement(self, ctx: XplorMRParser.Angle_db_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#angle_db_assign.
    def enterAngle_db_assign(self, ctx: XplorMRParser.Angle_db_assignContext):  # pylint: disable=unused-argument
        """
        @deprecated:  This term has not proved useful in practice and is only here for historical reasons.
        """

    # Exit a parse tree produced by XplorMRParser#angle_db_assign.
    def exitAngle_db_assign(self, ctx: XplorMRParser.Angle_db_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#pre_statement.
    def enterPre_statement(self, ctx: XplorMRParser.Pre_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#pre_statement.
    def exitPre_statement(self, ctx: XplorMRParser.Pre_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#pre_assign.
    def enterPre_assign(self, ctx: XplorMRParser.Pre_assignContext):  # pylint: disable=unused-argument
        self.preRestraints += 1
        self.__cur_subtype = 'pre'

    # Exit a parse tree produced by XplorMRParser#pre_assign.
    def exitPre_assign(self, ctx: XplorMRParser.Pre_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#pcs_statement.
    def enterPcs_statement(self, ctx: XplorMRParser.Pcs_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#pcs_statement.
    def exitPcs_statement(self, ctx: XplorMRParser.Pcs_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#pcs_assign.
    def enterPcs_assign(self, ctx: XplorMRParser.Pcs_assignContext):  # pylint: disable=unused-argument
        self.pcsRestraints += 1
        self.__cur_subtype = 'pcs'

    # Exit a parse tree produced by XplorMRParser#pcs_assign.
    def exitPcs_assign(self, ctx: XplorMRParser.Pcs_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#prdc_statement.
    def enterPrdc_statement(self, ctx: XplorMRParser.Prdc_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#prdc_statement.
    def exitPrdc_statement(self, ctx: XplorMRParser.Prdc_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#prdc_assign.
    def enterPrdc_assign(self, ctx: XplorMRParser.Prdc_assignContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#prdc_assign.
    def exitPrdc_assign(self, ctx: XplorMRParser.Prdc_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#porientation_statement.
    def enterPorientation_statement(self, ctx: XplorMRParser.Porientation_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#porientation_statement.
    def exitPorientation_statement(self, ctx: XplorMRParser.Porientation_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#porientation_assign.
    def enterPorientation_assign(self, ctx: XplorMRParser.Porientation_assignContext):  # pylint: disable=unused-argument
        self.pangRestraints += 1
        self.__cur_subtype = 'pang'

    # Exit a parse tree produced by XplorMRParser#porientation_assign.
    def exitPorientation_assign(self, ctx: XplorMRParser.Porientation_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#pccr_statement.
    def enterPccr_statement(self, ctx: XplorMRParser.Pccr_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#pccr_statement.
    def exitPccr_statement(self, ctx: XplorMRParser.Pccr_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#pccr_assign.
    def enterPccr_assign(self, ctx: XplorMRParser.Pccr_assignContext):  # pylint: disable=unused-argument
        self.pccrRestraints += 1
        self.__cur_subtype = 'pccr'

    # Exit a parse tree produced by XplorMRParser#pccr_assign.
    def exitPccr_assign(self, ctx: XplorMRParser.Pccr_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#hbond_statement.
    def enterHbond_statement(self, ctx: XplorMRParser.Hbond_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#hbond_statement.
    def exitHbond_statement(self, ctx: XplorMRParser.Hbond_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#hbond_assign.
    def enterHbond_assign(self, ctx: XplorMRParser.Hbond_assignContext):  # pylint: disable=unused-argument
        self.hbondRestraints += 1
        self.__cur_subtype = 'hbond'

    # Exit a parse tree produced by XplorMRParser#hbond_assign.
    def exitHbond_assign(self, ctx: XplorMRParser.Hbond_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#selection.
    def enterSelection(self, ctx: XplorMRParser.SelectionContext):  # pylint: disable=unused-argument
        if self.__debug:
            print("  " * self.depth + "enter_selection")

        if self.inVector3D:
            self.inVector3D_columnSel += 1

        elif self.depth == 0:
            self.stackSelections = []
            self.stackTerms = []
            self.factor = {}

    # Exit a parse tree produced by XplorMRParser#selection.
    def exitSelection(self, ctx: XplorMRParser.SelectionContext):  # pylint: disable=unused-argument
        if self.__debug:
            print("  " * self.depth + "exit_selection")

        atomSelection = self.stackSelections.pop() if self.stackSelections else []
        while self.stackSelections:
            _atomSelection = []
            _selection = self.stackSelections.pop()
            if _selection is not None:
                for _atom in _selection:
                    if _atom in atomSelection:
                        _atomSelection.append(_atom)
            atomSelection = _atomSelection

        if self.__debug:
            print("  " * self.depth + f"atom selection: {atomSelection}")

        if self.inVector3D:
            if self.inVector3D_columnSel == 0:
                self.inVector3D_tail = atomSelection[0]
                if len(atomSelection) > 1:
                    self.warningMessage += f"[Multiple selections] {self.__getCurrentRestraint()}"\
                        "The first atom has been selected to create a 3d-vector in the 'tail' clause.\n"
            else:
                self.inVector3D_head = atomSelection[0]
                if len(atomSelection) > 1:
                    self.warningMessage += f"[Multiple selections] {self.__getCurrentRestraint()}"\
                        "The first atom has been selected to create a 3d-vector in the 'head' clause.\n"

        else:
            self.atomSelectionSet.append(atomSelection)

    # Enter a parse tree produced by XplorMRParser#selection_expression.
    def enterSelection_expression(self, ctx: XplorMRParser.Selection_expressionContext):
        if self.__debug:
            print("  " * self.depth + f"enter_sel_expr, union: {bool(ctx.Or_op(0))}")

        if self.depth > 0 and len(self.factor) > 0:
            if 'atom_selection' not in self.factor:
                self.consumeFactor_expressions(cifCheck=False)
            if 'atom_selection' in self.factor:
                self.stackSelections.append(self.factor['atom_selection'])

        self.factor = {}

        self.depth += 1

    # Exit a parse tree produced by XplorMRParser#selection_expression.
    def exitSelection_expression(self, ctx: XplorMRParser.Selection_expressionContext):  # pylint: disable=unused-argument
        self.depth -= 1
        if self.__debug:
            print("  " * self.depth + "exit_sel_expr")

        atomSelection = []
        while self.stackTerms:
            _term = self.stackTerms.pop()
            if _term is not None:
                for _atom in _term:
                    if _atom not in atomSelection:
                        atomSelection.append(_atom)

        if len(atomSelection) > 0:
            self.stackSelections.append(atomSelection)

        self.factor = {}

    # Enter a parse tree produced by XplorMRParser#term.
    def enterTerm(self, ctx: XplorMRParser.TermContext):
        if self.__debug:
            print("  " * self.depth + f"enter_term, intersection: {bool(ctx.And_op(0))}")

        self.stackFactors = []
        self.factor = {}

        self.depth += 1

    # Exit a parse tree produced by XplorMRParser#term.
    def exitTerm(self, ctx: XplorMRParser.TermContext):  # pylint: disable=unused-argument
        self.depth -= 1
        if self.__debug:
            print("  " * self.depth + "exit_term")

        while self.stackFactors:
            _factor = self.__consumeFactor_expressions(self.stackFactors.pop(), cifCheck=False)
            self.factor = self.__intersectionFactor_expressions(self.factor, None if 'atom_selection' not in _factor else _factor['atom_selection'])

        self.stackTerms.append(self.factor['atom_selection'])

    def consumeFactor_expressions(self, clauseName='atom selection expression', cifCheck=True):
        """ Consume factor expressions as atom selection if possible.
        """

        if self.stackFactors:
            self.stackFactors.pop()

        self.factor = self.__consumeFactor_expressions(self.factor, clauseName, cifCheck)

    def __consumeFactor_expressions(self, _factor, clauseName='atom selection expression', cifCheck=True):
        """ Consume factor expressions as atom selection if possible.
        """
        if not self.__hasPolySeq:
            return _factor

        if not self.__hasCoord:
            cifCheck = False

        if ('atom_id' in _factor and _factor['atom_id'][0] is None)\
           or ('atom_selection' in _factor and len(_factor['atom_selection']) == 0):
            _factor = {'atom_selection': []}
            return _factor

        if not any(key for key in _factor if key != 'atom_selection'):
            return _factor

        if 'chain_id' not in _factor or len(_factor['chain_id']) == 0:
            _factor['chain_id'] = [ps['chain_id'] for ps in self.__polySeq]

        if 'seq_id' not in _factor and 'seq_ids' not in _factor:
            if 'comp_ids' in _factor and len(_factor['comp_ids']) > 0\
               and ('comp_id' not in _factor or len(_factor['comp_id']) == 0):
                lenCompIds = len(_factor['comp_ids'])
                _compIdSelect = set()
                for chainId in _factor['chain_id']:
                    ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chainId), None)
                    if ps is not None:
                        for realSeqId in ps['seq_id']:
                            realCompId = ps['comp_id'][ps['seq_id'].index(realSeqId)]
                            if (lenCompIds == 1 and re.match(_factor['comp_ids'][0], realCompId))\
                               or (lenCompIds == 2 and _factor['comp_ids'][0] <= realCompId <= _factor['comp_ids'][1]):
                                _compIdSelect.add(realCompId)
                _factor['comp_id'] = list(_compIdSelect)
                del _factor['comp_ids']

        if 'seq_ids' in _factor and len(_factor['seq_ids']) > 0\
           and ('seq_id' not in _factor or len(_factor['seq_id']) == 0):
            seqIds = []
            for chainId in _factor['chain_id']:
                ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chainId), None)
                if ps is not None:
                    for realSeqId in ps['seq_id']:
                        if 'comp_id' in _factor and len(_factor['comp_id']) > 0:
                            realCompId = ps['comp_id'][ps['seq_id'].index(realSeqId)]
                            if realCompId not in _factor['comp_id']:
                                continue
                        seqId = _factor['seq_ids'][0]
                        _seqId = toRegEx(seqId)
                        if re.match(_seqId, str(realSeqId)):
                            seqIds.append(realSeqId)
            _factor['seq_id'] = list(set(seqIds))
            del _factor['seq_ids']

        if 'seq_id' not in _factor or len(_factor['seq_id']) == 0:
            seqIds = []
            for chainId in _factor['chain_id']:
                ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chainId), None)
                if ps is not None:
                    for realSeqId in ps['seq_id']:
                        if 'comp_id' in _factor and len(_factor['comp_id']) > 0:
                            realCompId = ps['comp_id'][ps['seq_id'].index(realSeqId)]
                            if realCompId not in _factor['comp_id']:
                                continue
                        seqIds.append(realSeqId)
            _factor['seq_id'] = list(set(seqIds))

        if 'atom_id' not in _factor and 'atom_ids' not in _factor:
            if 'type_symbols' in _factor and len(_factor['type_symbols']) > 0\
               and ('type_symbol' not in _factor or len(_factor['type_symbol']) == 0):
                lenTypeSymbols = len(_factor['type_symbols'])
                _typeSymbolSelect = set()
                _compIdSelect = set()
                for chainId in _factor['chain_id']:
                    ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chainId), None)
                    if ps is not None:
                        _compIdSelect |= set(ps['comp_id'])
                for compId in _compIdSelect:
                    if self.__ccU.updateChemCompDict(compId):
                        for cca in self.__ccU.lastAtomList:
                            realTypeSymbol = cca[self.__ccU.ccaTypeSymbol]
                            if (lenTypeSymbols == 1 and re.match(_factor['type_symbols'][0], realTypeSymbol))\
                               or (lenTypeSymbols == 2 and _factor['type_symbols'][0] <= realTypeSymbol <= _factor['type_symbols'][1]):
                                _typeSymbolSelect.add(realTypeSymbol)
                _factor['type_symbol'] = list(_typeSymbolSelect)
                if len(_factor['type_symbol']) == 0:
                    _factor['atom_id'] = [None]
                del _factor['type_symbols']

            if 'type_symbol' in _factor:
                _atomIdSelect = set()
                _compIdSelect = set()
                for chainId in _factor['chain_id']:
                    ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chainId), None)
                    if ps is not None:
                        _compIdSelect |= set(ps['comp_id'])
                for compId in _compIdSelect:
                    if self.__ccU.updateChemCompDict(compId):
                        for cca in self.__ccU.lastAtomList:
                            if cca[self.__ccU.ccaTypeSymbol] in _factor['type_symbol']\
                               and cca[self.__ccU.ccaLeavingAtomFlag] != 'Y':
                                _atomIdSelect.add(cca[self.__ccU.ccaAtomId])
                _factor['atom_id'] = list(_atomIdSelect)
                if len(_factor['atom_id']) == 0:
                    _factor['atom_id'] = [None]

        if 'atom_ids' in _factor and len(_factor['atom_ids']) > 0\
           and ('atom_id' not in _factor or len(_factor['atom_id']) == 0):
            lenAtomIds = len(_factor['atom_ids'])
            _compIdSelect = set()
            for chainId in _factor['chain_id']:
                ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chainId), None)
                if ps is not None:
                    for realSeqId in ps['seq_id']:
                        realCompId = ps['comp_id'][ps['seq_id'].index(realSeqId)]
                        if 'comp_id' in _factor and len(_factor['comp_id']) > 0:
                            if realCompId not in _factor['comp_id']:
                                continue
                        _compIdSelect.add(realCompId)

            _atomIdSelect = set()
            for compId in _compIdSelect:
                if self.__ccU.updateChemCompDict(compId):
                    for cca in self.__ccU.lastAtomList:
                        if cca[self.__ccU.ccaLeavingAtomFlag] != 'Y':
                            realAtomId = cca[self.__ccU.ccaAtomId]
                            if (lenAtomIds == 1 and re.match(_factor['atom_ids'][0], realAtomId))\
                               or (lenAtomIds == 2 and _factor['atom_ids'][0] <= realAtomId <= _factor['atom_ids'][1]):
                                _atomIdSelect.add(realAtomId)
            _factor['atom_id'] = list(_atomIdSelect)
            if len(_factor['atom_id']) == 0:
                _factor['atom_id'] = [None]
            del _factor['atom_ids']

        if 'atom_id' not in _factor or len(_factor['atom_id']) == 0:
            _compIdSelect = set()
            for chainId in _factor['chain_id']:
                ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chainId), None)
                if ps is not None:
                    for realSeqId in ps['seq_id']:
                        realCompId = ps['comp_id'][ps['seq_id'].index(realSeqId)]
                        if 'comp_id' in _factor and len(_factor['comp_id']) > 0:
                            if realCompId not in _factor['comp_id']:
                                continue
                        _compIdSelect.add(realCompId)

            _atomIdSelect = set()
            for compId in _compIdSelect:
                if self.__ccU.updateChemCompDict(compId):
                    for cca in self.__ccU.lastAtomList:
                        if cca[self.__ccU.ccaLeavingAtomFlag] != 'Y':
                            realAtomId = cca[self.__ccU.ccaAtomId]
                            _atomIdSelect.add(realAtomId)
            _factor['atom_id'] = list(_atomIdSelect)
            if len(_factor['atom_id']) == 0:
                _factor['atom_id'] = [None]

        _atomSelection = []

        if _factor['atom_id'][0] is not None:
            for chainId in _factor['chain_id']:
                ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chainId), None)
                for seqId in _factor['seq_id']:
                    if ps is not None and seqId in ps['seq_id']:
                        compId = ps['comp_id'][ps['seq_id'].index(seqId)]
                    else:
                        compId = None

                    seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck)

                    for atomId in _factor['atom_id']:
                        if self.__cur_subtype == 'rdc' and atomId in XPLOR_RDC_PRINCIPAL_AXIS_NAMES:
                            continue
                        atomIds = self.__nefT.get_valid_star_atom(compId, atomId.upper())[0]

                        for _atomId in atomIds:
                            ccdCheck = not cifCheck

                            if cifCheck:
                                _atom = None
                                if coordAtomSite is not None:
                                    if _atomId in coordAtomSite['atom_id']:
                                        _atom = {}
                                        _atom['comp_id'] = coordAtomSite['comp_id']
                                        _atom['type_symbol'] = coordAtomSite['type_symbol'][coordAtomSite['atom_id'].index(_atomId)]
                                    elif 'alt_atom_id' in coordAtomSite and _atomId in coordAtomSite['alt_atom_id']:
                                        _atom = {}
                                        _atom['comp_id'] = coordAtomSite['comp_id']
                                        _atom['type_symbol'] = coordAtomSite['type_symbol'][coordAtomSite['alt_atom_id'].index(_atomId)]
                                        self.__authAtomId = 'auth_atom_id'
                                    elif self.__preferAuthSeq:
                                        _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck, asis=False)
                                        if _coordAtomSite is not None:
                                            if _atomId in _coordAtomSite['atom_id']:
                                                _atom = {}
                                                _atom['comp_id'] = _coordAtomSite['comp_id']
                                                _atom['type_symbol'] = _coordAtomSite['type_symbol'][_coordAtomSite['atom_id'].index(_atomId)]
                                                self.__preferAuthSeq = False
                                                self.__authSeqId = 'label_seq_id'
                                                seqKey = _seqKey
                                            elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                _atom = {}
                                                _atom['comp_id'] = _coordAtomSite['comp_id']
                                                _atom['type_symbol'] = _coordAtomSite['type_symbol'][_coordAtomSite['alt_atom_id'].index(_atomId)]
                                                self.__preferAuthSeq = False
                                                self.__authSeqId = 'label_seq_id'
                                                self.__authAtomId = 'auth_atom_id'
                                                seqKey = _seqKey

                                elif self.__preferAuthSeq:
                                    _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck, asis=False)
                                    if _coordAtomSite is not None:
                                        if _atomId in _coordAtomSite['atom_id']:
                                            _atom = {}
                                            _atom['comp_id'] = _coordAtomSite['comp_id']
                                            _atom['type_symbol'] = _coordAtomSite['type_symbol'][_coordAtomSite['atom_id'].index(_atomId)]
                                            self.__preferAuthSeq = False
                                            self.__authSeqId = 'label_seq_id'
                                            seqKey = _seqKey
                                        elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                            _atom = {}
                                            _atom['comp_id'] = _coordAtomSite['comp_id']
                                            _atom['type_symbol'] = _coordAtomSite['type_symbol'][_coordAtomSite['alt_atom_id'].index(_atomId)]
                                            self.__preferAuthSeq = False
                                            self.__authSeqId = 'label_seq_id'
                                            self.__authAtomId = 'auth_atom_id'
                                            seqKey = _seqKey

                                if _atom is not None:
                                    if ('comp_id' not in _factor or _atom['comp_id'] in _factor['comp_id'])\
                                       and ('type_symbol' not in _factor or _atom['type_symbol'] in _factor['type_symbol']):
                                        _atomSelection.append({'chain_id': chainId, 'seq_id': seqId, 'comp_id': _atom['comp_id'], 'atom_id': _atomId})
                                else:
                                    ccdCheck = True

                            if ccdCheck and compId is not None:
                                if self.__ccU.updateChemCompDict(compId) and ('comp_id' not in _factor or compId in _factor['comp_id']):
                                    cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId), None)
                                    if cca is not None and ('type_symbol' not in _factor or cca[self.__ccU.ccaTypeSymbol] in _factor['type_symbol']):
                                        _atomSelection.append({'chain_id': chainId, 'seq_id': seqId, 'comp_id': compId, 'atom_id': _atomId})
                                        if cifCheck and seqKey not in self.__coordUnobsRes:
                                            self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                                                f"{chainId}:{seqId}:{compId}:{atomId} is not present in the coordinates.\n"

        atomSelection = [dict(s) for s in set(frozenset(atom.items()) for atom in _atomSelection)]

        if 'atom_selection' not in _factor:
            _factor['atom_selection'] = atomSelection
        else:
            _atomSelection = []
            for _atom in _factor['atom_selection']:
                if _atom in atomSelection:
                    _atomSelection.append(_atom)
            _factor['atom_selection'] = _atomSelection

        if len(_factor['atom_selection']) == 0:
            if self.__cur_subtype == 'rdc' and _factor['atom_id'][0] in XPLOR_RDC_PRINCIPAL_AXIS_NAMES:
                return _factor
            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                f"The {clauseName} has no effect.\n"

        if 'chain_id' in _factor:
            del _factor['chain_id']
        if 'comp_id' in _factor:
            del _factor['comp_id']
        if 'seq_id' in _factor:
            del _factor['seq_id']
        if 'type_symbol' in _factor:
            del _factor['type_symbol']
        if 'atom_id' in _factor:
            del _factor['atom_id']

        return _factor

    def getCoordAtomSiteOf(self, chainId, seqId, cifCheck=True, asis=True):
        seqKey = (chainId, seqId)
        coordAtomSite = None
        if cifCheck:
            preferAuthSeq = self.__preferAuthSeq if asis else not self.__preferAuthSeq
            if preferAuthSeq:
                if seqKey in self.__coordAtomSite:
                    coordAtomSite = self.__coordAtomSite[seqKey]
            else:
                if seqKey in self.__labelToAuthSeq:
                    seqKey = self.__labelToAuthSeq[seqKey]
                    if seqKey in self.__coordAtomSite:
                        coordAtomSite = self.__coordAtomSite[seqKey]
        return seqKey, coordAtomSite

    def intersectionFactor_expressions(self, atomSelection=None):
        self.consumeFactor_expressions(cifCheck=False)

        self.factor = self.__intersectionFactor_expressions(self.factor, atomSelection)

    def __intersectionFactor_expressions(self, _factor, atomSelection=None):  # pylint: disable=no-self-use
        if 'atom_selection' not in _factor:
            _factor['atom_selection'] = atomSelection
            return _factor

        if atomSelection is None or len(atomSelection) == 0:
            _factor['atom_selection'] = []

        _atomSelection = []
        for _atom in _factor['atom_selection']:
            if _atom in atomSelection:
                _atomSelection.append(_atom)

        _factor['atom_selection'] = _atomSelection

        return _factor

    # Enter a parse tree produced by XplorMRParser#factor.
    def enterFactor(self, ctx: XplorMRParser.FactorContext):
        if self.__debug:
            print("  " * self.depth + f"enter_factor, concatenation: {bool(ctx.factor())}")

        if ctx.Point():
            self.inVector3D = True
            self.inVector3D_columnSel = -1
            self.inVector3D_tail = None
            self.inVector3D_head = None
            self.vector3D = None

        self.depth += 1

    # Exit a parse tree produced by XplorMRParser#factor.
    def exitFactor(self, ctx: XplorMRParser.FactorContext):
        self.depth -= 1
        if self.__debug:
            print("  " * self.depth + "exit_factor")

        # concatenation
        if ctx.factor() and self.stackSelections:
            self.stackFactors.pop()
            self.factor = {'atom_selection': self.stackSelections.pop()}

        if ctx.All() or ctx.Known():
            clauseName = 'all' if ctx.All() else 'known'
            if self.__debug:
                print("  " * self.depth + f"--> {clauseName}")
            if not self.__hasCoord:
                return
            try:

                atomSelection =\
                    self.__cR.getDictListWithFilter('atom_site',
                                                    [{'name': 'auth_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                                     {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                                     {'name': 'label_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                     {'name': 'label_atom_id', 'type': 'str', 'alt_name': 'atom_id'}
                                                     ],
                                                    [{'name': self.__modelNumName, 'type': 'int',
                                                      'value': REPRESENTATIVE_MODEL_ID}
                                                     ])

                self.intersectionFactor_expressions(atomSelection)

                if len(self.factor['atom_selection']) == 0:
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"The {clauseName!r} clause has no effect.\n"

                else:
                    if 'chain_id' in self.factor:
                        del self.factor['chain_id']
                    if 'comp_id' in self.factor:
                        del self.factor['comp_id']
                    if 'seq_id' in self.factor:
                        del self.factor['seq_id']
                    if 'type_symbol' in self.factor:
                        del self.factor['type_symbol']
                    if 'atom_id' in self.factor:
                        del self.factor['atom_id']
                    if 'comp_ids' in self.factor:
                        del self.factor['comp_ids']
                    if 'seq_ids' in self.factor:
                        del self.factor['seq_ids']
                    if 'type_symbols' in self.factor:
                        del self.factor['type_symbols']
                    if 'atom_ids' in self.factor:
                        del self.factor['atom_ids']

            except Exception as e:
                if self.__verbose:
                    self.__lfh.write(f"+XplorMRParserListener.exitFactor() ++ Error  - {str(e)}\n")

        elif ctx.Around() or ctx.Saround():
            clauseName = 'around' if ctx.Around() else 'saround'
            if self.__debug:
                print("  " * self.depth + f"--> {clauseName}")
            if not self.__hasCoord:
                return
            around = float(str(ctx.Real(0)))
            _atomSelection = []

            self.consumeFactor_expressions(f"atom selection expression before the {clauseName!r} clause")

            if 'atom_selection' in self.factor:

                for _atom in self.factor['atom_selection']:

                    try:

                        _origin =\
                            self.__cR.getDictListWithFilter('atom_site',
                                                            [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                             {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                             {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                                                             ],
                                                            [{'name': self.__authAsymId, 'type': 'str', 'value': _atom['chain_id']},
                                                             {'name': self.__authSeqId, 'type': 'int', 'value': _atom['seq_id']},
                                                             {'name': self.__authAtomId, 'type': 'str', 'value': _atom['atom_id']},
                                                             {'name': self.__modelNumName, 'type': 'int',
                                                              'value': REPRESENTATIVE_MODEL_ID}
                                                             ])

                        if len(_origin) != 1:
                            continue

                        origin = toNpArray(_origin[0])

                        _neighbor =\
                            self.__cR.getDictListWithFilter('atom_site',
                                                            [{'name': 'auth_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                                             {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                                             {'name': 'label_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                             {'name': 'label_atom_id', 'type': 'str', 'alt_name': 'atom_id'},
                                                             {'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                             {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                             {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                                                             ],
                                                            [{'name': 'Cartn_x', 'type': 'range-float',
                                                              'range': {'min_exclusive': (origin[0] - around),
                                                                        'max_exclusive': (origin[0] + around)}},
                                                             {'name': 'Cartn_y', 'type': 'range-float',
                                                              'range': {'min_exclusive': (origin[1] - around),
                                                                        'max_exclusive': (origin[1] + around)}},
                                                             {'name': 'Cartn_z', 'type': 'range-float',
                                                              'range': {'min_exclusive': (origin[2] - around),
                                                                        'max_exclusive': (origin[2] + around)}},
                                                             {'name': self.__modelNumName, 'type': 'int',
                                                              'value': REPRESENTATIVE_MODEL_ID}
                                                             ])

                        if len(_neighbor) == 0:
                            continue

                        neighbor = [atom for atom in _neighbor if np.linalg.norm(toNpArray(atom) - origin) < around]

                        for atom in neighbor:
                            del atom['x']
                            del atom['y']
                            del atom['z']
                            _atomSelection.append(atom)

                    except Exception as e:
                        if self.__verbose:
                            self.__lfh.write(f"+XplorMRParserListener.exitFactor() ++ Error  - {str(e)}\n")

                if ctx.Saround():
                    identity = np.identity(3, dtype=float)
                    zero = np.zeros(3, dtype=float)

                    oper_list = self.__cR.getDictList('pdbx_struct_oper_list')
                    if len(oper_list) > 0:
                        for oper in oper_list:
                            matrix = np.array([[float(oper['matrix[1][1]']), float(oper['matrix[1][2]']), float(oper['matrix[1][3]'])],
                                               [float(oper['matrix[2][1]']), float(oper['matrix[2][2]']), float(oper['matrix[2][3]'])],
                                               [float(oper['matrix[3][1]']), float(oper['matrix[3][2]']), float(oper['matrix[3][3]'])]], dtype=float)
                            vector = np.array([float(oper['vector[1]']), float(oper['vector[2]']), float(oper['vector[3]'])], dtype=float)

                            if np.array_equal(matrix, identity) and np.array_equal(vector, zero):
                                continue

                            inv_matrix = np.linalg.inv(matrix)

                            for _atom in self.factor['atom_selection']:

                                try:

                                    _origin =\
                                        self.__cR.getDictListWithFilter('atom_site',
                                                                        [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                                         {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                                         {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                                                                         ],
                                                                        [{'name': self.__authAsymId, 'type': 'str', 'value': _atom['chain_id']},
                                                                         {'name': self.__authSeqId, 'type': 'int', 'value': _atom['seq_id']},
                                                                         {'name': self.__authAtomId, 'type': 'str', 'value': _atom['atom_id']},
                                                                         {'name': self.__modelNumName, 'type': 'int',
                                                                          'value': REPRESENTATIVE_MODEL_ID}
                                                                         ])

                                    if len(_origin) != 1:
                                        continue

                                    origin = np.dot(inv_matrix, np.subtract(toNpArray(_origin[0]), vector))

                                    _neighbor =\
                                        self.__cR.getDictListWithFilter('atom_site',
                                                                        [{'name': 'auth_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                                                         {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                                                         {'name': 'label_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                                         {'name': 'label_atom_id', 'type': 'str', 'alt_name': 'atom_id'},
                                                                         {'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                                         {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                                         {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                                                                         ],
                                                                        [{'name': 'Cartn_x', 'type': 'range-float',
                                                                          'range': {'min_exclusive': (origin[0] - around),
                                                                                    'max_exclusive': (origin[0] + around)}},
                                                                         {'name': 'Cartn_y', 'type': 'range-float',
                                                                          'range': {'min_exclusive': (origin[1] - around),
                                                                                    'max_exclusive': (origin[1] + around)}},
                                                                         {'name': 'Cartn_z', 'type': 'range-float',
                                                                          'range': {'min_exclusive': (origin[2] - around),
                                                                                    'max_exclusive': (origin[2] + around)}},
                                                                         {'name': self.__modelNumName, 'type': 'int',
                                                                          'value': REPRESENTATIVE_MODEL_ID}
                                                                         ])

                                    if len(_neighbor) == 0:
                                        continue

                                    neighbor = [atom for atom in _neighbor if np.linalg.norm(toNpArray(atom) - origin) < around]

                                    for atom in neighbor:
                                        del atom['x']
                                        del atom['y']
                                        del atom['z']
                                        _atomSelection.append(atom)

                                except Exception as e:
                                    if self.__verbose:
                                        self.__lfh.write(f"+XplorMRParserListener.exitFactor() ++ Error  - {str(e)}\n")

                if len(self.factor['atom_selection']) > 0:
                    self.factor['atom_selection'] = [dict(s) for s in set(frozenset(atom.items()) for atom in _atomSelection)]

                    if len(self.factor['atom_selection']) == 0:
                        self.factor['atom_id'] = [None]
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            f"The {clauseName!r} clause has no effect.\n"

        elif ctx.Atom():
            if self.__debug:
                print("  " * self.depth + "--> atom")
            if not self.__hasPolySeq:
                return
            simpleNameIndex = simpleNamesIndex = 0  # these indices are necessary to deal with mixing case of 'Simple_name' and 'Simple_names'
            if ctx.Simple_name(0):
                chainId = str(ctx.Simple_name(0))
                self.factor['chain_id'] = [ps['chain_id'] for ps in self.__polySeq
                                           if ps['chain_id'] == chainId]
                if len(self.factor['chain_id']) > 0:
                    simpleNameIndex += 1

            if simpleNameIndex == 0 and ctx.Simple_names(0):
                chainId = str(ctx.Simple_names(0))
                _chainId = toRegEx(chainId)
                self.factor['chain_id'] = [ps['chain_id'] for ps in self.__polySeq
                                           if re.match(_chainId, ps['chain_id'])]
                simpleNamesIndex += 1

            if len(self.factor['chain_id']) == 0:
                self.factor['atom_id'] = [None]
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Couldn't specify segment name "\
                    f"'{chainId}' the coordinates.\n"  # do not use 'chainId!r' expression, '%' code throws ValueError

            if ctx.Integer(0):
                self.factor['seq_id'] = [int(str(ctx.Integer(0)))]

            if ctx.Integers():
                seqId = str(ctx.Integers())
                _seqId = toRegEx(seqId)
                _seqIdSelect = set()
                for chainId in self.factor['chain_id']:
                    ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chainId), None)
                    if ps is not None:
                        for realSeqId in ps['seq_id']:
                            if re.match(_seqId, str(realSeqId)):
                                _seqIdSelect.add(realSeqId)
                self.factor['seq_id'] = list(_seqIdSelect)

            _atomIdSelect = set()
            if ctx.Simple_name(simpleNameIndex):
                atomId = str(ctx.Simple_name(simpleNameIndex))
                for chainId in self.factor['chain_id']:
                    ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chainId), None)
                    if ps is None:
                        continue
                    for seqId in self.factor['seq_id']:
                        if seqId in ps['seq_id']:
                            compId = ps['comp_id'][ps['seq_id'].index(seqId)]
                            if self.__ccU.updateChemCompDict(compId):
                                if any(cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == atomId):
                                    _atomIdSelect.add(atomId)

            elif ctx.Simple_names(simpleNamesIndex):
                atomId = str(ctx.Simple_names(simpleNamesIndex))
                _atomId = toRegEx(atomId)
                for chainId in self.factor['chain_id']:
                    ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chainId), None)
                    if ps is None:
                        continue
                    for seqId in self.factor['seq_id']:
                        if seqId in ps['seq_id']:
                            compId = ps['comp_id'][ps['seq_id'].index(seqId)]
                            if self.__ccU.updateChemCompDict(compId):
                                for cca in self.__ccU.lastAtomList:
                                    if cca[self.__ccU.ccaLeavingAtomFlag] != 'Y':
                                        realAtomId = cca[self.__ccU.ccaAtomId]
                                        if re.match(_atomId, realAtomId):
                                            _atomIdSelect.add(realAtomId)

            self.factor['atom_id'] = list(_atomIdSelect)

            self.consumeFactor_expressions("'atom' clause", False)

        elif ctx.Attribute():
            if self.__debug:
                print("  " * self.depth + "--> attribute")
            if not self.__hasCoord:
                return
            absolute = bool(ctx.Abs())
            _attr_prop = str(ctx.Attr_properties())
            attr_prop = _attr_prop.lower()
            opCode = str(ctx.Comparison_ops())
            attr_value = float(str(ctx.Real(0)))

            validProp = True

            if attr_prop == 'b':
                valueType = {'name': 'B_iso_or_equiv'}
                if opCode == '=':
                    valueType['type'] = 'float' if not absolute else 'abs-float'
                    valueType['value'] = attr_value
                elif opCode == '<':
                    valueType['type'] = 'range-float' if not absolute else 'range-abs-float'
                    valueType['range'] = {'max_exclusive': attr_value}
                elif opCode == '>':
                    valueType['type'] = 'range-float' if not absolute else 'range-abs-float'
                    valueType['range'] = {'min_exclusive': attr_value}
                elif opCode == '<=':
                    valueType['type'] = 'range-float' if not absolute else 'range-abs-float'
                    valueType['range'] = {'max_inclusive': attr_value}
                elif opCode == '>=':
                    valueType['type'] = 'range-float' if not absolute else 'range-abs-float'
                    valueType['range'] = {'min_inclusive': attr_value}
                elif opCode == '#':
                    valueType['type'] = 'range-float' if not absolute else 'range-abs-float'
                    valueType['range'] = {'not_equal_to': attr_value}
                atomSelection =\
                    self.__cR.getDictListWithFilter('atom_site',
                                                    [{'name': 'auth_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                                     {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                                     {'name': 'label_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                     {'name': 'label_atom_id', 'type': 'str', 'alt_name': 'atom_id'}
                                                     ],
                                                    [valueType,
                                                     {'name': self.__modelNumName, 'type': 'int',
                                                      'value': REPRESENTATIVE_MODEL_ID}
                                                     ])

                self.intersectionFactor_expressions(atomSelection)

            elif attr_prop.startswith('bcom')\
                    or attr_prop.startswith('qcom')\
                    or attr_prop.startswith('xcom')\
                    or attr_prop.startswith('ycom')\
                    or attr_prop.startswith('zcom'):  # BCOMP, QCOMP, XCOMP, YCOMP, ZCOM`
                self.factor['atom_id'] = [None]
                self.warningMessage += f"[Unavailable resource] {self.__getCurrentRestraint()}"\
                    f"The attribute property {_attr_prop!r} "\
                    "requires a comparison coordinate set.\n"
                validProp = False

            elif attr_prop.startswith('char'):  # CAHRGE
                valueType = {'name': 'pdbx_formal_charge'}
                if opCode == '=':
                    valueType['type'] = 'int' if not absolute else 'abs-int'
                    valueType['value'] = attr_value
                elif opCode == '<':
                    valueType['type'] = 'range-int' if not absolute else 'range-abs-int'
                    valueType['range'] = {'max_exclusive': attr_value}
                elif opCode == '>':
                    valueType['type'] = 'range-int' if not absolute else 'range-abs-int'
                    valueType['range'] = {'min_exclusive': attr_value}
                elif opCode == '<=':
                    valueType['type'] = 'range-int' if not absolute else 'range-abs-int'
                    valueType['range'] = {'max_inclusive': attr_value}
                elif opCode == '>=':
                    valueType['type'] = 'range-int' if not absolute else 'range-abs-int'
                    valueType['range'] = {'min_inclusive': attr_value}
                elif opCode == '#':
                    valueType['type'] = 'range-int' if not absolute else 'range-abs-int'
                    valueType['range'] = {'not_equal_to': attr_value}
                atomSelection =\
                    self.__cR.getDictListWithFilter('atom_site',
                                                    [{'name': 'auth_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                                     {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                                     {'name': 'label_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                     {'name': 'label_atom_id', 'type': 'str', 'alt_name': 'atom_id'}
                                                     ],
                                                    [valueType,
                                                     {'name': self.__modelNumName, 'type': 'int',
                                                      'value': REPRESENTATIVE_MODEL_ID}
                                                     ])

                self.intersectionFactor_expressions(atomSelection)

            elif attr_prop in ('dx', 'dy', 'dz', 'harm'):
                self.factor['atom_id'] = [None]
                self.warningMessage += f"[Unavailable resource] {self.__getCurrentRestraint()}"\
                    f"The attribute property {_attr_prop!r} "\
                    "related to atomic force of each atom is not possessed in the static coordinate file.\n"
                validProp = False

            elif attr_prop.startswith('fbet'):  # FBETA
                self.factor['atom_id'] = [None]
                self.warningMessage += f"[Unavailable resource] {self.__getCurrentRestraint()}"\
                    f"The attribute property {_attr_prop!r} "\
                    "related to the Langevin dynamics (nonzero friction coefficient) is not possessed in the static coordinate file.\n"
                validProp = False

            elif attr_prop == 'mass':
                _typeSymbolSelect = set()
                atomTypes = self.__cR.getDictList('atom_type')
                if len(atomTypes) > 0 and 'symbol' in atomTypes[0]:
                    for atomType in atomTypes:
                        typeSymbol = atomType['symbol']
                        atomicNumber = int_atom(typeSymbol)
                        atomicWeight = ELEMENT_WEIGHTS[atomicNumber]

                        if (opCode == '=' and atomicWeight == attr_value)\
                           or (opCode == '<' and atomicWeight < attr_value)\
                           or (opCode == '>' and atomicWeight > attr_value)\
                           or (opCode == '<=' and atomicWeight <= attr_value)\
                           or (opCode == '>=' and atomicWeight >= attr_value)\
                           or (opCode == '#' and atomicWeight != attr_value):
                            _typeSymbolSelect.add(typeSymbol)

                atomSelection =\
                    self.__cR.getDictListWithFilter('atom_site',
                                                    [{'name': 'auth_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                                     {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                                     {'name': 'label_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                     {'name': 'label_atom_id', 'type': 'str', 'alt_name': 'atom_id'}
                                                     ],
                                                    [{'name': 'type_symbol', 'type': 'enum', 'enum': _typeSymbolSelect},
                                                     {'name': self.__modelNumName, 'type': 'int',
                                                      'value': REPRESENTATIVE_MODEL_ID}
                                                     ])

                self.intersectionFactor_expressions(atomSelection)

            elif attr_prop == 'q':
                valueType = {'name': 'occupancy'}
                if opCode == '=':
                    valueType['type'] = 'float' if not absolute else 'abs-float'
                    valueType['value'] = attr_value
                elif opCode == '<':
                    valueType['type'] = 'range-float' if not absolute else 'range-abs-float'
                    valueType['range'] = {'max_exclusive': attr_value}
                elif opCode == '>':
                    valueType['type'] = 'range-float' if not absolute else 'range-abs-float'
                    valueType['range'] = {'min_exclusive': attr_value}
                elif opCode == '<=':
                    valueType['type'] = 'range-float' if not absolute else 'range-abs-float'
                    valueType['range'] = {'max_inclusive': attr_value}
                elif opCode == '>=':
                    valueType['type'] = 'range-float' if not absolute else 'range-abs-float'
                    valueType['range'] = {'min_inclusive': attr_value}
                elif opCode == '#':
                    valueType['type'] = 'range-float' if not absolute else 'range-abs-float'
                    valueType['range'] = {'not_equal_to': attr_value}
                atomSelection =\
                    self.__cR.getDictListWithFilter('atom_site',
                                                    [{'name': 'auth_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                                     {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                                     {'name': 'label_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                     {'name': 'label_atom_id', 'type': 'str', 'alt_name': 'atom_id'}
                                                     ],
                                                    [valueType,
                                                     {'name': self.__modelNumName, 'type': 'int',
                                                      'value': REPRESENTATIVE_MODEL_ID}
                                                     ])

                self.intersectionFactor_expressions(atomSelection)

            elif attr_prop in ('refx', 'refy', 'refz', 'rmsd'):
                self.factor['atom_id'] = [None]
                self.warningMessage += f"[Unavailable resource] {self.__getCurrentRestraint()}"\
                    f"The attribute property {_attr_prop!r} "\
                    "requires a reference coordinate set.\n"
                validProp = False

            elif attr_prop == ('vx', 'vy', 'vz'):
                self.factor['atom_id'] = [None]
                self.warningMessage += f"[Unavailable resource] {self.__getCurrentRestraint()}"\
                    f"The attribute property {_attr_prop!r} "\
                    "related to current velocities of each atom is not possessed in the static coordinate file.\n"
                validProp = False

            elif attr_prop in ('x', 'y', 'z'):
                valueType = {'name': f"Cartn_{attr_prop}"}
                if opCode == '=':
                    valueType['type'] = 'float' if not absolute else 'abs-float'
                    valueType['value'] = attr_value
                elif opCode == '<':
                    valueType['type'] = 'range-float' if not absolute else 'range-abs-float'
                    valueType['range'] = {'max_exclusive': attr_value}
                elif opCode == '>':
                    valueType['type'] = 'range-float' if not absolute else 'range-abs-float'
                    valueType['range'] = {'min_exclusive': attr_value}
                elif opCode == '<=':
                    valueType['type'] = 'range-float' if not absolute else 'range-abs-float'
                    valueType['range'] = {'max_inclusive': attr_value}
                elif opCode == '>=':
                    valueType['type'] = 'range-float' if not absolute else 'range-abs-float'
                    valueType['range'] = {'min_inclusive': attr_value}
                elif opCode == '#':
                    valueType['type'] = 'range-float' if not absolute else 'range-abs-float'
                    valueType['range'] = {'not_equal_to': attr_value}
                atomSelection =\
                    self.__cR.getDictListWithFilter('atom_site',
                                                    [{'name': 'auth_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                                     {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                                     {'name': 'label_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                     {'name': 'label_atom_id', 'type': 'str', 'alt_name': 'atom_id'}
                                                     ],
                                                    [valueType,
                                                     {'name': self.__modelNumName, 'type': 'int',
                                                      'value': REPRESENTATIVE_MODEL_ID}
                                                     ])

                self.intersectionFactor_expressions(atomSelection)

            if validProp and len(self.factor['atom_selection']) == 0:
                self.factor['atom_id'] = [None]
                _absolute = ' abs' if absolute else ''
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The 'attribute' clause ('{_attr_prop}{_absolute} {opCode} {attr_value}') has no effect.\n"

        elif ctx.BondedTo():
            if self.__debug:
                print("  " * self.depth + "--> bondedto")
            if not self.__hasCoord:
                return
            if 'atom_selection' in self.factor and len(self.factor['atom_selection']) > 0:
                _atomSelection = []

                for _atom in self.factor['atom_selection']:
                    chainId = _atom['chain_id']
                    compId = _atom['comp_id']
                    seqId = _atom['seq_id']
                    atomId = _atom['atom_id']

                    _, coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId)

                    # intra
                    if self.__ccU.updateChemCompDict(compId):
                        leavingAtomIds = [cca[self.__ccU.ccaAtomId] for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaLeavingAtomFlag] == 'Y']

                        _atomIdSelect = set()
                        for ccb in self.__ccU.lastBonds:
                            if ccb[self.__ccU.ccbAtomId1] == atomId:
                                _atomIdSelect.add(ccb[self.__ccU.ccbAtomId2])
                            elif ccb[self.__ccU.ccbAtomId2] == atomId:
                                _atomIdSelect.add(ccb[self.__ccU.ccbAtomId1])

                        hasLeaavindAtomId = False

                        for _atomId in _atomIdSelect:

                            if _atomId in leavingAtomIds:
                                hasLeaavindAtomId = True
                                continue

                            _atom = None
                            if coordAtomSite is not None:
                                if _atomId in coordAtomSite['atom_id']:
                                    _atom = {}
                                    _atom['comp_id'] = coordAtomSite['comp_id']
                                elif 'alt_atom_id' in coordAtomSite and _atomId in coordAtomSite['alt_atom_id']:
                                    _atom = {}
                                    _atom['comp_id'] = coordAtomSite['comp_id']

                            if _atom is not None and _atom['comp_id'] == compId:
                                _atomSelection.append({'chain_id': chainId, 'seq_id': seqId, 'comp_id': compId, 'atom_id': _atomId})

                            else:
                                ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chainId), None)
                                if ps is not None and seqId in ps['seq_id'] and ps['comp_id'][ps['seq_id'].index(seqId)] == compId:
                                    if any(cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId):
                                        _atomSelection.append({'chain_id': chainId, 'seq_id': seqId, 'comp_id': compId, 'atom_id': _atomId})

                        # sequential
                        if hasLeaavindAtomId:
                            _origin =\
                                self.__cR.getDictListWithFilter('atom_site',
                                                                [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                                 {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                                 {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                                                                 ],
                                                                [{'name': self.__authAsymId, 'type': 'str', 'value': chainId},
                                                                 {'name': self.__authSeqId, 'type': 'int', 'value': seqId},
                                                                 {'name': self.__authAtomId, 'type': 'str', 'value': atomId},
                                                                 {'name': self.__modelNumName, 'type': 'int',
                                                                  'value': REPRESENTATIVE_MODEL_ID}
                                                                 ])

                            if len(_origin) == 1:
                                origin = toNpArray(_origin[0])

                                ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chainId), None)
                                if ps is not None:
                                    for _seqId in [seqId - 1, seqId + 1]:
                                        if _seqId in ps['seq_id']:
                                            _compId = ps['comp_id'][ps['seq_id'].index(_seqId)]
                                            if self.__ccU.updateChemCompDict(_compId):
                                                leavingAtomIds = [cca[self.__ccU.ccaAtomId] for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaLeavingAtomFlag] == 'Y']

                                                _atomIdSelect = set()
                                                for ccb in self.__ccU.lastBonds:
                                                    if ccb[self.__ccU.ccbAtomId1] in leavingAtomIds:
                                                        _atomId = ccb[self.__ccU.ccbAtomId2]
                                                        if _atomId not in leavingAtomIds:
                                                            _atomIdSelect.add(_atomId)
                                                    if ccb[self.__ccU.ccbAtomId2] in leavingAtomIds:
                                                        _atomId = ccb[self.__ccU.ccbAtomId1]
                                                        if _atomId not in leavingAtomIds:
                                                            _atomIdSelect.add(_atomId)

                                                for _atomId in _atomIdSelect:
                                                    _neighbor =\
                                                        self.__cR.getDictListWithFilter('atom_site',
                                                                                        [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                                                         {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                                                         {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                                                                                         ],
                                                                                        [{'name': self.__authAsymId, 'type': 'str', 'value': chainId},
                                                                                         {'name': self.__authSeqId, 'type': 'int', 'value': _seqId},
                                                                                         {'name': self.__authAtomId, 'type': 'str', 'value': _atomId},
                                                                                         {'name': self.__modelNumName, 'type': 'int',
                                                                                          'value': REPRESENTATIVE_MODEL_ID}
                                                                                         ])

                                                    if len(_neighbor) != 1:
                                                        continue

                                                    if np.linalg.norm(toNpArray(_neighbor[0]) - origin) < 2.5:
                                                        _atomSelection.append({'chain_id': chainId, 'seq_id': _seqId, 'comp_id': _compId, 'atom_id': _atomId})

                    # struct_conn category
                    _atom = self.__cR.getDictListWithFilter('struct_conn',
                                                            [{'name': 'ptnr1_auth_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                                             {'name': 'ptnr1_auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                                             {'name': 'ptnr1_label_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                             {'name': 'ptnr1_label_atom_id', 'type': 'str', 'alt_name': 'atom_id'}
                                                             ],
                                                            [{'name': 'ptnr2_auth_asym_id', 'type': 'str', 'value': chainId},
                                                             {'name': 'ptnr2_auth_seq_id', 'type': 'int', 'value': seqId},
                                                             {'name': 'ptnr2_label_atom_id', 'type': 'str', 'value': atomId},
                                                             {'name': self.__modelNumName, 'type': 'int',
                                                              'value': REPRESENTATIVE_MODEL_ID}
                                                             ])

                    if len(_atom) == 1:
                        _atomSelection.append(_atom[0])

                    _atom = self.__cR.getDictListWithFilter('struct_conn',
                                                            [{'name': 'ptnr2_auth_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                                             {'name': 'ptnr2_auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                                             {'name': 'ptnr2_label_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                             {'name': 'ptnr2_label_atom_id', 'type': 'str', 'alt_name': 'atom_id'}
                                                             ],
                                                            [{'name': 'ptnr1_auth_asym_id', 'type': 'str', 'value': chainId},
                                                             {'name': 'ptnr1_auth_seq_id', 'type': 'int', 'value': seqId},
                                                             {'name': 'ptnr1_label_atom_id', 'type': 'str', 'value': atomId},
                                                             {'name': self.__modelNumName, 'type': 'int',
                                                              'value': REPRESENTATIVE_MODEL_ID}
                                                             ])

                    if len(_atom) == 1:
                        _atomSelection.append(_atom[0])

                self.factor['atom_selection'] = [dict(s) for s in set(frozenset(atom.items()) for atom in _atomSelection)]

                if len(self.factor['atom_selection']) == 0:
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        "The 'bondedto' clause has no effect.\n"

            else:
                self.factor['atom_id'] = [None]
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    "The 'bondedto' clause has no effect because no atom is selected.\n"

        elif ctx.ByGroup():
            if self.__debug:
                print("  " * self.depth + "--> bygroup")
            if not self.__hasCoord:
                return
            if 'atom_selection' in self.factor and len(self.factor['atom_selection']) > 0:
                _atomSelection = []

                for _atom in self.factor['atom_selection']:
                    chainId = _atom['chain_id']
                    compId = _atom['comp_id']
                    seqId = _atom['seq_id']
                    atomId = _atom['atom_id']

                    _atomSelection.append(_atom)  # self atom

                    if self.__ccU.updateChemCompDict(compId):
                        _bondedAtomIdSelect = set()
                        for ccb in self.__ccU.lastBonds:
                            if ccb[self.__ccU.ccbAtomId1] == atomId:
                                _bondedAtomIdSelect.add(ccb[self.__ccU.ccbAtomId2])
                            elif ccb[self.__ccU.ccbAtomId2] == atomId:
                                _bondedAtomIdSelect.add(ccb[self.__ccU.ccbAtomId1])

                        _nonBondedAtomIdSelect = set()
                        for _atomId in _bondedAtomIdSelect:
                            for ccb in self.__ccU.lastBonds:
                                if ccb[self.__ccU.ccbAtomId1] == _atomId:
                                    _nonBondedAtomIdSelect.add(ccb[self.__ccU.ccbAtomId2])
                                elif ccb[self.__ccU.ccbAtomId2] == _atomId:
                                    _nonBondedAtomIdSelect.add(ccb[self.__ccU.ccbAtomId1])

                        if atomId in _nonBondedAtomIdSelect:
                            _nonBondedAtomIdSelect.remove(atomId)

                        for _atomId in _bondedAtomIdSelect:
                            if _atomId in _nonBondedAtomIdSelect:
                                _nonBondedAtomIdSelect.remove(_atomId)

                        if len(_nonBondedAtomIdSelect) > 0:
                            _origin =\
                                self.__cR.getDictListWithFilter('atom_site',
                                                                [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                                 {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                                 {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                                                                 ],
                                                                [{'name': self.__authAsymId, 'type': 'str', 'value': chainId},
                                                                 {'name': self.__authSeqId, 'type': 'int', 'value': seqId},
                                                                 {'name': self.__authAtomId, 'type': 'str', 'value': atomId},
                                                                 {'name': self.__modelNumName, 'type': 'int',
                                                                  'value': REPRESENTATIVE_MODEL_ID}
                                                                 ])

                            if len(_origin) == 1:
                                origin = toNpArray(_origin[0])

                                for _atomId in _nonBondedAtomIdSelect:
                                    _neighbor =\
                                        self.__cR.getDictListWithFilter('atom_site',
                                                                        [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                                         {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                                         {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                                                                         ],
                                                                        [{'name': self.__authAsymId, 'type': 'str', 'value': chainId},
                                                                         {'name': self.__authSeqId, 'type': 'int', 'value': seqId},
                                                                         {'name': self.__authAtomId, 'type': 'str', 'value': _atomId},
                                                                         {'name': self.__modelNumName, 'type': 'int',
                                                                          'value': REPRESENTATIVE_MODEL_ID}
                                                                         ])

                                    if len(_neighbor) != 1:
                                        continue

                                    if np.linalg.norm(toNpArray(_neighbor[0]) - origin) < 2.0:
                                        _atomSelection.append({'chain_id': chainId, 'seq_id': seqId, 'comp_id': compId, 'atom_id': _atomId})

                            else:
                                cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == atomId), None)
                                if cca is not None:
                                    _origin = {'x': float(cca[self.__ccU.ccaCartnX]), 'y': float(cca[self.__ccU.ccaCartnY]), 'z': float(cca[self.__ccU.ccaCartnZ])}
                                    origin = toNpArray(_origin)

                                    for _atomId in _nonBondedAtomIdSelect:
                                        _cca = next((_cca for _cca in self.__ccU.lastAtomList if _cca[self.__ccU.ccaAtomId] == _atomId), None)
                                        if _cca is not None:
                                            _neighbor = {'x': float(_cca[self.__ccU.ccaCartnX]), 'y': float(_cca[self.__ccU.ccaCartnY]), 'z': float(_cca[self.__ccU.ccaCartnZ])}

                                            if np.linalg.norm(toNpArray(_neighbor) - origin) < 2.0:
                                                _atomSelection.append({'chain_id': chainId, 'seq_id': seqId, 'comp_id': compId, 'atom_id': _atomId})

                atomSelection = [dict(s) for s in set(frozenset(atom.items()) for atom in _atomSelection)]

                if len(atomSelection) <= len(self.factor['atom_selection']):
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        "The 'bygroup' clause has no effect.\n"

                self.factor['atom_selection'] = atomSelection

            else:
                self.factor['atom_id'] = [None]
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    "The 'bygroup' clause has no effect because no atom is selected.\n"

        elif ctx.ByRes():
            if self.__debug:
                print("  " * self.depth + "--> byres")
            if not self.__hasCoord:
                return
            if 'atom_selection' in self.factor and len(self.factor['atom_selection']) > 0:
                _atomSelection = []

                _sequenceSelect = set()

                for _atom in self.factor['atom_selection']:
                    chainId = _atom['chain_id']
                    seqId = _atom['seq_id']

                    _sequenceSelect.add((chainId, seqId))

                for (chainId, seqId) in _sequenceSelect:
                    _atom = next(_atom for _atom in self.factor['atom_selection'] if _atom['chain_id'] == chainId and _atom['seq_id'] == seqId)
                    compId = _atom['comp_id']

                    _atomByRes =\
                        self.__cR.getDictListWithFilter('atom_site',
                                                        [{'name': 'label_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                         {'name': 'label_atom_id', 'type': 'str', 'alt_name': 'atom_id'}
                                                         ],
                                                        [{'name': self.__authAsymId, 'type': 'str', 'value': chainId},
                                                         {'name': self.__authSeqId, 'type': 'int', 'value': seqId},
                                                         {'name': self.__modelNumName, 'type': 'int',
                                                          'value': REPRESENTATIVE_MODEL_ID}
                                                         ])

                    if len(_atomByRes) > 0 and _atomByRes[0]['comp_id'] == compId:
                        for _atom in _atomByRes:
                            _atomSelection.append({'chain_id': chainId, 'seq_id': seqId, 'comp_id': _atom['comp_id'], 'atom_id': _atom['atom_id']})

                    else:
                        ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chainId), None)
                        if ps is not None and seqId in ps['seq_id'] and ps['comp_id'][ps['seq_id'].index(seqId)] == compId:
                            if self.__ccU.updateChemCompDict(compId):
                                atomIds = [cca[self.__ccU.ccaAtomId] for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaLeavingAtomFlag] != 'Y']
                                for atomId in atomIds:
                                    _atomSelection.append({'chain_id': chainId, 'seq_id': seqId, 'comp_id': compId, 'atom_id': atomId})

                self.factor['atom_selection'] = [dict(s) for s in set(frozenset(atom.items()) for atom in _atomSelection)]

                if len(self.factor['atom_selection']) == 0:
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        "The 'byres' clause has no effect.\n"

            else:
                self.factor['atom_id'] = [None]
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    "The 'byres' clause has no effect because no atom is selected.\n"

        elif ctx.Chemical():
            if self.__debug:
                print("  " * self.depth + "--> chemical")
            if ctx.Colon():  # range expression
                self.factor['type_symbols'] = [str(ctx.Simple_name(0)), str(ctx.Simple_name(1))]

            elif ctx.Simple_name(0):
                self.factor['type_symbol'] = [str(ctx.Simple_name(0))]

            elif ctx.Simple_names(0):
                self.factor['type_symbols'] = [str(ctx.Simple_names(0))]

            self.consumeFactor_expressions("'chemical' clause", False)

        elif ctx.Hydrogen():
            if self.__debug:
                print("  " * self.depth + "--> hydrogen")
            _typeSymbolSelect = set()
            atomTypes = self.__cR.getDictList('atom_type')
            if len(atomTypes) > 0 and 'symbol' in atomTypes[0]:
                for atomType in atomTypes:
                    typeSymbol = atomType['symbol']
                    atomicNumber = int_atom(typeSymbol)
                    atomicWeight = ELEMENT_WEIGHTS[atomicNumber]
                    if atomicWeight < 3.5:
                        _typeSymbolSelect.add(typeSymbol)

            self.factor['type_symbol'] = list(_typeSymbolSelect)

            self.consumeFactor_expressions("'hydrogen' clause", False)

        elif ctx.Id():
            if self.__debug:
                print("  " * self.depth + "--> id")
            self.factor['atom_id'] = [None]
            self.warningMessage += f"[Unavailable resource] {self.__getCurrentRestraint()}"\
                "The 'id' clause has no effect "\
                "because the internal atom number is not included in the coordinate file.\n"

        elif ctx.Name():
            if self.__debug:
                print("  " * self.depth + "--> name")
            if ctx.Colon():  # range expression
                self.factor['atom_ids'] = [str(ctx.Simple_name(0)), str(ctx.Simple_name(1))]

            elif ctx.Simple_name(0):
                self.factor['atom_id'] = [str(ctx.Simple_name(0))]

            elif ctx.Simple_names(0):
                self.factor['atom_ids'] = [str(ctx.Simple_names(0))]

        elif ctx.Not_op():
            if self.__debug:
                print("  " * self.depth + "--> not")
            if not self.__hasCoord:
                return

            try:

                _atomSelection =\
                    self.__cR.getDictListWithFilter('atom_site',
                                                    [{'name': 'auth_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                                     {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                                     {'name': 'label_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                     {'name': 'label_atom_id', 'type': 'str', 'alt_name': 'atom_id'}
                                                     ],
                                                    [{'name': self.__modelNumName, 'type': 'int',
                                                      'value': REPRESENTATIVE_MODEL_ID}
                                                     ])

            except Exception as e:
                if self.__verbose:
                    self.__lfh.write(f"+XplorMRParserListener.exitFactor() ++ Error  - {str(e)}\n")

            _refAtomSelection = [atom for atom in self.factor['atom_selection'] if atom in _atomSelection]
            self.factor['atom_selection'] = [atom for atom in _atomSelection if atom not in _refAtomSelection]

            if len(self.factor['atom_selection']) == 0:
                self.factor['atom_id'] = [None]
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    "The 'not' clause has no effect.\n"

        elif ctx.Point():
            if self.__debug:
                print("  " * self.depth + "--> point")
            if not self.__hasCoord:
                return
            if ctx.Tail():

                if self.inVector3D_tail is not None:

                    try:

                        _tail =\
                            self.__cR.getDictListWithFilter('atom_site',
                                                            [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                             {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                             {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                                                             ],
                                                            [{'name': self.__authAsymId, 'type': 'str', 'value': self.inVector3D_tail['chain_id']},
                                                             {'name': self.__authSeqId, 'type': 'int', 'value': self.inVector3D_tail['seq_id']},
                                                             {'name': self.__authAtomId, 'type': 'str', 'value': self.inVector3D_tail['atom_id']},
                                                             {'name': self.__modelNumName, 'type': 'int',
                                                              'value': REPRESENTATIVE_MODEL_ID}
                                                             ])

                        if len(_tail) == 1:
                            tail = toNpArray(_tail[0])

                            if self.inVector3D_head is None:
                                self.vector3D = tail

                            else:

                                _head =\
                                    self.__cR.getDictListWithFilter('atom_site',
                                                                    [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                                     {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                                     {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                                                                     ],
                                                                    [{'name': self.__authAsymId, 'type': 'str', 'value': self.inVector3D_head['chain_id']},
                                                                     {'name': self.__authSeqId, 'type': 'int', 'value': self.inVector3D_head['seq_id']},
                                                                     {'name': self.__authAtomId, 'type': 'str', 'value': self.inVector3D_head['atom_id']},
                                                                     {'name': self.__modelNumName, 'type': 'int',
                                                                      'value': REPRESENTATIVE_MODEL_ID}
                                                                     ])

                                if len(_head) == 1:
                                    head = toNpArray(_head[0])
                                    self.vector3D = np.subtract(tail, head, dtype=float)

                    except Exception as e:
                        if self.__verbose:
                            self.__lfh.write(f"+XplorMRParserListener.exitFactor() ++ Error  - {str(e)}\n")

                self.inVector3D_tail = self.inVector3D_head = None
                cut = float(str(ctx.Real(0)))

            else:
                self.vector3D = [float(str(ctx.Real(0))), float(str(ctx.Real(1))), float(str(ctx.Real(2)))]
                cut = float(str(ctx.Real(3)))

            if self.vector3D is None:
                self.factor['atom_id'] = [None]
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    "The 'point' clause has no effect because no 3d-vector is specified.\n"

            else:
                atomSelection = []

                try:

                    _neighbor =\
                        self.__cR.getDictListWithFilter('atom_site',
                                                        [{'name': 'auth_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                                         {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                                         {'name': 'label_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                         {'name': 'label_atom_id', 'type': 'str', 'alt_name': 'atom_id'},
                                                         {'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                         {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                         {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                                                         ],
                                                        [{'name': 'Cartn_x', 'type': 'range-float',
                                                          'range': {'min_exclusive': (self.vector3D[0] - cut),
                                                                    'max_exclusive': (self.vector3D[0] + cut)}},
                                                         {'name': 'Cartn_y', 'type': 'range-float',
                                                          'range': {'min_exclusive': (self.vector3D[1] - cut),
                                                                    'max_exclusive': (self.vector3D[1] + cut)}},
                                                         {'name': 'Cartn_z', 'type': 'range-float',
                                                          'range': {'min_exclusive': (self.vector3D[2] - cut),
                                                                    'max_exclusive': (self.vector3D[2] + cut)}},
                                                         {'name': self.__modelNumName, 'type': 'int',
                                                          'value': REPRESENTATIVE_MODEL_ID}
                                                         ])

                    if len(_neighbor) > 0:
                        neighbor = [atom for atom in _neighbor if np.linalg.norm(toNpArray(atom) - self.vector3D) < cut]

                        for atom in neighbor:
                            del atom['x']
                            del atom['y']
                            del atom['z']
                            atomSelection.append(atom)

                except Exception as e:
                    if self.__verbose:
                        self.__lfh.write(f"+XplorMRParserListener.exitFactor() ++ Error  - {str(e)}\n")

                self.factor['atom_selection'] = atomSelection

                if len(self.factor['atom_selection']) == 0:
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        "The 'cut' clause has no effect.\n"

            self.inVector3D = False
            self.vector3D = None

        elif ctx.Previous():
            if self.__debug:
                print("  " * self.depth + "--> previous")
            self.factor['atom_id'] = [None]
            self.warningMessage += f"[Unavailable resource] {self.__getCurrentRestraint()}"\
                "The 'previous' clause has no effect "\
                "because the internal atom selection is fragile in the restraint file.\n"

        elif ctx.Pseudo():
            if self.__debug:
                print("  " * self.depth + "--> pseudo")
            if not self.__hasCoord:
                return
            atomSelection = []

            try:

                _atomSelection =\
                    self.__cR.getDictListWithFilter('atom_site',
                                                    [{'name': 'auth_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                                     {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                                     {'name': 'label_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                     {'name': 'label_atom_id', 'type': 'str', 'alt_name': 'atom_id'}
                                                     ],
                                                    [{'name': self.__modelNumName, 'type': 'int',
                                                      'value': REPRESENTATIVE_MODEL_ID}
                                                     ])

                lastCompId = None
                pseudoAtoms = None

                for _atom in _atomSelection:
                    compId = _atom['comp_id']
                    atomId = _atom['atom_id']

                    if compId is not lastCompId:
                        pseudoAtoms = self.__csStat.getPseudoAtoms(compId)
                        lastCompId = compId

                    if atomId in pseudoAtoms:
                        atomSelection.append(_atom)

            except Exception as e:
                if self.__debug:
                    self.__lfh.write(f"+XplorMRParserListener.exitFactor() ++ Error  - {str(e)}\n")

            self.intersectionFactor_expressions(atomSelection)

            if len(self.factor['atom_selection']) == 0:
                self.factor['atom_id'] = [None]
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    "The 'pseudo' clause has no effect.\n"

        elif ctx.Residue():
            if self.__debug:
                print("  " * self.depth + "--> residue")
            if ctx.Colon():  # range expression
                self.factor['seq_id'] = list(range(int(str(ctx.Integer(0))), int(str(ctx.Integer(0))) + 1))

            elif ctx.Integer(0):
                self.factor['seq_id'] = [int(str(ctx.Integer(0)))]

            elif ctx.Integers():
                self.factor['seq_ids'] = [str(ctx.Integers())]

        elif ctx.Resname():
            if self.__debug:
                print("  " * self.depth + "--> resname")
            if ctx.Colon():  # range expression
                self.factor['comp_ids'] = [str(ctx.Simple_name(0)), str(ctx.Simple_name(1))]

            elif ctx.Simple_name(0):
                self.factor['comp_id'] = [str(ctx.Simple_name(0))]

            elif ctx.Simple_names(0):
                self.factor['comp_ids'] = [str(ctx.Simple_names(0))]

        elif ctx.SegIdentifier():
            if self.__debug:
                print("  " * self.depth + "--> segidentifier")
            if not self.__hasPolySeq:
                return
            if ctx.Colon():  # range expression
                if ctx.Simple_name(0):
                    begChainId = str(ctx.Simple_name(0))
                elif ctx.Double_quote_string(0):
                    begChainId = str(ctx.Simple_name(0)).strip('"').strip()
                if ctx.Simple_name(1):
                    endChainId = str(ctx.Simple_name(1))
                elif ctx.Double_quote_string(1):
                    endChainId = str(ctx.Simple_name(1)).strip('"').strip()
                self.factor['chain_id'] = [ps['chain_id'] for ps in self.__polySeq
                                           if begChainId <= ps['chain_id'] <= endChainId]

                if len(self.factor['chain_id']) == 0:
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"Couldn't specify segment name {begChainId:!r}:{endChainId:!r} in the coordinates.\n"

            else:
                if ctx.Simple_name(0) or ctx.Double_quote_string(0):
                    if ctx.Simple_name(0):
                        chainId = str(ctx.Simple_name(0))
                    elif ctx.Double_quote_string(0):
                        chainId = str(ctx.Simple_name(0)).strip('"').strip()
                    self.factor['chain_id'] = [ps['chain_id'] for ps in self.__polySeq
                                               if ps['chain_id'] == chainId]
                if ctx.Simple_names(0):
                    chainId = str(ctx.Simple_names(0))
                    _chainId = toRegEx(chainId)
                    self.factor['chain_id'] = [ps['chain_id'] for ps in self.__polySeq
                                               if re.match(_chainId, ps['chain_id'])]
                if len(self.factor['chain_id']) == 0:
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        "Couldn't specify segment name "\
                        f"'{chainId}' in the coordinates.\n"  # do not use 'chainId!r' expression, '%' code throws ValueError

        elif ctx.Store_1() or ctx.Store_2() or ctx.Store_3()\
                or ctx.Store_4() or ctx.Store_5() or ctx.Store_6()\
                or ctx.Store_7() or ctx.Store_8() or ctx.Store_9():
            if self.__debug:
                print("  " * self.depth + "--> store[1-9]")
            self.factor['atom_id'] = [None]
            self.warningMessage += f"[Unavailable resource] {self.__getCurrentRestraint()}"\
                "The 'store[1-9]' clause has no effect "\
                "because the internal vector statement is fragile in the restraint file.\n"

        elif ctx.Tag():
            if self.__debug:
                print("  " * self.depth + "--> tag")
            if not self.__hasCoord:
                return
            atomSelection = []
            _sequenceSelect = []

            try:

                _atomSelection =\
                    self.__cR.getDictListWithFilter('atom_site',
                                                    [{'name': 'auth_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                                     {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                                     {'name': 'label_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                     {'name': 'label_atom_id', 'type': 'str', 'alt_name': 'atom_id'}
                                                     ],
                                                    [{'name': self.__modelNumName, 'type': 'int',
                                                      'value': REPRESENTATIVE_MODEL_ID}
                                                     ])

                for _atom in _atomSelection:
                    _sequence = (_atom['chain_id'], _atom['seq_id'])

                    if _sequence in _sequenceSelect:
                        continue

                    atomSelection.append(_atom)
                    _sequenceSelect.append(_sequence)

            except Exception as e:
                if self.__verbose:
                    self.__lfh.write(f"+XplorMRParserListener.exitFactor() ++ Error  - {str(e)}\n")

            self.intersectionFactor_expressions(atomSelection)

            if len(self.factor['atom_selection']) == 0:
                self.factor['atom_id'] = [None]
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    "The 'tag' clause has no effect.\n"

        self.stackFactors.append(self.factor)

    def __getCurrentRestraint(self):
        if self.__cur_subtype == 'dist':
            return f"[Check the {self.distRestraints}th row of distance restraints] "
        if self.__cur_subtype == 'dihed':
            return f"[Check the {self.dihedRestraints}th row of dihedral angle restraints] "
        if self.__cur_subtype == 'rdc':
            return f"[Check the {self.rdcRestraints}th row of residual dipolar coupling restraints] "
        if self.__cur_subtype == 'plane':
            return f"[Check the {self.planeRestraints}th row of planality restraints] "
        if self.__cur_subtype == 'adist':
            return f"[Check the {self.adistRestraints}th row of antidistance restraints] "
        if self.__cur_subtype == 'jcoup':
            return f"[Check the {self.jcoupRestraints}th row of scalar J-coupling restraints] "
        if self.__cur_subtype == 'hvycs':
            return f"[Check the {self.hvycsRestraints}th row of carbon chemical shift restraints] "
        if self.__cur_subtype == 'procs':
            return f"[Check the {self.procsRestraints}th row of proton chemical shift restraints] "
        if self.__cur_subtype == 'rama':
            return f"[Check the {self.ramaRestraints}th row of dihedral angle database restraints] "
        if self.__cur_subtype == 'radi':
            return f"[Check the {self.radiRestraints}th row of radius of gyration restraints] "
        if self.__cur_subtype == 'diff':
            return f"[Check the {self.diffRestraints}th row of duffusion anisotropy restraints] "
        if self.__cur_subtype == 'nbase':
            return f"[Check the {self.nbaseRestraints}th row of residue-residue position/orientation database restraints] "
        if self.__cur_subtype == 'csa':
            return f"[Check the {self.csaRestraints}th row of (pseudo) chemical shift anisotropy restraints] "
        if self.__cur_subtype == 'ang':
            return f"[Check the {self.angRestraints}th row of angle database restraints] "
        if self.__cur_subtype == 'pre':
            return f"[Check the {self.preRestraints}th row of paramagnetic relaxation enhancement restraints] "
        if self.__cur_subtype == 'pcs':
            return f"[Check the {self.pcsRestraints}th row of paramagnetic pseudocontact shift restraints] "
        if self.__cur_subtype == 'prdc':
            return f"[Check the {self.prdcRestraints}th row of paramagnetic residual dipolar coupling restraints] "
        if self.__cur_subtype == 'pang':
            return f"[Check the {self.pangRestraints}th row of paramagnetic orientation restraints] "
        if self.__cur_subtype == 'pccr':
            return f"[Check the {self.pccrRestraints}th row of paramagnetic cross-correlation rate restraints] "
        if self.__cur_subtype == 'hbond':
            return f"[Check the {self.hbondRestraints}th row of hydrogen bond geometry restraints] "
        return ''

    def getContentSubtype(self):
        """ Return content subtype of XPLOR-NIH MR file.
        """

        if self.distStatements == 0 and self.distRestraints > 0:
            self.distStatements = 1

        if self.dihedStatements == 0 and self.dihedRestraints > 0:
            self.dihedStatements = 1

        if self.rdcStatements == 0 and self.rdcRestraints > 0:
            self.rdcStatements = 1

        if self.planeStatements == 0 and self.planeRestraints > 0:
            self.planeStatements = 1

        if self.adistStatements == 0 and self.adistRestraints > 0:
            self.adistStatements = 1

        if self.jcoupStatements == 0 and self.jcoupRestraints > 0:
            self.jcoupStatements = 1

        if self.hvycsStatements == 0 and self.hvycsRestraints > 0:
            self.hvycsStatements = 1

        if self.procsStatements == 0 and self.procsRestraints > 0:
            self.procsStatements = 1

        if self.ramaStatements == 0 and self.ramaRestraints > 0:
            self.ramaStatements = 1

        if self.radiStatements == 0 and self.radiRestraints > 0:
            self.radiStatements = 1

        if self.diffStatements == 0 and self.diffRestraints > 0:
            self.diffStatements = 1

        if self.nbaseStatements == 0 and self.nbaseRestraints > 0:
            self.nbaseStatements = 1

        if self.csaStatements == 0 and self.csaRestraints > 0:
            self.csaStatements = 1

        if self.angStatements == 0 and self.angRestraints > 0:
            self.angStatements = 1

        if self.preStatements == 0 and self.preRestraints > 0:
            self.preStatements = 1

        if self.pcsStatements == 0 and self.pcsRestraints > 0:
            self.pcsStatements = 1

        if self.prdcStatements == 0 and self.prdcRestraints > 0:
            self.prdcStatements = 1

        if self.pangStatements == 0 and self.pangRestraints > 0:
            self.pangStatements = 1

        if self.pccrStatements == 0 and self.pccrRestraints > 0:
            self.pccrStatements = 1

        if self.hbondStatements == 0 and self.hbondRestraints > 0:
            self.hbondStatements = 1

        contentSubtype = {'dist_restraint': self.distStatements,
                          'dihed_restraint': self.dihedStatements,
                          'rdc_restraint': self.rdcStatements,
                          'plane_restraint': self.planeStatements,
                          'adist_restraint': self.adistStatements,
                          'jcoup_restraint': self.jcoupStatements,
                          'hvycs_restraint': self.hvycsStatements,
                          'procs_restraint': self.procsStatements,
                          'rama_restraint': self.ramaStatements,
                          'radi_restraint': self.radiStatements,
                          'diff_restraint': self.diffStatements,
                          'nbase_restraint': self.nbaseStatements,
                          'csa_restraint': self.csaStatements,
                          'ang_restraint': self.angStatements,
                          'pre_restraint': self.preStatements,
                          'pcs_restraint': self.pcsStatements,
                          'prdc_restraint': self.prdcStatements,
                          'pang_restraint': self.pangStatements,
                          'pccr_restraint': self.pccrStatements,
                          'hbond_restraint': self.hbondStatements
                          }

        return {k: v for k, v in contentSubtype.items() if v > 0}

    def getCoordAtomSite(self):
        """ Return coordinates' atom name dictionary of each residue.
        """
        return self.__coordAtomSite

    def getCoordUnobsRes(self):
        """ Return catalog of unobserved residues of the coordinates.
        """
        return self.__coordUnobsRes

    def getLabelToAuthSeq(self):
        """ Return dictionary of differences between label_seq_id (as key) to auth_seq_id (as value).
        """
        return self.__labelToAuthSeq

# del XplorMRParser
