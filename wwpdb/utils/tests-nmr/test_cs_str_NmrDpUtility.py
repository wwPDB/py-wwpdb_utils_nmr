##
# File: test_cs_NmrDpUtility.py
# Date:  28-Feb-2020  M. Yokochi
#
# Updates:
# 18-Mar-2020  M. Yokochi - support 'Saveframe' data type as separated NMR data (DAOTHER-2737)
# 19-Mar-2020  M. Yokochi - check chain assignment for identical dimer case (DAOTHER-3343)
# 14-Apr-2020  M. Yokochi - add 'no-cs-row' and 'no-cs-loop' unit tests
# 22-Apr-2020  M. Yokochi - add a unit test for DAOTHER-5600
# 22-Apr-2020  M. Yokochi - add a unit test for DAOTHER-5602
# 23-Apr-2020  M. Yokochi - add a unit test for DAOTHER-5603
# 23-Apr-2020  M. Yokochi - add a unit test for DAOTHER-5609
# 23-Apr-2020  M. Yokochi - add a unit test for DAOTHER-5610
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
                             'no-cs-row': ['2la6-no-cs-row.str'],
                             'no-cs-loop': ['2la6-no-cs-loop.str'],
                             'daother-5213': ['bmr36129.str'],
                             'daother-2737': ['rcsb103272-shifts-original.apofepbstar3.str'],
                             'daother-3343': ['D_1200009291_cs.str'],
                             'daother-5594': ['rcsb104069shiftsoriginal.str'], #['rcsb104069shifts-revised.str']
                             'daother-5600': ['D_1000246544_cs-upload_P1.str.V1'],
                             'daother-5602': ['NMR-6v88_cs_rev.str'],
                             'daother-5603': ['D_1000245188_cs-upload_P1.str.V1'],
                             'daother-5609': ['D_1000248498_cs-upload_P1.str.V1'],
                             'daother-5610': ['6jpp_cs.str'] # ['6jpp_mod_cs.str']
                             }
        self.model_file_path = {'data': '2la6.cif',
                                'sf': '2la6.cif',
                                'loop': '2la6.cif',
                                'sf-double': '2la6.cif',
                                'sf-double-error': '2la6.cif',
                                'loop-double-error': '2la6.cif',
                                'loop-double': '2la6.cif',
                                'no-cs-row': '2la6.cif',
                                'no-cs-loop': '2la6.cif',
                                'daother-5213': 'pdb_extract_10300.cif',
                                'daother-2737': 'rcsb103272.cif',
                                'daother-3343': 'D_1200009291_model_P1.cif.V6',
                                'daother-5594': 'rcsb104069-coords-converted.cif',
                                'daother-5600': 'D_1000246544_model-upload_P1.cif.V1',
                                'daother-5602': 'NMR-6v88.cif',
                                'daother-5603': 'D_1000245188_model-upload_P1.cif.V1',
                                'daother-5609': 'D_1000248498_model-upload_P1.cif.V1',
                                'daother-5610': '6jpp.cif'
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
        self.utility.setVerbose(False)

        self.utility.op('nmr-cs-str-consistency-check')

        with open(self.data_dir_path + cs_type + '-cs-str-consistency-log.json', 'r') as file:
            report = json.loads(file.read())

        if not report['error'] is None:
            self.assertEqual(report['error']['internal_error'], None)

        if report['error'] is None:
            print('%s: %s' % (cs_type, report['information']['status']))
        elif not report['error']['format_issue'] is None:
            print('%s: %s\n format_issue: %s' % (cs_type, report['information']['status'], report['error']['format_issue'][0]['description']))
        elif not report['error']['missing_mandatory_content'] is None:
            print('%s: %s\n missing_mandatory_content: %s' % (cs_type, report['information']['status'], report['error']['missing_mandatory_content'][0]['description']))
        else:
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

    def test_nmr_cs_str_consistency_check_no_cs_row(self):
        self.__test_nmr_cs_str_consistency('no-cs-row')

    def test_nmr_cs_str_consistency_check_no_cs_loop(self):
        self.__test_nmr_cs_str_consistency('no-cs-loop')

    def test_nmr_cs_str_consistency_check_daother_5213(self):
        self.__test_nmr_cs_str_consistency('daother-5213')

    def test_nmr_cs_str_consistency_check_daother_2737(self):
        self.__test_nmr_cs_str_consistency('daother-2737')

    def test_nmr_cs_str_consistency_check_daother_3343(self):
        self.__test_nmr_cs_str_consistency('daother-3343')

    def test_nmr_cs_str_consistency_check_daother_5594(self):
        self.__test_nmr_cs_str_consistency('daother-5594')

    def test_nmr_cs_str_consistency_check_daother_5600(self):
        self.__test_nmr_cs_str_consistency('daother-5600')

    def test_nmr_cs_str_consistency_check_daother_5602(self):
        self.__test_nmr_cs_str_consistency('daother-5602')

    def test_nmr_cs_str_consistency_check_daother_5603(self):
        self.__test_nmr_cs_str_consistency('daother-5603')

    def test_nmr_cs_str_consistency_check_daother_5609(self):
        self.__test_nmr_cs_str_consistency('daother-5609')

    def test_nmr_cs_str_consistency_check_daother_5610(self):
        self.__test_nmr_cs_str_consistency('daother-5610')

if __name__ == '__main__':
    unittest.main()
