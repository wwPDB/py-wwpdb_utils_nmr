##
# File: BMRBChemShiftStat.py
# Date: 30-May-2019
#
# Updates:
##
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

        self.loadStatFromPickleFiles()

    def isOk(self):
        """ Return whether all BMRB statistics are available.
        """

        return len(self.aa_filt) > 0 and len(self.aa_full) > 0 and len(self.dna_filt) > 0 and len(self.dna_full) > 0 and len(self.others) > 0

    def printStat(self, list):
        """ Print out statistics.
        """

        for i in list:
            print (i)

    def loadStatFromCsvFiles(self):
        """ Load all BMRB chemical shift statistics from CSV files.
        """

        self.aa_filt = self.loadStatFromCsvFile(self.stat_dir + 'aa_filt.csv')
        self.aa_full = self.loadStatFromCsvFile(self.stat_dir + 'aa_full.csv')

        self.dna_filt = self.loadStatFromCsvFile(self.stat_dir + 'dna_filt.csv')
        self.dna_full = self.loadStatFromCsvFile(self.stat_dir + 'dna_full.csv')

        self.rna_filt = self.loadStatFromCsvFile(self.stat_dir + 'rna_filt.csv')
        self.rna_full = self.loadStatFromCsvFile(self.stat_dir + 'rna_full.csv')

        self.others = self.loadStatFromCsvFile(self.stat_dir + 'others.csv')

    def loadStatFromCsvFile(self, file_name, standard_residue=True):
        """ Load BMRB chemical shift statistics from a given CSV file.
        """

        list = []

        with open(file_name, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                if standard_residue:

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
                            _row['h_desc'] = 'methyl'

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
                            _row['h_desc'] = 'geminal'

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
                        if row['atom_id'].startswith('H'):
                            _row['h_desc'] = 'isolated'

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
                    if row['atom_id'].startswith('H'):
                        _row['h_desc'] = 'isolated'

                    list.append(_row)

        self.detectMethylProtonsFromAtomNomenclature(list)
        self.detectGeminalProtonsFromAtomNomenclature(list)

        return list

    def detectMethylProtonsFromAtomNomenclature(self, list):
        """ Detect methyl protons from atom nomenclature.
            @attention: This function should be re-written using CCD.
        """

        comp_ids = set()

        for i in list:
            comp_ids.add(i['comp_id'])

        for comp_id in comp_ids:
            _list = [i for i in list if i['comp_id'] == comp_id and i['atom_id'].startswith('H') and i['h_desc'] == 'isolated']

            h_1 = [i['atom_id'][:-1] for i in _list if i['atom_id'].endswith('1')]
            h_2 = [i['atom_id'][:-1] for i in _list if i['atom_id'].endswith('2')]
            h_3 = [i['atom_id'][:-1] for i in _list if i['atom_id'].endswith('3')]
            h_4 = [i['atom_id'][:-1] for i in _list if i['atom_id'].endswith('4')]

            common = set(h_1) & set(h_2) & set(h_3) - set(h_4)

            for c in common:
                for i in _list:
                    atom_id = i['atom_id']
                    if atom_id == c + '1' or atom_id == c + '2' or atom_id == c + '3':
                        i['h_desc'] = 'methyl'

    def detectGeminalProtonsFromAtomNomenclature(self, list):
        """ Detect geminal protons from atom nomenclature.
            @attention: This function should be re-written using CCD.
        """

        comp_ids = set()

        for i in list:
            comp_ids.add(i['comp_id'])

        for comp_id in comp_ids:
            _list = [i for i in list if i['comp_id'] == comp_id and i['atom_id'].startswith('H') and i['h_desc'] == 'isolated']

            h_1 = [i['atom_id'][:-1] for i in _list if i['atom_id'].endswith('1')]
            h_2 = [i['atom_id'][:-1] for i in _list if i['atom_id'].endswith('2')]
            h_3 = [i['atom_id'][:-1] for i in _list if i['atom_id'].endswith('3')]

            common = set(h_1) & set(h_2) - set(h_3)

            for c in common:
                for i in _list:
                    atom_id = i['atom_id']
                    if atom_id == c + '1' or atom_id == c + '2':
                        i['h_desc'] = 'genimal'

            common = set(h_2) & set(h_3) - set(h_1)

            for c in common:
                for i in _list:
                    atom_id = i['atom_id']
                    if atom_id == c + '2' or atom_id == c + '3':
                        i['h_desc'] = 'geminal'

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

        self.dna_filt = self.loadStatFromPickleFile(self.stat_dir + 'dna_filt.pkl')
        self.dna_full = self.loadStatFromPickleFile(self.stat_dir + 'dna_full.pkl')

        self.others = self.loadStatFromPickleFile(self.stat_dir + 'others.pkl')

    def loadStatFromPickleFile(self, file_name):
        """ Load BMRB chemical shift statistics from pickle file if possible.
        """

        if os.path.exists(file_name):

            with open(file_name, 'rb') as f:
                return pickle.load(f)

        return []
