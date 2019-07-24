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
        self.data_dir_path = os.path.join(here, '../nmr/NEFTranslator/data/')
        self.utility = NmrDpUtility()
        self.report = NmrDpReport()
        pass

    def tearDown(self):
        pass

    def __test_nmr_str_consistency(self, entry_id):
        self.utility.setSource(self.data_dir_path + entry_id + '.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + entry_id + '.cif', type='file')
        self.utility.setLog(self.data_dir_path + entry_id + '-str-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

        with open(self.data_dir_path + entry_id + '-str-consistency-log.json', 'r') as file:
            report = json.loads(file.read())

        self.assertEqual(report['error']['internal_error'], None)

    def __test_nmr_str2str_deposit_check(self, entry_id):
        if not os.access(self.data_dir_path + entry_id + '-str-consistency-log.json', os.F_OK):
            self.__test_nmr_str_consistency(entry_id)

        self.utility.setSource(self.data_dir_path + entry_id + '.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + entry_id + '.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + entry_id + '-str-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.addInput(name='insert_entry_id_to_loops', value=True, type='param')
        self.utility.setLog(self.data_dir_path + entry_id + '-str2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + entry_id + '-next.str')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str2str-deposit')

        with open(self.data_dir_path + entry_id + '-str2str-deposit-log.json', 'r') as file:
            report = json.loads(file.read())

        self.assertEqual(report['error']['internal_error'], None)

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

    def test_nmr_str2str_deposit_check_1nk2(self):
        self.__test_nmr_str2str_deposit_check('1nk2')

    def test_nmr_str2str_deposit_check_2kko(self):
        self.__test_nmr_str2str_deposit_check('2kko')

    def test_nmr_str2str_deposit_check_2mqq(self):
        self.__test_nmr_str2str_deposit_check('2mqq')

    def test_nmr_str2str_deposit_check_2mtv(self):
        self.__test_nmr_str2str_deposit_check('2mtv')

    def test_nmr_str2str_deposit_check_2l9r(self):
        self.__test_nmr_str2str_deposit_check('2l9r')

    def test_nmr_str2str_deposit_check_2la6(self):
        self.__test_nmr_str2str_deposit_check('2la6')

    def test_nmr_str2str_deposit_check_2lah(self):
        self.__test_nmr_str2str_deposit_check('2lah')

    def test_nmr_str2str_deposit_check_2lci(self):
        self.__test_nmr_str2str_deposit_check('2lci')

    def test_nmr_str2str_deposit_check_2ln3(self):
        self.__test_nmr_str2str_deposit_check('2ln3')

    def test_nmr_str2str_deposit_check_2loj(self):
        self.__test_nmr_str2str_deposit_check('2loj')

    def test_nmr_str2str_deposit_check_2ltl(self):
        self.__test_nmr_str2str_deposit_check('2ltl')

    def test_nmr_str2str_deposit_check_2ltm(self):
        self.__test_nmr_str2str_deposit_check('2ltm')

    def test_nmr_str2str_deposit_check_2m2e(self):
        self.__test_nmr_str2str_deposit_check('2m2e')

    def test_nmr_str2str_deposit_check_2m5o(self):
        self.__test_nmr_str2str_deposit_check('2m5o')

if __name__ == '__main__':
    unittest.main()
