##
# File: ParserListenerUtil.py
# Date: 18-Feb-2022
#
# Updates:
""" Utilities for MR/PT parser listener.
    @author: Masashi Yokochi
"""
import sys
import copy
import numpy as np


REPRESENTATIVE_MODEL_ID = 1


DIST_RESTRAINT_RANGE = {'min_inclusive': 0.5, 'max_inclusive': 50.0}
DIST_RESTRAINT_ERROR = {'min_exclusive': 0.0, 'max_exclusive': 150.0}


ANGLE_RESTRAINT_RANGE = {'min_inclusive': -225.0, 'max_inclusive': 225.0}
ANGLE_RESTRAINT_ERROR = {'min_exclusive': -360.0, 'max_exclusive': 360.0}


RDC_RESTRAINT_RANGE = {'min_exclusive': -100.0, 'max_exclusive': 100.0}
RDC_RESTRAINT_RANGE = {'min_exclusive': -200.0, 'max_exclusive': 200.0}


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


def translateAmberAtomNomenclature(atomId):
    """ Translate AMBER atom nomenclature to the IUPAC one.
    """

    atomId = atomId.upper()
    if atomId.endswith("O'1"):
        atomId = atomId[0:len(atomId) - 3] + "O1'"
    elif atomId.endswith("O'2"):
        atomId = atomId[0:len(atomId) - 3] + "O2'"
    elif atomId.endswith("O'3"):
        atomId = atomId[0:len(atomId) - 3] + "O3'"
    elif atomId.endswith("O'4"):
        atomId = atomId[0:len(atomId) - 3] + "O4'"
    elif atomId.endswith("O'5"):
        atomId = atomId[0:len(atomId) - 3] + "O5'"
    elif atomId.endswith("O'6"):
        atomId = atomId[0:len(atomId) - 3] + "O6'"
    elif atomId.endswith("'1"):
        atomId = atomId.rstrip('1')
    elif atomId.endswith("'2"):
        atomId = atomId.rstrip('2') + "'"
    elif atomId == 'O1P':
        atomId = 'OP1'
    elif atomId == 'O2P':
        atomId = 'OP2'
    elif atomId == 'O3P':
        atomId = 'OP3'
    elif atomId == 'H3T':
        atomId = "HO3'"
    elif atomId == 'H5T':
        atomId = 'HOP2'
    elif atomId.endswith('"'):
        atomId = atomId[0:len(atomId) - 1] + "''"

    return atomId


def checkCoordinates(verbose=True, log=sys.stdout, cR=None, polySeq=None,
                     coordAtomSite=None, coordUnobsRes=None, labelToAuthSeq=None,
                     testTag=True):
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

            altPolySeq = None

            if len(polySeq) > 1:
                ps = copy.copy(polySeq[0])
                ps['auth_seq_id'] = ps['seq_id']
                altPolySeq = [ps]
                lastSeqId = ps['auth_seq_id'][-1]

                for chainId in range(1, len(polySeq)):
                    ps = copy.copy(polySeq[chainId])
                    offset = lastSeqId + 1 - ps['seq_id'][0]
                    ps['auth_seq_id'] = [s + offset for s in ps['seq_id']]
                    altPolySeq.append(ps)
                    lastSeqId = ps['auth_seq_id'][-1]

        except Exception as e:
            if verbose:
                log.write(f"+ParserListenerUtil.checkCoordinates() ++ Error - {str(e)}\n")

    if not testTag:
        return {'polymer_sequence': polySeq, 'alt_polymer_sequence': altPolySeq}

    try:

        modelNumName = 'pdbx_PDB_model_num' if cR.hasItem('atom_site', 'pdbx_PDB_model_num') else 'ndb_model'
        authAsymId = 'pdbx_auth_asym_id' if cR.hasItem('atom_site', 'pdbx_auth_asym_id') else 'auth_asym_id'
        authSeqId = 'pdbx_auth_seq_id' if cR.hasItem('atom_site', 'pdbx_auth_seq_id') else 'auth_seq_id'
        authAtomId = 'pdbx_auth_atom_name' if cR.hasItem('atom_site', 'pdbx_auth_atom_name') else 'auth_atom_id'
        altAuthAtomId = None if authAtomId == 'auth_atom_id' else 'auth_atom_id'

        if coordAtomSite is None or labelToAuthSeq is None:

            if altAuthAtomId is not None:
                coord = cR.getDictListWithFilter('atom_site',
                                                 [{'name': authAsymId, 'type': 'str', 'alt_name': 'chain_id'},
                                                  {'name': authSeqId, 'type': 'int', 'alt_name': 'seq_id'},
                                                  {'name': 'label_seq_id', 'type': 'str', 'alt_name': 'alt_seq_id'},
                                                  {'name': 'auth_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                  {'name': authAtomId, 'type': 'str', 'alt_name': 'atom_id'},
                                                  {'name': altAuthAtomId, 'type': 'str', 'alt_name': 'alt_atom_id'},
                                                  {'name': 'type_symbol', 'type': 'str'}
                                                  ],
                                                 [{'name': modelNumName, 'type': 'int', 'value': REPRESENTATIVE_MODEL_ID}
                                                  ])
            else:
                coord = cR.getDictListWithFilter('atom_site',
                                                 [{'name': authAsymId, 'type': 'str', 'alt_name': 'chain_id'},
                                                  {'name': authSeqId, 'type': 'int', 'alt_name': 'seq_id'},
                                                  {'name': 'label_seq_id', 'type': 'str', 'alt_name': 'alt_seq_id'},
                                                  {'name': 'auth_comp_id', 'type': 'str', 'alt_name': 'comp_id'},
                                                  {'name': authAtomId, 'type': 'str', 'alt_name': 'atom_id'},
                                                  {'name': 'type_symbol', 'type': 'str'}
                                                  ],
                                                 [{'name': modelNumName, 'type': 'int', 'value': REPRESENTATIVE_MODEL_ID}
                                                  ])

            coordAtomSite = {}
            labelToAuthSeq = {}
            chainIds = set(c['chain_id'] for c in coord)
            for chainId in chainIds:
                seqIds = set(c['seq_id'] for c in coord if c['chain_id'] == chainId)
                for seqId in seqIds:
                    seqKey = (chainId, seqId)
                    compId = next(c['comp_id'] for c in coord
                                  if c['chain_id'] == chainId and c['seq_id'] is not None and c['seq_id'] == seqId)
                    atomIds = [c['atom_id'] for c in coord
                               if c['chain_id'] == chainId and c['seq_id'] is not None and c['seq_id'] == seqId]
                    typeSymbols = [c['type_symbol'] for c in coord
                                   if c['chain_id'] == chainId and c['seq_id'] is not None and c['seq_id'] == seqId]
                    coordAtomSite[seqKey] = {'comp_id': compId, 'atom_id': atomIds, 'type_symbol': typeSymbols}
                    if altAuthAtomId is not None:
                        altAtomIds = [c['alt_atom_id'] for c in coord
                                      if c['chain_id'] == chainId and c['seq_id'] is not None and c['seq_id'] == seqId]
                        coordAtomSite[seqKey]['alt_atom_id'] = altAtomIds
                    altSeqId = next((c['alt_seq_id'] for c in coord if c['chain_id'] == chainId and c['seq_id'] == seqId), None)
                    if altSeqId is not None and altSeqId.isdigit():
                        labelToAuthSeq[(chainId, int(altSeqId))] = seqKey

        if coordUnobsRes is None:
            coordUnobsRes = {}
            unobs = cR.getDictListWithFilter('pdbx_unobs_or_zero_occ_residues',
                                             [{'name': 'auth_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                              {'name': 'auth_seq_id', 'type': 'str', 'alt_name': 'seq_id'},
                                              {'name': 'auth_comp_id', 'type': 'str', 'alt_name': 'comp_id'}
                                              ],
                                             [{'name': 'PDB_model_num', 'type': 'int', 'value': REPRESENTATIVE_MODEL_ID}
                                              ])

            if len(unobs) > 0:
                chainIds = set(u['chain_id'] for u in unobs)
                for chainId in chainIds:
                    seqIds = set(int(u['seq_id']) for u in unobs if u['chain_id'] == chainId and u['seq_id'] is not None)
                    for seqId in seqIds:
                        seqKey = (chainId, seqId)
                        compId = next(u['comp_id'] for u in unobs
                                      if u['chain_id'] == chainId and u['seq_id'] is not None and int(u['seq_id']) == seqId)
                        coordUnobsRes[seqKey] = {'comp_id': compId}

    except Exception as e:
        if verbose:
            log.write(f"+ParserListenerUtil.checkCoordinates() ++ Error  - {str(e)}\n")

    return {'model_num_name': modelNumName,
            'auth_asym_id': authAsymId,
            'auth_seq_id': authSeqId,
            'auth_atom_id': authAtomId,
            'alt_auth_atom_id': altAuthAtomId,
            'polymer_sequence': polySeq,
            'alt_polymer_sequence': altPolySeq,
            'coord_atom_site': coordAtomSite,
            'coord_unobs_res': coordUnobsRes,
            'label_to_auth_seq': labelToAuthSeq}
