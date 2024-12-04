##
# File: NmrPipePKParserListener.py
# Date: 03-Dec-2024
#
# Updates:
""" ParserLister class for NMRPIPE PK files.
    @author: Masashi Yokochi
"""
import sys
import re
import copy
import collections
import numpy as np
import math

from antlr4 import ParseTreeListener

try:
    from wwpdb.utils.nmr.pk.NmrPipePKParser import NmrPipePKParser
    from wwpdb.utils.nmr.pk.BasePKParserListener import BasePKParserListener
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS,
                                                       REPRESENTATIVE_MODEL_ID,
                                                       REPRESENTATIVE_ALT_ID,
                                                       SPECTRAL_DIM_TEMPLATE,
                                                       isCyclicPolymer,
                                                       getMaxEffDigits,
                                                       roundString,
                                                       extractPeakAssignment,
                                                       getPkRow)
    from wwpdb.utils.nmr.AlignUtil import (emptyValue,
                                           sortPolySeqRst,
                                           syncCompIdOfPolySeqRst,
                                           alignPolymerSequence,
                                           assignPolymerSequence,
                                           trimSequenceAlignment,
                                           splitPolySeqRstForMultimers,
                                           splitPolySeqRstForExactNoes,
                                           splitPolySeqRstForNonPoly,
                                           splitPolySeqRstForBranched)

except ImportError:
    from nmr.pk.NmrPipePKParser import NmrPipePKParser
    from nmr.pk.BasePKParserListener import BasePKParserListener
    from nmr.mr.ParserListenerUtil import (ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS,
                                           REPRESENTATIVE_MODEL_ID,
                                           REPRESENTATIVE_ALT_ID,
                                           SPECTRAL_DIM_TEMPLATE,
                                           isCyclicPolymer,
                                           getMaxEffDigits,
                                           roundString,
                                           extractPeakAssignment,
                                           getPkRow)
    from nmr.AlignUtil import (emptyValue,
                               sortPolySeqRst,
                               syncCompIdOfPolySeqRst,
                               alignPolymerSequence,
                               assignPolymerSequence,
                               trimSequenceAlignment,
                               splitPolySeqRstForMultimers,
                               splitPolySeqRstForExactNoes,
                               splitPolySeqRstForNonPoly,
                               splitPolySeqRstForBranched)


# This class defines a complete listener for a parse tree produced by NmrPipePKParser.
class NmrPipePKParserListener(ParseTreeListener, BasePKParserListener):

    def __init__(self, verbose=True, log=sys.stdout,
                 representativeModelId=REPRESENTATIVE_MODEL_ID,
                 representativeAltId=REPRESENTATIVE_ALT_ID,
                 mrAtomNameMapping=None,
                 cR=None, caC=None, ccU=None, csStat=None, nefT=None,
                 reasons=None):
        super().__init__(verbose, log, representativeModelId, representativeAltId,
                         mrAtomNameMapping, cR, caC, ccU, csStat, nefT, reasons)

        self.file_type = 'nm-pea-pip'
        self.software_name = 'NMRPIPE'

    # Enter a parse tree produced by NmrPipePKParser#nmrpipe_pk.
    def enterNmrpipe_pk(self, ctx: NmrPipePKParser.Nmrpipe_pkContext):  # pylint: disable=unused-argument
        self.num_of_dim = -1
        self.acq_dim_id = 1
        self.spectral_dim = {}
        self.listIdInternal = {}
        self.chainNumberDict = {}
        self.extResKey = []
        self.polySeqRst = []
        self.polySeqRstFailed = []
        self.polySeqRstFailedAmbig = []
        self.compIdMap = {}
        self.f = []

    # Exit a parse tree produced by DynamoMRParser#dynamo_mr.
    def exitNmrpipe_pk(self, ctx: NmrPipePKParser.Nmrpipe_pkContext):  # pylint: disable=unused-argument

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

            if len(self.spectral_dim) > 0:
                for d, v in self.spectral_dim.items():
                    for _id, _v in v.items():
                        for __v in _v.values():
                            if 'freq_hint' in __v:
                                center = np.mean(np.array(__v['freq_hint']))

                                if __v['spectral_region'] is None:
                                    atom_type = __v['atom_type']
                                    if 125 < center < 130 and atom_type == 'C':
                                        __v['spectral_region'] = 'C_aro'
                                    elif 115 < center < 125 and atom_type == 'N':
                                        __v['spectral_region'] = 'N_ami'
                                    elif 170 < center < 180 and atom_type == 'C':
                                        __v['spectral_region'] = 'CO'
                                    elif 6 < center < 9 and atom_type == 'H':
                                        __v['spectral_region'] = 'H_ami_or_aro'
                                    elif 4 < center < 6 and atom_type == 'H':
                                        __v['spectral_region'] = 'H_all'
                                    elif 60 < center < 90 and atom_type == 'C':
                                        __v['spectral_region'] = 'C_all'
                                    elif 30 < center < 50 and atom_type == 'C':
                                        __v['spectral_region'] = 'C_ali'

                                del __v['freq_hint']

                            if __v['spectrometer_frequency'] is None and 'obs_freq_hint' in __v and len(__v['obs_freq_hint']) > 0:
                                __v['spectrometer_frequency'] = collections.Counter(__v['obs_freq_hint']).most_common()[0][0]

                            if 'obs_freq_hint' in __v:
                                del __v['obs_freq_hint']

                        for __v in _v.values():
                            if __v['spectral_region'] == 'H_ami_or_aro':
                                has_a = any(___v['spectral_region'] == 'C_aro' for ___v in _v.values())
                                __v['spectral_region'] = 'H_aro' if has_a else 'H_ami'

                        if self.debug:
                            print(f'num_of_dim: {d}, list_id: {_id}')
                            for __d, __v in _v.items():
                                print(f'{__d} {__v}')

        finally:
            self.warningMessage = sorted(list(set(self.f)), key=self.f.index)

    # Enter a parse tree produced by NmrPipePKParser#data_label.
    def enterData_label(self, ctx: NmrPipePKParser.Data_labelContext):  # pylint: disable=unused-argument

        def set_spectral_dim(_dim_id):
            self.num_of_dim = max(self.num_of_dim, _dim_id)
            if _dim_id not in self.cur_spectral_dim:
                cur_spectral_dim = copy.copy(SPECTRAL_DIM_TEMPLATE)

            if ctx.Simple_name_DA():
                cur_spectral_dim['axis_code'] = axis_code = str(ctx.Simple_name_DA())
            if axis_code is not None:
                digits = re.findall(r'\d+', axis_code)
                for digit in digits:
                    num = int(digit)
                    nuc = next((k for k, v in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS.items() if num == v[0]), None)
                    if nuc is not None:
                        cur_spectral_dim['atom_type'] = nuc
                        cur_spectral_dim['atom_isotope_number'] = num
                        break
                if cur_spectral_dim['atom_type'] is None:
                    for a in axis_code:
                        a = a.upper()
                        if a in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS:
                            cur_spectral_dim['atom_type'] = a
                            cur_spectral_dim['atom_isotope_number'] = ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS[a][0]
                            break

            truncated = False
            first_point = last_point = None
            if ctx.Integer_DA(0) and ctx.Integer_DA(1):
                first_point = int(str(ctx.Integer_DA(0)))
                last_point = int(str(ctx.Integer_DA(1)))

                truncated |= first_point != 1
                log2_last_point = math.log2(float(last_point))
                round_log2_last_point = int(log2_last_point)
                truncated |= log2_last_point - round_log2_last_point > 0.001

            isotope_number = cur_spectral_dim['atom_isotope_number']

            cur_spectral_dim['acquisition'] = 'yes' if _dim_id == self.acq_dim_id\
                and (isotope_number == 1 or (isotope_number == 13 and self.exptlMethod == 'SOLID-STATE NMR')) else 'no'

            if _dim_id == 1 and cur_spectral_dim['acquisition'] == 'no':
                self.acq_dim_id = self.num_of_dim

            cur_spectral_dim['under_sampling_type'] = 'not observed' if cur_spectral_dim['acquisition'] == 'yes' else 'aliased'

            if ctx.Ppm_value_DA(0) and ctx.Ppm_value_DA(1):
                row = [str(ctx.Ppm_value_DA(0)).replace('ppm', ''),
                       str(ctx.Ppm_value_DA(1)).replace('ppm', '')]

                max_eff_digits = getMaxEffDigits(row)

                first_ppm = float(row[0])
                last_ppm = float(row[1])
                cur_spectral_dim['value_first_point'] = first_ppm
                cur_spectral_dim['center_frequency_offset'] = roundString(str((first_ppm + last_ppm) / 2.0),
                                                                          max_eff_digits)

                if truncated:
                    _last_point = int(pow(2.0, round_log2_last_point + 1.0))
                    scale = float(_last_point) / float(last_point - first_point - 1)
                    cur_spectral_dim['sweep_width'] = roundString(str((first_ppm - last_ppm) * scale),
                                                                  max_eff_digits)
                else:
                    cur_spectral_dim['sweep_width'] = roundString(str(first_ppm - last_ppm),
                                                                  max_eff_digits)

                cur_spectral_dim['sweep_width_unit'] = 'ppm'

            self.cur_spectral_dim[_dim_id] = cur_spectral_dim

        if ctx.X_axis_DA():
            set_spectral_dim(1)
        elif ctx.Y_axis_DA():
            set_spectral_dim(2)
        elif ctx.Z_axis_DA():
            set_spectral_dim(3)
        elif ctx.A_axis_DA():
            set_spectral_dim(4)

    # Exit a parse tree produced by NmrPipePKParser#data_label.
    def exitData_label(self, ctx: NmrPipePKParser.Data_labelContext):  # pylint: disable=unused-argument
        if self.num_of_dim > 2 and self.exptlMethod != 'SOLID-STATE NMR':
            for _dim_id in range(2, self.num_of_dim + 1):
                cur_spectral_dim = self.cur_spectral_dim[_dim_id]
                if cur_spectral_dim['atom_isotope_number'] != 13:
                    continue
                if cur_spectral_dim['center_frequency_offset'] > 100.0:
                    continue
                if cur_spectral_dim['sweep_width'] < 50.0:
                    cur_spectral_dim['under_sampling_type'] = 'folded'

    # Enter a parse tree produced by NmrPipePKParser#peak_list_2d.
    def enterPeak_list_2d(self, ctx: NmrPipePKParser.Peak_list_2dContext):  # pylint: disable=unused-argument
        self.num_of_dim = 2
        self.cur_subtype = 'peak2d'
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
            self.spectral_dim[self.num_of_dim][self.cur_list_id][_dim_id]['freq_hint'] = []
            self.spectral_dim[self.num_of_dim][self.cur_list_id][_dim_id]['obs_freq_hint'] = []
        self.peaks2D = 0
        self.cur_spectral_dim = {}

        self.null_value = str(ctx.Null_value()) if ctx.Null_value() else None
        self.null_string = str(ctx.Null_string()) if ctx.Null_string() else None

    # Exit a parse tree produced by NmrPipePKParser#peak_list_2d.
    def exitPeak_list_2d(self, ctx: NmrPipePKParser.Peak_list_2dContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by NmrPipePKParser#peak_2d.
    def enterPeak_2d(self, ctx: NmrPipePKParser.Peak_2dContext):  # pylint: disable=unused-argument
        self.peaks2D += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by NmrPipePKParser#peak_2d.
    def exitPeak_2d(self, ctx: NmrPipePKParser.Peak_2dContext):

        try:

            if len(self.numberSelection) == 0:
                self.peaks2D -= 1
                return

            index = int(str(ctx.Integer(0)))
            # x_axis = self.numberSelection[0]
            # y_axis = self.numberSelection[1]
            # dx = self.numberSelection[2]
            # dy = self.numberSelection[3]
            x_ppm = self.numberSelection[4]
            y_ppm = self.numberSelection[5]
            x_hz = self.numberSelection[6]
            y_hz = self.numberSelection[7]
            # xw = self.numberSelection[8]
            # yw = self.numberSelection[9]
            xw_hz = self.numberSelection[10]
            yw_hz = self.numberSelection[11]
            # x1 = int(str(ctx.Integer(1)))
            # x3 = int(str(ctx.Integer(2)))
            # y1 = int(str(ctx.Integer(3)))
            # y3 = int(str(ctx.Integer(4)))
            height = self.originalNumberSelection[12]
            dheight = self.originalNumberSelection[13]
            vol = self.originalNumberSelection[14]
            # pchi2 = self.originalNumberSelection[15]
            type = int(str(ctx.Integer(5)))
            if ctx.Any_name():
                ass = str(ctx.Any_name())
                if ass in emptyValue or (self.null_string is not None and ass == self.null_string):
                    ass = None
            else:
                ass = None
            # clustid = int(str(ctx.Integer(6)))
            # memcnt = int(str(ctx.Integer(7)))

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            if x_ppm is None or y_ppm is None or type != 1:
                self.peaks2D -= 1
                return

            dstFunc = self.validatePeak2D(index, x_ppm, y_ppm, None, None, None, None,
                                          x_hz, y_hz, xw_hz, yw_hz, height, dheight, vol, None)

            if dstFunc is None:
                self.peaks2D -= 1
                return

            cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

            cur_spectral_dim[1]['freq_hint'].append(x_ppm)
            cur_spectral_dim[2]['freq_hint'].append(y_ppm)

            if x_ppm is not None and x_hz is not None and cur_spectral_dim[1]['spectrometer_frequency'] is None\
               and isinstance(cur_spectral_dim[1]['value_first_point'], float):
                cur_spectral_dim[1]['obs_freq_hint'].append(float(roundString(str(x_hz / (cur_spectral_dim[1]['value_first_point'] - x_ppm)),
                                                                              getMaxEffDigits([str(x_ppm), str(x_hz)]))))
            if y_ppm is not None and y_hz is not None and cur_spectral_dim[2]['spectrometer_frequency'] is None\
               and isinstance(cur_spectral_dim[2]['value_first_point'], float):
                cur_spectral_dim[2]['obs_freq_hint'].append(float(roundString(str(y_hz / (cur_spectral_dim[2]['value_first_point'] - y_ppm)),
                                                                              getMaxEffDigits([str(y_ppm), str(y_hz)]))))

            has_assignments = False

            if ass is not None:
                assignments =\
                    extractPeakAssignment(self.num_of_dim, ass, self.authAsymIdSet, self.compIdSet, self.altCompIdSet,
                                          self.polyPeptide, self.polyDeoxyribonucleotide, self.polyRibonucleotide, self.nefT)

                if assignments is not None:

                    self.retrieveLocalSeqScheme()

                    hasChainId = all(a['chain_id'] is not None for a in assignments)
                    hasCompId = all(a['comp_id'] is not None for a in assignments)

                    a1 = assignments[0]
                    a2 = assignments[1]

                    if hasChainId and hasCompId:
                        chainAssign1, asis1 = self.assignCoordPolymerSequenceWithChainId(a1['chain_id'], a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                        chainAssign2, asis2 = self.assignCoordPolymerSequenceWithChainId(a2['chain_id'], a2['seq_id'], a2['comp_id'], a2['atom_id'], index)

                    elif hasChainId:
                        chainAssign1 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a1['chain_id'], a1['seq_id'], a1['atom_id'], index)
                        chainAssign2 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a2['chain_id'], a2['seq_id'], a2['atom_id'], index)
                        asis1 = asis2 = False

                    elif hasCompId:
                        chainAssign1, asis1 = self.assignCoordPolymerSequence(a1['chain_id'], a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                        chainAssign2, asis2 = self.assignCoordPolymerSequence(a2['chain_id'], a2['seq_id'], a2['comp_id'], a2['atom_id'], index)

                    else:
                        chainAssign1 = self.assignCoordPolymerSequenceWithoutCompId(a1['seq_id'], a1['atom_id'], index)
                        chainAssign2 = self.assignCoordPolymerSequenceWithoutCompId(a2['seq_id'], a2['atom_id'], index)
                        asis1 = asis2 = False

                    if len(chainAssign1) > 0 and len(chainAssign2) > 0:
                        self.selectCoordAtoms(chainAssign1, a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                        self.selectCoordAtoms(chainAssign2, a2['seq_id'], a2['comp_id'], a2['atom_id'], index)

                        if len(self.atomSelectionSet) == self.num_of_dim:
                            has_assignments = True

            if self.createSfDict__:
                sf = self.getSf()

            if self.debug:
                print(f"subtype={self.cur_subtype} id={self.peaks2D} (index={index}) "
                      f"{ass} -> {self.atomSelectionSet[0] if has_assignments else None} {self.atomSelectionSet[1] if has_assignments else None} {dstFunc}")

            if self.createSfDict__ and sf is not None:
                sf['index_id'] += 1
                ambig_code1 = ambig_code2 = None
                if has_assignments:
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
                               details=ass)
                sf['loop'].add_data(row)

        finally:
            self.numberSelection.clear()
            self.originalNumberSelection.clear()

    # Enter a parse tree produced by NmrPipePKParser#peak_list_3d.
    def enterPeak_list_3d(self, ctx: NmrPipePKParser.Peak_list_3dContext):  # pylint: disable=unused-argument
        self.num_of_dim = 3
        self.cur_subtype = 'peak3d'
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
            self.spectral_dim[self.num_of_dim][self.cur_list_id][_dim_id]['freq_hint'] = []
            self.spectral_dim[self.num_of_dim][self.cur_list_id][_dim_id]['obs_freq_hint'] = []
        self.peaks3D = 0
        self.cur_spectral_dim = {}

        self.null_value = str(ctx.Null_value()) if ctx.Null_value() else None
        self.null_string = str(ctx.Null_string()) if ctx.Null_string() else None

    # Exit a parse tree produced by NmrPipePKParser#peak_list_3d.
    def exitPeak_list_3d(self, ctx: NmrPipePKParser.Peak_list_3dContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by NmrPipePKParser#peak_3d.
    def enterPeak_3d(self, ctx: NmrPipePKParser.Peak_3dContext):  # pylint: disable=unused-argument
        self.peaks3D += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by NmrPipePKParser#peak_3d.
    def exitPeak_3d(self, ctx: NmrPipePKParser.Peak_3dContext):

        try:

            if len(self.numberSelection) == 0:
                self.peaks3D -= 1
                return

            index = int(str(ctx.Integer(0)))
            # x_axis = self.numberSelection[0]
            # y_axis = self.numberSelection[1]
            # z_axis = self.numberSelection[2]
            # dx = self.numberSelection[3]
            # dy = self.numberSelection[4]
            # dz = self.numberSelection[5]
            x_ppm = self.numberSelection[6]
            y_ppm = self.numberSelection[7]
            z_ppm = self.numberSelection[8]
            x_hz = self.numberSelection[9]
            y_hz = self.numberSelection[10]
            z_hz = self.numberSelection[11]
            # xw = self.numberSelection[12]
            # yw = self.numberSelection[13]
            # zw = self.numberSelection[14]
            xw_hz = self.numberSelection[15]
            yw_hz = self.numberSelection[16]
            zw_hz = self.numberSelection[17]
            # x1 = int(str(ctx.Integer(1)))
            # x3 = int(str(ctx.Integer(2)))
            # y1 = int(str(ctx.Integer(3)))
            # y3 = int(str(ctx.Integer(4)))
            # z1 = int(str(ctx.Integer(5)))
            # z3 = int(str(ctx.Integer(6)))
            height = self.originalNumberSelection[18]
            dheight = self.originalNumberSelection[19]
            vol = self.originalNumberSelection[20]
            # pchi2 = self.originalNumberSelection[21]
            type = int(str(ctx.Integer(7)))
            if ctx.Any_name():
                ass = str(ctx.Any_name())
                if ass in emptyValue or (self.null_string is not None and ass == self.null_string):
                    ass = None
            else:
                ass = None
            # clustid = int(str(ctx.Integer(8)))
            # memcnt = int(str(ctx.Integer(9)))

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            if x_ppm is None or y_ppm is None or z_ppm is None or type != 1:
                self.peaks3D -= 1
                return

            dstFunc = self.validatePeak3D(index, x_ppm, y_ppm, z_ppm, None, None, None, None, None, None,
                                          x_hz, y_hz, z_hz, xw_hz, yw_hz, zw_hz, height, dheight, vol, None)

            if dstFunc is None:
                self.peaks3D -= 1
                return

            cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

            cur_spectral_dim[1]['freq_hint'].append(x_ppm)
            cur_spectral_dim[2]['freq_hint'].append(y_ppm)
            cur_spectral_dim[3]['freq_hint'].append(z_ppm)

            if x_ppm is not None and x_hz is not None and cur_spectral_dim[1]['spectrometer_frequency'] is None\
               and isinstance(cur_spectral_dim[1]['value_first_point'], float):
                cur_spectral_dim[1]['obs_freq_hint'].append(float(roundString(str(x_hz / (cur_spectral_dim[1]['value_first_point'] - x_ppm)),
                                                                              getMaxEffDigits([str(x_ppm), str(x_hz)]))))
            if y_ppm is not None and y_hz is not None and cur_spectral_dim[2]['spectrometer_frequency'] is None\
               and isinstance(cur_spectral_dim[2]['value_first_point'], float):
                cur_spectral_dim[2]['obs_freq_hint'].append(float(roundString(str(y_hz / (cur_spectral_dim[2]['value_first_point'] - y_ppm)),
                                                                              getMaxEffDigits([str(y_ppm), str(y_hz)]))))
            if z_ppm is not None and z_hz is not None and cur_spectral_dim[3]['spectrometer_frequency'] is None\
               and isinstance(cur_spectral_dim[3]['value_first_point'], float):
                cur_spectral_dim[3]['obs_freq_hint'].append(float(roundString(str(z_hz / (cur_spectral_dim[3]['value_first_point'] - z_ppm)),
                                                                              getMaxEffDigits([str(z_ppm), str(z_hz)]))))

            has_assignments = False

            if ass is not None:
                assignments =\
                    extractPeakAssignment(self.num_of_dim, ass, self.authAsymIdSet, self.compIdSet, self.altCompIdSet,
                                          self.polyPeptide, self.polyDeoxyribonucleotide, self.polyRibonucleotide, self.nefT)

                if assignments is not None:

                    self.retrieveLocalSeqScheme()

                    hasChainId = all(a['chain_id'] is not None for a in assignments)
                    hasCompId = all(a['comp_id'] is not None for a in assignments)

                    a1 = assignments[0]
                    a2 = assignments[1]
                    a3 = assignments[2]

                    if hasChainId and hasCompId:
                        chainAssign1, asis1 = self.assignCoordPolymerSequenceWithChainId(a1['chain_id'], a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                        chainAssign2, asis2 = self.assignCoordPolymerSequenceWithChainId(a2['chain_id'], a2['seq_id'], a2['comp_id'], a2['atom_id'], index)
                        chainAssign3, asis3 = self.assignCoordPolymerSequenceWithChainId(a3['chain_id'], a3['seq_id'], a3['comp_id'], a3['atom_id'], index)

                    elif hasChainId:
                        chainAssign1 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a1['chain_id'], a1['seq_id'], a1['atom_id'], index)
                        chainAssign2 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a2['chain_id'], a2['seq_id'], a2['atom_id'], index)
                        chainAssign3 = self.assignCoordPolymerSequenceWithChainIdWithoutCompId(a3['chain_id'], a3['seq_id'], a3['atom_id'], index)
                        asis1 = asis2 = asis3 = False

                    elif hasCompId:
                        chainAssign1, asis1 = self.assignCoordPolymerSequence(a1['chain_id'], a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                        chainAssign2, asis2 = self.assignCoordPolymerSequence(a2['chain_id'], a2['seq_id'], a2['comp_id'], a2['atom_id'], index)
                        chainAssign3, asis3 = self.assignCoordPolymerSequence(a3['chain_id'], a3['seq_id'], a3['comp_id'], a3['atom_id'], index)

                    else:
                        chainAssign1 = self.assignCoordPolymerSequenceWithoutCompId(a1['seq_id'], a1['atom_id'], index)
                        chainAssign2 = self.assignCoordPolymerSequenceWithoutCompId(a2['seq_id'], a2['atom_id'], index)
                        chainAssign3 = self.assignCoordPolymerSequenceWithoutCompId(a3['seq_id'], a3['atom_id'], index)
                        asis1 = asis2 = asis3 = False

                    if len(chainAssign1) > 0 and len(chainAssign2) > 0 and len(chainAssign3) > 0:
                        self.selectCoordAtoms(chainAssign1, a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                        self.selectCoordAtoms(chainAssign2, a2['seq_id'], a2['comp_id'], a2['atom_id'], index)
                        self.selectCoordAtoms(chainAssign3, a3['seq_id'], a3['comp_id'], a3['atom_id'], index)

                        if len(self.atomSelectionSet) == self.num_of_dim:
                            has_assignments = True

            if self.createSfDict__:
                sf = self.getSf()

            if self.debug:
                print(f"subtype={self.cur_subtype} id={self.peaks3D} (index={index}) "
                      f"{ass} -> {self.atomSelectionSet[0] if has_assignments else None} {self.atomSelectionSet[1] if has_assignments else None} "
                      f"{self.atomSelectionSet[2] if has_assignments else None} {dstFunc}")

            if self.createSfDict__ and sf is not None:
                sf['index_id'] += 1
                ambig_code1 = ambig_code2 = ambig_code3 = None
                if has_assignments:
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
                               ambig_code3=ambig_code3, details=ass)
                sf['loop'].add_data(row)

        finally:
            self.numberSelection.clear()
            self.originalNumberSelection.clear()

    # Enter a parse tree produced by NmrPipePKParser#peak_list_4d.
    def enterPeak_list_4d(self, ctx: NmrPipePKParser.Peak_list_4dContext):  # pylint: disable=unused-argument
        self.num_of_dim = 4
        self.cur_subtype = 'peak4d'
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
            self.spectral_dim[self.num_of_dim][self.cur_list_id][_dim_id]['freq_hint'] = []
            self.spectral_dim[self.num_of_dim][self.cur_list_id][_dim_id]['obs_freq_hint'] = []
        self.peaks4D = 0
        self.cur_spectral_dim = {}

        self.null_value = str(ctx.Null_value()) if ctx.Null_value() else None
        self.null_string = str(ctx.Null_string()) if ctx.Null_string() else None

    # Exit a parse tree produced by NmrPipePKParser#peak_list_4d.
    def exitPeak_list_4d(self, ctx: NmrPipePKParser.Peak_list_4dContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by NmrPipePKParser#peak_4d.
    def enterPeak_4d(self, ctx: NmrPipePKParser.Peak_4dContext):  # pylint: disable=unused-argument
        self.peaks4D += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by NmrPipePKParser#peak_4d.
    def exitPeak_4d(self, ctx: NmrPipePKParser.Peak_4dContext):

        try:

            if len(self.numberSelection) == 0:
                self.peaks4D -= 1
                return

            index = int(str(ctx.Integer(0)))
            # x_axis = self.numberSelection[0]
            # y_axis = self.numberSelection[1]
            # z_axis = self.numberSelection[2]
            # a_axis = self.numberSelection[3]
            # dx = self.numberSelection[4]
            # dy = self.numberSelection[5]
            # dz = self.numberSelection[6]
            # da = self.numberSelection[7]
            x_ppm = self.numberSelection[8]
            y_ppm = self.numberSelection[9]
            z_ppm = self.numberSelection[10]
            a_ppm = self.numberSelection[11]
            x_hz = self.numberSelection[12]
            y_hz = self.numberSelection[13]
            z_hz = self.numberSelection[14]
            a_hz = self.numberSelection[15]
            # xw = self.numberSelection[16]
            # yw = self.numberSelection[17]
            # zw = self.numberSelection[18]
            # aw = self.numberSelection[19]
            xw_hz = self.numberSelection[20]
            yw_hz = self.numberSelection[21]
            zw_hz = self.numberSelection[22]
            aw_hz = self.numberSelection[23]
            # x1 = int(str(ctx.Integer(1)))
            # x3 = int(str(ctx.Integer(2)))
            # y1 = int(str(ctx.Integer(3)))
            # y3 = int(str(ctx.Integer(4)))
            # z1 = int(str(ctx.Integer(5)))
            # z3 = int(str(ctx.Integer(6)))
            # a1 = int(str(ctx.Integer(7)))
            # a3 = int(str(ctx.Integer(8)))
            height = self.originalNumberSelection[24]
            dheight = self.originalNumberSelection[25]
            vol = self.originalNumberSelection[26]
            # pchi2 = self.originalNumberSelection[27]
            type = int(str(ctx.Integer(9)))
            if ctx.Any_name():
                ass = str(ctx.Any_name())
                if ass in emptyValue or (self.null_string is not None and ass == self.null_string):
                    ass = None
            else:
                ass = None
            # clustid = int(str(ctx.Integer(10)))
            # memcnt = int(str(ctx.Integer(11)))

            if not self.hasPolySeq and not self.hasNonPolySeq:
                return

            if x_ppm is None or y_ppm is None or z_ppm is None or a_ppm is None or type != 1:
                self.peaks4D -= 1
                return

            dstFunc = self.validatePeak4D(index, x_ppm, y_ppm, z_ppm, a_ppm, None, None, None, None, None, None, None, None,
                                          x_hz, y_hz, z_hz, a_hz, xw_hz, yw_hz, zw_hz, aw_hz, height, dheight, vol, None)

            if dstFunc is None:
                self.peaks4D -= 1
                return

            cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

            cur_spectral_dim[1]['freq_hint'].append(x_ppm)
            cur_spectral_dim[2]['freq_hint'].append(y_ppm)
            cur_spectral_dim[3]['freq_hint'].append(z_ppm)
            cur_spectral_dim[4]['freq_hint'].append(a_ppm)

            if x_ppm is not None and x_hz is not None and cur_spectral_dim[1]['spectrometer_frequency'] is None\
               and isinstance(cur_spectral_dim[1]['value_first_point'], float):
                cur_spectral_dim[1]['obs_freq_hint'].append(float(roundString(str(x_hz / (cur_spectral_dim[1]['value_first_point'] - x_ppm)),
                                                                              getMaxEffDigits([str(x_ppm), str(x_hz)]))))
            if y_ppm is not None and y_hz is not None and cur_spectral_dim[2]['spectrometer_frequency'] is None\
               and isinstance(cur_spectral_dim[2]['value_first_point'], float):
                cur_spectral_dim[2]['obs_freq_hint'].append(float(roundString(str(y_hz / (cur_spectral_dim[2]['value_first_point'] - y_ppm)),
                                                                              getMaxEffDigits([str(y_ppm), str(y_hz)]))))
            if z_ppm is not None and z_hz is not None and cur_spectral_dim[3]['spectrometer_frequency'] is None\
               and isinstance(cur_spectral_dim[3]['value_first_point'], float):
                cur_spectral_dim[3]['obs_freq_hint'].append(float(roundString(str(z_hz / (cur_spectral_dim[3]['value_first_point'] - z_ppm)),
                                                                              getMaxEffDigits([str(z_ppm), str(z_hz)]))))
            if a_ppm is not None and a_hz is not None and cur_spectral_dim[4]['spectrometer_frequency'] is None\
               and isinstance(cur_spectral_dim[4]['value_first_point'], float):
                cur_spectral_dim[4]['obs_freq_hint'].append(float(roundString(str(a_hz / (cur_spectral_dim[4]['value_first_point'] - a_ppm)),
                                                                              getMaxEffDigits([str(a_ppm), str(a_hz)]))))

            has_assignments = False

            if ass is not None:
                assignments =\
                    extractPeakAssignment(self.num_of_dim, ass, self.authAsymIdSet, self.compIdSet, self.altCompIdSet,
                                          self.polyPeptide, self.polyDeoxyribonucleotide, self.polyRibonucleotide, self.nefT)

                if assignments is not None:

                    self.retrieveLocalSeqScheme()

                    hasChainId = all(a['chain_id'] is not None for a in assignments)
                    hasCompId = all(a['comp_id'] is not None for a in assignments)

                    a1 = assignments[0]
                    a2 = assignments[1]
                    a3 = assignments[2]
                    a4 = assignments[3]

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
                        asis1 = asis2 = asis3 = asis4 = False

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
                        asis1 = asis2 = asis3 = asis4 = False

                    if len(chainAssign1) > 0 and len(chainAssign2) > 0 and len(chainAssign3) > 0 and len(chainAssign4) > 0:
                        self.selectCoordAtoms(chainAssign1, a1['seq_id'], a1['comp_id'], a1['atom_id'], index)
                        self.selectCoordAtoms(chainAssign2, a2['seq_id'], a2['comp_id'], a2['atom_id'], index)
                        self.selectCoordAtoms(chainAssign3, a3['seq_id'], a3['comp_id'], a3['atom_id'], index)
                        self.selectCoordAtoms(chainAssign4, a4['seq_id'], a4['comp_id'], a4['atom_id'], index)

                        if len(self.atomSelectionSet) == self.num_of_dim:
                            has_assignments = True

            if self.createSfDict__:
                sf = self.getSf()

            if self.debug:
                print(f"subtype={self.cur_subtype} id={self.peaks4D} (index={index}) "
                      f"{ass} -> {self.atomSelectionSet[0] if has_assignments else None} {self.atomSelectionSet[1] if has_assignments else None} "
                      f"{self.atomSelectionSet[2] if has_assignments else None} {self.atomSelectionSet[3] if has_assignments else None} {dstFunc}")

            if self.createSfDict__ and sf is not None:
                sf['index_id'] += 1
                ambig_code1 = ambig_code2 = ambig_code3 = ambig_code4 = None
                if has_assignments:
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
                               atom1, atom2, atom3, atom4, asis1=asis1, asis2=asis2, asis3=asis3, asis4=asis4,
                               ambig_code1=ambig_code1, ambig_code2=ambig_code2,
                               ambig_code3=ambig_code3, ambig_code4=ambig_code4, details=ass)
                sf['loop'].add_data(row)

        finally:
            self.numberSelection.clear()
            self.originalNumberSelection.clear()

    def enterNumber(self, ctx: NmrPipePKParser.NumberContext):  # pylint: disable=unused-argument
        pass

    # Exit a parse tree produced by NmrPipePKParser#number.
    def exitNumber(self, ctx: NmrPipePKParser.NumberContext):
        if ctx.Float():
            value = str(ctx.Float())
            if self.null_value is not None and value == self.null_value:
                self.numberSelection.append(None)
                self.originalNumberSelection.append(None)
            else:
                self.numberSelection.append(float(value))
                self.originalNumberSelection.append(value)

        elif ctx.Real():
            value = str(ctx.Real())
            if self.null_value is not None and value == self.null_value:
                self.numberSelection.append(None)
                self.originalNumberSelection.append(None)
            else:
                self.numberSelection.append(float(value))
                self.originalNumberSelection.append(value)

        else:
            self.numberSelection.append(None)
            self.originalNumberSelection.append(str(ctx.Any_name()))


# del NmrPipePKParser
