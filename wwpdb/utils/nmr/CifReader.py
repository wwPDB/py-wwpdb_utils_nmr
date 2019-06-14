##
# File: CifReader.py derived from wwpdb.apps.ccmodule.io.ChemCompIo.py
# Date: 31-May-2010  John Westbrook
#
# Update:
# 06-Aug-2010 - jdw - Generalized construction of methods to apply to any category
#                     Add accessors for lists of dictionaries.
# 12-May-2011 - rps - Added check for None when asking for category Object in __getDataList()
# 2012-10-24    RPS   Updated to reflect reorganization of modules in pdbx packages
# 14-Jun-2019   my  - Forked original code to wwpdb.util.nmr.CifReader
##
""" A collection of classes for parsing CIF files.
"""

import sys,time,os,traceback
from mmcif.io.PdbxReader import PdbxReader

class CifReader(object):
    """ Accessor methods for parsing CIF files.
    """

    def __init__(self, verbose=True, log=sys.stdout):
        self.__verbose = verbose
        self.__lfh = log

        # file path
        self.__filePath = None

        # active data block
        self.__dBlock = None

        # preset values
        self.empty_value = (None, '', '.', '?')
        #self.true_value = ('true', 't', 'yes', 'y', '1')

        #self.item_types = ('str', 'bool', 'int', 'index-int', 'positive-int', 'static-index', 'float', 'positive-float', 'range-float', 'enum', 'enum-int')

    def setFilePath(self, filePath):
        """ Set file path and test readability.
            @return: True for success or False otherwise.
        """

        try:
            self.__filePath = filePath
            if (not os.access(self.__filePath, os.R_OK)):
                if (self.__verbose):
                    self.__lfh.write("+ERROR- CifReader.setFilePath() Missing file %s\n" % self.__filePath)
                return False
            return True
        except:
            if (self.__verbose):
                self.__lfh.write("+ERROR- CifReader.setFilePath() Missing file %s\n" % self.__filePath)
            return False

    def parse(self):
        """ Parse CIF file and set internal active data block.
            @return: True for success or False otherwise.
        """

        try:
            block = self.__getDataBlock()
            return self.__setDataBlock(block)
        except:
            traceback.print_exc(file=sys.stdout)
            return False

    def __getDataBlock(self, blockId=None):
        """ Worker method to read cif file and set the target datablock
            If no blockId is provided return the first data block.
            @return: target data block
        """

        with open(self.__filePath, 'r') as ifh:
            myBlockList = []
            pRd = PdbxReader(ifh)
            pRd.read(myBlockList)
            if (blockId is not None):
                for block in myBlockList:
                    if (block.getType() == 'data' and block.getName() == blockId):
                        return block
            else:
                for block in myBlockList:
                    if (block.getType() == 'data'):
                        return block

            return None

    def __setDataBlock(self, dataBlock=None):
        """ Assigns the input data block as the active internal data block.
            @return: True for success or False otherwise.
        """

        ok = False
        try:
            if dataBlock.getType() == 'data':
                self.__dBlock = dataBlock
                ok = True
            else:
                self.__dBlock = None
        except:
            pass

        return ok

    def hasCategory(self, catName):
        """ Return whether a give category exists.
        """

        return catName in self.__dBlock.getObjNameList()

    def getDictList(self, catName):
        """ Return a list of dictionaries of a given category.
        """

        dList = []
        # get category object
        catObj = self.__dBlock.getObj(catName)

        if not catObj is None:
            len_catName = len(catName) + 2

            # get column name index
            itDict = {}
            itNameList = catObj.getItemNameList()
            for idxIt, itName in enumerate(itNameList):
                itDict[itName[len_catName:]] = idxIt

            # get row list
            rowList = catObj.getRowList()
            for row in rowList:
                tD = {}
                for k, v in itDict.items():
                    tD[k] = row[v]
                dList.append(tD)

        return dList

    def getPolymerSequence(self, catName, key_items):
        """ Extracts sequence from a given loop in a CIF file
        """

        key_names = [k['name'] for k in key_items]

        key_len = len(key_items)
        """
        for k in key_items:
            if not k['type'] in self.item_types:
                raise TypeError("Type %s of key item %s (alt. %s) must be one of %s" % (k['type'], k['name'], k['alt_name'], self.item_types))
        """
        asm = [] # assembly of a loop

        # get category object
        catObj = self.__dBlock.getObj(catName)

        if not catObj is None:
            len_catName = len(catName) + 2

            # get column name index
            itDict = {}
            altDict = {}

            itNameList = [j[len_catName:] for j in catObj.getItemNameList()]

            for idxIt, itName in enumerate(itNameList):
                itDict[itName] = idxIt
                if itName in key_names:
                    altDict[next(k['alt_name'] for k in key_items if k['name'] == itName)] = idxIt

            if set(key_names) & set(itDict.keys()) != set(key_names):
                raise LookupError("Missing one of data items %s." % key_names)

            # get row list
            rowList = catObj.getRowList()

            for i in rowList:
                for j in range(key_len):
                    if i[itDict[key_names[j]]] in self.empty_value:
                        raise ValueError("%s must not be empty." % itNameList[j])

            seq_dict = {}
            sid_dict = {}

            try:
                chain_id_col = altDict['chain_id']
                seq_id_col = altDict['seq_id']
                comp_id_col = altDict['comp_id']

                chains = sorted(set([i[chain_id_col] for i in rowList]))
                sorted_seq = sorted(set(['{} {:04d} {}'.format(i[chain_id_col], int(i[seq_id_col]), i[comp_id_col]) for i in rowList]))

                chk_dict = {'{} {:04d}'.format(i[chain_id_col], int(i[seq_id_col])):i[comp_id_col] for i in rowList}

                for i in rowList:
                    chk_key = '{} {:04d}'.format(i[chain_id_col], int(i[seq_id_col]))
                    if chk_dict[chk_key] != i[comp_id_col]:
                        raise KeyError("Sequence must be unique. %s %s, %s %s, %s %s vs %s." %\
                                       (itNameList[chain_id_col], i[chain_id_col],
                                        itNameList[seq_id_col], i[seq_id_col],
                                        itNameList[comp_id_col], i[comp_id_col], chk_dict[chk_key]))

                if len(chains) > 1:
                    for c in chains:
                        seq_dict[c] = [i.split(' ')[-1] for i in sorted_seq if i.split(' ')[0] == c]
                        sid_dict[c] = [int(i.split(' ')[1]) for i in sorted_seq if i.split(' ')[0] == c]
                else:
                    seq_dict[list(chains)[0]] = [i.split(' ')[-1] for i in sorted_seq]
                    sid_dict[list(chains)[0]] = [int(i.split(' ')[1]) for i in sorted_seq]

                asm = [] # assembly of a loop

                for c in chains:
                    ent = {} # entity

                    ent['chain_id'] = c
                    ent['seq_id'] = sid_dict[c]
                    ent['comp_id'] = seq_dict[c]

                    asm.append(ent)

            except ValueError:
                raise ValueError("%s must be int." % itNameList[seq_id_col])

        return asm
