##
# File: test_daother_7545.py
# Date:  15-Dec-2021  M. Yokochi
#
# Updates:
##
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
        self.data_dir_path = os.path.join(here, 'mock-data-daother-7545/')
        self.cs_file_path = {
            'daother-7545': ['D_1300025537_cs-upload_P1.str.V1'],
            'daother-7545_dihed_plus': ['D_1300025537_cs-upload_P1.str.V1'],
            'daother-7545_dihed_only': ['D_1300025537_cs-upload_P1.str.V1']
        }
        self.mr_file_path = {
            'daother-7545': ['D_1300025537_mr-upload_P1.dat.V2'],
            'daother-7545_dihed_plus': ['D_1300025537_mr-upload_P1.dat.V2', 'Torsion_angles.txt'],
            'daother-7545_dihed_only': ['Torsion_angles.txt']
        }
        self.model_file_path = {
            'daother-7545': 'D_1300025537_model-upload_P1.cif.V1',
            'daother-7545_dihed_plus': 'D_1300025537_model-upload_P1.cif.V1',
            'daother-7545_dihed_only': 'D_1300025537_model-upload_P1.cif.V1'
        }
        self.utility = NmrDpUtility()

    def tearDown(self):
        pass

    def __test_nmr_str_consistency(self, cs_type):
        self.utility.addInput(name='chem_shift_file_path_list', value=[self.data_dir_path + cs_file_path for cs_file_path in self.cs_file_path[cs_type]], type='file_list')
        if len(self.mr_file_path[cs_type]) == 1:
            self.utility.addInput(name='restraint_file_path_list', value=[self.data_dir_path + self.mr_file_path[cs_type][0]], type='file_list')
        else:
            mr_path_list = []
            for mr_path in self.mr_file_path[cs_type]:
                mr_path_list.append(self.data_dir_path + mr_path)
            self.utility.addInput(name='restraint_file_path_list', value=mr_path_list, type='file_list')
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

        if report['error'] is not None:
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

        if 'only' in cs_type:
            # DAOTHER-8108
            # self.assertEqual(report['information']['status'], 'Error')
            self.assertNotEqual(report['information']['status'], 'Error')
        else:
            self.assertNotEqual(report['information']['status'], 'Error')

    def test_nmr_str_consistency_check(self):
        self.__test_nmr_str_consistency('daother-7545')

    def test_nmr_str_consistency_check_dihed_plus(self):
        self.__test_nmr_str_consistency('daother-7545_dihed_plus')

    def test_nmr_str_consistency_check_dihed_only(self):
        self.__test_nmr_str_consistency('daother-7545_dihed_only')


if __name__ == '__main__':
    unittest.main()
