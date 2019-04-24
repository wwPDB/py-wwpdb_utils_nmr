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

    def test_getNMRSTARtag(self):
        bt = NEFT.NEFTranslator()
        self.assertEqual(bt.getNMRSTARtag('_nef_program_script.program_name'),
                         ['_Software_applied_methods.Software_name', '_Software_applied_methods.Software_name'])
        self.assertEqual(bt.getNMRSTARtag('_nef_program_script.script_name'),
                         ['_Software_applied_methods.Script_name', '_Software_applied_methods.Script_name'])
        self.assertEqual(bt.getNMRSTARtag('_nef_program_script.script'),
                         ['_Software_applied_methods.Script', '_Software_applied_methods.Script'])
        self.assertEqual(bt.getNMRSTARtag('_nef_sequence.index'),
                         ['_Chem_comp_assembly.NEF_index', '_Chem_comp_assembly.NEF_index'])
        self.assertEqual(bt.getNMRSTARtag('_nef_sequence.chain_code'),
                         ['_Chem_comp_assembly.Auth_asym_ID', '_Chem_comp_assembly.Entity_assembly_ID'])
        self.assertEqual(bt.getNMRSTARtag('_nef_sequence.sequence_code'),
                         ['_Chem_comp_assembly.Auth_seq_ID', '_Chem_comp_assembly.Comp_index_ID'])
        self.assertEqual(bt.getNMRSTARtag('_nef_sequence.residue_name'),
                         ['_Chem_comp_assembly.Auth_comp_ID', '_Chem_comp_assembly.Comp_ID'])
        self.assertEqual(bt.getNMRSTARtag('_nef_sequence.linking'),
                         ['_Chem_comp_assembly.Sequence_linking', '_Chem_comp_assembly.Sequence_linking'])
        self.assertEqual(bt.getNMRSTARtag('_nef_sequence.residue_variant'),
                         ['_Chem_comp_assembly.Auth_variant_ID', '_Chem_comp_assembly.Auth_variant_ID'])
        self.assertEqual(bt.getNMRSTARtag('_nef_sequence.cis_peptide'),
                         ['_Chem_comp_assembly.Cis_residue', '_Chem_comp_assembly.Cis_residue'])
        self.assertEqual(bt.getNMRSTARtag('_nef_chemical_shift.chain_code'),
                         ['_Atom_chem_shift.Auth_asym_ID', '_Atom_chem_shift.Entity_assembly_ID'])
        self.assertEqual(bt.getNMRSTARtag('_nef_chemical_shift.sequence_code'),
                         ['_Atom_chem_shift.Auth_seq_ID', '_Atom_chem_shift.Comp_index_ID'])
        self.assertEqual(bt.getNMRSTARtag('_nef_chemical_shift.residue_name'),
                         ['_Atom_chem_shift.Auth_comp_ID', '_Atom_chem_shift.Comp_ID'])
        self.assertEqual(bt.getNMRSTARtag('_nef_chemical_shift.atom_name'),
                         ['_Atom_chem_shift.Auth_atom_ID', '_Atom_chem_shift.Atom_ID'])
        self.assertEqual(bt.getNMRSTARtag('_nef_chemical_shift.value'),
                         ['_Atom_chem_shift.Val', '_Atom_chem_shift.Val'])
        self.assertEqual(bt.getNMRSTARtag('_nef_chemical_shift.value_uncertainty'),
                         ['_Atom_chem_shift.Val_err', '_Atom_chem_shift.Val_err'])
        self.assertEqual(bt.getNMRSTARtag('_nef_chemical_shift.element'),
                         ['_Atom_chem_shift.Atom_type', '_Atom_chem_shift.Atom_type'])
        self.assertEqual(bt.getNMRSTARtag('_nef_chemical_shift.isotope_number'),
                         ['_Atom_chem_shift.Atom_isotope_number', '_Atom_chem_shift.Atom_isotope_number'])
        self.assertEqual(bt.getNMRSTARtag('_nef_chemical_shift.chain_code'),
                         ['_Atom_chem_shift.Auth_asym_ID', '_Atom_chem_shift.Entity_assembly_ID'])
        self.assertEqual(bt.getNMRSTARtag('_nef_chemical_shift.sequence_code'),
                         ['_Atom_chem_shift.Auth_seq_ID', '_Atom_chem_shift.Comp_index_ID'])
        self.assertEqual(bt.getNMRSTARtag('_nef_chemical_shift.residue_name'),
                         ['_Atom_chem_shift.Auth_comp_ID', '_Atom_chem_shift.Comp_ID'])
        self.assertEqual(bt.getNMRSTARtag('_nef_chemical_shift.atom_name'),
                         ['_Atom_chem_shift.Auth_atom_ID', '_Atom_chem_shift.Atom_ID'])
        self.assertEqual(bt.getNMRSTARtag('_nef_chemical_shift.value'),
                         ['_Atom_chem_shift.Val', '_Atom_chem_shift.Val'])
        self.assertEqual(bt.getNMRSTARtag('_nef_chemical_shift.value_uncertainty'),
                         ['_Atom_chem_shift.Val_err', '_Atom_chem_shift.Val_err'])
        self.assertEqual(bt.getNMRSTARtag('_nef_chemical_shift.element'),
                         ['_Atom_chem_shift.Atom_type', '_Atom_chem_shift.Atom_type'])
        self.assertEqual(bt.getNMRSTARtag('_nef_chemical_shift.isotope_number'),
                         ['_Atom_chem_shift.Atom_isotope_number', '_Atom_chem_shift.Atom_isotope_number'])
        self.assertEqual(bt.getNMRSTARtag('_nef_chemical_shift.chain_code'),
                         ['_Atom_chem_shift.Auth_asym_ID', '_Atom_chem_shift.Entity_assembly_ID'])
        self.assertEqual(bt.getNMRSTARtag('_nef_chemical_shift.sequence_code'),
                         ['_Atom_chem_shift.Auth_seq_ID', '_Atom_chem_shift.Comp_index_ID'])
        self.assertEqual(bt.getNMRSTARtag('_nef_chemical_shift.residue_name'),
                         ['_Atom_chem_shift.Auth_comp_ID', '_Atom_chem_shift.Comp_ID'])
        self.assertEqual(bt.getNMRSTARtag('_nef_chemical_shift.atom_name'),
                         ['_Atom_chem_shift.Auth_atom_ID', '_Atom_chem_shift.Atom_ID'])
        self.assertEqual(bt.getNMRSTARtag('_nef_chemical_shift.value'),
                         ['_Atom_chem_shift.Val', '_Atom_chem_shift.Val'])
        self.assertEqual(bt.getNMRSTARtag('_nef_chemical_shift.value_uncertainty'),
                         ['_Atom_chem_shift.Val_err', '_Atom_chem_shift.Val_err'])
        self.assertEqual(bt.getNMRSTARtag('_nef_chemical_shift.element'),
                         ['_Atom_chem_shift.Atom_type', '_Atom_chem_shift.Atom_type'])
        self.assertEqual(bt.getNMRSTARtag('_nef_chemical_shift.isotope_number'),
                         ['_Atom_chem_shift.Atom_isotope_number', '_Atom_chem_shift.Atom_isotope_number'])
        self.assertEqual(bt.getNMRSTARtag('_nef_distance_restraint.index'),
                         ['_Gen_dist_constraint.Index_ID', '_Gen_dist_constraint.Index_ID'])
        self.assertEqual(bt.getNMRSTARtag('_nef_distance_restraint.restraint_id'),
                         ['_Gen_dist_constraint.ID', '_Gen_dist_constraint.ID'])
        self.assertEqual(bt.getNMRSTARtag('_nef_distance_restraint.restraint_combination_id'),
                         ['_Gen_dist_constraint.Combination_ID', '_Gen_dist_constraint.Combination_ID'])
        self.assertEqual(bt.getNMRSTARtag('_nef_distance_restraint.chain_code_1'),
                         ['_Gen_dist_constraint.Auth_asym_ID_1', '_Gen_dist_constraint.Entity_assembly_ID_1'])
        self.assertEqual(bt.getNMRSTARtag('_nef_distance_restraint.sequence_code_1'),
                         ['_Gen_dist_constraint.Auth_seq_ID_1', '_Gen_dist_constraint.Comp_index_ID_1'])
        self.assertEqual(bt.getNMRSTARtag('_nef_distance_restraint.residue_name_1'),
                         ['_Gen_dist_constraint.Auth_comp_ID_1', '_Gen_dist_constraint.Comp_ID_1'])
        self.assertEqual(bt.getNMRSTARtag('_nef_distance_restraint.atom_name_1'),
                         ['_Gen_dist_constraint.Auth_atom_ID_1', '_Gen_dist_constraint.Atom_ID_1'])
        self.assertEqual(bt.getNMRSTARtag('_nef_distance_restraint.chain_code_2'),
                         ['_Gen_dist_constraint.Auth_asym_ID_2', '_Gen_dist_constraint.Entity_assembly_ID_2'])
        self.assertEqual(bt.getNMRSTARtag('_nef_distance_restraint.sequence_code_2'),
                         ['_Gen_dist_constraint.Auth_seq_ID_2', '_Gen_dist_constraint.Comp_index_ID_2'])
        self.assertEqual(bt.getNMRSTARtag('_nef_distance_restraint.residue_name_2'),
                         ['_Gen_dist_constraint.Auth_comp_ID_2', '_Gen_dist_constraint.Comp_ID_2'])
        self.assertEqual(bt.getNMRSTARtag('_nef_distance_restraint.atom_name_2'),
                         ['_Gen_dist_constraint.Auth_atom_ID_2', '_Gen_dist_constraint.Atom_ID_2'])
        self.assertEqual(bt.getNMRSTARtag('_nef_distance_restraint.weight'),
                         ['_Gen_dist_constraint.Weight', '_Gen_dist_constraint.Weight'])
        self.assertEqual(bt.getNMRSTARtag('_nef_distance_restraint.target_value'),
                         ['_Gen_dist_constraint.Target_val', '_Gen_dist_constraint.Target_val'])
        self.assertEqual(bt.getNMRSTARtag('_nef_distance_restraint.target_value_uncertainty'),
                         ['_Gen_dist_constraint.Target_val_uncertainty', '_Gen_dist_constraint.Target_val_uncertainty'])
        self.assertEqual(bt.getNMRSTARtag('_nef_distance_restraint.lower_linear_limit'),
                         ['_Gen_dist_constraint.Lower_linear_limit', '_Gen_dist_constraint.Lower_linear_limit'])
        self.assertEqual(bt.getNMRSTARtag('_nef_distance_restraint.lower_limit'),
                         ['_Gen_dist_constraint.Distance_lower_bound_val',
                          '_Gen_dist_constraint.Distance_lower_bound_val'])
        self.assertEqual(bt.getNMRSTARtag('_nef_distance_restraint.upper_limit'),
                         ['_Gen_dist_constraint.Distance_upper_bound_val',
                          '_Gen_dist_constraint.Distance_upper_bound_val'])
        self.assertEqual(bt.getNMRSTARtag('_nef_distance_restraint.upper_linear_limit'),
                         ['_Gen_dist_constraint.Upper_linear_limit', '_Gen_dist_constraint.Upper_linear_limit'])


    def test_getNMRSTARlooptags(self):
        bt = NEFT.NEFTranslator()
        self.assertEqual(bt.getNMRSTARlooptags(
            ['_nef_program_script.program_name', '_nef_program_script.script_name', '_nef_program_script.script']),
                         ['_Software_applied_methods.Software_name', '_Software_applied_methods.Script_name',
                          '_Software_applied_methods.Script'])
        self.assertEqual(bt.getNMRSTARlooptags(
            ['_nef_sequence.index', '_nef_sequence.chain_code', '_nef_sequence.sequence_code',
             '_nef_sequence.residue_name', '_nef_sequence.linking', '_nef_sequence.residue_variant',
             '_nef_sequence.cis_peptide']), ['_Chem_comp_assembly.NEF_index', '_Chem_comp_assembly.Auth_asym_ID',
                                             '_Chem_comp_assembly.Auth_seq_ID', '_Chem_comp_assembly.Auth_comp_ID',
                                             '_Chem_comp_assembly.Sequence_linking',
                                             '_Chem_comp_assembly.Auth_variant_ID', '_Chem_comp_assembly.Cis_residue',
                                             '_Chem_comp_assembly.Entity_assembly_ID',
                                             '_Chem_comp_assembly.Comp_index_ID', '_Chem_comp_assembly.Comp_ID'])
        self.assertEqual(bt.getNMRSTARlooptags(
            ['_nef_chemical_shift.chain_code', '_nef_chemical_shift.sequence_code', '_nef_chemical_shift.residue_name',
             '_nef_chemical_shift.atom_name', '_nef_chemical_shift.value', '_nef_chemical_shift.value_uncertainty',
             '_nef_chemical_shift.element', '_nef_chemical_shift.isotope_number']),
                         ['_Atom_chem_shift.Auth_asym_ID', '_Atom_chem_shift.Auth_seq_ID',
                          '_Atom_chem_shift.Auth_comp_ID', '_Atom_chem_shift.Auth_atom_ID', '_Atom_chem_shift.Val',
                          '_Atom_chem_shift.Val_err', '_Atom_chem_shift.Atom_type',
                          '_Atom_chem_shift.Atom_isotope_number', '_Atom_chem_shift.Entity_assembly_ID',
                          '_Atom_chem_shift.Comp_index_ID', '_Atom_chem_shift.Comp_ID', '_Atom_chem_shift.Atom_ID',
                          '_Atom_chem_shift.Ambiguity_code', '_Atom_chem_shift.Ambiguity_set_ID',
                          '_Atom_chem_shift.Assigned_chem_shift_list_ID'])
        self.assertEqual(bt.getNMRSTARlooptags(
            ['_nef_chemical_shift.chain_code', '_nef_chemical_shift.sequence_code', '_nef_chemical_shift.residue_name',
             '_nef_chemical_shift.atom_name', '_nef_chemical_shift.value', '_nef_chemical_shift.value_uncertainty',
             '_nef_chemical_shift.element', '_nef_chemical_shift.isotope_number']),
                         ['_Atom_chem_shift.Auth_asym_ID', '_Atom_chem_shift.Auth_seq_ID',
                          '_Atom_chem_shift.Auth_comp_ID', '_Atom_chem_shift.Auth_atom_ID', '_Atom_chem_shift.Val',
                          '_Atom_chem_shift.Val_err', '_Atom_chem_shift.Atom_type',
                          '_Atom_chem_shift.Atom_isotope_number', '_Atom_chem_shift.Entity_assembly_ID',
                          '_Atom_chem_shift.Comp_index_ID', '_Atom_chem_shift.Comp_ID', '_Atom_chem_shift.Atom_ID',
                          '_Atom_chem_shift.Ambiguity_code', '_Atom_chem_shift.Ambiguity_set_ID',
                          '_Atom_chem_shift.Assigned_chem_shift_list_ID'])
        self.assertEqual(bt.getNMRSTARlooptags(
            ['_nef_chemical_shift.chain_code', '_nef_chemical_shift.sequence_code', '_nef_chemical_shift.residue_name',
             '_nef_chemical_shift.atom_name', '_nef_chemical_shift.value', '_nef_chemical_shift.value_uncertainty',
             '_nef_chemical_shift.element', '_nef_chemical_shift.isotope_number']),
                         ['_Atom_chem_shift.Auth_asym_ID', '_Atom_chem_shift.Auth_seq_ID',
                          '_Atom_chem_shift.Auth_comp_ID', '_Atom_chem_shift.Auth_atom_ID', '_Atom_chem_shift.Val',
                          '_Atom_chem_shift.Val_err', '_Atom_chem_shift.Atom_type',
                          '_Atom_chem_shift.Atom_isotope_number', '_Atom_chem_shift.Entity_assembly_ID',
                          '_Atom_chem_shift.Comp_index_ID', '_Atom_chem_shift.Comp_ID', '_Atom_chem_shift.Atom_ID',
                          '_Atom_chem_shift.Ambiguity_code', '_Atom_chem_shift.Ambiguity_set_ID',
                          '_Atom_chem_shift.Assigned_chem_shift_list_ID'])
        self.assertEqual(bt.getNMRSTARlooptags(['_nef_distance_restraint.index', '_nef_distance_restraint.restraint_id',
                                                '_nef_distance_restraint.restraint_combination_id',
                                                '_nef_distance_restraint.chain_code_1',
                                                '_nef_distance_restraint.sequence_code_1',
                                                '_nef_distance_restraint.residue_name_1',
                                                '_nef_distance_restraint.atom_name_1',
                                                '_nef_distance_restraint.chain_code_2',
                                                '_nef_distance_restraint.sequence_code_2',
                                                '_nef_distance_restraint.residue_name_2',
                                                '_nef_distance_restraint.atom_name_2', '_nef_distance_restraint.weight',
                                                '_nef_distance_restraint.target_value',
                                                '_nef_distance_restraint.target_value_uncertainty',
                                                '_nef_distance_restraint.lower_linear_limit',
                                                '_nef_distance_restraint.lower_limit',
                                                '_nef_distance_restraint.upper_limit',
                                                '_nef_distance_restraint.upper_linear_limit']),
                         ['_Gen_dist_constraint.Index_ID', '_Gen_dist_constraint.ID',
                          '_Gen_dist_constraint.Combination_ID', '_Gen_dist_constraint.Auth_asym_ID_1',
                          '_Gen_dist_constraint.Auth_seq_ID_1', '_Gen_dist_constraint.Auth_comp_ID_1',
                          '_Gen_dist_constraint.Auth_atom_ID_1', '_Gen_dist_constraint.Auth_asym_ID_2',
                          '_Gen_dist_constraint.Auth_seq_ID_2', '_Gen_dist_constraint.Auth_comp_ID_2',
                          '_Gen_dist_constraint.Auth_atom_ID_2', '_Gen_dist_constraint.Weight',
                          '_Gen_dist_constraint.Target_val', '_Gen_dist_constraint.Target_val_uncertainty',
                          '_Gen_dist_constraint.Lower_linear_limit', '_Gen_dist_constraint.Distance_lower_bound_val',
                          '_Gen_dist_constraint.Distance_upper_bound_val', '_Gen_dist_constraint.Upper_linear_limit',
                          '_Gen_dist_constraint.Entity_assembly_ID_1', '_Gen_dist_constraint.Comp_index_ID_1',
                          '_Gen_dist_constraint.Comp_ID_1', '_Gen_dist_constraint.Atom_ID_1',
                          '_Gen_dist_constraint.Entity_assembly_ID_2', '_Gen_dist_constraint.Comp_index_ID_2',
                          '_Gen_dist_constraint.Comp_ID_2', '_Gen_dist_constraint.Atom_ID_2',
                          '_Gen_dist_constraint.Member_logic_code'])

    def test_getSTARatom(self):
        bt = NEFT.NEFTranslator()
        self.assertEqual(bt.getSTARatom('CYS', 'HB%'), ('HB', ['HB2', 'HB3'], 1))
        self.assertEqual(bt.getSTARatom('TRP', 'CE%'), ('CE', ['CE2', 'CE3'], 1))
        self.assertEqual(bt.getSTARatom('TRP', 'CEX'), ('CE', ['CE2'], 2))
        self.assertEqual(bt.getSTARatom('TRP', 'CEY'), ('CE', ['CE3'], 2))
        self.assertEqual(bt.getSTARatom('LEU', 'HDY%'), ('HD', ['HD21', 'HD22', 'HD23'], 2))
        self.assertEqual(bt.getSTARatom('LEU', 'HD1%'), ('HD1', ['HD11', 'HD12', 'HD13'], 1))


    def test_translate_cs_row(self):
        bt = NEFT.NEFTranslator()
        bt.NEFtoNMRSTAR('data/2mqq.nef')
        input_tags = ['_nef_chemical_shift.chain_code', '_nef_chemical_shift.sequence_code',
                      '_nef_chemical_shift.residue_name', '_nef_chemical_shift.atom_name',
                      '_nef_chemical_shift.value', '_nef_chemical_shift.value_uncertainty',
                      '_nef_chemical_shift.element', '_nef_chemical_shift.isotope_number']
        output_tags = ['_Atom_chem_shift.Auth_asym_ID', '_Atom_chem_shift.Auth_seq_ID',
                       '_Atom_chem_shift.Auth_comp_ID', '_Atom_chem_shift.Auth_atom_ID',
                       '_Atom_chem_shift.Val', '_Atom_chem_shift.Val_err', '_Atom_chem_shift.Atom_type',
                       '_Atom_chem_shift.Atom_isotope_number', '_Atom_chem_shift.Entity_assembly_ID',
                       '_Atom_chem_shift.Comp_index_ID', '_Atom_chem_shift.Comp_ID', '_Atom_chem_shift.Atom_ID',
                       '_Atom_chem_shift.Ambiguity_code', '_Atom_chem_shift.Ambiguity_set_ID',
                       '_Atom_chem_shift.Assigned_chem_shift_list_ID']
        data = ['A', '484', 'THR', 'N', '108.193', '0.4', 'N', '15']
        data_out = [['A', '484', 'THR', 'N', '108.193', '0.4', 'N', '15', 1, 113, 'THR', 'N', 1, '.', None]]
        self.assertEqual(bt.translate_cs_row(input_tags,output_tags,data),data_out)
        data = ['A', '488', 'ALA', 'HB%', '1.625', '0.02', 'H', '1']
        data_out = [['A', '488', 'ALA', 'HB%', '1.625', '0.02', 'H', '1', 1, 117, 'ALA', u'HB1', 1, '.', None],
                    ['A', '488', 'ALA', 'HB%', '1.625', '0.02', 'H', '1', 1, 117, 'ALA', u'HB2', 1, '.', None],
                    ['A', '488', 'ALA', 'HB%', '1.625', '0.02', 'H', '1', 1, 117, 'ALA', u'HB3', 1, '.', None]]
        self.assertEqual(bt.translate_cs_row(input_tags, output_tags, data), data_out)
        data = ['A', '493', 'ILE', 'HD1%', '0.996', '0.02', 'H', '1']
        data_out = [['A', '493', 'ILE', 'HD1%', '0.996', '0.02', 'H', '1', 1, 122, 'ILE', u'HD11', 1, '.', None],
                    ['A', '493', 'ILE', 'HD1%', '0.996', '0.02', 'H', '1', 1, 122, 'ILE', u'HD12', 1, '.', None],
                    ['A', '493', 'ILE', 'HD1%', '0.996', '0.02', 'H', '1', 1, 122, 'ILE', u'HD13', 1, '.', None]]
        self.assertEqual(bt.translate_cs_row(input_tags, output_tags, data), data_out)
        data = ['A', '493', 'ILE', 'HG1x', '1.627', '0.02', 'H', '1']
        data_out = [['A', '493', 'ILE', 'HG1x', '1.627', '0.02', 'H', '1', 1, 122, 'ILE', u'HG12', 2, '.', None]]
        self.assertEqual(bt.translate_cs_row(input_tags, output_tags, data), data_out)
        data = ['A', '493', 'ILE', 'HG1y', '1.536', '0.02', 'H', '1']
        data_out = [['A', '493', 'ILE', 'HG1y', '1.536', '0.02', 'H', '1', 1, 122, 'ILE', u'HG13', 2, '.', None]]
        self.assertEqual(bt.translate_cs_row(input_tags, output_tags, data), data_out)
        data = ['A', '493', 'ILE', 'HG2%', '0.859', '0.02', 'H', '1']
        data_out = [['A', '493', 'ILE', 'HG2%', '0.859', '0.02', 'H', '1', 1, 122, 'ILE', u'HG21', 1, '.', None],
                    ['A', '493', 'ILE', 'HG2%', '0.859', '0.02', 'H', '1', 1, 122, 'ILE', u'HG22', 1, '.', None],
                    ['A', '493', 'ILE', 'HG2%', '0.859', '0.02', 'H', '1', 1, 122, 'ILE', u'HG23', 1, '.', None]]
        self.assertEqual(bt.translate_cs_row(input_tags, output_tags, data), data_out)

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
