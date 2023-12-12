##
# File: test_ChemCompUtil.py
# Date:  27-Apr-2022  M. Yokochi
#
# Updates:
#
import unittest
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

    def test_greek_letter_system(self):
        self.assertEqual(self.chem_comp_util.getAtomsBasedOnGreekLetterSystem('GHP', 'HA'), {'HA'})
        self.assertEqual(self.chem_comp_util.getAtomsBasedOnGreekLetterSystem('GHP', 'CA'), {'CA'})
        self.assertEqual(self.chem_comp_util.getAtomsBasedOnGreekLetterSystem('GHP', 'HB'), set())
        self.assertEqual(self.chem_comp_util.getAtomsBasedOnGreekLetterSystem('GHP', 'CB'), {'C1'})
        self.assertEqual(self.chem_comp_util.getAtomsBasedOnGreekLetterSystem('GHP', 'HG'), {'H6', 'HC2'})
        self.assertEqual(self.chem_comp_util.getAtomsBasedOnGreekLetterSystem('GHP', 'CG'), {'C6', 'C2'})
        self.assertEqual(self.chem_comp_util.getAtomsBasedOnGreekLetterSystem('GHP', 'HD'), {'H3', 'H5'})
        self.assertEqual(self.chem_comp_util.getAtomsBasedOnGreekLetterSystem('GHP', 'CD'), {'C3', 'C5'})
        self.assertEqual(self.chem_comp_util.getAtomsBasedOnGreekLetterSystem('GHP', 'HE'), set())
        self.assertEqual(self.chem_comp_util.getAtomsBasedOnGreekLetterSystem('GHP', 'CE'), {'C4'})
        self.assertEqual(self.chem_comp_util.getAtomsBasedOnGreekLetterSystem('GHP', 'HZ'), {'HO4'})
        self.assertEqual(self.chem_comp_util.getAtomsBasedOnGreekLetterSystem('GHP', 'OZ'), {'O4'})


if __name__ == "__main__":
    unittest.main()
