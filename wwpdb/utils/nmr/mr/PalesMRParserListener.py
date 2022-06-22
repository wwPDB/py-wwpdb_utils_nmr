##
# File: PalesMRParserListener.py
# Date: 17-Jun-2022
#
# Updates:
# Generated from PalesMRParser.g4 by ANTLR 4.10.1
""" ParserLister class for PALES (DYNAMO) MR files.
    @author: Masashi Yokochi
"""
import sys
import itertools
import copy

from antlr4 import ParseTreeListener

try:
    from wwpdb.utils.align.alignlib import PairwiseAlign  # pylint: disable=no-name-in-module
    from wwpdb.utils.nmr.mr.PalesMRParser import PalesMRParser
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (checkCoordinates,
                                                       getTypeOfDihedralRestraint,
                                                       translateToStdResName,
                                                       translateToStdAtomName,
                                                       REPRESENTATIVE_MODEL_ID,
                                                       DIST_RESTRAINT_RANGE,
                                                       DIST_RESTRAINT_ERROR,
                                                       ANGLE_RESTRAINT_RANGE,
                                                       ANGLE_RESTRAINT_ERROR,
                                                       RDC_RESTRAINT_RANGE,
                                                       RDC_RESTRAINT_ERROR,
                                                       KNOWN_ANGLE_ATOM_NAMES,
                                                       KNOWN_ANGLE_SEQ_OFFSET)
    from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
    from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from wwpdb.utils.nmr.NEFTranslator.NEFTranslator import (NEFTranslator,
                                                             ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS)
    from wwpdb.utils.nmr.AlignUtil import (monDict3,
                                           hasLargeSeqGap,
                                           fillBlankCompIdWithOffset, beautifyPolySeq,
                                           getMiddleCode, getGaugeCode, getScoreOfSeqAlign,
                                           getOneLetterCodeSequence)
except ImportError:
    from nmr.align.alignlib import PairwiseAlign  # pylint: disable=no-name-in-module
    from nmr.mr.PalesMRParser import PalesMRParser
    from nmr.mr.ParserListenerUtil import (checkCoordinates,
                                           getTypeOfDihedralRestraint,
                                           translateToStdResName,
                                           translateToStdAtomName,
                                           REPRESENTATIVE_MODEL_ID,
                                           DIST_RESTRAINT_RANGE,
                                           DIST_RESTRAINT_ERROR,
                                           ANGLE_RESTRAINT_RANGE,
                                           ANGLE_RESTRAINT_ERROR,
                                           RDC_RESTRAINT_RANGE,
                                           RDC_RESTRAINT_ERROR,
                                           KNOWN_ANGLE_ATOM_NAMES,
                                           KNOWN_ANGLE_SEQ_OFFSET)
    from nmr.ChemCompUtil import ChemCompUtil
    from nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from nmr.NEFTranslator.NEFTranslator import (NEFTranslator,
                                                 ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS)
    from nmr.AlignUtil import (monDict3,
                               hasLargeSeqGap,
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


TALOS_PREDICTION_CLASSES = ('Strong', 'Good', 'Generous', 'Warn', 'Bad', 'None')
TALOS_PREDICTION_MIN_CLASSES = ('Strong', 'Good')


# This class defines a complete listener for a parse tree produced by PalesMRParser.
class PalesMRParserListener(ParseTreeListener):

    # __verbose = None
    # __lfh = None
    __debug = False
    __remediate = False
    __omitDistLimitOutlier = True

    distRestraints = 0      # DYNAMO: Distance restraints
    dihedRestraints = 0     # DYNAMO: Torsion angle restraints
    rdcRestraints = 0       # PALES/DYNAMO: Residual dipolar coupling restraints
    jcoupRestraints = 0     # DYNAMO: Scalar coupling constant restraints

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

    # reasons for re-parsing request from the previous trial
    __reasons = None

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
    __altPolySeq = None
    __coordAtomSite = None
    __coordUnobsRes = None
    __labelToAuthSeq = None
    __authToLabelSeq = None

    __hasPolySeq = False
    __preferAuthSeq = True

    # chain number dictionary
    __chainNumberDict = None

    # polymer sequence of MR file
    __polySeqRst = None

    __seqAlign = None
    __chainAssign = None

    # current restraint subtype
    __cur_subtype = ''

    # collection of atom selection
    atomSelectionSet = []

    # collection of auxiliary atom selection
    auxAtomSelectionSet = []

    # collection of number selection
    numberSelection = []

    warningMessage = ''

    reasonsForReParsing = None

    def __init__(self, verbose=True, log=sys.stdout,
                 representativeModelId=REPRESENTATIVE_MODEL_ID,
                 cR=None, cC=None, ccU=None, csStat=None, nefT=None,
                 reasons=None):
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
            self.__altPolySeq = ret['alt_polymer_sequence']
            self.__coordAtomSite = ret['coord_atom_site']
            self.__coordUnobsRes = ret['coord_unobs_res']
            self.__labelToAuthSeq = ret['label_to_auth_seq']
            self.__authToLabelSeq = ret['auth_to_label_seq']

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

        # reasons for re-parsing request from the previous trial
        self.__reasons = reasons

    def setDebugMode(self, debug):
        self.__debug = debug

    # Enter a parse tree produced by PalesMRParser#pales_mr.
    def enterPales_mr(self, ctx: PalesMRParser.Pales_mrContext):  # pylint: disable=unused-argument
        self.__chainNumberDict = {}
        self.__polySeqRst = []

    # Exit a parse tree produced by PalesMRParser#pales_mr.
    def exitPales_mr(self, ctx: PalesMRParser.Pales_mrContext):  # pylint: disable=unused-argument
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

    # Enter a parse tree produced by PalesMRParser#sequence.
    def enterSequence(self, ctx: PalesMRParser.SequenceContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by PalesMRParser#sequence.
    def exitSequence(self, ctx: PalesMRParser.SequenceContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by PalesMRParser#distance_restraints.
    def enterDistance_restraints(self, ctx: PalesMRParser.Distance_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dist'

    # Exit a parse tree produced by PalesMRParser#distance_restraints.
    def exitDistance_restraints(self, ctx: PalesMRParser.Distance_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by PalesMRParser#distance_restraint.
    def enterDistance_restraint(self, ctx: PalesMRParser.Distance_restraintContext):  # pylint: disable=unused-argument
        self.distRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by PalesMRParser#distance_restraint.
    def exitDistance_restraint(self, ctx: PalesMRParser.Distance_restraintContext):

        try:

            index = int(str(ctx.Integer(0)))
            group = int(str(ctx.Integer(1)))

            seqId1 = int(str(ctx.Integer(2)))
            compId1 = str(ctx.Simple_name(0)).upper()
            atomId1 = str(ctx.Simple_name(1)).upper()
            seqId2 = int(str(ctx.Integer(3)))
            compId2 = str(ctx.Simple_name(2)).upper()
            atomId2 = str(ctx.Simple_name(3)).upper()

            target_value = None
            lower_limit = None
            upper_limit = None

            if None in self.numberSelection:
                return

            lower_limit = self.numberSelection[0]
            upper_limit = self.numberSelection[1]
            # fource_const = self.numberSelection[2]
            weight = self.numberSelection[3]
            scale = self.numberSelection[4]

            if weight <= 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"The relative weight value of '{weight}' must be a positive value.\n"
                return

            if scale <= 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"The relative scale value of '{scale}' must be a positive value.\n"
                return

            dstFunc = self.validateDistanceRange(index, group, weight, scale, target_value, lower_limit, upper_limit, self.__omitDistLimitOutlier)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            chainAssign1 = self.assignCoordPolymerSequence(None, seqId1, compId1, atomId1, index, group)
            chainAssign2 = self.assignCoordPolymerSequence(None, seqId2, compId2, atomId2, index, group)

            if len(chainAssign1) == 0 or len(chainAssign2) == 0:
                return

            self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1, True, index, group)
            self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2, True, index, group)

            if len(self.atomSelectionSet) < 2:
                return

            for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                  self.atomSelectionSet[1]):
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} id={self.distRestraints} (index={index}, group={group}) "
                          f"atom1={atom1} atom2={atom2} {dstFunc}")

        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by PalesMRParser#distance_restraints_sw_segid.
    def enterDistance_restraints_sw_segid(self, ctx: PalesMRParser.Distance_restraints_sw_segidContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dist'

    # Exit a parse tree produced by PalesMRParser#distance_restraints_sw_segid.
    def exitDistance_restraints_sw_segid(self, ctx: PalesMRParser.Distance_restraints_sw_segidContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by PalesMRParser#distance_restraint_sw_segid.
    def enterDistance_restraint_sw_segid(self, ctx: PalesMRParser.Distance_restraint_sw_segidContext):  # pylint: disable=unused-argument
        self.distRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by PalesMRParser#distance_restraint_sw_segid.
    def exitDistance_restraint_sw_segid(self, ctx: PalesMRParser.Distance_restraint_sw_segidContext):

        try:

            index = int(str(ctx.Integer(0)))
            group = int(str(ctx.Integer(1)))

            chainId1 = str(ctx.Simple_name(0))
            seqId1 = int(str(ctx.Integer(2)))
            compId1 = str(ctx.Simple_name(1)).upper()
            atomId1 = str(ctx.Simple_name(2)).upper()
            chainId2 = str(ctx.Simple_name(3))
            seqId2 = int(str(ctx.Integer(3)))
            compId2 = str(ctx.Simple_name(4)).upper()
            atomId2 = str(ctx.Simple_name(5)).upper()

            target_value = None
            lower_limit = None
            upper_limit = None

            if None in self.numberSelection:
                return

            lower_limit = self.numberSelection[0]
            upper_limit = self.numberSelection[1]
            # fource_const = self.numberSelection[2]
            weight = self.numberSelection[3]
            scale = self.numberSelection[4]

            if weight <= 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"The relative weight value of '{weight}' must be a positive value.\n"
                return

            if scale <= 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"The relative scale value of '{scale}' must be a positive value.\n"
                return

            dstFunc = self.validateDistanceRange(index, group, weight, scale, target_value, lower_limit, upper_limit, self.__omitDistLimitOutlier)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            chainAssign1 = self.assignCoordPolymerSequence(chainId1, seqId1, compId1, atomId1, index, group)
            chainAssign2 = self.assignCoordPolymerSequence(chainId2, seqId2, compId2, atomId2, index, group)

            if len(chainAssign1) == 0 or len(chainAssign2) == 0:
                return

            self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1, True, index, group)
            self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2, True, index, group)

            if len(self.atomSelectionSet) < 2:
                return

            for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                  self.atomSelectionSet[1]):
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} id={self.distRestraints} (index={index}, group={group}) "
                          f"atom1={atom1} atom2={atom2} {dstFunc}")

        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by PalesMRParser#distance_restraints_ew_segid.
    def enterDistance_restraints_ew_segid(self, ctx: PalesMRParser.Distance_restraints_ew_segidContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dist'

    # Exit a parse tree produced by PalesMRParser#distance_restraints_ew_segid.
    def exitDistance_restraints_ew_segid(self, ctx: PalesMRParser.Distance_restraints_ew_segidContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by PalesMRParser#distance_restraint_ew_segid.
    def enterDistance_restraint_ew_segid(self, ctx: PalesMRParser.Distance_restraint_ew_segidContext):  # pylint: disable=unused-argument
        self.distRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by PalesMRParser#distance_restraint_ew_segid.
    def exitDistance_restraint_ew_segid(self, ctx: PalesMRParser.Distance_restraint_ew_segidContext):

        try:

            index = int(str(ctx.Integer(0)))
            group = int(str(ctx.Integer(1)))

            seqId1 = int(str(ctx.Integer(2)))
            compId1 = str(ctx.Simple_name(0)).upper()
            atomId1 = str(ctx.Simple_name(1)).upper()
            chainId1 = str(ctx.Simple_name(2))
            chainId2 = str(ctx.Simple_name(5))
            seqId2 = int(str(ctx.Integer(3)))
            compId2 = str(ctx.Simple_name(3)).upper()
            atomId2 = str(ctx.Simple_name(4)).upper()
            chainId2 = str(ctx.Simple_name(5))

            target_value = None
            lower_limit = None
            upper_limit = None

            if None in self.numberSelection:
                return

            lower_limit = self.numberSelection[0]
            upper_limit = self.numberSelection[1]
            # fource_const = self.numberSelection[2]
            weight = self.numberSelection[3]
            scale = self.numberSelection[4]

            if weight <= 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"The relative weight value of '{weight}' must be a positive value.\n"
                return

            if scale <= 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"The relative scale value of '{scale}' must be a positive value.\n"
                return

            dstFunc = self.validateDistanceRange(index, group, weight, scale, target_value, lower_limit, upper_limit, self.__omitDistLimitOutlier)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            chainAssign1 = self.assignCoordPolymerSequence(chainId1, seqId1, compId1, atomId1, index, group)
            chainAssign2 = self.assignCoordPolymerSequence(chainId2, seqId2, compId2, atomId2, index, group)

            if len(chainAssign1) == 0 or len(chainAssign2) == 0:
                return

            self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1, True, index, group)
            self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2, True, index, group)

            if len(self.atomSelectionSet) < 2:
                return

            for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                  self.atomSelectionSet[1]):
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} id={self.distRestraints} (index={index}, group={group}) "
                          f"atom1={atom1} atom2={atom2} {dstFunc}")

        finally:
            self.numberSelection.clear()

    def validateDistanceRange(self, index, group, weight, scale, target_value, lower_limit, upper_limit, omit_dist_limit_outlier):
        """ Validate distance value range.
        """

        validRange = True
        dstFunc = {'weight': weight, 'scale': scale}

        if target_value is not None:
            if DIST_ERROR_MIN < target_value < DIST_ERROR_MAX:
                dstFunc['target_value'] = f"{target_value:.3f}"
            else:
                if target_value <= DIST_ERROR_MIN and omit_dist_limit_outlier:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index,g=group)}"\
                        f"The target value='{target_value:.3f}' is omitted because it is not within range {DIST_RESTRAINT_ERROR}.\n"
                    target_value = None
                else:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index,g=group)}"\
                        f"The target value='{target_value:.3f}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if lower_limit is not None:
            if DIST_ERROR_MIN <= lower_limit < DIST_ERROR_MAX:
                dstFunc['lower_limit'] = f"{lower_limit:.3f}"
            else:
                if lower_limit <= DIST_ERROR_MIN and omit_dist_limit_outlier:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index,g=group)}"\
                        f"The lower limit value='{lower_limit:.3f}' is omitted because it is not within range {DIST_RESTRAINT_ERROR}.\n"
                    lower_limit = None
                else:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index,g=group)}"\
                        f"The lower limit value='{lower_limit:.3f}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if upper_limit is not None:
            if DIST_ERROR_MIN < upper_limit <= DIST_ERROR_MAX:
                dstFunc['upper_limit'] = f"{upper_limit:.3f}"
            else:
                if upper_limit > DIST_ERROR_MAX and omit_dist_limit_outlier:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index,g=group)}"\
                        f"The upper limit value='{upper_limit:.3f}' is omitted because it is not within range {DIST_RESTRAINT_ERROR}.\n"
                    upper_limit = None
                else:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index,g=group)}"\
                        f"The upper limit value='{upper_limit:.3f}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if target_value is not None:

            if lower_limit is not None:
                if lower_limit > target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index,g=group)}"\
                        f"The lower limit value='{lower_limit:.3f}' must be less than the target value '{target_value:.3f}'.\n"

            if upper_limit is not None:
                if upper_limit < target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index,g=group)}"\
                        f"The upper limit value='{upper_limit:.3f}' must be grater than the target value '{target_value:.3f}'.\n"

        if lower_limit is not None and upper_limit is not None:
            if lower_limit > upper_limit:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"The lower limit value='{lower_limit:.3f}' must be less than the upper limit value '{upper_limit:.3f}'.\n"

        if not validRange:
            return None

        if target_value is not None:
            if DIST_RANGE_MIN <= target_value <= DIST_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"The target value='{target_value:.3f}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        if lower_limit is not None:
            if DIST_RANGE_MIN <= lower_limit <= DIST_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"The lower limit value='{lower_limit:.3f}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        if upper_limit is not None:
            if DIST_RANGE_MIN <= upper_limit <= DIST_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"The upper limit value='{upper_limit:.3f}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        return dstFunc

    def getRealChainSeqId(self, ps, seqId, compId):
        compId = translateToStdResName(compId)
        if self.__reasons is not None and 'label_seq_scheme' in self.__reasons and self.__reasons['label_seq_scheme']:
            seqKey = (ps['chain_id'], seqId)
            if seqKey in self.__labelToAuthSeq:
                _chainId, _seqId = self.__labelToAuthSeq[seqKey]
                if _seqId in ps['auth_seq_id']:
                    return _chainId, _seqId
        if seqId in ps['auth_seq_id']:
            idx = ps['auth_seq_id'].index(seqId)
            if compId in (ps['comp_id'][idx], ps['auth_comp_id'][idx]):
                return ps['auth_chain_id'], seqId
        if seqId in ps['seq_id']:
            idx = ps['seq_id'].index(seqId)
            if compId in (ps['comp_id'][idx], ps['auth_comp_id'][idx]):
                return ps['auth_chain_id'], ps['auth_seq_id'][idx]
        return ps['chain_id'], seqId

    def assignCoordPolymerSequence(self, refChainId, seqId, compId, atomId, index=None, group=None):
        """ Assign polymer sequences of the coordinates.
        """

        chainAssign = []
        _seqId = seqId

        self.updatePolySeqRst(str(refChainId), _seqId, compId)

        for ps in self.__polySeq:
            chainId, seqId = self.getRealChainSeqId(ps, _seqId, compId)
            if refChainId is not None and refChainId != chainId and refChainId in self.__chainNumberDict:
                if chainId != self.__chainNumberDict[refChainId]:
                    continue
            if seqId in ps['auth_seq_id']:
                idx = ps['auth_seq_id'].index(seqId)
                cifCompId = ps['comp_id'][idx]
                origCompId = ps['auth_comp_id'][idx]
                if compId in (cifCompId, origCompId):
                    if len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                        chainAssign.append((chainId, seqId, cifCompId))
                        if refChainId is not None and refChainId != chainId and refChainId not in self.__chainNumberDict:
                            self.__chainNumberDict[refChainId] = chainId
                elif len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                    chainAssign.append((chainId, seqId, cifCompId))
                    if refChainId is not None and refChainId != chainId and refChainId not in self.__chainNumberDict:
                        self.__chainNumberDict[refChainId] = chainId
                    """ defer to sequence alignment error
                    if cifCompId != translateToStdResName(compId):
                        self.warningMessage += f"[Unmatched residue name] {self.__getCurrentRestraint(n=index,g=group)}"\
                            f"The residue name {_seqId}:{compId} is unmatched with the name of the coordinates, {cifCompId}.\n"
                    """

        if len(chainAssign) == 0:
            for ps in self.__polySeq:
                chainId = ps['chain_id']
                if refChainId is not None and refChainId != chainId and refChainId in self.__chainNumberDict:
                    if chainId != self.__chainNumberDict[refChainId]:
                        continue
                seqKey = (chainId, _seqId)
                if seqKey in self.__authToLabelSeq:
                    _, seqId = self.__authToLabelSeq[seqKey]
                    if seqId in ps['seq_id']:
                        cifCompId = ps['comp_id'][ps['seq_id'].index(seqId)]
                        origCompId = ps['auth_comp_id'][ps['seq_id'].index(seqId)]
                        if compId in (cifCompId, origCompId):
                            if len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                                chainAssign.append((ps['auth_chain_id'], _seqId, cifCompId))
                                if refChainId is not None and refChainId != chainId and refChainId not in self.__chainNumberDict:
                                    self.__chainNumberDict[refChainId] = chainId
                                if self.reasonsForReParsing is None:
                                    self.reasonsForReParsing = {}
                                if 'label_seq_scheme' not in self.reasonsForReParsing:
                                    self.reasonsForReParsing['label_seq_scheme'] = True
                        elif len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                            chainAssign.append((ps['auth_chain_id'], _seqId, cifCompId))
                            if refChainId is not None and refChainId != chainId and refChainId not in self.__chainNumberDict:
                                self.__chainNumberDict[refChainId] = chainId
                            """ defer to sequence alignment error
                            if cifCompId != translateToStdResName(compId):
                                self.warningMessage += f"[Unmatched residue name] {self.__getCurrentRestraint(n=index,g=group)}"\
                                    f"The residue name {_seqId}:{compId} is unmatched with the name of the coordinates, {cifCompId}.\n"
                            """

        if len(chainAssign) == 0 and self.__altPolySeq is not None:
            for ps in self.__altPolySeq:
                chainId = ps['auth_chain_id']
                if refChainId is not None and refChainId != chainId and refChainId in self.__chainNumberDict:
                    if chainId != self.__chainNumberDict[refChainId]:
                        continue
                if _seqId in ps['auth_seq_id']:
                    cifCompId = ps['comp_id'][ps['auth_seq_id'].index(_seqId)]
                    chainAssign.append(chainId, _seqId, cifCompId)
                    if refChainId is not None and refChainId != chainId and refChainId not in self.__chainNumberDict:
                        self.__chainNumberDict[refChainId] = chainId
                    """ defer to sequence alignment error
                    if cifCompId != translateToStdResName(compId):
                        self.warningMessage += f"[Unmatched residue name] {self.__getCurrentRestraint(n=index,g=group)}"\
                            f"The residue name {_seqId}:{compId} is unmatched with the name of the coordinates, {cifCompId}.\n"
                    """

        if len(chainAssign) == 0:
            if seqId == 1 and atomId in ('H', 'HN'):
                return self.assignCoordPolymerSequence(refChainId, seqId, compId, 'H1')
            self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint(n=index,g=group)}"\
                f"{_seqId}:{compId}:{atomId} is not present in the coordinates.\n"

        return chainAssign

    def updatePolySeqRst(self, chainId, seqId, compId):
        """ Update polymer sequence of the current MR file.
        """

        ps = next((ps for ps in self.__polySeqRst if ps['chain_id'] == chainId), None)
        if ps is None:
            self.__polySeqRst.append({'chain_id': chainId, 'seq_id': [], 'comp_id': []})
            ps = self.__polySeqRst[-1]

        if seqId not in ps['seq_id']:
            ps['seq_id'].append(seqId)
            ps['comp_id'].append(translateToStdResName(compId))

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

                    self.warningMessage += f"[Concatenated sequence] The chain ID {chain_id2!r} of the sequences in the PALES/DYNAMO restraint file "\
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
                                f"in the PALES/DYNAMO restraint data (chain_id {chain_id2}).\n"
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
                            f"and the PALES/DYNAMO restraint data ({mr_seq_code}). "\
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

    def selectCoordAtoms(self, chainAssign, seqId, compId, atomId, allowAmbig=True, index=None, group=None):
        """ Select atoms of the coordinates.
        """

        atomSelection = []

        for chainId, cifSeqId, cifCompId in chainAssign:
            seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, cifSeqId, self.__hasCoord)

            _atomId, _, details = self.__nefT.get_valid_star_atom_in_xplor(cifCompId, atomId, leave_unmatched=True)
            if details is not None:
                _atomId, _, details = self.__nefT.get_valid_star_atom_in_xplor(cifCompId, atomId[:-1], leave_unmatched=True)

            if details is not None:
                _atomId_ = translateToStdAtomName(atomId, cifCompId, ccU=self.__ccU)
                if _atomId_ != atomId:
                    _atomId = self.__nefT.get_valid_star_atom_in_xplor(cifCompId, _atomId)[0]
            # _atomId = self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]
            lenAtomId = len(_atomId)
            if lenAtomId == 0:
                self.warningMessage += f"[Invalid atom nomenclature] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"{seqId}:{compId}:{atomId} is invalid atom nomenclature.\n"
                continue
            if lenAtomId > 1 and not allowAmbig:
                self.warningMessage += f"[Invalid atom selection] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"Ambiguous atom selection '{seqId}:{compId}:{atomId}' is not allowed as a angle restraint.\n"
                continue

            for cifAtomId in _atomId:
                atomSelection.append({'chain_id': chainId, 'seq_id': cifSeqId, 'comp_id': cifCompId, 'atom_id': cifAtomId})

                self.testCoordAtomIdConsistency(chainId, cifSeqId, cifCompId, cifAtomId, seqKey, coordAtomSite, index, group)

        if len(atomSelection) > 0:
            self.atomSelectionSet.append(atomSelection)

    def selectAuxCoordAtoms(self, chainAssign, seqId, compId, atomId, allowAmbig=True, index=None, group=None):
        """ Select auxiliary atoms of the coordinates.
        """

        atomSelection = []

        for chainId, cifSeqId, cifCompId in chainAssign:
            seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, cifSeqId, self.__hasCoord)

            _atomId, _, details = self.__nefT.get_valid_star_atom_in_xplor(cifCompId, atomId, leave_unmatched=True)
            if details is not None:
                _atomId, _, details = self.__nefT.get_valid_star_atom_in_xplor(cifCompId, atomId[:-1], leave_unmatched=True)

            if details is not None:
                _atomId_ = translateToStdAtomName(atomId, cifCompId, ccU=self.__ccU)
                if _atomId_ != atomId:
                    _atomId = self.__nefT.get_valid_star_atom_in_xplor(cifCompId, _atomId)[0]
            # _atomId = self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]
            lenAtomId = len(_atomId)
            if lenAtomId == 0:
                self.warningMessage += f"[Invalid atom nomenclature] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"{seqId}:{compId}:{atomId} is invalid atom nomenclature.\n"
                continue
            if lenAtomId > 1 and not allowAmbig:
                self.warningMessage += f"[Invalid atom selection] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"Ambiguous atom selection '{seqId}:{compId}:{atomId}' is not allowed as a angle restraint.\n"
                continue

            for cifAtomId in _atomId:
                atomSelection.append({'chain_id': chainId, 'seq_id': cifSeqId, 'comp_id': cifCompId, 'atom_id': cifAtomId})

                self.testCoordAtomIdConsistency(chainId, cifSeqId, cifCompId, cifAtomId, seqKey, coordAtomSite, index, group)

        if len(atomSelection) > 0:
            self.auxAtomSelectionSet.append(atomSelection)

    def testCoordAtomIdConsistency(self, chainId, seqId, compId, atomId, seqKey, coordAtomSite, index=None, group=None):
        if not self.__hasCoord:
            return

        found = False

        if coordAtomSite is not None:
            if atomId in coordAtomSite['atom_id']:
                found = True
            elif 'alt_atom_id' in coordAtomSite and atomId in coordAtomSite['alt_atom_id']:
                found = True
                # self.__authAtomId = 'auth_atom_id'
            elif self.__preferAuthSeq:
                _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, asis=False)
                if _coordAtomSite is not None:
                    if atomId in _coordAtomSite['atom_id']:
                        found = True
                        self.__preferAuthSeq = False
                        # self.__authSeqId = 'label_seq_id'
                        seqKey = _seqKey
                    elif 'alt_atom_id' in _coordAtomSite and atomId in _coordAtomSite['alt_atom_id']:
                        found = True
                        self.__preferAuthSeq = False
                        # self.__authSeqId = 'label_seq_id'
                        # self.__authAtomId = 'auth_atom_id'
                        seqKey = _seqKey

        elif self.__preferAuthSeq:
            _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, asis=False)
            if _coordAtomSite is not None:
                if atomId in _coordAtomSite['atom_id']:
                    found = True
                    self.__preferAuthSeq = False
                    # self.__authSeqId = 'label_seq_id'
                    seqKey = _seqKey
                elif 'alt_atom_id' in _coordAtomSite and atomId in _coordAtomSite['alt_atom_id']:
                    found = True
                    self.__preferAuthSeq = False
                    # self.__authSeqId = 'label_seq_id'
                    # self.__authAtomId = 'auth_atom_id'
                    seqKey = _seqKey

        if found:
            return

        if chainId in self.__chainNumberDict.values():

            _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, asis=False)
            if _coordAtomSite is not None:
                if atomId in _coordAtomSite['atom_id']:
                    found = True
                    self.__preferAuthSeq = False
                    # self.__authSeqId = 'label_seq_id'
                    seqKey = _seqKey
                elif 'alt_atom_id' in _coordAtomSite and atomId in _coordAtomSite['alt_atom_id']:
                    found = True
                    self.__preferAuthSeq = False
                    # self.__authSeqId = 'label_seq_id'
                    # self.__authAtomId = 'auth_atom_id'
                    seqKey = _seqKey

            if found:
                return

        if self.__ccU.updateChemCompDict(compId):
            cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == atomId), None)
            if cca is not None and seqKey not in self.__coordUnobsRes and self.__ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] == 'REL':
                if seqId == 1 and atomId in ('H', 'HN'):
                    self.testCoordAtomIdConsistency(chainId, seqId, compId, 'H1', seqKey, coordAtomSite)
                    return
                if atomId[0] == 'H':
                    ccb = next((ccb for ccb in self.__ccU.lastBonds
                                if atomId in (ccb[self.__ccU.ccbAtomId1], ccb[self.__ccU.ccbAtomId2])), None)
                    if ccb is not None:
                        bondedTo = ccb[self.__ccU.ccbAtomId2] if ccb[self.__ccU.ccbAtomId1] == atomId else ccb[self.__ccU.ccbAtomId1]
                        if bondedTo[0] in ('N', 'O', 'S'):
                            return
                self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint(n=index,g=group)}"\
                    f"{chainId}:{seqId}:{compId}:{atomId} is not present in the coordinates.\n"

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

    # Enter a parse tree produced by PalesMRParser#torsion_angle_restraints.
    def enterTorsion_angle_restraints(self, ctx: PalesMRParser.Torsion_angle_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dihed'

    # Exit a parse tree produced by PalesMRParser#torsion_angle_restraints.
    def exitTorsion_angle_restraints(self, ctx: PalesMRParser.Torsion_angle_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by PalesMRParser#torsion_angle_restraint.
    def enterTorsion_angle_restraint(self, ctx: PalesMRParser.Torsion_angle_restraintContext):  # pylint: disable=unused-argument
        self.dihedRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by PalesMRParser#torsion_angle_restraint.
    def exitTorsion_angle_restraint(self, ctx: PalesMRParser.Torsion_angle_restraintContext):

        try:

            index = int(str(ctx.Integer(0)))

            seqId1 = int(str(ctx.Integer(1)))
            compId1 = str(ctx.Simple_name(0)).upper()
            atomId1 = str(ctx.Simple_name(1)).upper()
            seqId2 = int(str(ctx.Integer(2)))
            compId2 = str(ctx.Simple_name(2)).upper()
            atomId2 = str(ctx.Simple_name(3)).upper()
            seqId3 = int(str(ctx.Integer(3)))
            compId3 = str(ctx.Simple_name(4)).upper()
            atomId3 = str(ctx.Simple_name(5)).upper()
            seqId4 = int(str(ctx.Integer(4)))
            compId4 = str(ctx.Simple_name(6)).upper()
            atomId4 = str(ctx.Simple_name(7)).upper()

            if None in self.numberSelection:
                return

            target_value = None
            lower_limit = self.numberSelection[0]
            upper_limit = self.numberSelection[1]
            # fource_const = self.numberSelection[2]

            dstFunc = self.validateAngleRange(index, 1.0, target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            chainAssign1 = self.assignCoordPolymerSequence(None, seqId1, compId1, atomId1, index)
            chainAssign2 = self.assignCoordPolymerSequence(None, seqId2, compId2, atomId2, index)
            chainAssign3 = self.assignCoordPolymerSequence(None, seqId3, compId3, atomId3, index)
            chainAssign4 = self.assignCoordPolymerSequence(None, seqId4, compId4, atomId4, index)

            if len(chainAssign1) == 0 or len(chainAssign2) == 0\
               or len(chainAssign3) == 0 or len(chainAssign4) == 0:
                return

            self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1, False)
            self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2, False)
            self.selectCoordAtoms(chainAssign3, seqId3, compId3, atomId3, False)
            self.selectCoordAtoms(chainAssign4, seqId4, compId4, atomId4, False)

            if len(self.atomSelectionSet) < 4:
                return

            if not self.areUniqueCoordAtoms('a Torsion angle'):
                return

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
                    print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} (index={index}) angleName={angleName} "
                          f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} {dstFunc}")

        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by PalesMRParser#torsion_angle_restraints_sw_segid.
    def enterTorsion_angle_restraints_sw_segid(self, ctx: PalesMRParser.Torsion_angle_restraints_sw_segidContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dihed'

    # Exit a parse tree produced by PalesMRParser#torsion_angle_restraints_sw_segid.
    def exitTorsion_angle_restraints_sw_segid(self, ctx: PalesMRParser.Torsion_angle_restraints_sw_segidContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by PalesMRParser#torsion_angle_restraint_sw_segid.
    def enterTorsion_angle_restraint_sw_segid(self, ctx: PalesMRParser.Torsion_angle_restraint_sw_segidContext):  # pylint: disable=unused-argument
        self.dihedRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by PalesMRParser#torsion_angle_restraint_sw_segid.
    def exitTorsion_angle_restraint_sw_segid(self, ctx: PalesMRParser.Torsion_angle_restraint_sw_segidContext):

        try:

            index = int(str(ctx.Integer(0)))

            chainId1 = str(ctx.Simple_name(0))
            seqId1 = int(str(ctx.Integer(1)))
            compId1 = str(ctx.Simple_name(1)).upper()
            atomId1 = str(ctx.Simple_name(2)).upper()
            chainId2 = str(ctx.Simple_name(3))
            seqId2 = int(str(ctx.Integer(2)))
            compId2 = str(ctx.Simple_name(4)).upper()
            atomId2 = str(ctx.Simple_name(5)).upper()
            chainId3 = str(ctx.Simple_name(6))
            seqId3 = int(str(ctx.Integer(3)))
            compId3 = str(ctx.Simple_name(7)).upper()
            atomId3 = str(ctx.Simple_name(8)).upper()
            chainId4 = str(ctx.Simple_name(9))
            seqId4 = int(str(ctx.Integer(4)))
            compId4 = str(ctx.Simple_name(10)).upper()
            atomId4 = str(ctx.Simple_name(11)).upper()

            if None in self.numberSelection:
                return

            target_value = None
            lower_limit = self.numberSelection[0]
            upper_limit = self.numberSelection[1]
            # fource_const = self.numberSelection[2]

            dstFunc = self.validateAngleRange(None, 1.0, target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            chainAssign1 = self.assignCoordPolymerSequence(chainId1, seqId1, compId1, atomId1, index)
            chainAssign2 = self.assignCoordPolymerSequence(chainId2, seqId2, compId2, atomId2, index)
            chainAssign3 = self.assignCoordPolymerSequence(chainId3, seqId3, compId3, atomId3, index)
            chainAssign4 = self.assignCoordPolymerSequence(chainId4, seqId4, compId4, atomId4, index)

            if len(chainAssign1) == 0 or len(chainAssign2) == 0\
               or len(chainAssign3) == 0 or len(chainAssign4) == 0:
                return

            self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1, False)
            self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2, False)
            self.selectCoordAtoms(chainAssign3, seqId3, compId3, atomId3, False)
            self.selectCoordAtoms(chainAssign4, seqId4, compId4, atomId4, False)

            if len(self.atomSelectionSet) < 4:
                return

            if not self.areUniqueCoordAtoms('a Torsion angle'):
                return

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
                    print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} (index={index}) angleName={angleName} "
                          f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} {dstFunc}")

        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by PalesMRParser#torsion_angle_restraints_ew_segid.
    def enterTorsion_angle_restraints_ew_segid(self, ctx: PalesMRParser.Torsion_angle_restraints_ew_segidContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dihed'

    # Exit a parse tree produced by PalesMRParser#torsion_angle_restraints_ew_segid.
    def exitTorsion_angle_restraints_ew_segid(self, ctx: PalesMRParser.Torsion_angle_restraints_ew_segidContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by PalesMRParser#torsion_angle_restraint_ew_segid.
    def enterTorsion_angle_restraint_ew_segid(self, ctx: PalesMRParser.Torsion_angle_restraint_ew_segidContext):  # pylint: disable=unused-argument
        self.dihedRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by PalesMRParser#torsion_angle_restraint_ew_segid.
    def exitTorsion_angle_restraint_ew_segid(self, ctx: PalesMRParser.Torsion_angle_restraint_ew_segidContext):

        try:

            index = int(str(ctx.Integer(0)))

            seqId1 = int(str(ctx.Integer(1)))
            compId1 = str(ctx.Simple_name(0)).upper()
            atomId1 = str(ctx.Simple_name(1)).upper()
            chainId1 = str(ctx.Simple_name(2))
            seqId2 = int(str(ctx.Integer(2)))
            compId2 = str(ctx.Simple_name(3)).upper()
            atomId2 = str(ctx.Simple_name(4)).upper()
            chainId2 = str(ctx.Simple_name(5))
            seqId3 = int(str(ctx.Integer(3)))
            compId3 = str(ctx.Simple_name(6)).upper()
            atomId3 = str(ctx.Simple_name(7)).upper()
            chainId3 = str(ctx.Simple_name(8))
            seqId4 = int(str(ctx.Integer(4)))
            compId4 = str(ctx.Simple_name(9)).upper()
            atomId4 = str(ctx.Simple_name(10)).upper()
            chainId4 = str(ctx.Simple_name(11))

            if None in self.numberSelection:
                return

            target_value = None
            lower_limit = self.numberSelection[0]
            upper_limit = self.numberSelection[1]
            # fource_const = self.numberSelection[2]

            dstFunc = self.validateAngleRange(None, 1.0, target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            chainAssign1 = self.assignCoordPolymerSequence(chainId1, seqId1, compId1, atomId1, index)
            chainAssign2 = self.assignCoordPolymerSequence(chainId2, seqId2, compId2, atomId2, index)
            chainAssign3 = self.assignCoordPolymerSequence(chainId3, seqId3, compId3, atomId3, index)
            chainAssign4 = self.assignCoordPolymerSequence(chainId4, seqId4, compId4, atomId4, index)

            if len(chainAssign1) == 0 or len(chainAssign2) == 0\
               or len(chainAssign3) == 0 or len(chainAssign4) == 0:
                return

            self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1, False)
            self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2, False)
            self.selectCoordAtoms(chainAssign3, seqId3, compId3, atomId3, False)
            self.selectCoordAtoms(chainAssign4, seqId4, compId4, atomId4, False)

            if len(self.atomSelectionSet) < 4:
                return

            if not self.areUniqueCoordAtoms('a Torsion angle'):
                return

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
                    print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} (index={index}) angleName={angleName} "
                          f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} {dstFunc}")

        finally:
            self.numberSelection.clear()

    def validateAngleRange(self, index, weight, target_value, lower_limit, upper_limit):
        """ Validate angle value range.
        """

        validRange = True
        dstFunc = {'weight': weight}

        if target_value is not None:
            if ANGLE_ERROR_MIN < target_value < ANGLE_ERROR_MAX:
                dstFunc['target_value'] = f"{target_value}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index)}"\
                    f"The target value='{target_value}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"

        if lower_limit is not None:
            if ANGLE_ERROR_MIN <= lower_limit < ANGLE_ERROR_MAX:
                dstFunc['lower_limit'] = f"{lower_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index)}"\
                    f"The lower limit value='{lower_limit:.3f}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"

        if upper_limit is not None:
            if ANGLE_ERROR_MIN < upper_limit <= ANGLE_ERROR_MAX:
                dstFunc['upper_limit'] = f"{upper_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index)}"\
                    f"The upper limit value='{upper_limit:.3f}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"
        """
        if target_value is not None:

            if lower_limit is not None:
                if lower_limit > target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index)}"\
                        f"The lower limit value='{lower_limit:.3f}' must be less than the target value '{target_value}'.\n"

            if upper_limit is not None:
                if upper_limit < target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index)}"\
                        f"The upper limit value='{upper_limit:.3f}' must be grater than the target value '{target_value}'.\n"
        """
        if not validRange:
            return None

        if target_value is not None:
            if ANGLE_RANGE_MIN <= target_value <= ANGLE_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index)}"\
                    f"The target value='{target_value}' should be within range {ANGLE_RESTRAINT_RANGE}.\n"

        if lower_limit is not None:
            if ANGLE_RANGE_MIN <= lower_limit <= ANGLE_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index)}"\
                    f"The lower limit value='{lower_limit:.3f}' should be within range {ANGLE_RESTRAINT_RANGE}.\n"

        if upper_limit is not None:
            if ANGLE_RANGE_MIN <= upper_limit <= ANGLE_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index)}"\
                    f"The upper limit value='{upper_limit:.3f}' should be within range {ANGLE_RESTRAINT_RANGE}.\n"

        return dstFunc

    # Enter a parse tree produced by PalesMRParser#rdc_restraints.
    def enterRdc_restraints(self, ctx: PalesMRParser.Rdc_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'rdc'

    # Exit a parse tree produced by PalesMRParser#rdc_restraints.
    def exitRdc_restraints(self, ctx: PalesMRParser.Rdc_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by PalesMRParser#rdc_restraint.
    def enterRdc_restraint(self, ctx: PalesMRParser.Rdc_restraintContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by PalesMRParser#rdc_restraint.
    def exitRdc_restraint(self, ctx: PalesMRParser.Rdc_restraintContext):

        try:

            seqId1 = int(str(ctx.Integer(0)))
            compId1 = str(ctx.Simple_name(0)).upper()
            atomId1 = str(ctx.Simple_name(1)).upper()
            seqId2 = int(str(ctx.Integer(1)))
            compId2 = str(ctx.Simple_name(2)).upper()
            atomId2 = str(ctx.Simple_name(3)).upper()

            if None in self.numberSelection:
                return

            target = self.numberSelection[0]
            error = abs(self.numberSelection[1])
            weight = self.numberSelection[2]

            if weight <= 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The relative weight value of '{weight}' must be a positive value.\n"
                return

            target_value = target
            lower_limit = target - error
            upper_limit = target + error

            dstFunc = self.validateRdcRange(weight, target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            chainAssign1 = self.assignCoordPolymerSequence(None, seqId1, compId1, atomId1)
            chainAssign2 = self.assignCoordPolymerSequence(None, seqId2, compId2, atomId2)

            if len(chainAssign1) == 0 or len(chainAssign2) == 0:
                return

            self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1)
            self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2)

            if len(self.atomSelectionSet) < 2:
                return

            if not self.areUniqueCoordAtoms('an RDC'):
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
                                "Found an RDC vector over multiple covalent bonds; "\
                                f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                            return

            for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                  self.atomSelectionSet[1]):
                if atom1['chain_id'] != atom2['chain_id']:
                    continue
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} id={self.rdcRestraints} "
                          f"atom1={atom1} atom2={atom2} {dstFunc}")

        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by PalesMRParser#rdc_restraints_sw_segid.
    def enterRdc_restraints_sw_segid(self, ctx: PalesMRParser.Rdc_restraints_sw_segidContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'rdc'

    # Exit a parse tree produced by PalesMRParser#rdc_restraints_sw_segid.
    def exitRdc_restraints_sw_segid(self, ctx: PalesMRParser.Rdc_restraints_sw_segidContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by PalesMRParser#rdc_restraint_sw_segid.
    def enterRdc_restraint_sw_segid(self, ctx: PalesMRParser.Rdc_restraint_sw_segidContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by PalesMRParser#rdc_restraint_sw_segid.
    def exitRdc_restraint_sw_segid(self, ctx: PalesMRParser.Rdc_restraint_sw_segidContext):

        try:

            chainId1 = str(ctx.Simple_name(0))
            seqId1 = int(str(ctx.Integer(0)))
            compId1 = str(ctx.Simple_name(1)).upper()
            atomId1 = str(ctx.Simple_name(2)).upper()
            chainId2 = str(ctx.Simple_name(3))
            seqId2 = int(str(ctx.Integer(1)))
            compId2 = str(ctx.Simple_name(4)).upper()
            atomId2 = str(ctx.Simple_name(5)).upper()

            if None in self.numberSelection:
                return

            target = self.numberSelection[0]
            error = abs(self.numberSelection[1])
            weight = self.numberSelection[2]

            if weight <= 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The relative weight value of '{weight}' must be a positive value.\n"
                return

            target_value = target
            lower_limit = target - error
            upper_limit = target + error

            dstFunc = self.validateRdcRange(weight, target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            chainAssign1 = self.assignCoordPolymerSequence(chainId1, seqId1, compId1, atomId1)
            chainAssign2 = self.assignCoordPolymerSequence(chainId2, seqId2, compId2, atomId2)

            if len(chainAssign1) == 0 or len(chainAssign2) == 0:
                return

            self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1)
            self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2)

            if len(self.atomSelectionSet) < 2:
                return

            if not self.areUniqueCoordAtoms('an RDC'):
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
                                "Found an RDC vector over multiple covalent bonds; "\
                                f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                            return

            for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                  self.atomSelectionSet[1]):
                if atom1['chain_id'] != atom2['chain_id']:
                    continue
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} id={self.rdcRestraints} "
                          f"atom1={atom1} atom2={atom2} {dstFunc}")

        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by PalesMRParser#rdc_restraints_ew_segid.
    def enterRdc_restraints_ew_segid(self, ctx: PalesMRParser.Rdc_restraints_ew_segidContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'rdc'

    # Exit a parse tree produced by PalesMRParser#rdc_restraints_ew_segid.
    def exitRdc_restraints_ew_segid(self, ctx: PalesMRParser.Rdc_restraints_ew_segidContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by PalesMRParser#rdc_restraint_ew_segid.
    def enterRdc_restraint_ew_segid(self, ctx: PalesMRParser.Rdc_restraint_ew_segidContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by PalesMRParser#rdc_restraint_ew_segid.
    def exitRdc_restraint_ew_segid(self, ctx: PalesMRParser.Rdc_restraint_ew_segidContext):

        try:

            seqId1 = int(str(ctx.Integer(0)))
            compId1 = str(ctx.Simple_name(0)).upper()
            atomId1 = str(ctx.Simple_name(1)).upper()
            chainId1 = str(ctx.Simple_name(2))
            seqId2 = int(str(ctx.Integer(1)))
            compId2 = str(ctx.Simple_name(3)).upper()
            atomId2 = str(ctx.Simple_name(4)).upper()
            chainId2 = str(ctx.Simple_name(5))

            if None in self.numberSelection:
                return

            target = self.numberSelection[0]
            error = abs(self.numberSelection[1])
            weight = self.numberSelection[2]

            if weight <= 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The relative weight value of '{weight}' must be a positive value.\n"
                return

            target_value = target
            lower_limit = target - error
            upper_limit = target + error

            dstFunc = self.validateRdcRange(weight, target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            chainAssign1 = self.assignCoordPolymerSequence(chainId1, seqId1, compId1, atomId1)
            chainAssign2 = self.assignCoordPolymerSequence(chainId2, seqId2, compId2, atomId2)

            if len(chainAssign1) == 0 or len(chainAssign2) == 0:
                return

            self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1)
            self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2)

            if len(self.atomSelectionSet) < 2:
                return

            if not self.areUniqueCoordAtoms('an RDC'):
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
                                "Found an RDC vector over multiple covalent bonds; "\
                                f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                            return

            for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                  self.atomSelectionSet[1]):
                if atom1['chain_id'] != atom2['chain_id']:
                    continue
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} id={self.rdcRestraints} "
                          f"atom1={atom1} atom2={atom2} {dstFunc}")

        finally:
            self.numberSelection.clear()

    def validateRdcRange(self, weight, target_value, lower_limit, upper_limit):
        """ Validate RDC value range.
        """

        validRange = True
        dstFunc = {'weight': weight}

        if target_value is not None:
            if RDC_ERROR_MIN < target_value < RDC_ERROR_MAX:
                dstFunc['target_value'] = f"{target_value}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The target value='{target_value}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if lower_limit is not None:
            if RDC_ERROR_MIN <= lower_limit < RDC_ERROR_MAX:
                dstFunc['lower_limit'] = f"{lower_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower limit value='{lower_limit:.3f}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if upper_limit is not None:
            if RDC_ERROR_MIN < upper_limit <= RDC_ERROR_MAX:
                dstFunc['upper_limit'] = f"{upper_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit:.3f}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if target_value is not None:

            if lower_limit is not None:
                if lower_limit > target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower limit value='{lower_limit:.3f}' must be less than the target value '{target_value}'.\n"

            if upper_limit is not None:
                if upper_limit < target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The upper limit value='{upper_limit:.3f}' must be grater than the target value '{target_value}'.\n"

        if not validRange:
            return None

        if target_value is not None:
            if RDC_RANGE_MIN <= target_value <= RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The target value='{target_value}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        if lower_limit is not None:
            if RDC_RANGE_MIN <= lower_limit <= RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The lower limit value='{lower_limit:.3f}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        if upper_limit is not None:
            if RDC_RANGE_MIN <= upper_limit <= RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit:.3f}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        return dstFunc

    def areUniqueCoordAtoms(self, subtype_name):
        """ Check whether atom selection sets are uniquely assigned.
        """

        for _atomSelectionSet in self.atomSelectionSet:

            if len(_atomSelectionSet) < 2:
                continue

            for (atom1, atom2) in itertools.combinations(_atomSelectionSet, 2):
                if atom1['chain_id'] != atom2['chain_id']:
                    continue
                if atom1['seq_id'] != atom2['seq_id']:
                    continue
                self.warningMessage += f"[Invalid atom selection] {self.__getCurrentRestraint()}"\
                    f"Ambiguous atom selection '{atom1['chain_id']}:{atom1['seq_id']}:{atom1['atom_id']} or "\
                    f"{atom2['atom_id']}' is not allowed as {subtype_name} restraint.\n"
                return False

        return True

    # Enter a parse tree produced by PalesMRParser#coupling_restraints.
    def enterCoupling_restraints(self, ctx: PalesMRParser.Coupling_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'jcoup'

    # Exit a parse tree produced by PalesMRParser#coupling_restraints.
    def exitCoupling_restraints(self, ctx: PalesMRParser.Coupling_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by PalesMRParser#coupling_restraint.
    def enterCoupling_restraint(self, ctx: PalesMRParser.Coupling_restraintContext):  # pylint: disable=unused-argument
        self.jcoupRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by PalesMRParser#coupling_restraint.
    def exitCoupling_restraint(self, ctx: PalesMRParser.Coupling_restraintContext):

        try:

            index = int(str(ctx.Integer(0)))

            seqId1 = int(str(ctx.Integer(1)))
            compId1 = str(ctx.Simple_name(0)).upper()
            atomId1 = str(ctx.Simple_name(1)).upper()
            seqId2 = int(str(ctx.Integer(2)))
            compId2 = str(ctx.Simple_name(2)).upper()
            atomId2 = str(ctx.Simple_name(3)).upper()
            seqId3 = int(str(ctx.Integer(3)))
            compId3 = str(ctx.Simple_name(4)).upper()
            atomId3 = str(ctx.Simple_name(5)).upper()
            seqId4 = int(str(ctx.Integer(4)))
            compId4 = str(ctx.Simple_name(6)).upper()
            atomId4 = str(ctx.Simple_name(7)).upper()

            if None in self.numberSelection:
                return

            A = self.numberSelection[0]
            B = self.numberSelection[1]
            C = self.numberSelection[2]
            phase = self.numberSelection[3]
            target_value = self.numberSelection[4]
            lower_limit = upper_limit = None
            # fource_const = self.numberSelection[5]

            dstFunc = self.validateCoupRange(index, 1.0, target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            chainAssign1 = self.assignCoordPolymerSequence(None, seqId1, compId1, atomId1, index)
            chainAssign2 = self.assignCoordPolymerSequence(None, seqId2, compId2, atomId2, index)
            chainAssign3 = self.assignCoordPolymerSequence(None, seqId3, compId3, atomId3, index)
            chainAssign4 = self.assignCoordPolymerSequence(None, seqId4, compId4, atomId4, index)

            if len(chainAssign1) == 0 or len(chainAssign2) == 0\
               or len(chainAssign3) == 0 or len(chainAssign4) == 0:
                return

            self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1, False)
            self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2, False)
            self.selectCoordAtoms(chainAssign3, seqId3, compId3, atomId3, False)
            self.selectCoordAtoms(chainAssign4, seqId4, compId4, atomId4, False)

            if len(self.atomSelectionSet) < 4:
                return

            if not self.areUniqueCoordAtoms('a Scalar coupling'):
                return

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
                    if angleName == 'PHI':
                        self.auxAtomSelectionSet.clear()
                        self.selectAuxCoordAtoms(chainAssign2, seqId2, compId2, 'H', False)
                        self.selectAuxCoordAtoms(chainAssign3, seqId3, compId3, 'HA', False)
                        if len(self.auxAtomSelectionSet) == 2:
                            print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} (index={index}) angleName={angleName} "
                                  f"A={A} B={B} C={C} phase={phase} "
                                  f"atom1={self.auxAtomSelectionSet[0][0]} atom2={self.auxAtomSelectionSet[1][0]} {dstFunc}")
                            continue
                    else:
                        print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} (index={index}) angleName={angleName} "
                              f"A={A} B={B} C={C} phase={phase} "
                              f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} {dstFunc}")

        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by PalesMRParser#coupling_restraints_sw_segid.
    def enterCoupling_restraints_sw_segid(self, ctx: PalesMRParser.Coupling_restraints_sw_segidContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'jcoup'

    # Exit a parse tree produced by PalesMRParser#coupling_restraints_sw_segid.
    def exitCoupling_restraints_sw_segid(self, ctx: PalesMRParser.Coupling_restraints_sw_segidContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by PalesMRParser#coupling_restraint_sw_segid.
    def enterCoupling_restraint_sw_segid(self, ctx: PalesMRParser.Coupling_restraint_sw_segidContext):  # pylint: disable=unused-argument
        self.jcoupRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by PalesMRParser#coupling_restraint_sw_segid.
    def exitCoupling_restraint_sw_segid(self, ctx: PalesMRParser.Coupling_restraint_sw_segidContext):

        try:

            index = int(str(ctx.Integer(0)))

            chainId1 = str(ctx.Simple_name(0))
            seqId1 = int(str(ctx.Integer(1)))
            compId1 = str(ctx.Simple_name(1)).upper()
            atomId1 = str(ctx.Simple_name(2)).upper()
            chainId2 = str(ctx.Simple_name(3))
            seqId2 = int(str(ctx.Integer(2)))
            compId2 = str(ctx.Simple_name(4)).upper()
            atomId2 = str(ctx.Simple_name(5)).upper()
            chainId3 = str(ctx.Simple_name(6))
            seqId3 = int(str(ctx.Integer(3)))
            compId3 = str(ctx.Simple_name(7)).upper()
            atomId3 = str(ctx.Simple_name(8)).upper()
            chainId4 = str(ctx.Simple_name(9))
            seqId4 = int(str(ctx.Integer(4)))
            compId4 = str(ctx.Simple_name(10)).upper()
            atomId4 = str(ctx.Simple_name(11)).upper()

            if None in self.numberSelection:
                return

            A = self.numberSelection[0]
            B = self.numberSelection[1]
            C = self.numberSelection[2]
            phase = self.numberSelection[3]
            target_value = self.numberSelection[4]
            lower_limit = upper_limit = None
            # fource_const = self.numberSelection[5]

            dstFunc = self.validateCoupRange(index, 1.0, target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            chainAssign1 = self.assignCoordPolymerSequence(chainId1, seqId1, compId1, atomId1, index)
            chainAssign2 = self.assignCoordPolymerSequence(chainId2, seqId2, compId2, atomId2, index)
            chainAssign3 = self.assignCoordPolymerSequence(chainId3, seqId3, compId3, atomId3, index)
            chainAssign4 = self.assignCoordPolymerSequence(chainId4, seqId4, compId4, atomId4, index)

            if len(chainAssign1) == 0 or len(chainAssign2) == 0\
               or len(chainAssign3) == 0 or len(chainAssign4) == 0:
                return

            self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1, False)
            self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2, False)
            self.selectCoordAtoms(chainAssign3, seqId3, compId3, atomId3, False)
            self.selectCoordAtoms(chainAssign4, seqId4, compId4, atomId4, False)

            if len(self.atomSelectionSet) < 4:
                return

            if not self.areUniqueCoordAtoms('a Scalar coupling'):
                return

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
                    if angleName == 'PHI':
                        self.auxAtomSelectionSet.clear()
                        self.selectAuxCoordAtoms(chainAssign2, seqId2, compId2, 'H', False)
                        self.selectAuxCoordAtoms(chainAssign3, seqId3, compId3, 'HA', False)
                        if len(self.auxAtomSelectionSet) == 2:
                            print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} (index={index}) angleName={angleName} "
                                  f"A={A} B={B} C={C} phase={phase} "
                                  f"atom1={self.auxAtomSelectionSet[0][0]} atom2={self.auxAtomSelectionSet[1][0]} {dstFunc}")
                            continue
                    else:
                        print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} (index={index}) angleName={angleName} "
                              f"A={A} B={B} C={C} phase={phase} "
                              f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} {dstFunc}")

        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by PalesMRParser#coupling_restraints_ew_segid.
    def enterCoupling_restraints_ew_segid(self, ctx: PalesMRParser.Coupling_restraints_ew_segidContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'jcoup'

    # Exit a parse tree produced by PalesMRParser#coupling_restraints_ew_segid.
    def exitCoupling_restraints_ew_segid(self, ctx: PalesMRParser.Coupling_restraints_ew_segidContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by PalesMRParser#coupling_restraint_ew_segid.
    def enterCoupling_restraint_ew_segid(self, ctx: PalesMRParser.Coupling_restraint_ew_segidContext):  # pylint: disable=unused-argument
        self.jcoupRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by PalesMRParser#coupling_restraint_ew_segid.
    def exitCoupling_restraint_ew_segid(self, ctx: PalesMRParser.Coupling_restraint_ew_segidContext):

        try:

            index = int(str(ctx.Integer(0)))

            seqId1 = int(str(ctx.Integer(1)))
            compId1 = str(ctx.Simple_name(0)).upper()
            atomId1 = str(ctx.Simple_name(1)).upper()
            chainId1 = str(ctx.Simple_name(2))
            seqId2 = int(str(ctx.Integer(2)))
            compId2 = str(ctx.Simple_name(3)).upper()
            atomId2 = str(ctx.Simple_name(4)).upper()
            chainId2 = str(ctx.Simple_name(5))
            seqId3 = int(str(ctx.Integer(3)))
            compId3 = str(ctx.Simple_name(6)).upper()
            atomId3 = str(ctx.Simple_name(7)).upper()
            chainId3 = str(ctx.Simple_name(8))
            seqId4 = int(str(ctx.Integer(4)))
            compId4 = str(ctx.Simple_name(9)).upper()
            atomId4 = str(ctx.Simple_name(10)).upper()
            chainId4 = str(ctx.Simple_name(11))

            if None in self.numberSelection:
                return

            A = self.numberSelection[0]
            B = self.numberSelection[1]
            C = self.numberSelection[2]
            phase = self.numberSelection[3]
            target_value = self.numberSelection[4]
            lower_limit = upper_limit = None
            # fource_const = self.numberSelection[5]

            dstFunc = self.validateCoupRange(index, 1.0, target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            chainAssign1 = self.assignCoordPolymerSequence(chainId1, seqId1, compId1, atomId1, index)
            chainAssign2 = self.assignCoordPolymerSequence(chainId2, seqId2, compId2, atomId2, index)
            chainAssign3 = self.assignCoordPolymerSequence(chainId3, seqId3, compId3, atomId3, index)
            chainAssign4 = self.assignCoordPolymerSequence(chainId4, seqId4, compId4, atomId4, index)

            if len(chainAssign1) == 0 or len(chainAssign2) == 0\
               or len(chainAssign3) == 0 or len(chainAssign4) == 0:
                return

            self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1, False)
            self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2, False)
            self.selectCoordAtoms(chainAssign3, seqId3, compId3, atomId3, False)
            self.selectCoordAtoms(chainAssign4, seqId4, compId4, atomId4, False)

            if len(self.atomSelectionSet) < 4:
                return

            if not self.areUniqueCoordAtoms('a Scalar coupling'):
                return

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
                    if angleName == 'PHI':
                        self.auxAtomSelectionSet.clear()
                        self.selectAuxCoordAtoms(chainAssign2, seqId2, compId2, 'H', False)
                        self.selectAuxCoordAtoms(chainAssign3, seqId3, compId3, 'HA', False)
                        if len(self.auxAtomSelectionSet) == 2:
                            print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} (index={index}) angleName={angleName} "
                                  f"A={A} B={B} C={C} phase={phase} "
                                  f"atom1={self.auxAtomSelectionSet[0][0]} atom2={self.auxAtomSelectionSet[1][0]} {dstFunc}")
                            continue
                    else:
                        print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} (index={index}) angleName={angleName} "
                              f"A={A} B={B} C={C} phase={phase} "
                              f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} {dstFunc}")

        finally:
            self.numberSelection.clear()

    def validateCoupRange(self, index, weight, target_value, lower_limit, upper_limit):
        """ Validate scalar J-coupling value range.
        """

        validRange = True
        dstFunc = {'weight': weight}

        if target_value is not None:
            if RDC_ERROR_MIN < target_value < RDC_ERROR_MAX:
                dstFunc['target_value'] = f"{target_value}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index)}"\
                    f"The target value='{target_value}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if lower_limit is not None:
            if RDC_ERROR_MIN <= lower_limit < RDC_ERROR_MAX:
                dstFunc['lower_limit'] = f"{lower_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index)}"\
                    f"The lower limit value='{lower_limit:.3f}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if upper_limit is not None:
            if RDC_ERROR_MIN < upper_limit <= RDC_ERROR_MAX:
                dstFunc['upper_limit'] = f"{upper_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index)}"\
                    f"The upper limit value='{upper_limit:.3f}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if target_value is not None:

            if lower_limit is not None:
                if lower_limit > target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index)}"\
                        f"The lower limit value='{lower_limit:.3f}' must be less than the target value '{target_value}'.\n"

            if upper_limit is not None:
                if upper_limit < target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(n=index)}"\
                        f"The upper limit value='{upper_limit:.3f}' must be grater than the target value '{target_value}'.\n"

        if not validRange:
            return None

        if target_value is not None:
            if RDC_RANGE_MIN <= target_value <= RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index)}"\
                    f"The target value='{target_value}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        if lower_limit is not None:
            if RDC_RANGE_MIN <= lower_limit <= RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index)}"\
                    f"The lower limit value='{lower_limit:.3f}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        if upper_limit is not None:
            if RDC_RANGE_MIN <= upper_limit <= RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index)}"\
                    f"The upper limit value='{upper_limit:.3f}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        return dstFunc

    # Enter a parse tree produced by PalesMRParser#talos_restraints.
    def enterTalos_restraints(self, ctx: PalesMRParser.Talos_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dihed'

    # Exit a parse tree produced by PalesMRParser#talos_restraints.
    def exitTalos_restraints(self, ctx: PalesMRParser.Talos_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by PalesMRParser#talos_restraint.
    def enterTalos_restraint(self, ctx: PalesMRParser.Talos_restraintContext):  # pylint: disable=unused-argument
        self.dihedRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by PalesMRParser#talos_restraint.
    def exitTalos_restraint(self, ctx: PalesMRParser.Talos_restraintContext):

        try:

            seqId = int(str(ctx.Integer(0)))
            compId = str(ctx.Simple_name(0)).upper()

            if compId not in monDict3.values() and compId not in monDict3:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Found unknown residue name {compId!r}.\n"
                return

            if compId in monDict3:
                pass
            else:
                compId = next(k for k, v in monDict3.items() if v == compId)

            if None in self.numberSelection:
                return

            # phi
            phi_target_value = self.numberSelection[0]
            psi_target_value = self.numberSelection[1]

            delta_phi_value = self.numberSelection[2]
            delta_psi_value = self.numberSelection[3]

            # dist = self.numberSelection[4]
            # s2 = self.numberSelection[5]

            # count = int(str(ctx.Integer(1)))
            # cs_count = int(str(ctx.Integer(2)))

            _class = str(ctx.Simple_name(1))

            if _class not in TALOS_PREDICTION_CLASSES:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The class name {_class!r} should be one of {TALOS_PREDICTION_CLASSES}.\n"
                return

            if _class not in TALOS_PREDICTION_MIN_CLASSES:  # ignore suspicious predictions
                return

            if not self.__hasPolySeq:
                return

            for angleName in ('PHI', 'PSI'):
                atomNames = KNOWN_ANGLE_ATOM_NAMES[angleName]
                seqOffset = KNOWN_ANGLE_SEQ_OFFSET[angleName]

                if angleName == 'PHI':
                    target_value = phi_target_value
                    lower_limit = phi_target_value - delta_phi_value
                    upper_limit = phi_target_value + delta_phi_value
                else:
                    target_value = psi_target_value
                    lower_limit = psi_target_value - delta_psi_value
                    upper_limit = psi_target_value + delta_psi_value

                dstFunc = self.validateAngleRange(None, 1.0, target_value, lower_limit, upper_limit)

                if dstFunc is None:
                    return

                atomId = next(name for name, offset in zip(atomNames, seqOffset) if offset == 0)

                chainAssign = self.assignCoordPolymerSequence(None, seqId, compId, atomId)

                if len(chainAssign) == 0:
                    self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                        f"{seqId}:{compId} is not present in the coordinates.\n"
                    return

                for chainId, cifSeqId, cifCompId in chainAssign:
                    ps = next(ps for ps in self.__polySeq if ps['auth_chain_id'] == chainId)

                    atomSelection = []

                    for atomId, offset in zip(atomNames, seqOffset):

                        atomSelection.clear()

                        _cifSeqId = cifSeqId + offset
                        _cifCompId = cifCompId if offset == 0 else (ps['comp_id'][ps['auth_seq_id'].index(_cifSeqId)] if _cifSeqId in ps['auth_seq_id'] else None)

                        if _cifCompId is None:
                            self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                                f"The sequence number '{seqId+offset}' is not present in polymer sequence of chain {chainId} of the coordinates.\n"
                            return

                        self.__ccU.updateChemCompDict(_cifCompId)

                        cifAtomId = next((cca[self.__ccU.ccaAtomId] for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == atomId), None)

                        if cifAtomId is None:
                            self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                                f"{seqId+offset}:{compId}:{atomId} is not present in the coordinates.\n"
                            return

                        atomSelection.append({'chain_id': chainId, 'seq_id': _cifSeqId, 'comp_id': _cifCompId, 'atom_id': cifAtomId})

                        if len(atomSelection) > 0:
                            self.atomSelectionSet.append(atomSelection)

                    if len(self.atomSelectionSet) < 4:
                        return

                    if not self.areUniqueCoordAtoms('a Torsion angle (TALOS)'):
                        return

                    for atom1, atom2, atom3, atom4 in itertools.product(self.atomSelectionSet[0],
                                                                        self.atomSelectionSet[1],
                                                                        self.atomSelectionSet[2],
                                                                        self.atomSelectionSet[3]):
                        if atom1['chain_id'] != atom2['chain_id'] or atom2['chain_id'] != atom3['chain_id']\
                           or atom3['chain_id'] != atom4['chain_id']:
                            continue
                        if self.__debug:
                            print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} angleName={angleName} className={_class} "
                                  f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} {dstFunc}")

        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by PalesMRParser#number.
    def enterNumber(self, ctx: PalesMRParser.NumberContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by PalesMRParser#number.
    def exitNumber(self, ctx: PalesMRParser.NumberContext):
        if ctx.Float():
            self.numberSelection.append(float(str(ctx.Float())))

        elif ctx.Integer():
            self.numberSelection.append(float(str(ctx.Integer())))

        else:
            self.numberSelection.append(None)

    def __getCurrentRestraint(self, n=None, g=None):
        if self.__cur_subtype == 'dist':
            return f"[Check the {self.distRestraints}th row of distance restraints (index={n}, group={g})] "
        if self.__cur_subtype == 'dihed':
            if n is not None:
                return f"[Check the {self.dihedRestraints}th row of torsion angle restraints (index={n})] "
            return f"[Check the {self.dihedRestraints}th row of torsion angle restraints] "
        if self.__cur_subtype == 'rdc':
            return f"[Check the {self.rdcRestraints}th row of residual dipolar coupling restraints] "
        if self.__cur_subtype == 'jcoup':
            return f"[Check the {self.jcoupRestraints}th row of scalar coupling constant restraints (index={n})] "
        return ''

    def getContentSubtype(self):
        """ Return content subtype of PALES MR file.
        """

        contentSubtype = {'dist_restraint': self.distRestraints,
                          'dihed_restraint': self.dihedRestraints,
                          'rdc_restraint': self.rdcRestraints,
                          'jcoup_restraint': self.jcoupRestraints
                          }

        return {k: 1 for k, v in contentSubtype.items() if v > 0}

    def getPolymerSequence(self):
        """ Return polymer sequence of PALES MR file.
        """
        return self.__polySeqRst

    def getSequenceAlignment(self):
        """ Return sequence alignment between coordinates and PALES MR.
        """
        return self.__seqAlign

    def getChainAssignment(self):
        """ Return chain assignment between coordinates and PALES MR.
        """
        return self.__chainAssign

    def getReasonsForReparsing(self):
        """ Return reasons for re-parsing PALES MR file.
        """
        return self.reasonsForReParsing


# del PalesMRParser
