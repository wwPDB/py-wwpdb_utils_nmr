##
# File: CifReader.py derived from wwpdb.apps.ccmodule.io.ChemCompIo.py
# Date: 31-May-2010  John Westbrook
#
# Update:
# 06-Aug-2010 - jdw - Generalized construction of methods to apply to any category
#                     Add accessors for lists of dictionaries.
# 12-May-2011 - rps - Added check for None when asking for category Object in __getDataList()
# 2012-10-24    RPS   Updated to reflect reorganization of modules in pdbx packages
# 23-Jul-2019   my  - Forked original code to wwpdb.util.nmr.CifReader
# 30-Jul-2019   my  - Add 'range-float' as filter item type
# 05-Aug-2019   my  - Add 'enum' as filter item type
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
        self.emptyValue = (None, '', '.', '?')
        self.trueValue = ('true', 't', 'yes', 'y', '1')

        # allowed item types
        self.itemTypes = ('str', 'bool', 'int', 'float', 'range-float', 'enum')

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
            if not blockId is None:
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

    def getPolymerSequence(self, catName, keyItems):
        """ Extracts sequence from a given loop in a CIF file
        """

        keyNames = [k['name'] for k in keyItems]

        len_key = len(keyItems)

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
                if itName in keyNames:
                    altDict[next(k['alt_name'] for k in keyItems if k['name'] == itName)] = idxIt

            if set(keyNames) & set(itDict.keys()) != set(keyNames):
                raise LookupError("Missing one of data items %s." % keyNames)

            # get row list
            rowList = catObj.getRowList()

            for row in rowList:
                for j in range(len_key):
                    if row[itDict[keyNames[j]]] in self.emptyValue:
                        raise ValueError("%s must not be empty." % itNameList[j])

            compDict = {}
            seqDict = {}

            try:
                chain_id_col = altDict['chain_id']
                seq_id_col = altDict['seq_id']
                comp_id_col = altDict['comp_id']

                chains = sorted(set([row[chain_id_col] for row in rowList]))
                sortedSeq = sorted(set(['{} {:04d} {}'.format(row[chain_id_col], int(row[seq_id_col]), row[comp_id_col]) for row in rowList]))

                keyDict = {'{} {:04d}'.format(row[chain_id_col], int(row[seq_id_col])):row[comp_id_col] for row in rowList}

                for row in rowList:
                    key = '{} {:04d}'.format(row[chain_id_col], int(row[seq_id_col]))
                    if keyDict[key] != row[comp_id_col]:
                        raise KeyError("Sequence must be unique. %s %s, %s %s, %s %s vs %s." %\
                                       (itNameList[chain_id_col], row[chain_id_col],
                                        itNameList[seq_id_col], row[seq_id_col],
                                        itNameList[comp_id_col], row[comp_id_col], keyDict[key]))

                if len(chains) > 1:
                    for c in chains:
                        compDict[c] = [s.split(' ')[-1] for s in sortedSeq if s.split(' ')[0] == c]
                        seqDict[c] = [int(s.split(' ')[1]) for s in sortedSeq if s.split(' ')[0] == c]
                else:
                    compDict[list(chains)[0]] = [s.split(' ')[-1] for s in sortedSeq]
                    seqDict[list(chains)[0]] = [int(s.split(' ')[1]) for s in sortedSeq]

                asm = [] # assembly of a loop

                for c in chains:
                    ent = {} # entity

                    ent['chain_id'] = c
                    ent['seq_id'] = seqDict[c]
                    ent['comp_id'] = compDict[c]

                    asm.append(ent)

            except ValueError:
                raise ValueError("%s must be int." % itNameList[seq_id_col])

        return asm

    def getDictListWithFilter(self, catName, dataItems, filterItems=None):
        """ Return a list of dictionaries of a given category with filter.
        """

        dataNames = [d['name'] for d in dataItems]

        for d in dataItems:
            if not d['type'] in self.itemTypes:
                raise TypeError("Type %s of data item %s must be one of %s." % (d['type'], d['name'], self.itemTypes))

        if not filterItems is None:
            filterNames = [f['name'] for f in filterItems]

            for f in filterItems:
                if not f['type'] in self.itemTypes:
                    raise TypeError("Type %s of filter item %s must be one of %s." % (f['type'], f['name'], self.itemTypes))

        dList = []

        # get category object
        catObj = self.__dBlock.getObj(catName)

        if not catObj is None:
            len_catName = len(catName) + 2

            # get column name index
            colDict = {}
            fcolDict = {}

            itNameList = [j[len_catName:] for j in catObj.getItemNameList()]

            for idxIt, itName in enumerate(itNameList):
                if itName in dataNames:
                    colDict[itName] = idxIt
                if (not filterItems is None) and itName in filterNames:
                    fcolDict[itName] = idxIt

            if set(dataNames) & set(itNameList) != set(dataNames):
                raise LookupError("Missing one of data items %s." % dataNames)

            if (not filterItems is None) and set(filterNames) & set(itNameList) != set(filterNames):
                raise LookupError("Missing one of filter items %s." % filterNames)

            # get row list
            rowList = catObj.getRowList()

            for row in rowList:
                filter = True
                if not filterItems is None:
                    for filterItem in filterItems:
                        val = row[fcolDict[filterItem['name']]]
                        if val in self.emptyValue:
                            if not filterItem['value'] in self.emptyValue:
                                filter = False
                                break
                        else:
                            filterItemType = filterItem['type']
                            if filterItemType == 'str' or filterItemType == 'enum':
                                pass
                            elif filterItemType == 'bool':
                                val = val.lower() in self.trueValue
                            elif filterItemType == 'int':
                                val = int(val)
                            else:
                                val = float(val)
                            if filterItemType == 'range-float':
                                _range = filterItem['range']
                                if ('min_exclusive' in _range and val <= _range['min_exclusive']) or ('min_inclusive' in _range and val < _range['min_inclusive']) or ('max_inclusive' in _range and val > _range['max_inclusive']) or ('max_exclusive' in _range and val >= _range['max_exclusive']):
                                    fileter = False
                                    break
                            elif filterItemType == 'enum':
                                if not val in filterItem['enum']:
                                    filter = False
                                    break
                            else:
                                if val != filterItem['value']:
                                    filter = False
                                    break

                if filter:
                    tD = {}
                    for dataItem in dataItems:
                        val = row[colDict[dataItem['name']]]
                        if val in self.emptyValue:
                            val = None
                        dataItemType = dataItem['type']
                        if dataItemType == 'str' or dataItemType == 'enum':
                            pass
                        elif dataItemType == 'bool':
                            val = val.lower() in self.trueValue
                        elif dataItemType == 'int' and not val is None:
                            val = int(val)
                        elif not val is None:
                            val = float(val)
                        if 'alt_name' in dataItem:
                            tD[dataItem['alt_name']] = val
                        else:
                            tD[dataItem['name']] = val
                    dList.append(tD)

        return dList
