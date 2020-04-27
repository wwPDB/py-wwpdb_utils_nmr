##
# File: NmrDpReport.py
# Date: 29-Jul-2019
#
# Updates:
# 09-Oct-2019  M. Yokochi - add setCorrectedError() to catch missing mandatory saveframe tag
# 10-Oct-2019  M. Yokochi - add 'enum_failure_ignorable' warning type
# 15-Oct-2019  M. Yokochi - add 'encouragement' waring type
# 27-Jan-2020  M. Yokochi - change warning type 'enum_failure' to 'enum_mismatch'
# 05-Feb-2020  M. Yokochi - move conflicted_data error to warning
# 10-Feb-2020  M. Yokochi - add methods to retrieve polymer sequence for sample sequence alignment
# 13-Feb-2020  M. Yokochi - add methods to retrieve content_subtype for apilayer.postModifyNMR
# 14-Feb-2020  M. Yokochi - add methods to pre-populate pdbx_nmr_spectral_peak_list, apilayer.postModifyNMRPeaks
# 21-Feb-2020  M. Yokochi - update content-type definitions
# 28-Feb-2020  M. Yokochi - add support for 'nmr-chemical-shifts' content type (DAOTHER-4515)
# 02-Mar-2020  M. Yokochi - add support for 'nmr-restraints' content type (DAOTHER-4515)
# 13-Mar-2020  M. Yokochi - change warning type from suspicious_data to anomalous_data
# 17-Mar-2020  M. Yokochi - remove irrelevant warning types in corrected_warning
# 18-Mar-2020  M. Yokochi - rename warning type from skipped_sf/lp_category to skipped_saveframe/loop_category
# 23-Mar-2020  M. Yokochi - add 'anomalous_chemical_shift' and 'unusual_chemical_shift' warning types
# 24-Mar-2020  M. Yokochi - add method to retrieve chemical shift reference (DAOTHER-1682)
# 03-Apr-2020  M. Yokochi - add methods to retrieve sequence alignment between coordinate and NMR data
# 15-Apr-2020  M. Yokochi - add getAverageRMSDWithinRange() (DAOTHER-4060)
# 18-Apr-2020  M. Yokochi - fix error of apilayer - getNmrSeqAlignment in NMR legacy deposition (DAOTHER-5594)
# 19-Apr-2020  M. Yokochi - support concatenated CS data in NMR legacy deposition (DAOTHER-5594)
# 19 Apr-2020  M. Yokochi - add 'not_superimposed_model' warning type (DAOTHER-4060)
# 20 Apr-2020  M. Yokochi - add 'concatenated_sequence' warning type (DAOTHER-5594)
# 22-Apr-2020  M. Yokochi - add 'ambiguity_code_mismatch' warning type (DAOTHER-5601)
# 25-Apr-2020  M. Yokochi - add 'entity' content subtype (DAOTHER-5611)
# 25-Apr-2020  M. Yokochi - add 'corrected_format_issue' warning type (DAOTHER-5611)
# 27-Apr-2020  M. Yokochi - add 'auth_atom_nomenclature_mismatch' warning type (DAOTHER-5611)
##
""" Wrapper class for data processing report of NMR data.
    @author: Masashi Yokochi
"""
import logging
import json
import copy
import re

class NmrDpReport:
    """ Wrapper class for data processing report of NMR data.
    """

    def __init__(self):
        self.__immutable = False

        self.__report = {'information': {'input_sources': [],
                                         'sequence_alignments': [],
                                         'chain_assignments': [],
                                         'diamagnetic': True,
                                         'disulfide_bond': False,
                                         'other_bond': False,
                                         'cyclic_polymer': False,
                                         'status': 'OK'
                                         },
                         'error': None,
                         'warning': None,
                         'corrected_warning': None
                         }

        self.status_codes = ('OK', 'Error', 'Warning')

        self.input_sources = [NmrDpReportInputSource()]
        self.sequence_alignment = NmrDpReportSequenceAlignment()
        self.chain_assignment = NmrDpReportChainAssignment()
        self.error = NmrDpReportError()
        self.warning = NmrDpReportWarning()
        self.corrected_warning = None

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

    def appendInputSource(self):
        self.input_sources.append(NmrDpReportInputSource())

    def isOk(self):
        return self.__report['information']['status'] == 'OK'

    def isError(self):
        return self.__report['information']['status'] == 'Error'

    def isDiamagnetic(self):
        return self.__report['information']['diamagnetic']

    def hasDisulfideBond(self):
        return self.__report['information']['disulfide_bond']

    def hasOtherBond(self):
        return self.__report['information']['other_bond']

    def hasCyclicPolymer(self):
        return self.__report['information']['cyclic_polymer']

    def getInputSource(self, id):
        """ Return input source of a given index.
            @return: input source of a given index, None otherwise
        """

        if id < 0 or id >= len(self.input_sources):
            return None

        return self.input_sources[id]

    def getInputSourceIdOfNmrData(self):
        """ Return input_source_id of NMR data file.
            @return: index of input source of NMR data file, -1 otherwise
        """

        for i in self.input_sources:
            if i.get()['content_type'] in ['nmr-data-nef', 'nmr-data-str']:
                return self.input_sources.index(i)

        return -1

    def getInputSourceIdsOfNmrLegacyData(self):
        """ Return array of input_source_id of NMR legacy data file.
            @return: array of index of input source of NMR legacy data file, [] otherwise
        """

        return [self.input_sources.index(i) for i in self.input_sources if i.get()['content_type'] in ['nmr-chemical-shifts', 'nmr-restraints']]

    def getInputSourceIdOfCoord(self):
        """ Return input_source_id of coordinate file.
            @return: index of input source of coordinate file, -1 otherwise
        """

        for i in self.input_sources:
            if i.get()['content_type'] == 'model':
                return self.input_sources.index(i)

        return -1

    def getNmrContentSubTypes(self):
        """ Return effective NMR content subtypes.
        """

        id = self.getInputSourceIdOfNmrData()

        if id < 0:
            return None

        nmr_input_source_dic = self.input_sources[id].get()

        return {k: v for k, v in nmr_input_source_dic['content_subtype'].items() if v > 0}

    def __getNmrLegacyContentSubTypes(self, id):
        """ Return effective NMR content subtypes.
        """

        if id < 0:
            return None

        nmr_input_source_dic = self.input_sources[id].get()

        return {k: v for k, v in nmr_input_source_dic['content_subtype'].items() if v > 0}

    def getNmrStatsOfExptlData(self, content_subtype):
        """ Return stats of experimental data of a given content subtype.
        """

        id = self.getInputSourceIdOfNmrData()

        if id < 0:
            return None

        nmr_input_source_dic = self.input_sources[id].get()

        if not 'stats_of_exptl_data' in nmr_input_source_dic:
            return None

        if not content_subtype in nmr_input_source_dic['stats_of_exptl_data']:
            return None

        return nmr_input_source_dic['stats_of_exptl_data'][content_subtype]

    def __getNmrLegacyStatsOfExptlData(self, id, content_subtype):
        """ Return stats of experimental data of a given content subtype.
        """

        if id < 0:
            return None

        nmr_input_source_dic = self.input_sources[id].get()

        if not 'stats_of_exptl_data' in nmr_input_source_dic:
            return None

        if not content_subtype in nmr_input_source_dic['stats_of_exptl_data']:
            return None

        return nmr_input_source_dic['stats_of_exptl_data'][content_subtype]

    def getNmrRestraints(self):
        """ Return stats of NMR restraints.
        """

        content_subtypes = self.getNmrContentSubTypes()

        if content_subtypes is None:
            return self.__getNmrRestraints()

        restraints = []

        id = self.getInputSourceIdOfNmrData()

        nmr_input_source_dic = self.input_sources[id].get()

        file_name = nmr_input_source_dic['file_name']
        file_type = 'NEF' if nmr_input_source_dic['file_type'] == 'nef' else 'NMR-STAR'

        content_subtype = 'dist_restraint'

        if content_subtype in content_subtypes:
            hydrogen_bonds = 0
            disulfide_bonds = 0
            diselenide_bonds = 0
            other_bonds = 0
            symmetric = 0
            noe_like = 0
            noe_exp_type = None
            for stat in self.getNmrStatsOfExptlData(content_subtype):
                for k, v in stat['number_of_constraints'].items():
                    if 'hydrogen_bonds' in k:
                        hydrogen_bonds += v
                    elif 'disulfide_bonds' in k:
                        disulfide_bonds += v
                    elif 'diselenide_bonds' in k:
                        diselenide_bonds += v
                    elif 'other_bonds' in k:
                        other_bonds += v
                    elif k == 'symmetric_constraints':
                        symmetric += v
                    else:
                        if noe_exp_type is None:
                            noe_exp_type = stat['exp_type']
                        noe_like += v
            if noe_like > 0:
                if noe_exp_type.lower() == 'unknown':
                    noe_exp_type = 'NOE? (To be decided)'
                else:
                    _noe_exp_type = noe_exp_type.lower()
                    if _noe_exp_type in ('csp', 'chemical shift perturbation', 'shift_perturbation'):
                        noe_exp_type = 'CSP'
                    elif _noe_exp_type == 'noe':
                        noe_exp_type = 'NOE'
                    elif _noe_exp_type in ('noe buildup', 'noe build-up', 'noe_build_up'):
                        noe_exp_type = 'NOE buildup'
                    elif _noe_exp_type in ('noe not seen', 'noe_not_seen'):
                        noe_exp_type = 'NOE not seen'
                    elif _noe_exp_type in ('pre', 'paramagnetic relaxation'):
                        noe_exp_type == 'PRE'
                    elif _noe_exp_type == 'pre solvent':
                        noe_exp_type = 'PRE solvent'
                    elif _noe_exp_type == 'roe':
                        noe_exp_type = 'ROE'

                restraint = {'constraint_filename': file_name,
                             'software_name': file_type,
                             'constraint_type': 'distance',
                             'constraint_subtype': noe_exp_type,
                             'constraint_number': noe_like}
                restraints.append(restraint)
            if hydrogen_bonds > 0:
                restraint = {'constraint_filename': file_name,
                             'software_name': file_type,
                             'constraint_type': 'distance',
                             'constraint_subtype': 'hydrogen bond',
                             'constraint_number': hydrogen_bonds}
                restraints.append(restraint)
            if disulfide_bonds > 0:
                restraint = {'constraint_filename': file_name,
                             'software_name': file_type,
                             'constraint_type': 'distance',
                             'constraint_subtype': 'disulfide bond',
                             'constraint_number': disulfide_bonds}
                restraints.append(restraint)
            if diselenide_bonds > 0:
                restraint = {'constraint_filename': file_name,
                             'software_name': file_type,
                             'constraint_type': 'distance',
                             'constraint_subtype': 'diselenide bond',
                             'constraint_number': diselenide_bonds}
                restraints.append(restraint)
            if other_bonds > 0:
                restraint = {'constraint_filename': file_name,
                             'software_name': file_type,
                             'constraint_type': 'distance',
                             'constraint_subtype': 'other bond',
                             'constraint_number': other_bonds}
                restraints.append(restraint)
            if symmetric > 0:
                restraint = {'constraint_filename': file_name,
                             'software_name': file_type,
                             'constraint_type': 'distance',
                             'constraint_subtype': 'symmetry',
                             'constraint_number': symmetric}
                restraints.append(restraint)

        content_subtype = 'dihed_restraint'

        if content_subtype in content_subtypes:
            proteins = 0;
            nucleic_acids = 0
            carbohydrates = 0
            others = 0
            for stat in self.getNmrStatsOfExptlData(content_subtype):
                for k, v in stat['number_of_constraints_per_polymer_type'].items():
                    if k == 'protein':
                        proteins += v
                    elif k == 'nucleic_acid':
                        nucleic_acids += v
                    elif k == 'carbohydrate':
                        carbohydrates += v
                    elif k == 'other':
                        others += v
            if proteins > 0:
                restraint = {'constraint_filename': file_name,
                             'software_name': file_type,
                             'constraint_type': 'protein dihedral angle',
                             'constraint_subtype': 'Not applicable',
                             'constraint_number': proteins}
                restraints.append(restraint)
            if nucleic_acids > 0:
                restraint = {'constraint_filename': file_name,
                             'software_name': file_type,
                             'constraint_type': 'nucleic acid dihedral angle',
                             'constraint_subtype': 'Not applicable',
                             'constraint_number': nucleic_acids}
                restraints.append(restraint)
            if carbohydrates > 0:
                restraint = {'constraint_filename': file_name,
                             'software_name': file_type,
                             'constraint_type': 'carbohydrate dihedral angle',
                             'constraint_subtype': 'Not applicable',
                             'constraint_number': carbohydrates}
                restraints.append(restraint)
            if others > 0:
                restraint = {'constraint_filename': file_name,
                             'software_name': file_type,
                             'constraint_type': 'other angle',
                             'constraint_subtype': 'Not applicable',
                             'constraint_number': others}
                restraints.append(restraint)

        content_subtype = 'rdc_restraint'

        if content_subtype in content_subtypes:
            rdc_total = 0
            for stat in self.getNmrStatsOfExptlData(content_subtype):
                for k, v in stat['number_of_constraints'].items():
                    rdc_total += v

            restraint = {'constraint_filename': file_name,
                         'software_name': file_type,
                         'constraint_type': 'intervector projection angle',
                         'constraint_subtype': 'RDC',
                         'constraint_number': rdc_total}

            restraints.append(restraint)

        return restraints if len(restraints) > 0 else None

    def __getNmrRestraints(self):
        """ Return stats of NMR restraints. (legacy)
        """

        list_id = self.getInputSourceIdsOfNmrLegacyData()

        if len(list_id) == 0:
            return None

        for id in list_id:

            content_subtypes = self.__getNmrLegacyContentSubTypes(id)

            if content_subtypes is None:
                continue

            nmr_input_source_dic = self.input_sources[id].get()

            file_name = nmr_input_source_dic['file_name']
            file_type = 'NEF' if nmr_input_source_dic['file_type'] == 'nef' else 'NMR-STAR'

            content_subtype = 'dist_restraint'

            if content_subtype in content_subtypes:

                stats = self.__getNmrLegacyStatsOfExptlData(id, content_subtype)

                if stats is None:
                    continue

                hydrogen_bonds = 0
                disulfide_bonds = 0
                diselenide_bonds = 0
                other_bonds = 0
                symmetric = 0
                noe_like = 0
                noe_exp_type = None

                for stat in stats:
                    for k, v in stat['number_of_constraints'].items():
                        if 'hydrogen_bonds' in k:
                            hydrogen_bonds += v
                        elif 'disulfide_bonds' in k:
                            disulfide_bonds += v
                        elif 'diselenide_bonds' in k:
                            diselenide_bonds += v
                        elif 'other_bonds' in k:
                            other_bonds += v
                        elif k == 'symmetric_constraints':
                            symmetric += v
                        else:
                            if noe_exp_type is None:
                                noe_exp_type = stat['exp_type']
                            noe_like += v
                if noe_like > 0:
                    if noe_exp_type.lower() == 'unknown':
                        noe_exp_type = 'NOE? (To be decided)'
                    else:
                        _noe_exp_type = noe_exp_type.lower()
                        if _noe_exp_type in ('csp', 'chemical shift perturbation', 'shift_perturbation'):
                            noe_exp_type = 'CSP'
                        elif _noe_exp_type == 'noe':
                            noe_exp_type = 'NOE'
                        elif _noe_exp_type in ('noe buildup', 'noe build-up', 'noe_build_up'):
                            noe_exp_type = 'NOE buildup'
                        elif _noe_exp_type in ('noe not seen', 'noe_not_seen'):
                            noe_exp_type = 'NOE not seen'
                        elif _noe_exp_type in ('pre', 'paramagnetic relaxation'):
                            noe_exp_type == 'PRE'
                        elif _noe_exp_type == 'pre solvent':
                            noe_exp_type = 'PRE solvent'
                        elif _noe_exp_type == 'roe':
                            noe_exp_type = 'ROE'

                    restraint = {'constraint_filename': file_name,
                                 'software_name': file_type,
                                 'constraint_type': 'distance',
                                 'constraint_subtype': noe_exp_type,
                                 'constraint_number': noe_like}
                    restraints.append(restraint)
                if hydrogen_bonds > 0:
                    restraint = {'constraint_filename': file_name,
                                 'software_name': file_type,
                                 'constraint_type': 'distance',
                                 'constraint_subtype': 'hydrogen bond',
                                 'constraint_number': hydrogen_bonds}
                    restraints.append(restraint)
                if disulfide_bonds > 0:
                    restraint = {'constraint_filename': file_name,
                                 'software_name': file_type,
                                 'constraint_type': 'distance',
                                 'constraint_subtype': 'disulfide bond',
                                 'constraint_number': disulfide_bonds}
                    restraints.append(restraint)
                if diselenide_bonds > 0:
                    restraint = {'constraint_filename': file_name,
                                 'software_name': file_type,
                                 'constraint_type': 'distance',
                                 'constraint_subtype': 'diselenide bond',
                                 'constraint_number': diselenide_bonds}
                    restraints.append(restraint)
                if other_bonds > 0:
                    restraint = {'constraint_filename': file_name,
                                 'software_name': file_type,
                                 'constraint_type': 'distance',
                                 'constraint_subtype': 'other bond',
                                 'constraint_number': other_bonds}
                    restraints.append(restraint)
                if symmetric > 0:
                    restraint = {'constraint_filename': file_name,
                                 'software_name': file_type,
                                 'constraint_type': 'distance',
                                 'constraint_subtype': 'symmetry',
                                 'constraint_number': symmetric}
                    restraints.append(restraint)

            content_subtype = 'dihed_restraint'

            if content_subtype in content_subtypes:

                stats = self.__getNmrLegacyStatsOfExptlData(id, content_subtype)

                if stats is None:
                    continue

                proteins = 0;
                nucleic_acids = 0
                carbohydrates = 0
                others = 0

                for stat in stats:
                    for k, v in stat['number_of_constraints_per_polymer_type'].items():
                        if k == 'protein':
                            proteins += v
                        elif k == 'nucleic_acid':
                            nucleic_acids += v
                        elif k == 'carbohydrate':
                            carbohydrates += v
                        elif k == 'other':
                            others += v
                if proteins > 0:
                    restraint = {'constraint_filename': file_name,
                                 'software_name': file_type,
                                 'constraint_type': 'protein dihedral angle',
                                 'constraint_subtype': 'Not applicable',
                                 'constraint_number': proteins}
                    restraints.append(restraint)
                if nucleic_acids > 0:
                    restraint = {'constraint_filename': file_name,
                                 'software_name': file_type,
                                 'constraint_type': 'nucleic acid dihedral angle',
                                 'constraint_subtype': 'Not applicable',
                                 'constraint_number': nucleic_acids}
                    restraints.append(restraint)
                if carbohydrates > 0:
                    restraint = {'constraint_filename': file_name,
                                 'software_name': file_type,
                                 'constraint_type': 'carbohydrate dihedral angle',
                                 'constraint_subtype': 'Not applicable',
                                 'constraint_number': carbohydrates}
                    restraints.append(restraint)
                if others > 0:
                    restraint = {'constraint_filename': file_name,
                                 'software_name': file_type,
                                 'constraint_type': 'other angle',
                                 'constraint_subtype': 'Not applicable',
                                 'constraint_number': others}
                    restraints.append(restraint)

            content_subtype = 'rdc_restraint'

            if content_subtype in content_subtypes:

                stats = self.__getNmrLegacyStatsOfExptlData(id, content_subtype)

                if stats is None:
                    continue

                rdc_total = 0

                for stat in stats:
                    for k, v in stat['number_of_constraints'].items():
                        rdc_total += v

                restraint = {'constraint_filename': file_name,
                             'software_name': file_type,
                             'constraint_type': 'intervector projection angle',
                             'constraint_subtype': 'RDC',
                             'constraint_number': rdc_total}

                restraints.append(restraint)

        return restraints if len(restraints) > 0 else None

    def getNmrPeaks(self):
        """ Return stats of NMR spectral peaks.
        """

        content_subtypes = self.getNmrContentSubTypes()

        if content_subtypes is None:
            return self.__getNmrPeaks()

        spectral_peaks = []

        content_subtype = 'spectral_peak'

        if content_subtype in content_subtypes:
            for stat in self.getNmrStatsOfExptlData(content_subtype):
                spectral_peaks.append({'list_id': stat['list_id'], 'sf_framecode': stat['sf_framecode'], 'number_of_spectral_dimensions': stat['number_of_spectral_dimensions'], 'spectral_dim': stat['spectral_dim']})

        return spectral_peaks

    def __getNmrPeaks(self):
        """ Return stats of NMR spectral peaks. (legacy)
        """

        list_id = self.getInputSourceIdsOfNmrLegacyData()

        if len(list_id) == 0:
            return []

        spectral_peaks = []

        content_subtype = 'spectral_peak'

        for id in list_id:

            content_subtypes = self.__getNmrLegacyContentSubTypes(id)

            if content_subtypes is None:
                continue

            stats = self.__getNmrLegacyStatsOfExptlData(id, content_subtype)

            if stats is None:
                continue

            for stat in stats:
                spectral_peaks.append({'list_id': stat['list_id'], 'sf_framecode': stat['sf_framecode'], 'number_of_spectral_dimensions': stat['number_of_spectral_dimensions'], 'spectral_dim': stat['spectral_dim']})

        return spectral_peaks

    def getNmrIsotopes(self):
        """ Return set of isotopes in assigned chemical shifts.
        """

        content_subtypes = self.getNmrContentSubTypes()

        if content_subtypes is None:
            return self.__getNmrIsotopes()

        content_subtype = 'chem_shift'

        if not content_subtype in content_subtypes:
            return None

        isotopes = {}

        pat = re.compile(r'^(\d+)(\D)$')

        for stat in self.getNmrStatsOfExptlData(content_subtype):
            for k in stat['number_of_assignments'].keys():
                try:
                    g = pat.search(k.split('_')[0].upper()).groups()
                    isotopes[g[0]] = g[1]
                except AttributeError:
                    pass

        return None if len(isotopes) == 0 else isotopes

    def __getNmrIsotopes(self):
        """ Return set of isotopes in assigned chemical shifts. (legacy)
        """

        list_id = self.getInputSourceIdsOfNmrLegacyData()

        if len(list_id) == 0:
            return None

        content_subtype = 'chem_shift'

        isotopes = {}

        pat = re.compile(r'^(\d+)(\D)$')

        for id in list_id:

            content_subtypes = self.__getNmrLegacyContentSubTypes(id)

            if content_subtypes is None:
                continue

            stats = self.__getNmrLegacyStatsOfExptlData(id, content_subtype)

            if stats is None:
                continue

            for stat in stats:
                for k in stat['number_of_assignments'].keys():
                    try:
                        g = pat.search(k.split('_')[0].upper()).groups()
                        isotopes[g[0]] = g[1]
                    except AttributeError:
                        pass

        return None if len(isotopes) == 0 else isotopes

    def getNmrChemShiftRefs(self):
        """ Return stats of NMR chemical shift references.
        """

        content_subtypes = self.getNmrContentSubTypes()

        if content_subtypes is None:
            return self.__getNmrChemShiftRefs()

        content_subtype = 'chem_shift_ref'

        if not content_subtype in content_subtypes:
            return None

        chem_shift_refs = []

        for stat in self.getNmrStatsOfExptlData(content_subtype):
            loop = []

            if not stat['loop'] is None:
                for l in stat['loop']:
                    _l = {}
                    for k, v in l.items():
                        if v is None or k == 'Entry_ID':
                            continue
                        _l[k.lower()] = v
                    loop.append(_l)

            saveframe_tag = {}

            if not stat['saveframe_tag'] is None:
                for k, v in stat['saveframe_tag'].items():
                    if v is None or k == 'Entry_ID' or k.startswith('Sf_'):
                        continue
                    saveframe_tag[k.lower()] = v

            chem_shift_refs.append({'list_id': stat['list_id'], 'sf_framecode': stat['sf_framecode'], 'loop': loop, 'saveframe_tag': saveframe_tag})

        return chem_shift_refs

    def __getNmrChemShiftRefs(self):
        """ Return stats of NMR chemical shift references. (legacy)
        """

        list_id = self.getInputSourceIdsOfNmrLegacyData()

        if len(list_id) == 0:
            return None

        content_subtype = 'chem_shift_ref'

        chem_shift_refs = []

        for id in list_id:

            content_subtypes = self.__getNmrLegacyContentSubTypes(id)

            if content_subtypes is None:
                continue

            stats = self.__getNmrLegacyStatsOfExptlData(id, content_subtype)

            if stats is None:
                continue

            for stat in stats:
                loop = []

                if not stat['loop'] is None:
                    for l in stat['loop']:
                        _l = {}
                        for k, v in l.items():
                            if v is None or k == 'Entry_ID':
                                continue
                            _l[k.lower()] = v
                        loop.append(_l)

                saveframe_tag = {}

                if not stat['saveframe_tag'] is None:
                    for k, v in stat['saveframe_tag'].items():
                        if v is None or k == 'Entry_ID' or k.startswith('Sf_'):
                            continue
                        saveframe_tag[k.lower()] = v

                chem_shift_refs.append({'list_id': stat['list_id'], 'sf_framecode': stat['sf_framecode'], 'loop': loop, 'saveframe_tag': saveframe_tag})

        return None if len(chem_shift_refs) == 0 else chem_shift_refs

    def getNmrPolymerSequenceOf(self, chain_id):
        """ Retrieve NMR polymer sequence having a given chain_id.
        """

        id = self.getInputSourceIdOfNmrData()

        if id < 0:
            ids = self.getInputSourceIdsOfNmrLegacyData()
            if len(ids) == 0:
                return None
            id = ids[0]

        nmr_input_source_dic = self.input_sources[id].get()

        nmr_polymer_sequence = nmr_input_source_dic['polymer_sequence']

        return next((ps for ps in nmr_polymer_sequence if ps['chain_id'] == chain_id), None)

    def getModelPolymerSequenceOf(self, chain_id):
        """ Retrieve model polymer sequence having a given chain_id.
        """

        id = self.getInputSourceIdOfCoord()

        if id < 0:
            return None

        cif_input_source_dic = self.input_sources[id].get()

        cif_polymer_sequence = cif_input_source_dic['polymer_sequence']

        return next((ps for ps in cif_polymer_sequence if ps['chain_id'] == chain_id), None)

    def getNmrSeq1LetterCodeOf(self, chain_id, fullSequence=True, unmappedSeqId=[]):
        """ Retrieve NMR polymer sequence (1-letter code) having a given chain_id.
        """

        id = self.getInputSourceIdOfNmrData()

        if id < 0:
            ids = self.getInputSourceIdsOfNmrLegacyData()
            if len(ids) == 0:
                return None
            id = ids[0]

        nmr_input_source_dic = self.input_sources[id].get()

        nmr_polymer_sequence = nmr_input_source_dic['polymer_sequence']

        ps = next((ps for ps in nmr_polymer_sequence if ps['chain_id'] == chain_id), None)

        if ps is None:
            return None

        code = ''

        for seq_id, comp_id in zip(ps['seq_id'], ps['comp_id']):

            if not fullSequence and seq_id in unmappedSeqId:
                continue

            if comp_id in self.monDict3:
                code += self.monDict3[comp_id]
            else:
                code += '(' + comp_id + ')'

        return code

    def getModelSeq1LetterCodeOf(self, chain_id):
        """ Retrieve model polymer sequence (1-letter code) having a given chain_id.
        """

        id = self.getInputSourceIdOfCoord()

        if id < 0:
            return None

        cif_input_source_dic = self.input_sources[id].get()

        cif_polymer_sequence = cif_input_source_dic['polymer_sequence']

        ps = next((ps for ps in cif_polymer_sequence if ps['chain_id'] == chain_id), None)

        if ps is None:
            return None

        code = ''
        for comp_id in ps['comp_id']:
            if comp_id in self.monDict3:
                code += self.monDict3[comp_id]
            else:
                code += '(' + comp_id + ')'

        return code

    def getNmrPolymerSequenceWithModelChainId(self, cif_chain_id):
        """ Retrieve NMR polymer sequence corresponding to a given coordinate chain_id.
        """

        chain_assign_dic = self.chain_assignment.get()

        key = 'model_poly_seq_vs_nmr_poly_seq'

        if not key in chain_assign_dic:
            return None

        if chain_assign_dic[key] is None:
            return None

        for chain_assign in chain_assign_dic[key]:

            if chain_assign['ref_chain_id'] == cif_chain_id:
                return self.getNmrPolymerSequenceOf(chain_assign['test_chain_id'])

        return None

    def getSequenceAlignmentWithNmrChainId(self, nmr_chain_id):
        """ Retrieve sequence alignment (nmr vs model) of a given NMR chain_id.
        """

        chain_assign_dic = self.chain_assignment.get()

        key = 'nmr_poly_seq_vs_model_poly_seq'

        if not key in chain_assign_dic:
            return None

        if chain_assign_dic[key] is None:
            return None

        for chain_assign in chain_assign_dic[key]:

            if chain_assign['ref_chain_id'] == nmr_chain_id:

                if chain_assign['conflict'] > 0:
                    return None

                cif_chain_id = chain_assign['test_chain_id']

                sequence_align_dic = self.sequence_alignment.get()

                if not key in sequence_align_dic:
                    return None

                if sequence_align_dic[key] is None:
                    return None

                for sequence_align in sequence_align_dic[key]:

                    if sequence_align['ref_chain_id'] == nmr_chain_id and sequence_align['test_chain_id'] == cif_chain_id:

                        if sequence_align['conflict'] > 0:
                            return None

                        return sequence_align

        return None

    def getSequenceAlignmentWithModelChainId(self, cif_chain_id):
        """ Retrieve sequence alignment (model vs nmr) of a given coordinate chain_id.
        """

        chain_assign_dic = self.chain_assignment.get()

        key = 'model_poly_seq_vs_nmr_poly_seq'

        if not key in chain_assign_dic:
            return None

        if chain_assign_dic[key] is None:
            return None

        for chain_assign in chain_assign_dic[key]:

            if chain_assign['ref_chain_id'] == cif_chain_id:

                if chain_assign['conflict'] > 0:
                    return None

                nmr_chain_id = chain_assign['test_chain_id']

                sequence_align_dic = self.sequence_alignment.get()

                if not key in sequence_align_dic:
                    return None

                if sequence_align_dic[key] is None:
                    return None

                for sequence_align in sequence_align_dic[key]:

                    if sequence_align['ref_chain_id'] == cif_chain_id and sequence_align['test_chain_id'] == nmr_chain_id:

                        if sequence_align['conflict'] > 0:
                            return None

                        return sequence_align

        return None

    def getModelPolymerSequenceWithNmrChainId(self, nmr_chain_id):
        """ Retrieve coordinate polymer sequence corresponding to a given NMR chain_id.
        """

        chain_assign_dic = self.chain_assignment.get()

        key = 'nmr_poly_seq_vs_model_poly_seq'

        if not key in chain_assign_dic:
            return None

        if chain_assign_dic[key] is None:
            return None

        for chain_assign in chain_assign_dic[key]:

            if chain_assign['ref_chain_id'] == nmr_chain_id:
                return self.getModelPolymerSequenceOf(chain_assign['test_chain_id'])

        return None

    def getNmrSeq1LetterCodeWithModelChainId(self, cif_chain_id):
        """ Retrieve NMR polymer sequence (1-letter code) corresponding to a given coordinate chain_id.
        """

        fullSeqeucne = self.getInputSourceIdOfNmrData() != -1
        unmappedSeqId = []

        chain_assign_dic = self.chain_assignment.get()

        key = 'model_poly_seq_vs_nmr_poly_seq'

        if not key in chain_assign_dic:
            return None

        if chain_assign_dic[key] is None:
            return None

        if not fullSeqeucne:

            _key = 'nmr_poly_seq_vs_model_poly_seq'

            if _key in chain_assign_dic and not chain_assign_dic[_key] is None:

                for _chain_assign in chain_assign_dic[_key]:

                    if _chain_assign['test_chain_id'] == cif_chain_id:

                        if 'unmapped_sequence' in _chain_assign:

                            for unmapped_sequence in _chain_assign['unmapped_sequence']:
                                unmappedSeqId.append(unmapped_sequence['ref_seq_id'])

                        break

        for chain_assign in chain_assign_dic[key]:

            if chain_assign['ref_chain_id'] == cif_chain_id:
                return self.getNmrSeq1LetterCodeOf(chain_assign['test_chain_id'], fullSequence=fullSeqeucne, unmappedSeqId=unmappedSeqId)

        return None

    def getModelSeq1LetterCodeWithNmrChainId(self, nmr_chain_id):
        """ Retrieve coordinate polymer sequence (1-letter code) corresponding to a given NMR chain_id.
        """

        chain_assign_dic = self.chain_assignment.get()

        key = 'nmr_poly_seq_vs_model_poly_seq'

        if not key in chain_assign_dic:
            return None

        if chain_assign_dic[key] is None:
            return None

        for chain_assign in chain_assign_dic[key]:

            if chain_assign['ref_chain_id'] == nmr_chain_id:
                return self.getModelSeq1LetterCodeOf(chain_assign['test_chain_id'])

        return None

    def getAverageRMSDWithinRange(self, cif_chain_id, cif_beg_seq_id, cif_end_seq_id):
        """ Calculate average RMSD of alpha carbons/phosphates within a given range in the ensemble.
        """

        poly_seq = self.getModelPolymerSequenceOf(cif_chain_id)

        if poly_seq is None or not 'type' in poly_seq:
            return None

        type = ent['type']

        if 'polypeptide' in type:
            rmsd_label = 'ca_rmsd'
        elif 'ribonucleotide' in type:
            rmsd_label = 'p_rmsd'
        else:
            return None

        if not rmsd_label in ent:
            return None

        if not (cif_beg_seq_id in poly_seq['seq_id'] and cif_end_seq_id in poly_seq['seq_id']):
            return None

        rmsd = [s[rmsd_label] for s in poly_seq if s['seq_id'] >= cif_beg_seq_id and s['seq_id'] <= cif_end_seq_id and not s[rmsd_label] is None]

        if len(rmsd) == 0:
            return None

        return sum[rmsd] / len(rmsd)

    def getTotalErrors(self):
        return self.error.getTotal()

    def getTotalWarnings(self):
        return self.warning.getTotal()

    def __setStatus(self, status):

        if status in self.status_codes:
            self.__report['information']['status'] = status
        else:
            logging.error('+NmrDpReport.__setStatus() ++ Error  - Unknown item type %s' % item)
            raise KeyError('+NmrDpReport.__setStatus() ++ Error  - Unknown item type %s' % item)

    def setError(self):

        if not self.__immutable:
            self.__report['error'] = self.error.get()

            self.__setStatus('Error')

        else:
            logging.warning('+NmrDpReport.setError() ++ Warning  - No effects on NMR data processing report because the report is immutable')
            raise UserWarning('+NmrDpReport.setError() ++ Warning  - No effects on NMR data processing report because the report is immutable')

    def setWarning(self):

        if not self.__immutable:
            self.__report['warning'] = self.warning.get()

            if not self.isError():
                self.__setStatus('Warning')

        else:
            logging.warning('+NmrDpReport.setWarning() ++ Warning  - No effects on NMR data processing report because the report is immutable')
            raise UserWarning('+NmrDpReport.setWarning() ++ Warning  - No effects on NMR data processing report because the report is immutable')

    def setDiamagnetic(self, diamagnetic):

        if type(diamagnetic) is bool:
            self.__report['information']['diamagnetic'] = diamagnetic

        else:
            logging.warning('+NmrDpReport.setDiamagnetic() ++ Warning  - No effects on NMR data processing report because input variable is not boolean type')
            raise UserDiamagnetic('+NmrDpReport.setDiamagnetic() ++ Warning  - No effects on NMR data processing report because input variable is not boolean type')

    def setDisulfideBond(self, disulfide_bond):

        if type(disulfide_bond) is bool:
            self.__report['information']['disulfide_bond'] = disulfide_bond

        else:
            logging.warning('+NmrDpReport.setDisulfideBond() ++ Warning  - No effects on NMR data processing report because input variable is not boolean type')
            raise UserDiamagnetic('+NmrDpReport.setDisulfideBond() ++ Warning  - No effects on NMR data processing report because input variable is not boolean type')

    def setOtherBond(self, other_bond):

        if type(other_bond) is bool:
            self.__report['information']['other_bond'] = other_bond

        else:
            logging.warning('+NmrDpReport.setOtherBond() ++ Warning  - No effects on NMR data processing report because input variable is not boolean type')
            raise UserDiamagnetic('+NmrDpReport.setOtherBond() ++ Warning  - No effects on NMR data processing report because input variable is not boolean type')

    def setCyclicPolymer(self, cyclic_polymer):

        if type(cyclic_polymer) is bool:
            self.__report['information']['cyclic_polymer'] = cyclic_polymer

        else:
            logging.warning('+NmrDpReport.setCyclicPolymer() ++ Warning  - No effects on NMR data processing report because input variable is not boolean type')
            raise UserDiamagnetic('+NmrDpReport.setCyclicPolymer() ++ Warning  - No effects on NMR data processing report because input variable is not boolean type')

    def setMutable(self):
        self.__immutable = False

    def get(self):

        if not self.__immutable:
            self.__report['information']['input_sources'] = [input_source.get() for input_source in self.input_sources]
            self.__report['information']['sequence_alignments'] = self.sequence_alignment.get()
            self.__report['information']['chain_assignments'] = self.chain_assignment.get()

            self.__immutable = True

        return self.__report

    def load(self, report):
        """ Retrieve NMR data processing report from JSON content.
            @return: True for success or False otherwise
        """

        if report is None:
            return False

        self.__report = copy.copy(report)

        self.input_sources = []

        for contents in self.__report['information']['input_sources']:

            input_source = NmrDpReportInputSource()
            input_source.put(contents)

            self.input_sources.append(input_source)

        self.sequence_alignment.put(self.__report['information']['sequence_alignments'])
        self.chain_assignment.put(self.__report['information']['chain_assignments'])

        if self.__report['error'] is None:
            self.error = NmrDpReportError()
        else:
            self.error.put(self.__report['error'])

        if self.__report['warning'] is None:
            self.warning = NmrDpReportWarning()
        else:
            self.warning.put(self.__report['warning'])

        self.setMutable()

        return True

    def writeFile(self, out_path):
        """ Write NMR data processing report as JSON file.
            @return: True for success or False otherwise
        """

        if self.get() is None:
            return False

        with open(out_path, 'w') as file:
            file.write(json.dumps(self.get(), indent=2))

        return True

    def loadFile(self, in_path):
        """ Retrieve NMR data processing report from JSON file.
            @return: True for success or False otherwise
        """

        with open(in_path, 'r') as file:

            report = json.loads(file.read())

            if report is None:
                return False

            self.load(report)

        return True

    def inheritFormatIssueErrors(self, prev_report):
        """ Inherit format issue errors from the previous report (e.g. nmr-*-consistency-check workflow operation).
        """

        item = 'format_issue'

        if not self.__immutable:

            file_name = self.input_sources[self.getInputSourceIdOfNmrData()].get()['file_name']
            _file_name = prev_report.input_sources[prev_report.getInputSourceIdOfNmrData()].get()['file_name']

            value_list = prev_report.error.getValueList(item, _file_name)

            if value_list is None:
                return

            for c in value_list:

                if 'file_name' in c:
                    c['file_name'] = file_name

                self.error.appendDescription(item, c)

        else:
            logging.warning('+NmrDpReport.inheritFormatIssueErrors() ++ Warning  - No effects on NMR data processing report because the report is immutable')
            raise UserWarning('+NmrDpReport.inheritFormatIssueErrors() ++ Warning  - No effects on NMR data processing report because the report is immutable')

    def setCorrectedError(self, prev_report):
        """ Initialize history of corrected errors in the previous report.
        """

        if not self.__immutable:

            file_name = self.input_sources[self.getInputSourceIdOfNmrData()].get()['file_name']
            _file_name = prev_report.input_sources[prev_report.getInputSourceIdOfNmrData()].get()['file_name']

            for item in prev_report.error.get().keys():

                if item == 'total':
                    continue

                value_list = self.error.getValueList(item, file_name)
                _value_list = prev_report.error.getUniqueValueList(item, _file_name)

                if _value_list is None:
                    continue

                list = []

                for _c in _value_list:

                    if value_list is None:
                        list.append(_c)

                    else:
                        try:
                            next(c for c in value_list if c['sf_framecode'] == _c['sf_framecode'] and c['description'] == _c['description'])
                        except StopIteration:
                            list.append(_c)

                for c in list:
                    self.error.appendDescription(item, c)

                if len(list) > 0:
                    self.setError()

        else:
            logging.warning('+NmrDpReport.setCorrectedError() ++ Warning  - No effects on NMR data processing report because the report is immutable')
            raise UserWarning('+NmrDpReport.setCorrectedError() ++ Warning  - No effects on NMR data processing report because the report is immutable')

    def setCorrectedWarning(self, prev_report):
        """ Initialize history of corrected warnings in the previous report.
        """

        if not self.__immutable:

            ignorable_warning_types = ['auth_atom_nomenclature_mismatch', 'ccd_mismatch', 'enum_mismatch_ignorable', 'skipped_saveframe_category', 'skipped_loop_category',
                                       'anomalous_chemical_shift', 'unusual_chemical_shift',
                                       'anomalous_data', 'unusual_data', 'remarkable_data', 'insufficient_data', 'conflicted_data', 'inconsistent_data',
                                       'total']

            self.corrected_warning = NmrDpReportWarning()

            file_name = self.input_sources[self.getInputSourceIdOfNmrData()].get()['file_name']
            _file_name = prev_report.input_sources[prev_report.getInputSourceIdOfNmrData()].get()['file_name']

            for item in prev_report.warning.get().keys():

                if item in ignorable_warning_types:
                    continue

                value_list = self.warning.getValueList(item, file_name)
                _value_list = prev_report.warning.getUniqueValueList(item, _file_name)

                if _value_list is None:
                    continue

                list = []

                for _c in _value_list:

                    if value_list is None:
                        list.append(_c)

                    else:
                        try:
                            next(c for c in value_list if c['sf_framecode'] == _c['sf_framecode'] and c['description'] == _c['description'])
                        except StopIteration:
                            list.append(_c)

                for c in list:
                    self.corrected_warning.appendDescription(item, c)

            self.__report['corrected_warning'] = self.corrected_warning.get()

        else:
            logging.warning('+NmrDpReport.setCorrectedWarning() ++ Warning  - No effects on NMR data processing report because the report is immutable')
            raise UserWarning('+NmrDpReport.setCorrectedWarning() ++ Warning  - No effects on NMR data processing report because the report is immutable')

class NmrDpReportInputSource:
    """ Wrapper class for data processing report of NMR data (input source).
    """

    def __init__(self):
        self.items = ('file_name', 'file_type', 'content_type', 'content_subtype',
                      'polymer_sequence', 'polymer_sequence_in_loop',
                      'non_standard_residue', 'disulfide_bond', 'other_bond',
                      'stats_of_exptl_data')
        self.file_types = ('pdbx', 'nef', 'nmr-star')
        self.content_types = ('model', 'nmr-data-nef', 'nmr-data-str', 'nmr-chemical-shifts', 'nmr-restraints')
        self.content_subtypes = ('coordinate', 'non_poly', 'entry_info', 'poly_seq', 'entity', 'chem_shift', 'chem_shift_ref', 'dist_restraint', 'dihed_restraint', 'rdc_restraint', 'spectral_peak')

        self.__contents = {item:None for item in self.items}

    def setItemValue(self, item, value):

        if item in self.items:

            if item == 'file_type' and not value in self.file_types:
                logging.error('+NmrDpReportInputSource.setItemValue() ++ Error  - Unknown file type %s' % value)
                raise ValueError('+NmrDpReportInputSource.setItemValue() ++ Error  - Unknown file type %s' % value)

            elif item == 'content_type' and not value in self.content_types:
                logging.error('+NmrDpReportInputSource.setItemValue() ++ Error  - Unknown content type %s' % value)
                raise ValueError('+NmrDpReportInputSource.setItemValue() ++ Error  - Unknown content type %s' % value)

            elif item == 'content_subtype':

                for k in value:

                    if not k in self.content_subtypes:
                        logging.error('+NmrDpReportInputSource.setItemValue() ++ Error  - Unknown content subtype in %s' % value.keys())
                        raise ValueError('+NmrDpReportInputSource.setItemValue() ++ Error  - Unknown content subtype in %s' % value.keys())

                non_positive_keys = [k for k in value if int(value[k]) <= 0]

                for k in non_positive_keys:
                    value.pop(k)

                if len(value) > 0:
                    self.__contents[item] = value

            else:
                self.__contents[item] = value

        else:
            logging.error('+NmrDpReportInputSource.setItemValue() ++ Error  - Unknown item type %s' % item)
            raise KeyError('+NmrDpReportInputSource.setItemValue() ++ Error  - Unknown item type %s' % item)

    def get(self):
        return self.__contents

    def put(self, contents):
        self.__contents = contents

    def updateNonStandardResidueByExptlData(self, chain_id, seq_id, content_subtype):
        """ Update specified non_starndard_residue by experimental data.
        """

        try:

            c = next(c for c in self.__contents['non_standard_residue'] if c['chain_id'] == chain_id)

            if seq_id in c['seq_id']:
                c['exptl_data'][c['seq_id'].index(seq_id)][content_subtype] = True

            else:
                logging.error('+NmrDpReportInputSource.updateNonStandardResidueByExptlData() ++ Error  - Unknown seq_id %s' % seq_id)
                raise KeyError('+NmrDpReportInputSource.updateNonStandardResidueByExptlData() ++ Error  - Unknown seq_id %s' % seq_id)

        except StopIteration:
            logging.error('+NmrDpReportInputSource.updateNonStandardResidueByExptlData() ++ Error  - Unknown chain_id %s' % chain_id)
            raise KeyError('+NmrDpReportInputSource.updateNonStandardResidueByExptlData() ++ Error  - Unknown chain_id %s' % chain_id)

class NmrDpReportSequenceAlignment:
    """ Wrapper class for data processing report of NMR data (sequence alignment).
    """

    def __init__(self):
        self.items = ('model_poly_seq_vs_coordinate', 'model_poly_seq_vs_nmr_poly_seq', 'nmr_poly_seq_vs_model_poly_seq', 'nmr_poly_seq_vs_chem_shift', 'nmr_poly_seq_vs_dist_restraint', 'nmr_poly_seq_vs_dihed_restraint', 'nmr_poly_seq_vs_rdc_restraint', 'nmr_poly_seq_vs_spectral_peak')

        self.__contents = {item:None for item in self.items}

    def setItemValue(self, item, value):

        if item in self.items:
            self.__contents[item] = value

        else:
            logging.error('+NmrDpReportSequenceAlignment.setItemValue() ++ Error  - Unknown item type %s' % item)
            raise KeyError('+NmrDpReportSequenceAlignment.setItemValue() ++ Error  - Unknown item type %s' % item)

    def get(self):
        return self.__contents

    def put(self, contents):
        self.__contents = contents

class NmrDpReportChainAssignment:
    """ Wrapper class for data processing report of NMR data (chain assignment).
    """

    def __init__(self):
        self.items = ('model_poly_seq_vs_nmr_poly_seq', 'nmr_poly_seq_vs_model_poly_seq')

        self.__contents = {item:None for item in self.items}

    def setItemValue(self, item, value):

        if item in self.items:
            self.__contents[item] = value

        else:
            logging.error('+NmrDpReportChainAssignment.setItemValue() ++ Error  - Unknown item type %s' % item)
            raise KeyError('+NmrDpReportChainAssignment.setItemValue() ++ Error  - Unknown item type %s' % item)

    def get(self):
        return self.__contents

    def put(self, contents):
        self.__contents = contents

class NmrDpReportError:
    """ Wrapper class for data processing report of NMR data (error).
    """

    def __init__(self):
        self.items = ('internal_error', 'format_issue', 'missing_mandatory_content', 'missing_mandatory_item', 'sequence_mismatch',
                      'invalid_data', 'invalid_atom_nomenclature', 'invalid_atom_type', 'invalid_isotope_number', 'invalid_ambiguity_code',
                      'multiple_data', 'missing_data', 'duplicated_index', 'anomalous_data')

        self.__contents = {item:None for item in self.items}

        self.__contents['total'] = 0

        self.chk_row_pat = re.compile(r'^\[Check row of (.*)\] (.*)$')
        self.chk_rows_pat = re.compile(r'\[Check rows of (.*)\] (.*)$')

    def appendDescription(self, item, value):

        if item in self.items:

            if self.__contents[item] is None:
                self.__contents[item] = []

            if item != 'internal_error' and 'category' in value:
                value['category'] = value['category'].lstrip('_')

            if item != 'internal_error' and 'description' in value:
                d = value['description']

                if d.startswith('[Check row of'):
                    g = self.chk_row_pat.search(d).groups()

                    loc = {}
                    for i in g[0].split(','):
                        p = i.lstrip()
                        s = p.index(' ')
                        loc[p[0: s]] = p[s:].lstrip()

                    value['row_location'] = loc
                    value['description'] = g[1]

                elif d.startswith('[Check rows of'):
                    g = self.chk_rows_pat.search(d).groups()

                    locs = {}
                    for i in g[0].split(','):
                        p = i.lstrip()
                        q = p.split(' ', 1)
                        locs[q[0]] = re.sub(' vs ', ',', q[1]).split(',')

                    value['row_locations'] = locs
                    value['description'] = g[1]

            self.__contents[item].append(value)

            self.__contents['total'] += 1

        else:
            logging.error('+NmrDpReportError.appendDescription() ++ Error  - Unknown item type %s' % item)
            raise KeyError('+NmrDpReportError.appendDescription() ++ Error  - Unknown item type %s' % item)

    def get(self):
        return self.__contents

    def put(self, contents):
        self.__contents = contents

    def getTotal(self):
        """ Return total number of errors.
            @return: total number of errors
        """

        return self.__contents['total']

    def exists(self, file_name, sf_framecode):
        """ Return whether an error specified by file name and saveframe exists.
            @return: True for an error exists or False otherwise
        """

        for item in self.__contents.keys():

            if item in ['total', 'internal_error'] or self.__contents[item] is None:
                continue

            try:
                next(c for c in self.__contents[item] if c['file_name'] == file_name and 'sf_framecode' in c and c['sf_framecode'] == sf_framecode)
                return True
            except StopIteration:
                pass

        return False

    def getValueList(self, item, file_name, key=None):
        """ Return list of error values specified by item name and file name.
        """

        if item in ['total', 'internal_error'] or self.__contents is None or (not item in self.__contents.keys()) or self.__contents[item] is None:
            return None

        return [c for c in self.__contents[item] if c['file_name'] == file_name or (key is None or key in c['description'])]

    def getValueListWithSf(self, item, file_name, sf_framecode, key=None):
        """ Return list of error values specified by item name, file name, and saveframe.
        """

        if item in ['total', 'internal_error'] or self.__contents is None or (not item in self.__contents.keys()) or self.__contents[item] is None:
            return None

        return [c for c in self.__contents[item] if c['file_name'] == file_name and c['sf_framecode'] == sf_framecode and (key is None or key in c['description'])]

    def getUniqueValueList(self, item, file_name):
        """ Return list of error values having unique sf_framecode and description.
        """

        if item in ['total', 'internal_error'] or self.__contents is None or (not item in self.__contents.keys()) or self.__contents[item] is None:
            return None

        list = []

        keys = set()

        for c in self.getValueList(item, file_name):

            if not 'sf_framecode' in c:
                continue

            key = c['sf_framecode'] + c['description']

            if key in keys:
                continue

            if 'row_location' in c:
                del c['row_location']

            elif 'row_locations' in c:
                del c['row_locations']

            list.append(c)

            keys.add(key)

        return list

    def getDescription(self, item, file_name, sf_framecode):
        """ Return error description specified by item name, file name, and saveframe.
        """

        if item in ['total', 'internal_error'] or self.__contents is None or (not item in self.__contents.keys()) or self.__contents[item] is None:
            return None

        try:
            c = next(c for c in self.__contents[item] if c['file_name'] == file_name and 'sf_framecode' in c and c['sf_framecode'] == sf_framecode)
            return c['description']
        except StopIteration:
            return None

    def getCombinedDescriptions(self, file_name, sf_framecode):
        """ Return combined error descriptions specified by file name and saveframe.
        """

        if self.__contents is None:
            return None

        d = []

        for item in self.items:

            if item == 'internal_error' or self.__contents[item] is None:
                continue

            for c in self.__contents[item]:

                if c['file_name'] == file_name and 'sf_framecode' in c and c['sf_framecode'] == sf_framecode:
                    d.append(item + ': ' + c['description'])

        if len(d) == 0:
            return None

        return d

class NmrDpReportWarning:
    """ Wrapper class for data processing report of NMR unified data (warning).
    """

    def __init__(self):
        self.items = ('encouragement', 'missing_content', 'missing_saveframe', 'missing_data', 'enum_mismatch',
                      'enum_mismatch_ignorable', 'corrected_format_issue',
                      'disordered_index', 'sequence_mismatch',
                      'atom_nomenclature_mismatch', 'auth_atom_nomenclature_mismatch', 'ccd_mismatch', 'ambiguity_code_mismatch',
                      'skipped_saveframe_category', 'skipped_loop_category',
                      'anomalous_chemical_shift', 'unusual_chemical_shift',
                      'anomalous_data', 'unusual_data', 'remarkable_data', 'insufficient_data',
                      'conflicted_data', 'inconsistent_data', 'redundant_data',
                      'concatenated_sequence', 'not_superimposed_model')

        self.__contents = {item:None for item in self.items}

        self.__contents['total'] = 0

        self.chk_row_pat = re.compile(r'^\[Check row of (.*)\] (.*)$')
        self.chk_rows_pat = re.compile(r'\[Check rows of (.*)\] (.*)$')

    def appendDescription(self, item, value):

        if item in self.items:

            if self.__contents[item] is None:
                self.__contents[item] = []

            if 'category' in value:
                value['category'] = value['category'].lstrip('_')

            if 'description' in value:
                d = value['description']

                if d.startswith('[Check row of'):
                    g = self.chk_row_pat.search(d).groups()

                    loc = {}
                    for i in g[0].split(','):
                        p = i.lstrip()
                        s = p.index(' ')
                        loc[p[0: s]] = p[s:].lstrip()

                    value['row_location'] = loc
                    value['description'] = g[1]

                elif d.startswith('[Check rows of'):
                    g = self.chk_rows_pat.search(d).groups()

                    locs = {}
                    for i in g[0].split(','):
                        p = i.lstrip()
                        q = p.split(' ', 1)
                        locs[q[0]] = re.sub(' vs ', ',', q[1]).split(',')

                    value['row_locations'] = locs
                    value['description'] = g[1]

            self.__contents[item].append(value)

            self.__contents['total'] += 1

        else:
            logging.error('+NmrDpReportWarning.appendDescription() ++ Error  - Unknown item type %s' % item)
            raise KeyError('+NmrDpReportWarning.appendDescription() ++ Error  - Unknown item type %s' % item)

    def get(self):
        return self.__contents

    def put(self, contents):
        self.__contents = contents

    def getTotal(self):
        """ Return total number of warnings.
            @return: total number of warnings
        """

        return self.__contents['total']

    def exists(self, file_name, sf_framecode):
        """ Return whether a warning specified by file name and saveframe exists.
            @return: True for a warning exists or False otherwise
        """

        for item in self.__contents.keys():

            if item in ['total', 'enum_mismatch_ignorable'] or self.__contents[item] is None:
                continue

            try:
                next(c for c in self.__contents[item] if c['file_name'] == file_name and 'sf_framecode' in c and c['sf_framecode'] == sf_framecode)
                return True
            except StopIteration:
                pass

        return False

    def getValueList(self, item, file_name, key=None):
        """ Return list of warning values specified by item name and file name.
        """

        if item == 'total' or self.__contents is None or (not item in self.__contents.keys()) or self.__contents[item] is None:
            return None

        return [c for c in self.__contents[item] if c['file_name'] == file_name and (key is None or key in c['description'])]

    def getValueListWithSf(self, item, file_name, sf_framecode, key=None):
        """ Return list of warning values specified by item name, file name, and saveframe.
        """

        if item == 'total' or self.__contents is None or (not item in self.__contents.keys()) or self.__contents[item] is None:
            return None

        return [c for c in self.__contents[item] if c['file_name'] == file_name and c['sf_framecode'] == sf_framecode and (key is None or key in c['description'])]

    def getUniqueValueList(self, item, file_name):
        """ Return list of warning values having unique sf_framecode and description.
        """

        if item == 'total' or self.__contents is None or (not item in self.__contents.keys()) or self.__contents[item] is None:
            return None

        list = []

        keys = set()

        for c in self.getValueList(item, file_name):

            if not 'sf_framecode' in c:
                continue

            key = c['sf_framecode'] + c['description']

            if key in keys:
                continue

            if 'row_location' in c:
                del c['row_location']

            elif 'row_locations' in c:
                del c['row_locations']

            list.append(c)

            keys.add(key)

        return list

    def getDescription(self, item, file_name, sf_framecode):
        """ Return warning description specified by item name, file name, and saveframe.
        """

        if item == 'total' or self.__contents is None or (not item in self.__contents.keys()) or self.__contents[item] is None:
            return None

        try:
            c = next(c for c in self.__contents[item] if c['file_name'] == file_name and 'sf_framecode' in c and c['sf_framecode'] == sf_framecode)
            return c['description']
        except StopIteration:
            return None

    def getCombinedDescriptions(self, file_name, sf_framecode):
        """ Return combined warning descriptions specified by file name and saveframe.
        """

        if self.__contents is None:
            return None

        d = []

        for item in self.items:

            if item == 'enum_mismatch_ignorable' or self.__contents[item] is None:
                continue

            for c in self.__contents[item]:

                if c['file_name'] == file_name and 'sf_framecode' in c and c['sf_framecode'] == sf_framecode:
                    d.append(item + ': ' + c['description'])

        if len(d) == 0:
            return None

        return d

    def sortChemicalShiftValidation(self):
        """ Sort warning about anomalous/unusual chemical shift.
        """

        if self.__contents is None:
            return

        d = []

        anomalous_cs = False
        mixed_status = False

        for item in ['anomalous_data', 'anomalous_chemical_shift', 'unusual_data', 'unusual_chemical_shift']:

            if not item in self.__contents.keys() or self.__contents[item] is None:
                continue

            _d = [c for c in self.__contents[item] if 'sigma' in c] if 'data' in item else self.__contents[item]
            _d_ = copy.copy(_d)

            if len(_d) > 0:

                if 'anomalous' in item:
                    anomalous_cs = True
                    for c in _d:
                        c['status'] = 'A'

                elif anomalous_cs:
                    mixed_status = True

                d.extend(_d)

                for c in _d_:
                    self.__contents[item].remove(c)

                if len(self.__contents[item]) == 0:
                    self.__contents[item] = None

        if len(d) == 0:
            return

        item = 'anomalous_chemical_shift' if anomalous_cs else 'unusual_chemical_shift'

        self.__contents[item] = []

        if mixed_status:
            for c in d:
                if not 'status' in c:
                    c['status'] = 'S'
                if not 'sigma' in c:
                    c['sigma'] = 0.0

            for c in sorted(sorted(d, key=lambda i: i['sigma'], reverse=True), key=lambda j: j['status']):
                if 'description_alt' in c:
                    c['description'] = c['description_alt']
                    del c['description_alt']
                del c['sigma']
                self.__contents[item].append(c)

        else:
            for c in d:
                if 'status' in c and not anomalous_cs:
                    del c['status']
                if not 'sigma' in c:
                    c['sigma'] = 0.0

            for c in sorted(d, key=lambda i: i['sigma'], reverse=True):
                if 'description_alt' in c:
                    c['description'] = c['description_alt']
                    del c['description_alt']
                del c['sigma']
                self.__contents[item].append(c)
