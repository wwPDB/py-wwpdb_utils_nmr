##
# File: GromacsMRParserListener.py
# Date: 02-June-2022
#
# Updates:
# Generated from GromacsMRParser.g4 by ANTLR 4.10.1
""" ParserLister class for GROMACS MR files.
    @author: Masashi Yokochi
"""
import sys
import itertools
import copy

from antlr4 import ParseTreeListener

try:
    from wwpdb.utils.align.alignlib import PairwiseAlign  # pylint: disable=no-name-in-module
    from wwpdb.utils.nmr.mr.GromacsMRParser import GromacsMRParser
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (checkCoordinates,
                                                       getTypeOfDihedralRestraint,
                                                       REPRESENTATIVE_MODEL_ID,
                                                       DIST_RESTRAINT_RANGE,
                                                       DIST_RESTRAINT_ERROR,
                                                       ANGLE_RESTRAINT_RANGE,
                                                       ANGLE_RESTRAINT_ERROR,
                                                       RDC_RESTRAINT_RANGE,
                                                       RDC_RESTRAINT_ERROR)
    from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
    from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from wwpdb.utils.nmr.NEFTranslator.NEFTranslator import (NEFTranslator,
                                                             ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS)
    from wwpdb.utils.nmr.AlignUtil import (hasLargeSeqGap,
                                           fillBlankCompIdWithOffset, beautifyPolySeq,
                                           getMiddleCode, getGaugeCode, getScoreOfSeqAlign,
                                           getOneLetterCodeSequence)
except ImportError:
    from nmr.align.alignlib import PairwiseAlign  # pylint: disable=no-name-in-module
    from nmr.mr.GromacsMRParser import GromacsMRParser
    from nmr.mr.ParserListenerUtil import (checkCoordinates,
                                           getTypeOfDihedralRestraint,
                                           REPRESENTATIVE_MODEL_ID,
                                           DIST_RESTRAINT_RANGE,
                                           DIST_RESTRAINT_ERROR,
                                           ANGLE_RESTRAINT_RANGE,
                                           ANGLE_RESTRAINT_ERROR,
                                           RDC_RESTRAINT_RANGE,
                                           RDC_RESTRAINT_ERROR)
    from nmr.ChemCompUtil import ChemCompUtil
    from nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from nmr.NEFTranslator.NEFTranslator import (NEFTranslator,
                                                 ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS)
    from nmr.AlignUtil import (hasLargeSeqGap,
                               fillBlankCompIdWithOffset, beautifyPolySeq,
                               getMiddleCode, getGaugeCode, getScoreOfSeqAlign,
                               getOneLetterCodeSequence)


DIST_RANGE_MIN = DIST_RESTRAINT_RANGE['min_inclusive']
DIST_RANGE_MAX = DIST_RESTRAINT_RANGE['max_inclusive']

DIST_ERROR_MIN = DIST_RESTRAINT_ERROR['min_exclusive']
DIST_ERROR_MAX = DIST_RESTRAINT_ERROR['max_exclusive']


ANGLE_RANGE_MIN = ANGLE_RESTRAINT_RANGE['min_inclusive']
ANGLE_RANGE_MAX = ANGLE_RESTRAINT_RANGE['max_inclusive']

ANGLE_ERROR_MIN = ANGLE_RESTRAINT_ERROR['min_exclusive']
ANGLE_ERROR_MAX = ANGLE_RESTRAINT_ERROR['max_exclusive']

RDC_RANGE_MIN = RDC_RESTRAINT_RANGE['min_inclusive']
RDC_RANGE_MAX = RDC_RESTRAINT_RANGE['max_inclusive']

RDC_ERROR_MIN = RDC_RESTRAINT_ERROR['min_exclusive']
RDC_ERROR_MAX = RDC_RESTRAINT_ERROR['max_exclusive']


# This class defines a complete listener for a parse tree produced by GromacsMRParser.
class GromacsMRParserListener(ParseTreeListener):

    # __verbose = None
    # __lfh = None
    __debug = False
    __omitDistLimitOutlier = True

    distRestraints = 0      # GROMACS: Distance restraints
    angRestraints = 0       # GROMACS: Angle restraints
    dihedRestraints = 0     # GROMACS: Dihedral angle restraints
    rdcRestraints = 0       # GROMACS: Residual dipolar coupling restraints
    geoRestraints = 0       # GROMACS: Coordinate geometry restraints

    # criterion for low sequence coverage
    low_seq_coverage = 0.3

    # criterion for minimum sequence coverage when conflict occurs (NMR separated deposition)
    # min_seq_coverage_w_conflict = 0.95

    # CCD accessing utility
    __ccU = None

    # BMRB chemical shift statistics
    __csStat = None

    # NEFTranslator
    __nefT = None

    # Pairwise align
    __pA = None

    # GromacsPTParserListener.getAtomNumberDict()
    __atomNumberDict = None

    # CIF reader
    # __cR = None
    __hasCoord = False

    # data item name for model ID in 'atom_site' category
    # __modelNumName = None

    # data item names for auth_asym_id, auth_seq_id, auth_atom_id in 'atom_site' category
    # __authAsymId = None
    # __authSeqId = None
    # __authAtomId = None
    # __altAuthAtomId = None

    # coordinates information generated by ParserListenerUtil.checkCoordinates()
    __polySeq = None
    # __altPolySeq = None
    # __coordAtomSite = None
    # __coordUnobsRes = None
    # __labelToAuthSeq = None
    # __authToLabelSeq = None

    __hasPolySeq = False
    __preferAuthSeq = True

    # polymer sequence of MR file
    __polySeqRst = None

    __seqAlign = None
    __chainAssign = None

    # current restraint subtype
    __cur_subtype = ''

    # collection of atom selection
    atomSelectionSet = []

    # collection of number selection
    numberSelection = []

    warningMessage = ''

    def __init__(self, verbose=True, log=sys.stdout,
                 representativeModelId=REPRESENTATIVE_MODEL_ID,
                 cR=None, cC=None, ccU=None, csStat=None, nefT=None,
                 atomNumberDict=None):
        # self.__verbose = verbose
        # self.__lfh = log
        # self.__cR = cR
        self.__hasCoord = cR is not None

        if self.__hasCoord:
            ret = checkCoordinates(verbose, log, representativeModelId, cR, cC)
            # self.__modelNumName = ret['model_num_name']
            # self.__authAsymId = ret['auth_asym_id']
            # self.__authSeqId = ret['auth_seq_id']
            # self.__authAtomId = ret['auth_atom_id']
            # self.__altAuthAtomId = ret['alt_auth_atom_id']
            self.__polySeq = ret['polymer_sequence']
            # self.__altPolySeq = ret['alt_polymer_sequence']
            # self.__coordAtomSite = ret['coord_atom_site']
            # self.__coordUnobsRes = ret['coord_unobs_res']
            # self.__labelToAuthSeq = ret['label_to_auth_seq']
            # self.__authToLabelSeq = ret['auth_to_label_seq']

        self.__hasPolySeq = self.__polySeq is not None and len(self.__polySeq) > 0

        # CCD accessing utility
        self.__ccU = ChemCompUtil(verbose, log) if ccU is None else ccU

        # BMRB chemical shift statistics
        self.__csStat = BMRBChemShiftStat(verbose, log, self.__ccU) if csStat is None else csStat

        # NEFTranslator
        self.__nefT = NEFTranslator(verbose, log, self.__ccU, self.__csStat) if nefT is None else nefT

        # Pairwise align
        if self.__hasPolySeq:
            self.__pA = PairwiseAlign()
            self.__pA.setVerbose(verbose)

        self.__atomNumberDict = atomNumberDict

    def setDebugMode(self, debug):
        self.__debug = debug

    # Enter a parse tree produced by GromacsMRParser#gromacs_mr.
    def enterGromacs_mr(self, ctx: GromacsMRParser.Gromacs_mrContext):  # pylint: disable=unused-argument
        self.__polySeqRst = []

    # Exit a parse tree produced by GromacsMRParser#gromacs_mr.
    def exitGromacs_mr(self, ctx: GromacsMRParser.Gromacs_mrContext):  # pylint: disable=unused-argument
        if self.__hasPolySeq and self.__polySeqRst is not None:
            self.sortPolySeqRst()

            self.alignPolymerSequence()
            self.assignPolymerSequence()

            if self.__chainAssign is not None:

                chain_mapping = {}

                for chain_assign in self.__chainAssign:
                    ref_chain_id = chain_assign['ref_chain_id']
                    test_chain_id = chain_assign['test_chain_id']

                    if ref_chain_id != test_chain_id:
                        chain_mapping[test_chain_id] = ref_chain_id

                if len(chain_mapping) > 0:

                    for ps in self.__polySeqRst:
                        if ps['chain_id'] in chain_mapping:
                            ps['chain_id'] = chain_mapping[ps['chain_id']]

                    self.alignPolymerSequence()
                    self.assignPolymerSequence()

                self.trimPolymerSequence()

        if len(self.warningMessage) == 0:
            self.warningMessage = None
        else:
            self.warningMessage = self.warningMessage[0:-1]
            self.warningMessage = '\n'.join(set(self.warningMessage.split('\n')))

    # Enter a parse tree produced by GromacsMRParser#distance_restraints.
    def enterDistance_restraints(self, ctx: GromacsMRParser.Distance_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dist'

    # Exit a parse tree produced by GromacsMRParser#distance_restraints.
    def exitDistance_restraints(self, ctx: GromacsMRParser.Distance_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by GromacsMRParser#distance_restraint.
    def enterDistance_restraint(self, ctx: GromacsMRParser.Distance_restraintContext):  # pylint: disable=unused-argument
        self.distRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by GromacsMRParser#distance_restraint.
    def exitDistance_restraint(self, ctx: GromacsMRParser.Distance_restraintContext):

        try:

            if None in self.numberSelection:
                return

            ai = int(str(ctx.Integer(0)))
            aj = int(str(ctx.Integer(1)))
            funct = int(str(ctx.Integer(2)))
            index = int(str(ctx.Integer(3)))

            lower_limit = self.numberSelection[0]
            upper_limit = self.numberSelection[1]
            upper_linear_limit = self.numberSelection[2]
            weight = self.numberSelection[3]

            if funct != 1:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=index)}"\
                    f"Unknown function type '{funct}' is set.\n"
                return

            if weight <= 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=index)}"\
                    f"The relative weight value of '{weight}' must be a positive value.\n"
                return

            dstFunc = self.validateDistanceRange(index, weight, lower_limit, upper_limit, upper_linear_limit, self.__omitDistLimitOutlier)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            if self.__atomNumberDict is None:
                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint(n=index)}"\
                    "Failed to recognize GROMACS atom numbers in the restraint file "\
                    "because GROMACS parameter/topology file is not available.\n"
                return

            atomSelection = []

            if ai in self.__atomNumberDict:
                atomSelection.append(self.__atomNumberDict[ai])
                self.atomSelectionSet.append(atomSelection)
            else:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=index)}"\
                    f"'ai={ai}' is not defined in the GROMACS parameter/topology file.\n"

            atomSelection.clear()

            if aj in self.__atomNumberDict:
                atomSelection.append(self.__atomNumberDict[aj])
                self.atomSelectionSet.append(atomSelection)
            else:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=index)}"\
                    f"'aj={aj}' is not defined in the GROMACS parameter/topology file.\n"

            if len(self.atomSelectionSet) < 2:
                return

            self.updatePolySeqRstFromAtomSelectionSet()

            for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                  self.atomSelectionSet[1]):
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} id={self.distRestraints} (index={index}) "
                          f"atom1={atom1} atom2={atom2} {dstFunc}")

        finally:
            self.numberSelection.clear()

    def validateDistanceRange(self, index, weight, lower_limit, upper_limit, upper_linear_limit, omit_dist_limit_outlier):
        """ Validate distance value range.
        """

        validRange = True
        dstFunc = {'weight': weight}

        if lower_limit is not None:
            if DIST_ERROR_MIN <= lower_limit < DIST_ERROR_MAX:
                dstFunc['lower_limit'] = f"{lower_limit}"
            else:
                if lower_limit <= DIST_ERROR_MIN and omit_dist_limit_outlier:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index)}"\
                        f"The lower limit value='{lower_limit}' is omitted because it is not within range {DIST_RESTRAINT_ERROR}.\n"
                    lower_limit = None
                else:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index)}"\
                        f"The lower limit value='{lower_limit}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if upper_limit is not None:
            if DIST_ERROR_MIN < upper_limit <= DIST_ERROR_MAX:
                dstFunc['upper_limit'] = f"{upper_limit}"
            else:
                if upper_limit > DIST_ERROR_MAX and omit_dist_limit_outlier:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index)}"\
                        f"The upper limit value='{upper_limit}' is omitted because it is not within range {DIST_RESTRAINT_ERROR}.\n"
                    upper_limit = None
                else:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index)}"\
                        f"The upper limit value='{upper_limit}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if upper_linear_limit is not None:
            if DIST_ERROR_MIN < upper_linear_limit <= DIST_ERROR_MAX:
                dstFunc['upper_linear_limit'] = f"{upper_linear_limit}"
            else:
                if upper_linear_limit > DIST_ERROR_MAX and self.__omitDistLimitOutlier:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index)}"\
                        f"The upper linear limit value='{upper_linear_limit}' is omitted because it is not within range {DIST_RESTRAINT_ERROR}.\n"
                    upper_linear_limit = None
                else:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index)}"\
                        f"The upper linear limit value='{upper_linear_limit}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if upper_limit is not None and upper_linear_limit is not None:
            if upper_limit > upper_linear_limit:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index)}"\
                    f"The upper limit value='{upper_limit}' must be less than the upper linear limit value '{upper_linear_limit}'.\n"

        if not validRange:
            return None

        if lower_limit is not None:
            if DIST_RANGE_MIN <= lower_limit <= DIST_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index)}"\
                    f"The lower limit value='{lower_limit}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        if upper_limit is not None:
            if DIST_RANGE_MIN <= upper_limit <= DIST_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index)}"\
                    f"The upper limit value='{upper_limit}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        if upper_linear_limit is not None:
            if DIST_RANGE_MIN <= upper_linear_limit <= DIST_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index)}"\
                    f"The upper linear limit value='{upper_linear_limit}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        return dstFunc

    # Enter a parse tree produced by GromacsMRParser#dihedral_restraints.
    def enterDihedral_restraints(self, ctx: GromacsMRParser.Dihedral_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dihed'

    # Exit a parse tree produced by GromacsMRParser#dihedral_restraints.
    def exitDihedral_restraints(self, ctx: GromacsMRParser.Dihedral_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by GromacsMRParser#dihedral_restraint.
    def enterDihedral_restraint(self, ctx: GromacsMRParser.Dihedral_restraintContext):  # pylint: disable=unused-argument
        self.dihedRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by GromacsMRParser#dihedral_restraint.
    def exitDihedral_restraint(self, ctx: GromacsMRParser.Dihedral_restraintContext):  # pylint: disable=unused-argument

        try:

            if None in self.numberSelection:
                return

            ai = int(str(ctx.Integer(0)))
            aj = int(str(ctx.Integer(1)))
            ak = int(str(ctx.Integer(2)))
            al = int(str(ctx.Integer(3)))
            funct = int(str(ctx.Integer(4)))

            target_value = self.numberSelection[0]
            delta = self.numberSelection[1]
            weight = self.numberSelection[2]

            lower_limit = target_value - delta
            upper_limit = target_value + delta

            if funct != 1:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Unknown function type '{funct}' is set.\n"
                return

            if weight <= 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The relative weight value of '{weight}' must be a positive value.\n"
                return

            dstFunc = self.validateAngleRange(weight, target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            if self.__atomNumberDict is None:
                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                    "Failed to recognize GROMACS atom numbers in the restraint file "\
                    "because GROMACS parameter/topology file is not available.\n"
                return

            atomSelection = []

            if ai in self.__atomNumberDict:
                atomSelection.append(self.__atomNumberDict[ai])
                self.atomSelectionSet.append(atomSelection)
            else:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"'ai={ai}' is not defined in the GROMACS parameter/topology file.\n"

            atomSelection.clear()

            if aj in self.__atomNumberDict:
                atomSelection.append(self.__atomNumberDict[aj])
                self.atomSelectionSet.append(atomSelection)
            else:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"'aj={aj}' is not defined in the GROMACS parameter/topology file.\n"

            atomSelection.clear()

            if ak in self.__atomNumberDict:
                atomSelection.append(self.__atomNumberDict[ak])
                self.atomSelectionSet.append(atomSelection)
            else:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"'ak={ak}' is not defined in the GROMACS parameter/topology file.\n"

            atomSelection.clear()

            if al in self.__atomNumberDict:
                atomSelection.append(self.__atomNumberDict[al])
                self.atomSelectionSet.append(atomSelection)
            else:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"'al={al}' is not defined in the GROMACS parameter/topology file.\n"

            if len(self.atomSelectionSet) < 4:
                return

            self.updatePolySeqRstFromAtomSelectionSet()

            compId = self.atomSelectionSet[0][0]['comp_id']
            peptide, nucleotide, carbohydrate = self.__csStat.getTypeOfCompId(compId)

            for atom1, atom2, atom3, atom4 in itertools.product(self.atomSelectionSet[0],
                                                                self.atomSelectionSet[1],
                                                                self.atomSelectionSet[2],
                                                                self.atomSelectionSet[3]):
                if atom1['chain_id'] != atom2['chain_id'] or atom2['chain_id'] != atom3['chain_id']\
                   or atom3['chain_id'] != atom4['chain_id']:
                    continue
                if self.__debug:
                    angleName = getTypeOfDihedralRestraint(peptide, nucleotide, carbohydrate,
                                                           [atom1, atom2, atom3, atom4])
                    print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} angleName={angleName} "
                          f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} {dstFunc}")

        finally:
            self.numberSelection.clear()

    def validateAngleRange(self, weight, target_value, lower_limit, upper_limit):
        """ Validate angle value range.
        """

        validRange = True
        dstFunc = {'weight': weight}

        if target_value is not None:
            if ANGLE_ERROR_MIN < target_value < ANGLE_ERROR_MAX:
                dstFunc['target_value'] = f"{target_value}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The target value='{target_value}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"

        if lower_limit is not None:
            if ANGLE_ERROR_MIN <= lower_limit < ANGLE_ERROR_MAX:
                dstFunc['lower_limit'] = f"{lower_limit}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower limit value='{lower_limit}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"

        if upper_limit is not None:
            if ANGLE_ERROR_MIN < upper_limit <= ANGLE_ERROR_MAX:
                dstFunc['upper_limit'] = f"{upper_limit}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"
        """
        if target_value is not None:

            if lower_limit is not None:
                if lower_limit > target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower limit value='{lower_limit}' must be less than the target value '{target_value}'.\n"

            if upper_limit is not None:
                if upper_limit < target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The upper limit value='{upper_limit}' must be grater than the target value '{target_value}'.\n"
        """
        if not validRange:
            return None

        if target_value is not None:
            if ANGLE_RANGE_MIN <= target_value <= ANGLE_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The target value='{target_value}' should be within range {ANGLE_RESTRAINT_RANGE}.\n"

        if lower_limit is not None:
            if ANGLE_RANGE_MIN <= lower_limit <= ANGLE_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The lower limit value='{lower_limit}' should be within range {ANGLE_RESTRAINT_RANGE}.\n"

        if upper_limit is not None:
            if ANGLE_RANGE_MIN <= upper_limit <= ANGLE_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit}' should be within range {ANGLE_RESTRAINT_RANGE}.\n"

        return dstFunc

    # Enter a parse tree produced by GromacsMRParser#orientation_restraints.
    def enterOrientation_restraints(self, ctx: GromacsMRParser.Orientation_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'rdc'

    # Exit a parse tree produced by GromacsMRParser#orientation_restraints.
    def exitOrientation_restraints(self, ctx: GromacsMRParser.Orientation_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by GromacsMRParser#orientation_restraint.
    def enterOrientation_restraint(self, ctx: GromacsMRParser.Orientation_restraintContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by GromacsMRParser#orientation_restraint.
    def exitOrientation_restraint(self, ctx: GromacsMRParser.Orientation_restraintContext):

        try:

            if None in self.numberSelection:
                return

            ai = int(str(ctx.Integer(0)))
            aj = int(str(ctx.Integer(1)))
            funct = int(str(ctx.Integer(2)))
            exp = int(str(ctx.Integer(3)))
            index = int(str(ctx.Integer(4)))

            alpha = self.numberSelection[0]
            # const = self.numberSelection[1]
            target_value = self.numberSelection[2]
            weight = self.numberSelection[3]

            if ai == aj:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                    f"Found zero RDC vector; (ai={ai}, aj={aj}).\n"
                return

            if funct != 1:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                    f"Unknown function type '{funct}' is set.\n"
                return

            if alpha != 3.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                    f"The 'alpha={alpha}' must be 3.0 for RDC restraints.\n"
                return

            if weight <= 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                    f"The relative weight value of '{weight}' must be a positive value.\n"
                return

            dstFunc = self.validateRdcRange(weight, exp, index, target_value, None, None)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            if self.__atomNumberDict is None:
                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                    "Failed to recognize GROMACS atom numbers in the restraint file "\
                    "because GROMACS parameter/topology file is not available.\n"
                return

            atomSelection = []

            if ai in self.__atomNumberDict:
                atomSelection.append(self.__atomNumberDict[ai])
                self.atomSelectionSet.append(atomSelection)
            else:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                    f"'ai={ai}' is not defined in the GROMACS parameter/topology file.\n"

            atomSelection.clear()

            if aj in self.__atomNumberDict:
                atomSelection.append(self.__atomNumberDict[aj])
                self.atomSelectionSet.append(atomSelection)
            else:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                    f"'aj={aj}' is not defined in the GROMACS parameter/topology file.\n"

            if len(self.atomSelectionSet) < 2:
                return

            chain_id_1 = self.atomSelectionSet[0][0]['chain_id']
            seq_id_1 = self.atomSelectionSet[0][0]['seq_id']
            comp_id_1 = self.atomSelectionSet[0][0]['comp_id']
            atom_id_1 = self.atomSelectionSet[0][0]['atom_id']

            chain_id_2 = self.atomSelectionSet[1][0]['chain_id']
            seq_id_2 = self.atomSelectionSet[1][0]['seq_id']
            comp_id_2 = self.atomSelectionSet[1][0]['comp_id']
            atom_id_2 = self.atomSelectionSet[1][0]['atom_id']

            if (atom_id_1[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS) or (atom_id_2[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS):
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                    f"Non-magnetic susceptible spin appears in RDC vector; "\
                    f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                    f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                return

            if chain_id_1 != chain_id_2:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                    f"Found inter-chain RDC vector; "\
                    f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                return

            if abs(seq_id_1 - seq_id_2) > 1:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                    f"Found inter-residue RDC vector; "\
                    f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                return

            if abs(seq_id_1 - seq_id_2) == 1:

                if self.__csStat.peptideLike(comp_id_1) and self.__csStat.peptideLike(comp_id_2) and\
                   ((seq_id_1 < seq_id_2 and atom_id_1 == 'C' and atom_id_2 in ('N', 'H')) or (seq_id_1 > seq_id_2 and atom_id_1 in ('N', 'H') and atom_id_2 == 'C')):
                    pass

                else:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                        "Found inter-residue RDC vector; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                    return

            elif atom_id_1 == atom_id_2:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                    "Found zero RDC vector; "\
                    f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                return

            else:

                if self.__ccU.updateChemCompDict(comp_id_1):  # matches with comp_id in CCD

                    if not any(b for b in self.__ccU.lastBonds
                               if ((b[self.__ccU.ccbAtomId1] == atom_id_1 and b[self.__ccU.ccbAtomId2] == atom_id_2)
                                   or (b[self.__ccU.ccbAtomId1] == atom_id_2 and b[self.__ccU.ccbAtomId2] == atom_id_1))):

                        if self.__nefT.validate_comp_atom(comp_id_1, atom_id_1) and self.__nefT.validate_comp_atom(comp_id_2, atom_id_2):
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                                "Found an RDC vector over multiple covalent bonds; "\
                                f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                            return

            self.updatePolySeqRstFromAtomSelectionSet()

            for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                  self.atomSelectionSet[1]):
                if atom1['chain_id'] != atom2['chain_id']:
                    continue
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} id={self.rdcRestraints} exp={exp} index={index} "
                          f"atom1={atom1} atom2={atom2} {dstFunc}")

        finally:
            self.numberSelection.clear()

    def validateRdcRange(self, exp, index, weight, target_value, lower_limit, upper_limit):
        """ Validate RDC value range.
        """

        validRange = True
        dstFunc = {'weight': weight}

        if target_value is not None:
            if RDC_ERROR_MIN < target_value < RDC_ERROR_MAX:
                dstFunc['target_value'] = f"{target_value}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                    f"The target value='{target_value}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if lower_limit is not None:
            if RDC_ERROR_MIN <= lower_limit < RDC_ERROR_MAX:
                dstFunc['lower_limit'] = f"{lower_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                    f"The lower limit value='{lower_limit:.3f}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if upper_limit is not None:
            if RDC_ERROR_MIN < upper_limit <= RDC_ERROR_MAX:
                dstFunc['upper_limit'] = f"{upper_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                    f"The upper limit value='{upper_limit:.3f}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if target_value is not None:

            if lower_limit is not None:
                if lower_limit > target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                        f"The lower limit value='{lower_limit:.3f}' must be less than the target value '{target_value}'.\n"

            if upper_limit is not None:
                if upper_limit < target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                        f"The upper limit value='{upper_limit:.3f}' must be grater than the target value '{target_value}'.\n"

        if not validRange:
            return None

        if target_value is not None:
            if RDC_RANGE_MIN <= target_value <= RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                    f"The target value='{target_value}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        if lower_limit is not None:
            if RDC_RANGE_MIN <= lower_limit <= RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                    f"The lower limit value='{lower_limit:.3f}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        if upper_limit is not None:
            if RDC_RANGE_MIN <= upper_limit <= RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                    f"The upper limit value='{upper_limit:.3f}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        return dstFunc

    # Enter a parse tree produced by GromacsMRParser#angle_restraints.
    def enterAngle_restraints(self, ctx: GromacsMRParser.Angle_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'ang'

    # Exit a parse tree produced by GromacsMRParser#angle_restraints.
    def exitAngle_restraints(self, ctx: GromacsMRParser.Angle_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by GromacsMRParser#angle_restraint.
    def enterAngle_restraint(self, ctx: GromacsMRParser.Angle_restraintContext):  # pylint: disable=unused-argument
        self.angRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by GromacsMRParser#angle_restraint.
    def exitAngle_restraint(self, ctx: GromacsMRParser.Angle_restraintContext):  # pylint: disable=unused-argument

        try:

            if None in self.numberSelection:
                return

            ai = int(str(ctx.Integer(0)))
            aj = int(str(ctx.Integer(1)))
            ak = int(str(ctx.Integer(2)))
            al = int(str(ctx.Integer(3)))
            funct = int(str(ctx.Integer(4)))
            mult = int(str(ctx.Integer(5)))

            target_value = self.numberSelection[0]
            delta = self.numberSelection[1]
            weight = 1.0

            lower_limit = target_value - delta
            upper_limit = target_value + delta

            len_atom_sorts = len(set(ai, aj, ak, al))

            if len_atom_sorts < 3 or ai == aj or ak == al:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Found zero angle vector; (ai={ai}, aj={aj}) - (ak={ak}, al={al}).\n"
                return

            if funct != 1:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Unknown function type '{funct}' is set.\n"
                return

            if mult <= 0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The multiplicity of angle restraint '{mult}' must be a positive integer.\n"
                return

            dstFunc = self.validateAngleRange(weight, target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            if self.__atomNumberDict is None:
                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                    "Failed to recognize GROMACS atom numbers in the restraint file "\
                    "because GROMACS parameter/topology file is not available.\n"
                return

            atomSelection = []

            if ai in self.__atomNumberDict:
                atomSelection.append(self.__atomNumberDict[ai])
                self.atomSelectionSet.append(atomSelection)
            else:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"'ai={ai}' is not defined in the GROMACS parameter/topology file.\n"

            atomSelection.clear()

            if aj in self.__atomNumberDict:
                atomSelection.append(self.__atomNumberDict[aj])
                self.atomSelectionSet.append(atomSelection)
            else:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"'aj={aj}' is not defined in the GROMACS parameter/topology file.\n"

            atomSelection.clear()

            if ak in self.__atomNumberDict:
                atomSelection.append(self.__atomNumberDict[ak])
                self.atomSelectionSet.append(atomSelection)
            else:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"'ak={ak}' is not defined in the GROMACS parameter/topology file.\n"

            atomSelection.clear()

            if al in self.__atomNumberDict:
                atomSelection.append(self.__atomNumberDict[al])
                self.atomSelectionSet.append(atomSelection)
            else:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"'al={al}' is not defined in the GROMACS parameter/topology file.\n"

            if len(self.atomSelectionSet) < 4:
                return

            self.updatePolySeqRstFromAtomSelectionSet()

            if len_atom_sorts == 3:
                if ai in (ak, al):
                    if ai == ak:
                        atom_order = [1, 0, 3]
                    else:
                        atom_order = [1, 0, 2]
                else:
                    if aj == ak:
                        atom_order = [0, 1, 3]
                    else:
                        atom_order = [0, 1, 2]

                for atom1, atom2, atom3 in itertools.product(self.atomSelectionSet[atom_order[0]],
                                                             self.atomSelectionSet[atom_order[1]],
                                                             self.atomSelectionSet[atom_order[2]]):
                    if atom1['chain_id'] != atom2['chain_id'] or atom2['chain_id'] != atom3['chain_id']:
                        continue
                    if self.__debug:
                        print(f"subtype={self.__cur_subtype} id={self.angRestraints} mult={mult} "
                              f"atom1={atom1} atom2={atom2} atom3={atom3} {dstFunc}")

            else:

                for atom1, atom2, atom3, atom4 in itertools.product(self.atomSelectionSet[0],
                                                                    self.atomSelectionSet[1],
                                                                    self.atomSelectionSet[2],
                                                                    self.atomSelectionSet[3]):
                    if atom1['chain_id'] != atom2['chain_id'] or atom2['chain_id'] != atom3['chain_id']\
                       or atom3['chain_id'] != atom4['chain_id']:
                        continue
                    if self.__debug:
                        print(f"subtype={self.__cur_subtype} id={self.angRestraints} mult={mult} "
                              f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} {dstFunc}")

        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by GromacsMRParser#angle_restraints_z.
    def enterAngle_restraints_z(self, ctx: GromacsMRParser.Angle_restraints_zContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'ang'

    # Exit a parse tree produced by GromacsMRParser#angle_restraints_z.
    def exitAngle_restraints_z(self, ctx: GromacsMRParser.Angle_restraints_zContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by GromacsMRParser#angle_restraint_z.
    def enterAngle_restraint_z(self, ctx: GromacsMRParser.Angle_restraint_zContext):  # pylint: disable=unused-argument
        self.angRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by GromacsMRParser#angle_restraint_z.
    def exitAngle_restraint_z(self, ctx: GromacsMRParser.Angle_restraint_zContext):

        try:

            if None in self.numberSelection:
                return

            ai = int(str(ctx.Integer(0)))
            aj = int(str(ctx.Integer(1)))
            funct = int(str(ctx.Integer(2)))
            mult = int(str(ctx.Integer(3)))

            target_value = self.numberSelection[0]
            delta = self.numberSelection[1]
            weight = 1.0

            lower_limit = target_value - delta
            upper_limit = target_value + delta

            if ai == aj:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Found zero angle vector; (ai={ai}, aj={aj}).\n"
                return

            if funct != 1:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Unknown function type '{funct}' is set.\n"
                return

            if mult <= 0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The multiplicity of angle restraint '{mult}' must be a positive integer.\n"
                return

            dstFunc = self.validateAngleRange(weight, target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            if self.__atomNumberDict is None:
                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                    "Failed to recognize GROMACS atom numbers in the restraint file "\
                    "because GROMACS parameter/topology file is not available.\n"
                return

            atomSelection = []

            if ai in self.__atomNumberDict:
                atomSelection.append(self.__atomNumberDict[ai])
                self.atomSelectionSet.append(atomSelection)
            else:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"'ai={ai}' is not defined in the GROMACS parameter/topology file.\n"

            atomSelection.clear()

            if aj in self.__atomNumberDict:
                atomSelection.append(self.__atomNumberDict[aj])
                self.atomSelectionSet.append(atomSelection)
            else:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"'aj={aj}' is not defined in the GROMACS parameter/topology file.\n"

            if len(self.atomSelectionSet) < 2:
                return

            self.updatePolySeqRstFromAtomSelectionSet()

            for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                  self.atomSelectionSet[1]):
                if atom1['chain_id'] != atom2['chain_id']:
                    continue
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} id={self.angRestraints} mult={mult} "
                          f"atom1={atom1} atom2={atom2} z-axis {dstFunc}")

        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by GromacsMRParser#position_restraints.
    def enterPosition_restraints(self, ctx: GromacsMRParser.Position_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'geo'

    # Exit a parse tree produced by GromacsMRParser#position_restraints.
    def exitPosition_restraints(self, ctx: GromacsMRParser.Position_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by GromacsMRParser#position_restraint.
    def enterPosition_restraint(self, ctx: GromacsMRParser.Position_restraintContext):  # pylint: disable=unused-argument
        self.geoRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by GromacsMRParser#position_restraint.
    def exitPosition_restraint(self, ctx: GromacsMRParser.Position_restraintContext):

        try:

            if None in self.numberSelection:
                return

            ai = int(str(ctx.Integer(0)))
            funct = int(str(ctx.Integer(1)))

            a = self.numberSelection[0]
            b = self.numberSelection[1]
            c = self.numberSelection[2]

            if funct not in (1, 2):
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Unknown function type '{funct}' is set.\n"
                return

            if not self.__hasPolySeq:
                return

            if self.__atomNumberDict is None:
                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                    "Failed to recognize GROMACS atom numbers in the restraint file "\
                    "because GROMACS parameter/topology file is not available.\n"
                return

            atomSelection = []

            if ai in self.__atomNumberDict:
                atomSelection.append(self.__atomNumberDict[ai])
                self.atomSelectionSet.append(atomSelection)
            else:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"'ai={ai}' is not defined in the GROMACS parameter/topology file.\n"

            if len(self.atomSelectionSet) < 1:
                return

            self.updatePolySeqRstFromAtomSelectionSet()

            for atom1 in self.atomSelectionSet[0]:
                if self.__debug:
                    if funct == 1:
                        print(f"subtype={self.__cur_subtype} id={self.angRestraints} "
                              f"atom={atom1} (kx, ky, kz)=({a}, {b}, {c})")
                    else:
                        print(f"subtype={self.__cur_subtype} id={self.angRestraints} "
                              f"atom={atom1} (g, r, k)=({a}, {b}, {c})")

        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by GromacsMRParser#number.
    def enterNumber(self, ctx: GromacsMRParser.NumberContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by GromacsMRParser#number.
    def exitNumber(self, ctx: GromacsMRParser.NumberContext):
        if ctx.Float():
            self.numberSelection.append(float(str(ctx.Float())))

        elif ctx.Integer():
            self.numberSelection.append(float(str(ctx.Integer())))

        else:
            self.numberSelection.append(None)

    def updatePolySeqRstFromAtomSelectionSet(self):
        """ Update polymer sequence of the current MR file.
        """

        if len(self.atomSelectionSet) == 0:
            return

        for atomSelection in self.atomSelectionSet:
            if len(atomSelection) == 0:
                continue
            for atom in atomSelection:
                chainId = atom['chain_id']
                seqId = atom['seq_id']

                ps = next((ps for ps in self.__polySeqRst if ps['chain_id'] == chainId), None)
                if ps is None:
                    self.__polySeqRst.append({'chain_id': chainId, 'seq_id': [], 'comp_id': []})
                    ps = self.__polySeqRst[-1]

                if seqId not in ps['seq_id']:
                    ps['seq_id'].append(seqId)
                    ps['comp_id'].append(atom['comp_id'])

    def sortPolySeqRst(self):
        """ Sort polymer sequence of the current MR file by sequence number.
        """

        if not self.__hasPolySeq or self.__polySeqRst is None:
            return

        for ps in self.__polySeqRst:
            minSeqId = min(ps['seq_id'])
            maxSeqId = max(ps['seq_id'])

            _seqIds = list(range(minSeqId, maxSeqId + 1))
            _compIds = ["."] * (maxSeqId - minSeqId + 1)

            for idx, seqId in enumerate(ps['seq_id']):
                _compIds[_seqIds.index(seqId)] = ps['comp_id'][idx]

            ps['seq_id'] = _seqIds
            ps['comp_id'] = _compIds

    def alignPolymerSequence(self):
        if not self.__hasPolySeq or self.__polySeqRst is None:
            return

        self.__seqAlign = []

        for s1 in self.__polySeq:
            chain_id = s1['auth_chain_id']

            for s2 in self.__polySeqRst:
                chain_id2 = s2['chain_id']

                self.__pA.setReferenceSequence(s1['comp_id'], 'REF' + chain_id)
                self.__pA.addTestSequence(s2['comp_id'], chain_id)
                self.__pA.doAlign()

                myAlign = self.__pA.getAlignment(chain_id)

                length = len(myAlign)

                if length == 0:
                    continue

                _matched, unmapped, conflict, offset_1, offset_2 = getScoreOfSeqAlign(myAlign)

                if length == unmapped + conflict or _matched <= conflict:
                    continue

                _s1 = s1 if offset_1 == 0 else fillBlankCompIdWithOffset(s1, offset_1)
                _s2 = s2 if offset_2 == 0 else fillBlankCompIdWithOffset(s2, offset_2)

                if conflict > 0 and hasLargeSeqGap(_s1, _s2):
                    __s1, __s2 = beautifyPolySeq(_s1, _s2)
                    _s1_ = __s1
                    _s2_ = __s2

                    self.__pA.setReferenceSequence(_s1_['comp_id'], 'REF' + chain_id)
                    self.__pA.addTestSequence(_s2_['comp_id'], chain_id)
                    self.__pA.doAlign()

                    myAlign = self.__pA.getAlignment(chain_id)

                    length = len(myAlign)

                    _matched, unmapped, _conflict, _offset_1, _offset_2 = getScoreOfSeqAlign(myAlign)

                    if _conflict == 0 and len(__s2['comp_id']) - len(s2['comp_id']) == conflict:
                        conflict = 0
                        offset_1 = _offset_1
                        offset_2 = _offset_2
                        _s1 = __s1
                        _s2 = __s2

                ref_length = len(s1['seq_id'])

                ref_code = getOneLetterCodeSequence(_s1['comp_id'])
                test_code = getOneLetterCodeSequence(_s2['comp_id'])
                mid_code = getMiddleCode(ref_code, test_code)
                ref_gauge_code = getGaugeCode(_s1['seq_id'])
                test_gauge_code = getGaugeCode(_s2['seq_id'])

                if any((__s1, __s2) for (__s1, __s2, __c1, __c2)
                       in zip(_s1['seq_id'], _s2['seq_id'], _s1['comp_id'], _s2['comp_id'])
                       if __c1 != '.' and __c2 != '.' and __c1 != __c2):
                    seq_id1 = []
                    seq_id2 = []
                    comp_id1 = []
                    comp_id2 = []
                    idx1 = 0
                    idx2 = 0
                    for i in range(length):
                        myPr = myAlign[i]
                        myPr0 = str(myPr[0])
                        myPr1 = str(myPr[1])
                        if myPr0 != '.':
                            while idx1 < len(_s1['seq_id']):
                                if _s1['comp_id'][idx1] == myPr0:
                                    seq_id1.append(_s1['seq_id'][idx1])
                                    comp_id1.append(myPr0)
                                    idx1 += 1
                                    break
                                idx1 += 1
                        else:
                            seq_id1.append(None)
                            comp_id1.append('.')
                        if myPr1 != '.':
                            while idx2 < len(_s2['seq_id']):
                                if _s2['comp_id'][idx2] == myPr1:
                                    seq_id2.append(_s2['seq_id'][idx2])
                                    comp_id2.append(myPr1)
                                    idx2 += 1
                                    break
                                idx2 += 1
                        else:
                            seq_id2.append(None)
                            comp_id2.append('.')
                    ref_code = getOneLetterCodeSequence(comp_id1)
                    test_code = getOneLetterCodeSequence(comp_id2)
                    mid_code = getMiddleCode(ref_code, test_code)
                    ref_gauge_code = getGaugeCode(seq_id1, offset_1)
                    test_gauge_code = getGaugeCode(seq_id2, offset_2)
                    if ' ' in ref_gauge_code:
                        for p, g in enumerate(ref_gauge_code):
                            if g == ' ':
                                ref_code = ref_code[0:p] + '-' + ref_code[p + 1:]
                    if ' ' in test_gauge_code:
                        for p, g in enumerate(test_gauge_code):
                            if g == ' ':
                                test_code = test_code[0:p] + '-' + test_code[p + 1:]

                matched = mid_code.count('|')

                seq_align = {'ref_chain_id': chain_id, 'test_chain_id': chain_id2, 'length': ref_length,
                             'matched': matched, 'conflict': conflict, 'unmapped': unmapped,
                             'sequence_coverage': float(f"{float(length - (unmapped + conflict)) / ref_length:.3f}"),
                             'ref_seq_id': _s1['seq_id'], 'test_seq_id': _s2['seq_id'],
                             'ref_gauge_code': ref_gauge_code, 'ref_code': ref_code, 'mid_code': mid_code,
                             'test_code': test_code, 'test_gauge_code': test_gauge_code}

                self.__seqAlign.append(seq_align)

    def assignPolymerSequence(self):
        if self.__seqAlign is None:
            return

        mr_chains = len(self.__polySeqRst)

        mat = []
        indices = []

        for s1 in self.__polySeq:
            chain_id = s1['auth_chain_id']

            cost = [0 for i in range(mr_chains)]

            for s2 in self.__polySeqRst:
                chain_id2 = s2['chain_id']

                result = next((seq_align for seq_align in self.__seqAlign
                               if seq_align['ref_chain_id'] == chain_id
                               and seq_align['test_chain_id'] == chain_id2), None)

                if result is not None:
                    cost[self.__polySeqRst.index(s2)] = result['unmapped'] + result['conflict'] - result['length']
                    if result['length'] >= len(s1['seq_id']) - result['unmapped']:
                        indices.append((self.__polySeq.index(s1), self.__polySeqRst.index(s2)))

            mat.append(cost)

        self.__chainAssign = []

        for row, column in indices:

            if mat[row][column] >= 0:
                _cif_chains = []
                for _row, _column in indices:
                    if column == _column:
                        _cif_chains.append(self.__polySeq[_row]['auth_chain_id'])

                if len(_cif_chains) > 1:
                    chain_id2 = self.__polySeqRst[column]['chain_id']

                    self.warningMessage += f"[Concatenated sequence] The chain ID {chain_id2!r} of the sequences in the GROMACS restraint file "\
                        f"will be re-assigned to the chain IDs {_cif_chains} in the coordinates during biocuration.\n"

            chain_id = self.__polySeq[row]['auth_chain_id']
            chain_id2 = self.__polySeqRst[column]['chain_id']

            result = next(seq_align for seq_align in self.__seqAlign
                          if seq_align['ref_chain_id'] == chain_id and seq_align['test_chain_id'] == chain_id2)

            chain_assign = {'ref_chain_id': chain_id, 'test_chain_id': chain_id2, 'length': result['length'],
                            'matched': result['matched'], 'conflict': result['conflict'], 'unmapped': result['unmapped'],
                            'sequence_coverage': result['sequence_coverage']}

            s1 = next(s for s in self.__polySeq if s['auth_chain_id'] == chain_id)
            s2 = next(s for s in self.__polySeqRst if s['chain_id'] == chain_id2)

            self.__pA.setReferenceSequence(s1['comp_id'], 'REF' + chain_id)
            self.__pA.addTestSequence(s2['comp_id'], chain_id)
            self.__pA.doAlign()

            myAlign = self.__pA.getAlignment(chain_id)

            length = len(myAlign)

            _matched, unmapped, conflict, offset_1, offset_2 = getScoreOfSeqAlign(myAlign)

            _s1 = s1 if offset_1 == 0 else fillBlankCompIdWithOffset(s1, offset_1)
            _s2 = s2 if offset_2 == 0 else fillBlankCompIdWithOffset(s2, offset_2)

            if conflict > 0 and hasLargeSeqGap(_s1, _s2):
                __s1, __s2 = beautifyPolySeq(_s1, _s2)
                _s1 = __s1
                _s2 = __s2

                self.__pA.setReferenceSequence(_s1['comp_id'], 'REF' + chain_id)
                self.__pA.addTestSequence(_s2['comp_id'], chain_id)
                self.__pA.doAlign()

                myAlign = self.__pA.getAlignment(chain_id)

                length = len(myAlign)

                _matched, unmapped, _conflict, _, _ = getScoreOfSeqAlign(myAlign)

                if _conflict == 0 and len(__s2['comp_id']) - len(s2['comp_id']) == conflict:
                    result['conflict'] = 0
                    s2 = __s2

            if result['unmapped'] > 0 or result['conflict'] > 0:

                aligned = [True] * length
                seq_id1 = []
                seq_id2 = []

                j = 0
                for i in range(length):
                    if str(myAlign[i][0]) != '.':
                        seq_id1.append(s1['seq_id'][j])
                        j += 1
                    else:
                        seq_id1.append(None)

                j = 0
                for i in range(length):
                    if str(myAlign[i][1]) != '.':
                        seq_id2.append(s2['seq_id'][j])
                        j += 1
                    else:
                        seq_id2.append(None)

                for i in range(length):
                    myPr = myAlign[i]
                    myPr0 = str(myPr[0])
                    myPr1 = str(myPr[1])
                    if myPr0 == '.' or myPr1 == '.':
                        aligned[i] = False
                    elif myPr0 != myPr1:
                        pass
                    else:
                        break

                for i in reversed(range(length)):
                    myPr = myAlign[i]
                    myPr0 = str(myPr[0])
                    myPr1 = str(myPr[1])
                    if myPr0 == '.' or myPr1 == '.':
                        aligned[i] = False
                    elif myPr0 != myPr1:
                        pass
                    else:
                        break

                _conflicts = 0

                for i in range(length):
                    myPr = myAlign[i]
                    if myPr[0] == myPr[1]:
                        continue

                    cif_comp_id = str(myPr[0])
                    mr_comp_id = str(myPr[1])

                    if mr_comp_id == '.' and cif_comp_id != '.':
                        pass

                    elif mr_comp_id != cif_comp_id and aligned[i]:
                        _conflicts += 1

                # if _conflicts > chain_assign['unmapped'] and chain_assign['sequence_coverage'] < self.min_seq_coverage_w_conflict:
                #    continue

                if _conflicts + offset_1 > _matched and chain_assign['sequence_coverage'] < self.low_seq_coverage:  # DAOTHER-7825 (2lyw)
                    continue

                unmapped = []
                conflict = []

                for i in range(length):
                    myPr = myAlign[i]
                    if myPr[0] == myPr[1]:
                        continue

                    cif_comp_id = str(myPr[0])
                    mr_comp_id = str(myPr[1])

                    if mr_comp_id == '.' and cif_comp_id != '.':

                        unmapped.append({'ref_seq_id': seq_id1[i], 'ref_comp_id': cif_comp_id})
                        """ unmapped residue is not error
                        if not aligned[i]:

                            if not self.__ccU.updateChemCompDict(cif_comp_id):
                                continue

                            if self.__ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] != 'REL':
                                continue

                            cif_seq_code = f"{chain_id}:{seq_id1[i]}:{cif_comp_id}"

                            self.warningMessage += f"[Sequence mismatch] {cif_seq_code} is not present "\
                                f"in the GROMACS restraint data (chain_id {chain_id2}).\n"
                        """
                    elif mr_comp_id != cif_comp_id and aligned[i]:

                        conflict.append({'ref_seq_id': seq_id1[i], 'ref_comp_id': cif_comp_id,
                                         'test_seq_id': seq_id2[i], 'test_comp_id': mr_comp_id})

                        cif_seq_code = f"{chain_id}:{seq_id1[i]}:{cif_comp_id}"
                        if cif_comp_id == '.':
                            cif_seq_code += ', insertion error'
                        mr_seq_code = f"{chain_id2}:{seq_id2[i]}:{mr_comp_id}"
                        if mr_comp_id == '.':
                            mr_seq_code += ', insertion error'

                        if cif_comp_id != '.':

                            if not self.__ccU.updateChemCompDict(cif_comp_id):
                                continue

                            if self.__ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] != 'REL':
                                continue

                        self.warningMessage += f"[Sequence mismatch] Sequence alignment error between the coordinate ({cif_seq_code}) "\
                            f"and the GROMACS restraint data ({mr_seq_code}). "\
                            "Please verify the two sequences and re-upload the correct file(s) if required.\n"

                if len(unmapped) > 0:
                    chain_assign['unmapped_sequence'] = unmapped

                if len(conflict) > 0:
                    chain_assign['conflict_sequence'] = conflict
                    chain_assign['conflict'] = len(conflict)
                    chain_assign['unmapped'] = chain_assign['unmapped'] - len(conflict)
                    if chain_assign['unmapped'] < 0:
                        chain_assign['conflict'] -= chain_assign['unmapped']
                        chain_assign['unmapped'] = 0

                    result['conflict'] = chain_assign['conflict']
                    result['unmapped'] = chain_assign['unmapped']

            self.__chainAssign.append(chain_assign)

        if len(self.__chainAssign) > 0:

            if len(self.__polySeq) > 1:

                if any(s for s in self.__polySeq if 'identical_chain_id' in s):

                    for chain_assign in self.__chainAssign:

                        if chain_assign['conflict'] > 0:
                            continue

                        chain_id = chain_assign['ref_chain_id']

                        try:
                            identity = next(s['identical_chain_id'] for s in self.__polySeq
                                            if s['auth_chain_id'] == chain_id and 'identical_chain_id' in s)

                            for chain_id in identity:

                                if not any(_chain_assign for _chain_assign in self.__chainAssign if _chain_assign['ref_chain_id'] == chain_id):
                                    _chain_assign = copy.copy(chain_assign)
                                    _chain_assign['ref_chain_id'] = chain_id
                                    self.__chainAssign.append(_chain_assign)

                        except StopIteration:
                            pass

    def trimPolymerSequence(self):
        if self.__seqAlign is None or self.__chainAssign is None:
            return

        uneffSeqAlignIdx = list(range(len(self.__seqAlign) - 1, -1, -1))

        for chain_assign in self.__chainAssign:
            ref_chain_id = chain_assign['ref_chain_id']
            test_chain_id = chain_assign['test_chain_id']

            effSeqAligIdx = next((idx for idx, seq_align in enumerate(self.__seqAlign)
                                  if seq_align['ref_chain_id'] == ref_chain_id
                                  and seq_align['test_chain_id'] == test_chain_id), None)

            if effSeqAligIdx is not None:
                uneffSeqAlignIdx.remove(effSeqAligIdx)

        if len(uneffSeqAlignIdx) > 0:
            for idx in uneffSeqAlignIdx:
                del self.__seqAlign[idx]

    def __getCurrentRestraint(self, dataset=None, n=None):
        if self.__cur_subtype == 'dist':
            return f"[Check the {self.distRestraints}th row of distance restraints (index={n})] "
        if self.__cur_subtype == 'ang':
            return f"[Check the {self.angRestraints}th row of angle restraints] "
        if self.__cur_subtype == 'dihed':
            return f"[Check the {self.dihedRestraints}th row of dihedral angle restraints] "
        if self.__cur_subtype == 'rdc':
            return f"[Check the {n}th row of residual dipolar coupling restraints (exp={dataset})] "
        if self.__cur_subtype == 'geo':
            return f"[Check the {self.geoRestraints}th row of coordinate geometry restraints] "
        return ''

    def getContentSubtype(self):
        """ Return content subtype of GROMACS MR file.
        """

        contentSubtype = {'dist_restraint': self.distRestraints,
                          'ang_restraint': self.angRestraints,
                          'dihed_restraint': self.dihedRestraints,
                          'geo_restraint': self.geoRestraints
                          }

        return {k: 1 for k, v in contentSubtype.items() if v > 0}

    def getPolymerSequence(self):
        """ Return polymer sequence of GROMACS MR file.
        """
        return self.__polySeqRst

    def getSequenceAlignment(self):
        """ Return sequence alignment between coordinates and GROMACS MR.
        """
        return self.__seqAlign

    def getChainAssignment(self):
        """ Return chain assignment between coordinates and GROMACS MR.
        """
        return self.__chainAssign


# del GromacsMRParser
