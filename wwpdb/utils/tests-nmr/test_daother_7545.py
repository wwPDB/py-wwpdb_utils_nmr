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

    def __test_nmr_str_consistency(self, entry_id):
        self.utility.addInput(name='chem_shift_file_path_list', value=[self.data_dir_path + cs_file_path for cs_file_path in self.cs_file_path[entry_id]], type='file_list')
        if len(self.mr_file_path[entry_id]) == 1:
            self.utility.addInput(name='restraint_file_path_list', value=[self.data_dir_path + self.mr_file_path[entry_id][0]], type='file_list')
        else:
            mr_path_list = []
            for mr_path in self.mr_file_path[entry_id]:
                mr_path_list.append(self.data_dir_path + mr_path)
            self.utility.addInput(name='restraint_file_path_list', value=mr_path_list, type='file_list')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + self.model_file_path[entry_id], type='file')
        self.utility.addInput(name='nonblk_anomalous_cs', value=True, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=False, type='param')
        self.utility.setLog(self.data_dir_path + entry_id + '-cs-str-consistency-log.json')
        self.utility.setVerbose(False)

        self.utility.op('nmr-cs-str-consistency-check')

        with open(self.data_dir_path + entry_id + '-cs-str-consistency-log.json', 'r') as file:
            report = json.loads(file.read())

        if report['error'] is not None:
            self.assertNotIn('internal_error', report['error'])

        status = report['information']['status']
        if report['error'] is None:
            print(f"{entry_id}: {status}")
        elif 'format_issue' in report['error']:
            print(f"{entry_id}: {status}\n format_issue: {report['error']['format_issue'][0]['description']}")
        elif 'missing_mandatory_content' in report['error']:
            print(f"{entry_id}: {status}\n missing_mandatory_content: {report['error']['missing_mandatory_content'][0]['description']}")
        else:
            error_type = {str(k): len(v) for k, v in report['error'].items() if str(k) != 'total'}
            print(f"{entry_id}: {status}, {error_type}")

        if 'only' in entry_id:
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
