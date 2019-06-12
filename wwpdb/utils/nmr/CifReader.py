##
# File: CifReader.py derived from wwpdb.apps.ccmodule.io.ChemCompIo.py
# Date: 31-May-2010  John Westbrook
#
# Update:
# 06-Aug-2010 - jdw - Generalized construction of methods to apply to any category
#                     Add accessors for lists of dictionaries.
# 12-May-2011 - rps - Added check for None when asking for category Object in __getDataList()
# 2012-10-24    RPS   Updated to reflect reorganization of modules in pdbx packages
# 11-Jun-2019   my  - Forked original code to wwpdb.util.nmr.CifReader
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
            for idxIt,itName in enumerate(itNameList):
                itDict[itName] = idxIt

            # get row list
            rowList = catObj.getRowList()
            for row in rowList:
                tD = {}
                for k, v in itDict.items():
                    tD[k[len_catName:]] = row[v]
                dList.append(tD)

        return dList
