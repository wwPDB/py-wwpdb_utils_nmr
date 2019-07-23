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

    def test_nmr_nef_consistency_check_1nk2(self):
        self.utility.setSource(self.data_dir_path + '1nk2.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '1nk2.cif', type='file')
        self.utility.setLog(self.data_dir_path + '1nk2-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_nef_consistency_check_2kko(self):
        self.utility.setSource(self.data_dir_path + '2kko.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2kko.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2kko-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_nef_consistency_check_2mqq(self):
        self.utility.setSource(self.data_dir_path + '2mqq.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2mqq.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2mqq-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_nef_consistency_check_2mtv(self):
        self.utility.setSource(self.data_dir_path + '2mtv.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2mtv.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2mtv-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_nef_consistency_check_2l9r(self):
        self.utility.setSource(self.data_dir_path + '2l9r.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2l9r.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2l9r-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_nef_consistency_check_2la6(self):
        self.utility.setSource(self.data_dir_path + '2la6.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2la6.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2la6-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_nef_consistency_check_2lah(self):
        self.utility.setSource(self.data_dir_path + '2lah.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2lah.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2lah-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_nef_consistency_check_2lci(self):
        self.utility.setSource(self.data_dir_path + '2lci.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2lci.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2lci-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_nef_consistency_check_2ln3(self):
        self.utility.setSource(self.data_dir_path + '2ln3.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2ln3.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2ln3-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_nef_consistency_check_2loj(self):
        self.utility.setSource(self.data_dir_path + '2loj.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2loj.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2loj-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_nef_consistency_check_2ltl(self):
        self.utility.setSource(self.data_dir_path + '2ltl.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2ltl.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2ltl-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_nef_consistency_check_2ltm(self):
        self.utility.setSource(self.data_dir_path + '2ltm.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2ltm.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2ltm-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_nef_consistency_check_2m2e(self):
        self.utility.setSource(self.data_dir_path + '2m2e.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2m2e.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2m2e-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_nef_consistency_check_2m5o(self):
        self.utility.setSource(self.data_dir_path + '2m5o.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2m5o.cif', type='file')
        self.utility.setLog(self.data_dir_path + '2m5o-nef-consistency-log.json')

        self.utility.op('nmr-nef-consistency-check')

    def test_nmr_nef2str_deposit_check_1nk2(self):
        self.utility.setSource(self.data_dir_path + '1nk2.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '1nk2.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '1nk2-nef-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '1nk2-nef2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '1nk2-next.nef')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '1nk2-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '1nk2-nef2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef2str-deposit')

    def test_nmr_nef2str_deposit_check_2kko(self):
        self.utility.setSource(self.data_dir_path + '2kko.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2kko.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2kko-nef-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2kko-nef2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2kko-next.nef')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2kko-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2kko-nef2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef2str-deposit')

    def test_nmr_nef2str_deposit_check_2mqq(self):
        self.utility.setSource(self.data_dir_path + '2mqq.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2mqq.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2mqq-nef-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2mqq-nef2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2mqq-next.nef')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2mqq-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2mqq-nef2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef2str-deposit')

    def test_nmr_nef2str_deposit_check_2mtv(self):
        self.utility.setSource(self.data_dir_path + '2mtv.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2mtv.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2mtv-nef-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2mtv-nef2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2mtv-next.nef')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2mtv-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2mtv-nef2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef2str-deposit')

    def test_nmr_nef2str_deposit_check_2l9r(self):
        self.utility.setSource(self.data_dir_path + '2l9r.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2l9r.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2l9r-nef-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2l9r-nef2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2l9r-next.nef')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2l9r-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2l9r-nef2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef2str-deposit')

    def test_nmr_nef2str_deposit_check_2la6(self):
        self.utility.setSource(self.data_dir_path + '2la6.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2la6.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2la6-nef-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2la6-nef2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2la6-next.nef')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2la6-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2la6-nef2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef2str-deposit')

    def test_nmr_nef2str_deposit_check_2lah(self):
        self.utility.setSource(self.data_dir_path + '2lah.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2lah.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2lah-nef-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2lah-nef2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2lah-next.nef')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2lah-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2lah-nef2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef2str-deposit')

    def test_nmr_nef2str_deposit_check_2lci(self):
        self.utility.setSource(self.data_dir_path + '2lci.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2lci.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2lci-nef-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2lci-nef2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2lci-next.nef')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2lci-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2lci-nef2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef2str-deposit')

    def test_nmr_nef2str_deposit_check_2ln3(self):
        self.utility.setSource(self.data_dir_path + '2ln3.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2ln3.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2ln3-nef-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2ln3-nef2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2ln3-next.nef')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2ln3-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2ln3-nef2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

        self.utility.op('nmr-nef2str-deposit')

    def test_nmr_nef2str_deposit_check_2loj(self):
        self.utility.setSource(self.data_dir_path + '2loj.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2loj.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2loj-nef-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2loj-nef2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2loj-next.nef')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2loj-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2loj-nef2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

    def test_nmr_nef2str_deposit_check_2ltl(self):
        self.utility.setSource(self.data_dir_path + '2ltl.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2ltl.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2ltl-nef-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2ltl-nef2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2ltl-next.nef')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2ltl-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2ltl-nef2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

    def test_nmr_nef2str_deposit_check_2ltm(self):
        self.utility.setSource(self.data_dir_path + '2ltm.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2ltm.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2ltm-nef-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2ltm-nef2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2ltm-next.nef')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2ltm-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2ltm-nef2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

    def test_nmr_nef2str_deposit_check_2m2e(self):
        self.utility.setSource(self.data_dir_path + '2m2e.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2m2e.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2m2e-nef-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2m2e-nef2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2m2e-next.nef')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2m2e-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2m2e-nef2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

    def test_nmr_nef2str_deposit_check_2m5o(self):
        self.utility.setSource(self.data_dir_path + '2m5o.nef')
        self.utility.addInput(name='coordinate_file_path', value=self.data_dir_path + '2m5o.cif', type='file')
        self.utility.addInput(name='report_file_path', value=self.data_dir_path + '2m5o-nef-consistency-log.json', type='file')
        self.utility.addInput(name='entry_id', value='NEED_ACC_NO', type='param')
        self.utility.setLog(self.data_dir_path + '2m5o-nef2str-deposit-log.json')
        self.utility.setDestination(self.data_dir_path + '2m5o-next.nef')
        self.utility.addOutput(name='nmr-star_file_path', value=self.data_dir_path + '2m5o-nef2str.str', type='file')
        self.utility.addOutput(name='report_file_path', value=self.data_dir_path + '2m5o-nef2str-str-deposit-log.json', type='file')
        self.utility.setVerbose(False)

if __name__ == '__main__':
    unittest.main()
