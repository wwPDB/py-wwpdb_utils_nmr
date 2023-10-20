##
# File: test_ChemCompUtil.py
# Date:  27-Apr-2022  M. Yokochi
#
# Updates:
#
import unittest
import os
import sys

try:
    from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
except ImportError:
    from nmr.ChemCompUtil import ChemCompUtil


if __package__ is None or __package__ == "":
    from os import path

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from commonsetup import TESTOUTPUT  # noqa: F401, pylint: disable=import-error,unused-import
else:
    from .commonsetup import TESTOUTPUT  # noqa: F401, pylint: disable=relative-beyond-top-level


class TestChemCompUtil(unittest.TestCase):
    def setUp(self):
        self.chem_comp_util = ChemCompUtil()

    def tearDown(self):
        pass

    def test_write_std_dict_as_pickle(self):
        self.chem_comp_util.write_std_dict_as_pickle()

    def test_protons_in_same_group(self):
        self.assertEqual(self.chem_comp_util.getProtonsInSameGroup('VAL', 'HG21'), ['HG21', 'HG22', 'HG23'])

    def test_effective_fw(self):
        self.assertEqual(round(self.chem_comp_util.getEffectiveFormulaWeight('ALA'), 3), 71.078)


if __name__ == "__main__":
    unittest.main()
