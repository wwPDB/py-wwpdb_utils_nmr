##
# File: test_NmrDpUtility.py
# Date:  28-Aug-2019  M. Yokochi
#
# Updates:
##
import unittest
import os
import sys

from wwpdb.utils.nmr.NmrDpUtility import NmrDpUtility
from wwpdb.utils.nmr.NmrDpReport import NmrDpReport, NmrDpReportInputSource, NmrDpReportSequenceAlignment, NmrDpReportError, NmrDpReportWarning
from testfixtures import LogCapture

class TestNmrDpUtility(unittest.TestCase):

    def setUp(self):
        here = os.path.abspath(os.path.dirname(__file__))
        self.data_dir_path = os.path.join(here, '../nmr/NEFTranslator/data/')
        self.utility = NmrDpUtility()
        pass

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
        self.assertEqual(nmr_content_subtypes, set(input_source.content_subtypes) - {'coordinate', 'non_poly'})

        # data directory exists
        self.assertEqual(os.path.isdir(self.data_dir_path), True)

    def test_nmr_nef_consistency_check(self):
        # no input
        with LogCapture() as logs:
            with self.assertRaises(ValueError):
                self.utility.op('nmr-nef-consistency-check')

        with LogCapture() as logs:
            with self.assertRaises(IOError):
                self.utility.setSource('dummydummy')

        self.utility.setSource(self.data_dir_path + '2l9r.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2l9r.cif', type='file')

        # invalid workflow operation
        with LogCapture() as logs:
            with self.assertRaises(KeyError):
                self.utility.op('nmr')

        self.utility.setLog(self.data_dir_path + '2l9r-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_str_consistency_check(self):
        # no input
        with LogCapture() as logs:
            with self.assertRaises(ValueError):
                self.utility.op('nmr-str-consistency-check')

        with LogCapture() as logs:
            with self.assertRaises(IOError):
                self.utility.setSource('dummydummy')

        self.utility.setSource(self.data_dir_path + '2l9r.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2l9r.cif', type='file')

        # invalid workflow operation
        with LogCapture() as logs:
            with self.assertRaises(KeyError):
                self.utility.op('nmr')

        self.utility.setLog(self.data_dir_path + '2l9r-str-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

    def test_translated_nmr_star_consistency_check(self):
        self.utility.setSource(self.data_dir_path + '2l9r-nef2str.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2l9r.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2l9r-nef2str-str-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

    def test_nmr_nef_consistency_check_non_std_residue(self):
        self.utility.setSource(self.data_dir_path + '2l9rnonstandard.nef')
        self.utility.setLog(self.data_dir_path + '2l9rnonstandard-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_nef_consistency_check_former_nef(self):
        self.utility.setSource(self.data_dir_path + '2l9rold.nef')
        self.utility.setLog(self.data_dir_path + '2l9rold-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_nef_consistency_check_cys(self):
        self.utility.setSource(self.data_dir_path + '2l9r-cys.nef')
        self.utility.setLog(self.data_dir_path + '2l9r-cys-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_str_consistency_check_bmrb_merged(self):
        self.utility.setSource(self.data_dir_path + 'merged_30562_6nox.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '6nox.cif', type='file')
        self.utility.setLog(self.data_dir_path + 'merged_30562_6nox-str-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

    def test_nmr_nef2str_deposit_str(self):
        self.utility.setSource(self.data_dir_path + '2l9r.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2l9r.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2l9r-nef2str-str-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

        self.utility.setSource(self.data_dir_path + '2l9r.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2l9r.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2l9r-nef2str-str-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='2l9r', type='param')
        self.utility.addInput(name='insert_entry_id_to_loops', value=True, type='param')
        self.utility.setLog(self.data_dir_path + '2l9r-nef2str-str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2l9r-nef2str-str.str')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2l9r-nef2str-str-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2l9r-nef2str-str-str-deposit-log.json', type='file')
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
        self.utility.addInput(name='entry_id', value='2l9r', type='param')
        self.utility.addInput(name='insert_entry_id_to_loops', value=True, type='param')
        self.utility.setLog(self.data_dir_path + '2l9r-str2str-nef-deposit-log.json')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str2str-deposit')

    def test_nmr_nef2str_deposit_check(self):
        if not os.access(self.data_dir_path + '2l9r-nef-consistency-log.json', os.F_OK):
            self.test_nmr_nef_consistency_check()

        self.utility.setSource(self.data_dir_path + '2l9r.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2l9r.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2l9r-nef-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2l9r-nef2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2l9r-next.nef')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2l9r-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2l9r-nef2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef2str-deposit')

    def test_nmr_nef2str_deposit_check_cys(self):
        if not os.access(self.data_dir_path + '2l9r-cys-nef-consistency-log.json', os.F_OK):
            self.test_nmr_nef_consistency_check_cys()

        self.utility.setSource(self.data_dir_path + '2l9r-cys.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2l9r-cys.cif', type='file')
        self.utility.addInput(name='report_file_path',value=self.data_dir_path + '2l9r-cys-nef-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2l9r-cys-nef2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2l9r-cys-next.nef')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2l9r-cys-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2l9r-cys-nef2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef2str-deposit')

    def test_nmr_str2str_deposit_check(self):
        if not os.access(self.data_dir_path + '2l9r-str-consistency-log.json', os.F_OK):
            self.test_nmr_str_consistency_check()

        self.utility.setSource(self.data_dir_path + '2l9r.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2l9r.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2l9r-str-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='2l9r', type='param')
        self.utility.addInput(name='insert_entry_id_to_loops', value=True, type='param')
        self.utility.setLog(self.data_dir_path + '2l9r-str2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2l9r-next.str')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str2str-deposit')

    def test_nmr_nef2str_deposit_check_non_std_residue(self):
        if not os.access(self.data_dir_path + '2l9rnonstandard-nef-consistency-log.json', os.F_OK):
            self.test_nmr_nef_consistency_check_non_std_residue()

        self.utility.setSource(self.data_dir_path + '2l9rnonstandard.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2l9r.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2l9rnonstandard-nef-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2l9rnonstandard-nef2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2l9rnonstandard-next.nef')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2l9rnonstandard-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2l9rnonstandard-nef2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef2str-deposit')

if __name__ == '__main__':
    unittest.main()
