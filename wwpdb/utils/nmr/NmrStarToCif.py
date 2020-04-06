#
# File: NmrStarToCif.py
# Date: 03-Apr-2020
#
# Updates:
# 06-Apr-2020  M. Yokochi - add support for Original_pdb_* items in restraints/peak lists
##
""" Wrapper class for NMR-STAR to CIF converter.
    @author: Masashi Yokochi
"""
import sys
import logging
from mmcif.io.IoAdapterPy import IoAdapterPy
from wwpdb.utils.nmr.io.mmCIFUtil import mmCIFUtil

class NmrStarToCif(object):

    def __init__(self, verbose=False, log=sys.stderr):
        self.__verbose = verbose
        self.__lfh = log

        # whether to add _pdbx_nmr_assigned_chem_shift_list category (for backward compatibility)
        self.__add_cs_list_cif = False
        # whether to add Original_pdb_* items in chemical shifts
        self.__add_original_pdb_in_chem_shift = True
        # whether to add Original_pdb_* items in distance restraints
        self.__add_original_pdb_in_dist_restraint = True
        # whether to add Origianl_pdb_* items in other restraints
        self.__add_original_pdb_in_others = False

        # empty value
        self.empty_value = (None, '', '.', '?')

    def convert(self, strPath=None, cifPath=None, originalFileName=None, fileType='nm-uni-nef'):
        """ Convert NMR-STAR to CIF
        """

        if strPath is None or cifPath is None:
            return False

        # whether to overwrite Auth_atom_ID by Atom_ID
        overwrite_auth_atom_id = 'nef' in fileType

        try:

            myIo = IoAdapterPy(False, sys.stderr)
            containerList = myIo.readFile(strPath)

            if containerList is not None and len(containerList) > 1:

                if self.__verbose:
                    self.__lfh.write('Input container list is  %r\n' % ([(c.getName(), c.getType()) for c in containerList]))

                for c in containerList:
                    c.setType('data')

                myIo.writeFile(cifPath, containerList=containerList[1:])

                # post modification for converted CIF file

                cifObj = mmCIFUtil(filePath=cifPath)

                categories = cifObj.GetCategories()

                # add _pdbx_nmr_assigned_chem_shift_list for each _Assigned_chem_shift_list for backward compatibility
                if self.__add_cs_list_cif:

                    cs_list_str = 'Assigned_chem_shift_list'
                    cs_list_cif = 'pdbx_nmr_assigned_chem_shift_list'

                    for k, v in categories.items():

                        if cs_list_str in v:
                            cifObj.AddCategory(k, cs_list_cif, ['entry_id', 'id', 'data_file_name'])
                            cifObj.InsertData(k, cs_list_cif, [[cifObj.GetSingleValue(k, cs_list_str, 'Entry_ID'), cifObj.GetSingleValue(k, cs_list_str, 'ID'), originalFileName]])

                # add _Atom_chem_shift.Original_PDB_* items

                lp_category = 'Atom_chem_shift'
                original_items = ['Original_PDB_strand_ID', 'Original_PDB_residue_no', 'Original_PDB_residue_name', 'Original_PDB_atom_name']
                original_auth_map = {'Original_PDB_strand_ID': 'Auth_asym_ID', 'Original_PDB_residue_no': 'Auth_seq_ID', 'Original_PDB_residue_name': 'Auth_comp_ID', 'Original_PDB_atom_name': 'Auth_atom_ID'}
                atom_id_tags = ['Atom_ID']
                auth_atom_id_tags = ['Auth_atom_ID']

                for k, v in categories.items():

                    if lp_category in v:
                        items = cifObj.GetAttributes(k, lp_category)

                        extended_items = [original_item for original_item in original_items if original_item not in items]

                        if len(extended_items) > 0:
                            dList, iList = cifObj.GetValueAndItemByBlock(k, lp_category)

                            auth_items = [original_auth_map[original_item] for original_item in extended_items]

                            extended_data_list = []

                            for src in dList:
                                dst = []
                                for auth_item in auth_items:
                                    dst.append(src[auth_item])
                                extended_data_list.append(dst)

                            if self.__add_original_pdb_in_chem_shift:
                                cifObj.ExtendCategory(k, lp_category, extended_items, extended_data_list)

                        if overwrite_auth_atom_id:
                            cifObj.CopyValueInRow(k, lp_category, atom_id_tags, auth_atom_id_tags)


                # add _Gen_dist_constraint.Original_PDB_* items

                lp_category = 'Gen_dist_constraint'
                _original_items = []
                _original_auth_map = {}
                _atom_id_tags = []
                _auth_atom_id_tags = []
                for i in range(1, 3):
                    for original_item in original_items:
                        _original_items.append(original_item + '_' + str(i))
                    for k, v in original_auth_map.items():
                        _original_auth_map[k + '_' + str(i)] = v + '_' + str(i)
                    for atom_id_tag in atom_id_tags:
                        _atom_id_tags.append(atom_id_tag + '_' + str(i))
                    for auth_atom_id_tag in auth_atom_id_tags:
                        _auth_atom_id_tags.append(auth_atom_id_tag + '_' + str(i))

                for k, v in categories.items():

                    if lp_category in v:
                        items = cifObj.GetAttributes(k, lp_category)

                        extended_items = [original_item for original_item in _original_items if original_item not in items]

                        if len(extended_items) > 0:
                            dList, iList = cifObj.GetValueAndItemByBlock(k, lp_category)

                            auth_items = [_original_auth_map[original_item] for original_item in extended_items]

                            extended_data_list = []

                            for src in dList:
                                dst = []
                                for auth_item in auth_items:
                                    dst.append(src[auth_item])
                                extended_data_list.append(dst)

                            if self.__add_original_pdb_in_dist_restraint:
                                cifObj.ExtendCategory(k, lp_category, extended_items, extended_data_list)

                        if overwrite_auth_atom_id:
                            cifObj.CopyValueInRow(k, lp_category, _atom_id_tags, _auth_atom_id_tags)

                if self.__add_original_pdb_in_others:

                    # add _Torsion_angle_constraint.Original_PDB_* items

                    lp_category = 'Torsion_angle_constraint'
                    _original_items = []
                    _original_auth_map = {}
                    _atom_id_tags = []
                    _auth_atom_id_tags = []
                    for i in range(1, 5):
                        for original_item in original_items:
                            _original_items.append(original_item + '_' + str(i))
                        for k, v in original_auth_map.items():
                            _original_auth_map[k + '_' + str(i)] = v + '_' + str(i)
                        for atom_id_tag in atom_id_tags:
                            _atom_id_tags.append(atom_id_tag + '_' + str(i))
                        for auth_atom_id_tag in auth_atom_id_tags:
                            _auth_atom_id_tags.append(auth_atom_id_tag + '_' + str(i))

                    for k, v in categories.items():

                        if lp_category in v:
                            items = cifObj.GetAttributes(k, lp_category)

                            extended_items = [original_item for original_item in _original_items if original_item not in items]

                            if len(extended_items) > 0:
                                dList, iList = cifObj.GetValueAndItemByBlock(k, lp_category)

                                auth_items = [_original_auth_map[original_item] for original_item in extended_items]

                                extended_data_list = []

                                for src in dList:
                                    dst = []
                                    for auth_item in auth_items:
                                        dst.append(src[auth_item])
                                    extended_data_list.append(dst)

                                cifObj.ExtendCategory(k, lp_category, extended_items, extended_data_list)

                            if overwrite_auth_atom_id:
                                cifObj.CopyValueInRow(k, lp_category, _atom_id_tags, _auth_atom_id_tags)

                    # add _RDC_constraint.Origianl_PDB_* items

                    lp_category = 'RDC_constraint'
                    _original_items = []
                    _original_auth_map = {}
                    _atom_id_tags = []
                    _auth_atom_id_tags = []
                    for i in range(1, 3):
                        for original_item in original_items:
                            _original_items.append(original_item + '_' + str(i))
                        for k, v in original_auth_map.items():
                            _original_auth_map[k + '_' + str(i)] = v + '_' + str(i)
                        for atom_id_tag in atom_id_tags:
                            _atom_id_tags.append(atom_id_tag + '_' + str(i))
                        for auth_atom_id_tag in auth_atom_id_tags:
                            _auth_atom_id_tags.append(auth_atom_id_tag + '_' + str(i))

                    for k, v in categories.items():

                        if lp_category in v:
                            items = cifObj.GetAttributes(k, lp_category)

                            extended_items = [original_item for original_item in _original_items if original_item not in items]

                            if len(extended_items) > 0:
                                dList, iList = cifObj.GetValueAndItemByBlock(k, lp_category)

                                auth_items = [_original_auth_map[original_item] for original_item in extended_items]

                                extended_data_list = []

                                for src in dList:
                                    dst = []
                                    for auth_item in auth_items:
                                        dst.append(src[auth_item])
                                    extended_data_list.append(dst)

                                cifObj.ExtendCategory(k, lp_category, extended_items, extended_data_list)

                            if overwrite_auth_atom_id:
                                cifObj.CopyValueInRow(k, lp_category, _atom_id_tags, _auth_atom_id_tags)

                    lp_category = 'Peak_row_format'

                    for k, v in categories.items():

                        if lp_category in v:
                            items = cifObj.GetAttributes(k, lp_category)
                            max_dim = 0
                            for i in range(1, 16):
                                if not 'Atom_ID_' + str(i) in items:
                                    break
                                max_dim = i

                            if max_dim > 1 and max_dim <= 16:
                                _original_items = []
                                _original_auth_map = {}
                                _atom_id_tags = []
                                _auth_atom_id_tags = []
                                for i in range(1, max_dim):
                                    for original_item in original_items:
                                        _original_items.append(original_item + '_' + str(i))
                                    for k, v in original_auth_map.items():
                                        _original_auth_map[k + '_' + str(i)] = v + '_' + str(i)
                                    for atom_id_tag in atom_id_tags:
                                        _atom_id_tags.append(atom_id_tag + '_' + str(i))
                                    for auth_atom_id_tag in auth_atom_id_tags:
                                        _auth_atom_id_tags.append(auth_atom_id_tag + '_' + str(i))

                                extended_items = [original_item for original_item in _original_items if original_item not in items]

                                has_auth_value = False

                                if len(extended_items) > 0:
                                    dList, iList = cifObj.GetValueAndItemByBlock(k, lp_category)

                                    auth_items = [_original_auth_map[original_item] for original_item in extended_items]

                                    extended_data_list = []

                                    for src in dList:
                                        dst = []
                                        for auth_item in auth_items:
                                            dst.append(src[auth_item])
                                            if not src[auth_item] in self.empty_value:
                                                has_auth_value = True
                                        extended_data_list.append(dst)

                                    if has_auth_value:
                                        cifObj.ExtendCategory(k, lp_category, extended_items, extended_data_list)

                                if overwrite_auth_atom_id and has_auth_value:
                                    cifObj.CopyValueInRow(k, lp_category, _atom_id_tags, _auth_atom_id_tags)

                cifObj.WriteCif(outputFilePath=cifPath)

                return True

        except StopIteration:
            pass
        """
        except Exception as e:
            self.__lfh.write('+ERROR- NmrStarToCif.convert() %s\n' % e)
        """
        return False
