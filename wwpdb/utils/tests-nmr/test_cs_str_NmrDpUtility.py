##
# File: test_cs_NmrDpUtility.py
# Date:  28-Feb-2020  M. Yokochi
#
# Updates:
#
import unittest
import os
import sys
import json

from wwpdb.utils.nmr.NmrDpUtility import NmrDpUtility
from wwpdb.utils.nmr.NmrDpReport import NmrDpReport, NmrDpReportInputSource, NmrDpReportSequenceAlignment, NmrDpReportError, NmrDpReportWarning
from testfixtures import LogCapture

class TestNmrDpUtility(unittest.TestCase):

    def setUp(self):
        here = os.path.abspath(os.path.dirname(__file__))
        self.data_dir_path = os.path.join(here, 'mock-data/')
        self.cs_file_path = {'data': ['2la6-cs-data.str'],
                             'sf': ['2la6-cs-sf.str'],
                             'loop': ['2la6-cs-loop.str'],
                             'sf-double': ['2la6-cs-sf-double.str'],
                             'sf-double-error': ['2la6-cs-sf-double-error.str'],
                             'loop-double-error': ['2la6-cs-loop-double-error.str'],
                             'loop-double': ['2la6-cs-loop.str', '2la6-cs-loop-2.str'],
                             'daother-5213': ['bmr36129.str']
                             }
        self.model_file_path = {'data': '2la6.cif',
                                'sf': '2la6.cif',
                                'loop': '2la6.cif',
                                'sf-double': '2la6.cif',
                                'sf-double-error': '2la6.cif',
                                'loop-double-error': '2la6.cif',
                                'loop-double': '2la6.cif',
                                'daother-5213': 'pdb_extract_10300.cif'
                                }
        self.utility = NmrDpUtility()
        pass

    def tearDown(self):
        pass

    def __test_nmr_cs_str_consistency(self, cs_type):
        self.utility.addInput(name='chem_shift_file_path_list', value=[self.data_dir_path + cs_file_path for cs_file_path in self.cs_file_path[cs_type]], type='file_list')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + self.model_file_path[cs_type], type='file')
        self.utility.addInput(name='nonblk_anomalous_cs', value=True, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=False, type='param')
        self.utility.setLog(self.data_dir_path + cs_type + '-cs-str-consistency-log.json')

        self.utility.op('nmr-cs-str-consistency-check')

        with open(self.data_dir_path + cs_type + '-cs-str-consistency-log.json', 'r') as file:
            report = json.loads(file.read())

        if not report['error'] is None:
            self.assertEqual(report['error']['internal_error'], None)

        print('%s: %s' % (cs_type, report['information']['status']))

    def test_nmr_cs_str_consistency_check_data(self):
        self.__test_nmr_cs_str_consistency('data')

    def test_nmr_cs_str_consistency_check_sf(self):
        self.__test_nmr_cs_str_consistency('sf')

    def test_nmr_cs_str_consistency_check_loop(self):
        self.__test_nmr_cs_str_consistency('loop')

    def test_nmr_cs_str_consistency_check_sf_double(self):
        self.__test_nmr_cs_str_consistency('sf-double')

    def test_nmr_cs_str_consistency_check_sf_double_error(self):
        self.__test_nmr_cs_str_consistency('sf-double-error')

    def test_nmr_cs_str_consistency_check_loop_double_error(self):
        self.__test_nmr_cs_str_consistency('loop-double-error')

    def test_nmr_cs_str_consistency_check_loop_double(self):
        self.__test_nmr_cs_str_consistency('loop-double')

    def test_nmr_cs_str_consistency_check_daother_5213(self):
        self.__test_nmr_cs_str_consistency('daother-5213')

if __name__ == '__main__':
    unittest.main()
