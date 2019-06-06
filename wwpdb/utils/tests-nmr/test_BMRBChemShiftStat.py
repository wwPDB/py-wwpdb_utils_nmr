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
        #self.bmrb_cs_stat.printStat(self.bmrb_cs_stat.aa_filt)
        #self.bmrb_cs_stat.printStat(self.bmrb_cs_stat.dna_filt)
        #self.bmrb_cs_stat.printStat(self.bmrb_cs_stat.rna_filt)
        #self.bmrb_cs_stat.printStat(self.bmrb_cs_stat.others)
        self.assertEqual(self.bmrb_cs_stat.isOk(), True)

    def test_bb_atoms(self):
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('GLY'), ['C', 'CA', 'H', 'HA2', 'HA3', 'N'])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('PRO'), ['C', 'CA', 'CB', 'HA', 'N'])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('ALA'), ['C', 'CA', 'CB', 'H', 'HA', 'N'])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('CYS'), ['C', 'CA', 'CB', 'H', 'HA', 'N'])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('PTR'), [])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('PTR', polypeptide_like=True), ['C', 'CA', 'CB', 'H', 'HA', 'N'])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('PTR', polynucleotide_like=True), [])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('DA'), ["C1'", "C2'", "C3'", "C4'", "C5'", "H1'", "H2'", "H2''", "H3'", "H4'", "H5'", "H5''", 'P'])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('A'), ["C1'", "C2'", "C3'", "C4'", "C5'", "H1'", "H2'", "H3'", "H4'", "H5'", "H5''", "HO2'", 'P'])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('5MC'), [])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('5MC', polypeptide_like=True), [])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('5MC', polynucleotide_like=True), ["H1'", "H2'", "H2''", "H3'", "H4'", "H5'", "H5''", 'P'])

    def test_arom_atoms(self):
        self.assertEqual(self.bmrb_cs_stat.getAromaticAtoms('ALA'), [])
        self.assertEqual(self.bmrb_cs_stat.getAromaticAtoms('PRO'), ['N'])
        self.assertEqual(self.bmrb_cs_stat.getAromaticAtoms('HIS'), ['CD2', 'CE1', 'CG', 'HD1', 'HD2', 'HE1', 'HE2', 'ND1', 'NE2'])
        self.assertEqual(self.bmrb_cs_stat.getAromaticAtoms('PHE'), ['CD1', 'CD2', 'CE1', 'CE2', 'CG', 'CZ', 'HD1', 'HD2', 'HE1', 'HE2', 'HZ'])
        self.assertEqual(self.bmrb_cs_stat.getAromaticAtoms('TYR'), ['CD1', 'CD2', 'CE1', 'CE2', 'CG', 'CZ', 'HD1', 'HD2', 'HE1', 'HE2'])
        self.assertEqual(self.bmrb_cs_stat.getAromaticAtoms('TRP'), ['CD1', 'CD2', 'CE2', 'CE3', 'CG', 'CH2', 'CZ2', 'CZ3', 'HD1', 'HE1', 'HE3', 'HH2', 'HZ2', 'HZ3', 'NE1'])
        self.assertEqual(self.bmrb_cs_stat.getAromaticAtoms('PTR'), ['CD1', 'CD2', 'CE1', 'CE2', 'HD1', 'HD2', 'HE1', 'HE2'])
        self.assertEqual(self.bmrb_cs_stat.getAromaticAtoms('DA'), ['C2', 'C4', 'C5', 'C6', 'C8', 'H2', 'H8', 'N1', 'N3', 'N7', 'N9'])
        self.assertEqual(self.bmrb_cs_stat.getAromaticAtoms('A'), ['C2', 'C4', 'C5', 'C6', 'C8', 'H2', 'H8', 'N1', 'N3', 'N7', 'N9'])
        self.assertEqual(self.bmrb_cs_stat.getAromaticAtoms('5MC'), [])

    def test_methyl_atoms(self):
        self.assertEqual(self.bmrb_cs_stat.getMethylAtoms('ALA'), ['CB', 'HB1', 'HB2', 'HB3'])
        self.assertEqual(self.bmrb_cs_stat.getMethylAtoms('CYS'), [])
        self.assertEqual(self.bmrb_cs_stat.getMethylAtoms('THR'), ['CG2', 'HG21', 'HG22', 'HG23'])
        self.assertEqual(self.bmrb_cs_stat.getMethylAtoms('ILE'), ['CD1', 'CG2', 'HD11', 'HD12', 'HD13', 'HG21', 'HG22', 'HG23'])
        self.assertEqual(self.bmrb_cs_stat.getMethylAtoms('VAL'), ['CG1', 'CG2', 'HG11', 'HG12', 'HG13', 'HG21', 'HG22', 'HG23'])
        self.assertEqual(self.bmrb_cs_stat.getMethylAtoms('LEU'), ['CD1', 'CD2', 'HD11', 'HD12', 'HD13', 'HD21', 'HD22', 'HD23'])
        self.assertEqual(self.bmrb_cs_stat.getMethylAtoms('DT'), ['C7', 'H71', 'H72', 'H73'])

    def test_sc_atoms(self):
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('GLY'), [])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('ALA'), ['CB', 'HB1', 'HB2', 'HB3'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('CYS'), ['CB', 'HB2', 'HB3', 'HG'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('THR'), ['CB', 'CG2', 'HB', 'HG1', 'HG21', 'HG22', 'HG23'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('PRO'), ['CB', 'CD', 'CG', 'HB2', 'HB3', 'HD2', 'HD3', 'HG2', 'HG3'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('PTR', polypeptide_like=True), ['CB', 'CD1', 'CD2', 'CE1', 'CE2', 'HB2', 'HB3', 'HD1', 'HD2', 'HE1', 'HE2'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('DA'), ['C2', 'C4', 'C5', 'C6', 'C8', 'H2', 'H61', 'H62', 'H8', 'N1', 'N3', 'N6', 'N7', 'N9'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('A'), ['C2', 'C4', 'C5', 'C6', 'C8', 'H2', 'H61', 'H62', 'H8', 'N1', 'N3', 'N6', 'N7', 'N9'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('5MC', polynucleotide_like=True), ['H6', 'HM51', 'HM52', 'HM53', 'HN41', 'HN42'])

if __name__ == '__main__':
    unittest.main()
