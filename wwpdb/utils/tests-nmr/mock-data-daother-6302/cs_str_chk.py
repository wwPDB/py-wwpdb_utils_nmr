##
# File: cs_str_chk.py (DAOTHER-6302)
# Date:  05-Nov-2020  M. Yokochi
#
# Updates:
#
import unittest
import json

from wwpdb.utils.nmr.NmrDpUtility import NmrDpUtility


class TestNmrDpUtility(unittest.TestCase):

    def setUp(self):
        self.data_dir_path = './'
        self.cs_file_path = {'daother-6302': ['D_1000245727_cs-upload_P1.str.V1-rev']
                             }
        self.model_file = {'daother-6302': 'D_1000245727_model_P1.cif.V1'}
        self.nmr_dp_util = NmrDpUtility()

    def tearDown(self):
        pass

    def __test_nmr_cs_str_consistency(self, entry_id):
        entry_dir_path = self.data_dir_path
        self.nmr_dp_util.addInput(name='chem_shift_file_path_list', value=[entry_dir_path + cs_file_path for cs_file_path in self.cs_file_path[entry_id]], type='file_list')
        self.nmr_dp_util.addInput(name='coordinate_file_path', value=self.model_file[entry_id], type='file')
        self.nmr_dp_util.addInput(name='nonblk_anomalous_cs', value=True, type='param')
        self.nmr_dp_util.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.nmr_dp_util.addInput(name='resolve_conflict', value=True, type='param')
        self.nmr_dp_util.addInput(name='check_mandatory_tag', value=False, type='param')
        self.nmr_dp_util.setLog(self.data_dir_path + entry_id.lower() + '-cs-str-consistency-log.json')
        self.nmr_dp_util.setVerbose(False)

        self.nmr_dp_util.op('nmr-cs-str-consistency-check')

        with open(self.data_dir_path + entry_id.lower() + '-cs-str-consistency-log.json', 'r') as file:
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

    def test_daother_6302(self):
        self.__test_nmr_cs_str_consistency('daother-6302')


if __name__ == '__main__':
    unittest.main()
