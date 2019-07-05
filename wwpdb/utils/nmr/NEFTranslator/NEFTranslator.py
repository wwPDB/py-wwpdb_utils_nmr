#.!/usr/bin/env python
##
# File: NEFTranslator.py
# Date: 05-Jul-2019
#
# Updates:
##

"""
This module does the following jobs
1. Validate the NEF and NMR-STAR files
2. Extract the sequence information
3. Format conversion

@author: Kumaran Baskaran
@author: Masashi Yokochi
"""

# Make sure print function work in python2 and python3
from __future__ import print_function

import sys
import os
import ntpath
import json
import logging
import re
import csv
import datetime
import pynmrstar
from pytz import utc

from wwpdb.utils.config.ConfigInfo import ConfigInfo, getSiteId
from wwpdb.apps.ccmodule.io.ChemCompIo import ChemCompReader

PY3 = (sys.version_info[0] == 3)

(scriptPath, scriptName) = ntpath.split(os.path.realpath(__file__))

__version__ = 'v1.2.0'

class NEFTranslator(object):
    """ NEF to NMR-STAR translator
    """

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s\t%(levelname)s\t%(message)s')

    mapFile = scriptPath + '/lib/NEF_NMRSTAR_equivalence.csv'
    NEFinfo = scriptPath + '/lib/NEF_mandatory.csv'
    atmFile = scriptPath + '/lib/atomDict.json'
    codeFile = scriptPath + '/lib/codeDict.json'

    def __init__(self):
        ch = logging.StreamHandler()
        ch.setFormatter(self.formatter)

        self.logger.addHandler(ch)

        (isOk, msg, self.tagMap) = self.load_csv_data(self.mapFile, transpose=True)

        if not isOk:
            self.logger.error(msg)

        (isOk, msg, self.atomDict) = self.load_json_data(self.atmFile)

        if not isOk:
            self.logger.error(msg)

        (isOk, msg, self.codeDict) = self.load_json_data(self.codeFile)

        if not isOk:
            self.logger.error(msg)

        (isOk, msg, self.NEFinfo) = self.load_csv_data(self.NEFinfo)

        if not isOk:
            self.logger.error(msg)

        ch.flush()

        # empty value
        self.empty_value = (None, '', '.', '?')

        # CCD accessing utility
        self.__cI = ConfigInfo(getSiteId())
        self.__ccCvsPath = self.__cI.get('SITE_CC_CVS_PATH')

        self.__ccR = ChemCompReader(False, sys.stderr)
        self.__ccR.setCachePath(self.__ccCvsPath)

        self.__last_comp_id = None
        self.__last_comp_id_test = False
        self.__last_chem_comp_dict = None
        self.__last_chem_comp_atoms = None
        self.__last_chem_comp_bonds = None

        # taken from wwpdb.apps.ccmodule.io.ChemCompIo
        self.__chem_comp_atom_dict = [
                ('_chem_comp_atom.comp_id','%s','str',''),
                ('_chem_comp_atom.atom_id','%s','str',''),
                ('_chem_comp_atom.alt_atom_id','%s','str',''),
                ('_chem_comp_atom.type_symbol','%s','str',''),
                ('_chem_comp_atom.charge','%s','str',''),
                ('_chem_comp_atom.pdbx_align','%s','str',''),
                ('_chem_comp_atom.pdbx_aromatic_flag','%s','str',''),
                ('_chem_comp_atom.pdbx_leaving_atom_flag','%s','str',''),
                ('_chem_comp_atom.pdbx_stereo_config','%s','str',''),
                ('_chem_comp_atom.model_Cartn_x','%s','str',''),
                ('_chem_comp_atom.model_Cartn_y','%s','str',''),
                ('_chem_comp_atom.model_Cartn_z','%s','str',''),
                ('_chem_comp_atom.pdbx_model_Cartn_x_ideal','%s','str',''),
                ('_chem_comp_atom.pdbx_model_Cartn_y_ideal','%s','str',''),
                ('_chem_comp_atom.pdbx_model_Cartn_z_ideal','%s','str',''),
                ('_chem_comp_atom.pdbx_component_atom_id','%s','str',''),
                ('_chem_comp_atom.pdbx_component_comp_id','%s','str',''),
                ('_chem_comp_atom.pdbx_ordinal','%s','str','')
                ]

        atom_id = next(d for d in self.__chem_comp_atom_dict if d[0] == '_chem_comp_atom.atom_id')
        self.__cca_atom_id = self.__chem_comp_atom_dict.index(atom_id)

        aromatic_flag = next(d for d in self.__chem_comp_atom_dict if d[0] == '_chem_comp_atom.pdbx_aromatic_flag')
        self.__cca_aromatic_flag = self.__chem_comp_atom_dict.index(aromatic_flag)

        leaving_atom_flag = next(d for d in self.__chem_comp_atom_dict if d[0] == '_chem_comp_atom.pdbx_leaving_atom_flag')
        self.__cca_leaving_atom_flag = self.__chem_comp_atom_dict.index(leaving_atom_flag)

        type_symbol = next(d for d in self.__chem_comp_atom_dict if d[0] == '_chem_comp_atom.type_symbol')
        self.__cca_type_symbol = self.__chem_comp_atom_dict.index(type_symbol)

        # taken from wwpdb.apps.ccmodule.io.ChemCompIo
        self.__chem_comp_bond_dict = [
                ('_chem_comp_bond.comp_id','%s','str',''),
                ('_chem_comp_bond.atom_id_1','%s','str',''),
                ('_chem_comp_bond.atom_id_2','%s','str',''),
                ('_chem_comp_bond.value_order','%s','str',''),
                ('_chem_comp_bond.pdbx_aromatic_flag','%s','str',''),
                ('_chem_comp_bond.pdbx_stereo_config','%s','str',''),
                ('_chem_comp_bond.pdbx_ordinal','%s','str','')
                ]

        atom_id_1 = next(d for d in self.__chem_comp_bond_dict if d[0] == '_chem_comp_bond.atom_id_1')
        self.__ccb_atom_id_1 = self.__chem_comp_bond_dict.index(atom_id_1)

        atom_id_2 = next(d for d in self.__chem_comp_bond_dict if d[0] == '_chem_comp_bond.atom_id_2')
        self.__ccb_atom_id_2 = self.__chem_comp_bond_dict.index(atom_id_2)

        aromatic_flag = next(d for d in self.__chem_comp_bond_dict if d[0] == '_chem_comp_bond.pdbx_aromatic_flag')
        self.__ccb_aromatic_flag = self.__chem_comp_bond_dict.index(aromatic_flag)

    @staticmethod
    def read_input_file(in_file):
        """ Reads input NEF/NMR-STAR file
        :param in_file: input file name with proper path
        :return status, data type Entry/Saveframe/Loop, data object
        """

        is_ok = True
        in_data = None

        try:
            in_data = pynmrstar.Entry.from_file(in_file)
            msg = 'Entry'

        except ValueError:

            try:
                in_data = pynmrstar.Saveframe.from_file(in_file)
                msg = 'Saveframe'

            except ValueError:

                try:
                    in_data = pynmrstar.Loop.from_file(in_file)
                    msg = 'Loop'

                except ValueError as e:
                    is_ok = False
                    msg = str(e) # '%s contains no valid saveframe or loop. PyNMRSTAR ++ Error  - %s' % (os.path.basename(in_file), str(e))

        except IOError as e:
            is_ok = False
            msg = str(e)

        return is_ok, msg, in_data

    @staticmethod
    def load_json_data(json_file):
        """ Loads json data
        :param json_file: json file
        :return dictionary
        """

        is_ok = True
        msg = 'Load JSON data file %s' % json_file
        data_dict = []

        try:
            with open(json_file, 'r') as jsonF:
                data_dict = json.loads(jsonF.read())

        except IOError as e:
            is_ok = False
            msg = str(e)

        return is_ok, msg, data_dict

    @staticmethod
    def load_csv_data(csv_file, transpose=False):
        """ Loads csv data
        :param csv_file: csv file
        :param transpose: transpose multidimensional csv lists
        :return list
        """

        is_ok = True
        msg = 'Load CSV data file %s' % csv_file
        csv_map = []

        try:
            csv_dat = []

            with open(csv_file, 'r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')

                for r in csv_reader:
                    if r[0][0] != '#':
                        csv_dat.append(r)

            if transpose:
                csv_map = list(map(list, zip(*csv_dat)))
            else:
                csv_map = csv_dat

        except IOError as e:
            is_ok = False
            msg = str(e)

        return is_ok, msg, csv_map

    def get_one_letter_code(self, comp_id):
        """ Convert comp ID to 1-letter code.
            extended by Masashi Yokochi
        """

        comp_id = comp_id.upper()

        if comp_id in self.codeDict:
            return self.codeDict[comp_id]
        elif comp_id in self.empty_value:
            return '.'
        else:
            return 'X'

    @staticmethod
    def time_stamp(time):
        """ Returns time stamp in human readable format for logging
        :param current system time via time.time()
        :return readable time stamp
        """

        return datetime.datetime.fromtimestamp(time, tz=utc).strftime('%Y-%m-%d %H:%M:%S')

    def validate_file(self, in_file, file_subtype='A'):
        """ Validates input NEF/NMR-STAR file
        file_subtype flags can be 'A' or 'S' or 'R'
            A for All in one file,
            S for chemical Shifts file,
            R for Restraints file
        """

        is_valid = True
        info = []
        warning = []
        error = []

        file_type = 'unknown'

        try:

            is_done, data_type, star_data = self.read_input_file(in_file)

            if is_done:

                minimal_info_nef_a = ['_nef_chemical_shift', '_nef_distance_restraint']
                minimal_info_nef_s = ['_nef_chemical_shift']
                minimal_info_nef_r = ['_nef_distance_restraint']

                minimal_info_nmrstar_a = ['_Atom_chem_shift', '_Gen_dist_constraint']
                minimal_info_nmrstar_s = ['_Atom_chem_shift']
                minimal_info_nmrstar_r = ['_Gen_dist_constraint']

                sf_list, lp_list = self.get_data_content(star_data, data_type)

                info.append('{} saveframes and {} loops found'.format(len(sf_list), len(lp_list)))

                nef_sf_list = [i for i in sf_list if 'nef' in i]
                nef_lp_list = [i for i in lp_list if 'nef' in i]

                info.append('{} saveframes and {} loops found with NEF prefix'.format(len(nef_sf_list), len(nef_lp_list)))

                if len(nef_sf_list) > 0 or len(nef_lp_list) > 0:

                    is_nef_file = True
                    info.append('{} is a NEF file'.format(in_file))
                    file_type = 'nef'

                else:

                    is_nef_file = False
                    info.append('{} is an NMR-STAR file'.format(in_file))
                    file_type = 'nmr-star'

                if is_nef_file:
                    if file_subtype == 'A':

                        for lp_info in minimal_info_nef_a:
                            if lp_info not in lp_list:
                                is_valid = False
                                error.append('{} loop not found'.format(lp_info))
                            else:
                                if self.is_empty_loop(star_data, lp_info, data_type):
                                    is_valid = False
                                    error.append('{} loop is empty'.format(lp_info))

                    elif file_subtype == 'S':

                        for lp_info in minimal_info_nef_s:
                            if lp_info not in lp_list:
                                is_valid = False
                                error.append('{} loop not found'.format(lp_info))
                            else:
                                if self.is_empty_loop(star_data, lp_info, data_type):
                                    is_valid = False
                                    error.append('{} loop is empty'.format(lp_info))

                    elif file_subtype == 'R':

                        for lp_info in minimal_info_nef_r:
                            if lp_info not in lp_list:
                                is_valid = False
                                error.append('{} loop not found'.format(lp_info))
                            else:
                                if self.is_empty_loop(star_data, lp_info, data_type):
                                    is_valid = False
                                    error.append('{} loop is empty'.format(lp_info))

                    else:
                        is_valid = False
                        error.append('file_subtype flag should be A/S/R')

                else:
                    if file_subtype == 'A':

                        for lp_info in minimal_info_nmrstar_a:
                            if lp_info not in lp_list:
                                is_valid = False
                                error.append('{} loop not found'.format(lp_info))
                            else:
                                if self.is_empty_loop(star_data, lp_info, data_type):
                                    is_valid = False
                                    error.append('{} loop is empty'.format(lp_info))

                    elif file_subtype == 'S':

                        for lp_info in minimal_info_nmrstar_s:
                            if lp_info not in lp_list:
                                is_valid = False
                                error.append('{} loop not found'.format(lp_info))
                            else:
                                if self.is_empty_loop(star_data, lp_info, data_type):
                                    is_valid = False
                                    error.append('{} loop is empty'.format(lp_info))

                    elif file_subtype == 'R':

                        for lp_info in minimal_info_nmrstar_r:
                            if lp_info not in lp_list:
                                is_valid = False
                                error.append('{} loop not found'.format(lp_info))
                            else:
                                if self.is_empty_loop(star_data, lp_info, data_type):
                                    is_valid = False
                                    error.append('{} loop is empty'.format(lp_info))

                    else:
                        is_valid = False
                        error.append('file_subtype flag should be A/S/R')

            else:
                is_valid = False
                error.append(data_type)

        except IOError as e:
            is_valid = False
            error.append(str(e))

        return is_valid, json.dumps({'info': info, 'warning': warning, 'error': error, 'file_type': file_type})

    @staticmethod
    def is_empty_loop(star_data, lp_category, data_type):
        """ Check if a given loop is empty
        """

        if data_type == 'Entry':

            loops = star_data.get_loops_by_category(lp_category)

            for loop in loops:
                if len(loop.data) == 0:
                    return True

            return False

        elif data_type == 'Saveframe':

            loop = star_data.get_loop_by_category(lp_category)
            return len(loop.data) == 0

        else:
            return len(star_data.data) == 0

    @staticmethod
    def is_empty_data(data):
        """ Check if given data has empty code.
            @author: Masashi Yokochi
            @return: True for empty data, False otherwise
        """

        for d in data:
            if d in (None, '', '.', '?'):
                return True

        return False

    @staticmethod
    def is_data(data):
        """ Check if given data has no empty code.
            @author: Masashi Yokochi
            @return: True for non-empty data, False for empty data
        """

        for d in data:
            if d in (None, '', '.', '?'):
                return False

        return True

    @staticmethod
    def get_data_content(star_data, data_type):

        sf_list = []
        lp_list = []

        if data_type == 'Entry':

            for sf in star_data.frame_list:
                sf_list.append(sf.category)

                for lp in sf:
                    lp_list.append(lp.category)

        elif data_type == 'Saveframe':

            for lp in star_data:
                lp_list.append(lp.category)

        else:
            lp_list.append(star_data.category)

        return sf_list, lp_list

    def get_seq_from_cs_loop(self, in_file):
        """ Extracts sequence from chemical shift loop
        :param in_file: NEF/NMR-STAR file
        :return status, json data
        """

        is_valid, json_dumps = self.validate_file(in_file, 'S')

        dat = json.loads(json_dumps)

        info = dat['info']
        warning = dat['warning']
        error = dat['error']

        is_ok = False
        seq = []

        if is_valid:

            info.append('File successfully read ')
            in_dat = self.read_input_file(in_file)[-1]

            if dat['file_type'] == 'nmr-star':

                info.append('NMR-STAR')
                seq = self.get_star_seq(in_dat)

                if len(seq[0]) > 0:
                    is_ok = True

                else:
                    error.append("Can't extract sequence from chemical shift loop")

            elif dat['file_type'] == 'nef':

                info.append('NEF')
                seq = self.get_nef_seq(in_dat)

                if len(seq[0]) > 0:
                    is_ok = True

                else:
                    error.append("Can't extract sequence from chemical shift loop")

            else:
                error.append("Can't identify file type, it is neither NEF nor NMR-STAR")

        else:
            error.append('File validation failed (or) File contains no chemical shift information')

        return is_ok, json.dumps({'info': info, 'warning': warning, 'error': error, 'file_type': dat['file_type'], 'data': seq})

    @staticmethod
    def get_nef_seq(star_data, lp_category='nef_chemical_shift', seq_id='sequence_code', comp_id='residue_name',
                    chain_id='chain_code', allow_empty=False):
        """ Extracts sequence from any given loops in an NEF file.
            extended by Masashi Yokochi
        """

        try:
            loops = star_data.get_loops_by_category(lp_category)
        except AttributeError:
            try:
                loops = [star_data.get_loop_by_category(lp_category)]
            except AttributeError:
                loops = [star_data]

        dat = [] # data of all loops

        tags = [seq_id, comp_id, chain_id]

        for loop in loops:
            seq_dict = {}
            sid_dict = {}

            seq_dat = []

            if set(tags) & set(loop.tags) == set(tags):
                seq_dat = loop.get_data_by_tag(tags)
            else:
                _tags_exist = False
                for i in range(1, 16):
                    _tags = [seq_id + '_' + str(i), comp_id + '_' + str(i), chain_id + '_' + str(i)]
                    if set(_tags) & set(loop.tags) == set(_tags):
                        _tags_exist = True
                        seq_dat += loop.get_data_by_tag(_tags)

                if not _tags_exist:
                    raise LookupError("Missing one of data items %s." % tags)

            if allow_empty:
                seq_dat = list(filter(NEFTranslator.is_data, seq_dat))
                if len(seq_dat) == 0:
                    continue
            else:
                for i in seq_dat:
                    if NEFTranslator.is_empty_data(i):
                        raise ValueError("Sequence must not be empty. %s %s, %s %s, %s %s." % (chain_id, i[2], seq_id, i[0], comp_id, i[1]))

            try:

                chains = sorted(set([i[2] for i in seq_dat]))
                sorted_seq = sorted(set(['{} {:04d} {}'.format(i[2], int(i[0]), i[1]) for i in seq_dat]))

                chk_dict = {'{} {:04d}'.format(i[2], int(i[0])):i[1] for i in seq_dat}

                for i in seq_dat:
                    chk_key = '{} {:04d}'.format(i[2], int(i[0]))
                    if chk_dict[chk_key] != i[1]:
                        raise KeyError("Sequence must be unique. %s %s, %s %s, %s %s vs %s." % (chain_id, i[2], seq_id, i[0], comp_id, i[1], chk_dict[chk_key]))

                if len(sorted_seq[0].split(' ')[-1]) > 1:
                    if len(chains) > 1:
                        for c in chains:
                            seq_dict[c] = [i.split(' ')[-1] for i in sorted_seq if i.split(' ')[0] == c]
                            sid_dict[c] = [int(i.split(' ')[1]) for i in sorted_seq if i.split(' ')[0] == c]
                    else:
                        seq_dict[list(chains)[0]] = [i.split(' ')[-1] for i in sorted_seq]
                        sid_dict[list(chains)[0]] = [int(i.split(' ')[1]) for i in sorted_seq]
                else:
                    if len(chains) > 1:
                        for c in chains:
                            seq_dict[c] = [i.split(' ')[-1] for i in sorted_seq if i.split(' ')[0] == c]
                            sid_dict[c] = [int(i.split(' ')[1]) for i in sorted_seq if i.split(' ')[0] == c]
                    else:
                        seq_dict[list(chains)[0]] = [i.split(' ')[-1] for i in sorted_seq]
                        sid_dict[list(chains)[0]] = [int(i.split(' ')[1]) for i in sorted_seq]

                asm = [] # assembly of a loop

                for c in chains:
                    ent = {} # entity

                    ent['chain_id'] = c
                    ent['seq_id'] = sid_dict[c]
                    ent['comp_id'] = seq_dict[c]

                    asm.append(ent)

                dat.append(asm)

            except ValueError:
                raise ValueError("%s must be int." % seq_id)

        if len(dat) == 0:
            dat.append([])

        return dat

    @staticmethod
    def get_star_seq(star_data, lp_category='Atom_chem_shift', seq_id='Comp_index_ID', comp_id='Comp_ID',
                     chain_id='Entity_assembly_ID', allow_empty=False):
        """ Extracts sequence from any given loops in an NMR-STAR file.
            extended by Masashi Yokochi
        """

        try:
            loops = star_data.get_loops_by_category(lp_category)
        except AttributeError:
            try:
                loops = [star_data.get_loop_by_category(lp_category)]
            except AttributeError:
                loops = [star_data]

        dat = [] # data of all loops

        tags = [seq_id, comp_id, chain_id]
        tags_ = [seq_id, comp_id]

        for loop in loops:
            seq_dict = {}
            sid_dict = {}

            seq_dat = []

            if set(tags) & set(loop.tags) == set(tags):
                seq_dat = loop.get_data_by_tag(tags)
            elif set(tags_) & set(loop.tags) == set(tags_): # No Entity_assembly_ID tag case
                seq_dat = loop.get_data_by_tag(tags_)
                for i in seq_dat:
                    i.append('1')
            else:
                _tags_exist = False
                for i in range(1, 16):
                    _tags = [seq_id + '_' + str(i), comp_id + '_' + str(i), chain_id + '_' + str(i)]
                    _tags_ = [seq_id + '_' + str(i), comp_id + '_' + str(i)]
                    if set(_tags) & set(loop.tags) == set(_tags):
                        _tags_exist = True
                        seq_dat += loop.get_data_by_tag(_tags)
                    elif set(_tags_) & set(loop.tags) == set(_tags_):
                        _tags_exist = True
                        seq_dat_ = loop.get_data_by_tag(_tags_)
                        for i in seq_dat_:
                            i.append('1')
                        seq_dat += seq_dat_

                if not _tags_exist:
                    raise LookupError("Missing one of data items %s." % tags)

            if allow_empty:
                seq_dat = list(filter(NEFTranslator.is_data, seq_dat))
                if len(seq_dat) == 0:
                    continue
            else:
                for i in seq_dat:
                    if NEFTranslator.is_empty_data(i):
                        raise ValueError("Sequence must not be empty. %s %s, %s %s, %s %s." % (chain_id, i[2], seq_id, i[0], comp_id, i[1]))

            try:

                chains = sorted(set([i[2] for i in seq_dat]))
                sorted_seq = sorted(set(['{} {:04d} {}'.format(i[2], int(i[0]), i[1]) for i in seq_dat]))

                chk_dict = {'{} {:04d}'.format(i[2], int(i[0])):i[1] for i in seq_dat}

                for i in seq_dat:
                    chk_key = '{} {:04d}'.format(i[2], int(i[0]))
                    if chk_dict[chk_key] != i[1]:
                        raise KeyError("Sequence must be unique. %s %s, %s %s, %s %s vs %s." % (chain_id, i[2], seq_id, i[0], comp_id, i[1], chk_dict[chk_key]))

                if len(sorted_seq[0].split(' ')[-1]) > 1:
                    if len(chains) > 1:
                        for c in chains:
                            seq_dict[c] = [i.split(' ')[-1] for i in sorted_seq if i.split(' ')[0] == c]
                            sid_dict[c] = [int(i.split(' ')[1]) for i in sorted_seq if i.split(' ')[0] == c]
                    else:
                        seq_dict[list(chains)[0]] = [i.split(' ')[-1] for i in sorted_seq]
                        sid_dict[list(chains)[0]] = [int(i.split(' ')[1]) for i in sorted_seq]
                else:
                    if len(chains) > 1:
                        for c in chains:
                            seq_dict[c] = [i.split(' ')[-1] for i in sorted_seq if i.split(' ')[0] == c]
                            sid_dict[c] = [int(i.split(' ')[1]) for i in sorted_seq if i.split(' ')[0] == c]
                    else:
                        seq_dict[list(chains)[0]] = [i.split(' ')[-1] for i in sorted_seq]
                        sid_dict[list(chains)[0]] = [int(i.split(' ')[1]) for i in sorted_seq]

                asm = [] # assembly of a loop

                for c in chains:
                    ent = {} # entity

                    ent['chain_id'] = c
                    ent['seq_id'] = sid_dict[c]
                    ent['comp_id'] = seq_dict[c]

                    asm.append(ent)

                dat.append(asm)

            except ValueError:
                raise ValueError("%s must be int.")

        if len(dat) == 0:
            dat.append([])

        return dat

    @staticmethod
    def get_star_auth_seq(star_data, lp_category='Atom_chem_shift', aseq_id='Auth_seq_ID', acomp_id='Auth_comp_ID',
                          asym_id='Auth_asym_ID', seq_id='Comp_index_ID', chain_id='Entity_assembly_ID', allow_empty=True):
        """ Extracts author sequence from any given loops in an NMR-STAR file.
            @author: Masashi Yokochi
        """

        try:
            loops = star_data.get_loops_by_category(lp_category)
        except AttributeError:
            try:
                loops = [star_data.get_loop_by_category(lp_category)]
            except AttributeError:
                loops = [star_data]

        dat = [] # data of all loops

        tags = [aseq_id, acomp_id, asym_id, seq_id, chain_id]
        tags_ = [aseq_id, acomp_id, seq_id, asym_id]

        for loop in loops:
            sid_dict = {}
            aseq_dict = {}
            asid_dict = {}
            asym_dict = {}

            seq_dat = []

            if set(tags) & set(loop.tags) == set(tags):
                seq_dat = loop.get_data_by_tag(tags)
            elif set(tags_) & set(loop.tags) == set(tags_): # No Entity_assembly_ID tag case
                seq_dat = loop.get_data_by_tag(tags_)
                for i in seq_dat:
                    i.append('1')
            else:
                _tags_exist = False
                for i in range(1, 16):
                    _tags = [aseq_id + '_' + str(i), acomp_id + '_' + str(i), asym_id + '_' + str(i), seq_id + '_' + str(i), chain_id + '_' + str(i)]
                    _tags_ = [aseq_id + '_' + str(i), acomp_id + '_' + str(i), asym_id + '_' + str(i), seq_id + '_' + str(i)]
                    if set(_tags) & set(loop.tags) == set(_tags):
                        _tags_exist = True
                        seq_dat += loop.get_data_by_tag(_tags)
                    elif set(_tags_) & set(loop.tags) == set(_tags_):
                        _tags_exist = True
                        seq_dat_ = loop.get_data_by_tag(_tags_)
                        for i in seq_dat_:
                            i.append('1')
                        seq_dat += seq_dat_

                if not _tags_exist:
                    raise LookupError("Missing one of data items %s." % tags)

            if allow_empty:
                seq_dat = list(filter(NEFTranslator.is_data, seq_dat))
                if len(seq_dat) == 0:
                    continue
            else:
                for i in seq_dat:
                    if NEFTranslator.is_empty_data(i):
                        raise ValueError("Author sequence must not be empty. %s %s, %s %s, %s %s, %s %s, %s %s." %\
                                         (chain_id, i[4], seq_id, i[3], asym_id, i[2], aseq_id, i[0], acomp_id, i[1]))

            try:

                chains = sorted(set([i[4] for i in seq_dat]))
                sorted_seq = sorted(set(['{}:{:04d}:{}:{: >4}:{}'.format(i[4], int(i[3]), i[2], i[0], i[1]) for i in seq_dat]))

                chk_dict = {'{}:{:04d}:{}:{: >4}'.format(i[4], int(i[3]), i[2], i[0]):i[1] for i in seq_dat}

                for i in seq_dat:
                    chk_key = '{}:{:04d}:{}:{: >4}'.format(i[4], int(i[3]), i[2], i[0])
                    if chk_dict[chk_key] != i[1]:
                        raise KeyError("Author sequence must be unique. %s %s, %s %s, %s %s, %s %s, %s %s vs %s." %\
                                       (chain_id, i[4], seq_id, i[3], asym_id, i[2], aseq_id, i[0], acomp_id, i[1], chk_dict[chk_key]))

                if len(sorted_seq[0].split(':')[-1]) > 1:
                    if len(chains) > 1:
                        for c in chains:
                            aseq_dict[c] = [i.split(':')[-1] for i in sorted_seq if i.split(':')[0] == c]
                            asid_dict[c] = [i.split(':')[3].strip() for i in sorted_seq if i.split(':')[0] == c]
                            asym_dict[c] = [i.split(':')[2] for i in sorted_seq if i.split(':')[0] == c]
                            sid_dict[c] = [int(i.split(':')[1]) for i in sorted_seq if i.split(':')[0] == c]
                    else:
                        aseq_dict[list(chains)[0]] = [i.split(':')[-1] for i in sorted_seq]
                        asid_dict[list(chains)[0]] = [i.split(':')[3].strip() for i in sorted_seq]
                        asym_dict[list(chains)[0]] = [i.split(':')[2] for i in sorted_seq]
                        sid_dict[list(chains)[0]] = [int(i.split(':')[1]) for i in sorted_seq]
                else:
                    if len(chains) > 1:
                        for c in chains:
                            aseq_dict[c] = [i.split(':')[-1] for i in sorted_seq if i.split(':')[0] == c]
                            asid_dict[c] = [i.split(':')[3].strip() for i in sorted_seq if i.split(':')[0] == c]
                            asym_dict[c] = [i.split(':')[2] for i in sorted_seq if i.split(':')[0] == c]
                            sid_dict[c] = [int(i.split(':')[1]) for i in sorted_seq if i.split(':')[0] == c]
                    else:
                        aseq_dict[list(chains)[0]] = [i.split(':')[-1] for i in sorted_seq]
                        asid_dict[list(chains)[0]] = [i.split(':')[3].strip() for i in sorted_seq]
                        asym_dict[list(chains)[0]] = [i.split(':')[2] for i in sorted_seq]
                        sid_dict[list(chains)[0]] = [int(i.split(':')[1]) for i in sorted_seq]

                asm = [] # assembly of a loop

                for c in chains:
                    ent = {} # entity

                    ent['chain_id'] = c
                    ent['seq_id'] = sid_dict[c]
                    ent['auth_asym_id'] = asym_dict[c]
                    ent['auth_seq_id'] = asid_dict[c]
                    ent['auth_comp_id'] = aseq_dict[c]

                    asm.append(ent)

                dat.append(asm)

            except ValueError:
                raise ValueError("%s must be int." % seq_id)

        if len(dat) == 0:
            dat.append([])

        return dat

    @staticmethod
    def get_nef_comp_atom_pair(star_data, lp_category='nef_chemical_shift', comp_id='residue_name', atom_id='atom_name',
                               allow_empty=False):
        """ Wrapper function of get_comp_atom_pair() for an NEF file.
            @author: Masashi Yokochi
        """

        return NEFTranslator.get_comp_atom_pair(star_data, lp_category, comp_id, atom_id, allow_empty)

    @staticmethod
    def get_star_comp_atom_pair(star_data, lp_category='Atom_chem_shift', comp_id='Comp_ID', atom_id='Atom_ID',
                                allow_empty=False):
        """ Wrapper function of get_comp_atom_pair() for an NMR-STAR file.
            @author: Masashi Yokochi
        """

        return NEFTranslator.get_comp_atom_pair(star_data, lp_category, comp_id, atom_id, allow_empty)

    @staticmethod
    def get_star_auth_comp_atom_pair(star_data, lp_category='Atom_chem_shift', comp_id='Auth_comp_ID', atom_id='Auth_atom_ID',
                                     allow_empty=True):
        """ Wrapper function of get_comp_atom_pair() for pairs of author comp_id and author atom_id in an NMR-STAR file.
            @author: Masashi Yokochi
        """

        return NEFTranslator.get_comp_atom_pair(star_data, lp_category, comp_id, atom_id, allow_empty)

    @staticmethod
    def get_comp_atom_pair(star_data, lp_category, comp_id, atom_id, allow_empty):
        """ Extracts unique pairs of comp_id and atom_id from any given loops in an NEF/NMR-STAR file.
            @author: Masashi Yokochi
        """

        try:
            loops = star_data.get_loops_by_category(lp_category)
        except AttributeError:
            try:
                loops = [star_data.get_loop_by_category(lp_category)]
            except AttributeError:
                loops = [star_data]

        dat = [] # data of all loops

        tags = [comp_id, atom_id]

        for loop in loops:
            comp_atom_dict = {}

            comp_atom_dat = []

            if set(tags) & set(loop.tags) == set(tags):
                comp_atom_dat = loop.get_data_by_tag(tags)
            else:
                _tags_exist = False
                for i in range(1, 16):
                    _tags = [comp_id + '_' + str(i), atom_id + '_' + str(i)]
                    if set(_tags) & set(loop.tags) == set(_tags):
                        _tags_exist = True
                        comp_atom_dat += loop.get_data_by_tag(_tags)

                if not _tags_exist:
                    raise LookupError("Missing one of data items %s." % tags)

            if allow_empty:
                comp_atom_dat = list(filter(NEFTranslator.is_data, comp_atom_dat))
                if len(comp_atom_dat) == 0:
                    continue
            else:
                for i in comp_atom_dat:
                    if NEFTranslator.is_empty_data(i):
                        raise ValueError("%s and %s must not be empty. %s %s, %s %s." % (comp_id, atom_id, comp_id, i[0], atom_id, i[1]))

            comps = sorted(set([i[0] for i in comp_atom_dat]))
            sorted_comp_atom = sorted(set(['{} {}'.format(i[0], i[1]) for i in comp_atom_dat]))

            for c in comps:
                comp_atom_dict[c] = [i.split(' ')[1] for i in sorted_comp_atom if i.split(' ')[0] == c]

            asm = [] # assembly of a loop

            for c in comps:
                ent = {} # entity

                ent['comp_id'] = c
                ent['atom_id'] = comp_atom_dict[c]

                asm.append(ent)

            dat.append(asm)

        if len(dat) == 0:
            dat.append([])

        return dat

    @staticmethod
    def get_nef_atom_type_from_cs_loop(star_data, lp_category='nef_chemical_shift', atom_type='element', isotope_number='isotope_number', atom_id='atom_name',
                                       allow_empty=False):
        """ Wrapper function of get_atom_type_from_cs_loop() for an NEF file.
            @author: Masashi Yokochi
        """

        return NEFTranslator.get_atom_type_from_cs_loop(star_data, lp_category, atom_type, isotope_number, atom_id, allow_empty)

    @staticmethod
    def get_star_atom_type_from_cs_loop(star_data, lp_category='Atom_chem_shift', atom_type='Atom_type', isotope_number='Atom_isotope_number', atom_id='Atom_ID',
                                        allow_empty=False):
        """ Wrapper function of get_atom_type_from_cs_loop() for an NMR-SAR file.
            @author: Masashi Yokochi
        """

        return NEFTranslator.get_atom_type_from_cs_loop(star_data, lp_category, atom_type, isotope_number, atom_id, allow_empty)

    @staticmethod
    def get_atom_type_from_cs_loop(star_data, lp_category, atom_type, isotope_number, atom_id, allow_empty):
        """ Extracts unique pairs of atom_type, isotope number, and atom_id from assigned chemical shifts in n NEF/NMR-SAR file.
            @author: Masashi Yokochi
        """

        try:
            loops = star_data.get_loops_by_category(lp_category)
        except AttributeError:
            try:
                loops = [star_data.get_loop_by_category(lp_category)]
            except AttributeError:
                loops = [star_data]

        dat = [] # data of all loops

        tags = [atom_type, isotope_number, atom_id]

        for loop in loops:
            ist_dict = {}
            atm_dict = {}

            a_type_dat = []

            if set(tags) & set(loop.tags) != set(tags):
                raise LookupError("Missing one of data items %s." % tags)

            a_type_dat = loop.get_data_by_tag(tags)

            if allow_empty:
                a_type_dat = list(filter(NEFTranslator.is_data, a_type_dat))
                if len(a_type_dat) == 0:
                    continue
            else:
                for i in a_type_dat:
                    if NEFTranslator.is_empty_data(i):
                        raise ValueError("%s, %s, and %s must not be empty. %s %s, %s %s, %s %s." %\
                                         (atom_type, isotope_number, atom_id, atom_type, i[0], isotope_number, i[1], atom_id, i[2]))

            try:

                a_types = sorted(set([i[0] for i in a_type_dat]))
                sorted_ist = sorted(set(['{} {}'.format(i[0], i[1]) for i in a_type_dat]))
                sorted_atm = sorted(set(['{} {}'.format(i[0], i[2]) for i in a_type_dat]))

                for t in a_types:
                    ist_dict[t] = [int(i.split(' ')[1]) for i in sorted_ist if i.split(' ')[0] == t]
                    atm_dict[t] = [i.split(' ')[1] for i in sorted_atm if i.split(' ')[0] == t]

                asm = [] # assembly of a loop

                for t in a_types:
                    ent = {} # entity

                    ent['atom_type'] = t
                    ent['isotope_number'] = ist_dict[t]
                    ent['atom_id'] = atm_dict[t]

                    asm.append(ent)

                dat.append(asm)

            except ValueError:
                raise ValueError("%s must be int." % isotope_number)

        if len(dat) == 0:
            dat.append([])

        return dat

    @staticmethod
    def get_star_ambig_code_from_cs_loop(star_data, lp_category='Atom_chem_shift', comp_id='Comp_ID', atom_id='Atom_ID', ambig_code='Ambiguity_code', ambig_set_id='Ambiguity_set_ID'):
        """ Extracts unique pairs of comp_id, atom_id, and ambiguity code from assigned chemical shifts in an NMR-SAR file.
            @author: Masashi Yokochi
        """

        try:
            loops = star_data.get_loops_by_category(lp_category)
        except AttributeError:
            try:
                loops = [star_data.get_loop_by_category(lp_category)]
            except AttributeError:
                loops = [star_data]

        dat = [] # data of all loops

        tags = [comp_id, atom_id, ambig_code, ambig_set_id]

        empty_value = (None, '', '.', '?')
        bmrb_ambiguity_codes = (1, 2, 3, 4, 5, 6, 9)

        for loop in loops:
            atm_dict = {}

            ambig_dat = []

            if set(tags) & set(loop.tags) != set(tags):
                raise LookupError("Missing one of data items %s." % tags)

            ambig_dat = loop.get_data_by_tag(tags)

            if len(ambig_dat) == 0:
                dat.append(None)
                continue

            for i in ambig_dat:
                # already checked elsewhere
                #if i[0] in empty_value:
                #   raise ValueError("%s should not be empty." % comp_id)
                #if i[1] in empty_value:
                #    raise ValueError("%s should not be empty." % atom_id)
                if not i[2] in empty_value:

                    try:
                       code = int(i[2])
                    except ValueError:
                        raise ValueError("%s must be one of %s." % (ambig_code, list(bmrb_ambiguity_codes)))

                    if not code in bmrb_ambiguity_codes:
                        raise ValueError("%s must be one of %s." % (ambig_code, list(bmrb_ambiguity_codes)))

                    if code >= 4:
                        if i[3] in empty_value:
                            raise ValueError("%s should not be empty for %s %s." % (ambig_set_id, ambig_code, code))
                        else:
                            try:
                                int(i[3])
                            except ValueError:
                                raise ValueError("%s must be integer." % ambig_set_id)

                if not i[3] in empty_value:

                    if i[2] in empty_value or not i[2] in ['4', '5', '6', '9']:
                        raise ValueError("%s must be empty for %s %s." % (ambig_set_id, ambig_code, i[2]))

            ambigs = sorted(set(['{}:{}'.format(i[0], i[2]) for i in ambig_dat]))
            sorted_atm = sorted(set(['{}:{} {}'.format(i[0], i[2], i[1]) for i in ambig_dat]))

            for a in ambigs:
                atm_dict[a] = [i.split(' ')[1] for i in sorted_atm if i.split(' ')[0] == a]

            asm = [] # assembly of a loop

            for a in ambigs:
                ent = {} # entity

                split_a = a.split(':')

                ent['comp_id'] = split_a[0]
                ent['ambig_code'] = None if split_a[1] in empty_value else int(split_a[1])
                ent['atom_id'] = atm_dict[a]

                asm.append(ent)

            dat.append(asm)

        if len(dat) == 0:
            dat.append([])

        return dat

    @staticmethod
    def get_nef_index(star_data, lp_category='nef_sequence', index_id='index'):
        """ Wrapper function of get_index() for an NEF file.
            @author: Masashi Yokochi
        """

        return NEFTranslator.get_index(star_data, lp_category, index_id)

    @staticmethod
    def get_star_index(star_data, lp_category='Chem_comp_assembly', index_id='NEF_index'):
        """ Wrapper function of get_index() for an NMR-STAR file.
            @author: Masashi Yokochi
        """

        return NEFTranslator.get_index(star_data, lp_category, index_id)

    @staticmethod
    def get_index(star_data, lp_category, index_id):
        """ Extracts index_id from any given loops in an NEF/NMR-STAR file.
            @author: Masashi Yokochi
        """

        try:
            loops = star_data.get_loops_by_category(lp_category)
        except AttributeError:
            try:
                loops = [star_data.get_loop_by_category(lp_category)]
            except AttributeError:
                loops = [star_data]

        dat = [] # data of all loops

        tags = [index_id]

        for loop in loops:
            index_dat = []

            if set(tags) & set(loop.tags) == set(tags):
                index_dat = loop.get_data_by_tag(tags)
            else:
                raise LookupError("Missing key item %s." % index_id)

            for i in index_dat:
                if NEFTranslator.is_empty_data(i):
                    raise ValueError("%s must not be empty." % index_id)

            try:

                idxs = [int(i) for i in index_dat[0]]

                dup_idxs = [i for i in set(idxs) if idxs.count(i) > 1]

                if len(dup_idxs) > 0:
                    raise KeyError("%s must be unique in loop. %s are duplicated." % (index_id, dup_idxs))

                dat.append(idxs)

            except ValueError:
                raise ValueError("%s must be int." % index_id)

        if len(dat) == 0:
            dat.append([])

        return dat

    @staticmethod
    def check_nef_data(star_data, lp_category='nef_chemical_shift',
                       key_items=[{'name': 'chain_code', 'type': 'str'},
                                  {'name': 'sequence_code', 'type': 'int'},
                                  {'name': 'residue_name', 'type': 'str'},
                                  {'name': 'atom_name', 'type': 'str'}],
                       data_items=[{'name': 'value', 'type': 'float', 'mandatory': True},
                                   {'name': 'value_uncertainty', 'type': 'positive-float', 'mandatory': False}]):
        """ Wrapper function of check_data() for an NEF file.
            @author: Masashi Yokochi
        """

        return NEFTranslator.check_data(star_data, lp_category, key_items, data_items)

    @staticmethod
    def check_star_data(star_data, lp_category='Atom_chem_shift',
                        key_items=[{'name': 'Entity_assembly_ID', 'type': 'int'},
                                   {'name': 'Comp_index_ID', 'type': 'int'},
                                   {'name': 'Comp_ID', 'type': 'str'},
                                   {'name': 'Atom_ID', 'type': 'str'}],
                        data_items=[{'name': 'Val', 'type': 'float', 'mandatory': True},
                                    {'name': 'Val_err', 'type': 'positive-float', 'mandatory': False}]):
        """ Wrapper function of check_data() for an NMR-STAR file.
            @author: Masashi Yokochi
        """

        return NEFTranslator.check_data(star_data, lp_category, key_items, data_items)

    @staticmethod
    def check_data(star_data, lp_category, key_items, data_items, allowed_tags=None, disallowed_tags=None, inc_idx_test=False, enforce_non_zero=False, enforce_sign=False, enforce_enum=False):
        """ Extracts unique data with sanity check from any given loops in an NEF/NMR-STAR file.
            @author: Masashi Yokochi
        """

        try:
            loops = star_data.get_loops_by_category(lp_category)
        except AttributeError:
            try:
                loops = [star_data.get_loop_by_category(lp_category)]
            except AttributeError:
                loops = [star_data]

        user_warn_msg = ''

        dat = [] # data of all loops

        item_types = ('str', 'bool', 'int', 'index-int', 'positive-int', 'pointer-index', 'float', 'positive-float', 'range-float', 'enum', 'enum-int')

        key_names = [k['name'] for k in key_items]
        data_names = [d['name'] for d in data_items]
        mand_data_names = [d['name'] for d in data_items if d['mandatory']]

        key_len = len(key_items)

        for k in key_items:
            if not k['type'] in item_types:
                raise TypeError("Type %s of key item %s must be one of %s." % (k['type'], k['name'], item_types))

        for d in data_items:
            if not d['type'] in item_types:
                raise TypeError("Type %s of data item %s must be one of %s." % (d['type'], d['name'], item_types))

        if not allowed_tags is None:

            if (set(key_names) | set(allowed_tags)) != set(allowed_tags):
                raise LookupError("Key items %s must not exists." % ((set(key_names) | set(allowed_tags)) - set(allowed_tags)))

            if (set(data_names) | set(allowed_tags)) != set(allowed_tags):
                raise LookupError("Data items %s must not exists." % ((set(data_names) | set(allowed_tags)) - set(allowed_tags)))

            for d in data_items:
                if 'group-mandatory' in d and d['group-mandatory']:
                    group = d['group']
                    for m in group['member-with']:
                        if not m in allowed_tags:
                            raise Error("Member data item %s of %s must exists in allowed tags." % (m, d['name']))
                    if not group['coexist-with'] is None:
                        for c in group['coexist-with']:
                            if not c in allowed_tags:
                                raise Error("Coexisting data item %s of %s must exists in allowed tags." % (c, d['name']))
                    if 'smaller-than' in group and group['smaller-than']:
                        for s in group['smaller-than']:
                            if not s in allowed_tags:
                                raise Error("Smaller data item %s of %s must exists in allowed tags." % (s, d['name']))
                    if 'larger-than' in group and group['larger-than']:
                        for l in group['larger-than']:
                            if not l in allowed_tags:
                                raise Error("Larger data item %s of %s must exists in allowed tags." % (l, d['name']))
                    if 'not-equal-to' in group and group['not-equal-to']:
                        for l in group['not-equal-to']:
                            if not l in allowed_tags:
                                raise Error("None-equal data item %s of %s must exists in allowed tags." % (l, d['name']))

        empty_value = (None, '', '.', '?')
        true_value = ('true', 't', 'yes', 'y', '1')

        for loop in loops:
            tag_dat = []

            if set(key_names) & set(loop.tags) != set(key_names):
                raise LookupError("Missing one of key items %s." % key_names)

            if len(mand_data_names) > 0 and set(mand_data_names) & set(loop.tags) != set(mand_data_names):
                raise LookupError("Missing one of data items %s." % mand_data_names)

            if not disallowed_tags is None:
                if len(set(loop.tags) & set(disallowed_tags)) > 0:
                    raise LookupError("Disallowed items %s exists." % (set(loop.tags) & set(disallowed_tags)))

            for d in data_items:
                if 'group-mandatory' in d and d['group-mandatory']:
                    name = d['name']
                    group = d['group']
                    if name in loop.tags:
                        if not group['coexist-with'] is None:
                            for c in group['coexist-with']:
                                if not c in loop.tags:
                                    raise LookupError("Missing one of data items %s." % set(group['coexist-with']).add(name))

                    else:
                        has_member = False
                        for m in group['member-with']:
                            if m in loop.tags:
                                has_member = True
                                break
                        if not has_member:
                            raise LookupError("Missing one of data items %s." % set(group['member-with']).add(name))

            tags = [k['name'] for k in key_items]
            for data_name in set(data_names) & set(loop.tags):
                tags.append(data_name)

            tag_len = len(tags)

            static_val = {}
            for name in tags:
                static_val[name] = None

            idx_tag_ids = set()
            for j in range(tag_len):
                name = tags[j]
                if name in key_names:
                    for k in key_items:
                        if k['name'] == name and k['type'] == 'index-int':
                            idx_tag_ids.add(j)
                else:
                    for d in data_items:
                        if d['name'] == name and d['type']== 'index-int':
                            idx_tag_ids.add(j)

            relax_key_ids = set()
            for j in range(tag_len):
                name = tags[j]
                for d in data_items:
                    if d['name'] == name and 'relax-key-if-exist' in d and d['relax-key-if-exist']:
                        relax_key_ids.add(j)

            tag_dat = loop.get_data_by_tag(tags)

            if inc_idx_test and len(idx_tag_ids) > 0:

                for _j in idx_tag_ids:

                    try:
                        idxs = [int(i[_j]) for i in tag_dat]

                        dup_idxs = [i for i in set(idxs) if idxs.count(i) > 1]

                        if len(dup_idxs) > 0:
                            raise KeyError("%s must be unique in loop. %s are duplicated." % (tags[_j], dup_idxs))

                    except ValueError:
                        raise ValueError("%s must be int." % tags[_j])

            for i in tag_dat:
                for j in range(tag_len):
                    if i[j] in empty_value:
                        name = tags[j]
                        if name in key_names:
                            raise ValueError("%s must not be empty." % name)
                        else:
                            for d in data_items:
                                if d['name'] == name and d['mandatory']:
                                    raise ValueError("%s must not be empty." % name)

            if inc_idx_test:
                keys = set()

                rechk = False

                for i in tag_dat:

                    key = ''
                    for j in range(key_len):
                        key += ' ' + i[j]
                    key.rstrip()

                    if key in keys:

                        relax_key = False

                        if len(relax_key_ids) > 0:
                            for j in relax_key_ids:
                                if not i[j] is empty_value:
                                    relax_key = True
                                    break

                        if relax_key:
                            rechk = True
                            continue

                        msg = ''
                        for j in range(key_len):
                            msg += key_names[j] + ' %s, ' % i[j]

                        idx_msg = ''

                        if len(idx_tag_ids) > 0:
                            for _j in idx_tag_ids:
                                idx_msg += tags[_j] + ' '

                                for _i in tag_dat:
                                    _key = ''
                                    for j in range(key_len):
                                        _key += " " + _i[j]
                                        _key.rstrip()

                                    if key == _key:
                                        idx_msg += _i[_j] + ' vs '

                                idx_msg = idx_msg[:-4] + ', '

                            idx_msg = '[Check rows of ' + idx_msg[:-2] + '] '

                        raise KeyError("%sValues of key items must be unique in loop. %s are duplicated." % (idx_msg, msg.rstrip().rstrip(',')))

                    keys.add(key)

                if rechk:
                    keys = set()

                    for i in tag_dat:

                        key = ''
                        for j in range(key_len):
                            key += ' ' + i[j]
                        for j in relax_key_ids:
                            key += ' ' + i[j]
                        key.rstrip()

                        if key in keys:
                            msg = ''
                            for j in range(key_len):
                                msg += key_names[j] + ' %s, ' % i[j]
                            for j in relax_key_ids:
                                if not i[j] in empty_value:
                                    msg += tags[j] + ' %s, ' % i[j]

                            idx_msg = ''

                            if len(idx_tag_ids) > 0:
                                for _j in idx_tag_ids:
                                    idx_msg += tags[_j] + ' '

                                    for _i in tag_dat:
                                        _key = ''
                                        for j in range(key_len):
                                            _key += " " + _i[j]
                                        for j in relax_key_ids:
                                            _key += " " + _i[j]
                                            _key.rstrip()

                                        if key == _key:
                                            idx_msg += _i[_j] + ' vs '

                                    idx_msg = idx_msg[:-4] + ', '

                                idx_msg = '[Check rows of ' + idx_msg[:-2] + '] '

                            raise KeyError("%sValues of key items must be unique in loop. %s are duplicated." % (idx_msg, msg.rstrip().rstrip(',')))

                        keys.add(key)

            asm = [] # assembly of a loop

            for i in tag_dat:
                ent = {} # entity

                for j in range(tag_len):
                    name = tags[j]
                    val = i[j]
                    if j < key_len:
                        k = key_items[j]
                        type = k['type']
                        if type == 'bool':
                            try:
                                ent[name] = val.lower() in true_value
                            except:
                                raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type))
                        elif type == 'int':
                            try:
                                ent[name] = int(val)
                            except:
                                raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type))
                        elif type == 'index-int' or type == 'positive-int':
                            try:
                                ent[name] = int(val)
                            except:
                                raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type))
                            if (type == 'index-int' and ent[name] <= 0) or (type == 'positive-int' and (ent[name] < 0 or (ent[name] == 0 and 'enforce-non-zero' in k and k['enforce-non-zero']))):
                                raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type))
                            elif ent[name] == 0 and enforce_non_zero:
                                user_warn_msg += "[Zero value error] %s%s '%s' is non-sense zero value as %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type)
                        elif type == 'pointer-index':
                            try:
                                ent[name] = int(val)
                            except:
                                raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type))
                            if ent[name] <= 0:
                                raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type))
                            elif static_val[name] is None:
                                static_val[name] = val
                            elif val != static_val[name] and inc_idx_test:
                                raise ValueError("%s%s %s vs %s must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, static_val[name], type))
                        elif type == 'float':
                            try:
                                ent[name] = float(val)
                            except:
                                raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type))
                        elif type == 'positive-float':
                            try:
                                ent[name] = float(val)
                            except:
                                raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type))
                            if ent[name] < 0.0 or (ent[name] == 0.0 and 'enforce-non-zero' in k and k['enforce-non-zero']):
                                raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type))
                            elif ent[name] == 0.0 and enforce_non_zero:
                                user_warn_msg += "[Zero value error] %s%s '%s' is non-sense zero value as %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type)
                        elif type == 'range-float':
                            try:
                                _range = k['range']
                                ent[name] = float(val)
                            except KeyError:
                                raise Error('Range of key item %s is not defined' % name)
                            except:
                                raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type))
                            if ('min_exclusive' in _range and _range['min_exclusive'] == 0.0 and ent[name] <= 0.0) or ('min_inclusive' in _range and _range['min_inclusive'] == 0.0 and ent[name] < 0):
                                if ent[name] < 0.0:
                                    if ('max_inclusive' in _range and abs(ent[name]) > _range['max_inclusive']) or ('max_exclusive' in _range and abs(ent[name]) >= _range['max_exclusive']) or ('enforce-sign' in k and k['enforce-sign']):
                                        raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, _range))
                                    elif enforce_sign:
                                        user_warn_msg += "[Negative value error] %s%s '%s' is non-sense negative value as %s, %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type, _range)
                                elif ent[name] == 0.0 and 'enforce-non-zero' in k and k['enforce-non-zero']:
                                    raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, _range))
                                elif ent[name] == 0.0 and enforce_non_zero:
                                    user_warn_msg += "[Zero value error] %s%s '%s' is non-sense zero value as %s, %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type, _range)
                            elif ('min_exclusive' in _range and ent[name] <= _range['min_exclusive']) or ('min_inclusive' in _range and ent[name] < _range['min_inclusive']) or ('max_inclusive' in _range and ent[name] > _range['max_inclusive']) or ('max_exclusive' in _range and ent[name] >= _range['max_exclusive']):
                                raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, _range))
                        elif type == 'enum':
                            try:
                                enum = k['enum']
                                if not val in enum:
                                    if 'enforce-enum' in k and k['enforce-enum']:
                                        raise ValueError("%s%s '%s' must be one of %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, enum))
                                    elif enforce_enum:
                                        user_warn_msg += "[Enumeration error] %s%s '%s' should be one of %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, enum)
                                ent[name] = val
                            except KeyError:
                                raise Error('Enumeration of key item %s is not defined' % name)
                        elif type == 'enum-int':
                            try:
                                enum = k['enum']
                                if not int(val) in enum:
                                    if 'enforce-enum' in k and k['enforce-enum']:
                                        raise ValueError("%s%s '%s' must be one of %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, enum))
                                    elif enforce_enum:
                                        user_warn_msg += "[Enumeration error] %s%s '%s' should be one of %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, enum)
                                ent[name] = int(val)
                            except KeyError:
                                raise Error('Enumeration of key item %s is not defined' % name)
                            except:
                                raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type))
                        else:
                                ent[name] = val

                    else:
                        for d in data_items:
                            if d['name'] == name:
                                type = d['type']
                                if val in empty_value:
                                   ent[name] = None
                                elif type == 'bool':
                                    try:
                                        ent[name] = val in true_value
                                    except:
                                        raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type))
                                elif type == 'int':
                                    try:
                                        ent[name] = int(val)
                                    except:
                                        raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type))
                                elif type == 'index-int' or type == 'positive-int':
                                    try:
                                        ent[name] = int(val)
                                    except:
                                        raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type))
                                    if (type == 'index-int' and ent[name] <= 0) or (type == 'positive-int' and (ent[name] < 0 or (ent[name] == 0 and 'enforce-non-zero' in d and d['enforce-non-zero']))):
                                        raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type))
                                    elif ent[name] == 0 and enforce_non_zero:
                                        user_warn_msg += "[Zero value error] %s%s '%s' is non-sense zero value as %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type)
                                elif type == 'pointer-index':
                                    try:
                                        ent[name] = int(val)
                                    except:
                                        raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type))
                                    if ent[name] <= 0:
                                        raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type))
                                    elif static_val[name] is None:
                                        static_val[name] = val
                                    elif val != static_val[name] and inc_idx_test:
                                        raise ValueError("%s%s %s vs %s must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, static_val[name], type))
                                elif type == 'float':
                                    try:
                                        ent[name] = float(val)
                                    except:
                                        raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type))
                                elif type == 'positive-float':
                                    try:
                                        ent[name] = float(val)
                                    except:
                                        raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type))
                                    if ent[name] < 0.0 or (ent[name] == 0.0 and 'enforce-non-zero' in d and d['enforce-non-zero']):
                                        raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type))
                                    elif ent[name] == 0.0 and enforce_non_zero:
                                        user_warn_msg += "[Zero value error] %s%s '%s' is non-sense zero value as %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type)
                                elif type == 'range-float':
                                    try:
                                        _range = d['range']
                                        ent[name] = float(val)
                                    except KeyError:
                                        raise Error('Range of data item %s is not defined' % name)
                                    except:
                                        raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type))
                                    if ('min_exclusive' in _range and _range['min_exclusive'] == 0.0 and ent[name] <= 0.0) or ('min_inclusive' in _range and _range['min_inclusive'] == 0.0 and ent[name] < 0):
                                        if ent[name] < 0.0:
                                            if ('max_inclusive' in _range and abs(ent[name]) > _range['max_inclusive']) or ('max_exclusive' in _range and abs(ent[name]) >= _range['max_exclusive']) or ('enforce-sign' in d and d['enforce-sign']):
                                                raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, _range))
                                            elif enforce_sign:
                                                user_warn_msg += "[Negative value error] %s%s '%s' is non-sense negative value as %s, %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type, _range)
                                        elif ent[name] == 0.0 and 'enforce-non-zero' in d and d['enforce-non-zero']:
                                            raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, _range))
                                        elif ent[name] == 0.0 and enforce_non_zero:
                                            user_warn_msg += "[Zero value error] %s%s '%s' is non-sense zero value as %s, %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type, _range)
                                    elif ('min_exclusive' in _range and ent[name] <= _range['min_exclusive']) or ('min_inclusive' in _range and ent[name] < _range['min_inclusive']) or ('max_inclusive' in _range and ent[name] > _range['max_inclusive']) or ('max_exclusive' in _range and ent[name] >= _range['max_exclusive']):
                                        raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, _range))
                                elif type == 'enum':
                                    try:
                                        enum = d['enum']
                                        if not val in enum:
                                            if 'enforce-enum' in d and d['enforce-enum']:
                                                raise ValueError("%s%s '%s' must be one of %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, enum))
                                            elif enforce_enum:
                                                user_warn_msg += "[Enumeration error] %s%s '%s' should be one of %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, enum)
                                        ent[name] = val
                                    except KeyError:
                                        raise Error('Enumeration of data item %s is not defined' % name)
                                elif type == 'enum-int':
                                    try:
                                        enum = d['enum']
                                        if not int(val) in enum:
                                            if 'enforce-enum' in d and d['enforce-enum']:
                                                raise ValueError("%s%s '%s' must be one of %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, enum))
                                            elif enforce_enum:
                                                user_warn_msg += "[Enumeration error] %s%s '%s' should be one of %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, enum)
                                        ent[name] = int(val)
                                    except KeyError:
                                        raise Error('Enumeration of data item %s is not defined' % name)
                                    except:
                                        raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type))
                                else:
                                        ent[name] = val

                for d in data_items:
                    if 'group-mandatory' in d and d['group-mandatory']:
                        name = d['name']
                        group = d['group']
                        if name in ent and not ent[name] is None:
                            if not group['coexist-with'] is None:
                                has_coexist = True
                                for c in group['coexist-with']:
                                    if not c in ent or ent[c] is None:
                                        raise ValueError("%sOne of data item %s must not be empty for a row having %s '%s'." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), c, name, ent[name]))

                            if 'smaller-than' in group and not group['smaller-than'] is None:
                                for s in group['smaller-than']:
                                    if s in ent and not ent[s] is None:
                                        if ent[name] <= ent[s]:
                                            raise ValueError("%sData item %s '%s' must be larger than %s '%s'." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, ent[name], s, ent[s]))

                            if 'larger-than' in group and not group['larger-than'] is None:
                                for l in group['larger-than']:
                                    if l in ent and not ent[l] is None:
                                        if ent[name] >= ent[l]:
                                            raise ValueError("%sData item %s '%s' must be smaller than %s '%s'." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, ent[name], l, ent[l]))

                            if 'not-equal-to' in group and not group['not-equal-to'] is None:
                                for n in group['not-equal-to']:
                                    if n in ent and not ent[n] is None:
                                        if ent[name] == ent[n]:
                                            raise ValueError("%sData item %s '%s' must not be equal to %s '%s'." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, ent[name], n, ent[n]))

                        else:
                            has_member = False
                            for m in group['member-with']:
                                if m in ent and not ent[m] is None:
                                    has_member = True
                                    break
                            if not has_member:
                                raise ValueError("%sOne of data items %s must not be empty." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), set(group['member-with']).add(name)))

                asm.append(ent)

            dat.append(asm)

        if len(user_warn_msg) > 0:
            raise UserWarning(user_warn_msg)

        if len(dat) == 0:
            dat.append([])

        return dat

    @staticmethod
    def idx_msg(idx_tag_ids, tags, ent):
        """ Return description about current index.
            @author: Masashi Yokochi
        """

        idx_msg = ''

        if len(idx_tag_ids) > 0:
            for _j in idx_tag_ids:
                idx_msg += tags[_j] + " " + str(ent[tags[_j]]) + ", "

            idx_msg = '[Check row of ' + idx_msg[:-2] + '] '

        return idx_msg

    @staticmethod
    def check_sf_tag(star_data, tag_items, allowed_tags=None, enforce_non_zero=False, enforce_sign=False, enforce_enum=False):
        """ Extracts saveframe tags with sanity check in an NEF/NMR-STAR file.
            @author: Masashi Yokochi
        """

        user_warn_msg = ''

        item_types = ('str', 'bool', 'int', 'positive-int', 'float', 'positive-float', 'range-float', 'enum', 'enum-int')

        tag_names = [t['name'] for t in tag_items]
        mand_tag_names = [t['name'] for t in tag_items if t['mandatory']]

        for t in tag_items:
            if not t['type'] in item_types:
                raise TypeError("Type %s of tag item %s must be one of %s." % (t['type'], t['name'], item_types))

        if not allowed_tags is None:

            if (set(tag_names) | set(allowed_tags)) != set(allowed_tags):
                raise LookupError("Tag items %s must not exists." % (set(tag_names) | set(allowed_tags)) - set(allowed_tags))

            for t in tag_items:
                if 'group-mandatory' in t and t['group-mandatory']:
                    group = t['group']
                    for m in group['member-with']:
                        if not m in allowed_tags:
                            raise Error("Member tag item %s of %s must exists in allowed tags." % (m, t['name']))
                    if not group['coexist-with'] is None:
                        for c in group['coexist-with']:
                            if not c in allowed_tags:
                                raise Error("Coexisting tag item %s of %s must exists in allowed tags." % (c, t['name']))
                    if 'smaller-than' in group and group['smaller-than']:
                        for s in group['smaller-than']:
                            if not s in allowed_tags:
                                raise Error("Smaller tag item %s of %s must exists in allowed tags." % (s, t['name']))
                    if 'larger-than' in group and group['larger-than']:
                        for l in group['larger-than']:
                            if not l in allowed_tags:
                                raise Error("Larger tag item %s of %s must exists in allowed tags." % (l, t['name']))
                    if 'not-equal-to' in group and group['not-equal-to']:
                        for l in group['not-equal-to']:
                            if not l in allowed_tags:
                                raise Error("None-equal tag item %s of %s must exists in allowed tags." % (l, t['name']))

        empty_value = (None, '', '.', '?')
        true_value = ('true', 't', 'yes', 'y', '1')

        sf_tags = {i[0]:i[1] for i in star_data.tags}

        if len(mand_tag_names) > 0 and set(mand_tag_names) & set(sf_tags.keys()) != set(mand_tag_names):
            raise LookupError("Missing one of tag items %s." % mand_tag_names)

        for t in tag_items:
            if 'group-mandatory' in t and t['group-mandatory']:
                name = t['name']
                group = t['group']
                if name in sf_tags.keys():
                    if not group['coexist-with'] is None:
                        for c in group['coexist-with']:
                            if not c in sf_tags.keys():
                                raise LookupError("Missing one of tags %s." % set(group['coexist-with']).add(name))

                else:
                    has_member = False
                    for m in group['member-with']:
                        if m in sf_tags.keys():
                            has_member = True
                            break
                    if not has_member:
                        raise LookupError("Missing one of tags %s." % set(group['member-with']).add(name))

        for name, val in sf_tags.items():
            if val in empty_value:
                for t in tag_items:
                    if t['name'] == name and t['mandatory']:
                        raise ValueError("%s must not be empty." % name)

        ent = {} # entity

        for name, val in sf_tags.items():
            for t in tag_items:
                if t['name'] == name:
                    type = t['type']
                    if val in empty_value and type != 'enum':
                       ent[name] = None
                    elif type == 'bool':
                        try:
                            ent[name] = val in true_value
                        except:
                            raise ValueError("%s '%s' must be %s." % (name, val, type))
                    elif type == 'int':
                        try:
                            ent[name] = int(val)
                        except:
                            raise ValueError("%s '%s' must be %s." % (name, val, type))
                    elif type == 'positive-int':
                        try:
                            ent[name] = int(val)
                        except:
                            raise ValueError("%s '%s' must be %s." % (name, val, type))
                        if ent[name] < 0 or (ent[name] == 0 and 'enforce-non-zero' in t and t['enforce-non-zero']):
                            raise ValueError("%s '%s' must be %s." % (name, val, type))
                        elif ent[name] == 0 and enforce_non_zero:
                            user_warn_msg += "[Zero value error] %s '%s' is non-sense zero value as %s." % (name, val, type)
                    elif type == 'float':
                        try:
                            ent[name] = float(val)
                        except:
                            raise ValueError("%s '%s' must be %s." % (name, val, type))
                    elif type == 'positive-float':
                        try:
                            ent[name] = float(val)
                        except:
                            raise ValueError("%s '%s' must be %s." % (name, val, type))
                        if ent[name] < 0.0 or (ent[name] == 0.0 and 'enforce-non-zero' in t and t['enforce-non-zero']):
                            raise ValueError("%s '%s' must be %s." % (name, val, type))
                        elif ent[name] == 0.0 and enforce_non_zero:
                            user_warn_msg += "[Zero value error] %s '%s' is non-sense zero value as %s." % (name, val, type)
                    elif type == 'range-float':
                        try:
                            _range = t['range']
                            ent[name] = float(val)
                        except KeyError:
                            raise Error('Range of tag item %s is not defined.' % name)
                        except:
                            raise ValueError("%s '%s' must be %s." % (name, val, type))
                        if ('min_exclusive' in _range and _range['min_exclusive'] == 0.0 and ent[name] <= 0.0) or ('min_inclusive' in _range and _range['min_inclusive'] == 0.0 and ent[name] < 0):
                            if ent[name] < 0.0:
                                if ('max_inclusive' in _range and abs(ent[name]) > _range['max_inclusive']) or ('max_exclusive' in _range and abs(ent[name]) >= _range['max_exclusive']) or ('enforce-sign' in t and t['enforce-sign']):
                                    raise ValueError("%s%s '%s' must be %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, _range))
                                elif enforce_sign:
                                    user_warn_msg += "[Negative value error] %s%s '%s' is non-sense negative value as %s, %s." % (NEFTranslator.idx_msg(idx_tag_ids, tags, ent), name, val, type, _range)
                            elif ent[name] == 0.0 and 'enforce-non-zero' in t and t['enforce-non-zero']:
                                raise ValueError("%s '%s' must be %s." % (name, val, _range))
                            elif ent[name] == 0.0 and enforce_non_zero:
                                user_warn_msg += "[Zero value error] %s '%s' is non-sense zero value as %s, %s." % (name, val, type, _range)
                        elif ('min_exclusive' in _range and ent[name] <= _range['min_exclusive']) or ('min_inclusive' in _range and ent[name] < _range['min_inclusive']) or ('max_inclusive' in _range and ent[name] > _range['max_inclusive']) or ('max_exclusive' in _range and ent[name] >= _range['max_exclusive']):
                            raise ValueError("%s '%s' must be %s." % (name, val, _range))
                    elif type == 'enum':
                        if val in empty_value:
                            val = '?' # '.' raises internal error in NmrDpUtility
                        try:
                            enum = t['enum']
                            if not val in enum:
                                if 'enforce-enum' in t and t['enforce-enum']:
                                    raise ValueError("%s '%s' must be one of %s." % (name, val, enum))
                                elif enforce_enum:
                                    user_warn_msg += "[Enumeration error] %s '%s' should be one of %s." % (name, val, enum)
                            ent[name] = None if val in empty_value else val
                        except KeyError:
                            raise Error('Enumeration of tag item %s is not defined.' % name)
                    elif type == 'enum-int':
                        try:
                            enum = t['enum']
                            if not int(val) in enum:
                                if 'enforce-enum' in t and t['enforce-enum']:
                                    raise ValueError("%s '%s' must be one of %s." % (name, val, enum))
                                elif enforce_enum:
                                    user_warn_msg += "[Enumeration error] %s '%s' should be one of %s." % (name, val, enum)
                            ent[name] = int(val)
                        except KeyError:
                            raise Error('Enumeration of tag item %s is not defined.' % name)
                        except:
                            raise ValueError("%s '%s' must be %s." % (name, val, type))
                    else:
                            ent[name] = val

            for t in tag_items:
                if 'group-mandatory' in t and t['group-mandatory']:
                    name = t['name']
                    group = t['group']
                    if name in ent and not ent[name] is None:
                        if not group['coexist-with'] is None:
                            has_coexist = True
                            for c in group['coexist-with']:
                                if not c in ent or ent[c] is None:
                                    raise ValueError("One of tag item %s must not be empty due to %s '%s'." % (c, name, ent[name]))

                        if 'smaller-than' in group and not group['smaller-than'] is None:
                            for s in group['smaller-than']:
                                if s in ent and not ent[s] is None:
                                    if ent[name] <= ent[s]:
                                        raise ValueError("Tag item %s '%s' must be larger than %s '%s'." % (name, ent[name], s, ent[s]))

                        if 'larger-than' in group and not group['larger-than'] is None:
                            for l in group['larger-than']:
                                if l in ent and not ent[l] is None:
                                    if ent[name] >= ent[l]:
                                        raise ValueError("Tag item %s '%s' must be smaller than %s '%s'." % (name, ent[name], l, ent[l]))

                        if 'not-equal-to' in group and not group['not-equal-to'] is None:
                            for n in group['not-equal-to']:
                                if n in ent and not ent[n] is None:
                                    if ent[name] == ent[n]:
                                        raise ValueError("Tag item %s '%s' must not be equal to %s '%s'." % (name, ent[name], n, ent[n]))

                    else:
                        has_member = False
                        for m in group['member-with']:
                            if m in ent and not ent[m] is None:
                                has_member = True
                                break
                        if not has_member:
                            raise ValueError("One of tag items %s must not be empty." % set(group['member-with']).add(name))

        if len(user_warn_msg) > 0:
            raise UserWarning(user_warn_msg)

        return ent

    def __updateChemCompDict(self, comp_id):
        """ Update CCD information for a given comp_id.
        """

        if comp_id != self.__last_comp_id:
            self.__last_comp_id_test = self.__ccR.setCompId(comp_id)
            self.__last_comp_id = comp_id

            if self.__last_comp_id_test:
                self.__last_chem_comp_dict = self.__ccR.getChemCompDict()
                self.__last_chem_comp_atoms = self.__ccR.getAtoms()
                self.__last_chem_comp_bonds = self.__ccR.getBonds()

        return self.__last_comp_id_test

    def validate_comp_atom(self, comp_id, atom_id):
        """ Validate input atom_id of comp_id.
            extended by Masashi Yokochi for supporting non-standard residue
        """

        comp_id = comp_id.upper()

        if comp_id in self.empty_value:
            return False

        atoms = []

        if comp_id in self.atomDict:
            atoms = self.atomDict[comp_id]

        else:
            self.__updateChemCompDict(comp_id)

            if self.__last_comp_id_test: # matches with comp_id in CCD
                atoms = [a[self.__cca_atom_id] for a in self.__last_chem_comp_atoms]
            else:
                return False

        return atom_id.upper() in atoms

    def validate_atom(self, star_data, lp_category='Atom_chem_shift', seq_id='Comp_index_ID', comp_id='Comp_ID', atom_id='Atom_ID'):
        """ Validates atom_id in a given loop against CCD.
            @return: list of unmatched row data [seq_id, comp_id, atom_id]
            extended by Masashi Yokochi for supporting non-standard residue
        """

        try:
            loop_data = star_data.get_loops_by_category(lp_category)
        except AttributeError:
            try:
                loop_data = [star_data.get_loop_by_category(lp_category)]
            except AttributeError:
                loop_data = [star_data]

        ns = []

        for lp in loop_data:

            try:

                atm_data = lp.get_data_by_tag([seq_id, comp_id, atom_id])

                for i in atm_data:

                    _comp_id_ = i[1].upper()
                    _atom_id_ = i[2].upper()

                    if _comp_id_ in self.empty_value:
                        ns.append(i)

                    elif _comp_id in self.atomDict:
                        if not _atom_id_ in self.atomDict[_comp_id_]:
                            ns.append(i)

                    else:
                        self.__updateChemCompDict(_comp_id_)

                        if self.__last_comp_id_test: # matches with comp_id in CCD
                            if not _atom_id_ in [a[self.__cca_atom_id] for a in self.__last_chem_comp_atoms]:
                                ns.append(i)

                        else:
                            ns.append(i)

            except ValueError:
                self.logger.error('Missing one of data items %s' % (seq_id, comp_id, atom_id))

        return ns

    def get_nmrstar_tag(self, tag):

        n = self.tagMap[0].index(tag)

        return [self.tagMap[1][n], self.tagMap[2][n]]

    def get_nmrstar_loop_tags(self, nef_loop_tags):

        aut_tag = []
        nt = []

        for t in nef_loop_tags:
            st = self.get_nmrstar_tag(t)

            if st[0] != st[1]:
                aut_tag.append(st[1])

            nt.append(st[0])

        if len(aut_tag) != 0:
            out_tag = nt + aut_tag
        else:
            out_tag = nt

        lp_category = nef_loop_tags[0].split('.')[0]

        if lp_category == '_nef_chemical_shift':
            out_tag.append('_Atom_chem_shift.Ambiguity_code')
            out_tag.append('_Atom_chem_shift.Ambiguity_set_ID')
            out_tag.append('_Atom_chem_shift.Assigned_chem_shift_list_ID')

        elif lp_category == '_nef_distance_restraint':
            out_tag.append('_Gen_dist_constraint.Member_logic_code')
            out_tag.append('_Gen_dist_constraint.Gen_dist_constraint_list_ID')

        elif lp_category == '_nef_dihedral_restraint':
            out_tag.append('_Torsion_angle_constraint.Torsion_angle_constraint_list_ID')

        elif lp_category == '_nef_rdc_restraint':
            out_tag.append('_RDC_constraint.RDC_constraint_list_ID')

        elif lp_category == '_nef_peak':
            out_tag.append('_Peak_row_format.Spectral_peak_list_ID')

        return out_tag

    def get_nmrstar_atom(self, comp_id, nef_atom):
        """ Returns list of instanced atom_id of a given NEF atom (including wildcard codes).
            @return: atom type, list of instanced atom_id of a given NEF atom, ambiguity_code.
            extended by Masashi Yokochi for supporting non-standard residue
        """

        comp_id = comp_id.upper()

        ambiguity_code = 1
        atom_type = None
        atom_list = []

        if comp_id in self.empty_value:

            atom_type = nef_atom

            if nef_atom == 'H%':
                atom_type = 'H'
                atom_list = ['H1', 'H2', 'H3']

            return atom_type, atom_list, ambiguity_code

        atoms = []

        if comp_id in self.atomDict:
            atoms = self.atomDict[comp_id]

        else:
            self.__updateChemCompDict(comp_id)

            if self.__last_comp_id_test: # matches with comp_id in CCD
                atoms = [a[self.__cca_atom_id] for a in self.__last_chem_comp_atoms]
            else:
                self.logger.critical('Non-standard residue found {}'.format(comp_id))

        try:

            ref_atom = re.findall(r'(\S+)([xyXY])([%*])$|(\S+)([%*])$|(\S+)([xyXY]$)', nef_atom)[0]

            atm_set = [ref_atom.index(i) for i in ref_atom if i != '']

            pattern = None

            if atm_set == [0, 1, 2]: # endswith [xyXY]%

                atom_type = ref_atom[0]
                xy_code = ref_atom[1].lower()

                len_atom_type = len(atom_type)

                pattern = re.compile(r'%s\S\d+' % (atom_type))

                alist2 = [i for i in atoms if re.search(pattern, i)]

                xid = sorted(set([int(i[len_atom_type]) for i in alist2]))

                if xy_code == 'x':
                    atom_list = [i for i in alist2 if int(i[len_atom_type]) == xid[0]]
                else:
                    atom_list = [i for i in alist2 if int(i[len_atom_type]) == xid[1]]

                ambiguity_code = 2

            elif atm_set == [3, 4]: # endswith [%*] but neither [xyXY][%*]

                atom_type = ref_atom[3]
                wc_code = ref_atom[4]

                if wc_code == '%':
                    pattern = re.compile(r'%s\d+' % atom_type)
                elif wc_code == '*':
                    pattern = re.compile(r'%s\S+' % atom_type)
                else:
                    logging.critical('Wrong NEF atom {}'.format(nef_atom))

                atom_list = [i for i in atoms if re.search(pattern, i)]

                ambiguity_code = 1

            elif atm_set == [5, 6]: # endswith [xyXY]

                atom_type = ref_atom[5]
                xy_code = ref_atom[6].lower()

                pattern = re.compile(r'%s\S+' % atom_type)

                atom_list = [i for i in atoms if re.search(pattern, i)]

                if len(atom_list) != 2:
                    atom_list = []
                elif xy_code == 'y':
                    atom_list = atom_list[-1:]
                elif xy_code == 'x':
                    atom_list = atom_list[:1]
                else:
                    logging.critical('Wrong NEF atom {}'.format(nef_atom))

                ambiguity_code = 2

            else:
                logging.critical('Wrong NEF atom {}'.format(nef_atom))

        except IndexError:

            atom_type = nef_atom

        if len(atom_list) == 0:

            if nef_atom in atoms:
                atom_list.append(nef_atom)

            elif nef_atom == 'H%': # To handle terminal protons
                atom_type = 'H'
                atom_list = ['H1', 'H2', 'H3']

        return atom_type, atom_list, ambiguity_code

    def translate_cs_row(self, f_tags, t_tags, row_data):
        """ Translates row of data in chemical shift loop from NEF into NMR-STAR
        :param f_tags: NEF tags
        :type f_tags: list
        :param t_tags: List NMR-STAR tags
        :type t_tags: list
        :param row_data: List NEF data
        :type row_data: list
        :return list of NMR-STAR row
        """

        out_row = []

        new_id = None
        if '_nef_chemical_shift.chain_code' in f_tags and '_nef_chemical_shift.sequence_code' in f_tags:

            cci = f_tags.index('_nef_chemical_shift.chain_code')
            sci = f_tags.index('_nef_chemical_shift.sequence_code')
            try:
                old_id = [i for i in self.seqDict.keys() if i[0] == row_data[cci] and i[1] == row_data[sci]][0]
                new_id = self.seqDict[old_id]
            except AttributeError:
                new_id = (cci, sci)
            except IndexError:
                new_id = (cci, sci)
        if len(f_tags) != len(t_tags):
            atm_index = f_tags.index('_nef_chemical_shift.atom_name')
            res_index = f_tags.index('_nef_chemical_shift.residue_name')
            n_atm = self.get_nmrstar_atom(row_data[res_index], row_data[atm_index])[1]
            ambi = self.get_nmrstar_atom(row_data[res_index], row_data[atm_index])[2]

            for i in n_atm:
                out = [None] * len(t_tags)
                for j in f_tags:
                    stgs = self.get_nmrstar_tag(j)
                    if stgs[0] == stgs[1]:
                        out[t_tags.index(stgs[0])] = row_data[f_tags.index(j)]
                    else:
                        if j == '_nef_chemical_shift.atom_name':
                            out[t_tags.index(stgs[0])] = row_data[f_tags.index(j)]
                            out[t_tags.index(stgs[1])] = i
                        elif j == '_nef_chemical_shift.chain_code':
                            out[t_tags.index(stgs[0])] = row_data[f_tags.index(j)]
                            out[t_tags.index(stgs[1])] = new_id[0]
                        elif j == '_nef_chemical_shift.sequence_code':
                            out[t_tags.index(stgs[0])] = row_data[f_tags.index(j)]
                            out[t_tags.index(stgs[1])] = new_id[1]
                        else:
                            out[t_tags.index(stgs[0])] = row_data[f_tags.index(j)]
                            out[t_tags.index(stgs[1])] = row_data[f_tags.index(j)]
                    out[t_tags.index('_Atom_chem_shift.Ambiguity_code')] = ambi
                    out[t_tags.index('_Atom_chem_shift.Ambiguity_set_ID')] = '.'

                out_row.append(out)

        else:
            out_row.append(row_data)

        return out_row

    @staticmethod
    def get_residue_identifier(tag_list):
        out_list = []

        for j in range(1, 16):
            out = [None] * 2
            chk_string = re.compile(r'\S+.chain_code_{}'.format(j))
            r1 = [chk_string.search(i).group() for i in tag_list if chk_string.search(i)]
            if len(r1) > 0:
                out[0] = r1[0]
            chk_string = re.compile(r'\S+.sequence_code_{}'.format(j))
            r2 = [chk_string.search(i).group() for i in tag_list if chk_string.search(i)]
            if len(r2) > 0:
                out[1] = r2[0]
            if len(r1) > 0 and len(r2) > 0:
                out_list.append(out)
        #             chk_string = re.compile('\S+.residue_name_{}'.format(j))
        #             r=[chk_string.search(i).group() for i in tag_list if chk_string.search(i)]
        #             if len(r)>0: out[2]=r[0]
        #             chk_string = re.compile('\S+.atom_name_{}'.format(j))
        #             r=[chk_string.search(i).group() for i in tag_list if chk_string.search(i)]
        #             if len(r)>0: out[3]=r[0]

        return out_list

    def translate_row(self, f_tags, t_tags, row_data):
        """ Translates row of data in a loop from NEF into NMR-STAR
        :param f_tags: NEF tags
        :type f_tags: list
        :param t_tags: NMR-STAR tags
        :type t_tags: list
        :param row_data: NEF data
        :type row_data: list
        :return list of NMR-STAR row
        """

        out_row = []

        res_list = self.get_residue_identifier(f_tags)
        tmp_dict = {}
        for res1 in res_list:
            try:
                tmp_dict[res1[0]] = self.seqDict[(row_data[f_tags.index(res1[0])], row_data[f_tags.index(res1[1])])][0]
            except KeyError:
                tmp_dict[res1[0]] = row_data[f_tags.index(res1[0])]
            try:
                tmp_dict[res1[1]] = self.seqDict[(row_data[f_tags.index(res1[0])], row_data[f_tags.index(res1[1])])][1]
            except KeyError:
                tmp_dict[res1[1]] = row_data[f_tags.index(res1[1])]
        # print (tmp_dict)
        if len(f_tags) != len(t_tags):
            out = [None] * len(t_tags)
            for j in f_tags:
                stgs = self.get_nmrstar_tag(j)
                if stgs[0] == stgs[1]:
                    out[t_tags.index(stgs[0])] = row_data[f_tags.index(j)]
                else:
                    if 'chain_code' in j or 'sequence_code' in j:
                        out[t_tags.index(stgs[0])] = row_data[f_tags.index(j)]
                        out[t_tags.index(stgs[1])] = tmp_dict[j]
                    else:
                        out[t_tags.index(stgs[0])] = row_data[f_tags.index(j)]
                        out[t_tags.index(stgs[1])] = row_data[f_tags.index(j)]

            out_row.append(out)

        else:
            out_row.append(row_data)

        return out_row

    def translate_seq_row(self, f_tags, t_tags, row_data):
        """ Translates row of data in sequence loop from NEF into NMR-STAR
        :param f_tags: NEF tags
        :type f_tags: list
        :param t_tags: NMR-STAR tags
        :type t_tags: list
        :param row_data: NEF data
        :type row_data: list
        :return list of NMR-STAR row
        """

        out_row = []

        if len(f_tags) != len(t_tags):
            out = [None] * len(t_tags)
            for j in f_tags:
                stgs = self.get_nmrstar_tag(j)
                if stgs[0] == stgs[1]:
                    out[t_tags.index(stgs[0])] = row_data[f_tags.index(j)]
                else:
                    if j == '_nef_sequence.chain_code':
                        out[t_tags.index(stgs[0])] = row_data[f_tags.index(j)]
                        out[t_tags.index(stgs[1])] = self.chains.index(row_data[f_tags.index(j)]) + 1
                    elif j == '_nef_sequence.sequence_code':
                        out[t_tags.index(stgs[0])] = row_data[f_tags.index(j)]
                        out[t_tags.index(stgs[1])] = self.cid[
                            self.chains.index(row_data[f_tags.index('_nef_sequence.chain_code')])]
                    else:
                        out[t_tags.index(stgs[0])] = row_data[f_tags.index(j)]
                        out[t_tags.index(stgs[1])] = row_data[f_tags.index(j)]

            out_row.append(out)

        else:
            out_row.append(row_data)

        return out_row

    def translate_restraint_row(self, f_tags, t_tags, row_data):
        """ Translates row of data in restraint loop from NEF into NMR-STAR
        :param f_tags: NEF tags
        :type f_tags: list
        :param t_tags: NMR-STAR tags
        :type t_tags: list
        :param row_data: NEF data
        :type row_data: list
        :return list of NMR-STAR row
        """

        out_row = []

        res_list = self.get_residue_identifier(f_tags)
        # print (res_list,f_tags)
        tmp_dict = {}
        for res1 in res_list:
            try:
                tmp_dict[res1[0]] = self.seqDict[(row_data[f_tags.index(res1[0])], row_data[f_tags.index(res1[1])])][0]
            except KeyError:
                tmp_dict[res1[0]] = row_data[f_tags.index(res1[0])]
            try:
                tmp_dict[res1[1]] = self.seqDict[(row_data[f_tags.index(res1[0])], row_data[f_tags.index(res1[1])])][1]
            except KeyError:
                tmp_dict[res1[1]] = row_data[f_tags.index(res1[1])]
        if len(f_tags) != len(t_tags):
            atm_index1 = f_tags.index('_nef_distance_restraint.atom_name_1')
            res_index1 = f_tags.index('_nef_distance_restraint.residue_name_1')
            atm_index2 = f_tags.index('_nef_distance_restraint.atom_name_2')
            res_index2 = f_tags.index('_nef_distance_restraint.residue_name_2')
            n_atm1 = self.get_nmrstar_atom(row_data[res_index1], row_data[atm_index1])[1]
            n_atm2 = self.get_nmrstar_atom(row_data[res_index2], row_data[atm_index2])[1]

            for i in n_atm1:
                for k in n_atm2:
                    out = [None] * len(t_tags)
                    for j in f_tags:
                        stgs = self.get_nmrstar_tag(j)
                        if stgs[0] == stgs[1]:
                            out[t_tags.index(stgs[0])] = row_data[f_tags.index(j)]
                        else:
                            if j == '_nef_distance_restraint.atom_name_1':
                                out[t_tags.index(stgs[0])] = row_data[f_tags.index(j)]
                                out[t_tags.index(stgs[1])] = i
                            elif 'chain_code_1' in j or 'sequence_code_1' in j:
                                out[t_tags.index(stgs[0])] = row_data[f_tags.index(j)]
                                out[t_tags.index(stgs[1])] = tmp_dict[j]
                            elif j == '_nef_distance_restraint.atom_name_2':
                                out[t_tags.index(stgs[0])] = row_data[f_tags.index(j)]
                                out[t_tags.index(stgs[1])] = k
                            elif 'chain_code_2' in j or 'sequence_code_2' in j:
                                out[t_tags.index(stgs[0])] = row_data[f_tags.index(j)]
                                out[t_tags.index(stgs[1])] = tmp_dict[j]
                            else:
                                out[t_tags.index(stgs[0])] = row_data[f_tags.index(j)]
                                out[t_tags.index(stgs[1])] = row_data[f_tags.index(j)]

                    out_row.append(out)

        else:
            out_row.append(row_data)

        return out_row

    def nef_to_nmrstar(self, nef_file, star_file=None):
        (file_path, file_name) = ntpath.split(os.path.realpath(nef_file))
        is_done = True
        info = []
        warning = []
        error = []
        if star_file is None:
            star_file = file_path + '/' + file_name.split('.')[0] + '.str'
        (is_readable, dat_content, nef_data) = self.read_input_file(nef_file)
        try:
            star_data = pynmrstar.Entry.from_scratch(nef_data.entry_id)
        except AttributeError:
            star_data = pynmrstar.Entry.from_scratch(file_name.split('.')[0])
            warning.append('Not a complete Entry')
        if is_readable:
            if dat_content == 'Entry':
                self.chains = sorted(list(set(nef_data.get_loops_by_category('nef_sequence')[0].get_tag('chain_code'))))
            elif dat_content == 'Saveframe':
                self.chains = sorted(list(set(nef_data[0].get_tag('chain_code'))))
            elif dat_content == 'Loop':
                self.chains = sorted(list(set(nef_data.get_tag('chain_code'))))
            else:
                is_done = False
                error.append('File content unknown')

            cs_list = 0
            rest_list = 0
            ang_list = 0
            rdc_list = 0
            peak_list = 0
            if dat_content == 'Entry':
                for saveframe in nef_data:
                    sf = pynmrstar.Saveframe.from_scratch(saveframe.name)

                    for tag in saveframe.tags:
                        if tag[0].lower() == 'sf_category':
                            sf.add_tag('Sf_category', self.get_nmrstar_tag(saveframe.category)[0])
                        else:
                            neftag = '{}.{}'.format(saveframe.tag_prefix, tag[0])
                            sf.add_tag(self.get_nmrstar_tag(neftag)[0], tag[1])
                    if saveframe.category == 'nef_nmr_meta_data':
                        sf.add_tag('NMR_STAR_version', '3.2.0.15')
                        # sf.add_tag('Generated_date', self.TimeStamp(time.time()), update=True)
                        try:
                            lp1 = saveframe.get_loop_by_category('_nef_program_script')
                            lp1.add_data(['NEFTranslator', 'NEFtoNMRSTAR', '.'])
                            # print (lp1.tags)
                        except KeyError:
                            pass  # May be better to add audit loop
                    for loop in saveframe:
                        if loop.category == '_nef_sequence':
                            self.cid = []  # Comp_index_ID list
                            for c in self.chains:  # Comp_index_ID initialized with 1
                                self.cid.append(1)
                            self.seqDict = {}

                        if loop.category == '_nef_distance_restraint':
                            r_index_id = 1
                            rest_list+=1
                        if loop.category == '_nef_dihedral_restraint':
                            ang_list+=1
                        if loop.category == '_nef_rdc_restraint':
                            rdc_list+=1
                        if loop.category == '_nef_chemical_shift':
                            cs_list += 1
                        if loop.category == '_nef_peak':
                            peak_list += 1
                        lp = pynmrstar.Loop.from_scratch()
                        lp_cols = self.get_nmrstar_loop_tags(loop.get_tag_names())
                        for t in lp_cols:
                            lp.add_tag(t)
                        # print (loop.category,lp.category,lp.get_tag_names(),loop.get_tag_names())
                        for dat in loop.data:
                            if loop.category == '_nef_sequence':
                                dd = self.translate_seq_row(loop.get_tag_names(), lp.get_tag_names(), dat)
                                self.cid[
                                    self.chains.index(dat[loop.get_tag_names().index('_nef_sequence.chain_code')])] += 1
                                for d in dd:
                                    lp.add_data(d)
                                    self.seqDict[(dat[loop.get_tag_names().index('_nef_sequence.chain_code')],
                                                  dat[loop.get_tag_names().index('_nef_sequence.sequence_code')])] = (
                                        d[lp.get_tag_names().index('_Chem_comp_assembly.Entity_assembly_ID')],
                                        d[lp.get_tag_names().index('_Chem_comp_assembly.Comp_index_ID')])

                            elif loop.category == '_nef_chemical_shift':
                                dd = self.translate_cs_row(loop.get_tag_names(), lp.get_tag_names(), dat)
                                for d in dd:
                                    d[lp.get_tag_names().index(
                                        '_Atom_chem_shift.Assigned_chem_shift_list_ID')] = cs_list
                                    lp.add_data(d)
                            elif loop.category == '_nef_distance_restraint':
                                dd = self.translate_restraint_row(loop.get_tag_names(), lp.get_tag_names(), dat)
                                for d in dd:
                                    d[lp.get_tag_names().index('_Gen_dist_constraint.Index_ID')] = r_index_id
                                    d[lp.get_tag_names().index('_Gen_dist_constraint.Gen_dist_constraint_list_ID')] = rest_list
                                    if len(dd) > 1:
                                        d[lp.get_tag_names().index('_Gen_dist_constraint.Member_logic_code')] = 'OR'
                                    lp.add_data(d)
                                    r_index_id += 1
                            elif loop.category == '_nef_dihedral_restraint':
                                dd = self.translate_row(loop.get_tag_names(), lp.get_tag_names(), dat)
                                for d in dd:
                                    d[lp.get_tag_names().index(
                                        '_Torsion_angle_constraint.Torsion_angle_constraint_list_ID')] = ang_list
                                    lp.add_data(d)
                            elif loop.category == '_nef_rdc_restraint':
                                dd = self.translate_row(loop.get_tag_names(), lp.get_tag_names(), dat)
                                for d in dd:
                                    d[lp.get_tag_names().index(
                                        '_RDC_constraint.RDC_constraint_list_ID')] = rdc_list
                                    lp.add_data(d)
                            elif loop.category == '_nef_peak':
                                dd = self.translate_row(loop.get_tag_names(), lp.get_tag_names(), dat)
                                for d in dd:
                                    d[lp.get_tag_names().index(
                                        '_Peak_row_format.Spectral_peak_list_ID')] = peak_list
                                    lp.add_data(d)
                            else:
                                dd = self.translate_row(loop.get_tag_names(), lp.get_tag_names(), dat)
                                for d in dd:
                                    lp.add_data(d)
                        # print (loop.data[0])
                        sf.add_loop(lp)
                    star_data.add_saveframe(sf)
                star_data.normalize()
                with open(star_file, 'w') as wstarfile:
                    wstarfile.write(str(star_data))
            elif dat_content == 'Saveframe' or dat_content == 'Loop':
                if dat_content == 'Saveframe':
                    saveframe = nef_data
                    sf = pynmrstar.Saveframe.from_scratch(saveframe.name)
                    for tag in saveframe.tags:
                        if tag[0].lower() == 'sf_category':
                            try:
                                sf.add_tag('Sf_category', self.get_nmrstar_tag(saveframe.category)[0])
                            except ValueError:
                                sf.add_tag('Sf_category', self.get_nmrstar_tag(tag[1])[0])
                        else:
                            neftag = '{}.{}'.format(saveframe.tag_prefix, tag[0])
                            sf.add_tag(self.get_nmrstar_tag(neftag)[0], tag[1])
                    if saveframe.category == 'nef_nmr_meta_data':
                        sf.add_tag('NMR_STAR_version', '3.2.0.15')

                else:
                    sf = pynmrstar.Saveframe.from_scratch(nef_data.category)
                    if nef_data.category == '_nef_chemical_shift':
                        sf.add_tag('_Assigned_chem_shift_list.Sf_category', 'nef_chemical_shift')
                    saveframe = [nef_data]
                for loop in saveframe:
                    if loop.category == '_nef_sequence':
                        self.cid = []  # Comp_index_ID list
                        for c in self.chains:  # Comp_index_ID initialized with 1
                            self.cid.append(1)
                        self.seqDict = {}

                    if loop.category == '_nef_distance_restraint':
                        r_index_id = 1
                    if loop.category == '_nef_chemical_shift':
                        cs_list += 1
                    lp = pynmrstar.Loop.from_scratch()
                    lp_cols = self.get_nmrstar_loop_tags(loop.get_tag_names())
                    for t in lp_cols:
                        lp.add_tag(t)
                    # print (loop.category,lp.category,lp.get_tag_names(),loop.get_tag_names())
                    for dat in loop.data:
                        if loop.category == '_nef_sequence':
                            dd = self.translate_seq_row(loop.get_tag_names(), lp.get_tag_names(), dat)
                            self.cid[
                                self.chains.index(dat[loop.get_tag_names().index('_nef_sequence.chain_code')])] += 1
                            for d in dd:
                                lp.add_data(d)
                                self.seqDict[(dat[loop.get_tag_names().index('_nef_sequence.chain_code')],
                                              dat[loop.get_tag_names().index('_nef_sequence.sequence_code')])] = (
                                    d[lp.get_tag_names().index('_Chem_comp_assembly.Entity_assembly_ID')],
                                    d[lp.get_tag_names().index('_Chem_comp_assembly.Comp_index_ID')])

                        elif loop.category == '_nef_chemical_shift':
                            dd = self.translate_cs_row(loop.get_tag_names(), lp.get_tag_names(), dat)
                            for d in dd:
                                d[lp.get_tag_names().index('_Atom_chem_shift.Assigned_chem_shift_list_ID')] = cs_list
                                lp.add_data(d)
                        elif loop.category == '_nef_distance_restraint':
                            dd = self.translate_restraint_row(loop.get_tag_names(), lp.get_tag_names(), dat)

                            for d in dd:
                                d[lp.get_tag_names().index('_Gen_dist_constraint.Index_ID')] = r_index_id
                                d[lp.get_tag_names().index(
                                    '_Gen_dist_constraint.Gen_dist_constraint_list_ID')] = rest_list
                                if len(dd) > 1:
                                    d[lp.get_tag_names().index('_Gen_dist_constraint.Member_logic_code')] = 'OR'
                                lp.add_data(d)
                                r_index_id += 1
                        elif loop.category == '_nef_dihedral_restraint':
                            dd = self.translate_row(loop.get_tag_names(), lp.get_tag_names(), dat)
                            for d in dd:
                                d[lp.get_tag_names().index(
                                    '_Torsion_angle_constraint.Torsion_angle_constraint_list_ID')] = ang_list
                                lp.add_data(d)
                        elif loop.category == '_nef_rdc_restraint':
                            dd = self.translate_row(loop.get_tag_names(), lp.get_tag_names(), dat)
                            for d in dd:
                                d[lp.get_tag_names().index(
                                    '_RDC_constraint.RDC_constraint_list_ID')] = rdc_list
                                lp.add_data(d)
                        elif loop.category == '_nef_peak':
                            dd = self.translate_row(loop.get_tag_names(), lp.get_tag_names(), dat)
                            for d in dd:
                                d[lp.get_tag_names().index(
                                    '_Peak_row_format.Spectral_peak_list_ID')] = peak_list_list
                                lp.add_data(d)
                        else:
                            dd = self.translate_row(loop.get_tag_names(), lp.get_tag_names(), dat)
                            for d in dd:
                                lp.add_data(d)
                    # print (loop.data[0])
                    sf.add_loop(lp)
                star_data.add_saveframe(sf)
            star_data.normalize()
            with open(star_file, 'w') as wstarfile:
                wstarfile.write(str(star_data))
            info.append('File {} successfully written'.format(star_file))

        else:
            is_done = False
            error.append('Input file not readable')
        return is_done, json.dumps({'info': info, 'warning': warning, 'error': error})

if __name__ == '__main__':
    bt = NEFTranslator()

    bt.nef_to_nmrstar('data/2l9r.nef')

    print (bt.validate_file('data/2l9r.str','A'))
