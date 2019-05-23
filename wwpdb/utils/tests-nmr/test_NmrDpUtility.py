import unittest
import os
import sys
import logging
import json

from wwpdb.utils.nmr.NmrDpUtility import NmrDpUtility
from wwpdb.utils.nmr.NmrDpReport import NmrDpReport, NmrDpReportInputSource, NmrDpReportSequenceAlignment, NmrDpReportError, NmrDpReportWarning
from testfixtures import LogCapture

logger = logging.getLogger('')

class TestNmrDpUtility(unittest.TestCase):

    def setUp(self):
        self.utility = NmrDpUtility()
        self.data_dir_path = '../nmr/NEFTranslator/data/'
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
        self.assertEqual(nmr_content_subtypes, set(input_source.content_subtypes) - {'coordinate'})

        # data directory exists
        self.assertEqual(os.path.isdir(self.data_dir_path), True)

    def test_nmr_nef_parser_check(self):
        # no input
        with LogCapture() as logs:
            with self.assertRaises(ValueError):
                self.utility.op('nmr-nef-parser-check')

        with LogCapture() as logs:
            with self.assertRaises(IOError):
                self.utility.setSource('dummydummy')

        self.utility.setSource(self.data_dir_path + '2l9r.nef')

        # invalid workflow operation
        with LogCapture() as logs:
            with self.assertRaises(KeyError):
                self.utility.op('nmr')

        self.utility.op('nmr-nef-parser-check')

        print(self.utility.report.getJson())

    def test_nmr_star_parser_check(self):
        # no input
        with LogCapture() as logs:
            with self.assertRaises(ValueError):
                self.utility.op('nmr-star-parser-check')

        with LogCapture() as logs:
            with self.assertRaises(IOError):
                self.utility.setSource('dummydummy')

        self.utility.setSource(self.data_dir_path + '2l9r.str')

        # invalid workflow operation
        with LogCapture() as logs:
            with self.assertRaises(KeyError):
                self.utility.op('nmr')

        self.utility.op('nmr-star-parser-check')

        #print(self.utility.report.getJson())

    def test_nmr_nef_parser_check_non_std_residue(self):
        self.utility.setSource(self.data_dir_path + '2l9rnonstandard.nef')

        self.utility.op('nmr-nef-parser-check')

        #print(self.utility.report.getJson())

if __name__ == '__main__':
    unittest.main()
