##
# File: BasePKParserListener.py
# Date: 03-Dec-2024
#
# Updates:
""" ParserLister base class for any peak list file.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "1.0.0"

import sys
import re
import copy
import collections
import numpy
import itertools
import pynmrstar

from typing import IO, List, Tuple, Optional

from wwpdb.utils.align.alignlib import PairwiseAlign  # pylint: disable=no-name-in-module

try:
    from wwpdb.utils.nmr.io.CifReader import (CifReader,
                                              SYMBOLS_ELEMENT)
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (coordAssemblyChecker,
                                                       translateToStdResName,
                                                       translateToStdAtomName,
                                                       translateToLigandName,
                                                       hasInterChainRestraint,
                                                       isLongRangeRestraint,
                                                       isCyclicPolymer,
                                                       isStructConn,
                                                       guessCompIdFromAtomId,
                                                       getMetalCoordOf,
                                                       getRestraintName,
                                                       contentSubtypeOf,
                                                       incListIdCounter,
                                                       decListIdCounter,
                                                       getSaveframe,
                                                       getPkLoop,
                                                       getAltLoops,
                                                       getAuxLoops,
                                                       getPkRow,
                                                       getPkGenCharRow,
                                                       getPkCharRow,
                                                       getPkChemShiftRow,
                                                       getSpectralDimRow,
                                                       getSpectralDimTransferRow,
                                                       getMaxEffDigits,
                                                       roundString,
                                                       ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS,
                                                       REPRESENTATIVE_MODEL_ID,
                                                       REPRESENTATIVE_ALT_ID,
                                                       MAX_PREF_LABEL_SCHEME_COUNT,
                                                       MAX_ALLOWED_EXT_SEQ,
                                                       UNREAL_AUTH_SEQ_NUM,
                                                       CS_RESTRAINT_RANGE,
                                                       CS_RESTRAINT_ERROR,
                                                       HEME_LIKE_RES_NAMES,
                                                       SPECTRAL_DIM_TEMPLATE)
    from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
    from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from wwpdb.utils.nmr.nef.NEFTranslator import NEFTranslator
    from wwpdb.utils.nmr.AlignUtil import (LARGE_ASYM_ID,
                                           monDict3,
                                           emptyValue,
                                           protonBeginCode,
                                           pseProBeginCode,
                                           aminoProtonCode,
                                           carboxylCode,
                                           zincIonCode,
                                           calciumIonCode,
                                           getOneLetterCode,
                                           updatePolySeqRst,
                                           revertPolySeqRst,
                                           sortPolySeqRst,
                                           syncCompIdOfPolySeqRst,
                                           alignPolymerSequence,
                                           assignPolymerSequence,
                                           trimSequenceAlignment,
                                           updatePolySeqRstAmbig,
                                           retrieveAtomIdentFromMRMap,
                                           retrieveAtomIdFromMRMap,
                                           retrieveRemappedSeqId,
                                           retrieveRemappedSeqIdAndCompId,
                                           splitPolySeqRstForMultimers,
                                           splitPolySeqRstForExactNoes,
                                           retrieveRemappedChainId,
                                           splitPolySeqRstForNonPoly,
                                           retrieveRemappedNonPoly,
                                           splitPolySeqRstForBranched,
                                           retrieveOriginalSeqIdFromMRMap)
    from wwpdb.utils.nmr.CifToNmrStar import (get_first_sf_tag,
                                              set_sf_tag)
except ImportError:
    from nmr.io.CifReader import (CifReader,
                                  SYMBOLS_ELEMENT)
    from nmr.mr.ParserListenerUtil import (coordAssemblyChecker,
                                           translateToStdResName,
                                           translateToStdAtomName,
                                           translateToLigandName,
                                           hasInterChainRestraint,
                                           isLongRangeRestraint,
                                           isCyclicPolymer,
                                           isStructConn,
                                           guessCompIdFromAtomId,
                                           getMetalCoordOf,
                                           getRestraintName,
                                           contentSubtypeOf,
                                           incListIdCounter,
                                           decListIdCounter,
                                           getSaveframe,
                                           getPkLoop,
                                           getAltLoops,
                                           getAuxLoops,
                                           getPkRow,
                                           getPkGenCharRow,
                                           getPkCharRow,
                                           getPkChemShiftRow,
                                           getSpectralDimRow,
                                           getSpectralDimTransferRow,
                                           getMaxEffDigits,
                                           roundString,
                                           ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS,
                                           REPRESENTATIVE_MODEL_ID,
                                           REPRESENTATIVE_ALT_ID,
                                           MAX_PREF_LABEL_SCHEME_COUNT,
                                           MAX_ALLOWED_EXT_SEQ,
                                           UNREAL_AUTH_SEQ_NUM,
                                           CS_RESTRAINT_RANGE,
                                           CS_RESTRAINT_ERROR,
                                           HEME_LIKE_RES_NAMES,
                                           SPECTRAL_DIM_TEMPLATE)
    from nmr.ChemCompUtil import ChemCompUtil
    from nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from nmr.nef.NEFTranslator import NEFTranslator
    from nmr.AlignUtil import (LARGE_ASYM_ID,
                               monDict3,
                               emptyValue,
                               protonBeginCode,
                               pseProBeginCode,
                               aminoProtonCode,
                               carboxylCode,
                               zincIonCode,
                               calciumIonCode,
                               getOneLetterCode,
                               updatePolySeqRst,
                               revertPolySeqRst,
                               sortPolySeqRst,
                               syncCompIdOfPolySeqRst,
                               alignPolymerSequence,
                               assignPolymerSequence,
                               trimSequenceAlignment,
                               updatePolySeqRstAmbig,
                               retrieveAtomIdentFromMRMap,
                               retrieveAtomIdFromMRMap,
                               retrieveRemappedSeqId,
                               retrieveRemappedSeqIdAndCompId,
                               splitPolySeqRstForMultimers,
                               splitPolySeqRstForExactNoes,
                               retrieveRemappedChainId,
                               splitPolySeqRstForNonPoly,
                               retrieveRemappedNonPoly,
                               splitPolySeqRstForBranched,
                               retrieveOriginalSeqIdFromMRMap)
    from nmr.CifToNmrStar import (get_first_sf_tag,
                                  set_sf_tag)


CS_RANGE_MIN = CS_RESTRAINT_RANGE['min_inclusive']
CS_RANGE_MAX = CS_RESTRAINT_RANGE['max_inclusive']

CS_ERROR_MIN = CS_RESTRAINT_ERROR['min_exclusive']
CS_ERROR_MAX = CS_RESTRAINT_ERROR['max_exclusive']

C_CARBONYL_CENTER_MAX = 180
C_CARBONYL_CENTER_MIN = 170

C_AROMATIC_CENTER_MAX = 133
C_AROMATIC_CENTER_MIN = 128
C_AROMATIC_CENTER_MIN_TOR = 123

N_AMIDE_CENTER_MAX = C_AROMATIC_CENTER_MIN
N_AMIDE_CENTER_MIN = 115

C_ALL_CENTER_MAX = 90
C_ALL_CENTER_MIN = 60

C_ALIPHATIC_CENTER_MAX = C_ALL_CENTER_MIN
C_ALIPHATIC_CENTER_MIN = 30

C_METHYL_CENTER_MAX = C_ALIPHATIC_CENTER_MIN
C_METHYL_CENTER_MIN = 10

HN_AROMATIC_CENTER_MAX = 9
HN_AROMATIC_CENTER_MIN = 6

H_ALL_CENTER_MAX = HN_AROMATIC_CENTER_MIN
H_ALL_CENTER_MIN = 4

H_ALIPHATIC_CENTER_MAX = H_ALL_CENTER_MIN
H_ALIPHATIC_CENTER_MIN = 2

H_METHYL_CENTER_MAX = H_ALIPHATIC_CENTER_MIN
H_METHYL_CENTER_MIN = 0


PEAK_ASSIGNMENT_SEPARATOR_PAT = re.compile('[^0-9A-Za-z\'\"]+')
PEAK_ASSIGNMENT_RESID_PAT = re.compile('[0-9]+')
PEAK_HALF_SPIN_NUCLEUS = ('H', 'Q', 'M', 'C', 'N', 'P', 'F')


MIN_CORRCOEF_FOR_ONE_BOND_TRANSFER = 0.2


def guess_primary_dim_transfer_type(solid_state_nmr: bool, data_file_name: str, d: int, cur_spectral_dim: dict) -> str:
    """ Return expected primary dimensional transfer type from a given frequencies.
    """

    file_name = data_file_name.lower()

    is_noesy = 'noe' in file_name or 'roe' in file_name
    no_aromatic = all(_dict['spectral_region'] != 'C-aromatic' for _dict in cur_spectral_dim.values())

    acq_dim_id = 1

    for __d, __v in cur_spectral_dim.items():
        if 'freq_hint' in __v:
            __v['freq_hint'] = numpy.array(__v['freq_hint'], dtype=float)  # list -> numpy array
            if __v['freq_hint'].size > 0:
                center = numpy.mean(__v['freq_hint'])
                max_ppm = __v['freq_hint'].max()

                if __v['atom_isotope_number'] is None:
                    if (C_AROMATIC_CENTER_MIN_TOR if 'aro' in file_name or 'anoe' in file_name else C_AROMATIC_CENTER_MIN)\
                       < center <= C_AROMATIC_CENTER_MAX:
                        __v['atom_type'] = 'C'
                        __v['axis_code'] = 'C-aromatic'
                    elif N_AMIDE_CENTER_MIN < center <= N_AMIDE_CENTER_MAX:
                        __v['atom_type'] = 'N'
                        __v['atom_isotope_number'] = 15
                        __v['axis_code'] = 'N'
                    elif C_CARBONYL_CENTER_MIN <= center <= C_CARBONYL_CENTER_MAX:
                        __v['atom_type'] = 'C'
                        __v['atom_isotope_number'] = 13
                        __v['axis_code'] = 'CO'
                    elif HN_AROMATIC_CENTER_MIN < center <= HN_AROMATIC_CENTER_MAX:
                        __v['atom_type'] = 'H'
                        __v['atom_isotope_number'] = 1
                        __v['axis_code'] = 'HN/H-aromatic'
                    elif H_ALL_CENTER_MIN < center <= H_ALL_CENTER_MAX:
                        __v['atom_type'] = 'H'
                        __v['atom_isotope_number'] = 1
                        __v['axis_code'] = 'H'  # all
                    elif H_ALIPHATIC_CENTER_MIN < center <= H_ALIPHATIC_CENTER_MAX:
                        __v['atom_type'] = 'H'
                        __v['atom_isotope_number'] = 1
                        __v['axis_code'] = 'H-aliphatic' if max_ppm < 7 else 'H'
                    elif H_METHYL_CENTER_MIN < center <= H_METHYL_CENTER_MAX:
                        __v['atom_type'] = 'H'
                        __v['atom_isotope_number'] = 1
                        __v['axis_code'] = 'H-methyl' if max_ppm < 3 else 'H-aliphatic'
                    elif C_ALL_CENTER_MIN < center <= C_ALL_CENTER_MAX:
                        __v['atom_type'] = 'C'
                        __v['atom_isotope_number'] = 13
                        __v['axis_code'] = 'C'  # all
                    elif C_ALIPHATIC_CENTER_MIN < center <= C_ALIPHATIC_CENTER_MAX:
                        __v['atom_type'] = 'C'
                        __v['atom_isotope_number'] = 13
                        __v['axis_code'] = 'C-aliphatic'
                    elif C_METHYL_CENTER_MIN < center <= C_METHYL_CENTER_MAX:
                        __v['atom_type'] = 'C'
                        __v['atom_isotope_number'] = 13
                        __v['axis_code'] = 'C-methyl'

                isotope_number = __v['atom_isotope_number']

                if isotope_number is not None:
                    __v['acquisition'] = 'yes' if __d == acq_dim_id\
                        and (isotope_number == 1 or (isotope_number == 13 and solid_state_nmr)) else 'no'

                    if __d == 1 and __v['acquisition'] == 'no':
                        acq_dim_id = d

                    __v['under_sampling_type'] = 'not observed' if __v['acquisition'] == 'yes' else 'aliased'

            if __v['spectral_region'] is None and __v['freq_hint'].size > 0:
                atom_type = __v['atom_type']
                if C_AROMATIC_CENTER_MIN_TOR < center <= C_AROMATIC_CENTER_MAX and atom_type == 'C':
                    __v['spectral_region'] = 'C-aromatic'
                elif N_AMIDE_CENTER_MIN < center <= N_AMIDE_CENTER_MAX and atom_type == 'N':
                    __v['spectral_region'] = 'N'
                elif C_CARBONYL_CENTER_MIN <= center <= C_CARBONYL_CENTER_MAX and atom_type == 'C':
                    __v['spectral_region'] = 'CO'
                elif HN_AROMATIC_CENTER_MIN < center <= HN_AROMATIC_CENTER_MAX and atom_type == 'H':
                    __v['spectral_region'] = 'HN/H-aromatic'
                elif H_ALL_CENTER_MIN < center <= H_ALL_CENTER_MAX and atom_type == 'H':
                    __v['spectral_region'] = 'H'  # all
                elif H_ALIPHATIC_CENTER_MIN < center <= H_ALIPHATIC_CENTER_MAX and atom_type == 'H':
                    __v['spectral_region'] = 'H-aliphatic' if max_ppm < 7 else 'H'
                elif H_METHYL_CENTER_MIN < center <= H_METHYL_CENTER_MAX and atom_type == 'H':
                    __v['spectral_region'] = 'H-methyl' if max_ppm < 3 else 'H-aliphatic'
                elif C_ALL_CENTER_MIN < center <= C_ALL_CENTER_MAX and atom_type == 'C':
                    __v['spectral_region'] = 'C'  # all
                elif C_ALIPHATIC_CENTER_MIN < center <= C_ALIPHATIC_CENTER_MAX and atom_type == 'C':
                    __v['spectral_region'] = 'C-aliphatic'
                elif C_METHYL_CENTER_MIN < center <= C_METHYL_CENTER_MAX and atom_type == 'C':
                    __v['spectral_region'] = 'C-methyl'

            if __v['freq_hint'].size > 0 and d > 2 and __d >= 2\
               and not solid_state_nmr and __v['atom_isotope_number'] == 13:
                min_ppm = __v['freq_hint'].min()
                width = max_ppm - min_ppm
                if center < 100.0 and width < 50.0:
                    __v['under_sampling_type'] = 'fold'

            if __v['spectrometer_frequency'] is None and 'obs_freq_hint' in __v and len(__v['obs_freq_hint']) > 0:
                __v['spectrometer_frequency'] = collections.Counter(__v['obs_freq_hint']).most_common()[0][0]

            if 'obs_freq_hint' in __v:
                del __v['obs_freq_hint']

            if __v['spectrometer_frequency'] is not None and __v['sweep_width_units'] == 'ppm':
                row = [str(__v['sweep_width']), str(__v['spectrometer_frequency'])]
                max_eff_digits = getMaxEffDigits(row)

                __v['sweep_width'] = float(roundString(str(__v['sweep_width'] * __v['spectrometer_frequency']),
                                                       max_eff_digits))
                __v['sweep_width_units'] = 'Hz'

    for __v in cur_spectral_dim.values():
        if __v['axis_code'] == 'HN/H-aromatic':
            has_a = any(___v['spectral_region'] == 'C-aromatic' for ___v in cur_spectral_dim.values())
            __v['axis_code'] = 'H-aromatic' if has_a else 'H'
        if __v['spectral_region'] == 'HN/H-aromatic':
            has_a = any(___v['spectral_region'] == 'C-aromatic' for ___v in cur_spectral_dim.values())
            __v['spectral_region'] = 'H-aromatic' if has_a else 'H'
            __v['_spectral_region'] = 'H-aromatic' if has_a else 'HN'
        else:
            __v['_spectral_region'] = __v['spectral_region']

    cur_spectral_dim_transfer = []

    dim_to_code = {1: 'x', 2: 'y', 3: 'z', 4: 'a'}

    # onebond: 'Any transfer that connects only directly bonded atoms in this experiment'
    for _dim_id1, _dict1 in cur_spectral_dim.items():
        _region1 = _dict1['_spectral_region']
        if _region1 in ('HN', 'H-aliphatic', 'H-aromatic', 'H-methyl'):
            cases = 0
            max_corrcoef = 0.0
            for _dim_id2, _dict2 in cur_spectral_dim.items():
                _region2 = _dict2['_spectral_region']
                if (_region1 == 'HN' and _region2 == 'N')\
                   or ((_region1 == 'H-aliphatic' or (is_noesy and no_aromatic and _region1 == 'H'))
                       and (_region2 == 'C-aliphatic' or (is_noesy and _region2 == 'C')))\
                   or (_region1 == 'H-aromatic' and _region2 == 'C-aromatic')\
                   or (_region1 == 'H-methyl' and _region2 == 'C-methyl'):
                    if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                        if not any(_transfer for _transfer in cur_spectral_dim_transfer
                                   if _transfer['type'] == 'onebond'
                                   and (_dim_id1 in [_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']]
                                        or _dim_id2 in [_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']])):
                            if _dict1['freq_hint'].size < 2\
                               or numpy.max(_dict1['freq_hint']) == numpy.min(_dict1['freq_hint'])\
                               or numpy.max(_dict2['freq_hint']) == numpy.min(_dict2['freq_hint']):
                                continue
                            _corrcoef = numpy.corrcoef(_dict1['freq_hint'], _dict2['freq_hint'])[0][1]
                            if _corrcoef < 0.0 or (_corrcoef < MIN_CORRCOEF_FOR_ONE_BOND_TRANSFER and no_aromatic):
                                continue
                            cases += 1
                            max_corrcoef = max(max_corrcoef, _corrcoef)

                            if d == 3:
                                for _dim_id3, _dict3 in cur_spectral_dim.items():
                                    if _dim_id3 in (_dim_id1, _dim_id2):
                                        continue
                                    if _dict3['atom_type'] != _dict1['atom_type']:
                                        continue
                                    if not any(_transfer for _transfer in cur_spectral_dim_transfer
                                       if _transfer['type'] == 'onebond'
                                       and (_dim_id3 in [_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']]
                                            or _dim_id2 in [_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']])):
                                        if _dict3['freq_hint'].size < 2\
                                           or numpy.max(_dict3['freq_hint']) == numpy.min(_dict3['freq_hint'])\
                                           or numpy.max(_dict2['freq_hint']) == numpy.min(_dict2['freq_hint']):
                                            continue
                                        _corrcoef = numpy.corrcoef(_dict3['freq_hint'], _dict2['freq_hint'])[0][1]
                                        if _corrcoef < 0.0 or (_corrcoef < MIN_CORRCOEF_FOR_ONE_BOND_TRANSFER and no_aromatic):
                                            continue
                                        cases += 1
                                        max_corrcoef = max(max_corrcoef, _corrcoef)

            if cases == 1:
                for _dim_id2, _dict2 in cur_spectral_dim.items():
                    _region2 = _dict2['_spectral_region']
                    if (_region1 == 'HN' and _region2 == 'N')\
                       or ((_region1 == 'H-aliphatic' or (is_noesy and no_aromatic and _region1 == 'H'))
                           and (_region2 == 'C-aliphatic' or (is_noesy and _region2 == 'C')))\
                       or (_region1 == 'H-aromatic' and _region2 == 'C-aromatic')\
                       or (_region1 == 'H-methyl' and _region2 == 'C-methyl'):
                        if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                            if not any(_transfer for _transfer in cur_spectral_dim_transfer
                                       if _transfer['type'] == 'onebond'
                                       and (_dim_id1 in [_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']]
                                            or _dim_id2 in [_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']])):
                                transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                            'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                            'type': 'onebond',
                                            'indirect': 'no'}
                                if transfer in cur_spectral_dim_transfer:
                                    continue
                                cur_spectral_dim_transfer.append(transfer)

            elif cases > 1:
                for _dim_id2, _dict2 in cur_spectral_dim.items():
                    _region2 = _dict2['_spectral_region']
                    if (_region1 == 'HN' and _region2 == 'N')\
                       or ((_region1 == 'H-aliphatic' or (is_noesy and no_aromatic and _region1 == 'H'))
                           and (_region2 == 'C-aliphatic' or (is_noesy and _region2 == 'C')))\
                       or (_region1 == 'H-aromatic' and _region2 == 'C-aromatic')\
                       or (_region1 == 'H-methyl' and _region2 == 'C-methyl'):
                        if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                            if not any(_transfer for _transfer in cur_spectral_dim_transfer
                                       if _transfer['type'] == 'onebond'
                                       and (_dim_id1 in [_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']]
                                            or _dim_id2 in [_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']])):
                                if _dict1['freq_hint'].size < 2\
                                   or numpy.max(_dict1['freq_hint']) == numpy.min(_dict1['freq_hint'])\
                                   or numpy.max(_dict2['freq_hint']) == numpy.min(_dict2['freq_hint']):
                                    continue
                                _corrcoef = numpy.corrcoef(_dict1['freq_hint'], _dict2['freq_hint'])[0][1]
                                if _corrcoef < 0.0 or (_corrcoef < max_corrcoef and no_aromatic):
                                    continue
                                transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                            'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                            'type': 'onebond',
                                            'indirect': 'no'}
                                if transfer in cur_spectral_dim_transfer:
                                    continue
                                cur_spectral_dim_transfer.append(transfer)

    for _dim_id1, _dict1 in cur_spectral_dim.items():
        _region1 = _dict1['_spectral_region']
        if _region1 in ('HN', 'H-aliphatic', 'H-aromatic', 'H-methyl'):
            for _dim_id2, _dict2 in cur_spectral_dim.items():
                _region2 = _dict2['_spectral_region']
                if (_region1 == 'HN' and _region2 == 'N')\
                   or ((_region1 == 'H-aliphatic' or (is_noesy and no_aromatic and _region1 == 'H'))
                       and (_region2 == 'C-aliphatic' or (is_noesy and _region2 == 'C')))\
                   or (_region1 == 'H-aromatic' and _region2 == 'C-aromatic')\
                   or (_region1 == 'H-methyl' and _region2 == 'C-methyl'):
                    if _dict1['acquisition'] == 'no' and _dict2['acquisition'] == 'no':
                        if not any(_transfer for _transfer in cur_spectral_dim_transfer
                                   if _transfer['type'] == 'onebond'
                                   and (_dim_id1 in [_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']]
                                        or _dim_id2 in [_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']])):
                            if _dict1['freq_hint'].size < 2\
                               or numpy.max(_dict1['freq_hint']) == numpy.min(_dict1['freq_hint'])\
                               or numpy.max(_dict2['freq_hint']) == numpy.min(_dict2['freq_hint']):
                                continue
                            _corrcoef = numpy.corrcoef(_dict1['freq_hint'], _dict2['freq_hint'])[0][1]
                            if _corrcoef < 0.0 or (_corrcoef < max_corrcoef and no_aromatic):
                                continue
                            transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                        'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                        'type': 'onebond',
                                        'indirect': 'no'}
                            if transfer in cur_spectral_dim_transfer:
                                continue
                            cur_spectral_dim_transfer.append(transfer)

    # jcoupling: 'Transfer via direct J coupling over one or more bonds'
    if 'cosy' in file_name:
        if d == 2:
            for _dim_id1, _dict1 in cur_spectral_dim.items():
                _iso_num1 = _dict1['atom_isotope_number']
                if _iso_num1 == 1:
                    for _dim_id2, _dict2 in cur_spectral_dim.items():
                        if _dim_id1 == _dim_id2 or _iso_num1 != _dict2['atom_isotope_number']:
                            continue
                        if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                            transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                        'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                        'type': 'jcoupling',
                                        'indirect': 'no'}
                        if transfer in cur_spectral_dim_transfer:
                            continue
                        cur_spectral_dim_transfer.append(transfer)

        elif d == 3:
            for _dim_id1, _dict1 in cur_spectral_dim.items():
                _region1 = _dict1['_spectral_region']
                if _region1 == 'HN':
                    for _dim_id2, _dict2 in cur_spectral_dim.items():
                        if _dim_id1 == _dim_id2 or _dict2['atom_isotope_number'] not in (1, 13):
                            continue
                        if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                            transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                        'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                        'type': 'jcoupling',
                                        'indirect': 'yes'}
                            if transfer in cur_spectral_dim_transfer:
                                continue
                            cur_spectral_dim_transfer.append(transfer)
            for _dim_id1, _dict1 in cur_spectral_dim.items():
                _region1 = _dict1['_spectral_region']
                if _region1 == 'H-aliphatic':
                    for _dim_id2, _dict2 in cur_spectral_dim.items():
                        _isotope2 = _dict2['atom_isotope']
                        if _dim_id1 == _dim_id2 or _isotope2 not in (1, 13):
                            continue
                        if _isotope2 == 13\
                           and not any(_transfer for _transfer in cur_spectral_dim_transfer
                                       if _transfer['type'] == 'onebond'
                                       and {_dim_id1, _dim_id2} == {_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']}):
                            if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                                transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                            'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                            'type': 'jcoupling',
                                            'indirect': 'yes' if _isotope2 == 1 else 'no'}
                                if transfer in cur_spectral_dim_transfer:
                                    continue
                                cur_spectral_dim_transfer.append(transfer)

        elif d == 4:
            for _dim_id1, _dict1 in cur_spectral_dim.items():
                _region1 = _dict1['_spectral_region']
                if _region1 == 'HN':
                    for _dim_id2, _dict2 in cur_spectral_dim.items():
                        if _dim_id1 == _dim_id2 or _dict2['atom_isotope_number'] != 1:
                            continue
                        if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                            transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                        'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                        'type': 'jcoupling',
                                        'indirect': 'yes'}
                            if transfer in cur_spectral_dim_transfer:
                                continue
                            cur_spectral_dim_transfer.append(transfer)
            for _dim_id1, _dict1 in cur_spectral_dim.items():
                _region1 = _dict1['_spectral_region']
                if _region1 == 'H-aliphatic':
                    for _dim_id2, _dict2 in cur_spectral_dim.items():
                        if _dim_id1 == _dim_id2 or _dict2['atom_isotope_number'] != 1:
                            continue
                        if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                            transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                        'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                        'type': 'jcoupling',
                                        'indirect': 'no'}
                            if transfer in cur_spectral_dim_transfer:
                                continue
                            cur_spectral_dim_transfer.append(transfer)

    # jmultibond: 'Transfer via direct J coupling over multiple bonds'

    # relayed: 'Transfer via multiple successive J coupling steps (TOCSY relay)'
    if 'tocsy' in file_name:
        if d == 2:
            for _dim_id1, _dict1 in cur_spectral_dim.items():
                _iso_num1 = _dict1['atom_isotope_number']
                if _iso_num1 == 1:
                    for _dim_id2, _dict2 in cur_spectral_dim.items():
                        if _dim_id1 == _dim_id2 or _iso_num1 != _dict2['atom_isotope_number']:
                            continue
                        if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                            transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                        'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                        'type': 'relayed',
                                        'indirect': 'no'}
                        if transfer in cur_spectral_dim_transfer:
                            continue
                        cur_spectral_dim_transfer.append(transfer)

        elif d == 3:
            for _dim_id1, _dict1 in cur_spectral_dim.items():
                _region1 = _dict1['_spectral_region']
                if _region1 == 'HN':
                    for _dim_id2, _dict2 in cur_spectral_dim.items():
                        if _dim_id1 == _dim_id2 or _dict2['atom_isotope_number'] not in (1, 13):
                            continue
                        if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                            transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                        'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                        'type': 'relayed',
                                        'indirect': 'yes'}
                            if transfer in cur_spectral_dim_transfer:
                                continue
                            cur_spectral_dim_transfer.append(transfer)
            for _dim_id1, _dict1 in cur_spectral_dim.items():
                _region1 = _dict1['_spectral_region']
                if _region1 == 'H-aliphatic':
                    for _dim_id2, _dict2 in cur_spectral_dim.items():
                        _isotope2 = _dict2['atom_isotope']
                        if _dim_id1 == _dim_id2 or _isotope2 not in (1, 13):
                            continue
                        if _isotope2 == 13\
                           and not any(_transfer for _transfer in cur_spectral_dim_transfer
                                       if _transfer['type'] == 'onebond'
                                       and {_dim_id1, _dim_id2} == {_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']}):
                            if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                                transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                            'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                            'type': 'relayed',
                                            'indirect': 'yes' if _isotope2 == 1 else 'no'}
                                if transfer in cur_spectral_dim_transfer:
                                    continue
                                cur_spectral_dim_transfer.append(transfer)

        elif d == 4:
            for _dim_id1, _dict1 in cur_spectral_dim.items():
                _region1 = _dict1['_spectral_region']
                if _region1 == 'HN':
                    for _dim_id2, _dict2 in cur_spectral_dim.items():
                        if _dim_id1 == _dim_id2 or _dict2['atom_isotope_number'] != 1:
                            continue
                        if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                            transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                        'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                        'type': 'relayed',
                                        'indirect': 'yes'}
                            if transfer in cur_spectral_dim_transfer:
                                continue
                            cur_spectral_dim_transfer.append(transfer)
            for _dim_id1, _dict1 in cur_spectral_dim.items():
                _region1 = _dict1['_spectral_region']
                if _region1 == 'H-aliphatic':
                    for _dim_id2, _dict2 in cur_spectral_dim.items():
                        if _dim_id1 == _dim_id2 or _dict2['atom_isotope_number'] != 1:
                            continue
                        if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                            transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                        'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                        'type': 'relayed',
                                        'indirect': 'no'}
                            if transfer in cur_spectral_dim_transfer:
                                continue
                            cur_spectral_dim_transfer.append(transfer)

    # relayed-alternate: 'Relayed transfer where peaks from an odd resp. even number of transfer steps have opposite sign'

    # through-space: 'Any transfer that does not go through the covalent bonded skeleton
    if 'noe' in file_name or 'roe' in file_name:
        for _dim_id1, _dict1 in cur_spectral_dim.items():
            _region1 = _dict1['_spectral_region']
            if _region1 in ('H', 'HN', 'H-aliphatic', 'H-aromatic', 'H-methyl'):
                for _dim_id2, _dict2 in cur_spectral_dim.items():
                    if _dim_id1 == _dim_id2 or _dict1['atom_isotope_number'] != _dict2['atom_isotope_number']:
                        continue
                    if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                        transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                    'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                    'type': 'through-space',
                                    'indirect': 'yes'}
                        if transfer in cur_spectral_dim_transfer:
                            continue
                        cur_spectral_dim_transfer.append(transfer)
                        if d == 2 and _region1 == 'H-aliphatic':
                            _dict1['spectral_region'] = _dict2['spectral_region'] = 'H'  # all
                            if 'H-aliphatic' in (_dict1['axis_code'], _dict2['axis_code']):
                                _dict1['axis_code'] = f'H{dim_to_code[_dim_id1]}'
                                _dict2['axis_code'] = f'H{dim_to_code[_dim_id2]}'
                        if d == 3:
                            _transfer = next((_transfer for _transfer in cur_spectral_dim_transfer if _transfer['type'] == 'onebond'), None)
                            if _transfer is not None:
                                if _dim_id1 not in (_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']):
                                    if _region1 == 'H-aliphatic':
                                        _dict1['spectral_region'] = 'H'  # all
                                        if _dict1['axis_code'] == 'H-aliphatic':
                                            _dict1['axis_code'] = 'H'
                                elif _region1 == 'HN':
                                    _dict1['spectral_region'] = _dict1['axis_code'] = 'HN'
                                if _dim_id2 not in (_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']):
                                    if _region1 == 'H-aliphatic':
                                        _dict2['spectral_region'] = 'H'  # all
                                        if _dict2['axis_code'] == 'H-aliphatic':
                                            _dict2['axis_code'] = 'H'
                                elif _dict2['_spectral_region'] == 'HN':
                                    _dict2['spectral_region'] = _dict2['axis_code'] = 'HN'

    if solid_state_nmr and d == 2:
        if 'rfdr' in file_name or 'darr' in file_name:
            for _dim_id1, _dict1 in cur_spectral_dim.items():
                _iso_num1 = _dict1['atom_isotope_number']
                if _iso_num1 in (1, 13):
                    for _dim_id2, _dict2 in cur_spectral_dim.items():
                        if _dim_id1 == _dim_id2 or _iso_num1 != _dict2['atom_isotope_number']:
                            continue
                        if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                            transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                        'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                        'type': 'through-space',
                                        'indirect': 'yes'}
                            if transfer in cur_spectral_dim_transfer:
                                continue
                            cur_spectral_dim_transfer.append(transfer)
                            if d == 2 and _dict1['spectral_region'] == _dict2['spectral_region']:
                                nuc = _dict1[1]['spectral_regison'][0]
                                _dict1['spectral_region'] = _dict2['spectral_region'] = nuc
                                if _dict1['axis_code'] == _dict2['axis_code']:
                                    _dict1['axis_code'] = f'{nuc}{dim_to_code[_dim_id1]}'
                                    _dict2['axis_code'] = f'{nuc}{dim_to_code[_dim_id2]}'

        elif 'redor' in file_name:
            for _dim_id1, _dict1 in cur_spectral_dim.items():
                _iso_num1 = _dict1['atom_isotope_number']
                if _iso_num1 in (13, 15, 19, 31):
                    for _dim_id2, _dict2 in cur_spectral_dim.items():
                        _iso_num2 = _dict2['atom_isotope_number']
                        if _dim_id1 == _dim_id2 or _iso_num2 not in (13, 15, 19, 31) or _iso_num1 == _iso_num2:
                            continue
                        if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                            transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                        'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                        'type': 'through-space',
                                        'indirect': 'yes'}
                            if transfer in cur_spectral_dim_transfer:
                                continue
                            cur_spectral_dim_transfer.append(transfer)

    for _dim_id1, _dict1 in cur_spectral_dim.items():
        _region1 = _dict1['_spectral_region']
        if _region1 in ('H', 'HN', 'H-aliphatic', 'H-aromatic', 'H-methyl') and d > 2:
            for _dim_id2, _dict2 in cur_spectral_dim.items():
                if _dim_id1 == _dim_id2 or _dict1['atom_isotope_number'] != _dict2['atom_isotope_number']:
                    continue
                if not any(_transfer for _transfer in cur_spectral_dim_transfer
                           if {_dim_id1, _dim_id2} == {_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']}):
                    if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                        transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                    'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                    'type': 'through-space' if 'long_range' in cur_spectral_dim[1] else 'through-space?',  # optimistic inferencing?
                                    'indirect': 'yes'}
                        if transfer in cur_spectral_dim_transfer:
                            continue
                        cur_spectral_dim_transfer.append(transfer)

    for _dim_id1, _dict1 in cur_spectral_dim.items():
        _region1 = _dict1['_spectral_region']
        if _region1 == 'H' and d == 2:  # all
            for _dim_id2, _dict2 in cur_spectral_dim.items():
                if _dim_id1 == _dim_id2 or _dict1['_spectral_region'] != _region1:
                    continue
                if not any(_transfer for _transfer in cur_spectral_dim_transfer
                           if {_dim_id1, _dim_id2} == {_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']}):
                    if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                        transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                    'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                    'type': 'through-space' if 'long_range' in cur_spectral_dim[1] else 'through-space?',  # optimistic inferencing?
                                    'indirect': 'yes'}
                        if transfer in cur_spectral_dim_transfer:
                            continue
                        cur_spectral_dim_transfer.append(transfer)

    if solid_state_nmr and d == 2:
        for _dim_id1, _dict1 in cur_spectral_dim.items():
            _region1 = _dict1['_spectral_region']
            if _region1 == 'C':  # all
                for _dim_id2, _dict2 in cur_spectral_dim.items():
                    if _dim_id1 == _dim_id2 or _dict1['_spectral_region'] != _region1:
                        continue
                    if not any(_transfer for _transfer in cur_spectral_dim_transfer
                               if {_dim_id1, _dim_id2} == {_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']}):
                        if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                            transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                        'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                        'type': 'through-space' if 'long_range' in cur_spectral_dim[1] else 'through-space?',  # optimistic inferencing?
                                        'indirect': 'yes'}
                            if transfer in cur_spectral_dim_transfer:
                                continue
                            cur_spectral_dim_transfer.append(transfer)

        for _dim_id1, _dict1 in cur_spectral_dim.items():
            _iso_num1 = _dict1['atom_isotope_number']
            if _iso_num1 in (13, 15, 19, 31):
                for _dim_id2, _dict2 in cur_spectral_dim.items():
                    _iso_num2 = _dict2['atom_isotope_number']
                    if _dim_id1 == _dim_id2 or _iso_num2 not in (13, 15, 19, 31) or _iso_num1 == _iso_num2:
                        continue
                    if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                        transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                    'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                    'type': 'through-space' if 'long_range' in cur_spectral_dim[1] else 'through-space?',  # optimistic inferencing?
                                    'indirect': 'yes'}
                        if transfer in cur_spectral_dim_transfer:
                            continue
                        cur_spectral_dim_transfer.append(transfer)

    for __v in cur_spectral_dim.values():
        if 'freq_hint' in __v:
            del __v['freq_hint']

    primary_dim_transfer = ''
    for transfer in cur_spectral_dim_transfer:
        if transfer['type'] == 'through-space':
            primary_dim_transfer = transfer['type']
            break
        if transfer['type'] == 'through-space?'\
                and primary_dim_transfer != 'through-space':
            primary_dim_transfer = transfer['type']
        elif transfer['type'].startswith('relayed')\
                and primary_dim_transfer not in ('through-space', 'through-space?'):
            primary_dim_transfer = transfer['type']
        elif transfer['type'] == 'jmultibond'\
                and primary_dim_transfer not in ('through-space', 'through-space?', 'relayed', 'relayed-alternate'):
            primary_dim_transfer = transfer['type']
        elif transfer['type'] == 'jcoupling'\
                and primary_dim_transfer not in ('through-space', 'through-space?', 'relayed', 'relayed-alternate', 'jmultibond'):
            primary_dim_transfer = transfer['type']
        elif transfer['type'] == 'onebond'\
                and primary_dim_transfer == '':
            primary_dim_transfer = transfer['type']

    return primary_dim_transfer


class BasePKParserListener():

    file_type = None
    software_name = None

    debug = False
    ass_expr_debug = False
    internal = False

    createSfDict__ = False

    # atom name mapping of public MR file between the archive coordinates and submitted ones
    __mrAtomNameMapping = None

    # CCD accessing utility
    ccU = None

    # BMRB chemical shift statistics
    csStat = None

    # NEFTranslator
    nefT = None

    # Pairwise align
    pA = None

    # reasons for re-parsing request from the previous trial
    reasons = None

    # CIF reader
    cR = None
    __hasCoord = False

    # experimental method
    exptlMethod = ''

    # data item name for model ID in 'atom_site' category
    modelNumName = None

    # data item names for auth_asym_id, auth_seq_id, auth_atom_id in 'atom_site' category
    __authSeqId = None

    # coordinates information generated by ParserListenerUtil.coordAssemblyChecker()
    polySeq = None
    __altPolySeq = None
    nonPoly = None
    branched = None
    __nonPolySeq = None
    __coordAtomSite = None
    __coordUnobsRes = None
    __coordUnobsAtom = None
    __labelToAuthSeq = None
    __authToLabelSeq = None
    authToStarSeq = None
    authToOrigSeq = None
    __modResidue = None
    __splitLigand = None

    __entityAssembly = None
    authAsymIdSet = None
    compIdSet = None
    altCompIdSet = None
    polyPeptide = False
    polyDeoxyribonucleotide = False
    polyRibonucleotide = False

    offsetHolder = None
    __shiftNonPosSeq = None
    __defaultSegId = None

    representativeModelId = REPRESENTATIVE_MODEL_ID
    representativeAltId = REPRESENTATIVE_ALT_ID
    hasPolySeq = False
    hasNonPoly = False
    hasBranched = False
    hasNonPolySeq = False
    isFirstResidueAla = False
    __preferAuthSeq = True
    __extendAuthSeq = False

    # chain number dictionary
    chainNumberDict = None

    # extended residue key
    extResKey = None

    # polymer sequence of MR file
    polySeqRst = None
    polySeqRstFailed = None
    polySeqRstFailedAmbig = None
    compIdMap = None

    seqAlign = None
    chainAssign = None

    # current restraint subtype
    cur_subtype = ''
    cur_list_id = -1
    cur_spectral_dim = {}
    use_peak_row_format = True
    null_value = None
    null_string = None

    # spectral metadata
    num_of_dim = -1
    acq_dim_id = 1
    spectral_dim = {}
    spectral_dim_transfer = {}
    spectrum_name = None

    # whether to allow extended sequence temporary
    __allow_ext_seq = False

    # whether current assignment derived not from unreliable extra comment
    no_extra_comment = False

    # collection of atom selection set for multiple assignments to a peak
    atomSelectionSets = []
    asIsSets = []

    # collection of atom selection
    atomSelectionSet = []

    # collection of auxiliary atom selection
    auxAtomSelectionSet = []

    # collection of position selection
    positionSelection = []

    # collection of number selection
    numberSelection = []
    originalNumberSelection = []

    # collection of assignment (XEASY)
    assignmentSelection = []

    f = None
    warningMessage = None

    reasonsForReParsing = {}

    # original source MR file name
    __originalFileName = '.'

    # list id counter
    __listIdCounter = {}

    # reserved list ids for NMR data remediation Phase 2
    __reservedListIds = {}

    listIdInternal = {}

    # entry ID
    entryId = '.'

    # dictionary of pynmrstar saveframes
    sfDict = {}

    # list of assigned chemical shift loops
    __csLoops = None

    __cachedDictForStarAtom = {}

    def __init__(self, verbose: bool = True, log: IO = sys.stdout,
                 representativeModelId: int = REPRESENTATIVE_MODEL_ID,
                 representativeAltId: str = REPRESENTATIVE_ALT_ID,
                 mrAtomNameMapping: Optional[List[dict]] = None,
                 cR: Optional[CifReader] = None, caC: Optional[dict] = None, ccU: Optional[ChemCompUtil] = None,
                 csStat: Optional[BMRBChemShiftStat] = None, nefT: Optional[NEFTranslator] = None,
                 reasons: Optional[dict] = None):

        self.representativeModelId = representativeModelId
        self.representativeAltId = representativeAltId
        self.__mrAtomNameMapping = None if mrAtomNameMapping is None or len(mrAtomNameMapping) == 0 else mrAtomNameMapping

        self.cR = cR
        self.__hasCoord = cR is not None

        # CCD accessing utility
        self.ccU = ChemCompUtil(verbose, log) if ccU is None else ccU

        if self.__hasCoord:
            ret = coordAssemblyChecker(verbose, log, representativeModelId, representativeAltId,
                                       cR, self.ccU, caC)
            self.modelNumName = ret['model_num_name']
            self.__authSeqId = ret['auth_seq_id']
            self.polySeq = ret['polymer_sequence']
            self.__altPolySeq = ret['alt_polymer_sequence']
            self.nonPoly = ret['non_polymer']
            self.branched = ret['branched']
            self.__coordAtomSite = ret['coord_atom_site']
            self.__coordUnobsRes = ret['coord_unobs_res']
            self.__coordUnobsAtom = ret['coord_unobs_atom'] if 'coord_unobs_atom' in ret else {}
            self.__labelToAuthSeq = ret['label_to_auth_seq']
            self.__authToLabelSeq = ret['auth_to_label_seq']
            self.authToStarSeq = ret['auth_to_star_seq']
            self.authToOrigSeq = ret['auth_to_orig_seq']
            self.__modResidue = ret['mod_residue']
            self.__splitLigand = ret['split_ligand']
            self.__entityAssembly = ret['entity_assembly']

            exptl = cR.getDictList('exptl')
            if len(exptl) > 0:
                for item in exptl:
                    if 'method' in item:
                        if 'NMR' in item['method']:
                            self.exptlMethod = item['method']

        self.offsetHolder = {}

        self.hasPolySeq = self.polySeq is not None and len(self.polySeq) > 0
        self.hasNonPoly = self.nonPoly is not None and len(self.nonPoly) > 0
        self.hasBranched = self.branched is not None and len(self.branched) > 0
        if self.hasNonPoly or self.hasBranched:
            self.hasNonPolySeq = True
            if self.hasNonPoly and self.hasBranched:
                self.nonPolySeq = self.nonPoly
                self.nonPolySeq.extend(self.branched)
            elif self.hasNonPoly:
                self.nonPolySeq = self.nonPoly
            else:
                self.nonPolySeq = self.branched

        if self.hasPolySeq:
            self.authAsymIdSet = set(ps['auth_chain_id'] for ps in self.polySeq)
            self.compIdSet = set()
            self.altCompIdSet = set()
            for ps in self.polySeq:
                self.compIdSet.update(set(ps['comp_id']))
                if 'auth_comp_id' in ps and ps['comp_id'] != ps['auth_comp_id']:
                    self.altCompIdSet.update(set(ps['auth_comp_id']))
            if self.hasNonPolySeq:
                for np in self.nonPolySeq:
                    self.compIdSet.update(set(np['comp_id']))
                    if 'auth_comp_id' in np and np['comp_id'] != np['auth_comp_id']:
                        self.altCompIdSet.update(set(np['auth_comp_id']))
                self.authAsymIdSet.update(set(np['auth_chain_id'] for np in self.nonPolySeq))
            for entity in self.__entityAssembly:
                if 'entity_poly_type' in entity:
                    poly_type = entity['entity_poly_type']
                    if poly_type.startswith('polypeptide'):
                        self.polyPeptide = True
                    elif poly_type == 'polydeoxyribonucleotide':
                        self.polyDeoxyribonucleotide = True
                    elif poly_type == 'polyribonucleotide':
                        self.polyRibonucleotide = True
            if 'ALA' in self.compIdSet:
                self.isFirstResidueAla = any(ps['comp_id'][0] == 'ALA' for ps in self.polySeq)

        # BMRB chemical shift statistics
        self.csStat = BMRBChemShiftStat(verbose, log, self.ccU) if csStat is None else csStat

        # NEFTranslator
        self.nefT = NEFTranslator(verbose, log, self.ccU, self.csStat) if nefT is None else nefT

        # Pairwise align
        if self.hasPolySeq:
            self.pA = PairwiseAlign()
            self.pA.setVerbose(verbose)

        # reasons for re-parsing request from the previous trial
        self.reasons = reasons
        self.__preferAuthSeqCount = 0
        self.__preferLabelSeqCount = 0

        self.reasonsForReParsing = {}  # reset to prevent interference from the previous run

        self.peaks2D = 0
        self.peaks3D = 0
        self.peaks4D = 0

        self.sfDict = {}

        self.__cachedDictForStarAtom = {}

    def setDebugMode(self, debug: bool):
        self.debug = debug

    def createSfDict(self, createSfDict: bool):
        self.createSfDict__ = createSfDict

    def setOriginaFileName(self, originalFileName: str):
        self.__originalFileName = originalFileName

    def setListIdCounter(self, listIdCounter: dict):
        self.__listIdCounter = listIdCounter

    def setReservedListIds(self, reservedListIds: dict):
        self.__reservedListIds = reservedListIds

    def setEntryId(self, entryId: str):
        self.entryId = entryId

    def setCsLoops(self, csLoops: List[dict]):
        self.__csLoops = csLoops

    def enter(self):
        self.num_of_dim = -1
        self.acq_dim_id = 1
        self.cur_spectral_dim = {}
        self.spectral_dim = {}
        self.spectral_dim_transfer = {}
        self.listIdInternal = {}
        self.chainNumberDict = {}
        self.extResKey = []
        self.polySeqRst = []
        self.polySeqRstFailed = []
        self.polySeqRstFailedAmbig = []
        self.compIdMap = {}
        self.f = []

    def exit(self, spectrum_names: Optional[dict] = None):

        self.fillPkAuxLoops(spectrum_names)

        try:

            if self.hasPolySeq and self.polySeqRst is not None:
                sortPolySeqRst(self.polySeqRst,
                               None if self.reasons is None else self.reasons.get('non_poly_remap'))

                self.seqAlign, _ = alignPolymerSequence(self.pA, self.polySeq, self.polySeqRst,
                                                        resolvedMultimer=self.reasons is not None)
                self.chainAssign, message = assignPolymerSequence(self.pA, self.ccU, self.file_type, self.polySeq, self.polySeqRst, self.seqAlign)

                if len(message) > 0:
                    self.f.extend(message)

                if self.chainAssign is not None:

                    if len(self.polySeq) == len(self.polySeqRst):

                        chain_mapping = {}

                        for ca in self.chainAssign:
                            ref_chain_id = ca['ref_chain_id']
                            test_chain_id = ca['test_chain_id']

                            if ref_chain_id != test_chain_id:
                                chain_mapping[test_chain_id] = ref_chain_id

                        if len(chain_mapping) == len(self.polySeq):

                            for ps in self.polySeqRst:
                                if ps['chain_id'] in chain_mapping:
                                    ps['chain_id'] = chain_mapping[ps['chain_id']]

                            self.seqAlign, _ = alignPolymerSequence(self.pA, self.polySeq, self.polySeqRst,
                                                                    resolvedMultimer=self.reasons is not None)
                            self.chainAssign, _ = assignPolymerSequence(self.pA, self.ccU, self.file_type, self.polySeq, self.polySeqRst, self.seqAlign)

                    trimSequenceAlignment(self.seqAlign, self.chainAssign)

                    if self.reasons is None and any(f for f in self.f
                                                    if '[Atom not found]' in f or '[Sequence mismatch]' in f):

                        seqIdRemap = []

                        cyclicPolymer = {}

                        for ca in self.chainAssign:
                            ref_chain_id = ca['ref_chain_id']
                            test_chain_id = ca['test_chain_id']

                            sa = next(sa for sa in self.seqAlign
                                      if sa['ref_chain_id'] == ref_chain_id
                                      and sa['test_chain_id'] == test_chain_id)

                            poly_seq_model = next(ps for ps in self.polySeq
                                                  if ps['auth_chain_id'] == ref_chain_id)
                            poly_seq_rst = next(ps for ps in self.polySeqRst
                                                if ps['chain_id'] == test_chain_id)

                            seq_id_mapping = {}
                            offset = None
                            for ref_seq_id, mid_code, test_seq_id in zip(sa['ref_seq_id'], sa['mid_code'], sa['test_seq_id']):
                                if test_seq_id is None:
                                    continue
                                if mid_code == '|':
                                    try:
                                        seq_id_mapping[test_seq_id] = next(auth_seq_id for auth_seq_id, seq_id
                                                                           in zip(poly_seq_model['auth_seq_id'], poly_seq_model['seq_id'])
                                                                           if seq_id == ref_seq_id and isinstance(auth_seq_id, int))
                                        if offset is None:
                                            offset = seq_id_mapping[test_seq_id] - test_seq_id
                                    except StopIteration:
                                        pass
                                elif mid_code == ' ' and test_seq_id in poly_seq_rst['seq_id']:
                                    idx = poly_seq_rst['seq_id'].index(test_seq_id)
                                    if poly_seq_rst['comp_id'][idx] == '.' and poly_seq_rst['auth_comp_id'][idx] not in emptyValue:
                                        seq_id_mapping[test_seq_id] = next(auth_seq_id for auth_seq_id, seq_id
                                                                           in zip(poly_seq_model['auth_seq_id'], poly_seq_model['seq_id'])
                                                                           if seq_id == ref_seq_id and isinstance(auth_seq_id, int))

                            if offset is not None and all(v - k == offset for k, v in seq_id_mapping.items()):
                                test_seq_id_list = list(seq_id_mapping.keys())
                                min_test_seq_id = min(test_seq_id_list)
                                max_test_seq_id = max(test_seq_id_list)
                                for test_seq_id in range(min_test_seq_id + 1, max_test_seq_id):
                                    if test_seq_id not in seq_id_mapping:
                                        seq_id_mapping[test_seq_id] = test_seq_id + offset

                            if ref_chain_id not in cyclicPolymer:
                                cyclicPolymer[ref_chain_id] =\
                                    isCyclicPolymer(self.cR, self.polySeq, ref_chain_id,
                                                    self.representativeModelId, self.representativeAltId, self.modelNumName)

                            if cyclicPolymer[ref_chain_id]:

                                poly_seq_model = next(ps for ps in self.polySeq
                                                      if ps['auth_chain_id'] == ref_chain_id)

                                offset = None
                                for seq_id, comp_id in zip(poly_seq_rst['seq_id'], poly_seq_rst['comp_id']):
                                    if seq_id is not None and seq_id not in seq_id_mapping:
                                        _seq_id = next((_seq_id for _seq_id, _comp_id in zip(poly_seq_model['seq_id'], poly_seq_model['comp_id'])
                                                        if _seq_id not in seq_id_mapping.values() and _comp_id == comp_id), None)
                                        if _seq_id is not None:
                                            offset = seq_id - _seq_id
                                            break

                                if offset is not None:
                                    for seq_id in poly_seq_rst['seq_id']:
                                        if seq_id is not None and seq_id not in seq_id_mapping:
                                            seq_id_mapping[seq_id] = seq_id - offset

                            if any(k for k, v in seq_id_mapping.items() if k != v)\
                               and not any(k for k, v in seq_id_mapping.items()
                                           if v in poly_seq_model['seq_id']
                                           and k == poly_seq_model['auth_seq_id'][poly_seq_model['seq_id'].index(v)]):
                                seqIdRemap.append({'chain_id': test_chain_id, 'seq_id_dict': seq_id_mapping})

                        if len(seqIdRemap) > 0:
                            if 'seq_id_remap' not in self.reasonsForReParsing:
                                self.reasonsForReParsing['seq_id_remap'] = seqIdRemap

                        if any(ps for ps in self.polySeq if 'identical_chain_id' in ps):
                            polySeqRst, chainIdMapping = splitPolySeqRstForMultimers(self.pA, self.polySeq, self.polySeqRst, self.chainAssign)

                            if polySeqRst is not None and (not self.hasNonPoly or len(self.polySeq) // len(self.nonPoly) in (1, 2)):
                                self.polySeqRst = polySeqRst
                                if 'chain_id_remap' not in self.reasonsForReParsing:
                                    self.reasonsForReParsing['chain_id_remap'] = chainIdMapping

                        if len(self.polySeq) == 1 and len(self.polySeqRst) == 1:
                            polySeqRst, chainIdMapping, _ =\
                                splitPolySeqRstForExactNoes(self.pA, self.polySeq, self.polySeqRst, self.chainAssign)

                            if polySeqRst is not None:
                                self.polySeqRst = polySeqRst
                                if 'chain_id_clone' not in self.reasonsForReParsing:
                                    self.reasonsForReParsing['chain_id_clone'] = chainIdMapping

                        if self.hasNonPoly:
                            polySeqRst, nonPolyMapping = splitPolySeqRstForNonPoly(self.ccU, self.nonPoly, self.polySeqRst,
                                                                                   self.seqAlign, self.chainAssign)

                            if polySeqRst is not None:
                                self.polySeqRst = polySeqRst
                                if 'non_poly_remap' not in self.reasonsForReParsing:
                                    self.reasonsForReParsing['non_poly_remap'] = nonPolyMapping

                        if self.hasBranched:
                            polySeqRst, branchedMapping = splitPolySeqRstForBranched(self.pA, self.polySeq, self.branched, self.polySeqRst,
                                                                                     self.chainAssign)

                            if polySeqRst is not None:
                                self.polySeqRst = polySeqRst
                                if 'branched_remap' not in self.reasonsForReParsing:
                                    self.reasonsForReParsing['branched_remap'] = branchedMapping

                        if len(self.polySeqRstFailed) > 0:
                            sortPolySeqRst(self.polySeqRstFailed)
                            if not any(f for f in self.f if '[Sequence mismatch]' in f):  # 2n6y
                                syncCompIdOfPolySeqRst(self.polySeqRstFailed, self.compIdMap)  # 2mx9

                            seqAlignFailed, _ = alignPolymerSequence(self.pA, self.polySeq, self.polySeqRstFailed)
                            chainAssignFailed, _ = assignPolymerSequence(self.pA, self.ccU, self.file_type,
                                                                         self.polySeq, self.polySeqRstFailed, seqAlignFailed)

                            if chainAssignFailed is not None:
                                seqIdRemapFailed = []

                                uniq_ps = not any('identical_chain_id' in ps for ps in self.polySeq)

                                for ca in chainAssignFailed:
                                    if ca['conflict'] > 0:
                                        continue
                                    ref_chain_id = ca['ref_chain_id']
                                    test_chain_id = ca['test_chain_id']

                                    sa = next((sa for sa in seqAlignFailed
                                               if sa['ref_chain_id'] == ref_chain_id
                                               and sa['test_chain_id'] == test_chain_id), None)

                                    if sa is None:
                                        continue

                                    poly_seq_model = next(ps for ps in self.polySeq
                                                          if ps['auth_chain_id'] == ref_chain_id)

                                    seq_id_mapping = {}
                                    for ref_seq_id, mid_code, test_seq_id in zip(sa['ref_seq_id'], sa['mid_code'], sa['test_seq_id']):
                                        if test_seq_id is None:
                                            continue
                                        if mid_code == '|':
                                            try:
                                                seq_id_mapping[test_seq_id] = next(auth_seq_id for auth_seq_id, seq_id
                                                                                   in zip(poly_seq_model['auth_seq_id'], poly_seq_model['seq_id'])
                                                                                   if seq_id == ref_seq_id and isinstance(auth_seq_id, int))
                                            except StopIteration:
                                                if uniq_ps:
                                                    seq_id_mapping[test_seq_id] = ref_seq_id

                                    offset = None
                                    offsets = [v - k for k, v in seq_id_mapping.items()]
                                    if len(offsets) > 0 and ('gap_in_auth_seq' not in poly_seq_model or not poly_seq_model['gap_in_auth_seq']):
                                        offsets = collections.Counter(offsets).most_common()
                                        if len(offsets) > 1:
                                            offset = offsets[0][0]
                                            for k, v in seq_id_mapping.items():
                                                if v - k != offset:
                                                    seq_id_mapping[k] = k + offset

                                    if uniq_ps and offset is not None and len(seq_id_mapping) > 0\
                                       and ('gap_in_auth_seq' not in poly_seq_model or not poly_seq_model['gap_in_auth_seq']):
                                        for ref_seq_id, mid_code, test_seq_id, ref_code, test_code in zip(sa['ref_seq_id'], sa['mid_code'], sa['test_seq_id'],
                                                                                                          sa['ref_code'], sa['test_code']):
                                            if test_seq_id is None:
                                                continue
                                            if mid_code == '|' and test_seq_id not in seq_id_mapping:
                                                seq_id_mapping[test_seq_id] = test_seq_id + offset
                                            elif ref_code != '.' and test_code == '.':
                                                seq_id_mapping[test_seq_id] = test_seq_id + offset

                                    if any(k for k, v in seq_id_mapping.items() if k != v)\
                                       and not any(k for k, v in seq_id_mapping.items()
                                                   if v in poly_seq_model['seq_id']
                                                   and k == poly_seq_model['auth_seq_id'][poly_seq_model['seq_id'].index(v)]):
                                        seqIdRemapFailed.append({'chain_id': ref_chain_id, 'seq_id_dict': seq_id_mapping,
                                                                 'comp_id_set': list(set(poly_seq_model['comp_id']))})

                                if len(seqIdRemapFailed) > 0:
                                    if 'chain_seq_id_remap' not in self.reasonsForReParsing:
                                        seqIdRemap = self.reasonsForReParsing['seq_id_remap'] if 'seq_id_remap' in self.reasonsForReParsing else []
                                        if len(seqIdRemap) != len(seqIdRemapFailed)\
                                           or seqIdRemap[0]['chain_id'] != seqIdRemapFailed[0]['chain_id']\
                                           or not all(src_seq_id in seqIdRemap[0] for src_seq_id in seqIdRemapFailed[0]):
                                            self.reasonsForReParsing['chain_seq_id_remap'] = seqIdRemapFailed

                                else:
                                    for ps in self.polySeqRstFailed:
                                        for ca in self.chainAssign:
                                            ref_chain_id = ca['ref_chain_id']
                                            test_chain_id = ca['test_chain_id']

                                            if test_chain_id != ps['chain_id']:
                                                continue

                                            sa = next(sa for sa in self.seqAlign
                                                      if sa['ref_chain_id'] == ref_chain_id
                                                      and sa['test_chain_id'] == test_chain_id)

                                            if len(sa['test_seq_id']) != len(sa['ref_seq_id']):
                                                continue

                                            poly_seq_model = next(ps for ps in self.polySeq
                                                                  if ps['auth_chain_id'] == ref_chain_id)

                                            seq_id_mapping, comp_id_mapping = {}, {}

                                            for seq_id, comp_id in zip(ps['seq_id'], ps['comp_id']):
                                                if seq_id in sa['test_seq_id']:
                                                    idx = sa['test_seq_id'].index(seq_id)
                                                    auth_seq_id = sa['ref_seq_id'][idx]
                                                    seq_id_mapping[seq_id] = auth_seq_id
                                                    comp_id_mapping[seq_id] = comp_id
                                            if any(k for k, v in seq_id_mapping.items() if k != v)\
                                               or ('label_seq_scheme' not in self.reasonsForReParsing
                                                   and all(v not in poly_seq_model['auth_seq_id'] for v in seq_id_mapping.values())):
                                                seqIdRemapFailed.append({'chain_id': ref_chain_id, 'seq_id_dict': seq_id_mapping,
                                                                         'comp_id_dict': comp_id_mapping})

                                    if len(seqIdRemapFailed) > 0:
                                        if 'ext_chain_seq_id_remap' not in self.reasonsForReParsing:
                                            seqIdRemap = self.reasonsForReParsing['seq_id_remap'] if 'seq_id_remap' in self.reasonsForReParsing else []
                                            if len(seqIdRemap) != len(seqIdRemapFailed)\
                                               or seqIdRemap[0]['chain_id'] != seqIdRemapFailed[0]['chain_id']\
                                               or not all(src_seq_id in seqIdRemap[0] for src_seq_id in seqIdRemapFailed[0]):
                                                self.reasonsForReParsing['ext_chain_seq_id_remap'] = seqIdRemapFailed

            if 'local_seq_scheme' in self.reasonsForReParsing:
                if 'non_poly_remap' in self.reasonsForReParsing or 'branched_remap' in self.reasonsForReParsing:
                    del self.reasonsForReParsing['local_seq_scheme']
                elif 'seq_id_remap' in self.reasonsForReParsing:
                    del self.reasonsForReParsing['local_seq_scheme']
                elif 'chain_seq_id_remap' in self.reasonsForReParsing:
                    del self.reasonsForReParsing['local_seq_scheme']
                elif 'ext_chain_seq_id_remap' in self.reasonsForReParsing:
                    del self.reasonsForReParsing['local_seq_scheme']

            if 'local_seq_scheme' in self.reasonsForReParsing and len(self.reasonsForReParsing) == 1:
                sortPolySeqRst(self.polySeqRstFailed)
                if len(self.polySeqRstFailed) > 0:
                    self.reasonsForReParsing['extend_seq_scheme'] = self.polySeqRstFailed
                del self.reasonsForReParsing['local_seq_scheme']

        finally:
            self.warningMessage = sorted(list(set(self.f)), key=self.f.index)

    def initSpectralDim(self):
        if self.num_of_dim not in (2, 3, 4):
            return
        self.cur_subtype = f'peak{self.num_of_dim}d'
        if self.num_of_dim not in self.listIdInternal:
            self.listIdInternal[self.num_of_dim] = 0
        self.listIdInternal[self.num_of_dim] += 1
        self.cur_list_id = self.listIdInternal[self.num_of_dim]
        if self.num_of_dim not in self.spectral_dim:
            self.spectral_dim[self.num_of_dim] = {}
        if self.cur_list_id not in self.spectral_dim[self.num_of_dim]:
            self.spectral_dim[self.num_of_dim][self.cur_list_id] = {}
        for _dim_id in range(1, self.num_of_dim + 1):
            self.spectral_dim[self.num_of_dim][self.cur_list_id][_dim_id] =\
                copy.copy(SPECTRAL_DIM_TEMPLATE
                          if len(self.cur_spectral_dim) == 0
                          or _dim_id not in self.cur_spectral_dim
                          else self.cur_spectral_dim[_dim_id])
            self.spectral_dim[self.num_of_dim][self.cur_list_id][_dim_id]['freq_hint'] = []  # list -> numpy array before exit()
            if self.file_type == 'nm-pea-pip':
                self.spectral_dim[self.num_of_dim][self.cur_list_id][_dim_id]['obs_freq_hint'] = []
        if self.num_of_dim not in self.spectral_dim_transfer:
            self.spectral_dim_transfer[self.num_of_dim] = {}
        if self.cur_list_id not in self.spectral_dim_transfer[self.num_of_dim]:
            self.spectral_dim_transfer[self.num_of_dim][self.cur_list_id] = []
        if self.num_of_dim == 2:
            self.peaks2D = 0
        if self.num_of_dim == 3:
            self.peaks3D = 0
        if self.num_of_dim == 4:
            self.peaks4D = 0
        self.use_peak_row_format = True

    def testAssignment(self, _dim_id: int, _assign: List[dict], _label: str) -> Tuple[bool, Optional[str]]:
        cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id][_dim_id]
        if cur_spectral_dim['atom_type'] is not None:
            if len(_assign) > 0 and 'atom_id' in _assign[0]:
                atom_type = cur_spectral_dim['atom_type']
                _atom_type = _assign[0]['atom_id'][0]
                if atom_type == _atom_type:
                    return True, None
                concat_type = _atom_type + atom_type
                if concat_type in _label:
                    _label = _label.replace(concat_type, atom_type)
                    return False, _label
                return False, None
        return True, None

    def validateAtomType(self, _dim_id: int, atom_type: str) -> bool:
        cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id][_dim_id]
        if cur_spectral_dim['atom_type'] is not None:
            if cur_spectral_dim['atom_type'] == atom_type:
                cur_spectral_dim['fixed'] = True  # be robust against interference of unreliable assignments (bmr36675)
                return True
            if 'fixed' in cur_spectral_dim:  # XEASY INNAME label is not reliable (2kj5)
                return False
            if atom_type in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS:
                cur_spectral_dim['fixed'] = True
                cur_spectral_dim['atom_type'] = None
                cur_spectral_dim['axis_code'] = None
                cur_spectral_dim['atom_isotope_number'] = None
        if atom_type in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS:
            cur_spectral_dim['atom_type'] = atom_type
            cur_spectral_dim['axis_code'] = atom_type
            cur_spectral_dim['atom_isotope_number'] = ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS[atom_type][0]
            return True
        return False

    def fillPkAuxLoops(self, spectrum_names: Optional[dict]):
        if len(self.spectral_dim) > 0:
            dim_to_code = {1: 'x', 2: 'y', 3: 'z', 4: 'a'}

            for d, v in self.spectral_dim.items():
                for _id, _v in v.items():

                    file_name = self.__originalFileName.lower()
                    alt_file_name = ''
                    try:
                        if spectrum_names is not None:
                            alt_file_name = spectrum_names[d][_id].lower()
                    except (KeyError, AttributeError):
                        pass

                    _file_names = (file_name, alt_file_name)

                    self.acq_dim_id = 1

                    for __d, __v in _v.items():
                        if 'freq_hint' in __v:
                            __v['freq_hint'] = numpy.array(__v['freq_hint'], dtype=float)  # list -> numpy array
                            if __v['freq_hint'].size > 0:
                                center = numpy.mean(__v['freq_hint'])
                                max_ppm = __v['freq_hint'].max()

                                if __v['atom_isotope_number'] is None:
                                    if (C_AROMATIC_CENTER_MIN_TOR if any('aro' in n for n in _file_names) or any('anoe' in n for n in _file_names) else C_AROMATIC_CENTER_MIN)\
                                       < center <= C_AROMATIC_CENTER_MAX:
                                        __v['atom_type'] = 'C'
                                        __v['atom_isotope_number'] = 13
                                        __v['axis_code'] = 'C-aromatic'
                                    elif N_AMIDE_CENTER_MIN < center <= N_AMIDE_CENTER_MAX:
                                        __v['atom_type'] = 'N'
                                        __v['atom_isotope_number'] = 15
                                        __v['axis_code'] = 'N'
                                    elif C_CARBONYL_CENTER_MIN <= center <= C_CARBONYL_CENTER_MAX:
                                        __v['atom_type'] = 'C'
                                        __v['atom_isotope_number'] = 13
                                        __v['axis_code'] = 'CO'
                                    elif HN_AROMATIC_CENTER_MIN < center <= HN_AROMATIC_CENTER_MAX:
                                        __v['atom_type'] = 'H'
                                        __v['atom_isotope_number'] = 1
                                        __v['axis_code'] = 'HN/H-aromatic'
                                    elif H_ALL_CENTER_MIN < center <= H_ALL_CENTER_MAX:
                                        __v['atom_type'] = 'H'
                                        __v['atom_isotope_number'] = 1
                                        __v['axis_code'] = 'H'  # all
                                    elif H_ALIPHATIC_CENTER_MIN < center <= H_ALIPHATIC_CENTER_MAX:
                                        __v['atom_type'] = 'H'
                                        __v['atom_isotope_number'] = 1
                                        __v['axis_code'] = 'H-aliphatic' if max_ppm < 7 else 'H'
                                    elif H_METHYL_CENTER_MIN < center <= H_METHYL_CENTER_MAX:
                                        __v['atom_type'] = 'H'
                                        __v['atom_isotope_number'] = 1
                                        __v['axis_code'] = 'H-methyl' if max_ppm < 3 else 'H-aliphatic'
                                    elif C_ALL_CENTER_MIN < center <= C_ALL_CENTER_MAX:
                                        __v['atom_type'] = 'C'
                                        __v['atom_isotope_number'] = 13
                                        __v['axis_code'] = 'C'  # all
                                    elif C_ALIPHATIC_CENTER_MIN < center <= C_ALIPHATIC_CENTER_MAX:
                                        __v['atom_type'] = 'C'
                                        __v['atom_isotope_number'] = 13
                                        __v['axis_code'] = 'C-aliphatic'
                                    elif C_METHYL_CENTER_MIN < center <= C_METHYL_CENTER_MAX:
                                        __v['atom_type'] = 'C'
                                        __v['atom_isotope_number'] = 13
                                        __v['axis_code'] = 'C-methyl'

                                isotope_number = __v['atom_isotope_number']

                                if isotope_number is not None:
                                    __v['acquisition'] = 'yes' if __d == self.acq_dim_id\
                                        and (isotope_number == 1 or (isotope_number == 13 and self.exptlMethod == 'SOLID-STATE NMR')) else 'no'

                                    if __d == 1 and __v['acquisition'] == 'no':
                                        self.acq_dim_id = d

                                    __v['under_sampling_type'] = 'not observed' if __v['acquisition'] == 'yes' else 'aliased'

                            if __v['spectral_region'] is None and __v['freq_hint'].size > 0:
                                atom_type = __v['atom_type']
                                if C_AROMATIC_CENTER_MIN_TOR < center <= C_AROMATIC_CENTER_MAX and atom_type == 'C':
                                    __v['spectral_region'] = 'C-aromatic'
                                elif N_AMIDE_CENTER_MIN < center <= N_AMIDE_CENTER_MAX and atom_type == 'N':
                                    __v['spectral_region'] = 'N'
                                elif C_CARBONYL_CENTER_MIN <= center <= C_CARBONYL_CENTER_MAX and atom_type == 'C':
                                    __v['spectral_region'] = 'CO'
                                elif HN_AROMATIC_CENTER_MIN < center <= HN_AROMATIC_CENTER_MAX and atom_type == 'H':
                                    __v['spectral_region'] = 'HN/H-aromatic'
                                elif H_ALL_CENTER_MIN < center <= H_ALL_CENTER_MAX and atom_type == 'H':
                                    __v['spectral_region'] = 'H'  # all
                                elif H_ALIPHATIC_CENTER_MIN < center <= H_ALIPHATIC_CENTER_MAX and atom_type == 'H':
                                    __v['spectral_region'] = 'H-aliphatic' if max_ppm < 7 else 'H'
                                elif H_METHYL_CENTER_MIN < center <= H_METHYL_CENTER_MAX and atom_type == 'H':
                                    __v['spectral_region'] = 'H-methyl' if max_ppm < 3 else 'H-aliphatic'
                                elif C_ALL_CENTER_MIN < center <= C_ALL_CENTER_MAX and atom_type == 'C':
                                    __v['spectral_region'] = 'C'  # all
                                elif C_ALIPHATIC_CENTER_MIN < center <= C_ALIPHATIC_CENTER_MAX and atom_type == 'C':
                                    __v['spectral_region'] = 'C-aliphatic'
                                elif C_METHYL_CENTER_MIN < center <= C_METHYL_CENTER_MAX and atom_type == 'C':
                                    __v['spectral_region'] = 'C-methyl'

                            if __v['freq_hint'].size > 0 and d > 2 and __d >= 2\
                               and self.exptlMethod != 'SOLID-STATE NMR' and __v['atom_isotope_number'] == 13:
                                min_ppm = __v['freq_hint'].min()
                                width = max_ppm - min_ppm
                                if center < 100.0 and width < 50.0:
                                    __v['under_sampling_type'] = 'fold'

                            if __v['spectrometer_frequency'] is None and 'obs_freq_hint' in __v and len(__v['obs_freq_hint']) > 0:
                                __v['spectrometer_frequency'] = collections.Counter(__v['obs_freq_hint']).most_common()[0][0]

                            if 'obs_freq_hint' in __v:
                                del __v['obs_freq_hint']

                            if __v['spectrometer_frequency'] is not None and __v['sweep_width_units'] == 'ppm':
                                row = [str(__v['sweep_width']), str(__v['spectrometer_frequency'])]
                                max_eff_digits = getMaxEffDigits(row)

                                __v['sweep_width'] = float(roundString(str(__v['sweep_width'] * __v['spectrometer_frequency']),
                                                                       max_eff_digits))
                                __v['sweep_width_units'] = 'Hz'

                    for __v in _v.values():
                        if __v['axis_code'] == 'HN/H-aromatic':
                            has_a = any(___v['spectral_region'] == 'C-aromatic' for ___v in _v.values())
                            __v['axis_code'] = 'H-aromatic' if has_a else 'H'
                        if __v['spectral_region'] == 'HN/H-aromatic':
                            has_a = any(___v['spectral_region'] == 'C-aromatic' for ___v in _v.values())
                            __v['spectral_region'] = 'H-aromatic' if has_a else 'H'
                            __v['_spectral_region'] = 'H-aromatic' if has_a else 'HN'
                        else:
                            __v['_spectral_region'] = __v['spectral_region']

            for d, v in self.spectral_dim.items():
                for _id, cur_spectral_dim in v.items():

                    if self.debug:
                        print(f'original file name: {self.__originalFileName}{", spectrum name: " + str(spectrum_names[d][_id]) if spectrum_names is not None else ""}')

                    file_name = self.__originalFileName.lower()
                    alt_file_name = ''
                    try:
                        if spectrum_names is not None:
                            alt_file_name = spectrum_names[d][_id].lower()
                    except (KeyError, AttributeError):
                        pass

                    _file_names = (file_name, alt_file_name)

                    cur_spectral_dim_transfer = self.spectral_dim_transfer[d][_id]

                    is_noesy = any('noe' in n for n in _file_names) or any('roe' in n for n in _file_names)
                    no_aromatic = all(_dict['_spectral_region'] != 'C-aromatic' for _dict in cur_spectral_dim.values())

                    if 'axis_order' in cur_spectral_dim[1]:
                        upper_count = lower_count = 0
                        for _dict in cur_spectral_dim.values():
                            if _dict['axis_order'].isupper():
                                upper_count += 1
                            if _dict['axis_order'].islower():
                                lower_count += 1
                        if 0 not in (upper_count, lower_count) and 2 in (upper_count, lower_count):
                            for _dim_id1, _dict1 in cur_spectral_dim.items():
                                for _dim_id2, _dict2 in cur_spectral_dim.items():
                                    if _dim_id1 >= _dim_id2:
                                        continue
                                    if (upper_count == 2 and _dict1['axis_order'].isupper() and _dict2['axis_order'].isupper())\
                                       or (lower_count == 2 and _dict1['axis_order'].islower() and _dict2['axis_order'].islower()):
                                        transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                                    'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                                    'type': 'onebond',
                                                    'indirect': 'no'}
                                        if transfer in cur_spectral_dim_transfer:
                                            continue
                                        cur_spectral_dim_transfer.append(transfer)

                    # onebond: 'Any transfer that connects only directly bonded atoms in this experiment'
                    for _dim_id1, _dict1 in cur_spectral_dim.items():
                        _region1 = _dict1['_spectral_region']
                        if _region1 in ('HN', 'H-aliphatic', 'H-aromatic', 'H-methyl'):
                            cases = 0
                            max_corrcoef = 0.0
                            for _dim_id2, _dict2 in cur_spectral_dim.items():
                                _region2 = _dict2['_spectral_region']
                                if (_region1 == 'HN' and _region2 == 'N')\
                                   or ((_region1 == 'H-aliphatic' or (is_noesy and no_aromatic and _region1 == 'H'))
                                       and (_region2 == 'C-aliphatic' or (is_noesy and _region2 == 'C')))\
                                   or (_region1 == 'H-aromatic' and _region2 == 'C-aromatic')\
                                   or (_region1 == 'H-methyl' and _region2 == 'C-methyl'):
                                    if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                                        if not any(_transfer for _transfer in cur_spectral_dim_transfer
                                                   if _transfer['type'] == 'onebond'
                                                   and (_dim_id1 in [_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']]
                                                        or _dim_id2 in [_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']])):
                                            if _dict1['freq_hint'].size < 2\
                                               or numpy.max(_dict1['freq_hint']) == numpy.min(_dict1['freq_hint'])\
                                               or numpy.max(_dict2['freq_hint']) == numpy.min(_dict2['freq_hint']):
                                                continue
                                            _corrcoef = numpy.corrcoef(_dict1['freq_hint'], _dict2['freq_hint'])[0][1]
                                            if _corrcoef < 0.0 or (_corrcoef < MIN_CORRCOEF_FOR_ONE_BOND_TRANSFER and no_aromatic):
                                                continue
                                            cases += 1
                                            max_corrcoef = max(max_corrcoef, _corrcoef)

                                            if d == 3:
                                                for _dim_id3, _dict3 in cur_spectral_dim.items():
                                                    if _dim_id3 in (_dim_id1, _dim_id2):
                                                        continue
                                                    if _dict3['atom_type'] != _dict1['atom_type']:
                                                        continue
                                                    if not any(_transfer for _transfer in cur_spectral_dim_transfer
                                                       if _transfer['type'] == 'onebond'
                                                       and (_dim_id3 in [_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']]
                                                            or _dim_id2 in [_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']])):
                                                        if _dict3['freq_hint'].size < 2\
                                                           or numpy.max(_dict3['freq_hint']) == numpy.min(_dict3['freq_hint'])\
                                                           or numpy.max(_dict2['freq_hint']) == numpy.min(_dict2['freq_hint']):
                                                            continue
                                                        _corrcoef = numpy.corrcoef(_dict3['freq_hint'], _dict2['freq_hint'])[0][1]
                                                        if _corrcoef < 0.0 or (_corrcoef < MIN_CORRCOEF_FOR_ONE_BOND_TRANSFER and no_aromatic):
                                                            continue
                                                        cases += 1
                                                        max_corrcoef = max(max_corrcoef, _corrcoef)

                            if cases == 1:
                                for _dim_id2, _dict2 in cur_spectral_dim.items():
                                    _region2 = _dict2['_spectral_region']
                                    if (_region1 == 'HN' and _region2 == 'N')\
                                       or ((_region1 == 'H-aliphatic' or (is_noesy and no_aromatic and _region1 == 'H'))
                                       and (_region2 == 'C-aliphatic' or (is_noesy and _region2 == 'C')))\
                                       or (_region1 == 'H-aromatic' and _region2 == 'C-aromatic')\
                                       or (_region1 == 'H-methyl' and _region2 == 'C-methyl'):
                                        if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                                            if not any(_transfer for _transfer in cur_spectral_dim_transfer
                                                       if _transfer['type'] == 'onebond'
                                                       and (_dim_id1 in [_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']]
                                                            or _dim_id2 in [_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']])):
                                                transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                                            'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                                            'type': 'onebond',
                                                            'indirect': 'no'}
                                                if transfer in cur_spectral_dim_transfer:
                                                    continue
                                                cur_spectral_dim_transfer.append(transfer)

                            elif cases > 1:
                                for _dim_id2, _dict2 in cur_spectral_dim.items():
                                    _region2 = _dict2['_spectral_region']
                                    if (_region1 == 'HN' and _region2 == 'N')\
                                       or ((_region1 == 'H-aliphatic' or (is_noesy and no_aromatic and _region1 == 'H'))
                                       and (_region2 == 'C-aliphatic' or (is_noesy and _region2 == 'C')))\
                                       or (_region1 == 'H-aromatic' and _region2 == 'C-aromatic')\
                                       or (_region1 == 'H-methyl' and _region2 == 'C-methyl'):
                                        if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                                            if not any(_transfer for _transfer in cur_spectral_dim_transfer
                                                       if _transfer['type'] == 'onebond'
                                                       and (_dim_id1 in [_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']]
                                                            or _dim_id2 in [_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']])):
                                                if _dict1['freq_hint'].size < 2\
                                                   or numpy.max(_dict1['freq_hint']) == numpy.min(_dict1['freq_hint'])\
                                                   or numpy.max(_dict2['freq_hint']) == numpy.min(_dict2['freq_hint']):
                                                    continue
                                                _corrcoef = numpy.corrcoef(_dict1['freq_hint'], _dict2['freq_hint'])[0][1]
                                                if _corrcoef < 0.0 or (_corrcoef < max_corrcoef and no_aromatic):
                                                    continue
                                                transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                                            'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                                            'type': 'onebond',
                                                            'indirect': 'no'}
                                                if transfer in cur_spectral_dim_transfer:
                                                    continue
                                                cur_spectral_dim_transfer.append(transfer)

                    for _dim_id1, _dict1 in cur_spectral_dim.items():
                        _region1 = _dict1['_spectral_region']
                        if _region1 in ('HN', 'H-aliphatic', 'H-aromatic', 'H-methyl'):
                            for _dim_id2, _dict2 in cur_spectral_dim.items():
                                _region2 = _dict2['_spectral_region']
                                if (_region1 == 'HN' and _region2 == 'N')\
                                   or ((_region1 == 'H-aliphatic' or (is_noesy and no_aromatic and _region1 == 'H'))
                                       and (_region2 == 'C-aliphatic' or (is_noesy and _region2 == 'C')))\
                                   or (_region1 == 'H-aromatic' and _region2 == 'C-aromatic')\
                                   or (_region1 == 'H-methyl' and _region2 == 'C-methyl'):
                                    if _dict1['acquisition'] == 'no' and _dict2['acquisition'] == 'no':
                                        if not any(_transfer for _transfer in cur_spectral_dim_transfer
                                                   if _transfer['type'] == 'onebond'
                                                   and (_dim_id1 in [_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']]
                                                        or _dim_id2 in [_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']])):
                                            if _dict1['freq_hint'].size < 2\
                                               or numpy.max(_dict1['freq_hint']) == numpy.min(_dict1['freq_hint'])\
                                               or numpy.max(_dict2['freq_hint']) == numpy.min(_dict2['freq_hint']):
                                                continue
                                            _corrcoef = numpy.corrcoef(_dict1['freq_hint'], _dict2['freq_hint'])[0][1]
                                            if _corrcoef < 0.0 or (_corrcoef < max_corrcoef and no_aromatic):
                                                continue
                                            transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                                        'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                                        'type': 'onebond',
                                                        'indirect': 'no'}
                                            if transfer in cur_spectral_dim_transfer:
                                                continue
                                            cur_spectral_dim_transfer.append(transfer)

                    # jcoupling: 'Transfer via direct J coupling over one or more bonds'
                    if any('cosy' in n for n in _file_names):
                        if d == 2:
                            for _dim_id1, _dict1 in cur_spectral_dim.items():
                                _iso_num1 = _dict1['atom_isotope_number']
                                if _iso_num1 == 1:
                                    for _dim_id2, _dict2 in cur_spectral_dim.items():
                                        if _dim_id1 == _dim_id2 or _iso_num1 != _dict2['atom_isotope_number']:
                                            continue
                                        if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                                            transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                                        'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                                        'type': 'jcoupling',
                                                        'indirect': 'no'}
                                        if transfer in cur_spectral_dim_transfer:
                                            continue
                                        cur_spectral_dim_transfer.append(transfer)

                        elif d == 3:
                            for _dim_id1, _dict1 in cur_spectral_dim.items():
                                _region1 = _dict1['_spectral_region']
                                if _region1 == 'HN':
                                    for _dim_id2, _dict2 in cur_spectral_dim.items():
                                        if _dim_id1 == _dim_id2 or _dict2['atom_isotope_number'] not in (1, 13):
                                            continue
                                        if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                                            transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                                        'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                                        'type': 'jcoupling',
                                                        'indirect': 'yes'}
                                            if transfer in cur_spectral_dim_transfer:
                                                continue
                                            cur_spectral_dim_transfer.append(transfer)
                            for _dim_id1, _dict1 in cur_spectral_dim.items():
                                _region1 = _dict1['_spectral_region']
                                if _region1 == 'H-aliphatic':
                                    for _dim_id2, _dict2 in cur_spectral_dim.items():
                                        _isotope2 = _dict2['atom_isotope_number']
                                        if _dim_id1 == _dim_id2 or _isotope2 not in (1, 13):
                                            continue
                                        if _isotope2 == 13\
                                           and not any(_transfer for _transfer in cur_spectral_dim_transfer
                                                       if _transfer['type'] == 'onebond'
                                                       and {_dim_id1, _dim_id2} == {_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']}):
                                            if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                                                transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                                            'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                                            'type': 'jcoupling',
                                                            'indirect': 'yes' if _isotope2 == 1 else 'no'}
                                                if transfer in cur_spectral_dim_transfer:
                                                    continue
                                                cur_spectral_dim_transfer.append(transfer)

                        elif d == 4:
                            for _dim_id1, _dict1 in cur_spectral_dim.items():
                                _region1 = _dict1['_spectral_region']
                                if _region1 == 'HN':
                                    for _dim_id2, _dict2 in cur_spectral_dim.items():
                                        if _dim_id1 == _dim_id2 or _dict2['atom_isotope_number'] != 1:
                                            continue
                                        if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                                            transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                                        'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                                        'type': 'jcoupling',
                                                        'indirect': 'yes'}
                                            if transfer in cur_spectral_dim_transfer:
                                                continue
                                            cur_spectral_dim_transfer.append(transfer)
                            for _dim_id1, _dict1 in cur_spectral_dim.items():
                                _region1 = _dict1['_spectral_region']
                                if _region1 == 'H-aliphatic':
                                    for _dim_id2, _dict2 in cur_spectral_dim.items():
                                        if _dim_id1 == _dim_id2 or _dict2['atom_isotope_number'] != 1:
                                            continue
                                        if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                                            transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                                        'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                                        'type': 'jcoupling',
                                                        'indirect': 'no'}
                                            if transfer in cur_spectral_dim_transfer:
                                                continue
                                            cur_spectral_dim_transfer.append(transfer)

                    # jmultibond: 'Transfer via direct J coupling over multiple bonds'

                    # relayed: 'Transfer via multiple successive J coupling steps (TOCSY relay)'
                    if any('tocsy' in n for n in _file_names):
                        if d == 2:
                            for _dim_id1, _dict1 in cur_spectral_dim.items():
                                _iso_num1 = _dict1['atom_isotope_number']
                                if _iso_num1 == 1:
                                    for _dim_id2, _dict2 in cur_spectral_dim.items():
                                        if _dim_id1 == _dim_id2 or _iso_num1 != _dict2['atom_isotope_number']:
                                            continue
                                        if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                                            transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                                        'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                                        'type': 'relayed',
                                                        'indirect': 'no'}
                                        if transfer in cur_spectral_dim_transfer:
                                            continue
                                        cur_spectral_dim_transfer.append(transfer)

                        elif d == 3:
                            for _dim_id1, _dict1 in cur_spectral_dim.items():
                                _region1 = _dict1['_spectral_region']
                                if _region1 == 'HN':
                                    for _dim_id2, _dict2 in cur_spectral_dim.items():
                                        if _dim_id1 == _dim_id2 or _dict2['atom_isotope_number'] not in (1, 13):
                                            continue
                                        if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                                            transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                                        'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                                        'type': 'relayed',
                                                        'indirect': 'yes'}
                                            if transfer in cur_spectral_dim_transfer:
                                                continue
                                            cur_spectral_dim_transfer.append(transfer)
                            for _dim_id1, _dict1 in cur_spectral_dim.items():
                                _region1 = _dict1['_spectral_region']
                                if _region1 == 'H-aliphatic':
                                    for _dim_id2, _dict2 in cur_spectral_dim.items():
                                        _isotope2 = _dict2['atom_isotope_number']
                                        if _dim_id1 == _dim_id2 or _isotope2 not in (1, 13):
                                            continue
                                        if _isotope2 == 13\
                                           and not any(_transfer for _transfer in cur_spectral_dim_transfer
                                                       if _transfer['type'] == 'onebond'
                                                       and {_dim_id1, _dim_id2} == {_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']}):
                                            if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                                                transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                                            'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                                            'type': 'relayed',
                                                            'indirect': 'yes' if _isotope2 == 1 else 'no'}
                                                if transfer in cur_spectral_dim_transfer:
                                                    continue
                                                cur_spectral_dim_transfer.append(transfer)

                        elif d == 4:
                            for _dim_id1, _dict1 in cur_spectral_dim.items():
                                _region1 = _dict1['_spectral_region']
                                if _region1 == 'HN':
                                    for _dim_id2, _dict2 in cur_spectral_dim.items():
                                        if _dim_id1 == _dim_id2 or _dict2['atom_isotope_number'] != 1:
                                            continue
                                        if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                                            transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                                        'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                                        'type': 'relayed',
                                                        'indirect': 'yes'}
                                            if transfer in cur_spectral_dim_transfer:
                                                continue
                                            cur_spectral_dim_transfer.append(transfer)
                            for _dim_id1, _dict1 in cur_spectral_dim.items():
                                _region1 = _dict1['_spectral_region']
                                if _region1 == 'H-aliphatic':
                                    for _dim_id2, _dict2 in cur_spectral_dim.items():
                                        if _dim_id1 == _dim_id2 or _dict2['atom_isotope_number'] != 1:
                                            continue
                                        if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                                            transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                                        'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                                        'type': 'relayed',
                                                        'indirect': 'no'}
                                            if transfer in cur_spectral_dim_transfer:
                                                continue
                                            cur_spectral_dim_transfer.append(transfer)

                    # relayed-alternate: 'Relayed transfer where peaks from an odd resp. even number of transfer steps have opposite sign'

                    # through-space: 'Any transfer that does not go through the covalent bonded skeleton
                    if any('noe' in n for n in _file_names) or any('roe' in n for n in _file_names):
                        for _dim_id1, _dict1 in cur_spectral_dim.items():
                            _region1 = _dict1['_spectral_region']
                            if _region1 in ('H', 'HN', 'H-aliphatic', 'H-aromatic', 'H-methyl'):
                                for _dim_id2, _dict2 in cur_spectral_dim.items():
                                    if _dim_id1 == _dim_id2 or _dict1['atom_isotope_number'] != _dict2['atom_isotope_number']:
                                        continue
                                    if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                                        transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                                    'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                                    'type': 'through-space',
                                                    'indirect': 'yes'}
                                        if transfer in cur_spectral_dim_transfer:
                                            continue
                                        cur_spectral_dim_transfer.append(transfer)
                                        if d == 2 and _region1 == 'H-aliphatic':
                                            _dict1['spectral_region'] = _dict2['spectral_region'] = 'H'  # all
                                            if 'H-aliphatic' in (_dict1['axis_code'], _dict2['axis_code']):
                                                _dict1['axis_code'] = f'H{dim_to_code[_dim_id1]}'
                                                _dict2['axis_code'] = f'H{dim_to_code[_dim_id2]}'
                                        if d == 3:
                                            _transfer = next((_transfer for _transfer in cur_spectral_dim_transfer if _transfer['type'] == 'onebond'), None)
                                            if _transfer is not None:
                                                if _dim_id1 not in (_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']):
                                                    if _region1 == 'H-aliphatic':
                                                        _dict1['spectral_region'] = 'H'  # all
                                                        if _dict1['axis_code'] == 'H-aliphatic':
                                                            _dict1['axis_code'] = 'H'
                                                elif _region1 == 'HN':
                                                    _dict1['spectral_region'] = _dict1['axis_code'] = 'HN'
                                                if _dim_id2 not in (_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']):
                                                    if _region1 == 'H-aliphatic':
                                                        _dict2['spectral_region'] = 'H'  # all
                                                        if _dict2['axis_code'] == 'H-aliphatic':
                                                            _dict2['axis_code'] = 'H'
                                                elif _dict2['_spectral_region'] == 'HN':
                                                    _dict2['spectral_region'] = _dict2['axis_code'] = 'HN'

                    if self.exptlMethod == 'SOLID-STATE NMR':
                        if any('rfdr' in n for n in _file_names) or any('darr' in n for n in _file_names):
                            for _dim_id1, _dict1 in cur_spectral_dim.items():
                                _iso_num1 = _dict1['atom_isotope_number']
                                if _iso_num1 in (1, 13):
                                    for _dim_id2, _dict2 in cur_spectral_dim.items():
                                        if _dim_id1 == _dim_id2 or _iso_num1 != _dict2['atom_isotope_number']:
                                            continue
                                        if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                                            transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                                        'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                                        'type': 'through-space',
                                                        'indirect': 'yes'}
                                            if transfer in cur_spectral_dim_transfer:
                                                continue
                                            cur_spectral_dim_transfer.append(transfer)
                                            if d == 2 and _dict1['spectral_region'] == _dict2['spectral_region']:
                                                nuc = _dict1[1]['spectral_regison'][0]
                                                _dict1['spectral_region'] = _dict2['spectral_region'] = nuc
                                                if _dict1['axis_code'] == _dict2['axis_code']:
                                                    _dict1['axis_code'] = f'{nuc}{dim_to_code[_dim_id1]}'
                                                    _dict2['axis_code'] = f'{nuc}{dim_to_code[_dim_id2]}'

                        elif any('redor' in n for n in _file_names):
                            for _dim_id1, _dict1 in cur_spectral_dim.items():
                                _iso_num1 = _dict1['atom_isotope_number']
                                if _iso_num1 in (13, 15, 19, 31):
                                    for _dim_id2, _dict2 in cur_spectral_dim.items():
                                        _iso_num2 = _dict2['atom_isotope_number']
                                        if _dim_id1 == _dim_id2 or _iso_num2 not in (13, 15, 19, 31) or _iso_num1 == _iso_num2:
                                            continue
                                        if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                                            transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                                        'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                                        'type': 'through-space',
                                                        'indirect': 'yes'}
                                            if transfer in cur_spectral_dim_transfer:
                                                continue
                                            cur_spectral_dim_transfer.append(transfer)

                    for _dim_id1, _dict1 in cur_spectral_dim.items():
                        _region1 = _dict1['_spectral_region']
                        if _region1 in ('H', 'HN', 'H-aliphatic', 'H-aromatic', 'H-methyl') and d > 2:
                            for _dim_id2, _dict2 in cur_spectral_dim.items():
                                if _dim_id1 == _dim_id2 or _dict1['atom_isotope_number'] != _dict2['atom_isotope_number']:
                                    continue
                                if not any(_transfer for _transfer in cur_spectral_dim_transfer
                                           if {_dim_id1, _dim_id2} == {_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']}):
                                    if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                                        transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                                    'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                                    'type': 'through-space' if 'long_range' in cur_spectral_dim[1] else 'through-space?',  # optimistic inferencing?
                                                    'indirect': 'yes'}
                                        if transfer in cur_spectral_dim_transfer:
                                            continue
                                        cur_spectral_dim_transfer.append(transfer)

                    for _dim_id1, _dict1 in cur_spectral_dim.items():
                        _region1 = _dict1['_spectral_region']
                        if _region1 == 'H' and d == 2:  # all
                            for _dim_id2, _dict2 in cur_spectral_dim.items():
                                if _dim_id1 == _dim_id2 or _dict1['_spectral_region'] != _region1:
                                    continue
                                if not any(_transfer for _transfer in cur_spectral_dim_transfer
                                           if {_dim_id1, _dim_id2} == {_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']}):
                                    if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                                        transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                                    'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                                    'type': 'through-space' if 'long_range' in cur_spectral_dim[1] else 'through-space?',  # optimistic inferencing?
                                                    'indirect': 'yes'}
                                        if transfer in cur_spectral_dim_transfer:
                                            continue
                                        cur_spectral_dim_transfer.append(transfer)

                    if self.exptlMethod == 'SOLID-STATE NMR' and d == 2:
                        for _dim_id1, _dict1 in cur_spectral_dim.items():
                            _region1 = _dict1['_spectral_region']
                            if _region1 == 'C':  # all
                                for _dim_id2, _dict2 in cur_spectral_dim.items():
                                    if _dim_id1 == _dim_id2 or _dict1['_spectral_region'] != _region1:
                                        continue
                                    if not any(_transfer for _transfer in cur_spectral_dim_transfer
                                               if {_dim_id1, _dim_id2} == {_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']}):
                                        if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                                            transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                                        'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                                        'type': 'through-space' if 'long_range' in cur_spectral_dim[1] else 'through-space?',  # optimistic inferencing?
                                                        'indirect': 'yes'}
                                            if transfer in cur_spectral_dim_transfer:
                                                continue
                                            cur_spectral_dim_transfer.append(transfer)

                        for _dim_id1, _dict1 in cur_spectral_dim.items():
                            _iso_num1 = _dict1['atom_isotope_number']
                            if _iso_num1 in (13, 15, 19, 31):
                                for _dim_id2, _dict2 in cur_spectral_dim.items():
                                    _iso_num2 = _dict2['atom_isotope_number']
                                    if _dim_id1 == _dim_id2 or _iso_num2 not in (13, 15, 19, 31) or _iso_num1 == _iso_num2:
                                        continue
                                    if 'yes' in (_dict1['acquisition'], _dict2['acquisition']):
                                        transfer = {'spectral_dim_id_1': min([_dim_id1, _dim_id2]),
                                                    'spectral_dim_id_2': max([_dim_id1, _dim_id2]),
                                                    'type': 'through-space' if 'long_range' in cur_spectral_dim[1] else 'through-space?',  # optimistic inferencing?
                                                    'indirect': 'yes'}
                                        if transfer in cur_spectral_dim_transfer:
                                            continue
                                        cur_spectral_dim_transfer.append(transfer)

                    for __v in cur_spectral_dim.values():
                        if 'freq_hint' in __v:
                            del __v['freq_hint']

                    if self.debug:
                        print(f'num_of_dim: {d}, list_id: {_id}')
                        print('spectral_dim')
                        for __d, __v in cur_spectral_dim.items():
                            print(f'{__d} {__v}')
                        print('spectral_dim_transfer')
                        for transfer in cur_spectral_dim_transfer:
                            print(transfer)

                    primary_dim_transfer = ''
                    for transfer in cur_spectral_dim_transfer:
                        if transfer['type'] == 'through-space':
                            primary_dim_transfer = transfer['type']
                            break
                        if transfer['type'] == 'through-space?'\
                                and primary_dim_transfer != 'through-space':
                            primary_dim_transfer = transfer['type']
                        elif transfer['type'].startswith('relayed')\
                                and primary_dim_transfer not in ('through-space', 'through-space?'):
                            primary_dim_transfer = transfer['type']
                        elif transfer['type'] == 'jmultibond'\
                                and primary_dim_transfer not in ('through-space', 'through-space?', 'relayed', 'relayed-alternate'):
                            primary_dim_transfer = transfer['type']
                        elif transfer['type'] == 'jcoupling'\
                                and primary_dim_transfer not in ('through-space', 'through-space?', 'relayed', 'relayed-alternate', 'jmultibond'):
                            primary_dim_transfer = transfer['type']
                        elif transfer['type'] == 'onebond'\
                                and primary_dim_transfer == '':
                            primary_dim_transfer = transfer['type']

                    exp_class = '.'

                    if primary_dim_transfer != 'onebond':
                        onebonds, onebond_codes = [], []
                        for transfer in cur_spectral_dim_transfer:
                            if transfer['type'] == 'onebond':
                                dim_id_1 = transfer['spectral_dim_id_1']
                                dim_id_2 = transfer['spectral_dim_id_2']
                                atom_type_1 = next(v['atom_type'] for k, v in cur_spectral_dim.items() if k == dim_id_1)
                                atom_type_2 = next(v['atom_type'] for k, v in cur_spectral_dim.items() if k == dim_id_2)
                                for _transfer in cur_spectral_dim_transfer:
                                    if _transfer['type'] != 'onebond':
                                        if dim_id_1 in (_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']):
                                            onebonds.append((dim_id_1, dim_id_2))
                                            onebond_codes.append(f'{atom_type_1}[{atom_type_2}]')
                                        if dim_id_2 in (_transfer['spectral_dim_id_1'], _transfer['spectral_dim_id_2']):
                                            onebonds.append((dim_id_2, dim_id_1))
                                            onebond_codes.append(f'{atom_type_2}[{atom_type_1}]')

                        for transfer in cur_spectral_dim_transfer:
                            if transfer['type'] == primary_dim_transfer:
                                dim_id_1 = transfer['spectral_dim_id_1']
                                dim_id_2 = transfer['spectral_dim_id_2']
                                onebond_1 = next((onebond for onebond in onebonds if dim_id_1 in onebond), None)
                                v_1 = next(v for k, v in cur_spectral_dim.items() if k == dim_id_1)
                                onebond_2 = next((onebond for onebond in onebonds if dim_id_2 in onebond), None)
                                v_2 = next(v for k, v in cur_spectral_dim.items() if k == dim_id_2)
                                if v_1['acquisition'] != v_2['acquisition'] and v_1['acquisition'] == 'no':
                                    onebond_1, onebond_2 = onebond_2, onebond_1
                                    v_1, v_2 = v_2, v_1
                                exp_class = f'{onebond_codes[onebonds.index(onebond_1)] if onebond_1 is not None else v_1["atom_type"]}_'\
                                    f'{onebond_codes[onebonds.index(onebond_2)] if onebond_2 is not None else v_2["atom_type"]}.{primary_dim_transfer}'
                                break

                    else:
                        for transfer in cur_spectral_dim_transfer:
                            if transfer['type'] == primary_dim_transfer:
                                dim_id_1 = transfer['spectral_dim_id_1']
                                dim_id_2 = transfer['spectral_dim_id_2']
                                v_1 = next(v for k, v in cur_spectral_dim.items() if k == dim_id_1)
                                v_2 = next(v for k, v in cur_spectral_dim.items() if k == dim_id_2)
                                if v_1['acquisition'] != v_2['acquisition'] and v_1['acquisition'] == 'no':
                                    v_1, v_2 = v_2, v_1
                                exp_class = f'{v_1["atom_type"]}_{v_2["atom_type"]}.{primary_dim_transfer}'
                                break

                    if self.debug:
                        print(f'experiment class: {exp_class}')

                    if self.software_name == 'PIPP' and any(transfer['type'] == 'onebond' for transfer in cur_spectral_dim_transfer):
                        if d == 3:
                            transfer = next(transfer for transfer in cur_spectral_dim_transfer if transfer['type'] == 'onebond')
                            pro_axis = hvy_axis = -1
                            for _dim_id, _dict in cur_spectral_dim.items():
                                if _dim_id in (transfer['spectral_dim_id_1'], transfer['spectral_dim_id_2']):
                                    if _dict['atom_isotope_number'] == 1:
                                        pro_axis = _dim_id
                                    else:
                                        hvy_axis = _dim_id
                            if pro_axis != -1 and hvy_axis != -1:
                                self.reasonsForReParsing['onebond_resolved'] = {0: 5 - hvy_axis - pro_axis, 1: hvy_axis - 1, 2: pro_axis - 1}
                        elif d == 4 and len([transfer for transfer in cur_spectral_dim_transfer if transfer['type'] == 'onebond']) == 2:
                            self.reasonsForReParsing['onebond_resolved'] = {}
                            for offset, transfer in enumerate([transfer for transfer in cur_spectral_dim_transfer if transfer['type'] == 'onebond']):
                                pro_axis = hvy_axis = -1
                                for _dim_id, _dict in cur_spectral_dim.items():
                                    if _dim_id in (transfer['spectral_dim_id_1'], transfer['spectral_dim_id_2']):
                                        if _dict['atom_isotope_number'] == 1:
                                            pro_axis = _dim_id
                                        else:
                                            hvy_axis = _dim_id
                                if pro_axis != -1 and hvy_axis != -1:
                                    self.reasonsForReParsing['onebond_resolved'][offset * 2] = hvy_axis - 1
                                    self.reasonsForReParsing['onebond_resolved'][offset * 2 + 1] = pro_axis - 1

                    if self.createSfDict__:
                        self.cur_subtype = f'peak{d}d'
                        self.cur_list_id = _id

                        sf = self.getSf()

                        if sf['peak_row_format']:
                            sf['saveframe'].add_loop(sf['loop'])
                            del sf['alt_loops']
                        else:
                            for alt_loop in sf['alt_loops']:
                                sf['saveframe'].add_loop(alt_loop)
                            del sf['loop']

                        list_id = sf['list_id']
                        sf['aux_loops'] = getAuxLoops('spectral_peak')

                        aux_lp = next((aux_lp for aux_lp in sf['aux_loops'] if aux_lp.category == '_Spectral_dim'), None)

                        if aux_lp is None:
                            continue

                        for _dim_id, _dict in cur_spectral_dim.items():
                            aux_lp.add_data(getSpectralDimRow(_dim_id, list_id, self.entryId, _dict))

                        sf['saveframe'].add_loop(aux_lp)

                        aux_lp = next((aux_lp for aux_lp in sf['aux_loops'] if aux_lp.category == '_Spectral_dim_transfer'), None)

                        if aux_lp is None:
                            continue

                        for _dict in cur_spectral_dim_transfer:
                            aux_lp.add_data(getSpectralDimTransferRow(list_id, self.entryId, _dict))

                        sf['saveframe'].add_loop(aux_lp)

                        if exp_class not in emptyValue:
                            tags = [t[0] for t in sf['saveframe'].tags]
                            if 'Experiment_class' in tags:
                                sf['saveframe'].tags[tags.index('Experiment_class')][1] = exp_class

                        if spectrum_names is not None:
                            try:
                                alt_file_name = spectrum_names[d][_id]
                                if alt_file_name not in emptyValue:
                                    exp_type = get_first_sf_tag(sf['saveframe'], 'Experiment_type')
                                    if exp_type in emptyValue:
                                        set_sf_tag(sf['saveframe'], 'Experiment_type', alt_file_name)
                            except (KeyError, AttributeError):
                                pass

                        has_assign = False

                        if sf['peak_row_format']:
                            lp = sf['loop']
                            for row in lp.get_tag('Auth_asym_ID_1'):
                                if row not in emptyValue:
                                    has_assign = True
                                    break

                        else:
                            lp = next((aux_lp for aux_lp in sf['aux_loops'] if aux_lp.category == '_Assigned_peak_chem_shift'), None)
                            if lp is None or len(lp) == 0:
                                continue
                            for row in lp.get_tag('Auth_entity_ID'):
                                if row not in emptyValue:
                                    has_assign = True
                                    break

                        if not has_assign:
                            continue

                        if any(transfer['type'] == 'onebond' for transfer in cur_spectral_dim_transfer):
                            onebond_dim_transfers = [[transfer['spectral_dim_id_1'], transfer['spectral_dim_id_2']]
                                                     for transfer in cur_spectral_dim_transfer
                                                     if transfer['type'] == 'onebond']

                            self.__remediatePeakAssignmentForOneBondTransfer(d, onebond_dim_transfers, sf['peak_row_format'], lp)

                        if any(transfer['type'] == 'jcoupling' for transfer in cur_spectral_dim_transfer):
                            jcoupling_dim_transfers = [[transfer['spectral_dim_id_1'], transfer['spectral_dim_id_2']]
                                                       for transfer in cur_spectral_dim_transfer
                                                       if transfer['type'] == 'jcoupling']

                            self.__remediatePeakAssignmentForJcouplingTransfer(d, jcoupling_dim_transfers, sf['peak_row_format'], lp)

                        if any(transfer['type'] == 'relayed' for transfer in cur_spectral_dim_transfer)\
                           and self.__csLoops is not None and len(self.__csLoops) > 0:
                            relayed_dim_transfers = [[transfer['spectral_dim_id_1'], transfer['spectral_dim_id_2']]
                                                     for transfer in cur_spectral_dim_transfer
                                                     if transfer['type'] == 'relayed']

                            self.__remediatePeakAssignmentForRelayedTransfer(d, relayed_dim_transfers, sf['peak_row_format'], lp)

    def __remediatePeakAssignmentForOneBondTransfer(self, num_of_dim: int, onebond_transfers: List[List[int]], use_peak_row_format: bool, loop: pynmrstar.Loop):

        details_col = loop.tags.index('Details')

        for dim_id_1, dim_id_2 in onebond_transfers:

            if use_peak_row_format:

                tags = [f'Entity_assembly_ID_{dim_id_1}', f'Comp_index_ID_{dim_id_1}', f'Comp_ID_{dim_id_1}', f'Atom_ID_{dim_id_1}', f'Position_{dim_id_1}',
                        f'Entity_assembly_ID_{dim_id_2}', f'Comp_index_ID_{dim_id_2}', f'Comp_ID_{dim_id_2}', f'Atom_ID_{dim_id_2}', f'Position_{dim_id_2}']

                dat = loop.get_tag(tags)

                for idx, row in enumerate(dat):

                    if any(row[col] in emptyValue for col in range(10)):
                        continue

                    chain_id, seq_id, comp_id, atom_id, chain_id2, seq_id2, comp_id2, atom_id2 =\
                        row[0], row[1], row[2], row[3], row[5], row[6], row[7], row[8]

                    if isinstance(chain_id, int):
                        chain_id = str(chain_id)

                    if isinstance(chain_id2, int):
                        chain_id2 = str(chain_id2)

                    if isinstance(seq_id, str):
                        seq_id = int(seq_id)

                    if isinstance(seq_id2, str):
                        seq_id2 = int(seq_id2)

                    if chain_id == chain_id2 and seq_id == seq_id2 and comp_id == comp_id2 and atom_id != atom_id2\
                       and self.ccU.updateChemCompDict(comp_id):
                        _atom_ids = self.nefT.get_valid_star_atom(comp_id, atom_id, leave_unmatched=False)[0]
                        _atom_ids2 = self.nefT.get_valid_star_atom(comp_id, atom_id2, leave_unmatched=False)[0]
                        if any(b for b in self.ccU.lastBonds
                           if ((b[self.ccU.ccbAtomId1] in _atom_ids and b[self.ccU.ccbAtomId2] in _atom_ids2)
                               or (b[self.ccU.ccbAtomId1] in _atom_ids2 and b[self.ccU.ccbAtomId2] in _atom_ids))):
                            continue

                        _atom_id, _atom_id2 = _atom_ids[0], _atom_ids2[0]

                        _atom_id2_ = self.ccU.getBondedAtoms(comp_id, _atom_id, exclProton=_atom_id[0] in protonBeginCode, onlyProton=_atom_id[0] not in protonBeginCode)
                        _atom_id_ = self.ccU.getBondedAtoms(comp_id, _atom_id2, exclProton=_atom_id2[0] in protonBeginCode, onlyProton=_atom_id2[0] not in protonBeginCode)

                        len_atom_id_ = len(_atom_id_)
                        len_atom_id2_ = len(_atom_id2_)

                        # pylint: disable=cell-var-from-loop
                        def swap_atom_1():
                            if loop.data[idx][details_col] in emptyValue:
                                loop.data[idx][details_col] = f'{atom_id} -> {_atom_id_[0]}'
                            loop.data[idx][loop.tags.index(f'Atom_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Auth_atom_ID_{dim_id_1}')] = _atom_id_[0]

                        # pylint: disable=cell-var-from-loop
                        def swap_atom_2():
                            if loop.data[idx][details_col] in emptyValue:
                                loop.data[idx][details_col] = f'{atom_id2} -> {_atom_id2_[0]}'
                            loop.data[idx][loop.tags.index(f'Atom_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Auth_atom_ID_{dim_id_2}')] = _atom_id2_[0]

                        if len_atom_id_ > 0 and len_atom_id2_ > 0 and atom_id[0] != _atom_id_[0][0] and atom_id2[0] == _atom_id2_[0][0]:
                            swap_atom_2()
                        elif len_atom_id_ > 0 and len_atom_id2_ > 0 and atom_id[0] == _atom_id_[0][0] and atom_id2[0] != _atom_id2_[0][0]:
                            swap_atom_1()
                        elif 0 < len_atom_id2_ < len_atom_id_:
                            swap_atom_2()
                        elif 0 < len_atom_id_ < len_atom_id2_:
                            swap_atom_1()
                        elif len(atom_id2) < len(atom_id):
                            swap_atom_2()
                        elif len(atom_id) < len(atom_id2):
                            swap_atom_1()
                        elif _atom_id2[0] in protonBeginCode and len_atom_id2_ > 0:
                            swap_atom_2()
                        elif _atom_id[0] in protonBeginCode and len_atom_id_ > 0:
                            swap_atom_1()
                        else:
                            self.f.append(f"[Inconsistent assigned peak] [Check row of Index_ID {loop.data[idx][loop.tags.index('Index_ID')]}] "
                                          f"Inconsistent assignments of spectral peak with onebond coherence transfer type, ({chain_id}:{seq_id}:{comp_id}:{atom_id}) vs "
                                          f"({chain_id}:{seq_id}:{comp_id}:{atom_id2}) have been cleared.")

                            if loop.data[idx][details_col] in emptyValue:
                                loop.data[idx][details_col] = f'{atom_id}, {atom_id2} -> cleared'

                            loop.data[idx][loop.tags.index(f'Atom_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Auth_atom_ID_{dim_id_1}')] =\
                                loop.data[idx][loop.tags.index(f'Atom_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Auth_atom_ID_{dim_id_2}')] = None

                    elif chain_id == chain_id2 and seq_id != seq_id2:
                        position, position2 = row[4], row[9]

                        if isinstance(position, str):
                            position = float(position)

                        if isinstance(position2, str):
                            position2 = float(position2)

                        shift, weight = self.__getCsValue(chain_id, seq_id, comp_id, atom_id)
                        shift2, weight2 = self.__getCsValue(chain_id, seq_id2, comp_id2, atom_id2)

                        shift_, _ = self.__getCsValue(chain_id, seq_id2, comp_id2, atom_id)
                        shift2_, _ = self.__getCsValue(chain_id, seq_id, comp_id, atom_id2)

                        # pylint: disable=cell-var-from-loop
                        def swap_seq_id_1():
                            if loop.data[idx][details_col] in emptyValue:
                                loop.data[idx][details_col] = f'{seq_id}:{comp_id} -> {seq_id2}:{comp_id2}'
                            loop.data[idx][loop.tags.index(f'Comp_index_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Comp_index_ID_{dim_id_2}')]
                            loop.data[idx][loop.tags.index(f'Comp_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Comp_ID_{dim_id_2}')]
                            loop.data[idx][loop.tags.index(f'Auth_seq_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Auth_seq_ID_{dim_id_2}')]
                            loop.data[idx][loop.tags.index(f'Auth_comp_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Auth_comp_ID_{dim_id_2}')]

                        # pylint: disable=cell-var-from-loop
                        def swap_seq_id_2():
                            if loop.data[idx][details_col] in emptyValue:
                                loop.data[idx][details_col] = f'{seq_id2}:{comp_id2} -> {seq_id}:{comp_id}'
                            loop.data[idx][loop.tags.index(f'Comp_index_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Comp_index_ID_{dim_id_1}')]
                            loop.data[idx][loop.tags.index(f'Comp_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Comp_ID_{dim_id_1}')]
                            loop.data[idx][loop.tags.index(f'Auth_seq_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Auth_seq_ID_{dim_id_1}')]
                            loop.data[idx][loop.tags.index(f'Auth_comp_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Auth_comp_ID_{dim_id_1}')]

                        if None in (shift, shift2):

                            if shift is None and shift2 is None:
                                continue

                            if shift is None and shift_ is not None:
                                swap_seq_id_1()

                            elif shift2 is None and shift2_ is not None:
                                swap_seq_id_2()

                            continue

                        diff = ((position - shift) * weight) ** 2 + ((position2 - shift2) * weight2) ** 2
                        diff *= 2.0

                        diff_ = diff2_ = None
                        if shift_ is not None:
                            diff_ = ((position - shift_) * weight) ** 2 + ((position2 - shift2) * weight2) ** 2
                        if shift2_ is not None:
                            diff2_ = ((position - shift) * weight) ** 2 + ((position2 - shift2_) * weight2) ** 2

                        if diff_ is not None and diff2_ is not None:
                            if diff_ < diff and diff2_ < diff:
                                if diff_ < diff2_:
                                    swap_seq_id_1()
                                elif diff_ > diff2_:
                                    swap_seq_id_2()
                            elif diff_ < diff:
                                swap_seq_id_1()
                            elif diff2_ < diff:
                                swap_seq_id_2()

                        elif diff_ is not None and diff_ < diff:
                            swap_seq_id_1()

                        elif diff2_ is not None and diff2_ < diff:
                            swap_seq_id_2()

                    elif chain_id != chain_id2:
                        position, position2 = row[4], row[9]

                        if isinstance(position, str):
                            position = float(position)

                        if isinstance(position2, str):
                            position2 = float(position2)

                        shift, weight = self.__getCsValue(chain_id, seq_id, comp_id, atom_id)
                        shift2, weight2 = self.__getCsValue(chain_id2, seq_id2, comp_id2, atom_id2)

                        shift_, _ = self.__getCsValue(chain_id2, seq_id2, comp_id2, atom_id)
                        shift2_, _ = self.__getCsValue(chain_id, seq_id, comp_id, atom_id2)

                        # pylint: disable=cell-var-from-loop
                        def swap_chain_seq_id_1():
                            if loop.data[idx][details_col] in emptyValue:
                                loop.data[idx][details_col] = f'{chain_id}:{seq_id}:{comp_id} -> {chain_id2}:{seq_id2}:{comp_id2}'
                            loop.data[idx][loop.tags.index(f'Entity_assembly_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Entity_assembly_ID_{dim_id_2}')]
                            loop.data[idx][loop.tags.index(f'Entity_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Entity_ID_{dim_id_2}')]
                            loop.data[idx][loop.tags.index(f'Comp_index_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Comp_index_ID_{dim_id_2}')]
                            loop.data[idx][loop.tags.index(f'Comp_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Comp_ID_{dim_id_2}')]
                            loop.data[idx][loop.tags.index(f'Auth_asym_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Auth_asym_ID_{dim_id_2}')]
                            loop.data[idx][loop.tags.index(f'Auth_seq_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Auth_seq_ID_{dim_id_2}')]
                            loop.data[idx][loop.tags.index(f'Auth_comp_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Auth_comp_ID_{dim_id_2}')]

                        # pylint: disable=cell-var-from-loop
                        def swap_chain_seq_id_2():
                            if loop.data[idx][details_col] in emptyValue:
                                loop.data[idx][details_col] = f'{chain_id2}:{seq_id2}:{comp_id2} -> {chain_id}:{seq_id}:{comp_id}'
                            loop.data[idx][loop.tags.index(f'Entity_assembly_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Entity_assembly_ID_{dim_id_1}')]
                            loop.data[idx][loop.tags.index(f'Entity_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Entity_ID_{dim_id_1}')]
                            loop.data[idx][loop.tags.index(f'Comp_index_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Comp_index_ID_{dim_id_1}')]
                            loop.data[idx][loop.tags.index(f'Comp_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Comp_ID_{dim_id_1}')]
                            loop.data[idx][loop.tags.index(f'Auth_asym_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Auth_asym_ID_{dim_id_1}')]
                            loop.data[idx][loop.tags.index(f'Auth_seq_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Auth_seq_ID_{dim_id_1}')]
                            loop.data[idx][loop.tags.index(f'Auth_comp_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Auth_comp_ID_{dim_id_1}')]

                        if None in (shift, shift2):

                            if shift is None and shift2 is None:
                                continue

                            if shift is None and shift_ is not None:
                                swap_chain_seq_id_1()

                            elif shift2 is None and shift2_ is not None:
                                swap_chain_seq_id_2()

                            continue

                        diff = ((position - shift) * weight) ** 2 + ((position2 - shift2) * weight2) ** 2
                        diff *= 2.0

                        diff_ = diff2_ = None
                        if shift_ is not None:
                            diff_ = ((position - shift_) * weight) ** 2 + ((position2 - shift2) * weight2) ** 2
                        if shift2_ is not None:
                            diff2_ = ((position - shift) * weight) ** 2 + ((position2 - shift2_) * weight2) ** 2

                        if diff_ is not None and diff2_ is not None:
                            if diff_ < diff and diff2_ < diff:
                                if diff_ < diff2_:
                                    swap_chain_seq_id_1()
                                elif diff_ > diff2_:
                                    swap_chain_seq_id_2()
                            elif diff_ < diff:
                                swap_chain_seq_id_1()
                            elif diff2_ < diff:
                                swap_chain_seq_id_2()

                        elif diff_ is not None and diff_ < diff:
                            swap_chain_seq_id_1()

                        elif diff2_ is not None and diff2_ < diff:
                            swap_chain_seq_id_2()

            else:

                tags = ['Peak_ID', 'Spectral_dim_ID', 'Entity_assembly_ID', 'Comp_index_ID', 'Comp_ID', 'Atom_ID', 'Val']

                chain_id_col = loop.tags.index('Entity_assembly_ID')
                entity_id_col = loop.tags.index('Entity_ID')
                seq_id_col = loop.tags.index('Comp_index_ID')
                comp_id_col = loop.tags.index('Comp_ID')
                atom_id_col = loop.tags.index('Atom_ID')
                auth_chain_id_col = loop.tags.index('Auth_asym_ID')
                auth_seq_id_col = loop.tags.index('Auth_seq_ID')
                auth_comp_id_col = loop.tags.index('Auth_comp_ID')
                auth_atom_id_col = loop.tags.index('Auth_atom_ID')

                dat = loop.get_tag(tags)

                peak_id = None

                for idx, row in enumerate(dat):
                    dim_id = row[1]

                    if any(row[col] in emptyValue for col in range(7)):
                        continue

                    if dim_id == 1:
                        peak_id = row[0]
                        chain_ids, seq_ids, comp_ids, atom_ids, positions = [], [], [], [], []
                    else:
                        if peak_id != row[0]:
                            continue

                    chain_ids.append(row[2] if isinstance(row[2], str) else str(row[2]))
                    seq_ids.append(int(row[3]) if isinstance(row[3], str) else row[3])
                    comp_ids.append(row[4])
                    atom_ids.append(row[5])
                    positions.append(float(row[6]) if isinstance(row[6], str) else row[6])

                    if dim_id < num_of_dim:
                        continue

                    if len(atom_ids) < num_of_dim:
                        continue

                    _dim_id_1 = dim_id_1 - 1
                    _dim_id_2 = dim_id_2 - 1

                    chain_id, seq_id, comp_id, atom_id, chain_id2, seq_id2, comp_id2, atom_id2 =\
                        chain_ids[_dim_id_1], seq_ids[_dim_id_1], comp_ids[_dim_id_1], atom_ids[_dim_id_1], \
                        chain_ids[_dim_id_2], seq_ids[_dim_id_2], comp_ids[_dim_id_2], atom_ids[_dim_id_2]

                    if chain_id == chain_id2 and seq_id == seq_id2 and comp_id == comp_id2 and atom_id != atom_id2\
                       and self.ccU.updateChemCompDict(comp_id):
                        _atom_ids = self.nefT.get_valid_star_atom(comp_id, atom_id, leave_unmatched=False)[0]
                        _atom_ids2 = self.nefT.get_valid_star_atom(comp_id, atom_id2, leave_unmatched=False)[0]
                        if any(b for b in self.ccU.lastBonds
                           if ((b[self.ccU.ccbAtomId1] in _atom_ids and b[self.ccU.ccbAtomId2] in _atom_ids2)
                               or (b[self.ccU.ccbAtomId1] in _atom_ids2 and b[self.ccU.ccbAtomId2] in _atom_ids))):
                            continue

                        _atom_id, _atom_id2 = _atom_ids[0], _atom_ids2[0]

                        _atom_id2_ = self.ccU.getBondedAtoms(comp_id, _atom_id, exclProton=_atom_id[0] in protonBeginCode, onlyProton=_atom_id[0] not in protonBeginCode)
                        _atom_id_ = self.ccU.getBondedAtoms(comp_id, _atom_id2, exclProton=_atom_id2[0] in protonBeginCode, onlyProton=_atom_id2[0] not in protonBeginCode)

                        len_atom_id_ = len(_atom_id_)
                        len_atom_id2_ = len(_atom_id2_)

                        # pylint: disable=cell-var-from-loop
                        def alt_swap_atom_1():
                            if loop.data[idx - num_of_dim + dim_id_1][details_col] in emptyValue:
                                loop.data[idx - num_of_dim + dim_id_1][details_col] = f'{atom_id} -> {_atom_id_[0]}'
                            loop.data[idx - num_of_dim + dim_id_1][atom_id_col] = loop.data[idx - num_of_dim + dim_id_1][auth_atom_id_col] = _atom_id_[0]

                        # pylint: disable=cell-var-from-loop
                        def alt_swap_atom_2():
                            if loop.data[idx - num_of_dim + dim_id_2][details_col] in emptyValue:
                                loop.data[idx - num_of_dim + dim_id_2][details_col] = f'{atom_id2} -> {_atom_id2_[0]}'
                            loop.data[idx - num_of_dim + dim_id_2][atom_id_col] = loop.data[idx - num_of_dim + dim_id_2][auth_atom_id_col] = _atom_id2_[0]

                        if len_atom_id_ > 0 and len_atom_id2_ > 0 and atom_id[0] != _atom_id_[0][0] and atom_id2[0] == _atom_id2_[0][0]:
                            alt_swap_atom_2()
                        elif len_atom_id_ > 0 and len_atom_id2_ > 0 and atom_id[0] == _atom_id_[0][0] and atom_id2[0] != _atom_id2_[0][0]:
                            alt_swap_atom_1()
                        elif 0 < len_atom_id2_ < len_atom_id_:
                            alt_swap_atom_2()
                        elif 0 < len_atom_id_ < len_atom_id2_:
                            alt_swap_atom_1()
                        elif len(atom_id2) < len(atom_id):
                            alt_swap_atom_2()
                        elif len(atom_id) < len(atom_id2):
                            alt_swap_atom_1()
                        elif _atom_id2[0] in protonBeginCode and len_atom_id2_ > 0:
                            alt_swap_atom_2()
                        elif _atom_id[0] in protonBeginCode and len_atom_id_ > 0:
                            alt_swap_atom_1()
                        else:
                            self.f.append(f"[Inconsistent assigned peak] [Check row of Peak_ID {loop.data[idx][loop.tags.index('Peak_ID')]}] "
                                          f"Inconsistent assignments of spectral peak with onebond coherence transfer type, ({chain_id}:{seq_id}:{comp_id}:{atom_id}) vs "
                                          f"({chain_id}:{seq_id}:{comp_id}:{atom_id2}) have been cleared.")

                            if loop.data[idx - num_of_dim + dim_id_1][details_col] in emptyValue:
                                loop.data[idx - num_of_dim + dim_id_1][details_col] = f'{atom_id} -> cleared'
                            if loop.data[idx - num_of_dim + dim_id_2][details_col] in emptyValue:
                                loop.data[idx - num_of_dim + dim_id_2][details_col] = f'{atom_id2} -> cleared'

                            loop.data[idx - num_of_dim + dim_id_1][atom_id_col] = loop.data[idx - num_of_dim + dim_id_1][auth_atom_id_col] =\
                                loop.data[idx - num_of_dim + dim_id_2][atom_id_col] = loop.data[idx - num_of_dim + dim_id_2][auth_atom_id_col] = None

                    elif chain_id == chain_id2 and seq_id != seq_id2:
                        position, position2 = positions[_dim_id_1], positions[_dim_id_2]

                        shift, weight = self.__getCsValue(chain_id, seq_id, comp_id, atom_id)
                        shift2, weight2 = self.__getCsValue(chain_id, seq_id2, comp_id2, atom_id2)

                        shift_, _ = self.__getCsValue(chain_id, seq_id2, comp_id2, atom_id)
                        shift2_, _ = self.__getCsValue(chain_id, seq_id, comp_id, atom_id2)

                        # pylint: disable=cell-var-from-loop
                        def alt_swap_seq_id_1():
                            if loop.data[idx][details_col] in emptyValue:
                                loop.data[idx - num_of_dim + dim_id_1][details_col] = f'{seq_id}:{comp_id} -> {seq_id2}:{comp_id2}'
                            loop.data[idx - num_of_dim + dim_id_1][seq_id_col] = loop.data[idx - num_of_dim + dim_id_2][seq_id_col]
                            loop.data[idx - num_of_dim + dim_id_1][comp_id_col] = loop.data[idx - num_of_dim + dim_id_2][comp_id_col]
                            loop.data[idx - num_of_dim + dim_id_1][auth_seq_id_col] = loop.data[idx - num_of_dim + dim_id_2][auth_seq_id_col]
                            loop.data[idx - num_of_dim + dim_id_1][auth_comp_id_col] = loop.data[idx - num_of_dim + dim_id_2][auth_comp_id_col]

                        # pylint: disable=cell-var-from-loop
                        def alt_swap_seq_id_2():
                            if loop.data[idx - num_of_dim + dim_id_2][details_col] in emptyValue:
                                loop.data[idx - num_of_dim + dim_id_2][details_col] = f'{seq_id2}:{comp_id2} -> {seq_id}:{comp_id}'
                            loop.data[idx - num_of_dim + dim_id_2][seq_id_col] = loop.data[idx - num_of_dim + dim_id_1][seq_id_col]
                            loop.data[idx - num_of_dim + dim_id_2][comp_id_col] = loop.data[idx - num_of_dim + dim_id_1][comp_id_col]
                            loop.data[idx - num_of_dim + dim_id_2][auth_seq_id_col] = loop.data[idx - num_of_dim + dim_id_1][auth_seq_id_col]
                            loop.data[idx - num_of_dim + dim_id_2][auth_comp_id_col] = loop.data[idx - num_of_dim + dim_id_1][auth_comp_id_col]

                        if None in (shift, shift2):

                            if shift is None and shift2 is None:
                                continue

                            if shift is None and shift_ is not None:
                                alt_swap_seq_id_1()

                            elif shift2 is None and shift2_ is not None:
                                alt_swap_seq_id_2()

                            continue

                        diff = ((position - shift) * weight) ** 2 + ((position2 - shift2) * weight2) ** 2
                        diff *= 2.0

                        diff_ = diff2_ = None
                        if shift_ is not None:
                            diff_ = ((position - shift_) * weight) ** 2 + ((position2 - shift2) * weight2) ** 2
                        if shift2_ is not None:
                            diff2_ = ((position - shift) * weight) ** 2 + ((position2 - shift2_) * weight2) ** 2

                        if diff_ is not None and diff2_ is not None:
                            if diff_ < diff and diff2_ < diff:
                                if diff_ < diff2_:
                                    alt_swap_seq_id_1()
                                elif diff_ > diff2_:
                                    alt_swap_seq_id_2()
                            elif diff_ < diff:
                                alt_swap_seq_id_1()
                            elif diff2_ < diff:
                                alt_swap_seq_id_2()

                        elif diff_ is not None and diff_ < diff:
                            alt_swap_seq_id_1()

                        elif diff2_ is not None and diff2_ < diff:
                            alt_swap_seq_id_2()

                    elif chain_id != chain_id2:
                        position, position2 = positions[_dim_id_1], positions[_dim_id_2]

                        shift, weight = self.__getCsValue(chain_id, seq_id, comp_id, atom_id)
                        shift2, weight2 = self.__getCsValue(chain_id2, seq_id2, comp_id2, atom_id2)

                        shift_, _ = self.__getCsValue(chain_id2, seq_id2, comp_id2, atom_id)
                        shift2_, _ = self.__getCsValue(chain_id, seq_id, comp_id, atom_id2)

                        # pylint: disable=cell-var-from-loop
                        def alt_swap_chain_seq_id_1():
                            if loop.data[idx][details_col] in emptyValue:
                                loop.data[idx - num_of_dim + dim_id_1][details_col] = f'{chain_id}:{seq_id}:{comp_id} -> {chain_id2}:{seq_id2}:{comp_id2}'
                            loop.data[idx - num_of_dim + dim_id_1][chain_id_col] = loop.data[idx - num_of_dim + dim_id_2][chain_id_col]
                            loop.data[idx - num_of_dim + dim_id_1][entity_id_col] = loop.data[idx - num_of_dim + dim_id_2][entity_id_col]
                            loop.data[idx - num_of_dim + dim_id_1][seq_id_col] = loop.data[idx - num_of_dim + dim_id_2][seq_id_col]
                            loop.data[idx - num_of_dim + dim_id_1][comp_id_col] = loop.data[idx - num_of_dim + dim_id_2][comp_id_col]
                            loop.data[idx - num_of_dim + dim_id_1][auth_chain_id_col] = loop.data[idx - num_of_dim + dim_id_2][auth_chain_id_col]
                            loop.data[idx - num_of_dim + dim_id_1][auth_seq_id_col] = loop.data[idx - num_of_dim + dim_id_2][auth_seq_id_col]
                            loop.data[idx - num_of_dim + dim_id_1][auth_comp_id_col] = loop.data[idx - num_of_dim + dim_id_2][auth_comp_id_col]

                        # pylint: disable=cell-var-from-loop
                        def alt_swap_chain_seq_id_2():
                            if loop.data[idx - num_of_dim + dim_id_2][details_col] in emptyValue:
                                loop.data[idx - num_of_dim + dim_id_2][details_col] = f'{chain_id2}:{seq_id2}:{comp_id2} -> {chain_id}:{seq_id}:{comp_id}'
                            loop.data[idx - num_of_dim + dim_id_2][chain_id_col] = loop.data[idx - num_of_dim + dim_id_1][chain_id_col]
                            loop.data[idx - num_of_dim + dim_id_2][entity_id_col] = loop.data[idx - num_of_dim + dim_id_1][entity_id_col]
                            loop.data[idx - num_of_dim + dim_id_2][seq_id_col] = loop.data[idx - num_of_dim + dim_id_1][seq_id_col]
                            loop.data[idx - num_of_dim + dim_id_2][comp_id_col] = loop.data[idx - num_of_dim + dim_id_1][comp_id_col]
                            loop.data[idx - num_of_dim + dim_id_2][auth_chain_id_col] = loop.data[idx - num_of_dim + dim_id_1][auth_chain_id_col]
                            loop.data[idx - num_of_dim + dim_id_2][auth_seq_id_col] = loop.data[idx - num_of_dim + dim_id_1][auth_seq_id_col]
                            loop.data[idx - num_of_dim + dim_id_2][auth_comp_id_col] = loop.data[idx - num_of_dim + dim_id_1][auth_comp_id_col]

                        if None in (shift, shift2):

                            if shift is None and shift2 is None:
                                continue

                            if shift is None and shift_ is not None:
                                alt_swap_chain_seq_id_1()

                            elif shift2 is None and shift2_ is not None:
                                alt_swap_chain_seq_id_2()

                            continue

                        diff = ((position - shift) * weight) ** 2 + ((position2 - shift2) * weight2) ** 2
                        diff *= 2.0

                        diff_ = diff2_ = None
                        if shift_ is not None:
                            diff_ = ((position - shift_) * weight) ** 2 + ((position2 - shift2) * weight2) ** 2
                        if shift2_ is not None:
                            diff2_ = ((position - shift) * weight) ** 2 + ((position2 - shift2_) * weight2) ** 2

                        if diff_ is not None and diff2_ is not None:
                            if diff_ < diff and diff2_ < diff:
                                if diff_ < diff2_:
                                    alt_swap_chain_seq_id_1()
                                elif diff_ > diff2_:
                                    alt_swap_chain_seq_id_2()
                            elif diff_ < diff:
                                alt_swap_chain_seq_id_1()
                            elif diff2_ < diff:
                                alt_swap_chain_seq_id_2()

                        elif diff_ is not None and diff_ < diff:
                            alt_swap_chain_seq_id_1()

                        elif diff2_ is not None and diff2_ < diff:
                            alt_swap_chain_seq_id_2()

    def __remediatePeakAssignmentForJcouplingTransfer(self, num_of_dim: int, jcoupling_transfers: List[List[int]], use_peak_row_format: bool, loop: pynmrstar.Loop):

        details_col = loop.tags.index('Details')

        for dim_id_1, dim_id_2 in jcoupling_transfers:

            if use_peak_row_format:

                tags = [f'Entity_assembly_ID_{dim_id_1}', f'Comp_index_ID_{dim_id_1}', f'Comp_ID_{dim_id_1}', f'Atom_ID_{dim_id_1}', f'Position_{dim_id_1}',
                        f'Entity_assembly_ID_{dim_id_2}', f'Comp_index_ID_{dim_id_2}', f'Comp_ID_{dim_id_2}', f'Atom_ID_{dim_id_2}', f'Position_{dim_id_2}']

                dat = loop.get_tag(tags)

                for idx, row in enumerate(dat):

                    if any(row[col] in emptyValue for col in range(10)):
                        continue

                    chain_id, seq_id, comp_id, atom_id, chain_id2, seq_id2, comp_id2, atom_id2 =\
                        row[0], row[1], row[2], row[3], row[5], row[6], row[7], row[8]

                    if isinstance(chain_id, int):
                        chain_id = str(chain_id)

                    if isinstance(chain_id2, int):
                        chain_id2 = str(chain_id2)

                    if isinstance(seq_id, str):
                        seq_id = int(seq_id)

                    if isinstance(seq_id2, str):
                        seq_id2 = int(seq_id2)

                    if chain_id == chain_id2 and seq_id == seq_id2 and comp_id == comp_id2:
                        continue

                    if chain_id == chain_id2 and seq_id != seq_id2:
                        position, position2 = row[4], row[9]

                        if isinstance(position, str):
                            position = float(position)

                        if isinstance(position2, str):
                            position2 = float(position2)

                        shift, weight = self.__getCsValue(chain_id, seq_id, comp_id, atom_id)
                        shift2, weight2 = self.__getCsValue(chain_id, seq_id2, comp_id2, atom_id2)

                        if None in (shift, shift2):
                            continue

                        diff = abs(position - shift) * weight
                        diff2 = abs(position2 - shift2) * weight2

                        if diff < diff2:
                            if self.__getCsValue(chain_id, seq_id, comp_id, atom_id2)[0] is not None:
                                if loop.data[idx][details_col] in emptyValue:
                                    loop.data[idx][details_col] = f'{seq_id2}:{comp_id2} -> {seq_id}:{comp_id}'
                                loop.data[idx][loop.tags.index(f'Comp_index_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Comp_index_ID_{dim_id_1}')]
                                loop.data[idx][loop.tags.index(f'Comp_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Comp_ID_{dim_id_1}')]
                                loop.data[idx][loop.tags.index(f'Auth_seq_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Auth_seq_ID_{dim_id_1}')]
                                loop.data[idx][loop.tags.index(f'Auth_comp_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Auth_comp_ID_{dim_id_1}')]

                        elif diff > diff2:
                            if self.__getCsValue(chain_id, seq_id2, comp_id2, atom_id)[0] is not None:
                                if loop.data[idx][details_col] in emptyValue:
                                    loop.data[idx][details_col] = f'{seq_id}:{comp_id} -> {seq_id2}:{comp_id2}'
                                loop.data[idx][loop.tags.index(f'Comp_index_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Comp_index_ID_{dim_id_2}')]
                                loop.data[idx][loop.tags.index(f'Comp_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Comp_ID_{dim_id_2}')]
                                loop.data[idx][loop.tags.index(f'Auth_seq_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Auth_seq_ID_{dim_id_2}')]
                                loop.data[idx][loop.tags.index(f'Auth_comp_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Auth_comp_ID_{dim_id_2}')]

                    elif chain_id != chain_id2:
                        position, position2 = row[4], row[9]

                        if isinstance(position, str):
                            position = float(position)

                        if isinstance(position2, str):
                            position2 = float(position2)

                        shift, weight = self.__getCsValue(chain_id, seq_id, comp_id, atom_id)
                        shift2, weight2 = self.__getCsValue(chain_id2, seq_id2, comp_id2, atom_id2)

                        if None in (shift, shift2):
                            continue

                        diff = abs(position - shift) * weight
                        diff2 = abs(position2 - shift2) * weight2

                        if diff < diff2:
                            if self.__getCsValue(chain_id, seq_id, comp_id, atom_id2)[0] is not None:
                                if loop.data[idx][details_col] in emptyValue:
                                    loop.data[idx][details_col] = f'{chain_id2}:{seq_id2}:{comp_id2} -> {chain_id}:{seq_id}:{comp_id}'
                                loop.data[idx][loop.tags.index(f'Entity_assembly_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Entity_assembly_ID_{dim_id_1}')]
                                loop.data[idx][loop.tags.index(f'Entity_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Entity_ID_{dim_id_1}')]
                                loop.data[idx][loop.tags.index(f'Comp_index_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Comp_index_ID_{dim_id_1}')]
                                loop.data[idx][loop.tags.index(f'Comp_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Comp_ID_{dim_id_1}')]
                                loop.data[idx][loop.tags.index(f'Auth_asym_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Auth_asym_ID_{dim_id_1}')]
                                loop.data[idx][loop.tags.index(f'Auth_seq_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Auth_seq_ID_{dim_id_1}')]
                                loop.data[idx][loop.tags.index(f'Auth_comp_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Auth_comp_ID_{dim_id_1}')]

                        elif diff > diff2:
                            if self.__getCsValue(chain_id2, seq_id2, comp_id2, atom_id)[0] is not None:
                                if loop.data[idx][details_col] in emptyValue:
                                    loop.data[idx][details_col] = f'{chain_id}:{seq_id}:{comp_id} -> {chain_id2}:{seq_id2}:{comp_id2}'
                                loop.data[idx][loop.tags.index(f'Entity_assembly_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Entity_assembly_ID_{dim_id_2}')]
                                loop.data[idx][loop.tags.index(f'Entity_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Entity_ID_{dim_id_2}')]
                                loop.data[idx][loop.tags.index(f'Comp_index_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Comp_index_ID_{dim_id_2}')]
                                loop.data[idx][loop.tags.index(f'Comp_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Comp_ID_{dim_id_2}')]
                                loop.data[idx][loop.tags.index(f'Auth_asym_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Auth_asym_ID_{dim_id_2}')]
                                loop.data[idx][loop.tags.index(f'Auth_seq_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Auth_seq_ID_{dim_id_2}')]
                                loop.data[idx][loop.tags.index(f'Auth_comp_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Auth_comp_ID_{dim_id_2}')]

            else:

                tags = ['Peak_ID', 'Spectral_dim_ID', 'Entity_assembly_ID', 'Comp_index_ID', 'Comp_ID', 'Atom_ID', 'Val']

                chain_id_col = loop.tags.index('Entity_assembly_ID')
                entity_id_col = loop.tags.index('Entity_ID')
                seq_id_col = loop.tags.index('Comp_index_ID')
                comp_id_col = loop.tags.index('Comp_ID')
                auth_chain_id_col = loop.tags.index('Auth_asym_ID')
                auth_seq_id_col = loop.tags.index('Auth_seq_ID')
                auth_comp_id_col = loop.tags.index('Auth_comp_ID')

                dat = loop.get_tag(tags)

                peak_id = None

                for idx, row in enumerate(dat):
                    dim_id = row[1]

                    if any(row[col] in emptyValue for col in range(7)):
                        continue

                    if dim_id == 1:
                        peak_id = row[0]
                        chain_ids, seq_ids, comp_ids, atom_ids, positions = [], [], [], [], []
                    else:
                        if peak_id != row[0]:
                            continue

                    chain_ids.append(row[2] if isinstance(row[2], str) else str(row[2]))
                    seq_ids.append(int(row[3]) if isinstance(row[3], str) else row[3])
                    comp_ids.append(row[4])
                    atom_ids.append(row[5])
                    positions.append(float(row[6]) if isinstance(row[6], str) else row[6])

                    if dim_id < num_of_dim:
                        continue

                    if len(atom_ids) < num_of_dim:
                        continue

                    _dim_id_1 = dim_id_1 - 1
                    _dim_id_2 = dim_id_2 - 1

                    chain_id, seq_id, comp_id, atom_id, position, chain_id2, seq_id2, comp_id2, atom_id2, position2 =\
                        chain_ids[_dim_id_1], seq_ids[_dim_id_1], comp_ids[_dim_id_1], atom_ids[_dim_id_1], positions[_dim_id_1], \
                        chain_ids[_dim_id_2], seq_ids[_dim_id_2], comp_ids[_dim_id_2], atom_ids[_dim_id_2], positions[_dim_id_2]

                    if chain_id == chain_id2 and seq_id == seq_id2 and comp_id == comp_id2:
                        continue

                    if chain_id == chain_id2 and seq_id != seq_id2:
                        shift, weight = self.__getCsValue(chain_id, seq_id, comp_id, atom_id)
                        shift2, weight2 = self.__getCsValue(chain_id, seq_id2, comp_id2, atom_id2)

                        if None in (shift, shift2):
                            continue

                        diff = abs(position - shift) * weight
                        diff2 = abs(position2 - shift2) * weight2

                        if diff < diff2:
                            if self.__getCsValue(chain_id, seq_id, comp_id, atom_id2)[0] is not None:
                                if loop.data[idx - num_of_dim + dim_id_2][details_col] in emptyValue:
                                    loop.data[idx - num_of_dim + dim_id_2][details_col] = f'{seq_id2}:{comp_id2} -> {seq_id}:{comp_id}'
                                loop.data[idx - num_of_dim + dim_id_2][seq_id_col] = loop.data[idx - num_of_dim + dim_id_1][seq_id_col]
                                loop.data[idx - num_of_dim + dim_id_2][comp_id_col] = loop.data[idx - num_of_dim + dim_id_1][comp_id_col]
                                loop.data[idx - num_of_dim + dim_id_2][auth_seq_id_col] = loop.data[idx - num_of_dim + dim_id_1][auth_seq_id_col]
                                loop.data[idx - num_of_dim + dim_id_2][auth_comp_id_col] = loop.data[idx - num_of_dim + dim_id_1][auth_comp_id_col]

                        elif diff > diff2:
                            if self.__getCsValue(chain_id, seq_id2, comp_id2, atom_id)[0] is not None:
                                if loop.data[idx][details_col] in emptyValue:
                                    loop.data[idx - num_of_dim + dim_id_1][details_col] = f'{seq_id}:{comp_id} -> {seq_id2}:{comp_id2}'
                                loop.data[idx - num_of_dim + dim_id_1][seq_id_col] = loop.data[idx - num_of_dim + dim_id_2][seq_id_col]
                                loop.data[idx - num_of_dim + dim_id_1][comp_id_col] = loop.data[idx - num_of_dim + dim_id_2][comp_id_col]
                                loop.data[idx - num_of_dim + dim_id_1][auth_seq_id_col] = loop.data[idx - num_of_dim + dim_id_2][auth_seq_id_col]
                                loop.data[idx - num_of_dim + dim_id_1][auth_comp_id_col] = loop.data[idx - num_of_dim + dim_id_2][auth_comp_id_col]

                    elif chain_id != chain_id2:
                        shift, weight = self.__getCsValue(chain_id, seq_id, comp_id, atom_id)
                        shift2, weight2 = self.__getCsValue(chain_id2, seq_id2, comp_id2, atom_id2)

                        if None in (shift, shift2):
                            continue

                        diff = abs(position - shift) * weight
                        diff2 = abs(position2 - shift2) * weight2

                        if diff < diff2:
                            if self.__getCsValue(chain_id, seq_id, comp_id, atom_id2)[0] is not None:
                                if loop.data[idx - num_of_dim + dim_id_2][details_col] in emptyValue:
                                    loop.data[idx - num_of_dim + dim_id_2][details_col] = f'{chain_id2}:{seq_id2}:{comp_id2} -> {chain_id}:{seq_id}:{comp_id}'
                                loop.data[idx - num_of_dim + dim_id_2][chain_id_col] = loop.data[idx - num_of_dim + dim_id_1][chain_id_col]
                                loop.data[idx - num_of_dim + dim_id_2][entity_id_col] = loop.data[idx - num_of_dim + dim_id_1][entity_id_col]
                                loop.data[idx - num_of_dim + dim_id_2][seq_id_col] = loop.data[idx - num_of_dim + dim_id_1][seq_id_col]
                                loop.data[idx - num_of_dim + dim_id_2][comp_id_col] = loop.data[idx - num_of_dim + dim_id_1][comp_id_col]
                                loop.data[idx - num_of_dim + dim_id_2][auth_chain_id_col] = loop.data[idx - num_of_dim + dim_id_1][auth_chain_id_col]
                                loop.data[idx - num_of_dim + dim_id_2][auth_seq_id_col] = loop.data[idx - num_of_dim + dim_id_1][auth_seq_id_col]
                                loop.data[idx - num_of_dim + dim_id_2][auth_comp_id_col] = loop.data[idx - num_of_dim + dim_id_1][auth_comp_id_col]

                        elif diff > diff2:
                            if self.__getCsValue(chain_id2, seq_id2, comp_id2, atom_id)[0] is not None:
                                if loop.data[idx][details_col] in emptyValue:
                                    loop.data[idx - num_of_dim + dim_id_1][details_col] = f'{chain_id}:{seq_id}:{comp_id} -> {chain_id2}:{seq_id2}:{comp_id2}'
                                loop.data[idx - num_of_dim + dim_id_1][chain_id_col] = loop.data[idx - num_of_dim + dim_id_2][chain_id_col]
                                loop.data[idx - num_of_dim + dim_id_1][entity_id_col] = loop.data[idx - num_of_dim + dim_id_2][entity_id_col]
                                loop.data[idx - num_of_dim + dim_id_1][seq_id_col] = loop.data[idx - num_of_dim + dim_id_2][seq_id_col]
                                loop.data[idx - num_of_dim + dim_id_1][comp_id_col] = loop.data[idx - num_of_dim + dim_id_2][comp_id_col]
                                loop.data[idx - num_of_dim + dim_id_1][auth_chain_id_col] = loop.data[idx - num_of_dim + dim_id_2][auth_chain_id_col]
                                loop.data[idx - num_of_dim + dim_id_1][auth_seq_id_col] = loop.data[idx - num_of_dim + dim_id_2][auth_seq_id_col]
                                loop.data[idx - num_of_dim + dim_id_1][auth_comp_id_col] = loop.data[idx - num_of_dim + dim_id_2][auth_comp_id_col]

    def __remediatePeakAssignmentForRelayedTransfer(self, num_of_dim: int, relayed_transfers: List[List[int]], use_peak_row_format: bool, loop: pynmrstar.Loop):

        details_col = loop.tags.index('Details')

        for dim_id_1, dim_id_2 in relayed_transfers:

            if use_peak_row_format:

                tags = [f'Entity_assembly_ID_{dim_id_1}', f'Comp_index_ID_{dim_id_1}', f'Comp_ID_{dim_id_1}', f'Atom_ID_{dim_id_1}', f'Position_{dim_id_1}',
                        f'Entity_assembly_ID_{dim_id_2}', f'Comp_index_ID_{dim_id_2}', f'Comp_ID_{dim_id_2}', f'Atom_ID_{dim_id_2}', f'Position_{dim_id_2}']

                dat = loop.get_tag(tags)

                for idx, row in enumerate(dat):

                    if any(row[col] in emptyValue for col in range(10)):
                        continue

                    chain_id, seq_id, comp_id, atom_id, chain_id2, seq_id2, comp_id2, atom_id2 =\
                        row[0], row[1], row[2], row[3], row[5], row[6], row[7], row[8]

                    if isinstance(chain_id, int):
                        chain_id = str(chain_id)

                    if isinstance(chain_id2, int):
                        chain_id2 = str(chain_id2)

                    if isinstance(seq_id, str):
                        seq_id = int(seq_id)

                    if isinstance(seq_id2, str):
                        seq_id2 = int(seq_id2)

                    if chain_id != chain_id2 or (seq_id == seq_id2 and comp_id == comp_id2):
                        continue

                    if abs(seq_id - seq_id2) > 1:
                        position, position2 = row[4], row[9]

                        if isinstance(chain_id, int):
                            chain_id = str(chain_id)

                        if isinstance(position, str):
                            position = float(position)

                        if isinstance(position2, str):
                            position2 = float(position2)

                        shift, weight = self.__getCsValue(chain_id, seq_id, comp_id, atom_id)
                        shift2, weight2 = self.__getCsValue(chain_id, seq_id2, comp_id2, atom_id2)

                        if None in (shift, shift2):
                            continue

                        diff = abs(position - shift) * weight
                        diff2 = abs(position2 - shift2) * weight2

                        if diff < diff2:
                            if self.__getCsValue(chain_id, seq_id, comp_id, atom_id2)[0] is not None:
                                if loop.data[idx][details_col] in emptyValue:
                                    loop.data[idx][details_col] = f'{seq_id2}:{comp_id2} -> {seq_id}:{comp_id}'
                                loop.data[idx][loop.tags.index(f'Comp_index_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Comp_index_ID_{dim_id_1}')]
                                loop.data[idx][loop.tags.index(f'Comp_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Comp_ID_{dim_id_1}')]
                                loop.data[idx][loop.tags.index(f'Auth_seq_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Auth_seq_ID_{dim_id_1}')]
                                loop.data[idx][loop.tags.index(f'Auth_comp_ID_{dim_id_2}')] = loop.data[idx][loop.tags.index(f'Auth_comp_ID_{dim_id_1}')]

                        elif diff > diff2:
                            if self.__getCsValue(chain_id, seq_id2, comp_id2, atom_id)[0] is not None:
                                if loop.data[idx][details_col] in emptyValue:
                                    loop.data[idx][details_col] = f'{seq_id}:{comp_id} -> {seq_id2}:{comp_id2}'
                                loop.data[idx][loop.tags.index(f'Comp_index_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Comp_index_ID_{dim_id_2}')]
                                loop.data[idx][loop.tags.index(f'Comp_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Comp_ID_{dim_id_2}')]
                                loop.data[idx][loop.tags.index(f'Auth_seq_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Auth_seq_ID_{dim_id_2}')]
                                loop.data[idx][loop.tags.index(f'Auth_comp_ID_{dim_id_1}')] = loop.data[idx][loop.tags.index(f'Auth_comp_ID_{dim_id_2}')]

            else:

                tags = ['Peak_ID', 'Spectral_dim_ID', 'Entity_assembly_ID', 'Comp_index_ID', 'Comp_ID', 'Atom_ID', 'Val']

                seq_id_col = loop.tags.index('Comp_index_ID')
                comp_id_col = loop.tags.index('Comp_ID')
                auth_seq_id_col = loop.tags.index('Auth_seq_ID')
                auth_comp_id_col = loop.tags.index('Auth_comp_ID')

                dat = loop.get_tag(tags)

                peak_id = None

                for idx, row in enumerate(dat):
                    dim_id = row[1]

                    if any(row[col] in emptyValue for col in range(7)):
                        continue

                    if dim_id == 1:
                        peak_id = row[0]
                        chain_ids, seq_ids, comp_ids, atom_ids, positions = [], [], [], [], []
                    else:
                        if peak_id != row[0]:
                            continue

                    chain_ids.append(row[2] if isinstance(row[2], str) else str(row[2]))
                    seq_ids.append(int(row[3]) if isinstance(row[3], str) else row[3])
                    comp_ids.append(row[4])
                    atom_ids.append(row[5])
                    positions.append(float(row[6]) if isinstance(row[6], str) else row[6])

                    if dim_id < num_of_dim:
                        continue

                    if len(atom_ids) < num_of_dim:
                        continue

                    _dim_id_1 = dim_id_1 - 1
                    _dim_id_2 = dim_id_2 - 1

                    chain_id, seq_id, comp_id, atom_id, position, chain_id2, seq_id2, comp_id2, atom_id2, position2 =\
                        chain_ids[_dim_id_1], seq_ids[_dim_id_1], comp_ids[_dim_id_1], atom_ids[_dim_id_1], positions[_dim_id_1], \
                        chain_ids[_dim_id_2], seq_ids[_dim_id_2], comp_ids[_dim_id_2], atom_ids[_dim_id_2], positions[_dim_id_2]

                    if chain_id != chain_id2 or (seq_id == seq_id2 and comp_id == comp_id2):
                        continue

                    if abs(seq_id - seq_id2) > 1:
                        chain_id = chain_ids[_dim_id_1]

                        if isinstance(chain_id, int):
                            chain_id = str(chain_id)

                        shift, weight = self.__getCsValue(chain_id, seq_id, comp_id, atom_id)
                        shift2, weight2 = self.__getCsValue(chain_id, seq_id2, comp_id2, atom_id2)

                        if None in (shift, shift2):
                            continue

                        diff = abs(position - shift) * weight
                        diff2 = abs(position2 - shift2) * weight2

                        if diff < diff2:
                            if self.__getCsValue(chain_id, seq_id, comp_id, atom_id2)[0] is not None:
                                if loop.data[idx - num_of_dim + dim_id_2][details_col] in emptyValue:
                                    loop.data[idx - num_of_dim + dim_id_2][details_col] = f'{seq_id2}:{comp_id2} -> {seq_id}:{comp_id}'
                                loop.data[idx - num_of_dim + dim_id_2][seq_id_col] = loop.data[idx - num_of_dim + dim_id_1][seq_id_col]
                                loop.data[idx - num_of_dim + dim_id_2][comp_id_col] = loop.data[idx - num_of_dim + dim_id_1][comp_id_col]
                                loop.data[idx - num_of_dim + dim_id_2][auth_seq_id_col] = loop.data[idx - num_of_dim + dim_id_1][auth_seq_id_col]
                                loop.data[idx - num_of_dim + dim_id_2][auth_comp_id_col] = loop.data[idx - num_of_dim + dim_id_1][auth_comp_id_col]

                        elif diff > diff2:
                            if self.__getCsValue(chain_id, seq_id2, comp_id2, atom_id)[0] is not None:
                                if loop.data[idx][details_col] in emptyValue:
                                    loop.data[idx - num_of_dim + dim_id_1][details_col] = f'{seq_id}:{comp_id} -> {seq_id2}:{comp_id2}'
                                loop.data[idx - num_of_dim + dim_id_1][seq_id_col] = loop.data[idx - num_of_dim + dim_id_2][seq_id_col]
                                loop.data[idx - num_of_dim + dim_id_1][comp_id_col] = loop.data[idx - num_of_dim + dim_id_2][comp_id_col]
                                loop.data[idx - num_of_dim + dim_id_1][auth_seq_id_col] = loop.data[idx - num_of_dim + dim_id_2][auth_seq_id_col]
                                loop.data[idx - num_of_dim + dim_id_1][auth_comp_id_col] = loop.data[idx - num_of_dim + dim_id_2][auth_comp_id_col]

    def __getCsValue(self, chain_id: str, seq_id: int, comp_id: str, atom_id: str) -> Tuple[Optional[float], Optional[float]]:

        if self.__csLoops is None or len(self.__csLoops) == 0:
            return None, None

        _atom_ids = self.nefT.get_valid_star_atom(comp_id, atom_id, leave_unmatched=False)[0]

        for lp in self.__csLoops:
            row = next((row for row in lp['data']
                        if row['Entity_assembly_ID'] == chain_id and row['Comp_index_ID'] == seq_id
                        and row['Comp_ID'] == comp_id and row['Atom_ID'] in _atom_ids), None)

            if row is not None:
                isotope_num = row['Atom_isotope_number']
                weight = 1.0
                if isotope_num == 13:
                    weight = 0.251449530
                elif isotope_num == 15:
                    weight = 0.101329118
                elif isotope_num == 2:
                    weight = 0.153506088
                return row['Val'], weight

        return None, None

    def validatePeak2D(self, index: int, pos_1: float, pos_2: float,
                       pos_unc_1: Optional[float], pos_unc_2: Optional[float],
                       lw_1: Optional[float], lw_2: Optional[float],
                       pos_hz_1: Optional[float], pos_hz_2: Optional[float],  # pylint: disable=unused-argument
                       lw_hz_1: Optional[float], lw_hz_2: Optional[float],
                       height: Optional[str], height_uncertainty: Optional[str],
                       volume: Optional[str], volume_uncertainty: Optional[str]) -> Optional[dict]:

        validRange = True
        dstFunc = {}

        if CS_ERROR_MIN < pos_1 < CS_ERROR_MAX:
            dstFunc['position_1'] = str(pos_1)
        else:
            validRange = False
            self.f.append(f"[Range value error] {self.getCurrentRestraint(n=index)}"
                          f"The position_1='{pos_1}' must be within range {CS_RESTRAINT_ERROR}.")

        if CS_ERROR_MIN < pos_2 < CS_ERROR_MAX:
            dstFunc['position_2'] = str(pos_2)
        else:
            validRange = False
            self.f.append(f"[Range value error] {self.getCurrentRestraint(n=index)}"
                          f"The position_2='{pos_2}' must be within range {CS_RESTRAINT_ERROR}.")

        if not validRange:
            return None

        if CS_RANGE_MIN <= pos_1 <= CS_RANGE_MAX:
            pass
        else:
            self.f.append(f"[Range value warning] {self.getCurrentRestraint(n=index)}"
                          f"The position_1='{pos_1}' should be within range {CS_RESTRAINT_RANGE}.")

        if CS_RANGE_MIN <= pos_2 <= CS_RANGE_MAX:
            pass
        else:
            self.f.append(f"[Range value warning] {self.getCurrentRestraint(n=index)}"
                          f"The position_2='{pos_2}' should be within range {CS_RESTRAINT_RANGE}.")

        if height is not None and float(height) != 0.0:
            dstFunc['height'] = height
        if volume is not None and float(volume) != 0.0:
            dstFunc['volume'] = volume
        if height_uncertainty is not None and float(height_uncertainty) != 0.0:
            dstFunc['height_uncertainty'] = height_uncertainty
        if volume_uncertainty is not None and float(volume_uncertainty) != 0.0:
            dstFunc['volume_uncertainty'] = volume_uncertainty

        if 'height' not in dstFunc and 'volume' not in dstFunc and not self.internal:
            self.f.append(f"[Missing data] {self.getCurrentRestraint(n=index)}"
                          "Neither height nor volume value is set.")
            return None

        if pos_unc_1 is not None and pos_unc_1 != 0.0:
            dstFunc['position_uncertainty_1'] = str(pos_unc_1)
        if pos_unc_2 is not None and pos_unc_2 != 0.0:
            dstFunc['position_uncertainty_2'] = str(pos_unc_2)

        if lw_hz_1 is not None and lw_hz_1 != 0.0:
            dstFunc['line_width_1'] = str(lw_hz_1)
        elif lw_1 is not None and lw_1 != 0.0:
            dstFunc['line_width_1'] = str(lw_1)
        if lw_hz_2 is not None and lw_hz_2 != 0.0:
            dstFunc['line_width_2'] = str(lw_hz_2)
        elif lw_2 is not None and lw_2 != 0.0:
            dstFunc['line_width_2'] = str(lw_2)

        return dstFunc

    def validatePeak3D(self, index: int, pos_1: float, pos_2: float, pos_3: float,
                       pos_unc_1: Optional[float], pos_unc_2: Optional[float], pos_unc_3: Optional[float],
                       lw_1: Optional[float], lw_2: Optional[float], lw_3: Optional[float],
                       pos_hz_1: Optional[float], pos_hz_2: Optional[float], pos_hz_3: Optional[float],  # pylint: disable=unused-argument
                       lw_hz_1: Optional[float], lw_hz_2: Optional[float], lw_hz_3: Optional[float],
                       height: Optional[str], height_uncertainty: Optional[str],
                       volume: Optional[str], volume_uncertainty: Optional[str]) -> Optional[dict]:

        validRange = True
        dstFunc = {}

        if CS_ERROR_MIN < pos_1 < CS_ERROR_MAX:
            dstFunc['position_1'] = str(pos_1)
        else:
            validRange = False
            self.f.append(f"[Range value error] {self.getCurrentRestraint(n=index)}"
                          f"The position_1='{pos_1}' must be within range {CS_RESTRAINT_ERROR}.")

        if CS_ERROR_MIN < pos_2 < CS_ERROR_MAX:
            dstFunc['position_2'] = str(pos_2)
        else:
            validRange = False
            self.f.append(f"[Range value error] {self.getCurrentRestraint(n=index)}"
                          f"The position_2='{pos_2}' must be within range {CS_RESTRAINT_ERROR}.")

        if CS_ERROR_MIN < pos_3 < CS_ERROR_MAX:
            dstFunc['position_3'] = str(pos_3)
        else:
            validRange = False
            self.f.append(f"[Range value error] {self.getCurrentRestraint(n=index)}"
                          f"The position_3='{pos_3}' must be within range {CS_RESTRAINT_ERROR}.")

        if not validRange:
            return None

        if CS_RANGE_MIN <= pos_1 <= CS_RANGE_MAX:
            pass
        else:
            self.f.append(f"[Range value warning] {self.getCurrentRestraint(n=index)}"
                          f"The position_1='{pos_1}' should be within range {CS_RESTRAINT_RANGE}.")

        if CS_RANGE_MIN <= pos_2 <= CS_RANGE_MAX:
            pass
        else:
            self.f.append(f"[Range value warning] {self.getCurrentRestraint(n=index)}"
                          f"The position_2='{pos_2}' should be within range {CS_RESTRAINT_RANGE}.")

        if CS_RANGE_MIN <= pos_3 <= CS_RANGE_MAX:
            pass
        else:
            self.f.append(f"[Range value warning] {self.getCurrentRestraint(n=index)}"
                          f"The position_3='{pos_3}' should be within range {CS_RESTRAINT_RANGE}.")

        if height is not None and float(height) != 0.0:
            dstFunc['height'] = height
        if volume is not None and float(volume) != 0.0:
            dstFunc['volume'] = volume
        if height_uncertainty is not None and float(height_uncertainty) != 0.0:
            dstFunc['height_uncertainty'] = height_uncertainty
        if volume_uncertainty is not None and float(volume_uncertainty) != 0.0:
            dstFunc['volume_uncertainty'] = volume_uncertainty

        if 'height' not in dstFunc and 'volume' not in dstFunc and not self.internal:
            self.f.append(f"[Missing data] {self.getCurrentRestraint(n=index)}"
                          "Neither height nor volume value is set.")
            return None

        if pos_unc_1 is not None and pos_unc_1 != 0.0:
            dstFunc['position_uncertainty_1'] = str(pos_unc_1)
        if pos_unc_2 is not None and pos_unc_2 != 0.0:
            dstFunc['position_uncertainty_2'] = str(pos_unc_2)
        if pos_unc_3 is not None and pos_unc_3 != 0.0:
            dstFunc['position_uncertainty_3'] = str(pos_unc_3)

        if lw_hz_1 is not None and lw_hz_1 != 0.0:
            dstFunc['line_width_1'] = str(lw_hz_1)
        elif lw_1 is not None and lw_1 != 0.0:
            dstFunc['line_width_1'] = str(lw_1)
        if lw_hz_2 is not None and lw_hz_2 != 0.0:
            dstFunc['line_width_2'] = str(lw_hz_2)
        elif lw_2 is not None and lw_2 != 0.0:
            dstFunc['line_width_2'] = str(lw_2)
        if lw_hz_3 is not None and lw_hz_3 != 0.0:
            dstFunc['line_width_3'] = str(lw_hz_3)
        elif lw_3 is not None and lw_3 != 0.0:
            dstFunc['line_width_3'] = str(lw_3)

        return dstFunc

    def validatePeak4D(self, index: int, pos_1: float, pos_2: float, pos_3: float, pos_4: float,
                       pos_unc_1: Optional[float], pos_unc_2: Optional[float], pos_unc_3: Optional[float], pos_unc_4: Optional[float],
                       lw_1: Optional[float], lw_2: Optional[float], lw_3: Optional[float], lw_4: Optional[float],
                       pos_hz_1: Optional[float], pos_hz_2: Optional[float], pos_hz_3: Optional[float], pos_hz_4: Optional[float],  # pylint: disable=unused-argument
                       lw_hz_1: Optional[float], lw_hz_2: Optional[float], lw_hz_3: Optional[float], lw_hz_4: Optional[float],
                       height: Optional[str], height_uncertainty: Optional[str],
                       volume: Optional[str], volume_uncertainty: Optional[str]) -> Optional[dict]:

        validRange = True
        dstFunc = {}

        if CS_ERROR_MIN < pos_1 < CS_ERROR_MAX:
            dstFunc['position_1'] = str(pos_1)
        else:
            validRange = False
            self.f.append(f"[Range value error] {self.getCurrentRestraint(n=index)}"
                          f"The position_1='{pos_1}' must be within range {CS_RESTRAINT_ERROR}.")

        if CS_ERROR_MIN < pos_2 < CS_ERROR_MAX:
            dstFunc['position_2'] = str(pos_2)
        else:
            validRange = False
            self.f.append(f"[Range value error] {self.getCurrentRestraint(n=index)}"
                          f"The position_2='{pos_2}' must be within range {CS_RESTRAINT_ERROR}.")

        if CS_ERROR_MIN < pos_3 < CS_ERROR_MAX:
            dstFunc['position_3'] = str(pos_3)
        else:
            validRange = False
            self.f.append(f"[Range value error] {self.getCurrentRestraint(n=index)}"
                          f"The position_3='{pos_3}' must be within range {CS_RESTRAINT_ERROR}.")

        if CS_ERROR_MIN < pos_4 < CS_ERROR_MAX:
            dstFunc['position_4'] = str(pos_4)
        else:
            validRange = False
            self.f.append(f"[Range value error] {self.getCurrentRestraint(n=index)}"
                          f"The position_4='{pos_4}' must be within range {CS_RESTRAINT_ERROR}.")

        if not validRange:
            return None

        if CS_RANGE_MIN <= pos_1 <= CS_RANGE_MAX:
            pass
        else:
            self.f.append(f"[Range value warning] {self.getCurrentRestraint(n=index)}"
                          f"The position_1='{pos_1}' should be within range {CS_RESTRAINT_RANGE}.")

        if CS_RANGE_MIN <= pos_2 <= CS_RANGE_MAX:
            pass
        else:
            self.f.append(f"[Range value warning] {self.getCurrentRestraint(n=index)}"
                          f"The position_2='{pos_2}' should be within range {CS_RESTRAINT_RANGE}.")

        if CS_RANGE_MIN <= pos_3 <= CS_RANGE_MAX:
            pass
        else:
            self.f.append(f"[Range value warning] {self.getCurrentRestraint(n=index)}"
                          f"The position_3='{pos_3}' should be within range {CS_RESTRAINT_RANGE}.")

        if CS_RANGE_MIN <= pos_4 <= CS_RANGE_MAX:
            pass
        else:
            self.f.append(f"[Range value warning] {self.getCurrentRestraint(n=index)}"
                          f"The position_4='{pos_4}' should be within range {CS_RESTRAINT_RANGE}.")

        if height is not None and float(height) != 0.0:
            dstFunc['height'] = height
        if volume is not None and float(volume) != 0.0:
            dstFunc['volume'] = volume
        if height_uncertainty is not None and float(height_uncertainty) != 0.0:
            dstFunc['height_uncertainty'] = height_uncertainty
        if volume_uncertainty is not None and float(volume_uncertainty) != 0.0:
            dstFunc['volume_uncertainty'] = volume_uncertainty

        if 'height' not in dstFunc and 'volume' not in dstFunc and not self.internal:
            self.f.append(f"[Missing data] {self.getCurrentRestraint(n=index)}"
                          "Neither height nor volume value is set.")
            return None

        if pos_unc_1 is not None and pos_unc_1 != 0.0:
            dstFunc['position_uncertainty_1'] = str(pos_unc_1)
        if pos_unc_2 is not None and pos_unc_2 != 0.0:
            dstFunc['position_uncertainty_2'] = str(pos_unc_2)
        if pos_unc_3 is not None and pos_unc_3 != 0.0:
            dstFunc['position_uncertainty_3'] = str(pos_unc_3)
        if pos_unc_4 is not None and pos_unc_4 != 0.0:
            dstFunc['position_uncertainty_4'] = str(pos_unc_4)

        if lw_hz_1 is not None and lw_hz_1 != 0.0:
            dstFunc['line_width_1'] = str(lw_hz_1)
        elif lw_1 is not None and lw_1 != 0.0:
            dstFunc['line_width_1'] = str(lw_1)
        if lw_hz_2 is not None and lw_hz_2 != 0.0:
            dstFunc['line_width_2'] = str(lw_hz_2)
        elif lw_2 is not None and lw_2 != 0.0:
            dstFunc['line_width_2'] = str(lw_2)
        if lw_hz_3 is not None and lw_hz_3 != 0.0:
            dstFunc['line_width_3'] = str(lw_hz_3)
        elif lw_3 is not None and lw_3 != 0.0:
            dstFunc['line_width_3'] = str(lw_3)
        if lw_hz_4 is not None and lw_hz_4 != 0.0:
            dstFunc['line_width_4'] = str(lw_hz_4)
        elif lw_4 is not None and lw_4 != 0.0:
            dstFunc['line_width_4'] = str(lw_4)

        return dstFunc

    def checkAssignments2D(self, index: int, assignments: List[List[dict]]
                           ) -> Tuple[bool, bool, Optional[bool], Optional[bool]]:
        has_assignments = has_multiple_assignments = False
        asis1 = asis2 = None

        primary_specral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id][1]
        has_long_range = 'long_range' in primary_specral_dim

        if 'is_noesy' not in primary_specral_dim:
            file_name = self.__originalFileName.lower()
            alt_file_name = '' if self.spectrum_name is None else self.spectrum_name.lower()
            _file_names = (file_name, alt_file_name)
            primary_specral_dim['is_noesy'] = any('noe' in n for n in _file_names) or any('roe' in n for n in _file_names)
            if primary_specral_dim['is_noesy']:
                primary_specral_dim['long_range'] = True

        if all(assignment is not None for assignment in assignments):

            self.retrieveLocalSeqScheme()

            try:

                hasChainId = all(a[0]['chain_id'] is not None for a in assignments)
                hasCompId = all(a[0]['comp_id'] is not None for a in assignments)

                has_multiple_assignments = any(len(assignment) > 1 for assignment in assignments)

                pairs = []
                if len(assignments[0]) == len(assignments[1]):
                    for a1, a2 in zip(assignments[0], assignments[1]):
                        pairs.append((a1, a2))
                else:
                    for a1, a2 in itertools.product(assignments[0], assignments[1]):
                        pairs.append((a1, a2))

                for a1, a2 in pairs:

                    self.atomSelectionSet.clear()
                    asis1 = asis2 = None

                    if hasChainId and hasCompId:
                        chainAssign1, asis1 = self.assignCoordPolymerSequenceWithChainId(a1['chain_id'], a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                        chainAssign2, asis2 = self.assignCoordPolymerSequenceWithChainId(a2['chain_id'], a2['seq_id'], a2['comp_id'], a2['atom_id'], index)

                    elif hasChainId:
                        chainAssign1 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a1['chain_id'], a1['seq_id'], a1['atom_id'], index)
                        chainAssign2 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a2['chain_id'], a2['seq_id'], a2['atom_id'], index)

                    elif hasCompId:
                        chainAssign1, asis1 = self.assignCoordPolymerSequence(a1['chain_id'], a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                        chainAssign2, asis2 = self.assignCoordPolymerSequence(a2['chain_id'], a2['seq_id'], a2['comp_id'], a2['atom_id'], index)

                    else:
                        chainAssign1 = self.assignCoordPolymerSequenceWithoutCompId(a1['seq_id'], a1['atom_id'], index)
                        chainAssign2 = self.assignCoordPolymerSequenceWithoutCompId(a2['seq_id'], a2['atom_id'], index)

                    if len(chainAssign1) > 0 and len(chainAssign2) > 0:
                        self.selectCoordAtoms(chainAssign1, a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                        self.selectCoordAtoms(chainAssign2, a2['seq_id'], a2['comp_id'], a2['atom_id'], index)
                        if len(self.atomSelectionSet) == self.num_of_dim:
                            has_assignments = True
                            has_assignments &= self.validateAtomType(1, self.atomSelectionSet[0][0]['atom_id'][0])
                            has_assignments &= self.validateAtomType(2, self.atomSelectionSet[1][0]['atom_id'][0])
                            if has_assignments:
                                self.atomSelectionSets.append(copy.copy(self.atomSelectionSet))
                                self.asIsSets.append([asis1, asis2])
                                if not has_long_range:
                                    if hasInterChainRestraint(self.atomSelectionSet):
                                        has_long_range = True
                                        if 'long_range' not in primary_specral_dim:
                                            primary_specral_dim['long_range'] = True
                                    else:
                                        for atom1, atom2 in itertools.product(self.atomSelectionSet[0],
                                                                              self.atomSelectionSet[1]):
                                            has_long_range |= isLongRangeRestraint([atom1, atom2], self.polySeq)
                                            if has_long_range:
                                                if 'long_range' not in primary_specral_dim:
                                                    primary_specral_dim['long_range'] = True
                                                break
                            else:
                                break
                        else:
                            has_assignments = False
                            break

            except (KeyError, TypeError):
                pass

        return has_assignments, has_multiple_assignments, asis1, asis2

    def checkAssignments3D(self, index: int, assignments: List[List[dict]]
                           ) -> Tuple[bool, bool, Optional[bool], Optional[bool], Optional[bool]]:
        has_assignments = has_multiple_assignments = False
        asis1 = asis2 = asis3 = None

        primary_specral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id][1]
        has_long_range = 'long_range' in primary_specral_dim

        if 'is_noesy' not in primary_specral_dim:
            file_name = self.__originalFileName.lower()
            alt_file_name = '' if self.spectrum_name is None else self.spectrum_name.lower()
            _file_names = (file_name, alt_file_name)
            primary_specral_dim['is_noesy'] = any('noe' in n for n in _file_names) or any('roe' in n for n in _file_names)
            if primary_specral_dim['is_noesy']:
                primary_specral_dim['long_range'] = True

        if all(assignment is not None for assignment in assignments):

            if self.reasons is not None and 'onebond_resolved' in self.reasons:
                _assignments = [None] * 3
                for k, v in self.reasons['onebond_resolved'].items():
                    _assignments[v] = assignments[k]
                assignments = _assignments

            self.retrieveLocalSeqScheme()

            try:

                hasChainId = all(a[0]['chain_id'] is not None for a in assignments)
                hasCompId = all(a[0]['comp_id'] is not None for a in assignments)

                has_multiple_assignments = any(len(assignment) > 1 for assignment in assignments)

                pairs = []
                if len(assignments[0]) == len(assignments[1]) == len(assignments[2]):
                    for a1, a2, a3 in zip(assignments[0], assignments[1], assignments[2]):
                        pairs.append((a1, a2, a3))
                else:
                    for a1, a2, a3 in itertools.product(assignments[0], assignments[1], assignments[2]):
                        pairs.append((a1, a2, a3))

                for a1, a2, a3 in pairs:

                    self.atomSelectionSet.clear()
                    asis1 = asis2 = asis3 = None

                    if hasChainId and hasCompId:
                        chainAssign1, asis1 = self.assignCoordPolymerSequenceWithChainId(a1['chain_id'], a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                        chainAssign2, asis2 = self.assignCoordPolymerSequenceWithChainId(a2['chain_id'], a2['seq_id'], a2['comp_id'], a2['atom_id'], index)
                        chainAssign3, asis3 = self.assignCoordPolymerSequenceWithChainId(a3['chain_id'], a3['seq_id'], a3['comp_id'], a3['atom_id'], index)

                    elif hasChainId:
                        chainAssign1 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a1['chain_id'], a1['seq_id'], a1['atom_id'], index)
                        chainAssign2 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a2['chain_id'], a2['seq_id'], a2['atom_id'], index)
                        chainAssign3 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a3['chain_id'], a3['seq_id'], a3['atom_id'], index)

                    elif hasCompId:
                        chainAssign1, asis1 = self.assignCoordPolymerSequence(a1['chain_id'], a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                        chainAssign2, asis2 = self.assignCoordPolymerSequence(a2['chain_id'], a2['seq_id'], a2['comp_id'], a2['atom_id'], index)
                        chainAssign3, asis3 = self.assignCoordPolymerSequence(a3['chain_id'], a3['seq_id'], a3['comp_id'], a3['atom_id'], index)

                    else:
                        chainAssign1 = self.assignCoordPolymerSequenceWithoutCompId(a1['seq_id'], a1['atom_id'], index)
                        chainAssign2 = self.assignCoordPolymerSequenceWithoutCompId(a2['seq_id'], a2['atom_id'], index)
                        chainAssign3 = self.assignCoordPolymerSequenceWithoutCompId(a3['seq_id'], a3['atom_id'], index)

                    if len(chainAssign1) > 0 and len(chainAssign2) > 0 and len(chainAssign3) > 0:
                        self.selectCoordAtoms(chainAssign1, a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                        self.selectCoordAtoms(chainAssign2, a2['seq_id'], a2['comp_id'], a2['atom_id'], index)
                        self.selectCoordAtoms(chainAssign3, a3['seq_id'], a3['comp_id'], a3['atom_id'], index)

                        if len(self.atomSelectionSet) == self.num_of_dim:
                            has_assignments = True
                            has_assignments &= self.validateAtomType(1, self.atomSelectionSet[0][0]['atom_id'][0])
                            has_assignments &= self.validateAtomType(2, self.atomSelectionSet[1][0]['atom_id'][0])
                            has_assignments &= self.validateAtomType(3, self.atomSelectionSet[2][0]['atom_id'][0])
                            if has_assignments:
                                self.atomSelectionSets.append(copy.copy(self.atomSelectionSet))
                                self.asIsSets.append([asis1, asis2, asis3])
                                if not has_long_range:
                                    if hasInterChainRestraint(self.atomSelectionSet):
                                        has_long_range = True
                                        if 'long_range' not in primary_specral_dim:
                                            primary_specral_dim['long_range'] = True
                                    else:
                                        for atom1, atom2, atom3 in itertools.product(self.atomSelectionSet[0],
                                                                                     self.atomSelectionSet[1],
                                                                                     self.atomSelectionSet[2]):
                                            has_long_range |= isLongRangeRestraint([atom1, atom2, atom3], self.polySeq)
                                            if has_long_range:
                                                if 'long_range' not in primary_specral_dim:
                                                    primary_specral_dim['long_range'] = True
                                                break
                            else:
                                break
                        else:
                            has_assignments = False
                            break

            except (KeyError, TypeError):
                pass

        return has_assignments, has_multiple_assignments, asis1, asis2, asis3

    def checkAssignments4D(self, index: int, assignments: List[List[dict]]
                           ) -> Tuple[bool, bool, Optional[bool], Optional[bool], Optional[bool], Optional[bool]]:
        has_assignments = has_multiple_assignments = False
        asis1 = asis2 = asis3 = asis4 = None

        primary_specral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id][1]
        has_long_range = 'long_range' in primary_specral_dim

        if 'is_noesy' not in primary_specral_dim:
            file_name = self.__originalFileName.lower()
            alt_file_name = '' if self.spectrum_name is None else self.spectrum_name.lower()
            _file_names = (file_name, alt_file_name)
            primary_specral_dim['is_noesy'] = any('noe' in n for n in _file_names) or any('roe' in n for n in _file_names)
            if primary_specral_dim['is_noesy']:
                primary_specral_dim['long_range'] = True

        if all(assignment is not None for assignment in assignments):

            if self.reasons is not None and 'onebond_resolved' in self.reasons:
                _assignments = [None] * 4
                for k, v in self.reasons['onebond_resolved'].items():
                    _assignments[v] = assignments[k]
                assignments = _assignments

            self.retrieveLocalSeqScheme()

            try:

                hasChainId = all(a[0]['chain_id'] is not None for a in assignments)
                hasCompId = all(a[0]['comp_id'] is not None for a in assignments)

                has_multiple_assignments = any(len(assignment) > 1 for assignment in assignments)

                pairs = []
                if len(assignments[0]) == len(assignments[1]) == len(assignments[2]) == len(assignments[3]):
                    for a1, a2, a3, a4 in zip(assignments[0], assignments[1], assignments[2], assignments[3]):
                        pairs.append((a1, a2, a3, a4))
                else:
                    for a1, a2, a3, a4 in itertools.product(assignments[0], assignments[1], assignments[2], assignments[3]):
                        pairs.append((a1, a2, a3, a4))

                for a1, a2, a3, a4 in pairs:

                    self.atomSelectionSet.clear()
                    asis1 = asis2 = asis3 = asis4 = None

                    if hasChainId and hasCompId:
                        chainAssign1, asis1 = self.assignCoordPolymerSequenceWithChainId(a1['chain_id'], a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                        chainAssign2, asis2 = self.assignCoordPolymerSequenceWithChainId(a2['chain_id'], a2['seq_id'], a2['comp_id'], a2['atom_id'], index)
                        chainAssign3, asis3 = self.assignCoordPolymerSequenceWithChainId(a3['chain_id'], a3['seq_id'], a3['comp_id'], a3['atom_id'], index)
                        chainAssign4, asis4 = self.assignCoordPolymerSequenceWithChainId(a4['chain_id'], a4['seq_id'], a4['comp_id'], a4['atom_id'], index)

                    elif hasChainId:
                        chainAssign1 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a1['chain_id'], a1['seq_id'], a1['atom_id'], index)
                        chainAssign2 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a2['chain_id'], a2['seq_id'], a2['atom_id'], index)
                        chainAssign3 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a3['chain_id'], a3['seq_id'], a3['atom_id'], index)
                        chainAssign4 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a4['chain_id'], a4['seq_id'], a4['atom_id'], index)

                    elif hasCompId:
                        chainAssign1, asis1 = self.assignCoordPolymerSequence(a1['chain_id'], a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                        chainAssign2, asis2 = self.assignCoordPolymerSequence(a2['chain_id'], a2['seq_id'], a2['comp_id'], a2['atom_id'], index)
                        chainAssign3, asis3 = self.assignCoordPolymerSequence(a3['chain_id'], a3['seq_id'], a3['comp_id'], a3['atom_id'], index)
                        chainAssign4, asis4 = self.assignCoordPolymerSequence(a4['chain_id'], a4['seq_id'], a4['comp_id'], a4['atom_id'], index)

                    else:
                        chainAssign1 = self.assignCoordPolymerSequenceWithoutCompId(a1['seq_id'], a1['atom_id'], index)
                        chainAssign2 = self.assignCoordPolymerSequenceWithoutCompId(a2['seq_id'], a2['atom_id'], index)
                        chainAssign3 = self.assignCoordPolymerSequenceWithoutCompId(a3['seq_id'], a3['atom_id'], index)
                        chainAssign4 = self.assignCoordPolymerSequenceWithoutCompId(a4['seq_id'], a4['atom_id'], index)

                    if len(chainAssign1) > 0 and len(chainAssign2) > 0 and len(chainAssign3) > 0 and len(chainAssign4) > 0:
                        self.selectCoordAtoms(chainAssign1, a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                        self.selectCoordAtoms(chainAssign2, a2['seq_id'], a2['comp_id'], a2['atom_id'], index)
                        self.selectCoordAtoms(chainAssign3, a3['seq_id'], a3['comp_id'], a3['atom_id'], index)
                        self.selectCoordAtoms(chainAssign4, a4['seq_id'], a4['comp_id'], a4['atom_id'], index)

                        if len(self.atomSelectionSet) == self.num_of_dim:
                            has_assignments = True
                            has_assignments &= self.validateAtomType(1, self.atomSelectionSet[0][0]['atom_id'][0])
                            has_assignments &= self.validateAtomType(2, self.atomSelectionSet[1][0]['atom_id'][0])
                            has_assignments &= self.validateAtomType(3, self.atomSelectionSet[2][0]['atom_id'][0])
                            has_assignments &= self.validateAtomType(4, self.atomSelectionSet[3][0]['atom_id'][0])
                            if has_assignments:
                                self.atomSelectionSets.append(copy.copy(self.atomSelectionSet))
                                self.asIsSets.append([asis1, asis2, asis3, asis4])
                                if not has_long_range:
                                    if hasInterChainRestraint(self.atomSelectionSet):
                                        has_long_range = True
                                        if 'long_range' not in primary_specral_dim:
                                            primary_specral_dim['long_range'] = True
                                    else:
                                        for atom1, atom2, atom3, atom4 in itertools.product(self.atomSelectionSet[0],
                                                                                            self.atomSelectionSet[1],
                                                                                            self.atomSelectionSet[2],
                                                                                            self.atomSelectionSet[3]):
                                            has_long_range |= isLongRangeRestraint([atom1, atom2, atom3, atom4], self.polySeq)
                                            if has_long_range:
                                                if 'long_range' not in primary_specral_dim:
                                                    primary_specral_dim['long_range'] = True
                                                break
                            else:
                                break
                        else:
                            has_assignments = False
                            break

            except (KeyError, TypeError):
                pass

        return has_assignments, has_multiple_assignments, asis1, asis2, asis3, asis4

    def addAssignedPkRow2D(self, index: int, dstFunc: dict, has_assignments: bool, has_multiple_assignments: bool,
                           asis1: Optional[bool], asis2: Optional[bool],
                           debug_label: Optional[str], details: Optional[str]):

        if self.debug:
            if not has_assignments:
                print(f"subtype={self.cur_subtype} id={self.peaks2D} (index={index}) "
                      f"{debug_label}None None {dstFunc}")
            for idx, atomSelectionSet in enumerate(self.atomSelectionSets, start=1):
                if has_multiple_assignments:
                    print(f"subtype={self.cur_subtype} id={self.peaks2D} (index={index}) combination_id={idx} "
                          f"{debug_label}{atomSelectionSet[0]} "
                          f"{atomSelectionSet[1]} {dstFunc}")
                else:
                    print(f"subtype={self.cur_subtype} id={self.peaks2D} (index={index}) "
                          f"{debug_label}{atomSelectionSet[0]} "
                          f"{atomSelectionSet[1]} {dstFunc}")

        if self.createSfDict__:
            sf = self.getSf()

            if sf is not None:
                sf['id'] = index
                sf['index_id'] += 1
                ambig_code1 = ambig_code2 = None
                if has_assignments and not has_multiple_assignments:
                    atom1 = self.atomSelectionSet[0][0]
                    atom2 = self.atomSelectionSet[1][0]
                    if len(self.atomSelectionSet[0]) > 1:
                        ambig_code1 = self.csStat.getMaxAmbigCodeWoSetId(atom1['comp_id'], atom1['atom_id'])
                        if ambig_code1 == 0:
                            ambig_code1 = None
                    if len(self.atomSelectionSet[1]) > 1:
                        ambig_code2 = self.csStat.getMaxAmbigCodeWoSetId(atom2['comp_id'], atom2['atom_id'])
                        if ambig_code2 == 0:
                            ambig_code2 = None
                else:
                    atom1 = atom2 = None

                row = getPkRow(self.cur_subtype, sf['id'], sf['index_id'],
                               sf['list_id'], self.entryId, dstFunc,
                               self.authToStarSeq, self.authToOrigSeq, self.offsetHolder,
                               atom1, atom2, asis1=asis1, asis2=asis2,
                               ambig_code1=ambig_code1, ambig_code2=ambig_code2,
                               details=details)
                sf['loop'].add_data(row)

                row = getPkGenCharRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, 'volume')
                if row is not None:
                    sf['alt_loops'][0].add_data(row)
                row = getPkGenCharRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, 'height')
                if row is not None:
                    sf['alt_loops'][0].add_data(row)

                for idx in range(self.num_of_dim):
                    row = getPkCharRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, idx + 1)
                    sf['alt_loops'][1].add_data(row)
                if has_assignments:
                    for atomSelectionSet, asIsSet in zip(self.atomSelectionSets, self.asIsSets):
                        uniqAtoms = []
                        for idx in range(self.num_of_dim):
                            atom = atomSelectionSet[idx]
                            atom0 = atom[0]
                            if atom0 not in uniqAtoms:
                                asis = asIsSet[idx]
                                ambig_code = None
                                if len(atom) > 1:
                                    ambig_code = self.csStat.getMaxAmbigCodeWoSetId(atom0['comp_id'], atom0['atom_id'])
                                    if ambig_code == 0:
                                        ambig_code = None
                                row = getPkChemShiftRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, idx + 1,
                                                        self.authToStarSeq, self.authToOrigSeq, self.offsetHolder,
                                                        atom0, asis, ambig_code)
                                sf['alt_loops'][2].add_data(row)
                                uniqAtoms.append(atom0)

    def addAssignedPkRow3D(self, index: int, dstFunc: dict, has_assignments: bool, has_multiple_assignments: bool,
                           asis1: Optional[bool], asis2: Optional[bool], asis3: Optional[bool],
                           debug_label: Optional[str], details: Optional[str]):

        if self.debug:
            if not has_assignments:
                print(f"subtype={self.cur_subtype} id={self.peaks3D} (index={index}) "
                      f"{debug_label}None None None {dstFunc}")
            for idx, atomSelectionSet in enumerate(self.atomSelectionSets, start=1):
                if has_multiple_assignments:
                    print(f"subtype={self.cur_subtype} id={self.peaks3D} (index={index}) combination_id={idx} "
                          f"{debug_label}{atomSelectionSet[0]} "
                          f"{atomSelectionSet[1]} "
                          f"{atomSelectionSet[2]} {dstFunc}")
                else:
                    print(f"subtype={self.cur_subtype} id={self.peaks3D} (index={index}) "
                          f"{debug_label}{atomSelectionSet[0]} "
                          f"{atomSelectionSet[1]} "
                          f"{atomSelectionSet[2]} {dstFunc}")

        if self.createSfDict__:
            sf = self.getSf()

            if sf is not None:
                sf['id'] = index
                sf['index_id'] += 1
                ambig_code1 = ambig_code2 = ambig_code3 = None
                if has_assignments and not has_multiple_assignments:
                    atom1 = self.atomSelectionSet[0][0]
                    atom2 = self.atomSelectionSet[1][0]
                    atom3 = self.atomSelectionSet[2][0]
                    if len(self.atomSelectionSet[0]) > 1:
                        ambig_code1 = self.csStat.getMaxAmbigCodeWoSetId(atom1['comp_id'], atom1['atom_id'])
                        if ambig_code1 == 0:
                            ambig_code1 = None
                    if len(self.atomSelectionSet[1]) > 1:
                        ambig_code2 = self.csStat.getMaxAmbigCodeWoSetId(atom2['comp_id'], atom2['atom_id'])
                        if ambig_code2 == 0:
                            ambig_code2 = None
                    if len(self.atomSelectionSet[2]) > 1:
                        ambig_code3 = self.csStat.getMaxAmbigCodeWoSetId(atom3['comp_id'], atom3['atom_id'])
                        if ambig_code3 == 0:
                            ambig_code3 = None
                else:
                    atom1 = atom2 = atom3 = None

                row = getPkRow(self.cur_subtype, sf['id'], sf['index_id'],
                               sf['list_id'], self.entryId, dstFunc,
                               self.authToStarSeq, self.authToOrigSeq, self.offsetHolder,
                               atom1, atom2, atom3, asis1=asis1, asis2=asis2, asis3=asis3,
                               ambig_code1=ambig_code1, ambig_code2=ambig_code2,
                               ambig_code3=ambig_code3,
                               details=details)
                sf['loop'].add_data(row)

                row = getPkGenCharRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, 'volume')
                if row is not None:
                    sf['alt_loops'][0].add_data(row)
                row = getPkGenCharRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, 'height')
                if row is not None:
                    sf['alt_loops'][0].add_data(row)

                for idx in range(self.num_of_dim):
                    row = getPkCharRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, idx + 1)
                    sf['alt_loops'][1].add_data(row)
                if has_assignments:
                    for atomSelectionSet, asIsSet in zip(self.atomSelectionSets, self.asIsSets):
                        uniqAtoms = []
                        for idx in range(self.num_of_dim):
                            atom = atomSelectionSet[idx]
                            atom0 = atom[0]
                            if atom0 not in uniqAtoms:
                                asis = asIsSet[idx]
                                ambig_code = None
                                if len(atom) > 1:
                                    ambig_code = self.csStat.getMaxAmbigCodeWoSetId(atom0['comp_id'], atom0['atom_id'])
                                    if ambig_code == 0:
                                        ambig_code = None
                                row = getPkChemShiftRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, idx + 1,
                                                        self.authToStarSeq, self.authToOrigSeq, self.offsetHolder,
                                                        atom0, asis, ambig_code)
                                sf['alt_loops'][2].add_data(row)
                                uniqAtoms.append(atom0)

    def addAssignedPkRow4D(self, index: int, dstFunc: dict, has_assignments: bool, has_multiple_assignments: bool,
                           asis1: Optional[bool], asis2: Optional[bool], asis3: Optional[bool], asis4: Optional[bool],
                           debug_label: Optional[str], details: Optional[str]):

        if self.debug:
            if not has_assignments:
                print(f"subtype={self.cur_subtype} id={self.peaks4D} (index={index}) "
                      f"{debug_label}None None None None {dstFunc}")
            for idx, atomSelectionSet in enumerate(self.atomSelectionSets, start=1):
                if has_multiple_assignments:
                    print(f"subtype={self.cur_subtype} id={self.peaks4D} (index={index}) combination_id={idx} "
                          f"{debug_label}{atomSelectionSet[0]} "
                          f"{atomSelectionSet[1]} "
                          f"{atomSelectionSet[2]} "
                          f"{atomSelectionSet[3]} {dstFunc}")
                else:
                    print(f"subtype={self.cur_subtype} id={self.peaks4D} (index={index}) "
                          f"{debug_label}{atomSelectionSet[0]} "
                          f"{atomSelectionSet[1]} "
                          f"{atomSelectionSet[2]} "
                          f"{atomSelectionSet[3]} {dstFunc}")

        if self.createSfDict__:
            sf = self.getSf()

            if sf is not None:
                sf['id'] = index
                sf['index_id'] += 1
                ambig_code1 = ambig_code2 = ambig_code3 = ambig_code4 = None
                if has_assignments and not has_multiple_assignments:
                    atom1 = self.atomSelectionSet[0][0]
                    atom2 = self.atomSelectionSet[1][0]
                    atom3 = self.atomSelectionSet[2][0]
                    atom4 = self.atomSelectionSet[3][0]
                    if len(self.atomSelectionSet[0]) > 1:
                        ambig_code1 = self.csStat.getMaxAmbigCodeWoSetId(atom1['comp_id'], atom1['atom_id'])
                        if ambig_code1 == 0:
                            ambig_code1 = None
                    if len(self.atomSelectionSet[1]) > 1:
                        ambig_code2 = self.csStat.getMaxAmbigCodeWoSetId(atom2['comp_id'], atom2['atom_id'])
                        if ambig_code2 == 0:
                            ambig_code2 = None
                    if len(self.atomSelectionSet[2]) > 1:
                        ambig_code3 = self.csStat.getMaxAmbigCodeWoSetId(atom3['comp_id'], atom3['atom_id'])
                        if ambig_code3 == 0:
                            ambig_code3 = None
                    if len(self.atomSelectionSet[3]) > 1:
                        ambig_code4 = self.csStat.getMaxAmbigCodeWoSetId(atom4['comp_id'], atom4['atom_id'])
                        if ambig_code4 == 0:
                            ambig_code4 = None
                else:
                    atom1 = atom2 = atom3 = atom4 = None

                row = getPkRow(self.cur_subtype, sf['id'], sf['index_id'],
                               sf['list_id'], self.entryId, dstFunc,
                               self.authToStarSeq, self.authToOrigSeq, self.offsetHolder,
                               atom1, atom2, atom3, atom4,
                               asis1=asis1, asis2=asis2, asis3=asis3, asis4=asis4,
                               ambig_code1=ambig_code1, ambig_code2=ambig_code2,
                               ambig_code3=ambig_code3, ambig_code4=ambig_code4,
                               details=details)
                sf['loop'].add_data(row)

                row = getPkGenCharRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, 'volume')
                if row is not None:
                    sf['alt_loops'][0].add_data(row)
                row = getPkGenCharRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, 'height')
                if row is not None:
                    sf['alt_loops'][0].add_data(row)

                for idx in range(self.num_of_dim):
                    row = getPkCharRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, idx + 1)
                    sf['alt_loops'][1].add_data(row)
                if has_assignments:
                    for atomSelectionSet, asIsSet in zip(self.atomSelectionSets, self.asIsSets):
                        uniqAtoms = []
                        for idx in range(self.num_of_dim):
                            atom = atomSelectionSet[idx]
                            atom0 = atom[0]
                            if atom0 not in uniqAtoms:
                                asis = asIsSet[idx]
                                ambig_code = None
                                if len(atom) > 1:
                                    ambig_code = self.csStat.getMaxAmbigCodeWoSetId(atom0['comp_id'], atom0['atom_id'])
                                    if ambig_code == 0:
                                        ambig_code = None
                                row = getPkChemShiftRow(self.cur_subtype, sf['id'], sf['list_id'], self.entryId, dstFunc, idx + 1,
                                                        self.authToStarSeq, self.authToOrigSeq, self.offsetHolder,
                                                        atom0, asis, ambig_code)
                                sf['alt_loops'][2].add_data(row)
                                uniqAtoms.append(atom0)

    def extractPeakAssignment(self, numOfDim: int, string: str, src_index: int, hint: Optional[List[dict]] = None) -> Optional[List[dict]]:
        """ Extract peak assignment from a given string.
        """

        if numOfDim not in (1, 2, 3, 4) or string is None:
            return None

        _str = PEAK_ASSIGNMENT_SEPARATOR_PAT.sub(' ', string.upper()).split()
        lenStr = len(_str)

        segIdLike, resIdLike, resNameLike, atomNameLike, _atomNameLike, __atomNameLike, ___atomNameLike =\
            [False] * lenStr, [False] * lenStr, [False] * lenStr, [False] * lenStr, [False] * lenStr, [False] * lenStr, [False] * lenStr

        segIdSpan, resIdSpan, resNameSpan, atomNameSpan, _atomNameSpan, __atomNameSpan, ___atomNameSpan =\
            [None] * lenStr, [None] * lenStr, [None] * lenStr, [None] * lenStr, [None] * lenStr, [None] * lenStr, [None] * lenStr

        if not self.__hasCoord:
            if self.authAsymIdSet is None:
                self.authAsymIdSet = set()
            if self.compIdSet is None:
                self.compIdSet = self.altCompIdSet = set(monDict3.keys())

        oneLetterCodeSet = []
        if self.polyPeptide and not self.polyDeoxyribonucleotide and not self.polyRibonucleotide:
            oneLetterCodeSet = [getOneLetterCode(compId) for compId in self.compIdSet if len(compId) == 3]
        elif not self.polyPeptide and self.polyDeoxyribonucleotide and not self.polyRibonucleotide:
            oneLetterCodeSet = [getOneLetterCode(compId) for compId in self.compIdSet if len(compId) == 2]
        elif not self.polyPeptide and not self.polyDeoxyribonucleotide and self.polyRibonucleotide:
            oneLetterCodeSet = [getOneLetterCode(compId) for compId in self.compIdSet if len(compId) == 1]
        hasOneLetterCodeSet = len(oneLetterCodeSet) > 0
        ligCompId = ligAtomId = None

        for idx, term in enumerate(_str):
            for segId in self.authAsymIdSet:
                if term.startswith(segId):
                    segIdLike[idx] = True
                    segIdSpan[idx] = (0, len(segId))
                    break

            resIdTest = PEAK_ASSIGNMENT_RESID_PAT.search(term)
            if resIdTest:
                resIdLike[idx] = True
                resIdSpan[idx] = resIdTest.span()

            minIndex = len(term)

            for compId in self.compIdSet:
                if compId in term:
                    resNameLike[idx] = True
                    index = term.index(compId)
                    if index < minIndex:
                        resNameSpan[idx] = (index, index + len(compId))
                        minIndex = index

            if not resNameLike[idx]:
                for compId in self.altCompIdSet:
                    if compId in term:
                        resNameLike[idx] = True
                        index = term.index(compId)
                        if index < minIndex:
                            resNameSpan[idx] = (index, index + len(compId))
                            minIndex = index

            if not resNameLike[idx] and hasOneLetterCodeSet:
                if not any(compId in term for compId in monDict3 if len(compId) == 3):
                    for compId in oneLetterCodeSet:
                        if compId in term:
                            resNameLike[idx] = True
                            index = term.index(compId)
                            if index < minIndex:
                                resNameSpan[idx] = (index, index + len(compId))
                                minIndex = index
                elif resIdLike[idx] and self.hasPolySeq:
                    _compId = next(compId for compId in monDict3 if len(compId) == 3 and compId in term)
                    resId = int(term[resIdSpan[idx][0]:resIdSpan[idx][1]])
                    for ps in self.polySeq:
                        _, _, compId = self.getRealChainSeqId(ps, resId, None)
                        if len(compId) == 3 and compId in monDict3 and _compId[0:2] == compId[0:2]:
                            resNameLike[idx] = True
                            index = term.index(_compId)
                            resNameSpan[idx] = (index, index + len(compId))
                            term = _str[idx] = term.replace(_compId, compId)
                            break

            if resNameLike[idx]:
                compId = term[resNameSpan[idx][0]:resNameSpan[idx][1]]
                if compId in self.compIdSet and compId not in monDict3:
                    ligCompId = compId

                if len(compId) == 1:
                    if resIdLike[idx] and self.hasPolySeq:
                        resId = int(term[resIdSpan[idx][0]:resIdSpan[idx][1]])
                        for ps in self.polySeq:
                            _, _, _compId = self.getRealChainSeqId(ps, resId, None)
                            if _compId is not None and _compId not in monDict3:
                                resNameLike[idx] = False
                                break
                    if resNameLike[idx]:
                        index = resNameSpan[idx][1]
                        if index < len(term):
                            if term[index].isdigit() or term[index] in PEAK_HALF_SPIN_NUCLEUS or term[index] in pseProBeginCode:
                                pass
                            else:
                                resNameLike[idx] = False

            if ligCompId is not None and ligCompId != term:
                _, _, details = self.nefT.get_valid_star_atom_in_xplor(ligCompId, term, leave_unmatched=True)
                if details is None or term[0] in PEAK_HALF_SPIN_NUCLEUS:
                    atomNameLike[idx] = True
                    atomNameSpan[idx] = (0, len(term) + 1)
                    ligAtomId = term

            for elem in PEAK_HALF_SPIN_NUCLEUS:
                if len(elem) == 1 and ligAtomId is None:
                    if elem in term:
                        index = term.rindex(elem)
                        atomId = term[index:len(term)]
                        if index - 1 >= 0 and term[index - 1] in PEAK_HALF_SPIN_NUCLEUS:
                            continue
                        if atomId[0] in ('Q', 'M') and index + 1 < len(term) and term[index + 1].isdigit():
                            continue
                        if atomId.startswith('MET') and ((index + 3 < len(term) and term[index + 3].isdigit()
                                                         or (index + 4 < len(term) and term[index + 4].isdigit()))):
                            continue
                        if resNameLike[idx]:
                            compId = term[resNameSpan[idx][0]:resNameSpan[idx][1]]
                            if len(compId) == 1 and hasOneLetterCodeSet:
                                compId = next(k for k, v in monDict3.items() if k in self.compIdSet and v == compId)
                                _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, atomId, leave_unmatched=True)
                                if details is None:
                                    atomNameLike[idx] = True
                                    atomNameSpan[idx] = (index, len(term))
                                    if resNameSpan[idx][0] == atomNameSpan[idx][0]:
                                        resNameLike[idx] = False
                                    break
                                _atomId = translateToStdAtomName(atomId, compId, ccU=self.ccU)
                                _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, _atomId, leave_unmatched=True)
                                if details is None:
                                    atomNameLike[idx] = True
                                    atomNameSpan[idx] = (index, len(term))
                                    if resNameSpan[idx][0] == atomNameSpan[idx][0]:
                                        resNameLike[idx] = False
                                    break
                        for compId in self.compIdSet:
                            _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, atomId, leave_unmatched=True)
                            if details is None:
                                atomNameLike[idx] = True
                                atomNameSpan[idx] = (index, len(term))
                                break
                            _atomId = translateToStdAtomName(atomId, compId, ccU=self.ccU)
                            _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, _atomId, leave_unmatched=True)
                            if details is None:
                                atomNameLike[idx] = True
                                atomNameSpan[idx] = (index, len(term))
                                break
                        if atomNameLike[idx]:
                            break

            if atomNameLike[idx]:
                _term = term[0:atomNameSpan[idx][0]]
                for elem in PEAK_HALF_SPIN_NUCLEUS:
                    if len(elem) == 1 and ligAtomId is None:
                        if elem in _term:
                            index = _term.rindex(elem)
                            atomId = _term[index:len(_term)]
                            if index - 1 >= 0 and _term[index - 1] in PEAK_HALF_SPIN_NUCLEUS:
                                continue
                            if atomId[0] in ('Q', 'M') and index + 1 < len(_term) and _term[index + 1].isdigit():
                                continue
                            if atomId.startswith('MET') and ((index + 3 < len(_term) and _term[index + 3].isdigit()
                                                              or (index + 4 < len(_term) and _term[index + 4].isdigit()))):
                                continue
                            if len(_term) == atomNameSpan[idx][0]:
                                continue
                            if resNameLike[idx]:
                                compId = term[resNameSpan[idx][0]:resNameSpan[idx][1]]
                                if len(compId) == 1 and hasOneLetterCodeSet:
                                    compId = next(k for k, v in monDict3.items() if k in self.compIdSet and v == compId)
                                    _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, atomId, leave_unmatched=True)
                                    if details is None:
                                        _atomNameLike[idx] = True
                                        _atomNameSpan[idx] = (index, len(_term))
                                        if resNameSpan[idx][0] == _atomNameSpan[idx][0]:
                                            resNameLike[idx] = False
                                        break
                                    _atomId = translateToStdAtomName(atomId, compId, ccU=self.ccU)
                                    _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, _atomId, leave_unmatched=True)
                                    if details is None:
                                        _atomNameLike[idx] = True
                                        _atomNameSpan[idx] = (index, len(_term))
                                        if resNameSpan[idx][0] == _atomNameSpan[idx][0]:
                                            resNameLike[idx] = False
                                        break
                            for compId in self.compIdSet:
                                _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, atomId, leave_unmatched=True)
                                if details is None:
                                    _atomNameLike[idx] = True
                                    _atomNameSpan[idx] = (index, len(_term))
                                    break
                                _atomId = translateToStdAtomName(atomId, compId, ccU=self.ccU)
                                _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, _atomId, leave_unmatched=True)
                                if details is None:
                                    _atomNameLike[idx] = True
                                    _atomNameSpan[idx] = (index, len(_term))
                                    break
                            if _atomNameLike[idx]:
                                break

            if numOfDim >= 3 and _atomNameLike[idx]:
                __term = term[0:_atomNameSpan[idx][0]]
                for elem in PEAK_HALF_SPIN_NUCLEUS:
                    if len(elem) == 1 and ligAtomId is None:
                        if elem in __term:
                            index = __term.rindex(elem)
                            atomId = __term[index:len(__term)]
                            if index - 1 >= 0 and __term[index - 1] in PEAK_HALF_SPIN_NUCLEUS:
                                continue
                            if atomId[0] in ('Q', 'M') and index + 1 < len(__term) and __term[index + 1].isdigit():
                                continue
                            if atomId.startswith('MET') and ((index + 3 < len(__term) and __term[index + 3].isdigit()
                                                              or (index + 4 < len(__term) and __term[index + 4].isdigit()))):
                                continue
                            if len(__term) == _atomNameSpan[idx][0]:
                                continue
                            if resNameLike[idx]:
                                compId = term[resNameSpan[idx][0]:resNameSpan[idx][1]]
                                if len(compId) == 1 and hasOneLetterCodeSet:
                                    compId = next(k for k, v in monDict3.items() if k in self.compIdSet and v == compId)
                                    _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, atomId, leave_unmatched=True)
                                    if details is None:
                                        __atomNameLike[idx] = True
                                        __atomNameSpan[idx] = (index, len(__term))
                                        if resNameSpan[idx][0] == __atomNameSpan[idx][0]:
                                            resNameLike[idx] = False
                                        break
                                    _atomId = translateToStdAtomName(atomId, compId, ccU=self.ccU)
                                    _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, _atomId, leave_unmatched=True)
                                    if details is None:
                                        __atomNameLike[idx] = True
                                        __atomNameSpan[idx] = (index, len(__term))
                                        if resNameSpan[idx][0] == __atomNameSpan[idx][0]:
                                            resNameLike[idx] = False
                                        break
                            for compId in self.compIdSet:
                                _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, atomId, leave_unmatched=True)
                                if details is None:
                                    __atomNameLike[idx] = True
                                    __atomNameSpan[idx] = (index, len(__term))
                                    break
                                _atomId = translateToStdAtomName(atomId, compId, ccU=self.ccU)
                                _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, _atomId, leave_unmatched=True)
                                if details is None:
                                    __atomNameLike[idx] = True
                                    __atomNameSpan[idx] = (index, len(__term))
                                    break
                            if __atomNameLike[idx]:
                                break

            if numOfDim >= 4 and __atomNameLike[idx]:
                ___term = term[0:__atomNameSpan[idx][0]]
                for elem in PEAK_HALF_SPIN_NUCLEUS:
                    if len(elem) == 1 and ligAtomId is None:
                        if elem in ___term:
                            index = ___term.rindex(elem)
                            atomId = ___term[index:len(___term)]
                            if index - 1 >= 0 and ___term[index - 1] in PEAK_HALF_SPIN_NUCLEUS:
                                continue
                            if atomId[0] in ('Q', 'M') and index + 1 < len(___term) and ___term[index + 1].isdigit():
                                continue
                            if atomId.startswith('MET') and ((index + 3 < len(___term) and ___term[index + 3].isdigit()
                                                              or (index + 4 < len(___term) and ___term[index + 4].isdigit()))):
                                continue
                            if len(___term) == __atomNameSpan[idx][0]:
                                continue
                            if resNameLike[idx]:
                                compId = term[resNameSpan[idx][0]:resNameSpan[idx][1]]
                                if len(compId) == 1 and hasOneLetterCodeSet:
                                    compId = next(k for k, v in monDict3.items() if k in self.compIdSet and v == compId)
                                    _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, atomId, leave_unmatched=True)
                                    if details is None:
                                        ___atomNameLike[idx] = True
                                        ___atomNameSpan[idx] = (index, len(___term))
                                        if resNameSpan[idx][0] == ___atomNameSpan[idx][0]:
                                            resNameLike[idx] = False
                                        break
                                    _atomId = translateToStdAtomName(atomId, compId, ccU=self.ccU)
                                    _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, _atomId, leave_unmatched=True)
                                    if details is None:
                                        ___atomNameLike[idx] = True
                                        ___atomNameSpan[idx] = (index, len(___term))
                                        if resNameSpan[idx][0] == ___atomNameSpan[idx][0]:
                                            resNameLike[idx] = False
                                        break
                            for compId in self.compIdSet:
                                _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, atomId, leave_unmatched=True)
                                if details is None:
                                    ___atomNameLike[idx] = True
                                    ___atomNameSpan[idx] = (index, len(___term))
                                    break
                                _atomId = translateToStdAtomName(atomId, compId, ccU=self.ccU)
                                _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, _atomId, leave_unmatched=True)
                                if details is None:
                                    ___atomNameLike[idx] = True
                                    ___atomNameSpan[idx] = (index, len(___term))
                                    break
                            if ___atomNameLike[idx]:
                                break

            if _atomNameLike[idx] and atomNameLike[idx]:
                concat = False
                if _atomNameSpan[idx][1] == atomNameSpan[idx][0]:
                    atomId = term[_atomNameSpan[idx][0]:atomNameSpan[idx][1]]
                    if resNameLike[idx]:
                        compId = term[resNameSpan[idx][0]:resNameSpan[idx][1]]
                        resId = term[resIdSpan[idx][0]:resIdSpan[idx][1]] if resIdLike[idx] else '.'
                        if len(compId) == 1 and hasOneLetterCodeSet:
                            compId = next(k for k, v in monDict3.items() if k in self.compIdSet and v == compId)
                            _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, atomId, leave_unmatched=True)
                            if details is None:
                                _atomNameLike[idx] = False
                                atomNameSpan[idx] = (_atomNameSpan[idx][0], atomNameSpan[idx][1])
                                if resNameSpan[idx][0] == atomNameSpan[idx][0]:
                                    resNameLike[idx] = False
                                concat = True
                            else:
                                _atomId = translateToStdAtomName(atomId, compId, ccU=self.ccU)
                                _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, _atomId, leave_unmatched=True)
                                if details is None:
                                    _atomNameLike[idx] = False
                                    atomNameSpan[idx] = (_atomNameSpan[idx][0], atomNameSpan[idx][1])
                                    if resNameSpan[idx][0] == atomNameSpan[idx][0]:
                                        resNameLike[idx] = False
                                    concat = True
                            if details is not None and numOfDim == 1:
                                _atomNameLike[idx] = False
                                for shift in range(_atomNameSpan[idx][0], atomNameSpan[idx][1]):
                                    _atomId = term[_atomNameSpan[idx][0] + shift:atomNameSpan[idx][1]]
                                    if len(_atomId) == 0:
                                        break
                                    if _atomId[0] == resId[0]:
                                        continue
                                    _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, _atomId, leave_unmatched=True)
                                    if details is None:
                                        _atomNameSpan[idx] = (_atomNameSpan[idx][0] + shift, len(_atomId))
                                        atomNameSpan[idx] = (_atomNameSpan[idx][0], atomNameSpan[idx][1])
                                        concat = True
                                        break
                                    __atomId = translateToStdAtomName(_atomId, compId, ccU=self.ccU)
                                    _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, __atomId, leave_unmatched=True)
                                    if details is None:
                                        _atomNameSpan[idx] = (_atomNameSpan[idx][0] + shift, len(_atomId))
                                        atomNameSpan[idx] = (_atomNameSpan[idx][0], atomNameSpan[idx][1])
                                        concat = True
                                        break
                        else:
                            _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, atomId, leave_unmatched=True)
                            if details is None:
                                _atomNameLike[idx] = False
                                atomNameSpan[idx] = (_atomNameSpan[idx][0], atomNameSpan[idx][1])
                                concat = True
                            else:
                                _atomId = translateToStdAtomName(atomId, compId, ccU=self.ccU)
                                _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, _atomId, leave_unmatched=True)
                                if details is None:
                                    _atomNameLike[idx] = False
                                    atomNameSpan[idx] = (_atomNameSpan[idx][0], atomNameSpan[idx][1])
                                    concat = True
                            if details is not None and numOfDim == 1:
                                _atomNameLike[idx] = False
                                for shift in range(_atomNameSpan[idx][0], atomNameSpan[idx][1]):
                                    _atomId = term[_atomNameSpan[idx][0] + shift:atomNameSpan[idx][1]]
                                    if len(_atomId) == 0:
                                        break
                                    if _atomId[0] == resId[0]:
                                        continue
                                    _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, _atomId, leave_unmatched=True)
                                    if details is None:
                                        _atomNameSpan[idx] = (_atomNameSpan[idx][0] + shift, len(_atomId))
                                        atomNameSpan[idx] = (_atomNameSpan[idx][0], atomNameSpan[idx][1])
                                        concat = True
                                        break
                                    __atomId = translateToStdAtomName(_atomId, compId, ccU=self.ccU)
                                    _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, __atomId, leave_unmatched=True)
                                    if details is None:
                                        _atomNameSpan[idx] = (_atomNameSpan[idx][0] + shift, len(_atomId))
                                        atomNameSpan[idx] = (_atomNameSpan[idx][0], atomNameSpan[idx][1])
                                        concat = True
                                        break
                    if not concat:
                        for compId in self.compIdSet:
                            _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, atomId, leave_unmatched=True)
                            if details is None:
                                _atomNameLike[idx] = False
                                atomNameSpan[idx] = (_atomNameSpan[idx][0], atomNameSpan[idx][1])
                                break
                            _atomId = translateToStdAtomName(atomId, compId, ccU=self.ccU)
                            _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, _atomId, leave_unmatched=True)
                            if details is None:
                                _atomNameLike[idx] = False
                                atomNameSpan[idx] = (_atomNameSpan[idx][0], atomNameSpan[idx][1])
                                break

            if __atomNameLike[idx] and _atomNameLike[idx] and atomNameLike[idx]:
                concat = False
                if __atomNameSpan[idx][1] == _atomNameSpan[idx][0] and _atomNameSpan[idx][1] == atomNameSpan[idx][0]:
                    atomId = term[__atomNameSpan[idx][0]:atomNameSpan[idx][1]]
                    if resNameLike[idx]:
                        compId = term[resNameSpan[idx][0]:resNameSpan[idx][1]]
                        if len(compId) == 1 and hasOneLetterCodeSet:
                            compId = next(k for k, v in monDict3.items() if k in self.compIdSet and v == compId)
                            _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, atomId, leave_unmatched=True)
                            if details is None:
                                __atomNameLike[idx] = _atomNameLike[idx] = False
                                atomNameSpan[idx] = (__atomNameSpan[idx][0], atomNameSpan[idx][1])
                                if resNameSpan[idx][0] == atomNameSpan[idx][0]:
                                    resNameLike[idx] = False
                                concat = True
                            else:
                                _atomId = translateToStdAtomName(atomId, compId, ccU=self.ccU)
                                _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, _atomId, leave_unmatched=True)
                                if details is None:
                                    __atomNameLike[idx] = _atomNameLike[idx] = False
                                    atomNameSpan[idx] = (__atomNameSpan[idx][0], atomNameSpan[idx][1])
                                    if resNameSpan[idx][0] == atomNameSpan[idx][0]:
                                        resNameLike[idx] = False
                                    concat = True

                    if not concat:
                        for compId in self.compIdSet:
                            _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, atomId, leave_unmatched=True)
                            if details is None:
                                __atomNameLike[idx] = _atomNameLike[idx] = False
                                atomNameSpan[idx] = (__atomNameSpan[idx][0], atomNameSpan[idx][1])
                                break
                            _atomId = translateToStdAtomName(atomId, compId, ccU=self.ccU)
                            _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, _atomId, leave_unmatched=True)
                            if details is None:
                                __atomNameLike[idx] = _atomNameLike[idx] = False
                                atomNameSpan[idx] = (__atomNameSpan[idx][0], atomNameSpan[idx][1])
                                break

            if ___atomNameLike[idx] and __atomNameLike[idx] and _atomNameLike[idx] and atomNameLike[idx]:
                concat = False
                if ___atomNameSpan[idx][1] == __atomNameSpan[idx][0] and __atomNameSpan[idx][1] == _atomNameSpan[idx][0]\
                   and _atomNameSpan[idx][1] == atomNameSpan[idx][0]:
                    atomId = term[___atomNameSpan[idx][0]:atomNameSpan[idx][1]]
                    if resNameLike[idx]:
                        compId = term[resNameSpan[idx][0]:resNameSpan[idx][1]]
                        if len(compId) == 1 and hasOneLetterCodeSet:
                            compId = next(k for k, v in monDict3.items() if k in self.compIdSet and v == compId)
                            _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, atomId, leave_unmatched=True)
                            if details is None:
                                ___atomNameLike[idx] = __atomNameLike[idx] = _atomNameLike[idx] = False
                                atomNameSpan[idx] = (___atomNameSpan[idx][0], atomNameSpan[idx][1])
                                if resNameSpan[idx][0] == atomNameSpan[idx][0]:
                                    resNameLike[idx] = False
                                concat = True
                            else:
                                _atomId = translateToStdAtomName(atomId, compId, ccU=self.ccU)
                                _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, _atomId, leave_unmatched=True)
                                if details is None:
                                    ___atomNameLike[idx] = __atomNameLike[idx] = _atomNameLike[idx] = False
                                    atomNameSpan[idx] = (___atomNameSpan[idx][0], atomNameSpan[idx][1])
                                    if resNameSpan[idx][0] == atomNameSpan[idx][0]:
                                        resNameLike[idx] = False
                                    concat = True
                    if not concat:
                        for compId in self.compIdSet:
                            _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, atomId, leave_unmatched=True)
                            if details is None:
                                ___atomNameLike[idx] = __atomNameLike[idx] = _atomNameLike[idx] = False
                                atomNameSpan[idx] = (___atomNameSpan[idx][0], atomNameSpan[idx][1])
                                break
                            _atomId = translateToStdAtomName(atomId, compId, ccU=self.ccU)
                            _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, _atomId, leave_unmatched=True)
                            if details is None:
                                ___atomNameLike[idx] = __atomNameLike[idx] = _atomNameLike[idx] = False
                                atomNameSpan[idx] = (___atomNameSpan[idx][0], atomNameSpan[idx][1])
                                break

            if __atomNameLike[idx] and _atomNameLike[idx]:
                concat = False
                if __atomNameSpan[idx][1] == _atomNameSpan[idx][0]:
                    atomId = term[__atomNameSpan[idx][0]:_atomNameSpan[idx][1]]
                    if resNameLike[idx]:
                        compId = term[resNameSpan[idx][0]:resNameSpan[idx][1]]
                        if len(compId) == 1 and hasOneLetterCodeSet:
                            compId = next(k for k, v in monDict3.items() if k in self.compIdSet and v == compId)
                            _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, atomId, leave_unmatched=True)
                            if details is None:
                                __atomNameLike[idx] = False
                                _atomNameSpan[idx] = (__atomNameSpan[idx][0], _atomNameSpan[idx][1])
                                if resNameSpan[idx][0] == _atomNameSpan[idx][0]:
                                    resNameLike[idx] = False
                                concat = True
                            else:
                                _atomId = translateToStdAtomName(atomId, compId, ccU=self.ccU)
                                _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, _atomId, leave_unmatched=True)
                                if details is None:
                                    __atomNameLike[idx] = False
                                    _atomNameSpan[idx] = (__atomNameSpan[idx][0], _atomNameSpan[idx][1])
                                    if resNameSpan[idx][0] == _atomNameSpan[idx][0]:
                                        resNameLike[idx] = False
                                    concat = True
                    if not concat:
                        for compId in self.compIdSet:
                            _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, atomId, leave_unmatched=True)
                            if details is None:
                                __atomNameLike[idx] = False
                                _atomNameSpan[idx] = (__atomNameSpan[idx][0], _atomNameSpan[idx][1])
                                break
                            _atomId = translateToStdAtomName(atomId, compId, ccU=self.ccU)
                            _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, _atomId, leave_unmatched=True)
                            if details is None:
                                __atomNameLike[idx] = False
                                _atomNameSpan[idx] = (__atomNameSpan[idx][0], _atomNameSpan[idx][1])
                                break

            if ___atomNameLike[idx] and __atomNameLike[idx] and _atomNameLike[idx]:
                concat = False
                if ___atomNameSpan[idx][1] == __atomNameSpan[idx][0] and __atomNameSpan[idx][1] == _atomNameSpan[idx][0]:
                    atomId = term[___atomNameSpan[idx][0]:_atomNameSpan[idx][1]]
                    if resNameLike[idx]:
                        compId = term[resNameSpan[idx][0]:resNameSpan[idx][1]]
                        if len(compId) == 1 and hasOneLetterCodeSet:
                            compId = next(k for k, v in monDict3.items() if k in self.compIdSet and v == compId)
                            _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, atomId, leave_unmatched=True)
                            if details is None:
                                ___atomNameLike[idx] = __atomNameLike[idx] = False
                                _atomNameSpan[idx] = (___atomNameSpan[idx][0], _atomNameSpan[idx][1])
                                if resNameSpan[idx][0] == _atomNameSpan[idx][0]:
                                    resNameLike[idx] = False
                                concat = True
                            else:
                                _atomId = translateToStdAtomName(atomId, compId, ccU=self.ccU)
                                _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, _atomId, leave_unmatched=True)
                                if details is None:
                                    ___atomNameLike[idx] = __atomNameLike[idx] = False
                                    _atomNameSpan[idx] = (___atomNameSpan[idx][0], _atomNameSpan[idx][1])
                                    if resNameSpan[idx][0] == _atomNameSpan[idx][0]:
                                        resNameLike[idx] = False
                                    concat = True
                    if not concat:
                        for compId in self.compIdSet:
                            _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, atomId, leave_unmatched=True)
                            if details is None:
                                ___atomNameLike[idx] = __atomNameLike[idx] = False
                                _atomNameSpan[idx] = (___atomNameSpan[idx][0], _atomNameSpan[idx][1])
                                break
                            _atomId = translateToStdAtomName(atomId, compId, ccU=self.ccU)
                            _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, _atomId, leave_unmatched=True)
                            if details is None:
                                ___atomNameLike[idx] = __atomNameLike[idx] = False
                                _atomNameSpan[idx] = (___atomNameSpan[idx][0], _atomNameSpan[idx][1])
                                break

            if ___atomNameLike[idx] and __atomNameLike[idx]:
                concat = False
                if ___atomNameSpan[idx][1] == __atomNameSpan[idx][0]:
                    atomId = term[___atomNameSpan[idx][0]:__atomNameSpan[idx][1]]
                    if resNameLike[idx]:
                        compId = term[resNameSpan[idx][0]:resNameSpan[idx][1]]
                        if len(compId) == 1 and hasOneLetterCodeSet:
                            compId = next(k for k, v in monDict3.items() if k in self.compIdSet and v == compId)
                            _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, atomId, leave_unmatched=True)
                            if details is None:
                                ___atomNameLike[idx] = False
                                __atomNameSpan[idx] = (___atomNameSpan[idx][0], __atomNameSpan[idx][1])
                                if resNameSpan[idx][0] == __atomNameSpan[idx][0]:
                                    resNameLike[idx] = False
                                concat = True
                            else:
                                _atomId = translateToStdAtomName(atomId, compId, ccU=self.ccU)
                                _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, _atomId, leave_unmatched=True)
                                if details is None:
                                    ___atomNameLike[idx] = False
                                    __atomNameSpan[idx] = (___atomNameSpan[idx][0], __atomNameSpan[idx][1])
                                    if resNameSpan[idx][0] == __atomNameSpan[idx][0]:
                                        resNameLike[idx] = False
                                    concat = True
                    if not concat:
                        for compId in self.compIdSet:
                            _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, atomId, leave_unmatched=True)
                            if details is None:
                                ___atomNameLike[idx] = False
                                __atomNameSpan[idx] = (___atomNameSpan[idx][0], __atomNameSpan[idx][1])
                                break
                            _atomId = translateToStdAtomName(atomId, compId, ccU=self.ccU)
                            _, _, details = self.nefT.get_valid_star_atom_in_xplor(compId, _atomId, leave_unmatched=True)
                            if details is None:
                                ___atomNameLike[idx] = False
                                __atomNameSpan[idx] = (___atomNameSpan[idx][0], __atomNameSpan[idx][1])
                                break

            if idx == 0 and atomNameLike[0] and not _atomNameLike[0] and self.hasNonPoly:
                if not segIdLike[0] and not resIdLike[0] and not resNameLike[0]:
                    ligands = 0
                    for np in self.nonPoly:
                        if 'alt_comp_id' in np and _str[0][0] == np['alt_comp_id'][0][0]:
                            ligands += 1
                    if ligands == 1:
                        for np in self.nonPoly:
                            if 'alt_comp_id' in np and _str[0][0] == np['alt_comp_id'][0][0]:
                                _string = f"{np['auth_chain_id']} {np['auth_seq_id'][0]} {np['comp_id'][0]}{string[atomNameSpan[0][1]:]}"
                                return self.extractPeakAssignment(numOfDim, _string, src_index, hint)

                if _str[0][0] == 'X' and term[atomNameSpan[idx][0]] != 'X' and len(self.nonPoly) == 1:
                    np = self.nonPoly[0]
                    _string = f"{np['auth_chain_id']} {np['auth_seq_id'][0]} {np['comp_id'][0]}{string[atomNameSpan[0][0]:]}"
                    return self.extractPeakAssignment(numOfDim, _string, src_index, hint)

            if self.ass_expr_debug:
                print(f'{idx} {term!r} segid:{segIdLike[idx]} {term[segIdSpan[idx][0]:segIdSpan[idx][1]] if segIdLike[idx] else ""}, '
                      f'resid:{resIdLike[idx]} {term[resIdSpan[idx][0]:resIdSpan[idx][1]] if resIdLike[idx] else ""}, '
                      f'resname:{resNameLike[idx]} {term[resNameSpan[idx][0]:resNameSpan[idx][1]] if resNameLike[idx] else ""}, '
                      f'atomname:{atomNameLike[idx]} {term[atomNameSpan[idx][0]:atomNameSpan[idx][1]] if atomNameLike[idx] else ""}, '
                      f'_atomname:{_atomNameLike[idx]} {term[_atomNameSpan[idx][0]:_atomNameSpan[idx][1]] if _atomNameLike[idx] else ""}, '
                      f'__atomname:{__atomNameLike[idx]} {term[__atomNameSpan[idx][0]:__atomNameSpan[idx][1]] if __atomNameLike[idx] else ""}, '
                      f'___atomname:{___atomNameLike[idx]} {term[___atomNameSpan[idx][0]:___atomNameSpan[idx][1]] if ___atomNameLike[idx] else ""}')

        atomNameCount = 0
        for idx in range(lenStr):
            if atomNameLike[idx]:
                atomNameCount += 1
            if _atomNameLike[idx]:
                atomNameCount += 1
            if __atomNameLike[idx]:
                atomNameCount += 1
            if ___atomNameLike[idx]:
                atomNameCount += 1

        if atomNameCount < numOfDim:
            return None

        if atomNameCount > numOfDim > 1:
            atomNameCount = 0
            ignoreBefore = False
            for idx in range(lenStr - 1, 0, -1):
                if ignoreBefore:
                    atomNameLike[idx] = _atomNameLike[idx] = __atomNameLike[idx] = ___atomNameLike[idx] = False
                else:
                    if atomNameLike[idx]:
                        atomNameCount += 1
                    if _atomNameLike[idx]:
                        atomNameCount += 1
                    if __atomNameLike[idx]:
                        atomNameCount += 1
                    if ___atomNameLike[idx]:
                        atomNameCount += 1
                    if atomNameCount >= numOfDim:
                        ignoreBefore = True

        hasResName = False
        for idx in range(lenStr):
            if ___atomNameLike[idx]:
                if resNameLike[idx]:
                    if not hasResName and resNameSpan[idx][0] < ___atomNameSpan[idx][0] and resNameSpan[idx][1] >= ___atomNameSpan[idx][1]:
                        ___atomNameLike[idx] = False
                    elif resNameSpan[idx][1] > ___atomNameSpan[idx][0]:
                        resNameLike[idx] = False
                if resIdLike[idx]:
                    if resIdSpan[idx][1] > ___atomNameSpan[idx][0]:
                        resIdLike[idx] = False
                if segIdLike[idx]:
                    if segIdSpan[idx][1] > ___atomNameSpan[idx][0]:
                        segIdLike[idx] = False

            elif __atomNameLike[idx]:
                if resNameLike[idx]:
                    if not hasResName and resNameSpan[idx][0] < __atomNameSpan[idx][0] and resNameSpan[idx][1] >= __atomNameSpan[idx][1]:
                        __atomNameLike[idx] = False
                    elif resNameSpan[idx][1] > __atomNameSpan[idx][0]:
                        resNameLike[idx] = False
                if resIdLike[idx]:
                    if resIdSpan[idx][1] > __atomNameSpan[idx][0]:
                        resIdLike[idx] = False
                if segIdLike[idx]:
                    if segIdSpan[idx][1] > __atomNameSpan[idx][0]:
                        segIdLike[idx] = False

            elif _atomNameLike[idx]:
                if resNameLike[idx]:
                    if not hasResName and resNameSpan[idx][0] < _atomNameSpan[idx][0] and resNameSpan[idx][1] >= _atomNameSpan[idx][1]:
                        _atomNameLike[idx] = False
                    elif resNameSpan[idx][1] > _atomNameSpan[idx][0]:
                        resNameLike[idx] = False
                if resIdLike[idx]:
                    if resIdSpan[idx][1] > _atomNameSpan[idx][0]:
                        resIdLike[idx] = False
                if segIdLike[idx]:
                    if segIdSpan[idx][1] > _atomNameSpan[idx][0]:
                        segIdLike[idx] = False

            elif atomNameLike[idx]:
                if resNameLike[idx]:
                    if not hasResName and resNameSpan[idx][0] < atomNameSpan[idx][0] and resNameSpan[idx][1] >= atomNameSpan[idx][1]:
                        atomNameLike[idx] = False
                    elif resNameSpan[idx][1] > atomNameSpan[idx][0]:
                        resNameLike[idx] = False
                if resIdLike[idx]:
                    if resIdSpan[idx][1] > atomNameSpan[idx][0]:
                        resIdLike[idx] = False
                if segIdLike[idx]:
                    if segIdSpan[idx][1] > atomNameSpan[idx][0]:
                        segIdLike[idx] = False

            if resNameLike[idx]:
                hasResName = True
                if segIdLike[idx]:
                    if segIdSpan[idx][1] > resNameSpan[idx][0]:
                        if numOfDim > 1 or not any(resNameLike[_idx] for _idx in range(idx + 1, lenStr))\
                           or (resIdSpan[idx] and segIdSpan[idx][1] == resIdSpan[idx][0]):
                            segIdLike[idx] = False
                        else:
                            resNameLike[idx] = False

            if resIdLike[idx]:
                if atomNameLike[idx]:
                    if resIdSpan[idx][1] > atomNameSpan[idx][0]:
                        resIdLike[idx] = False

            if self.ass_expr_debug:
                print(f' -> {idx} segid:{segIdLike[idx]}, resid:{resIdLike[idx]}, resname:{resNameLike[idx]}, '
                      f'atomname:{atomNameLike[idx]}, _atomname:{_atomNameLike[idx]}, __atomname:{__atomNameLike[idx]}, ___atomname:{___atomNameLike[idx]}')

        resIdCount = 0
        for idx in range(lenStr):
            if resIdLike[idx]:
                resIdCount += 1

        _resId = [h['seq_id'] for h in hint] if hint is not None else None
        if resIdCount == 0:
            if _resId is None:
                return None

        _resNameDict = [{h['auth_seq_id']: h['comp_id']} for h in hint] if hint is not None else None

        resIdLater = resIdCount == numOfDim
        if resIdLater:
            atomNameCount = 0
            for idx in range(lenStr):
                if atomNameLike[idx]:
                    atomNameCount += 1
            resIdLater = atomNameCount == numOfDim
            if resIdLater:
                anyResId = False
                for idx in range(lenStr):
                    if resIdLike[idx]:
                        anyResId = True
                    if atomNameLike[idx]:
                        if anyResId:
                            resIdLater = False
                        break

        if self.ass_expr_debug:
            print(f'num_of_dim: {numOfDim}, resid_count: {resIdCount}, resid_later:{resIdLater}')

        ret = []

        segId = resId = resName = atomName = _segId_ = _resId_ = authResId = None
        dimId = 1
        for idx, term in enumerate(_str):
            if segIdLike[idx]:
                segId = term[segIdSpan[idx][0]:segIdSpan[idx][1]]
                if _segId_ is not None and segId != _segId_:
                    resId = resName = None
                _segId_ = segId
            if resIdLike[idx]:
                resId = authResId = int(term[resIdSpan[idx][0]:resIdSpan[idx][1]])
                if _resId_ is not None and resId != _resId_:
                    resName = None
                _resId_ = resId
            if resNameLike[idx]:
                resName = term[resNameSpan[idx][0]:resNameSpan[idx][1]]
                if len(resName) == 1 and hasOneLetterCodeSet:
                    resName = next(k for k, v in monDict3.items() if k in self.compIdSet and v == resName)
            elif _resNameDict is not None and resName is None and len(ret) < len(_resNameDict)\
                    and _resId is not None and len(ret) < len(_resId) and _resId[len(ret)] in _resNameDict[len(ret)]\
                    and (authResId is None or authResId == _resId[len(ret)]):
                resName = _resNameDict[len(ret)][_resId[len(ret)]]
            if ___atomNameLike[idx]:
                if resIdLater:
                    for _idx, _term in enumerate(_str):
                        if _idx > idx and resIdLike[_idx]:
                            resId = int(_term[resIdSpan[_idx][0]:resIdSpan[_idx][1]])
                            segId = resName = None
                            break
                if resId is None:
                    if _resId is None or len(ret) >= len(_resId):
                        return None
                    resId = _resId[len(ret)]
                atomName = term[___atomNameSpan[idx][0]:___atomNameSpan[idx][1]]
                if self.__hasCoord:
                    if segId is None and resName is None:
                        chainAssign = self.assignCoordPolymerSequenceWithoutCompId(resId, atomName, src_index)
                        if len(chainAssign) > 0:
                            if self.__defaultSegId is None:
                                idx = next((chainAssign.index(a) for a in chainAssign if a[1] == resId), -1)
                            else:
                                idx = next((chainAssign.index(a) for a in chainAssign if a[0] == self.__defaultSegId and a[1] == resId), -1)
                            if idx != -1:
                                if self.__defaultSegId is None:
                                    self.__defaultSegId = chainAssign[idx][0]
                            else:
                                idx = 0
                            segId, _, resName, _ = chainAssign[idx]
                    elif segId is None:
                        chainAssign, _ = self.assignCoordPolymerSequence(self.__defaultSegId,
                                                                         resId, resName, atomName, src_index)
                        if len(chainAssign) > 0:
                            idx = next((chainAssign.index(a) for a in chainAssign if a[2] == resName), -1)
                            if idx != -1:
                                if self.__defaultSegId is None:
                                    self.__defaultSegId = chainAssign[idx][0]
                            else:
                                idx = 0
                            segId = chainAssign[idx][0]
                    elif resName is None:
                        chainAssign = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(segId, resId, atomName, src_index)
                        if len(chainAssign) > 0:
                            idx = next((chainAssign.index(a) for a in chainAssign if a[1] == resId), 0)
                            resName = chainAssign[idx][2]
                    _, _, details = self.nefT.get_valid_star_atom_in_xplor(resName, atomName, leave_unmatched=True)
                    if details is not None:
                        atomName = translateToStdAtomName(atomName, resName, ccU=self.ccU)
                    ret.append({'dim_id': dimId, 'chain_id': segId, 'seq_id': resId, 'auth_seq_id': authResId, 'comp_id': resName, 'atom_id': atomName})
                else:
                    ass = {'dim': dimId, 'atom_id': atomName}
                    if segId is not None:
                        ass['chain_id'] = segId
                    if resId is not None:
                        ass['seq_id'] = resId
                    if resName is not None:
                        ass['comp_id'] = resName
                    ret.append(ass)
                dimId += 1
            if __atomNameLike[idx]:
                if resIdLater:
                    for _idx, _term in enumerate(_str):
                        if _idx > idx and resIdLike[_idx]:
                            resId = int(_term[resIdSpan[_idx][0]:resIdSpan[_idx][1]])
                            segId = resName = None
                            break
                if resId is None:
                    if _resId is None or len(ret) >= len(_resId):
                        return None
                    resId = _resId[len(ret)]
                atomName = term[__atomNameSpan[idx][0]:__atomNameSpan[idx][1]]
                if self.__hasCoord:
                    if segId is None and resName is None:
                        chainAssign = self.assignCoordPolymerSequenceWithoutCompId(resId, atomName, src_index)
                        if len(chainAssign) > 0:
                            if self.__defaultSegId is None:
                                idx = next((chainAssign.index(a) for a in chainAssign if a[1] == resId), -1)
                            else:
                                idx = next((chainAssign.index(a) for a in chainAssign if a[0] == self.__defaultSegId and a[1] == resId), -1)
                            if idx != -1:
                                if self.__defaultSegId is None:
                                    self.__defaultSegId = chainAssign[idx][0]
                            else:
                                idx = 0
                            segId, _, resName, _ = chainAssign[idx]
                    elif segId is None:
                        chainAssign, _ = self.assignCoordPolymerSequence(self.__defaultSegId,
                                                                         resId, resName, atomName, src_index)
                        if len(chainAssign) > 0:
                            idx = next((chainAssign.index(a) for a in chainAssign if a[2] == resName), -1)
                            if idx != -1:
                                if self.__defaultSegId is None:
                                    self.__defaultSegId = chainAssign[idx][0]
                            else:
                                idx = 0
                            segId = chainAssign[idx][0]
                    elif resName is None:
                        chainAssign = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(segId, resId, atomName, src_index)
                        if len(chainAssign) > 0:
                            idx = next((chainAssign.index(a) for a in chainAssign if a[1] == resId), 0)
                            resName = chainAssign[idx][2]
                    _, _, details = self.nefT.get_valid_star_atom_in_xplor(resName, atomName, leave_unmatched=True)
                    if details is not None:
                        atomName = translateToStdAtomName(atomName, resName, ccU=self.ccU)
                    ret.append({'dim_id': dimId, 'chain_id': segId, 'seq_id': resId, 'auth_seq_id': authResId, 'comp_id': resName, 'atom_id': atomName})
                else:
                    ass = {'dim': dimId, 'atom_id': atomName}
                    if segId is not None:
                        ass['chain_id'] = segId
                    if resId is not None:
                        ass['seq_id'] = resId
                    if resName is not None:
                        ass['comp_id'] = resName
                    ret.append(ass)
                dimId += 1
            if _atomNameLike[idx]:
                if resIdLater:
                    for _idx, _term in enumerate(_str):
                        if _idx > idx and resIdLike[_idx]:
                            resId = int(_term[resIdSpan[_idx][0]:resIdSpan[_idx][1]])
                            segId = resName = None
                            break
                if resId is None:
                    if _resId is None or len(ret) >= len(_resId):
                        return None
                    resId = _resId[len(ret)]
                atomName = term[_atomNameSpan[idx][0]:_atomNameSpan[idx][1]]
                if self.__hasCoord:
                    if segId is None and resName is None:
                        chainAssign = self.assignCoordPolymerSequenceWithoutCompId(resId, atomName, src_index)
                        if len(chainAssign) > 0:
                            if self.__defaultSegId is None:
                                idx = next((chainAssign.index(a) for a in chainAssign if a[1] == resId), -1)
                            else:
                                idx = next((chainAssign.index(a) for a in chainAssign if a[0] == self.__defaultSegId and a[1] == resId), -1)
                            if idx != -1:
                                if self.__defaultSegId is None:
                                    self.__defaultSegId = chainAssign[idx][0]
                            else:
                                idx = 0
                            segId, _, resName, _ = chainAssign[idx]
                    elif segId is None:
                        chainAssign, _ = self.assignCoordPolymerSequence(self.__defaultSegId,
                                                                         resId, resName, atomName, src_index)
                        if len(chainAssign) > 0:
                            idx = next((chainAssign.index(a) for a in chainAssign if a[2] == resName), -1)
                            if idx != -1:
                                if self.__defaultSegId is None:
                                    self.__defaultSegId = chainAssign[idx][0]
                            else:
                                idx = 0
                            segId = chainAssign[idx][0]
                    elif resName is None:
                        chainAssign = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(segId, resId, atomName, src_index)
                        if len(chainAssign) > 0:
                            idx = next((chainAssign.index(a) for a in chainAssign if a[1] == resId), 0)
                            resName = chainAssign[idx][2]
                    _, _, details = self.nefT.get_valid_star_atom_in_xplor(resName, atomName, leave_unmatched=True)
                    if details is not None:
                        atomName = translateToStdAtomName(atomName, resName, ccU=self.ccU)
                    ret.append({'dim_id': dimId, 'chain_id': segId, 'seq_id': resId, 'auth_seq_id': authResId, 'comp_id': resName, 'atom_id': atomName})
                else:
                    ass = {'dim': dimId, 'atom_id': atomName}
                    if segId is not None:
                        ass['chain_id'] = segId
                    if resId is not None:
                        ass['seq_id'] = resId
                    if resName is not None:
                        ass['comp_id'] = resName
                    ret.append(ass)
                dimId += 1
            if atomNameLike[idx]:
                if resIdLater:
                    for _idx, _term in enumerate(_str):
                        if _idx > idx and resIdLike[_idx]:
                            resId = int(_term[resIdSpan[_idx][0]:resIdSpan[_idx][1]])
                            segId = resName = None
                            break
                if resId is None:
                    if _resId is None or len(ret) >= len(_resId):
                        return None
                    resId = _resId[len(ret)]
                atomName = term[atomNameSpan[idx][0]:atomNameSpan[idx][1]]
                if self.__hasCoord:
                    if segId is None and resName is None:
                        chainAssign = self.assignCoordPolymerSequenceWithoutCompId(resId, atomName, src_index)
                        if len(chainAssign) > 0:
                            if self.__defaultSegId is None:
                                idx = next((chainAssign.index(a) for a in chainAssign if a[1] == resId), -1)
                            else:
                                idx = next((chainAssign.index(a) for a in chainAssign if a[0] == self.__defaultSegId and a[1] == resId), -1)
                            if idx != -1:
                                if self.__defaultSegId is None:
                                    self.__defaultSegId = chainAssign[idx][0]
                            else:
                                idx = 0
                            segId, _, resName, _ = chainAssign[idx]
                    elif segId is None:
                        chainAssign, _ = self.assignCoordPolymerSequence(self.__defaultSegId,
                                                                         resId, resName, atomName, src_index)
                        if len(chainAssign) > 0:
                            idx = next((chainAssign.index(a) for a in chainAssign if a[2] == resName), -1)
                            if idx != -1:
                                if self.__defaultSegId is None:
                                    self.__defaultSegId = chainAssign[idx][0]
                            else:
                                idx = 0
                            segId = chainAssign[idx][0]
                    elif resName is None:
                        chainAssign = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(segId, resId, atomName, src_index)
                        if len(chainAssign) > 0:
                            idx = next((chainAssign.index(a) for a in chainAssign if a[1] == resId), 0)
                            resName = chainAssign[idx][2]
                    _, _, details = self.nefT.get_valid_star_atom_in_xplor(resName, atomName, leave_unmatched=True)
                    if details is not None:
                        atomName = translateToStdAtomName(atomName, resName, ccU=self.ccU)
                    ret.append({'dim_id': dimId, 'chain_id': segId, 'seq_id': resId, 'auth_seq_id': authResId, 'comp_id': resName, 'atom_id': atomName})
                else:
                    ass = {'dim': dimId, 'atom_id': atomName}
                    if segId is not None:
                        ass['chain_id'] = segId
                    if resId is not None:
                        ass['seq_id'] = resId
                    if resName is not None:
                        ass['comp_id'] = resName
                    ret.append(ass)
                dimId += 1

        multiple = len(ret) > numOfDim

        if multiple:
            if self.createSfDict__ and self.use_peak_row_format:
                sf = self.getSf()
                sf['peak_row_format'] = self.use_peak_row_format = False

        return ret if len(ret) > 0 else None

    def getRealChainSeqId(self, ps: dict, seqId: int, compId: Optional[str], isPolySeq: bool = True) -> Tuple[str, int, Optional[str]]:
        if compId is not None:
            compId = _compId = translateToStdResName(compId, ccU=self.ccU)
            if len(_compId) == 2 and _compId.startswith('D'):
                _compId = compId[1]
        if not self.__preferAuthSeq:
            seqKey = (ps['auth_chain_id'], seqId)
            if seqKey in self.__labelToAuthSeq:
                _chainId, _seqId = self.__labelToAuthSeq[seqKey]
                if _seqId in ps['auth_seq_id']:
                    return _chainId, _seqId, ps['comp_id'][ps['seq_id'].index(seqId)]
        if seqId in ps['auth_seq_id']:
            if compId is None:
                return ps['auth_chain_id'], seqId, ps['comp_id'][ps['auth_seq_id'].index(seqId)]
            for idx in [_idx for _idx, _seqId in enumerate(ps['auth_seq_id']) if _seqId == seqId]:
                if 'alt_comp_id' in ps and idx < len(ps['alt_comp_id']):
                    if compId in (ps['comp_id'][idx], ps['auth_comp_id'][idx], ps['alt_comp_id'][idx]):
                        return ps['auth_chain_id'], seqId, ps['comp_id'][idx]
                    if compId != _compId and _compId in (ps['comp_id'][idx], ps['auth_comp_id'][idx], ps['alt_comp_id'][idx]):
                        return ps['auth_chain_id'], seqId, ps['comp_id'][idx]
                if compId in (ps['comp_id'][idx], ps['auth_comp_id'][idx])\
                   or (isPolySeq and seqId == 1
                       and ((compId.endswith('-N') and all(c in ps['comp_id'][idx] for c in compId.split('-')[0]))
                            or (ps['comp_id'][idx] == 'PCA' and 'P' == compId[0] and ('GL' in compId or 'N' in compId)))):
                    return ps['auth_chain_id'], seqId, ps['comp_id'][idx]
                if compId != _compId and _compId in (ps['comp_id'][idx], ps['auth_comp_id'][idx]):
                    return ps['auth_chain_id'], seqId, ps['comp_id'][idx]
        if self.reasons is not None and 'extend_seq_scheme' in self.reasons:
            _ps = next((_ps for _ps in self.reasons['extend_seq_scheme'] if _ps['chain_id'] == ps['auth_chain_id']), None)
            if _ps is not None:
                if seqId in _ps['seq_id']:
                    return ps['auth_chain_id'], seqId, _ps['comp_id'][_ps['seq_id'].index(seqId)]
        return ps['auth_chain_id'], seqId, None

    def translateToStdResNameWrapper(self, seqId: int, compId: str, preferNonPoly: bool = False) -> str:
        _compId = compId
        refCompId = None
        for ps in self.polySeq:
            if preferNonPoly:
                continue
            _, _, refCompId = self.getRealChainSeqId(ps, seqId, _compId)
            if refCompId is not None:
                compId = translateToStdResName(_compId, refCompId=refCompId, ccU=self.ccU)
                if compId != _compId and compId in monDict3 and _compId in monDict3:
                    continue
                break
        if refCompId is None and self.hasNonPolySeq:
            for np in self.nonPolySeq:
                _, _, refCompId = self.getRealChainSeqId(np, seqId, _compId, False)
                if refCompId is not None:
                    compId = translateToStdResName(_compId, refCompId=refCompId, ccU=self.ccU)
                    break
        if refCompId is None:
            compId = translateToStdResName(_compId, ccU=self.ccU)
        return compId

    def assignCoordPolymerSequence(self, refChainId: str, seqId: int, compId: str, atomId: str, index: int
                                   ) -> Tuple[List[Tuple[str, int, str, bool]], bool]:
        """ Assign polymer sequences of the coordinates.
        """

        _refChainId = refChainId

        chainAssign = set()
        asis = False

        _seqId = seqId
        _compId = compId

        fixedChainId = fixedSeqId = fixedCompId = None

        preferNonPoly = False

        self.__allow_ext_seq = False

        if self.hasNonPoly:

            resolved = False

            for np in self.nonPoly:
                if 'alt_comp_id' in np and 'alt_auth_seq_id' in np\
                   and compId in np['alt_comp_id'] and seqId in np['alt_auth_seq_id']:
                    npCompId = np['comp_id'][0]
                    npSeqId = np['auth_seq_id'][0]
                    for ps in self.polySeq:
                        if 'ambig_auth_seq_id' in ps and seqId in ps['ambig_auth_seq_id']:
                            psCompId = ps['comp_id'][ps['auth_seq_id'].index(seqId)]
                            _atomId, _, details = self.nefT.get_valid_star_atom_in_xplor(psCompId, atomId, leave_unmatched=True)
                            if details is None:
                                _, _coordAtomSite = self.getCoordAtomSiteOf(ps['auth_chain_id'], seqId, psCompId, cifCheck=self.__hasCoord)
                                if _coordAtomSite is not None and all(_atomId_ in _coordAtomSite['atom_id'] for _atomId_ in _atomId):
                                    compId = _compId = psCompId
                                    resolved = True
                                    break
                            _, _coordAtomSite = self.getCoordAtomSiteOf(np['auth_chain_id'], npSeqId, npCompId, cifCheck=self.__hasCoord)
                            if self.__mrAtomNameMapping is not None:
                                atomId = retrieveAtomIdFromMRMap(self.ccU, self.__mrAtomNameMapping, npSeqId, npCompId, atomId, _coordAtomSite)
                            _atomId, _, details = self.nefT.get_valid_star_atom_in_xplor(npCompId, atomId, leave_unmatched=True)
                            if details is None:
                                if _coordAtomSite is not None and all(_atomId_ in _coordAtomSite['atom_id'] for _atomId_ in _atomId):
                                    compId = _compId = npCompId
                                    seqId = _seqId = npSeqId
                                    preferNonPoly = resolved = True
                                    break

            if not resolved and compId in ('CYSZ', 'CYZ', 'CYS', 'ION', 'ZN1', 'ZN2')\
               and atomId in zincIonCode:
                znCount = 0
                znSeqId = None
                for np in self.nonPoly:
                    if np['comp_id'][0] == 'ZN':
                        znSeqId = np['auth_seq_id'][0]
                        znCount += 1
                if znCount > 0:
                    compId = _compId = 'ZN'
                    if znCount == 1:
                        seqId = _seqId = znSeqId
                        atomId = 'ZN'
                        resolved = True
                    preferNonPoly = True

            if not resolved and compId in ('CYS', 'CYSC', 'CYC', 'CCA', 'CYO', 'ION', 'CA1', 'CA2')\
               and atomId in calciumIonCode:
                caCount = 0
                caSeqId = None
                for np in self.nonPoly:
                    if np['comp_id'][0] == 'CA':
                        caSeqId = np['auth_seq_id'][0]
                        caCount += 1
                if caCount > 0:
                    compId = _compId = 'CA'
                    if caCount == 1:
                        seqId = _seqId = caSeqId
                        atomId = 'CA'
                        resolved = True
                    preferNonPoly = True

            if not resolved and len(atomId) > 1 and atomId in SYMBOLS_ELEMENT:
                elemCount = 0
                for np in self.nonPoly:
                    if np['comp_id'][0] == atomId:
                        elemCount += 1
                if elemCount > 0:
                    _, elemSeqId = getMetalCoordOf(self.cR, seqId, compId, atomId)
                    if elemSeqId is not None:
                        seqId = _seqId = elemSeqId
                        compId = _compId = atomId
                        preferNonPoly = resolved = True
                    elif elemCount == 1:
                        for np in self.nonPoly:
                            if np['comp_id'][0] == atomId:
                                seqId = _seqId = np['auth_seq_id'][0]
                                compId = _compId = atomId
                                preferNonPoly = resolved = True

            if not resolved and len(compId) > 1 and compId in SYMBOLS_ELEMENT:
                elemCount = 0
                for np in self.nonPoly:
                    if np['comp_id'][0] == compId:
                        elemCount += 1
                if elemCount > 0:
                    _, elemSeqId = getMetalCoordOf(self.cR, seqId, compId, compId)
                    if elemSeqId is not None:
                        seqId = _seqId = elemSeqId
                        atomId = _compId = compId
                        preferNonPoly = True
                    elif elemCount == 1:
                        for np in self.nonPoly:
                            if np['comp_id'][0] == compId:
                                seqId = _seqId = np['auth_seq_id'][0]
                                atomId = _compId = compId
                                preferNonPoly = True

        if self.__splitLigand is not None and len(self.__splitLigand):
            found = False
            for (_, _seqId_, _compId_), ligList in self.__splitLigand.items():
                if _seqId_ != seqId or _compId_ != compId:
                    continue
                for idx, lig in enumerate(ligList):
                    _atomId = atomId
                    if self.__mrAtomNameMapping is not None and compId not in monDict3:
                        _, _, _atomId = retrieveAtomIdentFromMRMap(self.ccU, self.__mrAtomNameMapping, seqId, compId, atomId)

                    if _atomId in lig['atom_ids']:
                        seqId = _seqId = lig['auth_seq_id']
                        compId = _compId = lig['comp_id']
                        atomId = _atomId
                        preferNonPoly = idx > 0
                        found = True
                        break
                if found:
                    break

        if self.__mrAtomNameMapping is not None and compId not in monDict3:
            seqId, compId, _ = retrieveAtomIdentFromMRMap(self.ccU, self.__mrAtomNameMapping, seqId, compId, atomId)

        compId = self.translateToStdResNameWrapper(_seqId, _compId, preferNonPoly)

        if len(self.__modResidue) > 0:
            modRes = next((modRes for modRes in self.__modResidue
                           if modRes['auth_comp_id'] == compId
                           and (compId != _compId or seqId in (modRes['auth_seq_id'], modRes['seq_id']))), None)
            if modRes is not None:
                compId = modRes['comp_id']

        if self.reasons is not None:
            if 'non_poly_remap' in self.reasons and _compId in self.reasons['non_poly_remap']\
               and seqId in self.reasons['non_poly_remap'][_compId]:
                fixedChainId, fixedSeqId = retrieveRemappedNonPoly(self.reasons['non_poly_remap'], refChainId, seqId, _compId)
                refChainId = fixedChainId
                preferNonPoly = True
            if 'branched_remap' in self.reasons and seqId in self.reasons['branched_remap']:
                fixedChainId, fixedSeqId = retrieveRemappedChainId(self.reasons['branched_remap'], seqId)
                refChainId = fixedChainId
                preferNonPoly = True
            if not preferNonPoly:
                if 'chain_id_remap' in self.reasons and seqId in self.reasons['chain_id_remap']:
                    fixedChainId, fixedSeqId = retrieveRemappedChainId(self.reasons['chain_id_remap'], seqId)
                    refChainId = fixedChainId
                elif 'chain_id_clone' in self.reasons and seqId in self.reasons['chain_id_clone']:
                    fixedChainId, fixedSeqId = retrieveRemappedChainId(self.reasons['chain_id_clone'], seqId)
                    refChainId = fixedChainId
                elif 'seq_id_remap' in self.reasons\
                        or 'chain_seq_id_remap' in self.reasons\
                        or 'ext_chain_seq_id_remap' in self.reasons:
                    if 'ext_chain_seq_id_remap' in self.reasons:
                        fixedChainId, fixedSeqId, fixedCompId =\
                            retrieveRemappedSeqIdAndCompId(self.reasons['ext_chain_seq_id_remap'], refChainId, seqId,
                                                           compId if compId in monDict3 else None)
                        self.__allow_ext_seq = fixedCompId is not None
                        if fixedSeqId is not None:
                            refChainId = fixedChainId
                    if fixedSeqId is None and 'chain_seq_id_remap' in self.reasons:
                        fixedChainId, fixedSeqId = retrieveRemappedSeqId(self.reasons['chain_seq_id_remap'], refChainId, seqId,
                                                                         compId if compId in monDict3 else None)
                        if fixedSeqId is not None:
                            refChainId = fixedChainId
                    if fixedSeqId is None and 'seq_id_remap' in self.reasons:
                        _, fixedSeqId = retrieveRemappedSeqId(self.reasons['seq_id_remap'], refChainId, seqId)
            if fixedSeqId is not None:
                _seqId = fixedSeqId

        updatePolySeqRst(self.polySeqRst, self.polySeq[0]['chain_id'] if refChainId is None else refChainId, _seqId, compId, _compId)

        types = self.csStat.getTypeOfCompId(compId)
        if all(not t for t in types) or compId in ('MTS', 'ORI'):
            types = None
        elif compId != _compId:
            if types != self.csStat.getTypeOfCompId(_compId):
                types = None

        def comp_id_unmatched_with(ps, cif_comp_id):
            if 'alt_comp_id' in ps and self.csStat.peptideLike(cif_comp_id) and compId.startswith('D') and len(compId) >= 3\
               and self.ccU.lastChemCompDict['_chem_comp.type'].upper() == 'D-PEPTIDE LINKING':
                revertPolySeqRst(self.polySeqRst, ps['chain_id'] if fixedChainId is None else fixedChainId, _seqId, compId)

            if types is None or ('alt_comp_id' in ps and _compId in ps['alt_comp_id']):
                return False
            if compId not in monDict3 and cif_comp_id not in monDict3:
                return False
            return types != self.csStat.getTypeOfCompId(cif_comp_id)

        def comp_id_in_polymer(np):
            return (_seqId == 1
                    and ((compId.endswith('-N') and all(c in np['comp_id'][0] for c in compId.split('-')[0]))
                         or (np['comp_id'][0] == 'PCA' and 'P' == compId[0] and ('GL' in compId or 'N' in compId))))\
                or (compId in monDict3
                    and any(compId in ps['comp_id'] for ps in self.polySeq)
                    and compId not in np['comp_id'])

        if refChainId is not None or refChainId != _refChainId:
            if any(ps for ps in self.polySeq if ps['auth_chain_id'] == _refChainId):
                fixedChainId = _refChainId
            elif self.hasNonPolySeq:
                if any(np for np in self.nonPolySeq if np['auth_chain_id'] == _refChainId):
                    fixedChainId = _refChainId

        for ps in self.polySeq:
            if preferNonPoly:
                continue
            chainId, seqId, cifCompId = self.getRealChainSeqId(ps, _seqId, compId)
            if fixedChainId is None and refChainId is not None and refChainId != chainId and refChainId in self.chainNumberDict:
                if chainId != self.chainNumberDict[refChainId]:
                    continue
            if self.reasons is not None:
                if fixedChainId is not None:
                    if fixedChainId != chainId:
                        continue
                    if fixedSeqId is not None:
                        seqId = fixedSeqId
                elif fixedSeqId is not None:
                    seqId = fixedSeqId
            if seqId <= 0 and self.__shiftNonPosSeq is not None and chainId in self.__shiftNonPosSeq:
                seqId -= 1
            if seqId in ps['auth_seq_id'] or fixedCompId is not None:
                if fixedCompId is not None:
                    cifCompId = origCompId = fixedCompId
                else:
                    if cifCompId is not None:
                        idx = next((_idx for _idx, (_seqId_, _cifCompId_) in enumerate(zip(ps['auth_seq_id'], ps['comp_id']))
                                    if _seqId_ == seqId and _cifCompId_ == cifCompId), ps['auth_seq_id'].index(seqId))
                    else:
                        idx = ps['auth_seq_id'].index(seqId) if seqId in ps['auth_seq_id'] else ps['seq_id'].index(seqId)
                    cifCompId = ps['comp_id'][idx]
                    origCompId = ps['auth_comp_id'][idx]
                    if comp_id_unmatched_with(ps, cifCompId):
                        continue
                if cifCompId != compId:
                    if (self.__shiftNonPosSeq is None or chainId not in self.__shiftNonPosSeq)\
                       and seqId <= 0 and seqId - 1 in ps['auth_seq_id']\
                       and compId == ps['comp_id'][ps['auth_seq_id'].index(seqId - 1)]:
                        seqId -= 1
                        if self.__shiftNonPosSeq is None:
                            self.__shiftNonPosSeq = {}
                        self.__shiftNonPosSeq[chainId] = True
                    compIds = [_compId for _seqId, _compId in zip(ps['auth_seq_id'], ps['comp_id']) if _seqId == seqId]
                    if compId in compIds:
                        cifCompId = compId
                        origCompId = next(origCompId for _seqId, _compId, origCompId in zip(ps['auth_seq_id'], ps['comp_id'], ps['auth_comp_id'])
                                          if _seqId == seqId and _compId == compId)
                if self.__mrAtomNameMapping is not None and origCompId not in monDict3:
                    _, coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCompId, cifCheck=self.__hasCoord)
                    atomId = retrieveAtomIdFromMRMap(self.ccU, self.__mrAtomNameMapping, seqId, origCompId, atomId, coordAtomSite)
                if compId in (cifCompId, origCompId, 'MTS', 'ORI'):
                    if len(self.nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                        chainAssign.add((chainId, seqId, cifCompId, True))
                        if refChainId is not None and refChainId != chainId and refChainId not in self.chainNumberDict:
                            self.chainNumberDict[refChainId] = chainId
                else:
                    _atomId, _, details = self.nefT.get_valid_star_atom(cifCompId, atomId)
                    if len(_atomId) > 0 and (details is None or _compId not in monDict3):
                        chainAssign.add((chainId, seqId, cifCompId, True))
                        if refChainId is not None and refChainId != chainId and refChainId not in self.chainNumberDict:
                            self.chainNumberDict[refChainId] = chainId

            elif 'gap_in_auth_seq' in ps and ps['gap_in_auth_seq']:
                auth_seq_id_list = list(filter(None, ps['auth_seq_id']))
                if len(auth_seq_id_list) > 0:
                    min_auth_seq_id = min(auth_seq_id_list)
                    max_auth_seq_id = max(auth_seq_id_list)
                    if min_auth_seq_id <= seqId <= max_auth_seq_id:
                        _seqId_ = seqId + 1
                        while _seqId_ <= max_auth_seq_id:
                            if _seqId_ in ps['auth_seq_id']:
                                break
                            _seqId_ += 1
                        if _seqId_ not in ps['auth_seq_id']:
                            _seqId_ = seqId - 1
                            while _seqId_ >= min_auth_seq_id:
                                if _seqId_ in ps['auth_seq_id']:
                                    break
                                _seqId_ -= 1
                        if _seqId_ in ps['auth_seq_id']:
                            idx = ps['auth_seq_id'].index(_seqId_) - (_seqId_ - seqId)
                            try:
                                seqId_ = ps['auth_seq_id'][idx]
                                cifCompId = ps['comp_id'][idx]
                                origCompId = ps['auth_comp_id'][idx]
                                if comp_id_unmatched_with(ps, cifCompId):
                                    continue
                                if cifCompId != compId:
                                    compIds = [_compId for _seqId, _compId in zip(ps['auth_seq_id'], ps['comp_id']) if _seqId == seqId]
                                    if compId in compIds:
                                        cifCompId = compId
                                        origCompId = next(origCompId for _seqId, _compId, origCompId in zip(ps['auth_seq_id'], ps['comp_id'], ps['auth_comp_id'])
                                                          if _seqId == seqId and _compId == compId)
                                if self.__mrAtomNameMapping is not None and origCompId not in monDict3:
                                    _, coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId_, cifCompId, cifCheck=self.__hasCoord)
                                    atomId = retrieveAtomIdFromMRMap(self.ccU, self.__mrAtomNameMapping, seqId, origCompId, atomId, coordAtomSite)
                                if compId in (cifCompId, origCompId, 'MTS', 'ORI'):
                                    if len(self.nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                                        chainAssign.add((chainId, seqId_, cifCompId, True))
                                        if refChainId is not None and refChainId != chainId and refChainId not in self.chainNumberDict:
                                            self.chainNumberDict[refChainId] = chainId
                                else:
                                    _atomId, _, details = self.nefT.get_valid_star_atom(cifCompId, atomId)
                                    if len(_atomId) > 0 and (details is None or _compId not in monDict3):
                                        chainAssign.add((chainId, seqId_, cifCompId, True))
                                        if refChainId is not None and refChainId != chainId and refChainId not in self.chainNumberDict:
                                            self.chainNumberDict[refChainId] = chainId
                            except IndexError:
                                pass

        if self.hasNonPolySeq:
            ligands = 0
            if self.hasNonPoly:
                for np in self.nonPoly:
                    ligands += np['comp_id'].count(_compId)
                if ligands == 0:
                    for np in self.nonPoly:
                        ligands += np['comp_id'].count(compId)
                    if ligands == 1:
                        _compId = compId
                if ligands == 0:
                    for np in self.nonPoly:
                        if 'alt_comp_id' in np:
                            ligands += np['alt_comp_id'].count(_compId)
                if ligands == 0:
                    for np in self.nonPoly:
                        if 'alt_comp_id' in np:
                            ligands += np['alt_comp_id'].count(compId)
                    if ligands == 1:
                        _compId = compId
                if ligands == 0 and len(chainAssign) == 0:
                    __compId = None
                    for np in self.nonPoly:
                        for ligand in np['comp_id']:
                            __compId = translateToLigandName(_compId, ligand, self.ccU)
                            if __compId == ligand:
                                ligands += 1
                    if ligands == 1:
                        compId = _compId = __compId
                    elif len(self.nonPoly) == 1 and self.ccU.updateChemCompDict(_compId, False):
                        if self.ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] == 'OBS':
                            compId = _compId = self.nonPoly[0]['comp_id'][0]
                            ligands = 1
            for np in self.nonPolySeq:
                chainId, seqId, cifCompId = self.getRealChainSeqId(np, _seqId, compId, False)
                if fixedChainId is None and refChainId is not None and refChainId != chainId and refChainId in self.chainNumberDict:
                    if chainId != self.chainNumberDict[refChainId]:
                        continue
                if self.reasons is not None:
                    if fixedChainId is not None:
                        if fixedChainId != chainId:
                            continue
                        if fixedSeqId is not None:
                            seqId = fixedSeqId
                    elif fixedSeqId is not None:
                        seqId = fixedSeqId
                if comp_id_in_polymer(np):
                    continue
                if 'alt_auth_seq_id' in np and seqId not in np['auth_seq_id'] and seqId in np['alt_auth_seq_id']:
                    try:
                        seqId = next(_seqId_ for _seqId_, _altSeqId_ in zip(np['auth_seq_id'], np['alt_auth_seq_id']) if _altSeqId_ == seqId)
                    except StopIteration:
                        pass
                if seqId in np['auth_seq_id']\
                   or (ligands == 1 and (_compId in np['comp_id'] or ('alt_comp_id' in np and _compId in np['alt_comp_id']))):
                    if ligands == 1 and cifCompId is None:
                        cifCompId = _compId
                    idx = -1
                    try:
                        if cifCompId is not None:
                            idx = next(_idx for _idx, (_seqId_, _cifCompId_) in enumerate(zip(np['auth_seq_id'], np['comp_id']))
                                       if (_seqId_ == seqId or ligands == 1) and _cifCompId_ == cifCompId)
                            if ligands == 1:
                                seqId = np['auth_seq_id'][idx]
                    except StopIteration:
                        pass
                    if idx == -1:
                        idx = np['auth_seq_id'].index(seqId) if seqId in np['auth_seq_id']\
                            else np['seq_id'].index(seqId) if seqId in np['seq_id'] else 0
                    cifCompId = np['comp_id'][idx]
                    origCompId = np['auth_comp_id'][idx]
                    seqId = np['auth_seq_id'][idx]
                    if cifCompId in ('ZN', 'CA') and atomId[0] in protonBeginCode:  # 2loa
                        continue
                    if self.__mrAtomNameMapping is not None and origCompId not in monDict3:
                        _, coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCompId, cifCheck=self.__hasCoord)
                        atomId = retrieveAtomIdFromMRMap(self.ccU, self.__mrAtomNameMapping, _seqId, origCompId, atomId, coordAtomSite)
                    if compId in (cifCompId, origCompId, 'MTS', 'ORI'):
                        if len(self.nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                            if (ligands == 1 or cifCompId in HEME_LIKE_RES_NAMES) and any(a[3] for a in chainAssign):
                                chainAssign.clear()
                            chainAssign.add((chainId, seqId, cifCompId, False))
                            if refChainId is not None and refChainId != chainId and refChainId not in self.chainNumberDict:
                                self.chainNumberDict[refChainId] = chainId
                    else:
                        _atomId, _, details = self.nefT.get_valid_star_atom(cifCompId, atomId)
                        if len(_atomId) > 0 and (details is None or _compId not in monDict3):
                            if (ligands == 1 or cifCompId in HEME_LIKE_RES_NAMES) and any(a[3] for a in chainAssign):
                                chainAssign.clear()
                            chainAssign.add((chainId, seqId, cifCompId, False))
                            if refChainId is not None and refChainId != chainId and refChainId not in self.chainNumberDict:
                                self.chainNumberDict[refChainId] = chainId

        if len(chainAssign) == 0:
            for ps in self.polySeq:
                if preferNonPoly:
                    continue
                chainId = ps['chain_id']
                if refChainId is not None and refChainId != chainId and refChainId in self.chainNumberDict:
                    if chainId != self.chainNumberDict[refChainId]:
                        continue
                if fixedChainId is not None and fixedChainId != chainId:
                    continue
                seqKey = (chainId, _seqId)
                if seqKey in self.__authToLabelSeq:
                    _, seqId = self.__authToLabelSeq[seqKey]
                    if seqId in ps['seq_id']:
                        idx = ps['seq_id'].index(seqId)
                        cifCompId = ps['comp_id'][idx]
                        origCompId = ps['auth_comp_id'][idx]
                        if comp_id_unmatched_with(ps, cifCompId):
                            continue
                        if cifCompId != compId:
                            compIds = [_compId for _seqId, _compId in zip(ps['auth_seq_id'], ps['comp_id']) if _seqId == seqId]
                            if compId in compIds:
                                cifCompId = compId
                                origCompId = next(origCompId for _seqId, _compId, origCompId in zip(ps['auth_seq_id'], ps['comp_id'], ps['auth_comp_id'])
                                                  if _seqId == seqId and _compId == compId)
                        if self.__mrAtomNameMapping is not None and origCompId not in monDict3:
                            _, coordAtomSite = self.getCoordAtomSiteOf(chainId, _seqId, cifCompId, cifCheck=self.__hasCoord)
                            atomId = retrieveAtomIdFromMRMap(self.ccU, self.__mrAtomNameMapping, seqId, origCompId, atomId, coordAtomSite)
                        if compId in (cifCompId, origCompId, 'MTS', 'ORI'):
                            if len(self.nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                                chainAssign.add((ps['auth_chain_id'], _seqId, cifCompId, True))
                                if refChainId is not None and refChainId != chainId and refChainId not in self.chainNumberDict:
                                    self.chainNumberDict[refChainId] = chainId
                        else:
                            _atomId, _, details = self.nefT.get_valid_star_atom(cifCompId, atomId)
                            if len(_atomId) > 0 and (details is None or _compId not in monDict3):
                                chainAssign.add((ps['auth_chain_id'], _seqId, cifCompId, True))
                                if refChainId is not None and refChainId != chainId and refChainId not in self.chainNumberDict:
                                    self.chainNumberDict[refChainId] = chainId

            if self.hasNonPolySeq:
                for np in self.nonPolySeq:
                    chainId = np['auth_chain_id']
                    if refChainId is not None and refChainId != chainId and refChainId in self.chainNumberDict:
                        if chainId != self.chainNumberDict[refChainId]:
                            continue
                    if fixedChainId is not None and fixedChainId != chainId:
                        continue
                    if comp_id_in_polymer(np):
                        continue
                    seqKey = (chainId, _seqId)
                    if seqKey in self.__authToLabelSeq:
                        _, seqId = self.__authToLabelSeq[seqKey]
                        if seqId in np['seq_id']:
                            idx = np['seq_id'].index(seqId)
                            cifCompId = np['comp_id'][idx]
                            origCompId = np['auth_comp_id'][idx]
                            if self.__mrAtomNameMapping is not None and origCompId not in monDict3:
                                _, coordAtomSite = self.getCoordAtomSiteOf(chainId, _seqId, cifCompId, cifCheck=self.__hasCoord)
                                atomId = retrieveAtomIdFromMRMap(self.ccU, self.__mrAtomNameMapping, seqId, origCompId, atomId, coordAtomSite)
                            if compId in (cifCompId, origCompId, 'MTS', 'ORI'):
                                if len(self.nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                                    chainAssign.add((np['auth_chain_id'], _seqId, cifCompId, False))
                                    if refChainId is not None and refChainId != chainId and refChainId not in self.chainNumberDict:
                                        self.chainNumberDict[refChainId] = chainId
                            else:
                                _atomId, _, details = self.nefT.get_valid_star_atom(cifCompId, atomId)
                                if len(_atomId) > 0 and (details is None or _compId not in monDict3):
                                    chainAssign.add((np['auth_chain_id'], _seqId, cifCompId, False))
                                    if refChainId is not None and refChainId != chainId and refChainId not in self.chainNumberDict:
                                        self.chainNumberDict[refChainId] = chainId

        if len(chainAssign) == 0 and self.__altPolySeq is not None:
            for ps in self.__altPolySeq:
                if preferNonPoly:
                    continue
                chainId = ps['auth_chain_id']
                if refChainId is not None and refChainId != chainId and refChainId in self.chainNumberDict:
                    if chainId != self.chainNumberDict[refChainId]:
                        continue
                if fixedChainId is not None and fixedChainId != chainId:
                    continue
                if _seqId in ps['auth_seq_id']:
                    cifCompId = ps['comp_id'][ps['auth_seq_id'].index(_seqId)]
                    if comp_id_unmatched_with(ps, cifCompId):
                        continue
                    if cifCompId != compId:
                        if cifCompId in monDict3 and compId in monDict3:
                            continue
                        compIds = [_compId for _seqId, _compId in zip(ps['auth_seq_id'], ps['comp_id']) if _seqId == seqId]
                        if compId in compIds:
                            cifCompId = compId
                    chainAssign.add((chainId, _seqId, cifCompId, True))
                    if refChainId is not None and refChainId != chainId and refChainId not in self.chainNumberDict:
                        self.chainNumberDict[refChainId] = chainId

        if len(chainAssign) == 0 and (self.__preferAuthSeqCount - self.__preferLabelSeqCount < MAX_PREF_LABEL_SCHEME_COUNT or len(self.polySeq) > 1):
            for ps in self.polySeq:
                if preferNonPoly:
                    continue
                chainId = ps['chain_id']
                if refChainId is not None and refChainId != chainId and refChainId in self.chainNumberDict:
                    if chainId != self.chainNumberDict[refChainId]:
                        continue
                if fixedChainId is not None and fixedChainId != chainId:
                    continue
                seqKey = (chainId, _seqId)
                if seqKey in self.__labelToAuthSeq:
                    _, seqId = self.__labelToAuthSeq[seqKey]
                    if seqId in ps['auth_seq_id']:
                        idx = ps['seq_id'].index(_seqId)
                        cifCompId = ps['comp_id'][idx]
                        origCompId = ps['auth_comp_id'][idx]
                        if comp_id_unmatched_with(ps, cifCompId):
                            continue
                        if cifCompId != compId:
                            compIds = [_compId for _seqId, _compId in zip(ps['auth_seq_id'], ps['comp_id']) if _seqId == seqId]
                            if compId in compIds:
                                cifCompId = compId
                                origCompId = next(origCompId for _seqId, _compId, origCompId in zip(ps['auth_seq_id'], ps['comp_id'], ps['auth_comp_id'])
                                                  if _seqId == seqId and _compId == compId)
                        if self.__mrAtomNameMapping is not None and origCompId not in monDict3:
                            _, coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCompId, cifCheck=self.__hasCoord)
                            atomId = retrieveAtomIdFromMRMap(self.ccU, self.__mrAtomNameMapping, seqId, origCompId, atomId, coordAtomSite)
                        if compId in (cifCompId, origCompId, 'MTS', 'ORI'):
                            if len(self.nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                                chainAssign.add((ps['auth_chain_id'], seqId, cifCompId, True))
                                if compId in (cifCompId, origCompId):
                                    self.__authSeqId = 'label_seq_id'
                                    self.__setLocalSeqScheme()
                                    if refChainId is not None and refChainId != chainId and refChainId not in self.chainNumberDict:
                                        self.chainNumberDict[refChainId] = chainId
                        else:
                            _atomId, _, details = self.nefT.get_valid_star_atom(cifCompId, atomId)
                            if len(_atomId) > 0 and (details is None or _compId not in monDict3):
                                chainAssign.add((ps['auth_chain_id'], seqId, cifCompId, True))
                                self.__authSeqId = 'label_seq_id'
                                self.__setLocalSeqScheme()
                                if refChainId is not None and refChainId != chainId and refChainId not in self.chainNumberDict:
                                    self.chainNumberDict[refChainId] = chainId

        if len(chainAssign) == 0:
            if seqId == 1 or (refChainId, seqId - 1) in self.__coordUnobsRes:
                if atomId in aminoProtonCode and atomId != 'H1':
                    return self.assignCoordPolymerSequence(refChainId, seqId, compId, 'H1', index)
            auth_seq_id_list = list(filter(None, self.polySeq[0]['auth_seq_id']))
            min_auth_seq_id = max_auth_seq_id = UNREAL_AUTH_SEQ_NUM
            if len(auth_seq_id_list) > 0:
                min_auth_seq_id = min(auth_seq_id_list)
                max_auth_seq_id = max(auth_seq_id_list)
            if len(self.polySeq) == 1\
               and (seqId < 1
                    or (compId == 'ACE' and seqId == min_auth_seq_id - 1)
                    or (compId == 'NH2' and seqId == max_auth_seq_id + 1)
                    or (compId in monDict3 and self.__preferAuthSeqCount - self.__preferLabelSeqCount >= MAX_PREF_LABEL_SCHEME_COUNT)):
                refChainId = self.polySeq[0]['auth_chain_id']
                if (compId == 'ACE' and seqId == min_auth_seq_id - 1)\
                   or (compId == 'NH2' and seqId == max_auth_seq_id + 1)\
                   or (compId in monDict3 and self.__preferAuthSeqCount - self.__preferLabelSeqCount >= MAX_PREF_LABEL_SCHEME_COUNT
                       and (min_auth_seq_id - MAX_ALLOWED_EXT_SEQ <= seqId < min_auth_seq_id
                            or max_auth_seq_id < seqId <= max_auth_seq_id + MAX_ALLOWED_EXT_SEQ)):
                    self.f.append(f"[Sequence mismatch warning] {self.getCurrentRestraint(n=index)}"
                                  f"The residue '{_seqId}:{_compId}' is not present in polymer sequence "
                                  f"of chain {refChainId} of the coordinates. "
                                  "Please update the sequence in the Macromolecules page.")
                    resKey = (_seqId, _compId)
                    if resKey not in self.extResKey:
                        self.extResKey.append(resKey)
                    chainAssign.add((refChainId, _seqId, compId, True))
                    asis = True
                elif compId in monDict3 and self.__preferAuthSeqCount - self.__preferLabelSeqCount >= MAX_PREF_LABEL_SCHEME_COUNT:
                    self.f.append(f"[Sequence mismatch warning] {self.getCurrentRestraint(n=index)}"
                                  f"The residue '{_seqId}:{_compId}' is not present in polymer sequence "
                                  f"of chain {refChainId} of the coordinates. "
                                  "Please update the sequence in the Macromolecules page.")
                    resKey = (_seqId, _compId)
                    if resKey not in self.extResKey:
                        self.extResKey.append(resKey)
                elif self.no_extra_comment:
                    self.f.append(f"[Atom not found] {self.getCurrentRestraint(n=index)}"
                                  f"{_seqId}:{_compId}:{atomId} is not present in the coordinates. "
                                  f"The residue number '{_seqId}' is not present in polymer sequence "
                                  f"of chain {refChainId} of the coordinates. "
                                  "Please update the sequence in the Macromolecules page.")
            else:
                ext_seq = False
                if (compId in monDict3 or compId in ('ACE', 'NH2')) and self.__preferAuthSeqCount - self.__preferLabelSeqCount >= MAX_PREF_LABEL_SCHEME_COUNT:
                    refChainIds = []
                    _auth_seq_id_list = auth_seq_id_list
                    for idx, ps in enumerate(self.polySeq):
                        if idx > 0:
                            auth_seq_id_list = list(filter(None, ps['auth_seq_id']))
                            _auth_seq_id_list.extend(auth_seq_id_list)
                        if len(auth_seq_id_list) > 0:
                            if idx > 0:
                                min_auth_seq_id = min(auth_seq_id_list)
                                max_auth_seq_id = max(auth_seq_id_list)
                            if min_auth_seq_id - MAX_ALLOWED_EXT_SEQ <= seqId < min_auth_seq_id\
                               and (compId in monDict3 or (compId == 'ACE' and seqId == min_auth_seq_id - 1)):
                                refChainIds.append(ps['auth_chain_id'])
                                ext_seq = True
                            if max_auth_seq_id < seqId <= max_auth_seq_id + MAX_ALLOWED_EXT_SEQ\
                               and (compId in monDict3 or (compId == 'NH2' and seqId == max_auth_seq_id + 1)):
                                refChainIds.append(ps['auth_chain_id'])
                                ext_seq = True
                    if ext_seq and seqId in _auth_seq_id_list:
                        ext_seq = False
                if ext_seq:
                    refChainId = refChainIds[0] if len(refChainIds) == 1 else refChainIds
                    self.f.append(f"[Sequence mismatch warning] {self.getCurrentRestraint(n=index)}"
                                  f"The residue '{_seqId}:{_compId}' is not present in polymer sequence "
                                  f"of chain {refChainId} of the coordinates. "
                                  "Please update the sequence in the Macromolecules page.")
                    resKey = (_seqId, _compId)
                    if resKey not in self.extResKey:
                        self.extResKey.append(resKey)
                    if isinstance(refChainId, str):
                        chainAssign.add((refChainId, _seqId, compId, True))
                    else:
                        for _refChainId in refChainIds:
                            chainAssign.add((_refChainId, _seqId, compId, True))
                    asis = True
                elif self.no_extra_comment:
                    self.f.append(f"[Atom not found] {self.getCurrentRestraint(n=index)}"
                                  f"{_seqId}:{_compId}:{atomId} is not present in the coordinates.")
                updatePolySeqRst(self.polySeqRstFailed, self.polySeq[0]['chain_id'] if refChainId is None else refChainId, _seqId, compId, _compId)

        elif any(ca for ca in chainAssign if ca[0] == refChainId) and any(ca for ca in chainAssign if ca[0] != refChainId):
            _chainAssign = copy.copy(chainAssign)
            for _ca in _chainAssign:
                if _ca[0] != refChainId:
                    chainAssign.remove(_ca)

        return list(chainAssign), asis

    def assignCoordPolymerSequenceWithChainId(self, refChainId: str, seqId: int, compId: str, atomId: str, index: int
                                              ) -> Tuple[List[Tuple[str, int, str, bool]], bool]:
        """ Assign polymer sequences of the coordinates.
        """

        _refChainId = refChainId

        chainAssign = set()
        asis = False
        _seqId = seqId
        _compId = compId

        fixedChainId = fixedSeqId = fixedCompId = None

        preferNonPoly = False

        if self.hasNonPoly:

            resolved = False

            for np in self.nonPoly:
                if 'alt_comp_id' in np and 'alt_auth_seq_id' in np\
                   and compId in np['alt_comp_id'] and seqId in np['alt_auth_seq_id']:
                    npCompId = np['comp_id'][0]
                    npSeqId = np['auth_seq_id'][0]
                    for ps in self.polySeq:
                        if 'ambig_auth_seq_id' in ps and seqId in ps['ambig_auth_seq_id']:
                            psCompId = ps['comp_id'][ps['auth_seq_id'].index(seqId)]
                            _atomId, _, details = self.nefT.get_valid_star_atom_in_xplor(psCompId, atomId, leave_unmatched=True)
                            if details is None:
                                _, _coordAtomSite = self.getCoordAtomSiteOf(ps['auth_chain_id'], seqId, psCompId, cifCheck=self.__hasCoord)
                                if _coordAtomSite is not None and all(_atomId_ in _coordAtomSite['atom_id'] for _atomId_ in _atomId):
                                    compId = _compId = psCompId
                                    resolved = True
                                    break
                            _, _coordAtomSite = self.getCoordAtomSiteOf(np['auth_chain_id'], npSeqId, npCompId, cifCheck=self.__hasCoord)
                            if self.__mrAtomNameMapping is not None:
                                atomId = retrieveAtomIdFromMRMap(self.ccU, self.__mrAtomNameMapping, npSeqId, npCompId, atomId, _coordAtomSite)
                            _atomId, _, details = self.nefT.get_valid_star_atom_in_xplor(npCompId, atomId, leave_unmatched=True)
                            if details is None:
                                if _coordAtomSite is not None and all(_atomId_ in _coordAtomSite['atom_id'] for _atomId_ in _atomId):
                                    compId = _compId = npCompId
                                    seqId = _seqId = npSeqId
                                    preferNonPoly = resolved = True
                                    break

            if not resolved and compId in ('CYS', 'CYSZ', 'CYZ', 'CZN', 'CYO', 'ION', 'ZN1', 'ZN2')\
               and atomId in zincIonCode:
                znCount = 0
                znSeqId = None
                for np in self.nonPoly:
                    if np['comp_id'][0] == 'ZN':
                        znSeqId = np['auth_seq_id'][0]
                        znCount += 1
                if znCount > 0:
                    compId = _compId = 'ZN'
                    if znCount == 1:
                        seqId = _seqId = znSeqId
                        atomId = 'ZN'
                        resolved = True
                    preferNonPoly = True

            if not resolved and compId in ('CYS', 'CYSC', 'CYC', 'CCA', 'CYO', 'ION', 'CA1', 'CA2')\
               and atomId in calciumIonCode:
                caCount = 0
                caSeqId = None
                for np in self.nonPoly:
                    if np['comp_id'][0] == 'CA':
                        caSeqId = np['auth_seq_id'][0]
                        caCount += 1
                if caCount > 0:
                    compId = _compId = 'CA'
                    if caCount == 1:
                        seqId = _seqId = caSeqId
                        atomId = 'CA'
                        resolved = True
                    preferNonPoly = True

            if not resolved and len(atomId) > 1 and atomId in SYMBOLS_ELEMENT:
                elemCount = 0
                for np in self.nonPoly:
                    if np['comp_id'][0] == atomId:
                        elemCount += 1
                if elemCount > 0:
                    _, elemSeqId = getMetalCoordOf(self.cR, seqId, compId, atomId)
                    if elemSeqId is not None:
                        seqId = _seqId = elemSeqId
                        compId = _compId = atomId
                        preferNonPoly = resolved = True
                    elif elemCount == 1:
                        for np in self.nonPoly:
                            if np['comp_id'][0] == atomId:
                                seqId = _seqId = np['auth_seq_id'][0]
                                compId = _compId = atomId
                                preferNonPoly = resolved = True

            if not resolved and len(compId) > 1 and compId in SYMBOLS_ELEMENT:
                elemCount = 0
                for np in self.nonPoly:
                    if np['comp_id'][0] == compId:
                        elemCount += 1
                if elemCount > 0:
                    _, elemSeqId = getMetalCoordOf(self.cR, seqId, compId, compId)
                    if elemSeqId is not None:
                        seqId = _seqId = elemSeqId
                        atomId = _compId = compId
                        preferNonPoly = True
                    elif elemCount == 1:
                        for np in self.nonPoly:
                            if np['comp_id'][0] == compId:
                                seqId = _seqId = np['auth_seq_id'][0]
                                atomId = _compId = compId
                                preferNonPoly = True

        if self.__splitLigand is not None and len(self.__splitLigand):
            found = False
            for (_, _seqId_, _compId_), ligList in self.__splitLigand.items():
                if _seqId_ != seqId or _compId_ != compId:
                    continue
                for idx, lig in enumerate(ligList):
                    _atomId = atomId
                    if self.__mrAtomNameMapping is not None and compId not in monDict3:
                        _, _, _atomId = retrieveAtomIdentFromMRMap(self.ccU, self.__mrAtomNameMapping, seqId, compId, atomId)

                    if _atomId in lig['atom_ids']:
                        seqId = _seqId = lig['auth_seq_id']
                        compId = _compId = lig['comp_id']
                        atomId = _atomId
                        preferNonPoly = idx > 0
                        found = True
                        break
                if found:
                    break

        if self.__mrAtomNameMapping is not None and compId not in monDict3:
            seqId, compId, _ = retrieveAtomIdentFromMRMap(self.ccU, self.__mrAtomNameMapping, seqId, compId, atomId)

        compId = self.translateToStdResNameWrapper(_seqId, _compId, preferNonPoly)

        if len(self.__modResidue) > 0:
            modRes = next((modRes for modRes in self.__modResidue
                           if modRes['auth_comp_id'] == compId
                           and (compId != _compId or seqId in (modRes['auth_seq_id'], modRes['seq_id']))), None)
            if modRes is not None:
                compId = modRes['comp_id']

        self.__allow_ext_seq = False

        if self.reasons is not None:
            if 'unambig_atom_id_remap' in self.reasons and _compId in self.reasons['unambig_atom_id_remap']\
               and atomId in self.reasons['unambig_atom_id_remap'][_compId]:
                atomId = self.reasons['unambig_atom_id_remap'][_compId][atomId][0]  # select representative one
            if 'non_poly_remap' in self.reasons and _compId in self.reasons['non_poly_remap']\
               and seqId in self.reasons['non_poly_remap'][_compId]:
                fixedChainId, fixedSeqId = retrieveRemappedNonPoly(self.reasons['non_poly_remap'], str(refChainId), seqId, _compId)
                refChainId = fixedChainId
                preferNonPoly = True
            if 'branched_remap' in self.reasons and seqId in self.reasons['branched_remap']:
                fixedChainId, fixedSeqId = retrieveRemappedChainId(self.reasons['branched_remap'], seqId)
                refChainId = fixedChainId
                preferNonPoly = True
            if not preferNonPoly:
                if 'chain_id_remap' in self.reasons and seqId in self.reasons['chain_id_remap']:
                    fixedChainId, fixedSeqId = retrieveRemappedChainId(self.reasons['chain_id_remap'], seqId)
                    refChainId = fixedChainId
                elif 'chain_id_clone' in self.reasons and seqId in self.reasons['chain_id_clone']:
                    fixedChainId, fixedSeqId = retrieveRemappedChainId(self.reasons['chain_id_clone'], seqId)
                    refChainId = fixedChainId
                elif 'seq_id_remap' in self.reasons\
                        or 'chain_seq_id_remap' in self.reasons\
                        or 'ext_chain_seq_id_remap' in self.reasons:
                    if 'ext_chain_seq_id_remap' in self.reasons:
                        fixedChainId, fixedSeqId, fixedCompId =\
                            retrieveRemappedSeqIdAndCompId(self.reasons['ext_chain_seq_id_remap'], str(refChainId), seqId,
                                                           compId if compId in monDict3 else None)
                        self.__allow_ext_seq = fixedCompId is not None
                        if fixedSeqId is not None:
                            refChainId = fixedChainId
                    if fixedSeqId is None and 'chain_seq_id_remap' in self.reasons:
                        fixedChainId, fixedSeqId = retrieveRemappedSeqId(self.reasons['chain_seq_id_remap'], str(refChainId), seqId,
                                                                         compId if compId in monDict3 else None)
                        if fixedSeqId is not None:
                            refChainId = fixedChainId
                    if fixedSeqId is None and 'seq_id_remap' in self.reasons:
                        _, fixedSeqId = retrieveRemappedSeqId(self.reasons['seq_id_remap'], str(refChainId), seqId)
            if fixedSeqId is not None:
                _seqId = fixedSeqId

        updatePolySeqRst(self.polySeqRst, str(refChainId), _seqId, compId, _compId)

        types = self.csStat.getTypeOfCompId(compId)
        if all(not t for t in types) or compId in ('MTS', 'ORI'):
            types = None
        elif compId != _compId:
            if types != self.csStat.getTypeOfCompId(_compId):
                types = None

        def comp_id_unmatched_with(ps, cif_comp_id):
            if 'alt_comp_id' in ps and self.csStat.peptideLike(cif_comp_id) and compId.startswith('D') and len(compId) >= 3\
               and self.ccU.lastChemCompDict['_chem_comp.type'].upper() == 'D-PEPTIDE LINKING':
                revertPolySeqRst(self.polySeqRst, str(refChainId), _seqId, compId)

            if types is None or ('alt_comp_id' in ps and _compId in ps['alt_comp_id']):
                return False
            if compId not in monDict3 and cif_comp_id not in monDict3:
                return False
            return types != self.csStat.getTypeOfCompId(cif_comp_id)

        def comp_id_in_polymer(np):
            return (_seqId == 1
                    and ((compId.endswith('-N') and all(c in np['comp_id'][0] for c in compId.split('-')[0]))
                         or (np['comp_id'][0] == 'PCA' and 'P' == compId[0] and ('GL' in compId or 'N' in compId))))\
                or (compId in monDict3
                    and any(compId in ps['comp_id'] for ps in self.polySeq)
                    and compId not in np['comp_id'])

        if refChainId is not None or refChainId != _refChainId:
            if any(ps for ps in self.polySeq if ps['auth_chain_id'] == _refChainId):
                fixedChainId = _refChainId
            elif self.hasNonPolySeq:
                if any(np for np in self.nonPolySeq if np['auth_chain_id'] == _refChainId):
                    fixedChainId = _refChainId

        for ps in self.polySeq:
            if preferNonPoly:
                continue
            chainId, seqId, cifCompId = self.getRealChainSeqId(ps, _seqId, compId)
            if fixedChainId is None and refChainId is not None and refChainId != chainId and refChainId in self.chainNumberDict:
                if chainId != self.chainNumberDict[refChainId]:
                    continue
            if self.reasons is not None:
                if fixedChainId is not None:
                    if fixedChainId != chainId:
                        continue
                    if fixedSeqId is not None:
                        seqId = fixedSeqId
                elif fixedSeqId is not None:
                    seqId = fixedSeqId
            if seqId <= 0 and self.__shiftNonPosSeq is not None and chainId in self.__shiftNonPosSeq:
                seqId -= 1
            if seqId in ps['auth_seq_id'] or fixedCompId is not None:
                if fixedCompId is not None:
                    cifCompId = origCompId = fixedCompId
                else:
                    if cifCompId is not None:
                        idx = next((_idx for _idx, (_seqId_, _cifCompId_) in enumerate(zip(ps['auth_seq_id'], ps['comp_id']))
                                    if _seqId_ == seqId and _cifCompId_ == cifCompId), ps['auth_seq_id'].index(seqId))
                    else:
                        idx = ps['auth_seq_id'].index(seqId) if seqId in ps['auth_seq_id'] else ps['seq_id'].index(seqId)
                    cifCompId = ps['comp_id'][idx]
                    origCompId = ps['auth_comp_id'][idx]
                    if comp_id_unmatched_with(ps, cifCompId):
                        continue
                if cifCompId != compId:
                    if (self.__shiftNonPosSeq is None or chainId not in self.__shiftNonPosSeq)\
                       and seqId <= 0 and seqId - 1 in ps['auth_seq_id']\
                       and compId == ps['comp_id'][ps['auth_seq_id'].index(seqId - 1)]:
                        seqId -= 1
                        if self.__shiftNonPosSeq is None:
                            self.__shiftNonPosSeq = {}
                        self.__shiftNonPosSeq[chainId] = True
                    compIds = [_compId for _seqId, _compId in zip(ps['auth_seq_id'], ps['comp_id']) if _seqId == seqId]
                    if compId in compIds:
                        cifCompId = compId
                        origCompId = next(origCompId for _seqId, _compId, origCompId in zip(ps['auth_seq_id'], ps['comp_id'], ps['auth_comp_id'])
                                          if _seqId == seqId and _compId == compId)
                if self.__mrAtomNameMapping is not None and origCompId not in monDict3:
                    _, coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCompId, cifCheck=self.__hasCoord)
                    atomId = retrieveAtomIdFromMRMap(self.ccU, self.__mrAtomNameMapping, seqId, origCompId, atomId, coordAtomSite)
                if compId in (cifCompId, origCompId, 'MTS', 'ORI'):
                    if len(self.nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                        chainAssign.add((chainId, seqId, cifCompId, True))
                        if refChainId is not None and refChainId != chainId and refChainId not in self.chainNumberDict:
                            self.chainNumberDict[refChainId] = chainId
                else:
                    _atomId, _, details = self.nefT.get_valid_star_atom(cifCompId, atomId)
                    if len(_atomId) > 0 and (details is None or _compId not in monDict3):
                        chainAssign.add((chainId, seqId, cifCompId, True))
                        if refChainId is not None and refChainId != chainId and refChainId not in self.chainNumberDict:
                            self.chainNumberDict[refChainId] = chainId

            elif 'gap_in_auth_seq' in ps and ps['gap_in_auth_seq']:
                auth_seq_id_list = list(filter(None, ps['auth_seq_id']))
                if len(auth_seq_id_list) > 0:
                    min_auth_seq_id = min(auth_seq_id_list)
                    max_auth_seq_id = max(auth_seq_id_list)
                    if min_auth_seq_id <= seqId <= max_auth_seq_id:
                        _seqId_ = seqId + 1
                        while _seqId_ <= max_auth_seq_id:
                            if _seqId_ in ps['auth_seq_id']:
                                break
                            _seqId_ += 1
                        if _seqId_ not in ps['auth_seq_id']:
                            _seqId_ = seqId - 1
                            while _seqId_ >= min_auth_seq_id:
                                if _seqId_ in ps['auth_seq_id']:
                                    break
                                _seqId_ -= 1
                        if _seqId_ in ps['auth_seq_id']:
                            idx = ps['auth_seq_id'].index(_seqId_) - (_seqId_ - seqId)
                            try:
                                seqId_ = ps['auth_seq_id'][idx]
                                cifCompId = ps['comp_id'][idx]
                                origCompId = ps['auth_comp_id'][idx]
                                if comp_id_unmatched_with(ps, cifCompId):
                                    continue
                                if cifCompId != compId:
                                    compIds = [_compId for _seqId, _compId in zip(ps['auth_seq_id'], ps['comp_id']) if _seqId == seqId]
                                    if compId in compIds:
                                        cifCompId = compId
                                        origCompId = next(origCompId for _seqId, _compId, origCompId in zip(ps['auth_seq_id'], ps['comp_id'], ps['auth_comp_id'])
                                                          if _seqId == seqId and _compId == compId)
                                if self.__mrAtomNameMapping is not None and origCompId not in monDict3:
                                    _, coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId_, cifCompId, cifCheck=self.__hasCoord)
                                    atomId = retrieveAtomIdFromMRMap(self.ccU, self.__mrAtomNameMapping, seqId, origCompId, atomId, coordAtomSite)
                                if compId in (cifCompId, origCompId, 'MTS', 'ORI'):
                                    if len(self.nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                                        chainAssign.add((chainId, seqId_, cifCompId, True))
                                    else:
                                        _atomId, _, details = self.nefT.get_valid_star_atom(cifCompId, atomId)
                                        if len(_atomId) > 0 and (details is None or _compId not in monDict3):
                                            chainAssign.add((chainId, seqId_, cifCompId, True))
                            except IndexError:
                                pass

        if self.hasNonPolySeq:
            ligands = 0
            if self.hasNonPoly:
                for np in self.nonPoly:
                    ligands += np['comp_id'].count(_compId)
                if ligands == 0:
                    for np in self.nonPoly:
                        ligands += np['comp_id'].count(compId)
                    if ligands == 1:
                        _compId = compId
                if ligands == 0:
                    for np in self.nonPoly:
                        if 'alt_comp_id' in np:
                            ligands += np['alt_comp_id'].count(_compId)
                if ligands == 0:
                    for np in self.nonPoly:
                        if 'alt_comp_id' in np:
                            ligands += np['alt_comp_id'].count(compId)
                    if ligands == 1:
                        _compId = compId
                if ligands == 0 and len(chainAssign) == 0:
                    __compId = None
                    for np in self.nonPoly:
                        for ligand in np['comp_id']:
                            __compId = translateToLigandName(_compId, ligand, self.ccU)
                            if __compId == ligand:
                                ligands += 1
                    if ligands == 1:
                        compId = _compId = __compId
                    elif len(self.nonPoly) == 1 and self.ccU.updateChemCompDict(_compId, False):
                        if self.ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] == 'OBS':
                            compId = _compId = self.nonPoly[0]['comp_id'][0]
                            ligands = 1
            for np in self.nonPolySeq:
                chainId, seqId, cifCompId = self.getRealChainSeqId(np, _seqId, compId, False)
                if fixedChainId is None and refChainId is not None and refChainId != chainId and refChainId in self.chainNumberDict:
                    if chainId != self.chainNumberDict[refChainId]:
                        continue
                if self.reasons is not None:
                    if fixedChainId is not None:
                        if fixedChainId != chainId:
                            continue
                        if fixedSeqId is not None:
                            seqId = fixedSeqId
                    elif fixedSeqId is not None:
                        seqId = fixedSeqId
                if comp_id_in_polymer(np):
                    continue
                if 'alt_auth_seq_id' in np and seqId not in np['auth_seq_id'] and seqId in np['alt_auth_seq_id']:
                    try:
                        seqId = next(_seqId_ for _seqId_, _altSeqId_ in zip(np['auth_seq_id'], np['alt_auth_seq_id']) if _altSeqId_ == seqId)
                    except StopIteration:
                        pass
                if seqId in np['auth_seq_id']\
                   or (ligands == 1 and (_compId in np['comp_id'] or ('alt_comp_id' in np and _compId in np['alt_comp_id']))):
                    if ligands == 1 and cifCompId is None:
                        cifCompId = _compId
                    idx = -1
                    try:
                        if cifCompId is not None:
                            idx = next(_idx for _idx, (_seqId_, _cifCompId_) in enumerate(zip(np['auth_seq_id'], np['comp_id']))
                                       if (_seqId_ == seqId or ligands == 1) and _cifCompId_ == cifCompId)
                            if ligands == 1:
                                seqId = np['auth_seq_id'][idx]
                    except StopIteration:
                        pass
                    if idx == -1:
                        idx = np['auth_seq_id'].index(seqId) if seqId in np['auth_seq_id']\
                            else np['seq_id'].index(seqId) if seqId in np['seq_id'] else 0
                    cifCompId = np['comp_id'][idx]
                    origCompId = np['auth_comp_id'][idx]
                    seqId = np['auth_seq_id'][idx]
                    if cifCompId in ('ZN', 'CA') and atomId[0] in protonBeginCode:  # 2loa
                        continue
                    if self.__mrAtomNameMapping is not None and origCompId not in monDict3:
                        _, coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCompId, cifCheck=self.__hasCoord)
                        atomId = retrieveAtomIdFromMRMap(self.ccU, self.__mrAtomNameMapping, _seqId, origCompId, atomId, coordAtomSite)
                    if compId in (cifCompId, origCompId, 'MTS', 'ORI'):
                        if len(self.nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                            if (ligands == 1 or cifCompId in HEME_LIKE_RES_NAMES) and any(a[3] for a in chainAssign):
                                chainAssign.clear()
                            chainAssign.add((chainId, seqId, cifCompId, False))
                            if refChainId is not None and refChainId != chainId and refChainId not in self.chainNumberDict:
                                self.chainNumberDict[refChainId] = chainId
                    else:
                        _atomId, _, details = self.nefT.get_valid_star_atom(cifCompId, atomId)
                        if len(_atomId) > 0 and (details is None or _compId not in monDict3):
                            if (ligands == 1 or cifCompId in HEME_LIKE_RES_NAMES) and any(a[3] for a in chainAssign):
                                chainAssign.clear()
                            chainAssign.add((chainId, seqId, cifCompId, False))
                            if refChainId is not None and refChainId != chainId and refChainId not in self.chainNumberDict:
                                self.chainNumberDict[refChainId] = chainId

        if len(chainAssign) == 0:
            for ps in self.polySeq:
                if preferNonPoly:
                    continue
                chainId = ps['chain_id']
                if refChainId is not None and refChainId != chainId and refChainId in self.chainNumberDict:
                    if chainId != self.chainNumberDict[refChainId]:
                        continue
                if fixedChainId is not None and fixedChainId != chainId:
                    continue
                seqKey = (chainId, _seqId)
                if seqKey in self.__authToLabelSeq:
                    _, seqId = self.__authToLabelSeq[seqKey]
                    if seqId in ps['seq_id']:
                        idx = ps['seq_id'].index(seqId)
                        cifCompId = ps['comp_id'][idx]
                        origCompId = ps['auth_comp_id'][idx]
                        if comp_id_unmatched_with(ps, cifCompId):
                            continue
                        if cifCompId != compId:
                            compIds = [_compId for _seqId, _compId in zip(ps['auth_seq_id'], ps['comp_id']) if _seqId == seqId]
                            if compId in compIds:
                                cifCompId = compId
                                origCompId = next(origCompId for _seqId, _compId, origCompId in zip(ps['auth_seq_id'], ps['comp_id'], ps['auth_comp_id'])
                                                  if _seqId == seqId and _compId == compId)
                        if self.__mrAtomNameMapping is not None and origCompId not in monDict3:
                            _, coordAtomSite = self.getCoordAtomSiteOf(chainId, _seqId, cifCompId, cifCheck=self.__hasCoord)
                            atomId = retrieveAtomIdFromMRMap(self.ccU, self.__mrAtomNameMapping, seqId, origCompId, atomId, coordAtomSite)
                        if compId in (cifCompId, origCompId, 'MTS', 'ORI'):
                            if len(self.nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                                chainAssign.add((ps['auth_chain_id'], _seqId, cifCompId, True))
                                if refChainId is not None and refChainId != chainId and refChainId not in self.chainNumberDict:
                                    self.chainNumberDict[refChainId] = chainId
                        else:
                            _atomId, _, details = self.nefT.get_valid_star_atom(cifCompId, atomId)
                            if len(_atomId) > 0 and (details is None or _compId not in monDict3):
                                chainAssign.add((ps['auth_chain_id'], _seqId, cifCompId, True))
                                if refChainId is not None and refChainId != chainId and refChainId not in self.chainNumberDict:
                                    self.chainNumberDict[refChainId] = chainId

            if self.hasNonPolySeq:
                for np in self.nonPolySeq:
                    chainId = np['auth_chain_id']
                    if refChainId is not None and refChainId != chainId and refChainId in self.chainNumberDict:
                        if chainId != self.chainNumberDict[refChainId]:
                            continue
                    if fixedChainId is not None and fixedChainId != chainId:
                        continue
                    if comp_id_in_polymer(np):
                        continue
                    seqKey = (chainId, _seqId)
                    if seqKey in self.__authToLabelSeq:
                        _, seqId = self.__authToLabelSeq[seqKey]
                        if seqId in np['seq_id']:
                            idx = np['seq_id'].index(seqId)
                            cifCompId = np['comp_id'][idx]
                            origCompId = np['auth_comp_id'][idx]
                            if self.__mrAtomNameMapping is not None and origCompId not in monDict3:
                                _, coordAtomSite = self.getCoordAtomSiteOf(chainId, _seqId, cifCompId, cifCheck=self.__hasCoord)
                                atomId = retrieveAtomIdFromMRMap(self.ccU, self.__mrAtomNameMapping, seqId, origCompId, atomId, coordAtomSite)
                            if compId in (cifCompId, origCompId, 'MTS', 'ORI'):
                                if len(self.nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                                    chainAssign.add((np['auth_chain_id'], _seqId, cifCompId, False))
                                    if refChainId is not None and refChainId != chainId and refChainId not in self.chainNumberDict:
                                        self.chainNumberDict[refChainId] = chainId
                            else:
                                _atomId, _, details = self.nefT.get_valid_star_atom(cifCompId, atomId)
                                if len(_atomId) > 0 and (details is None or _compId not in monDict3):
                                    chainAssign.add((np['auth_chain_id'], _seqId, cifCompId, False))
                                    if refChainId is not None and refChainId != chainId and refChainId not in self.chainNumberDict:
                                        self.chainNumberDict[refChainId] = chainId

        if len(chainAssign) == 0 and self.__altPolySeq is not None:
            for ps in self.__altPolySeq:
                if preferNonPoly:
                    continue
                chainId = ps['auth_chain_id']
                if fixedChainId is None and refChainId is not None and refChainId != chainId and refChainId in self.chainNumberDict:
                    if chainId != self.chainNumberDict[refChainId]:
                        continue
                if fixedChainId is not None:
                    if fixedChainId != chainId:
                        continue
                    if fixedSeqId is not None:
                        _seqId = fixedSeqId
                elif fixedSeqId is not None:
                    _seqId = fixedSeqId
                if _seqId in ps['auth_seq_id']:
                    cifCompId = ps['comp_id'][ps['auth_seq_id'].index(_seqId)]
                    if comp_id_unmatched_with(ps, cifCompId):
                        continue
                    if cifCompId != compId:
                        if cifCompId in monDict3 and compId in monDict3:
                            continue
                        compIds = [_compId for _seqId, _compId in zip(ps['auth_seq_id'], ps['comp_id']) if _seqId == seqId]
                        if compId in compIds:
                            cifCompId = compId
                    chainAssign.add((chainId, _seqId, cifCompId, True))
                    if refChainId is not None and refChainId != chainId and refChainId not in self.chainNumberDict:
                        self.chainNumberDict[refChainId] = chainId

        if len(chainAssign) == 0 and (self.__preferAuthSeqCount - self.__preferLabelSeqCount < MAX_PREF_LABEL_SCHEME_COUNT or len(self.polySeq) > 1):
            for ps in self.polySeq:
                if preferNonPoly:
                    continue
                chainId = ps['chain_id']
                if refChainId is not None and refChainId != chainId and refChainId in self.chainNumberDict:
                    if chainId != self.chainNumberDict[refChainId]:
                        continue
                if fixedChainId is not None and fixedChainId != chainId:
                    continue
                seqKey = (chainId, _seqId)
                if seqKey in self.__labelToAuthSeq:
                    _, seqId = self.__labelToAuthSeq[seqKey]
                    if seqId in ps['auth_seq_id']:
                        idx = ps['seq_id'].index(_seqId)
                        cifCompId = ps['comp_id'][idx]
                        origCompId = ps['auth_comp_id'][idx]
                        if comp_id_unmatched_with(ps, cifCompId):
                            continue
                        if cifCompId != compId:
                            compIds = [_compId for _seqId, _compId in zip(ps['auth_seq_id'], ps['comp_id']) if _seqId == seqId]
                            if compId in compIds:
                                cifCompId = compId
                                origCompId = next(origCompId for _seqId, _compId, origCompId in zip(ps['auth_seq_id'], ps['comp_id'], ps['auth_comp_id'])
                                                  if _seqId == seqId and _compId == compId)
                        if self.__mrAtomNameMapping is not None and origCompId not in monDict3:
                            _, coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, cifCompId, cifCheck=self.__hasCoord)
                            atomId = retrieveAtomIdFromMRMap(self.ccU, self.__mrAtomNameMapping, seqId, origCompId, atomId, coordAtomSite)
                        if compId in (cifCompId, origCompId, 'MTS', 'ORI'):
                            if len(self.nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                                chainAssign.add((ps['auth_chain_id'], seqId, cifCompId, True))
                                if compId in (cifCompId, origCompId):
                                    self.__authSeqId = 'label_seq_id'
                                    self.__setLocalSeqScheme()
                                    if refChainId is not None and refChainId != chainId and refChainId not in self.chainNumberDict:
                                        self.chainNumberDict[refChainId] = chainId
                        else:
                            _atomId, _, details = self.nefT.get_valid_star_atom(cifCompId, atomId)
                            if len(_atomId) > 0 and (details is None or _compId not in monDict3):
                                chainAssign.add((ps['auth_chain_id'], seqId, cifCompId, True))
                                self.__authSeqId = 'label_seq_id'
                                self.__setLocalSeqScheme()
                                if refChainId is not None and refChainId != chainId and refChainId not in self.chainNumberDict:
                                    self.chainNumberDict[refChainId] = chainId

        if len(chainAssign) == 0:
            if seqId == 1 or (refChainId, seqId - 1) in self.__coordUnobsRes:
                if atomId in aminoProtonCode and atomId != 'H1':
                    return self.assignCoordPolymerSequenceWithChainId(refChainId, seqId, compId, 'H1', index)
            else:
                auth_seq_id_list = list(filter(None, self.polySeq[0]['auth_seq_id']))
                min_auth_seq_id = max_auth_seq_id = UNREAL_AUTH_SEQ_NUM
                if len(auth_seq_id_list) > 0:
                    min_auth_seq_id = min(auth_seq_id_list)
                    max_auth_seq_id = max(auth_seq_id_list)
                if len(self.polySeq) == 1\
                   and (seqId < 1
                        or (compId == 'ACE' and seqId == min_auth_seq_id - 1)
                        or (compId == 'NH2' and seqId == max_auth_seq_id + 1)
                        or (compId in monDict3 and self.__preferAuthSeqCount - self.__preferLabelSeqCount >= MAX_PREF_LABEL_SCHEME_COUNT)):
                    refChainId = self.polySeq[0]['auth_chain_id']
                    if (compId == 'ACE' and seqId == min_auth_seq_id - 1)\
                       or (compId == 'NH2' and seqId == max_auth_seq_id + 1)\
                       or (compId in monDict3 and self.__preferAuthSeqCount - self.__preferLabelSeqCount >= MAX_PREF_LABEL_SCHEME_COUNT
                           and (min_auth_seq_id - MAX_ALLOWED_EXT_SEQ <= seqId < min_auth_seq_id
                                or max_auth_seq_id < seqId <= max_auth_seq_id + MAX_ALLOWED_EXT_SEQ)):
                        self.f.append(f"[Sequence mismatch warning] {self.getCurrentRestraint(n=index)}"
                                      f"The residue '{_seqId}:{_compId}' is not present in polymer sequence "
                                      f"of chain {refChainId} of the coordinates. "
                                      "Please update the sequence in the Macromolecules page.")
                        resKey = (_seqId, _compId)
                        if resKey not in self.extResKey:
                            self.extResKey.append(resKey)
                        chainAssign.add((refChainId, _seqId, compId, True))
                        asis = True
                    elif compId in monDict3 and self.__preferAuthSeqCount - self.__preferLabelSeqCount >= MAX_PREF_LABEL_SCHEME_COUNT:
                        self.f.append(f"[Sequence mismatch warning] {self.getCurrentRestraint(n=index)}"
                                      f"The residue '{_seqId}:{_compId}' is not present in polymer sequence "
                                      f"of chain {refChainId} of the coordinates. "
                                      "Please update the sequence in the Macromolecules page.")
                        resKey = (_seqId, _compId)
                        if resKey not in self.extResKey:
                            self.extResKey.append(resKey)
                    elif self.no_extra_comment:
                        self.f.append(f"[Atom not found] {self.getCurrentRestraint(n=index)}"
                                      f"{_seqId}:{_compId}:{atomId} is not present in the coordinates. "
                                      f"The residue number '{_seqId}' is not present in polymer sequence "
                                      f"of chain {refChainId} of the coordinates. "
                                      "Please update the sequence in the Macromolecules page.")
                else:
                    ext_seq = False
                    if (compId in monDict3 or compId in ('ACE', 'NH2')) and self.__preferAuthSeqCount - self.__preferLabelSeqCount >= MAX_PREF_LABEL_SCHEME_COUNT:
                        refChainIds = []
                        _auth_seq_id_list = auth_seq_id_list
                        for idx, ps in enumerate(self.polySeq):
                            if idx > 0:
                                auth_seq_id_list = list(filter(None, ps['auth_seq_id']))
                                _auth_seq_id_list.extend(auth_seq_id_list)
                            if len(auth_seq_id_list) > 0:
                                if idx > 0:
                                    min_auth_seq_id = min(auth_seq_id_list)
                                    max_auth_seq_id = max(auth_seq_id_list)
                                if min_auth_seq_id - MAX_ALLOWED_EXT_SEQ <= seqId < min_auth_seq_id\
                                   and (compId in monDict3 or (compId == 'ACE' and seqId == min_auth_seq_id - 1)):
                                    refChainIds.append(ps['auth_chain_id'])
                                    ext_seq = True
                                if max_auth_seq_id < seqId <= max_auth_seq_id + MAX_ALLOWED_EXT_SEQ\
                                   and (compId in monDict3 or (compId == 'NH2' and seqId == max_auth_seq_id + 1)):
                                    refChainIds.append(ps['auth_chain_id'])
                                    ext_seq = True
                        if ext_seq and seqId in _auth_seq_id_list:
                            ext_seq = False
                    if ext_seq:
                        refChainId = refChainIds[0] if len(refChainIds) == 1 else refChainIds
                        self.f.append(f"[Sequence mismatch warning] {self.getCurrentRestraint(n=index)}"
                                      f"The residue '{_seqId}:{_compId}' is not present in polymer sequence "
                                      f"of chain {refChainId} of the coordinates. "
                                      "Please update the sequence in the Macromolecules page.")
                        resKey = (_seqId, _compId)
                        if resKey not in self.extResKey:
                            self.extResKey.append(resKey)
                        if isinstance(refChainId, str):
                            chainAssign.add((refChainId, _seqId, compId, True))
                        else:
                            for _refChainId in refChainIds:
                                chainAssign.add((_refChainId, _seqId, compId, True))
                        asis = True
                    elif self.no_extra_comment:
                        self.f.append(f"[Atom not found] {self.getCurrentRestraint(n=index)}"
                                      f"{_seqId}:{_compId}:{atomId} is not present in the coordinates.")
                    updatePolySeqRst(self.polySeqRstFailed, str(refChainId), _seqId, compId, _compId)

        elif any(ca for ca in chainAssign if ca[0] == refChainId) and any(ca for ca in chainAssign if ca[0] != refChainId):
            _chainAssign = copy.copy(chainAssign)
            for _ca in _chainAssign:
                if _ca[0] != refChainId:
                    chainAssign.remove(_ca)

        return list(chainAssign), asis

    def assignCoordPolymerSequenceWithoutCompId(self, seqId: int, atomId: str, index: int
                                                ) -> List[Tuple[str, int, str, bool]]:
        """ Assign polymer sequences of the coordinates.
        """

        chainAssign = set()
        _seqId = seqId

        fixedChainId = fixedSeqId = fixedCompId = None

        self.__allow_ext_seq = False

        if self.reasons is not None:
            if 'branched_remap' in self.reasons and seqId in self.reasons['branched_remap']:
                fixedChainId, fixedSeqId = retrieveRemappedChainId(self.reasons['branched_remap'], seqId)
            if 'chain_id_remap' in self.reasons and seqId in self.reasons['chain_id_remap']:
                fixedChainId, fixedSeqId = retrieveRemappedChainId(self.reasons['chain_id_remap'], seqId)
            elif 'chain_id_clone' in self.reasons and seqId in self.reasons['chain_id_clone']:
                fixedChainId, fixedSeqId = retrieveRemappedChainId(self.reasons['chain_id_clone'], seqId)
            if fixedSeqId is not None:
                seqId = _seqId = fixedSeqId

        for ps in self.polySeq:
            chainId, seqId, cifCompId = self.getRealChainSeqId(ps, _seqId, None)
            if self.reasons is not None:
                if 'seq_id_remap' not in self.reasons\
                   and 'chain_seq_id_remap' not in self.reasons\
                   and 'ext_chain_seq_id_remap' not in self.reasons:
                    if fixedChainId is not None and fixedChainId != chainId:
                        continue
                else:
                    if 'ext_chain_seq_id_remap' in self.reasons:
                        fixedChainId, fixedSeqId, fixedCompId =\
                            retrieveRemappedSeqIdAndCompId(self.reasons['ext_chain_seq_id_remap'], chainId, seqId)
                        if fixedChainId is not None and fixedChainId != chainId:
                            continue
                        if fixedSeqId is not None:
                            self.__allow_ext_seq = fixedCompId is not None
                            seqId = _seqId = fixedSeqId
                    if fixedSeqId is None and 'chain_seq_id_remap' in self.reasons:
                        fixedChainId, fixedSeqId = retrieveRemappedSeqId(self.reasons['chain_seq_id_remap'], chainId, seqId)
                        if fixedChainId is not None and fixedChainId != chainId:
                            continue
                        if fixedSeqId is not None:
                            seqId = _seqId = fixedSeqId
                    if fixedSeqId is None and 'seq_id_remap' in self.reasons:
                        _, fixedSeqId = retrieveRemappedSeqId(self.reasons['seq_id_remap'], chainId, seqId)
                        if fixedSeqId is not None:
                            seqId = _seqId = fixedSeqId
            if seqId in ps['auth_seq_id'] or fixedCompId is not None:
                if fixedCompId is not None:
                    cifCompId = fixedCompId
                else:
                    if cifCompId is not None:
                        idx = next((_idx for _idx, (_seqId_, _cifCompId_) in enumerate(zip(ps['auth_seq_id'], ps['comp_id']))
                                    if _seqId_ == seqId and _cifCompId_ == cifCompId), ps['auth_seq_id'].index(seqId))
                    else:
                        idx = ps['auth_seq_id'].index(seqId) if seqId in ps['auth_seq_id'] else ps['seq_id'].index(seqId)
                    cifCompId = ps['comp_id'][idx]
                if self.reasons is not None:
                    if 'non_poly_remap' in self.reasons and cifCompId in self.reasons['non_poly_remap']\
                       and seqId in self.reasons['non_poly_remap'][cifCompId]:
                        fixedChainId, fixedSeqId = retrieveRemappedNonPoly(self.reasons['non_poly_remap'], chainId, seqId, cifCompId)
                        if fixedSeqId is not None:
                            seqId = _seqId = fixedSeqId
                        if (fixedChainId is not None and fixedChainId != chainId) or seqId not in ps['auth_seq_id']:
                            continue
                updatePolySeqRst(self.polySeqRst, chainId, _seqId, cifCompId)
                if atomId is None or len(self.nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                    chainAssign.add((chainId, seqId, cifCompId, True))
            elif 'gap_in_auth_seq' in ps and ps['gap_in_auth_seq']:
                auth_seq_id_list = list(filter(None, ps['auth_seq_id']))
                if len(auth_seq_id_list) > 0:
                    min_auth_seq_id = min(auth_seq_id_list)
                    max_auth_seq_id = max(auth_seq_id_list)
                    if min_auth_seq_id <= seqId <= max_auth_seq_id:
                        _seqId_ = seqId + 1
                        while _seqId_ <= max_auth_seq_id:
                            if _seqId_ in ps['auth_seq_id']:
                                break
                            _seqId_ += 1
                        if _seqId_ not in ps['auth_seq_id']:
                            _seqId_ = seqId - 1
                            while _seqId_ >= min_auth_seq_id:
                                if _seqId_ in ps['auth_seq_id']:
                                    break
                                _seqId_ -= 1
                        if _seqId_ in ps['auth_seq_id']:
                            idx = ps['auth_seq_id'].index(_seqId_) - (_seqId_ - seqId)
                            try:
                                seqId_ = ps['auth_seq_id'][idx]
                                cifCompId = ps['comp_id'][idx]
                                updatePolySeqRst(self.polySeqRst, chainId, _seqId, cifCompId)
                                if atomId is None or len(self.nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                                    chainAssign.add((chainId, seqId_, cifCompId, True))
                            except IndexError:
                                pass

        if self.hasNonPolySeq:
            for np in self.nonPolySeq:
                chainId, seqId, cifCompId = self.getRealChainSeqId(np, _seqId, None, False)
                if self.reasons is not None:
                    if 'seq_id_remap' not in self.reasons and 'chain_seq_id_remap' not in self.reasons:
                        if fixedChainId is not None and fixedChainId != chainId:
                            continue
                    else:
                        if 'chain_seq_id_remap' in self.reasons:
                            fixedChainId, fixedSeqId = retrieveRemappedSeqId(self.reasons['chain_seq_id_remap'], chainId, seqId)
                            if fixedChainId is not None and fixedChainId != chainId:
                                continue
                            if fixedSeqId is not None:
                                seqId = _seqId = fixedSeqId
                        if fixedSeqId is None and 'seq_id_remap' in self.reasons:
                            _, fixedSeqId = retrieveRemappedSeqId(self.reasons['seq_id_remap'], chainId, seqId)
                            if fixedSeqId is not None:
                                seqId = _seqId = fixedSeqId
                if seqId in np['auth_seq_id']:
                    if cifCompId is not None:
                        idx = next((_idx for _idx, (_seqId_, _cifCompId_) in enumerate(zip(np['auth_seq_id'], np['comp_id']))
                                    if _seqId_ == seqId and _cifCompId_ == cifCompId), np['auth_seq_id'].index(seqId))
                    else:
                        idx = np['auth_seq_id'].index(seqId) if seqId in np['auth_seq_id'] else np['seq_id'].index(seqId)
                    cifCompId = np['comp_id'][idx]
                    updatePolySeqRst(self.polySeqRst, chainId, _seqId, cifCompId)
                    if atomId is None or len(self.nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                        chainAssign.add((chainId, seqId, cifCompId, False))

        if len(chainAssign) == 0:
            for ps in self.polySeq:
                chainId = ps['chain_id']
                if fixedChainId is not None and fixedChainId != chainId:
                    continue
                seqKey = (chainId, _seqId)
                if seqKey in self.__authToLabelSeq:
                    _, seqId = self.__authToLabelSeq[seqKey]
                    if seqId in ps['seq_id']:
                        cifCompId = ps['comp_id'][ps['seq_id'].index(seqId)]
                        updatePolySeqRst(self.polySeqRst, chainId, _seqId, cifCompId)
                        if atomId is None or len(self.nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                            chainAssign.add((ps['auth_chain_id'], _seqId, cifCompId, True))

            if self.hasNonPolySeq:
                for np in self.nonPolySeq:
                    chainId = np['auth_chain_id']
                    if fixedChainId is not None and fixedChainId != chainId:
                        continue
                    seqKey = (chainId, _seqId)
                    if seqKey in self.__authToLabelSeq:
                        _, seqId = self.__authToLabelSeq[seqKey]
                        if seqId in np['seq_id']:
                            cifCompId = np['comp_id'][np['seq_id'].index(seqId)]
                            updatePolySeqRst(self.polySeqRst, chainId, _seqId, cifCompId)
                            if atomId is None or len(self.nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                                chainAssign.add((np['auth_chain_id'], _seqId, cifCompId, False))

        if len(chainAssign) == 0 and self.__altPolySeq is not None:
            for ps in self.__altPolySeq:
                chainId = ps['auth_chain_id']
                if fixedChainId is not None and fixedChainId != chainId:
                    continue
                if _seqId in ps['auth_seq_id']:
                    cifCompId = ps['comp_id'][ps['auth_seq_id'].index(_seqId)]
                    updatePolySeqRst(self.polySeqRst, chainId, _seqId, cifCompId)
                    chainAssign.add((chainId, _seqId, cifCompId, True))

        if len(chainAssign) == 0 and (self.__preferAuthSeqCount - self.__preferLabelSeqCount < MAX_PREF_LABEL_SCHEME_COUNT or len(self.polySeq) > 1):
            for ps in self.polySeq:
                chainId = ps['chain_id']
                if fixedChainId is not None and fixedChainId != chainId:
                    continue
                seqKey = (chainId, _seqId)
                if seqKey in self.__labelToAuthSeq:
                    _, seqId = self.__labelToAuthSeq[seqKey]
                    if seqId in ps['auth_seq_id']:
                        cifCompId = ps['comp_id'][ps['auth_seq_id'].index(seqId)]
                        updatePolySeqRst(self.polySeqRst, chainId, seqId, cifCompId)
                        if atomId is None or len(self.nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                            chainAssign.add((ps['auth_chain_id'], seqId, cifCompId, True))
                            self.__authSeqId = 'label_seq_id'
                            self.__setLocalSeqScheme()

        if len(chainAssign) == 0:
            if seqId == 1 or (chainId if fixedChainId is None else fixedChainId, seqId - 1) in self.__coordUnobsRes:
                if atomId is not None and atomId in aminoProtonCode and atomId != 'H1':
                    return self.assignCoordPolymerSequenceWithoutCompId(seqId, 'H1', index)
            if atomId is not None and (('-' in atomId and ':' in atomId) or '.' in atomId):
                if self.no_extra_comment:
                    self.f.append(f"[Atom not found] {self.getCurrentRestraint(n=index)}"
                                  f"{_seqId}:?:{atomId} is not present in the coordinates.")
            elif atomId is not None:
                if len(self.polySeq) == 1 and seqId < 1:
                    refChainId = self.polySeq[0]['auth_chain_id']
                    if self.no_extra_comment:
                        self.f.append(f"[Atom not found] {self.getCurrentRestraint(n=index)}"
                                      f"{_seqId}:?:{atomId} is not present in the coordinates. "
                                      f"The residue number '{_seqId}' is not present in polymer sequence "
                                      f"of chain {refChainId} of the coordinates. "
                                      "Please update the sequence in the Macromolecules page.")
                else:
                    if self.no_extra_comment:
                        self.f.append(f"[Atom not found] {self.getCurrentRestraint(n=index)}"
                                      f"{_seqId}:{atomId} is not present in the coordinates.")
                    compIds = guessCompIdFromAtomId([atomId], self.polySeq, self.nefT)
                    if compIds is not None:
                        chainId = fixedChainId
                        if chainId is None and len(self.polySeq) == 1:
                            chainId = self.polySeq[0]['chain_id']
                        if chainId is not None:
                            if len(compIds) == 1:
                                updatePolySeqRst(self.polySeqRstFailed, chainId, seqId, compIds[0])
                            else:
                                updatePolySeqRstAmbig(self.polySeqRstFailedAmbig, chainId, seqId, compIds)

        return list(chainAssign)

    def assignCoordPolymerSequenceWithChainIdWithoutCompId(self, fixedChainId: str, seqId: int, atomId: str, index: int
                                                           ) -> List[Tuple[str, int, str, bool]]:
        """ Assign polymer sequences of the coordinates.
        """

        chainAssign = set()
        _seqId = seqId

        fixedSeqId = fixedCompId = None

        self.__allow_ext_seq = False

        if self.reasons is not None:
            if 'branched_remap' in self.reasons and seqId in self.reasons['branched_remap']:
                fixedChainId, fixedSeqId = retrieveRemappedChainId(self.reasons['branched_remap'], seqId)
            if 'chain_id_remap' in self.reasons and seqId in self.reasons['chain_id_remap']:
                fixedChainId, fixedSeqId = retrieveRemappedChainId(self.reasons['chain_id_remap'], seqId)
            elif 'chain_id_clone' in self.reasons and seqId in self.reasons['chain_id_clone']:
                fixedChainId, fixedSeqId = retrieveRemappedChainId(self.reasons['chain_id_clone'], seqId)
            if fixedSeqId is not None:
                seqId = _seqId = fixedSeqId

        for ps in self.polySeq:
            chainId, seqId, cifCompId = self.getRealChainSeqId(ps, _seqId, None)
            if chainId != fixedChainId:
                continue
            if self.reasons is not None:
                if 'seq_id_remap' not in self.reasons\
                   and 'chain_seq_id_remap' not in self.reasons\
                   and 'ext_chain_seq_id_remap' not in self.reasons:
                    if fixedChainId is not None and fixedChainId != chainId:
                        continue
                else:
                    if 'ext_chain_seq_id_remap' in self.reasons:
                        fixedChainId, fixedSeqId, fixedCompId =\
                            retrieveRemappedSeqIdAndCompId(self.reasons['ext_chain_seq_id_remap'], chainId, seqId)
                        if fixedChainId is not None and fixedChainId != chainId:
                            continue
                        if fixedSeqId is not None:
                            self.__allow_ext_seq = fixedCompId is not None
                            seqId = _seqId = fixedSeqId
                    if fixedSeqId is None and 'chain_seq_id_remap' in self.reasons:
                        fixedChainId, fixedSeqId = retrieveRemappedSeqId(self.reasons['chain_seq_id_remap'], chainId, seqId)
                        if fixedChainId is not None and fixedChainId != chainId:
                            continue
                        if fixedSeqId is not None:
                            seqId = _seqId = fixedSeqId
                    if fixedSeqId is None and 'seq_id_remap' in self.reasons:
                        _, fixedSeqId = retrieveRemappedSeqId(self.reasons['seq_id_remap'], chainId, seqId)
                        if fixedSeqId is not None:
                            seqId = _seqId = fixedSeqId
            if seqId in ps['auth_seq_id'] or fixedCompId is not None:
                if fixedCompId is not None:
                    cifCompId = fixedCompId
                else:
                    if cifCompId is not None:
                        idx = next((_idx for _idx, (_seqId_, _cifCompId_) in enumerate(zip(ps['auth_seq_id'], ps['comp_id']))
                                    if _seqId_ == seqId and _cifCompId_ == cifCompId), ps['auth_seq_id'].index(seqId))
                    else:
                        idx = ps['auth_seq_id'].index(seqId) if seqId in ps['auth_seq_id'] else ps['seq_id'].index(seqId)
                    cifCompId = ps['comp_id'][idx]
                if self.reasons is not None:
                    if 'non_poly_remap' in self.reasons and cifCompId in self.reasons['non_poly_remap']\
                       and seqId in self.reasons['non_poly_remap'][cifCompId]:
                        fixedChainId, fixedSeqId = retrieveRemappedNonPoly(self.reasons['non_poly_remap'], chainId, seqId, cifCompId)
                        if fixedSeqId is not None:
                            seqId = _seqId = fixedSeqId
                        if (fixedChainId is not None and fixedChainId != chainId) or seqId not in ps['auth_seq_id']:
                            continue
                updatePolySeqRst(self.polySeqRst, fixedChainId, _seqId, cifCompId)
                if len(self.nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                    chainAssign.add((chainId, seqId, cifCompId, True))
            elif 'gap_in_auth_seq' in ps and ps['gap_in_auth_seq']:
                auth_seq_id_list = list(filter(None, ps['auth_seq_id']))
                if len(auth_seq_id_list) > 0:
                    min_auth_seq_id = min(auth_seq_id_list)
                    max_auth_seq_id = max(auth_seq_id_list)
                    if min_auth_seq_id <= seqId <= max_auth_seq_id:
                        _seqId_ = seqId + 1
                        while _seqId_ <= max_auth_seq_id:
                            if _seqId_ in ps['auth_seq_id']:
                                break
                            _seqId_ += 1
                        if _seqId_ not in ps['auth_seq_id']:
                            _seqId_ = seqId - 1
                            while _seqId_ >= min_auth_seq_id:
                                if _seqId_ in ps['auth_seq_id']:
                                    break
                                _seqId_ -= 1
                        if _seqId_ in ps['auth_seq_id']:
                            idx = ps['auth_seq_id'].index(_seqId_) - (_seqId_ - seqId)
                            try:
                                seqId_ = ps['auth_seq_id'][idx]
                                cifCompId = ps['comp_id'][idx]
                                updatePolySeqRst(self.polySeqRst, fixedChainId, _seqId, cifCompId)
                                if len(self.nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                                    chainAssign.add((chainId, seqId_, cifCompId, True))
                            except IndexError:
                                pass

        if self.hasNonPolySeq:
            for np in self.nonPolySeq:
                chainId, seqId, cifCompId = self.getRealChainSeqId(np, _seqId, None, False)
                if chainId != fixedChainId:
                    continue
                if self.reasons is not None:
                    if 'seq_id_remap' not in self.reasons and 'chain_seq_id_remap' not in self.reasons:
                        if fixedChainId is not None and fixedChainId != chainId:
                            continue
                    else:
                        if 'chain_seq_id_remap' in self.reasons:
                            fixedChainId, fixedSeqId = retrieveRemappedSeqId(self.reasons['chain_seq_id_remap'], chainId, seqId)
                            if fixedChainId is not None and fixedChainId != chainId:
                                continue
                            if fixedSeqId is not None:
                                seqId = _seqId = fixedSeqId
                        if fixedSeqId is None and 'seq_id_remap' in self.reasons:
                            _, fixedSeqId = retrieveRemappedSeqId(self.reasons['seq_id_remap'], chainId, seqId)
                            if fixedSeqId is not None:
                                seqId = _seqId = fixedSeqId
                if seqId in np['auth_seq_id']:
                    if cifCompId is not None:
                        idx = next((_idx for _idx, (_seqId_, _cifCompId_) in enumerate(zip(np['auth_seq_id'], np['comp_id']))
                                    if _seqId_ == seqId and _cifCompId_ == cifCompId), np['auth_seq_id'].index(seqId))
                    else:
                        idx = np['auth_seq_id'].index(seqId) if seqId in np['auth_seq_id'] else np['seq_id'].index(seqId)
                    cifCompId = np['comp_id'][idx]
                    updatePolySeqRst(self.polySeqRst, fixedChainId, _seqId, cifCompId)
                    if len(self.nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                        chainAssign.add((chainId, seqId, cifCompId, False))

        if len(chainAssign) == 0:
            for ps in self.polySeq:
                chainId = ps['chain_id']
                if chainId != fixedChainId:
                    continue
                seqKey = (chainId, _seqId)
                if seqKey in self.__authToLabelSeq:
                    _, seqId = self.__authToLabelSeq[seqKey]
                    if seqId in ps['seq_id']:
                        cifCompId = ps['comp_id'][ps['seq_id'].index(seqId)]
                        updatePolySeqRst(self.polySeqRst, fixedChainId, _seqId, cifCompId)
                        if len(self.nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                            chainAssign.add((ps['auth_chain_id'], _seqId, cifCompId, True))

            if self.hasNonPolySeq:
                for np in self.nonPolySeq:
                    chainId = np['auth_chain_id']
                    if chainId != fixedChainId:
                        continue
                    seqKey = (chainId, _seqId)
                    if seqKey in self.__authToLabelSeq:
                        _, seqId = self.__authToLabelSeq[seqKey]
                        if seqId in np['seq_id']:
                            cifCompId = np['comp_id'][np['seq_id'].index(seqId)]
                            updatePolySeqRst(self.polySeqRst, fixedChainId, _seqId, cifCompId)
                            if len(self.nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                                chainAssign.add((np['auth_chain_id'], _seqId, cifCompId, False))

        if len(chainAssign) == 0 and self.__altPolySeq is not None:
            for ps in self.__altPolySeq:
                chainId = ps['auth_chain_id']
                if chainId != fixedChainId:
                    continue
                if _seqId in ps['auth_seq_id']:
                    cifCompId = ps['comp_id'][ps['auth_seq_id'].index(_seqId)]
                    updatePolySeqRst(self.polySeqRst, fixedChainId, _seqId, cifCompId)
                    chainAssign.add((chainId, _seqId, cifCompId, True))

        if len(chainAssign) == 0 and (self.__preferAuthSeqCount - self.__preferLabelSeqCount < MAX_PREF_LABEL_SCHEME_COUNT or len(self.polySeq) > 1):
            for ps in self.polySeq:
                chainId = ps['chain_id']
                if chainId != fixedChainId:
                    continue
                seqKey = (chainId, _seqId)
                if seqKey in self.__labelToAuthSeq:
                    _, seqId = self.__labelToAuthSeq[seqKey]
                    if seqId in ps['auth_seq_id']:
                        cifCompId = ps['comp_id'][ps['auth_seq_id'].index(seqId)]
                        updatePolySeqRst(self.polySeqRst, fixedChainId, seqId, cifCompId)
                        if len(self.nefT.get_valid_star_atom(cifCompId, atomId)[0]) > 0:
                            chainAssign.add((ps['auth_chain_id'], seqId, cifCompId, True))
                            self.__authSeqId = 'label_seq_id'
                            self.__setLocalSeqScheme()

        if len(chainAssign) == 0:
            if seqId == 1 or (fixedChainId, seqId - 1) in self.__coordUnobsRes:
                if atomId in aminoProtonCode and atomId != 'H1':
                    return self.assignCoordPolymerSequenceWithChainIdWithoutCompId(fixedChainId, seqId, 'H1', index)
            if (('-' in atomId and ':' in atomId) or '.' in atomId):
                if self.no_extra_comment:
                    self.f.append(f"[Atom not found] {self.getCurrentRestraint(n=index)}"
                                  f"{fixedChainId}:{_seqId}:?:{atomId} is not present in the coordinates.")
            else:
                if len(self.polySeq) == 1 and seqId < 1:
                    refChainId = self.polySeq[0]['auth_chain_id']
                    if self.no_extra_comment:
                        self.f.append(f"[Atom not found] {self.getCurrentRestraint(n=index)}"
                                      f"{_seqId}:?:{atomId} is not present in the coordinates. "
                                      f"The residue number '{_seqId}' is not present in polymer sequence "
                                      f"of chain {refChainId} of the coordinates. "
                                      "Please update the sequence in the Macromolecules page.")
                else:
                    if self.no_extra_comment:
                        self.f.append(f"[Atom not found] {self.getCurrentRestraint(n=index)}"
                                      f"{fixedChainId}:{_seqId}:{atomId} is not present in the coordinates.")
                    compIds = guessCompIdFromAtomId([atomId], self.polySeq, self.nefT)
                    if compIds is not None:
                        if len(compIds) == 1:
                            updatePolySeqRst(self.polySeqRstFailed, fixedChainId, seqId, compIds[0])
                        else:
                            updatePolySeqRstAmbig(self.polySeqRstFailedAmbig, fixedChainId, seqId, compIds)

        return list(chainAssign)

    def selectCoordAtoms(self, chainAssign: List[Tuple[str, int, str, bool]], seqId: int, compId: str, atomId: str,
                         index: int, allowAmbig: bool = True, offset: int = 0):
        """ Select atoms of the coordinates.
        """

        atomSelection = []

        authAtomId = atomId

        __compId = compId
        __atomId = atomId

        if self.__mrAtomNameMapping is not None and compId not in monDict3:
            __atomId = retrieveAtomIdFromMRMap(self.ccU, self.__mrAtomNameMapping, seqId, compId, atomId)

        compId = self.translateToStdResNameWrapper(seqId, __compId)

        for chainId, cifSeqId, cifCompId, isPolySeq in chainAssign:

            if offset != 0:
                cifSeqId += offset
                cifCompId = compId

            seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, cifSeqId, cifCompId, asis=self.__preferAuthSeq)

            if self.__mrAtomNameMapping is not None and cifCompId not in monDict3:
                __atomId = retrieveAtomIdFromMRMap(self.ccU, self.__mrAtomNameMapping, cifSeqId, cifCompId, atomId, coordAtomSite)
                if atomId != __atomId and coordAtomSite is not None\
                   and (__atomId in coordAtomSite['atom_id'] or (__atomId.endswith('%') and __atomId[:-1] + '2' in coordAtomSite['atom_id'])):
                    atomId = __atomId
                elif self.reasons is not None and 'branched_remap' in self.reasons:
                    _seqId = retrieveOriginalSeqIdFromMRMap(self.reasons['branched_remap'], chainId, cifSeqId)
                    if _seqId != cifSeqId:
                        _, _, atomId = retrieveAtomIdentFromMRMap(self.ccU, self.__mrAtomNameMapping, _seqId, cifCompId, atomId, None, coordAtomSite)

            _atomId = []
            if not isPolySeq and atomId[0] in ('Q', 'M') and coordAtomSite is not None:
                key = (chainId, cifSeqId, compId, atomId)
                if key in self.__cachedDictForStarAtom:
                    _atomId = copy.deepcopy(self.__cachedDictForStarAtom[key])
                else:
                    pattern = re.compile(fr'H{atomId[1:]}\d+') if compId in monDict3 else re.compile(fr'H{atomId[1:]}\S?$')
                    atomIdList = [a for a in coordAtomSite['atom_id'] if re.search(pattern, a) and a[-1] in ('1', '2', '3')]
                    if len(atomIdList) > 1:
                        hvyAtomIdList = [a for a in coordAtomSite['atom_id'] if a[0] in ('C', 'N')]
                        hvyAtomId = None
                        for canHvyAtomId in hvyAtomIdList:
                            if isStructConn(self.cR, chainId, cifSeqId, canHvyAtomId, chainId, cifSeqId, atomIdList[0],
                                            representativeModelId=self.representativeModelId, representativeAltId=self.representativeAltId,
                                            modelNumName=self.modelNumName):
                                hvyAtomId = canHvyAtomId
                                break
                        if hvyAtomId is not None:
                            for _atomId_ in atomIdList:
                                if isStructConn(self.cR, chainId, cifSeqId, hvyAtomId, chainId, cifSeqId, _atomId_,
                                                representativeModelId=self.representativeModelId, representativeAltId=self.representativeAltId,
                                                modelNumName=self.modelNumName):
                                    _atomId.append(_atomId_)
                    if len(_atomId) > 1:
                        self.__cachedDictForStarAtom[key] = copy.deepcopy(_atomId)
            if len(_atomId) > 1:
                details = None
            else:
                _atomId, _, details = self.nefT.get_valid_star_atom_in_xplor(cifCompId, atomId, leave_unmatched=True)
                if details is not None:
                    if atomId != __atomId:
                        _atomId, _, details = self.nefT.get_valid_star_atom_in_xplor(cifCompId, __atomId, leave_unmatched=True)
                    elif len(atomId) > 1 and not atomId[-1].isalpha() and (atomId[0] in pseProBeginCode or atomId[0] in ('C', 'N', 'P', 'F')):
                        _atomId, _, details = self.nefT.get_valid_star_atom_in_xplor(cifCompId, atomId[:-1], leave_unmatched=True)
                        if atomId[-1].isdigit() and int(atomId[-1]) <= len(_atomId):
                            _atomId = [_atomId[int(atomId[-1]) - 1]]

            if details is not None or atomId.endswith('"'):
                _atomId_ = translateToStdAtomName(atomId, cifCompId, ccU=self.ccU)
                if _atomId_ != atomId:
                    if atomId.startswith('HT') and len(_atomId_) == 2:
                        _atomId_ = 'H'
                    __atomId__ = self.nefT.get_valid_star_atom_in_xplor(cifCompId, _atomId_)[0]
                    if coordAtomSite is not None:
                        if any(_atomId_ for _atomId_ in __atomId__ if _atomId_ in coordAtomSite['atom_id']):
                            _atomId = __atomId__
                        elif __atomId__[0][0] in protonBeginCode:
                            __bondedTo = self.ccU.getBondedAtoms(cifCompId, __atomId__[0])
                            if len(__bondedTo) > 0 and __bondedTo[0] in coordAtomSite['atom_id']:
                                _atomId = __atomId__
                elif coordAtomSite is not None:
                    _atomId = []
            # _atomId = self.nefT.get_valid_star_atom(cifCompId, atomId)[0]

            if coordAtomSite is not None\
               and not any(_atomId_ for _atomId_ in _atomId if _atomId_ in coordAtomSite['atom_id']):
                if atomId in coordAtomSite['atom_id']:
                    _atomId = [atomId]
                elif seqId == 1 and atomId == 'H1' and self.csStat.peptideLike(compId) and 'H' in coordAtomSite['atom_id']:
                    _atomId = ['H']

            if coordAtomSite is None and not isPolySeq and self.hasNonPolySeq:
                try:
                    for np in self.nonPolySeq:
                        if np['auth_chain_id'] == chainId and cifSeqId in np['auth_seq_id']:
                            cifSeqId = np['seq_id'][np['auth_seq_id'].index(cifSeqId)]
                            seqKey, coordAtomSite = self.getCoordAtomSiteOf(chainId, cifSeqId, cifCompId)
                            if coordAtomSite is not None:
                                break
                except ValueError:
                    pass

            if coordAtomSite is not None:
                atomSiteAtomId = coordAtomSite['atom_id']
                if len(_atomId) == 0 and __atomId in zincIonCode and 'ZN' in atomSiteAtomId:
                    compId = atomId = 'ZN'
                    _atomId = [atomId]
                elif len(_atomId) == 0 and __atomId in calciumIonCode and 'CA' in atomSiteAtomId:
                    compId = atomId = 'CA'
                    _atomId = [atomId]
                elif not any(_atomId_ in atomSiteAtomId for _atomId_ in _atomId):
                    pass
                elif atomId[0] not in pseProBeginCode and not all(_atomId in atomSiteAtomId for _atomId in _atomId):
                    _atomId = [_atomId_ for _atomId_ in _atomId if _atomId_ in atomSiteAtomId]

            lenAtomId = len(_atomId)
            if self.reasons is not None and compId != cifCompId and __compId == cifCompId:
                compId = cifCompId
            if compId != cifCompId and compId in monDict3 and cifCompId in monDict3:
                multiChain = insCode = False
                if len(chainAssign) > 0:
                    chainIds = [ca[0] for ca in chainAssign]
                    multiChain = len(collections.Counter(chainIds).most_common()) > 1
                ps = next((ps for ps in self.polySeq if ps['auth_chain_id'] == chainId), None)
                if ps is not None:
                    compIds = [_compId for _seqId, _compId in zip(ps['auth_seq_id'], ps['comp_id']) if _seqId == cifSeqId]
                    if compId in compIds:
                        insCode = True
                        cifCompId = compId
                if not multiChain and not insCode:
                    if self.__preferAuthSeq:
                        _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, cifSeqId, cifCompId, asis=False)
                        if _coordAtomSite is not None and _coordAtomSite['comp_id'] == compId:
                            if lenAtomId > 0 and _atomId[0] in _coordAtomSite['atom_id']:
                                self.__authSeqId = 'label_seq_id'
                                self.__setLocalSeqScheme()
                                continue
                    self.f.append(f"[Sequence mismatch] {self.getCurrentRestraint(n=index)}"
                                  f"Residue name {__compId!r} of the spectral peak list does not match with {chainId}:{cifSeqId}:{cifCompId} of the coordinates.")
                    continue

            if compId != cifCompId and compId in monDict3 and not isPolySeq:
                continue

            if lenAtomId == 0 and not isPolySeq and cifCompId in SYMBOLS_ELEMENT:
                _atomId = [cifCompId]
                lenAtomId = 1

            if lenAtomId == 0:
                if compId != cifCompId and any(item for item in chainAssign if item[2] == compId):
                    continue
                if seqId == 1 and isPolySeq and cifCompId == 'ACE' and cifCompId != compId and offset == 0:
                    self.selectCoordAtoms(chainAssign, seqId, compId, atomId, index, allowAmbig, offset=1)
                    return
                self.f.append(f"[Invalid atom nomenclature] {self.getCurrentRestraint(n=index)}"
                              f"{seqId}:{__compId}:{__atomId} is invalid atom nomenclature.")
                continue
            if lenAtomId > 1 and not allowAmbig:
                self.f.append(f"[Invalid atom selection] {self.getCurrentRestraint(n=index)}"
                              f"Ambiguous atom selection '{seqId}:{__compId}:{__atomId}' is not allowed as a angle restraint.")
                continue

            if __compId != cifCompId and __compId not in self.compIdMap:
                self.compIdMap[__compId] = cifCompId

            for cifAtomId in _atomId:

                if seqKey in self.__coordUnobsRes and cifCompId in monDict3 and self.reasons is not None and 'non_poly_remap' in self.reasons:
                    if self.ccU.updateChemCompDict(cifCompId):
                        try:
                            next(cca for cca in self.ccU.lastAtomList
                                 if cca[self.ccU.ccaAtomId] == cifAtomId and cca[self.ccU.ccaLeavingAtomFlag] != 'Y')
                        except StopIteration:
                            continue
                        try:
                            if len(authAtomId) > len(cifAtomId):
                                next(cca for cca in self.ccU.lastAtomList
                                     if cca[self.ccU.ccaAtomId] == authAtomId and cca[self.ccU.ccaLeavingAtomFlag] != 'Y')
                        except StopIteration:
                            break

                if authAtomId in ('H', 'HN') and cifAtomId in ('HN1', 'HN2', 'HNA') and self.csStat.peptideLike(cifCompId)\
                   and coordAtomSite is not None and cifAtomId not in coordAtomSite['atom_id']:
                    if cifAtomId in ('HN2', 'HNA'):
                        if 'H2' not in coordAtomSite['atom_id']:
                            continue
                        cifAtomId = 'H2'
                    if cifAtomId == 'HN1' and 'H' in coordAtomSite['atom_id']:
                        cifAtomId = 'H'

                atomSelection.append({'chain_id': chainId, 'seq_id': cifSeqId, 'comp_id': cifCompId,
                                      'atom_id': cifAtomId, 'auth_atom_id': authAtomId})

                self.testCoordAtomIdConsistency(chainId, cifSeqId, cifCompId, cifAtomId, seqKey, coordAtomSite, index)

        if len(atomSelection) > 0:
            self.atomSelectionSet.append(atomSelection)

    def testCoordAtomIdConsistency(self, chainId: str, seqId: int, compId: str, atomId: str,
                                   seqKey: Tuple[str, int], coordAtomSite: Optional[dict], index: int) -> Tuple[str, bool]:
        asis = False
        if not self.__hasCoord:
            return atomId, asis

        found = False

        if coordAtomSite is not None:
            if atomId in coordAtomSite['atom_id']:
                found = True
            elif atomId in ('HN1', 'HN2', 'HN3') and ((atomId[-1] + 'HN') in coordAtomSite['atom_id']
                                                      or ('H' + atomId[-1]) in coordAtomSite['atom_id']):
                atomId = atomId[-1] + 'HN' if atomId[-1] + 'HN' in coordAtomSite['atom_id'] else 'H' + atomId[-1]
                found = True
            elif 'alt_atom_id' in coordAtomSite and atomId in coordAtomSite['alt_atom_id']:
                found = True
                # self.__authAtomId = 'auth_atom_id'

            elif self.__preferAuthSeq:
                _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, compId, asis=False)
                if _coordAtomSite is not None and _coordAtomSite['comp_id'] == compId and not self.__extendAuthSeq:
                    if atomId in _coordAtomSite['atom_id']:
                        found = True
                        self.__preferAuthSeq = False
                        self.__authSeqId = 'label_seq_id'
                        seqKey = _seqKey
                        self.__setLocalSeqScheme()
                    elif atomId in ('HN1', 'HN2', 'HN3') and ((atomId[-1] + 'HN') in _coordAtomSite['atom_id']
                                                              or ('H' + atomId[-1]) in _coordAtomSite['atom_id']):
                        atomId = atomId[-1] + 'HN' if atomId[-1] + 'HN' in _coordAtomSite['atom_id'] else 'H' + atomId[-1]
                        found = True
                        self.__preferAuthSeq = False
                        self.__authSeqId = 'label_seq_id'
                        seqKey = _seqKey
                        self.__setLocalSeqScheme()
                    elif 'alt_atom_id' in _coordAtomSite and atomId in _coordAtomSite['alt_atom_id']:
                        found = True
                        self.__preferAuthSeq = False
                        self.__authSeqId = 'label_seq_id'
                        # self.__authAtomId = 'auth_atom_id'
                        seqKey = _seqKey
                        self.__setLocalSeqScheme()

            else:
                self.__preferAuthSeq = True
                _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, compId)
                if _coordAtomSite is not None and _coordAtomSite['comp_id'] == compId:
                    if atomId in _coordAtomSite['atom_id']:
                        found = True
                        self.__authSeqId = 'auth_seq_id'
                        seqKey = _seqKey
                        self.__setLocalSeqScheme()
                    elif atomId in ('HN1', 'HN2', 'HN3') and ((atomId[-1] + 'HN') in _coordAtomSite['atom_id']
                                                              or ('H' + atomId[-1]) in _coordAtomSite['atom_id']):
                        atomId = atomId[-1] + 'HN' if atomId[-1] + 'HN' in _coordAtomSite['atom_id'] else 'H' + atomId[-1]
                        found = True
                        self.__authSeqId = 'auth_seq_id'
                        seqKey = _seqKey
                        self.__setLocalSeqScheme()
                    elif 'alt_atom_id' in _coordAtomSite and atomId in _coordAtomSite['alt_atom_id']:
                        found = True
                        self.__authSeqId = 'auth_seq_id'
                        # self.__authAtomId = 'auth_atom_id'
                        seqKey = _seqKey
                        self.__setLocalSeqScheme()
                    elif not self.__extendAuthSeq:
                        self.__preferAuthSeq = False
                elif not self.__extendAuthSeq:
                    self.__preferAuthSeq = False

        elif self.__preferAuthSeq and seqKey not in self.__coordUnobsRes:
            _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, compId, asis=False)
            if _coordAtomSite is not None and _coordAtomSite['comp_id'] == compId and not self.__extendAuthSeq:
                if atomId in _coordAtomSite['atom_id']:
                    found = True
                    self.__preferAuthSeq = False
                    self.__authSeqId = 'label_seq_id'
                    seqKey = _seqKey
                    self.__setLocalSeqScheme()
                elif atomId in ('HN1', 'HN2', 'HN3') and ((atomId[-1] + 'HN') in _coordAtomSite['atom_id']
                                                          or ('H' + atomId[-1]) in _coordAtomSite['atom_id']):
                    atomId = atomId[-1] + 'HN' if atomId[-1] + 'HN' in _coordAtomSite['atom_id'] else 'H' + atomId[-1]
                    found = True
                    self.__preferAuthSeq = False
                    self.__authSeqId = 'label_seq_id'
                    seqKey = _seqKey
                    self.__setLocalSeqScheme()
                elif 'alt_atom_id' in _coordAtomSite and atomId in _coordAtomSite['alt_atom_id']:
                    found = True
                    self.__preferAuthSeq = False
                    self.__authSeqId = 'label_seq_id'
                    # self.__authAtomId = 'auth_atom_id'
                    seqKey = _seqKey
                    self.__setLocalSeqScheme()

        elif not self.__preferAuthSeq:
            self.__preferAuthSeq = True
            _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, compId)
            if _coordAtomSite is not None and _coordAtomSite['comp_id'] == compId:
                if atomId in _coordAtomSite['atom_id']:
                    found = True
                    self.__authSeqId = 'auth_seq_id'
                    seqKey = _seqKey
                    self.__setLocalSeqScheme()
                elif atomId in ('HN1', 'HN2', 'HN3') and ((atomId[-1] + 'HN') in _coordAtomSite['atom_id']
                                                          or ('H' + atomId[-1]) in _coordAtomSite['atom_id']):
                    atomId = atomId[-1] + 'HN' if atomId[-1] + 'HN' in _coordAtomSite['atom_id'] else 'H' + atomId[-1]
                    found = True
                    self.__authSeqId = 'auth_seq_id'
                    seqKey = _seqKey
                    self.__setLocalSeqScheme()
                elif 'alt_atom_id' in _coordAtomSite and atomId in _coordAtomSite['alt_atom_id']:
                    found = True
                    self.__authSeqId = 'auth_seq_id'
                    # self.__authAtomId = 'auth_atom_id'
                    seqKey = _seqKey
                    self.__setLocalSeqScheme()
                elif not self.__extendAuthSeq:
                    self.__preferAuthSeq = False
            elif not self.__extendAuthSeq:
                self.__preferAuthSeq = False

        if found:
            if self.__preferAuthSeq:
                self.__preferAuthSeqCount += 1
            return atomId, asis

        if chainId in self.chainNumberDict.values():

            if self.__preferAuthSeq and seqKey not in self.__coordUnobsRes:
                _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, compId, asis=False)
                if _coordAtomSite is not None and _coordAtomSite['comp_id'] == compId and not self.__extendAuthSeq:
                    if atomId in _coordAtomSite['atom_id']:
                        found = True
                        self.__preferAuthSeq = False
                        self.__authSeqId = 'label_seq_id'
                        seqKey = _seqKey
                        self.__setLocalSeqScheme()
                    elif atomId in ('HN1', 'HN2', 'HN3') and ((atomId[-1] + 'HN') in _coordAtomSite['atom_id']
                                                              or ('H' + atomId[-1]) in _coordAtomSite['atom_id']):
                        atomId = atomId[-1] + 'HN' if atomId[-1] + 'HN' in _coordAtomSite['atom_id'] else 'H' + atomId[-1]
                        found = True
                        self.__preferAuthSeq = False
                        self.__authSeqId = 'label_seq_id'
                        seqKey = _seqKey
                        self.__setLocalSeqScheme()
                    elif 'alt_atom_id' in _coordAtomSite and atomId in _coordAtomSite['alt_atom_id']:
                        found = True
                        self.__preferAuthSeq = False
                        self.__authSeqId = 'label_seq_id'
                        # self.__authAtomId = 'auth_atom_id'
                        seqKey = _seqKey
                        self.__setLocalSeqScheme()
            elif not self.__preferAuthSeq:
                self.__preferAuthSeq = True
                _seqKey, _coordAtomSite = self.getCoordAtomSiteOf(chainId, seqId, compId)
                if _coordAtomSite is not None and _coordAtomSite['comp_id'] == compId:
                    if atomId in _coordAtomSite['atom_id']:
                        found = True
                        self.__authSeqId = 'auth_seq_id'
                        seqKey = _seqKey
                        self.__setLocalSeqScheme()
                    elif atomId in ('HN1', 'HN2', 'HN3') and ((atomId[-1] + 'HN') in _coordAtomSite['atom_id']
                                                              or ('H' + atomId[-1]) in _coordAtomSite['atom_id']):
                        atomId = atomId[-1] + 'HN' if atomId[-1] + 'HN' in _coordAtomSite['atom_id'] else 'H' + atomId[-1]
                        found = True
                        self.__authSeqId = 'auth_seq_id'
                        seqKey = _seqKey
                        self.__setLocalSeqScheme()
                    elif 'alt_atom_id' in _coordAtomSite and atomId in _coordAtomSite['alt_atom_id']:
                        found = True
                        self.__authSeqId = 'auth_seq_id'
                        # self.__authAtomId = 'auth_atom_id'
                        seqKey = _seqKey
                        self.__setLocalSeqScheme()
                    elif not self.__extendAuthSeq:
                        self.__preferAuthSeq = False
                elif not self.__extendAuthSeq:
                    self.__preferAuthSeq = False

            if found:
                if self.__preferAuthSeq:
                    self.__preferAuthSeqCount += 1
                return atomId, asis

        if self.ccU.updateChemCompDict(compId):
            cca = next((cca for cca in self.ccU.lastAtomList if cca[self.ccU.ccaAtomId] == atomId), None)
            if cca is not None and seqKey not in self.__coordUnobsRes and self.ccU.lastChemCompDict['_chem_comp.pdbx_release_status'] == 'REL':
                checked = False
                ps = next((ps for ps in self.polySeq if ps['auth_chain_id'] == chainId), None)
                auth_seq_id_list = list(filter(None, ps['auth_seq_id'])) if ps is not None else None
                min_auth_seq_id = max_auth_seq_id = UNREAL_AUTH_SEQ_NUM
                if auth_seq_id_list is not None and len(auth_seq_id_list) > 0:
                    min_auth_seq_id = min(auth_seq_id_list)
                    max_auth_seq_id = max(auth_seq_id_list)
                if seqId == 1 or (chainId, seqId - 1) in self.__coordUnobsRes\
                   or seqId == min_auth_seq_id:
                    if atomId in aminoProtonCode and atomId != 'H1':
                        return self.testCoordAtomIdConsistency(chainId, seqId, compId, 'H1', seqKey, coordAtomSite, index)
                    if atomId in aminoProtonCode or atomId == 'P' or atomId.startswith('HOP'):
                        checked = True
                if not checked:
                    if atomId[0] in protonBeginCode:
                        bondedTo = self.ccU.getBondedAtoms(compId, atomId)
                        if len(bondedTo) > 0 and bondedTo[0][0] != 'P':
                            if coordAtomSite is not None and bondedTo[0] in coordAtomSite['atom_id']:
                                if cca[self.ccU.ccaLeavingAtomFlag] != 'Y'\
                                   or (self.csStat.peptideLike(compId)
                                       and cca[self.ccU.ccaNTerminalAtomFlag] == 'N'
                                       and cca[self.ccU.ccaCTerminalAtomFlag] == 'N'):
                                    self.f.append(f"[Hydrogen not instantiated] {self.getCurrentRestraint(n=index)}"
                                                  f"{chainId}:{seqId}:{compId}:{atomId} is not properly instantiated in the coordinates. "
                                                  "Please re-upload the model file.")
                                    return atomId, asis
                            if bondedTo[0][0] == 'O':
                                return 'Ignorable hydroxyl group', asis
                    if seqId == max_auth_seq_id\
                       or (chainId, seqId + 1) in self.__coordUnobsRes and self.csStat.peptideLike(compId):
                        if coordAtomSite is not None and atomId in carboxylCode\
                           and not isCyclicPolymer(self.cR, self.polySeq, chainId, self.representativeModelId, self.representativeAltId, self.modelNumName):
                            self.f.append(f"[Coordinate issue] {self.getCurrentRestraint(n=index)}"
                                          f"{chainId}:{seqId}:{compId}:{atomId} is not properly instantiated in the coordinates. "
                                          "Please re-upload the model file.")
                            return atomId, asis

                    ext_seq = False
                    if auth_seq_id_list is not None and len(auth_seq_id_list) > 0:
                        if (compId == 'ACE' and seqId == min_auth_seq_id - 1)\
                           or (compId == 'NH2' and seqId == max_auth_seq_id + 1)\
                           or (compId in monDict3 and self.__preferAuthSeqCount - self.__preferLabelSeqCount >= MAX_PREF_LABEL_SCHEME_COUNT
                               and (min_auth_seq_id - MAX_ALLOWED_EXT_SEQ <= seqId < min_auth_seq_id
                                    or max_auth_seq_id < seqId <= max_auth_seq_id + MAX_ALLOWED_EXT_SEQ)):
                            ext_seq = True
                    if chainId in LARGE_ASYM_ID:
                        if ext_seq:
                            return atomId, asis
                        if self.__allow_ext_seq:
                            self.f.append(f"[Sequence mismatch warning] {self.getCurrentRestraint(n=index)}"
                                          f"The residue '{chainId}:{seqId}:{compId}' is not present in polymer sequence "
                                          f"of chain {chainId} of the coordinates. "
                                          "Please update the sequence in the Macromolecules page.")
                            asis = True
                        else:
                            if seqKey in self.__coordUnobsAtom\
                               and (atomId in self.__coordUnobsAtom[seqKey]['atom_ids']
                                    or (atomId[0] in protonBeginCode
                                        and any(bondedTo for bondedTo in self.ccU.getBondedAtoms(compId, atomId, exclProton=True)
                                                if bondedTo in self.__coordUnobsAtom[seqKey]['atom_ids']))):
                                if self.no_extra_comment:
                                    self.f.append(f"[Coordinate issue] {self.getCurrentRestraint(n=index)}"
                                                  f"{chainId}:{seqId}:{compId}:{atomId} is not present in the coordinates.")
                                return atomId, asis
                            if self.no_extra_comment:
                                self.f.append(f"[Atom not found] {self.getCurrentRestraint(n=index)}"
                                              f"{chainId}:{seqId}:{compId}:{atomId} is not present in the coordinates.")
                            updatePolySeqRst(self.polySeqRstFailed, chainId, seqId, compId)
        return atomId, asis

    def getCoordAtomSiteOf(self, chainId: str, seqId: int, compId: Optional[str] = None, cifCheck: bool = True, asis: bool = True
                           ) -> Tuple[Tuple[str, int], Optional[dict]]:
        seqKey = (chainId, seqId)
        if cifCheck:
            preferAuthSeq = self.__preferAuthSeq if asis else not self.__preferAuthSeq
            if preferAuthSeq:
                if compId is not None:
                    _seqKey = (chainId, seqId, compId)
                    if _seqKey in self.__coordAtomSite:
                        return seqKey, self.__coordAtomSite[_seqKey]
                if seqKey in self.__coordAtomSite:
                    if compId is None:
                        return seqKey, self.__coordAtomSite[seqKey]
                    _compId = self.__coordAtomSite[seqKey]['comp_id']
                    if compId == _compId:
                        return seqKey, self.__coordAtomSite[seqKey]
                    if self.hasNonPoly:
                        npList = [np for np in self.nonPoly if np['auth_chain_id'] == chainId]
                        for np in npList:
                            if np['comp_id'][0] == compId and np['auth_seq_id'][0] == seqId:
                                _seqKey = (chainId, np['seq_id'][0])
                                if _seqKey in self.__coordAtomSite and self.__coordAtomSite[_seqKey]['comp_id'] == compId:
                                    return _seqKey, self.__coordAtomSite[_seqKey]
                    return seqKey, self.__coordAtomSite[seqKey]
            else:
                if seqKey in self.__labelToAuthSeq:
                    seqKey = self.__labelToAuthSeq[seqKey]
                    if cifCheck and compId is not None:
                        _seqKey = (seqKey[0], seqKey[1], compId)
                        if _seqKey in self.__coordAtomSite:
                            return seqKey, self.__coordAtomSite[_seqKey]
                    if seqKey in self.__coordAtomSite:
                        return seqKey, self.__coordAtomSite[seqKey]
        return seqKey, None

    def getCurrentRestraint(self, n: int) -> str:
        if self.cur_subtype == 'peak2d':
            return f"[Check the {self.peaks2D}th row of 2D spectral peaks (list_id={self.cur_list_id}, index={n})] "
        if self.cur_subtype == 'peak3d':
            return f"[Check the {self.peaks3D}th row of 3D spectral peaks (list_id={self.cur_list_id}, index={n})] "
        if self.cur_subtype == 'peak4d':
            return f"[Check the {self.peaks4D}th row of 4D spectral peaks (list_id={self.cur_list_id}, index~{n})] "
        return ''

    def __setLocalSeqScheme(self):
        if 'local_seq_scheme' not in self.reasonsForReParsing:
            self.reasonsForReParsing['local_seq_scheme'] = {}
        preferAuthSeq = self.__authSeqId == 'auth_seq_id'
        if self.cur_subtype == 'peak2d':
            self.reasonsForReParsing['local_seq_scheme'][(self.cur_subtype, self.cur_list_id, self.peaks2D)] = preferAuthSeq
        if self.cur_subtype == 'peak3d':
            self.reasonsForReParsing['local_seq_scheme'][(self.cur_subtype, self.cur_list_id, self.peaks3D)] = preferAuthSeq
        if self.cur_subtype == 'peak4d':
            self.reasonsForReParsing['local_seq_scheme'][(self.cur_subtype, self.cur_list_id, self.peaks4D)] = preferAuthSeq
        if not preferAuthSeq:
            self.__preferLabelSeqCount += 1
            if self.__preferLabelSeqCount > MAX_PREF_LABEL_SCHEME_COUNT:
                self.reasonsForReParsing['label_seq_scheme'] = True

    def retrieveLocalSeqScheme(self):
        if self.reasons is None\
           or ('label_seq_scheme' not in self.reasons
               and 'local_seq_scheme' not in self.reasons
               and 'extend_seq_scheme' not in self.reasons):
            return
        if 'extend_seq_scheme' in self.reasons:
            self.__preferAuthSeq = self.__extendAuthSeq = True
            return
        if 'label_seq_scheme' in self.reasons and self.reasons['label_seq_scheme']:
            self.__preferAuthSeq = False
            # self.__authSeqId = 'label_seq_id'
            return
        if self.cur_subtype == 'peak2d':
            key = (self.cur_subtype, self.cur_list_id, self.peaks2D)
        if self.cur_subtype == 'peak3d':
            key = (self.cur_subtype, self.cur_list_id, self.peaks3D)
        if self.cur_subtype == 'peak4d':
            key = (self.cur_subtype, self.cur_list_id, self.peaks4D)
        else:
            return

        if key in self.reasons['local_seq_scheme']:
            self.__preferAuthSeq = self.reasons['local_seq_scheme'][key]

    def __addSf(self):
        content_subtype = contentSubtypeOf(self.cur_subtype)

        if content_subtype is None:
            return

        self.__listIdCounter = incListIdCounter(self.cur_subtype, self.__listIdCounter, reservedListIds=self.__reservedListIds)

        key = (self.cur_subtype, self.cur_list_id)

        if key in self.sfDict:
            if len(self.sfDict[key]) > 0:
                decListIdCounter(self.cur_subtype, self.__listIdCounter, reservedListIds=self.__reservedListIds)
                return
        else:
            self.sfDict[key] = []

        list_id = self.__listIdCounter[content_subtype]

        restraint_name = getRestraintName(self.cur_subtype)

        sf_framecode = f'{self.software_name}_' + restraint_name.replace(' ', '_') + f'_{list_id}'

        sf = getSaveframe(self.cur_subtype, sf_framecode, list_id, self.entryId, self.__originalFileName,
                          numOfDim=self.num_of_dim, spectrumName=self.spectrum_name)

        lp = getPkLoop(self.cur_subtype)

        alt_loops = getAltLoops(content_subtype)

        item = {'file_type': self.file_type, 'saveframe': sf, 'loop': lp, 'alt_loops': alt_loops, 'list_id': list_id,
                'id': 0, 'index_id': 0, 'num_of_dim': self.num_of_dim, 'peak_row_format': True}

        self.sfDict[key].append(item)

    def getSf(self) -> dict:
        key = (self.cur_subtype, self.cur_list_id)

        if key not in self.sfDict:
            self.__addSf()

        return self.sfDict[key][-1]

    def getContentSubtype(self) -> dict:
        """ Return content subtype of PK file.
        """

        n = sum(v for v in self.listIdInternal.values())

        return {'spectral_peak': n} if n > 0 else {}

    def getPolymerSequence(self) -> Optional[List[dict]]:
        """ Return polymer sequence of PK file.
        """

        return None if self.polySeqRst is None or len(self.polySeqRst) == 0 else self.polySeqRst

    def getSequenceAlignment(self) -> Optional[List[dict]]:
        """ Return sequence alignment between coordinates and PK.
        """

        return None if self.seqAlign is None or len(self.seqAlign) == 0 else self.seqAlign

    def getChainAssignment(self) -> Optional[List[dict]]:
        """ Return chain assignment between coordinates and PK.
        """

        return None if self.chainAssign is None or len(self.chainAssign) == 0 else self.chainAssign

    def getReasonsForReparsing(self) -> Optional[dict]:
        """ Return reasons for re-parsing PK file.
        """

        return None if len(self.reasonsForReParsing) == 0 else self.reasonsForReParsing

    def getSfDict(self) -> Tuple[dict, Optional[dict]]:
        """ Return a dictionary of pynmrstar saveframes.
        """

        if len(self.sfDict) == 0:
            return self.__listIdCounter, None
        ign_keys = []
        for k, v in self.sfDict.items():
            for item in reversed(v):
                if item['index_id'] == 0:
                    v.remove(item)
                    if len(v) == 0:
                        ign_keys.append(k)
                    self.__listIdCounter = decListIdCounter(k[0], self.__listIdCounter, reservedListIds=self.__reservedListIds)
        for k in ign_keys:
            del self.sfDict[k]
        return self.__listIdCounter, None if len(self.sfDict) == 0 else self.sfDict
