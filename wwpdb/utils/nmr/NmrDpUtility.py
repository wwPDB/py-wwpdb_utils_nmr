##
# File: NmrDpUtility.py
# Date: 13-May-2019
#
# Updates:
##
""" Wrapper class for data processing for NMR unified data.
"""
import sys
import os
import os.path
import pynmrstar
import logging
import json

from wwpdb.utils.nmr.NEFTranslator.NEFTranslator import NEFTranslator
from wwpdb.utils.nmr.NmrDpReport import NmrDpReport

class NmrDpUtility(object):
    """ Wrapper class for data processing for NMR unified data.
    """

    def __init__(self, verbose=False, log=sys.stderr):
        self.__verbose = verbose
        self.__lfh = log

        # current workflow operation
        self.__op = None

        # source, destination, and log file paths.
        self.__srcPath = None
        self.__dstPath = None
        self.__logPath = None

        # auxiliary input resource.
        self.__inputParamDict = {}

        # auxiliary output resource.
        self.__outputParamDict = {}

        # list of known workflow operations
        self.__workFlowOps = ('nmr-nef-parser-check','nmr-star-parser-check',
                              'nmr-nef-consistency-check','nmr-star-consistency-check',
                              'nmr-nef2star-deposit','nmr-star2star-deposit')

        # dictionary of processing tasks of each workflow operation
        self.__procTasksDict = {'nmr-parser-check':  [self.__initializeDpReport,
                                                      self.__instanceNEFTranslator,
                                                      self.__validateInputSource,
                                                      self.__detectContentSubType,
                                                      self.__extractPolymerSequence,
                                                      self.__extractPolymerSequenceInLoops] }
        """
                                                      self.__testSequenceConsistency]
                                }
                                                      self.__extractNonStandardResidue,
                                                      self._AlignPolymerSequence,
                                                      self.__testAtomNomenclature,
                                                      self.__testAtomType,
                                                      self.__testAtomIsotopeNumber,
                                                      self.__testAmbiguityCode,
                                                      self.__testDuplicationData,
                                                      self.__testAnomalousData,
                                                      self.__testSaspiciousData,
                                                      self__calculateStatistics],
                                'nmr-consistency-check': [self.__appendInputResource,
                                                          self.__extractCoordPolymerSequence,
                                                          self.__AlignCoordPolymerSequence,
                                                          self.__testCoordSequenceConsistency,
                                                          self.__testCoordAtomNomeclature],
                                'nmr-nef2star-deposit':  [self.__resolveNefMinorIssue,
                                                          self.__depositNef2Star],
                                'nmr-star2star-deposit': [self.__resolveStarMinorIssue,
                                                          self.__depositStar2Star]
                                }
        """
        # data processing report
        self.report = None

        # NEFTranslator
        self.nef_translator = None

        # PyNMRSTAR data
        self.__star_data_type = None
        self.__star_data = None

        # NMR content types
        self.nmr_content_subtypes = ('poly_seq', 'chem_shift', 'dist_restraint', 'dihed_restraint', 'rdc_restraint', 'spectral_peak')

        # readable file format name
        self.readable_format_name = {'nmr-nef': 'NEF (NMR Exchange Format)', 'nmr-star': 'NMR-STAR V3.2',
                                     'pdbx': 'PDBx/mmCIF', 'unknown': 'unknown'}

        # saveframe categories
        self.sf_categories = {'nmr-nef': {'poly_seq': 'nef_molecular_system',
                                          'chem_shift': 'nef_chemical_shift_list',
                                          'dist_restraint': 'nef_distance_restraint_list',
                                          'dihed_restraint': 'nef_dihedral_restraint_list',
                                          'rdc_restraint': 'nef_rdc_restraint_list',
                                          'spectral_peak': 'nef_nmr_spectrum'},
                              'nmr-star': {'poly_seq': 'assembly',
                                           'chem_shift': 'assigned_chemical_shifts',
                                           'dist_restraint': 'general_distance_constraints',
                                           'dihed_restraint': 'torsion_angle_constraints',
                                           'rdc_restraint': 'RDC_constraints',
                                           'spectral_peak': 'spectral_peak_list'}
                              }

        # loop categories
        self.lp_categories = {'nmr-nef': {'poly_seq': '_nef_sequence',
                                          'chem_shift': '_nef_chemical_shift',
                                          'dist_restraint': '_nef_distance_restraint',
                                          'dihed_restraint': '_nef_dihedral_restraint',
                                          'rdc_restraint': '_nef_rdc_restraint',
                                          'spectral_peak': '_nef_peak'},
                              'nmr-star': {'poly_seq': '_Chem_comp_assembly',
                                           'chem_shift': '_Atom_chem_shift',
                                           'dist_restraint': '_Gen_dist_constraint',
                                           'dihed_restraint': '_Torsion_angle_constraint',
                                           'rdc_restraint': '_RDC_constraint',
                                           'spectral_peak': '_Peak_row_format'}
                              }

    def setSource(self, fPath):
        """ Set primary source file path.
        """

        if os.access(fPath, os.F_OK):
            self.__srcPath = os.path.abspath(fPath)
        else:
            self.__srcPath = None

    def setDestination(self, fPath):
        """ Set primary destination file path.
        """

        self.__dstPath = os.path.abspath(fPath)

    def setLog(self, fPath):
        """ Set a log file path.
        """

        self.__logPath = os.path.abspath(fPath)

    def addInput(self, name=None, value=None, type='file'):
        """ Add a named input and value to the dictionary of input parameters.
        """

        try:
            if type == 'param':
                self.__inputParamDict[name] = value
            elif type == 'file':
                self.__inputParamDict[name] = os.path.abspath(value)
            else:
                logging.error("+NmrDpUtility.addInput() ++ Error  - Unknown input type '%s'" % type)
                raise KeyError("+NmrDpUtility.addInput() ++ Error - Unknown input type '%s'" % type)

                return False

            return True

        except Exception as e:
            logging.error("+NmrDpUtility.addInput() ++ Error  - %s" % str(e))
            raise ValueError("+NmrDpUtility.addInput() ++ Error - %s" % str(e))

            return False

    def addOutput(self, name=None, value=None, type='file'):
        """ Add a named input and value to the dictionary of output parameters.
        """

        try:
            if type == 'param':
                self.__outputParamDict[name] = value
            elif type == 'file':
                self.__outputParamDict[name] = os.path.abspath(value)
            else:
                logging.error("+NmrDpUtility.addOutput() ++ Error  - Unknown output type '%s'" % type)
                raise KeyError("+NmrDpUtility.addOutput() ++ Error - Unknown output type '%s'" % type)

                return False

            return True

        except:
            logging.error("+NmrDpUtility.addOutput() ++ Error  - %s" % str(e))
            raise ValueError("+NmrDpUtility.addOutput() ++ Error - %s" % str(e))

            return False

    def op(self, op):
        """ Perform a series of tasks for a given workflow operation.
        """

        if self.__srcPath is None:
            logging.error("+NmrDpUtility.op() ++ Error  - No input provided for workflow operation '%s'" % op)
            raise ValueError("+NmrDpUtility.op() ++ Error - No input provided for workflow operation '%s'" % op)

        if self.__verbose:
            self.__lfh.write("+NmrDpUtility.op() starting op %s\n" % op)

        if not op in self.__workFlowOps:
            logging.error("+NmrDpUtility.op() ++ Error  - Unknown workflow operation '%s'" % op)
            raise KeyError("+NmrDpUtility.op() ++ Error  - Unknown workflow operation '%s'" % op)

        self.__op = op

        # run workflow operation specific tasks
        if op in self.__procTasksDict:

            for task in self.__procTasksDict[op]:

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.op() starting op '%s' - task '%s'\n" % (op, task.__name__))

                if not task():
                    self.report.writeJson(self.__logPath)

                    return False

        # run general processing tasks
        if 'parser-check' in op:

            for task in self.__procTasksDict['nmr-parser-check']:

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.op() starting op '%s' - task '%s'\n" % (op, task.__name__))

                if not task():
                    self.report.writeJson(self.__logPath)

                    return False

        elif 'consistency-check' in op:

            for task in self.__procTasksDict['nmr-consistency-check']:

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.op() starting op '%s' - task '%s'\n" % (op, task.__name__))

                if not task():
                    self.report.writeJson(self.__logPath)

                    return False

        self.report.writeJson(self.__logPath)

        return True

    def __initializeDpReport(self):
        """ Initialize NMR data processing report.
        """

        self.report = NmrDpReport()

        # set primary input source as NMR unified data
        input_source = self.report.input_sources[0]

        input_source.setItemValue('file_name', os.path.basename(self.__srcPath))
        input_source.setItemValue('file_format', 'nmr-nef' if 'nef' in self.__op else 'nmr-star')
        input_source.setItemValue('content_type','nmr-unified-data')

        return input_source is not None

    def __instanceNEFTranslator(self):
        """ Instance NEFTanslator.
        """

        self.nef_translator = NEFTranslator()

        return self.nef_translator is not None

    def __validateInputSource(self):
        """ Validate input source using NEFTranslator.
        """

        is_valid, json_dumps = self.nef_translator.validate_file(self.__srcPath, 'A') # 'A' for NMR unified data, 'S' for assigned chemical shifts, 'R' for restraints.

        message = json.loads(json_dumps)

        _file_format = message['FILE'].lower() # nef/nmr-star/unknown

        if _file_format == 'nef':
            _file_format = 'nmr-nef'

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_format = input_source_dic['file_format']

        if is_valid:

            if _file_format != file_format:

                self.report.error.addDescription('format_isssue', "'%s' was selected as %s file, but recognized as an %s file." % (file_name, self.readable_format_name[file_format], self.readable_format_name[_file_format]))

                if len(message['error']) > 0:
                    for error_message in message['error']:
                        self.report.error.addDescription('format_issue', "Diagnostic information: %s" % error_message)

                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__validateInputSource() ++ Error  - '%s' was selected as %s file, but recognized as an %s file.\n" % (file_name, self.readable_format_name[file_format], self.readable_format_name[_file_format]))

                return False

            return True

        else:

            self.report.error.addDescription('format_isssue', "'%s' is invalid %s file." % (file_name, self.readable_format_name[file_format]))

            if len(message['error']) > 0:
                for error_message in message['error']:
                    self.report.error.addDescription('format_issue', "Diagnostic information: %s" % error_message)

            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__validateInputSource() ++ Error  - '%s' is invalid %s file." % (file_name, self.readable_format_name[file_format]))

            return False

    def __detectContentSubType(self):
        """ Detect content subtypes in NEF/NMR-STAR V3.2 file.
        """

        if self.report.isError():
            return False

        is_done, self.__star_data_type, self.__star_data = self.nef_translator.read_input_file(self.__srcPath) # NEFTranslator.validate_file() generates this object internally, but not re-used.

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_format = input_source_dic['file_format']

        lp_category_list = self.nef_translator.get_data_content(self.__star_data, self.__star_data_type)[1]

        # initialize loop counter
        lp_counts = {t:0 for t in self.nmr_content_subtypes}

        # increment loop counter of each content subtype
        for lp_category in lp_category_list:
            if lp_category in self.lp_categories[file_format].values():
                lp_counts[[k for k, v in self.lp_categories[file_format].items() if v == lp_category][0]] += 1

        content_subtypes = {k:lp_counts[k] for k in lp_counts if lp_counts[k] > 0}

        input_source.setItemValue('content_subtype', content_subtypes)

        content_subtype = 'poly_seq'

        if lp_counts[content_subtype] == 0:

            sf_category = self.sf_categories[file_format][content_subtype]

            self.report.warning.addDescription('missing_saveframe', "Saveframe category '%s' were not found in %s file." % (sf_category, file_name))
            self.report.setWarning(warning)

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__detectContentSubType() ++ Warning  - Saveframe category '%s' were not found in %s file.\n" % (sf_category, file_name))

        elif lp_counts[content_subtype] > 1:

            sf_category = self.sf_categories[file_format][content_subtype]

            self.report.error.addDescription('format_issue', "Unexpectedly, multiple saveframes belonging to category '%s' were found in %s file." % (sf_category, file_name))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__detectContentSubType() ++ Error  - Unexpectedly, multiple saveframes belonging to category '%s' were found in %s file.\n" % (sf_category, file_name))

        content_subtype = 'chem_shift'

        if lp_counts[content_subtype] == 0:

            sf_category = self.sf_categories[file_format][content_subtype]
            lp_category = self.lp_categories[file_format][content_subtype]

            self.report.error.addDescription('missing_mandatory_content', "Assigned chemical shifts are mandatory for PDB/BMRB deposition. Saveframe category '%s' and loop category '%s' were not found in %s file." % (sf_category, lp_category, file_name))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__detectContentSubType() ++ Error  - Assigned chemical shifts are mandatory for PDB/BMRB deposition. Saveframe category '%s' and loop category '%s' were not found in %s file." % (sf_category, lp_category, file_name))

        content_subtype = 'dist_restraint'

        if lp_counts[content_subtype] == 0:

            sf_category = self.sf_categories[file_format][content_subtype]
            lp_category = self.lp_categories[file_format][content_subtype]

            self.report.error.addDescription('missing_mandatory_content', "Distance restraints are mandatory for PDB/BMRB deposition. Saveframe category '%s' and loop category '%s' were not found in %s file." % (sf_category, lp_category, file_name))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__detectContentSubType() ++ Error  - Distance restraints are mandatory for PDB/BMRB deposition. Saveframe category '%s' and loop category '%s' were not found in %s file." % (sf_category, lp_category, file_name))

        content_subtype = 'spectral_peak'

        if lp_counts[content_subtype] == 0:

            sf_category = self.sf_categories[file_format][content_subtype]
            lp_category = self.lp_categories[file_format][content_subtype]

            self.report.warning.addDescription('missing_content', "Spectral peak list is missing. The wwPDB NMR Validation Task Force strongly encourages the submission of spectral peak lists, in particular those generated from NOESY spectra. Saveframe category '%s' and loop category '%s' were not found in %s file." % (sf_category, lp_category, file_name))
            self.report.setWarning()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__detectContentSubType() ++ Warning  - Spectral peak list is missing. The wwPDB NMR Validation Task Force strongly encourages the submission of spectral peak lists, in particular those generated from NOESY spectra. Saveframe category '%s' and loop category '%s' were not found in %s file." % (sf_category, lp_category, file_name))

        return self.report.isOk()

    def __getPolymerSequence(self, sf_data, content_subtype):
        """ Wrapper function to retrieve polymer sequence from loop of a specified saveframe and content subtype via NEFTranslator.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_format = input_source_dic['file_format']

        if file_format == 'nmr-nef':
            return self.nef_translator.get_nef_seq(sf_data, lp_category=self.lp_categories[file_format][content_subtype], allow_empty=(content_subtype == 'spectral_peak'))
        else:
            return self.nef_translator.get_star_seq(sf_data, lp_category=self.lp_categories[file_format][content_subtype], allow_empty=(content_subtype == 'spectral_peak'))

    def __extractPolymerSequence(self):
        """ Extract reference polymer sequence of NEF/NMR-STAR V3.2 file.
        """

        if self.report.isError():
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_format = input_source_dic['file_format']

        content_subtype = 'poly_seq'

        if not content_subtype in input_source_dic['content_subtype']:
            return False

        sf_category = self.sf_categories[file_format][content_subtype]

        sf_data = self.__star_data.get_saveframes_by_category(sf_category)[0]

        try:

            poly_seq, poly_sid = self.__getPolymerSequence(sf_data, content_subtype)

            input_source.setItemValue('polymer_sequence', poly_seq)
            input_source.setItemValue('polymer_sequence_id', poly_sid)

            return True

        except Exception as e:

            self.report.error.addDescription('format_issue', str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__extractPolymerSequence() ++ Error  - %s" % str(e))

            return False

    def __extractPolymerSequenceInLoops(self):
        """ Extract polymer sequence in interesting loops of NEF/NMR-STAR V3.2 file.
        """

        if self.report.isError():
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_format = input_source_dic['file_format']

        poly_seq_list_set = {}
        poly_sid_list_set = {}

        for content_subtype in self.nmr_content_subtypes:

            if content_subtype == 'poly_seq' or not content_subtype in input_source_dic['content_subtype']:
                continue

            poly_seq_list_set[content_subtype] = []
            poly_sid_list_set[content_subtype] = []

            sf_category = self.sf_categories[file_format][content_subtype]

            list_id = 1
            has_poly_seq = False

            for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

                sf_framecode = sf_data.get_tag('sf_framecode')[0]

                try:

                    poly_seq, poly_sid = self.__getPolymerSequence(sf_data, content_subtype)

                    if len(poly_seq) > 0:
                        poly_seq_list_set[content_subtype].append({'list_id': list_id, 'sf_framecode': sf_framecode, 'polymer_sequence': poly_seq})
                        poly_sid_list_set[content_subtype].append({'list_id': list_id, 'sf_framecode': sf_framecode, 'polymer_sequence': poly_sid})

                        has_poly_seq = True

                    list_id += 1

                except Exception as e:

                    self.report.error.addDescription('format_issue', str(e))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__extractPolymerSequenceInLoops() ++ Error  - %s" % str(e))

                    return False

            if not has_poly_seq:
                poly_seq_list_set.pop(content_subtype)
                poly_sid_list_set.pop(content_subtype)

        input_source.setItemValue('polymer_sequence_in_loop', poly_seq_list_set)
        input_source.setItemValue('polymer_sequence_id_in_loop', poly_sid_list_set)

        return True

    def __testSequenceConsistency(self):
        """ Apply sequence consistency test among extracted polymer sequences.
        """

        if self.report.isError():
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        return True

if __name__ == '__main__':
    dp = NmrDpUtility()
