##
# File: test_daother_7465.py
# Date:  15-Nov-2021  M. Yokochi
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
        self.data_dir_path = os.path.join(here, 'mock-data-daother-7465/')
        self.res_file_type = {
            'daother-7465': 'nm-res-cns',
            'daother-7465_2': 'nm-res-oth'
        }
        self.cs_file_path = {
            'daother-7465': ['D_1000251112_cs-upload_P1.str.V1'],
            'daother-7465_2': ['D_1000261119_cs-review_P1.str']
        }
        self.mr_file_path = {
            'daother-7465': ['D_1000251112_mr-upload_P1.cns.V1'],
            'daother-7465_2': ['D_1000261119_mr-upload_P1.dat']
        }
        self.model_file_path = {
            'daother-7465': 'D_800453_model_P1.cif.V1',
            'daother-7465_2': 'D_800461_model_P1.cif.V1'
        }
        self.utility = NmrDpUtility()

    def tearDown(self):
        pass

    def __test_nmr_cs_str_consistency(self, cs_type):
        self.utility.addInput(name='chem_shift_file_path_list', value=[self.data_dir_path + cs_file_path for cs_file_path in self.cs_file_path[cs_type]], type='file_list')
        if len(self.mr_file_path[cs_type]) == 1:
            self.utility.addInput(name='atypical_restraint_file_path_list',
                                  value=[{'file_name': self.data_dir_path + self.mr_file_path[cs_type][0], 'file_type': self.res_file_type[cs_type]}],
                                  type='file_dict_list')
        else:
            ar_path_list = []
            for i, ar_path in enumerate(self.mr_file_path[cs_type]):
                ar_path_list.append({'file_name': self.data_dir_path + ar_path, 'file_type': self.res_file_type[cs_type][i]})
            self.utility.addInput(name='atypical_restraint_file_path_list', value=ar_path_list, type='file_dict_list')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + self.model_file_path[cs_type], type='file')
        self.utility.addInput(name='nonblk_anomalous_cs', value=True, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=False, type='param')
        self.utility.setLog(self.data_dir_path + cs_type + '-cs-str-consistency-log.json')
        self.utility.setVerbose(False)

        self.utility.op('nmr-cs-str-consistency-check')

        with open(self.data_dir_path + cs_type + '-cs-str-consistency-log.json', 'r') as file:
            report = json.loads(file.read())

        if not report['error'] is None:
            self.assertNotIn('internal_error', report['error'])

        if report['error'] is None:
            print('%s: %s' % (cs_type, report['information']['status']))
        elif 'format_issue' in report['error']:
            print('%s: %s\n format_issue: %s' % (cs_type, report['information']['status'], report['error']['format_issue'][0]['description']))
        elif 'missing_mandatory_content' in report['error']:
            print('%s: %s\n missing_mandatory_content: %s' % (cs_type, report['information']['status'], report['error']['missing_mandatory_content'][0]['description']))
        else:
            error_type = {str(k): len(v) for k, v in report['error'].items() if str(k) != 'total'}
            print('%s: %s, %s' % (cs_type, report['information']['status'], error_type))

        if cs_type == 'daother-7465':
            # DAOTHER-8108
            self.assertIn('missing_content', report['warning'])
            self.assertEqual(1, len(report['warning']['missing_content']))
        else:
            self.assertIn('content_mismatch', report['error'])
            self.assertEqual(1, report['error']['total'])

    def test_nmr_cs_str_consistency_check_daother_7465(self):
        self.__test_nmr_cs_str_consistency('daother-7465')

    def test_nmr_cs_str_consistency_check_daother_7465_2(self):
        self.__test_nmr_cs_str_consistency('daother-7465_2')


if __name__ == '__main__':
    unittest.main()
