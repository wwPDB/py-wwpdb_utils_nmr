##
# File: test_NmrStarToCif.py
# Date:  02-Apr-2020  M. Yokochi
#
# Updates:
# 20-Oct-2021  M. Yokochi - add unit test for case-sensitive saveframe name (DAOTHER-7398, 7407)
#
import unittest
import os
import sys
from shutil import copyfile

if __package__ is None or __package__ == "":
    from os import path

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from commonsetup import TESTOUTPUT  # noqa:  F401 pylint: disable=import-error,unused-import
else:
    from .commonsetup import TESTOUTPUT  # noqa: F401 pylint: disable=relative-beyond-top-level

try:
    from wwpdb.utils.nmr.NmrStarToCif import NmrStarToCif
except ImportError:
    from nmr.NmrStarToCif import NmrStarToCif


if __package__ is None or __package__ == "":
    from os import path

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from commonsetup import TESTOUTPUT  # noqa: F401, pylint: disable=import-error,unused-import
else:
    from .commonsetup import TESTOUTPUT  # noqa: F401, pylint: disable=relative-beyond-top-level


class TestNmrStarToCif(unittest.TestCase):
    def setUp(self):
        here = os.path.abspath(os.path.dirname(__file__))
        self.data_dir_path = os.path.join(here, os.pardir, "tests-nmr", "mock-data")
        self.nmrstar_to_cif = NmrStarToCif()

    def tearDown(self):
        pass

    def test_unified(self):
        strPath = os.path.join(self.data_dir_path, "D_800269_nmr-data-str_P1.str.V1")
        outPath = os.path.join(TESTOUTPUT, "D_800269_nmr-data-str_P1.cif")
        ret = self.nmrstar_to_cif.convert(strPath=strPath, cifPath=outPath, originalFileName="2png.nef")

        self.assertTrue(ret)
        self.assertTrue(os.path.isfile(outPath))

    def test_legacy(self):
        refPathIn = os.path.join(self.data_dir_path, "D_800262_cs-upload-convert_P1.cif.V1")
        tempCif = os.path.join(TESTOUTPUT, "D_800262_cs-upload-convert_P1.cif.V8")
        copyfile(refPathIn, tempCif)
        ret = self.nmrstar_to_cif.clean(cifPath=tempCif, originalCsFileNameList=["D_800262_cs.str"])
        self.assertTrue(ret)

    def test_daother_5829(self):
        refPathIn = os.path.join(self.data_dir_path, "D_800350_cs_P1.cif.V2")
        tempCif = os.path.join(TESTOUTPUT, "D_800350_cs_P1.cif.V1")
        copyfile(refPathIn, tempCif)
        ret = self.nmrstar_to_cif.clean(cifPath=tempCif, originalCsFileNameList=["Ost4V23D.star"])
        self.assertTrue(ret)

    def test_D_1292117503(self):
        strPath = os.path.join(self.data_dir_path, "D_800439_nmr-data-str_P1.str.V2")
        cifPath = os.path.join(TESTOUTPUT, "D_800439_nmr-data-str_P1.cif.V2")
        ret = self.nmrstar_to_cif.convert(strPath=strPath, cifPath=cifPath, originalFileName="KpbK.str")
        self.assertTrue(ret)
        self.assertTrue(os.path.isfile(cifPath))

    def test_daother_7389(self):
        strPath = os.path.join(self.data_dir_path, "D_800444_nmr-data-str-upload-convert_P1.str.V1")
        cifPath = os.path.join(TESTOUTPUT, "D_800444_nmr-data-str-upload-convert_P1.cif.V1")
        ret = self.nmrstar_to_cif.convert(strPath=strPath, cifPath=cifPath, originalFileName="kbpk_letterCaseTest.nef")
        self.assertTrue(ret)
        self.assertTrue(os.path.isfile(cifPath))


if __name__ == "__main__":
    unittest.main()
