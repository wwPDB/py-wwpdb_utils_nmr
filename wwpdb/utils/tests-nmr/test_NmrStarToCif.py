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
from shutil import copyfile

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
        copyfile(self.data_dir_path + 'D_800262_cs-upload-convert_P1.cif.V1', self.data_dir_path + 'D_800262_cs-upload-convert_P1.cif.V8')
        self.nmrstar_to_cif.clean(cifPath=self.data_dir_path + 'D_800262_cs-upload-convert_P1.cif.V8', originalCsFileNameList=['D_800262_cs.str'])

    def test_daother_5829(self):
        copyfile(self.data_dir_path + 'D_800350_cs_P1.cif.V2', self.data_dir_path + 'D_800350_cs_P1.cif.V1')
        self.nmrstar_to_cif.clean(cifPath=self.data_dir_path + 'D_800350_cs_P1.cif.V1', originalCsFileNameList=['Ost4V23D.star'])

    def test_D_1292117503(self):
        self.nmrstar_to_cif.convert(strPath=self.data_dir_path + 'D_800439_nmr-data-str_P1.str.V2', cifPath=self.data_dir_path + 'D_800439_nmr-data-str_P1.cif.V2', originalFileName='KpbK.str')

if __name__ == '__main__':
    unittest.main()
