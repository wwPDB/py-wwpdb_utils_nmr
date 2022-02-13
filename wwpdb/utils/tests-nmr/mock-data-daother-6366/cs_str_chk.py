##
# File: cs_str_chk.py (DAOTHER-6366)
# Date:  26-Nov-2020  M. Yokochi
#
# Updates:
#
import unittest
import json

from wwpdb.utils.nmr.NmrDpUtility import NmrDpUtility


class TestNmrDpUtility(unittest.TestCase):

    def setUp(self):
        self.data_dir_path = './'
        self.cs_file_path = {'daother-6366': ['6wqe_cs.str']
                             }
        self.model_file = {'daother-6366': '6wqe.cif'}
        self.nmr_dp_util = NmrDpUtility()
        pass

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

    def test_daother_6366(self):
        self.__test_nmr_cs_str_consistency('daother-6366')


if __name__ == '__main__':
    unittest.main()
