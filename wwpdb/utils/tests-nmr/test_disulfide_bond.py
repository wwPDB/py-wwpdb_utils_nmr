##
# File: test_disulfide_bond.py
# Date:  25-Jun-2020  M. Yokochi
#
# Updates:
##
import unittest
import os
import json

from wwpdb.utils.nmr.NmrDpUtility import NmrDpUtility
from wwpdb.utils.nmr.NmrDpReport import NmrDpReport


class TestNmrDpUtility(unittest.TestCase):

    def setUp(self):
        here = os.path.abspath(os.path.dirname(__file__))
        self.data_dir_path = os.path.join(here, 'NMR-VTF/PDBStat_it2/')
        self.utility = NmrDpUtility()
        self.report = NmrDpReport()
        pass

    def tearDown(self):
        pass

    def __test_nmr_nef_consistency(self, entry_id):
        self.utility.setSource(self.data_dir_path + entry_id + '/' + entry_id + '-disulfide-bond.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + entry_id + '/' + entry_id + '.cif', type='file')
        self.utility.addInput(name='nonblk_anomalous_cs', value=True, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.setLog(self.data_dir_path + entry_id + '-disulfide-bond-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

        with open(self.data_dir_path + entry_id + '-disulfide-bond-nef-consistency-log.json', 'r') as file:
            report = json.loads(file.read())

        if not report['error'] is None:
            self.assertNotIn('internal_error', report['error'])

        if report['error'] is None:
            print('%s: %s' % (entry_id, report['information']['status']))
        elif 'format_issue' in report['error']:
            print('%s: %s\n format_issue: %s' % (entry_id, report['information']['status'], report['error']['format_issue'][0]['description']))
        elif 'missing_mandatory_content' in report['error']:
            print('%s: %s\n missing_mandatory_content: %s' % (entry_id, report['information']['status'], report['error']['missing_mandatory_content'][0]['description']))
        else:
            error_type = {str(k): len(v) for k, v in report['error'].items() if str(k) != 'total'}
            print('%s: %s, %s' % (entry_id, report['information']['status'], error_type))

    def __test_nmr_nef2str_deposit(self, entry_id):
        # if not os.access(self.data_dir_path + entry_id + '-nef-consistency-log.json', os.F_OK):
        self.__test_nmr_nef_consistency(entry_id)

        self.utility.setSource(self.data_dir_path + entry_id + '/' + entry_id + '-disulfide-bond.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + entry_id + '/' + entry_id + '.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + entry_id + '-disulfide-bond-nef-consistency-log.json', type='file')
        self.utility.addInput(name='nonblk_anomalous_cs', value=True, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.setLog(self.data_dir_path + entry_id + '-disulfide-bond-nef2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + entry_id + '-disulfide-bond-next.nef')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + entry_id + '-disulfide-bond-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + entry_id + '-disulfide-bond-nef2str-str-deposit-log.json', type='file')
        self.utility.addOutput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef2str-deposit')

        with open(self.data_dir_path + entry_id + '-disulfide-bond-nef2str-str-deposit-log.json', 'r') as file:
            report = json.loads(file.read())

        if not report['error'] is None:
            self.assertNotIn('internal_error', report['error'])

    def __test_nmr_str_consistency(self, entry_id):
        # if not os.access(self.data_dir_path + entry_id + '-disulfide-bond-nef2str.str', os.F_OK):
        self.__test_nmr_nef2str_deposit(entry_id)

        self.utility.setSource(self.data_dir_path + entry_id + '-disulfide-bond-nef2str.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + entry_id + '/' + entry_id + '.cif', type='file')
        self.utility.addInput(name='nonblk_anomalous_cs', value=True, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.setLog(self.data_dir_path + entry_id + '-disulfide-bond-str2nef-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

        with open(self.data_dir_path + entry_id + '-disulfide-bond-str2nef-consistency-log.json', 'r') as file:
            report = json.loads(file.read())

        if report['error'] is None:
            print('%s: %s' % (entry_id, report['information']['status']))
        elif 'format_issue' in report['error']:
            print('%s: %s\n format_issue: %s' % (entry_id, report['information']['status'], report['error']['format_issue'][0]['description']))
        elif 'missing_mandatory_content' in report['error']:
            print('%s: %s\n missing_mandatory_content: %s' % (entry_id, report['information']['status'], report['error']['missing_mandatory_content'][0]['description']))
        else:
            error_type = {str(k): len(v) for k, v in report['error'].items() if str(k) != 'total'}
            print('%s: %s, %s' % (entry_id, report['information']['status'], error_type))

    def __test_nmr_str2nef_release(self, entry_id):
        # if not os.access(self.data_dir_path + entry_id + '-disulfide-bond-str2nef-consistency-log.json', os.F_OK):
        self.__test_nmr_str_consistency(entry_id)

        self.utility.setSource(self.data_dir_path + entry_id + '-disulfide-bond-nef2str.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + entry_id + '/' + entry_id + '.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + entry_id + '-disulfide-bond-str2nef-consistency-log.json', type='file')
        self.utility.addInput(name='nonblk_anomalous_cs', value=True, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.setLog(self.data_dir_path + entry_id + '-disulfide-bond-str2nef-release-log.json')
        self.utility.setDestination(self.data_dir_path + entry_id + '-disulfide-bond-str2nef-next.str')
        self.utility.addOutput(name='nef_file_path', value=self.data_dir_path + entry_id + '-disulfide-bond-str2nef.nef', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + entry_id + '-disulfide-bond-str2nef-nef-release-log.json', type='file')
        self.utility.addOutput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str2nef-release')

        with open(self.data_dir_path + entry_id + '-disulfide-bond-str2nef-nef-release-log.json', 'r') as file:
            report = json.loads(file.read())

        if not report['error'] is None:
            self.assertNotIn('internal_error', report['error'])

        if report['error'] is None:
            print('%s: %s' % (entry_id, report['information']['status']))
        elif 'format_issue' in report['error']:
            print('%s: %s\n format_issue: %s' % (entry_id, report['information']['status'], report['error']['format_issue'][0]['description']))
        elif 'missing_mandatory_content' in report['error']:
            print('%s: %s\n missing_mandatory_content: %s' % (entry_id, report['information']['status'], report['error']['missing_mandatory_content'][0]['description']))
        else:
            error_type = {str(k): len(v) for k, v in report['error'].items() if str(k) != 'total'}
            print('%s: %s, %s' % (entry_id, report['information']['status'], error_type))

    def test_nmr_nef2str_deposit_6nbn(self):
        self.__test_nmr_nef2str_deposit('6nbn')

    def test_nmr_str2nef_release_6nbn(self):
        self.__test_nmr_str2nef_release('6nbn')


if __name__ == '__main__':
    unittest.main()
