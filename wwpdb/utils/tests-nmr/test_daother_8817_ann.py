##
# File: test_daother_8817_ann.py
# Date:  29-Sep-2023  M. Yokochi
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
        self.data_dir_path = os.path.join(here, 'mock-data-daother-8817/')
        self.data_file_path = {'daother-8817-ann': {'str': 'daother-8817-nef2cif.str',
                                                    'cif': 'D_8000212514_model_P1.cif.V5'},
                               'daother-8817-ann-2nd': {'str': 'D_8000212514_nmr-data-str_P1.str.V2',
                                                        'cif': 'D_8000212514_model_P1.cif.V2'},
                               'daother-8817-ann-3rd': {'str': 'daother-8817-nef2cif.str',
                                                        'cif': 'D_8000212514_model_P1.cif.V2'},
                               'daother-8817-ann-4th': {'str': 'D_800677_nmr-data-str_P1.str',
                                                        'cif': 'D_8000212514_model_P1.cif.V5'},
                               'daother-8817-ann-5th': {'str': 'D_800677_nmr-data-str_P1.str',
                                                        'cif': 'D_8000212514_model_P1.cif.V2'},
                               'daother-8817-ann-6th': {'str': 'daother-8817-nef2cif.cif',
                                                        'cif': 'D_1292133086_model_P1.cif.V19'},
                               'daother-8817-ann-7th': {'str': 'daother-8817-nef2cif.cif',
                                                        'cif': 'D_8000212922_model_P1.cif.V5'}
                               }
        self.utility = NmrDpUtility()

    def tearDown(self):
        pass

    def __test_nmr_str2cif_annotate(self, entry_id):  # pylint: disable=unused-private-member
        self.utility.setSource(self.data_dir_path + self.data_file_path[entry_id]['str'])
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + self.data_file_path[entry_id]['cif'], type='file')
        self.utility.addInput(name='nonblk_anomalous_cs', value=True, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.addOutput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.addOutput(name='insert_entry_id_to_loops', value=True, type='param')
        self.utility.addOutput(name='nmr_cif_file_path', value=self.data_dir_path + entry_id + '-next.cif', type='file')
        self.utility.setLog(self.data_dir_path + entry_id + '-str2cif-annotate-log.json')
        self.utility.setDestination(self.data_dir_path + entry_id + '-next.str')
        print(f' Generated {self.data_dir_path}{entry_id}-next.str')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str2cif-annotate')

        with open(self.data_dir_path + entry_id + '-str2cif-annotate-log.json', 'r') as file:
            report = json.loads(file.read())

        self.assertIsNone(report['error'])

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

    def test_nmr_str2cif_annotate_daother_8817(self):
        self.__test_nmr_str2cif_annotate('daother-8817-ann')

    def test_nmr_str2cif_annotate_daother_8817_2nd(self):
        self.__test_nmr_str2cif_annotate('daother-8817-ann-2nd')

    def test_nmr_str2cif_annotate_daother_8817_3rd(self):
        self.__test_nmr_str2cif_annotate('daother-8817-ann-3rd')

    def test_nmr_str2cif_annotate_daother_8817_4th(self):
        self.__test_nmr_str2cif_annotate('daother-8817-ann-4th')

    def test_nmr_str2cif_annotate_daother_8817_5th(self):
        self.__test_nmr_str2cif_annotate('daother-8817-ann-5th')

    def test_nmr_str2cif_annotate_daother_8817_6th(self):
        self.__test_nmr_str2cif_annotate('daother-8817-ann-6th')

    def test_nmr_str2cif_annotate_daother_8817_7th(self):
        self.__test_nmr_str2cif_annotate('daother-8817-ann-7th')


if __name__ == '__main__':
    unittest.main()
