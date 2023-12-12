##
# File: test_daother_8448.py
# Date:  12-Apr-2023  M. Yokochi
#
# Updates:
#
import unittest
import os
import json
from shutil import copyfile

try:
    from wwpdb.utils.nmr.NmrDpUtility import NmrDpUtility
except ImportError:
    from nmr.NmrDpUtility import NmrDpUtility


class TestNmrDpUtility(unittest.TestCase):

    def setUp(self):
        here = os.path.abspath(os.path.dirname(__file__))
        self.data_dir_path = os.path.join(here, 'mock-data-daother-8448/')
        self.cs_file_path = {
            'daother-8448': 'D_1000273709_cs_P1.str',
            'daother-8448-rev': 'D_1000273709_cs_P1_rev.str'
        }
        self.mr_file_path = {
            'daother-8448': ['D_1000273709_mr_P1.dat'],
            'daother-8448-rev': ['D_1000273709_mr_P1_rev.dat']
        }
        self.model_file_path = {
            'daother-8448': 'D_1000273709_model_P1.cif',
            'daother-8448-rev': 'D_1000273709_model_P1.cif'
        }
        self.utility = NmrDpUtility()

    def tearDown(self):
        pass

    def __test_nmr_cs_mr_merge(self, entry_id):

        print(entry_id)

        report_file = self.data_dir_path + entry_id + '-cs-mr-merged.json'

        cs_file = self.data_dir_path + self.cs_file_path[entry_id]
        if os.path.exists(cs_file + '.bk'):
            copyfile(cs_file + '.bk', cs_file)
        self.utility.addInput(name='chem_shift_file_path_list', value=[cs_file], type='file_list')

        cif_file = self.data_dir_path + self.model_file_path[entry_id]
        self.utility.addInput(name='coordinate_file_path', value=cif_file, type='file')

        mr_path_list = []
        for mr_path in self.mr_file_path[entry_id]:
            mr_path_list.append(self.data_dir_path + mr_path)

        self.utility.addInput(name='restraint_file_path_list',
                              value=mr_path_list,
                              type='file_list')

        self.utility.addInput(name='nonblk_anomalous_cs', value=False, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.addInput(name="merge_any_pk_as_is", value=True, type="param")
        self.utility.setDestination(self.data_dir_path + entry_id + '_cs_mr_merged.str')
        self.utility.setLog(report_file)
        self.utility.setVerbose(False)
        self.utility.setMrDebugMode(False)

        self.utility.op('nmr-cs-mr-merge')

        with open(report_file, 'r') as file:
            report = json.loads(file.read())

        if not report['error'] is None:
            self.assertNotIn('internal_error', report['error'])

        if entry_id == 'daother-8448':
            self.assertNotEqual(report['error'], None)
        elif entry_id == 'daother-8448-rev':
            self.assertEqual(report['error'], None)

        if report['error'] is None:
            print('========>>>> %s: %s' % (entry_id, report['information']['status']))
        elif 'format_issue' in report['error']:
            print('========>>>> %s: %s\n format_issue: %s' % (entry_id, report['information']['status'], report['error']['format_issue'][0]['description']))
        elif 'missing_mandatory_content' in report['error']:
            print('========>>>> %s: %s\n missing_mandatory_content: %s' % (entry_id, report['information']['status'], report['error']['missing_mandatory_content'][0]['description']))
        else:
            error_type = {str(k): len(v) for k, v in report['error'].items() if str(k) != 'total'}
            print('========>>>> %s: %s, %s' % (entry_id, report['information']['status'], error_type))

        if os.path.exists(self.data_dir_path + entry_id + '_cs_mr_merged.str'):
            self.__test_nmr_str2str_deposit(entry_id)

    def __test_nmr_str_consistency(self, entry_id):
        cif_file = self.data_dir_path + self.model_file_path[entry_id]
        self.utility.addInput(name='coordinate_file_path', value=cif_file, type='file')

        self.utility.setSource(self.data_dir_path + entry_id + '_cs_mr_merged.str')
        self.utility.addInput(name='nonblk_anomalous_cs', value=False, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.addInput(name='remediation', value=True, type='param')
        self.utility.setLog(self.data_dir_path + entry_id + '-str-consistency-log.json')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str-consistency-check')

        with open(self.data_dir_path + entry_id + '-str-consistency-log.json', 'r') as file:
            report = json.loads(file.read())

        if report['error'] is not None:
            self.assertNotIn('internal_error', report['error'])

        if report['error'] is None:
            print('%s: %s' % (entry_id, report['information']['status']))
        elif 'format_issue' in report['error']:
            print('%s: %s\n format_issue: %s' % (entry_id, report['information']['status'], report['error']['format_issue'][0]['description']))
        elif 'missing_mandatory_content' in report['error']:
            print('%s: %s\n missing_mandatory_content: %s' % (entry_id, report['information']['status'], report['error']['missing_mandatory_content'][0]['description']))
        else:
            error_type = {str(k): len(v) for k, v in report['error'].items() if v is not None and str(k) != 'total'}
            print('%s: %s, %s' % (entry_id.lower(), report['information']['status'], error_type))

    def __test_nmr_str2str_deposit(self, entry_id):
        if not os.access(self.data_dir_path + entry_id + '-str-consistency-log.json', os.F_OK):
            self.__test_nmr_str_consistency(entry_id)

        cif_file = self.data_dir_path + self.model_file_path[entry_id]
        self.utility.addInput(name='coordinate_file_path', value=cif_file, type='file')

        self.utility.setSource(self.data_dir_path + entry_id + '_cs_mr_merged.str')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + entry_id + '-str-consistency-log.json', type='file')
        self.utility.addInput(name='nonblk_anomalous_cs', value=False, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.addInput(name='remediation', value=True, type='param')
        self.utility.setLog(self.data_dir_path + entry_id + '-str2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + entry_id + '_nmr_data.str')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str2str-deposit')

        with open(self.data_dir_path + entry_id + '-str2str-deposit-log.json', 'r') as file:
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
            error_type = {str(k): len(v) for k, v in report['error'].items() if v is not None and str(k) != 'total'}
            print('%s: %s, %s' % (entry_id.lower(), report['information']['status'], error_type))

    def test_nmr_cs_mr_merge_daother_8448(self):
        self.__test_nmr_cs_mr_merge('daother-8448')

    def test_nmr_cs_mr_merge_daother_8448_rev(self):
        self.__test_nmr_cs_mr_merge('daother-8448-rev')


if __name__ == '__main__':
    unittest.main()
