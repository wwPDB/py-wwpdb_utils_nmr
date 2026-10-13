##
# File: PseudoChemCompTests.py
# Date: 03-Oct-2026  M. Yokochi
#
# Test the pseudo CCD that is derived from the coordinates of a non-standard residue (DAOTHER-8817):
# heavy atoms are bonded by covalent radii, and ambiguity code 3 (ring flip) is guessed in reference to
# phenylalanine, using the ideal and model coordinates of the test CCD without its bond table.
##
"""Test cases for buildPseudoChemCompBond(), isFlippableRingProtonHost() and their use by NefTranslator."""
import glob
import math
import os
import sys
import unittest

import numpy

from mmcif.io.PdbxReader import PdbxReader

# import commonsetup first: it mocks ConfigInfo, which ChemCompUtil reads when it is imported
if __package__ is None or __package__ == "":
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from commonsetup import HERE, TESTOUTPUT  # noqa: F401 pylint: disable=import-error,unused-import
else:
    from .commonsetup import HERE, TESTOUTPUT  # noqa: F401 pylint: disable=relative-beyond-top-level

from wwpdb.utils.nmr.mr.ParserListenerUtil import (buildPseudoChemCompBond,
                                                   isFlippableRingProtonHost)
from wwpdb.utils.nmr.nef.NefTranslator import NefTranslator

CCD_DIR = os.path.join(HERE, 'data', 'components', 'ligand-dict-v3')

# heavy atoms whose proton has ambiguity code 3
RING_FLIP_HOSTS = {'PHE': ['CD1', 'CD2', 'CE1', 'CE2'],
                   'TYR': ['CD1', 'CD2', 'CE1', 'CE2']}


def read_residue(compId, coordKind='pdbx_model_Cartn_{}_ideal'):
    """Return the atom_ids, type_symbols, coordinates and CCD bonds of a CCD file of the test data."""

    containerList = []
    with open(os.path.join(CCD_DIR, compId[0], compId, f'{compId}.cif'), 'r', encoding='utf-8') as ifh:
        PdbxReader(ifh).read(containerList)
    atoms = containerList[0].getObj('chem_comp_atom')
    bonds = containerList[0].getObj('chem_comp_bond')

    atomIds, typeSymbols, coords = [], [], {}
    for row in atoms.getRowList():
        try:
            xyz = numpy.array([float(row[atoms.getAttributeIndex(coordKind.format(c))]) for c in 'xyz'])
        except (ValueError, TypeError):
            continue
        atomId = row[atoms.getAttributeIndex('atom_id')]
        atomIds.append(atomId)
        typeSymbols.append(row[atoms.getAttributeIndex('type_symbol')])
        coords[atomId] = xyz

    ccdBonds = set()
    if bonds is not None:
        for row in bonds.getRowList():
            ccdBonds.add(frozenset((row[bonds.getAttributeIndex('atom_id_1')], row[bonds.getAttributeIndex('atom_id_2')])))

    return atomIds, typeSymbols, coords, ccdBonds


def ring_flip_hosts(atomIds, typeSymbols, coords):
    """Return the heavy atoms with one proton that isFlippableRingProtonHost() accepts."""

    bond, topo = buildPseudoChemCompBond(atomIds, typeSymbols, coords)
    return sorted(k for k, v in bond.items() if len(v) == 1 and k[0] == 'C' and isFlippableRingProtonHost(topo, bond, k))


class TestPseudoChemComp(unittest.TestCase):

    def test_heavy_atom_bonds_match_ccd(self):
        # a flat 2.5 A cutoff also bonded most atoms two bonds apart, e.g. CG-CE1 of PHE
        for compId in ('PHE', 'TYR', 'TRP', 'HIS'):
            with self.subTest(compId=compId):
                atomIds, typeSymbols, coords, ccdBonds = read_residue(compId)
                _, topo = buildPseudoChemCompBond(atomIds, typeSymbols, coords)
                found = {frozenset((a, b)) for a, nbrs in topo.items() for b in nbrs}
                heavy = {a for a, t in zip(atomIds, typeSymbols) if t != 'H'}
                expected = {p for p in ccdBonds if p <= heavy}
                self.assertEqual(found, expected)

    def test_ring_flip_hosts_in_reference_to_phenylalanine(self):
        for coordKind in ('pdbx_model_Cartn_{}_ideal', 'model_Cartn_{}'):
            for compId in ('PHE', 'TYR', 'TRP', 'HIS'):
                with self.subTest(compId=compId, coordKind=coordKind):
                    atomIds, typeSymbols, coords, _ = read_residue(compId, coordKind)
                    self.assertEqual(ring_flip_hosts(atomIds, typeSymbols, coords), RING_FLIP_HOSTS.get(compId, []))

    def test_no_ring_flip_hosts_elsewhere(self):
        # e.g. nucleotides, heme and the ring CH of tryptophan are not flippable rings
        for path in sorted(glob.glob(os.path.join(CCD_DIR, '*', '*', '*.cif'))):
            compId = os.path.basename(path)[:-4]
            if compId in RING_FLIP_HOSTS:
                continue
            with self.subTest(compId=compId):
                atomIds, typeSymbols, coords, _ = read_residue(compId)
                if len(atomIds) > 0:
                    self.assertEqual(ring_flip_hosts(atomIds, typeSymbols, coords), [])

    def test_nef_translator_guesses_ambiguity_code_from_pseudo_phe(self):
        # phenylalanine under a comp_id unknown to the CCD, so that NefTranslator falls back to the pseudo CCD
        atomIds, typeSymbols, coords, _ = read_residue('PHE')
        bond, topo = buildPseudoChemCompBond(atomIds, typeSymbols, coords)
        compId = 'XXX'
        neft = NefTranslator()
        neft.set_chem_comp_dict({compId: atomIds}, {compId: bond}, {compId: topo}, {})
        coordAtomSite = {'atom_id': atomIds, 'alt_atom_id': atomIds}
        for nefAtom, expected in (('HD%', (['HD1', 'HD2'], 3)),
                                  ('HE%', (['HE1', 'HE2'], 3)),
                                  ('HZ', (['HZ'], 1)),
                                  ('HB%', (['HB2', 'HB3'], 2))):
            with self.subTest(nefAtom=nefAtom):
                self.assertEqual(neft.get_star_atom_for_ligand_remap(compId, nefAtom, None, coordAtomSite)[:2], expected)

    def test_nef_translator_guesses_ambiguity_code_from_pseudo_tyr(self):
        # tyrosine under a comp_id unknown to the CCD, so that NefTranslator falls back to the pseudo CCD
        atomIds, typeSymbols, coords, _ = read_residue('TYR')
        bond, topo = buildPseudoChemCompBond(atomIds, typeSymbols, coords)
        compId = 'XXX'
        neft = NefTranslator()
        neft.set_chem_comp_dict({compId: atomIds}, {compId: bond}, {compId: topo}, {})
        coordAtomSite = {'atom_id': atomIds, 'alt_atom_id': atomIds}
        for nefAtom, expected in (('HD%', (['HD1', 'HD2'], 3)),
                                  ('HE%', (['HE1', 'HE2'], 3)),
                                  ('HH', (['HH'], 1)),
                                  ('HB%', (['HB2', 'HB3'], 2))):
            with self.subTest(nefAtom=nefAtom):
                self.assertEqual(neft.get_star_atom_for_ligand_remap(compId, nefAtom, None, coordAtomSite)[:2], expected)

    def test_nef_translator_guesses_ambiguity_code_from_pseudo_his(self):
        # histidine under a comp_id unknown to the CCD, so that NefTranslator falls back to the pseudo CCD
        atomIds, typeSymbols, coords, _ = read_residue('HIS')
        bond, topo = buildPseudoChemCompBond(atomIds, typeSymbols, coords)
        compId = 'XXX'
        neft = NefTranslator()
        neft.set_chem_comp_dict({compId: atomIds}, {compId: bond}, {compId: topo}, {})
        coordAtomSite = {'atom_id': atomIds, 'alt_atom_id': atomIds}
        for nefAtom, expected in (('HD%', (['HD1', 'HD2'], 1)),
                                  ('HE%', (['HE1', 'HE2'], 1)),
                                  ('HB%', (['HB2', 'HB3'], 2))):
            with self.subTest(nefAtom=nefAtom):
                self.assertEqual(neft.get_star_atom_for_ligand_remap(compId, nefAtom, None, coordAtomSite)[:2], expected)

    def test_nef_translator_guesses_ambiguity_code_from_pseudo_trp(self):
        # tryptophan under a comp_id unknown to the CCD, so that NefTranslator falls back to the pseudo CCD
        atomIds, typeSymbols, coords, _ = read_residue('TRP')
        bond, topo = buildPseudoChemCompBond(atomIds, typeSymbols, coords)
        compId = 'XXX'
        neft = NefTranslator()
        neft.set_chem_comp_dict({compId: atomIds}, {compId: bond}, {compId: topo}, {})
        coordAtomSite = {'atom_id': atomIds, 'alt_atom_id': atomIds}
        for nefAtom, expected in (('HD1', (['HD1'], 1)),
                                  ('HE1', (['HE1'], 1)),
                                  ('HE3', (['HE3'], 1)),
                                  ('HZ2', (['HZ2'], 1)),
                                  ('HZ3', (['HZ3'], 1)),
                                  ('HE%', (['HE1', 'HE3'], 1)),
                                  ('HZ%', (['HZ2', 'HZ3'], 1)),
                                  ('HH2', (['HH2'], 1)),
                                  ('HB%', (['HB2', 'HB3'], 2))):
            with self.subTest(nefAtom=nefAtom):
                self.assertEqual(neft.get_star_atom_for_ligand_remap(compId, nefAtom, None, coordAtomSite)[:2], expected)

    def test_rings_without_substituent_and_five_membered_rings(self):
        def regular_ring(n, radius):
            return [numpy.array([radius * math.cos(2 * math.pi * i / n), radius * math.sin(2 * math.pi * i / n), 0.0])
                    for i in range(n)]

        # a free benzene: no substituent on any mirror axis, every CH has a mirror partner
        carbons, hydrogens = regular_ring(6, 1.39), regular_ring(6, 2.47)
        atomIds = [f'C{i + 1}' for i in range(6)] + [f'H{i + 1}' for i in range(6)]
        self.assertEqual(ring_flip_hosts(atomIds, ['C'] * 6 + ['H'] * 6, dict(zip(atomIds, carbons + hydrogens))),
                         ['C1', 'C2', 'C3', 'C4', 'C5', 'C6'])

        # pyrrol-1-yl: the mirror axis runs through N1 and the midpoint of C3-C4
        ring = regular_ring(5, 1.19)
        atomIds, typeSymbols = ['N1', 'C2', 'C3', 'C4', 'C5', 'CX'], ['N', 'C', 'C', 'C', 'C', 'C']
        coords = dict(zip(atomIds, ring + [ring[0] * (1 + 1.45 / 1.19)]))
        for i, carbon in enumerate(('C2', 'C3', 'C4', 'C5'), start=1):
            atomIds.append(f'H{carbon[1]}')
            typeSymbols.append('H')
            coords[f'H{carbon[1]}'] = ring[i] * (1 + 1.08 / 1.19)
        self.assertEqual(ring_flip_hosts(atomIds, typeSymbols, coords), ['C2', 'C3', 'C4', 'C5'])

        # pyrrol-2-yl has no mirror symmetry
        coords = dict(zip(['N1', 'C2', 'C3', 'C4', 'C5'], ring))
        coords.update({'CX': ring[1] * (1 + 1.45 / 1.19), 'H3': ring[2] * 1.9, 'H4': ring[3] * 1.9, 'H5': ring[4] * 1.9,
                       'HN': ring[0] * 1.85})
        atomIds = list(coords)
        self.assertEqual(ring_flip_hosts(atomIds, ['N', 'C', 'C', 'C', 'C', 'C', 'H', 'H', 'H', 'H'], coords), [])

    def test_elements_from_type_symbol(self):
        # a mercury atom named HG is a heavy atom, not a proton
        coords = {'HG': numpy.zeros(3), 'C1': numpy.array([2.1, 0.0, 0.0]), 'H1': numpy.array([2.5, 1.0, 0.0])}
        bond, _ = buildPseudoChemCompBond(['HG', 'C1', 'H1'], ['HG', 'C', 'H'], coords)
        self.assertEqual(bond, {'C1': ['H1']})

        # NefTranslator with the type_symbol of each atom (chem_comp_type), as NmrDpUtility passes it
        atomIds, typeSymbols, coords, _ = read_residue('PHE')
        bond, topo = buildPseudoChemCompBond(atomIds, typeSymbols, coords)
        compId = 'XXX'
        neft = NefTranslator()
        neft.set_chem_comp_dict({compId: atomIds}, {compId: bond}, {compId: topo}, {},
                                {compId: dict(zip(atomIds, typeSymbols))})
        coordAtomSite = {'atom_id': atomIds, 'alt_atom_id': atomIds}
        for nefAtom, expected in (('HD%', (['HD1', 'HD2'], 3)), ('HZ', (['HZ'], 1))):
            with self.subTest(nefAtom=nefAtom):
                self.assertEqual(neft.get_star_atom_for_ligand_remap(compId, nefAtom, None, coordAtomSite)[:2], expected)


if __name__ == "__main__":
    unittest.main()
