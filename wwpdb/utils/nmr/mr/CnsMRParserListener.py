##
# File: CnsMRParserListener.py
# Date: 09-Feb-2022
#
# Updates:
# Generated from CnsMRParser.g4 by ANTLR 4.9
""" ParserLister class for CNS MR files.
    @author: Masashi Yokochi
"""
import sys
import re
import numpy as np

from antlr4 import ParseTreeListener
from wwpdb.utils.nmr.mr.CnsMRParser import CnsMRParser

from wwpdb.utils.nmr.NEFTranslator.NEFTranslator import NEFTranslator
from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
from wwpdb.utils.config.ConfigInfo import getSiteId
from wwpdb.utils.config.ConfigInfoApp import ConfigInfoAppCommon
from wwpdb.utils.nmr.io.ChemCompIo import ChemCompReader
from rmsd.calculate_rmsd import (int_atom, ELEMENT_WEIGHTS)  # noqa: F401 pylint: disable=no-name-in-module, import-error


def to_np_array(atom):
    """ Return Numpy array of a given Cartesian coordinate in {'x': float, 'y': float, 'z': float} format.
    """

    return np.asarray([atom['x'], atom['y'], atom['z']], dtype=float)


def to_re_exp(string):
    """ Return regular expression for a given string including CNS wildcard format.
    """

    if '*' in string:  # any string
        return string.replace('*', '.*')
    if '%' in string:  # a single character
        return string.replace('%', '.')
    if '#' in string:  # any number
        return string.replace('#', '[+-]?[0-9][0-9\\.]?')
    if '+' in string:  # any digit
        return string.replace('+', '[0-9]+')
    return string


# This class defines a complete listener for a parse tree produced by CnsMRParser.
class CnsMRParserListener(ParseTreeListener):

    __verbose = None
    __lfh = None

    distRestraints = 0      # CNS: Distance restraints
    dihedRestraints = 0     # CNS: Dihedral angle restraints
    rdcRestraints = 0       # CNS: Suscetibility anisotropy restraints
    planeRestraints = 0     # CNS: Plane restraints
    jcoupRestraints = 0     # CNS: Scalar J-coupling restraints
    hvycsRestraints = 0     # CNS: Carbon chemical shift restraints
    procsRestraints = 0     # CNS: Proton chemical shift restraints
    ramaRestraints = 0      # CNS: Conformation database restraints
    diffRestraints = 0      # CNS: Diffusion anisotropy restraints
    nbaseRestraints = 0     # CNS: Residue-residue position/orientation database restraints
    angRestraints = 0       # CNS: Angle database restraints

    distStatements = 0      # CNS: Distance statements
    dihedStatements = 0     # CNS: Dihedral angle statements
    rdcStatements = 0       # CNS: Suscetibility anisotropy statements
    planeStatements = 0     # CNS: Plane statements
    jcoupStatements = 0     # CNS: Scalar J-coupling statements
    hvycsStatements = 0     # CNS: Carbon chemical shift statements
    procsStatements = 0     # CNS: Proton chemical shift statements
    ramaStatements = 0      # CNS: Conformation database statements
    diffStatements = 0      # CNS: Diffusion anisotropy statements
    nbaseStatements = 0     # CNS: Residue-residue position/orientation database statements
    angStatements = 0       # CNS: Angle database statements

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

    __lastCompId = None
    __lastCompIdTest = False
    # __lastChemCompDict = None
    __lastChemCompAtoms = None
    __lastChemCompBonds = None

    __chemCompAtomDict = None
    __chemCompBondDict = None

    __ccaAtomId = None
    # __ccaAromaticFlag = None
    __ccaLeavingAtomFlag = None
    __ccaTypeSymbol = None

    __ccbAtomId1 = None
    __ccbAtomId2 = None
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

    # current restraint subtype
    __cur_subtype = None

    depth = 0

    stackSelections = None  # stack of selection
    stackTerms = None  # stack of term
    stackFactors = None  # stack of factor

    factor = None

    # 3D vectors in point clause
    inVector3D = False
    inVector3D_columnSel = -1
    inVector3D_tail = None
    inVector3D_head = None
    vector3D = None

    # collection of atom selection
    atomSelectionSet = None

    warningMessage = ''

    def __init__(self, verbose=True, log=sys.stdout, cR=None, polySeq=None):
        self.__verbose = verbose
        self.__lfh = log
        self.__cR = cR

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
                self.__lfh.write(f"+CnsMRParserListener.__init__() ++ Error  - {str(e)}\n")

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
                    self.__lfh.write(f"+CnsMRParserListener.__init__() ++ Error - {str(e)}\n")

        # NEFTranslator
        self.__nefT = NEFTranslator()

        if self.__nefT is None:
            raise IOError("+CnsMRParserListener.__init__() ++ Error  - NEFTranslator is not available.")

        # BMRB chemical shift statistics
        self.__csStat = BMRBChemShiftStat()

        if not self.__csStat.isOk():
            raise IOError("+CnsMRParserListener.__init__() ++ Error  - BMRBChemShiftStat is not available.")

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

        cartnX = next(d for d in self.__chemCompAtomDict if d[0] == '_chem_comp_atom.model_Cartn_x')
        cartnY = next(d for d in self.__chemCompAtomDict if d[0] == '_chem_comp_atom.model_Cartn_y')
        cartnZ = next(d for d in self.__chemCompAtomDict if d[0] == '_chem_comp_atom.model_Cartn_z')
        self.__ccaCartnX = self.__chemCompAtomDict.index(cartnX)
        self.__ccaCartnY = self.__chemCompAtomDict.index(cartnY)
        self.__ccaCartnZ = self.__chemCompAtomDict.index(cartnZ)

        # aromaticFlag = next(d for d in self.__chemCompAtomDict if d[0] == '_chem_comp_atom.pdbx_aromatic_flag')
        # self.__ccaAromaticFlag = self.__chemCompAtomDict.index(aromaticFlag)

        leavingAtomFlag = next(d for d in self.__chemCompAtomDict if d[0] == '_chem_comp_atom.pdbx_leaving_atom_flag')
        self.__ccaLeavingAtomFlag = self.__chemCompAtomDict.index(leavingAtomFlag)

        typeSymbol = next(d for d in self.__chemCompAtomDict if d[0] == '_chem_comp_atom.type_symbol')
        self.__ccaTypeSymbol = self.__chemCompAtomDict.index(typeSymbol)

        # taken from wwpdb.apps.ccmodule.io.ChemCompIo
        self.__chemCompBondDict = [
            ('_chem_comp_bond.comp_id', '%s', 'str', ''),
            ('_chem_comp_bond.atom_id_1', '%s', 'str', ''),
            ('_chem_comp_bond.atom_id_2', '%s', 'str', ''),
            ('_chem_comp_bond.value_order', '%s', 'str', ''),
            ('_chem_comp_bond.pdbx_aromatic_flag', '%s', 'str', ''),
            ('_chem_comp_bond.pdbx_stereo_config', '%s', 'str', ''),
            ('_chem_comp_bond.pdbx_ordinal', '%s', 'str', '')
        ]

        atomId1 = next(d for d in self.__chemCompBondDict if d[0] == '_chem_comp_bond.atom_id_1')
        self.__ccbAtomId1 = self.__chemCompBondDict.index(atomId1)

        atomId2 = next(d for d in self.__chemCompBondDict if d[0] == '_chem_comp_bond.atom_id_2')
        self.__ccbAtomId2 = self.__chemCompBondDict.index(atomId2)

        # aromaticFlag = next(d for d in self.__chemCompBondDict if d[0] == '_chem_comp_bond.pdbx_aromatic_flag')
        # self.__ccbAromaticFlag = self.__chemCompBondDict.index(aromaticFlag)

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
                self.__lastChemCompBonds = self.__ccR.getBonds()

        return self.__lastCompIdTest

    # Enter a parse tree produced by CnsMRParser#cns_mr.
    def enterCns_mr(self, ctx: CnsMRParser.Cns_mrContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#cns_mr.
    def exitCns_mr(self, ctx: CnsMRParser.Cns_mrContext):  # pylint: disable=unused-argument
        if len(self.warningMessage) == 0:
            self.warningMessage = None
        else:
            self.warningMessage = self.warningMessage[0:-1]

    # Enter a parse tree produced by CnsMRParser#distance_restraint.
    def enterDistance_restraint(self, ctx: CnsMRParser.Distance_restraintContext):  # pylint: disable=unused-argument
        self.distStatements += 1

    # Exit a parse tree produced by CnsMRParser#distance_restraint.
    def exitDistance_restraint(self, ctx: CnsMRParser.Distance_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#dihedral_angle_restraint.
    def enterDihedral_angle_restraint(self, ctx: CnsMRParser.Dihedral_angle_restraintContext):  # pylint: disable=unused-argument
        self.dihedStatements += 1

    # Exit a parse tree produced by CnsMRParser#dihedral_angle_restraint.
    def exitDihedral_angle_restraint(self, ctx: CnsMRParser.Dihedral_angle_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#plane_restraint.
    def enterPlane_restraint(self, ctx: CnsMRParser.Plane_restraintContext):  # pylint: disable=unused-argument
        self.planeStatements += 1

    # Exit a parse tree produced by CnsMRParser#plane_restraint.
    def exitPlane_restraint(self, ctx: CnsMRParser.Plane_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#harmonic_restraint.
    def enterHarmonic_restraint(self, ctx: CnsMRParser.Harmonic_restraintContext):  # pylint: disable=unused-argument
        self.angStatements += 1

    # Exit a parse tree produced by CnsMRParser#harmonic_restraint.
    def exitHarmonic_restraint(self, ctx: CnsMRParser.Harmonic_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#rdc_restraint.
    def enterRdc_restraint(self, ctx: CnsMRParser.Rdc_restraintContext):  # pylint: disable=unused-argument
        self.rdcStatements += 1

    # Exit a parse tree produced by CnsMRParser#rdc_restraint.
    def exitRdc_restraint(self, ctx: CnsMRParser.Rdc_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#coupling_restraint.
    def enterCoupling_restraint(self, ctx: CnsMRParser.Coupling_restraintContext):  # pylint: disable=unused-argument
        self.jcoupStatements += 1

    # Exit a parse tree produced by CnsMRParser#coupling_restraint.
    def exitCoupling_restraint(self, ctx: CnsMRParser.Coupling_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#carbon_shift_restraint.
    def enterCarbon_shift_restraint(self, ctx: CnsMRParser.Carbon_shift_restraintContext):  # pylint: disable=unused-argument
        self.hvycsStatements += 1

    # Exit a parse tree produced by CnsMRParser#carbon_shift_restraint.
    def exitCarbon_shift_restraint(self, ctx: CnsMRParser.Carbon_shift_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#proton_shift_restraint.
    def enterProton_shift_restraint(self, ctx: CnsMRParser.Proton_shift_restraintContext):  # pylint: disable=unused-argument
        self.procsStatements += 1

    # Exit a parse tree produced by CnsMRParser#proton_shift_restraint.
    def exitProton_shift_restraint(self, ctx: CnsMRParser.Proton_shift_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#conformation_db_restraint.
    def enterConformation_db_restraint(self, ctx: CnsMRParser.Conformation_db_restraintContext):  # pylint: disable=unused-argument
        self.ramaStatements += 1

    # Exit a parse tree produced by CnsMRParser#conformation_db_restraint.
    def exitConformation_db_restraint(self, ctx: CnsMRParser.Conformation_db_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#diffusion_anisotropy_restraint.
    def enterDiffusion_anisotropy_restraint(self, ctx: CnsMRParser.Diffusion_anisotropy_restraintContext):  # pylint: disable=unused-argument
        self.diffStatements += 1

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
        self.angStatements += 1

    # Exit a parse tree produced by CnsMRParser#angle_db_restraint.
    def exitAngle_db_restraint(self, ctx: CnsMRParser.Angle_db_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#noe_statement.
    def enterNoe_statement(self, ctx: CnsMRParser.Noe_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#noe_statement.
    def exitNoe_statement(self, ctx: CnsMRParser.Noe_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#noe_assign.
    def enterNoe_assign(self, ctx: CnsMRParser.Noe_assignContext):  # pylint: disable=unused-argument
        self.distRestraints += 1
        self.__cur_subtype = 'dist'

        self.atomSelectionSet = []

    # Exit a parse tree produced by CnsMRParser#noe_assign.
    def exitNoe_assign(self, ctx: CnsMRParser.Noe_assignContext):
        target = float(str(ctx.Real(0)))
        dminus = float(str(ctx.Real(1)))
        dplus = float(str(ctx.Real(2)))

        for i in range(0, len(self.atomSelectionSet), 2):
            j = i + 1
            for atom_1 in self.atomSelectionSet[i]:
                for atom_2 in self.atomSelectionSet[j]:
                    print(f"subtype={self.__cur_subtype} id={self.distRestraints} "
                          f"atom_1={atom_1} atom_2={atom_2} "
                          f"target_value={target:.3} lower_limit={target-dminus:.3} upper_limit={target+dplus:.3}")

    # Enter a parse tree produced by CnsMRParser#predict_statement.
    def enterPredict_statement(self, ctx: CnsMRParser.Predict_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#predict_statement.
    def exitPredict_statement(self, ctx: CnsMRParser.Predict_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#dihedral_statement.
    def enterDihedral_statement(self, ctx: CnsMRParser.Dihedral_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#dihedral_statement.
    def exitDihedral_statement(self, ctx: CnsMRParser.Dihedral_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#dihedral_assign.
    def enterDihedral_assign(self, ctx: CnsMRParser.Dihedral_assignContext):  # pylint: disable=unused-argument
        self.dihedRestraints += 1
        self.__cur_subtype = 'dihed'

    # Exit a parse tree produced by CnsMRParser#dihedral_assign.
    def exitDihedral_assign(self, ctx: CnsMRParser.Dihedral_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#plane_statement.
    def enterPlane_statement(self, ctx: CnsMRParser.Plane_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#plane_statement.
    def exitPlane_statement(self, ctx: CnsMRParser.Plane_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#group_statement.
    def enterGroup_statement(self, ctx: CnsMRParser.Group_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#group_statement.
    def exitGroup_statement(self, ctx: CnsMRParser.Group_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#harmonic_statement.
    def enterHarmonic_statement(self, ctx: CnsMRParser.Harmonic_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#harmonic_statement.
    def exitHarmonic_statement(self, ctx: CnsMRParser.Harmonic_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#sani_statement.
    def enterSani_statement(self, ctx: CnsMRParser.Sani_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#sani_statement.
    def exitSani_statement(self, ctx: CnsMRParser.Sani_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#sani_assign.
    def enterSani_assign(self, ctx: CnsMRParser.Sani_assignContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1
        self.__cur_subtype = 'rdc'

    # Exit a parse tree produced by CnsMRParser#sani_assign.
    def exitSani_assign(self, ctx: CnsMRParser.Sani_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#coupling_statement.
    def enterCoupling_statement(self, ctx: CnsMRParser.Coupling_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#coupling_statement.
    def exitCoupling_statement(self, ctx: CnsMRParser.Coupling_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#coup_assign.
    def enterCoup_assign(self, ctx: CnsMRParser.Coup_assignContext):  # pylint: disable=unused-argument
        self.jcoupRestraints += 1
        self.__cur_subtype = 'jcoup'

    # Exit a parse tree produced by CnsMRParser#coup_assign.
    def exitCoup_assign(self, ctx: CnsMRParser.Coup_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#carbon_shift_statement.
    def enterCarbon_shift_statement(self, ctx: CnsMRParser.Carbon_shift_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#carbon_shift_statement.
    def exitCarbon_shift_statement(self, ctx: CnsMRParser.Carbon_shift_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#carbon_shift_assign.
    def enterCarbon_shift_assign(self, ctx: CnsMRParser.Carbon_shift_assignContext):  # pylint: disable=unused-argument
        self.hvycsRestraints += 1
        self.__cur_subtype = 'hvycs'

    # Exit a parse tree produced by CnsMRParser#carbon_shift_assign.
    def exitCarbon_shift_assign(self, ctx: CnsMRParser.Carbon_shift_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#carbon_shift_rcoil.
    def enterCarbon_shift_rcoil(self, ctx: CnsMRParser.Carbon_shift_rcoilContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#carbon_shift_rcoil.
    def exitCarbon_shift_rcoil(self, ctx: CnsMRParser.Carbon_shift_rcoilContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#proton_shift_statement.
    def enterProton_shift_statement(self, ctx: CnsMRParser.Proton_shift_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#proton_shift_statement.
    def exitProton_shift_statement(self, ctx: CnsMRParser.Proton_shift_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#observed.
    def enterObserved(self, ctx: CnsMRParser.ObservedContext):  # pylint: disable=unused-argument
        self.procsRestraints += 1
        self.__cur_subtype = 'procs'

    # Exit a parse tree produced by CnsMRParser#observed.
    def exitObserved(self, ctx: CnsMRParser.ObservedContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#proton_shift_rcoil.
    def enterProton_shift_rcoil(self, ctx: CnsMRParser.Proton_shift_rcoilContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#proton_shift_rcoil.
    def exitProton_shift_rcoil(self, ctx: CnsMRParser.Proton_shift_rcoilContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#proton_shift_anisotropy.
    def enterProton_shift_anisotropy(self, ctx: CnsMRParser.Proton_shift_anisotropyContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#proton_shift_anisotropy.
    def exitProton_shift_anisotropy(self, ctx: CnsMRParser.Proton_shift_anisotropyContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#proton_shift_amides.
    def enterProton_shift_amides(self, ctx: CnsMRParser.Proton_shift_amidesContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#proton_shift_amides.
    def exitProton_shift_amides(self, ctx: CnsMRParser.Proton_shift_amidesContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#proton_shift_carbons.
    def enterProton_shift_carbons(self, ctx: CnsMRParser.Proton_shift_carbonsContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#proton_shift_carbons.
    def exitProton_shift_carbons(self, ctx: CnsMRParser.Proton_shift_carbonsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#proton_shift_nitrogens.
    def enterProton_shift_nitrogens(self, ctx: CnsMRParser.Proton_shift_nitrogensContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#proton_shift_nitrogens.
    def exitProton_shift_nitrogens(self, ctx: CnsMRParser.Proton_shift_nitrogensContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#proton_shift_oxygens.
    def enterProton_shift_oxygens(self, ctx: CnsMRParser.Proton_shift_oxygensContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#proton_shift_oxygens.
    def exitProton_shift_oxygens(self, ctx: CnsMRParser.Proton_shift_oxygensContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#proton_shift_ring_atoms.
    def enterProton_shift_ring_atoms(self, ctx: CnsMRParser.Proton_shift_ring_atomsContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#proton_shift_ring_atoms.
    def exitProton_shift_ring_atoms(self, ctx: CnsMRParser.Proton_shift_ring_atomsContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#proton_shift_alphas_and_amides.
    def enterProton_shift_alphas_and_amides(self, ctx: CnsMRParser.Proton_shift_alphas_and_amidesContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#proton_shift_alphas_and_amides.
    def exitProton_shift_alphas_and_amides(self, ctx: CnsMRParser.Proton_shift_alphas_and_amidesContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#conformation_statement.
    def enterConformation_statement(self, ctx: CnsMRParser.Conformation_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#conformation_statement.
    def exitConformation_statement(self, ctx: CnsMRParser.Conformation_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#conf_assign.
    def enterConf_assign(self, ctx: CnsMRParser.Conf_assignContext):  # pylint: disable=unused-argument
        self.ramaRestraints += 1
        self.__cur_subtype = 'rama'

    # Exit a parse tree produced by CnsMRParser#conf_assign.
    def exitConf_assign(self, ctx: CnsMRParser.Conf_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#diffusion_statement.
    def enterDiffusion_statement(self, ctx: CnsMRParser.Diffusion_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by CnsMRParser#diffusion_statement.
    def exitDiffusion_statement(self, ctx: CnsMRParser.Diffusion_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#dani_assign.
    def enterDani_assign(self, ctx: CnsMRParser.Dani_assignContext):  # pylint: disable=unused-argument
        self.diffRestraints += 1
        self.__cur_subtype = 'diff'

    # Exit a parse tree produced by CnsMRParser#dani_assign.
    def exitDani_assign(self, ctx: CnsMRParser.Dani_assignContext):  # pylint: disable=unused-argument
        pass

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
        self.angRestraints += 1
        self.__cur_subtype = 'ang'

    # Exit a parse tree produced by CnsMRParser#angle_db_assign.
    def exitAngle_db_assign(self, ctx: CnsMRParser.Angle_db_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by CnsMRParser#selection.
    def enterSelection(self, ctx: CnsMRParser.SelectionContext):  # pylint: disable=unused-argument
        if self.__verbose:
            print("  " * self.depth + "enter_selection")

        if self.inVector3D:
            self.inVector3D_columnSel += 1

        elif self.depth == 0:
            self.stackSelections = []
            self.stackTerms = []
            self.factor = {}

    # Exit a parse tree produced by CnsMRParser#selection.
    def exitSelection(self, ctx: CnsMRParser.SelectionContext):  # pylint: disable=unused-argument
        if self.__verbose:
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

        if self.__verbose:
            print("  " * self.depth + f"atom selection: {atomSelection}")

        if self.inVector3D:
            if self.inVector3D_columnSel == 0:
                self.inVector3D_tail = atomSelection[0]
                if len(atomSelection) > 1:
                    self.warningMessage += f"[Multiple selections] {self.__getCurrentRestraint()}"\
                        "The first atom has been selected to create a 3d-vector in the 'tail' clause.\n"
            elif self.inVector3D_columnSel == 1:
                self.inVector3D_head = atomSelection[0]
                if len(atomSelection) > 1:
                    self.warningMessage += f"[Multiple selections] {self.__getCurrentRestraint()}"\
                        "The first atom has been selected to create a 3d-vector in the 'head' clause.\n"

        else:
            self.atomSelectionSet.append(atomSelection)

    # Enter a parse tree produced by CnsMRParser#selection_expression.
    def enterSelection_expression(self, ctx: CnsMRParser.Selection_expressionContext):
        if self.__verbose:
            print("  " * self.depth + f"enter_sel_expr, union: {bool(ctx.Or_op(0))}")

        if self.depth > 0 and len(self.factor) > 0:
            if 'atom_selection' not in self.factor:
                self.consumeFactor_expressions(cifCheck=False)
            if 'atom_selection' in self.factor:
                self.stackSelections.append(self.factor['atom_selection'])

        self.factor = {}

        self.depth += 1

    # Exit a parse tree produced by CnsMRParser#selection_expression.
    def exitSelection_expression(self, ctx: CnsMRParser.Selection_expressionContext):  # pylint: disable=unused-argument
        self.depth -= 1
        if self.__verbose:
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
        if self.__verbose:
            print("  " * self.depth + f"enter_term, intersection: {bool(ctx.And_op(0))}")

        self.stackFactors = []
        self.factor = {}

        self.depth += 1

    # Exit a parse tree produced by CnsMRParser#term.
    def exitTerm(self, ctx: CnsMRParser.TermContext):  # pylint: disable=unused-argument
        self.depth -= 1
        if self.__verbose:
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
                        _seqId = to_re_exp(seqId)
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
                    if self.__updateChemCompDict(compId):
                        for cca in self.__lastChemCompAtoms:
                            realTypeSymbol = cca[self.__ccaTypeSymbol]
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
                    if self.__updateChemCompDict(compId):
                        for cca in self.__lastChemCompAtoms:
                            if cca[self.__ccaTypeSymbol] in _factor['type_symbol']\
                               and cca[self.__ccaLeavingAtomFlag] != 'Y':
                                _atomIdSelect.add(cca[self.__ccaAtomId])
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
                if self.__updateChemCompDict(compId):
                    for cca in self.__lastChemCompAtoms:
                        if cca[self.__ccaLeavingAtomFlag] != 'Y':
                            realAtomId = cca[self.__ccaAtomId]
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
                if self.__updateChemCompDict(compId):
                    for cca in self.__lastChemCompAtoms:
                        if cca[self.__ccaLeavingAtomFlag] != 'Y':
                            realAtomId = cca[self.__ccaAtomId]
                            _atomIdSelect.add(realAtomId)
            _factor['atom_id'] = list(_atomIdSelect)
            if len(_factor['atom_id']) == 0:
                _factor['atom_id'] = [None]

        _atomSelection = []

        try:

            if _factor['atom_id'][0] is not None:
                for chainId in _factor['chain_id']:
                    ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chainId), None)
                    for seqId in _factor['seq_id']:
                        if ps is not None and seqId in ps['seq_id']:
                            compId = ps['comp_id'][ps['seq_id'].index(seqId)]
                        else:
                            compId = None

                        for atomId in _factor['atom_id']:
                            atomIds = self.__nefT.get_valid_star_atom(compId, atomId.upper())[0]

                            for _atomId in atomIds:
                                ccdCheck = not cifCheck

                                if cifCheck:
                                    _atom =\
                                        self.__cR.getDictListWithFilter('atom_site',
                                                                        [{'name': 'label_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                                         {'name': 'type_symbol', 'type': 'str'},
                                                                         ],
                                                                        [{'name': self.__authAsymId, 'type': 'str', 'value': chainId},
                                                                         {'name': self.__authSeqId, 'type': 'int', 'value': seqId},
                                                                         {'name': self.__authAtomId, 'type': 'str', 'value': _atomId},
                                                                         {'name': self.__modelNumName, 'type': 'int',
                                                                          'value': self.__representativeModelId}
                                                                         ])

                                    if len(_atom) == 1:
                                        if ('comp_id' not in _factor or _atom[0]['comp_id'] in _factor['comp_id'])\
                                           and ('type_symbol' not in _factor or _atom[0]['type_symbol'] in _factor['type_symbol']):
                                            _atomSelection.append({'chain_id': chainId, 'seq_id': seqId, 'comp_id': _atom[0]['comp_id'], 'atom_id': _atomId})
                                    else:
                                        ccdCheck = True

                                if ccdCheck and compId is not None:
                                    if self.__updateChemCompDict(compId) and ('comp_id' not in _factor or compId in _factor['comp_id']):
                                        cca = next((cca for cca in self.__lastChemCompAtoms if cca[self.__ccaAtomId] == _atomId), None)
                                        if cca is not None and ('type_symbol' not in _factor or cca[self.__ccaTypeSymbol] in _factor['type_symbol']):
                                            _atomSelection.append({'chain_id': chainId, 'seq_id': seqId, 'comp_id': compId, 'atom_id': _atomId})
                                            if cifCheck:
                                                self.warningMessage += f"[Atom not found] {self.__getCurrentRestraint()}"\
                                                    "{chainId}:{seqId}:{compId}:{atomId} is not present in the coordinate.\n"

        except Exception as e:
            if self.__verbose:
                self.__lfh.write(f"+CnsMRParserListener.__consumeFactor_expressions() ++ Error  - {str(e)}\n")

        atomSelection = []
        for atom in _atomSelection:
            if atom not in atomSelection:
                atomSelection.append(atom)

        if 'atom_selection' not in _factor:
            _factor['atom_selection'] = atomSelection
        else:
            _atomSelection = []
            for _atom in _factor['atom_selection']:
                if _atom in atomSelection:
                    _atomSelection.append(_atom)
            _factor['atom_selection'] = _atomSelection

        if len(_factor['atom_selection']) == 0:
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

    # Enter a parse tree produced by CnsMRParser#factor.
    def enterFactor(self, ctx: CnsMRParser.FactorContext):
        if self.__verbose:
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
        if self.__verbose:
            print("  " * self.depth + "exit_factor")

        # concatenation
        if ctx.factor() and self.stackSelections:
            self.stackFactors.pop()
            self.factor = {'atom_selection': self.stackSelections.pop()}

        if ctx.All() or ctx.Known():
            clauseName = 'all' if ctx.All() else 'known'
            if self.__verbose:
                print("  " * self.depth + f"--> {clauseName}")
            try:

                atomSelection =\
                    self.__cR.getDictListWithFilter('atom_site',
                                                    [{'name': 'auth_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                                     {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                                     {'name': 'label_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                     {'name': 'label_atom_id', 'type': 'str', 'alt_name': 'atom_id'}
                                                     ],
                                                    [{'name': self.__modelNumName, 'type': 'int',
                                                      'value': self.__representativeModelId}
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
                    self.__lfh.write(f"+CnsMRParserListener.exitFactor() ++ Error  - {str(e)}\n")

        elif ctx.Around() or ctx.Saround():
            clauseName = 'around' if ctx.Around() else 'saround'
            if self.__verbose:
                print("  " * self.depth + f"--> {clauseName}")
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
                                                              'value': self.__representativeModelId}
                                                             ])

                        if len(_origin) != 1:
                            continue

                        origin = to_np_array(_origin[0])

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
                                                              'value': self.__representativeModelId}
                                                             ])

                        if len(_neighbor) == 0:
                            continue

                        neighbor = [atom for atom in _neighbor if np.linalg.norm(to_np_array(atom) - origin) < around]

                        for atom in neighbor:
                            del atom['x']
                            del atom['y']
                            del atom['z']
                            _atomSelection.append(atom)

                    except Exception as e:
                        if self.__verbose:
                            self.__lfh.write(f"+CnsMRParserListener.exitFactor() ++ Error  - {str(e)}\n")

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
                                                                          'value': self.__representativeModelId}
                                                                         ])

                                    if len(_origin) != 1:
                                        continue

                                    origin = np.dot(inv_matrix, np.subtract(to_np_array(_origin[0]), vector))

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
                                                                          'value': self.__representativeModelId}
                                                                         ])

                                    if len(_neighbor) == 0:
                                        continue

                                    neighbor = [atom for atom in _neighbor if np.linalg.norm(to_np_array(atom) - origin) < around]

                                    for atom in neighbor:
                                        del atom['x']
                                        del atom['y']
                                        del atom['z']
                                        _atomSelection.append(atom)

                                except Exception as e:
                                    if self.__verbose:
                                        self.__lfh.write(f"+CnsMRParserListener.exitFactor() ++ Error  - {str(e)}\n")

                if len(self.factor['atom_selection']) > 0:
                    atomSelection = []
                    for atom in _atomSelection:
                        if atom not in atomSelection:
                            atomSelection.append(atom)

                    self.factor['atom_selection'] = atomSelection

                    if len(self.factor['atom_selection']) == 0:
                        self.factor['atom_id'] = [None]
                        self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                            f"The {clauseName!r} clause has no effect.\n"

        elif ctx.Atom():
            if self.__verbose:
                print("  " * self.depth + "--> atom")
            simpleNameIndex = simpleNamesIndex = 0  # these indices are necessary to deal with mixing case of 'Simple_name' and 'Simple_names'
            if ctx.Simple_name(0):
                chainId = str(ctx.Simple_name(0))
                self.factor['chain_id'] = [ps['chain_id'] for ps in self.__polySeq
                                           if ps['chain_id'] == chainId]
                if len(self.factor['chain_id']) > 0:
                    simpleNameIndex += 1

            if simpleNameIndex == 0 and ctx.Simple_names(0):
                chainId = str(ctx.Simple_names(0))
                _chainId = to_re_exp(chainId)
                self.factor['chain_id'] = [ps['chain_id'] for ps in self.__polySeq
                                           if re.match(_chainId, ps['chain_id'])]
                simpleNamesIndex += 1

            if len(self.factor['chain_id']) == 0:
                self.factor['atom_id'] = [None]
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    "Couldn't specify segment name "\
                    f"'{chainId}' the coordinates.\n"  # do not use 'chainId!r' expression, '%' code throws ValueError

            if ctx.Integer(0):
                self.factor['seq_id'] = [int(str(ctx.Integer(0)))]

            if ctx.Integers():
                seqId = str(ctx.Integers())
                _seqId = to_re_exp(seqId)
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
                            if self.__updateChemCompDict(compId):
                                if any(cca for cca in self.__lastChemCompAtoms if cca[self.__ccaAtomId] == atomId):
                                    _atomIdSelect.add(atomId)

            elif ctx.Simple_names(simpleNamesIndex):
                atomId = str(ctx.Simple_names(simpleNamesIndex))
                _atomId = to_re_exp(atomId)
                for chainId in self.factor['chain_id']:
                    ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chainId), None)
                    if ps is None:
                        continue
                    for seqId in self.factor['seq_id']:
                        if seqId in ps['seq_id']:
                            compId = ps['comp_id'][ps['seq_id'].index(seqId)]
                            if self.__updateChemCompDict(compId):
                                for cca in self.__lastChemCompAtoms:
                                    if cca[self.__ccaLeavingAtomFlag] != 'Y':
                                        realAtomId = cca[self.__ccaAtomId]
                                        if re.match(_atomId, realAtomId):
                                            _atomIdSelect.add(realAtomId)

            self.factor['atom_id'] = list(_atomIdSelect)

            self.consumeFactor_expressions("'atom' clause", False)

        elif ctx.Attribute():
            if self.__verbose:
                print("  " * self.depth + "--> attribute")
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
                                                      'value': self.__representativeModelId}
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
                                                      'value': self.__representativeModelId}
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
                                                      'value': self.__representativeModelId}
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
                                                      'value': self.__representativeModelId}
                                                     ])

                self.intersectionFactor_expressions(atomSelection)

            elif attr_prop.startswith('scatter'):  # scatter_[ab][1-4], scatter_c, scatter_fp, scatter_fdp
                self.warningMessage += f"[Unavailable resource] {self.__getCurrentRestraint()}"\
                    f"The attribute property {_attr_prop!r} "\
                    "related to X-ray scattering power of each atom is not possessed in the static coordinate file.\n"
                validProp = False

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
                                                      'value': self.__representativeModelId}
                                                     ])

                self.intersectionFactor_expressions(atomSelection)

            if validProp and len(self.factor['atom_selection']) == 0:
                self.factor['atom_id'] = [None]
                _absolute = ' abs' if absolute else ''
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The 'attribute' clause ('{_attr_prop}{_absolute} {opCode} {attr_value}') has no effect.\n"

        elif ctx.BondedTo():
            if self.__verbose:
                print("  " * self.depth + "--> bondedto")
            if 'atom_selection' in self.factor and len(self.factor['atom_selection']) > 0:
                _atomSelection = []

                for _atom in self.factor['atom_selection']:
                    chainId = _atom['chain_id']
                    compId = _atom['comp_id']
                    seqId = _atom['seq_id']
                    atomId = _atom['atom_id']

                    # intra
                    if self.__updateChemCompDict(compId):
                        leavingAtomIds = [cca[self.__ccaAtomId] for cca in self.__lastChemCompAtoms if cca[self.__ccaLeavingAtomFlag] == 'Y']

                        _atomIdSelect = set()
                        for ccb in self.__lastChemCompBonds:
                            if ccb[self.__ccbAtomId1] == atomId:
                                _atomIdSelect.add(ccb[self.__ccbAtomId2])
                            elif ccb[self.__ccbAtomId2] == atomId:
                                _atomIdSelect.add(ccb[self.__ccbAtomId1])

                        hasLeaavindAtomId = False

                        for _atomId in _atomIdSelect:

                            if _atomId in leavingAtomIds:
                                hasLeaavindAtomId = True
                                continue

                            _atom =\
                                self.__cR.getDictListWithFilter('atom_site',
                                                                [{'name': 'label_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                                 ],
                                                                [{'name': self.__authAsymId, 'type': 'str', 'value': chainId},
                                                                 {'name': self.__authSeqId, 'type': 'int', 'value': seqId},
                                                                 {'name': self.__authAtomId, 'type': 'str', 'value': _atomId},
                                                                 {'name': self.__modelNumName, 'type': 'int',
                                                                  'value': self.__representativeModelId}
                                                                 ])

                            if len(_atom) == 1 and _atom[0]['comp_id'] == compId:
                                _atomSelection.append({'chain_id': chainId, 'seq_id': seqId, 'comp_id': compId, 'atom_id': _atomId})

                            else:
                                ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chainId), None)
                                if ps is not None and seqId in ps['seq_id'] and ps['comp_id'][ps['seq_id'].index(seqId)] == compId:
                                    if any(cca for cca in self.__lastChemCompAtoms if cca[self.__ccaAtomId] == _atomId):
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
                                                                  'value': self.__representativeModelId}
                                                                 ])

                            if len(_origin) == 1:
                                origin = to_np_array(_origin[0])

                                ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chainId), None)
                                if ps is not None:
                                    for _seqId in [seqId - 1, seqId + 1]:
                                        if _seqId in ps['seq_id']:
                                            _compId = ps['comp_id'][ps['seq_id'].index(_seqId)]
                                            if self.__updateChemCompDict(_compId):
                                                leavingAtomIds = [cca[self.__ccaAtomId] for cca in self.__lastChemCompAtoms if cca[self.__ccaLeavingAtomFlag] == 'Y']

                                                _atomIdSelect = set()
                                                for ccb in self.__lastChemCompBonds:
                                                    if ccb[self.__ccbAtomId1] in leavingAtomIds:
                                                        _atomId = ccb[self.__ccbAtomId2]
                                                        if _atomId not in leavingAtomIds:
                                                            _atomIdSelect.add(_atomId)
                                                    if ccb[self.__ccbAtomId2] in leavingAtomIds:
                                                        _atomId = ccb[self.__ccbAtomId1]
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
                                                                                          'value': self.__representativeModelId}
                                                                                         ])

                                                    if len(_neighbor) != 1:
                                                        continue

                                                    if np.linalg.norm(to_np_array(_neighbor[0]) - origin) < 2.5:
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

                atomSelection = []
                for atom in _atomSelection:
                    if atom not in atomSelection:
                        atomSelection.append(atom)

                self.factor['atom_selection'] = atomSelection

                if len(self.factor['atom_selection']) == 0:
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        "The 'bondedto' clause has no effect.\n"

            else:
                self.factor['atom_id'] = [None]
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    "The 'bondedto' clause has no effect because no atom is selected.\n"

        elif ctx.ByGroup():
            if self.__verbose:
                print("  " * self.depth + "--> bygroup")
            if 'atom_selection' in self.factor and len(self.factor['atom_selection']) > 0:
                _atomSelection = []

                for _atom in self.factor['atom_selection']:
                    chainId = _atom['chain_id']
                    compId = _atom['comp_id']
                    seqId = _atom['seq_id']
                    atomId = _atom['atom_id']

                    _atomSelection.append(_atom)  # self atom

                    if self.__updateChemCompDict(compId):
                        _bondedAtomIdSelect = set()
                        for ccb in self.__lastChemCompBonds:
                            if ccb[self.__ccbAtomId1] == atomId:
                                _bondedAtomIdSelect.add(ccb[self.__ccbAtomId2])
                            elif ccb[self.__ccbAtomId2] == atomId:
                                _bondedAtomIdSelect.add(ccb[self.__ccbAtomId1])

                        _nonBondedAtomIdSelect = set()
                        for _atomId in _bondedAtomIdSelect:
                            for ccb in self.__lastChemCompBonds:
                                if ccb[self.__ccbAtomId1] == _atomId:
                                    _nonBondedAtomIdSelect.add(ccb[self.__ccbAtomId2])
                                elif ccb[self.__ccbAtomId2] == _atomId:
                                    _nonBondedAtomIdSelect.add(ccb[self.__ccbAtomId1])

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
                                                                  'value': self.__representativeModelId}
                                                                 ])

                            if len(_origin) == 1:
                                origin = to_np_array(_origin[0])

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
                                                                          'value': self.__representativeModelId}
                                                                         ])

                                    if len(_neighbor) != 1:
                                        continue

                                    if np.linalg.norm(to_np_array(_neighbor[0]) - origin) < 2.0:
                                        _atomSelection.append({'chain_id': chainId, 'seq_id': seqId, 'comp_id': compId, 'atom_id': _atomId})

                            else:
                                cca = next((cca for cca in self.__lastChemCompAtoms if cca[self.__ccaAtomId] == atomId), None)
                                if cca is not None:
                                    _origin = {'x': float(cca[self.__ccaCartnX]), 'y': float(cca[self.__ccaCartnY]), 'z': float(cca[self.__ccaCartnZ])}
                                    origin = to_np_array(_origin)

                                    for _atomId in _nonBondedAtomIdSelect:
                                        _cca = next((_cca for _cca in self.__lastChemCompAtoms if _cca[self.__ccaAtomId] == _atomId), None)
                                        if _cca is not None:
                                            _neighbor = {'x': float(_cca[self.__ccaCartnX]), 'y': float(_cca[self.__ccaCartnY]), 'z': float(_cca[self.__ccaCartnZ])}

                                            if np.linalg.norm(to_np_array(_neighbor) - origin) < 2.0:
                                                _atomSelection.append({'chain_id': chainId, 'seq_id': seqId, 'comp_id': compId, 'atom_id': _atomId})

                atomSelection = []
                for atom in _atomSelection:
                    if atom not in atomSelection:
                        atomSelection.append(atom)

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
            if self.__verbose:
                print("  " * self.depth + "--> byres")
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
                                                          'value': self.__representativeModelId}
                                                         ])

                    if len(_atomByRes) > 0 and _atomByRes[0]['comp_id'] == compId:
                        for _atom in _atomByRes:
                            _atomSelection.append({'chain_id': chainId, 'seq_id': seqId, 'comp_id': _atom['comp_id'], 'atom_id': _atom['atom_id']})

                    else:
                        ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chainId), None)
                        if ps is not None and seqId in ps['seq_id'] and ps['comp_id'][ps['seq_id'].index(seqId)] == compId:
                            if self.__updateChemCompDict(compId):
                                atomIds = [cca[self.__ccaAtomId] for cca in self.__lastChemCompAtoms if cca[self.__ccaLeavingAtomFlag] != 'Y']
                                for atomId in atomIds:
                                    _atomSelection.append({'chain_id': chainId, 'seq_id': seqId, 'comp_id': compId, 'atom_id': atomId})

                atomSelection = []
                for atom in _atomSelection:
                    if atom not in atomSelection:
                        atomSelection.append(atom)

                self.factor['atom_selection'] = atomSelection

                if len(self.factor['atom_selection']) == 0:
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        "The 'byres' clause has no effect.\n"

            else:
                self.factor['atom_id'] = [None]
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    "The 'byres' clause has no effect because no atom is selected.\n"

        elif ctx.Chemical():
            if self.__verbose:
                print("  " * self.depth + "--> chemical")
            if ctx.Colon():  # range expression
                self.factor['type_symbols'] = [str(ctx.Simple_name(0)), str(ctx.Simple_name(1))]

            elif ctx.Simple_name(0):
                self.factor['type_symbol'] = [str(ctx.Simple_name(0))]

            elif ctx.Simple_names(0):
                self.factor['type_symbols'] = [str(ctx.Simple_names(0))]

            self.consumeFactor_expressions("'chemical' clause", False)

        elif ctx.Hydrogen():
            if self.__verbose:
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

        elif ctx.Fbox() or ctx.Sfbox():
            clauseName = 'fbox' if ctx.Fbox() else 'sfbox'
            if self.__verbose:
                print("  " * self.depth + f"--> {clauseName}")
            xmin = float(str(ctx.Real(0)))
            xmax = float(str(ctx.Real(1)))
            ymin = float(str(ctx.Real(2)))
            ymax = float(str(ctx.Real(3)))
            zmin = float(str(ctx.Real(4)))
            zmax = float(str(ctx.Real(5)))

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
                                                      'value': self.__representativeModelId}
                                                     ])

            except Exception as e:
                if self.__verbose:
                    self.__lfh.write(f"+CnsMRParserListener.exitFactor() ++ Error  - {str(e)}\n")

            if ctx.Sfbox():
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
                                                                  'value': self.__representativeModelId}
                                                                 ])

                            for atom in __atomSelection:
                                origin = to_np_array(atom)
                                mv = np.dot(matrix, np.add(origin, vector))

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

            atomSelection = []
            for atom in _atomSelection:
                if atom not in atomSelection:
                    atomSelection.append(atom)

            self.factor['atom_selection'] = atomSelection

            if len(self.factor['atom_selection']) == 0:
                self.factor['atom_id'] = [None]
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    f"The {clauseName!r} clause has no effect.\n"

        elif ctx.Id():
            if self.__verbose:
                print("  " * self.depth + "--> id")
            self.factor['atom_id'] = [None]
            self.warningMessage += f"[Unavailable resource] {self.__getCurrentRestraint()}"\
                "The 'id' clause has no effect "\
                "because the internal atom number is not included in the coordinate file.\n"

        elif ctx.Name():
            if self.__verbose:
                print("  " * self.depth + "--> name")
            if ctx.Colon():  # range expression
                self.factor['atom_ids'] = [str(ctx.Simple_name(0)), str(ctx.Simple_name(1))]

            elif ctx.Simple_name(0):
                self.factor['atom_id'] = [str(ctx.Simple_name(0))]

            elif ctx.Simple_names(0):
                self.factor['atom_ids'] = [str(ctx.Simple_names(0))]

        elif ctx.NONE():
            if self.__verbose:
                print("  " * self.depth + "--> none")
            self.factor['atom_selection'] = []

        elif ctx.Not_op():
            if self.__verbose:
                print("  " * self.depth + "--> not")

            try:

                _atomSelection =\
                    self.__cR.getDictListWithFilter('atom_site',
                                                    [{'name': 'auth_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                                     {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                                     {'name': 'label_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                     {'name': 'label_atom_id', 'type': 'str', 'alt_name': 'atom_id'}
                                                     ],
                                                    [{'name': self.__modelNumName, 'type': 'int',
                                                      'value': self.__representativeModelId}
                                                     ])

            except Exception as e:
                if self.__verbose:
                    self.__lfh.write(f"+CnsMRParserListener.exitFactor() ++ Error  - {str(e)}\n")

            _refAtomSelection = [atom for atom in self.factor['atom_selection'] if atom in _atomSelection]
            self.factor['atom_selection'] = [atom for atom in _atomSelection if atom not in _refAtomSelection]

            if len(self.factor['atom_selection']) == 0:
                self.factor['atom_id'] = [None]
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    "The 'not' clause has no effect.\n"

        elif ctx.Point():
            if self.__verbose:
                print("  " * self.depth + "--> point")
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
                                                              'value': self.__representativeModelId}
                                                             ])

                        if len(_tail) == 1:
                            tail = to_np_array(_tail[0])

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
                                                                      'value': self.__representativeModelId}
                                                                     ])

                                if len(_head) == 1:
                                    head = to_np_array(_head[0])
                                    self.vector3D = np.subtract(tail, head, dtype=float)

                    except Exception as e:
                        if self.__verbose:
                            self.__lfh.write(f"+CnsMRParserListener.exitFactor() ++ Error  - {str(e)}\n")

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
                                                          'value': self.__representativeModelId}
                                                         ])

                    if len(_neighbor) > 0:
                        neighbor = [atom for atom in _neighbor if np.linalg.norm(to_np_array(atom) - self.vector3D) < cut]

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
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        "The 'cut' clause has no effect.\n"

            self.inVector3D = False
            self.vector3D = None

        elif ctx.Previous():
            if self.__verbose:
                print("  " * self.depth + "--> previous")
            self.factor['atom_id'] = [None]
            self.warningMessage += f"[Unavailable resource] {self.__getCurrentRestraint()}"\
                "The 'previous' clause has no effect "\
                "because the internal atom selection is fragile in the restraint file.\n"

        elif ctx.Pseudo():
            if self.__verbose:
                print("  " * self.depth + "--> pseudo")
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
                                                      'value': self.__representativeModelId}
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
                self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                    "The 'pseudo' clause has no effect.\n"

        elif ctx.Residue():
            if self.__verbose:
                print("  " * self.depth + "--> residue")
            if ctx.Colon():  # range expression
                self.factor['seq_id'] = list(range(int(str(ctx.Integer(0))), int(str(ctx.Integer(0))) + 1))

            elif ctx.Integer(0):
                self.factor['seq_id'] = [int(str(ctx.Integer(0)))]

            elif ctx.Integers():
                self.factor['seq_ids'] = [str(ctx.Integers())]

        elif ctx.Resname():
            if self.__verbose:
                print("  " * self.depth + "--> resname")
            if ctx.Colon():  # range expression
                self.factor['comp_ids'] = [str(ctx.Simple_name(0)), str(ctx.Simple_name(1))]

            elif ctx.Simple_name(0):
                self.factor['comp_id'] = [str(ctx.Simple_name(0))]

            elif ctx.Simple_names(0):
                self.factor['comp_ids'] = [str(ctx.Simple_names(0))]

        elif ctx.SegIdentifier():
            if self.__verbose:
                print("  " * self.depth + "--> segidentifier")
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
                    _chainId = to_re_exp(chainId)
                    self.factor['chain_id'] = [ps['chain_id'] for ps in self.__polySeq
                                               if re.match(_chainId, ps['chain_id'])]
                if len(self.factor['chain_id']) == 0:
                    self.factor['atom_id'] = [None]
                    self.warningMessage += f"[Invalid data] {self.__getCurrentRestraint()}"\
                        "Couldn't specify segment name "\
                        f"'{chainId}' in the coordinates.\n"  # do not use 'chainId!r' expression, '%' code throws ValueError

        elif ctx.Sfbox():
            pass

        elif ctx.Store_1() or ctx.Store_2() or ctx.Store_3()\
                or ctx.Store_4() or ctx.Store_5() or ctx.Store_6()\
                or ctx.Store_7() or ctx.Store_8() or ctx.Store_9():
            if self.__verbose:
                print("  " * self.depth + "--> store[1-9]")
            self.factor['atom_id'] = [None]
            self.warningMessage += f"[Unavailable resource] {self.__getCurrentRestraint()}"\
                "The 'store[1-9]' clause has no effect "\
                "because the internal vector statement is fragile in the restraint file.\n"

        elif ctx.Tag():
            if self.__verbose:
                print("  " * self.depth + "--> tag")
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
                                                      'value': self.__representativeModelId}
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
        if self.__cur_subtype == 'nbase':
            return f"[Check the {self.nbaseRestraints}th row of residue-residue position/orientation database restraints] "
        if self.__cur_subtype == 'ang':
            return f"[Check the {self.angRestraints}th row of angle database restraints] "
        return ''

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

        if self.nbaseStatements == 0 and self.nbaseRestraints > 0:
            self.nbaseStatements = 1

        if self.angStatements == 0 and self.angRestraints > 0:
            self.angStatements = 1

        contentSubtype = {'dist_restraint': self.distStatements,
                          'dihed_restraint': self.dihedStatements,
                          'rdc_restraint': self.rdcStatements,
                          'plane_restraint': self.planeStatements,
                          'jcoup_restraint': self.jcoupStatements,
                          'hvycs_restraint': self.hvycsStatements,
                          'procs_restraint': self.procsStatements,
                          'rama_restraint': self.ramaStatements,
                          'diff_restraint': self.diffStatements,
                          'nbase_restraint': self.nbaseStatements,
                          'ang_restraint': self.angStatements
                          }

        return {k: v for k, v in contentSubtype.items() if v > 0}

# del CnsMRParser
