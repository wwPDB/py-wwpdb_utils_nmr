##
# File: ChemCompIo.py
# Date: 31-May-2010  John Westbrook
#
# Update:
# 06-Aug-2010 - jdw - Generalized construction of methods to apply to any category
#                     Add accessors for lists of dictionaries.
# 12-May-2011 - rps - Added check for None when asking for category Object in __getDataList()
# 2012-10-24    RPS   Updated to reflect reorganization of modules in pdbx packages
##
"""
A collection of classes supporting chemical component dictionary data files.

"""
__docformat__ = "restructuredtext en"
__author__ = "John Westbrook"
__email__ = "jwest@rcsb.rutgers.edu"
__license__ = "Creative Commons Attribution 3.0 Unported"
__version__ = "V0.01"


import sys
import os
import traceback

from mmcif.io.PdbxReader import PdbxReader


class ChemCompReader:
    """ Accessor methods chemical component definition data files.
    """
    def __init__(self, verbose=True, log=sys.stdout):
        self.__verbose = verbose
        self.__debug = False
        self.__lfh = log
        self.__dBlock = None
        self.__topCachePath = None
        self.__ccU = None
        self.__filePath = None
        #
        self.__cDict = {
            'chem_comp': [
                ('_chem_comp.id', '%s', 'str', ''),
                ('_chem_comp.name', '%s', 'str', ''),
                ('_chem_comp.type', '%s', 'str', ''),
                ('_chem_comp.pdbx_type', '%s', 'str', ''),
                ('_chem_comp.formula', '%s', 'str', ''),
                ('_chem_comp.mon_nstd_parent_comp_id', '%s', 'str', ''),
                ('_chem_comp.pdbx_synonyms', '%s', 'str', ''),
                ('_chem_comp.pdbx_formal_charge', '%s', 'str', ''),
                ('_chem_comp.pdbx_initial_date', '%s', 'str', ''),
                ('_chem_comp.pdbx_modified_date', '%s', 'str', ''),
                ('_chem_comp.pdbx_ambiguous_flag', '%s', 'str', ''),
                ('_chem_comp.pdbx_release_status', '%s', 'str', ''),
                ('_chem_comp.pdbx_replaced_by', '%s', 'str', ''),
                ('_chem_comp.pdbx_replaces', '%s', 'str', ''),
                ('_chem_comp.formula_weight', '%s', 'str', ''),
                ('_chem_comp.one_letter_code', '%s', 'str', ''),
                ('_chem_comp.three_letter_code', '%s', 'str', ''),
                ('_chem_comp.pdbx_model_coordinates_details', '%s', 'str', ''),
                ('_chem_comp.pdbx_model_coordinates_missing_flag', '%s', 'str', ''),
                ('_chem_comp.pdbx_ideal_coordinates_details', '%s', 'str', ''),
                ('_chem_comp.pdbx_ideal_coordinates_missing_flag', '%s', 'str', ''),
                ('_chem_comp.pdbx_model_coordinates_db_code', '%s', 'str', ''),
                ('_chem_comp.pdbx_subcomponent_list', '%s', 'str', ''),
                ('_chem_comp.pdbx_processing_site', '%s', 'str', '')
            ],
            'chem_comp_atom': [
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
                ('_chem_comp_atom.pdbx_ordinal', '%s', 'str', ''),
                ('_chem_comp_atom.pdbx_backbone_atom_flag', '%s', 'str', ''),
                ('_chem_comp_atom.pdbx_n_terminal_atom_flag', '%s', 'str', ''),
                ('_chem_comp_atom.pdbx_c_terminal_atom_flag', '%s', 'str', '')
            ],
            'chem_comp_bond': [
                ('_chem_comp_bond.comp_id', '%s', 'str', ''),
                ('_chem_comp_bond.atom_id_1', '%s', 'str', ''),
                ('_chem_comp_bond.atom_id_2', '%s', 'str', ''),
                ('_chem_comp_bond.value_order', '%s', 'str', ''),
                ('_chem_comp_bond.pdbx_aromatic_flag', '%s', 'str', ''),
                ('_chem_comp_bond.pdbx_stereo_config', '%s', 'str', ''),
                ('_chem_comp_bond.pdbx_ordinal', '%s', 'str', '')
            ],
            'chem_comp_descriptor': [
                ('_pdbx_chem_comp_descriptor.comp_id', '%s', 'str', ''),
                ('_pdbx_chem_comp_descriptor.type', '%s', 'str', ''),
                ('_pdbx_chem_comp_descriptor.program', '%s', 'str', ''),
                ('_pdbx_chem_comp_descriptor.program_version', '%s', 'str', ''),
                ('_pdbx_chem_comp_descriptor.descriptor', '%s', 'str', '')
            ],
            'chem_comp_identifier': [
                ('_pdbx_chem_comp_identifier.comp_id', '%s', 'str', ''),
                ('_pdbx_chem_comp_identifier.type', '%s', 'str', ''),
                ('_pdbx_chem_comp_identifier.program', '%s', 'str', ''),
                ('_pdbx_chem_comp_identifier.program_version', '%s', 'str', ''),
                ('_pdbx_chem_comp_identifier.identifier', '%s', 'str', '')
            ]
        }

    def setCachePath(self, topCachePath='/data/components/ligand-dict-v4'):
        """ Set the top file tree of chemical component dictionary.
        """
        self.__topCachePath = topCachePath

    def setCompId(self, compId):
        """ Set chemical component definition data file path of the input chemical component.
        """
        self.__ccU = compId.upper()
        hashd = self.__getCcdHash(self.__ccU)
        self.__filePath = os.path.join(self.__topCachePath, hashd, self.__ccU, self.__ccU + '.cif')
        if not os.access(self.__filePath, os.R_OK):
            if self.__verbose:
                self.__lfh.write(f"+ERROR- PdbxChemCompReader.getCompId() Missing file {self.__filePath}\n")
            return False
        return True

    def setFilePath(self, filePath, compId=None):
        """ Set data file path directory with chemical component ID.
        """
        try:
            if compId is not None:
                self.__ccU = str(compId).upper()
            self.__filePath = filePath
            if not os.access(self.__filePath, os.R_OK):
                if self.__verbose:
                    self.__lfh.write(f"+ERROR- PdbxChemCompReader.setFilePath() Missing file {self.__filePath}\n")
                return False
            return True
        except Exception:
            if self.__verbose:
                self.__lfh.write(f"+ERROR- PdbxChemCompReader.setFilePath() Missing file {self.__filePath}\n")
            return False

    def getAtomList(self):
        """ Get a list of list of data from the chem_comp_atom category.
        """
        self.__getComp()
        return self.__getDataList(catName='chem_comp_atom')

    def getBonds(self):
        """ Get a list of list of data from the chem_comp_bond category.
        """
        self.__getComp()
        return self.__getDataList(catName='chem_comp_bond')

    def getChemCompDict(self):
        """ Get a list of dictionaries of a chem_comp category.
        """
        try:
            self.__getComp()
            dL = self.__getDictList(catName='chem_comp')
            return dL[0]
        except Exception:
            return {}

    def __getComp(self):
        """ Get the definition data for the input chemical component.
            Data is read from chemical component definition file stored in the organization
            of CVS repository for chemical components.

            Returns True for success or False otherwise.
        """
        try:
            block = self.__getDataBlock(self.__filePath, self.__ccU)
            return self.__setDataBlock(block)

        except Exception:
            traceback.print_exc(file=sys.stdout)
            return False

    def __getDataBlock(self, filePath, blockId=None):
        """ Worker method to read chemical component definition file and set the target datablock
            corresponding to the target chemical component.
            If no blockId is provided return the first data block.
        """
        try:
            with open(filePath, 'r', encoding='utf-8') as ifh:
                myBlockList = []
                pRd = PdbxReader(ifh)
                pRd.read(myBlockList)

            if blockId is not None:
                for block in myBlockList:
                    if (block.getType() == 'data' and block.getName() == blockId):
                        if self.__debug:
                            block.printIt(self.__lfh)
                        return block
            else:
                for block in myBlockList:
                    if block.getType() == 'data':
                        if self.__debug:
                            block.printIt(self.__lfh)
                        return block

            return None
        except Exception:
            traceback.print_exc(file=self.__lfh)
            return None

    def __setDataBlock(self, dataBlock=None):
        """ Assigns the input data block as the active internal data block containing the
            target chemical component definition.
        """
        ok = False
        try:
            if dataBlock.getType() == 'data':
                self.__dBlock = dataBlock
                ok = True
            else:
                self.__dBlock = None
        except Exception:
            pass

        return ok

    def __getDictList(self, catName='chem_comp'):
        """ Return a list of dictionaries of the input category
        """
        # Get category object - from current data block
        itTupList = self.__cDict[catName]
        catObj = self.__dBlock.getObj(catName)
        #
        # Get column name index.
        #
        itDict = {}
        itNameList = catObj.getItemNameList()
        for idxIt, itName in enumerate(itNameList):
            itDict[itName] = idxIt
        #
        # Find the mapping to the local category definition
        #
        colDict = {}
        #
        for _ii, itTup in enumerate(itTupList):
            if itTup[0] in itDict:
                colDict[itTup[0]] = itDict[itTup[0]]
            else:
                colDict[itTup[0]] = -1
        #
        rowList = catObj.getRowList()
        dList = []
        for row in rowList:
            tD = {}
            for k, v in colDict.items():
                if v < 0:
                    tD[k] = ''
                else:
                    tD[k] = row[v]
            dList.append(tD)

        return dList

    def __getDataList(self, catName='chem_comp_bond'):
        """ Return a list a list of data from the input category including
            data types and default value replacement.
        """
        itTupList = self.__cDict[catName]
        dataList = []
        catObj = self.__dBlock.getObj(catName)
        if catObj is not None:
            itDict = {}
            itNameList = catObj.getItemNameList()
            for idxIt, itName in enumerate(itNameList):
                itDict[itName] = idxIt
            #
            colTupList = []
            # (column index of data or -1, type name, [default value])
            for _ii, itTup in enumerate(itTupList):
                if itTup[0] in itDict:
                    colTupList.append((itDict[itTup[0]], itTup[2], itTup[3]))
                else:
                    colTupList.append((-1, itTup[2], itTup[3]))
            #
            rowList = catObj.getRowList()

            for row in rowList:
                uR = []
                for cTup in colTupList:

                    if cTup[0] < 0:
                        uR.append(self.__applyType(cTup[1], cTup[2], cTup[2]))
                    else:
                        uR.append(self.__applyType(cTup[1], cTup[2], row[cTup[0]]))

                dataList.append(uR)

        return dataList

    def __applyType(self, ctype, default, val):  # pylint: disable=no-self-use
        """ Apply type conversion to the input value and assign default values to
            missing values.
        """
        tval = val
        if val is None:
            tval = default
        if isinstance(tval, str) and (len(tval) < 1 or tval in ('.', '?')):
            tval = default

        if ctype == "int":
            return int(str(tval))
        if ctype == "float":
            return float(str(tval))
        if ctype == "str":
            return str(tval)

        return tval

    def __getCcdHash(self, idCode):  # pylint: disable=no-self-use
        """Returns the hash code for a CCD id.  Currently first letter"""
        if not idCode:
            return None

        if len(idCode) > 3:
            hash_key = idCode.upper()[-2:]
        else:
            hash_key = idCode.upper()[0]

        return hash_key
