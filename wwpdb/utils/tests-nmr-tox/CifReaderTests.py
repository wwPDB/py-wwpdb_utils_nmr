##
# File: CifReaderTests.py
# Date: 02-Oct-2026  M. Yokochi
#
# Test that CifReader parses with SharingPdbxReader, which shares one str object among equal values,
# and that the parsed content is the same as that of mmcif's PdbxReader (DAOTHER-7829, 9785).
##
"""Test cases for the value sharing parse of CifReader."""
import os
import sys
import unittest

from mmcif.io.PdbxReader import PdbxReader

from wwpdb.utils.nmr.io.CifReader import CifReader, SharingPdbxReader

if __package__ is None or __package__ == "":
    from os import path

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from commonsetup import HERE, TESTOUTPUT  # noqa: F401 pylint: disable=import-error,unused-import
else:
    from .commonsetup import HERE, TESTOUTPUT  # noqa: F401 pylint: disable=relative-beyond-top-level

CIF_TEXT = """data_TEST
#
_entry.id TEST
#
loop_
_atom_site.group_PDB
_atom_site.id
_atom_site.type_symbol
_atom_site.label_atom_id
_atom_site.label_comp_id
_atom_site.label_asym_id
_atom_site.label_seq_id
_atom_site.Cartn_x
_atom_site.pdbx_PDB_model_num
ATOM 1 N N   ALA A 1 10.000 1
ATOM 2 C CA  ALA A 1 11.000 1
ATOM 3 C C   ALA A 1 12.000 1
ATOM 4 N N   GLY A 2 10.000 1
ATOM 5 C CA  GLY A 2 'C A' 1
ATOM 6 C C   GLY A 2 'C A' 1
#
_struct.title
;A multi-line
title
;
#
"""


def read_containers(readerClass, filePath):
    """Return the containers that readerClass parses from filePath."""

    containerList = []
    with open(filePath, 'r', encoding='utf-8') as ifh:
        readerClass(ifh).read(containerList)
    return containerList


def dump(containerList):
    """Return the content of the containers as comparable plain values."""

    return [(c.getType(), c.getName(),
             [(n, c.getObj(n).getAttributeList(), c.getObj(n).getRowList()) for n in c.getObjNameList()])
            for c in containerList]


class TestCifReader(unittest.TestCase):

    def setUp(self):
        self.cif_path = os.path.join(TESTOUTPUT, 'cif_reader_test.cif')
        with open(self.cif_path, 'w', encoding='utf-8') as ofh:
            ofh.write(CIF_TEXT)
        self.ccd_path = os.path.join(HERE, 'data', 'components', 'ligand-dict-v3', 'H', 'HEC', 'HEC.cif')

    def test_override_applies(self):
        # PdbxReader.read() calls self._PdbxReader__tokenizer; if mmcif renames it, the override is dead code
        self.assertTrue(hasattr(PdbxReader, '_PdbxReader__tokenizer'))
        self.assertIsNot(getattr(SharingPdbxReader, '_PdbxReader__tokenizer'), getattr(PdbxReader, '_PdbxReader__tokenizer'))

    def test_same_content_as_pdbx_reader(self):
        for filePath in (self.cif_path, self.ccd_path):
            with self.subTest(filePath=os.path.basename(filePath)):
                self.assertEqual(dump(read_containers(SharingPdbxReader, filePath)),
                                 dump(read_containers(PdbxReader, filePath)))

    def test_equal_values_are_shared(self):
        rows = read_containers(SharingPdbxReader, self.cif_path)[0].getObj('atom_site').getRowList()
        self.assertIs(rows[0][0], rows[5][0])  # ATOM
        self.assertIs(rows[0][3], rows[3][3])  # N
        self.assertIs(rows[0][7], rows[3][7])  # 10.000
        self.assertIs(rows[4][7], rows[5][7])  # quoted 'C A'
        # PdbxReader itself does not share them, so the identity above is the reader's doing
        _rows = read_containers(PdbxReader, self.cif_path)[0].getObj('atom_site').getRowList()
        self.assertIsNot(_rows[0][7], _rows[3][7])

    def test_cif_reader_parses_with_sharing(self):
        cR = CifReader(False, sys.stderr, use_cache=False)
        self.assertTrue(cR.parse(self.cif_path))
        atoms = cR.getDictList('atom_site')
        self.assertEqual([a['label_atom_id'] for a in atoms], ['N', 'CA', 'C', 'N', 'CA', 'C'])
        self.assertEqual(atoms[4]['Cartn_x'], 'C A')
        self.assertIs(atoms[0]['label_atom_id'], atoms[3]['label_atom_id'])
        self.assertIs(atoms[0]['Cartn_x'], atoms[3]['Cartn_x'])
        self.assertEqual(cR.getDictList('struct')[0]['title'], 'A multi-line\ntitle')


if __name__ == "__main__":
    unittest.main()
