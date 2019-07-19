##
# File: NmrDpReport.py
# Date: 17-Jul-2019
#
# Updates:
##
""" Wrapper class for data processing report of NMR unified data.
"""
import logging
import json
import re

class NmrDpReport:
    """ Wrapper class for data processing report of NMR unified data.
    """

    def __init__(self):
        self.__immutable = False

        self.__report = {'information': {'input_sources': [],
                                         'sequence_alignments': [],
                                         'chain_assignments': [],
                                         'diamagnetic': True,
                                         'disulfide_bond': False,
                                         'other_bond': False,
                                         'cyclic_polymer': False,
                                         'status': 'OK'
                                         },
                         'error': None,
                         'warning': None,
                         'corrected_warning': None
                         }

        self.status_codes = ('OK', 'Error', 'Warning')

        self.input_sources = [NmrDpReportInputSource()]
        self.sequence_alignment = NmrDpReportSequenceAlignment()
        self.chain_assignment = NmrDpReportChainAssignment()
        self.error = NmrDpReportError()
        self.warning = NmrDpReportWarning()
        self.corrected_warning = None

    def appendInputSource(self):
        self.input_sources.append(NmrDpReportInputSource())

    def isOk(self):
        return self.__report['information']['status'] == 'OK'

    def isError(self):
        return self.__report['information']['status'] == 'Error'

    def isDiamagnetic(self):
        return self.__report['information']['diamagnetic']

    def hasDisulfideBond(self):
        return self.__report['information']['disulfide_bond']

    def hasOtherBond(self):
        return self.__report['information']['other_bond']

    def hasCyclicPolymer(self):
        return self.__report['information']['cyclic_polymer']

    def getInputSource(self, id):
        """ Return input source of a given index.
            @return: input source of a given index, None otherwise
        """

        if id < 0 or id >= len(self.input_sources):
            return None

        return self.input_sources[id]

    def getInputSourceIdOfNmrUnifiedData(self):
        """ Return input_source_id of NMR unified data file.
            @return: index of input source of NMR unified data file, -1 otherwise
        """

        for i in self.input_sources:
            if i.get()['file_type'] in ['nef', 'nmr-star']:
                return self.input_sources.index(i)

        return -1

    def getInputSourceIdOfCoord(self):
        """ Return input_source_id of coordinate file.
            @return: index of input source of coordinate file, -1 otherwise
        """

        for i in self.input_sources:
            if i.get()['file_type'] == 'pdbx':
                return self.input_sources.index(i)

        return -1

    def getTotalErrors(self):
        return self.error.getTotal()

    def getTotalWarnings(self):
        return self.warning.getTotal()

    def __setStatus(self, status):

        if status in self.status_codes:
            self.__report['information']['status'] = status
        else:
            logging.error('+NmrDpReport.__setStatus() ++ Error  - Unknown item type %s' % item)
            raise KeyError('+NmrDpReport.__setStatus() ++ Error  - Unknown item type %s' % item)

    def setError(self):

        if not self.__immutable:
            self.__report['error'] = self.error.get()

            self.__setStatus('Error')

        else:
            logging.warning('+NmrDpReport.setError() ++ Warning  - No effects on NMR data processing report because the report is immutable')
            raise UserWarning('+NmrDpReport.setError() ++ Warning  - No effects on NMR data processing report because the report is immutable')

    def setWarning(self):

        if not self.__immutable:
            self.__report['warning'] = self.warning.get()

            if not self.isError():
                self.__setStatus('Warning')

        else:
            logging.warning('+NmrDpReport.setWarning() ++ Warning  - No effects on NMR data processing report because the report is immutable')
            raise UserWarning('+NmrDpReport.setWarning() ++ Warning  - No effects on NMR data processing report because the report is immutable')

    def setDiamagnetic(self, diamagnetic):

        if type(diamagnetic) is bool:
            self.__report['information']['diamagnetic'] = diamagnetic

        else:
            logging.warning('+NmrDpReport.setDiamagnetic() ++ Warning  - No effects on NMR data processing report because input variable is not boolean type')
            raise UserDiamagnetic('+NmrDpReport.setDiamagnetic() ++ Warning  - No effects on NMR data processing report because input variable is not boolean type')

    def setDisulfideBond(self, disulfide_bond):

        if type(disulfide_bond) is bool:
            self.__report['information']['disulfide_bond'] = disulfide_bond

        else:
            logging.warning('+NmrDpReport.setDisulfideBond() ++ Warning  - No effects on NMR data processing report because input variable is not boolean type')
            raise UserDiamagnetic('+NmrDpReport.setDisulfideBond() ++ Warning  - No effects on NMR data processing report because input variable is not boolean type')

    def setOtherBond(self, other_bond):

        if type(other_bond) is bool:
            self.__report['information']['other_bond'] = other_bond

        else:
            logging.warning('+NmrDpReport.setOtherBond() ++ Warning  - No effects on NMR data processing report because input variable is not boolean type')
            raise UserDiamagnetic('+NmrDpReport.setOtherBond() ++ Warning  - No effects on NMR data processing report because input variable is not boolean type')

    def setCyclicPolymer(self, cyclic_polymer):

        if type(cyclic_polymer) is bool:
            self.__report['information']['cyclic_polymer'] = cyclic_polymer

        else:
            logging.warning('+NmrDpReport.setCyclicPolymer() ++ Warning  - No effects on NMR data processing report because input variable is not boolean type')
            raise UserDiamagnetic('+NmrDpReport.setCyclicPolymer() ++ Warning  - No effects on NMR data processing report because input variable is not boolean type')

    def setMutable(self):
        self.__immutable = False

    def get(self):

        if not self.__immutable:
            self.__report['information']['input_sources'] = [input_source.get() for input_source in self.input_sources]
            self.__report['information']['sequence_alignments'] = self.sequence_alignment.get()
            self.__report['information']['chain_assignments'] = self.chain_assignment.get()

            self.__immutable = True

        return self.__report

    def getJson(self, indent_spaces=None):
        """ Return JSON content of NMR data processing report.
            @return: JSON content of NMR data processing report
        """

        if self.get() is None:
            return None

        return json.dumps(self.get(), indent=indent_spaces)

    def writeJson(self, out_path):
        """ Write NMR data processing report as JSON file.
            @return: True for success or False otherwise
        """

        if self.get() is None:
            return False

        with open(out_path, 'w') as file:
            file.write(json.dumps(self.get(), indent=2))

        return True

    def loadJson(self, in_path):
        """ Retrieve NMR data processing report from JSON file.
            @return: True for success or False otherwise
        """

        with open(in_path, 'r') as file:
            self.__report = json.loads(file.read())

        if self.__report is None:
            return False

        self.input_sources = []

        for contents in self.__report['information']['input_sources']:

            input_source = NmrDpReportInputSource()
            input_source.put(contents)

            self.input_sources.append(input_source)

        self.sequence_alignment.put(self.__report['information']['sequence_alignments'])
        self.chain_assignment.put(self.__report['information']['chain_assignments'])
        self.error.put(self.__report['error'])
        self.warning.put(self.__report['warning'])

        self.setMutable()

        return True

    def inheritFormatIssueErrors(self, prev_report):
        """ Inherit format issue errors from previous report (e.g. nmr-*-consistency-check workflow operation).
        """

        item = 'format_issue'

        if not self.__immutable:

            file_name = self.input_sources[self.getInputSourceIdOfNmrUnifiedData()].get()['file_name']
            _file_name = prev_report.input_sources[prev_report.getInputSourceIdOfNmrUnifiedData()].get()['file_name']

            value_list = prev_report.error.getValueList(item, _file_name)

            if value_list is None:
                return

            for c in value_list:

                if 'file_name' in c:
                    c['file_name'] = file_name

                self.error.appendDescription(item, c)

        else:
            logging.warning('+NmrDpReport.inheritFormatIssueErrors() ++ Warning  - No effects on NMR data processing report because the report is immutable')
            raise UserWarning('+NmrDpReport.inheritFormatIssueErrors() ++ Warning  - No effects on NMR data processing report because the report is immutable')

    def setCorrectedWarning(self, prev_report):
        """ Initialize history of corrected warnings in previous report.
        """

        if not self.__immutable:

            self.corrected_warning = NmrDpReportWarning()

            file_name = self.input_sources[self.getInputSourceIdOfNmrUnifiedData()].get()['file_name']
            _file_name = prev_report.input_sources[prev_report.getInputSourceIdOfNmrUnifiedData()].get()['file_name']

            for item in prev_report.warning.get().keys():

                if item == 'total':
                    continue

                value_list = self.warning.getValueList(item, file_name)
                _value_list = prev_report.warning.getUniqueValueList(item, _file_name)

                if _value_list is None:
                    continue

                list = []

                for _c in _value_list:

                    if value_list is None:
                        list.append(_c)

                    else:
                        try:
                            next(c for c in value_list if c['sf_framecode'] == _c['sf_framecode'] and c['description'] == _c['description'])
                        except StopIteration:
                            list.append(_c)

                for c in list:
                    self.corrected_warning.appendDescription(item, c)

            self.__report['corrected_warning'] = self.corrected_warning.get()

        else:
            logging.warning('+NmrDpReport.setCorrectedWarning() ++ Warning  - No effects on NMR data processing report because the report is immutable')
            raise UserWarning('+NmrDpReport.setCorrectedWarning() ++ Warning  - No effects on NMR data processing report because the report is immutable')

class NmrDpReportInputSource:
    """ Wrapper class for data processing report of NMR unified data (input source).
    """

    def __init__(self):
        self.items = ('file_name', 'file_type', 'content_type', 'content_subtype',
                      'polymer_sequence', 'polymer_sequence_in_loop',
                      'non_standard_residue', 'disulfide_bond',
                      'stats_of_exptl_data')
        self.file_types = ('pdbx', 'nef', 'nmr-star')
        self.content_types = ('model', 'nmr-unified-data-nef', 'nmr-unified-data-str')
        self.content_subtypes = ('coordinate', 'non_poly', 'entry_info', 'poly_seq', 'chem_shift', 'dist_restraint', 'dihed_restraint', 'rdc_restraint', 'spectral_peak')

        self.__contents = {item:None for item in self.items}

    def setItemValue(self, item, value):

        if item in self.items:

            if item == 'file_type' and not value in self.file_types:
                logging.error('+NmrDpReportInputSource.setItemValue() ++ Error  - Unknown file type %s' % value)
                raise ValueError('+NmrDpReportInputSource.setItemValue() ++ Error  - Unknown file type %s' % value)

            elif item == 'content_type' and not value in self.content_types:
                logging.error('+NmrDpReportInputSource.setItemValue() ++ Error  - Unknown content type %s' % value)
                raise ValueError('+NmrDpReportInputSource.setItemValue() ++ Error  - Unknown content type %s' % value)

            elif item == 'content_subtype':

                for k in value:

                    if not k in self.content_subtypes:
                        logging.error('+NmrDpReportInputSource.setItemValue() ++ Error  - Unknown content subtype in %s' % value.keys())
                        raise ValueError('+NmrDpReportInputSource.setItemValue() ++ Error  - Unknown content subtype in %s' % value.keys())

                non_positive_keys = [k for k in value if int(value[k]) <= 0]

                for k in non_positive_keys:
                    value.pop(k)

                if len(value) > 0:
                    self.__contents[item] = value

            else:
                self.__contents[item] = value

        else:
            logging.error('+NmrDpReportInputSource.setItemValue() ++ Error  - Unknown item type %s' % item)
            raise KeyError('+NmrDpReportInputSource.setItemValue() ++ Error  - Unknown item type %s' % item)

    def get(self):
        return self.__contents

    def put(self, contents):
        self.__contents = contents

    def updateNonStandardResidueByExptlData(self, chain_id, seq_id, content_subtype):
        """ Update specified non_starndard_residue by experimental data.
        """

        try:

            c = next(c for c in self.__contents['non_standard_residue'] if c['chain_id'] == chain_id)

            if seq_id in c['seq_id']:
                c['exptl_data'][c['seq_id'].index(seq_id)][content_subtype] = True

            else:
                logging.error('+NmrDpReportInputSource.updateNonStandardResidueByExptlData() ++ Error  - Unknown seq_id %s' % seq_id)
                raise KeyError('+NmrDpReportInputSource.updateNonStandardResidueByExptlData() ++ Error  - Unknown seq_id %s' % seq_id)

        except StopIteration:
            logging.error('+NmrDpReportInputSource.updateNonStandardResidueByExptlData() ++ Error  - Unknown chain_id %s' % chain_id)
            raise KeyError('+NmrDpReportInputSource.updateNonStandardResidueByExptlData() ++ Error  - Unknown chain_id %s' % chain_id)

class NmrDpReportSequenceAlignment:
    """ Wrapper class for data processing report of NMR unified data (sequence alignment).
    """

    def __init__(self):
        self.items = ('model_poly_seq_vs_coordinate', 'model_poly_seq_vs_nmr_poly_seq', 'nmr_poly_seq_vs_model_poly_seq', 'nmr_poly_seq_vs_chem_shift', 'nmr_poly_seq_vs_dist_restraint', 'nmr_poly_seq_vs_dihed_restraint', 'nmr_poly_seq_vs_rdc_restraint', 'nmr_poly_seq_vs_spectral_peak')

        self.__contents = {item:None for item in self.items}

    def setItemValue(self, item, value):

        if item in self.items:
            self.__contents[item] = value

        else:
            logging.error('+NmrDpReportSequenceAlignment.setItemValue() ++ Error  - Unknown item type %s' % item)
            raise KeyError('+NmrDpReportSequenceAlignment.setItemValue() ++ Error  - Unknown item type %s' % item)

    def get(self):
        return self.__contents

    def put(self, contents):
        self.__contents = contents

class NmrDpReportChainAssignment:
    """ Wrapper class for data processing report of NMR unified data (chain assignment).
    """

    def __init__(self):
        self.items = ('model_poly_seq_vs_nmr_poly_seq', 'nmr_poly_seq_vs_model_poly_seq')

        self.__contents = {item:None for item in self.items}

    def setItemValue(self, item, value):

        if item in self.items:
            self.__contents[item] = value

        else:
            logging.error('+NmrDpReportChainAssignment.setItemValue() ++ Error  - Unknown item type %s' % item)
            raise KeyError('+NmrDpReportChainAssignment.setItemValue() ++ Error  - Unknown item type %s' % item)

    def get(self):
        return self.__contents

    def put(self, contents):
        self.__contents = contents

class NmrDpReportError:
    """ Wrapper class for data processing report of NMR unified data (error).
    """

    def __init__(self):
        self.items = ('internal_error', 'format_issue', 'missing_mandatory_content', 'missing_mandatory_item', 'sequence_mismatch',
                      'invalid_data', 'invalid_atom_nomenclature', 'invalid_atom_type', 'invalid_isotope_number', 'invalid_ambiguity_code', 'multiple_data',
                      'missing_data', 'duplicated_index', 'anomalous_data')

        self.__contents = {item:None for item in self.items}

        self.__contents['total'] = 0

        self.chk_row_pat = re.compile(r'^\[Check row of (.*)\] (.*)$')
        self.chk_rows_pat = re.compile(r'\[Check rows of (.*)\] (.*)$')

    def appendDescription(self, item, value):

        if item in self.items:

            if self.__contents[item] is None:
                self.__contents[item] = []

            if item != 'internal_error' and 'category' in value:
                value['category'] = value['category'].lstrip('_')

            if item != 'internal_error' and 'description' in value:
                d = value['description']

                if d.startswith('[Check row of'):
                    g = self.chk_row_pat.search(d).groups()

                    loc = {}
                    for i in g[0].split(','):
                        p = i.lstrip()
                        s = p.index(' ')
                        loc[p[0:s]] = p[s:].lstrip()

                    value['row_location'] = loc
                    value['description'] = g[1]

                elif d.startswith('[Check rows of'):
                    g = self.chk_rows_pat.search(d).groups()

                    locs = {}
                    for i in g[0].split(','):
                        p = i.lstrip()
                        q = p.split(' ', 1)
                        locs[q[0]] = re.sub(' vs ', ',', q[1]).split(',')

                    value['row_locations'] = locs
                    value['description'] = g[1]

            self.__contents[item].append(value)

            self.__contents['total'] += 1

        else:
            logging.error('+NmrDpReportError.appendDescription() ++ Error  - Unknown item type %s' % item)
            raise KeyError('+NmrDpReportError.appendDescription() ++ Error  - Unknown item type %s' % item)

    def get(self):
        return self.__contents

    def put(self, contents):
        self.__contents = contents

    def getTotal(self):
        """ Return total number of errors.
            @return: total number of errors
        """

        return self.__contents['total']

    def exists(self, file_name, sf_framecode):
        """ Return whether an error specified by file name and saveframe exists.
            @return: True for an error exists or False otherwise
        """

        for item in self.__contents.keys():

            if item in ['total', 'internal_error'] or self.__contents[item] is None:
                continue

            try:
                next(c for c in self.__contents[item] if c['file_name'] == file_name and 'sf_framecode' in c and c['sf_framecode'] == sf_framecode)
                return True
            except StopIteration:
                pass

        return False

    def getValueList(self, item, file_name, key=None):
        """ Return list of error values specified by item name and file name.
        """

        if item in ['total', 'internal_error'] or self.__contents is None or (not item in self.__contents.keys()) or self.__contents[item] is None:
            return None

        return [c for c in self.__contents[item] if c['file_name'] == file_name or (key is None or key in c['description'])]

    def getValueListWithSf(self, item, file_name, sf_framecode, key=None):
        """ Return list of error values specified by item name, file name, and saveframe.
        """

        if item in ['total', 'internal_error'] or self.__contents is None or (not item in self.__contents.keys()) or self.__contents[item] is None:
            return None

        return [c for c in self.__contents[item] if c['file_name'] == file_name and c['sf_framecode'] == sf_framecode and (key is None or key in c['description'])]

    def getUniqueValueList(self, item, file_name):
        """ Return list of error values having unique sf_framecode and description.
        """

        if item in ['total', 'internal_error'] or self.__contents is None or (not item in self.__contents.keys()) or self.__contents[item] is None:
            return None

        list = []

        keys = set()

        for c in self.getValueList(item, file_name):

            key = c['sf_framecode'] + c['description']

            if key in keys:
                continue

            if 'row_location' in c:
                del c['row_location']

            elif 'row_locations' in c:
                del c['row_locations']

            list.append(c)

            keys.add(key)

        return list

    def getDescription(self, item, file_name, sf_framecode):
        """ Return error description specified by item name, file name, and saveframe.
        """

        if item in ['total', 'internal_error'] or self.__contents is None or (not item in self.__contents.keys()) or self.__contents[item] is None:
            return None

        try:
            c = next(c for c in self.__contents[item] if c['file_name'] == file_name and 'sf_framecode' in c and c['sf_framecode'] == sf_framecode)
            return c['description']
        except StopIteration:
            return None

    def getCombinedDescriptions(self, file_name, sf_framecode):
        """ Return combined error descriptions specified by file name and saveframe.
        """

        if self.__contents is None:
            return None

        d = []

        for item in self.items:

            if item == 'internal_error' or self.__contents[item] is None:
                continue

            for c in self.__contents[item]:

                if c['file_name'] == file_name and 'sf_framecode' in c and c['sf_framecode'] == sf_framecode:
                    d.append(item + ': ' + c['description'])

        if len(d) == 0:
            return None

        return d

class NmrDpReportWarning:
    """ Wrapper class for data processing report of NMR unified data (warning).
    """

    def __init__(self):
        self.items = ('missing_content', 'missing_saveframe', 'missing_data', 'enum_failure',
                      'disordered_index', 'sequence_mismatch', 'atom_nomenclature_mismatch', 'ccd_mismatch',
                      'skipped_sf_category', 'skipped_lp_category', 'suspicious_data', 'unusual_data', 'remarkable_data', 'unsufficient_data')

        self.__contents = {item:None for item in self.items}

        self.__contents['total'] = 0

        self.chk_row_pat = re.compile(r'^\[Check row of (.*)\] (.*)$')

    def appendDescription(self, item, value):

        if item in self.items:

            if self.__contents[item] is None:
                self.__contents[item] = []

            if 'category' in value:
                value['category'] = value['category'].lstrip('_')

            if 'description' in value:
                d = value['description']

                if d.startswith('[Check row of'):
                    g = self.chk_row_pat.search(d).groups()

                    loc = {}
                    for i in g[0].split(','):
                        p = i.lstrip()
                        s = p.index(' ')
                        loc[p[0:s]] = p[s:].lstrip()

                    value['row_location'] = loc
                    value['description'] = g[1]

            self.__contents[item].append(value)

            self.__contents['total'] += 1

        else:
            logging.error('+NmrDpReportWarning.appendDescription() ++ Error  - Unknown item type %s' % item)
            raise KeyError('+NmrDpReportWarning.appendDescription() ++ Error  - Unknown item type %s' % item)

    def get(self):
        return self.__contents

    def put(self, contents):
        self.__contents = contents

    def getTotal(self):
        """ Return total number of warnings.
            @return: total number of warnings
        """

        return self.__contents['total']

    def exists(self, file_name, sf_framecode):
        """ Return whether a warning specified by file name and saveframe exists.
            @return: True for a warning exists or False otherwise
        """

        for item in self.__contents.keys():

            if item == 'total' or self.__contents[item] is None:
                continue

            try:
                next(c for c in self.__contents[item] if c['file_name'] == file_name and 'sf_framecode' in c and c['sf_framecode'] == sf_framecode)
                return True
            except StopIteration:
                pass

        return False

    def getValueList(self, item, file_name, key=None):
        """ Return list of warning values specified by item name and file name.
        """

        if item == 'total' or self.__contents is None or (not item in self.__contents.keys()) or self.__contents[item] is None:
            return None

        return [c for c in self.__contents[item] if c['file_name'] == file_name and (key is None or key in c['description'])]

    def getValueListWithSf(self, item, file_name, sf_framecode, key=None):
        """ Return list of warning values specified by item name, file name, and saveframe.
        """

        if item == 'total' or self.__contents is None or (not item in self.__contents.keys()) or self.__contents[item] is None:
            return None

        return [c for c in self.__contents[item] if c['file_name'] == file_name and c['sf_framecode'] == sf_framecode and (key is None or key in c['description'])]

    def getUniqueValueList(self, item, file_name):
        """ Return list of warning values having unique sf_framecode and description.
        """

        if item == 'total' or self.__contents is None or (not item in self.__contents.keys()) or self.__contents[item] is None:
            return None

        list = []

        keys = set()

        for c in self.getValueList(item, file_name):

            key = c['sf_framecode'] + c['description']

            if key in keys:
                continue

            if 'row_location' in c:
                del c['row_location']

            elif 'row_locations' in c:
                del c['row_locations']

            list.append(c)

            keys.add(key)

        return list

    def getDescription(self, item, file_name, sf_framecode):
        """ Return warning description specified by item name, file name, and saveframe.
        """

        if item == 'total' or self.__contents is None or (not item in self.__contents.keys()) or self.__contents[item] is None:
            return None

        try:
            c = next(c for c in self.__contents[item] if c['file_name'] == file_name and 'sf_framecode' in c and c['sf_framecode'] == sf_framecode)
            return c['description']
        except StopIteration:
            return None

    def getCombinedDescriptions(self, file_name, sf_framecode):
        """ Return combined warning descriptions specified by file name and saveframe.
        """

        if self.__contents is None:
            return None

        d = []

        for item in self.items:

            if self.__contents[item] is None:
                continue

            for c in self.__contents[item]:

                if c['file_name'] == file_name and 'sf_framecode' in c and c['sf_framecode'] == sf_framecode:
                    d.append(item + ': ' + c['description'])

        if len(d) == 0:
            return None

        return d
