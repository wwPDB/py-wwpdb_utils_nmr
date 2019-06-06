##
# File: BMRBChemShiftStat.py
# Date: 06-Jun-2019
#
# Updates:
##
from __builtin__ import False
""" Wrapper class for retrieving BMRB chemical shift statistics.
"""
import sys
import os
import os.path
import csv
import re
import copy
import pickle

class BMRBChemShiftStat:
    """ Wrapper class for retrieving BMRB chemical shift statistics.
    """

    def __init__(self):
        # directory
        self.stat_dir = os.path.dirname(__file__) + '/bmrb_cs_stat/'

        # statistics objects
        self.aa_filt = []
        self.aa_full = []

        self.dna_filt = []
        self.dna_full = []

        self.rna_filt = []
        self.rna_full = []

        self.others = []

        self.__aa_comp_ids = set()
        self.__dna_comp_ids = set()
        self.__rna_comp_ids = set()
        self.__std_comp_ids = set()
        self.__all_comp_ids = set()

        self.aa_threshold = 0.1
        self.na_threshold = 0.3

        self.max_count_th = 10

        self.loadStatFromPickleFiles()

    def isOk(self):
        """ Return whether all BMRB chemical shift statistics are available.
        """

        return len(self.aa_filt) > 0 and len(self.aa_full) > 0 and len(self.dna_filt) > 0 and len(self.dna_full) > 0 and len(self.others) > 0

    def hasCompId(self, comp_id):
        """ Return whether a given comp_id has BMRB chemical shift statistics.
        """

        return comp_id in self.__all_comp_ids

    def getPolymerTypeOfCompId(self, comp_id):
        """ Return polymer type of a given comp_id.
            @return: polypeptide, polynucleotide
            @attention: This function should be re-written using CCD.
        """

        polypeptide = comp_id in self.__aa_comp_ids
        polynucleotide = comp_id in self.__dna_comp_ids or comp_id in self.__rna_comp_ids

        return polypeptide, polynucleotide

    def hasEnoughCSStat(self, comp_id, polypeptide_like=False, polynucleotide_like=False):
        """ Return whether a given comp_id has enough chemical shift statistics.
        """

        if not comp_id in self.__all_comp_ids:
            return False

        if comp_id in self.__std_comp_ids:
            return True

        try:

            if polypeptide_like or not polynucleotide_like:
                next(i for i in self.others if i['comp_id'] == comp_id and i['major'])
            else:
                next(i for i in self.others if i['comp_id'] == comp_id and i['aaa'])

            return True

        except:
            return False

    def get(self, comp_id, paramagnetic=False):
        """ Return BMRB chemical shift statistics for a given comp_id.
        """

        if not comp_id in self.__all_comp_ids:
            return []

        if comp_id in self.__aa_comp_ids:

            if paramagnetic:
                return [i for i in self.aa_full if i['comp_id'] == comp_id]
            else:
                return [i for i in self.aa_filt if i['comp_id'] == comp_id]

        elif comp_id in self.__dna_comp_ids:

            if paramagnetic:
                return [i for i in self.dna_full if i['comp_id'] == comp_id]
            else:
                return [i for i in self.dna_filt if i['comp_id'] == comp_id]

        elif comp_id in self.__rna_comp_ids:

            if paramagnetic:
                return [i for i in self.rna_full if i['comp_id'] == comp_id]
            else:
                return [i for i in self.rna_filt if i['comp_id'] == comp_id]

        else:
            return [i for i in self.others if i['comp_id'] == comp_id]

    def getMaxAmbigCodeWoSetId(self, comp_id, atom_id):
        """ Return maximum ambiguity code of a given atom that does not require declaration of ambiguity set ID.
            @return: one of (1, 2, 3), 0 for not found
        """

        if not comp_id in self.__all_comp_ids:
            return 0

        try:

            d = next(i['desc'] for i in self.get(comp_id) if i['atom_id'] == atom_id)

            if 'geminal' in d:
                return 2
            elif d == 'aroma-opposite':
                return 3
            else:
                return 1

        except StopIteration:
            return 0

    def getGeminalAtom(self, comp_id, atom_id):
        """ Return geminal or aromatic opposite atom of a given atom.
        """

        if not comp_id in self.__all_comp_ids:
            return None

        cs_stat = self.get(comp_id)

        try:

            d = next(i['desc'] for i in cs_stat if i['atom_id'] == atom_id)

            if d == 'methyl-geminal' and atom_id[0] == 'H':
                return next(i['atom_id'] for i in cs_stat if i['desc'] == d and i['atom_id'] != atom_id and i['atom_id'][:-2] == atom_id[:-2] and i['atom_id'][-1] == atom_id[-1])
            elif 'geminal' in d or d == 'aroma-opposite':
                return next(i['atom_id'] for i in cs_stat if i['desc'] == d and i['atom_id'] != atom_id and i['atom_id'][:-1] == atom_id[:-1])
            else:
                return None

        except StopIteration:
            return None

    def getBackBoneAtoms(self, comp_id, excl_minor_atom=False, polypeptide_like=False, polynucleotide_like=False):
        """ Return backbone atoms of a given comp_id.
            @attention: This function should be re-written using CCD.
        """

        if not comp_id in self.__all_comp_ids:
            return []

        cs_stat = self.get(comp_id)

        if comp_id in self.__aa_comp_ids:
            return [i['atom_id'] for i in cs_stat if i['atom_id'] in ['C', 'CA', 'CB', 'H', 'HA', 'HA2', 'HA3', 'N'] and
                    (not excl_minor_atom or (excl_minor_atom and i['major']))]

        elif comp_id in self.__dna_comp_ids:
            return [i['atom_id'] for i in cs_stat if i['atom_id'] in ["C1'", "C2'", "C3'", "C4'", "C5'", "H1'", "H2'", "H2''", "H3'", "H4'", "H5'", "H5''", 'P'] and
                    (not excl_minor_atom or (excl_minor_atom and i['major']))]

        elif comp_id in self.__rna_comp_ids:
            return [i['atom_id'] for i in cs_stat if i['atom_id'] in ["C1'", "C2'", "C3'", "C4'", "C5'", "H1'", "H2'", "H3'", "H4'", "H5'", "H5''", "HO2'", 'P'] and
                    (not excl_minor_atom or (excl_minor_atom and i['major']))]

        elif polypeptide_like:
            return [i['atom_id'] for i in cs_stat if i['atom_id'] in ['C', 'CA', 'CB', 'H', 'HA', 'HA2', 'HA3', 'N'] and
                    (not excl_minor_atom or (excl_minor_atom and i['major']))]

        elif polynucleotide_like:
            return [i['atom_id'] for i in cs_stat if i['atom_id'] in ["C1'", "C2'", "C3'", "C4'", "C5'", "H1'", "H2'", "H2''", "H3'", "H4'", "H5'", "H5''", 'P'] and
                    (not excl_minor_atom or (excl_minor_atom and i['aaa']))]

        return []

    def getAromaticAtoms(self, comp_id, excl_minor_atom=False, polypeptide_like=False, polynucleotide_like=False):
        """ Return aromatic atoms of a given comp_id.
            @attention: This function should be re-written using CCD.
        """

        if not comp_id in self.__all_comp_ids:
            return []

        cs_stat = self.get(comp_id)

        if comp_id in self.__std_comp_ids or polypeptide_like or not polynucleotide_like:
            return [i['atom_id'] for i in cs_stat if 'aroma' in i['desc'] and
                    (not excl_minor_atom or (excl_minor_atom and i['major']))]

        return [i['atom_id'] for i in cs_stat if 'aroma' in i['desc'] and
                (not excl_minor_atom or (excl_minor_atom and i['aaa']))]

    def getMethylAtoms(self, comp_id, excl_minor_atom=False, polypeptide_like=False, polynucleotide_like=False):
        """ Return atoms in methyl group of a geven comp_id.
            @attention: This function should be re-written using CCD.
        """

        if not comp_id in self.__all_comp_ids:
            return []

        cs_stat = self.get(comp_id)

        if comp_id in self.__std_comp_ids or polypeptide_like or not polynucleotide_like:
            return [i['atom_id'] for i in cs_stat if 'methyl' in i['desc'] and
                    (not excl_minor_atom or (excl_minor_atom and i['major']))]

        return [i['atom_id'] for i in cs_stat if 'methyl' in i['desc'] and
                (not excl_minor_atom or (excl_minor_atom and i['aaa']))]

    def getSideChainAtoms(self, comp_id, excl_minor_atom=False, polypeptide_like=False, polynucleotide_like=False):
        """ Return sidechain atoms of a given comp_id.
            @attention: This function should be re-written using CCD.
        """

        if not comp_id in self.__all_comp_ids:
            return []

        bb_atoms = self.getBackBoneAtoms(comp_id, False, polypeptide_like, polynucleotide_like)

        try:
            bb_atoms.remove('CB')
        except ValueError:
            pass

        cs_stat = self.get(comp_id)

        if comp_id in self.__std_comp_ids or polypeptide_like or not polynucleotide_like:
            return [i['atom_id'] for i in cs_stat if not i['atom_id'] in bb_atoms and
                    (not excl_minor_atom or (excl_minor_atom and i['major']))]

        return [i['atom_id'] for i in cs_stat if not i['atom_id'] in bb_atoms and
                (not excl_minor_atom or (excl_minor_atom and i['aaa']))]

    def printStat(self, list):
        """ Print out BMRB chemical shift statistics.
        """

        for i in list:
            print (i)

    def loadStatFromCsvFiles(self):
        """ Load all BMRB chemical shift statistics from CSV files.
        """

        self.aa_filt = self.loadStatFromCsvFile(self.stat_dir + 'aa_filt.csv', self.aa_threshold)
        self.aa_full = self.loadStatFromCsvFile(self.stat_dir + 'aa_full.csv', self.aa_threshold)

        self.dna_filt = self.loadStatFromCsvFile(self.stat_dir + 'dna_filt.csv', self.na_threshold)
        self.dna_full = self.loadStatFromCsvFile(self.stat_dir + 'dna_full.csv', self.na_threshold)

        self.rna_filt = self.loadStatFromCsvFile(self.stat_dir + 'rna_filt.csv', self.na_threshold)
        self.rna_full = self.loadStatFromCsvFile(self.stat_dir + 'rna_full.csv', self.na_threshold)

        self.others = self.loadStatFromCsvFile(self.stat_dir + 'others.csv', self.aa_threshold, self.na_threshold)

        self.__updateCompIdSet()

    def loadStatFromCsvFile(self, file_name, threshold, threshold2=None):
        """ Load BMRB chemical shift statistics from a given CSV file.
        """

        list = []

        with open(file_name, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:

                # methyl proton group
                if row['atom_id'].startswith('M'):
                    _atom_id = re.sub(r'^M', 'H', row['atom_id'])

                    for i in range(1, 4):
                        _row = {}
                        _row['comp_id'] = row['comp_id']
                        _row['atom_id'] = _atom_id + str(i)
                        _row['count'] = int(row['count'])
                        _row['avg'] = float(row['avg'])
                        try:
                            _row['std'] = float(row['std'])
                        except ValueError:
                            _row['std'] = None
                        _row['min'] = float(row['min'])
                        _row['max'] = float(row['max'])
                        _row['desc'] = 'methyl'
                        _row['major'] = False
                        _row['norm_freq'] = None

                        list.append(_row)

                # geminal proton group
                elif row['atom_id'].startswith('Q'):
                    _atom_id = re.sub(r'^Q', 'H', row['atom_id'])

                    for i in range(1, 3):
                        _row = {}
                        _row['comp_id'] = row['comp_id']
                        _row['atom_id'] = _atom_id + str(i)
                        _row['count'] = int(row['count'])
                        _row['avg'] = float(row['avg'])
                        try:
                            _row['std'] = float(row['std'])
                        except ValueError:
                            _row['std'] = None
                        _row['min'] = float(row['min'])
                        _row['max'] = float(row['max'])
                        _row['desc'] = 'geminal'
                        _row['major'] = False
                        _row['norm_freq'] = None

                        list.append(_row)

                else:
                    _row = {}
                    _row['comp_id'] = row['comp_id']
                    _row['atom_id'] = row['atom_id']
                    _row['count'] = int(row['count'])
                    _row['avg'] = float(row['avg'])
                    try:
                        _row['std'] = float(row['std'])
                    except ValueError:
                        _row['std'] = None
                    _row['min'] = float(row['min'])
                    _row['max'] = float(row['max'])
                    _row['desc'] = 'isolated'
                    _row['major'] = False
                    _row['norm_freq'] = None

                    list.append(_row)

        self.__detectMethylProtonFromAtomNomenclature(list)
        self.__detectGeminalProtonFromAtomNomenclature(list)

        self.__detectGeminalCarbon(list)
        self.__detectGeminalNitrogen(list)

        self.__detectMajorResonance(list, threshold, threshold2)

        return list

    def __detectMethylProtonFromAtomNomenclature(self, list):
        """ Detect methyl proton from atom nomenclature.
            @attention: This function should be re-written using CCD.
        """

        comp_ids = set()

        for i in list:
            comp_ids.add(i['comp_id'])

        for comp_id in comp_ids:
            h_list = [i for i in list if i['comp_id'] == comp_id and i['atom_id'].startswith('H') and i['desc'] == 'isolated']

            h_1 = [i['atom_id'][:-1] for i in h_list if i['atom_id'].endswith('1')]
            h_2 = [i['atom_id'][:-1] for i in h_list if i['atom_id'].endswith('2')]
            h_3 = [i['atom_id'][:-1] for i in h_list if i['atom_id'].endswith('3')]
            h_4 = [i['atom_id'][:-1] for i in h_list if i['atom_id'].endswith('4')]

            h_common = set(h_1) & set(h_2) & set(h_3) - set(h_4)

            for h in h_common:
                for i in h_list:
                    atom_id = i['atom_id']
                    if atom_id == h + '1' or atom_id == h + '2' or atom_id == h + '3':
                        i['desc'] = 'methyl'

    def __detectGeminalProtonFromAtomNomenclature(self, list):
        """ Detect geminal proton from atom nomenclature.
            @attention: This function should be re-written using CCD.
        """

        comp_ids = set()

        for i in list:
            comp_ids.add(i['comp_id'])

        for comp_id in comp_ids:
            h_list = [i for i in list if i['comp_id'] == comp_id and i['atom_id'].startswith('H') and i['desc'] == 'isolated']

            h_1 = [i['atom_id'][:-1] for i in h_list if i['atom_id'].endswith('1')]
            h_2 = [i['atom_id'][:-1] for i in h_list if i['atom_id'].endswith('2')]
            h_3 = [i['atom_id'][:-1] for i in h_list if i['atom_id'].endswith('3')]

            c_list = [i for i in list if i['comp_id'] == comp_id and i['atom_id'].startswith('C')]

            c_1 = ['H' + i['atom_id'][1:-1] for i in c_list if i['atom_id'].endswith('1')]
            c_2 = ['H' + i['atom_id'][1:-1] for i in c_list if i['atom_id'].endswith('2')]
            c_3 = ['H' + i['atom_id'][1:-1] for i in c_list if i['atom_id'].endswith('3')]

            n_list = [i for i in list if i['comp_id'] == comp_id and i['atom_id'].startswith('N')]

            n_1 = ['H' + i['atom_id'][1:-1] for i in n_list if i['atom_id'].endswith('1')]
            n_2 = ['H' + i['atom_id'][1:-1] for i in n_list if i['atom_id'].endswith('2')]
            n_3 = ['H' + i['atom_id'][1:-1] for i in n_list if i['atom_id'].endswith('3')]

            h_common = set(h_1) & set(h_2) - set(h_3)
            cn_common = set(c_1) & set(c_2) | set(c_1) & set(n_2) | set(n_1) & set(c_2)

            for h in h_common:
                for i in h_list:
                    atom_id = i['atom_id']
                    if atom_id == h + '1' or atom_id == h + '2':
                        atom_id = 'N' + i['atom_id'][1:]
                        try:
                            next(n for n in n_list if n['atom_id'] == atom_id)
                        except:
                            i['desc'] = 'aroma' if h in cn_common and i['avg'] > 5.0 else 'geminal'

            h_common = set(h_2) & set(h_3) - set(h_1)
            cn_common = set(c_2) & set(c_3) | set(c_2) & set(n_3) | set(n_2) & set(c_3)

            for h in h_common:
                for i in h_list:
                    atom_id = i['atom_id']
                    if atom_id == h + '2' or atom_id == h + '3':
                        atom_id = 'N' + i['atom_id'][1:]
                        try:
                            next(n for n in n_list if n['atom_id'] == atom_id)
                        except:
                            i['desc'] = 'aroma' if h in cn_common and i['avg'] > 5.0 else 'geminal'

            h_list = [i for i in list if i['comp_id'] == comp_id and i['atom_id'].startswith('H') and i['desc'] == 'isolated']

            for h in h_list:
                if h['avg'] > 5.0:
                    atom_id = 'C' + h['atom_id'][1:]
                    try:
                        next(c for c in c_list if c['atom_id'] == atom_id and c['avg'] > 95.0 and c['avg'] < 170.0)
                        h['desc'] = 'aroma'
                    except StopIteration:
                        pass

            h_list = [i for i in list if i['comp_id'] == comp_id and i['atom_id'].startswith('H') and i['desc'] == 'isolated']

            h_c = [i['atom_id'][:-1] for i in h_list if i['atom_id'].endswith("'") and not i['atom_id'].endswith("''")]
            h_cc = [i['atom_id'][:-2] for i in h_list if i['atom_id'].endswith("''")]

            c_c = ['H' + i['atom_id'][1:-1] for i in c_list if i['atom_id'].endswith("'") and not i['atom_id'].endswith("''")]
            c_cc = ['H' + i['atom_id'][1:-2] for i in c_list if i['atom_id'].endswith("''")]

            h_common = set(h_c) & set(h_cc) & set(c_c) - set(c_cc)

            for h in h_common:
                for i in h_list:
                    atom_id = i['atom_id']
                    if atom_id == h + "'" or atom_id == h + "''":
                        atom_id = 'N' + i['atom_id'][1:]
                        try:
                            next(n for n in n_list if n['atom_id'] == atom_id)
                        except:
                            i['desc'] = 'geminal'

            h_list = [i for i in list if i['comp_id'] == comp_id and i['atom_id'].startswith('H') and i['desc'] == 'aroma']

            h_1 = [i['atom_id'][:-1] for i in h_list if i['atom_id'].endswith('1')]
            h_2 = [i['atom_id'][:-1] for i in h_list if i['atom_id'].endswith('2')]
            h_3 = [i['atom_id'][:-1] for i in h_list if i['atom_id'].endswith('3')]

            h_common = set(h_1) & set(h_2)

            if len(h_common) > 0 and len(h_common) % 2 == 0:
                for h in h_common:
                    for i in h_list:
                        atom_id = i['atom_id']
                        if atom_id == h + '1' or atom_id == h + '2':
                            i['desc'] = 'aroma-opposite'

            h_common = set(h_2) & set(h_3)

            if len(h_common) > 0 and len(h_common) % 2 == 0:
                for h in h_common:
                    for i in h_list:
                        atom_id = i['atom_id']
                        if atom_id == h + '2' or atom_id == h + '3':
                            i['desc'] = 'aroma-opposite'

    def __detectGeminalCarbon(self, list):
        """ Detect geminal carbon from atom nomenclature.
            @attention: This function should be re-written using CCD.
        """

        comp_ids = set()

        for i in list:
            comp_ids.add(i['comp_id'])

        for comp_id in comp_ids:
            methyl_list = ['C' + i['atom_id'][1:-1] for i in list if i['comp_id'] == comp_id and i['atom_id'].startswith('H') and i['desc'] == 'methyl' and i['atom_id'].endswith('1')]

            methyl_1 = [i[:-1] for i in methyl_list if i.endswith('1')]
            methyl_2 = [i[:-1] for i in methyl_list if i.endswith('2')]
            methyl_3 = [i[:-1] for i in methyl_list if i.endswith('3')]

            c_list = [i for i in list if i['comp_id'] == comp_id and i['atom_id'].startswith('C')]

            for c in c_list:
                if c['atom_id'] in methyl_list:
                    c['desc'] = 'methyl'
                elif c['avg'] > 95.0 and c['avg'] < 170.0:
                    c['desc'] = 'aroma'

            methyl_common = set(methyl_1) & set(methyl_2) - set(methyl_3)

            for m in methyl_common:
                for c in c_list:
                    atom_id = c['atom_id']
                    if atom_id == m + '1' or atom_id == m + '2':
                        c['desc'] = 'methyl-geminal'
                        for h in [i for i in list if i['comp_id'] == comp_id and i['atom_id'].startswith('H') and i['desc'] == 'methyl' and i['atom_id'].startswith('H' + atom_id[1:])]:
                            h['desc'] = 'methyl-geminal'

            aroma_list = ['C' + i['atom_id'][1:] for i in list if i['comp_id'] == comp_id and i['atom_id'].startswith('H') and i['desc'] == 'aroma']

            for c in c_list:
                if c['atom_id'] in aroma_list:
                    c['desc'] = 'aroma'

            aroma_opposite_list = ['C' + i['atom_id'][1:] for i in list if i['comp_id'] == comp_id and i['atom_id'].startswith('H') and i['desc'] == 'aroma-opposite']

            for c in c_list:
                if c['atom_id'] in aroma_opposite_list:
                    c['desc'] = 'aroma-opposite'

    def __detectGeminalNitrogen(self, list):
        """ Detect geminal nitrogen from atom nomenclature.
            @attention: This function should be re-written using CCD.
        """

        comp_ids = set()

        for i in list:
            comp_ids.add(i['comp_id'])

        for comp_id in comp_ids:
            geminal_list = ['N' + i['atom_id'][1:-1] for i in list if i['comp_id'] == comp_id and i['atom_id'].startswith('H') and i['desc'] == 'geminal' and i['atom_id'].endswith('1')]

            geminal_1 = [i[:-1] for i in geminal_list if i.endswith('1')]
            geminal_2 = [i[:-1] for i in geminal_list if i.endswith('2')]
            geminal_3 = [i[:-1] for i in geminal_list if i.endswith('3')]

            n_list = [i for i in list if i['comp_id'] == comp_id and i['atom_id'].startswith('N')]

            for n in n_list:
                if n['avg'] > 125.0:
                    n['desc'] = 'aroma'
                    atom_id = 'H' + n['atom_id'][1:]
                    try:
                        h = next(i for i in list if i['comp_id'] == comp_id and i['atom_id'] == atom_id and i['desc'] == 'isolated')
                        h['desc'] = 'aroma'
                    except StopIteration:
                        pass

            geminal_common = set(geminal_1) & set(geminal_2) - set(geminal_3)

            for g in geminal_common:
                for n in n_list:
                    atom_id = n['atom_id']
                    if atom_id == g + '1' or atom_id == g + '2':
                        n['desc'] = 'geminal'

    def __detectMajorResonance(self, list, threshold, threshold2=None):
        """ Detect major resonance based on count of assignments.
        """

        comp_ids = set()

        for i in list:
            comp_ids.add(i['comp_id'])

        for comp_id in comp_ids:
            atom_list = [i for i in list if i['comp_id'] == comp_id]

            max_count = max([i['count'] for i in atom_list])

            for a in atom_list:
                a['norm_freq'] = float("%.3f" % (float(a['count']) / max_count))
                if max_count >= self.max_count_th:
                    if a['count'] > max_count * threshold:
                        a['major'] = True
                    if not threshold2 is None and a['count'] > max_count * threshold2:
                        a['aaa'] = True

    def writeStatAsPickleFiles(self):
        """ Write all BMRB chemical shift statistics as pickle files.
        """

        self.writeStatAsPickleFile(self.aa_filt, self.stat_dir + 'aa_filt.pkl')
        self.writeStatAsPickleFile(self.aa_full, self.stat_dir + 'aa_full.pkl')

        self.writeStatAsPickleFile(self.dna_filt, self.stat_dir + 'dna_filt.pkl')
        self.writeStatAsPickleFile(self.dna_full, self.stat_dir + 'dna_full.pkl')

        self.writeStatAsPickleFile(self.rna_filt, self.stat_dir + 'rna_filt.pkl')
        self.writeStatAsPickleFile(self.rna_full, self.stat_dir + 'rna_full.pkl')

        self.writeStatAsPickleFile(self.others, self.stat_dir + 'others.pkl')

    def writeStatAsPickleFile(self, list, file_name):
        """ Write BMRB chemical shift statistics as pickle file.
        """

        with open(file_name, 'wb') as f:
            pickle.dump(list, f)

    def loadStatFromPickleFiles(self):
        """ Load all BMRB chemical shift statistics from pickle files if possible.
        """

        self.aa_filt = self.loadStatFromPickleFile(self.stat_dir + 'aa_filt.pkl')
        self.aa_full = self.loadStatFromPickleFile(self.stat_dir + 'aa_full.pkl')

        self.dna_filt = self.loadStatFromPickleFile(self.stat_dir + 'dna_filt.pkl')
        self.dna_full = self.loadStatFromPickleFile(self.stat_dir + 'dna_full.pkl')

        self.rna_filt = self.loadStatFromPickleFile(self.stat_dir + 'rna_filt.pkl')
        self.rna_full = self.loadStatFromPickleFile(self.stat_dir + 'rna_full.pkl')

        self.others = self.loadStatFromPickleFile(self.stat_dir + 'others.pkl')

        self.__updateCompIdSet()

    def loadStatFromPickleFile(self, file_name):
        """ Load BMRB chemical shift statistics from pickle file if possible.
        """

        if os.path.exists(file_name):

            with open(file_name, 'rb') as f:
                return pickle.load(f)

        return []

    def __updateCompIdSet(self):
        """ Update set of comp_id having BMRB chemical shift statistics
        """

        for i in self.aa_filt:
            self.__aa_comp_ids.add(i['comp_id'])

        for i in self.dna_filt:
            self.__dna_comp_ids.add(i['comp_id'])

        for i in self.rna_filt:
            self.__rna_comp_ids.add(i['comp_id'])

        self.__all_comp_ids |= self.__aa_comp_ids
        self.__all_comp_ids |= self.__dna_comp_ids
        self.__all_comp_ids |= self.__rna_comp_ids

        self.__std_comp_ids = copy.copy(self.__all_comp_ids)

        for i in self.others:
            self.__all_comp_ids.add(i['comp_id'])
