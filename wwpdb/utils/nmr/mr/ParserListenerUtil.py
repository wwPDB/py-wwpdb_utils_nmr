##
# File: ParserListenerUtil.py
# Date: 18-Feb-2022
#
# Updates:
""" Utilities for MR/PT parser listener.
    @author: Masashi Yokochi
"""
import sys
import numpy as np


def toNpArray(atom):
    """ Return Numpy array of a given Cartesian coordinate in {'x': float, 'y': float, 'z': float} format.
    """

    return np.asarray([atom['x'], atom['y'], atom['z']], dtype=float)


def toRegEx(string):
    """ Return regular expression for a given string including XPLOR-NIH wildcard format.
    """

    if '*' in string:  # any string
        return string.replace('*', '.*')
    if '%' in string:  # a single character
        return string.replace('%', '.')
    if '#' in string:  # any number
        return string.replace('#', '[+-]?[0-9][0-9\\.]?')
    if '+' in string:  # any digit
        return string.replace('+', '[0-9]+')
    return string


def checkCoordinates(verbose=True, log=sys.stdout, cR=None, polySeq=None, testTag=True):
    """ Examine the coordinates for MR/PT parser listener.
    """

    if polySeq is None:

        # loop categories
        _lpCategories = {'poly_seq': 'pdbx_poly_seq_scheme',
                         'non_poly': 'pdbx_nonpoly_scheme',
                         'coordinate': 'atom_site',
                         'poly_seq_alias': 'ndb_poly_seq_scheme',
                         'non_poly_alias': 'ndb_nonpoly_scheme'
                         }

        # key items of loop
        _keyItems = {'poly_seq': [{'name': 'asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                  {'name': 'seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                  {'name': 'mon_id', 'type': 'str', 'alt_name': 'comp_id'},
                                  {'name': 'pdb_strand_id', 'type': 'str', 'alt_name': 'auth_chain_id'}
                                  ],
                     'poly_seq_alias': [{'name': 'id', 'type': 'str', 'alt_name': 'chain_id'},
                                        {'name': 'seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                        {'name': 'mon_id', 'type': 'str', 'alt_name': 'comp_id'}
                                        ],
                     'non_poly': [{'name': 'asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                  {'name': 'pdb_seq_num', 'type': 'int', 'alt_name': 'seq_id'},
                                  {'name': 'mon_id', 'type': 'str', 'alt_name': 'comp_id'},
                                  {'name': 'pdb_strand_id', 'type': 'str', 'alt_name': 'auth_chain_id'}
                                  ],
                     'non_poly_alias': [{'name': 'asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                        {'name': 'pdb_num', 'type': 'int', 'alt_name': 'seq_id'},
                                        {'name': 'mon_id', 'type': 'str', 'alt_name': 'comp_id'}
                                        ],
                     'coordinate': [{'name': 'label_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                    {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                    {'name': 'auth_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                    {'name': 'pdbx_PDB_model_num', 'type': 'int', 'alt_name': 'model_id'}
                                    ],
                     'coordinate_alias': [{'name': 'label_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                          {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                          {'name': 'auth_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                          {'name': 'ndb_model', 'type': 'int', 'alt_name': 'model_id'}
                                          ],
                     'coordinate_ins': [{'name': 'label_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                        {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                        {'name': 'auth_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                        {'name': 'pdbx_PDB_ins_code', 'type': 'str', 'alt_name': 'ins_code', 'default': '?'},
                                        {'name': 'label_seq_id', 'type': 'str', 'alt_name': 'label_seq_id', 'default': '.'},
                                        {'name': 'pdbx_PDB_model_num', 'type': 'int', 'alt_name': 'model_id'}
                                        ],
                     'coordinate_ins_alias': [{'name': 'label_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                              {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                              {'name': 'auth_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                              {'name': 'ndb_ins_code', 'type': 'str', 'alt_name': 'ins_code', 'default': '?'},
                                              {'name': 'label_seq_id', 'type': 'str', 'alt_name': 'label_seq_id', 'default': '.'},
                                              {'name': 'ndb_model', 'type': 'int', 'alt_name': 'model_id'}
                                              ]
                     }

        contetSubtype = 'poly_seq'

        alias = False
        lpCategory = _lpCategories[contetSubtype]
        keyItems = _keyItems[contetSubtype]

        if not cR.hasCategory(lpCategory):
            alias = True
            lpCategory = _lpCategories[contetSubtype + '_alias']
            keyItems = _keyItems[contetSubtype + '_alias']

        try:

            try:
                polySeq = cR.getPolymerSequence(lpCategory, keyItems,
                                                withStructConf=True, alias=alias)
            except KeyError:  # pdbx_PDB_ins_code throws KeyError
                if contetSubtype + ('_ins_alias' if alias else '_ins') in keyItems:
                    keyItems = _keyItems[contetSubtype + ('_ins_alias' if alias else '_ins')]
                    polySeq = cR.getPolymerSequence(lpCategory, keyItems,
                                                    withStructConf=True, alias=alias)
                else:
                    polySeq = []

        except Exception as e:
            if verbose:
                log.write(f"+ParserListenerUtil.checkCoordinates() ++ Error - {str(e)}\n")

    if not testTag:
        return {'polymer_sequence': polySeq}

    try:

        modelNumName = 'pdbx_PDB_model_num' if cR.hasItem('atom_site', 'pdbx_PDB_model_num') else 'ndb_model'
        authAsymId = 'pdbx_auth_asym_id' if cR.hasItem('atom_site', 'pdbx_auth_asym_id') else 'auth_asym_id'
        authSeqId = 'pdbx_auth_seq_id' if cR.hasItem('atom_site', 'pdbx_auth_seq_id') else 'auth_seq_id'
        authAtomId = 'pdbx_auth_atom_name' if cR.hasItem('atom_site', 'pdbx_auth_atom_name') else 'auth_atom_id'

    except Exception as e:

        if verbose:
            log.write(f"+ParserListenerUtil.checkCoordinates() ++ Error  - {str(e)}\n")

    return {'model_num_name': modelNumName,
            'auth_asym_id': authAsymId,
            'auth_seq_id': authSeqId,
            'auth_atom_id': authAtomId,
            'polymer_sequence': polySeq}