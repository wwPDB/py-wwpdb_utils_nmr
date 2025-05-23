##
# File: test_daother_7924.py
# Date:  10-Aug-2022  M. Yokochi
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
        self.data_dir_path = os.path.join(here, 'mock-data-daother-7924/')
        self.res_file_type = {
            'daother-7924': ['nm-res-cya', 'nm-res-cya', 'nm-res-cya', 'nm-res-cya', 'nm-res-cya']
        }
        self.cs_file_path = {
            'daother-7924': ['51520-ea22.str.txt']
        }
        self.mr_file_path = {
            'daother-7924': ['hbonds_dimer.lol', 'hbonds_dimer.upl', 'noesyc_dimer.upl', 'noesyn_dimer.upl', 'talos.aco']
        }
        self.model_file_path = {
            'daother-7924': 'D_800477_model_P1.cif.V4'
        }
        self.utility = NmrDpUtility()

    def tearDown(self):
        pass

    def __test_nmr_cs_str_consistency(self, entry_id):
        self.utility.addInput(name='chem_shift_file_path_list', value=[self.data_dir_path + cs_file_path for cs_file_path in self.cs_file_path[entry_id]], type='file_list')
        if len(self.mr_file_path[entry_id]) == 1:
            self.utility.addInput(name='atypical_restraint_file_path_list',
                                  value=[{'file_name': self.data_dir_path + self.mr_file_path[entry_id][0], 'file_type': self.res_file_type[entry_id]}],
                                  type='file_dict_list')
        else:
            ar_path_list = []
            for i, ar_path in enumerate(self.mr_file_path[entry_id]):
                ar_path_list.append({'file_name': self.data_dir_path + ar_path, 'file_type': self.res_file_type[entry_id][i]})
            self.utility.addInput(name='atypical_restraint_file_path_list', value=ar_path_list, type='file_dict_list')
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

        self.assertNotEqual(report['information']['status'], 'Error')
        if report['warning'] is not None:
            self.assertNotIn('missing_content', report['warning'])

    def test_nmr_cs_str_consistency_check_daother_7924(self):
        self.__test_nmr_cs_str_consistency('daother-7924')


if __name__ == '__main__':
    unittest.main()
