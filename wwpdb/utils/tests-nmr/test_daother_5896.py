##
# File: test_daother_5896.py
# Date:  30-Jun-2020  M. Yokochi
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
        self.data_dir_path = os.path.join(here, 'mock-data-daother-5896/')
        self.data_file_path = {'1pqx': {'nef': '1pqx_ccpn_modified.nef',
                                        'cif': '1pqx.cif'},
                               'penta_a': {'nef': 'penta__eT_spDi_a_modified.nef',
                                           'cif': 'penta_a_modified.cif'},
                               'penta_b': {'nef': 'penta__eT_spDi_b_modified.nef',
                                           'cif': 'penta_b_modified.cif'}
                              }
        self.utility = NmrDpUtility()
        self.report = NmrDpReport()
        pass

    def tearDown(self):
        pass

    def __test_nmr_nef_consistency(self, entry_id):
        self.utility.setSource(self.data_dir_path + self.data_file_path[entry_id]['nef'])
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + self.data_file_path[entry_id]['cif'], type='file')
        self.utility.addInput(name='nonblk_anomalous_cs', value=True, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.setLog(self.data_dir_path + entry_id + '-nef-consistency-log.json')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef-consistency-check')

        with open(self.data_dir_path + entry_id + '-nef-consistency-log.json', 'r') as file:
            report = json.loads(file.read())

        if not report['error'] is None:
            self.assertEqual(report['error']['internal_error'], None)

        if report['error'] is None:
            print('%s: %s' % (entry_id, report['information']['status']))
        elif not report['error']['format_issue'] is None:
            print('%s: %s\n format_issue: %s' % (entry_id, report['information']['status'], report['error']['format_issue'][0]['description']))
        elif not report['error']['missing_mandatory_content'] is None:
            print('%s: %s\n missing_mandatory_content: %s' % (entry_id, report['information']['status'], report['error']['missing_mandatory_content'][0]['description']))
        else:
            error_type = {str(k): len(v) for k, v in report['error'].items() if not v is None and str(k) != 'total'}
            print('%s: %s, %s' % (entry_id, report['information']['status'], error_type))

    def __test_nmr_nef2str_deposit(self, entry_id):
        if not os.access(self.data_dir_path + entry_id + '-nef-consistency-log.json', os.F_OK):
            self.__test_nmr_nef_consistency(entry_id)

        self.utility.setSource(self.data_dir_path + self.data_file_path[entry_id]['nef'])
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + self.data_file_path[entry_id]['cif'], type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + entry_id + '-nef-consistency-log.json', type='file')
        self.utility.addInput(name='nonblk_anomalous_cs', value=True, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.setLog(self.data_dir_path + entry_id + '-nef2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + entry_id + '-next.nef')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + entry_id + '-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + entry_id + '-nef2str-str-deposit-log.json', type='file')
        self.utility.addOutput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef2str-deposit')

        with open(self.data_dir_path + entry_id + '-nef2str-str-deposit-log.json', 'r') as file:
            report = json.loads(file.read())

        if not report['error'] is None:
            self.assertEqual(report['error']['internal_error'], None)

    def __test_nmr_str_consistency(self, entry_id):
        if not os.access(self.data_dir_path + entry_id + '-nef2str.str', os.F_OK):
            self.__test_nmr_nef2str_deposit(entry_id)

        self.utility.setSource(self.data_dir_path + entry_id + '-nef2str.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + self.data_file_path[entry_id]['cif'], type='file')
        self.utility.addInput(name='nonblk_anomalous_cs', value=True, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.setLog(self.data_dir_path + entry_id + '-str2nef-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

        with open(self.data_dir_path + entry_id + '-str2nef-consistency-log.json', 'r') as file:
            report = json.loads(file.read())

        if report['error'] is None:
            print('%s: %s' % (entry_id, report['information']['status']))
        elif not report['error']['format_issue'] is None:
            print('%s: %s\n format_issue: %s' % (entry_id, report['information']['status'], report['error']['format_issue'][0]['description']))
        elif not report['error']['missing_mandatory_content'] is None:
            print('%s: %s\n missing_mandatory_content: %s' % (entry_id, report['information']['status'], report['error']['missing_mandatory_content'][0]['description']))
        else:
            error_type = {str(k): len(v) for k, v in report['error'].items() if not v is None and str(k) != 'total'}
            print('%s: %s, %s' % (entry_id.lower(), report['information']['status'], error_type))

    def __test_nmr_str2nef_release(self, entry_id):
        if not os.access(self.data_dir_path + entry_id + '-str2nef-consistency-log.json', os.F_OK):
            self.__test_nmr_str_consistency(entry_id)

        self.utility.setSource(self.data_dir_path + entry_id + '-nef2str.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + self.data_file_path[entry_id]['cif'], type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + entry_id + '-str2nef-consistency-log.json', type='file')
        self.utility.addInput(name='nonblk_anomalous_cs', value=True, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.setLog(self.data_dir_path + entry_id + '-str2nef-release-log.json')
        self.utility.setDestination(self.data_dir_path + entry_id + '-str2nef-next.str')
        self.utility.addOutput(name='nef_file_path', value=self.data_dir_path + entry_id + '-str2nef.nef', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + entry_id + '-str2nef-nef-release-log.json', type='file')
        self.utility.addOutput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str2nef-release')

        with open(self.data_dir_path + entry_id + '-str2nef-nef-release-log.json', 'r') as file:
            report = json.loads(file.read())

        if not report['error'] is None:
            self.assertEqual(report['error']['internal_error'], None)

        if report['error'] is None:
            print('%s: %s' % (entry_id, report['information']['status']))
        elif not report['error']['format_issue'] is None:
            print('%s: %s\n format_issue: %s' % (entry_id, report['information']['status'], report['error']['format_issue'][0]['description']))
        elif not report['error']['missing_mandatory_content'] is None:
            print('%s: %s\n missing_mandatory_content: %s' % (entry_id, report['information']['status'], report['error']['missing_mandatory_content'][0]['description']))
        else:
            error_type = {str(k): len(v) for k, v in report['error'].items() if not v is None and str(k) != 'total'}
            print('%s: %s, %s' % (entry_id, report['information']['status'], error_type))

    def test_nmr_nef_consistency_check_1pqx(self):
        self.__test_nmr_nef_consistency('1pqx')

    def test_nmr_nef_consistency_check_penta_a(self):
        self.__test_nmr_nef_consistency('penta_a')

    def test_nmr_nef_consistency_check_penta_b(self):
        self.__test_nmr_nef_consistency('penta_b')

    def test_nmr_nef2str_deposit_1pqx(self):
        self.__test_nmr_nef2str_deposit('1pqx')

    def test_nmr_nef2str_deposit_penta_a(self):
        self.__test_nmr_nef2str_deposit('penta_a')

    def test_nmr_nef2str_deposit_penta_b(self):
        self.__test_nmr_nef2str_deposit('penta_b')

    def test_nmr_nef2str_release_penta_b(self):
        self.__test_nmr_str2nef_release('penta_b')

if __name__ == '__main__':
    unittest.main()
