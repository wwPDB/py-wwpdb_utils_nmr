##
# File: NmrDpUtility.py
# Date: 23-May-2019
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

from wwpdb.utils.nmr.NEFTranslator.NEFTranslator import NEFTranslator
from wwpdb.utils.nmr.NmrDpReport import NmrDpReport
from wwpdb.utils.align.alignlib import PairwiseAlign

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
                                                      self.__extractPolymerSequenceInLoop,
                                                      self.__testSequenceConsistency,
                                                      self.__extractCommonPolymerSequence,
                                                      self.__extractNonStandardResidue,
                                                      self.__appendPolymerSequenceAlignment,
                                                      self.__testAtomNomenclature,
                                                      self.__testAtomTypeOfCSLoop,
                                                      self.__testAmbiguityCodeOfCSLoop,
                                                      self.__testDuplicatedIndex,
                                                      self.__testDataConsistencyInLoop,
                                                      self.__testParentChildRelation] }
        """
                                }
                                                      self.__testAnomalousData,
                                                      self.__testSaspiciousData,
                                                      self__calculateStatistics],
                                'nmr-consistency-check': [self.__appendInputResource,
                                                          self.__retrieveDpReport,
                                                          self.__extractCoordPolymerSequence,
                                                          self.__alignCoordPolymerSequence,
                                                          self.__testCoordSequenceConsistency,
                                                          self.__testCoordAtomNomeclature],
                                'nmr-nef2star-deposit':  [self.__appendInputResource,
                                                          self.__retrieveDpReport,
                                                          self.__resolveNefMinorIssue,
                                                          self.__depositNef2Star],
                                'nmr-star2star-deposit': [self.__appendInputResource,
                                                          self.__retrieveDpReport,
                                                          self.__resolveStarMinorIssue,
                                                          self.__depositStar2Star]
                                }
        """
        # data processing report
        self.report = None

        # NEFTranslator
        self.nef_translator = None

        # PyNMRSTAR data
        self.__star_data = None

        # NMR content types
        self.nmr_content_subtypes = ('poly_seq', 'chem_shift', 'dist_restraint', 'dihed_restraint', 'rdc_restraint', 'spectral_peak')

        # readable file type
        self.readable_file_type = {'nef': 'NEF (NMR Exchange Format)',
                                   'nmr-star': 'NMR-STAR V3.2',
                                   'pdbx': 'PDBx/mmCIF',
                                   'unknown': 'unknown'
                                   }

        # atom isotopes
        self.atom_isotopes = {'H': {1, 2, 3},
                              'C': {13},
                              'N': {15, 14},
                              'O': {17},
                              'P': {31},
                              'S': {33},
                              'F': {19},
                              'CD': {113, 111},
                              'CA': {43}
                              }

        # ambiguity codes
        self.bmrb_ambiguity_codes = (1, 2, 3, 4, 5, 6, 9)

        isotope_nums = []
        for i in self.atom_isotopes.values():
            isotope_nums.extend(list(i))

        # saveframe categories
        self.sf_categories = {'nef': {'poly_seq': 'nef_molecular_system',
                                      'chem_shift': 'nef_chemical_shift_list',
                                      'dist_restraint': 'nef_distance_restraint_list',
                                      'dihed_restraint': 'nef_dihedral_restraint_list',
                                      'rdc_restraint': 'nef_rdc_restraint_list',
                                      'spectral_peak': 'nef_nmr_spectrum'
                                      },
                              'nmr-star': {'poly_seq': 'assembly',
                                           'chem_shift': 'assigned_chemical_shifts',
                                           'dist_restraint': 'general_distance_constraints',
                                           'dihed_restraint': 'torsion_angle_constraints',
                                           'rdc_restraint': 'RDC_constraints',
                                           'spectral_peak': 'spectral_peak_list'
                                           }
                              }

        # loop categories
        self.lp_categories = {'nef': {'poly_seq': '_nef_sequence',
                                      'chem_shift': '_nef_chemical_shift',
                                      'dist_restraint': '_nef_distance_restraint',
                                      'dihed_restraint': '_nef_dihedral_restraint',
                                      'rdc_restraint': '_nef_rdc_restraint',
                                      'spectral_peak': '_nef_peak'
                                      },
                              'nmr-star': {'poly_seq': '_Chem_comp_assembly',
                                           'chem_shift': '_Atom_chem_shift',
                                           'dist_restraint': '_Gen_dist_constraint',
                                           'dihed_restraint': '_Torsion_angle_constraint',
                                           'rdc_restraint': '_RDC_constraint',
                                           'spectral_peak': '_Peak_row_format'
                                           }
                              }

        # allowed chem shift range
        self.chem_shift_range = {'min_exclusive': -300.0, 'max_exclusive': 300.0}

        # allowed distance range
        self.dist_restraint_range = {'min_exclusive': 1.0, 'max_exclusive': 10.0}

        # allowed dihed range
        self.dihed_restraint_range = {'min_exclusive': -200.0, 'max_exclusive': 200.0}

        # allowed rdc range
        self.rdc_restraint_range = {'min_exclusive': -50.0, 'max_exclusive': 50.0}

        # index tags
        self.index_tags = {'nef': {'poly_seq': 'index',
                                   'chem_shift': None,
                                   'dist_restraint': 'index',
                                   'dihed_restraint': 'index',
                                   'rdc_restraint': 'index',
                                   'spectral_peak': 'index'
                                   },
                           'nmr-star': {'poly_seq': None,
                                        'chem_shift': None,
                                        'dist_restraint': 'Index_ID',
                                        'dihed_restraint': 'Index_ID',
                                        'rdc_restraint': 'Index_ID',
                                        'spectral_peak': 'Index_ID'
                                        }
                         }

        # key_items
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
                                       }
                          }

        # limit of spectral peak dimensions
        self.spectral_peak_lim_dim = 16

        # key items for spectral peak
        self.spectral_peak_key_items = {'nef': [{'name': 'position_%s', 'type': 'range-float',
                                                 'range': self.chem_shift_range}
                                                 ],
                                        'nmr-star': [{'name': 'Position_%s', 'type': 'range-float',
                                                 'range': self.chem_shift_range}
                                                 ]
                                        }

        # data items
        self.data_items = {'nef': {'poly_seq': [{'name': 'linking', 'type': 'enum', 'mandatory': False,
                                                 'enum': ('start', 'end', 'middle', 'cyclic', 'break', 'single', 'dummy')},
                                                {'name': 'residue_variant', 'type': 'str', 'mandatory': False},
                                                {'name': 'cis_peptide', 'type': 'bool', 'mandatory': False}
                                                ],
                                   'chem_shift': [{'name': 'value', 'type': 'range-float', 'mandatory': True,
                                                   'range': self.chem_shift_range},
                                                  {'name': 'value_uncertainty', 'type': 'positive-float', 'mandatory': False},
                                                  {'name': 'element', 'type': 'enum', 'mandatory': True,
                                                   'enum': set(self.atom_isotopes.keys())},
                                                  {'name': 'isotope_number', 'type': 'enum-int', 'mandatory': True,
                                                   'enum': set(isotope_nums)}
                                                  ],
                                   'dist_restraint': [{'name': 'index', 'type':'index-int', 'mandatory': True},
                                                      {'name': 'restraint_id', 'type':'positive-int', 'mandatory': True},
                                                      {'name': 'restraint_combination_id', 'type':'positive-int', 'mandatory': False},
                                                      {'name': 'weight', 'type':'positive-float', 'mandatory': True,
                                                       'enforce-non-zero': True},
                                                      {'name': 'target_value', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                       'range': self.dist_restraint_range,
                                                       'group': {'member-with': ['lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit'],
                                                                 'coexist-with': None,
                                                                 'smaller-than': ['lower_limit', 'lower_linear_limit'],
                                                                 'larger-than': ['upper_limit', 'upper_linear_limit']}},
                                                      {'name': 'target_value_uncertainty', 'type':'positive-float', 'mandatory': False},
                                                      {'name': 'lower_linear_limit', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                       'range': self.dist_restraint_range,
                                                       'group': {'member-with': ['target_value', 'lower_limit', 'upper_limit', 'upper_linear_limit'],
                                                                 'coexist-with': ['lower_limit', 'upper_limit', 'upper_linear_limit'],
                                                                 'smaller-than': None,
                                                                 'larger-than': ['lower_limit', 'upper_limit', 'upper_linear_limit']}},
                                                      {'name': 'lower_limit', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                       'range': self.dist_restraint_range,
                                                       'group': {'member-with': ['target_value', 'lower_linear_limit', 'upper_limit', 'upper_linear_limit'],
                                                                 'coexist-with': ['upper_limit'],
                                                                 'smaller-than': ['lower_linear_limit'],
                                                                 'larger-than': ['upper_limit', 'upper_linear_limit']}},
                                                      {'name': 'upper_limit', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                       'range': self.dist_restraint_range,
                                                       'group': {'member-with': ['target_value', 'lower_linear_limit', 'lower_limit', 'upper_linear_limit'],
                                                                 'coexist-with': ['lower_limit'],
                                                                 'smaller-than': ['lower_linear_limit', 'lower_limit'],
                                                                 'larger-than': ['upper_linear_limit']}},
                                                      {'name': 'upper_linear_limit', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                       'range': self.dist_restraint_range,
                                                       'group': {'member-with': ['target_value', 'lower_linear_limit', 'lower_limit', 'upper_limit'],
                                                                 'coexist-with': ['lower_linear_limit', 'lower_limit', 'upper_limit'],
                                                                 'smaller-than': ['lower_linear_limit', 'lower_limit', 'upper_limit'],
                                                                 'larger-than': None}}
                                                      ],
                                   'dihed_restraint': [{'name': 'index', 'type':'index-int', 'mandatory': True},
                                                       {'name': 'restraint_id', 'type':'positive-int', 'mandatory': True},
                                                       {'name': 'restraint_combination_id', 'type':'positive-int', 'mandatory': False},
                                                       {'name': 'weight', 'type':'positive-float', 'mandatory': True,
                                                        'enforce-non-zero': True},
                                                       {'name': 'target_value', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                        'range': self.dihed_restraint_range,
                                                        'group': {'member-with': ['lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit'],
                                                                  'coexist-with': None,
                                                                  'smaller-than': ['lower_limit', 'lower_linear_limit'],
                                                                  'larger-than': ['upper_limit', 'upper_linear_limit']}},
                                                       {'name': 'target_value_uncertainty', 'type':'float', 'mandatory': False},
                                                       {'name': 'lower_linear_limit', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                        'range': self.dihed_restraint_range,
                                                        'group': {'member-with': ['target_value', 'lower_limit', 'upper_limit', 'upper_linear_limit'],
                                                                  'coexist-with': ['lower_limit', 'upper_limit', 'upper_linear_limit'],
                                                                  'smaller-than': None,
                                                                  'larger-than': ['lower_limit', 'upper_limit', 'upper_linear_limit']}},
                                                       {'name': 'lower_limit', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                        'range': self.dihed_restraint_range,
                                                        'group': {'member-with': ['target_value', 'lower_linear_limit', 'upper_limit', 'upper_linear_limit'],
                                                                  'coexist-with': ['upper_limit'],
                                                                  'smaller-than': ['lower_linear_limit'],
                                                                  'larger-than': ['upper_limit', 'upper_linear_limit']}},
                                                       {'name': 'upper_limit', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                        'range': self.dihed_restraint_range,
                                                        'group': {'member-with': ['target_value', 'lower_linear_limit', 'lower_limit', 'upper_linear_limit'],
                                                                  'coexist-with': ['lower_limit'],
                                                                  'smaller-than': ['lower_linear_limit', 'lower_limit'],
                                                                  'larger-than': ['upper_linear_limit']}},
                                                       {'name': 'upper_linear_limit', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                        'range': self.dihed_restraint_range,
                                                        'group': {'member-with': ['target_value', 'lower_linear_limit', 'lower_limit', 'upper_limit'],
                                                                  'coexist-with': ['lower_linear_limit', 'lower_limit', 'upper_limit'],
                                                                  'smaller-than': ['lower_linear_limit', 'lower_limit', 'upper_limit'],
                                                                  'larger-than': None}},
                                                       {'name': 'name', 'type':'str', 'mandatory': False},
                                                    ],
                                   'rdc_restraint': [{'name': 'index', 'type':'index-int', 'mandatory': True},
                                                     {'name': 'restraint_id', 'type':'positive-int', 'mandatory': True},
                                                     {'name': 'restraint_combination_id', 'type':'positive-int', 'mandatory': False},
                                                     {'name': 'target_value', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                      'range': self.rdc_restraint_range,
                                                      'group': {'member-with': ['lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit'],
                                                                'coexist-with': None,
                                                                'smaller-than': ['lower_limit', 'lower_linear_limit'],
                                                                'larger-than': ['upper_limit', 'upper_linear_limit']}},
                                                     {'name': 'target_value_uncertainty', 'type':'positive-float', 'mandatory': False},
                                                     {'name': 'lower_linear_limit', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                      'range': self.rdc_restraint_range,
                                                      'group': {'member-with': ['target_value', 'lower_limit', 'upper_limit', 'upper_linear_limit'],
                                                                'coexist-with': ['lower_limit', 'upper_limit', 'upper_linear_limit'],
                                                                'smaller-than': None,
                                                                'larger-than': ['lower_limit', 'upper_limit', 'upper_linear_limit']}},
                                                     {'name': 'lower_limit', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                      'range': self.rdc_restraint_range,
                                                      'group': {'member-with': ['target_value', 'lower_linear_limit', 'upper_limit', 'upper_linear_limit'],
                                                                'coexist-with': ['upper_limit'],
                                                                'smaller-than': ['lower_linear_limit'],
                                                                'larger-than': ['upper_limit', 'upper_linear_limit']}},
                                                     {'name': 'upper_limit', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                      'range': self.rdc_restraint_range,
                                                      'group': {'member-with': ['target_value', 'lower_linear_limit', 'lower_limit', 'upper_linear_limit'],
                                                                'coexist-with': ['lower_limit'],
                                                                'smaller-than': ['lower_linear_limit', 'lower_limit'],
                                                                'larger-than': ['upper_linear_limit']}},
                                                     {'name': 'upper_linear_limit', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                      'range': self.rdc_restraint_range,
                                                      'group': {'member-with': ['target_value', 'lower_linear_limit', 'lower_limit', 'upper_limit'],
                                                                'coexist-with': ['lower_linear_limit', 'lower_limit', 'upper_limit'],
                                                                'smaller-than': ['lower_linear_limit', 'lower_limit', 'upper_limit'],
                                                                'larger-than': None}},
                                                     {'name': 'scale', 'type':'positive-float', 'mandatory': False,
                                                      'enforce-non-zero': True},
                                                     {'name': 'distance_dependent', 'type':'bool', 'mandatory': False}
                                                     ],
                                   'spectral_peak': [{'name': 'index', 'type':'index-int', 'mandatory': True},
                                                     {'name': 'peak_id', 'type':'positive-int', 'mandatory': True},
                                                     {'name': 'volume', 'type':'float', 'mandatory': False, 'group-mandatory': True,
                                                      'group': {'member-with': ['height'],
                                                                'coexist-with': None}},
                                                     {'name': 'volume_uncertainty', 'type':'positive-float','mandatory': False},
                                                     {'name': 'height', 'type':'float', 'mandatory': False, 'group-mandatory': True,
                                                      'group': {'member-with': ['volume'],
                                                                'coexist-with': None}},
                                                     {'name': 'height_uncertainty', 'type':'positive-float', 'mandatory': False}
                                                     ]
                                   },
                           'nmr-star': {'poly_seq': [{'name': 'Auth_asym_ID', 'type': 'str', 'mandatory': False},
                                                     {'name': 'Auth_seq_ID', 'type': 'int', 'mandatory': False},
                                                     {'name': 'Auth_comp_ID', 'type': 'str', 'mandatory': False},
                                                     {'name': 'Auth_variant_ID', 'type': 'str', 'mandatory': False},
                                                     {'name': 'Sequence_linking', 'type': 'enum', 'mandatory': False,
                                                      'enum': ('start', 'end', 'middle', 'cyclic', 'break', 'single', 'dummy')},
                                                     {'name': 'Cis_residue', 'type': 'bool', 'mandatory': False},
                                                     {'name': 'NEF_index', 'type': 'positive-int', 'mandatory': False}
                                                     ],
                                        'chem_shift': [{'name': 'Atom_type', 'type': 'enum', 'mandatory': True,
                                                        'enum': set(self.atom_isotopes.keys())},
                                                       {'name': 'Atom_isotope_number', 'type': 'enum-int', 'mandatory': True,
                                                        'enum': set(isotope_nums)},
                                                       {'name': 'Val', 'type': 'range-float', 'mandatory': True,
                                                        'range': self.chem_shift_range},
                                                       {'name': 'Val_err', 'type': 'positive-float', 'mandatory': False},
                                                       {'name': 'Ambiguity_code', 'type': 'enum-int', 'mandatory': False,
                                                        'enum': self.bmrb_ambiguity_codes},
                                                       {'name': 'Ambiguity_set_ID', 'type': 'positive-int', 'mandatory': False},
                                                       {'name': 'Auth_asym_ID', 'type': 'str', 'mandatory': False},
                                                       {'name': 'Auth_seq_ID', 'type': 'int', 'mandatory': False},
                                                       {'name': 'Auth_comp_ID', 'type': 'str', 'mandatory': False},
                                                       {'name': 'Auth_atom_ID', 'type': 'str', 'mandatory': False},
                                                       {'name': 'Assigned_chem_shift_list_ID', 'type': 'static-positive-int', 'mandatory': True}
                                                       ],
                                        'dist_restraint': [{'name': 'Index_ID', 'type': 'index-int', 'mandatory': True},
                                                           {'name': 'ID', 'type': 'positive-int', 'mandatory': True},
                                                           {'name': 'Combination_ID', 'type': 'positive-int', 'mandatory': False},
                                                           {'name': 'Member_logic_code', 'type': 'enum', 'mandatory': False,
                                                            'enum': ('OR', 'AND')},
                                                           {'name': 'Target_val', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                            'range': self.dist_restraint_range,
                                                            'group': {'member-with': ['Lower_linear_limit', 'Upper_linear_limit', 'Distance_lower_bound_val', 'Distance_upper_bound_val'],
                                                                      'coexist-with': None,
                                                                      'smaller-than': ['Lower_linear_limit', 'Distance_lower_bound_val'],
                                                                      'larger-than': ['Upper_linear_limit', 'Distance_upper_bound_val']}},
                                                           {'name': 'Target_val_uncertainty', 'type': 'positive-float', 'mandatory': False},
                                                           {'name': 'Lower_linear_limit', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                            'range': self.dist_restraint_range,
                                                            'group': {'member-with': ['Target_val', 'Upper_linear_limit', 'Distance_lower_bound_val', 'Distance_upper_bound_val'],
                                                                      'coexist-with': ['Upper_linear_limit', 'Distance_lower_bound_val', 'Distance_upper_bound_val'],
                                                                      'smaller-than': None,
                                                                      'larger-than': ['Upper_linear_limit', 'Distance_lower_bound_val', 'Distance_upper_bound_val']}},
                                                           {'name': 'Upper_linear_limit', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                            'range': self.dist_restraint_range,
                                                            'group': {'member-with': ['Target_val', 'Lower_linear_limit', 'Distance_lower_bound_val', 'Distance_upper_bound_val'],
                                                                      'coexist-with': ['Lower_linear_limit', 'Distance_lower_bound_val', 'Distance_upper_bound_val'],
                                                                      'smaller-than': ['Lower_linear_limit', 'Distance_lower_bound_val', 'Distance_upper_bound_val'],
                                                                      'larger-than': None}},
                                                           {'name': 'Distance_lower_bound_val', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                            'range': self.dist_restraint_range,
                                                            'group': {'member-with': ['Target_val', 'Lower_linear_limit', 'Upper_linear_limit', 'Distance_upper_bound_val'],
                                                                      'coexist-with': ['Distance_upper_bound_val'],
                                                                      'smaller-than': ['Lower_linear_limit'],
                                                                      'larger-than': ['Upper_linear_limit', 'Distance_upper_bound_val']}},
                                                           {'name': 'Distance_upper_bound_val', 'type': 'range-float', 'mandatory': False, 'group-mandatory': True,
                                                            'range': self.dist_restraint_range,
                                                            'group': {'member-with': ['Target_val', 'Lower_linear_limit', 'Upper_linear_limit', 'Distance_lower_bound_val'],
                                                                      'coexist-with': ['Distance_lower_bound_val'],
                                                                      'smaller-than': ['Lower_linear_limit', 'Distance_lower_bound_val'],
                                                                      'larger-than': ['Upper_linear_limit']}},
                                                           {'name': 'Weight', 'type': 'positive-float', 'mandatory': True,
                                                            'enforce-non-zero': True},
                                                           {'name': 'Auth_asym_ID_1', 'type': 'str', 'mandatory': False},
                                                           {'name': 'Auth_seq_ID_1', 'type': 'int', 'mandatory': False},
                                                           {'name': 'Auth_comp_ID_1', 'type': 'str', 'mandatory': False},
                                                           {'name': 'Auth_atom_ID_1', 'type': 'str', 'mandatory': False},
                                                           {'name': 'Auth_asym_ID_2', 'type': 'str', 'mandatory': False},
                                                           {'name': 'Auth_seq_ID_2', 'type': 'int', 'mandatory': False},
                                                           {'name': 'Auth_comp_ID_2', 'type': 'str', 'mandatory': False},
                                                           {'name': 'Auth_atom_ID_2', 'type': 'str', 'mandatory': False},
                                                           {'name': 'Gen_dist_constraint_list_ID', 'type': 'static-positive-int', 'mandatory': True},
                                                           ],
                                        'dihed_restraint': [{'name': 'Index_ID', 'type':'index-int', 'mandatory': True},
                                                            {'name': 'ID', 'type':'positive-int', 'mandatory': True},
                                                            {'name': 'Combination_ID', 'type':'positive-int', 'mandatory': False},
                                                            {'name': 'Torsion_angle_name', 'type':'str', 'mandatory': False},
                                                            {'name': 'Angle_lower_bound_val', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                             'range': self.dihed_restraint_range,
                                                             'group': {'member-with': ['Angle_target_val', 'Angle_lower_linear_limit', 'Angle_upper_linear_limit', 'Angle_upper_bound_val'],
                                                                       'coexist-with': ['Angle_upper_bound_val'],
                                                                       'smaller-than': ['Angle_lower_linear_limit'],
                                                                       'larger-than': ['Angle_upper_linear_limit', 'Angle_upper_bound_val']}},
                                                            {'name': 'Angle_upper_bound_val', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                             'range': self.dihed_restraint_range,
                                                             'group': {'member-with': ['Angle_target_val', 'Angle_lower_linear_limit', 'Angle_upper_linear_limit', 'Angle_lower_bound_val'],
                                                                       'coexist-with': ['Angle_lower_bound_val'],
                                                                       'smaller-than': ['Angle_lower_linear_limit', 'Angle_lower_bound_val'],
                                                                       'larger-than': ['Angle_upper_linear_limit']}},
                                                            {'name': 'Angle_target_val', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                             'range': self.dihed_restraint_range,
                                                             'group': {'member-with': ['Angle_lower_linear_limit', 'Angle_upper_linear_limit', 'Angle_lower_bound_val', 'Angle_upper_bound_val'],
                                                                       'coexist-with': None,
                                                                       'smaller-than': ['Angle_lower_linear_limit', 'Angle_lower_bound_val'],
                                                                       'larger-than': ['Angle_upper_linear_limit', 'Angle_upper_bound_val']}},
                                                            {'name': 'Angle_target_val_err', 'type':'positive-float', 'mandatory': False},
                                                            {'name': 'Angle_lower_linear_limit', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                             'range': self.dihed_restraint_range,
                                                             'group': {'member-with': ['Angle_target_val', 'Angle_upper_linear_limit', 'Angle_lower_bound_val', 'Angle_upper_bound_val'],
                                                                       'coexist-with': ['Angle_upper_linear_limit', 'Angle_lower_bound_val', 'Angle_upper_bound_val'],
                                                                       'smaller-than': None,
                                                                       'larger-than': ['Angle_upper_linear_limit', 'Angle_lower_bound_val', 'Angle_upper_bound_val']}},
                                                            {'name': 'Angle_upper_linear_limit', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                             'range': self.dihed_restraint_range,
                                                             'group': {'member-with': ['Angle_target_val', 'Angle_lower_linear_limit', 'Angle_lower_bound_val', 'Angle_upper_bound_val'],
                                                                      'coexist-with': ['Angle_lower_linear_limit', 'Angle_lower_bound_val', 'Angle_upper_bound_val'],
                                                                      'smaller-than': ['Angle_lower_linear_limit', 'Angle_lower_bound_val', 'Angle_upper_bound_val'],
                                                                      'larger-than': None}},
                                                            {'name': 'Weight', 'type':'positive-float', 'mandatory': True,
                                                             'enforce-non-zero': True},
                                                            {'name': 'Auth_asym_ID_1', 'type':'str', 'mandatory': False},
                                                            {'name': 'Auth_seq_ID_1', 'type':'int', 'mandatory': False},
                                                            {'name': 'Auth_comp_ID_1', 'type':'str', 'mandatory': False},
                                                            {'name': 'Auth_atom_ID_1', 'type':'str', 'mandatory': False},
                                                            {'name': 'Auth_asym_ID_2', 'type':'str', 'mandatory': False},
                                                            {'name': 'Auth_seq_ID_2', 'type':'int', 'mandatory': False},
                                                            {'name': 'Auth_comp_ID_2', 'type':'str', 'mandatory': False},
                                                            {'name': 'Auth_atom_ID_2', 'type':'str', 'mandatory': False},
                                                            {'name': 'Auth_asym_ID_3', 'type':'str', 'mandatory': False},
                                                            {'name': 'Auth_seq_ID_3', 'type':'int', 'mandatory': False},
                                                            {'name': 'Auth_comp_ID_3', 'type':'str', 'mandatory': False},
                                                            {'name': 'Auth_atom_ID_3', 'type':'str', 'mandatory': False},
                                                            {'name': 'Auth_asym_ID_4', 'type':'str', 'mandatory': False},
                                                            {'name': 'Auth_seq_ID_4', 'type':'int', 'mandatory': False},
                                                            {'name': 'Auth_comp_ID_4', 'type':'str', 'mandatory': False},
                                                            {'name': 'Auth_atom_ID_4', 'type':'str', 'mandatory': False},
                                                            {'name': 'Torsion_angle_constraint_list_ID', 'type':'static-positive-int', 'mandatory': True},
                                            ],
                                        'rdc_restraint': [{'name': 'Index_ID', 'type':'index-int', 'mandatory': True},
                                                          {'name': 'ID', 'type':'positive-int', 'mandatory': True},
                                                          {'name': 'Combination_ID', 'type':'positive-int', 'mandatory': False},
                                                          {'name': 'Weight', 'type':'positive-float', 'mandatory': True,
                                                           'enforce-non-zero': True},
                                                          {'name': 'Target_value', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                           'range': self.dihed_restraint_range,
                                                           'group': {'member-with': ['RDC_lower_linear_limit', 'RDC_upper_linear_limit', 'RDC_lower_bound', 'RDC_upper_bound'],
                                                                     'coexist-with': None,
                                                                     'smaller-than': ['RDC_lower_linear_limit', 'RDC_lower_bound'],
                                                                     'larger-than': ['RDC_upper_linear_limit', 'RDC_upper_bound']}},
                                                          {'name': 'Target_value_uncertainty', 'type':'positive-float', 'mandatory': False},
                                                          {'name': 'RDC_lower_bound', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                           'range': self.dihed_restraint_range,
                                                           'group': {'member-with': ['Target_value', 'RDC_lower_linear_limit', 'RDC_upper_linear_limit', 'RDC_upper_bound'],
                                                                     'coexist-with': ['RDC_upper_bound'],
                                                                     'smaller-than': ['RDC_lower_linear_limit'],
                                                                     'larger-than': ['RDC_upper_linear_limit', 'RDC_upper_bound']}},
                                                          {'name': 'RDC_upper_bound', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                           'range': self.dihed_restraint_range,
                                                           'group': {'member-with': ['Target_value', 'RDC_lower_linear_limit', 'RDC_upper_linear_limit', 'RDC_lower_bound'],
                                                                     'coexist-with': ['RDC_lower_bound'],
                                                                     'smaller-than': ['RDC_lower_linear_limit', 'RDC_lower_bound'],
                                                                     'larger-than': ['RDC_upper_linear_limit']}},
                                                          {'name': 'RDC_lower_linear_limit', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                           'range': self.dihed_restraint_range,
                                                           'group': {'member-with': ['Target_value', 'RDC_upper_linear_limit', 'RDC_lower_bound', 'RDC_upper_bound'],
                                                                     'coexist-with': ['RDC_upper_linear_limit', 'RDC_lower_bound', 'RDC_upper_bound'],
                                                                     'smaller-than': None,
                                                                     'larger-than': ['RDC_upper_linear_limit', 'RDC_lower_bound', 'RDC_upper_bound']}},
                                                          {'name': 'RDC_upper_linear_limit', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                           'range': self.dihed_restraint_range,
                                                           'group': {'member-with': ['Target_value', 'RDC_upper_linear_limit', 'RDC_lower_bound', 'RDC_upper_bound'],
                                                                     'coexist-with': ['RDC_upper_linear_limit', 'RDC_lower_bound', 'RDC_upper_bound'],
                                                                     'smaller-than': None,
                                                                     'larger-than': ['RDC_upper_linear_limit', 'RDC_lower_bound', 'RDC_upper_bound']}},
                                                          {'name': 'RDC_val_scale_factor', 'type':'positive-float', 'mandatory': False},
                                                          {'name': 'RDC_distant_dependent', 'type':'bool', 'mandatory': False},
                                                          {'name': 'Auth_asym_ID_1', 'type':'str', 'mandatory': False},
                                                          {'name': 'Auth_seq_ID_1', 'type':'int', 'mandatory': False},
                                                          {'name': 'Auth_comp_ID_1', 'type':'str', 'mandatory': False},
                                                          {'name': 'Auth_atom_ID_1', 'type':'str', 'mandatory': False},
                                                          {'name': 'Auth_asym_ID_2', 'type':'str', 'mandatory': False},
                                                          {'name': 'Auth_seq_ID_2', 'type':'int', 'mandatory': False},
                                                          {'name': 'Auth_comp_ID_2', 'type':'str', 'mandatory': False},
                                                          {'name': 'Auth_atom_ID_2', 'type':'str', 'mandatory': False},
                                                          {'name': 'RDC_constraint_list_ID', 'type':'static-positive-int', 'mandatory': True}
                                                          ],
                                        'spectral_peak': [{'name': 'Index_ID', 'type':'index-int', 'mandatory': True},
                                                          {'name': 'ID', 'type':'positive-int', 'mandatory': True},
                                                          {'name': 'Volume', 'type':'float', 'mandatory': False, 'group-mandatory': True,
                                                           'group': {'member-with': ['Height'],
                                                                     'coexist-with': None}},
                                                          {'name': 'Volume_uncertainty', 'type':'positive-float', 'mandatory': False},
                                                          {'name': 'Height', 'type':'float', 'mandatory': False, 'group-mandatory': True,
                                                           'group': {'member-with': ['Volume'],
                                                                     'coexist-with': None}},
                                                          {'name': 'Height_uncertainty', 'type':'positive-float', 'mandatory': False},
                                                          {'name': 'Spectral_peak_list_ID', 'type':'static-positive-int', 'mandatory': True}
                                                          ]
                                        }
                           }

        # data items for spectral peak
        self.spectral_peak_data_items = {'nef': [{'name': 'position_uncertainty_%s', 'type':'positive-float', 'mandatory': False},
                                                 {'name': 'chain_code_%s', 'type':'str', 'mandatory': False},
                                                 {'name': 'sequence_code_%s', 'type':'int', 'mandatory': False},
                                                 {'name': 'residue_name_%s', 'type':'str', 'mandatory': False},
                                                 {'name': 'atom_name_%s', 'type':'str', 'mandatory': False}],
                                         'nmr-star': [{'name': 'Position_uncertainty_%s', 'type':'positive-float', 'mandatory': False},
                                                      {'name': 'Entity_assembly_ID_%s', 'type':'positive-int', 'mandatory': False},
                                                      {'name': 'Comp_index_ID_%s', 'type':'int', 'mandatory': False},
                                                      {'name': 'Comp_ID_%s', 'type':'str', 'mandatory': False},
                                                      {'name': 'Atom_ID_%s', 'type':'str', 'mandatory': False},
                                                      {'name': 'Auth_asym_ID_%s', 'type':'str', 'mandatory': False},
                                                      {'name': 'Auth_seq_ID_%s', 'type':'int', 'mandatory': False},
                                                      {'name': 'Auth_comp_ID_%s', 'type':'str', 'mandatory': False},
                                                      {'name': 'Auth_atom_ID_%s', 'type':'str', 'mandatory': False}]
                                         }

        # number of dimension of spectral peak
        self.num_dim_items = {'nef': 'num_dimensions', 'nmr-star': 'Number_of_spectral_dimensions'}

        # allowed tags
        self.allowed_tags = {'nef': {'poly_seq': ['index', 'chain_code', 'sequence_code', 'residue_name', 'linking', 'residue_variant', 'cis_peptide'],
                                     'chem_shift': ['chain_code', 'sequence_code', 'residue_name', 'atom_name', 'value', 'value_uncertainty', 'element', 'isotope_number'],
                                     'dist_restraint': ['index', 'restraint_id', 'restraint_combination_id', 'chain_code_1', 'sequence_code_1', 'residue_name_1', 'atom_name_1', 'chain_code_2', 'sequence_code_2', 'residue_name_2', 'atom_name_2', 'weight', 'target_value', 'target_value_uncertainty', 'lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit'],
                                     'dihed_restraint': ['index', 'restraint_id', 'restraint_combination_id', 'chain_code_1', 'sequence_code_1', 'residue_name_1', 'atom_name_1', 'chain_code_2', 'sequence_code_2', 'residue_name_2', 'atom_name_2', 'chain_code_3', 'sequence_code_3', 'residue_name_3', 'atom_name_3', 'chain_code_4', 'sequence_code_4', 'residue_name_4', 'atom_name_4', 'weight', 'target_value', 'target_value_uncertainty', 'lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit', 'name' ],
                                     'rdc_restraint': ['index', 'restraint_id', 'restraint_combination_id', 'chain_code_1', 'sequence_code_1', 'residue_name_1', 'atom_name_1', 'chain_code_2', 'sequence_code_2', 'residue_name_2', 'atom_name_2', 'weight', 'target_value', 'target_value_uncertainty', 'lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit', 'scale', 'distance_dependent'],
                                     'spectral_peak': ['index', 'peak_id', 'volume', 'volume_uncertainty', 'height', 'height_uncertainty', 'position_1', 'position_uncertainty_1', 'position_2', 'position_uncertainty_2', 'position_3', 'position_uncertainty_3', 'position_4', 'position_uncertainty_4', 'position_5', 'position_uncertainty_5', 'position_6', 'position_uncertainty_6', 'position_7', 'position_uncertainty_7', 'position_8', 'position_uncertainty_8', 'position_9', 'position_uncertainty_9', 'position_10', 'position_uncertainty_10', 'position_11', 'position_uncertainty_11', 'position_12', 'position_uncertainty_12', 'position_13', 'position_uncertainty_13', 'position_14', 'position_uncertainty_14', 'position_15', 'position_uncertainty_15', 'chain_code_1', 'sequence_code_1', 'residue_name_1', 'atom_name_1', 'chain_code_2', 'sequence_code_2', 'residue_name_2', 'atom_name_2', 'chain_code_3', 'sequence_code_3', 'residue_name_3', 'atom_name_3', 'chain_code_4', 'sequence_code_4', 'residue_name_4', 'atom_name_4', 'chain_code_5', 'sequence_code_5', 'residue_name_5', 'atom_name_5', 'chain_code_6', 'sequence_code_6', 'residue_name_6', 'atom_name_6', 'chain_code_7', 'sequence_code_7', 'residue_name_7', 'atom_name_7', 'chain_code_8', 'sequence_code_8', 'residue_name_8', 'atom_name_8', 'chain_code_9', 'sequence_code_9', 'residue_name_9', 'atom_name_9', 'chain_code_10', 'sequence_code_10', 'residue_name_10', 'atom_name_10', 'chain_code_11', 'sequence_code_11', 'residue_name_11', 'atom_name_11', 'chain_code_12', 'sequence_code_12', 'residue_name_12', 'atom_name_12', 'chain_code_13', 'sequence_code_13', 'residue_name_13', 'atom_name_13', 'chain_code_14', 'sequence_code_14', 'residue_name_14', 'atom_name_14', 'chain_code_15', 'sequence_code_15', 'residue_name_15', 'atom_name_15']
                                     },
                             'nmr-star': {'poly_seq': ['Assembly_chem_comp_ID', 'Entity_assembly_ID', 'Entity_ID', 'Comp_index_ID', 'Comp_ID', 'Seq_ID', 'Auth_entity_assembly_ID', 'Auth_asym_ID', 'Auth_seq_ID', 'Auth_comp_ID', 'Auth_variant_ID', 'Sequence_linking', 'Cis_residue', 'NEF_index', 'Entry_ID', 'Assembly_ID'],
                                          'chem_shift': ['ID', 'Assembly_atom_ID', 'Entity_assembly_ID', 'Entity_ID', 'Comp_index_ID', 'Seq_ID', 'Comp_ID', 'Atom_ID', 'Atom_type', 'Atom_isotope_number', 'Val', 'Val_err', 'Assign_fig_of_merit', 'Ambiguity_code', 'Ambiguity_set_ID', 'Occupancy', 'Resonance_ID', 'NEF_atom_name', 'Auth_entity_assembly_ID', 'Auth_asym_ID', 'Auth_seq_ID', 'Auth_comp_ID', 'Auth_atom_ID', 'Details', 'Entry_ID', 'Assigned_chem_shift_list_ID'],
                                          'dist_restraint': ['Index_ID', 'ID', 'Combination_ID', 'Member_ID', 'Member_logic_code', 'Assembly_atom_ID_1', 'Entity_assembly_ID_1', 'Entity_ID_1', 'Comp_index_ID_1', 'Seq_ID_1', 'Comp_ID_1', 'Atom_ID_1', 'Atom_type_1', 'Atom_isotope_number_1', 'Resonance_ID_1', 'Assembly_atom_ID_2', 'Entity_assembly_ID_2', 'Entity_ID_2', 'Comp_index_ID_2', 'Seq_ID_2', 'Comp_ID_2', 'Atom_ID_2', 'Atom_type_2', 'Atom_isotope_number_2', 'Resonance_ID_2', 'Intensity_val', 'Intensity_lower_val_err', 'Intensity_upper_val_err', 'Distance_val', 'Target_val', 'Target_val_uncertainty', 'Lower_linear_limit', 'Upper_linear_limit', 'Distance_lower_bound_val', 'Distance_upper_bound_val', 'Contribution_fractional_val', 'Weight', 'Spectral_peak_ID', 'Spectral_peak_list_ID', 'PDB_record_ID_1', 'PDB_model_num_1', 'PDB_strand_ID_1', 'PDB_ins_code_1', 'PDB_residue_no_1', 'PDB_residue_name_1', 'PDB_atom_name_1', 'PDB_record_ID_2', 'PDB_model_num_2', 'PDB_strand_ID_2', 'PDB_ins_code_2', 'PDB_residue_no_2', 'PDB_residue_name_2', 'PDB_atom_name_2', 'Auth_entity_assembly_ID_1', 'Auth_asym_ID_1', 'Auth_chain_ID_1', 'Auth_seq_ID_1', 'Auth_comp_ID_1', 'Auth_atom_ID_1', 'Auth_alt_ID_1', 'Auth_atom_name_1', 'Auth_entity_assembly_ID_2', 'Auth_asym_ID_2', 'Auth_chain_ID_2', 'Auth_seq_ID_2', 'Auth_comp_ID_2', 'Auth_atom_ID_2', 'Auth_alt_ID_2', 'Auth_atom_name_2', 'Entry_ID', 'Gen_dist_constraint_list_ID'],
                                          'dihed_restraint': ['Index_ID', 'ID', 'Combination_ID', 'Set_ID', 'Torsion_angle_name', 'Assembly_atom_ID_1', 'Entity_assembly_ID_1', 'Entity_ID_1', 'Comp_index_ID_1', 'Seq_ID_1', 'Comp_ID_1', 'Atom_ID_1', 'Atom_type_1', 'Resonance_ID_1', 'Assembly_atom_ID_2', 'Entity_assembly_ID_2', 'Entity_ID_2', 'Comp_index_ID_2', 'Seq_ID_2', 'Comp_ID_2', 'Atom_ID_2', 'Atom_type_2', 'Resonance_ID_2', 'Assembly_atom_ID_3', 'Entity_assembly_ID_3', 'Entity_ID_3', 'Comp_index_ID_3', 'Seq_ID_3', 'Comp_ID_3', 'Atom_ID_3', 'Atom_type_3', 'Resonance_ID_3', 'Assembly_atom_ID_4', 'Entity_assembly_ID_4', 'Entity_ID_4', 'Comp_index_ID_4', 'Seq_ID_4', 'Comp_ID_4', 'Atom_ID_4', 'Atom_type_4', 'Resonance_ID_4', 'Angle_lower_bound_val', 'Angle_upper_bound_val', 'Angle_target_val', 'Angle_target_val_err', 'Angle_lower_linear_limit', 'Angle_upper_linear_limit', 'Weight', 'Source_experiment_ID', 'Figure_of_merit', 'PDB_record_ID_1', 'PDB_model_num_1', 'PDB_strand_ID_1', 'PDB_ins_code_1', 'PDB_residue_no_1', 'PDB_residue_name_1', 'PDB_atom_name_1', 'PDB_record_ID_2', 'PDB_model_num_2', 'PDB_strand_ID_2', 'PDB_ins_code_2', 'PDB_residue_no_2', 'PDB_residue_name_2', 'PDB_atom_name_2', 'PDB_record_ID_3', 'PDB_model_num_3', 'PDB_strand_ID_3', 'PDB_ins_code_3', 'PDB_residue_no_3', 'PDB_residue_name_3', 'PDB_atom_name_3', 'PDB_record_ID_4', 'PDB_model_num_4', 'PDB_strand_ID_4', 'PDB_ins_code_4', 'PDB_residue_no_4', 'PDB_residue_name_4', 'PDB_atom_name_4', 'Auth_entity_assembly_ID_1', 'Auth_asym_ID_1', 'Auth_chain_ID_1', 'Auth_seq_ID_1', 'Auth_comp_ID_1', 'Auth_atom_ID_1', 'Auth_alt_ID_1', 'Auth_atom_name_1', 'Auth_entity_assembly_ID_2', 'Auth_asym_ID_2', 'Auth_chain_ID_2', 'Auth_seq_ID_2', 'Auth_comp_ID_2', 'Auth_atom_ID_2', 'Auth_alt_ID_2', 'Auth_atom_name_2', 'Auth_entity_assembly_ID_3', 'Auth_asym_ID_3', 'Auth_chain_ID_3', 'Auth_seq_ID_3', 'Auth_comp_ID_3', 'Auth_atom_ID_3', 'Auth_alt_ID_3', 'Auth_atom_name_3', 'Auth_entity_assembly_ID_4', 'Auth_asym_ID_4', 'Auth_chain_ID_4', 'Auth_seq_ID_4', 'Auth_comp_ID_4', 'Auth_atom_ID_4', 'Auth_alt_ID_4', 'Auth_atom_name_4', 'Entry_ID', 'Torsion_angle_constraint_list_ID'],
                                          'rdc_restraint': ['Index_ID', 'ID', 'Combination_ID', 'Assembly_atom_ID_1', 'Entity_assembly_ID_1', 'Entity_ID_1', 'Comp_index_ID_1', 'Seq_ID_1', 'Comp_ID_1', 'Atom_ID_1', 'Atom_type_1', 'Atom_isotope_number_1', 'Resonance_ID_1', 'Assembly_atom_ID_2', 'Entity_assembly_ID_2', 'Entity_ID_2', 'Comp_index_ID_2', 'Seq_ID_2', 'Comp_ID_2', 'Atom_ID_2', 'Atom_type_2', 'Atom_isotope_number_2', 'Resonance_ID_2', 'Weight', 'RDC_val', 'RDC_val_err', 'Target_value', 'Target_value_uncertainty', 'RDC_lower_bound', 'RDC_upper_bound', 'RDC_lower_linear_limit', 'RDC_upper_linear_limit', 'RDC_val_scale_factor', 'RDC_bond_length', 'RDC_distant_dependent', 'Source_experiment_ID', 'PDB_record_ID_1', 'PDB_model_num_1', 'PDB_strand_ID_1', 'PDB_ins_code_1', 'PDB_residue_no_1', 'PDB_residue_name_1', 'PDB_atom_name_1', 'PDB_record_ID_2', 'PDB_model_num_2', 'PDB_strand_ID_2', 'PDB_ins_code_2', 'PDB_residue_no_2', 'PDB_residue_name_2', 'PDB_atom_name_2', 'Auth_entity_assembly_ID_1', 'Auth_asym_ID_1', 'Auth_chain_ID_1', 'Auth_seq_ID_1', 'Auth_comp_ID_1', 'Auth_atom_ID_1', 'Auth_alt_ID_1', 'Auth_atom_name_1', 'Auth_entity_assembly_ID_2', 'Auth_asym_ID_2', 'Auth_chain_ID_2', 'Auth_seq_ID_2', 'Auth_comp_ID_2', 'Auth_atom_ID_2', 'Auth_alt_ID_2', 'Auth_atom_name_2', 'Entry_ID', 'RDC_constraint_list_ID'],
                                          'spectral_peak': ['Index_ID', 'ID', 'Volume', 'Volume_uncertainty', 'Height', 'Height_uncertainty', 'Figure_of_merit', 'Restraint', 'Position_1', 'Position_uncertainty_1', 'Line_width_1', 'Line_width_uncertainty_1', 'Position_2', 'Position_uncertainty_2', 'Line_width_2', 'Line_width_uncertainty_2', 'Position_3', 'Position_uncertainty_3', 'Line_width_3', 'Line_width_uncertainty_3', 'Position_4', 'Position_uncertainty_4', 'Line_width_4', 'Line_width_uncertainty_4', 'Position_5', 'Position_uncertainty_5', 'Line_width_5', 'Line_width_uncertainty_5', 'Position_6', 'Position_uncertainty_6', 'Line_width_6', 'Line_width_uncertainty_6', 'Position_7', 'Position_uncertainty_7', 'Line_width_7', 'Line_width_uncertainty_7', 'Position_8', 'Position_uncertainty_8', 'Line_width_8', 'Line_width_uncertainty_8', 'Position_9', 'Position_uncertainty_9', 'Line_width_9', 'Line_width_uncertainty_9', 'Position_10', 'Position_uncertainty_10', 'Line_width_10', 'Line_width_uncertainty_10', 'Position_11', 'Position_uncertainty_11', 'Line_width_11', 'Line_width_uncertainty_11', 'Position_12', 'Position_uncertainty_12', 'Line_width_12', 'Line_width_uncertainty_12', 'Position_13', 'Position_uncertainty_13', 'Line_width_13', 'Line_width_uncertainty_13', 'Position_14', 'Position_uncertainty_14', 'Line_width_14', 'Line_width_uncertainty_14', 'Position_15', 'Position_uncertainty_15', 'Line_width_15', 'Line_width_uncertainty_15', 'Entity_assembly_ID_1', 'Entity_ID_1', 'Comp_index_ID_1', 'Seq_ID_1', 'Comp_ID_1', 'Atom_ID_1', 'Ambiguity_code_1', 'Ambiguity_set_ID_1', 'Entity_assembly_ID_2', 'Entity_ID_2', 'Comp_index_ID_2', 'Seq_ID_2', 'Comp_ID_2', 'Atom_ID_2', 'Ambiguity_code_2', 'Ambiguity_set_ID_2', 'Entity_assembly_ID_3', 'Entity_ID_3', 'Comp_index_ID_3', 'Seq_ID_3', 'Comp_ID_3', 'Atom_ID_3', 'Ambiguity_code_3', 'Ambiguity_set_ID_3', 'Entity_assembly_ID_4', 'Entity_ID_4', 'Comp_index_ID_4', 'Seq_ID_4', 'Comp_ID_4', 'Atom_ID_4', 'Ambiguity_code_4', 'Ambiguity_set_ID_4', 'Entity_assembly_ID_5', 'Entity_ID_5', 'Comp_index_ID_5', 'Seq_ID_5', 'Comp_ID_5', 'Atom_ID_5', 'Ambiguity_code_5', 'Ambiguity_set_ID_5', 'Entity_assembly_ID_6', 'Entity_ID_6', 'Comp_index_ID_6', 'Seq_ID_6', 'Comp_ID_6', 'Atom_ID_6', 'Ambiguity_code_6', 'Ambiguity_set_ID_6', 'Entity_assembly_ID_7', 'Entity_ID_7', 'Comp_index_ID_7', 'Seq_ID_7', 'Comp_ID_7', 'Atom_ID_7', 'Ambiguity_code_7', 'Ambiguity_set_ID_7', 'Entity_assembly_ID_8', 'Entity_ID_8', 'Comp_index_ID_8', 'Seq_ID_8', 'Comp_ID_8', 'Atom_ID_8', 'Ambiguity_code_8', 'Ambiguity_set_ID_8', 'Entity_assembly_ID_9', 'Entity_ID_9', 'Comp_index_ID_9', 'Seq_ID_9', 'Comp_ID_9', 'Atom_ID_9', 'Ambiguity_code_9', 'Ambiguity_set_ID_9', 'Entity_assembly_ID_10', 'Entity_ID_10', 'Comp_index_ID_10', 'Seq_ID_10', 'Comp_ID_10', 'Atom_ID_10', 'Ambiguity_code_10', 'Ambiguity_set_ID_10', 'Entity_assembly_ID_11', 'Entity_ID_11', 'Comp_index_ID_11', 'Seq_ID_11', 'Comp_ID_11', 'Atom_ID_11', 'Ambiguity_code_11', 'Ambiguity_set_ID_11', 'Entity_assembly_ID_12', 'Entity_ID_12', 'Comp_index_ID_12', 'Seq_ID_12', 'Comp_ID_12', 'Atom_ID_12', 'Ambiguity_code_12', 'Ambiguity_set_ID_12', 'Entity_assembly_ID_13', 'Entity_ID_13', 'Comp_index_ID_13', 'Seq_ID_13', 'Comp_ID_13', 'Atom_ID_13', 'Ambiguity_code_13', 'Ambiguity_set_ID_13', 'Entity_assembly_ID_14', 'Entity_ID_14', 'Comp_index_ID_14', 'Seq_ID_14', 'Comp_ID_14', 'Atom_ID_14', 'Ambiguity_code_14', 'Ambiguity_set_ID_14', 'Entity_assembly_ID_15', 'Entity_ID_15', 'Comp_index_ID_15', 'Seq_ID_15', 'Comp_ID_15', 'Atom_ID_15', 'Ambiguity_code_15', 'Ambiguity_set_ID_15', 'Auth_entity_assembly_ID_1', 'Auth_entity_ID_1', 'Auth_asym_ID_1', 'Auth_seq_ID_1', 'Auth_comp_ID_1', 'Auth_atom_ID_1', 'Auth_ambiguity_code_1', 'Auth_ambiguity_set_ID_1', 'Auth_entity_assembly_ID_2', 'Auth_entity_ID_2', 'Auth_asym_ID_2', 'Auth_seq_ID_2', 'Auth_comp_ID_2', 'Auth_atom_ID_2', 'Auth_ambiguity_code_2', 'Auth_ambiguity_set_ID_2', 'Auth_entity_assembly_ID_3', 'Auth_entity_ID_3', 'Auth_asym_ID_3', 'Auth_seq_ID_3', 'Auth_comp_ID_3', 'Auth_atom_ID_3', 'Auth_ambiguity_code_3', 'Auth_ambiguity_set_ID_3', 'Auth_entity_assembly_ID_4', 'Auth_entity_ID_4', 'Auth_asym_ID_4', 'Auth_seq_ID_4', 'Auth_comp_ID_4', 'Auth_atom_ID_4', 'Auth_ambiguity_code_4', 'Auth_ambiguity_set_ID_4', 'Auth_entity_assembly_ID_5', 'Auth_entity_ID_5', 'Auth_asym_ID_5', 'Auth_seq_ID_5', 'Auth_comp_ID_5', 'Auth_atom_ID_5', 'Auth_ambiguity_code_5', 'Auth_ambiguity_set_ID_5', 'Auth_entity_assembly_ID_6', 'Auth_entity_ID_6', 'Auth_asym_ID_6', 'Auth_seq_ID_6', 'Auth_comp_ID_6', 'Auth_atom_ID_6', 'Auth_ambiguity_code_6', 'Auth_ambiguity_set_ID_6', 'Auth_entity_assembly_ID_7', 'Auth_entity_ID_7', 'Auth_asym_ID_7', 'Auth_seq_ID_7', 'Auth_comp_ID_7', 'Auth_atom_ID_7', 'Auth_ambiguity_code_7', 'Auth_ambiguity_set_ID_7', 'Auth_entity_assembly_ID_8', 'Auth_entity_ID_8', 'Auth_asym_ID_8', 'Auth_seq_ID_8', 'Auth_comp_ID_8', 'Auth_atom_ID_8', 'Auth_ambiguity_code_8', 'Auth_ambiguity_set_ID_8', 'Auth_entity_assembly_ID_9', 'Auth_entity_ID_9', 'Auth_asym_ID_9', 'Auth_seq_ID_9', 'Auth_comp_ID_9', 'Auth_atom_ID_9', 'Auth_ambiguity_code_9', 'Auth_ambiguity_set_ID_9', 'Auth_entity_assembly_ID_10', 'Auth_entity_ID_10', 'Auth_asym_ID_10', 'Auth_seq_ID_10', 'Auth_comp_ID_10', 'Auth_atom_ID_10', 'Auth_ambiguity_code_10', 'Auth_ambiguity_set_ID_10', 'Auth_entity_assembly_ID_11', 'Auth_entity_ID_11', 'Auth_asym_ID_11', 'Auth_seq_ID_11', 'Auth_comp_ID_11', 'Auth_atom_ID_11', 'Auth_ambiguity_code_11', 'Auth_ambiguity_set_ID_11', 'Auth_entity_assembly_ID_12', 'Auth_entity_ID_12', 'Auth_asym_ID_12', 'Auth_seq_ID_12', 'Auth_comp_ID_12', 'Auth_atom_ID_12', 'Auth_ambiguity_code_12', 'Auth_ambiguity_set_ID_12', 'Auth_entity_assembly_ID_13', 'Auth_entity_ID_13', 'Auth_asym_ID_13', 'Auth_seq_ID_13', 'Auth_comp_ID_13', 'Auth_atom_ID_13', 'Auth_ambiguity_code_13', 'Auth_ambiguity_set_ID_13', 'Auth_entity_assembly_ID_14', 'Auth_entity_ID_14', 'Auth_asym_ID_14', 'Auth_seq_ID_14', 'Auth_comp_ID_14', 'Auth_atom_ID_14', 'Auth_ambiguity_code_14', 'Auth_ambiguity_set_ID_14', 'Auth_entity_assembly_ID_15', 'Auth_entity_ID_15', 'Auth_asym_ID_15', 'Auth_seq_ID_15', 'Auth_comp_ID_15', 'Auth_atom_ID_15', 'Auth_ambiguity_code_15', 'Auth_ambiguity_set_ID_15', 'Details', 'Sf_ID', 'Entry_ID', 'Spectral_peak_list_ID'],
                                          }
                              }

        # disallowed tags of spectral peak
        self.spectral_peak_disallowed_tags = {'nef': ['position_%s', 'position_uncertainty_%s', 'chain_code_%s', 'sequence_code_%s', 'residue_name_%s', 'atom_name_%s'],
                                              'nmr-star': ['Position_%s', 'Position_uncertainty_%s', 'Line_width_%s', 'Line_width_uncertainty_%s', 'Entity_assembly_ID_%s', 'Entity_ID_%s', 'Comp_index_ID_%s', 'Seq_ID_%s', 'Comp_ID_%s', 'Atom_ID_%s', 'Ambiguity_code_%s', 'Ambiguity_set_ID_%s', 'Auth_entity_assembly_ID_%s', 'Auth_entity_ID_%s', 'Auth_asym_ID_%s', 'Auth_seq_ID_%s', 'Auth_comp_ID_%s', 'Auth_atom_ID_%s', 'Auth_ambiguity_code_%s', 'Auth_ambiguity_set_ID_%s']
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
                         'U': 'U'}

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
                raise KeyError("+NmrDpUtility.addInput() ++ Error  - Unknown input type %s." % type)

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
                raise KeyError("+NmrDpUtility.addOutput() ++ Error  - Unknown output type %s." % type)

                return False

            return True

        except:
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

        # run workflow operation specific tasks
        if op in self.__procTasksDict:

            for task in self.__procTasksDict[op]:

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.op() starting op %s - task %s\n" % (op, task.__name__))

                if not task():
                    self.report.writeJson(self.__logPath)

                    return False

        # run general processing tasks
        if 'parser-check' in op:

            for task in self.__procTasksDict['nmr-parser-check']:

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.op() starting op %s - task %s\n" % (op, task.__name__))

                if not task():
                    self.report.writeJson(self.__logPath)

                    return False

        elif 'consistency-check' in op:

            for task in self.__procTasksDict['nmr-consistency-check']:

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.op() starting op %s - task %s\n" % (op, task.__name__))

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
        input_source.setItemValue('file_type', 'nef' if 'nef' in self.__op else 'nmr-star')
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

        _file_type = message['file_type'] # nef/nmr-star/unknown

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        if is_valid:

            if _file_type != file_type:

                self.report.error.addDescription('format_issue', "%s was selected as %s file, but recognized as %s file." % (file_name, self.readable_file_type[file_type], self.readable_file_type[_file_type]))

                if len(message['error']) > 0:
                    for error_message in message['error']:
                        self.report.error.addDescription('format_issue', "Diagnostic information - %s" % error_message)

                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__validateInputSource() ++ Error  - %s was selected as %s file, but recognized as %s file.\n" % (file_name, self.readable_file_type[file_type], self.readable_file_type[_file_type]))

                return False

            return True

        else:

            self.report.error.addDescription('format_issue', "%s is invalid %s file." % (file_name, self.readable_file_type[file_type]))

            if len(message['error']) > 0:
                for error_message in message['error']:
                    self.report.error.addDescription('format_issue', "Diagnostic information - %s" % error_message)

            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__validateInputSource() ++ Error  - %s is invalid %s file." % (file_name, self.readable_file_type[file_type]))

            return False

    def __detectContentSubType(self):
        """ Detect content subtypes in NEF/NMR-STAR V3.2 file.
        """

        if self.report.isError():
            return False

        is_done, star_data_type, self.__star_data = self.nef_translator.read_input_file(self.__srcPath) # NEFTranslator.validate_file() generates this object internally, but not re-used.

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        lp_category_list = self.nef_translator.get_data_content(self.__star_data, star_data_type)[1]

        # initialize loop counter
        lp_counts = {t:0 for t in self.nmr_content_subtypes}

        # increment loop counter of each content subtype
        for lp_category in lp_category_list:
            if lp_category in self.lp_categories[file_type].values():
                lp_counts[[k for k, v in self.lp_categories[file_type].items() if v == lp_category][0]] += 1

        content_subtypes = {k:lp_counts[k] for k in lp_counts if lp_counts[k] > 0}

        input_source.setItemValue('content_subtype', content_subtypes)

        content_subtype = 'poly_seq'

        if lp_counts[content_subtype] == 0:

            sf_category = self.sf_categories[file_type][content_subtype]

            self.report.warning.addDescription('missing_saveframe', "Saveframe category %s were not found in %s file." % (sf_category, file_name))
            self.report.setWarning(warning)

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__detectContentSubType() ++ Warning  - Saveframe category %s were not found in %s file.\n" % (sf_category, file_name))

        elif lp_counts[content_subtype] > 1:

            sf_category = self.sf_categories[file_type][content_subtype]

            self.report.error.addDescription('format_issue', "Unexpectedly, multiple saveframes belonging to category %s were found in %s file." % (sf_category, file_name))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__detectContentSubType() ++ Error  - Unexpectedly, multiple saveframes belonging to category %s were found in %s file.\n" % (sf_category, file_name))

        content_subtype = 'chem_shift'

        if lp_counts[content_subtype] == 0:

            sf_category = self.sf_categories[file_type][content_subtype]
            lp_category = self.lp_categories[file_type][content_subtype]

            self.report.error.addDescription('missing_mandatory_content', "Assigned chemical shifts are mandatory for PDB/BMRB deposition. Saveframe category %s and loop category %s were not found in %s file." % (sf_category, lp_category, file_name))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__detectContentSubType() ++ Error  - Assigned chemical shifts are mandatory for PDB/BMRB deposition. Saveframe category %s and loop category %s were not found in %s file." % (sf_category, lp_category, file_name))

        content_subtype = 'dist_restraint'

        if lp_counts[content_subtype] == 0:

            sf_category = self.sf_categories[file_type][content_subtype]
            lp_category = self.lp_categories[file_type][content_subtype]

            self.report.error.addDescription('missing_mandatory_content', "Distance restraints are mandatory for PDB/BMRB deposition. Saveframe category %s and loop category %s were not found in %s file." % (sf_category, lp_category, file_name))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__detectContentSubType() ++ Error  - Distance restraints are mandatory for PDB/BMRB deposition. Saveframe category %s and loop category %s were not found in %s file." % (sf_category, lp_category, file_name))

        content_subtype = 'spectral_peak'

        if lp_counts[content_subtype] == 0:

            sf_category = self.sf_categories[file_type][content_subtype]
            lp_category = self.lp_categories[file_type][content_subtype]

            self.report.warning.addDescription('missing_content', "Spectral peak list is missing. The wwPDB NMR Validation Task Force strongly encourages the submission of spectral peak lists, in particular those generated from NOESY spectra. Saveframe category %s and loop category %s were not found in %s file." % (sf_category, lp_category, file_name))
            self.report.setWarning()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__detectContentSubType() ++ Warning  - Spectral peak list is missing. The wwPDB NMR Validation Task Force strongly encourages the submission of spectral peak lists, in particular those generated from NOESY spectra. Saveframe category %s and loop category %s were not found in %s file." % (sf_category, lp_category, file_name))

        return not self.report.isError()

    def __getPolymerSequence(self, sf_data, content_subtype):
        """ Wrapper function to retrieve polymer sequence from loop of a specified saveframe and content subtype via NEFTranslator.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        if file_type == 'nef':
            return self.nef_translator.get_nef_seq(sf_data, lp_category=self.lp_categories[file_type][content_subtype], allow_empty=(content_subtype == 'spectral_peak'))
        else:
            return self.nef_translator.get_star_seq(sf_data, lp_category=self.lp_categories[file_type][content_subtype], allow_empty=(content_subtype == 'spectral_peak'))

    def __extractPolymerSequence(self):
        """ Extract reference polymer sequence of NEF/NMR-STAR V3.2 file.
        """

        if self.report.isError():
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        content_subtype = 'poly_seq'

        if not content_subtype in input_source_dic['content_subtype']:
            return True

        sf_category = self.sf_categories[file_type][content_subtype]

        sf_data = self.__star_data.get_saveframes_by_category(sf_category)[0]

        sf_framecode = sf_data.get_tag('sf_framecode')[0]

        try:

            poly_seq = self.__getPolymerSequence(sf_data, content_subtype)[0]

            input_source.setItemValue('polymer_sequence', poly_seq)

            if file_type == 'nmr-star':
                auth_poly_seq = self.nef_translator.get_star_auth_seq(sf_data, lp_category=self.lp_categories[file_type][content_subtype])[0]

                for cid in range(len(poly_seq)):
                    chain_id = poly_seq[cid]['chain_id']
                    comp_ids = poly_seq[cid]['comp_id']

                    for auth_cid in range(len(auth_poly_seq)):

                        if auth_poly_seq[auth_cid]['chain_id'] != chain_id:
                            continue

                        auth_comp_ids = auth_poly_seq[auth_cid]['auth_comp_id']

                        if comp_ids == auth_comp_ids: # no difference
                            continue

                        for i in range(len(poly_seq[cid]['comp_id'])):

                            comp_id = comp_ids[i]
                            auth_comp_id = auth_comp_ids[i]

                            if comp_id == auth_comp_id:
                                continue

                            seq_id = poly_seq[cid]['seq_id'][i]

                            auth_asym_id = auth_poly_seq[auth_cid]['auth_asym_id'][i]
                            auth_seq_id = auth_poly_seq[auth_cid]['auth_seq_id'][i]

                            self.report.warning.addDescription('sequence_mismatch', "Author comp ID %s (auth_asym_id %s, auth_seq_id %s) vs %s (chain_id %s, seq_id %s) mismatches in %s saveframe." % (auth_comp_id, auth_asym_id, auth_seq_id, comp_id, chain_id, seq_id, sf_framecode))
                            self.report.setWarning()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__extractPolymerSequence() ++ Warning  - Author comp ID %s (auth_asym_id %s, auth_seq_id %s) vs %s (chain_id %s, seq_id %s) mismatches in %s saveframe." % (auth_comp_id, auth_asym_id, auth_seq_id, comp_id, chain_id, seq_id, sf_framecode))

            return True

        except KeyError as e:

            self.report.error.addDescription('sequence_mismatch', "%s, %s saveframe." % (str(e).strip("'"), sf_framecode))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__extractPolymerSequence() ++ KeyError  - %s" % str(e))

        except LookupError as e:

            self.report.error.addDescription('missing_mandatory_item', "%s, %s saveframe." % (str(e).strip("'"), sf_framecode))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__extractPolymerSequence() ++ LookupError  - %s" % str(e))

        except ValueError as e:

            self.report.error.addDescription('invalid_data', "%s, %s saveframe." % (str(e).strip("'"), sf_framecode))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__extractPolymerSequence() ++ ValueError  - %s" % str(e))

        except Exception as e:

            self.report.error.addDescription('internal_error', "+NmrDpUtility.__extractPolymerSequence() ++ Error  - %s" % str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__extractPolymerSequence() ++ Error  - %s" % str(e))

        return False

    def __extractPolymerSequenceInLoop(self):
        """ Extract polymer sequence in interesting loops of NEF/NMR-STAR V3.2 file.
        """

        if self.report.isError():
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        poly_seq_list_set = {}
        poly_sid_list_set = {}

        for content_subtype in self.nmr_content_subtypes:

            if content_subtype == 'poly_seq' or not content_subtype in input_source_dic['content_subtype']:
                continue

            poly_seq_list_set[content_subtype] = []

            sf_category = self.sf_categories[file_type][content_subtype]

            list_id = 1
            has_poly_seq = False

            for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

                sf_framecode = sf_data.get_tag('sf_framecode')[0]

                try:

                    poly_seq = self.__getPolymerSequence(sf_data, content_subtype)

                    if len(poly_seq) > 0:
                        poly_seq_list_set[content_subtype].append({'list_id': list_id, 'sf_framecode': sf_framecode, 'polymer_sequence': poly_seq[0]})

                        has_poly_seq = True

                        if file_type == 'nmr-star':
                            auth_poly_seq = self.nef_translator.get_star_auth_seq(sf_data, lp_category=self.lp_categories[file_type][content_subtype])[0]

                            for cid in range(len(poly_seq)):
                                chain_id = poly_seq[cid]['chain_id']
                                comp_ids = poly_seq[cid]['comp_id']

                                for auth_cid in range(len(auth_poly_seq)):

                                    if auth_poly_seq[auth_cid]['chain_id'] != chain_id:
                                        continue

                                    auth_comp_ids = auth_poly_seq[auth_cid]['auth_comp_id']

                                    if comp_ids == auth_comp_ids: # no difference
                                        continue

                                    for i in range(len(poly_seq[cid]['comp_id'])):

                                        comp_id = comp_ids[i]
                                        auth_comp_id = auth_comp_ids[i]

                                        if comp_id == auth_comp_id:
                                            continue

                                        seq_id = poly_seq[cid]['seq_id'][i]

                                        auth_asym_id = auth_poly_seq[auth_cid]['auth_asym_id'][i]
                                        auth_seq_id = auth_poly_seq[auth_cid]['auth_seq_id'][i]

                                        self.report.warning.addDescription('sequence_mismatch', "Author comp ID %s (auth_asym_id %s, auth_seq_id %s) vs %s (chain_id %s, seq_id %s) mismatches in %s saveframe." % (auth_comp_id, auth_asym_id, auth_seq_id, comp_id, chain_id, seq_id, sf_framecode))
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__extractPolymerSequenceInLoop() ++ Warning  - Author comp ID %s (auth_asym_id %s, auth_seq_id %s) vs %s (chain_id %s, seq_id %s) mismatches in %s saveframe." % (auth_comp_id, auth_asym_id, auth_seq_id, comp_id, chain_id, seq_id, sf_framecode))

                    list_id += 1

                except KeyError as e:

                    self.report.error.addDescription('sequence_mismatch', "%s, %s saveframe." % (str(e).strip("'"), sf_framecode))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__extractPolymerSequenceInLoop() ++ KeyError  - %s" % str(e))

                except LookupError as e:

                    self.report.error.addDescription('missing_mandatory_item', "%s, %s saveframe." % (str(e).strip("'"), sf_framecode))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__extractPolymerSequenceInLoop() ++ LookupError  - %s" % str(e))

                except ValueError as e:

                    self.report.error.addDescription('invalid_data', "%s, %s saveframe." % (str(e).strip("'"), sf_framecode))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__extractPolymerSequenceInLoop() ++ ValueError  - %s" % str(e))

                except Exception as e:

                    self.report.error.addDescription('internal_error', "+NmrDpUtility.__extractPolymerSequenceInLoop() ++ Error  - %s" % str(e))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__extractPolymerSequenceInLoop() ++ Error  - %s" % str(e))

            if not has_poly_seq:
                poly_seq_list_set.pop(content_subtype)

        if self.report.isError():
            return False

        input_source.setItemValue('polymer_sequence_in_loop', poly_seq_list_set)

        return True

    def __testSequenceConsistency(self):
        """ Perform sequence consistency test among extracted polymer sequences.
        """

        if self.report.isError():
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        polymer_sequence = input_source_dic['polymer_sequence']
        polymer_sequence_in_loop = input_source_dic['polymer_sequence_in_loop']

        has_poly_seq = 'polymer_sequence' in input_source_dic
        has_poly_seq_in_loop = 'polymer_sequence_in_loop' in input_source_dic

        if not has_poly_seq and not has_poly_seq_in_loop:
            return True

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

            # reference polymer sequence exists
            if has_poly_seq and subtype1 == poly_seq:
                ps1 = polymer_sequence

                ref_cids = {s1['chain_id'] for s1 in ps1}

                list_len2 = len(polymer_sequence_in_loop[subtype2])

                for list_id2 in range(list_len2):
                    ps2 = polymer_sequence_in_loop[subtype2][list_id2]['polymer_sequence']

                    sf_framecode2 = polymer_sequence_in_loop[subtype2][list_id2]['sf_framecode']

                    for s2 in ps2:

                        if not s2['chain_id'] in ref_cids:
                            self.report.error.addDescription('sequence_mismatch', "Invalid chain_id %s exists in %s saveframe." % (cid, sf_framecode2))
                            self.report.setError()

                        else:

                            for s1 in ps1:

                                if s1['chain_id'] != s2['chain_id']:
                                    continue

                                for j in range(len(s2['seq_id'])):
                                    sid = s2['seq_id'][j]
                                    seq = s2['comp_id'][j]

                                    if not sid in s1['seq_id']:
                                        self.report.error.addDescription('sequence_mismatch', "Invalid seq_id %s (chain_id %s) exists in %s saveframe." % (sid, cid, sf_framecode2))
                                        self.report.setError()

                                    else:
                                        i = s1['seq_id'].index(sid)

                                        if seq != s1['comp_id'][i]:
                                            self.report.error.addDescription('sequence_mismatch', "Invalid comp_id %s vs %s (seq_id %s, chain_id %s) exists in %s saveframe." % (seq, s1['comp_id'][i], sid, cid, sf_framecode2))
                                            self.report.setError()

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

                            cid = s2['chain_id']

                            for s1 in ps1:

                                if cid != s1['chain_id']:
                                    continue

                                for j in range(len(s2['seq_id'])):
                                    sid = s2['seq_id'][j]
                                    seq = s2['comp_id'][j]

                                    if sid in s1['seq_id']:
                                        i = s1['seq_id'].index(sid)

                                        if seq != s1['comp_id'][i]:
                                            self.report.error.addDescription('sequence_mismatch', "Unmatched comp_id %s vs %s (seq_id %s, chain_id %s) exists in %s against %s saveframe." % (seq, s1['comp_id'][i], sid, cid, sf_framecode2, sf_framecode1))
                                            self.report.setError()

                        # inverse check required for unverified sequences
                        for s1 in ps1:

                            cid = s1['chain_id']

                            for s2 in ps2:

                                if cid != s2['chain_id]']:
                                    continue

                                for i in range(len(s1['seq_id'])):
                                    sid = s1['seq_id'][i]
                                    seq = s1['comp_id'][i]

                                    if sid in s2['seq_id']:
                                        j = s2['seq_id'].index(sid)

                                        if seq != s2['comp_id'][j]:
                                            self.report.error.addDescription('sequence_mismatch', "Unmatched comp_id %s vs %s (seq_id %s, chain_id %s) exists in %s against %s saveframe." % (seq, s2['comp_id'][j], sid, cid, sf_framecode1, sf_framecode2))
                                            self.report.setError()

        return not self.report.isError()

    def __extractCommonPolymerSequence(self):
        """ Extract common polymer sequence if required.
        """

        if self.report.isError():
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        has_poly_seq = 'polymer_sequence' in input_source_dic
        has_poly_seq_in_loop = 'polymer_sequence_in_loop' in input_source_dic

        # pass if poly_seq exists
        if has_poly_seq or not has_poly_seq_in_loop:
            return True

        polymer_sequence_in_loop = input_source_dic['polymer_sequence_in_loop']

        common_poly_seq = {}

        for subtype in polymer_sequence_in_loop.keys():
            list_len = len(polymer_sequence_in_loop[subtype])

            for list_id in range(list_len):
                ps = polymer_sequence_in_loop[subtype][list_id]['polymer_sequence']

                for s in ps:
                    cid = s['chain_id']

                    if not cid in common_poly_seq:
                        common_poly_seq[cid] = set()

        for subtype in polymer_sequence_in_loop.keys():
            list_len = len(polymer_sequence_in_loop[subtype])

            for list_id in range(list_len):
                ps = polymer_sequence_in_loop[subtype][list_id]['polymer_sequence']

                cid = s['chain_id']

                for i in range(len(s['seq_id'])):
                    sid = s['seq_id'][i]
                    seq = s['comp_id'][i]

                    common_poly_seq[cid].add('{:04d} {}'.format(sid, seq))

        asm = [] # molecular assembly of a loop

        for cid in sorted(common_poly_seq.keys()):

            if len(common_poly_seq[cid]) > 0:
                sorted_poly_seq = sorted(common_poly_seq[cid])

                ent = {} # entity
                ent['chain_id'] = cid
                ent['seq_id'] = [int(i.split(' ')[0]) for i in sorted_poly_seq]
                ent['comp_id'] = [i.split(' ')[1] for i in sorted_poly_seq]
                asm.append(ent)

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

        has_poly_seq = 'polymer_sequence' in input_source_dic

        if not has_poly_seq:

            if self.__verbose:
                logging.warning('+NmrDpUtility.__extractNonStandardResidue() ++ Warning  - Common polymer sequence does not exist, __extractCommonPolymerSequence() should be invoked.')

            return True

        polymer_sequence = input_source_dic['polymer_sequence']

        asm_has = False

        asm = []

        for s in polymer_sequence:

            ent_has = False

            ent = {}
            ent['chain_id'] = s['chain_id']
            ent['seq_id'] = []
            ent['comp_id'] = []

            for i in range(len(s['seq_id'])):
                sid = s['seq_id'][i]
                seq = s['comp_id'][i]

                if self.nef_translator.get_one_letter_code(seq) == '?':
                    asm_has = True
                    ent_has = True

                    ent['seq_id'].append(sid)
                    ent['comp_id'].append(seq)

            if ent_has:
                asm.append(ent)

        if asm_has:
            input_source.setItemValue('non_standard_residue', asm)

        return True

    def __appendPolymerSequenceAlignment(self):
        """ Append polymer sequence alignment of interesting loops of NEF/NMR-STAR V3.2 file.
        """

        if self.report.isError():
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        has_poly_seq = 'polymer_sequence' in input_source_dic
        has_poly_seq_in_loop = 'polymer_sequence_in_loop' in input_source_dic

        if not has_poly_seq:

            self.report.error.addDescription('internal_error', "+NmrDpUtility.__appendPolymerSequenceAlignment() ++ Error  - Common polymer sequence does not exist, __extractCommonPolymerSequence() should be invoked.")
            self.report.setError()

            if self.__verbose:
                logging.warning("+NmrDpUtility.__appendPolymerSequenceAlignment() ++ Error  - Common polymer sequence does not exist, __extractCommonPolymerSequence() should be invoked.")

            return False

        if not has_poly_seq_in_loop:
            return True

        polymer_sequence = input_source_dic['polymer_sequence']
        polymer_sequence_in_loop = input_source_dic['polymer_sequence_in_loop']

        for s1 in polymer_sequence:
            cid = s1['chain_id']

            for subtype in polymer_sequence_in_loop.keys():
                list_len = len(polymer_sequence_in_loop[subtype])

                has_seq_align = False

                seq_align_set = []

                for list_id in range(list_len):
                    ps2 = polymer_sequence_in_loop[subtype][list_id]['polymer_sequence']

                    for s2 in ps2:

                        if cid != s2['chain_id']:
                            continue

                        _s2 = self.__fillBlankedCompId(s1, s2)

                        pA = PairwiseAlign()
                        pA.setVerbose(self.__verbose)
                        pA.setReferenceSequence(s1['comp_id'], 'REF' + cid)
                        pA.addTestSequence(_s2['comp_id'], cid)
                        pA.doAlign()
                        #pA.prAlignmentConflicts(cid)
                        myAlign = pA.getAlignment(cid)

                        length = len(myAlign)

                        if length == 0:
                            continue

                        has_seq_align = True

                        conflicts = 0
                        for myPr in myAlign:
                            if myPr[0] != myPr[1]:
                                conflicts += 1

                        ref_seq = self.__get1LetterCodeSequence(s1['comp_id'])
                        tst_seq = self.__get1LetterCodeSequence(_s2['comp_id'])
                        mid_seq = self.__getMiddleCode(ref_seq, tst_seq)

                        seq_align = {'list_id': polymer_sequence_in_loop[subtype][list_id]['list_id'],
                                     'sf_framecode': polymer_sequence_in_loop[subtype][list_id]['sf_framecode'],
                                     'chain_id': cid, 'length': length, 'conflict': conflicts, 'coverage': float('{:.3f}'.format(float(length - conflicts) / float(length))), 'ref_seq_id': s1['seq_id'], 'reference_seq': ref_seq, 'middle_code': mid_seq, 'test_seq': tst_seq}

                        seq_align_set.append(seq_align)

                if has_seq_align:
                    self.report.sequence_alignment.setItemValue('poly_seq_vs_' + subtype, seq_align_set)

        return True

    def __fillBlankedCompId(self, s1, s2):
        """ Fill blanked comp ID in s2 against s1.
        """

        sid = sorted(set(s1['seq_id']) | set(s2['seq_id']))
        seq = []

        for i in sid:
            if i in s2['seq_id']:
                j = s2['seq_id'].index(i)
                seq.append(s2['comp_id'][j])
            else:
                seq.append('.') # blank comp id

        return {'chain_id': s2['chain_id'], 'seq_id': sid, 'comp_id': seq}

    def __get1LetterCode(self, comp_id):
        """ Convert comp ID to 1-letter code.
        """

        if comp_id in self.monDict3:
            return self.monDict3[comp_id]
        elif comp_id in (None, '', '.', '?'):
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

    def __getMiddleCode(self, ref_seq, tst_seq):
        """ Return array of middle code of sequence alignment.
        """

        array = ''

        for i in range(len(ref_seq)):
            array += '|' if ref_seq[i] == tst_seq[i] else ' '

        return array

    def __testAtomNomenclature(self):
        """ Perform atom nomenclature test for standard residues supported by NEFTranslator.
        """

        if self.report.isError():
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        polymer_sequence_in_loop = input_source_dic['polymer_sequence_in_loop']

        for content_subtype in polymer_sequence_in_loop.keys():

            sf_category = self.sf_categories[file_type][content_subtype]

            list_id = 1

            for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

                sf_framecode = sf_data.get_tag('sf_framecode')[0]

                try:

                    if file_type == 'nef':
                        pairs = self.nef_translator.get_nef_comp_atom_pair(
                            sf_data,
                            lp_category=self.lp_categories[file_type][content_subtype],
                            allow_empty=(content_subtype == 'spectral_peak'))[0]
                    else:
                        pairs = self.nef_translator.get_star_comp_atom_pair(
                            sf_data,
                            lp_category=self.lp_categories[file_type][content_subtype],
                            allow_empty=(content_subtype == 'spectral_peak'))[0]

                    for pair in pairs:
                        comp_id = pair['comp_id']
                        atom_ids = pair['atom_id']

                        # standard residue
                        if self.nef_translator.get_one_letter_code(comp_id) != '?':

                            if file_type == 'nef':

                                _atom_ids = []
                                for atom_id in atom_ids:

                                    _atom_id = self.nef_translator.get_nmrstar_atom(comp_id, atom_id)[1]

                                    if len(_atom_id) == 0:
                                        self.report.error.addDescription('invalid_atom_nomenclature', "Invalid atom_id %s (comp_id %s) exists in %s saveframe." % (atom_id, comp_id, sf_framecode))
                                        self.report.setError()

                                    else:
                                        _atom_ids.extend(self.nef_translator.get_nmrstar_atom(comp_id, atom_id)[1])

                                atom_ids = sorted(set(_atom_ids))

                            for atom_id in atom_ids:

                                if not self.nef_translator.validate_comp_atom(comp_id, atom_id):
                                    self.report.error.addDescription('invalid_atom_nomenclature', "Invalid atom_id %s (comp_id %s) exists in %s saveframe." % (atom_id, comp_id, sf_framecode))
                                    self.report.setError()

                        # non-standard residue
                        else:
                            pass

                    list_id += 1

                except LookupError as e:

                    self.report.error.addDescription('missing_mandatory_item', "%s, %s saveframe." % (str(e).strip("'"), sf_framecode))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testAtomNomenclature() ++ LookupError  - %s" % str(e))

                except ValueError as e:

                    self.report.error.addDescription('invalid_data', "%s, %s saveframe." % (str(e).strip("'"), sf_framecode))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testAtomNomenclature() ++ ValueError  - %s" % str(e))

                except Exception as e:

                    self.report.error.addDescription('internal_error', "+NmrDpUtility.__testAtomNomenclature() ++ Error  - %s" % str(e))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testAtomNomenclature() ++ Error  - %s" % str(e))

        return not self.report.isError()

    def __testAtomTypeOfCSLoop(self):
        """ Perform atom type, isotope number test on assigned chemical shifts.
        """

        if self.report.isError():
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        content_subtype = 'chem_shift'

        if not content_subtype in input_source_dic['content_subtype'].keys():

            self.report.error.addDescription('internal_error', "+NmrDpUtility.__testAtomTypeOfCSLoop() ++ Error  - Assigned chemical shift loop does not exists in %s file." % file_name)
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__testAtomTypeOfCSLoop() ++ Error  - Assigned chemical shift loop does not exists in %s file" % file_name)

            return False

        sf_category = self.sf_categories[file_type][content_subtype]

        list_id = 1

        for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

            sf_framecode = sf_data.get_tag('sf_framecode')[0]

            try:

                if file_type == 'nef':
                    a_types = self.nef_translator.get_nef_atom_type_from_cs_loop(sf_data)[0]
                else:
                    a_types = self.nef_translator.get_star_atom_type_from_cs_loop(sf_data)[0]

                for a_type in a_types:
                    atom_type = a_type['atom_type']
                    isotope_nums = a_type['isotope_number']
                    atom_ids = a_type['atom_id']

                    if not atom_type in self.atom_isotopes.keys():
                        self.report.error.addDescription('invalid_atom_type', "Invalid atom_type %s exists in %s saveframe." % (atom_type, sf_framecode))
                        self.report.setError()

                    else:
                        for isotope_num in isotope_nums:
                            if not isotope_num in self.atom_isotopes[atom_type]:
                                self.report.error.addDescription('invalid_isotope_number', "Invalid isotope number %s (atom_type %s, allowed isotope number %s) exists in %s saveframe." % (isotope_num, atom_type, self.atom_isotopes[atom_type], sf_framecode))
                                self.report.setError()

                        for atom_id in atom_ids:
                            if not atom_id.startswith(atom_type):
                                self.report.error.addDescription('invalid_atom_nomenclature', "Invalid atom_id %s (atom_type %s) exists in %s saveframe." % (atom_id, atom_type, sf_framecode))
                                self.report.setError()

                list_id += 1

            except LookupError as e:

                self.report.error.addDescription('missing_mandatory_item', "%s, %s saveframe." % (str(e).strip("'"), sf_framecode))
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__testAtomTypeOfCSLoop() ++ LookupError  - %s" % str(e))

            except ValueError as e:

                self.report.error.addDescription('invalid_data', "%s, %s saveframe." % (str(e).strip("'"), sf_framecode))
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__testAtomTypeOfCSLoop() ++ ValueError  - %s" % str(e))

            except Exception as e:

                self.report.error.addDescription('internal_error', "+NmrDpUtility.__testAtomTypeOfCSLoop() ++ Error  - %s" % str(e))
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__testAtomTypeOfCSLoop() ++ Error  - %s" % str(e))

        return not self.report.isError()

    def __testAmbiguityCodeOfCSLoop(self):
        """ Perform ambiguity code test on assigned chemical shifts.
        """

        if self.report.isError():
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        content_subtype = 'chem_shift'

        if not content_subtype in input_source_dic['content_subtype'].keys():

            self.report.error.addDescription('internal_error', "+NmrDpUtility.__testAmbiguityCodeOfCSLoop() ++ Error  - Assigned chemical shift loop does not exists in %s file." % file_name)
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__testAmbiguityCodeOfCSLoop() ++ Error  - Assigned chemical shift loop does not exists in %s file" % file_name)

            return False

        # NEF file has no ambiguity code
        if file_type == 'nef':
            return True

        sf_category = self.sf_categories[file_type][content_subtype]

        list_id = 1

        for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

            sf_framecode = sf_data.get_tag('sf_framecode')[0]

            try:

                a_codes = self.nef_translator.get_star_ambig_code_from_cs_loop(sf_data)[0]

                comp_ids_wo_ambig_code = []

                for a_code in a_codes:
                    comp_id = a_code['comp_id']
                    ambig_code = a_code['ambig_code']
                    atom_ids = a_code['atom_id']

                    # standard residue
                    if self.nef_translator.get_one_letter_code(comp_id) != '?':

                        if ambig_code is None:
                            comp_ids_wo_ambig_code.append(comp_id)

                        elif ambig_code == 1 or ambig_code >= 4:
                            pass

                        # ambig_code is 2 (geminal atoms) or 3 (aromatic ring atoms in opposite side)
                        else:

                            for atom_id in atom_ids:

                                if ambig_code > self.__getMaxAmbigCodeWoSetId(comp_id, atom_id):
                                    self.report.error.addDescription('invalid_ambiguity_code', "Invalid ambiguity code %s (comp_id %s, atom_id %s, allowed ambig_code %s) exists in %s saveframe." % (ambig_code, comp_id, atom_id, [1, self.__getMaxAmbigCodeWoSetId(comp_id, atom_id), 4, 5, 6, 9], sf_framecode))
                                    self.report.setError()

                    # non-standard residue
                    else:
                        pass

                if len(comp_ids_wo_ambig_code) > 0:
                    self.report.warning.addDescription('missing_data', "Missing ambiguity code for standard residues in %s saveframe." % sf_framecode)
                    self.report.setWarning()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testAmbigCodeOfCSLoop() ++ Warning  - Missing ambiguity code for standard residues in %s saveframe." % sf_framecode)

                list_id += 1

            except LookupError as e:

                self.report.error.addDescription('missing_mandatory_item', "%s, %s saveframe." % (str(e).strip("'"), sf_framecode))
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__testAmbigCodeOfCSLoop() ++ LookupError  - %s" % str(e))

            except ValueError as e:

                self.report.error.addDescription('invalid_data', "%s, %s saveframe." % (str(e).strip("'"), sf_framecode))
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__testAmbigCodeOfCSLoop() ++ ValueError  - %s" % str(e))

            except Exception as e:

                self.report.error.addDescription('internal_error', "+NmrDpUtility.__testAmbigCodeOfCSLoop() ++ Error  - %s" % str(e))
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__testAmbigCodeOfCSLoop() ++ Error  - %s" % str(e))

        return not self.report.isError()

    def __getMaxAmbigCodeWoSetId(self, comp_id, atom_id):
        """ Return maximum ambiguity code of a given atom that does not require declaration of ambiguity set ID
        """

        code = self.__get1LetterCode(comp_id)

        if code == '.' or code == 'X':
            return 1

        if atom_id.startswith('H'):

            if comp_id == 'ARG':
                if atom_id in ['HB2', 'HB3', 'HG2', 'HG3', 'HD2', 'HD3', 'HH11', 'HH12', 'HH21', 'HH22']:
                    return 2

            elif comp_id == 'ASN':
                if atom_id in ['HB2', 'HB3', 'HD21', 'HD22']:
                    return 2

            elif comp_id in ['ASP', 'CYS', 'HIS', 'SER', 'TRP']:
                if atom_id in ['HB2', 'HB3']:
                    return 2

            elif comp_id == 'GLN':
                if atom_id in ['HB2', 'HB3', 'HG2', 'HG3', 'HE21', 'HE22']:
                    return 2

            elif comp_id in ['GLU', 'MET']:
                if atom_id in ['HB2', 'HB3', 'HG2', 'HG3']:
                    return 2

            elif comp_id == 'GLY':
                if atom_id in ['HA2', 'HA3']:
                    return 2

            elif comp_id == 'ILE':
                if atom_id in ['HG12', 'HG13']:
                    return 2

            elif comp_id == 'LEU':
                if atom_id in ['HB2', 'HB3', 'HD11', 'HD12', 'HD13', 'HD21', 'HD22', 'HD23']:
                    return 2

            elif comp_id == 'LYS':
                if atom_id in ['HB2', 'HB3', 'HG2', 'HG3', 'HD2', 'HD3', 'HE2', 'HE3']:
                    return 2

            elif comp_id in ['PHE', 'TYR']:
                if atom_id in ['HB2', 'HB3']:
                    return 2

                elif atom_id in ['HD1', 'HD2', 'HE1', 'HE2']:
                    return 3

            elif comp_id == 'PRO':
                if atom_id in ['HB2', 'HB3', 'HG2', 'HG3', 'HD2', 'HD3']:
                    return 2

            elif comp_id == 'VAL':
                if atom_id in ['HG11', 'HG12', 'HG13', 'HG21', 'HG22', 'HG23']:
                    return 2

            elif comp_id == 'DA':
                if atom_id in ['H61', 'H62', "H2'", "H2''", "H5'", "H5''"]:
                    return 2

            elif comp_id == 'DG':
                if atom_id in ['H21', 'H22', "H2'", "H2''", "H5'", "H5''"]:
                    return 2

            elif comp_id == 'DC':
                if atom_id in ['H41', 'H42', "H2'", "H2''", "H5'", "H5''"]:
                    return 2

            elif comp_id == 'DT':
                if atom_id in ["H2'", "H2''", "H5'", "H5''"]:
                    return 2

            elif comp_id == 'A':
                if atom_id in ['H61', 'H62', "H5'", "H5''"]:
                    return 2

            elif comp_id == 'G':
                if atom_id in ['H21', 'H22', "H5'", "H5''"]:
                    return 2

            elif comp_id == 'C':
                if atom_id in ['H41', 'H42', "H5'", "H5''"]:
                    return 2

            elif comp_id == 'U':
                if atom_id in ["H5'", "H5''"]:
                    return 2

        elif atom_id.startswith('C'):

            if comp_id == 'LEU':
                if atom_id in ['CD1', 'CD2']:
                    return 2

            elif comp_id in ['PHE', 'TYR']:
                if atom_id in ['CD1', 'CD2', 'CE1', 'CE2']:
                    return 3

            elif comp_id == 'VAL':
                if atom_id in ['CG1', 'CG2']:
                    return 2

        elif atom_id.startswith('N'):

            if comp_id == 'ARG':
                if atom_id in ['NH1', 'NH2']:
                    return 2

        return 1

    def __testDuplicatedIndex(self):
        """ Perform duplication test on index of interesting loops of NEF/NMR-STAR V3.2 file.
        """

        if self.report.isError():
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        for content_subtype in input_source_dic['content_subtype'].keys():

            sf_category = self.sf_categories[file_type][content_subtype]
            index_tag = self.index_tags[file_type][content_subtype]

            if index_tag is None:
                continue

            list_id = 1

            for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

                sf_framecode = sf_data.get_tag('sf_framecode')[0]

                try:

                    indices = self.nef_translator.get_index(sf_data, lp_category=self.lp_categories[file_type][content_subtype], index_id=self.index_tags[file_type][content_subtype])[0]

                    if indices != range(1, len(indices) + 1):
                        self.report.warning.addDescription('disordered_index', "Index (loop tag %s.%s) is disordered in %s saveframe." % (self.lp_categories[file_type][content_subtype], index_tag, sf_framecode))
                        self.report.setWarning()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__testIndexConsistency() ++ Warning  - %s" % str(e))

                    list_id += 1

                except KeyError as e:

                    self.report.error.addDescription('duplicated_index', "%s, %s saveframe." % (str(e).strip("'"), sf_framecode))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testIndexConsistency() ++ KeyError  - %s" % str(e))

                except LookupError as e:

                    self.report.error.addDescription('missing_mandatory_item', "%s, %s saveframe." % (str(e).strip("'"), sf_framecode))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testIndexConsistency() ++ LookupError  - %s" % str(e))

                except ValueError as e:

                    self.report.error.addDescription('invalid_data', "%s, %s saveframe." % (str(e).strip("'"), sf_framecode))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testIndexConsistency() ++ ValueError  - %s" % str(e))

                except Exception as e:

                    self.report.error.addDescription('internal_error', "+NmrDpUtility.__testIndexConsistency() ++ Error  - %s" % str(e))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testIndexConsistency() ++ Error  - %s" % str(e))

        return not self.report.isError()

    def __testDataConsistencyInLoop(self):
        """ Perform consistency test on data of interesting loops of NEF/NMR-STAR V3.2 file
        """

        if self.report.isError():
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        for content_subtype in input_source_dic['content_subtype'].keys():

            sf_category = self.sf_categories[file_type][content_subtype]

            list_id = 1

            for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

                sf_framecode = sf_data.get_tag('sf_framecode')[0]

                allowed_tags = self.allowed_tags[file_type][content_subtype]
                disallowed_tags = None

                if content_subtype == 'spectral_peak':

                    try:

                        _num_dim = sf_data.get_tag(self.num_dim_items[file_type])[0]
                        num_dim = int(_num_dim)

                    except ValueError:
                        self.report.error.addDescription('invalid_data', "%s %s must be in %s, %s saveframe." % (self.num_dim_items[file_type], _num_dim, set(range(1, self.spectral_peak_lim_dim)), sf_framecode))
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__testDataConsistencyInLoop() ++ ValueError  - %s %s must be in %s, %s saveframe." % (self.num_dim_items[file_type], _num_dim, range(1, self.spectral_peak_lim_dim), sf_framecode))

                    if not num_dim in range(1, self.spectral_peak_lim_dim):

                        self.report.error.addDescription('invalid_data', "%s %s must be in %s, %s saveframe." % (self.num_dim_items[file_type], num_dim, range(1, self.spectral_peak_lim_dim), sf_framecode))
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__testDataConsistencyInLoop() ++ ValueError  - %s %s must be in %s, %s saveframe." % (self.num_dim_items[file_type], num_dim, range(1, self.spectral_peak_lim_dim), sf_framecode))

                    max_dim = num_dim + 1

                    key_items = []
                    for dim in range(1, max_dim):
                        for k in self.spectral_peak_key_items[file_type]:
                            _k = copy.copy(k)
                            if '%s' in k['name']:
                               _k['name'] = k['name'] % dim
                            key_items.append(_k)

                    data_items = []
                    for d in self.data_items[file_type][content_subtype]:
                        data_items.append(d)
                    for dim in range(1, max_dim):
                        for d in self.spectral_peak_data_items[file_type]:
                            _d = copy.copy(d)
                            if '%s' in d['name']:
                                _d['name'] = d['name'] % dim
                            data_items.append(_d)

                    if max_dim < self.spectral_peak_lim_dim:
                        disallowed_tags = []
                        for dim in range(max_dim, self.spectral_peak_lim_dim):
                            for t in self.spectral_peak_disallowed_tags[file_type]:
                                if '%s' in t:
                                    t = t % dim
                                disallowed_tags.append(t)

                else:

                    key_items = self.key_items[file_type][content_subtype]
                    data_items = self.data_items[file_type][content_subtype]

                try:

                    data = self.nef_translator.check_data(sf_data, self.lp_categories[file_type][content_subtype], key_items, data_items, allowed_tags, disallowed_tags, False, False)[0]

                    # TODO

                    list_id += 1

                except KeyError as e:

                    self.report.error.addDescription('multiple_data', "%s, %s saveframe." % (str(e).strip("'"), sf_framecode))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testDataConsistencyInLoop() ++ KeyError  - %s" % str(e))

                except LookupError as e:

                    self.report.error.addDescription('missing_mandatory_item', "%s, %s saveframe." % (str(e).strip("'"), sf_framecode))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testDataConsistencyInLoop() ++ LookupError  - %s" % str(e))

                except ValueError as e:

                    self.report.error.addDescription('invalid_data', "%s, %s saveframe." % (str(e).strip("'"), sf_framecode))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testDataConsistencyInLoop() ++ ValueError  - %s" % str(e))

                except UserWarning as e:

                    self.report.warning.addDescription('missing_data', "%s, %s saveframe." % (str(e).strip("'"), sf_framecode))
                    self.report.setWarning()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testDataConsistencyInLoop() ++ Warning  - %s" % str(e))

                    # retry allowing zero, range

                    try:
                        data = self.nef_translator.check_data(sf_data, self.lp_categories[file_type][content_subtype], key_items, data_items, allowed_tags, disallowed_tags, False, True)[0]
                    except:
                        pass
                """
                except Exception as e:

                    self.report.error.addDescription('internal_error', "+NmrDpUtility.__testDataConsistencyInLoop() ++ Error  - %s" % str(e))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testDataConsistencyInLoop() ++ Error  - %s" % str(e))
                """
        return not self.report.isError()

    def __testParentChildRelation(self):
        """ Perform consistency test on saveframe category and loop category relationship of interesting loops of NEF/NMR-STAR V3.2 file
        """

        if self.report.isError():
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        for content_subtype in input_source_dic['content_subtype'].keys():

            sf_category = self.sf_categories[file_type][content_subtype]

            list_id = 1

            for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

                sf_framecode = sf_data.get_tag('sf_framecode')[0]

        return self.report.isError()

if __name__ == '__main__':
    dp = NmrDpUtility()
