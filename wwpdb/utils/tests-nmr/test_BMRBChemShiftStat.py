##
# File: test_BMRBChemShiftStat.py
# Date:  29-Jul-2019  M. Yokochi
#
# Updates:
# 16-Apr-2020  M. Yokochi - fix ambiguity code of atom name starts with 'Q' (e.g. LYZ:QZ)
# 20-Nov-2020  M. Yokochi - add unit test for HEM, HEB, HEC (DAOTHER-6366)
# 13-Oct-2021  M. Yokochi - code refactoring according to PEP8 using Pylint (DAOTHER-7389, issue #5)
##
import unittest

from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat


class TestBMRBChemShiftStat(unittest.TestCase):

    def setUp(self):
        self.bmrb_cs_stat = BMRBChemShiftStat()

    def tearDown(self):
        pass

    def test_load_from_csv(self):
        self.bmrb_cs_stat.loadStatFromCsvFiles()

    def test_write_as_pickle(self):
        self.bmrb_cs_stat.loadStatFromCsvFiles()
        self.bmrb_cs_stat.writeStatAsPickleFiles()

    def test_init(self):
        self.assertEqual(self.bmrb_cs_stat.isOk(), True)

    def test_poly_type(self):
        self.assertEqual(self.bmrb_cs_stat.getTypeOfCompId('ALA')[0], True)
        self.assertEqual(self.bmrb_cs_stat.getTypeOfCompId('GLY')[0], True)
        self.assertEqual(self.bmrb_cs_stat.getTypeOfCompId('PRO')[0], True)
        self.assertEqual(self.bmrb_cs_stat.getTypeOfCompId('PTR')[0], True)
        self.assertEqual(self.bmrb_cs_stat.getTypeOfCompId('DA')[1], True)
        self.assertEqual(self.bmrb_cs_stat.getTypeOfCompId('5MC')[1], True)
        self.assertEqual(self.bmrb_cs_stat.getTypeOfCompId('NAG')[2], True)
        self.assertEqual(self.bmrb_cs_stat.getTypeOfCompId('GLC')[2], True)

    def test_bb_atoms(self):
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('GLY'), ['C', 'CA', 'H', 'HA2', 'HA3', 'N'])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('PRO'), ['C', 'CA', 'CB', 'HA', 'N'])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('ALA'), ['C', 'CA', 'CB', 'H', 'HA', 'N'])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('CYS'), ['C', 'CA', 'CB', 'H', 'HA', 'N'])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('PTR'), ['C', 'CA', 'CB', 'H', 'HA', 'N'])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('PTR', polypeptide_like=True), ['C', 'CA', 'CB', 'H', 'HA', 'N'])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('PTR', polynucleotide_like=True), ['P'])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('DA'), ["C1'", "C2'", "C3'", "C4'", "C5'", "H1'", "H2'", "H2''", "H3'", "H4'", "H5'", "H5''", 'P'])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('DA', excl_minor_atom=True), ["H1'", "H2'", "H2''", "H3'", "H4'", "H5'", "H5''"])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('A'), ["C1'", "C2'", "C3'", "C4'", "C5'", "H1'", "H2'", "H3'", "H4'", "H5'", "H5''", "HO2'", 'P'])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('A', excl_minor_atom=True), ["C1'", "C2'", "C3'", "C4'", "C5'", "H1'", "H2'", "H3'", "H4'", "H5'", "H5''"])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('5MC'), ["H1'", "H2'", "H3'", "H4'", "H5'", "H5''", 'P', "C5'", "C4'", "C3'", "C2'", "C1'"])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('5MC', polypeptide_like=True), [])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('5MC', polynucleotide_like=True), ["H1'", "H2'", "H3'", "H4'", "H5'", "H5''", 'P', "C5'", "C4'", "C3'", "C2'", "C1'"])

    def test_arom_atoms(self):
        self.assertEqual(self.bmrb_cs_stat.getAromaticAtoms('ALA'), [])
        self.assertEqual(self.bmrb_cs_stat.getAromaticAtoms('PRO'), [])
        self.assertEqual(self.bmrb_cs_stat.getAromaticAtoms('HIS'), ['CD2', 'CE1', 'CG', 'HD1', 'HD2', 'HE1', 'HE2', 'ND1', 'NE2'])
        self.assertEqual(self.bmrb_cs_stat.getAromaticAtoms('PHE'), ['CD1', 'CD2', 'CE1', 'CE2', 'CG', 'CZ', 'HD1', 'HD2', 'HE1', 'HE2', 'HZ'])
        self.assertEqual(self.bmrb_cs_stat.getAromaticAtoms('TYR'), ['CD1', 'CD2', 'CE1', 'CE2', 'CG', 'CZ', 'HD1', 'HD2', 'HE1', 'HE2'])
        self.assertEqual(self.bmrb_cs_stat.getAromaticAtoms('TRP'), ['CD1', 'CD2', 'CE2', 'CE3', 'CG', 'CH2', 'CZ2', 'CZ3', 'HD1', 'HE1', 'HE3', 'HH2', 'HZ2', 'HZ3', 'NE1'])
        self.assertEqual(self.bmrb_cs_stat.getAromaticAtoms('PTR'), ['CD1', 'CD2', 'CE1', 'CE2', 'HD1', 'HD2', 'HE1', 'HE2', 'CG', 'CZ'])
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
        self.assertEqual(self.bmrb_cs_stat.getRepresentativeMethylProtons('ALA'), ['HB1'])
        self.assertEqual(self.bmrb_cs_stat.getNonRepresentativeMethylProtons('ALA'), ['HB2', 'HB3'])
        self.assertEqual(self.bmrb_cs_stat.getMethylAtoms('HEM'), ['CMA', 'CMB', 'CMC', 'CMD', 'HMA', 'HMAA', 'HMAB', 'HMB', 'HMBA', 'HMBB', 'HMC', 'HMCA', 'HMCB', 'HMD', 'HMDA', 'HMDB'])
        self.assertEqual(self.bmrb_cs_stat.getRepresentativeMethylProtons('HEM'), ['HMA', 'HMB', 'HMC', 'HMD'])
        self.assertEqual(self.bmrb_cs_stat.getNonRepresentativeMethylProtons('HEM'), ['HMAA', 'HMAB', 'HMBA', 'HMBB', 'HMCA', 'HMCB', 'HMDA', 'HMDB'])
        self.assertEqual(self.bmrb_cs_stat.getMethylAtoms('HEB'), ['HBB1', 'HBB2', 'HBB3', 'HMA1', 'HMA2', 'HMA3', 'HMB1',
                                                                   'HMB2', 'HMB3', 'HMC1', 'HMC2', 'HMC3', 'HMD1', 'HMD2', 'HMD3', 'CMA', 'CMB', 'CBB', 'CMC', 'CMD'])
        self.assertEqual(self.bmrb_cs_stat.getRepresentativeMethylProtons('HEB'), ['HBB1', 'HMA1', 'HMB1', 'HMC1', 'HMD1'])
        self.assertEqual(self.bmrb_cs_stat.getNonRepresentativeMethylProtons('HEB'), ['HBB2', 'HBB3', 'HMA2', 'HMA3', 'HMB2', 'HMB3', 'HMC2', 'HMC3', 'HMD2', 'HMD3'])
        self.assertEqual(self.bmrb_cs_stat.getMethylAtoms('HEC'), ['CBB', 'CBC', 'CMA', 'CMB', 'CMC', 'CMD',
                                                                   'HBB1', 'HBB2', 'HBB3', 'HBC1', 'HBC2', 'HBC3', 'HMA1', 'HMA2',
                                                                   'HMA3', 'HMB1', 'HMB2', 'HMB3', 'HMC1', 'HMC2', 'HMC3', 'HMD1', 'HMD2', 'HMD3'])
        self.assertEqual(self.bmrb_cs_stat.getRepresentativeMethylProtons('HEC'), ['HBB1', 'HBC1', 'HMA1', 'HMB1', 'HMC1', 'HMD1'])
        self.assertEqual(self.bmrb_cs_stat.getNonRepresentativeMethylProtons('HEC'), ['HBB2', 'HBB3', 'HBC2', 'HBC3', 'HMA2', 'HMA3', 'HMB2', 'HMB3', 'HMC2', 'HMC3', 'HMD2', 'HMD3'])

    def test_sc_atoms(self):
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('GLY'), [])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('ALA'), ['CB', 'HB1', 'HB2', 'HB3'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('CYS'), ['CB', 'HB2', 'HB3', 'HG'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('THR'), ['CB', 'CG2', 'HB', 'HG1', 'HG21', 'HG22', 'HG23'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('THR', excl_minor_atom=True), ['CB', 'CG2', 'HB', 'HG21', 'HG22', 'HG23'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('PRO'), ['CB', 'CD', 'CG', 'HB2', 'HB3', 'HD2', 'HD3', 'HG2', 'HG3'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('ARG'), ['CB', 'CD', 'CG', 'CZ', 'HB2', 'HB3', 'HD2', 'HD3',
                                                                      'HE', 'HG2', 'HG3', 'HH11', 'HH12', 'HH21', 'HH22', 'NE', 'NH1', 'NH2'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('ARG', excl_minor_atom=True), ['CB', 'CD', 'CG', 'HB2', 'HB3', 'HD2', 'HD3', 'HE', 'HG2', 'HG3', 'NE'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('LYS'), ['CB', 'CD', 'CE', 'CG', 'HB2', 'HB3', 'HD2', 'HD3', 'HE2', 'HE3', 'HG2', 'HG3', 'NZ', 'HZ1', 'HZ2', 'HZ3'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('LYS', excl_minor_atom=True), ['CB', 'CD', 'CE', 'CG', 'HB2', 'HB3', 'HD2', 'HD3', 'HE2', 'HE3', 'HG2', 'HG3'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('PTR', polypeptide_like=True), ['CB', 'CD1', 'CD2', 'CE1', 'CE2',
                                                                                             'HB2', 'HB3', 'HD1', 'HD2', 'HE1', 'HE2', 'CG', 'CZ', 'P', 'HO2P', 'HO3P'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('PTR', excl_minor_atom=True, polypeptide_like=True), ['CB', 'CD1', 'CD2',
                                                                                                                   'CE1', 'CE2', 'HB2', 'HB3', 'HD1', 'HD2', 'HE1', 'HE2'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('DA'), ['C2', 'C4', 'C5', 'C6', 'C8', 'H2', 'H61', 'H62', 'H8', 'N1', 'N3', 'N6', 'N7', 'N9'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('DA', excl_minor_atom=True), ['H2', 'H8'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('A'), ['C2', 'C4', 'C5', 'C6', 'C8', 'H2', 'H61', 'H62', 'H8', 'N1', 'N3', 'N6', 'N7', 'N9'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('5MC', polynucleotide_like=True), ['H6', 'HM51', 'HM52', 'HM53', 'HN41',
                                                                                                'HN42', 'N1', 'C2', 'N3', 'C4', 'N4', 'C5', 'C6', 'CM5', 'HOP2', 'HOP3', "HO2'"])

    def test_geminal_atom(self):
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('ARG', 'HB2'), 'HB3')
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('ARG', 'HB3'), 'HB2')
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('U', "H5'"), "H5''")
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('U', "H5''"), "H5'")
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('VAL', 'HG11'), 'HG21')
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('VAL', 'HG21'), 'HG11')
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('VAL', 'CG1'), 'CG2')
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('VAL', 'CG2'), 'CG1')

    def test_maxambigcode(self):
        self.assertEqual(self.bmrb_cs_stat.getMaxAmbigCodeWoSetId('ARG', 'HB2'), 2)
        self.assertEqual(self.bmrb_cs_stat.getMaxAmbigCodeWoSetId('TRP', 'CE2'), 1)
        self.assertEqual(self.bmrb_cs_stat.getMaxAmbigCodeWoSetId('TYR', 'HE2'), 3)
        self.assertEqual(self.bmrb_cs_stat.getMaxAmbigCodeWoSetId('GLU', 'HB2'), 2)
        self.assertEqual(self.bmrb_cs_stat.getMaxAmbigCodeWoSetId('LYS', 'HZ1'), 1)

if __name__ == '__main__':
    unittest.main()
