##
# File: XplorMRParserListener.py
# Date: 27-Jan-2022
#
# Updates:
# Generated from XplorMRParser.g4 by ANTLR 4.9
""" ParserLister class for XPLOR-NIH MR files.
    @author: Masashi Yokochi
"""
import sys
import re
import numpy as np

from antlr4 import ParseTreeListener
from wwpdb.utils.nmr.mr.XplorMRParser import XplorMRParser

from wwpdb.utils.config.ConfigInfo import getSiteId
from wwpdb.utils.config.ConfigInfoApp import ConfigInfoAppCommon
from wwpdb.utils.nmr.io.ChemCompIo import ChemCompReader
from rmsd.calculate_rmsd import (int_atom, ELEMENT_WEIGHTS)  # noqa: F401 pylint: disable=no-name-in-module, import-error


def to_np_array(atom):
    """ Return Numpy array of a given Cartesian coordinate in {'x': float, 'y': float, 'z': float} format.
    """

    return np.asarray([atom['x'], atom['y'], atom['z']])


def to_re_exp(string):
    """ Return regular expression for a given string including XPLOR-NIH wildcard format.
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


# This class defines a complete listener for a parse tree produced by XplorMRParser.
class XplorMRParserListener(ParseTreeListener):

    __verbose = None
    __lfh = None

    distRestraints = 0      # XPLOR-NIH: Distance restraints
    dihedRestraints = 0     # XPLOR-NIH: Dihedral angle restraints
    rdcRestraints = 0       # XPLOR-NIH: Residual Dipolar Couplings
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

    distStatements = 0      # XPLOR-NIH: Distance restraints
    dihedStatements = 0     # XPLOR-NIH: Dihedral angle restraints
    rdcStatements = 0       # XPLOR-NIH: Residual Dipolar Couplings
    planeStatements = 0     # XPLOR-NIH: Planality restraints
    adistStatements = 0     # XPLOR-NIH: Antidiatance restraints
    jcoupStatements = 0     # XPLOR-NIH: Scalar J-coupling restraints
    hvycsStatements = 0     # XPLOR-NIH: Carbon chemical shift restraints
    procsStatements = 0     # XPLOR-NIH: Proton chemical shift restraints
    ramaStatements = 0      # XPLOR-NIH: Dihedral angle database restraints
    radiStatements = 0      # XPLOR-NIH: Radius of gyration restraints
    diffStatements = 0      # XPLOR-NIH: Diffusion anisotropy restraints
    nbaseStatements = 0     # XPLOR-NIH: Residue-residue position/orientation database restraints
    csaStatements = 0       # XPLOR-NIH: (Pseudo) Chemical shift anisotropy restraints
    angStatements = 0       # XPLOR-NIH: Angle database restraints
    preStatements = 0       # XPLOR-NIH: Paramagnetic relaxation enhancement restraints
    pcsStatements = 0       # XPLOR-NIH: Paramagnetic pseudocontact shift restraints
    prdcStatements = 0      # XPLOR-NIH: Paramagnetic residual dipolar coupling restraints
    pangStatements = 0      # XPLOR-NIH: Paramagnetic orientation restraints
    pccrStatements = 0      # XPLOR-NIH: Paramagnetic cross-correlation rate restraints
    hbondStatements = 0     # XPLOR-NIH: Hydrogen bond geometry restraints

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

    # ChemComp reader
    __ccR = None

    __lastCompId = None
    __lastCompIdTest = False
    __lastChemCompDict = None
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
    __ccbAromaticFlag = None

    # CIF reader
    __cR = None

    # data item name for model ID in 'atom_site' category
    __modelNumName = None
    # representative model id
    __representativeModelId = 1
    # total number of models
    # __totalModels = 0

    # polymer sequences in the coordinate file generated by NmrDpUtility.__extractCoordPolymerSequence()
    __polySeq = None

    # atom selection-expressions in a statement
    atomSelExpr = [[None, None]]

    # pointers for each atom selection-expression in a statement
    depthSelExpr = -1
    columnSelExpr = [-1]
    columnTerm = [-1]
    columnFactor = [-1]

    factor = None

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

        except Exception as e:

            if self.__verbose:
                self.__lfh.write(f"+XplorMRParserListener() ++ Error  - {str(e)}\n")

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
                    self.__lfh.write(f"+XplorMRParserListener() ++ Error - {str(e)}\n")

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

        aromaticFlag = next(d for d in self.__chemCompBondDict if d[0] == '_chem_comp_bond.pdbx_aromatic_flag')
        self.__ccbAromaticFlag = self.__chemCompBondDict.index(aromaticFlag)

    def __updateChemCompDict(self, compId):
        """ Update CCD information for a given comp_id.
            @return: True for successfully update CCD information or False for the case a given comp_id does not exist in CCD
        """

        compId = compId.upper()

        if compId != self.__lastCompId:
            self.__lastCompIdTest = False if '_' in compId else self.__ccR.setCompId(compId)
            self.__lastCompId = compId

            if self.__lastCompIdTest:
                self.__lastChemCompDict = self.__ccR.getChemCompDict()
                self.__lastChemCompAtoms = self.__ccR.getAtomList()
                self.__lastChemCompBonds = self.__ccR.getBonds()

        return self.__lastCompIdTest

    # Enter a parse tree produced by XplorMRParser#xplor_nih_mr.
    def enterXplor_nih_mr(self, ctx: XplorMRParser.Xplor_nih_mrContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#xplor_nih_mr.
    def exitXplor_nih_mr(self, ctx: XplorMRParser.Xplor_nih_mrContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#distance_restraint.
    def enterDistance_restraint(self, ctx: XplorMRParser.Distance_restraintContext):  # pylint: disable=unused-argument
        self.distStatements += 1

    # Exit a parse tree produced by XplorMRParser#distance_restraint.
    def exitDistance_restraint(self, ctx: XplorMRParser.Distance_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#dihedral_angle_restraint.
    def enterDihedral_angle_restraint(self, ctx: XplorMRParser.Dihedral_angle_restraintContext):  # pylint: disable=unused-argument
        self.dihedStatements += 1

    # Exit a parse tree produced by XplorMRParser#dihedral_angle_restraint.
    def exitDihedral_angle_restraint(self, ctx: XplorMRParser.Dihedral_angle_restraintContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#rdc_restraint.
    def enterRdc_restraint(self, ctx: XplorMRParser.Rdc_restraintContext):  # pylint: disable=unused-argument
        self.rdcStatements += 1

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
        self.angStatements += 1

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
    def enterNoe_statement(self, ctx: XplorMRParser.Noe_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#noe_statement.
    def exitNoe_statement(self, ctx: XplorMRParser.Noe_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#noe_assign.
    def enterNoe_assign(self, ctx: XplorMRParser.Noe_assignContext):
        self.distRestraints += 1

        selExprSize = 2
        while ctx.selection(selExprSize) is not None:
            selExprSize += 1

        self.depthSelExpr = 0

        while selExprSize > len(self.atomSelExpr[0]):
            self.atomSelExpr[0].append(None)

        for atomSel in self.atomSelExpr[0]:
            if atomSel is None:
                atomSel = []
            else:
                atomSel.clear()

        # """
        # d_target = float(ctx.Real(0))
        # d_minus = float(ctx.Real(1))
        # d_plus = float(ctx.Real(2))
        # """

    # Exit a parse tree produced by XplorMRParser#noe_assign.
    def exitNoe_assign(self, ctx: XplorMRParser.Noe_assignContext):  # pylint: disable=unused-argument
        self.columnSelExpr[self.depthSelExpr] = -1

    # Enter a parse tree produced by XplorMRParser#predict_statement.
    def enterPredict_statement(self, ctx: XplorMRParser.Predict_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#predict_statement.
    def exitPredict_statement(self, ctx: XplorMRParser.Predict_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#dihedral_statement.
    def enterDihedral_statement(self, ctx: XplorMRParser.Dihedral_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#dihedral_statement.
    def exitDihedral_statement(self, ctx: XplorMRParser.Dihedral_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#dihedral_assign.
    def enterDihedral_assign(self, ctx: XplorMRParser.Dihedral_assignContext):  # pylint: disable=unused-argument
        self.dihedRestraints += 1

    # Exit a parse tree produced by XplorMRParser#dihedral_assign.
    def exitDihedral_assign(self, ctx: XplorMRParser.Dihedral_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#sani_statement.
    def enterSani_statement(self, ctx: XplorMRParser.Sani_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#sani_statement.
    def exitSani_statement(self, ctx: XplorMRParser.Sani_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#sani_assign.
    def enterSani_assign(self, ctx: XplorMRParser.Sani_assignContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1

    # Exit a parse tree produced by XplorMRParser#sani_assign.
    def exitSani_assign(self, ctx: XplorMRParser.Sani_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#xdip_statement.
    def enterXdip_statement(self, ctx: XplorMRParser.Xdip_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#xdip_statement.
    def exitXdip_statement(self, ctx: XplorMRParser.Xdip_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#xdip_assign.
    def enterXdip_assign(self, ctx: XplorMRParser.Xdip_assignContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1

    # Exit a parse tree produced by XplorMRParser#xdip_assign.
    def exitXdip_assign(self, ctx: XplorMRParser.Xdip_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#vean_statement.
    def enterVean_statement(self, ctx: XplorMRParser.Vean_statementContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#vean_statement.
    def exitVean_statement(self, ctx: XplorMRParser.Vean_statementContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#vean_assign.
    def enterVean_assign(self, ctx: XplorMRParser.Vean_assignContext):  # pylint: disable=unused-argument
        self.rdcRestraints += 1

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

    # Exit a parse tree produced by XplorMRParser#rama_assign.
    def exitRama_assign(self, ctx: XplorMRParser.Rama_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#collapse_statement.
    def enterCollapse_statement(self, ctx: XplorMRParser.Collapse_statementContext):  # pylint: disable=unused-argument
        self.radiRestraints += 1

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
        self.angRestraints += 1

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

    # Exit a parse tree produced by XplorMRParser#hbond_assign.
    def exitHbond_assign(self, ctx: XplorMRParser.Hbond_assignContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#selection.
    def enterSelection(self, ctx: XplorMRParser.SelectionContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#selection.
    def exitSelection(self, ctx: XplorMRParser.SelectionContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by XplorMRParser#selection_expression.
    def enterSelection_expression(self, ctx: XplorMRParser.Selection_expressionContext):  # pylint: disable=unused-argument
        self.columnSelExpr[self.depthSelExpr] += 1

    # Exit a parse tree produced by XplorMRParser#selection_expression.
    def exitSelection_expression(self, ctx: XplorMRParser.Selection_expressionContext):  # pylint: disable=unused-argument
        self.columnTerm[self.depthSelExpr] = -1

    # Enter a parse tree produced by XplorMRParser#term.
    def enterTerm(self, ctx: XplorMRParser.TermContext):  # pylint: disable=unused-argument
        self.columnTerm[self.depthSelExpr] += 1

        self.factor = {}

    # Exit a parse tree produced by XplorMRParser#term.
    def exitTerm(self, ctx: XplorMRParser.TermContext):  # pylint: disable=unused-argument
        self.columnFactor[self.depthSelExpr] = -1

        self.consumeFactor_expressions()

        print(self.factor)

    def consumeFactor_expressions(self, clauseName='atom selection expression'):
        """ Consume factor expressions as atom selection if possible.
        """

        if 'atom_selection' in self.factor or len(self.factor) == 0:
            return

        if 'chain_id' not in self.factor or len(self.factor['chain_id']) == 0:
            self.factor['chain_id'] = [ps['chain_id'] for ps in self.__polySeq]

        if 'seq_id' not in self.factor and 'seq_ids' not in self.factor:
            if 'comp_ids' in self.factor and len(self.factor['comp_ids']) > 0\
               and ('comp_id' not in self.factor or len(self.factor['comp_id']) == 0):
                lenCompIds = len(self.factor['comp_ids'])
                _compIdSelect = set()
                for chainId in self.factor['chain_id']:
                    ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chainId), None)
                    if ps is not None:
                        for realSeqId in ps['seq_id']:
                            realCompId = ps['comp_id'][ps['seq_id'].index(realSeqId)]
                            if (lenCompIds == 1 and re.match(self.factor['comp_ids'][0], realCompId))\
                               or (lenCompIds == 2 and self.factor['comp_ids'][0] <= realCompId <= self.factor['comp_ids'][1]):
                                _compIdSelect.add(realCompId)
                self.factor['comp_id'] = list(_compIdSelect)
                del self.factor['comp_ids']

        if 'seq_ids' in self.factor and len(self.factor['seq_ids']) > 0\
           and ('seq_id' not in self.factor or len(self.factor['seq_id']) == 0):
            seqIds = []
            for chainId in self.factor['chain_id']:
                ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chainId), None)
                if ps is not None:
                    for realSeqId in ps['seq_id']:
                        if 'comp_id' in self.factor and len(self.factor['comp_id']) > 0:
                            realCompId = ps['comp_id'][ps['seq_id'].index(realSeqId)]
                            if realCompId not in self.factor['comp_id']:
                                continue
                        seqId = self.factor['seq_ids'][0]
                        _seqId = to_re_exp(seqId)
                        if re.match(_seqId, str(realSeqId)):
                            seqIds.append(realSeqId)
            self.factor['seq_id'] = list(set(seqIds))
            del self.factor['seq_ids']

        if 'seq_id' not in self.factor or len(self.factor['seq_id']) == 0:
            seqIds = []
            for chainId in self.factor['chain_id']:
                ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chainId), None)
                if ps is not None:
                    for realSeqId in ps['seq_id']:
                        if 'comp_id' in self.factor and len(self.factor['comp_id']) > 0:
                            realCompId = ps['comp_id'][ps['seq_id'].index(realSeqId)]
                            if realCompId not in self.factor['comp_id']:
                                continue
                        seqIds.append(realSeqId)
            self.factor['seq_id'] = list(set(seqIds))

        if 'atom_id' not in self.factor and 'atom_ids' not in self.factor:
            if 'type_symbols' in self.factor and len(self.factor['type_symbols']) > 0\
               and ('type_symbol' not in self.factor or len(self.factor['type_symbol']) == 0):
                lenTypeSymbols = len(self.factor['type_symbols'])
                _typeSymbolSelect = set()
                _compIdSelect = set()
                for chainId in self.factor['chain_id']:
                    ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chainId), None)
                    if ps is not None:
                        _compIdSelect |= set(ps['comp_id'])
                for compId in _compIdSelect:
                    if self.__updateChemCompDict(compId):
                        for cca in self.__lastChemCompAtoms:
                            realTypeSymbol = cca[self.__ccaTypeSymbol]
                            if (lenTypeSymbols == 1 and re.match(self.factor['type_symbols'][0], realTypeSymbol))\
                               or (lenTypeSymbols == 2 and self.factor['type_symbols'][0] <= realTypeSymbol <= self.factor['type_symbols'][1]):
                                _typeSymbolSelect.add(realTypeSymbol)
                self.factor['type_symbol'] = list(_typeSymbolSelect)
                if len(self.factor['type_symbol']) == 0:
                    self.factor['atom_id'] = [None]
                del self.factor['type_symbols']

            if 'type_symbol' in self.factor and len(self.factor['type_symbol']) > 0:
                _atomIdSelect = set()
                _compIdSelect = set()
                for chainId in self.factor['chain_id']:
                    ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chainId), None)
                    if ps is not None:
                        _compIdSelect |= set(ps['comp_id'])
                for compId in _compIdSelect:
                    if self.__updateChemCompDict(compId):
                        for cca in self.__lastChemCompAtoms:
                            if cca[self.__ccaTypeSymbol] in self.factor['type_symbol']\
                               and cca[self.__ccaLeavingAtomFlag] != 'Y':
                                _atomIdSelect.add(cca[self.__ccaAtomId])
                self.factor['atom_id'] = list(_atomIdSelect)
                if len(self.factor['atom_id']) == 0:
                    self.factor['atom_id'] = [None]

        if 'atom_ids' in self.factor and len(self.factor['atom_ids']) > 0\
           and ('atom_id' not in self.factor or len(self.factor['atom_id']) == 0):
            lenAtomIds = len(self.factor['atom_ids'])
            _compIdSelect = set()
            for chainId in self.factor['chain_id']:
                ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chainId), None)
                if ps is not None:
                    for realSeqId in ps['seq_id']:
                        realCompId = ps['comp_id'][ps['seq_id'].index(realSeqId)]
                        if 'comp_id' in self.factor and len(self.factor['comp_id']) > 0:
                            if realCompId not in self.factor['comp_id']:
                                continue
                        _compIdSelect.add(realCompId)

            _atomIdSelect = set()
            for compId in _compIdSelect:
                if self.__updateChemCompDict(compId):
                    for cca in self.__lastChemCompAtoms:
                        if cca[self.__ccaLeavingAtomFlag] != 'Y':
                            realAtomId = cca[self.__ccaAtomId]
                            if (lenAtomIds == 1 and re.match(self.factor['atom_ids'][0], realAtomId))\
                               or (lenAtomIds == 2 and self.factor['atom_ids'][0] <= realAtomId <= self.factor['atom_ids'][1]):
                                _atomIdSelect.add(realAtomId)
            self.factor['atom_id'] = list(_atomIdSelect)
            if len(self.factor['atom_id']) == 0:
                self.factor['atom_id'] = [None]
            del self.factor['atom_ids']

        if 'atom_id' not in self.factor or len(self.factor['atom_id']) == 0:
            _compIdSelect = set()
            for chainId in self.factor['chain_id']:
                ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chainId), None)
                if ps is not None:
                    for realSeqId in ps['seq_id']:
                        realCompId = ps['comp_id'][ps['seq_id'].index(realSeqId)]
                        if 'comp_id' in self.factor and len(self.factor['comp_id']) > 0:
                            if realCompId not in self.factor['comp_id']:
                                continue
                        _compIdSelect.add(realCompId)

            _atomIdSelect = set()
            for compId in _compIdSelect:
                if self.__updateChemCompDict(compId):
                    for cca in self.__lastChemCompAtoms:
                        if cca[self.__ccaLeavingAtomFlag] != 'Y':
                            realAtomId = cca[self.__ccaAtomId]
                            _atomIdSelect.add(realAtomId)
            self.factor['atom_id'] = list(_atomIdSelect)
            if len(self.factor['atom_id']) == 0:
                self.factor['atom_id'] = [None]

        _atomSelection = []

        try:

            if self.factor['atom_id'][0] is not None:
                for chainId in self.factor['chain_id']:
                    for seqId in self.factor['seq_id']:
                        for atomId in self.factor['atom_id']:
                            _atom =\
                                self.__cR.getDictListWithFilter('atom_site',
                                                                [{'name': 'label_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                                 {'name': 'type_symbol', 'type': 'str'},
                                                                 ],
                                                                [{'name': 'auth_asym_id', 'type': 'str', 'value': chainId},
                                                                 {'name': 'auth_seq_id', 'type': 'int', 'value': seqId},
                                                                 {'name': 'label_atom_id', 'type': 'str', 'value': atomId},
                                                                 {'name': self.__modelNumName, 'type': 'int',
                                                                  'value': self.__representativeModelId}
                                                                 ])

                            if len(_atom) == 1:
                                if ('comp_id' not in self.factor or _atom[0]['comp_id'] in self.factor['comp_id'])\
                                   and ('type_symbol' not in self.factor or _atom[0]['type_symbol'] in self.factor['type_symbol']):
                                    _atomSelection.append({'chain_id': chainId, 'seq_id': seqId, 'comp_id': _atom[0]['comp_id'], 'atom_id': atomId})

                            else:
                                ps = next((ps for ps in self.__polySeq if ps['chain_id'] == chainId), None)
                                if ps is not None and seqId in ps['seq_id']:
                                    compId = ps['comp_id'][ps['seq_id'].index(seqId)]
                                    if self.__updateChemCompDict(compId) and ('comp_id' not in self.factor or compId in self.factor['comp_id']):
                                        cca = next((cca for cca in self.__lastChemCompAtoms if cca[self.__ccaAtomId] == atomId), None)
                                        if cca is not None and ('type_symbol' not in self.factor or cca[self.__ccaTypeSymbol] in self.factor['type_symbol']):
                                            _atomSelection.append({'chain_id': chainId, 'seq_id': seqId, 'comp_id': compId, 'atom_id': atomId})

        except Exception as e:
            if self.__verbose:
                self.__lfh.write(f"+XplorMRParserListener.consumeFactor_expressions() ++ Error  - {str(e)}\n")

        atomSelection = []
        for atom in _atomSelection:
            if atom not in atomSelection:
                atomSelection.append(atom)

        self.factor['atom_selection'] = atomSelection

        if len(self.factor['atom_selection']) == 0:
            self.warningMessage += f"[Invalid data] The {clauseName} has no effect.\n"

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

    # Enter a parse tree produced by XplorMRParser#factor.
    def enterFactor(self, ctx: XplorMRParser.FactorContext):
        self.columnFactor[self.depthSelExpr] += 1
        if ctx.selection_expression() is not None:
            self.depthSelExpr += 1

            depth = self.depthSelExpr

            if depth + 1 > len(self.atomSelExpr):
                self.atomSelExpr.append([])  # add empty list
                self.atomSelExpr[depth].append(None)

                for atomSel in self.atomSelExpr[depth]:
                    if atomSel is None:
                        atomSel = []
                    else:
                        atomSel.clear()

                self.columnSelExpr.append(-1)
                self.columnTerm.append(-1)
                self.columnFactor.append(-1)
        else:  # @debug
            depth = self.depthSelExpr

        # @debug
        # if self.__verbose:
        #    print(f"{depth=} {self.columnSelExpr[depth]=} {self.columnTerm[depth]=} {self.columnFactor[depth]=}")

    # Exit a parse tree produced by XplorMRParser#factor.
    def exitFactor(self, ctx: XplorMRParser.FactorContext):

        if ctx.All():

            try:

                self.factor['atom_selection'] =\
                    self.__cR.getDictListWithFilter('atom_site',
                                                    [{'name': 'auth_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                                     {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                                     {'name': 'label_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                     {'name': 'label_atom_id', 'type': 'str', 'alt_name': 'atom_id'}
                                                     ],
                                                    [{'name': self.__modelNumName, 'type': 'int',
                                                      'value': self.__representativeModelId}
                                                     ])

                if len(self.factor['atom_selection']) == 0:
                    self.warningMessage += "[Invalid data] The 'all' clause has no effect.\n"
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

        elif ctx.Around():
            around = float(str(ctx.Real()))
            _atomSelection = []

            self.consumeFactor_expressions("atom selection expression before the 'around' clause")

            if 'atom_selection' in self.factor:

                for _atom in self.factor['atom_selection']:

                    try:

                        _origin =\
                            self.__cR.getDictListWithFilter('atom_site',
                                                            [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                             {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                             {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                                                             ],
                                                            [{'name': 'auth_asym_id', 'type': 'str', 'value': _atom['chain_id']},
                                                             {'name': 'auth_seq_id', 'type': 'int', 'value': _atom['seq_id']},
                                                             {'name': 'label_atom_id', 'type': 'str', 'value': _atom['atom_id']},
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
                            self.__lfh.write(f"+XplorMRParserListener.exitFactor() ++ Error  - {str(e)}\n")

                if len(self.factor['atom_selection']) > 0:
                    atomSelection = []
                    for atom in _atomSelection:
                        if atom not in atomSelection:
                            atomSelection.append(atom)

                    self.factor['atom_selection'] = atomSelection

                    if len(self.factor['atom_selection']) == 0:
                        self.warningMessage += "[Invalid data] The 'around' clause has no effect.\n"

        elif ctx.Atom():
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
                self.warningMessage += "[Invalid data] Couldn't specify segment name "\
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

            self.consumeFactor_expressions("'atom' clause")

        elif ctx.Attribute():
            absolute = bool(ctx.Abs())
            _attr_prop = str(ctx.Simple_name(0))
            attr_prop = _attr_prop.lower()
            opCode = str(ctx.Comparison_ops())
            attr_value = float(str(ctx.Real()))

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
                self.factor['atom_selection'] =\
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

            elif attr_prop.startswith('bcom')\
                    or attr_prop.startswith('qcom')\
                    or attr_prop.startswith('xcom')\
                    or attr_prop.startswith('ycom')\
                    or attr_prop.startswith('zcom'):  # BCOMP, QCOMP, XCOMP, YCOMP, ZCOM`
                self.warningMessage += f"[Unavailable resource] The attribute property {_attr_prop!r} "\
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
                self.factor['atom_selection'] =\
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

            elif attr_prop in ('dx', 'dy', 'dz', 'harm'):
                self.warningMessage += f"[Unavailable resource] The attribute property {_attr_prop!r} "\
                    "related to atomic force of each atom is not possessed by the static coordinate file.\n"
                validProp = False

            elif attr_prop.startswith('fbet'):  # FBETA
                self.warningMessage += f"[Unavailable resource] The attribute property {_attr_prop!r} "\
                    "related to the Langevin dynamics (nonzero friction coefficient) is not possessed by the static coordinate file.\n"
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

                self.factor['atom_selection'] =\
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
                self.factor['atom_selection'] =\
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

            elif attr_prop in ('refx', 'refy', 'refz', 'rmsd'):
                self.warningMessage += f"[Unavailable resource] The attribute property {_attr_prop!r} "\
                    "requires a reference coordinate set.\n"
                validProp = False

            elif attr_prop == ('vx', 'vy', 'vz'):
                self.warningMessage += f"[Unavailable resource] The attribute property {_attr_prop!r} "\
                    "related to current velocities of each atom is not possessed by the static coordinate file.\n"
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
                self.factor['atom_selection'] =\
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

            else:
                self.warningMessage += f"[Syntax error] The attribute property {_attr_prop!r} is unknown.\n"
                validProp = False

            if validProp and len(self.factor['atom_selection']) == 0:
                _absolute = ' abs ' if absolute else ''
                self.warningMessage += f"[Invalid data] The 'attribute' clause ('{_attr_prop}{_absolute} {opCode} {attr_value}') has no effect.\n"

        elif ctx.BondedTo():
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
                                                                [{'name': 'auth_asym_id', 'type': 'str', 'value': chainId},
                                                                 {'name': 'auth_seq_id', 'type': 'int', 'value': seqId},
                                                                 {'name': 'label_atom_id', 'type': 'str', 'value': _atomId},
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
                                                                [{'name': 'auth_asym_id', 'type': 'str', 'value': chainId},
                                                                 {'name': 'auth_seq_id', 'type': 'int', 'value': seqId},
                                                                 {'name': 'label_atom_id', 'type': 'str', 'value': atomId},
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
                                                                                        [{'name': 'auth_asym_id', 'type': 'str', 'value': chainId},
                                                                                         {'name': 'auth_seq_id', 'type': 'int', 'value': _seqId},
                                                                                         {'name': 'label_atom_id', 'type': 'str', 'value': _atomId},
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
                    self.warningMessage += "[Invalid data] The 'bondedto' clause has no effect.\n"

            else:
                self.warningMessage += "[Invalid data] The 'bondedto' clause has no effect because no atom is selected.\n"

        elif ctx.ByGroup():
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
                                                                [{'name': 'auth_asym_id', 'type': 'str', 'value': chainId},
                                                                 {'name': 'auth_seq_id', 'type': 'int', 'value': seqId},
                                                                 {'name': 'label_atom_id', 'type': 'str', 'value': atomId},
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
                                                                        [{'name': 'auth_asym_id', 'type': 'str', 'value': chainId},
                                                                         {'name': 'auth_seq_id', 'type': 'int', 'value': seqId},
                                                                         {'name': 'label_atom_id', 'type': 'str', 'value': _atomId},
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
                    self.warningMessage += "[Invalid data] The 'bygroup' clause has no effect.\n"

                self.factor['atom_selection'] = atomSelection

            else:
                self.warningMessage += "[Invalid data] The 'bygroup' clause has no effect because no atom is selected.\n"

        elif ctx.ByRes():
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
                                                        [{'name': 'auth_asym_id', 'type': 'str', 'value': chainId},
                                                         {'name': 'auth_seq_id', 'type': 'int', 'value': seqId},
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
                    self.warningMessage += "[Invalid data] The 'byres' clause has no effect.\n"

            else:
                self.warningMessage += "[Invalid data] The 'byres' clause has no effect because no atom is selected.\n"

        elif ctx.Chemical():
            if ctx.Colon():  # range expression
                self.factor['type_symbols'] = [str(ctx.Simple_name(0)), str(ctx.Simple_name(1))]

            elif ctx.Simple_name(0):
                self.factor['type_symbol'] = [str(ctx.Simple_name(0))]

            elif ctx.Simple_names(0):
                self.factor['type_symbols'] = [str(ctx.Simple_names(0))]

            self.consumeFactor_expressions("'chemical' clause")

        elif ctx.Hydrogen():
            pass

        elif ctx.Id():
            pass

        elif ctx.Known():
            pass

        elif ctx.Name():
            if ctx.Colon():  # range expression
                self.factor['atom_ids'] = [str(ctx.Simple_name(0)), str(ctx.Simple_name(1))]

            elif ctx.Simple_name(0):
                self.factor['atom_id'] = [str(ctx.Simple_name(0))]

            elif ctx.Simple_names(0):
                self.factor['atom_ids'] = [str(ctx.Simple_names(0))]

        elif ctx.Not_op():
            pass

        elif ctx.Point():
            pass

        elif ctx.Cut():
            pass

        elif ctx.Previous():
            pass

        elif ctx.Pseudo():
            pass

        elif ctx.Residue():
            if ctx.Colon():  # range expression
                self.factor['seq_id'] = list(range(int(str(ctx.Integer(0))), int(str(ctx.Integer(0))) + 1))

            elif ctx.Integer(0):
                self.factor['seq_id'] = [int(str(ctx.Integer(0)))]

            elif ctx.Integers():
                self.factor['seq_ids'] = [str(ctx.Integers())]

        elif ctx.Resname():
            if ctx.Colon():  # range expression
                self.factor['comp_ids'] = [str(ctx.Simple_name(0)), str(ctx.Simple_name(1))]

            elif ctx.Simple_name(0):
                self.factor['comp_id'] = [str(ctx.Simple_name(0))]

            elif ctx.Simple_names(0):
                self.factor['comp_ids'] = [str(ctx.Simple_names(0))]

        elif ctx.Saround():
            pass

        elif ctx.SegIdentifier():
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
                    self.warningMessage += f"[Invalid data] Couldn't specify segment name {begChainId:!r}:{endChainId:!r} in the coordinates.\n"

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
                    self.warningMessage += "[Invalid data] Couldn't specify segment name "\
                        f"'{chainId}' in the coordinates.\n"  # do not use 'chainId!r' expression, '%' code throws ValueError

        elif ctx.Store_1() or ctx.Store_2() or ctx.Store_3()\
                or ctx.Store_4() or ctx.Store_5() or ctx.Store_6()\
                or ctx.Store_7() or ctx.Store_8() or ctx.Store_9():
            self.warningMessage += "[Unavailable resource] The 'store#' clause has no effect because no vector statement is available.\n"

        elif ctx.Tag():
            pass

        if ctx.selection_expression() is not None:
            self.depthSelExpr -= 1

    # Enter a parse tree produced by XplorMRParser#vector_3d.
    def enterVector_3d(self, ctx: XplorMRParser.Vector_3dContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by XplorMRParser#vector_3d.
    def exitVector_3d(self, ctx: XplorMRParser.Vector_3dContext):  # pylint: disable=unused-argument
        pass

    # The followings are extensions.
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

        contetSubtype = {'dist_restraint': self.distStatements,
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

        return {k: v for k, v in contetSubtype.items() if v > 0}

# del XplorMRParser
