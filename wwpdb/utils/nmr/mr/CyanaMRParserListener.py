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

from antlr4 import ParseTreeListener
from wwpdb.utils.nmr.mr.CyanaMRParser import CyanaMRParser
from wwpdb.utils.nmr.mr.ParserListenerUtil import checkCoordinates

from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
from wwpdb.utils.nmr.NEFTranslator.NEFTranslator import NEFTranslator


# This class defines a complete listener for a parse tree produced by CyanaMRParser.
class CyanaMRParserListener(ParseTreeListener):

    __verbose = None
    __lfh = None

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

    __assumeUpperLimit = None

    # CIF reader
    __cR = None

    # data item name for model ID in 'atom_site' category
    __modelNumName = None
    # representative model id
    __representativeModelId = 1

    # data item names for auth_asym_id, auth_seq_id, auth_atom_id in 'atom_site' category
    __authAsymId = None
    __authSeqId = None
    __authAtomId = None

    # polymer sequences in the coordinate file generated by NmrDpUtility.__extractCoordPolymerSequence()
    __polySeq = None

    # current restraint subtype
    __cur_subtype = None

    # collection of atom selection
    atomSelectionSet = None

    warningMessage = ''

    def __init__(self, verbose=True, log=sys.stdout, cR=None, polySeq=None,
                 ccU=None, csStat=None, nefT=None, assumeUpperLimit=True):
        self.__verbose = verbose
        self.__lfh = log
        self.__cR = cR

        dict = checkCoordinates(verbose, log, cR, polySeq)
        self.__modelNumName = dict['model_num_name']
        self.__authAsymId = dict['auth_asym_id']
        self.__authSeqId = dict['auth_seq_id']
        self.__authAtomId = dict['auth_atom_id']
        self.__polySeq = dict['polymer_sequence']

        # CCD accessing utility
        self.__ccU = ChemCompUtil(verbose, log) if ccU is None else ccU

        # BMRB chemical shift statistics
        self.__csStat = BMRBChemShiftStat(verbose, log, self.__ccU) if csStat is None else csStat

        # NEFTranslator
        self.__nefT = NEFTranslator(verbose, log, self.__ccU, self.__csStat) if nefT is None else nefT

        self.__assumeUpperLimit = assumeUpperLimit

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

        self.atomSelectionSet = []

    # Exit a parse tree produced by CyanaMRParser#distance_restraint.
    def exitDistance_restraint(self, ctx: CyanaMRParser.Distance_restraintContext):
        seqId1 = int(str(ctx.Integer(0)))
        compId1 = str(ctx.Simple_name(0)).upper()
        atomId1 = str(ctx.Simple_name(1)).upper()
        seqId2 = int(str(ctx.Integer(1)))
        compId2 = str(ctx.Simple_name(2)).upper()
        atomId2 = str(ctx.Simple_name(3)).upper()

        if self.__assumeUpperLimit:
            upper_limit = float(str(ctx.Float()))
            lower_limit = 1.8  # default value of PDBStat
        else:
            lower_limit = float(str(ctx.Float()))
            upper_limit = 5.5

        target_value = (upper_limit + lower_limit) / 2.0  # default procedure of PDBStat

        chainId1 = []
        chainId2 = []

        for ps in self.__polySeq:
            chainId = ps['chain_id']
            if seqId1 in ps['seq_id']:
                compId = ps['comp_id'][ps['seq_id'].index(seqId1)]
                if compId == compId1:
                    chainId1.append(chainId)
            if seqId2 in ps['seq_id']:
                compId = ps['comp_id'][ps['seq_id'].index(seqId2)]
                if compId == compId2:
                    chainId2.append(chainId)

        if len(chainId1) == 0 or len(chainId2) == 0:
            if len(chainId1) == 0:
                self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                    f"{seqId1}:{compId1}:{atomId1} is not present in the coordinate.\n"
                chainId1 = [self.__polySeq[0]['chain_id']]  # mitigation
            if len(chainId2) == 0:
                self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                    f"{seqId2}:{compId2}:{atomId2} is not present in the coordinate.\n"
                chainId2 = [self.__polySeq[0]['chain_id']]  # mitigation

        _atomId1 = self.__nefT.get_valid_star_atom(compId1, atomId1)[0]
        _atomId2 = self.__nefT.get_valid_star_atom(compId2, atomId2)[0]

        if len(_atomId1) == 0 or len(_atomId2) == 0:
            if len(_atomId1) == 0:
                self.warningMessage += f"[Invalid atom nomenclature] {self.__getCurrentRestraint()}"\
                    f"{seqId1}:{compId1}:{atomId1} is invalid atom nomenclature.\n"
            if len(_atomId2) == 0:
                self.warningMessage += f"[Invalid atom nomenclature] {self.__getCurrentRestraint()}"\
                    f"{seqId2}:{compId2}:{atomId2} is invalid atom nomenclature.\n"
            return

        try:

            atomSelection = []

            for chainId in chainId1:
                seqId = seqId1
                compId = compId1
                for atomId in _atomId1:
                    atomSelection.append({'chain_id': chainId, 'seq_id': seqId, 'comp_id': compId, 'atom_id': atomId})

                    _atom =\
                        self.__cR.getDictListWithFilter('atom_site',
                                                        [{'name': 'label_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                         {'name': 'type_symbol', 'type': 'str'},
                                                         ],
                                                        [{'name': self.__authAsymId, 'type': 'str', 'value': chainId},
                                                         {'name': self.__authSeqId, 'type': 'int', 'value': seqId},
                                                         {'name': self.__authAtomId, 'type': 'str', 'value': atomId},
                                                         {'name': self.__modelNumName, 'type': 'int',
                                                          'value': self.__representativeModelId}
                                                         ])

                    if len(_atom) == 1:
                        pass
                    elif self.__ccU.updateChemCompDict(compId):
                        cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == atomId), None)
                        if cca is not None:
                            self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                                f"{chainId}:{seqId}:{compId}:{atomId} is not present in the coordinate.\n"

            self.atomSelectionSet.append(atomSelection)

            atomSelection = []

            for chainId in chainId2:
                seqId = seqId2
                compId = compId2
                for atomId in _atomId2:
                    atomSelection.append({'chain_id': chainId, 'seq_id': seqId, 'comp_id': compId, 'atom_id': atomId})

                    _atom =\
                        self.__cR.getDictListWithFilter('atom_site',
                                                        [{'name': 'label_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                         {'name': 'type_symbol', 'type': 'str'},
                                                         ],
                                                        [{'name': self.__authAsymId, 'type': 'str', 'value': chainId},
                                                         {'name': self.__authSeqId, 'type': 'int', 'value': seqId},
                                                         {'name': self.__authAtomId, 'type': 'str', 'value': atomId},
                                                         {'name': self.__modelNumName, 'type': 'int',
                                                          'value': self.__representativeModelId}
                                                         ])

                    if len(_atom) == 1:
                        pass
                    elif self.__ccU.updateChemCompDict(compId):
                        cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == atomId), None)
                        if cca is not None:
                            self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                                f"{chainId}:{seqId}:{compId}:{atomId} is not present in the coordinate.\n"

            self.atomSelectionSet.append(atomSelection)

        except Exception as e:
            if self.__verbose:
                self.__lfh.write(f"+CyanaMRParserListener.enterDistance_restraint() ++ Error  - {str(e)}\n")

        for atom_1 in self.atomSelectionSet[0]:
            for atom_2 in self.atomSelectionSet[1]:
                print(f"subtype={self.__cur_subtype} id={self.distRestraints} "
                      f"atom_1={atom_1} atom_2={atom_2} "
                      f"target_value={target_value:.3} lower_limit={lower_limit:.3} upper_limit={upper_limit:.3}")

    # Enter a parse tree produced by CyanaMRParser#torsion_angle_restraints.
    def enterTorsion_angle_restraints(self, ctx: CyanaMRParser.Torsion_angle_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'dihed'

    # Exit a parse tree produced by CyanaMRParser#torsion_angle_restraints.
    def exitTorsion_angle_restraints(self, ctx: CyanaMRParser.Torsion_angle_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#torsion_angle_restraint.
    def enterTorsion_angle_restraint(self, ctx: CyanaMRParser.Torsion_angle_restraintContext):  # pylint: disable=unused-argument
        self.dihedRestraints += 1

    # Exit a parse tree produced by CyanaMRParser#torsion_angle_restraint.
    def exitTorsion_angle_restraint(self, ctx: CyanaMRParser.Torsion_angle_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#rdc_restraints.
    def enterRdc_restraints(self, ctx: CyanaMRParser.Rdc_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'rdc'

    # Exit a parse tree produced by CyanaMRParser#rdc_restraints.
    def exitRdc_restraints(self, ctx: CyanaMRParser.Rdc_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#rdc_parameter.
    def enterRdc_parameter(self, ctx: CyanaMRParser.Rdc_parameterContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CyanaMRParser#rdc_parameter.
    def exitRdc_parameter(self, ctx: CyanaMRParser.Rdc_parameterContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#rdc_restraint.
    def enterRdc_restraint(self, ctx: CyanaMRParser.Rdc_restraintContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1

    # Exit a parse tree produced by CyanaMRParser#rdc_restraint.
    def exitRdc_restraint(self, ctx: CyanaMRParser.Rdc_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#pcs_restraints.
    def enterPcs_restraints(self, ctx: CyanaMRParser.Pcs_restraintsContext):  # pylint: disable=unused-argument
        self.__cur_subtype = 'pcs'

    # Exit a parse tree produced by CyanaMRParser#pcs_restraints.
    def exitPcs_restraints(self, ctx: CyanaMRParser.Pcs_restraintsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#pcs_parameter.
    def enterPcs_parameter(self, ctx: CyanaMRParser.Pcs_parameterContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CyanaMRParser#pcs_parameter.
    def exitPcs_parameter(self, ctx: CyanaMRParser.Pcs_parameterContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CyanaMRParser#pcs_restraint.
    def enterPcs_restraint(self, ctx: CyanaMRParser.Pcs_restraintContext):  # pylint: disable=unused-argument
        self.pcsRestraints += 1

    # Exit a parse tree produced by CyanaMRParser#pcs_restraint.
    def exitPcs_restraint(self, ctx: CyanaMRParser.Pcs_restraintContext):  # pylint: disable=unused-argument
        pass

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

# del CyanaMRParser