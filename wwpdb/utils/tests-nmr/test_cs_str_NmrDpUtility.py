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
# 13-May-2020  M. Yokochi - add a unit test for DAOTHER-5673
# 15-May-2020  M. Yokochi - add a unit test for DAOTHER-5687
# 08-Jul-2020  M. Yokochi - add unit tests for DAOTHER-5910 and 5926
# 12-Mar-2021  M. Yokochi - add a unit test for DAOTHER-6693
# 20-May-2021  M. Yokochi - add unit tests for DAOTHER-6834 and 6855
# 24-May-2021  M. Yokochi - add unit test for DAOTHER-6809
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
        self.data_dir_path = os.path.join(here, 'mock-data/')
        self.cs_file_path = {'data': ['2la6-cs-data.str'],
                             'sf': ['2la6-cs-sf.str'],
                             'loop': ['2la6-cs-loop.str'],
                             'sf-double': ['2la6-cs-sf-double.str'],
                             'sf-double-error': ['2la6-cs-sf-double-error.str'],
                             'loop-double-error': ['2la6-cs-loop-double-error.str'],
                             'loop-double': ['2la6-cs-loop.str', '2la6-cs-loop-2.str'],
                             'no-cs-row-error': ['2la6-no-cs-row.str'],
                             'no-cs-loop-error': ['2la6-no-cs-loop.str'],
                             'loop-less-error': ['2la6-cs-loop-less.str'],
                             'stop-less-error': ['2la6-cs-stop-less.str'],
                             'loop-with-name-error': ['2la6-cs-loop-with-name.str'],
                             'loop-stop-less-error': ['2la6-cs-loop-stop-less.str'],
                             'data-save-less-error': ['2la6-cs-data-save-less.str'],
                             'data-stop-less-error': ['2la6-cs-data-stop-less.str'],
                             'data-stop-save-less-error': ['2la6-cs-data-stop-save-less.str'],
                             'data-without-name-error': ['2la6-cs-data-without-name.str'],
                             'data-invalid-stop-error': ['2la6-cs-data-invalid-stop.str'],
                             'data-invalid-save-error': ['2la6-cs-data-invalid-save.str'],
                             'daother-5213': ['bmr36129.str'],
                             'daother-2737': ['rcsb103272-shifts-original.apofepbstar3.str'],
                             'daother-3343': ['D_1200009291_cs.str'],
                             'daother-5594': ['rcsb104069shiftsoriginal.str'],  # ['rcsb104069shifts-revised.str']
                             'daother-4060': ['bmr547_dummy.str'],
                             'daother-5600': ['D_1000246544_cs-upload_P1.str.V1'],
                             'daother-5602': ['NMR-6v88_cs.str'],  # ['NMR-6v88_cs_rev.str'],
                             'daother-5603': ['D_1000245188_cs-upload_P1.str.V1'],
                             'daother-5609': ['D_1000248498_cs-upload_P1.str.V1'],
                             'daother-5610': ['6jpp_cs.str'],  # ['6jpp_mod_cs.str'],
                             'daother-5673': ['D_1000249191_cs-upload_P1.str.V1'],
                             'daother-5687': ['2la6.str'],
                             'daother-5910': ['D_1000225716_cs_P1.cif.V4'],
                             'daother-5926': ['swallow_NMR-Star_3-1.str'],
                             'daother-6693': ['D_1000247867_cs-upload_P1.str.V1'],
                             'daother-6834': ['daother-6834_cs-upload_P1.str.V1'],
                             'daother-6855': ['D_1000256494_cs-upload_P1.str.V1'],
                             'daother-6809': ['D_1000256134_cs_P1.str']
                             }
        self.model_file_path = {'data': '2la6.cif',
                                'sf': '2la6.cif',
                                'loop': '2la6.cif',
                                'sf-double': '2la6.cif',
                                'sf-double-error': '2la6.cif',
                                'loop-double-error': '2la6.cif',
                                'loop-double': '2la6.cif',
                                'no-cs-row-error': '2la6.cif',
                                'no-cs-loop-error': '2la6.cif',
                                'loop-less-error': '2la6.cif',
                                'stop-less-error': '2la6.cif',
                                'loop-stop-less-error': '2la6.cif',
                                'loop-with-name-error': '2la6.cif',
                                'data-save-less-error': '2la6.cif',
                                'data-stop-less-error': '2la6.cif',
                                'data-stop-save-less-error': '2la6.cif',
                                'data-without-name-error': '2la6.cif',
                                'data-invalid-stop-error': '2la6.cif',
                                'data-invalid-save-error': '2la6.cif',
                                'daother-5213': 'pdb_extract_10300.cif',
                                'daother-2737': 'rcsb103272.cif',
                                'daother-3343': 'D_1200009291_model_P1.cif.V6',
                                'daother-5594': 'rcsb104069-coords-converted.cif',
                                'daother-4060': '1dmo.cif',
                                'daother-5600': 'D_1000246544_model-upload_P1.cif.V1',
                                'daother-5602': 'NMR-6v88.cif',
                                'daother-5603': 'D_1000245188_model-upload_P1.cif.V1',
                                'daother-5609': 'D_1000248498_model-upload_P1.cif.V1',
                                'daother-5610': '6jpp.cif',
                                'daother-5673': 'D_1000249191_model-upload_P1.cif.V1',
                                'daother-5687': '2la6.cif',
                                'daother-5910': 'D_1000225716_model_P1.cif.V22',
                                'daother-5926': 'D_800365_model_P1.cif.V4',
                                'daother-6693': 'D_1000247867_model-upload_P1.cif.V1',
                                'daother-6834': 'D_1000247867_model-upload_P1.cif.V1',
                                'daother-6855': 'D_1000256494_model-upload-convert_P1.cif.V1',
                                'daother-6809': 'D_1000256134_model_P1.cif.V14'
                                }
        self.utility = NmrDpUtility()

    def tearDown(self):
        pass

    def __test_nmr_cs_str_consistency(self, entry_id):
        self.utility.addInput(name='chem_shift_file_path_list', value=[{'file_name': self.data_dir_path + cs_file_path,
                                                                        'file_type': 'nmr-star',
                                                                        'original_file_name': 'original_' + cs_file_path}
                                                                       for cs_file_path in self.cs_file_path[entry_id]], type='file_dict_list')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + self.model_file_path[entry_id], type='file')
        self.utility.addInput(name='nonblk_anomalous_cs', value=True, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=False, type='param')
        self.utility.setDestination(self.data_dir_path + self.cs_file_path[entry_id][0] + '-daother-7407-next.str')
        self.utility.addOutput(name='nmr_cif_file_path', value=self.data_dir_path + self.cs_file_path[entry_id][0] + '-daother-7407-next.cif', type='file')
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

    def test_nmr_cs_str_consistency_check_no_cs_row_error(self):
        self.__test_nmr_cs_str_consistency('no-cs-row-error')

    def test_nmr_cs_str_consistency_check_no_cs_loop_error(self):
        self.__test_nmr_cs_str_consistency('no-cs-loop-error')

    def test_nmr_cs_str_consistency_check_loop_less_error(self):
        self.__test_nmr_cs_str_consistency('loop-less-error')

    def test_nmr_cs_str_consistency_check_stop_less_error(self):
        self.__test_nmr_cs_str_consistency('stop-less-error')

    def test_nmr_cs_str_consistency_check_loop_stop_less_error(self):
        self.__test_nmr_cs_str_consistency('loop-stop-less-error')

    def test_nmr_cs_str_consistency_check_loop_with_name_error(self):
        self.__test_nmr_cs_str_consistency('loop-with-name-error')

    def test_nmr_cs_str_consistency_check_data_save_less_error(self):
        self.__test_nmr_cs_str_consistency('data-save-less-error')

    def test_nmr_cs_str_consistency_check_data_stop_less_error(self):
        self.__test_nmr_cs_str_consistency('data-stop-less-error')

    def test_nmr_cs_str_consistency_check_data_stop_save_less_error(self):
        self.__test_nmr_cs_str_consistency('data-stop-save-less-error')

    def test_nmr_cs_str_consistency_check_data_without_name_error(self):
        self.__test_nmr_cs_str_consistency('data-without-name-error')

    def test_nmr_cs_str_consistency_check_data_invalid_stop_error(self):
        self.__test_nmr_cs_str_consistency('data-invalid-stop-error')

    def test_nmr_cs_str_consistency_check_data_invalid_save_error(self):
        self.__test_nmr_cs_str_consistency('data-invalid-save-error')

    def test_nmr_cs_str_consistency_check_daother_5213(self):
        self.__test_nmr_cs_str_consistency('daother-5213')

    def test_nmr_cs_str_consistency_check_daother_2737(self):
        self.__test_nmr_cs_str_consistency('daother-2737')

    def test_nmr_cs_str_consistency_check_daother_3343(self):
        self.__test_nmr_cs_str_consistency('daother-3343')

    def test_nmr_cs_str_consistency_check_daother_5594(self):
        self.__test_nmr_cs_str_consistency('daother-5594')

    def test_nmr_cs_str_consistency_check_daother_4060(self):
        self.__test_nmr_cs_str_consistency('daother-4060')

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

    def test_nmr_cs_str_consistency_check_daother_5673(self):
        self.__test_nmr_cs_str_consistency('daother-5673')

    def test_nmr_cs_str_consistency_check_daother_5687(self):
        self.__test_nmr_cs_str_consistency('daother-5687')

    def test_nmr_cs_str_consistency_check_daother_5910(self):
        self.__test_nmr_cs_str_consistency('daother-5910')

    def test_nmr_cs_str_consistency_check_daother_5926(self):
        self.__test_nmr_cs_str_consistency('daother-5926')

    def test_nmr_cs_str_consistency_check_daother_6693(self):
        self.__test_nmr_cs_str_consistency('daother-6693')

    def test_nmr_cs_str_consistency_check_daother_6834(self):
        self.__test_nmr_cs_str_consistency('daother-6834')

    def test_nmr_cs_str_consistency_check_daother_6855(self):
        self.__test_nmr_cs_str_consistency('daother-6855')

    def test_nmr_cs_str_consistency_check_daother_6809(self):
        self.__test_nmr_cs_str_consistency('daother-6809')


if __name__ == '__main__':
    unittest.main()
