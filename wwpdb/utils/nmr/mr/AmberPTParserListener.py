##
# File: AmberPTParserListener.py
# Date: 27-Jan-2022
#
# Updates:
# Generated from AmberPTParser.g4 by ANTLR 4.9
""" ParserLister class for AMBER PT files.
    @author: Masashi Yokochi
"""
import sys
import re

from antlr4 import ParseTreeListener
from wwpdb.utils.nmr.mr.AmberPTParser import AmberPTParser

from wwpdb.utils.nmr.NEFTranslator.NEFTranslator import NEFTranslator
from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
from wwpdb.utils.config.ConfigInfo import getSiteId
from wwpdb.utils.config.ConfigInfoApp import ConfigInfoAppCommon
from wwpdb.utils.nmr.io.ChemCompIo import ChemCompReader


def chunk_string(string, length=4):
    """ Split a string into fixed length chunks.
    """
    return [string[i:i + length] for i in range(0, len(string), length)]


# This class defines a complete listener for a parse tree produced by AmberPTParser.
class AmberPTParserListener(ParseTreeListener):

    __verbose = None
    __lfh = None

    versionStatements = 0
    amberAtomTypeStatements = 0
    angleEquilValueStatements = 0
    angleForceConstantStatements = 0
    anglesIncHydrogenStatements = 0
    anglesWithoutHydrogenStatements = 0
    atomicNumberStatements = 0
    atomNameStatements = 0
    atomTypeIndexStatements = 0
    atomsPerMoleculeStatements = 0
    bondEquilValueStatements = 0
    bondForceConstantStatements = 0
    bondsIncHydrogenStatements = 0
    bondsWithoutHydrogenStatements = 0
    boxDimensionsStatements = 0
    capInfoStatements = 0
    capInfo2Statements = 0
    chargeStatements = 0
    dihedralForceConstantStatements = 0
    dihedralPeriodicityStatements = 0
    dihedralPhaseStatements = 0
    dihedralsIncHydrogenStatements = 0
    dihedralsWithoutHydrogenStatements = 0
    excludedAtomsListStatements = 0
    hbcutStatements = 0
    hbondAcoefStatements = 0
    hbondBcoefStatements = 0
    ipolStatements = 0
    irotatStatements = 0
    joinArrayStatements = 0
    lennardJonesAcoefStatements = 0
    lennardJonesBcoefStatements = 0
    massStatements = 0
    nonbondedParmIndexStatements = 0
    numberExcludedAtomsStatements = 0
    pointersStatements = 0
    polarizabilityStatements = 0
    radiiStatements = 0
    radiusSetStatements = 0
    residueLabelStatements = 0
    residuePointerStatements = 0
    sceeScaleFactorStatements = 0
    scnbScaleFactorStatements = 0
    screenStatements = 0
    soltyStatements = 0
    solventPointersStatements = 0
    titleStatements = 0
    treeChainClassificationStatements = 0

    # loop categories
    lpCategories = {'poly_seq': 'pdbx_poly_seq_scheme',
                    'non_poly': 'pdbx_nonpoly_scheme',
                    'coordinate': 'atom_site',
                    'poly_seq_alias': 'ndb_poly_seq_scheme',
                    'non_poly_alias': 'ndb_nonpoly_scheme'
                    }

    # key items of loop
    keyItems = {'poly_seq': [{'name': 'asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                             {'name': 'seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                             {'name': 'mon_id', 'type': 'str', 'alt_name': 'comp_id'},
                             {'name': 'pdb_strand_id', 'type': 'str', 'alt_name': 'auth_chain_id'}
                             ],
                'poly_seq_alias': [{'name': 'id', 'type': 'str', 'alt_name': 'chain_id'},
                                   {'name': 'seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                   {'name': 'mon_id', 'type': 'str', 'alt_name': 'comp_id'}
                                   ],
                'non_poly': [{'name': 'asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                             {'name': 'pdb_seq_num', 'type': 'int', 'alt_name': 'seq_id'},
                             {'name': 'mon_id', 'type': 'str', 'alt_name': 'comp_id'},
                             {'name': 'pdb_strand_id', 'type': 'str', 'alt_name': 'auth_chain_id'}
                             ],
                'non_poly_alias': [{'name': 'asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                   {'name': 'pdb_num', 'type': 'int', 'alt_name': 'seq_id'},
                                   {'name': 'mon_id', 'type': 'str', 'alt_name': 'comp_id'}
                                   ],
                'coordinate': [{'name': 'label_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                               {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                               {'name': 'auth_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                               {'name': 'pdbx_PDB_model_num', 'type': 'int', 'alt_name': 'model_id'}
                               ],
                'coordinate_alias': [{'name': 'label_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                     {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                     {'name': 'auth_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                     {'name': 'ndb_model', 'type': 'int', 'alt_name': 'model_id'}
                                     ],
                'coordinate_ins': [{'name': 'label_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                   {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                   {'name': 'auth_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                   {'name': 'pdbx_PDB_ins_code', 'type': 'str', 'alt_name': 'ins_code', 'default': '?'},
                                   {'name': 'label_seq_id', 'type': 'str', 'alt_name': 'label_seq_id', 'default': '.'},
                                   {'name': 'pdbx_PDB_model_num', 'type': 'int', 'alt_name': 'model_id'}
                                   ],
                'coordinate_ins_alias': [{'name': 'label_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                         {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                         {'name': 'auth_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                         {'name': 'ndb_ins_code', 'type': 'str', 'alt_name': 'ins_code', 'default': '?'},
                                         {'name': 'label_seq_id', 'type': 'str', 'alt_name': 'label_seq_id', 'default': '.'},
                                         {'name': 'ndb_model', 'type': 'int', 'alt_name': 'model_id'}
                                         ]
                }

    # NEFTranslator
    __nefT = None

    # BMRB chemical shift statistics
    __csStat = None

    # ChemComp reader
    __ccR = None

    __assumeUpperLimit = None

    __lastCompId = None
    __lastCompIdTest = False
    # __lastChemCompDict = None
    __lastChemCompAtoms = None
    # __lastChemCompBonds = None

    __chemCompAtomDict = None
    # __chemCompBondDict = None

    __ccaAtomId = None
    # __ccaAromaticFlag = None
    # __ccaLeavingAtomFlag = None
    # __ccaTypeSymbol = None

    # __ccbAtomId1 = None
    # __ccbAtomId2 = Non
    # __ccbAromaticFlag = None

    # CIF reader
    __cR = None

    # data item name for model ID in 'atom_site' category
    __modelNumName = None
    # representative model id
    __representativeModelId = 1
    # total number of models
    # __totalModels = 0

    # data item names for auth_asym_id, auth_seq_id, auth_atom_id in 'atom_site' category
    __authAsymId = None
    __authSeqId = None
    __authAtomId = None

    # polymer sequences in the coordinate file generated by NmrDpUtility.__extractCoordPolymerSequence()
    __polySeq = None

    # residue_label
    __polySeqInMR = None

    # residue label = None
    __residueLabel = None

    # residue_pointer
    __residuePointer = None

    # atom_name
    __atomName = None

    # AMBER atom number dictionary
    __atomNumberDict = None

    # current restraint subtype
    __cur_subtype = None

    # Fortran format
    __a_format_pat = re.compile(r'\((\d+)[aA](\d+)\)$')
    __i_format_pat = re.compile(r'\((\d+)[iI](\d+)\)$')
    __i_format_pat = re.compile(r'\((\d+)[eE](\d+)\.?(\d+)?\)$')

    __cur_column_len = None
    __cur_word_len = None

    warningMessage = ''

    def __init__(self, verbose=True, log=sys.stdout, cR=None, polySeq=None, assumeUpperLimit=True):
        self.__verbose = verbose
        self.__lfh = log
        self.__cR = cR
        self.__assumeUpperLimit = assumeUpperLimit

        try:

            self.__modelNumName = 'pdbx_PDB_model_num' if self.__cR.hasItem('atom_site', 'pdbx_PDB_model_num') else 'ndb_model'

            modelIds = self.__cR.getDictListWithFilter('atom_site',
                                                       [{'name': self.__modelNumName, 'type': 'int', 'alt_name': 'model_id'}
                                                        ])

            if len(modelIds) > 0:
                modelIds = set(dict['model_id'] for dict in modelIds)

                self.__representativeModelId = min(modelIds)
                # self.__totalModels = len(modelIds)

            self.__authAsymId = 'pdbx_auth_asym_id' if self.__cR.hasItem('atom_site', 'pdbx_auth_asym_id') else 'auth_asym_id'
            self.__authSeqId = 'pdbx_auth_seq_id' if self.__cR.hasItem('atom_site', 'pdbx_auth_seq_id') else 'auth_seq_id'
            self.__authAtomId = 'pdbx_auth_atom_name' if self.__cR.hasItem('atom_site', 'pdbx_auth_atom_name') else 'auth_atom_id'

        except Exception as e:

            if self.__verbose:
                self.__lfh.write(f"+AmberPTParserListener.__init__() ++ Error  - {str(e)}\n")

        if polySeq is not None:
            self.__polySeq = polySeq

        else:

            contetSubtype = 'poly_seq'

            alias = False
            lpCategory = self.lpCategories[contetSubtype]
            keyItems = self.keyItems[contetSubtype]

            if not self.__cR.hasCategory(lpCategory):
                alias = True
                lpCategory = self.lpCategories[contetSubtype + '_alias']
                keyItems = self.keyItems[contetSubtype + '_alias']

            try:

                try:
                    self.__polySeq = self.__cR.getPolymerSequence(lpCategory, keyItems,
                                                                  withStructConf=True, alias=alias)
                except KeyError:  # pdbx_PDB_ins_code throws KeyError
                    if contetSubtype + ('_ins_alias' if alias else '_ins') in self.keyItems:
                        keyItems = self.keyItems[contetSubtype + ('_ins_alias' if alias else '_ins')]
                        self.__polySeq = self.__cR.getPolymerSequence(lpCategory, keyItems,
                                                                      withStructConf=True, alias=alias)
                    else:
                        self.__polySeq = []

            except Exception as e:
                if self.__verbose:
                    self.__lfh.write(f"+AmberPTParserListener.__init__() ++ Error - {str(e)}\n")

        # NEFTranslator
        self.__nefT = NEFTranslator()

        if self.__nefT is None:
            raise IOError("+AmberPTParserListener.__init__() ++ Error  - NEFTranslator is not available.")

        # BMRB chemical shift statistics
        self.__csStat = BMRBChemShiftStat()

        if not self.__csStat.isOk():
            raise IOError("+AmberPTParserListener.__init__() ++ Error  - BMRBChemShiftStat is not available.")

        # CCD accessing utility
        __cICommon = ConfigInfoAppCommon(getSiteId())
        __ccCvsPath = __cICommon.get_site_cc_cvs_path()

        self.__ccR = ChemCompReader(verbose, log)
        self.__ccR.setCachePath(__ccCvsPath)

        # taken from wwpdb.apps.ccmodule.io.ChemCompIo
        self.__chemCompAtomDict = [
            ('_chem_comp_atom.comp_id', '%s', 'str', ''),
            ('_chem_comp_atom.atom_id', '%s', 'str', ''),
            ('_chem_comp_atom.alt_atom_id', '%s', 'str', ''),
            ('_chem_comp_atom.type_symbol', '%s', 'str', ''),
            ('_chem_comp_atom.charge', '%s', 'str', ''),
            ('_chem_comp_atom.pdbx_align', '%s', 'str', ''),
            ('_chem_comp_atom.pdbx_aromatic_flag', '%s', 'str', ''),
            ('_chem_comp_atom.pdbx_leaving_atom_flag', '%s', 'str', ''),
            ('_chem_comp_atom.pdbx_stereo_config', '%s', 'str', ''),
            ('_chem_comp_atom.model_Cartn_x', '%s', 'str', ''),
            ('_chem_comp_atom.model_Cartn_y', '%s', 'str', ''),
            ('_chem_comp_atom.model_Cartn_z', '%s', 'str', ''),
            ('_chem_comp_atom.pdbx_model_Cartn_x_ideal', '%s', 'str', ''),
            ('_chem_comp_atom.pdbx_model_Cartn_y_ideal', '%s', 'str', ''),
            ('_chem_comp_atom.pdbx_model_Cartn_z_ideal', '%s', 'str', ''),
            ('_chem_comp_atom.pdbx_component_atom_id', '%s', 'str', ''),
            ('_chem_comp_atom.pdbx_component_comp_id', '%s', 'str', ''),
            ('_chem_comp_atom.pdbx_ordinal', '%s', 'str', '')
        ]

        atomId = next(d for d in self.__chemCompAtomDict if d[0] == '_chem_comp_atom.atom_id')
        self.__ccaAtomId = self.__chemCompAtomDict.index(atomId)

    def __updateChemCompDict(self, compId):
        """ Update CCD information for a given comp_id.
            @return: True for successfully update CCD information or False for the case a given comp_id does not exist in CCD
        """

        compId = compId.upper()

        if compId != self.__lastCompId:
            self.__lastCompIdTest = False if '_' in compId else self.__ccR.setCompId(compId)
            self.__lastCompId = compId

            if self.__lastCompIdTest:
                # self.__lastChemCompDict = self.__ccR.getChemCompDict()
                self.__lastChemCompAtoms = self.__ccR.getAtomList()
                # self.__lastChemCompBonds = self.__ccR.getBonds()

        return self.__lastCompIdTest

    # Enter a parse tree produced by AmberPTParser#amber_pt.
    def enterAmber_pt(self, ctx: AmberPTParser.Amber_ptContext):  # pylint: disable=unused-argument
        self.__atomNumberDict = {}
        self.__polySeqInMR = []

    # Exit a parse tree produced by AmberPTParser#amber_pt.
    def exitAmber_pt(self, ctx: AmberPTParser.Amber_ptContext):  # pylint: disable=unused-argument
        residuePointer2 = [resPoint - 1 for resPoint in self.__residuePointer]
        del residuePointer2[0]
        residuePointer2.append(self.__residuePointer[-1] + 1000)

        chainId = self.__polySeq[0]['chain_id']

        for atomNum, atomName in enumerate(self.__atomName, start=1):
            seqId = next(resNum for resNum, (atomNumBegin, atomNumEnd)
                         in enumerate(zip(self.__residuePointer, residuePointer2), start=1)
                         if atomNum >= atomNumBegin and atomNum <= atomNumEnd)
            compId = self.__residueLabel[seqId - 1]
            self.__atomNumberDict[atomNum] = {'chain_id': chainId,
                                              'seq_id': seqId,
                                              'comp_id': compId,
                                              'atom_id': atomName}

        self.__polySeqInMR.append({'chain_id': chainId,
                                   'seq_id': list(range(1, len(self.__residueLabel) + 1)),
                                   'comp_id': self.__residueLabel})

        print(self.__polySeq)
        print(self.__polySeqInMR)

        if len(self.warningMessage) == 0:
            self.warningMessage = None
        else:
            self.warningMessage = self.warningMessage[0:-1]

    # Enter a parse tree produced by AmberPTParser#version_statement.
    def enterVersion_statement(self, ctx: AmberPTParser.Version_statementContext):  # pylint: disable=unused-argument
        self.versionStatements += 1

    # Exit a parse tree produced by AmberPTParser#version_statement.
    def exitVersion_statement(self, ctx: AmberPTParser.Version_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#amber_atom_type_statement.
    def enterAmber_atom_type_statement(self, ctx: AmberPTParser.Amber_atom_type_statementContext):  # pylint: disable=unused-argument
        self.amberAtomTypeStatements += 1

    # Exit a parse tree produced by AmberPTParser#amber_atom_type_statement.
    def exitAmber_atom_type_statement(self, ctx: AmberPTParser.Amber_atom_type_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#angle_equil_value_statement.
    def enterAngle_equil_value_statement(self, ctx: AmberPTParser.Angle_equil_value_statementContext):  # pylint: disable=unused-argument
        self.angleEquilValueStatements += 1

    # Exit a parse tree produced by AmberPTParser#angle_equil_value_statement.
    def exitAngle_equil_value_statement(self, ctx: AmberPTParser.Angle_equil_value_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#angle_force_constant_statement.
    def enterAngle_force_constant_statement(self, ctx: AmberPTParser.Angle_force_constant_statementContext):  # pylint: disable=unused-argument
        self.angleForceConstantStatements += 1

    # Exit a parse tree produced by AmberPTParser#angle_force_constant_statement.
    def exitAngle_force_constant_statement(self, ctx: AmberPTParser.Angle_force_constant_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#angles_inc_hydrogen_statement.
    def enterAngles_inc_hydrogen_statement(self, ctx: AmberPTParser.Angles_inc_hydrogen_statementContext):  # pylint: disable=unused-argument
        self.anglesIncHydrogenStatements += 1

    # Exit a parse tree produced by AmberPTParser#angles_inc_hydrogen_statement.
    def exitAngles_inc_hydrogen_statement(self, ctx: AmberPTParser.Angles_inc_hydrogen_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#angles_without_hydrogen_statement.
    def enterAngles_without_hydrogen_statement(self, ctx: AmberPTParser.Angles_without_hydrogen_statementContext):  # pylint: disable=unused-argument
        self.anglesWithoutHydrogenStatements += 1

    # Exit a parse tree produced by AmberPTParser#angles_without_hydrogen_statement.
    def exitAngles_without_hydrogen_statement(self, ctx: AmberPTParser.Angles_without_hydrogen_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#atomic_number_statement.
    def enterAtomic_number_statement(self, ctx: AmberPTParser.Atomic_number_statementContext):  # pylint: disable=unused-argument
        self.atomicNumberStatements += 1

    # Exit a parse tree produced by AmberPTParser#atomic_number_statement.
    def exitAtomic_number_statement(self, ctx: AmberPTParser.Atomic_number_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#atom_name_statement.
    def enterAtom_name_statement(self, ctx: AmberPTParser.Atom_name_statementContext):  # pylint: disable=unused-argument
        self.atomNameStatements += 1

    # Exit a parse tree produced by AmberPTParser#atom_name_statement.
    def exitAtom_name_statement(self, ctx: AmberPTParser.Atom_name_statementContext):  # pylint: disable=unused-argument
        atomIdList = []
        i = 0
        while ctx.Simple_name(i):
            chunk = chunk_string(str(ctx.Simple_name(i)).upper(), self.__cur_word_len)
            atomIdList.extend(chunk)
            i += 1

        self.__atomName = atomIdList

    # Enter a parse tree produced by AmberPTParser#atom_type_index_statement.
    def enterAtom_type_index_statement(self, ctx: AmberPTParser.Atom_type_index_statementContext):  # pylint: disable=unused-argument
        self.atomTypeIndexStatements += 1

    # Exit a parse tree produced by AmberPTParser#atom_type_index_statement.
    def exitAtom_type_index_statement(self, ctx: AmberPTParser.Atom_type_index_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#atoms_per_molecule_statement.
    def enterAtoms_per_molecule_statement(self, ctx: AmberPTParser.Atoms_per_molecule_statementContext):  # pylint: disable=unused-argument
        self.atomsPerMoleculeStatements += 1

    # Exit a parse tree produced by AmberPTParser#atoms_per_molecule_statement.
    def exitAtoms_per_molecule_statement(self, ctx: AmberPTParser.Atoms_per_molecule_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#bond_equil_value_statement.
    def enterBond_equil_value_statement(self, ctx: AmberPTParser.Bond_equil_value_statementContext):  # pylint: disable=unused-argument
        self.bondEquilValueStatements += 1

    # Exit a parse tree produced by AmberPTParser#bond_equil_value_statement.
    def exitBond_equil_value_statement(self, ctx: AmberPTParser.Bond_equil_value_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#bond_force_constant_statement.
    def enterBond_force_constant_statement(self, ctx: AmberPTParser.Bond_force_constant_statementContext):  # pylint: disable=unused-argument
        self.bondForceConstantStatements += 1

    # Exit a parse tree produced by AmberPTParser#bond_force_constant_statement.
    def exitBond_force_constant_statement(self, ctx: AmberPTParser.Bond_force_constant_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#bonds_inc_hydrogen_statement.
    def enterBonds_inc_hydrogen_statement(self, ctx: AmberPTParser.Bonds_inc_hydrogen_statementContext):  # pylint: disable=unused-argument
        self.bondsIncHydrogenStatements += 1

    # Exit a parse tree produced by AmberPTParser#bonds_inc_hydrogen_statement.
    def exitBonds_inc_hydrogen_statement(self, ctx: AmberPTParser.Bonds_inc_hydrogen_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#bonds_without_hydrogen_statement.
    def enterBonds_without_hydrogen_statement(self, ctx: AmberPTParser.Bonds_without_hydrogen_statementContext):  # pylint: disable=unused-argument
        self.bondsWithoutHydrogenStatements += 1

    # Exit a parse tree produced by AmberPTParser#bonds_without_hydrogen_statement.
    def exitBonds_without_hydrogen_statement(self, ctx: AmberPTParser.Bonds_without_hydrogen_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#box_dimensions_statement.
    def enterBox_dimensions_statement(self, ctx: AmberPTParser.Box_dimensions_statementContext):  # pylint: disable=unused-argument
        self.boxDimensionsStatements += 1

    # Exit a parse tree produced by AmberPTParser#box_dimensions_statement.
    def exitBox_dimensions_statement(self, ctx: AmberPTParser.Box_dimensions_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#cap_info_statement.
    def enterCap_info_statement(self, ctx: AmberPTParser.Cap_info_statementContext):  # pylint: disable=unused-argument
        self.capInfoStatements += 1

    # Exit a parse tree produced by AmberPTParser#cap_info_statement.
    def exitCap_info_statement(self, ctx: AmberPTParser.Cap_info_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#cap_info2_statement.
    def enterCap_info2_statement(self, ctx: AmberPTParser.Cap_info2_statementContext):  # pylint: disable=unused-argument
        self.capInfo2Statements += 1

    # Exit a parse tree produced by AmberPTParser#cap_info2_statement.
    def exitCap_info2_statement(self, ctx: AmberPTParser.Cap_info2_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#charge_statement.
    def enterCharge_statement(self, ctx: AmberPTParser.Charge_statementContext):  # pylint: disable=unused-argument
        self.chargeStatements += 1

    # Exit a parse tree produced by AmberPTParser#charge_statement.
    def exitCharge_statement(self, ctx: AmberPTParser.Charge_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#dihedral_force_constant_statement.
    def enterDihedral_force_constant_statement(self, ctx: AmberPTParser.Dihedral_force_constant_statementContext):  # pylint: disable=unused-argument
        self.dihedralForceConstantStatements += 1

    # Exit a parse tree produced by AmberPTParser#dihedral_force_constant_statement.
    def exitDihedral_force_constant_statement(self, ctx: AmberPTParser.Dihedral_force_constant_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#dihedral_periodicity_statement.
    def enterDihedral_periodicity_statement(self, ctx: AmberPTParser.Dihedral_periodicity_statementContext):  # pylint: disable=unused-argument
        self.dihedralPeriodicityStatements += 1

    # Exit a parse tree produced by AmberPTParser#dihedral_periodicity_statement.
    def exitDihedral_periodicity_statement(self, ctx: AmberPTParser.Dihedral_periodicity_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#dihedral_phase_statement.
    def enterDihedral_phase_statement(self, ctx: AmberPTParser.Dihedral_phase_statementContext):  # pylint: disable=unused-argument
        self.dihedralPhaseStatements += 1

    # Exit a parse tree produced by AmberPTParser#dihedral_phase_statement.
    def exitDihedral_phase_statement(self, ctx: AmberPTParser.Dihedral_phase_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#dihedrals_inc_hydrogen_statement.
    def enterDihedrals_inc_hydrogen_statement(self, ctx: AmberPTParser.Dihedrals_inc_hydrogen_statementContext):  # pylint: disable=unused-argument
        self.dihedralsIncHydrogenStatements += 1

    # Exit a parse tree produced by AmberPTParser#dihedrals_inc_hydrogen_statement.
    def exitDihedrals_inc_hydrogen_statement(self, ctx: AmberPTParser.Dihedrals_inc_hydrogen_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#dihedrals_without_hydrogen_statement.
    def enterDihedrals_without_hydrogen_statement(self, ctx: AmberPTParser.Dihedrals_without_hydrogen_statementContext):  # pylint: disable=unused-argument
        self.dihedralsWithoutHydrogenStatements += 1

    # Exit a parse tree produced by AmberPTParser#dihedrals_without_hydrogen_statement.
    def exitDihedrals_without_hydrogen_statement(self, ctx: AmberPTParser.Dihedrals_without_hydrogen_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#excluded_atoms_list_statement.
    def enterExcluded_atoms_list_statement(self, ctx: AmberPTParser.Excluded_atoms_list_statementContext):  # pylint: disable=unused-argument
        self.excludedAtomsListStatements += 1

    # Exit a parse tree produced by AmberPTParser#excluded_atoms_list_statement.
    def exitExcluded_atoms_list_statement(self, ctx: AmberPTParser.Excluded_atoms_list_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#hbcut_statement.
    def enterHbcut_statement(self, ctx: AmberPTParser.Hbcut_statementContext):  # pylint: disable=unused-argument
        self.hbcutStatements += 1

    # Exit a parse tree produced by AmberPTParser#hbcut_statement.
    def exitHbcut_statement(self, ctx: AmberPTParser.Hbcut_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#hbond_acoef_statement.
    def enterHbond_acoef_statement(self, ctx: AmberPTParser.Hbond_acoef_statementContext):  # pylint: disable=unused-argument
        self.hbondAcoefStatements += 1

    # Exit a parse tree produced by AmberPTParser#hbond_acoef_statement.
    def exitHbond_acoef_statement(self, ctx: AmberPTParser.Hbond_acoef_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#hbond_bcoef_statement.
    def enterHbond_bcoef_statement(self, ctx: AmberPTParser.Hbond_bcoef_statementContext):  # pylint: disable=unused-argument
        self.hbondBcoefStatements += 1

    # Exit a parse tree produced by AmberPTParser#hbond_bcoef_statement.
    def exitHbond_bcoef_statement(self, ctx: AmberPTParser.Hbond_bcoef_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#ipol_statement.
    def enterIpol_statement(self, ctx: AmberPTParser.Ipol_statementContext):  # pylint: disable=unused-argument
        self.ipolStatements += 1

    # Exit a parse tree produced by AmberPTParser#ipol_statement.
    def exitIpol_statement(self, ctx: AmberPTParser.Ipol_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#irotat_statement.
    def enterIrotat_statement(self, ctx: AmberPTParser.Irotat_statementContext):  # pylint: disable=unused-argument
        self.irotatStatements += 1

    # Exit a parse tree produced by AmberPTParser#irotat_statement.
    def exitIrotat_statement(self, ctx: AmberPTParser.Irotat_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#join_array_statement.
    def enterJoin_array_statement(self, ctx: AmberPTParser.Join_array_statementContext):  # pylint: disable=unused-argument
        self.joinArrayStatements += 1

    # Exit a parse tree produced by AmberPTParser#join_array_statement.
    def exitJoin_array_statement(self, ctx: AmberPTParser.Join_array_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#lennard_jones_acoef_statement.
    def enterLennard_jones_acoef_statement(self, ctx: AmberPTParser.Lennard_jones_acoef_statementContext):  # pylint: disable=unused-argument
        self.lennardJonesAcoefStatements += 1

    # Exit a parse tree produced by AmberPTParser#lennard_jones_acoef_statement.
    def exitLennard_jones_acoef_statement(self, ctx: AmberPTParser.Lennard_jones_acoef_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#lennard_jones_bcoef_statement.
    def enterLennard_jones_bcoef_statement(self, ctx: AmberPTParser.Lennard_jones_bcoef_statementContext):  # pylint: disable=unused-argument
        self.lennardJonesBcoefStatements += 1

    # Exit a parse tree produced by AmberPTParser#lennard_jones_bcoef_statement.
    def exitLennard_jones_bcoef_statement(self, ctx: AmberPTParser.Lennard_jones_bcoef_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#mass_statement.
    def enterMass_statement(self, ctx: AmberPTParser.Mass_statementContext):  # pylint: disable=unused-argument
        self.massStatements += 1

    # Exit a parse tree produced by AmberPTParser#mass_statement.
    def exitMass_statement(self, ctx: AmberPTParser.Mass_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#nonbonded_parm_index_statement.
    def enterNonbonded_parm_index_statement(self, ctx: AmberPTParser.Nonbonded_parm_index_statementContext):  # pylint: disable=unused-argument
        self.nonbondedParmIndexStatements += 1

    # Exit a parse tree produced by AmberPTParser#nonbonded_parm_index_statement.
    def exitNonbonded_parm_index_statement(self, ctx: AmberPTParser.Nonbonded_parm_index_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#number_excluded_atoms_statement.
    def enterNumber_excluded_atoms_statement(self, ctx: AmberPTParser.Number_excluded_atoms_statementContext):  # pylint: disable=unused-argument
        self.numberExcludedAtomsStatements += 1

    # Exit a parse tree produced by AmberPTParser#number_excluded_atoms_statement.
    def exitNumber_excluded_atoms_statement(self, ctx: AmberPTParser.Number_excluded_atoms_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#pointers_statement.
    def enterPointers_statement(self, ctx: AmberPTParser.Pointers_statementContext):  # pylint: disable=unused-argument
        self.pointersStatements += 1

    # Exit a parse tree produced by AmberPTParser#pointers_statement.
    def exitPointers_statement(self, ctx: AmberPTParser.Pointers_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#polarizability_statement.
    def enterPolarizability_statement(self, ctx: AmberPTParser.Polarizability_statementContext):  # pylint: disable=unused-argument
        self.polarizabilityStatements += 1

    # Exit a parse tree produced by AmberPTParser#polarizability_statement.
    def exitPolarizability_statement(self, ctx: AmberPTParser.Polarizability_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#radii_statement.
    def enterRadii_statement(self, ctx: AmberPTParser.Radii_statementContext):  # pylint: disable=unused-argument
        self.radiiStatements += 1

    # Exit a parse tree produced by AmberPTParser#radii_statement.
    def exitRadii_statement(self, ctx: AmberPTParser.Radii_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#radius_set_statement.
    def enterRadius_set_statement(self, ctx: AmberPTParser.Radius_set_statementContext):  # pylint: disable=unused-argument
        self.radiusSetStatements += 1

    # Exit a parse tree produced by AmberPTParser#radius_set_statement.
    def exitRadius_set_statement(self, ctx: AmberPTParser.Radius_set_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#residue_label_statement.
    def enterResidue_label_statement(self, ctx: AmberPTParser.Residue_label_statementContext):  # pylint: disable=unused-argument
        self.residueLabelStatements += 1

        self.__residueLabel = []

    # Exit a parse tree produced by AmberPTParser#residue_label_statement.
    def exitResidue_label_statement(self, ctx: AmberPTParser.Residue_label_statementContext):
        i = 0
        while ctx.Simple_name(i):
            chunk = chunk_string(str(ctx.Simple_name(i)).upper(), self.__cur_word_len)
            self.__residueLabel.extend(chunk)
            i += 1

    # Enter a parse tree produced by AmberPTParser#residue_pointer_statement.
    def enterResidue_pointer_statement(self, ctx: AmberPTParser.Residue_pointer_statementContext):  # pylint: disable=unused-argument
        self.residuePointerStatements += 1

        self.__residuePointer = []

    # Exit a parse tree produced by AmberPTParser#residue_pointer_statement.
    def exitResidue_pointer_statement(self, ctx: AmberPTParser.Residue_pointer_statementContext):
        i = 0
        while ctx.Integer(i):
            self.__residuePointer.append(int(str(ctx.Integer(i))))
            i += 1

    # Enter a parse tree produced by AmberPTParser#scee_scale_factor_statement.
    def enterScee_scale_factor_statement(self, ctx: AmberPTParser.Scee_scale_factor_statementContext):  # pylint: disable=unused-argument
        self.sceeScaleFactorStatements += 1

    # Exit a parse tree produced by AmberPTParser#scee_scale_factor_statement.
    def exitScee_scale_factor_statement(self, ctx: AmberPTParser.Scee_scale_factor_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#scnb_scale_factor_statement.
    def enterScnb_scale_factor_statement(self, ctx: AmberPTParser.Scnb_scale_factor_statementContext):  # pylint: disable=unused-argument
        self.scnbScaleFactorStatements += 1

    # Exit a parse tree produced by AmberPTParser#scnb_scale_factor_statement.
    def exitScnb_scale_factor_statement(self, ctx: AmberPTParser.Scnb_scale_factor_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#screen_statement.
    def enterScreen_statement(self, ctx: AmberPTParser.Screen_statementContext):  # pylint: disable=unused-argument
        self.screenStatements += 1

    # Exit a parse tree produced by AmberPTParser#screen_statement.
    def exitScreen_statement(self, ctx: AmberPTParser.Screen_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#solty_statement.
    def enterSolty_statement(self, ctx: AmberPTParser.Solty_statementContext):  # pylint: disable=unused-argument
        self.soltyStatements += 1

    # Exit a parse tree produced by AmberPTParser#solty_statement.
    def exitSolty_statement(self, ctx: AmberPTParser.Solty_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#solvent_pointers_statement.
    def enterSolvent_pointers_statement(self, ctx: AmberPTParser.Solvent_pointers_statementContext):  # pylint: disable=unused-argument
        self.solventPointersStatements += 1

    # Exit a parse tree produced by AmberPTParser#solvent_pointers_statement.
    def exitSolvent_pointers_statement(self, ctx: AmberPTParser.Solvent_pointers_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#title_statement.
    def enterTitle_statement(self, ctx: AmberPTParser.Title_statementContext):  # pylint: disable=unused-argument
        self.titleStatements += 1

    # Exit a parse tree produced by AmberPTParser#title_statement.
    def exitTitle_statement(self, ctx: AmberPTParser.Title_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#tree_chain_classification_statement.
    def enterTree_chain_classification_statement(self, ctx: AmberPTParser.Tree_chain_classification_statementContext):  # pylint: disable=unused-argument
        self.treeChainClassificationStatements += 1

    # Exit a parse tree produced by AmberPTParser#tree_chain_classification_statement.
    def exitTree_chain_classification_statement(self, ctx: AmberPTParser.Tree_chain_classification_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by AmberPTParser#format_function.
    def enterFormat_function(self, ctx: AmberPTParser.Format_functionContext):
        try:
            if ctx.Fortran_format_A():
                g = self.__a_format_pat.search(str(ctx.Fortran_format_A())).groups()
                self.__cur_column_len = int(g[0])
                self.__cur_word_len = int(g[1])
            elif ctx.Fortran_format_I():
                g = self.__i_format_pat.search(str(ctx.Fortran_format_I())).groups()
                self.__cur_column_len = int(g[0])
                self.__cur_word_len = int(g[1])
            else:
                g = self.__e_format_pat.search(str(ctx.Fortran_format_E())).groups()
                self.__cur_column_len = int(g[0])
                self.__cur_word_len = int(g[1])
        except AttributeError:
            self.__cur_column_len = self.__cur_word_len = None

    # Exit a parse tree produced by AmberPTParser#format_function.
    def exitFormat_function(self, ctx: AmberPTParser.Format_functionContext):  # pylint: disable=unused-argument
        pass

    def getContentSubtype(self):
        """ Return content subtype of AMBER PT file.
        """

        contentSubtype = {'version': self.versionStatements,
                          'amber_atom_type': self.amberAtomTypeStatements,
                          'angle_equil_value': self.angleEquilValueStatements,
                          'angle_force_constant': self.angleForceConstantStatements,
                          'angles_inc_hydrogen': self.anglesIncHydrogenStatements,
                          'angles_without_hydrogen': self.anglesWithoutHydrogenStatements,
                          'atomic_number': self.atomicNumberStatements,
                          'atom_name': self.atomNameStatements,
                          'atom_type_index': self.atomTypeIndexStatements,
                          'atoms_per_molecule': self.atomsPerMoleculeStatements,
                          'bond_equil_value': self.bondEquilValueStatements,
                          'bond_force_constant': self.bondForceConstantStatements,
                          'bonds_inc_hydrogen': self.bondsIncHydrogenStatements,
                          'bonds_without_hydrogen': self.bondsWithoutHydrogenStatements,
                          'box_dimensions': self.boxDimensionsStatements,
                          'cap_info': self.capInfoStatements,
                          'cap_info2': self.capInfo2Statements,
                          'charge': self.chargeStatements,
                          'dihedral_force_constant': self.dihedralForceConstantStatements,
                          'dihedral_periodicity': self.dihedralPeriodicityStatements,
                          'dihedral_phase': self.dihedralPhaseStatements,
                          'dihedrals_inc_hydrogen': self.dihedralsIncHydrogenStatements,
                          'dihedrals_without_hydrogen': self.dihedralsWithoutHydrogenStatements,
                          'excluded_atoms_list': self.excludedAtomsListStatements,
                          'hbcut': self.hbcutStatements,
                          'hbond_acoef': self.hbondAcoefStatements,
                          'hbond_bcoef': self.hbondBcoefStatements,
                          'ipol': self.ipolStatements,
                          'irotat': self.irotatStatements,
                          'join_array': self.joinArrayStatements,
                          'lennard_jones_acoef': self.lennardJonesAcoefStatements,
                          'lennard_jones_bcoef': self.lennardJonesBcoefStatements,
                          'mass': self.massStatements,
                          'nonbonded_parm_index': self.nonbondedParmIndexStatements,
                          'number_excluded_atoms': self.numberExcludedAtomsStatements,
                          'pointers': self.pointersStatements,
                          'polarizability': self.polarizabilityStatements,
                          'radii': self.radiiStatements,
                          'radius_set': self.radiusSetStatements,
                          'residue_label': self.residueLabelStatements,
                          'residue_pointer': self.residuePointerStatements,
                          'scee_scale_factor': self.sceeScaleFactorStatements,
                          'scnb_scale_factor': self.scnbScaleFactorStatements,
                          'screen': self.screenStatements,
                          'solty': self.soltyStatements,
                          'solvent_pointers': self.solventPointersStatements,
                          'title': self.titleStatements,
                          'tree_chain_classification': self.treeChainClassificationStatements
                          }

        return {k: 1 for k, v in contentSubtype.items() if v > 0}

    def getPolymerSequence(self):
        """ Return polymer sequence of AMBER PT file.
        """
        return self.__polySeqInMR

    def getAtomNumberDict(self):
        """ Return AMBER atomic number dictionary.
        """
        return self.__atomNumberDict

# del AmberPTParser
