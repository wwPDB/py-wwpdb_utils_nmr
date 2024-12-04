##
# File: NmrViewPKParserListener.py
# Date: 03-Dec-2024
#
# Updates:
""" ParserLister class for NMRVIEW PK files.
    @author: Masashi Yokochi
"""
import sys
import re
import copy
import collections
import numpy as np

from antlr4 import ParseTreeListener

try:
    from wwpdb.utils.nmr.pk.NmrViewPKParser import NmrViewPKParser
    from wwpdb.utils.nmr.pk.BasePKParserListener import BasePKParserListener
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS,
                                                       REPRESENTATIVE_MODEL_ID,
                                                       REPRESENTATIVE_ALT_ID,
                                                       SPECTRAL_DIM_TEMPLATE,
                                                       isCyclicPolymer,
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
    from nmr.pk.NmrViewPKParser import NmrViewPKParser
    from nmr.pk.BasePKParserListener import BasePKParserListener
    from nmr.mr.ParserListenerUtil import (ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS,
                                           REPRESENTATIVE_MODEL_ID,
                                           REPRESENTATIVE_ALT_ID,
                                           SPECTRAL_DIM_TEMPLATE,
                                           isCyclicPolymer,
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


# This class defines a complete listener for a parse tree produced by NmrViewPKParser.
class NmrViewPKParserListener(ParseTreeListener, BasePKParserListener):

    __cur_label_type = None

    __labels = None

    def __init__(self, verbose=True, log=sys.stdout,
                 representativeModelId=REPRESENTATIVE_MODEL_ID,
                 representativeAltId=REPRESENTATIVE_ALT_ID,
                 mrAtomNameMapping=None,
                 cR=None, caC=None, ccU=None, csStat=None, nefT=None,
                 reasons=None):
        super().__init__(verbose, log, representativeModelId, representativeAltId,
                         mrAtomNameMapping, cR, caC, ccU, csStat, nefT, reasons)

        self.file_type = 'nm-pea-view'
        self.software_name = 'NMRVIEW'

    # Enter a parse tree produced by NmrViewPKParser#nmrview_pk.
    def enterNmrview_pk(self, ctx: NmrViewPKParser.Nmrview_pkContext):  # pylint: disable=unused-argument
        self.num_of_dim = -1
        self.spectral_dim = {}
        self.listIdInternal = {}
        self.chainNumberDict = {}
        self.extResKey = []
        self.polySeqRst = []
        self.polySeqRstFailed = []
        self.polySeqRstFailedAmbig = []
        self.compIdMap = {}
        self.f = []

    # Exit a parse tree produced by NmrViewPKParser#nmrview_pk.
    def exitNmrview_pk(self, ctx: NmrViewPKParser.Nmrview_pkContext):  # pylint: disable=unused-argument

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
                    for _v in v.values():
                        for __d, __v in _v.items():
                            if 'freq_hint' in __v:
                                if len(__v['freq_hint']) > 0 and d > 2 and __d >= 2\
                                   and self.exptlMethod != 'SOLID-STATE NMR' and __v['atom_isotope_number'] == 13:
                                    center = np.mean(np.array(__v['freq_hint']))
                                    if center < 100.0 and __v['sweep_width'] / __v['spectrometer_frequency'] < 50.0:
                                        __v['under_sampling_type'] = 'fold'
                                del __v['freq_hint']

        finally:
            self.warningMessage = sorted(list(set(self.f)), key=self.f.index)

    # Enter a parse tree produced by NmrViewPKParser#data_label.
    def enterData_label(self, ctx: NmrViewPKParser.Data_labelContext):  # pylint: disable=unused-argument
        self.__labels = {}
        self.__cur_label_type = None

    # Exit a parse tree produced by NmrViewPKParser#data_label.
    def exitData_label(self, ctx: NmrViewPKParser.Data_labelContext):  # pylint: disable=unused-argument
        self.__labels = None
        self.__cur_label_type = None

    # Enter a parse tree produced by NmrViewPKParser#labels.
    def enterLabels(self, ctx: NmrViewPKParser.LabelsContext):  # pylint: disable=unused-argument:
        if self.__cur_label_type is None:
            self.__cur_label_type = 'label'
        elif self.__cur_label_type == 'label':
            self.__cur_label_type = 'sw'
        elif self.__cur_label_type == 'sw':
            self.__cur_label_type = 'sf'
        else:
            self.__cur_label_type = None
            return
        if self.__cur_label_type not in self.__labels:
            self.__labels[self.__cur_label_type] = []

    # Exit a parse tree produced by NmrViewPKParser#labels.
    def exitLabels(self, ctx: NmrViewPKParser.LabelsContext):  # pylint: disable=unused-argument:

        labels = self.__labels[self.__cur_label_type]

        if self.__cur_label_type == 'label':

            self.num_of_dim = len(labels)

            for _dim_id, _axis_code in enumerate(labels, start=1):
                if _dim_id not in self.cur_spectral_dim:
                    cur_spectral_dim = copy.copy(SPECTRAL_DIM_TEMPLATE)

                cur_spectral_dim['axis_code'] = _axis_code

                digits = re.findall(r'\d+', _axis_code)
                for digit in digits:
                    num = int(digit)
                    nuc = next((k for k, v in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS.items() if num == v[0]), None)
                    if nuc is not None:
                        cur_spectral_dim['atom_type'] = nuc
                        cur_spectral_dim['atom_isotope_number'] = num
                        break
                if cur_spectral_dim['atom_type'] is None:
                    for a in _axis_code:
                        a = a.upper()
                        if a in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS:
                            cur_spectral_dim['atom_type'] = a
                            cur_spectral_dim['atom_isotope_number'] = ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS[a][0]
                            break

                isotope_number = cur_spectral_dim['atom_isotope_number']

                cur_spectral_dim['acquisition'] = 'yes' if _dim_id == 1 and (isotope_number == 1
                                                                             or (isotope_number == 13
                                                                                 and self.exptlMethod == 'SOLID-STATE NMR')) else 'no'
                cur_spectral_dim['under_sampling_type'] = 'not observed' if cur_spectral_dim['acquisition'] == 'yes' else 'aliased'

                self.cur_spectral_dim[_dim_id] = cur_spectral_dim

        elif self.__cur_label_type == 'sw':

            for _dim_id, _spectral_width in enumerate(labels, start=1):
                self.cur_spectral_dim[_dim_id]['sweep_width'] = _spectral_width
                self.cur_spectral_dim[_dim_id]['sweep_width_unit'] = 'Hz'

        elif self.__cur_label_type == 'sf':

            for _dim_id, _freq in enumerate(labels, start=1):
                self.cur_spectral_dim[_dim_id]['spectrometer_frequency'] = _freq

    # Enter a parse tree produced by NmrViewPKParser#peak_list_2d.
    def enterPeak_list_2d(self, ctx: NmrViewPKParser.Peak_list_2dContext):  # pylint: disable=unused-argument
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
        self.peaks2D = 0
        self.cur_spectral_dim = {}

    # Exit a parse tree produced by NmrViewPKParser#peak_list_2d.
    def exitPeak_list_2d(self, ctx: NmrViewPKParser.Peak_list_2dContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by NmrViewPKParser#peak_2d.
    def enterPeak_2d(self, ctx: NmrViewPKParser.Peak_2dContext):  # pylint: disable=unused-argument
        self.peaks2D += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by NmrViewPKParser#peak_2d.
    def exitPeak_2d(self, ctx: NmrViewPKParser.Peak_2dContext):

        index = int(str(ctx.Integer(0)))

        L1 = str(ctx.ENCLOSE_DATA(0))[1:-1]
        P1 = float(str(ctx.Float(0)))
        W1 = float(str(ctx.Float(1)))
        B1 = float(str(ctx.Float(2)))
        # E1 = str(ctx.Simple_name(0))
        # J1 = str(ctx.ENCLOSE_DATA(1))[1:-1]
        # U1 = str(ctx.ENCLOSE_DATA(2))[1:-1]

        L2 = str(ctx.ENCLOSE_DATA(3))[1:-1]
        P2 = float(str(ctx.Float(3)))
        W2 = float(str(ctx.Float(4)))
        B2 = float(str(ctx.Float(5)))
        # E2 = str(ctx.Simple_name(1))
        # J2 = str(ctx.ENCLOSE_DATA(4))[1:-1]
        # U2 = str(ctx.ENCLOSE_DATA(5))[1:-1]

        vol = float(str(ctx.Float(6)))
        _int = float(str(ctx.Float(7)))
        stat = int(str(ctx.Integer(1)))
        if ctx.ENCLOSE_DATA(6):
            comment = str(ctx.ENCLOSE_DATA(6))[1:-1]
            if comment in emptyValue:
                comment = None
        else:
            comment = None
        # flag0 = int(str(ctx.Integer(2)))

        if L1 in emptyValue:
            L1 = None
        if L2 in emptyValue:
            L2 = None

        if not self.hasPolySeq and not self.hasNonPolySeq:
            return

        if P1 is None or P2 is None or stat != 0:
            self.peaks2D -= 1
            return

        dstFunc = self.validatePeak2D(index, P1, P2, B1, B2, W1, W2,
                                      None, None, None, None, _int, None, vol)

        if dstFunc is None:
            self.peaks2D -= 1
            return

        cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

        cur_spectral_dim[1]['freq_hint'].append(P1)
        cur_spectral_dim[2]['freq_hint'].append(P2)

        has_assignments = False

        if L1 is not None and L2 is not None:
            assignments = [None] * self.num_of_dim
            assignments[0] = extractPeakAssignment(1, L1, self.authAsymIdSet, self.compIdSet, self.altCompIdSet,
                                                   self.polyPeptide, self.polyDeoxyribonucleotide, self.polyRibonucleotide, self.nefT)
            assignments[1] = extractPeakAssignment(1, L2, self.authAsymIdSet, self.compIdSet, self.altCompIdSet,
                                                   self.polyPeptide, self.polyDeoxyribonucleotide, self.polyRibonucleotide, self.nefT)

            if all(a is not None for a in assignments):

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
                  f"{L1}, {L2} -> {self.atomSelectionSet[0] if has_assignments else None} {self.atomSelectionSet[1] if has_assignments else None} {dstFunc}")

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
                           details=comment)
            sf['loop'].add_data(row)

    # Enter a parse tree produced by NmrViewPKParser#peak_list_3d.
    def enterPeak_list_3d(self, ctx: NmrViewPKParser.Peak_list_3dContext):  # pylint: disable=unused-argument
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
        self.peaks3D = 0
        self.cur_spectral_dim = {}

    # Exit a parse tree produced by NmrViewPKParser#peak_list_3d.
    def exitPeak_list_3d(self, ctx: NmrViewPKParser.Peak_list_3dContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by NmrViewPKParser#peak_3d.
    def enterPeak_3d(self, ctx: NmrViewPKParser.Peak_3dContext):  # pylint: disable=unused-argument
        self.peaks3D += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by NmrViewPKParser#peak_3d.
    def exitPeak_3d(self, ctx: NmrViewPKParser.Peak_3dContext):

        index = int(str(ctx.Integer(0)))

        L1 = str(ctx.ENCLOSE_DATA(0))[1:-1]
        P1 = float(str(ctx.Float(0)))
        W1 = float(str(ctx.Float(1)))
        B1 = float(str(ctx.Float(2)))
        # E1 = str(ctx.Simple_name(0))
        # J1 = str(ctx.ENCLOSE_DATA(1))[1:-1]
        # U1 = str(ctx.ENCLOSE_DATA(2))[1:-1]

        L2 = str(ctx.ENCLOSE_DATA(3))[1:-1]
        P2 = float(str(ctx.Float(3)))
        W2 = float(str(ctx.Float(4)))
        B2 = float(str(ctx.Float(5)))
        # E2 = str(ctx.Simple_name(1))
        # J2 = str(ctx.ENCLOSE_DATA(4))[1:-1]
        # U2 = str(ctx.ENCLOSE_DATA(5))[1:-1]

        L3 = str(ctx.ENCLOSE_DATA(6))[1:-1]
        P3 = float(str(ctx.Float(6)))
        W3 = float(str(ctx.Float(7)))
        B3 = float(str(ctx.Float(8)))
        # E3 = str(ctx.Simple_name(2))
        # J3 = str(ctx.ENCLOSE_DATA(7))[1:-1]
        # U3 = str(ctx.ENCLOSE_DATA(8))[1:-1]

        vol = float(str(ctx.Float(9)))
        _int = float(str(ctx.Float(10)))
        stat = int(str(ctx.Integer(1)))
        if ctx.ENCLOSE_DATA(9):
            comment = str(ctx.ENCLOSE_DATA(9))[1:-1]
            if comment in emptyValue:
                comment = None
        else:
            comment = None
        # flag0 = int(str(ctx.Integer(2)))

        if L1 in emptyValue:
            L1 = None
        if L2 in emptyValue:
            L2 = None
        if L3 in emptyValue:
            L3 = None

        if not self.hasPolySeq and not self.hasNonPolySeq:
            return

        if P1 is None or P2 is None or P3 is None or stat != 0:
            self.peaks3D -= 1
            return

        dstFunc = self.validatePeak3D(index, P1, P2, P3, B1, B2, B3, W1, W2, W3,
                                      None, None, None, None, None, None, _int, None, vol)

        if dstFunc is None:
            self.peaks3D -= 1
            return

        cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

        cur_spectral_dim[1]['freq_hint'].append(P1)
        cur_spectral_dim[2]['freq_hint'].append(P2)
        cur_spectral_dim[3]['freq_hint'].append(P3)

        has_assignments = False

        if L1 is not None and L2 is not None and L3 is not None:
            assignments = [None] * self.num_of_dim
            assignments[0] = extractPeakAssignment(1, L1, self.authAsymIdSet, self.compIdSet, self.altCompIdSet,
                                                   self.polyPeptide, self.polyDeoxyribonucleotide, self.polyRibonucleotide, self.nefT)
            assignments[1] = extractPeakAssignment(1, L2, self.authAsymIdSet, self.compIdSet, self.altCompIdSet,
                                                   self.polyPeptide, self.polyDeoxyribonucleotide, self.polyRibonucleotide, self.nefT)
            assignments[2] = extractPeakAssignment(1, L3, self.authAsymIdSet, self.compIdSet, self.altCompIdSet,
                                                   self.polyPeptide, self.polyDeoxyribonucleotide, self.polyRibonucleotide, self.nefT)

            if all(a is not None for a in assignments):

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
                  f"{L1}, {L2}, {L3} -> {self.atomSelectionSet[0] if has_assignments else None} {self.atomSelectionSet[1] if has_assignments else None} "
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
                           ambig_code1=ambig_code1, ambig_code2=ambig_code2, ambig_code3=ambig_code3,
                           details=comment)
            sf['loop'].add_data(row)

    # Enter a parse tree produced by NmrViewPKParser#peak_list_4d.
    def enterPeak_list_4d(self, ctx: NmrViewPKParser.Peak_list_4dContext):  # pylint: disable=unused-argument
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
        self.peaks4D = 0
        self.cur_spectral_dim = {}

    # Exit a parse tree produced by NmrViewPKParser#peak_list_4d.
    def exitPeak_list_4d(self, ctx: NmrViewPKParser.Peak_list_4dContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by NmrViewPKParser#peak_4d.
    def enterPeak_4d(self, ctx: NmrViewPKParser.Peak_4dContext):  # pylint: disable=unused-argument
        self.peaks4D += 1

        self.atomSelectionSet.clear()

    # Exit a parse tree produced by NmrViewPKParser#peak_4d.
    def exitPeak_4d(self, ctx: NmrViewPKParser.Peak_4dContext):

        index = int(str(ctx.Integer(0)))

        L1 = str(ctx.ENCLOSE_DATA(0))[1:-1]
        P1 = float(str(ctx.Float(0)))
        W1 = float(str(ctx.Float(1)))
        B1 = float(str(ctx.Float(2)))
        # E1 = str(ctx.Simple_name(0))
        # J1 = str(ctx.ENCLOSE_DATA(1))[1:-1]
        # U1 = str(ctx.ENCLOSE_DATA(2))[1:-1]

        L2 = str(ctx.ENCLOSE_DATA(3))[1:-1]
        P2 = float(str(ctx.Float(3)))
        W2 = float(str(ctx.Float(4)))
        B2 = float(str(ctx.Float(5)))
        # E2 = str(ctx.Simple_name(1))
        # J2 = str(ctx.ENCLOSE_DATA(4))[1:-1]
        # U2 = str(ctx.ENCLOSE_DATA(5))[1:-1]

        L3 = str(ctx.ENCLOSE_DATA(6))[1:-1]
        P3 = float(str(ctx.Float(6)))
        W3 = float(str(ctx.Float(7)))
        B3 = float(str(ctx.Float(8)))
        # E3 = str(ctx.Simple_name(2))
        # J3 = str(ctx.ENCLOSE_DATA(7))[1:-1]
        # U3 = str(ctx.ENCLOSE_DATA(8))[1:-1]

        L4 = str(ctx.ENCLOSE_DATA(9))[1:-1]
        P4 = float(str(ctx.Float(9)))
        W4 = float(str(ctx.Float(10)))
        B4 = float(str(ctx.Float(11)))
        # E4 = str(ctx.Simple_name(3))
        # J4 = str(ctx.ENCLOSE_DATA(10))[1:-1]
        # U4 = str(ctx.ENCLOSE_DATA(11))[1:-1]

        vol = float(str(ctx.Float(12)))
        _int = float(str(ctx.Float(13)))
        stat = int(str(ctx.Integer(1)))
        if ctx.ENCLOSE_DATA(12):
            comment = str(ctx.ENCLOSE_DATA(12))[1:-1]
            if comment in emptyValue:
                comment = None
        else:
            comment = None
        # flag0 = int(str(ctx.Integer(2)))

        if L1 in emptyValue:
            L1 = None
        if L2 in emptyValue:
            L2 = None
        if L3 in emptyValue:
            L3 = None
        if L4 in emptyValue:
            L4 = None

        if not self.hasPolySeq and not self.hasNonPolySeq:
            return

        if P1 is None or P2 is None or P3 is None or P4 is None or stat != 0:
            self.peaks4D -= 1
            return

        dstFunc = self.validatePeak4D(index, P1, P2, P3, P4, B1, B2, B3, B4, W1, W2, W3, W4,
                                      None, None, None, None, None, None, None, None, _int, None, vol)

        if dstFunc is None:
            self.peaks4D -= 1
            return

        cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

        cur_spectral_dim[1]['freq_hint'].append(P1)
        cur_spectral_dim[2]['freq_hint'].append(P2)
        cur_spectral_dim[3]['freq_hint'].append(P3)
        cur_spectral_dim[4]['freq_hint'].append(P4)

        has_assignments = False

        if L1 is not None and L2 is not None and L3 is not None and L4 is not None:
            assignments = [None] * self.num_of_dim
            assignments[0] = extractPeakAssignment(1, L1, self.authAsymIdSet, self.compIdSet, self.altCompIdSet,
                                                   self.polyPeptide, self.polyDeoxyribonucleotide, self.polyRibonucleotide, self.nefT)
            assignments[1] = extractPeakAssignment(1, L2, self.authAsymIdSet, self.compIdSet, self.altCompIdSet,
                                                   self.polyPeptide, self.polyDeoxyribonucleotide, self.polyRibonucleotide, self.nefT)
            assignments[2] = extractPeakAssignment(1, L3, self.authAsymIdSet, self.compIdSet, self.altCompIdSet,
                                                   self.polyPeptide, self.polyDeoxyribonucleotide, self.polyRibonucleotide, self.nefT)
            assignments[3] = extractPeakAssignment(1, L4, self.authAsymIdSet, self.compIdSet, self.altCompIdSet,
                                                   self.polyPeptide, self.polyDeoxyribonucleotide, self.polyRibonucleotide, self.nefT)

            if all(a is not None for a in assignments):

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

                if len(chainAssign1) > 0 and len(chainAssign2) > 0 and len(chainAssign3) > 0 and len(chainAssign4):
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
                  f"{L1}, {L2}, {L3}, {L4} -> {self.atomSelectionSet[0] if has_assignments else None} {self.atomSelectionSet[1] if has_assignments else None} "
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
                           ambig_code1=ambig_code1, ambig_code2=ambig_code2, ambig_code3=ambig_code3, ambig_code4=ambig_code4,
                           details=comment)
            sf['loop'].add_data(row)

    # Enter a parse tree produced by NmrViewPKParser#peak_list_wo_eju_2d.
    def enterPeak_list_wo_eju_2d(self, ctx: NmrViewPKParser.Peak_list_wo_eju_2dContext):  # pylint: disable=unused-argument
        self.enterPeak_list_2d(ctx)

    # Exit a parse tree produced by NmrViewPKParser#peak_list_wo_eju_2d.
    def exitPeak_list_wo_eju_2d(self, ctx: NmrViewPKParser.Peak_list_wo_eju_2dContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by NmrViewPKParser#peak_wo_eju_2d.
    def enterPeak_wo_eju_2d(self, ctx: NmrViewPKParser.Peak_wo_eju_2dContext):  # pylint: disable=unused-argument
        self.enterPeak_2d(ctx)

    # Exit a parse tree produced by NmrViewPKParser#peak_wo_eju_2d.
    def exitPeak_wo_eju_2d(self, ctx: NmrViewPKParser.Peak_wo_eju_2dContext):

        index = int(str(ctx.Integer(0)))

        L1 = str(ctx.ENCLOSE_DATA(0))[1:-1]
        P1 = float(str(ctx.Float(0)))
        W1 = float(str(ctx.Float(1)))
        B1 = float(str(ctx.Float(2)))

        L2 = str(ctx.ENCLOSE_DATA(1))[1:-1]
        P2 = float(str(ctx.Float(3)))
        W2 = float(str(ctx.Float(4)))
        B2 = float(str(ctx.Float(5)))

        vol = float(str(ctx.Float(6)))
        _int = float(str(ctx.Float(7)))
        stat = int(str(ctx.Integer(1)))
        if ctx.ENCLOSE_DATA(2):
            comment = str(ctx.ENCLOSE_DATA(2))[1:-1]
            if comment in emptyValue:
                comment = None
        else:
            comment = None
        # flag0 = int(str(ctx.Integer(2)))

        if L1 in emptyValue:
            L1 = None
        if L2 in emptyValue:
            L2 = None

        if not self.hasPolySeq and not self.hasNonPolySeq:
            return

        if P1 is None or P2 is None or stat != 0:
            self.peaks2D -= 1
            return

        dstFunc = self.validatePeak2D(index, P1, P2, B1, B2, W1, W2,
                                      None, None, None, None, _int, None, vol)

        if dstFunc is None:
            self.peaks2D -= 1
            return

        cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

        cur_spectral_dim[1]['freq_hint'].append(P1)
        cur_spectral_dim[2]['freq_hint'].append(P2)

        has_assignments = False

        if L1 is not None and L2 is not None:
            assignments = [None] * self.num_of_dim
            assignments[0] = extractPeakAssignment(1, L1, self.authAsymIdSet, self.compIdSet, self.altCompIdSet,
                                                   self.polyPeptide, self.polyDeoxyribonucleotide, self.polyRibonucleotide, self.nefT)
            assignments[1] = extractPeakAssignment(1, L2, self.authAsymIdSet, self.compIdSet, self.altCompIdSet,
                                                   self.polyPeptide, self.polyDeoxyribonucleotide, self.polyRibonucleotide, self.nefT)

            if all(a is not None for a in assignments):

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
                  f"{L1}, {L2} -> {self.atomSelectionSet[0] if has_assignments else None} {self.atomSelectionSet[1] if has_assignments else None} {dstFunc}")

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
                           details=comment)
            sf['loop'].add_data(row)

    # Enter a parse tree produced by NmrViewPKParser#peak_list_wo_eju_3d.
    def enterPeak_list_wo_eju_3d(self, ctx: NmrViewPKParser.Peak_list_wo_eju_3dContext):  # pylint: disable=unused-argument
        self.enterPeak_list_3d(ctx)

    # Exit a parse tree produced by NmrViewPKParser#peak_list_wo_eju_3d.
    def exitPeak_list_wo_eju_3d(self, ctx: NmrViewPKParser.Peak_list_wo_eju_3dContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by NmrViewPKParser#peak_wo_eju_3d.
    def enterPeak_wo_eju_3d(self, ctx: NmrViewPKParser.Peak_wo_eju_3dContext):  # pylint: disable=unused-argument
        self.enterPeak_3d(ctx)

    # Exit a parse tree produced by NmrViewPKParser#peak_wo_eju_3d.
    def exitPeak_wo_eju_3d(self, ctx: NmrViewPKParser.Peak_wo_eju_3dContext):

        index = int(str(ctx.Integer(0)))

        L1 = str(ctx.ENCLOSE_DATA(0))[1:-1]
        P1 = float(str(ctx.Float(0)))
        W1 = float(str(ctx.Float(1)))
        B1 = float(str(ctx.Float(2)))

        L2 = str(ctx.ENCLOSE_DATA(1))[1:-1]
        P2 = float(str(ctx.Float(3)))
        W2 = float(str(ctx.Float(4)))
        B2 = float(str(ctx.Float(5)))

        L3 = str(ctx.ENCLOSE_DATA(2))[1:-1]
        P3 = float(str(ctx.Float(6)))
        W3 = float(str(ctx.Float(7)))
        B3 = float(str(ctx.Float(8)))

        vol = float(str(ctx.Float(9)))
        _int = float(str(ctx.Float(10)))
        stat = int(str(ctx.Integer(1)))
        if ctx.ENCLOSE_DATA(3):
            comment = str(ctx.ENCLOSE_DATA(3))[1:-1]
            if comment in emptyValue:
                comment = None
        else:
            comment = None
        # flag0 = int(str(ctx.Integer(2)))

        if L1 in emptyValue:
            L1 = None
        if L2 in emptyValue:
            L2 = None
        if L3 in emptyValue:
            L3 = None

        if not self.hasPolySeq and not self.hasNonPolySeq:
            return

        if P1 is None or P2 is None or P3 is None or stat != 0:
            self.peaks3D -= 1
            return

        dstFunc = self.validatePeak3D(index, P1, P2, P3, B1, B2, B3, W1, W2, W3,
                                      None, None, None, None, None, None, _int, None, vol)

        if dstFunc is None:
            self.peaks3D -= 1
            return

        cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

        cur_spectral_dim[1]['freq_hint'].append(P1)
        cur_spectral_dim[2]['freq_hint'].append(P2)
        cur_spectral_dim[3]['freq_hint'].append(P3)

        has_assignments = False

        if L1 is not None and L2 is not None and L3 is not None:
            assignments = [None] * self.num_of_dim
            assignments[0] = extractPeakAssignment(1, L1, self.authAsymIdSet, self.compIdSet, self.altCompIdSet,
                                                   self.polyPeptide, self.polyDeoxyribonucleotide, self.polyRibonucleotide, self.nefT)
            assignments[1] = extractPeakAssignment(1, L2, self.authAsymIdSet, self.compIdSet, self.altCompIdSet,
                                                   self.polyPeptide, self.polyDeoxyribonucleotide, self.polyRibonucleotide, self.nefT)
            assignments[2] = extractPeakAssignment(1, L3, self.authAsymIdSet, self.compIdSet, self.altCompIdSet,
                                                   self.polyPeptide, self.polyDeoxyribonucleotide, self.polyRibonucleotide, self.nefT)

            if all(a is not None for a in assignments):

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
                  f"{L1}, {L2}, {L3} -> {self.atomSelectionSet[0] if has_assignments else None} {self.atomSelectionSet[1] if has_assignments else None} "
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
                           ambig_code1=ambig_code1, ambig_code2=ambig_code2, ambig_code3=ambig_code3,
                           details=comment)
            sf['loop'].add_data(row)

    # Enter a parse tree produced by NmrViewPKParser#peak_list_wo_eju_4d.
    def enterPeak_list_wo_eju_4d(self, ctx: NmrViewPKParser.Peak_list_wo_eju_4dContext):  # pylint: disable=unused-argument
        self.enterPeak_list_4d(ctx)

    # Exit a parse tree produced by NmrViewPKParser#peak_list_wo_eju_4d.
    def exitPeak_list_wo_eju_4d(self, ctx: NmrViewPKParser.Peak_list_wo_eju_4dContext):  # pylint: disable=unused-argument
        pass

    # Enter a parse tree produced by NmrViewPKParser#peak_wo_eju_4d.
    def enterPeak_wo_eju_4d(self, ctx: NmrViewPKParser.Peak_wo_eju_4dContext):  # pylint: disable=unused-argument
        self.enterPeak_4d(ctx)

    # Exit a parse tree produced by NmrViewPKParser#peak_wo_eju_4d.
    def exitPeak_wo_eju_4d(self, ctx: NmrViewPKParser.Peak_wo_eju_4dContext):

        index = int(str(ctx.Integer(0)))

        L1 = str(ctx.ENCLOSE_DATA(0))[1:-1]
        P1 = float(str(ctx.Float(0)))
        W1 = float(str(ctx.Float(1)))
        B1 = float(str(ctx.Float(2)))

        L2 = str(ctx.ENCLOSE_DATA(1))[1:-1]
        P2 = float(str(ctx.Float(3)))
        W2 = float(str(ctx.Float(4)))
        B2 = float(str(ctx.Float(5)))

        L3 = str(ctx.ENCLOSE_DATA(2))[1:-1]
        P3 = float(str(ctx.Float(6)))
        W3 = float(str(ctx.Float(7)))
        B3 = float(str(ctx.Float(8)))

        L4 = str(ctx.ENCLOSE_DATA(3))[1:-1]
        P4 = float(str(ctx.Float(9)))
        W4 = float(str(ctx.Float(10)))
        B4 = float(str(ctx.Float(11)))

        vol = float(str(ctx.Float(12)))
        _int = float(str(ctx.Float(13)))
        stat = int(str(ctx.Integer(1)))
        if ctx.ENCLOSE_DATA(4):
            comment = str(ctx.ENCLOSE_DATA(4))[1:-1]
            if comment in emptyValue:
                comment = None
        else:
            comment = None
        # flag0 = int(str(ctx.Integer(2)))

        if L1 in emptyValue:
            L1 = None
        if L2 in emptyValue:
            L2 = None
        if L3 in emptyValue:
            L3 = None
        if L4 in emptyValue:
            L4 = None

        if not self.hasPolySeq and not self.hasNonPolySeq:
            return

        if P1 is None or P2 is None or P3 is None or P4 is None or stat != 0:
            self.peaks4D -= 1
            return

        dstFunc = self.validatePeak4D(index, P1, P2, P3, P4, B1, B2, B3, B4, W1, W2, W3, W4,
                                      None, None, None, None, None, None, None, None, _int, None, vol)

        if dstFunc is None:
            self.peaks4D -= 1
            return

        cur_spectral_dim = self.spectral_dim[self.num_of_dim][self.cur_list_id]

        cur_spectral_dim[1]['freq_hint'].append(P1)
        cur_spectral_dim[2]['freq_hint'].append(P2)
        cur_spectral_dim[3]['freq_hint'].append(P3)
        cur_spectral_dim[4]['freq_hint'].append(P4)

        has_assignments = False

        if L1 is not None and L2 is not None and L3 is not None and L4 is not None:
            assignments = [None] * self.num_of_dim
            assignments[0] = extractPeakAssignment(1, L1, self.authAsymIdSet, self.compIdSet, self.altCompIdSet,
                                                   self.polyPeptide, self.polyDeoxyribonucleotide, self.polyRibonucleotide, self.nefT)
            assignments[1] = extractPeakAssignment(1, L2, self.authAsymIdSet, self.compIdSet, self.altCompIdSet,
                                                   self.polyPeptide, self.polyDeoxyribonucleotide, self.polyRibonucleotide, self.nefT)
            assignments[2] = extractPeakAssignment(1, L3, self.authAsymIdSet, self.compIdSet, self.altCompIdSet,
                                                   self.polyPeptide, self.polyDeoxyribonucleotide, self.polyRibonucleotide, self.nefT)
            assignments[3] = extractPeakAssignment(1, L4, self.authAsymIdSet, self.compIdSet, self.altCompIdSet,
                                                   self.polyPeptide, self.polyDeoxyribonucleotide, self.polyRibonucleotide, self.nefT)

            if all(a is not None for a in assignments):

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

                if len(chainAssign1) > 0 and len(chainAssign2) > 0 and len(chainAssign3) > 0 and len(chainAssign4):
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
                  f"{L1}, {L2}, {L3}, {L4} -> {self.atomSelectionSet[0] if has_assignments else None} {self.atomSelectionSet[1] if has_assignments else None} "
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
                           ambig_code1=ambig_code1, ambig_code2=ambig_code2, ambig_code3=ambig_code3, ambig_code4=ambig_code4,
                           details=comment)
            sf['loop'].add_data(row)

    # Enter a parse tree produced by NmrViewPKParser#label.
    def enterLabel(self, ctx: NmrViewPKParser.LabelContext):
        if ctx.Float_LA():
            self.__labels[self.__cur_label_type].append(float(str(ctx.Float_LA())))
        elif ctx.Simple_name_LA():
            self.__labels[self.__cur_label_type].append(str(ctx.Simple_name_LA()))
        else:
            value = str(ctx.ENCLOSE_DATA_LA())[1:-1].strip()
            if self.__cur_label_type == 'label':
                self.__labels[self.__cur_label_type].append(value)
            else:
                self.__labels[self.__cur_label_type].append(float(value))

    # Exit a parse tree produced by NmrViewPKParser#label.
    def exitLabel(self, ctx: NmrViewPKParser.LabelContext):
        pass


# del NmrViewPKParser
