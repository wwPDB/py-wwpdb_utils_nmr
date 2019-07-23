import unittest
import os
import sys

from wwpdb.utils.nmr.NmrDpUtility import NmrDpUtility
from wwpdb.utils.nmr.NmrDpReport import NmrDpReport, NmrDpReportInputSource, NmrDpReportSequenceAlignment, NmrDpReportError, NmrDpReportWarning
from testfixtures import LogCapture

class TestNmrDpUtility(unittest.TestCase):

    def setUp(self):
        here = os.path.abspath(os.path.dirname(__file__))
        self.data_dir_path = os.path.join(here, '../nmr/NEFTranslator/data/')
        self.utility = NmrDpUtility()
        pass

    def tearDown(self):
        pass

    def test_nmr_str_consistency_check_1nk2(self):
        self.utility.setSource(self.data_dir_path + '1nk2.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '1nk2.cif', type='file')
        self.utility.setLog(self.data_dir_path + '1nk2-str-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

    def test_nmr_str_consistency_check_2kko(self):
        self.utility.setSource(self.data_dir_path + '2kko.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2kko.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2kko-str-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

    def test_nmr_str_consistency_check_2mqq(self):
        self.utility.setSource(self.data_dir_path + '2mqq.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2mqq.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2mqq-str-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

    def test_nmr_str_consistency_check_2mtv(self):
        self.utility.setSource(self.data_dir_path + '2mtv.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2mtv.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2mtv-str-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

    def test_nmr_str_consistency_check_2l9r(self):
        self.utility.setSource(self.data_dir_path + '2l9r.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2l9r.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2l9r-str-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

    def test_nmr_str_consistency_check_2la6(self):
        self.utility.setSource(self.data_dir_path + '2la6.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2la6.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2la6-str-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

    def test_nmr_str_consistency_check_2lah(self):
        self.utility.setSource(self.data_dir_path + '2lah.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2lah.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2lah-str-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

    def test_nmr_str_consistency_check_2lci(self):
        self.utility.setSource(self.data_dir_path + '2lci.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2lci.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2lci-str-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

    def test_nmr_str_consistency_check_2ln3(self):
        self.utility.setSource(self.data_dir_path + '2ln3.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2ln3.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2ln3-str-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

    def test_nmr_str_consistency_check_2loj(self):
        self.utility.setSource(self.data_dir_path + '2loj.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2loj.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2loj-str-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

    def test_nmr_str_consistency_check_2ltl(self):
        self.utility.setSource(self.data_dir_path + '2ltl.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2ltl.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2ltl-str-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

    def test_nmr_str_consistency_check_2ltm(self):
        self.utility.setSource(self.data_dir_path + '2ltm.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2ltm.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2ltm-str-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

    def test_nmr_str_consistency_check_2m2e(self):
        self.utility.setSource(self.data_dir_path + '2m2e.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2m2e.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2m2e-str-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

    def test_nmr_str_consistency_check_2m5o(self):
        self.utility.setSource(self.data_dir_path + '2m5o.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2m5o.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2m5o-str-consistency-log.json')

        self.utility.op('nmr-str-consistency-check')

    def test_nmr_str2str_deposit_check_1nk2(self):
        self.utility.setSource(self.data_dir_path + '1nk2.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '1nk2.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '1nk2-str-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '1nk2-str2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '1nk2-next.str')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '1nk2-str2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '1nk2-str2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str2str-deposit')

    def test_nmr_str2str_deposit_check_2kko(self):
        self.utility.setSource(self.data_dir_path + '2kko.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2kko.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2kko-str-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2kko-str2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2kko-next.str')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2kko-str2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2kko-str2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str2str-deposit')

    def test_nmr_str2str_deposit_check_2mqq(self):
        self.utility.setSource(self.data_dir_path + '2mqq.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2mqq.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2mqq-str-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2mqq-str2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2mqq-next.str')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2mqq-str2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2mqq-str2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str2str-deposit')

    def test_nmr_str2str_deposit_check_2mtv(self):
        self.utility.setSource(self.data_dir_path + '2mtv.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2mtv.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2mtv-str-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2mtv-str2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2mtv-next.str')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2mtv-str2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2mtv-str2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str2str-deposit')

    def test_nmr_str2str_deposit_check_2l9r(self):
        self.utility.setSource(self.data_dir_path + '2l9r.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2l9r.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2l9r-str-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2l9r-str2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2l9r-next.str')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2l9r-str2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2l9r-str2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str2str-deposit')

    def test_nmr_str2str_deposit_check_2la6(self):
        self.utility.setSource(self.data_dir_path + '2la6.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2la6.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2la6-str-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2la6-str2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2la6-next.str')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2la6-str2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2la6-str2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str2str-deposit')

    def test_nmr_str2str_deposit_check_2lah(self):
        self.utility.setSource(self.data_dir_path + '2lah.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2lah.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2lah-str-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2lah-str2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2lah-next.str')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2lah-str2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2lah-str2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str2str-deposit')

    def test_nmr_str2str_deposit_check_2lci(self):
        self.utility.setSource(self.data_dir_path + '2lci.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2lci.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2lci-str-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2lci-str2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2lci-next.str')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2lci-str2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2lci-str2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str2str-deposit')

    def test_nmr_str2str_deposit_check_2ln3(self):
        self.utility.setSource(self.data_dir_path + '2ln3.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2ln3.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2ln3-str-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2ln3-str2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2ln3-next.str')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2ln3-str2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2ln3-str2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

        self.utility.op('nmr-str2str-deposit')

    def test_nmr_str2str_deposit_check_2loj(self):
        self.utility.setSource(self.data_dir_path + '2loj.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2loj.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2loj-str-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2loj-str2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2loj-next.str')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2loj-str2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2loj-str2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

    def test_nmr_str2str_deposit_check_2ltl(self):
        self.utility.setSource(self.data_dir_path + '2ltl.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2ltl.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2ltl-str-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2ltl-str2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2ltl-next.str')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2ltl-str2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2ltl-str2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

    def test_nmr_str2str_deposit_check_2ltm(self):
        self.utility.setSource(self.data_dir_path + '2ltm.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2ltm.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2ltm-str-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2ltm-str2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2ltm-next.str')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2ltm-str2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2ltm-str2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

    def test_nmr_str2str_deposit_check_2m2e(self):
        self.utility.setSource(self.data_dir_path + '2m2e.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2m2e.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2m2e-str-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2m2e-str2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2m2e-next.str')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2m2e-str2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2m2e-str2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

    def test_nmr_str2str_deposit_check_2m5o(self):
        self.utility.setSource(self.data_dir_path + '2m5o.str')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2m5o.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2m5o-str-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2m5o-str2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2m5o-next.str')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2m5o-str2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2m5o-str2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

if __name__ == '__main__':
    unittest.main()
