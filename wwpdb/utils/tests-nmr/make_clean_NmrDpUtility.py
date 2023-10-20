##
# File: make_clean_NmrDpUtility.py
# Date:  30-Jul-2019  M. Yokochi
#
# Updates:
# 09-Oct-2019  M. Yokochi - add 'resolve_conflict' option in __test_nmr_nef_consistency and rename log file
# 05-Feb-2020  M. Yokochi - add 'check_mandatory_tag' option
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

    def __test_nmr_nef_consistency(self, entry_id):
        self.utility.setSource(self.data_dir_path + entry_id + '.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + entry_id + '.cif', type='file')
        self.utility.addInput(name='nonblk_anomalous_cs', value=True, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.setLog(self.data_dir_path + entry_id + '-clean-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

        with open(self.data_dir_path + entry_id + '-clean-nef-consistency-log.json', 'r') as file:
            report = json.loads(file.read())

        if not report['error'] is None:
            self.assertNotIn('internal_error', report['error'])

    def __test_nmr_nef2str_deposit(self, entry_id):
        if not os.access(self.data_dir_path + entry_id + '-clean-nef-consistency-log.json', os.F_OK):
            self.__test_nmr_nef_consistency(entry_id)

        print(entry_id)

        self.utility.setSource(self.data_dir_path + entry_id + '.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + entry_id + '.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + entry_id + '-clean-nef-consistency-log.json', type='file')
        self.utility.addInput(name='nonblk_anomalous_cs', value=True, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.setLog(self.data_dir_path + entry_id + '-clean-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + entry_id + '-clean.nef')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + entry_id + '-clean.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + entry_id + '-clean-str-deposit-log.json', type='file')
        self.utility.addOutput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef2str-deposit')

        with open(self.data_dir_path + entry_id + '-clean-deposit-log.json', 'r') as file:
            report = json.loads(file.read())

        if not report['error'] is None and os.path.exists(self.data_dir_path + entry_id + '-clean.nef'):
            os.remove(self.data_dir_path + entry_id + '-clean.nef')

        with open(self.data_dir_path + entry_id + '-clean-str-deposit-log.json', 'r') as file:
            report = json.loads(file.read())

        if not report['error'] is None and os.path.exists(self.data_dir_path + entry_id + '-clean.str'):
            os.remove(self.data_dir_path + entry_id + '-clean.str')

    def test_nmr_nef2str_deposit_check_1nk2(self):
        self.__test_nmr_nef2str_deposit('1nk2')

    def test_nmr_nef2str_deposit_check_2kko(self):
        self.__test_nmr_nef2str_deposit('2kko')

    def test_nmr_nef2str_deposit_check_2mqq(self):
        self.__test_nmr_nef2str_deposit('2mqq')

    def test_nmr_nef2str_deposit_check_2mtv(self):
        self.__test_nmr_nef2str_deposit('2mtv')

    def test_nmr_nef2str_deposit_check_2l9r(self):
        self.__test_nmr_nef2str_deposit('2l9r')

    def test_nmr_nef2str_deposit_check_2la6(self):
        self.__test_nmr_nef2str_deposit('2la6')

    def test_nmr_nef2str_deposit_check_2lah(self):
        self.__test_nmr_nef2str_deposit('2lah')

    def test_nmr_nef2str_deposit_check_2lci(self):
        self.__test_nmr_nef2str_deposit('2lci')

    def test_nmr_nef2str_deposit_check_2ln3(self):
        self.__test_nmr_nef2str_deposit('2ln3')

    def test_nmr_nef2str_deposit_check_2loj(self):
        self.__test_nmr_nef2str_deposit('2loj')

    def test_nmr_nef2str_deposit_check_2ltl(self):
        self.__test_nmr_nef2str_deposit('2ltl')

    def test_nmr_nef2str_deposit_check_2ltm(self):
        self.__test_nmr_nef2str_deposit('2ltm')

    def test_nmr_nef2str_deposit_check_2m2e(self):
        self.__test_nmr_nef2str_deposit('2m2e')

    def test_nmr_nef2str_deposit_check_2m5o(self):
        self.__test_nmr_nef2str_deposit('2m5o')


if __name__ == '__main__':
    unittest.main()
