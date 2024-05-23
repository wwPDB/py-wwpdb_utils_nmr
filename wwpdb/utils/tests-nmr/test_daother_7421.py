##
# File: test_daother_7421.py
# Date:  27-Oct-2021  M. Yokochi
#
# Updates:
#
import unittest
import os
import json

try:
    from wwpdb.utils.nmr.NmrDpUtility import NmrDpUtility
    from wwpdb.utils.nmr.NmrDpReport import NmrDpReport
except ImportError:
    from nmr.NmrDpUtility import NmrDpUtility
    from nmr.NmrDpReport import NmrDpReport


class TestNmrDpUtility(unittest.TestCase):

    def setUp(self):
        here = os.path.abspath(os.path.dirname(__file__))
        self.data_dir_path = os.path.join(here, 'mock-data-daother-7421/')
        self.res_file_type = {
            'daother-7421': ['nm-res-amb', 'nm-res-amb', 'nm-aux-amb']
        }
        self.cs_file_path = {
            'daother-7421': ['D_1292118884_cs-upload_P1.str.V1']
        }
        self.mr_file_path = {
            'daother-7421': ['D_1292118884_mr-upload_P1.amber.V1', 'D_1292118884_mr-upload_P2.amber.V1', 'D_1292118884_mr-upload_P1.dat.V1']
        }
        self.model_file_path = {
            'daother-7421': 'D_800450_model_P1.cif.V1'
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

        with open(self.data_dir_path + entry_id + '-cs-str-consistency-log.json', 'r') as file:
            data = json.load(file)
            report = NmrDpReport()
            report.load(data)
            self.assertEqual(report.getNmrSeq1LetterCodeWithModelChainId('B', label_scheme=False).strip(), 'CUUAUUUG')

    def test_nmr_cs_str_consistency_check_daother_7421(self):
        self.__test_nmr_cs_str_consistency('daother-7421')


if __name__ == '__main__':
    unittest.main()
