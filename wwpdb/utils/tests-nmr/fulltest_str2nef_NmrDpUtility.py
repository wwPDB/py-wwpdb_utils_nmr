##
# File: fulltest_str2nef_NmrDpUtility.py
# Date:  28-Nov-2019  M. Yokochi
#
# Updates:
# 21-Feb-2020  M. Yokochi - change name of workflow operation (nmr-str2nef-release)
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
        self.data_dir_path = os.path.join(here, 'mock-data/')
        self.utility = NmrDpUtility()

    def tearDown(self):
        pass

    def __test_nmr_str_consistency(self, entry_id):
        self.utility.setSource(self.data_dir_path + entry_id + '.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + entry_id + '.cif', type='file')
        self.utility.setLog(self.data_dir_path + entry_id + '-str2nef-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

        with open(self.data_dir_path + entry_id + '-str2nef-consistency-log.json', 'r') as file:
            report = json.loads(file.read())

        if report['error'] is not None:
            self.assertNotIn('internal_error', report['error'])

    def __test_nmr_str2nef_release(self, entry_id):
        if not os.access(self.data_dir_path + entry_id + '-str2nef-consistency-log.json', os.F_OK):
            self.__test_nmr_str_consistency(entry_id)

        print(entry_id)

        self.utility.setSource(self.data_dir_path + entry_id + '.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + entry_id + '.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + entry_id + '-str2nef-consistency-log.json', type='file')
        self.utility.setLog(self.data_dir_path + entry_id + '-str2nef-release-log.json')
        self.utility.setDestination(self.data_dir_path + entry_id + '-str2nef-next.str')
        self.utility.addOutput(name='nef_file_path', value=self.data_dir_path + entry_id + '-str2nef.nef', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + entry_id + '-str2nef-nef-release-log.json', type='file')
        self.utility.addOutput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str2nef-release')

        with open(self.data_dir_path + entry_id + '-str2nef-nef-release-log.json', 'r') as file:
            report = json.loads(file.read())

        if report['error'] is not None:
            self.assertNotIn('internal_error', report['error'])

    def test_nmr_str_consistency_check_1nk2(self):
        self.__test_nmr_str_consistency('1nk2')

    def test_nmr_str_consistency_check_2mqq(self):
        self.__test_nmr_str_consistency('2mqq')

    def test_nmr_str_consistency_check_2mtv(self):
        self.__test_nmr_str_consistency('2mtv')

    def test_nmr_str_consistency_check_2l9r(self):
        self.__test_nmr_str_consistency('2l9r')

    def test_nmr_str_consistency_check_2la6(self):
        self.__test_nmr_str_consistency('2la6')

    def test_nmr_str_consistency_check_2lah(self):
        self.__test_nmr_str_consistency('2lah')

    def test_nmr_str_consistency_check_2lci(self):
        self.__test_nmr_str_consistency('2lci')

    def test_nmr_str_consistency_check_2ln3(self):
        self.__test_nmr_str_consistency('2ln3')

    def test_nmr_str_consistency_check_2loj(self):
        self.__test_nmr_str_consistency('2loj')

    def test_nmr_str_consistency_check_2ltl(self):
        self.__test_nmr_str_consistency('2ltl')

    def test_nmr_str_consistency_check_2ltm(self):
        self.__test_nmr_str_consistency('2ltm')

    def test_nmr_str_consistency_check_2m2e(self):
        self.__test_nmr_str_consistency('2m2e')

    def test_nmr_str_consistency_check_2m5o(self):
        self.__test_nmr_str_consistency('2m5o')

    def test_nmr_str2nef_release_1nk2(self):
        self.__test_nmr_str2nef_release('1nk2')

    def test_nmr_str2nef_release_2kko(self):
        self.__test_nmr_str2nef_release('2kko')

    def test_nmr_str2nef_release_2mqq(self):
        self.__test_nmr_str2nef_release('2mqq')

    def test_nmr_str2nef_release_2mtv(self):
        self.__test_nmr_str2nef_release('2mtv')

    def test_nmr_str2nef_release_2l9r(self):
        self.__test_nmr_str2nef_release('2l9r')

    def test_nmr_str2nef_release_2la6(self):
        self.__test_nmr_str2nef_release('2la6')

    def test_nmr_str2nef_release_2lah(self):
        self.__test_nmr_str2nef_release('2lah')

    def test_nmr_str2nef_release_2lci(self):
        self.__test_nmr_str2nef_release('2lci')

    def test_nmr_str2nef_release_2ln3(self):
        self.__test_nmr_str2nef_release('2ln3')

    def test_nmr_str2nef_release_2loj(self):
        self.__test_nmr_str2nef_release('2loj')

    def test_nmr_str2nef_release_2ltl(self):
        self.__test_nmr_str2nef_release('2ltl')

    def test_nmr_str2nef_release_2ltm(self):
        self.__test_nmr_str2nef_release('2ltm')

    def test_nmr_str2nef_release_2m2e(self):
        self.__test_nmr_str2nef_release('2m2e')

    def test_nmr_str2nef_release_2m5o(self):
        self.__test_nmr_str2nef_release('2m5o')


if __name__ == '__main__':
    unittest.main()
