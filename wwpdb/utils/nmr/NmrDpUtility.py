##
# File: NmrDpUtility.py
# Date: 14-Jun-2019
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
import types
from munkres import Munkres

from wwpdb.utils.nmr.NEFTranslator.NEFTranslator import NEFTranslator
from wwpdb.utils.nmr.NmrDpReport import NmrDpReport
from wwpdb.utils.align.alignlib import PairwiseAlign
from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
from wwpdb.utils.config.ConfigInfo import ConfigInfo, getSiteId
from wwpdb.apps.ccmodule.io.ChemCompIo import ChemCompReader
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

        # auxiliary input resource.
        self.__inputParamDict = {}

        # auxiliary output resource.
        self.__outputParamDict = {}

        # list of known workflow operations
        self.__workFlowOps = ('nmr-nef-consistency-check', 'nmr-str-consistency-check',
                              'nmr-nef2str-deposit', 'nmr-str2str-deposit')

        # dictionary of processing tasks of each workflow operation
        self.__procTasksDict = {'nmr-consistency-check':
                                [self.__initializeDpReport,
                                 self.__instanceNEFTranslator,
                                 self.__instanceBMRBChemShiftStat,
                                 # validate NMR data only
                                 self.__validateInputSource,
                                 self.__detectContentSubType,
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
                                 self.__calculateStatsOfExptlData,
                                 # validate coordinate only
                                 self.__appendCoordinate,
                                 self.__detectCoordContentSubType,
                                 self.__extractCoordPolymerSequence,
                                 self.__extractCoordNonPolymerScheme,
                                 self.__extractCoordPolymerSequenceInLoop,
                                 self.__extractCoordNonStandardResidue,
                                 self.__appendCoordPolymerSequenceAlignment,
                                 # cross-check
                                 self.__assignCoordPolymerSequence,
                                 self.__testCorrdAtomIdConsistency
                                 ]
                                }
        """
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

        # BMRB chemical shift statistics
        self.bmrb_cs_stat = None

        # PyNMRSTAR data
        self.__star_data = None
        self.__star_data_type = None
        self.__sf_category_list = []
        self.__lp_category_list = []

        # empty value
        self.empty_value = (None, '', '.', '?')

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
        self.content_type = {'nef': 'nmr-unified-data',
                             'nmr-star': 'nmr-unified-data',
                             'pdbx': 'model'
                             }

        # paramagnetic elements, except for Oxygen
        self.paramag_elems = {'LI', 'O', 'NA', 'MG', 'AL', 'K', 'CA', 'SC', 'TI', 'V', 'MN', 'RB', 'SR', 'Y', 'ZR', 'NB', 'MO', 'TC', 'RU', 'RH', 'PD', 'SN', 'CS', 'BA', 'LA', 'CE', 'PR', 'ND', 'PM', 'SM', 'EU', 'GD', 'TB', 'DY', 'HO', 'ER', 'TM', 'YB', 'LU', 'HF', 'TA', 'W', 'RE', 'OS', 'IR', 'PT', 'FR', 'RA', 'AC'}\
                                - {'O'}

        # ferromagnetic elements
        self.ferromag_elems = {'CR', 'FE', 'CO', 'NI'}

        # isotope numbers of NMR observable atoms
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
        self.dist_restraint_range = {'min_exclusive': 1.0, 'max_exclusive': 10.0}
        self.dist_restraint_error = {'min_exclusive': 0.0, 'max_exclusive': 5.0}

        # allowed dihed range
        self.dihed_restraint_range = {'min_exclusive': -200.0, 'max_exclusive': 200.0}
        self.dihed_restraint_error = {'min_exclusive': 0.0, 'max_exclusive': 20.0}

        # allowed rdc range
        self.rdc_restraint_range = {'min_exclusive': -50.0, 'max_exclusive': 50.0}
        self.rdc_restraint_error = {'min_exclusive': 0.0, 'max_exclusive': 5.0}

        # allowed weight range
        self.weight_range = {'min_exclusive': 0.0, 'max_inclusive': 10.0}
        # allowed scale range
        self.scale_range = self.weight_range

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
                                   'dist_restraint': [{'name': 'index', 'type':'index-int', 'mandatory': True},
                                                      {'name': 'restraint_id', 'type':'positive-int', 'mandatory': True,
                                                       'enforce-non-zero': True},
                                                      {'name': 'restraint_combination_id', 'type':'positive-int', 'mandatory': False,
                                                       'enforce-non-zero': True},
                                                      {'name': 'weight', 'type':'range-float', 'mandatory': True,
                                                       'range': self.weight_range},
                                                      {'name': 'target_value', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                       'range': self.dist_restraint_range,
                                                       'group': {'member-with': ['lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit'],
                                                                 'coexist-with': None,
                                                                 'smaller-than': ['lower_limit', 'lower_linear_limit'],
                                                                 'larger-than': ['upper_limit', 'upper_linear_limit']}},
                                                      {'name': 'target_value_uncertainty', 'type':'range-float', 'mandatory': False,
                                                       'range': self.dist_restraint_error},
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
                                                       {'name': 'restraint_id', 'type':'index-int', 'mandatory': True},
                                                       {'name': 'restraint_combination_id', 'type':'positive-int', 'mandatory': False,
                                                        'enforce-non-zero': True},
                                                       {'name': 'weight', 'type':'range-float', 'mandatory': True,
                                                        'range': self.weight_range},
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
                                                     {'name': 'restraint_id', 'type':'index-int', 'mandatory': True},
                                                     {'name': 'restraint_combination_id', 'type':'positive-int', 'mandatory': False,
                                                      'enforce-non-zero': True},
                                                     {'name': 'target_value', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                      'range': self.rdc_restraint_range,
                                                      'group': {'member-with': ['lower_linear_limit', 'lower_limit', 'upper_limit', 'upper_linear_limit'],
                                                                'coexist-with': None,
                                                                'smaller-than': ['lower_limit', 'lower_linear_limit'],
                                                                'larger-than': ['upper_limit', 'upper_linear_limit']}},
                                                     {'name': 'target_value_uncertainty', 'type':'range-float', 'mandatory': False,
                                                      'range': self.rdc_restraint_error},
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
                                                     {'name': 'scale', 'type':'range-float', 'mandatory': False,
                                                      'range': self.scale_range},
                                                     {'name': 'distance_dependent', 'type':'bool', 'mandatory': False}
                                                     ],
                                   'spectral_peak': [{'name': 'index', 'type':'index-int', 'mandatory': True},
                                                     {'name': 'peak_id', 'type':'positive-int', 'mandatory': True,
                                                      'enforce-non-zero': True},
                                                     {'name': 'volume', 'type':'float', 'mandatory': False, 'group-mandatory': True,
                                                      'group': {'member-with': ['height'],
                                                                'coexist-with': None}},
                                                     {'name': 'volume_uncertainty', 'type':'positive-float', 'mandatory': False},
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
                                                      'enum': ('start', 'end', 'middle', 'cyclic', 'break', 'single', 'dummy'),
                                                      'enforce-enum': True},
                                                     {'name': 'Cis_residue', 'type': 'bool', 'mandatory': False},
                                                     {'name': 'NEF_index', 'type': 'index-int', 'mandatory': False}
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
                                                       {'name': 'Assigned_chem_shift_list_ID', 'type': 'static-index', 'mandatory': True}
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
                                                           {'name': 'Weight', 'type': 'range-float', 'mandatory': True,
                                                            'range': self.weight_range},
                                                           {'name': 'Auth_asym_ID_1', 'type': 'str', 'mandatory': False},
                                                           {'name': 'Auth_seq_ID_1', 'type': 'int', 'mandatory': False},
                                                           {'name': 'Auth_comp_ID_1', 'type': 'str', 'mandatory': False},
                                                           {'name': 'Auth_atom_ID_1', 'type': 'str', 'mandatory': False},
                                                           {'name': 'Auth_asym_ID_2', 'type': 'str', 'mandatory': False},
                                                           {'name': 'Auth_seq_ID_2', 'type': 'int', 'mandatory': False},
                                                           {'name': 'Auth_comp_ID_2', 'type': 'str', 'mandatory': False},
                                                           {'name': 'Auth_atom_ID_2', 'type': 'str', 'mandatory': False},
                                                           {'name': 'Gen_dist_constraint_list_ID', 'type': 'static-index', 'mandatory': True},
                                                           ],
                                        'dihed_restraint': [{'name': 'Index_ID', 'type':'index-int', 'mandatory': True},
                                                            {'name': 'ID', 'type':'index-int', 'mandatory': True},
                                                            {'name': 'Combination_ID', 'type':'positive-int', 'mandatory': False,
                                                             'enforce-non-zero': True},
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
                                                            {'name': 'Angle_target_val_err', 'type':'range-float', 'mandatory': False,
                                                             'range': self.dihed_restraint_error},
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
                                                            {'name': 'Weight', 'type':'range-float', 'mandatory': True,
                                                             'range': self.weight_range},
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
                                                            {'name': 'Torsion_angle_constraint_list_ID', 'type':'static-index', 'mandatory': True},
                                            ],
                                        'rdc_restraint': [{'name': 'Index_ID', 'type':'index-int', 'mandatory': True},
                                                          {'name': 'ID', 'type':'index-int', 'mandatory': True},
                                                          {'name': 'Combination_ID', 'type':'positive-int', 'mandatory': False,
                                                           'enforce-non-zero': True},
                                                          {'name': 'Weight', 'type':'range-float', 'mandatory': True,
                                                           'range': self.weight_range},
                                                          {'name': 'Target_value', 'type':'range-float', 'mandatory': False, 'group-mandatory': True,
                                                           'range': self.dihed_restraint_range,
                                                           'group': {'member-with': ['RDC_lower_linear_limit', 'RDC_upper_linear_limit', 'RDC_lower_bound', 'RDC_upper_bound'],
                                                                     'coexist-with': None,
                                                                     'smaller-than': ['RDC_lower_linear_limit', 'RDC_lower_bound'],
                                                                     'larger-than': ['RDC_upper_linear_limit', 'RDC_upper_bound']}},
                                                          {'name': 'Target_value_uncertainty', 'type':'range-float', 'mandatory': False,
                                                           'range': self.rdc_restraint_error},
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
                                                          {'name': 'RDC_val_scale_factor', 'type':'range-float', 'mandatory': False,
                                                           'range': self.scale_range},
                                                          {'name': 'RDC_distant_dependent', 'type':'bool', 'mandatory': False},
                                                          {'name': 'Auth_asym_ID_1', 'type':'str', 'mandatory': False},
                                                          {'name': 'Auth_seq_ID_1', 'type':'int', 'mandatory': False},
                                                          {'name': 'Auth_comp_ID_1', 'type':'str', 'mandatory': False},
                                                          {'name': 'Auth_atom_ID_1', 'type':'str', 'mandatory': False},
                                                          {'name': 'Auth_asym_ID_2', 'type':'str', 'mandatory': False},
                                                          {'name': 'Auth_seq_ID_2', 'type':'int', 'mandatory': False},
                                                          {'name': 'Auth_comp_ID_2', 'type':'str', 'mandatory': False},
                                                          {'name': 'Auth_atom_ID_2', 'type':'str', 'mandatory': False},
                                                          {'name': 'RDC_constraint_list_ID', 'type':'static-index', 'mandatory': True}
                                                          ],
                                        'spectral_peak': [{'name': 'Index_ID', 'type':'index-int', 'mandatory': True},
                                                          {'name': 'ID', 'type':'positive-int', 'mandatory': True,
                                                           'enforce-non-zero': True},
                                                          {'name': 'Volume', 'type':'float', 'mandatory': False, 'group-mandatory': True,
                                                           'group': {'member-with': ['Height'],
                                                                     'coexist-with': None}},
                                                          {'name': 'Volume_uncertainty', 'type':'positive-float', 'mandatory': False},
                                                          {'name': 'Height', 'type':'float', 'mandatory': False, 'group-mandatory': True,
                                                           'group': {'member-with': ['Volume'],
                                                                     'coexist-with': None}},
                                                          {'name': 'Height_uncertainty', 'type':'positive-float', 'mandatory': False},
                                                          {'name': 'Spectral_peak_list_ID', 'type':'static-index', 'mandatory': True}
                                                          ]
                                        }
                           }

        # loop data items for spectral peak
        self.pk_data_items = {'nef': [{'name': 'position_uncertainty_%s', 'type':'range-float', 'mandatory': False,
                                       'range': self.chem_shift_error},
                                      {'name': 'chain_code_%s', 'type':'str', 'mandatory': False,
                                       'relax-key-if-exist': True},
                                      {'name': 'sequence_code_%s', 'type':'int', 'mandatory': False,
                                       'relax-key-if-exist': True},
                                      {'name': 'residue_name_%s', 'type':'str', 'mandatory': False,
                                       'relax-key-if-exist': True},
                                      {'name': 'atom_name_%s', 'type':'str', 'mandatory': False,
                                       'relax-key-if-exist': True}],
                              'nmr-star': [{'name': 'Position_uncertainty_%s', 'type':'range-float', 'mandatory': False,
                                            'range': self.chem_shift_error},
                                           {'name': 'Entity_assembly_ID_%s', 'type':'positive-int', 'mandatory': False,
                                            'enforce-non-zero': True,
                                            'relax-key-if-exist': True},
                                           {'name': 'Comp_index_ID_%s', 'type':'int', 'mandatory': False,
                                            'relax-key-if-exist': True},
                                           {'name': 'Comp_ID_%s', 'type':'str', 'mandatory': False,
                                            'relax-key-if-exist': True},
                                           {'name': 'Atom_ID_%s', 'type':'str', 'mandatory': False,
                                            'relax-key-if-exist': True},
                                           {'name': 'Auth_asym_ID_%s', 'type':'str', 'mandatory': False},
                                           {'name': 'Auth_seq_ID_%s', 'type':'int', 'mandatory': False},
                                           {'name': 'Auth_comp_ID_%s', 'type':'str', 'mandatory': False},
                                           {'name': 'Auth_atom_ID_%s', 'type':'str', 'mandatory': False}]
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
                                              'isotope_number': 'isotope_number'},
                                      'nmr-star': {'chain_id': 'Entity_assembly_ID',
                                                   'seq_id': 'Comp_index_ID',
                                                   'comp_id': 'Comp_ID',
                                                   'atom_id': 'Atom_ID',
                                                   'value': 'Val',
                                                   'error': 'Val_err',
                                                   'atom_type': 'Atom_type',
                                                   'isotope_number': 'Atom_isotope_number'}
                                      }

        # item name in spectral peak loop
        self.item_names_in_pk_loop = {'nef': {'chain_id': 'chain_code_%s',
                                              'seq_id': 'sequence_code_%s',
                                              'comp_id': 'residue_name_%s',
                                              'atom_id': 'atom_name_%s',
                                              'position': 'position_%s'},
                                      'nmr-star': {'chain_id': 'Entity_assembly_ID_%s',
                                                   'seq_id': 'Comp_index_ID_%s',
                                                   'comp_id': 'Comp_ID_%s',
                                                   'atom_id': 'Atom_ID_%s',
                                                   'position': 'Position_%s'}
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
                         'U': 'U'}

        # main contents of loops
        self.lp_data = {'poly_seq': [],
                        'chem_shift': [],
                        'dist_restraint': [],
                        'dihed_restraint': [],
                        'rdc_restraint': [],
                        'spectral_peak': []
                        }

        # auxiliary contents of loops
        self.aux_data = {'poly_seq': [],
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

        if 'consistency-check' in op:

            for task in self.__procTasksDict['nmr-consistency-check']:

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
                    pass

        if 'consistency-check' in op:

            for task in self.__procTasksDict['nmr-consistency-check']:

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.op() starting op %s - task %s\n" % (op, task.__name__))

                if not task():
                    pass

        self.report.writeJson(self.__logPath)

        return not self.report.isError()

    def __initializeDpReport(self):
        """ Initialize NMR data processing report.
        """

        self.report = NmrDpReport()

        # set primary input source as NMR unified data
        input_source = self.report.input_sources[0]

        file_type = 'nef' if 'nef' in self.__op else 'nmr-star'
        content_type = self.content_type[file_type]

        input_source.setItemValue('file_name', os.path.basename(self.__srcPath))
        input_source.setItemValue('file_type', file_type)
        input_source.setItemValue('content_type', content_type)

        self.__testDiamagnetism()

        return input_source is not None

    def __testDiamagnetism(self):
        """ Test diamagnetism of molecular assembly.
        """

        if 'coordinate_file_path' in self.__inputParamDict:

            try:

                if not self.__cR.setFilePath(file_path) or not self.__cR.parse():
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

    def __instanceNEFTranslator(self):
        """ Instance NEFTanslator.
        """

        self.nef_translator = NEFTranslator()

        if self.nef_translator is None:

            err = "+NmrDpUtility.__instanceNEFTranslator() ++ Error - NEFTranslator is not available."

            self.report.error.appendDescription('internal_error', err)
            self.report.setError()

            if self.__verbose:
                self.__lfh.write(err + '\n')

            return False

        return True

    def __instanceBMRBChemShiftStat(self):
        """ Instance BMRBChemShiftStat.
        """

        self.bmrb_cs_stat = BMRBChemShiftStat()

        if self.bmrb_cs_stat.isOk():
            return True

        err = "+NmrDpUtility.__instanceBMRBChemShiftStat() ++ Error - BMRB chemical shift statistics is not available."

        self.report.error.appendDescription('internal_error', err)
        self.report.setError()

        if self.__verbose:
            self.__lfh.write(err + '\n')

        return False

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

                err = "%s was selected as %s file, but recognized as %s file." % (file_name, self.readable_file_type[file_type], self.readable_file_type[_file_type])

                if len(message['error']) > 0:
                    for error_message in message['error']:
                        err += err_message

                self.report.error.appendDescription('format_issue', {'file_name': file_name, 'description': err})
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__validateInputSource() ++ Error  - %s\n" % err)

                return False

            return True

        else:

            err = "%s is invalid %s file." % (file_name, self.readable_file_type[file_type])

            if len(message['error']) > 0:
                for error_message in message['error']:
                    err += err_message

            self.report.error.appendDescription('format_issue', {'file_name': file_name, 'description': err})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__validateInputSource() ++ Error  - %s\n" % err)

            return False

    def __detectContentSubType(self):
        """ Detect content subtypes.
        """

        if self.report.isError():
            return False

        is_done, self.__star_data_type, self.__star_data = self.nef_translator.read_input_file(self.__srcPath) # NEFTranslator.validate_file() generates this object internally, but not re-used.

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        self.__sf_category_list, self.__lp_category_list = self.nef_translator.get_data_content(self.__star_data, self.__star_data_type)

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
            return self.nef_translator.get_nef_seq(sf_data, lp_category=self.lp_categories[file_type][content_subtype], allow_empty=(content_subtype == 'spectral_peak'))
        else:
            return self.nef_translator.get_star_seq(sf_data, lp_category=self.lp_categories[file_type][content_subtype], allow_empty=(content_subtype == 'spectral_peak'))

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
                auth_poly_seq = self.nef_translator.get_star_auth_seq(sf_data, lp_category)[0]

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

                                    self.report.warning.appendDescription('sequence_mismatch', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': warn})
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

                                        self.report.warning.appendDescription('sequence_mismatch', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': warn})
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

                                self.report.warning.appendDescription('sequence_mismatch', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': warn})
                                self.report.setWarning()

                                if self.__verbose:
                                    self.__lfh.write("+NmrDpUtility.__extractPolymerSequence() ++ Warning  - %s\n" % warn)

                                break

            return True

        except KeyError as e:

            self.report.error.appendDescription('sequence_mismatch', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__extractPolymerSequence() ++ KeyError  - %s" % str(e))

        except LookupError as e:

            self.report.error.appendDescription('missing_mandatory_item', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__extractPolymerSequence() ++ LookupError  - %s" % str(e))

        except ValueError as e:

            self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
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

                        list_id += 1
                        has_poly_seq = True

                        if file_type == 'nmr-star':
                            auth_poly_seq = self.nef_translator.get_star_auth_seq(sf_data, lp_category)[0]

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

                                                self.report.warning.appendDescription('sequence_mismatch', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': warn})
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

                                                    self.report.warning.appendDescription('sequence_mismatch', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': warn})
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

                                            self.report.warning.appendDescription('sequence_mismatch', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': warn})
                                            self.report.setWarning()

                                            if self.__verbose:
                                                self.__lfh.write("+NmrDpUtility.__extractPolymerSequenceInLoop() ++ Warning  - %s\n" % warn)

                                            break

                except KeyError as e:

                    self.report.error.appendDescription('sequence_mismatch', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__extractPolymerSequenceInLoop() ++ KeyError  - %s" % str(e))

                except LookupError as e:

                    self.report.error.appendDescription('missing_mandatory_item', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__extractPolymerSequenceInLoop() ++ LookupError  - %s" % str(e))

                except ValueError as e:

                    self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__extractPolymerSequenceInLoop() ++ ValueError  - %s" % str(e))

                except Exception as e:

                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__extractPolymerSequenceInLoop() ++ Error  - %s" % str(e))
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

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

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

            lp_category1 = self.lp_categories[file_type][subtype1]
            lp_category2 = self.lp_categories[file_type][subtype2]

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

                            err = "Invalid chain_id %s exists." % cid

                            self.report.error.appendDescription('sequence_mismatch', {'file_name': file_name, 'saveframe': sf_framecode2, 'category': lp_category2, 'description': err})
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__testSequenceConsistency() ++ Error  - %s\n" % err)

                        else:

                            for s1 in ps1:

                                if s1['chain_id'] != s2['chain_id']:
                                    continue

                                for j in range(len(s2['seq_id'])):
                                    sid = s2['seq_id'][j]
                                    seq = s2['comp_id'][j]

                                    if not sid in s1['seq_id']:

                                        err = "Invalid seq_id %s (chain_id %s) exists." % (sid, cid)

                                        self.report.error.appendDescription('sequence_mismatch', {'file_name': file_name, 'saveframe': sf_framecode2, 'category': lp_category2, 'description': err})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__testSequenceConsistency() ++ Error  - %s\n" % err)

                                    else:
                                        i = s1['seq_id'].index(sid)

                                        if seq != s1['comp_id'][i]:

                                            err = "Invalid comp_id %s vs %s (seq_id %s, chain_id %s) exists." % (seq, s1['comp_id'][i], sid, cid)

                                            self.report.error.appendDescription('sequence_mismatch', {'file_name': file_name, 'saveframe': sf_framecode2, 'category': lp_category2, 'description': err})
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

                                            err = "Unmatched comp_id %s vs %s (seq_id %s, chain_id %s) exists against %s saveframe." % (seq, s1['comp_id'][i], sid, cid, sf_framecode1)

                                            self.report.error.appendDescription('sequence_mismatch', {'file_name': file_name, 'saveframe': sf_framecode2, 'category': lp_category2, 'description': err})
                                            self.report.setError()

                                            if self.__verbose:
                                                self.__lfh.write("+NmrDpUtility.__testSequenceConsistency() ++ Error  - %s\n" % err)

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

                                            err = "Unmatched comp_id %s vs %s (seq_id %s, chain_id %s) exists against %s saveframe." % (seq, s2['comp_id'][j], sid, cid, sf_framecode2)

                                            self.report.error.appendDescription('sequence_mismatch', {'file_name': file_name, 'saveframe': sf_framecode1, 'category': lp_category1, 'description': err})
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
                asm.append({'chain_id': cid, 'seq_id': [int(i.split(' ')[0]) for i in sorted_poly_seq], 'comp_id': [i.split(' ')[1] for i in sorted_poly_seq]})

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
            return True

        polymer_sequence = input_source_dic['polymer_sequence']

        asm_has = False

        asm = []

        for s in polymer_sequence:

            ent_has = False

            ent = {'chain_id': s['chain_id'], 'seq_id': [], 'comp_id': []}

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
        """ Append polymer sequence alignment of interesting loops.
        """

        if self.report.isError():
            return False

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        has_poly_seq = 'polymer_sequence' in input_source_dic
        has_poly_seq_in_loop = 'polymer_sequence_in_loop' in input_source_dic

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

                        self.__pA.setReferenceSequence(s1['comp_id'], 'REF' + cid)
                        self.__pA.addTestSequence(_s2['comp_id'], cid)
                        self.__pA.doAlign()
                        #self.__pA.prAlignmentConflicts(cid)
                        myAlign = self.__pA.getAlignment(cid)

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
                                     'chain_id': cid, 'length': length, 'conflict': conflicts, 'sequence_coverage': float('{:.3f}'.format(float(length - conflicts) / float(length))), 'ref_seq_id': s1['seq_id'], 'reference_seq': ref_seq, 'middle_code': mid_seq, 'test_seq': tst_seq}

                        seq_align_set.append(seq_align)

                if has_seq_align:
                    self.report.sequence_alignment.setItemValue('nmr_poly_seq_vs_' + subtype, seq_align_set)

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

    def __getMiddleCode(self, ref_seq, tst_seq):
        """ Return array of middle code of sequence alignment.
        """

        array = ''

        for i in range(len(ref_seq)):
            array += '|' if ref_seq[i] == tst_seq[i] else ' '

        return array

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
                        pairs = self.nef_translator.get_nef_comp_atom_pair(sf_data, lp_category,
                                                                           allow_empty=(content_subtype == 'spectral_peak'))[0]
                    else:
                        pairs = self.nef_translator.get_star_comp_atom_pair(sf_data, lp_category,
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

                                        err = "Invalid atom_id %s (comp_id %s) exists." % (atom_id, comp_id)

                                        self.report.error.appendDescription('invalid_atom_nomenclature', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__validateAtomNomenclature() ++ Error  - %s\n" % err)

                                    else:
                                        _atom_ids.extend(_atom_id)

                                atom_ids = sorted(set(_atom_ids))

                            for atom_id in atom_ids:

                                if not self.nef_translator.validate_comp_atom(comp_id, atom_id):

                                    err = "Invalid atom_id %s (comp_id %s) exists." % (atom_id, comp_id)

                                    self.report.error.appendDescription('invalid_atom_nomenclature', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                                    self.report.setError()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__validateAtomNomenclature() ++ Error  - %s\n" % err)

                        # non-standard residue
                        else:
                            self.__updateChemCompDict(comp_id)

                            if self.__last_comp_id_test: # matches with comp_id in CCD

                                ref_atom_ids = [a[self.__cca_atom_id] for a in self.__last_chem_comp_atoms if a[self.__cca_leaving_atom_flag] != 'Y']
                                unk_atom_ids = []

                                for atom_id in atom_ids:

                                    if not atom_id in ref_atom_ids:
                                        unk_atom_ids.append(atom_id)

                                if len(unk_atom_ids) > 0:
                                    cc_name = self.__last_chem_comp_dict['_chem_comp.name']

                                    warn = "Unknown atom_id %s (comp_id %s, comp_name %s) exist." % (unk_atom_ids, comp_id, cc_name)

                                    self.report.warning.appendDescription('atom_nomenclature_mismatch', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': warn})
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
                        auth_pairs = self.nef_translator.get_star_auth_comp_atom_pair(sf_data, lp_category)[0]

                        for auth_pair in auth_pairs:
                            comp_id = auth_pair['comp_id']
                            auth_atom_ids = auth_pair['atom_id']

                            # standard residue
                            if self.nef_translator.get_one_letter_code(comp_id) != '?':

                                _auth_atom_ids = []
                                for auth_atom_id in auth_atom_ids:

                                    _auth_atom_id = self.nef_translator.get_nmrstar_atom(comp_id, auth_atom_id)[1]

                                    if len(_auth_atom_id) == 0:

                                        warn = "Unmatched author atom ID %s (auth_comp_id %s) exists." % (auth_atom_id, comp_id)

                                        self.report.warning.appendDescription('atom_nomenclature_mismatch', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': warn})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__validateAtomNomenclature() ++ Warning  - %s\n" % warn)

                                    else:
                                        _auth_atom_ids.extend(_auth_atom_id)

                                auth_atom_ids = sorted(set(_auth_atom_ids))

                                for auth_atom_id in auth_atom_ids:

                                    if not self.nef_translator.validate_comp_atom(comp_id, auth_atom_id):

                                        warn = "Unmatched author atom ID %s (auth_comp_id %s) exists." % (auth_atom_id, comp_id)

                                        self.report.warning.appendDescription('atom_nomenclature_mismatch', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': warn})
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

                                        self.report.warning.appendDescription('atom_nomenclature_mismatch', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': warn})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__validateAtomNomenclature() ++ Warning  - %s\n" % warn)

                                    break

                                if not has_comp_id:

                                        warn = "Unmatched author atom ID %s (auth_comp_id %s, non-standard residue) exists." % (auth_atom_ids, comp_id)

                                        self.report.warning.appendDescription('atom_nomenclature_mismatch', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': warn})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__validateAtomNomenclature() ++ Warning  - %s\n" % warn)

                except LookupError as e:

                    self.report.error.appendDescription('missing_mandatory_item', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__validateAtomNomenclature() ++ LookupError  - %s" % str(e))

                except ValueError as e:

                    self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
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
                    a_types = self.nef_translator.get_nef_atom_type_from_cs_loop(sf_data)[0]
                else:
                    a_types = self.nef_translator.get_star_atom_type_from_cs_loop(sf_data)[0]

                for a_type in a_types:
                    atom_type = a_type['atom_type']
                    isotope_nums = a_type['isotope_number']
                    atom_ids = a_type['atom_id']

                    if not atom_type in self.atom_isotopes.keys():

                        err = "Invalid atom_type %s exists." % atom_type

                        self.report.error.appendDescription('invalid_atom_type', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__validateAtomTypeOfCSLoop() ++ Error  - %s\n" % err)

                    else:
                        for isotope_num in isotope_nums:
                            if not isotope_num in self.atom_isotopes[atom_type]:

                                err = "Invalid isotope number %s (atom_type %s, allowed isotope number %s) exists." % (isotope_num, atom_type, self.atom_isotopes[atom_type])

                                self.report.error.appendDescription('invalid_isotope_number', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write("+NmrDpUtility.__validateAtomTypeOfCSLoop() ++ Error  - %s\n" % err)

                        for atom_id in atom_ids:
                            if not atom_id.startswith(atom_type):

                                err = "Invalid atom_id %s (atom_type %s) exists." % (atom_id, atom_type)

                                self.report.error.appendDescription('invalid_atom_nomenclature', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write("+NmrDpUtility.__validateAtomTypeOfCSLoop() ++ Error  - %s\n" % err)

            except LookupError as e:

                self.report.error.appendDescription('missing_mandatory_item', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__validateAtomTypeOfCSLoop() ++ LookupError  - %s" % str(e))

            except ValueError as e:

                self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
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

                a_codes = self.nef_translator.get_star_ambig_code_from_cs_loop(sf_data)[0]

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

                            allowed_ambig_code = self.bmrb_cs_stat.getMaxAmbigCodeWoSetId(comp_id, atom_id)

                            if ambig_code > allowed_ambig_code:

                                err = "Invalid ambiguity code %s (comp_id %s, atom_id %s, allowed ambig_code %s) exists." % (ambig_code, comp_id, atom_id, [1, allowed_ambig_code, 4, 5, 6, 9])

                                self.report.error.appendDescription('invalid_ambiguity_code', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write("+NmrDpUtility.__testAmbigCodeOfCSLoop() ++ Error  - %s\n" % err)

                if len(comp_ids_wo_ambig_code) > 0:

                    warn = "Missing ambiguity code for the following residues %s." % comp_ids_wo_ambig_code

                    self.report.warning.appendDescription('missing_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': warn})
                    self.report.setWarning()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testAmbigCodeOfCSLoop() ++ Warning  - %s\n" % warn)

            except LookupError as e:

                self.report.error.appendDescription('missing_mandatory_item', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__testAmbigCodeOfCSLoop() ++ LookupError  - %s" % str(e))

            except ValueError as e:

                self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
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

                    indices = self.nef_translator.get_index(sf_data, lp_category, index_id=index_tag)[0]

                    if indices != range(1, len(indices) + 1):

                        warn = "Index (loop tag %s.%s) is disordered." % (lp_category, index_tag)

                        self.report.warning.appendDescription('disordered_index', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': warn})
                        self.report.setWarning()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__testIndexConsistency() ++ Warning  - %s\n" % warn)

                except KeyError as e:

                    self.report.error.appendDescription('duplicated_index', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testIndexConsistency() ++ KeyError  - %s" % str(e))

                except LookupError as e:

                    self.report.error.appendDescription('missing_mandatory_item', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testIndexConsistency() ++ LookupError  - %s" % str(e))

                except ValueError as e:

                    self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
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

                    lp_data = self.nef_translator.check_data(sf_data, lp_category, key_items, data_items, allowed_tags, disallowed_tags,
                                                             inc_idx_test=True, enforce_non_zero=True, enforce_enum=True)[0]

                    self.lp_data[content_subtype].append({'sf_framecode': sf_framecode, 'data': lp_data})

                except KeyError as e:

                    self.report.error.appendDescription('multiple_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testDataConsistencyInLoop() ++ KeyError  - %s" % str(e))

                except LookupError as e:

                    self.report.error.appendDescription('missing_mandatory_item', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testDataConsistencyInLoop() ++ LookupError  - %s" % str(e))

                except ValueError as e:

                    self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testDataConsistencyInLoop() ++ ValueError  - %s" % str(e))

                except UserWarning as e:

                    warn = str(e).strip("'")

                    zero = warn.startswith('[ZERO] ')
                    enum = warn.startswith("[ENUM] ")

                    if zero or enum:

                        warn = warn[7:]

                        self.report.warning.appendDescription('missing_data' if zero else 'enum_failure', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': warn})
                        self.report.setWarning()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__testDataConsistencyInLoop() ++ Warning  - %s\n" % warn)

                        # try to parse data without constraints

                        try:

                            lp_data = self.nef_translator.check_data(sf_data, lp_category, key_items, data_items, allowed_tags, disallowed_tags,
                                                                     inc_idx_test=False, enforce_non_zero=False, enforce_enum=False)[0]

                            self.lp_data[content_subtype].append({'sf_framecode': sf_framecode, 'data': lp_data})

                        except:
                            pass

                    else:

                        self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testDataConsistencyInLoop() ++ Error  - %s" % str(e))
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__testDataConsistencyInLoop() ++ Error  - %s" % str(e))

                except Exception as e:

                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testDataConsistencyInLoop() ++ Error  - %s" % str(e))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testDataConsistencyInLoop() ++ Error  - %s" % str(e))

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

                        self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__testDataConsistencyInAuxLoop() ++ ValueError  - %s\n" % err)

                loops = sf_data.loops

                for loop in loops:

                    lp_category = loop.category

                    # main content of loop has been processed in __testDataConsistencyInLoop()
                    if lp_category in self.lp_categories[file_type][content_subtype]:
                        continue

                    elif lp_category in self.aux_lp_categories[file_type][content_subtype]:

                        key_items = self.aux_key_items[file_type][content_subtype][lp_category]
                        data_items = self.aux_data_items[file_type][content_subtype][lp_category]
                        allowed_tags = self.aux_allowed_tags[file_type][content_subtype][lp_category]

                        try:

                            aux_data = self.nef_translator.check_data(sf_data, lp_category, key_items, data_items, allowed_tags, None,
                                                                      inc_idx_test=True, enforce_non_zero=True, enforce_enum=True)[0]

                            self.aux_data[content_subtype].append({'sf_framecode': sf_framecode, 'lp_category': lp_category, 'data': aux_data})

                            if content_subtype == 'spectral_peak':
                                self.__testDataConsistencyInAuxLoopOfSpectralPeak(file_name, file_type, sf_framecode, num_dim, lp_category, aux_data)

                        except KeyError as e:

                            self.report.error.appendDescription('multiple_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__testDataConsistencyInAuxLoop() ++ KeyError  - %s" % str(e))

                        except LookupError as e:

                            self.report.error.appendDescription('missing_mandatory_item', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__testDataConsistencyInAuxLoop() ++ LookupError  - %s" % str(e))

                        except ValueError as e:

                            self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': str(e).strip("'")})
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__testDataConsistencyInAuxLoop() ++ ValueError  - %s" % str(e))

                        except UserWarning as e:

                            warn = str(e).strip("'")

                            zero = warn.startswith('[ZERO] ')
                            enum = warn.startswith("[ENUM] ")

                            if zero or enum:

                                warn = warn[7:]

                                self.report.warning.appendDescription('missing_data' if zero else 'enum_failure', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': warn})
                                self.report.setWarning()

                                if self.__verbose:
                                    self.__lfh.write("+NmrDpUtility.__testDataConsistencyInAuxLoop() ++ Warning  - %s\n" % warn)

                                # try to parse data without constraints

                                try:

                                    aux_data = self.nef_translator.check_data(sf_data, lp_category, key_items, data_items, allowed_tags, None,
                                                                              inc_idx_test=True, enforce_non_zero=False, enforce_enum=False)[0]

                                    self.aux_data[content_subtype].append({'sf_framecode': sf_framecode, 'lp_category': lp_category, 'data': aux_data})

                                    if content_subtype == 'spectral_peak':
                                        self.__testDataConsistencyInAuxLoopOfSpectralPeak(file_name, file_type, sf_framecode, num_dim, lp_category, aux_data)

                                except:
                                    pass

                            else:

                                self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testDataConsistencyInAuxLoop() ++ Error  - %s" % str(e))
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write("+NmrDpUtility.__testDataConsistencyInAuxLoop() ++ Error  - %s" % str(e))

                        except Exception as e:

                            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testDataConsistencyInAuxLoop() ++ Error  - %s" % str(e))
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__testDataConsistencyInAuxLoop() ++ Error  - %s" % str(e))

                    elif lp_category in self.linked_lp_categories[file_type][content_subtype]:

                        warn = "Unsupported %s loop category exists." % lp_category

                        self.report.warning.appendDescription('skipped_lp_category', {'file_name': file_name, 'saveframe': sf_framecode, 'description': warn})
                        self.report.setWarning()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__testDataConsistencyInAuxLoop() ++ Warning  - %s\n" % warn)

                    else:

                        err = "%s loop category exists unexpectedly." % loop.category

                        self.report.error.appendDescription('format_issue', {'file_name': file_name, 'saveframe': sf_framecode, 'description': err})
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
                self.report.error.appendDescription('missing_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
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

                lp_data = next((l['data'] for l in self.lp_data[content_subtype] if l['sf_framecode'] == sf_framecode), None)

                if not lp_data is None:
                    for i in lp_data:
                        for j in range(num_dim):
                            position = i[position_names[j]]

                            if position < min_points[j] or position > max_points[j]:

                                err = '[Check row of %s %s] %s %s is out of range (min_position %s, max_position %s).' % (index_tag, i[index_tag], position_names[j], position, min_points[j], max_points[j])

                                self.report.error.appendDescription('anomalous_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
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

                        self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
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

                    sf_tag_data = self.nef_translator.check_sf_tag(sf_data, self.sf_tag_items[file_type][content_subtype], self.sf_allowed_tags[file_type][content_subtype],
                                                            enforce_non_zero=True, enforce_enum=True)

                    self.__testParentChildRelation(file_name, file_type, content_subtype, parent_keys, list_id, sf_framecode, sf_tag_data)

                    list_id += 1

                except LookupError as e:

                    self.report.error.appendDescription('missing_mandatory_item', {'file_name': file_name, 'saveframe': sf_framecode, 'description': str(e).strip("'")})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testSfTagConsistency() ++ LookupError  - %s" % str(e))

                except ValueError as e:

                    self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'saveframe': sf_framecode, 'description': str(e).strip("'")})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testSfTagConsistency() ++ ValueError  - %s" % str(e))

                except UserWarning as e:

                    warn = str(e).strip("'")

                    zero = warn.startswith("[ZERO] ")
                    enum = warn.startswith("[ENUM] ")

                    if zero or enum:

                        warn = warn[7:]

                        self.report.warning.appendDescription('missing_data' if zero else 'enum_failure', {'file_name': file_name, 'saveframe': sf_framecode, 'description': warn})
                        self.report.setWarning()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__testSfTagConsistency() ++ Warning  - %s\n" % warn)

                        # try to parse data without constraints

                        try:

                            sf_tag_data = self.nef_translator.check_sf_tag(sf_data, self.sf_tag_items[file_type][content_subtype], self.sf_allowed_tags[file_type][content_subtype],
                                                                    enfoce_non_zero=False, enforce_enum=False)

                            self.__testParentChildRelation(file_name, file_type, content_subtype, parent_keys, list_id, sf_framecode, sf_tag_data)

                            list_id += 1

                        except:
                            pass

                    else:

                        self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testSfTagConsistency() ++ Error  - %s" % str(e))
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__testSfTagConsistency() ++ Error  - %s" % str(e))

                except Exception as e:

                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testSfTagConsistency() ++ Error  - %s" % str(e))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__testSfTagConsistency() ++ Error  - %s" % str(e))

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

            self.report.error.appendDescription('duplicated_index', {'file_name': file_name, 'saveframe': sf_framecode, 'description': err})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__testParentChildRelation() ++ KeyError  - %s\n" % err)

        index_tag = self.index_tags[file_type][content_subtype]
        lp_category = self.lp_categories[file_type][content_subtype]

        try:

            lp_data = next((l['data'] for l in self.lp_data[content_subtype] if l['sf_framecode'] == sf_framecode), None)

            if not lp_data is None:
                for i in lp_data:
                    if child_key_name in i and i[child_key_name] != parent_key:

                        err = '[Check row of %s %s] %s %s must be %s.' % (index_tag, i[index_tag], child_key_name, i[child_key_name], parent_key)

                        self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__testParentChildRelation() ++ ValueError  - %s\n" % err)

            for lp_category in self.aux_lp_categories[file_type][content_subtype]:

                aux_data = next((l['data'] for l in self.aux_data[content_subtype] if l['sf_framecode'] == sf_framecode and l['lp_category'] == lp_category), None)

                if not aux_data is None:
                    for i in aux_data:
                        if child_key_name in i and i[child_key_name] != parent_key:

                            err = '[Check row of %s %s] %s %s must be %s.' % (index_tag, i[index_tag], child_key_name, i[child_key_name], parent_key)

                            self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
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

        index_tag = self.index_tags[file_type][content_subtype]
        max_cs_err = self.chem_shift_error['max_exclusive']

        for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

            sf_framecode = sf_data.get_tag('sf_framecode')[0]

            try:

                lp_data = next(l['data'] for l in self.lp_data[content_subtype] if l['sf_framecode'] == sf_framecode)

                item_names = self.item_names_in_cs_loop[file_type]
                value_name = item_names['value']
                ambig_code_name = 'Ambiguity_code'

                chk_row_tmp = "[Check row of {0} %s, {1} %s, {2} %s, {3} %s".format(item_names['chain_id'], item_names['seq_id'], item_names['comp_id'], item_names['atom_id'])
                row_tmp = "{0} %s, {1} %s, {2} %s, {3} %s".format(item_names['chain_id'], item_names['seq_id'], item_names['comp_id'], item_names['atom_id'])

                methyl_cs_vals = {}

                for i in lp_data:
                    chain_id = i[item_names['chain_id']]
                    seq_id = i[item_names['seq_id']]
                    comp_id = i[item_names['comp_id']]
                    atom_id = i[item_names['atom_id']]
                    value = i[value_name]

                    one_letter_code = self.__get1LetterCode(comp_id)

                    has_cs_stat = False

                    # non-standard residue
                    if one_letter_code == 'X':

                        neighbor_comp_ids = set([j[item_names['comp_id']] for j in lp_data if j[item_names['chain_id']] == chain_id and abs(j[item_names['seq_id']] - seq_id) < 3 and j[item_names['seq_id']] != seq_id])

                        polypeptide_like = False

                        for comp_id2 in neighbor_comp_ids:
                            polypeptide_like |= self.bmrb_cs_stat.getTypeOfCompId(comp_id2)[0]

                        for cs_stat in self.bmrb_cs_stat.get(comp_id):

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

                                        err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) + '] Chemical shift values in the same methyl group %s %s vs %s are inconsistent.' %\
                                              (value_name, value, methyl_cs_vals[methyl_cs_key])

                                        self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError  - %s\n" % err)

                                        break

                                if std_value is None:

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) + '] Insufficient chemical shift statistics is available to verify %s %s (avg %s).' %\
                                           (value_name, value, avg_value)

                                    self.report.warning.appendDescription('unusual_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': warn})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ Warning  - %s\n" % warn)

                                    break

                                z_score = (value - avg_value) / std_value

                                if self.bmrb_cs_stat.hasEnoughStat(comp_id, polypeptide_like):
                                    tolerance = std_value

                                    if value < min_value - tolerance or value > max_value + tolerance:

                                        err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) + '] %s %s is out of range (avg %s, std %s, min %s, max %s, Z_score %.2f).' %\
                                              (value_name, value, avg_value, std_value, min_value, max_value, z_score)

                                        self.report.error.appendDescription('anomalous_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError  - %s\n" % err)

                                    elif abs(z_score) > 7.5:

                                        warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) + '] %s %s must be verified (avg %s, std %s, min %s, max %s, Z_score %.2f).' %\
                                               (value_name, value, avg_value, std_value, min_value, max_value, z_score)

                                        self.report.warning.appendDescription('suspicious_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': warn})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ Warning  - %s\n" % warn)

                                    elif abs(z_score) > 5.3:

                                        warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) + '] %s %s should be verified (avg %s, std %s, min %s, max %s, Z_score %.2f).' %\
                                               (value_name, value, avg_value, std_value, min_value, max_value, z_score)

                                        self.report.warning.appendDescription('unusual_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': warn})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ Warning  - %s\n" % warn)

                                    elif not cs_stat['primary']:

                                        warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) + '] %s %s is remarkable assignment (appearance rate %s).' %\
                                               (value_name, value, cs_stat['norm_freq'], lp_category)

                                        self.report.warning.appendDescription('remarkable_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': warn})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ Warning  - %s\n" % warn)

                                else:
                                    tolerance = std_value * 10.0

                                    if value < min_value - tolerance or value > max_value + tolerance:

                                        err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) + '] %s %s is out of range (avg %s, std %s, min %s, max %s, Z_score %.2f).' %\
                                              (value_name, value, avg_value, std_value, min_value, max_value, z_score)

                                        self.report.error.appendDescription('anomalous_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError  - %s\n" % err)

                                    elif abs(z_score) > 10.0:

                                        warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) + '] %s %s must be verified (avg %s, std %s, min %s, max %s, Z_score %.2f).' %\
                                               (value_name, value, avg_value, std_value, min_value, max_value, z_score)

                                        self.report.warning.appendDescription('suspicious_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': warn})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ Warning  - %s\n" % warn)

                                break

                    # standard residue
                    else:

                        if file_type == 'nef':
                            _atom_id = self.nef_translator.get_nmrstar_atom(comp_id, atom_id)[1]

                            if len(_atom_id) == 0:
                                continue

                            # representative atom id
                            atom_id_ = _atom_id[0]
                            atom_name = atom_id + ' (e.g. %s)' % atom_id_

                        else:
                            atom_id_ = atom_id
                            atom_name = atom_id

                        for cs_stat in self.bmrb_cs_stat.get(comp_id, self.report.isDiamagnetic()):

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

                                        self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError  - %s\n" % err)

                                        break

                                if std_value is None:

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name) + '] Insufficient chemical shift statistics is available to verify %s %s (avg %s).' %\
                                           (value_name, value, avg_value)

                                    self.report.warning.appendDescription('unusual_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': warn})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ Warning  - %s\n" % warn)

                                    break

                                z_score = (value - avg_value) / std_value
                                tolerance = std_value / 10.0

                                if value < min_value - tolerance or value > max_value + tolerance:

                                    err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name) + '] %s %s is out of range (avg %s, std %s, min %s, max %s, Z_score %.2f).' %\
                                          (value_name, value, avg_value, std_value, min_value, max_value, z_score)

                                    self.report.error.appendDescription('anomalous_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                                    self.report.setError()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError  - %s\n" % err)

                                elif abs(z_score) > 5.0:

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name) + '] %s %s must be verified (avg %s, std %s, min %s, max %s, Z_score %.2f).' %\
                                           (value_name, value, avg_value, std_value, min_value, max_value, z_score)

                                    self.report.warning.appendDescription('suspicious_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': warn})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ Warning  - %s\n" % warn)

                                elif abs(z_score) > 3.6:

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name) + '] %s %s should be verified (avg %s, std %s, min %s, max %s, Z_score %.2f).' %\
                                           (value_name, value, avg_value, std_value, min_value, max_value, z_score)

                                    self.report.warning.appendDescription('unusual_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': warn})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ Warning  - %s\n" % warn)

                                elif not cs_stat['primary']:

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name) + '] %s %s is remarkable assignment (appearance rate %s).' %\
                                           (value_name, value, cs_stat['norm_freq'])

                                    self.report.warning.appendDescription('remarkable_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': warn})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ Warning  - %s\n" % warn)

                                break

                    if not has_cs_stat:

                        warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) + '] No chemical shift statistics is available to verify %s %s.' %\
                               (value_name, value)

                        self.report.warning.appendDescription('unusual_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': warn})
                        self.report.setWarning()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ Warning  - %s\n" % warn)

                    # check ambiguity code
                    if file_type == 'nmr-star' and ambig_code_name in i:
                        ambig_code = i[ambig_code_name]

                        if ambig_code in self.empty_value or ambig_code == 1:
                            continue

                        allowed_ambig_code = self.bmrb_cs_stat.getMaxAmbigCodeWoSetId(comp_id, atom_id)

                        if ambig_code == 2 or ambig_code == 3:

                            ambig_code_desc = 'ambiguity of geminal atoms or geminal methyl proton groups' if ambig_code == 2 else 'aromatic atoms on opposite sides of symmetrical rings'

                            if ambig_code != allowed_ambig_code:

                                err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) + '] Invalid %s %s (allowed ambig_code %s) exists.' %\
                                      (ambig_code_name, ambig_code, [1, allowed_ambig_code, 4, 5, 6, 9])

                                self.report.error.appendDescription('invalid_ambiguity_code', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError - %s\n" % err)

                            atom_id2 = self.bmrb_cs_stat.getGeminalAtom(comp_id, atom_id)

                            try:

                                ambig_code2 = next(j[ambig_code_name] for j in lp_data if j[item_names['chain_id']] == chain_id and j[item_names['seq_id']] == seq_id and j[item_names['comp_id']] == comp_id and j[item_names['atom_id']] == atom_id2)

                                if ambig_code2 != ambig_code:

                                    err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) + '] %s %s indicates %s. However, %s %s of %s %s is inconsistent.' %\
                                          (ambig_code_name, ambig_code, ambig_code_desc, ambig_code_name, ambig_code2, item_names['atom_id'], atom_id2)

                                    self.report.error.appendDescription('invalid_ambiguity_code', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                                    self.report.setError()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError - %s\n" % err)

                            except StopIteration:

                                err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) + '] %s %s indicates %s. However, row of %s %s of the same residue was not found.' %\
                                      (ambig_code_name, ambig_code, ambig_code_desc, item_names['atom_id'], atom_id2)

                                self.report.error.appendDescription('invalid_ambiguity_code', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError - %s\n" % err)

                        elif ambig_code in [4, 5, 6, 9]:

                            ambig_set_id_name = 'Ambiguity_set_ID'

                            if not ambig_set_id_name in i:

                                err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) + '] %s %s requires %s loop tag.' %\
                                      (ambig_code_name, ambig_code, ambig_set_id_name)

                                self.report.error.appendDescription('missing_mandatory_item', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ LookupError  - %s\n" % err)

                            else:

                                ambig_set_id = i[ambig_set_id_name]

                                if ambig_set_id in self.empty_value:

                                    err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) + '] %s %s requires %s value.' %\
                                          (ambig_code_name, ambig_code, ambig_set_id_name)

                                    self.report.error.appendDescription('missing_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                                    self.report.setError()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError  - %s\n" % err)

                                else:

                                    ambig_set = [j for j in lp_data if j[ambig_set_id_name] == ambig_set_id and j != i]

                                    if len(ambig_set) == 0:

                                        err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) + '] %s %s requires other rows sharing %s %s.' %\
                                              (ambig_code_name, ambig_code, ambig_set_id_name, ambig_set_id)

                                        self.report.error.appendDescription('missing_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ LookupError  - %s\n" % err)

                                    # Intra-residue ambiguities
                                    elif ambig_code == 4:

                                        for j in ambig_set:
                                            chain_id2 = j[item_names['chain_id']]
                                            seq_id2 = j[item_names['seq_id']]
                                            comp_id2 = j[item_names['comp_id']]
                                            atom_id2 = j[item_names['atom_id']]

                                            if (chain_id2 != chain_id or seq_id2 != seq_id or comp_id2 != comp_id) and atom_id < atom_id2:

                                                err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) +\
                                                      ', %s %s, %s %s] It indicates intra-residue ambiguities. However, row of ' % (ambig_code_name, ambig_code, ambig_set_id_name, ambig_set_id) +\
                                                      row_tmp % (chain_id2, seq_id2, comp_id2, atom_id2) + ' exists.'

                                                self.report.error.appendDescription('invalid_ambiguity_code', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                                                self.report.setError()

                                                if self.__verbose:
                                                    self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError - %s\n" % err)

                                    # Inter-residue ambiguities
                                    elif ambig_code == 5:

                                        for j in ambig_set:
                                            chain_id2 = j[item_names['chain_id']]
                                            seq_id2 = j[item_names['seq_id']]
                                            comp_id2 = j[item_names['comp_id']]
                                            atom_id2 = j[item_names['atom_id']]

                                            if ((chain_id2 != chain_id and chain_id < chain_id2) or (seq_id2 == seq_id and atom_id < atom_id2)):

                                                err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) +\
                                                      ', %s %s, %s %s] It indicates inter-residue ambiguities. However, row of ' % (ambig_code_name, ambig_code, ambig_set_id_name, ambig_set_id) +\
                                                      row_tmp % (chain_id2, seq_id2, comp_id2, atom_id2) + ' exists.'

                                                self.report.error.appendDescription('invalid_ambiguity_code', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                                                self.report.setError()

                                                if self.__verbose:
                                                    self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError - %s\n" % err)

                                    # Inter-molecular ambiguities
                                    elif ambig_code == 6:

                                        for j in ambig_set:
                                            chain_id2 = j[item_names['chain_id']]
                                            seq_id2 = j[item_names['seq_id']]
                                            comp_id2 = j[item_names['comp_id']]
                                            atom_id2 = j[item_names['atom_id']]
                                            value2 = j[value_name]

                                            if chain_id2 == chain_id and (seq_id < seq_id2 or (seq_id == seq_id2 and atom_id < atom_id2)):

                                                err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) +\
                                                      ', %s %s, %s %s] It indicates inter-molecular ambiguities. However, row of ' % (ambig_code_name, ambig_code, ambig_set_id_name, ambig_set_id) +\
                                                      row_tmp % (chain_id2, seq_id2, comp_id2, atom_id2) + ' exists.'

                                                self.report.error.appendDescription('invalid_ambiguity_code', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                                                self.report.setError()

                                                if self.__verbose:
                                                    self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError - %s\n" % err)

                                    for j in ambig_set:
                                        chain_id2 = j[item_names['chain_id']]
                                        seq_id2 = j[item_names['seq_id']]
                                        comp_id2 = j[item_names['comp_id']]
                                        atom_id2 = j[item_names['atom_id']]
                                        value2 = j[value_name]

                                        if atom_id[0] != atom_id2[0] and atom_id < atom_id2:

                                            err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) +\
                                                  ', %s %s, %s %s] However, observation nucleus of ' % (ambig_code_name, ambig_code, ambig_set_id_name, ambig_set_id) +\
                                                  row_tmp % (chain_id2, seq_id2, comp_id2, atom_id2) + ' sharing the same %s differs.' % ambig_set_id_name

                                            self.report.error.appendDescription('invalid_ambiguity_code', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                                            self.report.setError()

                                            if self.__verbose:
                                                self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError - %s\n" % err)

                                        elif abs(value2 - value) > max_cs_err and value < value2:

                                            err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) +\
                                                  ', %s %s, %s %s, %s %s] However, %s %s of ' % (value_name, value, ambig_code_name, ambig_code, ambig_set_id_name, ambig_set_id, value_name, value2) +\
                                                  row_tmp % (chain_id2, seq_id2, comp_id2, atom_id2) +\
                                                  'differs by %s (tolerance %s).' % (value2 - value, max_cs_err)

                                            self.report.error.appendDescription('invalid_ambiguity_code', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                                            self.report.setError()

                                            if self.__verbose:
                                                self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError - %s\n" % err)

                        else:

                            err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id) + '] Invalid ambiguity code %s (allowed ambig_code %s) exists.' %\
                                  (ambig_code, self.bmrb_ambiguity_codes)

                            self.report.error.appendDescription('invalid_ambiguity_code', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write("+NmrDpUtility.__validateCSValue() ++ ValueError - %s\n" % err)

            except StopIteration:

                err = "Assigned chemical shifts are mandatory. Saveframe %s did not exist." % sf_framecode

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

        for sf_data in self.__star_data.get_saveframes_by_category(sf_category):

            sf_framecode = sf_data.get_tag('sf_framecode')[0]
            cs_list = sf_data.get_tag(self.cs_list_sf_tag_name[file_type])[0]

            try:

                cs_data = next(l['data'] for l in self.lp_data['chem_shift'] if l['sf_framecode'] == cs_list)

                cs_item_names = self.item_names_in_cs_loop[file_type]
                cs_value_name = cs_item_names['value']
                cs_error_name = cs_item_names['error']
                cs_atom_type = cs_item_names['atom_type']
                cs_iso_number = cs_item_names['isotope_number']

            except StopIteration:

                err = "Assigned chemical shifts are mandatory. Referred saveframe %s did not exist." % (cs_list, self.cs_list_sf_tag_name[file_type])

                self.report.error.appendDescription('missing_mandatory_content', {'file_name': file_name, 'saveframe': sf_framecode, 'description': err})
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

            aux_data = next((l['data'] for l in self.aux_data[content_subtype] if l['sf_framecode'] == sf_framecode and l['lp_category'] == self.aux_lp_categories[file_type][content_subtype][0]), None)

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

            aux_data = next((l['data'] for l in self.aux_data[content_subtype] if l['sf_framecode'] == sf_framecode and l['lp_category'] == self.aux_lp_categories[file_type][content_subtype][1]), None)

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

            index_tag = self.index_tags[file_type][content_subtype]
            max_cs_err = self.chem_shift_error['max_exclusive']

            try:

                lp_data = next((l['data'] for l in self.lp_data[content_subtype] if l['sf_framecode'] == sf_framecode), None)

                if not lp_data is None:
                    for i in lp_data:
                        for d in range(num_dim):
                            chain_id = i[item_names[d]['chain_id']]
                            if chain_id in self.empty_value:
                                continue

                            seq_id = i[item_names[d]['seq_id']]
                            if seq_id in self.empty_value:
                                continue

                            comp_id = i[item_names[d]['comp_id']]
                            if comp_id in self.empty_value:
                                continue

                            atom_id = i[item_names[d]['atom_id']]
                            if atom_id in self.empty_value:
                                continue

                            position = i[item_names[d]['position']]

                            try:

                                cs = next(j for j in cs_data if j[cs_item_names['chain_id']] == chain_id and
                                                                j[cs_item_names['seq_id']] == seq_id and
                                                                j[cs_item_names['comp_id']] == comp_id and
                                                                j[cs_item_names['atom_id']] == atom_id)

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
                                              (index_tag, i[index_tag], item_names[d]['position'], position, item_names[d]['chain_id'], chain_id, item_names[d]['seq_id'], seq_id, item_names[d]['comp_id'], comp_id, item_names[d]['atom_id'], atom_id, sf_framecode, value, position - value, error, cs_list)

                                        self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write("+NmrDpUtility.__testCSValueConsistencyInPkLoop() ++ ValueError  - %s\n" % err)

                                axis_code = str(cs[cs_iso_number]) + cs[cs_atom_type]

                                if axis_code != axis_codes[d]:

                                    err = '[Check row of %s %s] Assignment of spectral peak %s %s, %s %s, %s %s, %s %s is inconsistent with axis code %s vs %s.' %\
                                          (index_tag, i[index_tag], item_names[d]['chain_id'], chain_id, item_names[d]['seq_id'], seq_id, item_names[d]['comp_id'], comp_id, item_names[d]['atom_id'], atom_id, axis_code, axis_codes[d])

                                    self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                                    self.report.setError()

                                    if self.__verbose:
                                        self.__lfh.write("+NmrDpUtility.__testCSValueConsistencyInPkLoop() ++ ValueError  - %s\n" % err)

                            except StopIteration:

                                err = '[Check row of %s %s] Assignment of spectral peak %s %s, %s %s, %s %s, %s %s was not found in assigned chemical shifts in %s saveframe.' %\
                                      (index_tag, i[index_tag], item_names[d]['chain_id'], chain_id, item_names[d]['seq_id'], seq_id, item_names[d]['comp_id'], comp_id, item_names[d]['atom_id'], atom_id, cs_list)

                                self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write("+NmrDpUtility.__testCSValueConsistencyInPkLoop() ++ ValueError  - %s\n" % err)

                            if True in onebond[d]:
                                for d2 in range(num_dim):
                                    if onebond[d][d2]:
                                        chain_id2 = i[item_names[d2]['chain_id']]
                                        seq_id2 = i[item_names[d2]['seq_id']]
                                        comp_id2 = i[item_names[d2]['comp_id']]
                                        atom_id2 = i[item_names[d2]['atom_id']]

                                        if not atom_id2 is None:
                                            diff = len(atom_id) != len(atom_id2)
                                            _atom_id = '_' + (atom_id[1:-1] if atom_id.startswith('H') and diff else atom_id[1:])
                                            _atom_id2 = '_' + (atom_id2[1:-1] if atom_id2.startswith('H') and diff else atom_id2[1:])

                                        if chain_id2 in self.empty_value or seq_id2 in self.empty_value or comp_id2 in self.empty_value or atom_id2 in self.empty_value or\
                                           (d < d2 and (chain_id2 != chain_id or seq_id2 != seq_id or comp_id2 != comp_id or _atom_id2 != _atom_id)):

                                            err = '[Check row of %s %s] Coherence transfer type is onebond. However, assignment of spectral peak is inconsistent with the type, (%s %s, %s %s, %s %s, %s %s) vs (%s %s, %s %s, %s %s, %s %s).' %\
                                                  (index_tag, i[index_tag], item_names[d]['chain_id'], chain_id, item_names[d]['seq_id'], seq_id, item_names[d]['comp_id'], comp_id, item_names[d]['atom_id'], atom_id,
                                                   item_names[d2]['chain_id'], chain_id2, item_names[d2]['seq_id'], seq_id2, item_names[d2]['comp_id'], comp_id2, item_names[d2]['atom_id'], atom_id2)

                                            self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                                            self.report.setError()

                                            if self.__verbose:
                                                self.__lfh.write("+NmrDpUtility.__testCSValueConsistencyInPkLoop() ++ ValueError  - %s\n" % err)

                            if True in jcoupling[d]:
                                for d2 in range(num_dim):
                                    if jcoupling[d][d2]:
                                        chain_id2 = i[item_names[d2]['chain_id']]
                                        seq_id2 = i[item_names[d2]['seq_id']]
                                        comp_id2 = i[item_names[d2]['comp_id']]
                                        atom_id2 = i[item_names[d2]['atom_id']]

                                        if chain_id2 in self.empty_value or seq_id2 in self.empty_value or comp_id2 in self.empty_value or atom_id2 in self.empty_value or\
                                           (d < d2 and (chain_id2 != chain_id or abs(seq_id2 - seq_id) > 1)):

                                            err = '[Check row of %s %s] Coherence transfer type is jcoupling. However, assignment of spectral peak is inconsistent with the type, (%s %s, %s %s, %s %s, %s %s) vs (%s %s, %s %s, %s %s, %s %s).' %\
                                                  (index_tag, i[index_tag], item_names[d]['chain_id'], chain_id, item_names[d]['seq_id'], seq_id, item_names[d]['comp_id'], comp_id, item_names[d]['atom_id'], atom_id,
                                                   item_names[d2]['chain_id'], chain_id2, item_names[d2]['seq_id'], seq_id2, item_names[d2]['comp_id'], comp_id2, item_names[d2]['atom_id'], atom_id2)

                                            self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                                            self.report.setError()

                                            if self.__verbose:
                                                self.__lfh.write("+NmrDpUtility.__testCSValueConsistencyInPkLoop() ++ ValueError  - %s\n" % err)

                            if True in relayed[d]:
                                for d2 in range(num_dim):
                                    if relayed[d][d2]:
                                        chain_id2 = i[item_names[d2]['chain_id']]
                                        seq_id2 = i[item_names[d2]['seq_id']]
                                        comp_id2 = i[item_names[d2]['comp_id']]
                                        atom_id2 = i[item_names[d2]['atom_id']]

                                        if chain_id2 in self.empty_value or seq_id2 in self.empty_value or comp_id2 in self.empty_value or atom_id2 in self.empty_value or\
                                           (d < d2 and (chain_id2 != chain_id or seq_id2 != seq_id or comp_id2 != comp_id or atom_id[0] != atom_id2[0])):

                                            err = '[Check row of %s %s] Coherence transfer type is relayed. However, assignment of spectral peak is inconsistent with the type, (%s %s, %s %s, %s %s, %s %s) vs (%s %s, %s %s, %s %s, %s %s).' %\
                                                  (index_tag, i[index_tag], item_names[d]['chain_id'], chain_id, item_names[d]['seq_id'], seq_id, item_names[d]['comp_id'], comp_id, item_names[d]['atom_id'], atom_id,
                                                   item_names[d2]['chain_id'], chain_id2, item_names[d2]['seq_id'], seq_id2, item_names[d2]['comp_id'], comp_id2, item_names[d2]['atom_id'], atom_id2)

                                            self.report.error.appendDescription('invalid_data', {'file_name': file_name, 'saveframe': sf_framecode, 'category': lp_category, 'description': err})
                                            self.report.setError()

                                            if self.__verbose:
                                                self.__lfh.write("+NmrDpUtility.__testCSValueConsistencyInPkLoop() ++ ValueError  - %s\n" % err)

            except Exception as e:

                self.report.error.appendDescription('internal_error', "+NmrDpUtility.__testCSValueConsistencyInPkLoop() ++ Error  - %s" % str(e))
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__testCSValueConsistencyInPkLoop() ++ Error  - %s" % str(e))

        return self.report.getTotalErrors() == __errors

    def __calculateStatsOfExptlData(self):
        """ Calculate statistics of experimental data.
        """

        input_source = self.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        if input_source_dic['content_subtype'] is None:
            return False

        __errors = self.report.getTotalErrors()

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

                lp_data = next((l['data'] for l in self.lp_data[content_subtype] if l['sf_framecode'] == sf_framecode), None)

                if not lp_data is None:

                    ent = {'list_id': list_id, 'sf_framecode': sf_framecode, 'number_of_rows': len(lp_data), 'sequence_coverage': []}

                    if content_subtype == 'chem_shift':
                        pass

                    elif content_subtype == 'dist_restraint':
                        pass

                    elif content_subtype == 'dihed_restraint':
                        pass

                    elif content_subtype == 'rdc_restraint':
                        pass

                    elif content_subtype == 'spectral_peak':
                        pass

                    else:

                        err = "Module for calculation of statistics on content subtype %s were not found." % content_subtype

                        self.report.error.appendDescription('internal_error', "+NmrDpUtility.__calculateStatsOfExptlData() ++ Error  - %s" % err)
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write("+NmrDpUtility.__calculateStatsOfExptlData() ++ Error  - %s\n" % err)

                        continue

                    asm.append(ent)

                    list_id += 1

            if list_id > 1:
                stats[content_subtype] = asm

        input_source.setItemValue('stats_of_exptl_data', stats)

        return self.report.getTotalErrors() == __errors

    def __appendCoordinate(self):
        """ Append coordinate file as secondary input resource.
        """

        file_type = 'pdbx'
        content_type = self.content_type[file_type]

        if 'coordinate_file_path' in self.__inputParamDict:

            file_path = self.__inputParamDict['coordinate_file_path']
            file_name = os.path.basename(file_path)

            try:

                if not self.__cR.setFilePath(file_path):

                    err = "No such %s file." % file_name

                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__appendCoordinate() ++ Error  - %s" % err)
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__appendCoordinate() ++ Error  - %s\n" % err)

                    return False

                if not self.__cR.parse():

                    err = "%s is invalid %s file." % (file_name, self.readable_file_type[file_type])

                    self.report.error.appendDescription('internal_error', "+NmrDpUtility.__appendCoordinate() ++ Error  - %s" % err)
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write("+NmrDpUtility.__appendCoordinate() ++ Error  - %s\n" % err)

                    return False

                self.report.addInputSource()

                input_source = self.report.input_sources[-1]

                input_source.setItemValue('file_name', file_name)
                input_source.setItemValue('file_type', file_type)
                input_source.setItemValue('content_type', content_type)

                return True

            except:
                pass

        else:

            err = "%s formatted model file is mandatory." % self.readable_file_type[file_type]

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__appendCoordinate() ++ Error  - %s" % err)
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__appendCoordinate() ++ Error  - %s\n" % err)

            return False

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

                warn = "Category %s did not exist." % self.lp_categories[file_type][content_subtype]

                self.report.warning.appendDescription('missing_content', {'file_name': file_name, 'description': warn})
                self.report.setWarning()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__detectCoordContentSubType() ++ Warning  - %s\n" % warn)

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

                    list_id += 1
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

            if not has_poly_seq:
                poly_seq_list_set.pop(content_subtype)

        if self.report.getTotalErrors() > __errors:
            return False

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

        has_poly_seq = 'polymer_sequence' in input_source_dic

        if not has_poly_seq:
            return True

        polymer_sequence = input_source_dic['polymer_sequence']

        asm_has = False

        asm = []

        for s in polymer_sequence:

            ent_has = False

            ent = {'chain_id': s['chain_id'], 'seq_id': [], 'comp_id': []}

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

    def __appendCoordPolymerSequenceAlignment(self):
        """ Append polymer sequence alignment between coordinate and NMR data.
        """

        id = self.report.getInputSourceIdOfCoord()

        if id < 0:
            return True

        # sequence alignment inside coordinate file

        input_source = self.report.input_sources[id]
        input_source_dic = input_source.get()

        has_poly_seq = 'polymer_sequence' in input_source_dic
        has_poly_seq_in_loop = 'polymer_sequence_in_loop' in input_source_dic

        if not has_poly_seq:
            return False

        if has_poly_seq_in_loop:

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

                            self.__pA.setReferenceSequence(s1['comp_id'], 'REF' + cid)
                            self.__pA.addTestSequence(_s2['comp_id'], cid)
                            self.__pA.doAlign()
                            #self.__pA.prAlignmentConflicts(cid)
                            myAlign = self.__pA.getAlignment(cid)

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
                                         'chain_id': cid, 'length': length, 'conflict': conflicts, 'sequence_coverage': float('{:.3f}'.format(float(length - conflicts) / float(length))), 'ref_seq_id': s1['seq_id'], 'reference_seq': ref_seq, 'middle_code': mid_seq, 'test_seq': tst_seq}

                            seq_align_set.append(seq_align)

                    if has_seq_align:
                        self.report.sequence_alignment.setItemValue('model_poly_seq_vs_' + subtype, seq_align_set)

        # sequence alignment between model and NMR data

        nmr_input_source = self.report.input_sources[0]
        nmr_input_source_dic = nmr_input_source.get()

        has_nmr_poly_seq = 'polymer_sequence' in nmr_input_source_dic

        if not has_nmr_poly_seq:

            err = "Common polymer sequence did not exist, __extractCommonPolymerSequence() should be invoked."

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__appendCoordPolymerSequenceAlignment() ++ Error  - %s" % err)
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__appendCoordPolymerSequenceAlignment() ++ Error  - %s\n" % err)

            return False

        nmr_polymer_sequence = nmr_input_source_dic['polymer_sequence']

        for s1 in polymer_sequence:
            cid = s1['chain_id']

            has_seq_align = False

            seq_align_set = []

            for s2 in nmr_polymer_sequence:
                cid2 = s2['chain_id']

                _s2 = self.__fillBlankedCompId(s1, s2)

                self.__pA.setReferenceSequence(s1['comp_id'], 'REF' + cid)
                self.__pA.addTestSequence(_s2['comp_id'], cid2)
                self.__pA.doAlign()
                #self.__pA.prAlignmentConflicts(cid)
                myAlign = self.__pA.getAlignment(cid)

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

                seq_align = {'ref_chain_id': cid, 'test_chain_id': cid2, 'length': length, 'conflict': conflicts, 'sequence_coverage': float('{:.3f}'.format(float(length - conflicts) / float(length))), 'ref_seq_id': s1['seq_id'], 'reference_seq': ref_seq, 'middle_code': mid_seq, 'test_seq': tst_seq}

                seq_align_set.append(seq_align)

            if has_seq_align:
                self.report.sequence_alignment.setItemValue('model_poly_seq_vs_nmr_poly_seq', seq_align_set)

        for s1 in nmr_polymer_sequence:
            cid = s1['chain_id']

            has_seq_align = False

            seq_align_set = []

            for s2 in polymer_sequence:
                cid2 = s2['chain_id']

                _s2 = self.__fillBlankedCompId(s1, s2)

                self.__pA.setReferenceSequence(s1['comp_id'], 'REF' + cid)
                self.__pA.addTestSequence(_s2['comp_id'], cid2)
                self.__pA.doAlign()
                #self.__pA.prAlignmentConflicts(cid)
                myAlign = self.__pA.getAlignment(cid)

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

                seq_align = {'ref_chain_id': cid, 'test_chain_id': cid2, 'length': length, 'conflict': conflicts, 'sequence_coverage': float('{:.3f}'.format(float(length - conflicts) / float(length))), 'ref_seq_id': s1['seq_id'], 'reference_seq': ref_seq, 'middle_code': mid_seq, 'test_seq': tst_seq}

                seq_align_set.append(seq_align)

            if has_seq_align:
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

        has_cif_poly_seq = 'polymer_sequence' in cif_input_source_dic

        if not has_cif_poly_seq:
            return False

        nmr_input_source = self.report.input_sources[0]
        nmr_input_source_dic = nmr_input_source.get()

        nmr_file_name = nmr_input_source_dic['file_name']

        has_nmr_poly_seq = 'polymer_sequence' in nmr_input_source_dic

        if not has_nmr_poly_seq:

            err = "Common polymer sequence did not exist, __extractCommonPolymerSequence() should be invoked."

            self.report.error.appendDescription('internal_error', "+NmrDpUtility.__assignCoordPolymerSequence() ++ Error  - %s" % err)
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__assignCoordPolymerSequence() ++ Error  - %s\n" % err)

            return False

        seq_align_dic = self.report.sequence_alignment.get()

        if 'model_poly_seq_vs_nmr_poly_seq' in seq_align_dic and 'nmr_poly_seq_vs_model_poly_seq' in seq_align_dic:

            cif_polymer_sequence = cif_input_source_dic['polymer_sequence']
            nmr_polymer_sequence = nmr_input_source_dic['polymer_sequence']

            cif_chains = len(cif_polymer_sequence)
            nmr_chains = len(nmr_polymer_sequence)

            # map polymer sequences between coordinate and NMR data using Hungarian algorithm
            m = Munkres()

            # from model to nmr

            cif2nmr = {}

            mat = []

            for s1 in cif_polymer_sequence:
                cid = s1['chain_id']

                cost = [0 * nmr_chains]

                for s2 in nmr_polymer_sequence:
                    cid2 = s2['chain_id']

                    result = next((seq_align for seq_align in seq_align_dic['model_poly_seq_vs_nmr_poly_seq'] if seq_align['ref_chain_id'] == cid and seq_align['test_chain_id'] == cid2), None)

                    if not result is None:
                        cost[nmr_polymer_sequence.index(s2)] = result['conflict'] - result['length']

                mat.append(cost)

            indices = m.compute(mat)

            chain_assign_set = []

            for row, column in indices:

                if mat[row][column] >= 0:
                    continue

                cid = cif_polymer_sequence[row]['chain_id']
                cid2 = nmr_polymer_sequence[column]['chain_id']

                cif2nmr[cid] = cid2

                result = next(seq_align for seq_align in seq_align_dic['model_poly_seq_vs_nmr_poly_seq'] if seq_align['ref_chain_id'] == cid and seq_align['test_chain_id'] == cid2)

                chain_assign = {'ref_chain_id': cid, 'test_chain_id': cid2, 'length': result['length'], 'conflict': result['conflict'], 'sequence_coverage': result['sequence_coverage']}

                chain_assign_set.append(chain_assign)

            if len(chain_assign_set) > 0:
                self.report.chain_assignment.setItemValue('model_poly_seq_vs_nmr_poly_seq', chain_assign_set)

            # from nmr to model

            nmr2cif = {}

            mat = []

            for s1 in nmr_polymer_sequence:
                cid = s1['chain_id']

                cost = [0 * cif_chains]

                for s2 in cif_polymer_sequence:
                    cid2 = s2['chain_id']

                    result = next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq'] if seq_align['ref_chain_id'] == cid and seq_align['test_chain_id'] == cid2), None)

                    if not result is None:
                        cost[cif_polymer_sequence.index(s2)] = result['conflict'] - result['length']

                mat.append(cost)

            indices = m.compute(mat)

            chain_assign_set = []

            for row, column in indices:

                if mat[row][column] >= 0:
                    continue

                cid = nmr_polymer_sequence[row]['chain_id']
                cid2 = cif_polymer_sequence[column]['chain_id']

                nmr2cif[cid] = cid2

                result = next(seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq'] if seq_align['ref_chain_id'] == cid and seq_align['test_chain_id'] == cid2)

                chain_assign = {'ref_chain_id': cid, 'test_chain_id': cid2, 'length': result['length'], 'conflict': result['conflict'], 'sequence_coverage': result['sequence_coverage']}

                chain_assign_set.append(chain_assign)

            if len(chain_assign_set) > 0:
                self.report.chain_assignment.setItemValue('nmr_poly_seq_vs_model_poly_seq', chain_assign_set)

            # check conflict

            conflicts = []

            for s1 in cif_polymer_sequence:
                cid = s1['chain_id']

                if cid in cif2nmr:
                    cid2 = cif2nmr[cid]

                    result = next(seq_align for seq_align in seq_align_dic['model_poly_seq_vs_nmr_poly_seq'] if seq_align['ref_chain_id'] == cid and seq_align['test_chain_id'] == cid2)

                    if result['conflict'] == 0:
                        continue

                    s2 = next(s for s in nmr_polymer_sequence if s['chain_id'] == cid2)

                    _s2 = self.__fillBlankedCompId(s1, s2)

                    self.__pA.setReferenceSequence(s1['comp_id'], 'REF' + cid)
                    self.__pA.addTestSequence(_s2['comp_id'], cid2)
                    self.__pA.doAlign()
                    #self.__pA.prAlignmentConflicts(cid)
                    myAlign = self.__pA.getAlignment(cid)

                    for i in range(len(myAlign)):
                        myPr = myAlign[i]
                        if myPr[0] == myPr[1]:
                            continue

                        cif_comp_id = myPr[0].encode()
                        nmr_comp_id = myPr[1].encode()

                        if nmr_comp_id == '.':
                            continue

                        c = {'cif_chain_id': cid, 'cif_seq_id': s1['seq_id'][i], 'cif_comp_id': cif_comp_id,
                             'nmr_chain_id': cid2, 'nmr_seq_id': _s2['seq_id'][i], 'nmr_comp_id': nmr_comp_id}

                        if not c in conflicts:
                            conflicts.append(c)

            # reverse check

            for s1 in nmr_polymer_sequence:
                cid = s1['chain_id']

                if cid in nmr2cif:
                    cid2 = nmr2cif[cid]

                    result = next(seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq'] if seq_align['ref_chain_id'] == cid and seq_align['test_chain_id'] == cid2)

                    if result['conflict'] == 0:
                        continue

                    s2 = next(s for s in cif_polymer_sequence if s['chain_id'] == cid2)

                    _s2 = self.__fillBlankedCompId(s1, s2)

                    self.__pA.setReferenceSequence(s1['comp_id'], 'REF' + cid)
                    self.__pA.addTestSequence(_s2['comp_id'], cid2)
                    self.__pA.doAlign()
                    #self.__pA.prAlignmentConflicts(cid)
                    myAlign = self.__pA.getAlignment(cid)

                    for i in range(len(myAlign)):
                        myPr = myAlign[i]
                        if myPr[0] == myPr[1]:
                            continue

                        nmr_comp_id = myPr[0].encode()
                        cif_comp_id = myPr[1].encode()

                        if cif_comp_id == '.':
                            continue

                        c = {'cif_chain_id': cid2, 'cif_seq_id': _s2['seq_id'][i], 'cif_comp_id': cif_comp_id,
                             'nmr_chain_id': cid, 'nmr_seq_id': s1['seq_id'][i], 'nmr_comp_id': nmr_comp_id}

                        if not c in conflicts:
                            conflicts.append(c)

            for c in conflicts:

                err = "Sequence alignment error between %s (chain_id %s, seq_id %s, comp_id %s) and %s (chain_id %s, seq_id %s, comp_id %s)." %\
                    (cif_file_name, c['cif_chain_id'], c['cif_seq_id'], c['cif_comp_id'],
                     nmr_file_name, c['nmr_chain_id'], c['nmr_seq_id'], c['nmr_comp_id'])

                self.report.error.appendDescription('sequence_mismatch', {'file_name': cif_file_name, 'description': err})
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write("+NmrDpUtility.__assignCoordPolymerSequence() ++ Error  - %s" % err)

            return len(conflicts) == 0

        else:

            err = "No sequence alignment found."

            self.report.error.appendDescription('sequence_mismatch', {'file_name': cif_file_name, 'description': err})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write("+NmrDpUtility.__assignCoordPolymerSequence() ++ Error  - %s" % err)

            return False

    def __testCorrdAtomIdConsistency(self):
        """ Perform consistency test on atom names of coordinate file.
        """

        id = self.report.getInputSourceIdOfCoord()

        if id < 0:
            return True

        cif_input_source = self.report.input_sources[id]
        cif_input_source_dic = cif_input_source.get()

        cif_file_name = cif_input_source_dic['file_name']

        nmr_input_source = self.report.input_sources[0]
        nmr_input_source_dic = nmr_input_source.get()

        nmr_file_name = nmr_input_source_dic['file_name']

        return True

if __name__ == '__main__':
    dp = NmrDpUtility()
