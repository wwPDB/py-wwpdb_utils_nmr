##
# File: test_daother_8817_ann_next.py
# Date:  05-Apr-2024  M. Yokochi
#
# Updates:
#
import unittest
import os
import json

try:
    from wwpdb.utils.nmr.NmrDpUtility import NmrDpUtility
except ImportError:
    from nmr.NmrDpUtility import NmrDpUtility


class TestNmrDpUtility(unittest.TestCase):

    def setUp(self):
        here = os.path.abspath(os.path.dirname(__file__))
        self.data_dir_path = os.path.join(here, 'mock-data-daother-8817/')
        self.data_file_path = {'daother-8817-ann-4th': {'str': 'D_800677_nmr-data-str_P1.str',
                                                        'cif': 'D_8000212514_model_P1.cif.V5'},
                               'daother-8817-ann-5th': {'str': 'D_800677_nmr-data-str_P1.str',
                                                        'cif': 'D_8000212514_model_P1.cif.V2'},
                               'daother-8817-ann-7th': {'str': 'daother-8817-ann-7th-next.str',
                                                        'cif': 'D_8000212922_model_P1.cif.V5'}
                               }
        self.utility = NmrDpUtility()

    def tearDown(self):
        pass

    def __test_nmr_str_consistency(self, entry_id):
        entry_dir = self.data_dir_path

        cif_file = entry_dir + self.data_file_path[entry_id]['cif']
        self.utility.addInput(name='coordinate_file_path', value=cif_file, type='file')

        self.utility.setSource(entry_dir + self.data_file_path[entry_id]['str'])
        self.utility.addInput(name='nonblk_anomalous_cs', value=False, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.addInput(name='remediation', value=True, type='param')
        self.utility.setLog(entry_dir + entry_id + '-str-consistency-log.json')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str-consistency-check')

        with open(entry_dir + entry_id + '-str-consistency-log.json', 'r') as file:
            report = json.loads(file.read())

        if report['error'] is not None:
            self.assertNotIn('internal_error', report['error'])

        self.assertIsNone(report['error'])

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
        entry_dir = self.data_dir_path

        if not os.access(entry_dir + entry_id + '-str-consistency-log.json', os.F_OK):
            self.__test_nmr_str_consistency(entry_id)

        cif_file = entry_dir + self.data_file_path[entry_id]['cif']
        self.utility.addInput(name='coordinate_file_path', value=cif_file, type='file')

        print(f'model file: {cif_file}')
        print(f'nmr   file: {entry_dir}{self.data_file_path[entry_id]["str"]}')
        self.utility.setSource(entry_dir + self.data_file_path[entry_id]['str'])
        self.utility.addInput(name='report_file_path', value=entry_dir + entry_id + '-str-consistency-log.json', type='file')
        self.utility.addInput(name='nonblk_anomalous_cs', value=False, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.addInput(name='remediation', value=True, type='param')
        self.utility.setLog(entry_dir + entry_id + '-str2str-deposit-log.json')
        self.utility.setDestination(entry_dir + entry_id + '_nmr_data.str')
        print(f' Generated {entry_dir}{entry_id}_nmr_data.str')

        self.utility.addOutput(name='nmr_cif_file_path', value=entry_dir + entry_id + '_nmr_data.cif', type='file')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str2cif-deposit')

        with open(entry_dir + entry_id + '-str2str-deposit-log.json', 'r') as file:
            report = json.loads(file.read())

        if report['error'] is not None:
            self.assertNotIn('internal_error', report['error'])

        self.assertIsNone(report['error'])

        if report['error'] is None:
            print('%s: %s' % (entry_id, report['information']['status']))
        elif 'format_issue' in report['error']:
            print('%s: %s\n format_issue: %s' % (entry_id, report['information']['status'], report['error']['format_issue'][0]['description']))
        elif 'missing_mandatory_content' in report['error']:
            print('%s: %s\n missing_mandatory_content: %s' % (entry_id, report['information']['status'], report['error']['missing_mandatory_content'][0]['description']))
        else:
            error_type = {str(k): len(v) for k, v in report['error'].items() if v is not None and str(k) != 'total'}
            print('%s: %s, %s' % (entry_id.lower(), report['information']['status'], error_type))

    def test_nmr_str2str_deposit_daother_8817_ann_4th(self):
        self.__test_nmr_str_consistency('daother-8817-ann-4th')
        self.__test_nmr_str2str_deposit('daother-8817-ann-4th')

    def test_nmr_str2str_deposit_daother_8817_ann_5th(self):
        self.__test_nmr_str_consistency('daother-8817-ann-5th')
        self.__test_nmr_str2str_deposit('daother-8817-ann-5th')

    def test_nmr_str2str_deposit_daother_8817_ann_7th(self):
        self.__test_nmr_str_consistency('daother-8817-ann-7th')
        self.__test_nmr_str2str_deposit('daother-8817-ann-7th')


if __name__ == '__main__':
    unittest.main()
