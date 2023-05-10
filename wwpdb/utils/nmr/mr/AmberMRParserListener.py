##
# File: AmberMRParserListener.py
# Date: 27-Jan-2022
#
# Updates:
""" ParserLister class for AMBER MR files.
    @author: Masashi Yokochi
"""
import sys
import copy
import re
import itertools
import numpy

from antlr4 import ParseTreeListener
from operator import itemgetter

try:
    from wwpdb.utils.align.alignlib import PairwiseAlign  # pylint: disable=no-name-in-module
    from wwpdb.utils.nmr.mr.AmberMRParser import AmberMRParser
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (toNpArray,
                                                       stripQuot,
                                                       coordAssemblyChecker,
                                                       translateToStdAtomName,
                                                       translateToStdResName,
                                                       isIdenticalRestraint,
                                                       isLongRangeRestraint,
                                                       isAmbigAtomSelection,
                                                       getTypeOfDihedralRestraint,
                                                       getRdcCode,
                                                       getRestraintName,
                                                       contentSubtypeOf,
                                                       incListIdCounter,
                                                       decListIdCounter,
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
                                                       RDC_RESTRAINT_ERROR,
                                                       CSA_RESTRAINT_RANGE,
                                                       CSA_RESTRAINT_ERROR,
                                                       PCS_RESTRAINT_RANGE,
                                                       PCS_RESTRAINT_ERROR,
                                                       CS_RESTRAINT_RANGE,
                                                       CS_RESTRAINT_ERROR,
                                                       DIST_AMBIG_LOW,
                                                       DIST_AMBIG_UP,
                                                       CARTN_DATA_ITEMS,
                                                       AUTH_ATOM_CARTN_DATA_ITEMS)
    from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
    from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from wwpdb.utils.nmr.NEFTranslator.NEFTranslator import NEFTranslator
    from wwpdb.utils.nmr.AlignUtil import (LARGE_ASYM_ID,
                                           monDict3,
                                           protonBeginCode,
                                           aminoProtonCode,
                                           rdcBbPairCode,
                                           updatePolySeqRst,
                                           updatePolySeqRstFromAtomSelectionSet,
                                           sortPolySeqRst,
                                           alignPolymerSequence,
                                           assignPolymerSequence,
                                           trimSequenceAlignment,
                                           retrieveAtomIdentFromMRMap)
except ImportError:
    from nmr.align.alignlib import PairwiseAlign  # pylint: disable=no-name-in-module
    from nmr.mr.AmberMRParser import AmberMRParser
    from nmr.mr.ParserListenerUtil import (toNpArray,
                                           stripQuot,
                                           coordAssemblyChecker,
                                           translateToStdAtomName,
                                           translateToStdResName,
                                           isIdenticalRestraint,
                                           isLongRangeRestraint,
                                           isAmbigAtomSelection,
                                           getTypeOfDihedralRestraint,
                                           getRdcCode,
                                           getRestraintName,
                                           contentSubtypeOf,
                                           incListIdCounter,
                                           decListIdCounter,
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
                                           RDC_RESTRAINT_ERROR,
                                           CSA_RESTRAINT_RANGE,
                                           CSA_RESTRAINT_ERROR,
                                           PCS_RESTRAINT_RANGE,
                                           PCS_RESTRAINT_ERROR,
                                           CS_RESTRAINT_RANGE,
                                           CS_RESTRAINT_ERROR,
                                           DIST_AMBIG_LOW,
                                           DIST_AMBIG_UP,
                                           CARTN_DATA_ITEMS,
                                           AUTH_ATOM_CARTN_DATA_ITEMS)
    from nmr.ChemCompUtil import ChemCompUtil
    from nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from nmr.NEFTranslator.NEFTranslator import NEFTranslator
    from nmr.AlignUtil import (LARGE_ASYM_ID,
                               monDict3,
                               protonBeginCode,
                               aminoProtonCode,
                               rdcBbPairCode,
                               updatePolySeqRst,
                               updatePolySeqRstFromAtomSelectionSet,
                               sortPolySeqRst,
                               alignPolymerSequence,
                               assignPolymerSequence,
                               trimSequenceAlignment,
                               retrieveAtomIdentFromMRMap)


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


CSA_RANGE_MIN = CSA_RESTRAINT_RANGE['min_inclusive']
CSA_RANGE_MAX = CSA_RESTRAINT_RANGE['max_inclusive']

CSA_ERROR_MIN = CSA_RESTRAINT_ERROR['min_exclusive']
CSA_ERROR_MAX = CSA_RESTRAINT_ERROR['max_exclusive']


PCS_RANGE_MIN = PCS_RESTRAINT_RANGE['min_inclusive']
PCS_RANGE_MAX = PCS_RESTRAINT_RANGE['max_inclusive']

PCS_ERROR_MIN = PCS_RESTRAINT_ERROR['min_exclusive']
PCS_ERROR_MAX = PCS_RESTRAINT_ERROR['max_exclusive']


CS_RANGE_MIN = CS_RESTRAINT_RANGE['min_inclusive']
CS_RANGE_MAX = CS_RESTRAINT_RANGE['max_inclusive']

CS_ERROR_MIN = CS_RESTRAINT_ERROR['min_exclusive']
CS_ERROR_MAX = CS_RESTRAINT_ERROR['max_exclusive']


# maximum column size of IAT
MAX_COL_IAT = 8


# maximum column size of IGRn
MAX_COL_IGR = 200


# maximum column size of RSTWT
MAX_COL_RSTWT = 4


# column sizes of distance restraint
COL_DIST = 2


# column sizes of angle restraint
COL_ANG = 3


# column sizes of torsional angle restraint
COL_DIHED = 4


# column sizes of plane-point angle restraint
COL_PLANE_POINT = 5


# column sizes of plane-plane angle restraint
COL_PLANE_PLANE = 8


# column sizes of generalized distance restraint (2 coordinate vectors)
COL_DIST_COORD2 = 4


# column sizes of generalized distance restraint (3 coordinate vectors)
COL_DIST_COORD3 = 6


# column sizes of generalized distance restraint (4 coordinate vectors)
COL_DIST_COORD4 = 8


# This class defines a complete listener for a parse tree produced by AmberMRParser.
class AmberMRParserListener(ParseTreeListener):

    __file_type = 'nm-res-amb'

    __verbose = None
    __lfh = None
    __debug = False

    __createSfDict = False
    __omitDistLimitOutlier = True
    __correctCircularShift = True

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

    # AmberPTParserListener.getAtomNumberDict()
    __atomNumberDict = None

    # AMBER atom number dictionary reconstructing from Sander comments
    __sanderAtomNumberDict = None
    __hasComments = False

    # CIF reader
    __cR = None
    __hasCoord = False

    # data item name for model ID in 'atom_site' category
    __modelNumName = None

    # data item names for auth_asym_id, auth_seq_id, auth_atom_id in 'atom_site' category
    __authAsymId = None
    __authSeqId = None
    __authAtomId = None

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
    __authToInsCode = None

    __offsetHolder = None

    __representativeModelId = REPRESENTATIVE_MODEL_ID
    __hasPolySeq = False
    __hasNonPoly = False
    __hasBranched = False
    __hasNonPolySeq = False
    __preferAuthSeq = True
    __gapInAuthSeq = False
    __concatHetero = False

    # polymer sequence of MR file
    __polySeqRst = None

    __seqAlign = None
    __chainAssign = None

    # current restraint subtype
    __cur_subtype = ''

    # last Sander comment
    lastComment = None
    prevComment = None

    lastElemName = None
    lastPlaneSeqId = None

    metalIonMapping = None

    # IAT
    numIatCol = 0
    setIatCol = None
    iat = None

    likeDist = None

    # IGRn
    numIgrCol = None
    setIgrCol = None
    igr = None

    ixpk = -1
    inpk = -1

    iresid = 0

    numAtnamCol = 0
    setAtnamCol = None
    atnam = None

    numGrnamCol = None
    setGrnamCol = None
    grnam = None

    # R1, R2, R3, R4
    lowerLinearLimit = None
    lowerLimit = None
    upperLimit = None
    upperLinearLimit = None

    rstwt = [0.0, 0.0, 0.0, 0.0]  # generalized distance 2/3/4

    # dipolar couplings
    id = None
    jd = None
    dobsl = None
    dobsu = None
    dwt = None
    gigj = None
    dij = None
    ndip = None
    dataset = None
    numDatasets = None
    s11 = None
    s12 = None
    s13 = None
    s22 = None
    s23 = None

    # CSA
    icsa = None
    jcsa = None
    kcsa = None
    cobsl = None
    cobsu = None
    cwt = None
    ncsa = None
    datasetc = None
    sigma11 = None
    sigma12 = None
    sigma13 = None
    sigma22 = None
    sigma23 = None
    field = None

    # PCS
    iprot = None
    obs = None
    wt = None
    tolpro = None
    mltpro = None
    nprot = None
    nmpmc = None
    optphi = None
    opttet = None
    optomg = None
    opta1 = None
    opta2 = None
    optkon = None
    nme = None

    # CS
    shrang = None
    iatr = None
    natr = None
    namr = None
    _str = None
    nring = None
    nter = None
    cter = None

    # NOESY
    ihp = None
    jhp = None
    aexp = None
    arange = None
    awt = None
    emix = None
    npeak = None
    invwt1 = None
    invwt2 = None
    omega = None
    taurot = None
    taumet = None
    id2o = None

    # Amber 10: ambmask
    depth = 0

    hasFuncExprs = False
    funcExprs = None

    inGenDist = False
    inGenDist_funcExprs = None
    inGenDist_weight = None

    inPlane = False
    inPlane_columnSel = -1
    inPlane_funcExprs = None
    inPlane_funcExprs2 = None

    inCom = False
    inCom_funcExprs = None

    # collection of atom selection
    atomSelectionSet = []

    # current residue name for atom name mapping
    __cur_resname_for_mapping = ''

    # unambigous atom name mapping
    unambigAtomNameMapping = {}

    # ambigous atom name mapping
    ambigAtomNameMapping = {}

    __f = __g = None
    warningMessage = None

    reasonsForReParsing = {}

    # original source MR file name
    __originalFileName = '.'

    # list id counter
    __listIdCounter = {}

    # entry ID
    __entryId = '.'

    # dictionary of pynmrstar saveframes
    sfDict = {}

    # last edited pynmrstar saveframe
    __lastSfDict = {}

    def __init__(self, verbose=True, log=sys.stdout,
                 representativeModelId=REPRESENTATIVE_MODEL_ID,
                 mrAtomNameMapping=None,
                 cR=None, caC=None, ccU=None, csStat=None, nefT=None,
                 atomNumberDict=None, reasons=None):
        self.__verbose = verbose
        self.__lfh = log

        self.__representativeModelId = representativeModelId
        self.__mrAtomNameMapping = None if mrAtomNameMapping is None or len(mrAtomNameMapping) == 0 else mrAtomNameMapping

        self.__cR = cR
        self.__hasCoord = cR is not None

        if self.__hasCoord:
            ret = coordAssemblyChecker(verbose, log, representativeModelId, cR, caC)
            self.__modelNumName = ret['model_num_name']
            self.__authAsymId = ret['auth_asym_id']
            self.__authSeqId = ret['auth_seq_id']
            self.__authAtomId = ret['auth_atom_id']
            self.__polySeq = ret['polymer_sequence']
            self.__altPolySeq = ret['alt_polymer_sequence']
            self.__nonPoly = ret['non_polymer']
            self.__branched = ret['branched']
            self.__coordAtomSite = ret['coord_atom_site']
            self.__coordUnobsRes = ret['coord_unobs_res']
            self.__labelToAuthSeq = ret['label_to_auth_seq']
            self.__authToLabelSeq = ret['auth_to_label_seq']
            self.__authToStarSeq = ret['auth_to_star_seq']
            self.__authToInsCode = ret['auth_to_ins_code']

        self.__offsetHolder = {}

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
            if len(self.__polySeq) > 1:
                self.__concatHetero = True
                for ps in self.__polySeq:
                    if 'identical_auth_chain_id' in ps:
                        self.__concatHetero = False
                        break

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

        self.reasonsForReParsing = {}  # reset to prevent interference from the previous run

        if atomNumberDict is not None:
            self.__atomNumberDict = atomNumberDict
        else:
            self.__sanderAtomNumberDict = {}

        self.nmrRestraints = 0       # AMBER: NMR restraints
        self.distRestraints = 0      # AMBER: Distance restraints
        self.angRestraints = 0       # AMBER: Angle restraints
        self.dihedRestraints = 0     # AMBER: Torsional angle restraints
        self.planeRestraints = 0     # AMBER: Plane-point/plane angle restraints
        self.noepkRestraints = 0     # AMBER: NOESY volume restraints
        self.procsRestraints = 0     # AMBER: Chemical shift restraints
        self.pcsRestraints = 0       # AMBER: Psuedocontact shift restraints
        self.rdcRestraints = 0       # AMBER: Direct dipolar coupling restraints
        self.csaRestraints = 0       # AMBER: Residual CSA or pseudo-CSA restraints
        self.geoRestraints = 0       # AMBER: Generalized distance restraints

        # last Sander comment
        self.lastComment = None

        # IAT
        self.numIatCol = 0
        self.setIatCol = None
        self.iat = None

        self.likeDist = None

        # IGRn
        self.numIgrCol = None
        self.setIgrCol = None
        self.igr = None

        self.ixpk = -1
        self.nxpk = -1

        self.iresid = 0

        self.numAtnamCol = 0
        self.setAtnamCol = None
        self.atnam = None

        self.numGrnamCol = None
        self.setGrnamCol = None
        self.grnam = None

        # R1, R2, R3, R4
        self.lowerLinearLimit = None
        self.lowerLimit = None
        self.upperLimit = None
        self.upperLinearLimit = None

        # dipolar couplings
        self.id = None
        self.jd = None
        self.dobsl = None
        self.dobsu = None
        self.dwt = None
        self.gigj = None
        self.dij = None
        self.ndip = None
        self.dataset = None
        self.numDatasets = None
        self.s11 = None
        self.s12 = None
        self.s13 = None
        self.s22 = None
        self.s23 = None

        # CSA
        self.icsa = None
        self.jcsa = None
        self.kcsa = None
        self.cobsl = None
        self.cobsu = None
        self.cwt = None
        self.ncsa = None
        self.datasetc = None
        self.sigma11 = None
        self.sigma12 = None
        self.sigma13 = None
        self.sigma22 = None
        self.sigma23 = None
        self.field = None

        # PCS
        self.iprot = None
        self.obs = None
        self.wt = None
        self.tolpro = None
        self.mltpro = None
        self.nprot = None
        self.nmpmc = None
        self.optphi = None
        self.opttet = None
        self.optomg = None
        self.opta1 = None
        self.opta2 = None
        self.optkon = None
        self.nme = None

        # CS
        self.shrang = None
        self.iatr = None
        self.natr = None
        self.namr = None
        self._str = None
        self.nring = None
        self.nter = None
        self.cter = None

        # NOESY
        self.ihp = None
        self.jhp = None
        self.aexp = None
        self.arange = None
        self.awt = None
        self.emix = None
        self.npeak = None
        self.invwt1 = None
        self.invwt2 = None
        self.omega = None
        self.taurot = None
        self.taumet = None
        self.id2o = None

        self.dist_sander_pat = re.compile(r'(\d+) (\S+) (\S+) '
                                          r'(\d+) (\S+) (\S+) '
                                          r'([-+]?\d*\.?\d+).*')

        self.dist_sander_pat2 = re.compile(r'(\d+) (\S+) (\S+) '
                                           r'(\d+) (\S+) (\S+) '
                                           r'([-+]?\d*\.?\d+) '
                                           r'([-+]?\d*\.?\d+).*')

        self.ang_sander_pat = re.compile(r'(\d+) (\S+) (\S+): '
                                         r'\(\s*(\d+) (\S+) (\S+)\s*\)\s*-\s*'
                                         r'\(\s*(\d+) (\S+) (\S+)\s*\)\s*-\s*'
                                         r'\(\s*(\d+) (\S+) (\S+)\s*\).*')  # r'([-+]?\d*\.?\d+) [-+]?\d*\.?\d+).*')
        self.ang_nang_sander_pat = re.compile(r'N angles for residue (\d+).*')

        self.ang_nang_atoms = [['H', 'N', 'C'],
                               ['H', 'N', 'CA']
                               ]

        self.dihed_sander_pat = re.compile(r'(\d+) (\S+) (\S+): '
                                           r'\(\s*(\d+) (\S+) (\S+)\s*\)\s*-\s*'
                                           r'\(\s*(\d+) (\S+) (\S+)\s*\)\s*-\s*'
                                           r'\(\s*(\d+) (\S+) (\S+)\s*\)\s*-\s*'
                                           r'\(\s*(\d+) (\S+) (\S+)\s*\) '
                                           r'([-+]?\d*\.?\d+) '
                                           r'([-+]?\d*\.?\d+).*')

        self.dihed_sander_pat2 = re.compile(r'\(\s*(\d+) (\S+) (\S+)\s*\)\s*-\s*'
                                            r'\(\s*(\d+) (\S+) (\S+)\s*\)\s*-\s*'
                                            r'\(\s*(\d+) (\S+) (\S+)\s*\)\s*-\s*'
                                            r'\(\s*(\d+) (\S+) (\S+)\s*\) '
                                            r'([-+]?\d*\.?\d+) '
                                            r'([-+]?\d*\.?\d+).*')

        self.dihed_chiral_sander_pat = re.compile(r'chirality for residue (\d+) atoms: '
                                                  r'(\S+) (\S+) (\S+) (\S+).*')
        self.dihed_omega_sander_pat = re.compile(r'trans-omega constraint for residue (\d+).*')

        self.dihed_plane_residue_pat = re.compile(r'PLANAR RESTRAINTS FOR RESIDUE (\d+).*')
        self.dihed_plane_sander_pat = re.compile(r'ANGLE (\S+)\s*-\s*(\S+)\s*-\s*(\S+)\s*-\s*(\S+) -> '
                                                 r'([-+]?\d*\.?\d+).*')

        self.dihed_omega_atoms = ['CA', 'N', 'C', 'CA']  # OMEGA dihedral angle defined by CA(i), N(i), C(i-1), CA(i-1)

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

    # Enter a parse tree produced by AmberMRParser#amber_mr.
    def enterAmber_mr(self, ctx: AmberMRParser.Amber_mrContext):  # pylint: disable=unused-argument
        self.__polySeqRst = []
        self.__f = []
        self.__g = []

    # Exit a parse tree produced by AmberMRParser#amber_mr.
    def exitAmber_mr(self, ctx: AmberMRParser.Amber_mrContext):  # pylint: disable=unused-argument

        try:

            if self.__hasPolySeq and self.__polySeqRst is not None:
                sortPolySeqRst(self.__polySeqRst)

                self.__seqAlign, _ = alignPolymerSequence(self.__pA, self.__polySeq, self.__polySeqRst)
                self.__chainAssign, message = assignPolymerSequence(self.__pA, self.__ccU, self.__file_type, self.__polySeq, self.__polySeqRst, self.__seqAlign)

                if len(message) > 0:
                    self.__f.extend(message)

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

                    if self.__atomNumberDict is None and self.__sanderAtomNumberDict is not None and len(self.__polySeqRst) == 0:

                        for atomNum in self.__sanderAtomNumberDict.values():
                            updatePolySeqRst(self.__polySeqRst, atomNum['chain_id'], atomNum['seq_id'],
                                             atomNum['comp_id'], atomNum.get('auth_comp_id'))

                        sortPolySeqRst(self.__polySeqRst)

                        self.__seqAlign, _ = alignPolymerSequence(self.__pA, self.__polySeq, self.__polySeqRst)
                        self.__chainAssign, message = assignPolymerSequence(self.__pA, self.__ccU, self.__file_type, self.__polySeq, self.__polySeqRst, self.__seqAlign)

                        seq_id_mapping = {}

                        for ca in self.__chainAssign:
                            ref_chain_id = ca['ref_chain_id']
                            test_chain_id = ca['test_chain_id']

                            sa = next((sa for sa in self.__seqAlign
                                       if sa['ref_chain_id'] == ref_chain_id
                                       and sa['test_chain_id'] == test_chain_id), None)

                            if sa is not None:
                                for ref_auth_seq_id, test_seq_id in zip(sa['ref_auth_seq_id'] if 'ref_auth_seq_id' in sa else sa['ref_seq_id'],
                                                                        sa['test_seq_id']):
                                    seq_key = (test_chain_id, test_seq_id)
                                    seq_id_mapping[seq_key] = (ref_chain_id, ref_auth_seq_id)

                        for atomNum in self.__sanderAtomNumberDict.values():
                            test_chain_id = atomNum['chain_id']
                            test_seq_id = atomNum['seq_id']

                            seq_key = (test_chain_id, test_seq_id)

                            if seq_key in seq_id_mapping:
                                ref_chain_id, ref_auth_seq_id = seq_id_mapping[seq_key]
                                atomNum['chain_id'] = ref_chain_id
                                atomNum['seq_id'] = ref_auth_seq_id
                                atomNum['auth_seq_id'] = test_seq_id

                if self.__reasons is None and any(f for f in self.__f if 'Missing data' in f):
                    if len(self.unambigAtomNameMapping) > 0:
                        if 'unambig_atom_id_remap' not in self.reasonsForReParsing:
                            self.reasonsForReParsing['unambig_atom_id_remap'] = self.unambigAtomNameMapping
                    if len(self.ambigAtomNameMapping) > 0:
                        if 'ambig_atom_id_remap' not in self.reasonsForReParsing:
                            self.reasonsForReParsing['ambig_atom_id_remap'] = self.ambigAtomNameMapping

        finally:
            self.warningMessage = sorted(list(set(self.__f)), key=self.__f.index)

    # Enter a parse tree produced by AmberMRParser#comment.
    def enterComment(self, ctx: AmberMRParser.CommentContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#comment.
    def exitComment(self, ctx: AmberMRParser.CommentContext):
        comment = []
        for col in range(20):
            if ctx.Any_name(col):
                text = str(ctx.Any_name(col))
                if text[0] in ('#', '!'):
                    break
                comment.append(str(ctx.Any_name(col)))
            else:
                break
        self.lastComment = None if len(comment) == 0 else ' '.join(comment)

        if self.lastComment:
            if len(comment) == 1 and self.__hasNonPoly:
                self.lastElemName = ''.join([s for s in self.lastComment.upper() if not s.isdigit()])
                if not any(np for np in self.__nonPoly if self.lastElemName in np['auth_comp_id']):
                    self.lastElemName = None
                if self.lastElemName is not None:
                    if self.metalIonMapping is None:
                        self.metalIonMapping = {}
                    self.metalIonMapping[self.lastElemName] = []

            if self.dihed_plane_residue_pat.match(self.lastComment):
                g = self.dihed_plane_residue_pat.search(self.lastComment).groups()
                self.lastPlaneSeqId = int(g[0])

    # Enter a parse tree produced by AmberMRParser#nmr_restraint.
    def enterNmr_restraint(self, ctx: AmberMRParser.Nmr_restraintContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#nmr_restraint.
    def exitNmr_restraint(self, ctx: AmberMRParser.Nmr_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#noesy_volume_restraint.
    def enterNoesy_volume_restraint(self, ctx: AmberMRParser.Noesy_volume_restraintContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#noesy_volume_restraint.
    def exitNoesy_volume_restraint(self, ctx: AmberMRParser.Noesy_volume_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#chemical_shift_restraint.
    def enterChemical_shift_restraint(self, ctx: AmberMRParser.Chemical_shift_restraintContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#chemical_shift_restraint.
    def exitChemical_shift_restraint(self, ctx: AmberMRParser.Chemical_shift_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#pcs_restraint.
    def enterPcs_restraint(self, ctx: AmberMRParser.Pcs_restraintContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#pcs_restraint.
    def exitPcs_restraint(self, ctx: AmberMRParser.Pcs_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#dipolar_coupling_restraint.
    def enterDipolar_coupling_restraint(self, ctx: AmberMRParser.Dipolar_coupling_restraintContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#dipolar_coupling_restraint.
    def exitDipolar_coupling_restraint(self, ctx: AmberMRParser.Dipolar_coupling_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#csa_restraint.
    def enterCsa_restraint(self, ctx: AmberMRParser.Csa_restraintContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#csa_restraint.
    def exitCsa_restraint(self, ctx: AmberMRParser.Csa_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#restraint_statement.
    def enterRestraint_statement(self, ctx: AmberMRParser.Restraint_statementContext):  # pylint: disable=unused-argument
        self.nmrRestraints += 1

        self.__cur_subtype = ''

        self.numIatCol = 0
        self.setIatCol = None
        self.iat = [0] * 8

        self.likeDist = False

        self.numIgrCol = None
        self.setIgrCol = None
        self.igr = None

        self.ixpk = -1
        self.nxpk = -1

        self.iresid = 0

        self.numAtnamCol = 0
        self.setAtnamCol = None
        self.atnam = [''] * 8

        self.numGrnamCol = None
        self.setGrnamCol = None
        self.grnam = None

        # No need to reset R1/2/3/4 because Amber allows to refer the previous value defined
        # self.lowerLinearLimit = None
        # self.lowerLimit = None
        # self.upperLimit = None
        # self.upperLinearLimit = None

        self.hasFuncExprs = False

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by AmberMRParser#restraint_statement.
    def exitRestraint_statement(self, ctx: AmberMRParser.Restraint_statementContext):  # pylint: disable=unused-argument

        try:

            self.detectRestraintType(self.likeDist)

            if len(self.__cur_subtype) == 0:
                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                "Couldn't specify NMR restraint type because the number of columns in the 'iat' clause did not match.")
                return

            # conventional restraint
            if not self.hasFuncExprs:

                if self.setIatCol is not None and len(self.setIatCol) > 0:
                    setIatCol = sorted(self.setIatCol)
                    self.numIatCol = max(setIatCol)
                    if list(range(1, self.numIatCol + 1)) != setIatCol:
                        misIatCol = ','.join([str(col) for col in set(range(1, self.numIatCol + 1)) - set(setIatCol)])
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                        f"Couldn't specify NMR restraint type because of missing 'iat({misIatCol})' clause(s).")
                        return

                # cross-check between IAT and IGRn variables
                for col in range(0, self.numIatCol):
                    iat = self.iat[col]

                    varNum = col + 1
                    varName = 'igr' + str(varNum)

                    if iat > 0 and self.igr is not None and varNum in self.igr:
                        if len(self.igr[varNum]) > 0:
                            nonpCols = [col_ for col_, val in enumerate(self.igr[varNum]) if val <= 0]
                            maxCol = MAX_COL_IGR if len(nonpCols) == 0 else min(nonpCols)
                            valArray = ','.join([str(val) for col_, val in enumerate(self.igr[varNum]) if val > 0 and col_ < maxCol])
                            if len(valArray) > 0:
                                self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                                f"'{varName}={valArray}' has no effect because 'iat({varNum})={iat}'.")
                        del self.igr[varNum]

                    elif iat < 0:
                        if self.igr is None or varNum not in self.igr or len(self.igr[varNum]) == 0:
                            hint = ''
                            if self.ixpk != -1:
                                hint += f"ixpk={self.ixpk},"
                            if self.nxpk != -1:
                                hint += f"nxpk={self.nxpk},"
                            for _col in range(0, self.numIatCol):
                                if _col == col:
                                    continue
                                _varNum = _col + 1
                                if self.iat[_col] > 0:
                                    hint += f"iat({_col+1})={self.iat[_col]},"
                                elif self.igr is not None and _varNum in self.igr:
                                    nonpCols = [col_ for col_, val in enumerate(self.igr[_varNum]) if val <= 0]
                                    maxCol = MAX_COL_IGR if len(nonpCols) == 0 else min(nonpCols)
                                    valArray = ','.join([str(val) for col_, val in enumerate(self.igr[_varNum]) if val > 0 and col_ < maxCol])
                                    hint += f"igr({_col+1})={valArray},"
                            if len(hint) > 0:
                                hint = f" The peripheral atom selections are: {hint[:-1]}."
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"'{varName}' is missing despite being set 'iat({varNum})={iat}'.{hint}")
                        else:
                            nonpCols = [col_ for col_, val in enumerate(self.igr[varNum]) if val <= 0]
                            maxCol = MAX_COL_IGR if len(nonpCols) == 0 else min(nonpCols)
                            valArray = ','.join([str(val) for col_, val in enumerate(self.igr[varNum]) if val > 0 and col_ < maxCol])
                            if len(valArray) == 0:
                                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                f"'{varName}' includes non-positive integers.")
                                del self.igr[varNum]
                            else:
                                nonp = [val for col_, val in enumerate(self.igr[varNum]) if val > 0 and col_ < maxCol]
                                if self.iresid == 0:
                                    if len(nonp) != len(set(nonp)):
                                        if self.__hasPolySeq:
                                            self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                                            f"'{varName}={valArray}' includes redundant integers.")
                                    elif len(nonp) < 2:
                                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                        f"Surprisingly '{varName}={valArray}' consists of a single integer.")
                                else:
                                    mask = [str(val) + '@' + grnam
                                            for col_, (val, grnam) in enumerate(zip(self.igr[varNum], self.grnam[varNum]))
                                            if val > 0 and col_ < maxCol]
                                    varName2 = 'grnam' + str(varNum)
                                    valArray2 = ','.join([val for col_, val in enumerate(self.grnam[varNum]) if len(val) > 0 and col_ < maxCol])
                                    if len(mask) != len(set(mask)):
                                        if self.__hasPolySeq:
                                            self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                                            f"'{varName}={valArray}' and '{varName2}={valArray2}' include redundant atoms.")
                                    elif len(nonp) < 2 or len(mask) < 2:
                                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                        f"Surprisingly '{varName}={valArray}' consists of a single integer "
                                                        f"or '{varName2}={valArray2}' consists of a single string.")
                                self.igr[varNum] = list(set(nonp))  # trimming non-positive/redundant integer

                self.iat = self.iat[0:self.numIatCol]  # trimming default zero integer

                # convert AMBER atom numbers to corresponding coordinate atoms based on AMBER parameter/topology file
                if self.__atomNumberDict is not None or self.iresid == 1:

                    self.__hasComments = True

                    chk_dihed = mis_dihed = False

                    subtype_name = ''
                    if self.__cur_subtype == 'dist':
                        subtype_name = ' as a distance restraint'
                    elif self.__cur_subtype == 'geo':
                        subtype_name = ' as a generalized distance restraint'
                    elif self.__cur_subtype == 'ang':
                        subtype_name = ' as an angle restraint'
                    elif self.__cur_subtype == 'dihed':
                        subtype_name = ' as a dihedral angle restraint'
                        if self.iresid == 0:
                            chk_dihed = True
                            mis_iat = None
                            dihed_factors = {}
                            self.__g.clear()
                    lastComment = str(self.lastComment)
                    hint = '' if lastComment is None else\
                        (" or ambiguous atom name mapping information generated by 'makeDIST_RST' should be attached to the AMBER restraint file "
                         f"for interpretation of Sander comment {lastComment!r}{subtype_name}, "
                         if 'AMB' in lastComment and (('-' in lastComment and ':' in lastComment) or '.' in lastComment)
                         else f" or Sander comment {lastComment!r} couldn't be interpreted{subtype_name}")

                    for col, iat in enumerate(self.iat):

                        atomSelection = []

                        if self.iresid == 0:

                            if iat > 0:
                                if iat in self.__atomNumberDict:
                                    atomSelection.append(copy.copy(self.__atomNumberDict[iat]))
                                    if chk_dihed:
                                        dihed_factors[col] = copy.copy(self.__atomNumberDict[iat])
                                else:
                                    if chk_dihed:
                                        mis_dihed = True
                                        mis_iat = iat
                                        self.__g.append(f"[Missing data] {self.__getCurrentRestraint()}"
                                                        f"'iat({col+1})={iat}' is not defined in the AMBER parameter/topology file{hint}.")
                                    else:
                                        self.__f.append(f"[Missing data] {self.__getCurrentRestraint()}"
                                                        f"'iat({col+1})={iat}' is not defined in the AMBER parameter/topology file{hint}.")
                            elif iat < 0:
                                varNum = col + 1
                                if self.igr is None:
                                    self.__f.append(f"[Missing data] {self.__getCurrentRestraint()}"
                                                    f"'igr({varNum})' is not defined in the AMBER parameter/topology file{hint}.")
                                elif varNum in self.igr:
                                    for igr in self.igr[varNum]:
                                        if igr in self.__atomNumberDict:
                                            atomSelection.append(copy.copy(self.__atomNumberDict[igr]))
                                        else:
                                            self.__f.append(f"[Missing data] {self.__getCurrentRestraint()}"
                                                            f"'igr({varNum})={igr}' is not defined in the AMBER parameter/topology file{hint}.")

                        else:

                            if iat > 0:
                                if col >= len(self.atnam):
                                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                    f"'atnam({col+1})' is missing despite being set iresid=1, iat({col+1})={iat}.")
                                else:
                                    atnam = self.atnam[col]
                                    if len(atnam) == 0:
                                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                        f"'atnam({col+1})={atnam}' is empty despite being set iresid=1, iat({col+1})={iat}.")
                                    else:
                                        factor = self.getAtomNumberDictFromAmbmaskInfo(iat, self.atnam[col])
                                        if factor is not None:
                                            atomSelection.append(factor)

                            elif iat < 0:
                                varNum = col + 1
                                if self.igr is None:
                                    self.__f.append(f"[Missing data] {self.__getCurrentRestraint()}"
                                                    f"'igr({varNum})' is not defined in the AMBER parameter/topology file{hint}.")
                                elif varNum in self.igr:
                                    if varNum not in self.grnam:
                                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                        f"'grnam({varNum})' is missing despite being set iresid=1, igr({varNum})={self.igr[varNum]}.")
                                    else:
                                        for igr, grnam in zip(self.igr[varNum], self.grnam[varNum]):
                                            if len(grnam) == 0:
                                                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                                f"'grnam({varNum})={self.grnam[varNum]}' is empty "
                                                                f"despite being set iresid=1, igr({varNum})={self.igr[varNum]}.")
                                            else:
                                                for order in range(6):
                                                    factor = self.getAtomNumberDictFromAmbmaskInfo(igr, grnam, order)
                                                    if factor is None:
                                                        break
                                                    atomSelection.append(factor)

                        self.atomSelectionSet.append(atomSelection)

                    if chk_dihed and mis_dihed:
                        rescued = True
                        compId = next((v['comp_id'] for v in dihed_factors.values()), None)
                        if len(dihed_factors) < 3 or 0 not in dihed_factors or 3 not in dihed_factors\
                           or dihed_factors[0]['seq_id'] != dihed_factors[3]['seq_id'] or not self.__ccU.updateChemCompDict(compId):
                            rescued = False
                        else:
                            mis_idx = 1 if 1 not in dihed_factors else 2
                            atomId1 = next((cca[self.__ccU.ccaAtomId] for cca in self.__ccU.lastAtomList
                                            if cca[self.__ccU.ccaAtomId] == dihed_factors[mis_idx - 1]['atom_id']), None)
                            atomId2 = next((cca[self.__ccU.ccaAtomId] for cca in self.__ccU.lastAtomList
                                            if cca[self.__ccU.ccaAtomId] == dihed_factors[mis_idx + 1]['atom_id']), None)
                            if atomId1 is None or atomId2 is None:
                                rescued = False
                            else:
                                bondedTo1 = self.__ccU.getBondedAtoms(compId, atomId1)
                                bondedTo2 = self.__ccU.getBondedAtoms(compId, atomId2)
                                commonAtomId = set(bondedTo1).intersection(bondedTo2)
                                if len(commonAtomId) != 1:
                                    rescued = False
                                else:
                                    _factor = copy.copy(dihed_factors[0])
                                    _factor['atom_id'] = _factor['auth_atom_id'] = list(commonAtomId)[0]
                                    self.__atomNumberDict[mis_iat] = _factor
                                    self.atomSelectionSet.insert(mis_idx, [_factor])

                        if not rescued:
                            self.__f.extend(self.__g)

                    if self.lastComment is not None:
                        if self.__debug:
                            print('# ' + self.lastComment)

                    updatePolySeqRstFromAtomSelectionSet(self.__polySeqRst, self.atomSelectionSet)

                    if any(len(atomSelection) == 0 for atomSelection in self.atomSelectionSet):
                        return

                    if self.__cur_subtype in ('dist', 'geo'):

                        dstFunc = self.validateDistanceRange(1.0)

                        if dstFunc is None:
                            return

                        lenIat = len(self.iat)

                        # simple distance
                        if lenIat == COL_DIST:

                            if self.__createSfDict:
                                sf = self.__getSf(constraintType=getDistConstraintType(self.atomSelectionSet, dstFunc,
                                                                                       self.__csStat, self.__originalFileName),
                                                  potentialType=getPotentialType(self.__file_type, self.__cur_subtype, dstFunc))
                                sf['id'] += 1
                                memberLogicCode = 'OR' if len(self.atomSelectionSet[0]) * len(self.atomSelectionSet[1]) > 1 else '.'

                                memberId = '.'
                                if memberLogicCode == 'OR':
                                    if len(self.atomSelectionSet[0]) * len(self.atomSelectionSet[1]) > 1\
                                       and (isAmbigAtomSelection(self.atomSelectionSet[0], self.__csStat)
                                            or isAmbigAtomSelection(self.atomSelectionSet[1], self.__csStat)):
                                        memberId = 0
                                        _atom1 = _atom2 = None

                            for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                                  self.atomSelectionSet[1]):
                                if isIdenticalRestraint([atom1, atom2]):
                                    continue
                                if self.__debug:
                                    print(f"subtype={self.__cur_subtype} id={self.distRestraints} "
                                          f"atom1={atom1} atom2={atom2} {dstFunc}")
                                if self.__createSfDict and sf is not None:
                                    if isinstance(memberId, int):
                                        if _atom1 is None or isAmbigAtomSelection([_atom1, atom1], self.__csStat)\
                                           or isAmbigAtomSelection([_atom2, atom2], self.__csStat):
                                            memberId += 1
                                            _atom1, _atom2 = atom1, atom2
                                    sf['index_id'] += 1
                                    row = getRow(self.__cur_subtype, sf['id'], sf['index_id'],
                                                 '.', memberId, memberLogicCode,
                                                 sf['list_id'], self.__entryId, dstFunc,
                                                 self.__authToStarSeq, self.__authToInsCode, self.__offsetHolder,
                                                 atom1, atom2)
                                    sf['loop'].add_data(row)

                                    if sf['constraint_subsubtype'] == 'ambi':
                                        continue

                                    if memberLogicCode == 'OR'\
                                       and (isAmbigAtomSelection(self.atomSelectionSet[0], self.__csStat)
                                            or isAmbigAtomSelection(self.atomSelectionSet[1], self.__csStat)):
                                        sf['constraint_subsubtype'] = 'ambi'
                                    if 'upper_limit' in dstFunc and dstFunc['upper_limit'] is not None:
                                        upperLimit = float(dstFunc['upper_limit'])
                                        if upperLimit <= DIST_AMBIG_LOW or upperLimit >= DIST_AMBIG_UP:
                                            sf['constraint_subsubtype'] = 'ambi'

                        # generalized distance
                        else:

                            # generalized distance 2
                            if lenIat == COL_DIST_COORD2:

                                if self.__createSfDict:
                                    sf = self.__getSf('AMBER generalized distance restraint of 4 atoms')
                                    sf['id'] += 1
                                    if len(sf['loop']['tags']) == 0:
                                        sf['loop']['tags'] = ['index_id', 'id',
                                                              'auth_asym_id_1', 'auth_seq_id_1', 'auth_comp_id_1', 'auth_atom_id_1',
                                                              'auth_asym_id_2', 'auth_seq_id_2', 'auth_comp_id_2', 'auth_atom_id_2',
                                                              'auth_asym_id_3', 'auth_seq_id_3', 'auth_comp_id_3', 'auth_atom_id_3',
                                                              'auth_asym_id_4', 'auth_seq_id_4', 'auth_comp_id_4', 'auth_atom_id_4'
                                                              'target_value', 'target_value_uncertainty',
                                                              'lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit',
                                                              'weight_1', 'weight_2',
                                                              'list_id', 'entry_id']

                                for atom1, atom2, atom3, atom4 in itertools.product(self.atomSelectionSet[0],
                                                                                    self.atomSelectionSet[1],
                                                                                    self.atomSelectionSet[2],
                                                                                    self.atomSelectionSet[3]):
                                    if self.__debug:
                                        print(f"subtype={self.__cur_subtype} id={self.geoRestraints} "
                                              f"weight={self.inGenDist_weight} "
                                              f"|atom1={atom1} atom2={atom2}| "
                                              f"|atom3={atom3} atom4={atom4}| "
                                              f"{dstFunc}")
                                    if self.__createSfDict and sf is not None:
                                        sf['index_id'] += 1
                                        sf['loop']['data'].append([sf['index_id'], sf['id'],
                                                                   atom1['chain_id'], atom1['seq_id'], atom1['comp_id'], atom1['atom_id'],
                                                                   atom2['chain_id'], atom2['seq_id'], atom2['comp_id'], atom2['atom_id'],
                                                                   atom3['chain_id'], atom3['seq_id'], atom3['comp_id'], atom3['atom_id'],
                                                                   atom4['chain_id'], atom4['seq_id'], atom4['comp_id'], atom4['atom_id'],
                                                                   dstFunc.get('target_value'), None,
                                                                   dstFunc.get('lower_linear_limit'),
                                                                   dstFunc.get('lower_limit'),
                                                                   dstFunc.get('upper_limit'),
                                                                   dstFunc.get('upper_linear_limit'),
                                                                   self.inGenDist_weight[0], self.inGenDist_weight[1],
                                                                   sf['list_id'], self.__entryId])

                            # generalized distance 3
                            elif lenIat == COL_DIST_COORD3:

                                if self.__createSfDict:
                                    sf = self.__getSf('AMBER generalized distance restraint of 6 atoms')
                                    sf['id'] += 1
                                    if len(sf['loop']['tags']) == 0:
                                        sf['loop']['tags'] = ['index_id', 'id',
                                                              'auth_asym_id_1', 'auth_seq_id_1', 'auth_comp_id_1', 'auth_atom_id_1',
                                                              'auth_asym_id_2', 'auth_seq_id_2', 'auth_comp_id_2', 'auth_atom_id_2',
                                                              'auth_asym_id_3', 'auth_seq_id_3', 'auth_comp_id_3', 'auth_atom_id_3',
                                                              'auth_asym_id_4', 'auth_seq_id_4', 'auth_comp_id_4', 'auth_atom_id_4'
                                                              'auth_asym_id_5', 'auth_seq_id_5', 'auth_comp_id_5', 'auth_atom_id_5',
                                                              'auth_asym_id_6', 'auth_seq_id_6', 'auth_comp_id_6', 'auth_atom_id_6'
                                                              'target_value', 'target_value_uncertainty',
                                                              'lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit',
                                                              'weight_1', 'weight_2', 'weight_3',
                                                              'list_id', 'entry_id']

                                for atom1, atom2, atom3, atom4, atom5, atom6 in itertools.product(self.atomSelectionSet[0],
                                                                                                  self.atomSelectionSet[1],
                                                                                                  self.atomSelectionSet[2],
                                                                                                  self.atomSelectionSet[3],
                                                                                                  self.atomSelectionSet[4],
                                                                                                  self.atomSelectionSet[5]):
                                    if self.__debug:
                                        print(f"subtype={self.__cur_subtype} id={self.geoRestraints} "
                                              f"weight={self.inGenDist_weight} "
                                              f"|atom1={atom1} atom2={atom2}| "
                                              f"|atom3={atom3} atom4={atom4}| "
                                              f"|atom5={atom5} atom6={atom6}| "
                                              f"{dstFunc}")
                                    if self.__createSfDict and sf is not None:
                                        sf['index_id'] += 1
                                        sf['loop']['data'].append([sf['index_id'], sf['id'],
                                                                   atom1['chain_id'], atom1['seq_id'], atom1['comp_id'], atom1['atom_id'],
                                                                   atom2['chain_id'], atom2['seq_id'], atom2['comp_id'], atom2['atom_id'],
                                                                   atom3['chain_id'], atom3['seq_id'], atom3['comp_id'], atom3['atom_id'],
                                                                   atom4['chain_id'], atom4['seq_id'], atom4['comp_id'], atom4['atom_id'],
                                                                   atom5['chain_id'], atom5['seq_id'], atom5['comp_id'], atom5['atom_id'],
                                                                   atom6['chain_id'], atom6['seq_id'], atom6['comp_id'], atom6['atom_id'],
                                                                   dstFunc.get('target_value'), None,
                                                                   dstFunc.get('lower_linear_limit'),
                                                                   dstFunc.get('lower_limit'),
                                                                   dstFunc.get('upper_limit'),
                                                                   dstFunc.get('upper_linear_limit'),
                                                                   self.inGenDist_weight[0], self.inGenDist_weight[1], self.inGenDist_weight[2],
                                                                   sf['list_id'], self.__entryId])

                            # generalized distance 4
                            else:

                                if self.__createSfDict:
                                    sf = self.__getSf('AMBER generalized distance restraint of 8 atoms')
                                    sf['id'] += 1
                                    if len(sf['loop']['tags']) == 0:
                                        sf['loop']['tags'] = ['index_id', 'id',
                                                              'auth_asym_id_1', 'auth_seq_id_1', 'auth_comp_id_1', 'auth_atom_id_1',
                                                              'auth_asym_id_2', 'auth_seq_id_2', 'auth_comp_id_2', 'auth_atom_id_2',
                                                              'auth_asym_id_3', 'auth_seq_id_3', 'auth_comp_id_3', 'auth_atom_id_3',
                                                              'auth_asym_id_4', 'auth_seq_id_4', 'auth_comp_id_4', 'auth_atom_id_4'
                                                              'auth_asym_id_5', 'auth_seq_id_5', 'auth_comp_id_5', 'auth_atom_id_5',
                                                              'auth_asym_id_6', 'auth_seq_id_6', 'auth_comp_id_6', 'auth_atom_id_6'
                                                              'auth_asym_id_7', 'auth_seq_id_7', 'auth_comp_id_7', 'auth_atom_id_7',
                                                              'auth_asym_id_8', 'auth_seq_id_8', 'auth_comp_id_8', 'auth_atom_id_8'
                                                              'target_value', 'target_value_uncertainty',
                                                              'lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit',
                                                              'weight_1', 'weight_2', 'weight_3', 'weight_4',
                                                              'list_id', 'entry_id']

                                for atom1, atom2, atom3, atom4, atom5, atom6, atom7, atom8 in itertools.product(self.atomSelectionSet[0],
                                                                                                                self.atomSelectionSet[1],
                                                                                                                self.atomSelectionSet[2],
                                                                                                                self.atomSelectionSet[3],
                                                                                                                self.atomSelectionSet[4],
                                                                                                                self.atomSelectionSet[5],
                                                                                                                self.atomSelectionSet[6],
                                                                                                                self.atomSelectionSet[7]):
                                    if self.__debug:
                                        print(f"subtype={self.__cur_subtype} id={self.geoRestraints} "
                                              f"weight={self.inGenDist_weight} "
                                              f"|atom1={atom1} atom2={atom2}| "
                                              f"|atom3={atom3} atom4={atom4}| "
                                              f"|atom5={atom5} atom6={atom6}| "
                                              f"|atom7={atom7} atom8={atom8}| "
                                              f"{dstFunc}")
                                    if self.__createSfDict and sf is not None:
                                        sf['index_id'] += 1
                                        sf['loop']['data'].append([sf['index_id'], sf['id'],
                                                                   atom1['chain_id'], atom1['seq_id'], atom1['comp_id'], atom1['atom_id'],
                                                                   atom2['chain_id'], atom2['seq_id'], atom2['comp_id'], atom2['atom_id'],
                                                                   atom3['chain_id'], atom3['seq_id'], atom3['comp_id'], atom3['atom_id'],
                                                                   atom4['chain_id'], atom4['seq_id'], atom4['comp_id'], atom4['atom_id'],
                                                                   atom5['chain_id'], atom5['seq_id'], atom5['comp_id'], atom5['atom_id'],
                                                                   atom6['chain_id'], atom6['seq_id'], atom6['comp_id'], atom6['atom_id'],
                                                                   atom7['chain_id'], atom7['seq_id'], atom7['comp_id'], atom7['atom_id'],
                                                                   atom8['chain_id'], atom8['seq_id'], atom8['comp_id'], atom8['atom_id'],
                                                                   dstFunc.get('target_value'), None,
                                                                   dstFunc.get('lower_linear_limit'),
                                                                   dstFunc.get('lower_limit'),
                                                                   dstFunc.get('upper_limit'),
                                                                   dstFunc.get('upper_linear_limit'),
                                                                   self.inGenDist_weight[0], self.inGenDist_weight[1],
                                                                   self.inGenDist_weight[2], self.inGenDist_weight[3],
                                                                   sf['list_id'], self.__entryId])

                            self.rstwt = [0.0, 0.0, 0.0, 0.0]

                    # angle
                    elif self.__cur_subtype == 'ang':
                        valid = True
                        for col, iat in enumerate(self.iat):
                            if iat < 0:
                                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                f"Ambiguous atom selection 'iat({col+1})={iat}' is not allowed as a angle restraint.")
                                valid = False
                        if not valid:
                            return

                        dstFunc = self.validateAngleRange(1.0)

                        if dstFunc is None:
                            return

                        if self.__createSfDict:
                            sf = self.__getSf('angle restraint')
                            sf['id'] += 1
                            if len(sf['loop']['tags']) == 0:
                                sf['loop']['tags'] = ['index_id', 'id',
                                                      'auth_asym_id_1', 'auth_seq_id_1', 'auth_comp_id_1', 'auth_atom_id_1',
                                                      'auth_asym_id_2', 'auth_seq_id_2', 'auth_comp_id_2', 'auth_atom_id_2',
                                                      'auth_asym_id_3', 'auth_seq_id_3', 'auth_comp_id_3', 'auth_atom_id_3',
                                                      'target_value', 'target_value_uncertainty',
                                                      'lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit',
                                                      'list_id', 'entry_id']

                        for atom1, atom2, atom3 in itertools.product(self.atomSelectionSet[0],
                                                                     self.atomSelectionSet[1],
                                                                     self.atomSelectionSet[2]):
                            if isLongRangeRestraint([atom1, atom2, atom3], self.__polySeq if self.__gapInAuthSeq else None):
                                continue
                            if self.__debug:
                                print(f"subtype={self.__cur_subtype} id={self.angRestraints} "
                                      f"atom1={atom1} atom2={atom2} atom3={atom3} {dstFunc}")
                            if self.__createSfDict and sf is not None:
                                sf['index_id'] += 1
                                sf['loop']['data'].append([sf['index_id'], sf['id'],
                                                           atom1['chain_id'], atom1['seq_id'], atom1['comp_id'], atom1['atom_id'],
                                                           atom2['chain_id'], atom2['seq_id'], atom2['comp_id'], atom2['atom_id'],
                                                           atom3['chain_id'], atom3['seq_id'], atom3['comp_id'], atom3['atom_id'],
                                                           dstFunc.get('target_value'), None,
                                                           dstFunc.get('lower_linear_limit'),
                                                           dstFunc.get('lower_limit'),
                                                           dstFunc.get('upper_limit'),
                                                           dstFunc.get('upper_linear_limit'),
                                                           sf['list_id'], self.__entryId])

                    # torsional angle
                    elif self.__cur_subtype == 'dihed':
                        valid = True
                        for col, iat in enumerate(self.iat):
                            if iat < 0:
                                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                f"Ambiguous atom selection 'iat({col+1})={iat}' is not allowed as a torsional angle restraint.")
                                valid = False
                        if not valid:
                            return

                        dstFunc = self.validateAngleRange(1.0)

                        if dstFunc is None:
                            return

                        if len(self.atomSelectionSet[0]) == 0:
                            return

                        if self.__createSfDict:
                            sf = self.__getSf(potentialType=getPotentialType(self.__file_type, self.__cur_subtype, dstFunc))

                        compId = self.atomSelectionSet[0][0]['comp_id']
                        peptide, nucleotide, carbohydrate = self.__csStat.getTypeOfCompId(compId)

                        first_item = True

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
                                if first_item:
                                    sf['id'] += 1
                                    first_item = False
                                sf['index_id'] += 1
                                row = getRow(self.__cur_subtype, sf['id'], sf['index_id'],
                                             '.', None, angleName,
                                             sf['list_id'], self.__entryId, dstFunc,
                                             self.__authToStarSeq, self.__authToInsCode, self.__offsetHolder,
                                             atom1, atom2, atom3, atom4)
                                sf['loop'].add_data(row)

                    # plane-(point/plane) angle
                    else:
                        valid = True
                        for col, iat in enumerate(self.iat):
                            if iat < 0:
                                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                f"Ambiguous atom selection 'iat({col+1})={iat}' is not allowed as a plane-(point/plane) angle restraint.")
                                valid = False
                        if not valid:
                            return

                        dstFunc = self.validateAngleRange(1.0)

                        if dstFunc is None:
                            return

                        # plane-point angle
                        if lenIat == COL_PLANE_POINT:

                            if self.__createSfDict:
                                sf = self.__getSf('AMBER plane-point angle restraint')
                                sf['id'] += 1
                                if len(sf['loop']['tags']) == 0:
                                    sf['loop']['tags'] = ['index_id', 'id',
                                                          'plane_auth_asym_id_1', 'plane_auth_seq_id_1', 'plane_auth_comp_id_1', 'plane_auth_atom_id_1',
                                                          'plane_auth_asym_id_2', 'plane_auth_seq_id_2', 'plane_auth_comp_id_2', 'plane_auth_atom_id_2',
                                                          'plane_auth_asym_id_3', 'plane_auth_seq_id_3', 'plane_auth_comp_id_3', 'plane_auth_atom_id_3',
                                                          'plane_auth_asym_id_4', 'plane_auth_seq_id_4', 'plane_auth_comp_id_4', 'plane_auth_atom_id_4'
                                                          'point_auth_asym_id', 'point_auth_seq_id', 'ponit_auth_comp_id', 'point_auth_atom_id',
                                                          'target_value', 'target_value_uncertainty',
                                                          'lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit',
                                                          'list_id', 'entry_id']

                            for atom1, atom2, atom3, atom4, atom5 in itertools.product(self.atomSelectionSet[0],
                                                                                       self.atomSelectionSet[1],
                                                                                       self.atomSelectionSet[2],
                                                                                       self.atomSelectionSet[3],
                                                                                       self.atomSelectionSet[4]):
                                if self.__debug:
                                    print(f"subtype={self.__cur_subtype} id={self.planeRestraints} "
                                          f"plane: |atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4}| "
                                          f"point: atom={atom5}"
                                          f"{dstFunc}")
                                if self.__createSfDict and sf is not None:
                                    sf['index_id'] += 1
                                    sf['loop']['data'].append([sf['index_id'], sf['id'],
                                                               atom1['chain_id'], atom1['seq_id'], atom1['comp_id'], atom1['atom_id'],
                                                               atom2['chain_id'], atom2['seq_id'], atom2['comp_id'], atom2['atom_id'],
                                                               atom3['chain_id'], atom3['seq_id'], atom3['comp_id'], atom3['atom_id'],
                                                               atom4['chain_id'], atom4['seq_id'], atom4['comp_id'], atom4['atom_id'],
                                                               atom5['chain_id'], atom5['seq_id'], atom5['comp_id'], atom5['atom_id'],
                                                               dstFunc.get('target_value'), None,
                                                               dstFunc.get('lower_linear_limit'),
                                                               dstFunc.get('lower_limit'),
                                                               dstFunc.get('upper_limit'),
                                                               dstFunc.get('upper_linear_limit'),
                                                               sf['list_id'], self.__entryId])

                        # plane-plane angle
                        else:

                            if self.__createSfDict:
                                sf = self.__getSf('AMBER plane-plane angle restraint')
                                sf['id'] += 1
                                if len(sf['loop']['tags']) == 0:
                                    sf['loop']['tags'] = ['index_id', 'id',
                                                          'plane_1_auth_asym_id_1', 'plane_1_auth_seq_id_1', 'plane_1_auth_comp_id_1', 'plane_1_auth_atom_id_1',
                                                          'plane_1_auth_asym_id_2', 'plane_1_auth_seq_id_2', 'plane_1_auth_comp_id_2', 'plane_1_auth_atom_id_2',
                                                          'plane_1_auth_asym_id_3', 'plane_1_auth_seq_id_3', 'plane_1_auth_comp_id_3', 'plane_1_auth_atom_id_3',
                                                          'plane_1_auth_asym_id_4', 'plane_1_auth_seq_id_4', 'plane_1_auth_comp_id_4', 'plane_1_auth_atom_id_4'
                                                          'plane_2_auth_asym_id_5', 'plane_2_auth_seq_id_5', 'plane_2_auth_comp_id_5', 'plane_2_auth_atom_id_5',
                                                          'plane_2_auth_asym_id_6', 'plane_2_auth_seq_id_6', 'plane_2_auth_comp_id_6', 'plane_2_auth_atom_id_6'
                                                          'plane_2_auth_asym_id_7', 'plane_2_auth_seq_id_7', 'plane_2_auth_comp_id_7', 'plane_2_auth_atom_id_7',
                                                          'plane_2_auth_asym_id_8', 'plane_2_auth_seq_id_8', 'plane_2_auth_comp_id_8', 'plane_2_auth_atom_id_8'
                                                          'target_value', 'target_value_uncertainty',
                                                          'lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit',
                                                          'list_id', 'entry_id']

                            for atom1, atom2, atom3, atom4, atom5, atom6, atom7, atom8 in itertools.product(self.atomSelectionSet[0],
                                                                                                            self.atomSelectionSet[1],
                                                                                                            self.atomSelectionSet[2],
                                                                                                            self.atomSelectionSet[3],
                                                                                                            self.atomSelectionSet[4],
                                                                                                            self.atomSelectionSet[5],
                                                                                                            self.atomSelectionSet[6],
                                                                                                            self.atomSelectionSet[7]):
                                if self.__debug:
                                    print(f"subtype={self.__cur_subtype} id={self.planeRestraints} "
                                          f"plane1: |atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4}| "
                                          f"plane2: |atom1={atom5} atom2={atom6} atom3={atom7} atom4={atom8}| "
                                          f"{dstFunc}")
                                if self.__createSfDict and sf is not None:
                                    sf['index_id'] += 1
                                    sf['loop']['data'].append([sf['index_id'], sf['id'],
                                                               atom1['chain_id'], atom1['seq_id'], atom1['comp_id'], atom1['atom_id'],
                                                               atom2['chain_id'], atom2['seq_id'], atom2['comp_id'], atom2['atom_id'],
                                                               atom3['chain_id'], atom3['seq_id'], atom3['comp_id'], atom3['atom_id'],
                                                               atom4['chain_id'], atom4['seq_id'], atom4['comp_id'], atom4['atom_id'],
                                                               atom5['chain_id'], atom5['seq_id'], atom5['comp_id'], atom5['atom_id'],
                                                               atom6['chain_id'], atom6['seq_id'], atom6['comp_id'], atom6['atom_id'],
                                                               atom7['chain_id'], atom7['seq_id'], atom7['comp_id'], atom7['atom_id'],
                                                               atom8['chain_id'], atom8['seq_id'], atom8['comp_id'], atom8['atom_id'],
                                                               dstFunc.get('target_value'), None,
                                                               dstFunc.get('lower_linear_limit'),
                                                               dstFunc.get('lower_limit'),
                                                               dstFunc.get('upper_limit'),
                                                               dstFunc.get('upper_linear_limit'),
                                                               sf['list_id'], self.__entryId])

                # try to update AMBER atom number dictionary based on Sander comments
                elif self.__hasPolySeq and self.iresid == 0:

                    self.__hasComments = True

                    if self.__cur_subtype == 'dist' and len(self.iat) == COL_DIST:
                        subtype_name = 'distance restraint'

                        e = self.lastElemName

                        g = None\
                            if self.lastComment is None or not self.dist_sander_pat.match(self.lastComment)\
                            else self.dist_sander_pat.search(self.lastComment).groups()

                        for col, iat in enumerate(self.iat):
                            offset = col * 3

                            if iat > 0:
                                if iat in self.__sanderAtomNumberDict:
                                    pass
                                else:
                                    if g is None and (e is None or col > 0):
                                        self.reportSanderCommentIssue(subtype_name)
                                        return
                                    if g is not None:
                                        factor = {'auth_seq_id': int(g[offset + 0]),
                                                  'auth_comp_id': g[offset + 1],
                                                  'auth_atom_id': g[offset + 2],
                                                  'iat': iat
                                                  }
                                        if not self.updateSanderAtomNumberDict(factor):
                                            if 'AMB' in g[offset + 1] and ((':' in g[offset + 2] and '-' in g[offset + 2]) or '.' in g[offset + 2]):
                                                self.__f.append(f"[Missing data] {self.__getCurrentRestraint()}"
                                                                f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                                f"based on Sander comment {' '.join(g[offset:offset+3])!r}. "
                                                                "Please attach ambiguous atom name mapping information generated by 'makeDIST_RST' to the AMBER restraint file.")
                                            else:
                                                _factor = self.getAtomNumberDictFromAmbmaskInfo(int(g[offset + 0]), g[offset + 2])
                                                if _factor is None:
                                                    if all(iat for iat in self.iat if iat > 0):
                                                        _col = (col + 1) % 2
                                                        _offset = _col * 3
                                                        _factor = {'auth_seq_id': int(g[_offset + 0]),
                                                                   'auth_comp_id': g[_offset + 1],
                                                                   'auth_atom_id': g[_offset + 2],
                                                                   'iat': self.iat[_col]
                                                                   }
                                                        if self.updateSanderAtomNumberDict(_factor):
                                                            around = float(g[6]) + 1.0

                                                            g2 = None\
                                                                if self.lastComment is None or not self.dist_sander_pat2.match(self.lastComment)\
                                                                else self.dist_sander_pat2.search(self.lastComment).groups()

                                                            if g2 is not None:
                                                                _around = max(float(g2[6]), float(g2[7]))
                                                                around = max(around, _around)

                                                            factor = self.getNeighborCandidateAtom(factor, self.__sanderAtomNumberDict[self.iat[_col]], around)
                                                            if factor is not None:
                                                                if self.updateSanderAtomNumberDict(factor):
                                                                    continue
                                                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                                    f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                                    f"based on Sander comment {' '.join(g[offset:offset+3])!r}.")
                                                    continue
                                                factor = {'auth_seq_id': int(g[offset + 0]),
                                                          'auth_comp_id': _factor['comp_id'],  # pylint: disable=unsubscriptable-object
                                                          'auth_atom_id': _factor['atom_id'],  # pylint: disable=unsubscriptable-object
                                                          'iat': iat
                                                          }
                                                if not self.updateSanderAtomNumberDict(factor):
                                                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                                    f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                                    f"based on Sander comment {' '.join(g[offset:offset+3])!r}.")

                                    else:
                                        s = None
                                        for np in self.__nonPoly:
                                            for _s, _c in zip(np['auth_seq_id'], np['auth_comp_id']):
                                                if _c != e:
                                                    continue
                                                if _s in self.metalIonMapping[e]:
                                                    continue
                                                s = _s
                                                break
                                            if s is not None:
                                                break
                                        if s is None:
                                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                            f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                            f"based on Sander comment {e!r}.")
                                        else:
                                            factor = {'auth_seq_id': s,
                                                      'auth_comp_id': e,
                                                      'auth_atom_id': e,
                                                      'iat': iat
                                                      }
                                            if self.updateSanderAtomNumberDict(factor):
                                                self.metalIonMapping[e].append(s)
                                            else:
                                                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                                f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                                f"based on Sander comment {e!r}.")

                            elif iat < 0:
                                varNum = col + 1
                                if self.igr is None:
                                    self.__f.append(f"[Missing data] {self.__getCurrentRestraint()}"
                                                    f"'igr({varNum})' is not defined in the AMBER parameter/topology file{hint}.")
                                elif varNum in self.igr:
                                    igr = self.igr[varNum]
                                    if igr[0] not in self.__sanderAtomNumberDict:
                                        if g is None:
                                            self.reportSanderCommentIssue(subtype_name)
                                            return
                                        factor = {'auth_seq_id': int(g[offset + 0]),
                                                  'auth_comp_id': g[offset + 1],
                                                  'auth_atom_id': g[offset + 2],
                                                  'igr': igr
                                                  }
                                        if not self.updateSanderAtomNumberDict(factor):
                                            if 'AMB' in g[offset + 1] and ((':' in g[offset + 2] and '-' in g[offset + 2]) or '.' in g[offset + 2]):
                                                self.__f.append(f"[Missing data] {self.__getCurrentRestraint()}"
                                                                f"Couldn't specify 'igr({varNum})={igr}' in the coordinates "
                                                                f"based on Sander comment {' '.join(g[offset:offset+3])!r}. "
                                                                "Please attach ambiguous atom name mapping information generated by 'makeDIST_RST' to the AMBER restraint file.")
                                            else:
                                                for order, iat in enumerate(igr):
                                                    _factor = self.getAtomNumberDictFromAmbmaskInfo(int(g[offset + 0]), g[offset + 2], order)
                                                    if _factor is None:
                                                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                                        f"Couldn't specify 'igr({varNum})={igr}' in the coordinates "
                                                                        f"based on Sander comment {' '.join(g[offset:offset+3])!r}.")
                                                        break
                                                    factor = {'auth_seq_id': int(g[offset + 0]),
                                                              'auth_comp_id': _factor['comp_id'],  # pylint: disable=unsubscriptable-object
                                                              'auth_atom_id': _factor['atom_id'],  # pylint: disable=unsubscriptable-object
                                                              'iat': iat
                                                              }
                                                    if not self.updateSanderAtomNumberDict(factor):
                                                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                                        f"Couldn't specify 'igr({varNum})={igr}' in the coordinates "
                                                                        f"based on Sander comment {' '.join(g[offset:offset+3])!r}.")

                    if self.__cur_subtype == 'ang':
                        subtype_name = 'angle restraint'

                        g = None\
                            if self.lastComment is None or not self.ang_sander_pat.match(self.lastComment)\
                            else self.ang_sander_pat.search(self.lastComment).groups()

                        gn = None\
                            if self.lastComment is None or not self.ang_nang_sander_pat.match(self.lastComment)\
                            else self.ang_nang_sander_pat.search(self.lastComment).groups()

                        _gn = None\
                            if self.lastComment is not None or gn is not None or self.prevComment is None\
                            or not self.ang_nang_sander_pat.match(self.prevComment)\
                            else self.ang_nang_sander_pat.search(self.prevComment).groups()

                        if _gn is not None:
                            for col, iat in enumerate(self.iat):

                                if iat > 0:
                                    if iat in self.__sanderAtomNumberDict:
                                        pass
                                    else:
                                        seqId = int(_gn[0])
                                        atomId = self.ang_nang_atoms[1][col]
                                        _factor = self.getAtomNumberDictFromAmbmaskInfo(seqId, atomId)
                                        if _factor is None:
                                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                            f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                            f"based on Sander comment {self.prevComment!r}.")
                                            continue
                                        factor = {'auth_seq_id': seqId,
                                                  'auth_comp_id': _factor['comp_id'],  # pylint: disable=unsubscriptable-object
                                                  'auth_atom_id': atomId,
                                                  'iat': iat
                                                  }
                                        if not self.updateSanderAtomNumberDict(factor):
                                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                            f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                            f"based on Sander comment {self.prevComment!r}.")

                            self.prevComment = None

                        elif gn is not None:
                            for col, iat in enumerate(self.iat):

                                if iat > 0:
                                    if iat in self.__sanderAtomNumberDict:
                                        pass
                                    else:
                                        seqId = int(gn[0])
                                        atomId = self.ang_nang_atoms[0][col]
                                        _factor = self.getAtomNumberDictFromAmbmaskInfo(seqId, atomId)
                                        if _factor is None:
                                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                            f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                            f"based on Sander comment {self.lastComment!r}.")
                                            continue
                                        factor = {'auth_seq_id': seqId,
                                                  'auth_comp_id': _factor['comp_id'],  # pylint: disable=unsubscriptable-object
                                                  'auth_atom_id': atomId,
                                                  'iat': iat
                                                  }
                                        if not self.updateSanderAtomNumberDict(factor):
                                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                            f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                            f"based on Sander comment {self.lastComment!r}.")

                        else:
                            for col, iat in enumerate(self.iat):
                                offset = col * 3 + 3

                                if iat > 0:
                                    if iat in self.__sanderAtomNumberDict:
                                        pass
                                    else:
                                        if g is None:
                                            self.reportSanderCommentIssue(subtype_name)
                                            return
                                        factor = {'auth_seq_id': int(g[offset + 0]),
                                                  'auth_comp_id': g[offset + 1],
                                                  'auth_atom_id': g[offset + 2],
                                                  'iat': iat
                                                  }
                                        if not self.updateSanderAtomNumberDict(factor):
                                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                            f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                            f"based on Sander comment {' '.join(g[offset:offset+3])!r}.")

                    if self.__cur_subtype == 'dihed':
                        subtype_name = 'torsional angle restraint'

                        g = None\
                            if self.lastComment is None or not self.dihed_sander_pat.match(self.lastComment)\
                            else self.dihed_sander_pat.search(self.lastComment).groups()

                        g2 = None\
                            if self.lastComment is None or not self.dihed_sander_pat2.match(self.lastComment)\
                            else self.dihed_sander_pat2.search(self.lastComment).groups()

                        gc = None\
                            if self.lastComment is None or not self.dihed_chiral_sander_pat.match(self.lastComment)\
                            else self.dihed_chiral_sander_pat.search(self.lastComment).groups()

                        go = None\
                            if self.lastComment is None or not self.dihed_omega_sander_pat.match(self.lastComment)\
                            else self.dihed_omega_sander_pat.search(self.lastComment).groups()

                        gp = None\
                            if self.lastComment is None or self.lastPlaneSeqId is None or not self.dihed_plane_sander_pat.match(self.lastComment)\
                            else self.dihed_plane_sander_pat.search(self.lastComment).groups()

                        if gp is not None:
                            for col, iat in enumerate(self.iat):

                                if iat > 0:
                                    if iat in self.__sanderAtomNumberDict:
                                        pass
                                    else:
                                        factor = {'auth_seq_id': self.lastPlaneSeqId,
                                                  'auth_atom_id': gp[col],
                                                  'iat': iat
                                                  }
                                        if not self.updateSanderAtomNumberDict(factor):
                                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                            f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                            f"based on Sander comment 'PLANAR RESTRAINTS FOR RESIDUE {self.lastPlaneSeqId}' and {gp[col]!r}.")

                        if go is not None:
                            for col, iat in enumerate(self.iat):

                                if iat > 0:
                                    if iat in self.__sanderAtomNumberDict:
                                        pass
                                    else:
                                        seqId = int(go[0])
                                        if col >= 2:
                                            seqId -= 1
                                        atomId = self.dihed_omega_atoms[col]
                                        _factor = self.getAtomNumberDictFromAmbmaskInfo(seqId, atomId)
                                        if _factor is None:
                                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                            f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                            f"based on Sander comment {self.lastComment!r}.")
                                            continue
                                        factor = {'auth_seq_id': seqId,
                                                  'auth_comp_id': _factor['comp_id'],  # pylint: disable=unsubscriptable-object
                                                  'auth_atom_id': atomId,
                                                  'iat': iat
                                                  }
                                        if not self.updateSanderAtomNumberDict(factor):
                                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                            f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                            f"based on Sander comment {self.lastComment!r}.")

                        elif gc is not None:
                            for col, iat in enumerate(self.iat):

                                if iat > 0:
                                    if iat in self.__sanderAtomNumberDict:
                                        pass
                                    else:
                                        seqId = int(gc[0])
                                        atomId = gc[col + 1]
                                        _factor = self.getAtomNumberDictFromAmbmaskInfo(seqId, atomId)
                                        if _factor is None:
                                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                            f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                            f"based on Sander comment {self.lastComment!r}.")
                                            continue
                                        factor = {'auth_seq_id': seqId,
                                                  'auth_comp_id': _factor['comp_id'],  # pylint: disable=unsubscriptable-object
                                                  'auth_atom_id': atomId,
                                                  'iat': iat
                                                  }
                                        if not self.updateSanderAtomNumberDict(factor):
                                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                            f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                            f"based on Sander comment {self.lastComment!r}.")

                        else:
                            for col, iat in enumerate(self.iat):
                                offset = col * 3 + 3
                                offset2 = col * 3

                                if iat > 0:
                                    if iat in self.__sanderAtomNumberDict:
                                        pass
                                    else:
                                        if g is None and g2 is None:
                                            self.reportSanderCommentIssue(subtype_name)
                                            return
                                        if g is not None:
                                            factor = {'auth_seq_id': int(g[offset + 0]),
                                                      'auth_comp_id': g[offset + 1],
                                                      'auth_atom_id': g[offset + 2],
                                                      'iat': iat
                                                      }
                                            if not self.updateSanderAtomNumberDict(factor):
                                                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                                f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                                f"based on Sander comment {' '.join(g[offset:offset+3])!r}.")
                                        else:
                                            factor = {'auth_seq_id': int(g2[offset2 + 0]),
                                                      'auth_comp_id': g2[offset2 + 1],
                                                      'auth_atom_id': g2[offset2 + 2],
                                                      'iat': iat
                                                      }
                                            if not self.updateSanderAtomNumberDict(factor):
                                                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                                f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                                f"based on Sander comment {' '.join(g2[offset2:offset2+3])!r}.")

                elif self.lastComment is not None:
                    if not self.__hasComments:
                        self.__hasComments = True

            # Amber 10: ambmask
            else:

                self.__hasComments = True

                # convert AMBER atom numbers to corresponding coordinate atoms based on AMBER parameter/topology file
                if self.__atomNumberDict is not None:

                    # 1st plane should be processed at first due to plane-point angle restraint
                    if self.__cur_subtype == 'plane':

                        for col, funcExpr in enumerate(self.inPlane_funcExprs):

                            atomSelection = []

                            if isinstance(funcExpr, dict):
                                if 'iat' in funcExpr:
                                    iat = funcExpr['iat']
                                    if iat in self.__atomNumberDict:
                                        atomSelection.append(copy.copy(self.__atomNumberDict[iat]))
                                    else:
                                        self.__f.append(f"[Missing data] {self.__getCurrentRestraint()}"
                                                        f"'iat({col+1})={iat}' is not defined in the AMBER parameter/topology file.")
                                else:  # ambmask format
                                    factor = self.getAtomNumberDictFromAmbmaskInfo(funcExpr['seq_id'], funcExpr['atom_id'])
                                    if factor is not None:
                                        atomSelection.append(factor)
                            else:  # list
                                rawExprs = []
                                for _funcExpr in funcExpr:
                                    if 'igr' in _funcExpr:
                                        rawExprs.append(str(_funcExpr['igr']))
                                    else:  # ambmask format
                                        rawExprs.append(f":{_funcExpr['seq_id']}@{_funcExpr['atom_id']}")
                                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                f"Ambiguous atom selection 'igr({col+1})={', '.join(rawExprs)}' is not allowed as a plane-(point/plane) angle restraint.")
                                return

                            self.atomSelectionSet.append(atomSelection)

                    for col, funcExpr in enumerate(self.funcExprs):

                        atomSelection = []

                        if isinstance(funcExpr, dict):
                            if 'iat' in funcExpr:
                                iat = funcExpr['iat']
                                if iat in self.__atomNumberDict:
                                    atomSelection.append(copy.copy(self.__atomNumberDict[iat]))
                                else:
                                    self.__f.append(f"[Missing data] {self.__getCurrentRestraint()}"
                                                    f"'iat({col+1})={iat}' is not defined in the AMBER parameter/topology file.")
                            else:  # ambmask format
                                factor = self.getAtomNumberDictFromAmbmaskInfo(funcExpr['seq_id'], funcExpr['atom_id'])
                                if factor is not None:
                                    atomSelection.append(factor)
                        else:  # list
                            for _funcExpr in funcExpr:
                                if 'igr' in _funcExpr:
                                    igr = _funcExpr['igr']
                                    if igr in self.__atomNumberDict:
                                        atomSelection.append(copy.copy(self.__atomNumberDict[igr]))
                                    else:
                                        self.__f.append(f"[Missing data] {self.__getCurrentRestraint()}"
                                                        f"'igr({col+1})={igr}' is not defined in the AMBER parameter/topology file.")
                                else:  # ambmask format
                                    factor = self.getAtomNumberDictFromAmbmaskInfo(_funcExpr['seq_id'], _funcExpr['atom_id'])
                                    if factor is not None:
                                        atomSelection.append(factor)

                        self.atomSelectionSet.append(atomSelection)

                    if self.lastComment is not None:
                        if self.__debug:
                            print('# ' + self.lastComment)

                    updatePolySeqRstFromAtomSelectionSet(self.__polySeqRst, self.atomSelectionSet)

                    if any(len(atomSelection) == 0 for atomSelection in self.atomSelectionSet):
                        return

                    if self.__cur_subtype in ('dist', 'geo'):

                        dstFunc = self.validateDistanceRange(1.0)

                        if dstFunc is None:
                            return

                        # simple distance
                        if not self.inGenDist:

                            if self.__createSfDict:
                                sf = self.__getSf(constraintType=getDistConstraintType(self.atomSelectionSet, dstFunc,
                                                                                       self.__csStat, self.__originalFileName),
                                                  potentialType=getPotentialType(self.__file_type, self.__cur_subtype, dstFunc))
                                sf['id'] += 1
                                memberLogicCode = 'OR' if len(self.atomSelectionSet[0]) * len(self.atomSelectionSet[1]) > 1 else '.'

                                memberId = '.'
                                if memberLogicCode == 'OR':
                                    if len(self.atomSelectionSet[0]) * len(self.atomSelectionSet[1]) > 1\
                                       and (isAmbigAtomSelection(self.atomSelectionSet[0], self.__csStat)
                                            or isAmbigAtomSelection(self.atomSelectionSet[1], self.__csStat)):
                                        memberId = 0
                                        _atom1 = _atom2 = None

                            for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                                  self.atomSelectionSet[1]):
                                if isIdenticalRestraint([atom1, atom2]):
                                    continue
                                if self.__debug:
                                    print(f"subtype={self.__cur_subtype} id={self.distRestraints} "
                                          f"atom1={atom1} atom2={atom2} {dstFunc}")
                                if self.__createSfDict and sf is not None:
                                    if isinstance(memberId, int):
                                        if _atom1 is None or isAmbigAtomSelection([_atom1, atom1], self.__csStat)\
                                           or isAmbigAtomSelection([_atom2, atom2], self.__csStat):
                                            memberId += 1
                                            _atom1, _atom2 = atom1, atom2
                                    sf['index_id'] += 1
                                    row = getRow(self.__cur_subtype, sf['id'], sf['index_id'],
                                                 '.', memberId, memberLogicCode,
                                                 sf['list_id'], self.__entryId, dstFunc,
                                                 self.__authToStarSeq, self.__authToInsCode, self.__offsetHolder,
                                                 atom1, atom2)
                                    sf['loop'].add_data(row)

                                    if sf['constraint_subsubtype'] == 'ambi':
                                        continue

                                    if memberLogicCode == 'OR'\
                                       and (isAmbigAtomSelection(self.atomSelectionSet[0], self.__csStat)
                                            or isAmbigAtomSelection(self.atomSelectionSet[1], self.__csStat)):
                                        sf['constraint_subsubtype'] = 'ambi'
                                    if 'upper_limit' in dstFunc and dstFunc['upper_limit'] is not None:
                                        upperLimit = float(dstFunc['upper_limit'])
                                        if upperLimit <= DIST_AMBIG_LOW or upperLimit >= DIST_AMBIG_UP:
                                            sf['constraint_subsubtype'] = 'ambi'

                        # generalized distance
                        else:

                            for col, funcExpr in enumerate(self.inGenDist_funcExprs):

                                atomSelection = []

                                if isinstance(funcExpr, dict):
                                    if 'iat' in funcExpr:
                                        iat = funcExpr['iat']
                                        if iat in self.__atomNumberDict:
                                            atomSelection.append(copy.copy(self.__atomNumberDict[iat]))
                                        else:
                                            self.__f.append(f"[Missing data] {self.__getCurrentRestraint()}"
                                                            f"'iat({col+1})={iat}' is not defined in the AMBER parameter/topology file.")
                                    else:  # ambmask format
                                        factor = self.getAtomNumberDictFromAmbmaskInfo(funcExpr['seq_id'], funcExpr['atom_id'])
                                        if factor is not None:
                                            atomSelection.append(factor)
                                else:  # list
                                    for _funcExpr in funcExpr:
                                        if 'igr' in _funcExpr:
                                            igr = _funcExpr['igr']
                                            if igr in self.__atomNumberDict:
                                                atomSelection.append(copy.copy(self.__atomNumberDict[igr]))
                                            else:
                                                self.__f.append(f"[Missing data] {self.__getCurrentRestraint()}"
                                                                f"'igr({col+1})={igr}' is not defined in the AMBER parameter/topology file.")
                                        else:  # ambmask format
                                            factor = self.getAtomNumberDictFromAmbmaskInfo(_funcExpr['seq_id'], _funcExpr['atom_id'])
                                            if factor is not None:
                                                atomSelection.append(factor)

                                self.atomSelectionSet.append(atomSelection)

                            lenWeight = len(self.inGenDist_weight)

                            # generalized distance 2
                            if lenWeight == 2:

                                if self.__createSfDict:
                                    sf = self.__getSf('AMBER generalized distance restraint of 4 atoms')
                                    sf['id'] += 1
                                    if len(sf['loop']['tags']) == 0:
                                        sf['loop']['tags'] = ['index_id', 'id',
                                                              'auth_asym_id_1', 'auth_seq_id_1', 'auth_comp_id_1', 'auth_atom_id_1',
                                                              'auth_asym_id_2', 'auth_seq_id_2', 'auth_comp_id_2', 'auth_atom_id_2',
                                                              'auth_asym_id_3', 'auth_seq_id_3', 'auth_comp_id_3', 'auth_atom_id_3',
                                                              'auth_asym_id_4', 'auth_seq_id_4', 'auth_comp_id_4', 'auth_atom_id_4'
                                                              'target_value', 'target_value_uncertainty',
                                                              'lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit',
                                                              'weight_1', 'weight_2',
                                                              'list_id', 'entry_id']

                                for atom1, atom2, atom3, atom4 in itertools.product(self.atomSelectionSet[0],
                                                                                    self.atomSelectionSet[1],
                                                                                    self.atomSelectionSet[2],
                                                                                    self.atomSelectionSet[3]):
                                    if self.__debug:
                                        print(f"subtype={self.__cur_subtype} id={self.geoRestraints} "
                                              f"weight={self.inGenDist_weight} "
                                              f"|atom1={atom1} atom2={atom2}| "
                                              f"|atom3={atom3} atom4={atom4}| "
                                              f"{dstFunc}")
                                    if self.__createSfDict and sf is not None:
                                        sf['index_id'] += 1
                                        sf['loop']['data'].append([sf['index_id'], sf['id'],
                                                                   atom1['chain_id'], atom1['seq_id'], atom1['comp_id'], atom1['atom_id'],
                                                                   atom2['chain_id'], atom2['seq_id'], atom2['comp_id'], atom2['atom_id'],
                                                                   atom3['chain_id'], atom3['seq_id'], atom3['comp_id'], atom3['atom_id'],
                                                                   atom4['chain_id'], atom4['seq_id'], atom4['comp_id'], atom4['atom_id'],
                                                                   dstFunc.get('target_value'), None,
                                                                   dstFunc.get('lower_linear_limit'),
                                                                   dstFunc.get('lower_limit'),
                                                                   dstFunc.get('upper_limit'),
                                                                   dstFunc.get('upper_linear_limit'),
                                                                   self.inGenDist_weight[0], self.inGenDist_weight[1],
                                                                   sf['list_id'], self.__entryId])

                            # generalized distance 3
                            elif lenWeight == 3:

                                if self.__createSfDict:
                                    sf = self.__getSf('AMBER generalized distance restraint of 6 atoms')
                                    sf['id'] += 1
                                    if len(sf['loop']['tags']) == 0:
                                        sf['loop']['tags'] = ['index_id', 'id',
                                                              'auth_asym_id_1', 'auth_seq_id_1', 'auth_comp_id_1', 'auth_atom_id_1',
                                                              'auth_asym_id_2', 'auth_seq_id_2', 'auth_comp_id_2', 'auth_atom_id_2',
                                                              'auth_asym_id_3', 'auth_seq_id_3', 'auth_comp_id_3', 'auth_atom_id_3',
                                                              'auth_asym_id_4', 'auth_seq_id_4', 'auth_comp_id_4', 'auth_atom_id_4'
                                                              'auth_asym_id_5', 'auth_seq_id_5', 'auth_comp_id_5', 'auth_atom_id_5',
                                                              'auth_asym_id_6', 'auth_seq_id_6', 'auth_comp_id_6', 'auth_atom_id_6'
                                                              'target_value', 'target_value_uncertainty',
                                                              'lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit',
                                                              'weight_1', 'weight_2', 'weight_3',
                                                              'list_id', 'entry_id']

                                for atom1, atom2, atom3, atom4, atom5, atom6 in itertools.product(self.atomSelectionSet[0],
                                                                                                  self.atomSelectionSet[1],
                                                                                                  self.atomSelectionSet[2],
                                                                                                  self.atomSelectionSet[3],
                                                                                                  self.atomSelectionSet[4],
                                                                                                  self.atomSelectionSet[5]):
                                    if self.__debug:
                                        print(f"subtype={self.__cur_subtype} id={self.geoRestraints} "
                                              f"weight={self.inGenDist_weight} "
                                              f"|atom1={atom1} atom2={atom2}| "
                                              f"|atom3={atom3} atom4={atom4}| "
                                              f"|atom5={atom5} atom6={atom6}| "
                                              f"{dstFunc}")
                                    if self.__createSfDict and sf is not None:
                                        sf['index_id'] += 1
                                        sf['loop']['data'].append([sf['index_id'], sf['id'],
                                                                   atom1['chain_id'], atom1['seq_id'], atom1['comp_id'], atom1['atom_id'],
                                                                   atom2['chain_id'], atom2['seq_id'], atom2['comp_id'], atom2['atom_id'],
                                                                   atom3['chain_id'], atom3['seq_id'], atom3['comp_id'], atom3['atom_id'],
                                                                   atom4['chain_id'], atom4['seq_id'], atom4['comp_id'], atom4['atom_id'],
                                                                   atom5['chain_id'], atom5['seq_id'], atom5['comp_id'], atom5['atom_id'],
                                                                   atom6['chain_id'], atom6['seq_id'], atom6['comp_id'], atom6['atom_id'],
                                                                   dstFunc.get('target_value'), None,
                                                                   dstFunc.get('lower_linear_limit'),
                                                                   dstFunc.get('lower_limit'),
                                                                   dstFunc.get('upper_limit'),
                                                                   dstFunc.get('upper_linear_limit'),
                                                                   self.inGenDist_weight[0], self.inGenDist_weight[1], self.inGenDist_weight[2],
                                                                   sf['list_id'], self.__entryId])

                            # generalized distance 4
                            else:

                                if self.__createSfDict:
                                    sf = self.__getSf('AMBER generalized distance restraint of 8 atoms')
                                    sf['id'] += 1
                                    if len(sf['loop']['tags']) == 0:
                                        sf['loop']['tags'] = ['index_id', 'id',
                                                              'auth_asym_id_1', 'auth_seq_id_1', 'auth_comp_id_1', 'auth_atom_id_1',
                                                              'auth_asym_id_2', 'auth_seq_id_2', 'auth_comp_id_2', 'auth_atom_id_2',
                                                              'auth_asym_id_3', 'auth_seq_id_3', 'auth_comp_id_3', 'auth_atom_id_3',
                                                              'auth_asym_id_4', 'auth_seq_id_4', 'auth_comp_id_4', 'auth_atom_id_4'
                                                              'auth_asym_id_5', 'auth_seq_id_5', 'auth_comp_id_5', 'auth_atom_id_5',
                                                              'auth_asym_id_6', 'auth_seq_id_6', 'auth_comp_id_6', 'auth_atom_id_6'
                                                              'auth_asym_id_7', 'auth_seq_id_7', 'auth_comp_id_7', 'auth_atom_id_7',
                                                              'auth_asym_id_8', 'auth_seq_id_8', 'auth_comp_id_8', 'auth_atom_id_8'
                                                              'target_value', 'target_value_uncertainty',
                                                              'lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit',
                                                              'weight_1', 'weight_2', 'weight_3', 'weight_4',
                                                              'list_id', 'entry_id']

                                for atom1, atom2, atom3, atom4, atom5, atom6, atom7, atom8 in itertools.product(self.atomSelectionSet[0],
                                                                                                                self.atomSelectionSet[1],
                                                                                                                self.atomSelectionSet[2],
                                                                                                                self.atomSelectionSet[3],
                                                                                                                self.atomSelectionSet[4],
                                                                                                                self.atomSelectionSet[5],
                                                                                                                self.atomSelectionSet[6],
                                                                                                                self.atomSelectionSet[7]):
                                    if self.__debug:
                                        print(f"subtype={self.__cur_subtype} id={self.geoRestraints} "
                                              f"weight={self.inGenDist_weight} "
                                              f"|atom1={atom1} atom2={atom2}| "
                                              f"|atom3={atom3} atom4={atom4}| "
                                              f"|atom5={atom5} atom6={atom6}| "
                                              f"|atom7={atom7} atom8={atom8}| "
                                              f"{dstFunc}")
                                    if self.__createSfDict and sf is not None:
                                        sf['index_id'] += 1
                                        sf['loop']['data'].append([sf['index_id'], sf['id'],
                                                                   atom1['chain_id'], atom1['seq_id'], atom1['comp_id'], atom1['atom_id'],
                                                                   atom2['chain_id'], atom2['seq_id'], atom2['comp_id'], atom2['atom_id'],
                                                                   atom3['chain_id'], atom3['seq_id'], atom3['comp_id'], atom3['atom_id'],
                                                                   atom4['chain_id'], atom4['seq_id'], atom4['comp_id'], atom4['atom_id'],
                                                                   atom5['chain_id'], atom5['seq_id'], atom5['comp_id'], atom5['atom_id'],
                                                                   atom6['chain_id'], atom6['seq_id'], atom6['comp_id'], atom6['atom_id'],
                                                                   atom7['chain_id'], atom7['seq_id'], atom7['comp_id'], atom7['atom_id'],
                                                                   atom8['chain_id'], atom8['seq_id'], atom8['comp_id'], atom8['atom_id'],
                                                                   dstFunc.get('target_value'), None,
                                                                   dstFunc.get('lower_linear_limit'),
                                                                   dstFunc.get('lower_limit'),
                                                                   dstFunc.get('upper_limit'),
                                                                   dstFunc.get('upper_linear_limit'),
                                                                   self.inGenDist_weight[0], self.inGenDist_weight[1],
                                                                   self.inGenDist_weight[2], self.inGenDist_weight[3],
                                                                   sf['list_id'], self.__entryId])

                            self.rstwt = [0.0, 0.0, 0.0, 0.0]

                    # angle
                    elif self.__cur_subtype == 'ang':
                        valid = True
                        for col, funcExpr in enumerate(self.funcExprs):
                            if isinstance(funcExpr, list):
                                rawExprs = []
                                for _funcExpr in funcExpr:
                                    if 'igr' in _funcExpr:
                                        rawExprs.append(str(_funcExpr['igr']))
                                    else:  # ambmask format
                                        rawExprs.append(f":{_funcExpr['seq_id']}@{_funcExpr['atom_id']}")
                                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                f"Ambiguous atom selection 'igr({col+1})={', '.join(rawExprs)}' is not allowed as an angle restraint.")
                                valid = False
                        if not valid:
                            return

                        dstFunc = self.validateAngleRange(1.0)

                        if dstFunc is None:
                            return

                        if self.__createSfDict:
                            sf = self.__getSf('angle restraint')
                            sf['id'] += 1
                            if len(sf['loop']['tags']) == 0:
                                sf['loop']['tags'] = ['index_id', 'id',
                                                      'auth_asym_id_1', 'auth_seq_id_1', 'auth_comp_id_1', 'auth_atom_id_1',
                                                      'auth_asym_id_2', 'auth_seq_id_2', 'auth_comp_id_2', 'auth_atom_id_2',
                                                      'auth_asym_id_3', 'auth_seq_id_3', 'auth_comp_id_3', 'auth_atom_id_3',
                                                      'target_value', 'target_value_uncertainty',
                                                      'lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit',
                                                      'list_id', 'entry_id']

                        for atom1, atom2, atom3 in itertools.product(self.atomSelectionSet[0],
                                                                     self.atomSelectionSet[1],
                                                                     self.atomSelectionSet[2]):
                            if isLongRangeRestraint([atom1, atom2, atom3], self.__polySeq if self.__gapInAuthSeq else None):
                                continue
                            if self.__debug:
                                print(f"subtype={self.__cur_subtype} id={self.angRestraints} "
                                      f"atom1={atom1} atom2={atom2} atom3={atom3} {dstFunc}")
                            if self.__createSfDict and sf is not None:
                                sf['index_id'] += 1
                                sf['loop']['data'].append([sf['index_id'], sf['id'],
                                                           atom1['chain_id'], atom1['seq_id'], atom1['comp_id'], atom1['atom_id'],
                                                           atom2['chain_id'], atom2['seq_id'], atom2['comp_id'], atom2['atom_id'],
                                                           atom3['chain_id'], atom3['seq_id'], atom3['comp_id'], atom3['atom_id'],
                                                           dstFunc.get('target_value'), None,
                                                           dstFunc.get('lower_linear_limit'),
                                                           dstFunc.get('lower_limit'),
                                                           dstFunc.get('upper_limit'),
                                                           dstFunc.get('upper_linear_limit'),
                                                           sf['list_id'], self.__entryId])

                    # torsional angle
                    elif self.__cur_subtype == 'dihed':
                        valid = True
                        for col, funcExpr in enumerate(self.funcExprs):
                            if isinstance(funcExpr, list):
                                rawExprs = []
                                for _funcExpr in funcExpr:
                                    if 'igr' in _funcExpr:
                                        rawExprs.append(str(_funcExpr['igr']))
                                    else:  # ambmask format
                                        rawExprs.append(f":{_funcExpr['seq_id']}@{_funcExpr['atom_id']}")
                                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                f"Ambiguous atom selection 'igr({col+1})={', '.join(rawExprs)}' is not allowed as a torsional angle restraint.")
                                valid = False
                        if not valid:
                            return

                        dstFunc = self.validateAngleRange(1.0)

                        if dstFunc is None:
                            return

                        if len(self.atomSelectionSet[0]) == 0:
                            return

                        if self.__createSfDict:
                            sf = self.__getSf(potentialType=getPotentialType(self.__file_type, self.__cur_subtype, dstFunc))

                        compId = self.atomSelectionSet[0][0]['comp_id']
                        peptide, nucleotide, carbohydrate = self.__csStat.getTypeOfCompId(compId)

                        first_item = True

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
                                if first_item:
                                    sf['id'] += 1
                                    first_item = False
                                sf['index_id'] += 1
                                row = getRow(self.__cur_subtype, sf['id'], sf['index_id'],
                                             '.', None, angleName,
                                             sf['list_id'], self.__entryId, dstFunc,
                                             self.__authToStarSeq, self.__authToInsCode, self.__offsetHolder,
                                             atom1, atom2, atom3, atom4)
                                sf['loop'].add_data(row)

                    # plane-(point/plane) angle
                    else:

                        dstFunc = self.validateAngleRange(1.0)

                        if dstFunc is None:
                            return

                        # plane-point angle
                        if self.inPlane_columnSel == 0:

                            for col, funcExpr in enumerate(self.funcExprs, 4):
                                if isinstance(funcExpr, list):
                                    rawExprs = []
                                    for _funcExpr in funcExpr:
                                        if 'igr' in _funcExpr:
                                            rawExprs.append(str(_funcExpr['igr']))
                                        else:  # ambmask format
                                            rawExprs.append(f":{_funcExpr['seq_id']}@{_funcExpr['atom_id']}")
                                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                    f"Ambiguous atom selection 'igr({col+1})={', '.join(rawExprs)}' is not allowed as a plane-point angle restraint.")
                                    return

                            if self.__createSfDict:
                                sf = self.__getSf('AMBER plane-point angle restraint')
                                sf['id'] += 1
                                if len(sf['loop']['tags']) == 0:
                                    sf['loop']['tags'] = ['index_id', 'id',
                                                          'plane_auth_asym_id_1', 'plane_auth_seq_id_1', 'plane_auth_comp_id_1', 'plane_auth_atom_id_1',
                                                          'plane_auth_asym_id_2', 'plane_auth_seq_id_2', 'plane_auth_comp_id_2', 'plane_auth_atom_id_2',
                                                          'plane_auth_asym_id_3', 'plane_auth_seq_id_3', 'plane_auth_comp_id_3', 'plane_auth_atom_id_3',
                                                          'plane_auth_asym_id_4', 'plane_auth_seq_id_4', 'plane_auth_comp_id_4', 'plane_auth_atom_id_4'
                                                          'point_auth_asym_id', 'point_auth_seq_id', 'ponit_auth_comp_id', 'point_auth_atom_id',
                                                          'target_value', 'target_value_uncertainty',
                                                          'lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit',
                                                          'list_id', 'entry_id']

                            for atom1, atom2, atom3, atom4, atom5 in itertools.product(self.atomSelectionSet[0],
                                                                                       self.atomSelectionSet[1],
                                                                                       self.atomSelectionSet[2],
                                                                                       self.atomSelectionSet[3],
                                                                                       self.atomSelectionSet[4]):
                                if self.__debug:
                                    print(f"subtype={self.__cur_subtype} id={self.planeRestraints} "
                                          f"plane: |atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4}| "
                                          f"point: atom={atom5}"
                                          f"{dstFunc}")
                                if self.__createSfDict and sf is not None:
                                    sf['index_id'] += 1
                                    sf['loop']['data'].append([sf['index_id'], sf['id'],
                                                               atom1['chain_id'], atom1['seq_id'], atom1['comp_id'], atom1['atom_id'],
                                                               atom2['chain_id'], atom2['seq_id'], atom2['comp_id'], atom2['atom_id'],
                                                               atom3['chain_id'], atom3['seq_id'], atom3['comp_id'], atom3['atom_id'],
                                                               atom4['chain_id'], atom4['seq_id'], atom4['comp_id'], atom4['atom_id'],
                                                               atom5['chain_id'], atom5['seq_id'], atom5['comp_id'], atom5['atom_id'],
                                                               dstFunc.get('target_value'), None,
                                                               dstFunc.get('lower_linear_limit'),
                                                               dstFunc.get('lower_limit'),
                                                               dstFunc.get('upper_limit'),
                                                               dstFunc.get('upper_linear_limit'),
                                                               sf['list_id'], self.__entryId])

                        # plane-plane angle
                        else:

                            # 2nd plane
                            for col, funcExpr in enumerate(self.inPlane_funcExprs2, 4):

                                atomSelection = []

                                if isinstance(funcExpr, dict):
                                    if 'iat' in funcExpr:
                                        iat = funcExpr['iat']
                                        if iat in self.__atomNumberDict:
                                            atomSelection.append(copy.copy(self.__atomNumberDict[iat]))
                                        else:
                                            self.__f.append(f"[Missing data] {self.__getCurrentRestraint()}"
                                                            f"'iat({col+1})={iat}' is not defined in the AMBER parameter/topology file.")
                                    else:  # ambmask format
                                        factor = self.getAtomNumberDictFromAmbmaskInfo(funcExpr['seq_id'], funcExpr['atom_id'])
                                        if factor is not None:
                                            atomSelection.append(factor)
                                else:  # list
                                    rawExprs = []
                                    for _funcExpr in funcExpr:
                                        if 'igr' in _funcExpr:
                                            rawExprs.append(str(_funcExpr['igr']))
                                        else:  # ambmask format
                                            rawExprs.append(f":{_funcExpr['seq_id']}@{_funcExpr['atom_id']}")
                                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                    f"Ambiguous atom selection 'igr({col+1})={', '.join(rawExprs)}' is not allowed as a plane-plane angle restraint.")
                                    return

                                self.atomSelectionSet.append(atomSelection)

                            if self.__createSfDict:
                                sf = self.__getSf('AMBER plane-plane angle restraint')
                                sf['id'] += 1
                                if len(sf['loop']['tags']) == 0:
                                    sf['loop']['tags'] = ['index_id', 'id',
                                                          'plane_1_auth_asym_id_1', 'plane_1_auth_seq_id_1', 'plane_1_auth_comp_id_1', 'plane_1_auth_atom_id_1',
                                                          'plane_1_auth_asym_id_2', 'plane_1_auth_seq_id_2', 'plane_1_auth_comp_id_2', 'plane_1_auth_atom_id_2',
                                                          'plane_1_auth_asym_id_3', 'plane_1_auth_seq_id_3', 'plane_1_auth_comp_id_3', 'plane_1_auth_atom_id_3',
                                                          'plane_1_auth_asym_id_4', 'plane_1_auth_seq_id_4', 'plane_1_auth_comp_id_4', 'plane_1_auth_atom_id_4'
                                                          'plane_2_auth_asym_id_5', 'plane_2_auth_seq_id_5', 'plane_2_auth_comp_id_5', 'plane_2_auth_atom_id_5',
                                                          'plane_2_auth_asym_id_6', 'plane_2_auth_seq_id_6', 'plane_2_auth_comp_id_6', 'plane_2_auth_atom_id_6'
                                                          'plane_2_auth_asym_id_7', 'plane_2_auth_seq_id_7', 'plane_2_auth_comp_id_7', 'plane_2_auth_atom_id_7',
                                                          'plane_2_auth_asym_id_8', 'plane_2_auth_seq_id_8', 'plane_2_auth_comp_id_8', 'plane_2_auth_atom_id_8'
                                                          'target_value', 'target_value_uncertainty',
                                                          'lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit',
                                                          'list_id', 'entry_id']

                            for atom1, atom2, atom3, atom4, atom5, atom6, atom7, atom8 in itertools.product(self.atomSelectionSet[0],
                                                                                                            self.atomSelectionSet[1],
                                                                                                            self.atomSelectionSet[2],
                                                                                                            self.atomSelectionSet[3],
                                                                                                            self.atomSelectionSet[4],
                                                                                                            self.atomSelectionSet[5],
                                                                                                            self.atomSelectionSet[6],
                                                                                                            self.atomSelectionSet[7]):
                                if self.__debug:
                                    print(f"subtype={self.__cur_subtype} id={self.planeRestraints} "
                                          f"plane1: |atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4}| "
                                          f"plane2: |atom1={atom5} atom2={atom6} atom3={atom7} atom4={atom8}| "
                                          f"{dstFunc}")
                                if self.__createSfDict and sf is not None:
                                    sf['index_id'] += 1
                                    sf['loop']['data'].append([sf['index_id'], sf['id'],
                                                               atom1['chain_id'], atom1['seq_id'], atom1['comp_id'], atom1['atom_id'],
                                                               atom2['chain_id'], atom2['seq_id'], atom2['comp_id'], atom2['atom_id'],
                                                               atom3['chain_id'], atom3['seq_id'], atom3['comp_id'], atom3['atom_id'],
                                                               atom4['chain_id'], atom4['seq_id'], atom4['comp_id'], atom4['atom_id'],
                                                               atom5['chain_id'], atom5['seq_id'], atom5['comp_id'], atom5['atom_id'],
                                                               atom6['chain_id'], atom6['seq_id'], atom6['comp_id'], atom6['atom_id'],
                                                               atom7['chain_id'], atom7['seq_id'], atom7['comp_id'], atom7['atom_id'],
                                                               atom8['chain_id'], atom8['seq_id'], atom8['comp_id'], atom8['atom_id'],
                                                               dstFunc.get('target_value'), None,
                                                               dstFunc.get('lower_linear_limit'),
                                                               dstFunc.get('lower_limit'),
                                                               dstFunc.get('upper_limit'),
                                                               dstFunc.get('upper_linear_limit'),
                                                               sf['list_id'], self.__entryId])

                # try to update AMBER atom number dictionary based on Sander comments
                elif self.__hasPolySeq:

                    if self.__cur_subtype == 'dist' and not self.inGenDist:
                        subtype_name = 'distance restraint'

                        g = None\
                            if self.lastComment is None or not self.dist_sander_pat.match(self.lastComment)\
                            else self.dist_sander_pat.search(self.lastComment).groups()

                        for col, funcExpr in enumerate(self.funcExprs):
                            offset = col * 3

                            if isinstance(funcExpr, dict):
                                if 'iat' in funcExpr:
                                    iat = funcExpr['iat']
                                    if iat in self.__sanderAtomNumberDict:
                                        pass
                                    else:
                                        if g is None:
                                            self.reportSanderCommentIssue(subtype_name)
                                            return
                                        factor = {'auth_seq_id': int(g[offset + 0]),
                                                  'auth_comp_id': g[offset + 1],
                                                  'auth_atom_id': g[offset + 2],
                                                  'iat': iat
                                                  }
                                        if not self.updateSanderAtomNumberDict(factor):
                                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                            f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                            f"based on Sander comment {' '.join(g[offset:offset+3])!r}.")

                            else:  # list
                                igr = [_funcExpr['igr'] for _funcExpr in funcExpr if 'igr' in _funcExpr]
                                mask = [_funcExpr['atom_id'] for _funcExpr in funcExpr if 'atom_id' in _funcExpr]
                                if len(igr) > 0 and len(mask) == 0:  # support igr solely
                                    if igr[0] not in self.__sanderAtomNumberDict:
                                        if g is None:
                                            self.reportSanderCommentIssue(subtype_name)
                                            return
                                        factor = {'auth_seq_id': int(g[offset + 0]),
                                                  'auth_comp_id': g[offset + 1],
                                                  'auth_atom_id': g[offset + 2],
                                                  'igr': igr
                                                  }
                                        if not self.updateSanderAtomNumberDict(factor):
                                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                            f"Couldn't specify 'igr({col+1})={igr}' in the coordinates "
                                                            f"based on Sander comment {' '.join(g[offset:offset+3])!r}.")

                    elif self.__cur_subtype == 'ang':
                        subtype_name = 'angle restraint'

                        g = None\
                            if self.lastComment is None or not self.ang_sander_pat.match(self.lastComment)\
                            else self.ang_sander_pat.search(self.lastComment).groups()

                        gn = None\
                            if self.lastComment is None or not self.ang_nang_sander_pat.match(self.lastComment)\
                            else self.ang_nang_sander_pat.search(self.lastComment).groups()

                        _gn = None\
                            if self.lastComment is not None or gn is not None or self.prevComment is None\
                            or not self.ang_nang_sander_pat.match(self.prevComment)\
                            else self.ang_nang_sander_pat.search(self.prevComment).groups()

                        if _gn is not None:
                            for col, funcExpr in enumerate(self.funcExprs):

                                if isinstance(funcExpr, dict):
                                    if 'iat' in funcExpr:
                                        iat = funcExpr['iat']
                                        if iat in self.__sanderAtomNumberDict:
                                            pass
                                        else:
                                            seqId = int(_gn[0])
                                            atomId = self.ang_nang_atoms[1][col]
                                            _factor = self.getAtomNumberDictFromAmbmaskInfo(seqId, atomId)
                                            if _factor is None:
                                                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                                f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                                f"based on Sander comment {self.prevComment!r}.")
                                                continue
                                            factor = {'auth_seq_id': seqId,
                                                      'auth_comp_id': _factor['comp_id'],  # pylint: disable=unsubscriptable-object
                                                      'auth_atom_id': atomId,
                                                      'iat': iat
                                                      }
                                            if not self.updateSanderAtomNumberDict(factor):
                                                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                                f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                                f"based on Sander comment {self.prevComment!r}.")

                            self.prevComment = None

                        elif gn is not None:
                            for col, funcExpr in enumerate(self.funcExprs):

                                if isinstance(funcExpr, dict):
                                    if 'iat' in funcExpr:
                                        iat = funcExpr['iat']
                                        if iat in self.__sanderAtomNumberDict:
                                            pass
                                        else:
                                            seqId = int(_gn[0])
                                            atomId = self.ang_nang_atoms[0][col]
                                            _factor = self.getAtomNumberDictFromAmbmaskInfo(seqId, atomId)
                                            if _factor is None:
                                                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                                f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                                f"based on Sander comment {self.lastComment!r}.")
                                                continue
                                            factor = {'auth_seq_id': seqId,
                                                      'auth_comp_id': _factor['comp_id'],  # pylint: disable=unsubscriptable-object
                                                      'auth_atom_id': atomId,
                                                      'iat': iat
                                                      }
                                            if not self.updateSanderAtomNumberDict(factor):
                                                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                                f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                                f"based on Sander comment {self.lastComment!r}.")

                        else:
                            for col, funcExpr in enumerate(self.funcExprs):
                                offset = col * 3 + 3

                                if isinstance(funcExpr, dict):
                                    if 'iat' in funcExpr:
                                        iat = funcExpr['iat']
                                        if iat in self.__sanderAtomNumberDict:
                                            pass
                                        else:
                                            if g is None:
                                                self.reportSanderCommentIssue(subtype_name)
                                                return
                                            factor = {'auth_seq_id': int(g[offset + 0]),
                                                      'auth_comp_id': g[offset + 1],
                                                      'auth_atom_id': g[offset + 2],
                                                      'iat': iat
                                                      }
                                            if not self.updateSanderAtomNumberDict(factor):
                                                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                                f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                                f"based on Sander comment {' '.join(g[offset:offset+3])!r}.")

                    elif self.__cur_subtype == 'dihed':
                        subtype_name = 'torsional angle restraint'

                        g = None\
                            if self.lastComment is None or not self.dihed_sander_pat.match(self.lastComment)\
                            else self.dihed_sander_pat.search(self.lastComment).groups()

                        g2 = None\
                            if self.lastComment is None or not self.dihed_sander_pat2.match(self.lastComment)\
                            else self.dihed_sander_pat2.search(self.lastComment).groups()

                        gc = None\
                            if self.lastComment is None or not self.dihed_chiral_sander_pat.match(self.lastComment)\
                            else self.dihed_chiral_sander_pat.search(self.lastComment).groups()

                        go = None\
                            if self.lastComment is None or not self.dihed_omega_sander_pat.match(self.lastComment)\
                            else self.dihed_omega_sander_pat.search(self.lastComment).groups()

                        if go is not None:
                            for col, funcExpr in enumerate(self.funcExprs):

                                if isinstance(funcExpr, dict):
                                    if 'iat' in funcExpr:
                                        iat = funcExpr['iat']
                                        if iat in self.__sanderAtomNumberDict:
                                            pass
                                        else:
                                            seqId = int(go[0])
                                            if col >= 2:
                                                seqId -= 1
                                            atomId = self.dihed_omega_atoms[col]
                                            _factor = self.getAtomNumberDictFromAmbmaskInfo(seqId, atomId)
                                            if _factor is None:
                                                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                                f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                                f"based on Sander comment {self.lastComment!r}.")
                                                continue
                                            factor = {'auth_seq_id': seqId,
                                                      'auth_comp_id': _factor['comp_id'],  # pylint: disable=unsubscriptable-object
                                                      'auth_atom_id': atomId,
                                                      'iat': iat
                                                      }
                                            if not self.updateSanderAtomNumberDict(factor):
                                                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                                f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                                f"based on Sander comment {self.lastComment!r}.")

                        elif gc is not None:
                            for col, funcExpr in enumerate(self.funcExprs):

                                if isinstance(funcExpr, dict):
                                    if 'iat' in funcExpr:
                                        iat = funcExpr['iat']
                                        if iat in self.__sanderAtomNumberDict:
                                            pass
                                        else:
                                            seqId = int(gc[0])
                                            atomId = gc[col + 1]
                                            _factor = self.getAtomNumberDictFromAmbmaskInfo(seqId, atomId)
                                            if _factor is None:
                                                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                                f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                                f"based on Sander comment {self.lastComment!r}.")
                                                continue
                                            factor = {'auth_seq_id': seqId,
                                                      'auth_comp_id': _factor['comp_id'],  # pylint: disable=unsubscriptable-object
                                                      'auth_atom_id': atomId,
                                                      'iat': iat
                                                      }
                                            if not self.updateSanderAtomNumberDict(factor):
                                                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                                f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                                f"based on Sander comment {self.lastComment!r}.")

                        else:
                            for col, funcExpr in enumerate(self.funcExprs):
                                offset = col * 3 + 3
                                offset2 = col * 3

                                if isinstance(funcExpr, dict):
                                    if 'iat' in funcExpr:
                                        iat = funcExpr['iat']
                                        if iat in self.__sanderAtomNumberDict:
                                            pass
                                        else:
                                            if g is None and g2 is not None:
                                                self.reportSanderCommentIssue(subtype_name)
                                                return
                                            if g is not None:
                                                factor = {'auth_seq_id': int(g[offset + 0]),
                                                          'auth_comp_id': g[offset + 1],
                                                          'auth_atom_id': g[offset + 2],
                                                          'iat': iat
                                                          }
                                                if not self.updateSanderAtomNumberDict(factor):
                                                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                                    f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                                    f"based on Sander comment {' '.join(g[offset:offset+3])!r}.")
                                            else:
                                                factor = {'auth_seq_id': int(g2[offset2 + 0]),
                                                          'auth_comp_id': g2[offset2 + 1],
                                                          'auth_atom_id': g2[offset2 + 2],
                                                          'iat': iat
                                                          }
                                                if not self.updateSanderAtomNumberDict(factor):
                                                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                                    f"Couldn't specify 'iat({col+1})={iat}' in the coordinates "
                                                                    f"based on Sander comment {' '.join(g2[offset2:offset2+3])!r}.")

        finally:

            if self.lastComment is not None:
                self.prevComment = self.lastComment

            self.lastComment = None

    def validateDistanceRange(self, wt):
        """ Validate distance value range.
        """

        validRange = True
        dstFunc = {'weight': wt}

        if self.lowerLimit is not None:
            if DIST_ERROR_MIN <= self.lowerLimit < DIST_ERROR_MAX:
                dstFunc['lower_limit'] = f"{self.lowerLimit}"
            else:
                if self.lowerLimit <= DIST_ERROR_MIN and self.__omitDistLimitOutlier:
                    self.__f.append(f"[Range value warning] {self.__getCurrentRestraint()}"
                                    f"The lower limit value 'r2={self.lowerLimit}' is omitted because it is not within range {DIST_RESTRAINT_ERROR}.")
                    self.lowerLimit = None
                else:
                    validRange = False
                    self.__f.append(f"[Range value error] {self.__getCurrentRestraint()}"
                                    f"The lower limit value 'r2={self.lowerLimit}' must be within range {DIST_RESTRAINT_ERROR}.")

        if self.upperLimit is not None:
            if DIST_ERROR_MIN < self.upperLimit <= DIST_ERROR_MAX:
                dstFunc['upper_limit'] = f"{self.upperLimit}"
            else:
                if (self.upperLimit <= DIST_ERROR_MIN or self.upperLimit > DIST_ERROR_MAX) and self.__omitDistLimitOutlier:
                    self.__f.append(f"[Range value warning] {self.__getCurrentRestraint()}"
                                    f"The upper limit value 'r3={self.upperLimit}' is omitted because it is not within range {DIST_RESTRAINT_ERROR}.")
                    self.upperLimit = None
                else:
                    validRange = False
                    self.__f.append(f"[Range value error] {self.__getCurrentRestraint()}"
                                    f"The upper limit value 'r3={self.upperLimit}' must be within range {DIST_RESTRAINT_ERROR}.")

        if self.lowerLinearLimit is not None:
            if DIST_ERROR_MIN <= self.lowerLinearLimit < DIST_ERROR_MAX:
                dstFunc['lower_linear_limit'] = f"{self.lowerLinearLimit}"
            else:
                if self.lowerLinearLimit <= DIST_ERROR_MIN and self.__omitDistLimitOutlier:
                    self.__f.append(f"[Range value warning] {self.__getCurrentRestraint()}"
                                    f"The lower linear limit value 'r1={self.lowerLinearLimit}' is omitted because it is not within range {DIST_RESTRAINT_ERROR}.")
                    self.lowerLinearLimit = None
                else:
                    validRange = False
                    self.__f.append(f"[Range value error] {self.__getCurrentRestraint()}"
                                    f"The lower linear limit value 'r1={self.lowerLinearLimit}' must be within range {DIST_RESTRAINT_ERROR}.")

        if self.upperLinearLimit is not None:
            if DIST_ERROR_MIN < self.upperLinearLimit <= DIST_ERROR_MAX:
                dstFunc['upper_linear_limit'] = f"{self.upperLinearLimit}"
            else:
                if (self.upperLinearLimit <= DIST_ERROR_MIN or self.upperLinearLimit > DIST_ERROR_MAX) and self.__omitDistLimitOutlier:
                    self.__f.append(f"[Range value warning] {self.__getCurrentRestraint()}"
                                    f"The upper linear limit value 'r4={self.upperLinearLimit}' is omitted because it is not  within range {DIST_RESTRAINT_ERROR}.")
                    self.upperLinearLimit = None
                else:
                    validRange = False
                    self.__f.append(f"[Range value error] {self.__getCurrentRestraint()}"
                                    f"The upper linear limit value 'r4={self.upperLinearLimit}' must be within range {DIST_RESTRAINT_ERROR}.")

        if self.lowerLimit is not None and self.upperLimit is not None:
            if self.lowerLimit > self.upperLimit:
                validRange = False
                self.__f.append(f"[Range value error] {self.__getCurrentRestraint()}"
                                f"The lower limit value 'r2={self.lowerLimit}' must be less than the upper limit value 'r3={self.upperLimit}'.")

        if self.lowerLinearLimit is not None and self.upperLimit is not None:
            if self.lowerLinearLimit > self.upperLimit:
                validRange = False
                self.__f.append(f"[Range value error] {self.__getCurrentRestraint()}"
                                f"The lower linear limit value 'r1={self.lowerLinearLimit}' must be less than the upper limit value 'r3={self.upperLimit}'.")

        if self.lowerLimit is not None and self.upperLinearLimit is not None:
            if self.lowerLimit > self.upperLinearLimit:
                validRange = False
                self.__f.append(f"[Range value error] {self.__getCurrentRestraint()}"
                                f"The lower limit value 'r2={self.lowerLimit}' must be less than the upper limit value 'r4={self.upperLinearLimit}'.")

        if self.lowerLinearLimit is not None and self.upperLinearLimit is not None:
            if self.lowerLinearLimit > self.upperLinearLimit:
                validRange = False
                self.__f.append(f"[Range value error] {self.__getCurrentRestraint()}"
                                f"The lower linear limit value 'r1={self.lowerLinearLimit}' must be less than the upper limit value 'r4={self.upperLinearLimit}'.")

        if self.lowerLimit is not None and self.lowerLinearLimit is not None:
            if self.lowerLinearLimit > self.lowerLimit:
                validRange = False
                self.__f.append(f"[Range value error] {self.__getCurrentRestraint()}"
                                f"The lower linear limit value 'r1={self.lowerLinearLimit}' must be less than the lower limit value 'r2={self.lowerLimit}'.")

        if self.upperLimit is not None and self.upperLinearLimit is not None:
            if self.upperLimit > self.upperLinearLimit:
                validRange = False
                self.__f.append(f"[Range value error] {self.__getCurrentRestraint()}"
                                f"The upper limit value 'r3={self.upperLimit}' must be less than the upper linear limit value 'r4={self.upperLinearLimit}'.")

        if not validRange:
            self.lastComment = None
            return None

        if self.lowerLimit is not None:
            if DIST_RANGE_MIN <= self.lowerLimit <= DIST_RANGE_MAX:
                pass
            else:
                self.__f.append(f"[Range value warning] {self.__getCurrentRestraint()}"
                                f"The lower limit value 'r2={self.lowerLimit}' should be within range {DIST_RESTRAINT_RANGE}.")

        if self.upperLimit is not None:
            if DIST_RANGE_MIN <= self.upperLimit <= DIST_RANGE_MAX:
                pass
            else:
                self.__f.append(f"[Range value warning] {self.__getCurrentRestraint()}"
                                f"The upper limit value 'r3={self.upperLimit}' should be within range {DIST_RESTRAINT_RANGE}.")

        if self.lowerLinearLimit is not None:
            if DIST_RANGE_MIN <= self.lowerLinearLimit <= DIST_RANGE_MAX:
                pass
            else:
                self.__f.append(f"[Range value warning] {self.__getCurrentRestraint()}"
                                f"The lower linear limit value 'r1={self.lowerLinearLimit}' should be within range {DIST_RESTRAINT_RANGE}.")

        if self.upperLinearLimit is not None:
            if DIST_RANGE_MIN <= self.upperLinearLimit <= DIST_RANGE_MAX:
                pass
            else:
                self.__f.append(f"[Range value warning] {self.__getCurrentRestraint()}"
                                f"The upper linear limit value 'r4={self.upperLinearLimit}' should be within range {DIST_RESTRAINT_RANGE}.")

        return dstFunc

    def validateAngleRange(self, wt):
        """ Validate angle value range.
        """

        validRange = True
        dstFunc = {'weight': wt}

        if self.__correctCircularShift:
            _array = numpy.array([self.lowerLimit, self.upperLimit, self.lowerLinearLimit, self.upperLinearLimit],
                                 dtype=float)

            shift = None
            if numpy.nanmin(_array) >= THRESHHOLD_FOR_CIRCULAR_SHIFT:
                shift = -(numpy.nanmax(_array) // 360) * 360
            elif numpy.nanmax(_array) <= -THRESHHOLD_FOR_CIRCULAR_SHIFT:
                shift = -(numpy.nanmin(_array) // 360) * 360
            if shift is not None:
                self.__f.append(f"[Range value warning] {self.__getCurrentRestraint()}"
                                "The limit values for an angle restraint have been circularly shifted "
                                f"to fit within range {ANGLE_RESTRAINT_ERROR}.")
                if self.lowerLimit is not None:
                    self.lowerLimit += shift
                if self.upperLimit is not None:
                    self.upperLimit += shift
                if self.lowerLinearLimit is not None:
                    self.lowerLinearLimit += shift
                if self.upperLinearLimit is not None:
                    self.upperLinearLimit += shift

        if self.lowerLimit is not None:
            if ANGLE_ERROR_MIN <= self.lowerLimit < ANGLE_ERROR_MAX:
                dstFunc['lower_limit'] = f"{self.lowerLimit}"
            else:
                validRange = False
                self.__f.append(f"[Range value error] {self.__getCurrentRestraint()}"
                                f"The lower limit value 'r2={self.lowerLimit}' must be within range {ANGLE_RESTRAINT_ERROR}.")

        if self.upperLimit is not None:
            if ANGLE_ERROR_MIN < self.upperLimit <= ANGLE_ERROR_MAX:
                dstFunc['upper_limit'] = f"{self.upperLimit}"
            else:
                validRange = False
                self.__f.append(f"[Range value error] {self.__getCurrentRestraint()}"
                                f"The upper limit value 'r3={self.upperLimit}' must be within range {ANGLE_RESTRAINT_ERROR}.")

        if self.lowerLinearLimit is not None:
            if ANGLE_ERROR_MIN <= self.lowerLinearLimit < ANGLE_ERROR_MAX:
                dstFunc['lower_linear_limit'] = f"{self.lowerLinearLimit}"
            else:
                validRange = False
                self.__f.append(f"[Range value error] {self.__getCurrentRestraint()}"
                                f"The lower linear limit value 'r1={self.lowerLinearLimit}' must be within range {ANGLE_RESTRAINT_ERROR}.")

        if self.upperLinearLimit is not None:
            if ANGLE_ERROR_MIN < self.upperLinearLimit <= ANGLE_ERROR_MAX:
                dstFunc['upper_linear_limit'] = f"{self.upperLinearLimit}"
            else:
                validRange = False
                self.__f.append(f"[Range value error] {self.__getCurrentRestraint()}"
                                f"The upper linear limit value 'r4={self.upperLinearLimit}' must be within range {ANGLE_RESTRAINT_ERROR}.")

        if self.lowerLimit is not None and self.lowerLinearLimit is not None:
            if self.lowerLinearLimit > self.lowerLimit:
                validRange = False
                self.__f.append(f"[Range value error] {self.__getCurrentRestraint()}"
                                f"The lower linear limit value 'r1={self.lowerLinearLimit}' must be less than the lower limit value 'r2={self.lowerLimit}'.")

        if self.upperLimit is not None and self.upperLinearLimit is not None:
            if self.upperLimit > self.upperLinearLimit:
                validRange = False
                self.__f.append(f"[Range value error] {self.__getCurrentRestraint()}"
                                f"The upper limit value 'r3={self.upperLimit}' must be less than the upper linear limit value 'r4={self.upperLinearLimit}'.")

        if not validRange:
            self.lastComment = None
            return None

        if self.lowerLimit is not None:
            if ANGLE_RANGE_MIN <= self.lowerLimit <= ANGLE_RANGE_MAX:
                pass
            else:
                self.__f.append(f"[Range value warning] {self.__getCurrentRestraint()}"
                                f"The lower limit value 'r2={self.lowerLimit}' should be within range {ANGLE_RESTRAINT_RANGE}.")

        if self.upperLimit is not None:
            if ANGLE_RANGE_MIN <= self.upperLimit <= ANGLE_RANGE_MAX:
                pass
            else:
                self.__f.append(f"[Range value warning] {self.__getCurrentRestraint()}"
                                f"The upper limit value 'r3={self.upperLimit}' should be within range {ANGLE_RESTRAINT_RANGE}.")

        if self.lowerLinearLimit is not None:
            if ANGLE_RANGE_MIN <= self.lowerLinearLimit <= ANGLE_RANGE_MAX:
                pass
            else:
                self.__f.append(f"[Range value warning] {self.__getCurrentRestraint()}"
                                f"The lower linear limit value 'r1={self.lowerLinearLimit}' should be within range {ANGLE_RESTRAINT_RANGE}.")

        if self.upperLinearLimit is not None:
            if ANGLE_RANGE_MIN <= self.upperLinearLimit <= ANGLE_RANGE_MAX:
                pass
            else:
                self.__f.append(f"[Range value warning] {self.__getCurrentRestraint()}"
                                f"The upper linear limit value 'r4={self.upperLinearLimit}' should be within range {ANGLE_RESTRAINT_RANGE}.")

        return dstFunc

    def validatePcsRange(self, n, wt, tolpro, mltpro):
        """ Validate PCS value range.
        """

        obs = self.obs[n]

        validRange = True
        dstFunc = {'weight': wt, 'tolerance': tolpro, 'multiplicity': mltpro}

        if obs is not None:
            if PCS_ERROR_MIN < obs < PCS_ERROR_MAX:
                dstFunc['target_value'] = f"{obs}"
            else:
                validRange = False
                self.__f.append(f"[Range value error] {self.__getCurrentRestraint(self.nmpmc,n)}"
                                f"The target value 'obs({n})={obs}' must be within range {PCS_RESTRAINT_ERROR}.")

        if not validRange:
            self.lastComment = None
            return None

        if obs is not None:
            if PCS_RANGE_MIN <= obs <= PCS_RANGE_MAX:
                pass
            else:
                self.__f.append(f"[Range value warning] {self.__getCurrentRestraint(self.nmpmc,n)}"
                                f"The target value 'obs({n})={obs}' should be within range {PCS_RESTRAINT_RANGE}.")

        return dstFunc

    def validateRdcRange(self, n, wt):
        """ Validate RDC value range.
        """

        dobsl = self.dobsl[n]
        dobsu = self.dobsu[n]

        if dobsl is not None and dobsu is not None and dobsl > dobsu:
            dobsl, dobsu = dobsu, dobsl

        validRange = True
        dstFunc = {'weight': wt}

        if dobsl is not None:
            if RDC_ERROR_MIN < dobsl < RDC_ERROR_MAX:
                dstFunc['lower_limit'] = f"{dobsl}"
            else:
                validRange = False
                self.__f.append(f"[Range value error] {self.__getCurrentRestraint(self.dataset,n)}"
                                f"The lower limit value 'dobsl({n})={dobsl}' must be within range {RDC_RESTRAINT_ERROR}.")

        if dobsu is not None:
            if RDC_ERROR_MIN < dobsu < RDC_ERROR_MAX:
                dstFunc['upper_limit'] = f"{dobsu}"
            else:
                validRange = False
                self.__f.append(f"[Range value error] {self.__getCurrentRestraint(self.dataset,n)}"
                                f"The upper limit value 'dobsu({n})={dobsu}' must be within range {RDC_RESTRAINT_ERROR}.")

        if not validRange:
            self.lastComment = None
            return None

        if dobsl is not None:
            if RDC_RANGE_MIN <= dobsl <= RDC_RANGE_MAX:
                pass
            else:
                self.__f.append(f"[Range value warning] {self.__getCurrentRestraint(self.dataset,n)}"
                                f"The lower limit value 'dobsl({n})={dobsl}' should be within range {RDC_RESTRAINT_RANGE}.")

        if dobsu is not None:
            if RDC_RANGE_MIN <= dobsu <= RDC_RANGE_MAX:
                pass
            else:
                self.__f.append(f"[Range value warning] {self.__getCurrentRestraint(self.dataset,n)}"
                                f"The upper limit value 'dobsu({n})={dobsu}' should be within range {RDC_RESTRAINT_RANGE}.")

        return dstFunc

    def validateCsaRange(self, n, wt):
        """ Validate CSA value range.
        """

        cobsl = self.cobsl[n]
        cobsu = self.cobsu[n]

        if cobsl is not None and cobsu is not None and cobsl > cobsu:
            cobsl, cobsu = cobsu, cobsl

        validRange = True
        dstFunc = {'weight': wt}

        if cobsl is not None:
            if CSA_ERROR_MIN < cobsl < CSA_ERROR_MAX:
                dstFunc['lower_limit'] = f"{cobsl}"
            else:
                validRange = False
                self.__f.append(f"[Range value error] {self.__getCurrentRestraint(self.datasetc,n)}"
                                f"The lower limit value 'cobsl({n})={cobsl}' must be within range {CSA_RESTRAINT_ERROR}.")

        if cobsu is not None:
            if CSA_ERROR_MIN < cobsu < CSA_ERROR_MAX:
                dstFunc['upper_limit'] = f"{cobsu}"
            else:
                validRange = False
                self.__f.append(f"[Range value error] {self.__getCurrentRestraint(self.datasetc,n)}"
                                f"The upper limit value 'cobsu({n})={cobsu}' must be within range {CSA_RESTRAINT_ERROR}.")

        if not validRange:
            self.lastComment = None
            return None

        if cobsl is not None:
            if CSA_RANGE_MIN <= cobsl <= CSA_RANGE_MAX:
                pass
            else:
                self.__f.append(f"[Range value warning] {self.__getCurrentRestraint(self.datasetc,n)}"
                                f"The lower limit value 'cobsl({n})={cobsl}' should be within range {CSA_RESTRAINT_RANGE}.")

        if cobsu is not None:
            if CSA_RANGE_MIN <= cobsu <= CSA_RANGE_MAX:
                pass
            else:
                self.__f.append(f"[Range value warning] {self.__getCurrentRestraint(self.datasetc,n)}"
                                f"The upper limit value 'cobsu({n})={cobsu}' should be within range {CSA_RESTRAINT_RANGE}.")

        return dstFunc

    def getAtomNumberDictFromAmbmaskInfo(self, seqId, atomId, order=0, useDefault=True):
        """ Return atom number dictionary like component from Amber 10 ambmask information.
        """
        if not self.__hasPolySeq:
            return None

        if self.__concatHetero:
            useDefault = False

        cifCheck = self.__hasCoord

        authAtomId = atomId

        factor = {}

        found = False

        enforceAuthSeq = self.__reasons is not None and 'auth_seq_scheme' in self.__reasons

        for ps in (self.__polySeq if useDefault else self.__altPolySeq):
            chainId = ps['auth_chain_id']

            if not useDefault and seqId not in ps['auth_seq_id'] and 'gap_in_auth_seq' in ps:
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
                        idx = ps['auth_seq_id'].index(_seqId_) - (_seqId_ - seqId)
                        try:
                            seqId = ps['auth_seq_id'][idx]
                        except IndexError:
                            pass

            if seqId in (ps['seq_id'] if useDefault and not enforceAuthSeq else ps['auth_seq_id']):
                idx = ps['seq_id'].index(seqId) if useDefault and not enforceAuthSeq else ps['auth_seq_id'].index(seqId)
                compId = ps['comp_id'][idx]
                cifSeqId = None if useDefault and not enforceAuthSeq else ps['seq_id'][ps['auth_seq_id'].index(seqId)]

                seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId if cifSeqId is None else cifSeqId, cifCheck)

                if compId not in monDict3 and self.__mrAtomNameMapping is not None:
                    origCompId = ps['auth_comp_id'][idx]
                    _, _, atomId = retrieveAtomIdentFromMRMap(self.__mrAtomNameMapping, seqId, origCompId, atomId, coordAtomSite)

                if compId in monDict3 or coordAtomSite is None:
                    atomId = translateToStdAtomName(atomId, compId, ccU=self.__ccU)
                else:
                    atomId = translateToStdAtomName(atomId, compId, coordAtomSite['atom_id'], ccU=self.__ccU)

                atomIds = self.__nefT.get_valid_star_atom_in_xplor(compId, atomId)[0]

                if coordAtomSite is not None\
                   and not any(_atomId for _atomId in atomIds if _atomId in coordAtomSite['atom_id'])\
                   and atomId in coordAtomSite['atom_id']:
                    atomIds = [atomId]

                for idx, _atomId in enumerate(atomIds):

                    if idx != order:
                        continue

                    ccdCheck = not cifCheck

                    if cifCheck:
                        if coordAtomSite is not None:
                            if _atomId in coordAtomSite['atom_id']:
                                found = True
                            elif 'alt_atom_id' in coordAtomSite and _atomId in coordAtomSite['alt_atom_id']:
                                found = True
                                self.__authAtomId = 'auth_atom_id'
                            elif self.__preferAuthSeq:
                                _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId if cifSeqId is None else cifSeqId, cifCheck, asis=False)
                                if _coordAtomSite is not None:
                                    if _atomId in _coordAtomSite['atom_id']:
                                        found = True
                                        self.__preferAuthSeq = False
                                        self.__authSeqId = 'label_seq_id'
                                        seqKey = _seqKey
                                    elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                        found = True
                                        self.__preferAuthSeq = False
                                        self.__authSeqId = 'label_seq_id'
                                        self.__authAtomId = 'auth_atom_id'
                                        seqKey = _seqKey

                        elif self.__preferAuthSeq:
                            _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId if cifSeqId is None else cifSeqId, cifCheck, asis=False)
                            if _coordAtomSite is not None:
                                if _atomId in _coordAtomSite['atom_id']:
                                    found = True
                                    self.__preferAuthSeq = False
                                    self.__authSeqId = 'label_seq_id'
                                    seqKey = _seqKey
                                elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                    found = True
                                    self.__preferAuthSeq = False
                                    self.__authSeqId = 'label_seq_id'
                                    self.__authAtomId = 'auth_atom_id'
                                    seqKey = _seqKey

                        if found:
                            factor['chain_id'] = chainId
                            factor['seq_id'] = seqId if cifSeqId is None else cifSeqId
                            factor['comp_id'] = compId
                            factor['atom_id'] = _atomId
                            factor['auth_seq_id'] = seqId
                            factor['auth_atom_id'] = authAtomId
                            return factor

                        ccdCheck = True

                    if ccdCheck:
                        if self.__ccU.updateChemCompDict(compId):
                            cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId), None)
                            if cca is not None:
                                factor['chain_id'] = chainId
                                factor['seq_id'] = seqId if cifSeqId is None else cifSeqId
                                factor['comp_id'] = compId
                                factor['atom_id'] = _atomId
                                factor['auth_seq_id'] = seqId
                                factor['auth_atom_id'] = authAtomId
                                if cifCheck and seqKey not in self.__coordUnobsRes and self.__ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] == 'REL':
                                    checked = False
                                    _seqId = factor['seq_id']
                                    if _seqId == 1 or (chainId, _seqId - 1) in self.__coordUnobsRes or _seqId == ps['auth_seq_id'][0]:
                                        if coordAtomSite is not None and ((_atomId in aminoProtonCode and 'H1' in coordAtomSite['atom_id']) or _atomId == 'P'):
                                            checked = True
                                    if _atomId[0] in protonBeginCode:
                                        bondedTo = self.__ccU.getBondedAtoms(compId, _atomId)
                                        if len(bondedTo) > 0:
                                            if coordAtomSite is not None and bondedTo[0] in coordAtomSite['atom_id'] and cca[self.__ccU.ccaLeavingAtomFlag] != 'Y':
                                                checked = True
                                                self.__f.append(f"[Hydrogen not instantiated] {self.__getCurrentRestraint()}"
                                                                f"{chainId}:{seqId}:{compId}:{authAtomId} is not properly instantiated in the coordinates. "
                                                                "Please re-upload the model file.")
                                    if not checked:
                                        if chainId in LARGE_ASYM_ID:
                                            self.__f.append(f"[Atom not found] {self.__getCurrentRestraint()}"
                                                            f"{chainId}:{seqId}:{compId}:{authAtomId} is not present in the coordinates.")
                                            if 'auth_seq_scheme' not in self.reasonsForReParsing:
                                                self.reasonsForReParsing['auth_seq_scheme'] = True
                                return factor
                            if chainId in LARGE_ASYM_ID:
                                self.__f.append(f"[Atom not found] {self.__getCurrentRestraint()}"
                                                f"{chainId}:{seqId}:{compId}:{authAtomId} is not present in the coordinates.")
                                if 'auth_seq_scheme' not in self.reasonsForReParsing:
                                    self.reasonsForReParsing['auth_seq_scheme'] = True
                            return None

        if not useDefault:
            for ps in self.__polySeq:
                chainId = ps['auth_chain_id']

                seqKey = (chainId, seqId)
                if seqKey not in self.__authToLabelSeq and 'gap_in_auth_seq' in ps:
                    min_auth_seq_id = ps['auth_seq_id'][0]
                    max_auth_seq_id = ps['auth_seq_id'][-1]
                    if min_auth_seq_id <= seqId <= max_auth_seq_id:
                        offset = 1
                        while seqId + offset <= max_auth_seq_id:
                            if seqId + offset in ps['auth_seq_id']:
                                break
                            offset += 1
                        if seqId + offset not in ps['auth_seq_id']:
                            offset = -1
                            while seqId + offset >= min_auth_seq_id:
                                if seqId + offset in ps['auth_seq_id']:
                                    break
                                offset -= 1
                        if seqId + offset in ps['auth_seq_id']:
                            idx = ps['auth_seq_id'].index(seqId + offset) - offset
                            try:
                                seqId_ = ps['auth_seq_id'][idx]
                                seqKey = (chainId, seqId_)
                            except IndexError:
                                pass

                if seqKey in self.__authToLabelSeq:
                    _, seqId = self.__authToLabelSeq[seqKey]
                    if seqId in ps['seq_id']:
                        idx = ps['seq_id'].index(seqId)
                        compId = ps['comp_id'][idx]

                        seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck)

                        if compId not in monDict3 and self.__mrAtomNameMapping is not None:
                            origCompId = ps['auth_comp_id'][idx]
                            _, _, atomId = retrieveAtomIdentFromMRMap(self.__mrAtomNameMapping, seqId, origCompId, atomId, coordAtomSite)

                        if compId in monDict3 or coordAtomSite is None:
                            atomId = translateToStdAtomName(atomId, compId, ccU=self.__ccU)
                        else:
                            atomId = translateToStdAtomName(atomId, compId, coordAtomSite['atom_id'], ccU=self.__ccU)

                        atomIds = self.__nefT.get_valid_star_atom_in_xplor(compId, atomId)[0]

                        if coordAtomSite is not None\
                           and not any(_atomId for _atomId in atomIds if _atomId in coordAtomSite['atom_id'])\
                           and atomId in coordAtomSite['atom_id']:
                            atomIds = [atomId]

                        for idx, _atomId in enumerate(atomIds):

                            if idx != order:
                                continue

                            ccdCheck = not cifCheck

                            if cifCheck:
                                if coordAtomSite is not None:
                                    if _atomId in coordAtomSite['atom_id']:
                                        found = True
                                    elif 'alt_atom_id' in coordAtomSite and _atomId in coordAtomSite['alt_atom_id']:
                                        found = True
                                        self.__authAtomId = 'auth_atom_id'
                                    elif self.__preferAuthSeq:
                                        _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck, asis=False)
                                        if _coordAtomSite is not None:
                                            if _atomId in _coordAtomSite['atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                self.__authSeqId = 'label_seq_id'
                                                seqKey = _seqKey
                                            elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                self.__authSeqId = 'label_seq_id'
                                                self.__authAtomId = 'auth_atom_id'
                                                seqKey = _seqKey

                                elif self.__preferAuthSeq:
                                    _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck, asis=False)
                                    if _coordAtomSite is not None:
                                        if _atomId in _coordAtomSite['atom_id']:
                                            found = True
                                            self.__preferAuthSeq = False
                                            self.__authSeqId = 'label_seq_id'
                                            seqKey = _seqKey
                                        elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                            found = True
                                            self.__preferAuthSeq = False
                                            self.__authSeqId = 'label_seq_id'
                                            self.__authAtomId = 'auth_atom_id'
                                            seqKey = _seqKey

                                if found:
                                    factor['chain_id'] = chainId
                                    factor['seq_id'] = seqId
                                    factor['comp_id'] = compId
                                    factor['atom_id'] = _atomId
                                    factor['auth_seq_id'] = seqId
                                    factor['auth_atom_id'] = authAtomId
                                    return factor

                                ccdCheck = True

                            if ccdCheck:
                                if self.__ccU.updateChemCompDict(compId):
                                    cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId), None)
                                    if cca is not None:
                                        factor['chain_id'] = chainId
                                        factor['seq_id'] = seqId
                                        factor['comp_id'] = compId
                                        factor['atom_id'] = _atomId
                                        factor['auth_seq_id'] = seqId
                                        factor['auth_atom_id'] = authAtomId
                                        if cifCheck and seqKey not in self.__coordUnobsRes and self.__ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] == 'REL':
                                            checked = False
                                            if seqId == 1 or (chainId, seqId - 1) in self.__coordUnobsRes or seqId == ps['auth_seq_id'][0]:
                                                if coordAtomSite is not None and ((_atomId in aminoProtonCode and 'H1' in coordAtomSite['atom_id']) or _atomId == 'P'):
                                                    checked = True
                                            if _atomId[0] in protonBeginCode:
                                                bondedTo = self.__ccU.getBondedAtoms(compId, _atomId)
                                                if len(bondedTo) > 0:
                                                    if coordAtomSite is not None and bondedTo[0] in coordAtomSite['atom_id'] and cca[self.__ccU.ccaLeavingAtomFlag] != 'Y':
                                                        checked = True
                                                        self.__f.append(f"[Hydrogen not instantiated] {self.__getCurrentRestraint()}"
                                                                        f"{chainId}:{seqId}:{compId}:{authAtomId} is not properly instantiated in the coordinates. "
                                                                        "Please re-upload the model file.")
                                            if not checked:
                                                if chainId in LARGE_ASYM_ID:
                                                    self.__f.append(f"[Atom not found] {self.__getCurrentRestraint()}"
                                                                    f"{chainId}:{seqId}:{compId}:{authAtomId} is not present in the coordinates.")
                                                    if 'auth_seq_scheme' not in self.reasonsForReParsing:
                                                        self.reasonsForReParsing['auth_seq_scheme'] = True
                                        return factor
                                    if chainId in LARGE_ASYM_ID:
                                        self.__f.append(f"[Atom not found] {self.__getCurrentRestraint()}"
                                                        f"{chainId}:{seqId}:{compId}:{authAtomId} is not present in the coordinates.")
                                        if 'auth_seq_scheme' not in self.reasonsForReParsing:
                                            self.reasonsForReParsing['auth_seq_scheme'] = True
                                    return None

        if not useDefault or self.__altPolySeq is None:
            return None

        return self.getAtomNumberDictFromAmbmaskInfo(seqId, atomId, order, False)

    def reportSanderCommentIssue(self, subtype_name):
        """ Report Sander comment issue.
        """
        if self.lastComment is None:
            self.__f.append(f"[Missing data] {self.__getCurrentRestraint()}"
                            "Failed to recognize AMBER atom numbers in the restraint file "
                            "because neither AMBER parameter/topology file nor Sander comment are available.")
        else:
            lastComment = str(self.lastComment)
            if 'AMB' in lastComment and (('-' in lastComment and ':' in lastComment) or '.' in lastComment):
                self.__f.append(f"[Missing data] {self.__getCurrentRestraint()}"
                                "Failed to recognize AMBER atom numbers in the restraint file "
                                f"To interpret Sander comment {lastComment!r} as a {subtype_name}, "
                                "please attach ambiguous atom name mapping information generated by 'makeDIST_RST' to the AMBER restraint file.")
            else:
                self.__f.append(f"[Missing data] {self.__getCurrentRestraint()}"
                                "Failed to recognize AMBER atom numbers in the restraint file "
                                f"because Sander comment {lastComment!r} couldn't be interpreted as a {subtype_name}.")

    def updateSanderAtomNumberDict(self, factor, cifCheck=True, useDefault=True):
        """ Try to update Sander atom number dictionary.
        """
        if not self.__hasPolySeq:
            return False

        authCompId = factor['auth_comp_id'].upper() if 'auth_comp_id' in factor else 'None'
        authAtomId = _authAtomId = factor['auth_atom_id']

        if self.__reasons is not None and 'ambig_atom_id_remap' in self.__reasons\
           and authCompId in self.__reasons['ambig_atom_id_remap'] and authAtomId in self.__reasons['ambig_atom_id_remap'][authCompId]:
            return self.updateSanderAtomNumberDictWithAmbigCode(factor, cifCheck, useDefault)

        if len(self.ambigAtomNameMapping) > 0\
           and authCompId in self.ambigAtomNameMapping and authAtomId in self.ambigAtomNameMapping[authCompId]:
            return self.updateSanderAtomNumberDictWithAmbigCode(factor, cifCheck, useDefault)

        if not self.__hasCoord:
            cifCheck = False

        found = False

        enforceAuthSeq = self.__reasons is not None and 'auth_seq_scheme' in self.__reasons

        for ps in (self.__polySeq if useDefault else self.__altPolySeq):
            chainId = ps['auth_chain_id']
            seqId = factor['auth_seq_id']

            if not useDefault and seqId not in ps['auth_seq_id'] and 'gap_in_auth_seq' in ps:
                min_auth_seq_id = ps['auth_seq_id'][0]
                max_auth_seq_id = ps['auth_seq_id'][-1]
                if min_auth_seq_id <= seqId <= max_auth_seq_id:
                    offset = 1
                    while seqId + offset <= max_auth_seq_id:
                        if seqId + offset in ps['auth_seq_id']:
                            break
                        offset += 1
                    if seqId + offset not in ps['auth_seq_id']:
                        offset = -1
                        while seqId + offset >= min_auth_seq_id:
                            if seqId + offset in ps['auth_seq_id']:
                                break
                            offset -= 1
                    if seqId + offset in ps['auth_seq_id']:
                        idx = ps['auth_seq_id'].index(seqId + offset) - offset
                        try:
                            seqId = ps['auth_seq_id'][idx]
                        except IndexError:
                            pass

            if seqId in (ps['seq_id'] if useDefault and not enforceAuthSeq else ps['auth_seq_id']):
                idx = ps['seq_id'].index(seqId) if useDefault and not enforceAuthSeq else ps['auth_seq_id'].index(seqId)
                compId = ps['comp_id'][idx]
                origCompId = ps['auth_comp_id'][idx]
                cifSeqId = None if useDefault else ps['seq_id'][idx]

                if compId not in monDict3 and self.__mrAtomNameMapping is not None:
                    _, authCompId, _authAtomId = retrieveAtomIdentFromMRMap(self.__mrAtomNameMapping, seqId, origCompId, authAtomId)

                if (((authCompId in (compId, origCompId, 'None') or compId not in monDict3) and useDefault) or not useDefault)\
                   or compId == translateToStdResName(authCompId, self.__ccU):

                    seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId if cifSeqId is None else cifSeqId, cifCheck)
                    if coordAtomSite is not None and _authAtomId in coordAtomSite['atom_id']:
                        authAtomId = _authAtomId

                    fixed = False
                    if self.__reasons is not None:
                        if 'unambig_atom_id_remap' in self.__reasons and authCompId in self.__reasons['unambig_atom_id_remap']\
                           and authAtomId in self.__reasons['unambig_atom_id_remap'][authCompId]:
                            atomIds = self.__reasons['unambig_atom_id_remap'][authCompId][authAtomId]
                            fixed = True
                    if len(self.unambigAtomNameMapping) > 0:
                        if authCompId in self.unambigAtomNameMapping\
                           and authAtomId in self.unambigAtomNameMapping[authCompId]:
                            atomIds = self.unambigAtomNameMapping[authCompId][authAtomId]
                            fixed = True

                    if not fixed:
                        authAtomId = translateToStdAtomName(authAtomId, compId, ccU=self.__ccU)

                        atomIds = self.__nefT.get_valid_star_atom_in_xplor(compId, authAtomId)[0]

                    if coordAtomSite is not None\
                       and not any(_atomId for _atomId in atomIds if _atomId in coordAtomSite['atom_id'])\
                       and authAtomId in coordAtomSite['atom_id']:
                        atomIds = [authAtomId]

                    if 'iat' in factor:
                        iat = factor['iat']
                        for _atomId in atomIds:
                            ccdCheck = not cifCheck

                            if cifCheck:
                                if coordAtomSite is not None:
                                    if _atomId in coordAtomSite['atom_id']:
                                        found = True
                                    elif 'alt_atom_id' in coordAtomSite and _atomId in coordAtomSite['alt_atom_id']:
                                        found = True
                                        self.__authAtomId = 'auth_atom_id'
                                    elif self.__preferAuthSeq:
                                        _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId if cifSeqId is None else cifSeqId, cifCheck, asis=False)
                                        if _coordAtomSite is not None:
                                            if _atomId in _coordAtomSite['atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                self.__authSeqId = 'label_seq_id'
                                                seqKey = _seqKey
                                            elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                self.__authSeqId = 'label_seq_id'
                                                self.__authAtomId = 'auth_atom_id'
                                                seqKey = _seqKey

                                elif self.__preferAuthSeq:
                                    _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId if cifSeqId is None else cifSeqId, cifCheck, asis=False)
                                    if _coordAtomSite is not None:
                                        if _atomId in _coordAtomSite['atom_id']:
                                            found = True
                                            self.__preferAuthSeq = False
                                            self.__authSeqId = 'label_seq_id'
                                            seqKey = _seqKey
                                        elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                            found = True
                                            self.__preferAuthSeq = False
                                            self.__authSeqId = 'label_seq_id'
                                            self.__authAtomId = 'auth_atom_id'
                                            seqKey = _seqKey

                                if found:
                                    factor['chain_id'] = chainId
                                    factor['seq_id'] = seqId if cifSeqId is None else cifSeqId
                                    factor['comp_id'] = compId
                                    factor['atom_id'] = _atomId
                                    del factor['iat']
                                    self.__sanderAtomNumberDict[iat] = factor
                                    return True

                                ccdCheck = True

                            if ccdCheck:
                                if self.__ccU.updateChemCompDict(compId):
                                    cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId), None)
                                    if cca is not None:
                                        factor['chain_id'] = chainId
                                        factor['seq_id'] = seqId if cifSeqId is None else cifSeqId
                                        factor['comp_id'] = compId
                                        factor['atom_id'] = _atomId
                                        del factor['iat']
                                        self.__sanderAtomNumberDict[iat] = factor
                                        if cifCheck and seqKey not in self.__coordUnobsRes and self.__ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] == 'REL':
                                            checked = False
                                            _seqId = factor['seq_id']
                                            if _seqId == 1 or (chainId, _seqId - 1) in self.__coordUnobsRes or _seqId == ps['auth_seq_id'][0]:
                                                if coordAtomSite is not None and ((_atomId in aminoProtonCode and 'H1' in coordAtomSite['atom_id']) or _atomId == 'P'):
                                                    checked = True
                                            if _atomId[0] in protonBeginCode:
                                                bondedTo = self.__ccU.getBondedAtoms(compId, _atomId)
                                                if len(bondedTo) > 0:
                                                    if coordAtomSite is not None and bondedTo[0] in coordAtomSite['atom_id'] and cca[self.__ccU.ccaLeavingAtomFlag] != 'Y':
                                                        checked = True
                                                        self.__f.append(f"[Hydrogen not instantiated] {self.__getCurrentRestraint()}"
                                                                        f"{chainId}:{seqId}:{compId}:{authAtomId} is not properly instantiated in the coordinates. "
                                                                        "Please re-upload the model file.")
                                            if not checked:
                                                if chainId in LARGE_ASYM_ID:
                                                    self.__f.append(f"[Atom not found] {self.__getCurrentRestraint()}"
                                                                    f"{chainId}:{seqId}:{compId}:{authAtomId} is not present in the coordinates.")
                                        return True

                    elif 'igr' in factor:
                        for igr, _atomId in zip(sorted(factor['igr']), atomIds):
                            _factor = copy.copy(factor)
                            ccdCheck = not cifCheck

                            if cifCheck:
                                if coordAtomSite is not None:
                                    if _atomId in coordAtomSite['atom_id']:
                                        found = True
                                    elif 'alt_atom_id' in coordAtomSite and _atomId in coordAtomSite['alt_atom_id']:
                                        found = True
                                        self.__authAtomId = 'auth_atom_id'
                                    elif self.__preferAuthSeq:
                                        _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId if cifSeqId is None else cifSeqId, cifCheck, asis=False)
                                        if _coordAtomSite is not None:
                                            if _atomId in _coordAtomSite['atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                self.__authSeqId = 'label_seq_id'
                                                seqKey = _seqKey
                                            elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                self.__authSeqId = 'label_seq_id'
                                                self.__authAtomId = 'auth_atom_id'
                                                seqKey = _seqKey

                                elif self.__preferAuthSeq:
                                    _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId if cifSeqId is None else cifSeqId, cifCheck, asis=False)
                                    if _coordAtomSite is not None:
                                        if _atomId in _coordAtomSite['atom_id']:
                                            found = True
                                            self.__preferAuthSeq = False
                                            self.__authSeqId = 'label_seq_id'
                                            seqKey = _seqKey
                                        elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                            found = True
                                            self.__preferAuthSeq = False
                                            self.__authSeqId = 'label_seq_id'
                                            self.__authAtomId = 'auth_atom_id'
                                            seqKey = _seqKey

                                if found:
                                    _factor['chain_id'] = chainId
                                    _factor['seq_id'] = seqId if cifSeqId is None else cifSeqId
                                    _factor['comp_id'] = compId
                                    _factor['atom_id'] = _atomId
                                    del _factor['igr']
                                    self.__sanderAtomNumberDict[igr] = _factor
                                else:
                                    ccdCheck = True

                            if ccdCheck:
                                if self.__ccU.updateChemCompDict(compId):
                                    cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId), None)
                                    if cca is not None:
                                        found = True
                                        _factor['chain_id'] = chainId
                                        _factor['seq_id'] = seqId if cifSeqId is None else cifSeqId
                                        _factor['comp_id'] = compId
                                        _factor['atom_id'] = _atomId
                                        del _factor['igr']
                                        self.__sanderAtomNumberDict[igr] = _factor
                                        if cifCheck and seqKey not in self.__coordUnobsRes and self.__ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] == 'REL':
                                            checked = False
                                            _seqId = _factor['seq_id']
                                            if _seqId == 1 or (chainId, _seqId - 1) in self.__coordUnobsRes or _seqId == ps['auth_seq_id'][0]:
                                                if coordAtomSite is not None and ((_atomId in aminoProtonCode and 'H1' in coordAtomSite['atom_id']) or _atomId == 'P'):
                                                    checked = True
                                            if _atomId[0] in protonBeginCode:
                                                bondedTo = self.__ccU.getBondedAtoms(compId, _atomId)
                                                if len(bondedTo) > 0:
                                                    if coordAtomSite is not None and bondedTo[0] in coordAtomSite['atom_id'] and cca[self.__ccU.ccaLeavingAtomFlag] != 'Y':
                                                        checked = True
                                                        self.__f.append(f"[Hydrogen not instantiated] {self.__getCurrentRestraint()}"
                                                                        f"{chainId}:{seqId}:{compId}:{authAtomId} is not properly instantiated in the coordinates. "
                                                                        "Please re-upload the model file.")
                                            if not checked:
                                                if chainId in LARGE_ASYM_ID:
                                                    self.__f.append(f"[Atom not found] {self.__getCurrentRestraint()}"
                                                                    f"{chainId}:{seqId}:{compId}:{authAtomId} is not present in the coordinates.")

                        if found:
                            return True

        if self.__hasNonPolySeq and useDefault:

            for np in self.__nonPolySeq:
                chainId = np['auth_chain_id']

                if factor['auth_seq_id'] in np['auth_seq_id']:
                    idx = np['auth_seq_id'].index(factor['auth_seq_id'])
                    seqId = np['seq_id'][idx]
                    compId = np['comp_id'][idx]

                    authCompId = factor['auth_comp_id'].upper() if 'auth_comp_id' in factor else 'None'
                    authAtomId = factor['auth_atom_id']

                    seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck)

                    if compId not in monDict3 and self.__mrAtomNameMapping is not None:
                        _, compId, authAtomId = retrieveAtomIdentFromMRMap(self.__mrAtomNameMapping, seqId, authCompId, authAtomId, coordAtomSite)

                    fixed = False
                    if self.__reasons is not None:
                        if 'unambig_atom_id_remap' in self.__reasons and authCompId in self.__reasons['unambig_atom_id_remap']\
                           and authAtomId in self.__reasons['unambig_atom_id_remap'][authCompId]:
                            atomIds = self.__reasons['unambig_atom_id_remap'][authCompId][authAtomId]
                            fixed = True
                    if len(self.unambigAtomNameMapping) > 0:
                        if authCompId in self.unambigAtomNameMapping\
                           and authAtomId in self.unambigAtomNameMapping[authCompId]:
                            atomIds = self.unambigAtomNameMapping[authCompId][authAtomId]
                            fixed = True

                    if not fixed:
                        atomIds = self.__nefT.get_valid_star_atom_in_xplor(compId, authAtomId)[0]

                    if coordAtomSite is not None\
                       and not any(_atomId for _atomId in atomIds if _atomId in coordAtomSite['atom_id'])\
                       and authAtomId in coordAtomSite['atom_id']:
                        atomIds = [authAtomId]

                    if 'iat' in factor:
                        iat = factor['iat']
                        for _atomId in atomIds:
                            ccdCheck = not cifCheck

                            if cifCheck:
                                if coordAtomSite is not None:
                                    if _atomId in coordAtomSite['atom_id']:
                                        found = True
                                    elif 'alt_atom_id' in coordAtomSite and _atomId in coordAtomSite['alt_atom_id']:
                                        found = True
                                        self.__authAtomId = 'auth_atom_id'
                                    elif self.__preferAuthSeq:
                                        _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck, asis=False)
                                        if _coordAtomSite is not None:
                                            if _atomId in _coordAtomSite['atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                self.__authSeqId = 'label_seq_id'
                                                seqKey = _seqKey
                                            elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                self.__authSeqId = 'label_seq_id'
                                                self.__authAtomId = 'auth_atom_id'
                                                seqKey = _seqKey

                                elif self.__preferAuthSeq:
                                    _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck, asis=False)
                                    if _coordAtomSite is not None:
                                        if _atomId in _coordAtomSite['atom_id']:
                                            found = True
                                            self.__preferAuthSeq = False
                                            self.__authSeqId = 'label_seq_id'
                                            seqKey = _seqKey
                                        elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                            found = True
                                            self.__preferAuthSeq = False
                                            self.__authSeqId = 'label_seq_id'
                                            self.__authAtomId = 'auth_atom_id'
                                            seqKey = _seqKey

                                if found:
                                    factor['chain_id'] = chainId
                                    factor['seq_id'] = seqId
                                    factor['comp_id'] = compId
                                    factor['atom_id'] = _atomId
                                    del factor['iat']
                                    self.__sanderAtomNumberDict[iat] = factor
                                    return True

                                ccdCheck = True

                            if ccdCheck:
                                if self.__ccU.updateChemCompDict(compId):
                                    cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId), None)
                                    if cca is not None:
                                        factor['chain_id'] = chainId
                                        factor['seq_id'] = seqId
                                        factor['comp_id'] = compId
                                        factor['atom_id'] = _atomId
                                        del factor['iat']
                                        self.__sanderAtomNumberDict[iat] = factor
                                        if cifCheck and seqKey not in self.__coordUnobsRes and self.__ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] == 'REL':
                                            checked = False
                                            if seqId == 1 or (chainId, seqId - 1) in self.__coordUnobsRes or seqId == np['auth_seq_id'][0]:
                                                if coordAtomSite is not None and ((_atomId in aminoProtonCode and 'H1' in coordAtomSite['atom_id']) or _atomId == 'P'):
                                                    checked = True
                                            if _atomId[0] in protonBeginCode:
                                                bondedTo = self.__ccU.getBondedAtoms(compId, _atomId)
                                                if len(bondedTo) > 0:
                                                    if coordAtomSite is not None and bondedTo[0] in coordAtomSite['atom_id'] and cca[self.__ccU.ccaLeavingAtomFlag] != 'Y':
                                                        checked = True
                                                        self.__f.append(f"[Hydrogen not instantiated] {self.__getCurrentRestraint()}"
                                                                        f"{chainId}:{seqId}:{compId}:{authAtomId} is not properly instantiated in the coordinates. "
                                                                        "Please re-upload the model file.")
                                            if not checked:
                                                if chainId in LARGE_ASYM_ID:
                                                    self.__f.append(f"[Atom not found] {self.__getCurrentRestraint()}"
                                                                    f"{chainId}:{seqId}:{compId}:{authAtomId} is not present in the coordinates.")
                                        return True

                    elif 'igr' in factor:
                        for igr, _atomId in zip(sorted(factor['igr']), atomIds):
                            _factor = copy.copy(factor)
                            ccdCheck = not cifCheck

                            if cifCheck:
                                if coordAtomSite is not None:
                                    if _atomId in coordAtomSite['atom_id']:
                                        found = True
                                    elif 'alt_atom_id' in coordAtomSite and _atomId in coordAtomSite['alt_atom_id']:
                                        found = True
                                        self.__authAtomId = 'auth_atom_id'
                                    elif self.__preferAuthSeq:
                                        _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck, asis=False)
                                        if _coordAtomSite is not None:
                                            if _atomId in _coordAtomSite['atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                self.__authSeqId = 'label_seq_id'
                                                seqKey = _seqKey
                                            elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                self.__authSeqId = 'label_seq_id'
                                                self.__authAtomId = 'auth_atom_id'
                                                seqKey = _seqKey

                                elif self.__preferAuthSeq:
                                    _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck, asis=False)
                                    if _coordAtomSite is not None:
                                        if _atomId in _coordAtomSite['atom_id']:
                                            found = True
                                            self.__preferAuthSeq = False
                                            self.__authSeqId = 'label_seq_id'
                                            seqKey = _seqKey
                                        elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                            found = True
                                            self.__preferAuthSeq = False
                                            self.__authSeqId = 'label_seq_id'
                                            self.__authAtomId = 'auth_atom_id'
                                            seqKey = _seqKey

                                if found:
                                    _factor['chain_id'] = chainId
                                    _factor['seq_id'] = seqId
                                    _factor['comp_id'] = compId
                                    _factor['atom_id'] = _atomId
                                    del _factor['igr']
                                    self.__sanderAtomNumberDict[igr] = _factor
                                else:
                                    ccdCheck = True

                            if ccdCheck:
                                if self.__ccU.updateChemCompDict(compId):
                                    cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId), None)
                                    if cca is not None:
                                        found = True
                                        _factor['chain_id'] = chainId
                                        _factor['seq_id'] = seqId
                                        _factor['comp_id'] = compId
                                        _factor['atom_id'] = _atomId
                                        del _factor['igr']
                                        self.__sanderAtomNumberDict[igr] = _factor
                                        if cifCheck and seqKey not in self.__coordUnobsRes and self.__ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] == 'REL':
                                            checked = False
                                            if seqId == 1 or (chainId, seqId - 1) in self.__coordUnobsRes or seqId == np['auth_seq_id'][0]:
                                                if coordAtomSite is not None and ((_atomId in aminoProtonCode and 'H1' in coordAtomSite['atom_id']) or _atomId == 'P'):
                                                    checked = True
                                            if _atomId[0] in protonBeginCode:
                                                bondedTo = self.__ccU.getBondedAtoms(compId, _atomId)
                                                if len(bondedTo) > 0:
                                                    if coordAtomSite is not None and bondedTo[0] in coordAtomSite['atom_id'] and cca[self.__ccU.ccaLeavingAtomFlag] != 'Y':
                                                        checked = True
                                                        self.__f.append(f"[Hydrogen not instantiated] {self.__getCurrentRestraint()}"
                                                                        f"{chainId}:{seqId}:{compId}:{authAtomId} is not properly instantiated in the coordinates. "
                                                                        "Please re-upload the model file.")
                                            if not checked:
                                                if chainId in LARGE_ASYM_ID:
                                                    self.__f.append(f"[Atom not found] {self.__getCurrentRestraint()}"
                                                                    f"{chainId}:{seqId}:{compId}:{authAtomId} is not present in the coordinates.")

                        if found:
                            return True

        if not useDefault or self.__altPolySeq is None:
            return False

        return self.updateSanderAtomNumberDict(factor, cifCheck, False)

    def updateSanderAtomNumberDictWithAmbigCode(self, factor, cifCheck=True, useDefault=True):
        """ Try to update Sander atom number dictionary.
        """
        if not self.__hasPolySeq:
            return False

        authCompId = factor['auth_comp_id'].upper() if 'auth_comp_id' in factor else 'None'
        authAtomId = factor['auth_atom_id']

        atomIdList = None

        try:

            if self.__reasons is not None and 'ambig_atom_id_remap' in self.__reasons\
               and authCompId in self.__reasons['ambig_atom_id_remap'] and authAtomId in self.__reasons['ambig_atom_id_remap'][authCompId]:
                atomIdList = self.__reasons['ambig_atom_id_remap'][authCompId][authAtomId]['atom_id_list']

            if len(self.ambigAtomNameMapping) > 0\
               and authCompId in self.ambigAtomNameMapping and authAtomId in self.ambigAtomNameMapping[authCompId]:
                atomIdList = self.ambigAtomNameMapping[authCompId][authAtomId]['atom_id_list']

        except KeyError:
            return False

        if atomIdList is None or len(atomIdList) == 0:
            return False

        if not self.__hasCoord:
            cifCheck = False

        allFound = True

        enforceAuthSeq = self.__reasons is not None and 'auth_seq_scheme' in self.__reasons

        for atom in atomIdList:
            chainId = atom['chain_id']
            seqId = atom['seq_id']
            authCompId = atom['comp_id']
            authAtomId = _authAtomId = atom['atom_id']

            found = False

            for ps in (self.__polySeq if useDefault else self.__altPolySeq):
                if ps['auth_chain_id'] != chainId:
                    continue

                if not useDefault and seqId not in ps['auth_seq_id'] and 'gap_in_auth_seq' in ps:
                    min_auth_seq_id = ps['auth_seq_id'][0]
                    max_auth_seq_id = ps['auth_seq_id'][-1]
                    if min_auth_seq_id <= seqId <= max_auth_seq_id:
                        offset = 1
                        while seqId + offset <= max_auth_seq_id:
                            if seqId + offset in ps['auth_seq_id']:
                                break
                            offset += 1
                        if seqId + offset not in ps['auth_seq_id']:
                            offset = -1
                            while seqId + offset >= min_auth_seq_id:
                                if seqId + offset in ps['auth_seq_id']:
                                    break
                                offset -= 1
                        if seqId + offset in ps['auth_seq_id']:
                            idx = ps['auth_seq_id'].index(seqId + offset) - offset
                            try:
                                seqId = ps['auth_seq_id'][idx]
                            except IndexError:
                                pass

                if seqId in (ps['seq_id'] if useDefault and not enforceAuthSeq else ps['auth_seq_id']):
                    idx = ps['seq_id'].index(seqId) if useDefault and not enforceAuthSeq else ps['auth_seq_id'].index(seqId)
                    compId = ps['comp_id'][idx]
                    origCompId = ps['auth_comp_id'][idx]
                    cifSeqId = None if useDefault else ps['seq_id'][idx]

                    if compId not in monDict3 and self.__mrAtomNameMapping is not None:
                        _, authCompId, _authAtomId = retrieveAtomIdentFromMRMap(self.__mrAtomNameMapping, seqId, origCompId, authAtomId)

                    if (((authCompId in (compId, origCompId, 'None') or compId not in monDict3) and useDefault) or not useDefault)\
                       or compId == translateToStdResName(authCompId, self.__ccU):

                        seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId if cifSeqId is None else cifSeqId, cifCheck)
                        if coordAtomSite is not None and _authAtomId in coordAtomSite['atom_id']:
                            authAtomId = _authAtomId

                        atomIds = self.__nefT.get_valid_star_atom_in_xplor(compId, authAtomId)[0]

                        if coordAtomSite is not None\
                           and not any(_atomId for _atomId in atomIds if _atomId in coordAtomSite['atom_id'])\
                           and authAtomId in coordAtomSite['atom_id']:
                            atomIds = [authAtomId]

                        if 'iat' in factor:
                            iat = factor['iat']
                            for _atomId in atomIds:
                                ccdCheck = not cifCheck

                                if cifCheck:
                                    if coordAtomSite is not None:
                                        if _atomId in coordAtomSite['atom_id']:
                                            found = True
                                        elif 'alt_atom_id' in coordAtomSite and _atomId in coordAtomSite['alt_atom_id']:
                                            found = True
                                            self.__authAtomId = 'auth_atom_id'
                                        elif self.__preferAuthSeq:
                                            _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId if cifSeqId is None else cifSeqId, cifCheck, asis=False)
                                            if _coordAtomSite is not None:
                                                if _atomId in _coordAtomSite['atom_id']:
                                                    found = True
                                                    self.__preferAuthSeq = False
                                                    self.__authSeqId = 'label_seq_id'
                                                    seqKey = _seqKey
                                                elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                    found = True
                                                    self.__preferAuthSeq = False
                                                    self.__authSeqId = 'label_seq_id'
                                                    self.__authAtomId = 'auth_atom_id'
                                                    seqKey = _seqKey

                                    elif self.__preferAuthSeq:
                                        _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId if cifSeqId is None else cifSeqId, cifCheck, asis=False)
                                        if _coordAtomSite is not None:
                                            if _atomId in _coordAtomSite['atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                self.__authSeqId = 'label_seq_id'
                                                seqKey = _seqKey
                                            elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                self.__authSeqId = 'label_seq_id'
                                                self.__authAtomId = 'auth_atom_id'
                                                seqKey = _seqKey

                                    if found:
                                        factor['chain_id'] = chainId
                                        factor['seq_id'] = seqId if cifSeqId is None else cifSeqId
                                        factor['comp_id'] = compId
                                        factor['atom_id'] = _atomId
                                        del factor['iat']
                                        self.__sanderAtomNumberDict[iat] = factor
                                        break

                                    ccdCheck = True

                                if ccdCheck:
                                    if self.__ccU.updateChemCompDict(compId):
                                        cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId), None)
                                        if cca is not None:
                                            factor['chain_id'] = chainId
                                            factor['seq_id'] = seqId if cifSeqId is None else cifSeqId
                                            factor['comp_id'] = compId
                                            factor['atom_id'] = _atomId
                                            del factor['iat']
                                            self.__sanderAtomNumberDict[iat] = factor
                                            if cifCheck and seqKey not in self.__coordUnobsRes and self.__ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] == 'REL':
                                                checked = False
                                                _seqId = factor['seq_id']
                                                if _seqId == 1 or (chainId, _seqId - 1) in self.__coordUnobsRes or _seqId == ps['auth_seq_id'][0]:
                                                    if coordAtomSite is not None and ((_atomId in aminoProtonCode and 'H1' in coordAtomSite['atom_id']) or _atomId == 'P'):
                                                        checked = True
                                                if _atomId[0] in protonBeginCode:
                                                    bondedTo = self.__ccU.getBondedAtoms(compId, _atomId)
                                                    if len(bondedTo) > 0:
                                                        if coordAtomSite is not None and bondedTo[0] in coordAtomSite['atom_id'] and cca[self.__ccU.ccaLeavingAtomFlag] != 'Y':
                                                            checked = True
                                                            self.__f.append(f"[Hydrogen not instantiated] {self.__getCurrentRestraint()}"
                                                                            f"{chainId}:{seqId}:{compId}:{authAtomId} is not properly instantiated in the coordinates. "
                                                                            "Please re-upload the model file.")
                                                if not checked:
                                                    if chainId in LARGE_ASYM_ID:
                                                        self.__f.append(f"[Atom not found] {self.__getCurrentRestraint()}"
                                                                        f"{chainId}:{seqId}:{compId}:{authAtomId} is not present in the coordinates.")
                                            break

                        elif 'igr' in factor:
                            for igr, _atomId in zip(sorted(factor['igr']), atomIds):
                                _factor = copy.copy(factor)
                                ccdCheck = not cifCheck

                                if cifCheck:
                                    if coordAtomSite is not None:
                                        if _atomId in coordAtomSite['atom_id']:
                                            found = True
                                        elif 'alt_atom_id' in coordAtomSite and _atomId in coordAtomSite['alt_atom_id']:
                                            found = True
                                            self.__authAtomId = 'auth_atom_id'
                                        elif self.__preferAuthSeq:
                                            _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId if cifSeqId is None else cifSeqId, cifCheck, asis=False)
                                            if _coordAtomSite is not None:
                                                if _atomId in _coordAtomSite['atom_id']:
                                                    found = True
                                                    self.__preferAuthSeq = False
                                                    self.__authSeqId = 'label_seq_id'
                                                    seqKey = _seqKey
                                                elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                    found = True
                                                    self.__preferAuthSeq = False
                                                    self.__authSeqId = 'label_seq_id'
                                                    self.__authAtomId = 'auth_atom_id'
                                                    seqKey = _seqKey

                                    elif self.__preferAuthSeq:
                                        _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId if cifSeqId is None else cifSeqId, cifCheck, asis=False)
                                        if _coordAtomSite is not None:
                                            if _atomId in _coordAtomSite['atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                self.__authSeqId = 'label_seq_id'
                                                seqKey = _seqKey
                                            elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                self.__authSeqId = 'label_seq_id'
                                                self.__authAtomId = 'auth_atom_id'
                                                seqKey = _seqKey

                                    if found:
                                        _factor['chain_id'] = chainId
                                        _factor['seq_id'] = seqId if cifSeqId is None else cifSeqId
                                        _factor['comp_id'] = compId
                                        _factor['atom_id'] = _atomId
                                        del _factor['igr']
                                        self.__sanderAtomNumberDict[igr] = _factor
                                    else:
                                        ccdCheck = True

                                if ccdCheck:
                                    if self.__ccU.updateChemCompDict(compId):
                                        cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId), None)
                                        if cca is not None:
                                            found = True
                                            _factor['chain_id'] = chainId
                                            _factor['seq_id'] = seqId if cifSeqId is None else cifSeqId
                                            _factor['comp_id'] = compId
                                            _factor['atom_id'] = _atomId
                                            del _factor['igr']
                                            self.__sanderAtomNumberDict[igr] = _factor
                                            if cifCheck and seqKey not in self.__coordUnobsRes and self.__ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] == 'REL':
                                                checked = False
                                                _seqId = _factor['seq_id']
                                                if _seqId == 1 or (chainId, _seqId - 1) in self.__coordUnobsRes or _seqId == ps['auth_seq_id'][0]:
                                                    if coordAtomSite is not None and ((_atomId in aminoProtonCode and 'H1' in coordAtomSite['atom_id']) or _atomId == 'P'):
                                                        checked = True
                                                if _atomId[0] in protonBeginCode:
                                                    bondedTo = self.__ccU.getBondedAtoms(compId, _atomId)
                                                    if len(bondedTo) > 0:
                                                        if coordAtomSite is not None and bondedTo[0] in coordAtomSite['atom_id'] and cca[self.__ccU.ccaLeavingAtomFlag] != 'Y':
                                                            checked = True
                                                            self.__f.append(f"[Hydrogen not instantiated] {self.__getCurrentRestraint()}"
                                                                            f"{chainId}:{seqId}:{compId}:{authAtomId} is not properly instantiated in the coordinates. "
                                                                            "Please re-upload the model file.")
                                                if not checked:
                                                    if chainId in LARGE_ASYM_ID:
                                                        self.__f.append(f"[Atom not found] {self.__getCurrentRestraint()}"
                                                                        f"{chainId}:{seqId}:{compId}:{authAtomId} is not present in the coordinates.")

            if not found and self.__hasNonPolySeq and useDefault:

                for np in self.__nonPolySeq:
                    if np['auth_chain_id'] != chainId:
                        continue

                    if seqId in np['auth_seq_id']:
                        idx = np['auth_seq_id'].index(factor['auth_seq_id'])
                        seqId = np['seq_id'][idx]
                        compId = np['comp_id'][idx]

                        seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck)

                        if compId not in monDict3 and self.__mrAtomNameMapping is not None:
                            origCompId = np['auth_comp_id'][idx]
                            _, compId, authAtomId = retrieveAtomIdentFromMRMap(self.__mrAtomNameMapping, seqId, origCompId, authAtomId, coordAtomSite)

                        atomIds = self.__nefT.get_valid_star_atom_in_xplor(compId, authAtomId)[0]

                        if coordAtomSite is not None\
                           and not any(_atomId for _atomId in atomIds if _atomId in coordAtomSite['atom_id'])\
                           and authAtomId in coordAtomSite['atom_id']:
                            atomIds = [authAtomId]

                        if 'iat' in factor:
                            iat = factor['iat']
                            for _atomId in atomIds:
                                ccdCheck = not cifCheck

                                if cifCheck:
                                    if coordAtomSite is not None:
                                        if _atomId in coordAtomSite['atom_id']:
                                            found = True
                                        elif 'alt_atom_id' in coordAtomSite and _atomId in coordAtomSite['alt_atom_id']:
                                            found = True
                                            self.__authAtomId = 'auth_atom_id'
                                        elif self.__preferAuthSeq:
                                            _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck, asis=False)
                                            if _coordAtomSite is not None:
                                                if _atomId in _coordAtomSite['atom_id']:
                                                    found = True
                                                    self.__preferAuthSeq = False
                                                    self.__authSeqId = 'label_seq_id'
                                                    seqKey = _seqKey
                                                elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                    found = True
                                                    self.__preferAuthSeq = False
                                                    self.__authSeqId = 'label_seq_id'
                                                    self.__authAtomId = 'auth_atom_id'
                                                    seqKey = _seqKey

                                    elif self.__preferAuthSeq:
                                        _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck, asis=False)
                                        if _coordAtomSite is not None:
                                            if _atomId in _coordAtomSite['atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                self.__authSeqId = 'label_seq_id'
                                                seqKey = _seqKey
                                            elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                self.__authSeqId = 'label_seq_id'
                                                self.__authAtomId = 'auth_atom_id'
                                                seqKey = _seqKey

                                    if found:
                                        factor['chain_id'] = chainId
                                        factor['seq_id'] = seqId
                                        factor['comp_id'] = compId
                                        factor['atom_id'] = _atomId
                                        del factor['iat']
                                        self.__sanderAtomNumberDict[iat] = factor
                                        break

                                    ccdCheck = True

                                if ccdCheck:
                                    if self.__ccU.updateChemCompDict(compId):
                                        cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId), None)
                                        if cca is not None:
                                            factor['chain_id'] = chainId
                                            factor['seq_id'] = seqId
                                            factor['comp_id'] = compId
                                            factor['atom_id'] = _atomId
                                            del factor['iat']
                                            self.__sanderAtomNumberDict[iat] = factor
                                            if cifCheck and seqKey not in self.__coordUnobsRes and self.__ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] == 'REL':
                                                checked = False
                                                if seqId == 1 or (chainId, seqId - 1) in self.__coordUnobsRes or seqId == np['auth_seq_id'][0]:
                                                    if coordAtomSite is not None and ((_atomId in aminoProtonCode and 'H1' in coordAtomSite['atom_id']) or _atomId == 'P'):
                                                        checked = True
                                                if _atomId[0] in protonBeginCode:
                                                    bondedTo = self.__ccU.getBondedAtoms(compId, _atomId)
                                                    if len(bondedTo) > 0:
                                                        if coordAtomSite is not None and bondedTo[0] in coordAtomSite['atom_id'] and cca[self.__ccU.ccaLeavingAtomFlag] != 'Y':
                                                            checked = True
                                                            self.__f.append(f"[Hydrogen not instantiated] {self.__getCurrentRestraint()}"
                                                                            f"{chainId}:{seqId}:{compId}:{authAtomId} is not properly instantiated in the coordinates. "
                                                                            "Please re-upload the model file.")
                                                if not checked:
                                                    if chainId in LARGE_ASYM_ID:
                                                        self.__f.append(f"[Atom not found] {self.__getCurrentRestraint()}"
                                                                        f"{chainId}:{seqId}:{compId}:{authAtomId} is not present in the coordinates.")
                                            break

                        elif 'igr' in factor:
                            for igr, _atomId in zip(sorted(factor['igr']), atomIds):
                                _factor = copy.copy(factor)
                                ccdCheck = not cifCheck

                                if cifCheck:
                                    if coordAtomSite is not None:
                                        if _atomId in coordAtomSite['atom_id']:
                                            found = True
                                        elif 'alt_atom_id' in coordAtomSite and _atomId in coordAtomSite['alt_atom_id']:
                                            found = True
                                            self.__authAtomId = 'auth_atom_id'
                                        elif self.__preferAuthSeq:
                                            _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck, asis=False)
                                            if _coordAtomSite is not None:
                                                if _atomId in _coordAtomSite['atom_id']:
                                                    found = True
                                                    self.__preferAuthSeq = False
                                                    self.__authSeqId = 'label_seq_id'
                                                    seqKey = _seqKey
                                                elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                    found = True
                                                    self.__preferAuthSeq = False
                                                    self.__authSeqId = 'label_seq_id'
                                                    self.__authAtomId = 'auth_atom_id'
                                                    seqKey = _seqKey

                                    elif self.__preferAuthSeq:
                                        _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCheck, asis=False)
                                        if _coordAtomSite is not None:
                                            if _atomId in _coordAtomSite['atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                self.__authSeqId = 'label_seq_id'
                                                seqKey = _seqKey
                                            elif 'alt_atom_id' in _coordAtomSite and _atomId in _coordAtomSite['alt_atom_id']:
                                                found = True
                                                self.__preferAuthSeq = False
                                                self.__authSeqId = 'label_seq_id'
                                                self.__authAtomId = 'auth_atom_id'
                                                seqKey = _seqKey

                                    if found:
                                        _factor['chain_id'] = chainId
                                        _factor['seq_id'] = seqId
                                        _factor['comp_id'] = compId
                                        _factor['atom_id'] = _atomId
                                        del _factor['igr']
                                        self.__sanderAtomNumberDict[igr] = _factor
                                    else:
                                        ccdCheck = True

                                if ccdCheck:
                                    if self.__ccU.updateChemCompDict(compId):
                                        cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == _atomId), None)
                                        if cca is not None:
                                            found = True
                                            _factor['chain_id'] = chainId
                                            _factor['seq_id'] = seqId
                                            _factor['comp_id'] = compId
                                            _factor['atom_id'] = _atomId
                                            del _factor['igr']
                                            self.__sanderAtomNumberDict[igr] = _factor
                                            if cifCheck and seqKey not in self.__coordUnobsRes and self.__ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] == 'REL':
                                                checked = False
                                                if seqId == 1 or (chainId, seqId - 1) in self.__coordUnobsRes or seqId == np['auth_seq_id'][0]:
                                                    if coordAtomSite is not None and ((_atomId in aminoProtonCode and 'H1' in coordAtomSite['atom_id']) or _atomId == 'P'):
                                                        checked = True
                                                if _atomId[0] in protonBeginCode:
                                                    bondedTo = self.__ccU.getBondedTo(compId, _atomId)
                                                    if len(bondedTo) > 0:
                                                        if coordAtomSite is not None and bondedTo[0] in coordAtomSite['atom_id'] and cca[self.__ccU.ccaLeavingAtomFlag] != 'Y':
                                                            checked = True
                                                            self.__f.append(f"[Hydrogen not instantiated] {self.__getCurrentRestraint()}"
                                                                            f"{chainId}:{seqId}:{compId}:{authAtomId} is not properly instantiated in the coordinates. "
                                                                            "Please re-upload the model file.")
                                                if not checked:
                                                    if chainId in LARGE_ASYM_ID:
                                                        self.__f.append(f"[Atom not found] {self.__getCurrentRestraint()}"
                                                                        f"{chainId}:{seqId}:{compId}:{authAtomId} is not present in the coordinates.")

            if not found:
                allFound = False

        if allFound:
            return True

        if not useDefault or self.__altPolySeq is None:
            return False

        return self.updateSanderAtomNumberDictWithAmbigCode(factor, cifCheck, False)

    def getNeighborCandidateAtom(self, factor, src_atom, around):
        """ Try to find neighbor atom from given conditions.
        """
        if not self.__hasCoord:
            return None

        if self.__reasons is not None and 'auth_seq_scheme' in self.__reasons:
            self.__authAsymId = 'auth_asym_id'
            self.__authSeqId = 'auth_seq_id'

        try:

            _origin =\
                self.__cR.getDictListWithFilter('atom_site',
                                                CARTN_DATA_ITEMS,
                                                [{'name': self.__authAsymId, 'type': 'str', 'value': src_atom['chain_id']},
                                                 {'name': self.__authSeqId, 'type': 'int', 'value': src_atom['seq_id']},
                                                 {'name': self.__authAtomId, 'type': 'str', 'value': src_atom['atom_id']},
                                                 {'name': self.__modelNumName, 'type': 'int',
                                                  'value': self.__representativeModelId},
                                                 {'name': 'label_alt_id', 'type': 'enum',
                                                  'enum': ('A')}
                                                 ])

            if len(_origin) != 1:
                return None

            origin = toNpArray(_origin[0])

            _neighbor =\
                self.__cR.getDictListWithFilter('atom_site',
                                                AUTH_ATOM_CARTN_DATA_ITEMS,
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
                return None

            neighbor = [atom for atom in _neighbor if numpy.linalg.norm(toNpArray(atom) - origin) < around
                        and translateToStdResName(factor['auth_comp_id'], self.__ccU)
                        in (atom['comp_id'], translateToStdResName(atom['comp_id'], self.__ccU))
                        and atom['atom_id'][0] == factor['auth_atom_id'][0]]

            len_neighbor = len(neighbor)

            if len_neighbor == 0:
                return None

            if len_neighbor == 1:
                factor['auth_atom_id'] = neighbor[0]['atom_id']
                return factor

            atomList = []

            for n in neighbor:
                atomList.append({'chain_id': n['chain_id'], 'seq_id': n['seq_id'], 'comp_id': n['comp_id'], 'atom_id': n['atom_id'],
                                 'distance': numpy.linalg.norm(toNpArray(n) - origin)})

            p = sorted(atomList, key=itemgetter('distance'))[0]
            factor['auth_atom_id'] = p['atom_id']
            return factor

        except Exception as e:
            if self.__verbose:
                self.__lfh.write(f"+AmberMRParserListener.getNeighborCandidateAtom() ++ Error  - {str(e)}")

        return None

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

    # Enter a parse tree produced by AmberMRParser#restraint_factor.
    def enterRestraint_factor(self, ctx: AmberMRParser.Restraint_factorContext):
        if ctx.IAT():
            varName = 'iat'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if decimal <= 0 or decimal > MAX_COL_IAT:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{MAX_COL_IAT}.")
                    return
                if self.numIatCol > 0 and self.iresid == 0:
                    zeroCols = [col for col, val in enumerate(self.iat) if val == 0]
                    maxCol = MAX_COL_IAT if len(zeroCols) == 0 else min(zeroCols)
                    valArray = ','.join([str(val) for col, val in enumerate(self.iat) if val != 0 and col < maxCol])
                    self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                    f"You have mixed different syntaxes for the '{varName}' variable, '{varName}={valArray}' "
                                    f"and '{varName}({decimal})={str(ctx.Integers())}', which will overwrite.")
                if self.setIatCol is None:
                    self.setIatCol = []
                if decimal in self.setIatCol and self.iresid == 0:
                    self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                    f"The argument value of '{varName}({decimal})' must be unique. "
                                    f"'{varName}({decimal})={str(ctx.Integers())}' will overwrite.")
                else:
                    self.setIatCol.append(decimal)
                rawIntArray = str(ctx.Integers()).split(',')
                val = int(rawIntArray[0])
                if len(rawIntArray) > 1:
                    self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                    f"The '{varName}({decimal})={str(ctx.Integers())}' can not be an array of integers, "
                                    f"hence the first value '{varName}({decimal})={val}' will be evaluated as a valid value.")
                self.iat[decimal - 1] = val
                if val == 0:
                    self.setIatCol.remove(decimal)
                    if self.numIatCol >= decimal:
                        self.numIatCol = decimal - 1
                        self.__cur_subtype = ''
                else:
                    self.numIatCol = max(self.numIatCol, decimal)

            else:
                if ctx.Integers():
                    if self.setIatCol is not None and len(self.setIatCol) > 0 and self.iresid == 0:
                        valArray = ','.join([f"{varName}({valCol})={self.iat[valCol - 1]}"
                                             for valCol in self.setIatCol if self.iat[valCol - 1] != 0])
                        self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                        f"You have mixed different syntaxes for the '{varName}' variable, '{varName}={valArray}' "
                                        f"and '{varName}={str(ctx.Integers())}', which will overwrite.")
                    if self.numIatCol > 0 and self.iresid == 0:
                        zeroCols = [col for col, val in enumerate(self.iat) if val == 0]
                        maxCol = MAX_COL_IAT if len(zeroCols) == 0 else min(zeroCols)
                        valArray = ','.join([str(val) for col, val in enumerate(self.iat) if val != 0 and col < maxCol])
                        self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                        f"You have overwritten the '{varName}' variable, '{varName}={valArray}' "
                                        f"and '{varName}={str(ctx.Integers())}', which will overwrite.")
                    rawIntArray = str(ctx.Integers()).split(',')
                    numIatCol = 0
                    for col, rawInt in enumerate(rawIntArray):
                        val = int(rawInt)
                        if val == 0:
                            break
                        self.iat[col] = val
                        numIatCol += 1
                    self.numIatCol = numIatCol
                elif ctx.MultiplicativeInt():
                    if self.setIatCol is not None and len(self.setIatCol) > 0 and self.iresid == 0:
                        valArray = ','.join([f"{varName}({valCol})={self.iat[valCol - 1]}"
                                             for valCol in self.setIatCol if self.iat[valCol - 1] != 0])
                        self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                        f"You have mixed different syntaxes for the '{varName}' variable, '{varName}={valArray}' "
                                        f"and '{varName}={str(ctx.MultiplicativeInt())}', which will overwrite.")
                    if self.numIatCol > 0 and self.iresid == 0:
                        zeroCols = [col for col, val in enumerate(self.iat) if val == 0]
                        maxCol = MAX_COL_IAT if len(zeroCols) == 0 else min(zeroCols)
                        valArray = ','.join([str(val) for col, val in enumerate(self.iat) if val != 0 and col < maxCol])
                        self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                        f"You have overwritten the '{varName}' variable, '{varName}={valArray}' "
                                        f"and '{varName}={str(ctx.MultiplicativeInt())}', which will overwrite.")
                    offset = 0
                    for multiplicativeInt in str(ctx.MultiplicativeInt()).split(','):
                        rawMultInt = multiplicativeInt.split('*')
                        numIatCol = int(rawMultInt[0])
                        if offset + numIatCol <= 0 or offset + numIatCol > MAX_COL_IAT:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The argument value of '{varName}({numIatCol})' derived from "
                                            f"'{str(ctx.MultiplicativeInt())}' must be in the range 1-{MAX_COL_IAT}.")
                            return
                        val = int(rawMultInt[1])
                        for col in range(0, numIatCol):
                            self.iat[offset + col] = val
                        if val != 0:
                            self.numIatCol = offset + numIatCol
                        else:
                            self.numIatCol = 0
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The '{varName}' values '{val}' derived from "
                                            f"'{str(ctx.MultiplicativeInt())}' must be non-zero integer.")
                            break
                        offset += numIatCol
                    if self.numIatCol in (2, 3, 5, 6):  # possible to specify restraint type, see also detectRestraintType()
                        self.detectRestraintType(self.numIatCol in (2, 6))

        elif ctx.IGR1() or ctx.IGR2() or ctx.IGR3() or ctx.IGR4()\
                or ctx.IGR5() or ctx.IGR6() or ctx.IGR7() or ctx.IGR8():
            varNum = 0
            if ctx.IGR1():
                varNum = 1
            if ctx.IGR2():
                varNum = 2
            if ctx.IGR3():
                varNum = 3
            if ctx.IGR4():
                varNum = 4
            if ctx.IGR5():
                varNum = 5
            if ctx.IGR6():
                varNum = 6
            if ctx.IGR7():
                varNum = 7
            if ctx.IGR8():
                varNum = 8

            varName = 'igr' + str(varNum)

            if self.igr is None:
                self.igr = {}
                self.numIgrCol = {}
                self.setIgrCol = {}

            if varNum not in self.igr:
                self.igr[varNum] = [0] * MAX_COL_IGR
                self.numIgrCol[varNum] = 0
                self.setIgrCol[varNum] = None

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if decimal <= 0 or decimal > MAX_COL_IGR:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{MAX_COL_IGR}.")
                    return
                if self.numIgrCol[varNum] > 0:
                    nonpCols = [col for col, val in enumerate(self.igr[varNum]) if val <= 0]
                    maxCol = MAX_COL_IGR if len(nonpCols) == 0 else min(nonpCols)
                    valArray = ','.join([str(val) for col, val in enumerate(self.igr[varNum]) if val > 0 and col < maxCol])
                    self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                    f"You have mixed different syntaxes for the '{varName}' variable, '{varName}={valArray}' "
                                    f"and '{varName}({decimal})={str(ctx.Integers())}', which will overwrite.")
                if self.setIgrCol[varNum] is None:
                    self.setIgrCol[varNum] = []
                if decimal in self.setIgrCol[varNum]:
                    self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                    f"The argument value of '{varName}({decimal})' must be unique. "
                                    f"'{varName}({decimal})={str(ctx.Integers())}' will overwrite.")
                else:
                    self.setIgrCol[varNum].append(decimal)
                rawIntArray = str(ctx.Integers()).split(',')
                val = int(rawIntArray[0])
                if len(rawIntArray) > 1:
                    self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                    f"The '{varName}({decimal})={str(ctx.Integers())}' can not be an array of integers, "
                                    f"hence the first value '{varName}({decimal})={val}' will be evaluated as a valid value.")
                self.igr[varNum][decimal - 1] = val
                if val == 0:
                    self.setIgrCol[varNum].remove(decimal)
                    if self.numIgrCol[varNum] >= decimal:
                        self.numIgrCol[varNum] = decimal - 1

            else:
                if ctx.Integers():
                    if self.setIgrCol[varNum] is not None and len(self.setIgrCol[varNum]) > 0:
                        valArray = ','.join([f"{varName}({valCol})={self.igr[varNum][valCol - 1]}"
                                             for valCol in self.setIgrCol[varNum] if self.igr[varNum][valCol - 1] > 0])
                        self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                        f"You have mixed different syntaxes for the '{varName}' variable, '{varName}={valArray}' "
                                        f"and '{varName}={str(ctx.Integers())}', which will overwrite.")
                    if self.numIgrCol[varNum] > 0:
                        nonpCols = [col for col, val in enumerate(self.igr[varNum]) if val <= 0]
                        maxCol = MAX_COL_IGR if len(nonpCols) == 0 else min(nonpCols)
                        valArray = ','.join([str(val) for col, val in enumerate(self.igr[varNum]) if val > 0 and col < maxCol])
                        self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                        f"You have overwritten the '{varName}' variable, '{varName}={valArray}' "
                                        f"and '{varName}={str(ctx.Integers())}', which will overwrite.")
                    rawIntArray = str(ctx.Integers()).split(',')
                    numIgrCol = 0
                    for col, rawInt in enumerate(rawIntArray):
                        val = int(rawInt)
                        if val <= 0:
                            break
                        self.igr[varNum][col] = val
                        numIgrCol += 1
                    self.numIgrCol[varNum] = numIgrCol
                elif ctx.MultiplicativeInt():
                    if self.setIgrCol[varNum] is not None and len(self.setIgrCol[varNum]) > 0:
                        valArray = ','.join([f"{varName}({valCol})={self.igr[varNum][valCol - 1]}"
                                             for valCol in self.setIgrCol[varNum] if self.igr[varNum][valCol - 1] > 0])
                        self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                        f"You have mixed different syntaxes for the '{varName}' variable, '{varName}={valArray}' "
                                        f"and '{varName}={str(ctx.MultiplicativeInt())}', which will overwrite.")
                    if self.numIgrCol[varNum] > 0:
                        nonpCols = [col for col, val in enumerate(self.igr[varNum]) if val <= 0]
                        maxCol = MAX_COL_IGR if len(nonpCols) == 0 else min(nonpCols)
                        valArray = ','.join([str(val) for col, val in enumerate(self.igr[varNum]) if val > 0 and col < maxCol])
                        self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                        f"You have overwritten the '{varName}' variable, '{varName}={valArray}' "
                                        f"and '{varName}={str(ctx.MultiplicativeInt())}', which will overwrite.")
                    offset = 0
                    for multiplicativeInt in str(ctx.MultiplicativeInt()).split(','):
                        rawMultInt = multiplicativeInt.split('*')
                        numIgrCol = int(rawMultInt[0])
                        if offset + numIgrCol <= 0 or offset + numIgrCol > MAX_COL_IGR:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The argument value of '{varName}({numIgrCol})' derived from "
                                            f"'{str(ctx.MultiplicativeInt())}' must be in the range 1-{MAX_COL_IGR}.")
                            return
                        val = int(rawMultInt[1])
                        for col in range(0, numIgrCol):
                            self.igr[varNum][offset + col] = val
                        if val > 0:
                            self.numIgrCol[varNum] = offset + numIgrCol
                        else:
                            self.numIgrCol[varNum] = 0
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The '{varName}' values '{val}' derived from "
                                            f"'{str(ctx.MultiplicativeInt())}' must be positive integer.")
                            break
                        offset += numIgrCol

        elif ctx.R1():
            self.lowerLinearLimit = float(str(ctx.Real()))

        elif ctx.R2():
            self.lowerLimit = float(str(ctx.Real()))

        elif ctx.R3():
            self.upperLimit = float(str(ctx.Real()))

        elif ctx.R4():
            self.upperLinearLimit = float(str(ctx.Real()))

        elif ctx.RSTWT():
            varName = 'rstwt'

            self.detectRestraintType(False)

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if decimal <= 0 or decimal > MAX_COL_RSTWT:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{MAX_COL_RSTWT}.")
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                val = float(rawRealArray[0])
                self.rstwt[decimal - 1] = val
                if decimal == 1:
                    self.detectRestraintType(True)

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > MAX_COL_RSTWT:
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                        f"The length of '{varName}={','.join(rawRealArray)}' must not exceed {MAX_COL_RSTWT}.")
                        return
                    for col, rawReal in enumerate(rawRealArray):
                        val = float(rawReal)
                        self.rstwt[col] = val
                        if col == 1:
                            self.detectRestraintType(True)
                elif ctx.MultiplicativeReal():
                    offset = 0
                    for multiplicativeReal in str(ctx.MultiplicativeReal()).split(','):
                        rawMultReal = multiplicativeReal.split('*')
                        numCol = int(rawMultReal[0])
                        if offset + numCol <= 0 or offset + numCol > MAX_COL_RSTWT:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The argument value of '{varName}({numCol})' derived from "
                                            f"'{str(ctx.MultiplicativeReal())}' must not exceed {MAX_COL_RSTWT}.")
                            return
                        val = float(rawMultReal[1])
                        for col in range(0, numCol):
                            self.rstwt[offset + col] = val
                            if offset + col == 1:
                                self.detectRestraintType(True)
                        offset += numCol

        elif ctx.IALTD():
            self.detectRestraintType(True)

        elif ctx.RJCOEF():
            self.detectRestraintType(False)

        # Amber 10: ambmask
        elif ctx.RESTRAINT():
            self.hasFuncExprs = True
            self.inGenDist = False
            self.inPlane = False
            self.inPlane_columnSel = -1
            self.inCom = False
            self.funcExprs = []

        elif ctx.IXPK():
            self.ixpk = int(str(ctx.Integer()))

        elif ctx.NXPK():
            self.nxpk = int(str(ctx.Integer()))

        elif ctx.IRESID():
            self.iresid = int(str(ctx.BoolInt()))

        elif ctx.ATNAM():
            varName = 'atnam'

            if ctx.Qstrings():
                if self.setAtnamCol is not None and len(self.setAtnamCol) > 0:
                    valArray = ','.join([f"{varName}({valCol})={self.atnam[valCol - 1]}"
                                         for valCol in self.setAtnamCol if len(self.atnam[valCol - 1]) > 0])
                    self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                    f"You have mixed different syntaxes for the '{varName}' variable, '{varName}={valArray}' "
                                    f"and '{varName}={str(ctx.Qstrings())}', which will overwrite.")
                if self.numAtnamCol > 0:
                    zeroCols = [col for col, val in enumerate(self.atnam) if len(val) == 0]
                    maxCol = MAX_COL_IAT if len(zeroCols) == 0 else min(zeroCols)
                    valArray = ','.join([str(val) for col, val in enumerate(self.atnam) if len(val) > 0 and col < maxCol])
                    self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                    f"You have overwritten the '{varName}' variable, '{varName}={valArray}' "
                                    f"and '{varName}={str(ctx.Qstrings())}', which will overwrite.")
                rawStrArray = str(ctx.Qstrings()).split(',')
                numAtnamCol = 0
                for col, rawStr in enumerate(rawStrArray):
                    val = stripQuot(rawStr)
                    if len(val) == 0:
                        break
                    self.atnam[col] = val
                    numAtnamCol += 1
                self.numAtnamCol = numAtnamCol

        elif ctx.ATNAM_Lp():
            varName = 'atnam'

            if ctx.Decimal_AP():
                decimal = int(str(ctx.Decimal_AP()))
                if decimal <= 0 or decimal > MAX_COL_IAT:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{MAX_COL_IAT}.")
                    return
                if self.numAtnamCol > 0:
                    zeroCols = [col for col, val in enumerate(self.atnam) if len(val) == 0]
                    maxCol = MAX_COL_IAT if len(zeroCols) == 0 else min(zeroCols)
                    valArray = ','.join([str(val) for col, val in enumerate(self.atnam) if len(val) > 0 and col < maxCol])
                    self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                    f"You have mixed different syntaxes for the '{varName}' variable, '{varName}={valArray}' "
                                    f"and '{varName}({decimal})={str(ctx.Qstring_AP())}', which will overwrite.")
                if self.setAtnamCol is None:
                    self.setAtnamCol = []
                if decimal in self.setAtnamCol:
                    self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                    f"The argument value of '{varName}({decimal})' must be unique. "
                                    f"'{varName}({decimal})={str(ctx.Qstring_AP())}' will overwrite.")
                else:
                    self.setAtnamCol.append(decimal)
                rawStrArray = str(ctx.Qstring_AP()).split(',')
                val = stripQuot(rawStrArray[0])
                if len(rawStrArray) > 1:
                    self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                    f"The '{varName}({decimal})={str(ctx.Qstring_AP())}' can not be an array of strings, "
                                    f"hence the first value '{varName}({decimal})={val}' will be evaluated as a valid value.")
                self.atnam[decimal - 1] = val
                if len(val) == 0:
                    self.setAtnamCol.remove(decimal)
                    if self.numAtnamCol >= decimal:
                        self.numAtnamCol = decimal - 1

        elif ctx.GRNAM1() or ctx.GRNAM2() or ctx.GRNAM3() or ctx.GRNAM4()\
                or ctx.GRNAM5() or ctx.GRNAM6() or ctx.GRNAM7() or ctx.GRNAM8():
            varNum = 0
            if ctx.GRNAM1():
                varNum = 1
            if ctx.GRNAM2():
                varNum = 2
            if ctx.GRNAM3():
                varNum = 3
            if ctx.GRNAM4():
                varNum = 4
            if ctx.GRNAM5():
                varNum = 5
            if ctx.GRNAM6():
                varNum = 6
            if ctx.GRNAM7():
                varNum = 7
            if ctx.GRNAM8():
                varNum = 8

            varName = 'grnam' + str(varNum)

            if ctx.Qstrings():
                if self.setGrnamCol[varNum] is not None and len(self.setGrnamCol[varNum]) > 0:
                    valArray = ','.join([f"{varName}({valCol})={self.grnam[varNum][valCol - 1]}"
                                         for valCol in self.setGrnamCol[varNum] if len(self.grnam[varNum][valCol - 1]) > 0])
                    self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                    f"You have mixed different syntaxes for the '{varName}' variable, '{varName}={valArray}' "
                                    f"and '{varName}={str(ctx.Qstrings())}', which will overwrite.")
                if self.numGrnamCol[varNum] > 0:
                    nonpCols = [col for col, val in enumerate(self.grnam[varNum]) if len(val) == 0]
                    maxCol = MAX_COL_IGR if len(nonpCols) == 0 else min(nonpCols)
                    valArray = ','.join([str(val) for col, val in enumerate(self.grnam[varNum]) if len(val) > 0 and col < maxCol])
                    self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                    f"You have overwritten the '{varName}' variable, '{varName}={valArray}' "
                                    f"and '{varName}={str(ctx.Qstrings())}', which will overwrite.")
                rawStrArray = str(ctx.Qstrings()).split(',')
                numGrnamCol = 0
                for col, rawStr in enumerate(rawStrArray):
                    val = stripQuot(rawStr)
                    if len(val) == 0:
                        break
                    self.grnam[varNum][col] = val
                    numGrnamCol += 1
                self.numGrnamCol[varNum] = numGrnamCol

        elif ctx.GRNAM1_Lp() or ctx.GRNAM2_Lp() or ctx.GRNAM3_Lp() or ctx.GRNAM4_Lp()\
                or ctx.GRNAM5_Lp() or ctx.GRNAM6_Lp() or ctx.GRNAM7_Lp() or ctx.GRNAM8_Lp():
            varNum = 0
            if ctx.GRNAM1_Lp():
                varNum = 1
            if ctx.GRNAM2_Lp():
                varNum = 2
            if ctx.GRNAM3_Lp():
                varNum = 3
            if ctx.GRNAM4_Lp():
                varNum = 4
            if ctx.GRNAM5_Lp():
                varNum = 5
            if ctx.GRNAM6_Lp():
                varNum = 6
            if ctx.GRNAM7_Lp():
                varNum = 7
            if ctx.GRNAM8_Lp():
                varNum = 8

            varName = 'grnam' + str(varNum)

            if self.grnam is None:
                self.grnam = {}
                self.numGrnamCol = {}
                self.setGrnamCol = {}

            if varNum not in self.grnam:
                self.grnam[varNum] = [''] * MAX_COL_IGR
                self.numGrnamCol[varNum] = 0
                self.setGrnamCol[varNum] = None

            if ctx.Decimal_AP():
                decimal = int(str(ctx.Decimal_AP()))
                if decimal <= 0 or decimal > MAX_COL_IGR:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{MAX_COL_IGR}.")
                    return
                if self.numGrnamCol[varNum] > 0:
                    nonpCols = [col for col, val in enumerate(self.grnam[varNum]) if len(val) == 0]
                    maxCol = MAX_COL_IGR if len(nonpCols) == 0 else min(nonpCols)
                    valArray = ','.join([str(val) for col, val in enumerate(self.grnam[varNum]) if len(val) > 0 and col < maxCol])
                    self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                    f"You have mixed different syntaxes for the '{varName}' variable, '{varName}={valArray}' "
                                    f"and '{varName}({decimal})={str(ctx.Qstring_AP())}', which will overwrite.")
                if self.setGrnamCol[varNum] is None:
                    self.setGrnamCol[varNum] = []
                if decimal in self.setGrnamCol[varNum]:
                    self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                    f"The argument value of '{varName}({decimal})' must be unique. "
                                    f"'{varName}({decimal})={str(ctx.Qstring_AP())}' will overwrite.")
                else:
                    self.setGrnamCol[varNum].append(decimal)
                rawStrArray = str(ctx.Qstring_AP()).split(',')
                val = stripQuot(rawStrArray[0])
                if len(rawStrArray) > 1:
                    self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                    f"The '{varName}({decimal})={str(ctx.Qstring_AP())}' can not be an array of strings, "
                                    f"hence the first value '{varName}({decimal})={val}' will be evaluated as a valid value.")
                self.grnam[varNum][decimal - 1] = val
                if len(val) == 0:
                    self.setGrnamCol[varNum].remove(decimal)
                    if self.numGrnamCol[varNum] >= decimal:
                        self.numGrnamCol[varNum] = decimal - 1

    def detectRestraintType(self, likeDist):
        self.likeDist = likeDist

        if len(self.__cur_subtype) > 0:
            return

        if self.numIatCol == COL_DIST:
            self.distRestraints += 1
            self.__cur_subtype = 'dist'

        elif self.numIatCol == COL_ANG:
            self.angRestraints += 1
            self.__cur_subtype = 'ang'

        elif self.numIatCol == COL_DIHED:  # torsional angle or generalized distance 2
            if likeDist:
                self.geoRestraints += 1
                self.__cur_subtype = 'geo'
            else:
                self.dihedRestraints += 1
                self.__cur_subtype = 'dihed'

        elif self.numIatCol == COL_PLANE_POINT:
            self.planeRestraints += 1
            self.__cur_subtype = 'plane'

        elif self.numIatCol == COL_DIST_COORD3:  # generalized distance 3
            self.geoRestraints += 1
            self.__cur_subtype = 'geo'

        elif self.numIatCol == COL_PLANE_PLANE:  # plane-plane angle or generalized distance 4
            if likeDist:
                self.geoRestraints += 1
                self.__cur_subtype = 'geo'
            else:
                self.planeRestraints += 1
                self.__cur_subtype = 'plane'

    # Exit a parse tree produced by AmberMRParser#restraint_factor.
    def exitRestraint_factor(self, ctx: AmberMRParser.Restraint_factorContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#noeexp_statement.
    def enterNoeexp_statement(self, ctx: AmberMRParser.Noeexp_statementContext):  # pylint: disable=unused-argument
        self.noepkRestraints += 1
        self.__cur_subtype = 'noepk'

        self.ihp = {}
        self.jhp = {}
        self.aexp = {}
        self.arange = {}
        self.awt = {}
        self.emix = {}
        self.npeak = {}
        self.invwt1 = 0.0
        self.invwt2 = 0.0
        self.omega = 500.0  # MHz
        self.taurot = 1.0  # ns
        self.taumet = 0.0001  # ns
        self.id2o = 0

        if self.__createSfDict:
            self.__addSf()

    # Exit a parse tree produced by AmberMRParser#noeexp_statement.
    def exitNoeexp_statement(self, ctx: AmberMRParser.Noeexp_statementContext):  # pylint: disable=unused-argument
        try:

            imixes = self.npeak.keys()
            if len(imixes) <= 0:
                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                "No NOESY experiment exists.")
                return

            for imix in imixes:

                if imix not in self.emix:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                    f"The mixing time of the NOESY experiment emix({imix}) is unknown.")
                    continue

                mix = self.emix[imix]

                for ipeak in range(1, self.npeak[imix] + 1):

                    if ipeak not in self.ihp[imix]:
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"
                                        f"The atom number involved in the NOESY peak ihp({imix},{ipeak}) was not set.")
                        continue

                    if ipeak not in self.jhp[imix]:
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"
                                        f"The atom number involved in the NOESY peak jhp({imix},{ipeak}) was not set.")
                        continue

                    if ipeak not in self.aexp[imix]:
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"
                                        f"The NOESY peak volume aexp({imix},{ipeak}) was not set.")
                        continue

                    _iprot = self.ihp[imix][ipeak]
                    _jprot = self.jhp[imix][ipeak]

                    if _iprot <= 0:
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"
                                        f"The atom number involved in the NOESY peak 'ihp({imix},{ipeak})={_iprot}' should be a positive integer.")
                        continue

                    if _jprot <= 0:
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"
                                        f"The atom number involved in the NOESY peak 'jhp({imix},{ipeak})={_jprot}' should be a positive integer.")
                        continue

                    awt = 1.0
                    if imix in self.awt and ipeak in self.awt[imix]:
                        awt = self.awt[imix][ipeak]
                        if awt <= 0.0:
                            awt = 1.0

                    arange = 0.0
                    if imix in self.arange and ipeak in self.arange[imix]:
                        arange = max(self.arange[imix][ipeak], 0.0)

                    # convert AMBER atom numbers to corresponding coordinate atoms based on AMBER parameter/topology file
                    if self.__atomNumberDict is not None:

                        self.atomSelectionSet = []

                        atomSelection = []

                        if _iprot in self.__atomNumberDict:
                            atomSelection.append(copy.copy(self.__atomNumberDict[_iprot]))
                        else:
                            self.__f.append(f"[Missing data] {self.__getCurrentRestraint(imix,ipeak)}"
                                            f"'ihp({imix},{ipeak})={_iprot}' is not defined in the AMBER parameter/topology file.")
                            continue

                        chain_id = atomSelection[0]['chain_id']
                        seq_id = atomSelection[0]['seq_id']
                        comp_id = atomSelection[0]['comp_id']
                        atom_id = atomSelection[0].get('atom_id', None)
                        if atom_id is None:
                            atom_id = atomSelection[0]['atom_id'] = atomSelection[0]['auth_atom_id']

                        self.atomSelectionSet.append(atomSelection)

                        if atom_id[0] not in protonBeginCode:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"
                                            f"({chain_id}:{seq_id}:{comp_id}:{atom_id} (derived from ihp) is not a proton.")
                            continue

                        atomSelection = []

                        if _jprot in self.__atomNumberDict:
                            atomSelection.append(copy.copy(self.__atomNumberDict[_jprot]))
                        else:
                            self.__f.append(f"[Missing data] {self.__getCurrentRestraint(imix,ipeak)}"
                                            f"'jhp({imix},{ipeak})={_jprot}' is not defined in the AMBER parameter/topology file.")
                            continue

                        chain_id = atomSelection[0]['chain_id']
                        seq_id = atomSelection[0]['seq_id']
                        comp_id = atomSelection[0]['comp_id']
                        atom_id = atomSelection[0].get('atom_id', None)
                        if atom_id is None:
                            atom_id = atomSelection[0]['atom_id'] = atomSelection[0]['auth_atom_id']

                        self.atomSelectionSet.append(atomSelection)

                        if atom_id[0] not in protonBeginCode:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"
                                            f"({chain_id}:{seq_id}:{comp_id}:{atom_id} (derived from jhp) is not a proton.")
                            continue

                        dstFunc = self.validateNoexpRange(imix, ipeak, awt, arange)

                        if self.__createSfDict:
                            sf = self.__getSf()
                            sf['id'] += 1

                        updatePolySeqRstFromAtomSelectionSet(self.__polySeqRst, self.atomSelectionSet)

                        if any(len(atomSelection) == 0 for atomSelection in self.atomSelectionSet):
                            continue

                        for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                              self.atomSelectionSet[1]):
                            if isIdenticalRestraint([atom1, atom2]):
                                continue
                            if self.__debug:
                                print(f"subtype={self.__cur_subtype} dataset={imix} mixing_time={mix} peak={ipeak} "
                                      f"atom1={atom1} atom2={atom2} {dstFunc}")
                            if self.__createSfDict and sf is not None:
                                sf['index_id'] += 1
                                row = getRow(self.__cur_subtype, sf['id'], sf['index_id'],
                                             '.', None, None,
                                             sf['list_id'], self.__entryId, dstFunc,
                                             self.__authToStarSeq, self.__authToInsCode, self.__offsetHolder,
                                             atom1, atom2)
                                sf['loop'].add_data(row)

                    elif self.__hasPolySeq:
                        self.__f.append(f"[Missing data] {self.__getCurrentRestraint()}"
                                        "Failed to recognize AMBER atom numbers in the NOESY volume restraint file "
                                        "because AMBER parameter/topology file is not available.")
                        return

        finally:
            if self.__createSfDict:
                self.__trimSfWoLp()

    def validateNoexpRange(self, imix, ipeak, awt, arange):
        """ Validate NOESY peak volume range.
        """

        aexp = self.aexp[imix][ipeak]

        dstFunc = {'weight': awt, 'tolerance': arange}

        dstFunc['target_value'] = f"{aexp}"

        return dstFunc

    # Enter a parse tree produced by AmberMRParser#noeexp_factor.
    def enterNoeexp_factor(self, ctx: AmberMRParser.Noeexp_factorContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#noeexp_factor.
    def exitNoeexp_factor(self, ctx: AmberMRParser.Noeexp_factorContext):
        if ctx.IHP():
            varName = 'ihp'

            if ctx.Decimal(0) and ctx.Decimal(1):
                imix = int(str(ctx.Decimal(0)))
                ipeak = int(str(ctx.Decimal(1)))
                if imix in self.npeak and ipeak > self.npeak[imix]:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"
                                    f"The second argument value of '{varName}({imix},{ipeak})' must be in the range 1-{self.npeak[imix]}, "
                                    f"regulated by 'npeak({imix})={self.npeak[imix]}'.")
                    return
                if imix not in self.ihp:
                    self.ihp[imix] = {}
                self.ihp[imix][ipeak] = int(str(ctx.Integer()))

        elif ctx.JHP():
            varName = 'jhp'

            if ctx.Decimal(0) and ctx.Decimal(1):
                imix = int(str(ctx.Decimal(0)))
                ipeak = int(str(ctx.Decimal(1)))
                if imix in self.npeak and ipeak > self.npeak[imix]:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"
                                    f"The second argument value of '{varName}({imix},{ipeak})' must be in the range 1-{self.npeak[imix]}, "
                                    f"regulated by 'npeak({imix})={self.npeak[imix]}'.")
                    return
                if imix not in self.jhp:
                    self.jhp[imix] = {}
                self.jhp[imix][ipeak] = int(str(ctx.Integer()))

        elif ctx.AEXP():
            varName = 'aexp'

            if ctx.Decimal(0) and ctx.Decimal(1):
                imix = int(str(ctx.Decimal(0)))
                ipeak = int(str(ctx.Decimal(1)))
                if imix in self.npeak and ipeak > self.npeak[imix]:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"
                                    f"The second argument value of '{varName}({imix},{ipeak})' must be in the range 1-{self.npeak[imix]}, "
                                    f"regulated by 'npeak({imix})={self.npeak[imix]}'.")
                    return
                if imix not in self.aexp:
                    self.aexp[imix] = {}
                self.aexp[imix][ipeak] = float(str(ctx.Real()))

        elif ctx.ARANGE():
            varName = 'arange'

            if ctx.Decimal(0) and ctx.Decimal(1):
                imix = int(str(ctx.Decimal(0)))
                ipeak = int(str(ctx.Decimal(1)))
                if imix in self.npeak and ipeak > self.npeak[imix]:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"
                                    f"The second argument value of '{varName}({imix},{ipeak})' must be in the range 1-{self.npeak[imix]}, "
                                    f"regulated by 'npeak({imix})={self.npeak[imix]}'.")
                    return
                if imix not in self.arange:
                    self.arange[imix] = {}
                val = float(str(ctx.Real()))
                if val < 0.0:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"
                                    f"The uncertainty of peak volume '{varName}({imix},{ipeak})={val}' must not be a negative value.")
                    return
                self.arange[imix][ipeak] = val

        elif ctx.AWT():
            varName = 'awt'

            if ctx.Decimal(0) and ctx.Decimal(1):
                imix = int(str(ctx.Decimal(0)))
                ipeak = int(str(ctx.Decimal(1)))
                if imix in self.npeak and ipeak > self.npeak[imix]:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"
                                    f"The second argument value of '{varName}({imix},{ipeak})' must be in the range 1-{self.npeak[imix]}, "
                                    f"regulated by 'npeak({imix})={self.npeak[imix]}'.")
                    return
                if imix not in self.awt:
                    self.awt[imix] = {}
                val = float(str(ctx.Real()))
                if val <= 0.0:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(imix,ipeak)}"
                                    f"The relative weight value '{varName}({imix},{ipeak})={val}' must not be a negative value.")
                    return
                self.awt[imix][ipeak] = val

        elif ctx.NPEAK():
            varName = 'npeak'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal(0)))
                rawIntArray = str(ctx.Integers()).split(',')
                val = int(rawIntArray[0])
                if len(rawIntArray) > 1:
                    self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                    f"The '{varName}({decimal})={str(ctx.Integers())}' can not be an array of integers, "
                                    f"hence the first value '{varName}({decimal})={val}' will be evaluated as a valid value.")
                if val > 0:
                    self.npeak[decimal] = val

            else:
                if ctx.Integers():
                    rawIntArray = str(ctx.Integers()).split(',')
                    for col, rawInt in enumerate(rawIntArray, start=1):
                        val = int(rawInt)
                        if val <= 0:
                            break
                        self.npeak[col] = val
                elif ctx.MultiplicativeInt():
                    offset = 1
                    for multiplicativeInt in str(ctx.MultiplicativeInt()).split(','):
                        rawMultInt = multiplicativeInt.split('*')
                        numNpeakCol = int(rawMultInt[0])
                        val = int(rawMultInt[1])
                        for col in range(0, numNpeakCol):
                            if val <= 0:
                                break
                            self.npeak[offset + col] = val
                        offset += numNpeakCol

        elif ctx.EMIX():
            varName = 'emix'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal(0)))
                rawRealArray = str(ctx.Reals()).split(',')
                val = float(rawRealArray[0])
                if len(rawRealArray) > 1:
                    self.__f.append(f"[Redundant data] {self.__getCurrentRestraint()}"
                                    f"The '{varName}({decimal})={str(ctx.Reals())}' can not be an array of reals, "
                                    f"hence the first value '{varName}({decimal})={val}' will be evaluated as a valid value.")
                if val <= 0.0:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                    f"The mixing time '{varName}({decimal})={val}' must be a positive value.")
                    return
                self.emix[decimal] = val

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        val = float(rawReal)
                        if val <= 0.0:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The mixing time '{varName}({col})={val}' must be a positive value.")
                            break
                        self.emix[col] = val
                elif ctx.MultiplicativeReal():
                    offset = 1
                    for multiplicativeReal in str(ctx.MultiplicativeReal()).split(','):
                        rawMultReal = multiplicativeReal.split('*')
                        numEmixCol = int(rawMultReal[0])
                        val = float(rawMultReal[1])
                        for col in range(0, numEmixCol):
                            if val <= 0.0:
                                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                                f"The mixing time '{varName}({col})={val}' must be a positive value.")
                                break
                            self.emix[offset + col] = val
                            offset += numEmixCol

        elif ctx.INVWT1():
            self.invwt1 = float(str(ctx.Real()))

        elif ctx.INVWT2():
            self.invwt2 = float(str(ctx.Real()))

        elif ctx.OMEGA():
            self.omega = float(str(ctx.Real()))

        elif ctx.TAUROT():
            self.taurot = float(str(ctx.Real()))

        elif ctx.TAUMET():
            self.taumet = float(str(ctx.Real()))

        elif ctx.ID2O():
            self.id2o = int(str(ctx.BoolInt()))

    # Enter a parse tree produced by AmberMRParser#shf_statement.
    def enterShf_statement(self, ctx: AmberMRParser.Shf_statementContext):  # pylint: disable=unused-argument
        self.procsRestraints += 1
        self.__cur_subtype = 'procs'

        self.iprot = {}
        self.obs = {}
        self.wt = {}
        self.nprot = -1

        self.shrang = {}
        self.iatr = {}
        self.natr = {}
        self.namr = {}
        self._str = {}
        self.nring = -1
        self.nter = 1
        self.cter = -1

        if self.__createSfDict:
            self.__addSf()

    # Exit a parse tree produced by AmberMRParser#shf_statement.
    def exitShf_statement(self, ctx: AmberMRParser.Shf_statementContext):  # pylint: disable=unused-argument
        try:

            if self.nprot < 0 and len(self.iprot) > 0:  # pylint: disable=chained-comparison
                self.nprot = max(self.iprot.keys())

            if self.nprot <= 0:
                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                "The number of observed chemical shifts 'nprot' is the mandatory variable.")
                return

            for n in range(1, self.nprot + 1):

                if n not in self.iprot:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(n=n)}"
                                    f"The atom number involved in the chemical shifts nprot({n}) was not set.")
                    continue

                if n not in self.obs:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(n=n)}"
                                    f"The observed chemical shift value obs({n}) was not set.")
                    continue

                _iprot = self.iprot[n]

                if _iprot <= 0:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(n=n)}"
                                    f"The atom number involved in the chemical shift 'iprot({n})={_iprot}' should be a positive integer.")
                    continue

                wt = 1.0
                if n in self.wt:
                    wt = self.wt[n]
                    if wt <= 0.0:
                        wt = 1.0

                shrang = 0.0
                if n in self.shrang:
                    shrang = max(self.shrang[n], 0.0)

                # convert AMBER atom numbers to corresponding coordinate atoms based on AMBER parameter/topology file
                if self.__atomNumberDict is not None:

                    self.atomSelectionSet.clear()

                    atomSelection = []

                    if _iprot in self.__atomNumberDict:
                        atomSelection.append(copy.copy(self.__atomNumberDict[_iprot]))
                    else:
                        self.__f.append(f"[Missing data] {self.__getCurrentRestraint(n=n)}"
                                        f"'iprot({n})={_iprot}' is not defined in the AMBER parameter/topology file.")
                        continue

                    chain_id = atomSelection[0]['chain_id']
                    seq_id = atomSelection[0]['seq_id']
                    comp_id = atomSelection[0]['comp_id']
                    atom_id = atomSelection[0].get('atom_id', None)
                    if atom_id is None:
                        atom_id = atomSelection[0]['atom_id'] = atomSelection[0]['auth_atom_id']

                    self.atomSelectionSet.append(atomSelection)

                    if atom_id[0] not in protonBeginCode:
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(n=n)}"
                                        f"({chain_id}:{seq_id}:{comp_id}:{atom_id} is not a proton.")
                        continue

                    dstFunc = self.validateShfRange(n, wt, shrang)

                    if dstFunc is None:
                        return

                    if self.__createSfDict:
                        sf = self.__getSf()
                        sf['id'] += 1

                    for atom in self.atomSelectionSet[0]:
                        if self.__debug:
                            print(f"subtype={self.__cur_subtype} n={n} "
                                  f"atom={atom} {dstFunc}")
                        if self.__createSfDict and sf is not None:
                            sf['index_id'] += 1
                            row = getRow(self.__cur_subtype, sf['id'], sf['index_id'],
                                         '.', None, None,
                                         sf['list_id'], self.__entryId, dstFunc,
                                         self.__authToStarSeq, self.__authToInsCode, self.__offsetHolder,
                                         atom)
                            sf['loop'].add_data(row)

                elif self.__hasPolySeq:
                    self.__f.append(f"[Missing data] {self.__getCurrentRestraint()}"
                                    "Failed to recognize AMBER atom numbers in the chemical shift restraint file "
                                    "because AMBER parameter/topology file is not available.")
                    return

            if self.nring <= 0:
                return

            for r in range(1, self.nring + 1):

                if r not in self.natr:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                    f"The number of atoms in a ring 'natr({r})' was not set.")
                    continue

                for n in range(1, self.natr[r] + 1):

                    if n not in self.iatr[r]:
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                        f"The ring atom 'iatr({n},{r})' was not set.")
                        continue

                    _iat = self.iatr[r][n]

                    if _iat <= 0:
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(n)}"
                                        f"The atom number involved in the ring 'iatr({n},{r})={_iat}' should be a positive integer.")
                        continue

                    # convert AMBER atom numbers to corresponding coordinate atoms based on AMBER parameter/topology file
                    if self.__atomNumberDict is not None:

                        self.atomSelectionSet.clear()

                        atomSelection = []

                        if _iat in self.__atomNumberDict:
                            atomSelection.append(copy.copy(self.__atomNumberDict[_iat]))
                        else:
                            self.__f.append(f"[Missing data] {self.__getCurrentRestraint()}"
                                            f"The ring atom 'iatr({n},{r})={_iat}' is not defined in the AMBER parameter/topology file.")
                            continue

                        chain_id = atomSelection[0]['chain_id']
                        seq_id = atomSelection[0]['seq_id']
                        comp_id = atomSelection[0]['comp_id']
                        atom_id = atomSelection[0].get('atom_id', None)
                        if atom_id is None:
                            atom_id = atomSelection[0]['atom_id'] = atomSelection[0]['auth_atom_id']

                        self.atomSelectionSet.append(atomSelection)

                        updatePolySeqRstFromAtomSelectionSet(self.__polySeqRst, self.atomSelectionSet)

                        if any(len(atomSelection) == 0 for atomSelection in self.atomSelectionSet):
                            continue

                        for atom in self.atomSelectionSet[0]:
                            if self.__debug:
                                print(f"subtype={self.__cur_subtype} iatr({n},{r}) "
                                      f"ring_atom={atom}")

                    elif self.__hasPolySeq:
                        self.__f.append(f"[Missing data] {self.__getCurrentRestraint()}"
                                        "Failed to recognize AMBER atom numbers in the chemical shift restraint file "
                                        "because AMBER parameter/topology file is not available.")
                        return

        finally:
            if self.__createSfDict:
                self.__trimSfWoLp()

    def validateShfRange(self, n, wt, shrang):
        """ Validate chemical shift value range.
        """

        obs = self.obs[n]

        validRange = True
        dstFunc = {'weight': wt, 'tolerance': shrang}

        if obs is not None:
            if CS_ERROR_MIN < obs < CS_ERROR_MAX:
                dstFunc['target_value'] = f"{obs}"
            else:
                validRange = False
                self.__f.append(f"[Range value error] {self.__getCurrentRestraint(n=n)}"
                                f"The target value 'obs({n})={obs}' must be within range {CS_RESTRAINT_ERROR}.")

        if not validRange:
            self.lastComment = None
            return None

        if obs is not None:
            if CS_RANGE_MIN <= obs <= CS_RANGE_MAX:
                pass
            else:
                self.__f.append(f"[Range value warning] {self.__getCurrentRestraint(n=n)}"
                                f"The target value 'obs({n})={obs}' should be within range {CS_RESTRAINT_RANGE}.")

        return dstFunc

    # Enter a parse tree produced by AmberMRParser#shf_factor.
    def enterShf_factor(self, ctx: AmberMRParser.Shf_factorContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#shf_factor.
    def exitShf_factor(self, ctx: AmberMRParser.Shf_factorContext):
        if ctx.IPROT():
            varName = 'iprot'

            if ctx.Decimal(0):
                decimal = int(str(ctx.Decimal(0)))
                if self.nprot > 0 and decimal > self.nprot:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(n=decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nprot}, "
                                    f"regulated by 'nprot={self.nprot}'.")
                    return
                self.iprot[decimal] = int(str(ctx.Integer()))

        elif ctx.OBS():
            varName = 'obs'

            if ctx.Decimal(0):
                decimal = int(str(ctx.Decimal(0)))
                if self.nprot > 0 and decimal > self.nprot:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(n=decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nprot}, "
                                    f"regulated by 'nprot={self.nprot}'.")
                    return
                self.obs[decimal] = float(str(ctx.Real()))

        elif ctx.SHRANG():
            varName = 'shrang'

            if ctx.Decimal(0):
                decimal = int(str(ctx.Decimal(0)))
                if self.nprot > 0 and decimal > self.nprot:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(n=decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nprot}, "
                                    f"regulated by 'nprot={self.nprot}'.")
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                val = float(rawRealArray[0])
                if val < 0.0:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(n=decimal)}"
                                    f"The uncertainty of observed shift '{varName}({decimal})={val}' must not be a negative value.")
                    return
                self.shrang[decimal] = val

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.nprot:
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                        f"The length of '{varName}={ctx.Reals()}' must not exceed 'nprot={self.nprot}'.")
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        val = float(rawReal)
                        if val < 0.0:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The uncertainty of observed shift '{varName}({col})={val}' must not be a negative.")
                            return
                        self.shrang[col] = val
                elif ctx.MultiplicativeReal():
                    offset = 0
                    for multiplicativeReal in str(ctx.MultiplicativeReal()).split(','):
                        rawMultReal = multiplicativeReal.split('*')
                        numCol = int(rawMultReal[0])
                        if offset + numCol <= 0 or offset + numCol > self.nprot:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The argument value of '{varName}({numCol})' derived from "
                                            f"'{str(ctx.MultiplicativeReal())}' must be in the range 1-{self.nprot}, "
                                            f"regulated by 'nprot={self.nprot}'.")
                            return
                        val = float(rawMultReal[1])
                        if val < 0.0:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The uncertainty of observed shift '{varName}={val}' derived from "
                                            f"'{str(ctx.MultiplicativeReal())}' must not be a negative.")
                            return
                        for col in range(0, numCol):
                            self.shrang[offset + col + 1] = val
                        offset += numCol

        elif ctx.WT():
            varName = 'wt'

            if ctx.Decimal(0):
                decimal = int(str(ctx.Decimal(0)))
                if self.nprot > 0 and decimal > self.nprot:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(n=decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nprot}, "
                                    f"regulated by 'nprot={self.nprot}'.")
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                val = float(rawRealArray[0])
                if val < 0.0:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(n=decimal)}"
                                    f"The relative weight value '{varName}({decimal})={val}' must not be a negative value.")
                    return
                if val == 0.0:
                    self.__f.append(f"[Range value warning] {self.__getCurrentRestraint(n=decimal)}"
                                    f"The relative weight value '{varName}({decimal})={val}' should be a positive value.")
                self.wt[decimal] = val

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.nprot:
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                        f"The length of '{varName}={ctx.Reals()}' must not exceed 'nprot={self.nprot}'.")
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        val = float(rawReal)
                        if val < 0.0:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The relative weight value '{varName}({col})={val}' must not be a negative value.")
                            return
                        if val == 0.0:
                            self.__f.append(f"[Range value warning] {self.__getCurrentRestraint()}"
                                            f"The relative weight value '{varName}({col})={val}' should be a positive value.")
                        self.wt[col] = val
                elif ctx.MultiplicativeReal():
                    offset = 0
                    for multiplicativeReal in str(ctx.MultiplicativeReal()).split(','):
                        rawMultReal = multiplicativeReal.split('*')
                        numCol = int(rawMultReal[0])
                        if offset + numCol <= 0 or offset + numCol > self.nprot:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The argument value of '{varName}({numCol})' derived from "
                                            f"'{str(ctx.MultiplicativeReal())}' must be in the range 1-{self.nprot}, "
                                            f"regulated by 'nprot={self.nprot}'.")
                            return
                        val = float(rawMultReal[1])
                        if val < 0.0:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The relative weight value '{varName}={val}' derived from "
                                            f"'{str(ctx.MultiplicativeReal())}' must not be a negative value.")
                            return
                        if val == 0.0:
                            self.__f.append(f"[Range value warning] {self.__getCurrentRestraint()}"
                                            f"The relative weight value '{varName}={val}' derived from "
                                            f"'{str(ctx.MultiplicativeReal())}' should be a positive value.")
                        for col in range(0, numCol):
                            self.wt[offset + col + 1] = val
                        offset += numCol

        elif ctx.NPROT():
            self.nprot = int(str(ctx.Integer()))
            if self.nprot <= 0:
                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                f"The number of protons 'nprot={self.nprot}' must be a positive integer.")
                return

        elif ctx.IATR():
            varName = 'iatr'

            if ctx.Decimal(0) and ctx.Decimal(1):
                j = int(str(ctx.Decimal(0)))
                ring = int(str(ctx.Decimal(1)))
                if self.nring > 0 and ring > self.nring:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(n=decimal)}"
                                    f"The second argument value of '{varName}({j},{ring})' must be in the range 1-{self.nring}, "
                                    f"regulated by 'nring={self.nring}'.")
                    return
                if ring in self.natr and j > self.natr[ring]:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(n=decimal)}"
                                    f"The first argument value of '{varName}({j},{ring})' must be in the range 1-{self.natr[ring]}, "
                                    f"regulated by 'natr({ring})={self.natr[ring]}'.")
                    return
                self.iatr[ring][j] = int(str(ctx.Integer()))

        elif ctx.NATR():
            varName = 'natr'

            if ctx.Decimal(0):
                decimal = int(str(ctx.Decimal(0)))
                if self.nring > 0 and decimal > self.nring:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(n=decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nring}, "
                                    f"regulated by 'nring={self.nring}'.")
                    return
                val = int(str(ctx.Integer()))
                if val < 0:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                    f"The number of atoms in a ring '{varName}({decimal})={val}' must not be a negative integer.")
                    return
                self.natr[decimal] = val
                self.iatr[decimal] = {}

        elif ctx.STR():
            varName = 'str'

            if ctx.Decimal(0):
                decimal = int(str(ctx.Decimal(0)))
                if self.nring > 0 and decimal > self.nring:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(n=decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nring}, "
                                    f"regulated by 'nring={self.nring}'.")
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                val = float(rawRealArray[0])
                if val <= 0.0:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(n=decimal)}"
                                    f"The relative strength value '{varName}({decimal})={val}' must be a positive value.")
                    return
                self._str[decimal] = val

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.nring:
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                        f"The length of '{varName}={ctx.Reals()}' must not exceed 'nring={self.nring}'.")
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        val = float(rawReal)
                        if val <= 0.0:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The relative strength value '{varName}({col})={val}' must be a positive value.")
                            return
                        self._str[col] = val
                elif ctx.MultiplicativeReal():
                    offset = 0
                    for multiplicativeReal in str(ctx.MultiplicativeReal()).split(','):
                        rawMultReal = multiplicativeReal.split('*')
                        numCol = int(rawMultReal[0])
                        if offset + numCol <= 0 or offset + numCol > self.nring:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The argument value of '{varName}({numCol})' derived from "
                                            f"'{str(ctx.MultiplicativeReal())}' must be in the range 1-{self.nring}, "
                                            f"regulated by 'nring={self.nring}'.")
                            return
                        val = float(rawMultReal[1])
                        if val <= 0.0:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The relative strength value '{varName}={val}' derived from "
                                            f"'{str(ctx.MultiplicativeReal())}' must be a positive value.")
                            return
                        for col in range(0, numCol):
                            self._str[offset + col + 1] = val
                        offset += numCol

        elif ctx.NRING():
            self.nring = int(str(ctx.Integer()))
            if self.nring < 0:
                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                f"The number of rings 'nring={self.nring}' must not be a negative integer.")
                return

        elif ctx.NTER():
            self.nter = int(str(ctx.Integer()))
            if self.cter is not None and self.nter >= self.cter:
                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                f"The residue number of N-terminus 'nter={self.nter}' must be less than 'cter={self.cter}'.")
                return

        elif ctx.CTER():
            self.cter = int(str(ctx.Integer()))
            if self.nter >= self.cter:
                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                f"The residue number of C-terminus 'cter={self.cter}' must be greater than 'nter={self.nter}'.")
                return

        elif ctx.NAMR():
            varName = 'namr'

            if ctx.Decimal(0):
                decimal = int(str(ctx.Decimal(0)))
                if self.nring > 0 and decimal > self.nring:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(n=decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nring}, "
                                    f"regulated by 'nring={self.nring}'.")
                    return
                self.namr[decimal] = str(ctx.Qstring()).strip()

    # Enter a parse tree produced by AmberMRParser#pcshf_statement.
    def enterPcshf_statement(self, ctx: AmberMRParser.Pcshf_statementContext):  # pylint: disable=unused-argument
        self.pcsRestraints += 1
        self.__cur_subtype = 'pcs'

        self.iprot = {}
        self.obs = {}
        self.wt = {}
        self.tolpro = {}
        self.mltpro = {}
        self.nprot = -1
        self.nmpmc = 'undefined'
        self.optphi = {}
        self.opttet = {}
        self.optomg = {}
        self.opta1 = {}
        self.opta2 = {}
        self.optkon = 0.0
        self.nme = -1

    # Exit a parse tree produced by AmberMRParser#pcshf_statement.
    def exitPcshf_statement(self, ctx: AmberMRParser.Pcshf_statementContext):  # pylint: disable=unused-argument
        if self.nprot < 0 and len(self.iprot) > 0:  # pylint: disable=chained-comparison
            self.nprot = max(self.iprot.keys())

        if self.nprot <= 0:
            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                            "The number of observed PCS values 'nprot' is the mandatory variable.")
            return

        if self.nme < 0 and len(self.optphi) > 0:  # pylint: disable=chained-comparison
            self.nme = max(self.optphi.keys())
        """
        if self.nme <= 0:
            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                            "The number of paramagnetic centers 'nme' is the mandatory variable.")
            return
        """
        for n in range(1, self.nprot + 1):

            if n not in self.iprot:
                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,n)}"
                                f"The atom number involved in the PCS nprot({n}) was not set.")
                continue

            if n not in self.obs:
                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,n)}"
                                f"The observed PCS value obs({n}) was not set.")
                continue

            _iprot = self.iprot[n]

            if _iprot <= 0:
                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,n)}"
                                f"The atom number involved in the PCS 'iprot({n})={_iprot}' should be a positive integer.")
                continue

            wt = 1.0
            if n in self.wt:
                wt = self.wt[n]
                if wt <= 0.0:
                    wt = 1.0

            tolpro = 1.0
            if n in self.tolpro:
                tolpro = self.tolpro[n]
                if tolpro <= 0.0:
                    tolpro = 1.0

            mltpro = 1
            if n in self.mltpro:
                mltpro = self.mltpro[n]
                if mltpro <= 0:
                    mltpro = 1

            # convert AMBER atom numbers to corresponding coordinate atoms based on AMBER parameter/topology file
            if self.__atomNumberDict is not None:

                self.atomSelectionSet.clear()

                atomSelection = []

                if _iprot in self.__atomNumberDict:
                    atomSelection.append(copy.copy(self.__atomNumberDict[_iprot]))
                else:
                    self.__f.append(f"[Missing data] {self.__getCurrentRestraint(self.nmpmc,n)}"
                                    f"'iprot({n})={_iprot}' is not defined in the AMBER parameter/topology file.")
                    continue

                chain_id = atomSelection[0]['chain_id']
                seq_id = atomSelection[0]['seq_id']
                comp_id = atomSelection[0]['comp_id']
                atom_id = atomSelection[0].get('atom_id', None)
                if atom_id is None:
                    atom_id = atomSelection[0]['atom_id'] = atomSelection[0]['auth_atom_id']

                self.atomSelectionSet.append(atomSelection)

                if atom_id[0] not in protonBeginCode:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,n)}"
                                    f"({chain_id}:{seq_id}:{comp_id}:{atom_id} is not a proton.")
                    continue

                dstFunc = self.validatePcsRange(n, wt, tolpro, mltpro)

                if dstFunc is None:
                    return

                if self.__createSfDict:
                    sf = self.__getSf()
                    sf['id'] += 1

                updatePolySeqRstFromAtomSelectionSet(self.__polySeqRst, self.atomSelectionSet)

                if any(len(atomSelection) == 0 for atomSelection in self.atomSelectionSet):
                    continue

                for atom in self.atomSelectionSet[0]:
                    if self.__debug:
                        print(f"subtype={self.__cur_subtype} dataset={self.nmpmc} n={n} "
                              f"atom={atom} {dstFunc}")
                    if self.__createSfDict and sf is not None:
                        sf['index_id'] += 1
                        row = getRow(self.__cur_subtype, sf['id'], sf['index_id'],
                                     '.', None, None,
                                     sf['list_id'], self.__entryId, dstFunc,
                                     self.__authToStarSeq, self.__authToInsCode, self.__offsetHolder,
                                     atom)
                        sf['loop'].add_data(row)

            elif self.__hasPolySeq:
                self.__f.append(f"[Missing data] {self.__getCurrentRestraint()}"
                                "Failed to recognize AMBER atom numbers in the Psuedocontact shift restraint file "
                                "because AMBER parameter/topology file is not available.")
                return

    # Enter a parse tree produced by AmberMRParser#pcshf_factor.
    def enterPcshf_factor(self, ctx: AmberMRParser.Pcshf_factorContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#pcshf_factor.
    def exitPcshf_factor(self, ctx: AmberMRParser.Pcshf_factorContext):
        if ctx.IPROT():
            varName = 'iprot'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.nprot > 0 and decimal > self.nprot:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nprot}, "
                                    f"regulated by 'nprot={self.nprot}'.")
                    return
                self.iprot[decimal] = int(str(ctx.Integer()))

        elif ctx.OBS():
            varName = 'obs'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.nprot > 0 and decimal > self.nprot:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nprot}, "
                                    f"regulated by 'nprot={self.nprot}'.")
                    return
                self.obs[decimal] = float(str(ctx.Real()))

        elif ctx.WT():
            varName = 'wt'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.nprot > 0 and decimal > self.nprot:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nprot}, "
                                    f"regulated by 'nprot={self.nprot}'.")
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                val = float(rawRealArray[0])
                if val < 0.0:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,decimal)}"
                                    f"The relative weight value '{varName}({decimal})={val}' must not be a negative value.")
                    return
                if val == 0.0:
                    self.__f.append(f"[Range value warning] {self.__getCurrentRestraint(self.nmpmc,decimal)}"
                                    f"The relative weight value '{varName}({decimal})={val}' should be a positive value.")
                self.wt[decimal] = val

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.nprot:
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                        f"The length of '{varName}={ctx.Reals()}' must not exceed 'nprot={self.nprot}'.")
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        val = float(rawReal)
                        if val < 0.0:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The relative weight value '{varName}({col})={val}' must not be a negative value.")
                            return
                        if val == 0.0:
                            self.__f.append(f"[Range value warning] {self.__getCurrentRestraint()}"
                                            f"The relative weight value '{varName}({col})={val}' should be a positive value.")
                        self.wt[col] = val
                elif ctx.MultiplicativeReal():
                    offset = 0
                    for multiplicativeReal in str(ctx.MultiplicativeReal()).split(','):
                        rawMultReal = multiplicativeReal.split('*')
                        numCol = int(rawMultReal[0])
                        if offset + numCol <= 0 or offset + numCol > self.nprot:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The argument value of '{varName}({numCol})' derived from "
                                            f"'{str(ctx.MultiplicativeReal())}' must be in the range 1-{self.nprot}, "
                                            f"regulated by 'nprot={self.nprot}'.")
                            return
                        val = float(rawMultReal[1])
                        if val < 0.0:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The relative weight value '{varName}={val}' derived from "
                                            f"'{str(ctx.MultiplicativeReal())}' must not be a negative value.")
                            return
                        if val == 0.0:
                            self.__f.append(f"[Range value warning] {self.__getCurrentRestraint()}"
                                            f"The relative weight value '{varName}={val}' derived from "
                                            f"'{str(ctx.MultiplicativeReal())}' should be a positive value.")
                        for col in range(0, numCol):
                            self.wt[offset + col + 1] = val
                        offset += numCol

        elif ctx.TOLPRO():
            varName = 'tolpro'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.nprot > 0 and decimal > self.nprot:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nprot}, "
                                    f"regulated by 'nprot={self.nprot}'.")
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                val = float(rawRealArray[0])
                if val <= 0.0:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,decimal)}"
                                    f"The relative tolerance value '{varName}({decimal})={val}' must be a positive value.")
                    return
                self.tolpro[decimal] = val

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.nprot:
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                        f"The length of '{varName}={ctx.Reals()}' must not exceed 'nprot={self.nprot}'.")
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        val = float(rawReal)
                        if val <= 0.0:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The relative tolerance value '{varName}({col})={val}' must be a positive value.")
                            return
                        self.tolpro[col] = val
                elif ctx.MultiplicativeReal():
                    offset = 0
                    for multiplicativeReal in str(ctx.MultiplicativeReal()).split(','):
                        rawMultReal = multiplicativeReal.split('*')
                        numCol = int(rawMultReal[0])
                        if offset + numCol <= 0 or offset + numCol > self.nprot:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The argument value of '{varName}({numCol})' derived from "
                                            f"'{str(ctx.MultiplicativeReal())}' must be in the range 1-{self.nprot}, "
                                            f"regulated by 'nprot={self.nprot}'.")
                            return
                        val = float(rawMultReal[1])
                        if val <= 0.0:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The relative tolerance value '{varName}={val}' derived from "
                                            f"'{str(ctx.MultiplicativeReal())}' must be a positive value.")
                            return
                        for col in range(0, numCol):
                            self.tolpro[offset + col + 1] = val
                        offset += numCol

        elif ctx.MLTPRO():
            varName = 'mltpro'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.nprot > 0 and decimal > self.nprot:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nprot}, "
                                    f"regulated by 'nprot={self.nprot}'.")
                    return
                val = int(str(ctx.Integer()))
                if val <= 0:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,decimal)}"
                                    f"The multiplicity of NMR signal of '{varName}({decimal})={val}' must be a positive integer.")
                    return
                self.mltpro[decimal] = val

        elif ctx.NPROT():
            self.nprot = int(str(ctx.Integer()))
            if self.nprot <= 0:
                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                f"The number of protons 'nprot={self.nprot}' must be a positive integer.")
                return

        elif ctx.OPTPHI():
            varName = 'optphi'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.nme > 0 and decimal > self.nme:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nme}, "
                                    f"regulated by 'nme={self.nme}'.")
                    return
                self.optphi[decimal] = float(str(ctx.Real()))

        elif ctx.OPTTET():
            varName = 'opttet'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.nme > 0 and decimal > self.nme:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nme}, "
                                    f"regulated by 'nme={self.nme}'.")
                    return
                self.opttet[decimal] = float(str(ctx.Real()))

        elif ctx.OPTOMG():
            varName = 'optomg'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.nme > 0 and decimal > self.nme:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nme}, "
                                    f"regulated by 'nme={self.nme}'.")
                    return
                self.optomg[decimal] = float(str(ctx.Real()))

        elif ctx.OPTA1():
            varName = 'opta1'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.nme > 0 and decimal > self.nme:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nme}, "
                                    f"regulated by 'nme={self.nme}'.")
                    return
                self.opta1[decimal] = float(str(ctx.Real()))

        elif ctx.OPTA2():
            varName = 'opta2'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.nme > 0 and decimal > self.nme:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.nmpmc,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.nme}, "
                                    f"regulated by 'nme={self.nme}'.")
                    return
                self.opta2[decimal] = float(str(ctx.Real()))

        elif ctx.OPTKON():
            self.optkon = float(str(ctx.Real()))

        elif ctx.NME():
            self.nme = int(str(ctx.Integer()))
            if self.nme <= 0:
                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                f"The number of paramagnetic centers 'nme={self.nme}' must be a positive integer.")
                return

        elif ctx.NMPMC():
            self.nmpmc = str(ctx.Qstring()).strip()

    # Enter a parse tree produced by AmberMRParser#align_statement.
    def enterAlign_statement(self, ctx: AmberMRParser.Align_statementContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1
        self.__cur_subtype = 'rdc'

        self.id = {}
        self.jd = {}
        self.dobsl = {}
        self.dobsu = {}
        self.dwt = {}
        self.gigj = {}
        self.dij = {}
        self.ndip = -1
        self.dataset = 1
        self.numDatasets = 1
        self.s11 = {}
        self.s12 = {}
        self.s13 = {}
        self.s22 = {}
        self.s23 = {}

        if self.__createSfDict:
            self.__addSf()

    # Exit a parse tree produced by AmberMRParser#align_statement.
    def exitAlign_statement(self, ctx: AmberMRParser.Align_statementContext):  # pylint: disable=unused-argument
        try:

            if self.ndip < 0 and len(self.id) > 0:  # pylint: disable=chained-comparison
                self.ndip = max(self.id.keys())

            if self.ndip <= 0:
                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                "The number of observed dipolar couplings 'ndip' is the mandatory variable.")
                return

            for n in range(1, self.ndip + 1):

                if n not in self.id:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.dataset,n)}"
                                    f"The first atom number involved in the dipolar coupling id({n}) was not set.")
                    continue

                if n not in self.jd:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.dataset,n)}"
                                    f"The second atom number involved in the dipolar coupling jd({n}) was not set.")
                    continue

                if n not in self.dobsl:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.dataset,n)}"
                                    f"The lower limit value for the observed dipolar coupling dobsl({n}) was not set.")
                    continue

                if n not in self.dobsu:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.dataset,n)}"
                                    f"The upper limit value for the observed dipolar coupling dobsu({n}) was not set.")
                    continue

                _id = self.id[n]
                _jd = self.jd[n]

                if _id <= 0:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.dataset,n)}"
                                    f"The first atom number involved in the dipolar coupling 'id({n})={_id}' should be a positive integer.")
                    continue

                if _jd <= 0:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.dataset,n)}"
                                    f"The second atom number involved in the dipolar coupling 'jd({n})={_jd}' should be a positive integer.")
                    continue

                dwt = 1.0
                if n in self.dwt:
                    dwt = self.dwt[n]
                    if dwt <= 0.0:
                        dwt = 1.0

                # convert AMBER atom numbers to corresponding coordinate atoms based on AMBER parameter/topology file
                if self.__atomNumberDict is not None:

                    self.atomSelectionSet.clear()

                    atomSelection = []

                    if _id in self.__atomNumberDict:
                        atomSelection.append(copy.copy(self.__atomNumberDict[_id]))
                    else:
                        atom_id_i = None
                        if _jd in self.__atomNumberDict:
                            atom_sel_j = self.__atomNumberDict[_jd]
                            comp_id_j = atom_sel_j['comp_id']
                            atom_id_j = atom_sel_j['atom_id']
                            if self.__ccU.updateChemCompDict(comp_id_j):  # matches with comp_id in CCD
                                if atom_id_j[0] in protonBeginCode:
                                    b = next((b for b in self.__ccU.lastBonds
                                              if atom_id_j in (b[self.__ccU.ccbAtomId1], b[self.__ccU.ccbAtomId2])), None)
                                else:
                                    b = next((b for b in self.__ccU.lastBonds
                                              if (b[self.__ccU.ccbAtomId1] == atom_id_j and b[self.__ccU.ccbAtomId2][0] not in protonBeginCode)
                                              or (b[self.__ccU.ccbAtomId2] == atom_id_j and b[self.__ccU.ccbAtomId1][0] not in protonBeginCode)), None)
                                if b is not None:
                                    atom_id_i = b[self.__ccU.ccbAtomId1] if b[self.__ccU.ccbAtomId1] != atom_id_j else b[self.__ccU.ccbAtomId2]
                                    atom_sel_i = copy.copy(atom_sel_j)
                                    atom_sel_i['auth_atom_id'] = atom_sel_i['atom_id'] = atom_id_i
                                    self.__atomNumberDict[_id] = atom_sel_i
                                    atomSelection.append(atom_sel_i)
                        if atom_id_i is None:
                            self.__f.append(f"[Missing data] {self.__getCurrentRestraint(self.dataset,n)}"
                                            f"'id({n})={_id}' is not defined in the AMBER parameter/topology file.")
                            continue

                    chain_id_1 = atomSelection[0]['chain_id']
                    seq_id_1 = atomSelection[0]['seq_id']
                    comp_id_1 = atomSelection[0]['comp_id']
                    atom_id_1 = atomSelection[0].get('atom_id', None)
                    if atom_id_1 is None:
                        atom_id_1 = atomSelection[0]['atom_id'] = atomSelection[0]['auth_atom_id']

                    self.atomSelectionSet.append(atomSelection)

                    atomSelection = []

                    if _jd in self.__atomNumberDict:
                        atomSelection.append(copy.copy(self.__atomNumberDict[_jd]))
                    else:
                        atom_id_j = None
                        if _id in self.__atomNumberDict:
                            atom_sel_i = self.__atomNumberDict[_id]
                            comp_id_i = atom_sel_i['comp_id']
                            atom_id_i = atom_sel_i['atom_id']
                            if self.__ccU.updateChemCompDict(comp_id_i):  # matches with comp_id in CCD
                                if atom_id_i[0] in protonBeginCode:
                                    b = next((b for b in self.__ccU.lastBonds
                                              if atom_id_i in (b[self.__ccU.ccbAtomId1], b[self.__ccU.ccbAtomId2])), None)
                                else:
                                    b = next((b for b in self.__ccU.lastBonds
                                              if (b[self.__ccU.ccbAtomId1] == atom_id_i and b[self.__ccU.ccbAtomId2][0] not in protonBeginCode)
                                              or (b[self.__ccU.ccbAtomId2] == atom_id_i and b[self.__ccU.ccbAtomId1][0] not in protonBeginCode)), None)
                                if b is not None:
                                    atom_id_j = b[self.__ccU.ccbAtomId1] if b[self.__ccU.ccbAtomId1] != atom_id_i else b[self.__ccU.ccbAtomId2]
                                    atom_sel_j = copy.copy(atom_sel_i)
                                    atom_sel_j['auth_atom_id'] = atom_sel_j['atom_id'] = atom_id_j
                                    self.__atomNumberDict[_jd] = atom_sel_j
                                    atomSelection.append(atom_sel_j)
                        if atom_id_j is None:
                            self.__f.append(f"[Missing data] {self.__getCurrentRestraint(self.dataset,n)}"
                                            f"'jd({n})={_jd}' is not defined in the AMBER parameter/topology file.")
                            continue

                    chain_id_2 = atomSelection[0]['chain_id']
                    seq_id_2 = atomSelection[0]['seq_id']
                    comp_id_2 = atomSelection[0]['comp_id']
                    atom_id_2 = atomSelection[0].get('atom_id', None)
                    if atom_id_2 is None:
                        atom_id_2 = atomSelection[0]['atom_id'] = atomSelection[0]['auth_atom_id']

                    self.atomSelectionSet.append(atomSelection)

                    if (atom_id_1[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS) or (atom_id_2[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS):
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.dataset,n)}"
                                        "Non-magnetic susceptible spin appears in RDC vector; "
                                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "
                                        f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).")
                        continue

                    if chain_id_1 != chain_id_2:
                        ps1 = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chain_id_1 and 'identical_auth_chain_id' in ps), None)
                        ps2 = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chain_id_2 and 'identical_auth_chain_id' in ps), None)
                        if ps1 is None and ps2 is None:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.dataset,n)}"
                                            "Found inter-chain RDC vector; "
                                            f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "
                                            f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).")
                            continue

                    elif abs(seq_id_1 - seq_id_2) > 1:
                        ps1 = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chain_id_1 and 'gap_in_auth_seq' in ps and ps['gap_in_auth_seq']), None)
                        if ps1 is None:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.dataset,n)}"
                                            "Found inter-residue RDC vector; "
                                            f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "
                                            f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).")
                            continue

                    elif abs(seq_id_1 - seq_id_2) == 1:

                        if self.__csStat.peptideLike(comp_id_1) and self.__csStat.peptideLike(comp_id_2) and\
                                ((seq_id_1 < seq_id_2 and atom_id_1 == 'C' and atom_id_2 in rdcBbPairCode)
                                 or (seq_id_1 > seq_id_2 and atom_id_1 in rdcBbPairCode and atom_id_2 == 'C')
                                 or (seq_id_1 < seq_id_2 and atom_id_1.startswith('HA') and atom_id_2 == 'H')
                                 or (seq_id_1 > seq_id_2 and atom_id_1 == 'H' and atom_id_2.startswith('HA'))):
                            pass

                        else:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.dataset,n)}"
                                            "Found inter-residue RDC vector; "
                                            f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "
                                            f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).")
                            continue

                    elif atom_id_1 == atom_id_2:
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.dataset,n)}"
                                        "Found zero RDC vector; "
                                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "
                                        f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).")
                        continue

                    elif self.__ccU.updateChemCompDict(comp_id_1):  # matches with comp_id in CCD

                        if not self.__ccU.hasBond(comp_id_1, atom_id_1, atom_id_2):

                            if self.__nefT.validate_comp_atom(comp_id_1, atom_id_1) and self.__nefT.validate_comp_atom(comp_id_2, atom_id_2):
                                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.dataset,n)}"
                                                "Found an RDC vector over multiple covalent bonds; "
                                                f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "
                                                f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}).")
                                continue

                    dstFunc = self.validateRdcRange(n, dwt)

                    if dstFunc is None:
                        return

                    if self.__createSfDict:
                        sf = self.__getSf(potentialType=getPotentialType(self.__file_type, self.__cur_subtype, dstFunc),
                                          rdcCode=getRdcCode([self.atomSelectionSet[0][0], self.atomSelectionSet[1][0]]))
                        sf['id'] += 1

                    updatePolySeqRstFromAtomSelectionSet(self.__polySeqRst, self.atomSelectionSet)

                    if any(len(atomSelection) == 0 for atomSelection in self.atomSelectionSet):
                        continue

                    for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                          self.atomSelectionSet[1]):
                        if isIdenticalRestraint([atom1, atom2]):
                            continue
                        if isLongRangeRestraint([atom1, atom2], self.__polySeq if self.__gapInAuthSeq else None):
                            continue
                        if self.__debug:
                            print(f"subtype={self.__cur_subtype} dataset={self.dataset} n={n} "
                                  f"atom1={atom1} atom2={atom2} {dstFunc}")
                        if self.__createSfDict and sf is not None:
                            sf['index_id'] += 1
                            row = getRow(self.__cur_subtype, sf['id'], sf['index_id'],
                                         '.', None, None,
                                         sf['list_id'], self.__entryId, dstFunc,
                                         self.__authToStarSeq, self.__authToInsCode, self.__offsetHolder,
                                         atom1, atom2)
                            sf['loop'].add_data(row)

                elif self.__hasPolySeq:
                    self.__f.append(f"[Missing data] {self.__getCurrentRestraint()}"
                                    "Failed to recognize AMBER atom numbers in the Direct dipolar coupling restraint file "
                                    "because AMBER parameter/topology file is not available.")
                    return

        finally:
            if self.__createSfDict:
                self.__trimSfWoLp()

        # Enter a parse tree produced by AmberMRParser#align_factor.
    def enterAlign_factor(self, ctx: AmberMRParser.Align_factorContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#align_factor.
    def exitAlign_factor(self, ctx: AmberMRParser.Align_factorContext):
        if ctx.ID():
            varName = 'id'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "
                                    f"regulated by 'ndip={self.ndip}'.")
                    return
                self.id[decimal] = int(str(ctx.Integer()))

        elif ctx.JD():
            varName = 'jd'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "
                                    f"regulated by 'ndip={self.ndip}'.")
                    return
                self.jd[decimal] = int(str(ctx.Integer()))

        elif ctx.DOBSL():
            varName = 'dobsl'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "
                                    f"regulated by 'ndip={self.ndip}'.")
                    return
                self.dobsl[decimal] = float(str(ctx.Real()))

        elif ctx.DOBSU():
            varName = 'dobsu'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "
                                    f"regulated by 'ndip={self.ndip}'.")
                    return
                self.dobsu[decimal] = float(str(ctx.Real()))

        elif ctx.DOBS():
            varName = 'dobs'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "
                                    f"regulated by 'ndip={self.ndip}'.")
                    return
                self.dobsl[decimal] = self.dobsu[decimal] = float(str(ctx.Real()))

        elif ctx.DWT():
            varName = 'dwt'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "
                                    f"regulated by 'ndip={self.ndip}'.")
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                val = float(rawRealArray[0])
                if val < 0.0:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"
                                    f"The relative weight value '{varName}({decimal})={val}' must not be a negative value.")
                    return
                if val == 0.0:
                    self.__f.append(f"[Range value warning] {self.__getCurrentRestraint(self.dataset,decimal)}"
                                    f"The relative weight value '{varName}({decimal})={val}' should be a positive value.")
                self.dwt[decimal] = val

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.ndip:
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                        f"The length of '{varName}={ctx.Reals()}' must not exceed 'ndip={self.ndip}'.")
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        val = float(rawReal)
                        if val < 0.0:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The relative weight value '{varName}({col})={val}' must not be a negative value.")
                            return
                        if val == 0.0:
                            self.__f.append(f"[Range value warning] {self.__getCurrentRestraint()}"
                                            f"The relative weight value '{varName}({col})={val}' should be a positive value.")
                        self.dwt[col] = val
                elif ctx.MultiplicativeReal():
                    offset = 0
                    for multiplicativeReal in str(ctx.MultiplicativeReal()).split(','):
                        rawMultReal = multiplicativeReal.split('*')
                        numCol = int(rawMultReal[0])
                        if offset + numCol <= 0 or offset + numCol > self.ndip:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The argument value of '{varName}({numCol})' derived from "
                                            f"'{str(ctx.MultiplicativeReal())}' must be in the range 1-{self.ndip}, "
                                            f"regulated by 'ndip={self.ndip}'.")
                            return
                        val = float(rawMultReal[1])
                        if val < 0.0:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The relative weight value '{varName}={val}' derived from "
                                            f"'{str(ctx.MultiplicativeReal())}' must not be a negative value.")
                            return
                        if val == 0.0:
                            self.__f.append(f"[Range value warning] {self.__getCurrentRestraint()}"
                                            f"The relative weight value '{varName}={val}' derived from "
                                            f"'{str(ctx.MultiplicativeReal())}' should be a positive value.")
                        for col in range(0, numCol):
                            self.dwt[offset + col + 1] = val
                        offset += numCol

        elif ctx.GIGJ():
            varName = 'gigj'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "
                                    f"regulated by 'ndip={self.ndip}'.")
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                self.gigj[decimal] = float(rawRealArray[0])

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.ndip:
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                        f"The length of '{varName}={ctx.Reals()}' must not exceed 'ndip={self.ndip}'.")
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        self.gigj[col] = float(rawReal)
                elif ctx.MultiplicativeReal():
                    offset = 0
                    for multiplicativeReal in str(ctx.MultiplicativeReal()).split(','):
                        rawMultReal = multiplicativeReal.split('*')
                        numCol = int(rawMultReal[0])
                        if offset + numCol <= 0 or offset + numCol > self.ndip:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The argument value of '{varName}({numCol})' derived from "
                                            f"'{str(ctx.MultiplicativeReal())}' must be in the range 1-{self.ndip}, "
                                            f"regulated by 'ndip={self.ndip}'.")
                            return
                        val = float(rawMultReal[1])
                        for col in range(0, numCol):
                            self.gigj[offset + col + 1] = val
                        offset += numCol

        elif ctx.DIJ():
            varName = 'dij'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "
                                    f"regulated by 'ndip={self.ndip}'.")
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                self.dij[decimal] = float(rawRealArray[0])

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.ndip:
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                        f"The length of '{varName}={ctx.Reals()}' must not exceed 'ndip={self.ndip}'.")
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        self.dij[col] = float(rawReal)
                elif ctx.MultiplicativeReal():
                    offset = 0
                    for multiplicativeReal in str(ctx.MultiplicativeReal()).split(','):
                        rawMultReal = multiplicativeReal.split('*')
                        numCol = int(rawMultReal[0])
                        if offset + numCol <= 0 or offset + numCol > self.ndip:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The argument value of '{varName}({numCol})' derived from "
                                            f"'{str(ctx.MultiplicativeReal())}' must be in the range 1-{self.ndip}, "
                                            f"regulated by 'ndip={self.ndip}'.")
                            return
                        val = float(rawMultReal[1])
                        for col in range(0, numCol):
                            self.dij[offset + col + 1] = val
                        offset += numCol

        elif ctx.NDIP():
            self.ndip = int(str(ctx.Integer()))
            if self.ndip <= 0:
                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                f"The argument value of 'ndip={self.ndip}' must be a positive integer.")
                return

        if ctx.DATASET():
            varName = 'dataset'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "
                                    f"regulated by 'ndip={self.ndip}'.")
                    return

            self.dataset = int(str(ctx.Integer()))

            if self.dataset <= 0:
                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                f"The argument value of '{varName}={self.dataset}' must be a positive integer.")
                return

            if self.dataset > self.numDatasets:
                self.numDatasets = self.dataset
                """
                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                f"The argument value of '{varName}={self.dataset}' must be in the range 1-{self.numDatasets}, "
                                f"regulated by 'num_dataset={self.numDatasets}'.")
                return
                """
        elif ctx.NUM_DATASETS():
            self.numDatasets = int(str(ctx.Integer()))
            if self.numDatasets <= 0:
                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                f"The argument value of 'num_dataset={self.numDatasets}' must be a positive integer.")
                return

        elif ctx.S11():
            varName = 's11'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "
                                    f"regulated by 'ndip={self.ndip}'.")
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                self.s11[decimal] = float(rawRealArray[0])

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.ndip:
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                        f"The length of '{varName}={ctx.Reals()}' must not exceed 'ndip={self.ndip}'.")
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        self.s11[col] = float(rawReal)

        elif ctx.S12():
            varName = 's12'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "
                                    f"regulated by 'ndip={self.ndip}'.")
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                self.s12[decimal] = float(rawRealArray[0])

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.ndip:
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                        f"The length of '{varName}={ctx.Reals()}' must not exceed 'ndip={self.ndip}'.")
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        self.s12[col] = float(rawReal)

        elif ctx.S13():
            varName = 's13'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "
                                    f"regulated by 'ndip={self.ndip}'.")
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                self.s13[decimal] = float(rawRealArray[0])

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.ndip:
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                        f"The length of '{varName}={ctx.Reals()}' must not exceed 'ndip={self.ndip}'.")
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        self.s13[col] = float(rawReal)

        elif ctx.S22():
            varName = 's22'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "
                                    f"regulated by 'ndip={self.ndip}'.")
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                self.s22[decimal] = float(rawRealArray[0])

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.ndip:
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                        f"The length of '{varName}={ctx.Reals()}' must not exceed 'ndip={self.ndip}'.")
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        self.s22[col] = float(rawReal)

        elif ctx.S23():
            varName = 's23'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ndip > 0 and decimal > self.ndip:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.dataset,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ndip}, "
                                    f"regulated by 'ndip={self.ndip}'.")
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                self.s23[decimal] = float(rawRealArray[0])

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.ndip:
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                        f"The length of '{varName}={ctx.Reals()}' must not exceed 'ndip={self.ndip}'.")
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        self.s23[col] = float(rawReal)

    # Enter a parse tree produced by AmberMRParser#csa_statement.
    def enterCsa_statement(self, ctx: AmberMRParser.Csa_statementContext):  # pylint: disable=unused-argument
        self.csaRestraints += 1
        self.__cur_subtype = 'csa'

        self.icsa = {}
        self.jcsa = {}
        self.kcsa = {}
        self.cobsl = {}
        self.cobsu = {}
        self.cwt = {}
        self.ncsa = -1
        self.datasetc = 1

        if self.__createSfDict:
            self.__addSf()

    # Exit a parse tree produced by AmberMRParser#csa_statement.
    def exitCsa_statement(self, ctx: AmberMRParser.Csa_statementContext):  # pylint: disable=unused-argument
        try:

            if self.ncsa < 0 and len(self.icsa) > 0:  # pylint: disable=chained-comparison
                self.ncsa = max(self.icsa.keys())

            if self.ncsa <= 0:
                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                "The number of observed CSA values 'ncsa' is the mandatory variable.")
                return

            for n in range(1, self.ncsa + 1):

                if n not in self.icsa:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"
                                    f"The first atom number involved in the CSA icsa({n}) was not set.")
                    continue

                if n not in self.jcsa:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"
                                    f"The second atom number involved in the CSA jcsa({n}) was not set.")
                    continue

                if n not in self.kcsa:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"
                                    f"The second atom number involved in the CSA kcsa({n}) was not set.")
                    continue

                if n not in self.cobsl:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"
                                    f"The lower limit value for the observed CSA cobsl({n}) was not set.")
                    continue

                if n not in self.cobsu:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"
                                    f"The upper limit value for the observed CSA cobsu({n}) was not set.")
                    continue

                _icsa = self.icsa[n]
                _jcsa = self.jcsa[n]
                _kcsa = self.kcsa[n]

                if _icsa <= 0:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"
                                    f"The first atom number involved in the CSA 'icsa({n})={_icsa}' should be a positive integer.")
                    continue

                if _jcsa <= 0:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"
                                    f"The second atom number involved in the CSA 'jcsa({n})={_jcsa}' should be a positive integer.")
                    continue

                if _kcsa <= 0:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"
                                    f"The second atom number involved in the CSA 'kcsa({n})={_kcsa}' should be a positive integer.")
                    continue

                cwt = 1.0
                if n in self.cwt:
                    cwt = self.cwt[n]
                    if cwt <= 0.0:
                        cwt = 1.0

                # convert AMBER atom numbers to corresponding coordinate atoms based on AMBER parameter/topology file
                if self.__atomNumberDict is not None:

                    self.atomSelectionSet.clear()

                    atomSelection = []

                    if _icsa in self.__atomNumberDict:
                        atomSelection.append(copy.copy(self.__atomNumberDict[_icsa]))
                    else:
                        self.__f.append(f"[Missing data] {self.__getCurrentRestraint(self.datasetc,n)}"
                                        f"'icsa({n})={_icsa}' is not defined in the AMBER parameter/topology file.")
                        continue

                    chain_id_1 = atomSelection[0]['chain_id']
                    seq_id_1 = atomSelection[0]['seq_id']
                    comp_id_1 = atomSelection[0]['comp_id']
                    atom_id_1 = atomSelection[0].get('atom_id', None)
                    if atom_id_1 is None:
                        atom_id_1 = atomSelection[0]['atom_id'] = atomSelection[0]['auth_atom_id']

                    self.atomSelectionSet.append(atomSelection)

                    atomSelection = []

                    if _jcsa in self.__atomNumberDict:
                        atomSelection.append(copy.copy(self.__atomNumberDict[_jcsa]))
                    else:
                        self.__f.append(f"[Missing data] {self.__getCurrentRestraint(self.datasetc,n)}"
                                        f"'jcsa({n})={_jcsa}' is not defined in the AMBER parameter/topology file.")
                        continue

                    chain_id_2 = atomSelection[0]['chain_id']
                    seq_id_2 = atomSelection[0]['seq_id']
                    comp_id_2 = atomSelection[0]['comp_id']
                    atom_id_2 = atomSelection[0].get('atom_id', None)
                    if atom_id_2 is None:
                        atom_id_2 = atomSelection[0]['atom_id'] = atomSelection[0]['auth_atom_id']

                    self.atomSelectionSet.append(atomSelection)

                    atomSelection = []

                    if _kcsa in self.__atomNumberDict:
                        atomSelection.append(copy.copy(self.__atomNumberDict[_kcsa]))
                    else:
                        self.__f.append(f"[Missing data] {self.__getCurrentRestraint(self.datasetc,n)}"
                                        f"'kcsa({n})={_kcsa}' is not defined in the AMBER parameter/topology file.")
                        continue

                    chain_id_3 = atomSelection[0]['chain_id']
                    seq_id_3 = atomSelection[0]['seq_id']
                    comp_id_3 = atomSelection[0]['comp_id']
                    atom_id_3 = atomSelection[0].get('atom_id', None)
                    if atom_id_3 is None:
                        atom_id_3 = atomSelection[0]['atom_id'] = atomSelection[0]['auth_atom_id']

                    self.atomSelectionSet.append(atomSelection)

                    if (atom_id_1[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS) or (atom_id_2[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS)\
                       or (atom_id_3[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS):
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"
                                        "Non-magnetic susceptible spin appears in CSA vector; "
                                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "
                                        f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}, "
                                        f"{chain_id_3}:{seq_id_3}:{comp_id_3}:{atom_id_3}).")
                        continue

                    if chain_id_1 != chain_id_2 or chain_id_2 != chain_id_3:
                        ps1 = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chain_id_1 and 'identical_auth_chain_id' in ps), None)
                        ps2 = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chain_id_2 and 'identical_auth_chain_id' in ps), None)
                        ps3 = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chain_id_3 and 'identical_auth_chain_id' in ps), None)
                        if ps1 is None and ps2 is None and ps3 is None:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"
                                            "Found inter-chain CSA vector; "
                                            f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "
                                            f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}, "
                                            f"{chain_id_3}:{seq_id_3}:{comp_id_3}:{atom_id_3}).")
                            continue

                    elif abs(seq_id_1 - seq_id_2) > 1 or abs(seq_id_2 - seq_id_3) > 1 or abs(seq_id_3 - seq_id_1) > 1:
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"
                                        "Found inter-residue CSA vector; "
                                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "
                                        f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}, "
                                        f"{chain_id_3}:{seq_id_3}:{comp_id_3}:{atom_id_3}).")
                        continue

                    elif abs(seq_id_1 - seq_id_2) == 1 or abs(seq_id_2 - seq_id_3) == 1 or abs(seq_id_3 - seq_id_1) == 1:

                        if abs(seq_id_1 - seq_id_2) == 1:

                            if self.__csStat.peptideLike(comp_id_1) and self.__csStat.peptideLike(comp_id_2) and\
                                    ((seq_id_1 < seq_id_2 and atom_id_1 == 'C' and atom_id_2 in rdcBbPairCode)
                                     or (seq_id_1 > seq_id_2 and atom_id_1 in rdcBbPairCode and atom_id_2 == 'C')
                                     or (seq_id_1 < seq_id_2 and atom_id_1.startswith('HA') and atom_id_2 == 'H')
                                     or (seq_id_1 > seq_id_2 and atom_id_1 == 'H' and atom_id_2.startswith('HA'))):
                                pass

                            else:
                                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"
                                                "Found inter-residue CSA vector; "
                                                f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "
                                                f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}, "
                                                f"{chain_id_3}:{seq_id_3}:{comp_id_3}:{atom_id_3}).")
                                continue

                        elif abs(seq_id_2 - seq_id_3) == 1:

                            if self.__csStat.peptideLike(comp_id_2) and self.__csStat.peptideLike(comp_id_3) and\
                                    ((seq_id_2 < seq_id_3 and atom_id_2 == 'C' and atom_id_3 in rdcBbPairCode)
                                     or (seq_id_2 > seq_id_3 and atom_id_2 in rdcBbPairCode and atom_id_3 == 'C')
                                     or (seq_id_2 < seq_id_3 and atom_id_2.startswith('HA') and atom_id_3 == 'H')
                                     or (seq_id_2 > seq_id_3 and atom_id_2 == 'H' and atom_id_3.startswith('HA'))):
                                pass

                            else:
                                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"
                                                "Found inter-residue CSA vector; "
                                                f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "
                                                f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}, "
                                                f"{chain_id_3}:{seq_id_3}:{comp_id_3}:{atom_id_3}).")
                                continue

                        elif abs(seq_id_3 - seq_id_1) == 1:

                            if self.__csStat.peptideLike(comp_id_3) and self.__csStat.peptideLike(comp_id_1) and\
                                    ((seq_id_3 < seq_id_1 and atom_id_3 == 'C' and atom_id_1 in rdcBbPairCode)
                                     or (seq_id_3 > seq_id_1 and atom_id_3 in rdcBbPairCode and atom_id_1 == 'C')
                                     or (seq_id_3 < seq_id_1 and atom_id_3.startswith('HA') and atom_id_1 == 'H')
                                     or (seq_id_3 > seq_id_1 and atom_id_3 == 'H' and atom_id_1.startswith('HA'))):
                                pass

                            else:
                                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"
                                                "Found inter-residue CSA vector; "
                                                f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "
                                                f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}, "
                                                f"{chain_id_3}:{seq_id_3}:{comp_id_3}:{atom_id_3}).")
                                continue

                    elif atom_id_1 == atom_id_2 or atom_id_2 == atom_id_3 or atom_id_3 == atom_id_1:
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"
                                        "Found zero CSA vector; "
                                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "
                                        f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}, "
                                        f"{chain_id_3}:{seq_id_3}:{comp_id_3}:{atom_id_3}).")
                        continue

                    else:

                        if self.__ccU.updateChemCompDict(comp_id_1) and seq_id_1 == seq_id_2:  # matches with comp_id in CCD

                            if not self.__ccU.hasBond(comp_id_1, atom_id_1, atom_id_2):

                                if self.__nefT.validate_comp_atom(comp_id_1, atom_id_1) and self.__nefT.validate_comp_atom(comp_id_2, atom_id_2):
                                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"
                                                    "Found an CSA vector over multiple covalent bonds; "
                                                    f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "
                                                    f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}, "
                                                    f"{chain_id_3}:{seq_id_3}:{comp_id_3}:{atom_id_3}).")
                                    continue

                        if self.__ccU.updateChemCompDict(comp_id_3) and seq_id_3 == seq_id_2:  # matches with comp_id in CCD

                            if not self.__ccU.hasBond(comp_id_1, atom_id_2, atom_id_3):

                                if self.__nefT.validate_comp_atom(comp_id_3, atom_id_3) and self.__nefT.validate_comp_atom(comp_id_2, atom_id_2):
                                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,n)}"
                                                    "Found an CSA vector over multiple covalent bonds; "
                                                    f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "
                                                    f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}, "
                                                    f"{chain_id_3}:{seq_id_3}:{comp_id_3}:{atom_id_3}).")
                                    continue

                    dstFunc = self.validateCsaRange(n, cwt)

                    if dstFunc is None:
                        return

                    if self.__createSfDict:
                        sf = self.__getSf()
                        sf['id'] += 1

                    updatePolySeqRstFromAtomSelectionSet(self.__polySeqRst, self.atomSelectionSet)

                    if any(len(atomSelection) == 0 for atomSelection in self.atomSelectionSet):
                        continue

                    for atom1, atom2, atom3 in itertools.product(self.atomSelectionSet[0],
                                                                 self.atomSelectionSet[1],
                                                                 self.atomSelectionSet[2]):
                        if isLongRangeRestraint([atom1, atom2, atom3], self.__polySeq if self.__gapInAuthSeq else None):
                            continue
                        if self.__debug:
                            print(f"subtype={self.__cur_subtype} dataset={self.datasetc} n={n} "
                                  f"atom1={atom1} atom2(CSA central)={atom2} atom3={atom3} {dstFunc}")
                        if self.__createSfDict and sf is not None:
                            sf['index_id'] += 1
                            row = getRow(self.__cur_subtype, sf['id'], sf['index_id'],
                                         '.', None, None,
                                         sf['list_id'], self.__entryId, dstFunc,
                                         self.__authToStarSeq, self.__authToInsCode, self.__offsetHolder,
                                         atom2)
                            sf['loop'].add_data(row)

                elif self.__hasPolySeq:
                    self.__f.append(f"[Missing data] {self.__getCurrentRestraint()}"
                                    "Failed to recognize AMBER atom numbers in the Residual CSA or psuedo-CSA restraint file "
                                    "because AMBER parameter/topology file is not available.")
                    return

        finally:
            if self.__createSfDict:
                self.__trimSfWoLp()

    # Enter a parse tree produced by AmberMRParser#csa_factor.
    def enterCsa_factor(self, ctx: AmberMRParser.Csa_factorContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#csa_factor.
    def exitCsa_factor(self, ctx: AmberMRParser.Csa_factorContext):
        if ctx.ICSA():
            varName = 'icsa'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ncsa > 0 and decimal > self.ncsa:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ncsa}, "
                                    f"regulated by 'ncsa={self.ncsa}'.")
                    return
                self.icsa[decimal] = int(str(ctx.Integer()))

        elif ctx.JCSA():
            varName = 'jcsa'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ncsa > 0 and decimal > self.ncsa:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ncsa}, "
                                    f"regulated by 'ncsa={self.ncsa}'.")
                    return
                self.jcsa[decimal] = int(str(ctx.Integer()))

        elif ctx.KCSA():
            varName = 'kcsa'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ncsa > 0 and decimal > self.ncsa:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ncsa}, "
                                    f"regulated by 'ncsa={self.ncsa}'.")
                    return
                self.kcsa[decimal] = int(str(ctx.Integer()))

        elif ctx.COBSL():
            varName = 'cobsl'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ncsa > 0 and decimal > self.ncsa:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ncsa}, "
                                    f"regulated by 'ncsa={self.ncsa}'.")
                    return
                self.cobsl[decimal] = float(str(ctx.Real()))

        elif ctx.COBSU():
            varName = 'cobsu'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ncsa > 0 and decimal > self.ncsa:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ncsa}, "
                                    f"regulated by 'ncsa={self.ncsa}'.")
                    return
                self.cobsu[decimal] = float(str(ctx.Real()))

        elif ctx.COBS():
            varName = 'cobs'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ncsa > 0 and decimal > self.ncsa:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ncsa}, "
                                    f"regulated by 'ncsa={self.ncsa}'.")
                    return
                self.cobsl[decimal] = self.cobsu[decimal] = float(str(ctx.Real()))

        elif ctx.CWT():
            varName = 'cwt'

            if ctx.Decimal():
                decimal = int(str(ctx.Decimal()))
                if self.ncsa > 0 and decimal > self.ncsa:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,decimal)}"
                                    f"The argument value of '{varName}({decimal})' must be in the range 1-{self.ncsa}, "
                                    f"regulated by 'ncsa={self.ncsa}'.")
                    return
                rawRealArray = str(ctx.Reals()).split(',')
                val = float(rawRealArray[0])
                if val < 0.0:
                    self.__f.append(f"[Invalid data] {self.__getCurrentRestraint(self.datasetc,decimal)}"
                                    f"The relative weight value '{varName}({decimal})={val}' must not be a negative value.")
                    return
                if val == 0.0:
                    self.__f.append(f"[Range value warning] {self.__getCurrentRestraint(self.datasetc,decimal)}"
                                    f"The relative weight value '{varName}({decimal})={val}' should be a positive value.")
                self.cwt[decimal] = val

            else:
                if ctx.Reals():
                    rawRealArray = str(ctx.Reals()).split(',')
                    if len(rawRealArray) > self.ncsa:
                        self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                        f"The length of '{varName}={ctx.Reals()}' must not exceed 'ncsa={self.ncsa}'.")
                        return
                    for col, rawReal in enumerate(rawRealArray, start=1):
                        val = float(rawReal)
                        if val < 0.0:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The relative weight value '{varName}({col})={val}' must not be a negative value.")
                            return
                        if val == 0.0:
                            self.__f.append(f"[Range value warning] {self.__getCurrentRestraint()}"
                                            f"The relative weight value '{varName}({col})={val}' should be a positive value.")
                        self.cwt[col] = val
                elif ctx.MultiplicativeReal():
                    offset = 0
                    for multiplicativeReal in str(ctx.MultiplicativeReal()).split(','):
                        rawMultReal = multiplicativeReal.split('*')
                        numCol = int(rawMultReal[0])
                        if offset + numCol <= 0 or offset + numCol > self.ncsa:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The argument value of '{varName}({numCol})' derived from "
                                            f"'{str(ctx.MultiplicativeReal())}' must be in the range 1-{self.ncsa}, "
                                            f"regulated by 'ncsa={self.ncsa}'.")
                            return
                        val = float(rawMultReal[1])
                        if val < 0.0:
                            self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                            f"The relative weight value '{varName}={val}' derived from "
                                            f"'{str(ctx.MultiplicativeReal())}' must not be a negative value.")
                            return
                        if val == 0.0:
                            self.__f.append(f"[Range value warning] {self.__getCurrentRestraint()}"
                                            f"The relative weight value '{varName}={val}' derived from "
                                            f"'{str(ctx.MultiplicativeReal())}' should be a positive value.")
                        for col in range(0, numCol):
                            self.cwt[offset + col + 1] = val
                        offset += numCol

        elif ctx.NCSA():
            self.ncsa = int(str(ctx.Integer()))
            if self.ncsa <= 0:
                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                f"The argument value of 'ncsa={self.ncsa}' must be a positive integer.")
                return

        elif ctx.DATASETC():
            self.datasetc = int(str(ctx.Integer()))
            if self.datasetc <= 0:
                self.__f.append(f"[Invalid data] {self.__getCurrentRestraint()}"
                                f"The argument value of 'datasetc={self.datasetc}' must be a positive integer.")
                return

        elif ctx.SIGMA11():
            self.sigma11 = float(str(ctx.Real()))

        elif ctx.SIGMA12():
            self.sigma12 = float(str(ctx.Real()))

        elif ctx.SIGMA13():
            self.sigma13 = float(str(ctx.Real()))

        elif ctx.SIGMA22():
            self.sigma22 = float(str(ctx.Real()))

        elif ctx.SIGMA23():
            self.sigma23 = float(str(ctx.Real()))

        elif ctx.FIELD():
            self.field = float(str(ctx.Real()))

    # Enter a parse tree produced by AmberMRParser#distance_rst_func_call.
    def enterDistance_rst_func_call(self, ctx: AmberMRParser.Distance_rst_func_callContext):  # pylint: disable=unused-argument
        if self.__debug:
            print("  " * self.depth + "enter_distance_rst_func")

        if self.depth == 0:
            self.distRestraints += 1
            self.__cur_subtype = 'dist'

        self.depth += 1

    # Exit a parse tree produced by AmberMRParser#distance_rst_func_call.
    def exitDistance_rst_func_call(self, ctx: AmberMRParser.Distance_rst_func_callContext):  # pylint: disable=unused-argument
        self.depth -= 1
        if self.__debug:
            print("  " * self.depth + "exit_distance_rst_func")

    # Enter a parse tree produced by AmberMRParser#angle_rst_func_call.
    def enterAngle_rst_func_call(self, ctx: AmberMRParser.Angle_rst_func_callContext):  # pylint: disable=unused-argument
        if self.__debug:
            print("  " * self.depth + "enter_angle_rst_func")

        if self.depth == 0:
            self.angRestraints += 1
            self.__cur_subtype = 'ang'

        self.depth += 1

    # Exit a parse tree produced by AmberMRParser#angle_rst_func_call.
    def exitAngle_rst_func_call(self, ctx: AmberMRParser.Angle_rst_func_callContext):  # pylint: disable=unused-argument
        self.depth -= 1
        if self.__debug:
            print("  " * self.depth + "exit_angle_rst_func")

    # Enter a parse tree produced by AmberMRParser#plane_point_angle_rst_func_call.
    def enterPlane_point_angle_rst_func_call(self, ctx: AmberMRParser.Plane_point_angle_rst_func_callContext):  # pylint: disable=unused-argument
        if self.__debug:
            print("  " * self.depth + "enter_plane_point_angle_rst_func")

        if self.depth == 0:
            self.angRestraints += 1
            self.__cur_subtype = 'plane'

        self.depth += 1

    # Exit a parse tree produced by AmberMRParser#plane_point_angle_rst_func_call.
    def exitPlane_point_angle_rst_func_call(self, ctx: AmberMRParser.Plane_point_angle_rst_func_callContext):  # pylint: disable=unused-argument
        self.depth -= 1
        if self.__debug:
            print("  " * self.depth + "exit_plane_point_angle_rst_func")

    # Enter a parse tree produced by AmberMRParser#plane_plane_angle_rst_func_call.
    def enterPlane_plane_angle_rst_func_call(self, ctx: AmberMRParser.Plane_plane_angle_rst_func_callContext):  # pylint: disable=unused-argument
        if self.__debug:
            print("  " * self.depth + "enter_plane_plane_angle_rst_func")

        if self.depth == 0:
            self.angRestraints += 1
            self.__cur_subtype = 'plane'

        self.depth += 1

    # Exit a parse tree produced by AmberMRParser#plane_plane_angle_rst_func_call.
    def exitPlane_plane_angle_rst_func_call(self, ctx: AmberMRParser.Plane_plane_angle_rst_func_callContext):  # pylint: disable=unused-argument
        self.depth -= 1
        if self.__debug:
            print("  " * self.depth + "exit_plane_plane_angle_rst_func")

    # Enter a parse tree produced by AmberMRParser#torsion_rst_func_call.
    def enterTorsion_rst_func_call(self, ctx: AmberMRParser.Torsion_rst_func_callContext):  # pylint: disable=unused-argument
        if self.__debug:
            print("  " * self.depth + "enter_torsion_rst_func")

        if self.depth == 0:
            self.dihedRestraints += 1
            self.__cur_subtype = 'dihed'

        self.depth += 1

    # Exit a parse tree produced by AmberMRParser#torsion_rst_func_call.
    def exitTorsion_rst_func_call(self, ctx: AmberMRParser.Torsion_rst_func_callContext):  # pylint: disable=unused-argument
        self.depth -= 1
        if self.__debug:
            print("  " * self.depth + "exit_torsion_rst_func")

    # Enter a parse tree produced by AmberMRParser#coordinate2_rst_func_call.
    def enterCoordinate2_rst_func_call(self, ctx: AmberMRParser.Coordinate2_rst_func_callContext):  # pylint: disable=unused-argument
        if self.__debug:
            print("  " * self.depth + "enter_coordinate2_rst_func")

        if self.depth == 0:
            self.geoRestraints += 1
            self.__cur_subtype = 'geo'

        self.depth += 1

        self.inGenDist = True
        self.inGenDist_funcExprs = []
        self.inGenDist_weight = [float(str(ctx.Real_F(0))),
                                 float(str(ctx.Real_F(1)))]

    # Exit a parse tree produced by AmberMRParser#coordinate2_rst_func_call.
    def exitCoordinate2_rst_func_call(self, ctx: AmberMRParser.Coordinate2_rst_func_callContext):  # pylint: disable=unused-argument
        self.depth -= 1
        if self.__debug:
            print("  " * self.depth + "exit_coordinate2_rst_func")

    # Enter a parse tree produced by AmberMRParser#coordinate3_rst_func_call.
    def enterCoordinate3_rst_func_call(self, ctx: AmberMRParser.Coordinate3_rst_func_callContext):  # pylint: disable=unused-argument
        if self.__debug:
            print("  " * self.depth + "enter_coordinate3_rst_func")

        if self.depth == 0:
            self.geoRestraints += 1
            self.__cur_subtype = 'geo'

        self.depth += 1

        self.inGenDist = True
        self.inGenDist_funcExprs = []
        self.inGenDist_weight = [float(str(ctx.Real_F(0))),
                                 float(str(ctx.Real_F(1))),
                                 float(str(ctx.Real_F(2)))]

    # Exit a parse tree produced by AmberMRParser#coordinate3_rst_func_call.
    def exitCoordinate3_rst_func_call(self, ctx: AmberMRParser.Coordinate3_rst_func_callContext):  # pylint: disable=unused-argument
        self.depth -= 1
        if self.__debug:
            print("  " * self.depth + "exit_coordinate3_rst_func")

    # Enter a parse tree produced by AmberMRParser#coordinate4_rst_func_call.
    def enterCoordinate4_rst_func_call(self, ctx: AmberMRParser.Coordinate4_rst_func_callContext):  # pylint: disable=unused-argument
        if self.__debug:
            print("  " * self.depth + "enter_coordinate4_rst_func")

        if self.depth == 0:
            self.geoRestraints += 1
            self.__cur_subtype = 'geo'

        self.depth += 1

        self.inGenDist = True
        self.inGenDist_funcExprs = []
        self.inGenDist_weight = [float(str(ctx.Real_F(0))),
                                 float(str(ctx.Real_F(1))),
                                 float(str(ctx.Real_F(2))),
                                 float(str(ctx.Real_F(3)))]

    # Exit a parse tree produced by AmberMRParser#coordinate4_rst_func_call.
    def exitCoordinate4_rst_func_call(self, ctx: AmberMRParser.Coordinate4_rst_func_callContext):  # pylint: disable=unused-argument
        self.depth -= 1
        if self.__debug:
            print("  " * self.depth + "exit_coordinate4_rst_func")

    # Enter a parse tree produced by AmberMRParser#restraint_func_expr.
    def enterRestraint_func_expr(self, ctx: AmberMRParser.Restraint_func_exprContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#restraint_func_expr.
    def exitRestraint_func_expr(self, ctx: AmberMRParser.Restraint_func_exprContext):
        funcExpr = {}

        if ctx.Integer_F():
            funcExpr['igr' if self.inCom else 'iat'] = int(str(ctx.Integer_F()))

        elif ctx.Ambmask_F():
            ambmask = str(ctx.Ambmask_F())[1:].split('@')
            funcExpr['seq_id'] = int(ambmask[0])
            funcExpr['atom_id'] = ambmask[1]

        elif ctx.com_rst_func_call():
            return

        if self.inCom:
            self.inCom_funcExprs.append(funcExpr)
            return

        if self.inPlane:
            if self.inPlane_columnSel == 0:
                self.inPlane_funcExprs.append(funcExpr)
            else:
                self.inPlane_funcExprs2.append(funcExpr)
            return

        if self.inGenDist:
            self.inGenDist_funcExprs.append(funcExpr)
            return

        self.funcExprs.append(funcExpr)

    # Enter a parse tree produced by AmberMRParser#plane_rst_func_call.
    def enterPlane_rst_func_call(self, ctx: AmberMRParser.Plane_rst_func_callContext):  # pylint: disable=unused-argument
        if self.__debug:
            print("  " * self.depth + "enter_plane_rst_func")

        self.depth += 1

        self.inPlane = True
        self.inPlane_columnSel += 1

        if self.inPlane_columnSel == 0:
            self.inPlane_funcExprs = []
        else:
            self.inPlane_funcExprs2 = []

    # Exit a parse tree produced by AmberMRParser#plane_rst_func_call.
    def exitPlane_rst_func_call(self, ctx: AmberMRParser.Plane_rst_func_callContext):  # pylint: disable=unused-argument
        self.depth -= 1
        if self.__debug:
            print("  " * self.depth + "exit_plane_rst_func")

        self.inPlane = False

    # Enter a parse tree produced by AmberMRParser#com_rst_func_call.
    def enterCom_rst_func_call(self, ctx: AmberMRParser.Com_rst_func_callContext):  # pylint: disable=unused-argument
        if self.__debug:
            print("  " * self.depth + "enter_com_rst_func")

        self.depth += 1

        self.inCom = True
        self.inCom_funcExprs = []

    # Exit a parse tree produced by AmberMRParser#com_rst_func_call.
    def exitCom_rst_func_call(self, ctx: AmberMRParser.Com_rst_func_callContext):  # pylint: disable=unused-argument
        self.depth -= 1
        if self.__debug:
            print("  " * self.depth + "exit_com_rst_func")

        self.inCom = False

        if self.inPlane:
            if self.inPlane_columnSel == 0:
                self.inPlane_funcExprs.append(self.inCom_funcExprs)
            else:
                self.inPlane_funcExprs2.append(self.inCom_funcExprs)
            return

        if self.inGenDist:
            self.inGenDist_funcExprs.append(self.inCom_funcExprs)
            return

        self.funcExprs.append(self.inCom_funcExprs)

    # Enter a parse tree produced by AmberMRParser#unambig_atom_name_mapping.
    def enterUnambig_atom_name_mapping(self, ctx: AmberMRParser.Unambig_atom_name_mappingContext):
        self.__cur_resname_for_mapping = str(ctx.Simple_name()).upper()

    # Exit a parse tree produced by AmberMRParser#unambig_atom_name_mapping.
    def exitUnambig_atom_name_mapping(self, ctx: AmberMRParser.Unambig_atom_name_mappingContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberMRParser#mapping_list.
    def enterMapping_list(self, ctx: AmberMRParser.Mapping_listContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#mapping_list.
    def exitMapping_list(self, ctx: AmberMRParser.Mapping_listContext):
        atomName = str(ctx.Simple_name_MP(0)).upper()
        iupacName = set()

        i = 1
        while ctx.Simple_name_MP(i):
            iupacName.add(str(ctx.Simple_name_MP(i)).upper())
            i += 1

        if self.__cur_resname_for_mapping not in self.unambigAtomNameMapping:
            self.unambigAtomNameMapping[self.__cur_resname_for_mapping] = {}
        self.unambigAtomNameMapping[self.__cur_resname_for_mapping][atomName] = list(iupacName)

    # Enter a parse tree produced by AmberMRParser#ambig_atom_name_mapping.
    def enterAmbig_atom_name_mapping(self, ctx: AmberMRParser.Ambig_atom_name_mappingContext):
        self.__cur_resname_for_mapping = str(ctx.Simple_name()).upper()

    # Exit a parse tree produced by AmberMRParser#ambig_atom_name_mapping.
    def exitAmbig_atom_name_mapping(self, ctx: AmberMRParser.Ambig_atom_name_mappingContext):  # pylint: disable=unused-argument
        self.updateAmbigAtomNameMapping()

    # Enter a parse tree produced by AmberMRParser#ambig_list.
    def enterAmbig_list(self, ctx: AmberMRParser.Ambig_listContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by AmberMRParser#ambig_list.
    def exitAmbig_list(self, ctx: AmberMRParser.Ambig_listContext):
        if ctx.Ambig_code_MP():
            ambigCode = str(ctx.Ambig_code_MP())
            i = 0
        else:
            ambigCode = str(ctx.Simple_name_MP(0)).upper()
            i = 1

        mapName = []

        j = 0
        while ctx.Simple_name_MP(i):
            mapName.append({'atom_name': str(ctx.Simple_name_MP(i)).upper(),
                            'seq_id': int(str(ctx.Integer_MP(j)))})
            i += 1
            j += 1

        if self.__cur_resname_for_mapping not in self.ambigAtomNameMapping:
            self.ambigAtomNameMapping[self.__cur_resname_for_mapping] = {}
        self.ambigAtomNameMapping[self.__cur_resname_for_mapping][ambigCode] = mapName

    def updateAmbigAtomNameMapping(self):
        if not self.__hasPolySeq or len(self.ambigAtomNameMapping) == 0:
            return

        unambigResidues = None
        if len(self.unambigAtomNameMapping) > 0:
            unambigResidues = [translateToStdResName(residue, self.__ccU) for residue in self.unambigAtomNameMapping.keys()]

        for ambigDict in self.ambigAtomNameMapping.values():
            for ambigList in ambigDict.values():
                for ambig in ambigList:

                    if 'atom_id_list' in ambig:
                        continue

                    atomName = ambig['atom_name']
                    seqId = ambig['seq_id']

                    chainAssign = self.assignCoordPolymerSequenceWithoutCompId(seqId)

                    if len(chainAssign) == 0:
                        continue

                    ambig['atom_id_list'] = []

                    for cifChainId, cifSeqId, cifCompId in chainAssign:

                        has_unambig = False

                        if unambigResidues is not None and cifCompId in unambigResidues:

                            unambigMap = next(v for k, v in self.unambigAtomNameMapping.items()
                                              if translateToStdResName(k, self.__ccU) == cifCompId)

                            if atomName in unambigMap:

                                for cifAtomId in unambigMap[atomName]:
                                    ambig['atom_id_list'].append({'chain_id': cifChainId,
                                                                  'seq_id': cifSeqId,
                                                                  'comp_id': cifCompId,
                                                                  'atom_id': cifAtomId})

                                has_unambig = True

                        if has_unambig:
                            continue

                        self.atomSelectionSet.clear()

                        self.selectCoordAtoms(chainAssign, seqId, None, ambig['atom_name'].upper(), enableWarning=False)

                        if len(self.atomSelectionSet[0]) > 0:
                            ambig['atom_id_list'].extend(self.atomSelectionSet[0])
                            continue

                        _atomId, _, details = self.__nefT.get_valid_star_atom_in_xplor(cifCompId, atomName, leave_unmatched=True)
                        if details is not None and len(atomName) > 1:
                            _atomId, _, details = self.__nefT.get_valid_star_atom_in_xplor(cifCompId, atomName[:-1], leave_unmatched=True)

                        if details is not None:
                            _atomId_ = translateToStdAtomName(atomName, cifCompId, ccU=self.__ccU)
                            if _atomId_ != atomName:
                                if atomName.startswith('HT') and len(_atomId_) == 2:
                                    _atomId_ = 'H'
                                _atomId = self.__nefT.get_valid_star_atom_in_xplor(cifCompId, _atomId_)[0]

                        for cifAtomId in _atomId:
                            ambig['atom_id_list'].append({'chain_id': cifChainId,
                                                          'seq_id': cifSeqId,
                                                          'comp_id': cifCompId,
                                                          'atom_id': cifAtomId})

                    ambig['atom_id_list'] = [dict(s) for s in set(frozenset(atom.items()) for atom in ambig['atom_id_list'])]

    def getRealChainSeqId(self, ps, seqId, compId=None, isPolySeq=True):  # pylint: disable=no-self-use
        if compId is not None:
            compId = translateToStdResName(compId, self.__ccU)
        if seqId in ps['auth_seq_id']:
            if compId is None:
                return ps['auth_chain_id'], seqId
            idx = ps['auth_seq_id'].index(seqId)
            if compId in (ps['comp_id'][idx], ps['auth_comp_id'][idx]):
                return ps['auth_chain_id'], seqId
        if seqId in ps['seq_id']:
            idx = ps['seq_id'].index(seqId)
            if compId is None:
                return ps['auth_chain_id'], ps['auth_seq_id'][idx]
            if compId in (ps['comp_id'][idx], ps['auth_comp_id'][idx]):
                return ps['auth_chain_id'], ps['auth_seq_id'][idx]
        return ps['chain_id' if isPolySeq else 'auth_chain_id'], seqId

    def assignCoordPolymerSequenceWithoutCompId(self, seqId, atomId=None):
        """ Assign polymer sequences of the coordinates.
        """

        chainAssign = set()
        _seqId = seqId

        for ps in self.__polySeq:
            chainId, seqId = self.getRealChainSeqId(ps, _seqId, None)
            if seqId in ps['auth_seq_id']:
                idx = ps['auth_seq_id'].index(seqId)
                cifCompId = ps['comp_id'][idx]
                if atomId is None or len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                    chainAssign.add((chainId, seqId, cifCompId, True))
            elif 'gap_in_auth_seq' in ps:
                min_auth_seq_id = ps['auth_seq_id'][0]
                max_auth_seq_id = ps['auth_seq_id'][-1]
                if min_auth_seq_id <= seqId <= max_auth_seq_id:
                    offset = 1
                    while seqId + offset <= max_auth_seq_id:
                        if seqId + offset in ps['auth_seq_id']:
                            break
                        offset += 1
                    if seqId + offset not in ps['auth_seq_id']:
                        offset = -1
                        while seqId + offset >= min_auth_seq_id:
                            if seqId + offset in ps['auth_seq_id']:
                                break
                            offset -= 1
                    if seqId + offset in ps['auth_seq_id']:
                        idx = ps['auth_seq_id'].index(seqId + offset) - offset
                        try:
                            seqId_ = ps['auth_seq_id'][idx]
                            cifCompId = ps['comp_id'][idx]
                            if atomId is None or len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                                chainAssign.add((chainId, seqId_, cifCompId, True))
                        except IndexError:
                            pass

        if self.__hasNonPolySeq:
            for np in self.__nonPolySeq:
                chainId, seqId = self.getRealChainSeqId(np, _seqId, None, False)
                if seqId in np['auth_seq_id']:
                    idx = np['auth_seq_id'].index(seqId)
                    cifCompId = np['comp_id'][idx]
                    if atomId is None or len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                        chainAssign.add((chainId, seqId, cifCompId, False))

        if len(chainAssign) == 0:
            for ps in self.__polySeq:
                chainId = ps['chain_id']
                seqKey = (chainId, _seqId)
                if seqKey in self.__authToLabelSeq:
                    _, seqId = self.__authToLabelSeq[seqKey]
                    if seqId in ps['seq_id']:
                        cifCompId = ps['comp_id'][ps['seq_id'].index(seqId)]
                        if atomId is None or len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                            chainAssign.add((ps['auth_chain_id'], _seqId, cifCompId, True))

            if self.__hasNonPolySeq:
                for np in self.__nonPolySeq:
                    chainId = np['auth_chain_id']
                    seqKey = (chainId, _seqId)
                    if seqKey in self.__authToLabelSeq:
                        _, seqId = self.__authToLabelSeq[seqKey]
                        if seqId in np['seq_id']:
                            cifCompId = np['comp_id'][np['seq_id'].index(seqId)]
                            if atomId is None or len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                                chainAssign.add((np['auth_chain_id'], _seqId, cifCompId, False))

        if len(chainAssign) == 0 and self.__altPolySeq is not None:
            for ps in self.__altPolySeq:
                chainId = ps['auth_chain_id']
                if _seqId in ps['auth_seq_id']:
                    cifCompId = ps['comp_id'][ps['auth_seq_id'].index(_seqId)]
                    chainAssign.add((chainId, _seqId, cifCompId, True))

        if len(chainAssign) == 0:
            for ps in self.__polySeq:
                chainId = ps['chain_id']
                seqKey = (chainId, _seqId)
                if seqKey in self.__labelToAuthSeq:
                    _, seqId = self.__labelToAuthSeq[seqKey]
                    if seqId in ps['auth_seq_id']:
                        cifCompId = ps['comp_id'][ps['auth_seq_id'].index(seqId)]
                        if atomId is None or len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                            chainAssign.add((ps['auth_chain_id'], seqId, cifCompId, True))
                            self.__authSeqId = 'label_seq_id'

        if len(chainAssign) == 0:
            if seqId == 1 or (chainId, seqId - 1) in self.__coordUnobsRes:
                if atomId is not None and atomId in aminoProtonCode and atomId != 'H1':
                    return self.assignCoordPolymerSequenceWithoutCompId(seqId, 'H1')
            if atomId is not None and (('-' in atomId and ':' in atomId) or '.' in atomId):
                self.__f.append(f"[Atom not found] "
                                f"{_seqId}:{atomId} is not present in the coordinates. "
                                "Please attach ambiguous atom name mapping information generated by 'makeDIST_RST' to the AMBER restraint file.")
            else:
                if seqId < 1 and len(self.__polySeq) == 1:
                    self.__f.append(f"[Atom not found] {self.__getCurrentRestraint()}"
                                    f"{_seqId}:{atomId} is not present in the coordinates. "
                                    f"The residue number '{_seqId}' is not present in polymer sequence of chain {self.__polySeq[0]['chain_id']} of the coordinates. "
                                    "Please update the sequence in the Macromolecules page.")
                else:
                    self.__f.append(f"[Atom not found] "
                                    f"{_seqId}:{atomId} is not present in the coordinates.")

        return list(chainAssign)

    def selectCoordAtoms(self, chainAssign, seqId, compId, atomId, allowAmbig=True, enableWarning=True, offset=0):
        """ Select atoms of the coordinates.
        """

        atomSelection = []

        for chainId, cifSeqId, cifCompId, isPolySeq in chainAssign:

            if offset != 0:
                cifSeqId += offset
                cifCompId = compId

            seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, cifSeqId, self.__hasCoord)

            _atomId, _, details = self.__nefT.get_valid_star_atom_in_xplor(cifCompId, atomId, leave_unmatched=True)
            if details is not None and len(atomId) > 1 and not atomId[-1].isalpha():
                _atomId, _, details = self.__nefT.get_valid_star_atom_in_xplor(cifCompId, atomId[:-1], leave_unmatched=True)
                if atomId[-1].isdigit() and int(atomId[-1]) <= len(_atomId):
                    _atomId = [_atomId[int(atomId[-1]) - 1]]

            if details is not None:
                _atomId_ = translateToStdAtomName(atomId, cifCompId, ccU=self.__ccU)
                if _atomId_ != atomId:
                    if atomId.startswith('HT') and len(_atomId_) == 2:
                        _atomId_ = 'H'
                    __atomId = self.__nefT.get_valid_star_atom_in_xplor(cifCompId, _atomId_)[0]
                    if coordAtomSite is not None:
                        if any(_atomId_ for _atomId_ in __atomId if _atomId_ in coordAtomSite['atom_id']):
                            _atomId = __atomId
                        elif __atomId[0][0] in protonBeginCode:
                            __bondedTo = self.__ccU.getBondedAtoms(cifCompId, __atomId[0])
                            if len(__bondedTo) > 0 and __bondedTo[0] in coordAtomSite['atom_id']:
                                _atomId = __atomId
                elif coordAtomSite is not None:
                    _atomId = []
            # _atomId = self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]

            if coordAtomSite is not None\
               and not any(_atomId_ for _atomId_ in _atomId if _atomId_ in coordAtomSite['atom_id'])\
               and atomId in coordAtomSite['atom_id']:
                _atomId = [atomId]

            lenAtomId = len(_atomId)
            if lenAtomId == 0:
                if seqId == 1 and isPolySeq and cifCompId == 'ACE' and cifCompId != compId and offset == 0:
                    self.selectCoordAtoms(chainAssign, seqId, compId, atomId, allowAmbig, enableWarning, offset=1)
                    return
                if enableWarning:
                    self.__f.append(f"[Invalid atom nomenclature] "
                                    f"{seqId}:{compId}:{atomId} is invalid atom nomenclature.")
                continue
            if lenAtomId > 1 and not allowAmbig:
                if enableWarning:
                    self.__f.append(f"[Invalid atom selection] "
                                    f"Ambiguous atom selection '{seqId}:{compId}:{atomId}' is not allowed as a angle restraint.")
                continue

            for cifAtomId in _atomId:
                atomSelection.append({'chain_id': chainId, 'seq_id': cifSeqId, 'comp_id': cifCompId, 'atom_id': cifAtomId})

                self.testCoordAtomIdConsistency(chainId, cifSeqId, cifCompId, cifAtomId, seqKey, coordAtomSite, enableWarning)

        if len(atomSelection) > 0:
            self.atomSelectionSet.append(atomSelection)

    def testCoordAtomIdConsistency(self, chainId, seqId, compId, atomId, seqKey, coordAtomSite, enableWarning=True):
        if not self.__hasCoord:
            return

        found = False

        if coordAtomSite is not None:
            if atomId in coordAtomSite['atom_id']:
                found = True
            elif 'alt_atom_id' in coordAtomSite and atomId in coordAtomSite['alt_atom_id']:
                found = True
                self.__authAtomId = 'auth_atom_id'
            elif self.__preferAuthSeq:
                _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, asis=False)
                if _coordAtomSite is not None:
                    if atomId in _coordAtomSite['atom_id']:
                        found = True
                        self.__preferAuthSeq = False
                        self.__authSeqId = 'label_seq_id'
                        seqKey = _seqKey
                    elif 'alt_atom_id' in _coordAtomSite and atomId in _coordAtomSite['alt_atom_id']:
                        found = True
                        self.__preferAuthSeq = False
                        self.__authSeqId = 'label_seq_id'
                        self.__authAtomId = 'auth_atom_id'
                        seqKey = _seqKey

        elif self.__preferAuthSeq:
            _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, asis=False)
            if _coordAtomSite is not None:
                if atomId in _coordAtomSite['atom_id']:
                    found = True
                    self.__preferAuthSeq = False
                    self.__authSeqId = 'label_seq_id'
                    seqKey = _seqKey
                elif 'alt_atom_id' in _coordAtomSite and atomId in _coordAtomSite['alt_atom_id']:
                    found = True
                    self.__preferAuthSeq = False
                    self.__authSeqId = 'label_seq_id'
                    self.__authAtomId = 'auth_atom_id'
                    seqKey = _seqKey

        if found:
            return

        _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, asis=False)
        if _coordAtomSite is not None:
            if atomId in _coordAtomSite['atom_id']:
                found = True
                self.__preferAuthSeq = False
                self.__authSeqId = 'label_seq_id'
                seqKey = _seqKey
            elif 'alt_atom_id' in _coordAtomSite and atomId in _coordAtomSite['alt_atom_id']:
                found = True
                self.__preferAuthSeq = False
                self.__authSeqId = 'label_seq_id'
                self.__authAtomId = 'auth_atom_id'
                seqKey = _seqKey

        if found:
            return

        if self.__ccU.updateChemCompDict(compId):
            cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == atomId), None)
            if cca is not None and seqKey not in self.__coordUnobsRes and self.__ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] == 'REL':
                checked = False
                ps = next((ps for ps in self.__polySeq if ps['auth_chain_id'] == chainId), None)
                if seqId == 1 or (chainId, seqId - 1) in self.__coordUnobsRes or (ps is not None and ps['auth_seq_id'][0] == seqId):
                    if atomId in aminoProtonCode and atomId != 'H1':
                        self.testCoordAtomIdConsistency(chainId, seqId, compId, 'H1', seqKey, coordAtomSite)
                        return
                    if atomId in aminoProtonCode or atomId == 'P' or atomId.startswith('HOP'):
                        checked = True
                if not checked:
                    if atomId[0] in protonBeginCode:
                        bondedTo = self.__ccU.getBondedAtoms(compId, atomId)
                        if len(bondedTo) > 0:
                            if coordAtomSite is not None and bondedTo[0] in coordAtomSite['atom_id'] and cca[self.__ccU.ccaLeavingAtomFlag] != 'Y':
                                if enableWarning:
                                    self.__f.append(f"[Hydrogen not instantiated] "
                                                    f"{chainId}:{seqId}:{compId}:{atomId} is not properly instantiated in the coordinates. "
                                                    "Please re-upload the model file.")
                                    return
                    if enableWarning:
                        if chainId in LARGE_ASYM_ID:
                            self.__f.append(f"[Atom not found] "
                                            f"{chainId}:{seqId}:{compId}:{atomId} is not present in the coordinates.")

    def __getCurrentRestraint(self, dataset=None, n=None):
        if self.__cur_subtype == 'dist':
            return f"[Check the {self.distRestraints}th row of distance restraints] "
        if self.__cur_subtype == 'ang':
            return f"[Check the {self.angRestraints}th row of angle restraints] "
        if self.__cur_subtype == 'dihed':
            return f"[Check the {self.dihedRestraints}th row of torsional angle restraints] "
        if self.__cur_subtype == 'rdc':
            if dataset is None or n is None:
                return f"[Check the {self.rdcRestraints}th row of residual dipolar coupling restraints] "
            return f"[Check the {n}th row of residual dipolar coupling restraints (dataset={dataset})] "
        if self.__cur_subtype == 'plane':
            return f"[Check the {self.planeRestraints}th row of plane-point/plane angle restraints] "
        if self.__cur_subtype == 'noepk':
            if dataset is None or n is None:
                return f"[Check the {self.noepkRestraints}th row of NOESY volume restraints] "
            return f"[Check the {n}th row of NOESY volume restraints (dataset={dataset})] "
        if self.__cur_subtype == 'procs':
            if n is None:
                return f"[Check the {self.procsRestraints}th row of chemical shift restraints] "
            return f"[Check the {n}th row of chemical shift restraints] "
        if self.__cur_subtype == 'pcs':
            if dataset is None or n is None:
                return f"[Check the {self.pcsRestraints}th row of pseudocontact shift restraints] "
            return f"[Check the {n}th row of pseudocontact shift restraints (name of paramagnetic center={dataset})] "
        if self.__cur_subtype == 'csa':
            if dataset is None or n is None:
                return f"[Check the {self.csaRestraints}th row of residual CSA or pseudo-CSA restraints] "
            return f"[Check the {n}th row of residual CSA or pseudo-CSA restraints (dataset={dataset})] "
        if self.__cur_subtype == 'geo':
            return f"[Check the {self.geoRestraints}th row of generalized distance restraints] "
        return f"[Check the {self.nmrRestraints}th row of NMR restraints] "

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

        sf_framecode = 'AMBER_' + restraint_name.replace(' ', '_') + f'_{list_id}'

        sf = getSaveframe(self.__cur_subtype, sf_framecode, list_id, self.__entryId, self.__originalFileName,
                          constraintType=constraintType, potentialType=potentialType, rdcCode=rdcCode)

        not_valid = True

        lp = getLoop(self.__cur_subtype, hasInsCode=(self.__authToInsCode is not None))
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

        self.__lastSfDict[self.__cur_subtype] = item

        self.sfDict[key].append(item)

    def __getSf(self, constraintType=None, potentialType=None, rdcCode=None):
        key = (self.__cur_subtype, constraintType, potentialType, rdcCode, None)

        if key not in self.sfDict:
            replaced = False
            if potentialType is not None or rdcCode is not None:
                old_key = (self.__cur_subtype, constraintType, None, None, None)
                if old_key in self.sfDict:
                    replaced = True
                    self.sfDict[key] = [self.sfDict[old_key].pop(-1)]
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

    def __trimSfWoLp(self):
        if self.__cur_subtype not in self.__lastSfDict:
            return
        if self.__lastSfDict[self.__cur_subtype]['index_id'] > 0:
            return
        for k, v in self.sfDict.items():
            for item in reversed(v):
                if item == self.__lastSfDict:
                    v.remove(item)
                    if len(v) == 0:
                        del self.sfDict[k]
                    self.__listIdCounter = decListIdCounter(k[0], self.__listIdCounter)
                    return

    def getContentSubtype(self):
        """ Return content subtype of AMBER MR file.
        """

        contentSubtype = {'dist_restraint': self.distRestraints,
                          'ang_restraint': self.angRestraints,
                          'dihed_restraint': self.dihedRestraints,
                          'rdc_restraint': self.rdcRestraints,
                          'plane_restraint': self.planeRestraints,
                          'noepk_restraint': self.noepkRestraints,
                          'procs_restraint': self.procsRestraints,
                          'pcs_restraint': self.pcsRestraints,
                          'csa_restraint': self.csaRestraints,
                          'geo_restraint': self.geoRestraints
                          }

        return {k: 1 for k, v in contentSubtype.items() if v > 0}

    def getPolymerSequence(self):
        """ Return polymer sequence of AMBER MR file.
        """
        return None if self.__polySeqRst is None or len(self.__polySeqRst) == 0 else self.__polySeqRst

    def getSequenceAlignment(self):
        """ Return sequence alignment between coordinates and AMBER MR.
        """
        return None if self.__seqAlign is None or len(self.__seqAlign) == 0 else self.__seqAlign

    def getChainAssignment(self):
        """ Return chain assignment between coordinates and AMBER MR.
        """
        return None if self.__chainAssign is None or len(self.__chainAssign) == 0 else self.__chainAssign

    def getAtomNumberDict(self):
        """ Return AMBER atomic number dictionary.
        """
        return self.__atomNumberDict

    def getSanderAtomNumberDict(self):
        """ Return AMBER atomic number dictionary based on Sander comments.
        """
        return self.__sanderAtomNumberDict

    def getReasonsForReparsing(self):
        """ Return reasons for re-parsing AMBER MR file.
        """
        return None if len(self.reasonsForReParsing) == 0 else self.reasonsForReParsing

    def hasComments(self):
        """ Return whether Sander comments are available.
        """
        return self.__hasComments

    def getSfDict(self):
        """ Return a dictionary of pynmrstar saveframes.
        """
        if len(self.sfDict) == 0:
            return self.__listIdCounter, None
        ign_keys = []
        for k, v in self.sfDict.items():
            for item in reversed(v):
                if item['index_id'] == 0:
                    v.remove(item)
                    if len(v) == 0:
                        ign_keys.append(k)
                    self.__listIdCounter = decListIdCounter(k[0], self.__listIdCounter)
        for k in ign_keys:
            del self.sfDict[k]
        return self.__listIdCounter, None if len(self.sfDict) == 0 else self.sfDict

# del AmberMRParser
