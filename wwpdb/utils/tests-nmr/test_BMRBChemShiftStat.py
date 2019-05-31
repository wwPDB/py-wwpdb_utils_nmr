import unittest
import os
import sys

from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat

class TestBMRBChemShiftStat(unittest.TestCase):

    def setUp(self):
        self.bmrb_cs_stat = BMRBChemShiftStat()
        pass

    def tearDown(self):
        pass

    def test_load_from_csv(self):
        self.bmrb_cs_stat.loadStatFromCsvFiles()
        
    def test_write_as_pickle(self):
        self.bmrb_cs_stat.loadStatFromCsvFiles()
        self.bmrb_cs_stat.writeStatAsPickleFiles()
        
    def test_init(self):
        self.bmrb_cs_stat.printStat(self.bmrb_cs_stat.dna_full)

if __name__ == '__main__':
    unittest.main()
