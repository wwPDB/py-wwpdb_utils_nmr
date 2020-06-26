##
# File: test_nef_str_consist_chk.py
# Date:  29-Apr-2020  M. Yokochi
#
# Updates:
##
import unittest
import os
import sys
import json

from wwpdb.utils.nmr.NmrDpUtility import NmrDpUtility
from wwpdb.utils.nmr.NmrDpReport import NmrDpReport, NmrDpReportInputSource, NmrDpReportSequenceAlignment, NmrDpReportError, NmrDpReportWarning
from testfixtures import LogCapture

class TestNmrDpUtility(unittest.TestCase):

    def setUp(self):
        here = os.path.abspath(os.path.dirname(__file__))
        self.data_dir_path = os.path.join(here, 'mock-data-daother-5621/')
        self.nef_data_file_path = {'1pqx': {'nef': '1pqx.nef',
                                            'cif': '1pqx.cif'}}
        self.str_data_file_path = {'1pqx': {'str': '1pqx.str',
                                            'cif': '1pqx.cif'}}
        self.utility = NmrDpUtility()
        self.report = NmrDpReport()
        pass

    def tearDown(self):
        pass

    def __test_nmr_nef_consistency(self, entry_id):
        self.utility.setSource(self.data_dir_path + self.nef_data_file_path[entry_id]['nef'])
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + self.nef_data_file_path[entry_id]['cif'], type='file')
        self.utility.addInput(name='nonblk_anomalous_cs', value=True, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.setLog(self.data_dir_path + entry_id + '-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

        with open(self.data_dir_path + entry_id + '-nef-consistency-log.json', 'r') as file:
            report = json.loads(file.read())

        if not report['error'] is None:
            self.assertEqual(report['error']['internal_error'], None)

        self.assertEqual(report['warning']['anomalous_chemical_shift'], None)

    def __test_nmr_str_consistency(self, entry_id):
        self.utility.setSource(self.data_dir_path + self.str_data_file_path[entry_id]['str'])
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + self.str_data_file_path[entry_id]['cif'], type='file')
        self.utility.addInput(name='nonblk_anomalous_cs', value=True, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.setLog(self.data_dir_path + entry_id + '-str-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

        with open(self.data_dir_path + entry_id + '-str-consistency-log.json', 'r') as file:
            report = json.loads(file.read())

        if not report['error'] is None:
            self.assertEqual(report['error']['internal_error'], None)

    def test_nmr_nef_consistency_check_1pqx(self):
        self.__test_nmr_nef_consistency('1pqx')

    def test_nmr_str_consistency_check_1pqx(self):
        self.__test_nmr_str_consistency('1pqx')

if __name__ == '__main__':
    unittest.main()
