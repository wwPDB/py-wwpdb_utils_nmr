##
# File: test_CifToNmrStar.py
# Date:  15-Apr-2022  M. Yokochi
#
# Updates:
# 10-Nov-2022  M. Yokochi re-write unit test for cs validation code
#
import unittest
import os
import sys
import pynmrstar
from packaging import version

try:
    from wwpdb.utils.nmr.CifToNmrStar import CifToNmrStar
except ImportError:
    from nmr.CifToNmrStar import CifToNmrStar


__pynmrstar_v3_3_4__ = version.parse(pynmrstar.__version__) >= version.parse("3.3.4")


if __package__ is None or __package__ == "":
    from os import path

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from commonsetup import TESTOUTPUT  # noqa: F401, pylint: disable=import-error,unused-import
else:
    from .commonsetup import TESTOUTPUT  # noqa: F401, pylint: disable=relative-beyond-top-level


class TestCifToNmrStar(unittest.TestCase):
    def setUp(self):
        self.cif_to_nmr_star = CifToNmrStar(log=sys.stderr)

    def tearDown(self):
        pass

    def test_write_schema_as_pickles(self):
        if not __pynmrstar_v3_3_4__:
            if os.access(self.cif_to_nmr_star.schema_dir, os.W_OK):
                self.cif_to_nmr_star.write_schema_as_pickles()

    def test_convert_2mmz(self):
        if os.path.exists('mock-data-remediation'):
            self.assertTrue(self.cif_to_nmr_star.convert('mock-data-remediation/2mmz/2mmz_cs.str', 'mock-data-remediation/2mmz/2mmz_cs.str.cif2str'))

    def test_convert_6i4n(self):
        if os.path.exists('mock-data-remediation'):
            self.assertTrue(self.cif_to_nmr_star.convert('mock-data-remediation/6i4n/6i4n_cs.str', 'mock-data-remediation/6i4n/6i4n_cs.str.cif2str'))

    def test_convert_5xbo(self):
        if os.path.exists('mock-data-remediation'):
            self.assertTrue(self.cif_to_nmr_star.convert('mock-data-remediation/5xbo/5xbo_cs.str', 'mock-data-remediation/5xbo/5xbo_cs.str.cif2str'))

    def test_convert_1d2b(self):
        self.assertTrue(self.cif_to_nmr_star.convert('mock-data/1d2b_cs.str', 'mock-data/1d2b_cs.str.cif2str'))

    def test_convert_4apd(self):
        if os.path.exists('mock-data-remediation'):
            self.assertTrue(self.cif_to_nmr_star.convert('mock-data-remediation/4apd/4apd_cs.str', 'mock-data-remediation/4apd/4apd_cs.str.cif2str'))

    def test_convert_7kaa(self):
        if os.path.exists('mock-data-remediation'):
            self.assertTrue(self.cif_to_nmr_star.convert('mock-data-remediation/7kaa/7kaa_cs.str', 'mock-data-remediation/7kaa/7kaa_cs.str.cif2str'))

    def test_convert_daother_9437(self):
        if os.path.exists('mock-data-daother-9437'):
            self.assertTrue(self.cif_to_nmr_star.convert('mock-data-daother-9437/test2.str', 'mock-data-daother-9437/test2.cif2str'))


if __name__ == "__main__":
    unittest.main()
