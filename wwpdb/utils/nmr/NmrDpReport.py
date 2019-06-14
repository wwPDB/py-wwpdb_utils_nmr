##
# File: NmrDpReport.py
# Date: 14-Jun-2019
#
# Updates:
##
""" Wrapper class for data processing report of NMR unified data.
"""
import logging
import json
import types
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
                                         'status': 'OK'},
                         'error': None,
                         'warning': None }

        self.status_codes = ('OK', 'ERROR', 'WARNING')

        self.input_sources = [NmrDpReportInputSource()]
        self.sequence_alignment = NmrDpReportSequenceAlignment()
        self.chain_assignment = NmrDpReportChainAssignment()
        self.error = NmrDpReportError()
        self.warning = NmrDpReportWarning()

    def addInputSource(self):
        self.input_sources.append(NmrDpReportInputSource())

    def isOk(self):
        return self.__report['information']['status'] == 'OK'

    def isError(self):
        return self.__report['information']['status'] == 'ERROR'

    def isDiamagnetic(self):
        return self.__report['information']['diamagnetic']

    def getInputSourceIdOfCoord(self):
        """ Return input_source_id of coordinate file.
            @return: index id of input_source, otherwise -1
        """

        for i in self.input_sources:
            if i.get()['file_type'] is 'pdbx':
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

            self.__setStatus('ERROR')

        else:
            logging.warning('+NmrDpReport.setError() ++ Warning  - No effects on NMR data processing report because the report is immutable')
            raise UserWarning('+NmrDpReport.setError() ++ Warning  - No effects on NMR data processing report because the report is immutable')

    def setWarning(self):

        if not self.__immutable:
            self.__report['warning'] = self.warning.get()

            if not self.isError():
                self.__setStatus('WARNING')

        else:
            logging.warning('+NmrDpReport.setWarning() ++ Warning  - No effects on NMR data processing report because the report is immutable')
            raise UserWarning('+NmrDpReport.setWarning() ++ Warning  - No effects on NMR data processing report because the report is immutable')

    def setDiamagnetic(self, diamagnetic):

        if type(diamagnetic) is types.BooleanType:
            self.__report['information']['diamagnetic'] = diamagnetic

        else:
            logging.warning('+NmrDpReport.setDiamagnetic() ++ Warning  - No effects on NMR data processing report because input variable is not boolean type')
            raise UserDiamagnetic('+NmrDpReport.setWarning() ++ Warning  - No effects on NMR data processing report because input variable is not boolean type')

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
        return json.dumps(self.get(), indent=indent_spaces)

    def writeJson(self, out_path):
        if out_path is None:
            return self.getJson()

        with open(out_path, encoding='utf-8') as file:
            file.write(json.dumps(self.get(), indent=2))

class NmrDpReportInputSource:
    """ Wrapper class for data processing report of NMR unified data (input source).
    """

    def __init__(self):
        self.items = ('file_name', 'file_type', 'content_type', 'content_subtype',
                      'polymer_sequence', 'polymer_sequence_in_loop',
                      'non_standard_residue',
                      'stats_of_exptl_data')
        self.file_types = ('pdbx', 'nef', 'nmr-star')
        self.content_types = ('model', 'nmr-unified-data')
        self.content_subtypes = ('coordinate', 'entry_info', 'poly_seq', 'chem_shift', 'dist_restraint', 'dihed_restraint', 'rdc_restraint', 'spectral_peak')

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
        self.chk_rows_key_pat = re.compile(r'^(.*) (.*)$')

    def appendDescription(self, item, value):

        if item in self.items:

            if self.__contents[item] is None:
                self.__contents[item] = []

            if 'category' in value:
                value['category'] = value['category'].lstrip('_')

            if not item is 'internal_error' and 'description' in value:
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

    def getTotal(self):
        return self.__contents['total']

class NmrDpReportWarning:
    """ Wrapper class for data processing report of NMR unified data (warning).
    """

    def __init__(self):
        self.items = ('missing_content', 'missing_saveframe', 'missing_data', 'enum_failure',
                      'disordered_index', 'sequence_mismatch', 'atom_nomenclature_mismatch',
                      'skipped_sf_category', 'skipped_lp_category', 'suspicious_data', 'unusual_data', 'remarkable_data')

        self.__contents = {item:None for item in self.items}

        self.__contents['total'] = 0

        self.chk_row_pat = re.compile(r'^\[Check row of (.*)\] (.*)$')

    def appendDescription(self, item, value):

        if item in self.items:

            if self.__contents[item] is None:
                self.__contents[item] = []

            if 'category' in value:
                value['category'] = value['category'].lstrip('_')

            if not item is 'internal_error' and 'description' in value:
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

    def getTotal(self):
        return self.__contents['total']
