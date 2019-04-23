from unittest import TestCase
import sys
import os
import pynmrstar

# Local imports
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
import NEFTranslator as NEFT


class TestNEFTranslator(TestCase):

    def test_readInFile(self):
        bt = NEFT.NEFTranslator()
        read_out = bt.readInFile('data/2mtv.nef')
        self.assertEqual(read_out[0], True)
        self.assertEqual(read_out[1], 'Entry')
        read_out = bt.readInFile('data/saveframeonly.nef')
        self.assertEqual(read_out[0], True)
        self.assertEqual(read_out[1], 'Saveframe')
        read_out = bt.readInFile('data/loopOnly1.nef')
        self.assertEqual(read_out[0], True)
        self.assertEqual(read_out[1], 'Loop')
        read_out = bt.readInFile('data/nonsense.nef')
        self.assertEqual(read_out[0], False)
        self.assertEqual(read_out[1],
                         'File contains no valid saveframe or loop. Invalid file PyNMRSTAR Error:'
                         '("Invalid token found in saveframe \'internaluseyoushouldntseethis_frame\': \'A\'", 2)')

    def test_load_atom_dict(self):
        bt = NEFT.NEFTranslator()
        self.assertTrue(len(bt.atomDict) > 0, "Can't read atomDict.json or its empty")

    def test_load_code_dict(self):
        bt = NEFT.NEFTranslator()
        self.assertTrue(len(bt.codeDict) > 0, "Can't read codeDict.json or its empty")

    def test_getOneLetter(self):
        bt = NEFT.NEFTranslator()
        self.assertTrue(bt.getOneLetter('ALA') == 'A')
        self.assertTrue(bt.getOneLetter('Ala') == 'A')
        self.assertTrue(bt.getOneLetter('Axy') == '?')

    def test_load_map_file(self):
        bt = NEFT.NEFTranslator()
        self.assertTrue(len(bt.tagMap) > 0, "Can't read NEF-NMRSTAR_equivalence.csv or its empty")

    def test_load_nef_info(self):
        bt = NEFT.NEFTranslator()
        self.assertTrue(len(bt.NEFinfo) > 0, "Can't read NEF_mandatory.csv or its empty")

    def test_TimeStamp(self):
        bt = NEFT.NEFTranslator()
        self.assertEqual(bt.TimeStamp(1556036192.7247672), '2019-04-23 11:16:32')

    def test_ValidateFile(self):
        bt = NEFT.NEFTranslator()
        self.assertEqual(bt.ValidateFile('data/xxx.xx', 'A')[0], False)  # File not found
        self.assertEqual(bt.ValidateFile('data/2l9r.nef', 'A')[0], True)
        self.assertEqual(bt.ValidateFile('data/2l9r.nef', 'S')[0], True)
        self.assertEqual(bt.ValidateFile('data/2l9r.nef', 'R')[0], True)
        self.assertEqual(bt.ValidateFile('data/2l9r.nef', 'X')[0], False)
        self.assertEqual(bt.ValidateFile('data/2l9r.str', 'A')[0], True)
        self.assertEqual(bt.ValidateFile('data/2l9r.str', 'S')[0], True)
        self.assertEqual(bt.ValidateFile('data/2l9r.str', 'R')[0], True)
        self.assertEqual(bt.ValidateFile('data/2l9r.str', 'X')[0], False)
        self.assertEqual(bt.ValidateFile('data/nocs.nef', 'A')[0], False)
        self.assertEqual(bt.ValidateFile('data/nocs.nef', 'S')[0], False)
        self.assertEqual(bt.ValidateFile('data/nocs.nef', 'R')[0], True)
        self.assertEqual(bt.ValidateFile('data/norest.nef', 'A')[0], False)
        self.assertEqual(bt.ValidateFile('data/norest.nef', 'S')[0], True)
        self.assertEqual(bt.ValidateFile('data/norest.nef', 'R')[0], False)
        self.assertEqual(bt.ValidateFile('data/norestcs.nef', 'A')[0], False)
        self.assertEqual(bt.ValidateFile('data/norestcs.nef', 'S')[0], False)
        self.assertEqual(bt.ValidateFile('data/norestcs.nef', 'R')[0], False)
        self.assertEqual(bt.ValidateFile('data/nocs.str', 'A')[0], False)
        self.assertEqual(bt.ValidateFile('data/nocs.str', 'S')[0], False)
        self.assertEqual(bt.ValidateFile('data/nocs.str', 'R')[0], True)
        self.assertEqual(bt.ValidateFile('data/norest.str', 'A')[0], False)
        self.assertEqual(bt.ValidateFile('data/norest.str', 'S')[0], True)
        self.assertEqual(bt.ValidateFile('data/norest.str', 'R')[0], False)
        self.assertEqual(bt.ValidateFile('data/norestcs.str', 'A')[0], False)
        self.assertEqual(bt.ValidateFile('data/norestcs.str', 'S')[0], False)
        self.assertEqual(bt.ValidateFile('data/norestcs.str', 'R')[0], False)
        self.assertEqual(bt.ValidateFile('data/nodat.str', 'R')[0], False)
        self.assertEqual(bt.ValidateFile('data/nodat.nef', 'R')[0], False)
        self.assertEqual(bt.ValidateFile('data/saveframeonly.nef', 'S')[0], True)
        self.assertEqual(bt.ValidateFile('data/loopOnly1.nef', 'S')[0], True)
        self.assertEqual(bt.ValidateFile('data/nonsense.nef', 'R')[0], False)

    def test_IsEmptyLoop(self):
        bt = NEFT.NEFTranslator()
        dat = pynmrstar.Entry.from_file('data/nodat.nef')
        self.assertEqual(bt.IsEmptyLoop(dat, '_nef_chemical_shift', 'Entry'), False)
        self.assertEqual(bt.IsEmptyLoop(dat, '_nef_distance_restraint', 'Entry'), True)
        dat = pynmrstar.Entry.from_file('data/nodat.str')
        self.assertEqual(bt.IsEmptyLoop(dat, '_Atom_chem_shift', 'Entry'), False)
        self.assertEqual(bt.IsEmptyLoop(dat, '_Gen_dist_constraint', 'Entry'), True)

    #
    # def test_GetSTARInfo(self):
    #     self.fail()
    #
    # def test_getSeqFromCS(self):
    #     self.fail()
    #
    def test_GetNEFSeq(self):
        bt = NEFT.NEFTranslator()
        dat = pynmrstar.Entry.from_file('data/2mqq.nef')
        self.assertEqual(bt.GetNEFSeq(dat), [{'A': ['TYR', 'GLY', 'HIS', 'ALA', 'ASP', 'SER', 'PRO', 'VAL', 'LEU',
                                                    'MET', 'VAL', 'TYR', 'GLY', 'LEU', 'ASP', 'GLN', 'SER', 'LYS',
                                                    'MET', 'ASN', 'CYS', 'ASP', 'ARG', 'VAL', 'PHE', 'ASN', 'VAL',
                                                    'PHE', 'CYS', 'LEU', 'TYR', 'GLY', 'ASN', 'VAL', 'GLU', 'LYS',
                                                    'VAL', 'LYS', 'PHE', 'MET', 'LYS', 'SER', 'LYS', 'PRO', 'GLY',
                                                    'ALA', 'ALA', 'MET', 'VAL', 'GLU', 'MET', 'ALA', 'ASP', 'GLY',
                                                    'TYR', 'ALA', 'VAL', 'ASP', 'ARG', 'ALA', 'ILE', 'THR', 'HIS',
                                                    'LEU', 'ASN', 'ASN', 'ASN', 'PHE', 'MET', 'PHE', 'GLY', 'GLN',
                                                    'LYS', 'MET', 'ASN', 'VAL', 'CYS', 'VAL', 'SER', 'LYS', 'GLN',
                                                    'PRO', 'ALA', 'ILE', 'MET', 'PRO', 'GLY', 'GLN', 'SER', 'TYR',
                                                    'GLY', 'LEU', 'GLU', 'ASP', 'GLY', 'SER', 'CYS', 'SER', 'TYR',
                                                    'LYS', 'ASP', 'PHE', 'SER', 'GLU', 'SER', 'ARG', 'ASN', 'ASN',
                                                    'ARG', 'PHE', 'SER', 'THR', 'PRO', 'GLU', 'GLN', 'ALA', 'ALA',
                                                    'LYS', 'ASN', 'ARG', 'ILE', 'GLN', 'HIS', 'PRO', 'SER', 'ASN',
                                                    'VAL', 'LEU', 'HIS', 'PHE', 'PHE', 'ASN', 'ALA', 'PRO', 'LEU',
                                                    'GLU', 'VAL', 'THR', 'GLU', 'GLU', 'ASN', 'PHE', 'PHE', 'GLU',
                                                    'ILE', 'CYS', 'ASP', 'GLU', 'LEU', 'GLY', 'VAL', 'LYS', 'ARG',
                                                    'PRO', 'THR', 'SER', 'VAL', 'LYS', 'VAL', 'PHE', 'SER', 'GLY',
                                                    'LYS', 'SER', 'GLU', 'ARG', 'SER', 'SER', 'SER', 'GLY', 'LEU',
                                                    'LEU', 'GLU', 'TRP', 'ASP', 'SER', 'LYS', 'SER', 'ASP', 'ALA',
                                                    'LEU', 'GLU', 'THR', 'LEU', 'GLY', 'PHE', 'LEU', 'ASN', 'HIS',
                                                    'TYR', 'GLN', 'MET', 'LYS', 'ASN', 'PRO', 'ASN', 'GLY', 'PRO',
                                                    'TYR', 'PRO', 'TYR', 'THR', 'LEU', 'LYS', 'LEU', 'CYS', 'PHE',
                                                    'SER', 'THR', 'ALA', 'GLN', 'HIS', 'ALA', 'SER']},
                                             {'B': ['A', 'C', 'A', 'C', 'A']},
                                             {'C': ['A', 'C', 'A', 'C', 'A']}])
        self.assertEqual(bt.GetNEFSeq(dat, 'nef_sequence', 'sequence_code', 'residue_name'),
                         [{'A': ['TYR', 'GLY', 'PRO', 'HIS', 'ALA', 'ASP', 'SER', 'PRO', 'VAL', 'LEU', 'MET', 'VAL',
                                 'TYR', 'GLY', 'LEU', 'ASP', 'GLN', 'SER', 'LYS', 'MET', 'ASN', 'CYS', 'ASP', 'ARG',
                                 'VAL', 'PHE', 'ASN', 'VAL', 'PHE', 'CYS', 'LEU', 'TYR', 'GLY', 'ASN', 'VAL', 'GLU',
                                 'LYS', 'VAL', 'LYS', 'PHE', 'MET', 'LYS', 'SER', 'LYS', 'PRO', 'GLY', 'ALA', 'ALA',
                                 'MET', 'VAL', 'GLU', 'MET', 'ALA', 'ASP', 'GLY', 'TYR', 'ALA', 'VAL', 'ASP', 'ARG',
                                 'ALA', 'ILE', 'THR', 'HIS', 'LEU', 'ASN', 'ASN', 'ASN', 'PHE', 'MET', 'PHE', 'GLY',
                                 'GLN', 'LYS', 'MET', 'ASN', 'VAL', 'CYS', 'VAL', 'SER', 'LYS', 'GLN', 'PRO', 'ALA',
                                 'ILE', 'MET', 'PRO', 'GLY', 'GLN', 'SER', 'TYR', 'GLY', 'LEU', 'GLU', 'ASP', 'GLY',
                                 'SER', 'CYS', 'SER', 'TYR', 'LYS', 'ASP', 'PHE', 'SER', 'GLU', 'SER', 'ARG', 'ASN',
                                 'ASN', 'ARG', 'PHE', 'SER', 'THR', 'PRO', 'GLU', 'GLN', 'ALA', 'ALA', 'LYS', 'ASN',
                                 'ARG', 'ILE', 'GLN', 'HIS', 'PRO', 'SER', 'ASN', 'VAL', 'LEU', 'HIS', 'PHE', 'PHE',
                                 'ASN', 'ALA', 'PRO', 'LEU', 'GLU', 'VAL', 'THR', 'GLU', 'GLU', 'ASN', 'PHE', 'PHE',
                                 'GLU', 'ILE', 'CYS', 'ASP', 'GLU', 'LEU', 'GLY', 'VAL', 'LYS', 'ARG', 'PRO', 'THR',
                                 'SER', 'VAL', 'LYS', 'VAL', 'PHE', 'SER', 'GLY', 'LYS', 'SER', 'GLU', 'ARG', 'SER',
                                 'SER', 'SER', 'GLY', 'LEU', 'LEU', 'GLU', 'TRP', 'ASP', 'SER', 'LYS', 'SER', 'ASP',
                                 'ALA', 'LEU', 'GLU', 'THR', 'LEU', 'GLY', 'PHE', 'LEU', 'ASN', 'HIS', 'TYR', 'GLN',
                                 'MET', 'LYS', 'ASN', 'PRO', 'ASN', 'GLY', 'PRO', 'TYR', 'PRO', 'TYR', 'THR', 'LEU',
                                 'LYS', 'LEU', 'CYS', 'PHE', 'SER', 'THR', 'ALA', 'GLN', 'HIS', 'ALA', 'SER'],
                           'C': ['A', 'C', 'A', 'C', 'A'], 'B': ['A', 'C', 'A', 'C', 'A']}])
        dat = bt.readInFile('data/saveframeonly.nef')[2]
        self.assertEqual(bt.GetNEFSeq(dat), [{'A': ['HIS', 'MET', 'SER', 'HIS', 'THR', 'GLN', 'VAL', 'ILE', 'GLU',
                                                    'LEU', 'GLU', 'ARG', 'LYS', 'PHE', 'SER', 'HIS', 'GLN', 'LYS',
                                                    'TYR', 'LEU', 'SER', 'ALA', 'PRO', 'GLU', 'ARG', 'ALA', 'HIS',
                                                    'LEU', 'ALA', 'LYS', 'ASN', 'LEU', 'LYS', 'LEU', 'THR', 'GLU',
                                                    'THR', 'GLN', 'VAL', 'LYS', 'ILE', 'TRP', 'PHE', 'GLN', 'ASN',
                                                    'ARG', 'ARG', 'TYR', 'LYS', 'THR', 'LYS', 'ARG', 'LYS', 'GLN',
                                                    'LEU', 'SER', 'SER', 'GLU', 'LEU', 'GLY']}])
        dat = bt.readInFile('data/loopOnly1.nef')[2]
        self.assertEqual(bt.GetNEFSeq(dat), [{'A': ['HIS', 'MET', 'ASN', 'SER', 'GLN', 'ARG', 'LEU', 'ILE', 'HIS',
                                                    'ILE', 'LYS', 'THR', 'LEU', 'THR', 'THR', 'PRO', 'ASN', 'GLU',
                                                    'ASN', 'ALA', 'LEU', 'LYS', 'PHE', 'LEU', 'SER', 'THR', 'ASP',
                                                    'GLY', 'GLU', 'MET', 'LEU', 'GLN', 'THR', 'ARG', 'GLY', 'SER',
                                                    'LYS', 'SER', 'ILE', 'VAL', 'ILE', 'LYS', 'ASN', 'THR', 'ASP',
                                                    'GLU', 'ASN', 'LEU', 'ILE', 'ASN', 'HIS', 'SER', 'LYS', 'LEU',
                                                    'ALA', 'GLN', 'GLN', 'ILE', 'PHE', 'LEU', 'GLN', 'CYS', 'PRO',
                                                    'GLY', 'VAL', 'GLU', 'SER', 'LEU', 'MET', 'ILE', 'GLY', 'ASP',
                                                    'ASP', 'PHE', 'LEU', 'THR', 'ILE', 'ASN', 'LYS', 'ASP', 'ARG',
                                                    'MET', 'VAL', 'HIS', 'TRP', 'ASN', 'SER', 'ILE', 'LYS', 'PRO',
                                                    'GLU', 'ILE', 'ILE', 'ASP', 'LEU', 'LEU', 'THR', 'LYS', 'GLN',
                                                    'LEU', 'ALA', 'TYR', 'GLY', 'GLU', 'ASP', 'VAL', 'ILE', 'SER',
                                                    'LYS', 'GLU']}])

    def test_GetNMRSTARSeq(self):
        bt = NEFT.NEFTranslator()
        dat = pynmrstar.Entry.from_file('data/2mqq.str')
        self.assertEqual(bt.GetNMRSTARSeq(dat),
                         [{'1': ['TYR', 'GLY', 'HIS', 'ALA', 'ASP', 'SER', 'PRO', 'VAL', 'LEU', 'MET', 'VAL', 'TYR',
                                 'GLY', 'LEU', 'ASP', 'GLN', 'SER', 'LYS', 'MET', 'ASN', 'CYS', 'ASP', 'ARG', 'VAL',
                                 'PHE', 'ASN', 'VAL', 'PHE', 'CYS', 'LEU', 'TYR', 'GLY', 'ASN', 'VAL', 'GLU', 'LYS',
                                 'VAL', 'LYS', 'PHE', 'MET', 'LYS', 'SER', 'LYS', 'PRO', 'GLY', 'ALA', 'ALA', 'MET',
                                 'VAL', 'GLU', 'MET', 'ALA', 'ASP', 'GLY', 'TYR', 'ALA', 'VAL', 'ASP', 'ARG', 'ALA',
                                 'ILE', 'THR', 'HIS', 'LEU', 'ASN', 'ASN', 'ASN', 'PHE', 'MET', 'PHE', 'GLY', 'GLN',
                                 'LYS', 'MET', 'ASN', 'VAL', 'CYS', 'VAL', 'SER', 'LYS', 'GLN', 'PRO', 'ALA', 'ILE',
                                 'MET', 'PRO', 'GLY', 'GLN', 'SER', 'TYR', 'GLY', 'LEU', 'GLU', 'ASP', 'GLY', 'SER',
                                 'CYS', 'SER', 'TYR', 'LYS', 'ASP', 'PHE', 'SER', 'GLU', 'SER', 'ARG', 'ASN', 'ASN',
                                 'ARG', 'PHE', 'SER', 'THR', 'PRO', 'GLU', 'GLN', 'ALA', 'ALA', 'LYS', 'ASN', 'ARG',
                                 'ILE', 'GLN', 'HIS', 'PRO', 'SER', 'ASN', 'VAL', 'LEU', 'HIS', 'PHE', 'PHE', 'ASN',
                                 'ALA', 'PRO', 'LEU', 'GLU', 'VAL', 'THR', 'GLU', 'GLU', 'ASN', 'PHE', 'PHE', 'GLU',
                                 'ILE', 'CYS', 'ASP', 'GLU', 'LEU', 'GLY', 'VAL', 'LYS', 'ARG', 'PRO', 'THR', 'SER',
                                 'VAL', 'LYS', 'VAL', 'PHE', 'SER', 'GLY', 'LYS', 'SER', 'GLU', 'ARG', 'SER', 'SER',
                                 'SER', 'GLY', 'LEU', 'LEU', 'GLU', 'TRP', 'ASP', 'SER', 'LYS', 'SER', 'ASP', 'ALA',
                                 'LEU', 'GLU', 'THR', 'LEU', 'GLY', 'PHE', 'LEU', 'ASN', 'HIS', 'TYR', 'GLN', 'MET',
                                 'LYS', 'ASN', 'PRO', 'ASN', 'GLY', 'PRO', 'TYR', 'PRO', 'TYR', 'THR', 'LEU', 'LYS',
                                 'LEU', 'CYS', 'PHE', 'SER', 'THR', 'ALA', 'GLN', 'HIS', 'ALA', 'SER']},
                          {'2': ['A', 'C', 'A', 'C', 'A']}, {'3': ['A', 'C', 'A', 'C', 'A']}])
        self.assertEqual(bt.GetNMRSTARSeq(dat, 'Chem_comp_assembly', 'Comp_index_ID', 'Comp_ID'),
                         [{'1': ['TYR', 'GLY', 'PRO', 'HIS', 'ALA', 'ASP', 'SER', 'PRO', 'VAL', 'LEU', 'MET', 'VAL',
                                 'TYR',
                                 'GLY', 'LEU', 'ASP', 'GLN', 'SER', 'LYS', 'MET', 'ASN', 'CYS', 'ASP', 'ARG', 'VAL',
                                 'PHE', 'ASN', 'VAL', 'PHE', 'CYS', 'LEU', 'TYR', 'GLY', 'ASN', 'VAL', 'GLU', 'LYS',
                                 'VAL', 'LYS', 'PHE', 'MET', 'LYS', 'SER', 'LYS', 'PRO', 'GLY', 'ALA', 'ALA', 'MET',
                                 'VAL', 'GLU', 'MET', 'ALA', 'ASP', 'GLY', 'TYR', 'ALA', 'VAL', 'ASP', 'ARG', 'ALA',
                                 'ILE', 'THR', 'HIS', 'LEU', 'ASN', 'ASN', 'ASN', 'PHE', 'MET', 'PHE', 'GLY', 'GLN',
                                 'LYS', 'MET', 'ASN', 'VAL', 'CYS', 'VAL', 'SER', 'LYS', 'GLN', 'PRO', 'ALA', 'ILE',
                                 'MET', 'PRO', 'GLY', 'GLN', 'SER', 'TYR', 'GLY', 'LEU', 'GLU', 'ASP', 'GLY', 'SER',
                                 'CYS', 'SER', 'TYR', 'LYS', 'ASP', 'PHE', 'SER', 'GLU', 'SER', 'ARG', 'ASN', 'ASN',
                                 'ARG', 'PHE', 'SER', 'THR', 'PRO', 'GLU', 'GLN', 'ALA', 'ALA', 'LYS', 'ASN', 'ARG',
                                 'ILE', 'GLN', 'HIS', 'PRO', 'SER', 'ASN', 'VAL', 'LEU', 'HIS', 'PHE', 'PHE', 'ASN',
                                 'ALA', 'PRO', 'LEU', 'GLU', 'VAL', 'THR', 'GLU', 'GLU', 'ASN', 'PHE', 'PHE', 'GLU',
                                 'ILE', 'CYS', 'ASP', 'GLU', 'LEU', 'GLY', 'VAL', 'LYS', 'ARG', 'PRO', 'THR', 'SER',
                                 'VAL', 'LYS', 'VAL', 'PHE', 'SER', 'GLY', 'LYS', 'SER', 'GLU', 'ARG', 'SER', 'SER',
                                 'SER', 'GLY', 'LEU', 'LEU', 'GLU', 'TRP', 'ASP', 'SER', 'LYS', 'SER', 'ASP', 'ALA',
                                 'LEU', 'GLU', 'THR', 'LEU', 'GLY', 'PHE', 'LEU', 'ASN', 'HIS', 'TYR', 'GLN', 'MET',
                                 'LYS', 'ASN', 'PRO', 'ASN', 'GLY', 'PRO', 'TYR', 'PRO', 'TYR', 'THR', 'LEU', 'LYS',
                                 'LEU', 'CYS', 'PHE', 'SER', 'THR', 'ALA', 'GLN', 'HIS', 'ALA', 'SER'],
                           '2': ['A', 'C', 'A', 'C', 'A'], '3': ['A', 'C', 'A', 'C', 'A']}])

    def test_ValidateAtom(self):
        bt = NEFT.NEFTranslator()
        dat = pynmrstar.Entry.from_file('data/2mqq.nef')
        self.assertEqual(len(bt.ValidateAtom(dat, 'nef_chemical_shift', 'sequence_code', 'residue_name', 'atom_name')),
                         567)
        self.assertEqual(
            len(bt.ValidateAtom(dat, 'nef_distance_restraint', 'sequence_code_1', 'residue_name_1', 'atom_name_1')),
            2960)
        self.assertEqual(
            len(bt.ValidateAtom(dat, 'nef_distance_restraint', 'sequence_code_2', 'residue_name_2', 'atom_name_2')),
            3147)
        dat = pynmrstar.Entry.from_file('data/2mqq.str')
        self.assertEqual(len(bt.ValidateAtom(dat)), 0)
        self.assertEqual(len(bt.ValidateAtom(dat, 'Gen_dist_constraint', 'Comp_index_ID_1', 'Comp_ID_1', 'Atom_ID_1')),
                         0)
        self.assertEqual(len(bt.ValidateAtom(dat, 'Gen_dist_constraint', 'Comp_index_ID_2', 'Comp_ID_2', 'Atom_ID_2')),
                         0)

    # def test_getNMRSTARtag(self):
    #     self.fail()
    #
    # def test_getNEFtag(self):
    #     self.fail()
    #
    # def test_getNMRSTARlooptags(self):
    #     self.fail()
    #
    def test_getSTARatom(self):
        bt = NEFT.NEFTranslator()
        self.assertEqual(bt.getSTARatom('CYS', 'HB%'), ('HB', ['HB2', 'HB3'], 1))
        self.assertEqual(bt.getSTARatom('TRP', 'CE%'), ('CE', ['CE2', 'CE3'], 1))
        self.assertEqual(bt.getSTARatom('TRP', 'CEX'), ('CE', ['CE2'], 2))
        self.assertEqual(bt.getSTARatom('TRP', 'CEY'), ('CE', ['CE3'], 2))
        self.assertEqual(bt.getSTARatom('LEU', 'HDY%'), ('HD', ['HD21', 'HD22', 'HD23'], 2))
        self.assertEqual(bt.getSTARatom('LEU', 'HD1%'), ('HD1', ['HD11', 'HD12', 'HD13'], 1))

    # def test_findAmbiguityCode(self):
    #     self.fail()
    #
    # def test_translate_cs_row(self):
    #     self.fail()
    #
    # def test_get_identifier(self):
    #     self.fail()
    #
    # def test_translate_row(self):
    #     self.fail()
    #
    # def test_translate_seq_row(self):
    #     self.fail()
    #
    # def test_translate_restraint_row(self):
    #     self.fail()
    #
    # def test_NEFtoNMRSTAR(self):
    #     self.fail()
