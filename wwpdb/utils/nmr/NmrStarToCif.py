#
# File: NmrStarToCif.py
# Date: 02-Apr-2020
#
# Updates:
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

        self.__add_cs_list_cif = False
        self.__ow_auth_atom_id = True

    def convert(self, strPath=None, cifPath=None, originalFileName=None):
        """ Convert NMR-STAR to CIF
        """

        if strPath is None or cifPath is None:
            return False

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

                cs_str = 'Atom_chem_shift'
                original_items = ['Original_PDB_strand_ID', 'Original_PDB_residue_no', 'Original_PDB_residue_name', 'Original_PDB_atom_name']
                original_auth_map = {'Original_PDB_strand_ID': 'Auth_asym_ID', 'Original_PDB_residue_no': 'Auth_seq_ID', 'Original_PDB_residue_name': 'Auth_comp_ID', 'Original_PDB_atom_name': 'Auth_atom_ID'}

                for k, v in categories.items():

                    if cs_str in v:
                        items = cifObj.GetAttributes(k, cs_str)

                        extended_items = [original_item for original_item in original_items if original_item not in items]

                        if len(extended_items) == 0:
                            continue

                        dList, iList = cifObj.GetValueAndItemByBlock(k, cs_str)

                        auth_items = [original_auth_map[original_item] for original_item in extended_items]

                        extended_data_list = []

                        for src in dList:
                            dst = []
                            for auth_item in auth_items:
                                dst.append(src[auth_item])
                            extended_data_list.append(dst)

                        cifObj.ExtendCategory(k, cs_str, extended_items, extended_data_list)

                        if self.__ow_auth_atom_id:
                            cifObj.CopyValueInRow(k, cs_str, ['Atom_ID'], ['Auth_atom_ID'])

                cifObj.WriteCif(outputFilePath=cifPath)

                return True

        except Exception as e:
            self.__lfh.write('+ERROR- NmrStarToCif.convert() %s\n' % e)

        return False
