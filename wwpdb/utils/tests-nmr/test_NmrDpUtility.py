import unittest
import os
import sys

from wwpdb.utils.nmr.NmrDpUtility import NmrDpUtility
from wwpdb.utils.nmr.NmrDpReport import NmrDpReport, NmrDpReportInputSource, NmrDpReportSequenceAlignment, NmrDpReportError, NmrDpReportWarning
from testfixtures import LogCapture

class TestNmrDpUtility(unittest.TestCase):

    def setUp(self):
        here = os.path.abspath(os.path.dirname(__file__))
        self.utility = NmrDpUtility()
        self.data_dir_path = os.path.join(here, '../nmr/NEFTranslator/data/')
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

    def test_nmr_star_consistency_check(self):
        # no input
        with LogCapture() as logs:
            with self.assertRaises(ValueError):
                self.utility.op('nmr-str-consistency-check')

        with LogCapture() as logs:
            with self.assertRaises(IOError):
                self.utility.setSource('dummydummy')

        self.utility.setSource(self.data_dir_path + '2l9r.str')

        # invalid workflow operation
        with LogCapture() as logs:
            with self.assertRaises(KeyError):
                self.utility.op('nmr')

        self.utility.setLog(self.data_dir_path + '2l9r-str-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

    def test_nmr_nef_consistency_check_non_std_residue(self):
        self.utility.setSource(self.data_dir_path + '2l9rnonstandard.nef')
        self.utility.setLog(self.data_dir_path + '2l9rnonstandard-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_nef2str_deposit_check(self):
        self.utility.setSource(self.data_dir_path + '2l9r.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2l9r.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2l9r-nef-consistency-log.json', type='file')
        self.utility.setLog(self.data_dir_path + '2l9r-nef2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2l9r-next.nef')

        self.utility.op('nmr-nef2str-deposit')

if __name__ == '__main__':
    unittest.main()
