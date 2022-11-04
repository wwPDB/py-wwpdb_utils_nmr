##
# File: GromacsMRParserListener.py
# Date: 02-June-2022
#
# Updates:
# Generated from GromacsMRParser.g4 by ANTLR 4.11.1
""" ParserLister class for GROMACS MR files.
    @author: Masashi Yokochi
"""
import sys
import itertools
import numpy

from antlr4 import ParseTreeListener

try:
    from wwpdb.utils.align.alignlib import PairwiseAlign  # pylint: disable=no-name-in-module
    from wwpdb.utils.nmr.mr.GromacsMRParser import GromacsMRParser
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (coordAssemblyChecker,
                                                       isLongRangeRestraint,
                                                       getTypeOfDihedralRestraint,
                                                       getRestraintName,
                                                       contentSubtypeOf,
                                                       incListIdCounter,
                                                       getSaveframe,
                                                       getLoop,
                                                       getRow,
                                                       getDistConstraintType,
                                                       getPotentialType,
                                                       ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS,
                                                       REPRESENTATIVE_MODEL_ID,
                                                       THRESHHOLD_FOR_CIRCULAR_SHIFT,
                                                       DIST_RESTRAINT_RANGE,
                                                       DIST_RESTRAINT_ERROR,
                                                       ANGLE_RESTRAINT_RANGE,
                                                       ANGLE_RESTRAINT_ERROR,
                                                       RDC_RESTRAINT_RANGE,
                                                       RDC_RESTRAINT_ERROR)
    from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
    from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from wwpdb.utils.nmr.NEFTranslator.NEFTranslator import NEFTranslator
    from wwpdb.utils.nmr.AlignUtil import (updatePolySeqRstFromAtomSelectionSet,
                                           sortPolySeqRst,
                                           alignPolymerSequence,
                                           assignPolymerSequence,
                                           trimSequenceAlignment)
except ImportError:
    from nmr.align.alignlib import PairwiseAlign  # pylint: disable=no-name-in-module
    from nmr.mr.GromacsMRParser import GromacsMRParser
    from nmr.mr.ParserListenerUtil import (coordAssemblyChecker,
                                           isLongRangeRestraint,
                                           getTypeOfDihedralRestraint,
                                           getRestraintName,
                                           contentSubtypeOf,
                                           incListIdCounter,
                                           getSaveframe,
                                           getLoop,
                                           getRow,
                                           getDistConstraintType,
                                           getPotentialType,
                                           ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS,
                                           REPRESENTATIVE_MODEL_ID,
                                           THRESHHOLD_FOR_CIRCULAR_SHIFT,
                                           DIST_RESTRAINT_RANGE,
                                           DIST_RESTRAINT_ERROR,
                                           ANGLE_RESTRAINT_RANGE,
                                           ANGLE_RESTRAINT_ERROR,
                                           RDC_RESTRAINT_RANGE,
                                           RDC_RESTRAINT_ERROR)
    from nmr.ChemCompUtil import ChemCompUtil
    from nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from nmr.NEFTranslator.NEFTranslator import NEFTranslator
    from nmr.AlignUtil import (updatePolySeqRstFromAtomSelectionSet,
                               sortPolySeqRst,
                               alignPolymerSequence,
                               assignPolymerSequence,
                               trimSequenceAlignment)


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

    __file_type = 'nm-res-gro'

    # __verbose = None
    # __lfh = None
    __debug = False

    __createSfDict = False
    __omitDistLimitOutlier = True
    __correctCircularShift = True

    # atom name mapping of public MR file between the archive coordinates and submitted ones
    # __mrAtomNameMapping = None

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

    # coordinates information generated by ParserListenerUtil.coordAssemblyChecker()
    __polySeq = None
    # __altPolySeq = None
    # __coordAtomSite = None
    # __coordUnobsRes = None
    # __labelToAuthSeq = None
    # __authToLabelSeq = None
    __authToStarSeq = None

    __hasPolySeq = False
    __preferAuthSeq = True
    __gapInAuthSeq = False

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

    # original source MR file name
    __originalFileName = '.'

    # list id counter
    __listIdCounter = {}

    # entry ID
    __entryId = '.'

    # dictionary of pynmrstar saveframes
    sfDict = {}

    def __init__(self, verbose=True, log=sys.stdout,
                 representativeModelId=REPRESENTATIVE_MODEL_ID,
                 mrAtomNameMapping=None,   # pylint: disable=unused-argument
                 cR=None, caC=None, ccU=None, csStat=None, nefT=None,
                 atomNumberDict=None):
        # self.__verbose = verbose
        # self.__lfh = log

        # self.__mrAtomNameMapping = None if mrAtomNameMapping is None or len(mrAtomNameMapping) == 0 else mrAtomNameMapping

        # self.__cR = cR
        self.__hasCoord = cR is not None

        if self.__hasCoord:
            ret = coordAssemblyChecker(verbose, log, representativeModelId, cR, caC)
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
            self.__authToStarSeq = ret['auth_to_star_seq']

        self.__hasPolySeq = self.__polySeq is not None and len(self.__polySeq) > 0
        if self.__hasPolySeq:
            self.__gapInAuthSeq = any(ps for ps in self.__polySeq if ps['gap_in_auth_seq'])

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

        self.distRestraints = 0      # GROMACS: Distance restraints
        self.angRestraints = 0       # GROMACS: Angle restraints
        self.dihedRestraints = 0     # GROMACS: Dihedral angle restraints
        self.rdcRestraints = 0       # GROMACS: Residual dipolar coupling restraints
        self.geoRestraints = 0       # GROMACS: Coordinate geometry restraints

    def setDebugMode(self, debug):
        self.__debug = debug

    def createSfDict(self, createSfDict):
        self.__createSfDict = createSfDict

    def setOriginaFileName(self, originalFileName):
        self.__originalFileName = originalFileName

    def setListIdCounter(self, listIdCounter):
        self.__listIdCounter = listIdCounter

    def setEntryId(self, entryId):
        self.__entryId = entryId

    # Enter a parse tree produced by GromacsMRParser#gromacs_mr.
    def enterGromacs_mr(self, ctx: GromacsMRParser.Gromacs_mrContext):  # pylint: disable=unused-argument
        self.__polySeqRst = []

    # Exit a parse tree produced by GromacsMRParser#gromacs_mr.
    def exitGromacs_mr(self, ctx: GromacsMRParser.Gromacs_mrContext):  # pylint: disable=unused-argument
        if self.__hasPolySeq and self.__polySeqRst is not None:
            sortPolySeqRst(self.__polySeqRst)

            self.__seqAlign, _ = alignPolymerSequence(self.__pA, self.__polySeq, self.__polySeqRst)
            self.__chainAssign, message = assignPolymerSequence(self.__pA, self.__ccU, self.__file_type, self.__polySeq, self.__polySeqRst, self.__seqAlign)

            if len(message) > 0:
                self.warningMessage += message

            if self.__chainAssign is not None:

                if len(self.__polySeq) == len(self.__polySeqRst):

                    chain_mapping = {}

                    for ca in self.__chainAssign:
                        ref_chain_id = ca['ref_chain_id']
                        test_chain_id = ca['test_chain_id']

                        if ref_chain_id != test_chain_id:
                            chain_mapping[test_chain_id] = ref_chain_id

                    if len(chain_mapping) == len(self.__polySeq):

                        for ps in self.__polySeqRst:
                            if ps['chain_id'] in chain_mapping:
                                ps['chain_id'] = chain_mapping[ps['chain_id']]

                        self.__seqAlign, _ = alignPolymerSequence(self.__pA, self.__polySeq, self.__polySeqRst)
                        self.__chainAssign, _ = assignPolymerSequence(self.__pA, self.__ccU, self.__file_type, self.__polySeq, self.__polySeqRst, self.__seqAlign)

                trimSequenceAlignment(self.__seqAlign, self.__chainAssign)

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

            if weight < 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(n=index)}"\
                    f"The relative weight value of '{weight}' must not be a negative value.\n"
                return
            if weight == 0.0:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(n=index)}"\
                    f"The relative weight value of '{weight}' should be a positive value.\n"

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
                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint(n=index)}"\
                    f"'ai={ai}' is not defined in the GROMACS parameter/topology file.\n"

            atomSelection.clear()

            if aj in self.__atomNumberDict:
                atomSelection.append(self.__atomNumberDict[aj])
                self.atomSelectionSet.append(atomSelection)
            else:
                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint(n=index)}"\
                    f"'aj={aj}' is not defined in the GROMACS parameter/topology file.\n"

            if len(self.atomSelectionSet) < 2:
                return

            if self.__createSfDict:
                sf = self.__getSf(constraintType=getDistConstraintType(self.atomSelectionSet),
                                  potentialType=getPotentialType(self.__file_type, self.__cur_subtype, dstFunc))
                sf['id'] += 1
                memberLogicCode = '.' if len(self.atomSelectionSet[0]) * len(self.atomSelectionSet[1]) > 1 else 'OR'

            updatePolySeqRstFromAtomSelectionSet(self.__polySeqRst, self.atomSelectionSet)

            for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                  self.atomSelectionSet[1]):
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} id={self.distRestraints} (index={index}) "
                          f"atom1={atom1} atom2={atom2} {dstFunc}")
                if self.__createSfDict and sf is not None:
                    sf['index_id'] += 1
                    row = getRow(self.__cur_subtype, sf['id'], sf['index_id'],
                                 '.', memberLogicCode,
                                 sf['list_id'], self.__entryId, dstFunc, self.__authToStarSeq, atom1, atom2)
                    sf['loop'].add_data(row)

        except ValueError:
            self.distRestraints -= 1
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
                if (upper_limit <= DIST_ERROR_MIN or upper_limit > DIST_ERROR_MAX) and omit_dist_limit_outlier:
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
                if (upper_linear_limit <= DIST_ERROR_MIN or upper_linear_limit > DIST_ERROR_MAX) and omit_dist_limit_outlier:
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

            if delta > 0.0:
                lower_limit = target_value - delta
                upper_limit = target_value + delta
            else:
                lower_limit = upper_limit = None

            if funct != 1:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Unknown function type '{funct}' is set.\n"
                return

            if weight < 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The relative weight value of '{weight}' must not be a negative value.\n"
                return
            if weight == 0.0:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The relative weight value of '{weight}' should be a positive value.\n"

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
                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                    f"'ai={ai}' is not defined in the GROMACS parameter/topology file.\n"

            atomSelection.clear()

            if aj in self.__atomNumberDict:
                atomSelection.append(self.__atomNumberDict[aj])
                self.atomSelectionSet.append(atomSelection)
            else:
                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                    f"'aj={aj}' is not defined in the GROMACS parameter/topology file.\n"

            atomSelection.clear()

            if ak in self.__atomNumberDict:
                atomSelection.append(self.__atomNumberDict[ak])
                self.atomSelectionSet.append(atomSelection)
            else:
                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                    f"'ak={ak}' is not defined in the GROMACS parameter/topology file.\n"

            atomSelection.clear()

            if al in self.__atomNumberDict:
                atomSelection.append(self.__atomNumberDict[al])
                self.atomSelectionSet.append(atomSelection)
            else:
                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                    f"'al={al}' is not defined in the GROMACS parameter/topology file.\n"

            if len(self.atomSelectionSet) < 4:
                return

            if self.__createSfDict:
                sf = self.__getSf(potentialType=getPotentialType(self.__file_type, self.__cur_subtype, dstFunc))
                sf['id'] += 1

            updatePolySeqRstFromAtomSelectionSet(self.__polySeqRst, self.atomSelectionSet)

            compId = self.atomSelectionSet[0][0]['comp_id']
            peptide, nucleotide, carbohydrate = self.__csStat.getTypeOfCompId(compId)

            for atom1, atom2, atom3, atom4 in itertools.product(self.atomSelectionSet[0],
                                                                self.atomSelectionSet[1],
                                                                self.atomSelectionSet[2],
                                                                self.atomSelectionSet[3]):
                angleName = getTypeOfDihedralRestraint(peptide, nucleotide, carbohydrate,
                                                       [atom1, atom2, atom3, atom4])
                if angleName is None:
                    continue
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} angleName={angleName} "
                          f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} {dstFunc}")
                if self.__createSfDict and sf is not None:
                    sf['index_id'] += 1
                    row = getRow(self.__cur_subtype, sf['id'], sf['index_id'],
                                 '.', angleName,
                                 sf['list_id'], self.__entryId, dstFunc, self.__authToStarSeq, atom1, atom2, atom3, atom4)
                    sf['loop'].add_data(row)

        except ValueError:
            self.dihedRestraints -= 1
        finally:
            self.numberSelection.clear()

    def validateAngleRange(self, weight, target_value, lower_limit, upper_limit):
        """ Validate angle value range.
        """

        validRange = True
        dstFunc = {'weight': weight}

        if self.__correctCircularShift:
            _array = numpy.array([target_value, lower_limit, upper_limit],
                                 dtype=float)

            shift = None
            if numpy.nanmin(_array) >= THRESHHOLD_FOR_CIRCULAR_SHIFT:
                shift = -(numpy.nanmax(_array) // 360) * 360
            elif numpy.nanmax(_array) <= -THRESHHOLD_FOR_CIRCULAR_SHIFT:
                shift = -(numpy.nanmin(_array) // 360) * 360
            if shift is not None:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    "The target/limit values for an angle restraint have been circularly shifted "\
                    f"to fit within range {ANGLE_RESTRAINT_ERROR}.\n"
                if target_value is not None:
                    target_value += shift
                if lower_limit is not None:
                    lower_limit += shift
                if upper_limit is not None:
                    upper_limit += shift

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

            if weight < 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                    f"The relative weight value of '{weight}' must not be a negative value.\n"
                return
            if weight == 0.0:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                    f"The relative weight value of '{weight}' should be a positive value.\n"

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
                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                    f"'ai={ai}' is not defined in the GROMACS parameter/topology file.\n"

            atomSelection.clear()

            if aj in self.__atomNumberDict:
                atomSelection.append(self.__atomNumberDict[aj])
                self.atomSelectionSet.append(atomSelection)
            else:
                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
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
                ps1 = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chain_id_1 and 'identical_auth_chain_id' in ps), None)
                ps2 = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chain_id_2 and 'identical_auth_chain_id' in ps), None)
                if ps1 is None and ps2 is None:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                        f"Found inter-chain RDC vector; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                    return

            elif abs(seq_id_1 - seq_id_2) > 1:
                ps1 = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chain_id_1 and 'gap_in_auth_seq' in ps and ps['gap_in_auth_seq']), None)
                if ps1 is None:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                        f"Found inter-residue RDC vector; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                    return

            elif abs(seq_id_1 - seq_id_2) == 1:

                if self.__csStat.peptideLike(comp_id_1) and self.__csStat.peptideLike(comp_id_2) and\
                        ((seq_id_1 < seq_id_2 and atom_id_1 == 'C' and atom_id_2 in ('N', 'H', 'CA'))
                         or (seq_id_1 > seq_id_2 and atom_id_1 in ('N', 'H', 'CA') and atom_id_2 == 'C')
                         or (seq_id_1 < seq_id_2 and atom_id_1.startswith('HA') and atom_id_2 == 'H')
                         or (seq_id_1 > seq_id_2 and atom_id_1 == 'H' and atom_id_2.startswith('HA'))):
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

            elif self.__ccU.updateChemCompDict(comp_id_1):  # matches with comp_id in CCD

                if not any(b for b in self.__ccU.lastBonds
                           if ((b[self.__ccU.ccbAtomId1] == atom_id_1 and b[self.__ccU.ccbAtomId2] == atom_id_2)
                               or (b[self.__ccU.ccbAtomId1] == atom_id_2 and b[self.__ccU.ccbAtomId2] == atom_id_1))):

                    if self.__nefT.validate_comp_atom(comp_id_1, atom_id_1) and self.__nefT.validate_comp_atom(comp_id_2, atom_id_2):
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                            "Found an RDC vector over multiple covalent bonds; "\
                            f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                        return

            if self.__createSfDict:
                sf = self.__getSf(potentialType=getPotentialType(self.__file_type, self.__cur_subtype, dstFunc))
                sf['id'] += 1

            updatePolySeqRstFromAtomSelectionSet(self.__polySeqRst, self.atomSelectionSet)

            for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                  self.atomSelectionSet[1]):
                if isLongRangeRestraint([atom1, atom2], self.__polySeq if self.__gapInAuthSeq else None):
                    continue
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} id={self.rdcRestraints} exp={exp} index={index} "
                          f"atom1={atom1} atom2={atom2} {dstFunc}")
                if self.__createSfDict and sf is not None:
                    sf['index_id'] += 1
                    row = getRow(self.__cur_subtype, sf['id'], sf['index_id'],
                                 '.', None,
                                 sf['list_id'], self.__entryId, dstFunc, self.__authToStarSeq, atom1, atom2)
                    sf['loop'].add_data(row)

        except ValueError:
            self.rdcRestraints -= 1
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
                dstFunc['lower_limit'] = f"{lower_limit:.6f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                    f"The lower limit value='{lower_limit:.6f}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if upper_limit is not None:
            if RDC_ERROR_MIN < upper_limit <= RDC_ERROR_MAX:
                dstFunc['upper_limit'] = f"{upper_limit:.6f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                    f"The upper limit value='{upper_limit:.6f}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if target_value is not None:

            if lower_limit is not None:
                if lower_limit > target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                        f"The lower limit value='{lower_limit:.6f}' must be less than the target value '{target_value}'.\n"

            if upper_limit is not None:
                if upper_limit < target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                        f"The upper limit value='{upper_limit:.6f}' must be greater than the target value '{target_value}'.\n"

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
                    f"The lower limit value='{lower_limit:.6f}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        if upper_limit is not None:
            if RDC_RANGE_MIN <= upper_limit <= RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint(dataset=exp,n=index)}"\
                    f"The upper limit value='{upper_limit:.6f}' should be within range {RDC_RESTRAINT_RANGE}.\n"

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

            if delta > 0.0:
                lower_limit = target_value - delta
                upper_limit = target_value + delta
            else:
                lower_limit = upper_limit = None

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
                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                    f"'ai={ai}' is not defined in the GROMACS parameter/topology file.\n"

            atomSelection.clear()

            if aj in self.__atomNumberDict:
                atomSelection.append(self.__atomNumberDict[aj])
                self.atomSelectionSet.append(atomSelection)
            else:
                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                    f"'aj={aj}' is not defined in the GROMACS parameter/topology file.\n"

            atomSelection.clear()

            if ak in self.__atomNumberDict:
                atomSelection.append(self.__atomNumberDict[ak])
                self.atomSelectionSet.append(atomSelection)
            else:
                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                    f"'ak={ak}' is not defined in the GROMACS parameter/topology file.\n"

            atomSelection.clear()

            if al in self.__atomNumberDict:
                atomSelection.append(self.__atomNumberDict[al])
                self.atomSelectionSet.append(atomSelection)
            else:
                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                    f"'al={al}' is not defined in the GROMACS parameter/topology file.\n"

            if len(self.atomSelectionSet) < 4:
                return

            if self.__createSfDict:
                sf = self.__getSf('angle restraint' if len_atom_sorts == 3 else 'angle restraint (intervector projection angle)')
                sf['id'] += 1
                if len(sf['loop']['tags']) == 0:
                    if len_atom_sorts == 3:
                        sf['loop']['tags'] = ['index_id', 'id',
                                              'auth_asym_id_1', 'auth_seq_id_1', 'auth_comp_id_1', 'auth_atom_id_1',
                                              'auth_asym_id_2', 'auth_seq_id_2', 'auth_comp_id_2', 'auth_atom_id_2',
                                              'auth_asym_id_3', 'auth_seq_id_3', 'auth_comp_id_3', 'auth_atom_id_3',
                                              'target_value', 'target_value_uncertainty',
                                              'lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit',
                                              'multiplicity',
                                              'list_id', 'entry_id']
                    else:
                        sf['loop']['tags'] = ['index_id', 'id',
                                              'auth_asym_id_1', 'auth_seq_id_1', 'auth_comp_id_1', 'auth_atom_id_1',
                                              'auth_asym_id_2', 'auth_seq_id_2', 'auth_comp_id_2', 'auth_atom_id_2',
                                              'auth_asym_id_3', 'auth_seq_id_3', 'auth_comp_id_3', 'auth_atom_id_3',
                                              'auth_asym_id_4', 'auth_seq_id_4', 'auth_comp_id_4', 'auth_atom_id_4',
                                              'target_value', 'target_value_uncertainty',
                                              'lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit',
                                              'multiplicity',
                                              'list_id', 'entry_id']

            updatePolySeqRstFromAtomSelectionSet(self.__polySeqRst, self.atomSelectionSet)

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
                    if isLongRangeRestraint([atom1, atom2, atom3], self.__polySeq if self.__gapInAuthSeq else None):
                        continue
                    if self.__debug:
                        print(f"subtype={self.__cur_subtype} id={self.angRestraints} mult={mult} "
                              f"atom1={atom1} atom2={atom2} atom3={atom3} {dstFunc}")
                    if self.__createSfDict and sf is not None:
                        sf['index_id'] += 1
                        sf['loop']['data'].append([sf['index_id'], sf['id'],
                                                   atom1['chain_id'], atom1['seq_id'], atom1['comp_id'], atom1['atom_id'],
                                                   atom2['chain_id'], atom2['seq_id'], atom2['comp_id'], atom2['atom_id'],
                                                   atom3['chain_id'], atom3['seq_id'], atom3['comp_id'], atom3['atom_id'],
                                                   dstFunc['target_value'] if 'target_value' in dstFunc else None, None,
                                                   dstFunc['lower_linear_limit'] if 'lower_linear_limit' in dstFunc else None,
                                                   dstFunc['lower_limit'] if 'lower_limit' in dstFunc else None,
                                                   dstFunc['upper_limit'] if 'upper_limit' in dstFunc else None,
                                                   dstFunc['upper_linear_limit'] if 'upper_linear_limit' in dstFunc else None,
                                                   mult,
                                                   sf['list_id'], self.__entryId])

            else:

                for atom1, atom2, atom3, atom4 in itertools.product(self.atomSelectionSet[0],
                                                                    self.atomSelectionSet[1],
                                                                    self.atomSelectionSet[2],
                                                                    self.atomSelectionSet[3]):
                    if isLongRangeRestraint([atom1, atom2, atom3, atom4], self.__polySeq if self.__gapInAuthSeq else None):
                        continue
                    if self.__debug:
                        print(f"subtype={self.__cur_subtype} id={self.angRestraints} mult={mult} "
                              f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} {dstFunc}")
                    if self.__createSfDict and sf is not None:
                        sf['index_id'] += 1
                        sf['loop']['data'].append([sf['index_id'], sf['id'],
                                                   atom1['chain_id'], atom1['seq_id'], atom1['comp_id'], atom1['atom_id'],
                                                   atom2['chain_id'], atom2['seq_id'], atom2['comp_id'], atom2['atom_id'],
                                                   atom3['chain_id'], atom3['seq_id'], atom3['comp_id'], atom3['atom_id'],
                                                   atom4['chain_id'], atom4['seq_id'], atom4['comp_id'], atom4['atom_id'],
                                                   dstFunc['target_value'] if 'target_value' in dstFunc else None, None,
                                                   dstFunc['lower_linear_limit'] if 'lower_linear_limit' in dstFunc else None,
                                                   dstFunc['lower_limit'] if 'lower_limit' in dstFunc else None,
                                                   dstFunc['upper_limit'] if 'upper_limit' in dstFunc else None,
                                                   dstFunc['upper_linear_limit'] if 'upper_linear_limit' in dstFunc else None,
                                                   mult,
                                                   sf['list_id'], self.__entryId])

        except ValueError:
            self.angRestraints -= 1
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

            if delta > 0.0:
                lower_limit = target_value - delta
                upper_limit = target_value + delta
            else:
                lower_limit = upper_limit = None

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
                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                    f"'ai={ai}' is not defined in the GROMACS parameter/topology file.\n"

            atomSelection.clear()

            if aj in self.__atomNumberDict:
                atomSelection.append(self.__atomNumberDict[aj])
                self.atomSelectionSet.append(atomSelection)
            else:
                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                    f"'aj={aj}' is not defined in the GROMACS parameter/topology file.\n"

            if len(self.atomSelectionSet) < 2:
                return

            if self.__createSfDict:
                sf = self.__getSf('angle restraint (intervector projection angle with z-axis)')
                sf['id'] += 1
                if len(sf['loop']['tags']) == 0:
                    sf['loop']['tags'] = ['index_id', 'id',
                                          'auth_asym_id_1', 'auth_seq_id_1', 'auth_comp_id_1', 'auth_atom_id_1',
                                          'auth_asym_id_2', 'auth_seq_id_2', 'auth_comp_id_2', 'auth_atom_id_2',
                                          'target_value', 'target_value_uncertainty',
                                          'lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit',
                                          'multiplicity',
                                          'list_id', 'entry_id']

            updatePolySeqRstFromAtomSelectionSet(self.__polySeqRst, self.atomSelectionSet)

            for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                  self.atomSelectionSet[1]):
                if isLongRangeRestraint([atom1, atom2], self.__polySeq if self.__gapInAuthSeq else None):
                    continue
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} id={self.angRestraints} mult={mult} "
                          f"atom1={atom1} atom2={atom2} z-axis {dstFunc}")
                if self.__createSfDict and sf is not None:
                    sf['index_id'] += 1
                    sf['loop']['data'].append([sf['index_id'], sf['id'],
                                               atom1['chain_id'], atom1['seq_id'], atom1['comp_id'], atom1['atom_id'],
                                               atom2['chain_id'], atom2['seq_id'], atom2['comp_id'], atom2['atom_id'],
                                               dstFunc['target_value'] if 'target_value' in dstFunc else None, None,
                                               dstFunc['lower_linear_limit'] if 'lower_linear_limit' in dstFunc else None,
                                               dstFunc['lower_limit'] if 'lower_limit' in dstFunc else None,
                                               dstFunc['upper_limit'] if 'upper_limit' in dstFunc else None,
                                               dstFunc['upper_linear_limit'] if 'upper_linear_limit' in dstFunc else None,
                                               mult,
                                               sf['list_id'], self.__entryId])

        except ValueError:
            self.angRestraints -= 1
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
                self.warningMessage += f"[Missing data] {self.__getCurrentRestraint()}"\
                    f"'ai={ai}' is not defined in the GROMACS parameter/topology file.\n"

            if len(self.atomSelectionSet) < 1:
                return

            if self.__createSfDict:
                sf = self.__getSf('harmonic coordinate restraint, GROMACS position restraint')
                sf['id'] += 1
                if len(sf['loop']['tags']) == 0:
                    if funct == 1:
                        sf['loop']['tags'] = ['index_id', 'id',
                                              'auth_asym_id', 'auth_seq_id', 'auth_comp_id', 'auth_atom_id',
                                              'kx', 'ky', 'kz',
                                              'list_id', 'entry_id']
                    else:
                        sf['loop']['tags'] = ['index_id', 'id',
                                              'auth_asym_id', 'auth_seq_id', 'auth_comp_id', 'auth_atom_id',
                                              'g', 'r', 'k',
                                              'list_id', 'entry_id']

            updatePolySeqRstFromAtomSelectionSet(self.__polySeqRst, self.atomSelectionSet)

            for atom1 in self.atomSelectionSet[0]:
                if self.__debug:
                    if funct == 1:
                        print(f"subtype={self.__cur_subtype} id={self.geoRestraints} "
                              f"atom={atom1} (kx, ky, kz)=({a}, {b}, {c})")
                    else:
                        print(f"subtype={self.__cur_subtype} id={self.geoRestraints} "
                              f"atom={atom1} (g, r, k)=({a}, {b}, {c})")
                if self.__createSfDict and sf is not None:
                    sf['index_id'] += 1
                    sf['loop']['data'].append([sf['index_id'], sf['id'],
                                               atom1['chain_id'], atom1['seq_id'], atom1['comp_id'], atom1['atom_id'],
                                               a, b, c,
                                               sf['list_id'], self.__entryId])

        except ValueError:
            self.geoRestraints -= 1
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

    def __addSf(self, constraintType=None, potentialType=None):
        content_subtype = contentSubtypeOf(self.__cur_subtype)

        if content_subtype is None:
            return

        self.__listIdCounter = incListIdCounter(self.__cur_subtype, self.__listIdCounter)

        key = (self.__cur_subtype, constraintType, potentialType, None)

        if key not in self.sfDict:
            self.sfDict[key] = []

        list_id = self.__listIdCounter[content_subtype]

        sf_framecode = 'GROMACS_' + getRestraintName(self.__cur_subtype, False).replace(' ', '_') + f'_{list_id}'

        sf = getSaveframe(self.__cur_subtype, sf_framecode, list_id, self.__entryId, self.__originalFileName,
                          constraintType=constraintType, potentialType=potentialType)

        not_valid = True

        lp = getLoop(self.__cur_subtype)
        if not isinstance(lp, dict):
            sf.add_loop(lp)
            not_valid = False

        item = {'file_type': self.__file_type, 'saveframe': sf, 'loop': lp, 'list_id': list_id,
                'id': 0, 'index_id': 0}

        if not_valid:
            item['tags'] = []

        self.sfDict[key].append(item)

    def __getSf(self, constraintType=None, potentialType=None):
        key = (self.__cur_subtype, constraintType, potentialType, None)

        if key not in self.sfDict:
            replaced = False
            if potentialType is not None:
                old_key = (self.__cur_subtype, constraintType, None, None)
                if old_key in self.sfDict:
                    replaced = True
                    self.sfDict[key] = [self.sfDict[old_key][-1]]
                    del self.sfDict[old_key][-1]
                    if len(self.sfDict[old_key]) == 0:
                        del self.sfDict[old_key]
                    sf = self.sfDict[key][-1]['saveframe']
                    idx = next((idx for idx, t in enumerate(sf.tags) if t[0] == 'Potential_type'), -1)
                    if idx != -1:
                        sf.tags[idx][1] = potentialType
                    else:
                        sf.add_tag('Potential_type', potentialType)
            if not replaced:
                self.__addSf(constraintType=constraintType, potentialType=potentialType)

        return self.sfDict[key][-1]

    def getContentSubtype(self):
        """ Return content subtype of GROMACS MR file.
        """

        contentSubtype = {'dist_restraint': self.distRestraints,
                          'ang_restraint': self.angRestraints,
                          'dihed_restraint': self.dihedRestraints,
                          'rdc_restraint': self.rdcRestraints,
                          'geo_restraint': self.geoRestraints
                          }

        return {k: 1 for k, v in contentSubtype.items() if v > 0}

    def getPolymerSequence(self):
        """ Return polymer sequence of GROMACS MR file.
        """
        return None if self.__polySeqRst is None or len(self.__polySeqRst) == 0 else self.__polySeqRst

    def getSequenceAlignment(self):
        """ Return sequence alignment between coordinates and GROMACS MR.
        """
        return None if self.__seqAlign is None or len(self.__seqAlign) == 0 else self.__seqAlign

    def getChainAssignment(self):
        """ Return chain assignment between coordinates and GROMACS MR.
        """
        return None if self.__chainAssign is None or len(self.__chainAssign) == 0 else self.__chainAssign

    def getListIdCounter(self):
        """ Return updated list id counter.
        """
        return self.__listIdCounter

    def getSfDict(self):
        """ Return a dictionary of pynmrstar saveframes.
        """
        return None if len(self.sfDict) == 0 else self.sfDict

# del GromacsMRParser
