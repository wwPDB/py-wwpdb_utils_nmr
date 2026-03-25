##
# File: NEFImportTests.py
# Date:  06-Oct-2018  E. Peisach
#
# Updates:
##
"""Test cases for NefTranslator - simply import everything to ensure imports work"""
import sys
import unittest

from wwpdb.utils.nmr.BmrbChemShiftStat import BmrbChemShiftStat
from wwpdb.utils.nmr.NmrDpUtility import NmrDpUtility
from wwpdb.utils.nmr.NmrDpReport import NmrDpReport
from wwpdb.utils.nmr.nef.NefTranslator import NefTranslator
from wwpdb.utils.nmr.rci.RCI import RCI

if __package__ is None or __package__ == "":
    from os import path

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from commonsetup import TESTOUTPUT  # noqa:  F401 pylint: disable=import-error,unused-import
else:
    from .commonsetup import TESTOUTPUT  # noqa: F401 pylint: disable=relative-beyond-top-level


class ImportTests(unittest.TestCase):
    def testInstantiate(self):  # pylint: disable=no-self-use
        _c = NefTranslator()  # noqa: F841
        _npu = NmrDpUtility()  # noqa: F841
        _ndp = NmrDpReport()  # noqa: F841
        # _nstc = NmrStarToCif()  # noqa: F841
        _rci = RCI()  # noqa: F841
        _bmrb = BmrbChemShiftStat()  # noqa: F841


if __name__ == "__main__":
    unittest.main()
