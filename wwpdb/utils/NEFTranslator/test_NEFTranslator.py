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
        self.assertEqual(read_out[1], 'File contains no valid saveframe or loop. Invalid file PyNMRSTAR Error:("Invalid token found in saveframe \'internaluseyoushouldntseethis_frame\': \'A\'", 2)')


    # def test_load_atom_dict(self):
    #     self.fail()
    #
    # def test_load_code_dict(self):
    #     self.fail()
    #
    # def test_getOneLetter(self):
    #     self.fail()
    #
    # def test_load_map_file(self):
    #     self.fail()
    #
    # def test_load_nef_info(self):
    #     self.fail()
    #
    # def test_TimeStamp(self):
    #     self.fail()
    #
    # def test_ValidateFile(self):
    #     self.fail()
    #
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
        self.assertEqual(bt.GetNEFSeq(dat), [{
                                                 'A': u'YGHADSPVLMVYGLDQSKMNCDRVFNVFCLYGNVEKVKFMKSKPGAAMVEMADGYAVDRAITHLNNNFMFGQKMNVCVSKQPAIMPGQSYGLEDGSCSYKDFSESRNNRFSTPEQAAKNRIQHPSNVLHFFNAPLEVTEENFFEICDELGVKRPTSVKVFSGKSERSSSGLLEWDSKSDALETLGFLNHYQMKNPNGPYPYTLKLCFSTAQHAS'},
                                             {'B': 'ACACA'}, {'C': 'ACACA'}])
        self.assertEqual(bt.GetNEFSeq(dat, 'nef_sequence', 'sequence_code', 'residue_name'), [{
                                                                                                  'A': u'YGPHADSPVLMVYGLDQSKMNCDRVFNVFCLYGNVEKVKFMKSKPGAAMVEMADGYAVDRAITHLNNNFMFGQKMNVCVSKQPAIMPGQSYGLEDGSCSYKDFSESRNNRFSTPEQAAKNRIQHPSNVLHFFNAPLEVTEENFFEICDELGVKRPTSVKVFSGKSERSSSGLLEWDSKSDALETLGFLNHYQMKNPNGPYPYTLKLCFSTAQHAS',
                                                                                                  'C': u'ACACA',
                                                                                                  'B': u'ACACA'}])
        dat = bt.readInFile('data/saveframeonly.nef')[2]
        self.assertEqual(bt.GetNEFSeq(dat), [{'A': u'HMSHTQVIELERKFSHQKYLSAPERAHLAKNLKLTETQVKIWFQNRRYKTKRKQLSSELG'}])
        dat = bt.readInFile('data/loopOnly1.nef')[2]
        self.assertEqual(bt.GetNEFSeq(dat), [{
                                                 'A': u'HMNSQRLIHIKTLTTPNENALKFLSTDGEMLQTRGSKSIVIKNTDENLINHSKLAQQIFLQCPGVESLMIGDDFLTINKDRMVHWNSIKPEIIDLLTKQLAYGEDVISKE'}])

    #
    # def test_GetNMRSTARSeq(self):
    #     self.fail()
    #
    # def test_ValidateAtom(self):
    #     self.fail()
    #
    # def test_getNMRSTARtag(self):
    #     self.fail()
    #
    # def test_getNEFtag(self):
    #     self.fail()
    #
    # def test_getNMRSTARlooptags(self):
    #     self.fail()
    #
    # def test_getSTARatom(self):
    #     self.fail()
    #
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
