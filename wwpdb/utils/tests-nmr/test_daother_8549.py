##
# File: test_daother_8549.py
# Date:  13-May-2023  M. Yokochi
#
# Updates:
#
import unittest
import os
import shutil

from wwpdb.utils.nmr.NmrDpUtility import NmrDpUtility


class TestNmrDpUtility(unittest.TestCase):

    def setUp(self):
        self.utility = NmrDpUtility()

    def tearDown(self):
        pass

    def test_nmr_str2nef_release_8549(self):
        here = os.path.abspath(os.path.dirname(__file__))
        data_dir_path = os.path.join(here, 'mock-data-daother-8549')

        inputNmrDataStrFile = os.path.join(data_dir_path, 'D_8000212194_nmr-data-str_P1.cif.V2')

        shutil.copyfile(inputNmrDataStrFile + '.bk', inputNmrDataStrFile)

        outputNmrDataNefFile = os.path.join(data_dir_path, 'D_8000212194_nmr-data-nef_P1.cif.V2')

        if os.path.exists(outputNmrDataNefFile):
            os.remove(outputNmrDataNefFile)

        logOutPath2 = os.path.join(data_dir_path, 'D_8000212194-logstrstr.json')
        logOutPath1 = os.path.join(data_dir_path, 'D_8000212194-logstrnef.json')
        # strOut = os.path.join(data_dir_path, 'dummy.str')
        self.utility.setVerbose(True)

        self.utility.setSource(inputNmrDataStrFile)
        # self.utility.setDestination(strOut)
        self.utility.addOutput(name="nef_file_path", value=outputNmrDataNefFile, type="file")
        self.utility.addOutput(name="report_file_path", value=logOutPath2, type="file")
        self.utility.addOutput(name="insert_entry_id_to_loops", value=True, type="param")
        self.utility.setLog(logOutPath1)
        self.utility.op("nmr-str2nef-release")

        self.assertTrue(os.path.exists(outputNmrDataNefFile))
    # """
    # def test_nmr_str2nef_release_2mes(self):
    #     here = os.path.abspath(os.path.dirname(__file__))
    #     data_dir_path = os.path.join(here, 'mock-data-daother-8549')

    #     inputNmrDataStrFile = os.path.join(data_dir_path, '2mes_nmr_data.str')
    #     outputNmrDataNefFile = os.path.join(data_dir_path, '2mes_nmr_data.nef')

    #     if os.path.exists(outputNmrDataNefFile):
    #         os.remove(outputNmrDataNefFile)

    #     logOutPath2 = os.path.join(data_dir_path, '2mes-logstrstr.json')
    #     logOutPath1 = os.path.join(data_dir_path, '2mes-logstrnef.json')
    #     # strOut = os.path.join(data_dir_path, 'dummy.str')
    #     self.utility.setVerbose(True)

    #     self.utility.setSource(inputNmrDataStrFile)
    #     # self.utility.setDestination(strOut)
    #     self.utility.addOutput(name="nef_file_path", value=outputNmrDataNefFile, type="file")
    #     self.utility.addOutput(name="report_file_path", value=logOutPath2, type="file")
    #     self.utility.addOutput(name="insert_entry_id_to_loops", value=True, type="param")
    #     self.utility.setLog(logOutPath1)
    #     self.utility.op("nmr-str2nef-release")

    #     self.assertTrue(os.path.exists(outputNmrDataNefFile))
    # """


if __name__ == '__main__':
    unittest.main()
