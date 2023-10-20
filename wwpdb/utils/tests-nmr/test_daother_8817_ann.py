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
                                                    'cif': 'D_8000212514_model_P1.cif.V5'}}
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
        self.utility.setVerbose(False)

        self.utility.op('nmr-str2cif-annotate')

        with open(self.data_dir_path + entry_id + '-str2cif-annotate-log.json', 'r') as file:
            report = json.loads(file.read())

        if report['error'] is None:
            print('%s: %s' % (entry_id, report['information']['status']))
        elif 'format_issue' in report['error']:
            print('%s: %s\n format_issue: %s' % (entry_id, report['information']['status'], report['error']['format_issue'][0]['description']))
        elif 'missing_mandatory_content' in report['error']:
            print('%s: %s\n missing_mandatory_content: %s' % (entry_id, report['information']['status'], report['error']['missing_mandatory_content'][0]['description']))
        else:
            error_type = {str(k): len(v) for k, v in report['error'].items() if str(k) != 'total'}
            print('%s: %s, %s' % (entry_id, report['information']['status'], error_type))

    def test_nmr_str2cif_annotate_daother_8817(self):
        self.__test_nmr_str2cif_annotate('daother-8817-ann')


if __name__ == '__main__':
    unittest.main()
