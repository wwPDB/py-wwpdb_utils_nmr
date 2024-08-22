##
# File: NEFImportTests.py
# Date:  06-Oct-2018  E. Peisach
#
# Updates:
##
"""Test cases for NEFTranslator - simply import everything to ensure imports work"""

import unittest
import sys

if __package__ is None or __package__ == "":
    from os import path

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from commonsetup import TESTOUTPUT  # noqa:  F401 pylint: disable=import-error,unused-import
else:
    from .commonsetup import TESTOUTPUT  # noqa: F401 pylint: disable=relative-beyond-top-level

from wwpdb.utils.nmr.NEFTranslator.NEFTranslator import NEFTranslator
from wwpdb.utils.nmr.NmrDpUtility import NmrDpUtility
from wwpdb.utils.nmr.NmrDpReport import NmrDpReport
# NmrStarToCif class has been deprecated
# from wwpdb.utils.nmr.NmrStarToCif import NmrStarToCif
from wwpdb.utils.nmr.rci.RCI import RCI
from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat


class ImportTests(unittest.TestCase):
    def testInstantiate(self):
        _c = NEFTranslator()  # noqa: F841
        _npu = NmrDpUtility()  # noqa: F841
        _ndp = NmrDpReport()  # noqa: F841
        _# nstc = NmrStarToCif()  # noqa: F841
        _rci = RCI()  # noqa: F841
        _bmrb = BMRBChemShiftStat()  # noqa: F841


if __name__ == "__main__":
    unittest.main()
