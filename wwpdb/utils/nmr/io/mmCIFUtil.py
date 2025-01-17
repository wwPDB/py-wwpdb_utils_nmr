##
# File: mmCIFUtil.py
# Date: 21-Aug-2012  Zukang Feng
#
# Update:
# 07-Apr-2020  M. Yokochi - re-write Zukang's version to being aware of multiple datablocks
# 30-May-2024  M. Yokochi - resolve duplication of datablock/saveframe name (DAOTHER-9437)
# 16-Jan-2025  M. Yokochi - abandon symbolic label representations in mmCIF for mutual format conversion
##
""" A collection of classes for manipulating CIF files containing multiple datablocks.
"""
__docformat__ = "restructuredtext en"
__author__ = "Zukang Feng, Masashi Yokochi"
__email__ = "zfeng@rcsb.rutgers.edu, yokochi@protein.osaka-u.ac.jp"
__license__ = "Creative Commons Attribution 3.0 Unported"
__version__ = "1.0.3"

import sys
import os
import copy
import re

from typing import Any, IO, List, Tuple, Optional

from mmcif.api.DataCategory import DataCategory
from mmcif.api.PdbxContainers import DataContainer
from mmcif.io.PdbxReader import PdbxReader
from mmcif.io.PdbxWriter import PdbxWriter

try:
    from wwpdb.utils.nmr.AlignUtil import emptyValue
except ImportError:
    from nmr.AlignUtil import emptyValue


label_symbol_pattern = re.compile(r'^\$[^\s\$\?\\\'\"\`;]+$')


def get_ext_block_name(name: str, ext: int = 1) -> str:
    """ Return unique block name avoiding duplication.
    """

    return name if ext == 1 else f'{name}_{ext}'


def abandon_symbolic_labels(containerList: list):
    """ Abandon symbolic label representations that serve as saveframe pointers in NMR-STAR.
    """

    for container in containerList:
        container.setType('data')

        for category in container.getObjNameList():
            obj = container.getObj(category)
            attrs = obj.getAttributeList()
            labelCols = [idx for idx, attr in enumerate(attrs) if attr.endswith('_label')]
            if len(labelCols) == 0:
                continue
            for idx, row in enumerate(obj.getRowList()):
                for col, val in enumerate(row):
                    if col in labelCols and label_symbol_pattern.match(val):
                        obj.setValue(val[1:], attrs[col], idx)


class mmCIFUtil:
    """ Accessor methods for manipulating CIF files containing multiple datablocks.
    """

    def __init__(self, verbose: bool = False, log: IO = sys.stderr, filePath: Optional[str] = None):
        self.__class_name__ = self.__class__.__name__

        self.__verbose = verbose
        self.__lfh = log

        self.__filePath = filePath
        self.__dataList = []
        self.__dataMap = {}
        self.__blockNameList = []

        if self.__filePath is None:
            return

        try:
            if not os.access(self.__filePath, os.R_OK):
                if self.__verbose:
                    self.__lfh.write(f"+{self.__class_name__} ++ Error  - Missing file {self.__filePath}\n")
                return

            with open(self.__filePath, 'r', encoding='utf-8') as ifh:
                pRd = PdbxReader(ifh)
                pRd.read(self.__dataList)

            if len(self.__dataList) > 0:
                is_star = all(container.getType() == 'data' for container in self.__dataList)
                idx = 0
                for container in self.__dataList:
                    if is_star or (not is_star and container.getType() != 'data'):
                        blockName = container.getName()
                        self.__blockNameList.append(blockName)

                        if blockName not in self.__dataMap:
                            self.__dataMap[blockName] = idx
                        else:
                            ext = 2
                            while True:
                                extBlockName = get_ext_block_name(blockName, ext)
                                if extBlockName not in self.__dataMap:
                                    self.__dataMap[extBlockName] = idx
                                    break
                                ext += 1
                    idx += 1

        except Exception as e:
            if self.__verbose and 'loop_ declaration outside of data_ block or save_ frame' not in str(e):
                self.__lfh.write(f"+{self.__class_name__} ++ Error  - Read {self.__filePath} failed {str(e)}\n")

    def GetBlockIDList(self) -> List[str]:
        """ Return list of blockID.
        """

        return self.__blockNameList

    def GetValueAndItemByBlock(self, blockName: str, catName: str, ext: int = 1) -> Tuple[List[dict], List[str]]:
        """ Get category values and item names.
        """

        if blockName not in self.__dataMap:
            return [], []

        catObj = self.__dataList[self.__dataMap[get_ext_block_name(blockName, ext)]].getObj(catName)

        if catObj is None:
            return [], []

        iList = catObj.getAttributeList()
        dList = []
        for row in catObj.getRowList():
            try:
                tD = {}
                for idxIt, itName in enumerate(iList):
                    if row[idxIt] not in emptyValue:
                        tD[itName] = row[idxIt]

                if len(tD) > 0:
                    dList.append(tD)

            except IndexError:
                pass

        return dList, iList

    def GetValue(self, blockName: str, catName: str, ext: int = 1) -> List[dict]:
        """ Get category values in a given datablock and category.
        """

        return self.GetValueAndItemByBlock(blockName, catName, ext)[0]

    def GetSingleValue(self, blockName: str, catName: str, itemName: str, ext: int) -> Any:
        """ Get the first value of a given datablock, category, and item.
        """

        dlist = self.GetValue(blockName, catName, ext)

        if len(dlist) > 0 and itemName in dlist[0]:
            return dlist[0][itemName]

        return ''

    def UpdateSingleRowValue(self, blockName: str, catName: str, itemName: str, rowIndex: int, value: Any, ext: int = 1):
        """ Update single row with a given value.
        """

        if blockName not in self.__dataMap:
            return

        catObj = self.__dataList[self.__dataMap[get_ext_block_name(blockName, ext)]].getObj(catName)

        if catObj is None:
            return

        catObj.setValue(value, itemName, rowIndex)

    def UpdateMultipleRowsValue(self, blockName: str, catName: str, itemName: str, value: Any, ext: int = 1):
        """ Update multiple rows with a given value.
        """

        if blockName not in self.__dataMap:
            return

        catObj = self.__dataList[self.__dataMap[get_ext_block_name(blockName, ext)]].getObj(catName)

        if catObj is None:
            return

        for rowIndex in range(0, catObj.getRowCount()):
            catObj.setValue(value, itemName, rowIndex)

    def AddBlock(self, blockName: str, ext: int = 1):
        """ Add a datablock.
        """

        self.__dataMap[get_ext_block_name(blockName, ext)] = len(self.__dataList)
        self.__dataList.append(DataContainer(blockName))

    def AddCategory(self, blockName: str, catName: str, items: List[str], ext: int = 1):
        """ Add a category in a given datablock.
        """

        if blockName not in self.__dataMap:
            return

        category = DataCategory(catName)

        for item in items:
            category.appendAttribute(item)

        self.__dataList[self.__dataMap[get_ext_block_name(blockName, ext)]].append(category)

    def RemoveCategory(self, blockName: str, catName: str, ext: int = 1):
        """ Remove a category in a given datablock.
        """

        if blockName not in self.__dataMap:
            return

        idx = self.__dataMap[get_ext_block_name(blockName, ext)]

        catObj = self.__dataList[idx].getObj(catName)

        if catObj is None:
            return

        self.__dataList[idx].remove(catName)

    def MoveCategoryToTop(self, blockName: str, catName: str, ext: int = 1):
        """ Move category to top in a given datablock.
        """

        if blockName not in self.__dataMap:
            return

        idx = self.__dataMap[get_ext_block_name(blockName, ext)]

        catObj = self.__dataList[idx].getObj(catName)

        if catObj is None:
            return

        _catNameList = copy.copy(self.__dataList[idx].getObjNameList())
        _catNameList.remove(catName)

        _catObjList = [copy.copy(catObj)]
        _catObjList.extend([copy.copy(self.__dataList[idx].getObj(_catName)) for _catName in _catNameList])

        for _catName in _catNameList:
            self.__dataList[idx].remove(_catName)

        for _catObj in _catObjList:
            self.__dataList[idx].append(_catObj)

    def InsertData(self, blockName: str, catName: str, dataList: list, ext: int = 1):
        """ Insert data in a given datablock and category.
        """

        if blockName not in self.__dataMap:
            return

        catObj = self.__dataList[self.__dataMap[get_ext_block_name(blockName, ext)]].getObj(catName)

        if catObj is None:
            return

        for data in dataList:
            catObj.append(data)

    def ExtendCategory(self, blockName: str, catName: str, items: List[str], dataList: list, col: int = -1, ext: int = 1):
        """ Extend existing category in a given datablock.
        """

        if blockName not in self.__dataMap:
            return

        catObj = self.__dataList[self.__dataMap[get_ext_block_name(blockName, ext)]].getObj(catName)

        if catObj is None:
            return

        append_items = col < 0 or col >= catObj.getAttributeCount()

        len_data = len(dataList)
        empty_row = ['.'] * len(items)

        if append_items:

            for item in items:
                catObj.appendAttribute(item)

            for idx, row in enumerate(catObj.getRowList()):
                if idx < len_data:
                    row.extend(dataList[idx])
                else:
                    row.extend(empty_row)

        else:

            attrNameList = catObj.getAttributeList()
            _attrNameList = attrNameList[0:col] + items + attrNameList[col:]

            _rowList = []
            for idx, row in enumerate(catObj.getRowList()):
                _row = row[0:col]

                if idx < len_data:
                    _row.extend(dataList[idx])
                else:
                    _row.extend(empty_row)

                _row.extend(row[col:])

                _rowList.append(_row)

            catObj.setAttributeNameList(_attrNameList)
            catObj.setRowList(_rowList)

    def CopyValueInRow(self, blockName: str, catName: str, srcItems: List[str], dstItems: List[str], ext: int = 1):
        """ Copy values of source items to destination items.
        """

        if None in (srcItems, dstItems) or len(srcItems) != len(dstItems):
            return

        if blockName not in self.__dataMap:
            return

        catObj = self.__dataList[self.__dataMap[get_ext_block_name(blockName, ext)]].getObj(catName)

        if catObj is None:
            return

        attrs = catObj.getAttributeList()

        for item in srcItems:
            if item not in attrs:
                return

        for item in dstItems:
            if item not in attrs:
                return

        src_cols = [attrs.index(item) for item in srcItems]
        dst_cols = [attrs.index(item) for item in dstItems]

        for row in catObj.getRowList():
            for j, src_col in enumerate(src_cols):
                row[dst_cols[j]] = row[src_col]

    def WriteCif(self, outputFilePath: Optional[str] = None):
        """ Write CIF file.
        """

        if not outputFilePath:
            return

        with open(outputFilePath, 'w', encoding='utf-8') as ofh:
            pdbxW = PdbxWriter(ofh)
            pdbxW.write(self.__dataList)

    def GetCategories(self) -> dict:
        """ Get all categories in all datablocks.
        """

        return {container.getName(): container.getObjNameList() for container in self.__dataList}

    def GetAttributes(self, blockName: str, catName: str, ext: int = 1) -> List[str]:
        """ Get item name in given datablock and category.
        """

        if blockName not in self.__dataMap:
            return []

        catObj = self.__dataList[self.__dataMap[get_ext_block_name(blockName, ext)]].getObj(catName)

        if catObj is None:
            return []

        return catObj.getAttributeList()

    def GetRowLength(self, blockName: str, catName: str, ext: int = 1) -> int:
        """ Return length of rows of a given datablock and category.
        """

        if blockName not in self.__dataMap:
            return 0

        catObj = self.__dataList[self.__dataMap[get_ext_block_name(blockName, ext)]].getObj(catName)

        if catObj is None:
            return 0

        return len(catObj.getRowList())

    def GetRowList(self, blockName: str, catName: str, ext: int = 1) -> List[list]:
        """ Get a list of list of a given datablock and category.
        """

        if blockName not in self.__dataMap:
            return []

        catObj = self.__dataList[self.__dataMap[get_ext_block_name(blockName, ext)]].getObj(catName)

        if catObj is None:
            return []

        return catObj.getRowList()

    def GetDictList(self, blockName: str, catName: str, ext: int = 1) -> dict:
        """ Get a list of dictionary of a given datablock and category.
        """

        dList, iList = self.GetValueAndItemByBlock(blockName, catName, ext)
        data = [[x.get(y) for y in iList] for x in dList]

        return {catName: {"Items": iList, "Values": data}}

    def GetDataBlock(self, blockName: str, ext: int = 1) -> dict:
        """ Get a dictionary of a given datablock.
        """

        categories = self.GetCategories()

        if blockName not in categories:
            return {}

        data = {}
        for catName in categories[blockName]:
            data.update(self.GetDictList(blockName, catName, ext))

        return data
