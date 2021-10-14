##
# File: cs_str_chk_rcsb.py (DAOTHER-5611)
# Date:  24-Apr-2020  M. Yokochi
#
# Updates:
#
import unittest
import os
import json

from wwpdb.utils.nmr.NmrDpUtility import NmrDpUtility


class TestNmrDpUtility(unittest.TestCase):

    def setUp(self):
        here = os.path.abspath(os.path.dirname(__file__))
        self.data_dir_path = os.path.join(here, 'Pickup/')
        self.entries = ['6NZN', '6OC9', '6PQE', '6PQF', '6PSI', '6PVR', '6PVT', '6PX7', '6PX8']
        self.cs_file = {'6NZN': ['D_1000238834_cs-upload_P1.str.V1'],
                        '6OC9': ['D_1000240310_cs-upload_P1.str.V1'],
                        '6PQE': ['D_1000242877_cs-upload_P1.str.V1'],
                        '6PQF': ['D_1000242879_cs-upload_P1.str.V1'],
                        '6PSI': ['D_1000242994_cs-upload_P1.str.V1'],
                        '6PVR': ['D_1000243168_cs-upload_P1.str.V1'],
                        '6PVT': ['D_1000243177_cs-upload_P1.str.V1'],
                        '6PX7': ['D_1000243136_cs-upload_P1.str.V1'],
                        '6PX8': ['D_1000243232_cs-upload_P1.str.V1']
                        }
        self.cs_file_2 = {'6NZN': ['D_1000238834_cs-upload_P1.str.V2'],
                          '6OC9': ['D_1000240310_cs-upload_P1.str.V2'],
                          '6PQE': ['D_1000242877_cs-upload_P1.str.V2'],
                          '6PQF': ['D_1000242879_cs-upload_P1.str.V2'],
                          '6PSI': ['D_1000242994_cs-upload_P1.str.V2'],
                          '6PVR': ['D_1000243168_cs-upload_P1.str.V2'],
                          '6PVT': ['D_1000243177_cs-upload_P1.str.V2'],
                          '6PX7': ['D_1000243136_cs-upload_P1.str.V2'],
                          '6PX8': ['D_1000243232_cs-upload_P1.str.V2']
                          }
        self.original_model_file = {'6NZN': 'D_1000238834_model-upload_P1.cif.V1',
                                    '6OC9': 'D_1000240310_model-upload_P1.pdb.V1',
                                    '6PQE': 'D_1000242877_model-upload_P1.pdb.V1',
                                    '6PQF': 'D_1000242879_model-upload_P1.cif.V1',
                                    '6PSI': 'D_1000242994_model-upload_P1.pdb.V1',
                                    '6PVR': 'D_1000243168_model-upload_P1.cif.V1',
                                    '6PVT': 'D_1000243177_model-upload_P1.cif.V1',
                                    '6PX7': 'D_1000243136_model-upload_P1.pdb.V1',
                                    '6PX8': 'D_1000243232_model-upload_P1.pdb.V1'
                                    }
        self.model_file = {entry_id: entry_id.lower() + '.cif' for entry_id in self.entries}
        self.alt_model_file = {'6PVR': 'D_800299_model_P1.cif.V4'}
        self.nmr_dp_util = NmrDpUtility()
        pass

    def tearDown(self):
        pass

    def __test_nmr_cs_str_consistency(self, entry_id):
        entry_dir_path = self.data_dir_path + entry_id + '/'
        self.nmr_dp_util.addInput(name='chem_shift_file_path_list', value=[entry_dir_path + cs_file for cs_file in self.cs_file[entry_id]], type='file_list')
        self.nmr_dp_util.addOutput(name='chem_shift_file_path_list', value=[entry_dir_path + cs_file for cs_file in self.cs_file_2[entry_id]], type='file_list')
        if entry_id not in self.alt_model_file:
            self.nmr_dp_util.addInput(name='coordinate_file_path', value=entry_dir_path + self.model_file[entry_id], type='file')
        else:
            self.nmr_dp_util.addInput(name='coordinate_file_path', value=entry_dir_path + self.alt_model_file[entry_id], type='file')
        self.nmr_dp_util.addInput(name='nonblk_anomalous_cs', value=True, type='param')
        self.nmr_dp_util.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.nmr_dp_util.addInput(name='resolve_conflict', value=True, type='param')
        self.nmr_dp_util.addInput(name='check_mandatory_tag', value=False, type='param')
        self.nmr_dp_util.setLog(self.data_dir_path + entry_id.lower() + '-cs-str-consistency-log.json')
        self.nmr_dp_util.setVerbose(False)

        self.nmr_dp_util.op('nmr-cs-str-consistency-check')

        with open(self.data_dir_path + entry_id.lower() + '-cs-str-consistency-log.json', 'r') as file:
            report = json.loads(file.read())

        if not report['error'] is None:
            self.assertNotIn('internal_error', report['error'])

        if report['error'] is None:
            print('%s: %s' % (entry_id.lower(), report['information']['status']))
        elif 'format_issue' in report['error']:
            print('%s: %s\n format_issue: %s' % (entry_id.lower(), report['information']['status'], report['error']['format_issue'][0]['description']))
        elif 'missing_mandatory_content' in report['error']:
            print('%s: %s\n missing_mandatory_content: %s' % (entry_id.lower(), report['information']['status'], report['error']['missing_mandatory_content'][0]['description']))
        else:
            error_type = {str(k): len(v) for k, v in report['error'].items() if str(k) != 'total'}
            print('%s: %s, %s' % (entry_id.lower(), report['information']['status'], error_type))

    def test_6nzn(self):
        self.__test_nmr_cs_str_consistency('6NZN')

    def test_6oc9(self):
        self.__test_nmr_cs_str_consistency('6OC9')

    def test_6pqe(self):
        self.__test_nmr_cs_str_consistency('6PQE')

    def test_6pqf(self):
        self.__test_nmr_cs_str_consistency('6PQF')

    def test_6psi(self):
        self.__test_nmr_cs_str_consistency('6PSI')

    def test_6pvr(self):
        self.__test_nmr_cs_str_consistency('6PVR')

    def test_6pvt(self):
        self.__test_nmr_cs_str_consistency('6PVT')

    def test_6px7(self):
        self.__test_nmr_cs_str_consistency('6PX7')

    def test_6px8(self):
        self.__test_nmr_cs_str_consistency('6PX8')


if __name__ == '__main__':
    unittest.main()
