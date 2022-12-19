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
# 20-Oct-2022  M. Yokochi - add support for CYANA/ROSETTA disulfide bond restraint (NMR restraint remediation)
#
import unittest
import os

from wwpdb.utils.nmr.NmrDpUtility import NmrDpUtility
from wwpdb.utils.nmr.NmrDpReport import NmrDpReportInputSource


class TestNmrDpUtility(unittest.TestCase):

    def setUp(self):
        here = os.path.abspath(os.path.dirname(__file__))
        self.data_dir_path = os.path.join(here, 'mock-data/')
        self.utility = NmrDpUtility()

    def tearDown(self):
        pass

    def test_init(self):
        nmr_content_subtypes = set(self.utility.nmr_content_subtypes)

        self.assertEqual(nmr_content_subtypes, set(self.utility.sf_categories['nef'].keys()))
        self.assertEqual(nmr_content_subtypes, set(self.utility.sf_categories['nmr-star'].keys()))

        self.assertEqual(nmr_content_subtypes, set(self.utility.lp_categories['nef'].keys()))
        self.assertEqual(nmr_content_subtypes, set(self.utility.lp_categories['nmr-star'].keys()))

        # compare NMR content subtypes in NmrDpReportInputSource
        input_source = NmrDpReportInputSource()
        self.assertEqual(set(nmr_content_subtypes), set(input_source.content_subtypes)
                         - {'plane_restraint', 'adist_restraint',
                            'rama_restraint', 'radi_restraint', 'diff_restraint',
                            'nbase_restraint', 'ang_restraint', 'pre_restraint',
                            'pcs_restraint', 'prdc_restraint', 'pang_restraint', 'pccr_restraint',
                            'hbond_restraint', 'ssbond_restraint', 'geo_restraint',
                            'coordinate', 'branched', 'non_poly', 'topology'})

        # data directory exists
        self.assertEqual(os.path.isdir(self.data_dir_path), True)

    def test_nmr_nef_consistency(self):
        # no input
        with self.assertRaises(ValueError):
            self.utility.op('nmr-nef-consistency-check')

        with self.assertRaises(IOError):
            self.utility.setSource('dummydummy')

        self.utility.setSource(self.data_dir_path + '2l9r.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2l9r.cif', type='file')

        # invalid workflow operation
        with self.assertRaises(KeyError):
            self.utility.op('nmr')

        self.utility.setLog(self.data_dir_path + '2l9r-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_str_consistency(self):
        # no input
        with self.assertRaises(ValueError):
            self.utility.op('nmr-str-consistency-check')

        with self.assertRaises(IOError):
            self.utility.setSource('dummydummy')

        self.utility.setSource(self.data_dir_path + '2l9r.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2l9r.cif', type='file')

        # invalid workflow operation
        with self.assertRaises(KeyError):
            self.utility.op('nmr')

        self.utility.setLog(self.data_dir_path + '2l9r-str-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

    def test_nmr_nef_consistency_check_non_std_residue(self):
        self.utility.setSource(self.data_dir_path + '2l9rnonstandard.nef')
        self.utility.setLog(self.data_dir_path + '2l9rnonstandard-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_nef_consistency_check_no_distance(self):
        self.utility.setSource(self.data_dir_path + '2l9r-no-distance.nef')
        self.utility.setLog(self.data_dir_path + '2l9rnodistance-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_nef_consistency_check_former_nef(self):
        self.utility.setSource(self.data_dir_path + '2l9rold.nef')
        self.utility.setLog(self.data_dir_path + '2l9rold-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_nef_consistency_check_cys(self):
        self.utility.setSource(self.data_dir_path + '2l9r-cys.nef')
        self.utility.setLog(self.data_dir_path + '2l9r-cys-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_nef_consistency_check_xplor_nih(self):
        self.utility.setSource(self.data_dir_path + 'mth1743-test-20190919.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '1ryg.cif', type='file')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.setLog(self.data_dir_path + 'mth1743-test-20190919-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_nef_consistency_check_xplor_nih_remediated(self):
        self.utility.setSource(self.data_dir_path + 'NEF-Xplor-NIH-20191016-remediated.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '1ryg.cif', type='file')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.setLog(self.data_dir_path + 'NEF-Xplor-NIH-20191016-remediated-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_nef_consistency_check_daother_4785(self):
        self.utility.setSource(self.data_dir_path + 'CCPN_2mtv_docr.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2mtv.cif', type='file')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.setLog(self.data_dir_path + 'ccpn_2mtv_docr-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_nef_consistency_check_daother_5681(self):
        self.utility.setSource(self.data_dir_path + '2k2e.nef-withoutrestraints')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2k2e.cif', type='file')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.setLog(self.data_dir_path + '2k2e.nef-withoutrestraints-consistency-log.json')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_nef_consistency_check_daother_5682(self):
        self.utility.setSource(self.data_dir_path + '2k2e.nef-withoutchemicalshifts')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2k2e.cif', type='file')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.setLog(self.data_dir_path + '2k2e.nef-withoutchemicalshifts-consistency-log.json')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_nef_consistency_check_daother_5682_modified(self):
        self.utility.setSource(self.data_dir_path + '2k2e.nef-withoutchemicalshifts-modified')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2k2e.cif', type='file')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.setLog(self.data_dir_path + '2k2e.nef-withoutchemicalshifts-modified-consistency-log.json')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_nef_consistency_check_daother_5650(self):
        self.utility.setSource(self.data_dir_path + '../NMR-VTF/PDBStat_it2/2k2e/2k2e.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2k2e.cif-only2models', type='file')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.setLog(self.data_dir_path + '2k2e.nef-only2models-consistency-log.json')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_str_consistency_check_bmrb_merged(self):
        self.utility.setSource(self.data_dir_path + 'merged_30562_6nox.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '6nox.cif', type='file')
        self.utility.setLog(self.data_dir_path + 'merged_30562_6nox-str-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

    def test_nmr_nef2str_deposit_str(self):
        self.utility.setSource(self.data_dir_path + '2l9r.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2l9r.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2l9r-nef2str-str-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

        self.utility.setSource(self.data_dir_path + '2l9r.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2l9r.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2l9r-nef2str-str-consistency-log.json', type='file')
        self.utility.setLog(self.data_dir_path + '2l9r-nef2str-str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2l9r-nef2str-str.str')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2l9r-nef2str-str-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2l9r-nef2str-str-str-deposit-log.json', type='file')
        self.utility.addOutput(name='entry_id', value='2l9r', type='param')
        self.utility.addOutput(name='insert_entry_id_to_loops', value=True, type='param')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef2str-deposit')

    def test_nmr_str2str_deposit_nef(self):
        self.utility.setSource(self.data_dir_path + '2l9r.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2l9r.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2l9r-str2str-nef-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

        self.utility.setSource(self.data_dir_path + '2l9r.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2l9r.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2l9r-str2str-nef-consistency-log.json', type='file')
        self.utility.setLog(self.data_dir_path + '2l9r-str2str-nef-deposit-log.json')
        self.utility.addOutput(name='entry_id', value='2l9r', type='param')
        self.utility.addOutput(name='insert_entry_id_to_loops', value=True, type='param')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str2str-deposit')

    def test_nmr_nef2str_deposit(self):
        if not os.access(self.data_dir_path + '2l9r-nef-consistency-log.json', os.F_OK):
            self.test_nmr_nef_consistency()

        self.utility.setSource(self.data_dir_path + '2l9r.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2l9r.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2l9r-nef-consistency-log.json', type='file')
        self.utility.setLog(self.data_dir_path + '2l9r-nef2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2l9r-next.nef')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2l9r-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2l9r-nef2str-str-deposit-log.json', type='file')
        self.utility.addOutput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef2str-deposit')

    def test_nmr_nef2str_deposit_check_cys(self):
        if not os.access(self.data_dir_path + '2l9r-cys-nef-consistency-log.json', os.F_OK):
            self.test_nmr_nef_consistency_check_cys()

        self.utility.setSource(self.data_dir_path + '2l9r-cys.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2l9r-cys.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2l9r-cys-nef-consistency-log.json', type='file')
        self.utility.setLog(self.data_dir_path + '2l9r-cys-nef2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2l9r-cys-next.nef')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2l9r-cys-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2l9r-cys-nef2str-str-deposit-log.json', type='file')
        self.utility.addOutput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef2str-deposit')

    def test_nmr_nef2str_deposit_check_xplor_nih(self):
        if not os.access(self.data_dir_path + 'mth1743-test-20190919-nef-consistency-log.json', os.F_OK):
            self.test_nmr_nef_consistency_check_xplor_nih()

        self.utility.setSource(self.data_dir_path + 'mth1743-test-20190919.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '1ryg.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + 'mth1743-test-20190919-nef-consistency-log.json', type='file')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.setLog(self.data_dir_path + 'mth1743-test-20190919-nef2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + 'mth1743-test-20190919-next.nef')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + 'mth1743-test-20190919-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + 'mth1743-test-20190919-nef2str-str-deposit-log.json', type='file')
        self.utility.addOutput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef2str-deposit')

    def test_nmr_nef2str_deposit_check_daother_4785(self):
        if not os.access(self.data_dir_path + 'ccpn_2mtv_docr-nef-consistency-log.json', os.F_OK):
            self.test_nmr_nef_consistency_check_daother_4785()

        self.utility.setSource(self.data_dir_path + 'CCPN_2mtv_docr.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2mtv.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + 'ccpn_2mtv_docr-nef-consistency-log.json', type='file')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.setLog(self.data_dir_path + 'ccpn_2mtv_docr-nef2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + 'ccpn_2mtv_docr-next.nef')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + 'ccpn_2mtv_docr-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + 'ccpn_2mtv_docr-nef2str-str-deposit-log.json', type='file')
        self.utility.addOutput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef2str-deposit')

    def test_nmr_str2str_deposit(self):
        if not os.access(self.data_dir_path + '2l9r-str-consistency-log.json', os.F_OK):
            self.test_nmr_str_consistency()

        self.utility.setSource(self.data_dir_path + '2l9r.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2l9r.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2l9r-str-consistency-log.json', type='file')
        self.utility.setLog(self.data_dir_path + '2l9r-str2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2l9r-next.str')
        self.utility.addOutput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.addOutput(name='insert_entry_id_to_loops', value=True, type='param')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str2str-deposit')

    def test_nmr_nef2str_deposit_check_non_std_residue(self):
        if not os.access(self.data_dir_path + '2l9rnonstandard-nef-consistency-log.json', os.F_OK):
            self.test_nmr_nef_consistency_check_non_std_residue()

        self.utility.setSource(self.data_dir_path + '2l9rnonstandard.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2l9r.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2l9rnonstandard-nef-consistency-log.json', type='file')
        self.utility.setLog(self.data_dir_path + '2l9rnonstandard-nef2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2l9rnonstandard-next.nef')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2l9rnonstandard-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2l9rnonstandard-nef2str-str-deposit-log.json', type='file')
        self.utility.addOutput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef2str-deposit')

    def test_nmr_nef2str_deposit_no_distance(self):
        if not os.access(self.data_dir_path + '2l9rnodistance-nef-consistency-log.json', os.F_OK):
            self.test_nmr_nef_consistency_check_no_distance()

        self.utility.setSource(self.data_dir_path + '2l9r-no-distance.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2l9r.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2l9rnodistance-nef-consistency-log.json', type='file')
        self.utility.setLog(self.data_dir_path + '2l9rnodistance-nef2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2l9r-no-distance-next.nef')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2l9r-no-distance-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2l9rnodistance-nef2str-str-deposit-log.json', type='file')
        self.utility.addOutput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef2str-deposit')

    def test_nmr_str2str_deposit_bmrb_merged(self):
        self.utility.setSource(self.data_dir_path + 'merged_30562_6nox.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '6nox.cif', type='file')
        self.utility.setLog(self.data_dir_path + 'merged_30562_6nox-str-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

        self.utility.setSource(self.data_dir_path + 'merged_30562_6nox.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '6nox.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + 'merged_30562_6nox-str-consistency-log.json', type='file')
        self.utility.addInput(name='nonblk_anomalous_cs', value=True, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.setLog(self.data_dir_path + 'merged_30562_6nox-str2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + 'merged_30562_6nox-next.str')
        self.utility.addOutput(name='entry_id', value='6nox', type='param')
        self.utility.addOutput(name='insert_entry_id_to_loops', value=True, type='param')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str2str-deposit')

    def test_nmr_str2str_deposit_cleaned(self):
        self.utility.setSource(self.data_dir_path + '24642_2mqq-clean.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2mqq.cif', type='file')
        self.utility.setLog(self.data_dir_path + '24642_2mqq-str2str-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

        self.utility.setSource(self.data_dir_path + '24642_2mqq-clean.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2mqq.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '24642_2mqq-str2str-consistency-log.json', type='file')
        self.utility.setLog(self.data_dir_path + '24642-str2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '24642_2mqq-clean-next.str')
        self.utility.addOutput(name='entry_id', value='2mqq', type='param')
        self.utility.addOutput(name='insert_entry_id_to_loops', value=True, type='param')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str2str-deposit')

    def test_nmr_str2str_deposit_chem_shift_ref(self):
        self.utility.setSource(self.data_dir_path + '2la6-chem-shift-ref.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2la6.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2la6-chem-shift-ref-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

        self.utility.setSource(self.data_dir_path + '2la6-chem-shift-ref.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2la6.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2la6-chem-shift-ref-consistency-log.json', type='file')
        self.utility.setLog(self.data_dir_path + '2la6-chem-shift-ref-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2la6-chem-shift-ref-next.str')
        self.utility.addOutput(name='entry_id', value='2la6', type='param')
        self.utility.addOutput(name='insert_entry_id_to_loops', value=True, type='param')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str2str-deposit')

    def test_nmr_str_consistency_check_review(self):
        self.utility.setSource(self.data_dir_path + 'D_800107_nmr-data-str-review_P1.str.V20.rev')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + 'D_800107_model_P1.cif.V3', type='file')
        self.utility.setLog(self.data_dir_path + 'D_800107_nmr-data-str-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

        # pynmrstar.Entry.from_file(self.data_dir_path + 'D_800107_nmr-data-str-review_P1.str.V20.rev')

    def test_nmr_str_consistency_check_daother_5926(self):
        self.utility.setSource(self.data_dir_path + 'swallow_NMR-Star_3-1.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + 'D_800365_model_P1.cif.V4', type='file')
        self.utility.addInput(name='nonblk_anomalous_cs', value=True, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.setLog(self.data_dir_path + 'daother-5926-str-consistency-log.json')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str-consistency-check')

    def test_nmr_str2str_deposit_daother_5926(self):
        if not os.access(self.data_dir_path + 'daother-5926-str-consistency-log.json', os.F_OK):
            self.test_nmr_str_consistency_check_daother_5926()

        self.utility.setSource(self.data_dir_path + 'swallow_NMR-Star_3-1.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + 'D_800365_model_P1.cif.V4', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + 'daother-5926-str-consistency-log.json', type='file')
        self.utility.addInput(name='nonblk_anomalous_cs', value=True, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.setLog(self.data_dir_path + 'daother-5926-str2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + 'swallow_NMR-Star_3-1-next.str')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str2str-deposit')


if __name__ == '__main__':
    unittest.main()
