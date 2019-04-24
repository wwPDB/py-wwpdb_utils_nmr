"""
This module does the following jobs
1. Validate the NEF and NMR-STAR files
2. Extract the sequence information
3. Format conversion

@author: Kumaran Baskaran

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
import time
import datetime

PY3 = (sys.version_info[0] == 3)

(scriptPath, scriptName) = ntpath.split(os.path.realpath(__file__))
try:
    # Try to call the pynmrstr form the standard 'pip' installation
    import pynmrstar
except ImportError as e:
    # If pynmrstar is not available then it can import from depui/PyNMRSTAR
    sys.path.append(scriptPath + '/../PyNMRSTAR')  # It is a relative path to current script file
    try:
        import bmrb as pynmrstar
    except ImportError as e:
        print(scriptPath, scriptName)
        print("ERROR: STAR parser(PyNMRSTAR) from BMRB is not available")
        print(str(e))
        exit(1)
# global variable
__version__ = "v1.2-4-g1d9647a"


class NEFTranslator(object):
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
        self.load_map_file()
        self.load_atom_dict()
        self.load_code_dict()
        self.load_nef_info()
        ch.flush()

    @staticmethod
    def readInFile(inFile):

        isOk = False
        try:
            inData = pynmrstar.Entry.from_file(inFile)
            isOk = True
            msg = "Entry"
        except ValueError:
            try:
                inData = pynmrstar.Saveframe.from_file(inFile)
                isOk = True
                msg = "Saveframe"
            except ValueError:
                try:
                    inData = pynmrstar.Loop.from_file(inFile)
                    isOk = True
                    msg = "Loop"
                except ValueError as e:
                    inData = None
                    msg = "File contains no valid saveframe or loop. Invalid file PyNMRSTAR Error:{}".format(e)
        except IOError:
            inData = None
            msg = "File not found"
        return (isOk, msg, inData)

    def load_atom_dict(self):
        """Reads the atomDict json file and creates a dictionary of resides and atoms"""
        try:
            with open(self.atmFile, 'r') as atomF:  # type: BinaryIO
                self.atomDict = json.loads(atomF.read())
        except IOError:
            self.logger.error(
                "atomDict.json file is missing! check the file is inside  {} ".format(self.mapFile + '/lib/'))
            self.atomDict = []

    def load_code_dict(self):
        '''Reads the codeDict json file and creates a dictionary of 3letter to 1 letter code'''
        try:
            with open(self.codeFile, 'r') as codeF:
                self.codeDict = json.loads(codeF.read())
        except IOError:
            self.logger.error(
                "codeDict.json file is missing! check the file is inside  {} ".format(self.mapFile + '/lib/'))
            self.codeDict = []

    def getOneLetter(self, res):
        try:
            ol = self.codeDict[res.upper()]
        except KeyError:
            ol = '?'
        return ol

    def load_map_file(self):
        '''Reads the NEF_NMRSTAR_equivalence.csv file and create a mapping as a list'''
        try:
            with open(self.mapFile, 'r') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                map_dat = []
                for r in spamreader:
                    # print r
                    if r[0][0] != '#':
                        map_dat.append(r)
            self.tagMap = list(map(list, zip(*map_dat)))
        except IOError:
            self.logger.error("NEF-NMRSTAR_equivalence.csv file is missing! check the file is inside  {} ".format(
                self.mapFile + '/lib/'))
            self.tagMap = []

    def load_nef_info(self):
        """Reads mandatory tag information for NEF file"""
        try:
            with open(self.NEFinfo, 'r') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                map_dat = []
                for r in spamreader:
                    # print r
                    if r[0][0] != '#':
                        map_dat.append(r)
            self.NEFinfo = map_dat
        except IOError:
            logger.error(
                "NEF_mandatory.csv file is missing! check the file is inside  {} ".format(self.mapFile + '/lib/'))
            self.NEFinfo = []

    def TimeStamp(self, ts):
        return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    def ValidateFile(self, inFile, fileType='A'):
        ''' Validates input file.
        fileType flags can be 'A' or 'S' or 'R'.
        A for  All in one file,
        S for chemical Shifts file,
        R for 'Restraints file'''
        INFO = []
        WARNING = []
        ERROR = []
        file_typ = 'UNKNOWN'
        try:
            file_info = self.readInFile(inFile)
            if file_info[0]:
                self.inData = file_info[2]
                sf_list = []
                lp_list = []
                minimal_info_nef_A = ['_nef_chemical_shift', '_nef_distance_restraint']
                minimal_info_nef_S = ['_nef_chemical_shift']
                minimal_info_nef_R = ['_nef_distance_restraint']
                minimal_info_nmrstar_A = ['_Atom_chem_shift', '_Gen_dist_constraint']
                minimal_info_nmrstar_S = ['_Atom_chem_shift']
                minimal_info_nmrstar_R = ['_Gen_dist_constraint']

                (sf_list, lp_list) = self.GetSTARInfo(self.inData, file_info[1])
                msg = "{} saveframes and {} loops found".format(len(sf_list), len(lp_list))
                INFO.append(msg)
                nef_sf_list = [i for i in sf_list if 'nef' in i]
                nef_lp_list = [i for i in lp_list if 'nef' in i]
                msg = "{} saveframes and {} loops found with nef prefix".format(len(nef_sf_list), len(nef_lp_list))
                INFO.append(msg)
                if len(nef_sf_list) > 0 or len(nef_lp_list) > 0:
                    isNEFfile = True
                    msg = "{} is a NEF file".format(inFile)
                    file_typ = 'NEF'
                else:
                    isNEFfile = False
                    msg = "{} is a NMR-STAR file".format(inFile)
                    file_typ = "NMR-STAR"
                INFO.append(msg)
                if isNEFfile:
                    isValid = True
                    if fileType == "A":
                        for lp_info in minimal_info_nef_A:
                            if lp_info not in lp_list:
                                isValid = False
                                ERROR.append('{} loop not found'.format(lp_info))
                            else:
                                if self.IsEmptyLoop(self.inData, lp_info, file_info[1]):
                                    isValid = False
                                    ERROR.append('{} loop is empty'.format(lp_info))
                    elif fileType == "S":
                        for lp_info in minimal_info_nef_S:
                            if lp_info not in lp_list:
                                isValid = False
                                ERROR.append('{} loop not found'.format(lp_info))
                            else:
                                if self.IsEmptyLoop(self.inData, lp_info, file_info[1]):
                                    isValid = False
                                    ERROR.append('{} loop is empty'.format(lp_info))
                    elif fileType == "R":
                        for lp_info in minimal_info_nef_R:
                            if lp_info not in lp_list:
                                isValid = False
                                ERROR.append('{} loop not found'.format(lp_info))
                            else:
                                if self.IsEmptyLoop(self.inData, lp_info, file_info[1]):
                                    isValid = False
                                    ERROR.append('{} loop is empty'.format(lp_info))
                    else:
                        msg = "fileType flag should be A/S/R"
                        ERROR.append(msg)
                        isValid = False
                else:
                    isValid = True
                    if fileType == "A":
                        for lp_info in minimal_info_nmrstar_A:
                            if lp_info not in lp_list:
                                isValid = False
                                ERROR.append('{} loop not found'.format(lp_info))
                            else:
                                if self.IsEmptyLoop(self.inData, lp_info, file_info[1]):
                                    isValid = False
                                    ERROR.append('{} loop is empty'.format(lp_info))
                    elif fileType == "S":
                        for lp_info in minimal_info_nmrstar_S:
                            if lp_info not in lp_list:
                                isValid = False
                                ERROR.append('{} loop not found'.format(lp_info))
                            else:
                                if self.IsEmptyLoop(self.inData, lp_info, file_info[1]):
                                    isValid = False
                                    ERROR.append('{} loop is empty'.format(lp_info))
                    elif fileType == "R":
                        for lp_info in minimal_info_nmrstar_R:
                            if lp_info not in lp_list:
                                isValid = False
                                ERROR.append('{} loop not found'.format(lp_info))
                            else:
                                if self.IsEmptyLoop(self.inData, lp_info, file_info[1]):
                                    isValid = False
                                    ERROR.append('{} loop is empty'.format(lp_info))
                    else:
                        msg = "fileType flag should be A/S/R"
                        ERROR.append(msg)
                        isValid = False

                # INFO.append(isNEFfile)
            else:
                ERROR.append(file_info[1])
                isValid = False
        except IOError as e:
            msg = "File not found {}".format(inFile)
            ERROR.append(msg)
            isValid = "ERROR"

        return (isValid, json.dumps({'INFO': INFO, 'WARNING': WARNING, 'ERROR': ERROR, 'FILE': file_typ}))

    @staticmethod
    def IsEmptyLoop(starData, lpCategory, dflag):
        isLoopHasData = False
        if dflag == "Entry":
            lp_data = starData.get_loops_by_category(lpCategory)
            isLoopHasData = False
            for lpd in lp_data:
                if len(lpd.data) == 0:
                    isLoopHasData = True
        elif dflag == "Saveframe":
            lp_data = starData.get_loop_by_category(lpCategory)
            isLoopHasData = False

            if len(lp_data.data) == 0:
                isLoopHasData = True
        else:
            if len(starData.data) == 0:
                isLoopHasData = True
        return isLoopHasData

    @staticmethod
    def GetSTARInfo(starData, dflag):
        sf_list = []
        lp_list = []
        if dflag == "Entry":
            for sf in starData.frame_list:
                sf_list.append(sf.category)
                for lp in sf:
                    lp_list.append(lp.category)
        elif dflag == "Saveframe":
            for lp in starData:
                lp_list.append(lp.category)
        else:
            lp_list.append(starData.category)
        return (sf_list, lp_list)

    def getSeqFromCS(self, inFile):
        (flg, jsondata) = self.ValidateFile(inFile, 'S')
        dat = json.loads(jsondata)
        INFO = dat['INFO']
        WARNING = dat['WARNING']
        ERROR = dat['ERROR']
        isOk = False
        if flg:
            INFO.append('File successfully read')
            inDat = self.readInFile(inFile)[-1]
            if dat['FILE'] == "NMR-STAR":
                INFO.append('NMR-STAR')
                sq = self.GetNMRSTARSeq(inDat)
                if len(sq):
                    isOk = True
                else:
                    ERROR.append("Can't extract sequence from chemical shift loop")
            elif dat['FILE'] == "NEF":
                INFO.append('NEF')
                sq = self.GetNEFSeq(inDat)
                if len(sq):
                    isOk = True
                else:
                    ERROR.append("Can't extract sequence from chemical shift loop")
            else:
                ERROR.append("Can't identify file type, it is neither NEF nor NMR-STAR")
        else:
            sq = []
            ERROR.append('File validation failed (or) File contains no chemical shift information')
        return (isOk, json.dumps({'INFO': INFO, 'WARNING': WARNING, 'ERROR': ERROR, 'FILE': dat['FILE'], 'DATA': sq}))

    def GetNEFSeq(self, strData, lp_category='nef_chemical_shift', seq_id='sequence_code', res_id='residue_name',
                  chain_id='chain_code'):
        '''Extracts sequence from any given loop from a NEF file'''
        try:
            csLoop = strData.get_loops_by_category(lp_category)
        except AttributeError:
            try:
                csLoop = [strData.get_loop_by_category(lp_category)]
            except AttributeError:
                csLoop = [strData]
        seq = []
        for csl in csLoop:
            seq_dict = {}
            seqdat = csl.get_data_by_tag([seq_id, res_id, chain_id])
            chains = ((set([i[2] for i in seqdat])))
            seq1 = (sorted(set(['{}-{:03d}-{}'.format(i[2], int(i[0]), i[1]) for i in seqdat])))

            if len(seq1[0].split("-")[-1]) > 1:
                if len(chains) > 1:
                    for c in chains:
                        # seq2 = "".join([self.getOneLetter(i.split("-")[-1]) for i in seq1 if i.split("-")[0] == c])
                        seq2 = [i.split("-")[-1] for i in seq1 if i.split("-")[0] == c]
                        seq_dict[c] = seq2
                else:
                    # seq2 = "".join([self.getOneLetter(i.split("-")[-1]) for i in seq1])
                    seq2 = [i.split("-")[-1] for i in seq1]
                    seq_dict[list(chains)[0]] = seq2
            else:
                if len(chains) > 1:
                    for c in chains:
                        # seq2 = "".join([i.split("-")[-1] for i in seq1 if i.split("-")[0] == c])
                        seq2 = [i.split("-")[-1] for i in seq1 if i.split("-")[0] == c]
                        seq_dict[c] = seq2
                else:
                    # seq2 = "".join([i.split("-")[-1] for i in seq1])
                    seq2 = [i.split("-")[-1] for i in seq1]
                    seq_dict[list(chains)[0]] = seq2
            seq.append(seq_dict)
        return seq

    def GetNMRSTARSeq(self, strData, lp_category='Atom_chem_shift', seq_id='Comp_index_ID', res_id='Comp_ID',
                      chain_id='Entity_assembly_ID'):
        '''Extracts sequence from any given NMR-STAR file'''
        try:
            csLoop = strData.get_loops_by_category(lp_category)
        except AttributeError:
            try:
                csLoop = [strData.get_loop_by_category(lp_category)]
            except AttributeError:
                csLoop = [strData]
        seq = []
        for csl in csLoop:
            seq_dict = {}
            if '_{}.Entity_assembly_ID'.format(lp_category) not in csl.get_tag_names():
                seqdat = csl.get_data_by_tag([seq_id, res_id])
                for i in seqdat:
                    i.append(".")
            else:
                seqdat = csl.get_data_by_tag([seq_id, res_id, chain_id])

            chains = ((set([i[2] for i in seqdat])))
            seq1 = (sorted(set(['{}-{:03d}-{}'.format(i[2], int(i[0]), i[1]) for i in seqdat])))
            if len(seq1[0].split("-")[-1]) > 1:
                if len(chains) > 1:
                    for c in chains:
                        # seq2 = "".join([self.getOneLetter(i.split("-")[-1]) for i in seq1 if i.split("-")[0] == c])
                        seq2 = [i.split("-")[-1] for i in seq1 if i.split("-")[0] == c]
                        seq_dict[c] = seq2
                else:
                    # seq2 = "".join([self.getOneLetter(i.split("-")[-1]) for i in seq1])
                    seq2 = [i.split("-")[-1] for i in seq1]
                    seq_dict[list(chains)[0]] = seq2
            else:
                if len(chains) > 1:
                    for c in chains:
                        # seq2 = "".join([i.split("-")[-1] for i in seq1 if i.split("-")[0] == c])
                        seq2 = [i.split("-")[-1] for i in seq1 if i.split("-")[0] == c]
                        seq_dict[c] = seq2
                else:
                    # seq2 = "".join([i.split("-")[-1] for i in seq1])
                    seq2 = [i.split("-")[-1] for i in seq1]
                    seq_dict[list(chains)[0]] = seq2
            seq.append(seq_dict)
        return seq

    def ValidateAtom(self, starData, lpCategory='Atom_chem_shift', seq_id='Comp_index_ID', res_id='Comp_ID',
                     atom_id='Atom_ID'):
        '''
        Validates the atoms in a given loop against IUPAC standard

        '''
        try:
            loop_data = starData.get_loops_by_category(lpCategory)
        except AttributeError:
            try:
                loop_data = [starData.get_loop_by_category(lpCategory)]
            except AttributeError:
                loop_data = [starData]

        ns = []
        for lp in loop_data:
            try:
                atm_data = lp.get_data_by_tag([seq_id, res_id, atom_id])
                for i in atm_data:
                    try:
                        if i[2] not in self.atomDict[i[1].upper()]:
                            ns.append(i)
                    except KeyError:
                        ns.append(i)
            except ValueError:
                print("One of the following tag is missing ", seq_id, res_id, atom_id)

            # nonStandard = [i for i in atm_data if i[2] not in self.atomDict[i[1].upper]]
            # ns.append(nonStandard)
        return ns

    def getNMRSTARtag(self, tag):
        n = self.tagMap[0].index(tag)
        return [self.tagMap[1][n], self.tagMap[2][n]]

    # def getNEFtag(self, tag):
    #     n = self.tagMap[1].index(tag)
    #     return self.tagMap[0][n]

    def getNMRSTARlooptags(self, neflooptags):
        aut_tag = []
        nt = []
        for t in neflooptags:
            st = self.getNMRSTARtag(t)
            if st[0] != st[1]:
                aut_tag.append(st[1])
            nt.append(st[0])
        if len(aut_tag) != 0:
            out_tag = nt + aut_tag
        else:
            out_tag = nt
        if neflooptags[0].split(".")[0] == "_nef_chemical_shift":
            out_tag.append('_Atom_chem_shift.Ambiguity_code')
            out_tag.append('_Atom_chem_shift.Ambiguity_set_ID')
            out_tag.append('_Atom_chem_shift.Assigned_chem_shift_list_ID')
        if neflooptags[0].split(".")[0] == "_nef_distance_restraint":
            out_tag.append('_Gen_dist_constraint.Member_logic_code')

        return out_tag

    def getSTARatom(self, res, nefAtom):
        '''
        Returns (atom with out wildcard,[IUPAC atom list],ambiguity code)

        '''
        ac = 1
        try:
            atms = self.atomDict[res]
            alist = []
            try:
                refatm = re.findall(r'(\S+)([xyXY])([%*])$|(\S+)([%*])$|(\S+)([xyXY]$)', nefAtom)[0]
                atm_set = [refatm.index(i) for i in refatm if i != ""]
                if atm_set == [0, 1, 2]:
                    aaa = refatm[0]
                    pattern = re.compile(r'%s\S\d+' % (refatm[0]))
                    alist2 = [i for i in atms if re.search(pattern, i)]
                    xid = sorted(set([int(i[len(refatm[0])]) for i in alist2]))
                    if refatm[1] == "x" or refatm[1] == "X":
                        alist = [i for i in alist2 if int(i[len(refatm[0])]) == xid[0]]
                    else:
                        alist = [i for i in alist2 if int(i[len(refatm[0])]) == xid[1]]
                    ac = 2
                elif atm_set == [3, 4]:
                    aaa = refatm[3]
                    if refatm[4] == "%":
                        pattern = re.compile(r'%s\d+' % (refatm[3]))
                    elif refatm[4] == "*":
                        pattern = re.compile(r'%s\S+' % (refatm[3]))
                    else:
                        looging.critical("Wrong NEF atom {}".format(nefAtom))
                    alist = [i for i in atms if re.search(pattern, i)]
                    ac = 1

                elif atm_set == [5, 6]:
                    aaa = refatm[5]
                    pattern = re.compile(r'%s\S+' % (refatm[5]))
                    alist = [i for i in atms if re.search(pattern, i)]
                    if len(alist) != 2:
                        alist = []
                    elif refatm[6] == "y" or refatm[6] == "Y":
                        # alist.reverse()[]
                        alist = alist[-1:]
                    elif refatm[6] == "x" or refatm[6] == "X":
                        alist = alist[:1]
                    else:
                        looging.critical("Wrong NEF atom {}".format(nefAtom))
                    ac = 2

                else:
                    looging.critical("Wrong NEF atom {}".format(nefAtom))
            except IndexError:

                # print nefAtom
                pass
                aaa = nefAtom
            if len(alist) == 0:
                if nefAtom in atms:
                    alist.append(nefAtom)
                else:
                    if nefAtom == "H%":  # To handle terminal protons
                        alist = ['H1', 'H2', 'H3']
                        aaa = "H"
        except KeyError:
            # self.logfile.write("%s\tResidue not found,%s,%s\n"%(self.TimeStamp(time.time()),res,nefAtom))
            # print "Residue not found",res,nefAtom
            if res != ".": self.logger.critical("Non-standard residue found {}".format(res))
            alist = []
            aaa = nefAtom

            if nefAtom == "H%":
                alist = ['H1', 'H2', 'H3']
                aaa = "H"
        return (aaa, alist, ac)

    # def findAmbiguityCode(self, neflist):
    #     for nn in neflist:
    #         seqid = sorted(set([int(i[0]) for i in nn]))
    #         for sid in seqid:
    #             sqgroup = [i for i in nn if int(i[0]) == sid]
    #             sqatm = [i[2] for i in sqgroup]
    #             print("atm", sqatm)
    #             print([s for s in sqatm if ('C' in s and 'X' in s.upper()) or ('C' in s and 'Y' in s.upper()) or (
    #                     'H' in s and 'X' in s.upper()) or ('H' in s and 'Y' in s.upper())])

    def translate_cs_row(self, f_tags, t_tags, row_data):
        out_row = []

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
            n_atm = self.getSTARatom(row_data[res_index], row_data[atm_index])[1]
            ambi = self.getSTARatom(row_data[res_index], row_data[atm_index])[2]

            for i in n_atm:
                out = [None] * len(t_tags)
                for j in f_tags:
                    stgs = self.getNMRSTARtag(j)
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
    def get_identifier(tag_list):
        out_list = []
        for j in range(1, 16):
            out = [None] * 2
            chk_string = re.compile('\S+.chain_code_{}'.format(j))
            r1 = [chk_string.search(i).group() for i in tag_list if chk_string.search(i)]
            if len(r1) > 0: out[0] = r1[0]
            chk_string = re.compile('\S+.sequence_code_{}'.format(j))
            r2 = [chk_string.search(i).group() for i in tag_list if chk_string.search(i)]
            if len(r2) > 0: out[1] = r2[0]
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
        # print (f_tags)
        out_row = []
        res_list = self.get_identifier(f_tags)
        #print (res_list,f_tags)
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
                stgs = self.getNMRSTARtag(j)
                if stgs[0] == stgs[1]:
                    out[t_tags.index(stgs[0])] = row_data[f_tags.index(j)]
                else:
                    if 'chain_code' in j or 'sequence_code' in j:
                        out[t_tags.index(stgs[0])] = row_data[f_tags.index(j)]
                        out[t_tags.index(stgs[1])] = tmp_dict[j]
                    else:
                        out[t_tags.index(stgs[0])] = row_data[f_tags.index(j)]
                        out[t_tags.index(stgs[1])] = row_data[f_tags.index(j)]

                # else:
                #   print ("ERROR",f_tags)
            out_row.append(out)
        else:
            out_row.append(row_data)
        return out_row

    def translate_seq_row(self, f_tags, t_tags, row_data):
        out_row = []
        if len(f_tags) != len(t_tags):
            out = [None] * len(t_tags)
            for j in f_tags:
                stgs = self.getNMRSTARtag(j)
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
        out_row = []
        res_list = self.get_identifier(f_tags)
        #print (res_list,f_tags)
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
            n_atm1 = self.getSTARatom(row_data[res_index1], row_data[atm_index1])[1]
            n_atm2 = self.getSTARatom(row_data[res_index2], row_data[atm_index2])[1]

            for i in n_atm1:
                for k in n_atm2:
                    out = [None] * len(t_tags)
                    for j in f_tags:
                        stgs = self.getNMRSTARtag(j)
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

    def NEFtoNMRSTAR(self, nefFile):
        (filePath, fileName) = ntpath.split(os.path.realpath(nefFile))
        isDone = True
        INFO = []
        WARNING = []
        ERROR = []
        starFile = filePath + "/" + fileName.split(".")[0] + ".str"
        (isReadable, dat_content, nefData) = self.readInFile(nefFile)
        try:
            starData = pynmrstar.Entry.from_scratch(nefData.entry_id)
        except AttributeError:
            starData = pynmrstar.Entry.from_scratch(fileName.split(".")[0])
            WARNING.append('Not a complete Entry')
        if isReadable:
            if dat_content == "Entry":
                self.chains = sorted(list(set(nefData.get_loops_by_category('nef_sequence')[0].get_tag('chain_code'))))
            elif dat_content == "Saveframe":
                self.chains = sorted(list(set(nefData[0].get_tag('chain_code'))))
            elif dat_content == "Loop":
                self.chains = sorted(list(set(nefData.get_tag('chain_code'))))
            else:
                isDone = False
                ERROR.append('File content unknown')

            cs_list = 0
            if dat_content == "Entry":
                for saveframe in nefData:
                    sf = pynmrstar.Saveframe.from_scratch(saveframe.name)

                    for tag in saveframe.tags:
                        if tag[0].lower() == "sf_category":
                            sf.add_tag("Sf_category", self.getNMRSTARtag(saveframe.category)[0])
                        else:
                            neftag = '{}.{}'.format(saveframe.tag_prefix, tag[0])
                            sf.add_tag(self.getNMRSTARtag(neftag)[0], tag[1])
                    if saveframe.category == "nef_nmr_meta_data":
                        sf.add_tag("NMR_STAR_version", "3.2.0.15")
                        #sf.add_tag("Generated_date", self.TimeStamp(time.time()), update=True)
                        try:
                            lp1=saveframe.get_loop_by_category('_nef_program_script')
                            lp1.add_data(['NEFTranslator','NEFtoNMRSTAR','.'])
                            #print (lp1.tags)
                        except KeyError:
                            pass # May be better to add audit loop
                    for loop in saveframe:
                        if loop.category == "_nef_sequence":
                            self.cid = []  # Comp_index_ID list
                            for c in self.chains:  # Comp_index_ID initialized with 1
                                self.cid.append(1)
                            self.seqDict = {}

                        if loop.category == '_nef_distance_restraint':
                            r_index_id = 1
                        if loop.category == "_nef_chemical_shift":
                            cs_list += 1
                        lp = pynmrstar.Loop.from_scratch()
                        lp_cols = self.getNMRSTARlooptags(loop.get_tag_names())
                        for t in lp_cols:
                            lp.add_tag(t)
                        # print (loop.category,lp.category,lp.get_tag_names(),loop.get_tag_names())
                        for dat in loop.data:
                            if loop.category == "_nef_sequence":
                                dd = self.translate_seq_row(loop.get_tag_names(), lp.get_tag_names(), dat)
                                self.cid[
                                    self.chains.index(dat[loop.get_tag_names().index('_nef_sequence.chain_code')])] += 1
                                for d in dd:
                                    lp.add_data(d)
                                    self.seqDict[(dat[loop.get_tag_names().index('_nef_sequence.chain_code')],
                                                  dat[loop.get_tag_names().index('_nef_sequence.sequence_code')])] = (
                                        d[lp.get_tag_names().index('_Chem_comp_assembly.Entity_assembly_ID')],
                                        d[lp.get_tag_names().index('_Chem_comp_assembly.Comp_index_ID')])

                            elif loop.category == "_nef_chemical_shift":
                                dd = self.translate_cs_row(loop.get_tag_names(), lp.get_tag_names(), dat)
                                for d in dd:
                                    d[lp.get_tag_names().index(
                                        '_Atom_chem_shift.Assigned_chem_shift_list_ID')] = cs_list
                                    lp.add_data(d)
                            elif loop.category == '_nef_distance_restraint':
                                dd = self.translate_restraint_row(loop.get_tag_names(), lp.get_tag_names(), dat)

                                for d in dd:
                                    d[lp.get_tag_names().index('_Gen_dist_constraint.Index_ID')] = r_index_id
                                    if len(dd) > 1:
                                        d[lp.get_tag_names().index('_Gen_dist_constraint.Member_logic_code')] = "OR"
                                    lp.add_data(d)
                                    r_index_id += 1
                            else:
                                dd = self.translate_row(loop.get_tag_names(), lp.get_tag_names(), dat)
                                for d in dd:
                                    lp.add_data(d)

                        # print (loop.data[0])
                        sf.add_loop(lp)
                    starData.add_saveframe(sf)
                starData.normalize()
                with open(starFile, 'w') as wstarfile:
                    wstarfile.write(str(starData))
            elif dat_content == "Saveframe" or dat_content == "Loop":
                if dat_content == "Saveframe":
                    saveframe = nefData
                    sf = pynmrstar.Saveframe.from_scratch(saveframe.name)
                    for tag in saveframe.tags:
                        if tag[0].lower() == "sf_category":
                            try:

                                sf.add_tag("Sf_category", self.getNMRSTARtag(saveframe.category)[0])
                            except ValueError:
                                sf.add_tag("Sf_category", self.getNMRSTARtag(tag[1])[0])
                        else:
                            neftag = '{}.{}'.format(saveframe.tag_prefix, tag[0])
                            sf.add_tag(self.getNMRSTARtag(neftag)[0], tag[1])
                    if saveframe.category == "nef_nmr_meta_data":
                        sf.add_tag("NMR_STAR_version", "3.2.0.15")

                else:
                    sf = pynmrstar.Saveframe.from_scratch(nefData.category)
                    if nefData.category == "_nef_chemical_shift":
                        sf.add_tag("_Assigned_chem_shift_list.Sf_category", 'nef_chemical_shift')
                    saveframe = [nefData]
                for loop in saveframe:
                    if loop.category == "_nef_sequence":
                        self.cid = []  # Comp_index_ID list
                        for c in self.chains:  # Comp_index_ID initialized with 1
                            self.cid.append(1)
                        self.seqDict = {}

                    if loop.category == '_nef_distance_restraint':
                        r_index_id = 1
                    if loop.category == "_nef_chemical_shift":
                        cs_list += 1
                    lp = pynmrstar.Loop.from_scratch()
                    lp_cols = self.getNMRSTARlooptags(loop.get_tag_names())
                    for t in lp_cols:
                        lp.add_tag(t)
                    # print (loop.category,lp.category,lp.get_tag_names(),loop.get_tag_names())
                    for dat in loop.data:
                        if loop.category == "_nef_sequence":
                            dd = self.translate_seq_row(loop.get_tag_names(), lp.get_tag_names(), dat)
                            self.cid[
                                self.chains.index(dat[loop.get_tag_names().index('_nef_sequence.chain_code')])] += 1
                            for d in dd:
                                lp.add_data(d)
                                self.seqDict[(dat[loop.get_tag_names().index('_nef_sequence.chain_code')],
                                              dat[loop.get_tag_names().index('_nef_sequence.sequence_code')])] = (
                                    d[lp.get_tag_names().index('_Chem_comp_assembly.Entity_assembly_ID')],
                                    d[lp.get_tag_names().index('_Chem_comp_assembly.Comp_index_ID')])

                        elif loop.category == "_nef_chemical_shift":
                            dd = self.translate_cs_row(loop.get_tag_names(), lp.get_tag_names(), dat)
                            for d in dd:
                                d[lp.get_tag_names().index('_Atom_chem_shift.Assigned_chem_shift_list_ID')] = cs_list
                                lp.add_data(d)
                        elif loop.category == '_nef_distance_restraint':
                            dd = self.translate_restraint_row(loop.get_tag_names(), lp.get_tag_names(), dat)

                            for d in dd:
                                d[lp.get_tag_names().index('_Gen_dist_constraint.Index_ID')] = r_index_id
                                if len(dd) > 1:
                                    d[lp.get_tag_names().index('_Gen_dist_constraint.Member_logic_code')] = "OR"
                                lp.add_data(d)
                                r_index_id += 1
                        else:
                            dd = self.translate_row(loop.get_tag_names(), lp.get_tag_names(), dat)
                            for d in dd:
                                lp.add_data(d)

                    # print (loop.data[0])
                    sf.add_loop(lp)
                starData.add_saveframe(sf)
            starData.normalize()
            with open(starFile, 'w') as wstarfile:
                wstarfile.write(str(starData))

        else:
            isDone = False
            ERROR.append('Input file not readable')
        return (isDone, json.dumps({'INFO': INFO, 'WARNING': WARNING, 'ERROR': ERROR}))


if __name__ == "__main__":
    # fname = sys.argv[1]

    bt = NEFTranslator()
    bt.NEFtoNMRSTAR('data/2mqq.nef')
