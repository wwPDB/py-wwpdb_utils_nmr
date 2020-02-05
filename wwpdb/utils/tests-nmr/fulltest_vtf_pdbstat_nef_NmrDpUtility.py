##
# File: fulltest_vtf_pdbstat_nef_NmrDpUtility.py
# Date:  10-Dec-2019  M. Yokochi
#
# Updates:
##
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
        self.data_dir_path = os.path.join(here, 'NMR-VTF/PDBStat_examples/')
        self.data_file_path = {'2k2e': {'nef': 'BeR31/BeR31_2k2e.nef',
                                        'cif': 'BeR31/BeR31_2k2e.cif'},
                               '2jr2': {'nef': 'CsR4/CsR4_2jr2.nef',
                                        'cif': 'CsR4/CsR4_2jr2.cif'},
                               '2kcu': {'nef': 'CtR107/CtR107_2kcu.nef',
                                        'cif': 'CtR107/CtR107_2kcu.cif'},
                               '2ko1': {'nef': 'CtR148A/CtR148A_2ko1.nef',
                                        'cif': 'CtR148A/CtR148A_2ko1.cif'},
                               '2kpu': {'nef': 'DhR29B/DhR29B_2kpu.nef',
                                        'cif': 'DhR29B/DhR29B_2kpu.cif'},
                               '2kyi': {'nef': 'DhR8C/DhR8C_2kyi.nef',
                                        'cif': 'DhR8C/DhR8C_2kyi.cif'},
                               '2ko7': {'nef': 'HR41/HR41_2ko7.nef',
                                        'cif': 'HR41/HR41_2ko7.cif'},
                               'l22_t12': {'nef': 'L22_T12/L22_rt.nef',
                                           'cif': 'L22_T12/L22_rt.cif'},
                               '2kko': {'nef': 'MbR242E/MbR242E_2kko.nef',
                                        'cif': 'MbR242E/MbR242E_2kko.cif'},
                               '2luz': {'nef': 'MiR12/MiR12_2luz.nef',
                                        'cif': 'MiR12/MiR12_2luz.cif'},
                               '2kw5': {'nef': 'SgR145/SgR145_2kw5.nef',
                                        'cif': 'SgR145/SgR145_2kw5.cif'},
                               '2juw': {'nef': 'SoR77/SoR77_2juw.nef',
                                        'cif': 'SoR77/SoR77_2juw.cif'},
                               '2la3': {'nef': 'SPR104/SPR104_2l3a.nef',
                                        'cif': 'SPR104/SPR104_2l3a.cif'},
                               '2kzn': {'nef': 'SR10/SR10_2kzn.nef',
                                        'cif': 'SR10/SR10_2kzn.cif'},
                               '2loy': {'nef': 'WR73/WR73_2loy.nef',
                                        'cif': 'WR73/WR73_2loy.cif'},
                               '1pqx': {'nef': 'ZR18/ZR18_1pqx.nef',
                                        'cif': 'ZR18/ZR18_1pqx.cif'}}
        self.utility = NmrDpUtility()
        self.report = NmrDpReport()
        pass

    def tearDown(self):
        pass

    def __test_nmr_nef_consistency(self, entry_id):
        self.utility.setSource(self.data_dir_path + self.data_file_path[entry_id]['nef'])
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + self.data_file_path[entry_id]['cif'], type='file')
        self.utility.setLog(self.data_dir_path + entry_id + '-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

        with open(self.data_dir_path + entry_id + '-nef-consistency-log.json', 'r') as file:
            report = json.loads(file.read())

        if not report['error'] is None:
            self.assertEqual(report['error']['internal_error'], None)

        print('%s: %s' % (entry_id, report['information']['status']))

    def __test_nmr_nef2str_deposit_check(self, entry_id):
        if not os.access(self.data_dir_path + entry_id + '-nef-consistency-log.json', os.F_OK):
            self.__test_nmr_nef_consistency(entry_id)

        self.utility.setSource(self.data_dir_path + self.data_file_path[entry_id]['nef'])
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + self.data_file_path[entry_id]['cif'], type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + entry_id + '-nef-consistency-log.json', type='file')
        self.utility.setLog(self.data_dir_path + entry_id + '-nef2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + entry_id + '-next.nef')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + entry_id + '-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + entry_id + '-nef2str-str-deposit-log.json', type='file')
        self.utility.addOutput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef2str-deposit')

        with open(self.data_dir_path + entry_id + '-nef2str-str-deposit-log.json', 'r') as file:
            report = json.loads(file.read())

        if not report['error'] is None:
            self.assertEqual(report['error']['internal_error'], None)

    def test_nmr_nef_consistency_check_2k2e(self):
        self.__test_nmr_nef_consistency('2k2e')

    def test_nmr_nef_consistency_check_2jr2(self):
        self.__test_nmr_nef_consistency('2jr2')

    def test_nmr_nef_consistency_check_2kcu(self):
        self.__test_nmr_nef_consistency('2kcu')

    def test_nmr_nef_consistency_check_2ko1(self):
        self.__test_nmr_nef_consistency('2ko1')

    def test_nmr_nef_consistency_check_2kpu(self):
        self.__test_nmr_nef_consistency('2kpu')

    def test_nmr_nef_consistency_check_2kyi(self):
        self.__test_nmr_nef_consistency('2kyi')

    def test_nmr_nef_consistency_check_2ko7(self):
        self.__test_nmr_nef_consistency('2ko7')

    def test_nmr_nef_consistency_check_l22_t12(self):
        self.__test_nmr_nef_consistency('l22_t12')

    def test_nmr_nef_consistency_check_2kko(self):
        self.__test_nmr_nef_consistency('2kko')

    def test_nmr_nef_consistency_check_2luz(self):
        self.__test_nmr_nef_consistency('2luz')

    def test_nmr_nef_consistency_check_2kw5(self):
        self.__test_nmr_nef_consistency('2kw5')

    def test_nmr_nef_consistency_check_2juw(self):
        self.__test_nmr_nef_consistency('2juw')

    def test_nmr_nef_consistency_check_2la3(self):
        self.__test_nmr_nef_consistency('2la3')

    def test_nmr_nef_consistency_check_2kzn(self):
        self.__test_nmr_nef_consistency('2kzn')

    def test_nmr_nef_consistency_check_2loy(self):
        self.__test_nmr_nef_consistency('2loy')

    def test_nmr_nef_consistency_check_1pqx(self):
        self.__test_nmr_nef_consistency('1pqx')

if __name__ == '__main__':
    unittest.main()
