##
# File: ChemCompUtil.py
# Date: 18-Feb-2022
#
# Updates:
##
""" Wrapper class for retrieving chemical component dictionary.
    @author: Masashi Yokochi
"""
import sys

from wwpdb.utils.config.ConfigInfo import getSiteId
from wwpdb.utils.config.ConfigInfoApp import ConfigInfoAppCommon
from wwpdb.utils.nmr.io.ChemCompIo import ChemCompReader


class ChemCompUtil:
    """ Wrapper class for retrieving chemical component dictionary.
    """

    def __init__(self, verbose=False, log=sys.stderr):
        _cICommon = ConfigInfoAppCommon(getSiteId())
        _ccCvsPath = _cICommon.get_site_cc_cvs_path()

        self.__ccR = ChemCompReader(verbose, log)
        self.__ccR.setCachePath(_ccCvsPath)

        self.lastCompId = None
        self.lastStatus = False
        self.lastChemCompDict = None
        self.lastAtomList = None
        self.lastBonds = None

        # taken from wwpdb.apps.ccmodule.io.ChemCompIo
        _chemCompAtomDict = [
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
            ('_chem_comp_atom.pdbx_ordinal', '%s', 'str', ' ')
        ]

        atomId = next(d for d in _chemCompAtomDict if d[0] == '_chem_comp_atom.atom_id')
        self.ccaAtomId = _chemCompAtomDict.index(atomId)

        aromaticFlag = next(d for d in _chemCompAtomDict if d[0] == '_chem_comp_atom.pdbx_aromatic_flag')
        self.ccaAromaticFlag = _chemCompAtomDict.index(aromaticFlag)

        leavingAtomFlag = next(d for d in _chemCompAtomDict if d[0] == '_chem_comp_atom.pdbx_leaving_atom_flag')
        self.ccaLeavingAtomFlag = _chemCompAtomDict.index(leavingAtomFlag)

        typeSymbol = next(d for d in _chemCompAtomDict if d[0] == '_chem_comp_atom.type_symbol')
        self.ccaTypeSymbol = _chemCompAtomDict.index(typeSymbol)

        cartnX = next(d for d in _chemCompAtomDict if d[0] == '_chem_comp_atom.model_Cartn_x')
        cartnY = next(d for d in _chemCompAtomDict if d[0] == '_chem_comp_atom.model_Cartn_y')
        cartnZ = next(d for d in _chemCompAtomDict if d[0] == '_chem_comp_atom.model_Cartn_z')
        self.ccaCartnX = _chemCompAtomDict.index(cartnX)
        self.ccaCartnY = _chemCompAtomDict.index(cartnY)
        self.ccaCartnZ = _chemCompAtomDict.index(cartnZ)

        # taken from wwpdb.apps.ccmodule.io.ChemCompIo
        _chemCompBondDict = [
            ('_chem_comp_bond.comp_id', '%s', 'str', ''),
            ('_chem_comp_bond.atom_id_1', '%s', 'str', ''),
            ('_chem_comp_bond.atom_id_2', '%s', 'str', ''),
            ('_chem_comp_bond.value_order', '%s', 'str', ''),
            ('_chem_comp_bond.pdbx_aromatic_flag', '%s', 'str', ''),
            ('_chem_comp_bond.pdbx_stereo_config', '%s', 'str', ''),
            ('_chem_comp_bond.pdbx_ordinal', '%s', 'str', '')
        ]

        atomId1 = next(d for d in _chemCompBondDict if d[0] == '_chem_comp_bond.atom_id_1')
        self.ccbAtomId1 = _chemCompBondDict.index(atomId1)

        atomId2 = next(d for d in _chemCompBondDict if d[0] == '_chem_comp_bond.atom_id_2')
        self.ccbAtomId2 = _chemCompBondDict.index(atomId2)

        aromaticFlag = next(d for d in _chemCompBondDict if d[0] == '_chem_comp_bond.pdbx_aromatic_flag')
        self.ccbAromaticFlag = _chemCompBondDict.index(aromaticFlag)

        self.__cache = {}

    def updateChemCompDict(self, compId):
        """ Update CCD information for a given comp_id.
            @return: True for successfully update CCD information or False for the case a given comp_id does not exist in CCD
        """

        compId = compId.upper()

        if compId != self.lastCompId:
            self.lastStatus = False if '_' in compId else self.__ccR.setCompId(compId)
            self.lastCompId = compId

            if self.lastStatus:
                if compId in self.__cache:
                    self.lastChemCompDict = self.__cache[compId]['chem_comp']
                    self.lastAtomList = self.__cache[compId]['chem_comp_atom']
                    self.lastBonds = self.__cache[compId]['chem_comp_bond']
                else:
                    self.lastChemCompDict = self.__ccR.getChemCompDict()
                    self.lastAtomList = self.__ccR.getAtomList()
                    self.lastBonds = self.__ccR.getBonds()
                    self.__cache[compId] = {'chem_comp': self.lastChemCompDict,
                                            'chem_comp_atom': self.lastAtomList,
                                            'chem_comp_bond': self.lastBonds}

        return self.lastStatus
