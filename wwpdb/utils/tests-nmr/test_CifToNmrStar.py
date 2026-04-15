##
# File: test_CifToNmrStar.py
# Date:  15-Apr-2022  M. Yokochi
#
# Updates:
# 10-Nov-2022  M. Yokochi re-write unit test for cs validation code
#
import os
import sys
import unittest

try:
    from wwpdb.utils.nmr.CifToNmrStar import CifToNmrStar
except ImportError:
    from nmr.CifToNmrStar import CifToNmrStar


class TestCifToNmrStar(unittest.TestCase):
    def setUp(self):
        self.cif_to_nmr_star = CifToNmrStar(log=sys.stderr)

    def tearDown(self):
        pass

    def test_convert_2mmz(self):
        if os.path.exists('mock-data-remediation'):
            self.assertTrue(self.cif_to_nmr_star.convert('mock-data-remediation/2mmz/2mmz_cs.str',
                                                         'mock-data-remediation/2mmz/2mmz_cs.str.cif2str'))

    def test_convert_6i4n(self):
        if os.path.exists('mock-data-remediation'):
            self.assertTrue(self.cif_to_nmr_star.convert('mock-data-remediation/6i4n/6i4n_cs.str',
                                                         'mock-data-remediation/6i4n/6i4n_cs.str.cif2str'))

    def test_convert_5xbo(self):
        if os.path.exists('mock-data-remediation'):
            self.assertTrue(self.cif_to_nmr_star.convert('mock-data-remediation/5xbo/5xbo_cs.str',
                                                         'mock-data-remediation/5xbo/5xbo_cs.str.cif2str'))

    def test_convert_1d2b(self):
        self.assertTrue(self.cif_to_nmr_star.convert('mock-data/1d2b_cs.str',
                                                     'mock-data/1d2b_cs.str.cif2str'))

    def test_convert_4apd(self):
        if os.path.exists('mock-data-remediation'):
            self.assertTrue(self.cif_to_nmr_star.convert('mock-data-remediation/4apd/4apd_cs.str',
                                                         'mock-data-remediation/4apd/4apd_cs.str.cif2str'))

    def test_convert_7kaa(self):
        if os.path.exists('mock-data-remediation'):
            self.assertTrue(self.cif_to_nmr_star.convert('mock-data-remediation/7kaa/7kaa_cs.str',
                                                         'mock-data-remediation/7kaa/7kaa_cs.str.cif2str'))

    def test_convert_daother_9437(self):
        if os.path.exists('mock-data-daother-9437'):
            self.assertTrue(self.cif_to_nmr_star.convert('mock-data-daother-9437/test2.str',
                                                         'mock-data-daother-9437/test2.cif2str'))

    def test_daother_10580(self):
        if os.path.exists('mock-data-daother-10580'):
            self.assertTrue(self.cif_to_nmr_star.convert('mock-data-daother-10580/B36_BMRB_2_2p5ppmCplus.txt',
                                                         'mock-data-daother-10580/B36_BMRB_2_2p5ppmCplus.txt.cif2str'))


if __name__ == "__main__":
    unittest.main()
