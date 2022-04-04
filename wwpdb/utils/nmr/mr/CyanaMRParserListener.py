##
# File: CyanaMRParserListener.py
# Date: 27-Jan-2022
#
# Updates:
# Generated from CyanaMRParser.g4 by ANTLR 4.9
""" ParserLister class for CYANA MR files.
    @author: Masashi Yokochi
"""
import sys
import itertools

from antlr4 import ParseTreeListener

try:
    from wwpdb.utils.nmr.mr.CyanaMRParser import CyanaMRParser
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (checkCoordinates,
                                                       REPRESENTATIVE_MODEL_ID,
                                                       DIST_RESTRAINT_RANGE,
                                                       DIST_RESTRAINT_ERROR,
                                                       ANGLE_RESTRAINT_RANGE,
                                                       ANGLE_RESTRAINT_ERROR,
                                                       RDC_RESTRAINT_RANGE,
                                                       RDC_RESTRAINT_ERROR,
                                                       PCS_RESTRAINT_RANGE,
                                                       PCS_RESTRAINT_ERROR,
                                                       KNOWN_ANGLE_NAMES,
                                                       KNOWN_ANGLE_ATOM_NAMES,
                                                       KNOWN_ANGLE_SEQ_OFFSET,
                                                       KNOWN_ANGLE_CARBO_ATOM_NAMES,
                                                       KNOWN_ANGLE_CARBO_SEQ_OFFSET)
    from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
    from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from wwpdb.utils.nmr.NEFTranslator.NEFTranslator import (NEFTranslator,
                                                             ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS)
except ImportError:
    from nmr.mr.CyanaMRParser import CyanaMRParser
    from nmr.mr.ParserListenerUtil import (checkCoordinates,
                                           REPRESENTATIVE_MODEL_ID,
                                           DIST_RESTRAINT_RANGE,
                                           DIST_RESTRAINT_ERROR,
                                           ANGLE_RESTRAINT_RANGE,
                                           ANGLE_RESTRAINT_ERROR,
                                           RDC_RESTRAINT_RANGE,
                                           RDC_RESTRAINT_ERROR,
                                           PCS_RESTRAINT_RANGE,
                                           PCS_RESTRAINT_ERROR,
                                           KNOWN_ANGLE_NAMES,
                                           KNOWN_ANGLE_ATOM_NAMES,
                                           KNOWN_ANGLE_SEQ_OFFSET,
                                           KNOWN_ANGLE_CARBO_ATOM_NAMES,
                                           KNOWN_ANGLE_CARBO_SEQ_OFFSET)
    from nmr.ChemCompUtil import ChemCompUtil
    from nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from nmr.NEFTranslator.NEFTranslator import (NEFTranslator,
                                                 ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS)


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


PCS_RANGE_MIN = PCS_RESTRAINT_RANGE['min_inclusive']
PCS_RANGE_MAX = PCS_RESTRAINT_RANGE['max_inclusive']

PCS_ERROR_MIN = PCS_RESTRAINT_ERROR['min_exclusive']
PCS_ERROR_MAX = PCS_RESTRAINT_ERROR['max_exclusive']


# This class defines a complete listener for a parse tree produced by CyanaMRParser.
class CyanaMRParserListener(ParseTreeListener):

    # __verbose = None
    # __lfh = None
    __debug = False

    distRestraints = 0      # CYANA: Distance restraint file
    dihedRestraints = 0     # CYANA: Torsion angle restraint file
    rdcRestraints = 0       # CYANA: Residual dipolar coupling restraint file
    pcsRestraints = 0       # CYANA: Pseudocontact shift restraint file

    # CCD accessing utility
    __ccU = None

    # BMRB chemical shift statistics
    __csStat = None

    # NEFTranslator
    __nefT = None

    # reasons for re-parsing request from the previous trial
    __reasons = None

    __upl_or_lol = None  # must be one of (None, 'upl_only', 'upl_w_lol', 'lol_only', 'lol_w_upl')

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

    # polymer sequences in the coordinate file generated by NmrDpUtility.__extractCoordPolymerSequence()
    __hasPolySeq = False
    __polySeq = None
    __altPolySeq = None
    __coordAtomSite = None
    __coordUnobsRes = None
    __labelToAuthSeq = None
    __authToLabelSeq = None
    __preferAuthSeq = True

    # current restraint subtype
    __cur_subtype = None

    # RDC parameter dictionary
    rdcParameterDict = None

    # PCS parameter dictionary
    pcsParameterDict = None

    # collection of atom selection
    atomSelectionSet = []

    # collection of number selection
    numberSelection = []

    warningMessage = ''

    reasonsForReParsing = None

    def __init__(self, verbose=True, log=sys.stdout,
                 representativeModelId=REPRESENTATIVE_MODEL_ID,
                 cR=None, cC=None, ccU=None, csStat=None, nefT=None,
                 reasons=None, upl_or_lol=None):
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

        # reasons for re-parsing request from the previous trial
        self.__reasons = reasons

        self.__upl_or_lol = upl_or_lol

        if upl_or_lol not in (None, 'upl_only', 'upl_w_lol', 'lol_only', 'lol_w_upl'):
            msg = f"The argument 'upl_or_lol' must be one of {(None, 'upl_only', 'upl_w_lol', 'lol_only', 'lol_w_upl')}"
            log.write(f"'+CyanaMRParserListener.__init__() ++ ValueError  -  {msg}\n")
            raise ValueError(f"'+CyanaMRParserListener.__init__() ++ ValueError  -  {msg}")

        self.__max_dist_value = None

    def setDebugMode(self, debug):
        self.__debug = debug

    # Enter a parse tree produced by CyanaMRParser#cyana_mr.
    def enterCyana_mr(self, ctx: CyanaMRParser.Cyana_mrContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CyanaMRParser#cyana_mr.
    def exitCyana_mr(self, ctx: CyanaMRParser.Cyana_mrContext):  # pylint: disable=unused-argument
        if len(self.warningMessage) == 0:
            self.warningMessage = None
        else:
            self.warningMessage = self.warningMessage[0:-1]
            self.warningMessage = '\n'.join(set(self.warningMessage.split('\n')))

    # Enter a parse tree produced by CyanaMRParser#distance_restraints.
    def enterDistance_restraints(self, ctx: CyanaMRParser.Distance_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dist'

    # Exit a parse tree produced by CyanaMRParser#distance_restraints.
    def exitDistance_restraints(self, ctx: CyanaMRParser.Distance_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#distance_restraint.
    def enterDistance_restraint(self, ctx: CyanaMRParser.Distance_restraintContext):  # pylint: disable=unused-argument
        self.distRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by CyanaMRParser#distance_restraint.
    def exitDistance_restraint(self, ctx: CyanaMRParser.Distance_restraintContext):
        seqId1 = int(str(ctx.Integer(0)))
        compId1 = str(ctx.Simple_name(0)).upper()
        atomId1 = str(ctx.Simple_name(1)).upper()
        seqId2 = int(str(ctx.Integer(1)))
        compId2 = str(ctx.Simple_name(2)).upper()
        atomId2 = str(ctx.Simple_name(3)).upper()

        target_value = None
        lower_limit = None
        upper_limit = None

        value = self.numberSelection[0]

        self.numberSelection.clear()

        if DIST_RANGE_MIN <= value <= DIST_RANGE_MAX:
            if self.__max_dist_value is None:
                self.__max_dist_value = value
            if value > self.__max_dist_value:
                self.__max_dist_value = value

        if self.__upl_or_lol is None or self.__upl_or_lol == 'upl_only':
            if value > 1.8:
                upper_limit = value
                lower_limit = 1.8  # default value of PDBStat
                target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat
            else:
                lower_limit = value

        elif self.__upl_or_lol == 'upl_w_lol':
            upper_limit = value

        elif self.__upl_or_lol == 'lol_only':
            lower_limit = value
            upper_limit = 5.5  # default value of PDBStat
            target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat

        else:  # 'lol_w_upl'
            lower_limit = value

        dstFunc = self.validateDistanceRange(1.0, target_value, lower_limit, upper_limit)

        if dstFunc is None:
            return

        if not self.__hasPolySeq:
            return

        chainAssign1 = self.assignCoordPolymerSequence(seqId1, compId1, atomId1)
        chainAssign2 = self.assignCoordPolymerSequence(seqId2, compId2, atomId2)

        if len(chainAssign1) == 0 or len(chainAssign2) == 0:
            return

        self.selectCoordAtoms(chainAssign1, seqId1, compId1, atomId1)
        self.selectCoordAtoms(chainAssign2, seqId2, compId2, atomId2)

        if len(self.atomSelectionSet) < 2:
            return

        for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                              self.atomSelectionSet[1]):
            if self.__debug:
                print(f"subtype={self.__cur_subtype} id={self.distRestraints} "
                      f"atom1={atom1} atom2={atom2} {dstFunc}")

    def validateDistanceRange(self, weight, target_value, lower_limit, upper_limit):
        """ Validate distance value range.
        """

        validRange = True
        dstFunc = {'weight': weight}

        if target_value is not None:
            if DIST_ERROR_MIN < target_value < DIST_ERROR_MAX:
                dstFunc['target_value'] = f"{target_value:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The target value='{target_value}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if lower_limit is not None:
            if DIST_ERROR_MIN <= lower_limit < DIST_ERROR_MAX:
                dstFunc['lower_limit'] = f"{lower_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower limit value='{lower_limit}' must be within range {DIST_RESTRAINT_ERROR}.\n"

        if upper_limit is not None:
            if DIST_ERROR_MIN < upper_limit <= DIST_ERROR_MAX:
                dstFunc['upper_limit'] = f"{upper_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit}' must be within range {DIST_RESTRAINT_ERROR}.\n"

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
                    f"The lower limit value='{lower_limit}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        if upper_limit is not None:
            if DIST_RANGE_MIN <= upper_limit <= DIST_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit}' should be within range {DIST_RESTRAINT_RANGE}.\n"

        return dstFunc

    def getRealChainSeqId(self, ps, seqId, compId):
        if self.__reasons is not None and 'label_seq_scheme' in self.__reasons and self.__reasons['label_seq_scheme']:
            seqKey = (ps['chain_id'], seqId)
            if seqKey in self.__labelToAuthSeq:
                _chainId, _seqId = self.__labelToAuthSeq[seqKey]
                if _seqId in ps['auth_seq_id']:
                    return _chainId, _seqId
        if seqId in ps['auth_seq_id']:
            if ps['comp_id'][ps['auth_seq_id'].index(seqId)] == compId:
                return ps['auth_chain_id'], seqId
        if seqId in ps['seq_id']:
            if ps['comp_id'][ps['seq_id'].index(seqId)] == compId:
                return ps['auth_chain_id'], ps['auth_seq_id'][ps['seq_id'].index(seqId)]
        return ps['chain_id'], seqId

    def assignCoordPolymerSequence(self, seqId, compId, atomId):
        """ Assign polymer sequences of the coordinates.
        """

        chainAssign = []
        _seqId = seqId

        for ps in self.__polySeq:
            chainId, seqId = self.getRealChainSeqId(ps, _seqId, compId)
            if seqId in ps['auth_seq_id']:
                cifCompId = ps['comp_id'][ps['auth_seq_id'].index(seqId)]
                if cifCompId == compId:
                    if len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                        chainAssign.append((chainId, seqId, cifCompId))
                elif len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                    chainAssign.append((chainId, seqId, cifCompId))
                    if cifCompId != compId:
                        self.warningMessage += f"[Unmatched residue name] {self.__getCurrentRestraint()}"\
                            f"The residue name {_seqId}:{compId} is unmatched with the name of the coordinates, {cifCompId}.\n"

        if len(chainAssign) == 0:
            for ps in self.__polySeq:
                chainId = ps['chain_id']
                seqKey = (chainId, _seqId)
                if seqKey in self.__authToLabelSeq:
                    _, seqId = self.__authToLabelSeq[seqKey]
                    if seqId in ps['seq_id']:
                        cifCompId = ps['comp_id'][ps['seq_id'].index(seqId)]
                        if cifCompId == compId:
                            if len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                                chainAssign.append((ps['auth_chain_id'], _seqId, cifCompId))
                                if self.reasonsForReParsing is None:
                                    self.reasonsForReParsing = {}
                                if 'label_seq_scheme' not in self.reasonsForReParsing:
                                    self.reasonsForReParsing['label_seq_scheme'] = True
                        elif len(self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                            chainAssign.append((ps['auth_chain_id'], _seqId, cifCompId))
                            if cifCompId != compId:
                                self.warningMessage += f"[Unmatched residue name] {self.__getCurrentRestraint()}"\
                                    f"The residue name {_seqId}:{compId} is unmatched with the name of the coordinates, {cifCompId}.\n"

        if len(chainAssign) == 0 and self.__altPolySeq is not None:
            for ps in self.__altPolySeq:
                chainId = ps['auth_chain_id']
                if _seqId in ps['auth_seq_id']:
                    cifCompId = ps['comp_id'][ps['auth_seq_id'].index(_seqId)]
                    chainAssign.append(chainId, _seqId, cifCompId)
                    if cifCompId != compId:
                        self.warningMessage += f"[Unmatched residue name] {self.__getCurrentRestraint()}"\
                            f"The residue name {_seqId}:{compId} is unmatched with the name of the coordinates, {cifCompId}.\n"

        if len(chainAssign) == 0:
            self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                f"{_seqId}:{compId}:{atomId} is not present in the coordinates.\n"

        return chainAssign

    def selectCoordAtoms(self, chainAssign, seqId, compId, atomId, allowAmbig=True):
        """ Select atoms of the coordinates.
        """

        atomSelection = []

        for chainId, cifSeqId, cifCompId in chainAssign:
            seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, cifSeqId, self.__hasCoord)

            _atomId = self.__nefT.get_valid_star_atom(cifCompId, atomId)[0]
            lenAtomId = len(_atomId)
            if lenAtomId == 0:
                self.warningMessage += f"[Invalid atom nomenclature] {self.__getCurrentRestraint()}"\
                    f"{seqId}:{compId}:{atomId} is invalid atom nomenclature.\n"
                continue
            if lenAtomId > 1 and not allowAmbig:
                self.warningMessage += f"[Invalid atom selection] {self.__getCurrentRestraint()}"\
                    f"Ambiguous atom selection '{seqId}:{compId}:{atomId}' is not allowed as a angle restraint.\n"
                continue

            for cifAtomId in _atomId:
                atomSelection.append({'chain_id': chainId, 'seq_id': cifSeqId, 'comp_id': cifCompId, 'atom_id': cifAtomId})

                self.testCoordAtomIdConsistency(chainId, cifSeqId, cifCompId, cifAtomId, seqKey, coordAtomSite)

        if len(atomSelection) > 0:
            self.atomSelectionSet.append(atomSelection)

    def testCoordAtomIdConsistency(self, chainId, seqId, compId, atomId, seqKey, coordAtomSite):
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

        if self.__ccU.updateChemCompDict(compId):
            cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == atomId), None)
            if cca is not None and seqKey not in self.__coordUnobsRes:
                self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
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

    # Enter a parse tree produced by CyanaMRParser#torsion_angle_restraints.
    def enterTorsion_angle_restraints(self, ctx: CyanaMRParser.Torsion_angle_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dihed'

    # Exit a parse tree produced by CyanaMRParser#torsion_angle_restraints.
    def exitTorsion_angle_restraints(self, ctx: CyanaMRParser.Torsion_angle_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#torsion_angle_restraint.
    def enterTorsion_angle_restraint(self, ctx: CyanaMRParser.Torsion_angle_restraintContext):  # pylint: disable=unused-argument
        self.dihedRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by CyanaMRParser#torsion_angle_restraint.
    def exitTorsion_angle_restraint(self, ctx: CyanaMRParser.Torsion_angle_restraintContext):  # pylint: disable=unused-argument
        seqId = int(str(ctx.Integer()))
        compId = str(ctx.Simple_name(0)).upper()
        angleName = str(ctx.Simple_name(1)).upper()
        lower_limit = self.numberSelection[0]
        upper_limit = self.numberSelection[1]

        self.numberSelection.clear()

        if lower_limit > upper_limit:
            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                f"The angle's lower limit '{lower_limit}' must be less than or equal to the upper limit '{upper_limit}'.\n"
            return

        if angleName not in KNOWN_ANGLE_NAMES:
            self.warningMessage += f"[Enum mismatch ignorable] {self.__getCurrentRestraint()}"\
                f"The angle identifier '{str(ctx.Simple_name(1))}' is unknown.\n"
            return

        target_value = (upper_limit + lower_limit) / 2.0

        while target_value > ANGLE_RANGE_MAX:
            target_value -= 360.0
        while target_value < ANGLE_RANGE_MIN:
            target_value += 360.0

        dstFunc = self.validateAngleRange(1.0, target_value, lower_limit, upper_limit)

        if dstFunc is None:
            return

        if not self.__hasPolySeq:
            return

        peptide, nucleotide, carbohydrate = self.__csStat.getTypeOfCompId(compId)

        if carbohydrate:
            atomNames = KNOWN_ANGLE_CARBO_ATOM_NAMES[angleName]
            seqOffset = KNOWN_ANGLE_CARBO_SEQ_OFFSET[angleName]
        else:
            atomNames = KNOWN_ANGLE_ATOM_NAMES[angleName]
            seqOffset = KNOWN_ANGLE_SEQ_OFFSET[angleName]

        if isinstance(atomNames, list):
            atomId = next(name for name, offset in zip(atomNames, seqOffset) if offset == 0)
        else:  # 'CHI'
            atomId = next(name for name, offset in zip(atomNames['Y'], seqOffset['Y']) if offset == 0)

        chainAssign = self.assignCoordPolymerSequence(seqId, compId, atomId)

        if len(chainAssign) == 0:
            self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                f"{seqId}:{compId} is not present in the coordinates.\n"
            return

        for chainId, cifSeqId, cifCompId in chainAssign:
            ps = next(ps for ps in self.__polySeq if ps['auth_chain_id'] == chainId)

            peptide, nucleotide, carbohydrate = self.__csStat.getTypeOfCompId(cifCompId)

            atomNames = None
            seqOffset = None

            if carbohydrate:
                atomNames = KNOWN_ANGLE_CARBO_ATOM_NAMES[angleName]
                seqOffset = KNOWN_ANGLE_CARBO_SEQ_OFFSET[angleName]
            elif nucleotide and angleName == 'CHI':
                if self.__ccU.updateChemCompDict(cifCompId):
                    try:
                        next(cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == 'N9')
                        atomNames = KNOWN_ANGLE_ATOM_NAMES['CHI']['R']
                        seqOffset = KNOWN_ANGLE_SEQ_OFFSET['CHI']['R']
                    except StopIteration:
                        atomNames = KNOWN_ANGLE_ATOM_NAMES['CHI']['Y']
                        seqOffset = KNOWN_ANGLE_SEQ_OFFSET['CHI']['Y']
            else:
                atomNames = KNOWN_ANGLE_ATOM_NAMES[angleName]
                seqOffset = KNOWN_ANGLE_SEQ_OFFSET[angleName]

            if peptide and angleName in ('PHI', 'PSI', 'OMEGA',
                                         'CHI1', 'CHI2', 'CHI3', 'CHI4', 'CHI5',
                                         'CHI21', 'CHI22', 'CHI31', 'CHI32', 'CHI42'):
                pass
            elif nucleotide and angleName in ('ALPHA', 'BETA', 'GAMMA', 'DELTA', 'EPSILON', 'ZETA',
                                              'CHI', 'ETA', 'THETA', "ETA'", "THETA'",
                                              'NU0', 'NU1', 'NU2', 'NU3', 'NU4',
                                              'TAU0', 'TAU1', 'TAU2', 'TAU3', 'TAU4'):
                pass
            elif carbohydrate and angleName in ('PHI', 'PSI', 'OMEGA'):
                pass
            else:
                self.warningMessage += f"[Enum mismatch ignorable] {self.__getCurrentRestraint()}"\
                    f"The angle identifier {str(ctx.Simple_name(1))!r} did not match with residue {compId!r}.\n"
                return

            for atomId, offset in zip(atomNames, seqOffset):

                atomSelection = []

                _cifSeqId = cifSeqId + offset
                _cifCompId = cifCompId if offset == 0 else (ps['comp_id'][ps['auth_seq_id'].index(_cifSeqId)] if _cifSeqId in ps['auth_seq_id'] else None)

                if _cifCompId is None:
                    self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                        f"The sequence number '{seqId+offset}' is not present in polymer sequence of chain {chainId} of the coordinates.\n"
                    return

                self.__ccU.updateChemCompDict(_cifCompId)

                if isinstance(atomId, str):
                    cifAtomId = next((cca[self.__ccU.ccaAtomId] for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == atomId), None)
                else:
                    cifAtomId = next((cca[self.__ccU.ccaAtomId] for cca in self.__ccU.lastAtomList if atomId.match(cca[self.__ccU.ccaAtomId])), None)

                if cifAtomId is None:
                    self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                        f"{seqId+offset}:{compId}:{atomId} is not present in the coordinates.\n"
                    return

                atomSelection.append({'chain_id': chainId, 'seq_id': _cifSeqId, 'comp_id': _cifCompId, 'atom_id': cifAtomId})

                if len(atomSelection) > 0:
                    self.atomSelectionSet.append(atomSelection)

            if len(self.atomSelectionSet) < 4:
                return

            for atom1, atom2, atom3, atom4 in itertools.product(self.atomSelectionSet[0],
                                                                self.atomSelectionSet[1],
                                                                self.atomSelectionSet[2],
                                                                self.atomSelectionSet[3]):
                if self.__debug:
                    print(f"subtype={self.__cur_subtype} id={self.dihedRestraints} angleName={angleName} "
                          f"atom1={atom1} atom2={atom2} atom3={atom3} atom4={atom4} {dstFunc}")

    def validateAngleRange(self, weight, target_value, lower_limit, upper_limit):
        """ Validate angle value range.
        """

        validRange = True
        dstFunc = {'weight': weight}

        if target_value is not None:
            if ANGLE_ERROR_MIN < target_value < ANGLE_ERROR_MAX:
                dstFunc['target_value'] = f"{target_value:.3f}"
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
                    f"The lower limit value='{lower_limit}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"

        if upper_limit is not None:
            if ANGLE_ERROR_MIN < upper_limit <= ANGLE_ERROR_MAX:
                dstFunc['upper_limit'] = f"{upper_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit}' must be within range {ANGLE_RESTRAINT_ERROR}.\n"

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

    # Enter a parse tree produced by CyanaMRParser#rdc_restraints.
    def enterRdc_restraints(self, ctx: CyanaMRParser.Rdc_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'rdc'

        self.rdcParameterDict = {}

    # Exit a parse tree produced by CyanaMRParser#rdc_restraints.
    def exitRdc_restraints(self, ctx: CyanaMRParser.Rdc_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#rdc_parameter.
    def enterRdc_parameter(self, ctx: CyanaMRParser.Rdc_parameterContext):  # pylint: disable=unused-argument
        orientation = int(str(ctx.Integer(0)))
        magnitude = float(str(ctx.Float(0)))
        rhombicity = float(str(ctx.Float(1)))
        orientationCenterSeqId = int(str(ctx.Integer(1)))

        self.rdcParameterDict[orientation] = {'magnitude': magnitude,
                                              'rhombicity': rhombicity,
                                              'orientation_center_seq_id': orientationCenterSeqId}

        if self.__debug:
            print(f"subtype={self.__cur_subtype} orientation={orientation} "
                  f"parameters={self.rdcParameterDict[orientation]}")

    # Exit a parse tree produced by CyanaMRParser#rdc_parameter.
    def exitRdc_parameter(self, ctx: CyanaMRParser.Rdc_parameterContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#rdc_restraint.
    def enterRdc_restraint(self, ctx: CyanaMRParser.Rdc_restraintContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by CyanaMRParser#rdc_restraint.
    def exitRdc_restraint(self, ctx: CyanaMRParser.Rdc_restraintContext):
        seqId1 = int(str(ctx.Integer(0)))
        compId1 = str(ctx.Simple_name(0)).upper()
        atomId1 = str(ctx.Simple_name(1)).upper()
        seqId2 = int(str(ctx.Integer(1)))
        compId2 = str(ctx.Simple_name(2)).upper()
        atomId2 = str(ctx.Simple_name(3)).upper()
        target = self.numberSelection[0]
        error = abs(self.numberSelection[1])
        weight = self.numberSelection[2]
        orientation = int(str(ctx.Integer(2)))

        self.numberSelection.clear()

        if weight <= 0.0:
            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                f"The relative weight value of '{weight}' must be a positive value.\n"
            return

        if orientation not in self.rdcParameterDict:
            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                f"The orientation '{orientation}' must be defined before you start to describe RDC restraints.\n"
            return

        if seqId1 == self.rdcParameterDict[orientation]['orientation_center_seq_id']:
            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                f"The residue number '{seqId1}' must not be the same as the center of orientation.\n"
            return

        if seqId2 == self.rdcParameterDict[orientation]['orientation_center_seq_id']:
            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                f"The residue number '{seqId2}' must not be the same as the center of orientation.\n"
            return

        target_value = target
        lower_limit = target - error
        upper_limit = target + error

        dstFunc = self.validateRdcRange(weight, orientation, target_value, lower_limit, upper_limit)

        if dstFunc is None:
            return

        if not self.__hasPolySeq:
            return

        chainAssign1 = self.assignCoordPolymerSequence(seqId1, compId1, atomId1)
        chainAssign2 = self.assignCoordPolymerSequence(seqId2, compId2, atomId2)

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
            if self.__debug:
                print(f"subtype={self.__cur_subtype} id={self.rdcRestraints} "
                      f"atom1={atom1} atom2={atom2} {dstFunc}")

    def validateRdcRange(self, weight, orientation, target_value, lower_limit, upper_limit):
        """ Validate RDC value range.
        """

        validRange = True
        dstFunc = {'weight': weight, 'orientation': orientation}

        if target_value is not None:
            if RDC_ERROR_MIN < target_value < RDC_ERROR_MAX:
                dstFunc['target_value'] = f"{target_value:.3f}"
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
                    f"The lower limit value='{lower_limit}' must be within range {RDC_RESTRAINT_ERROR}.\n"

        if upper_limit is not None:
            if RDC_ERROR_MIN < upper_limit <= RDC_ERROR_MAX:
                dstFunc['upper_limit'] = f"{upper_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit}' must be within range {RDC_RESTRAINT_ERROR}.\n"

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
                    f"The lower limit value='{lower_limit}' should be within range {RDC_RESTRAINT_RANGE}.\n"

        if upper_limit is not None:
            if RDC_RANGE_MIN <= upper_limit <= RDC_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit}' should be within range {RDC_RESTRAINT_RANGE}.\n"

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

    # Enter a parse tree produced by CyanaMRParser#pcs_restraints.
    def enterPcs_restraints(self, ctx: CyanaMRParser.Pcs_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'pcs'

        self.pcsParameterDict = {}

    # Exit a parse tree produced by CyanaMRParser#pcs_restraints.
    def exitPcs_restraints(self, ctx: CyanaMRParser.Pcs_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#pcs_parameter.
    def enterPcs_parameter(self, ctx: CyanaMRParser.Pcs_parameterContext):
        orientation = int(str(ctx.Integer(0)))
        magnitude = float(str(ctx.Float(0)))
        rhombicity = float(str(ctx.Float(1)))
        orientationCenterSeqId = int(str(ctx.Integer(1)))

        self.pcsParameterDict[orientation] = {'magnitude': magnitude,
                                              'rhombicity': rhombicity,
                                              'orientation_center_seq_id': orientationCenterSeqId}

        if self.__debug:
            print(f"subtype={self.__cur_subtype} orientation={orientation} "
                  f"parameters={self.pcsParameterDict[orientation]}")

    # Exit a parse tree produced by CyanaMRParser#pcs_parameter.
    def exitPcs_parameter(self, ctx: CyanaMRParser.Pcs_parameterContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#pcs_restraint.
    def enterPcs_restraint(self, ctx: CyanaMRParser.Pcs_restraintContext):  # pylint: disable=unused-argument
        self.pcsRestraints += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by CyanaMRParser#pcs_restraint.
    def exitPcs_restraint(self, ctx: CyanaMRParser.Pcs_restraintContext):  # pylint: disable=unused-argument
        seqId = int(str(ctx.Integer(0)))
        compId = str(ctx.Simple_name(0)).upper()
        atomId = str(ctx.Simple_name(1)).upper()
        target = self.numberSelection[0]
        error = abs(self.numberSelection[1])
        weight = self.numberSelection[2]
        orientation = int(str(ctx.Integer(1)))

        self.numberSelection.clear()

        if weight <= 0.0:
            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                f"The relative weight value of '{weight}' must be a positive value.\n"
            return

        if orientation not in self.pcsParameterDict:
            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                f"The orientation '{orientation}' must be defined before you start to describe PCS restraints.\n"
            return

        if seqId == self.pcsParameterDict[orientation]['orientation_center_seq_id']:
            self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                f"The residue number '{seqId}' must not be the same as the center of orientation.\n"
            return

        target_value = target
        lower_limit = target - error
        upper_limit = target + error

        dstFunc = self.validatePcsRange(weight, orientation, target_value, lower_limit, upper_limit)

        if dstFunc is None:
            return

        if not self.__hasPolySeq:
            return

        chainAssign = self.assignCoordPolymerSequence(seqId, compId, atomId)

        if len(chainAssign) == 0:
            return

        self.selectCoordAtoms(chainAssign, seqId, compId, atomId)

        if len(self.atomSelectionSet) < 1:
            return

        for atom in self.atomSelectionSet[0]:
            if self.__debug:
                print(f"subtype={self.__cur_subtype} id={self.pcsRestraints} "
                      f"atom={atom} {dstFunc}")

    # Enter a parse tree produced by CyanaMRParser#number.
    def enterNumber(self, ctx: CyanaMRParser.NumberContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CyanaMRParser#number.
    def exitNumber(self, ctx: CyanaMRParser.NumberContext):
        if ctx.Float():
            self.numberSelection.append(float(str(ctx.Float())))
        else:
            self.numberSelection.append(float(str(ctx.Integer())))

    def validatePcsRange(self, weight, orientation, target_value, lower_limit, upper_limit):
        """ Validate PCS value range.
        """

        validRange = True
        dstFunc = {'weight': weight, 'orientation': orientation}

        if target_value is not None:
            if PCS_ERROR_MIN < target_value < PCS_ERROR_MAX:
                dstFunc['target_value'] = f"{target_value:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The target value='{target_value}' must be within range {PCS_RESTRAINT_ERROR}.\n"

        if lower_limit is not None:
            if PCS_ERROR_MIN <= lower_limit < PCS_ERROR_MAX:
                dstFunc['lower_limit'] = f"{lower_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The lower limit value='{lower_limit}' must be within range {PCS_RESTRAINT_ERROR}.\n"

        if upper_limit is not None:
            if PCS_ERROR_MIN < upper_limit <= PCS_ERROR_MAX:
                dstFunc['upper_limit'] = f"{upper_limit:.3f}"
            else:
                validRange = False
                self.warningMessage += f"[Range value error] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit}' must be within range {PCS_RESTRAINT_ERROR}.\n"

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

        if not validRange:
            return None

        if target_value is not None:
            if PCS_RANGE_MIN <= target_value <= PCS_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The target value='{target_value}' should be within range {PCS_RESTRAINT_RANGE}.\n"

        if lower_limit is not None:
            if PCS_RANGE_MIN <= lower_limit <= PCS_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The lower limit value='{lower_limit}' should be within range {PCS_RESTRAINT_RANGE}.\n"

        if upper_limit is not None:
            if PCS_RANGE_MIN <= upper_limit <= PCS_RANGE_MAX:
                pass
            else:
                self.warningMessage += f"[Range value warning] {self.__getCurrentRestraint()}"\
                    f"The upper limit value='{upper_limit}' should be within range {PCS_RESTRAINT_RANGE}.\n"

        return dstFunc

    def __getCurrentRestraint(self):
        if self.__cur_subtype == 'dist':
            return f"[Check the {self.distRestraints}th row of distance restraints] "
        if self.__cur_subtype == 'dihed':
            return f"[Check the {self.dihedRestraints}th row of torsion angle restraints] "
        if self.__cur_subtype == 'rdc':
            return f"[Check the {self.rdcRestraints}th row of residual dipolar coupling restraints] "
        if self.__cur_subtype == 'pcs':
            return f"[Check the {self.pcsRestraints}th row of pseudocontact shift restraints] "
        return ''

    def getContentSubtype(self):
        """ Return content subtype of CYANA MR file.
        """

        contentSubtype = {'dist_restraint': self.distRestraints,
                          'dihed_restraint': self.dihedRestraints,
                          'rdc_restraint': self.rdcRestraints,
                          'pcs_restraint': self.pcsRestraints
                          }

        return {k: 1 for k, v in contentSubtype.items() if v > 0}

    def getReasonsForReparsing(self):
        """ Return reasons for re-parsing CYANA MR file.
        """
        return self.reasonsForReParsing

    def isUplDistanceRestraint(self):
        """ Return whether CYANA MR file contains upper limit distance restraints.
        """
        if self.__max_dist_value is None:
            return None
        return self.__max_dist_value > 3.5

# del CyanaMRParser
