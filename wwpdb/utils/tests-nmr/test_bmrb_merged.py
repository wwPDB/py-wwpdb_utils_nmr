##
# File: test_bmrb_merged.py
# Date:  07-Sep-2020  M. Yokochi
#
# Updates:
#
import unittest
import os
import sys

from wwpdb.utils.nmr.NmrDpUtility import NmrDpUtility
from wwpdb.utils.nmr.NmrDpReport import NmrDpReport, NmrDpReportInputSource, NmrDpReportSequenceAlignment, NmrDpReportError, NmrDpReportWarning
from testfixtures import LogCapture

class TestNmrDpUtility(unittest.TestCase):

    def setUp(self):
        here = os.path.abspath(os.path.dirname(__file__))
        self.merge_dir = os.path.join(here, 'bmrb_merged')
        self.utility = NmrDpUtility()
        pass

    def tearDown(self):
        pass

    def __test_nmr_str2str_deposit_bmrb_merged(self, bmrb_id, pdb_id):
        cur_dir = self.merge_dir + '/bmr' + bmrb_id + '/'
        mr_template = 'merged_' + bmrb_id + '_' + pdb_id
        merged_mr_file = cur_dir + mr_template + '.str'
        coord_cif_file = cur_dir + pdb_id + '.cif'

        self.utility.setSource(merged_mr_file)
        self.utility.addInput(name='coordinate_file_path', value=coord_cif_file, type='file')
        self.utility.setLog(cur_dir + mr_template + '-str-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

        self.utility.setSource(merged_mr_file)
        self.utility.addInput(name='coordinate_file_path', value=coord_cif_file, type='file')
        self.utility.addInput(name='report_file_path', value=cur_dir + mr_template + '-str-consistency-log.json', type='file')
        self.utility.addInput(name='nonblk_anomalous_cs', value=True, type='param')
        self.utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        self.utility.setLog(cur_dir + mr_template + '-str2str-deposit-log.json')
        self.utility.setDestination(cur_dir + mr_template + '-next.str')
        self.utility.addOutput(name='entry_id', value=bmrb_id, type='param')
        self.utility.addOutput(name='insert_entry_id_to_loops', value=True, type='param')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str2str-deposit')

    def test_nmr_str2str_deposit_bmrb_merged(self):
        self.__test_nmr_str2str_deposit_bmrb_merged('15400', '2jt8')

if __name__ == '__main__':
    unittest.main()
