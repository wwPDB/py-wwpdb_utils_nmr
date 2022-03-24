##
# File: test_NmrDpUtility.py
# Date:  26-Sep-2019  M. Yokochi
#
# Updates:
# 09-Oct-2019  M. Yokochi - add unit test for Xplor-NIH enabling 'check_mandatory_tag' option
# 28-Nov-2019  M. Yokochi - add unit test for NEF-Xplor-NIH-20191016-remediated.nef
# 26-Feb-2020  M. Yokochi - add unit test for CCPN_2mtv_docr.nef (DAOTHER-4785)
# 24-Mar-2020  M. Yokochi - add unit test for chemical shift reference (DAOTHER-1682)
# 14-May-2020  M. Yokochi - add unit tests for missing mandatory content (DAOTHER-5681 and 5682)
# 30-May-2020  M. Yokochi - add unit test for detection of total number of models (DAOTHER-5650)
# 08-Jul-2020  M. Yokochi - add unit test for combined NMR-STAR (DAOTHER-5926)
# 24-Aug-2021  M. Yokochi - add support for XPLOR-NIH planarity restraints (DAOTHER-7265)
# 27-Jan-2022  M. Yokochi - add restraint types described by XPLOR-NIH, CNS, CYANA, and AMBER systems (NMR restraint remediation)
# 04-Mar-2022  M. Yokochi - add coordinate geometry restraint (DAOTHER-7690, NMR restraint remediation)
#
import unittest
import os
import sys

if __package__ is None or __package__ == "":
    from os import path

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from commonsetup import TESTOUTPUT  # noqa:  F401 pylint: disable=import-error,unused-import
else:
    from .commonsetup import TESTOUTPUT  # noqa: F401 pylint: disable=relative-beyond-top-level

from wwpdb.utils.nmr.NmrDpUtility import NmrDpUtility
from wwpdb.utils.nmr.NmrDpReport import NmrDpReportInputSource
from testfixtures import LogCapture


skipsome = True
if os.getenv("FULLTEST") is not None:
    skipsome = False


class TestNmrDpUtility(unittest.TestCase):
    def setUp(self):
        here = os.path.abspath(os.path.dirname(__file__))
        self.data_dir_path = os.path.join(here, os.pardir, "tests-nmr", "mock-data")
        self.utility = NmrDpUtility()

    def tearDown(self):
        pass

    def test_init(self):
        nmr_content_subtypes = set(self.utility.nmr_content_subtypes)

        self.assertEqual(nmr_content_subtypes, set(self.utility.sf_categories["nef"].keys()))
        self.assertEqual(nmr_content_subtypes, set(self.utility.sf_categories["nmr-star"].keys()))

        self.assertEqual(nmr_content_subtypes, set(self.utility.lp_categories["nef"].keys()))
        self.assertEqual(nmr_content_subtypes, set(self.utility.lp_categories["nmr-star"].keys()))

        # compare NMR content subtypes in NmrDpReportInputSource
        input_source = NmrDpReportInputSource()
        self.assertEqual(
            set(nmr_content_subtypes),
            set(input_source.content_subtypes)
            - {
                "plane_restraint",
                "adist_restraint",
                "jcoup_restraint",
                "hvycs_restraint",
                "procs_restraint",
                "rama_restraint",
                "radi_restraint",
                "diff_restraint",
                "nbase_restraint",
                "csa_restraint",
                "ang_restraint",
                "pre_restraint",
                "pcs_restraint",
                "prdc_restraint",
                "pang_restraint",
                "pccr_restraint",
                "noepk_restraint",
                "hbond_restraint",
                "geo_restraint",
                "coordinate",
                "non_poly",
                "topology",
            },
        )

        # data directory exists
        self.assertEqual(os.path.isdir(self.data_dir_path), True)

    def test_nmr_nef_consistency(self):
        # no input
        with LogCapture() as _logs:
            with self.assertRaises(ValueError):
                self.utility.op("nmr-nef-consistency-check")

        with LogCapture() as _logs:
            with self.assertRaises(IOError):
                self.utility.setSource("dummydummy")

        srcPath = os.path.join(self.data_dir_path, "2l9r.nef")
        self.utility.setSource(srcPath)
        self.utility.addInput(name="coordinate_file_path", value=srcPath, type="file")

        # invalid workflow operation
        with LogCapture() as _logs:  # noqa: F841
            with self.assertRaises(KeyError):
                self.utility.op("nmr")

        self.utility.setLog(os.path.join(TESTOUTPUT, "2l9r-nef-consistency-log.json"))

        self.utility.op("nmr-nef-consistency-check")

    def test_nmr_str_consistency(self):
        # no input
        with LogCapture() as _logs:
            with self.assertRaises(ValueError):
                self.utility.op("nmr-str-consistency-check")

        with LogCapture() as _logs:
            with self.assertRaises(IOError):
                self.utility.setSource("dummydummy")

        self.utility.setSource(os.path.join(self.data_dir_path, "2l9r.str"))
        self.utility.addInput(name="coordinate_file_path", value=os.path.join(self.data_dir_path, "2l9r.cif"), type="file")

        # invalid workflow operation
        with LogCapture() as _logs:  # noqa: F841
            with self.assertRaises(KeyError):
                self.utility.op("nmr")

        self.utility.setLog(os.path.join(TESTOUTPUT, "2l9r-str-consistency-log.json"))

        self.utility.op("nmr-str-consistency-check")

    def test_nmr_nef_consistency_check_non_std_residue(self):
        self.utility.setSource(os.path.join(self.data_dir_path, "2l9rnonstandard.nef"))
        self.utility.setLog(os.path.join(TESTOUTPUT, "2l9rnonstandard-nef-consistency-log.json"))

        self.utility.op("nmr-nef-consistency-check")

    @unittest.skipIf(skipsome is True, "Skip some tests")
    def test_nmr_nef_consistency_check_former_nef(self):
        self.utility.setSource(os.path.join(self.data_dir_path, "2l9rold.nef"))
        self.utility.setLog(os.path.join(TESTOUTPUT, "2l9rold-nef-consistency-log.json"))

        self.utility.op("nmr-nef-consistency-check")

    @unittest.skipIf(skipsome is True, "Skip some tests")
    def test_nmr_nef_consistency_check_cys(self):
        self.utility.setSource(os.path.join(self.data_dir_path, "2l9r-cys.nef"))
        self.utility.setLog(os.path.join(TESTOUTPUT, "2l9r-cys-nef-consistency-log.json"))

        self.utility.op("nmr-nef-consistency-check")

    @unittest.skipIf(skipsome is True, "Skip some tests")
    def test_nmr_nef_consistency_check_xplor_nih(self):
        self.utility.setSource(os.path.join(self.data_dir_path, "mth1743-test-20190919.nef"))
        self.utility.addInput(name="coordinate_file_path", value=os.path.join(self.data_dir_path, "1ryg.cif"), type="file")
        self.utility.addInput(name="resolve_conflict", value=True, type="param")
        self.utility.addInput(name="check_mandatory_tag", value=True, type="param")
        self.utility.setLog(os.path.join(TESTOUTPUT, "mth1743-test-20190919-nef-consistency-log.json"))

        self.utility.op("nmr-nef-consistency-check")

    @unittest.skipIf(skipsome is True, "Skip some tests")
    def test_nmr_nef_consistency_check_xplor_nih_remediated(self):
        self.utility.setSource(os.path.join(self.data_dir_path, "NEF-Xplor-NIH-20191016-remediated.nef"))
        self.utility.addInput(name="coordinate_file_path", value=os.path.join(self.data_dir_path, "1ryg.cif"), type="file")
        self.utility.addInput(name="resolve_conflict", value=True, type="param")
        self.utility.addInput(name="check_mandatory_tag", value=True, type="param")
        self.utility.setLog(os.path.join(TESTOUTPUT, "NEF-Xplor-NIH-20191016-remediated-nef-consistency-log.json"))

        self.utility.op("nmr-nef-consistency-check")

    @unittest.skipIf(skipsome is True, "Skip some tests")
    def test_nmr_nef_consistency_check_daother_4785(self):
        self.utility.setSource(os.path.join(self.data_dir_path, "CCPN_2mtv_docr.nef"))
        self.utility.addInput(name="coordinate_file_path", value=os.path.join(self.data_dir_path, "2mtv.cif"), type="file")
        self.utility.addInput(name="resolve_conflict", value=True, type="param")
        self.utility.addInput(name="check_mandatory_tag", value=True, type="param")
        self.utility.setLog(os.path.join(TESTOUTPUT, "ccpn_2mtv_docr-nef-consistency-log.json"))

        self.utility.op("nmr-nef-consistency-check")

    @unittest.skipIf(skipsome is True, "Skip some tests")
    def test_nmr_nef_consistency_check_daother_5681(self):
        self.utility.setSource(os.path.join(self.data_dir_path, "2k2e.nef-withoutrestraints"))
        self.utility.addInput(name="coordinate_file_path", value=os.path.join(self.data_dir_path, "2k2e.cif"), type="file")
        self.utility.addInput(name="resolve_conflict", value=True, type="param")
        self.utility.addInput(name="check_mandatory_tag", value=True, type="param")
        self.utility.setLog(os.path.join(TESTOUTPUT, "2k2e.nef-withoutrestraints-consistency-log.json"))
        self.utility.setVerbose(False)

        self.utility.op("nmr-nef-consistency-check")

    @unittest.skipIf(skipsome is True, "Skip some tests")
    def test_nmr_nef_consistency_check_daother_5682(self):
        self.utility.setSource(os.path.join(self.data_dir_path, "2k2e.nef-withoutchemicalshifts"))
        self.utility.addInput(name="coordinate_file_path", value=os.path.join(self.data_dir_path, "2k2e.cif"), type="file")
        self.utility.addInput(name="resolve_conflict", value=True, type="param")
        self.utility.addInput(name="check_mandatory_tag", value=True, type="param")
        self.utility.setLog(os.path.join(TESTOUTPUT, "2k2e.nef-withoutchemicalshifts-consistency-log.json"))
        self.utility.setVerbose(False)

        self.utility.op("nmr-nef-consistency-check")

    @unittest.skipIf(skipsome is True, "Skip some tests")
    def test_nmr_nef_consistency_check_daother_5682_modified(self):
        self.utility.setSource(os.path.join(self.data_dir_path, "2k2e.nef-withoutchemicalshifts-modified"))
        self.utility.addInput(name="coordinate_file_path", value=os.path.join(self.data_dir_path, "2k2e.cif"), type="file")
        self.utility.addInput(name="resolve_conflict", value=True, type="param")
        self.utility.addInput(name="check_mandatory_tag", value=True, type="param")
        self.utility.setLog(os.path.join(TESTOUTPUT, "2k2e.nef-withoutchemicalshifts-modified-consistency-log.json"))
        self.utility.setVerbose(False)

        self.utility.op("nmr-nef-consistency-check")

    @unittest.skipIf(skipsome is True, "Skip some tests")
    def test_nmr_nef_consistency_check_daother_5650(self):
        self.utility.setSource(os.path.join(self.data_dir_path, os.pardir, "NMR-VTF", "PDBStat_it2", "2k2e/2k2e.nef"))
        self.utility.addInput(name="coordinate_file_path", value=os.path.join(self.data_dir_path, "2k2e.cif-only2models"), type="file")
        self.utility.addInput(name="resolve_conflict", value=True, type="param")
        self.utility.addInput(name="check_mandatory_tag", value=True, type="param")
        self.utility.setLog(os.path.join(TESTOUTPUT, "2k2e.nef-only2models-consistency-log.json"))
        self.utility.setVerbose(False)

        self.utility.op("nmr-nef-consistency-check")

    @unittest.skipIf(skipsome is True, "Skip some tests")
    def test_nmr_str_consistency_check_bmrb_merged(self):
        self.utility.setSource(os.path.join(self.data_dir_path, "merged_30562_6nox.str"))
        self.utility.addInput(name="coordinate_file_path", value=os.path.join(self.data_dir_path, "6nox.cif"), type="file")
        self.utility.setLog(os.path.join(TESTOUTPUT, "merged_30562_6nox-str-consistency-log.json"))

        self.utility.op("nmr-str-consistency-check")

    def test_nmr_nef2str_deposit_str(self):
        nefSrcPath = os.path.join(self.data_dir_path, "2l9r.nef")
        modelSrcPath = os.path.join(self.data_dir_path, "2l9r.cif")
        consistJsonPath = os.path.join(TESTOUTPUT, "2l9r-nef2str-str-consistency-log.json")

        self.utility.setSource(nefSrcPath)
        self.utility.addInput(name="coordinate_file_path", value=modelSrcPath, type="file")
        self.utility.setLog(consistJsonPath)

        self.utility.op("nmr-nef-consistency-check")

        self.utility.setSource(nefSrcPath)
        self.utility.addInput(name="coordinate_file_path", value=modelSrcPath, type="file")
        self.utility.addInput(name="report_file_path", value=consistJsonPath, type="file")
        self.utility.setLog(os.path.join(TESTOUTPUT, "2l9r-nef2str-str-deposit-log.json"))
        self.utility.setDestination(os.path.join(TESTOUTPUT, "2l9r-nef2str-str.str"))
        self.utility.addOutput(name="nmr-star_file_path", value=os.path.join(TESTOUTPUT, "2l9r-nef2str-str-nef2str.str"), type="file")
        self.utility.addOutput(name="report_file_path", value=os.path.join(TESTOUTPUT, "2l9r-nef2str-str-str-deposit-log.json"), type="file")
        self.utility.addOutput(name="entry_id", value="2l9r", type="param")
        self.utility.addOutput(name="insert_entry_id_to_loops", value=True, type="param")
        self.utility.setVerbose(False)

        self.utility.op("nmr-nef2str-deposit")

    def test_nmr_str2str_deposit_nef(self):
        nefSrcPath = os.path.join(self.data_dir_path, "2l9r.nef")
        modelSrcPath = os.path.join(self.data_dir_path, "2l9r.cif")
        jsonLogPath = os.path.join(TESTOUTPUT, "2l9r-str2str-nef-consistency-log.json")

        self.utility.setSource(nefSrcPath)
        self.utility.addInput(name="coordinate_file_path", value=modelSrcPath, type="file")
        self.utility.setLog(jsonLogPath)

        self.utility.op("nmr-str-consistency-check")

        self.utility.setSource(nefSrcPath)
        self.utility.addInput(name="coordinate_file_path", value=modelSrcPath, type="file")
        self.utility.addInput(name="report_file_path", value=jsonLogPath, type="file")
        self.utility.setLog(os.path.join(TESTOUTPUT, "2l9r-str2str-nef-deposit-log.json"))
        self.utility.addOutput(name="entry_id", value="2l9r", type="param")
        self.utility.addOutput(name="insert_entry_id_to_loops", value=True, type="param")
        self.utility.setVerbose(False)

        self.utility.op("nmr-str2str-deposit")

    def test_nmr_nef2str_deposit(self):
        jsonLogPath = os.path.join(TESTOUTPUT, "2l9r-nef-consistency-log.json")
        if not os.access(jsonLogPath, os.F_OK):
            self.test_nmr_nef_consistency()

        self.utility.setSource(os.path.join(self.data_dir_path, "2l9r.nef"))
        self.utility.addInput(name="coordinate_file_path", value=os.path.join(self.data_dir_path, "2l9r.cif"), type="file")
        self.utility.addInput(name="report_file_path", value=jsonLogPath, type="file")
        self.utility.setLog(os.path.join(TESTOUTPUT, "2l9r-nef2str-deposit-log.json"))
        self.utility.setDestination(os.path.join(TESTOUTPUT, "2l9r-next.nef"))
        self.utility.addOutput(name="nmr-star_file_path", value=os.path.join(TESTOUTPUT, "2l9r-nef2str.str"), type="file")
        self.utility.addOutput(name="report_file_path", value=os.path.join(TESTOUTPUT, "2l9r-nef2str-str-deposit-log.json"), type="file")
        self.utility.addOutput(name="entry_id", value="NEED_ACC_NO", type="param")
        self.utility.setVerbose(False)

        self.utility.op("nmr-nef2str-deposit")

    @unittest.skipIf(skipsome is True, "Skip some tests")
    def test_nmr_nef2str_deposit_check_cys(self):
        jsonLogPath = os.path.join(TESTOUTPUT, "2l9r-cys-nef-consistency-log.json")
        if not os.access(jsonLogPath, os.F_OK):
            self.test_nmr_nef_consistency_check_cys()

        self.utility.setSource(os.path.join(self.data_dir_path, "2l9r-cys.nef"))
        self.utility.addInput(name="coordinate_file_path", value=os.path.join(self.data_dir_path, "2l9r-cys.cif"), type="file")
        self.utility.addInput(name="report_file_path", value=jsonLogPath, type="file")
        self.utility.setLog(os.path.join(TESTOUTPUT, "2l9r-cys-nef2str-deposit-log.json"))
        self.utility.setDestination(os.path.join(TESTOUTPUT, "2l9r-cys-next.nef"))
        self.utility.addOutput(name="nmr-star_file_path", value=os.path.join(TESTOUTPUT, "2l9r-cys-nef2str.str"), type="file")
        self.utility.addOutput(name="report_file_path", value=os.path.join(TESTOUTPUT, "2l9r-cys-nef2str-str-deposit-log.json"), type="file")
        self.utility.addOutput(name="entry_id", value="NEED_ACC_NO", type="param")
        self.utility.setVerbose(False)

        self.utility.op("nmr-nef2str-deposit")

    @unittest.skipIf(skipsome is True, "Skip some tests")
    def test_nmr_nef2str_deposit_check_xplor_nih(self):
        jsonLogPath = os.path.join(TESTOUTPUT, "mth1743-test-20190919-nef-consistency-log.json")
        if not os.access(jsonLogPath, os.F_OK):
            self.test_nmr_nef_consistency_check_xplor_nih()

        self.utility.setSource(os.path.join(self.data_dir_path, "mth1743-test-20190919.nef"))
        self.utility.addInput(name="coordinate_file_path", value=os.path.join(self.data_dir_path, "1ryg.cif"), type="file")
        self.utility.addInput(name="report_file_path", value=jsonLogPath, type="file")
        self.utility.addInput(name="resolve_conflict", value=True, type="param")
        self.utility.addInput(name="check_mandatory_tag", value=True, type="param")
        self.utility.setLog(os.path.join(TESTOUTPUT, "mth1743-test-20190919-nef2str-deposit-log.json"))
        self.utility.setDestination(os.path.join(TESTOUTPUT, "mth1743-test-20190919-next.nef"))
        self.utility.addOutput(name="nmr-star_file_path", value=os.path.join(TESTOUTPUT, "mth1743-test-20190919-nef2str.str"), type="file")
        self.utility.addOutput(name="report_file_path", value=os.path.join(TESTOUTPUT, "mth1743-test-20190919-nef2str-str-deposit-log.json"), type="file")
        self.utility.addOutput(name="entry_id", value="NEED_ACC_NO", type="param")
        self.utility.setVerbose(False)

        self.utility.op("nmr-nef2str-deposit")

    @unittest.skipIf(skipsome is True, "Skip some tests")
    def test_nmr_nef2str_deposit_check_daother_4785(self):
        jsonLogPath = os.path.join(TESTOUTPUT, "ccpn_2mtv_docr-nef-consistency-log.json")
        if not os.access(jsonLogPath, os.F_OK):
            self.test_nmr_nef_consistency_check_daother_4785()

        self.utility.setSource(os.path.join(self.data_dir_path, "CCPN_2mtv_docr.nef"))
        self.utility.addInput(name="coordinate_file_path", value=os.path.join(self.data_dir_path, "2mtv.cif"), type="file")
        self.utility.addInput(name="report_file_path", value=jsonLogPath, type="file")
        self.utility.addInput(name="resolve_conflict", value=True, type="param")
        self.utility.addInput(name="check_mandatory_tag", value=True, type="param")
        self.utility.setLog(os.path.join(TESTOUTPUT, "ccpn_2mtv_docr-nef2str-deposit-log.json"))
        self.utility.setDestination(os.path.join(TESTOUTPUT, "ccpn_2mtv_docr-next.nef"))
        self.utility.addOutput(name="nmr-star_file_path", value=os.path.join(TESTOUTPUT, "ccpn_2mtv_docr-nef2str.str"), type="file")
        self.utility.addOutput(name="report_file_path", value=os.path.join(TESTOUTPUT, "ccpn_2mtv_docr-nef2str-str-deposit-log.json"), type="file")
        self.utility.addOutput(name="entry_id", value="NEED_ACC_NO", type="param")
        self.utility.setVerbose(False)

        self.utility.op("nmr-nef2str-deposit")

    @unittest.skipIf(skipsome is True, "Skip some tests")
    def test_nmr_str2str_deposit(self):
        jsonLogPath = os.path.join(TESTOUTPUT, "2l9r-str-consistency-log.json")
        if not os.access(jsonLogPath, os.F_OK):
            self.test_nmr_str_consistency()

        self.utility.setSource(os.path.join(self.data_dir_path, "2l9r.str"))
        self.utility.addInput(name="coordinate_file_path", value=os.path.join(self.data_dir_path, "2l9r.cif"), type="file")
        self.utility.addInput(name="report_file_path", value=jsonLogPath, type="file")
        self.utility.setLog(os.path.join(TESTOUTPUT, "2l9r-str2str-deposit-log.json"))
        self.utility.setDestination(os.path.join(TESTOUTPUT, "2l9r-next.str"))
        self.utility.addOutput(name="entry_id", value="NEED_ACC_NO", type="param")
        self.utility.addOutput(name="insert_entry_id_to_loops", value=True, type="param")
        self.utility.setVerbose(False)

        self.utility.op("nmr-str2str-deposit")

    @unittest.skipIf(skipsome is True, "Skip some tests")
    def test_nmr_nef2str_deposit_check_non_std_residue(self):
        jsonLogPath = os.path.join(TESTOUTPUT, "2l9rnonstandard-nef-consistency-log.json")
        if not os.access(jsonLogPath, os.F_OK):
            self.test_nmr_nef_consistency_check_non_std_residue()

        self.utility.setSource(os.path.join(self.data_dir_path, "2l9rnonstandard.nef"))
        self.utility.addInput(name="coordinate_file_path", value=os.path.join(self.data_dir_path, "2l9r.cif"), type="file")
        self.utility.addInput(name="report_file_path", value=jsonLogPath, type="file")
        self.utility.setLog(os.path.join(TESTOUTPUT, "2l9rnonstandard-nef2str-deposit-log.json"))
        self.utility.setDestination(os.path.join(TESTOUTPUT, "2l9rnonstandard-next.nef"))
        self.utility.addOutput(name="nmr-star_file_path", value=os.path.join(TESTOUTPUT, "2l9rnonstandard-nef2str.str"), type="file")
        self.utility.addOutput(name="report_file_path", value=os.path.join(TESTOUTPUT, "2l9rnonstandard-nef2str-str-deposit-log.json"), type="file")
        self.utility.addOutput(name="entry_id", value="NEED_ACC_NO", type="param")
        self.utility.setVerbose(False)

        self.utility.op("nmr-nef2str-deposit")

    @unittest.skipIf(skipsome is True, "Skip some tests")
    def test_nmr_str2str_deposit_bmrb_merged(self):
        strSrcPath = os.path.join(self.data_dir_path, "merged_30562_6nox.str")
        modelSrcPath = os.path.join(self.data_dir_path, "6nox.cif")
        jsonLogPath = os.path.join(TESTOUTPUT, "merged_30562_6nox-str-consistency-log.json")

        self.utility.setSource(strSrcPath)
        self.utility.addInput(name="coordinate_file_path", value=modelSrcPath, type="file")
        self.utility.setLog(jsonLogPath)

        self.utility.op("nmr-str-consistency-check")

        self.utility.setSource(strSrcPath)
        self.utility.addInput(name="coordinate_file_path", value=modelSrcPath, type="file")
        self.utility.addInput(name="report_file_path", value=jsonLogPath, type="file")
        self.utility.addInput(name="nonblk_anomalous_cs", value=True, type="param")
        self.utility.addInput(name="nonblk_bad_nterm", value=True, type="param")
        self.utility.setLog(os.path.join(TESTOUTPUT, "merged_30562_6nox-str2str-deposit-log.json"))
        self.utility.setDestination(os.path.join(TESTOUTPUT, "merged_30562_6nox-next.str"))
        self.utility.addOutput(name="entry_id", value="6nox", type="param")
        self.utility.addOutput(name="insert_entry_id_to_loops", value=True, type="param")
        self.utility.setVerbose(False)

        self.utility.op("nmr-str2str-deposit")

    @unittest.skip("Until test corrected")
    def test_nmr_str2str_deposit_cleaned(self):
        self.utility.setSource(os.path.join(self.data_dir_path, "24642_2mqq-clean.str"))
        self.utility.addInput(name="coordinate_file_path", value=os.path.join(self.data_dir_path, "2mqq.cif"), type="file")
        self.utility.setLog(os.path.join(TESTOUTPUT, "24642_2mqq-str2str-consistency-log.json"))

        self.utility.op("nmr-str-consistency-check")

        self.utility.setSource(os.path.join(self.data_dir_path, "24642_2mqq-clean.str"))
        self.utility.addInput(name="coordinate_file_path", value=os.path.join(self.data_dir_path, "2mqq.cif"), type="file")
        self.utility.addInput(name="report_file_path", value=os.path.join(TESTOUTPUT, "24642_2mqq-str2str-consistency-log.json"), type="file")
        self.utility.setLog(os.path.join(TESTOUTPUT, "24642-str2str-deposit-log.json"))
        self.utility.setDestination(os.path.join(TESTOUTPUT, "24642_2mqq-clean-next.str"))
        self.utility.addOutput(name="entry_id", value="2mqq", type="param")
        self.utility.addOutput(name="insert_entry_id_to_loops", value=True, type="param")
        self.utility.setVerbose(False)

        self.utility.op("nmr-str2str-deposit")

    @unittest.skipIf(skipsome is True, "Skip some tests")
    def test_nmr_str2str_deposit_chem_shift_ref(self):
        self.utility.setSource(os.path.join(self.data_dir_path, "2la6-chem-shift-ref.str"))
        self.utility.addInput(name="coordinate_file_path", value=os.path.join(self.data_dir_path, "2la6.cif"), type="file")
        self.utility.setLog(os.path.join(TESTOUTPUT, "2la6-chem-shift-ref-consistency-log.json"))

        self.utility.op("nmr-str-consistency-check")

        self.utility.setSource(os.path.join(self.data_dir_path, "2la6-chem-shift-ref.str"))
        self.utility.addInput(name="coordinate_file_path", value=os.path.join(self.data_dir_path, "2la6.cif"), type="file")
        self.utility.addInput(name="report_file_path", value=os.path.join(TESTOUTPUT, "2la6-chem-shift-ref-consistency-log.json"), type="file")
        self.utility.setLog(os.path.join(TESTOUTPUT, "2la6-chem-shift-ref-deposit-log.json"))
        self.utility.setDestination(os.path.join(TESTOUTPUT, "2la6-chem-shift-ref-next.str"))
        self.utility.addOutput(name="entry_id", value="2la6", type="param")
        self.utility.addOutput(name="insert_entry_id_to_loops", value=True, type="param")
        self.utility.setVerbose(False)

        self.utility.op("nmr-str2str-deposit")

    @unittest.skipIf(skipsome is True, "Skip some tests")
    def test_nmr_str_consistency_check_review(self):
        self.utility.setSource(os.path.join(self.data_dir_path, "D_800107_nmr-data-str-review_P1.str.V20.rev"))
        self.utility.addInput(name="coordinate_file_path", value=os.path.join(self.data_dir_path, "D_800107_model_P1.cif.V3"), type="file")
        self.utility.setLog(os.path.join(TESTOUTPUT, "D_800107_nmr-data-str-consistency-log.json"))

        self.utility.op("nmr-str-consistency-check")

        # pynmrstar.Entry.from_file(self.data_dir_path + 'D_800107_nmr-data-str-review_P1.str.V20.rev')

    @unittest.skipIf(skipsome is True, "Skip some tests")
    def test_nmr_str_consistency_check_daother_5926(self):
        self.utility.setSource(os.path.join(self.data_dir_path, "swallow_NMR-Star_3-1.str"))
        self.utility.addInput(name="coordinate_file_path", value=os.path.join(self.data_dir_path, "D_800365_model_P1.cif.V4"), type="file")
        self.utility.addInput(name="nonblk_anomalous_cs", value=True, type="param")
        self.utility.addInput(name="nonblk_bad_nterm", value=True, type="param")
        self.utility.addInput(name="resolve_conflict", value=True, type="param")
        self.utility.addInput(name="check_mandatory_tag", value=True, type="param")
        self.utility.setLog(os.path.join(TESTOUTPUT, "daother-5926-str-consistency-log.json"))
        self.utility.setVerbose(False)

        self.utility.op("nmr-str-consistency-check")

    @unittest.skipIf(skipsome is True, "Skip some tests")
    def test_nmr_str2str_deposit_daother_5926(self):
        jsonLogPath = os.path.join(TESTOUTPUT, "daother-5926-str-consistency-log.json")
        if not os.access(jsonLogPath, os.F_OK):
            self.test_nmr_str_consistency_check_daother_5926()

        self.utility.setSource(os.path.join(self.data_dir_path, "swallow_NMR-Star_3-1.str"))
        self.utility.addInput(name="coordinate_file_path", value=os.path.join(self.data_dir_path, "D_800365_model_P1.cif.V4"), type="file")
        self.utility.addInput(name="report_file_path", value=jsonLogPath, type="file")
        self.utility.addInput(name="nonblk_anomalous_cs", value=True, type="param")
        self.utility.addInput(name="nonblk_bad_nterm", value=True, type="param")
        self.utility.addInput(name="resolve_conflict", value=True, type="param")
        self.utility.addInput(name="check_mandatory_tag", value=True, type="param")
        self.utility.setLog(os.path.join(TESTOUTPUT, "daother-5926-str2str-deposit-log.json"))
        self.utility.setDestination(os.path.join(TESTOUTPUT, "swallow_NMR-Star_3-1-next.str"))
        self.utility.setVerbose(False)

        self.utility.op("nmr-str2str-deposit")


if __name__ == "__main__":
    unittest.main()
