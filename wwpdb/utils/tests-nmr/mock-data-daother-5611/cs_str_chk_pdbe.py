##
# File: cs_str_chk_pdbe.py (DAOTHER-5611)
# Date:  24-Apr-2020  M. Yokochi
#
# Updates:
#
import unittest
import os
import sys
import json

from wwpdb.utils.nmr.NmrDpUtility import NmrDpUtility
from wwpdb.utils.nmr.NmrDpReport import NmrDpReport, NmrDpReportInputSource, NmrDpReportSequenceAlignment, NmrDpReportError, NmrDpReportWarning

class TestNmrDpUtility(unittest.TestCase):

    def setUp(self):
        here = os.path.abspath(os.path.dirname(__file__))
        self.data_dir_path = os.path.join(here, '5611_NMR-FILES/')
        self.entries = ['6QEB', '6QES', '6QET', '6QEU', '6QF8', '6QWR', '6TPH']
        self.cs_file = {entry_id: ['shifts-upload.str'] for entry_id in self.entries}
        self.cs_file_2 = {entry_id: ['shifts-upload.str.V2'] for entry_id in self.entries}
        self.original_model_file = {'6QEB': 'model-upload.cif',
                                    '6QES': 'model-upload.pdb',
                                    '6QET': 'model-upload.pdb',
                                    '6QEU': 'model-upload.pdb',
                                    '6QF8': 'model-upload.pdb',
                                    '6QWR': 'model-upload.pdb',
                                    '6TPH': 'model-upload.cif'
                                    }
        self.model_file = {entry_id: entry_id.lower() + '.cif' for entry_id in self.entries}
        self.nmr_dp_util = NmrDpUtility()
        pass

    def tearDown(self):
        pass

    def __test_nmr_cs_str_consistency(self, entry_id):
        entry_dir_path = self.data_dir_path + entry_id + '/'
        self.nmr_dp_util.addInput(name='chem_shift_file_path_list', value=[entry_dir_path + cs_file for cs_file in self.cs_file[entry_id]], type='file_list')
        self.nmr_dp_util.addOutput(name='chem_shift_file_path_list', value=[entry_dir_path + cs_file for cs_file in self.cs_file_2[entry_id]], type='file_list')
        self.nmr_dp_util.addInput(name='coordinate_file_path', value=entry_dir_path + self.model_file[entry_id], type='file')
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

    def test_6qeb(self):
        self.__test_nmr_cs_str_consistency('6QEB')

    def test_6qes(self):
        self.__test_nmr_cs_str_consistency('6QES')

    def test_6qet(self):
        self.__test_nmr_cs_str_consistency('6QET')

    def test_6qeu(self):
        self.__test_nmr_cs_str_consistency('6QEU')

    def test_6qf8(self):
        self.__test_nmr_cs_str_consistency('6QF8')

    def test_6qwr(self):
        self.__test_nmr_cs_str_consistency('6QWR')

    def test_6tph(self):
        self.__test_nmr_cs_str_consistency('6TPH')

if __name__ == '__main__':
    unittest.main()
