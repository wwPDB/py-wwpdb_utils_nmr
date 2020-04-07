##
# File: test_NmrStarToCif.py
# Date:  02-Apr-2020  M. Yokochi
#
# Updates:
#
import unittest
import os
import sys

from wwpdb.utils.nmr.NmrStarToCif import NmrStarToCif
from testfixtures import LogCapture

class TestNmrStarToCif(unittest.TestCase):

    def setUp(self):
        here = os.path.abspath(os.path.dirname(__file__))
        self.data_dir_path = os.path.join(here, 'mock-data/')
        self.nmrstar_to_cif = NmrStarToCif()
        pass

    def tearDown(self):
        pass

    def test_unified(self):
        self.nmrstar_to_cif.convert(strPath=self.data_dir_path + 'D_800269_nmr-data-str_P1.str.V1', cifPath=self.data_dir_path + 'D_800269_nmr-data-str_P1.cif.V1', originalFileName='2png.nef')

    def test_legacy(self):
        self.nmrstar_to_cif.clean(cifPath=self.data_dir_path + 'D_800262_cs-upload-convert_P1.cif.V8', originalCsFileNameList=['D_800262_cs.str'])

if __name__ == '__main__':
    unittest.main()
