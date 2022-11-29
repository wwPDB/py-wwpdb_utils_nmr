##
# File: CnsMRParserListener.py
# Date: 09-Feb-2022
#
# Updates:
# Generated from CnsMRParser.g4 by ANTLR 4.11.1
""" ParserLister class for CNS MR files.
    @author: Masashi Yokochi
"""
import sys
import re
import itertools
import copy
import numpy

from antlr4 import ParseTreeListener
from rmsd.calculate_rmsd import (int_atom, ELEMENT_WEIGHTS)  # noqa: F401 pylint: disable=no-name-in-module, import-error

try:
    from wwpdb.utils.align.alignlib import PairwiseAlign  # pylint: disable=no-name-in-module
    from wwpdb.utils.nmr.mr.CnsMRParser import CnsMRParser
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (toNpArray,
                                                       toRegEx, toNefEx,
                                                       coordAssemblyChecker,
                                                       extendCoordChainsForExactNoes,
                                                       translateToStdResName,
                                                       translateToStdAtomName,
                                                       hasInterChainRestraint,
                                                       isLongRangeRestraint,
                                                       isAsymmetricRangeRestraint,
                                                       isAmbigAtomSelection,
                                                       getTypeOfDihedralRestraint,
                                                       getRdcCode,
                                                       isCyclicPolymer,
                                                       getRestraintName,
                                                       contentSubtypeOf,
                                                       incListIdCounter,
                                                       getSaveframe,
                                                       getLoop,
                                                       getAuxLoops,
                                                       getRow,
                                                       getAuxRow,
                                                       getDistConstraintType,
                                                       getPotentialType,
                                                       ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS,
                                                       REPRESENTATIVE_MODEL_ID,
                                                       MAX_PREF_LABEL_SCHEME_COUNT,
                                                       THRESHHOLD_FOR_CIRCULAR_SHIFT,
                                                       DIST_RESTRAINT_RANGE,
                                                       DIST_RESTRAINT_ERROR,
                                                       ANGLE_RESTRAINT_RANGE,
                                                       ANGLE_RESTRAINT_ERROR,
                                                       RDC_RESTRAINT_RANGE,
                                                       RDC_RESTRAINT_ERROR,
                                                       CS_RESTRAINT_RANGE,
                                                       CS_RESTRAINT_ERROR,
                                                       T1T2_RESTRAINT_RANGE,
                                                       T1T2_RESTRAINT_ERROR,
                                                       DIST_AMBIG_LOW,
                                                       DIST_AMBIG_UP,
                                                       XPLOR_RDC_PRINCIPAL_AXIS_NAMES,
                                                       XPLOR_NITROXIDE_NAMES,
                                                       XPLOR_ORIGIN_AXIS_COLS)
    from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
    from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from wwpdb.utils.nmr.NEFTranslator.NEFTranslator import NEFTranslator
    from wwpdb.utils.nmr.AlignUtil import (LEN_MAJOR_ASYM_ID_SET,
                                           MAJOR_ASYM_ID_SET,
                                           MAX_MAG_IDENT_ASYM_ID,
                                           monDict3,
                                           updatePolySeqRst,
                                           sortPolySeqRst,
                                           alignPolymerSequence,
                                           assignPolymerSequence,
                                           trimSequenceAlignment,
                                           retrieveAtomIdentFromMRMap,
                                           retrieveAtomIdFromMRMap,
                                           retrieveRemappedSeqId,
                                           splitPolySeqRstForMultimers,
                                           splitPolySeqRstForExactNoes,
                                           retrieveRemappedChainId,
                                           splitPolySeqRstForNonPoly,
                                           retrieveRemappedNonPoly,
                                           splitPolySeqRstForBranched,
                                           retrieveOriginalSeqIdFromMRMap)
except ImportError:
    from nmr.align.alignlib import PairwiseAlign  # pylint: disable=no-name-in-module
    from nmr.mr.CnsMRParser import CnsMRParser
    from nmr.mr.ParserListenerUtil import (toNpArray,
                                           toRegEx, toNefEx,
                                           coordAssemblyChecker,
                                           extendCoordChainsForExactNoes,
                                           translateToStdResName,
                                           translateToStdAtomName,
                                           hasInterChainRestraint,
                                           isLongRangeRestraint,
                                           isAsymmetricRangeRestraint,
                                           isAmbigAtomSelection,
                                           getTypeOfDihedralRestraint,
                                           getRdcCode,
                                           isCyclicPolymer,
                                           getRestraintName,
                                           contentSubtypeOf,
                                           incListIdCounter,
                                           getSaveframe,
                                           getLoop,
                                           getAuxLoops,
                                           getRow,
                                           getAuxRow,
                                           getDistConstraintType,
                                           getPotentialType,
                                           ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS,
                                           REPRESENTATIVE_MODEL_ID,
                                           MAX_PREF_LABEL_SCHEME_COUNT,
                                           THRESHHOLD_FOR_CIRCULAR_SHIFT,
                                           DIST_RESTRAINT_RANGE,
                                           DIST_RESTRAINT_ERROR,
                                           ANGLE_RESTRAINT_RANGE,
                                           ANGLE_RESTRAINT_ERROR,
                                           RDC_RESTRAINT_RANGE,
                                           RDC_RESTRAINT_ERROR,
                                           CS_RESTRAINT_RANGE,
                                           CS_RESTRAINT_ERROR,
                                           T1T2_RESTRAINT_RANGE,
                                           T1T2_RESTRAINT_ERROR,
                                           DIST_AMBIG_LOW,
                                           DIST_AMBIG_UP,
                                           XPLOR_RDC_PRINCIPAL_AXIS_NAMES,
                                           XPLOR_NITROXIDE_NAMES,
                                           XPLOR_ORIGIN_AXIS_COLS)
    from nmr.ChemCompUtil import ChemCompUtil
    from nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from nmr.NEFTranslator.NEFTranslator import NEFTranslator
    from nmr.AlignUtil import (LEN_MAJOR_ASYM_ID_SET,
                               MAJOR_ASYM_ID_SET,
                               MAX_MAG_IDENT_ASYM_ID,
                               monDict3,
                               updatePolySeqRst,
                               sortPolySeqRst,
                               alignPolymerSequence,
                               assignPolymerSequence,
                               trimSequenceAlignment,
                               retrieveAtomIdentFromMRMap,
                               retrieveAtomIdFromMRMap,
                               retrieveRemappedSeqId,
                               splitPolySeqRstForMultimers,
                               splitPolySeqRstForExactNoes,
                               retrieveRemappedChainId,
                               splitPolySeqRstForNonPoly,
                               retrieveRemappedNonPoly,
                               splitPolySeqRstForBranched,
                               retrieveOriginalSeqIdFromMRMap)


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


CS_RANGE_MIN = CS_RESTRAINT_RANGE['min_inclusive']
CS_RANGE_MAX = CS_RESTRAINT_RANGE['max_inclusive']

CS_ERROR_MIN = CS_RESTRAINT_ERROR['min_exclusive']
CS_ERROR_MAX = CS_RESTRAINT_ERROR['max_exclusive']


T1T2_RANGE_MIN = T1T2_RESTRAINT_RANGE['min_inclusive']
T1T2_RANGE_MAX = T1T2_RESTRAINT_RANGE['max_inclusive']

T1T2_ERROR_MIN = T1T2_RESTRAINT_ERROR['min_exclusive']
T1T2_ERROR_MAX = T1T2_RESTRAINT_ERROR['max_exclusive']


# This class defines a complete listener for a parse tree produced by CnsMRParser.
class CnsMRParserListener(ParseTreeListener):

    __file_type = 'nm-res-cns'

    __verbose = None
    __lfh = None
    __debug = False
    __sel_expr_debug = False

    __createSfDict = False
    __omitDistLimitOutlier = True
    __allowZeroUpperLimit = False
    __correctCircularShift = True

    # @see: https://bmrb.io/ref_info/atom_nom.tbl
    # @see: https://bmrb.io/macro/files/xplor_to_iupac.Nov140620
    # whether to trust the ref_info or the macro for atom nomenclature of ASN/GLN amino group
    __trust_bmrb_ref_info = True

    # atom name mapping of public MR file between the archive coordinates and submitted ones
    __mrAtomNameMapping = None

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
    __cR = None
    __hasCoord = False

    # experimental method
    __exptlMethod = ''
    # whether solid-state NMR is applied to symmetric samples such as fibrils
    __symmetric = 'no'

    # data item name for model ID in 'atom_site' category
    __modelNumName = None

    # data item names for auth_asym_id, auth_seq_id, auth_atom_id in 'atom_site' category
    __authAsymId = None
    __authSeqId = None
    __authAtomId = None
    # __altAuthAtomId = None

    # coordinates information generated by ParserListenerUtil.coordAssemblyChecker()
    __polySeq = None
    __altPolySeq = None
    __nonPoly = None
    __branched = None
    __nonPolySeq = None
    __coordAtomSite = None
    __coordUnobsRes = None
    __labelToAuthSeq = None
    __authToLabelSeq = None
    __authToStarSeq = None

    __representativeModelId = REPRESENTATIVE_MODEL_ID
    __hasPolySeq = False
    __hasNonPoly = False
    __hasBranched = False
    __hasNonPolySeq = False
    __preferAuthSeq = True
    __gapInAuthSeq = False

    # large model
    __largeModel = False
    __representativeAsymId = 'A'

    # polymer sequence of MR file
    __polySeqRst = None

    __seqAlign = None
    __chainAssign = None

    # current restraint subtype
    __cur_subtype = ''
    __with_axis = False
    __cur_auth_atom_id = ''

    # vector statement
    __cur_vector_mode = ''
    __cur_vector_atom_prop_type = ''

    # evaluate statement
    __cur_symbol_name = ''
    __cur_vflc_op_code = ''

    depth = 0

    stackSelections = None  # stack of selection
    stackTerms = None  # stack of term
    stackFactors = None  # stack of factor
    stackVflc = None  # stack of Vflc

    factor = None

    # distance
    noePotential = 'biharmonic'
    noeAverage = 'r-6'
    squareExponent = 2.0
    softExponent = 2.0
    squareConstant = 20.0
    squareOffset = 0.0
    rSwitch = 10.0
    scale = 1.0
    asymptote = 0.0
    B_high = 0.01
    ceiling = 30.0
    temperature = 300.0
    monomers = 1
    ncount = 2
    scale_a = None
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

    # CS
    csExpect = None

    # planality
    planeWeight = 300.0

    # NCS
    ncsSigb = 2.0
    ncsWeight = 300.0

    # Rama
    ramaPotential = None
    ramaError = None
    ramaForceConst = 1.0
    ramaSize = None
    ramaPhase = None
    ramaExpectGrid = None
    ramaExpectValue = None

    # diffusion
    diffCoef = None
    diffForceConst = 1.0
    diffPotential = None

    # generic statements
    classification = None
    coefficients = None

    # collection of atom selection
    atomSelectionSet = []

    # collection of number selection
    numberSelection = []

    # collection of number selection in factor
    numberFSelection = []

    # store[1-9]
    storeSet = {i: [] for i in range(1, 10)}

    # vector mode: do
    vectorDo = {}

    # evaluate
    evaluate = {}

    # control
    evaluateFor = {}

    warningMessage = ''

    __warningInAtomSelection = ''

    reasonsForReParsing = {}

    __cachedDictForAtomIdList = {}

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
                 mrAtomNameMapping=None,
                 cR=None, caC=None, ccU=None, csStat=None, nefT=None,
                 reasons=None):
        self.__verbose = verbose
        self.__lfh = log

        self.__representativeModelId = representativeModelId
        self.__mrAtomNameMapping = None if mrAtomNameMapping is None or len(mrAtomNameMapping) == 0 else mrAtomNameMapping

        self.__cR = cR
        self.__hasCoord = cR is not None

        if self.__hasCoord:
            exptl = cR.getDictList('exptl')
            if len(exptl) > 0 and 'method' in exptl[0]:
                self.__exptlMethod = exptl[0]['method']
            ret = coordAssemblyChecker(verbose, log, representativeModelId, cR, caC)
            self.__modelNumName = ret['model_num_name']
            self.__authAsymId = ret['auth_asym_id']
            self.__authSeqId = ret['auth_seq_id']
            self.__authAtomId = ret['auth_atom_id']
            # self.__altAuthAtomId = ret['alt_auth_atom_id']
            self.__polySeq = ret['polymer_sequence']
            self.__altPolySeq = ret['alt_polymer_sequence']
            self.__nonPoly = ret['non_polymer']
            self.__branched = ret['branched']
            self.__coordAtomSite = ret['coord_atom_site']
            self.__coordUnobsRes = ret['coord_unobs_res']
            self.__labelToAuthSeq = ret['label_to_auth_seq']
            self.__authToLabelSeq = ret['auth_to_label_seq']
            self.__authToStarSeq = ret['auth_to_star_seq']

        self.__hasPolySeq = self.__polySeq is not None and len(self.__polySeq) > 0
        self.__hasNonPoly = self.__nonPoly is not None and len(self.__nonPoly) > 0
        self.__hasBranched = self.__branched is not None and len(self.__branched) > 0
        if self.__hasNonPoly or self.__hasBranched:
            self.__hasNonPolySeq = True
            if self.__hasNonPoly and self.__hasBranched:
                self.__nonPolySeq = self.__nonPoly
                self.__nonPolySeq.extend(self.__branched)
            elif self.__hasNonPoly:
                self.__nonPolySeq = self.__nonPoly
            else:
                self.__nonPolySeq = self.__branched

        if self.__hasPolySeq:
            self.__gapInAuthSeq = any(ps for ps in self.__polySeq if ps['gap_in_auth_seq'])

        self.__largeModel = self.__hasPolySeq and len(self.__polySeq) > LEN_MAJOR_ASYM_ID_SET
        if self.__largeModel:
            self.__representativeAsymId = next(c for c in MAJOR_ASYM_ID_SET if any(ps for ps in self.__polySeq if ps['auth_chain_id'] == c))

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

        if reasons is not None and 'model_chain_id_ext' in reasons:
            self.__polySeq, self.__altPolySeq, self.__coordAtomSite, self.__coordUnobsRes,\
                self.__labelToAuthSeq, self.__authToLabelSeq, self.__authToStarSeq =\
                extendCoordChainsForExactNoes(reasons['model_chain_id_ext'],
                                              self.__polySeq, self.__altPolySeq,
                                              self.__coordAtomSite, self.__coordUnobsRes,
                                              self.__authToLabelSeq, self.__authToStarSeq)

        # reasons for re-parsing request from the previous trial
        self.__reasons = reasons
        self.__preferLabelSeqCount = 0

        self.reasonsForReParsing = {}  # reset to prevent interference from the previous run

        self.distRestraints = 0      # CNS: Distance restraints
        self.dihedRestraints = 0     # CNS: Dihedral angle restraints
        self.rdcRestraints = 0       # CNS: Suscetibility anisotropy restraints
        self.planeRestraints = 0     # CNS: Plane restraints
        self.jcoupRestraints = 0     # CNS: Scalar J-coupling restraints
        self.hvycsRestraints = 0     # CNS: Carbon chemical shift restraints
        self.procsRestraints = 0     # CNS: Proton chemical shift restraints
        self.ramaRestraints = 0      # CNS: Conformation database restraints
        self.diffRestraints = 0      # CNS: Diffusion anisotropy restraints
        # self.angRestraints = 0       # CNS: Angle database restraints
        self.geoRestraints = 0       # CNS: Harmonic coordinate/NCS restraints

        self.distStatements = 0      # CNS: Distance statements
        self.dihedStatements = 0     # CNS: Dihedral angle statements
        self.rdcStatements = 0       # CNS: Suscetibility anisotropy statements
        self.planeStatements = 0     # CNS: Plane statements
        self.jcoupStatements = 0     # CNS: Scalar J-coupling statements
        self.hvycsStatements = 0     # CNS: Carbon chemical shift statements
        self.procsStatements = 0     # CNS: Proton chemical shift statements
        self.ramaStatements = 0      # CNS: Conformation database statements
        self.diffStatements = 0      # CNS: Diffusion anisotropy statements
        # self.angStatements = 0       # CNS: Angle database statements
        self.geoStatements = 0       # CNS: Harmonic coordinate/NCS restraints

        self.sfDict = {}

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

    # Enter a parse tree produced by CnsMRParser#cns_mr.
    def enterCns_mr(self, ctx: CnsMRParser.Cns_mrContext):  # pylint: disable=unused-argument
        self.__polySeqRst = []

    # Exit a parse tree produced by CnsMRParser#cns_mr.
    def exitCns_mr(self, ctx: CnsMRParser.Cns_mrContext):  # pylint: disable=unused-argument
        if self.__hasPolySeq and self.__polySeqRst is not None:
            sortPolySeqRst(self.__polySeqRst,
                           None if self.__reasons is None or 'non_poly_remap' not in self.__reasons else self.__reasons['non_poly_remap'])

            self.__seqAlign, _ = alignPolymerSequence(self.__pA, self.__polySeq, self.__polySeqRst,
                                                      resolvedMultimer=(self.__reasons is not None))
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

                        self.__seqAlign, _ = alignPolymerSequence(self.__pA, self.__polySeq, self.__polySeqRst,
                                                                  resolvedMultimer=(self.__reasons is not None))
                        self.__chainAssign, _ = assignPolymerSequence(self.__pA, self.__ccU, self.__file_type, self.__polySeq, self.__polySeqRst, self.__seqAlign)

                trimSequenceAlignment(self.__seqAlign, self.__chainAssign)

                if 'Atom not found' in self.warningMessage and self.__reasons is None:

                    seqIdRemap = []

                    cyclicPolymer = {}

                    for ca in self.__chainAssign:
                        ref_chain_id = ca['ref_chain_id']
                        test_chain_id = ca['test_chain_id']

                        sa = next(sa for sa in self.__seqAlign
                                  if sa['ref_chain_id'] == ref_chain_id
                                  and sa['test_chain_id'] == test_chain_id)

                        poly_seq_model = next(ps for ps in self.__polySeq
                                              if ps['auth_chain_id'] == ref_chain_id)
                        poly_seq_rst = next(ps for ps in self.__polySeqRst
                                            if ps['chain_id'] == test_chain_id)

                        seq_id_mapping = {}
                        for ref_seq_id, mid_code, test_seq_id in zip(sa['ref_seq_id'], sa['mid_code'], sa['test_seq_id']):
                            if mid_code == '|':
                                try:
                                    seq_id_mapping[test_seq_id] = next(auth_seq_id for auth_seq_id, seq_id
                                                                       in zip(poly_seq_model['auth_seq_id'], poly_seq_model['seq_id'])
                                                                       if seq_id == ref_seq_id)
                                except StopIteration:
                                    pass

                        if ref_chain_id not in cyclicPolymer:
                            cyclicPolymer[ref_chain_id] =\
                                isCyclicPolymer(self.__cR, self.__polySeq, ref_chain_id, self.__representativeModelId, self.__modelNumName)

                        if cyclicPolymer[ref_chain_id]:

                            poly_seq_model = next(ps for ps in self.__polySeq
                                                  if ps['auth_chain_id'] == ref_chain_id)

                            offset = None
                            for seq_id, comp_id in zip(poly_seq_rst['seq_id'], poly_seq_rst['comp_id']):
                                if seq_id not in seq_id_mapping:
                                    _seq_id = next((_seq_id for _seq_id, _comp_id in zip(poly_seq_model['seq_id'], poly_seq_model['comp_id'])
                                                    if _seq_id not in seq_id_mapping.values() and _comp_id == comp_id), None)
                                    if _seq_id is not None:
                                        offset = seq_id - _seq_id
                                        break

                            if offset is not None:
                                for seq_id in poly_seq_rst['seq_id']:
                                    if seq_id not in seq_id_mapping:
                                        seq_id_mapping[seq_id] = seq_id - offset

                        if any(k for k, v in seq_id_mapping.items() if k != v)\
                           and not any(k for k, v in seq_id_mapping.items()
                                       if v in poly_seq_model['seq_id']
                                       and k == poly_seq_model['auth_seq_id'][poly_seq_model['seq_id'].index(v)]):
                            seqIdRemap.append({'chain_id': test_chain_id, 'seq_id_dict': seq_id_mapping})

                    if len(seqIdRemap) > 0:
                        if 'seq_id_remap' not in self.reasonsForReParsing:
                            self.reasonsForReParsing['seq_id_remap'] = seqIdRemap

                    if any(ps for ps in self.__polySeq if 'identical_chain_id' in ps):
                        polySeqRst, chainIdMapping = splitPolySeqRstForMultimers(self.__pA, self.__polySeq, self.__polySeqRst, self.__chainAssign)

                        if polySeqRst is not None:
                            self.__polySeqRst = polySeqRst
                            if 'chain_id_remap' not in self.reasonsForReParsing:
                                self.reasonsForReParsing['chain_id_remap'] = chainIdMapping

                    if len(self.__polySeq) == 1 and len(self.__polySeqRst) == 1:
                        polySeqRst, chainIdMapping, modelChainIdExt =\
                            splitPolySeqRstForExactNoes(self.__pA, self.__polySeq, self.__polySeqRst, self.__chainAssign)

                        if polySeqRst is not None:
                            self.__polySeqRst = polySeqRst
                            if 'chain_id_clone' not in self.reasonsForReParsing:
                                self.reasonsForReParsing['chain_id_clone'] = chainIdMapping
                            if 'model_chain_id_ext' not in self.reasonsForReParsing:
                                self.reasonsForReParsing['model_chain_id_ext'] = modelChainIdExt

                    if self.__hasNonPoly:
                        polySeqRst, nonPolyMapping = splitPolySeqRstForNonPoly(self.__ccU, self.__nonPoly, self.__polySeqRst,
                                                                               self.__seqAlign, self.__chainAssign)

                        if polySeqRst is not None:
                            self.__polySeqRst = polySeqRst
                            if 'non_poly_remap' not in self.reasonsForReParsing:
                                self.reasonsForReParsing['non_poly_remap'] = nonPolyMapping

                    if self.__hasBranched:
                        polySeqRst, branchedMapping = splitPolySeqRstForBranched(self.__pA, self.__polySeq, self.__branched, self.__polySeqRst,
                                                                                 self.__chainAssign)

                        if polySeqRst is not None:
                            self.__polySeqRst = polySeqRst
                            if 'branched_remap' not in self.reasonsForReParsing:
                                self.reasonsForReParsing['branched_remap'] = branchedMapping

        # """
        # if 'label_seq_scheme' in self.reasonsForReParsing and self.reasonsForReParsing['label_seq_scheme']:
        #     if 'non_poly_remap' in self.reasonsForReParsing:
        #         self.reasonsForReParsing['label_seq_scheme'] = False
        #     if 'seq_id_remap' in self.reasonsForReParsing:
        #         del self.reasonsForReParsing['seq_id_remap']
        # """
        if 'local_seq_scheme' in self.reasonsForReParsing:
            if 'non_poly_remap' in self.reasonsForReParsing or 'branched_remap' in self.reasonsForReParsing:
                del self.reasonsForReParsing['local_seq_scheme']
            if 'seq_id_remap' in self.reasonsForReParsing:
                del self.reasonsForReParsing['seq_id_remap']

        if 'seq_id_remap' in self.reasonsForReParsing and 'non_poly_remap' in self.reasonsForReParsing:
            del self.reasonsForReParsing['seq_id_remap']

        if len(self.warningMessage) == 0:
            self.warningMessage = None
        else:
            self.warningMessage = self.warningMessage[0:-1]
            self.warningMessage = '\n'.join(set(self.warningMessage.split('\n')))

    # Enter a parse tree produced by CnsMRParser#distance_restraint.
    def enterDistance_restraint(self, ctx: CnsMRParser.Distance_restraintContext):  # pylint: disable=unused-argument
        self.classification = '.'

        self.distStatements += 1
        self.__cur_subtype = 'dist'

        self.noePotential = 'biharmonic'  # default potential
        self.noeAverage = 'r-6'  # default averaging method
        self.squareExponent = 2.0
        self.softExponent = 2.0
        self.squareConstant = 20.0
        self.squareOffset = 0.0
        self.rSwitch = 10.0
        self.scale = 1.0
        self.asymptote = 0.0
        self.B_high = 0.01
        self.ceiling = 30.0
        self.temperature = 300.0
        self.monomers = 1
        self.ncount = 2
        self.symmTarget = None
        self.symmDminus = None
        self.symmDplus = None

        if self.__createSfDict:
            self.__addSf()

    # Exit a parse tree produced by CnsMRParser#distance_restraint.
    def exitDistance_restraint(self, ctx: CnsMRParser.Distance_restraintContext):  # pylint: disable=unused-argument
        if self.__createSfDict and self.__cur_subtype == 'dist':
            sf = self.__getSf()

            if 'aux_loops' in sf:
                return

            sf['aux_loops'] = getAuxLoops(self.__cur_subtype)

            aux_lp = next((aux_lp for aux_lp in sf['aux_loops'] if aux_lp.category == '_Gen_dist_constraint_software_param'), None)

            if aux_lp is None:
                return

            aux_lp.add_data(getAuxRow(self.__cur_subtype, aux_lp.category, sf['list_id'], self.__entryId,
                                      {'Type': 'class name', 'Value': self.classification}))
            aux_lp.add_data(getAuxRow(self.__cur_subtype, aux_lp.category, sf['list_id'], self.__entryId,
                                      {'Type': 'potential function', 'Value': self.noePotential}))
            aux_lp.add_data(getAuxRow(self.__cur_subtype, aux_lp.category, sf['list_id'], self.__entryId,
                                      {'Type': 'averaging method', 'Value': self.noeAverage}))
            aux_lp.add_data(getAuxRow(self.__cur_subtype, aux_lp.category, sf['list_id'], self.__entryId,
                                      {'Type': 'scaling constant', 'Value': self.scale}))
            aux_lp.add_data(getAuxRow(self.__cur_subtype, aux_lp.category, sf['list_id'], self.__entryId,
                                      {'Type': 'ceiling', 'Value': self.ceiling}))
            if self.noePotential in ('square', 'softsquare'):
                aux_lp.add_data(getAuxRow(self.__cur_subtype, aux_lp.category, sf['list_id'], self.__entryId,
                                          {'Type': 'exponent', 'Value': self.squareExponent}))
            if self.noePotential == 'softsquare':
                aux_lp.add_data(getAuxRow(self.__cur_subtype, aux_lp.category, sf['list_id'], self.__entryId,
                                          {'Type': 'soft exponent', 'Value': self.softExponent}))
            if self.noePotential in ('square', 'softsquare'):
                aux_lp.add_data(getAuxRow(self.__cur_subtype, aux_lp.category, sf['list_id'], self.__entryId,
                                          {'Type': 'auxiliary scaling constant', 'Value': self.squareConstant}))
            if self.noePotential in ('square', 'softsquare'):
                aux_lp.add_data(getAuxRow(self.__cur_subtype, aux_lp.category, sf['list_id'], self.__entryId,
                                          {'Type': 'negative offset', 'Value': self.squareOffset}))
            if self.noePotential == 'softsquare':
                aux_lp.add_data(getAuxRow(self.__cur_subtype, aux_lp.category, sf['list_id'], self.__entryId,
                                          {'Type': 'switch distance', 'Value': self.rSwitch}))
            if self.noePotential == 'softsquare':
                aux_lp.add_data(getAuxRow(self.__cur_subtype, aux_lp.category, sf['list_id'], self.__entryId,
                                          {'Type': 'asymptote slope', 'Value': self.asymptote}))
            if self.noePotential == 'high':
                aux_lp.add_data(getAuxRow(self.__cur_subtype, aux_lp.category, sf['list_id'], self.__entryId,
                                          {'Type': 'B_high', 'Value': self.B_high}))
            if self.noePotential == 'biharmonic':
                aux_lp.add_data(getAuxRow(self.__cur_subtype, aux_lp.category, sf['list_id'], self.__entryId,
                                          {'Type': 'temperature', 'Value': self.temperature}))
            if self.noeAverage == 'sum':
                aux_lp.add_data(getAuxRow(self.__cur_subtype, aux_lp.category, sf['list_id'], self.__entryId,
                                          {'Type': 'number monomers', 'Value': self.monomers}))
            if self.noePotential == 'high':
                aux_lp.add_data(getAuxRow(self.__cur_subtype, aux_lp.category, sf['list_id'], self.__entryId,
                                          {'Type': 'number assign statements', 'Value': self.ncount}))

            sf['saveframe'].add_loop(aux_lp)

    # Enter a parse tree produced by CnsMRParser#dihedral_angle_restraint.
    def enterDihedral_angle_restraint(self, ctx: CnsMRParser.Dihedral_angle_restraintContext):  # pylint: disable=unused-argument
        self.dihedStatements += 1
        self.__cur_subtype = 'dihed'

        self.scale = 1.0

        if self.__createSfDict:
            self.__addSf()

    # Exit a parse tree produced by CnsMRParser#dihedral_angle_restraint.
    def exitDihedral_angle_restraint(self, ctx: CnsMRParser.Dihedral_angle_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#plane_restraint.
    def enterPlane_restraint(self, ctx: CnsMRParser.Plane_restraintContext):  # pylint: disable=unused-argument
        self.planeStatements += 1
        self.__cur_subtype = 'plane'

        if self.__createSfDict:
            self.__addSf('planality restraint, CNS PLANE/GROUP statement')

    # Exit a parse tree produced by CnsMRParser#plane_restraint.
    def exitPlane_restraint(self, ctx: CnsMRParser.Plane_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#harmonic_restraint.
    def enterHarmonic_restraint(self, ctx: CnsMRParser.Harmonic_restraintContext):  # pylint: disable=unused-argument
        self.geoStatements += 1
        self.__cur_subtype = 'geo'

        self.squareExponent = 2.0
        self.vector3D = [0.0] * 3

        if self.__createSfDict:
            self.__addSf('NCS restraint, CNS HARMonic statement')

    # Exit a parse tree produced by CnsMRParser#harmonic_restraint.
    def exitHarmonic_restraint(self, ctx: CnsMRParser.Harmonic_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#rdc_restraint.
    def enterRdc_restraint(self, ctx: CnsMRParser.Rdc_restraintContext):  # pylint: disable=unused-argument
        self.classification = '.'

        self.rdcStatements += 1
        self.__cur_subtype = 'rdc'

        self.potential = 'square'  # default potential
        self.scale = 1.0

        if self.__createSfDict:
            self.__addSf()

    # Exit a parse tree produced by CnsMRParser#rdc_restraint.
    def exitRdc_restraint(self, ctx: CnsMRParser.Rdc_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#coupling_restraint.
    def enterCoupling_restraint(self, ctx: CnsMRParser.Coupling_restraintContext):  # pylint: disable=unused-argument
        self.classification = '.'

        self.jcoupStatements += 1
        self.__cur_subtype = 'jcoup'

        if self.__createSfDict:
            self.__addSf()

    # Exit a parse tree produced by CnsMRParser#coupling_restraint.
    def exitCoupling_restraint(self, ctx: CnsMRParser.Coupling_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#carbon_shift_restraint.
    def enterCarbon_shift_restraint(self, ctx: CnsMRParser.Carbon_shift_restraintContext):  # pylint: disable=unused-argument
        self.classification = '.'

        self.hvycsStatements += 1
        self.__cur_subtype = 'hvycs'

        if self.__createSfDict:
            self.__addSf()

    # Exit a parse tree produced by CnsMRParser#carbon_shift_restraint.
    def exitCarbon_shift_restraint(self, ctx: CnsMRParser.Carbon_shift_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#proton_shift_restraint.
    def enterProton_shift_restraint(self, ctx: CnsMRParser.Proton_shift_restraintContext):  # pylint: disable=unused-argument
        self.classification = '.'

        self.procsStatements += 1
        self.__cur_subtype = 'procs'

        if self.__createSfDict:
            self.__addSf()

    # Exit a parse tree produced by CnsMRParser#proton_shift_restraint.
    def exitProton_shift_restraint(self, ctx: CnsMRParser.Proton_shift_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#conformation_db_restraint.
    def enterConformation_db_restraint(self, ctx: CnsMRParser.Conformation_db_restraintContext):  # pylint: disable=unused-argument
        self.classification = '.'

        self.ramaStatements += 1
        self.__cur_subtype = 'rama'

        if self.__createSfDict:
            self.__addSf('dihedral angle database restraint, CNS CONFormation statement')

    # Exit a parse tree produced by CnsMRParser#conformation_db_restraint.
    def exitConformation_db_restraint(self, ctx: CnsMRParser.Conformation_db_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#diffusion_anisotropy_restraint.
    def enterDiffusion_anisotropy_restraint(self, ctx: CnsMRParser.Diffusion_anisotropy_restraintContext):  # pylint: disable=unused-argument
        self.classification = '.'

        self.diffStatements += 1
        self.__cur_subtype = 'diff'

        if self.__createSfDict:
            self.__addSf('diffusion anisotropy restraint, CNS DANIsotropy statement')

    # Exit a parse tree produced by CnsMRParser#diffusion_anisotropy_restraint.
    def exitDiffusion_anisotropy_restraint(self, ctx: CnsMRParser.Diffusion_anisotropy_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#one_bond_coupling_restraint.
    def enterOne_bond_coupling_restraint(self, ctx: CnsMRParser.One_bond_coupling_restraintContext):  # pylint: disable=unused-argument
        """
        @deprecated: This restraint has not been useful in practice, but has been preserved for historical reasons.
        """

    # Exit a parse tree produced by CnsMRParser#one_bond_coupling_restraint.
    def exitOne_bond_coupling_restraint(self, ctx: CnsMRParser.One_bond_coupling_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#angle_db_restraint.
    def enterAngle_db_restraint(self, ctx: CnsMRParser.Angle_db_restraintContext):  # pylint: disable=unused-argument
        """
        @deprecated:  This term has not proved useful in practice and is only here for historical reasons.
        """

    # Exit a parse tree produced by CnsMRParser#angle_db_restraint.
    def exitAngle_db_restraint(self, ctx: CnsMRParser.Angle_db_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#noe_statement.
    def enterNoe_statement(self, ctx: CnsMRParser.Noe_statementContext):
        if ctx.Potential_types():
            code = str(ctx.Potential_types()).upper()
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
            elif code.startswith('3DPO'):
                self.noePotential = '3dpo'
            else:
                self.noePotential = 'biharmonic'
                self.warningMessage += "[Enum mismatch ignorable] "\
                    f"The potential type {str(ctx.Potential_types())!r} is unknown potential type for the 'NOE' statements. "\
                    f"Instead, set the default potential {self.noePotential!r}.\n"

        elif ctx.Averaging_methods():
            code = str(ctx.Averaging_methods()).upper()
            if code == 'R-6':
                self.noeAverage = 'r-6'
            elif code == 'R-3':
                self.noeAverage = 'r-3'
            elif code == 'SUM':
                self.noeAverage = 'sum'
            elif code.startswith('CENT'):
                self.noeAverage = 'center'
            else:
                self.noeAverage = 'r-6'
                self.warningMessage += "[Enum mismatch ignorable] "\
                    f"The averaging method {str(ctx.Averaging_methods())!r} is unknown method for the 'NOE' statements. "\
                    f"Instead, set the default method {self.noeAverage!r}.\n"

        elif ctx.SqExponent():
            self.squareExponent = self.getNumber_s(ctx.number_s(0))
            if isinstance(self.squareExponent, str):
                if self.squareExponent in self.evaluate:
                    self.squareExponent = self.evaluate[self.squareExponent]
                else:
                    self.warningMessage += "[Unsupported data] "\
                        f"The symbol {self.squareExponent!r} in the 'NOE' statement is not defined so that set the default value.\n"
                    self.squareExponent = 2.0
            if self.squareExponent is None or self.squareExponent <= 0.0:
                self.warningMessage += "[Invalid data] "\
                    "The exponent value of square-well or soft-square function "\
                    f"'NOE {str(ctx.SqExponent())} {self.getClass_name(ctx.class_name(0))} {self.squareExponent} END' must be a positive value.\n"

        elif ctx.SoExponent():
            self.softExponent = self.getNumber_s(ctx.number_s(0))
            if isinstance(self.softExponent, str):
                if self.softExponent in self.evaluate:
                    self.softExponent = self.evaluate[self.softExponent]
                else:
                    self.warningMessage += "[Unsupported data] "\
                        f"The symbol {self.softExponent!r} in the 'NOE' statement is not defined so that set the default value.\n"
                    self.softExponent = 2.0
            if self.softExponent is None or self.softExponent <= 0.0:
                self.warningMessage += "[Invalid data] "\
                    "The exponent value for soft-square function only "\
                    f"'NOE {str(ctx.SoExponent())} {self.getClass_name(ctx.class_name(0))} {self.softExponent} END' must be a positive value.\n"

        elif ctx.SqConstant():
            self.squareConstant = self.getNumber_s(ctx.number_s(0))
            if isinstance(self.squareConstant, str):
                if self.squareConstant in self.evaluate:
                    self.squareConstant = self.evaluate[self.squareConstant]
                else:
                    self.warningMessage += "[Unsupported data] "\
                        f"The symbol {self.squareConstant!r} in the 'NOE' statement is not defined so that set the default value.\n"
                    self.squareConstant = 20.0
            if self.squareConstant is None or self.squareConstant <= 0.0:
                self.warningMessage += "[Invalid data] "\
                    "The auxiliary scaling constant of square-well or soft-square function "\
                    f"'NOE {str(ctx.SqConstant())} {self.getClass_name(ctx.class_name(0))} {self.squareConstant} END' must be a positive value.\n"

        elif ctx.SqOffset():
            self.squareOffset = self.getNumber_s(ctx.number_s(0))
            if isinstance(self.squareOffset, str):
                if self.squareOffset in self.evaluate:
                    self.squareOffset = self.evaluate[self.squareOffset]
                else:
                    self.warningMessage += "[Unsupported data] "\
                        f"The symbol {self.squareOffset!r} in the 'NOE' statement is not defined so that set the default value.\n"
                    self.squareOffset = 0.0
            if self.squareOffset is None or self.squareOffset < 0.0:
                self.warningMessage += "[Invalid data] "\
                    "The negative offset value to all upper bounds of square-well or soft-square function "\
                    f"'NOE {str(ctx.SqOffset())} {self.getClass_name(ctx.class_name(0))} {self.squareOffset} END' must not be a negative value.\n"

        elif ctx.Rswitch():
            self.rSwitch = self.getNumber_s(ctx.number_s(0))
            if isinstance(self.rSwitch, str):
                if self.rSwitch in self.evaluate:
                    self.rSwitch = self.evaluate[self.rSwitch]
                else:
                    self.warningMessage += "[Unsupported data] "\
                        f"The symbol {self.rSwitch!r} in the 'NOE' statement is not defined so that set the default value.\n"
                    self.rSwitch = 10.0
            if self.rSwitch is None or self.rSwitch < 0.0:
                self.warningMessage += "[Invalid data] "\
                    "The smoothing parameter of soft-square function "\
                    f"'NOE {str(ctx.Rswitch())} {self.getClass_name(ctx.class_name(0))} {self.rSwitch} END' must not be a negative value.\n"

        elif ctx.Scale():
            self.scale = self.getNumber_s(ctx.number_s(0))
            if isinstance(self.scale, str):
                if self.scale in self.evaluate:
                    self.scale = self.evaluate[self.scale]
                else:
                    self.warningMessage += "[Unsupported data] "\
                        f"The symbol {self.scale!r} in the 'NOE' statement is not defined so that set the default value.\n"
                    self.scale = 1.0
            if self.scale is None or self.scale == 0.0:
                self.warningMessage += "[Range value warning] "\
                    f"The scale value 'NOE {str(ctx.Scale())} {self.getClass_name(ctx.class_name(0))} {self.scale} END' should be a positive value.\n"
            elif self.scale < 0.0:
                self.warningMessage += "[Invalid data] "\
                    f"The scale value 'NOE {str(ctx.Scale())} {self.getClass_name(ctx.class_name(0))} {self.scale} END' must not be a negative value.\n"

        elif ctx.Asymptote():
            self.asymptote = self.getNumber_s(ctx.number_s(0))
            if isinstance(self.asymptote, str):
                if self.asymptote in self.evaluate:
                    self.asymptote = self.evaluate[self.asymptote]
                else:
                    self.warningMessage += "[Unsupported data] "\
                        f"The symbol {self.asymptote!r} in the 'NOE' statement is not defined so that set the default value.\n"
                    self.asymptote = 0.0
            if self.asymptote is None:
                self.warningMessage += "[Range value warning] "\
                    f"The asymptote slope value 'NOE {str(ctx.Asymptote())} {self.getClass_name(ctx.class_name(0))} {self.asymptote} END' should be a non-negative value.\n"
            elif self.asymptote < 0.0:
                self.warningMessage += "[Invalid data] "\
                    f"The asymptote slope value 'NOE {str(ctx.Asymptote())} {self.getClass_name(ctx.class_name(0))} {self.asymptote} END' must not be a negative value.\n"

        elif ctx.Bhig():
            self.B_high = self.getNumber_s(ctx.number_s(0))
            if isinstance(self.B_high, str):
                if self.B_high in self.evaluate:
                    self.B_high = self.evaluate[self.B_high]
                else:
                    self.warningMessage += "[Unsupported data] "\
                        f"The symbol {self.B_high!r} in the 'NOE' statement is not defined so that set the default value.\n"
                    self.B_high = 0.01
            if self.B_high is None:
                self.warningMessage += "[Range value warning] "\
                    f"The potential barrier value 'NOE {str(ctx.Bhig())} {self.getClass_name(ctx.class_name(0))} {self.B_high} END' should be a non-negative value.\n"
            elif self.B_high < 0.0:
                self.warningMessage += "[Invalid data] "\
                    f"The potential barrier value 'NOE {str(ctx.Bhig())} {self.getClass_name(ctx.class_name(0))} {self.B_high} END' must not be a negative value.\n"

        elif ctx.Ceiling():
            self.ceiling = self.getNumber_s(ctx.number_s(0))
            if isinstance(self.ceiling, str):
                if self.ceiling in self.evaluate:
                    self.ceiling = self.evaluate[self.ceiling]
                else:
                    self.warningMessage += "[Unsupported data] "\
                        f"The symbol {self.ceiling!r} in the 'NOE' statement is not defined so that set the default value.\n"
                    self.ceiling = 30.0
            if self.ceiling is None:
                self.warningMessage += "[Range value warning] "\
                    f"The ceiling value for energy constant 'NOE {str(ctx.Ceiling())} {self.ceiling} END' should be a non-negative value.\n"
            elif self.ceiling < 0.0:
                self.warningMessage += "[Invalid data] "\
                    f"The ceiling value for energy constant 'NOE {str(ctx.Ceiling())} {self.ceiling} END' must not be a negative value.\n"

        elif ctx.Temperature():
            self.temperature = self.getNumber_s(ctx.number_s(0))
            if isinstance(self.temperature, str):
                if self.temperature in self.evaluate:
                    self.temperature = self.evaluate[self.temperature]
                else:
                    self.warningMessage += "[Unsupported data] "\
                        f"The symbol {self.temperature!r} in the 'NOE' statement is not defined so that set the default value.\n"
                    self.temperature = 300.0
            if self.temperature is None:
                self.warningMessage += "[Range value warning] "\
                    f"The temperature 'NOE {str(ctx.Temparature())} {self.temperature} END' should be a non-negative value.\n"
            elif self.temperature < 0.0:
                self.warningMessage += "[Invalid data] "\
                    f"The temperature 'NOE {str(ctx.Temparature())} {self.temperature} END' must not be a negative value.\n"

        elif ctx.Monomers():
            self.monomers = int(str(ctx.Integer()))
            if self.monomers is None or self.monomers == 0:
                self.warningMessage += "[Range value warning] "\
                    f"The number of monomers 'NOE {str(ctx.Monomers())} {self.getClass_name(ctx.class_name(0))} {self.monomers} END' should be a positive value.\n"
            elif self.monomers < 0:
                self.warningMessage += "[Invalid data] "\
                    f"The number of monomers 'NOE {str(ctx.Monomers())} {self.getClass_name(ctx.class_name(0))} {self.monomers} END' must not be a negative value.\n"

        elif ctx.Ncount():
            self.ncount = int(str(ctx.Integer()))
            if self.ncount is None or self.ncount == 0:
                self.warningMessage += "[Range value warning] "\
                    f"The number of assign statements 'NOE {str(ctx.Ncount())} {self.getClass_name(ctx.class_name(0))} {self.ncount} END' should be a positive value.\n"
            elif self.ncount < 0:
                self.warningMessage += "[Invalid data] "\
                    f"The number of assign statements 'NOE {str(ctx.Ncount())} {self.getClass_name(ctx.class_name(0))} {self.ncount} END' must not be a negative value.\n"

        elif ctx.Reset():
            self.noePotential = 'biharmonic'  # default potential
            self.squareExponent = 2.0
            self.softExponent = 2.0
            self.squareConstant = 20.0
            self.squareOffset = 0.0
            self.rSwitch = 10.0
            self.scale = 1.0
            self.asymptote = 0.0
            self.B_high = 0.01
            self.ceiling = 30.0
            self.temperature = 300.0
            self.monomers = 1
            self.ncount = 2
            self.symmTarget = None
            self.symmDminus = None
            self.symmDplus = None

    # Exit a parse tree produced by CnsMRParser#noe_statement.
    def exitNoe_statement(self, ctx: CnsMRParser.Noe_statementContext):  # pylint: disable=unused-argument
        if self.__debug:
            print(f"subtype={self.__cur_subtype} (NOE) classification={self.classification!r}")

    # Enter a parse tree produced by CnsMRParser#noe_assign.
    def enterNoe_assign(self, ctx: CnsMRParser.Noe_assignContext):  # pylint: disable=unused-argument
        self.distRestraints += 1
        if self.__cur_subtype != 'dist':
            self.distStatements += 1
        self.__cur_subtype = 'dist'

        self.atomSelectionSet.clear()
        self.__warningInAtomSelection = ''

        self.scale_a = None

    # Exit a parse tree produced by CnsMRParser#noe_assign.
    def exitNoe_assign(self, ctx: CnsMRParser.Noe_assignContext):  # pylint: disable=unused-argument

        try:

            if None in self.numberSelection:
                return

            target = self.numberSelection[0]

            if len(self.numberSelection) > 2:
                dminus = self.numberSelection[1]
                dplus = self.numberSelection[2]

            elif len(self.numberSelection) > 1:
                dminus = dplus = self.numberSelection[1]

            else:
                dminus = dplus = 0.0

            scale = self.scale if self.scale_a is None else self.scale_a

            if scale < 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The weight value '{scale}' must not be a negative value.\n"
                return
            if scale == 0.0:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The weight value '{scale}' should be a positive value.\n"

            target_value = target
            lower_limit = None
            upper_limit = None
            lower_linear_limit = None
            upper_linear_limit = None

            if self.noePotential == 'biharmonic':
                lower_limit = target - dminus
                upper_limit = target + dplus
            elif self.noePotential == 'lognormal':
                pass
            elif self.noePotential == 'square':
                if abs(self.squareExponent - 2.0) < abs(self.squareExponent - 1.0):
                    lower_linear = target - dminus
                    upper_linear = target + dplus - self.squareOffset
                else:
                    lower_linear_limit = target - dminus
                    upper_linear_limit = target + dplus - self.squareOffset
            elif self.noePotential == 'softsquare':
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

            if not self.__hasPolySeq:
                return

            self.__allowZeroUpperLimit = False
            if self.__reasons is not None and 'model_chain_id_ext' in self.__reasons\
               and len(self.atomSelectionSet[0]) > 0\
               and len(self.atomSelectionSet[0]) == len(self.atomSelectionSet[1]):
                chain_id_1 = self.atomSelectionSet[0][0]['chain_id']
                seq_id_1 = self.atomSelectionSet[0][0]['seq_id']
                atom_id_1 = self.atomSelectionSet[0][0]['atom_id']

                chain_id_2 = self.atomSelectionSet[1][0]['chain_id']
                seq_id_2 = self.atomSelectionSet[1][0]['seq_id']
                atom_id_2 = self.atomSelectionSet[1][0]['atom_id']

                if chain_id_1 != chain_id_2 and seq_id_1 == seq_id_2 and atom_id_1 == atom_id_2\
                   and ((chain_id_1 in self.__reasons['model_chain_id_ext'] and chain_id_2 in self.__reasons['model_chain_id_ext'][chain_id_1])
                        or (chain_id_2 in self.__reasons['model_chain_id_ext'] and chain_id_1 in self.__reasons['model_chain_id_ext'][chain_id_2])):
                    self.__allowZeroUpperLimit = True
            self.__allowZeroUpperLimit |= hasInterChainRestraint(self.atomSelectionSet)

            dstFunc = self.validateDistanceRange(scale,
                                                 target_value, lower_limit, upper_limit,
                                                 lower_linear_limit, upper_linear_limit)

            if dstFunc is None:
                return

            combinationId = '.'
            if self.__createSfDict:
                sf = self.__getSf(constraintType=getDistConstraintType(self.atomSelectionSet, dstFunc, self.__originalFileName),
                                  potentialType=getPotentialType(self.__file_type, self.__cur_subtype, dstFunc))
                sf['id'] += 1
                if len(self.atomSelectionSet) > 2:
                    combinationId = 0

            for i in range(0, len(self.atomSelectionSet), 2):
                if isinstance(combinationId, int):
                    combinationId += 1
                if self.__createSfDict:
                    memberLogicCode = 'OR' if len(self.atomSelectionSet[i]) * len(self.atomSelectionSet[i + 1]) > 1 else '.'
                for atom1, atom2 in itertools.product(self.atomSelectionSet[i],
                                                      self.atomSelectionSet[i + 1]):
                    if self.__debug:
                        print(f"subtype={self.__cur_subtype} (NOE) id={self.distRestraints} "
                              f"atom1={atom1} atom2={atom2} {dstFunc}")
                    if self.__createSfDict and sf is not None:
                        sf['index_id'] += 1
                        row = getRow(self.__cur_subtype, sf['id'], sf['index_id'],
                                     combinationId, memberLogicCode,
                                     sf['list_id'], self.__entryId, dstFunc, self.__authToStarSeq, atom1, atom2)
                        sf['loop'].add_data(row)

                        if sf['constraint_subsubtype'] == 'ambi':
                            continue

                        if isinstance(combinationId, int)\
                           or (memberLogicCode == 'OR'
                               and (isAmbigAtomSelection(self.atomSelectionSet[i], self.__csStat)
                                    or isAmbigAtomSelection(self.atomSelectionSet[i + 1], self.__csStat))):
                            sf['constraint_subsubtype'] = 'ambi'
                        if 'upper_limit' in dstFunc and dstFunc['upper_limit'] is not None:
                            upperLimit = float(dstFunc['upper_limit'])
                            if upperLimit <= DIST_AMBIG_LOW or upperLimit >= DIST_AMBIG_UP:
                                sf['constraint_subsubtype'] = 'ambi'

        finally:
            self.numberSelection.clear()

    def validateDistanceRange(self, weight,
                              target_value, lower_limit, upper_limit,
                              lower_linear_limit, upper_linear_limit):
        """ Validate distance value range.
        """

        validRange = True
        dstFunc = {'weight': weight, 'potential': self.noePotential, 'average': self.noeAverage}

        if target_value is not None:
            if DIST_ERROR_MIN < target_value < DIST_ERROR_MAX or (target_value == 0.0 and self.__allowZeroUpperLimit):
                dstFunc['target_value'] = f"{target_value}"
            else:
                if target_value <= DIST_ERROR_MIN and self.__omitDistLimitOutlier:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                        f"The target value='{target_value}' is omitted because it is not within range {DIST_RESTRAINT_ERROR}.\n"
                    target_value = None
                else:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The target value='{target_value}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if lower_limit is not None:
            if DIST_ERROR_MIN <= lower_limit < DIST_ERROR_MAX:
                dstFunc['lower_limit'] = f"{lower_limit:.3f}"
            else:
                if lower_limit <= DIST_ERROR_MIN and self.__omitDistLimitOutlier:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                        f"The lower limit value='{lower_limit:.3f}' is omitted because it is not within range {DIST_RESTRAINT_ERROR}.\n"
                    lower_limit = None
                else:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower limit value='{lower_limit:.3f}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if upper_limit is not None:
            if DIST_ERROR_MIN < upper_limit <= DIST_ERROR_MAX or (upper_limit == 0.0 and self.__allowZeroUpperLimit):
                dstFunc['upper_limit'] = f"{upper_limit:.3f}"
            else:
                if (upper_limit <= DIST_ERROR_MIN or upper_limit > DIST_ERROR_MAX) and self.__omitDistLimitOutlier:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                        f"The upper limit value='{upper_limit:.3f}' is omitted because it is not within range {DIST_RESTRAINT_ERROR}.\n"
                    upper_limit = None
                else:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The upper limit value='{upper_limit:.3f}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if lower_linear_limit is not None:
            if DIST_ERROR_MIN <= lower_linear_limit < DIST_ERROR_MAX:
                dstFunc['lower_linear_limit'] = f"{lower_linear_limit:.3f}"
            else:
                if lower_linear_limit <= DIST_ERROR_MIN and self.__omitDistLimitOutlier:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                        f"The lower linear limit value='{lower_linear_limit:.3f}' is omitted because it is not within range {DIST_RESTRAINT_ERROR}.\n"
                    lower_linear_limit = None
                else:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower linear limit value='{lower_linear_limit:.3f}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if upper_linear_limit is not None:
            if DIST_ERROR_MIN < upper_linear_limit <= DIST_ERROR_MAX or (upper_linear_limit == 0.0 and self.__allowZeroUpperLimit):
                dstFunc['upper_linear_limit'] = f"{upper_linear_limit:.3f}"
            else:
                if (upper_linear_limit <= DIST_ERROR_MIN or upper_linear_limit > DIST_ERROR_MAX) and self.__omitDistLimitOutlier:
                    self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                        f"The upper linear limit value='{upper_linear_limit:.3f}' is omitted because it is not within range {DIST_RESTRAINT_ERROR}.\n"
                    upper_linear_limit = None
                else:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The upper linear limit value='{upper_linear_limit:.3f}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if target_value is not None:

            if lower_limit is not None:
                if lower_limit > target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower limit value='{lower_limit:.3f}' must be less than the target value '{target_value}'. "\
                        "It indicates that a negative value was unexpectedly set: "\
                        f"d={target_value}, dminus={self.numberSelection[1]}, dplus={self.numberSelection[2]}.\n"

            if lower_linear_limit is not None:
                if lower_linear_limit > target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower linear limit value='{lower_linear_limit:.3f}' must be less than the target value '{target_value}'. "\
                        "It indicates that a negative value was unexpectedly set: "\
                        f"d={target_value}, dminus={self.numberSelection[1]}, dplus={self.numberSelection[2]}.\n"

            if upper_limit is not None:
                if upper_limit < target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The upper limit value='{upper_limit:.3f}' must be greater than the target value '{target_value}'. "\
                        "It indicates that a negative value was unexpectedly set: "\
                        f"d={target_value}, dminus={self.numberSelection[1]}, dplus={self.numberSelection[2]}.\n"

            if upper_linear_limit is not None:
                if upper_linear_limit < target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The upper linear limit value='{upper_linear_limit:.3f}' must be greater than the target value '{target_value}'. "\
                        "It indicates that a negative value was unexpectedly set: "\
                        f"d={target_value}, dminus={self.numberSelection[1]}, dplus={self.numberSelection[2]}.\n"

        else:

            if lower_limit is not None and upper_limit is not None:
                if lower_limit > upper_limit:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower limit value='{lower_limit:.3f}' must be less than the upper limit value '{upper_limit:.3f}'.\n"

            if lower_linear_limit is not None and upper_limit is not None:
                if lower_linear_limit > upper_limit:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower linear limit value='{lower_linear_limit:.3f}' must be less than the upper limit value '{upper_limit:.3f}'.\n"

            if lower_limit is not None and upper_linear_limit is not None:
                if lower_limit > upper_linear_limit:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower limit value='{lower_limit:.3f}' must be less than the upper limit value '{upper_linear_limit:.3f}'.\n"

            if lower_linear_limit is not None and upper_linear_limit is not None:
                if lower_linear_limit > upper_linear_limit:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower linear limit value='{lower_linear_limit:.3f}' must be less than the upper limit value '{upper_linear_limit:.3f}'.\n"

            if lower_limit is not None and lower_linear_limit is not None:
                if lower_linear_limit > lower_limit:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower linear limit value='{lower_linear_limit:.3f}' must be less than the lower limit value '{lower_limit:.3f}'.\n"

            if upper_limit is not None and upper_linear_limit is not None:
                if upper_limit > upper_linear_limit:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The upper limit value='{upper_limit:.3f}' must be less than the upper linear limit value '{upper_linear_limit:.3f}'.\n"

        if not validRange:
            return None

        if target_value is not None:
            if DIST_RANGE_MIN <= target_value <= DIST_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The target value='{target_value}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        if lower_limit is not None:
            if DIST_RANGE_MIN <= lower_limit <= DIST_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The lower limit value='{lower_limit:.3f}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        if upper_limit is not None:
            if DIST_RANGE_MIN <= upper_limit <= DIST_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit:.3f}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        if lower_linear_limit is not None:
            if DIST_RANGE_MIN <= lower_linear_limit <= DIST_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The lower linear limit value='{lower_linear_limit:.3f}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        if upper_linear_limit is not None:
            if DIST_RANGE_MIN <= upper_linear_limit <= DIST_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The upper linear limit value='{upper_linear_limit:.3f}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        return dstFunc

    # Enter a parse tree produced by CnsMRParser#predict_statement.
    def enterPredict_statement(self, ctx: CnsMRParser.Predict_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#predict_statement.
    def exitPredict_statement(self, ctx: CnsMRParser.Predict_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#noe_annotation.
    def enterNoe_annotation(self, ctx: CnsMRParser.Noe_annotationContext):
        if ctx.Weight():
            self.scale_a = self.getNumber_a(ctx.number_a())

    # Exit a parse tree produced by CnsMRParser#noe_annotation.
    def exitNoe_annotation(self, ctx: CnsMRParser.Noe_annotationContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#dihedral_statement.
    def enterDihedral_statement(self, ctx: CnsMRParser.Dihedral_statementContext):
        if ctx.Scale():
            self.scale = self.getNumber_s(ctx.number_s())
            if isinstance(self.scale, str):
                if self.scale in self.evaluate:
                    self.scale = self.evaluate[self.scale]
                else:
                    self.warningMessage += "[Unsupported data] "\
                        f"The scale value 'RESTRAINTS DIHEDRAL {str(ctx.Scale())}={self.scale} END' "\
                        f"where the symbol {self.scale!r} is not defined so that set the default value.\n"
                    self.scale = 1.0
            if self.scale < 0.0:
                self.warningMessage += "[Invalid data] "\
                    f"The scale value 'RESTRAINTS DIHEDRAL {str(ctx.Scale())}={self.scale} END' must not be a negative value.\n"
            elif self.scale == 0.0:
                self.warningMessage += "[Range value warning] "\
                    f"The scale value 'RESTRAINTS DIHEDRAL {str(ctx.Scale())}={self.scale} END' should be a positive value.\n"

        elif ctx.Reset():
            self.scale = 1.0

    # Exit a parse tree produced by CnsMRParser#dihedral_statement.
    def exitDihedral_statement(self, ctx: CnsMRParser.Dihedral_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#dihedral_assign.
    def enterDihedral_assign(self, ctx: CnsMRParser.Dihedral_assignContext):  # pylint: disable=unused-argument
        self.dihedRestraints += 1
        if self.__cur_subtype != 'dihed':
            self.dihedStatements += 1
        self.__cur_subtype = 'dihed'

        self.atomSelectionSet.clear()
        self.__warningInAtomSelection = ''

    # Exit a parse tree produced by CnsMRParser#dihedral_assign.
    def exitDihedral_assign(self, ctx: CnsMRParser.Dihedral_assignContext):

        try:

            if None in self.numberSelection:
                return

            energyConst = self.numberSelection[0]
            target = self.numberSelection[1]
            delta = abs(self.numberSelection[2])
            exponent = int(str(ctx.Integer()))

            if energyConst <= 0.0:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The energy constant value {energyConst} must be a positive value.\n"
                return

            if exponent not in (0, 1, 2, 4):
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The exponent value of dihedral angle restraint 'ed={exponent}' should be 1 (linear well), 2 (square well) or 4 (quartic well).\n"
                return

            target_value = target
            lower_limit = None
            upper_limit = None
            lower_linear_limit = None
            upper_linear_limit = None

            if delta > 0.0:
                if exponent in (2, 4):
                    lower_limit = target - delta
                    upper_limit = target + delta
                else:
                    lower_linear_limit = target - delta
                    upper_linear_limit = target + delta

            dstFunc = self.validateAngleRange(self.scale if exponent > 0 else 0.0, {'energy_const': energyConst, 'exponent': exponent},
                                              target_value, lower_limit, upper_limit,
                                              lower_linear_limit, upper_linear_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            if not self.areUniqueCoordAtoms('a dihedral angle (DIHE)'):
                if len(self.__warningInAtomSelection) > 0:
                    self.warningMessage += self.__warningInAtomSelection
                return

            if self.__createSfDict:
                sf = self.__getSf(potentialType=getPotentialType(self.__file_type, self.__cur_subtype, dstFunc))
                sf['id'] += 1

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
                    print(f"subtype={self.__cur_subtype} (DIHE) id={self.dihedRestraints} angleName={angleName} "
                          f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} {dstFunc}")
                if self.__createSfDict and sf is not None:
                    sf['index_id'] += 1
                    row = getRow(self.__cur_subtype, sf['id'], sf['index_id'],
                                 '.', angleName,
                                 sf['list_id'], self.__entryId, dstFunc, self.__authToStarSeq, atom1, atom2, atom3, atom4)
                    sf['loop'].add_data(row)

        finally:
            self.numberSelection.clear()

    def validateAngleRange(self, weight, misc_dict,
                           target_value, lower_limit, upper_limit,
                           lower_linear_limit=None, upper_linear_limit=None):
        """ Validate angle value range.
        """

        validRange = True
        dstFunc = {'weight': weight}

        if self.__correctCircularShift:
            _array = numpy.array([target_value, lower_limit, upper_limit, lower_linear_limit, upper_linear_limit],
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
                if lower_linear_limit is not None:
                    upper_linear_limit += shift
                if upper_linear_limit is not None:
                    upper_linear_limit += shift

        if isinstance(misc_dict, dict):
            for k, v in misc_dict.items():
                dstFunc[k] = v

        if target_value is not None:
            if ANGLE_ERROR_MIN < target_value < ANGLE_ERROR_MAX:
                dstFunc['target_value'] = f"{target_value}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The target value='{target_value}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"

        if lower_limit is not None:
            if ANGLE_ERROR_MIN <= lower_limit < ANGLE_ERROR_MAX:
                dstFunc['lower_limit'] = f"{lower_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower limit value='{lower_limit:.3f}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"

        if upper_limit is not None:
            if ANGLE_ERROR_MIN < upper_limit <= ANGLE_ERROR_MAX:
                dstFunc['upper_limit'] = f"{upper_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit:.3f}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"

        if lower_linear_limit is not None:
            if ANGLE_ERROR_MIN <= lower_linear_limit < ANGLE_ERROR_MAX:
                dstFunc['lower_linear_limit'] = f"{lower_linear_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower linear limit value='{lower_linear_limit:.3f}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"

        if upper_linear_limit is not None:
            if ANGLE_ERROR_MIN < upper_linear_limit <= ANGLE_ERROR_MAX:
                dstFunc['upper_linear_limit'] = f"{upper_linear_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper linear limit value='{upper_linear_limit:.3f}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"

        if lower_limit is not None and lower_linear_limit is not None:
            if lower_linear_limit > lower_limit:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower linear limit value='{lower_linear_limit:.3f}' must be less than the lower limit value '{lower_limit:.3f}'.\n"

        if upper_limit is not None and upper_linear_limit is not None:
            if upper_limit > upper_linear_limit:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit:.3f}' must be less than the upper linear limit value '{upper_linear_limit:.3f}'.\n"

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
                    f"The lower limit value='{lower_limit:.3f}' should be within range {ANGLE_RESTRAINT_RANGE}.\n"

        if upper_limit is not None:
            if ANGLE_RANGE_MIN <= upper_limit <= ANGLE_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit:.3f}' should be within range {ANGLE_RESTRAINT_RANGE}.\n"

        if lower_linear_limit is not None:
            if ANGLE_RANGE_MIN <= lower_linear_limit <= ANGLE_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The lower linear limit value='{lower_linear_limit:.3f}' should be within range {ANGLE_RESTRAINT_RANGE}.\n"

        if upper_linear_limit is not None:
            if ANGLE_RANGE_MIN <= upper_linear_limit <= ANGLE_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The upper linear limit value='{upper_linear_limit:.3f}' should be within range {ANGLE_RESTRAINT_RANGE}.\n"

        return dstFunc

    def areUniqueCoordAtoms(self, subtype_name, skip_col=None):
        """ Check whether atom selection sets are uniquely assigned.
        """

        for col, _atomSelectionSet in enumerate(self.atomSelectionSet):
            _lenAtomSelectionSet = len(_atomSelectionSet)

            if _lenAtomSelectionSet == 0:
                if skip_col is not None and col in skip_col:
                    continue
                return False  # raised error already

            if _lenAtomSelectionSet == 1:
                continue

            for (atom1, atom2) in itertools.combinations(_atomSelectionSet, 2):
                if atom1['chain_id'] != atom2['chain_id']:
                    continue
                if atom1['seq_id'] != atom2['seq_id']:
                    continue
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Ambiguous atom selection '{atom1['chain_id']}:{atom1['seq_id']}:{atom1['comp_id']}:{atom1['atom_id']} or "\
                    f"{atom2['atom_id']}' is not allowed as {subtype_name} restraint.\n"
                return False

        return True

    # Enter a parse tree produced by CnsMRParser#plane_statement.
    def enterPlane_statement(self, ctx: CnsMRParser.Plane_statementContext):
        if ctx.Initialize():
            self.planeWeight = 300.0

    # Exit a parse tree produced by CnsMRParser#plane_statement.
    def exitPlane_statement(self, ctx: CnsMRParser.Plane_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#plane_group.
    def enterPlane_group(self, ctx: CnsMRParser.Plane_groupContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#plane_group.
    def exitPlane_group(self, ctx: CnsMRParser.Plane_groupContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#group_statement.
    def enterGroup_statement(self, ctx: CnsMRParser.Group_statementContext):
        self.planeRestraints += 1
        if self.__cur_subtype != 'plane':
            self.planeStatements += 1
        self.__cur_subtype = 'plane'

        self.atomSelectionSet.clear()
        self.__warningInAtomSelection = ''

        if ctx.Weight():
            self.planeWeight = self.getNumber_s(ctx.number_s())
            if isinstance(self.planeWeight, str):
                if self.planeWeight in self.evaluate:
                    self.planeWeight = self.evaluate[self.planeWeight]
                else:
                    self.warningMessage += "[Unsupported data] "\
                        f"The weight value 'GROUP {str(ctx.Weight())}={self.planeWeight} END' "\
                        f"where the symbol {self.planeWeight!r} is not defined so that set the default value.\n"
                    self.planeWeight = 300.0
            if self.planeWeight < 0.0:
                self.warningMessage += "[Invalid data] "\
                    f"The weight value 'GROUP {str(ctx.Weight())}={self.planeWeight} END' must not be a negative value.\n"
            elif self.planeWeight == 0.0:
                self.warningMessage += "[Range value warning] "\
                    f"The weight value 'GROUP {str(ctx.Weight())}={self.planeWeight} END' should be a positive value.\n"

    # Exit a parse tree produced by CnsMRParser#group_statement.
    def exitGroup_statement(self, ctx: CnsMRParser.Group_statementContext):  # pylint: disable=unused-argument
        if not self.__hasPolySeq:
            return

        if len(self.atomSelectionSet) == 0:
            return

        if self.__createSfDict:
            sf = self.__getSf('planality restraint, CNS PLANE/GROUP statement')
            sf['id'] += 1
            if len(sf['loop']['tags']) == 0:
                sf['loop']['tags'] = ['index_id', 'id',
                                      'auth_asym_id', 'auth_seq_id', 'auth_comp_id', 'auth_atom_id',
                                      'list_id', 'entry_id']
                sf['tags'].append(['weight', self.planeWeight])

        for atom1 in self.atomSelectionSet[0]:
            if self.__debug:
                print(f"subtype={self.__cur_subtype} (PLANE/GROUP) id={self.planeRestraints} "
                      f"atom={atom1} weight={self.planeWeight}")
            if self.__createSfDict and sf is not None:
                sf['index_id'] += 1
                sf['loop']['data'].append([sf['index_id'], sf['id'],
                                           atom1['chain_id'], atom1['seq_id'], atom1['comp_id'], atom1['atom_id'],
                                           sf['list_id'], self.__entryId])

    # Enter a parse tree produced by CnsMRParser#harmonic_statement.
    def enterHarmonic_statement(self, ctx: CnsMRParser.Harmonic_statementContext):
        if ctx.Exponent():
            self.squareExponent = int(str(ctx.Integer()))
            if self.squareExponent <= 0.0:
                self.warningMessage += "[Invalid data] "\
                    "The exponent value  "\
                    f"'RESTRAINTS HARMONIC {str(ctx.Exponent())}={self.squareExponent} END' must be a positive value.\n"

        elif ctx.Normal():
            if ctx.number_s(0):
                self.vector3D = [self.getNumber_s(ctx.number_s(0)),
                                 self.getNumber_s(ctx.number_s(1)),
                                 self.getNumber_s(ctx.number_s(2))]

            elif ctx.Tail():
                self.inVector3D = True
                self.inVector3D_columnSel = -1
                self.inVector3D_tail = None
                self.inVector3D_head = None
                self.vector3D = None

    # Exit a parse tree produced by CnsMRParser#harmonic_statement.
    def exitHarmonic_statement(self, ctx: CnsMRParser.Harmonic_statementContext):  # pylint: disable=unused-argument
        if self.vector3D is None:
            self.vector3D = [0.0] * 3  # set default vector if not available

        if 'harm' not in self.vectorDo or len(self.vector3D['harm']) == 0:
            self.warningMessage += "[Invalid data] "\
                "No vector statement for harmonic coordinate restraints exists.\n"
            return

        for col, vector in enumerate(self.vector3D['harm'], start=1):
            dstFunc = {}
            if 'value' in vector:
                dstFunc['energy_const'] = vector['value']
            dstFunc['exponent'] = self.squareExponent
            for atom1 in vector['atom_selection']:
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} (HARM) id={col} "
                          f"atom={atom1} {dstFunc} normal_vector={self.vector3D}")

        self.vector3D['harm'] = []

    # Enter a parse tree produced by CnsMRParser#harmonic_assign.
    def enterHarmonic_assign(self, ctx: CnsMRParser.Harmonic_assignContext):  # pylint: disable=unused-argument
        self.geoRestraints += 1
        if self.__cur_subtype != 'geo':
            self.geoStatements += 1
        self.__cur_subtype = 'geo'

        self.atomSelectionSet.clear()
        self.__warningInAtomSelection = ''

    # Exit a parse tree produced by CnsMRParser#harmonic_assign.
    def exitHarmonic_assign(self, ctx: CnsMRParser.Harmonic_assignContext):  # pylint: disable=unused-argument

        try:

            if None in self.numberSelection:
                return

            self.vector3D = [self.numberSelection[0], self.numberSelection[1], self.numberSelection[2]]

            if not self.__hasPolySeq:
                return

            for atom1 in self.atomSelectionSet[0]:
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} (HARM) id={self.geoRestraints} "
                          f"atom={atom1} normal_vector={self.vector3D}")

        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by CnsMRParser#sani_statement.
    def enterSani_statement(self, ctx: CnsMRParser.Sani_statementContext):
        if ctx.Potential_types():
            code = str(ctx.Potential_types()).upper()
            if code.startswith('SQUA'):
                self.potential = 'square'
            elif code.startswith('HARM'):
                self.potential = 'harmonic'
            else:
                self.potential = 'square'
                self.warningMessage += "[Enum mismatch ignorable] "\
                    f"The potential type {str(ctx.Potential_types())!r} is unknown potential type for the 'SANIsotropy' statements. "\
                    f"Instead, set the default potential {self.potential!r}.\n"

        elif ctx.Reset():
            self.potential = 'square'
            self.coefficients = None

        elif ctx.Coefficients():
            self.coefficients = {'DFS': self.getNumber_s(ctx.number_s(0)),
                                 'anisotropy': self.getNumber_s(ctx.number_s(1)),
                                 'rhombicity': self.getNumber_s(ctx.number_s(2))
                                 }

    # Exit a parse tree produced by CnsMRParser#sani_statement.
    def exitSani_statement(self, ctx: CnsMRParser.Sani_statementContext):  # pylint: disable=unused-argument
        if self.__debug:
            print(f"subtype={self.__cur_subtype} (SANI) classification={self.classification!r} "
                  f"coefficients={self.coefficients}")

    # Enter a parse tree produced by CnsMRParser#sani_assign.
    def enterSani_assign(self, ctx: CnsMRParser.Sani_assignContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1
        if self.__cur_subtype != 'rdc':
            self.rdcStatements += 1
        self.__cur_subtype = 'rdc'

        self.atomSelectionSet.clear()
        self.__warningInAtomSelection = ''

    # Exit a parse tree produced by CnsMRParser#sani_assign.
    def exitSani_assign(self, ctx: CnsMRParser.Sani_assignContext):  # pylint: disable=unused-argument

        try:

            if None in self.numberSelection:
                return

            target = self.numberSelection[0]

            if len(self.numberSelection) > 1:
                delta = abs(self.numberSelection[1])
            else:
                delta = 0.0

            target_value = target
            lower_limit = None
            upper_limit = None

            if self.potential == 'square' and delta > 0.0:
                lower_limit = target - delta
                upper_limit = target + delta
                if len(self.numberSelection) > 2:
                    error_less = delta
                    error_greater = abs(self.numberSelection[2])
                    lower_limit = target - error_less
                    upper_limit = target + error_greater

            dstFunc = self.validateRdcRange(1.0, {'potential': self.potential},
                                            target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            if not self.areUniqueCoordAtoms('an RDC (SANI)', XPLOR_ORIGIN_AXIS_COLS):
                if len(self.__warningInAtomSelection) > 0:
                    self.warningMessage += self.__warningInAtomSelection
                return

            chain_id_1 = self.atomSelectionSet[4][0]['chain_id']
            seq_id_1 = self.atomSelectionSet[4][0]['seq_id']
            comp_id_1 = self.atomSelectionSet[4][0]['comp_id']
            atom_id_1 = self.atomSelectionSet[4][0]['atom_id']

            chain_id_2 = self.atomSelectionSet[5][0]['chain_id']
            seq_id_2 = self.atomSelectionSet[5][0]['seq_id']
            comp_id_2 = self.atomSelectionSet[5][0]['comp_id']
            atom_id_2 = self.atomSelectionSet[5][0]['atom_id']

            chain_id_set = None
            if self.__exptlMethod == 'SOLID-STATE NMR':
                ps = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chain_id_1 and 'identical_auth_chain_id' in ps), None)
                if ps is not None:
                    chain_id_set = [chain_id_1]
                    chain_id_set.extend(ps['identical_auth_chain_id'])
                    chain_id_set.sort()
                    if self.__symmetric != 'no':
                        pass
                    elif len(chain_id_set) > MAX_MAG_IDENT_ASYM_ID and chain_id_2 in chain_id_set:
                        self.__symmetric = 'linear'

                        try:

                            _head =\
                                self.__cR.getDictListWithFilter('atom_site',
                                                                [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                                 {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                                 {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                                                                 ],
                                                                [{'name': self.__authAsymId, 'type': 'str', 'value': chain_id_set[0]},
                                                                 {'name': self.__authSeqId, 'type': 'int', 'value': seq_id_1},
                                                                 {'name': self.__authAtomId, 'type': 'str', 'value': atom_id_1},
                                                                 {'name': self.__modelNumName, 'type': 'int',
                                                                  'value': self.__representativeModelId},
                                                                 {'name': 'label_alt_id', 'type': 'enum',
                                                                  'enum': ('A')}
                                                                 ])

                            _tail =\
                                self.__cR.getDictListWithFilter('atom_site',
                                                                [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                                 {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                                 {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                                                                 ],
                                                                [{'name': self.__authAsymId, 'type': 'str', 'value': chain_id_set[-1]},
                                                                 {'name': self.__authSeqId, 'type': 'int', 'value': seq_id_1},
                                                                 {'name': self.__authAtomId, 'type': 'str', 'value': atom_id_1},
                                                                 {'name': self.__modelNumName, 'type': 'int',
                                                                  'value': self.__representativeModelId},
                                                                 {'name': 'label_alt_id', 'type': 'enum',
                                                                  'enum': ('A')}
                                                                 ])

                            if len(_head) == 1 and len(_tail) == 1:
                                if numpy.linalg.norm(toNpArray(_head[0]) - toNpArray(_tail[0])) < 10.0:
                                    self.__symmetric = 'circular'

                        except Exception as e:
                            if self.__verbose:
                                self.__lfh.write(f"+CnsMRParserListener.exitSani_assign() ++ Error  - {str(e)}\n")

            if (atom_id_1[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS) or (atom_id_2[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS):
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Non-magnetic susceptible spin appears in RDC vector; "\
                    f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                    f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                return

            if chain_id_1 != chain_id_2:
                if self.__symmetric == 'no':
                    ps1 = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chain_id_1 and 'identical_auth_chain_id' in ps), None)
                    ps2 = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chain_id_2 and 'identical_auth_chain_id' in ps), None)
                    if ps1 is None and ps2 is None:
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            f"Found inter-chain RDC vector; "\
                            f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                        return

            elif abs(seq_id_1 - seq_id_2) > 1:
                ps1 = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chain_id_1 and 'gap_in_auth_seq' in ps and ps['gap_in_auth_seq']), None)
                if ps1 is None:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
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
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        "Found inter-residue RDC vector; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                    return

            elif atom_id_1 == atom_id_2:
                if self.__symmetric == 'no':
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        "Found zero RDC vector; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                    return

            elif self.__ccU.updateChemCompDict(comp_id_1):  # matches with comp_id in CCD

                if not any(b for b in self.__ccU.lastBonds
                           if ((b[self.__ccU.ccbAtomId1] == atom_id_1 and b[self.__ccU.ccbAtomId2] == atom_id_2)
                               or (b[self.__ccU.ccbAtomId1] == atom_id_2 and b[self.__ccU.ccbAtomId2] == atom_id_1))):

                    if self.__nefT.validate_comp_atom(comp_id_1, atom_id_1) and self.__nefT.validate_comp_atom(comp_id_2, atom_id_2):
                        if atom_id_1[0] == 'H' and atom_id_2[0] == 'H':
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                "Found an RDC vector over multiple covalent bonds in the 'SANIsotropy' statement; "\
                                f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}). "\
                                "Did you accidentally select 'SANIsotropy' statement, instead of 'XDIPolar' statement of XPLOR-NIH?\n"
                        else:
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                "Found an RDC vector over multiple covalent bonds in the 'SANIsotropy' statement; "\
                                f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                        return

            if self.__createSfDict:
                sf = self.__getSf(potentialType=getPotentialType(self.__file_type, self.__cur_subtype, dstFunc),
                                  rdcCode=getRdcCode([self.atomSelectionSet[4][0], self.atomSelectionSet[5][0]]))
                sf['id'] += 1

            for atom1, atom2 in itertools.product(self.atomSelectionSet[4],
                                                  self.atomSelectionSet[5]):
                if self.__symmetric == 'no':
                    if isLongRangeRestraint([atom1, atom2], self.__polySeq if self.__gapInAuthSeq else None):
                        continue
                else:
                    if isAsymmetricRangeRestraint([atom1, atom2], chain_id_set, self.__symmetric):
                        continue
                    if atom1['chain_id'] != atom2['chain_id']:
                        self.warningMessage += f"[Anomalous RDC vector] {self.__getCurrentRestraint()}"\
                            f"Found inter-chain RDC vector; "\
                            f"({atom1['chain_id']}:{atom1['seq_id']}:{atom1['comp_id']}:{atom1['atom_id']}, "\
                            f"{atom2['chain_id']}:{atom2['seq_id']}:{atom2['comp_id']}:{atom2['atom_id']}). "\
                            "However, it might be an artificial RDC constraint on solid-state NMR applied to symmetric samples such as fibrils.\n"

                if self.__debug:
                    print(f"subtype={self.__cur_subtype} (SANI) id={self.rdcRestraints} "
                          f"atom1={atom1} atom2={atom2} {dstFunc}")
                if self.__createSfDict and sf is not None:
                    sf['index_id'] += 1
                    row = getRow(self.__cur_subtype, sf['id'], sf['index_id'],
                                 '.', None,
                                 sf['list_id'], self.__entryId, dstFunc, self.__authToStarSeq, atom1, atom2)
                    sf['loop'].add_data(row)

        finally:
            self.numberSelection.clear()

    def validateRdcRange(self, weight, misc_dict,
                         target_value, lower_limit, upper_limit,
                         lower_linear_limit=None, upper_linear_limit=None):
        """ Validate angle value range.
        """

        validRange = True
        dstFunc = {'weight': weight}

        if isinstance(misc_dict, dict):
            for k, v in misc_dict.items():
                dstFunc[k] = v

        if target_value is not None:
            if RDC_ERROR_MIN < target_value < RDC_ERROR_MAX:
                dstFunc['target_value'] = f"{target_value}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The target value='{target_value}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if lower_limit is not None:
            if RDC_ERROR_MIN <= lower_limit < RDC_ERROR_MAX:
                dstFunc['lower_limit'] = f"{lower_limit:.6f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower limit value='{lower_limit:.6f}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if upper_limit is not None:
            if RDC_ERROR_MIN < upper_limit <= RDC_ERROR_MAX:
                dstFunc['upper_limit'] = f"{upper_limit:.6f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit:.6f}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if lower_linear_limit is not None:
            if RDC_ERROR_MIN <= lower_linear_limit < RDC_ERROR_MAX:
                dstFunc['lower_linear_limit'] = f"{lower_linear_limit:.6f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower linear limit value='{lower_linear_limit:.6f}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if upper_linear_limit is not None:
            if RDC_ERROR_MIN < upper_linear_limit <= RDC_ERROR_MAX:
                dstFunc['upper_linear_limit'] = f"{upper_linear_limit:.6f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper linear limit value='{upper_linear_limit:.6f}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if target_value is not None:

            if lower_limit is not None:
                if lower_limit > target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower limit value='{lower_limit:.6f}' must be less than the target value '{target_value}'.\n"

            if lower_linear_limit is not None:
                if lower_linear_limit > target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower linear limit value='{lower_linear_limit:.6f}' must be less than the target value '{target_value}'.\n"

            if upper_limit is not None:
                if upper_limit < target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The upper limit value='{upper_limit:.6f}' must be greater than the target value '{target_value}'.\n"

            if upper_linear_limit is not None:
                if upper_linear_limit < target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The upper linear limit value='{upper_linear_limit:.6f}' must be greater than the target value '{target_value}'.\n"

        else:

            if lower_limit is not None and upper_limit is not None:
                if lower_limit > upper_limit:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower limit value='{lower_limit:.6f}' must be less than the upper limit value '{upper_limit:.6f}'.\n"

            if lower_linear_limit is not None and upper_limit is not None:
                if lower_linear_limit > upper_limit:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower linear limit value='{lower_linear_limit:.6f}' must be less than the upper limit value '{upper_limit:.6f}'.\n"

            if lower_limit is not None and upper_linear_limit is not None:
                if lower_limit > upper_linear_limit:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower limit value='{lower_limit:.6f}' must be less than the upper limit value '{upper_linear_limit:.6f}'.\n"

            if lower_linear_limit is not None and upper_linear_limit is not None:
                if lower_linear_limit > upper_linear_limit:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower linear limit value='{lower_linear_limit:.6f}' must be less than the upper limit value '{upper_linear_limit:.6f}'.\n"

            if lower_limit is not None and lower_linear_limit is not None:
                if lower_linear_limit > lower_limit:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower linear limit value='{lower_linear_limit:.6f}' must be less than the lower limit value '{lower_limit:.6f}'.\n"

            if upper_limit is not None and upper_linear_limit is not None:
                if upper_limit > upper_linear_limit:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The upper limit value='{upper_limit:.6f}' must be less than the upper linear limit value '{upper_linear_limit:.6f}'.\n"

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
                    f"The lower limit value='{lower_limit:.6f}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        if upper_limit is not None:
            if RDC_RANGE_MIN <= upper_limit <= RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit:.6f}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        if lower_linear_limit is not None:
            if RDC_RANGE_MIN <= lower_linear_limit <= RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The lower linear limit value='{lower_linear_limit:.6f}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        if upper_linear_limit is not None:
            if RDC_RANGE_MIN <= upper_linear_limit <= RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The upper linear limit value='{upper_linear_limit:.6f}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        return dstFunc

    # Enter a parse tree produced by CnsMRParser#coupling_statement.
    def enterCoupling_statement(self, ctx: CnsMRParser.Coupling_statementContext):
        if ctx.Potential_types():
            code = str(ctx.Potential_types()).upper()
            if code.startswith('SQUA'):
                self.potential = 'square'
            elif code.startswith('HARM'):
                self.potential = 'harmonic'
            elif code.startswith('MULT'):
                self.potential = 'multiple'
            else:
                self.potential = 'square'
                self.warningMessage += "[Enum mismatch ignorable] "\
                    f"The potential type {str(ctx.Potential_types())!r} is unknown potential type for the 'COUPling' statements. "\
                    f"Instead, set the default potential {self.potential!r}.\n"

        elif ctx.Reset():
            self.potential = 'square'
            self.coefficients = None

        elif ctx.Coefficients():
            self.coefficients = {'Karplus_coef_a': self.getNumber_s(ctx.number_s(0)),
                                 'Karplus_coef_b': self.getNumber_s(ctx.number_s(1)),
                                 'Karplus_coef_c': self.getNumber_s(ctx.number_s(2)),
                                 'Karplus_phase': self.getNumber_s(ctx.number_s(3))
                                 }

    # Exit a parse tree produced by CnsMRParser#coupling_statement.
    def exitCoupling_statement(self, ctx: CnsMRParser.Coupling_statementContext):  # pylint: disable=unused-argument
        if self.__debug:
            print(f"subtype={self.__cur_subtype} (COUP) classification={self.classification!r} "
                  f"coefficients={self.coefficients}")

    # Enter a parse tree produced by CnsMRParser#coup_assign.
    def enterCoup_assign(self, ctx: CnsMRParser.Coup_assignContext):  # pylint: disable=unused-argument
        self.jcoupRestraints += 1
        if self.__cur_subtype != 'jcoup':
            self.jcoupStatements += 1
        self.__cur_subtype = 'jcoup'

        self.atomSelectionSet.clear()
        self.__warningInAtomSelection = ''

    # Exit a parse tree produced by CnsMRParser#coup_assign.
    def exitCoup_assign(self, ctx: CnsMRParser.Coup_assignContext):  # pylint: disable=unused-argument

        try:

            if None in self.numberSelection:
                return

            target = self.numberSelection[0]
            delta = abs(self.numberSelection[1])

            target_value = target
            lower_limit = None
            upper_limit = None

            if self.potential != 'harmonic' and delta > 0.0:
                lower_limit = target - delta
                upper_limit = target + delta

            dstFunc = self.validateRdcRange(1.0, {'potential': self.potential},
                                            target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            dstFunc2 = None

            if len(self.numberSelection) > 3:
                target = self.numberSelection[2]
                delta = abs(self.numberSelection[3])

                target_value = target
                lower_limit = None
                upper_limit = None

                if self.potential != 'harmonic' and delta > 0.0:
                    lower_limit = target - delta
                    upper_limit = target + delta

                dstFunc2 = self.validateRdcRange(1.0, {'potential': self.potential},
                                                 target_value, lower_limit, upper_limit)

                if dstFunc2 is None:
                    return

            if not self.__hasPolySeq:
                return

            if not self.areUniqueCoordAtoms('a J-coupling (COUP)'):
                if len(self.__warningInAtomSelection) > 0:
                    self.warningMessage += self.__warningInAtomSelection
                return

            for i in range(0, len(self.atomSelectionSet), 4):
                chain_id_1 = self.atomSelectionSet[i][0]['chain_id']
                seq_id_1 = self.atomSelectionSet[i][0]['seq_id']
                comp_id_1 = self.atomSelectionSet[i][0]['comp_id']
                atom_id_1 = self.atomSelectionSet[i][0]['atom_id']

                chain_id_2 = self.atomSelectionSet[i + 3][0]['chain_id']
                seq_id_2 = self.atomSelectionSet[i + 3][0]['seq_id']
                comp_id_2 = self.atomSelectionSet[i + 3][0]['comp_id']
                atom_id_2 = self.atomSelectionSet[i + 3][0]['atom_id']

                if (atom_id_1[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS) or (atom_id_2[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS):
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"Non-magnetic susceptible spin appears in J-coupling vector; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                        f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                    return

                if chain_id_1 != chain_id_2:
                    ps1 = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chain_id_1 and 'identical_auth_chain_id' in ps), None)
                    ps2 = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chain_id_2 and 'identical_auth_chain_id' in ps), None)
                    if ps1 is None and ps2 is None:
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            f"Found inter-chain J-coupling vector; "\
                            f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                        return

                elif abs(seq_id_1 - seq_id_2) > 1:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"Found inter-residue J-coupling vector; "\
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
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            "Found inter-residue J-coupling vector; "\
                            f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                        return

                elif atom_id_1 == atom_id_2:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        "Found zero J-coupling vector; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                    return

                elif self.__ccU.updateChemCompDict(comp_id_1):  # matches with comp_id in CCD

                    if not any(b for b in self.__ccU.lastBonds
                               if ((b[self.__ccU.ccbAtomId1] == atom_id_1 and b[self.__ccU.ccbAtomId2] == atom_id_2)
                                   or (b[self.__ccU.ccbAtomId1] == atom_id_2 and b[self.__ccU.ccbAtomId2] == atom_id_1))):

                        if self.__nefT.validate_comp_atom(comp_id_1, atom_id_1) and self.__nefT.validate_comp_atom(comp_id_2, atom_id_2):
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                "Found an J-coupling vector over multiple covalent bonds in the 'COUPling' statement; "\
                                f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                            return

            if self.__createSfDict:
                sf = self.__getSf()
                sf['id'] += 1

            if len(self.atomSelectionSet) == 4:
                for atom1, atom2, atom3, atom4 in itertools.product(self.atomSelectionSet[0],
                                                                    self.atomSelectionSet[1],
                                                                    self.atomSelectionSet[2],
                                                                    self.atomSelectionSet[3]):
                    if isLongRangeRestraint([atom1, atom2, atom3, atom4], self.__polySeq if self.__gapInAuthSeq else None):
                        continue
                    if self.__debug:
                        print(f"subtype={self.__cur_subtype} (COUP) id={self.jcoupRestraints} "
                              f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} {dstFunc}")
                    if self.__createSfDict and sf is not None:
                        sf['index_id'] += 1
                        row = getRow(self.__cur_subtype, sf['id'], sf['index_id'],
                                     '.', None,
                                     sf['list_id'], self.__entryId, dstFunc, self.__authToStarSeq, atom1, atom2, atom3, atom4)
                        sf['loop'].add_data(row)

            else:
                for atom1, atom2, atom3, atom4 in itertools.product(self.atomSelectionSet[0],
                                                                    self.atomSelectionSet[1],
                                                                    self.atomSelectionSet[2],
                                                                    self.atomSelectionSet[3]):
                    if isLongRangeRestraint([atom1, atom2, atom3, atom4], self.__polySeq if self.__gapInAuthSeq else None):
                        continue
                    if self.__debug:
                        print(f"subtype={self.__cur_subtype} (COUP) id={self.jcoupRestraints} "
                              f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} {dstFunc}")
                    if self.__createSfDict and sf is not None:
                        sf['index_id'] += 1
                        row = getRow(self.__cur_subtype, sf['id'], sf['index_id'],
                                     '.', None,
                                     sf['list_id'], self.__entryId, dstFunc, self.__authToStarSeq, atom1, atom2)
                        sf['loop'].add_data(row)

                for atom1, atom2, atom3, atom4 in itertools.product(self.atomSelectionSet[4],
                                                                    self.atomSelectionSet[5],
                                                                    self.atomSelectionSet[6],
                                                                    self.atomSelectionSet[7]):
                    if isLongRangeRestraint([atom1, atom2, atom3, atom4], self.__polySeq if self.__gapInAuthSeq else None):
                        continue
                    if self.__debug:
                        if dstFunc2 is None:
                            print(f"subtype={self.__cur_subtype} (COUP) id={self.jcoupRestraints} "
                                  f"atom4={atom1} atom5={atom2} atom6={atom3} atom7={atom4} {dstFunc}")
                        else:
                            print(f"subtype={self.__cur_subtype} (COUP) id={self.jcoupRestraints} "
                                  f"atom4={atom1} atom5={atom2} atom6={atom3} atom7={atom4} {dstFunc2}")
                    if self.__createSfDict and sf is not None:
                        sf['index_id'] += 1
                        row = getRow(self.__cur_subtype, sf['id'], sf['index_id'],
                                     '.', None,
                                     sf['list_id'], self.__entryId, dstFunc if dstFunc2 is None else dstFunc2, self.__authToStarSeq,
                                     atom1, atom2, atom3, atom4)
                        sf['loop'].add_data(row)

        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by CnsMRParser#carbon_shift_statement.
    def enterCarbon_shift_statement(self, ctx: CnsMRParser.Carbon_shift_statementContext):
        if ctx.Potential_types():
            code = str(ctx.Potential_types()).upper()
            if code.startswith('SQUA'):
                self.potential = 'square'
            elif code.startswith('HARM'):
                self.potential = 'harmonic'
            else:
                self.potential = 'square'
                self.warningMessage += "[Enum mismatch ignorable] "\
                    f"The potential type {str(ctx.Potential_types())!r} is unknown potential type for the 'CARBon' statements. "\
                    f"Instead, set the default potential {self.potential!r}.\n"

        elif ctx.Reset():
            self.potential = 'square'

        elif ctx.Expectation():
            self.csExpect = {'psi_position': int(str(ctx.Integer(0))),
                             'phi_poistion': int(str(ctx.Integer(1))),
                             'ca_shift': self.getNumber_s(ctx.number_s(0)),
                             'ca_shift_error': self.getNumber_s(ctx.number_s(1)),
                             'cb_shift': self.getNumber_s(ctx.number_s(2)),
                             'cb_shift_error': self.getNumber_s(ctx.number_s(3))
                             }

    # Exit a parse tree produced by CnsMRParser#carbon_shift_statement.
    def exitCarbon_shift_statement(self, ctx: CnsMRParser.Carbon_shift_statementContext):  # pylint: disable=unused-argument
        if self.__debug:
            print(f"subtype={self.__cur_subtype} (CARB) classification={self.classification!r} "
                  f"expectation={self.csExpect}")

    # Enter a parse tree produced by CnsMRParser#carbon_shift_assign.
    def enterCarbon_shift_assign(self, ctx: CnsMRParser.Carbon_shift_assignContext):  # pylint: disable=unused-argument
        self.hvycsRestraints += 1
        self.__cur_subtype = 'hvycs'

        self.atomSelectionSet.clear()
        self.__warningInAtomSelection = ''

    # Exit a parse tree produced by CnsMRParser#carbon_shift_assign.
    def exitCarbon_shift_assign(self, ctx: CnsMRParser.Carbon_shift_assignContext):  # pylint: disable=unused-argument

        try:

            if None in self.numberSelection:
                return

            ca_shift = self.numberSelection[0]
            cb_shift = self.numberSelection[1]

            if CS_ERROR_MIN < ca_shift < CS_ERROR_MAX:
                pass
            else:
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"CA chemical shift value '{ca_shift}' must be within range {CS_RESTRAINT_ERROR}.\n"
                return

            if not self.__hasPolySeq:
                return

            if not self.areUniqueCoordAtoms('a carbon chemical shift (CARB)'):
                if len(self.__warningInAtomSelection) > 0:
                    self.warningMessage += self.__warningInAtomSelection
                return

            dstFunc = {'ca_shift': ca_shift, 'cb_shift': cb_shift, 'weight': 1.0, 'potential': self.potential}

            chain_id_1 = self.atomSelectionSet[0][0]['chain_id']
            seq_id_1 = self.atomSelectionSet[0][0]['seq_id']
            atom_id_1 = self.atomSelectionSet[0][0]['atom_id']

            chain_id_2 = self.atomSelectionSet[1][0]['chain_id']
            seq_id_2 = self.atomSelectionSet[1][0]['seq_id']
            atom_id_2 = self.atomSelectionSet[1][0]['atom_id']

            chain_id_3 = self.atomSelectionSet[2][0]['chain_id']
            seq_id_3 = self.atomSelectionSet[2][0]['seq_id']
            atom_id_3 = self.atomSelectionSet[2][0]['atom_id']

            chain_id_4 = self.atomSelectionSet[3][0]['chain_id']
            seq_id_4 = self.atomSelectionSet[3][0]['seq_id']
            atom_id_4 = self.atomSelectionSet[3][0]['atom_id']

            chain_id_5 = self.atomSelectionSet[4][0]['chain_id']
            seq_id_5 = self.atomSelectionSet[4][0]['seq_id']
            atom_id_5 = self.atomSelectionSet[4][0]['atom_id']

            chain_ids = [chain_id_1, chain_id_2, chain_id_3, chain_id_4, chain_id_5]
            seq_ids = [seq_id_1, seq_id_2, seq_id_3, seq_id_4, seq_id_5]
            offsets = [seq_id - seq_id_3 for seq_id in seq_ids]
            atom_ids = [atom_id_1, atom_id_2, atom_id_3, atom_id_4, atom_id_5]

            if chain_ids != [chain_id_1] * 5 or offsets != [-1, 0, 0, 0, 1] or atom_ids != ['C', 'N', 'CA', 'C', 'N']:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    "The atom selection order must be [C(i-1), N(i), CA(i), C(i), N(i+1)].\n"
                return

            comp_id = self.atomSelectionSet[2][0]['comp_id']

            if comp_id == 'GLY':
                del dstFunc['cb_shift']

            else:

                if CS_ERROR_MIN < cb_shift < CS_ERROR_MAX:
                    pass
                else:
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"CB chemical shift value '{ca_shift}' must be within range {CS_RESTRAINT_ERROR}.\n"
                    return

            if self.__createSfDict:
                sf = self.__getSf()
                sf['id'] += 1

            for atom1, atom2, atom3, atom4, atom5 in itertools.product(self.atomSelectionSet[0],
                                                                       self.atomSelectionSet[1],
                                                                       self.atomSelectionSet[2],
                                                                       self.atomSelectionSet[3],
                                                                       self.atomSelectionSet[4]):
                if isLongRangeRestraint([atom1, atom2, atom3, atom4], self.__polySeq if self.__gapInAuthSeq else None):
                    continue
                if isLongRangeRestraint([atom2, atom3, atom4, atom5], self.__polySeq if self.__gapInAuthSeq else None):
                    continue
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} (CARB) id={self.hvycsRestraints} "
                          f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} atom5={atom5} {dstFunc}")
                if self.__createSfDict and sf is not None:
                    sf['index_id'] += 1
                    row = getRow(self.__cur_subtype, sf['id'], sf['index_id'],
                                 '.', None,
                                 sf['list_id'], self.__entryId, dstFunc, self.__authToStarSeq, atom1, atom2, atom3, atom4, atom5)
                    sf['loop'].add_data(row)

        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by CnsMRParser#carbon_shift_rcoil.
    def enterCarbon_shift_rcoil(self, ctx: CnsMRParser.Carbon_shift_rcoilContext):  # pylint: disable=unused-argument
        self.atomSelectionSet.clear()
        self.__warningInAtomSelection = ''

    # Exit a parse tree produced by CnsMRParser#carbon_shift_rcoil.
    def exitCarbon_shift_rcoil(self, ctx: CnsMRParser.Carbon_shift_rcoilContext):  # pylint: disable=unused-argument

        try:

            if None in self.numberSelection:
                return

            rcoil_a = self.numberSelection[0]
            rcoil_b = self.numberSelection[1]

            if CS_ERROR_MIN < rcoil_a < CS_ERROR_MAX:
                pass
            else:
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"Random coil 'a' chemical shift value '{rcoil_a}' must be within range {CS_RESTRAINT_ERROR}.\n"
                return

            if CS_ERROR_MIN < rcoil_b < CS_ERROR_MAX:
                pass
            else:
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"Random coil 'b' chemical shift value '{rcoil_b}' must be within range {CS_RESTRAINT_ERROR}.\n"
                return

            dstFunc = {'rcoil_a': rcoil_a, 'rcoil_b': rcoil_b}

            for atom1 in self.atomSelectionSet[0]:
                if atom1['atom_id'][0] != 'C':
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"Not a carbon; {atom1}.\n"
                    return

            for atom1 in self.atomSelectionSet[0]:
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} (CARB/RCOI) id={self.hvycsRestraints} "
                          f"atom={atom1} {dstFunc}")

        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by CnsMRParser#proton_shift_statement.
    def enterProton_shift_statement(self, ctx: CnsMRParser.Proton_shift_statementContext):
        if ctx.Potential_types():
            code = str(ctx.Potential_types()).upper()
            if code.startswith('SQUA'):
                self.potential = 'square'
            elif code.startswith('HARM'):
                self.potential = 'harmonic'
            elif code.startswith('MULT'):
                self.potential = 'multiple'
            else:
                self.potential = 'square'
                self.warningMessage += "[Enum mismatch ignorable] "\
                    f"The potential type {str(ctx.Potential_types())!r} is unknown potential type for the 'PROTONshift' statements. "\
                    f"Instead, set the default potential {self.potential!r}.\n"

        elif ctx.Reset():
            self.potential = 'square'
            self.coefficients = None

    # Exit a parse tree produced by CnsMRParser#proton_shift_statement.
    def exitProton_shift_statement(self, ctx: CnsMRParser.Proton_shift_statementContext):  # pylint: disable=unused-argument
        if self.__debug:
            print(f"subtype={self.__cur_subtype} (PROTON) classification={self.classification!r}")

    # Enter a parse tree produced by CnsMRParser#observed.
    def enterObserved(self, ctx: CnsMRParser.ObservedContext):  # pylint: disable=unused-argument
        self.procsRestraints += 1
        self.__cur_subtype = 'procs'

        self.atomSelectionSet.clear()
        self.__warningInAtomSelection = ''

    # Exit a parse tree produced by CnsMRParser#observed.
    def exitObserved(self, ctx: CnsMRParser.ObservedContext):  # pylint: disable=unused-argument

        try:

            if None in self.numberSelection:
                return

            obs_value = self.numberSelection[0]

            obs_value_2 = None
            if len(self.numberSelection) > 1:
                obs_value_2 = self.numberSelection[1]

            if CS_ERROR_MIN < obs_value < CS_ERROR_MAX:
                pass
            else:
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The observed chemical shift value '{obs_value}' must be within range {CS_RESTRAINT_ERROR}.\n"
                return

            if obs_value_2 is not None:
                if CS_ERROR_MIN < obs_value_2 < CS_ERROR_MAX:
                    pass
                else:
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The 2nd observed chemical shift value '{obs_value_2}' must be within range {CS_RESTRAINT_ERROR}.\n"
                    return

            if obs_value_2 is None:
                dstFunc = {'obs_value': obs_value}
            else:
                dstFunc = {'obs_value': obs_value, 'obs_value_2': obs_value_2}

            lenAtomSelectionSet = len(self.atomSelectionSet)

            if obs_value_2 is None and lenAtomSelectionSet == 2:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    "Missing observed chemical shift value for the 2nd atom selection.\n"
                return

            if obs_value_2 is not None and lenAtomSelectionSet == 1:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Missing 2nd atom selection for the observed chemical shift value '{obs_value_2}'.\n"
                return

            for atom1 in self.atomSelectionSet[0]:
                if atom1['atom_id'][0] != 'H':
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"Not a proton; {atom1}.\n"
                return

            if self.__createSfDict:
                sf = self.__getSf()
                sf['id'] += 1

            if lenAtomSelectionSet == 1:
                for atom1 in self.atomSelectionSet[0]:
                    if self.__debug:
                        print(f"subtype={self.__cur_subtype} (PROTON/OBSE) id={self.procsRestraints} "
                              f"atom={atom1} {dstFunc}")
                    if self.__createSfDict and sf is not None:
                        sf['index_id'] += 1
                        row = getRow(self.__cur_subtype, sf['id'], sf['index_id'],
                                     '.', None,
                                     sf['list_id'], self.__entryId, dstFunc, self.__authToStarSeq, atom1)
                        sf['loop'].add_data(row)

            else:
                for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                      self.atomSelectionSet[1]):
                    if self.__debug:
                        print(f"subtype={self.__cur_subtype} (PROTON/OBSE) id={self.procsRestraints} "
                              f"atom1={atom1} atom2={atom2} {dstFunc}")
                    if self.__createSfDict and sf is not None:
                        sf['index_id'] += 1
                        row = getRow(self.__cur_subtype, sf['id'], sf['index_id'],
                                     1, '.',
                                     sf['list_id'], self.__entryId, dstFunc, self.__authToStarSeq, atom1)
                        sf['loop'].add_data(row)
                        #
                        sf['index_id'] += 1
                        row = getRow(self.__cur_subtype, sf['id'], sf['index_id'],
                                     2, '.',
                                     sf['list_id'], self.__entryId, dstFunc, self.__authToStarSeq, None, atom2)
                        sf['loop'].add_data(row)

        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by CnsMRParser#proton_shift_rcoil.
    def enterProton_shift_rcoil(self, ctx: CnsMRParser.Proton_shift_rcoilContext):  # pylint: disable=unused-argument
        self.atomSelectionSet.clear()
        self.__warningInAtomSelection = ''

    # Exit a parse tree produced by CnsMRParser#proton_shift_rcoil.
    def exitProton_shift_rcoil(self, ctx: CnsMRParser.Proton_shift_rcoilContext):  # pylint: disable=unused-argument

        try:

            if None in self.numberSelection:
                return

            rcoil = self.numberSelection[0]

            if CS_ERROR_MIN < rcoil < CS_ERROR_MAX:
                pass
            else:
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"Random coil chemical shift value '{rcoil}' must be within range {CS_RESTRAINT_ERROR}.\n"
                return

            dstFunc = {'rcoil': rcoil}

            for atom1 in self.atomSelectionSet[0]:
                if atom1['atom_id'][0] != 'H':
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"Not a proton; {atom1}.\n"
                    return

            for atom1 in self.atomSelectionSet[0]:
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} (PROTON/RCOI) id={self.procsRestraints} "
                          f"atom={atom1} {dstFunc}")

        finally:
            self.numberSelection.clear()

    # Enter a parse tree produced by CnsMRParser#proton_shift_anisotropy.
    def enterProton_shift_anisotropy(self, ctx: CnsMRParser.Proton_shift_anisotropyContext):  # pylint: disable=unused-argument
        self.atomSelectionSet.clear()
        self.__warningInAtomSelection = ''

    # Exit a parse tree produced by CnsMRParser#proton_shift_anisotropy.
    def exitProton_shift_anisotropy(self, ctx: CnsMRParser.Proton_shift_anisotropyContext):
        co_or_cn = str(ctx.Simple_name(0))
        is_cooh = None
        if ctx.Logical():
            is_cooh = str(ctx.Logical()) in ('TRUE', 'ON')
        sc_or_bb = str(ctx.Simple_name(1))

        if not self.areUniqueCoordAtoms('a proton chemical shift (PROTON/ANIS)'):
            if len(self.__warningInAtomSelection) > 0:
                self.warningMessage += self.__warningInAtomSelection
            return

        dstFunc = {'co_or_cn': co_or_cn.lower(), 'is_cooh': is_cooh, 'sc_or_bb': sc_or_bb.lower()}

        chain_id_1 = self.atomSelectionSet[0][0]['chain_id']
        seq_id_1 = self.atomSelectionSet[0][0]['seq_id']
        atom_id_1 = self.atomSelectionSet[0][0]['atom_id']

        chain_id_2 = self.atomSelectionSet[1][0]['chain_id']
        seq_id_2 = self.atomSelectionSet[1][0]['seq_id']
        atom_id_2 = self.atomSelectionSet[1][0]['atom_id']

        chain_id_3 = self.atomSelectionSet[2][0]['chain_id']
        seq_id_3 = self.atomSelectionSet[2][0]['seq_id']
        atom_id_3 = self.atomSelectionSet[2][0]['atom_id']

        chain_ids = [chain_id_1, chain_id_2, chain_id_3]
        seq_ids = [seq_id_1, seq_id_2, seq_id_3]
        offsets = [seq_id - seq_id_2 for seq_id in seq_ids]
        atom_ids = [atom_id_1, atom_id_2, atom_id_3]

        if chain_ids != [chain_id_1] * 3 or offsets != [0] * 3 or atom_ids != ['CA', 'C', 'O']:
            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                "The atom selection order must be [CA(i), C(i), O(i)].\n"
            return

        for atom1, atom2, atom3 in itertools.product(self.atomSelectionSet[0],
                                                     self.atomSelectionSet[1],
                                                     self.atomSelectionSet[2]):
            if isLongRangeRestraint([atom1, atom2, atom3], self.__polySeq if self.__gapInAuthSeq else None):
                continue
            if self.__debug:
                print(f"subtype={self.__cur_subtype} (PROTON/ANIS) id={self.procsRestraints} "
                      f"atom1={atom1} atom2={atom2} atom3={atom3} {dstFunc}")

    # Enter a parse tree produced by CnsMRParser#proton_shift_amides.
    def enterProton_shift_amides(self, ctx: CnsMRParser.Proton_shift_amidesContext):  # pylint: disable=unused-argument
        self.atomSelectionSet.clear()
        self.__warningInAtomSelection = ''

    # Exit a parse tree produced by CnsMRParser#proton_shift_amides.
    def exitProton_shift_amides(self, ctx: CnsMRParser.Proton_shift_amidesContext):  # pylint: disable=unused-argument
        for atom1 in self.atomSelectionSet[0]:
            if atom1['atom_id'] != 'H':
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Not a backbone amide proton; {atom1}.\n"
                return

        for atom1 in self.atomSelectionSet[0]:
            print(f"subtype={self.__cur_subtype} (PROTON/AMID) id={self.procsRestraints} "
                  f"atom={atom1}")

    # Enter a parse tree produced by CnsMRParser#proton_shift_carbons.
    def enterProton_shift_carbons(self, ctx: CnsMRParser.Proton_shift_carbonsContext):  # pylint: disable=unused-argument
        self.atomSelectionSet.clear()
        self.__warningInAtomSelection = ''

    # Exit a parse tree produced by CnsMRParser#proton_shift_carbons.
    def exitProton_shift_carbons(self, ctx: CnsMRParser.Proton_shift_carbonsContext):  # pylint: disable=unused-argument
        for atom1 in self.atomSelectionSet[0]:
            if atom1['atom_id'] != 'C':
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Not a backbone carbonyl carbon; {atom1}.\n"
                return

        for atom1 in self.atomSelectionSet[0]:
            print(f"subtype={self.__cur_subtype} (PROTON/CARB) id={self.procsRestraints} "
                  f"atom={atom1}")

    # Enter a parse tree produced by CnsMRParser#proton_shift_nitrogens.
    def enterProton_shift_nitrogens(self, ctx: CnsMRParser.Proton_shift_nitrogensContext):  # pylint: disable=unused-argument
        self.atomSelectionSet.clear()
        self.__warningInAtomSelection = ''

    # Exit a parse tree produced by CnsMRParser#proton_shift_nitrogens.
    def exitProton_shift_nitrogens(self, ctx: CnsMRParser.Proton_shift_nitrogensContext):  # pylint: disable=unused-argument
        for atom1 in self.atomSelectionSet[0]:
            if atom1['atom_id'] != 'N':
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Not a backbone nitrogen; {atom1}.\n"
                return

        for atom1 in self.atomSelectionSet[0]:
            print(f"subtype={self.__cur_subtype} (PROTON/NITR) id={self.procsRestraints} "
                  f"atom={atom1}")

    # Enter a parse tree produced by CnsMRParser#proton_shift_oxygens.
    def enterProton_shift_oxygens(self, ctx: CnsMRParser.Proton_shift_oxygensContext):  # pylint: disable=unused-argument
        self.atomSelectionSet.clear()
        self.__warningInAtomSelection = ''

    # Exit a parse tree produced by CnsMRParser#proton_shift_oxygens.
    def exitProton_shift_oxygens(self, ctx: CnsMRParser.Proton_shift_oxygensContext):  # pylint: disable=unused-argument
        for atom1 in self.atomSelectionSet[0]:
            if atom1['atom_id'] != 'O':
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Not a backbone oxygen; {atom1}.\n"
                return

        for atom1 in self.atomSelectionSet[0]:
            print(f"subtype={self.__cur_subtype} (PROTON/OXYG) id={self.procsRestraints} "
                  f"atom={atom1}")

    # Enter a parse tree produced by CnsMRParser#proton_shift_ring_atoms.
    def enterProton_shift_ring_atoms(self, ctx: CnsMRParser.Proton_shift_ring_atomsContext):  # pylint: disable=unused-argument
        self.atomSelectionSet.clear()
        self.__warningInAtomSelection = ''

    # Exit a parse tree produced by CnsMRParser#proton_shift_ring_atoms.
    def exitProton_shift_ring_atoms(self, ctx: CnsMRParser.Proton_shift_ring_atomsContext):
        ring_name = str(ctx.Simple_name())

        ringNames = ('PHE', 'TYR', 'HIS', 'TRP5', 'TRP6', 'ADE6', 'ADE5', 'GUA6', 'GUA5', 'THY', 'CYT', 'URA')

        if ring_name not in ringNames:
            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                f"{ring_name!r} must be one of {ringNames}.\n"
            return

        if not self.areUniqueCoordAtoms('a proton chemical shift (PROTON/RING)'):
            if len(self.__warningInAtomSelection) > 0:
                self.warningMessage += self.__warningInAtomSelection
            return

        if len(self.atomSelectionSet) == 5:
            for atom1, atom2, atom3, atom4, atom5 in itertools.product(self.atomSelectionSet[0],
                                                                       self.atomSelectionSet[1],
                                                                       self.atomSelectionSet[2],
                                                                       self.atomSelectionSet[3],
                                                                       self.atomSelectionSet[4]):
                if isLongRangeRestraint([atom1, atom2, atom3, atom4, atom5], self.__polySeq if self.__gapInAuthSeq else None):
                    continue
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} (PROTON/RING) id={self.procsRestraints} "
                          f"ring_name={ring_name} atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} atom5={atom5}")

        else:
            for atom1, atom2, atom3, atom4, atom5, atom6 in itertools.product(self.atomSelectionSet[0],
                                                                              self.atomSelectionSet[1],
                                                                              self.atomSelectionSet[2],
                                                                              self.atomSelectionSet[3],
                                                                              self.atomSelectionSet[4],
                                                                              self.atomSelectionSet[5]):
                if isLongRangeRestraint([atom1, atom2, atom3, atom4, atom5, atom6], self.__polySeq if self.__gapInAuthSeq else None):
                    continue
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} (PROTON/RING) id={self.procsRestraints} "
                          f"ring_name={ring_name} atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} atom5={atom5} atom6={atom6}")

    # Enter a parse tree produced by CnsMRParser#proton_shift_alphas_and_amides.
    def enterProton_shift_alphas_and_amides(self, ctx: CnsMRParser.Proton_shift_alphas_and_amidesContext):  # pylint: disable=unused-argument
        self.atomSelectionSet.clear()
        self.__warningInAtomSelection = ''

    # Exit a parse tree produced by CnsMRParser#proton_shift_alphas_and_amides.
    def exitProton_shift_alphas_and_amides(self, ctx: CnsMRParser.Proton_shift_alphas_and_amidesContext):  # pylint: disable=unused-argument
        for atom1 in self.atomSelectionSet[0]:
            if atom1['atom_id'] == 'H' or atom1['atom_id'].startswith('HA'):
                pass
            else:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Neither alpha protons nor amide proton; {atom1}.\n"
                return

        for atom1 in self.atomSelectionSet[0]:
            print(f"subtype={self.__cur_subtype} (PROTON/ALPH) id={self.procsRestraints} "
                  f"atom={atom1}")

    # Enter a parse tree produced by CnsMRParser#conformation_statement.
    def enterConformation_statement(self, ctx: CnsMRParser.Conformation_statementContext):
        if ctx.Error():
            self.ramaError = self.getNumber_s(ctx.number_s())
            if isinstance(self.ramaError, str):
                if self.ramaError in self.evaluate:
                    self.ramaError = self.evaluate[self.ramaError]
                else:
                    self.warningMessage += "[Unsupported data] "\
                        f"The error value 'CONF {str(ctx.Error())} {self.ramaError} END'"

        elif ctx.ForceConstant():
            self.ramaForceConst = self.getNumber_s(ctx.number_s())

        elif ctx.Potential_types():
            code = str(ctx.Potential_types()).upper()
            if code.startswith('SQUA'):
                self.ramaPotential = 'square'
            elif code.startswith('HARM'):
                self.ramaPotential = 'harmonic'
            else:
                self.ramaPotential = 'square'
                self.warningMessage += "[Enum mismatch ignorable] "\
                    f"The potential type {str(ctx.Potential_types())!r} is unknown potential type for the 'CONFormation' statements. "\
                    f"Instead, set the default potential {self.ramaPotential!r}.\n"

        elif ctx.Size():
            self.ramaSize = []
            dim = str(ctx.Dimensions()).lower()
            self.ramaSize.append(int(str(ctx.Integer(0))))
            if dim in ('twod', 'threed', 'fourd'):
                self.ramaSize.append(int(str(ctx.Integer(1))))
            if dim in ('threed', 'fourd'):
                self.ramaSize.append(int(str(ctx.Integer(2))))
            if dim == 'fourd':
                self.ramaSize.append(int(str(ctx.Integer(3))))

        elif ctx.Phase():
            self.ramaPhase = []
            for d in range(4):
                offset = d * 3
                if ctx.Integer(offset):
                    phase = []
                    for i in range(3):
                        if ctx.Integer(offset + i):
                            phase.append(int(str(ctx.Integer(offset + i))))
                        else:
                            break
                    self.ramaPhase.append(phase)
                else:
                    break

        elif ctx.Expectation():
            self.ramaExpectValue = self.getNumber_s(ctx.number_s())

            self.ramaExpectGrid = []
            for d in range(4):
                if ctx.Integer(d):
                    self.ramaExpectGrid.append(int(str(ctx.Integer(d))))
                else:
                    break

        elif ctx.Reset():
            self.ramaError = None
            self.ramaForceConst = 1.0
            self.ramaPotential = 'square'
            self.ramaSize = None
            self.ramaPhase = None
            self.ramaExpectGrid = None
            self.ramaExpectValue = None

        elif ctx.Zero():
            self.ramaExpectGrid = None
            self.ramaExpectValue = None

    # Exit a parse tree produced by CnsMRParser#conformation_statement.
    def exitConformation_statement(self, ctx: CnsMRParser.Conformation_statementContext):  # pylint: disable=unused-argument
        if self.__debug:
            print(f"subtype={self.__cur_subtype} (CONF) classification={self.classification!r} "
                  f"error={self.ramaError} force_constant={self.ramaForceConst} potential={self.ramaPotential} "
                  f"size={self.ramaSize} phase={self.ramaSize} expectation={self.ramaExpectGrid} {self.ramaExpectValue}")

    # Enter a parse tree produced by CnsMRParser#conf_assign.
    def enterConf_assign(self, ctx: CnsMRParser.Conf_assignContext):  # pylint: disable=unused-argument
        self.ramaRestraints += 1
        self.__cur_subtype = 'rama'

        self.atomSelectionSet.clear()
        self.__warningInAtomSelection = ''

    # Exit a parse tree produced by CnsMRParser#conf_assign.
    def exitConf_assign(self, ctx: CnsMRParser.Conf_assignContext):  # pylint: disable=unused-argument
        if not self.__hasPolySeq:
            return

        if not self.areUniqueCoordAtoms('a conformation database (CONF)'):
            if len(self.__warningInAtomSelection) > 0:
                self.warningMessage += self.__warningInAtomSelection
            return

        for i in range(0, len(self.atomSelectionSet), 2):
            chain_id_1 = self.atomSelectionSet[i][0]['chain_id']
            seq_id_1 = self.atomSelectionSet[i][0]['seq_id']
            comp_id_1 = self.atomSelectionSet[i][0]['comp_id']
            atom_id_1 = self.atomSelectionSet[i][0]['atom_id']

            chain_id_2 = self.atomSelectionSet[i + 1][0]['chain_id']
            seq_id_2 = self.atomSelectionSet[i + 1][0]['seq_id']
            comp_id_2 = self.atomSelectionSet[i + 1][0]['comp_id']
            atom_id_2 = self.atomSelectionSet[i + 1][0]['atom_id']

            if (atom_id_1[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS) or (atom_id_2[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS):
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Non-magnetic susceptible spin appears in dihedral angle vector; "\
                    f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                    f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                return

            if chain_id_1 != chain_id_2:
                ps1 = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chain_id_1 and 'identical_auth_chain_id' in ps), None)
                ps2 = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chain_id_2 and 'identical_auth_chain_id' in ps), None)
                if ps1 is None and ps2 is None:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"Found inter-chain dihedral angle vector; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                    return

            elif abs(seq_id_1 - seq_id_2) > 1:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Found inter-residue dihedral angle vector; "\
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
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        "Found inter-residue dihedral angle vector; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                    return

            elif atom_id_1 == atom_id_2:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    "Found zero dihedral angle vector; "\
                    f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                return

            elif self.__ccU.updateChemCompDict(comp_id_1):  # matches with comp_id in CCD

                if not any(b for b in self.__ccU.lastBonds
                           if ((b[self.__ccU.ccbAtomId1] == atom_id_1 and b[self.__ccU.ccbAtomId2] == atom_id_2)
                               or (b[self.__ccU.ccbAtomId1] == atom_id_2 and b[self.__ccU.ccbAtomId2] == atom_id_1))):

                    if self.__nefT.validate_comp_atom(comp_id_1, atom_id_1) and self.__nefT.validate_comp_atom(comp_id_2, atom_id_2):
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            "Found an dihedral angle vector over multiple covalent bonds in the 'CONFormation' statement; "\
                            f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                        return

        if self.__createSfDict:
            sf = self.__getSf('dihedral angle database restraint, CNS CONFormation statement')
            sf['id'] += 1
            if len(sf['loop']['tags']) == 0:
                sf['loop']['tags'] = ['index_id', 'id', 'combination_id',
                                      'auth_asym_id_1', 'auth_seq_id_1', 'auth_comp_id_1', 'auth_atom_id_1',
                                      'auth_asym_id_2', 'auth_seq_id_2', 'auth_comp_id_2', 'auth_atom_id_2',
                                      'auth_asym_id_3', 'auth_seq_id_3', 'auth_comp_id_3', 'auth_atom_id_3',
                                      'auth_asym_id_4', 'auth_seq_id_4', 'auth_comp_id_4', 'auth_atom_id_4',
                                      'list_id', 'entry_id']
                sf['tags'].append(['classification', self.classification])
                sf['tags'].append(['error', self.ramaError])
                sf['tags'].append(['force_constant', self.ramaForceConst])
                sf['tags'].append(['potential', self.ramaPotential])
                sf['tags'].append(['size', self.ramaSize])
                sf['tags'].append(['phase', self.ramaPhase])
                sf['tags'].append(['expect_grid', self.ramaExpectGrid])
                sf['tags'].append(['expect_value', self.ramaExpectValue])

        for i in range(0, len(self.atomSelectionSet), 4):
            for atom1, atom2, atom3, atom4 in itertools.product(self.atomSelectionSet[i],
                                                                self.atomSelectionSet[i + 1],
                                                                self.atomSelectionSet[i + 2],
                                                                self.atomSelectionSet[i + 3]):
                if isLongRangeRestraint([atom1, atom2, atom3, atom4], self.__polySeq if self.__gapInAuthSeq else None):
                    continue
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} (CONF) id={self.ramaRestraints} "
                          f"atom{i+1}={atom1} atom{i+2}={atom2} atom{i+3}={atom3} atom{i+4}={atom4}")
                if self.__createSfDict and sf is not None:
                    sf['index_id'] += 1
                    sf['loop']['data'].append([sf['index_id'], sf['id'], '.' if len(self.atomSelectionSet) == 4 else (i + 1),
                                               atom1['chain_id'], atom1['seq_id'], atom1['comp_id'], atom1['atom_id'],
                                               atom2['chain_id'], atom2['seq_id'], atom2['comp_id'], atom2['atom_id'],
                                               atom3['chain_id'], atom3['seq_id'], atom3['comp_id'], atom3['atom_id'],
                                               atom4['chain_id'], atom4['seq_id'], atom4['comp_id'], atom4['atom_id'],
                                               sf['list_id'], self.__entryId])

    # Enter a parse tree produced by CnsMRParser#diffusion_statement.
    def enterDiffusion_statement(self, ctx: CnsMRParser.Diffusion_statementContext):
        if ctx.Coefficients():
            self.diffCoef = {'Tc': self.getNumber_s(ctx.number_s(0)),
                             'anisotropy': self.getNumber_s(ctx.number_s(1)),
                             'rhombicity': self.getNumber_s(ctx.number_s(2)),
                             'frequency_1h': self.getNumber_s(ctx.number_s(3)),
                             'frequency_15n': self.getNumber_s(ctx.number_s(4))
                             }

        elif ctx.ForceConstant():
            self.diffForceConst = self.getNumber_s(ctx.number_s(0))

        elif ctx.Potential_types():
            code = str(ctx.Potential_types()).upper()
            if code.startswith('SQUA'):
                self.diffPotential = 'square'
            elif code.startswith('HARM'):
                self.diffPotential = 'harmonic'
            else:
                self.diffPotential = 'square'
                self.warningMessage += "[Enum mismatch ignorable] "\
                    f"The potential type {str(ctx.Potential_types())!r} is unknown potential type for the 'DANIsotropy' statements. "\
                    f"Instead, set the default potential {self.diffPotential!r}.\n"

        elif ctx.Reset():
            self.diffCoef = None
            self.diffForceConst = 1.0
            self.diffPotential = 'square'

    # Exit a parse tree produced by CnsMRParser#diffusion_statement.
    def exitDiffusion_statement(self, ctx: CnsMRParser.Diffusion_statementContext):  # pylint: disable=unused-argument
        if self.__debug:
            print(f"subtype={self.__cur_subtype} (DANI) classification={self.classification!r} "
                  f"coefficients={self.diffCoef} force_constant={self.diffForceConst} "
                  f"potential={self.diffPotential}")

    # Enter a parse tree produced by CnsMRParser#dani_assign.
    def enterDani_assign(self, ctx: CnsMRParser.Dani_assignContext):  # pylint: disable=unused-argument
        self.diffRestraints += 1
        self.__cur_subtype = 'diff'

        self.atomSelectionSet.clear()
        self.__warningInAtomSelection = ''

    # Exit a parse tree produced by CnsMRParser#dani_assign.
    def exitDani_assign(self, ctx: CnsMRParser.Dani_assignContext):  # pylint: disable=unused-argument

        try:

            if None in self.numberSelection:
                return

            target = self.numberSelection[0]

            if len(self.numberSelection) > 1:
                delta = abs(self.numberSelection[1])
            else:
                delta = 0.0

            target_value = target
            lower_limit = None
            upper_limit = None

            if self.potential == 'square' and delta > 0.0:
                lower_limit = target - delta
                upper_limit = target + delta

            dstFunc = self.validateT1T2Range(1.0,
                                             target_value, lower_limit, upper_limit)

            if dstFunc is None:
                return

            if not self.__hasPolySeq:
                return

            if not self.areUniqueCoordAtoms('a diffusion anisotropy (DANI)', XPLOR_ORIGIN_AXIS_COLS):
                if len(self.__warningInAtomSelection) > 0:
                    self.warningMessage += self.__warningInAtomSelection
                return

            chain_id_1 = self.atomSelectionSet[4][0]['chain_id']
            seq_id_1 = self.atomSelectionSet[4][0]['seq_id']
            comp_id_1 = self.atomSelectionSet[4][0]['comp_id']
            atom_id_1 = self.atomSelectionSet[4][0]['atom_id']

            chain_id_2 = self.atomSelectionSet[5][0]['chain_id']
            seq_id_2 = self.atomSelectionSet[5][0]['seq_id']
            comp_id_2 = self.atomSelectionSet[5][0]['comp_id']
            atom_id_2 = self.atomSelectionSet[5][0]['atom_id']

            if (atom_id_1[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS) or (atom_id_2[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS):
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Non-magnetic susceptible spin appears in diffusion anisotropy vector; "\
                    f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                    f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                return

            if chain_id_1 != chain_id_2:
                ps1 = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chain_id_1 and 'identical_auth_chain_id' in ps), None)
                ps2 = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chain_id_2 and 'identical_auth_chain_id' in ps), None)
                if ps1 is None and ps2 is None:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        f"Found inter-chain diffusion anisotropy vector; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                    return

            elif abs(seq_id_1 - seq_id_2) > 1:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"Found inter-residue diffusion anisotropy vector; "\
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
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        "Found inter-residue diffusion anisotropy vector; "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                    return

            elif atom_id_1 == atom_id_2:
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    "Found zero diffusion anisotropy vector; "\
                    f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                return

            elif self.__ccU.updateChemCompDict(comp_id_1):  # matches with comp_id in CCD

                if not any(b for b in self.__ccU.lastBonds
                           if ((b[self.__ccU.ccbAtomId1] == atom_id_1 and b[self.__ccU.ccbAtomId2] == atom_id_2)
                               or (b[self.__ccU.ccbAtomId1] == atom_id_2 and b[self.__ccU.ccbAtomId2] == atom_id_1))):

                    if self.__nefT.validate_comp_atom(comp_id_1, atom_id_1) and self.__nefT.validate_comp_atom(comp_id_2, atom_id_2):
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            "Found a diffusion anisotropy vector over multiple covalent bonds in the 'DANIsotropy' statement; "\
                            f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).\n"
                        return

            if self.__createSfDict:
                sf = self.__getSf('diffusion anisotropy restraint, CNS DANIsotropy statement')
                sf['id'] += 1
                if len(sf['loop']['tags']) == 0:
                    sf['loop']['tags'] = ['index_id', 'id',
                                          'auth_asym_id_1', 'auth_seq_id_1', 'auth_comp_id_1', 'auth_atom_id_1',
                                          'auth_asym_id_2', 'auth_seq_id_2', 'auth_comp_id_2', 'auth_atom_id_2',
                                          't1/t2_ratio', 't1/t2_ratio_err'
                                          'list_id', 'entry_id']
                    sf['tags'].append(['classification', self.classification])
                    sf['tags'].append(['coefficients', self.diffCoef])
                    sf['tags'].append(['force_constant', self.diffForceConst])
                    sf['tags'].append(['potential', self.diffPotential])

            for atom1, atom2 in itertools.product(self.atomSelectionSet[4],
                                                  self.atomSelectionSet[5]):
                if isLongRangeRestraint([atom1, atom2], self.__polySeq if self.__gapInAuthSeq else None):
                    continue
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} (DANI) id={self.diffRestraints} "
                          f"atom1={atom1} atom2={atom2} {dstFunc}")
                if self.__createSfDict and sf is not None:
                    sf['index_id'] += 1
                    sf['loop']['data'].append([sf['index_id'], sf['id'],
                                               atom1['chain_id'], atom1['seq_id'], atom1['comp_id'], atom1['atom_id'],
                                               atom2['chain_id'], atom2['seq_id'], atom2['comp_id'], atom2['atom_id'],
                                               target, delta,
                                               sf['list_id'], self.__entryId])

        finally:
            self.numberSelection.clear()

    def validateT1T2Range(self, weight,
                          target_value, lower_limit, upper_limit,
                          lower_linear_limit=None, upper_linear_limit=None):
        """ Validate T1/T2 value range.
        """

        validRange = True
        dstFunc = {'weight': weight, 'potential': self.potential}

        if target_value is not None:
            if T1T2_ERROR_MIN < target_value < T1T2_ERROR_MAX:
                dstFunc['target_value'] = f"{target_value}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The target value='{target_value}' must be within range {T1T2_RESTRAINT_ERROR}.\n"

        if lower_limit is not None:
            if T1T2_ERROR_MIN <= lower_limit < T1T2_ERROR_MAX:
                dstFunc['lower_limit'] = f"{lower_limit:.6f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower limit value='{lower_limit:.6f}' must be within range {T1T2_RESTRAINT_ERROR}.\n"

        if upper_limit is not None:
            if T1T2_ERROR_MIN < upper_limit <= T1T2_ERROR_MAX:
                dstFunc['upper_limit'] = f"{upper_limit:.6f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit:.6f}' must be within range {T1T2_RESTRAINT_ERROR}.\n"

        if lower_linear_limit is not None:
            if T1T2_ERROR_MIN <= lower_linear_limit < T1T2_ERROR_MAX:
                dstFunc['lower_linear_limit'] = f"{lower_linear_limit:.6f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower linear limit value='{lower_linear_limit:.6f}' must be within range {T1T2_RESTRAINT_ERROR}.\n"

        if upper_linear_limit is not None:
            if T1T2_ERROR_MIN < upper_linear_limit <= T1T2_ERROR_MAX:
                dstFunc['upper_linear_limit'] = f"{upper_linear_limit:.6f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper linear limit value='{upper_linear_limit:.6f}' must be within range {T1T2_RESTRAINT_ERROR}.\n"

        if target_value is not None:

            if lower_limit is not None:
                if lower_limit > target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower limit value='{lower_limit:.6f}' must be less than the target value '{target_value}'.\n"

            if lower_linear_limit is not None:
                if lower_linear_limit > target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower linear limit value='{lower_linear_limit:.6f}' must be less than the target value '{target_value}'.\n"

            if upper_limit is not None:
                if upper_limit < target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The upper limit value='{upper_limit:.6f}' must be greater than the target value '{target_value}'.\n"

            if upper_linear_limit is not None:
                if upper_linear_limit < target_value:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The upper linear limit value='{upper_linear_limit:.6f}' must be greater than the target value '{target_value}'.\n"

        else:

            if lower_limit is not None and upper_limit is not None:
                if lower_limit > upper_limit:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower limit value='{lower_limit:.6f}' must be less than the upper limit value '{upper_limit:.6f}'.\n"

            if lower_linear_limit is not None and upper_limit is not None:
                if lower_linear_limit > upper_limit:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower linear limit value='{lower_linear_limit:.6f}' must be less than the upper limit value '{upper_limit:.6f}'.\n"

            if lower_limit is not None and upper_linear_limit is not None:
                if lower_limit > upper_linear_limit:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower limit value='{lower_limit:.6f}' must be less than the upper limit value '{upper_linear_limit:.6f}'.\n"

            if lower_linear_limit is not None and upper_linear_limit is not None:
                if lower_linear_limit > upper_linear_limit:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower linear limit value='{lower_linear_limit:.6f}' must be less than the upper limit value '{upper_linear_limit:.6f}'.\n"

            if lower_limit is not None and lower_linear_limit is not None:
                if lower_linear_limit > lower_limit:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The lower linear limit value='{lower_linear_limit:.6f}' must be less than the lower limit value '{lower_limit:.6f}'.\n"

            if upper_limit is not None and upper_linear_limit is not None:
                if upper_limit > upper_linear_limit:
                    validRange = False
                    self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                        f"The upper limit value='{upper_limit:.6f}' must be less than the upper linear limit value '{upper_linear_limit:.6f}'.\n"

        if not validRange:
            return None

        if target_value is not None:
            if T1T2_RANGE_MIN <= target_value <= T1T2_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The target value='{target_value}' should be within range {T1T2_RESTRAINT_RANGE}.\n"

        if lower_limit is not None:
            if T1T2_RANGE_MIN <= lower_limit <= T1T2_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The lower limit value='{lower_limit:.6f}' should be within range {T1T2_RESTRAINT_RANGE}.\n"

        if upper_limit is not None:
            if T1T2_RANGE_MIN <= upper_limit <= T1T2_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit:.6f}' should be within range {T1T2_RESTRAINT_RANGE}.\n"

        if lower_linear_limit is not None:
            if T1T2_RANGE_MIN <= lower_linear_limit <= T1T2_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The lower linear limit value='{lower_linear_limit:.6f}' should be within range {T1T2_RESTRAINT_RANGE}.\n"

        if upper_linear_limit is not None:
            if T1T2_RANGE_MIN <= upper_linear_limit <= T1T2_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The upper linear limit value='{upper_linear_limit:.6f}' should be within range {T1T2_RESTRAINT_RANGE}.\n"

        return dstFunc

    # Enter a parse tree produced by CnsMRParser#one_bond_coupling_statement.
    def enterOne_bond_coupling_statement(self, ctx: CnsMRParser.One_bond_coupling_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#one_bond_coupling_statement.
    def exitOne_bond_coupling_statement(self, ctx: CnsMRParser.One_bond_coupling_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#one_bond_assign.
    def enterOne_bond_assign(self, ctx: CnsMRParser.One_bond_assignContext):  # pylint: disable=unused-argument
        """
        @deprecated: This restraint has not been useful in practice, but has been preserved for historical reasons.
        """

    # Exit a parse tree produced by CnsMRParser#one_bond_assign.
    def exitOne_bond_assign(self, ctx: CnsMRParser.One_bond_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#angle_db_statement.
    def enterAngle_db_statement(self, ctx: CnsMRParser.Angle_db_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#angle_db_statement.
    def exitAngle_db_statement(self, ctx: CnsMRParser.Angle_db_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#angle_db_assign.
    def enterAngle_db_assign(self, ctx: CnsMRParser.Angle_db_assignContext):  # pylint: disable=unused-argument
        """
        @deprecated:  This term has not proved useful in practice and is only here for historical reasons.
        """

    # Exit a parse tree produced by CnsMRParser#angle_db_assign.
    def exitAngle_db_assign(self, ctx: CnsMRParser.Angle_db_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#ncs_restraint.
    def enterNcs_restraint(self, ctx: CnsMRParser.Ncs_restraintContext):  # pylint: disable=unused-argument
        self.geoStatements += 1
        self.__cur_subtype = 'geo'

        if self.__createSfDict:
            self.__addSf('NCS restraint, CNS NCS/GROUP statement')

    # Exit a parse tree produced by CnsMRParser#ncs_restraint.
    def exitNcs_restraint(self, ctx: CnsMRParser.Ncs_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#ncs_statement.
    def enterNcs_statement(self, ctx: CnsMRParser.Ncs_statementContext):
        if ctx.Initialize():
            self.ncsSigb = 2.0
            self.ncsWeight = 300.0

    # Exit a parse tree produced by CnsMRParser#ncs_statement.
    def exitNcs_statement(self, ctx: CnsMRParser.Ncs_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#ncs_group_statement.
    def enterNcs_group_statement(self, ctx: CnsMRParser.Ncs_group_statementContext):
        self.geoRestraints += 1
        if self.__cur_subtype != 'geo':
            self.geoStatements += 1
        self.__cur_subtype = 'geo'

        self.atomSelectionSet.clear()
        self.__warningInAtomSelection = ''

        if ctx.Sigb():
            self.ncsSigb = self.getNumber_s(ctx.number_s())
            if isinstance(self.ncsSigb, str):
                if self.ncsSigb in self.evaluate:
                    self.ncsSigb = self.evaluate[self.ncsSigb]
                else:
                    self.warningMessage += "[Unsupported data] "\
                        f"The B-factor value 'GROUP {str(ctx.Sigb())}={self.ncsSigb} END' "\
                        f"where the symbol {self.ncsSigb!r} is not defined so that set the default value.\n"
                    self.ncsSigb = 2.0
            if self.ncsSigb <= 0.0:
                self.warningMessage += "[Invalid data] "\
                    f"The B-factor value 'GROUP {str(ctx.Sigb())}={self.ncsSigb} END' must be a positive value.\n"

        elif ctx.Weight():
            self.ncsWeight = self.getNumber_s(ctx.number_s())
            if isinstance(self.ncsWeight, str):
                if self.ncsWeight in self.evaluate:
                    self.ncsWeight = self.evaluate[self.ncsWeight]
                else:
                    self.warningMessage += "[Unsupported data] "\
                        f"The weight value 'GROUP {str(ctx.Weight())}={self.ncsWeight} END' "\
                        f"where the symbol {self.ncsWeight!r} is not defined so that set the default value.\n"
                    self.ncsWeight = 300.0
            if self.ncsWeight < 0.0:
                self.warningMessage += "[Invalid data] "\
                    f"The weight value 'GROUP {str(ctx.Weight())}={self.ncsWeight} END' must not be a negative value.\n"
            elif self.ncsWeight == 0.0:
                self.warningMessage += "[Range value warning] "\
                    f"The weight value 'GROUP {str(ctx.Weight())}={self.ncsWeight} END' should be a positive value.\n"

    # Exit a parse tree produced by CnsMRParser#ncs_group_statement.
    def exitNcs_group_statement(self, ctx: CnsMRParser.Ncs_group_statementContext):  # pylint: disable=unused-argument
        if not self.__hasPolySeq:
            return

        if len(self.atomSelectionSet) == 0:
            return

        if self.__createSfDict:
            sf = self.__getSf('NCS restraint, CNS NCS/GROUP statement')
            sf['id'] += 1
            if len(sf['loop']['tags']) == 0:
                sf['loop']['tags'] = ['index_id', 'id',
                                      'auth_asym_id', 'auth_seq_id', 'auth_comp_id', 'auth_atom_id',
                                      'list_id', 'entry_id']
                sf['tags'].append(['sigma_b', self.ncsSigb])
                sf['tags'].append(['weight', self.ncsWeight])

        for atom1 in self.atomSelectionSet[0]:
            if atom1['atom_id'] == 'H':
                continue
            if self.__debug:
                print(f"subtype={self.__cur_subtype} (NCS/GROUP) id={self.geoRestraints} "
                      f"atom={atom1} sigb={self.ncsSigb} weight={self.ncsWeight}")
            if self.__createSfDict and sf is not None:
                sf['index_id'] += 1
                sf['loop']['data'].append([sf['index_id'], sf['id'],
                                           atom1['chain_id'], atom1['seq_id'], atom1['comp_id'], atom1['atom_id'],
                                           sf['list_id'], self.__entryId])

    # Enter a parse tree produced by CnsMRParser#selection.
    def enterSelection(self, ctx: CnsMRParser.SelectionContext):  # pylint: disable=unused-argument
        if self.__sel_expr_debug:
            print("  " * self.depth + "enter_selection")

        if self.inVector3D:
            self.inVector3D_columnSel += 1

        elif self.depth == 0:
            self.stackSelections = []
            self.stackTerms = []
            self.factor = {}

    # Exit a parse tree produced by CnsMRParser#selection.
    def exitSelection(self, ctx: CnsMRParser.SelectionContext):  # pylint: disable=unused-argument
        if self.__sel_expr_debug:
            print("  " * self.depth + "exit_selection")

        if 'and' not in self.stackSelections:

            atomSelection = self.stackSelections.pop() if self.stackSelections else []

            while self.stackSelections:
                _selection = self.stackSelections.pop()
                if _selection is not None:
                    if self.depth > 0:
                        for _atom in _selection:
                            if _atom not in atomSelection:
                                atomSelection.append(_atom)
                    else:
                        atomSelection = self.__intersectionAtom_selections(_selection, atomSelection)

        else:

            blockSelections = []
            blockSelections.append(None)
            blockId = 0

            for _selection in self.stackSelections:

                if _selection is None:
                    continue

                if isinstance(_selection, str) and _selection == 'and':
                    blockSelections.append(None)
                    blockId += 1
                    continue

                if blockSelections[blockId] is None:
                    blockSelections[blockId] = _selection

                else:
                    for _atom in _selection:
                        if _atom not in blockSelections[blockId]:
                            blockSelections[blockId].append(_atom)

            self.stackSelections.clear()

            atomSelection = blockSelections.pop()

            while blockSelections:
                atomSelection = self.__intersectionAtom_selections(blockSelections.pop(), atomSelection)

        while self.stackSelections:
            _selection = self.stackSelections.pop()
            if _selection is not None:
                for _atom in _selection:
                    if _atom not in atomSelection:
                        atomSelection.append(_atom)

        if '*' in atomSelection:
            atomSelection.remove('*')

        if self.__createSfDict:
            atomSelection = sorted(atomSelection, key=lambda x: (x['chain_id'], x['seq_id'], x['atom_id']))

        if self.__sel_expr_debug:
            print("  " * self.depth + f"atom selection: {atomSelection}")

        if self.inVector3D:
            if self.inVector3D_columnSel == 0:
                self.inVector3D_tail = atomSelection[0]
                if len(atomSelection) > 1:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        "Ambiguous atoms have been selected to create a 3d-vector in the 'tail' clause.\n"
            else:
                self.inVector3D_head = atomSelection[0]
                if len(atomSelection) > 1:
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        "Ambiguous atoms have been selected to create a 3d-vector in the 'head' clause.\n"

        else:
            self.atomSelectionSet.append(atomSelection)

    # Enter a parse tree produced by CnsMRParser#selection_expression.
    def enterSelection_expression(self, ctx: CnsMRParser.Selection_expressionContext):
        if self.__sel_expr_debug:
            print("  " * self.depth + f"enter_sel_expr, union: {bool(ctx.Or_op(0))}")

        if self.depth > 0 and len(self.factor) > 0:
            if 'atom_selection' not in self.factor:
                self.consumeFactor_expressions(cifCheck=True)
            if 'atom_selection' in self.factor:
                self.stackSelections.append(self.factor['atom_selection'])
                self.stackSelections.append('and')  # intersection

        self.factor = {}

        self.depth += 1

    # Exit a parse tree produced by CnsMRParser#selection_expression.
    def exitSelection_expression(self, ctx: CnsMRParser.Selection_expressionContext):  # pylint: disable=unused-argument
        self.depth -= 1
        if self.__sel_expr_debug:
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

    # Enter a parse tree produced by CnsMRParser#term.
    def enterTerm(self, ctx: CnsMRParser.TermContext):
        if self.__sel_expr_debug:
            print("  " * self.depth + f"enter_term, intersection: {bool(ctx.And_op(0))}")

        self.stackFactors = []
        self.factor = {}

        self.depth += 1

    # Exit a parse tree produced by CnsMRParser#term.
    def exitTerm(self, ctx: CnsMRParser.TermContext):  # pylint: disable=unused-argument
        self.depth -= 1
        if self.__sel_expr_debug:
            print("  " * self.depth + "exit_term")

        while self.stackFactors:
            _factor = self.__consumeFactor_expressions(self.stackFactors.pop(), cifCheck=True)
            self.factor = self.__intersectionFactor_expressions(self.factor, None if 'atom_selection' not in _factor else _factor['atom_selection'])

        if 'atom_selection' in self.factor:
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

        if not any(key for key in _factor if not(key == 'atom_selection' or key.startswith('auth'))):
            return _factor

        if len(_factor) == 2 and 'chain_id' in _factor and len(_factor['chain_id']) == 0 and 'alt_chain_id' in _factor:
            if self.__largeModel:
                _factor['chain_id'] = [self.__representativeAsymId]
            else:
                _factor['atom_selection'] = ['*']
                del _factor['chain_id']
                return _factor

        if len(self.atomSelectionSet) == 0:
            self.__retrieveLocalSeqScheme()

        if 'atom_id' in _factor and len(_factor['atom_id']) == 1:
            self.__cur_auth_atom_id = _factor['atom_id'][0]
        elif 'atom_ids' in _factor and len(_factor['atom_ids']) == 1:
            self.__cur_auth_atom_id = _factor['atom_ids'][0]
        else:
            self.__cur_auth_atom_id = ''

        if 'atom_id' not in _factor and 'atom_ids' not in _factor\
           and 'type_symbol' not in _factor and 'type_symbols' not in _factor:
            _factor['atom_not_specified'] = True

        if 'chain_id' not in _factor or len(_factor['chain_id']) == 0:
            if self.__largeModel:
                _factor['chain_id'] = [self.__representativeAsymId]
            else:
                _factor['chain_id'] = [ps['auth_chain_id'] for ps in self.__polySeq]
                if self.__hasNonPolySeq:
                    for np in self.__nonPolySeq:
                        _chainId = np['auth_chain_id']
                        if _chainId not in _factor['chain_id']:
                            _factor['chain_id'].append(_chainId)

        if 'seq_id' not in _factor and 'seq_ids' not in _factor:
            if 'comp_ids' in _factor and len(_factor['comp_ids']) > 0\
               and ('comp_id' not in _factor or len(_factor['comp_id']) == 0):
                lenCompIds = len(_factor['comp_ids'])
                _compIdSelect = set()
                for chainId in _factor['chain_id']:
                    ps = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chainId), None)
                    if ps is not None:
                        for realSeqId in ps['auth_seq_id']:
                            idx = ps['auth_seq_id'].index(realSeqId)
                            realCompId = ps['comp_id'][idx]
                            origCompId = ps['auth_comp_id'][idx]
                            if (lenCompIds == 1
                                and (re.match(toRegEx(translateToStdResName(_factor['comp_ids'][0], self.__ccU)), realCompId)
                                     or re.match(toRegEx(translateToStdResName(_factor['comp_ids'][0], self.__ccU)), origCompId)))\
                               or (lenCompIds == 2
                                   and (translateToStdResName(_factor['comp_ids'][0], self.__ccU) <= realCompId
                                        <= translateToStdResName(_factor['comp_ids'][1], self.__ccU)
                                        or translateToStdResName(_factor['comp_ids'][0], self.__ccU) <= origCompId
                                        <= translateToStdResName(_factor['comp_ids'][1], self.__ccU))):
                                _compIdSelect.add(realCompId)
                if self.__hasNonPolySeq:
                    for chainId in _factor['chain_id']:
                        npList = [np for np in self.__nonPolySeq if np['auth_chain_id'] == chainId]
                        for np in npList:
                            for realSeqId in np['auth_seq_id']:
                                idx = np['auth_seq_id'].index(realSeqId)
                                realCompId = np['comp_id'][idx]
                                origCompId = np['auth_comp_id'][idx]
                                if (lenCompIds == 1
                                    and (re.match(toRegEx(translateToStdResName(_factor['comp_ids'][0], self.__ccU)), realCompId)
                                         or re.match(toRegEx(translateToStdResName(_factor['comp_ids'][0], self.__ccU)), origCompId)))\
                                   or (lenCompIds == 2
                                       and (translateToStdResName(_factor['comp_ids'][0], self.__ccU) <= realCompId
                                            <= translateToStdResName(_factor['comp_ids'][1], self.__ccU)
                                            or translateToStdResName(_factor['comp_ids'][0], self.__ccU) <= origCompId
                                            <= translateToStdResName(_factor['comp_ids'][1], self.__ccU))):
                                    _compIdSelect.add(realCompId)
                _factor['comp_id'] = list(_compIdSelect)
                del _factor['comp_ids']

        if 'seq_ids' in _factor and len(_factor['seq_ids']) > 0\
           and ('seq_id' not in _factor or len(_factor['seq_id']) == 0):
            seqId = _factor['seq_ids'][0]
            _seqId = toRegEx(seqId)
            seqIds = []
            for chainId in _factor['chain_id']:
                ps = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chainId), None)
                if ps is not None:
                    found = False
                    for realSeqId in ps['auth_seq_id']:
                        if 'comp_id' in _factor and len(_factor['comp_id']) > 0:
                            idx = ps['auth_seq_id'].index(realSeqId)
                            realCompId = ps['comp_id'][idx]
                            origCompId = ps['auth_comp_id'][idx]
                            _compIdList = [translateToStdResName(_compId, self.__ccU) for _compId in _factor['comp_id']]
                            if realCompId not in _compIdList and origCompId not in _compIdList:
                                continue
                        if re.match(_seqId, str(realSeqId)):
                            seqIds.append(realSeqId)
                            found = True
                    if not found:
                        for realSeqId in ps['auth_seq_id']:
                            if 'comp_id' in _factor and len(_factor['comp_id']) > 0:
                                idx = ps['auth_seq_id'].index(realSeqId)
                                realCompId = ps['comp_id'][idx]
                                origCompId = ps['auth_comp_id'][idx]
                                _compIdList = [translateToStdResName(_compId, self.__ccU) for _compId in _factor['comp_id']]
                                if realCompId not in _compIdList and origCompId not in _compIdList:
                                    continue
                            seqKey = (chainId, realSeqId)
                            if seqKey in self.__authToLabelSeq:
                                _, realSeqId = self.__authToLabelSeq[seqKey]
                                if re.match(_seqId, str(realSeqId)):
                                    seqIds.append(realSeqId)
            if self.__hasNonPolySeq:
                for chainId in _factor['chain_id']:
                    npList = [np for np in self.__nonPolySeq if np['auth_chain_id'] == chainId]
                    for np in npList:
                        found = False
                        for realSeqId in np['auth_seq_id']:
                            if 'comp_id' in _factor and len(_factor['comp_id']) > 0:
                                idx = np['auth_seq_id'].index(realSeqId)
                                realCompId = np['comp_id'][idx]
                                origCompId = np['auth_comp_id'][idx]
                                _compIdList = [translateToStdResName(_compId, self.__ccU) for _compId in _factor['comp_id']]
                                if realCompId not in _compIdList and origCompId not in _compIdList:
                                    continue
                            if re.match(_seqId, str(realSeqId)):
                                seqIds.append(realSeqId)
                                found = True
                        if not found:
                            for realSeqId in np['auth_seq_id']:
                                if 'comp_id' in _factor and len(_factor['comp_id']) > 0:
                                    idx = np['auth_seq_id'].index(realSeqId)
                                    realCompId = np['comp_id'][idx]
                                    origCompId = np['auth_comp_id'][idx]
                                    _compIdList = [translateToStdResName(_compId, self.__ccU) for _compId in _factor['comp_id']]
                                    if realCompId not in _compIdList and origCompId not in _compIdList:
                                        continue
                                seqKey = (chainId, realSeqId)
                                if seqKey in self.__authToLabelSeq:
                                    _, realSeqId = self.__authToLabelSeq[seqKey]
                                    if re.match(_seqId, str(realSeqId)):
                                        seqIds.append(realSeqId)
            _factor['seq_id'] = list(set(seqIds))
            del _factor['seq_ids']

        if 'seq_id' not in _factor or len(_factor['seq_id']) == 0:
            seqIds = []
            for chainId in _factor['chain_id']:
                ps = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chainId), None)
                if ps is not None:
                    for realSeqId in ps['auth_seq_id']:
                        if 'comp_id' in _factor and len(_factor['comp_id']) > 0:
                            idx = ps['auth_seq_id'].index(realSeqId)
                            realCompId = ps['comp_id'][idx]
                            origCompId = ps['auth_comp_id'][idx]
                            _compIdList = [translateToStdResName(_compId, self.__ccU) for _compId in _factor['comp_id']]
                            if realCompId not in _compIdList and origCompId not in _compIdList:
                                continue
                        seqIds.append(realSeqId)
            if self.__hasNonPolySeq:
                for chainId in _factor['chain_id']:
                    npList = [np for np in self.__nonPolySeq if np['auth_chain_id'] == chainId]
                    for np in npList:
                        for realSeqId in np['auth_seq_id']:
                            if 'comp_id' in _factor and len(_factor['comp_id']) > 0:
                                idx = np['auth_seq_id'].index(realSeqId)
                                realCompId = np['comp_id'][idx]
                                origCompId = np['auth_comp_id'][idx]
                                _compIdList = [translateToStdResName(_compId, self.__ccU) for _compId in _factor['comp_id']]
                                if realCompId not in _compIdList and origCompId not in _compIdList:
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
                    ps = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chainId), None)
                    if ps is not None:
                        _compIdSelect |= set(ps['comp_id'])
                if self.__hasNonPolySeq:
                    for chainId in _factor['chain_id']:
                        npList = [np for np in self.__nonPolySeq if np['auth_chain_id'] == chainId]
                        for np in npList:
                            _compIdSelect |= set(np['comp_id'])
                for compId in _compIdSelect:
                    if self.__ccU.updateChemCompDict(compId):
                        for cca in self.__ccU.lastAtomList:
                            realTypeSymbol = cca[self.__ccU.ccaTypeSymbol]
                            if (lenTypeSymbols == 1 and re.match(toRegEx(_factor['type_symbols'][0]), realTypeSymbol))\
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
                    ps = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chainId), None)
                    if ps is not None:
                        _compIdSelect |= set(ps['comp_id'])
                if self.__hasNonPolySeq:
                    for chainId in _factor['chain_id']:
                        npList = [np for np in self.__nonPolySeq if np['auth_chain_id'] == chainId]
                        for np in npList:
                            _compIdSelect |= set(np['comp_id'])
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
                ps = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chainId), None)
                if ps is not None:
                    for realSeqId in ps['auth_seq_id']:
                        if 'seq_id' in _factor and len(_factor['seq_id']) > 0:
                            if self.getOrigSeqId(ps, realSeqId) not in _factor['seq_id']:
                                continue
                        idx = ps['auth_seq_id'].index(realSeqId)
                        realCompId = ps['comp_id'][idx]
                        if 'comp_id' in _factor and len(_factor['comp_id']) > 0:
                            origCompId = ps['auth_comp_id'][idx]
                            _compIdList = [translateToStdResName(_compId, self.__ccU) for _compId in _factor['comp_id']]
                            if realCompId not in _compIdList and origCompId not in _compIdList:
                                continue
                        _compIdSelect.add(realCompId)
            if self.__hasNonPolySeq:
                for chainId in _factor['chain_id']:
                    npList = [np for np in self.__nonPolySeq if np['auth_chain_id'] == chainId]
                    for np in npList:
                        for realSeqId in np['auth_seq_id']:
                            if 'seq_id' in _factor and len(_factor['seq_id']) > 0:
                                if self.getOrigSeqId(np, realSeqId, False) not in _factor['seq_id']:
                                    continue
                            idx = np['auth_seq_id'].index(realSeqId)
                            realCompId = np['comp_id'][idx]
                            if 'comp_id' in _factor and len(_factor['comp_id']) > 0:
                                origCompId = np['auth_comp_id'][idx]
                                _compIdList = [translateToStdResName(_compId, self.__ccU) for _compId in _factor['comp_id']]
                                if realCompId not in _compIdList and origCompId not in _compIdList:
                                    continue
                            _compIdSelect.add(realCompId)

            _atomIdSelect = set()
            for compId in _compIdSelect:
                if self.__ccU.updateChemCompDict(compId):
                    refAtomIdList = [cca[self.__ccU.ccaAtomId] for cca in self.__ccU.lastAtomList]
                    for cca in self.__ccU.lastAtomList:
                        if cca[self.__ccU.ccaLeavingAtomFlag] != 'Y':
                            realAtomId = cca[self.__ccU.ccaAtomId]
                            if lenAtomIds == 1:
                                atomId = translateToStdAtomName(_factor['atom_ids'][0], compId, refAtomIdList)
                                _, _, details = self.__nefT.get_valid_star_atom(compId, atomId, leave_unmatched=True)
                                if details is not None:
                                    _, _, details = self.__nefT.get_valid_star_atom_in_xplor(compId, atomId, leave_unmatched=True)
                                    if details is None and atomId.rfind('1') != -1:
                                        idx = atomId.rindex('1')
                                        atomId = atomId[0:idx] + '3' + atomId[idx + 1:]
                                _atomId = toNefEx(toRegEx(atomId))
                                if re.match(_atomId, realAtomId):
                                    _atomIdSelect.add(realAtomId)
                                    _factor['alt_atom_id'] = _factor['atom_ids'][0]
                            elif lenAtomIds == 2:
                                atomId1 = translateToStdAtomName(_factor['atom_ids'][0], compId, refAtomIdList)
                                atomId2 = translateToStdAtomName(_factor['atom_ids'][1], compId, refAtomIdList)
                                _, _, details = self.__nefT.get_valid_star_atom(compId, atomId1, leave_unmatched=True)
                                if details is not None:
                                    _, _, details = self.__nefT.get_valid_star_atom_in_xplor(compId, atomId1, leave_unmatched=True)
                                    if details is None and atomId1.rfind('1') != -1:
                                        idx = atomId1.rindex('1')
                                        atomId1 = atomId1[0:idx] + '3' + atomId1[idx + 1:]
                                _, _, details = self.__nefT.get_valid_star_atom(compId, atomId2, leave_unmatched=True)
                                if details is not None:
                                    _, _, details = self.__nefT.get_valid_star_atom_in_xplor(compId, atomId2, leave_unmatched=True)
                                    if details is None and atomId2.rfind('1') != -1:
                                        idx = atomId2.rindex('1')
                                        atomId2 = atomId2[0:idx] + '3' + atomId2[idx + 1:]
                                if (atomId1 < atomId2 and atomId1 <= realAtomId <= atomId2)\
                                   or (atomId1 > atomId2 and atomId2 <= realAtomId <= atomId1):
                                    _atomIdSelect.add(realAtomId)
            _factor['atom_id'] = list(_atomIdSelect)

            if len(_factor['atom_id']) == 0:
                self.__preferAuthSeq = not self.__preferAuthSeq

                _compIdSelect = set()
                for chainId in _factor['chain_id']:
                    ps = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chainId), None)
                    if ps is not None:
                        for realSeqId in ps['auth_seq_id']:
                            if 'seq_id' in _factor and len(_factor['seq_id']) > 0:
                                if self.getOrigSeqId(ps, realSeqId) not in _factor['seq_id']:
                                    continue
                            idx = ps['auth_seq_id'].index(realSeqId)
                            realCompId = ps['comp_id'][idx]
                            if 'comp_id' in _factor and len(_factor['comp_id']) > 0:
                                origCompId = ps['auth_comp_id'][idx]
                                _compIdList = [translateToStdResName(_compId, self.__ccU) for _compId in _factor['comp_id']]
                                if realCompId not in _compIdList and origCompId not in _compIdList:
                                    continue
                            _compIdSelect.add(realCompId)
                if self.__hasNonPolySeq:
                    for chainId in _factor['chain_id']:
                        npList = [np for np in self.__nonPolySeq if np['auth_chain_id'] == chainId]
                        for np in npList:
                            for realSeqId in np['auth_seq_id']:
                                if 'seq_id' in _factor and len(_factor['seq_id']) > 0:
                                    if self.getOrigSeqId(np, realSeqId, False) not in _factor['seq_id']:
                                        continue
                                idx = np['auth_seq_id'].index(realSeqId)
                                realCompId = np['comp_id'][idx]
                                if 'comp_id' in _factor and len(_factor['comp_id']) > 0:
                                    origCompId = np['auth_comp_id'][idx]
                                    _compIdList = [translateToStdResName(_compId, self.__ccU) for _compId in _factor['comp_id']]
                                    if realCompId not in _compIdList and origCompId not in _compIdList:
                                        continue
                                _compIdSelect.add(realCompId)

                _atomIdSelect = set()
                for compId in _compIdSelect:
                    if self.__ccU.updateChemCompDict(compId):
                        refAtomIdList = [cca[self.__ccU.ccaAtomId] for cca in self.__ccU.lastAtomList]
                        for cca in self.__ccU.lastAtomList:
                            if cca[self.__ccU.ccaLeavingAtomFlag] != 'Y':
                                realAtomId = cca[self.__ccU.ccaAtomId]
                                if lenAtomIds == 1:
                                    atomId = translateToStdAtomName(_factor['atom_ids'][0], compId, refAtomIdList)
                                    _, _, details = self.__nefT.get_valid_star_atom(compId, atomId, leave_unmatched=True)
                                    if details is not None:
                                        _, _, details = self.__nefT.get_valid_star_atom_in_xplor(compId, atomId, leave_unmatched=True)
                                        if details is None and atomId.rfind('1') != -1:
                                            idx = atomId.rindex('1')
                                            atomId = atomId[0:idx] + '3' + atomId[idx + 1:]
                                    _atomId = toNefEx(toRegEx(atomId))
                                    if re.match(_atomId, realAtomId):
                                        _atomIdSelect.add(realAtomId)
                                        _factor['alt_atom_id'] = _factor['atom_ids'][0]
                                elif lenAtomIds == 2:
                                    atomId1 = translateToStdAtomName(_factor['atom_ids'][0], compId, refAtomIdList)
                                    atomId2 = translateToStdAtomName(_factor['atom_ids'][1], compId, refAtomIdList)
                                    _, _, details = self.__nefT.get_valid_star_atom(compId, atomId1, leave_unmatched=True)
                                    if details is not None:
                                        _, _, details = self.__nefT.get_valid_star_atom_in_xplor(compId, atomId1, leave_unmatched=True)
                                        if details is None and atomId1.rfind('1') != -1:
                                            idx = atomId1.rindex('1')
                                            atomId1 = atomId1[0:idx] + '3' + atomId1[idx + 1:]
                                    _, _, details = self.__nefT.get_valid_star_atom(compId, atomId2, leave_unmatched=True)
                                    if details is not None:
                                        _, _, details = self.__nefT.get_valid_star_atom_in_xplor(compId, atomId2, leave_unmatched=True)
                                        if details is None and atomId2.rfind('1') != -1:
                                            idx = atomId2.rindex('1')
                                            atomId2 = atomId2[0:idx] + '3' + atomId2[idx + 1:]
                                    if (atomId1 < atomId2 and atomId1 <= realAtomId <= atomId2)\
                                       or (atomId1 > atomId2 and atomId2 <= realAtomId <= atomId1):
                                        _atomIdSelect.add(realAtomId)
                _factor['atom_id'] = list(_atomIdSelect)

                if len(_factor['atom_id']) > 0:
                    self.__authSeqId = 'auth_seq_id' if self.__preferAuthSeq else 'label_seq_id'
                    if len(self.atomSelectionSet) > 0:
                        self.__setLocalSeqScheme()
                else:
                    self.__preferAuthSeq = not self.__preferAuthSeq

                if len(_factor['atom_id']) == 0:
                    _factor['atom_id'] = [None]
                    _factor['alt_atom_id'] = _factor['atom_ids']
            # del _factor['atom_ids']

        if 'atom_id' not in _factor or len(_factor['atom_id']) == 0:
            _compIdSelect = set()
            _nonPolyCompIdSelect = []
            for chainId in _factor['chain_id']:
                ps = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chainId), None)
                if ps is not None:
                    for realSeqId in ps['auth_seq_id']:
                        if 'seq_id' in _factor and len(_factor['seq_id']) > 0:
                            if self.getOrigSeqId(ps, realSeqId) not in _factor['seq_id']:
                                continue
                        idx = ps['auth_seq_id'].index(realSeqId)
                        realCompId = ps['comp_id'][idx]
                        if 'comp_id' in _factor and len(_factor['comp_id']) > 0:
                            origCompId = ps['auth_comp_id'][idx]
                            _compIdList = [translateToStdResName(_compId, self.__ccU) for _compId in _factor['comp_id']]
                            if realCompId not in _compIdList and origCompId not in _compIdList:
                                continue
                        _compIdSelect.add(realCompId)
            if self.__hasNonPolySeq:
                for chainId in _factor['chain_id']:
                    npList = [np for np in self.__nonPolySeq if np['auth_chain_id'] == chainId]
                    for np in npList:
                        for realSeqId in np['auth_seq_id']:
                            if 'seq_id' in _factor and len(_factor['seq_id']) > 0:
                                if self.getOrigSeqId(np, realSeqId, False) not in _factor['seq_id']:
                                    continue
                            idx = np['auth_seq_id'].index(realSeqId)
                            realCompId = np['comp_id'][idx]
                            if 'comp_id' in _factor and len(_factor['comp_id']) > 0:
                                origCompId = np['auth_comp_id'][idx]
                                _compIdList = [translateToStdResName(_compId, self.__ccU) for _compId in _factor['comp_id']]
                                if realCompId not in _compIdList and origCompId not in _compIdList:
                                    continue
                            _nonPolyCompIdSelect.append({'chain_id': chainId,
                                                         'seq_id': realSeqId,
                                                         'comp_id': realCompId})

            _atomIdSelect = set()
            for compId in _compIdSelect:
                if self.__ccU.updateChemCompDict(compId):
                    for cca in self.__ccU.lastAtomList:
                        if cca[self.__ccU.ccaLeavingAtomFlag] != 'Y':
                            realAtomId = cca[self.__ccU.ccaAtomId]
                            _atomIdSelect.add(realAtomId)

            for nonPolyCompId in _nonPolyCompIdSelect:
                _, coordAtomSite = self.getCoordAtomSiteOf(nonPolyCompId['chain_id'], nonPolyCompId['seq_id'], cifCheck)
                if coordAtomSite is not None:
                    for realAtomId in coordAtomSite['atom_id']:
                        _atomIdSelect.add(realAtomId)

            _factor['atom_id'] = list(_atomIdSelect)
            if len(_factor['atom_id']) == 0:
                self.__preferAuthSeq = not self.__preferAuthSeq

                _compIdSelect = set()
                _nonPolyCompIdSelect = []
                for chainId in _factor['chain_id']:
                    ps = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chainId), None)
                    if ps is not None:
                        for realSeqId in ps['auth_seq_id']:
                            if 'seq_id' in _factor and len(_factor['seq_id']) > 0:
                                if self.getOrigSeqId(ps, realSeqId) not in _factor['seq_id']:
                                    continue
                            idx = ps['auth_seq_id'].index(realSeqId)
                            realCompId = ps['comp_id'][idx]
                            if 'comp_id' in _factor and len(_factor['comp_id']) > 0:
                                origCompId = ps['auth_comp_id'][idx]
                                _compIdList = [translateToStdResName(_compId, self.__ccU) for _compId in _factor['comp_id']]
                                if realCompId not in _compIdList and origCompId not in _compIdList:
                                    continue
                            _compIdSelect.add(realCompId)
                if self.__hasNonPolySeq:
                    for chainId in _factor['chain_id']:
                        npList = [np for np in self.__nonPolySeq if np['auth_chain_id'] == chainId]
                        for np in npList:
                            for realSeqId in np['auth_seq_id']:
                                if 'seq_id' in _factor and len(_factor['seq_id']) > 0:
                                    if self.getOrigSeqId(np, realSeqId, False) not in _factor['seq_id']:
                                        continue
                                idx = np['auth_seq_id'].index(realSeqId)
                                realCompId = np['comp_id'][idx]
                                if 'comp_id' in _factor and len(_factor['comp_id']) > 0:
                                    origCompId = np['auth_comp_id'][idx]
                                    _compIdList = [translateToStdResName(_compId, self.__ccU) for _compId in _factor['comp_id']]
                                    if realCompId not in _compIdList and origCompId not in _compIdList:
                                        continue
                                _nonPolyCompIdSelect.append({'chain_id': chainId,
                                                             'seq_id': realSeqId,
                                                             'comp_id': realCompId})

                _atomIdSelect = set()
                for compId in _compIdSelect:
                    if self.__ccU.updateChemCompDict(compId):
                        for cca in self.__ccU.lastAtomList:
                            if cca[self.__ccU.ccaLeavingAtomFlag] != 'Y':
                                realAtomId = cca[self.__ccU.ccaAtomId]
                                _atomIdSelect.add(realAtomId)

                for nonPolyCompId in _nonPolyCompIdSelect:
                    _, coordAtomSite = self.getCoordAtomSiteOf(nonPolyCompId['chain_id'], nonPolyCompId['seq_id'], cifCheck)
                    if coordAtomSite is not None:
                        for realAtomId in coordAtomSite['atom_id']:
                            _atomIdSelect.add(realAtomId)

                _factor['atom_id'] = list(_atomIdSelect)

                if len(_factor['atom_id']) > 0:
                    self.__authSeqId = 'auth_seq_id' if self.__preferAuthSeq else 'label_seq_id'
                    if len(self.atomSelectionSet) > 0:
                        self.__setLocalSeqScheme()
                else:
                    self.__preferAuthSeq = not self.__preferAuthSeq

                if len(_factor['atom_id']) == 0:
                    _factor['atom_id'] = [None]

        _atomSelection = []

        self.__with_axis = self.__cur_subtype in ('rdc', 'diff')

        if _factor['atom_id'][0] is not None:
            foundCompId = self.__consumeFactor_expressions__(_factor, cifCheck, _atomSelection, isPolySeq=True, isChainSpecified=True)
            if self.__hasNonPolySeq:
                foundCompId |= self.__consumeFactor_expressions__(_factor, cifCheck, _atomSelection, isPolySeq=False, isChainSpecified=True, altPolySeq=self.__nonPolySeq)

            if not foundCompId and len(_factor['chain_id']) == 1 and len(self.__polySeq) > 1:
                self.__consumeFactor_expressions__(_factor, cifCheck, _atomSelection, isPolySeq=True, isChainSpecified=False)
                if self.__hasNonPolySeq:
                    self.__consumeFactor_expressions__(_factor, cifCheck, _atomSelection, isPolySeq=False, isChainSpecified=False, altPolySeq=self.__nonPolySeq)

        if 'atom_ids' in _factor:
            del _factor['atom_ids']
        if 'atom_not_specified' in _factor:
            del _factor['atom_not_specified']

        atomSelection = [dict(s) for s in set(frozenset(atom.items()) for atom in _atomSelection)]

        if 'alt_chain_id' in _factor:
            for _atom in atomSelection:
                self.updateSegmentIdDict(_factor, _atom['chain_id'])

        if 'atom_selection' not in _factor:
            _factor['atom_selection'] = atomSelection
        else:
            _atomSelection = []
            for _atom in _factor['atom_selection']:
                if _atom in atomSelection:
                    _atomSelection.append(_atom)
            _factor['atom_selection'] = _atomSelection

        if len(_factor['atom_selection']) == 0:
            if self.__with_axis and _factor['atom_id'][0] in XPLOR_RDC_PRINCIPAL_AXIS_NAMES:
                return _factor
            if self.__cur_subtype == 'dist' and _factor['atom_id'][0] in XPLOR_NITROXIDE_NAMES:
                return _factor
            __factor = copy.copy(_factor)
            del __factor['atom_selection']
            if self.__cur_subtype != 'plane':
                if cifCheck:
                    self.warningMessage += f"[Insufficient atom selection] {self.__getCurrentRestraint()}"\
                        f"The {clauseName} has no effect for a factor {__factor}.\n"
                    self.__preferAuthSeq = not self.__preferAuthSeq
                    self.__authSeqId = 'auth_seq_id' if self.__preferAuthSeq else 'label_seq_id'
                    self.__setLocalSeqScheme()
                    # """
                    # if 'atom_id' in __factor and __factor['atom_id'][0] is None:
                    #     if 'label_seq_scheme' not in self.reasonsForReParsing:
                    #         self.reasonsForReParsing['label_seq_scheme'] = True
                    # """
                else:
                    self.__warningInAtomSelection += f"[Insufficient atom selection] {self.__getCurrentRestraint()}"\
                        f"The {clauseName} has no effect for a factor {__factor}. "\
                        "Please update the sequence in the Macromolecules page.\n"
            else:
                hint = f" Please verify that the planality restraints match with the residue {_factor['comp_id'][0]!r}"\
                    if 'comp_id' in _factor and len(_factor['comp_id']) == 1 else ''
                self.warningMessage += f"[Insufficient atom selection] {self.__getCurrentRestraint()}"\
                    f"The {clauseName} has no effect for a factor {__factor}.{hint}\n"

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
        if 'alt_chain_id' in _factor:
            del _factor['alt_chain_id']
        if 'alt_atom_id' in _factor:
            del _factor['alt_atom_id']

        return _factor

    def __consumeFactor_expressions__(self, _factor, cifCheck, _atomSelection, isPolySeq=True, isChainSpecified=True, altPolySeq=None):
        atomSpecified = True
        if 'atom_not_specified' in _factor:
            atomSpecified = not _factor['atom_not_specified']
        foundCompId = False

        for chainId in (_factor['chain_id'] if isChainSpecified else [ps['auth_chain_id'] for ps in (self.__polySeq if isPolySeq else altPolySeq)]):
            psList = [ps for ps in (self.__polySeq if isPolySeq else altPolySeq) if ps['auth_chain_id'] == chainId]

            if len(psList) == 0:
                continue

            for ps in psList:

                for seqId in _factor['seq_id']:
                    _seqId_ = seqId
                    seqId = self.getRealSeqId(ps, seqId, isPolySeq)

                    if self.__reasons is not None:
                        if 'branched_remap' in self.__reasons and seqId in self.__reasons['branched_remap']:
                            fixedChainId, seqId = retrieveRemappedChainId(self.__reasons['branched_remap'], seqId)
                            if fixedChainId != chainId:
                                continue
                        if 'chain_id_remap' in self.__reasons and seqId in self.__reasons['chain_id_remap']:
                            fixedChainId, seqId = retrieveRemappedChainId(self.__reasons['chain_id_remap'], seqId)
                            if fixedChainId != chainId:
                                continue
                        elif 'chain_id_clone' in self.__reasons and seqId in self.__reasons['chain_id_clone']:
                            fixedChainId, seqId = retrieveRemappedChainId(self.__reasons['chain_id_clone'], seqId)
                            if fixedChainId != chainId:
                                continue
                        elif 'seq_id_remap' in self.__reasons:
                            _, seqId = retrieveRemappedSeqId(self.__reasons['seq_id_remap'], chainId, seqId)

                    if ps is not None and seqId in ps['auth_seq_id']:
                        compId = ps['comp_id'][ps['auth_seq_id'].index(seqId)]
                    elif 'gap_in_auth_seq' in ps and seqId is not None:
                        compId = None
                        min_auth_seq_id = ps['auth_seq_id'][0]
                        max_auth_seq_id = ps['auth_seq_id'][-1]
                        if min_auth_seq_id <= seqId <= max_auth_seq_id:
                            _seqId_ = seqId + 1
                            while _seqId_ <= max_auth_seq_id:
                                if _seqId_ in ps['auth_seq_id']:
                                    break
                                _seqId_ += 1
                            if _seqId_ not in ps['auth_seq_id']:
                                _seqId_ = seqId - 1
                                while _seqId_ >= min_auth_seq_id:
                                    if _seqId_ in ps['auth_seq_id']:
                                        break
                                    _seqId_ -= 1
                            if _seqId_ in ps['auth_seq_id']:
                                idx = ps['auth_seq_id'].index(_seqId_) - _seqId_ - seqId
                                try:
                                    seqId = ps['auth_seq_id'][idx]
                                    compId = ps['comp_id'][idx]
                                except IndexError:
                                    pass
                    else:
                        compId = None

                    if not isPolySeq and compId is None:
                        if 'alt_auth_seq_id' in ps and seqId in ps['alt_auth_seq_id']:
                            idx = ps['alt_auth_seq_id'].index(seqId)
                            seqId = ps['seq_id'][idx]
                            compId = ps['comp_id'][idx]
                        elif seqId in ps['seq_id']:
                            idx = ps['seq_id'].index(seqId)
                            compId = ps['comp_id'][idx]
                            _seqId_ = ps['auth_seq_id'][idx]

                    seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck)

                    if compId is None and seqKey in self.__authToLabelSeq:
                        _, seqId = self.__authToLabelSeq[seqKey]
                        if ps is not None and seqId in ps['auth_seq_id']:
                            compId = ps['comp_id'][ps['auth_seq_id'].index(seqId)]
                            seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck)

                    if compId is None and coordAtomSite is not None and ps is not None and seqKey[1] in ps['auth_seq_id']:
                        compId = ps['comp_id'][ps['auth_seq_id'].index(seqKey[1])]

                    if coordAtomSite is None and not isPolySeq:
                        try:
                            idx = ps['auth_seq_id'].index(seqId)
                            seqId = ps['seq_id'][idx]
                            compId = ps['comp_id'][idx]
                            seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck)
                        except ValueError:
                            pass

                    if compId is None:
                        continue

                    if self.__reasons is not None:
                        if 'non_poly_remap' in self.__reasons and compId in self.__reasons['non_poly_remap']\
                           and seqId in self.__reasons['non_poly_remap'][compId]:
                            fixedChainId, seqId = retrieveRemappedNonPoly(self.__reasons['non_poly_remap'], chainId, seqId, compId)
                            if fixedChainId != chainId:
                                continue

                    _seqId = seqId
                    if not isPolySeq and 'alt_auth_seq_id' in ps and seqId in ps['auth_seq_id'] and seqId not in ps['alt_auth_seq_id']:
                        seqId = next(_altSeqId for _seqId, _altSeqId in zip(ps['auth_seq_id'], ps['alt_auth_seq_id']) if _seqId == seqId)
                        seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck)

                    if not isPolySeq and isChainSpecified and self.doesNonPolySeqIdMatchWithPolySeqUnobs(_factor['chain_id'][0], _seqId_):
                        continue

                    foundCompId = True

                    if not self.__with_axis:
                        updatePolySeqRst(self.__polySeqRst, chainId, seqId, compId)

                    for atomId in _factor['atom_id']:
                        if self.__with_axis:
                            if atomId in XPLOR_RDC_PRINCIPAL_AXIS_NAMES:
                                continue
                            updatePolySeqRst(self.__polySeqRst, chainId, seqId, compId)

                        origAtomId = _factor['atom_id'] if 'alt_atom_id' not in _factor else _factor['alt_atom_id']

                        atomId = atomId.upper()

                        if compId not in monDict3 and self.__mrAtomNameMapping is not None and (_seqId in ps['auth_seq_id'] or _seqId_ in ps['auth_seq_id']):
                            if _seqId in ps['auth_seq_id']:
                                authCompId = ps['auth_comp_id'][ps['auth_seq_id'].index(_seqId)]
                            else:
                                authCompId = ps['auth_comp_id'][ps['auth_seq_id'].index(_seqId_)]
                            atomId = retrieveAtomIdFromMRMap(self.__mrAtomNameMapping, _seqId, authCompId, atomId, coordAtomSite)
                            if coordAtomSite is not None and atomId not in coordAtomSite['atom_id']:
                                if self.__reasons is not None and 'branched_remap' in self.__reasons:
                                    _seqId_ = retrieveOriginalSeqIdFromMRMap(self.__reasons['branched_remap'], chainId, seqId)
                                    if _seqId_ != seqId:
                                        _, _, atomId = retrieveAtomIdentFromMRMap(self.__mrAtomNameMapping, _seqId_, authCompId, atomId, coordAtomSite)
                                elif seqId != _seqId:
                                    atomId = retrieveAtomIdFromMRMap(self.__mrAtomNameMapping, seqId, authCompId, atomId, coordAtomSite)

                        atomIds = self.getAtomIdList(_factor, compId, atomId)

                        # @see: https://bmrb.io/ref_info/atom_nom.tbl
                        if self.__trust_bmrb_ref_info:
                            pass

                        # @see: https://bmrb.io/macro/files/xplor_to_iupac.Nov140620
                        else:
                            if compId == 'ASN':
                                if atomId == 'HD21':
                                    _atomId = atomId[:-1] + '2'
                                    if self.__nefT.validate_comp_atom(compId, _atomId):
                                        atomIds = self.__nefT.get_valid_star_atom(compId, _atomId)[0]
                                elif atomId == 'HD22':
                                    _atomId = atomId[:-1] + '1'
                                    if self.__nefT.validate_comp_atom(compId, _atomId):
                                        atomIds = self.__nefT.get_valid_star_atom(compId, _atomId)[0]
                            elif compId == 'GLN':
                                if atomId == 'HE21':
                                    _atomId = atomId[:-1] + '2'
                                    if self.__nefT.validate_comp_atom(compId, _atomId):
                                        atomIds = self.__nefT.get_valid_star_atom(compId, _atomId)[0]
                                elif atomId == 'HE22':
                                    _atomId = atomId[:-1] + '1'
                                    if self.__nefT.validate_comp_atom(compId, _atomId):
                                        atomIds = self.__nefT.get_valid_star_atom(compId, _atomId)[0]

                        if coordAtomSite is not None\
                           and not any(_atomId for _atomId in atomIds if _atomId in coordAtomSite['atom_id']):
                            if atomId in coordAtomSite['atom_id']:
                                atomIds = [atomId]
                            elif 'alt_atom_id' in _factor:
                                _atomId_ = toNefEx(toRegEx(_factor['alt_atom_id']))
                                _atomIds_ = [_atomId for _atomId in coordAtomSite['atom_id'] if re.match(_atomId_, _atomId)]
                                if len(_atomIds_) > 0:
                                    atomIds = _atomIds_

                        if self.__cur_subtype == 'dist' and atomId in XPLOR_NITROXIDE_NAMES and coordAtomSite is not None\
                           and atomId not in coordAtomSite['atom_id']:
                            if compId == 'CYS' and 'SG' in coordAtomSite['atom_id']:
                                atomIds = ['SG']
                                _factor['alt_atom_id'] = atomId + '(nitroxide attached point)'
                            elif compId == 'SER' and 'OG' in coordAtomSite['atom_id']:
                                atomIds = ['OG']
                                _factor['alt_atom_id'] = atomId + '(nitroxide attached point)'

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
                                    elif self.__preferAuthSeq and atomSpecified:
                                        _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck, asis=False)
                                        if _coordAtomSite is not None:
                                            _compId = _coordAtomSite['comp_id']
                                            _atomId = self.getAtomIdList(_factor, _compId, atomId)[0]
                                            if _atomId in _coordAtomSite['atom_id']:
                                                _atom = {}
                                                _atom['comp_id'] = _compId
                                                _atom['type_symbol'] = _coordAtomSite['type_symbol'][_coordAtomSite['atom_id'].index(_atomId)]
                                                self.__preferAuthSeq = False
                                                self.__authSeqId = 'label_seq_id'
                                                seqKey = _seqKey
                                                chainId, seqId = seqKey
                                                if len(self.atomSelectionSet) > 0:
                                                    self.__setLocalSeqScheme()
                                            elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                _atom = {}
                                                _atom['comp_id'] = _compId
                                                _atom['type_symbol'] = _coordAtomSite['type_symbol'][_coordAtomSite['alt_atom_id'].index(_atomId)]
                                                self.__preferAuthSeq = False
                                                self.__authSeqId = 'label_seq_id'
                                                self.__authAtomId = 'auth_atom_id'
                                                seqKey = _seqKey
                                                chainId, seqId = seqKey
                                                if len(self.atomSelectionSet) > 0:
                                                    self.__setLocalSeqScheme()
                                    elif _seqId_ in ps['auth_seq_id'] and atomSpecified:
                                        self.__preferAuthSeq = True
                                        _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, _seqId_, cifCheck)
                                        if _coordAtomSite is not None:
                                            _compId = _coordAtomSite['comp_id']
                                            _atomId = self.getAtomIdList(_factor, _compId, atomId)[0]
                                            if _atomId in _coordAtomSite['atom_id']:
                                                _atom = {}
                                                _atom['comp_id'] = _compId
                                                _atom['type_symbol'] = _coordAtomSite['type_symbol'][_coordAtomSite['atom_id'].index(_atomId)]
                                                self.__authSeqId = 'auth_seq_id'
                                                seqKey = _seqKey
                                                chainId, seqId = seqKey
                                                if len(self.atomSelectionSet) > 0:
                                                    self.__setLocalSeqScheme()
                                            elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                _atom = {}
                                                _atom['comp_id'] = _compId
                                                _atom['type_symbol'] = _coordAtomSite['type_symbol'][_coordAtomSite['alt_atom_id'].index(_atomId)]
                                                self.__authSeqId = 'auth_seq_id'
                                                self.__authAtomId = 'auth_atom_id'
                                                seqKey = _seqKey
                                                chainId, seqId = seqKey
                                                if len(self.atomSelectionSet) > 0:
                                                    self.__setLocalSeqScheme()
                                            else:
                                                self.__preferAuthSeq = False
                                        else:
                                            self.__preferAuthSeq = False

                                elif self.__preferAuthSeq and atomSpecified:
                                    if len(self.atomSelectionSet) == 0:
                                        _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck, asis=False)
                                        if _coordAtomSite is not None:
                                            _compId = _coordAtomSite['comp_id']
                                            _atomId = self.getAtomIdList(_factor, _compId, atomId)[0]
                                            if _atomId in _coordAtomSite['atom_id']:
                                                _atom = {}
                                                _atom['comp_id'] = _compId
                                                _atom['type_symbol'] = _coordAtomSite['type_symbol'][_coordAtomSite['atom_id'].index(_atomId)]
                                                self.__preferAuthSeq = False
                                                self.__authSeqId = 'label_seq_id'
                                                seqKey = _seqKey
                                                chainId, seqId = seqKey
                                                if len(self.atomSelectionSet) > 0:
                                                    self.__setLocalSeqScheme()
                                            elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                _atom = {}
                                                _atom['comp_id'] = _compId
                                                _atom['type_symbol'] = _coordAtomSite['type_symbol'][_coordAtomSite['alt_atom_id'].index(_atomId)]
                                                self.__preferAuthSeq = False
                                                self.__authSeqId = 'label_seq_id'
                                                self.__authAtomId = 'auth_atom_id'
                                                seqKey = _seqKey
                                                chainId, seqId = seqKey
                                                if len(self.atomSelectionSet) > 0:
                                                    self.__setLocalSeqScheme()
                                elif _seqId_ in ps['auth_seq_id'] and atomSpecified:
                                    if len(self.atomSelectionSet) == 0:
                                        self.__preferAuthSeq = True
                                        _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, _seqId_, cifCheck)
                                        if _coordAtomSite is not None:
                                            _compId = _coordAtomSite['comp_id']
                                            _atomId = self.getAtomIdList(_factor, _compId, atomId)[0]
                                            if _atomId in _coordAtomSite['atom_id']:
                                                _atom = {}
                                                _atom['comp_id'] = _compId
                                                _atom['type_symbol'] = _coordAtomSite['type_symbol'][_coordAtomSite['atom_id'].index(_atomId)]
                                                self.__authSeqId = 'auth_seq_id'
                                                seqKey = _seqKey
                                                chainId, seqId = seqKey
                                                if len(self.atomSelectionSet) > 0:
                                                    self.__setLocalSeqScheme()
                                            elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                _atom = {}
                                                _atom['comp_id'] = _compId
                                                _atom['type_symbol'] = _coordAtomSite['type_symbol'][_coordAtomSite['alt_atom_id'].index(_atomId)]
                                                self.__authSeqId = 'auth_seq_id'
                                                self.__authAtomId = 'auth_atom_id'
                                                seqKey = _seqKey
                                                chainId, seqId = seqKey
                                                if len(self.atomSelectionSet) > 0:
                                                    self.__setLocalSeqScheme()
                                            else:
                                                self.__preferAuthSeq = False
                                        else:
                                            self.__preferAuthSeq = False

                                if _atom is not None:
                                    _compIdList = None if 'comp_id' not in _factor else [translateToStdResName(_compId, self.__ccU) for _compId in _factor['comp_id']]
                                    if ('comp_id' not in _factor or _atom['comp_id'] in _compIdList)\
                                       and ('type_symbol' not in _factor or _atom['type_symbol'] in _factor['type_symbol']):
                                        selection = {'chain_id': chainId, 'seq_id': seqId, 'comp_id': _atom['comp_id'], 'atom_id': _atomId}
                                        if len(self.__cur_auth_atom_id) > 0:
                                            selection['auth_atom_id'] = self.__cur_auth_atom_id
                                        _atomSelection.append(selection)
                                else:
                                    ccdCheck = True

                            if (len(_factor['chain_id']) > 1 or len(_factor['seq_id']) > 1) and not atomSpecified:
                                continue

                            if isPolySeq and 'ambig_auth_seq_id' in ps and _seqId in ps['ambig_auth_seq_id']:
                                continue

                            if not isPolySeq and 'alt_auth_seq_id' in ps and _seqId in ps['auth_seq_id'] and _seqId not in ps['alt_auth_seq_id']:
                                continue

                            if ccdCheck and compId is not None and _atomId not in XPLOR_RDC_PRINCIPAL_AXIS_NAMES and _atomId not in XPLOR_NITROXIDE_NAMES:
                                _compIdList = None if 'comp_id' not in _factor else [translateToStdResName(_compId, self.__ccU) for _compId in _factor['comp_id']]
                                if self.__ccU.updateChemCompDict(compId) and ('comp_id' not in _factor or compId in _compIdList):
                                    if len(origAtomId) > 1:
                                        typeSymbols = set()
                                        for _atomId_ in origAtomId:
                                            typeSymbol = next((cca[self.__ccU.ccaTypeSymbol] for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId_), None)
                                            if typeSymbol is not None:
                                                typeSymbols.add(typeSymbol)
                                                if len(typeSymbols) > 1:
                                                    break
                                        if len(typeSymbols) > 1:
                                            continue
                                    cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId), None)
                                    if cca is not None and ('type_symbol' not in _factor or cca[self.__ccU.ccaTypeSymbol] in _factor['type_symbol']):
                                        selection = {'chain_id': chainId, 'seq_id': seqId, 'comp_id': compId, 'atom_id': _atomId}
                                        if len(self.__cur_auth_atom_id) > 0:
                                            selection['auth_atom_id'] = self.__cur_auth_atom_id
                                        _atomSelection.append(selection)
                                        if cifCheck and seqKey not in self.__coordUnobsRes and self.__ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] == 'REL':
                                            if self.__cur_subtype != 'plane' and coordAtomSite is not None:
                                                checked = False
                                                if seqId == 1 and _atomId in ('H', 'HN'):
                                                    if coordAtomSite is not None and 'H1' in coordAtomSite['atom_id']:
                                                        checked = True
                                                if _atomId[0] == 'H':
                                                    ccb = next((ccb for ccb in self.__ccU.lastBonds
                                                                if _atomId in (ccb[self.__ccU.ccbAtomId1], ccb[self.__ccU.ccbAtomId2])), None)
                                                    if ccb is not None:
                                                        bondedTo = ccb[self.__ccU.ccbAtomId2] if ccb[self.__ccU.ccbAtomId1] == _atomId else ccb[self.__ccU.ccbAtomId1]
                                                        if coordAtomSite is not None and bondedTo in coordAtomSite['atom_id'] and cca[self.__ccU.ccaLeavingAtomFlag] != 'Y':
                                                            checked = True
                                                            if len(origAtomId) == 1:
                                                                _atomSelection[-1]['hydrogen_not_instantiated'] = True
                                                                self.warningMessage += f"[Hydrogen not instantiated] {self.__getCurrentRestraint()}"\
                                                                    f"{chainId}:{seqId}:{compId}:{origAtomId} is not properly instantiated in the coordinates. "\
                                                                    "Please re-upload the model file.\n"
                                                if not checked:
                                                    if chainId in MAJOR_ASYM_ID_SET:
                                                        if isPolySeq and not self.__preferAuthSeq\
                                                           and ('label_seq_offset' not in self.reasonsForReParsing
                                                                or chainId not in self.reasonsForReParsing['label_seq_offset']):
                                                            if 'label_seq_offset' not in self.reasonsForReParsing:
                                                                self.reasonsForReParsing['label_seq_offset'] = {}
                                                            offset = self.getLabelSeqOffsetDueToUnobs(ps)
                                                            self.reasonsForReParsing['label_seq_offset'][chainId] = offset
                                                            if offset != 0:
                                                                self.reasonsForReParsing['label_seq_scheme'] = True
                                                        if seqId < 1 and len(self.__polySeq) == 1:
                                                            self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                                                                f"{chainId}:{seqId}:{compId}:{origAtomId} is not present in the coordinates. "\
                                                                f"The residue number '{seqId}' is not present in polymer sequence of chain {chainId} of the coordinates. "\
                                                                "Please update the sequence in the Macromolecules page.\n"
                                                        else:
                                                            self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                                                                f"{chainId}:{seqId}:{compId}:{origAtomId} is not present in the coordinates.\n"
                                    elif cca is None and 'type_symbol' not in _factor and 'atom_ids' not in _factor:
                                        # """
                                        # if self.__reasons is None and seqKey in self.__authToLabelSeq:
                                        #     _, _seqId = self.__authToLabelSeq[seqKey]
                                        #     if ps is not None and _seqId in ps['auth_seq_id']:
                                        #         _compId = ps['comp_id'][ps['auth_seq_id'].index(_seqId)]
                                        #         if self.__ccU.updateChemCompDict(_compId):
                                        #             cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId), None)
                                        #             if cca is not None:
                                        #                 if 'label_seq_scheme' not in self.reasonsForReParsing:
                                        #                     self.reasonsForReParsing['label_seq_scheme'] = True
                                        # """
                                        if cifCheck and self.__cur_subtype != 'plane'\
                                           and 'seq_id' in _factor and len(_factor['seq_id']) == 1\
                                           and (self.__reasons is None or 'non_poly_remap' not in self.__reasons):
                                            if chainId in MAJOR_ASYM_ID_SET:
                                                if seqId < 1 and len(self.__polySeq) == 1:
                                                    self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                                                        f"{chainId}:{seqId}:{compId}:{origAtomId} is not present in the coordinates. "\
                                                        f"The residue number '{seqId}' is not present in polymer sequence of chain {chainId} of the coordinates. "\
                                                        "Please update the sequence in the Macromolecules page.\n"
                                                else:
                                                    self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                                                        f"{chainId}:{seqId}:{compId}:{origAtomId} is not present in the coordinates.\n"

        return foundCompId

    def getOrigSeqId(self, ps, seqId, isPolySeq=True):
        # if self.__reasons is not None and 'label_seq_scheme' in self.__reasons and self.__reasons['label_seq_scheme'] or not self.__preferAuthSeq:
        if not self.__preferAuthSeq:
            chainId = ps['chain_id']
            offset = 0
            if isPolySeq and self.__reasons is not None and 'label_seq_offset' in self.__reasons and chainId in self.__reasons['label_seq_offset']:
                offset = self.__reasons['label_seq_offset'][chainId]
            seqKey = (ps['chain_id' if isPolySeq else 'auth_chain_id'], seqId)
            if seqKey in self.__authToLabelSeq:
                _chainId, _seqId = self.__authToLabelSeq[seqKey]
                if _seqId in ps['seq_id']:
                    return _seqId + offset
        if seqId in ps['auth_seq_id']:
            return seqId
        # if seqId in ps['seq_id']:
        #     return ps['auth_seq_id'][ps['seq_id'].index(seqId)]
        return seqId

    def getRealSeqId(self, ps, seqId, isPolySeq=True):
        # if self.__reasons is not None and 'label_seq_scheme' in self.__reasons and self.__reasons['label_seq_scheme'] or not self.__preferAuthSeq:
        if not self.__preferAuthSeq:
            chainId = ps['chain_id']
            offset = 0
            if isPolySeq and self.__reasons is not None and 'label_seq_offset' in self.__reasons and chainId in self.__reasons['label_seq_offset']:
                offset = self.__reasons['label_seq_offset'][chainId]
            seqKey = (ps['chain_id' if isPolySeq else 'auth_chain_id'], seqId + offset)
            if seqKey in self.__labelToAuthSeq:
                _chainId, _seqId = self.__labelToAuthSeq[seqKey]
                if _seqId in ps['auth_seq_id']:
                    return _seqId
        if seqId in ps['auth_seq_id']:
            return seqId
        # if seqId in ps['seq_id']:
        #     return ps['auth_seq_id'][ps['seq_id'].index(seqId)]
        return seqId

    def getRealChainId(self, chainId):
        if self.__reasons is not None and 'segment_id_mismatch' in self.__reasons and chainId in self.__reasons['segment_id_mismatch']:
            _chainId = self.__reasons['segment_id_mismatch'][chainId]
            if _chainId is not None:
                chainId = _chainId
        return chainId

    def updateSegmentIdDict(self, factor, chainId):
        if self.__reasons is not None or 'alt_chain_id' not in factor\
           or len(self.reasonsForReParsing) == 0 or 'segment_id_mismatch' not in self.reasonsForReParsing:
            return
        altChainId = factor['alt_chain_id']
        if altChainId not in self.reasonsForReParsing['segment_id_mismatch']:
            return
        if self.reasonsForReParsing['segment_id_mismatch'][altChainId] is not None:
            return
        self.reasonsForReParsing['segment_id_mismatch'][altChainId] = chainId

    def getCoordAtomSiteOf(self, chainId, seqId, cifCheck=True, asis=True):
        seqKey = (chainId, seqId)
        if asis:
            return seqKey, self.__coordAtomSite[seqKey] if cifCheck and seqKey in self.__coordAtomSite else None
        if seqKey in self.__labelToAuthSeq:
            seqKey = self.__labelToAuthSeq[seqKey]
            return seqKey, self.__coordAtomSite[seqKey] if cifCheck and seqKey in self.__coordAtomSite else None
        return seqKey, None

    def getAtomIdList(self, factor, compId, atomId):
        key = (compId, atomId, 'alt_atom_id' in factor)
        if key in self.__cachedDictForAtomIdList:
            return self.__cachedDictForAtomIdList[key]
        atomIds, _, details = self.__nefT.get_valid_star_atom_in_xplor(compId, atomId, leave_unmatched=True)
        if 'alt_atom_id' in factor and details is not None and len(atomId) > 1 and not atomId[-1].isalpha():
            atomIds, _, details = self.__nefT.get_valid_star_atom_in_xplor(compId, atomId[:-1], leave_unmatched=True)
            if atomId[-1].isdigit() and int(atomId[-1]) <= len(atomIds):
                atomIds = [atomIds[int(atomId[-1]) - 1]]

        if details is not None:
            _atomId = toNefEx(translateToStdAtomName(atomId, compId, ccU=self.__ccU))
            if _atomId != atomId:
                atomIds = self.__nefT.get_valid_star_atom_in_xplor(compId, _atomId)[0]
        self.__cachedDictForAtomIdList[key] = atomIds
        return atomIds

    def getLabelSeqOffsetDueToUnobs(self, ps):
        authChainId = ps['auth_chain_id']
        for labelSeqId, authSeqId in zip(ps['seq_id'], ps['auth_seq_id']):
            seqKey = (authChainId, authSeqId)
            if seqKey not in self.__coordUnobsRes:
                return labelSeqId - 1
        return ps['seq_id'][-1] - 1

    def doesNonPolySeqIdMatchWithPolySeqUnobs(self, chainId, seqId):
        _ps_ = next((_ps_ for _ps_ in self.__polySeq if _ps_['auth_chain_id'] == chainId), None)
        if _ps_ is not None:
            _chainId_ = _ps_['chain_id']
            _seqKey_ = (_chainId_, seqId)
            if _seqKey_ in self.__labelToAuthSeq:
                if self.__labelToAuthSeq[_seqKey_] != _seqKey_:
                    if self.__labelToAuthSeq[_seqKey_] in self.__coordUnobsRes:
                        return True
                else:
                    max_label_seq_id = _ps_['seq_id'][-1]
                    _seqId_ = seqId + 1
                    while _seqId_ <= max_label_seq_id:
                        if _seqId_ in _ps_['seq_id']:
                            _seqKey_ = (_chainId_, _seqId_)
                            if _seqKey_ in self.__labelToAuthSeq and self.__labelToAuthSeq[_seqKey_] != _seqKey_:
                                break
                        _seqId_ += 1
                    if _seqId_ not in _ps_['seq_id']:
                        min_label_seq_id = _ps_['seq_id'][0]
                        _seqId_ = seqId - 1
                        while _seqId_ >= min_label_seq_id:
                            if _seqId_ in _ps_['seq_id']:
                                _seqKey_ = (_chainId_, _seqId_)
                                if _seqKey_ in self.__labelToAuthSeq and self.__labelToAuthSeq[_seqKey_] != _seqKey_:
                                    break
                            _seqId_ -= 1
                    if _seqId_ in _ps_['seq_id']:
                        _seqKey_ = (_chainId_, _seqId_)
                        if _seqKey_ in self.__labelToAuthSeq and self.__labelToAuthSeq[_seqKey_] != _seqKey_:
                            __chainId__, __seqId__ = self.__labelToAuthSeq[_seqKey_]
                            __seqKey__ = (__chainId__, __seqId__ - (_seqId_ - seqId))
                            if __seqKey__ in self.__coordUnobsRes:
                                return True
        return False

    def intersectionFactor_expressions(self, atomSelection=None):
        self.consumeFactor_expressions(cifCheck=False)

        self.factor = self.__intersectionFactor_expressions(self.factor, atomSelection)

    def __intersectionFactor_expressions(self, _factor, atomSelection=None):  # pylint: disable=no-self-use
        if 'atom_selection' not in _factor:
            _factor['atom_selection'] = atomSelection
            return _factor

        if atomSelection is None or len(atomSelection) == 0:
            _factor['atom_selection'] = []

        elif isinstance(atomSelection[0], str) and atomSelection[0] == '*':
            return _factor

        _atomSelection = []
        for _atom in _factor['atom_selection']:
            if isinstance(_atom, str) and _atom == '*':
                _factor['atom_selection'] = atomSelection
                return _factor
            if _atom in atomSelection:
                _atomSelection.append(_atom)
            elif 'hydrogen_not_instantiated' in _atom and _atom['hydrogen_not_instantiated']:
                chain_id = _atom['chain_id']
                seq_id = _atom['seq_id']
                if any(_atom2 for _atom2 in atomSelection if _atom2['chain_id'] == chain_id and _atom2['seq_id'] == seq_id):
                    _atomSelection.append(_atom)

        _factor['atom_selection'] = _atomSelection

        return _factor

    def __intersectionAtom_selections(self, _selection1, _selection2):  # pylint: disable=no-self-use
        if _selection1 is None or len(_selection1) == 0 or _selection2 is None or len(_selection2) == 0:
            return []

        if isinstance(_selection2[0], str) and _selection2[0] == '*':
            return _selection1

        hasAuthSeqId1 = any(_atom for _atom in _selection1 if 'auth_atom_id' in _atom)
        hasAuthSeqId2 = any(_atom for _atom in _selection2 if 'auth_atom_id' in _atom)

        _atomSelection = []

        if not hasAuthSeqId1 and not hasAuthSeqId2:
            for _atom in _selection1:
                if isinstance(_atom, str) and _atom == '*':
                    return _selection2
                if _atom in _selection2:
                    _atomSelection.append(_atom)
                elif 'hydrogen_not_instantiated' in _atom and _atom['hydrogen_not_instantiated']:
                    chain_id = _atom['chain_id']
                    seq_id = _atom['seq_id']
                    if any(_atom2 for _atom2 in _selection2 if _atom2['chain_id'] == chain_id and _atom2['seq_id'] == seq_id):
                        _atomSelection.append(_atom)

        elif hasAuthSeqId1 and not hasAuthSeqId2:
            __selection1 = copy.deepcopy(_selection1)
            for _atom in __selection1:
                _atom.pop('auth_atom_id')
            for idx, _atom in enumerate(__selection1):
                if isinstance(_atom, str) and _atom == '*':
                    return _selection2
                if _atom in _selection2:
                    _atomSelection.append(_selection1[idx])
                elif 'hydrogen_not_instantiated' in _atom and _atom['hydrogen_not_instantiated']:
                    chain_id = _atom['chain_id']
                    seq_id = _atom['seq_id']
                    if any(_atom2 for _atom2 in _selection2 if _atom2['chain_id'] == chain_id and _atom2['seq_id'] == seq_id):
                        _atomSelection.append(_selection1[idx])

        elif not hasAuthSeqId1 and hasAuthSeqId2:
            __selection2 = copy.deepcopy(_selection2)
            for idx, _atom in enumerate(__selection2):
                _atom.pop('auth_atom_id')
            for idx, _atom in enumerate(__selection2):
                if isinstance(_atom, str) and _atom == '*':
                    return _selection1
                if _atom in _selection1:
                    _atomSelection.append(_selection2[idx])
                elif 'hydrogen_not_instantiated' in _atom and _atom['hydrogen_not_instantiated']:
                    chain_id = _atom['chain_id']
                    seq_id = _atom['seq_id']
                    if any(_atom1 for _atom1 in _selection1 if _atom1['chain_id'] == chain_id and _atom1['seq_id'] == seq_id):
                        _atomSelection.append(_selection2[idx])

        else:
            __selection1 = copy.deepcopy(_selection1)
            for _atom in __selection1:
                _atom.pop('auth_atom_id')
            __selection2 = copy.deepcopy(_selection2)
            for _atom in __selection2:
                _atom.pop('auth_atom_id')
            for idx, _atom in enumerate(__selection1):
                if isinstance(_atom, str) and _atom == '*':
                    return _selection2
                if _atom in __selection2:
                    _atomSelection.append(_selection1[idx])
                elif 'hydrogen_not_instantiated' in _atom and _atom['hydrogen_not_instantiated']:
                    chain_id = _atom['chain_id']
                    seq_id = _atom['seq_id']
                    if any(_atom2 for _atom2 in __selection2 if _atom2['chain_id'] == chain_id and _atom2['seq_id'] == seq_id):
                        _atomSelection.append(_selection1[idx])

        return _atomSelection

    # Enter a parse tree produced by CnsMRParser#factor.
    def enterFactor(self, ctx: CnsMRParser.FactorContext):
        if self.__sel_expr_debug:
            print("  " * self.depth + f"enter_factor, concatenation: {bool(ctx.factor())}")

        if ctx.Point():
            self.inVector3D = True
            self.inVector3D_columnSel = -1
            self.inVector3D_tail = None
            self.inVector3D_head = None
            self.vector3D = None

        self.depth += 1

    # Exit a parse tree produced by CnsMRParser#factor.
    def exitFactor(self, ctx: CnsMRParser.FactorContext):
        self.depth -= 1
        if self.__sel_expr_debug:
            print("  " * self.depth + "exit_factor")

        try:

            # concatenation
            if ctx.factor() and self.stackSelections:
                self.stackFactors.pop()
                self.factor = {'atom_selection': self.stackSelections.pop()}

            if ctx.All() or ctx.Known():
                clauseName = 'all' if ctx.All() else 'known'
                if self.__sel_expr_debug:
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
                                                          'value': self.__representativeModelId},
                                                         {'name': 'label_alt_id', 'type': 'enum',
                                                          'enum': ('A')}
                                                         ])

                    self.intersectionFactor_expressions(atomSelection)

                    if len(self.factor['atom_selection']) == 0:
                        self.factor['atom_id'] = [None]
                        self.warningMessage += f"[Insufficient atom selection] {self.__getCurrentRestraint()}"\
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
                        if 'alt_chain_id' in self.factor:
                            del self.factor['alt_chain_id']
                        if 'alt_atom_id' in self.factor:
                            del self.factor['alt_atom_id']

                except Exception as e:
                    if self.__verbose:
                        self.__lfh.write(f"+CnsMRParserListener.exitFactor() ++ Error  - {str(e)}\n")

            elif ctx.Around() or ctx.Saround():
                clauseName = 'around' if ctx.Around() else 'saround'
                if self.__sel_expr_debug:
                    print("  " * self.depth + f"--> {clauseName}")
                if not self.__hasCoord:
                    return
                if None in self.numberFSelection:
                    return
                around = self.numberFSelection[0]
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
                                                                  'value': self.__representativeModelId},
                                                                 {'name': 'label_alt_id', 'type': 'enum',
                                                                  'enum': ('A')}
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
                                                                  'value': self.__representativeModelId},
                                                                 {'name': 'label_alt_id', 'type': 'enum',
                                                                  'enum': ('A')}
                                                                 ])

                            if len(_neighbor) == 0:
                                continue

                            neighbor = [atom for atom in _neighbor if numpy.linalg.norm(toNpArray(atom) - origin) < around]

                            for atom in neighbor:
                                del atom['x']
                                del atom['y']
                                del atom['z']
                                _atomSelection.append(atom)

                        except Exception as e:
                            if self.__verbose:
                                self.__lfh.write(f"+CnsMRParserListener.exitFactor() ++ Error  - {str(e)}\n")

                    if ctx.Saround():
                        identity = numpy.identity(3, dtype=float)
                        zero = numpy.zeros(3, dtype=float)

                        oper_list = self.__cR.getDictList('pdbx_struct_oper_list')
                        if len(oper_list) > 0:
                            for oper in oper_list:
                                matrix = numpy.array([[float(oper['matrix[1][1]']), float(oper['matrix[1][2]']), float(oper['matrix[1][3]'])],
                                                     [float(oper['matrix[2][1]']), float(oper['matrix[2][2]']), float(oper['matrix[2][3]'])],
                                                     [float(oper['matrix[3][1]']), float(oper['matrix[3][2]']), float(oper['matrix[3][3]'])]], dtype=float)
                                vector = numpy.array([float(oper['vector[1]']), float(oper['vector[2]']), float(oper['vector[3]'])], dtype=float)

                                if numpy.array_equal(matrix, identity) and numpy.array_equal(vector, zero):
                                    continue

                                inv_matrix = numpy.linalg.inv(matrix)

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
                                                                              'value': self.__representativeModelId},
                                                                             {'name': 'label_alt_id', 'type': 'enum',
                                                                              'enum': ('A')}
                                                                             ])

                                        if len(_origin) != 1:
                                            continue

                                        origin = numpy.dot(inv_matrix, numpy.subtract(toNpArray(_origin[0]), vector))

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
                                                                              'value': self.__representativeModelId},
                                                                             {'name': 'label_alt_id', 'type': 'enum',
                                                                              'enum': ('A')}
                                                                             ])

                                        if len(_neighbor) == 0:
                                            continue

                                        neighbor = [atom for atom in _neighbor if numpy.linalg.norm(toNpArray(atom) - origin) < around]

                                        for atom in neighbor:
                                            del atom['x']
                                            del atom['y']
                                            del atom['z']
                                            _atomSelection.append(atom)

                                    except Exception as e:
                                        if self.__verbose:
                                            self.__lfh.write(f"+CnsMRParserListener.exitFactor() ++ Error  - {str(e)}\n")

                    if len(self.factor['atom_selection']) > 0:
                        self.factor['atom_selection'] = [dict(s) for s in set(frozenset(atom.items()) for atom in _atomSelection)]

                        if len(self.factor['atom_selection']) == 0:
                            self.factor['atom_id'] = [None]
                            self.warningMessage += f"[Insufficient atom selection] {self.__getCurrentRestraint()}"\
                                f"The {clauseName!r} clause has no effect.\n"

            elif ctx.Atom():
                if self.__sel_expr_debug:
                    print("  " * self.depth + "--> atom")
                if not self.__hasPolySeq:
                    return
                simpleNameIndex = simpleNamesIndex = 0  # these indices are necessary to deal with mixing case of 'Simple_name' and 'Simple_names'
                if ctx.Simple_name(0):
                    chainId = str(ctx.Simple_name(0))
                    self.factor['chain_id'] = [ps['auth_chain_id'] for ps in self.__polySeq
                                               if ps['auth_chain_id'] == self.getRealChainId(chainId)]
                    if self.__hasNonPolySeq:
                        for np in self.__nonPolySeq:
                            _chainId = np['auth_chain_id']
                            if _chainId == self.getRealChainId(chainId) and _chainId not in self.factor['chain_id']:
                                self.factor['chain_id'].append(_chainId)
                    if len(self.factor['chain_id']) > 0:
                        simpleNameIndex += 1

                if simpleNameIndex == 0 and ctx.Simple_names(0):
                    chainId = str(ctx.Simple_names(0))
                    _chainId = toRegEx(chainId)
                    self.factor['chain_id'] = [ps['auth_chain_id'] for ps in self.__polySeq
                                               if re.match(_chainId, ps['auth_chain_id'])]
                    if self.__hasNonPolySeq:
                        for np in self.__nonPolySeq:
                            __chainId = np['auth_chain_id']
                            if re.match(_chainId, __chainId) and __chainId not in self.factor['chain_id']:
                                self.factor['chain_id'].append(__chainId)
                    simpleNamesIndex += 1

                if len(self.factor['chain_id']) == 0:
                    if len(self.__polySeq) == 1:
                        self.factor['chain_id'] = self.__polySeq[0]['chain_id']
                        self.factor['auth_chain_id'] = chainId
                    elif self.__reasons is not None:
                        self.factor['atom_id'] = [None]
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            "Couldn't specify segment name "\
                            f"'{chainId}' the coordinates.\n"  # do not use 'chainId!r' expression, '%' code throws ValueError
                    else:
                        if 'segment_id_mismatch' not in self.reasonsForReParsing:
                            self.reasonsForReParsing['segment_id_mismatch'] = {}
                        if chainId not in self.reasonsForReParsing['segment_id_mismatch']:
                            self.reasonsForReParsing['segment_id_mismatch'][chainId] = None
                        self.factor['alt_chain_id'] = chainId

                if ctx.Integer(0):
                    self.factor['seq_id'] = [int(str(ctx.Integer(0)))]

                if ctx.Integers():
                    seqId = str(ctx.Integers())
                    _seqId = toRegEx(seqId)
                    _seqIdSelect = set()
                    for chainId in self.factor['chain_id']:
                        ps = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chainId), None)
                        if ps is not None:
                            found = False
                            for realSeqId in ps['auth_seq_id']:
                                realSeqId = self.getRealSeqId(ps, realSeqId)
                                if re.match(_seqId, str(realSeqId)):
                                    _seqIdSelect.add(realSeqId)
                                    found = True
                            if not found:
                                for realSeqId in ps['auth_seq_id']:
                                    realSeqId = self.getRealSeqId(ps, realSeqId)
                                    seqKey = (chainId, realSeqId)
                                    if seqKey in self.__authToLabelSeq:
                                        _, realSeqId = self.__authToLabelSeq[seqKey]
                                        if re.match(_seqId, str(realSeqId)):
                                            _seqIdSelect.add(realSeqId)
                    if self.__hasNonPolySeq:
                        for chainId in self.factor['chain_id']:
                            npList = [np for np in self.__nonPolySeq if np['auth_chain_id'] == chainId]
                            for np in npList:
                                found = False
                                for realSeqId in np['auth_seq_id']:
                                    realSeqId = self.getRealSeqId(np, realSeqId, False)
                                    if re.match(_seqId, str(realSeqId)):
                                        _seqIdSelect.add(realSeqId)
                                        found = True
                                if not found:
                                    for realSeqId in np['auth_seq_id']:
                                        realSeqId = self.getRealSeqId(np, realSeqId, False)
                                        seqKey = (chainId, realSeqId)
                                        if seqKey in self.__authToLabelSeq:
                                            _, realSeqId = self.__authToLabelSeq[seqKey]
                                            if re.match(_seqId, str(realSeqId)):
                                                _seqIdSelect.add(realSeqId)
                    self.factor['seq_id'] = list(_seqIdSelect)

                _atomIdSelect = set()
                if ctx.Simple_name(simpleNameIndex):
                    atomId = str(ctx.Simple_name(simpleNameIndex))
                    for chainId in self.factor['chain_id']:
                        ps = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chainId), None)
                        if ps is None:
                            continue
                        for seqId in self.factor['seq_id']:
                            if seqId in ps['auth_seq_id']:
                                seqId = self.getRealSeqId(ps, seqId)
                                compId = ps['comp_id'][ps['auth_seq_id'].index(seqId)]
                                if self.__ccU.updateChemCompDict(compId):
                                    if any(cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == atomId):
                                        _atomIdSelect.add(atomId)
                    if self.__hasNonPolySeq:
                        for chainId in self.factor['chain_id']:
                            npList = [np for np in self.__nonPolySeq if np['auth_chain_id'] == chainId]
                            for np in npList:
                                for seqId in self.factor['seq_id']:
                                    if seqId in np['auth_seq_id']:
                                        seqId = self.getRealSeqId(np, seqId, False)
                                        compId = np['comp_id'][np['auth_seq_id'].index(seqId)]
                                        if self.__ccU.updateChemCompDict(compId):
                                            if any(cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == atomId):
                                                _atomIdSelect.add(atomId)

                elif ctx.Simple_names(simpleNamesIndex):
                    atomId = translateToStdAtomName(str(ctx.Simple_names(simpleNamesIndex)),
                                                    None if 'comp_id' not in self.factor else self.factor['comp_id'][0],
                                                    ccU=self.__ccU)
                    _atomId = toRegEx(atomId)
                    for chainId in self.factor['chain_id']:
                        ps = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chainId), None)
                        if ps is None:
                            continue
                        for seqId in self.factor['seq_id']:
                            if seqId in ps['auth_seq_id']:
                                seqId = self.getRealSeqId(ps, seqId)
                                compId = ps['comp_id'][ps['auth_seq_id'].index(seqId)]
                                if self.__ccU.updateChemCompDict(compId):
                                    for cca in self.__ccU.lastAtomList:
                                        if cca[self.__ccU.ccaLeavingAtomFlag] != 'Y':
                                            realAtomId = cca[self.__ccU.ccaAtomId]
                                            if re.match(_atomId, realAtomId):
                                                _atomIdSelect.add(realAtomId)
                    if self.__hasNonPolySeq:
                        for chainId in self.factor['chain_id']:
                            npList = [np for np in self.__nonPolySeq if np['auth_chain_id'] == chainId]
                            for np in npList:
                                for seqId in self.factor['seq_id']:
                                    if seqId in np['auth_seq_id']:
                                        seqId = self.getRealSeqId(np, seqId, False)
                                        compId = np['comp_id'][np['auth_seq_id'].index(seqId)]
                                        if self.__ccU.updateChemCompDict(compId):
                                            for cca in self.__ccU.lastAtomList:
                                                if cca[self.__ccU.ccaLeavingAtomFlag] != 'Y':
                                                    realAtomId = cca[self.__ccU.ccaAtomId]
                                                    if re.match(_atomId, realAtomId):
                                                        _atomIdSelect.add(realAtomId)

                self.factor['atom_id'] = list(_atomIdSelect)

                self.consumeFactor_expressions("'atom' clause", False)

            elif ctx.Attribute():
                if self.__sel_expr_debug:
                    print("  " * self.depth + "--> attribute")
                if not self.__hasCoord:
                    return
                absolute = bool(ctx.Abs())
                _attr_prop = str(ctx.Attr_properties())
                attr_prop = _attr_prop.lower()
                opCode = str(ctx.Comparison_ops())
                if None in self.numberFSelection:
                    return
                attr_value = self.numberFSelection[0]

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
                                                          'value': self.__representativeModelId},
                                                         {'name': 'label_alt_id', 'type': 'enum',
                                                          'enum': ('A')}
                                                         ])

                    self.intersectionFactor_expressions(atomSelection)

                elif attr_prop.startswith('bcom')\
                        or attr_prop.startswith('qcom')\
                        or attr_prop.startswith('xcom')\
                        or attr_prop.startswith('ycom')\
                        or attr_prop.startswith('zcom'):  # BCOMP, QCOMP, XCOMP, YCOMP, ZCOM`
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Unsupported data] {self.__getCurrentRestraint()}"\
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
                                                          'value': self.__representativeModelId},
                                                         {'name': 'label_alt_id', 'type': 'enum',
                                                          'enum': ('A')}
                                                         ])

                    self.intersectionFactor_expressions(atomSelection)

                elif attr_prop in ('dx', 'dy', 'dz', 'harm'):
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Unsupported data] {self.__getCurrentRestraint()}"\
                        f"The attribute property {_attr_prop!r} "\
                        "related to atomic force of each atom is not possessed in the static coordinate file.\n"
                    validProp = False

                elif attr_prop.startswith('fbet'):  # FBETA
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Unsupported data] {self.__getCurrentRestraint()}"\
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
                                                        [{'name': 'type_symbol', 'type': 'enum',
                                                          'enum': _typeSymbolSelect},
                                                         {'name': self.__modelNumName, 'type': 'int',
                                                          'value': self.__representativeModelId},
                                                         {'name': 'label_alt_id', 'type': 'enum',
                                                          'enum': ('A')}
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
                                                          'value': self.__representativeModelId},
                                                         {'name': 'label_alt_id', 'type': 'enum',
                                                          'enum': ('A')}
                                                         ])

                    self.intersectionFactor_expressions(atomSelection)

                elif attr_prop.startswith('scatter'):  # scatter_[ab][1-4], scatter_c, scatter_fp, scatter_fdp
                    self.warningMessage += f"[Unsupported data] {self.__getCurrentRestraint()}"\
                        f"The attribute property {_attr_prop!r} "\
                        "related to X-ray scattering power of each atom is not possessed in the static coordinate file.\n"
                    validProp = False

                elif attr_prop in ('refx', 'refy', 'refz', 'rmsd'):
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Unsupported data] {self.__getCurrentRestraint()}"\
                        f"The attribute property {_attr_prop!r} "\
                        "requires a reference coordinate set.\n"
                    validProp = False

                elif attr_prop == ('vx', 'vy', 'vz'):
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Unsupported data] {self.__getCurrentRestraint()}"\
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
                                                          'value': self.__representativeModelId},
                                                         {'name': 'label_alt_id', 'type': 'enum',
                                                          'enum': ('A')}
                                                         ])

                    self.intersectionFactor_expressions(atomSelection)

                elif attr_prop.startswith('store'):
                    store_id = int(attr_prop[-1])
                    self.factor['atom_id'] = [None]
                    if len(self.storeSet[store_id]) == 0:
                        self.warningMessage += f"[Unsupported data] {self.__getCurrentRestraint()}"\
                            f"The 'store{store_id}' clause has no effect "\
                            "because the internal vector statement is not set.\n"
                        validProp = False

                if validProp and len(self.factor['atom_selection']) == 0:
                    self.factor['atom_id'] = [None]
                    _absolute = ' abs' if absolute else ''
                    self.warningMessage += f"[Insufficient atom selection] {self.__getCurrentRestraint()}"\
                        f"The 'attribute' clause ('{_attr_prop}{_absolute} {opCode} {attr_value}') has no effect.\n"

            elif ctx.BondedTo():
                if self.__sel_expr_debug:
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
                                    ps = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chainId), None)
                                    if ps is not None and seqId in ps['auth_seq_id'] and ps['comp_id'][ps['auth_seq_id'].index(seqId)] == compId:
                                        seqId = self.getRealSeqId(ps, seqId)
                                        if any(cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId):
                                            _atomSelection.append({'chain_id': chainId, 'seq_id': seqId, 'comp_id': compId, 'atom_id': _atomId})
                                    if self.__hasNonPolySeq:
                                        npList = [np for np in self.__nonPolySeq if np['auth_chain_id'] == chainId]
                                        for np in npList:
                                            if seqId in np['auth_seq_id'] and np['comp_id'][np['auth_seq_id'].index(seqId)] == compId:
                                                seqId = self.getRealSeqId(np, seqId, False)
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
                                                                      'value': self.__representativeModelId},
                                                                     {'name': 'label_alt_id', 'type': 'enum',
                                                                      'enum': ('A')}
                                                                     ])

                                if len(_origin) == 1:
                                    origin = toNpArray(_origin[0])

                                    ps = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chainId), None)
                                    if ps is not None:
                                        for _seqId in [seqId - 1, seqId + 1]:
                                            if _seqId in ps['auth_seq_id']:
                                                _seqId = self.getRealSeqId(ps, _seqId)
                                                _compId = ps['comp_id'][ps['auth_seq_id'].index(_seqId)]
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
                                                                                              'value': self.__representativeModelId},
                                                                                             {'name': 'label_alt_id', 'type': 'enum',
                                                                                              'enum': ('A')}
                                                                                             ])

                                                        if len(_neighbor) != 1:
                                                            continue

                                                        if numpy.linalg.norm(toNpArray(_neighbor[0]) - origin) < 2.5:
                                                            _atomSelection.append({'chain_id': chainId, 'seq_id': _seqId, 'comp_id': _compId, 'atom_id': _atomId})

                                    if self.__hasNonPolySeq:
                                        npList = [np for np in self.__nonPolySeq if np['auth_chain_id'] == chainId]
                                        for np in npList:
                                            for _seqId in [seqId - 1, seqId + 1]:
                                                if _seqId in np['auth_seq_id']:
                                                    _seqId = self.getRealSeqId(np, _seqId, False)
                                                    _compId = np['comp_id'][np['auth_seq_id'].index(_seqId)]
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
                                                                                                  'value': self.__representativeModelId},
                                                                                                 {'name': 'label_alt_id', 'type': 'enum',
                                                                                                  'enum': ('A')}
                                                                                                 ])

                                                            if len(_neighbor) != 1:
                                                                continue

                                                            if numpy.linalg.norm(toNpArray(_neighbor[0]) - origin) < 2.5:
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
                                                                  'value': self.__representativeModelId}
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
                                                                  'value': self.__representativeModelId}
                                                                 ])

                        if len(_atom) == 1:
                            _atomSelection.append(_atom[0])

                    self.factor['atom_selection'] = [dict(s) for s in set(frozenset(atom.items()) for atom in _atomSelection)]

                    if len(self.factor['atom_selection']) == 0:
                        self.factor['atom_id'] = [None]
                        self.warningMessage += f"[Insufficient atom selection] {self.__getCurrentRestraint()}"\
                            "The 'bondedto' clause has no effect.\n"

                else:
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Insufficient atom selection] {self.__getCurrentRestraint()}"\
                        "The 'bondedto' clause has no effect because no atom is selected.\n"

            elif ctx.ByGroup():
                if self.__sel_expr_debug:
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
                                                                      'value': self.__representativeModelId},
                                                                     {'name': 'label_alt_id', 'type': 'enum',
                                                                      'enum': ('A')}
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
                                                                              'value': self.__representativeModelId},
                                                                             {'name': 'label_alt_id', 'type': 'enum',
                                                                              'enum': ('A')}
                                                                             ])

                                        if len(_neighbor) != 1:
                                            continue

                                        if numpy.linalg.norm(toNpArray(_neighbor[0]) - origin) < 2.0:
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

                                                if numpy.linalg.norm(toNpArray(_neighbor) - origin) < 2.0:
                                                    _atomSelection.append({'chain_id': chainId, 'seq_id': seqId, 'comp_id': compId, 'atom_id': _atomId})

                    atomSelection = [dict(s) for s in set(frozenset(atom.items()) for atom in _atomSelection)]

                    if len(atomSelection) <= len(self.factor['atom_selection']):
                        self.factor['atom_id'] = [None]
                        self.warningMessage += f"[Insufficient atom selection] {self.__getCurrentRestraint()}"\
                            "The 'bygroup' clause has no effect.\n"

                    self.factor['atom_selection'] = atomSelection

                else:
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Insufficient atom selection] {self.__getCurrentRestraint()}"\
                        "The 'bygroup' clause has no effect because no atom is selected.\n"

            elif ctx.ByRes():
                if self.__sel_expr_debug:
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
                                                              'value': self.__representativeModelId},
                                                             {'name': 'label_alt_id', 'type': 'enum',
                                                              'enum': ('A')}
                                                             ])

                        if len(_atomByRes) > 0 and _atomByRes[0]['comp_id'] == compId:
                            for _atom in _atomByRes:
                                _atomSelection.append({'chain_id': chainId, 'seq_id': seqId, 'comp_id': _atom['comp_id'], 'atom_id': _atom['atom_id']})

                        else:
                            ps = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chainId), None)
                            if ps is not None and seqId in ps['auth_seq_id'] and ps['comp_id'][ps['auth_seq_id'].index(seqId)] == compId:
                                seqId = self.getRealSeqId(ps, seqId)
                                if self.__ccU.updateChemCompDict(compId):
                                    atomIds = [cca[self.__ccU.ccaAtomId] for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaLeavingAtomFlag] != 'Y']
                                    for atomId in atomIds:
                                        _atomSelection.append({'chain_id': chainId, 'seq_id': seqId, 'comp_id': compId, 'atom_id': atomId})
                            if self.__hasNonPolySeq:
                                npList = [np for np in self.__nonPolySeq if np['auth_chain_id'] == chainId]
                                for np in npList:
                                    if seqId in np['auth_seq_id'] and np['comp_id'][np['auth_seq_id'].index(seqId)] == compId:
                                        seqId = self.getRealSeqId(np, seqId, False)
                                        if self.__ccU.updateChemCompDict(compId):
                                            atomIds = [cca[self.__ccU.ccaAtomId] for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaLeavingAtomFlag] != 'Y']
                                            for atomId in atomIds:
                                                _atomSelection.append({'chain_id': chainId, 'seq_id': seqId, 'comp_id': compId, 'atom_id': atomId})

                    self.factor['atom_selection'] = [dict(s) for s in set(frozenset(atom.items()) for atom in _atomSelection)]

                    if len(self.factor['atom_selection']) == 0:
                        self.factor['atom_id'] = [None]
                        self.warningMessage += f"[Insufficient atom selection] {self.__getCurrentRestraint()}"\
                            "The 'byres' clause has no effect.\n"

                else:
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Insufficient atom selection] {self.__getCurrentRestraint()}"\
                        "The 'byres' clause has no effect because no atom is selected.\n"

            elif ctx.Chemical():
                if self.__sel_expr_debug:
                    print("  " * self.depth + "--> chemical")
                if ctx.Colon():  # range expression
                    self.factor['type_symbols'] = [str(ctx.Simple_name(0)), str(ctx.Simple_name(1))]

                elif ctx.Simple_name(0):
                    self.factor['type_symbol'] = [str(ctx.Simple_name(0))]

                elif ctx.Simple_names(0):
                    self.factor['type_symbols'] = [str(ctx.Simple_names(0))]

                elif ctx.Symbol_name():
                    symbol_name = str(ctx.Symbol_name())
                    if symbol_name in self.evaluate:
                        val = self.evaluate[symbol_name]
                        if isinstance(val, list):
                            self.factor['type_symbol'] = val
                        else:
                            self.factor['type_symbol'] = [val]
                    elif symbol_name in self.evaluateFor:
                        val = self.evaluateFor[symbol_name]
                        if isinstance(val, list):
                            self.factor['type_symbol'] = val
                        else:
                            self.factor['type_symbol'] = [val]
                    else:
                        self.warningMessage += f"[Unsupported data] {self.__getCurrentRestraint()}"\
                            f"The symbol {symbol_name!r} is not defined.\n"

                self.consumeFactor_expressions("'chemical' clause", False)

            elif ctx.Hydrogen():
                if self.__sel_expr_debug:
                    print("  " * self.depth + "--> hydrogen")
                if not self.__hasCoord:
                    return
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

            elif ctx.Fbox() or ctx.Sfbox():
                clauseName = 'fbox' if ctx.Fbox() else 'sfbox'
                if self.__sel_expr_debug:
                    print("  " * self.depth + f"--> {clauseName}")
                if not self.__hasCoord:
                    return
                if None in self.numberFSelection:
                    return
                xmin = self.numberFSelection[0]
                xmax = self.numberFSelection[1]
                ymin = self.numberFSelection[2]
                ymax = self.numberFSelection[3]
                zmin = self.numberFSelection[4]
                zmax = self.numberFSelection[5]

                try:

                    _atomSelection =\
                        self.__cR.getDictListWithFilter('atom_site',
                                                        [{'name': 'auth_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                                         {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                                         {'name': 'label_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                         {'name': 'label_atom_id', 'type': 'str', 'alt_name': 'atom_id'}
                                                         ],
                                                        [{'name': 'Cartn_x', 'type': 'range-float',
                                                          'range': {'min_exclusive': xmin,
                                                                    'max_exclusive': xmax}},
                                                         {'name': 'Cartn_y', 'type': 'range-float',
                                                          'range': {'min_exclusive': ymin,
                                                                    'max_exclusive': ymax}},
                                                         {'name': 'Cartn_z', 'type': 'range-float',
                                                          'range': {'min_exclusive': zmin,
                                                                    'max_exclusive': zmax}},
                                                         {'name': self.__modelNumName, 'type': 'int',
                                                          'value': self.__representativeModelId},
                                                         {'name': 'label_alt_id', 'type': 'enum',
                                                          'enum': ('A')}
                                                         ])

                except Exception as e:
                    if self.__verbose:
                        self.__lfh.write(f"+CnsMRParserListener.exitFactor() ++ Error  - {str(e)}\n")

                if ctx.Sfbox():
                    identity = numpy.identity(3, dtype=float)
                    zero = numpy.zeros(3, dtype=float)

                    oper_list = self.__cR.getDictList('pdbx_struct_oper_list')
                    if len(oper_list) > 0:
                        for oper in oper_list:
                            matrix = numpy.array([[float(oper['matrix[1][1]']), float(oper['matrix[1][2]']), float(oper['matrix[1][3]'])],
                                                 [float(oper['matrix[2][1]']), float(oper['matrix[2][2]']), float(oper['matrix[2][3]'])],
                                                 [float(oper['matrix[3][1]']), float(oper['matrix[3][2]']), float(oper['matrix[3][3]'])]], dtype=float)
                            vector = numpy.array([float(oper['vector[1]']), float(oper['vector[2]']), float(oper['vector[3]'])], dtype=float)

                            if numpy.array_equal(matrix, identity) and numpy.array_equal(vector, zero):
                                continue

                            try:

                                __atomSelection =\
                                    self.__cR.getDictListWithFilter('atom_site',
                                                                    [{'name': 'auth_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                                                     {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                                                     {'name': 'label_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                                     {'name': 'label_atom_id', 'type': 'str', 'alt_name': 'atom_id'},
                                                                     {'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                                     {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                                     {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                                                                     ],
                                                                    [{'name': self.__modelNumName, 'type': 'int',
                                                                      'value': self.__representativeModelId},
                                                                     {'name': 'label_alt_id', 'type': 'enum',
                                                                      'enum': ('A')}
                                                                     ])

                                for atom in __atomSelection:
                                    origin = toNpArray(atom)
                                    mv = numpy.dot(matrix, numpy.add(origin, vector))

                                    if xmin < mv[0] < xmax\
                                       and ymin < mv[1] < ymax\
                                       and zmin < mv[2] < zmax:
                                        del atom['x']
                                        del atom['y']
                                        del atom['z']
                                        _atomSelection.append(atom)

                            except Exception as e:
                                if self.__verbose:
                                    self.__lfh.write(f"+CnsMRParserListener.exitFactor() ++ Error  - {str(e)}\n")

                self.factor['atom_selection'] = [dict(s) for s in set(frozenset(atom.items()) for atom in _atomSelection)]

                if len(self.factor['atom_selection']) == 0:
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Insufficient atom selection] {self.__getCurrentRestraint()}"\
                        f"The {clauseName!r} clause has no effect.\n"

            elif ctx.Id():
                if self.__sel_expr_debug:
                    print("  " * self.depth + "--> id")
                self.factor['atom_id'] = [None]
                self.warningMessage += f"[Unsupported data] {self.__getCurrentRestraint()}"\
                    "The 'id' clause has no effect "\
                    "because the internal atom number is not included in the coordinate file.\n"

            elif ctx.Name():
                if self.__sel_expr_debug:
                    print("  " * self.depth + "--> name")

                eval_factor = False
                if 'atom_id' in self.factor or 'atom_ids' in self.factor:
                    __factor = copy.copy(self.factor)
                    self.consumeFactor_expressions("'name' clause", False)
                    eval_factor = True

                if ctx.Colon():  # range expression
                    if ctx.Simple_name(0):
                        begAtomId = str(ctx.Simple_name(0))
                    elif ctx.Double_quote_string(0):
                        begAtomId = str(ctx.Double_quote_string(0)).strip('"').strip()
                        if len(begAtomId) == 0:
                            return
                    if ctx.Simple_name(1):
                        endAtomId = str(ctx.Simple_name(1))
                    elif ctx.Double_quote_string(1):
                        endAtomId = str(ctx.Double_quote_string(1)).strip('"').strip()
                        if len(endAtomId) == 0:
                            return
                    self.factor['atom_ids'] = [begAtomId, endAtomId]

                elif ctx.Simple_name(0) or ctx.Double_quote_string(0):
                    if ctx.Simple_name(0):
                        self.factor['atom_id'] = [str(ctx.Simple_name(0))]
                    elif ctx.Double_quote_string(0):
                        self.factor['atom_id'] = [str(ctx.Double_quote_string(0)).strip('"').strip()]

                elif ctx.Simple_names(0):
                    self.factor['atom_ids'] = [str(ctx.Simple_names(0))]

                elif ctx.Symbol_name():
                    symbol_name = str(ctx.Symbol_name())
                    if symbol_name in self.evaluate:
                        val = self.evaluate[symbol_name]
                        if isinstance(val, list):
                            self.factor['atom_id'] = val
                        else:
                            self.factor['atom_id'] = [val]
                    elif symbol_name in self.evaluateFor:
                        val = self.evaluateFor[symbol_name]
                        if isinstance(val, list):
                            self.factor['atom_id'] = val
                        else:
                            self.factor['atom_id'] = [val]
                    else:
                        self.warningMessage += f"[Unsupported data] {self.__getCurrentRestraint()}"\
                            f"The symbol {symbol_name!r} is not defined.\n"

                if eval_factor and 'atom_selection' in self.factor:
                    if len(self.factor['atom_selection']) == 0:
                        if self.__with_axis and __factor['atom_id'][0] in XPLOR_RDC_PRINCIPAL_AXIS_NAMES:
                            pass
                        elif self.__cur_subtype == 'plane':
                            pass
                        elif self.__cur_subtype == 'dist' and 'atom_id' in __factor and __factor['atom_id'][0] in XPLOR_NITROXIDE_NAMES:
                            pass
                        else:
                            _factor = copy.copy(self.factor)
                            if 'atom_selection' in __factor:
                                del __factor['atom_selection']
                            del _factor['atom_selection']
                            self.warningMessage += f"[Insufficient atom selection] {self.__getCurrentRestraint()}"\
                                f"The 'name' clause has no effect for a conjunction of factor {__factor} and {_factor}.\n"

            elif ctx.NONE():
                if self.__sel_expr_debug:
                    print("  " * self.depth + "--> none")
                self.factor['atom_selection'] = []

            elif ctx.Not_op():
                if self.__sel_expr_debug:
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
                                                          'value': self.__representativeModelId},
                                                         {'name': 'label_alt_id', 'type': 'enum',
                                                          'enum': ('A')}
                                                         ])

                except Exception as e:
                    if self.__verbose:
                        self.__lfh.write(f"+CnsMRParserListener.exitFactor() ++ Error  - {str(e)}\n")

                if 'atom_selection' not in self.factor:
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Insufficient atom selection] {self.__getCurrentRestraint()}"\
                        "The 'not' clause has no effect.\n"
                else:
                    _refAtomSelection = [atom for atom in self.factor['atom_selection'] if atom in _atomSelection]
                    self.factor['atom_selection'] = [atom for atom in _atomSelection if atom not in _refAtomSelection]

                    if len(self.factor['atom_selection']) == 0:
                        self.factor['atom_id'] = [None]
                        self.warningMessage += f"[Insufficient atom selection] {self.__getCurrentRestraint()}"\
                            "The 'not' clause has no effect.\n"

            elif ctx.Point():
                if self.__sel_expr_debug:
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
                                                                  'value': self.__representativeModelId},
                                                                 {'name': 'label_alt_id', 'type': 'enum',
                                                                  'enum': ('A')}
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
                                                                          'value': self.__representativeModelId},
                                                                         {'name': 'label_alt_id', 'type': 'enum',
                                                                          'enum': ('A')}
                                                                         ])

                                    if len(_head) == 1:
                                        head = toNpArray(_head[0])
                                        self.vector3D = numpy.subtract(tail, head, dtype=float)

                        except Exception as e:
                            if self.__verbose:
                                self.__lfh.write(f"+CnsMRParserListener.exitFactor() ++ Error  - {str(e)}\n")

                    self.inVector3D_tail = self.inVector3D_head = None
                    if None in self.numberFSelection:
                        return
                    cut = self.numberFSelection[0]

                else:
                    if None in self.numberFSelection:
                        return
                    self.vector3D = [self.numberFSelection[0], self.numberFSelection[1], self.numberFSelection[2]]
                    cut = self.numberFSelection[3]

                if self.vector3D is None:
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Insufficient atom selection] {self.__getCurrentRestraint()}"\
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
                                                              'value': self.__representativeModelId},
                                                             {'name': 'label_alt_id', 'type': 'enum',
                                                              'enum': ('A')}
                                                             ])

                        if len(_neighbor) > 0:
                            neighbor = [atom for atom in _neighbor if numpy.linalg.norm(toNpArray(atom) - self.vector3D) < cut]

                            for atom in neighbor:
                                del atom['x']
                                del atom['y']
                                del atom['z']
                                atomSelection.append(atom)

                    except Exception as e:
                        if self.__verbose:
                            self.__lfh.write(f"+CnsMRParserListener.exitFactor() ++ Error  - {str(e)}\n")

                    self.factor['atom_selection'] = atomSelection

                    if len(self.factor['atom_selection']) == 0:
                        self.factor['atom_id'] = [None]
                        self.warningMessage += f"[Insufficient atom selection] {self.__getCurrentRestraint()}"\
                            "The 'cut' clause has no effect.\n"

                self.inVector3D = False
                self.vector3D = None

            elif ctx.Previous():
                if self.__sel_expr_debug:
                    print("  " * self.depth + "--> previous")
                self.factor['atom_id'] = [None]
                self.warningMessage += f"[Unsupported data] {self.__getCurrentRestraint()}"\
                    "The 'previous' clause has no effect "\
                    "because the internal atom selection is fragile in the restraint file.\n"

            elif ctx.Pseudo():
                if self.__sel_expr_debug:
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
                                                          'value': self.__representativeModelId},
                                                         {'name': 'label_alt_id', 'type': 'enum',
                                                          'enum': ('A')}
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
                    if self.__verbose:
                        self.__lfh.write(f"+CnsMRParserListener.exitFactor() ++ Error  - {str(e)}\n")

                self.intersectionFactor_expressions(atomSelection)

                if len(self.factor['atom_selection']) == 0:
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Insufficient atom selection] {self.__getCurrentRestraint()}"\
                        "The 'pseudo' clause has no effect.\n"

            elif ctx.Residue():
                if self.__sel_expr_debug:
                    print("  " * self.depth + "--> residue")

                eval_factor = False
                if 'seq_id' in self.factor or 'seq_ids' in self.factor:
                    __factor = copy.copy(self.factor)
                    self.consumeFactor_expressions("'residue' clause", False)
                    eval_factor = True

                if ctx.Colon():  # range expression
                    self.factor['seq_id'] = list(range(int(str(ctx.Integer(0))), int(str(ctx.Integer(0))) + 1))

                elif ctx.Integer(0):
                    self.factor['seq_id'] = [int(str(ctx.Integer(0)))]

                elif ctx.Integers():
                    self.factor['seq_ids'] = [str(ctx.Integers())]

                elif ctx.Symbol_name():
                    symbol_name = str(ctx.Symbol_name())
                    if symbol_name in self.evaluate:
                        val = self.evaluate[symbol_name]
                        if isinstance(val, list):
                            self.factor['seq_id'] = [v if isinstance(v, int) else int(v) for v in val]
                        else:
                            self.factor['seq_id'] = [val if isinstance(val, int) else int(val)]
                    elif symbol_name in self.evaluateFor:
                        val = self.evaluateFor[symbol_name]
                        if isinstance(val, list):
                            self.factor['seq_id'] = [v if isinstance(v, int) else int(v) for v in val]
                        else:
                            self.factor['seq_id'] = [val if isinstance(val, int) else int(val)]
                    else:
                        self.warningMessage += f"[Unsupported data] {self.__getCurrentRestraint()}"\
                            f"The symbol {symbol_name!r} is not defined.\n"

                if eval_factor and 'atom_selection' in self.factor:
                    if len(self.factor['atom_selection']) == 0:
                        if self.__with_axis and 'atom_id' in __factor and __factor['atom_id'][0] in XPLOR_RDC_PRINCIPAL_AXIS_NAMES:
                            pass
                        elif self.__cur_subtype == 'plane':
                            pass
                        elif self.__cur_subtype == 'dist' and 'atom_id' in __factor and __factor['atom_id'][0] in XPLOR_NITROXIDE_NAMES:
                            pass
                        else:
                            _factor = copy.copy(self.factor)
                            if 'atom_selection' in __factor:
                                del __factor['atom_selection']
                            del _factor['atom_selection']
                            self.warningMessage += f"[Insufficient atom selection] {self.__getCurrentRestraint()}"\
                                f"The 'residue' clause has no effect for a conjunction of factor {__factor} and {_factor}.\n"

            elif ctx.Resname():
                if self.__sel_expr_debug:
                    print("  " * self.depth + "--> resname")

                eval_factor = False
                if 'comp_id' in self.factor or 'comp_ids' in self.factor:
                    __factor = copy.copy(self.factor)
                    self.consumeFactor_expressions("'resname' clause", False)
                    eval_factor = True

                if ctx.Colon():  # range expression
                    self.factor['comp_ids'] = [str(ctx.Simple_name(0)), str(ctx.Simple_name(1))]

                elif ctx.Simple_name(0):
                    self.factor['comp_id'] = [str(ctx.Simple_name(0))]

                elif ctx.Simple_names(0):
                    self.factor['comp_ids'] = [str(ctx.Simple_names(0))]

                elif ctx.Symbol_name():
                    symbol_name = str(ctx.Symbol_name())
                    if symbol_name in self.evaluate:
                        val = self.evaluate[symbol_name]
                        if isinstance(val, list):
                            self.factor['comp_id'] = val
                        else:
                            self.factor['comp_id'] = [val]
                    elif symbol_name in self.evaluateFor:
                        val = self.evaluateFor[symbol_name]
                        if isinstance(val, list):
                            self.factor['comp_id'] = val
                        else:
                            self.factor['comp_id'] = [val]
                    else:
                        self.warningMessage += f"[Unsupported data] {self.__getCurrentRestraint()}"\
                            f"The symbol {symbol_name!r} is not defined.\n"

                if eval_factor and 'atom_selection' in self.factor:
                    if len(self.factor['atom_selection']) == 0:
                        if self.__with_axis and 'atom_id' in __factor and __factor['atom_id'][0] in XPLOR_RDC_PRINCIPAL_AXIS_NAMES:
                            pass
                        elif self.__cur_subtype == 'plane':
                            pass
                        elif self.__cur_subtype == 'dist' and 'atom_id' in __factor and __factor['atom_id'][0] in XPLOR_NITROXIDE_NAMES:
                            pass
                        else:
                            _factor = copy.copy(self.factor)
                            if 'atom_selection' in __factor:
                                del __factor['atom_selection']
                            del _factor['atom_selection']
                            self.warningMessage += f"[Insufficient atom selection] {self.__getCurrentRestraint()}"\
                                f"The 'resname' clause has no effect for a conjunction of factor {__factor} and {_factor}.\n"

            elif ctx.SegIdentifier():
                if self.__sel_expr_debug:
                    print("  " * self.depth + "--> segidentifier")
                if not self.__hasPolySeq:
                    return

                eval_factor = False
                if 'chain_id' in self.factor:
                    __factor = copy.copy(self.factor)
                    self.consumeFactor_expressions("'segidentifier' clause", False)
                    eval_factor = True

                if ctx.Colon():  # range expression
                    if ctx.Simple_name(0):
                        begChainId = str(ctx.Simple_name(0))
                    elif ctx.Double_quote_string(0):
                        begChainId = str(ctx.Double_quote_string(0)).strip('"').strip()
                        if len(begChainId) == 0:
                            return
                    if ctx.Simple_name(1):
                        endChainId = str(ctx.Simple_name(1))
                    elif ctx.Double_quote_string(1):
                        endChainId = str(ctx.Double_quote_string(1)).strip('"').strip()
                        if len(endChainId) == 0:
                            return
                    self.factor['chain_id'] = [ps['auth_chain_id'] for ps in self.__polySeq
                                               if begChainId <= ps['auth_chain_id'] <= endChainId]
                    if self.__hasNonPolySeq:
                        for np in self.__nonPolySeq:
                            _chainId = np['auth_chain_id']
                            if begChainId <= _chainId <= endChainId and _chainId not in self.factor['chain_id']:
                                self.factor['chain_id'].append(_chainId)

                    if len(self.factor['chain_id']) == 0:
                        if len(self.__polySeq) == 1:
                            self.factor['chain_id'] = self.__polySeq[0]['chain_id']
                            self.factor['auth_chain_id'] = [begChainId, endChainId]
                        else:
                            self.factor['atom_id'] = [None]
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                f"Couldn't specify segment name {begChainId:!r}:{endChainId:!r} in the coordinates.\n"

                else:
                    if ctx.Simple_name(0) or ctx.Double_quote_string(0):
                        if ctx.Simple_name(0):
                            chainId = str(ctx.Simple_name(0))
                        elif ctx.Double_quote_string(0):
                            chainId = str(ctx.Double_quote_string(0)).strip('"').strip()
                            if len(chainId) == 0:
                                return
                        self.factor['chain_id'] = [ps['auth_chain_id'] for ps in self.__polySeq
                                                   if ps['auth_chain_id'] == self.getRealChainId(chainId)]
                        if self.__hasNonPolySeq:
                            for np in self.__nonPolySeq:
                                _chainId = np['auth_chain_id']
                                if _chainId == self.getRealChainId(chainId) and _chainId not in self.factor['chain_id']:
                                    self.factor['chain_id'].append(_chainId)
                    if ctx.Simple_names(0):
                        chainId = str(ctx.Simple_names(0))
                        _chainId = toRegEx(chainId)
                        self.factor['chain_id'] = [ps['auth_chain_id'] for ps in self.__polySeq
                                                   if re.match(_chainId, ps['auth_chain_id'])]
                        if self.__hasNonPolySeq:
                            for np in self.__nonPolySeq:
                                __chainId = np['auth_chain_id']
                                if re.match(_chainId, __chainId) and __chainId not in self.factor['chain_id']:
                                    self.factor['chain_id'].append(__chainId)
                    if ctx.Symbol_name():
                        symbol_name = chainId = str(ctx.Symbol_name())
                        if symbol_name in self.evaluate:
                            val = self.evaluate[symbol_name]
                            if isinstance(val, list):
                                self.factor['chain_id'] = val
                            else:
                                self.factor['chain_id'] = [val]
                        elif symbol_name in self.evaluateFor:
                            val = self.evaluateFor[symbol_name]
                            if isinstance(val, list):
                                self.factor['chain_id'] = val
                            else:
                                self.factor['chain_id'] = [val]
                        else:
                            self.warningMessage += f"[Unsupported data] {self.__getCurrentRestraint()}"\
                                f"The symbol {symbol_name!r} is not defined.\n"
                    if len(self.factor['chain_id']) == 0:
                        if len(self.__polySeq) == 1:
                            self.factor['chain_id'] = self.__polySeq[0]['chain_id']
                            self.factor['auth_chain_id'] = chainId
                        elif self.__reasons is not None:
                            self.factor['atom_id'] = [None]
                            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                                "Couldn't specify segment name "\
                                f"'{chainId}' in the coordinates.\n"  # do not use 'chainId!r' expression, '%' code throws ValueError
                        else:
                            if 'segment_id_mismatch' not in self.reasonsForReParsing:
                                self.reasonsForReParsing['segment_id_mismatch'] = {}
                            if chainId not in self.reasonsForReParsing['segment_id_mismatch']:
                                self.reasonsForReParsing['segment_id_mismatch'][chainId] = None
                            self.factor['alt_chain_id'] = chainId

                if eval_factor and 'atom_selection' in self.factor:
                    if len(self.factor['atom_selection']) == 0:
                        if self.__with_axis and 'atom_id' in __factor and __factor['atom_id'][0] in XPLOR_RDC_PRINCIPAL_AXIS_NAMES:
                            pass
                        elif self.__cur_subtype == 'plane':
                            pass
                        elif self.__cur_subtype == 'dist' and 'atom_id' in __factor and __factor['atom_id'][0] in XPLOR_NITROXIDE_NAMES:
                            pass
                        else:
                            _factor = copy.copy(self.factor)
                            if 'atom_selection' in __factor:
                                del __factor['atom_selection']
                            del _factor['atom_selection']
                            self.warningMessage += f"[Insufficient atom selection] {self.__getCurrentRestraint()}"\
                                f"The 'segidentifier' clause has no effect for a conjunction of factor {__factor} and {_factor}.\n"

            elif ctx.Sfbox():
                pass

            elif ctx.Store1():
                if self.__sel_expr_debug:
                    print("  " * self.depth + "--> store1")
                if len(self.storeSet[1]) == 0:
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Unsupported data] {self.__getCurrentRestraint()}"\
                        "The 'store1' clause has no effect "\
                        "because the internal vector statement is not set.\n"
                else:
                    self.factor = copy.copy(self.storeSet[1])

            elif ctx.Store2():
                if self.__sel_expr_debug:
                    print("  " * self.depth + "--> store2")
                if len(self.storeSet[2]) == 0:
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Unsupported data] {self.__getCurrentRestraint()}"\
                        "The 'store2' clause has no effect "\
                        "because the internal vector statement is not set.\n"
                else:
                    self.factor = copy.copy(self.storeSet[2])

            elif ctx.Store3():
                if self.__sel_expr_debug:
                    print("  " * self.depth + "--> store3")
                if len(self.storeSet[3]) == 0:
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Unsupported data] {self.__getCurrentRestraint()}"\
                        "The 'store3' clause has no effect "\
                        "because the internal vector statement is not set.\n"
                else:
                    self.factor = copy.copy(self.storeSet[3])

            elif ctx.Store4():
                if self.__sel_expr_debug:
                    print("  " * self.depth + "--> store4")
                if len(self.storeSet[4]) == 0:
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Unsupported data] {self.__getCurrentRestraint()}"\
                        "The 'store4' clause has no effect "\
                        "because the internal vector statement is not set.\n"
                else:
                    self.factor = copy.copy(self.storeSet[4])

            elif ctx.Store5():
                if self.__sel_expr_debug:
                    print("  " * self.depth + "--> store5")
                if len(self.storeSet[5]) == 0:
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Unsupported data] {self.__getCurrentRestraint()}"\
                        "The 'store5' clause has no effect "\
                        "because the internal vector statement is not set.\n"
                else:
                    self.factor = copy.copy(self.storeSet[5])

            elif ctx.Store6():
                if self.__sel_expr_debug:
                    print("  " * self.depth + "--> store6")
                if len(self.storeSet[6]) == 0:
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Unsupported data] {self.__getCurrentRestraint()}"\
                        "The 'store6' clause has no effect "\
                        "because the internal vector statement is not set.\n"
                else:
                    self.factor = copy.copy(self.storeSet[6])

            elif ctx.Store7():
                if self.__sel_expr_debug:
                    print("  " * self.depth + "--> store7")
                if len(self.storeSet[7]) == 0:
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Unsupported data] {self.__getCurrentRestraint()}"\
                        "The 'store7' clause has no effect "\
                        "because the internal vector statement is not set.\n"
                else:
                    self.factor = copy.copy(self.storeSet[7])

            elif ctx.Store8():
                if self.__sel_expr_debug:
                    print("  " * self.depth + "--> store8")
                if len(self.storeSet[8]) == 0:
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Unsupported data] {self.__getCurrentRestraint()}"\
                        "The 'store8' clause has no effect "\
                        "because the internal vector statement is not set.\n"
                else:
                    self.factor = copy.copy(self.storeSet[8])

            elif ctx.Store9():
                if self.__sel_expr_debug:
                    print("  " * self.depth + "--> store9")
                if len(self.storeSet[9]) == 0:
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Unsupported data] {self.__getCurrentRestraint()}"\
                        "The 'store9' clause has no effect "\
                        "because the internal vector statement is not set.\n"
                else:
                    self.factor = copy.copy(self.storeSet[9])

            elif ctx.Tag():
                if self.__sel_expr_debug:
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
                                                          'value': self.__representativeModelId},
                                                         {'name': 'label_alt_id', 'type': 'enum',
                                                          'enum': ('A')}
                                                         ])

                    for _atom in _atomSelection:
                        _sequence = (_atom['chain_id'], _atom['seq_id'])

                        if _sequence in _sequenceSelect:
                            continue

                        atomSelection.append(_atom)
                        _sequenceSelect.append(_sequence)

                except Exception as e:
                    if self.__verbose:
                        self.__lfh.write(f"+CnsMRParserListener.exitFactor() ++ Error  - {str(e)}\n")

                self.intersectionFactor_expressions(atomSelection)

                if len(self.factor['atom_selection']) == 0:
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Insufficient atom selection] {self.__getCurrentRestraint()}"\
                        "The 'tag' clause has no effect.\n"

            self.stackFactors.append(self.factor)

        finally:
            self.numberFSelection.clear()

    # Enter a parse tree produced by CnsMRParser#number.
    def enterNumber(self, ctx: CnsMRParser.NumberContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#number.
    def exitNumber(self, ctx: CnsMRParser.NumberContext):
        if ctx.Real():
            self.numberSelection.append(float(str(ctx.Real())))

        elif ctx.Integer():
            self.numberSelection.append(float(str(ctx.Integer())))

        elif ctx.Symbol_name():
            symbol_name = str(ctx.Symbol_name())
            if symbol_name in self.evaluate:
                self.numberSelection.append(float(self.evaluate[symbol_name]))
            else:
                self.warningMessage += f"[Unsupported data] {self.__getCurrentRestraint()}"\
                    f"The symbol {symbol_name!r} is not defined.\n"
                self.numberSelection.append(None)

        else:
            self.numberSelection.append(None)

    # Enter a parse tree produced by CnsMRParser#number_f.
    def enterNumber_f(self, ctx: CnsMRParser.Number_fContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#number_f.
    def exitNumber_f(self, ctx: CnsMRParser.Number_fContext):
        if ctx.Real():
            self.numberFSelection.append(float(str(ctx.Real())))

        elif ctx.Integer():
            self.numberFSelection.append(float(str(ctx.Integer())))

        else:
            self.numberFSelection.append(None)

    # Enter a parse tree produced by CnsMRParser#number_s.
    def enterNumber_s(self, ctx: CnsMRParser.Number_sContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#number_s.
    def exitNumber_s(self, ctx: CnsMRParser.Number_sContext):  # pylint: disable=unused-argument
        pass

    def getNumber_s(self, ctx: CnsMRParser.Number_sContext):  # pylint: disable=no-self-use
        if ctx is None:
            return None

        if ctx.Real():
            return float(str(ctx.Real()))

        if ctx.Integer():
            return float(str(ctx.Integer()))

        if ctx.Symbol_name():
            return str(ctx.Symbol_name())

        return None

    # Enter a parse tree produced by CnsMRParser#number_a.
    def enterNumber_a(self, ctx: CnsMRParser.Number_aContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#number_a.
    def exitNumber_a(self, ctx: CnsMRParser.Number_aContext):  # pylint: disable=unused-argument
        pass

    def getNumber_a(self, ctx: CnsMRParser.Number_aContext):  # pylint: disable=no-self-use
        if ctx is None:
            return None

        if ctx.Real():
            return float(str(ctx.Real()))

        if ctx.Integer():
            return float(str(ctx.Integer()))

        return None

    # Enter a parse tree produced by CnsMRParser#classification.
    def enterClassification(self, ctx: CnsMRParser.ClassificationContext):
        self.classification = self.getClass_name(ctx.class_name())

    # Exit a parse tree produced by CnsMRParser#classification.
    def exitClassification(self, ctx: CnsMRParser.ClassificationContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#class_name.
    def enterClass_name(self, ctx: CnsMRParser.Class_nameContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#class_name.
    def exitClass_name(self, ctx: CnsMRParser.Class_nameContext):  # pylint: disable=unused-argument
        pass

    def getClass_name(self, ctx: CnsMRParser.Class_nameContext):  # pylint: disable=no-self-use
        if ctx is None:
            return None

        if ctx.Simple_name():
            return str(ctx.Simple_name())

        if ctx.Noe():
            return str(ctx.Noe())

        if ctx.Restraints():
            return str(ctx.Restraints())

        if ctx.AngleDb():
            return str(ctx.AngleDb())

        if ctx.HBonded():
            return str(ctx.HBonded())

        if ctx.Dihedral():
            return str(ctx.Dihedral())

        if ctx.Improper():
            return str(ctx.Improper())

        return None

    # Enter a parse tree produced by CnsMRParser#flag_statement.
    def enterFlag_statement(self, ctx: CnsMRParser.Flag_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#flag_statement.
    def exitFlag_statement(self, ctx: CnsMRParser.Flag_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#vector_statement.
    def enterVector_statement(self, ctx: CnsMRParser.Vector_statementContext):  # pylint: disable=unused-argument
        self.__cur_vector_mode = ''
        self.__cur_vector_atom_prop_type = ''

        self.__cur_vflc_op_code = ''
        self.stackVflc = []

        self.atomSelectionSet.clear()
        self.__warningInAtomSelection = ''

    # Exit a parse tree produced by CnsMRParser#vector_statement.
    def exitVector_statement(self, ctx: CnsMRParser.Vector_statementContext):  # pylint: disable=unused-argument
        if self.__cur_vector_mode == 'identity':
            if self.__cur_vector_atom_prop_type.startswith('store'):
                self.storeSet[int(self.__cur_vector_atom_prop_type[-1])] = {'atom_selection': copy.copy(self.atomSelectionSet[0])}

        elif self.__cur_vector_mode == 'do':
            if len(self.__cur_vector_atom_prop_type) > 0:
                vector_name = self.__cur_vector_atom_prop_type
                if len(vector_name) > 4:
                    vector_name = vector_name[:4]
                if vector_name not in self.vectorDo:
                    self.vectorDo[vector_name] = []
                vector = {'atom_selection': copy.copy(self.atomSelectionSet[0])}
                while self.stackVflc:
                    vector['value'] = self.stackVflc.pop()
                self.vectorDo[vector_name].append(vector)

    # Enter a parse tree produced by CnsMRParser#vector_mode.
    def enterVector_mode(self, ctx: CnsMRParser.Vector_modeContext):
        if ctx.Identity_Lp():
            self.__cur_vector_mode = 'identity'

        elif ctx.Do_Lp():
            self.__cur_vector_mode = 'do'

        elif ctx.Show():
            self.__cur_vector_mode = 'show'

    # Exit a parse tree produced by CnsMRParser#vector_mode.
    def exitVector_mode(self, ctx: CnsMRParser.Vector_modeContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#vector_expression.
    def enterVector_expression(self, ctx: CnsMRParser.Vector_expressionContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#vector_expression.
    def exitVector_expression(self, ctx: CnsMRParser.Vector_expressionContext):
        if ctx.Atom_properties_VE():
            self.__cur_vector_atom_prop_type = str(ctx.Atom_properties_VE()).lower()

    # Enter a parse tree produced by CnsMRParser#vector_operation.
    def enterVector_operation(self, ctx: CnsMRParser.Vector_operationContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#vector_operation.
    def exitVector_operation(self, ctx: CnsMRParser.Vector_operationContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#vflc.
    def enterVflc(self, ctx: CnsMRParser.VflcContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#vflc.
    def exitVflc(self, ctx: CnsMRParser.VflcContext):
        if ctx.Integer_VE():
            self.stackVflc.append(int(str(ctx.Integer_VE())))
        elif ctx.Real_VE():
            self.stackVflc.append(float(str(ctx.Real_VE())))
        elif ctx.Simple_name_VE():
            self.stackVflc.append(str(ctx.Simple_name_VE()))
        elif ctx.Double_quote_string_VE():
            self.stackVflc.append(str(ctx.Double_quote_string_VE()).strip('"').strip())
        elif ctx.Symbol_name_VE():
            symbol_name = str(ctx.Symbol_name_VE())
            if symbol_name in self.evaluate:
                self.stackVflc.append(self.evaluate[symbol_name])
            elif symbol_name in self.evaluateFor:
                self.stackVflc.append(self.evaluateFor[symbol_name])
            else:
                self.warningMessage += f"[Unsupported data] {self.__getCurrentRestraint()}"\
                    f"The symbol {symbol_name!r} is not defined.\n"
        elif ctx.Atom_properties_VE():
            pass
        elif ctx.vector_func_call():
            pass

    # Enter a parse tree produced by CnsMRParser#vector_func_call.
    def enterVector_func_call(self, ctx: CnsMRParser.Vector_func_callContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#vector_func_call.
    def exitVector_func_call(self, ctx: CnsMRParser.Vector_func_callContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#vector_show_property.
    def enterVector_show_property(self, ctx: CnsMRParser.Vector_show_propertyContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#vector_show_property.
    def exitVector_show_property(self, ctx: CnsMRParser.Vector_show_propertyContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#evaluate_statement.
    def enterEvaluate_statement(self, ctx: CnsMRParser.Evaluate_statementContext):
        if ctx.Symbol_name_VE():
            self.__cur_symbol_name = str(ctx.Symbol_name_VE())

        self.__cur_vflc_op_code = ''
        self.stackVflc = []

    # Exit a parse tree produced by CnsMRParser#evaluate_statement.
    def exitEvaluate_statement(self, ctx: CnsMRParser.Evaluate_statementContext):  # pylint: disable=unused-argument
        if self.stackVflc:
            self.evaluate[self.__cur_symbol_name] = self.stackVflc[0]

            if self.__cur_vflc_op_code in ('+', '-', '*', '/', '^'):
                s = self.stackVflc[0]
                n = self.stackVflc[1]
                if isinstance(s, list) and not isinstance(n, list):
                    if self.__cur_vflc_op_code == '+':
                        self.evaluate[self.__cur_symbol_name] = [_s + n for _s in s]
                    elif self.__cur_vflc_op_code == '-':
                        self.evaluate[self.__cur_symbol_name] = [_s - n for _s in s]
                    elif self.__cur_vflc_op_code == '*':
                        self.evaluate[self.__cur_symbol_name] = [_s * n for _s in s]
                    elif self.__cur_vflc_op_code == '/':
                        self.evaluate[self.__cur_symbol_name] = [_s / n for _s in s]
                    elif self.__cur_vflc_op_code == '^':
                        self.evaluate[self.__cur_symbol_name] = [_s ** n for _s in s]
                elif not isinstance(s, list) and isinstance(n, list):
                    if self.__cur_vflc_op_code == '+':
                        self.evaluate[self.__cur_symbol_name] = [s + _n for _n in n]
                    elif self.__cur_vflc_op_code == '-':
                        self.evaluate[self.__cur_symbol_name] = [s - _n for _n in n]
                    elif self.__cur_vflc_op_code == '*':
                        self.evaluate[self.__cur_symbol_name] = [s * _n for _n in n]
                    elif self.__cur_vflc_op_code == '/':
                        self.evaluate[self.__cur_symbol_name] = [s / _n for _n in n]
                    elif self.__cur_vflc_op_code == '^':
                        self.evaluate[self.__cur_symbol_name] = [s ** _n for _n in n]
                elif isinstance(s, list) and isinstance(n, list):
                    if self.__cur_vflc_op_code == '+':
                        self.evaluate[self.__cur_symbol_name] = [_s + _n for _s, _n in zip(s, n)]
                    elif self.__cur_vflc_op_code == '-':
                        self.evaluate[self.__cur_symbol_name] = [_s - _n for _s, _n in zip(s, n)]
                    elif self.__cur_vflc_op_code == '*':
                        self.evaluate[self.__cur_symbol_name] = [_s * _n for _s, _n in zip(s, n)]
                    elif self.__cur_vflc_op_code == '/':
                        self.evaluate[self.__cur_symbol_name] = [_s / _n for _s, _n in zip(s, n)]
                    elif self.__cur_vflc_op_code == '^':
                        self.evaluate[self.__cur_symbol_name] = [_s ** _n for _s, _n in zip(s, n)]
                else:
                    if self.__cur_vflc_op_code == '+':
                        self.evaluate[self.__cur_symbol_name] = s + n
                    elif self.__cur_vflc_op_code == '-':
                        self.evaluate[self.__cur_symbol_name] = s - n
                    elif self.__cur_vflc_op_code == '*':
                        self.evaluate[self.__cur_symbol_name] = s * n
                    elif self.__cur_vflc_op_code == '/':
                        self.evaluate[self.__cur_symbol_name] = s / n
                    elif self.__cur_vflc_op_code == '^':
                        self.evaluate[self.__cur_symbol_name] = s ** n

        self.stackVflc.clear()

    # Enter a parse tree produced by CnsMRParser#evaluate_operation.
    def enterEvaluate_operation(self, ctx: CnsMRParser.Evaluate_operationContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#evaluate_operation.
    def exitEvaluate_operation(self, ctx: CnsMRParser.Evaluate_operationContext):
        if ctx.Add_op_VE():
            self.__cur_vflc_op_code = '+'
        elif ctx.Sub_op_VE():
            self.__cur_vflc_op_code = '-'
        elif ctx.Mul_op_VE():
            self.__cur_vflc_op_code = '*'
        elif ctx.Div_op_VE():
            self.__cur_vflc_op_code = '/'
        elif ctx.Exp_op_VE():
            self.__cur_vflc_op_code = '^'

    # Enter a parse tree produced by CnsMRParser#patch_statement.
    def enterPatch_statement(self, ctx: CnsMRParser.Patch_statementContext):  # pylint: disable=unused-argument
        self.geoRestraints += 1
        self.__cur_subtype = 'geo'

        self.atomSelectionSet.clear()
        self.__warningInAtomSelection = ''

    # Exit a parse tree produced by CnsMRParser#patch_statement.
    def exitPatch_statement(self, ctx: CnsMRParser.Patch_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#parameter_setting.
    def enterParameter_setting(self, ctx: CnsMRParser.Parameter_settingContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#parameter_setting.
    def exitParameter_setting(self, ctx: CnsMRParser.Parameter_settingContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#parameter_statement.
    def enterParameter_statement(self, ctx: CnsMRParser.Parameter_statementContext):  # pylint: disable=unused-argument
        self.geoRestraints += 1
        self.__cur_subtype = 'geo'

    # Exit a parse tree produced by CnsMRParser#parameter_statement.
    def exitParameter_statement(self, ctx: CnsMRParser.Parameter_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#noe_assign_loop.
    def enterNoe_assign_loop(self, ctx: CnsMRParser.Noe_assign_loopContext):
        symbol_name = None
        if ctx.Symbol_name_CF():
            symbol_name = str(ctx.Symbol_name_CF())

        if ctx.Integer_CF(0):
            int_list = []
            idx = 0
            while True:
                if ctx.Integer_CF(idx):
                    int_list.append(int(str(ctx.Integer_CF(idx))))
                    idx += 1
                else:
                    break
            if symbol_name is not None:
                self.evaluateFor[symbol_name] = int_list

        if ctx.Real_CF(0):
            real_list = []
            idx = 0
            while True:
                if ctx.Real_CF(idx):
                    real_list.append(float(str(ctx.Real_CF(idx))))
                    idx += 1
                else:
                    break
            if symbol_name[0] is not None:
                self.evaluateFor[symbol_name] = real_list

        if ctx.Simple_name_CF(0):
            str_list = []
            idx = 0
            while True:
                if ctx.Simple_name_CF(idx):
                    str_list.append(str(ctx.Simple_name_CF(idx)))
                    idx += 1
                else:
                    break
            if symbol_name is not None:
                self.evaluateFor[symbol_name] = str_list

    # Exit a parse tree produced by CnsMRParser#noe_assign_loop.
    def exitNoe_assign_loop(self, ctx: CnsMRParser.Noe_assign_loopContext):
        if ctx.Symbol_name_CF():
            symbol_name = str(ctx.Symbol_name_CF())
            if symbol_name in self.evaluateFor:
                del self.evaluateFor[symbol_name]

    # Enter a parse tree produced by CnsMRParser#dihedral_assign_loop.
    def enterDihedral_assign_loop(self, ctx: CnsMRParser.Dihedral_assign_loopContext):
        symbol_name = None
        if ctx.Symbol_name_CF():
            symbol_name = str(ctx.Symbol_name_CF())

        if ctx.Integer_CF(0):
            int_list = []
            idx = 0
            while True:
                if ctx.Integer_CF(idx):
                    int_list.append(int(str(ctx.Integer_CF(idx))))
                    idx += 1
                else:
                    break
            if symbol_name is not None:
                self.evaluateFor[symbol_name] = int_list

        if ctx.Real_CF(0):
            real_list = []
            idx = 0
            while True:
                if ctx.Real_CF(idx):
                    real_list.append(float(str(ctx.Real_CF(idx))))
                    idx += 1
                else:
                    break
            if symbol_name[0] is not None:
                self.evaluateFor[symbol_name] = real_list

        if ctx.Simple_name_CF(0):
            str_list = []
            idx = 0
            while True:
                if ctx.Simple_name_CF(idx):
                    str_list.append(str(ctx.Simple_name_CF(idx)))
                    idx += 1
                else:
                    break
            if symbol_name is not None:
                self.evaluateFor[symbol_name] = str_list

    # Exit a parse tree produced by CnsMRParser#dihedral_assign_loop.
    def exitDihedral_assign_loop(self, ctx: CnsMRParser.Dihedral_assign_loopContext):
        if ctx.Symbol_name_CF():
            symbol_name = str(ctx.Symbol_name_CF())
            if symbol_name in self.evaluateFor:
                del self.evaluateFor[symbol_name]

    # Enter a parse tree produced by CnsMRParser#sani_assign_loop.
    def enterSani_assign_loop(self, ctx: CnsMRParser.Sani_assign_loopContext):
        symbol_name = None
        if ctx.Symbol_name_CF():
            symbol_name = str(ctx.Symbol_name_CF())

        if ctx.Integer_CF(0):
            int_list = []
            idx = 0
            while True:
                if ctx.Integer_CF(idx):
                    int_list.append(int(str(ctx.Integer_CF(idx))))
                    idx += 1
                else:
                    break
            if symbol_name is not None:
                self.evaluateFor[symbol_name] = int_list

        if ctx.Real_CF(0):
            real_list = []
            idx = 0
            while True:
                if ctx.Real_CF(idx):
                    real_list.append(float(str(ctx.Real_CF(idx))))
                    idx += 1
                else:
                    break
            if symbol_name[0] is not None:
                self.evaluateFor[symbol_name] = real_list

        if ctx.Simple_name_CF(0):
            str_list = []
            idx = 0
            while True:
                if ctx.Simple_name_CF(idx):
                    str_list.append(str(ctx.Simple_name_CF(idx)))
                    idx += 1
                else:
                    break
            if symbol_name is not None:
                self.evaluateFor[symbol_name] = str_list

    # Exit a parse tree produced by CnsMRParser#sani_assign_loop.
    def exitSani_assign_loop(self, ctx: CnsMRParser.Sani_assign_loopContext):
        if ctx.Symbol_name_CF():
            symbol_name = str(ctx.Symbol_name_CF())
            if symbol_name in self.evaluateFor:
                del self.evaluateFor[symbol_name]

    # Enter a parse tree produced by CnsMRParser#coup_assign_loop.
    def enterCoup_assign_loop(self, ctx: CnsMRParser.Coup_assign_loopContext):
        symbol_name = None
        if ctx.Symbol_name_CF():
            symbol_name = str(ctx.Symbol_name_CF())

        if ctx.Integer_CF(0):
            int_list = []
            idx = 0
            while True:
                if ctx.Integer_CF(idx):
                    int_list.append(int(str(ctx.Integer_CF(idx))))
                    idx += 1
                else:
                    break
            if symbol_name is not None:
                self.evaluateFor[symbol_name] = int_list

        if ctx.Real_CF(0):
            real_list = []
            idx = 0
            while True:
                if ctx.Real_CF(idx):
                    real_list.append(float(str(ctx.Real_CF(idx))))
                    idx += 1
                else:
                    break
            if symbol_name[0] is not None:
                self.evaluateFor[symbol_name] = real_list

        if ctx.Simple_name_CF(0):
            str_list = []
            idx = 0
            while True:
                if ctx.Simple_name_CF(idx):
                    str_list.append(str(ctx.Simple_name_CF(idx)))
                    idx += 1
                else:
                    break
            if symbol_name is not None:
                self.evaluateFor[symbol_name] = str_list

    # Exit a parse tree produced by CnsMRParser#coup_assign_loop.
    def exitCoup_assign_loop(self, ctx: CnsMRParser.Coup_assign_loopContext):
        if ctx.Symbol_name_CF():
            symbol_name = str(ctx.Symbol_name_CF())
            if symbol_name in self.evaluateFor:
                del self.evaluateFor[symbol_name]

    # Enter a parse tree produced by CnsMRParser#carbon_shift_assign_loop.
    def enterCarbon_shift_assign_loop(self, ctx: CnsMRParser.Carbon_shift_assign_loopContext):
        symbol_name = None
        if ctx.Symbol_name_CF():
            symbol_name = str(ctx.Symbol_name_CF())

        if ctx.Integer_CF(0):
            int_list = []
            idx = 0
            while True:
                if ctx.Integer_CF(idx):
                    int_list.append(int(str(ctx.Integer_CF(idx))))
                    idx += 1
                else:
                    break
            if symbol_name is not None:
                self.evaluateFor[symbol_name] = int_list

        if ctx.Real_CF(0):
            real_list = []
            idx = 0
            while True:
                if ctx.Real_CF(idx):
                    real_list.append(float(str(ctx.Real_CF(idx))))
                    idx += 1
                else:
                    break
            if symbol_name[0] is not None:
                self.evaluateFor[symbol_name] = real_list

        if ctx.Simple_name_CF(0):
            str_list = []
            idx = 0
            while True:
                if ctx.Simple_name_CF(idx):
                    str_list.append(str(ctx.Simple_name_CF(idx)))
                    idx += 1
                else:
                    break
            if symbol_name is not None:
                self.evaluateFor[symbol_name] = str_list

    # Exit a parse tree produced by CnsMRParser#carbon_shift_assign_loop.
    def exitCarbon_shift_assign_loop(self, ctx: CnsMRParser.Carbon_shift_assign_loopContext):
        if ctx.Symbol_name_CF():
            symbol_name = str(ctx.Symbol_name_CF())
            if symbol_name in self.evaluateFor:
                del self.evaluateFor[symbol_name]

    # Enter a parse tree produced by CnsMRParser#plane_group_loop.
    def enterPlane_group_loop(self, ctx: CnsMRParser.Plane_group_loopContext):
        symbol_name = None
        if ctx.Symbol_name_CF():
            symbol_name = str(ctx.Symbol_name_CF())

        if ctx.Integer_CF(0):
            int_list = []
            idx = 0
            while True:
                if ctx.Integer_CF(idx):
                    int_list.append(int(str(ctx.Integer_CF(idx))))
                    idx += 1
                else:
                    break
            if symbol_name is not None:
                self.evaluateFor[symbol_name] = int_list

        if ctx.Real_CF(0):
            real_list = []
            idx = 0
            while True:
                if ctx.Real_CF(idx):
                    real_list.append(float(str(ctx.Real_CF(idx))))
                    idx += 1
                else:
                    break
            if symbol_name[0] is not None:
                self.evaluateFor[symbol_name] = real_list

        if ctx.Simple_name_CF(0):
            str_list = []
            idx = 0
            while True:
                if ctx.Simple_name_CF(idx):
                    str_list.append(str(ctx.Simple_name_CF(idx)))
                    idx += 1
                else:
                    break
            if symbol_name is not None:
                self.evaluateFor[symbol_name] = str_list

    # Exit a parse tree produced by CnsMRParser#plane_group_loop.
    def exitPlane_group_loop(self, ctx: CnsMRParser.Plane_group_loopContext):
        if ctx.Symbol_name_CF():
            symbol_name = str(ctx.Symbol_name_CF())
            if symbol_name in self.evaluateFor:
                del self.evaluateFor[symbol_name]

    def __getCurrentRestraint(self):
        if self.__cur_subtype == 'dist':
            return f"[Check the {self.distRestraints}th row of distance restraints] "
        if self.__cur_subtype == 'dihed':
            return f"[Check the {self.dihedRestraints}th row of dihedral angle restraints] "
        if self.__cur_subtype == 'rdc':
            return f"[Check the {self.rdcRestraints}th row of residual dipolar coupling restraints] "
        if self.__cur_subtype == 'plane':
            return f"[Check the {self.planeRestraints}th row of plane restraints] "
        if self.__cur_subtype == 'jcoup':
            return f"[Check the {self.jcoupRestraints}th row of scalar J-coupling restraints] "
        if self.__cur_subtype == 'hvycs':
            return f"[Check the {self.hvycsRestraints}th row of carbon chemical shift restraints] "
        if self.__cur_subtype == 'procs':
            return f"[Check the {self.procsRestraints}th row of proton chemical shift restraints] "
        if self.__cur_subtype == 'rama':
            return f"[Check the {self.ramaRestraints}th row of conformation database restraints] "
        if self.__cur_subtype == 'diff':
            return f"[Check the {self.diffRestraints}th row of duffusion anisotropy restraints] "
        # if self.__cur_subtype == 'ang':
        #     return f"[Check the {self.angRestraints}th row of angle database restraints] "
        if self.__cur_subtype == 'geo':
            return f"[Check the {self.geoRestraints}th row of harmonic coordinate/NCS restraints] "
        return ''

    def __setLocalSeqScheme(self):
        if 'local_seq_scheme' not in self.reasonsForReParsing:
            self.reasonsForReParsing['local_seq_scheme'] = {}
        if self.__cur_subtype == 'dist':
            self.reasonsForReParsing['local_seq_scheme'][(self.__cur_subtype, self.distRestraints)] = self.__preferAuthSeq
        elif self.__cur_subtype == 'dihed':
            self.reasonsForReParsing['local_seq_scheme'][(self.__cur_subtype, self.dihedRestraints)] = self.__preferAuthSeq
        elif self.__cur_subtype == 'rdc':
            self.reasonsForReParsing['local_seq_scheme'][(self.__cur_subtype, self.rdcRestraints)] = self.__preferAuthSeq
        elif self.__cur_subtype == 'plane':
            self.reasonsForReParsing['loca_seq_scheme'][(self.__cur_subtype, self.planeRestraints)] = self.__preferAuthSeq
        elif self.__cur_subtype == 'jcoup':
            self.reasonsForReParsing['local_seq_scheme'][(self.__cur_subtype, self.jcoupRestraints)] = self.__preferAuthSeq
        elif self.__cur_subtype == 'hvycs':
            self.reasonsForReParsing['local_seq_scheme'][(self.__cur_subtype, self.hvycsRestraints)] = self.__preferAuthSeq
        elif self.__cur_subtype == 'procs':
            self.reasonsForReParsing['local_seq_scheme'][(self.__cur_subtype, self.procsRestraints)] = self.__preferAuthSeq
        elif self.__cur_subtype == 'rama':
            self.reasonsForReParsing['local_seq_scheme'][(self.__cur_subtype, self.ramaRestraints)] = self.__preferAuthSeq
        elif self.__cur_subtype == 'diff':
            self.reasonsForReParsing['local_seq_scheme'][(self.__cur_subtype, self.diffRestraints)] = self.__preferAuthSeq
        # elif self.__cur_subtype == 'ang':
        #     self.reasonsForReParsing['local_seq_scheme'][(self.__cur_subtype, self.angRestraints)] = self.__preferAuthSeq
        elif self.__cur_subtype == 'geo':
            self.reasonsForReParsing['local_seq_scheme'][(self.__cur_subtype, self.geoRestraints)] = self.__preferAuthSeq
        if not self.__preferAuthSeq:
            self.__preferLabelSeqCount += 1
            if self.__preferLabelSeqCount > MAX_PREF_LABEL_SCHEME_COUNT:
                self.reasonsForReParsing['label_seq_scheme'] = True

    def __retrieveLocalSeqScheme(self):
        if self.__reasons is None or 'local_seq_scheme' not in self.__reasons:
            return
        if 'label_seq_scheme' in self.__reasons and self.__reasons['label_seq_scheme']:
            self.__preferAuthSeq = False
            self.__authSeqId = 'label_seq_id'
            return
        if self.__cur_subtype == 'dist':
            key = (self.__cur_subtype, self.distRestraints)
        elif self.__cur_subtype == 'dihed':
            key = (self.__cur_subtype, self.dihedRestraints)
        elif self.__cur_subtype == 'rdc':
            key = (self.__cur_subtype, self.rdcRestraints)
        elif self.__cur_subtype == 'plane':
            key = (self.__cur_subtype, self.planeRestraints)
        elif self.__cur_subtype == 'jcoup':
            key = (self.__cur_subtype, self.jcoupRestraints)
        elif self.__cur_subtype == 'hvycs':
            key = (self.__cur_subtype, self.hvycsRestraints)
        elif self.__cur_subtype == 'procs':
            key = (self.__cur_subtype, self.procsRestraints)
        elif self.__cur_subtype == 'rama':
            key = (self.__cur_subtype, self.ramaRestraints)
        elif self.__cur_subtype == 'diff':
            key = (self.__cur_subtype, self.diffRestraints)
        # elif self.__cur_subtype == 'ang':
        #     key = (self.__cur_subtype, self.angRestraints)
        elif self.__cur_subtype == 'geo':
            key = (self.__cur_subtype, self.geoRestraints)
        else:
            return

        if key in self.__reasons['local_seq_scheme']:
            self.__preferAuthSeq = self.__reasons['local_seq_scheme'][key]

    def __addSf(self, constraintType=None, potentialType=None, rdcCode=None):
        content_subtype = contentSubtypeOf(self.__cur_subtype)

        if content_subtype is None:
            return

        self.__listIdCounter = incListIdCounter(self.__cur_subtype, self.__listIdCounter)

        key = (self.__cur_subtype, constraintType, potentialType, rdcCode, None)

        if key not in self.sfDict:
            self.sfDict[key] = []

        list_id = self.__listIdCounter[content_subtype]

        restraint_name = getRestraintName(self.__cur_subtype)

        sf_framecode = 'CNS_' + restraint_name.replace(' ', '_') + f'_{list_id}'

        sf = getSaveframe(self.__cur_subtype, sf_framecode, list_id, self.__entryId, self.__originalFileName,
                          constraintType=constraintType, potentialType=potentialType, rdcCode=rdcCode)

        not_valid = True

        lp = getLoop(self.__cur_subtype)
        if not isinstance(lp, dict):
            sf.add_loop(lp)
            not_valid = False

        _restraint_name = restraint_name.split()

        item = {'file_type': self.__file_type, 'saveframe': sf, 'loop': lp, 'list_id': list_id,
                'id': 0, 'index_id': 0,
                'constraint_type': ' '.join(_restraint_name[:-1])}

        if not_valid:
            item['tags'] = []

        if self.__cur_subtype == 'dist':
            item['constraint_subsubtype'] = 'simple'
            if constraintType is None:
                item['NOE_dist_averaging_method'] = self.noeAverage
            elif 'ROE' in constraintType:
                item['ROE_dist_averaging_method'] = self.noeAverage

        self.sfDict[key].append(item)

    def __getSf(self, constraintType=None, potentialType=None, rdcCode=None):
        key = (self.__cur_subtype, constraintType, potentialType, rdcCode, None)

        if key not in self.sfDict:
            replaced = False
            if potentialType is not None or rdcCode is not None:
                old_key = (self.__cur_subtype, constraintType, None, None, None)
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
                    if rdcCode is not None:
                        idx = next((idx for idx, t in enumerate(sf.tags) if t[0] == 'Details'), -1)
                        if idx != -1:
                            sf.tags[idx][1] = rdcCode
                        else:
                            sf.add_tag('Details', rdcCode)
            if not replaced:
                self.__addSf(constraintType=constraintType, potentialType=potentialType, rdcCode=rdcCode)

        return self.sfDict[key][-1]

    def getContentSubtype(self):
        """ Return content subtype of CNS MR file.
        """

        if self.distStatements == 0 and self.distRestraints > 0:
            self.distStatements = 1

        if self.dihedStatements == 0 and self.dihedRestraints > 0:
            self.dihedStatements = 1

        if self.rdcStatements == 0 and self.rdcRestraints > 0:
            self.rdcStatements = 1

        if self.planeStatements == 0 and self.planeRestraints > 0:
            self.planeStatements = 1

        if self.jcoupStatements == 0 and self.jcoupRestraints > 0:
            self.jcoupStatements = 1

        if self.hvycsStatements == 0 and self.hvycsRestraints > 0:
            self.hvycsStatements = 1

        if self.procsStatements == 0 and self.procsRestraints > 0:
            self.procsStatements = 1

        if self.ramaStatements == 0 and self.ramaRestraints > 0:
            self.ramaStatements = 1

        if self.diffStatements == 0 and self.diffRestraints > 0:
            self.diffStatements = 1

        # if self.angStatements == 0 and self.angRestraints > 0:
        #     self.angStatements = 1

        if self.geoStatements == 0 and self.geoRestraints > 0:
            self.geoStatements = 1

        contentSubtype = {'dist_restraint': self.distStatements,
                          'dihed_restraint': self.dihedStatements,
                          'rdc_restraint': self.rdcStatements,
                          'plane_restraint': self.planeStatements,
                          'jcoup_restraint': self.jcoupStatements,
                          'hvycs_restraint': self.hvycsStatements,
                          'procs_restraint': self.procsStatements,
                          'rama_restraint': self.ramaStatements,
                          'diff_restraint': self.diffStatements,
                          # 'ang_restraint': self.angStatements
                          'geo_restraint': self.geoStatements
                          }

        return {k: v for k, v in contentSubtype.items() if v > 0}

    def getPolymerSequence(self):
        """ Return polymer sequence of CNS MR file.
        """
        return None if self.__polySeqRst is None or len(self.__polySeqRst) == 0 else self.__polySeqRst

    def getSequenceAlignment(self):
        """ Return sequence alignment between coordinates and CNS MR.
        """
        return None if self.__seqAlign is None or len(self.__seqAlign) == 0 else self.__seqAlign

    def getChainAssignment(self):
        """ Return chain assignment between coordinates and CNS MR.
        """
        return None if self.__chainAssign is None or len(self.__chainAssign) == 0 else self.__chainAssign

    def getReasonsForReparsing(self):
        """ Return reasons for re-parsing CNS MR file.
        """
        return None if len(self.reasonsForReParsing) == 0 else self.reasonsForReParsing

    def getListIdCounter(self):
        """ Return updated list id counter.
        """
        return self.__listIdCounter

    def getSfDict(self):
        """ Return a dictionary of pynmrstar saveframes.
        """
        return None if len(self.sfDict) == 0 else self.sfDict

# del CnsMRParser
