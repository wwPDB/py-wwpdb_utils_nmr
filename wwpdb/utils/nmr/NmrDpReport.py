##
# File: NmrDpReport.py
# Date: 14-May-2019
#
# Updates:
##
""" Wrapper class for data processing report of NMR unified data.
"""
import logging
import json

class NmrDpReport:
    """ Wrapper class for data processing report of NMR unified data.
    """

    def __init__(self):
        self.__complete = False

        self.__report = {'information': {'input_sources': [],
                                         'sequence_alignments': [],
                                         'status': 'OK'},
                         'error': None,
                         'warning': None }

        self.status_codes = ('OK', 'ERROR', 'WARNING')

        self.input_sources = [NmrDpReportInputSource()]
        self.sequence_alignment = NmrDpReportSequenceAlignment()
        self.error = NmrDpReportError()
        self.warning = NmrDpReportWarning()

    def addInputSource(self):
        self.input_sources.append(NmrDpReportInputSource())

    def isOk(self):
        return self.__report['information']['status'] == 'OK'

    def isError(self):
        return self.__report['information']['status'] == 'ERROR'

    def __setStatus(self, status):

        if status in self.status_codes:
            self.__report['information']['status'] = status
        else:
            logging.error('+NmrDpReport.__setStatus() Unknown item type %s' % item)
            raise KeyError('+NmrDpReport.__setStatus() Unknown item type %s' % item)

    def setError(self):

        if not self.__complete:
            self.__report['error'] = self.error.get()

            self.__setStatus('ERROR')

        else:
            logging.warning('+NmrDpReport.setError() No effects on NMR data processing report because the report is complete')
            raise UserWarning('+NmrDpReport.setError() No effects on NMR data processing report because the report is complete')

    def setWarning(self):

        if not self.__complete:
            self.__report['warning'] = self.warning.get()

            if not self.isError():
                self.__setStatus('WARNING')

        else:
            logging.warning('+NmrDpReport.setWarning() No effects on NMR data processing report because the report is complete')
            raise UserWarning('+NmrDpReport.setWarning() No effects on NMR data processing report because the report is complete')

    def get(self):

        if not self.__complete:
            self.__report['information']['input_sources'] = [input_source.get() for input_source in self.input_sources]
            self.__report['information']['sequence_alignments'] = self.sequence_alignment.get()

            self.__complete = True

            logging.info('+NmrDpReport.get() NMR data processing report is complete')

        return self.__report

    def getJson(self):
        return json.dumps(self.get(), indent=2)

class NmrDpReportInputSource:
    """ Wrapper class for data processing report of NMR unified data (input source).
    """

    def __init__(self):
        self.items = ('file_name', 'format_type', 'content_type', 'content_subtype',
                      'polymer_sequence', 'polymer_sequence_id',
                      'polymer_sequence_in_loop', 'polymer_sequence_id_in_loop',
                      'non_standard_residue',
                      'sequence_coverage_by_exptl_data',
                      'statistics_of_exptl_data')
        self.format_types = ('pdbx', 'nmr-nef', 'nmr-star')
        self.content_types = ('model', 'nmr-unified-data')
        self.content_subtypes = ('coordinate', 'poly_seq', 'chem_shift', 'dist_restraint', 'dihed_restraint', 'rdc_restraint', 'spectral_peak')

        self.__contents = {item:None for item in self.items}

    def setItemValue(self, item, value):

        if item in self.items:

            if item == 'format_type' and not value in self.format_types:
                logging.error('+NmrDpReportInputSource.setItemValue() Unknown format type %s' % value)
                raise ValueError('+NmrDpReportInputSource.setItemValue() Unknown format type %s' % value)

            elif item == 'content_type' and not value in self.content_types:
                logging.error('+NmrDpReportInputSource.setItemValue() Unknown content type %s' % value)
                raise ValueError('+NmrDpReportInputSource.setItemValue() Unknown content type %s' % value)

            elif item == 'content_subtype':

                for k in value:

                    if not k in self.content_subtypes:
                        logging.error('+NmrDpReportInputSource.setItemValue() Unknown content subtype in %s' % value.keys())
                        raise ValueError('+NmrDpReportInputSource.setItemValue() Unknown content subtype in %s' % value.keys())

                non_positive_keys = [k for k in value if int(value[k]) <= 0]

                for k in non_positive_keys:
                    value.pop(k)

                if (len(value) > 0):
                    self.__contents[item] = value

            else:
                self.__contents[item] = value

        else:
            logging.error('+NmrDpReportInputSource.setItemValue() Unknown item type %s' % item)
            raise KeyError('+NmrDpReportInputSource.setItemValue() Unknown item type %s' % item)

    def get(self):
        return self.__contents

class NmrDpReportSequenceAlignment:
    """ Wrapper class for data processing report of NMR unified data (sequence alignment).
    """

    def __init__(self):
        self.items = ('coordinate_vs_poly_seq', 'poly_seq_vs_chem_shift', 'poly_seq_vs_dist_restraint', 'poly_seq_vs_dihed_restraint', 'poly_seq_vs_rdc_restraint', 'poly_seq_vs_spectral_peak')

        self.__contents = {item:None for item in self.items}

    def setItemValue(self, item, value):

        if item in self.items:
            self.__contents[item] = value

        else:
            logging.error('+NmrDpReportSequenceAlignment.setItemValue() Unknown item type %s' % item)
            raise KeyError('+NmrDpReportSequenceAlignment.setItemValue() Unknown item type %s' % item)

    def get(self):
        return self.__contents

class NmrDpReportError:
    """ Wrapper class for data processing report of NMR unified data (error).
    """

    def __init__(self):
        self.items = ('format_issue', 'missing_mandatory_content', 'missing_mandatory_item', 'blanked_mandatory_value', 'sequence_mismatche',
                      'invalid_atom_nomenclature', 'invalid_atom_type', 'invalid_atom_isotope_number', 'invalid_ambiguity_code',
                      'duplicated_data', 'anomalous_data')

        self.__contents = {item:None for item in self.items}

    def setItemValue(self, item, value):

        if item in self.items:
            self.__contents[item] = value

        else:
            logging.error('+NmrDpReportError.setItemValue() Unknown item type %s' % item)
            raise KeyError('+NmrDpReportError.setItemValue() Unknown item type %s' % item)

    def get(self):
        return self.__contents

class NmrDpReportWarning:
    """ Wrapper class for data processing report of NMR unified data (warning).
    """

    def __init__(self):
        self.items = ('missing_content', 'missing_saveframe', 'missing_item', 'blanked_item', 'sequence_mismatche', 'suspicious_data')

        self.__contents = {item:None for item in self.items}

    def setItemValue(self, item, value):

        if item in self.items:
            self.__contents[item] = value

        else:
            logging.error('+NmrDpReportWarning.setItemValue() Unknown item type %s' % item)
            raise KeyError('+NmrDpReportWarning.setItemValue() Unknown item type %s' % item)

    def get(self):
        return self.__contents
