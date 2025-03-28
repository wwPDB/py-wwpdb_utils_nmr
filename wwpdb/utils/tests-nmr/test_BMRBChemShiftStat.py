##
# File: test_BMRBChemShiftStat.py
# Date:  29-Jul-2019  M. Yokochi
#
# Updates:
# 16-Apr-2020  M. Yokochi - fix ambiguity code of atom name starts with 'Q' (e.g. LYZ:QZ)
# 20-Nov-2020  M. Yokochi - add unit test for HEM, HEB, HEC (DAOTHER-6366)
# 13-Oct-2021  M. Yokochi - code refactoring according to PEP8 using Pylint (DAOTHER-7389, issue #5)
# 22-Apr-2024  M. Yokochi - add unit test to verify BMRB CS statistics are filtered by CCD (DAOTHER-9317)
# 22-Apr-2024  M. Yokochi - add unit test to update BMRB CS statistics from https://bmrb.io/ftp/pub/bmrb/statistics/chem_shifts/ (DAOTHER-9317)
##
import unittest

try:
    from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
except ImportError:
    from nmr.BMRBChemShiftStat import BMRBChemShiftStat


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

    # def test_init(self):
    #     self.assertEqual(self.bmrb_cs_stat.isOk(), True)

    def test_poly_type(self):
        self.assertEqual(self.bmrb_cs_stat.getTypeOfCompId('ALA')[0], True)
        self.assertEqual(self.bmrb_cs_stat.getTypeOfCompId('GLY')[0], True)
        self.assertEqual(self.bmrb_cs_stat.getTypeOfCompId('PRO')[0], True)
        self.assertEqual(self.bmrb_cs_stat.getTypeOfCompId('PTR')[0], True)
        self.assertEqual(self.bmrb_cs_stat.getTypeOfCompId('DA')[1], True)
        self.assertEqual(self.bmrb_cs_stat.getTypeOfCompId('5MC')[1], True)
        self.assertEqual(self.bmrb_cs_stat.getTypeOfCompId('NAG')[2], True)
        self.assertEqual(self.bmrb_cs_stat.getTypeOfCompId('GLC')[2], True)
        self.assertEqual(self.bmrb_cs_stat.getTypeOfCompId('MK8')[0], True)

    def test_bb_atoms(self):
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('GLY'), ['C', 'CA', 'H', 'HA2', 'HA3', 'N'])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('PRO'), ['C', 'CA', 'HA', 'N'])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('ALA'), ['C', 'CA', 'H', 'HA', 'N'])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('CYS'), ['C', 'CA', 'H', 'HA', 'N'])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('PTR'), ['C', 'CA', 'H', 'HA', 'N'])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('PTR', polypeptide_like=True), ['C', 'CA', 'H', 'HA', 'N'])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('PTR', polynucleotide_like=True), ['P'])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('DA'), ["C1'", "C2'", "C3'", "C4'", "C5'", "H1'", "H2'", "H2''", "H3'", "H4'", "H5'", "H5''", 'P'])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('DA', excl_minor_atom=True), ["H1'", "H2'", "H2''", "H3'", "H4'", "H5'", "H5''", 'P'])
        self.assertEqual(set(self.bmrb_cs_stat.getBackBoneAtoms('A')), {"C1'", "C2'", "C3'", "C4'", "C5'", "H1'", "H2'", "H3'", "H4'", "H5'", "H5''", "HO2'", 'P'})
        self.assertEqual(set(self.bmrb_cs_stat.getBackBoneAtoms('A', excl_minor_atom=True)), {"C1'", "C2'", "C3'", "C4'", "C5'", "H1'", "H2'", "H3'", "H4'", "H5'", "H5''"})
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('5MC'), ["H1'", "H2'", "HO2'", "H3'", "H4'", "H5'", "H5''", 'P', "C5'", "C4'", "C3'", "C2'", "C1'"])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('5MC', polypeptide_like=True), [])
        self.assertEqual(self.bmrb_cs_stat.getBackBoneAtoms('5MC', polynucleotide_like=True), ["H1'", "H2'", "HO2'", "H3'", "H4'", "H5'", "H5''",
                                                                                               'P', "C5'", "C4'", "C3'", "C2'", "C1'"])

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
        self.assertEqual(self.bmrb_cs_stat.getMethylAtoms('ILE'), ['CG2', 'HG21', 'HG22', 'HG23', 'CD1', 'HD11', 'HD12', 'HD13'])
        self.assertEqual(self.bmrb_cs_stat.getMethylAtoms('VAL'), ['CG1', 'HG11', 'HG12', 'HG13', 'CG2', 'HG21', 'HG22', 'HG23'])
        self.assertEqual(self.bmrb_cs_stat.getMethylAtoms('LEU'), ['CD1', 'HD11', 'HD12', 'HD13', 'CD2', 'HD21', 'HD22', 'HD23'])
        self.assertEqual(self.bmrb_cs_stat.getMethylAtoms('DT'), ['C7', 'H71', 'H72', 'H73'])
        self.assertEqual(self.bmrb_cs_stat.getRepMethylProtons('ALA'), ['HB1'])
        self.assertEqual(self.bmrb_cs_stat.getNonRepMethylProtons('ALA'), ['HB2', 'HB3'])
        self.assertEqual(self.bmrb_cs_stat.getMethylAtoms('HEM'), ['CMA', 'HMA', 'HMAA', 'HMAB', 'CMB', 'HMB', 'HMBA', 'HMBB', 'CMC', 'HMC', 'HMCA', 'HMCB',
                                                                   'CMD', 'HMD', 'HMDA', 'HMDB'])
        self.assertEqual(self.bmrb_cs_stat.getRepMethylProtons('HEM'), ['HMA', 'HMB', 'HMC', 'HMD'])
        self.assertEqual(self.bmrb_cs_stat.getNonRepMethylProtons('HEM'), ['HMAA', 'HMAB', 'HMBA', 'HMBB', 'HMCA', 'HMCB', 'HMDA', 'HMDB'])
        self.assertEqual(self.bmrb_cs_stat.getMethylAtoms('HEB'), ['CMA', 'HMA1', 'HMA2', 'HMA3', 'CMB', 'HMB1', 'HMB2', 'HMB3', 'CBB', 'HBB1', 'HBB2', 'HBB3',
                                                                   'CMC', 'HMC1', 'HMC2', 'HMC3', 'CMD', 'HMD1', 'HMD2', 'HMD3'])
        self.assertEqual(self.bmrb_cs_stat.getRepMethylProtons('HEB'), ['HMA1', 'HMB1', 'HBB1', 'HMC1', 'HMD1'])
        self.assertEqual(self.bmrb_cs_stat.getNonRepMethylProtons('HEB'), ['HMA2', 'HMA3', 'HMB2', 'HMB3', 'HBB2', 'HBB3', 'HMC2', 'HMC3', 'HMD2', 'HMD3'])
        self.assertEqual(self.bmrb_cs_stat.getMethylAtoms('HEC'), ['CMA', 'HMA1', 'HMA2', 'HMA3', 'CMB', 'HMB1', 'HMB2', 'HMB3', 'CBB', 'HBB1', 'HBB2', 'HBB3',
                                                                   'CMC', 'HMC1', 'HMC2', 'HMC3', 'CBC', 'HBC1', 'HBC2', 'HBC3', 'CMD', 'HMD1', 'HMD2', 'HMD3'])
        self.assertEqual(self.bmrb_cs_stat.getRepMethylProtons('HEC'), ['HMA1', 'HMB1', 'HBB1', 'HMC1', 'HBC1', 'HMD1'])
        self.assertEqual(self.bmrb_cs_stat.getNonRepMethylProtons('HEC'), ['HMA2', 'HMA3', 'HMB2', 'HMB3', 'HBB2', 'HBB3', 'HMC2', 'HMC3', 'HBC2', 'HBC3', 'HMD2', 'HMD3'])
        self.assertEqual(self.bmrb_cs_stat.getRepMethylProtons('L94'), ['H171', 'H474', 'H181', 'H484'])
        self.assertEqual(self.bmrb_cs_stat.getMethylAtoms('MET'), ['CE', 'HE1', 'HE2', 'HE3'])

    def test_sc_atoms(self):
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('GLY'), [])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('ALA'), ['CB', 'HB1', 'HB2', 'HB3'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('CYS'), ['CB', 'HB2', 'HB3', 'HG'])
        self.assertEqual(set(self.bmrb_cs_stat.getSideChainAtoms('THR')), {'CB', 'CG2', 'HB', 'HG1', 'HG21', 'HG22', 'HG23'})
        self.assertEqual(set(self.bmrb_cs_stat.getSideChainAtoms('THR', excl_minor_atom=True)), {'CB', 'CG2', 'HB', 'HG21', 'HG22', 'HG23'})
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('PRO'), ['CB', 'CD', 'CG', 'HB2', 'HB3', 'HD2', 'HD3', 'HG2', 'HG3'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('ARG'), ['CB', 'CD', 'CG', 'CZ', 'HB2', 'HB3', 'HD2', 'HD3',
                                                                      'HE', 'HG2', 'HG3', 'HH11', 'HH12', 'HH21', 'HH22', 'NE', 'NH1', 'NH2'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('ARG', excl_minor_atom=True), ['CB', 'CD', 'CG', 'HB2', 'HB3', 'HD2', 'HD3', 'HE', 'HG2', 'HG3'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('LYS'), ['CB', 'CD', 'CE', 'CG', 'HB2', 'HB3', 'HD2', 'HD3', 'HE2', 'HE3', 'HG2', 'HG3', 'NZ', 'HZ1', 'HZ2', 'HZ3'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('LYS', excl_minor_atom=True), ['CB', 'CD', 'CE', 'CG', 'HB2', 'HB3', 'HD2', 'HD3', 'HE2', 'HE3', 'HG2', 'HG3'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('PTR', polypeptide_like=True), ['CB', 'CD1', 'CD2', 'CE1', 'CE2',
                                                                                             'HB2', 'HB3', 'HD1', 'HD2', 'HE1', 'HE2', 'CG', 'CZ', 'P', 'HO2P', 'HO3P'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('PTR', excl_minor_atom=True, polypeptide_like=True), ['CB', 'CD1', 'CD2',
                                                                                                                   'CE1', 'CE2', 'HB2', 'HB3', 'HD1', 'HD2', 'HE1', 'HE2'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('DA'), ['C2', 'C4', 'C5', 'C6', 'C8', 'H2', 'H61', 'H62', 'H8', 'N1', 'N3', 'N6', 'N7', 'N9'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('DA', excl_minor_atom=True), ['H2', 'H8'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('A'), ['C2', 'C4', 'C5', 'C6', 'C8', 'H2', 'H61', 'H62', 'H8', 'N1', 'N3', 'N6', 'N7', 'N9'])
        self.assertEqual(self.bmrb_cs_stat.getSideChainAtoms('5MC', polynucleotide_like=True), ['HN41', 'HN42', 'H6', 'HM51', 'HM52', 'HM53',
                                                                                                'N1', 'C2', 'N3', 'C4', 'N4', 'C5', 'C6', 'CM5', 'HOP2', 'HOP3'])

    def test_geminal_atom(self):
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('ARG', 'HB2'), 'HB3')
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('ARG', 'HB3'), 'HB2')
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('U', "H5'"), "H5''")
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('U', "H5''"), "H5'")
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('VAL', 'HG11'), 'HG21')
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('VAL', 'HG21'), 'HG11')
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('VAL', 'CG1'), 'CG2')
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('VAL', 'CG2'), 'CG1')
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('LEU', 'HD12'), 'HD22')
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('TYR', 'HD2'), 'HD1')
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('DG', 'H21'), 'H22')
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('DG', 'H22'), 'H21')
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('DG', "H2'"), "H2''")
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('DG', "H2''"), "H2'")
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('D4P', 'H1'), 'H6')
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('D4P', 'H3'), 'H5')
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('GHP', 'HC2'), 'H6')
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('GHP', 'H3'), 'H5')
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('D4P', 'C2'), 'C6')
        self.assertEqual(self.bmrb_cs_stat.getGeminalAtom('GHP', 'C2'), 'C6')

    def test_maxambigcode(self):
        self.assertEqual(self.bmrb_cs_stat.getMaxAmbigCodeWoSetId('ARG', 'HB2'), 2)
        self.assertEqual(self.bmrb_cs_stat.getMaxAmbigCodeWoSetId('TRP', 'CE2'), 1)
        self.assertEqual(self.bmrb_cs_stat.getMaxAmbigCodeWoSetId('TYR', 'HE2'), 3)
        self.assertEqual(self.bmrb_cs_stat.getMaxAmbigCodeWoSetId('GLU', 'HB2'), 2)
        self.assertEqual(self.bmrb_cs_stat.getMaxAmbigCodeWoSetId('LYS', 'HZ1'), 1)
        self.assertEqual(self.bmrb_cs_stat.getMaxAmbigCodeWoSetId('D4P', 'H1'), 3)
        self.assertEqual(self.bmrb_cs_stat.getMaxAmbigCodeWoSetId('D4P', 'H6'), 3)
        self.assertEqual(self.bmrb_cs_stat.getMaxAmbigCodeWoSetId('GHP', 'HC2'), 3)
        self.assertEqual(self.bmrb_cs_stat.getMaxAmbigCodeWoSetId('GHP', 'H6'), 3)
        self.assertEqual(self.bmrb_cs_stat.getMaxAmbigCodeWoSetId('FUC', 'H61'), 1)
        self.assertEqual(self.bmrb_cs_stat.getMaxAmbigCodeWoSetId('M3L', 'HM11'), 2)

    def test_prot_in_same_group(self):
        self.assertEqual(self.bmrb_cs_stat.getProtonsInSameGroup('ARG', 'HB2'), ['HB2', 'HB3'])
        self.assertEqual(self.bmrb_cs_stat.getProtonsInSameGroup('VAL', 'HG11'), ['HG11', 'HG12', 'HG13'])
        self.assertEqual(self.bmrb_cs_stat.getProtonsInSameGroup('TYR', 'HD2'), ['HD2'])
        self.assertEqual(self.bmrb_cs_stat.getProtonsInSameGroup('ILE', 'HD11'), ['HD11', 'HD12', 'HD13'])

    def test_peptide_line(self):
        self.assertEqual(self.bmrb_cs_stat.peptideLike('6NA'), True)
        self.assertEqual(self.bmrb_cs_stat.peptideLike('D4P'), True)
        self.assertEqual(self.bmrb_cs_stat.peptideLike('GHP'), True)

    def test_udpate_stat_cvs_files(self):
        self.assertEqual(self.bmrb_cs_stat.updateStatCsvFiles(), True)

    def test_atom_nomenclature(self):
        self.assertEqual(self.bmrb_cs_stat.testAtomNomenclatureOfLibrary(), True)

    def test_doh_hn1(self):
        self.assertEqual(self.bmrb_cs_stat.checkAtomNomenclature('HN1', 'DOH'), (True, 'BHD', 'H'))

    def test_daother_9317(self):
        self.assertEqual([stat['atom_id'] for stat in self.bmrb_cs_stat.get('MEA') if 'avg' in stat], ['H', 'HA', 'HB1', 'HB2', 'HD1', 'HD2', 'HE1', 'HE2'])

    def test_get_ile_cs_stat(self):
        self.assertEqual([stat['atom_id'] for stat in self.bmrb_cs_stat.get('ILE') if 'avg' in stat and stat['desc'] == 'methyl' and stat['atom_id'][0] == 'H'],
                         ['HD11', 'HD12', 'HD13', 'HG21', 'HG22', 'HG23'])

    def test_dc_h3_stat(self):
        h3c_stat = next(cs_stat for cs_stat in self.bmrb_cs_stat.get('DC') if cs_stat['atom_id'] == "H3'")
        self.assertTrue(h3c_stat['avg'] < 5.0)
        h3_stat = next((cs_stat for cs_stat in self.bmrb_cs_stat.get('DC') if cs_stat['atom_id'] == "H3"), None)
        self.assertIsNone(h3_stat)
        hn3_stat = next(cs_stat for cs_stat in self.bmrb_cs_stat.get('DNR') if cs_stat['atom_id'] == "HN3")
        self.assertTrue(hn3_stat['avg'] > 5.0)

    def test_c_h42_stat(self):
        h4c_stat = next(cs_stat for cs_stat in self.bmrb_cs_stat.get('C') if cs_stat['atom_id'] == "H4'")
        self.assertTrue(h4c_stat['avg'] < 5.0)
        h41_stat = next(cs_stat for cs_stat in self.bmrb_cs_stat.get('C') if cs_stat['atom_id'] == "H41")
        self.assertTrue(h41_stat['avg'] > 5.0)
        h42_stat = next(cs_stat for cs_stat in self.bmrb_cs_stat.get('C') if cs_stat['atom_id'] == "H42")
        self.assertTrue(h42_stat['avg'] > 5.0)


if __name__ == '__main__':
    unittest.main()
