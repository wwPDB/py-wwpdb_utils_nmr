##
# File: fulltest_vtf_bmrb_str_consist_chk.py
# Date:  10-Dec-2019  M. Yokochi
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
        self.data_dir_path = os.path.join(here, 'NMR-VTF/BMRB/')
        self.data_file_path = {'2k2e': {'str': 'BeR31/BeR31.str',
                                        'cif': 'BeR31/BeR31.cif'},
                               '2jr2': {'str': 'CsR4/CsR4.str',
                                        'cif': 'CsR4/CsR4.cif'},
                               '2kcu': {'str': 'CtR107/CtR107.str',
                                        'cif': 'CtR107/CtR107.cif'},
                               '2ko1': {'str': 'CtR148A/CtR148A.str',
                                        'cif': 'CtR148A/CtR148A.cif'},
                               '2kpu': {'str': 'DhR29B/DhR29B.str',
                                        'cif': 'DhR29B/DhR29B.cif'},
                               '2kyi': {'str': 'DhR8C/DhR8C.str',
                                        'cif': 'DhR8C/DhR8C.cif'},
                               '2ko7': {'str': 'HR41/HR41.str',
                                        'cif': 'HR41/HR41.cif'},
                               'l22_t12': {'str': 'L22_T12/L22_T12.str',
                                           'cif': 'L22_T12/L22_T12.cif'},
                               '2kko': {'str': 'MbR242E/MbR242E.str',
                                        'cif': 'MbR242E/MbR242E.cif'},
                               '2luz': {'str': 'MiR12/MiR12.str',
                                        'cif': 'MiR12/MiR12.cif'},
                               '2kw5': {'str': 'SgR145/SgR145.str',
                                        'cif': 'SgR145/SgR145.cif'},
                               '2juw': {'str': 'SoR77/SoR77.str',
                                        'cif': 'SoR77/SoR77.cif'},
                               '2la3': {'str': 'SPR104/SPR104.str',
                                        'cif': 'SPR104/SPR104.cif'},
                               '2kzn': {'str': 'SR10/SR10.str',
                                        'cif': 'SR10/SR10.cif'},
                               '2loy': {'str': 'WR73/WR73.str',
                                        'cif': 'WR73/WR73.cif'},
                               '1pqx': {'str': 'ZR18/ZR18.str',
                                        'cif': 'ZR18/ZR18.cif'}}
        self.utility = NmrDpUtility()

    def tearDown(self):
        pass

    def __test_nmr_str_consistency(self, entry_id):
        self.utility.setSource(self.data_dir_path + self.data_file_path[entry_id]['str'])
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + self.data_file_path[entry_id]['cif'], type='file')
        self.utility.addInput(name='nonblk_anomalous_cs', value=True, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.setLog(self.data_dir_path + entry_id + '-str-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

        with open(self.data_dir_path + entry_id + '-str-consistency-log.json', 'r') as file:
            report = json.loads(file.read())

        if not report['error'] is None:
            self.assertNotIn('internal_error', report['error'])

        if report['error'] is None:
            print('%s: %s' % (entry_id, report['information']['status']))
        elif 'format_issue' in report['error']:
            print('%s: %s\n format_issue: %s' % (entry_id, report['information']['status'], report['error']['format_issue'][0]['description']))
        elif 'missing_mandatory_content' in report['error']:
            print('%s: %s\n missing_mandatory_content: %s' % (entry_id, report['information']['status'], report['error']['missing_mandatory_content'][0]['description']))
        else:
            error_type = {str(k): len(v) for k, v in report['error'].items() if str(k) != 'total'}
            print('%s: %s, %s' % (entry_id, report['information']['status'], error_type))

    def __test_nmr_str2str_deposit(self, entry_id):  # pylint: disable=unused-private-member
        if not os.access(self.data_dir_path + entry_id + '-str-consistency-log.json', os.F_OK):
            self.__test_nmr_str_consistency(entry_id)

        self.utility.setSource(self.data_dir_path + self.data_file_path[entry_id]['str'])
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + self.data_file_path[entry_id]['cif'], type='file')
        self.utility.addInput(name='nonblk_anomalous_cs', value=True, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.addInput(name='resolve_conflict', value=True, type='param')
        self.utility.addInput(name='check_mandatory_tag', value=True, type='param')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + entry_id + '-str-consistency-log.json', type='file')
        self.utility.addOutput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.addOutput(name='insert_entry_id_to_loops', value=True, type='param')
        self.utility.setLog(self.data_dir_path + entry_id + '-str2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + entry_id + '-next.str')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str2str-deposit')

        with open(self.data_dir_path + entry_id + '-str2str-deposit-log.json', 'r') as file:
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

    def test_nmr_str_consistency_check_2k2e(self):
        self.__test_nmr_str_consistency('2k2e')

    def test_nmr_str_consistency_check_2jr2(self):
        self.__test_nmr_str_consistency('2jr2')

    def test_nmr_str_consistency_check_2kcu(self):
        self.__test_nmr_str_consistency('2kcu')

    def test_nmr_str_consistency_check_2ko1(self):
        self.__test_nmr_str_consistency('2ko1')

    def test_nmr_str_consistency_check_2kpu(self):
        self.__test_nmr_str_consistency('2kpu')

    def test_nmr_str_consistency_check_2kyi(self):
        self.__test_nmr_str_consistency('2kyi')

    def test_nmr_str_consistency_check_2ko7(self):
        self.__test_nmr_str_consistency('2ko7')

    def test_nmr_str_consistency_check_l22_t12(self):
        self.__test_nmr_str_consistency('l22_t12')

    def test_nmr_str_consistency_check_2kko(self):
        self.__test_nmr_str_consistency('2kko')

    def test_nmr_str_consistency_check_2luz(self):
        self.__test_nmr_str_consistency('2luz')

    def test_nmr_str_consistency_check_2kw5(self):
        self.__test_nmr_str_consistency('2kw5')

    def test_nmr_str_consistency_check_2juw(self):
        self.__test_nmr_str_consistency('2juw')

    def test_nmr_str_consistency_check_2la3(self):
        self.__test_nmr_str_consistency('2la3')

    def test_nmr_str_consistency_check_2kzn(self):
        self.__test_nmr_str_consistency('2kzn')

    def test_nmr_str_consistency_check_2loy(self):
        self.__test_nmr_str_consistency('2loy')

    def test_nmr_str_consistency_check_1pqx(self):
        self.__test_nmr_str_consistency('1pqx')


if __name__ == '__main__':
    unittest.main()
