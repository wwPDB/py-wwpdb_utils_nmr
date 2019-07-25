##
# File: NmrDpUtility.py
# Date: 25-Jul-2019
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
import itertools
import copy
import collections
import re
import math

from munkres import Munkres

from wwpdb.utils.nmr.NEFTranslator.NEFTranslator import NEFTranslator
from wwpdb.utils.nmr.NmrDpReport import NmrDpReport
from wwpdb.utils.align.alignlib import PairwiseAlign
from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
from wwpdb.utils.config.ConfigInfo import ConfigInfo, getSiteId
from wwpdb.utils.nmr.io.ChemCompIo import ChemCompReader
from wwpdb.utils.nmr.CifReader import CifReader

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

        self.__cifPath = None

        # auxiliary input resource.
        self.__inputParamDict = {}

        # auxiliary output resource.
        self.__outputParamDict = {}

        # list of known workflow operations
        self.__workFlowOps = ('nmr-nef-consistency-check', 'nmr-str-consistency-check',
                              'nmr-nef2str-deposit', 'nmr-str2str-deposit')

        # validation tasks for NMR data only
        __nmrCheckTasks = [self.__detectContentSubType,
                           self.__extractPolymerSequence,
                           self.__extractPolymerSequenceInLoop,
                           self.__testSequenceConsistency,
                           self.__extractCommonPolymerSequence,
                           self.__extractNonStandardResidue,
                           self.__appendPolymerSequenceAlignment,
                           self.__validateAtomNomenclature,
                           self.__validateAtomTypeOfCSLoop,
                           self.__validateAmbigCodeOfCSLoop,
                           self.__testIndexConsistency,
                           self.__testDataConsistencyInLoop,
                           self.__testDataConsistencyInAuxLoop,
                           self.__testSfTagConsistency,
                           self.__validateCSValue,
                           self.__testCSValueConsistencyInPkLoop,
                           self.__testRDCVector
                           ]

        # validation tasks for coordinate file only
        __cifCheckTasks = [self.__validateCoordInputSource,
                           self.__detectCoordContentSubType,
                           self.__extractCoordPolymerSequence,
                           self.__extractCoordNonPolymerScheme,
                           self.__extractCoordPolymerSequenceInLoop,
                           self.__extractCoordNonStandardResidue,
                           self.__appendCoordPolymerSequenceAlignment
                           ]

        # cross validation tasks
        __crossCheckTasks = [self.__assignCoordPolymerSequence,
                             self.__testCoordAtomIdConsistency,
                             self.__extractCoordDisulfideBond,
                             self.__extractCoordOtherBond,
                             self.__calculateStatsOfExptlData
                             ]

        # nmr-*-consistency-check tasks
        __checkTasks = [self.__initializeDpReport, self.__validateInputSource]
        __checkTasks.extend(__nmrCheckTasks)
        __checkTasks.extend(__cifCheckTasks)
        __checkTasks.extend(__crossCheckTasks)

        # nmr-*-deposit tasks
        __depositTasks = [self.__retrieveDpReport, self.__validateInputSource, self.__parseCoordinate,
                          # resolve minor issues
                          self.__deleteSkippedSf,
                          self.__deleteSkippedLoop,
                          self.__updatePolymerSequence,
                          self.__updateDihedralAngleType,
                          self.__fixDisorderedIndex,
                          self.__removeNonSenseZeroValue,
                          self.__fixNonSenseNegativeValue,
                          self.__fixEnumerationValue,
                          #self.__fixBadAmbiguityCode,
                          self.__resetCapitalStringInLoop,
                          self.__resetBoolValueInLoop,
                          self.__resetBoolValueInAuxLoop,
                          self.__appendParentSfTag,
                          self.__addUnnamedEntryId,
                          self.__depositNmrData,
                          # re-setup for next
                          self.__initializeDpReportForNext, self.__validateInputSourceForNext]

        __depositTasks.extend(__nmrCheckTasks)
        __depositTasks.extend(__cifCheckTasks)
        __depositTasks.extend(__crossCheckTasks)

        # additional nmr-nef2str tasks
        __nef2strTasks = [self.__translateNef2Str, self.__dumpDpReport, self.__initResourceForNef2Str]

        __nef2strTasks.extend(__checkTasks)
        __nef2strTasks.append(self.__dumpDpReport)
        __nef2strTasks.extend(__depositTasks)

        # dictionary of processing tasks of each workflow operation
        self.__procTasksDict = {'consistency-check': __checkTasks,
                                'deposit': __depositTasks,
                                'nmr-nef2str-deposit': __nef2strTasks
                                }

        # data processing report
        self.report = None
        self.report_prev = None

        # NEFTranslator
        self.__nefT = NEFTranslator()

        if self.__nefT is None:

            logging.error("+NmrDpUtility.__init__() ++ Error  - NEFTranslator is not available.")
            raise IOError("+NmrDpUtility.__init__() ++ Error  - NEFTranslator is not available.")

        # BMRB chemical shift statistics
        self.__csStat = BMRBChemShiftStat()

        if not self.__csStat.isOk():

            logging.error("+NmrDpUtility.__init__() ++ Error  - BMRBChemShiftStat is not available.")
            raise IOError("+NmrDpUtility.__init__() ++ Error  - BMRBChemShiftStat is not available.")

        # PyNMRSTAR data
        self.__star_data = None
        self.__star_data_type = None
        self.__sf_category_list = []
        self.__lp_category_list = []

        # empty value
        self.empty_value = (None, '', '.', '?')

        # true value
        self.true_value = ('true', 't', 'yes', 'y', '1')

        # NMR content types
        self.nmr_content_subtypes = ('entry_info', 'poly_seq', 'chem_shift', 'dist_restraint', 'dihed_restraint', 'rdc_restraint', 'spectral_peak')

        # CIF content types
        self.cif_content_subtypes = ('poly_seq', 'non_poly', 'coordinate')

        # readable file type
        self.readable_file_type = {'nef': 'NEF (NMR Exchange Format)',
                                   'nmr-star': 'NMR-STAR V3.2',
                                   'pdbx': 'PDBx/mmCIF',
                                   'unknown': 'unknown'
                                   }

        # content type
        self.content_type = {'nef': 'nmr-unified-data-nef',
                             'nmr-star': 'nmr-unified-data-str',
                             'pdbx': 'model'
                             }

        # paramagnetic elements, except for Oxygen
        self.paramag_elems = ('LI', 'NA', 'MG', 'AL', 'K', 'CA', 'SC', 'TI', 'V', 'MN', 'RB', 'SR', 'Y', 'ZR', 'NB', 'MO', 'TC', 'RU', 'RH', 'PD', 'SN', 'CS', 'BA', 'LA', 'CE', 'PR', 'ND', 'PM', 'SM', 'EU', 'GD', 'TB', 'DY', 'HO', 'ER', 'TM', 'YB', 'LU', 'HF', 'TA', 'W', 'RE', 'OS', 'IR', 'PT', 'FR', 'RA', 'AC')

        # ferromagnetic elements
        self.ferromag_elems = ('CR', 'FE', 'CO', 'NI')

        # non-metal elements
        self.non_metal_elems = ('H', 'C', 'N', 'O', 'P', 'S', 'SE')

        # isotope numbers of NMR observable atoms
        self.atom_isotopes = {'H': [1, 2, 3],
                              'C': [13],
                              'N': [15, 14],
                              'O': [17],
                              'P': [31],
                              'S': [33],
                              'F': [19],
                              'CD': [113, 111],
                              'CA': [43]
                              }

        # ambiguity codes
        self.bmrb_ambiguity_codes = (1, 2, 3, 4, 5, 6, 9)

        isotope_nums = []
        for i in self.atom_isotopes.values():
            isotope_nums.extend(list(i))

        # saveframe categories
        self.sf_categories = {'nef': {'entry_info': 'nef_nmr_meta_data',
                                      'poly_seq': 'nef_molecular_system',
                                      'chem_shift': 'nef_chemical_shift_list',
                                      'dist_restraint': 'nef_distance_restraint_list',
                                      'dihed_restraint': 'nef_dihedral_restraint_list',
                                      'rdc_restraint': 'nef_rdc_restraint_list',
                                      'spectral_peak': 'nef_nmr_spectrum'
                                      },
                              'nmr-star': {'entry_info': 'entry_information',
                                           'poly_seq': 'assembly',
                                           'chem_shift': 'assigned_chemical_shifts',
                                           'dist_restraint': 'general_distance_constraints',
                                           'dihed_restraint': 'torsion_angle_constraints',
                                           'rdc_restraint': 'RDC_constraints',
                                           'spectral_peak': 'spectral_peak_list'
                                           }
                              }

        # loop categories
        self.lp_categories = {'nef': {'entry_info': '_nef_program_script',
                                      'poly_seq': '_nef_sequence',
                                      'chem_shift': '_nef_chemical_shift',
                                      'dist_restraint': '_nef_distance_restraint',
                                      'dihed_restraint': '_nef_dihedral_restraint',
                                      'rdc_restraint': '_nef_rdc_restraint',
                                      'spectral_peak': '_nef_peak'
                                      },
                              'nmr-star': {'entry_info': '_Software_applied_methods',
                                           'poly_seq': '_Chem_comp_assembly',
                                           'chem_shift': '_Atom_chem_shift',
                                           'dist_restraint': '_Gen_dist_constraint',
                                           'dihed_restraint': '_Torsion_angle_constraint',
                                           'rdc_restraint': '_RDC_constraint',
                                           'spectral_peak': '_Peak_row_format'
                                           },
                              'pdbx': {'poly_seq': 'pdbx_poly_seq_scheme',
                                       'non_poly': 'pdbx_nonpoly_scheme',
                                       'coordinate': 'atom_site'
                                       }
                              }

        # allowed chem shift range
        self.chem_shift_range = {'min_exclusive': -300.0, 'max_exclusive': 300.0}
        self.chem_shift_error = {'min_exclusive': 0.0, 'max_exclusive': 3.0}

        # allowed distance range
        self.dist_restraint_range = {'min_exclusive': 1.0, 'max_exclusive': 50.0}
        self.dist_restraint_error = {'min_exclusive': 0.0, 'max_exclusive': 5.0}

        # allowed dihed range
        self.dihed_restraint_range = {'min_exclusive': -360.0, 'max_exclusive': 360.0}
        self.dihed_restraint_error = {'min_exclusive': 0.0, 'max_exclusive': 20.0}

        # allowed rdc range
        self.rdc_restraint_range = {'min_exclusive': -50.0, 'max_exclusive': 50.0}
        self.rdc_restraint_error = {'min_exclusive': 0.0, 'max_exclusive': 5.0}

        # allowed weight range
        self.weight_range = {'min_exclusive': 0.0, 'max_inclusive': 10.0}
        # allowed scale range
        self.scale_range = self.weight_range

        # criterion for detection of low sequence coverage
        self.low_sequence_coverage = 0.3

        # loop index tags
        self.index_tags = {'nef': {'entry_info': None,
                                   'poly_seq': 'index',
                                   'chem_shift': None,
                                   'dist_restraint': 'index',
                                   'dihed_restraint': 'index',
                                   'rdc_restraint': 'index',
                                   'spectral_peak': 'index'
                                   },
                           'nmr-star': {'entry_info': None,
                                        'poly_seq': None,
                                        'chem_shift': None,
                                        'dist_restraint': 'Index_ID',
                                        'dihed_restraint': 'Index_ID',
                                        'rdc_restraint': 'Index_ID',
                                        'spectral_peak': 'Index_ID'
                                        },
                           'pdbx': {'poly_seq': None,
                                    'non_poly': None,
                                    'coordinate': 'id'
                                    }
                           }

        # loop key items
        self.key_items = {'nef': {'poly_seq': [{'name': 'chain_code', 'type': 'str'},
                                               {'name': 'sequence_code', 'type': 'int'},
                                               {'name': 'residue_name', 'type': 'str'}
                                               ],
                                   'chem_shift': [{'name': 'chain_code', 'type': 'str'},
                                                  {'name': 'sequence_code', 'type': 'int'},
                                                  {'name': 'residue_name', 'type': 'str'},
                                                  {'name': 'atom_name', 'type': 'str'}
                                                  ],
                                   'dist_restraint': [{'name': 'chain_code_1', 'type': 'str'},
                                                      {'name': 'sequence_code_1', 'type': 'int'},
                                                      {'name': 'residue_name_1', 'type': 'str'},
                                                      {'name': 'atom_name_1', 'type': 'str'},
                                                      {'name': 'chain_code_2', 'type': 'str'},
                                                      {'name': 'sequence_code_2', 'type': 'int'},
                                                      {'name': 'residue_name_2', 'type': 'str'},
                                                      {'name': 'atom_name_2', 'type': 'str'}
                                                      ],
                                   'dihed_restraint': [{'name': 'chain_code_1', 'type': 'str'},
                                                       {'name': 'sequence_code_1', 'type': 'int'},
                                                       {'name': 'residue_name_1', 'type': 'str'},
                                                       {'name': 'atom_name_1', 'type': 'str'},
                                                       {'name': 'chain_code_2', 'type': 'str'},
                                                       {'name': 'sequence_code_2', 'type': 'int'},
                                                       {'name': 'residue_name_2', 'type': 'str'},
                                                       {'name': 'atom_name_2', 'type': 'str'},
                                                       {'name': 'chain_code_3', 'type': 'str'},
                                                       {'name': 'sequence_code_3', 'type': 'int'},
                                                       {'name': 'residue_name_3', 'type': 'str'},
                                                       {'name': 'atom_name_3', 'type': 'str'},
                                                       {'name': 'chain_code_4', 'type': 'str'},
                                                       {'name': 'sequence_code_4', 'type': 'int'},
                                                       {'name': 'residue_name_4', 'type': 'str'},
                                                       {'name': 'atom_name_4', 'type': 'str'}
                                                       ],
                                   'rdc_restraint': [{'name': 'chain_code_1', 'type': 'str'},
                                                     {'name': 'sequence_code_1', 'type': 'int'},
                                                     {'name': 'residue_name_1', 'type': 'str'},
                                                     {'name': 'atom_name_1', 'type': 'str'},
                                                     {'name': 'chain_code_2', 'type': 'str'},
                                                     {'name': 'sequence_code_2', 'type': 'int'},
                                                     {'name': 'residue_name_2', 'type': 'str'},
                                                     {'name': 'atom_name_2', 'type': 'str'}
                                                     ],
                                   'spectral_peak': None
                                   },
                          'nmr-star': {'poly_seq': [{'name': 'Entity_assembly_ID', 'type': 'positive-int'},
                                                    {'name': 'Comp_index_ID', 'type': 'int'},
                                                    {'name': 'Comp_ID', 'type': 'str'}
                                                    ],
                                       'chem_shift': [{'name': 'Entity_assembly_ID', 'type': 'positive-int'},
                                                      {'name': 'Comp_index_ID', 'type': 'int'},
                                                      {'name': 'Comp_ID', 'type': 'str'},
                                                      {'name': 'Atom_ID', 'type': 'str'}
                                                      ],
                                       'dist_restraint': [{'name': 'Entity_assembly_ID_1', 'type': 'positive-int'},
                                                          {'name': 'Comp_index_ID_1', 'type': 'int'},
                                                          {'name': 'Comp_ID_1', 'type': 'str'},
                                                          {'name': 'Atom_ID_1', 'type': 'str'},
                                                          {'name': 'Entity_assembly_ID_2', 'type': 'positive-int'},
                                                          {'name': 'Comp_index_ID_2', 'type': 'int'},
                                                          {'name': 'Comp_ID_2', 'type': 'str'},
                                                          {'name': 'Atom_ID_2', 'type': 'str'}
                                                          ],
                                       'dihed_restraint': [{'name': 'Entity_assembly_ID_1', 'type': 'positive-int'},
                                                           {'name': 'Comp_index_ID_1', 'type': 'int'},
                                                           {'name': 'Comp_ID_1', 'type': 'str'},
                                                           {'name': 'Atom_ID_1', 'type': 'str'},
                                                           {'name': 'Entity_assembly_ID_2', 'type': 'positive-int'},
                                                           {'name': 'Comp_index_ID_2', 'type': 'int'},
                                                           {'name': 'Comp_ID_2', 'type': 'str'},
                                                           {'name': 'Atom_ID_2', 'type': 'str'},
                                                           {'name': 'Entity_assembly_ID_3', 'type': 'positive-int'},
                                                           {'name': 'Comp_index_ID_3', 'type': 'int'},
                                                           {'name': 'Comp_ID_3', 'type': 'str'},
                                                           {'name': 'Atom_ID_3', 'type': 'str'},
                                                           {'name': 'Entity_assembly_ID_4', 'type': 'positive-int'},
                                                           {'name': 'Comp_index_ID_4', 'type': 'int'},
                                                           {'name': 'Comp_ID_4', 'type': 'str'},
                                                           {'name': 'Atom_ID_4', 'type': 'str'}
                                                           ],
                                       'rdc_restraint': [{'name': 'Entity_assembly_ID_1', 'type': 'positive-int'},
                                                         {'name': 'Comp_index_ID_1', 'type': 'int'},
                                                         {'name': 'Comp_ID_1', 'type': 'str'},
                                                         {'name': 'Atom_ID_1', 'type': 'str'},
                                                         {'name': 'Entity_assembly_ID_2', 'type': 'positive-int'},
                                                         {'name': 'Comp_index_ID_2', 'type': 'int'},
                                                         {'name': 'Comp_ID_2', 'type': 'str'},
                                                         {'name': 'Atom_ID_2', 'type': 'str'}
                                                         ],
                                       'spectral_peak': None
                                       },
                          'pdbx': {'poly_seq': [{'name': 'asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                                {'name': 'seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                                {'name': 'mon_id', 'type': 'str', 'alt_name': 'comp_id'}
                                                ],
                                   'non_poly': [{'name': 'asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                                {'name': 'pdb_seq_num', 'type': 'int', 'alt_name': 'seq_id'},
                                                {'name': 'mon_id', 'type': 'str', 'alt_name': 'comp_id'}
                                                ],
                                   'coordinate': [{'name': 'label_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                                  {'name': 'label_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                                  {'name': 'label_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                  {'name': 'pdbx_PDB_model_num', 'type': 'int', 'alt_name': 'model_id'}
                                                  ]
                                   }
                          }

        # limit number of dimensions
        self.lim_num_dim = 16

        # key items for spectral peak
        self.pk_key_items = {'nef': [{'name': 'position_%s', 'type': 'float'}
                                     ],
                             'nmr-star': [{'name': 'Position_%s', 'type': 'float'}
                                          ]
                             }

        # loop data items
        self.data_items = {'nef': {'poly_seq': [{'name': 'linking', 'type': 'enum', 'mandatory': False,
                                                 'enum': ('start', 'end', 'middle', 'cyclic', 'break', 'single', 'dummy'),
                                                 'enforce-enum': True},
                                                {'name': 'residue_variant', 'type': 'str', 'mandatory': False},
                                                {'name': 'cis_peptide', 'type': 'bool', 'mandatory': False}
                                                ],
                                   'chem_shift': [{'name': 'value', 'type': 'range-float', 'mandatory': True,
                                                   'range': self.chem_shift_range},
                                                  {'name': 'value_uncertainty', 'type': 'range-float', 'mandatory': False,
                                                   'range': self.chem_shift_error},
                                                  {'name': 'element', 'type': 'enum', 'mandatory': True,
                                                   'enum': set(self.atom_isotopes.keys()),
                                                   'enforce-enum': True},
                                                  {'name': 'isotope_number', 'type': 'enum-int', 'mandatory': True,
                                                   'enum': set(isotope_nums),
                                                   'enforce-enum': True}
                                                  ],
                                   'dist_restraint': [{'name': 'index', 'type': 'index-int', 'mandatory': True},
                                                      {'name': 'restraint_id', 'type': 'positive-int', 'mandatory': True,
                                                       'enforce-non-zero': True},
                                                      {'name': 'restraint_combination_id', 'type': 'positive-int', 'mandatory': False,
                                                       'enforce-non-zero': True},
                                                      {'name': 'weight', 'type': 'range-float', 'mandatory': True,
                                                       'range': self.weight_range,
                                                       'enforce-non-zero': True},
                                                      {'name': 'target_value', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                       'range': self.dist_restraint_range,
                                                       'group': {'member-with': ['lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit'],
                                                                 'coexist-with': None,
                                                                 'smaller-than': ['lower_limit', 'lower_linear_limit'],
                                                                 'larger-than': ['upper_limit', 'upper_linear_limit']}},
                                                      {'name': 'target_value_uncertainty', 'type': 'range-float', 'mandatory': False,
                                                       'range': self.dist_restraint_error},
                                                      {'name': 'lower_linear_limit', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                       'range': self.dist_restraint_range,
                                                       'group': {'member-with': ['target_value', 'lower_limit', 'upper_limit', 'upper_linear_limit'],
                                                                 'coexist-with': None, # ['lower_limit', 'upper_limit', 'upper_linear_limit'],
                                                                 'smaller-than': ['lower_limit'],
                                                                 'larger-than': ['upper_limit', 'upper_linear_limit']}},
                                                      {'name': 'lower_limit', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                       'range': self.dist_restraint_range,
                                                       'group': {'member-with': ['target_value', 'lower_linear_limit', 'upper_limit', 'upper_linear_limit'],
                                                                 'coexist-with': None, # ['upper_limit'],
                                                                 'smaller-than': None,
                                                                 'larger-than': ['lower_linear_limit', 'upper_limit', 'upper_linear_limit']}},
                                                      {'name': 'upper_limit', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                       'range': self.dist_restraint_range,
                                                       'group': {'member-with': ['target_value', 'lower_linear_limit', 'lower_limit', 'upper_linear_limit'],
                                                                 'coexist-with': None, # ['lower_limit'],
                                                                 'smaller-than': ['lower_linear_limit', 'lower_limit', 'upper_linear_limit'],
                                                                 'larger-than': None}},
                                                      {'name': 'upper_linear_limit', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                       'range': self.dist_restraint_range,
                                                       'group': {'member-with': ['target_value', 'lower_linear_limit', 'lower_limit', 'upper_limit'],
                                                                 'coexist-with': None, # ['lower_linear_limit', 'lower_limit', 'upper_limit'],
                                                                 'smaller-than': ['lower_linear_limit', 'lower_limit'],
                                                                 'larger-than': ['upper_limit']}}
                                                      ],
                                   'dihed_restraint': [{'name': 'index', 'type': 'index-int', 'mandatory': True},
                                                       {'name': 'restraint_id', 'type': 'positive-int', 'mandatory': True},
                                                       {'name': 'restraint_combination_id', 'type': 'positive-int', 'mandatory': False,
                                                        'enforce-non-zero': True},
                                                       {'name': 'weight', 'type': 'range-float', 'mandatory': True,
                                                        'range': self.weight_range,
                                                        'enforce-non-zero': True},
                                                       {'name': 'target_value', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                       'range': self.dihed_restraint_range,
                                                       'group': {'member-with': ['lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit'],
                                                                 'coexist-with': None,
                                                                 'smaller-than': ['lower_limit', 'lower_linear_limit'],
                                                                 'larger-than': ['upper_limit', 'upper_linear_limit']}},
                                                      {'name': 'target_value_uncertainty', 'type': 'range-float', 'mandatory': False,
                                                       'range': self.dihed_restraint_error},
                                                      {'name': 'lower_linear_limit', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                       'range': self.dihed_restraint_range,
                                                       'group': {'member-with': ['target_value', 'lower_limit', 'upper_limit', 'upper_linear_limit'],
                                                                 'coexist-with': None, # ['lower_limit', 'upper_limit', 'upper_linear_limit'],
                                                                 'smaller-than': ['lower_limit'],
                                                                 'larger-than': ['upper_limit', 'upper_linear_limit']}},
                                                      {'name': 'lower_limit', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                       'range': self.dihed_restraint_range,
                                                       'group': {'member-with': ['target_value', 'lower_linear_limit', 'upper_limit', 'upper_linear_limit'],
                                                                 'coexist-with': None, # ['upper_limit'],
                                                                 'smaller-than': None,
                                                                 'larger-than': ['lower_linear_limit', 'upper_limit', 'upper_linear_limit']}},
                                                      {'name': 'upper_limit', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                       'range': self.dihed_restraint_range,
                                                       'group': {'member-with': ['target_value', 'lower_linear_limit', 'lower_limit', 'upper_linear_limit'],
                                                                 'coexist-with': None, # ['lower_limit'],
                                                                 'smaller-than': ['lower_linear_limit', 'lower_limit', 'upper_linear_limit'],
                                                                 'larger-than': None}},
                                                      {'name': 'upper_linear_limit', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                       'range': self.dihed_restraint_range,
                                                       'group': {'member-with': ['target_value', 'lower_linear_limit', 'lower_limit', 'upper_limit'],
                                                                 'coexist-with': None, # ['lower_linear_limit', 'lower_limit', 'upper_limit'],
                                                                 'smaller-than': ['lower_linear_limit', 'lower_limit'],
                                                                 'larger-than': ['upper_limit']}},
                                                       {'name': 'name', 'type': 'str', 'mandatory': False},
                                                    ],
                                   'rdc_restraint': [{'name': 'index', 'type': 'index-int', 'mandatory': True},
                                                     {'name': 'restraint_id', 'type': 'positive-int', 'mandatory': True},
                                                     {'name': 'restraint_combination_id', 'type': 'positive-int', 'mandatory': False,
                                                      'enforce-non-zero': True},
                                                     {'name': 'target_value', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                       'range': self.rdc_restraint_range,
                                                       'group': {'member-with': ['lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit'],
                                                                 'coexist-with': None,
                                                                 'smaller-than': ['lower_limit', 'lower_linear_limit'],
                                                                 'larger-than': ['upper_limit', 'upper_linear_limit']}},
                                                      {'name': 'target_value_uncertainty', 'type': 'range-float', 'mandatory': False,
                                                       'range': self.rdc_restraint_error},
                                                      {'name': 'lower_linear_limit', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                       'range': self.rdc_restraint_range,
                                                       'group': {'member-with': ['target_value', 'lower_limit', 'upper_limit', 'upper_linear_limit'],
                                                                 'coexist-with': None, # ['lower_limit', 'upper_limit', 'upper_linear_limit'],
                                                                 'smaller-than': ['lower_limit'],
                                                                 'larger-than': ['upper_limit', 'upper_linear_limit']}},
                                                      {'name': 'lower_limit', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                       'range': self.rdc_restraint_range,
                                                       'group': {'member-with': ['target_value', 'lower_linear_limit', 'upper_limit', 'upper_linear_limit'],
                                                                 'coexist-with': None, # ['upper_limit'],
                                                                 'smaller-than': None,
                                                                 'larger-than': ['lower_linear_limit', 'upper_limit', 'upper_linear_limit']}},
                                                      {'name': 'upper_limit', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                       'range': self.rdc_restraint_range,
                                                       'group': {'member-with': ['target_value', 'lower_linear_limit', 'lower_limit', 'upper_linear_limit'],
                                                                 'coexist-with': None, # ['lower_limit'],
                                                                 'smaller-than': ['lower_linear_limit', 'lower_limit', 'upper_linear_limit'],
                                                                 'larger-than': None}},
                                                      {'name': 'upper_linear_limit', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                       'range': self.rdc_restraint_range,
                                                       'group': {'member-with': ['target_value', 'lower_linear_limit', 'lower_limit', 'upper_limit'],
                                                                 'coexist-with': None, # ['lower_linear_limit', 'lower_limit', 'upper_limit'],
                                                                 'smaller-than': ['lower_linear_limit', 'lower_limit'],
                                                                 'larger-than': ['upper_limit']}},
                                                     {'name': 'scale', 'type': 'range-float', 'mandatory': False,
                                                      'range': self.scale_range,
                                                      'enforce-non-zero': True},
                                                     {'name': 'distance_dependent', 'type': 'bool', 'mandatory': False}
                                                     ],
                                   'spectral_peak': [{'name': 'index', 'type': 'index-int', 'mandatory': True},
                                                     {'name': 'peak_id', 'type': 'positive-int', 'mandatory': True,
                                                      'enforce-non-zero': True},
                                                     {'name': 'volume', 'type': 'float', 'mandatory': False, 'group-mandatory': True,
                                                      'group': {'member-with': ['height'],
                                                                'coexist-with': None}},
                                                     {'name': 'volume_uncertainty', 'type': 'positive-float', 'mandatory': False},
                                                     {'name': 'height', 'type': 'float', 'mandatory': False, 'group-mandatory': True,
                                                      'group': {'member-with': ['volume'],
                                                                'coexist-with': None}},
                                                     {'name': 'height_uncertainty', 'type': 'positive-float', 'mandatory': False}
                                                     ]
                                   },
                           'nmr-star': {'poly_seq': [{'name': 'Auth_asym_ID', 'type': 'str', 'mandatory': False},
                                                     {'name': 'Auth_seq_ID', 'type': 'int', 'mandatory': False},
                                                     {'name': 'Auth_comp_ID', 'type': 'str', 'mandatory': False},
                                                     {'name': 'Auth_variant_ID', 'type': 'str', 'mandatory': False},
                                                     {'name': 'Sequence_linking', 'type': 'enum', 'mandatory': False,
                                                      'enum': ('start', 'end', 'middle', 'cyclic', 'break', 'single', 'dummy'),
                                                      'enforce-enum': True},
                                                     {'name': 'Cis_residue', 'type': 'bool', 'mandatory': False},
                                                     {'name': 'NEF_index', 'type': 'index-int', 'mandatory': False},
                                                     {'name': 'Assembly_ID', 'type': 'pointer-index', 'mandatory': False}
                                                     ],
                                        'chem_shift': [{'name': 'Atom_type', 'type': 'enum', 'mandatory': True,
                                                        'enum': set(self.atom_isotopes.keys()),
                                                        'enforce-enum': True},
                                                       {'name': 'Atom_isotope_number', 'type': 'enum-int', 'mandatory': True,
                                                        'enum': set(isotope_nums),
                                                        'enforce-enum': True},
                                                       {'name': 'Val', 'type': 'range-float', 'mandatory': True,
                                                        'range': self.chem_shift_range},
                                                       {'name': 'Val_err', 'type': 'range-float', 'mandatory': False,
                                                        'range': self.chem_shift_error},
                                                       {'name': 'Ambiguity_code', 'type': 'enum-int', 'mandatory': False,
                                                        'enum': self.bmrb_ambiguity_codes,
                                                        'enforce-enum': True},
                                                       {'name': 'Ambiguity_set_ID', 'type': 'positive-int', 'mandatory': False,
                                                        'enforce-non-zero': True},
                                                       {'name': 'Auth_asym_ID', 'type': 'str', 'mandatory': False},
                                                       {'name': 'Auth_seq_ID', 'type': 'int', 'mandatory': False},
                                                       {'name': 'Auth_comp_ID', 'type': 'str', 'mandatory': False},
                                                       {'name': 'Auth_atom_ID', 'type': 'str', 'mandatory': False},
                                                       {'name': 'Assigned_chem_shift_list_ID', 'type': 'pointer-index', 'mandatory': True}
                                                       ],
                                        'dist_restraint': [{'name': 'Index_ID', 'type': 'index-int', 'mandatory': True},
                                                           {'name': 'ID', 'type': 'positive-int', 'mandatory': True,
                                                            'enforce-non-zero': True},
                                                           {'name': 'Combination_ID', 'type': 'positive-int', 'mandatory': False,
                                                            'enforce-non-zero': True},
                                                           {'name': 'Member_logic_code', 'type': 'enum', 'mandatory': False,
                                                            'enum': ('OR', 'AND'),
                                                            'enforce-enum': True},
                                                           {'name': 'Target_val', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                            'range': self.dist_restraint_range,
                                                            'group': {'member-with': ['Lower_linear_limit', 'Upper_linear_limit', 'Distance_lower_bound_val', 'Distance_upper_bound_val'],
                                                                      'coexist-with': None,
                                                                      'smaller-than': ['Lower_linear_limit', 'Distance_lower_bound_val'],
                                                                      'larger-than': ['Upper_linear_limit', 'Distance_upper_bound_val']}},
                                                           {'name': 'Target_val_uncertainty', 'type': 'range-float', 'mandatory': False,
                                                            'range': self.dist_restraint_error},
                                                           {'name': 'Lower_linear_limit', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                            'range': self.dist_restraint_range,
                                                            'group': {'member-with': ['Target_val', 'Upper_linear_limit', 'Distance_lower_bound_val', 'Distance_upper_bound_val'],
                                                                      'coexist-with': None, # ['Upper_linear_limit', 'Distance_lower_bound_val', 'Distance_upper_bound_val'],
                                                                      'smaller-than': ['Distance_upper_bound_val'],
                                                                      'larger-than': ['Upper_linear_limit', 'Distance_lower_bound_val']}},
                                                           {'name': 'Upper_linear_limit', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                            'range': self.dist_restraint_range,
                                                            'group': {'member-with': ['Target_val', 'Lower_linear_limit', 'Distance_lower_bound_val', 'Distance_upper_bound_val'],
                                                                      'coexist-with': None, # ['Lower_linear_limit', 'Distance_lower_bound_val', 'Distance_upper_bound_val'],
                                                                      'smaller-than': ['Lower_linear_limit', 'Distance_lower_bound_val'],
                                                                      'larger-than': ['Distance_upper_bound_val']}},
                                                           {'name': 'Distance_lower_bound_val', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                            'range': self.dist_restraint_range,
                                                            'group': {'member-with': ['Target_val', 'Lower_linear_limit', 'Upper_linear_limit', 'Distance_upper_bound_val'],
                                                                      'coexist-with': None, # ['Distance_upper_bound_val'],
                                                                      'smaller-than': None,
                                                                      'larger-than': ['Lower_linear_limit', 'Upper_linear_limit', 'Distance_upper_bound_val']}},
                                                           {'name': 'Distance_upper_bound_val', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                            'range': self.dist_restraint_range,
                                                            'group': {'member-with': ['Target_val', 'Lower_linear_limit', 'Upper_linear_limit', 'Distance_lower_bound_val'],
                                                                      'coexist-with': None, # ['Distance_lower_bound_val'],
                                                                      'smaller-than': ['Lower_linear_limit', 'Distance_lower_bound_val', 'Upper_linear_limit'],
                                                                      'larger-than': None}},
                                                           {'name': 'Weight', 'type': 'range-float', 'mandatory': True,
                                                            'range': self.weight_range,
                                                            'enforce-non-zero': True},
                                                           {'name': 'Auth_asym_ID_1', 'type': 'str', 'mandatory': False},
                                                           {'name': 'Auth_seq_ID_1', 'type': 'int', 'mandatory': False},
                                                           {'name': 'Auth_comp_ID_1', 'type': 'str', 'mandatory': False},
                                                           {'name': 'Auth_atom_ID_1', 'type': 'str', 'mandatory': False},
                                                           {'name': 'Auth_asym_ID_2', 'type': 'str', 'mandatory': False},
                                                           {'name': 'Auth_seq_ID_2', 'type': 'int', 'mandatory': False},
                                                           {'name': 'Auth_comp_ID_2', 'type': 'str', 'mandatory': False},
                                                           {'name': 'Auth_atom_ID_2', 'type': 'str', 'mandatory': False},
                                                           {'name': 'Gen_dist_constraint_list_ID', 'type': 'pointer-index', 'mandatory': True},
                                                           ],
                                        'dihed_restraint': [{'name': 'Index_ID', 'type': 'index-int', 'mandatory': True},
                                                            {'name': 'ID', 'type': 'index-int', 'mandatory': True},
                                                            {'name': 'Combination_ID', 'type': 'positive-int', 'mandatory': False,
                                                             'enforce-non-zero': True},
                                                            {'name': 'Torsion_angle_name', 'type': 'str', 'mandatory': False},
                                                            {'name': 'Angle_lower_bound_val', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                             'range': self.dihed_restraint_range,
                                                             'group': {'member-with': ['Angle_target_val', 'Angle_lower_linear_limit', 'Angle_upper_linear_limit', 'Angle_upper_bound_val'],
                                                                       'coexist-with': None, # ['Angle_upper_bound_val'],
                                                                       'smaller-than': None,
                                                                       'larger-than': ['Angle_lower_linear_limit', 'Angle_upper_linear_limit', 'Angle_upper_bound_val']}},
                                                            {'name': 'Angle_upper_bound_val', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                             'range': self.dihed_restraint_range,
                                                             'group': {'member-with': ['Angle_target_val', 'Angle_lower_linear_limit', 'Angle_upper_linear_limit', 'Angle_lower_bound_val'],
                                                                       'coexist-with': None, # ['Angle_lower_bound_val'],
                                                                       'smaller-than': ['Angle_lower_linear_limit', 'Angle_lower_bound_val', 'Angle_upper_linear_limit'],
                                                                       'larger-than': None}},
                                                            {'name': 'Angle_target_val', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                             'range': self.dihed_restraint_range,
                                                             'group': {'member-with': ['Angle_lower_linear_limit', 'Angle_upper_linear_limit', 'Angle_lower_bound_val', 'Angle_upper_bound_val'],
                                                                       'coexist-with': None,
                                                                       'smaller-than': ['Angle_lower_linear_limit', 'Angle_lower_bound_val'],
                                                                       'larger-than': ['Angle_upper_linear_limit', 'Angle_upper_bound_val']}},
                                                            {'name': 'Angle_target_val_err', 'type': 'range-float', 'mandatory': False,
                                                             'range': self.dihed_restraint_error},
                                                            {'name': 'Angle_lower_linear_limit', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                             'range': self.dihed_restraint_range,
                                                             'group': {'member-with': ['Angle_target_val', 'Angle_upper_linear_limit', 'Angle_lower_bound_val', 'Angle_upper_bound_val'],
                                                                       'coexist-with': None, # ['Angle_upper_linear_limit', 'Angle_lower_bound_val', 'Angle_upper_bound_val'],
                                                                       'smaller-than': ['Angle_lower_bound_val'],
                                                                       'larger-than': ['Angle_upper_linear_limit', 'Angle_upper_bound_val']}},
                                                            {'name': 'Angle_upper_linear_limit', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                             'range': self.dihed_restraint_range,
                                                             'group': {'member-with': ['Angle_target_val', 'Angle_lower_linear_limit', 'Angle_lower_bound_val', 'Angle_upper_bound_val'],
                                                                      'coexist-with': None, # ['Angle_lower_linear_limit', 'Angle_lower_bound_val', 'Angle_upper_bound_val'],
                                                                      'smaller-than': ['Angle_lower_linear_limit', 'Angle_lower_bound_val'],
                                                                      'larger-than': ['Angle_upper_bound_val']}},
                                                            {'name': 'Weight', 'type': 'range-float', 'mandatory': True,
                                                             'range': self.weight_range,
                                                             'enforce-non-zero': True},
                                                            {'name': 'Auth_asym_ID_1', 'type': 'str', 'mandatory': False},
                                                            {'name': 'Auth_seq_ID_1', 'type': 'int', 'mandatory': False},
                                                            {'name': 'Auth_comp_ID_1', 'type': 'str', 'mandatory': False},
                                                            {'name': 'Auth_atom_ID_1', 'type': 'str', 'mandatory': False},
                                                            {'name': 'Auth_asym_ID_2', 'type': 'str', 'mandatory': False},
                                                            {'name': 'Auth_seq_ID_2', 'type': 'int', 'mandatory': False},
                                                            {'name': 'Auth_comp_ID_2', 'type': 'str', 'mandatory': False},
                                                            {'name': 'Auth_atom_ID_2', 'type': 'str', 'mandatory': False},
                                                            {'name': 'Auth_asym_ID_3', 'type': 'str', 'mandatory': False},
                                                            {'name': 'Auth_seq_ID_3', 'type': 'int', 'mandatory': False},
                                                            {'name': 'Auth_comp_ID_3', 'type': 'str', 'mandatory': False},
                                                            {'name': 'Auth_atom_ID_3', 'type': 'str', 'mandatory': False},
                                                            {'name': 'Auth_asym_ID_4', 'type': 'str', 'mandatory': False},
                                                            {'name': 'Auth_seq_ID_4', 'type': 'int', 'mandatory': False},
                                                            {'name': 'Auth_comp_ID_4', 'type': 'str', 'mandatory': False},
                                                            {'name': 'Auth_atom_ID_4', 'type': 'str', 'mandatory': False},
                                                            {'name': 'Torsion_angle_constraint_list_ID', 'type': 'pointer-index', 'mandatory': True},
                                            ],
                                        'rdc_restraint': [{'name': 'Index_ID', 'type': 'index-int', 'mandatory': True},
                                                          {'name': 'ID', 'type': 'index-int', 'mandatory': True},
                                                          {'name': 'Combination_ID', 'type': 'positive-int', 'mandatory': False,
                                                           'enforce-non-zero': True},
                                                          {'name': 'Weight', 'type': 'range-float', 'mandatory': True,
                                                           'range': self.weight_range,
                                                           'enforce-non-zero': True},
                                                          {'name': 'Target_value', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                           'range': self.rdc_restraint_range,
                                                           'group': {'member-with': ['RDC_lower_linear_limit', 'RDC_upper_linear_limit', 'RDC_lower_bound', 'RDC_upper_bound'],
                                                                     'coexist-with': None,
                                                                     'smaller-than': ['RDC_lower_linear_limit', 'RDC_lower_bound'],
                                                                     'larger-than': ['RDC_upper_linear_limit', 'RDC_upper_bound']}},
                                                          {'name': 'Target_value_uncertainty', 'type': 'range-float', 'mandatory': False,
                                                           'range': self.rdc_restraint_error},
                                                          {'name': 'RDC_lower_bound', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                           'range': self.rdc_restraint_range,
                                                           'group': {'member-with': ['Target_value', 'RDC_lower_linear_limit', 'RDC_upper_linear_limit', 'RDC_upper_bound'],
                                                                     'coexist-with': None, # ['RDC_upper_bound'],
                                                                     'smaller-than': None,
                                                                     'larger-than': ['RDC_lower_linear_limit', 'RDC_upper_linear_limit', 'RDC_upper_bound']}},
                                                          {'name': 'RDC_upper_bound', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                           'range': self.rdc_restraint_range,
                                                           'group': {'member-with': ['Target_value', 'RDC_lower_linear_limit', 'RDC_upper_linear_limit', 'RDC_lower_bound'],
                                                                     'coexist-with': None, # ['RDC_lower_bound'],
                                                                     'smaller-than': ['RDC_lower_linear_limit', 'RDC_lower_bound', 'RDC_upper_linear_limit'],
                                                                     'larger-than': None}},
                                                          {'name': 'RDC_lower_linear_limit', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                           'range': self.rdc_restraint_range,
                                                           'group': {'member-with': ['Target_value', 'RDC_upper_linear_limit', 'RDC_lower_bound', 'RDC_upper_bound'],
                                                                     'coexist-with': None, # ['RDC_upper_linear_limit', 'RDC_lower_bound', 'RDC_upper_bound'],
                                                                     'smaller-than': ['RDC_lower_bound'],
                                                                     'larger-than': ['RDC_upper_linear_limit', 'RDC_upper_bound']}},
                                                          {'name': 'RDC_upper_linear_limit', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                           'range': self.rdc_restraint_range,
                                                           'group': {'member-with': ['Target_value', 'RDC_upper_linear_limit', 'RDC_lower_bound', 'RDC_upper_bound'],
                                                                     'coexist-with': None, # ['RDC_upper_linear_limit', 'RDC_lower_bound', 'RDC_upper_bound'],
                                                                     'smaller-than': ['RDC_upper_bound'],
                                                                     'larger-than': ['RDC_upper_linear_limit', 'RDC_lower_bound']}},
                                                          {'name': 'RDC_val_scale_factor', 'type': 'range-float', 'mandatory': False,
                                                           'range': self.scale_range,
                                                           'enforce-non-zero': True},
                                                          {'name': 'RDC_distant_dependent', 'type': 'bool', 'mandatory': False},
                                                          {'name': 'Auth_asym_ID_1', 'type': 'str', 'mandatory': False},
                                                          {'name': 'Auth_seq_ID_1', 'type': 'int', 'mandatory': False},
                                                          {'name': 'Auth_comp_ID_1', 'type': 'str', 'mandatory': False},
                                                          {'name': 'Auth_atom_ID_1', 'type': 'str', 'mandatory': False},
                                                          {'name': 'Auth_asym_ID_2', 'type': 'str', 'mandatory': False},
                                                          {'name': 'Auth_seq_ID_2', 'type': 'int', 'mandatory': False},
                                                          {'name': 'Auth_comp_ID_2', 'type': 'str', 'mandatory': False},
                                                          {'name': 'Auth_atom_ID_2', 'type': 'str', 'mandatory': False},
                                                          {'name': 'RDC_constraint_list_ID', 'type': 'pointer-index', 'mandatory': True}
                                                          ],
                                        'spectral_peak': [{'name': 'Index_ID', 'type': 'index-int', 'mandatory': True},
                                                          {'name': 'ID', 'type': 'positive-int', 'mandatory': True,
                                                           'enforce-non-zero': True},
                                                          {'name': 'Volume', 'type': 'float', 'mandatory': False, 'group-mandatory': True,
                                                           'group': {'member-with': ['Height'],
                                                                     'coexist-with': None}},
                                                          {'name': 'Volume_uncertainty', 'type': 'positive-float', 'mandatory': False},
                                                          {'name': 'Height', 'type': 'float', 'mandatory': False, 'group-mandatory': True,
                                                           'group': {'member-with': ['Volume'],
                                                                     'coexist-with': None}},
                                                          {'name': 'Height_uncertainty', 'type': 'positive-float', 'mandatory': False},
                                                          {'name': 'Spectral_peak_list_ID', 'type': 'pointer-index', 'mandatory': True}
                                                          ]
                                        }
                           }

        # common potential descriptor items
        self.potential_items = {'nef': {'dist_restraint':  {'target_value': 'target_value',
                                                            'lower_limit': 'lower_limit',
                                                            'upper_limit': 'upper_limit',
                                                            'lower_linear_limit': 'lower_linear_limit',
                                                            'upper_linear_limit': 'upper_linear_limit'},
                                        'dihed_restraint': {'target_value': 'target_value',
                                                            'lower_limit': 'lower_limit',
                                                            'upper_limit': 'upper_limit',
                                                            'lower_linear_limit': 'lower_linear_limit',
                                                            'upper_linear_limit': 'upper_linear_limit'},
                                        'rdc_restraint':   {'target_value': 'target_value',
                                                            'lower_limit': 'lower_limit',
                                                            'upper_limit': 'upper_limit',
                                                            'lower_linear_limit': 'lower_linear_limit',
                                                            'upper_linear_limit': 'upper_linear_limit'}
                                        },
                                'nmr-star': {'dist_restraint':  {'target_value': 'Target_val',
                                                                 'lower_limit': 'Distance_lower_bound_val',
                                                                 'upper_limit': 'Distance_upper_bound_val',
                                                                 'lower_linear_limit': 'Lower_linear_limit',
                                                                 'upper_linear_limit': 'Upper_linear_limit'},
                                             'dihed_restraint': {'target_value': 'Angle_target_val',
                                                                 'lower_limit': 'Angle_lower_bound_val',
                                                                 'upper_limit': 'Angle_upper_bound_val',
                                                                 'lower_linear_limit': 'Angle_lower_linear_limit',
                                                                 'upper_linear_limit': 'Angle_upper_linear_limit'},
                                             'rdc_restraint':   {'target_value': 'Target_value',
                                                                 'lower_limit': 'RDC_lower_bound',
                                                                 'upper_limit': 'RDC_upper_bound',
                                                                 'lower_linear_limit': 'RDC_lower_linear_limit',
                                                                 'upper_linear_limit': 'RDC_upper_linear_limit'}
                                             }
                                }

        # loop data items for spectral peak
        self.pk_data_items = {'nef': [{'name': 'position_uncertainty_%s', 'type': 'range-float', 'mandatory': False,
                                       'range': self.chem_shift_error},
                                      {'name': 'chain_code_%s', 'type': 'str', 'mandatory': False,
                                       'relax-key-if-exist': True},
                                      {'name': 'sequence_code_%s', 'type': 'int', 'mandatory': False,
                                       'relax-key-if-exist': True},
                                      {'name': 'residue_name_%s', 'type': 'str', 'mandatory': False,
                                       'relax-key-if-exist': True},
                                      {'name': 'atom_name_%s', 'type': 'str', 'mandatory': False,
                                       'relax-key-if-exist': True}],
                              'nmr-star': [{'name': 'Position_uncertainty_%s', 'type': 'range-float', 'mandatory': False,
                                            'range': self.chem_shift_error},
                                           {'name': 'Entity_assembly_ID_%s', 'type': 'positive-int', 'mandatory': False,
                                            'enforce-non-zero': True,
                                            'relax-key-if-exist': True},
                                           {'name': 'Comp_index_ID_%s', 'type': 'int', 'mandatory': False,
                                            'relax-key-if-exist': True},
                                           {'name': 'Comp_ID_%s', 'type': 'str', 'mandatory': False,
                                            'relax-key-if-exist': True},
                                           {'name': 'Atom_ID_%s', 'type': 'str', 'mandatory': False,
                                            'relax-key-if-exist': True},
                                           {'name': 'Auth_asym_ID_%s', 'type': 'str', 'mandatory': False},
                                           {'name': 'Auth_seq_ID_%s', 'type': 'int', 'mandatory': False},
                                           {'name': 'Auth_comp_ID_%s', 'type': 'str', 'mandatory': False},
                                           {'name': 'Auth_atom_ID_%s', 'type': 'str', 'mandatory': False}]
                              }

        # number of dimension of spectral peak
        self.num_dim_items = {'nef': 'num_dimensions', 'nmr-star': 'Number_of_spectral_dimensions'}

        # allowed loop tags
        self.allowed_tags = {'nef': {'entry_info': ['program_name', 'script_name', 'script'],
                                     'poly_seq': ['index', 'chain_code', 'sequence_code', 'residue_name', 'linking', 'residue_variant', 'cis_peptide'],
                                     'chem_shift': ['chain_code', 'sequence_code', 'residue_name', 'atom_name', 'value', 'value_uncertainty', 'element', 'isotope_number'],
                                     'dist_restraint': ['index', 'restraint_id', 'restraint_combination_id', 'chain_code_1', 'sequence_code_1', 'residue_name_1', 'atom_name_1', 'chain_code_2', 'sequence_code_2', 'residue_name_2', 'atom_name_2', 'weight', 'target_value', 'target_value_uncertainty', 'lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit'],
                                     'dihed_restraint': ['index', 'restraint_id', 'restraint_combination_id', 'chain_code_1', 'sequence_code_1', 'residue_name_1', 'atom_name_1', 'chain_code_2', 'sequence_code_2', 'residue_name_2', 'atom_name_2', 'chain_code_3', 'sequence_code_3', 'residue_name_3', 'atom_name_3', 'chain_code_4', 'sequence_code_4', 'residue_name_4', 'atom_name_4', 'weight', 'target_value', 'target_value_uncertainty', 'lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit', 'name' ],
                                     'rdc_restraint': ['index', 'restraint_id', 'restraint_combination_id', 'chain_code_1', 'sequence_code_1', 'residue_name_1', 'atom_name_1', 'chain_code_2', 'sequence_code_2', 'residue_name_2', 'atom_name_2', 'weight', 'target_value', 'target_value_uncertainty', 'lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit', 'scale', 'distance_dependent'],
                                     'spectral_peak': ['index', 'peak_id', 'volume', 'volume_uncertainty', 'height', 'height_uncertainty', 'position_1', 'position_uncertainty_1', 'position_2', 'position_uncertainty_2', 'position_3', 'position_uncertainty_3', 'position_4', 'position_uncertainty_4', 'position_5', 'position_uncertainty_5', 'position_6', 'position_uncertainty_6', 'position_7', 'position_uncertainty_7', 'position_8', 'position_uncertainty_8', 'position_9', 'position_uncertainty_9', 'position_10', 'position_uncertainty_10', 'position_11', 'position_uncertainty_11', 'position_12', 'position_uncertainty_12', 'position_13', 'position_uncertainty_13', 'position_14', 'position_uncertainty_14', 'position_15', 'position_uncertainty_15', 'chain_code_1', 'sequence_code_1', 'residue_name_1', 'atom_name_1', 'chain_code_2', 'sequence_code_2', 'residue_name_2', 'atom_name_2', 'chain_code_3', 'sequence_code_3', 'residue_name_3', 'atom_name_3', 'chain_code_4', 'sequence_code_4', 'residue_name_4', 'atom_name_4', 'chain_code_5', 'sequence_code_5', 'residue_name_5', 'atom_name_5', 'chain_code_6', 'sequence_code_6', 'residue_name_6', 'atom_name_6', 'chain_code_7', 'sequence_code_7', 'residue_name_7', 'atom_name_7', 'chain_code_8', 'sequence_code_8', 'residue_name_8', 'atom_name_8', 'chain_code_9', 'sequence_code_9', 'residue_name_9', 'atom_name_9', 'chain_code_10', 'sequence_code_10', 'residue_name_10', 'atom_name_10', 'chain_code_11', 'sequence_code_11', 'residue_name_11', 'atom_name_11', 'chain_code_12', 'sequence_code_12', 'residue_name_12', 'atom_name_12', 'chain_code_13', 'sequence_code_13', 'residue_name_13', 'atom_name_13', 'chain_code_14', 'sequence_code_14', 'residue_name_14', 'atom_name_14', 'chain_code_15', 'sequence_code_15', 'residue_name_15', 'atom_name_15']
                                     },
                             'nmr-star': {'entry_info': ['Software_ID', 'Software_label', 'Methods_ID', 'Methods_label', 'Software_name', 'Script_name', 'Script', 'Software_specific_info', 'Sf_ID', 'Entry_ID', 'Software_applied_list_ID'],
                                          'poly_seq': ['Assembly_chem_comp_ID', 'Entity_assembly_ID', 'Entity_ID', 'Comp_index_ID', 'Comp_ID', 'Seq_ID', 'Auth_entity_assembly_ID', 'Auth_asym_ID', 'Auth_seq_ID', 'Auth_comp_ID', 'Auth_variant_ID', 'Sequence_linking', 'Cis_residue', 'NEF_index', 'Sf_ID', 'Entry_ID', 'Assembly_ID'],
                                          'chem_shift': ['ID', 'Assembly_atom_ID', 'Entity_assembly_ID', 'Entity_ID', 'Comp_index_ID', 'Seq_ID', 'Comp_ID', 'Atom_ID', 'Atom_type', 'Atom_isotope_number', 'Val', 'Val_err', 'Assign_fig_of_merit', 'Ambiguity_code', 'Ambiguity_set_ID', 'Occupancy', 'Resonance_ID', 'Auth_entity_assembly_ID', 'Auth_asym_ID', 'Auth_seq_ID', 'Auth_comp_ID', 'Auth_atom_ID', 'PDB_record_ID', 'PDB_model_num', 'PDB_strand_ID', 'PDB_ins_code', 'PDB_residue_no', 'PDB_residue_name', 'PDB_atom_name', 'Original_PDB_strand_ID', 'Original_PDB_residue_no', 'Original_PDB_residue_name', 'Original_PDB_atom_name', 'Details', 'Sf_ID', 'Entry_ID', 'Assigned_chem_shift_list_ID'],
                                          'dist_restraint': ['Index_ID', 'ID', 'Combination_ID', 'Member_ID', 'Member_logic_code', 'Assembly_atom_ID_1', 'Entity_assembly_ID_1', 'Entity_ID_1', 'Comp_index_ID_1', 'Seq_ID_1', 'Comp_ID_1', 'Atom_ID_1', 'Atom_type_1', 'Atom_isotope_number_1', 'Resonance_ID_1', 'Assembly_atom_ID_2', 'Entity_assembly_ID_2', 'Entity_ID_2', 'Comp_index_ID_2', 'Seq_ID_2', 'Comp_ID_2', 'Atom_ID_2', 'Atom_type_2', 'Atom_isotope_number_2', 'Resonance_ID_2', 'Intensity_val', 'Intensity_lower_val_err', 'Intensity_upper_val_err', 'Distance_val', 'Target_val', 'Target_val_uncertainty', 'Lower_linear_limit', 'Upper_linear_limit', 'Distance_lower_bound_val', 'Distance_upper_bound_val', 'Contribution_fractional_val', 'Weight', 'Spectral_peak_ID', 'Spectral_peak_list_ID', 'PDB_record_ID_1', 'PDB_model_num_1', 'PDB_strand_ID_1', 'PDB_ins_code_1', 'PDB_residue_no_1', 'PDB_residue_name_1', 'PDB_atom_name_1', 'PDB_record_ID_2', 'PDB_model_num_2', 'PDB_strand_ID_2', 'PDB_ins_code_2', 'PDB_residue_no_2', 'PDB_residue_name_2', 'PDB_atom_name_2', 'Auth_entity_assembly_ID_1', 'Auth_asym_ID_1', 'Auth_chain_ID_1', 'Auth_seq_ID_1', 'Auth_comp_ID_1', 'Auth_atom_ID_1', 'Auth_alt_ID_1', 'Auth_atom_name_1', 'Auth_entity_assembly_ID_2', 'Auth_asym_ID_2', 'Auth_chain_ID_2', 'Auth_seq_ID_2', 'Auth_comp_ID_2', 'Auth_atom_ID_2', 'Auth_alt_ID_2', 'Auth_atom_name_2', 'Sf_ID', 'Entry_ID', 'Gen_dist_constraint_list_ID'],
                                          'dihed_restraint': ['Index_ID', 'ID', 'Combination_ID', 'Set_ID', 'Torsion_angle_name', 'Assembly_atom_ID_1', 'Entity_assembly_ID_1', 'Entity_ID_1', 'Comp_index_ID_1', 'Seq_ID_1', 'Comp_ID_1', 'Atom_ID_1', 'Atom_type_1', 'Resonance_ID_1', 'Assembly_atom_ID_2', 'Entity_assembly_ID_2', 'Entity_ID_2', 'Comp_index_ID_2', 'Seq_ID_2', 'Comp_ID_2', 'Atom_ID_2', 'Atom_type_2', 'Resonance_ID_2', 'Assembly_atom_ID_3', 'Entity_assembly_ID_3', 'Entity_ID_3', 'Comp_index_ID_3', 'Seq_ID_3', 'Comp_ID_3', 'Atom_ID_3', 'Atom_type_3', 'Resonance_ID_3', 'Assembly_atom_ID_4', 'Entity_assembly_ID_4', 'Entity_ID_4', 'Comp_index_ID_4', 'Seq_ID_4', 'Comp_ID_4', 'Atom_ID_4', 'Atom_type_4', 'Resonance_ID_4', 'Angle_lower_bound_val', 'Angle_upper_bound_val', 'Angle_target_val', 'Angle_target_val_err', 'Angle_lower_linear_limit', 'Angle_upper_linear_limit', 'Weight', 'Source_experiment_ID', 'Figure_of_merit', 'PDB_record_ID_1', 'PDB_model_num_1', 'PDB_strand_ID_1', 'PDB_ins_code_1', 'PDB_residue_no_1', 'PDB_residue_name_1', 'PDB_atom_name_1', 'PDB_record_ID_2', 'PDB_model_num_2', 'PDB_strand_ID_2', 'PDB_ins_code_2', 'PDB_residue_no_2', 'PDB_residue_name_2', 'PDB_atom_name_2', 'PDB_record_ID_3', 'PDB_model_num_3', 'PDB_strand_ID_3', 'PDB_ins_code_3', 'PDB_residue_no_3', 'PDB_residue_name_3', 'PDB_atom_name_3', 'PDB_record_ID_4', 'PDB_model_num_4', 'PDB_strand_ID_4', 'PDB_ins_code_4', 'PDB_residue_no_4', 'PDB_residue_name_4', 'PDB_atom_name_4', 'Auth_entity_assembly_ID_1', 'Auth_asym_ID_1', 'Auth_chain_ID_1', 'Auth_seq_ID_1', 'Auth_comp_ID_1', 'Auth_atom_ID_1', 'Auth_alt_ID_1', 'Auth_atom_name_1', 'Auth_entity_assembly_ID_2', 'Auth_asym_ID_2', 'Auth_chain_ID_2', 'Auth_seq_ID_2', 'Auth_comp_ID_2', 'Auth_atom_ID_2', 'Auth_alt_ID_2', 'Auth_atom_name_2', 'Auth_entity_assembly_ID_3', 'Auth_asym_ID_3', 'Auth_chain_ID_3', 'Auth_seq_ID_3', 'Auth_comp_ID_3', 'Auth_atom_ID_3', 'Auth_alt_ID_3', 'Auth_atom_name_3', 'Auth_entity_assembly_ID_4', 'Auth_asym_ID_4', 'Auth_chain_ID_4', 'Auth_seq_ID_4', 'Auth_comp_ID_4', 'Auth_atom_ID_4', 'Auth_alt_ID_4', 'Auth_atom_name_4', 'Sf_ID', 'Entry_ID', 'Torsion_angle_constraint_list_ID'],
                                          'rdc_restraint': ['Index_ID', 'ID', 'Combination_ID', 'Assembly_atom_ID_1', 'Entity_assembly_ID_1', 'Entity_ID_1', 'Comp_index_ID_1', 'Seq_ID_1', 'Comp_ID_1', 'Atom_ID_1', 'Atom_type_1', 'Atom_isotope_number_1', 'Resonance_ID_1', 'Assembly_atom_ID_2', 'Entity_assembly_ID_2', 'Entity_ID_2', 'Comp_index_ID_2', 'Seq_ID_2', 'Comp_ID_2', 'Atom_ID_2', 'Atom_type_2', 'Atom_isotope_number_2', 'Resonance_ID_2', 'Weight', 'RDC_val', 'RDC_val_err', 'Target_value', 'Target_value_uncertainty', 'RDC_lower_bound', 'RDC_upper_bound', 'RDC_lower_linear_limit', 'RDC_upper_linear_limit', 'RDC_val_scale_factor', 'RDC_bond_length', 'RDC_distant_dependent', 'Source_experiment_ID', 'PDB_record_ID_1', 'PDB_model_num_1', 'PDB_strand_ID_1', 'PDB_ins_code_1', 'PDB_residue_no_1', 'PDB_residue_name_1', 'PDB_atom_name_1', 'PDB_record_ID_2', 'PDB_model_num_2', 'PDB_strand_ID_2', 'PDB_ins_code_2', 'PDB_residue_no_2', 'PDB_residue_name_2', 'PDB_atom_name_2', 'Auth_entity_assembly_ID_1', 'Auth_asym_ID_1', 'Auth_chain_ID_1', 'Auth_seq_ID_1', 'Auth_comp_ID_1', 'Auth_atom_ID_1', 'Auth_alt_ID_1', 'Auth_atom_name_1', 'Auth_entity_assembly_ID_2', 'Auth_asym_ID_2', 'Auth_chain_ID_2', 'Auth_seq_ID_2', 'Auth_comp_ID_2', 'Auth_atom_ID_2', 'Auth_alt_ID_2', 'Auth_atom_name_2', 'Sf_ID', 'Entry_ID', 'RDC_constraint_list_ID'],
                                          'spectral_peak': ['Index_ID', 'ID', 'Volume', 'Volume_uncertainty', 'Height', 'Height_uncertainty', 'Figure_of_merit', 'Restraint', 'Position_1', 'Position_uncertainty_1', 'Line_width_1', 'Line_width_uncertainty_1', 'Position_2', 'Position_uncertainty_2', 'Line_width_2', 'Line_width_uncertainty_2', 'Position_3', 'Position_uncertainty_3', 'Line_width_3', 'Line_width_uncertainty_3', 'Position_4', 'Position_uncertainty_4', 'Line_width_4', 'Line_width_uncertainty_4', 'Position_5', 'Position_uncertainty_5', 'Line_width_5', 'Line_width_uncertainty_5', 'Position_6', 'Position_uncertainty_6', 'Line_width_6', 'Line_width_uncertainty_6', 'Position_7', 'Position_uncertainty_7', 'Line_width_7', 'Line_width_uncertainty_7', 'Position_8', 'Position_uncertainty_8', 'Line_width_8', 'Line_width_uncertainty_8', 'Position_9', 'Position_uncertainty_9', 'Line_width_9', 'Line_width_uncertainty_9', 'Position_10', 'Position_uncertainty_10', 'Line_width_10', 'Line_width_uncertainty_10', 'Position_11', 'Position_uncertainty_11', 'Line_width_11', 'Line_width_uncertainty_11', 'Position_12', 'Position_uncertainty_12', 'Line_width_12', 'Line_width_uncertainty_12', 'Position_13', 'Position_uncertainty_13', 'Line_width_13', 'Line_width_uncertainty_13', 'Position_14', 'Position_uncertainty_14', 'Line_width_14', 'Line_width_uncertainty_14', 'Position_15', 'Position_uncertainty_15', 'Line_width_15', 'Line_width_uncertainty_15', 'Entity_assembly_ID_1', 'Entity_ID_1', 'Comp_index_ID_1', 'Seq_ID_1', 'Comp_ID_1', 'Atom_ID_1', 'Ambiguity_code_1', 'Ambiguity_set_ID_1', 'Entity_assembly_ID_2', 'Entity_ID_2', 'Comp_index_ID_2', 'Seq_ID_2', 'Comp_ID_2', 'Atom_ID_2', 'Ambiguity_code_2', 'Ambiguity_set_ID_2', 'Entity_assembly_ID_3', 'Entity_ID_3', 'Comp_index_ID_3', 'Seq_ID_3', 'Comp_ID_3', 'Atom_ID_3', 'Ambiguity_code_3', 'Ambiguity_set_ID_3', 'Entity_assembly_ID_4', 'Entity_ID_4', 'Comp_index_ID_4', 'Seq_ID_4', 'Comp_ID_4', 'Atom_ID_4', 'Ambiguity_code_4', 'Ambiguity_set_ID_4', 'Entity_assembly_ID_5', 'Entity_ID_5', 'Comp_index_ID_5', 'Seq_ID_5', 'Comp_ID_5', 'Atom_ID_5', 'Ambiguity_code_5', 'Ambiguity_set_ID_5', 'Entity_assembly_ID_6', 'Entity_ID_6', 'Comp_index_ID_6', 'Seq_ID_6', 'Comp_ID_6', 'Atom_ID_6', 'Ambiguity_code_6', 'Ambiguity_set_ID_6', 'Entity_assembly_ID_7', 'Entity_ID_7', 'Comp_index_ID_7', 'Seq_ID_7', 'Comp_ID_7', 'Atom_ID_7', 'Ambiguity_code_7', 'Ambiguity_set_ID_7', 'Entity_assembly_ID_8', 'Entity_ID_8', 'Comp_index_ID_8', 'Seq_ID_8', 'Comp_ID_8', 'Atom_ID_8', 'Ambiguity_code_8', 'Ambiguity_set_ID_8', 'Entity_assembly_ID_9', 'Entity_ID_9', 'Comp_index_ID_9', 'Seq_ID_9', 'Comp_ID_9', 'Atom_ID_9', 'Ambiguity_code_9', 'Ambiguity_set_ID_9', 'Entity_assembly_ID_10', 'Entity_ID_10', 'Comp_index_ID_10', 'Seq_ID_10', 'Comp_ID_10', 'Atom_ID_10', 'Ambiguity_code_10', 'Ambiguity_set_ID_10', 'Entity_assembly_ID_11', 'Entity_ID_11', 'Comp_index_ID_11', 'Seq_ID_11', 'Comp_ID_11', 'Atom_ID_11', 'Ambiguity_code_11', 'Ambiguity_set_ID_11', 'Entity_assembly_ID_12', 'Entity_ID_12', 'Comp_index_ID_12', 'Seq_ID_12', 'Comp_ID_12', 'Atom_ID_12', 'Ambiguity_code_12', 'Ambiguity_set_ID_12', 'Entity_assembly_ID_13', 'Entity_ID_13', 'Comp_index_ID_13', 'Seq_ID_13', 'Comp_ID_13', 'Atom_ID_13', 'Ambiguity_code_13', 'Ambiguity_set_ID_13', 'Entity_assembly_ID_14', 'Entity_ID_14', 'Comp_index_ID_14', 'Seq_ID_14', 'Comp_ID_14', 'Atom_ID_14', 'Ambiguity_code_14', 'Ambiguity_set_ID_14', 'Entity_assembly_ID_15', 'Entity_ID_15', 'Comp_index_ID_15', 'Seq_ID_15', 'Comp_ID_15', 'Atom_ID_15', 'Ambiguity_code_15', 'Ambiguity_set_ID_15', 'Auth_entity_assembly_ID_1', 'Auth_entity_ID_1', 'Auth_asym_ID_1', 'Auth_seq_ID_1', 'Auth_comp_ID_1', 'Auth_atom_ID_1', 'Auth_ambiguity_code_1', 'Auth_ambiguity_set_ID_1', 'Auth_entity_assembly_ID_2', 'Auth_entity_ID_2', 'Auth_asym_ID_2', 'Auth_seq_ID_2', 'Auth_comp_ID_2', 'Auth_atom_ID_2', 'Auth_ambiguity_code_2', 'Auth_ambiguity_set_ID_2', 'Auth_entity_assembly_ID_3', 'Auth_entity_ID_3', 'Auth_asym_ID_3', 'Auth_seq_ID_3', 'Auth_comp_ID_3', 'Auth_atom_ID_3', 'Auth_ambiguity_code_3', 'Auth_ambiguity_set_ID_3', 'Auth_entity_assembly_ID_4', 'Auth_entity_ID_4', 'Auth_asym_ID_4', 'Auth_seq_ID_4', 'Auth_comp_ID_4', 'Auth_atom_ID_4', 'Auth_ambiguity_code_4', 'Auth_ambiguity_set_ID_4', 'Auth_entity_assembly_ID_5', 'Auth_entity_ID_5', 'Auth_asym_ID_5', 'Auth_seq_ID_5', 'Auth_comp_ID_5', 'Auth_atom_ID_5', 'Auth_ambiguity_code_5', 'Auth_ambiguity_set_ID_5', 'Auth_entity_assembly_ID_6', 'Auth_entity_ID_6', 'Auth_asym_ID_6', 'Auth_seq_ID_6', 'Auth_comp_ID_6', 'Auth_atom_ID_6', 'Auth_ambiguity_code_6', 'Auth_ambiguity_set_ID_6', 'Auth_entity_assembly_ID_7', 'Auth_entity_ID_7', 'Auth_asym_ID_7', 'Auth_seq_ID_7', 'Auth_comp_ID_7', 'Auth_atom_ID_7', 'Auth_ambiguity_code_7', 'Auth_ambiguity_set_ID_7', 'Auth_entity_assembly_ID_8', 'Auth_entity_ID_8', 'Auth_asym_ID_8', 'Auth_seq_ID_8', 'Auth_comp_ID_8', 'Auth_atom_ID_8', 'Auth_ambiguity_code_8', 'Auth_ambiguity_set_ID_8', 'Auth_entity_assembly_ID_9', 'Auth_entity_ID_9', 'Auth_asym_ID_9', 'Auth_seq_ID_9', 'Auth_comp_ID_9', 'Auth_atom_ID_9', 'Auth_ambiguity_code_9', 'Auth_ambiguity_set_ID_9', 'Auth_entity_assembly_ID_10', 'Auth_entity_ID_10', 'Auth_asym_ID_10', 'Auth_seq_ID_10', 'Auth_comp_ID_10', 'Auth_atom_ID_10', 'Auth_ambiguity_code_10', 'Auth_ambiguity_set_ID_10', 'Auth_entity_assembly_ID_11', 'Auth_entity_ID_11', 'Auth_asym_ID_11', 'Auth_seq_ID_11', 'Auth_comp_ID_11', 'Auth_atom_ID_11', 'Auth_ambiguity_code_11', 'Auth_ambiguity_set_ID_11', 'Auth_entity_assembly_ID_12', 'Auth_entity_ID_12', 'Auth_asym_ID_12', 'Auth_seq_ID_12', 'Auth_comp_ID_12', 'Auth_atom_ID_12', 'Auth_ambiguity_code_12', 'Auth_ambiguity_set_ID_12', 'Auth_entity_assembly_ID_13', 'Auth_entity_ID_13', 'Auth_asym_ID_13', 'Auth_seq_ID_13', 'Auth_comp_ID_13', 'Auth_atom_ID_13', 'Auth_ambiguity_code_13', 'Auth_ambiguity_set_ID_13', 'Auth_entity_assembly_ID_14', 'Auth_entity_ID_14', 'Auth_asym_ID_14', 'Auth_seq_ID_14', 'Auth_comp_ID_14', 'Auth_atom_ID_14', 'Auth_ambiguity_code_14', 'Auth_ambiguity_set_ID_14', 'Auth_entity_assembly_ID_15', 'Auth_entity_ID_15', 'Auth_asym_ID_15', 'Auth_seq_ID_15', 'Auth_comp_ID_15', 'Auth_atom_ID_15', 'Auth_ambiguity_code_15', 'Auth_ambiguity_set_ID_15', 'Details', 'Sf_ID', 'Entry_ID', 'Spectral_peak_list_ID'],
                                          }
                              }

        # disallowed loop tags of spectral peak
        self.spectral_peak_disallowed_tags = {'nef': ['position_%s', 'position_uncertainty_%s', 'chain_code_%s', 'sequence_code_%s', 'residue_name_%s', 'atom_name_%s'],
                                              'nmr-star': ['Position_%s', 'Position_uncertainty_%s', 'Line_width_%s', 'Line_width_uncertainty_%s', 'Entity_assembly_ID_%s', 'Entity_ID_%s', 'Comp_index_ID_%s', 'Seq_ID_%s', 'Comp_ID_%s', 'Atom_ID_%s', 'Ambiguity_code_%s', 'Ambiguity_set_ID_%s', 'Auth_entity_assembly_ID_%s', 'Auth_entity_ID_%s', 'Auth_asym_ID_%s', 'Auth_seq_ID_%s', 'Auth_comp_ID_%s', 'Auth_atom_ID_%s', 'Auth_ambiguity_code_%s', 'Auth_ambiguity_set_ID_%s']
                                              }

        # saveframe tag prefixes (saveframe holder categories)
        self.sf_tag_prefixes = {'nef': {'entry_info': '_nef_nmr_meta_data',
                                        'poly_seq': '_nef_molecular_system',
                                        'chem_shift': '_nef_chemical_shift_list',
                                        'dist_restraint': '_nef_distance_restraint_list',
                                        'dihed_restraint': '_nef_dihedral_restraint_list',
                                        'rdc_restraint': '_nef_rdc_restraint_list',
                                        'spectral_peak': '_nef_nmr_spectrum'
                                        },
                                'nmr-star': {'entry_info': '_Entry',
                                             'poly_seq': '_Assembly',
                                             'chem_shift': '_Assigned_chem_shift_list',
                                             'dist_restraint': '_Gen_dist_constraint_list',
                                             'dihed_restraint': '_Torsion_angle_constraint_list',
                                             'rdc_restraint': '_RDC_constraint_list',
                                             'spectral_peak': '_Spectral_peak_list'
                                             }
                              }

        # saveframe tag items
        self.sf_tag_items = {'nef': {'entry_info': [{'name': 'sf_category', 'type': 'str', 'mandatory': True},
                                                    {'name': 'sf_framecode', 'type': 'str', 'mandatory': True},
                                                    {'name': 'format_name', 'type': 'str', 'mandatory': True},
                                                    {'name': 'format_version', 'type': 'str', 'mandatory': True},
                                                    {'name': 'program_name', 'type': 'str', 'mandatory': True},
                                                    {'name': 'program_version', 'type': 'str', 'mandatory': True},
                                                    {'name': 'creation_date', 'type': 'str', 'mandatory': True},
                                                    {'name': 'uuid', 'type': 'str', 'mandatory': True},
                                                    {'name': 'coordinate_file_name', 'type': 'str', 'mandatory': False}
                                                   ],
                                     'poly_seq': [{'name': 'sf_category', 'type': 'str', 'mandatory': True},
                                                  {'name': 'sf_framecode', 'type': 'str', 'mandatory': True}
                                                  ],
                                     'chem_shift': [{'name': 'sf_category', 'type': 'str', 'mandatory': True},
                                                    {'name': 'sf_framecode', 'type': 'str', 'mandatory': True}
                                                    ],
                                     'dist_restraint': [{'name': 'sf_category', 'type': 'str', 'mandatory': True},
                                                        {'name': 'sf_framecode', 'type': 'str', 'mandatory': True},
                                                        {'name': 'potential_type', 'type': 'enum', 'mandatory': True,
                                                         'enum': ('log-harmonic', 'parabolic', 'square-well-parabolic', 'square-well-parabolic-linear', 'upper-bound-parabolic', 'lower-bound-parabolic', 'upper-bound-parabolic-linear', 'lower-bound-parabolic-linear')},
                                                        {'name': 'restraint_origin', 'type': 'enum', 'mandatory': False,
                                                         'enum': ('NOE', 'NOE build-up', 'NOE not seen', 'ROE', 'ROE build-up', 'hydrogen bond', 'disulfide bond', 'paramagnetic relaxation', 'symmetry', 'general distance')}
                                                        ],
                                     'dihed_restraint': [{'name': 'sf_category', 'type': 'str', 'mandatory': True},
                                                         {'name': 'sf_framecode', 'type': 'str', 'mandatory': True},
                                                         {'name': 'potential_type', 'type': 'enum', 'mandatory': True,
                                                          'enum': ('log-harmonic', 'parabolic', 'square-well-parabolic', 'square-well-parabolic-linear', 'upper-bound-parabolic', 'lower-bound-parabolic', 'upper-bound-parabolic-linear', 'lower-bound-parabolic-linear')},
                                                         {'name': 'restraint_origin', 'type': 'enum', 'mandatory': False,
                                                          'enum': ('J-couplings', 'backbone chemical shifts')}
                                                         ],
                                     'rdc_restraint': [{'name': 'sf_category', 'type': 'str', 'mandatory': True},
                                                       {'name': 'sf_framecode', 'type': 'str', 'mandatory': True},
                                                       {'name': 'potential_type', 'type': 'enum', 'mandatory': True,
                                                        'enum': ('log-harmonic', 'parabolic', 'square-well-parabolic', 'square-well-parabolic-linear', 'upper-bound-parabolic', 'lower-bound-parabolic', 'upper-bound-parabolic-linear', 'lower-bound-parabolic-linear')},
                                                       {'name': 'restraint_origin', 'type': 'enum', 'mandatory': False,
                                                        'enum': ('RDC')},
                                                       {'name': 'tensor_magnitude', 'type': 'float', 'mandatory': False},
                                                       {'name': 'tensor_rhombicity', 'type': 'positive-float', 'mandatory': False},
                                                       {'name': 'tensor_chain_code', 'type': 'str', 'mandatory': False},
                                                       {'name': 'tensor_sequence_code', 'type': 'str', 'mandatory': False},
                                                       {'name': 'tensor_residue_name', 'type': 'str', 'mandatory': False}
                                                       ],
                                       'spectral_peak': [{'name': 'sf_category', 'type': 'str', 'mandatory': True},
                                                         {'name': 'sf_framecode', 'type': 'str', 'mandatory': True},
                                                         {'name': 'num_dimensions', 'type': 'enum-int', 'mandatory': True,
                                                          'enum': set(range(1, self.lim_num_dim)),
                                                          'enforce-enum': True},
                                                         {'name': 'chemical_shift_list', 'type': 'str', 'mandatory': False},
                                                         {'name': 'experiment_classification', 'type': 'str', 'mandatory': False},
                                                         {'name': 'experiment_type', 'type': 'str', 'mandatory': False}
                                                         ]
                                     },
                             'nmr-star': {'entry_info': [{'name': 'Sf_category', 'type': 'str', 'mandatory': True},
                                                         {'name': 'Sf_framecode', 'type': 'str', 'mandatory': True},
                                                         {'name': 'NMR_STAR_version', 'type': 'str', 'mandatory': True},
                                                         {'name': 'Source_data_format', 'type': 'str', 'mandatory': False},
                                                         {'name': 'Source_data_format_version', 'type': 'str', 'mandatory': False},
                                                         {'name': 'Generated_software_name', 'type': 'str', 'mandatory': False},
                                                         {'name': 'Generated_software_version', 'type': 'str', 'mandatory': False},
                                                         {'name': 'Generated_date', 'type': 'str', 'mandatory': False},
                                                         {'name': 'UUID', 'type': 'str', 'mandatory': False},
                                                         {'name': 'Related_coordinate_file_name', 'type': 'str', 'mandatory': False}
                                                         ],
                                          'poly_seq': [{'name': 'Sf_category', 'type': 'str', 'mandatory': True},
                                                       {'name': 'Sf_framecode', 'type': 'str', 'mandatory': True}
                                                       ],
                                          'chem_shift': [{'name': 'Sf_category', 'type': 'str', 'mandatory': True},
                                                         {'name': 'Sf_framecode', 'type': 'str', 'mandatory': True}
                                                         ],
                                          'dist_restraint': [{'name': 'Sf_category', 'type': 'str', 'mandatory': True},
                                                             {'name': 'Sf_framecode', 'type': 'str', 'mandatory': True},
                                                             {'name': 'Constraint_type', 'type': 'enum', 'mandatory': False,
                                                              'enum': ('NOE', 'NOE build-up', 'NOE not seen', 'ROE', 'ROE build-up', 'hydrogen bond', 'disulfide bond', 'paramagnetic relaxation', 'symmetry', 'general distance')},
                                                             {'name': 'Potential_type', 'type': 'enum', 'mandatory': False,
                                                              'enum': ('log-harmonic', 'parabolic', 'square-well-parabolic', 'square-well-parabolic-linear', 'upper-bound-parabolic', 'lower-bound-parabolic', 'upper-bound-parabolic-linear', 'lower-bound-parabolic-linear')}
                                                             ],
                                          'dihed_restraint': [{'name': 'Sf_category', 'type': 'str', 'mandatory': True},
                                                              {'name': 'Sf_framecode', 'type': 'str', 'mandatory': True},
                                                              {'name': 'Constraint_type', 'type': 'enum', 'mandatory': False,
                                                               'enum': ('J-couplings', 'backbone chemical shifts')},
                                                              {'name': 'Potential_type', 'type': 'enum', 'mandatory': False,
                                                               'enum': ('log-harmonic', 'parabolic', 'square-well-parabolic', 'square-well-parabolic-linear', 'upper-bound-parabolic', 'lower-bound-parabolic', 'upper-bound-parabolic-linear', 'lower-bound-parabolic-linear')}
                                                              ],
                                          'rdc_restraint': [{'name': 'Sf_category', 'type': 'str', 'mandatory': True},
                                                              {'name': 'Sf_framecode', 'type': 'str', 'mandatory': True},
                                                              {'name': 'Constraint_type', 'type': 'enum', 'mandatory': False,
                                                               'enum': ('RDC')},
                                                              {'name': 'Potential_type', 'type': 'enum', 'mandatory': False,
                                                               'enum': ('log-harmonic', 'parabolic', 'square-well-parabolic', 'square-well-parabolic-linear', 'upper-bound-parabolic', 'lower-bound-parabolic', 'upper-bound-parabolic-linear', 'lower-bound-parabolic-linear')},
                                                              {'name': 'Tensor_magnitude', 'type': 'float', 'mandatory': False},
                                                              {'name': 'Tensor_rhombicity', 'type': 'positive-float', 'mandatory': False},
                                                              {'name': 'Tensor_auth_asym_ID', 'type': 'str', 'mandatory': False},
                                                              {'name': 'Tensor_auth_seq_ID', 'type': 'str', 'mandatory': False},
                                                              {'name': 'Tensor_auth_comp_ID', 'type': 'str', 'mandatory': False}
                                                              ],
                                          'spectral_peak': [{'name': 'Sf_category', 'type': 'str', 'mandatory': True},
                                                            {'name': 'Sf_framecode', 'type': 'str', 'mandatory': True},
                                                            {'name': 'Experiment_class', 'type': 'str', 'mandatory': False},
                                                            {'name': 'Experiment_type', 'type': 'str', 'mandatory': False},
                                                            {'name': 'Number_of_spectral_dimensions', 'type': 'enum-int', 'mandatory': True,
                                                             'enum': set(range(1, self.lim_num_dim)),
                                                             'enforce-enum': True},
                                                            {'name': 'Chemical_shift_list', 'type': 'str', 'mandatory': True}
                                                            ]
                                          }
                             }

        # allowed saveframe tags
        self.sf_allowed_tags = {'nef': {'entry_info': ['sf_category', 'sf_framecode', 'format_name', 'format_version', 'program_name', 'program_version', 'creation_date', 'uuid', 'coordinate_file_name'],
                                        'poly_seq': ['sf_category', 'sf_framecode'],
                                        'chem_shift': ['sf_category', 'sf_framecode'],
                                        'dist_restraint': ['sf_category', 'sf_framecode', 'potential_type', 'restraint_origin'],
                                        'dihed_restraint': ['sf_category', 'sf_framecode', 'potential_type', 'restraint_origin'],
                                        'rdc_restraint': ['sf_category', 'sf_framecode', 'potential_type', 'restraint_origin', 'tensor_magnitude', 'tensor_rhombicity', 'tensor_chain_code', 'tensor_sequence_code', 'tensor_residue_name'],
                                        'spectral_peak': ['sf_category', 'sf_framecode', 'num_dimensions', 'chemical_shift_list', 'experiment_classification', 'experiment_type']
                                        },
                                'nmr-star': {'entry_info': ['Sf_category', 'Sf_framecode', 'Sf_ID', 'ID', 'Title', 'Type', 'Version_type', 'Submission_date', 'Accession_date', 'Last_release_date', 'Original_release_date', 'Origination', 'Format_name', 'NMR_STAR_version', 'Original_NMR_STAR_version', 'Experimental_method', 'Experimental_method_subtype', 'Source_data_format', 'Source_data_format_version', 'Generated_software_name', 'Generated_software_version', 'Generated_software_ID', 'Generated_software_label', 'Generated_date', 'DOI', 'UUID', 'Related_coordinate_file_name', 'Dep_release_code_coordinates', 'Dep_release_code_nmr_constraints', 'Dep_release_code_chemical_shifts', 'Dep_release_code_nmr_exptl', 'Dep_release_code_sequence', 'CASP_target', 'Details', 'Special_processing_instructions', 'Update_BMRB_accession_code', 'Replace_BMRB_accession_code', 'Update_PDB_accession_code', 'Replace_PDB_accession_code', 'PDB_coordinate_file_version', 'BMRB_update_details', 'PDB_update_details', 'Release_request', 'Release_date_request', 'Release_date_justification', 'Status_code', 'Recvd_deposit_form', 'Date_deposition_form', 'Recvd_coordinates', 'Date_coordinates', 'Recvd_nmr_constraints', 'Date_nmr_constraints', 'Recvd_chemical_shifts', 'Date_chemical_shifts', 'Recvd_manuscript', 'Date_manuscript', 'Recvd_author_approval', 'Date_author_approval', 'Recvd_initial_deposition_date', 'PDB_date_submitted', 'Author_release_status_code', 'Date_of_PDB_release', 'Date_hold_coordinates', 'Date_hold_nmr_constraints', 'Date_hold_chemical_shifts', 'PDB_deposit_site', 'PDB_process_site', 'BMRB_deposit_site', 'BMRB_process_site', 'BMRB_annotator', 'BMRB_internal_directory_name', 'RCSB_annotator', 'Author_approval_type', 'Assigned_BMRB_ID', 'Assigned_BMRB_deposition_code', 'Assigned_PDB_ID', 'Assigned_PDB_deposition_code', 'Assigned_restart_ID'],
                                             'poly_seq': ['Sf_category', 'Sf_framecode', 'Entry_ID', 'Sf_ID', 'ID', 'Name', 'BMRB_code', 'Number_of_components', 'Organic_ligands', 'Metal_ions', 'Non_standard_bonds', 'Ambiguous_conformational_states', 'Ambiguous_chem_comp_sites', 'Molecules_in_chemical_exchange', 'Paramagnetic', 'Thiol_state', 'Molecular_mass', 'Enzyme_commission_number', 'Details', 'DB_query_date', 'DB_query_revised_last_date'],
                                             'chem_shift': ['Sf_category', 'Sf_framecode', 'Entry_ID', 'Sf_ID', 'ID', 'Name', 'Data_file_name', 'Sample_condition_list_ID', 'Sample_condition_list_label', 'Chem_shift_reference_ID', 'Chem_shift_reference_label', 'Chem_shift_1H_err', 'Chem_shift_13C_err', 'Chem_shift_15N_err', 'Chem_shift_31P_err', 'Chem_shift_2H_err', 'Chem_shift_19F_err', 'Error_derivation_method', 'Details', 'Text_data_format', 'Text_data'],
                                             'dist_restraint': ['Sf_category', 'Sf_framecode', 'Entry_ID', 'Sf_ID', 'ID', 'Name', 'Data_file_name', 'Constraint_type', 'Constraint_file_ID', 'Potential_type', 'Block_ID', 'Details', 'Text_data_format', 'Text_data'],
                                             'dihed_restraint': ['Sf_category', 'Sf_framecode', 'Entry_ID', 'Sf_ID', 'ID', 'Name', 'Data_file_name', 'Constraint_file_ID', 'Potential_type', 'Constraint_type', 'Block_ID', 'Details', 'Text_data_format', 'Text_data'],
                                             'rdc_restraint': ['Sf_category', 'Sf_framecode', 'Entry_ID', 'Sf_ID', 'ID', 'Name', 'Data_file_name', 'Constraint_file_ID', 'Block_ID', 'Potential_type', 'Constraint_type', 'Tensor_entity_assembly_ID', 'Tensor_comp_index_ID', 'Tensor_seq_ID', 'Tensor_comp_ID', 'Tensor_auth_entity_assembly_ID', 'Tensor_auth_asym_ID', 'Tensor_auth_seq_ID', 'Tensor_auth_comp_ID', 'Dipolar_constraint_calib_method', 'Tensor_magnitude', 'Tensor_rhombicity', 'Mol_align_tensor_axial_sym_mol', 'Mol_align_tensor_rhombic_mol', 'General_order_param_int_motions', 'Bond_length_usage_flag', 'Assumed_H_N_bond_length', 'Assumed_H_C_bond_length', 'Assumed_C_N_bond_length', 'Data_file_format', 'Details', 'Text_data_format', 'Text_data'],
                                             'spectral_peak': ['Sf_category', 'Sf_framecode', 'Entry_ID', 'Sf_ID', 'ID', 'Name', 'Data_file_name', 'Sample_ID', 'Sample_label', 'Sample_condition_list_ID', 'Sample_condition_list_label', 'Experiment_ID', 'Experiment_name', 'Experiment_class', 'Experiment_type', 'Number_of_spectral_dimensions', 'Chemical_shift_list', 'Assigned_chem_shift_list_ID', 'Assigned_chem_shift_list_label', 'Details', 'Text_data_format', 'Text_data']
                                             }
                                }

        # auxiliary loop categories
        self.aux_lp_categories = {'nef': {'entry_info': [],
                                          'poly_seq':  [],
                                          'chem_shift': [],
                                          'dist_restraint': [],
                                          'dihed_restraint': [],
                                          'rdc_restraint': [],
                                          'spectral_peak': ['_nef_spectrum_dimension', '_nef_spectrum_dimension_transfer']
                                          },
                                  'nmr-star': {'entry_info': [],
                                               'poly_seq':  [],
                                               'chem_shift': [],
                                               'dist_restraint': [],
                                               'dihed_restraint': [],
                                               'rdc_restraint': [],
                                               'spectral_peak': ['_Spectral_dim', '_Spectral_dim_transfer']
                                               }
                                  }

        # linked loop categories
        self.linked_lp_categories = {'nef': {'entry_info': ['_nef_related_entries', '_nef_program_script', '_nef_run_history'],
                                             'poly_seq':  ['_nef_sequence', '_nef_covalent_links'],
                                             'chem_shift': ['_nef_chemical_shift'],
                                             'dist_restraint': ['_nef_distance_restraint'],
                                             'dihed_restraint': ['_nef_dihedral_restraint'],
                                             'rdc_restraint': ['_nef_rdc_restraint'],
                                             'spectral_peak': ['_nef_spectrum_dimension', '_nef_spectrum_dimension_transfer', '_nef_peak']
                                             },
                                  'nmr-star': {'entry_info': ['_Study_list', '_Entry_experimental_methods', '_Entry_author', '_SG_project', '_Entry_src', '_Struct_keywords', '_Data_set', '_Datum', '_Release', '_Related_entries', '_Matched_entries', '_Auxiliary_files', '_Citation', '_Assembly', '_Assembly_annotation_list', '_Assembly_subsystem', '_Entity', '_Entity_natural_src_list', '_Entity_natural_src', '_Entity_experimental_src_list', '_Chem_comp', '_Chem_comp_atom', '_Sample', '_Sample_condition_list', '_Entity_purity_list', '_Software', '_Method', '_Mass_spec', '_Mass_spectrometer_list', '_Mass_spec_ref_compd_set', '_Chromatographic_system', '_Chromatographic_column', '_Fluorescence_instrument', '_EMR_instrument', '_Xray_instrument', '_NMR_spectrometer', '_NMR_spectrometer_list', '_NMR_spectrometer_probe', '_Experiment_list', '_NMR_spec_expt', '_NMR_spectral_processing', '_MS_expt', '_MS_expt_param', '_MS_expt_software', '_Computer', '_Chem_shift_reference', '_Assigned_chem_shift_list', '_Chem_shifts_calc_type', '_Theoretical_chem_shift_list', '_Theoretical_chem_shift', '_Coupling_constant_list', '_Theoretical_coupling_constant_list', '_Spectral_peak_list', '_Resonance_linker_list', '_Resonance_assignment', '_Chem_shift_isotope_effect_list', '_Chem_shift_perturbation_list', '_Chem_shift_anisotropy', '_RDC_list', '_RDC_experiment', '_RDC_software', '_RDC', '_Dipolar_coupling_list', '_Dipolar_coupling_experiment', '_Dipolar_coupling_software', '_Dipolar_coupling', '_Spectral_density_list', '_Spectral_density_experiment', '_Spectral_density_software', '_Spectral_density', '_Other_data_type_list', '_Other_data_experiment', '_Other_data_software', '_Other_data', '_Chemical_rate_list', '_Chemical_rate_experiment', '_Chemical_rate_software', '_Chemical_rate', '_H_exch_rate_list', '_H_exch_rate_experiment', '_H_exch_rate_software', '_H_exch_rate', '_H_exch_protection_factor_list', '_H_exch_protection_fact_experiment', '_H_exch_protection_fact_software', '_H_exch_protection_factor', '_Homonucl_NOE_list', '_Homonucl_NOE_experiment', '_Homonucl_NOE_software', '_Homonucl_NOE', '_Heteronucl_NOE_list', '_Heteronucl_NOE_experiment', '_Heteronucl_NOE_software', '_Heteronucl_NOE', '_Theoretical_heteronucl_NOE_list', '_Theoretical_heteronucl_NOE_experiment', '_Theoretical_heteronucl_NOE_software', '_Theoretical_heteronucl_NOE', '_Heteronucl_T1_list', '_Heteronucl_T1_experiment', '_Heteronucl_T1_software', '_T1', '_Theoretical_heteronucl_T1_list', '_Theoretical_heteronucl_T1_experiment', '_Theoretical_heteronucl_T1_software', '_Theoretical_T1', '_Heteronucl_T1rho_list', '_Heteronucl_T1rho_experiment', '_Heteronucl_T1rho_software', '_T1rho', '_Heteronucl_T2_list', '_Heteronucl_T2_experiment', '_Heteronucl_T2_software', '_T2', '_Theoretical_heteronucl_T2_list', '_Theoretical_heteronucl_T2_experiment', '_Theoretical_heteronucl_T2_software', '_Theoretical_T2', '_Auto_relaxation_list', '_Auto_relaxation_experiment', '_Auto_relaxation_software', '_Auto_relaxation', '_Theoretical_auto_relaxation_list', '_Theoretical_auto_relaxation_experiment', '_Theoretical_auto_relaxation_software', '_Theoretical_auto_relaxation', '_Dipole_dipole_relax_list', '_Dipole_dipole_relax_experiment', '_Dipole_dipole_relax_software', '_Dipole_dipole_relax', '_Cross_correlation_DD_list', '_Cross_correlation_DD_experiment', '_Cross_correlation_DD_software', '_Cross_correlation_DD', '_Theoretical_cross_correlation_DD_list', '_Theoretical_cross_correlation_DD_experiment', '_Theoretical_cross_correlation_DD_software', '_Theoretical_cross_correlation_DD', '_Cross_correlation_D_CSA_list', '_Cross_correlation_D_CSA_experiment', '_Cross_correlation_D_CSA_software', '_Cross_correlation_D_CSA', '_Order_parameter_list', '_Order_parameter_experiment', '_Order_parameter_software', '_Order_param', '_PH_titration_list', '_PH_titration_experiment', '_PH_titration_software', '_PH_titr_result', '_PH_param_list', '_PH_param', '_D_H_fractionation_factor_list', '_D_H_fract_factor_experiment', '_D_H_fract_factor_software', '_D_H_fractionation_factor', '_Binding_value_list', '_Binding_experiment', '_Binding_software', '_Binding_result', '_Binding_partners', '_Binding_param_list', '_Binding_param', '_Deduced_secd_struct_list', '_Deduced_secd_struct_experiment', '_Deduced_secd_struct_software', '_Deduced_secd_struct_exptl', '_Deduced_secd_struct_feature', '_Deduced_H_bond_list', '_Deduced_H_bond_experiment', '_Deduced_H_bond_software', '_Deduced_H_bond', '_Conformer_stat_list', '_Conformer_stat_list_ens', '_Conformer_stat_list_rep', '_Conf_stats_software', '_Conformer_family_coord_set', '_Conformer_family_refinement', '_Conformer_family_software', '_Energetic_penalty_function', '_Conformer_family_coord_set_expt', '_Conf_family_coord_set_constr_list', '_Struct_image', '_Local_structure_quality', '_Model_type', '_Atom_site', '_Atom_sites_footnote', '_Representative_conformer', '_Rep_conf_refinement', '_Rep_conf_software', '_Terminal_residue', '_Rep_conf', '_Rep_coordinate_details', '_Constraint_stat_list', '_Constraint_stat_list_ens', '_Constraint_stat_list_rep', '_Constraint_stats_constr_list', '_Constraint_file', '_Force_constant_list', '_Force_constant_software', '_Force_constant', '_Angular_order_parameter_list', '_Angular_order_param', '_Tertiary_struct_element_list', '_Tertiary_struct_element_sel', '_Tertiary_struct', '_Structure_annotation', '_Struct_anno_software', '_Struct_classification', '_Struct_anno_char', '_Secondary_struct_list', '_Secondary_struct_sel', '_Secondary_struct', '_Bond_annotation_list', '_Bond_annotation', '_Bond_observed_conformer', '_Structure_interaction_list', '_Structure_interaction', '_Observed_conformer', '_Other_struct_feature_list', '_Other_struct_feature', '_Tensor_list', '_Interatomic_distance_list', '_Interatomic_dist', '_Gen_dist_constraint_list', '_Gen_dist_constraint_expt', '_Gen_dist_constraint_software', '_Gen_dist_constraint_software_param', '_Gen_dist_constraint', '_Gen_dist_constraint_comment_org', '_Gen_dist_constraint_parse_err', '_Gen_dist_constraint_parse_file', '_Gen_dist_constraint_conv_err', '_Distance_constraint_list', '_Distance_constraint_expt', '_Distance_constraint_software', '_Dist_constr_software_setting', '_Dist_constraint_tree', '_Dist_constraint', '_Dist_constraint_value', '_Dist_constraint_comment_org', '_Dist_constraint_parse_err', '_Dist_constraint_parse_file', '_Dist_constraint_conv_err', '_Floating_chirality_assign', '_Floating_chirality_software', '_Floating_chirality', '_Torsion_angle_constraint_list', '_Torsion_angle_constraints_expt', '_Torsion_angle_constraint_software', '_Karplus_equation', '_Torsion_angle_constraint', '_TA_constraint_comment_org', '_TA_constraint_parse_err', '_TA_constraint_parse_file', '_TA_constraint_conv_err', '_RDC_constraint_list', '_RDC_constraint_expt', '_RDC_constraint_software', '_RDC_constraint', '_RDC_constraint_comment_org', '_RDC_constraint_parse_err', '_RDC_constraint_parse_file', '_RDC_constraint_conv_err', '_J_three_bond_constraint_list', '_J_three_bond_constraint_expt', '_J_three_bond_constraint_software', '_J_three_bond_constraint', '_CA_CB_constraint_list', '_CA_CB_constraint_expt', '_CA_CB_constraint_software', '_CA_CB_constraint', '_H_chem_shift_constraint_list', '_H_chem_shift_constraint_expt', '_H_chem_shift_constraint_software', '_H_chem_shift_constraint', '_Peak_constraint_link_list', '_Peak_constraint_link', '_SAXS_constraint_list', '_SAXS_constraint_expt', '_SAXS_constraint_software', '_SAXS_constraint', '_Other_constraint_list', '_Other_constraint_expt', '_Other_constraint_software', '_Org_constr_file_comment', '_MZ_ratio_data_list', '_MZ_ratio_experiment', '_MZ_ratio_software', '_MZ_ratio_spectrum_param', '_MZ_precursor_ion', '_MZ_precursor_ion_annotation', '_MZ_product_ion', '_MZ_product_ion_annotation', '_MS_chromatogram_list', '_MS_chromatogram_experiment', '_MS_chromatogram_software', '_MS_chromatogram_param', '_MS_chromatogram_ion', '_MS_chrom_ion_annotation', '_Software_specific_info_list', '_Software_specific_info', '_Software_applied_list', '_Software_applied_methods', '_Software_applied_history', '_History'],
                                               'poly_seq':  ['_Assembly_type', '_Entity_assembly', '_Bond', '_Entity_deleted_atom', '_Struct_asym', '_Assembly_db_link', '_Assembly_common_name', '_Assembly_systematic_name', '_Assembly_interaction', '_Chem_comp_assembly', '_PDBX_poly_seq_scheme', '_PDBX_nonpoly_scheme', '_Atom_type', '_Atom', '_Assembly_bio_function', '_Angle', '_Torsion_angle', '_Assembly_segment', '_Assembly_segment_description', '_Assembly_keyword', '_Assembly_citation', '_Author_annotation', '_Sample_component', '_Chemical_rate', '_Auto_relaxation', '_Theoretical_auto_relaxation', '_Binding_result', '_Binding_partners', '_Struct_anno_char' ],
                                               'chem_shift': ['_Chem_shift_experiment', '_Systematic_chem_shift_offset', '_Chem_shift_software', '_Atom_chem_shift', '_Ambiguous_atom_chem_shift', '_Spectral_peak_list', '_Assigned_peak_chem_shift', '_Assigned_spectral_transition'],
                                               'dist_restraint': ['_Gen_dist_constraint_expt', '_Gen_dist_constraint_software', '_Gen_dist_constraint_software_param', '_Gen_dist_constraint', '_Gen_dist_constraint_comment_org', '_Gen_dist_constraint_parse_err', '_Gen_dist_constraint_parse_file', '_Gen_dist_constraint_conv_err'],
                                               'dihed_restraint': ['_Torsion_angle_constraints_expt', '_Torsion_angle_constraint_software', '_Karplus_equation', '_Torsion_angle_constraint', '_TA_constraint_comment_org', '_TA_constraint_parse_err', '_TA_constraint_parse_file', '_TA_constraint_conv_err'],
                                               'rdc_restraint': ['_RDC_constraint_expt', '_RDC_constraint_software', '_RDC_constraint', '_RDC_constraint_comment_org', '_RDC_constraint_parse_err', '_RDC_constraint_parse_file', '_RDC_constraint_conv_err'],
                                               'spectral_peak': ['_Spectral_dim', '_Spectral_dim_transfer', '_Spectral_peak_software', '_Peak', '_Peak_general_char', '_Peak_char', '_Assigned_peak_chem_shift', '_Peak_row_format', '_Spectral_transition', '_Spectral_transition_general_char', '_Spectral_transition_char', '_Assigned_spectral_transition', '_Gen_dist_constraint', '_Dist_constraint_value']
                                               }
                                  }

        # auxiliary loop key items
        self.aux_key_items = {'nef': {'entry_info': None,
                                      'poly_seq':  None,
                                      'chem_shift': None,
                                      'dist_restraint': None,
                                      'dihed_restraint': None,
                                      'rdc_restraint': None,
                                      'spectral_peak': {
                                          '_nef_spectrum_dimension': [{'name': 'dimension_id', 'type': 'index-int'}
                                                                      ],
                                          '_nef_spectrum_dimension_transfer': [{'name': 'dimension_1', 'type': 'positive-int'},
                                                                               {'name': 'dimension_2', 'type': 'positive-int'},
                                                                               ]
                                          }
                                      },
                              'nmr-star': {'entry_info': None,
                                           'poly_seq':  None,
                                           'chem_shift': None,
                                           'dist_restraint': None,
                                           'dihed_restraint': None,
                                           'rdc_restraint': None,
                                           'spectral_peak': {
                                               '_Spectral_dim': [{'name': 'ID', 'type': 'index-int'}
                                                                 ],
                                               '_Spectral_dim_transfer': [{'name': 'Spectral_dim_ID_1', 'type': 'positive-int'},
                                                                          {'name': 'Spectral_dim_ID_2', 'type': 'positive-int'},
                                                                          ]
                                               }
                                           }
                                  }

        # auxiliary loop data items
        self.aux_data_items = {'nef': {'entry_info': None,
                                       'poly_seq':  None,
                                       'chem_shift': None,
                                       'dist_restraint': None,
                                       'dihed_restraint': None,
                                       'rdc_restraint': None,
                                       'spectral_peak': {
                                           '_nef_spectrum_dimension': [{'name': 'axis_unit', 'type': 'enum', 'mandatory': True,
                                                                        'enum': ('ppm', 'Hz'),
                                                                        'enforce-enum': True},
                                                                       {'name': 'axis_code', 'type': 'str', 'mandatory': True},
                                                                       {'name': 'spectrometer_frequency', 'type': 'positive-float', 'mandatory': False,
                                                                        'enforce-non-zero': True},
                                                                       {'name': 'spectral_width', 'type': 'positive-float', 'mandatory': False,
                                                                        'enforce-non-zero': True},
                                                                       {'name': 'value_first_point', 'type': 'float', 'mandatory': False},
                                                                       {'name': 'folding', 'type': 'enum', 'mandatory': False,
                                                                        'enum': ('circular', 'mirror', 'none')},
                                                                       {'name': 'absolute_peak_positions', 'type': 'bool', 'mandatory': False},
                                                                       {'name': 'is_acquisition', 'type': 'bool', 'mandatory': False},
                                                                       ],
                                           '_nef_spectrum_dimension_transfer': [{'name': 'transfer_type', 'type': 'enum', 'mandatory': True,
                                                                                 'enum': ('onebond', 'jcoupling', 'jmultibond', 'relayed', 'relayed-alternate', 'through-space'),
                                                                                 'enforce-enum': True},
                                                                                {'name': 'is_indirect', 'type': 'bool', 'mandatory': False}
                                                                                ]
                                           }
                                       },
                                  'nmr-star': {'entry_info': None,
                                               'poly_seq':  None,
                                               'chem_shift': None,
                                               'dist_restraint': None,
                                               'dihed_restraint': None,
                                               'rdc_restraint': None,
                                               'spectral_peak': {
                                                   '_Spectral_dim': [{'name': 'Axis_code', 'type': 'str', 'mandatory': True},
                                                                     {'name': 'Spectrometer_frequency', 'type': 'positive-float', 'mandatory': False,
                                                                      'enforce-non-zero': True},
                                                                     {'name': 'Under_sampling_type', 'type': 'enum', 'mandatory': False,
                                                                      'enum': ('aliased', 'folded', 'not observed')},
                                                                     {'name': 'Sweep_width', 'type': 'positive-float', 'mandatory': False,
                                                                      'enforce-non-zero': True},
                                                                     {'name': 'Sweep_width_units', 'type': 'enum', 'mandatory': True,
                                                                      'enum': ('ppm', 'Hz'),
                                                                      'enforce-enum': True},
                                                                     {'name': 'Value_first_point', 'type': 'float', 'mandatory': False},
                                                                     {'name': 'Absolute_peak_positions', 'type': 'bool', 'mandatory': False},
                                                                     {'name': 'Acquisition', 'type': 'bool', 'mandatory': False},
                                                                     ],
                                                   '_Spectral_dim_transfer': [{'name': 'Indirect', 'type': 'bool', 'mandatory': False},
                                                                              {'name': 'Type', 'type': 'enum', 'mandatory': True,
                                                                               'enum': ('onebond', 'jcoupling', 'jmultibond', 'relayed', 'relayed-alternate', 'through-space'),
                                                                               'enforce-enum': True}
                                                                              ]
                                                   }
                                               }
                                  }

        # allowed auxiliary loop tags
        self.aux_allowed_tags = {'nef': {'entry_info': None,
                                         'poly_seq':  None,
                                         'chem_shift': None,
                                         'dist_restraint': None,
                                         'dihed_restraint': None,
                                         'rdc_restraint': None,
                                         'spectral_peak': {
                                             '_nef_spectrum_dimension': ['dimension_id', 'axis_unit', 'axis_code', 'spectrometer_frequency', 'spectral_width', 'value_first_point', 'folding', 'absolute_peak_positions', 'is_acquisition'],
                                             '_nef_spectrum_dimension_transfer': ['dimension_1', 'dimension_2', 'transfer_type', 'is_indirect']
                                             }
                                         },
                                 'nmr-star': {'entry_info': None,
                                              'poly_seq':  None,
                                              'chem_shift': None,
                                              'dist_restraint': None,
                                              'dihed_restraint': None,
                                              'rdc_restraint': None,
                                              'spectral_peak': {
                                                  '_Spectral_dim': ['ID', 'Axis_code', 'Spectrometer_frequency', 'Atom_type', 'Atom_isotope_number', 'Spectral_region', 'Magnetization_linkage_ID', 'Under_sampling_type', 'Sweep_width', 'Sweep_width_units', 'Value_first_point', 'Absolute_peak_positions', 'Acquisition', 'Center_frequency_offset', 'Encoding_code', 'Encoded_reduced_dimension_ID', 'Sf_ID', 'Entry_ID', 'Spectral_peak_list_ID'],
                                                  '_Spectral_dim_transfer': ['Spectral_dim_ID_1', 'Spectral_dim_ID_2', 'Indirect', 'Type', 'Sf_ID', 'Entry_ID', 'Spectral_peak_list_ID']
                                                  }
                                              }
                                  }

        # item name in cs loop
        self.item_names_in_cs_loop = {'nef': {'chain_id': 'chain_code',
                                              'seq_id': 'sequence_code',
                                              'comp_id': 'residue_name',
                                              'atom_id': 'atom_name',
                                              'value': 'value',
                                              'error': 'value_uncertainty',
                                              'atom_type': 'element',
                                              'isotope_number': 'isotope_number'
                                              },
                                      'nmr-star': {'chain_id': 'Entity_assembly_ID',
                                                   'seq_id': 'Comp_index_ID',
                                                   'comp_id': 'Comp_ID',
                                                   'atom_id': 'Atom_ID',
                                                   'value': 'Val',
                                                   'error': 'Val_err',
                                                   'atom_type': 'Atom_type',
                                                   'isotope_number': 'Atom_isotope_number'
                                                   }
                                      }

        # item name in spectral peak loop
        self.item_names_in_pk_loop = {'nef': {'chain_id': 'chain_code_%s',
                                              'seq_id': 'sequence_code_%s',
                                              'comp_id': 'residue_name_%s',
                                              'atom_id': 'atom_name_%s',
                                              'position': 'position_%s'
                                              },
                                      'nmr-star': {'chain_id': 'Entity_assembly_ID_%s',
                                                   'seq_id': 'Comp_index_ID_%s',
                                                   'comp_id': 'Comp_ID_%s',
                                                   'atom_id': 'Atom_ID_%s',
                                                   'position': 'Position_%s'
                                                   }
                                      }

        # item name in distance restraint loop
        self.item_names_in_ds_loop = {'nef': {'combination_id': 'restraint_combination_id',
                                              'chain_id_1': 'chain_code_1',
                                              'seq_id_1': 'sequence_code_1',
                                              'comp_id_1': 'residue_name_1',
                                              'atom_id_1': 'atom_name_1',
                                              'chain_id_2': 'chain_code_2',
                                              'seq_id_2': 'sequence_code_2',
                                              'comp_id_2': 'residue_name_2',
                                              'atom_id_2': 'atom_name_2',
                                              'target_value': 'target_value',
                                              'lower_linear_limit': 'lower_linear_limit',
                                              'upper_linear_limit': 'upper_linear_limit',
                                              'lower_limit': 'lower_limit',
                                              'upper_limit': 'upper_limit'
                                              },
                                      'nmr-star': {'combination_id': 'Combination_ID',
                                                   'chain_id_1': 'Entity_assembly_ID_1',
                                                   'seq_id_1': 'Comp_index_ID_1',
                                                   'comp_id_1': 'Comp_ID_1',
                                                   'atom_id_1': 'Atom_ID_1',
                                                   'chain_id_2': 'Entity_assembly_ID_2',
                                                   'seq_id_2': 'Comp_index_ID_2',
                                                   'comp_id_2': 'Comp_ID_2',
                                                   'atom_id_2': 'Atom_ID_2',
                                                   'target_value': 'Target_val',
                                                   'lower_linear_limit': 'Lower_linear_limit',
                                                   'upper_linear_limit': 'Upper_linear_limit',
                                                   'lower_limit': 'Distance_lower_bound_val',
                                                   'upper_limit': 'Distance_upper_bound_val'
                                                   }
                                      }

        # item name in dihedral restraint loop
        self.item_names_in_dh_loop = {'nef': {'chain_id_1': 'chain_code_1',
                                              'seq_id_1': 'sequence_code_1',
                                              'comp_id_1': 'residue_name_1',
                                              'atom_id_1': 'atom_name_1',
                                              'chain_id_2': 'chain_code_2',
                                              'seq_id_2': 'sequence_code_2',
                                              'comp_id_2': 'residue_name_2',
                                              'atom_id_2': 'atom_name_2',
                                              'chain_id_3': 'chain_code_3',
                                              'seq_id_3': 'sequence_code_3',
                                              'comp_id_3': 'residue_name_3',
                                              'atom_id_3': 'atom_name_3',
                                              'chain_id_4': 'chain_code_4',
                                              'seq_id_4': 'sequence_code_4',
                                              'comp_id_4': 'residue_name_4',
                                              'atom_id_4': 'atom_name_4',
                                              'angle_type': 'name'
                                              },
                                      'nmr-star': {'chain_id_1': 'Entity_assembly_ID_1',
                                                   'seq_id_1': 'Comp_index_ID_1',
                                                   'comp_id_1': 'Comp_ID_1',
                                                   'atom_id_1': 'Atom_ID_1',
                                                   'chain_id_2': 'Entity_assembly_ID_2',
                                                   'seq_id_2': 'Comp_index_ID_2',
                                                   'comp_id_2': 'Comp_ID_2',
                                                   'atom_id_2': 'Atom_ID_2',
                                                   'chain_id_3': 'Entity_assembly_ID_3',
                                                   'seq_id_3': 'Comp_index_ID_3',
                                                   'comp_id_3': 'Comp_ID_3',
                                                   'atom_id_3': 'Atom_ID_3',
                                                   'chain_id_4': 'Entity_assembly_ID_4',
                                                   'seq_id_4': 'Comp_index_ID_4',
                                                   'comp_id_4': 'Comp_ID_4',
                                                   'atom_id_4': 'Atom_ID_4',
                                                   'angle_type': 'Torsion_angle_name',
                                                   }
                                      }

        # item name in rdc restraint loop
        self.item_names_in_rdc_loop = {'nef': {'chain_id_1': 'chain_code_1',
                                               'seq_id_1': 'sequence_code_1',
                                               'comp_id_1': 'residue_name_1',
                                               'atom_id_1': 'atom_name_1',
                                               'chain_id_2': 'chain_code_2',
                                               'seq_id_2': 'sequence_code_2',
                                               'comp_id_2': 'residue_name_2',
                                               'atom_id_2': 'atom_name_2'
                                               },
                                       'nmr-star': {'chain_id_1': 'Entity_assembly_ID_1',
                                                    'seq_id_1': 'Comp_index_ID_1',
                                                    'comp_id_1': 'Comp_ID_1',
                                                    'atom_id_1': 'Atom_ID_1',
                                                    'chain_id_2': 'Entity_assembly_ID_2',
                                                    'seq_id_2': 'Comp_index_ID_2',
                                                    'comp_id_2': 'Comp_ID_2',
                                                    'atom_id_2': 'Atom_ID_2'
                                                    }
                                       }

        # saveframe tag name for chemical shift list in spectral peak
        self.cs_list_sf_tag_name = {'nef': 'chemical_shift_list',
                                    'nmr-star': 'Chemical_shift_list'
                                    }

        # taken from wwpdb.utils.align.SequenceReferenceData.py
        self.monDict3 = {'ALA': 'A',
                         'ARG': 'R',
                         'ASN': 'N',
                         'ASP': 'D',
                         'ASX': 'B',
                         'CYS': 'C',
                         'GLN': 'Q',
                         'GLU': 'E',
                         'GLX': 'Z',
                         'GLY': 'G',
                         'HIS': 'H',
                         'ILE': 'I',
                         'LEU': 'L',
                         'LYS': 'K',
                         'MET': 'M',
                         'PHE': 'F',
                         'PRO': 'P',
                         'SER': 'S',
                         'THR': 'T',
                         'TRP': 'W',
                         'TYR': 'Y',
                         'VAL': 'V',
                         'DA': 'A',
                         'DC': 'C',
                         'DG': 'G',
                         'DT': 'T',
                         'DU': 'U',
                         'DI': 'I',
                         'A': 'A',
                         'C': 'C',
                         'G': 'G',
                         'I': 'I',
                         'T': 'T',
                         'U': 'U'
                         }

        # main contents of loops
        self.__lp_data = {'poly_seq': [],
                          'chem_shift': [],
                          'dist_restraint': [],
                          'dihed_restraint': [],
                          'rdc_restraint': [],
                          'spectral_peak': []
                          }

        # auxiliary contents of loops
        self.__aux_data = {'poly_seq': [],
                           'chem_shift': [],
                           'dist_restraint': [],
                           'dihed_restraint': [],
                           'rdc_restraint': [],
                           'spectral_peak': []
                           }

        # Pairwise align
        self.__pA = PairwiseAlign()
        self.__pA.setVerbose(self.__verbose)

        # CCD accessing utility
        self.__cI = ConfigInfo(getSiteId())
        self.__ccCvsPath = self.__cI.get('SITE_CC_CVS_PATH')

        self.__ccR = ChemCompReader(self.__verbose, self.__lfh)
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

        # CIF reader
        self.__cR = CifReader(self.__verbose, self.__lfh)

    def setVerbose(self, flag):
        """ Set verbose mode.
        """

        self.__verbose = flag

    def setSource(self, fPath):
        """ Set primary source file path.
        """

        if os.access(fPath, os.F_OK):
            self.__srcPath = os.path.abspath(fPath)

        else:
            logging.error("+NmrDpUtility.setSource() ++ Error  - Could not access to file path %s." % fPath)
            raise IOError("+NmrDpUtility.setSource() ++ Error  - Could not access to file path %s." % fPath)

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
                logging.error("+NmrDpUtility.addInput() ++ Error  - Unknown input type %s." % type)
                raise ValueError("+NmrDpUtility.addInput() ++ Error  - Unknown input type %s." % type)

                return False

            return True

        except Exception as e:

            logging.error("+NmrDpUtility.addInput() ++ Error  - %s" % str(e))
            raise ValueError("+NmrDpUtility.addInput() ++ Error  - %s" % str(e))

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
                logging.error("+NmrDpUtility.addOutput() ++ Error  - Unknown output type %s." % type)
                raise ValueError("+NmrDpUtility.addOutput() ++ Error  - Unknown output type %s." % type)

                return False

            return True

        except Exception as e:

            logging.error("+NmrDpUtility.addOutput() ++ Error  - %s" % str(e))
            raise ValueError("+NmrDpUtility.addOutput() ++ Error  - %s" % str(e))

            return False

    def op(self, op):
        """ Perform a series of tasks for a given workflow operation.
        """

        if self.__srcPath is None:
            logging.error("+NmrDpUtility.op() ++ Error  - No input provided for workflow operation %s." % op)
            raise ValueError("+NmrDpUtility.op() ++ Error  - No input provided for workflow operation %s." % op)

        if self.__verbose:
            self.__lfh.write("+NmrDpUtility.op() starting op %s\n" % op)

        if not op in self.__workFlowOps:
            logging.error("+NmrDpUtility.op() ++ Error  - Unknown workflow operation %s." % op)
            raise KeyError("+NmrDpUtility.op() ++ Error  - Unknown workflow operation %s." % op)

        self.__op = op

        if op.endswith('consistency-check'):

            for task in self.__procTasksDict['consistency-check']:

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.op() starting op %s - task %s\n" % (op, task.__name__))

                if not task():
                    pass

        elif op.endswith('deposit'):

            for task in self.__procTasksDict['deposit']:

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.op() starting op %s - task %s\n" % (op, task.__name__))

                if not task():
                    pass

        # run workflow operation specific tasks
        if op in self.__procTasksDict:

            for task in self.__procTasksDict[op]:

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.op() starting op %s - task %s\n" % (op, task.__name__))

                if not task():
                    if task == self.__translateNef2Str:
                        break

        self.__dumpDpReport()

        return not self.report.isError()

    def __dumpDpReport(self):
        """ Dump current NMR data processing report.
        """

        if self.report_prev != None:
            self.report.inheritFormatIssueErrors(self.report_prev)

            if not self.report_prev.warning.get() is None:
                self.report.setCorrectedWarning(self.report_prev)

        return self.report.writeJson(self.__logPath)

    def __initializeDpReport(self, srcPath=None):
        """ Initialize NMR data processing report.
        """

        if srcPath is None:
            srcPath = self.__srcPath

        self.report = NmrDpReport()

        # set primary input source as NMR unified data
        input_source = self.report.input_sources[0]

        file_type = 'nef' if 'nef' in self.__op else 'nmr-star'
        content_type = self.content_type[file_type]

        input_source.setItemValue('file_name', os.path.basename(srcPath))
        input_source.setItemValue('file_type', file_type)
        input_source.setItemValue('content_type', content_type)

        self.__testDiamagnetism()

        return input_source is not None

    def __testDiamagnetism(self):
        """ Test diamagnetism of molecular assembly.
        """

        if self.__cifPath is None:
            self.__setCoordFilePath()

        if self.__cifPath is None:
            return

            try:

                if not self.__cR.parse():
                    return

                comp_comp_list = cR.getDictList('chem_comp')

                non_std_comp_ids = [i['id'] for i in comp_comp_list if i['mon_nstd_flag'] != 'y']

                if len(non_std_comp_ids) == 0:
                    return

                for comp_id in non_std_comp_ids:

                    self.__updateChemCompDict(comp_id)

                    if self.__last_comp_id_test: # matches with comp_id in CCD
                        ref_elems = set([a[self.__cca_type_symbol] for a in self.__last_chem_comp_atoms if a[self.__cca_leaving_atom_flag] != 'Y'])

                        for elem in ref_elems:
                            if elem in self.paramag_elems or elem in self.ferromag_elems:
                                self.report.setDiamagnetic(False)
                                break

            except:
                pass

    def __updateChemCompDict(self, comp_id):
        """ Update CCD information for a given comp_id.
            @return: True for successfully update CCD information or False for the case a given comp_id does not exist in CCD
        """

        comp_id = comp_id.upper()

        if comp_id != self.__last_comp_id:
            self.__last_comp_id_test = self.__ccR.setCompId(comp_id)
            self.__last_comp_id = comp_id

            if self.__last_comp_id_test:
                self.__last_chem_comp_dict = self.__ccR.getChemCompDict()
                self.__last_chem_comp_atoms = self.__ccR.getAtomList()
                self.__last_chem_comp_bonds = self.__ccR.getBonds()

        return self.__last_comp_id_test

    def __validateInputSource(self, srcPath=None):
        """ Validate NMR unified data as primary input source.
        """

        if srcPath is None:
            srcPath = self.__srcPath

        is_valid, json_dumps = self.__nefT.validate_file(srcPath, 'A') # 'A' for NMR unified data, 'S' for assigned chemical shifts, 'R' for restraints.

        message = json.loads(json_dumps)

        _file_type = message['file_type'] # nef/nmr-star/unknown

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        if is_valid:

            if _file_type != file_type:

                err = "%s was selected as %s file, but recognized as %s file." % (file_name, self.readable_file_type[file_type], self.readable_file_type[_file_type])

                if len(message['error']) > 0:
                    for err_message in message['error']:
                        if not 'No such file or directory' in err_message:
                            err += ' ' + err_message

                self.report.error.appendDescription('format_issue', {'file_name': file_name, 'description': err})
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__validateInputSource() ++ Error  - %s\n" % err)

                return False

            is_done, self.__star_data_type, self.__star_data = self.__nefT.read_input_file(srcPath) # NEFTranslator.validate_file() generates this object internally, but not re-used.

            self.__rescueFormerNef()

            return True

        else:

            err = "%s is invalid %s file." % (file_name, self.readable_file_type[file_type])

            if len(message['error']) > 0:
                for err_message in message['error']:
                    if not 'No such file or directory' in err_message:
                        err += ' ' + err_message

            self.report.error.appendDescription('format_issue', {'file_name': file_name, 'description': err})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__validateInputSource() ++ Error  - %s\n" % err)

            return False

    def __rescueFormerNef(self):
        """ Rescue former NEF version prior to 1.0.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        if file_type != 'nef':
            return True

        content_subtype = 'entry_info'

        sf_category = self.sf_categories[file_type][content_subtype]

        for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

            version = sf_data.get_tag('format_version')[0]

            if not version.startswith('0.'):
                return True

            sf_data.format_version = '1.0'

        for content_subtype in self.nmr_content_subtypes:

            sf_category = self.sf_categories[file_type][content_subtype]
            lp_category = self.lp_categories[file_type][content_subtype]

            for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

                lp_data = sf_data.get_loop_by_category(lp_category)

                index_tag = self.index_tags[file_type][content_subtype]

                if not index_tag is None:

                    try:
                        tag_pos = next(lp_data.tags.index(tag) for tag in lp_data.tags if tag == 'ordinal')
                        lp_data.tags[tag_pos] = 'index'
                    except StopIteration:
                        pass

                    try:
                        tag_pos = next(lp_data.tags.index(tag) for tag in lp_data.tags if tag == 'index_id')
                        lp_data.tags[tag_pos] = 'index'
                    except StopIteration:
                        pass

                if content_subtype == 'poly_seq':

                    try:
                        tag_pos = next(lp_data.tags.index(tag) for tag in lp_data.tags if tag == 'residue_type')
                        lp_data.tags[tag_pos] = 'residue_name'
                    except StopIteration:
                        pass

                    if not 'index' in lp_data.tags:

                        id = 1

                        for i in lp_data:
                            i.append(id)
                            id += 1

                        lp_data.add_tag(lp_category + '.index')

                if content_subtype == 'chem_shift':

                    try:
                        next(tag for tag in sf_data.tags if tag[0] == 'atom_chemical_shift_units')
                        sf_data.delete_tag('atom_chemical_shift_units')
                    except StopIteration:
                        pass

                    try:
                        tag_pos = next(lp_data.tags.index(tag) for tag in lp_data.tags if tag == 'residue_type')
                        lp_data.tags[tag_pos] = 'residue_name'
                    except StopIteration:
                        pass

                    if not 'element' in lp_data.tags:

                        try:
                            atom_name_col = lp_data.tags.index('atom_name')

                            for i in lp_data:
                                i.append(i[atom_name_col][0])

                            lp_data.add_tag(lp_category + '.element')

                        except ValueError:
                            pass

                    if not 'isotope_number' in lp_data.tags:

                        try:
                            atom_name_col = lp_data.tags.index('atom_name')

                            for i in lp_data:
                                i.append(self.atom_isotopes[i[atom_name_col][0]][0])

                            lp_data.add_tag(lp_category + '.isotope_number')

                        except ValueError:
                            pass

                if content_subtype == 'rdc_restraint':

                    try:
                        tag = next(tag for tag in sf_data.tags if tag[0] == 'tensor_residue_type')
                        sf_data.add_tag(sf_category + '.tensor_residue_name', tag[1])
                        sf_data.delete_tag('tensor_residue_type')
                    except StopIteration:
                        pass

                if content_subtype == 'dist_restraint' or content_subtype == 'rdc_restraint':
                    max_dim = 3

                elif content_subtype == 'dihed_restraint':
                    max_dim = 5

                elif content_subtype == 'spectral_peak':

                    try:

                        _num_dim = sf_data.get_tag(self.num_dim_items[file_type])[0]
                        num_dim = int(_num_dim)

                        if not num_dim in range(1, self.lim_num_dim):
                            raise ValueError()

                    except ValueError: # raised error already at __testIndexConsistency()
                        continue

                    max_dim = num_dim + 1

                else:
                    continue

                for j in range(1, max_dim):

                    _residue_type = 'residue_type_' + str(j)

                    try:
                        tag_pos = next(lp_data.tags.index(tag) for tag in lp_data.tags if tag == _residue_type)
                        lp_data.tags[tag_pos] = 'residue_name_' + str(j)
                    except StopIteration:
                        pass

        return True

    def __detectContentSubType(self):
        """ Detect content subtypes.
        """

        if self.report.isError():
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        self.__sf_category_list, self.__lp_category_list = self.__nefT.get_data_content(self.__star_data, self.__star_data_type)

        for sf_category in self.__sf_category_list:
            if not sf_category in self.sf_categories[file_type].values():

                warn = "Unsupported %s saveframe category exists in %s file." % (sf_category, file_name)

                self.report.warning.appendDescription('skipped_sf_category', {'file_name': file_name, 'description': warn})
                self.report.setWarning()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__detectContentSubType() ++ Warning  - %s\n" % warn)

        # initialize loop counter
        lp_counts = {t:0 for t in self.nmr_content_subtypes}

        # increment loop counter of each content subtype
        for lp_category in self.__lp_category_list:
            if lp_category in self.lp_categories[file_type].values():
                lp_counts[[k for k, v in self.lp_categories[file_type].items() if v == lp_category][0]] += 1

        content_subtypes = {k:lp_counts[k] for k in lp_counts if lp_counts[k] > 0}

        input_source.setItemValue('content_subtype', content_subtypes)

        content_subtype = 'poly_seq'

        if lp_counts[content_subtype] == 0:

            sf_category = self.sf_categories[file_type][content_subtype]

            warn = "Saveframe category %s did not exist in %s file." % (sf_category, file_name)

            self.report.warning.appendDescription('missing_saveframe', {'file_name': file_name, 'description': warn})
            self.report.setWarning()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__detectContentSubType() ++ Warning  - %s\n" % warn)

        elif lp_counts[content_subtype] > 1:

            sf_category = self.sf_categories[file_type][content_subtype]

            err = "Unexpectedly, multiple saveframes belonging to category %s were found in %s file." % (sf_category, file_name)

            self.report.error.appendDescription('format_issue', {'file_name': file_name, 'description': err})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__detectContentSubType() ++ Error  - %s\n" % err)

        content_subtype = 'chem_shift'

        if lp_counts[content_subtype] == 0:

            sf_category = self.sf_categories[file_type][content_subtype]
            lp_category = self.lp_categories[file_type][content_subtype]

            err = "Assigned chemical shifts are mandatory for PDB/BMRB deposition. Saveframe category %s and loop category %s were not found in %s file." % (sf_category, lp_category, file_name)

            self.report.error.appendDescription('missing_mandatory_content', {'file_name': file_name, 'description': err})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__detectContentSubType() ++ Error  - %s\n" % err)

        content_subtype = 'dist_restraint'

        if lp_counts[content_subtype] == 0:

            sf_category = self.sf_categories[file_type][content_subtype]
            lp_category = self.lp_categories[file_type][content_subtype]

            err = "Distance restraints are mandatory for PDB/BMRB deposition. Saveframe category %s and loop category %s were not found in %s file." % (sf_category, lp_category, file_name)

            self.report.error.appendDescription('missing_mandatory_content', {'file_name': file_name, 'description': err})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__detectContentSubType() ++ Error  - %s\n" % err)

        content_subtype = 'spectral_peak'

        if lp_counts[content_subtype] == 0:

            sf_category = self.sf_categories[file_type][content_subtype]
            lp_category = self.lp_categories[file_type][content_subtype]

            warn = "Spectral peak list is missing. The wwPDB NMR Validation Task Force strongly encourages the submission of spectral peak lists, in particular those generated from NOESY spectra. Saveframe category %s and loop category %s were not found in %s file." % (sf_category, lp_category, file_name)

            self.report.warning.appendDescription('missing_content', {'file_name': file_name, 'description': warn})
            self.report.setWarning()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__detectContentSubType() ++ Warning  - %s\n" % warn)

        return not self.report.isError()

    def __getPolymerSequence(self, sf_data, content_subtype):
        """ Wrapper function to retrieve polymer sequence from loop of a specified saveframe and content subtype via NEFTranslator.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        if file_type == 'nef':
            return self.__nefT.get_nef_seq(sf_data, lp_category=self.lp_categories[file_type][content_subtype], allow_empty=(content_subtype == 'spectral_peak'))
        else:
            return self.__nefT.get_star_seq(sf_data, lp_category=self.lp_categories[file_type][content_subtype], allow_empty=(content_subtype == 'spectral_peak'))

    def __extractPolymerSequence(self):
        """ Extract reference polymer sequence.
        """

        if self.report.isError():
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        content_subtype = 'poly_seq'

        if not content_subtype in input_source_dic['content_subtype']:
            return True

        sf_category = self.sf_categories[file_type][content_subtype]
        lp_category = self.lp_categories[file_type][content_subtype]

        sf_data = self.__star_data.get_saveframes_by_category(sf_category)[0]

        sf_framecode = sf_data.get_tag('sf_framecode')[0]

        try:

            poly_seq = self.__getPolymerSequence(sf_data, content_subtype)[0]

            input_source.setItemValue('polymer_sequence', poly_seq)

            if file_type == 'nmr-star':
                auth_poly_seq = self.__nefT.get_star_auth_seq(sf_data, lp_category)[0]

                for cid in range(len(poly_seq)):
                    chain_id = poly_seq[cid]['chain_id']
                    seq_ids = poly_seq[cid]['seq_id']
                    comp_ids = poly_seq[cid]['comp_id']

                    for auth_cid in range(len(auth_poly_seq)):

                        if auth_poly_seq[auth_cid]['chain_id'] != chain_id:
                            continue

                        _seq_ids = auth_poly_seq[auth_cid]['seq_id']
                        auth_asym_ids = auth_poly_seq[auth_cid]['auth_asym_id']
                        auth_seq_ids = auth_poly_seq[auth_cid]['auth_seq_id']
                        auth_comp_ids = auth_poly_seq[auth_cid]['auth_comp_id']

                        auth_asym_id_set = sorted(set(auth_asym_ids))

                        for auth_asym_id in auth_asym_id_set:

                            offsets = []
                            total = 0

                            for j in range(len(auth_seq_ids)):
                                auth_seq_id = auth_seq_ids[j]

                                if auth_seq_id in self.empty_value:
                                    continue

                                try:

                                    _auth_seq_id = int(auth_seq_id)

                                    offsets.append(_auth_seq_id - _seq_ids[j])
                                    total += 1

                                except ValueError:

                                    warn = "auth_seq_id '%s' (auth_asym_id %s, auth_comp_id %s) has to be int." % (auth_seq_id, auth_asym_id, auth_comp_ids[j])

                                    self.report.warning.appendDescription('sequence_mismatch', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__extractPolymerSequence() ++ Warning  - %s\n" % warn)

                                    pass

                            if total > 1:

                                offset = collections.Counter(offsets).most_common()[0][0]

                                for j in range(len(auth_seq_ids)):
                                    auth_seq_id = auth_seq_ids[j]

                                    if auth_seq_id in self.empty_value:
                                        continue

                                    try:

                                        _auth_seq_id = int(auth_seq_id)
                                    except ValueError:
                                        continue

                                    if _auth_seq_id - _seq_ids[j] != offset:

                                        warn = "auth_seq_id '%s' vs '%d' (auth_asym_id %s, auth_comp_id %s) mismatches." % (auth_seq_id, seq_ids[j] + offset, auth_asym_id, auth_comp_ids[j])

                                        self.report.warning.appendDescription('sequence_mismatch', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__extractPolymerSequence() ++ Warning  - %s\n" % warn)

                        for i in range(len(comp_ids)):

                            seq_id = seq_ids[i]
                            comp_id = comp_ids[i]

                            for j in range(len(auth_comp_ids)):

                                if _seq_ids[j] != seq_id:
                                    continue

                                auth_comp_id = auth_comp_ids[j]

                                if comp_id == auth_comp_id:
                                    continue

                                auth_asym_id = auth_asym_ids[j]
                                auth_seq_id = auth_seq_ids[j]

                                warn = "auth_comp_id %s (auth_asym_id %s, auth_seq_id %s) vs %s (chain_id %s, seq_id %s) mismatches." % (auth_comp_id, auth_asym_id, auth_seq_id, comp_id, chain_id, seq_id)

                                self.report.warning.appendDescription('sequence_mismatch', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                                self.report.setWarning()

                                if self.__verbose:
                                    self.__lfh.write("+NmrDpUtility.__extractPolymerSequence() ++ Warning  - %s\n" % warn)

                                break

            return True

        except KeyError as e:

            self.report.error.appendDescription('sequence_mismatch', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__extractPolymerSequence() ++ KeyError  - %s" % str(e))

        except LookupError as e:

            self.report.error.appendDescription('missing_mandatory_item', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__extractPolymerSequence() ++ LookupError  - %s" % str(e))

        except ValueError as e:

            self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__extractPolymerSequence() ++ ValueError  - %s" % str(e))

        except Exception as e:

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__extractPolymerSequence() ++ Error  - %s" % str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__extractPolymerSequence() ++ Error  - %s" % str(e))

        return False

    def __extractPolymerSequenceInLoop(self):
        """ Extract polymer sequence in interesting loops.
        """

        if self.report.isError():
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        poly_seq_list_set = {}
        poly_sid_list_set = {}

        for content_subtype in self.nmr_content_subtypes:

            if content_subtype == 'entry_info' or content_subtype == 'poly_seq' or not content_subtype in input_source_dic['content_subtype']:
                continue

            poly_seq_list_set[content_subtype] = []

            sf_category = self.sf_categories[file_type][content_subtype]
            lp_category = self.lp_categories[file_type][content_subtype]

            list_id = 1

            has_poly_seq = False

            for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

                sf_framecode = sf_data.get_tag('sf_framecode')[0]

                try:

                    poly_seq = self.__getPolymerSequence(sf_data, content_subtype)[0]

                    if len(poly_seq) > 0:

                        poly_seq_list_set[content_subtype].append({'list_id': list_id, 'sf_framecode': sf_framecode, 'polymer_sequence': poly_seq})

                        has_poly_seq = True

                        if file_type == 'nmr-star':
                            auth_poly_seq = self.__nefT.get_star_auth_seq(sf_data, lp_category)[0]

                            for cid in range(len(poly_seq)):
                                chain_id = poly_seq[cid]['chain_id']
                                seq_ids = poly_seq[cid]['seq_id']
                                comp_ids = poly_seq[cid]['comp_id']

                                for auth_cid in range(len(auth_poly_seq)):

                                    if auth_poly_seq[auth_cid]['chain_id'] != chain_id:
                                        continue

                                    _seq_ids = auth_poly_seq[auth_cid]['seq_id']
                                    auth_asym_ids = auth_poly_seq[auth_cid]['auth_asym_id']
                                    auth_seq_ids = auth_poly_seq[auth_cid]['auth_seq_id']
                                    auth_comp_ids = auth_poly_seq[auth_cid]['auth_comp_id']

                                    auth_asym_id_set = sorted(set(auth_asym_ids))

                                    for auth_asym_id in auth_asym_id_set:

                                        offsets = []
                                        total = 0

                                        for j in range(len(auth_seq_ids)):
                                            auth_seq_id = auth_seq_ids[j]

                                            if auth_seq_id in self.empty_value:
                                                continue

                                            try:

                                                _auth_seq_id = int(auth_seq_id)

                                                offsets.append(_auth_seq_id - _seq_ids[j])
                                                total += 1

                                            except ValueError:

                                                warn = "auth_seq_id '%s' (auth_asym_id %s, auth_comp_id %s) has to be int." % (auth_seq_id, auth_asym_id, auth_comp_ids[j])

                                                self.report.warning.appendDescription('sequence_mismatch', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                                                self.report.setWarning()

                                                if self.__verbose:
                                                    self.__lfh.write("+NmrDpUtility.__extractPolymerSequenceInLoop() ++ Warning  - %s\n" % warn)

                                                pass

                                        if total > 1:

                                            offset = collections.Counter(offsets).most_common()[0][0]

                                            for j in range(len(auth_seq_ids)):
                                                auth_seq_id = auth_seq_ids[j]

                                                if auth_seq_id in self.empty_value:
                                                    continue

                                                try:

                                                    _auth_seq_id = int(auth_seq_id)

                                                except ValueError:
                                                    continue

                                                if _auth_seq_id - _seq_ids[j] != offset:

                                                    warn = "auth_seq_id '%s' vs '%d' (auth_asym_id %s, auth_comp_id %s) mismatches." % (auth_seq_id, seq_ids[j] + offset, auth_asym_id, auth_comp_ids[j])

                                                    self.report.warning.appendDescription('sequence_mismatch', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                                                    self.report.setWarning()

                                                    if self.__verbose:
                                                        self.__lfh.write("+NmrDpUtility.__extractPolymerSequenceInLoop() ++ Warning  - %s\n" % warn)

                                    for i in range(len(comp_ids)):

                                        seq_id = seq_ids[i]
                                        comp_id = comp_ids[i]

                                        for j in range(len(auth_comp_ids)):

                                            if _seq_ids[j] != seq_id:
                                                continue

                                            auth_comp_id = auth_comp_ids[j]

                                            if comp_id == auth_comp_id:
                                                continue

                                            auth_asym_id = auth_asym_ids[j]
                                            auth_seq_id = auth_seq_ids[j]

                                            warn = "auth_comp_id %s (auth_asym_id %s, auth_seq_id %s) vs %s (chain_id %s, seq_id %s) mismatches." % (auth_comp_id, auth_asym_id, auth_seq_id, comp_id, chain_id, seq_id)

                                            self.report.warning.appendDescription('sequence_mismatch', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                                            self.report.setWarning()

                                            if self.__verbose:
                                                self.__lfh.write("+NmrDpUtility.__extractPolymerSequenceInLoop() ++ Warning  - %s\n" % warn)

                                            break

                except KeyError as e:

                    self.report.error.appendDescription('sequence_mismatch', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__extractPolymerSequenceInLoop() ++ KeyError  - %s" % str(e))

                except LookupError as e:

                    self.report.error.appendDescription('missing_mandatory_item', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__extractPolymerSequenceInLoop() ++ LookupError  - %s" % str(e))

                except ValueError as e:

                    self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__extractPolymerSequenceInLoop() ++ ValueError  - %s" % str(e))

                except Exception as e:

                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__extractPolymerSequenceInLoop() ++ Error  - %s" % str(e))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__extractPolymerSequenceInLoop() ++ Error  - %s" % str(e))

                list_id += 1

            if not has_poly_seq:
                poly_seq_list_set.pop(content_subtype)

        if self.report.isError():
            return False

        if len(poly_seq_list_set) > 0:
            input_source.setItemValue('polymer_sequence_in_loop', poly_seq_list_set)

        return True

    def __hasKeyValue(self, dict=None, key=None):
        """ Return whether a given dictionary has effective value for a key.
            @return: True if dict[key] has effective value, False otherwise
        """

        if dict is None or key is None:
            return False

        if key in dict:
            return False if dict[key] is None else True

        return False

    def __testSequenceConsistency(self):
        """ Perform sequence consistency test among extracted polymer sequences.
        """

        if self.report.isError():
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        has_poly_seq = self.__hasKeyValue(input_source_dic, 'polymer_sequence')
        has_poly_seq_in_loop = self.__hasKeyValue(input_source_dic, 'polymer_sequence_in_loop')

        if not has_poly_seq and not has_poly_seq_in_loop:
            return True

        polymer_sequence = input_source_dic['polymer_sequence']
        polymer_sequence_in_loop = input_source_dic['polymer_sequence_in_loop']

        poly_seq = 'poly_seq'

        subtype_with_poly_seq = [poly_seq if has_poly_seq else None]

        for subtype in polymer_sequence_in_loop.keys():
            subtype_with_poly_seq.append(subtype)

        for subtype_pair in itertools.combinations_with_replacement(subtype_with_poly_seq, 2):

            # poly_seq is reference sequence and suppress tests on combinations of two sequences in loop
            if has_poly_seq and (not poly_seq in subtype_pair or subtype_pair == (poly_seq, poly_seq)):
                continue

            subtype1 = subtype_pair[0] # poly_seq will appear only on subtype1
            subtype2 = subtype_pair[1]

            lp_category1 = self.lp_categories[file_type][subtype1]
            lp_category2 = self.lp_categories[file_type][subtype2]

            # reference polymer sequence exists
            if has_poly_seq and subtype1 == poly_seq:
                ps1 = polymer_sequence

                ref_chain_ids = {s1['chain_id'] for s1 in ps1}

                list_len2 = len(polymer_sequence_in_loop[subtype2])

                for list_id2 in range(list_len2):
                    ps2 = polymer_sequence_in_loop[subtype2][list_id2]['polymer_sequence']

                    sf_framecode2 = polymer_sequence_in_loop[subtype2][list_id2]['sf_framecode']

                    for s2 in ps2:

                        chain_id = s2['chain_id']

                        if not chain_id in ref_chain_ids:

                            err = "Invalid chain_id %s exists." % chain_id

                            self.report.error.appendDescription('sequence_mismatch', {'file_name': file_name, 'sf_framecode': sf_framecode2, 'category': lp_category2, 'description': err})
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__testSequenceConsistency() ++ Error  - %s\n" % err)

                        else:

                            for s1 in ps1:

                                if s1['chain_id'] != s2['chain_id']:
                                    continue

                                for j in range(len(s2['seq_id'])):
                                    seq_id = s2['seq_id'][j]
                                    comp_id = s2['comp_id'][j]

                                    if not seq_id in s1['seq_id']:

                                        err = "Invalid seq_id %s (chain_id %s) exists." % (seq_id, chain_id)

                                        self.report.error.appendDescription('sequence_mismatch', {'file_name': file_name, 'sf_framecode': sf_framecode2, 'category': lp_category2, 'description': err})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__testSequenceConsistency() ++ Error  - %s\n" % err)

                                    else:
                                        i = s1['seq_id'].index(seq_id)

                                        if comp_id != s1['comp_id'][i]:

                                            err = "Invalid comp_id %s vs %s (seq_id %s, chain_id %s) exists." % (comp_id, s1['comp_id'][i], seq_id, chain_id)

                                            self.report.error.appendDescription('sequence_mismatch', {'file_name': file_name, 'sf_framecode': sf_framecode2, 'category': lp_category2, 'description': err})
                                            self.report.setError()

                                            if self.__verbose:
                                                self.__lfh.write("+NmrDpUtility.__testSequenceConsistency() ++ Error  - %s\n" % err)

            # brute force check
            else:

                list_len1 = len(polymer_sequence_in_loop[subtype1])
                list_len2 = len(polymer_sequence_in_loop[subtype2])

                for list_id1 in range(list_len1):
                    ps1 = polymer_sequence_in_loop[subtype1][list_id1]['polymer_sequence']

                    sf_framecode1 = polymer_sequence_in_loop[subtype1][list_id1]['sf_framecode']

                    for list_id2 in range(list_len2):
                        ps2 = polymer_sequence_in_loop[subtype2][list_id2]['polymer_sequence']

                        sf_framecode2 = polymer_sequence_in_loop[subtype2][list_id2]['sf_framecode']

                        # suppress redundant tests inside the same subtype
                        if subtype1 == suntype2 and list_id1 >= list_id2:
                            continue

                        for s2 in ps2:

                            chain_id = s2['chain_id']

                            for s1 in ps1:

                                if chain_id != s1['chain_id']:
                                    continue

                                for j in range(len(s2['seq_id'])):
                                    seq_id = s2['seq_id'][j]
                                    comp_id = s2['comp_id'][j]

                                    if seq_id in s1['seq_id']:
                                        i = s1['seq_id'].index(seq_id)

                                        if comp_id != s1['comp_id'][i]:

                                            err = "Unmatched comp_id %s vs %s (seq_id %s, chain_id %s) exists against %s saveframe." % (comp_id, s1['comp_id'][i], seq_id, chain_id, sf_framecode1)

                                            self.report.error.appendDescription('sequence_mismatch', {'file_name': file_name, 'sf_framecode': sf_framecode2, 'category': lp_category2, 'description': err})
                                            self.report.setError()

                                            if self.__verbose:
                                                self.__lfh.write("+NmrDpUtility.__testSequenceConsistency() ++ Error  - %s\n" % err)

                        # inverse check required for unverified sequences
                        for s1 in ps1:

                            chain_id = s1['chain_id']

                            for s2 in ps2:

                                if chain_id != s2['chain_id]']:
                                    continue

                                for i in range(len(s1['seq_id'])):
                                    seq_id = s1['seq_id'][i]
                                    comp_id = s1['comp_id'][i]

                                    if seq_id in s2['seq_id']:
                                        j = s2['seq_id'].index(seq_id)

                                        if comp_id != s2['comp_id'][j]:

                                            err = "Unmatched comp_id %s vs %s (seq_id %s, chain_id %s) exists against %s saveframe." % (comp_id, s2['comp_id'][j], seq_id, chain_id, sf_framecode2)

                                            self.report.error.appendDescription('sequence_mismatch', {'file_name': file_name, 'sf_framecode': sf_framecode1, 'category': lp_category1, 'description': err})
                                            self.report.setError()

                                            if self.__verbose:
                                                self.__lfh.write("+NmrDpUtility.__testSequenceConsistency() ++ Error  - %s\n" % err)

        return not self.report.isError()

    def __extractCommonPolymerSequence(self):
        """ Extract common polymer sequence if required.
        """

        if self.report.isError():
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        has_poly_seq = self.__hasKeyValue(input_source_dic, 'polymer_sequence')
        has_poly_seq_in_loop = self.__hasKeyValue(input_source_dic, 'polymer_sequence_in_loop')

        # pass if poly_seq exists
        if has_poly_seq or not has_poly_seq_in_loop:
            return True

        polymer_sequence_in_loop = input_source_dic['polymer_sequence_in_loop']

        common_poly_seq = {}

        for content_subtype in polymer_sequence_in_loop.keys():
            list_len = len(polymer_sequence_in_loop[content_subtype])

            for list_id in range(list_len):
                ps = polymer_sequence_in_loop[content_subtype][list_id]['polymer_sequence']

                for s in ps:
                    chain_id = s['chain_id']

                    if not chain_id in common_poly_seq:
                        common_poly_seq[chain_id] = set()

        for content_subtype in polymer_sequence_in_loop.keys():
            list_len = len(polymer_sequence_in_loop[content_subtype])

            for list_id in range(list_len):
                ps = polymer_sequence_in_loop[content_subtype][list_id]['polymer_sequence']

                chain_id = s['chain_id']

                for i in range(len(s['seq_id'])):
                    seq_id = s['seq_id'][i]
                    comp_id = s['comp_id'][i]

                    common_poly_seq[chain_id].add('{:04d} {}'.format(seq_id, comp_id))

        asm = [] # molecular assembly of a loop

        for chain_id in sorted(common_poly_seq.keys()):

            if len(common_poly_seq[chain_id]) > 0:
                sorted_poly_seq = sorted(common_poly_seq[chain_id])
                asm.append({'chain_id': chain_id, 'seq_id': [int(i.split(' ')[0]) for i in sorted_poly_seq], 'comp_id': [i.split(' ')[1] for i in sorted_poly_seq]})

        if len(asm) > 0:
            input_source.setItemValue('polymer_sequence', asm)

        return True

    def __extractNonStandardResidue(self):
        """ Extract non-standard residue.
        """

        if self.report.isError():
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']
        file_name = input_source_dic['file_name']

        content_subtype = 'poly_seq'

        has_poly_seq = self.__hasKeyValue(input_source_dic, 'polymer_sequence')

        if not has_poly_seq:
            return True

        polymer_sequence = input_source_dic['polymer_sequence']

        sf_category = self.sf_categories[file_type][content_subtype]
        lp_category = self.lp_categories[file_type][content_subtype]

        sf_data = self.__star_data.get_saveframes_by_category(sf_category)[0]

        sf_framecode = sf_data.get_tag('sf_framecode')[0]

        asm = []

        for s in polymer_sequence:

            has_non_std_comp_id = False

            ent = {'chain_id': s['chain_id'], 'seq_id': [], 'comp_id': [], 'chem_comp_name': [], 'exptl_data': []}

            for i in range(len(s['seq_id'])):
                seq_id = s['seq_id'][i]
                comp_id = s['comp_id'][i]

                if self.__get1LetterCode(comp_id) == 'X':
                    has_non_std_comp_id = True

                    ent['seq_id'].append(seq_id)
                    ent['comp_id'].append(comp_id)

                    self.__updateChemCompDict(comp_id)

                    if self.__last_comp_id_test: # matches with comp_id in CCD
                        cc_name = self.__last_chem_comp_dict['_chem_comp.name']
                        cc_rel_status = self.__last_chem_comp_dict['_chem_comp.pdbx_release_status']
                        if cc_rel_status == 'REL':
                            ent['chem_comp_name'].append(cc_name)
                        else:
                            ent['chem_comp_name'].append('(Not available due to CCD status code %s)' % cc_rel_status)

                    else:
                        ent['chem_comp_name'].append(None)

                        warn = 'Non standard residue (chain_id %s, seq_id %s, comp_id %s) did not match with chemical component dictionary (CCD).'

                        self.report.warning.appendDescription('ccd_mismatch', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                        self.report.setWarning()

                        if self.__verbose:
                           self.__lfh.write("+NmrDpUtility.__extractNonStandardResidue() ++ Warning  - %s\n" % warn)

                    ent['exptl_data'].append({'chem_shift': False, 'dist_restraint': False, 'dihed_restraint': False, 'rdc_restraint': False, 'spectral_peak': False, 'coordinate': False})

            if has_non_std_comp_id:
                asm.append(ent)

        if len(asm) > 0:
            input_source.setItemValue('non_standard_residue', asm)

        return True

    def __appendPolymerSequenceAlignment(self):
        """ Append polymer sequence alignment of interesting loops.
        """

        if self.report.isError():
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        has_poly_seq = self.__hasKeyValue(input_source_dic, 'polymer_sequence')
        has_poly_seq_in_loop = self.__hasKeyValue(input_source_dic, 'polymer_sequence_in_loop')

        if not has_poly_seq:

            err = "Common polymer sequence did not exist, __extractCommonPolymerSequence() should be invoked."

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__appendPolymerSequenceAlignment() ++ Error  - %s" % err)
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__appendPolymerSequenceAlignment() ++ Error  - %s\n" % err)

            return False

        if not has_poly_seq_in_loop:
            return True

        polymer_sequence = input_source_dic['polymer_sequence']
        polymer_sequence_in_loop = input_source_dic['polymer_sequence_in_loop']

        if polymer_sequence is None:
            return False

        for content_subtype in polymer_sequence_in_loop.keys():
            list_len = len(polymer_sequence_in_loop[content_subtype])

            seq_align_set = []

            for s1 in polymer_sequence:
                chain_id = s1['chain_id']

                if type(chain_id) == int:
                    _chain_id = str(chain_id)
                else:
                    _chain_id = chain_id

                for list_id in range(list_len):
                    ps2 = polymer_sequence_in_loop[content_subtype][list_id]['polymer_sequence']

                    for s2 in ps2:

                        if chain_id != s2['chain_id']:
                            continue

                        _s2 = self.__fillBlankedCompId(s1, s2)

                        self.__pA.setReferenceSequence(s1['comp_id'], 'REF' + _chain_id)
                        self.__pA.addTestSequence(_s2['comp_id'], _chain_id)
                        self.__pA.doAlign()
                        #self.__pA.prAlignmentConflicts(_chain_id)
                        myAlign = self.__pA.getAlignment(_chain_id)

                        length = len(myAlign)

                        if length == 0:
                            continue

                        unmapped = 0
                        conflict = 0
                        for i in range(length):
                            myPr = myAlign[i]
                            if myPr[0].encode() == '.' or myPr[1].encode() == '.':
                                unmapped += 1
                            elif myPr[0] != myPr[1]:
                                conflict += 1

                        if length == unmapped + conflict:
                            continue

                        ref_length = len(s1['seq_id'])

                        ref_code = self.__get1LetterCodeSequence(s1['comp_id'])
                        test_code = self.__get1LetterCodeSequence(_s2['comp_id'])
                        mid_code = self.__getMiddleCode(ref_code, test_code)
                        ref_gauge_code = self.__getGaugeCode(s1['seq_id'])
                        test_gauge_code = self.__getGaugeCode(_s2['seq_id'])

                        seq_align = {'list_id': polymer_sequence_in_loop[content_subtype][list_id]['list_id'],
                                     'sf_framecode': polymer_sequence_in_loop[content_subtype][list_id]['sf_framecode'],
                                     'chain_id': chain_id, 'length': ref_length, 'conflict': conflict, 'unmapped': unmapped, 'sequence_coverage': float('{:.3f}'.format(float(length - (unmapped + conflict)) / float(ref_length))),
                                     'ref_seq_id': s1['seq_id'],
                                     'ref_gauge_code': ref_gauge_code, 'ref_code': ref_code, 'mid_code': mid_code, 'test_code': test_code, 'test_gauge_code': test_gauge_code}

                        seq_align_set.append(seq_align)

                        for j in range(len(ref_code)):
                            if ref_code[j] == 'X' and test_code[j] == 'X':
                                input_source.updateNonStandardResidueByExptlData(chain_id, s1['seq_id'][j], content_subtype)

            if len(seq_align_set) > 0:
                self.report.sequence_alignment.setItemValue('nmr_poly_seq_vs_' + content_subtype, seq_align_set)

        return True

    def __fillBlankedCompId(self, s1, s2):
        """ Fill blanked comp ID in s2 against s1.
        """

        seq_ids = sorted(set(s1['seq_id']) | set(s2['seq_id']))
        comp_ids = []

        for i in seq_ids:
            if i in s2['seq_id']:
                j = s2['seq_id'].index(i)
                comp_ids.append(s2['comp_id'][j])
            else:
                comp_ids.append('.') # blank comp id

        return {'chain_id': s2['chain_id'], 'seq_id': seq_ids, 'comp_id': comp_ids}

    def __get1LetterCode(self, comp_id):
        """ Convert comp ID to 1-letter code.
        """

        comp_id = comp_id.upper()

        if comp_id in self.monDict3:
            return self.monDict3[comp_id]
        elif comp_id in self.empty_value:
            return '.'
        else:
            return 'X'

    def __get1LetterCodeSequence(self, comp_ids):
        """ Convert array of comp ID to 1-letter code sequence.
        """

        array = ''

        for comp_id in comp_ids:
            array += self.__get1LetterCode(comp_id)

        return array

    def __getMiddleCode(self, ref_seq, test_seq):
        """ Return array of middle code of sequence alignment.
        """

        array = ''

        for i in range(len(ref_seq)):
            if i < len(test_seq):
                array += '|' if ref_seq[i] == test_seq[i] else ' '
            else:
                array += ' '

        return array

    def __getGaugeCode(self, seq_id):
        """ Return gauge code for seq ID.
        """

        sid_len = len(seq_id)
        code_len = 0

        chars = []

        for sid in seq_id:

            if sid >= 0 and sid % 10 == 0 and code_len == 0:

                code = str(sid)
                code_len = len(code)

                for j in range(code_len):
                    chars.append(code[j])

            if code_len > 0:
                code_len -= 1
            else:
                chars.append('-')

        for t in range(sid_len / 10):
            offset = (t + 1) * 10 - 1

            code = ''

            p = offset
            while p < len(chars) and chars[p] != '-':
                code += chars[p]
                chars[p] = '-'
                p += 1

            code_len = len(code)

            offset -= code_len - 1

            if offset >= 0:
                for j in range(code_len):
                    chars[offset + j] = code[j]

        array = ''.join(chars)

        return array[:sid_len]

    def __validateAtomNomenclature(self):
        """ Validate atom nomenclature using NEFTranslator and CCD.
        """

        if self.report.isError():
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        polymer_sequence_in_loop = input_source_dic['polymer_sequence_in_loop']

        for content_subtype in polymer_sequence_in_loop.keys():

            sf_category = self.sf_categories[file_type][content_subtype]
            lp_category = self.lp_categories[file_type][content_subtype]

            for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

                sf_framecode = sf_data.get_tag('sf_framecode')[0]

                try:

                    if file_type == 'nef':
                        pairs = self.__nefT.get_nef_comp_atom_pair(sf_data, lp_category,
                                                                   allow_empty=(content_subtype == 'spectral_peak'))[0]
                    else:
                        pairs = self.__nefT.get_star_comp_atom_pair(sf_data, lp_category,
                                                                    allow_empty=(content_subtype == 'spectral_peak'))[0]

                    for pair in pairs:
                        comp_id = pair['comp_id']
                        atom_ids = pair['atom_id']

                        # standard residue
                        if self.__nefT.get_one_letter_code(comp_id) != 'X':

                            if file_type == 'nef':

                                _atom_ids = []
                                for atom_id in atom_ids:

                                    _atom_id = self.__nefT.get_nmrstar_atom(comp_id, atom_id, leave_unmatched=False)[0]

                                    if len(_atom_id) == 0:

                                        err = "Invalid atom_id %s (comp_id %s) exists." % (atom_id, comp_id)

                                        self.report.error.appendDescription('invalid_atom_nomenclature', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__validateAtomNomenclature() ++ Error  - %s\n" % err)

                                    else:
                                        _atom_ids.extend(_atom_id)

                                atom_ids = sorted(set(_atom_ids))

                            for atom_id in atom_ids:

                                if not self.__nefT.validate_comp_atom(comp_id, atom_id):

                                    err = "Invalid atom_id %s (comp_id %s) exists." % (atom_id, comp_id)

                                    self.report.error.appendDescription('invalid_atom_nomenclature', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                    self.report.setError()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__validateAtomNomenclature() ++ Error  - %s\n" % err)

                        # non-standard residue
                        else:
                            self.__updateChemCompDict(comp_id)

                            if self.__last_comp_id_test: # matches with comp_id in CCD

                                ref_atom_ids = [a[self.__cca_atom_id] for a in self.__last_chem_comp_atoms] # if a[self.__cca_leaving_atom_flag] != 'Y']
                                unk_atom_ids = []

                                for atom_id in atom_ids:

                                    if not atom_id in ref_atom_ids:
                                        unk_atom_ids.append(atom_id)

                                if len(unk_atom_ids) > 0:
                                    cc_rel_status = self.__last_chem_comp_dict['_chem_comp.pdbx_release_status']
                                    if cc_rel_status == 'REL':
                                        cc_name = self.__last_chem_comp_dict['_chem_comp.name']
                                    else:
                                        cc_name = '(Not available due to CCD status code %s)' % cc_rel_status

                                    warn = "Unknown atom_id %s (comp_id %s, chem_comp_name %s) exist." % (unk_atom_ids, comp_id, cc_name)

                                    self.report.warning.appendDescription('atom_nomenclature_mismatch', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__validateAtomNomenclature() ++ Warning  - %s\n" % warn)

                                ref_elems = set([a[self.__cca_type_symbol] for a in self.__last_chem_comp_atoms if a[self.__cca_leaving_atom_flag] != 'Y'])

                                for elem in ref_elems:
                                    if elem in self.paramag_elems or elem in self.ferromag_elems:
                                        self.report.setDiagmagnetic(False)
                                        break

                            else:
                                pass

                    if file_type == 'nmr-star':
                        auth_pairs = self.__nefT.get_star_auth_comp_atom_pair(sf_data, lp_category)[0]

                        for auth_pair in auth_pairs:
                            comp_id = auth_pair['comp_id']
                            auth_atom_ids = auth_pair['atom_id']

                            # standard residue
                            if self.__nefT.get_one_letter_code(comp_id) != 'X':

                                _auth_atom_ids = []
                                for auth_atom_id in auth_atom_ids:

                                    _auth_atom_id = self.__nefT.get_nmrstar_atom(comp_id, auth_atom_id, leave_unmatched=False)[0]

                                    if len(_auth_atom_id) == 0:

                                        warn = "Unmatched author atom ID %s (auth_comp_id %s) exists." % (auth_atom_id, comp_id)

                                        self.report.warning.appendDescription('atom_nomenclature_mismatch', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__validateAtomNomenclature() ++ Warning  - %s\n" % warn)

                                    else:
                                        _auth_atom_ids.extend(_auth_atom_id)

                                auth_atom_ids = sorted(set(_auth_atom_ids))

                                for auth_atom_id in auth_atom_ids:

                                    if not self.__nefT.validate_comp_atom(comp_id, auth_atom_id):

                                        warn = "Unmatched author atom ID %s (auth_comp_id %s) exists." % (auth_atom_id, comp_id)

                                        self.report.warning.appendDescription('atom_nomenclature_mismatch', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__validateAtomNomenclature() ++ Warning  - %s\n" % warn)

                            # non-standard residue
                            else:
                                has_comp_id = False

                                for pair in pairs:

                                    if pair['comp_id'] != comp_id:
                                        continue

                                    has_comp_id = True

                                    atom_ids = pair['atom_id']

                                    if (set(auth_atom_ids) | set(atom_ids)) != set(atom_ids):

                                        warn = "Unmatched author atom ID %s (auth_comp_id %s, non-standard residue) exists." % ((set(auth_atom_ids) | set(atom_ids)) - set(atom_ids), comp_id)

                                        self.report.warning.appendDescription('atom_nomenclature_mismatch', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__validateAtomNomenclature() ++ Warning  - %s\n" % warn)

                                    break

                                if not has_comp_id:

                                        warn = "Unmatched author atom ID %s (auth_comp_id %s, non-standard residue) exists." % (auth_atom_ids, comp_id)

                                        self.report.warning.appendDescription('atom_nomenclature_mismatch', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__validateAtomNomenclature() ++ Warning  - %s\n" % warn)

                except LookupError as e:

                    self.report.error.appendDescription('missing_mandatory_item', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__validateAtomNomenclature() ++ LookupError  - %s" % str(e))

                except ValueError as e:

                    self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__validateAtomNomenclature() ++ ValueError  - %s" % str(e))

                except Exception as e:

                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__validateAtomNomenclature() ++ Error  - %s" % str(e))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__validateAtomNomenclature() ++ Error  - %s" % str(e))

        return not self.report.isError()

    def __validateAtomTypeOfCSLoop(self):
        """ Validate atom type, isotope number on assigned chemical shifts.
        """

        if self.report.isError():
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        content_subtype = 'chem_shift'

        if not content_subtype in input_source_dic['content_subtype'].keys():

            err = "Assigned chemical shift loop did not exist in %s file." % file_name

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__validateAtomTypeOfCSLoop() ++ Error  - %s" % err)
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__validateAtomTypeOfCSLoop() ++ Error  - %s\n" % err)

            return False

        sf_category = self.sf_categories[file_type][content_subtype]
        lp_category = self.lp_categories[file_type][content_subtype]

        for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

            sf_framecode = sf_data.get_tag('sf_framecode')[0]

            try:

                if file_type == 'nef':
                    a_types = self.__nefT.get_nef_atom_type_from_cs_loop(sf_data)[0]
                else:
                    a_types = self.__nefT.get_star_atom_type_from_cs_loop(sf_data)[0]

                for a_type in a_types:
                    atom_type = a_type['atom_type']
                    isotope_nums = a_type['isotope_number']
                    atom_ids = a_type['atom_id']

                    if not atom_type in self.atom_isotopes.keys():

                        err = "Invalid atom_type %s exists." % atom_type

                        self.report.error.appendDescription('invalid_atom_type', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__validateAtomTypeOfCSLoop() ++ Error  - %s\n" % err)

                    else:
                        for isotope_num in isotope_nums:
                            if not isotope_num in self.atom_isotopes[atom_type]:

                                err = "Invalid isotope number %s (atom_type %s, allowed isotope number %s) exists." % (isotope_num, atom_type, self.atom_isotopes[atom_type])

                                self.report.error.appendDescription('invalid_isotope_number', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write("+NmrDpUtility.__validateAtomTypeOfCSLoop() ++ Error  - %s\n" % err)

                        for atom_id in atom_ids:
                            if not atom_id.startswith(atom_type):

                                err = "Invalid atom_id %s (atom_type %s) exists." % (atom_id, atom_type)

                                self.report.error.appendDescription('invalid_atom_nomenclature', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write("+NmrDpUtility.__validateAtomTypeOfCSLoop() ++ Error  - %s\n" % err)

            except LookupError as e:

                self.report.error.appendDescription('missing_mandatory_item', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__validateAtomTypeOfCSLoop() ++ LookupError  - %s" % str(e))

            except ValueError as e:

                self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__validateAtomTypeOfCSLoop() ++ ValueError  - %s" % str(e))

            except Exception as e:

                self.report.error.appendDescription('internal_error', "+NmrDpUtility.__validateAtomTypeOfCSLoop() ++ Error  - %s" % str(e))
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__validateAtomTypeOfCSLoop() ++ Error  - %s" % str(e))

        return not self.report.isError()

    def __validateAmbigCodeOfCSLoop(self):
        """ Validate ambiguity code on assigned chemical shifts.
        """

        if self.report.isError():
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        content_subtype = 'chem_shift'

        if not content_subtype in input_source_dic['content_subtype'].keys():

            err = "Assigned chemical shift loop did not exist in %s file." % file_name

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__validateAmbigCodeOfCSLoop() ++ Error  - %s" % err)
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__validateAmbigCodeOfCSLoop() ++ Error  - %s\n" % err)

            return False

        # NEF file has no ambiguity code
        if file_type == 'nef':
            return True

        sf_category = self.sf_categories[file_type][content_subtype]
        lp_category = self.lp_categories[file_type][content_subtype]

        for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

            sf_framecode = sf_data.get_tag('sf_framecode')[0]

            try:

                a_codes = self.__nefT.get_star_ambig_code_from_cs_loop(sf_data)[0]

                comp_ids_wo_ambig_code = []

                for a_code in a_codes:
                    comp_id = a_code['comp_id']
                    ambig_code = a_code['ambig_code']
                    atom_ids = a_code['atom_id']

                    if ambig_code is None:
                        comp_ids_wo_ambig_code.append(comp_id)

                    elif ambig_code == 1 or ambig_code >= 4:
                        pass

                    # ambig_code is 2 (geminal atoms) or 3 (aromatic ring atoms in opposite side)
                    else:

                        for atom_id in atom_ids:

                            allowed_ambig_code = self.__csStat.getMaxAmbigCodeWoSetId(comp_id, atom_id)

                            if ambig_code > allowed_ambig_code:

                                err = "Invalid ambiguity code %s (comp_id %s, atom_id %s, allowed ambig_code %s) exists." % (ambig_code, comp_id, atom_id, [1, allowed_ambig_code, 4, 5, 6, 9])

                                self.report.error.appendDescription('invalid_ambiguity_code', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write("+NmrDpUtility.__testAmbigCodeOfCSLoop() ++ Error  - %s\n" % err)

                if len(comp_ids_wo_ambig_code) > 0:

                    warn = "Missing ambiguity code for the following residues %s." % comp_ids_wo_ambig_code

                    self.report.warning.appendDescription('missing_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                    self.report.setWarning()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testAmbigCodeOfCSLoop() ++ Warning  - %s\n" % warn)

            except LookupError as e:

                self.report.error.appendDescription('missing_mandatory_item', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__testAmbigCodeOfCSLoop() ++ LookupError  - %s" % str(e))

            except ValueError as e:

                self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__testAmbigCodeOfCSLoop() ++ ValueError  - %s" % str(e))

            except Exception as e:

                self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testAmbigCodeOfCSLoop() ++ Error  - %s" % str(e))
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__testAmbigCodeOfCSLoop() ++ Error  - %s" % str(e))

        return not self.report.isError()

    def __testIndexConsistency(self):
        """ Perform consistency test on index of interesting loops.
        """

        if self.report.isError():
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        for content_subtype in input_source_dic['content_subtype'].keys():

            sf_category = self.sf_categories[file_type][content_subtype]
            lp_category = self.lp_categories[file_type][content_subtype]

            index_tag = self.index_tags[file_type][content_subtype]

            if index_tag is None:
                continue

            for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

                sf_framecode = sf_data.get_tag('sf_framecode')[0]

                try:

                    indices = self.__nefT.get_index(sf_data, lp_category, index_id=index_tag)[0]

                    if indices != range(1, len(indices) + 1):

                        warn = "Index (loop tag %s.%s) is disordered." % (lp_category, index_tag)

                        self.report.warning.appendDescription('disordered_index', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                        self.report.setWarning()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__testIndexConsistency() ++ Warning  - %s\n" % warn)

                except KeyError as e:

                    self.report.error.appendDescription('duplicated_index', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testIndexConsistency() ++ KeyError  - %s" % str(e))

                except LookupError as e:

                    self.report.error.appendDescription('missing_mandatory_item', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testIndexConsistency() ++ LookupError  - %s" % str(e))

                except ValueError as e:

                    self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testIndexConsistency() ++ ValueError  - %s" % str(e))

                except Exception as e:

                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testIndexConsistency() ++ Error  - %s" % str(e))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testIndexConsistency() ++ Error  - %s" % str(e))

        return not self.report.isError()

    def __testDataConsistencyInLoop(self):
        """ Perform consistency test on data of interesting loops.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        if input_source_dic['content_subtype'] is None:
            return False

        __errors = self.report.getTotalErrors()

        for content_subtype in input_source_dic['content_subtype'].keys():

            if content_subtype == 'entry_info':
                continue

            sf_category = self.sf_categories[file_type][content_subtype]
            lp_category = self.lp_categories[file_type][content_subtype]

            for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

                sf_framecode = sf_data.get_tag('sf_framecode')[0]

                allowed_tags = self.allowed_tags[file_type][content_subtype]
                disallowed_tags = None

                if content_subtype == 'spectral_peak':

                    try:

                        _num_dim = sf_data.get_tag(self.num_dim_items[file_type])[0]
                        num_dim = int(_num_dim)

                        if not num_dim in range(1, self.lim_num_dim):
                            raise ValueError()

                    except ValueError: # raised error already at __testIndexConsistency()
                        continue

                    max_dim = num_dim + 1

                    key_items = []
                    for dim in range(1, max_dim):
                        for k in self.pk_key_items[file_type]:
                            _k = copy.copy(k)
                            if '%s' in k['name']:
                               _k['name'] = k['name'] % dim
                            key_items.append(_k)

                    data_items = []
                    for d in self.data_items[file_type][content_subtype]:
                        data_items.append(d)
                    for dim in range(1, max_dim):
                        for d in self.pk_data_items[file_type]:
                            _d = copy.copy(d)
                            if '%s' in d['name']:
                                _d['name'] = d['name'] % dim
                            data_items.append(_d)

                    if max_dim < self.lim_num_dim:
                        disallowed_tags = []
                        for dim in range(max_dim, self.lim_num_dim):
                            for t in self.spectral_peak_disallowed_tags[file_type]:
                                if '%s' in t:
                                    t = t % dim
                                disallowed_tags.append(t)

                else:

                    key_items = self.key_items[file_type][content_subtype]
                    data_items = self.data_items[file_type][content_subtype]

                try:

                    lp_data = self.__nefT.check_data(sf_data, lp_category, key_items, data_items, allowed_tags, disallowed_tags,
                                                     inc_idx_test=True, enforce_non_zero=True, enforce_sign=True, enforce_enum=True)[0]

                    self.__lp_data[content_subtype].append({'sf_framecode': sf_framecode, 'data': lp_data})

                except KeyError as e:

                    self.report.error.appendDescription('multiple_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testDataConsistencyInLoop() ++ KeyError  - %s" % str(e))

                except LookupError as e:

                    self.report.error.appendDescription('missing_mandatory_item', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testDataConsistencyInLoop() ++ LookupError  - %s" % str(e))

                except ValueError as e:

                    self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testDataConsistencyInLoop() ++ ValueError  - %s" % str(e))

                except UserWarning as e:

                    warns = str(e).strip("'").split('\n')

                    for warn in warns:

                        if warn == '':
                            continue

                        zero = warn.startswith('[Zero value error] ')
                        nega = warn.startswith('[Negative value error] ')
                        enum = warn.startswith('[Enumeration error] ')

                        if zero or nega or enum:

                            if zero:
                                warn = warn[19:]
                            elif nega:
                                warn = warn[23:]
                            else:
                                warn = warn[20:]

                            self.report.warning.appendDescription('missing_data' if zero else ('unusual_data' if nega else 'enum_failure'), {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                            self.report.setWarning()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__testDataConsistencyInLoop() ++ Warning  - %s\n" % warn)

                        else:

                            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testDataConsistencyInLoop() ++ Error  - %s" % warn)
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__testDataConsistencyInLoop() ++ Error  - %s" % warn)

                    # try to parse data without constraints

                    try:

                        lp_data = self.__nefT.check_data(sf_data, lp_category, key_items, data_items, allowed_tags, disallowed_tags)[0]

                        self.__lp_data[content_subtype].append({'sf_framecode': sf_framecode, 'data': lp_data})

                    except:
                        pass

                except Exception as e:

                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testDataConsistencyInLoop() ++ Error  - %s" % str(e))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testDataConsistencyInLoop() ++ Error  - %s" % str(e))

                if not lp_data is None and len(lp_data) == 0:

                    warn = "Unexpectedly, no rows found in a loop."

                    self.report.warning.appendDescription('missing_content', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                    self.report.setWarning()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testDataConsistencyInLoop() ++ Warning  - %s\n" % warn)

        return self.report.getTotalErrors() == __errors

    def __testDataConsistencyInAuxLoop(self):
        """ Perform consistency test on data of auxiliary loops.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        if input_source_dic['content_subtype'] is None:
            return False

        __errors = self.report.getTotalErrors()

        for content_subtype in input_source_dic['content_subtype'].keys():

            sf_category = self.sf_categories[file_type][content_subtype]
            lp_category = self.lp_categories[file_type][content_subtype]

            for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

                sf_framecode = sf_data.get_tag('sf_framecode')[0]

                if content_subtype == 'spectral_peak':

                    try:

                        _num_dim = sf_data.get_tag(self.num_dim_items[file_type])[0]
                        num_dim = int(_num_dim)

                        if not num_dim in range(1, self.lim_num_dim):
                            raise ValueError()

                    except ValueError:

                        err = "%s %s must be in %s." % (self.num_dim_items[file_type], _num_dim, set(range(1, self.lim_num_dim)))

                        self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__testDataConsistencyInAuxLoop() ++ ValueError  - %s\n" % err)

                for loop in sf_data.loops:

                    lp_category = loop.category

                    # main content of loop has been processed in __testDataConsistencyInLoop()
                    if lp_category in self.lp_categories[file_type][content_subtype]:
                        continue

                    elif lp_category in self.aux_lp_categories[file_type][content_subtype]:

                        key_items = self.aux_key_items[file_type][content_subtype][lp_category]
                        data_items = self.aux_data_items[file_type][content_subtype][lp_category]
                        allowed_tags = self.aux_allowed_tags[file_type][content_subtype][lp_category]

                        try:

                            aux_data = self.__nefT.check_data(sf_data, lp_category, key_items, data_items, allowed_tags, None,
                                                              inc_idx_test=True, enforce_non_zero=True, enforce_sign=True, enforce_enum=True)[0]

                            self.__aux_data[content_subtype].append({'sf_framecode': sf_framecode, 'category': lp_category, 'data': aux_data})

                            if content_subtype == 'spectral_peak':
                                self.__testDataConsistencyInAuxLoopOfSpectralPeak(file_name, file_type, sf_framecode, num_dim, lp_category, aux_data)

                        except KeyError as e:

                            self.report.error.appendDescription('multiple_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__testDataConsistencyInAuxLoop() ++ KeyError  - %s" % str(e))

                        except LookupError as e:

                            self.report.error.appendDescription('missing_mandatory_item', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__testDataConsistencyInAuxLoop() ++ LookupError  - %s" % str(e))

                        except ValueError as e:

                            self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__testDataConsistencyInAuxLoop() ++ ValueError  - %s" % str(e))

                        except UserWarning as e:

                            warns = str(e).strip("'").split('\n')

                            for warn in warns:

                                if warn == '':
                                    continue

                                zero = warn.startswith('[Zero value error] ')
                                nega = warn.startswith('[Negative value error] ')
                                enum = warn.startswith('[Enumeration error] ')

                                if zero or nega or enum:

                                    if zero:
                                        warn = warn[19:]
                                    elif nega:
                                        warn = warn[23:]
                                    else:
                                        warn = warn[20:]

                                    self.report.warning.appendDescription('missing_data' if zero else ('unusual_data' if nega else 'enum_failure'), {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__testDataConsistencyInAuxLoop() ++ Warning  - %s\n" % warn)

                                else:

                                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testDataConsistencyInAuxLoop() ++ Error  - %s" % warn)
                                    self.report.setError()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__testDataConsistencyInAuxLoop() ++ Error  - %s" % warn)

                            # try to parse data without constraints

                            try:

                                aux_data = self.__nefT.check_data(sf_data, lp_category, key_items, data_items, allowed_tags, None)[0]

                                self.__aux_data[content_subtype].append({'sf_framecode': sf_framecode, 'category': lp_category, 'data': aux_data})

                                if content_subtype == 'spectral_peak':
                                    self.__testDataConsistencyInAuxLoopOfSpectralPeak(file_name, file_type, sf_framecode, num_dim, lp_category, aux_data)

                            except:
                                pass

                        except Exception as e:

                            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testDataConsistencyInAuxLoop() ++ Error  - %s" % str(e))
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__testDataConsistencyInAuxLoop() ++ Error  - %s" % str(e))

                    elif lp_category in self.linked_lp_categories[file_type][content_subtype]:

                        warn = "Unsupported %s loop category exists." % lp_category

                        self.report.warning.appendDescription('skipped_lp_category', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                        self.report.setWarning()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__testDataConsistencyInAuxLoop() ++ Warning  - %s\n" % warn)

                    else:

                        err = "%s loop category exists unexpectedly." % loop.category

                        self.report.error.appendDescription('format_issue', {'file_name': file_name, 'sf_framecode': sf_framecode, 'description': err})
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__testDataConsistencyInAuxLoop() ++ Error  - %s\n" % err)

        return self.report.getTotalErrors() == __errors

    def __testDataConsistencyInAuxLoopOfSpectralPeak(self, file_name, file_type, sf_framecode, num_dim, lp_category, aux_data):
        """ Perform consistency test on data of spectral peak loops.
        """

        content_subtype = 'spectral_peak'

        max_dim = num_dim + 1

        if (file_type == 'nef' and lp_category == '_nef_spectrum_dimension') or (file_type == 'nmr-star' and lp_category == '_Spectral_dim'):

            err = "The number of dimension %s and the number of rows %s are not matched." % (num_dim, len(aux_data))

            if len(aux_data) != num_dim:
                self.report.error.appendDescription('missing_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__testDataConsistencyInAuxLoopOfSpectralPeak() ++ Error  - %s\n" % err)

            try:

                min_points = []
                max_points = []

                for i in range(1, max_dim):

                    for sp_dim in aux_data:

                        if file_type == 'nef':

                            if sp_dim['dimension_id'] != i:
                                continue

                            first_point = sp_dim['value_first_point']
                            sp_width = sp_dim['spectral_width']
                            acq = sp_dim['is_acquisition']
                            abs = sp_dim['absolute_peak_positions']

                            if sp_dim['axis_unit'] == 'Hz':
                                sp_freq = sp_dim['spectrometer_frequency']
                                first_point /= sp_freq
                                sp_width /= sp_freq

                        else:

                            if sp_dim['ID'] != i:
                                continue

                            axis_unit = sp_dim['Sweep_width_units']
                            first_point = sp_dim['Value_first_point']
                            sp_width = sp_dim['Sweep_width']
                            acq = sp_dim['Acquisition']
                            abs = sp_dim['Absolute_peak_positions']

                            if sp_dim['Sweep_width_units'] == 'Hz':
                                sp_freq = sp_dim['Spectrometer_frequency']
                                first_point /= sp_freq
                                sp_width /= sp_freq

                        last_point = first_point - sp_width

                        min_point = last_point - (sp_width if abs else 0.0)
                        max_point = first_point + (sp_width if abs else 0.0)

                        min_points.append(min_point)
                        max_points.append(max_point)

                key_items = []
                for dim in range(1, max_dim):
                    for k in self.pk_key_items[file_type]:
                        _k = copy.copy(k)
                        if '%s' in k['name']:
                           _k['name'] = k['name'] % dim
                        key_items.append(_k)

                position_names = [k['name'] for k in key_items]
                index_tag = self.index_tags[file_type][content_subtype]

                lp_data = next((l['data'] for l in self.__lp_data[content_subtype] if l['sf_framecode'] == sf_framecode), None)

                if not lp_data is None:

                    for i in lp_data:
                        for j in range(num_dim):
                            position = i[position_names[j]]

                            if position < min_points[j] or position > max_points[j]:

                                err = '[Check row of %s %s] %s %s is out of range (min_position %s, max_position %s).' % (index_tag, i[index_tag], position_names[j], position, min_points[j], max_points[j])

                                self.report.error.appendDescription('anomalous_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write("+NmrDpUtility.__testDataConsistencyInAuxLoopOfSpectralPeak() ++ ValueError  - %s\n" % err)

            except Exception as e:

                self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testDataConsistencyInAuxLoopOfSpectralPeak() ++ Error  - %s" % str(e))
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__testDataConsistencyInAuxLoopOfSpectralPeak() ++ Error  - %s" % str(e))

        if (file_type == 'nef' and lp_category == '_nef_spectrum_dimension_transfer') or (file_type == 'nmr-star' and lp_category == '_Spectral_dim_transfer'):

            for i in aux_data:
                for name in [j['name'] for j in self.aux_key_items[file_type][content_subtype][lp_category]]:
                    if not i[name] in range(1, max_dim):

                        err = "%s '%s' must be one of %s." % (name, i[name], range(1, max_dim), lp_category)

                        self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__testDataConsistencyInAuxLoopOfSpectralPeak() ++ ValueError  - %s\n" % err)

    def __testSfTagConsistency(self):
        """ Perform consistency test on saveframe tags.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        if input_source_dic['content_subtype'] is None:
            return False

        __errors = self.report.getTotalErrors()

        for content_subtype in input_source_dic['content_subtype'].keys():

            sf_category = self.sf_categories[file_type][content_subtype]

            parent_keys = set()

            list_id = 1  # tentative parent key if not exists

            for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

                sf_framecode = sf_data.get_tag('sf_framecode')[0]

                if sf_data.tag_prefix != self.sf_tag_prefixes[file_type][content_subtype]:

                    err = "Saveframe tag prefix %s did not match with %s in saveframe %s." % (sf_data.tag_prefix, self.sf_tag_prefixes[file_type][content_subtype], sf_framecode)

                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testSfTagConsistency() ++ Error  - %s" % err)
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testSfTagConsistency() ++ Error  - %s\n" % err)

                    pass

                try:

                    sf_tag_data = self.__nefT.check_sf_tag(sf_data, self.sf_tag_items[file_type][content_subtype], self.sf_allowed_tags[file_type][content_subtype],
                                                            enforce_non_zero=True, enforce_sign=True, enforce_enum=True)

                    self.__testParentChildRelation(file_name, file_type, content_subtype, parent_keys, list_id, sf_framecode, sf_tag_data)

                except LookupError as e:

                    self.report.error.appendDescription('missing_mandatory_item', {'file_name': file_name, 'sf_framecode': sf_framecode, 'description': str(e).strip("'")})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testSfTagConsistency() ++ LookupError  - %s" % str(e))

                except ValueError as e:

                    self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'description': str(e).strip("'")})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testSfTagConsistency() ++ ValueError  - %s" % str(e))

                except UserWarning as e:

                    warns = str(e).strip("'").split('\n')

                    for warn in warns:

                        if warn == '':
                            continue

                        zero = warn.startswith('[Zero value error] ')
                        nega = warn.startswith('[Negative value error] ')
                        enum = warn.startswith('[Enumeration error] ')

                        if zero or nega or enum:

                            if zero:
                                warn = warn[19:]
                            elif nega:
                                warn = warn[23:]
                            else:
                                warn = warn[20:]

                            self.report.warning.appendDescription('missing_data' if zero else ('unusual_data' if nega else 'enum_failure'), {'file_name': file_name, 'sf_framecode': sf_framecode, 'description': warn})
                            self.report.setWarning()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__testSfTagConsistency() ++ Warning  - %s\n" % warn)

                        else:

                            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testSfTagConsistency() ++ Error  - %s" % warn)
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__testSfTagConsistency() ++ Error  - %s" % warn)

                    # try to parse data without constraints

                    try:

                        sf_tag_data = self.__nefT.check_sf_tag(sf_data, self.sf_tag_items[file_type][content_subtype], self.sf_allowed_tags[file_type][content_subtype],
                                                                enfoce_non_zero=False, enforce_sign=False, enforce_enum=False)

                        self.__testParentChildRelation(file_name, file_type, content_subtype, parent_keys, list_id, sf_framecode, sf_tag_data)

                    except:
                        pass

                except Exception as e:

                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testSfTagConsistency() ++ Error  - %s" % str(e))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testSfTagConsistency() ++ Error  - %s" % str(e))

                list_id += 1

        return self.report.getTotalErrors() == __errors

    def __testParentChildRelation(self, file_name, file_type, content_subtype, parent_keys, list_id, sf_framecode, sf_tag_data):
        """ Perform consistency test on saveframe category and loop category relationship of interesting loops.
        """

        if file_type == 'nef' or content_subtype == 'entry_info':
            return True

        __errors = self.report.getTotalErrors()

        key_base = self.sf_tag_prefixes['nmr-star'][content_subtype].lstrip('_')

        parent_key_name = key_base + '.ID'
        child_key_name = key_base + '_ID'

        if parent_key_name in sf_tag_data:
            parent_key = sf_tag_data[parent_key_name]
        else:
            parent_key = list_id

        if parent_key in parent_keys:

            err = "%s '%s' must be unique." % (parent_key_name, parent_key)

            self.report.error.appendDescription('duplicated_index', {'file_name': file_name, 'sf_framecode': sf_framecode, 'description': err})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__testParentChildRelation() ++ KeyError  - %s\n" % err)

        index_tag = self.index_tags[file_type][content_subtype]
        lp_category = self.lp_categories[file_type][content_subtype]

        try:

            lp_data = next((l['data'] for l in self.__lp_data[content_subtype] if l['sf_framecode'] == sf_framecode), None)

            if not lp_data is None:

                for i in lp_data:
                    if child_key_name in i and i[child_key_name] != parent_key:

                        err = '[Check row of %s %s] %s %s must be %s.' % (index_tag, i[index_tag], child_key_name, i[child_key_name], parent_key)

                        self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__testParentChildRelation() ++ ValueError  - %s\n" % err)

            for lp_category in self.aux_lp_categories[file_type][content_subtype]:

                aux_data = next((l['data'] for l in self.__aux_data[content_subtype] if l['sf_framecode'] == sf_framecode and l['category'] == lp_category), None)

                if not aux_data is None:
                    for i in aux_data:
                        if child_key_name in i and i[child_key_name] != parent_key:

                            err = '[Check row of %s %s] %s %s must be %s.' % (index_tag, i[index_tag], child_key_name, i[child_key_name], parent_key)

                            self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__testParentChildRelation() ++ ValueError  - %s\n" % err)

        except Exception as e:

                self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testParentChildRelation() ++ Error  - %s" % str(e))
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__testParentChildRelation() ++ Error  - %s" % str(e))

        return self.report.getTotalErrors() == __errors

    def __validateCSValue(self):
        """ Validate assigned chemical shift value based on BMRB chemical shift statistics.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        if input_source_dic['content_subtype'] is None:
            return False

        __errors = self.report.getTotalErrors()

        content_subtype = 'chem_shift'

        if not content_subtype in input_source_dic['content_subtype'].keys():

            err = "Assigned chemical shift loop did not exist in %s file." % file_name

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__validateCSValue() ++ Error  - %s" % err)
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ Error  - %s\n" % err)

            return False

        sf_category = self.sf_categories[file_type][content_subtype]
        lp_category = self.lp_categories[file_type][content_subtype]

        item_names = self.item_names_in_cs_loop[file_type]
        chain_id_name = item_names['chain_id']
        seq_id_name = item_names['seq_id']
        comp_id_name = item_names['comp_id']
        atom_id_name = item_names['atom_id']
        value_name = item_names['value']
        ambig_code_name = 'Ambiguity_code' # NMR-STAR specific

        index_tag = self.index_tags[file_type][content_subtype]
        max_cs_err = self.chem_shift_error['max_exclusive']

        for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

            sf_framecode = sf_data.get_tag('sf_framecode')[0]

            try:

                lp_data = next(l['data'] for l in self.__lp_data[content_subtype] if l['sf_framecode'] == sf_framecode)

                chk_row_tmp = "[Check row of {0} %s, {1} %s, {2} %s, {3} %s".format(chain_id_name, seq_id_name, comp_id_name, atom_id_name)
                row_tmp = "{0} %s, {1} %s, {2} %s, {3} %s".format(chain_id_name, seq_id_name, comp_id_name, atom_id_name)

                methyl_cs_vals = {}

                for i in lp_data:
                    chain_id = i[chain_id_name]
                    seq_id = i[seq_id_name]
                    comp_id = i[comp_id_name]
                    atom_id = i[atom_id_name]
                    value = i[value_name]

                    if file_type == 'nef':
                        _atom_id, ambig_code, details = self.__nefT.get_nmrstar_atom(comp_id, atom_id, leave_unmatched=True)

                        if len(_atom_id) == 0:
                            continue

                        if len(_atom_id) == 1 and atom_id == _atom_id[0]:
                            atom_id_ = atom_id
                            atom_name = atom_id

                            if not details is None:
                                atom_name += ', besides that, ' + details.rstrip('.')

                        else:
                            atom_name = atom_id + ' (e.g. '

                            for atom_id_ in _atom_id:
                                atom_name += atom_id_ + ' '

                            atom_name = atom_name.rstrip() + ')'

                            # representative atom id
                            atom_id_ = _atom_id[0]

                    else:
                        atom_id_ = atom_id
                        atom_name = atom_id

                    one_letter_code = self.__get1LetterCode(comp_id)

                    has_cs_stat = False

                    # non-standard residue
                    if one_letter_code == 'X':

                        neighbor_comp_ids = set([j[comp_id_name] for j in lp_data if j[chain_id_name] == chain_id and abs(j[seq_id_name] - seq_id) < 3 and j[seq_id_name] != seq_id])

                        polypeptide_like = False

                        for comp_id2 in neighbor_comp_ids:
                            polypeptide_like |= self.__csStat.getTypeOfCompId(comp_id2)[0]

                        for cs_stat in self.__csStat.get(comp_id):

                            if cs_stat['atom_id'] == atom_id_:
                                min_value = cs_stat['min']
                                max_value = cs_stat['max']
                                avg_value = cs_stat['avg']
                                std_value = cs_stat['std']

                                has_cs_stat = True

                                if atom_id.startswith('H') and 'methyl' in cs_stat['desc']:
                                    methyl_cs_key = "%s %04d %s" % (chain_id, seq_id, atom_id[:-1])

                                    if not methyl_cs_key in methyl_cs_vals:
                                        methyl_cs_vals[methyl_cs_key] = value

                                    elif value != methyl_cs_vals[methyl_cs_key]:

                                        err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name) + '] Chemical shift values in the same methyl group %s %s vs %s are inconsistent.' %\
                                              (value_name, value, methyl_cs_vals[methyl_cs_key])

                                        self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError  - %s\n" % err)

                                        break

                                if std_value is None:

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name) + '] Insufficient chemical shift statistics on comp_id %s, atom_id %s is available to verify %s %s (avg %s).' %\
                                           (comp_id, atom_name, value_name, value, avg_value)

                                    self.report.warning.appendDescription('unusual_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ Warning  - %s\n" % warn)

                                    break

                                z_score = (value - avg_value) / std_value

                                if self.__csStat.hasEnoughStat(comp_id, polypeptide_like):
                                    tolerance = std_value

                                    if (value < min_value - tolerance or value > max_value + tolerance) and abs(z_score) > 7.5:

                                        err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name) + '] %s %s (chain_id %s, seq_id %s, comp_id %s, atom_id %s) is out of range (avg %s, std %s, min %s, max %s, Z_score %.2f).' %\
                                              (value_name, value, chain_id, seq_id, comp_id, atom_name, avg_value, std_value, min_value, max_value, z_score)

                                        self.report.error.appendDescription('anomalous_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError  - %s\n" % err)

                                    elif abs(z_score) > 7.5:

                                        warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name) + '] %s %s (chain_id %s, seq_id %s, comp_id %s, atom_id %s) must be verified (avg %s, std %s, min %s, max %s, Z_score %.2f).' %\
                                               (value_name, value, chain_id, seq_id, comp_id, atom_name, avg_value, std_value, min_value, max_value, z_score)

                                        self.report.warning.appendDescription('suspicious_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ Warning  - %s\n" % warn)

                                    elif abs(z_score) > 5.3:

                                        warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name) + '] %s %s (chain_id %s, seq_id %s, comp_id %s, atom_id %s) should be verified (avg %s, std %s, min %s, max %s, Z_score %.2f).' %\
                                               (value_name, value, chain_id, seq_id, comp_id, atom_name, avg_value, std_value, min_value, max_value, z_score)

                                        self.report.warning.appendDescription('unusual_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ Warning  - %s\n" % warn)

                                    elif not cs_stat['primary']:

                                        warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name) + '] %s %s is remarkable assignment (appearance_rate %s %%).' %\
                                               (value_name, value, cs_stat['norm_freq'] * 100.0)

                                        self.report.warning.appendDescription('remarkable_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ Warning  - %s\n" % warn)

                                else:
                                    tolerance = std_value * 10.0

                                    if (value < min_value - tolerance or value > max_value + tolerance) and abs(z_score) > 10.0:

                                        err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name) + '] %s %s (chain_id %s, seq_id %s, comp_id %s, atom_id %s) is out of range (avg %s, std %s, min %s, max %s, Z_score %.2f).' %\
                                              (value_name, value, chain_id, seq_id, comp_id, atom_name, avg_value, std_value, min_value, max_value, z_score)

                                        self.report.error.appendDescription('anomalous_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError  - %s\n" % err)

                                    elif abs(z_score) > 10.0:

                                        warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name) + '] %s %s (chain_id %s, seq_id %s, comp_id %s, atom_id %s) must be verified (avg %s, std %s, min %s, max %s, Z_score %.2f).' %\
                                               (value_name, value, chain_id, seq_id, comp_id, atom_name, avg_value, std_value, min_value, max_value, z_score)

                                        self.report.warning.appendDescription('suspicious_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ Warning  - %s\n" % warn)

                                break

                    # standard residue
                    else:

                        for cs_stat in self.__csStat.get(comp_id, self.report.isDiamagnetic()):

                            if cs_stat['atom_id'] == atom_id_:
                                min_value = cs_stat['min']
                                max_value = cs_stat['max']
                                avg_value = cs_stat['avg']
                                std_value = cs_stat['std']

                                has_cs_stat = True

                                if atom_id.startswith('H') and 'methyl' in cs_stat['desc']:
                                    methyl_cs_key = "%s %04d %s" % (chain_id, seq_id, atom_id[:-1])

                                    if not methyl_cs_key in methyl_cs_vals:
                                        methyl_cs_vals[methyl_cs_key] = value

                                    elif value != methyl_cs_vals[methyl_cs_key]:

                                        err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name) + '] Chemical shift values in the same methyl group %s %s vs %s are inconsistent.' %\
                                              (value_name, value, methyl_cs_vals[methyl_cs_key])

                                        self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError  - %s\n" % err)

                                        break

                                if std_value is None:

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name) + '] Insufficient chemical shift statistics on comp_id %s, atom_id %s is available to verify %s %s (avg %s).' %\
                                           (comp_id, atom_name, value_name, value, avg_value)

                                    self.report.warning.appendDescription('unusual_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ Warning  - %s\n" % warn)

                                    break

                                z_score = (value - avg_value) / std_value
                                tolerance = std_value / 10.0

                                if (value < min_value - tolerance or value > max_value + tolerance) and abs(z_score) > 5.0:

                                    err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name) + '] %s %s (chain_id %s, seq_id %s, comp_id %s, atom_id %s) is out of range (avg %s, std %s, min %s, max %s, Z_score %.2f).' %\
                                          (value_name, value, chain_id, seq_id, comp_id, atom_name, avg_value, std_value, min_value, max_value, z_score)

                                    self.report.error.appendDescription('anomalous_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                    self.report.setError()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError  - %s\n" % err)

                                elif abs(z_score) > 5.0:

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name) + '] %s %s (chain_id %s, seq_id %s, comp_id %s, atom_id %s) must be verified (avg %s, std %s, min %s, max %s, Z_score %.2f).' %\
                                           (value_name, value, chain_id, seq_id, comp_id, atom_name, avg_value, std_value, min_value, max_value, z_score)

                                    self.report.warning.appendDescription('suspicious_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ Warning  - %s\n" % warn)

                                elif abs(z_score) > 3.6:

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name) + '] %s %s (chain_id %s, seq_id %s, comp_id %s, atom_id %s) should be verified (avg %s, std %s, min %s, max %s, Z_score %.2f).' %\
                                           (value_name, value, chain_id, seq_id, comp_id, atom_name, avg_value, std_value, min_value, max_value, z_score)

                                    self.report.warning.appendDescription('unusual_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ Warning  - %s\n" % warn)

                                elif not cs_stat['primary']:

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name) + '] %s %s is remarkable assignment (appearance_rate %s %%).' %\
                                           (value_name, value, cs_stat['norm_freq'] * 100.0)

                                    self.report.warning.appendDescription('remarkable_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ Warning  - %s\n" % warn)

                                break

                    if not has_cs_stat:

                        warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name) + '] No chemical shift statistics is available to verify %s %s.' %\
                               (value_name, value)

                        self.report.warning.appendDescription('unusual_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                        self.report.setWarning()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ Warning  - %s\n" % warn)

                    # check ambiguity code
                    if file_type == 'nmr-star' and ambig_code_name in i:
                        ambig_code = i[ambig_code_name]

                        if ambig_code in self.empty_value or ambig_code == 1:
                            continue

                        allowed_ambig_code = self.__csStat.getMaxAmbigCodeWoSetId(comp_id, atom_id)

                        if ambig_code == 2 or ambig_code == 3:

                            ambig_code_desc = 'ambiguity of geminal atoms or geminal methyl proton groups' if ambig_code == 2 else 'aromatic atoms on opposite sides of symmetrical rings'

                            if ambig_code != allowed_ambig_code:

                                err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) + '] Invalid %s %s (allowed ambig_code %s) exists.' %\
                                      (ambig_code_name, ambig_code, [1, allowed_ambig_code, 4, 5, 6, 9])

                                self.report.error.appendDescription('invalid_ambiguity_code', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError - %s\n" % err)

                            atom_id2 = self.__csStat.getGeminalAtom(comp_id, atom_id)

                            try:

                                ambig_code2 = next(j[ambig_code_name] for j in lp_data if j[chain_id_name] == chain_id and j[seq_id_name] == seq_id and j[comp_id_name] == comp_id and j[atom_id_name] == atom_id2)

                                if ambig_code2 != ambig_code:

                                    err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) + '] %s %s indicates %s. However, %s %s of %s %s is inconsistent.' %\
                                          (ambig_code_name, ambig_code, ambig_code_desc, ambig_code_name, ambig_code2, atom_id_name, atom_id2)

                                    self.report.error.appendDescription('invalid_ambiguity_code', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                    self.report.setError()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError - %s\n" % err)

                            except StopIteration:
                                pass
                                """
                                warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) + '] %s %s indicates %s. However, row of %s %s of the same residue was not found.' %\
                                       (ambig_code_name, ambig_code, ambig_code_desc, atom_id_name, atom_id2)

                                self.report.warning.appendDescription('bad_ambiguity_code', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                                self.report.setWarning()

                                if self.__verbose:
                                    self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ Warning - %s\n" % warn)
                                """

                        elif ambig_code in [4, 5, 6, 9]:

                            ambig_set_id_name = 'Ambiguity_set_ID'

                            if not ambig_set_id_name in i:

                                err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) + '] %s %s requires %s loop tag.' %\
                                      (ambig_code_name, ambig_code, ambig_set_id_name)

                                self.report.error.appendDescription('missing_mandatory_item', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ LookupError  - %s\n" % err)

                            else:

                                ambig_set_id = i[ambig_set_id_name]

                                if ambig_set_id in self.empty_value:

                                    err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) + '] %s %s requires %s value.' %\
                                          (ambig_code_name, ambig_code, ambig_set_id_name)

                                    self.report.error.appendDescription('missing_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                    self.report.setError()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError  - %s\n" % err)

                                else:

                                    ambig_set = [j for j in lp_data if j[ambig_set_id_name] == ambig_set_id and j != i]

                                    if len(ambig_set) == 0:

                                        err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) + '] %s %s requires other rows sharing %s %s.' %\
                                              (ambig_code_name, ambig_code, ambig_set_id_name, ambig_set_id)

                                        self.report.error.appendDescription('missing_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ LookupError  - %s\n" % err)

                                    # Intra-residue ambiguities
                                    elif ambig_code == 4:

                                        for j in ambig_set:
                                            chain_id2 = j[chain_id_name]
                                            seq_id2 = j[seq_id_name]
                                            comp_id2 = j[comp_id_name]
                                            atom_id2 = j[atom_id_name]

                                            if (chain_id2 != chain_id or seq_id2 != seq_id or comp_id2 != comp_id) and atom_id < atom_id2:

                                                err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) +\
                                                      ', %s %s, %s %s] It indicates intra-residue ambiguities. However, row of ' % (ambig_code_name, ambig_code, ambig_set_id_name, ambig_set_id) +\
                                                      row_tmp % (chain_id2, seq_id2, comp_id2, atom_id2) + ' exists.'

                                                self.report.error.appendDescription('invalid_ambiguity_code', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                                self.report.setError()

                                                if self.__verbose:
                                                    self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError - %s\n" % err)

                                    # Inter-residue ambiguities
                                    elif ambig_code == 5:

                                        for j in ambig_set:
                                            chain_id2 = j[chain_id_name]
                                            seq_id2 = j[seq_id_name]
                                            comp_id2 = j[comp_id_name]
                                            atom_id2 = j[atom_id_name]

                                            if ((chain_id2 != chain_id and chain_id < chain_id2) or (seq_id2 == seq_id and atom_id < atom_id2)):

                                                err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) +\
                                                      ', %s %s, %s %s] It indicates inter-residue ambiguities. However, row of ' % (ambig_code_name, ambig_code, ambig_set_id_name, ambig_set_id) +\
                                                      row_tmp % (chain_id2, seq_id2, comp_id2, atom_id2) + ' exists.'

                                                self.report.error.appendDescription('invalid_ambiguity_code', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                                self.report.setError()

                                                if self.__verbose:
                                                    self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError - %s\n" % err)

                                    # Inter-molecular ambiguities
                                    elif ambig_code == 6:

                                        for j in ambig_set:
                                            chain_id2 = j[chain_id_name]
                                            seq_id2 = j[seq_id_name]
                                            comp_id2 = j[comp_id_name]
                                            atom_id2 = j[atom_id_name]
                                            value2 = j[value_name]

                                            if chain_id2 == chain_id and (seq_id < seq_id2 or (seq_id == seq_id2 and atom_id < atom_id2)):

                                                err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) +\
                                                      ', %s %s, %s %s] It indicates inter-molecular ambiguities. However, row of ' % (ambig_code_name, ambig_code, ambig_set_id_name, ambig_set_id) +\
                                                      row_tmp % (chain_id2, seq_id2, comp_id2, atom_id2) + ' exists.'

                                                self.report.error.appendDescription('invalid_ambiguity_code', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                                self.report.setError()

                                                if self.__verbose:
                                                    self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError - %s\n" % err)

                                    for j in ambig_set:
                                        chain_id2 = j[chain_id_name]
                                        seq_id2 = j[seq_id_name]
                                        comp_id2 = j[comp_id_name]
                                        atom_id2 = j[atom_id_name]
                                        value2 = j[value_name]

                                        if atom_id[0] != atom_id2[0] and atom_id < atom_id2:

                                            err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) +\
                                                  ', %s %s, %s %s] However, observation nucleus of ' % (ambig_code_name, ambig_code, ambig_set_id_name, ambig_set_id) +\
                                                  row_tmp % (chain_id2, seq_id2, comp_id2, atom_id2) + ' sharing the same %s differs.' % ambig_set_id_name

                                            self.report.error.appendDescription('invalid_ambiguity_code', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                            self.report.setError()

                                            if self.__verbose:
                                                self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError - %s\n" % err)

                                        elif abs(value2 - value) > max_cs_err and value < value2:

                                            err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) +\
                                                  ', %s %s, %s %s, %s %s] However, %s %s of ' % (value_name, value, ambig_code_name, ambig_code, ambig_set_id_name, ambig_set_id, value_name, value2) +\
                                                  row_tmp % (chain_id2, seq_id2, comp_id2, atom_id2) +\
                                                  'differs by %s (tolerance %s).' % (value2 - value, max_cs_err)

                                            self.report.error.appendDescription('invalid_ambiguity_code', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                            self.report.setError()

                                            if self.__verbose:
                                                self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError - %s\n" % err)

                        else:

                            err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) + '] Invalid ambiguity code %s (allowed ambig_code %s) exists.' %\
                                  (ambig_code, self.bmrb_ambiguity_codes)

                            self.report.error.appendDescription('invalid_ambiguity_code', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError - %s\n" % err)

            except StopIteration:

                err = "Assigned chemical shifts of saveframe %s did not parsed properly. Please fix problems reported." % sf_framecode

                self.report.error.appendDescription('missing_mandatory_content', {'file_name': file_name, 'description': err})
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ Error  - %s\n" % err)

            except Exception as e:
                self.report.error.appendDescription('internal_error', "+NmrDpUtility.__validateCSValue() ++ Error  - %s" % str(e))
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ Error  - %s" % str(e))

        return self.report.getTotalErrors() == __errors

    def __testCSValueConsistencyInPkLoop(self):
        """ Perform consistency test on peak position and assignment of spectral peaks.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        if input_source_dic['content_subtype'] is None:
            return False

        content_subtype = 'spectral_peak'

        if not content_subtype in input_source_dic['content_subtype'].keys():
            return True

        __errors = self.report.getTotalErrors()

        sf_category = self.sf_categories[file_type][content_subtype]
        lp_category = self.lp_categories[file_type][content_subtype]

        cs_item_names = self.item_names_in_cs_loop[file_type]
        cs_chain_id_name = cs_item_names['chain_id']
        cs_seq_id_name = cs_item_names['seq_id']
        cs_comp_id_name = cs_item_names['comp_id']
        cs_atom_id_name = cs_item_names['atom_id']
        cs_value_name = cs_item_names['value']
        cs_error_name = cs_item_names['error']
        cs_atom_type = cs_item_names['atom_type']
        cs_iso_number = cs_item_names['isotope_number']

        for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

            sf_framecode = sf_data.get_tag('sf_framecode')[0]
            cs_list = sf_data.get_tag(self.cs_list_sf_tag_name[file_type])[0]

            try:

                cs_data = next(l['data'] for l in self.__lp_data['chem_shift'] if l['sf_framecode'] == cs_list)

            except StopIteration:

                err = "Assigned chemical shifts are mandatory. Referred saveframe %s did not exist." % cs_list

                self.report.error.appendDescription('missing_mandatory_content', {'file_name': file_name, 'sf_framecode': sf_framecode, 'description': err})
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__testCSValueConsistencyInPkLoop() ++ Error  - %s\n" % err)

                    continue

            try:

                _num_dim = sf_data.get_tag(self.num_dim_items[file_type])[0]
                num_dim = int(_num_dim)

                if not num_dim in range(1, self.lim_num_dim):
                    raise ValueError()

            except ValueError: # raised error already at __testIndexConsistency()
                return False

            max_dim = num_dim + 1

            aux_data = next((l['data'] for l in self.__aux_data[content_subtype] if l['sf_framecode'] == sf_framecode and l['category'] == self.aux_lp_categories[file_type][content_subtype][0]), None)

            axis_codes = []
            abs_pk_pos = []
            sp_widths = []
            if not aux_data is None:
                for i in range(1, max_dim):
                    for sp_dim in aux_data:
                        if file_type == 'nef':
                            if sp_dim['dimension_id'] != i:
                                continue
                            axis_codes.append(sp_dim['axis_code'])
                            abs_pk_pos.append(sp_dim['absolute_peak_positions'])
                            sp_width = sp_dim['spectral_width']
                            if sp_dim['axis_unit'] == 'Hz':
                                sp_freq = sp_dim['spectrometer_frequency']
                                sp_width /= sp_freq
                            sp_widths.append(sp_width)
                        else:
                            if sp_dim['ID'] != i:
                                continue
                            axis_codes.append(sp_dim['Axis_code'])
                            abs_pk_pos.append(sp_dim['Absolute_peak_positions'])
                            sp_width = sp_dim['Sweep_width']
                            if sp_dim['Sweep_width_units'] == 'Hz':
                                sp_freq = sp_dim['Spectrometer_frequency']
                                sp_width /= sp_freq
                            sp_widths.append(sp_width)
            else:
                for i in range(num_dim):
                    abs_pk_pos.append(False)

            aux_data = next((l['data'] for l in self.__aux_data[content_subtype] if l['sf_framecode'] == sf_framecode and l['category'] == self.aux_lp_categories[file_type][content_subtype][1]), None)

            onebond = [[False] * num_dim for i in range(num_dim)]
            if not aux_data is None:
                for sp_dim_trans in aux_data:
                    if file_type == 'nef':
                        if sp_dim_trans['transfer_type'] == 'onebond':
                            dim_1 = sp_dim_trans['dimension_1']
                            dim_2 = sp_dim_trans['dimension_2']
                            onebond[dim_1 - 1][dim_2 - 1] = True
                            onebond[dim_2 - 1][dim_1 - 1] = True
                    else:
                        if sp_dim_trans['Type'] == 'onebond':
                            dim_1 = sp_dim_trans['Spectral_dim_ID_1']
                            dim_2 = sp_dim_trans['Spectral_dim_ID_2']
                            onebond[dim_1 - 1][dim_2 - 1] = True
                            onebond[dim_2 - 1][dim_1 - 1] = True

            jcoupling = [[False] * num_dim for i in range(num_dim)]
            if not aux_data is None:
                for sp_dim_trans in aux_data:
                    if file_type == 'nef':
                        if sp_dim_trans['transfer_type'].startswith('j'):
                            dim_1 = sp_dim_trans['dimension_1']
                            dim_2 = sp_dim_trans['dimension_2']
                            jcoupling[dim_1 - 1][dim_2 - 1] = True
                            jcoupling[dim_2 - 1][dim_1 - 1] = True
                    else:
                        if sp_dim_trans['Type'].startswith('j'):
                            dim_1 = sp_dim_trans['Spectral_dim_ID_1']
                            dim_2 = sp_dim_trans['Spectral_dim_ID_2']
                            jcoupling[dim_1 - 1][dim_2 - 1] = True
                            jcoupling[dim_2 - 1][dim_1 - 1] = True

            relayed = [[False] * num_dim for i in range(num_dim)]
            if not aux_data is None:
                for sp_dim_trans in aux_data:
                    if file_type == 'nef':
                        if sp_dim_trans['transfer_type'].startswith('relayed'):
                            dim_1 = sp_dim_trans['dimension_1']
                            dim_2 = sp_dim_trans['dimension_2']
                            relayed[dim_1 - 1][dim_2 - 1] = True
                            relayed[dim_2 - 1][dim_1 - 1] = True
                    else:
                        if sp_dim_trans['Type'].startswith('relayed'):
                            dim_1 = sp_dim_trans['Spectral_dim_ID_1']
                            dim_2 = sp_dim_trans['Spectral_dim_ID_2']
                            relayed[dim_1 - 1][dim_2 - 1] = True
                            relayed[dim_2 - 1][dim_1 - 1] = True

            item_names = []
            for dim in range(1, max_dim):
                _d = {}
                for k, v in self.item_names_in_pk_loop[file_type].items():
                    if '%s' in v:
                        v = v % dim
                    _d[k] = v
                item_names.append(_d)

            chain_id_names = []
            seq_id_names = []
            comp_id_names = []
            atom_id_names = []
            position_names = []

            for d in range(num_dim):
                chain_id_names.append(item_names[d]['chain_id'])
                seq_id_names.append(item_names[d]['seq_id'])
                comp_id_names.append(item_names[d]['comp_id'])
                atom_id_names.append(item_names[d]['atom_id'])
                position_names.append(item_names[d]['position'])

            index_tag = self.index_tags[file_type][content_subtype]
            max_cs_err = self.chem_shift_error['max_exclusive']

            try:

                lp_data = next((l['data'] for l in self.__lp_data[content_subtype] if l['sf_framecode'] == sf_framecode), None)

                if not lp_data is None:

                    for i in lp_data:
                        for d in range(num_dim):
                            chain_id = i[chain_id_names[d]]
                            if chain_id in self.empty_value:
                                continue

                            seq_id = i[seq_id_names[d]]
                            if seq_id in self.empty_value:
                                continue

                            comp_id = i[comp_id_names[d]]
                            if comp_id in self.empty_value:
                                continue

                            atom_id = i[atom_id_names[d]]
                            if atom_id in self.empty_value:
                                continue

                            position = i[position_names[d]]

                            try:

                                cs = next(j for j in cs_data if j[cs_chain_id_name] == chain_id and
                                                                j[cs_seq_id_name] == seq_id and
                                                                j[cs_comp_id_name] == comp_id and
                                                                j[cs_atom_id_name] == atom_id)

                                value = cs[cs_value_name]
                                error = cs[cs_error_name]

                                if error is None or error * 5.0 > max_cs_err:
                                    error = max_cs_err
                                else:
                                    error *= 5.0

                                if abs(position - value) > error:

                                    if not abs_pk_pos[d]:
                                        if position < value:
                                            while position < value:
                                                position += sp_widths[d]
                                        elif position > value:
                                            while position > value:
                                                position -= sp_widths[d]

                                    if abs(position - value) > error:

                                        err = '[Check row of %s %s] Peak position of spectral peak %s %s (%s %s, %s %s, %s %s, %s %s) in %s saveframe is inconsistent with the assigned chemical shift value %s (difference %s, tolerance %s) in %s saveframe.' %\
                                              (index_tag, i[index_tag], position_names[d], position, chain_id_names[d], chain_id, seq_id_names[d], seq_id, comp_id_names[d], comp_id, atom_id_names[d], atom_id, sf_framecode, value, position - value, error, cs_list)

                                        self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__testCSValueConsistencyInPkLoop() ++ ValueError  - %s\n" % err)

                                axis_code = str(cs[cs_iso_number]) + cs[cs_atom_type]

                                if axis_code != axis_codes[d]:

                                    err = '[Check row of %s %s] Assignment of spectral peak %s %s, %s %s, %s %s, %s %s is inconsistent with axis code %s vs %s.' %\
                                          (index_tag, i[index_tag], chain_id_names[d], chain_id, seq_id_names[d], seq_id, comp_id_names[d], comp_id, atom_id_names[d], atom_id, axis_code, axis_codes[d])

                                    self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                    self.report.setError()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__testCSValueConsistencyInPkLoop() ++ ValueError  - %s\n" % err)

                            except StopIteration:

                                err = '[Check row of %s %s] Assignment of spectral peak %s %s, %s %s, %s %s, %s %s was not found in assigned chemical shifts in %s saveframe.' %\
                                      (index_tag, i[index_tag], chain_id_names[d], chain_id, seq_id_names[d], seq_id, comp_id_names[d], comp_id, atom_id_names[d], atom_id, cs_list)

                                self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write("+NmrDpUtility.__testCSValueConsistencyInPkLoop() ++ ValueError  - %s\n" % err)

                            if True in onebond[d]:
                                for d2 in range(num_dim):
                                    if onebond[d][d2]:
                                        chain_id2 = i[chain_id_names[d2]]
                                        seq_id2 = i[seq_id_names[d2]]
                                        comp_id2 = i[comp_id_names[d2]]
                                        atom_id2 = i[atom_id_names[d2]]

                                        if not atom_id2 is None:
                                            diff = len(atom_id) != len(atom_id2)
                                            _atom_id = '_' + (atom_id[1:-1] if atom_id.startswith('H') and diff else atom_id[1:])
                                            _atom_id2 = '_' + (atom_id2[1:-1] if atom_id2.startswith('H') and diff else atom_id2[1:])

                                        if chain_id2 in self.empty_value or seq_id2 in self.empty_value or comp_id2 in self.empty_value or atom_id2 in self.empty_value or\
                                           (d < d2 and (chain_id2 != chain_id or seq_id2 != seq_id or comp_id2 != comp_id or _atom_id2 != _atom_id)):

                                            err = '[Check row of %s %s] Coherence transfer type is onebond. However, assignment of spectral peak is inconsistent with the type, (%s %s, %s %s, %s %s, %s %s) vs (%s %s, %s %s, %s %s, %s %s).' %\
                                                  (index_tag, i[index_tag], chain_id_names[d], chain_id, seq_id_names[d], seq_id, comp_id_names[d], comp_id, atom_id_names[d], atom_id,
                                                   chain_id_names[d2], chain_id2, seq_id_names[d2], seq_id2, comp_id_names[d2], comp_id2, atom_id_names[d2], atom_id2)

                                            self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                            self.report.setError()

                                            if self.__verbose:
                                                self.__lfh.write("+NmrDpUtility.__testCSValueConsistencyInPkLoop() ++ ValueError  - %s\n" % err)

                            if True in jcoupling[d]:
                                for d2 in range(num_dim):
                                    if jcoupling[d][d2]:
                                        chain_id2 = i[chain_id_names[d2]]
                                        seq_id2 = i[seq_id_names[d2]]
                                        comp_id2 = i[comp_id_names[d2]]
                                        atom_id2 = i[atom_id_names[d2]]

                                        if chain_id2 in self.empty_value or seq_id2 in self.empty_value or comp_id2 in self.empty_value or atom_id2 in self.empty_value or\
                                           (d < d2 and (chain_id2 != chain_id or abs(seq_id2 - seq_id) > 1)):

                                            err = '[Check row of %s %s] Coherence transfer type is jcoupling. However, assignment of spectral peak is inconsistent with the type, (%s %s, %s %s, %s %s, %s %s) vs (%s %s, %s %s, %s %s, %s %s).' %\
                                                  (index_tag, i[index_tag], chain_id_names[d], chain_id, seq_id_names[d], seq_id, comp_id_names[d], comp_id, atom_id_names[d], atom_id,
                                                   chain_id_names[d2], chain_id2, seq_id_names[d2], seq_id2, comp_id_names[d2], comp_id2, atom_id_names[d2], atom_id2)

                                            self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                            self.report.setError()

                                            if self.__verbose:
                                                self.__lfh.write("+NmrDpUtility.__testCSValueConsistencyInPkLoop() ++ ValueError  - %s\n" % err)

                            if True in relayed[d]:
                                for d2 in range(num_dim):
                                    if relayed[d][d2]:
                                        chain_id2 = i[chain_id_names[d2]]
                                        seq_id2 = i[seq_id_names[d2]]
                                        comp_id2 = i[comp_id_names[d2]]
                                        atom_id2 = i[atom_id_names[d2]]

                                        if chain_id2 in self.empty_value or seq_id2 in self.empty_value or comp_id2 in self.empty_value or atom_id2 in self.empty_value or\
                                           (d < d2 and (chain_id2 != chain_id or seq_id2 != seq_id or comp_id2 != comp_id or atom_id[0] != atom_id2[0])):

                                            err = '[Check row of %s %s] Coherence transfer type is relayed. However, assignment of spectral peak is inconsistent with the type, (%s %s, %s %s, %s %s, %s %s) vs (%s %s, %s %s, %s %s, %s %s).' %\
                                                  (index_tag, i[index_tag], chain_id_names[d], chain_id, seq_id_names[d], seq_id, comp_id_names[d], comp_id, atom_id_names[d], atom_id,
                                                   chain_id_names[d2], chain_id2, seq_id_names[d2], seq_id2, comp_id_names[d2], comp_id2, atom_id_names[d2], atom_id2)

                                            self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                            self.report.setError()

                                            if self.__verbose:
                                                self.__lfh.write("+NmrDpUtility.__testCSValueConsistencyInPkLoop() ++ ValueError  - %s\n" % err)

            except Exception as e:

                self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testCSValueConsistencyInPkLoop() ++ Error  - %s" % str(e))
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__testCSValueConsistencyInPkLoop() ++ Error  - %s" % str(e))

        return self.report.getTotalErrors() == __errors

    def __testRDCVector(self):
        """ Perform consistency test on RDC bond vectors.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        if input_source_dic['content_subtype'] is None:
            return False

        __errors = self.report.getTotalErrors()

        content_subtype = 'rdc_restraint'

        if not content_subtype in input_source_dic['content_subtype'].keys():
            return True

        sf_category = self.sf_categories[file_type][content_subtype]
        lp_category = self.lp_categories[file_type][content_subtype]

        item_names = self.item_names_in_rdc_loop[file_type]
        index_tag = self.index_tags[file_type][content_subtype]
        chain_id_1_name = item_names['chain_id_1']
        chain_id_2_name = item_names['chain_id_2']
        seq_id_1_name = item_names['seq_id_1']
        seq_id_2_name = item_names['seq_id_2']
        comp_id_1_name = item_names['comp_id_1']
        comp_id_2_name = item_names['comp_id_2']
        atom_id_1_name = item_names['atom_id_1']
        atom_id_2_name = item_names['atom_id_2']

        for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

            sf_framecode = sf_data.get_tag('sf_framecode')[0]

            try:

                lp_data = next((l['data'] for l in self.__lp_data[content_subtype] if l['sf_framecode'] == sf_framecode), None)

                if not lp_data is None:

                    for i in lp_data:
                        chain_id_1 = i[chain_id_1_name]
                        seq_id_1 = i[seq_id_1_name]
                        comp_id_1 = i[comp_id_1_name]
                        atom_id_1 = i[atom_id_1_name]
                        chain_id_2 = i[chain_id_2_name]
                        seq_id_2 = i[seq_id_2_name]
                        comp_id_2 = i[comp_id_2_name]
                        atom_id_2 = i[atom_id_2_name]

                        try:
                            self.atom_isotopes[atom_id_1[0]]
                            self.atom_isotopes[atom_id_2[0]]
                        except KeyError:

                            idx_msg = "[Check row of %s %s] " % (index_tag, i[index_tag])

                            err = "%sNon-magnetic susceptible spins appeared in RDC vector (chain_id_1 %s, seq_id_1 %s, comp_id_1 %s, atom_id_1 %s, chain_id_2 %s, seq_id_2 %s, comp_id_2 %s, atom_id_2 %s)." %\
                                  (idx_msg, chain_id_1, seq_id_1, comp_id_1, atom_id_1, chain_id_2, seq_id_2, comp_id_2, atom_id_2)

                            self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__testRDCVector() ++ Error  - %s\n" % err)

                        if chain_id_1 != chain_id_2:

                            idx_msg = "[Check row of %s %s] " % (index_tag, i[index_tag])

                            err = "%sInvalid inter-chain RDC vector (chain_id_1 %s, seq_id_1 %s, comp_id_1 %s, atom_id_1 %s, chain_id_2 %s, seq_id_2 %s, comp_id_2 %s, atom_id_2 %s) exists." %\
                                  (idx_msg, chain_id_1, seq_id_1, comp_id_1, atom_id_1, chain_id_2, seq_id_2, comp_id_2, atom_id_2)

                            self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__testRDCVector() ++ Error  - %s\n" % err)

                        elif abs(seq_id_1 - seq_id_2) > 1:

                            idx_msg = "[Check row of %s %s] " % (index_tag, i[index_tag])

                            err = "%sInvalid inter-residue RDC vector (chain_id_1 %s, seq_id_1 %s, comp_id_1 %s, atom_id_1 %s, chain_id_2 %s, seq_id_2 %s, comp_id_2 %s, atom_id_2 %s) exists." %\
                                  (idx_msg, chain_id_1, seq_id_1, comp_id_1, atom_id_1, chain_id_2, seq_id_2, comp_id_2, atom_id_2)

                            self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__testRDCVector() ++ Error  - %s\n" % err)

                        elif abs(seq_id_1 - seq_id_2) == 1:

                            if self.__csStat.getTypeOfCompId(comp_id_1)[0] and self.__csStat.getTypeOfCompId(comp_id_2)[0] and\
                               ((seq_id_1 < seq_id_2 and atom_id_1 == 'C' and atom_id_2 == 'N') or (seq_id_1 > seq_id_2 and atom_id_1 == 'N' and atom_id_2 == 'C')):
                                pass

                            else:
                                err = "%sInvalid inter-residue RDC vector (chain_id_1 %s, seq_id_1 %s, comp_id_1 %s, atom_id_1 %s, chain_id_2 %s, seq_id_2 %s, comp_id_2 %s, atom_id_2 %s) exists." %\
                                      (idx_msg, chain_id_1, seq_id_1, comp_id_1, atom_id_1, chain_id_2, seq_id_2, comp_id_2, atom_id_2)

                                self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write("+NmrDpUtility.__testRDCVector() ++ Error  - %s\n" % err)

                        elif atom_id_1 == atom_id_2:

                            idx_msg = "[Check row of %s %s] " % (index_tag, i[index_tag])

                            err = "%sZero RDC vector (chain_id_1 %s, seq_id_1 %s, comp_id_1 %s, atom_id_1 %s, chain_id_2 %s, seq_id_2 %s, comp_id_2 %s, atom_id_2 %s) exists." %\
                                  (idx_msg, chain_id_1, seq_id_1, comp_id_1, atom_id_1, chain_id_2, seq_id_2, comp_id_2, atom_id_2)

                            self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__testRDCVector() ++ Error  - %s\n" % err)

                        else:

                            self.__updateChemCompDict(comp_id_1)

                            if self.__last_comp_id_test: # matches with comp_id in CCD

                                try:
                                    next(b for b in self.__last_chem_comp_bonds if\
                                         ((b[self.__ccb_atom_id_1] == atom_id_1 and b[self.__ccb_atom_id_2] == atom_id_2) or\
                                          (b[self.__ccb_atom_id_1] == atom_id_2 and b[self.__ccb_atom_id_2] == atom_id_1)))
                                except StopIteration:

                                    idx_msg = "[Check row of %s %s] " % (index_tag, i[index_tag])

                                    warn = "%sMultiple bonds' RDC vector (chain_id_1 %s, seq_id_1 %s, comp_id_1 %s, atom_id_1 %s, chain_id_2 %s, seq_id_2 %s, comp_id_2 %s, atom_id_2 %s) exists." %\
                                           (idx_msg, chain_id_1, seq_id_1, comp_id_1, atom_id_1, chain_id_2, seq_id_2, comp_id_2, atom_id_2)

                                    self.report.warning.appendDescription('remarkable_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__testRDCVector() ++ Warning  - %s\n" % warn)

                                    pass

                            else: # raised warning already somewhere
                                pass

            except Exception as e:

                self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testRDCVector() ++ Error  - %s" % str(e))
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__testRDCVector() ++ Error  - %s" % str(e))

        return self.report.getTotalErrors() == __errors

    def __calculateStatsOfExptlData(self):
        """ Calculate statistics of experimental data.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']
        file_name = input_source_dic['file_name']

        if input_source_dic['content_subtype'] is None:
            return False

        __errors = self.report.getTotalErrors()

        seq_align_dic = self.report.sequence_alignment.get()

        stats = {}

        for content_subtype in input_source_dic['content_subtype'].keys():

            if content_subtype == 'entry_info' or content_subtype == 'poly_seq':
                continue

            sf_category = self.sf_categories[file_type][content_subtype]
            lp_category = self.lp_categories[file_type][content_subtype]

            asm = []

            list_id = 1

            for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

                sf_framecode = sf_data.get_tag('sf_framecode')[0]

                _list_id = list_id
                if file_type == 'nmr-star':
                    val = sf_data.get_tag('ID')
                    if len(val) > 0:
                        _list_id = int(val[0])

                lp_data = next((l['data'] for l in self.__lp_data[content_subtype] if l['sf_framecode'] == sf_framecode), None)

                ent = {'list_id': _list_id, 'sf_framecode': sf_framecode, 'number_of_rows': 0 if lp_data is None else len(lp_data)}

                if content_subtype == 'dist_restraint' or content_subtype == 'dihed_restraint' or content_subtype == 'rdc_restraint':

                    type = sf_data.get_tag('restraint_origin' if file_type == 'nef' else 'Constraint_type')
                    if len(type) > 0 and not type[0] in self.empty_value:
                        ent['exp_type'] = type[0]
                    else:
                        ent['exp_type'] = 'Unknown'

                elif content_subtype == 'spectral_peak':

                    type = sf_data.get_tag('experiment_type' if file_type == 'nef' else 'Experiment_type')
                    if len(type) > 0 and not type[0] in self.empty_value:
                        ent['exp_type'] = type[0]
                    else:
                        ent['exp_type'] = 'Unknown'

                if not lp_data is None:

                    if content_subtype == 'chem_shift' or content_subtype == 'dist_restraint' or content_subtype == 'dihed_restraint' or content_subtype == 'rdc_restraint' or content_subtype == 'spectral_peak':

                        sa_name = 'nmr_poly_seq_vs_' + content_subtype

                        if sa_name in seq_align_dic and not seq_align_dic[sa_name] is None:

                            low_sequence_coverage = ''

                            seq_coverage = []

                            for seq_align in seq_align_dic[sa_name]:

                                if seq_align['list_id'] == list_id:

                                    sc = {}
                                    sc['chain_id'] = seq_align['chain_id']
                                    sc['length'] = seq_align['length']
                                    sc['sequence_coverage'] = seq_align['sequence_coverage']

                                    if seq_align['sequence_coverage'] < self.low_sequence_coverage and seq_align['length'] > 1:
                                        if (not 'exp_type' in ent['exp_type']) or not ent['exp_type'] in ['disulfide bound', 'paramagnetic relaxation', 'symmetry', 'J-couplings']:
                                            low_sequence_coverage += 'coverage %s for chain_id %s, length %s, ' % (seq_align['sequence_coverage'], seq_align['chain_id'], seq_align['length'])

                                    seq_coverage.append(sc)

                            if len(seq_coverage) > 0:

                                ent['sequence_coverage'] = seq_coverage

                                if len(low_sequence_coverage) > 0:

                                    warn = 'Low sequence coverage of NMR experimental data was found (' + low_sequence_coverage[:-2] + ') in %s saveframe.' % sf_framecode

                                    self.report.warning.appendDescription('unsufficient_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': warn})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__calculateStatsOfExptlData() ++ Warning  - %s\n" % warn)

                            if content_subtype == 'chem_shift':

                                try:

                                    item_names = self.item_names_in_cs_loop[file_type]

                                    anomalous_errs = self.report.error.getValueListWithSf('anomalous_data', file_name, sf_framecode, key='Z_score')
                                    suspicious_warns = self.report.warning.getValueListWithSf('suspicious_data', file_name, sf_framecode, key='Z_score')
                                    unusual_warns = self.report.warning.getValueListWithSf('unusual_data', file_name, sf_framecode, key='Z_score')

                                    pattern = r'^' + item_names['value'] + r' ([+-]?([0-9]*[.])?[0-9]+) (.*) Z_score ([+-]?([0-9]*[.])?[0-9]+)\)\.$'

                                    p = re.compile(pattern)

                                    cs_ann = []

                                    if not anomalous_errs is None:

                                        for a_err in anomalous_errs:
                                            ann = {}
                                            ann['level'] = 'anomalous'
                                            ann['chain_id'] = a_err['row_location'][item_names['chain_id']]
                                            ann['seq_id'] = int(a_err['row_location'][item_names['seq_id']])
                                            ann['comp_id'] = a_err['row_location'][item_names['comp_id']]
                                            ann['atom_id'] = a_err['row_location'][item_names['atom_id']]
                                            g = p.search(a_err['description']).groups()
                                            ann['value'] = float(g[0])
                                            ann['z_score'] = float(g[3])

                                            comp_id = ann['comp_id']
                                            atom_id = ann['atom_id'].split(' ')[0]

                                            polypeptide_like = self.__csStat.getTypeOfCompId(comp_id)[0]

                                            if self.__csStat.hasEnoughStat(comp_id, polypeptide_like):
                                                non_rep_methyl_pros = self.__csStat.getNonRepresentativeMethylProtons(comp_id, excl_minor_atom=True, primary=polypeptide_like)

                                                if atom_id in non_rep_methyl_pros:
                                                    continue

                                            cs_ann.append(ann)

                                    if not suspicious_warns is None:

                                        for s_warn in suspicious_warns:
                                            ann = {}
                                            ann['level'] = 'suspicious'
                                            ann['chain_id'] = s_warn['row_location'][item_names['chain_id']]
                                            ann['seq_id'] = int(s_warn['row_location'][item_names['seq_id']])
                                            ann['comp_id'] = s_warn['row_location'][item_names['comp_id']]
                                            ann['atom_id'] = s_warn['row_location'][item_names['atom_id']]
                                            g = p.search(s_warn['description']).groups()
                                            ann['value'] = float(g[0])
                                            ann['z_score'] = float(g[3])

                                            comp_id = ann['comp_id']
                                            atom_id = ann['atom_id'].split(' ')[0]

                                            polypeptide_like = self.__csStat.getTypeOfCompId(comp_id)[0]

                                            if self.__csStat.hasEnoughStat(comp_id, polypeptide_like):
                                                non_rep_methyl_pros = self.__csStat.getNonRepresentativeMethylProtons(comp_id, excl_minor_atom=True, primary=polypeptide_like)

                                                if atom_id in non_rep_methyl_pros:
                                                    continue

                                            cs_ann.append(ann)

                                    if not unusual_warns is None:

                                        for u_warn in unusual_warns:
                                            ann = {}
                                            ann['level'] = 'unusual'
                                            ann['chain_id'] = u_warn['row_location'][item_names['chain_id']]
                                            ann['seq_id'] = int(u_warn['row_location'][item_names['seq_id']])
                                            ann['comp_id'] = u_warn['row_location'][item_names['comp_id']]
                                            ann['atom_id'] = u_warn['row_location'][item_names['atom_id']]
                                            g = p.search(u_warn['description']).groups()
                                            ann['value'] = float(g[0])
                                            ann['z_score'] = float(g[3])

                                            comp_id = ann['comp_id']
                                            atom_id = ann['atom_id'].split(' ')[0]

                                            polypeptide_like = self.__csStat.getTypeOfCompId(comp_id)[0]

                                            if self.__csStat.hasEnoughStat(comp_id, polypeptide_like):
                                                non_rep_methyl_pros = self.__csStat.getNonRepresentativeMethylProtons(comp_id, excl_minor_atom=True, primary=polypeptide_like)

                                                if atom_id in non_rep_methyl_pros:
                                                    continue

                                            cs_ann.append(ann)

                                except Exception as e:

                                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__calculateStatsOfExptlData() ++ Error  - %s" % str(e))
                                    self.report.setError()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__calculateStatsOfExptlData() ++ Error  - %s" % str(e))

                                self.__calculateStatsOfAssignedChemShift(sf_framecode, lp_data, cs_ann, ent)

                            elif content_subtype == 'dist_restraint':
                                self.__calculateStatsOfDistanceRestraint(sf_framecode, lp_data, ent)

                            elif content_subtype == 'dihed_restraint':
                                self.__calculateStatsOfDihedralRestraint(lp_data, ent)

                            elif content_subtype == 'rdc_restraint':
                                self.__calculateStatsOfRdcRestraint(lp_data, ent)

                            elif content_subtype == 'spectral_peak':

                                try:

                                    _num_dim = sf_data.get_tag(self.num_dim_items[file_type])[0]
                                    num_dim = int(_num_dim)

                                    if not num_dim in range(1, self.lim_num_dim):
                                        raise ValueError()

                                except ValueError: # raised error already at __testIndexConsistency()
                                    continue

                                self.__calculateStatsOfSpectralPeak(num_dim, lp_data, ent)

                    else:

                        err = "Module for calculation of statistics on content subtype %s were not found." % content_subtype

                        self.report.error.appendDescription('internal_error', "+NmrDpUtility.__calculateStatsOfExptlData() ++ Error  - %s" % err)
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__calculateStatsOfExptlData() ++ Error  - %s\n" % err)

                        continue

                has_err = self.report.error.exists(file_name, sf_framecode)
                has_warn = self.report.warning.exists(file_name, sf_framecode)

                if has_err:
                    status = 'Error'
                    ent['error_descriptions'] = self.report.error.getCombinedDescriptions(file_name, sf_framecode)
                    if has_warn:
                        ent['warning_descriptions'] = self.report.warning.getCombinedDescriptions(file_name, sf_framecode)
                elif has_warn:
                    status = 'Warning'
                    ent['warning_descriptions'] = self.report.warning.getCombinedDescriptions(file_name, sf_framecode)
                else:
                    status = 'OK'

                ent['status'] = status

                asm.append(ent)

                list_id += 1

            if len(asm) > 0:
                stats[content_subtype] = asm

        input_source.setItemValue('stats_of_exptl_data', stats)

        return self.report.getTotalErrors() == __errors

    def __calculateStatsOfAssignedChemShift(self, sf_framecode, lp_data, cs_ann, ent):
        """ Calculate statistics of assigned chemical shifts.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        item_names = self.item_names_in_cs_loop[file_type]
        chain_id_name = item_names['chain_id']
        seq_id_name = item_names['seq_id']
        comp_id_name = item_names['comp_id']
        atom_id_name = item_names['atom_id']
        value_name = item_names['value']
        atom_type = item_names['atom_type']
        iso_number = item_names['isotope_number']

        try:

            count = {}

            for i in lp_data:

                if i[atom_type] in self.empty_value or i[iso_number] in self.empty_value or value_name in self.empty_value:
                    continue

                data_type = str(i[iso_number]) + i[atom_type].lower() + '_chemical_shifts'

                if data_type in count:
                    count[data_type] += 1
                else:
                    count[data_type] = 1

            if len(count) > 0:
                ent['number_of_assignments'] = count

            polymer_sequence = input_source_dic['polymer_sequence']

            if polymer_sequence is None:
                return

            if 'sequence_coverage' in ent:

                completeness = []

                for sc in ent['sequence_coverage']:

                    cc = {}

                    chain_id = sc['chain_id']

                    cc['chain_id'] = chain_id

                    # all atoms

                    all_c = []

                    excluded_comp_id = []
                    excluded_atom_id = []

                    id = 0

                    h1_col = -1
                    c13_col = -1
                    n15_col = -1
                    p31_col = -1

                    for data_type in count:

                        atom_group = {}
                        atom_group['atom_group'] = 'all_' + data_type
                        atom_group['number_of_assigned_shifts'] = 0
                        atom_group['number_of_target_shifts'] = 0
                        atom_group['completeness'] = 0.0

                        if data_type.startswith('1h'):
                            h1_col = id

                        elif data_type.startswith('13c'):
                            c13_col = id

                        elif data_type.startswith('15n'):
                            n15_col = id

                        elif data_type.startswith('31p'):
                            p31_col = id

                        id += 1

                        all_c.append(atom_group)

                    for s in polymer_sequence:

                        if s['chain_id'] == chain_id:

                            for i in range(len(s['seq_id'])):
                                seq_id = s['seq_id'][i]
                                comp_id = s['comp_id'][i]

                                polypeptide_like = self.__csStat.getTypeOfCompId(comp_id)[0]

                                if self.__csStat.hasEnoughStat(comp_id, polypeptide_like):

                                    all_atoms = self.__csStat.getAllAtoms(comp_id, excl_minor_atom=True, primary=polypeptide_like)
                                    non_excl_atoms = self.__csStat.getAllAtoms(comp_id, excl_minor_atom=False)
                                    non_rep_methyl_pros = self.__csStat.getNonRepresentativeMethylProtons(comp_id, excl_minor_atom=True, primary=polypeptide_like)

                                    for a in all_atoms:

                                        if a.startswith('H') and not a in non_rep_methyl_pros:
                                            all_c[h1_col]['number_of_target_shifts'] += 1

                                        elif a.startswith('C') and c13_col != -1:
                                            all_c[c13_col]['number_of_target_shifts'] += 1

                                        elif a.startswith('N') and n15_col != -1:
                                            all_c[n15_col]['number_of_target_shifts'] += 1

                                        elif a.startswith('P') and p31_col != -1:
                                            all_c[p31_col]['number_of_target_shifts'] += 1

                                    for j in lp_data:

                                        if file_type == 'nef':
                                            _chain_id = j[chain_id_name]
                                        else:
                                            _chain_id = str(j[chain_id_name])

                                        if _chain_id != chain_id or j[seq_id_name] != seq_id or j[comp_id_name] != comp_id or j[value_name] in self.empty_value:
                                            continue

                                        atom_id = j[atom_id_name]
                                        data_type = str(j[iso_number]) + j[atom_type]

                                        if file_type == 'nef':

                                            atom_ids = self.__nefT.get_nmrstar_atom(comp_id, atom_id, leave_unmatched=False)[0]

                                            if len(atom_ids) == 0:
                                                continue

                                            for a in atom_ids:

                                                if a in all_atoms:

                                                    if data_type == '1H' and not a in non_rep_methyl_pros:
                                                        all_c[h1_col]['number_of_assigned_shifts'] += 1

                                                    elif data_type == '13C':
                                                        all_c[c13_col]['number_of_assigned_shifts'] += 1

                                                    elif data_type == '15N':
                                                        all_c[n15_col]['number_of_assigned_shifts'] += 1

                                                    elif data_type == '31P':
                                                        all_c[p31_col]['number_of_assigned_shifts'] += 1

                                                elif a in non_excl_atoms:
                                                    excluded_atom_id.append({'seq_id': seq_id, 'comp_id': comp_id, 'atom_id': a, 'value': j[value_name]})

                                        else:

                                            if atom_id in all_atoms:

                                                if data_type == '1H' and not atom_id in non_rep_methyl_pros:
                                                    all_c[h1_col]['number_of_assigned_shifts'] += 1

                                                elif data_type == '13C':
                                                    all_c[c13_col]['number_of_assigned_shifts'] += 1

                                                elif data_type == '15N':
                                                    all_c[n15_col]['number_of_assigned_shifts'] += 1

                                                elif data_type == '31P':
                                                    all_c[p31_col]['number_of_assigned_shifts'] += 1

                                            elif atom_id in non_excl_atoms:
                                                excluded_atom_id.append({'seq_id': seq_id, 'comp_id': comp_id, 'atom_id': atom_id, 'value': j[value_name]})

                                else:
                                    excluded_comp_id.append({'seq_id': seq_id, 'comp_id': comp_id})

                            for c in all_c:
                                if c['number_of_target_shifts'] > 0:
                                    c['completeness'] = float('{:.3f}'.format(float(c['number_of_assigned_shifts']) / float(c['number_of_target_shifts'])))
                                else:
                                    c['completeness'] = None

                            break

                    cc['completeness_of_all_assignments'] = all_c

                    cc['excluded_comp_id_in_statistics'] = excluded_comp_id if len(excluded_comp_id) > 0 else None
                    cc['excluded_atom_id_in_statistics'] = excluded_atom_id if len(excluded_atom_id) > 0 else None

                    # backbone atoms (bb)

                    bb_c = []

                    id = 0

                    h1_col = -1
                    c13_col = -1
                    n15_col = -1
                    p31_col = -1

                    for data_type in count:

                        atom_group = {}
                        atom_group['atom_group'] = 'backbone_' + data_type
                        atom_group['number_of_assigned_shifts'] = 0
                        atom_group['number_of_target_shifts'] = 0
                        atom_group['completeness'] = 0.0

                        if data_type.startswith('1h'):
                            h1_col = id

                        elif data_type.startswith('13c'):
                            c13_col = id

                        elif data_type.startswith('15n'):
                            n15_col = id

                        elif data_type.startswith('31p'):
                            p31_col = id

                        id += 1

                        bb_c.append(atom_group)

                    for s in polymer_sequence:

                        if s['chain_id'] == chain_id:

                            for i in range(len(s['seq_id'])):
                                seq_id = s['seq_id'][i]
                                comp_id = s['comp_id'][i]

                                polypeptide_like = self.__csStat.getTypeOfCompId(comp_id)[0]

                                if self.__csStat.hasEnoughStat(comp_id, polypeptide_like):

                                    bb_atoms = self.__csStat.getBackBoneAtoms(comp_id, excl_minor_atom=True)
                                    non_rep_methyl_pros = self.__csStat.getNonRepresentativeMethylProtons(comp_id, excl_minor_atom=True, primary=polypeptide_like)

                                    for a in bb_atoms:

                                        if a.startswith('H') and h1_col != -1 and not a in non_rep_methyl_pros:
                                            bb_c[h1_col]['number_of_target_shifts'] += 1

                                        elif a.startswith('C') and c13_col != -1:
                                            bb_c[c13_col]['number_of_target_shifts'] += 1

                                        elif a.startswith('N') and n15_col != -1:
                                            bb_c[n15_col]['number_of_target_shifts'] += 1

                                        elif a.startswith('P') and p31_col != -1:
                                            bb_c[p31_col]['number_of_target_shifts'] += 1

                                    for j in lp_data:

                                        if file_type == 'nef':
                                            _chain_id = j[chain_id_name]
                                        else:
                                            _chain_id = str(j[chain_id_name])

                                        if _chain_id != chain_id or j[seq_id_name] != seq_id or j[comp_id_name] != comp_id or j[value_name] in self.empty_value:
                                            continue

                                        atom_id = j[atom_id_name]
                                        data_type = str(j[iso_number]) + j[atom_type]

                                        if file_type == 'nef':

                                            atom_ids = self.__nefT.get_nmrstar_atom(comp_id, atom_id, leave_unmatched=False)[0]

                                            if len(atom_ids) == 0:
                                                continue

                                            for a in atom_ids:

                                                if a in bb_atoms:

                                                    if data_type == '1H' and not a in non_rep_methyl_pros:
                                                        bb_c[h1_col]['number_of_assigned_shifts'] += 1

                                                    elif data_type == '13C':
                                                        bb_c[c13_col]['number_of_assigned_shifts'] += 1

                                                    elif data_type == '15N':
                                                        bb_c[n15_col]['number_of_assigned_shifts'] += 1

                                                    elif data_type == '31P':
                                                        bb_c[p31_col]['number_of_assigned_shifts'] += 1

                                        elif atom_id in bb_atoms:

                                            if data_type == '1H' and not atom_id in non_rep_methyl_pros:
                                                bb_c[h1_col]['number_of_assigned_shifts'] += 1

                                            elif data_type == '13C':
                                                bb_c[c13_col]['number_of_assigned_shifts'] += 1

                                            elif data_type == '15N':
                                                bb_c[n15_col]['number_of_assigned_shifts'] += 1

                                            elif data_type == '31P':
                                                bb_c[p31_col]['number_of_assigned_shifts'] += 1

                            for c in bb_c:
                                if c['number_of_target_shifts'] > 0:
                                    c['completeness'] = float('{:.3f}'.format(float(c['number_of_assigned_shifts']) / float(c['number_of_target_shifts'])))
                                else:
                                    c['completeness'] = None

                            break

                    if len(bb_c) > 0:
                        cc['completeness_of_backbone_assignments'] = bb_c

                    # sidechain atoms (sc)

                    sc_c = []

                    id = 0

                    h1_col = -1
                    c13_col = -1
                    n15_col = -1
                    p31_col = -1

                    for data_type in count:

                        atom_group = {}
                        atom_group['atom_group'] = 'sidechain_' + data_type
                        atom_group['number_of_assigned_shifts'] = 0
                        atom_group['number_of_target_shifts'] = 0
                        atom_group['completeness'] = 0.0

                        if data_type.startswith('1h'):
                            h1_col = id

                        elif data_type.startswith('13c'):
                            c13_col = id

                        elif data_type.startswith('15n'):
                            n15_col = id

                        elif data_type.startswith('31p'):
                            p31_col = id

                        id += 1

                        sc_c.append(atom_group)

                    for s in polymer_sequence:

                        if s['chain_id'] == chain_id:

                            for i in range(len(s['seq_id'])):
                                seq_id = s['seq_id'][i]
                                comp_id = s['comp_id'][i]

                                polypeptide_like = self.__csStat.getTypeOfCompId(comp_id)[0]

                                if self.__csStat.hasEnoughStat(comp_id, polypeptide_like):

                                    sc_atoms = self.__csStat.getSideChainAtoms(comp_id, excl_minor_atom=True)
                                    non_rep_methyl_pros = self.__csStat.getNonRepresentativeMethylProtons(comp_id, excl_minor_atom=True, primary=polypeptide_like)

                                    for a in sc_atoms:

                                        if a.startswith('H') and h1_col != -1 and not a in non_rep_methyl_pros:
                                            sc_c[h1_col]['number_of_target_shifts'] += 1

                                        elif a.startswith('C') and c13_col != -1:
                                            sc_c[c13_col]['number_of_target_shifts'] += 1

                                        elif a.startswith('N') and n15_col != -1:
                                            sc_c[n15_col]['number_of_target_shifts'] += 1

                                        elif a.startswith('P') and p31_col != -1:
                                            sc_c[p31_col]['number_of_target_shifts'] += 1

                                    for j in lp_data:

                                        if file_type == 'nef':
                                            _chain_id = j[chain_id_name]
                                        else:
                                            _chain_id = str(j[chain_id_name])

                                        if _chain_id != chain_id or j[seq_id_name] != seq_id or j[comp_id_name] != comp_id or j[value_name] in self.empty_value:
                                            continue

                                        atom_id = j[atom_id_name]
                                        data_type = str(j[iso_number]) + j[atom_type]

                                        if file_type == 'nef':

                                            atom_ids = self.__nefT.get_nmrstar_atom(comp_id, atom_id, leave_unmatched=False)[0]

                                            if len(atom_ids) == 0:
                                                continue

                                            for a in atom_ids:

                                                if a in sc_atoms:

                                                    if data_type == '1H' and not a in non_rep_methyl_pros:
                                                        sc_c[h1_col]['number_of_assigned_shifts'] += 1

                                                    elif data_type == '13C':
                                                        sc_c[c13_col]['number_of_assigned_shifts'] += 1

                                                    elif data_type == '15N':
                                                        sc_c[n15_col]['number_of_assigned_shifts'] += 1

                                                    elif data_type == '31P':
                                                        sc_c[p31_col]['number_of_assigned_shifts'] += 1

                                        elif atom_id in sc_atoms:

                                            if data_type == '1H' and not atom_id in non_rep_methyl_pros:
                                                sc_c[h1_col]['number_of_assigned_shifts'] += 1

                                            elif data_type == '13C':
                                                sc_c[c13_col]['number_of_assigned_shifts'] += 1

                                            elif data_type == '15N':
                                                sc_c[n15_col]['number_of_assigned_shifts'] += 1

                                            elif data_type == '31P':
                                                sc_c[p31_col]['number_of_assigned_shifts'] += 1

                            for c in sc_c:
                                if c['number_of_target_shifts'] > 0:
                                    c['completeness'] = float('{:.3f}'.format(float(c['number_of_assigned_shifts']) / float(c['number_of_target_shifts'])))
                                else:
                                    c['completeness'] = None

                            break

                    if len(sc_c) > 0:
                        cc['completeness_of_sidechain_assignments'] = sc_c

                    # methyl group atoms (ch3)

                    ch3_c = []

                    id = 0

                    h1_col = -1
                    c13_col = -1

                    for data_type in count:

                        atom_group = {}
                        atom_group['atom_group'] = 'methyl_' + data_type
                        atom_group['number_of_assigned_shifts'] = 0
                        atom_group['number_of_target_shifts'] = 0
                        atom_group['completeness'] = 0.0

                        if data_type.startswith('1h'):
                            h1_col = id

                        elif data_type.startswith('13c'):
                            c13_col = id

                        else:
                            continue

                        id += 1

                        ch3_c.append(atom_group)

                    for s in polymer_sequence:

                        if s['chain_id'] == chain_id:

                            for i in range(len(s['seq_id'])):
                                seq_id = s['seq_id'][i]
                                comp_id = s['comp_id'][i]

                                polypeptide_like = self.__csStat.getTypeOfCompId(comp_id)[0]

                                if self.__csStat.hasEnoughStat(comp_id, polypeptide_like):

                                    ch3_atoms = self.__csStat.getMethylAtoms(comp_id, excl_minor_atom=True, primary=polypeptide_like)
                                    non_rep_methyl_pros = self.__csStat.getNonRepresentativeMethylProtons(comp_id, excl_minor_atom=True, primary=polypeptide_like)

                                    for a in ch3_atoms:

                                        if a.startswith('H') and h1_col != -1 and not a in non_rep_methyl_pros:
                                            ch3_c[h1_col]['number_of_target_shifts'] += 1

                                        elif a.startswith('C') and c13_col != -1:
                                            ch3_c[c13_col]['number_of_target_shifts'] += 1

                                    for j in lp_data:

                                        if file_type == 'nef':
                                            _chain_id = j[chain_id_name]
                                        else:
                                            _chain_id = str(j[chain_id_name])

                                        if _chain_id != chain_id or j[seq_id_name] != seq_id or j[comp_id_name] != comp_id or j[value_name] in self.empty_value:
                                            continue

                                        atom_id = j[atom_id_name]
                                        data_type = str(j[iso_number]) + j[atom_type]

                                        if file_type == 'nef':

                                            atom_ids = self.__nefT.get_nmrstar_atom(comp_id, atom_id, leave_unmatched=False)[0]

                                            if len(atom_ids) == 0:
                                                continue

                                            for a in atom_ids:

                                                if a in ch3_atoms:

                                                    if data_type == '1H' and not a in non_rep_methyl_pros:
                                                        ch3_c[h1_col]['number_of_assigned_shifts'] += 1

                                                    elif data_type == '13C':
                                                        ch3_c[c13_col]['number_of_assigned_shifts'] += 1

                                        elif atom_id in ch3_atoms:

                                            if data_type == '1H' and not atom_id in non_rep_methyl_pros:
                                                ch3_c[h1_col]['number_of_assigned_shifts'] += 1

                                            elif data_type == '13C':
                                                ch3_c[c13_col]['number_of_assigned_shifts'] += 1

                            for c in ch3_c:
                                if c['number_of_target_shifts'] > 0:
                                    c['completeness'] = float('{:.3f}'.format(float(c['number_of_assigned_shifts']) / float(c['number_of_target_shifts'])))
                                else:
                                    c['completeness'] = None

                            break

                    if len(ch3_c) > 0:
                        cc['completeness_of_methyl_assignments'] = ch3_c

                    # aromatic atoms (aro)

                    aro_c = []

                    id = 0

                    h1_col = -1
                    c13_col = -1
                    n15_col = -1

                    for data_type in count:

                        atom_group = {}
                        atom_group['atom_group'] = 'aromatic_' + data_type
                        atom_group['number_of_assigned_shifts'] = 0
                        atom_group['number_of_target_shifts'] = 0
                        atom_group['completeness'] = 0.0

                        if data_type.startswith('1h'):
                            h1_col = id

                        elif data_type.startswith('13c'):
                            c13_col = id

                        elif data_type.startswith('15n'):
                            n15_col = id

                        else:
                            continue

                        id += 1

                        aro_c.append(atom_group)

                    for s in polymer_sequence:

                        if s['chain_id'] == chain_id:

                            for i in range(len(s['seq_id'])):
                                seq_id = s['seq_id'][i]
                                comp_id = s['comp_id'][i]

                                polypeptide_like = self.__csStat.getTypeOfCompId(comp_id)[0]

                                if self.__csStat.hasEnoughStat(comp_id, polypeptide_like):

                                    aro_atoms = self.__csStat.getAromaticAtoms(comp_id, excl_minor_atom=True, primary=polypeptide_like)
                                    non_rep_methyl_pros = self.__csStat.getNonRepresentativeMethylProtons(comp_id, excl_minor_atom=True, primary=polypeptide_like)

                                    for a in aro_atoms:

                                        if a.startswith('H') and h1_col != -1 and not a in non_rep_methyl_pros:
                                            aro_c[h1_col]['number_of_target_shifts'] += 1

                                        elif a.startswith('C') and c13_col != -1:
                                            aro_c[c13_col]['number_of_target_shifts'] += 1

                                        elif a.startswith('N') and n15_col != -1:
                                            aro_c[n15_col]['number_of_target_shifts'] += 1

                                    for j in lp_data:

                                        if file_type == 'nef':
                                            _chain_id = j[chain_id_name]
                                        else:
                                            _chain_id = str(j[chain_id_name])

                                        if _chain_id != chain_id or j[seq_id_name] != seq_id or j[comp_id_name] != comp_id or j[value_name] in self.empty_value:
                                            continue

                                        atom_id = j[atom_id_name]
                                        data_type = str(j[iso_number]) + j[atom_type]

                                        if file_type == 'nef':

                                            atom_ids = self.__nefT.get_nmrstar_atom(comp_id, atom_id, leave_unmatched=False)[0]

                                            if len(atom_ids) == 0:
                                                continue

                                            for a in atom_ids:

                                                if a in aro_atoms:

                                                    if data_type == '1H' and not a in non_rep_methyl_pros:
                                                        aro_c[h1_col]['number_of_assigned_shifts'] += 1

                                                    elif data_type == '13C':
                                                        aro_c[c13_col]['number_of_assigned_shifts'] += 1

                                                    elif data_type == '15N':
                                                        aro_c[n15_col]['number_of_assigned_shifts'] += 1

                                        elif atom_id in aro_atoms:

                                            if data_type == '1H' and not atom_id in non_rep_methyl_pros:
                                                aro_c[h1_col]['number_of_assigned_shifts'] += 1

                                            elif data_type == '13C':
                                                aro_c[c13_col]['number_of_assigned_shifts'] += 1

                                            elif data_type == '15N':
                                                aro_c[n15_col]['number_of_assigned_shifts'] += 1

                            for c in aro_c:
                                if c['number_of_target_shifts'] > 0:
                                    c['completeness'] = float('{:.3f}'.format(float(c['number_of_assigned_shifts']) / float(c['number_of_target_shifts'])))
                                else:
                                    c['completeness'] = None

                            break

                    if len(aro_c) > 0:
                        cc['completeness_of_aromatic_assignments'] = aro_c

                    completeness.append(cc)

                if len(completeness) > 0:
                    ent['completeness'] = completeness

            z_scores = {}

            for k in count.keys():
                z_scores[k] = []

            max_val = 0.0
            min_val = 0.0

            for i in lp_data:

                if i[atom_type] in self.empty_value or i[iso_number] in self.empty_value or value_name in self.empty_value:
                    continue

                data_type = str(i[iso_number]) + i[atom_type].lower() + '_chemical_shifts'

                chain_id = i[chain_id_name]
                seq_id = i[seq_id_name]
                comp_id = i[comp_id_name]
                atom_id = i[atom_id_name]
                value = i[value_name]

                if file_type == 'nef':
                    _atom_id, ambig_code, details = self.__nefT.get_nmrstar_atom(comp_id, atom_id, leave_unmatched=True)

                    if len(_atom_id) == 0:
                        continue

                    if len(_atom_id) == 1 and atom_id == _atom_id[0]:
                        atom_id_ = atom_id

                    else:
                        # representative atom id
                        atom_id_ = _atom_id[0]

                else:
                    atom_id_ = atom_id

                one_letter_code = self.__get1LetterCode(comp_id)

                has_cs_stat = False

                # non-standard residue
                if one_letter_code == 'X':

                    neighbor_comp_ids = set([j[comp_id_name] for j in lp_data if j[chain_id_name] == chain_id and abs(j[seq_id_name] - seq_id) < 3 and j[seq_id_name] != seq_id])

                    polypeptide_like = False

                    for comp_id2 in neighbor_comp_ids:
                        polypeptide_like |= self.__csStat.getTypeOfCompId(comp_id2)[0]

                    for cs_stat in self.__csStat.get(comp_id):

                        if cs_stat['atom_id'] == atom_id_:
                            avg_value = cs_stat['avg']
                            std_value = cs_stat['std']

                            has_cs_stat = True

                            break

                # standard residue
                else:

                    for cs_stat in self.__csStat.get(comp_id, self.report.isDiamagnetic()):

                        if cs_stat['atom_id'] == atom_id_:
                            avg_value = cs_stat['avg']
                            std_value = cs_stat['std']

                            has_cs_stat = True

                            break

                if not has_cs_stat or std_value is None:
                    continue

                z_score = (value - avg_value) / std_value

                if z_score > max_val:
                    max_val = z_score

                elif z_score < min_val:
                    min_val = z_score

                z_scores[data_type].append(z_score)

            target_scale = (max_val - min_val) / 20.0

            scale = 1.0

            while scale < target_scale:
                scale *= 2.0

            while scale > target_scale:
                scale /= 2.0

            range_of_vals = []
            count_of_vals = []

            v = 0.0
            while v < min_val:
                v += scale

            while v > min_val:
                v -= scale

            while v < max_val:

                _count = copy.copy(count)

                for k in count.keys():
                    _count[k] = len([z for z in z_scores[k] if z >= v and z < v + scale])

                range_of_vals.append(v)
                count_of_vals.append(_count)

                v += scale

            transposed = {}

            for k in count.keys():
                transposed[k] = []

                for j in range(len(range_of_vals)):
                    transposed[k].append(count_of_vals[j][k])

            if len(range_of_vals) > 1:
                """
                has_value = False
                for j in range(1, len(range_of_vals) - 1):
                    for k in count.keys():
                        if transposed[k][j] > 0:
                            has_value = True
                            break
                    if has_value:
                        break

                if has_value:
                """
                ent['histogram'] = {'range_of_values': range_of_vals, 'number_of_values': transposed, 'annotations': cs_ann}

            if 'sequence_coverage' in ent:

                # prediction of redox state of CYS

                cys_redox_state = []

                for sc in ent['sequence_coverage']:

                    chain_id = sc['chain_id']

                    for s in polymer_sequence:

                        if s['chain_id'] == chain_id:

                            for i in range(len(s['seq_id'])):
                                seq_id = s['seq_id'][i]
                                comp_id = s['comp_id'][i]

                                if comp_id != 'CYS':
                                    continue

                                cys = {'chain_id': chain_id, 'seq_id': seq_id}

                                ca_chem_shift = None
                                cb_chem_shift = None

                                for j in lp_data:

                                    _chain_id = j[chain_id_name]
                                    atom_id = j[atom_id_name]

                                    if type(_chain_id) is int:
                                        __chain_id = str(_chain_id)
                                    else:
                                        __chain_id = _chain_id

                                    if __chain_id == chain_id and j[seq_id_name] == seq_id and j[comp_id_name] == comp_id:
                                        if atom_id == 'CA':
                                            ca_chem_shift = j[value_name]
                                        elif atom_id == 'CB':
                                            cb_chem_shift = j[value_name]

                                    if ca_chem_shift is None or cb_chem_shift is None:
                                        if __chain_id == chain_id and j[seq_id_name] > seq_id:
                                            break
                                    else:
                                        break

                                cys['ca_chem_shift'] = ca_chem_shift
                                cys['cb_chem_shift'] = cb_chem_shift

                                if not cb_chem_shift is None:
                                    if cb_chem_shift < 32.0:
                                        cys['redox_state_pred'] = 'reduced'
                                    elif cb_chem_shift > 35.0:
                                        cys['redox_state_pred'] = 'oxidized'
                                    else:
                                        cys['redox_state_pred'] = 'ambiguous'
                                elif not ca_chem_shift is None:
                                    cys['redox_state_pred'] = 'ambiguous'
                                else:
                                    cys['redox_state_pred'] = 'unknown'

                                if cys['redox_state_pred'] == 'ambiguous':
                                    oxi, red = self.__predictRedoxStateOfCystein(ca_chem_shift, cb_chem_shift)
                                    if oxi < 0.001:
                                        cys['redox_state_pred'] = 'reduced'
                                    elif red < 0.001:
                                        cys['redox_state_pred'] = 'oxidized'
                                    else:
                                        cys['redox_state_pred'] = 'oxidized %s (%%), reduced %s (%%)' % ('{:.1f}'.format(oxi * 100.0), '{:.1f}'.format(red * 100.0))

                                cys['in_disulfide_bond'] = False
                                if not input_source_dic['disulfide_bond'] is None:
                                    try:
                                        next(b for b in input_source_dic['disulfide_bond'] if (b['chain_id_1'] == chain_id and b['seq_id_1'] == seq_id) or (b['chain_id_2'] == chain_id and b['seq_id_2'] == seq_id))
                                        cys['in_disulfide_bond'] = True
                                    except StopIteration:
                                        pass

                                cys['in_other_bond'] = False
                                if not input_source_dic['other_bond'] is None:
                                    try:
                                        next(b for b in input_source_dic['other_bond'] if (b['chain_id_1'] == chain_id and b['seq_id_1'] == seq_id) or (b['chain_id_2'] == chain_id and b['seq_id_2'] == seq_id))
                                        cys['in_other_bond'] = True
                                    except StopIteration:
                                        pass

                                cys_redox_state.append(cys)

                    if len(cys_redox_state) > 0:
                        ent['cys_redox_state'] = cys_redox_state

                # prediction of cis-trans peptide of PRO

                pro_cis_trans = []

                for sc in ent['sequence_coverage']:

                    chain_id = sc['chain_id']

                    for s in polymer_sequence:

                        if s['chain_id'] == chain_id:

                            for i in range(len(s['seq_id'])):
                                seq_id = s['seq_id'][i]
                                comp_id = s['comp_id'][i]

                                if comp_id != 'PRO':
                                    continue

                                pro = {'chain_id': chain_id, 'seq_id': seq_id}

                                cb_chem_shift = None
                                cg_chem_shift = None

                                for j in lp_data:

                                    _chain_id = j[chain_id_name]
                                    atom_id = j[atom_id_name]

                                    if type(_chain_id) is int:
                                        __chain_id = str(_chain_id)
                                    else:
                                        __chain_id = _chain_id

                                    if __chain_id == chain_id and j[seq_id_name] == seq_id and j[comp_id_name] == comp_id:
                                        if atom_id == 'CB':
                                            cb_chem_shift = j[value_name]
                                        elif atom_id == 'CG':
                                            cg_chem_shift = j[value_name]

                                    if cb_chem_shift is None or cg_chem_shift is None:
                                        if __chain_id == chain_id and j[seq_id_name] > seq_id:
                                            break
                                    else:
                                        break

                                pro['cb_chem_shift'] = cb_chem_shift
                                pro['cg_chem_shift'] = cg_chem_shift

                                if not cb_chem_shift is None and not cg_chem_shift is None:
                                    delta = cb_chem_shift - cg_chem_shift
                                    if delta < 4.8:
                                        pro['cis_trans_pred'] = 'trans'
                                    elif delta > 9.15:
                                        pro['cis_trans_pred'] = 'cis'
                                    else:
                                        pro['cis_trans_pred'] = 'ambiguous'
                                elif not cb_chem_shift is None or not cg_chem_shift is None:
                                    pro['cis_trans_pred'] = 'ambiguous'
                                else:
                                    pro['cis_trans_pred'] = 'unknown'

                                if pro['cis_trans_pred'] == 'ambiguous':
                                    cis, trs = self.__predictCisTransPeptideOfProline(cb_chem_shift, cg_chem_shift)
                                    if cis < 0.001:
                                        pro['cis_trans_pred'] = 'trans'
                                    elif trs < 0.001:
                                        pro['cis_trans_pred'] = 'cis'
                                    else:
                                        pro['cis_trans_pred'] = 'cis %s (%%), trans %s (%%)' % ('{:.1f}'.format(cis * 100.0), '{:.1f}'.format(trs * 100.0))

                                pro['in_cis_peptide_bond'] = self.__isProtCis(chain_id, seq_id)

                                if (pro['in_cis_peptide_bond'] and pro['cis_trans_pred'] != 'cis') or (not pro['in_cis_peptide_bond'] and pro['cis_trans_pred'] != 'trans'):
                                    item = None
                                    if ',' in pro['cis_trans_pred']:
                                        if (pro['in_cis_peptide_bond'] and cis > trs) or\
                                           (not pro['in_cis_peptide_bond'] and trs > cis):
                                            pass
                                        else:
                                            item = 'unusual_data'
                                    else:
                                        item = 'suspicious_data'

                                    if not item is None:

                                        shifts = ''
                                        if not cb_chem_shift is None:
                                            shifts += 'CB %s, ' % cb_chem_shift
                                        if not cg_chem_shift is None:
                                            shifts += 'CG %s, ' % cg_chem_shift

                                        warn = "%s-peptide bond (chain_id %s, seq_id %s, comp_id %s) could not supported by assigned chemical shift values (%scis_trans_pred %s)." %\
                                               ('cis' if pro['in_cis_peptide_bond'] else 'trans', chain_id, seq_id, comp_id, shifts, pro['cis_trans_pred'])

                                        self.report.warning.appendDescription(item, {'file_name': file_name, 'sf_framecode': sf_framecode, 'description': warn})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__calculateStatsOfAssignedChemShift() ++ Warning  - %s\n" % warn)

                                pro_cis_trans.append(pro)

                    if len(pro_cis_trans) > 0:
                        ent['pro_cis_trans'] = pro_cis_trans

                # prediction of tautomeric state of HIS

                his_tautomeric_state = []

                for sc in ent['sequence_coverage']:

                    chain_id = sc['chain_id']

                    for s in polymer_sequence:

                        if s['chain_id'] == chain_id:

                            for i in range(len(s['seq_id'])):
                                seq_id = s['seq_id'][i]
                                comp_id = s['comp_id'][i]

                                if comp_id != 'HIS':
                                    continue

                                his = {'chain_id': chain_id, 'seq_id': seq_id}

                                cg_chem_shift = None
                                cd2_chem_shift = None
                                nd1_chem_shift = None
                                ne2_chem_shift = None

                                for j in lp_data:

                                    _chain_id = j[chain_id_name]
                                    atom_id = j[atom_id_name]

                                    if type(_chain_id) is int:
                                        __chain_id = str(_chain_id)
                                    else:
                                        __chain_id = _chain_id

                                    if __chain_id == chain_id and j[seq_id_name] == seq_id and j[comp_id_name] == comp_id:
                                        if atom_id == 'CG':
                                            cg_chem_shift = j[value_name]
                                        elif atom_id == 'CD2':
                                            cd2_chem_shift = j[value_name]
                                        elif atom_id == 'ND1':
                                            nd1_chem_shift = j[value_name]
                                        elif atom_id == 'NE2':
                                            ne2_chem_shift = j[value_name]

                                    if cg_chem_shift is None or cd2_chem_shift is None or nd1_chem_shift is None or ne2_chem_shift is None:
                                        if __chain_id == chain_id and j[seq_id_name] > seq_id:
                                            break
                                    else:
                                        break

                                his['cg_chem_shift'] = cg_chem_shift
                                his['cd2_chem_shift'] = cd2_chem_shift
                                his['nd1_chem_shift'] = nd1_chem_shift
                                his['ne2_chem_shift'] = ne2_chem_shift

                                if not cg_chem_shift is None or not cd2_chem_shift is None or not nd1_chem_shift is None or not ne2_chem_shift is None:
                                    bip, tau, pi = self.__predictTautomerOfHistidine(cg_chem_shift, cd2_chem_shift, nd1_chem_shift, ne2_chem_shift)
                                    if tau < 0.001 and pi < 0.001:
                                        his['tautomeric_state_pred'] = 'biprotonated'
                                    elif bip < 0.001 and pi < 0.001:
                                        his['tautomeric_state_pred'] = 'tau-tautomer'
                                    elif bip < 0.001 and tau < 0.001:
                                        his['tautomeric_statem_pred'] = 'pi-tautomer'
                                    else:
                                        his['tautomeric_state_pred'] = 'biprotonated %s (%%), tau-tautomer %s (%%), pi-tautomer %s (%%)' % ('{:.1f}'.format(bip * 100.0), '{:.1f}'.format(tau * 100.0), '{:.1f}'.format(pi * 100.0))
                                else:
                                    his['tautomeric_state_pred'] = 'unknown'

                                his['tautomeric_state'] = self.__getTautomerOfHistidine(chain_id, seq_id)

                                if his['tautomeric_state_pred'] != 'unknown':
                                    item = None
                                    if his['tautomeric_state_pred'] != his['tautomeric_state']:
                                        if ',' in his['tautomeric_state_pred']:
                                            if (his['tautomeric_state'] == 'biprotonated' and bip > tau and bip > pi) or\
                                               (his['tautomeric_state'] == 'tau-tautomer' and tau > bip and tau > pi) or\
                                               (his['tautomeric_state'] == 'pi-tautomer' and pi > bip and pi > tau):
                                                pass
                                            else:
                                                item = 'unusual_data'
                                        else:
                                            item = 'suspicious_data'

                                    if not item is None:

                                        shifts = ''
                                        if not cg_chem_shift is None:
                                            shifts += 'CG %s, ' % cg_chem_shift
                                        if not cd2_chem_shift is None:
                                            shifts += 'CD2 %s, ' % cd2_chem_shift
                                        if not nd1_chem_shift is None:
                                            shifts += 'ND1 %s, ' % nd1_chem_shift
                                        if not ne2_chem_shift is None:
                                            shifts += 'NE2 %s, ' % ne2_chem_shift

                                        warn = "Tautomeric state %s (chain_id %s, seq_id %s, comp_id %s) could not supported by assigned chemical shift values (%stautomeric_state_pred %s)." %\
                                               (his['tautomeric_state'], chain_id, seq_id, comp_id, shifts, his['tautomeric_state_pred'])

                                        self.report.warning.appendDescription(item, {'file_name': file_name, 'sf_framecode': sf_framecode, 'description': warn})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__calculateStatsOfAssignedChemShift() ++ Warning  - %s\n" % warn)

                                his_tautomeric_state.append(his)

                if len(his_tautomeric_state) > 0:
                    ent['his_tautomeric_state'] = his_tautomeric_state

        except Exception as e:

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__calculateStatsOfAssignedChemShift() ++ Error  - %s" % str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__calculateStatsOfAssignedChemShift() ++ Error  - %s" % str(e))

    def __calculateStatsOfDistanceRestraint(self, sf_framecode, lp_data, ent):
        """ Calculate statistics of distance restraints.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        item_names = self.item_names_in_ds_loop[file_type]
        comb_id_name = item_names['combination_id']
        chain_id_1_name = item_names['chain_id_1']
        chain_id_2_name = item_names['chain_id_2']
        seq_id_1_name = item_names['seq_id_1']
        seq_id_2_name = item_names['seq_id_2']
        comp_id_1_name = item_names['comp_id_1']
        comp_id_2_name = item_names['comp_id_2']
        atom_id_1_name = item_names['atom_id_1']
        atom_id_2_name = item_names['atom_id_2']
        target_value_name = item_names['target_value']
        lower_limit_name = item_names['lower_limit']
        upper_limit_name = item_names['upper_limit']
        lower_linear_limit_name = item_names['lower_linear_limit']
        upper_linear_limit_name = item_names['upper_linear_limit']

        try:

            max_val = -100.0
            min_val = 100.0

            count = {}
            potential = {}

            comb_id_set = set()

            for i in lp_data:
                comb_id = i[comb_id_name]
                chain_id_1 = i[chain_id_1_name]
                chain_id_2 = i[chain_id_2_name]
                seq_id_1 = i[seq_id_1_name]
                seq_id_2 = i[seq_id_2_name]
                comp_id_1 = i[comp_id_1_name]
                comp_id_2 = i[comp_id_2_name]
                atom_id_1 = i[atom_id_1_name]
                atom_id_2 = i[atom_id_2_name]

                target_value = i[target_value_name]
                upper_limit_value = None
                lower_limit_value = None

                if target_value is None:

                    if not i[lower_limit_name] is None and not i[upper_limit_name] is None:
                        target_value = (i[lower_limit_name] + i[upper_limit_name]) / 2.0

                    elif not i[lower_linear_limit_name] is None and not i[upper_linear_limit_name] is None:
                        target_value = (i[lower_linear_limit_name] + i[upper_linear_limit_name]) / 2.0

                    elif not i[upper_linear_limit_name] is None:
                        target_value = i[upper_linear_limit_name]
                        upper_limit_value = target_value

                    elif not i[upper_limit_name] is None:
                        target_value = i[upper_limit_name]
                        upper_limit_value = target_value

                    elif not i[lower_linear_limit_name] is None:
                        target_value = i[lower_linear_limit_name]
                        lower_limit_value = target_value

                    elif not i[lower_limit_name] is None:
                        target_value = i[lower_limit_name]
                        lower_limit_value = target_value

                    else:
                        continue

                if target_value > max_val:
                    max_val = target_value

                if target_value < min_val:
                    min_val = target_value

                if not comb_id in self.empty_value:
                    comb_id_set.add(comp_id)

                hydrogen_bond_type = None
                hydrogen_bond = False
                disulfide_bond_type = None
                disulfide_bond = False
                diselenide_bond_type = None
                diselenide_bond = False
                other_bond_type = None
                other_bond = False
                symmetry = False

                if chain_id_1 != chain_id_2 or seq_id_1 != seq_id_2:

                    atom_id_1_ = atom_id_1[0]
                    atom_id_2_ = atom_id_2[0]

                    if not upper_limit_value is None:
                        target_value -= 0.4
                    elif not lower_limit_value is None:
                        target_value += 0.4

                    if (atom_id_1_ == 'F' and atom_id_2_ == 'H') or (atom_id_2_ == 'F' and atom_id_1_ == 'H'):

                        if target_value >= 1.2 and target_value <= 1.5:
                            hydrogen_bond_type = 'F...H-F'
                            hydrogen_bond = True
                        elif target_value < 1.2:
                            hydrogen_bond_type = 'F...H-F (too close!)'
                            hydrogen_bond = True

                    elif (atom_id_1_ == 'F' and atom_id_2_ == 'F') or (atom_id_2_ == 'F' and atom_id_1_ == 'F'):

                        if target_value >= 2.2 and target_value <= 2.5:
                            hydrogen_bond_type = 'F...h-F'
                            hydrogen_bond = True
                        elif target_value < 2.2:
                            hydrogen_bond_type = 'F...h-F (too close!)'
                            hydrogen_bond = True

                    elif (atom_id_1_ == 'O' and atom_id_2_ == 'H') or (atom_id_2_ == 'O' and atom_id_1_ == 'H'):

                        if target_value >= 1.5 and target_value <= 2.2:
                            hydrogen_bond_type = 'O...H-x'
                            hydrogen_bond = True
                        elif target_value < 1.5:
                            hydrogen_bond_type = 'O...H-x (too close!)'
                            hydrogen_bond = True

                    elif (atom_id_1_ == 'O' and atom_id_2_ == 'N') or (atom_id_2_ == 'O' and atom_id_1_ == 'N'):

                        if target_value >= 2.5 and target_value <= 3.2:
                            hydrogen_bond_type = 'O...h-N'
                            hydrogen_bond = True
                        elif target_value < 2.5:
                            hydrogen_bond_type = 'O...h-N (too close!)'
                            hydrogen_bond = True

                    elif (atom_id_1_ == 'O' and atom_id_2_ == 'O') or (atom_id_2_ == 'O' and atom_id_1_ == 'O'):

                        if target_value >= 2.5 and target_value <= 3.2:
                            hydrogen_bond_type = 'O...h-O'
                            hydrogen_bond = True
                        elif target_value < 2.5:
                            hydrogen_bond_type = 'O...h-O (too close!)'
                            hydrogen_bond = True

                    elif (atom_id_1_ == 'N' and atom_id_2_ == 'H') or (atom_id_2_ == 'N' and atom_id_1_ == 'H'):

                        if target_value >= 1.5 and target_value <= 2.2:
                            hydrogen_bond_type = 'N...H-x'
                            hydrogen_bond = True
                        elif target_value < 1.5:
                            hydrogen_bond_type = 'N...H-x (too close!)'
                            hydrogen_bond = True

                    elif (atom_id_1_ == 'N' and atom_id_2_ == 'N') or (atom_id_2_ == 'N' and atom_id_1_ == 'N'):

                        if target_value >= 2.5 and target_value <= 3.2:
                            hydrogen_bond_type = 'N...h_N'
                            hydrogen_bond = True
                        elif target_value < 2.5:
                            hydrogen_bond_type = 'N...h_N (too close!)'
                            hydrogen_bond = True

                    elif atom_id_1_ == 'S' and atom_id_2_ == 'S':

                        if target_value >= 1.9 and target_value <= 2.3:
                            disulfide_bond_type = 'S...S'
                            disulfide_bond = True
                        elif target_value < 1.9:
                            disulfide_bond_type = 'S...S (too close!)'
                            disulfide_bond = True

                    elif atom_id_1_ == 'SE' and atom_id_2_ == 'SE':

                        if target_value >= 2.1 and target_value <= 2.6:
                            diselenide_bond_type = 'Se...Se'
                            diselenide_bond = True
                        elif target_value < 2.1:
                            diselenide_bond_type = 'Se...Se (too close!)'
                            diselenide_bond = True

                    elif (atom_id_1_ == 'N' and not atom_id_2_ in self.non_metal_elems) or (atom_id_2_ == 'N' and not atom_id_1_ in self.non_metal_elems):

                        metal = atom_id_2_ if atom_id_1_ in self.non_metal_elems else atom_id_1_
                        metal = metal.title()

                        if target_value >= 1.9 and target_value <= 2.1:
                            other_bond_type = 'N...' + metal
                            other_bond = True
                        elif target_value < 1.9:
                            other_bond_type = 'N...' + metal + ' (too close!)'
                            other_bond = True

                    elif (atom_id_1_ == 'O' and not atom_id_2_ in self.non_metal_elems) or (atom_id_2_ == 'O' and not atom_id_1_ in self.non_metal_elems):

                        metal = atom_id_2_ if atom_id_1_ in self.non_metal_elems else atom_id_1_
                        metal = metal.title()

                        if target_value >= 2.0 and target_value <= 2.2:
                            other_bond_type = 'O...' + metal
                            other_bond = True
                        elif target_value < 2.0:
                            other_bond_type = 'O...' + metal + ' (too close!)'
                            other_bond = True

                    elif (atom_id_1_ == 'P' and not atom_id_2_ in self.non_metal_elems) or (atom_id_2_ == 'P' and not atom_id_1_ in self.non_metal_elems):

                        metal = atom_id_2_ if atom_id_1_ in self.non_metal_elems else atom_id_1_
                        metal = metal.title()

                        if target_value >= 2.1 and target_value <= 2.5:
                            other_bond_type = 'P...' + metal
                            other_bond = True
                        elif target_value < 2.1:
                            other_bond_type = 'P...' + metal + ' (too close!)'
                            other_bond = True

                    elif (atom_id_1_ == 'S' and not atom_id_2_ in self.non_metal_elems) or (atom_id_2_ == 'S' and not atom_id_1_ in self.non_metal_elems):

                        metal = atom_id_2_ if atom_id_1_ in self.non_metal_elems else atom_id_1_
                        metal = metal.title()

                        if target_value >= 2.2 and target_value <= 2.6:
                            other_bond_type = 'S...' + metal
                            other_bond = True
                        elif target_value < 2.2:
                            other_bond_type = 'S...' + metal + ' (too close!)'
                            other_bond = True

                    elif (atom_id_1_ == 'SE' and not atom_id_2_ in self.non_metal_elems) or (atom_id_2_ == 'SE' and not atom_id_1_ in self.non_metal_elems):

                        metal = atom_id_2_ if atom_id_1_ in self.non_metal_elems else atom_id_1_
                        metal = metal.title()

                        if target_value >= 2.3 and target_value <= 2.7:
                            other_bond_type = 'Se...' + metal
                            other_bond = True
                        elif target_value < 2.3:
                            other_bond_type = 'Se...' + metal + ' (too close!)'
                            other_bond = True

                    else:

                        for j in lp_data:

                            if j is i:
                                continue

                            _chain_id_1 = j[chain_id_1_name]
                            _chain_id_2 = j[chain_id_2_name]
                            _seq_id_1 = j[seq_id_1_name]
                            _seq_id_2 = j[seq_id_2_name]
                            _comp_id_1 = j[comp_id_1_name]
                            _comp_id_2 = j[comp_id_2_name]

                            if _chain_id_1 != _chain_id_2 and _chain_id_1 != chain_id_1 and _chain_id_2 != chain_id_2:

                                if seq_id_1 == _seq_id_1 and comp_id_1 == _comp_id_1 and\
                                   seq_id_2 == _seq_id_2 and comp_id_2 == _comp_id_2:
                                    symmetry = True
                                    break

                                elif seq_id_1 == _seq_id_2 and comp_id_1 == _comp_id_2 and\
                                     seq_id_2 == _seq_id_1 and comp_id_2 == _comp_id_1:
                                    symmetry = True
                                    break

                range_of_seq = abs(seq_id_1 - seq_id_2)

                if hydrogen_bond:
                    if chain_id_1 != chain_id_2:
                        data_type = 'inter-chain_hydrogen_bonds'
                    elif range_of_seq > 5:
                        data_type = 'long_range_hydrogen_bonds'
                    else:
                        data_type = 'hydrogen_bonds'
                    data_type += '_' + hydrogen_bond_type

                    if 'too close!' in hydrogen_bond_type:

                        values = ''
                        if not i[target_value_name] is None:
                            values += '%s %s, ' % (target_value_name, i[target_value_name])
                        if not i[lower_limit_name] is None:
                            values += '%s %s, ' % (lower_limit_name, i[lower_limit_name])
                        if not i[upper_limit_name] is None:
                            values += '%s %s, ' % (upper_limit_name, i[upper_limit_name])
                        if not i[lower_linear_limit_name] is None:
                            values += '%s %s, ' % (lower_linear_limit_name, i[lower_linear_limit_name])
                        if not i[upper_linear_limit_name] is None:
                            values += '%s %s, ' % (upper_linear_limit_name, i[upper_linear_limit_name])

                        warn = "Hydrogen bond constraint (chain_id_1 %s, seq_id_1 %s, comp_id_1 %s, atom_id_1 %s, chain_id_2 %s, seq_id_2 %s, comp_id_2 %s, atom_id_2 %s) is too close (%s)." %\
                               (chain_id_1, seq_id_1, comp_id_1, atom_id_1, chain_id_2, seq_id_2, comp_id_2, atom_id_2, values[:-2])

                        self.report.warning.appendDescription('unusual_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'description': warn})
                        self.report.setWarning()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__calculateStatsOfDistanceRestraint() ++ Warning  - %s\n" % warn)

                elif disulfide_bond:
                    if chain_id_1 != chain_id_2:
                        data_type = 'inter-chain_disulfide_bonds'
                    elif range_of_seq > 5:
                        data_type = 'long_range_disulfide_bonds'
                    else:
                        data_type = 'disulfide_bonds'
                    data_type += '_' + disulfide_bond_type

                    if 'too close!' in disulfide_bond_type:

                        values = ''
                        if not i[target_value_name] is None:
                            values += '%s %s, ' % (target_value_name, i[target_value_name])
                        if not i[lower_limit_name] is None:
                            values += '%s %s, ' % (lower_limit_name, i[lower_limit_name])
                        if not i[upper_limit_name] is None:
                            values += '%s %s, ' % (upper_limit_name, i[upper_limit_name])
                        if not i[lower_linear_limit_name] is None:
                            values += '%s %s, ' % (lower_linear_limit_name, i[lower_linear_limit_name])
                        if not i[upper_linear_limit_name] is None:
                            values += '%s %s, ' % (upper_linear_limit_name, i[upper_linear_limit_name])

                        warn = "Disulfide bond constraint (chain_id_1 %s, seq_id_1 %s, comp_id_1 %s, atom_id_1 %s, chain_id_2 %s, seq_id_2 %s, comp_id_2 %s, atom_id_2 %s) is too close (%s)." %\
                               (chain_id_1, seq_id_1, comp_id_1, atom_id_1, chain_id_2, seq_id_2, comp_id_2, atom_id_2, values[:-2])

                        self.report.warning.appendDescription('unusual_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'description': warn})
                        self.report.setWarning()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__calculateStatsOfDistanceRestraint() ++ Warning  - %s\n" % warn)

                elif diselenide_bond:
                    if chain_id_1 != chain_id_2:
                        data_type = 'inter-chain_diselenide_bonds'
                    elif range_of_seq > 5:
                        data_type = 'long_range_diselenide_bonds'
                    else:
                        data_type = 'diselenide_bonds'
                    data_type += '_' + diselenide_bond_type

                    if 'too close!' in diselenide_bond_type:

                        values = ''
                        if not i[target_value_name] is None:
                            values += '%s %s, ' % (target_value_name, i[target_value_name])
                        if not i[lower_limit_name] is None:
                            values += '%s %s, ' % (lower_limit_name, i[lower_limit_name])
                        if not i[upper_limit_name] is None:
                            values += '%s %s, ' % (upper_limit_name, i[upper_limit_name])
                        if not i[lower_linear_limit_name] is None:
                            values += '%s %s, ' % (lower_linear_limit_name, i[lower_linear_limit_name])
                        if not i[upper_linear_limit_name] is None:
                            values += '%s %s, ' % (upper_linear_limit_name, i[upper_linear_limit_name])

                        warn = "Diselenide bond constraint (chain_id_1 %s, seq_id_1 %s, comp_id_1 %s, atom_id_1 %s, chain_id_2 %s, seq_id_2 %s, comp_id_2 %s, atom_id_2 %s) is too close (%s)." %\
                               (chain_id_1, seq_id_1, comp_id_1, atom_id_1, chain_id_2, seq_id_2, comp_id_2, atom_id_2, values[:-2])

                        self.report.warning.appendDescription('unusual_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'description': warn})
                        self.report.setWarning()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__calculateStatsOfDistanceRestraint() ++ Warning  - %s\n" % warn)

                elif other_bond:
                    if chain_id_1 != chain_id_2:
                        data_type = 'inter-chain_other_bonds'
                    elif range_of_seq > 5:
                        data_type = 'long_range_other_bonds'
                    else:
                        data_type = 'other_bonds'
                    data_type += '_' + other_bond_type

                    if 'too close!' in other_bond_type:

                        values = ''
                        if not i[target_value_name] is None:
                            values += '%s %s, ' % (target_value_name, i[target_value_name])
                        if not i[lower_limit_name] is None:
                            values += '%s %s, ' % (lower_limit_name, i[lower_limit_name])
                        if not i[upper_limit_name] is None:
                            values += '%s %s, ' % (upper_limit_name, i[upper_limit_name])
                        if not i[lower_linear_limit_name] is None:
                            values += '%s %s, ' % (lower_linear_limit_name, i[lower_linear_limit_name])
                        if not i[upper_linear_limit_name] is None:
                            values += '%s %s, ' % (upper_linear_limit_name, i[upper_linear_limit_name])

                        warn = "Other bond constraint (chain_id_1 %s, seq_id_1 %s, comp_id_1 %s, atom_id_1 %s, chain_id_2 %s, seq_id_2 %s, comp_id_2 %s, atom_id_2 %s) is too close (%s)." %\
                               (chain_id_1, seq_id_1, comp_id_1, atom_id_1, chain_id_2, seq_id_2, comp_id_2, atom_id_2, values[:-2])

                        self.report.warning.appendDescription('unusual_data', {'file_name': file_name, 'sf_framecode': sf_framecode, 'description': warn})
                        self.report.setWarning()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__calculateStatsOfDistanceRestraint() ++ Warning  - %s\n" % warn)

                elif symmetry:
                    data_type = 'symmetric_constraints'
                elif chain_id_1 != chain_id_2:
                    data_type = 'inter-chain_constraints'
                elif range_of_seq == 0:
                    data_type = 'intra-residue_constraints'
                elif range_of_seq < 5:

                    if file_type == 'nef':
                        _atom_id_1 = self.__nefT.get_nmrstar_atom(comp_id_1, atom_id_1, leave_unmatched=False)[0]
                        _atom_id_2 = self.__nefT.get_nmrstar_atom(comp_id_2, atom_id_2, leave_unmatched=False)[0]

                        if len(_atom_id_1) > 0 and len(_atom_id_2) > 0:
                            is_sc_atom_1 = _atom_id_1[0] in self.__csStat.getSideChainAtoms(comp_id_1)
                            is_sc_atom_2 = _atom_id_2[0] in self.__csStat.getSideChainAtoms(comp_id_2)

                            if is_sc_atom_1:
                                is_bb_atom_1 = False
                            else:
                                is_bb_atom_1 = _atom_id_1[0] in self.__csStat.getBackBoneAtoms(comp_id_1)

                            if is_sc_atom_2:
                                is_bb_atom_2 = False
                            else:
                                is_bb_atom_2 = _atom_id_2[0] in self.__csStat.getBackBoneAtoms(comp_id_2)

                        else:
                            is_bb_atom_1 = False
                            is_bb_atom_2 = False
                            is_sc_atom_1 = False
                            is_sc_atom_2 = False

                    else:
                        is_sc_atom_1 = atom_id_1 in self.__csStat.getSideChainAtoms(comp_id_1)
                        is_sc_atom_2 = atom_id_2 in self.__csStat.getSideChainAtoms(comp_id_2)

                        if is_sc_atom_1:
                            is_bb_atom_1 = False
                        else:
                            is_bb_atom_1 = atom_id_1 in self.__csStat.getBackBoneAtoms(comp_id_1)

                        if is_sc_atom_2:
                            is_bb_atom_2 = False
                        else:
                            is_bb_atom_2 = atom_id_2 in self.__csStat.getBackBoneAtoms(comp_id_2)

                    is_bb_bb = is_bb_atom_1 and is_bb_atom_2
                    is_bb_sc = (is_bb_atom_1 and is_sc_atom_2) or (is_sc_atom_1 and is_bb_atom_2)
                    is_sc_sc = is_sc_atom_1 and is_sc_atom_2

                    if range_of_seq == 1:
                        data_type = 'sequential_constraints'
                    else:
                        data_type = 'medium_range_constraints'

                    if is_bb_bb:
                        data_type += '_backbone-backbone'
                    elif is_bb_sc:
                        data_type += '_backbone-sidechain'
                    elif is_sc_sc:
                        data_type += '_sidechain-sidechain'
                else:
                    data_type = 'long_range_constraints'

                if data_type in count:
                    count[data_type] += 1
                else:
                    count[data_type] = 1

                # detect potential type

                targe_value = i[target_value_name]
                lower_limit_value = i[lower_limit_name]
                upper_limit_value = i[upper_limit_name]
                lower_linear_limit_value = i[lower_linear_limit_name]
                upper_linear_limit_value = i[upper_linear_limit_name]

                if (not lower_limit_value is None) and\
                   (not upper_limit_value is None) and\
                   lower_linear_limit_value is None and\
                   upper_linear_limit_value is None:
                    potential_type = 'square-well-parabolic'
                elif (not lower_limit_value is None) and\
                   (not upper_limit_value is None) and\
                   (not lower_linear_limit_value is None) and\
                   (not upper_linear_limit_value is None):
                    potential_type = 'square-well-parabolic-linear'
                elif lower_limit_value is None and\
                   (not upper_limit_value is None) and\
                   lower_linear_limit_value is None and\
                   upper_linear_limit_value is None:
                    potential_type = 'upper-bound-parabolic'
                elif (not lower_limit_value is None) and\
                   upper_limit_value is None and\
                   lower_linear_limit_value is None and\
                   upper_linear_limit_value is None:
                    potential_type = 'lower-bound-parabolic'
                elif lower_limit_value is None and\
                   (not upper_limit_value is None) and\
                   lower_linear_limit_value is None and\
                   (not upper_linear_limit_value is None):
                    potential_type = 'upper-bound-parabolic-linear'
                elif (not lower_limit_value is None) and\
                   upper_limit_value is None and\
                   (not lower_linear_limit_value is None) and\
                   upper_linear_limit_value is None:
                    potential_type = 'lower-bound-parabolic-linear'
                elif (not target_value is None) and\
                   lower_limit_value is None and\
                   upper_limit_value is None and\
                   lower_linear_limit_value is None and\
                   upper_linear_limit_value is None:
                    potential_type = 'log-harmonic'
                else:
                    potential_type = 'unknown'

                if potential_type in potential:
                    potential[potential_type] += 1
                else:
                    potential[potential_type] = 1

            if len(count) == 0:
                return

            ent['number_of_constraints'] = count
            ent['number_of_potential_types'] = potential
            ent['range'] = {'max_value': max_val, 'min_value': min_val}
            ent['ambiguous_constraint_sets'] = len(comb_id_set)

            target_scale = (max_val - min_val) / 10.0

            scale = 1.0

            while scale < target_scale:
                scale *= 2.0

            while scale > target_scale:
                scale /= 2.0

            range_of_vals = []
            count_of_vals = []

            v = 0.0
            while v < min_val:
                v += scale

            while v > min_val:
                v -= scale

            while v < max_val:

                _count = copy.copy(count)

                for k in count.keys():
                    _count[k] = 0

                for i in lp_data:
                    chain_id_1 = i[chain_id_1_name]
                    chain_id_2 = i[chain_id_2_name]
                    seq_id_1 = i[seq_id_1_name]
                    seq_id_2 = i[seq_id_2_name]
                    comp_id_1 = i[comp_id_1_name]
                    comp_id_2 = i[comp_id_2_name]
                    atom_id_1 = i[atom_id_1_name]
                    atom_id_2 = i[atom_id_2_name]

                    target_value = i[target_value_name]

                    upper_limit_value = None
                    lower_limit_value = None

                    if target_value is None:

                        if not i[lower_limit_name] is None and not i[upper_limit_name] is None:
                            target_value = (i[lower_limit_name] + i[upper_limit_name]) / 2.0

                        elif not i[lower_linear_limit_name] is None and not i[upper_linear_limit_name] is None:
                            target_value = (i[lower_linear_limit_name] + i[upper_linear_limit_name]) / 2.0

                        elif not i[upper_linear_limit_name] is None:
                            target_value = i[upper_linear_limit_name]
                            upper_limit_value = target_value

                        elif not i[upper_limit_name] is None:
                            target_value = i[upper_limit_name]
                            upper_limit_value = target_value

                        elif not i[lower_linear_limit_name] is None:
                            target_value = i[lower_linear_limit_name]
                            lower_limit_value = target_value

                        elif not i[lower_limit_name] is None:
                            target_value = i[lower_limit_name]
                            lower_limit_value = target_value

                        else:
                            continue

                    if target_value < v or target_value >= v + scale:
                        continue

                    hydrogen_bond_type = None
                    hydrogen_bond = False
                    disulfide_bond_type = None
                    disulfide_bond = False
                    diselenide_bond_type = None
                    diselenide_bond = False
                    other_bond_type = None
                    other_bond = False
                    symmetry = False

                    if chain_id_1 != chain_id_2 or seq_id_1 != seq_id_2:

                        atom_id_1_ = atom_id_1[0]
                        atom_id_2_ = atom_id_2[0]

                        if not upper_limit_value is None:
                            target_value -= 0.4
                        elif not lower_limit_value is None:
                            target_value += 0.4

                        if (atom_id_1_ == 'F' and atom_id_2_ == 'H') or (atom_id_2_ == 'F' and atom_id_1_ == 'H'):

                            if target_value >= 1.2 and target_value <= 1.5:
                                hydrogen_bond_type = 'F...H-F'
                                hydrogen_bond = True
                            elif target_value < 1.2:
                                hydrogen_bond_type = 'F...H-F (too close!)'
                                hydrogen_bond = True

                        elif (atom_id_1_ == 'F' and atom_id_2_ == 'F') or (atom_id_2_ == 'F' and atom_id_1_ == 'F'):

                            if target_value >= 2.2 and target_value <= 2.5:
                                hydrogen_bond_type = 'F...h-F'
                                hydrogen_bond = True
                            elif target_value < 2.2:
                                hydrogen_bond_type = 'F...h-F (too close!)'
                                hydrogen_bond = True

                        elif (atom_id_1_ == 'O' and atom_id_2_ == 'H') or (atom_id_2_ == 'O' and atom_id_1_ == 'H'):

                            if target_value >= 1.5 and target_value <= 2.2:
                                hydrogen_bond_type = 'O...H-x'
                                hydrogen_bond = True
                            elif target_value < 1.5:
                                hydrogen_bond_type = 'O...H-x (too close!)'
                                hydrogen_bond = True

                        elif (atom_id_1_ == 'O' and atom_id_2_ == 'N') or (atom_id_2_ == 'O' and atom_id_1_ == 'N'):

                            if target_value >= 2.5 and target_value <= 3.2:
                                hydrogen_bond_type = 'O...h-N'
                                hydrogen_bond = True
                            elif target_value < 2.5:
                                hydrogen_bond_type = 'O...h-N (too close!)'
                                hydrogen_bond = True

                        elif (atom_id_1_ == 'O' and atom_id_2_ == 'O') or (atom_id_2_ == 'O' and atom_id_1_ == 'O'):

                            if target_value >= 2.5 and target_value <= 3.2:
                                hydrogen_bond_type = 'O...h-O'
                                hydrogen_bond = True
                            elif target_value < 2.5:
                                hydrogen_bond_type = 'O...h-O (too close!)'
                                hydrogen_bond = True

                        elif (atom_id_1_ == 'N' and atom_id_2_ == 'H') or (atom_id_2_ == 'N' and atom_id_1_ == 'H'):

                            if target_value >= 1.5 and target_value <= 2.2:
                                hydrogen_bond_type = 'N...H-x'
                                hydrogen_bond = True
                            elif target_value < 1.5:
                                hydrogen_bond_type = 'N...H-x (too close!)'
                                hydrogen_bond = True

                        elif (atom_id_1_ == 'N' and atom_id_2_ == 'N') or (atom_id_2_ == 'N' and atom_id_1_ == 'N'):

                            if target_value >= 2.5 and target_value <= 3.2:
                                hydrogen_bond_type = 'N...h_N'
                                hydrogen_bond = True
                            elif target_value < 2.5:
                                hydrogen_bond_type = 'N...h_N (too close!)'
                                hydrogen_bond = True

                        elif atom_id_1_ == 'S' and atom_id_2_ == 'S':

                            if target_value >= 1.9 and target_value <= 2.3:
                                disulfide_bond_type = 'S...S'
                                disulfide_bond = True
                            elif target_value < 1.9:
                                disulfide_bond_type = 'S...S (too close!)'
                                disulfide_bond = True

                        elif atom_id_1_ == 'SE' and atom_id_2_ == 'SE':

                            if target_value >= 2.1 and target_value <= 2.6:
                                diselenide_bond_type = 'Se...Se'
                                diselenide_bond = True
                            elif target_value < 2.1:
                                diselenide_bond_type = 'Se...Se (too close!)'
                                diselenide_bond = True

                        elif (atom_id_1_ == 'N' and not atom_id_2_ in self.non_metal_elems) or (atom_id_2_ == 'N' and not atom_id_1_ in self.non_metal_elems):

                            metal = atom_id_2_ if atom_id_1_ in self.non_metal_elems else atom_id_1_
                            metal = metal.title()

                            if target_value >= 1.9 and target_value <= 2.1:
                                other_bond_type = 'N...' + metal
                                other_bond = True
                            elif target_value < 1.9:
                                other_bond_type = 'N...' + metal + ' (too close!)'
                                other_bond = True

                        elif (atom_id_1_ == 'O' and not atom_id_2_ in self.non_metal_elems) or (atom_id_2_ == 'O' and not atom_id_1_ in self.non_metal_elems):

                            metal = atom_id_2_ if atom_id_1_ in self.non_metal_elems else atom_id_1_
                            metal = metal.title()

                            if target_value >= 2.0 and target_value <= 2.2:
                                other_bond_type = 'O...' + metal
                                other_bond = True
                            elif target_value < 2.0:
                                other_bond_type = 'O...' + metal + ' (too close!)'
                                other_bond = True

                        elif (atom_id_1_ == 'P' and not atom_id_2_ in self.non_metal_elems) or (atom_id_2_ == 'P' and not atom_id_1_ in self.non_metal_elems):

                            metal = atom_id_2_ if atom_id_1_ in self.non_metal_elems else atom_id_1_
                            metal = metal.title()

                            if target_value >= 2.1 and target_value <= 2.5:
                                other_bond_type = 'P...' + metal
                                other_bond = True
                            elif target_value < 2.1:
                                other_bond_type = 'P...' + metal + ' (too close!)'
                                other_bond = True

                        elif (atom_id_1_ == 'S' and not atom_id_2_ in self.non_metal_elems) or (atom_id_2_ == 'S' and not atom_id_1_ in self.non_metal_elems):

                            metal = atom_id_2_ if atom_id_1_ in self.non_metal_elems else atom_id_1_
                            metal = metal.title()

                            if target_value >= 2.2 and target_value <= 2.6:
                                other_bond_type = 'S...' + metal
                                other_bond = True
                            elif target_value < 2.2:
                                other_bond_type = 'S...' + metal + ' (too close!)'
                                other_bond = True

                        elif (atom_id_1_ == 'SE' and not atom_id_2_ in self.non_metal_elems) or (atom_id_2_ == 'SE' and not atom_id_1_ in self.non_metal_elems):

                            metal = atom_id_2_ if atom_id_1_ in self.non_metal_elems else atom_id_1_
                            metal = metal.title()

                            if target_value >= 2.3 and target_value <= 2.7:
                                other_bond_type = 'Se...' + metal
                                other_bond = True
                            elif target_value < 2.3:
                                other_bond_type = 'Se...' + metal + ' (too close!)'
                                other_bond = True

                        else:

                            for j in lp_data:

                                if j is i:
                                    continue

                                _chain_id_1 = j[chain_id_1_name]
                                _chain_id_2 = j[chain_id_2_name]
                                _seq_id_1 = j[seq_id_1_name]
                                _seq_id_2 = j[seq_id_2_name]
                                _comp_id_1 = j[comp_id_1_name]
                                _comp_id_2 = j[comp_id_2_name]

                                if _chain_id_1 != _chain_id_2 and _chain_id_1 != chain_id_1 and _chain_id_2 != chain_id_2:

                                    if seq_id_1 == _seq_id_1 and comp_id_1 == _comp_id_1 and\
                                       seq_id_2 == _seq_id_2 and comp_id_2 == _comp_id_2:
                                        symmetry = True
                                        break

                                    elif seq_id_1 == _seq_id_2 and comp_id_1 == _comp_id_2 and\
                                         seq_id_2 == _seq_id_1 and comp_id_2 == _comp_id_1:
                                        symmetry = True
                                        break

                    range_of_seq = abs(seq_id_1 - seq_id_2)

                    if hydrogen_bond:
                        if chain_id_1 != chain_id_2:
                            data_type = 'inter-chain_hydrogen_bonds'
                        elif range_of_seq > 5:
                            data_type = 'long_range_hydrogen_bonds'
                        else:
                            data_type = 'hydrogen_bonds'
                        data_type += '_' + hydrogen_bond_type
                    elif disulfide_bond:
                        if chain_id_1 != chain_id_2:
                            data_type = 'inter-chain_disulfide_bonds'
                        elif range_of_seq > 5:
                            data_type = 'long_range_disulfide_bonds'
                        else:
                            data_type = 'disulfide_bonds'
                        data_type += '_' + disulfide_bond_type
                    elif diselenide_bond:
                        if chain_id_1 != chain_id_2:
                            data_type = 'inter-chain_diselenide_bonds'
                        elif range_of_seq > 5:
                            data_type = 'long_range_diselenide_bonds'
                        else:
                            data_type = 'diselenide_bonds'
                        data_type += '_' + diselenide_bond_type
                    elif other_bond:
                        if chain_id_1 != chain_id_2:
                            data_type = 'inter-chain_other_bonds'
                        elif range_of_seq > 5:
                            data_type = 'long_range_other_bonds'
                        else:
                            data_type = 'other_bonds'
                        data_type += '_' + other_bond_type
                    elif symmetry:
                        data_type = 'symmetric_constraints'
                    elif chain_id_1 != chain_id_2:
                        data_type = 'inter-chain_constraints'
                    elif range_of_seq == 0:
                        data_type = 'intra-residue_constraints'
                    elif range_of_seq < 5:

                        if file_type == 'nef':
                            _atom_id_1 = self.__nefT.get_nmrstar_atom(comp_id_1, atom_id_1, leave_unmatched=False)[0]
                            _atom_id_2 = self.__nefT.get_nmrstar_atom(comp_id_2, atom_id_2, leave_unmatched=False)[0]

                            if len(_atom_id_1) > 0 and len(_atom_id_2) > 0:
                                is_sc_atom_1 = _atom_id_1[0] in self.__csStat.getSideChainAtoms(comp_id_1)
                                is_sc_atom_2 = _atom_id_2[0] in self.__csStat.getSideChainAtoms(comp_id_2)

                                if is_sc_atom_1:
                                    is_bb_atom_1 = False
                                else:
                                    is_bb_atom_1 = _atom_id_1[0] in self.__csStat.getBackBoneAtoms(comp_id_1)

                                if is_sc_atom_2:
                                    is_bb_atom_2 = False
                                else:
                                    is_bb_atom_2 = _atom_id_2[0] in self.__csStat.getBackBoneAtoms(comp_id_2)

                            else:
                                is_bb_atom_1 = False
                                is_bb_atom_2 = False
                                is_sc_atom_1 = False
                                is_sc_atom_2 = False

                        else:
                            is_sc_atom_1 = atom_id_1 in self.__csStat.getSideChainAtoms(comp_id_1)
                            is_sc_atom_2 = atom_id_2 in self.__csStat.getSideChainAtoms(comp_id_2)

                            if is_sc_atom_1:
                                is_bb_atom_1 = False
                            else:
                                is_bb_atom_1 = atom_id_1 in self.__csStat.getBackBoneAtoms(comp_id_1)

                            if is_sc_atom_2:
                                is_bb_atom_2 = False
                            else:
                                is_bb_atom_2 = atom_id_2 in self.__csStat.getBackBoneAtoms(comp_id_2)

                        is_bb_bb = is_bb_atom_1 and is_bb_atom_2
                        is_bb_sc = (is_bb_atom_1 and is_sc_atom_2) or (is_sc_atom_1 and is_bb_atom_2)
                        is_sc_sc = is_sc_atom_1 and is_sc_atom_2

                        if range_of_seq == 1:
                            data_type = 'sequential_constraints'
                        else:
                            data_type = 'medium_range_constraints'

                        if is_bb_bb:
                            data_type += '_backbone-backbone'
                        elif is_bb_sc:
                            data_type += '_backbone-sidechain'
                        elif is_sc_sc:
                            data_type += '_sidechain-sidechain'
                    else:
                        data_type = 'long_range_constraints'

                    _count[data_type] += 1

                range_of_vals.append(v)
                count_of_vals.append(_count)

                v += scale

            transposed = {}

            for k in count.keys():
                transposed[k] = []

                for j in range(len(range_of_vals)):
                    transposed[k].append(count_of_vals[j][k])

            if len(range_of_vals) > 1:
                """
                has_value = False
                for j in range(1, len(range_of_vals) - 1):
                    for k in count.keys():
                        if transposed[k][j] > 0:
                            has_value = True
                            break
                    if has_value:
                        break

                if has_value:
                """
                ent['histogram'] = {'range_of_values': range_of_vals, 'number_of_values': transposed}

        except Exception as e:

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__calculateStatsOfDistanceRestraint() ++ Error  - %s" % str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__calculateStatsOfDistanceRestraint() ++ Error  - %s" % str(e))

    def __calculateStatsOfDihedralRestraint(self, lp_data, ent):
        """ Calculate statistics of dihedral angle restraints.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        item_names = self.potential_items[file_type]['dihed_restraint']
        target_value_name = item_names['target_value']
        lower_limit_name = item_names['lower_limit']
        upper_limit_name = item_names['upper_limit']
        lower_linear_limit_name = item_names['lower_linear_limit']
        upper_linear_limit_name = item_names['upper_linear_limit']

        dh_item_names = self.item_names_in_dh_loop[file_type]
        chain_id_1_name = dh_item_names['chain_id_1']
        chain_id_2_name = dh_item_names['chain_id_2']
        chain_id_3_name = dh_item_names['chain_id_3']
        chain_id_4_name = dh_item_names['chain_id_4']
        seq_id_1_name = dh_item_names['seq_id_1']
        seq_id_2_name = dh_item_names['seq_id_2']
        seq_id_3_name = dh_item_names['seq_id_3']
        seq_id_4_name = dh_item_names['seq_id_4']
        comp_id_1_name = dh_item_names['comp_id_1']
        comp_id_2_name = dh_item_names['comp_id_2']
        comp_id_3_name = dh_item_names['comp_id_3']
        comp_id_4_name = dh_item_names['comp_id_4']
        atom_id_1_name = dh_item_names['atom_id_1']
        atom_id_2_name = dh_item_names['atom_id_2']
        atom_id_3_name = dh_item_names['atom_id_3']
        atom_id_4_name = dh_item_names['atom_id_4']
        angle_type_name = dh_item_names['angle_type']

        dihed_atom_ids = ['N', 'CA', 'C']

        chi1_atom_id_4_pat = re.compile(r'^[COS]G1?$')
        chi2_atom_id_3_pat = re.compile(r'^CG1?$')
        chi2_atom_id_4_pat = re.compile(r'^[CNOS]D1?$')
        chi3_atom_id_3_pat = re.compile(r'^[CS]D$')
        chi3_atom_id_4_pat = re.compile(r'^[CNO]E1?$')
        chi4_atom_id_3_pat = re.compile(r'^[CN]E$')
        chi4_atom_id_4_pat = re.compile(r'^[CN]Z$')

        try:

            count = {}
            potential = {}

            phi_list = []
            psi_list = []
            chi1_list = []
            chi2_list = []

            for i in lp_data:
                target_value = i[target_value_name]

                if target_value is None:

                    if not i[lower_limit_name] is None and not i[upper_limit_name] is None:
                        target_value = (i[lower_limit_name] + i[upper_limit_name]) / 2.0

                    elif not i[lower_linear_limit_name] is None and not i[upper_linear_limit_name] is None:
                        target_value = (i[lower_linear_limit_name] + i[upper_linear_limit_name]) / 2.0

                    else:
                        continue

                target_value = float('{:.1f}'.format(target_value))

                while target_value > 180.0:
                    target_value -= 360.0
                while target_value < -180.0:
                    target_value += 360.0

                if not i[lower_limit_name] is None and not i[upper_limit_name] is None:
                    lower_limit = i[lower_limit_name]
                    upper_limit = i[upper_limit_name]

                    while lower_limit - target_value > 180.0:
                        lower_limit -= 360.0
                    while lower_limit - target_value < -180.0:
                        lower_limit += 360.0

                    while upper_limit - target_value > 180.0:
                        upper_limit -= 360.0
                    while upper_limit - target_value < -180.0:
                        upper_limit += 360.0

                elif not i[lower_linear_limit_name] is None and not i[upper_linear_limit_name] is None:
                    lower_limit = i[lower_linear_limit_name]
                    upper_limit = i[upper_linear_limit_name]

                    while lower_limit - target_value > 180.0:
                        lower_limit -= 360.0
                    while lower_limit - target_value < -180.0:
                        lower_limit += 360.0

                    while upper_limit - target_value > 180.0:
                        upper_limit -= 360.0
                    while upper_limit - target_value < -180.0:
                        upper_limit += 360.0

                else:
                    lower_limit = None
                    upper_limit = None

                chain_id_1 = i[chain_id_1_name]
                chain_id_2 = i[chain_id_2_name]
                chain_id_3 = i[chain_id_3_name]
                chain_id_4 = i[chain_id_4_name]
                seq_ids = []
                seq_ids.append(i[seq_id_1_name])
                seq_ids.append(i[seq_id_2_name])
                seq_ids.append(i[seq_id_3_name])
                seq_ids.append(i[seq_id_4_name])
                comp_id = i[comp_id_1_name]
                comp_ids = []
                comp_ids.append(i[comp_id_1_name])
                comp_ids.append(i[comp_id_2_name])
                comp_ids.append(i[comp_id_3_name])
                comp_ids.append(i[comp_id_4_name])
                atom_ids = []
                atom_ids.append(i[atom_id_1_name])
                atom_ids.append(i[atom_id_2_name])
                atom_ids.append(i[atom_id_3_name])
                atom_ids.append(i[atom_id_4_name])
                data_type = i[angle_type_name]

                seq_id_common = collections.Counter(seq_ids).most_common()
                comp_id_common = collections.Counter(comp_ids).most_common()

                if data_type in self.empty_value:

                    data_type = 'unknown'

                    if chain_id_1 == chain_id_2 and chain_id_2 == chain_id_3 and chain_id_3 == chain_id_4:

                        polypeptide_like = self.__csStat.getTypeOfCompId(comp_id)[0]

                        if polypeptide_like:

                            if len(seq_id_common) == 2:

                                # phi or psi

                                if seq_id_common[0][1] == 3 and seq_id_common[1][1] == 1:

                                    # phi

                                    seq_id_prev = seq_id_common[1][0]

                                    if seq_id_common[0][0] == seq_id_prev + 1:

                                        j = 0
                                        if seq_ids[j] == seq_id_prev and atom_ids[j] == 'C':
                                            atom_ids.pop(j)
                                            if atom_ids == dihed_atom_ids:
                                                data_type = 'phi'

                                    # psi

                                    seq_id_next = seq_id_common[1][0]

                                    if seq_id_common[0][0] == seq_id_next - 1:

                                        j = 3
                                        if seq_ids[j] == seq_id_next and atom_ids[j] == 'N':
                                            atom_ids.pop(j)
                                            if atom_ids == dihed_atom_ids:
                                                data_type = 'psi'

                                # omega

                                if atom_ids[0] == 'O' and atom_ids[1] == 'C' and atom_ids[2] == 'N' and (atom_ids[3] == 'H' or atom_ids[3] == 'CA') and\
                                   seq_ids[0] == seq_ids[1] and seq_ids[1] + 1 == seq_ids[2] and seq_ids[2] == seq_ids[3]:
                                    data_type = 'omega'

                            elif len(seq_id_common) == 1:

                                # chi1

                                if atom_ids[0] == 'N' and atom_ids[1] == 'CA' and atom_ids[2] == 'CB' and chi1_atom_id_4_pat.match(atom_ids[3]):
                                    #if (atom_ids[3] == 'CG' and comp_id in ['ARG', 'ASN', 'ASP', 'GLN', 'GLU', 'HIS', 'LEU', 'LYS', 'MET', 'PHE', 'PRO', 'TRP', 'TYR']) or\
                                    #   (atom_ids[3] == 'CG1' and comp_id in ['ILE', 'VAL']) or\
                                    #   (atom_ids[3] == 'OG' and comp_id == 'SER') or\
                                    #   (atom_ids[3] == 'OG1' and comp_id == 'THR') or\
                                    #   (atom_ids[3] == 'SG' and comp_id == 'CYS'):
                                    data_type = 'chi1'

                                # chi2

                                if atom_ids[0] == 'CA' and atom_ids[1] == 'CB' and chi2_atom_id_3_pat(atom_ids[2]) and chi2_atom_id_4_pat(atom_ids[3]):
                                    #if (atom_ids[2] == 'CG' and atom_ids[3] == 'CD' and comp_id in ['ARG', 'GLN', 'GLU', 'LYS', 'PRO']) or\
                                    #   (atom_ids[2] == 'CG' and atom_ids[3] == 'CD1' and comp_id in ['LEU', 'PHE', 'TRP', 'TYR']) or\
                                    #   (atom_ids[2] == 'CG' and atom_ids[3] == 'ND1' and comp_id == 'HIS') or\
                                    #   (atom_ids[2] == 'CG' and atom_ids[3] == 'OD1' and comp_id in ['ASN', 'ASP']) or\
                                    #   (atom_ids[2] == 'CG' and atom_ids[3] == 'SD' and comp_id == 'MET') or\
                                    #   (atom_ids[2] == 'CG1' and atom_ids[3] == 'CD' and comp_id == 'ILE'):
                                    data_type = 'chi2'

                                # chi3

                                if atom_ids[0] == 'CB' and atom_ids[1] == 'CG' and chi3_atom_id_3_pat(atom_ids[2]) and chi3_atom_id_4_pat(atom_ids[3]):
                                    #if (atom_ids[2] == 'CD' and atom_ids[3] == 'CE' and comp_id == 'LYS') or\
                                    #   (atom_ids[2] == 'CD' and atom_ids[3] == 'NE' and comp_id == 'ARG') or\
                                    #   (atom_ids[2] == 'CD' and atom_ids[3] == 'OE1' and comp_id in ['GLN', 'GLU']) or\
                                    #   (atom_ids[2] == 'SD' and atom_ids[3] == 'CE' and comp_id == 'MET'):
                                    data_type = 'chi3'

                                # chi4

                                if atom_ids[0] == 'CG' and atom_ids[1] == 'CD' and chi4_atom_id_3_pat(atom_ids[2]) and chi4_atom_id_4_par(atom_ids[3]):
                                    #if (atom_ids[2] == 'NE' and atom_ids[3] == 'CZ' and comp_id == 'ARG') or\
                                    #  (atom_ids[2] == 'CE' and atom_ids[3] == 'NZ' and comp_id == 'LYS'):
                                    data_type = 'chi4'

                                # chi5

                                if atom_ids == ['CD', 'NE', 'CZ', 'NH1']: # and comp_id == 'ARG':
                                    data_type = 'chi5'

                else:
                    data_type = data_type.lower()

                data_type += '_angle_constraints'

                if data_type in count:
                    count[data_type] += 1
                else:
                    count[data_type] = 1

                if data_type.startswith('phi_'):
                    phi = {}
                    phi['chain_id'] = chain_id_1
                    phi['seq_id'] = seq_id_common[0][0]
                    phi['comp_id'] = comp_id_common[0][0]
                    phi['value'] = target_value
                    phi['error'] = None if lower_limit is None or upper_limit is None else [lower_limit, upper_limit]
                    phi_list.append(phi)

                elif data_type.startswith('psi_'):
                    psi = {}
                    psi['chain_id'] = chain_id_1
                    psi['seq_id'] = seq_id_common[0][0]
                    psi['comp_id'] = comp_id_common[0][0]
                    psi['value'] = target_value
                    psi['error'] = None if lower_limit is None or upper_limit is None else [lower_limit, upper_limit]
                    psi_list.append(psi)

                elif data_type.startswith('chi1_'):
                    chi1 = {}
                    chi1['chain_id'] = chain_id_1
                    chi1['seq_id'] = seq_id_common[0][0]
                    chi1['comp_id'] = comp_id_common[0][0]
                    chi1['value'] = target_value
                    chi1['error'] = None if lower_limit is None or upper_limit is None else [lower_limit, upper_limit]
                    chi1_list.append(chi1)

                elif data_type.startswith('chi2_'):
                    chi2 = {}
                    chi2['chain_id'] = chain_id_1
                    chi2['seq_id'] = seq_id_common[0][0]
                    chi2['comp_id'] = comp_id_common[0][0]
                    chi2['value'] = target_value
                    chi2['error'] = None if lower_limit is None or upper_limit is None else [lower_limit, upper_limit]
                    chi2_list.append(chi2)

                # detect potential type

                targe_value = i[target_value_name]
                lower_limit_value = i[lower_limit_name]
                upper_limit_value = i[upper_limit_name]
                lower_linear_limit_value = i[lower_linear_limit_name]
                upper_linear_limit_value = i[upper_linear_limit_name]

                if (not lower_limit_value is None) and\
                   (not upper_limit_value is None) and\
                   lower_linear_limit_value is None and\
                   upper_linear_limit_value is None:
                    potential_type = 'square-well-parabolic'
                elif (not lower_limit_value is None) and\
                   (not upper_limit_value is None) and\
                   (not lower_linear_limit_value is None) and\
                   (not upper_linear_limit_value is None):
                    potential_type = 'square-well-parabolic-linear'
                elif lower_limit_value is None and\
                   (not upper_limit_value is None) and\
                   lower_linear_limit_value is None and\
                   upper_linear_limit_value is None:
                    potential_type = 'upper-bound-parabolic'
                elif (not lower_limit_value is None) and\
                   upper_limit_value is None and\
                   lower_linear_limit_value is None and\
                   upper_linear_limit_value is None:
                    potential_type = 'lower-bound-parabolic'
                elif lower_limit_value is None and\
                   (not upper_limit_value is None) and\
                   lower_linear_limit_value is None and\
                   (not upper_linear_limit_value is None):
                    potential_type = 'upper-bound-parabolic-linear'
                elif (not lower_limit_value is None) and\
                   upper_limit_value is None and\
                   (not lower_linear_limit_value is None) and\
                   upper_linear_limit_value is None:
                    potential_type = 'lower-bound-parabolic-linear'
                elif (not target_value is None) and\
                   lower_limit_value is None and\
                   upper_limit_value is None and\
                   lower_linear_limit_value is None and\
                   upper_linear_limit_value is None:
                    potential_type = 'parabolic'
                else:
                    potential_type = 'unknown'

                if potential_type in potential:
                    potential[potential_type] += 1
                else:
                    potential[potential_type] = 1

            if len(count) > 0:
                ent['number_of_constraints'] = count
                ent['number_of_potential_types'] = potential

            if 'phi_angle_constraints' in count and 'psi_angle_constraints' in count:

                phi_psi_value = {}
                phi_psi_error = {}

                for phi in phi_list:
                    try:
                        psi = next(psi for psi in psi_list if psi['chain_id'] == phi['chain_id'] and psi['seq_id'] == phi['seq_id'])

                        comp_id = phi['comp_id']

                        if not comp_id in phi_psi_value:
                            phi_psi_value[comp_id] = []

                        phi_psi_value[comp_id].append([phi['value'], psi['value'], str(phi['chain_id']) + ':' + str(phi['seq_id']) + ':' + phi['comp_id']])

                        if (not phi['error'] is None) or (not psi['error'] is None):

                            if not comp_id in phi_psi_error:
                                phi_psi_error[comp_id] = []

                            phi_psi_error[comp_id].append([phi['value'], psi['value'],
                                                           None if phi['error'] is None else phi['error'][0],
                                                           None if phi['error'] is None else phi['error'][1],
                                                           None if psi['error'] is None else psi['error'][0],
                                                           None if psi['error'] is None else psi['error'][1]])

                    except StopIteration:
                        pass

                if len(phi_psi_value) > 0:

                    phi_psi_plot = {}

                    phi_psi_plot['values'] = phi_psi_value

                    if len(phi_psi_error) > 0:
                        phi_psi_plot['errors'] = phi_psi_error

                    ent['phi_psi_plot'] = phi_psi_plot

            if 'chi1_angle_constraints' in count and 'chi2_angle_constraints' in count:

                chi1_chi2_value = {}
                chi1_chi2_error = {}

                for chi1 in chi1_list:
                    try:
                        chi2 = next(chi2 for chi2 in chi2_list if chi2['chain_id'] == chi1['chain_id'] and chi2['seq_id'] == chi1['seq_id'])

                        comp_id = chi1['comp_id']

                        if not comp_id in chi1_chi2_value:
                            chi1_chi2_value[comp_id] = []

                        chi1_chi2_value[comp_id].append([chi1['value'], chi2['value'], str(chi1['chain_id']) + ':' + str(chi1['seq_id']) + ':' + chi1['comp_id']])

                        if (not chi1['error'] is None) or (not chi2['error'] is None):

                            if not comp_id in chi1_chi2_error:
                                chi1_chi2_error[comp_id] = []

                            chi1_chi2_error[comp_id].append([chi1['value'], chi2['value'],
                                                            None if chi1['error'] is None else chi1['error'][0],
                                                            None if chi1['error'] is None else chi1['error'][1],
                                                            None if chi2['error'] is None else chi2['error'][0],
                                                            None if chi2['error'] is None else chi2['error'][1]])

                    except StopIteration:
                        pass

                if len(chi1_chi2_value) > 0:

                    chi1_chi2_plot = {}

                    chi1_chi2_plot['values'] = chi1_chi2_value

                    if len(chi1_chi2_error) > 0:
                        chi1_chi2_plot['errors'] = chi1_chi2_error

                    ent['chi1_chi2_plot'] = chi1_chi2_plot

        except Exception as e:

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__calculateStatsOfDihedralRestraint() ++ Error  - %s" % str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__calculateStatsOfDihedralRestraint() ++ Error  - %s" % str(e))

    def __calculateStatsOfRdcRestraint(self, lp_data, ent):
        """ Calculate statistics of RDC restraints.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        item_names = self.potential_items[file_type]['rdc_restraint']
        target_value_name = item_names['target_value']
        lower_limit_name = item_names['lower_limit']
        upper_limit_name = item_names['upper_limit']
        lower_linear_limit_name = item_names['lower_linear_limit']
        upper_linear_limit_name = item_names['upper_linear_limit']

        try:

            max_val = 0.0
            min_val = 0.0

            max_val_ = -100.0
            min_val_ = 100.0

            for i in lp_data:
                target_value = i[target_value_name]

                if target_value is None:

                    if not i[lower_limit_name] is None and not i[upper_limit_name] is None:
                        target_value = (i[lower_limit_name] + i[upper_limit_name]) / 2.0

                    elif not i[lower_linear_limit_name] is None and not i[upper_linear_limit_name] is None:
                        target_value = (i[lower_linear_limit_name] + i[upper_linear_limit_name]) / 2.0

                    elif not i[upper_linear_limit_name] is None:
                        target_value = i[upper_linear_limit_name]

                    elif not i[upper_limit_name] is None:
                        target_value = i[upper_limit_name]

                    elif not i[lower_linear_limit_name] is None:
                        target_value = i[lower_linear_limit_name]

                    elif not i[lower_limit_name] is None:
                        target_value = i[lower_limit_name]

                    else:
                        continue

                if target_value > max_val:
                    max_val = target_value

                elif target_value < min_val:
                    min_val = target_value

                if target_value > max_val_:
                    max_val_ = target_value

                if target_value < min_val_:
                    min_val_ = target_value

            item_names = self.item_names_in_rdc_loop[file_type]
            atom_id_1_name = item_names['atom_id_1']
            atom_id_2_name = item_names['atom_id_2']

            count = {}
            potential = {}

            for i in lp_data:
                atom_id_1 = i[atom_id_1_name]
                atom_id_2 = i[atom_id_2_name]

                try:
                    iso_number_1 = self.atom_isotopes[atom_id_1[0]][0]
                    iso_number_2 = self.atom_isotopes[atom_id_2[0]][0]
                except KeyError:
                    pass

                if iso_number_1 < iso_number_2:
                    vector_type = atom_id_1 + '-' + atom_id_2
                elif iso_number_2 > iso_number_1:
                    vector_type = atom_id_2 + '-' + atom_id_1
                else:
                    vector_type = sorted(atom_id_1, atom_id_2)

                data_type = vector_type + '_bond_vectors'

                if data_type in count:
                    count[data_type] += 1
                else:
                    count[data_type] = 1

                # detect potential type

                targe_value = i[target_value_name]
                lower_limit_value = i[lower_limit_name]
                upper_limit_value = i[upper_limit_name]
                lower_linear_limit_value = i[lower_linear_limit_name]
                upper_linear_limit_value = i[upper_linear_limit_name]

                if (not lower_limit_value is None) and\
                   (not upper_limit_value is None) and\
                   lower_linear_limit_value is None and\
                   upper_linear_limit_value is None:
                    potential_type = 'square-well-parabolic'
                elif (not lower_limit_value is None) and\
                   (not upper_limit_value is None) and\
                   (not lower_linear_limit_value is None) and\
                   (not upper_linear_limit_value is None):
                    potential_type = 'square-well-parabolic-linear'
                elif lower_limit_value is None and\
                   (not upper_limit_value is None) and\
                   lower_linear_limit_value is None and\
                   upper_linear_limit_value is None:
                    potential_type = 'upper-bound-parabolic'
                elif (not lower_limit_value is None) and\
                   upper_limit_value is None and\
                   lower_linear_limit_value is None and\
                   upper_linear_limit_value is None:
                    potential_type = 'lower-bound-parabolic'
                elif lower_limit_value is None and\
                   (not upper_limit_value is None) and\
                   lower_linear_limit_value is None and\
                   (not upper_linear_limit_value is None):
                    potential_type = 'upper-bound-parabolic-linear'
                elif (not lower_limit_value is None) and\
                   upper_limit_value is None and\
                   (not lower_linear_limit_value is None) and\
                   upper_linear_limit_value is None:
                    potential_type = 'lower-bound-parabolic-linear'
                elif (not target_value is None) and\
                   lower_limit_value is None and\
                   upper_limit_value is None and\
                   lower_linear_limit_value is None and\
                   upper_linear_limit_value is None:
                    potential_type = 'parabolic'
                else:
                    potential_type = 'unknown'

                if potential_type in potential:
                    potential[potential_type] += 1
                else:
                    potential[potential_type] = 1

            if len(count) == 0:
                return

            ent['number_of_constraints'] = count
            ent['number_of_potential_typs'] = potential
            ent['range'] = {'max_value': max_val_, 'min_value': min_val_}

            target_scale = (max_val - min_val) / 12.0

            scale = 1.0

            while scale < target_scale:
                scale *= 2.0

            while scale > target_scale:
                scale /= 2.0

            range_of_vals = []
            count_of_vals = []

            v = 0.0
            while v < min_val:
                v += scale

            while v > min_val:
                v -= scale

            while v < max_val:

                _count = copy.copy(count)

                for k in count.keys():
                    _count[k] = 0

                for i in lp_data:
                    target_value = i[target_value_name]

                    if target_value is None:

                        if not i[lower_limit_name] is None and not i[upper_limit_name] is None:
                            target_value = (i[lower_limit_name] + i[upper_limit_name]) / 2.0

                        elif not i[lower_linear_limit_name] is None and not i[upper_linear_limit_name] is None:
                            target_value = (i[lower_linear_limit_name] + i[upper_linear_limit_name]) / 2.0

                        elif not i[upper_linear_limit_name] is None:
                            target_value = i[upper_linear_limit_name]

                        elif not i[upper_limit_name] is None:
                            target_value = i[upper_limit_name]

                        elif not i[lower_linear_limit_name] is None:
                            target_value = i[lower_linear_limit_name]

                        elif not i[lower_limit_name] is None:
                            target_value = i[lower_limit_name]

                        else:
                            continue

                    if target_value < v or target_value >= v + scale:
                        continue

                    atom_id_1 = i[atom_id_1_name]
                    atom_id_2 = i[atom_id_2_name]

                    try:
                        iso_number_1 = self.atom_isotopes[atom_id_1[0]][0]
                        iso_number_2 = self.atom_isotopes[atom_id_2[0]][0]
                    except KeyError:
                        pass

                    if iso_number_1 < iso_number_2:
                        vector_type = atom_id_1 + '-' + atom_id_2
                    elif iso_number_2 > iso_number_1:
                        vector_type = atom_id_2 + '-' + atom_id_1
                    else:
                        vector_type = sorted(atom_id_1, atom_id_2)

                    data_type = vector_type + '_bond_vectors'
                    _count[data_type] += 1

                range_of_vals.append(v)
                count_of_vals.append(_count)

                v += scale

            transposed = {}

            for k in count.keys():
                transposed[k] = []

                for j in range(len(range_of_vals)):
                    transposed[k].append(count_of_vals[j][k])

            if len(range_of_vals) > 1:
                """
                has_value = False
                for j in range(1, len(range_of_vals) - 1):
                    for k in count.keys():
                        if transposed[k][j] > 0:
                            has_value = True
                            break
                    if has_value:
                        break

                if has_value:
                """
                ent['histogram'] = {'range_of_values': range_of_vals, 'number_of_values': transposed}

        except Exception as e:

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__calculateStatsOfRdcRestraint() ++ Error  - %s" % str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__calculateStatsOfRdcRestraint() ++ Error  - %s" % str(e))

    def __calculateStatsOfSpectralPeak(self, num_dim, lp_data, ent):
        """ Calculate statistics of spectral peaks.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        max_dim = num_dim + 1

        item_names = []
        for dim in range(1, max_dim):
            _d = {}
            for k, v in self.item_names_in_pk_loop[file_type].items():
                if '%s' in v:
                    v = v % dim
                _d[k] = v
            item_names.append(_d)

        chain_id_names = []
        seq_id_names = []
        comp_id_names = []
        atom_id_names = []

        try:

            count = {'assigned_spectral_peaks': 0, 'unassigned_spectral_peaks': 0}

            for j in range(num_dim):
                chain_id_names.append(item_names[j]['chain_id'])
                seq_id_names.append(item_names[j]['seq_id'])
                comp_id_names.append(item_names[j]['comp_id'])
                atom_id_names.append(item_names[j]['atom_id'])

            for i in lp_data:

                has_assignment = True

                for j in range(num_dim):
                    chain_id = i[chain_id_names[j]]
                    seq_id = i[seq_id_names[j]]
                    comp_id = i[comp_id_names[j]]
                    atom_id = i[atom_id_names[j]]

                    if chain_id in self.empty_value or seq_id in self.empty_value or comp_id in self.empty_value or atom_id in self.empty_value:
                        has_assignment = False
                        break

                if has_assignment:
                    count['assigned_spectral_peaks'] += 1
                else:
                    count['unassigned_spectral_peaks'] += 1

            ent['number_of_spectral_peaks'] = count

        except Exception as e:

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__calculateStatsOfSpectralPeak() ++ Error  - %s" % str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__calculateStatsOfSpectralPeak() ++ Error  - %s" % str(e))

    def __validateCoordInputSource(self):
        """ Validate coordinate file as secondary input resource.
        """

        file_type = 'pdbx'
        content_type = self.content_type[file_type]

        if self.__parseCoordinate():

            file_name = os.path.basename(self.__cifPath)

            self.report.appendInputSource()

            input_source = self.report.input_sources[-1]

            input_source.setItemValue('file_name', file_name)
            input_source.setItemValue('file_type', file_type)
            input_source.setItemValue('content_type', content_type)

            return True

        return False

    def __parseCoordinate(self):
        """ Parse coordinate file.
        """

        file_type = 'pdbx'

        if self.__cifPath is None:
            self.__setCoordFilePath()

        if self.__cifPath is None:

            if 'coordinate_file_path' in self.__inputParamDict:

                err = "No such %s file." % self.__inputParamDict['coordinate_file_path']

                self.report.error.appendDescription('internal_error', "+NmrDpUtility.__parseCoordinate() ++ Error  - %s" % err)
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__parseCoordinate() ++ Error  - %s\n" % err)

                return False

            else:

                err = "%s formatted coordinate file is mandatory." % self.readable_file_type[file_type]

                self.report.error.appendDescription('internal_error', "+NmrDpUtility.__parseCoordinate() ++ Error  - %s" % err)
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__parseCoordinate() ++ Error  - %s\n" % err)

                return False

        file_name = os.path.basename(self.__cifPath)

        try:

            if not self.__cR.parse():

                err = "%s is invalid %s file." % (file_name, self.readable_file_type[file_type])

                self.report.error.appendDescription('internal_error', "+NmrDpUtility.__parseCoordinate() ++ Error  - %s" % err)
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__parseCoordinate() ++ Error  - %s\n" % err)

                return False

            return True

        except:
            return False

    def __setCoordFilePath(self):
        """ Set effective coordinate file path.
        """

        if 'coordinate_file_path' in self.__inputParamDict:

            fPath = self.__inputParamDict['coordinate_file_path']

            try:

                if self.__cR.setFilePath(fPath):
                    self.__cifPath = fPath

                # try deposit storage if possible
                elif 'proc_coord_file_path' in self.__inputParamDict:

                    fPath = self.__inputParamDict['proc_coord_file_path']

                    if self.__cR.setFilePath(fPath):
                        self.__cifPath = fPath

            except:
                pass

    def __detectCoordContentSubType(self):
        """ Detect content subtypes of coordinate file.
        """

        id = self.report.getInputSourceIdOfCoord()

        if id < 0:
            return True

        input_source = self.report.input_sources[id]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        # initialize loop counter
        lp_counts = {t:0 for t in self.cif_content_subtypes}

        for content_subtype in self.cif_content_subtypes:

            lp_category = self.lp_categories[file_type][content_subtype]

            if self.__cR.hasCategory(lp_category):
                lp_counts[content_subtype] = 1

            elif content_subtype != 'non_poly':

                err = "Category %s is mandatory." % self.lp_categories[file_type][content_subtype]

                self.report.error.appendDescription('missing_mandatory_content', {'file_name': file_name, 'description': err})
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__detectCoordContentSubType() ++ Error  - %s\n" % err)

        content_subtypes = {k:lp_counts[k] for k in lp_counts if lp_counts[k] > 0}

        input_source.setItemValue('content_subtype', content_subtypes)

        return True

    def __extractCoordPolymerSequence(self):
        """ Extract reference polymer sequence of coordinate file.
        """

        id = self.report.getInputSourceIdOfCoord()

        if id < 0:
            return True

        input_source = self.report.input_sources[id]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        content_subtype = 'poly_seq'

        if not content_subtype in input_source_dic['content_subtype']:
            return True

        lp_category = self.lp_categories[file_type][content_subtype]

        try:

            poly_seq = self.__cR.getPolymerSequence(lp_category, self.key_items[file_type][content_subtype])

            input_source.setItemValue('polymer_sequence', poly_seq)

            return True

        except KeyError as e:

            self.report.error.appendDescription('sequence_mismatch', {'file_name': file_name, 'category': lp_category, 'description': str(e).strip("'")})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__extractCoordPolymerSequence() ++ KeyError  - %s" % str(e))

        except LookupError as e:

            self.report.error.appendDescription('missing_mandatory_item', {'file_name': file_name, 'category': lp_category, 'description': str(e).strip("'")})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__extractCoordPolymerSequence() ++ LookupError  - %s" % str(e))

        except ValueError as e:

            self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'category': lp_category, 'description': str(e).strip("'")})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__extractCoordPolymerSequence() ++ ValueError  - %s" % str(e))

        except Exception as e:

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__extractCoordPolymerSequence() ++ Error  - %s" % str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__extractCoordPolymerSequence() ++ Error  - %s" % str(e))

        return False

    def __extractCoordNonPolymerScheme(self):
        """ Extract non-polymer scheme of coordinate file.
        """

        id = self.report.getInputSourceIdOfCoord()

        if id < 0:
            return True

        input_source = self.report.input_sources[id]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        content_subtype = 'non_poly'

        if not content_subtype in input_source_dic['content_subtype']:
            return True

        lp_category = self.lp_categories[file_type][content_subtype]

        try:

            non_poly = self.__cR.getPolymerSequence(lp_category, self.key_items[file_type][content_subtype])

            if len(non_poly) > 0:

                poly_seq = input_source_dic['polymer_sequence']

                if poly_seq is None:

                    err = "Polymer sequence did not exist, __extractCoordPolymerSequence() should be invoked."

                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__extractCoordNonPolymerScheme() ++ Error  - %s" % err)
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__extractCoordNonPolymerScheme() ++ Error  - %s" % err)

                    return False

                for np in non_poly:
                    poly_seq.append(np)

                input_source.setItemValue('polymer_sequence', poly_seq)

            return True

        except KeyError as e:

            self.report.error.appendDescription('sequence_mismatch', {'file_name': file_name, 'category': lp_category, 'description': str(e).strip("'")})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__extractCoordNonPolymerScheme() ++ KeyError  - %s" % str(e))

        except LookupError as e:

            self.report.error.appendDescription('missing_mandatory_item', {'file_name': file_name, 'category': lp_category, 'description': str(e).strip("'")})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__extractCoordNonPolymerScheme() ++ LookupError  - %s" % str(e))

        except ValueError as e:

            self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'category': lp_category, 'description': str(e).strip("'")})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__extractCoordNonPolymerScheme() ++ ValueError  - %s" % str(e))

        except Exception as e:

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__extractCoordNonPolymerScheme() ++ Error  - %s" % str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__extractCoordNonPolymerScheme() ++ Error  - %s" % str(e))

        return False

    def __extractCoordPolymerSequenceInLoop(self):
        """ Extract polymer sequence in interesting loops of coordinate file.
        """

        id = self.report.getInputSourceIdOfCoord()

        if id < 0:
            return True

        __errors = self.report.getTotalErrors()

        input_source = self.report.input_sources[id]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        poly_seq_list_set = {}
        poly_sid_list_set = {}

        for content_subtype in self.cif_content_subtypes:

            if content_subtype == 'entry_info' or content_subtype == 'poly_seq' or not content_subtype in input_source_dic['content_subtype']:
                continue

            poly_seq_list_set[content_subtype] = []

            lp_category = self.lp_categories[file_type][content_subtype]

            list_id = 1

            has_poly_seq = False

            try:

                poly_seq = self.__cR.getPolymerSequence(lp_category, self.key_items[file_type][content_subtype])

                if len(poly_seq) > 0:

                    poly_seq_list_set[content_subtype].append({'list_id': list_id, 'polymer_sequence': poly_seq})

                    has_poly_seq = True

            except KeyError as e:

                self.report.error.appendDescription('sequence_mismatch', {'file_name': file_name, 'category': lp_category, 'description': str(e).strip("'")})
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__extractCoordPolymerSequenceInLoop() ++ KeyError  - %s" % str(e))

            except LookupError as e:

                self.report.error.appendDescription('missing_mandatory_item', {'file_name': file_name, 'category': lp_category, 'description': str(e).strip("'")})
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__extractCoordPolymerSequenceInLoop() ++ LookupError  - %s" % str(e))

            except ValueError as e:

                self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'category': lp_category, 'description': str(e).strip("'")})
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__extractCoordPolymerSequenceInLoop() ++ ValueError  - %s" % str(e))

            except Exception as e:

                self.report.error.appendDescription('internal_error', "+NmrDpUtility.__extractCoordPolymerSequenceInLoop() ++ Error  - %s" % str(e))
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__extractCoordPolymerSequenceInLoop() ++ Error  - %s" % str(e))

            list_id += 1

            if not has_poly_seq:
                poly_seq_list_set.pop(content_subtype)

        if self.report.getTotalErrors() > __errors:
            return False

        if len(poly_seq_list_set) > 0:
            input_source.setItemValue('polymer_sequence_in_loop', poly_seq_list_set)

        return True

    def __extractCoordNonStandardResidue(self):
        """ Extract non-standard residue of coordinate file.
        """

        id = self.report.getInputSourceIdOfCoord()

        if id < 0:
            return True

        input_source = self.report.input_sources[id]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        has_poly_seq = self.__hasKeyValue(input_source_dic, 'polymer_sequence')

        if not has_poly_seq:
            return True

        polymer_sequence = input_source_dic['polymer_sequence']

        asm = []

        for s in polymer_sequence:

            has_non_std_comp_id = False

            ent = {'chain_id': s['chain_id'], 'seq_id': [], 'comp_id': [], 'chem_comp_name': [], 'exptl_data': []}

            for i in range(len(s['seq_id'])):
                seq_id = s['seq_id'][i]
                comp_id = s['comp_id'][i]

                if self.__get1LetterCode(comp_id) == 'X':
                    has_non_std_comp_id = True

                    ent['seq_id'].append(seq_id)
                    ent['comp_id'].append(comp_id)

                    self.__updateChemCompDict(comp_id)

                    if self.__last_comp_id_test: # matches with comp_id in CCD
                        cc_name = self.__last_chem_comp_dict['_chem_comp.name']
                        cc_rel_status = self.__last_chem_comp_dict['_chem_comp.pdbx_release_status']
                        if cc_rel_status == 'REL':
                            ent['chem_comp_name'].append(cc_name)
                        else:
                            ent['chem_comp_name'].append('(Not available due to CCD status code %s)' % cc_rel_status)

                    else:
                        ent['chem_comp_name'].append(None)

                    ent['exptl_data'].append({'coordinate': False})

            if has_non_std_comp_id:
                asm.append(ent)

        if len(asm) > 0:
            input_source.setItemValue('non_standard_residue', asm)

        return True

    def __appendCoordPolymerSequenceAlignment(self):
        """ Append polymer sequence alignment between coordinate and NMR data.
        """

        id = self.report.getInputSourceIdOfCoord()

        if id < 0:
            return True

        # sequence alignment inside coordinate file

        input_source = self.report.input_sources[id]
        input_source_dic = input_source.get()

        has_poly_seq = self.__hasKeyValue(input_source_dic, 'polymer_sequence')
        has_poly_seq_in_loop = self.__hasKeyValue(input_source_dic, 'polymer_sequence_in_loop')

        if not has_poly_seq:
            return False

        polymer_sequence = input_source_dic['polymer_sequence']

        if has_poly_seq_in_loop:

            polymer_sequence_in_loop = input_source_dic['polymer_sequence_in_loop']

            for content_subtype in polymer_sequence_in_loop.keys():
                list_len = len(polymer_sequence_in_loop[content_subtype])

                seq_align_set = []

                for s1 in polymer_sequence:
                    chain_id = s1['chain_id']

                    if type(chain_id) == int:
                        _chain_id = str(chain_id)
                    else:
                        _chain_id = chain_id

                    for list_id in range(list_len):
                        ps2 = polymer_sequence_in_loop[content_subtype][list_id]['polymer_sequence']

                        for s2 in ps2:

                            if chain_id != s2['chain_id']:
                                continue

                            #_s2 = self.__fillBlankedCompId(s1, s2)

                            self.__pA.setReferenceSequence(s1['comp_id'], 'REF' + _chain_id)
                            self.__pA.addTestSequence(s2['comp_id'], _chain_id)
                            self.__pA.doAlign()
                            #self.__pA.prAlignmentConflicts(_chain_id)
                            myAlign = self.__pA.getAlignment(_chain_id)

                            length = len(myAlign)

                            if length == 0:
                                continue

                            unmapped = 0
                            conflict = 0
                            for i in range(length):
                                myPr = myAlign[i]
                                if myPr[0].encode() == '.' or myPr[1].encode() == '.':
                                    unmapped += 1
                                elif myPr[0] != myPr[1]:
                                    conflict += 1

                            if length == unmapped + conflict:
                                continue

                            ref_length = len(s1['seq_id'])

                            ref_code = self.__get1LetterCodeSequence(s1['comp_id'])
                            test_code = self.__get1LetterCodeSequence(s2['comp_id'])
                            mid_code = self.__getMiddleCode(ref_code, test_code)
                            ref_gauge_code = self.__getGaugeCode(s1['seq_id'])
                            test_gauge_code = self.__getGaugeCode(s2['seq_id'])

                            seq_align = {'list_id': polymer_sequence_in_loop[content_subtype][list_id]['list_id'],
                                         'chain_id': chain_id, 'length': ref_length, 'conflict': conflict, 'unmapped': unmapped, 'sequence_coverage': float('{:.3f}'.format(float(length - (unmapped + conflict)) / float(ref_length))),
                                         'ref_seq_id': s1['seq_id'],
                                         'ref_gauge_code': ref_gauge_code, 'ref_code': ref_code, 'mid_code': mid_code, 'test_code': test_code, 'test_gauge_code': test_gauge_code}

                            seq_align_set.append(seq_align)

                if len(seq_align_set) > 0:
                    self.report.sequence_alignment.setItemValue('model_poly_seq_vs_' + content_subtype, seq_align_set)

        # sequence alignment between model and NMR data

        nmr_input_source = self.report.input_sources[0]
        nmr_input_source_dic = nmr_input_source.get()

        has_nmr_poly_seq = self.__hasKeyValue(nmr_input_source_dic, 'polymer_sequence')

        if not has_nmr_poly_seq:

            err = "Common polymer sequence did not exist, __extractCommonPolymerSequence() should be invoked."

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__appendCoordPolymerSequenceAlignment() ++ Error  - %s" % err)
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__appendCoordPolymerSequenceAlignment() ++ Error  - %s\n" % err)

            return False

        nmr_polymer_sequence = nmr_input_source_dic['polymer_sequence']

        seq_align_set = []

        for s1 in polymer_sequence:
            chain_id = s1['chain_id']

            if type(chain_id) == int:
                _chain_id = str(chain_id)
            else:
                _chain_id = chain_id

            for s2 in nmr_polymer_sequence:
                chain_id2 = s2['chain_id']

                #_s2 = self.__fillBlankedCompId(s1, s2)

                self.__pA.setReferenceSequence(s1['comp_id'], 'REF' + _chain_id)
                self.__pA.addTestSequence(s2['comp_id'], _chain_id)
                self.__pA.doAlign()
                #self.__pA.prAlignmentConflicts(_chain_id)
                myAlign = self.__pA.getAlignment(_chain_id)

                length = len(myAlign)

                if length == 0:
                    continue

                unmapped = 0
                conflict = 0
                for i in range(length):
                    myPr = myAlign[i]
                    if myPr[0].encode() == '.' or myPr[1].encode() == '.':
                        unmapped += 1
                    elif myPr[0] != myPr[1]:
                        conflict += 1

                if length == unmapped + conflict:
                    continue

                ref_length = len(s1['seq_id'])

                ref_code = self.__get1LetterCodeSequence(s1['comp_id'])
                test_code = self.__get1LetterCodeSequence(s2['comp_id'])
                mid_code = self.__getMiddleCode(ref_code, test_code)
                ref_gauge_code = self.__getGaugeCode(s1['seq_id'])
                test_gauge_code = self.__getGaugeCode(s2['seq_id'])

                seq_align = {'ref_chain_id': chain_id, 'test_chain_id': chain_id2, 'length': ref_length, 'conflict': conflict, 'unmapped': unmapped, 'sequence_coverage': float('{:.3f}'.format(float(length - (unmapped + conflict)) / float(ref_length))),
                             'ref_seq_id': s1['seq_id'], 'test_seq_id': s2['seq_id'],
                             'ref_gauge_code': ref_gauge_code, 'ref_code': ref_code, 'mid_code': mid_code, 'test_code': test_code, 'test_gauge_code': test_gauge_code}

                seq_align_set.append(seq_align)

        if len(seq_align_set) > 0:
            self.report.sequence_alignment.setItemValue('model_poly_seq_vs_nmr_poly_seq', seq_align_set)

        seq_align_set = []

        for s1 in nmr_polymer_sequence:
            chain_id = s1['chain_id']

            if type(chain_id) == int:
                _chain_id = str(chain_id)
            else:
                _chain_id = chain_id

            for s2 in polymer_sequence:
                chain_id2 = s2['chain_id']

                #_s2 = self.__fillBlankedCompId(s1, s2)

                self.__pA.setReferenceSequence(s1['comp_id'], 'REF' + _chain_id)
                self.__pA.addTestSequence(s2['comp_id'], _chain_id)
                self.__pA.doAlign()
                #self.__pA.prAlignmentConflicts(_chain_id)
                myAlign = self.__pA.getAlignment(_chain_id)

                length = len(myAlign)

                if length == 0:
                    continue

                unmapped = 0
                conflict = 0
                for i in range(length):
                    myPr = myAlign[i]
                    if myPr[0].encode() == '.' or myPr[1].encode() == '.':
                        unmapped += 1
                    elif myPr[0] != myPr[1]:
                        conflict += 1

                if length == unmapped + conflict:
                    continue

                ref_length = len(s1['seq_id'])

                ref_code = self.__get1LetterCodeSequence(s1['comp_id'])
                test_code = self.__get1LetterCodeSequence(s2['comp_id'])
                mid_code = self.__getMiddleCode(ref_code, test_code)
                ref_gauge_code = self.__getGaugeCode(s1['seq_id'])
                test_gauge_code = self.__getGaugeCode(s2['seq_id'])

                seq_align = {'ref_chain_id': chain_id, 'test_chain_id': chain_id2, 'length': ref_length, 'conflict': conflict, 'unmapped': unmapped, 'sequence_coverage': float('{:.3f}'.format(float(length - (unmapped + conflict)) / float(ref_length))),
                             'ref_seq_id': s1['seq_id'], 'test_seq_id': s2['seq_id'],
                             'ref_gauge_code': ref_gauge_code, 'ref_code': ref_code, 'mid_code': mid_code, 'test_code': test_code, 'test_gauge_code': test_gauge_code}

                seq_align_set.append(seq_align)

        if len(seq_align_set) > 0:
            self.report.sequence_alignment.setItemValue('nmr_poly_seq_vs_model_poly_seq', seq_align_set)

        return True

    def __assignCoordPolymerSequence(self):
        """ Assign polymer sequences of coordinate file.
        """

        id = self.report.getInputSourceIdOfCoord()

        if id < 0:
            return True

        cif_input_source = self.report.input_sources[id]
        cif_input_source_dic = cif_input_source.get()

        cif_file_name = cif_input_source_dic['file_name']

        has_cif_poly_seq = self.__hasKeyValue(cif_input_source_dic, 'polymer_sequence')

        if not has_cif_poly_seq:
            return False

        nmr_input_source = self.report.input_sources[0]
        nmr_input_source_dic = nmr_input_source.get()

        nmr_file_name = nmr_input_source_dic['file_name']

        has_nmr_poly_seq = self.__hasKeyValue(nmr_input_source_dic, 'polymer_sequence')

        if not has_nmr_poly_seq:

            err = "Common polymer sequence did not exist, __extractCommonPolymerSequence() should be invoked."

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__assignCoordPolymerSequence() ++ Error  - %s" % err)
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__assignCoordPolymerSequence() ++ Error  - %s\n" % err)

            return False

        __errors = self.report.getTotalErrors()

        seq_align_dic = self.report.sequence_alignment.get()

        if 'model_poly_seq_vs_nmr_poly_seq' in seq_align_dic and 'nmr_poly_seq_vs_model_poly_seq' in seq_align_dic:

            cif_polymer_sequence = cif_input_source_dic['polymer_sequence']
            nmr_polymer_sequence = nmr_input_source_dic['polymer_sequence']

            if nmr_polymer_sequence is None:
                return False

            cif_chains = len(cif_polymer_sequence)
            nmr_chains = len(nmr_polymer_sequence)

            # map polymer sequences between coordinate and NMR data using Hungarian algorithm
            m = Munkres()

            # from model to nmr

            mat = []

            for s1 in cif_polymer_sequence:
                chain_id = s1['chain_id']

                cost = [0 for i in range(nmr_chains)]

                for s2 in nmr_polymer_sequence:
                    chain_id2 = s2['chain_id']

                    result = next((seq_align for seq_align in seq_align_dic['model_poly_seq_vs_nmr_poly_seq'] if seq_align['ref_chain_id'] == chain_id and seq_align['test_chain_id'] == chain_id2), None)

                    if not result is None:
                        cost[nmr_polymer_sequence.index(s2)] = result['unmapped'] + result['conflict'] - result['length']

                mat.append(cost)

            indices = m.compute(mat)

            chain_assign_set = []

            for row, column in indices:

                if mat[row][column] >= 0:
                    continue

                chain_id = cif_polymer_sequence[row]['chain_id']
                chain_id2 = nmr_polymer_sequence[column]['chain_id']

                if type(chain_id) == int:
                    _chain_id = str(chain_id)
                else:
                    _chain_id = chain_id

                result = next(seq_align for seq_align in seq_align_dic['model_poly_seq_vs_nmr_poly_seq'] if seq_align['ref_chain_id'] == chain_id and seq_align['test_chain_id'] == chain_id2)

                chain_assign = {'ref_chain_id': chain_id, 'test_chain_id': chain_id2, 'length': result['length'], 'conflict': result['conflict'], 'unmapped': result['unmapped'], 'sequence_coverage': result['sequence_coverage']}

                s1 = next(s for s in cif_polymer_sequence if s['chain_id'] == chain_id)
                s2 = next(s for s in nmr_polymer_sequence if s['chain_id'] == chain_id2)

                #_s2 = self.__fillBlankedCompId(s1, s2)

                self.__pA.setReferenceSequence(s1['comp_id'], 'REF' + _chain_id)
                self.__pA.addTestSequence(s2['comp_id'], _chain_id)
                self.__pA.doAlign()
                #self.__pA.prAlignmentConflicts(_chain_id)
                myAlign = self.__pA.getAlignment(_chain_id)

                length = len(myAlign)

                ref_code = self.__get1LetterCodeSequence(s1['comp_id'])
                test_code = self.__get1LetterCodeSequence(s2['comp_id'])

                for j in range(len(ref_code)):
                    if ref_code[j] == 'X' and test_code[j] == 'X':
                        nmr_input_source.updateNonStandardResidueByExptlData(chain_id2, s2['seq_id'][j], 'coordinate')
                        cif_input_source.updateNonStandardResidueByExptlData(chain_id, s1['seq_id'][j], 'coordinate')

                if result['unmapped'] > 0 or result['conflict'] > 0:

                    unmapped = []
                    conflict = []

                    for i in range(length):
                        myPr = myAlign[i]
                        if myPr[0] == myPr[1]:
                            continue

                        cif_comp_id = myPr[0].encode()
                        nmr_comp_id = myPr[1].encode()

                        if i >= len(s1['seq_id']):
                            continue

                        if nmr_comp_id == '.' or i >= len(s2['seq_id']):
                            unmapped.append({'ref_seq_id': s1['seq_id'][i], 'ref_comp_id': cif_comp_id})

                            warn = "%s's sequence (chain_id %s, seq_id %s, comp_id %s) could not mapped to anything in %s." %\
                                   (cif_file_name, chain_id, s1['seq_id'][i], cif_comp_id, nmr_file_name)

                            self.report.warning.appendDescription('sequence_mismatch', {'file_name': cif_file_name, 'description': warn})
                            self.report.setWarning()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__assignCoordPolymerSequence() ++ Warning  - %s" % warn)

                        else:
                            conflict.append({'ref_seq_id': s1['seq_id'][i], 'ref_comp_id': cif_comp_id,
                                             'test_seq_id': s2['seq_id'][i], 'test_comp_id': nmr_comp_id})

                            err = "Sequence alignment error between %s (chain_id %s, seq_id %s, comp_id %s) and %s (chain_id %s, seq_id %s, comp_id %s)." %\
                                  (cif_file_name, chain_id, s1['seq_id'][i], cif_comp_id, nmr_file_name, chain_id2, s2['seq_id'][i], nmr_comp_id)

                            self.report.error.appendDescription('sequence_mismatch', {'file_name': cif_file_name, 'description': err})
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__assignCoordPolymerSequence() ++ Error  - %s" % err)

                    if len(unmapped) > 0:
                        chain_assign['unmapped_sequence'] = unmapped

                    if len(conflict) > 0:
                        chain_assign['conflict_sequence'] = conflict

                chain_assign_set.append(chain_assign)

            if len(chain_assign_set) > 0:
                self.report.chain_assignment.setItemValue('model_poly_seq_vs_nmr_poly_seq', chain_assign_set)

            # from nmr to model

            mat = []

            for s1 in nmr_polymer_sequence:
                chain_id = s1['chain_id']

                cost = [0 for i in range(cif_chains)]

                for s2 in cif_polymer_sequence:
                    chain_id2 = s2['chain_id']

                    result = next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq'] if seq_align['ref_chain_id'] == chain_id and seq_align['test_chain_id'] == chain_id2), None)

                    if not result is None:
                        cost[cif_polymer_sequence.index(s2)] = result['unmapped'] + result['conflict'] - result['length']

                mat.append(cost)

            indices = m.compute(mat)

            chain_assign_set = []

            for row, column in indices:

                if mat[row][column] >= 0:
                    continue

                chain_id = nmr_polymer_sequence[row]['chain_id']
                chain_id2 = cif_polymer_sequence[column]['chain_id']

                if type(chain_id) == int:
                    _chain_id = str(chain_id)
                else:
                    _chain_id = chain_id

                result = next(seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq'] if seq_align['ref_chain_id'] == chain_id and seq_align['test_chain_id'] == chain_id2)

                chain_assign = {'ref_chain_id': chain_id, 'test_chain_id': chain_id2, 'length': result['length'], 'conflict': result['conflict'], 'unmapped': result['unmapped'], 'sequence_coverage': result['sequence_coverage']}

                if result['unmapped'] > 0 or result['conflict'] > 0:

                    unmapped = []
                    conflict = []

                    s1 = next(s for s in nmr_polymer_sequence if s['chain_id'] == chain_id)
                    s2 = next(s for s in cif_polymer_sequence if s['chain_id'] == chain_id2)

                    #_s2 = self.__fillBlankedCompId(s1, s2)

                    self.__pA.setReferenceSequence(s1['comp_id'], 'REF' + _chain_id)
                    self.__pA.addTestSequence(s2['comp_id'], _chain_id)
                    self.__pA.doAlign()
                    #self.__pA.prAlignmentConflicts(_chain_id)
                    myAlign = self.__pA.getAlignment(_chain_id)

                    for i in range(len(myAlign)):
                        myPr = myAlign[i]
                        if myPr[0] == myPr[1]:
                            continue

                        nmr_comp_id = myPr[0].encode()
                        cif_comp_id = myPr[1].encode()

                        if i >= len(s1['seq_id']):
                            continue

                        if cif_comp_id == '.' or i >= len(s2['seq_id']):
                            unmapped.append({'ref_seq_id': s1['seq_id'][i], 'ref_comp_id': nmr_comp_id})

                            warn = "%s's sequence (chain_id %s, seq_id %s, comp_id %s) could not mapped to anything in %s." %\
                                   (nmr_file_name, chain_id, s1['seq_id'][i], nmr_comp_id, cif_file_name)

                            self.report.warning.appendDescription('sequence_mismatch', {'file_name': nmr_file_name, 'description': warn})
                            self.report.setWarning()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__assignCoordPolymerSequence() ++ Warning  - %s" % warn)

                        else:
                            conflict.append({'ref_seq_id': s1['seq_id'][i], 'ref_comp_id': nmr_comp_id,
                                             'test_seq_id': s2['seq_id'][i], 'test_comp_id': cif_comp_id})

                            err = "Sequence alignment error between %s (chain_id %s, seq_id %s, comp_id %s) and %s (chain_id %s, seq_id %s, comp_id %s)." %\
                                  (nmr_file_name, chain_id, s1['seq_id'][i], nmr_comp_id, cif_file_name, chain_id2, s2['seq_id'][i], cif_comp_id)

                            self.report.error.appendDescription('sequence_mismatch', {'file_name': nmr_file_name, 'description': err})
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__assignCoordPolymerSequence() ++ Error  - %s" % err)

                    if len(unmapped) > 0:
                        chain_assign['unmapped_sequence'] = unmapped

                    if len(conflict) > 0:
                        chain_assign['conflict_sequence'] = conflict

                chain_assign_set.append(chain_assign)

            if len(chain_assign_set) > 0:
                self.report.chain_assignment.setItemValue('nmr_poly_seq_vs_model_poly_seq', chain_assign_set)

            return self.report.getTotalErrors() == __errors

        else:

            err = "No sequence alignment found."

            self.report.error.appendDescription('sequence_mismatch', {'file_name': cif_file_name, 'description': err})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__assignCoordPolymerSequence() ++ Error  - %s" % err)

            return False

    def __testCoordAtomIdConsistency(self):
        """ Perform consistency test on atom names of coordinate file.
        """

        id = self.report.getInputSourceIdOfCoord()

        if id < 0:
            return True

        cif_input_source = self.report.input_sources[id]
        cif_input_source_dic = cif_input_source.get()

        cif_polymer_sequence = cif_input_source_dic['polymer_sequence']

        nmr_input_source = self.report.input_sources[0]
        nmr_input_source_dic = nmr_input_source.get()

        file_type = nmr_input_source_dic['file_type']
        file_name = nmr_input_source_dic['file_name']

        seq_align_dic = self.report.sequence_alignment.get()
        chain_assign_dic = self.report.chain_assignment.get()

        if not 'nmr_poly_seq_vs_model_poly_seq' in chain_assign_dic:

            err = "Chain assignment did not exist, __assignCoordPolymerSequence() should be invoked."

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testCoordAtomIdConsistency() ++ Error  - %s" % err)
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__testCoordAtomIdConsistency() ++ Error  - %s\n" % err)

            return False

        if chain_assign_dic['nmr_poly_seq_vs_model_poly_seq'] is None:
            return False

        __errors = self.report.getTotalErrors()

        nmr2ca = {}

        for chain_assign in chain_assign_dic['nmr_poly_seq_vs_model_poly_seq']:

            ref_chain_id = chain_assign['ref_chain_id']
            test_chain_id = chain_assign['test_chain_id']

            result = next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq'] if seq_align['ref_chain_id'] == ref_chain_id and seq_align['test_chain_id'] == test_chain_id), None)

            nmr2ca[str(ref_chain_id)] = result

        try:

            coord = self.__cR.getDictListWithFilter('atom_site',
                                                    [{'name': 'label_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                                      {'name': 'label_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                                      {'name': 'label_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                      {'name': 'label_atom_id', 'type': 'str', 'alt_name': 'atom_id'}
                                                     ],
                                                    [{'name': 'pdbx_PDB_model_num', 'type': 'int', 'value': 1}
                                                     ])

        except Exception as e:

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testCoordAtomIdConsistency() ++ Error  - %s" % str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__testCoordAtomIdConsistency() ++ Error  - %s" % str(e))

            return False

        if nmr_input_source_dic['content_subtype'] is None:
            return False

        for content_subtype in nmr_input_source_dic['content_subtype'].keys():

            if content_subtype == 'entry_info' or content_subtype == 'poly_seq':
                continue

            sf_category = self.sf_categories[file_type][content_subtype]
            lp_category = self.lp_categories[file_type][content_subtype]

            index_tag = self.index_tags[file_type][content_subtype]

            list_id = 1

            for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

                sf_framecode = sf_data.get_tag('sf_framecode')[0]

                lp_data = next((l['data'] for l in self.__lp_data[content_subtype] if l['sf_framecode'] == sf_framecode), None)

                if not lp_data is None:

                    has_seq_align = False

                    sa_name = 'nmr_poly_seq_vs_' + content_subtype

                    if sa_name in seq_align_dic and not seq_align_dic[sa_name] is None:

                        for seq_align in seq_align_dic[sa_name]:

                            if seq_align['list_id'] == list_id:
                                has_seq_align = True
                                break

                    if not has_seq_align:
                        continue

                    item_names = []

                    if content_subtype == 'chem_shift':
                        max_dim = 2

                        item_names.append(self.item_names_in_cs_loop[file_type])

                    else:

                        if content_subtype == 'dist_restraint' or content_subtype == 'rdc_restraint':
                            max_dim = 3

                        elif content_subtype == 'dihed_restring':
                            max_dim = 5

                        elif content_subtype == 'spectral_peak':

                            try:

                                _num_dim = sf_data.get_tag(self.num_dim_items[file_type])[0]
                                num_dim = int(_num_dim)

                                if not num_dim in range(1, self.lim_num_dim):
                                    raise ValueError()

                            except ValueError: # raised error already at __testIndexConsistency()
                                continue

                            max_dim = num_dim + 1

                        else:
                            continue

                        for j in range(1, max_dim):
                            _item_names = {}
                            for k, v in self.item_names_in_pk_loop[file_type].items():
                                if '%s' in v:
                                    v = v % j
                                _item_names[k] = v
                            item_names.append(_item_names)

                    num_dim = max_dim - 1

                    chain_id_names = []
                    seq_id_names = []
                    comp_id_names = []
                    atom_id_names = []

                    for j in range(num_dim):
                        chain_id_names.append(item_names[j]['chain_id'])
                        seq_id_names.append(item_names[j]['seq_id'])
                        comp_id_names.append(item_names[j]['comp_id'])
                        atom_id_names.append(item_names[j]['atom_id'])

                    for i in lp_data:

                        for j in range(num_dim):
                            chain_id = i[chain_id_names[j]]
                            seq_id = i[seq_id_names[j]]
                            comp_id = i[comp_id_names[j]]
                            atom_id = i[atom_id_names[j]]

                            if content_subtype == 'spectral_peak' and (chain_id in self.empty_value or seq_id in self.empty_value or comp_id in self.empty_value or atom_id in self.empty_value):
                                continue

                            if not str(chain_id) in nmr2ca:
                                continue

                            ca = nmr2ca[str(chain_id)]

                            cif_chain_id = ca['test_chain_id']

                            cif_seq_id = None
                            for k in range(ca['length']):
                                if ca['ref_seq_id'][k] == seq_id:
                                    cif_seq_id = ca['test_seq_id'][k]
                                    break

                            if cif_seq_id is None:
                                continue

                            cif_ps = next(ps for ps in cif_polymer_sequence if ps['chain_id'] == cif_chain_id)

                            cif_comp_id = None
                            for k in range(len(cif_ps['seq_id'])):
                                if cif_ps['seq_id'][k] == cif_seq_id:
                                    cif_comp_id = cif_ps['comp_id'][k]
                                    break

                            if cif_comp_id is None:
                                continue

                            if file_type == 'nef':
                                _atom_id, ambig_code, details = self.__nefT.get_nmrstar_atom(comp_id, atom_id, leave_unmatched=True)

                                if len(_atom_id) == 0:
                                    continue

                                if len(_atom_id) == 1 and atom_id == _atom_id[0]:
                                    atom_id_ = atom_id
                                    atom_name = atom_id

                                    if not details is None:
                                        atom_name += ', besides that, ' + details.rstrip('.')

                                else:
                                    atom_name = atom_id + ' (e.g. '

                                    for atom_id_ in _atom_id:
                                        atom_name += atom_id_ + ' '

                                    atom_name = atom_name.rstrip() + ')'

                                    # representative atom id
                                    atom_id_ = _atom_id[0]

                            else:
                                atom_id_ = atom_id
                                atom_name = atom_id

                            result = next((c for c in coord if c['chain_id'] == cif_chain_id and c['seq_id'] == cif_seq_id and c['comp_id'] == cif_comp_id and c['atom_id'] == atom_id_), None)

                            if result is None:

                                idx_msg = ''
                                if not index_tag is None:
                                    idx_msg = "[Check row of %s %s] " % (index_tag, i[index_tag])

                                err = "%sAtom (%s %s, %s %s, %s %s, %s %s) is not incorporated in the atomic coordinate." %\
                                      (idx_msg, chain_id_names[j], chain_id, seq_id_names[j], seq_id, comp_id_names[j], comp_id, atom_id_names[j], atom_name)

                                self.report.error.appendDescription('invalid_atom_nomenclature', {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category, 'description': err})
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write("+NmrDpUtility.__testCoordAtomIdConsistency() ++ Error  - %s\n" % err)

                list_id += 1

        return self.report.getTotalErrors() == __errors

    def __retrieveDpReport(self):
        """ Retrieve NMR data processing report from JSON file.
        """

        if 'report_file_path' in self.__inputParamDict:

            fPath = self.__inputParamDict['report_file_path']

            if os.access(fPath, os.F_OK):

                if os.path.getsize(fPath) > 0:

                    self.report = NmrDpReport()
                    self.report.loadJson(fPath)

                    self.report_prev = NmrDpReport()
                    self.report_prev.loadJson(fPath)

                    return True

                logging.error("+NmrDpUtility.__retrieveDpReport() ++ Error  - Could not find any content in file path %s." % fPath)
                raise IOError("+NmrDpUtility.__retrieveDpReport() ++ Error  - Could not find any content in file path %s." % fPath)

            logging.error("+NmrDpUtility.__retrieveDpReport() ++ Error  - Could not access to file path %s." % fPath)
            raise IOError("+NmrDpUtility.__retrieveDpReport() ++ Error  - Could not access to file path %s." % fPath)

        logging.error("+NmrDpUtility.__retrieveDpReport() ++ Error  - Could not find 'report_file_path' input parameter.")
        raise KeyError("+NmrDpUtility.__retrieveDpReport() ++ Error  - Could not find 'report_file_path' input parameter.")

    def __deleteSkippedSf(self):
        """ Delete skipped saveframes.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']
        file_name = input_source_dic['file_name']

        warnings = self.report.warning.getValueList('skipped_sf_category', file_name)

        if warnings is None:
            return True

        for w in warnings:

            if self.__star_data_type == "Entry" or self.__star_data_type == "Saveframe":

                if not 'sf_category' in w:

                    err = "Could not specify 'sf_category' in NMR data processing report."

                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__deleteSkippedSf() ++ Error  - %s" % err)
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__deleteSkippedSf() ++ Error  - %s\n" % err)

                else:

                    sf_list = self.__star_data.get_saveframes_by_category(w['sf_category'])

                    if sf_list is None:

                        err = "Could not specify sf_category %s unexpectedly in %s file." % (w['sf_category'], file_name)

                        self.report.error.appendDescription('internal_error', "+NmrDpUtility.__deleteSkippedSf() ++ Error  - %s" % err)
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__deleteSkippedSf() ++ Error  - %s\n" % err)

                    else:

                        for sf_data in reversed(sf_list):
                            del self.__star_data[sf_data]

            else:

                err = "Unexpected PyNMRSTAR object type %s found about %s file." % (self.__star_data_type, file_name)

                self.report.error.appendDescription('internal_error', "+NmrDpUtility.__deleteSkippedSf() ++ Error  - %s" % err)
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__deleteSkippedSf() ++ Error  - %s\n" % err)

        return True

    def __deleteSkippedLoop(self):
        """ Delete skipped loops.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']
        file_name = input_source_dic['file_name']

        warnings = self.report.warning.getValueList('skipped_lp_category', file_name)

        if warnings is None:
            return True

        for w in warnings:

            if self.__star_data_type == "Entry" or self.__star_data_type == "Saveframe":

                if not 'sf_framecode' in w:

                    err = "Could not specify 'sf_framecode' in NMR data processing report."

                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__deleteSkippedLoop() ++ Error  - %s" % err)
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__deleteSkippedLoop() ++ Error  - %s\n" % err)

                else:

                    sf_data = self.__star_data.get_saveframe_by_name(w['sf_framecode'])

                    if sf_data is None:

                        err = "Could not specify saveframe %s unexpectedly in %s file." % (w['sf_framecode'], file_name)

                        self.report.error.appendDescription('internal_error', "+NmrDpUtility.__deleteSkippedLoop() ++ Error  - %s" % err)
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__deleteSkippedLoop() ++ Error  - %s\n" % err)

                    else:

                        if not 'category' in w:

                            err = "Could not specify 'category' in NMR data processing report."

                            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__deleteSkippedLoop() ++ Error  - %s" % err)
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__deleteSkippedLoop() ++ Error  - %s\n" % err)

                        else:
                            del sf_data[w['category']]

            else:

                err = "Unexpected PyNMRSTAR object type %s found about %s file." % (self.__star_data_type, file_name)

                self.report.error.appendDescription('internal_error', "+NmrDpUtility.__deleteSkippedLoop() ++ Error  - %s" % err)
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__deleteSkippedLoop() ++ Error  - %s\n" % err)

        return True

    def __updatePolymerSequence(self):
        """ Update polymer sequence.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        has_poly_seq = self.__hasKeyValue(input_source_dic, 'polymer_sequence')

        if not has_poly_seq:

            err = "Common polymer sequence did not exist, __extractCommonPolymerSequence() should be invoked."

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__generatePolySeqIfNot() ++ Error  - %s" % err)
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__generatePolySeqIfNot() ++ Error  - %s\n" % err)

            return False

        if self.__srcPath is self.__dstPath:
            return True

        content_subtype = 'poly_seq'

        sf_category = self.sf_categories[file_type][content_subtype]
        lp_category = self.lp_categories[file_type][content_subtype]

        key_items = self.key_items[file_type][content_subtype]
        data_items = self.data_items[file_type][content_subtype]

        orig_lp_data = None

        has_res_var_dat = False

        has_auth_asym_id = False
        has_auth_seq_id = False
        has_auth_comp_id = False
        has_nef_index_dat = False
        has_assembly_id = False
        has_entry_id = False

        try:

            sf_data = self.__star_data.get_saveframes_by_category(sf_category)[0]

            if not sf_data is None:

                sf_framecode = sf_data.get_tag('sf_framecode')[0]

                orig_lp_data = next((l['data'] for l in self.__lp_data[content_subtype] if l['sf_framecode'] == sf_framecode), None)

                if orig_lp_data is None:
                    orig_lp_data = self.__nefT.check_data(sf_data, lp_category, key_items, data_items, None, None)[0]

                if file_type == 'nef':
                    if 'residue_variant' in orig_lp_data[0]:
                        result = next((i for i in orig_lp_data if not i['residue_variant'] in self.empty_value), None)
                        if not result is None:
                            has_res_var_dat = True

                else:
                    if 'Auth_variant_ID' in orig_lp_data[0]:
                        result = next((i for i in orig_lp_data if not i['Auth_variant_ID'] in self.empty_value), None)
                        if not result is None:
                            has_res_var_dat = True

                    if 'Auth_asym_ID' in orig_lp_data[0]:
                        result = next((i for i in orig_lp_data if not i['Auth_asym_ID'] in self.empty_value), None)
                        if not result is None:
                            has_auth_asym_id = True

                    if 'Auth_seq_ID' in orig_lp_data[0]:
                        result = next((i for i in orig_lp_data if not i['Auth_seq_ID'] in self.empty_value), None)
                        if not result is None:
                            has_auth_seq_id = True

                    if 'Auth_comp_ID' in orig_lp_data[0]:
                        result = next((i for i in orig_lp_data if not i['Auth_comp_ID'] in self.empty_value), None)
                        if not result is None:
                            has_auth_comp_id = True

                    if 'NEF_index' in orig_lp_data[0]:
                        result = next((i for i in orig_lp_data if not i['NEF_index'] in self.empty_value), None)
                        if not result is None:
                            has_nef_index_dat = True

                    if 'Assembly_ID' in orig_lp_data[0]:
                        has_assembly_id = True

                    if 'Entry_ID' in orig_lp_data[0]:
                        has_entry_id = True

        except:
            pass

        sf_cat_name = '_nef_molecular_system' if file_type == 'nef' else '_Assembly'

        poly_seq_sf_data = pynmrstar.Saveframe.from_scratch(sf_cat_name)

        if file_type == 'nef':
            poly_seq_sf_data.add_tag(sf_cat_name + '.sf_category', 'nef_molecular_system')
            poly_seq_sf_data.add_tag(sf_cat_name + '.sf_framecode', 'nef_molecular_system')
        else:
            poly_seq_sf_data.add_tag(sf_cat_name + '.Sf_category', 'assembly')
            poly_seq_sf_data.add_tag(sf_cat_name + '.Sf_framecode', 'assembly')

        lp_cat_name = '_nef_sequence' if file_type == 'nef' else '_Chem_comp_assembly'

        lp_data = pynmrstar.Loop.from_scratch(lp_cat_name)

        has_index_tag = not self.index_tags[file_type][content_subtype] is None

        if has_index_tag:
            lp_data.add_tag(lp_cat_name + '.' + self.index_tags[file_type][content_subtype])

        for key_item in key_items:
            lp_data.add_tag(lp_cat_name + '.' + key_item['name'])

        for data_item in data_items:
            data_name = data_item['name']
            if data_name != 'NEF_index':
                lp_data.add_tag(lp_cat_name + '.' + data_name)
            elif has_nef_index_dat:
                lp_data.add_tag(lp_cat_name + '.' + data_name)

        if has_entry_id:
            lp_data.add_tag(lp_cat_name + '.Entry_ID')

        polymer_sequence = input_source_dic['polymer_sequence']

        if not polymer_sequence is None:

            chains = []

            for s in polymer_sequence:
                chains.append(s['chain_id'])

            row_id = 1

            for s in polymer_sequence:

                chain_id = s['chain_id']
                seq_id_offset = 1 - s['seq_id'][0]

                length = len(s['seq_id'])

                cyclic = self.__isCyclicPolymer(chain_id)

                if cyclic:
                    self.report.setCyclicPolymer(cyclic)

                for j in range(length):

                    row = []

                    if has_index_tag:
                        row.append(row_id)

                    auth_seq_id = s['seq_id'][j]
                    auth_comp_id = s['comp_id'][j]

                    seq_id = auth_seq_id #+ seq_id_offset
                    _seq_id_ = auth_seq_id + seq_id_offset
                    comp_id = auth_comp_id.upper()

                    if file_type == 'nef':

                        row.append(chain_id) # chain_code
                        row.append(seq_id) # sequence_code
                        row.append(comp_id) # residue_name

                        # linking

                        if cyclic and (_seq_id_ == 1 or _seq_id_ == length):
                            row.append('cyclic')
                        elif _seq_id_ == 1 and length == 1:
                            row.append('single')
                        elif _seq_id_ == 1:
                            row.append('start')
                        elif _seq_id_ == length:
                            row.append('end')
                        elif auth_seq_id - 1 == s['seq_id'][j - 1] and auth_seq_id + 1 == s['seq_id'][j + 1]:
                            row.append('middle')
                        else:
                            row.append('break')

                        # residue_variant

                        if has_res_var_dat:
                            orig_row = next((i for i in orig_lp_data if i['chain_code'] == chain_id and i['sequence_code'] == auth_seq_id and i['residue_name'] == auth_comp_id), None)
                            if not orig_row is None:
                                row.append(orig_row['residue_variant'])
                            else:
                                row.append('.')
                        else:
                            row.append('.')

                        # cis_peptide

                        if self.__isProtCis(chain_id, seq_id):
                            row.append('true')
                        elif comp_id == 'PRO' or comp_id == 'GLY':
                            row.append('false')
                        else:
                            row.append('.')

                    else:

                        cid = chains.index(chain_id) + 1

                        row.append(cid) # Entity_assembly_ID
                        row.append(seq_id) # Comp_index_ID
                        row.append(comp_id) # Comp_ID

                        orig_row = next((i for i in orig_lp_data if i['Entity_assembly_ID'] == cid and i['Comp_index_ID'] == auth_seq_id and i['Comp_ID'] == auth_comp_id), None)

                        # Auth_asym_ID

                        if has_auth_asym_id:
                            if not orig_row is None:
                                row.append(orig_row['Auth_asym_ID'])
                            else:
                                row.append(chain_id)
                        else:
                            row.append(chain_id)

                        # Auth_seq_ID

                        if has_auth_seq_id:
                            if not orig_row is None:
                                row.append(orig_row['Auth_seq_ID'])
                            else:
                                row.append(auth_seq_id)
                        else:
                            row.append(auth_seq_id)

                        # Auth_comp_ID

                        if has_auth_comp_id:
                            if not orig_row is None:
                                row.append(orig_row['Auth_comp_ID'])
                            else:
                                row.append(auth_comp_id)
                        else:
                            row.append(auth_comp_id)

                        # Auth_variant_ID

                        if has_res_var_dat:
                            if not orig_row is None:
                                row.append(orig_row['Auth_variant_ID'])
                            else:
                                row.append('.')
                        else:
                            row.append('.')

                        # Sequence_linking

                        if cyclic and (seq_id == 1 or seq_id == length):
                            row.append('cyclic')
                        elif seq_id == 1 and length == 1:
                            row.append('single')
                        elif seq_id == 1:
                            row.append('start')
                        elif seq_id == length:
                            row.append('end')
                        elif auth_seq_id - 1 == s['seq_id'][j - 1] and auth_seq_id + 1 == s['seq_id'][j + 1]:
                            row.append('middle')
                        else:
                            row.append('break')

                        # Cis_residue

                        if self.__isProtCis(chain_id, seq_id):
                            row.append('yes')
                        elif comp_id == 'PRO' or comp_id == 'GLY':
                            row.append('no')
                        else:
                            row.append('.')

                        # NEF_index

                        if has_nef_index_dat:
                            if not orig_row is None:
                                row.append(orig_row['NEF_index'])
                            else:
                                row.append('.')

                        # Assembly_ID

                        if has_assembly_id:
                            if not orig_row is None:
                                row.append(orig_row['Assembly_ID'])
                            else:
                                row.append(1)

                        else:
                            row.append(1)

                        if has_entry_id:
                            if not orig_row is None:
                                row.append(orig_row['Entry_ID'])
                            else:
                                row.append('.')

                    lp_data.add_data(row)

                    row_id += 1

            poly_seq_sf_data.add_loop(lp_data)

            # replace polymer sequence

            sf_list = self.__star_data.get_saveframes_by_category(sf_category)

            if not sf_list is None:

                for old_sf_data in reversed(sf_list):
                    del self.__star_data[old_sf_data]

        norm_star_data = copy.copy(self.__star_data)

        for content_subtype in self.nmr_content_subtypes:

            sf_category = self.sf_categories[file_type][content_subtype]

            if content_subtype == 'poly_seq':

                if not polymer_sequence is None:
                    norm_star_data.add_saveframe(poly_seq_sf_data)

            elif (not input_source_dic['content_subtype'] is None) and content_subtype in input_source_dic['content_subtype']:

                sf_list = self.__star_data.get_saveframes_by_category(sf_category)

                if not sf_list is None:

                    for old_sf_data in reversed(sf_list):
                        del norm_star_data[old_sf_data]

                    for sf_data in sf_list:
                        norm_star_data.add_saveframe(sf_data)

        self.__star_data = norm_star_data

        #if file_type == 'nmr-star':
        #   self.__star_data.normalize()

        return True

    def __isCyclicPolymer(self, nmr_chain_id):
        """ Return whether a given chain is cyclic polymer based on coordinate annotation.
            @return: True for cyclic polymer or False otherwise
        """

        id = self.report.getInputSourceIdOfCoord()

        if id < 0:
            return False

        cif_input_source = self.report.input_sources[id]
        cif_input_source_dic = cif_input_source.get()

        cif_polymer_sequence = cif_input_source_dic['polymer_sequence']

        chain_assign_dic = self.report.chain_assignment.get()

        if not 'nmr_poly_seq_vs_model_poly_seq' in chain_assign_dic:

            err = "Chain assignment did not exist, __assignCoordPolymerSequence() should be invoked."

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__isCyclicPolymer() ++ Error  - %s" % err)
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__isCyclicPolymer() ++ Error  - %s\n" % err)

            return False

        if chain_assign_dic['nmr_poly_seq_vs_model_poly_seq'] is None:
            return False

        for chain_assign in chain_assign_dic['nmr_poly_seq_vs_model_poly_seq']:

            if chain_assign['ref_chain_id'] != nmr_chain_id:
                continue

            cif_chain_id = chain_assign['test_chain_id']

            for s in cif_polymer_sequence:

                if s['chain_id'] != cif_chain_id:
                    continue

                beg_cif_seq_id = s['seq_id'][0]
                end_cif_seq_id = s['seq_id'][-1]

                try:

                    struct_conn = self.__cR.getDictListWithFilter('struct_conn',
                                                                  [{'name': 'conn_type_id', 'type': 'str'}
                                                                   ],
                                                                  [{'name': 'pdbx_leaving_atom_flag', 'type': 'str', 'value': 'both'},
                                                                   {'name': 'ptnr1_label_asym_id', 'type': 'str', 'value': cif_chain_id},
                                                                   {'name': 'ptnr2_label_asym_id', 'type': 'str', 'value': cif_chain_id},
                                                                   {'name': 'ptnr1_label_seq_id', 'type': 'int', 'value': beg_cif_seq_id},
                                                                   {'name': 'ptnr2_label_seq_id', 'type': 'int', 'value': end_cif_seq_id},
                                                                   ])

                except Exception as e:

                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__isCyclicPolymer() ++ Error  - %s" % str(e))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__isCyclicPolymer() ++ Error  - %s" % str(e))

                    return False

                if len(struct_conn) == 0:
                    return False

                elif struct_conn[0]['conn_type_id'] == 'covale':
                    return True

        return False

    def __isProtCis(self, nmr_chain_id, nmr_seq_id):
        """ Return whether type of peptide conformer of a given sequence is cis based on coordinate annotation.
            @return: True for cis peptide conformer or False otherwise
        """

        id = self.report.getInputSourceIdOfCoord()

        if id < 0:
            return False

        cif_input_source = self.report.input_sources[id]
        cif_input_source_dic = cif_input_source.get()

        cif_polymer_sequence = cif_input_source_dic['polymer_sequence']

        seq_align_dic = self.report.sequence_alignment.get()
        chain_assign_dic = self.report.chain_assignment.get()

        if not 'nmr_poly_seq_vs_model_poly_seq' in chain_assign_dic:

            err = "Chain assignment did not exist, __assignCoordPolymerSequence() should be invoked."

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__isProtCis() ++ Error  - %s" % err)
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__isProtCis() ++ Error  - %s\n" % err)

            return False

        if chain_assign_dic['nmr_poly_seq_vs_model_poly_seq'] is None:
            return False

        for chain_assign in chain_assign_dic['nmr_poly_seq_vs_model_poly_seq']:

            if chain_assign['ref_chain_id'] != nmr_chain_id:
                continue

            cif_chain_id = chain_assign['test_chain_id']

            result = next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq'] if seq_align['ref_chain_id'] == nmr_chain_id and seq_align['test_chain_id'] == cif_chain_id), None)

            if not result is None:

                cif_seq_id = None
                for k in range(result['length']):
                    if result['ref_seq_id'][k] == nmr_seq_id:
                        cif_seq_id = result['test_seq_id'][k]
                        break

                if cif_seq_id is None:
                    continue

                try:

                    prot_cis = self.__cR.getDictListWithFilter('struct_mon_prot_cis',
                                                               [{'name': 'pdbx_PDB_model_num', 'type': 'int'}
                                                                ],
                                                               [{'name': 'pdbx_label_asym_id_2', 'type': 'str', 'value': cif_chain_id},
                                                                {'name': 'pdbx_label_seq_id_2', 'type': 'int', 'value': cif_seq_id}
                                                                ])

                except Exception as e:

                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__isProtCis() ++ Error  - %s" % str(e))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__isProtCis() ++ Error  - %s" % str(e))

                    return False

                return len(prot_cis) > 0

        return False

    def __getTautomerOfHistidine(self, nmr_chain_id, nmr_seq_id):
        """ Return tautomeric state of a given histidine based on coordinate annotation.
            @return: One of 'biprotonated', 'tau-tautomer', 'pi-tautomer', 'unknown'
        """

        id = self.report.getInputSourceIdOfCoord()

        if id < 0:
            return 'unknown'

        cif_input_source = self.report.input_sources[id]
        cif_input_source_dic = cif_input_source.get()

        cif_polymer_sequence = cif_input_source_dic['polymer_sequence']

        seq_align_dic = self.report.sequence_alignment.get()
        chain_assign_dic = self.report.chain_assignment.get()

        if not 'nmr_poly_seq_vs_model_poly_seq' in chain_assign_dic:

            err = "Chain assignment did not exist, __assignCoordPolymerSequence() should be invoked."

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__getTautomerOfHistidine() ++ Error  - %s" % err)
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__getTautomerOfHistidine() ++ Error  - %s\n" % err)

            return 'unknown'

        if chain_assign_dic['nmr_poly_seq_vs_model_poly_seq'] is None:
            return 'unknown'

        for chain_assign in chain_assign_dic['nmr_poly_seq_vs_model_poly_seq']:

            if chain_assign['ref_chain_id'] != nmr_chain_id:
                continue

            cif_chain_id = chain_assign['test_chain_id']

            result = next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq'] if seq_align['ref_chain_id'] == nmr_chain_id and seq_align['test_chain_id'] == cif_chain_id), None)

            if not result is None:

                cif_seq_id = None
                for k in range(result['length']):
                    if result['ref_seq_id'][k] == nmr_seq_id and result['ref_code'][k] == 'H':
                        cif_seq_id = result['test_seq_id'][k]
                        break

                if cif_seq_id is None:
                    continue

                try:

                    protons = self.__cR.getDictListWithFilter('atom_site',
                                                    [{'name': 'label_atom_id', 'type': 'str', 'alt_name': 'atom_id'}
                                                     ],
                                                    [{'name': 'label_asym_id', 'type': 'str', 'value': cif_chain_id},
                                                     {'name': 'label_seq_id', 'type': 'int', 'value': cif_seq_id},
                                                     {'name': 'label_comp_id', 'type': 'str', 'value': 'HIS'},
                                                     {'name': 'type_symbol', 'type': 'str', 'value': 'H'},
                                                     {'name': 'pdbx_PDB_model_num', 'type': 'int', 'value': 1}])

                except Exception as e:

                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__getTautomerOfHistidine() ++ Error  - %s" % str(e))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__getTautomerOfHistidine() ++ Error  - %s" % str(e))

                    return 'unknown'

                if len(protons) > 0:

                    has_hd1 = False
                    has_he2 = False

                    for h in protons:
                        if h['atom_id'] == 'HD1':
                            has_hd1 = True
                        elif h['atom_id'] == 'HE2':
                            has_he2 = True

                    if has_hd1 and has_he2:
                        return 'biprotonated'
                    elif has_hd1:
                        return 'tau-tautomer'
                    elif has_he2:
                        return 'pi-tautomer'

        return 'unknown'

    def __extractCoordDisulfideBond(self):
        """ Extract disulfide bond of coordinate file.
        """

        id = self.report.getInputSourceIdOfCoord()

        if id < 0:
            return False

        input_source = self.report.input_sources[id]

        chain_assign_dic = self.report.chain_assignment.get()

        if not 'model_poly_seq_vs_nmr_poly_seq' in chain_assign_dic:

            err = "Chain assignment did not exist, __assignCoordPolymerSequence() should be invoked."

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__extractCoodDisulfideBond() ++ Error  - %s" % err)
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__extractCoodDisulfideBond() ++ Error  - %s\n" % err)

            return False

        if chain_assign_dic['model_poly_seq_vs_nmr_poly_seq'] is None:
            return False

        try:

            struct_conn = self.__cR.getDictListWithFilter('struct_conn',
                                                          [{'name': 'conn_type_id', 'type': 'str'},
                                                           {'name': 'ptnr1_label_asym_id', 'type': 'str'},
                                                           {'name': 'ptnr1_label_seq_id', 'type': 'int'},
                                                           {'name': 'ptnr1_label_comp_id', 'type': 'str'},
                                                           {'name': 'ptnr1_label_atom_id', 'type': 'str'},
                                                           {'name': 'ptnr2_label_asym_id', 'type': 'str'},
                                                           {'name': 'ptnr2_label_seq_id', 'type': 'int'},
                                                           {'name': 'ptnr2_label_comp_id', 'type': 'str'},
                                                           {'name': 'ptnr2_label_atom_id', 'type': 'str'},
                                                           {'name': 'pdbx_dist_value', 'type': 'float'}
                                                           ])

        except Exception as e:

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__extractCoodDisulfideBond() ++ Error  - %s" % str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__extractCoodDisulfideBond() ++ Error  - %s" % str(e))

            return False

        if len(struct_conn) > 0:

            asm = []

            for sc in struct_conn:

                if sc['conn_type_id'] != 'disulf':
                    continue

                disulf = {}
                disulf['chain_id_1'] = sc['ptnr1_label_asym_id']
                disulf['seq_id_1'] = sc['ptnr1_label_seq_id']
                disulf['comp_id_1'] = sc['ptnr1_label_comp_id']
                disulf['atom_id_1'] = sc['ptnr1_label_atom_id']
                disulf['chain_id_2'] = sc['ptnr2_label_asym_id']
                disulf['seq_id_2'] = sc['ptnr2_label_seq_id']
                disulf['comp_id_2'] = sc['ptnr2_label_comp_id']
                disulf['atom_id_2'] = sc['ptnr2_label_atom_id']
                disulf['distance_value'] = sc['pdbx_dist_value']
                asm.append(disulf)

            if len(asm) > 0:
                input_source.setItemValue('disulfide_bond', asm)

                self.report.setDisulfideBond(True)

                return self.__mapCoordDisulfideBond2Nmr(asm)

        return True

    def __mapCoordDisulfideBond2Nmr(self, bond_list):
        """ Map disulfide bond of coordinate file to NMR data.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        polymer_sequence = input_source_dic['polymer_sequence']

        if polymer_sequence is None:
            return False

        seq_align_dic = self.report.sequence_alignment.get()
        chain_assign_dic = self.report.chain_assignment.get()

        if not 'nmr_poly_seq_vs_model_poly_seq' in chain_assign_dic:

            err = "Chain assignment did not exist, __assignCoordPolymerSequence() should be invoked."

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__mapCoordDisulfideBond2Nmr() ++ Error  - %s" % err)
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__mapCoordDisulfideBond2Nmr() ++ Error  - %s\n" % err)

            return False

        if chain_assign_dic['model_poly_seq_vs_nmr_poly_seq'] is None:
            return False

        content_subtype = 'chem_shift'

        if not content_subtype in input_source_dic['content_subtype'].keys():

            err = "Assigned chemical shift loop did not exist in %s file." % file_name

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__mapCoordDisulfideBond2Nmr() ++ Error  - %s" % err)
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__mapCoordDisulfideBond2Nmr() ++ Error  - %s\n" % err)

            return False

        sf_category = self.sf_categories[file_type][content_subtype]
        lp_category = self.lp_categories[file_type][content_subtype]

        key_items = self.key_items[file_type][content_subtype]
        data_items = self.data_items[file_type][content_subtype]

        item_names = self.item_names_in_cs_loop[file_type]
        chain_id_name = item_names['chain_id']
        seq_id_name = item_names['seq_id']
        comp_id_name = item_names['comp_id']
        atom_id_name = item_names['atom_id']
        value_name = item_names['value']

        asm = []

        for bond in bond_list:

            cif_chain_id_1 = bond['chain_id_1']
            cif_seq_id_1 = bond['seq_id_1']
            cif_chain_id_2 = bond['chain_id_2']
            cif_seq_id_2 = bond['seq_id_2']

            try:
                ca = next(ca for ca in chain_assign_dic['model_poly_seq_vs_nmr_poly_seq'] if ca['ref_chain_id'] == cif_chain_id_1)
                nmr_chain_id_1 = ca['test_chain_id']
            except StopIteration:
                continue

            result = next((seq_align for seq_align in seq_align_dic['model_poly_seq_vs_nmr_poly_seq'] if seq_align['ref_chain_id'] == cif_chain_id_1 and seq_align['test_chain_id'] == nmr_chain_id_1), None)

            if result is None:
                continue

            nmr_seq_id_1 = None
            for k in range(result['length']):
                if result['ref_seq_id'][k] == cif_seq_id_1:
                    nmr_seq_id_1 = result['test_seq_id'][k]
                    break

            if nmr_seq_id_1 is None:
                continue

            ps1 = next((ps1 for ps1 in polymer_sequence if ps1['chain_id'] == nmr_chain_id_1), None)

            if ps1 is None:
                continue

            nmr_comp_id_1 = None
            for k in range(len(ps1['seq_id'])):
                if ps1['seq_id'][k] == nmr_seq_id_1:
                    nmr_comp_id_1 = ps1['comp_id'][k]
                    break

            if nmr_comp_id_1 is None:
                continue

            try:
                ca = next(ca for ca in chain_assign_dic['model_poly_seq_vs_nmr_poly_seq'] if ca['ref_chain_id'] == cif_chain_id_2)
                nmr_chain_id_2 = ca['test_chain_id']
            except StopIteration:
                continue

            result = next((seq_align for seq_align in seq_align_dic['model_poly_seq_vs_nmr_poly_seq'] if seq_align['ref_chain_id'] == cif_chain_id_2 and seq_align['test_chain_id'] == nmr_chain_id_2), None)

            if result is None:
                continue

            nmr_seq_id_2 = None
            for k in range(result['length']):
                if result['ref_seq_id'][k] == cif_seq_id_2:
                    nmr_seq_id_2 = result['test_seq_id'][k]
                    break

            if nmr_seq_id_2 is None:
                continue

            ps2 = next((ps2 for ps2 in polymer_sequence if ps2['chain_id'] == nmr_chain_id_2), None)

            if ps2 is None:
                continue

            nmr_comp_id_2 = None
            for k in range(len(ps2['seq_id'])):
                if ps2['seq_id'][k] == nmr_seq_id_2:
                    nmr_comp_id_2 = ps2['comp_id'][k]
                    break

            if nmr_comp_id_2 is None:
                continue

            disulf = {}
            disulf['chain_id_1'] = nmr_chain_id_1
            disulf['seq_id_1'] = nmr_seq_id_1
            disulf['comp_id_1'] = nmr_comp_id_1
            disulf['atom_id_1'] = bond['atom_id_1']
            disulf['chain_id_2'] = nmr_chain_id_2
            disulf['seq_id_2'] = nmr_seq_id_2
            disulf['comp_id_2'] = nmr_comp_id_2
            disulf['atom_id_2'] = bond['atom_id_2']
            disulf['distance_value'] = bond['distance_value']
            disulf['warning_description_1'] = None
            disulf['warning_description_2'] = None

            ca_chem_shift_1 = None
            cb_chem_shift_1 = None
            ca_chem_shift_2 = None
            cb_chem_shift_2 = None

            for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

                sf_framecode = sf_data.get_tag('sf_framecode')[0]

                if self.report.error.exists(file_name, sf_framecode):
                    continue

                lp_data = next((l['data'] for l in self.__lp_data[content_subtype] if l['sf_framecode'] == sf_framecode), None)

                if lp_data is None:

                    try:

                        lp_data = self.__nefT.check_data(sf_data, lp_category, key_items, data_items, None, None)[0]

                        self.__lp_data[content_subtype].append({'sf_framecode': sf_framecode, 'data': lp_data})

                    except:
                        pass

                if not lp_data is None:

                    for i in lp_data:
                        _chain_id = i[chain_id_name]
                        seq_id = i[seq_id_name]
                        comp_id = i[comp_id_name]
                        atom_id = i[atom_id_name]

                        if type(_chain_id) is int:
                            chain_id = str(_chain_id)
                        else:
                            chain_id = _chain_id

                        if chain_id == nmr_chain_id_1 and seq_id == nmr_seq_id_1 and comp_id == nmr_comp_id_1:
                            if atom_id == 'CA' and ca_chem_shift_1 is None:
                                ca_chem_shift_1 = i[value_name]
                            elif atom_id == 'CB' and cb_chem_shift_1 is None:
                                cb_chem_shift_1 = i[value_name]

                        elif chain_id == nmr_chain_id_2 and seq_id == nmr_seq_id_2 and comp_id == nmr_comp_id_2:
                            if atom_id == 'CA' and ca_chem_shift_2 is None:
                                ca_chem_shift_2 = i[value_name]
                            elif atom_id == 'CB' and cb_chem_shift_2 is None:
                                cb_chem_shift_2 = i[value_name]

                        if ca_chem_shift_1 is None or cb_chem_shift_1 is None or ca_chem_shift_2 is None or cb_chem_shift_2 is None:
                            pass
                        else:
                            break

                    if ca_chem_shift_1 is None or cb_chem_shift_1 is None or ca_chem_shift_2 is None or cb_chem_shift_2 is None:
                        pass
                    else:
                        break

            disulf['ca_chem_shift_1'] = ca_chem_shift_1
            disulf['cb_chem_shift_1'] = cb_chem_shift_1
            disulf['ca_chem_shift_2'] = ca_chem_shift_2
            disulf['cb_chem_shift_2'] = cb_chem_shift_2

            if not cb_chem_shift_1 is None:
                if cb_chem_shift_1 < 32.0:
                    disulf['redox_state_pred_1'] = 'reduced'
                elif cb_chem_shift_1 > 35.0:
                    disulf['redox_state_pred_1'] = 'oxidized'
                elif not cb_chem_shift_2 is None:
                    if cb_chem_shift_2 < 32.0:
                        disulf['redox_state_pred_1'] = 'reduced'
                    elif cb_chem_shift_2 > 35.0:
                        disulf['redox_state_pred_1'] = 'oxidized'
                    else:
                        disulf['redox_state_pred_1'] = 'ambiguous'
                else:
                    disulf['redox_state_pred_1'] = 'ambiguous'
            else:
                disulf['redox_state_pred_1'] = 'unknown'

            if not cb_chem_shift_2 is None:
                if cb_chem_shift_2 < 32.0:
                    disulf['redox_state_pred_2'] = 'reduced'
                elif cb_chem_shift_2 > 35.0:
                    disulf['redox_state_pred_2'] = 'oxidized'
                elif not cb_chem_shift_1 is None:
                    if cb_chem_shift_1 < 32.0:
                        disulf['redox_state_pred_2'] = 'reduced'
                    elif cb_chem_shift_1 > 35.0:
                        disulf['redox_state_pred_2'] = 'oxidized'
                    else:
                        disulf['redox_state_pred_2'] = 'ambiguous'
                else:
                    disulf['redox_state_pred_2'] = 'ambiguous'
            else:
                disulf['redox_state_pred_2'] = 'unknown'

            if disulf['redox_state_pred_1'] == 'ambiguous' and (not ca_chem_shift_1 is None or not cb_chem_shift_1 is None):
                oxi, red = self.__predictRedoxStateOfCystein(ca_chem_shift_1, cb_chem_shift_1)
                disulf['redox_state_pred_1'] = 'oxidized %s (%%), reduced %s (%%)' % ('{:.1f}'.format(oxi * 100.0), '{:.1f}'.format(red * 100.0))

            if disulf['redox_state_pred_2'] == 'ambiguous' and (not ca_chem_shift_2 is None or not cb_chem_shift_2 is None):
                oxi, red = self.__predictRedoxStateOfCystein(ca_chem_shift_2, cb_chem_shift_2)
                disulf['redox_state_pred_2'] = 'oxidized %s (%%), reduced %s (%%)' % ('{:.1f}'.format(oxi * 100.0), '{:.1f}'.format(red * 100.0))

            if disulf['redox_state_pred_1'] != 'oxidized' and disulf['redox_state_pred_1'] != 'unknown':

                warn = "Disulfide bond (chain_id_1 %s, seq_id_1 %s, comp_id_1 %s, chain_id_2 %s, seq_id_2 %s, comp_id_2 %s) could not supported by assigned chemical shift values (CA_1 %s, CB_1 %s, redox_state_pred_1 %s)." %\
                       (nmr_chain_id_1, nmr_seq_id_1, nmr_comp_id_1, nmr_chain_id_2, nmr_seq_id_2, nmr_comp_id_2, ca_chem_shift_1, cb_chem_shift_1, disulf['redox_state_pred_1'])

                item = 'suspicious_data' if disulf['redox_state_pred_1'] == 'reduced' else 'unusual_data'

                self.report.warning.appendDescription(item, {'file_name': file_name, 'sf_framecode': sf_framecode, 'description': warn})
                self.report.setWarning()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__mapCoordDisulfideBond2Nmr() ++ Warning  - %s\n" % warn)

                disulf['warning_description_1'] = item + ': ' + warn

            if disulf['redox_state_pred_2'] != 'oxidized' and disulf['redox_state_pred_2'] != 'unknown':

                warn = "Disulfide bond (chain_id_1 %s, seq_id_1 %s, comp_id_1 %s, chain_id_2 %s, seq_id_2 %s, comp_id_2 %s) could not supported by assigned chemical shift values (CA_2 %s, CB_2 %s, redox_state_pred_2 %s)." %\
                       (nmr_chain_id_1, nmr_seq_id_1, nmr_comp_id_1, nmr_chain_id_2, nmr_seq_id_2, nmr_comp_id_2, ca_chem_shift_2, cb_chem_shift_2, disulf['redox_state_pred_2'])

                item = 'suspicious_data' if disulf['redox_state_pred_2'] == 'reduced' else 'unusual_data'

                self.report.warning.appendDescription(item, {'file_name': file_name, 'sf_framecode': sf_framecode, 'description': warn})
                self.report.setWarning()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__mapCoordDisulfideBond2Nmr() ++ Warning  - %s\n" % warn)

                disulf['warning_description_2'] = item + ': ' + warn

            asm.append(disulf)

        if len(asm) > 0:
            input_source.setItemValue('disulfide_bond', asm)
            return True

        return False

    def __extractCoordOtherBond(self):
        """ Extract other bond (neither disulfide nor covalent bond) of coordinate file.
        """

        id = self.report.getInputSourceIdOfCoord()

        if id < 0:
            return False

        input_source = self.report.input_sources[id]

        chain_assign_dic = self.report.chain_assignment.get()

        if not 'model_poly_seq_vs_nmr_poly_seq' in chain_assign_dic:

            err = "Chain assignment did not exist, __assignCoordPolymerSequence() should be invoked."

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__extractCoodOtherBond() ++ Error  - %s" % err)
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__extractCoodOtherBond() ++ Error  - %s\n" % err)

            return False

        if chain_assign_dic['model_poly_seq_vs_nmr_poly_seq'] is None:
            return False

        try:

            struct_conn = self.__cR.getDictListWithFilter('struct_conn',
                                                          [{'name': 'conn_type_id', 'type': 'str'},
                                                           {'name': 'ptnr1_label_asym_id', 'type': 'str'},
                                                           {'name': 'ptnr1_label_seq_id', 'type': 'int'},
                                                           {'name': 'ptnr1_label_comp_id', 'type': 'str'},
                                                           {'name': 'ptnr1_label_atom_id', 'type': 'str'},
                                                           {'name': 'ptnr2_label_asym_id', 'type': 'str'},
                                                           {'name': 'ptnr2_label_seq_id', 'type': 'int'},
                                                           {'name': 'ptnr2_label_comp_id', 'type': 'str'},
                                                           {'name': 'ptnr2_label_atom_id', 'type': 'str'},
                                                           {'name': 'pdbx_dist_value', 'type': 'float'}
                                                           ])

        except Exception as e:

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__extractCoodOtherBond() ++ Error  - %s" % str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__extractCoodOtherBond() ++ Error  - %s" % str(e))

            return False

        if len(struct_conn) > 0:

            asm = []

            for sc in struct_conn:

                if sc['conn_type_id'] == 'disulf' or sc['conn_type_id'] == 'covale' or sc['conn_type_id'] == 'hydrog':
                    continue

                other = {}
                other['chain_id_1'] = sc['ptnr1_label_asym_id']
                other['seq_id_1'] = sc['ptnr1_label_seq_id']
                other['comp_id_1'] = sc['ptnr1_label_comp_id']
                other['atom_id_1'] = sc['ptnr1_label_atom_id']
                other['chain_id_2'] = sc['ptnr2_label_asym_id']
                other['seq_id_2'] = sc['ptnr2_label_seq_id']
                other['comp_id_2'] = sc['ptnr2_label_comp_id']
                other['atom_id_2'] = sc['ptnr2_label_atom_id']
                other['distance_value'] = sc['pdbx_dist_value']
                asm.append(other)

            if len(asm) > 0:
                input_source.setItemValue('other_bond', asm)

                self.report.setOtherBond(True)

                return self.__mapCoordOtherBond2Nmr(asm)

        return True

    def __mapCoordOtherBond2Nmr(self, bond_list):
        """ Map other bond (neither disulfide nor covalent bond) of coordinate file to NMR data.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        polymer_sequence = input_source_dic['polymer_sequence']

        if polymer_sequence is None:
            return False

        seq_align_dic = self.report.sequence_alignment.get()
        chain_assign_dic = self.report.chain_assignment.get()

        if not 'nmr_poly_seq_vs_model_poly_seq' in chain_assign_dic:

            err = "Chain assignment did not exist, __assignCoordPolymerSequence() should be invoked."

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__mapCoordOtherBond2Nmr() ++ Error  - %s" % err)
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__mapCoordOtherBond2Nmr() ++ Error  - %s\n" % err)

            return False

        if chain_assign_dic['model_poly_seq_vs_nmr_poly_seq'] is None:
            return False

        content_subtype = 'chem_shift'

        if not content_subtype in input_source_dic['content_subtype'].keys():

            err = "Assigned chemical shift loop did not exist in %s file." % file_name

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__mapCoordOtherBond2Nmr() ++ Error  - %s" % err)
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__mapCoordOtherBond2Nmr() ++ Error  - %s\n" % err)

            return False

        sf_category = self.sf_categories[file_type][content_subtype]
        lp_category = self.lp_categories[file_type][content_subtype]

        key_items = self.key_items[file_type][content_subtype]
        data_items = self.data_items[file_type][content_subtype]

        item_names = self.item_names_in_cs_loop[file_type]
        chain_id_name = item_names['chain_id']
        seq_id_name = item_names['seq_id']
        comp_id_name = item_names['comp_id']
        atom_id_name = item_names['atom_id']
        value_name = item_names['value']

        asm = []

        for bond in bond_list:

            cif_chain_id_1 = bond['chain_id_1']
            cif_seq_id_1 = bond['seq_id_1']
            cif_chain_id_2 = bond['chain_id_2']
            cif_seq_id_2 = bond['seq_id_2']

            try:
                ca = next(ca for ca in chain_assign_dic['model_poly_seq_vs_nmr_poly_seq'] if ca['ref_chain_id'] == cif_chain_id_1)
                nmr_chain_id_1 = ca['test_chain_id']
            except StopIteration:
                continue

            result = next((seq_align for seq_align in seq_align_dic['model_poly_seq_vs_nmr_poly_seq'] if seq_align['ref_chain_id'] == cif_chain_id_1 and seq_align['test_chain_id'] == nmr_chain_id_1), None)

            if result is None:
                continue

            nmr_seq_id_1 = None
            for k in range(result['length']):
                if result['ref_seq_id'][k] == cif_seq_id_1:
                    nmr_seq_id_1 = result['test_seq_id'][k]
                    break

            if nmr_seq_id_1 is None:
                continue

            ps1 = next((ps1 for ps1 in polymer_sequence if ps1['chain_id'] == nmr_chain_id_1), None)

            if ps1 is None:
                continue

            nmr_comp_id_1 = None
            for k in range(len(ps1['seq_id'])):
                if ps1['seq_id'][k] == nmr_seq_id_1:
                    nmr_comp_id_1 = ps1['comp_id'][k]
                    break

            if nmr_comp_id_1 is None:
                continue

            try:
                ca = next(ca for ca in chain_assign_dic['model_poly_seq_vs_nmr_poly_seq'] if ca['ref_chain_id'] == cif_chain_id_2)
                nmr_chain_id_2 = ca['test_chain_id']
            except StopIteration:
                continue

            result = next((seq_align for seq_align in seq_align_dic['model_poly_seq_vs_nmr_poly_seq'] if seq_align['ref_chain_id'] == cif_chain_id_2 and seq_align['test_chain_id'] == nmr_chain_id_2), None)

            if result is None:
                continue

            nmr_seq_id_2 = None
            for k in range(result['length']):
                if result['ref_seq_id'][k] == cif_seq_id_2:
                    nmr_seq_id_2 = result['test_seq_id'][k]
                    break

            if nmr_seq_id_2 is None:
                continue

            ps2 = next((ps2 for ps2 in polymer_sequence if ps2['chain_id'] == nmr_chain_id_2), None)

            if ps2 is None:
                continue

            nmr_comp_id_2 = None
            for k in range(len(ps2['seq_id'])):
                if ps2['seq_id'][k] == nmr_seq_id_2:
                    nmr_comp_id_2 = ps2['comp_id'][k]
                    break

            if nmr_comp_id_2 is None:
                continue

            other = {}
            other['chain_id_1'] = nmr_chain_id_1
            other['seq_id_1'] = nmr_seq_id_1
            other['comp_id_1'] = nmr_comp_id_1
            other['atom_id_1'] = bond['atom_id_1']
            other['chain_id_2'] = nmr_chain_id_2
            other['seq_id_2'] = nmr_seq_id_2
            other['comp_id_2'] = nmr_comp_id_2
            other['atom_id_2'] = bond['atom_id_2']
            other['distance_value'] = bond['distance_value']
            other['warning_description_1'] = None
            other['warning_description_2'] = None

            ca_chem_shift_1 = None
            cb_chem_shift_1 = None
            ca_chem_shift_2 = None
            cb_chem_shift_2 = None

            for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

                sf_framecode = sf_data.get_tag('sf_framecode')[0]

                if self.report.error.exists(file_name, sf_framecode):
                    continue

                lp_data = next((l['data'] for l in self.__lp_data[content_subtype] if l['sf_framecode'] == sf_framecode), None)

                if lp_data is None:

                    try:

                        lp_data = self.__nefT.check_data(sf_data, lp_category, key_items, data_items, None, None)[0]

                        self.__lp_data[content_subtype].append({'sf_framecode': sf_framecode, 'data': lp_data})

                    except:
                        pass

                if not lp_data is None:

                    for i in lp_data:
                        _chain_id = i[chain_id_name]
                        seq_id = i[seq_id_name]
                        comp_id = i[comp_id_name]
                        atom_id = i[atom_id_name]

                        if type(_chain_id) is int:
                            chain_id = str(_chain_id)
                        else:
                            chain_id = _chain_id

                        if chain_id == nmr_chain_id_1 and seq_id == nmr_seq_id_1 and comp_id == nmr_comp_id_1:
                            if atom_id == 'CA' and ca_chem_shift_1 is None:
                                ca_chem_shift_1 = i[value_name]
                            elif atom_id == 'CB' and cb_chem_shift_1 is None:
                                cb_chem_shift_1 = i[value_name]

                        elif chain_id == nmr_chain_id_2 and seq_id == nmr_seq_id_2 and comp_id == nmr_comp_id_2:
                            if atom_id == 'CA' and ca_chem_shift_2 is None:
                                ca_chem_shift_2 = i[value_name]
                            elif atom_id == 'CB' and cb_chem_shift_2 is None:
                                cb_chem_shift_2 = i[value_name]

                        if ca_chem_shift_1 is None or cb_chem_shift_1 is None or ca_chem_shift_2 is None or cb_chem_shift_2 is None:
                            pass
                        else:
                            break

                    if ca_chem_shift_1 is None or cb_chem_shift_1 is None or ca_chem_shift_2 is None or cb_chem_shift_2 is None:
                        pass
                    else:
                        break

            other['ca_chem_shift_1'] = ca_chem_shift_1
            other['cb_chem_shift_1'] = cb_chem_shift_1
            other['ca_chem_shift_2'] = ca_chem_shift_2
            other['cb_chem_shift_2'] = cb_chem_shift_2

            if not cb_chem_shift_1 is None:
                if cb_chem_shift_1 < 32.0:
                    other['redox_state_pred_1'] = 'reduced'
                elif cb_chem_shift_1 > 35.0:
                    other['redox_state_pred_1'] = 'oxidized'
                elif not cb_chem_shift_2 is None:
                    if cb_chem_shift_2 < 32.0:
                        other['redox_state_pred_1'] = 'reduced'
                    elif cb_chem_shift_2 > 35.0:
                        other['redox_state_pred_1'] = 'oxidized'
                    else:
                        other['redox_state_pred_1'] = 'ambiguous'
                else:
                    other['redox_state_pred_1'] = 'ambiguous'
            else:
                other['redox_state_pred_1'] = 'unknown'

            if not cb_chem_shift_2 is None:
                if cb_chem_shift_2 < 32.0:
                    other['redox_state_pred_2'] = 'reduced'
                elif cb_chem_shift_2 > 35.0:
                    other['redox_state_pred_2'] = 'oxidized'
                elif not cb_chem_shift_1 is None:
                    if cb_chem_shift_1 < 32.0:
                        other['redox_state_pred_2'] = 'reduced'
                    elif cb_chem_shift_1 > 35.0:
                        other['redox_state_pred_2'] = 'oxidized'
                    else:
                        other['redox_state_pred_2'] = 'ambiguous'
                else:
                    other['redox_state_pred_2'] = 'ambiguous'
            else:
                other['redox_state_pred_2'] = 'unknown'

            if other['redox_state_pred_1'] == 'ambiguous' and (not ca_chem_shift_1 is None or not cb_chem_shift_1 is None):
                oxi, red = self.__predictRedoxStateOfCystein(ca_chem_shift_1, cb_chem_shift_1)
                other['redox_state_pred_1'] = 'oxidized %s (%%), reduced %s (%%)' % ('{:.1f}'.format(oxi * 100.0), '{:.1f}'.format(red * 100.0))

            if other['redox_state_pred_2'] == 'ambiguous' and (not ca_chem_shift_2 is None or not cb_chem_shift_2 is None):
                oxi, red = self.__predictRedoxStateOfCystein(ca_chem_shift_2, cb_chem_shift_2)
                other['redox_state_pred_2'] = 'oxidized %s (%%), reduced %s (%%)' % ('{:.1f}'.format(oxi * 100.0), '{:.1f}'.format(red * 100.0))

            if other['redox_state_pred_1'] != 'oxidized' and other['redox_state_pred_1'] != 'unknown':

                warn = "Other bond (chain_id_1 %s, seq_id_1 %s, comp_id_1 %s, chain_id_2 %s, seq_id_2 %s, comp_id_2 %s) could not supported by assigned chemical shift values (CA_1 %s, CB_1 %s, redox_state_pred_1 %s)." %\
                       (nmr_chain_id_1, nmr_seq_id_1, nmr_comp_id_1, nmr_chain_id_2, nmr_seq_id_2, nmr_comp_id_2, ca_chem_shift_1, cb_chem_shift_1, other['redox_state_pred_1'])

                item = 'suspicious_data' if other['redox_state_pred_1'] == 'reduced' else 'unusual_data'

                self.report.warning.appendDescription(item, {'file_name': file_name, 'sf_framecode': sf_framecode, 'description': warn})
                self.report.setWarning()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__mapCoordOtherBond2Nmr() ++ Warning  - %s\n" % warn)

                other['warning_description_1'] = item + ': ' + warn

            if other['redox_state_pred_2'] != 'oxidized' and other['redox_state_pred_2'] != 'unknown':

                warn = "Other bond (chain_id_1 %s, seq_id_1 %s, comp_id_1 %s, chain_id_2 %s, seq_id_2 %s, comp_id_2 %s) could not supported by assigned chemical shift values (CA_2 %s, CB_2 %s, redox_state_pred_2 %s)." %\
                       (nmr_chain_id_1, nmr_seq_id_1, nmr_comp_id_1, nmr_chain_id_2, nmr_seq_id_2, nmr_comp_id_2, ca_chem_shift_2, cb_chem_shift_2, other['redox_state_pred_2'])

                item = 'suspicious_data' if other['redox_state_pred_2'] == 'reduced' else 'unusual_data'

                self.report.warning.appendDescription(item, {'file_name': file_name, 'sf_framecode': sf_framecode, 'description': warn})
                self.report.setWarning()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__mapCoordOtherBond2Nmr() ++ Warning  - %s\n" % warn)

                other['warning_description_2'] = item + ': ' + warn

            asm.append(other)

        if len(asm) > 0:
            input_source.setItemValue('other_bond', asm)
            return True

        return False

    def __predictRedoxStateOfCystein(self, ca_chem_shift, cb_chem_shift):
        """ Return prediction of redox state of Cystein using assigned CA, CB chemical shifts.
            @return: probability of oxidized state, probability of reduced state
        """

        oxi_ca = {'avr': 55.5, 'std': 2.5}
        oxi_cb = {'avr': 40.7, 'std': 3.8}

        red_ca = {'avr': 59.3, 'std': 3.2}
        red_cb = {'avr': 28.3, 'std': 2.2}

        oxi = 1.0
        red = 1.0

        if not ca_chem_shift is None:
            oxi *= self.__probabilityDensity(ca_chem_shift, oxi_ca['avr'], oxi_ca['std'])
            red *= self.__probabilityDensity(ca_chem_shift, red_ca['avr'], red_ca['std'])

        if not cb_chem_shift is None:
            if cb_chem_shift < 32.0:
                oxi = 0.0
            else:
                oxi *= self.__probabilityDensity(cb_chem_shift, oxi_cb['avr'], oxi_cb['std'])
            if cb_chem_shift > 35.0:
                red = 0.0
            else:
                red *= self.__probabilityDensity(cb_chem_shift, red_cb['avr'], red_cb['std'])

        sum = oxi + red

        if sum == 0.0 or sum == 2.0:
            return 0.0, 0.0

        return oxi / sum, red / sum

    def __predictCisTransPeptideOfProline(self, cb_chem_shift, cg_chem_shift):
        """ Return prediction of cis-trans peptide bond of Proline using assigned CB, CG chemical shifts.
            @return: probability of cis-peptide bond, probability of trans-peptide bond
        """

        cis_cb = {'avr': 34.16, 'std': 1.15, 'max': 36.23, 'min': 30.74}
        cis_cg = {'avr': 24.52, 'std': 1.09, 'max': 27.01, 'min': 22.10}
        cis_dl = {'avr': 9.64, 'std': 1.27}

        trs_cb = {'avr': 31.75, 'std': 0.98, 'max': 35.83, 'min': 26.30}
        trs_cg = {'avr': 27.26, 'std': 1.05, 'max': 33.39, 'min': 19.31}
        trs_dl = {'avr': 4.51, 'std': 1.17}

        cis = 1.0
        trs = 1.0

        if not cb_chem_shift is None:
            if cb_chem_shift < cis_cb['min'] - cis_cb['std'] or cb_chem_shift > cis_cb['max'] + cis_cb['std']:
                cis = 0.0
            else:
                cis *= self.__probabilityDensity(cb_chem_shift, cis_cb['avr'], cis_cb['std'])
            if cb_chem_shift < trs_cb['min'] - trs_cb['std'] or cb_chem_shift > trs_cb['max'] + trs_cb['std']:
                trs = 0.0
            else:
                trs *= self.__probabilityDensity(cb_chem_shift, trs_cb['avr'], trs_cb['std'])

        if not cg_chem_shift is None:
            if cg_chem_shift < cis_cg['min'] - cis_cg['std'] or cg_chem_shift > cis_cg['max'] + cis_cg['std']:
                cis = 0.0
            else:
                cis *= self.__probabilityDensity(cg_chem_shift, cis_cg['avr'], cis_cg['std'])
            if cg_chem_shift < trs_cg['min'] - trs_cg['std'] or cg_chem_shift > trs_cg['max'] + trs_cg['std']:
                trs = 0.0
            else:
                trs *= self.__probabilityDensity(cg_chem_shift, trs_cg['avr'], trs_cg['std'])

        if not cb_chem_shift is None and not cg_chem_shift is None:
            delta_shift = cb_chem_shift - cg_chem_shift

            cis *= self.__probabilityDensity(delta_shift, cis_dl['avr'], cis_dl['std'])
            trs *= self.__probabilityDensity(delta_shift, trs_dl['avr'], trs_dl['std'])

        sum = cis + trs

        if sum == 0.0 or sum == 2.0:
            return 0.0, 0.0

        return cis / sum, trs / sum

    def __predictTautomerOfHistidine(self, cg_chem_shift, cd2_chem_shift, nd1_chem_shift, ne2_chem_shift):
        """ Return prediction of tautomeric state of Histidine using assigned CG, CD2, ND1, and NE2 chemical shifts.
            @return: probability of biprotonated, probability of tau tautomer, probability of pi tautomer
        """

        bip_cg = {'avr': 131.2, 'std': 0.7}
        bip_cd2 = {'avr': 120.6, 'std': 1.3}
        bip_nd1 = {'avr': 190.0, 'std': 1.9}
        bip_ne2 = {'avr': 176.3, 'std': 1.9}

        tau_cg = {'avr': 135.7, 'std': 2.2}
        tau_cd2 = {'avr': 116.9, 'std': 2.1}
        tau_nd1 = {'avr': 249.4, 'std': 1.9}
        tau_ne2 = {'avr': 171.1, 'std': 1.9}

        pi_cg = {'avr': 125.7, 'std': 2.2}
        pi_cd2 = {'avr': 125.6, 'std': 2.1}
        pi_nd1 = {'avr': 171.8, 'std': 1.9}
        pi_ne2 = {'avr': 248.2, 'std': 1.9}

        bip = 1.0
        tau = 1.0
        pi = 1.0

        if not cg_chem_shift is None:
            bip *= self.__probabilityDensity(cg_chem_shift, bip_cg['avr'], bip_cg['std'])
            tau *= self.__probabilityDensity(cg_chem_shift, tau_cg['avr'], tau_cg['std'])
            pi *= self.__probabilityDensity(cg_chem_shift, pi_cg['avr'], pi_cg['std'])

        if not cd2_chem_shift is None:
            bip *= self.__probabilityDensity(cd2_chem_shift, bip_cd2['avr'], bip_cd2['std'])
            tau *= self.__probabilityDensity(cd2_chem_shift, tau_cd2['avr'], tau_cd2['std'])
            pi *= self.__probabilityDensity(cd2_chem_shift, pi_cd2['avr'], pi_cd2['std'])

        if not nd1_chem_shift is None:
            bip *= self.__probabilityDensity(nd1_chem_shift, bip_nd1['avr'], bip_nd1['std'])
            tau *= self.__probabilityDensity(nd1_chem_shift, tau_nd1['avr'], tau_nd1['std'])
            pi *= self.__probabilityDensity(nd1_chem_shift, pi_nd1['avr'], pi_nd1['std'])

        if not ne2_chem_shift is None:
            bip *= self.__probabilityDensity(ne2_chem_shift, bip_ne2['avr'], bip_ne2['std'])
            tau *= self.__probabilityDensity(ne2_chem_shift, tau_ne2['avr'], tau_ne2['std'])
            pi *= self.__probabilityDensity(ne2_chem_shift, pi_ne2['avr'], pi_ne2['std'])

        sum = bip + tau + pi

        if sum == 0.0 or sum == 3.0:
            return 0.0, 0.0, 0.0

        return bip / sum, tau / sum, pi / sum

    def __probabilityDensity(self, value, mean, stddev):
        """ Return probability density.
        """

        return math.exp(-((value - mean) ** 2.0) / (2.0 * (stddev ** 2))) / ((2.0 * math.pi * (stddev ** 2.0)) ** 0.5)

    def __updateDihedralAngleType(self):
        """ Update dihedral angle types (phi, psi, omega, chi[1-5] for polypeptide-like residue) if possible.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']
        file_name = input_source_dic['file_name']

        content_subtype = 'dihed_restraint'

        if input_source_dic['content_subtype'] is None:
            return True

        if not content_subtype in input_source_dic['content_subtype'].keys():
            return True

        item_names = self.item_names_in_dh_loop[file_type]
        index_id_name = self.index_tags[file_type][content_subtype]
        chain_id_1_name = item_names['chain_id_1']
        chain_id_2_name = item_names['chain_id_2']
        chain_id_3_name = item_names['chain_id_3']
        chain_id_4_name = item_names['chain_id_4']
        seq_id_1_name = item_names['seq_id_1']
        seq_id_2_name = item_names['seq_id_2']
        seq_id_3_name = item_names['seq_id_3']
        seq_id_4_name = item_names['seq_id_4']
        comp_id_1_name = item_names['comp_id_1']
        atom_id_1_name = item_names['atom_id_1']
        atom_id_2_name = item_names['atom_id_2']
        atom_id_3_name = item_names['atom_id_3']
        atom_id_4_name = item_names['atom_id_4']
        angle_type_name = item_names['angle_type']

        dihed_atom_ids = ['N', 'CA', 'C']

        chi1_atom_id_4_pat = re.compile(r'^[COS]G1?$')
        chi2_atom_id_3_pat = re.compile(r'^CG1?$')
        chi2_atom_id_4_pat = re.compile(r'^[CNOS]D1?$')
        chi3_atom_id_3_pat = re.compile(r'^[CS]D$')
        chi3_atom_id_4_pat = re.compile(r'^[CNO]E1?$')
        chi4_atom_id_3_pat = re.compile(r'^[CN]E$')
        chi4_atom_id_4_pat = re.compile(r'^[CN]Z$')

        sf_category = self.sf_categories[file_type][content_subtype]
        lp_category = self.lp_categories[file_type][content_subtype]

        for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

            sf_framecode = sf_data.get_tag('sf_framecode')[0]

            lp_data = next((l['data'] for l in self.__lp_data[content_subtype] if l['sf_framecode'] == sf_framecode), None)

            if lp_data is None:

                key_items = self.key_items[file_type][content_subtype]
                data_items = self.data_items[file_type][content_subtype]

                try:

                    lp_data = self.__nefT.check_data(sf_data, lp_category, key_items, data_items, None, None)[0]

                    self.__lp_data[content_subtype].append({'sf_framecode': w['sf_framecode'], 'data': lp_data})

                except:
                    pass

            if not lp_data is None:

                phi_index = []
                psi_index = []
                omega_index = []
                chi1_index = []
                chi2_index = []
                chi3_index = []
                chi4_index = []
                chi5_index = []

                try:

                    for i in lp_data:
                        index_id = i[index_id_name]
                        chain_id_1 = i[chain_id_1_name]
                        chain_id_2 = i[chain_id_2_name]
                        chain_id_3 = i[chain_id_3_name]
                        chain_id_4 = i[chain_id_4_name]
                        seq_ids = []
                        seq_ids.append(i[seq_id_1_name])
                        seq_ids.append(i[seq_id_2_name])
                        seq_ids.append(i[seq_id_3_name])
                        seq_ids.append(i[seq_id_4_name])
                        comp_id = i[comp_id_1_name]
                        atom_ids = []
                        atom_ids.append(i[atom_id_1_name])
                        atom_ids.append(i[atom_id_2_name])
                        atom_ids.append(i[atom_id_3_name])
                        atom_ids.append(i[atom_id_4_name])
                        angle_type = i[angle_type_name]

                        if not angle_type in self.empty_value:
                           continue

                        if chain_id_1 != chain_id_2 or chain_id_2 != chain_id_3 or chain_id_3 != chain_id_4:
                            continue

                        polypeptide_like = self.__csStat.getTypeOfCompId(comp_id)[0]

                        if not polypeptide_like:
                            continue

                        seq_id_common = collections.Counter(seq_ids).most_common()

                        if len(seq_id_common) == 2:

                            # phi or psi

                            if seq_id_common[0][1] == 3 and seq_id_common[1][1] == 1:

                                # phi

                                seq_id_prev = seq_id_common[1][0]

                                if seq_id_common[0][0] == seq_id_prev + 1:

                                    j = 0
                                    if seq_ids[j] == seq_id_prev and atom_ids[j] == 'C':
                                        atom_ids.pop(j)
                                        if atom_ids == dihed_atom_ids:
                                            phi_index.append(index_id)

                                # psi

                                seq_id_next = seq_id_common[1][0]

                                if seq_id_common[0][0] == seq_id_next - 1:

                                    j = 3
                                    if seq_ids[j] == seq_id_next and atom_ids[j] == 'N':
                                        atom_ids.pop(j)
                                        if atom_ids == dihed_atom_ids:
                                            psi_index.append(index_id)

                            # omega

                            if atom_ids[0] == 'O' and atom_ids[1] == 'C' and atom_ids[2] == 'N' and (atom_ids[3] == 'H' or atom_ids[3] == 'CA') and\
                               seq_ids[0] == seq_ids[1] and seq_ids[1] + 1 == seq_ids[2] and seq_ids[2] == seq_ids[3]:
                                omega_index.append(index_id)

                        elif len(seq_id_common) == 1:

                            # chi1

                            if atom_ids[0] == 'N' and atom_ids[1] == 'CA' and atom_ids[2] == 'CB' and chi1_atom_id_4_pat.match(atom_ids[3]):
                                #if (atom_ids[3] == 'CG' and comp_id in ['ARG', 'ASN', 'ASP', 'GLN', 'GLU', 'HIS', 'LEU', 'LYS', 'MET', 'PHE', 'PRO', 'TRP', 'TYR']) or\
                                #   (atom_ids[3] == 'CG1' and comp_id in ['ILE', 'VAL']) or\
                                #   (atom_ids[3] == 'OG' and comp_id == 'SER') or\
                                #   (atom_ids[3] == 'OG1' and comp_id == 'THR') or\
                                #   (atom_ids[3] == 'SG' and comp_id == 'CYS'):
                               chi1_index.append(index_id)

                            # chi2

                            if atom_ids[0] == 'CA' and atom_ids[1] == 'CB' and chi2_atom_id_3_pat(atom_ids[2]) and chi2_atom_id_4_pat(atom_ids[3]):
                                #if (atom_ids[2] == 'CG' and atom_ids[3] == 'CD' and comp_id in ['ARG', 'GLN', 'GLU', 'LYS', 'PRO']) or\
                                #   (atom_ids[2] == 'CG' and atom_ids[3] == 'CD1' and comp_id in ['LEU', 'PHE', 'TRP', 'TYR']) or\
                                #   (atom_ids[2] == 'CG' and atom_ids[3] == 'ND1' and comp_id == 'HIS') or\
                                #   (atom_ids[2] == 'CG' and atom_ids[3] == 'OD1' and comp_id in ['ASN', 'ASP']) or\
                                #   (atom_ids[2] == 'CG' and atom_ids[3] == 'SD' and comp_id == 'MET') or\
                                #   (atom_ids[2] == 'CG1' and atom_ids[3] == 'CD' and comp_id == 'ILE'):
                                chi2_index.append(index_id)

                            # chi3

                            if atom_ids[0] == 'CB' and atom_ids[1] == 'CG' and chi3_atom_id_3_pat(atom_ids[2]) and chi3_atom_id_4_pat(atom_ids[3]):
                                #if (atom_ids[2] == 'CD' and atom_ids[3] == 'CE' and comp_id == 'LYS') or\
                                #   (atom_ids[2] == 'CD' and atom_ids[3] == 'NE' and comp_id == 'ARG') or\
                                #   (atom_ids[2] == 'CD' and atom_ids[3] == 'OE1' and comp_id in ['GLN', 'GLU']) or\
                                #   (atom_ids[2] == 'SD' and atom_ids[3] == 'CE' and comp_id == 'MET'):
                                chi3_index.append(index_id)

                            # chi4

                            if atom_ids[0] == 'CG' and atom_ids[1] == 'CD' and chi4_atom_id_3_pat(atom_ids[2]) and chi4_atom_id_4_par(atom_ids[3]):
                                #if (atom_ids[2] == 'NE' and atom_ids[3] == 'CZ' and comp_id == 'ARG') or\
                                #  (atom_ids[2] == 'CE' and atom_ids[3] == 'NZ' and comp_id == 'LYS'):
                                chi4_index.append(index_id)

                            # chi5

                            if atom_ids == ['CD', 'NE', 'CZ', 'NH1']: # and comp_id == 'ARG':
                                chi5_index.append(index_id)

                except Exception as e:

                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__updateDihedralAngleType() ++ Error  - %s" % str(e))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__updateDihedralAngleType() ++ Error  - %s" % str(e))

                    return False

                if len(phi_index) + len(psi_index) + len(omega_index) +\
                   len(chi1_index) + len(chi2_index) + len(chi3_index) + len(chi4_index) + len(chi5_index) > 0:

                    lp_data = sf_data.get_loop_by_category(lp_category)

                    idxCol = lp_data.tags.index(index_id_name)
                    aglCol = lp_data.tags.index(angle_type_name)

                    for row in lp_data.data:

                        index_id = int(row[idxCol])

                        if index_id in phi_index:
                            row[aglCol] = 'PHI'
                        elif index_id in psi_index:
                            row[aglCol] = 'PSI'
                        elif index_id in omega_index:
                            row[aglCol] = 'OMEGA'
                        elif index_id in chi1_index:
                            row[aglCol] = 'CHI1'
                        elif index_id in chi2_index:
                            row[aglCol] = 'CHI2'
                        elif index_id in chi3_index:
                            row[aglCol] = 'CHI3'
                        elif index_id in chi4_index:
                            row[aglCol] = 'CHI4'
                        elif index_id in chi5_index:
                            row[aglCol] = 'CHI5'

        return True

    def __fixDisorderedIndex(self):
        """ Fix disordered indices.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']
        file_name = input_source_dic['file_name']

        warnings = self.report.warning.getValueList('disordered_index', file_name)

        if warnings is None:
            return True

        for w in warnings:

            if self.__star_data_type == "Entry" or self.__star_data_type == "Saveframe":

                if not 'sf_framecode' in w:

                    err = "Could not specify 'sf_framecode' in NMR data processing report."

                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__fixDisorderedIndex() ++ Error  - %s" % err)
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__fixDisorderedIndex() ++ Error  - %s\n" % err)

                else:

                    sf_data = self.__star_data.get_saveframe_by_name(w['sf_framecode'])

                    if sf_data is None:

                        err = "Could not specify saveframe %s unexpectedly in %s file." % (w['sf_framecode'], file_name)

                        self.report.error.appendDescription('internal_error', "+NmrDpUtility.__fixDisorderedIndex() ++ Error  - %s" % err)
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__fixDisorderedIndex() ++ Error  - %s\n" % err)

                    else:

                        if not 'category' in w:

                            err = "Could not specify 'category' in NMR data processing report."

                            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__fixDisorderedIndex() ++ Error  - %s" % err)
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__fixDisorderedIndex() ++ Error  - %s\n" % err)

                        else:

                            try:

                                content_subtype = next(c for c in input_source_dic['content_subtype'].keys() if self.lp_categories[file_type][c] == w['category'] and not self.index_tags[file_type][c] is None)

                                lp_data = sf_data.get_loop_by_category(w['category'])
                                lp_data.renumber_rows(self.index_tags[file_type][content_subtype])

                            except StopIteration:

                                err = "Could not specify content_subtype in NMR data processing report."

                                self.report.error.appendDescription('internal_error', "+NmrDpUtility.__fixDisorderedIndex() ++ Error  - %s" % err)
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write("+NmrDpUtility.__fixDisorderedIndex() ++ Error  - %s\n" % err)

            else:

                err = "Unexpected PyNMRSTAR object type %s found about %s file." % (self.__star_data_type, file_name)

                self.report.error.appendDescription('internal_error', "+NmrDpUtility.__fixDisorderedIndex() ++ Error  - %s" % err)
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__fixDisorderedIndex() ++ Error  - %s\n" % err)

        return True

    def __removeNonSenseZeroValue(self):
        """ Remove non-sense zero values.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']
        file_name = input_source_dic['file_name']

        warnings = self.report.warning.getValueList('missing_data', file_name)

        if warnings is None:
            return True

        for w in warnings:

            if not "is non-sense zero value" in w['description']:
                continue

            if self.__star_data_type == "Entry" or self.__star_data_type == "Saveframe":

                if not 'sf_framecode' in w:

                    err = "Could not specify 'sf_framecode' in NMR data processing report."

                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__removeNonSenseZeroValue() ++ Error  - %s" % err)
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__removeNonSenseZeroValue() ++ Error  - %s\n" % err)

                else:

                    sf_data = self.__star_data.get_saveframe_by_name(w['sf_framecode'])

                    if sf_data is None:

                        err = "Could not specify saveframe %s unexpectedly in %s file." % (w['sf_framecode'], file_name)

                        self.report.error.appendDescription('internal_error', "+NmrDpUtility.__removeNonSenseZeroValue() ++ Error  - %s" % err)
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__removeNonSenseZeroValue() ++ Error  - %s\n" % err)

                    else:

                        if not 'category' in w:

                            err = "Could not specify 'category' in NMR data processing report."

                            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__removeNonSenseZeroValue() ++ Error  - %s" % err)
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__removeNonSenseZeroValue() ++ Error  - %s\n" % err)

                        else:

                            itName = w['description'].split(' ')[0]

                            lp_data = sf_data.get_loop_by_category(w['category'])

                            if not itName in lp_data.tags:

                                err = "Could not find loop tag %s in %s category, %s saveframe, %s file." % (itName, w['category'], w['sf_framecode'], file_name)

                                self.report.error.appendDescription('internal_error', "+NmrDpUtility.__removeNonSenseZeroValue() ++ Error  - %s" % err)
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write("+NmrDpUtility.__removeNonSenseZeroValue() ++ Error  - %s\n" % err)

                            else:

                                itCol = lp_data.tags.index(itName)

                                for row in lp_data.data:

                                    val = row[itCol]

                                    if val is self.empty_value:
                                        continue

                                    try:
                                        if float(val) == 0:
                                            row[itCol] = '.'
                                    except ValueError:
                                        row[itCol] = '.'

            else:

                err = "Unexpected PyNMRSTAR object type %s found about %s file." % (self.__star_data_type, file_name)

                self.report.error.appendDescription('internal_error', "+NmrDpUtility.__removeNonSenseZeroValue() ++ Error  - %s" % err)
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__removeNonSenseZeroValue() ++ Error  - %s\n" % err)

        return True

    def __fixNonSenseNegativeValue(self):
        """ Fix non-sense negative values.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']
        file_name = input_source_dic['file_name']

        warnings = self.report.warning.getValueList('unusual_data', file_name)

        if warnings is None:
            return True

        for w in warnings:

            if not "is non-sense negative value" in w['description']:
                continue

            if self.__star_data_type == "Entry" or self.__star_data_type == "Saveframe":

                if not 'sf_framecode' in w:

                    err = "Could not specify 'sf_framecode' in NMR data processing report."

                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__fixNonSenseNegativeValue() ++ Error  - %s" % err)
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__fixNonSenseNegativeValue() ++ Error  - %s\n" % err)

                else:

                    sf_data = self.__star_data.get_saveframe_by_name(w['sf_framecode'])

                    if sf_data is None:

                        err = "Could not specify saveframe %s unexpectedly in %s file." % (w['sf_framecode'], file_name)

                        self.report.error.appendDescription('internal_error', "+NmrDpUtility.__fixNonSenseNegativeValue() ++ Error  - %s" % err)
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__fixNonSenseNegativeValue() ++ Error  - %s\n" % err)

                    else:

                        if not 'category' in w:

                            err = "Could not specify 'category' in NMR data processing report."

                            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__fixNonSenseNegativeValue() ++ Error  - %s" % err)
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__fixNonSenseNegativeValue() ++ Error  - %s\n" % err)

                        else:

                            itName = w['description'].split(' ')[0]

                            lp_data = sf_data.get_loop_by_category(w['category'])

                            if not itName in lp_data.tags:

                                err = "Could not find loop tag %s in %s category, %s saveframe, %s file." % (itName, w['category'], w['sf_framecode'], file_name)

                                self.report.error.appendDescription('internal_error', "+NmrDpUtility.__fixNonSenseNegativeValue() ++ Error  - %s" % err)
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write("+NmrDpUtility.__fixNonSenseNegativeValue() ++ Error  - %s\n" % err)

                            else:

                                itCol = lp_data.tags.index(itName)

                                for row in lp_data.data:

                                    val = row[itCol]

                                    if val is self.empty_value:
                                        continue

                                    try:
                                        if float(val) < 0.0:
                                            row[itCol] = abs(float(val))
                                    except ValueError:
                                        row[itCol] = '.'

            else:

                err = "Unexpected PyNMRSTAR object type %s found about %s file." % (self.__star_data_type, file_name)

                self.report.error.appendDescription('internal_error', "+NmrDpUtility.__fixNonSenseNegativeValue() ++ Error  - %s" % err)
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__fixNonSenseNegativeValue() ++ Error  - %s\n" % err)

        return True

    def __fixEnumerationValue(self):
        """ Fix enumeration failures if possible.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']
        file_name = input_source_dic['file_name']

        warnings = self.report.warning.getValueList('enum_failure', file_name)

        if warnings is None:
            return True

        self.chk_desc_pat = re.compile(r'^(.*) \'(.*)\' should be one of \((.*)\)\.$')
        self.chk_desc_pat_one = re.compile(r'^(.*) \'(.*)\' should be one of (.*)\.$')

        for w in warnings:

            if not "should be one of" in w['description']:
                continue

            try:
                g = self.chk_desc_pat.search(w['description']).groups()
            except AttributeError:
                g = self.chk_desc_pat_one.search(w['description']).groups()

            itName = g[0]
            itValue = None if g[1] in self.empty_value else g[1]
            itEnum = [str(e.strip("'")) for e in re.sub(r"\', \'", "\',\'", g[2]).split(',')]

            if self.__star_data_type == "Entry" or self.__star_data_type == "Saveframe":

                if not 'sf_framecode' in w:

                    err = "Could not specify 'sf_framecode' in NMR data processing report."

                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__fixEnumerationValue() ++ Error  - %s" % err)
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__fixEnumerationValue() ++ Error  - %s\n" % err)

                else:

                    sf_data = self.__star_data.get_saveframe_by_name(w['sf_framecode'])

                    if sf_data is None:

                        err = "Could not specify saveframe %s unexpectedly in %s file." % (w['sf_framecode'], file_name)

                        self.report.error.appendDescription('internal_error', "+NmrDpUtility.__fixEnumerationValue() ++ Error  - %s" % err)
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__fixEnumerationValue() ++ Error  - %s\n" % err)

                    else:

                        if not 'category' in w:

                            tagNames = [t[0] for t in sf_data.tags]

                            if not itName in tagNames:

                                err = "Could not find saveframe tag %s in %s saveframe, %s file." % (itName, w['sf_framecode'], file_name)

                                self.report.error.appendDescription('internal_error', "+NmrDpUtility.__fixEnumerationValue() ++ Error  - %s" % err)
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write("+NmrDpUtility.__fixEnumerationValue() ++ Error  - %s\n" % err)

                            else:

                                itCol = tagNames.index(itName)

                                val = sf_data.tags[itCol][1]
                                if val in self.empty_value:
                                    val = None

                                if val is itValue or val == itValue:
                                    if len(itEnum) == 1:
                                        sf_data.tags[itCol][1] = itEnum[0]

                                    # specific remediation follows
                                    else:

                                        sf_category = sf_data.get_tag('sf_category')[0]

                                        try:

                                            content_subtype = next(c for c in input_source_dic['content_subtype'].keys() if self.sf_categories[file_type][c] == sf_category)

                                            if (file_type == 'nef' and itName == 'restraint_origin') or (file_type == 'nmr-star' and itName == 'Constraint_type'):

                                                lp_data = next((l['data'] for l in self.__lp_data[content_subtype] if l['sf_framecode'] == w['sf_framecode']), None)

                                                if lp_data is None:
                                                    lp_category = self.lp_categories[file_type][content_subtype]

                                                    key_items = self.key_items[file_type][content_subtype]
                                                    data_items = self.data_items[file_type][content_subtype]

                                                    try:

                                                        lp_data = self.__nefT.check_data(sf_data, lp_category, key_items, data_items, None, None)[0]

                                                        self.__lp_data[content_subtype].append({'sf_framecode': w['sf_framecode'], 'data': lp_data})

                                                    except:
                                                        pass

                                                if not lp_data is None:

                                                    if content_subtype == 'dist_restraint':

                                                        # 'NOE', 'NOE build-up', 'NOE not seen', 'ROE', 'ROE build-up', 'hydrogen bond', 'disulfide bond', 'paramagnetic relaxation', 'symmetry', 'general distance'

                                                        if self.__testDistRestraintAsHydrogenBond(lp_data):
                                                            sf_data.tags[itCol][1] = 'hydrogen bond'

                                                        elif self.__testDistRestraintAsDisulfideBond(lp_data):
                                                            sf_data.tags[itCol][1] = 'disulfide bond'

                                                        elif self.__testDistRestraintAsSymmetry(lp_data):
                                                            sf_data.tags[itCol][1] = 'symmetry'

                                                    elif content_subtype == 'dihed_restraint':

                                                        # 'J-couplings', 'backbone chemical shifts'

                                                        if self.__testDihedRestraintAsBackBoneChemShifts(lp_data):
                                                            sf_data.tags[itCol][1] = 'backbone chemical shifts'
                                                        #else:
                                                        #    sf_data.tags[itCol][1] = 'J-couplings'

                                                    elif content_subtype == 'rdc_restraint':
                                                        sf_data.tags[itCol][1] = 'RDC'

                                            if (file_type == 'nef' and itName == 'potential_type') or (file_type == 'nmr-star' and itName == 'Potential_type'):

                                                lp_data = next((l['data'] for l in self.__lp_data[content_subtype] if l['sf_framecode'] == w['sf_framecode']), None)

                                                if lp_data is None:
                                                    lp_category = self.lp_categories[file_type][content_subtype]

                                                    key_items = self.key_items[file_type][content_subtype]
                                                    data_items = self.data_items[file_type][content_subtype]

                                                    try:

                                                        lp_data = self.__nefT.check_data(sf_data, lp_category, key_items, data_items, None, None)[0]

                                                        self.__lp_data[content_subtype].append({'sf_framecode': w['sf_framecode'], 'data': lp_data})

                                                    except:
                                                        pass

                                                if not lp_data is None:

                                                    # 'log-harmonic', 'parabolic'
                                                    # 'square-well-parabolic', 'square-well-parabolic-linear',
                                                    # 'upper-bound-parabolic', 'lower-bound-parabolic',
                                                    # 'upper-bound-parabolic-linear', 'lower-bound-parabolic-linear'

                                                    if self.__testRestraintPotentialSWP(content_subtype, lp_data):
                                                        sf_data.tags[itCol][1] = 'square-well-parabolic'
                                                    elif self.__testRestraintPotentialSWPL(content_subtype, lp_data):
                                                        sf_data.tags[itCol][1] = 'square-well-parabolic-linear'
                                                    elif self.__testRestraintPotentialUBP(content_subtype, lp_data):
                                                        sf_data.tags[itCol][1] = 'upper-bound-parabolic'
                                                    elif self.__testRestraintPotentialLBP(content_subtype, lp_data):
                                                        sf_data.tags[itCol][1] = 'lower-bound-parabolic'
                                                    elif self.__testRestraintPotentialUBPL(content_subtype, lp_data):
                                                        sf_data.tags[itCol][1] = 'upper-bound-parabolic-linear'
                                                    elif self.__testRestraintPotentialLBPL(content_subtype, lp_data):
                                                        sf_data.tags[itCol][1] = 'lower-bound-parabolic-linear'
                                                    elif self.__testRestraintPonentialLHorP(content_subtype, lp_data):
                                                        if content_subtype == 'dist_restraint':
                                                            sf_data.tags[itCol][1] = 'log-harmonic'
                                                        else:
                                                            sf_data.tags[itCol][1] = 'parabolic'

                                        except StopIteration:

                                            err = "Could not specify content_subtype in NMR data processing report."

                                            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__fixEnumeration() ++ Error  - %s" % err)
                                            self.report.setError()

                                            if self.__verbose:
                                                self.__lfh.write("+NmrDpUtility.__fixEnumeration() ++ Error  - %s\n" % err)

                        else:

                            lp_data = sf_data.get_loop_by_category(w['category'])

                            if not itName in lp_data.tags:

                                err = "Could not find loop tag %s in %s category, %s saveframe, %s file." % (itName, w['category'], w['sf_framecode'], file_name)

                                self.report.error.appendDescription('internal_error', "+NmrDpUtility.__fixEnumerationValue() ++ Error  - %s" % err)
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write("+NmrDpUtility.__fixEnumerationValue() ++ Error  - %s\n" % err)

                            else:

                                itCol = lp_data.tags.index(itName)

                                for row in lp_data.data:

                                    val = row[itCol]

                                    if val is self.empty_value:
                                        continue

                                    if val == itValue:

                                        if len(itEnum) == 1:
                                            row[itCol] = itEnum[0]

                                        elif file_type == 'nef' and itName == 'folding':

                                            # 'circular', 'mirror', 'none'

                                            if val in ['aliased', 'folded', 'not observed']:
                                                if val == 'aliased':
                                                    row[itCol] = 'mirror'
                                                elif val == 'folded':
                                                    row[itCol] = 'circular'
                                                else:
                                                    row[itCol] = 'none'

                                        elif file_type == 'nmr-star' and itName == 'Under_sampling_type':

                                            # 'aliased', 'folded', 'not observed'

                                            if val in ['circular', 'mirror', 'none']:
                                                if val == 'circular':
                                                    row[itCol] = 'folded'
                                                elif val == 'mirror':
                                                    row[itCol] = 'aliased'
                                                else:
                                                    row[itCol] = 'not observed'

            else:

                err = "Unexpected PyNMRSTAR object type %s found about %s file." % (self.__star_data_type, file_name)

                self.report.error.appendDescription('internal_error', "+NmrDpUtility.__fixEnumerationValue() ++ Error  - %s" % err)
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__fixEnumerationValue() ++ Error  - %s\n" % err)

        return True

    def __testDistRestraintAsHydrogenBond(self, lp_data):
        """ Detect whether given distance restraints are derived from hydrogen bonds.
        """

        if lp_data is None:
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        item_names = self.item_names_in_ds_loop[file_type]
        chain_id_1_name = item_names['chain_id_1']
        chain_id_2_name = item_names['chain_id_2']
        seq_id_1_name = item_names['seq_id_1']
        seq_id_2_name = item_names['seq_id_2']
        atom_id_1_name = item_names['atom_id_1']
        atom_id_2_name = item_names['atom_id_2']
        target_value_name = item_names['target_value']
        lower_limit_name = item_names['lower_limit']
        upper_limit_name = item_names['upper_limit']
        lower_linear_limit_name = item_names['lower_linear_limit']
        upper_linear_limit_name = item_names['upper_linear_limit']

        try:

            for i in lp_data:
                chain_id_1 = i[chain_id_1_name]
                chain_id_2 = i[chain_id_2_name]
                seq_id_1 = i[seq_id_1_name]
                seq_id_2 = i[seq_id_2_name]

                if chain_id_1 == chain_id_2 and seq_id_1 == seq_id_2:
                    return False

                target_value = i[target_value_name]
                upper_limit_value = None
                lower_limit_value = None

                if target_value is None:

                    if not i[lower_limit_name] is None and not i[upper_limit_name] is None:
                        target_value = (i[lower_limit_name] + i[upper_limit_name]) / 2.0

                    elif not i[lower_linear_limit_name] is None and not i[upper_linear_limit_name] is None:
                        target_value = (i[lower_linear_limit_name] + i[upper_linear_limit_name]) / 2.0

                    elif not i[upper_linear_limit_name] is None:
                        target_value = i[upper_linear_limit_name]
                        upper_limit_value = target_value

                    elif not i[upper_limit_name] is None:
                        target_value = i[upper_limit_name]
                        upper_limit_value = target_value

                    elif not i[lower_linear_limit_name] is None:
                        target_value = i[lower_linear_limit_name]
                        lower_limit_value = target_value

                    elif not i[lower_limit_name] is None:
                        target_value = i[lower_limit_name]
                        lower_limit_value = target_value

                    else:
                        return False

                atom_id_1_ = i[atom_id_1_name][0]
                atom_id_2_ = i[atom_id_2_name][0]

                if not upper_limit_value is None:
                    target_value -= 0.4
                elif not lower_limit_value is None:
                    target_value += 0.4

                if (atom_id_1_ == 'F' and atom_id_2_ == 'H') or (atom_id_2_ == 'F' and atom_id_1_ == 'H'):

                    if target_value < 1.2 or target_value > 1.5:
                        return False

                elif (atom_id_1_ == 'F' and atom_id_2_ == 'F') or (atom_id_2_ == 'F' and atom_id_1_ == 'F'):

                    if target_value < 2.2 or target_value > 2.5:
                        return False

                elif (atom_id_1_ == 'O' and atom_id_2_ == 'H') or (atom_id_2_ == 'O' and atom_id_1_ == 'H'):

                    if target_value < 1.5 or target_value > 2.2:
                        return False

                elif (atom_id_1_ == 'O' and atom_id_2_ == 'N') or (atom_id_2_ == 'O' and atom_id_1_ == 'N'):

                    if target_value < 2.5 or target_value > 3.2:
                        return False

                elif (atom_id_1_ == 'O' and atom_id_2_ == 'O') or (atom_id_2_ == 'O' and atom_id_1_ == 'O'):

                    if target_value < 2.5 or target_value > 3.2:
                        return False

                elif (atom_id_1_ == 'N' and atom_id_2_ == 'H') or (atom_id_2_ == 'N' and atom_id_1_ == 'H'):

                    if target_value < 1.5 or target_value > 2.2:
                        return False

                elif (atom_id_1_ == 'N' and atom_id_2_ == 'N') or (atom_id_2_ == 'N' and atom_id_1_ == 'N'):

                    if target_value < 2.5 or target_value > 3.2:
                        return False

                else:
                    return False

        except Exception as e:

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testDistRestraintAsHydrogenBond() ++ Error  - %s" % str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__testDistRestraintAsHydrogenBond() ++ Error  - %s" % str(e))

            return False

        return True

    def __testDistRestraintAsDisulfideBond(self, lp_data):
        """ Detect whether given distance restraints are derived from disulfide bonds.
        """

        if lp_data is None:
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        item_names = self.item_names_in_ds_loop[file_type]
        chain_id_1_name = item_names['chain_id_1']
        chain_id_2_name = item_names['chain_id_2']
        seq_id_1_name = item_names['seq_id_1']
        seq_id_2_name = item_names['seq_id_2']
        atom_id_1_name = item_names['atom_id_1']
        atom_id_2_name = item_names['atom_id_2']
        target_value_name = item_names['target_value']
        lower_limit_name = item_names['lower_limit']
        upper_limit_name = item_names['upper_limit']
        lower_linear_limit_name = item_names['lower_linear_limit']
        upper_linear_limit_name = item_names['upper_linear_limit']

        try:

            for i in lp_data:
                chain_id_1 = i[chain_id_1_name]
                chain_id_2 = i[chain_id_2_name]
                seq_id_1 = i[seq_id_1_name]
                seq_id_2 = i[seq_id_2_name]

                if chain_id_1 == chain_id_2 and seq_id_1 == seq_id_2:
                    return False

                target_value = i[target_value_name]
                upper_limit_value = None
                lower_limit_value = None

                if target_value is None:

                    if not i[lower_limit_name] is None and not i[upper_limit_name] is None:
                        target_value = (i[lower_limit_name] + i[upper_limit_name]) / 2.0

                    elif not i[lower_linear_limit_name] is None and not i[upper_linear_limit_name] is None:
                        target_value = (i[lower_linear_limit_name] + i[upper_linear_limit_name]) / 2.0

                    elif not i[upper_linear_limit_name] is None:
                        target_value = i[upper_linear_limit_name]
                        upper_limit_value = target_value

                    elif not i[upper_limit_name] is None:
                        target_value = i[upper_limit_name]
                        upper_limit_value = target_value

                    elif not i[lower_linear_limit_name] is None:
                        target_value = i[lower_linear_limit_name]
                        lower_limit_value = target_value

                    elif not i[lower_limit_name] is None:
                        target_value = i[lower_limit_name]
                        lower_limit_value = target_value

                    else:
                        return False

                atom_id_1_ = i[atom_id_1_name][0]
                atom_id_2_ = i[atom_id_2_name][0]

                if not upper_limit_value is None:
                    target_value -= 0.4
                elif not lower_limit_value is None:
                    target_value += 0.4

                if atom_id_1_ == 'S' and atom_id_2_ == 'S':

                    if target_value < 1.9 or target_value > 2.3:
                        return False

                else:
                    return False

        except Exception as e:

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testDistRestraintAsDisulfideBond() ++ Error  - %s" % str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__testDistRestraintAsDisulfideBond() ++ Error  - %s" % str(e))

            return False

        return True

    def __testDistRestraintAsSymmetry(self, lp_data):
        """ Detect whether given distance restraints are derived from symmetric assembly.
        """

        if lp_data is None:
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        item_names = self.item_names_in_ds_loop[file_type]
        chain_id_1_name = item_names['chain_id_1']
        chain_id_2_name = item_names['chain_id_2']
        seq_id_1_name = item_names['seq_id_1']
        seq_id_2_name = item_names['seq_id_2']
        comp_id_1_name = item_names['comp_id_1']
        comp_id_2_name = item_names['comp_id_2']

        try:

            for i in lp_data:
                chain_id_1 = i[chain_id_1_name]
                chain_id_2 = i[chain_id_2_name]
                seq_id_1 = i[seq_id_1_name]
                seq_id_2 = i[seq_id_2_name]
                comp_id_1 = i[comp_id_1_name]
                comp_id_2 = i[comp_id_2_name]

                if chain_id_1 == chain_id_2:
                    return False

                has_symmetry = False

                for j in lp_data:

                    if j is i:
                        continue

                    _chain_id_1 = j[chain_id_1_name]
                    _chain_id_2 = j[chain_id_2_name]
                    _seq_id_1 = j[seq_id_1_name]
                    _seq_id_2 = j[seq_id_2_name]
                    _comp_id_1 = j[comp_id_1_name]
                    _comp_id_2 = j[comp_id_2_name]

                    if _chain_id_1 != _chain_id_2 and _chain_id_1 != chain_id_1 and _chain_id_2 != chain_id_2:

                        if seq_id_1 == _seq_id_1 and comp_id_1 == _comp_id_1 and\
                           seq_id_2 == _seq_id_2 and comp_id_2 == _comp_id_2:
                            has_symmetry = True
                            break

                        elif seq_id_1 == _seq_id_2 and comp_id_1 == _comp_id_2 and\
                             seq_id_2 == _seq_id_1 and comp_id_2 == _comp_id_1:
                            has_symmetry = True
                            break

                if not has_symmetry:
                    return False

        except Exception as e:

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testDistRestraintAsSymmetry() ++ Error  - %s" % str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__testDistRestraintAsSymmetry() ++ Error  - %s" % str(e))

            return False

        return True

    def __testDihedRestraintAsBackBoneChemShifts(self, lp_data):
        """ Detect whether given dihedral restraints are derived from backbone chemical shifts.
        """

        if lp_data is None:
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']
        file_name = input_source_dic['file_name']

        item_names = self.item_names_in_dh_loop[file_type]
        chain_id_1_name = item_names['chain_id_1']
        chain_id_2_name = item_names['chain_id_2']
        chain_id_3_name = item_names['chain_id_3']
        chain_id_4_name = item_names['chain_id_4']
        seq_id_1_name = item_names['seq_id_1']
        seq_id_2_name = item_names['seq_id_2']
        seq_id_3_name = item_names['seq_id_3']
        seq_id_4_name = item_names['seq_id_4']
        comp_id_1_name = item_names['comp_id_1']
        atom_id_1_name = item_names['atom_id_1']
        atom_id_2_name = item_names['atom_id_2']
        atom_id_3_name = item_names['atom_id_3']
        atom_id_4_name = item_names['atom_id_4']
        angle_type_name = item_names['angle_type']

        dihed_atom_ids = ['N', 'CA', 'C']

        dh_chains = set()
        dh_seq_ids = {}
        cs_chains = set()
        cs_seq_ids = {}

        try:

            for i in lp_data:
                chain_id_1 = i[chain_id_1_name]
                chain_id_2 = i[chain_id_2_name]
                chain_id_3 = i[chain_id_3_name]
                chain_id_4 = i[chain_id_4_name]
                seq_ids = []
                seq_ids.append(i[seq_id_1_name])
                seq_ids.append(i[seq_id_2_name])
                seq_ids.append(i[seq_id_3_name])
                seq_ids.append(i[seq_id_4_name])
                comp_id = i[comp_id_1_name]
                atom_ids = []
                atom_ids.append(i[atom_id_1_name])
                atom_ids.append(i[atom_id_2_name])
                atom_ids.append(i[atom_id_3_name])
                atom_ids.append(i[atom_id_4_name])
                angle_type = i[angle_type_name]

                if angle_type in self.empty_value:
                    continue

                angle_type = angle_type.lower()

                if not angle_type in ['phi', 'psi']:
                    continue

                if chain_id_1 != chain_id_2 or chain_id_2 != chain_id_3 or chain_id_3 != chain_id_4:
                    return False

                polypeptide_like = self.__csStat.getTypeOfCompId(comp_id)[0]

                if not polypeptide_like:
                    return False

                dh_chains.add(chain_id_1)

                seq_id_common = collections.Counter(seq_ids).most_common()

                if len(seq_id_common) != 2 or seq_id_common[0][1] != 3 or seq_id_common[1][1] != 1:
                    return False

                # phi

                if angle_type == 'phi':

                    seq_id_prev = seq_id_common[1][0]

                    if seq_id_common[0][0] != seq_id_prev + 1:
                        return False

                    j = 0
                    if seq_ids[j] == seq_id_prev:
                        if atom_ids[j] != 'C':
                            return False
                        atom_ids.pop(j)
                        if atom_ids != dihed_atom_ids:
                            return False

                # psi

                else:

                    seq_id_next = seq_id_common[1][0]

                    if seq_id_common[0][0] != seq_id_next - 1:
                        return False

                    j = 3
                    if seq_ids[j] == seq_id_next:
                        if atom_ids[j] != 'N':
                            return False
                        atom_ids.pop(j)
                        if atom_ids != dihed_atom_ids:
                            return False

                if type(chain_id_1) is int:
                    chain_id = str(chain_id_1)
                else:
                    chain_id = chain_id_1

                if not chain_id in dh_seq_ids:
                    dh_seq_ids[chain_id] = set()

                dh_seq_ids[chain_id].add(seq_id_common[0][0])

            # check backbone CA atoms

            content_subtype = 'chem_shift'

            if not content_subtype in input_source_dic['content_subtype'].keys():

                err = "Assigned chemical shift loop did not exist in %s file." % file_name

                self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testDihedRestraintAsBackBoneChemShifts() ++ Error  - %s" % err)
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__testDihedRestraintAsBackBoneChemShifts() ++ Error  - %s\n" % err)

                return False

            sf_category = self.sf_categories[file_type][content_subtype]
            lp_category = self.lp_categories[file_type][content_subtype]

            key_items = self.key_items[file_type][content_subtype]
            data_items = self.data_items[file_type][content_subtype]

            item_names = self.item_names_in_cs_loop[file_type]
            chain_id_name = item_names['chain_id']
            seq_id_name = item_names['seq_id']
            atom_id_name = item_names['atom_id']

            for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

                sf_framecode = sf_data.get_tag('sf_framecode')[0]

                if self.report.error.exists(file_name, sf_framecode):
                    continue

                lp_data = next((l['data'] for l in self.__lp_data[content_subtype] if l['sf_framecode'] == sf_framecode), None)

                if lp_data is None:

                    try:

                        lp_data = self.__nefT.check_data(sf_data, lp_category, key_items, data_items, None, None)[0]

                        self.__lp_data[content_subtype].append({'sf_framecode': sf_framecode, 'data': lp_data})

                    except:
                        pass

                if not lp_data is None:

                    for i in lp_data:
                        _chain_id = i[chain_id_name]
                        seq_id = i[seq_id_name]
                        atom_id = i[atom_id_name]

                        if type(_chain_id) is int:
                            chain_id = str(_chain_id)
                        else:
                            chain_id = _chain_id

                        if _chain_id in dh_chains and seq_id in dh_seq_ids[chain_id] and atom_id == 'CA':
                            cs_chains.add(_chain_id)

                            if not chain_id in cs_seq_ids:
                                cs_seq_ids[chain_id] = set()

                            cs_seq_ids[chain_id].add(seq_id)

            if cs_chains != dh_chains:
                return False

            for chain_id in dh_seq_ids.keys():

                if len(cs_seq_ids[chain_id] & dh_seq_ids[chain_id]) < len(dh_seq_ids[chain_id]) * 0.8:
                    return False

        except Exception as e:

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testDihedRestraintAsBackBoneChemShifts() ++ Error  - %s" % str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__testDihedRestraintAsBackBoneChemShifts() ++ Error  - %s" % str(e))

            return False

        return True

    def __testRestraintPotentialSWP(self, content_subtype, lp_data):
        """ Detect square-well-parabolic potential.
        """

        if lp_data is None:
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        try:

            item_names = self.potential_items[file_type][content_subtype]
            lower_limit_name = item_names['lower_limit']
            upper_limit_name = item_names['upper_limit']
            lower_linear_limit_name = item_names['lower_linear_limit']
            upper_linear_limit_name = item_names['upper_linear_limit']

            for i in lp_data:
                if (not i[lower_limit_name] is None) and\
                   (not i[upper_limit_name] is None) and\
                   i[lower_linear_limit_name] is None and\
                   i[upper_linear_limit_name] is None:
                    continue

                else:
                    return False

        except Exception as e:

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testRestraintPotentialSWP() ++ Error  - %s" % str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__testRestraintPotentialSWP() ++ Error  - %s" % str(e))

            return False

        return True

    def __testRestraintPotentialSWPL(self, content_subtype, lp_data):
        """ Detect square-well-parabolic-linear potential.
        """

        if lp_data is None:
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        try:

            item_names = self.potential_items[file_type][content_subtype]
            lower_limit_name = item_names['lower_limit']
            upper_limit_name = item_names['upper_limit']
            lower_linear_limit_name = item_names['lower_linear_limit']
            upper_linear_limit_name = item_names['upper_linear_limit']

            for i in lp_data:
                if (not i[lower_limit_name] is None) and\
                   (not i[upper_limit_name] is None) and\
                   (not i[lower_linear_limit_name] is None) and\
                   (not i[upper_linear_limit_name] is None):
                    continue

                else:
                    return False

        except Exception as e:

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testRestraintPotentialSWPL() ++ Error  - %s" % str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__testRestraintPotentialSWPL() ++ Error  - %s" % str(e))

            return False

        return True

    def __testRestraintPotentialUBP(self, content_subtype, lp_data):
        """ Detect upper-bound-parabolic potential.
        """

        if lp_data is None:
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        try:

            item_names = self.potential_items[file_type][content_subtype]
            lower_limit_name = item_names['lower_limit']
            upper_limit_name = item_names['upper_limit']
            lower_linear_limit_name = item_names['lower_linear_limit']
            upper_linear_limit_name = item_names['upper_linear_limit']

            for i in lp_data:
                if i[lower_limit_name] is None and\
                   (not i[upper_limit_name] is None) and\
                   i[lower_linear_limit_name] is None and\
                   i[upper_linear_limit_name] is None:
                    continue

                else:
                    return False

        except Exception as e:

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testRestraintPotentialUBP() ++ Error  - %s" % str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__testRestraintPotentialUBP() ++ Error  - %s" % str(e))

            return False

        return True

    def __testRestraintPotentialLBP(self, content_subtype, lp_data):
        """ Detect lower-bound-parabolic potential.
        """

        if lp_data is None:
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        try:

            item_names = self.potential_items[file_type][content_subtype]
            lower_limit_name = item_names['lower_limit']
            upper_limit_name = item_names['upper_limit']
            lower_linear_limit_name = item_names['lower_linear_limit']
            upper_linear_limit_name = item_names['upper_linear_limit']

            for i in lp_data:
                if (not i[lower_limit_name] is None) and\
                   i[upper_limit_name] is None and\
                   i[lower_linear_limit_name] is None and\
                   i[upper_linear_limit_name] is None:
                    continue

                else:
                    return False

        except Exception as e:

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testRestraintPotentialLBP() ++ Error  - %s" % str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__testRestraintPotentialLBP() ++ Error  - %s" % str(e))

            return False

        return True

    def __testRestraintPotentialUBPL(self, content_subtype, lp_data):
        """ Detect upper-bound-parabolic-linear potential.
        """

        if lp_data is None:
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        try:

            item_names = self.potential_items[file_type][content_subtype]
            lower_limit_name = item_names['lower_limit']
            upper_limit_name = item_names['upper_limit']
            lower_linear_limit_name = item_names['lower_linear_limit']
            upper_linear_limit_name = item_names['upper_linear_limit']

            for i in lp_data:
                if i[lower_limit_name] is None and\
                   (not i[upper_limit_name] is None) and\
                   i[lower_linear_limit_name] is None and\
                   (not i[upper_linear_limit_name] is None):
                    continue

                else:
                    return False

        except Exception as e:

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testRestraintPotentialUBPL() ++ Error  - %s" % str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__testRestraintPotentialUBPL() ++ Error  - %s" % str(e))

            return False

        return True

    def __testRestraintPotentialLBPL(self, content_subtype, lp_data):
        """ Detect lower-bound-parabolic-linear potential.
        """

        if lp_data is None:
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        try:

            item_names = self.potential_items[file_type][content_subtype]
            lower_limit_name = item_names['lower_limit']
            upper_limit_name = item_names['upper_limit']
            lower_linear_limit_name = item_names['lower_linear_limit']
            upper_linear_limit_name = item_names['upper_linear_limit']

            for i in lp_data:
                if (not i[lower_limit_name] is None) and\
                   i[upper_limit_name] is None and\
                   (not i[lower_linear_limit_name] is None) and\
                   i[upper_linear_limit_name] is None:
                    continue

                else:
                    return False

        except Exception as e:

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testRestraintPotentialLBPL() ++ Error  - %s" % str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__testRestraintPotentialLBPL() ++ Error  - %s" % str(e))

            return False

        return True

    def __testRestraintPonentialLHorP(self, content_subtype, lp_data):
        """ Detect log-harmonic or parabolic potential.
        """

        if lp_data is None:
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        try:

            item_names = self.potential_items[file_type][content_subtype]
            target_value_name = item_names['target_value']
            lower_limit_name = item_names['lower_limit']
            upper_limit_name = item_names['upper_limit']
            lower_linear_limit_name = item_names['lower_linear_limit']
            upper_linear_limit_name = item_names['upper_linear_limit']

            for i in lp_data:
                if (not i[target_value_name] is None) and\
                   i[lower_limit_name] is None and\
                   i[upper_limit_name] is None and\
                   i[lower_linear_limit_name] is None and\
                   i[upper_linear_limit_name] is None:
                    continue

                else:
                    return False

        except Exception as e:

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testRestraintPotentialLHorP() ++ Error  - %s" % str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__testRestraintPotentialLHorP() ++ Error  - %s" % str(e))

            return False

        return True

    def __fixBadAmbiguityCode(self):
        """ Fix bad ambiguity code if possible.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']
        file_name = input_source_dic['file_name']

        # NEF file has no ambiguity code
        if file_type == 'nef':
            return True

        warnings = self.report.warning.getValueList('bad_ambiguity_code', file_name)

        if warnings is None:
            return True

        for w in warnings:

            if not "the same residue was not found." in w['description']:
                continue

            if self.__star_data_type == "Entry" or self.__star_data_type == "Saveframe":

                if not 'sf_framecode' in w:

                    err = "Could not specify 'sf_framecode' in NMR data processing report."

                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__fixBadAmbiguityCode() ++ Error  - %s" % err)
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__fixBadAmbiguityCode() ++ Error  - %s\n" % err)

                elif not 'category' in w:

                    err = "Could not specify 'category' in NMR data processing report."

                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__fixBadAmbiguityCode() ++ Error  - %s" % err)
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__fixBadAmbiguityCode() ++ Error  - %s\n" % err)

                elif not 'row_location' in w:

                    err = "Could not specify 'row_location' in NMR data processing report."

                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__fixBadAmbiguityCode() ++ Error  - %s" % err)
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__fixBadAmbiguityCode() ++ Error  - %s\n" % err)

                else:

                    sf_data = self.__star_data.get_saveframe_by_name(w['sf_framecode'])

                    if sf_data is None:

                        err = "Could not specify saveframe %s unexpectedly in %s file." % (w['sf_framecode'], file_name)

                        self.report.error.appendDescription('internal_error', "+NmrDpUtility.__fixBadAmbiguityCode() ++ Error  - %s" % err)
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__fixBadAmbiguityCode() ++ Error  - %s\n" % err)

                    else:

                        description = w['description'].split(' ')

                        itName = description[0]
                        itVal = description[1]

                        lp_data = sf_data.get_loop_by_category(w['category'])

                        if not itName in lp_data.tags:

                            err = "Could not find loop tag %s in %s category, %s saveframe, %s file." % (itName, w['category'], w['sf_framecode'], file_name)

                            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__fixBadAmbiguityCode() ++ Error  - %s" % err)
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__fixBadAmbiguityCode() ++ Error  - %s\n" % err)

                        else:
                            itCol = lp_data.tags.index(itName)

                            itColVal = {str(itCol): itVal}

                            has_loop_tag = True

                            for k, v in w['row_location'].items():

                                if k in lp_data.tags:
                                    itColVal[str(lp_data.tags.index(k))] = v

                                else:

                                    err = "Could not find loop tag %s in %s category, %s saveframe, %s file." % (k, w['category'], w['sf_framecode'], file_name)

                                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__fixBadAmbiguityCode() ++ Error  - %s" % err)
                                    self.report.setError()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__fixBadAmbiguityCode() ++ Error  - %s\n" % err)

                                    has_loop_tag = False

                            if not has_loop_tag:
                                continue

                            for row in lp_data.data:

                                exist = True

                                for k, v in itColVal.items():

                                    if row[int(k)] != v:
                                        exist = False
                                        break

                                if exist:
                                    row[itCol] = 1
                                    break

            else:

                err = "Unexpected PyNMRSTAR object type %s found about %s file." % (self.__star_data_type, file_name)

                self.report.error.appendDescription('internal_error', "+NmrDpUtility.__fixBadAmbiguityCode() ++ Error  - %s" % err)
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__fixBadAmbiguityCode() ++ Error  - %s\n" % err)

        return True

    def __resetCapitalStringInLoop(self):
        """ Reset capital string values (chain_id, comp_id, atom_id) in loops depending on file type.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        if input_source_dic['content_subtype'] is None:
            return False

        for content_subtype in input_source_dic['content_subtype'].keys():

            if content_subtype == 'entry_info':
                continue

            sf_category = self.sf_categories[file_type][content_subtype]
            lp_category = self.lp_categories[file_type][content_subtype]

            for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

                if content_subtype == 'spectral_peak':

                    try:

                        _num_dim = sf_data.get_tag(self.num_dim_items[file_type])[0]
                        num_dim = int(_num_dim)

                        if not num_dim in range(1, self.lim_num_dim):
                            raise ValueError()

                    except ValueError: # raised error already at __testIndexConsistency()
                        continue

                    max_dim = num_dim + 1

                    key_items = []
                    for dim in range(1, max_dim):
                        for k in self.pk_key_items[file_type]:
                            _k = copy.copy(k)
                            if '%s' in k['name']:
                               _k['name'] = k['name'] % dim
                            key_items.append(_k)

                    data_items = []
                    for d in self.data_items[file_type][content_subtype]:
                        data_items.append(d)
                    for dim in range(1, max_dim):
                        for d in self.pk_data_items[file_type]:
                            _d = copy.copy(d)
                            if '%s' in d['name']:
                                _d['name'] = d['name'] % dim
                            data_items.append(_d)

                    if max_dim < self.lim_num_dim:
                        disallowed_tags = []
                        for dim in range(max_dim, self.lim_num_dim):
                            for t in self.spectral_peak_disallowed_tags[file_type]:
                                if '%s' in t:
                                    t = t % dim
                                disallowed_tags.append(t)

                else:

                    key_items = self.key_items[file_type][content_subtype]
                    data_items = self.data_items[file_type][content_subtype]

                lp_data = sf_data.get_loop_by_category(lp_category)

                if file_type == 'nef':
                    key_names = [k['name'] for k in key_items if k['name'].startswith('chain_code') or k['name'].startswith('residue_name') or k['name'].startswith('atom_name') or k['name'] == 'element']
                else:
                    key_names = [k['name'] for k in key_items if k['name'].startswith('Comp_ID') or k['name'].startswith('Atom_ID') or k['name'] == 'Atom_type']

                for itName in key_names:

                    if itName in lp_data.tags:

                        itCol = lp_data.tags.index(itName)

                        for row in lp_data.data:

                            val = row[itCol]

                            if val is self.empty_value:
                                continue

                            if file_type == 'nef' and itName.startswith('atom_name') and ('x' in val or 'y' in val):
                                continue

                            row[itCol] = val.upper()

                if file_type == 'nef':
                    data_names = [d['name'] for d in data_items if d['name'].startswith('chain_code') or d['name'].startswith('residue_name') or d['name'].startswith('atom_name') or d['name'] == 'element']
                else:
                    data_names = [d['name'] for d in data_items if d['name'].startswith('Comp_ID') or d['name'].startswith('Atom_ID') or d['name'] == 'Atom_type']

                for itName in data_names:

                    if itName in lp_data.tags:

                        itCol = lp_data.tags.index(itName)

                        for row in lp_data.data:

                            val = row[itCol]

                            if val is self.empty_value:
                                continue

                            if file_type == 'nef' and itName.startswith('atom_name') and ('x' in val or 'y' in val):
                                continue

                            row[itCol] = val.upper()

        return True

    def __resetBoolValueInLoop(self):
        """ Reset bool values in loops depending on file type.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        yes_value = 'true' if file_type == 'nef' else 'yes'
        no_value = 'false' if file_type == 'nef' else 'no'

        if input_source_dic['content_subtype'] is None:
            return False

        for content_subtype in input_source_dic['content_subtype'].keys():

            if content_subtype == 'entry_info':
                continue

            sf_category = self.sf_categories[file_type][content_subtype]
            lp_category = self.lp_categories[file_type][content_subtype]

            for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

                if content_subtype == 'spectral_peak':

                    try:

                        _num_dim = sf_data.get_tag(self.num_dim_items[file_type])[0]
                        num_dim = int(_num_dim)

                        if not num_dim in range(1, self.lim_num_dim):
                            raise ValueError()

                    except ValueError: # raised error already at __testIndexConsistency()
                        continue

                    max_dim = num_dim + 1

                    key_items = []
                    for dim in range(1, max_dim):
                        for k in self.pk_key_items[file_type]:
                            _k = copy.copy(k)
                            if '%s' in k['name']:
                               _k['name'] = k['name'] % dim
                            key_items.append(_k)

                    data_items = []
                    for d in self.data_items[file_type][content_subtype]:
                        data_items.append(d)
                    for dim in range(1, max_dim):
                        for d in self.pk_data_items[file_type]:
                            _d = copy.copy(d)
                            if '%s' in d['name']:
                                _d['name'] = d['name'] % dim
                            data_items.append(_d)

                    if max_dim < self.lim_num_dim:
                        disallowed_tags = []
                        for dim in range(max_dim, self.lim_num_dim):
                            for t in self.spectral_peak_disallowed_tags[file_type]:
                                if '%s' in t:
                                    t = t % dim
                                disallowed_tags.append(t)

                else:

                    key_items = self.key_items[file_type][content_subtype]
                    data_items = self.data_items[file_type][content_subtype]

                has_bool_key = False

                if not key_items is None:
                    has_bool_key = next((k['type'] == 'bool' for k in key_items if k['type'] == 'bool'), False)

                has_bool_data = False

                if not data_items is None:
                    has_bool_data = next((d['type'] == 'bool' for d in data_items if d['type'] == 'bool'), False)

                if has_bool_key or has_bool_data:

                    lp_data = sf_data.get_loop_by_category(lp_category)

                    if has_bool_key:

                        for itName in [k['name'] for k in key_items if k['type'] == 'bool']:

                            if itName in lp_data.tags:

                                itCol = lp_data.tags.index(itName)

                                for row in lp_data.data:

                                    val = row[itCol]

                                    if val is self.empty_value:
                                        continue

                                    if val.lower() in self.true_value:
                                        row[itCol] = yes_value
                                    else:
                                        row[itCol] = no_value

                    if has_bool_data:

                        for itName in [d['name'] for d in data_items if d['type'] == 'bool']:

                            if itName in lp_data.tags:

                                itCol = lp_data.tags.index(itName)

                                for row in lp_data.data:

                                    val = row[itCol]

                                    if val is self.empty_value:
                                        continue

                                    if val.lower() in self.true_value:
                                        row[itCol] = yes_value
                                    else:
                                        row[itCol] = no_value

        return True

    def __resetBoolValueInAuxLoop(self):
        """ Reset bool values in auxiliary loops depending on file type.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        yes_value = 'true' if file_type == 'nef' else 'yes'
        no_value = 'false' if file_type == 'nef' else 'no'

        if input_source_dic['content_subtype'] is None:
            return False

        for content_subtype in input_source_dic['content_subtype'].keys():

            if content_subtype == 'entry_info':
                continue

            sf_category = self.sf_categories[file_type][content_subtype]

            for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

                sf_framecode = sf_data.get_tag('sf_framecode')[0]

                for loop in sf_data.loops:

                    lp_category = loop.category

                    # main content of loop has been processed in __resetBoolValueInLoop()
                    if lp_category in self.lp_categories[file_type][content_subtype]:
                        continue

                    elif lp_category in self.aux_lp_categories[file_type][content_subtype]:

                        key_items = self.aux_key_items[file_type][content_subtype][lp_category]
                        data_items = self.aux_data_items[file_type][content_subtype][lp_category]

                        has_bool_key = False

                        if not key_items is None:
                            has_bool_key = next((k['type'] == 'bool' for k in key_items if k['type'] == 'bool'), False)

                        has_bool_data = False

                        if not data_items is None:
                            has_bool_data = next((d['type'] == 'bool' for d in data_items if d['type'] == 'bool'), False)

                        if has_bool_key or has_bool_data:

                            lp_data = sf_data.get_loop_by_category(lp_category)

                            if has_bool_key:

                                for itName in [k['name'] for k in key_items if k['type'] == 'bool']:

                                    if itName in lp_data.tags:

                                        itCol = lp_data.tags.index(itName)

                                        for row in lp_data.data:

                                            val = row[itCol]

                                            if val is self.empty_value:
                                                continue

                                            if val.lower() in self.true_value:
                                                row[itCol] = yes_value
                                            else:
                                                row[itCol] = no_value

                            if has_bool_data:

                                for itName in [d['name'] for d in data_items if d['type'] == 'bool']:

                                    if itName in lp_data.tags:

                                        itCol = lp_data.tags.index(itName)

                                        for row in lp_data.data:

                                            val = row[itCol]

                                            if val is self.empty_value:
                                                continue

                                            if val.lower() in self.true_value:
                                                row[itCol] = yes_value
                                            else:
                                                row[itCol] = no_value

        return True

    def __appendParentSfTag(self):
        """ Append parent tag in saveframe if not exists.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        if file_type == 'nef':
            return True

        if input_source_dic['content_subtype'] is None:
            return False

        for content_subtype in input_source_dic['content_subtype'].keys():

            if content_subtype == 'entry_info':
                continue

            sf_category = self.sf_categories[file_type][content_subtype]
            lp_category = self.lp_categories[file_type][content_subtype]

            data_items = self.data_items[file_type][content_subtype]

            list_id_tag_in_lp = None

            if not data_items is None:
                list_id_tag_in_lp = next((d for d in data_items if d['type'] == 'pointer-index'), None)

            if not list_id_tag_in_lp is None:

                for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

                    sf_framecode = sf_data.get_tag('sf_framecode')[0]

                    warn_desc = self.report.warning.getDescription('duplicated_index', file_name, sf_framecode)

                    if not warn_desc is None and warn_desc.split(' ')[0] == self.sf_tag_prefixes[file_type][content_subtype].lstrip('_') + '.ID':
                        continue

                    lp_data = sf_data.get_loop_by_category(lp_category)

                    itName = list_id_tag_in_lp['name']

                    if itName in lp_data.tags:

                        itCol = lp_data.tags.index(itName)

                        list_ids = []

                        for row in lp_data.data:

                            val = row[itCol]

                            if val is self.empty_value:
                                continue

                            list_ids.append(val)

                        list_id = collections.Counter(list_ids).most_common()[0][0]

                        if len(sf_data.get_tag('ID')) == 0:
                            sf_data.add_tag('ID', list_id)

                        else:
                            itCol = tagNames.index('ID')
                            sf_data.tags[itCol][1] = list_id

        return True

    def __addUnnamedEntryId(self, entry_id='UNNAMED', insert_entry_id_to_loops=True):
        """ Add UNNAMED entry id.
        """

        if 'entry_id' in self.__inputParamDict and not self.__inputParamDict['entry_id'] is None:
            entry_id = self.__inputParamDict['entry_id']

        if 'insert_entry_id_to_loops' in self.__inputParamDict and not self.__inputParamDict['insert_entry_id_to_loops'] is None:
            if type(self.__inputParamDict['insert_entry_id_to_loops']) is bool:
                insert_entry_id_to_loops = self.__inputParamDict['insert_entry_id_to_loops']
            else:
                insert_entry_id_to_loops = self.__inputParamDict['insert_entry_id_to_loops'] in self.true_value

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        # update datablock name

        if self.__star_data_type == 'Entry':
            self.__star_data.entry_id = entry_id + self.content_type[file_type]

        if file_type == 'nef':
            return True

        if input_source_dic['content_subtype'] is None:
            return False

        self.__sortCSLoop()

        if self.__updateAtomChemShiftId():
            self.__updateAmbiguousAtomChemShift(entry_id, insert_entry_id_to_loops)

        for content_subtype in input_source_dic['content_subtype'].keys():

            sf_category = self.sf_categories[file_type][content_subtype]
            lp_category = self.lp_categories[file_type][content_subtype]

            for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

                entryIdTag = 'ID' if content_subtype == 'entry_info' else 'Entry_ID'

                if entryIdTag in self.sf_allowed_tags[file_type][content_subtype]:

                    if len(sf_data.get_tag(entryIdTag)) == 0:
                            sf_data.add_tag(entryIdTag, entry_id)

                    else:
                        itCol = tagNames.index(entryIdTag)
                        sf_data.tags[itCol][1] = entry_id

                if insert_entry_id_to_loops:

                    entryIdTag = 'Entry_ID'

                    lp_data = sf_data.get_loop_by_category(lp_category)

                    if not lp_data is None:

                        if entryIdTag in self.allowed_tags[file_type][content_subtype]:

                            if entryIdTag in lp_data.tags:

                                itCol = lp_data.tags.index(entryIdTag)

                                for row in lp_data.data:
                                    row[itCol] = entry_id

                            else:

                                for row in lp_data.data:
                                    row.append(entry_id)

                                lp_data.add_tag(entryIdTag)

                    for loop in sf_data.loops:

                        lp_category = loop.category

                        if lp_category in self.lp_categories[file_type][content_subtype]:
                            continue

                        elif lp_category in self.aux_lp_categories[file_type][content_subtype]:

                            lp_data = sf_data.get_loop_by_category(lp_category)

                            if entryIdTag in self.aux_allowed_tags[file_type][content_subtype][lp_category]:

                                if entryIdTag in lp_data.tags:

                                    itCol = lp_data.tags.index(entryIdTag)

                                    for row in lp_data.data:
                                        row[itCol] = entry_id

                                else:

                                    for row in lp_data.data:
                                        row.append(entry_id)

                                    lp_data.add_tag(entryIdTag)

        return True

    def __sortCSLoop(self):
        """ Sort assigned chemical shift loop if required.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        content_subtype = 'chem_shift'

        if not content_subtype in input_source_dic['content_subtype'].keys():

            err = "Assigned chemical shift loop did not exist in %s file." % file_name

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__sortCSLoop() ++ Error  - %s" % err)
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__sortCSLoop() ++ Error  - %s\n" % err)

            return False

        sf_category = self.sf_categories[file_type][content_subtype]
        lp_category = self.lp_categories[file_type][content_subtype]

        key_items = self.key_items[file_type][content_subtype]
        data_items = self.data_items[file_type][content_subtype]

        item_names = self.item_names_in_cs_loop[file_type]
        chain_id_name = item_names['chain_id']
        seq_id_name = item_names['seq_id']
        atom_id_name = item_names['atom_id']

        for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

            sf_framecode = sf_data.get_tag('sf_framecode')[0]

            if self.report.error.exists(file_name, sf_framecode):
                continue

            lp_data = next((l['data'] for l in self.__lp_data[content_subtype] if l['sf_framecode'] == sf_framecode), None)

            if lp_data is None:

                try:

                    lp_data = self.__nefT.check_data(sf_data, lp_category, key_items, data_items, None, None)[0]

                    self.__lp_data[content_subtype].append({'sf_framecode': sf_framecode, 'data': lp_data})

                except:
                    pass

            if not lp_data is None:

                atoms = []

                id = 0

                for i in lp_data:
                    chain_id = i[chain_id_name]
                    seq_id = i[seq_id_name]
                    atom_id = i[atom_id_name]

                    atoms.append('{:<4}:{:04d}:{:<8}:{:06d}'.format(chain_id, seq_id, atom_id, id))

                    id += 1

                sorted_atoms = sorted(atoms)

                sorted_id = []

                for j in sorted_atoms:
                    sorted_id.append(int(j.split(':')[3]))

                if sorted_id != range(id):

                    lp_data = sf_data.get_loop_by_category(lp_category)

                    new_lp_data = pynmrstar.Loop.from_scratch(lp_category)

                    for tag in lp_data.tags:
                        new_lp_data.add_tag(lp_category + '.' + tag)

                    for i in sorted_id:
                        new_lp_data.add_data(lp_data[i])

                    del sf_data[lp_data]

                    sf_data.add_loop(new_lp_data)

        return True

    def __updateAtomChemShiftId(self):
        """ Update _Atom_chem_shift.ID.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        if file_type == 'nef':
            return False

        content_subtype = 'chem_shift'

        if not content_subtype in input_source_dic['content_subtype'].keys():

            err = "Assigned chemical shift loop did not exist in %s file." % file_name

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__updateAtomChemShiftId() ++ Error  - %s" % err)
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__updateAtomChemShiftId() ++ Error  - %s\n" % err)

            return False

        sf_category = self.sf_categories[file_type][content_subtype]
        lp_category = self.lp_categories[file_type][content_subtype]

        for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

            sf_framecode = sf_data.get_tag('sf_framecode')[0]

            if self.report.error.exists(file_name, sf_framecode):
                continue

            lp_data = sf_data.get_loop_by_category(lp_category)

            ambig_set_id_name = 'Ambiguity_set_ID'

            ambig_set_id_col = lp_data.tags.index(ambig_set_id_name)

            ambig_set_id_dic = {}

            if ambig_set_id_name in lp_data.tags:

                ambig_set_ids = []

                for i in lp_data:

                    ambig_set_id = i[ambig_set_id_col]

                    if not ambig_set_id in self.empty_value:
                        ambig_set_ids.append(str(ambig_set_id))

                if len(ambig_set_ids) > 0:

                    id = 1

                    for ambig_set_id in ambig_set_ids:

                        if ambig_set_id in ambig_set_id_dic:
                            continue

                        ambig_set_id_dic[ambig_set_id] = str(id)

                        id += 1

            disordered_ambig_set_id = False

            for k, v in ambig_set_id_dic.items():
                if k != v:
                    disordered_ambig_set_id = True
                    break

            if disordered_ambig_set_id:

                for i in lp_data:
                    ambig_set_id = i[ambig_set_id_col]

                    if not ambig_set_id in self.empty_value:
                        i[ambig_set_id_col] = int(ambig_set_id_dic[str(ambig_set_id)])

            if 'ID' in lp_data.tags:
                lp_data.renumber_rows('ID')

            else:
                new_lp_data = pynmrstar.Loop.from_scratch(lp_category)

                new_lp_data.add_tag(lp_category + '.ID')

                for tag in lp_data.tags:
                    new_lp_data.add_tag(lp_category + '.' + tag)

                id = 1

                for i in lp_data:
                    new_lp_data.add_data([str(id)] + i)
                    id += 1

                del sf_data[lp_data]

                sf_data.add_loop(new_lp_data)

        return True

    def __updateAmbiguousAtomChemShift(self, entry_id='UNNAMED', insert_entry_id_to_loops=True):
        """ Update _Ambiguous_atom_chem_shift loops.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        if file_type == 'nef':
            return False

        content_subtype = 'chem_shift'

        if not content_subtype in input_source_dic['content_subtype'].keys():

            err = "Assigned chemical shift loop did not exist in %s file." % file_name

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__updateAmbiguousAtomChemShift() ++ Error  - %s" % err)
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__updateAmbiguousAtomChemShift() ++ Error  - %s\n" % err)

            return False

        sf_category = self.sf_categories[file_type][content_subtype]
        lp_category = self.lp_categories[file_type][content_subtype]

        key_items = self.key_items[file_type][content_subtype]
        data_items = self.data_items[file_type][content_subtype]

        for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

            sf_framecode = sf_data.get_tag('sf_framecode')[0]

            if self.report.error.exists(file_name, sf_framecode):
                continue

            lp_data = next((l['data'] for l in self.__lp_data[content_subtype] if l['sf_framecode'] == sf_framecode), None)

            if lp_data is None:

                try:

                    lp_data = self.__nefT.check_data(sf_data, lp_category, key_items, data_items, None, None)[0]

                    self.__lp_data[content_subtype].append({'sf_framecode': sf_framecode, 'data': lp_data})

                except:
                    pass

            if not lp_data is None:

                ambig_set_id_name = 'Ambiguity_set_ID'

                has_ambig_set_id = False

                for i in lp_data:

                    if ambig_set_id_name in i and not i[ambig_set_id_name] in self.empty_value:
                        has_ambig_set_id = True
                        break

                if has_ambig_set_id:

                    aux_lp_cateogry = '_Ambiguous_atom_chem_shift'

                    for aux_loop in sf_data.loops:

                        if aux_loop.category == aux_lp_cateogry:
                            del sf_data[aux_loop]
                            break

                    aux_lp_data = pynmrstar.Loop.from_scratch(aux_lp_cateogry)
                    aux_lp_data.add_tag(aux_lp_cateogry + '.Ambiguous_shift_set_ID')
                    aux_lp_data.add_tag(aux_lp_cateogry + '.Assigned_chem_shift_list_ID')
                    aux_lp_data.add_tag(aux_lp_cateogry + '.Atom_chem_shift_ID')

                    if insert_entry_id_to_loops:
                        aux_lp_data.add_tag(aux_lp_cateogry + '.Entry_ID')

                    id = 1

                    for i in lp_data:

                        if ambig_set_id_name in i and not i[ambig_set_id_name] in self.empty_value:

                            row = []

                            row.append(i[ambig_set_id_name])
                            row.append(i['Assigned_chem_shift_list_ID'])
                            row.append(id)

                            if insert_entry_id_to_loops:
                                row.append(entry_id)

                            aux_lp_data.add_data(row)

                        id += 1

                    sf_data.add_loop(aux_lp_data)

        return True

    def __depositNmrData(self):
        """ Deposit next NMR unified data file.
        """

        if self.__dstPath is None:

            err = "Not found destination file path."

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__depositNmrData() ++ Error  - %s" % err)
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__depositNmrData() ++ Error  - %s\n" % err)

            return False

        if self.__star_data is None:
            return False

        self.__star_data.write_to_file(self.__dstPath)

        return not self.report.isError()

    def __initializeDpReportForNext(self):
        """ Initialize NMR data processing report using the next version of NMR unified data.
        """

        return self.__initializeDpReport(srcPath=self.__dstPath)

    def __validateInputSourceForNext(self):
        """ Validate the next version of NMR unified data as primary input source.
        """

        return self.__validateInputSource(srcPath=self.__dstPath)

    def __translateNef2Str(self):
        """ Translate NEF to NMR-STAR V3.2 file.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = os.path.basename(self.__dstPath)
        file_type = input_source_dic['file_type']

        out_file_path = self.__outputParamDict['nmr-star_file_path']

        if 'nmr-star_file_path' in self.__outputParamDict:

            try:

                is_valid, json_dumps = self.__nefT.nef_to_nmrstar(self.__dstPath, out_file_path)

            except Exception as e:

                err = "%s is invalid %s file." % (file_name, self.readable_file_type[file_type])
                if not 'No such file or directory' in str(e):
                    err += ' ' + str(e)

                self.report.error.appendDescription('format_issue', {'file_name': file_name, 'description': err})
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__translateNef2Str() ++ Error  - %s\n" % err)

                if os.path.exists(out_file_path):
                    os.remove(out_file_path)

                return False

            if is_valid:
                return True

            else:

                message = json.loads(json_dumps)

                err = "%s is invalid %s file." % (file_name, self.readable_file_type[file_type])

                if len(message['error']) > 0:
                    for err_message in message['error']:
                        if not 'No such file or directory' in err_message:
                            err += ' ' + err_message

                self.report.error.appendDescription('format_issue', {'file_name': file_name, 'description': err})
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__translateNef2Str() ++ Error  - %s\n" % err)

                if os.path.exists(out_file_path):
                    os.remove(out_file_path)

                return False

        else:
            logging.error("+NmrDpUtility.__translateNef2Str() ++ Error  - Could not find 'nmr-star_file_path' output parameter.")
            raise KeyError("+NmrDpUtility.__translateNef2Str() ++ Error  - Could not find 'nmr-star_file_path' output parameter.")

        return False

    def __initResourceForNef2Str(self):
        """ Initialize resources for the translated NMR-STAR V3.2 file.
        """

        try:

            self.__srcPath = self.__outputParamDict['nmr-star_file_path']
            self.__dstPath = self.__srcPath
            self.__logPath = self.__outputParamDict['report_file_path']
            self.addInput('report_file_path', self.__logPath, type='file')
            self.__op = 'nmr-star-consistency-check'

            # reset cache dictionaries

            for content_subtype in self.__lp_data.keys():
                self.__lp_data[content_subtype] = []

            for content_subtype in self.__aux_data.keys():
                self.__aux_data[content_subtype] = []

            return True

        except:
            logging.error("+NmrDpUtility.__initReousrceForNef2Str() ++ Error  - Could not find 'nmr-star_file_path' or 'report_file_path' output parameter.")
            raise KeyError("+NmrDpUtility.__initReousrceForNef2Str() ++ Error  - Could not find 'nmr-star_file_path' or 'report_file_path' output parameter.")

        return False

if __name__ == '__main__':
    dp = NmrDpUtility()
