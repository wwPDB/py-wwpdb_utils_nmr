##
# File: NmrDpValidation.py
# Date: 06-Jan-2026
#
# Updates:
##
""" Wrapper class for NMR data validation.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "4.8.1"

import itertools
import copy
import math
import pynmrstar
import numpy
import functools

from operator import itemgetter
from typing import IO, List, Union, Tuple, Optional

try:
    from wwpdb.utils.nmr.NmrDpConstant import (SF_CATEGORIES,
                                               LP_CATEGORIES,
                                               CUTOFF_AROMATIC,
                                               CUTOFF_PARAMAGNETIC,
                                               VICINITY_AROMATIC,
                                               VICINITY_PARAMAGNETIC,
                                               CUTOFF_BOND_LENGTH,
                                               MAGIC_ANGLE,
                                               INCONSIST_OVER_CONFLICTED,
                                               R_CONFLICTED_DIST_RESTRAINT,
                                               R_INCONSISTENT_DIST_RESTRAINT,
                                               INDEX_TAGS,
                                               CONSIST_ID_TAGS,
                                               PK_KEY_ITEMS,
                                               DATA_ITEMS,
                                               CONSIST_DATA_ITEMS,
                                               NUM_DIM_ITEMS,
                                               ALLOWED_TAGS,
                                               DISALLOWED_PK_TAGS,
                                               SF_ALLOWED_TAGS,
                                               AUX_LP_CATEGORIES,
                                               LINKED_LP_CATEGORIES,
                                               AUX_ALLOWED_TAGS,
                                               ITEM_NAMES_IN_CS_LOOP,
                                               ITEM_NAMES_IN_PK_LOOP,
                                               ITEM_NAMES_IN_DIST_LOOP,
                                               ITEM_NAMES_IN_DIHED_LOOP,
                                               ITEM_NAMES_IN_RDC_LOOP)
    from wwpdb.utils.nmr.nef.NEFTranslator import (NEFTranslator,
                                                   PARAMAGNETIC_ELEMENTS,
                                                   FERROMAGNETIC_ELEMENTS,
                                                   MAX_DIM_NUM_OF_SPECTRA)
    from wwpdb.utils.nmr.NmrDpReport import NmrDpReport
    from wwpdb.utils.nmr.AlignUtil import (LOW_SEQ_COVERAGE,
                                           LARGE_ASYM_ID,
                                           emptyValue,
                                           monDict3,
                                           protonBeginCode,
                                           pseProBeginCode,
                                           aminoProtonCode,
                                           rdcBbPairCode,
                                           letterToDigit,
                                           alignPolymerSequence,
                                           assignPolymerSequence)
    from wwpdb.utils.nmr.io.CifReader import (CifReader,
                                              LEN_MAJOR_ASYM_ID)
    from wwpdb.utils.nmr.CifToNmrStar import (CifToNmrStar,
                                              has_key_value,
                                              get_first_sf_tag,
                                              set_sf_tag)
    from wwpdb.utils.nmr.NmrVrptUtility import (write_as_pickle,
                                                to_np_array,
                                                distance,
                                                to_unit_vector,
                                                dihedral_angle)
    from wwpdb.utils.nmr.mr.PdbMrSplitter import concat_seq_id_ins_code_pattern
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (translateToStdResName,
                                                       translateToStdAtomName,
                                                       isIdenticalRestraint,
                                                       isAmbigAtomSelection,
                                                       getTypeOfDihedralRestraint,
                                                       isLikeHis,
                                                       getRestraintName,
                                                       incListIdCounter,
                                                       getSaveframe,
                                                       getLoop,
                                                       getRowForStrMr,
                                                       assignCoordPolymerSequenceWithChainId,
                                                       selectCoordAtoms,
                                                       getPotentialType,
                                                       ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS,
                                                       ALLOWED_AMBIGUITY_CODES,
                                                       CS_UNCERTAINTY_RANGE,
                                                       DIST_UNCERTAINTY_RANGE,
                                                       ANGLE_UNCERTAINTY_RANGE,
                                                       RDC_UNCERTAINTY_RANGE,
                                                       REPRESENTATIVE_ASYM_ID,
                                                       NMR_STAR_LP_KEY_ITEMS,
                                                       NMR_STAR_LP_DATA_ITEMS,
                                                       NMR_STAR_LP_DATA_ITEMS_INS_CODE,
                                                       THRESHOLD_FOR_CIRCULAR_SHIFT,
                                                       PLANE_LIKE_LOWER_LIMIT,
                                                       PLANE_LIKE_UPPER_LIMIT)
except ImportError:
    from nmr.NmrDpConstant import (SF_CATEGORIES,
                                   LP_CATEGORIES,
                                   CUTOFF_AROMATIC,
                                   CUTOFF_PARAMAGNETIC,
                                   VICINITY_AROMATIC,
                                   VICINITY_PARAMAGNETIC,
                                   CUTOFF_BOND_LENGTH,
                                   MAGIC_ANGLE,
                                   INCONSIST_OVER_CONFLICTED,
                                   R_CONFLICTED_DIST_RESTRAINT,
                                   R_INCONSISTENT_DIST_RESTRAINT,
                                   INDEX_TAGS,
                                   CONSIST_ID_TAGS,
                                   PK_KEY_ITEMS,
                                   DATA_ITEMS,
                                   CONSIST_DATA_ITEMS,
                                   NUM_DIM_ITEMS,
                                   ALLOWED_TAGS,
                                   DISALLOWED_PK_TAGS,
                                   SF_ALLOWED_TAGS,
                                   AUX_LP_CATEGORIES,
                                   LINKED_LP_CATEGORIES,
                                   AUX_ALLOWED_TAGS,
                                   ITEM_NAMES_IN_CS_LOOP,
                                   ITEM_NAMES_IN_PK_LOOP,
                                   ITEM_NAMES_IN_DIST_LOOP,
                                   ITEM_NAMES_IN_DIHED_LOOP,
                                   ITEM_NAMES_IN_RDC_LOOP)
    from nmr.nef.NEFTranslator import (NEFTranslator,
                                       PARAMAGNETIC_ELEMENTS,
                                       FERROMAGNETIC_ELEMENTS,
                                       MAX_DIM_NUM_OF_SPECTRA)
    from nmr.NmrDpReport import NmrDpReport
    from nmr.AlignUtil import (LOW_SEQ_COVERAGE,
                               LARGE_ASYM_ID,
                               emptyValue,
                               monDict3,
                               protonBeginCode,
                               pseProBeginCode,
                               aminoProtonCode,
                               rdcBbPairCode,
                               letterToDigit,
                               alignPolymerSequence,
                               assignPolymerSequence)
    from nmr.io.CifReader import (CifReader,
                                  LEN_MAJOR_ASYM_ID)
    from nmr.CifToNmrStar import (CifToNmrStar,
                                  has_key_value,
                                  get_first_sf_tag,
                                  set_sf_tag)
    from nmr.NmrVrptUtility import (write_as_pickle,
                                    to_np_array,
                                    distance,
                                    to_unit_vector,
                                    dihedral_angle)
    from nmr.mr.PdbMrSplitter import concat_seq_id_ins_code_pattern
    from nmr.mr.ParserListenerUtil import (translateToStdResName,
                                           translateToStdAtomName,
                                           isIdenticalRestraint,
                                           isAmbigAtomSelection,
                                           getTypeOfDihedralRestraint,
                                           isLikeHis,
                                           getRestraintName,
                                           incListIdCounter,
                                           getSaveframe,
                                           getLoop,
                                           getRowForStrMr,
                                           assignCoordPolymerSequenceWithChainId,
                                           selectCoordAtoms,
                                           getPotentialType,
                                           ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS,
                                           ALLOWED_AMBIGUITY_CODES,
                                           CS_UNCERTAINTY_RANGE,
                                           DIST_UNCERTAINTY_RANGE,
                                           ANGLE_UNCERTAINTY_RANGE,
                                           RDC_UNCERTAINTY_RANGE,
                                           REPRESENTATIVE_ASYM_ID,
                                           NMR_STAR_LP_KEY_ITEMS,
                                           NMR_STAR_LP_DATA_ITEMS,
                                           NMR_STAR_LP_DATA_ITEMS_INS_CODE,
                                           THRESHOLD_FOR_CIRCULAR_SHIFT,
                                           PLANE_LIKE_LOWER_LIMIT,
                                           PLANE_LIKE_UPPER_LIMIT)


CS_UNCERT_MAX = CS_UNCERTAINTY_RANGE['max_inclusive']

DIST_UNCERT_MAX = DIST_UNCERTAINTY_RANGE['max_inclusive']

ANGLE_UNCERT_MAX = ANGLE_UNCERTAINTY_RANGE['max_inclusive']

RDC_UNCERT_MAX = RDC_UNCERTAINTY_RANGE['max_inclusive']


def is_like_planality_boundary(row: dict, lower_limit_name: str, upper_limit_name: str) -> bool:
    """ Return whether boundary conditions like planality restraint.
    """

    try:

        upper_limit = float(row[upper_limit_name])
        lower_limit = float(row[lower_limit_name])

        _array = numpy.array([upper_limit, lower_limit], dtype=float)

        shift = None
        if numpy.nanmin(_array) >= THRESHOLD_FOR_CIRCULAR_SHIFT:
            shift = -(numpy.nanmax(_array) // 360) * 360
        elif numpy.nanmax(_array) <= -THRESHOLD_FOR_CIRCULAR_SHIFT:
            shift = -(numpy.nanmin(_array) // 360) * 360
        if shift is not None:
            upper_limit += shift
            lower_limit += shift

        return PLANE_LIKE_LOWER_LIMIT <= lower_limit < 0.0 < upper_limit <= PLANE_LIKE_UPPER_LIMIT\
            or PLANE_LIKE_LOWER_LIMIT <= lower_limit - 180.0 < 0.0 < upper_limit - 180.0 <= PLANE_LIKE_UPPER_LIMIT\
            or PLANE_LIKE_LOWER_LIMIT <= lower_limit - 360.0 < 0.0 < upper_limit - 360.0 <= PLANE_LIKE_UPPER_LIMIT

    except (ValueError, TypeError):
        return False


class NmrDpValidation:
    """ Wrapper class for NMR data validation.
    """
    __slots__ = ('__class_name__',
                 '__version__',
                 '__verbose',
                 '__lfh',
                 '__op',
                 '__remediation_mode',
                 '__combined_mode',
                 '__native_combined',
                 '__annotation_mode',
                 '__internal_mode',
                 '__bmrb_only',
                 '__nonblk_anomalous_cs',
                 '__nonblk_bad_nterm',
                 '__resolve_conflict',
                 '__conversion_server',
                 '__transl_pseudo_name',
                 '__excl_missing_data',
                 '__entry_id',
                 '__leave_intl_note',
                 '__reduced_atom_notation',
                 '__cifChecked',
                 '__coordPropCachePath',
                 'report',
                 '__file_path_list_len',
                 'cs_anomalous_error_scaled_by_sigma',
                 'cs_unusual_error_scaled_by_sigma',
                 'key_items',
                 'consist_key_items',
                 'pk_data_items',
                 'aux_key_items',
                 'aux_data_items',
                 '__exptl_method',
                 '__representative_model_id',
                 '__representative_alt_id',
                 '__eff_model_ids',
                 '__coord_atom_site_tags',
                 '__lp_data',
                 '__aux_data',
                 '__star_data_type',
                 '__star_data',
                 '__sf_category_list',
                 '__list_id_counter',
                 '__mr_sf_dict_holder',
                 '__cca_dat',
                 '__mr_atom_name_mapping',
                 '__symmetric',
                 '__is_cyclic_polymer',
                 '__cR',
                 '__caC',
                 '__cpC',
                 '__cpC_hash',
                 '__pA',
                 '__ccU',
                 '__csStat',
                 '__c2S',
                 '__nefT')

    def __init__(self, verbose: bool, log: IO,
                 op: str, remediationMode: bool, combinedMode: bool, nativeCombined: bool, annotationMode: bool, internalMode: bool,
                 bmrbOnly: bool, nonblkAnomalousCs: bool, nonblkBadNterm: bool, resolveConflict: bool, conversionServer: bool,
                 translPseudoName: bool, exclMissingData: bool,
                 entryId: str, leaveIntlNote: bool, reducedAtomNotation: bool, cifChecked: bool, coordPropCachePath: str,
                 report: NmrDpReport, filePathListLen: int, csAnomalousErrorScaledBySigma: float, csUnusualErrorScaledBySigma: float,
                 keyItems: dict, consistKeyItems: dict, pkDataItems: dict, auxKeyItems: dict, auxDataItems: dict,
                 expylMethod: str, representativeModelId: int, represetativeAltId: str, effModelIds: List[int],
                 coordAtomSiteTags: List[str], lpData: dict, auxData: dict,
                 cR: Optional[CifReader] = None, caC: Optional[dict] = None, cpC: dict = None, cpCHash: str = None,
                 c2S: Optional[CifToNmrStar] = None, nefT: Optional[NEFTranslator] = None):
        self.__class_name__ = self.__class__.__name__
        self.__version__ = __version__

        self.__verbose = verbose
        self.__lfh = log

        # current workflow operation
        self.__op = op

        # whether to enable remediation routines
        self.__remediation_mode = remediationMode
        # whether NMR combined deposition or not (NMR conventional deposition)
        self.__combined_mode = combinedMode
        # whether native NMR combined deposition
        self.__native_combined = nativeCombined
        # whether to allow sequence mismatch during annotation
        self.__annotation_mode = annotationMode
        # whether to allow to raise internal error
        self.__internal_mode = internalMode

        # whether to allow empty coordinate file path
        self.__bmrb_only = bmrbOnly
        # whether not to block deposition because of anomalous cs
        self.__nonblk_anomalous_cs = nonblkAnomalousCs
        # whether not to block deposition because bad n-term amino group
        self.__nonblk_bad_nterm = nonblkBadNterm
        # whether to resolve conflict
        self.__resolve_conflict = resolveConflict
        # whether to skip missing_mandatory_content error for data conversion server (DAOTHER-9785)
        self.__conversion_server = conversionServer
        # whether to translate conventional pseudo atom nomenclature in combined NMR-STAR file
        self.__transl_pseudo_name = translPseudoName

        # whether to exclude missing mandatory data (enabled if NMR conventional deposition)
        self.__excl_missing_data = exclMissingData

        # current entry_id, to be replaced
        self.__entry_id = entryId

        # whether to leave internal commentary note in processed NMR-STAR file
        self.__leave_intl_note = leaveIntlNote
        # whether to use reduced atom notation in warning/error message
        self.__reduced_atom_notation = reducedAtomNotation

        # whether coordinate file is already examined
        self.__cifChecked = cifChecked

        # cache path of coordinate properties
        self.__coordPropCachePath = coordPropCachePath

        # data processing report
        self.report = report

        # PyNMRSTAR data
        self.__file_path_list_len = filePathListLen

        # criterion on chemical shift for anomalous value scaled by its sigma
        self.cs_anomalous_error_scaled_by_sigma = csAnomalousErrorScaledBySigma
        # criterion on chemical shift for unusual value scaled by its sigma
        self.cs_unusual_error_scaled_by_sigma = csUnusualErrorScaledBySigma

        # key items of loop
        self.key_items = keyItems
        # key items of loop to check consistency
        self.consist_key_items = consistKeyItems
        # loop data items for spectral peak
        self.pk_data_items = pkDataItems
        # auxiliary loop key items
        self.aux_key_items = auxKeyItems
        # auxiliary loop data items
        self.aux_data_items = auxDataItems

        # experimental method
        self.__exptl_method = expylMethod

        # representative model id
        self.__representative_model_id = representativeModelId
        # representative_alt_id
        self.__representative_alt_id = represetativeAltId
        # list of effective model_id
        self.__eff_model_ids = effModelIds
        # item tag names of 'atom_site' category of the coordinates
        self.__coord_atom_site_tags = coordAtomSiteTags

        self.__lp_data = lpData
        self.__aux_data = auxData

        # list of pynmrstar data types
        self.__star_data_type = None

        # list of pynmrstar data
        self.__star_data = None

        # list of saveframe categories
        self.__sf_category_list = None

        # validateStrMr() specific
        self.__list_id_counter = None
        self.__mr_sf_dict_holder = None

        # validateStrMr() and validateStrPk() specific
        self.__cca_dat = None

        # validateCsValue() specific
        self.__mr_atom_name_mapping = None

        # whether solid-state NMR is applied to symmetric samples such as fibrils
        self.__symmetric = None

        # whether nmr chain is cyclic polymer or not
        self.__is_cyclic_polymer = {}

        # NmrDpReport
        self.report = report

        # CifReader
        self.__cR = cR

        # ParserListerUtil.coordAssemblyChecker()
        self.__caC = caC

        # coordinate properties cache
        self.__cpC = cpC

        # hash value of coordinate properties cache
        self.__cpC_hash = cpCHash

        # CifToNmrStar
        self.__c2S = CifToNmrStar(log) if c2S is None else c2S

        # NEFTranslator
        self.__nefT = nefT

        self.__ccU = nefT.ccU
        self.__csStat = nefT.csStat
        self.__pA = nefT.pA

    @property
    def star_data_type(self):
        return self.__star_data_type

    @star_data_type.setter
    def star_data_type(self, star_data_type: List[str]):
        if star_data_type == self.__star_data_type:
            return
        self.__star_data_type = star_data_type

    @property
    def star_data(self):
        return self.__star_data

    @star_data.setter
    def star_data(self, star_data: List[Union[pynmrstar.Entry, pynmrstar.Saveframe, pynmrstar.Loop]]):
        if star_data == self.__star_data:
            return
        self.__star_data = star_data

    @property
    def sf_category_list(self):
        return self.__sf_category_list

    @sf_category_list.setter
    def sf_category_list(self, sf_category_list: List[str]):
        if sf_category_list == self.__sf_category_list:
            return
        self.__sf_category_list = sf_category_list

    @property
    def list_id_counter(self):
        return self.__list_id_counter

    @list_id_counter.setter
    def list_id_counter(self, list_id_counter: dict):
        if list_id_counter == self.__list_id_counter:
            return
        self.__list_id_counter = list_id_counter

    @property
    def mr_sf_dict_holder(self):
        return self.__mr_sf_dict_holder

    @mr_sf_dict_holder.setter
    def mr_sf_dict_holder(self, mr_sf_dict_holder: dict):
        if mr_sf_dict_holder == self.__mr_sf_dict_holder:
            return
        self.__mr_sf_dict_holder = mr_sf_dict_holder

    @property
    def cca_dat(self):
        return self.__cca_dat

    @cca_dat.setter
    def cca_dat(self, cca_dat: list):
        if cca_dat == self.__cca_dat:
            return
        self.__cca_dat = cca_dat

    @property
    def mr_atom_name_mapping(self):
        return self.__mr_atom_name_mapping

    @mr_atom_name_mapping.setter
    def mr_atom_name_mapping(self, mr_atom_name_mapping: Optional[List[dict]]):
        if mr_atom_name_mapping == self.__mr_atom_name_mapping:
            return
        self.__mr_atom_name_mapping = mr_atom_name_mapping

    def getChemCompNameAndStatusOf(self, comp_id: str) -> Tuple[bool, Optional[str], Optional[str]]:
        """ Return _chem_comp.name and release status a given CCD ID, if possible.
        """

        cc_name = cc_rel_status = processing_site = None

        if len(self.__star_data_type) > 0 and self.__star_data_type[0] == 'Entry' and 'chem_comp' in self.__sf_category_list:
            chem_comp_sf = next((sf for sf in self.__star_data[0].frame_list if sf.name == f'chem_comp_{comp_id}'), None)

            if chem_comp_sf is not None:
                cc_name = get_first_sf_tag(chem_comp_sf, 'Name')
                if cc_name in emptyValue:
                    cc_name = None
                processing_site = get_first_sf_tag(chem_comp_sf, 'Processing_site')
                if processing_site in emptyValue:
                    processing_site = None

        if self.__ccU.updateChemCompDict(comp_id):  # matches with comp_id in CCD
            is_valid = True

            if cc_name is None:
                cc_name = self.__ccU.lastChemCompDict['_chem_comp.name']

            if processing_site is not None and processing_site.startswith('BMRB'):
                is_valid = False
                cc_name += f', processing site {processing_site}'
            else:
                cc_rel_status = self.__ccU.lastChemCompDict['_chem_comp.pdbx_release_status']

        else:
            is_valid = False

        return is_valid, cc_name, cc_rel_status

    def isNmrAtomName(self, comp_id: str, atom_id: str) -> bool:
        """ Return whether a given atom_id uses NMR conventional atom name.
        """

        return ((atom_id in ('HN', 'CO') and self.__csStat.peptideLike(comp_id))
                or atom_id.startswith('Q') or atom_id.startswith('M')
                or atom_id.endswith('%') or atom_id.endswith('#')
                or self.__csStat.getMaxAmbigCodeWoSetId(comp_id, atom_id) == 0)

    def getAtomIdListInXplor(self, comp_id: str, atom_id: str) -> List[str]:
        """ Return atom ID list in IUPAC atom nomenclature for a given atom_id in XPLOR atom nomenclature.
        """

        atom_list, _, details = self.__nefT.get_valid_star_atom_in_xplor(comp_id, atom_id)

        return atom_list if details is None else []

    def getAtomIdListInXplorForLigandRemap(self, comp_id: str, atom_id: str, coord_atom_site: dict) -> List[str]:
        """ Return atom ID list in IUPAC atom nomenclature for a given atom_id in XPLOR atom nomenclature
            in reference to coordinates' alternative atom IDs. (DAOTHER-9286)
        """

        return self.__nefT.get_valid_star_atom_in_xplor_for_ligand_remap(comp_id, atom_id, coord_atom_site)[0]

    def getRepAtomId(self, comp_id: str, atom_id: str) -> str:
        """ Return a representative atom ID in IUPAC atom nomenclature for a given atom_id.
        """

        _atom_id = self.__nefT.get_valid_star_atom(comp_id, atom_id, leave_unmatched=False)[0]

        return atom_id if len(_atom_id) == 0 else _atom_id[0]

    def getAtomIdList(self, comp_id: str, atom_id: str) -> List[str]:
        """ Return atom ID list in IUPAC atom nomenclature for a given atom_id.
        """

        return self.__nefT.get_valid_star_atom(comp_id, atom_id, leave_unmatched=False)[0]

    def __getAtomIdListWithAmbigCode(self, comp_id: str, atom_id: str, leave_unmatched: bool = True
                                     ) -> Tuple[List[str], Optional[int], Optional[str]]:
        """ Return lists of atom ID, ambiguity_code, details in IUPAC atom nomenclature for a given conventional NMR atom name.
            @see: NEFTranslator.get_valid_star_atom()
        """

        return self.__nefT.get_valid_star_atom(comp_id, atom_id, leave_unmatched=leave_unmatched)

    def getReducedAtomNotation(self, chain_id_name: str, chain_id: str, seq_id_name: str, seq_id: int,
                               comp_id_name: str, comp_id: str, atom_id_name: str, atom_id: str) -> str:
        """ Return reduced form of atom notation.
        """

        if self.__reduced_atom_notation:
            return f"{chain_id}:{seq_id}:{comp_id}:{atom_id}"

        return f"{chain_id_name} {chain_id}, {seq_id_name} {seq_id}, {comp_id_name} {comp_id}, {atom_id_name} {atom_id}"

    def __getReducedAtomNotations(self, key_items: List[dict], row_data: dict) -> str:
        """ Return reduced from of series of atom notations.
        """

        msg = ''

        if self.__reduced_atom_notation:
            j = 0
            for k in key_items:
                msg += f"{row_data[k['name']]}:"
                j += 1
                if j % 4 == 0:
                    msg = msg[:-1] + ' - '
            return msg[:-3]

        for k in key_items:
            msg += k['name'] + f" {row_data[k['name']]}, "

        return msg[:-2]

    def getTypeOfDihedralRestraint(self, data_type: str, peptide: bool, nucleotide: bool, carbohydrate: bool,  # pylint: disable=no-self-use
                                   atoms: List[dict], plane_like: bool) -> str:
        """ Return type of dihedral angle restraint.
        """

        if data_type in emptyValue:
            data_type = getTypeOfDihedralRestraint(peptide, nucleotide, carbohydrate,
                                                   atoms, plane_like)

            if data_type in emptyValue or data_type.startswith('pseudo'):
                data_type = 'undefined'
            else:
                data_type = data_type.lower()

        else:
            data_type = data_type.lower()

        if not data_type.endswith('_angle_constraints'):
            data_type += '_angle_constraints'

        return data_type

    def isCyclicPolymer(self, nmr_chain_id: str) -> bool:
        """ Return whether a given chain is cyclic polymer based on coordinate annotation.
            @return: True for cyclic polymer, False otherwise
        """

        if nmr_chain_id in self.__is_cyclic_polymer:
            return self.__is_cyclic_polymer[nmr_chain_id]

        try:

            is_cyclic = self.__isCyclicPolymer__(nmr_chain_id)

            return is_cyclic

        finally:
            self.__is_cyclic_polymer[nmr_chain_id] = is_cyclic

    def __isCyclicPolymer__(self, nmr_chain_id: str) -> bool:
        """ Return whether a given chain is cyclic polymer based on coordinate annotation.
            @return: True for cyclic polymer, False otherwise
        """

        cif_ps = self.report.getModelPolymerSequenceWithNmrChainId(nmr_chain_id)

        if cif_ps is None:
            return False

        cif_chain_id = cif_ps['chain_id']
        beg_cif_seq_id = cif_ps['seq_id'][0]
        end_cif_seq_id = cif_ps['seq_id'][-1]

        try:

            if self.__cR.hasCategory('struct_conn'):
                filter_items = [{'name': 'ptnr1_label_asym_id', 'type': 'str', 'value': cif_chain_id},
                                {'name': 'ptnr2_label_asym_id', 'type': 'str', 'value': cif_chain_id},
                                {'name': 'ptnr1_label_seq_id', 'type': 'int', 'value': beg_cif_seq_id},
                                {'name': 'ptnr2_label_seq_id', 'type': 'int', 'value': end_cif_seq_id}
                                ]

                if not self.__bmrb_only and self.__cR.hasItem('struct_conn', 'pdbx_leaving_atom_flag'):
                    filter_items.append({'name': 'pdbx_leaving_atom_flag', 'type': 'str', 'value': 'both'})

                struct_conn = self.__cR.getDictListWithFilter('struct_conn',
                                                              [{'name': 'conn_type_id', 'type': 'str'}
                                                               ],
                                                              filter_items)

            else:
                struct_conn = []

        except Exception as e:

            self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.__isCyclicPolymer__() ++ Error  - " + str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write(f"+{self.__class_name__}.__isCyclicPolymer__() ++ Error  - {str(e)}\n")

            return False

        if len(struct_conn) == 0:

            label_to_auth_seq = self.__caC['label_to_auth_seq']

            seq_key_1 = (cif_chain_id, beg_cif_seq_id)
            seq_key_2 = (cif_chain_id, end_cif_seq_id)
            close_contact = []

            if seq_key_1 in label_to_auth_seq and seq_key_2 in label_to_auth_seq:
                auth_cif_chain_id, auth_beg_cif_seq_id = label_to_auth_seq[seq_key_1]
                _, auth_end_cif_seq_id = label_to_auth_seq[seq_key_2]

                try:

                    if self.__cR.hasCategory('pdbx_validate_close_contact'):
                        close_contact = self.__cR.getDictListWithFilter('pdbx_validate_close_contact',
                                                                        [{'name': 'dist', 'type': 'float'}
                                                                         ],
                                                                        [{'name': 'PDB_model_num', 'type': 'int', 'value': self.__representative_model_id},
                                                                         {'name': 'auth_asym_id_1', 'type': 'str', 'value': auth_cif_chain_id},
                                                                         {'name': 'auth_seq_id_1', 'type': 'int', 'value': auth_beg_cif_seq_id},
                                                                         {'name': 'auth_atom_id_1', 'type': 'str', 'value': 'N'},
                                                                         {'name': 'auth_asym_id_2', 'type': 'str', 'value': auth_cif_chain_id},
                                                                         {'name': 'auth_seq_id_2', 'type': 'int', 'value': auth_end_cif_seq_id},
                                                                         {'name': 'auth_atom_id_2', 'type': 'str', 'value': 'C'}
                                                                         ])

                except Exception as e:

                    self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.__isCyclicPolymer__() ++ Error  - " + str(e))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write(f"+{self.__class_name__}.__isCyclicPolymer__() ++ Error  - {str(e)}\n")

                    return False

            if len(close_contact) == 0:

                bond = self.getCoordBondLength(cif_chain_id, beg_cif_seq_id, 'N', cif_chain_id, end_cif_seq_id, 'C')

                if bond is None:
                    return False

                dist = next((b['distance'] for b in bond if b['model_id'] == self.__representative_model_id), None)

                if dist is None:
                    return False

                return 1.0 < dist < 2.4

            return 1.0 < close_contact[0]['dist'] < 2.4

        return struct_conn[0]['conn_type_id'].startswith('covale')

    def isProtCis(self, nmr_chain_id: str, nmr_seq_id: int) -> bool:
        """ Return whether type of peptide conformer of a given sequence is cis based on coordinate annotation.
            @return: True for cis peptide conformer, False otherwise
        """

        cif_ps = self.report.getModelPolymerSequenceWithNmrChainId(nmr_chain_id)

        if cif_ps is None:
            return False

        cif_chain_id = cif_ps['chain_id']

        seq_align_dic = self.report.sequence_alignment.get()

        if not has_key_value(seq_align_dic, 'nmr_poly_seq_vs_model_poly_seq'):
            return False

        result = next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq']
                       if seq_align['ref_chain_id'] == nmr_chain_id and seq_align['test_chain_id'] == cif_chain_id), None)

        if result is not None:

            cif_seq_id = next((test_seq_id for ref_seq_id, test_seq_id
                               in zip(result['ref_seq_id'], result['test_seq_id'])
                               if ref_seq_id == nmr_seq_id), None)

            if cif_seq_id is None:
                return False

            try:

                if self.__cR.hasCategory('struct_mon_prot_cis'):
                    alias = not self.__cR.hasItem('struct_mon_prot_cis', 'pdbx_PDB_model_num')

                    model_num_name = 'ndb_model_num' if alias else 'pdbx_PDB_model_num'
                    label_asym_id_2_name = 'ndb_label_asym_id_2' if alias else 'pdbx_label_asym_id_2'
                    label_seq_id_2_name = 'ndb_label_seq_id_2' if alias else 'pdbx_label_seq_id_2'

                    prot_cis = self.__cR.getDictListWithFilter('struct_mon_prot_cis',
                                                               [{'name': model_num_name, 'type': 'int'}
                                                                ],
                                                               [{'name': label_asym_id_2_name, 'type': 'str', 'value': cif_chain_id},
                                                                {'name': label_seq_id_2_name, 'type': 'int', 'value': cif_seq_id}
                                                                ])

                else:
                    prot_cis = []

            except Exception as e:

                self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.isProtCis() ++ Error  - " + str(e))
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write(f"+{self.__class_name__}.isProtCis() ++ Error  - {str(e)}\n")

                return False

            return len(prot_cis) > 0

        return False

    def getNmrBondLength(self, nmr_chain_id_1: str, nmr_seq_id_1: int, nmr_atom_id_1: str,
                         nmr_chain_id_2: str, nmr_seq_id_2: int, nmr_atom_id_2: str) -> Optional[List[dict]]:
        """ Return the bond length of given two NMR atoms.
            @return: the bond length
        """

        intra_chain = nmr_chain_id_1 == nmr_chain_id_2

        s_1 = self.report.getModelPolymerSequenceWithNmrChainId(nmr_chain_id_1)

        if s_1 is None:
            return None

        s_2 = s_1 if intra_chain else self.report.getModelPolymerSequenceWithNmrChainId(nmr_chain_id_2)

        if s_2 is None:
            return None

        cif_chain_id_1 = s_1['chain_id']
        cif_chain_id_2 = cif_chain_id_1 if intra_chain else s_2['chain_id']

        seq_align_dic = self.report.sequence_alignment.get()

        if not has_key_value(seq_align_dic, 'nmr_poly_seq_vs_model_poly_seq'):
            return None

        seq_key = (nmr_chain_id_1, nmr_seq_id_1, nmr_atom_id_1, nmr_chain_id_2, nmr_seq_id_2, nmr_atom_id_2)

        if seq_key in self.__cpC['bond_length']:
            return self.__cpC['bond_length'][seq_key]

        result_1 = next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq']
                         if seq_align['ref_chain_id'] == nmr_chain_id_1 and seq_align['test_chain_id'] == cif_chain_id_1), None)
        result_2 = result_1 if intra_chain else next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq']
                                                      if seq_align['ref_chain_id'] == nmr_chain_id_2 and seq_align['test_chain_id'] == cif_chain_id_2), None)

        if None not in (result_1, result_2):

            cif_seq_id_1 = next((test_seq_id for ref_seq_id, test_seq_id
                                 in zip(result_1['ref_seq_id'], result_1['test_seq_id']) if ref_seq_id == nmr_seq_id_1), None)

            if cif_seq_id_1 is None:
                self.__cpC['bond_length'][seq_key] = None
                return None

            cif_seq_id_2 = next((test_seq_id for ref_seq_id, test_seq_id
                                 in zip(result_2['ref_seq_id'], result_2['test_seq_id']) if ref_seq_id == nmr_seq_id_2), None)

            if cif_seq_id_2 is None:
                self.__cpC['bond_length'][seq_key] = None
                return None

            bond = self.getCoordBondLength(cif_chain_id_1, cif_seq_id_1, nmr_atom_id_1, cif_chain_id_2, cif_seq_id_2, nmr_atom_id_2)

            if bond is not None:
                self.__cpC['bond_length'][seq_key] = bond

                return bond

        self.__cpC['bond_length'][seq_key] = None

        return None

    def getCoordBondLength(self, cif_chain_id_1: str, cif_seq_id_1: int, cif_atom_id_1: str,
                           cif_chain_id_2: str, cif_seq_id_2: int, cif_atom_id_2: str,
                           label_scheme: bool = True) -> Optional[List[dict]]:
        """ Return the bond length of given two CIF atoms.
            @return: the bond length
        """

        try:

            model_num_name = 'pdbx_PDB_model_num' if 'pdbx_PDB_model_num' in self.__coord_atom_site_tags else 'ndb_model'

            data_items = [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                          {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                          {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'},
                          {'name': model_num_name, 'type': 'int', 'alt_name': 'model_id'}
                          ]

            atom_site_1 = self.__cR.getDictListWithFilter('atom_site',
                                                          data_items,
                                                          [{'name': 'label_asym_id' if label_scheme else 'auth_asym_id', 'type': 'str', 'value': cif_chain_id_1},
                                                           {'name': 'label_seq_id' if label_scheme else 'auth_seq_id', 'type': 'int', 'value': cif_seq_id_1},
                                                           {'name': 'label_atom_id' if label_scheme else 'auth_atom_id', 'type': 'str', 'value': cif_atom_id_1},
                                                           {'name': 'label_alt_id', 'type': 'enum', 'enum': (self.__representative_alt_id,)}
                                                           ])

            atom_site_2 = self.__cR.getDictListWithFilter('atom_site',
                                                          data_items,
                                                          [{'name': 'label_asym_id' if label_scheme else 'auth_asym_id', 'type': 'str', 'value': cif_chain_id_2},
                                                           {'name': 'label_seq_id' if label_scheme else 'auth_seq_id', 'type': 'int', 'value': cif_seq_id_2},
                                                           {'name': 'label_atom_id' if label_scheme else 'auth_atom_id', 'type': 'str', 'value': cif_atom_id_2},
                                                           {'name': 'label_alt_id', 'type': 'enum', 'enum': (self.__representative_alt_id,)}
                                                           ])

        except Exception as e:

            self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.getCoordBondLength() ++ Error  - " + str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write(f"+{self.__class_name__}.getCoordBondLength() ++ Error  - {str(e)}\n")

            return None

        model_ids = set(a['model_id'] for a in atom_site_1) | set(a['model_id'] for a in atom_site_2)

        bond = []

        for model_id in model_ids:
            a_1 = next((a for a in atom_site_1 if a['model_id'] == model_id), None)
            a_2 = next((a for a in atom_site_2 if a['model_id'] == model_id), None)

            if None in (a_1, a_2):
                continue

            bond.append({'model_id': model_id, 'distance': float(f"{distance(to_np_array(a_1), to_np_array(a_2)):.3f}")})

        if len(bond) > 0:
            return bond

        return None

    def __getNearestAromaticRing(self, nmr_chain_id: str, nmr_seq_id: int, nmr_atom_id: str) -> Optional[dict]:
        """ Return the nearest aromatic ring around a given atom.
            @return: the nearest aromatic ring
        """

        cif_ps = self.report.getModelPolymerSequenceWithNmrChainId(nmr_chain_id)

        if cif_ps is None:
            return None

        cif_chain_id = cif_ps['chain_id']

        seq_align_dic = self.report.sequence_alignment.get()

        if not has_key_value(seq_align_dic, 'nmr_poly_seq_vs_model_poly_seq'):
            return None

        seq_key = (nmr_chain_id, nmr_seq_id, nmr_atom_id)

        if seq_key in self.__cpC['near_ring']:
            return self.__cpC['near_ring'][seq_key]

        result = next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq']
                       if seq_align['ref_chain_id'] == nmr_chain_id and seq_align['test_chain_id'] == cif_chain_id), None)

        if result is not None:

            cif_seq_id = next((test_seq_id for ref_seq_id, test_seq_id
                               in zip(result['ref_seq_id'], result['test_seq_id'])
                               if ref_seq_id == nmr_seq_id), None)

            if cif_seq_id is None:
                self.__cpC['near_ring'][seq_key] = None
                return None

            try:

                model_num_name = 'pdbx_PDB_model_num' if 'pdbx_PDB_model_num' in self.__coord_atom_site_tags else 'ndb_model'

                _origin = self.__cR.getDictListWithFilter('atom_site',
                                                          [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                           {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                           {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                                                           ],
                                                          [{'name': 'label_asym_id', 'type': 'str', 'value': cif_chain_id},
                                                           {'name': 'label_seq_id', 'type': 'int', 'value': cif_seq_id},
                                                           {'name': 'label_atom_id', 'type': 'str', 'value': nmr_atom_id},
                                                           {'name': model_num_name, 'type': 'int', 'value': self.__representative_model_id},
                                                           {'name': 'label_alt_id', 'type': 'enum', 'enum': (self.__representative_alt_id,)}
                                                           ])

            except Exception as e:

                self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.__getNearestAromaticRing() ++ Error  - " + str(e))
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write(f"+{self.__class_name__}.__getNearestAromaticRing() ++ Error  - {str(e)}\n")

                return None

            if len(_origin) != 1:
                self.__cpC['near_ring'][seq_key] = None
                return None

            o = to_np_array(_origin[0])

            try:

                _neighbor = self.__cR.getDictListWithFilter('atom_site',
                                                            [{'name': 'label_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                                             {'name': 'label_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                                             {'name': 'label_comp_id', 'type': 'starts-with-alnum', 'alt_name': 'comp_id'},
                                                             {'name': 'label_atom_id', 'type': 'starts-with-alnum', 'alt_name': 'atom_id'},
                                                             {'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                             {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                             {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'},
                                                             {'name': 'type_symbol', 'type': 'str'}
                                                             ],
                                                            [{'name': 'Cartn_x', 'type': 'range-float',
                                                              'range': {'min_exclusive': (o[0] - CUTOFF_AROMATIC),
                                                                        'max_exclusive': (o[0] + CUTOFF_AROMATIC)}},
                                                             {'name': 'Cartn_y', 'type': 'range-float',
                                                              'range': {'min_exclusive': (o[1] - CUTOFF_AROMATIC),
                                                                        'max_exclusive': (o[1] + CUTOFF_AROMATIC)}},
                                                             {'name': 'Cartn_z', 'type': 'range-float',
                                                              'range': {'min_exclusive': (o[2] - CUTOFF_AROMATIC),
                                                                        'max_exclusive': (o[2] + CUTOFF_AROMATIC)}},
                                                             {'name': model_num_name, 'type': 'int', 'value': self.__representative_model_id},
                                                             {'name': 'label_alt_id', 'type': 'enum', 'enum': (self.__representative_alt_id,)}
                                                             ])

            except Exception as e:

                self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.__getNearestAromaticRing() ++ Error  - " + str(e))
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write(f"+{self.__class_name__}.__getNearestAromaticRing() ++ Error  - {str(e)}\n")

                return None

            if len(_neighbor) == 0:
                self.__cpC['near_ring'][seq_key] = None
                return None

            neighbor = [n for n in _neighbor
                        if n['seq_id'] != cif_seq_id
                        and n['type_symbol'] not in protonBeginCode
                        and distance(to_np_array(n), o) < CUTOFF_AROMATIC
                        and n['atom_id'] in self.__csStat.getAromaticAtoms(n['comp_id'])]

            if len(neighbor) == 0:
                self.__cpC['near_ring'][seq_key] = None
                return None

            if not has_key_value(seq_align_dic, 'model_poly_seq_vs_nmr_poly_seq'):
                self.__cpC['near_ring'][seq_key] = None
                return None

            atom_list = []

            for n in neighbor:

                _cif_chain_id = n['chain_id']

                _ps = self.report.getNmrPolymerSequenceWithModelChainId(_cif_chain_id)

                if _ps is None:
                    continue

                _nmr_chain_id = _ps['chain_id']

                result = next((seq_align for seq_align in seq_align_dic['model_poly_seq_vs_nmr_poly_seq']
                               if seq_align['ref_chain_id'] == _cif_chain_id and seq_align['test_chain_id'] == _nmr_chain_id), None)

                if result is not None:

                    _nmr_seq_id = next((test_seq_id for ref_seq_id, test_seq_id
                                        in zip(result['ref_seq_id'], result['test_seq_id'])
                                        if ref_seq_id == n['seq_id']), None)

                    atom_list.append({'chain_id': _nmr_chain_id,
                                      'seq_id': _nmr_seq_id,
                                      'cif_chain_id': _cif_chain_id,
                                      'cif_seq_id': n['seq_id'],
                                      'comp_id': n['comp_id'],
                                      'atom_id': n['atom_id'],
                                      'distance': distance(to_np_array(n), o)})

            if len(atom_list) == 0:
                return None

            na = sorted(atom_list, key=itemgetter('distance'))[0]

            na_atom_id = na['atom_id']

            if not self.__ccU.updateChemCompDict(na['comp_id']):
                self.__cpC['near_ring'][seq_key] = None
                return None

            # matches with comp_id in CCD

            half_ring_traces = []

            for b1 in self.__ccU.lastBonds:

                if b1[self.__ccU.ccbAromaticFlag] != 'Y':
                    continue

                if b1[self.__ccU.ccbAtomId1] == na_atom_id and b1[self.__ccU.ccbAtomId2][0] not in protonBeginCode:
                    na_ = b1[self.__ccU.ccbAtomId2]

                elif b1[self.__ccU.ccbAtomId2] == na_atom_id and b1[self.__ccU.ccbAtomId1][0] not in protonBeginCode:
                    na_ = b1[self.__ccU.ccbAtomId1]

                else:
                    continue

                for b2 in self.__ccU.lastBonds:

                    if b2[self.__ccU.ccbAromaticFlag] != 'Y':
                        continue

                    if b2[self.__ccU.ccbAtomId1] == na_ and b2[self.__ccU.ccbAtomId2][0] not in protonBeginCode and b2[self.__ccU.ccbAtomId2] != na_atom_id:
                        na__ = b2[self.__ccU.ccbAtomId2]

                    elif b2[self.__ccU.ccbAtomId2] == na_ and b2[self.__ccU.ccbAtomId1][0] not in protonBeginCode and b2[self.__ccU.ccbAtomId1] != na_atom_id:
                        na__ = b2[self.__ccU.ccbAtomId1]

                    else:
                        continue

                    for b3 in self.__ccU.lastBonds:

                        if b3[self.__ccU.ccbAromaticFlag] != 'Y':
                            continue

                        if b3[self.__ccU.ccbAtomId1] == na__ and b3[self.__ccU.ccbAtomId2][0] not in protonBeginCode and b3[self.__ccU.ccbAtomId2] != na_:
                            na___ = b3[self.__ccU.ccbAtomId2]

                        elif b3[self.__ccU.ccbAtomId2] == na__ and b3[self.__ccU.ccbAtomId1][0] not in protonBeginCode and b3[self.__ccU.ccbAtomId1] != na_:
                            na___ = b3[self.__ccU.ccbAtomId1]

                        else:
                            continue

                        half_ring_traces.append(na_atom_id + ':' + na_ + ':' + na__ + ':' + na___)

            len_half_ring_traces = len(half_ring_traces)

            if len_half_ring_traces < 2:
                self.__cpC['near_ring'][seq_key] = None
                return None

            ring_traces = []

            for i in range(len_half_ring_traces - 1):

                half_ring_trace_1 = half_ring_traces[i].split(':')

                for j in range(i + 1, len_half_ring_traces):

                    half_ring_trace_2 = half_ring_traces[j].split(':')

                    # hexagonal ring
                    if half_ring_trace_1[3] == half_ring_trace_2[3]:
                        ring_traces.append(half_ring_traces[i] + ':' + half_ring_trace_2[2] + ':' + half_ring_trace_2[1])

                    # pentagonal ring
                    elif half_ring_trace_1[3] == half_ring_trace_2[2] and half_ring_trace_1[2] == half_ring_trace_2[3]:
                        ring_traces.append(half_ring_traces[i] + ':' + half_ring_trace_2[1])

            if len(ring_traces) == 0:
                self.__cpC['near_ring'][seq_key] = None
                return None

            ring_atoms = None
            ring_trace_score = 0

            for ring_trace in ring_traces:

                _ring_atoms = ring_trace.split(':')

                score = 0

                for a in atom_list:

                    if a['chain_id'] != na['chain_id'] or a['seq_id'] != na['seq_id'] or a['comp_id'] != na['comp_id']:
                        continue

                    if a['atom_id'] in _ring_atoms:
                        score += 1

                if score > ring_trace_score:
                    ring_atoms = _ring_atoms
                    ring_trace_score = score

            try:

                _na = self.__cR.getDictListWithFilter('atom_site',
                                                      [{'name': 'label_atom_id', 'type': 'starts-with-alnum', 'alt_name': 'atom_id'},
                                                       {'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                       {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                       {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'},
                                                       {'name': model_num_name, 'type': 'int', 'alt_name': 'model_id'}
                                                       ],
                                                      [{'name': 'label_asym_id', 'type': 'str', 'value': na['cif_chain_id']},
                                                       {'name': 'label_seq_id', 'type': 'int', 'value': na['cif_seq_id']},
                                                       {'name': 'label_comp_id', 'type': 'str', 'value': na['comp_id']},
                                                       {'name': 'label_atom_id', 'type': 'enum', 'enum': ring_atoms},
                                                       {'name': 'label_alt_id', 'type': 'enum', 'enum': (self.__representative_alt_id,)}
                                                       ])

            except Exception as e:

                self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.__getNearestAromaticRing() ++ Error  - " + str(e))
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write(f"+{self.__class_name__}.__getNearestAromaticRing() ++ Error  - {str(e)}\n")

                return None

            if len(_na) == 0:
                self.__cpC['near_ring'][seq_key] = None
                return None

            model_ids = set(a['model_id'] for a in _na)

            len_model_ids = 0

            dist = ring_dist = ring_angle = 0.0

            for model_id in model_ids:

                rc = numpy.array([0.0] * 3)

                total = 0

                for a in _na:

                    if a['model_id'] == model_id:

                        _a = to_np_array(a)

                        if a['atom_id'] == na_atom_id:
                            dist += distance(_a, o)

                        rc = numpy.add(rc, _a)

                        total += 1

                if total == len(ring_atoms):

                    rc = rc / total

                    ring_dist += distance(rc, o)

                    na_ = next(to_np_array(na_) for na_ in _na if na_['atom_id'] == ring_atoms[0])
                    na__ = next(to_np_array(na__) for na__ in _na if na__['atom_id'] == ring_atoms[1])
                    na___ = next(to_np_array(na___) for na___ in _na if na___['atom_id'] == ring_atoms[-1])

                    ring_vector = numpy.cross(na__ - na_, na___ - na_)

                    ring_angle += math.acos(abs(numpy.dot(to_unit_vector(o - rc), to_unit_vector(ring_vector))))

                    len_model_ids += 1

            if len_model_ids == 0:  # DAOTHER-8840
                return None

            na['ring_atoms'] = ring_atoms
            na['distance'] = float(f"{dist / len_model_ids:.1f}")
            na['ring_distance'] = float(f"{ring_dist / len_model_ids:.1f}")
            na['ring_angle'] = float(f"{numpy.degrees(ring_angle / len_model_ids):.1f}")

            self.__cpC['near_ring'][seq_key] = na
            return na

        self.__cpC['near_ring'][seq_key] = None
        return None

    def __getNearestParaFerroMagneticAtom(self, nmr_chain_id: str, nmr_seq_id: int, nmr_atom_id: str) -> Optional[dict]:
        """ Return the nearest paramagnetic/ferromagnetic atom around a given atom.
            @return: the nearest paramagnetic/ferromagnetic atom
        """

        if self.report.isDiamagnetic():
            return None

        cif_ps = self.report.getModelPolymerSequenceWithNmrChainId(nmr_chain_id)

        if cif_ps is None:
            return None

        cif_chain_id = cif_ps['chain_id']

        seq_align_dic = self.report.sequence_alignment.get()

        if not has_key_value(seq_align_dic, 'nmr_poly_seq_vs_model_poly_seq'):
            return None

        seq_key = (nmr_chain_id, nmr_seq_id, nmr_atom_id)

        if seq_key in self.__cpC['near_para_ferro']:
            return self.__cpC['near_para_ferro'][seq_key]

        result = next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq']
                       if seq_align['ref_chain_id'] == nmr_chain_id and seq_align['test_chain_id'] == cif_chain_id), None)

        if result is not None:

            cif_seq_id = next((test_seq_id for ref_seq_id, test_seq_id
                               in zip(result['ref_seq_id'], result['test_seq_id'])
                               if ref_seq_id == nmr_seq_id), None)

            if cif_seq_id is None:
                self.__cpC['near_para_ferro'][seq_key] = None
                return None

            try:

                model_num_name = 'pdbx_PDB_model_num' if 'pdbx_PDB_model_num' in self.__coord_atom_site_tags else 'ndb_model'

                _origin = self.__cR.getDictListWithFilter('atom_site',
                                                          [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                           {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                           {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                                                           ],
                                                          [{'name': 'label_asym_id', 'type': 'str', 'value': cif_chain_id},
                                                           {'name': 'label_seq_id', 'type': 'int', 'value': cif_seq_id},
                                                           {'name': 'label_atom_id', 'type': 'str', 'value': nmr_atom_id},
                                                           {'name': model_num_name, 'type': 'int', 'value': self.__representative_model_id},
                                                           {'name': 'label_alt_id', 'type': 'enum', 'enum': (self.__representative_alt_id,)}
                                                           ])

            except Exception as e:

                self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.__getNearestParaFerroMagneticAtom() ++ Error  - " + str(e))
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write(f"+{self.__class_name__}.__getNearestParaFerroMagneticAtom() ++ Error  - {str(e)}\n")

                return None

            if len(_origin) != 1:
                self.__cpC['near_para_ferro'][seq_key] = None
                return None

            o = to_np_array(_origin[0])

            try:

                _neighbor = self.__cR.getDictListWithFilter('atom_site',
                                                            [{'name': 'auth_asym_id', 'type': 'str', 'alt_name': 'chain_id', 'default': REPRESENTATIVE_ASYM_ID},
                                                             {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},  # non-polymer
                                                             {'name': 'label_comp_id', 'type': 'starts-with-alnum', 'alt_name': 'comp_id'},
                                                             {'name': 'label_atom_id', 'type': 'starts-with-alnum', 'alt_name': 'atom_id'},
                                                             {'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                             {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                             {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'},
                                                             {'name': 'type_symbol', 'type': 'str'}
                                                             ],
                                                            [{'name': 'Cartn_x', 'type': 'range-float',
                                                              'range': {'min_exclusive': (o[0] - CUTOFF_PARAMAGNETIC),
                                                                        'max_exclusive': (o[0] + CUTOFF_PARAMAGNETIC)}},
                                                             {'name': 'Cartn_y', 'type': 'range-float',
                                                              'range': {'min_exclusive': (o[1] - CUTOFF_PARAMAGNETIC),
                                                                        'max_exclusive': (o[1] + CUTOFF_PARAMAGNETIC)}},
                                                             {'name': 'Cartn_z', 'type': 'range-float',
                                                              'range': {'min_exclusive': (o[2] - CUTOFF_PARAMAGNETIC),
                                                                        'max_exclusive': (o[2] + CUTOFF_PARAMAGNETIC)}},
                                                             {'name': model_num_name, 'type': 'int', 'value': self.__representative_model_id},
                                                             {'name': 'label_alt_id', 'type': 'enum', 'enum': (self.__representative_alt_id,)}
                                                             ])

            except Exception as e:

                self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.__getNearestParaFerroMagneticAtom() ++ Error  - " + str(e))
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write(f"+{self.__class_name__}.__getNearestParaFerroMagneticAtom() ++ Error  - {str(e)}\n")

                return None

            if len(_neighbor) == 0:
                self.__cpC['near_para_ferro'][seq_key] = None
                return None

            neighbor = [n for n in _neighbor
                        if n['seq_id'] != cif_seq_id
                        and distance(to_np_array(n), o) < CUTOFF_PARAMAGNETIC
                        and (n['type_symbol'] in PARAMAGNETIC_ELEMENTS
                             or n['type_symbol'] in FERROMAGNETIC_ELEMENTS)]

            if len(neighbor) == 0:
                self.__cpC['near_para_ferro'][seq_key] = None
                return None

            atom_list = []

            for n in neighbor:
                atom_list.append({'chain_id': n['chain_id'], 'seq_id': n['seq_id'], 'comp_id': n['comp_id'], 'atom_id': n['atom_id'],
                                  'distance': distance(to_np_array(n), o)})

            if len(atom_list) == 0:
                return None

            p = sorted(atom_list, key=itemgetter('distance'))[0]

            try:

                _p = self.__cR.getDictListWithFilter('atom_site',
                                                     [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                      {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                      {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                                                      ],
                                                     [{'name': 'auth_asym_id', 'type': 'str', 'value': p['chain_id']},
                                                      {'name': 'auth_seq_id', 'type': 'int', 'value': p['seq_id']},  # non-polymer
                                                      {'name': 'label_comp_id', 'type': 'str', 'value': p['comp_id']},
                                                      {'name': 'label_atom_id', 'type': 'str', 'value': p['atom_id']},
                                                      {'name': 'label_alt_id', 'type': 'enum', 'enum': (self.__representative_alt_id,)}
                                                      ])

            except Exception as e:

                self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.__getNearestParaFerroMagneticAtom() ++ Error  - " + str(e))
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write(f"+{self.__class_name__}.__getNearestParaFerroMagneticAtom() ++ Error  - {str(e)}\n")

                return None

            if len(_p) == 0:
                self.__cpC['near_para_ferro'][seq_key] = None
                return None

            dist = 0.0

            for __p in _p:
                dist += distance(to_np_array(__p), o)

            p['distance'] = float(f"{dist / len(_p):.1f}")

            self.__cpC['near_para_ferro'][seq_key] = p
            return p

        self.__cpC['near_para_ferro'][seq_key] = None
        return None

    def testTautomerOfHistidinePerModel(self) -> bool:
        """ Check tautomeric state of a given histidine per model. (DAOTHER-9252)
        """

        src_id = self.report.getInputSourceIdOfCoord()

        if src_id < 0:
            return False

        cif_input_source = self.report.input_sources[src_id]
        cif_input_source_dic = cif_input_source.get()

        has_poly_seq = has_key_value(cif_input_source_dic, 'polymer_sequence')

        if not has_poly_seq:
            return False

        file_name = cif_input_source_dic['file_name']
        cif_poly_seq = cif_input_source_dic['polymer_sequence']

        if len(self.__cpC['tautomer_per_model']) > 0:

            for inst in self.__cpC['tautomer_per_model']:
                tautomer_per_model = inst['tautomer_per_model']

                try:
                    rep_tautomer = tautomer_per_model[self.__representative_model_id]
                except KeyError:
                    try:
                        rep_tautomer = tautomer_per_model[self.__eff_model_ids[0]]
                    except KeyError:
                        continue

                if any(tautomer != rep_tautomer for tautomer in tautomer_per_model.values()):
                    chain_id, auth_chain_id = inst['chain_id'], inst['auth_chain_id']
                    seq_id, auth_seq_id = inst['seq_id'], inst['auth_seq_id']
                    comp_id = inst['comp_id']
                    cif_seq_code = f"{chain_id}:{seq_id}:{comp_id}"
                    if chain_id != auth_chain_id or seq_id != auth_seq_id:
                        cif_seq_code += f" ({auth_chain_id}:{auth_seq_id}:{comp_id} in author sequence scheme)"

                    err = f'{cif_seq_code} has been instantiated with different tautomeric states across models, {tautomer_per_model}. '\
                        'Please re-upload the model file.'

                    if self.__internal_mode and not self.__conversion_server:

                        self.report.warning.appendDescription('coordinate_issue',
                                                              {'file_name': file_name, 'category': 'atom_site',
                                                               'description': err})
                        self.report.setWarning()

                        if self.__verbose:
                            self.__lfh.write(f"+{self.__class_name__}.testTautomerOfHistidinePerModel() ++ Warning  - {err}\n")

                    else:

                        self.report.error.appendDescription('coordinate_issue',
                                                            {'file_name': file_name, 'category': 'atom_site',
                                                             'description': err})
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write(f"+{self.__class_name__}.testTautomerOfHistidinePerModel() ++ Error  - {err}\n")

            return True

        model_num_name = 'pdbx_PDB_model_num' if 'pdbx_PDB_model_num' in self.__coord_atom_site_tags else 'ndb_model'

        for ps in cif_poly_seq:
            chain_id = ps['chain_id']

            auth_chain_id = chain_id
            if 'auth_chain_id' in ps:
                auth_chain_id = ps['auth_chain_id']

            if len(cif_poly_seq) >= LEN_MAJOR_ASYM_ID:
                if auth_chain_id not in LARGE_ASYM_ID:
                    continue

            for seq_id, comp_id in zip(ps['seq_id'], ps['comp_id']):

                if not isLikeHis(comp_id, self.__ccU):
                    continue

                if comp_id == 'HIS':
                    hd1_name = 'HD1'
                    he2_name = 'HE2'
                else:
                    _hd1_name = self.__ccU.getBondedAtoms(comp_id, 'ND1', onlyProton=True)
                    _he2_name = self.__ccU.getBondedAtoms(comp_id, 'NE2', onlyProton=True)
                    if len(_hd1_name) != 1 or len(_he2_name) != 1:
                        continue
                    hd1_name = _hd1_name[0]
                    he2_name = _he2_name[0]

                try:
                    auth_seq_id = ps['auth_seq_id'][ps['seq_id'].index(seq_id)]
                except (KeyError, IndexError, ValueError):
                    auth_seq_id = seq_id

                try:

                    protons = self.__cR.getDictListWithFilter('atom_site',
                                                              [{'name': 'label_atom_id', 'type': 'starts-with-alnum', 'alt_name': 'atom_id'},
                                                               {'name': model_num_name, 'type': 'int', 'alt_name': 'model_id'},
                                                               ],
                                                              [{'name': 'label_asym_id', 'type': 'str', 'value': chain_id},
                                                               {'name': 'label_seq_id', 'type': 'int', 'value': seq_id},
                                                               {'name': 'label_comp_id', 'type': 'str', 'value': comp_id},
                                                               {'name': 'type_symbol', 'type': 'str', 'value': 'H'},
                                                               {'name': 'label_alt_id', 'type': 'enum', 'enum': (self.__representative_alt_id,)}
                                                               ])

                except Exception as e:

                    self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.testTautomerOfHistidinePerModel() ++ Error  - " + str(e))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write(f"+{self.__class_name__}.testTautomerOfHistidinePerModel() ++ Error  - {str(e)}\n")

                    return False

                if len(protons) > 0:

                    tautomer_per_model = {}

                    for model_id in self.__eff_model_ids:

                        _protons = [h for h in protons if h['model_id'] == model_id]

                        has_hd1 = has_he2 = False

                        for h in _protons:
                            if h['atom_id'] == hd1_name:
                                has_hd1 = True
                            elif h['atom_id'] == he2_name:
                                has_he2 = True

                        if has_hd1 and has_he2:
                            tautomer_per_model[model_id] = 'biprotonated'

                        elif has_hd1:
                            tautomer_per_model[model_id] = 'pi-tautomer'

                        elif has_he2:
                            tautomer_per_model[model_id] = 'tau-tautomer'

                        else:
                            tautomer_per_model[model_id] = 'unknown'

                    try:
                        rep_tautomer = tautomer_per_model[self.__representative_model_id]
                    except KeyError:
                        try:
                            rep_tautomer = tautomer_per_model[self.__eff_model_ids[0]]
                        except KeyError:
                            continue

                    self.__cpC['tautomer_per_model'].append({'chain_id': chain_id, 'seq_id': seq_id, 'comp_id': comp_id,
                                                             'auth_chain_id': auth_chain_id, 'auth_seq_id': auth_seq_id,
                                                             'tautomer_per_model': tautomer_per_model})

                    if any(tautomer != rep_tautomer for tautomer in tautomer_per_model.values()):
                        cif_seq_code = f"{chain_id}:{seq_id}:{comp_id}"
                        if chain_id != auth_chain_id or seq_id != auth_seq_id:
                            cif_seq_code += f" ({auth_chain_id}:{auth_seq_id}:{comp_id} in author sequence scheme)"

                        err = f'{cif_seq_code} has been instantiated with different tautomeric states across models, {tautomer_per_model}. '\
                            'Please re-upload the model file.'

                        if self.__internal_mode and not self.__conversion_server:

                            self.report.warning.appendDescription('coordinate_issue',
                                                                  {'file_name': file_name, 'category': 'atom_site',
                                                                   'description': err})
                            self.report.setWarning()

                            if self.__verbose:
                                self.__lfh.write(f"+{self.__class_name__}.testTautomerOfHistidinePerModel() ++ Warning  - {err}\n")

                        else:

                            self.report.error.appendDescription('coordinate_issue',
                                                                {'file_name': file_name, 'category': 'atom_site',
                                                                 'description': err})
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write(f"+{self.__class_name__}.testTautomerOfHistidinePerModel() ++ Error  - {err}\n")

        if self.__coordPropCachePath is not None:
            hash_value = hash(str(self.__cpC))
            if hash_value != self.__cpC_hash:
                write_as_pickle(self.__cpC, self.__coordPropCachePath)
                self.__cpC_hash = hash_value

        return True

    def getTautomerOfHistidine(self, nmr_chain_id: str, nmr_seq_id: int) -> str:
        """ Return tautomeric state of a given histidine.
            @return: One of 'biprotonated', 'tau-tautomer', 'pi-tautomer', 'unknown'
        """

        cif_ps = self.report.getModelPolymerSequenceWithNmrChainId(nmr_chain_id)

        if cif_ps is None:
            return 'unknown'

        cif_chain_id = cif_ps['chain_id']

        seq_align_dic = self.report.sequence_alignment.get()

        if not has_key_value(seq_align_dic, 'nmr_poly_seq_vs_model_poly_seq'):
            return 'unknown'

        seq_key = (nmr_chain_id, nmr_seq_id)

        if seq_key in self.__cpC['tautomer']:
            return self.__cpC['tautomer'][seq_key]

        result = next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq']
                       if seq_align['ref_chain_id'] == nmr_chain_id and seq_align['test_chain_id'] == cif_chain_id), None)

        if result is not None:

            cif_seq_id = next((test_seq_id for ref_seq_id, ref_code, test_seq_id
                               in zip(result['ref_seq_id'], result['ref_code'], result['test_seq_id'])
                               if ref_seq_id == nmr_seq_id and ref_code == 'H'), None)

            if cif_seq_id is None:
                self.__cpC['tautomer'][seq_key] = 'unknown'
                return 'unknown'

            try:

                model_num_name = 'pdbx_PDB_model_num' if 'pdbx_PDB_model_num' in self.__coord_atom_site_tags else 'ndb_model'

                protons = self.__cR.getDictListWithFilter('atom_site',
                                                          [{'name': 'label_atom_id', 'type': 'starts-with-alnum', 'alt_name': 'atom_id'}
                                                           ],
                                                          [{'name': 'label_asym_id', 'type': 'str', 'value': cif_chain_id},
                                                           {'name': 'label_seq_id', 'type': 'int', 'value': cif_seq_id},
                                                           {'name': 'label_comp_id', 'type': 'str', 'value': 'HIS'},
                                                           {'name': 'type_symbol', 'type': 'str', 'value': 'H'},
                                                           {'name': model_num_name, 'type': 'int', 'value': self.__representative_model_id},
                                                           {'name': 'label_alt_id', 'type': 'enum', 'enum': (self.__representative_alt_id,)}
                                                           ])

            except Exception as e:

                self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.getTautomerOfHistidine() ++ Error  - " + str(e))
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write(f"+{self.__class_name__}.getTautomerOfHistidine() ++ Error  - {str(e)}\n")

                return 'unknown'

            if len(protons) > 0:

                has_hd1 = has_he2 = False

                for h in protons:
                    if h['atom_id'] == 'HD1':
                        has_hd1 = True
                    elif h['atom_id'] == 'HE2':
                        has_he2 = True

                if has_hd1 and has_he2:
                    self.__cpC['tautomer'][seq_key] = 'biprotonated'
                    return 'biprotonated'

                if has_hd1:
                    self.__cpC['tautomer'][seq_key] = 'pi-tautomer'
                    return 'pi-tautomer'

                if has_he2:
                    self.__cpC['tautomer'][seq_key] = 'tau-tautomer'
                    return 'tau-tautomer'

        self.__cpC['tautomer'][seq_key] = 'unknown'
        return 'unknown'

    def getRotamerOfValine(self, nmr_chain_id: str, nmr_seq_id: int) -> List[dict]:
        """ Return rotameric state distribution of a given valine.
            @return: One of 'gauche+', 'trans', 'gauche-', 'unknown'
        """

        none = [{'name': 'chi1', 'unknown': 1.0}]

        cif_ps = self.report.getModelPolymerSequenceWithNmrChainId(nmr_chain_id)

        if cif_ps is None:
            return none

        cif_chain_id = cif_ps['chain_id']

        seq_align_dic = self.report.sequence_alignment.get()

        if not has_key_value(seq_align_dic, 'nmr_poly_seq_vs_model_poly_seq'):
            return none

        seq_key = (nmr_chain_id, nmr_seq_id, 'VAL')

        if seq_key in self.__cpC['rotamer']:
            return self.__cpC['rotamer'][seq_key]

        result = next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq']
                       if seq_align['ref_chain_id'] == nmr_chain_id and seq_align['test_chain_id'] == cif_chain_id), None)

        if result is not None:

            cif_seq_id = next((test_seq_id for ref_seq_id, ref_code, test_seq_id
                               in zip(result['ref_seq_id'], result['ref_code'], result['test_seq_id'])
                               if ref_seq_id == nmr_seq_id and ref_code == 'V'), None)

            if cif_seq_id is None:
                self.__cpC['rotamer'][seq_key] = none
                return none

            try:

                model_num_name = 'pdbx_PDB_model_num' if 'pdbx_PDB_model_num' in self.__coord_atom_site_tags else 'ndb_model'

                atoms = self.__cR.getDictListWithFilter('atom_site',
                                                        [{'name': 'label_atom_id', 'type': 'starts-with-alnum', 'alt_name': 'atom_id'},
                                                         {'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                         {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                         {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'},
                                                         {'name': model_num_name, 'type': 'int', 'alt_name': 'model_id'}
                                                         ],
                                                        [{'name': 'label_asym_id', 'type': 'str', 'value': cif_chain_id},
                                                         {'name': 'label_seq_id', 'type': 'int', 'value': cif_seq_id},
                                                         {'name': 'label_comp_id', 'type': 'str', 'value': 'VAL'},
                                                         {'name': 'label_alt_id', 'type': 'enum', 'enum': (self.__representative_alt_id,)}
                                                         ])

            except Exception as e:

                self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.getRotamerOfValine() ++ Error  - " + str(e))
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write(f"+{self.__class_name__}.getRotamerOfValine() ++ Error  - {str(e)}\n")

                return none

            model_ids = set(a['model_id'] for a in atoms)
            total_models = float(len(model_ids))

            rot1 = {'name': 'chi1', 'gauche-': 0.0, 'trans': 0.0, 'gauche+': 0.0, 'unknown': 0.0}

            for model_id in model_ids:
                _atoms = [a for a in atoms if a['model_id'] == model_id]

                try:
                    n = to_np_array(next(a for a in _atoms if a['atom_id'] == 'N'))
                    ca = to_np_array(next(a for a in _atoms if a['atom_id'] == 'CA'))
                    cb = to_np_array(next(a for a in _atoms if a['atom_id'] == 'CB'))
                    cg1 = to_np_array(next(a for a in _atoms if a['atom_id'] == 'CG1'))

                    chi1 = dihedral_angle(n, ca, cb, cg1)

                    if 0.0 <= chi1 < 120.0:
                        rot1['gauche+'] += 1.0
                    elif -120.0 <= chi1 < 0.0:
                        rot1['gauche-'] += 1.0
                    else:
                        rot1['trans'] += 1.0
                except StopIteration:
                    rot1['unknown'] += 1.0

            if rot1['unknown'] == total_models:
                self.__cpC['rotamer'][seq_key] = none
                return none

            if rot1['unknown'] == 0.0:
                del rot1['unknown']

            _rot1 = rot1.copy()

            for k, v in _rot1.items():
                if k == 'name':
                    continue
                rot1[k] = float(f"{v/total_models:.3f}")

            self.__cpC['rotamer'][seq_key] = [rot1]
            return [rot1]

        self.__cpC['rotamer'][seq_key] = none
        return none

    def getRotamerOfLeucine(self, nmr_chain_id: str, nmr_seq_id: int) -> List[dict]:
        """ Return rotameric state distribution of a given leucine.
            @return: One of 'gauche+', 'trans', 'gauche-', 'unknown'
        """

        none = [{'name': 'chi1', 'unknown': 1.0}, {'name': 'chi2', 'unknown': 1.0}]

        cif_ps = self.report.getModelPolymerSequenceWithNmrChainId(nmr_chain_id)

        if cif_ps is None:
            return none

        cif_chain_id = cif_ps['chain_id']

        seq_align_dic = self.report.sequence_alignment.get()

        if not has_key_value(seq_align_dic, 'nmr_poly_seq_vs_model_poly_seq'):
            return none

        seq_key = (nmr_chain_id, nmr_seq_id, 'LEU')

        if seq_key in self.__cpC['rotamer']:
            return self.__cpC['rotamer'][seq_key]

        result = next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq']
                       if seq_align['ref_chain_id'] == nmr_chain_id and seq_align['test_chain_id'] == cif_chain_id), None)

        if result is not None:

            cif_seq_id = next((test_seq_id for ref_seq_id, ref_code, test_seq_id
                               in zip(result['ref_seq_id'], result['ref_code'], result['test_seq_id'])
                               if ref_seq_id == nmr_seq_id and ref_code == 'L'), None)

            if cif_seq_id is None:
                self.__cpC['rotamer'][seq_key] = none
                return none

            try:

                model_num_name = 'pdbx_PDB_model_num' if 'pdbx_PDB_model_num' in self.__coord_atom_site_tags else 'ndb_model'

                atoms = self.__cR.getDictListWithFilter('atom_site',
                                                        [{'name': 'label_atom_id', 'type': 'starts-with-alnum', 'alt_name': 'atom_id'},
                                                         {'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                         {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                         {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'},
                                                         {'name': model_num_name, 'type': 'int', 'alt_name': 'model_id'}
                                                         ],
                                                        [{'name': 'label_asym_id', 'type': 'str', 'value': cif_chain_id},
                                                         {'name': 'label_seq_id', 'type': 'int', 'value': cif_seq_id},
                                                         {'name': 'label_comp_id', 'type': 'str', 'value': 'LEU'},
                                                         {'name': 'label_alt_id', 'type': 'enum', 'enum': (self.__representative_alt_id,)}
                                                         ])

            except Exception as e:

                self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.getRotamerOfLeucine() ++ Error  - " + str(e))
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write(f"+{self.__class_name__}.getRotamerOfLeucine() ++ Error  - {str(e)}\n")

                return none

            model_ids = set(a['model_id'] for a in atoms)
            total_models = float(len(model_ids))

            rot1 = {'name': 'chi1', 'gauche-': 0.0, 'trans': 0.0, 'gauche+': 0.0, 'unknown': 0.0}
            rot2 = {'name': 'chi2', 'gauche-': 0.0, 'trans': 0.0, 'gauche+': 0.0, 'unknown': 0.0}

            for model_id in model_ids:
                _atoms = [a for a in atoms if a['model_id'] == model_id]

                try:
                    n = to_np_array(next(a for a in _atoms if a['atom_id'] == 'N'))
                    ca = to_np_array(next(a for a in _atoms if a['atom_id'] == 'CA'))
                    cb = to_np_array(next(a for a in _atoms if a['atom_id'] == 'CB'))
                    cg = to_np_array(next(a for a in _atoms if a['atom_id'] == 'CG'))
                    cd1 = to_np_array(next(a for a in _atoms if a['atom_id'] == 'CD1'))

                    chi1 = dihedral_angle(n, ca, cb, cg)

                    if 0.0 <= chi1 < 120.0:
                        rot1['gauche+'] += 1.0
                    elif -120.0 <= chi1 < 0.0:
                        rot1['gauche-'] += 1.0
                    else:
                        rot1['trans'] += 1.0

                    chi2 = dihedral_angle(ca, cb, cg, cd1)

                    if 0.0 <= chi2 < 120.0:
                        rot2['gauche+'] += 1.0
                    elif -120.0 <= chi2 < 0.0:
                        rot2['gauche-'] += 1.0
                    else:
                        rot2['trans'] += 1.0

                except StopIteration:
                    rot1['unknown'] += 1.0
                    rot2['unknown'] += 1.0

            if rot1['unknown'] == total_models:
                self.__cpC['rotamer'][seq_key] = none
                return none

            if rot1['unknown'] == 0.0:
                del rot1['unknown']
            if rot2['unknown'] == 0.0:
                del rot2['unknown']

            _rot1 = rot1.copy()
            _rot2 = rot2.copy()

            for k, v in _rot1.items():
                if k == 'name':
                    continue
                rot1[k] = float(f"{v/total_models:.3f}")

            for k, v in _rot2.items():
                if k == 'name':
                    continue
                rot2[k] = float(f"{v/total_models:.3f}")

            self.__cpC['rotamer'][seq_key] = [rot1, rot2]
            return [rot1, rot2]

        self.__cpC['rotamer'][seq_key] = none
        return none

    def getRotamerOfIsoleucine(self, nmr_chain_id: str, nmr_seq_id: int) -> List[dict]:
        """ Return rotameric state distribution of a given isoleucine.
            @return: One of 'gauche+', 'trans', 'gauche-', 'unknown'
        """

        none = [{'name': 'chi1', 'unknown': 1.0}, {'name': 'chi2', 'unknown': 1.0}]

        cif_ps = self.report.getModelPolymerSequenceWithNmrChainId(nmr_chain_id)

        if cif_ps is None:
            return none

        cif_chain_id = cif_ps['chain_id']

        seq_align_dic = self.report.sequence_alignment.get()

        if not has_key_value(seq_align_dic, 'nmr_poly_seq_vs_model_poly_seq'):
            return none

        seq_key = (nmr_chain_id, nmr_seq_id, 'ILE')

        if seq_key in self.__cpC['rotamer']:
            return self.__cpC['rotamer'][seq_key]

        result = next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq']
                       if seq_align['ref_chain_id'] == nmr_chain_id and seq_align['test_chain_id'] == cif_chain_id), None)

        if result is not None:

            cif_seq_id = next((test_seq_id for ref_seq_id, ref_code, test_seq_id
                               in zip(result['ref_seq_id'], result['ref_code'], result['test_seq_id'])
                               if ref_seq_id == nmr_seq_id and ref_code == 'I'), None)

            if cif_seq_id is None:
                self.__cpC['rotamer'][seq_key] = none
                return none

            try:

                model_num_name = 'pdbx_PDB_model_num' if 'pdbx_PDB_model_num' in self.__coord_atom_site_tags else 'ndb_model'

                atoms = self.__cR.getDictListWithFilter('atom_site',
                                                        [{'name': 'label_atom_id', 'type': 'starts-with-alnum', 'alt_name': 'atom_id'},
                                                         {'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                         {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                         {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'},
                                                         {'name': model_num_name, 'type': 'int', 'alt_name': 'model_id'}
                                                         ],
                                                        [{'name': 'label_asym_id', 'type': 'str', 'value': cif_chain_id},
                                                         {'name': 'label_seq_id', 'type': 'int', 'value': cif_seq_id},
                                                         {'name': 'label_comp_id', 'type': 'str', 'value': 'ILE'},
                                                         {'name': 'label_alt_id', 'type': 'enum', 'enum': (self.__representative_alt_id,)}
                                                         ])

            except Exception as e:

                self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.getRotamerOfIsoleucine() ++ Error  - " + str(e))
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write(f"+{self.__class_name__}.getRotamerOfIsoleucine() ++ Error  - {str(e)}\n")

                return none

            model_ids = set(a['model_id'] for a in atoms)
            total_models = float(len(model_ids))

            rot1 = {'name': 'chi1', 'gauche-': 0.0, 'trans': 0.0, 'gauche+': 0.0, 'unknown': 0.0}
            rot2 = {'name': 'chi2', 'gauche-': 0.0, 'trans': 0.0, 'gauche+': 0.0, 'unknown': 0.0}

            for model_id in model_ids:
                _atoms = [a for a in atoms if a['model_id'] == model_id]

                try:
                    n = to_np_array(next(a for a in _atoms if a['atom_id'] == 'N'))
                    ca = to_np_array(next(a for a in _atoms if a['atom_id'] == 'CA'))
                    cb = to_np_array(next(a for a in _atoms if a['atom_id'] == 'CB'))
                    cg1 = to_np_array(next(a for a in _atoms if a['atom_id'] == 'CG1'))
                    cd1 = to_np_array(next(a for a in _atoms if a['atom_id'] == 'CD1'))

                    chi1 = dihedral_angle(n, ca, cb, cg1)

                    if 0.0 <= chi1 < 120.0:
                        rot1['gauche+'] += 1.0
                    elif -120.0 <= chi1 < 0.0:
                        rot1['gauche-'] += 1.0
                    else:
                        rot1['trans'] += 1.0

                    chi2 = dihedral_angle(ca, cb, cg1, cd1)

                    if 0.0 <= chi2 < 120.0:
                        rot2['gauche+'] += 1.0
                    elif -120.0 <= chi2 < 0.0:
                        rot2['gauche-'] += 1.0
                    else:
                        rot2['trans'] += 1.0

                except StopIteration:
                    rot1['unknown'] += 1.0
                    rot2['unknown'] += 1.0

            if rot1['unknown'] == total_models:
                self.__cpC['rotamer'][seq_key] = none
                return none

            if rot1['unknown'] == 0.0:
                del rot1['unknown']
            if rot2['unknown'] == 0.0:
                del rot2['unknown']

            _rot1 = rot1.copy()
            _rot2 = rot2.copy()

            for k, v in _rot1.items():
                if k == 'name':
                    continue
                rot1[k] = float(f"{v/total_models:.3f}")

            for k, v in _rot2.items():
                if k == 'name':
                    continue
                rot2[k] = float(f"{v/total_models:.3f}")

            self.__cpC['rotamer'][seq_key] = [rot1, rot2]
            return [rot1, rot2]

        self.__cpC['rotamer'][seq_key] = none
        return none

    def __fixAtomNomenclature(self, comp_id: str, atom_id_conv_dict: dict):
        """ Fix atom nomenclature.
        """

        for fileListId in range(self.__file_path_list_len):

            input_source = self.report.input_sources[fileListId]
            input_source_dic = input_source.get()

            file_type = input_source_dic['file_type']

            if input_source_dic['content_subtype'] is None:
                continue

            for content_subtype in input_source_dic['content_subtype']:

                if content_subtype == ['entry_info', 'entity', 'chem_shift_ref']:
                    continue

                sf_category = SF_CATEGORIES[file_type][content_subtype]
                lp_category = LP_CATEGORIES[file_type][content_subtype]

                if content_subtype == 'poly_seq':
                    lp_category = AUX_LP_CATEGORIES[file_type][content_subtype][0]

                if file_type == 'nmr-star' and content_subtype == 'spectral_peak_alt':
                    lp_category = '_Assigned_peak_chem_shift'

                if self.__star_data_type[fileListId] == 'Loop':
                    sf = self.__star_data[fileListId]

                    self.__fixAtomNomenclature__(fileListId, file_type, content_subtype, sf, lp_category, comp_id, atom_id_conv_dict)

                elif self.__star_data_type[fileListId] == 'Saveframe':
                    sf = self.__star_data[fileListId]

                    self.__fixAtomNomenclature__(fileListId, file_type, content_subtype, sf, lp_category, comp_id, atom_id_conv_dict)

                else:

                    for sf in self.__star_data[fileListId].get_saveframes_by_category(sf_category):

                        if not any(True for loop in sf.loops if loop.category == lp_category):
                            continue

                        self.__fixAtomNomenclature__(fileListId, file_type, content_subtype, sf, lp_category, comp_id, atom_id_conv_dict)

    def __fixAtomNomenclature__(self, file_list_id: int, file_type: str, content_subtype: str,
                                sf: Union[pynmrstar.Saveframe, pynmrstar.Loop],
                                lp_category: str, comp_id: str, atom_id_conv_dict: dict):
        """ Fix atom nomenclature.
        """

        comp_id_name = 'residue_name' if file_type == 'nef' else 'Comp_ID'
        atom_id_name = 'atom_name' if file_type == 'nef' else 'Atom_ID'

        max_dim = 2

        if content_subtype in ('poly_seq', 'dist_restraint', 'rdc_restraint'):
            max_dim = 3

        elif content_subtype == 'dihed_restraint':
            max_dim = 5

        elif content_subtype == 'spectral_peak':

            try:

                _num_dim = get_first_sf_tag(sf, NUM_DIM_ITEMS[file_type])
                num_dim = int(_num_dim)

                if num_dim not in range(1, MAX_DIM_NUM_OF_SPECTRA):
                    raise ValueError()

            except ValueError:  # raised error already at testIndexConsistency()
                return

            max_dim = num_dim + 1

        loop = sf if self.__star_data_type[file_list_id] == 'Loop' else sf.get_loop(lp_category)

        if max_dim == 2:

            comp_id_col = loop.tags.index(comp_id_name) if comp_id_name in loop.tags else -1
            atom_id_col = loop.tags.index(atom_id_name) if atom_id_name in loop.tags else -1

            if -1 in (comp_id_col, atom_id_col):
                return

            for row in loop:

                _comp_id = row[comp_id_col].upper()

                if _comp_id != comp_id:
                    continue

                atom_id = row[atom_id_col]

                if atom_id in atom_id_conv_dict:
                    row[atom_id_col] = atom_id_conv_dict[atom_id]

        else:

            for j in range(1, max_dim):

                _comp_id_name = comp_id_name + '_' + str(j)
                _atom_id_name = atom_id_name + '_' + str(j)

                comp_id_col = loop.tags.index(_comp_id_name) if _comp_id_name in loop.tags else -1
                atom_id_col = loop.tags.index(_atom_id_name) if _atom_id_name in loop.tags else -1

                if -1 in (comp_id_col, atom_id_col):
                    continue

                for row in loop:

                    _comp_id = row[comp_id_col].upper()

                    if _comp_id != comp_id:
                        continue

                    atom_id = row[atom_id_col]

                    if atom_id in atom_id_conv_dict:
                        row[atom_id_col] = atom_id_conv_dict[atom_id]

    def updateGenDistConstIdInMrStr(self, sf_item: dict) -> bool:
        """ Update _Gen_dist_constraint.ID in NMR-STAR restraint file.
        """

        loop = sf_item['loop']

        lp = pynmrstar.Loop.from_scratch(loop.category)

        lp.add_tag(loop.tags)

        id_col = loop.tags.index('ID')
        if 'Index_ID' not in loop.tags:
            tag = loop.category + '.Index_ID'
            for idx in range(len(loop)):
                loop.data[idx].append(idx + 1)
            loop.add_tag(tag)
            lp.add_tag(tag)
        if 'Member_ID' not in loop.tags:
            tag = loop.category + '.Member_ID'
            loop.add_tag(tag, update_data=True)
            lp.add_tag(tag)
        if 'Member_logic_code' not in loop.tags:
            tag = loop.category + '.Member_logic_code'
            loop.add_tag(tag, update_data=True)
            lp.add_tag(tag)

        index_id_col = loop.tags.index('Index_ID')
        member_id_col = loop.tags.index('Member_ID')
        member_logic_code_col = loop.tags.index('Member_logic_code')

        combination_id_col = loop.tags.index('Combination_ID') if 'Combination_ID' in loop.tags else -1

        chain_id_1_col = loop.tags.index('Auth_asym_ID_1')
        seq_id_1_col = loop.tags.index('Auth_seq_ID_1')
        comp_id_1_col = loop.tags.index('Auth_comp_ID_1')
        atom_id_1_col = loop.tags.index('Auth_atom_ID_1')

        ref_chain_id_1_col = loop.tags.index('Entity_assembly_ID_1')
        ref_seq_id_1_col = loop.tags.index('Comp_index_ID_1')
        ref_comp_id_1_col = loop.tags.index('Comp_ID_1')
        ref_atom_id_1_col = loop.tags.index('Atom_ID_1')

        chain_id_2_col = loop.tags.index('Auth_asym_ID_2')
        seq_id_2_col = loop.tags.index('Auth_seq_ID_2')
        comp_id_2_col = loop.tags.index('Auth_comp_ID_2')
        atom_id_2_col = loop.tags.index('Auth_atom_ID_2')

        ref_chain_id_2_col = loop.tags.index('Entity_assembly_ID_2')
        ref_seq_id_2_col = loop.tags.index('Comp_index_ID_2')
        ref_comp_id_2_col = loop.tags.index('Comp_ID_2')
        ref_atom_id_2_col = loop.tags.index('Atom_ID_2')

        target_val_col = loop.tags.index('Target_val') if 'Target_val' in loop.tags else -1
        target_val_err_col = loop.tags.index('Target_val_uncertainty') if 'Target_val_uncertainty' in loop.tags else -1
        lower_linear_limit_col = loop.tags.index('Lower_linear_limit') if 'Lower_linear_limit' in loop.tags else -1
        upper_linear_limit_col = loop.tags.index('Upper_linear_limit') if 'Upper_linear_limit' in loop.tags else -1
        lower_limit_col = loop.tags.index('Distance_lower_bound_val') if 'Distance_lower_bound_val' in loop.tags else -1
        upper_limit_col = loop.tags.index('Distance_upper_bound_val') if 'Distance_upper_bound_val' in loop.tags else -1
        weight_col = loop.tags.index('Weight') if 'Weight' in loop.tags else -1

        cs_loops = self.__lp_data['chem_shift']

        @functools.lru_cache()
        def get_cs_value(chain_id, seq_id, comp_id, atom_id):
            if cs_loops is None or len(cs_loops) == 0:
                return None

            if isinstance(chain_id, int):
                chain_id = str(chain_id)

            _atom_ids = self.__nefT.get_valid_star_atom(comp_id, atom_id, leave_unmatched=False)[0]

            for lp in cs_loops:
                row = next((row for row in lp['data']
                            if row['Entity_assembly_ID'] == chain_id and row['Comp_index_ID'] == seq_id
                            and row['Comp_ID'] == comp_id and row['Atom_ID'] in _atom_ids), None)

                if row is not None:
                    val = row['Val']
                    return val if val not in emptyValue else None

            return None

        def concat_target_val(row):
            return (str(row[target_val_col]) if target_val_col != -1 else '')\
                + (str(row[target_val_err_col]) if target_val_err_col != -1 else '')\
                + (str(row[lower_linear_limit_col]) if lower_linear_limit_col != -1 else '')\
                + (str(row[upper_linear_limit_col]) if upper_linear_limit_col != -1 else '')\
                + (str(row[lower_limit_col]) if lower_limit_col != -1 else '')\
                + (str(row[upper_limit_col]) if upper_limit_col != -1 else '')\
                + (str(row[weight_col]) if weight_col != -1 else '')

        _rest_id = _member_logic_code = _cs_val1 = _cs_val2 = None
        _atom1, _atom2 = {}, {}
        _values = ''

        modified = has_member_id = False

        sf_item['id'] = 0

        for row in loop:
            _row = row

            sf_item['id'] += 1
            duplicated = False

            try:

                rest_id = row[id_col]
                try:
                    member_id = row[member_id_col]
                except IndexError:
                    member_id = None
                try:
                    member_logic_code = row[member_logic_code_col]
                except IndexError:
                    member_logic_code = None
                values = concat_target_val(row)

                try:
                    atom1 = {'chain_id': row[chain_id_1_col],
                             'seq_id': int(row[seq_id_1_col]),
                             'comp_id': row[comp_id_1_col],
                             'atom_id': row[atom_id_1_col],
                             'ref_chain_id': row[ref_chain_id_1_col],
                             'ref_seq_id': int(row[ref_seq_id_1_col]),
                             'ref_comp_id': row[ref_comp_id_1_col],
                             'ref_atom_id': row[ref_atom_id_1_col]}
                    cs_val1 = get_cs_value(atom1['ref_chain_id'], atom1['ref_seq_id'], atom1['ref_comp_id'], atom1['ref_atom_id'])
                except (ValueError, TypeError):
                    atom1 = {}
                    cs_val1 = None

                try:
                    atom2 = {'chain_id': row[chain_id_2_col],
                             'seq_id': int(row[seq_id_2_col]),
                             'comp_id': row[comp_id_2_col],
                             'atom_id': row[atom_id_2_col],
                             'ref_chain_id': row[ref_chain_id_2_col],
                             'ref_seq_id': int(row[ref_seq_id_2_col]),
                             'ref_comp_id': row[ref_comp_id_2_col],
                             'ref_atom_id': row[ref_atom_id_2_col]}
                    cs_val2 = get_cs_value(atom2['ref_chain_id'], atom2['ref_seq_id'], atom2['ref_comp_id'], atom2['ref_atom_id'])
                except (ValueError, TypeError):
                    atom2 = {}
                    cs_val2 = None

                if member_id not in emptyValue:
                    has_member_id = True

                _atoms1 = [atom1, _atom1]
                _atoms2 = [atom2, _atom2]

                if _rest_id is None:
                    pass

                elif rest_id != _rest_id and len(atom1) > 0 and len(atom2) > 0:

                    if (member_id in emptyValue or member_logic_code == 'OR'):

                        if atom1['atom_id'][0] in protonBeginCode and atom2['atom_id'][0] in protonBeginCode:

                            if (values == _values and not isAmbigAtomSelection(_atoms1, self.__csStat)
                                and not isAmbigAtomSelection(_atoms2, self.__csStat))\
                               or (values == _values and atom1['ref_chain_id'] != atom2['ref_chain_id']
                                   and ((not isAmbigAtomSelection(_atoms1, self.__csStat)
                                         and atom1['ref_chain_id'] != _atom2['ref_chain_id'] and atom2['comp_id'] == _atom2['comp_id'])
                                        or (not isAmbigAtomSelection(_atoms2, self.__csStat)
                                            and atom2['ref_chain_id'] != _atom1['ref_chain_id'] and atom1['comp_id'] == _atom1['comp_id']))):

                                diff_cs_val1 = cs_val1 is not None and _cs_val1 is not None and cs_val1 != _cs_val1
                                diff_cs_val2 = cs_val2 is not None and _cs_val2 is not None and cs_val2 != _cs_val2

                                if (not isAmbigAtomSelection(_atoms1, self.__csStat) and diff_cs_val1)\
                                   or (not isAmbigAtomSelection(_atoms2, self.__csStat) and diff_cs_val2):
                                    pass

                                else:

                                    try:

                                        _row[member_logic_code_col] = 'OR'

                                        if _member_logic_code in emptyValue:
                                            lp.data[-1][member_logic_code_col] = 'OR'

                                    except IndexError:
                                        pass

                                    sf_item['id'] -= 1

                                    modified = True

                        elif values == _values and isIdenticalRestraint(_atoms1, self.__nefT) and isIdenticalRestraint(_atoms2, self.__nefT):
                            sf_item['id'] -= 1
                            duplicated = True

                elif member_logic_code != 'AND':

                    if not isAmbigAtomSelection(_atoms1, self.__csStat)\
                       and not isAmbigAtomSelection(_atoms2, self.__csStat):

                        if member_logic_code in emptyValue:
                            modified = True

                        try:

                            _row[member_logic_code_col] = 'OR'

                            if _member_logic_code in emptyValue:
                                lp.data[-1][member_logic_code_col] = 'OR'

                                modified = True

                        except IndexError:
                            pass

                    sf_item['id'] -= 1

                _rest_id, _member_logic_code, _atom1, _atom2, _values, _cs_val1, _cs_val2 =\
                    rest_id, member_logic_code, atom1, atom2, values, cs_val1, cs_val2

            except ValueError:
                _atom1, _atom2 = {}, {}

            if not self.__native_combined:  # DAOTHER-8855
                _row[id_col] = sf_item['id']
            if combination_id_col == -1 or (combination_id_col != -1 and _row[combination_id_col] in emptyValue):
                try:
                    _row[member_id_col] = None
                except IndexError:
                    pass

            if duplicated:
                continue

            lp.add_data(_row)

        get_cs_value.cache_clear()

        if not modified and not has_member_id:
            return True

        member_id_dict = {}

        def update_member_id_dict(rows):
            if len(rows) < 2:
                return

            atom_sel1, atom_sel2 = [], []

            for row in rows:

                try:
                    atom1 = {'chain_id': row[chain_id_1_col],
                             'seq_id': int(row[seq_id_1_col]),
                             'comp_id': row[comp_id_1_col],
                             'atom_id': row[atom_id_1_col]}
                except (ValueError, TypeError):
                    atom1 = {}

                try:
                    atom2 = {'chain_id': row[chain_id_2_col],
                             'seq_id': int(row[seq_id_2_col]),
                             'comp_id': row[comp_id_2_col],
                             'atom_id': row[atom_id_2_col]}
                except (ValueError, TypeError):
                    atom2 = {}

                atom_sel1.append(atom1)
                atom_sel2.append(atom2)

            if isAmbigAtomSelection(atom_sel1, self.__csStat)\
               or isAmbigAtomSelection(atom_sel2, self.__csStat):
                for member_id, row in enumerate(rows, start=1):
                    try:
                        index_id = row[index_id_col]
                        member_id_dict[index_id] = member_id
                    except IndexError:
                        pass

        _row = _rest_id = None
        _union_rows = []

        for row in lp:
            rest_id = row[id_col]

            if _rest_id is not None and rest_id == _rest_id:
                if len(_union_rows) == 0:
                    _union_rows.append(_row)

                _union_rows.append(row)

            else:

                if len(_union_rows) > 0:
                    update_member_id_dict(_union_rows)

                _union_rows = []

            _row = row
            _rest_id = rest_id

        if len(_union_rows) > 0:
            update_member_id_dict(_union_rows)

        if len(member_id_dict) > 0:
            for row in lp:
                try:

                    index_id = row[index_id_col]
                    member_logic_code = row[member_logic_code_col]
                    if member_logic_code == 'AND':
                        continue

                    if index_id in member_id_dict:
                        row[member_id_col] = member_id_dict[index_id]

                except IndexError:
                    pass

        def concat_all_val(row):
            return str(row[chain_id_1_col]) + str(row[seq_id_1_col]) + str(row[comp_id_1_col]) + str(row[atom_id_1_col])\
                + str(row[chain_id_2_col]) + str(row[seq_id_2_col]) + str(row[comp_id_2_col]) + str(row[atom_id_2_col])\
                + concat_target_val(row)

        len_data = len(lp)

        try:

            for idx, row in enumerate(lp, start=1):
                if row[member_logic_code_col] != 'OR':
                    continue
                if idx - 2 > 0:
                    _row = lp.data[idx - 2]
                    if concat_all_val(row) == concat_all_val(_row):
                        row[member_logic_code_col] = '.'
                if idx < len_data:
                    _row = lp.data[idx]
                    if concat_all_val(row) == concat_all_val(_row):
                        row[member_logic_code_col] = '.'

        except IndexError:
            pass

        try:

            del sf_item['saveframe'][loop]

            sf_item['saveframe'].add_loop(lp)
            sf_item['loop'] = lp

            return True

        except ValueError:
            return False

    def updateTorsionAngleConstIdInMrStr(self, sf_item: dict) -> bool:  # pylint: disable=no-self-use
        """ Update _Torsion_angle_constraint.ID in NMR-STAR restraint file.
        """

        loop = sf_item['loop']

        lp = pynmrstar.Loop.from_scratch(loop.category)

        lp.add_tag(loop.tags)

        id_col = loop.tags.index('ID')
        if 'Index_ID' not in loop.tags:
            tag = loop.category + '.Index_ID'
            for idx in range(len(loop)):
                loop.data[idx].append(idx + 1)
            loop.add_tag(tag)
            lp.add_tag(tag)
        if 'Combination_ID' not in loop.tags:
            tag = loop.category + '.Combination_ID'
            loop.add_tag(tag, update_data=True)
            lp.add_tag(tag)

        index_id_col = loop.tags.index('Index_ID')
        combination_id_col = loop.tags.index('Combination_ID')

        chain_id_1_col = loop.tags.index('Auth_asym_ID_1')
        seq_id_1_col = loop.tags.index('Auth_seq_ID_1')
        atom_id_1_col = loop.tags.index('Auth_atom_ID_1')

        chain_id_2_col = loop.tags.index('Auth_asym_ID_2')
        seq_id_2_col = loop.tags.index('Auth_seq_ID_2')
        atom_id_2_col = loop.tags.index('Auth_atom_ID_2')

        chain_id_3_col = loop.tags.index('Auth_asym_ID_3')
        seq_id_3_col = loop.tags.index('Auth_seq_ID_3')
        atom_id_3_col = loop.tags.index('Auth_atom_ID_3')

        chain_id_4_col = loop.tags.index('Auth_asym_ID_4')
        seq_id_4_col = loop.tags.index('Auth_seq_ID_4')
        atom_id_4_col = loop.tags.index('Auth_atom_ID_4')

        target_val_col = loop.tags.index('Angle_target_val') if 'Angle_target_val' in loop.tags else -1
        target_val_err_col = loop.tags.index('Angle_target_val_err') if 'Angle_target_val_err' in loop.tags else -1
        lower_linear_limit_col = loop.tags.index('Angle_lower_linear_limit') if 'Angle_lower_linear_limit' in loop.tags else -1
        upper_linear_limit_col = loop.tags.index('Angle_upper_linear_limit') if 'Angle_upper_linear_limit' in loop.tags else -1
        lower_limit_col = loop.tags.index('Angle_lower_bound_val') if 'Angle_lower_bound_val' in loop.tags else -1
        upper_limit_col = loop.tags.index('Angle_upper_bound_val') if 'Angle_upper_bound_val' in loop.tags else -1
        weight_col = loop.tags.index('Weight') if 'Weight' in loop.tags else -1

        modified = False

        sf_item['id'] = 0
        sf_item['index_id'] = 0

        len_loop = len(loop)

        proc_row = [False] * len_loop

        for idx, row in enumerate(loop):

            if proc_row[idx]:
                continue

            _row = row

            sf_item['id'] += 1
            sf_item['index_id'] += 1

            try:
                combination_id = row[combination_id_col]
            except IndexError:
                combination_id = None

            if combination_id not in emptyValue and str(combination_id) != '1':
                sf_item['id'] -= 1

            _row[id_col] = sf_item['id']
            try:
                _row[index_id_col] = sf_item['index_id']
            except IndexError:
                while index_id_col >= len(_row):
                    _row.append(None)
                _row[index_id_col] = sf_item['index_id']

            try:
                key = _row[chain_id_1_col] + str(_row[seq_id_1_col]) + _row[atom_id_1_col]\
                    + _row[chain_id_2_col] + str(_row[seq_id_2_col]) + _row[atom_id_2_col]\
                    + _row[chain_id_3_col] + str(_row[seq_id_3_col]) + _row[atom_id_3_col]\
                    + _row[chain_id_4_col] + str(_row[seq_id_4_col]) + _row[atom_id_4_col]
                values = (str(_row[target_val_col]) if target_val_col != -1 else '')\
                    + (str(_row[target_val_err_col]) if target_val_err_col != -1 else '')\
                    + (str(_row[lower_linear_limit_col]) if lower_linear_limit_col != -1 else '')\
                    + (str(_row[upper_linear_limit_col]) if upper_linear_limit_col != -1 else '')\
                    + (str(_row[lower_limit_col]) if lower_limit_col != -1 else '')\
                    + (str(_row[upper_limit_col]) if upper_limit_col != -1 else '')\
                    + (str(_row[weight_col]) if weight_col != -1 else '')
            except TypeError:
                return False

            if combination_id in emptyValue and idx + 1 < len_loop:
                combination_id = 1

                for idx2 in range(idx + 1, len_loop):

                    if proc_row[idx2]:
                        continue

                    _row_ = loop.data[idx2]

                    try:
                        _key = _row_[chain_id_1_col] + str(_row_[seq_id_1_col]) + _row_[atom_id_1_col]\
                            + _row_[chain_id_2_col] + str(_row_[seq_id_2_col]) + _row_[atom_id_2_col]\
                            + _row_[chain_id_3_col] + str(_row_[seq_id_3_col]) + _row_[atom_id_3_col]\
                            + _row_[chain_id_4_col] + str(_row_[seq_id_4_col]) + _row_[atom_id_4_col]
                        _values = (str(_row_[target_val_col]) if target_val_col != -1 else '')\
                            + (str(_row_[target_val_err_col]) if target_val_err_col != -1 else '')\
                            + (str(_row_[lower_linear_limit_col]) if lower_linear_limit_col != -1 else '')\
                            + (str(_row_[upper_linear_limit_col]) if upper_linear_limit_col != -1 else '')\
                            + (str(_row_[lower_limit_col]) if lower_limit_col != -1 else '')\
                            + (str(_row_[upper_limit_col]) if upper_limit_col != -1 else '')\
                            + (str(_row_[weight_col]) if weight_col != -1 else '')
                    except TypeError:
                        return False

                    if key == _key:
                        modified = True

                        if values == _values:
                            proc_row[idx2] = True
                            continue

                        if combination_id == 1:
                            try:
                                _row[combination_id_col] = combination_id
                            except IndexError:
                                while combination_id_col >= len(_row):
                                    _row.append(None)
                                _row[combination_id_col] = combination_id
                            lp.add_data(_row)

                        sf_item['index_id'] += 1
                        combination_id += 1

                        _row_[id_col] = sf_item['id']
                        try:
                            _row_[index_id_col] = sf_item['index_id']
                        except IndexError:
                            while index_id_col >= len(_row_):
                                _row_.append(None)
                            _row_[index_id_col] = sf_item['index_id']
                        try:
                            _row_[combination_id_col] = combination_id
                        except IndexError:
                            while combination_id_col >= len(_row_):
                                _row_.append(None)
                            _row_[combination_id_col] = combination_id

                        lp.add_data(_row_)

                        proc_row[idx2] = True

                if combination_id == 1:
                    lp.add_data(_row)

            else:
                lp.add_data(_row)

        if not modified:
            return True

        try:

            del sf_item['saveframe'][loop]

            sf_item['saveframe'].add_loop(lp)
            sf_item['loop'] = lp

            return True

        except ValueError:
            return False

    def validateAtomNomenclature(self, file_name: str, file_type: str, content_subtype: str,
                                 sf: Union[pynmrstar.Saveframe, pynmrstar.Loop],
                                 sf_framecode: str, lp_category: str):  # , first_comp_ids):
        """ Validate atom nomenclature using NEFTranslator and CCD.
        """

        try:

            if file_type == 'nef':  # DAOTHER-7389, issue #3, allow empty for 'chem_shift'
                pairs = self.__nefT.get_nef_comp_atom_pair(sf, lp_category,
                                                           allow_empty=content_subtype in ('chem_shift', 'spectral_peak'))[0]
            else:  # DAOTHER-7389, issue #3, allow empty for 'chem_shift'
                pairs = self.__nefT.get_star_comp_atom_pair(sf, lp_category,
                                                            allow_empty=content_subtype in ('chem_shift', 'spectral_peak'))[0]

            for pair in pairs:
                comp_id = pair['comp_id']
                atom_ids = pair['atom_id']

                # standard residue
                if comp_id in monDict3:

                    if file_type == 'nef':

                        _atom_ids = []
                        for atom_id in atom_ids:

                            if atom_id in emptyValue:
                                continue

                            _atom_id = self.__nefT.get_star_atom(comp_id, atom_id, leave_unmatched=False)[0]

                            if len(_atom_id) == 0:

                                if self.__nonblk_bad_nterm and self.__csStat.peptideLike(comp_id)\
                                   and atom_id in ('H1', 'H2', 'H3', 'HT1', 'HT2', 'HT3'):  # and comp_id in first_comp_ids:
                                    continue

                                if self.__remediation_mode and atom_id[0] in ('Q', 'M'):  # DAOTHER-8663, 8751
                                    continue

                                if self.__remediation_mode and self.__csStat.getTypeOfCompId(comp_id)[1]\
                                   and atom_id == "HO5'":
                                    continue

                                err = f"Invalid atom name {atom_id!r} (comp_id {comp_id!r}) in a loop {lp_category}."

                                self.report.error.appendDescription('invalid_atom_nomenclature',
                                                                    {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                     'description': err})
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write(f"+{self.__class_name__}.validateAtomNomenclature() ++ Error  - {err}\n")

                            else:
                                _atom_ids.extend(_atom_id)

                        atom_ids = sorted(set(_atom_ids))

                    for atom_id in atom_ids:

                        if atom_id in emptyValue:
                            continue

                        if self.__remediation_mode and atom_id[0] in ('Q', 'M'):  # DAOTHER-8663, 8751
                            continue

                        if self.__csStat.peptideLike(comp_id):
                            if atom_id.upper() == 'HN':
                                self.__fixAtomNomenclature(comp_id, {atom_id: 'H'})
                                continue
                            if atom_id.upper() == 'CO':
                                self.__fixAtomNomenclature(comp_id, {atom_id: 'C'})
                                continue

                            _atom_id = self.__nefT.get_star_atom(comp_id, translateToStdAtomName(atom_id, comp_id, ccU=self.__ccU), leave_unmatched=False)[0]
                            if len(_atom_id) == 1 and atom_id != _atom_id[0]:
                                self.__fixAtomNomenclature(comp_id, {atom_id: _atom_id[0]})
                                continue

                        elif len(atom_id) > 2 and atom_id.endswith('"') and atom_id[-2].isdigit():  # 7zew, 7zex: H5" -> H5''
                            self.__fixAtomNomenclature(comp_id, {atom_id: atom_id[:-1] + "''"})
                            continue

                        atom_id_ = atom_id

                        if (file_type == 'nef' or not self.__combined_mode or self.__transl_pseudo_name) and self.isNmrAtomName(comp_id, atom_id):
                            atom_id_ = self.getRepAtomId(comp_id, atom_id)

                            if file_type == 'nmr-star' and self.__combined_mode and self.__transl_pseudo_name and atom_id != atom_id_\
                               and not content_subtype.startswith('spectral_peak'):

                                warn = f"Conventional psuedo atom {comp_id}:{atom_id} is translated to {atom_id_!r} "\
                                    "according to the IUPAC atom nomenclature."

                                self.report.warning.appendDescription('auth_atom_nomenclature_mismatch',
                                                                      {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                       'description': warn})
                                self.report.setWarning()

                                if self.__verbose:
                                    self.__lfh.write(f"+{self.__class_name__}.validateAtomNomenclature() ++ Warning  - {warn}\n")

                                self.__fixAtomNomenclature(comp_id, {atom_id: atom_id_})

                        if not self.__nefT.validate_comp_atom(comp_id, atom_id_):

                            if self.__csStat.peptideLike(comp_id) and atom_id_.startswith('H') and atom_id_.endswith('1')\
                               and self.__nefT.validate_comp_atom(comp_id, atom_id_[:-1] + '2') and self.__nefT.validate_comp_atom(comp_id, atom_id_[:-1] + '3')\
                               and not content_subtype.startswith('spectral_peak'):

                                _atom_id_ = atom_id_[:-1]
                                _atom_id_1 = _atom_id_ + '1'
                                _atom_id_2 = _atom_id_ + '2'
                                _atom_id_3 = _atom_id_ + '3'

                                warn = f"{comp_id}:{_atom_id_1}/{_atom_id_2} should be {comp_id}:{_atom_id_3}/{_atom_id_2} "\
                                    "according to the IUPAC atom nomenclature, respectively."

                                self.report.warning.appendDescription('auth_atom_nomenclature_mismatch',
                                                                      {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                       'description': warn})
                                self.report.setWarning()

                                if self.__verbose:
                                    self.__lfh.write(f"+{self.__class_name__}.validateAtomNomenclature() ++ Warning  - {warn}\n")

                                # @see: https://bmrb.io/ref_info/atom_nom.tbl
                                self.__fixAtomNomenclature(comp_id, {_atom_id_1: _atom_id_3})

                            elif self.__nonblk_bad_nterm and self.__csStat.peptideLike(comp_id)\
                                    and atom_id in ('H1', 'H2', 'H3', 'HT1', 'HT2', 'HT3'):  # and comp_id in first_comp_ids:
                                pass

                            elif self.__remediation_mode and atom_id[0] in ('Q', 'M'):  # DAOTHER-8663, 8751
                                pass

                            elif self.__remediation_mode and self.__csStat.getTypeOfCompId(comp_id)[1]\
                                    and atom_id == "HO5'":
                                pass

                            else:
                                is_valid, cc_name, cc_rel_status = self.getChemCompNameAndStatusOf(comp_id)

                                if is_valid:
                                    if cc_rel_status != 'REL':
                                        cc_name = f"(Not available due to CCD status code {cc_rel_status})"
                                cc_name = '' if cc_name is None else ', ' + cc_name

                                if content_subtype.startswith('spectral_peak') or (self.__csStat.peptideLike(comp_id)
                                                                                   and atom_id in ('H1', 'H2', 'H3', 'HT1', 'HT2', 'HT3')):

                                    err = f"Unmatched atom name {atom_id!r} (comp_id {comp_id!r}{cc_name}) in a loop {lp_category}."

                                    self.report.warning.appendDescription('atom_nomenclature_mismatch',
                                                                          {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                           'description': err})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.validateAtomNomenclature() ++ Warning  - {err}\n")

                                else:

                                    err = f"Invalid atom name {atom_id!r} (comp_id {comp_id!r}{cc_name}) in a loop {lp_category}."

                                    if self.__remediation_mode and len(self.getAtomIdListInXplor(comp_id, atom_id)) > 0:

                                        self.report.warning.appendDescription('atom_nomenclature_mismatch',
                                                                              {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                               'description': err})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.validateAtomNomenclature() ++ Warning  - {err}\n")

                                    else:

                                        self.report.error.appendDescription('invalid_atom_nomenclature',
                                                                            {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                             'description': err})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.validateAtomNomenclature() ++ Error  - {err}\n")

                # non-standard residue
                else:

                    if self.__ccU.updateChemCompDict(comp_id):  # matches with comp_id in CCD

                        ref_atom_ids = [a[self.__ccU.ccaAtomId] for a in self.__ccU.lastAtomList]  # if a[self.__ccU.ccaLeavingAtomFlag] != 'Y']
                        unk_atom_ids = []

                        for atom_id in atom_ids:

                            if atom_id in emptyValue:
                                continue

                            if file_type == 'nef':
                                _atom_id = self.__nefT.get_star_atom(comp_id, atom_id, leave_unmatched=False)[0]
                                if len(_atom_id) > 0:
                                    atom_id = _atom_id[0]

                            if atom_id not in ref_atom_ids:

                                if self.__remediation_mode and atom_id[0] in ('Q', 'M'):  # DAOTHER-8663, 8751
                                    continue

                                unk_atom_ids.append(atom_id)

                        if len(unk_atom_ids) > 0:
                            is_valid, cc_name, cc_rel_status = self.getChemCompNameAndStatusOf(comp_id)

                            if is_valid:
                                if cc_rel_status != 'REL':
                                    cc_name = f"(Not available due to CCD status code {cc_rel_status})"
                            cc_name = '' if cc_name is None else ', ' + cc_name

                            warn = f"Unknown atom_id {unk_atom_ids!r} (comp_id {comp_id!r}{cc_name})."

                            self.report.warning.appendDescription('atom_nomenclature_mismatch',
                                                                  {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                   'description': warn})
                            self.report.setWarning()

                            if self.__verbose:
                                self.__lfh.write(f"+{self.__class_name__}.validateAtomNomenclature() ++ Warning  - {warn}\n")

                        ref_elems = set(a[self.__ccU.ccaTypeSymbol] for a in self.__ccU.lastAtomList if a[self.__ccU.ccaLeavingAtomFlag] != 'Y')

                        for elem in ref_elems:
                            if elem in PARAMAGNETIC_ELEMENTS or elem in FERROMAGNETIC_ELEMENTS:
                                self.report.setDiamagnetic(False)
                                break

                        for atom_id in atom_ids:

                            if atom_id in emptyValue:
                                continue

                            if self.__remediation_mode and atom_id[0] in ('Q', 'M'):  # DAOTHER-8663, 8751
                                continue

                            if self.__csStat.peptideLike(comp_id):
                                if atom_id.upper() == 'HN':
                                    self.__fixAtomNomenclature(comp_id, {atom_id: 'H'})
                                    continue
                                if atom_id.upper() == 'CO':
                                    self.__fixAtomNomenclature(comp_id, {atom_id: 'C'})
                                    continue

                            elif len(atom_id) > 2 and atom_id.endswith('"') and atom_id[-2].isdigit():  # 7zew, 7zex: H5" -> H5''
                                self.__fixAtomNomenclature(comp_id, {atom_id: atom_id[:-1] + "''"})
                                continue

                            atom_id_ = atom_id

                            if (file_type == 'nef' or not self.__combined_mode or self.__transl_pseudo_name) and self.isNmrAtomName(comp_id, atom_id)\
                               and not content_subtype.startswith('spectral_peak'):
                                atom_id_ = self.getRepAtomId(comp_id, atom_id)

                                if file_type == 'nmr-star' and self.__combined_mode and self.__transl_pseudo_name and atom_id != atom_id_:

                                    warn = f"Conventional psuedo atom {comp_id}:{atom_id} is translated to {atom_id_!r} "\
                                        "according to the IUPAC atom nomenclature."

                                    self.report.warning.appendDescription('auth_atom_nomenclature_mismatch',
                                                                          {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                           'description': warn})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.validateAtomNomenclature() ++ Warning  - {warn}\n")

                                    self.__fixAtomNomenclature(comp_id, {atom_id: atom_id_})

                    else:
                        pass

            if file_type == 'nmr-star':

                try:

                    peptide_only = all(len(pair['comp_id']) == 3 and pair['comp_id'] in monDict3 for pair in pairs)

                    auth_pairs = self.__nefT.get_star_auth_comp_atom_pair(sf, lp_category)[0]

                    for auth_pair in auth_pairs:
                        auth_comp_id = auth_pair['comp_id']
                        if peptide_only and len(auth_comp_id) == 1:
                            comp_id = next((k for k, v in monDict3.items() if v == auth_comp_id), auth_comp_id)
                        else:
                            comp_id = auth_comp_id
                        comp_id = translateToStdResName(comp_id, ccU=self.__ccU)
                        auth_atom_ids = auth_pair['atom_id']

                        # standard residue
                        if comp_id in monDict3:

                            self.__ccU.updateChemCompDict(comp_id)
                            ref_atom_ids = [a[self.__ccU.ccaAtomId] for a in self.__ccU.lastAtomList]

                            _auth_atom_ids = []
                            for auth_atom_id in auth_atom_ids:

                                if auth_atom_id in emptyValue:
                                    continue

                                _auth_atom_id = translateToStdAtomName(auth_atom_id, comp_id, ref_atom_ids, ccU=self.__ccU)

                                auth_atom_ids = self.getAtomIdList(comp_id, _auth_atom_id)

                                if len(auth_atom_ids) > 0:
                                    _auth_atom_ids.extend(auth_atom_ids)

                                else:

                                    if self.__nonblk_bad_nterm and self.__csStat.peptideLike(comp_id)\
                                       and _auth_atom_id in ('H1', 'H2', 'H3', 'HT1', 'HT2', 'HT3'):  # and comp_id in first_comp_ids:
                                        continue

                                    if self.__remediation_mode and _auth_atom_id[0] in ('Q', 'M'):  # DAOTHER-8663, 8751
                                        continue

                                    if self.__remediation_mode and self.__csStat.getTypeOfCompId(comp_id)[1]\
                                       and atom_id == "HO5'":
                                        continue

                                    auth_atom_ids = self.getAtomIdListInXplor(comp_id, _auth_atom_id)

                                    if len(auth_atom_ids) > 0:
                                        _auth_atom_ids.extend(auth_atom_ids)

                                    else:

                                        warn = f"Unmatched Auth_atom_ID {auth_atom_id!r} (Auth_comp_ID {auth_comp_id})."

                                        self.report.warning.appendDescription('auth_atom_nomenclature_mismatch',
                                                                              {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                               'description': warn})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.validateAtomNomenclature() ++ Warning  - {warn}\n")

                            auth_atom_ids = sorted(set(_auth_atom_ids))

                            for auth_atom_id in auth_atom_ids:

                                if auth_atom_id in emptyValue:
                                    continue

                                if not self.__nefT.validate_comp_atom(comp_id,
                                                                      translateToStdAtomName(auth_atom_id, comp_id, ref_atom_ids, ccU=self.__ccU)):

                                    if self.__nonblk_bad_nterm and self.__csStat.peptideLike(comp_id)\
                                       and auth_atom_id in ('H1', 'H2', 'H3', 'HT1', 'HT2', 'HT3'):  # and comp_id in first_comp_ids:
                                        continue

                                    if self.__remediation_mode and auth_atom_id[0] in ('Q', 'M'):  # DAOTHER-8663, 8751
                                        continue

                                    if self.__remediation_mode and self.__csStat.getTypeOfCompId(comp_id)[1]\
                                       and atom_id == "HO5'":
                                        continue

                                    warn = f"Unmatched Auth_atom_ID {auth_atom_id!r} (Auth_comp_ID {auth_comp_id})."

                                    self.report.warning.appendDescription('auth_atom_nomenclature_mismatch',
                                                                          {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                           'description': warn})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.validateAtomNomenclature() ++ Warning  - {warn}\n")

                        # non-standard residue
                        else:
                            has_comp_id = False

                            for pair in pairs:

                                if pair['comp_id'] != comp_id:
                                    continue

                                has_comp_id = True

                                atom_ids = pair['atom_id']

                                if (set(auth_atom_ids) | set(atom_ids)) != set(atom_ids):

                                    for auth_atom_id in (set(auth_atom_ids) | set(atom_ids)) - set(atom_ids):

                                        if auth_atom_id in emptyValue:
                                            continue

                                        if self.__nonblk_bad_nterm and self.__csStat.peptideLike(comp_id)\
                                           and auth_atom_id in ('H1', 'H2', 'H3', 'HT1', 'HT2', 'HT3'):  # and comp_id in first_comp_ids:
                                            continue

                                        if self.__remediation_mode and auth_atom_id[0] in ('Q', 'M'):  # DAOTHER-8663, 8751
                                            continue

                                        if self.__remediation_mode and self.__csStat.getTypeOfCompId(comp_id)[1]\
                                           and atom_id == "HO5'":
                                            continue

                                        warn = f"Unmatched Auth_atom_ID {auth_atom_id!r} (Auth_comp_ID {comp_id}, non-standard residue)."

                                        self.report.warning.appendDescription('auth_atom_nomenclature_mismatch',
                                                                              {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                               'description': warn})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.validateAtomNomenclature() ++ Warning  - {warn}\n")

                                break

                            if not has_comp_id:

                                for auth_atom_id in auth_atom_ids:

                                    if auth_atom_id in emptyValue:
                                        continue

                                    if self.__nonblk_bad_nterm and self.__csStat.peptideLike(comp_id)\
                                       and auth_atom_id in ('H1', 'H2', 'H3', 'HT1', 'HT2', 'HT3'):  # and comp_id in first_comp_ids:
                                        continue

                                    if self.__remediation_mode and auth_atom_id[0] in ('Q', 'M'):  # DAOTHER-8663, 8751
                                        continue

                                    if self.__remediation_mode and self.__csStat.getTypeOfCompId(comp_id)[1]\
                                       and atom_id == "HO5'":
                                        continue

                                    warn = f"Unmatched Auth_atom_ID {auth_atom_id!r} (Auth_comp_ID {comp_id}, non-standard residue)."

                                    self.report.warning.appendDescription('auth_atom_nomenclature_mismatch',
                                                                          {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                           'description': warn})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.validateAtomNomenclature() ++ Warning  - {warn}\n")

                except LookupError:
                    # """
                    # self.report.error.appendDescription('missing_mandatory_item',
                    #                                     {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                    #                                      'description': str(e).strip("'")})
                    # self.report.setError()

                    # self.__lfh.write(f"+{self.__class_name__}.validateAtomNomenclature() ++ LookupError  - "
                    #                  f"{file_name} {sf_framecode} {lp_category} {str(e)}\n")
                    # """
                    pass

                except ValueError as e:

                    self.report.error.appendDescription('invalid_data',
                                                        {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                         'description': str(e).strip("'")})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write(f"+{self.__class_name__}.validateAtomNomenclature() ++ ValueError  - {str(e)}\n")

                except UserWarning as e:

                    errs = str(e).strip("'").split('\n')

                    for err in errs:

                        if len(err) == 0:
                            continue

                        if err.startswith('[Invalid data]'):

                            p = err.index(']') + 2
                            err = err[p:]

                            self.report.error.appendDescription('invalid_data',
                                                                {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                 'description': err})
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write(f"+{self.__class_name__}.validateAtomNomenclature() ++ ValueError  - {err}\n")

                        else:

                            self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.validateAtomNomenclature() ++ Error  - " + err)
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write(f"+{self.__class_name__}.validateAtomNomenclature() ++ Error  - {err}\n")

                except Exception as e:

                    self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.validateAtomNomenclature() ++ Error  - " + str(e))
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write(f"+{self.__class_name__}.validateAtomNomenclature() ++ Error  - {str(e)}\n")

        except LookupError as e:

            self.report.error.appendDescription('missing_mandatory_item',
                                                {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                 'description': str(e).strip("'")})
            self.report.setError()

            self.__lfh.write(f"+{self.__class_name__}.validateAtomNomenclature() ++ LookupError  - "
                             f"{file_name} {sf_framecode} {lp_category} {str(e)}\n")

        except ValueError as e:

            self.report.error.appendDescription('invalid_data',
                                                {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                 'description': str(e).strip("'")})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write(f"+{self.__class_name__}.validateAtomNomenclature() ++ ValueError  - {str(e)}\n")

        except UserWarning as e:

            errs = str(e).strip("'").split('\n')

            for err in errs:

                if len(err) == 0:
                    continue

                if err.startswith('[Invalid data]'):

                    p = err.index(']') + 2
                    err = err[p:]

                    self.report.error.appendDescription('invalid_data',
                                                        {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                         'description': err})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write(f"+{self.__class_name__}.validateAtomNomenclature() ++ ValueError  - {err}\n")

                else:

                    self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.validateAtomNomenclature() ++ Error  - " + err)
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write(f"+{self.__class_name__}.validateAtomNomenclature() ++ Error  - {err}\n")

        except Exception as e:

            self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.validateAtomNomenclature() ++ Error  - " + str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write(f"+{self.__class_name__}.validateAtomNomenclature() ++ Error  - {str(e)}\n")

    def validateAtomTypeOfCsLoop(self, file_name: str, file_type: str,
                                 sf: Union[pynmrstar.Saveframe, pynmrstar.Loop],
                                 sf_framecode: str, lp_category: str):
        """ Validate atom type, isotope number on assigned chemical shifts.
        """

        if not self.__combined_mode:
            return

        try:

            # DAOTHER-7389, issue #3, allow empty for 'chem_shift'
            if file_type == 'nef':
                a_types = self.__nefT.get_nef_atom_type_from_cs_loop(sf, allow_empty=True)[0]
            else:
                a_types = self.__nefT.get_star_atom_type_from_cs_loop(sf, allow_empty=True)[0]

            for a_type in a_types:
                atom_type = a_type['atom_type']
                isotope_nums = a_type['isotope_number']
                atom_ids = a_type['atom_id']

                if atom_type not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS.keys():

                    err = f"Invalid atom_type {atom_type!r} in a loop {lp_category}."

                    self.report.error.appendDescription('invalid_atom_type',
                                                        {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                         'description': err})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write(f"+{self.__class_name__}.validateAtomTypeOfCsLoop() ++ Error  - {err}\n")

                else:

                    for isotope_num in isotope_nums:
                        if isotope_num not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS[atom_type]:

                            err = f"Invalid isotope number {str(isotope_num)!r} (atom_type {atom_type}, "\
                                f"allowed isotope number {ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS[atom_type]}) in a loop {lp_category}."

                            self.report.error.appendDescription('invalid_isotope_number',
                                                                {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                 'description': err})
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write(f"+{self.__class_name__}.validateAtomTypeOfCsLoop() ++ Error  - {err}\n")

                    for atom_id in atom_ids:
                        if not atom_id.startswith(atom_type):

                            if self.__remediation_mode and 1 in isotope_nums and atom_id[0] in pseProBeginCode:  # DAOTHER-8663, 8751, 9520
                                continue

                            err = f"Invalid atom name {atom_id!r} (atom_type {atom_type!r}) in a loop {lp_category}."

                            self.report.error.appendDescription('invalid_atom_nomenclature',
                                                                {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                 'description': err})
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write(f"+{self.__class_name__}.validateAtomTypeOfCsLoop() ++ Error  - {err}\n")

        except LookupError as e:

            if not self.__resolve_conflict:
                self.report.error.appendDescription('missing_mandatory_item',
                                                    {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                     'description': str(e).strip("'")})
                self.report.setError()

                self.__lfh.write(f"+{self.__class_name__}.validateAtomTypeOfCsLoop() ++ LookupError  - "
                                 f"{file_name} {sf_framecode} {lp_category} {str(e)}\n")

        except ValueError as e:

            self.report.error.appendDescription('invalid_data',
                                                {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                 'description': str(e).strip("'")})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write(f"+{self.__class_name__}.validateAtomTypeOfCsLoop() ++ ValueError  - {str(e)}\n")

        except UserWarning as e:

            errs = str(e).strip("'").split('\n')

            for err in errs:

                if len(err) == 0:
                    continue

                if err.startswith('[Invalid data]'):

                    p = err.index(']') + 2
                    err = err[p:]

                    self.report.error.appendDescription('invalid_data',
                                                        {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                         'description': err})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write(f"+{self.__class_name__}.validateAtomTypeOfCsLoop() ++ ValueError  - {err}\n")

                else:

                    self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.validateAtomTypeOfCsLoop() ++ Error  - " + err)
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write(f"+{self.__class_name__}.validateAtomTypeOfCsLoop() ++ Error  - {err}\n")

        except Exception as e:

            self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.validateAtomTypeOfCsLoop() ++ Error  - " + str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write(f"+{self.__class_name__}.validateAtomTypeOfCsLoop() ++ Error  - {str(e)}\n")

    def validateAmbigCodeOfCsLoop(self, file_name: str,
                                  sf: Union[pynmrstar.Saveframe, pynmrstar.Loop],
                                  sf_framecode: str, lp_category: str) -> bool:
        """ Validate ambiguity code on assigned chemical shifts.
        """

        try:

            need_set_id = False
            valid = True

            a_codes = self.__nefT.get_star_ambig_code_from_cs_loop(sf)[0]

            comp_ids_wo_ambig_code = []

            for a_code in a_codes:
                comp_id = a_code['comp_id']
                ambig_code = a_code['ambig_code']
                atom_ids = a_code['atom_id']

                if ambig_code is None:
                    comp_ids_wo_ambig_code.append(comp_id)

                elif ambig_code == 1 or ambig_code >= 4:
                    need_set_id |= ambig_code in (4, 5, 6, 9)

                # ambig_code is 2 (geminal atoms) or 3 (aromatic ring atoms in opposite side)
                else:

                    for atom_id in atom_ids:

                        _atom_id = atom_id

                        if self.isNmrAtomName(comp_id, atom_id):
                            _atom_id = self.getRepAtomId(comp_id, atom_id)

                        allowed_ambig_code = self.__csStat.getMaxAmbigCodeWoSetId(comp_id, _atom_id)

                        if ambig_code > allowed_ambig_code > 0:

                            if allowed_ambig_code < 1:

                                if self.__remediation_mode:
                                    pass

                                else:

                                    warn = f"Ambiguity code {str(ambig_code)!r} (comp_id {comp_id}, atom_id {atom_id}) "\
                                        "should be '1' according to the BMRB definition."

                                    self.report.warning.appendDescription('ambiguity_code_mismatch',
                                                                          {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                           'description': warn})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.validateAmbigCodeOfCsLoop() ++ Warning  - {warn}\n")

                                    valid = False

                            else:

                                if self.__remediation_mode:
                                    pass

                                else:

                                    err = f"Invalid ambiguity code {str(ambig_code)!r} (comp_id {comp_id}, atom_id {atom_id}, "\
                                        f"allowed ambig_code {[1, allowed_ambig_code, 4, 5, 6, 9]}) in a loop {lp_category}."

                                    self.report.error.appendDescription('invalid_ambiguity_code',
                                                                        {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                         'description': err})
                                    self.report.setError()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.validateAmbigCodeOfCsLoop() ++ Error  - {err}\n")

                                    valid = False

            if len(comp_ids_wo_ambig_code) > 0:

                warn = f"Missing ambiguity code for the following residues {comp_ids_wo_ambig_code}."

                self.report.warning.appendDescription('missing_data',
                                                      {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                       'description': warn})
                self.report.setWarning()

                if self.__verbose:
                    self.__lfh.write(f"+{self.__class_name__}.validateAmbigCodeOfCsLoop() ++ Warning  - {warn}\n")

                valid = False

            if need_set_id and valid:

                list_id = get_first_sf_tag(sf, 'ID')

                try:

                    lp = sf.get_loop(lp_category)

                    ambig_code_col = lp.tags.index('Ambiguity_code')
                    ambig_set_id_col = lp.tags.index('Ambiguity_set_ID')

                    id_col = lp.tags.index('ID')
                    chain_id_col = lp.tags.index('Entity_assembly_ID')
                    seq_id_col = lp.tags.index('Comp_index_ID')
                    atom_type_col = lp.tags.index('Atom_type')

                    aux_lp_category = AUX_LP_CATEGORIES['nmr-star']['chem_shift'][0]

                    if any(True for aux_loop in sf if aux_loop.category == aux_lp_category):

                        aux_loop = sf.get_loop(aux_lp_category)

                        del sf[aux_loop]

                    aux_lp = pynmrstar.Loop.from_scratch(aux_lp_category)

                    aux_items = ['Ambiguous_shift_set_ID', 'Atom_chem_shift_ID', 'Entry_ID', 'Assigned_chem_shift_list_ID']

                    aux_tags = [aux_lp_category + '.' + item for item in aux_items]

                    aux_lp.add_tag(aux_tags)

                    inter_residue_seq_id = {}

                    for _row in lp:

                        ambig_code = _row[ambig_code_col]

                        if ambig_code in emptyValue:
                            continue

                        if isinstance(ambig_code, str):
                            ambig_code = int(ambig_code)

                        if ambig_code not in (5, 6, 9):
                            continue

                        chain_id = _row[chain_id_col]
                        seq_id = _row[seq_id_col]

                        if chain_id not in inter_residue_seq_id:
                            inter_residue_seq_id[chain_id] = set()

                        inter_residue_seq_id[chain_id].add(seq_id)

                    aux_index_id = 0
                    ambig_shift_set_id = {}

                    for _idx, _row in enumerate(lp):

                        ambig_code = _row[ambig_code_col]

                        if ambig_code in emptyValue:
                            continue

                        if isinstance(ambig_code, str):
                            ambig_code = int(ambig_code)

                        if ambig_code not in (4, 5):
                            continue

                        chain_id = _row[chain_id_col]
                        seq_id = _row[seq_id_col]
                        atom_type = _row[atom_type_col]

                        if ambig_code == 4:
                            key = (chain_id, str(seq_id), atom_type, ambig_code)
                        else:
                            key = (chain_id, str(inter_residue_seq_id[chain_id]), atom_type, ambig_code)

                        if key not in ambig_shift_set_id:
                            aux_index_id += 1
                            ambig_shift_set_id[key] = aux_index_id

                        lp.data[_idx][ambig_set_id_col] = ambig_shift_set_id[key]

                        _aux_row = [None] * 4
                        _aux_row[0], _aux_row[1], _aux_row[2], _aux_row[3] =\
                            ambig_shift_set_id[key], _row[id_col], self.__entry_id, list_id

                        aux_lp.add_data(_aux_row)

                    if len(aux_lp) > 0:
                        sf.add_loop(aux_lp)
                        return True

                except (KeyError, IndexError, ValueError):
                    pass

        except LookupError as e:

            if not self.__resolve_conflict:
                self.report.error.appendDescription('missing_mandatory_item',
                                                    {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                     'description': str(e).strip("'")})
                self.report.setError()

                self.__lfh.write(f"+{self.__class_name__}.validateAmbigCodeOfCsLoop() ++ LookupError  - "
                                 f"{file_name} {sf_framecode} {lp_category} {str(e)}\n")

        except ValueError as e:

            self.report.error.appendDescription('invalid_data',
                                                {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                 'description': str(e).strip("'")})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write(f"+{self.__class_name__}.validateAmbigCodeOfCsLoop() ++ ValueError  - {str(e)}\n")

        except UserWarning as e:

            errs = str(e).strip("'").split('\n')

            for err in errs:

                if len(err) == 0:
                    continue

                if err.startswith('[Invalid data]'):

                    p = err.index(']') + 2
                    err = err[p:]

                    self.report.error.appendDescription('invalid_data',
                                                        {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                         'description': err})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write(f"+{self.__class_name__}.validateAmbigCodeOfCsLoop() ++ ValueError  - {err}\n")

                else:

                    self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.validateAmbigCodeOfCsLoop() ++ Error  - " + err)
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write(f"+{self.__class_name__}.validateAmbigCodeOfCsLoop() ++ Error  - {err}\n")

        except Exception as e:

            self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.validateAmbigCodeOfCsLoop() ++ Error  - " + str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write(f"+{self.__class_name__}.validateAmbigCodeOfCsLoop() ++ Error  - {str(e)}\n")

        return False

    def testIndexConsistency(self, file_name: str,
                             sf: Union[pynmrstar.Saveframe, pynmrstar.Loop],
                             sf_framecode: str, lp_category: str, index_tag: str):
        """ Perform consistency test on index of interesting loops.
        """

        try:

            indices = self.__nefT.get_index(sf, lp_category, index_id=index_tag)[0]

            if indices != list(range(1, len(indices) + 1)):

                warn = f"Index of loop, '{lp_category}.{index_tag}', should be ordinal numbers."

                self.report.warning.appendDescription('disordered_index',
                                                      {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                       'description': warn})
                self.report.setWarning()

                if self.__verbose:
                    self.__lfh.write(f"+{self.__class_name__}.testIndexConsistency() ++ Warning  - {warn}\n")

        except KeyError as e:

            self.report.error.appendDescription('duplicated_index',
                                                {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                 'description': str(e).strip("'")})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write(f"+{self.__class_name__}.testIndexConsistency() ++ KeyError  - {str(e)}\n")

        except LookupError:
            # """
            # self.report.error.appendDescription('missing_mandatory_item',
            #                                     {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
            #                                      'description': str(e).strip("'")})
            # self.report.setError()

            # self.__lfh.write(f"+{self.__class_name__}.testIndexConsistency() ++ LookupError  - "
            #                  f"{file_name} {sf_framecode} {lp_category} {str(e)}\n")
            # """
            pass

        except ValueError as e:

            self.report.error.appendDescription('invalid_data',
                                                {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                 'description': str(e).strip("'")})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write(f"+{self.__class_name__}.testIndexConsistency() ++ ValueError  - {str(e)}\n")

        except UserWarning as e:

            errs = str(e).strip("'").split('\n')

            for err in errs:

                if len(err) == 0:
                    continue

                if err.startswith('[Invalid data]'):

                    p = err.index(']') + 2
                    err = err[p:]

                    self.report.error.appendDescription('invalid_data',
                                                        {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                         'description': err})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write(f"+{self.__class_name__}.testIndexConsistency() ++ ValueError  - {err}\n")

                elif err.startswith('[Too big loop]'):
                    continue

                else:

                    self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.testIndexConsistency() ++ Error  - " + err)
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write(f"+{self.__class_name__}.testIndexConsistency() ++ Error  - {err}\n")

        except Exception as e:

            self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.testIndexConsistency() ++ Error  - " + str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write(f"+{self.__class_name__}.testIndexConsistency() ++ Error  - {str(e)}\n")

    def testDataConsistencyInLoop(self, file_list_id: int, file_name: str, file_type: str, content_subtype: str,
                                  sf: Union[pynmrstar.Saveframe, pynmrstar.Loop],
                                  sf_framecode: str, lp_category: str, parent_pointer: int):
        """ Perform consistency test on data of interesting loops.
        """

        allowed_tags = ALLOWED_TAGS[file_type][content_subtype]
        disallowed_tags = None

        if content_subtype == 'spectral_peak':

            try:

                _num_dim = get_first_sf_tag(sf, NUM_DIM_ITEMS[file_type])
                num_dim = int(_num_dim)

                if num_dim not in range(1, MAX_DIM_NUM_OF_SPECTRA):
                    raise ValueError()

            except ValueError:  # raised error already at testIndexConsistency()
                return

            max_dim = num_dim + 1

            key_items = []
            for dim in range(1, max_dim):
                for k in PK_KEY_ITEMS[file_type]:
                    if k['type'] == 'float':  # position
                        _k = copy.copy(k)
                        if '%s' in k['name']:
                            _k['name'] = k['name'] % dim
                        key_items.append(_k)
            for k in PK_KEY_ITEMS[file_type]:
                if k['type'] == 'positive-int':  # peak_id
                    key_items.append(k)

            data_items = []
            for d in DATA_ITEMS[file_type][content_subtype]:
                data_items.append(d)
            for dim in range(1, max_dim):
                for d in self.pk_data_items[file_type]:
                    _d = copy.copy(d)
                    if '%s' in d['name']:
                        _d['name'] = d['name'] % dim
                    if 'default-from' in d and '%s' in d['default-from']:  # DAOTHER-7421
                        _d['default-from'] = d['default-from'] % dim
                    data_items.append(_d)

            if max_dim < MAX_DIM_NUM_OF_SPECTRA:
                disallowed_tags = []
                for dim in range(max_dim, MAX_DIM_NUM_OF_SPECTRA):
                    for t in DISALLOWED_PK_TAGS[file_type]:
                        if '%s' in t:
                            t = t % dim
                        disallowed_tags.append(t)

                if self.__bmrb_only:
                    loop = sf.get_loop(lp_category)
                    disallowed_tags = list(set(loop.tags) & set(disallowed_tags))
                    loop.remove_tag(disallowed_tags)

        else:

            key_items = self.key_items[file_type][content_subtype]
            data_items = DATA_ITEMS[file_type][content_subtype]

            if file_type == 'nmr-star' and content_subtype == 'ccr_dd_restraint':
                loop = sf.get_loop(lp_category)
                if 'Dipole_2_chem_comp_index_ID_2' in loop.tags:
                    key_items = copy.copy(key_items)
                    key_item = next((key_item for key_item in key_items if key_item['name'] == 'Dipole_2_comp_index_ID_2'), None)
                    if key_item is not None:
                        key_item['name'] = 'Dipole_2_chem_comp_index_ID_2'

        lp_data = None

        try:

            lp_data = self.__nefT.check_data(sf, lp_category, key_items, data_items,
                                             allowed_tags, disallowed_tags, parent_pointer=parent_pointer,
                                             test_on_index=True, enforce_non_zero=True, enforce_sign=True, enforce_range=True, enforce_enum=True,
                                             enforce_allowed_tags=(file_type == 'nmr-star' and not self.__bmrb_only),
                                             excl_missing_data=self.__excl_missing_data)[0]

            self.__lp_data[content_subtype].append({'file_name': file_name, 'sf_framecode': sf_framecode, 'data': lp_data})

        except KeyError as e:

            self.report.error.appendDescription('multiple_data',
                                                {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                 'description': str(e).strip("'")})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write(f"+{self.__class_name__}.testDataConsistencyInLoop() ++ KeyError  - {str(e)}\n")

        except LookupError as e:

            item = 'format_issue' if 'Unauthorized' in str(e) else 'missing_mandatory_item'

            self.report.error.appendDescription(item,
                                                {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                 'description': str(e).strip("'")})
            self.report.setError()

            self.__lfh.write(f"+{self.__class_name__}.testDataConsistencyInLoop() ++ LookupError  - "
                             f"{file_name} {sf_framecode} {lp_category} {str(e)}\n")

        except ValueError as e:

            self.report.error.appendDescription('invalid_data',
                                                {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                 'description': str(e).strip("'")})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write(f"+{self.__class_name__}.testDataConsistencyInLoop() ++ ValueError  - {str(e)}\n")

        except UserWarning as e:

            warns = str(e).strip("'").split('\n')

            has_multiple_data = has_bad_pattern = False

            for warn in warns:

                if len(warn) == 0:
                    continue

                zero = warn.startswith('[Zero value error]')
                nega = warn.startswith('[Negative value error]')
                rang = warn.startswith('[Range value error]')
                enum = warn.startswith('[Enumeration error]')
                mult = warn.startswith('[Multiple data]')
                remo = warn.startswith('[Remove bad pattern]')
                clea = warn.startswith('[Clear bad pattern]')

                if zero or nega or range or enum or mult or remo or clea:

                    p = warn.index(']') + 2
                    warn = warn[p:]

                    if zero or nega or rang:
                        item = 'unusual_data'
                    elif enum:
                        item = 'enum_mismatch'
                    elif remo:
                        if content_subtype == 'chem_shift':
                            warn += ' Your unassigned chemical shifts have been removed.'
                            item = 'incompletely_assigned_chemical_shift'
                        else:
                            item = 'insufficient_data'
                        has_bad_pattern = True
                    elif clea:
                        if content_subtype == 'chem_shift':
                            warn += ' Partially assiged chemical shifts should be resolved or removed.'
                            item = 'incompletely_assigned_chemical_shift'
                        elif content_subtype.startswith('spectral_peak'):

                            if self.__remediation_mode:
                                continue

                            warn += ' Unassigned spectral peaks can be included in your peak list(s).'
                            item = 'incompletely_assigned_spectral_peak'
                        else:
                            item = 'insufficient_data'
                    elif self.__resolve_conflict:
                        item = 'redundant_data'
                        has_multiple_data = True
                    else:
                        item = 'multiple_data'

                    if zero or nega or rang or enum or remo or clea or self.__resolve_conflict:

                        self.report.warning.appendDescription(item,
                                                              {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                               'description': warn})
                        self.report.setWarning()

                        if self.__verbose:
                            self.__lfh.write(f"+{self.__class_name__}.testDataConsistencyInLoop() ++ Warning  - {warn}\n")

                    else:

                        self.report.error.appendDescription(item,
                                                            {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                             'description': warn})
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write(f"+{self.__class_name__}.testDataConsistencyInLoop() ++ KeyError  - {warn}\n")

                else:

                    self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.testDataConsistencyInLoop() ++ Error  - " + warn)
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write(f"+{self.__class_name__}.testDataConsistencyInLoop() ++ Error  - {warn}\n")

            # try to parse data without constraints
            if has_multiple_data:
                conflict_id = self.__nefT.get_conflict_id(sf, lp_category, key_items)[0]

                if len(conflict_id) > 0:
                    loop = sf if self.__star_data_type[file_list_id] == 'Loop' else sf.get_loop(lp_category)

                    for lcid in conflict_id:
                        del loop.data[lcid]

                    index_tag = INDEX_TAGS[file_type][content_subtype]
                    if index_tag is not None:
                        index_col = loop.tags.index(index_tag) if index_tag in loop.tags else -1
                        if index_col != -1:
                            for idx, row in enumerate(loop, start=1):
                                row[index_col] = idx

            # try to parse data without bad patterns
            if has_bad_pattern:
                conflict_id = self.__nefT.get_bad_pattern_id(sf, lp_category, key_items, data_items)[0]

                if len(conflict_id) > 0:
                    loop = sf if self.__star_data_type[file_list_id] == 'Loop' else sf.get_loop(lp_category)

                    for lcid in conflict_id:
                        del loop.data[lcid]

            try:

                lp_data = self.__nefT.check_data(sf, lp_category, key_items, data_items,
                                                 allowed_tags, disallowed_tags, parent_pointer=parent_pointer,
                                                 enforce_allowed_tags=(file_type == 'nmr-star' and not self.__bmrb_only),
                                                 excl_missing_data=self.__excl_missing_data)[0]

                self.__lp_data[content_subtype].append({'file_name': file_name, 'sf_framecode': sf_framecode, 'data': lp_data})

            except Exception:
                pass

        except Exception as e:

            self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.testDataConsistencyInLoop() ++ Error  - " + str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write(f"+{self.__class_name__}.__testDataConsistencyInLoop() ++ Error  - {str(e)}\n")

    def detectConflictDataInLoop(self, file_name: str, file_type: str, content_subtype: str,
                                 sf: Union[pynmrstar.Saveframe, pynmrstar.Loop],
                                 sf_framecode: str, lp_category: str):
        """ Detect redundant/inconsistent data of interesting loops.
        """

        lp_data = next((lp['data'] for lp in self.__lp_data[content_subtype]
                        if lp['file_name'] == file_name and lp['sf_framecode'] == sf_framecode), None)

        if lp_data is None or len(lp_data) == 0:
            return

        key_items = self.consist_key_items[file_type][content_subtype]

        if file_type == 'nmr-star' and content_subtype == 'ccr_dd_restraint':
            loop = sf.get_loop(lp_category)
            if 'Dipole_2_chem_comp_index_ID_2' in loop.tags:
                key_items = copy.copy(key_items)
                key_item = next((key_item for key_item in key_items if key_item['name'] == 'Dipole_2_comp_index_ID_2'), None)
                if key_item is not None:
                    key_item['name'] = 'Dipole_2_chem_comp_index_ID_2'

        conflict_id_set = self.__nefT.get_conflict_id_set(sf, lp_category, key_items)[0]

        if conflict_id_set is None:
            return

        data_items = CONSIST_DATA_ITEMS[file_type][content_subtype]
        index_tag = INDEX_TAGS[file_type][content_subtype]
        id_tag = CONSIST_ID_TAGS[file_type][content_subtype]

        data_unit_name = 'atom pair'

        if content_subtype == 'dist_restraint':
            max_inclusive = DIST_UNCERT_MAX

        elif content_subtype == 'dihed_restraint':
            max_inclusive = ANGLE_UNCERT_MAX

            data_unit_name = 'dihedral angle'

            dh_item_names = ITEM_NAMES_IN_DIHED_LOOP[file_type]
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
            lower_limit_name = dh_item_names['lower_limit']
            upper_limit_name = dh_item_names['upper_limit']

            def ext_atoms(row):
                return ({'chain_id': row[chain_id_1_name], 'seq_id': row[seq_id_1_name],
                         'comp_id': row[comp_id_1_name], 'atom_id': row[atom_id_1_name]},
                        {'chain_id': row[chain_id_2_name], 'seq_id': row[seq_id_2_name],
                         'comp_id': row[comp_id_2_name], 'atom_id': row[atom_id_2_name]},
                        {'chain_id': row[chain_id_3_name], 'seq_id': row[seq_id_3_name],
                         'comp_id': row[comp_id_3_name], 'atom_id': row[atom_id_3_name]},
                        {'chain_id': row[chain_id_4_name], 'seq_id': row[seq_id_4_name],
                         'comp_id': row[comp_id_4_name], 'atom_id': row[atom_id_4_name]})

        elif content_subtype == 'rdc_restraint':
            max_inclusive = RDC_UNCERT_MAX

            data_unit_name = 'bond vector'

        for id_set in conflict_id_set:
            len_id_set = len(id_set)

            if len_id_set < 2:
                continue

            redundant = True

            for i in range(len_id_set - 1):

                for j in range(i + 1, len_id_set):

                    try:
                        row_1 = lp_data[id_set[i]]
                        row_2 = lp_data[id_set[j]]
                    except IndexError:
                        continue

                    conflict = inconsist = False

                    discrepancy = ''

                    for d in data_items:
                        dname = d['name']

                        if dname not in row_1:
                            continue

                        val_1 = row_1[dname]
                        val_2 = row_2[dname]

                        if val_1 is None and val_2 is None:
                            continue

                        if None in (val_1, val_2):
                            redundant = False
                            continue

                        if val_1 == val_2:
                            continue

                        redundant = False

                        _val_1 = str(val_1) if val_1 >= 0.0 else '(' + str(val_1) + ')'
                        _val_2 = str(val_2) if val_2 >= 0.0 else '(' + str(val_2) + ')'

                        if content_subtype == 'dist_restraint':

                            r = abs(val_1 - val_2) / abs(val_1 + val_2)

                            if r >= R_CONFLICTED_DIST_RESTRAINT:
                                discrepancy += f"{dname} |{_val_1}-{_val_2}|/|{_val_1}+{_val_2}| = {r:.1%} is out of acceptable range, "\
                                               f"{int(R_CONFLICTED_DIST_RESTRAINT * 100)} %, "
                                conflict = True

                            elif r >= R_INCONSISTENT_DIST_RESTRAINT:
                                discrepancy += f"{dname} |{_val_1}-{_val_2}|/|{_val_1}+{_val_2}| = {r:.1%} is out of typical range, "\
                                               f"{int(R_INCONSISTENT_DIST_RESTRAINT * 100)} %, "
                                inconsist = True

                        else:

                            r = abs(val_1 - val_2)

                            if content_subtype == 'dihed_restraint':

                                if r > 180.0:
                                    if val_1 < val_2:
                                        r = abs(val_1 - (val_2 - 360.0))
                                    if val_1 > val_2:
                                        r = abs(val_1 - (val_2 + 360.0))

                                atom1, atom2, atom3, atom4 = ext_atoms(row_1)

                                data_type = row_1[angle_type_name]

                                peptide, nucleotide, carbohydrate = self.__csStat.getTypeOfCompId(atom2['comp_id'])
                                plane_like = is_like_planality_boundary(row_1, lower_limit_name, upper_limit_name)

                                data_type = self.getTypeOfDihedralRestraint(data_type, peptide, nucleotide, carbohydrate,
                                                                            [atom1, atom2, atom3, atom4], plane_like)[0]

                                if not data_type.startswith('phi') and not data_type.startswith('psi') and not data_type.startswith('omega'):
                                    continue

                            if r > max_inclusive:
                                discrepancy += f"{dname} |{_val_1}-{_val_2}| = {r:.1f} is out of acceptable range, "\
                                               f"{max_inclusive}{'°' if content_subtype == 'dihed_restraint' else 'Hz'}, "
                                conflict = True

                            elif r > max_inclusive * INCONSIST_OVER_CONFLICTED:
                                discrepancy += f"{dname} |{_val_1}-{_val_2}| = {r:.1f} is out of typical range, "\
                                               f"{max_inclusive * INCONSIST_OVER_CONFLICTED}{'°' if content_subtype == 'dihed_restraint' else 'Hz'}, "
                                inconsist = True

                    if conflict:

                        msg = '' if content_subtype != 'dihed_restraint' else angle_type_name + f" {row_1[angle_type_name]}, "
                        msg += self.__getReducedAtomNotations(key_items, row_1)

                        if index_tag in row_1:
                            warn = f"[Check rows of {index_tag} {row_1[index_tag]} vs {row_2[index_tag]}, {id_tag} {row_1[id_tag]} vs {row_2[id_tag]}] "
                        else:
                            warn = f"[Check rows of {index_tag} {id_set[i] + 1} vs {id_set[j] + 1}, {id_tag} {row_1[id_tag]} vs {row_2[id_tag]}] "
                        warn += f"Found conflict on restraints ({discrepancy[:-2]}) for the same {data_unit_name} ({msg})."

                        self.report.warning.appendDescription('conflicted_data',
                                                              {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                               'description': warn,
                                                               'sigma': float(f"{r / max_inclusive:.2f}")})
                        self.report.setWarning()

                        if self.__verbose:
                            self.__lfh.write(f"+{self.__class_name__}.detetConflictDataInLoop() ++ Warning  - {warn}\n")

                    elif inconsist:

                        msg = '' if content_subtype != 'dihed_restraint' else angle_type_name + f" {row_1[angle_type_name]}, "
                        msg += self.__getReducedAtomNotations(key_items, row_1)

                        if index_tag in row_1:
                            warn = f"[Check rows of {index_tag} {row_1[index_tag]} vs {row_2[index_tag]}, {id_tag} {row_1[id_tag]} vs {row_2[id_tag]}] "
                        else:
                            warn = f"[Check rows of {index_tag} {id_set[i] + 1} vs {id_set[j] + 1}, {id_tag} {row_1[id_tag]} vs {row_2[id_tag]}] "
                        warn += f"Found discrepancy in restraints ({discrepancy[:-2]}) for the same {data_unit_name} ({msg})."

                        self.report.warning.appendDescription('inconsistent_data',
                                                              {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                               'description': warn,
                                                               'sigma': float(f"{r / max_inclusive:.2f}")})
                        self.report.setWarning()

                        if self.__verbose:
                            self.__lfh.write(f"+{self.__class_name__}.detetConflictDataInLoop() ++ Warning  - {warn}\n")

            if redundant:

                idx_msg = index_tag + ' '
                if index_tag in lp_data[0]:
                    for row_id in id_set:
                        try:
                            idx_msg += f"{lp_data[row_id][index_tag]} vs "
                        except IndexError:
                            continue
                else:
                    for row_id in id_set:
                        idx_msg += f"{row_id + 1} vs "
                idx_msg = idx_msg[:-4] + ', '
                idx_msg += id_tag + ' '
                for row_id in id_set:
                    try:
                        idx_msg += f"{lp_data[row_id][id_tag]} vs "
                    except IndexError:
                        continue

                if not idx_msg.endswith(' vs '):
                    continue

                warn = f"[Check rows of {idx_msg[:-4]}] Found redundant restraints for the same {data_unit_name}."

                self.report.warning.appendDescription('redundant_data',
                                                      {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                       'description': warn})
                self.report.setWarning()

                if self.__verbose:
                    self.__lfh.write(f"+{self.__class_name__}.detetConflictDataInLoop() ++ Warning  - {warn}\n")

    def validateCsValue(self, file_list_id: int, file_name: str, file_type: str, content_subtype: str,
                        sf: Union[pynmrstar.Saveframe, pynmrstar.Loop],
                        sf_framecode: str, lp_category: str) -> bool:
        """ Validate assigned chemical shift value based on BMRB chemical shift statistics.
        """

        no_reason_message = " Neither aromatic ring nor paramagnetic/ferromagnetic atom were found in the vicinity."
        fold_warn_message = " Please check for folded/aliased signals."

        item_names = ITEM_NAMES_IN_CS_LOOP[file_type]
        chain_id_name = item_names['chain_id']
        seq_id_name = item_names['seq_id']
        comp_id_name = item_names['comp_id']
        atom_id_name = item_names['atom_id']
        value_name = item_names['value']
        ambig_code_name = 'Ambiguity_code'  # NMR-STAR specific
        occupancy_name = 'Occupancy'  # NMR-STAR specific

        full_value_name = lp_category + '.' + value_name

        max_inclusive = 0.01

        modified = False

        has_mr_atom_name_mapping = file_type == 'nmr-star' and self.__remediation_mode\
            and self.__mr_atom_name_mapping is not None and len(self.__mr_atom_name_mapping) > 0

        try:

            details_col = -1

            if file_type == 'nmr-star':

                loop = sf if self.__star_data_type[file_list_id] == 'Loop' else sf.get_loop(lp_category)

                if has_mr_atom_name_mapping:
                    auth_seq_id_col = loop.tags.index('Auth_seq_ID') if 'Auth_seq_ID' in loop.tags else -1
                    auth_comp_id_col = loop.tags.index('Auth_comp_ID') if 'Auth_comp_ID' in loop.tags else -1
                    auth_atom_id_col = loop.tags.index('Auth_atom_ID') if 'Auth_atom_ID' in loop.tags else -1
                    orig_atom_name_col = loop.tags.index('Original_PDB_atom_name') if 'Original_PDB_atom_name' in loop.tags else -1
                    if -1 in (auth_seq_id_col, auth_comp_id_col, auth_atom_id_col, orig_atom_name_col):
                        has_mr_atom_name_mapping = False

                if 'Details' in loop.tags:
                    details_col = loop.tags.index('Details')

                if ambig_code_name in loop.tags:
                    ambig_code_col = loop.tags.index(ambig_code_name)
                    ambig_code_dat = loop.get_tag(ambig_code_name)
                    if len(ambig_code_dat) > 0:
                        ambig_code_set = set()
                        invalid_ambig_code_set = set()
                        for row in ambig_code_dat:
                            if row not in emptyValue:
                                if row.isdigit() and int(row) in ALLOWED_AMBIGUITY_CODES:
                                    ambig_code_set.add(int(row))
                                else:
                                    invalid_ambig_code_set.add(row)
                        if len(invalid_ambig_code_set) > 0:
                            if seq_id_name in loop.tags and comp_id_name in loop.tags:
                                seq_key_set = set()
                                seq_key_dat = loop.get_tag([seq_id_name, comp_id_name])
                                for row in seq_key_dat:
                                    seq_key = (row[0], row[1])
                                    seq_key_set.add(seq_key)
                                if len(invalid_ambig_code_set) > len(seq_key_set) * 2:
                                    for row in loop:
                                        row[ambig_code_col] = '.'
                                else:
                                    for row in loop:
                                        if row[ambig_code_col] in invalid_ambig_code_set:
                                            row[ambig_code_col] = '.'
                        if len(ambig_code_set) == 1:
                            if 1 not in ambig_code_set:  # 2lrk
                                comp_id_col = loop.tags.index(comp_id_name)
                                atom_id_col = loop.tags.index(atom_id_name)
                                for row in loop:
                                    comp_id = row[comp_id_col]
                                    _atom_id = atom_id = row[atom_id_col]
                                    if self.isNmrAtomName(comp_id, atom_id):
                                        _atom_id = self.getRepAtomId(comp_id, atom_id)
                                    allowed_ambig_code = self.__csStat.getMaxAmbigCodeWoSetId(comp_id, _atom_id)
                                    if allowed_ambig_code in (0, 1):
                                        row[ambig_code_col] = '1'

            if (file_type == 'nef' or not self.__nonblk_anomalous_cs) and len(self.__lp_data[content_subtype]) > 0:
                lp_data = next(lp['data'] for lp in self.__lp_data[content_subtype]
                               if lp['file_name'] == file_name and lp['sf_framecode'] == sf_framecode)

            else:

                key_items = self.key_items[file_type][content_subtype]
                data_items = DATA_ITEMS[file_type][content_subtype]

                try:

                    lp_data = self.__nefT.check_data(sf, lp_category, key_items, data_items, None, None, None,
                                                     enforce_allowed_tags=(file_type == 'nmr-star'),
                                                     excl_missing_data=self.__excl_missing_data)[0]

                except Exception:

                    err = f"Assigned chemical shifts of {sf_framecode!r} saveframe was not parsed properly. Please fix problems reported."

                    self.report.error.appendDescription('missing_mandatory_content',
                                                        {'file_name': file_name, 'description': err})
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Error  - {err}\n")

                    return False

            chk_row_tmp = f"[Check row of {chain_id_name} %s, {seq_id_name} %s, {comp_id_name} %s, {atom_id_name} %s"
            row_tmp = f"{chain_id_name} %s, {seq_id_name} %s, {comp_id_name} %s, {atom_id_name} %s"

            methyl_cs_vals = {}
            failed_methyl_cs_keys = []

            for idx, row in enumerate(lp_data):
                chain_id = row[chain_id_name]
                seq_id = row[seq_id_name]
                comp_id = row[comp_id_name]
                atom_id = row[atom_id_name]
                value = row[value_name]
                occupancy = '.' if file_type == 'nef' else row[occupancy_name]

                alt_chain_id = set(emptyValue)
                alt_chain_id.add(chain_id)
                if chain_id.isalpha():
                    alt_chain_id.add(str(letterToDigit(chain_id)))

                if value in emptyValue:
                    continue

                if file_type == 'nef' or self.isNmrAtomName(comp_id, atom_id):
                    _atom_id, ambig_code, details = self.__getAtomIdListWithAmbigCode(comp_id, atom_id)

                    len_atom_id = len(_atom_id)

                    if len_atom_id == 0:
                        continue

                    if len_atom_id == 1 and atom_id == _atom_id[0]:
                        atom_id_ = atom_id
                        atom_name = atom_id

                        if details is not None:
                            atom_name += f", where {details.rstrip('.')}"

                    else:
                        atom_name = f'{atom_id} (e.g. '

                        for atom_id_ in _atom_id:
                            atom_name += f'{atom_id_} '

                        atom_name = f'{atom_name.rstrip()})'

                        # representative atom id
                        atom_id_ = _atom_id[0]

                else:
                    atom_id_ = atom_id
                    atom_name = atom_id

                has_cs_stat = False

                # non-standard residue
                if comp_id not in monDict3:

                    if has_mr_atom_name_mapping and atom_id_[0] == 'H':
                        try:
                            _row_ = loop.data[idx]
                            auth_seq_id, auth_comp_id, auth_atom_id, orig_atom_name =\
                                int(_row_[auth_seq_id_col]), _row_[auth_comp_id_col], _row_[auth_atom_id_col], _row_[orig_atom_name_col].upper()
                            if auth_comp_id not in emptyValue and auth_atom_id not in emptyValue and orig_atom_name not in emptyValue\
                               and auth_atom_id != orig_atom_name:
                                try:
                                    atom_map = next(atom_map for atom_map in self.__mr_atom_name_mapping
                                                    if atom_map['auth_seq_id'] == auth_seq_id and atom_map['auth_comp_id'] == auth_comp_id
                                                    and atom_map['auth_atom_id'] == auth_atom_id and atom_map['original_atom_id'] == auth_atom_id)
                                    atom_map['original_atom_id'] = orig_atom_name
                                except StopIteration:
                                    pass
                        except (ValueError, TypeError):
                            pass

                    neighbor_comp_ids = set(_row[comp_id_name] for _row in lp_data
                                            if _row[chain_id_name] == chain_id and abs(_row[seq_id_name] - seq_id) < 4 and _row[seq_id_name] != seq_id)

                    polypeptide_like = False

                    for comp_id2 in neighbor_comp_ids:
                        polypeptide_like |= self.__csStat.peptideLike(comp_id2)

                    cs_stats = self.__csStat.get(comp_id)
                    if len(cs_stats) == 0:
                        if self.__ccU.updateChemCompDict(comp_id):
                            parent_comp_id = self.__ccU.lastChemCompDict['_chem_comp.mon_nstd_parent_comp_id']
                            if parent_comp_id in monDict3:  # DAOTHER-9198: retrieve BMRB chemical shift statittics from parent comp_id if possible (i.e. DNR -> DC)
                                cs_stats = self.__csStat.get(parent_comp_id)

                    cs_stat = next((cs_stat for cs_stat in cs_stats if cs_stat['atom_id'] == atom_id_ and cs_stat['count'] > 0), None)

                    if cs_stat is not None:
                        min_value = cs_stat['min']
                        max_value = cs_stat['max']
                        avg_value = cs_stat['avg']
                        std_value = cs_stat['std']

                        has_cs_stat = True

                        if atom_id_[0] in protonBeginCode and 'methyl' in cs_stat['desc']:
                            methyl_h_list = self.__csStat.getProtonsInSameGroup(comp_id, atom_id)
                            _atom_id = methyl_h_list[0] if len(methyl_h_list) > 0 else atom_id
                            methyl_cs_key = (chain_id, seq_id, _atom_id, occupancy)

                            if methyl_cs_key not in methyl_cs_vals:
                                methyl_cs_vals[methyl_cs_key] = value

                            elif value != methyl_cs_vals[methyl_cs_key] and methyl_cs_key not in failed_methyl_cs_keys:
                                failed_methyl_cs_keys.append(methyl_cs_key)

                                err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                    + "] Chemical shift values in the same methyl group "\
                                    f"({full_value_name} {value} vs {methyl_cs_vals[methyl_cs_key]}) are inconsistent."

                                if self.__combined_mode and not self.__remediation_mode:

                                    self.report.error.appendDescription('invalid_data',
                                                                        {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                         'description': err})
                                    self.report.setError()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ ValueError  - {err}\n")

                                else:

                                    self.report.warning.appendDescription('conflicted_data',
                                                                          {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                           'description': err,
                                                                           'sigma': float(f"{abs(value - methyl_cs_vals[methyl_cs_key]) / max_inclusive:.2f}")})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {err}\n")

                        if std_value is None or std_value <= 0.0:

                            warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                + f"] Insufficient chemical shift statistics on comp_id {comp_id}, atom_id {atom_name} is available "\
                                f"to verify {full_value_name} {value} (avg {avg_value})."

                            self.report.warning.appendDescription('unusual_data',
                                                                  {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                   'description': warn})
                            self.report.setWarning()

                            if self.__verbose:
                                self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {warn}\n")

                            continue

                        if avg_value is None:

                            warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                + f"] Insufficient chemical shift statistics on comp_id {comp_id}, atom_id {atom_name} is available to verify {full_value_name} {value}."

                            self.report.warning.appendDescription('unusual_data',
                                                                  {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                   'description': warn})
                            self.report.setWarning()

                            if self.__verbose:
                                self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {warn}\n")

                            continue

                        z_score = float(f"{(value - avg_value) / std_value:.2f}")
                        sigma = abs(z_score)

                        if self.__csStat.hasSufficientStat(comp_id, polypeptide_like):
                            tolerance = std_value

                            if (value < min_value - tolerance or value > max_value + tolerance)\
                               and sigma > self.cs_anomalous_error_scaled_by_sigma\
                               and std_value > max_inclusive:

                                na = self.__getNearestAromaticRing(chain_id, seq_id, atom_id_)
                                pa = self.__getNearestParaFerroMagneticAtom(chain_id, seq_id, atom_id_)

                                if na is None and pa is None:

                                    err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                        + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) is not within expected range "\
                                        f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f})."

                                    err_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} ({value} ppm, {sigma:.2f} sigma), "\
                                        f"which is outside of expected range ({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                        f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value})."

                                    if self.__cifChecked:
                                        err += no_reason_message
                                        err_alt += no_reason_message

                                    err += fold_warn_message
                                    err_alt += fold_warn_message

                                    if self.__nonblk_anomalous_cs or self.__remediation_mode:

                                        self.report.warning.appendDescription('anomalous_data',
                                                                              {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                               'description': err,
                                                                               'value': value, 'z_score': z_score, 'description_alt': err_alt, 'sigma': sigma})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {err}\n")

                                        if self.__bmrb_only and self.__leave_intl_note and file_type == 'nmr-star' and details_col != -1:
                                            _details = loop.data[idx][details_col]
                                            details = f"{full_value_name} {value} is not within expected range "\
                                                f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f})."\
                                                f"{no_reason_message if self.__cifChecked else ''}"\
                                                f"{fold_warn_message}\n"
                                            if _details in emptyValue or (details not in _details):
                                                if _details in emptyValue:
                                                    loop.data[idx][details_col] = details
                                                else:
                                                    loop.data[idx][details_col] += ('' if '\n' in _details else '\n') + details
                                                modified = True

                                    else:

                                        self.report.error.appendDescription('anomalous_data',
                                                                            {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                             'description': err,
                                                                             'value': value, 'z_score': z_score, 'description_alt': err_alt, 'sigma': sigma})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ ValueError  - {err}\n")

                                elif pa is None:

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                        + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) should be verified "\
                                        f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f}). "\
                                        f"The nearest aromatic ring ({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                        f"is located at a distance of {na['ring_distance']}Å, "\
                                        f"and has an elevation angle of {na['ring_angle']}° with the ring plane."

                                    warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} ({value} ppm, {sigma:.2f} sigma), "\
                                        f"which is outside of expected range ({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                        f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value}). "\
                                        f"The nearest aromatic ring ({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                        f"is located at a distance of {na['ring_distance']}Å, "\
                                        f"and has an elevation angle of {na['ring_angle']}° with the ring plane."

                                    if (na['ring_angle'] - MAGIC_ANGLE) * z_score > 0.0 or self.__nonblk_anomalous_cs or self.__remediation_mode:

                                        self.report.warning.appendDescription('anomalous_data'
                                                                              if (na['ring_angle'] - MAGIC_ANGLE) * z_score < 0.0
                                                                              or na['ring_distance'] > VICINITY_AROMATIC
                                                                              else 'unusual_data',
                                                                              {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                               'description': warn,
                                                                               'value': value, 'z_score': z_score, 'description_alt': warn_alt, 'sigma': sigma})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {warn}\n")

                                        if self.__bmrb_only and self.__leave_intl_note and file_type == 'nmr-star' and details_col != -1\
                                           and ((na['ring_angle'] - MAGIC_ANGLE) * z_score < 0.0 or na['ring_distance'] > VICINITY_AROMATIC):
                                            _details = loop.data[idx][details_col]
                                            details = f"{full_value_name} {value} is not within expected range "\
                                                f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f}). "\
                                                f"The nearest aromatic ring {na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']} "\
                                                f"is located at a distance of {na['ring_distance']}Å, "\
                                                f"and has an elevation angle of {na['ring_angle']}° with the ring plane.\n"
                                            if _details in emptyValue or (details not in _details):
                                                if _details in emptyValue:
                                                    loop.data[idx][details_col] = details
                                                else:
                                                    loop.data[idx][details_col] += ('' if '\n' in _details else '\n') + details
                                                modified = True

                                    else:

                                        self.report.error.appendDescription('anomalous_data',
                                                                            {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                             'description': warn,
                                                                             'value': value, 'z_score': z_score, 'description_alt': warn_alt, 'sigma': sigma})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ ValueError  - {warn}\n")

                                else:

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                        + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) should be verified "\
                                        f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f}). "\
                                        f"The nearest paramagnetic/ferromagnetic atom ({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                        f"is located at a distance of {pa['distance']}Å."

                                    warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} ({value} ppm, {sigma:.2f} sigma), "\
                                        f"which is outside of expected range ({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                        f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value}). "\
                                        f"The nearest paramagnetic/ferromagnetic atom ({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                        f"is located at a distance of {pa['distance']}Å."

                                    self.report.warning.appendDescription('anomalous_data' if pa['distance'] > VICINITY_PARAMAGNETIC else 'unusual_data',
                                                                          {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                           'description': warn,
                                                                           'value': value, 'z_score': z_score, 'description_alt': warn_alt, 'sigma': sigma})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {warn}\n")

                                    if self.__bmrb_only and self.__leave_intl_note and file_type == 'nmr-star' and details_col != -1\
                                       and pa['distance'] > VICINITY_PARAMAGNETIC:
                                        _details = loop.data[idx][details_col]
                                        details = f"{full_value_name} {value} is not within expected range "\
                                            f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f}). "\
                                            f"The nearest paramagnetic/ferromagnetic atom {pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']} "\
                                            f"is located at a distance of {pa['distance']}Å.\n"
                                        if _details in emptyValue or (details not in _details):
                                            if _details in emptyValue:
                                                loop.data[idx][details_col] = details
                                            else:
                                                loop.data[idx][details_col] += ('' if '\n' in _details else '\n') + details
                                            modified = True

                            elif sigma > self.cs_anomalous_error_scaled_by_sigma and std_value > max_inclusive:

                                na = self.__getNearestAromaticRing(chain_id, seq_id, atom_id_)
                                pa = self.__getNearestParaFerroMagneticAtom(chain_id, seq_id, atom_id_)

                                if na is None and pa is None:

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                        + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) "\
                                        f"must be verified (avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f})."

                                    warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} ({value} ppm, {sigma:.2f} sigma), "\
                                        f"which is outside of expected range ({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                        f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value})."

                                    if self.__cifChecked:
                                        warn += no_reason_message
                                        warn_alt += no_reason_message

                                    self.report.warning.appendDescription('anomalous_data',
                                                                          {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                           'description': warn,
                                                                           'value': value, 'z_score': z_score, 'description_alt': warn_alt, 'sigma': sigma})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {warn}\n")

                                elif pa is None:

                                    if (na['ring_angle'] - MAGIC_ANGLE) * z_score < 0.0 or na['ring_distance'] > VICINITY_AROMATIC:

                                        warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                            + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) should be verified "\
                                            f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f}). "\
                                            f"The nearest aromatic ring ({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                            f"is located at a distance of {na['ring_distance']}Å, "\
                                            f"and has an elevation angle of {na['ring_angle']}° with the ring plane."

                                        warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} ({value} ppm, {sigma:.2f} sigma), "\
                                            f"which is outside of expected range ({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                            f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value}). "\
                                            f"The nearest aromatic ring ({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                            f"is located at a distance of {na['ring_distance']}Å, "\
                                            f"and has an elevation angle of {na['ring_angle']}° with the ring plane."

                                        self.report.warning.appendDescription('unusual_data',
                                                                              {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                               'description': warn,
                                                                               'value': value, 'z_score': z_score, 'description_alt': warn_alt, 'sigma': sigma})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {warn}\n")

                                else:

                                    if pa['distance'] > VICINITY_PARAMAGNETIC:

                                        warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                            + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) should be verified "\
                                            f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f}). "\
                                            f"The nearest paramagnetic/ferromagnetic atom ({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                            f"is located at a distance of {pa['distance']}Å."

                                        warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} ({value} ppm, {sigma:.2f} sigma), "\
                                            f"which is outside of expected range ({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                            f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value}). "\
                                            f"The nearest paramagnetic/ferromagnetic atom ({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                            f"is located at a distance of {pa['distance']}Å."

                                        self.report.warning.appendDescription('unusual_data',
                                                                              {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                               'description': warn,
                                                                               'value': value, 'z_score': z_score, 'description_alt': warn_alt, 'sigma': sigma})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {warn}\n")

                            elif sigma > self.cs_unusual_error_scaled_by_sigma and std_value > max_inclusive:

                                na = self.__getNearestAromaticRing(chain_id, seq_id, atom_id_)
                                pa = self.__getNearestParaFerroMagneticAtom(chain_id, seq_id, atom_id_)

                                warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                    + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) should be verified "\
                                    f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f})."

                                warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} ({value} ppm, {sigma:.2f} sigma), "\
                                    f"which is outside of expected range ({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                    f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value})."

                                if na is not None:

                                    if (na['ring_angle'] - MAGIC_ANGLE) * z_score < 0.0 or na['ring_distance'] > VICINITY_AROMATIC:
                                        warn += f" The nearest aromatic ring ({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                            f"is located at a distance of {na['ring_distance']}Å, "\
                                            f"and has an elevation angle of {na['ring_angle']}° with the ring plane."
                                        warn_alt += f" The nearest aromatic ring ({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                            f"is located at a distance of {na['ring_distance']}Å, "\
                                            f"and has an elevation angle of {na['ring_angle']}° with the ring plane."
                                    else:
                                        warn = warn_alt = None

                                elif pa is not None:

                                    if pa['distance'] > VICINITY_PARAMAGNETIC:
                                        warn += f" The nearest paramagnetic/ferromagnetic atom ({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                            f"is located at a distance of {pa['distance']}Å."
                                        warn_alt += f" The nearest paramagnetic/ferromagnetic atom ({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                            f"is located at a distance of {pa['distance']}Å."
                                    else:
                                        warn = warn_alt = None

                                elif self.__cifChecked:
                                    warn += no_reason_message
                                    warn_alt += no_reason_message

                                if warn is not None:
                                    self.report.warning.appendDescription('unusual_data',
                                                                          {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                           'description': warn,
                                                                           'value': value, 'z_score': z_score, 'description_alt': warn_alt, 'sigma': sigma})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {warn}\n")

                            elif not cs_stat['primary'] and cs_stat['norm_freq'] < 0.03 and self.__exptl_method != 'SOLID-STATE NMR':

                                warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                    + f"] {full_value_name} {value} is an unusual/rare assignment. "\
                                    f"Occurrence of {atom_name} in {comp_id} is {cs_stat['norm_freq']:.1%} in BMRB archive."

                                self.report.warning.appendDescription('unusual/rare_data',
                                                                      {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                       'description': warn})
                                self.report.setWarning()

                                if self.__verbose:
                                    self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {warn}\n")

                        else:

                            tolerance = std_value * 10.0  # rare residue/ligand

                            if min_value < max_value and (value < min_value - tolerance or value > max_value + tolerance)\
                               and sigma > self.cs_anomalous_error_scaled_by_sigma\
                               and std_value > max_inclusive:

                                na = self.__getNearestAromaticRing(chain_id, seq_id, atom_id_)
                                pa = self.__getNearestParaFerroMagneticAtom(chain_id, seq_id, atom_id_)

                                if na is None and pa is None:

                                    err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                        + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) is not within expected range "\
                                        f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f})."

                                    err_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} ({value} ppm, {sigma:.2f} sigma), "\
                                        f"which is outside of expected range ({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                        f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value})."

                                    if self.__cifChecked:
                                        err += no_reason_message
                                        err_alt += no_reason_message

                                    err += fold_warn_message
                                    err_alt += fold_warn_message

                                    if self.__nonblk_anomalous_cs or self.__remediation_mode:

                                        self.report.warning.appendDescription('anomalous_data',
                                                                              {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                               'description': err,
                                                                               'value': value, 'z_score': z_score, 'description_alt': err_alt, 'sigma': sigma})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {err}\n")

                                        if self.__bmrb_only and self.__leave_intl_note and file_type == 'nmr-star' and details_col != -1:
                                            _details = loop.data[idx][details_col]
                                            details = f"{full_value_name} {value} is not within expected range "\
                                                f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f})."\
                                                f"{no_reason_message if self.__cifChecked else ''}"\
                                                f"{fold_warn_message}\n"
                                            if _details in emptyValue or (details not in _details):
                                                if _details in emptyValue:
                                                    loop.data[idx][details_col] = details
                                                else:
                                                    loop.data[idx][details_col] += ('' if '\n' in _details else '\n') + details
                                                modified = True

                                    else:

                                        self.report.error.appendDescription('anomalous_data',
                                                                            {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                             'description': err,
                                                                             'value': value, 'z_score': z_score, 'description_alt': err_alt, 'sigma': sigma})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ ValueError  - {err}\n")

                                elif pa is None:

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                        + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) should be verified "\
                                        f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f}). "\
                                        f"The nearest aromatic ring ({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                        f"is located at a distance of {na['ring_distance']}Å, "\
                                        f"and has an elevation angle of {na['ring_angle']}° with the ring plane."

                                    warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} ({value} ppm, {sigma:.2f} sigma), "\
                                        f"which is outside of expected range ({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                        f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value}). "\
                                        f"The nearest aromatic ring ({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                        f"is located at a distance of {na['ring_distance']}Å, "\
                                        f"and has an elevation angle of {na['ring_angle']}° with the ring plane."

                                    if (na['ring_angle'] - MAGIC_ANGLE) * z_score > 0.0 or self.__nonblk_anomalous_cs or self.__remediation_mode:

                                        if (na['ring_angle'] - MAGIC_ANGLE) * z_score < 0.0 or na['ring_distance'] > VICINITY_AROMATIC:

                                            self.report.warning.appendDescription('anomalous_data',
                                                                                  {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                                   'description': warn,
                                                                                   'value': value, 'z_score': z_score, 'description_alt': warn_alt, 'sigma': sigma})
                                            self.report.setWarning()

                                            if self.__verbose:
                                                self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {warn}\n")

                                            if self.__bmrb_only and self.__leave_intl_note and file_type == 'nmr-star' and details_col != -1:
                                                _details = loop.data[idx][details_col]
                                                details = f"{full_value_name} {value} is not within expected range "\
                                                    f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f}). "\
                                                    f"The nearest aromatic ring {na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']} "\
                                                    f"is located at a distance of {na['ring_distance']}Å, "\
                                                    f"and has an elevation angle of {na['ring_angle']}° with the ring plane.\n"
                                                if _details in emptyValue or (details not in _details):
                                                    if _details in emptyValue:
                                                        loop.data[idx][details_col] = details
                                                    else:
                                                        loop.data[idx][details_col] += ('' if '\n' in _details else '\n') + details
                                                    modified = True

                                    else:

                                        self.report.error.appendDescription('anomalous_data',
                                                                            {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                             'description': warn,
                                                                             'value': value, 'z_score': z_score, 'description_alt': warn_alt, 'sigma': sigma})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ ValueError  - {warn}\n")

                                else:

                                    if pa['distance'] > VICINITY_PARAMAGNETIC:

                                        warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                            + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) should be verified "\
                                            f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f}). "\
                                            f"The nearest paramagnetic/ferromagnetic atom ({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                            f"is located at a distance of {pa['distance']}Å."

                                        warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} ({value} ppm, {sigma:.2f} sigma), "\
                                            f"which is outside of expected range ({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                            f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value}). "\
                                            f"The nearest paramagnetic/ferromagnetic atom ({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                            f"is located at a distance of {pa['distance']}Å."

                                        self.report.warning.appendDescription('unusual_data',
                                                                              {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                               'description': warn,
                                                                               'value': value, 'z_score': z_score, 'description_alt': warn_alt, 'sigma': sigma})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {warn}\n")

                                        if self.__bmrb_only and self.__leave_intl_note and file_type == 'nmr-star' and details_col != -1:
                                            _details = loop.data[idx][details_col]
                                            details = f"{full_value_name} {value} is not within expected range "\
                                                f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f}). "\
                                                f"The nearest paramagnetic/ferromagnetic atom {pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']} "\
                                                f"is located at a distance of {pa['distance']}Å.\n"
                                            if _details in emptyValue or (details not in _details):
                                                if _details in emptyValue:
                                                    loop.data[idx][details_col] = details
                                                else:
                                                    loop.data[idx][details_col] += ('' if '\n' in _details else '\n') + details
                                                modified = True

                            elif sigma > self.cs_anomalous_error_scaled_by_sigma and std_value > max_inclusive:

                                na = self.__getNearestAromaticRing(chain_id, seq_id, atom_id_)
                                pa = self.__getNearestParaFerroMagneticAtom(chain_id, seq_id, atom_id_)

                                if na is None and pa is None:

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                        + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) "\
                                        f"must be verified (avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f})."

                                    warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} ({value} ppm, {sigma:.2f} sigma), "\
                                        f"which is outside of expected range ({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                        f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value})."

                                    if self.__cifChecked:
                                        warn += no_reason_message
                                        warn_alt += no_reason_message

                                    self.report.warning.appendDescription('anomalous_data',
                                                                          {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                           'description': warn,
                                                                           'value': value, 'z_score': z_score, 'description_alt': warn_alt, 'sigma': sigma})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {warn}\n")

                                elif pa is None:

                                    if (na['ring_angle'] - MAGIC_ANGLE) * z_score < 0.0 or na['ring_distance'] > VICINITY_AROMATIC:

                                        warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                            + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) should be verified "\
                                            f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f}). "\
                                            f"The nearest aromatic ring ({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                            f"is located at a distance of {na['ring_distance']}Å, "\
                                            f"and has an elevation angle of {na['ring_angle']}° with the ring plane."

                                        warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} ({value} ppm, {sigma:.2f} sigma), "\
                                            f"which is outside of expected range ({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                            f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value}). "\
                                            f"The nearest aromatic ring ({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                            f"is located at a distance of {na['ring_distance']}Å, "\
                                            f"and has an elevation angle of {na['ring_angle']}° with the ring plane."

                                        self.report.warning.appendDescription('unusual_data',
                                                                              {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                               'description': warn,
                                                                               'value': value, 'z_score': z_score, 'description_alt': warn_alt, 'sigma': sigma})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {warn}\n")

                                else:

                                    if pa['distance'] > VICINITY_PARAMAGNETIC:

                                        warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                            + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) should be verified "\
                                            f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f}). "\
                                            f"The nearest paramagnetic/ferromagnetic atom ({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                            f"is located at a distance of {pa['distance']}Å."

                                        warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} ({value} ppm, {sigma:.2f} sigma), "\
                                            f"which is outside of expected range ({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                            f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value}). "\
                                            f"The nearest paramagnetic/ferromagnetic atom ({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                            f"is located at a distance of {pa['distance']}Å."

                                        self.report.warning.appendDescription('unusual_data',
                                                                              {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                               'description': warn,
                                                                               'value': value, 'z_score': z_score, 'description_alt': warn_alt, 'sigma': sigma})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {warn}\n")

                # standard residue
                else:

                    cs_stat = next((cs_stat for cs_stat in self.__csStat.get(comp_id, self.report.isDiamagnetic())
                                    if cs_stat['atom_id'] == atom_id_ and cs_stat['count'] > 0), None)

                    if cs_stat is not None:
                        min_value = cs_stat['min']
                        max_value = cs_stat['max']
                        avg_value = cs_stat['avg']
                        std_value = cs_stat['std']

                        has_cs_stat = True

                        if atom_id_[0] in protonBeginCode and 'methyl' in cs_stat['desc']:
                            methyl_cs_key = (chain_id, seq_id, atom_id_[:-1], occupancy)

                            if methyl_cs_key not in methyl_cs_vals:
                                methyl_cs_vals[methyl_cs_key] = value

                            elif value != methyl_cs_vals[methyl_cs_key] and methyl_cs_key not in failed_methyl_cs_keys:
                                failed_methyl_cs_keys.append(methyl_cs_key)

                                err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                    + "] Chemical shift values in the same methyl group "\
                                    f"({full_value_name} {value} vs {methyl_cs_vals[methyl_cs_key]}) are inconsistent."

                                if self.__combined_mode and not self.__remediation_mode:

                                    self.report.error.appendDescription('invalid_data',
                                                                        {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                         'description': err})
                                    self.report.setError()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ ValueError  - {err}\n")

                                else:

                                    self.report.warning.appendDescription('conflicted_data',
                                                                          {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                           'description': err,
                                                                           'sigma': float(f"{abs(value - methyl_cs_vals[methyl_cs_key]) / max_inclusive:.2f}")})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {err}\n")

                        if std_value is None or std_value <= 0.0:

                            warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                + f"] Insufficient chemical shift statistics on comp_id {comp_id}, atom_id {atom_name} is available "\
                                f"to verify {full_value_name} {value} (avg {avg_value})."

                            self.report.warning.appendDescription('unusual_data',
                                                                  {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                   'description': warn})
                            self.report.setWarning()

                            if self.__verbose:
                                self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {warn}\n")

                            continue

                        if avg_value is None:

                            warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                + f"] Insufficient chemical shift statistics on comp_id {comp_id}, atom_id {atom_name} is available to verify {full_value_name} {value}."

                            self.report.warning.appendDescription('unusual_data',
                                                                  {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                   'description': warn})
                            self.report.setWarning()

                            if self.__verbose:
                                self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {warn}\n")

                            continue

                        z_score = float(f"{(value - avg_value) / std_value:.2f}")
                        sigma = abs(z_score)
                        tolerance = std_value

                        if (value < min_value - tolerance or value > max_value + tolerance)\
                           and sigma > self.cs_unusual_error_scaled_by_sigma\
                           and std_value > max_inclusive:

                            na = self.__getNearestAromaticRing(chain_id, seq_id, atom_id_)
                            pa = self.__getNearestParaFerroMagneticAtom(chain_id, seq_id, atom_id_)

                            if na is None and pa is None:

                                err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                    + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) is not within expected range "\
                                    f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f})."

                                err_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} ({value} ppm, {sigma:.2f} sigma), "\
                                    f"which is outside of expected range ({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                    f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value})."

                                if self.__cifChecked:
                                    err += no_reason_message
                                    err_alt += no_reason_message

                                err += fold_warn_message
                                err_alt += fold_warn_message

                                if self.__nonblk_anomalous_cs or self.__remediation_mode:

                                    self.report.warning.appendDescription('anomalous_data',
                                                                          {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                           'description': err,
                                                                           'value': value, 'z_score': z_score, 'description_alt': err_alt, 'sigma': sigma})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {err}\n")

                                    if self.__bmrb_only and self.__leave_intl_note and file_type == 'nmr-star' and details_col != -1:
                                        _details = loop.data[idx][details_col]
                                        details = f"{full_value_name} {value} is not within expected range "\
                                            f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f})."\
                                            f"{no_reason_message if self.__cifChecked else ''}"\
                                            f"{fold_warn_message}\n"
                                        if _details in emptyValue or (details not in _details):
                                            if _details in emptyValue:
                                                loop.data[idx][details_col] = details
                                            else:
                                                loop.data[idx][details_col] += ('' if '\n' in _details else '\n') + details
                                            modified = True

                                else:

                                    self.report.error.appendDescription('anomalous_data',
                                                                        {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                         'description': err,
                                                                         'value': value, 'z_score': z_score, 'description_alt': err_alt, 'sigma': sigma})
                                    self.report.setError()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ ValueError  - {err}\n")

                            elif pa is None:

                                warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                    + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) should be verified "\
                                    f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f}). "\
                                    f"The nearest aromatic ring ({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                    f"is located at a distance of {na['ring_distance']}Å, "\
                                    f"and has an elevation angle of {na['ring_angle']}° with the ring plane."

                                warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} ({value} ppm, {sigma:.2f} sigma), "\
                                    f"which is outside of expected range ({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                    f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value}). "\
                                    f"The nearest aromatic ring ({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                    f"is located at a distance of {na['ring_distance']}Å, "\
                                    f"and has an elevation angle of {na['ring_angle']}° with the ring plane."

                                if (na['ring_angle'] - MAGIC_ANGLE) * z_score > 0.0 or self.__nonblk_anomalous_cs or self.__remediation_mode:

                                    self.report.warning.appendDescription('anomalous_data'
                                                                          if (na['ring_angle'] - MAGIC_ANGLE) * z_score < 0.0
                                                                          or na['ring_distance'] > VICINITY_AROMATIC
                                                                          else 'unusual_data',
                                                                          {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                           'description': warn,
                                                                           'value': value, 'z_score': z_score, 'description_alt': warn_alt, 'sigma': sigma})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {warn}\n")

                                    if self.__bmrb_only and self.__leave_intl_note and file_type == 'nmr-star' and details_col != -1\
                                       and ((na['ring_angle'] - MAGIC_ANGLE) * z_score > 0.0 or self.__nonblk_anomalous_cs):
                                        _details = loop.data[idx][details_col]
                                        details = f"{full_value_name} {value} is not within expected range "\
                                            f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f}). "\
                                            f"The nearest aromatic ring {na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']} "\
                                            f"is located at a distance of {na['ring_distance']}Å, "\
                                            f"and has an elevation angle of {na['ring_angle']}° with the ring plane.\n"
                                        if _details in emptyValue or (details not in _details):
                                            if _details in emptyValue:
                                                loop.data[idx][details_col] = details
                                            else:
                                                loop.data[idx][details_col] += ('' if '\n' in _details else '\n') + details
                                            modified = True

                                else:

                                    self.report.error.appendDescription('anomalous_data',
                                                                        {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                         'description': warn,
                                                                         'value': value, 'z_score': z_score, 'description_alt': warn_alt, 'sigma': sigma})
                                    self.report.setError()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ ValueError  - {warn}\n")

                            else:

                                warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                    + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) should be verified "\
                                    f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f}). "\
                                    f"The nearest paramagnetic/ferromagnetic atom ({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                    f"is located at a distance of {pa['distance']}Å."

                                warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} ({value} ppm, {sigma:.2f} sigma), "\
                                    f"which is outside of expected range ({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                    f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value}). "\
                                    f"The nearest paramagnetic/ferromagnetic atom ({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                    f"is located at a distance of {pa['distance']}Å."

                                self.report.warning.appendDescription('anomalous_data' if pa['distance'] > VICINITY_PARAMAGNETIC else 'unusual_data',
                                                                      {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                       'description': warn,
                                                                       'value': value, 'z_score': z_score, 'description_alt': warn_alt, 'sigma': sigma})
                                self.report.setWarning()

                                if self.__verbose:
                                    self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {warn}\n")

                                if self.__bmrb_only and self.__leave_intl_note and file_type == 'nmr-star' and details_col != -1\
                                   and pa['distance'] > VICINITY_PARAMAGNETIC:
                                    _details = loop.data[idx][details_col]
                                    details = f"{full_value_name} {value} is not within expected range "\
                                        f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f}). "\
                                        f"The nearest paramagnetic/ferromagnetic atom {pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']} "\
                                        f"is located at a distance of {pa['distance']}Å.\n"
                                    if _details in emptyValue or (details not in _details):
                                        if _details in emptyValue:
                                            loop.data[idx][details_col] = details
                                        else:
                                            loop.data[idx][details_col] += ('' if '\n' in _details else '\n') + details
                                        modified = True

                        elif sigma > self.cs_unusual_error_scaled_by_sigma and std_value > max_inclusive:  # Set 5.0 to be consistent with validation report

                            na = self.__getNearestAromaticRing(chain_id, seq_id, atom_id_)
                            pa = self.__getNearestParaFerroMagneticAtom(chain_id, seq_id, atom_id_)

                            if na is None and pa is None:

                                warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                    + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) "\
                                    f"must be verified (avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f})."

                                warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} ({value} ppm, {sigma:.2f} sigma), "\
                                    f"which is outside of expected range ({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                    f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value})."

                                if self.__cifChecked:
                                    warn += no_reason_message
                                    warn_alt += no_reason_message

                                self.report.warning.appendDescription('anomalous_data',
                                                                      {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                       'description': warn,
                                                                       'value': value, 'z_score': z_score, 'description_alt': warn_alt, 'sigma': sigma})
                                self.report.setWarning()

                                if self.__verbose:
                                    self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {warn}\n")

                            elif pa is None:

                                if (na['ring_angle'] - MAGIC_ANGLE) * z_score < 0.0 or na['ring_distance'] > VICINITY_AROMATIC:

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                        + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) should be verified "\
                                        f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f}). "\
                                        f"The nearest aromatic ring ({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                        f"is located at a distance of {na['ring_distance']}Å, "\
                                        f"and has an elevation angle of {na['ring_angle']}° with the ring plane."

                                    warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} ({value} ppm, {sigma:.2f} sigma), "\
                                        f"which is outside of expected range ({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                        f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value}). "\
                                        f"The nearest aromatic ring ({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                        f"is located at a distance of {na['ring_distance']}Å, "\
                                        f"and has an elevation angle of {na['ring_angle']}° with the ring plane."

                                    self.report.warning.appendDescription('unusual_data',
                                                                          {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                           'description': warn,
                                                                           'value': value, 'z_score': z_score, 'description_alt': warn_alt, 'sigma': sigma})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {warn}\n")

                            else:

                                if pa['distance'] > VICINITY_PARAMAGNETIC:

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                        + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) should be verified "\
                                        f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f}). "\
                                        f"The nearest paramagnetic/ferromagnetic atom ({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                        f"is located at a distance of {pa['distance']}Å."

                                    warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} ({value} ppm, {sigma:.2f} sigma), "\
                                        f"which is outside of expected range ({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                        f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value}). "\
                                        f"The nearest paramagnetic/ferromagnetic atom ({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                        f"is located at a distance of {pa['distance']}Å."

                                    self.report.warning.appendDescription('unusual_data',
                                                                          {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                           'description': warn,
                                                                           'value': value, 'z_score': z_score, 'description_alt': warn_alt, 'sigma': sigma})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {warn}\n")

                        elif not cs_stat['primary'] and cs_stat['norm_freq'] < 0.03 and self.__exptl_method != 'SOLID-STATE NMR':

                            warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                + f"] {full_value_name} {value} is an unusual/rare assignment. "\
                                f"Occurrence of {atom_name} in {comp_id} is {cs_stat['norm_freq']:.1%} in BMRB archive."

                            self.report.warning.appendDescription('unusual/rare_data',
                                                                  {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                   'description': warn})
                            self.report.setWarning()

                            if self.__verbose:
                                self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {warn}\n")

                if not has_cs_stat:

                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                        + f"] No chemical shift statistics is available to verify {full_value_name} {value}."

                    self.report.warning.appendDescription('unusual_data',
                                                          {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                           'description': warn})
                    self.report.setWarning()

                    if self.__verbose:
                        self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {warn}\n")

                # check ambiguity code
                if file_type == 'nmr-star' and ambig_code_name in row:
                    ambig_code = row[ambig_code_name]

                    if ambig_code in emptyValue or ambig_code == 1:
                        continue

                    _atom_id = atom_id

                    if self.isNmrAtomName(comp_id, atom_id):
                        _atom_id = self.getRepAtomId(comp_id, atom_id)

                    allowed_ambig_code = self.__csStat.getMaxAmbigCodeWoSetId(comp_id, _atom_id)

                    if ambig_code in (2, 3):

                        ambig_code_desc = 'ambiguity of geminal atoms or geminal methyl proton groups' if ambig_code == 2\
                            else 'aromatic atoms on opposite sides of symmetrical rings'

                        _atom_id2 = self.__csStat.getGeminalAtom(comp_id, _atom_id)

                        if ambig_code != allowed_ambig_code:

                            if allowed_ambig_code == 1:

                                try:

                                    _row = next(_row for _row in lp_data
                                                if _row[chain_id_name] == chain_id
                                                and _row[seq_id_name] == seq_id
                                                and _row[comp_id_name] == comp_id
                                                and _row[atom_id_name] == _atom_id2)

                                    loop.data[lp_data.index(_row)][loop.tags.index(ambig_code_name)] = 1

                                except StopIteration:
                                    pass

                            elif allowed_ambig_code > 0:

                                if self.__remediation_mode:
                                    pass

                                else:

                                    err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id)\
                                        + f"] Invalid {ambig_code_name} {str(ambig_code)!r} "\
                                        f"(allowed ambig_code {[1, allowed_ambig_code, 4, 5, 6, 9]}) in a loop {lp_category}."

                                    self.report.error.appendDescription('invalid_ambiguity_code',
                                                                        {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                         'description': err})
                                    self.report.setError()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ ValueError  - {err}\n")

                        try:

                            _row = next(_row for _row in lp_data
                                        if _row[chain_id_name] == chain_id
                                        and _row[seq_id_name] == seq_id
                                        and _row[comp_id_name] == comp_id
                                        and _row[atom_id_name] == _atom_id2)

                            ambig_code2 = _row[ambig_code_name]

                            if ambig_code2 is not None and ambig_code2 != ambig_code:

                                if ambig_code2 < 4:
                                    loop.data[lp_data.index(_row)][loop.tags.index(ambig_code_name)] = ambig_code

                                if self.__remediation_mode:
                                    pass

                                else:

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id)\
                                        + f"] {ambig_code_name} {str(ambig_code)!r} indicates {ambig_code_desc}. "\
                                        f"However, {ambig_code_name} {ambig_code2} of {atom_id_name} {_atom_id2} is inconsistent."

                                    self.report.warning.appendDescription('ambiguity_code_mismatch',
                                                                          {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                           'description': warn})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {warn}\n")

                        except StopIteration:
                            pass

                    elif ambig_code in (4, 5, 6, 9):

                        ambig_set_id_name = 'Ambiguity_set_ID'

                        if ambig_set_id_name not in row:

                            err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id)\
                                + f"] {ambig_code_name} {str(ambig_code)!r} requires {ambig_set_id_name} loop tag."

                            if self.__remediation_mode:

                                self.report.warning.appendDescription('missing_data',
                                                                      {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                       'description': err})
                                self.report.setWarning()

                                if self.__verbose:
                                    self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {err}\n")

                            else:

                                self.report.error.appendDescription('missing_mandatory_item',
                                                                    {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                     'description': err})
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ LookupError  - "
                                                     f"{file_name} {sf_framecode} {lp_category} {err}\n")

                        else:

                            ambig_set_id = row[ambig_set_id_name]

                            if ambig_set_id in emptyValue:

                                if ambig_code in (4, 5):

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id)\
                                        + f"] {ambig_code_name} {str(ambig_code)!r} requires {ambig_set_id_name} value."

                                    self.report.warning.appendDescription('missing_data',
                                                                          {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                           'description': warn})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {warn}\n")

                            else:

                                ambig_set = [_row for _row in lp_data if _row[ambig_set_id_name] == ambig_set_id and _row != row]

                                if len(ambig_set) == 0:

                                    if ambig_code == 4:
                                        ambig_desc = 'of intra-residue atoms '
                                    elif ambig_code == 5:
                                        ambig_desc = 'of inter-residue atoms '
                                    else:
                                        ambig_desc = ''

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id)\
                                        + f"] {ambig_code_name} {str(ambig_code)!r} requires other rows {ambig_desc}sharing {ambig_set_id_name} {ambig_set_id}."

                                    self.report.warning.appendDescription('missing_data',
                                                                          {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                           'description': warn})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Warning  - {warn}\n")

                                # intra-residue ambiguities
                                elif ambig_code == 4:

                                    for _row in ambig_set:
                                        chain_id2 = _row[chain_id_name]
                                        seq_id2 = _row[seq_id_name]
                                        comp_id2 = _row[comp_id_name]
                                        atom_id2 = _row[atom_id_name]

                                        _atom_id2 = atom_id2

                                        if self.isNmrAtomName(comp_id2, atom_id2):
                                            _atom_id2 = self.getRepAtomId(comp_id2, atom_id2)

                                        if (chain_id2 != chain_id or seq_id2 != seq_id or comp_id2 != comp_id) and _atom_id < _atom_id2:

                                            err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id)\
                                                + f", {ambig_code_name} {str(ambig_code)!r}, {ambig_set_id_name} {ambig_set_id}] "\
                                                "It indicates intra-residue ambiguities. However, row of "\
                                                + row_tmp % (chain_id2, seq_id2, comp_id2, atom_id2) + ' exists.'

                                            self.report.error.appendDescription('invalid_ambiguity_code',
                                                                                {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                                 'description': err})
                                            self.report.setError()

                                            if self.__verbose:
                                                self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ ValueError  - {err}\n")

                                # inter-residue ambiguities
                                elif ambig_code == 5:

                                    inter_residue_seq_id = False

                                    for _row in ambig_set:
                                        chain_id2 = _row[chain_id_name]
                                        seq_id2 = _row[seq_id_name]
                                        comp_id2 = _row[comp_id_name]
                                        atom_id2 = _row[atom_id_name]

                                        _atom_id2 = atom_id2

                                        if self.isNmrAtomName(comp_id2, atom_id2):
                                            _atom_id2 = self.getRepAtomId(comp_id2, atom_id2)

                                        if chain_id2 != chain_id or seq_id2 != seq_id:
                                            inter_residue_seq_id = True
                                            break

                                    if not inter_residue_seq_id:

                                        for _row in ambig_set:
                                            chain_id2 = _row[chain_id_name]
                                            seq_id2 = _row[seq_id_name]
                                            comp_id2 = _row[comp_id_name]
                                            atom_id2 = _row[atom_id_name]

                                            _atom_id2 = atom_id2

                                            if self.isNmrAtomName(comp_id2, atom_id2):
                                                _atom_id2 = self.getRepAtomId(comp_id2, atom_id2)

                                            if chain_id2 == chain_id and seq_id2 == seq_id and _atom_id < _atom_id2:

                                                err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id)\
                                                    + f", {ambig_code_name} {str(ambig_code)!r}, {ambig_set_id_name} {ambig_set_id}] "\
                                                    "It indicates inter-residue ambiguities. However, row of "\
                                                    + row_tmp % (chain_id2, seq_id2, comp_id2, atom_id2) + ' exists.'

                                                self.report.error.appendDescription('invalid_ambiguity_code',
                                                                                    {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                                     'description': err})
                                                self.report.setError()

                                                if self.__verbose:
                                                    self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ ValueError  - {err}\n")

                                # inter-molecular ambiguities
                                elif ambig_code == 6:

                                    for _row in ambig_set:
                                        chain_id2 = _row[chain_id_name]
                                        seq_id2 = _row[seq_id_name]
                                        comp_id2 = _row[comp_id_name]
                                        atom_id2 = _row[atom_id_name]

                                        _atom_id2 = atom_id2

                                        if self.isNmrAtomName(comp_id2, atom_id2):
                                            _atom_id2 = self.getRepAtomId(comp_id2, atom_id2)

                                        if chain_id2 == chain_id and (seq_id < seq_id2 or (seq_id == seq_id2 and _atom_id < _atom_id2)):

                                            if chain_id == chain_id2 and seq_id == seq_id2:
                                                if _atom_id2 in self.__csStat.getProtonsInSameGroup(comp_id, _atom_id):
                                                    continue

                                            if not any(True for _row_ in ambig_set if _row_[chain_id_name] != chain_id
                                               and _row_[seq_id_name] == seq_id and _row_[comp_id_name] == comp_id
                                               and _row_[atom_id_name] == atom_id):

                                                err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id)\
                                                    + f", {ambig_code_name} {str(ambig_code)!r}, {ambig_set_id_name} {ambig_set_id}] "\
                                                    "It indicates inter-molecular ambiguities. However, row of "\
                                                    + row_tmp % (chain_id2, seq_id2, comp_id2, atom_id2) + ' exists.'

                                                self.report.error.appendDescription('invalid_ambiguity_code',
                                                                                    {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                                     'description': err})
                                                self.report.setError()

                                                if self.__verbose:
                                                    self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ ValueError  - {err}\n")

                                for _row in ambig_set:
                                    chain_id2 = _row[chain_id_name]
                                    seq_id2 = _row[seq_id_name]
                                    comp_id2 = _row[comp_id_name]
                                    atom_id2 = _row[atom_id_name]
                                    value2 = _row[value_name]

                                    if comp_id2 not in monDict3:
                                        continue

                                    _atom_id2 = atom_id2

                                    if self.isNmrAtomName(comp_id2, atom_id2):
                                        _atom_id2 = self.getRepAtomId(comp_id2, atom_id2)

                                    if _atom_id[0] != _atom_id2[0] and _atom_id < _atom_id2:

                                        if self.__remediation_mode:

                                            chain_id_col = loop.tags.index(chain_id_name)
                                            seq_id_col = loop.tags.index(seq_id_name)
                                            comp_id_col = loop.tags.index(comp_id_name)
                                            atom_id_col = loop.tags.index(atom_id_name)
                                            ambig_code_col = loop.tags.index(ambig_code_name)

                                            row = next(row for row in loop
                                                       if row[chain_id_col] in alt_chain_id and int(row[seq_id_col]) == seq_id
                                                       and row[comp_id_col] == comp_id and row[atom_id_col] == atom_id)

                                            row[ambig_code_col] = allowed_ambig_code

                                            row = next(row for row in loop
                                                       if row[chain_id_col] in alt_chain_id and int(row[seq_id_col]) == seq_id2
                                                       and row[comp_id_col] == comp_id2 and row[atom_id_col] == atom_id2)

                                            row[ambig_code_col] = allowed_ambig_code

                                            modified = True

                                        else:

                                            err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id)\
                                                + f", {ambig_code_name} {str(ambig_code)!r}, {ambig_set_id_name} {ambig_set_id}] "\
                                                "However, observation nucleus of "\
                                                + row_tmp % (chain_id2, seq_id2, comp_id2, atom_id2)\
                                                + f" is different in the set that share the same ambiguity code ({_atom_id[0]!r} vs {_atom_id2[0]!r})."

                                            self.report.error.appendDescription('invalid_ambiguity_code',
                                                                                {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                                 'description': err})
                                            self.report.setError()

                                            if self.__verbose:
                                                self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ ValueError  - {err}\n")

                                    elif abs(value2 - value) > CS_UNCERT_MAX and value < value2 and ambig_code <= 4:

                                        if self.__remediation_mode:

                                            chain_id_col = loop.tags.index(chain_id_name)
                                            seq_id_col = loop.tags.index(seq_id_name)
                                            comp_id_col = loop.tags.index(comp_id_name)
                                            atom_id_col = loop.tags.index(atom_id_name)
                                            ambig_code_col = loop.tags.index(ambig_code_name)

                                            row = next(row for row in loop
                                                       if row[chain_id_col] in alt_chain_id and int(row[seq_id_col]) == seq_id
                                                       and row[comp_id_col] == comp_id and row[atom_id_col] == atom_id)

                                            row[ambig_code_col] = allowed_ambig_code

                                            row = next(row for row in loop
                                                       if row[chain_id_col] in alt_chain_id and int(row[seq_id_col]) == seq_id2
                                                       and row[comp_id_col] == comp_id2 and row[atom_id_col] == atom_id2)

                                            row[ambig_code_col] = allowed_ambig_code

                                            modified = True

                                        else:

                                            err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id)\
                                                + f", {value_name} {value}, {ambig_code_name} {str(ambig_code)!r}, {ambig_set_id_name} {ambig_set_id}] "\
                                                f"However, {value_name} {value2} of "\
                                                + row_tmp % (chain_id2, seq_id2, comp_id2, atom_id2)\
                                                + " is noticeably diffrent from others in the set that share the same ambiguity code "\
                                                f"by {value2 - value:.3f} (tolerance {CS_UNCERT_MAX})."

                                            self.report.error.appendDescription('invalid_ambiguity_code',
                                                                                {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                                 'description': err})
                                            self.report.setError()

                                            if self.__verbose:
                                                self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ ValueError  - {err}\n")

                    else:

                        err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id)\
                            + f"] Invalid ambiguity code {str(ambig_code)!r} (allowed ambig_code {ALLOWED_AMBIGUITY_CODES}) in a loop."

                        self.report.error.appendDescription('invalid_ambiguity_code',
                                                            {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                             'description': err})
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ ValueError  - {err}\n")

        except StopIteration:

            err = f"Assigned chemical shifts of {sf_framecode!r} saveframe was not parsed properly. Please fix problems reported."

            self.report.error.appendDescription('missing_mandatory_content',
                                                {'file_name': file_name, 'description': err})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Error  - {err}\n")

        except Exception as e:

            self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.validateCsValue() ++ Error  - " + str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write(f"+{self.__class_name__}.validateCsValue() ++ Error  - {str(e)}\n")

        return modified

    def testRdcVector(self, file_name: str, file_type: str, content_subtype: str, sf_framecode: str, lp_category: str):
        """ Perform consistency test on RDC bond vectors.
        """

        item_names = ITEM_NAMES_IN_RDC_LOOP[file_type]
        index_tag = INDEX_TAGS[file_type][content_subtype]
        chain_id_1_name = item_names['chain_id_1']
        chain_id_2_name = item_names['chain_id_2']
        seq_id_1_name = item_names['seq_id_1']
        seq_id_2_name = item_names['seq_id_2']
        comp_id_1_name = item_names['comp_id_1']
        comp_id_2_name = item_names['comp_id_2']
        atom_id_1_name = item_names['atom_id_1']
        atom_id_2_name = item_names['atom_id_2']

        def ext_atom_names(row):
            return (row[chain_id_1_name], row[chain_id_2_name],
                    row[seq_id_1_name], row[seq_id_2_name],
                    row[comp_id_1_name], row[comp_id_2_name],
                    row[atom_id_1_name], row[atom_id_2_name])

        try:

            lp_data = next((lp['data'] for lp in self.__lp_data[content_subtype]
                            if lp['file_name'] == file_name and lp['sf_framecode'] == sf_framecode), None)

            if lp_data is not None:

                for row in lp_data:
                    chain_id_1, chain_id_2, seq_id_1, seq_id_2, \
                        comp_id_1, comp_id_2, atom_id_1, atom_id_2 = ext_atom_names(row)

                    if atom_id_1 in emptyValue or atom_id_2 in emptyValue:
                        continue

                    if (atom_id_1[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS) or (atom_id_2[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS):

                        idx_msg = f"[Check row of {index_tag} {row[index_tag]}] " if index_tag in row else ''

                        err = idx_msg + "Non-magnetic susceptible spin appears in RDC vector; "\
                            f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                            f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2})."

                        self.report.error.appendDescription('invalid_data',
                                                            {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                             'description': err})
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write(f"+{self.__class_name__}.testRdcVector() ++ Error  - {err}\n")

                    if chain_id_1 != chain_id_2:

                        if self.__exptl_method == 'SOLID-STATE NMR' and self.__symmetric is None:

                            src_id = self.report.getInputSourceIdOfCoord()

                            if src_id >= 0:

                                cif_input_source = self.report.input_sources[src_id]
                                cif_input_source_dic = cif_input_source.get()

                                has_cif_poly_seq = has_key_value(cif_input_source_dic, 'polymer_sequence')

                                if has_cif_poly_seq:

                                    cif_poly_seq = cif_input_source_dic['polymer_sequence']

                                    self.__symmetric = 'no'

                                    for ps in cif_poly_seq:

                                        if 'identical_auth_chain_id' in ps:

                                            if len(ps['identical_auth_chain_id']) + 1 > 2:
                                                self.__symmetric = 'yes'

                        idx_msg = f"[Check row of {index_tag} {row[index_tag]}] " if index_tag in row else ''

                        if self.__symmetric == 'no':

                            err = idx_msg + "Found inter-chain RDC vector; "\
                                f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}) in a loop {lp_category}."

                            self.report.error.appendDescription('invalid_data',
                                                                {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                 'description': err})
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write(f"+{self.__class_name__}.testRdcVector() ++ Error  - {err}\n")

                        else:

                            err = idx_msg + "Found inter-chain RDC vector; "\
                                f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}) in a loop {lp_category}. "\
                                "However, it might be an artificial RDC constraint on solid-state NMR applied to symmetric samples such as fibrils.\n"

                            self.report.warning.appendDescription('anomalous_rdc_vector',
                                                                  {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                   'description': err})
                            self.report.setWarning()

                            if self.__verbose:
                                self.__lfh.write(f"+{self.__class_name__}.testRdcVector() ++ Warning  - {err}\n")

                    elif abs(seq_id_1 - seq_id_2) > 1:

                        idx_msg = f"[Check row of {index_tag} {row[index_tag]}] " if index_tag in row else ''

                        err = idx_msg + "Found inter-residue RDC vector; "\
                            f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}) in a loop {lp_category}."

                        self.report.error.appendDescription('invalid_data',
                                                            {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                             'description': err})
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write(f"+{self.__class_name__}.testRdcVector() ++ Error  - {err}\n")

                    elif abs(seq_id_1 - seq_id_2) == 1:

                        if self.__csStat.peptideLike(comp_id_1) and self.__csStat.peptideLike(comp_id_2)\
                           and ((seq_id_1 < seq_id_2 and atom_id_1 == 'C' and atom_id_2 in rdcBbPairCode)
                                or (seq_id_1 > seq_id_2 and atom_id_1 in rdcBbPairCode and atom_id_2 == 'C')
                                or (seq_id_1 < seq_id_2 and atom_id_1.startswith('HA') and atom_id_2 == 'H')
                                or (seq_id_1 > seq_id_2 and atom_id_1 == 'H' and atom_id_2.startswith('HA'))):
                            pass

                        else:

                            idx_msg = f"[Check row of {index_tag} {row[index_tag]}] " if index_tag in row else ''

                            err = idx_msg + "Found inter-residue RDC vector; "\
                                f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}) in a loop {lp_category}."

                            self.report.error.appendDescription('invalid_data',
                                                                {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                 'description': err})
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write(f"+{self.__class_name__}.testRdcVector() ++ Error  - {err}\n")

                    elif atom_id_1 == atom_id_2:

                        idx_msg = f"[Check row of {index_tag} {row[index_tag]}] " if index_tag in row else ''

                        err = idx_msg + "Found zero RDC vector; "\
                            f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2})."

                        self.report.error.appendDescription('invalid_data',
                                                            {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                             'description': err})
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write(f"+{self.__class_name__}.testRdcVector() ++ Error  - {err}\n")

                    else:

                        if self.__ccU.updateChemCompDict(comp_id_1):  # matches with comp_id in CCD

                            if not self.__ccU.hasBond(comp_id_1, atom_id_1, atom_id_2):

                                if self.__nefT.validate_comp_atom(comp_id_1, atom_id_1) and self.__nefT.validate_comp_atom(comp_id_2, atom_id_2):

                                    idx_msg = f"[Check row of {index_tag} {row[index_tag]}] " if index_tag in row else ''

                                    warn = idx_msg + "Found an RDC vector over multiple covalent bonds; "\
                                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2})."

                                    self.report.warning.appendDescription('unusual/rare_data',
                                                                          {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                           'description': warn})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.testRdcVector() ++ Warning  - {warn}\n")

                                else:  # raised error already somewhere because of invalid atom nomenclature
                                    pass

                        else:  # raised warning already somewhere because of unknown comp_id
                            pass

        except Exception as e:

            self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.testRdcVector() ++ Error  - " + str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write(f"+{self.__class_name__}.testRdcVector() ++ Error  - {str(e)}\n")

    def testCoordCovalentBond(self, file_name: str, file_type: str, content_subtype: str, sf_framecode: str, lp_category: str):
        """ Perform consistency test on covalent bonds.
        """

        item_names = ITEM_NAMES_IN_RDC_LOOP[file_type]
        chain_id_1_name = item_names['chain_id_1']
        chain_id_2_name = item_names['chain_id_2']
        seq_id_1_name = item_names['seq_id_1']
        seq_id_2_name = item_names['seq_id_2']
        comp_id_1_name = item_names['comp_id_1']
        comp_id_2_name = item_names['comp_id_2']
        atom_id_1_name = item_names['atom_id_1']
        atom_id_2_name = item_names['atom_id_2']

        def ext_atom_names(row):
            return (row[chain_id_1_name], row[chain_id_2_name],
                    row[seq_id_1_name], row[seq_id_2_name],
                    row[comp_id_1_name], row[comp_id_2_name],
                    row[atom_id_1_name], row[atom_id_2_name])

        try:

            aux_data = next((lp['data'] for lp in self.__aux_data[content_subtype]
                             if lp['file_name'] == file_name and lp['sf_framecode'] == sf_framecode
                             and lp['category'] == lp_category), None)

            if aux_data is not None:

                for row in aux_data:
                    chain_id_1, chain_id_2, seq_id_1, seq_id_2, \
                        comp_id_1, comp_id_2, atom_id_1, atom_id_2 = ext_atom_names(row)

                    bond = self.getNmrBondLength(chain_id_1, seq_id_1, atom_id_1, chain_id_2, seq_id_2, atom_id_2)

                    if bond is None:
                        continue

                    broken_bond = [b for b in bond if b['distance'] > CUTOFF_BOND_LENGTH]

                    if len(broken_bond) == 0:
                        continue

                    length_list = ''
                    for bb in broken_bond:
                        length_list += f"{bb['distance']} (model_id {bb['model_id']}), "

                    warn = "Covalent bond ("\
                        + self.getReducedAtomNotation(chain_id_1_name, chain_id_1, seq_id_1_name, seq_id_1, comp_id_1_name, comp_id_1, atom_id_1_name, atom_id_1)\
                        + " - "\
                        + self.getReducedAtomNotation(chain_id_2_name, chain_id_2, seq_id_2_name, seq_id_2, comp_id_2_name, comp_id_2, atom_id_2_name, atom_id_2)\
                        + f") is out of acceptable range, {length_list[:-2]}Å."

                    self.report.warning.appendDescription('anomalous_bond_length',
                                                          {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                           'description': warn})
                    self.report.setWarning()

                    if self.__verbose:
                        self.__lfh.write(f"+{self.__class_name__}.testCoordCovalentBond() ++ Warning  - {warn}\n")

        except Exception as e:

            self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.testCoordCovalentBond() ++ Error  - " + str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write(f"+{self.__class_name__}.testCoordCovalentBond() ++ Error  - {str(e)}\n")

    def testResidueVariant(self, file_name: str, file_type: str, content_subtype: str,
                           sf: Union[pynmrstar.Saveframe, pynmrstar.Loop],
                           sf_framecode: str, lp_category: str, cif_poly_seq: List[dict], nmr2ca: dict):
        """ Perform consistency test on residue variants.
        """

        item_names = ITEM_NAMES_IN_CS_LOOP[file_type]
        chain_id_name = item_names['chain_id']
        seq_id_name = item_names['seq_id']
        comp_id_name = item_names['comp_id']
        atom_id_name = item_names['atom_id']
        variant_name = 'residue_variant' if file_type == 'nef' else item_names['atom_id']

        key_items = self.aux_key_items[file_type][content_subtype][lp_category]
        data_items = self.aux_data_items[file_type][content_subtype][lp_category]
        allowed_tags = AUX_ALLOWED_TAGS[file_type][content_subtype][lp_category]

        try:

            aux_data = self.__nefT.check_data(sf, lp_category, key_items, data_items,
                                              allowed_tags, None, None,
                                              enforce_allowed_tags=(file_type == 'nmr-star'),
                                              excl_missing_data=self.__excl_missing_data)[0]

            if aux_data is not None:

                for row in aux_data:
                    chain_id = row[chain_id_name]
                    seq_id = row[seq_id_name]
                    comp_id = row[comp_id_name]
                    variant = row[variant_name]

                    if chain_id not in nmr2ca:
                        continue

                    ca = next((ca['seq_align'] for ca in nmr2ca[chain_id] if ('seq_unmap' not in ca or (seq_id not in ca['seq_unmap']))), None)  # DAOTHER-7465

                    if ca is None:
                        continue

                    cif_chain_id = ca['test_chain_id']

                    cif_seq_id = next((test_seq_id for ref_seq_id, test_seq_id
                                       in zip(ca['ref_seq_id'], ca['test_seq_id']) if ref_seq_id == seq_id), None)

                    if cif_seq_id is None:
                        continue

                    cif_ps = next(ps for ps in cif_poly_seq if ps['chain_id'] == cif_chain_id)

                    cif_comp_id = next((_comp_id for _seq_id, _comp_id
                                        in zip(cif_ps['seq_id'], cif_ps['comp_id']) if _seq_id == cif_seq_id), None)

                    if cif_comp_id is None:
                        continue

                    seq_key = (cif_chain_id, cif_seq_id)

                    if seq_key in self.__caC['coord_unobs_res']:  # DAOTHER-7665
                        continue

                    coord_atom_site_ = self.__caC['coord_atom_site'].get(seq_key)

                    self.__ccU.updateChemCompDict(comp_id)

                    if file_type == 'nef':

                        if variant in emptyValue:
                            continue

                        for _variant in variant.split(','):
                            _variant_ = _variant.strip(' ')

                            if _variant_[0] not in ('-', '+'):

                                warn = f"Residue variant {_variant_!r} should start with either '-' or '+' symbol according to the NEF sepcification."

                                self.report.warning.appendDescription('atom_nomenclature_mismatch',
                                                                      {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                       'description': warn})
                                self.report.setWarning()

                                if self.__verbose:
                                    self.__lfh.write(f"+{self.__class_name__}.textResidueVariant() ++ Warning  - {warn}\n")

                                continue

                            atom_id = _variant_[1:]

                            if file_type == 'nef' or self.isNmrAtomName(comp_id, atom_id):
                                _atom_id, _, details = self.__getAtomIdListWithAmbigCode(comp_id, atom_id)

                                len_atom_id = len(_atom_id)

                                if len_atom_id == 0:
                                    continue

                                if len_atom_id == 1 and atom_id == _atom_id[0]:
                                    atom_id_ = atom_id
                                    atom_name = atom_id

                                    if details is not None:
                                        atom_name += f", where {details.rstrip('.')}"

                                else:
                                    atom_name = f'{atom_id} (e.g. '

                                    for atom_id_ in _atom_id:
                                        atom_name += f'{atom_id_} '

                                    atom_name = f'{atom_name.rstrip()})'

                                    # representative atom id
                                    atom_id_ = _atom_id[0]

                            else:
                                atom_id_ = atom_id
                                atom_name = atom_id

                            if _variant_[0] == '-':

                                if self.__ccU.lastStatus:  # matches with comp_id in CCD

                                    if not self.__nefT.validate_comp_atom(comp_id, atom_id_):

                                        warn = "Atom ("\
                                            + self.getReducedAtomNotation(chain_id_name, chain_id, seq_id_name, seq_id, comp_id_name, comp_id, atom_id_name, atom_name)\
                                            + f", {variant_name} {_variant_!r}) did not match with chemical component dictionary (CCD)."

                                        self.report.warning.appendDescription('atom_nomenclature_mismatch',
                                                                              {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                               'description': warn})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.textResidueVariant() ++ Warning  - {warn}\n")

                                if coord_atom_site_ is not None and coord_atom_site_['comp_id'] == cif_comp_id\
                                   and (atom_id_ in coord_atom_site_['atom_id']
                                        or ('auth_atom_id' in coord_atom_site_ and atom_id_ in coord_atom_site_['auth_atom_id']))\
                                   and lp_category != '_Entity_deleted_atom':

                                    err = "Atom ("\
                                        + self.getReducedAtomNotation(chain_id_name, chain_id, seq_id_name, seq_id, comp_id_name, comp_id, atom_id_name, atom_name)\
                                        + f", {variant_name} {_variant_!r}) is unexpectedly incorporated in the coordinates."

                                    self.report.error.appendDescription('invalid_atom_nomenclature',
                                                                        {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                         'description': err})
                                    self.report.setError()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.testResidueVariant() ++ Error  - {err}\n")

                            else:

                                if coord_atom_site_ is not None and coord_atom_site_['comp_id'] == cif_comp_id\
                                   and (atom_id_ not in coord_atom_site_['atom_id']
                                        and (('auth_atom_id' in coord_atom_site_ and atom_id_ not in coord_atom_site_['auth_atom_id'])
                                             or 'auth_atom_id' not in coord_atom_site_)):

                                    err = "Atom ("\
                                        + self.getReducedAtomNotation(chain_id_name, chain_id, seq_id_name, seq_id, comp_id_name, comp_id, atom_id_name, atom_name)\
                                        + f") which is a {variant_name} {_variant_!r} is not present in the coordinates."

                                    checked = False
                                    if atom_id_[0] in protonBeginCode:
                                        cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == atom_id_), None)
                                        bonded_to = self.__ccU.getBondedAtoms(comp_id, atom_id_)
                                        peptide_like = self.__csStat.peptideLike(comp_id)
                                        if cca is not None and len(bonded_to) > 0:
                                            if coord_atom_site_ is not None and bonded_to[0] in coord_atom_site_['atom_id']\
                                               and (cca[self.__ccU.ccaLeavingAtomFlag] != 'Y'
                                                    or (peptide_like
                                                        and cca[self.__ccU.ccaNTerminalAtomFlag] == 'N'
                                                        and cca[self.__ccU.ccaCTerminalAtomFlag] == 'N')):
                                                checked = True
                                                err = "Atom ("\
                                                    + self.getReducedAtomNotation(chain_id_name, chain_id, seq_id_name, seq_id, comp_id_name, comp_id, atom_id_name, atom_name)\
                                                    + f") which is a {variant_name} {_variant_!r} is not properly instantiated in the coordinates. Please re-upload the model file."

                                    if self.__remediation_mode and checked:
                                        continue

                                    if content_subtype.startswith('spectral_peak'):

                                        self.report.warning.appendDescription('hydrogen_not_instantiated' if checked else 'assigned_peak_atom_not_found',
                                                                              {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                               'description': err})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.testResidueVariant() ++ Warning  - {err}\n")

                                    else:

                                        self.report.error.appendDescription('hydrogen_not_instantiated' if checked else 'atom_not_found',
                                                                            {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                             'description': err})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.testResidueVariant() ++ Error  - {err}\n")

                    else:

                        atom_id = variant

                        if file_type == 'nef' or self.isNmrAtomName(comp_id, atom_id):
                            _atom_id, _, details = self.__getAtomIdListWithAmbigCode(comp_id, atom_id)

                            len_atom_id = len(_atom_id)

                            if len_atom_id == 0:
                                continue

                            if len_atom_id == 1 and atom_id == _atom_id[0]:
                                atom_id_ = atom_id
                                atom_name = atom_id

                                if details is not None:
                                    atom_name += f", where {details.rstrip('.')}"

                            else:
                                atom_name = f'{atom_id} (e.g. '

                                for atom_id_ in _atom_id:
                                    atom_name += f'{atom_id_} '

                                atom_name = f'{atom_name.rstrip()})'

                                # representative atom id
                                atom_id_ = _atom_id[0]

                        else:
                            atom_id_ = atom_id
                            atom_name = atom_id

                            if self.__ccU.lastStatus:  # matches with comp_id in CCD

                                if not self.__nefT.validate_comp_atom(comp_id, atom_id_):

                                    warn = "Atom ("\
                                        + self.getReducedAtomNotation(chain_id_name, chain_id, seq_id_name, seq_id, comp_id_name, comp_id, atom_id_name, atom_name)\
                                        + ") did not match with chemical component dictionary (CCD)."

                                    self.report.warning.appendDescription('atom_nomenclature_mismatch',
                                                                          {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                           'description': warn})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.textResidueVariant() ++ Warning  - {warn}\n")

                            if coord_atom_site_ is not None and coord_atom_site_['comp_id'] == cif_comp_id\
                               and (atom_id_ in coord_atom_site_['atom_id']
                                    and (('auth_atom_id' in coord_atom_site_ and atom_id_ in coord_atom_site_['auth_atom_id'])
                                         or 'auth_atom_id' not in coord_atom_site_))\
                               and lp_category != '_Entity_deleted_atom':

                                err = "Atom ("\
                                    + self.getReducedAtomNotation(chain_id_name, chain_id, seq_id_name, seq_id, comp_id_name, comp_id, atom_id_name, atom_name)\
                                    + ") is unexpectedly incorporated in the coordinates."

                                self.report.error.appendDescription('invalid_atom_nomenclature',
                                                                    {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                     'description': err})
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write(f"+{self.__class_name__}.testResidueVariant() ++ Error  - {err}\n")

        except LookupError as e:

            item = 'format_issue' if 'Unauthorized' in str(e) else 'missing_mandatory_item'

            self.report.error.appendDescription(item,
                                                {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                 'description': str(e).strip("'")})
            self.report.setError()

            self.__lfh.write(f"+{self.__class_name__}.testResidueVariant() ++ LookupError  - "
                             f"{file_name} {sf_framecode} {lp_category} {str(e)}\n")

        except ValueError as e:

            self.report.error.appendDescription('invalid_data',
                                                {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                 'description': str(e).strip("'")})
            self.report.setError()

            if self.__verbose:
                self.__lfh.write(f"+{self.__class_name__}.testResidueVariant() ++ ValueError  - {str(e)}\n")

        except Exception as e:

            self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.testResidueVariant() ++ Error  - " + str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write(f"+{self.__class_name__}.testResidueVariant() ++ Error  - {str(e)}\n")

    def validateStrMr(self, file_list_id: int, file_type: str, original_file_name: str, content_subtype: str,
                      _sf: Union[pynmrstar.Saveframe, pynmrstar.Loop],
                      sf_framecode: str, lp_category: str) -> bool:
        """ Validate data content of NMR-STAR restraint files.
        """

        self.__list_id_counter = incListIdCounter(content_subtype, self.__list_id_counter, reduced=False)

        list_id = self.__list_id_counter[content_subtype]

        restraint_name = getRestraintName(content_subtype)

        _sf_framecode = sf_framecode

        is_sf = True
        if len(sf_framecode) == 0:
            sf_framecode = restraint_name.replace(' ', '_').lower() + f'_{list_id}'
            is_sf = False

        sf = getSaveframe(content_subtype, sf_framecode, list_id, self.__entry_id, original_file_name,
                          reduced=False)

        # merge saveframe tags of the source saveframe
        if is_sf:

            origTagNames = [t[0] for t in _sf.tags]
            tagNames = [t[0] for t in sf.tags]

            for idx, origTagName in enumerate(origTagNames):
                if origTagName in SF_ALLOWED_TAGS[file_type][content_subtype]:
                    set_sf_tag(sf, origTagName, _sf.tags[idx][1])

        try:

            loop = _sf if self.__star_data_type[file_list_id] == 'Loop' else _sf.get_loop(lp_category)

            if not isinstance(loop, pynmrstar.Loop):
                loop = None

        except KeyError:
            loop = None

        _restraint_name = restraint_name.split()

        sf_item = {'file_type': file_type, 'saveframe': sf, 'list_id': list_id,
                   'id': 0, 'index_id': 0,
                   'constraint_type': ' '.join(_restraint_name[:-1])}

        if content_subtype == 'dist_restraint':
            sf_item['constraint_subsubtype'] = 'simple'

        if loop is not None:

            input_source = self.report.input_sources[file_list_id]
            input_source_dic = input_source.get()

            has_poly_seq_in_lp = has_key_value(input_source_dic, 'polymer_sequence_in_loop')

            if has_poly_seq_in_lp and content_subtype != 'ph_param_data':
                poly_seq_in_lp = input_source_dic['polymer_sequence_in_loop']

                poly_seq = seq_align = chain_assign = br_seq_align = br_chain_assign = np_seq_align = np_chain_assign = None

                if has_poly_seq_in_lp and content_subtype in poly_seq_in_lp:
                    _poly_seq_in_lp = next((_poly_seq_in_lp for _poly_seq_in_lp in poly_seq_in_lp[content_subtype]
                                            if _poly_seq_in_lp['sf_framecode'] == _sf_framecode), None)

                    if _poly_seq_in_lp is not None:
                        list_id = _poly_seq_in_lp['list_id']
                        poly_seq = _poly_seq_in_lp['polymer_sequence']

                        seq_align, _ = alignPolymerSequence(self.__pA, self.__caC['polymer_sequence'], poly_seq, conservative=False)
                        chain_assign, _ = assignPolymerSequence(self.__pA, self.__ccU, file_type, self.__caC['polymer_sequence'], poly_seq, seq_align)

                        if self.__caC['branched'] is not None:
                            br_seq_align, _ = alignPolymerSequence(self.__pA, self.__caC['branched'], poly_seq, conservative=False)
                            br_chain_assign, _ = assignPolymerSequence(self.__pA, self.__ccU, file_type, self.__caC['branched'], poly_seq, br_seq_align)

                        if self.__caC['non_polymer'] is not None:
                            np_seq_align, _ = alignPolymerSequence(self.__pA, self.__caC['non_polymer'], poly_seq, conservative=False)
                            np_chain_assign, _ = assignPolymerSequence(self.__pA, self.__ccU, file_type, self.__caC['non_polymer'], poly_seq, np_seq_align)

                def get_auth_seq_scheme(chain_id, seq_id):
                    auth_asym_id = auth_seq_id = None

                    if seq_id is not None:

                        if chain_assign is not None:
                            auth_asym_id = next((ca['ref_chain_id'] for ca in chain_assign if ca['test_chain_id'] == chain_id), None)
                            if auth_asym_id is not None:
                                sa = next((sa for sa in seq_align
                                           if sa['ref_chain_id'] == auth_asym_id and sa['test_chain_id'] == chain_id and seq_id in sa['test_seq_id']
                                           and sa['sequence_coverage'] >= LOW_SEQ_COVERAGE), None)
                                if sa is not None:
                                    _ref_seq_id_name = 'ref_auth_seq_id' if 'ref_auth_seq_id' in sa else 'ref_seq_id'
                                    auth_seq_id = next((ref_seq_id for ref_seq_id, test_seq_id in zip(sa[_ref_seq_id_name], sa['test_seq_id'])
                                                        if test_seq_id == seq_id), None)

                        if None in (auth_asym_id, auth_seq_id) and br_seq_align is not None:
                            auth_asym_id = next((ca['ref_chain_id'] for ca in br_chain_assign if ca['test_chain_id'] == chain_id), None)
                            if auth_asym_id is not None:
                                sa = next((sa for sa in br_seq_align
                                           if sa['ref_chain_id'] == auth_asym_id and sa['test_chain_id'] == chain_id and seq_id in sa['test_seq_id']
                                           and sa['sequence_coverage'] >= LOW_SEQ_COVERAGE), None)
                                if sa is not None:
                                    _ref_seq_id_name = 'ref_auth_seq_id' if 'ref_auth_seq_id' in sa else 'ref_seq_id'
                                    auth_seq_id = next((ref_seq_id for ref_seq_id, test_seq_id in zip(sa[_ref_seq_id_name], sa['test_seq_id'])
                                                        if test_seq_id == seq_id), None)

                        if None in (auth_asym_id, auth_seq_id) and np_seq_align is not None:
                            auth_asym_id = next((ca['ref_chain_id'] for ca in np_chain_assign if ca['test_chain_id'] == chain_id), None)
                            if auth_asym_id is not None:
                                sa = next((sa for sa in np_seq_align
                                           if sa['ref_chain_id'] == auth_asym_id and sa['test_chain_id'] == chain_id and seq_id in sa['test_seq_id']
                                           and sa['sequence_coverage'] >= LOW_SEQ_COVERAGE), None)
                                if sa is not None:
                                    _ref_seq_id_name = 'ref_auth_seq_id' if 'ref_auth_seq_id' in sa else 'ref_seq_id'
                                    auth_seq_id = next((ref_seq_id for ref_seq_id, test_seq_id in zip(sa[_ref_seq_id_name], sa['test_seq_id'])
                                                        if test_seq_id == seq_id), None)

                    return auth_asym_id, auth_seq_id

                has_ins_code = False

                if poly_seq is not None:

                    for ps in poly_seq:

                        if has_ins_code:
                            break

                        auth_asym_id, _ = get_auth_seq_scheme(ps['chain_id'], ps['seq_id'][0])

                        if self.__caC['polymer_sequence'] is not None\
                           and any(True for cif_ps in self.__caC['polymer_sequence']
                                   if cif_ps['auth_chain_id'] == auth_asym_id and 'ins_code' in cif_ps):
                            has_ins_code = True

                        if self.__caC['branched'] is not None\
                           and any(True for cif_ps in self.__caC['branched']
                                   if cif_ps['auth_chain_id'] == auth_asym_id and 'ins_code' in cif_ps):
                            has_ins_code = True

                        if self.__caC['non_polymer'] is not None\
                           and any(True for cif_ps in self.__caC['non_polymer']
                                   if cif_ps['auth_chain_id'] == auth_asym_id and 'ins_code' in cif_ps):
                            has_ins_code = True

                lp = getLoop(content_subtype, reduced=False, hasInsCode=has_ins_code)

                sf.add_loop(lp)
                sf_item['loop'] = lp

                index_tag = INDEX_TAGS[file_type][content_subtype]
                id_col = loop.tags.index('ID') if 'ID' in loop.tags else -1
                combination_id_col = member_id_col = member_logic_code_col = upper_limit_col = -1
                auth_comp_id_1_col = auth_comp_id_2_col = torsion_angle_name_col = -1
                if content_subtype == 'dist_restraint':
                    if 'Combination_ID' in loop.tags:
                        combination_id_col = loop.tags.index('Combination_ID')
                    if 'Member_ID' in loop.tags:
                        member_id_col = loop.tags.index('Member_ID')
                    if 'Member_logic_code' in loop.tags:
                        member_logic_code_col = loop.tags.index('Member_logic_code')
                    if 'Distance_upper_bound_val' in loop.tags:
                        upper_limit_col = loop.tags.index('Distance_upper_bound_val')
                    if 'Auth_comp_ID_1' in loop.tags:
                        auth_comp_id_1_col = loop.tags.index('Auth_comp_ID_1')
                    if 'Auth_comp_ID_2' in loop.tags:
                        auth_comp_id_2_col = loop.tags.index('Auth_comp_ID_2')
                elif content_subtype == 'dihed_restraint':
                    if 'Torsion_angle_name' in loop.tags:
                        torsion_angle_name_col = loop.tags.index('Torsion_angle_name')

                key_items = [item['name'] for item in NMR_STAR_LP_KEY_ITEMS[content_subtype]]

                if content_subtype == 'ccr_dd_restraint' and 'Dipole_2_chem_comp_index_ID_2' in loop.tags:
                    key_items = copy.copy(key_items)
                    key_item = next((key_item for key_item in key_items if key_item['name'] == 'Dipole_2_comp_index_ID_2'), None)
                    if key_item is not None:
                        key_item['name'] = 'Dipole_2_chem_comp_index_ID_2'

                len_key_items = len(key_items)

                atom_dim_num = (len_key_items - 1) // 5  # 5 for entity_assembly_id, entity_id, comp_index_id, comp_id, atom_id tags

                if atom_dim_num == 0:
                    err = f"Unexpected key items {key_items} set for processing {lp_category} loop in {sf_framecode} saveframe of {original_file_name} file."

                    self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.validateStrMr() ++ KeyError  - " + err)
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write(f"+{self.__class_name__}.validateStrMr() ++ KeyError  - {err}\n")

                    return False

                key_chain_id_names = [key_items[idx] for idx in range(1, len_key_items, 5)]
                key_entity_id_names = [key_items[idx] for idx in range(2, len_key_items, 5)]
                key_seq_id_names = [key_items[idx] for idx in range(3, len_key_items, 5)]
                key_comp_id_names = [key_items[idx] for idx in range(4, len_key_items, 5)]
                key_atom_id_names = [key_items[idx] for idx in range(5, len_key_items, 5)]

                key_tags = key_chain_id_names
                key_tags.extend(key_seq_id_names)
                key_tags.extend(key_comp_id_names)
                key_tags.extend(key_atom_id_names)

                auth_items = [auth_item['name'] for auth_item in NMR_STAR_LP_DATA_ITEMS[content_subtype]
                              if auth_item['name'].startswith('Auth') or 'auth' in auth_item['name']]

                auth_chain_id_names = [auth_item for auth_item in auth_items if 'asym' in auth_item or 'entity_assembly' in auth_item]
                auth_seq_id_names = [auth_item for auth_item in auth_items if 'seq' in auth_item]
                auth_comp_id_names = [auth_item for auth_item in auth_items if 'comp' in auth_item]
                auth_atom_id_names = [auth_item for auth_item in auth_items if 'atom' in auth_item and 'atom_name' not in auth_item]
                auth_atom_name_names = [auth_item for auth_item in auth_items if 'atom_name' in auth_item]

                auth_pdb_tags = auth_chain_id_names
                auth_pdb_tags.extend(auth_seq_id_names)
                auth_pdb_tags.extend(auth_comp_id_names)
                auth_pdb_tags.extend(auth_atom_id_names)

                coord_atom_site = self.__caC['coord_atom_site']
                auth_to_star_seq = self.__caC['auth_to_star_seq']
                auth_to_orig_seq = self.__caC['auth_to_orig_seq']
                auth_to_ins_code = self.__caC['auth_to_ins_code'] if has_ins_code else None
                auth_to_star_seq_ann = self.__caC['auth_to_star_seq_ann']
                auth_atom_name_to_id = self.__caC['auth_atom_name_to_id']

                model_num_name = 'pdbx_PDB_model_num' if 'pdbx_PDB_model_num' in self.__coord_atom_site_tags else 'ndb_model'

                # split concatination of auth_seq_id and ins_code (DAOTHER-10418)
                if auth_to_ins_code is not None and len(auth_to_ins_code) > 0\
                   and set(auth_seq_id_names) & set(loop.tags) == set(auth_seq_id_names):
                    auth_dat = loop.get_tag(auth_seq_id_names)

                    if any(True for row in auth_dat if any(True for val in row if isinstance(val, str))):

                        auth_seq_id_cols = [loop.tags.index(auth_seq_id_name) for auth_seq_id_name in auth_seq_id_names]

                        ins_code_names = [auth_item['name'] for auth_item in NMR_STAR_LP_DATA_ITEMS_INS_CODE[content_subtype]
                                          if auth_item['name'].startswith('PDB_ins_code')]

                        for ins_code_name in ins_code_names:
                            if ins_code_name not in loop.tags:
                                loop.add_tag(ins_code_name, update_data=True)

                        ins_code_cols = [loop.tags.index(ins_code_name) for ins_code_name in ins_code_names]

                        for idx, row in enumerate(auth_dat):
                            for col, val in enumerate(row):
                                if isinstance(val, str) and concat_seq_id_ins_code_pattern.match(val):
                                    g = concat_seq_id_ins_code_pattern.search(val).groups()
                                    loop.data[idx][auth_seq_id_cols[col]] = g[0]
                                    if g[1] not in emptyValue:
                                        loop.data[idx][ins_code_cols[col]] = g[1]

                offset_holder = {}

                has_key_seq = False

                if set(key_tags) & set(loop.tags) == set(key_tags):
                    dat = loop.get_tag(key_seq_id_names)
                    if len(dat) > 0:
                        has_key_seq = True
                        for row in dat:
                            try:
                                for d in range(atom_dim_num):
                                    int(row[d])
                            except (ValueError, TypeError):
                                has_key_seq = False
                                break

                has_auth_seq = valid_auth_seq = False

                if set(auth_pdb_tags) & set(loop.tags) == set(auth_pdb_tags):
                    auth_dat = loop.get_tag(auth_pdb_tags)
                    if len(auth_dat) > 0:
                        has_auth_seq = valid_auth_seq = True
                        if not self.__annotation_mode:
                            for row in auth_dat:
                                try:
                                    for d in range(atom_dim_num):
                                        seq_key = (row[d], int(row[atom_dim_num + d]), row[atom_dim_num * 2 + d])
                                        if seq_key not in auth_to_star_seq_ann:
                                            valid_auth_seq = False
                                            break
                                    if not valid_auth_seq:
                                        break
                                except (ValueError, TypeError):
                                    has_auth_seq = valid_auth_seq = False
                                    break

                if has_key_seq or has_auth_seq:

                    has_auth_atom_name = len(auth_atom_name_names) > 0 and set(auth_atom_name_names) & set(loop.tags) == set(auth_atom_name_names)

                    if valid_auth_seq:

                        if has_auth_atom_name:
                            auth_pdb_tags.extend(auth_atom_name_names)

                        dat = loop.get_tag(auth_pdb_tags)

                        prefer_auth_atom_name = False

                        if (self.__annotation_mode or self.__native_combined) and len(auth_atom_name_to_id) > 0:

                            count_auth_name = count_auth_id = 0

                            for row_ in dat:

                                for d in range(atom_dim_num):
                                    chain_id = row_[d]
                                    seq_id = int(row_[atom_dim_num + d])
                                    comp_id = row_[atom_dim_num * 2 + d]
                                    atom_id = row_[atom_dim_num * 3 + d]

                                    seq_key = (chain_id, seq_id, comp_id)

                                    try:
                                        auth_to_star_seq[seq_key]  # pylint: disable=pointless-statement
                                    except KeyError:
                                        comp_id = next((_auth_comp_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                        if _auth_asym_id == chain_id and _auth_seq_id == seq_id), comp_id)

                                    if comp_id in auth_atom_name_to_id:
                                        if atom_id in auth_atom_name_to_id[comp_id]:
                                            count_auth_name += 1
                                        if atom_id in auth_atom_name_to_id[comp_id].values():
                                            count_auth_id += 1

                            if count_auth_name + count_auth_id == 0:

                                for row_ in dat:

                                    for d in range(atom_dim_num):
                                        chain_id = row_[d]
                                        seq_id = int(row_[atom_dim_num + d])
                                        comp_id = row_[atom_dim_num * 2 + d]
                                        atom_id = row_[atom_dim_num * 3 + d]

                                        seq_key = (chain_id, seq_id, comp_id)

                                        try:
                                            auth_to_star_seq_ann[seq_key]  # pylint: disable=pointless-statement
                                            _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                                            if _seq_key in coord_atom_site:  # DAOTHER-8817
                                                comp_id = coord_atom_site[_seq_key]['comp_id']
                                        except KeyError:
                                            continue

                                        if comp_id in auth_atom_name_to_id:
                                            if atom_id in auth_atom_name_to_id[comp_id]:
                                                count_auth_name += 1
                                            if atom_id in auth_atom_name_to_id[comp_id].values():
                                                count_auth_id += 1

                            prefer_auth_atom_name = count_auth_name > count_auth_id

                        for idx, row_ in enumerate(dat):
                            atom_sels = [None] * atom_dim_num

                            for d in range(atom_dim_num):
                                chain_id = auth_chain_id = row_[d]
                                seq_id = int(row_[atom_dim_num + d])
                                comp_id = row_[atom_dim_num * 2 + d]
                                atom_id = row_[atom_dim_num * 3 + d]

                                seq_key = (chain_id, seq_id, comp_id)

                                try:

                                    entity_assembly_id, comp_index_id, _, _ = auth_to_star_seq[seq_key]  # pylint: disable=pointless-statement

                                    if self.__annotation_mode or self.__native_combined:
                                        _auth_asym_id, _auth_seq_id =\
                                            next(((k[0], k[1]) for k, v in auth_to_star_seq.items()
                                                  if v[0] == entity_assembly_id and v[1] == comp_index_id and k[2] == comp_id), (None, None))
                                        if _auth_asym_id is not None:
                                            seq_key = (_auth_asym_id, _auth_seq_id, comp_id)
                                            if seq_key in auth_to_star_seq:
                                                chain_id, seq_id = _auth_asym_id, _auth_seq_id

                                except KeyError:
                                    if self.__annotation_mode or self.__native_combined:
                                        _auth_asym_id, _auth_seq_id =\
                                            next(((k[0], k[1]) for k, v in auth_to_star_seq.items()
                                                  if chain_id.isdigit() and v[0] == int(chain_id) and v[1] == seq_id and k[2] == comp_id), (None, None))
                                        if _auth_asym_id is not None:
                                            seq_key = (_auth_asym_id, _auth_seq_id, comp_id)
                                            if seq_key in auth_to_star_seq:
                                                chain_id, seq_id = _auth_asym_id, _auth_seq_id
                                        else:
                                            chain_id = next((_auth_asym_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                             if _auth_seq_id == seq_id and _auth_comp_id == comp_id), chain_id)
                                            seq_key = (chain_id, seq_id, comp_id)
                                            if seq_key in auth_to_star_seq:
                                                row_[d] = chain_id
                                            else:
                                                chain_id, comp_id =\
                                                    next(((_auth_asym_id, _auth_comp_id) for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                          if _auth_seq_id == seq_id), (chain_id, comp_id))
                                                seq_key = (chain_id, seq_id, comp_id)
                                                if seq_key in auth_to_star_seq:
                                                    row_[d] = chain_id
                                                    row_[atom_dim_num * 2 + d] = comp_id
                                        if seq_key not in auth_to_star_seq:
                                            comp_id = next((_auth_comp_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                            if _auth_asym_id == chain_id and _auth_seq_id == seq_id), comp_id)
                                            _auth_seq_id = next((_auth_seq_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                                 if _auth_asym_id == chain_id and _auth_comp_id == comp_id), None)
                                            if _auth_seq_id is not None:
                                                seq_key = (chain_id, _auth_seq_id, comp_id)

                                if has_auth_atom_name:
                                    auth_atom_id = row_[atom_dim_num * 4 + d]
                                    if auth_atom_id in emptyValue:
                                        auth_atom_id = atom_id
                                else:
                                    auth_atom_id = atom_id

                                _assign, warn = assignCoordPolymerSequenceWithChainId(self.__caC, self.__nefT, chain_id, seq_id, comp_id, atom_id)

                                rescued = False

                                if warn is not None:

                                    _index_tag = index_tag if index_tag is not None else 'ID'
                                    try:
                                        _index_tag_col = loop.tags.index(_index_tag)
                                        idx_msg = f"[Check row of {_index_tag} {loop.data[idx][_index_tag_col]}] "
                                    except ValueError:
                                        _index_tag = 'ID'
                                        try:
                                            _index_tag_col = loop.tags.index(_index_tag)
                                            idx_msg = f"[Check row of {_index_tag} {loop.data[idx][_index_tag_col]}] "
                                        except ValueError:
                                            _index_tag = 'Index_ID'
                                            idx_msg = f"[Check row of {_index_tag} {idx + 1}] "

                                    if warn.startswith('[Atom not found]'):
                                        if not self.__remediation_mode or 'Macromolecules page' not in warn:
                                            self.report.error.appendDescription('atom_not_found',
                                                                                {'file_name': original_file_name,
                                                                                 'sf_framecode': sf_framecode,
                                                                                 'category': lp_category,
                                                                                 'description': idx_msg + warn})
                                            self.report.setError()

                                            if self.__verbose:
                                                self.__lfh.write(f"+{self.__class_name__}.validateStrMr() ++ Error  - {idx_msg + warn}\n")

                                    if content_subtype != 'dihed_restraint' or not self.__remediation_mode:
                                        continue

                                    if d not in (0, 3) or not warn.startswith('[Atom not found]'):
                                        _d = 1 if d == 0 else 2
                                        _chain_id = row_[_d]
                                        _seq_id = int(row_[atom_dim_num + _d])
                                        _comp_id = row_[atom_dim_num * 2 + _d]
                                        _atom_id = row_[atom_dim_num * 3 + _d]

                                        if chain_id != _chain_id or abs(seq_id - _seq_id) != 1:
                                            continue

                                        if not self.__ccU.updateChemCompDict(comp_id.upper()):
                                            continue

                                        cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == atom_id.upper()), None)

                                        if cca is None:
                                            continue

                                        __assign, _warn = assignCoordPolymerSequenceWithChainId(self.__caC, self.__nefT, _chain_id, _seq_id, _comp_id, _atom_id)

                                        if len(__assign) != 1 or _warn is not None:
                                            continue

                                        chainId, cifSeqId, _, _ = __assign[0]
                                        cifSeqId -= _seq_id - seq_id

                                        atom_sels[d] = [{'chain_id': chainId,
                                                         'seq_id': cifSeqId,
                                                         'comp_id': comp_id.upper(),
                                                         'atom_id': atom_id.upper(),
                                                         'auth_atom_id': auth_atom_id}]
                                        warn = None

                                        rescued = True

                                if not rescued:
                                    enableWarning = True
                                    if content_subtype == 'dist_restraint':
                                        if (auth_comp_id_1_col != -1 and loop.data[idx][auth_comp_id_1_col] == 'HOH')\
                                           or (auth_comp_id_2_col != -1 and loop.data[idx][auth_comp_id_2_col] == 'HOH'):
                                            enableWarning = False
                                    elif content_subtype == 'dihed_restraint':
                                        if torsion_angle_name_col != -1 and loop.data[idx][torsion_angle_name_col] == 'PPA':
                                            enableWarning = False

                                    atom_sels[d], warn = selectCoordAtoms(self.__cR, self.__caC, self.__nefT, _assign, auth_chain_id, seq_id, comp_id, atom_id, auth_atom_id,
                                                                          allowAmbig=content_subtype in ('dist_restraint', 'noepk_restraint'),
                                                                          enableWarning=enableWarning,
                                                                          preferAuthAtomName=prefer_auth_atom_name and comp_id in auth_atom_name_to_id,
                                                                          representativeModelId=self.__representative_model_id, representativeAltId=self.__representative_alt_id,
                                                                          modelNumName=model_num_name)

                                if warn is not None:

                                    _index_tag = index_tag if index_tag is not None else 'ID'
                                    try:
                                        _index_tag_col = loop.tags.index(_index_tag)
                                        idx_msg = f"[Check row of {_index_tag} {loop.data[idx][_index_tag_col]}] "
                                    except ValueError:
                                        _index_tag = 'ID'
                                        try:
                                            _index_tag_col = loop.tags.index(_index_tag)
                                            idx_msg = f"[Check row of {_index_tag} {loop.data[idx][_index_tag_col]}] "
                                        except ValueError:
                                            _index_tag = 'Index_ID'
                                            idx_msg = f"[Check row of {_index_tag} {idx + 1}] "

                                    if warn.startswith('[Atom not found]'):
                                        if not self.__remediation_mode or 'Macromolecules page' not in warn:
                                            self.report.error.appendDescription('atom_not_found',
                                                                                {'file_name': original_file_name,
                                                                                 'sf_framecode': sf_framecode,
                                                                                 'category': lp_category,
                                                                                 'description': idx_msg + warn})
                                            self.report.setError()

                                            if self.__verbose:
                                                self.__lfh.write(f"+{self.__class_name__}.validateStrMr() ++ Error  - {idx_msg + warn}\n")

                                    elif warn.startswith('[Hydrogen not instantiated]'):
                                        self.report.warning.appendDescription('hydrogen_not_instantiated',
                                                                              {'file_name': original_file_name,
                                                                               'sf_framecode': sf_framecode,
                                                                               'category': lp_category,
                                                                               'description': idx_msg + warn})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.validateStrMr() ++ Warning  - {idx_msg + warn}\n")

                                    elif warn.startswith('[Invalid atom nomenclature]'):
                                        self.report.error.appendDescription('invalid_atom_nomenclature',
                                                                            {'file_name': original_file_name,
                                                                             'sf_framecode': sf_framecode,
                                                                             'category': lp_category,
                                                                             'description': idx_msg + warn})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.validateStrMr() ++ Error  - {idx_msg + warn}\n")

                                    elif warn.startswith('[Invalid atom selection]') or warn.startswith('[Invalid data]'):
                                        self.report.error.appendDescription('invalid_data',
                                                                            {'file_name': original_file_name,
                                                                             'sf_framecode': sf_framecode,
                                                                             'category': lp_category,
                                                                             'description': idx_msg + warn})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.validateStrMr() ++ ValueError  - {idx_msg + warn}\n")

                                    continue

                            if any(True for d in range(atom_dim_num) if atom_sels[d] is None or len(atom_sels[d]) == 0):
                                continue

                            sf_item['id'] += 1

                            if content_subtype == 'dist_restraint':
                                Id = '.'
                                if id_col != -1:
                                    Id = loop.data[idx][id_col]
                                    try:
                                        _Id = int(Id)
                                    except ValueError:
                                        Id = '.'
                                Id = sf_item['id'] if isinstance(Id, str) and Id == '.' else _Id
                                combinationId = '.'
                                if combination_id_col != -1:
                                    combinationId = loop.data[idx][combination_id_col]
                                    try:
                                        int(combinationId)
                                    except ValueError:
                                        combinationId = '.'
                                memberId = '.'
                                if member_id_col != -1:
                                    memberId = loop.data[idx][member_id_col]
                                    try:
                                        int(memberId)
                                    except ValueError:
                                        memberId = '.'
                                valid_atom_sels = atom_sels[0] is not None and atom_sels[1] is not None
                                if valid_atom_sels and len(atom_sels[0]) * len(atom_sels[1]) > 1\
                                   and (isAmbigAtomSelection(atom_sels[0], self.__csStat)
                                        or isAmbigAtomSelection(atom_sels[1], self.__csStat)):
                                    memberId = 0
                                memberLogicCode = '.'
                                if member_logic_code_col != -1:
                                    memberLogicCode = loop.data[idx][member_logic_code_col]
                                    if memberLogicCode in emptyValue:
                                        memberLogicCode = '.'
                                memberLogicCode = 'OR' if valid_atom_sels and len(atom_sels[0]) * len(atom_sels[1]) > 1 else memberLogicCode

                                if isinstance(memberId, int):
                                    _atom1 = _atom2 = None

                                if valid_atom_sels:
                                    for atom1, atom2 in itertools.product(atom_sels[0], atom_sels[1]):
                                        if isIdenticalRestraint([atom1, atom2]):
                                            continue
                                        if isinstance(memberId, int):
                                            if _atom1 is None or isAmbigAtomSelection([_atom1, atom1], self.__csStat)\
                                               or isAmbigAtomSelection([_atom2, atom2], self.__csStat):
                                                memberId += 1
                                                _atom1, _atom2 = atom1, atom2
                                        sf_item['index_id'] += 1
                                        _row = getRowForStrMr(content_subtype, Id, sf_item['index_id'],
                                                              memberId, memberLogicCode, list_id, self.__entry_id,
                                                              loop.tags, loop.data[idx],
                                                              auth_to_star_seq, auth_to_orig_seq, auth_to_ins_code, offset_holder,
                                                              [atom1, atom2], self.__annotation_mode)
                                        lp.add_data(_row)

                                elif atom_sels[0] is not None:
                                    atom2 = None
                                    for atom1 in atom_sels[0]:
                                        sf_item['index_id'] += 1
                                        _row = getRowForStrMr(content_subtype, Id, sf_item['index_id'],
                                                              memberId, memberLogicCode, list_id, self.__entry_id,
                                                              loop.tags, loop.data[idx],
                                                              auth_to_star_seq, auth_to_orig_seq, auth_to_ins_code, offset_holder,
                                                              [atom1, atom2], self.__annotation_mode)
                                        lp.add_data(_row)

                                elif atom_sels[1] is not None:
                                    atom1 = None
                                    for atom2 in atom_sels[1]:
                                        sf_item['index_id'] += 1
                                        _row = getRowForStrMr(content_subtype, Id, sf_item['index_id'],
                                                              memberId, memberLogicCode, list_id, self.__entry_id,
                                                              loop.tags, loop.data[idx],
                                                              auth_to_star_seq, auth_to_orig_seq, auth_to_ins_code, offset_holder,
                                                              [atom1, atom2], self.__annotation_mode)
                                        lp.add_data(_row)

                                else:
                                    atom1 = atom2 = None
                                    sf_item['index_id'] += 1
                                    _row = getRowForStrMr(content_subtype, Id, sf_item['index_id'],
                                                          memberId, memberLogicCode, list_id, self.__entry_id,
                                                          loop.tags, loop.data[idx],
                                                          auth_to_star_seq, auth_to_orig_seq, auth_to_ins_code, offset_holder,
                                                          [atom1, atom2], self.__annotation_mode)
                                    lp.add_data(_row)

                            else:

                                sf_item['index_id'] += 1
                                _row = getRowForStrMr(content_subtype, sf_item['id'], sf_item['index_id'],
                                                      None, None, list_id, self.__entry_id,
                                                      loop.tags, loop.data[idx],
                                                      auth_to_star_seq, auth_to_orig_seq, auth_to_ins_code, offset_holder,
                                                      atom_sels, self.__annotation_mode)
                                lp.add_data(_row)

                    else:

                        if has_auth_atom_name:
                            key_tags.extend(auth_atom_name_names)

                        dat = loop.get_tag(key_tags)

                        prefer_auth_atom_name = False

                        if (self.__annotation_mode or self.__native_combined) and len(auth_atom_name_to_id) > 0:

                            count_auth_name = count_auth_id = 0

                            for row_ in dat:

                                for d in range(atom_dim_num):
                                    chain_id = row_[d]
                                    seq_id = int(row_[atom_dim_num + d])
                                    comp_id = row_[atom_dim_num * 2 + d]
                                    atom_id = row_[atom_dim_num * 3 + d]

                                    seq_key = (chain_id, seq_id, comp_id)

                                    try:

                                        entity_assembly_id, comp_index_id, _, _ = auth_to_star_seq[seq_key]  # pylint: disable=pointless-statement

                                        _auth_asym_id, _auth_seq_id =\
                                            next(((k[0], k[1]) for k, v in auth_to_star_seq.items()
                                                  if v[0] == entity_assembly_id and v[1] == comp_index_id and k[2] == comp_id), (None, None))
                                        if _auth_asym_id is not None:
                                            seq_key = (_auth_asym_id, _auth_seq_id, comp_id)
                                            if seq_key in auth_to_star_seq:
                                                chain_id, seq_id = _auth_asym_id, _auth_seq_id

                                    except KeyError:
                                        _auth_asym_id, _auth_seq_id =\
                                            next(((k[0], k[1]) for k, v in auth_to_star_seq.items()
                                                  if chain_id.isdigit() and v[0] == int(chain_id) and v[1] == seq_id and k[2] == comp_id), (None, None))
                                        if _auth_asym_id is not None:
                                            seq_key = (_auth_asym_id, _auth_seq_id, comp_id)
                                            if seq_key in auth_to_star_seq:
                                                chain_id, seq_id = _auth_asym_id, _auth_seq_id
                                        else:
                                            chain_id = next((_auth_asym_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                             if _auth_seq_id == seq_id and _auth_comp_id == comp_id), chain_id)
                                            seq_key = (chain_id, seq_id, comp_id)
                                            if seq_key in auth_to_star_seq:
                                                row_[d] = chain_id
                                            else:
                                                chain_id, comp_id =\
                                                    next(((_auth_asym_id, _auth_comp_id) for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                          if _auth_seq_id == seq_id), (chain_id, comp_id))
                                                seq_key = (chain_id, seq_id, comp_id)
                                                if seq_key in auth_to_star_seq:
                                                    row_[d] = chain_id
                                                    row_[atom_dim_num * 2 + d] = comp_id
                                        if seq_key not in auth_to_star_seq:
                                            comp_id = next((_auth_comp_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                            if _auth_asym_id == chain_id and _auth_seq_id == seq_id), comp_id)
                                            _auth_seq_id = next((_auth_seq_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                                 if _auth_asym_id == chain_id and _auth_comp_id == comp_id), None)
                                            if _auth_seq_id is not None:
                                                seq_key = (chain_id, _auth_seq_id, comp_id)

                                    if comp_id in auth_atom_name_to_id:
                                        if atom_id in auth_atom_name_to_id[comp_id]:
                                            count_auth_name += 1
                                        if atom_id in auth_atom_name_to_id[comp_id].values():
                                            count_auth_id += 1

                            if count_auth_name + count_auth_id == 0:

                                for row_ in dat:

                                    for d in range(atom_dim_num):
                                        chain_id = row_[d]
                                        seq_id = int(row_[atom_dim_num + d])
                                        comp_id = row_[atom_dim_num * 2 + d]
                                        atom_id = row_[atom_dim_num * 3 + d]

                                        seq_key = (chain_id, seq_id, comp_id)

                                        try:
                                            auth_to_star_seq_ann[seq_key]  # pylint: disable=pointless-statement
                                            _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                                            if _seq_key in coord_atom_site:  # DAOTHER-8817
                                                comp_id = coord_atom_site[_seq_key]['comp_id']
                                        except KeyError:
                                            continue

                                        if comp_id in auth_atom_name_to_id:
                                            if atom_id in auth_atom_name_to_id[comp_id]:
                                                count_auth_name += 1
                                            if atom_id in auth_atom_name_to_id[comp_id].values():
                                                count_auth_id += 1

                            prefer_auth_atom_name = count_auth_name > count_auth_id

                        for idx, row_ in enumerate(dat):
                            atom_sels = [None] * atom_dim_num

                            for d in range(atom_dim_num):
                                chain_id = auth_chain_id = row_[d]
                                seq_id = int(row_[atom_dim_num + d])
                                comp_id = row_[atom_dim_num * 2 + d]
                                atom_id = row_[atom_dim_num * 3 + d]

                                seq_key = (chain_id, seq_id, comp_id)

                                try:

                                    entity_assembly_id, comp_index_id, _, _ = auth_to_star_seq[seq_key]  # pylint: disable=pointless-statement

                                    if self.__annotation_mode or self.__native_combined:
                                        _auth_asym_id, _auth_seq_id =\
                                            next(((k[0], k[1]) for k, v in auth_to_star_seq.items()
                                                  if v[0] == entity_assembly_id and v[1] == comp_index_id and k[2] == comp_id), (None, None))
                                        if _auth_asym_id is not None:
                                            seq_key = (_auth_asym_id, _auth_seq_id, comp_id)
                                            if seq_key in auth_to_star_seq:
                                                chain_id, seq_id = _auth_asym_id, _auth_seq_id

                                except KeyError:
                                    if self.__annotation_mode or self.__native_combined:
                                        _auth_asym_id, _auth_seq_id =\
                                            next(((k[0], k[1]) for k, v in auth_to_star_seq.items()
                                                  if chain_id.isdigit() and v[0] == int(chain_id) and v[1] == seq_id and k[2] == comp_id), (None, None))
                                        if _auth_asym_id is not None:
                                            seq_key = (_auth_asym_id, _auth_seq_id, comp_id)
                                            if seq_key in auth_to_star_seq:
                                                chain_id, seq_id = _auth_asym_id, _auth_seq_id
                                        else:
                                            chain_id = next((_auth_asym_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                             if _auth_seq_id == seq_id and _auth_comp_id == comp_id), chain_id)
                                            seq_key = (chain_id, seq_id, comp_id)
                                            if seq_key in auth_to_star_seq:
                                                row_[d] = chain_id
                                            else:
                                                chain_id, comp_id =\
                                                    next(((_auth_asym_id, _auth_comp_id) for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                          if _auth_seq_id == seq_id), (chain_id, comp_id))
                                                seq_key = (chain_id, seq_id, comp_id)
                                                if seq_key in auth_to_star_seq:
                                                    row_[d] = chain_id
                                                    row_[atom_dim_num * 2 + d] = comp_id
                                        if seq_key not in auth_to_star_seq:
                                            comp_id = next((_auth_comp_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                            if _auth_asym_id == chain_id and _auth_seq_id == seq_id), comp_id)
                                            _auth_seq_id = next((_auth_seq_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                                 if _auth_asym_id == chain_id and _auth_comp_id == comp_id), None)
                                            if _auth_seq_id is not None:
                                                seq_key = (chain_id, _auth_seq_id, comp_id)

                                if has_auth_atom_name:
                                    auth_atom_id = row_[atom_dim_num * 4 + d]
                                    if auth_atom_id in emptyValue:
                                        auth_atom_id = atom_id
                                else:
                                    auth_atom_id = atom_id

                                auth_asym_id = auth_seq_id = None

                                if chain_assign is not None:
                                    auth_asym_id = next((ca['ref_chain_id'] for ca in chain_assign if ca['test_chain_id'] == chain_id), None)
                                    if auth_asym_id is not None:
                                        sa = next((sa for sa in seq_align
                                                   if sa['ref_chain_id'] == auth_asym_id and sa['test_chain_id'] == chain_id and seq_id in sa['test_seq_id']), None)
                                        if sa is not None:
                                            _ref_seq_id_name = 'ref_auth_seq_id' if 'ref_auth_seq_id' in sa else 'ref_seq_id'
                                            auth_seq_id = next((ref_seq_id for ref_seq_id, test_seq_id in zip(sa[_ref_seq_id_name], sa['test_seq_id'])
                                                                if test_seq_id == seq_id), None)
                                            if auth_seq_id is None:
                                                for offset in range(1, 10):
                                                    auth_seq_id = next((ref_seq_id for ref_seq_id, test_seq_id in zip(sa[_ref_seq_id_name], sa['test_seq_id'])
                                                                        if test_seq_id == seq_id + offset), None)
                                                    if auth_seq_id is not None:
                                                        auth_seq_id -= offset
                                                        break
                                                    auth_seq_id = next((ref_seq_id for ref_seq_id, test_seq_id in zip(sa[_ref_seq_id_name], sa['test_seq_id'])
                                                                        if test_seq_id == seq_id - offset), None)
                                                    if auth_seq_id is not None:
                                                        auth_seq_id += offset
                                                        break

                                if None in (auth_asym_id, auth_seq_id) and br_seq_align is not None:
                                    auth_asym_id = next((ca['ref_chain_id'] for ca in br_chain_assign if ca['test_chain_id'] == chain_id), None)
                                    if auth_asym_id is not None:
                                        sa = next((sa for sa in br_seq_align
                                                   if sa['ref_chain_id'] == auth_asym_id and sa['test_chain_id'] == chain_id and seq_id in sa['test_seq_id']), None)
                                        if sa is not None:
                                            _ref_seq_id_name = 'ref_auth_seq_id' if 'ref_auth_seq_id' in sa else 'ref_seq_id'
                                            auth_seq_id = next((ref_seq_id for ref_seq_id, test_seq_id in zip(sa[_ref_seq_id_name], sa['test_seq_id'])
                                                                if test_seq_id == seq_id), None)

                                if None in (auth_asym_id, auth_seq_id) and np_seq_align is not None:
                                    auth_asym_id = next((ca['ref_chain_id'] for ca in np_chain_assign if ca['test_chain_id'] == chain_id), None)
                                    if auth_asym_id is not None:
                                        sa = next((sa for sa in np_seq_align
                                                   if sa['ref_chain_id'] == auth_asym_id and sa['test_chain_id'] == chain_id and seq_id in sa['test_seq_id']), None)
                                        if sa is not None:
                                            _ref_seq_id_name = 'ref_auth_seq_id' if 'ref_auth_seq_id' in sa else 'ref_seq_id'
                                            auth_seq_id = next((ref_seq_id for ref_seq_id, test_seq_id in zip(sa[_ref_seq_id_name], sa['test_seq_id'])
                                                                if test_seq_id == seq_id), None)

                                if None in (auth_asym_id, auth_seq_id):
                                    if seq_key in auth_to_star_seq:
                                        auth_asym_id, auth_seq_id, _ = seq_key
                                    else:
                                        entity_id_name = key_entity_id_names[d]
                                        if entity_id_name not in loop.tags:
                                            continue
                                        try:
                                            entity_assembly_id = int(chain_id)
                                            entity_id = int(loop.data[idx][loop.tags.index(entity_id_name)])
                                        except ValueError:
                                            continue
                                        k = next((k for k, v in auth_to_star_seq.items() if v[0] == entity_assembly_id and v[1] == seq_id and v[2] == entity_id), None)
                                        if k is None:
                                            continue
                                        auth_asym_id, auth_seq_id, _ = k

                                chain_id, seq_id = auth_asym_id, auth_seq_id

                                _assign, warn = assignCoordPolymerSequenceWithChainId(self.__caC, self.__nefT, chain_id, seq_id, comp_id, atom_id)

                                if warn is not None:

                                    _index_tag = index_tag if index_tag is not None else 'ID'
                                    try:
                                        _index_tag_col = loop.tags.index(_index_tag)
                                        idx_msg = f"[Check row of {_index_tag} {loop.data[idx][_index_tag_col]}] "
                                    except ValueError:
                                        _index_tag = 'ID'
                                        try:
                                            _index_tag_col = loop.tags.index(_index_tag)
                                            idx_msg = f"[Check row of {_index_tag} {loop.data[idx][_index_tag_col]}] "
                                        except ValueError:
                                            _index_tag = 'Index_ID'
                                            idx_msg = f"[Check row of {_index_tag} {idx + 1}] "

                                    if warn.startswith('[Atom not found]'):
                                        if not self.__remediation_mode or 'Macromolecules page' not in warn:
                                            self.report.error.appendDescription('atom_not_found',
                                                                                {'file_name': original_file_name,
                                                                                 'sf_framecode': sf_framecode,
                                                                                 'category': lp_category,
                                                                                 'description': idx_msg + warn})
                                            self.report.setError()

                                            if self.__verbose:
                                                self.__lfh.write(f"+{self.__class_name__}.validateStrMr() ++ Error  - {idx_msg + warn}\n")

                                    continue

                                enableWarning = True
                                if content_subtype == 'dist_restraint':
                                    if (auth_comp_id_1_col != -1 and loop.data[idx][auth_comp_id_1_col] == 'HOH')\
                                       or (auth_comp_id_2_col != -1 and loop.data[idx][auth_comp_id_2_col] == 'HOH'):
                                        enableWarning = False
                                elif content_subtype == 'dihed_restraint':
                                    if torsion_angle_name_col != -1 and loop.data[idx][torsion_angle_name_col] == 'PPA':
                                        enableWarning = False

                                atom_sels[d], warn = selectCoordAtoms(self.__cR, self.__caC, self.__nefT, _assign, auth_chain_id, seq_id, comp_id, atom_id, auth_atom_id,
                                                                      allowAmbig=content_subtype in ('dist_restraint', 'noepk_restraint'),
                                                                      enableWarning=enableWarning,
                                                                      preferAuthAtomName=prefer_auth_atom_name,
                                                                      representativeModelId=self.__representative_model_id, representativeAltId=self.__representative_alt_id,
                                                                      modelNumName=model_num_name)

                                if warn is not None:

                                    _index_tag = index_tag if index_tag is not None else 'ID'
                                    try:
                                        _index_tag_col = loop.tags.index(_index_tag)
                                        idx_msg = f"[Check row of {_index_tag} {loop.data[idx][_index_tag_col]}] "
                                    except ValueError:
                                        _index_tag = 'ID'
                                        try:
                                            _index_tag_col = loop.tags.index(_index_tag)
                                            idx_msg = f"[Check row of {_index_tag} {loop.data[idx][_index_tag_col]}] "
                                        except ValueError:
                                            _index_tag = 'Index_ID'
                                            idx_msg = f"[Check row of {_index_tag} {idx + 1}] "

                                    if warn.startswith('[Atom not found]'):
                                        if not self.__remediation_mode or 'Macromolecules page' not in warn:
                                            self.report.error.appendDescription('atom_not_found',
                                                                                {'file_name': original_file_name,
                                                                                 'sf_framecode': sf_framecode,
                                                                                 'category': lp_category,
                                                                                 'description': idx_msg + warn})
                                            self.report.setError()

                                            if self.__verbose:
                                                self.__lfh.write(f"+{self.__class_name__}.validateStrMr() ++ Error  - {idx_msg + warn}\n")

                                    elif warn.startswith('[Hydrogen not instantiated]'):
                                        self.report.warning.appendDescription('hydrogen_not_instantiated',
                                                                              {'file_name': original_file_name,
                                                                               'sf_framecode': sf_framecode,
                                                                               'category': lp_category,
                                                                               'description': idx_msg + warn})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.validateStrMr() ++ Warning  - {idx_msg + warn}\n")

                                    elif warn.startswith('[Invalid atom nomenclature]'):
                                        self.report.error.appendDescription('invalid_atom_nomenclature',
                                                                            {'file_name': original_file_name,
                                                                             'sf_framecode': sf_framecode,
                                                                             'category': lp_category,
                                                                             'description': idx_msg + warn})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.validateStrMr() ++ Error  - {idx_msg + warn}\n")

                                    elif warn.startswith('[Invalid atom selection]') or warn.startswith('[Invalid data]'):
                                        self.report.error.appendDescription('invalid_data',
                                                                            {'file_name': original_file_name,
                                                                             'sf_framecode': sf_framecode,
                                                                             'category': lp_category,
                                                                             'description': idx_msg + warn})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.validateStrMr() ++ ValueError  - {idx_msg + warn}\n")

                                    continue

                            if any(True for d in range(atom_dim_num) if atom_sels[d] is None or len(atom_sels[d]) == 0):
                                continue

                            sf_item['id'] += 1

                            if content_subtype == 'dist_restraint':
                                Id = '.'
                                if id_col != -1:
                                    Id = loop.data[idx][id_col]
                                    try:
                                        _Id = int(Id)
                                    except ValueError:
                                        Id = '.'
                                Id = sf_item['id'] if isinstance(Id, str) and Id == '.' else _Id
                                combinationId = '.'
                                if combination_id_col != -1:
                                    combinationId = loop.data[idx][combination_id_col]
                                    try:
                                        int(combinationId)
                                    except ValueError:
                                        combinationId = '.'
                                memberId = '.'
                                if member_id_col != -1:
                                    memberId = loop.data[idx][member_id_col]
                                    try:
                                        int(memberId)
                                    except ValueError:
                                        memberId = '.'
                                valid_atom_sels = atom_sels[0] is not None and atom_sels[1] is not None
                                if valid_atom_sels and len(atom_sels[0]) * len(atom_sels[1]) > 1\
                                   and (isAmbigAtomSelection(atom_sels[0], self.__csStat)
                                        or isAmbigAtomSelection(atom_sels[1], self.__csStat)):
                                    memberId = 0
                                memberLogicCode = '.'
                                if member_logic_code_col != -1:
                                    memberLogicCode = loop.data[idx][member_logic_code_col]
                                    if memberLogicCode in emptyValue:
                                        memberLogicCode = '.'
                                memberLogicCode = 'OR' if valid_atom_sels and len(atom_sels[0]) * len(atom_sels[1]) > 1 else memberLogicCode

                                if isinstance(memberId, int):
                                    _atom1 = _atom2 = None

                                if valid_atom_sels:
                                    for atom1, atom2 in itertools.product(atom_sels[0], atom_sels[1]):
                                        if isIdenticalRestraint([atom1, atom2]):
                                            continue
                                        if isinstance(memberId, int):
                                            if _atom1 is None or isAmbigAtomSelection([_atom1, atom1], self.__csStat)\
                                               or isAmbigAtomSelection([_atom2, atom2], self.__csStat):
                                                memberId += 1
                                                _atom1, _atom2 = atom1, atom2
                                        sf_item['index_id'] += 1
                                        _row = getRowForStrMr(content_subtype, Id, sf_item['index_id'],
                                                              memberId, memberLogicCode, list_id, self.__entry_id,
                                                              loop.tags, loop.data[idx],
                                                              auth_to_star_seq, auth_to_orig_seq, auth_to_ins_code, offset_holder,
                                                              [atom1, atom2], self.__annotation_mode)
                                        lp.add_data(_row)

                                elif atom_sels[0] is not None:
                                    atom2 = None
                                    for atom1 in atom_sels[0]:
                                        sf_item['index_id'] += 1
                                        _row = getRowForStrMr(content_subtype, Id, sf_item['index_id'],
                                                              memberId, memberLogicCode, list_id, self.__entry_id,
                                                              loop.tags, loop.data[idx],
                                                              auth_to_star_seq, auth_to_orig_seq, auth_to_ins_code, offset_holder,
                                                              [atom1, atom2], self.__annotation_mode)
                                        lp.add_data(_row)

                                elif atom_sels[1] is not None:
                                    atom1 = None
                                    for atom2 in atom_sels[1]:
                                        sf_item['index_id'] += 1
                                        _row = getRowForStrMr(content_subtype, Id, sf_item['index_id'],
                                                              memberId, memberLogicCode, list_id, self.__entry_id,
                                                              loop.tags, loop.data[idx],
                                                              auth_to_star_seq, auth_to_orig_seq, auth_to_ins_code, offset_holder,
                                                              [atom1, atom2], self.__annotation_mode)
                                        lp.add_data(_row)

                                else:
                                    atom1 = atom2 = None
                                    sf_item['index_id'] += 1
                                    _row = getRowForStrMr(content_subtype, Id, sf_item['index_id'],
                                                          memberId, memberLogicCode, list_id, self.__entry_id,
                                                          loop.tags, loop.data[idx],
                                                          auth_to_star_seq, auth_to_orig_seq, auth_to_ins_code, offset_holder,
                                                          [atom1, atom2], self.__annotation_mode)
                                    lp.add_data(_row)

                            else:

                                sf_item['index_id'] += 1
                                _row = getRowForStrMr(content_subtype, sf_item['id'], sf_item['index_id'],
                                                      None, None, list_id, self.__entry_id,
                                                      loop.tags, loop.data[idx],
                                                      auth_to_star_seq, auth_to_orig_seq, auth_to_ins_code, offset_holder,
                                                      atom_sels, self.__annotation_mode)
                                lp.add_data(_row)

                else:  # nothing to do because of insufficient sequence tags

                    del sf[lp]
                    lp = loop

                    sf.add_loop(lp)
                    sf_item['loop'] = lp

            elif content_subtype == 'ph_param_data':

                lp = getLoop(content_subtype, reduced=False, hasInsCode=False)

                sf.add_loop(lp)
                sf_item['loop'] = lp

                for row in loop:
                    sf_item['id'] += 1
                    sf_item['index_id'] += 1

                    _row = getRowForStrMr(content_subtype, sf_item['id'], sf_item['index_id'],
                                          None, None, list_id, self.__entry_id,
                                          loop.tags, row,
                                          {}, {}, {}, {},
                                          [None], self.__annotation_mode)
                    lp.add_data(_row)

            else:

                auth_to_star_seq = self.__caC['auth_to_star_seq']

                key_items = [item['name'] for item in NMR_STAR_LP_KEY_ITEMS[content_subtype]]

                if content_subtype == 'ccr_dd_restraint' and 'Dipole_2_chem_comp_index_ID_2' in loop.tags:
                    key_items = copy.copy(key_items)
                    key_item = next((key_item for key_item in key_items if key_item['name'] == 'Dipole_2_comp_index_ID_2'), None)
                    if key_item is not None:
                        key_item['name'] = 'Dipole_2_chem_comp_index_ID_2'

                len_key_items = len(key_items)

                atom_dim_num = (len_key_items - 1) // 5  # 5 for entity_assembly_id, entity_id, comp_index_id, comp_id, atom_id tags

                if atom_dim_num == 0:
                    err = f"Unexpected key items {key_items} set for processing {lp_category} loop in {sf_framecode} saveframe of {original_file_name} file."

                    self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.validateStrMr() ++ KeyError  - " + err)
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write(f"+{self.__class_name__}.validateStrMr() ++ KeyError  - {err}\n")

                    return False

                prefer_auth_atom_name = True

                coord_atom_site = self.__caC['coord_atom_site']
                auth_to_orig_seq = self.__caC['auth_to_orig_seq']
                auth_to_ins_code = None

                model_num_name = 'pdbx_PDB_model_num' if 'pdbx_PDB_model_num' in self.__coord_atom_site_tags else 'ndb_model'

                offset_holder = {}

                index_tag = INDEX_TAGS[file_type][content_subtype]
                id_col = loop.tags.index('ID') if 'ID' in loop.tags else -1
                combination_id_col = member_id_col = member_logic_code_col = upper_limit_col = -1
                auth_comp_id_1_col = auth_comp_id_2_col = torsion_angle_name_col = -1
                if content_subtype == 'dist_restraint':
                    if 'Combination_ID' in loop.tags:
                        combination_id_col = loop.tags.index('Combination_ID')
                    if 'Member_ID' in loop.tags:
                        member_id_col = loop.tags.index('Member_ID')
                    if 'Member_logic_code' in loop.tags:
                        member_logic_code_col = loop.tags.index('Member_logic_code')
                    if 'Distance_upper_bound_val' in loop.tags:
                        upper_limit_col = loop.tags.index('Distance_upper_bound_val')
                    if 'Auth_comp_ID_1' in loop.tags:
                        auth_comp_id_1_col = loop.tags.index('Auth_comp_ID_1')
                    if 'Auth_comp_ID_2' in loop.tags:
                        auth_comp_id_2_col = loop.tags.index('Auth_comp_ID_2')
                elif content_subtype == 'dihed_restraint':
                    if 'Torsion_angle_name' in loop.tags:
                        torsion_angle_name_col = loop.tags.index('Torsion_angle_name')

                auth_items = [auth_item['name'] for auth_item in NMR_STAR_LP_DATA_ITEMS[content_subtype]
                              if auth_item['name'].startswith('Auth') or 'auth' in auth_item['name']]

                auth_chain_id_names = [auth_item for auth_item in auth_items if 'asym' in auth_item or 'entity_assembly' in auth_item]
                auth_seq_id_names = [auth_item for auth_item in auth_items if 'seq' in auth_item]
                auth_comp_id_names = [auth_item for auth_item in auth_items if 'comp' in auth_item]
                auth_atom_id_names = [auth_item for auth_item in auth_items if 'atom' in auth_item and 'atom_name' not in auth_item]

                has_auth_chain_tags = set(auth_chain_id_names) & set(loop.tags) == set(auth_chain_id_names)
                has_auth_seq_tags = set(auth_seq_id_names) & set(loop.tags) == set(auth_seq_id_names)
                has_auth_comp_tags = set(auth_comp_id_names) & set(loop.tags) == set(auth_comp_id_names)
                has_auth_atom_tags = set(auth_atom_id_names) & set(loop.tags) == set(auth_atom_id_names)

                if not has_auth_chain_tags and self.__caC['polymer_sequence'] is not None and len(self.__caC['polymer_sequence']) == 1:
                    auth_chain_id = self.__caC['polymer_sequence'][0]['auth_chain_id']
                    for auth_chain_id_name in auth_chain_id_names:
                        if auth_chain_id_name in loop.tags:
                            continue
                        loop.add_tag(auth_chain_id_name)
                        for row in loop:
                            row.append(auth_chain_id)
                    has_auth_chain_tags = True

                has_valid_comp_id = True
                if has_auth_chain_tags and has_auth_seq_tags and has_auth_atom_tags and not has_auth_comp_tags:
                    for d, auth_comp_id_name in enumerate(auth_comp_id_names):
                        if auth_comp_id_name in loop.tags:
                            tags = [auth_chain_id_names[d], auth_seq_id_names[d], auth_comp_id_names[d]]
                            for idx, row in enumerate(loop.get_tag(tags)):
                                if row[2] not in emptyValue:
                                    continue
                                try:
                                    chain_id, seq_id = row[0], int(row[1])
                                    comp_id = next((_auth_comp_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                    if _auth_asym_id == chain_id and _auth_seq_id == seq_id), None)
                                except (TypeError, ValueError):
                                    comp_id = None
                                    has_valid_comp_id = False
                                loop.data[idx][loop.tags.index(auth_comp_id_names[d])] = comp_id
                            continue
                        loop.add_tag(auth_comp_id_name)
                        tags = [auth_chain_id_names[d], auth_seq_id_names[d]]
                        for idx, row in enumerate(loop.get_tag(tags)):
                            try:
                                chain_id, seq_id = row[0], int(row[1])
                                comp_id = next((_auth_comp_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                if _auth_asym_id == chain_id and _auth_seq_id == seq_id), None)
                            except (TypeError, ValueError):
                                comp_id = None
                            loop.data[idx].append(comp_id)
                            if comp_id is None:
                                has_valid_comp_id = False
                        has_auth_comp_tags = True

                if has_auth_chain_tags and has_auth_seq_tags and has_auth_atom_tags and has_auth_comp_tags and has_valid_comp_id:
                    is_valid = True

                    lp = getLoop(content_subtype, reduced=False)

                    sf.add_loop(lp)
                    sf_item['loop'] = lp

                    auth_items = []
                    for d in range(atom_dim_num):
                        auth_items.extend([auth_chain_id_names[d], auth_seq_id_names[d], auth_comp_id_names[d], auth_atom_id_names[d]])
                    for idx, row in enumerate(loop.get_tag(auth_items)):
                        atom_sels = [None] * atom_dim_num

                        for d in range(atom_dim_num):

                            try:

                                chain_id = auth_chain_id = row[d * 4]
                                seq_id = int(row[d * 4 + 1])
                                comp_id = row[d * 4 + 2]
                                atom_id = row[d * 4 + 3]

                                seq_key = (chain_id, seq_id, comp_id)

                                entity_assembly_id, comp_index_id, _, _ = auth_to_star_seq[seq_key]  # pylint: disable=pointless-statement

                                if self.__annotation_mode or self.__native_combined:
                                    _auth_asym_id, _auth_seq_id =\
                                        next(((k[0], k[1]) for k, v in auth_to_star_seq.items()
                                              if v[0] == entity_assembly_id and v[1] == comp_index_id and k[2] == comp_id), (None, None))
                                    if _auth_asym_id is not None:
                                        seq_key = (_auth_asym_id, _auth_seq_id, comp_id)
                                        if seq_key in auth_to_star_seq:
                                            chain_id, seq_id = _auth_asym_id, _auth_seq_id

                            except KeyError:
                                continue
                            except ValueError:
                                is_valid = False
                                continue

                            auth_atom_id = atom_id

                            auth_asym_id = auth_seq_id = None

                            if seq_key in auth_to_star_seq:
                                auth_asym_id, auth_seq_id, _ = seq_key
                            else:
                                k = next((k for k, v in auth_to_star_seq.items() if v[0] == entity_assembly_id and v[1] == seq_id and v[2] == entity_id), None)
                                if k is None:
                                    continue
                                auth_asym_id, auth_seq_id, _ = k

                            chain_id, seq_id = auth_asym_id, auth_seq_id

                            _assign, warn = assignCoordPolymerSequenceWithChainId(self.__caC, self.__nefT, chain_id, seq_id, comp_id, atom_id)

                            if warn is not None:

                                _index_tag = index_tag if index_tag is not None else 'ID'
                                try:
                                    _index_tag_col = loop.tags.index(_index_tag)
                                    idx_msg = f"[Check row of {_index_tag} {loop.data[idx][_index_tag_col]}] "
                                except ValueError:
                                    _index_tag = 'ID'
                                    try:
                                        _index_tag_col = loop.tags.index(_index_tag)
                                        idx_msg = f"[Check row of {_index_tag} {loop.data[idx][_index_tag_col]}] "
                                    except ValueError:
                                        _index_tag = 'Index_ID'
                                        idx_msg = f"[Check row of {_index_tag} {idx + 1}] "

                                if warn.startswith('[Atom not found]'):
                                    if not self.__remediation_mode or 'Macromolecules page' not in warn:
                                        self.report.error.appendDescription('atom_not_found',
                                                                            {'file_name': original_file_name,
                                                                             'sf_framecode': sf_framecode,
                                                                             'category': lp_category,
                                                                             'description': idx_msg + warn})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.validateStrMr() ++ Error  - {idx_msg + warn}\n")

                                continue

                            enableWarning = True
                            if content_subtype == 'dist_restraint':
                                if (auth_comp_id_1_col != -1 and loop.data[idx][auth_comp_id_1_col] == 'HOH')\
                                   or (auth_comp_id_2_col != -1 and loop.data[idx][auth_comp_id_2_col] == 'HOH'):
                                    enableWarning = False
                            elif content_subtype == 'dihed_restraint':
                                if torsion_angle_name_col != -1 and loop.data[idx][torsion_angle_name_col] == 'PPA':
                                    enableWarning = False

                            atom_sels[d], warn = selectCoordAtoms(self.__cR, self.__caC, self.__nefT, _assign, auth_chain_id, seq_id, comp_id, atom_id, auth_atom_id,
                                                                  allowAmbig=content_subtype in ('dist_restraint', 'noepk_restraint'),
                                                                  enableWarning=enableWarning,
                                                                  preferAuthAtomName=prefer_auth_atom_name,
                                                                  representativeModelId=self.__representative_model_id, representativeAltId=self.__representative_alt_id,
                                                                  modelNumName=model_num_name)

                            if warn is not None:

                                _index_tag = index_tag if index_tag is not None else 'ID'
                                try:
                                    _index_tag_col = loop.tags.index(_index_tag)
                                    idx_msg = f"[Check row of {_index_tag} {loop.data[idx][_index_tag_col]}] "
                                except ValueError:
                                    _index_tag = 'ID'
                                    try:
                                        _index_tag_col = loop.tags.index(_index_tag)
                                        idx_msg = f"[Check row of {_index_tag} {loop.data[idx][_index_tag_col]}] "
                                    except ValueError:
                                        _index_tag = 'Index_ID'
                                        idx_msg = f"[Check row of {_index_tag} {idx + 1}] "

                                if warn.startswith('[Atom not found]'):
                                    if not self.__remediation_mode or 'Macromolecules page' not in warn:
                                        self.report.error.appendDescription('atom_not_found',
                                                                            {'file_name': original_file_name,
                                                                             'sf_framecode': sf_framecode,
                                                                             'category': lp_category,
                                                                             'description': idx_msg + warn})
                                        self.report.setError()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.validateStrMr() ++ Error  - {idx_msg + warn}\n")

                                elif warn.startswith('[Hydrogen not instantiated]'):
                                    self.report.warning.appendDescription('hydrogen_not_instantiated',
                                                                          {'file_name': original_file_name,
                                                                           'sf_framecode': sf_framecode,
                                                                           'category': lp_category,
                                                                           'description': idx_msg + warn})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.validateStrMr() ++ Warning  - {idx_msg + warn}\n")

                                elif warn.startswith('[Invalid atom nomenclature]'):
                                    self.report.error.appendDescription('invalid_atom_nomenclature',
                                                                        {'file_name': original_file_name,
                                                                         'sf_framecode': sf_framecode,
                                                                         'category': lp_category,
                                                                         'description': idx_msg + warn})
                                    self.report.setError()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.validateStrMr() ++ Error  - {idx_msg + warn}\n")

                                elif warn.startswith('[Invalid atom selection]') or warn.startswith('[Invalid data]'):
                                    self.report.error.appendDescription('invalid_data',
                                                                        {'file_name': original_file_name,
                                                                         'sf_framecode': sf_framecode,
                                                                         'category': lp_category,
                                                                         'description': idx_msg + warn})
                                    self.report.setError()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.validateStrMr() ++ ValueError  - {idx_msg + warn}\n")

                                continue

                        if any(True for d in range(atom_dim_num) if atom_sels[d] is None or len(atom_sels[d]) == 0):
                            continue

                        sf_item['id'] += 1

                        if content_subtype == 'dist_restraint':
                            Id = '.'
                            if id_col != -1:
                                Id = loop.data[idx][id_col]
                                try:
                                    _Id = int(Id)
                                except ValueError:
                                    Id = '.'
                            Id = sf_item['id'] if isinstance(Id, str) and Id == '.' else _Id
                            combinationId = '.'
                            if combination_id_col != -1:
                                combinationId = loop.data[idx][combination_id_col]
                                try:
                                    int(combinationId)
                                except ValueError:
                                    combinationId = '.'
                            memberId = '.'
                            if member_id_col != -1:
                                memberId = loop.data[idx][member_id_col]
                                try:
                                    int(memberId)
                                except ValueError:
                                    memberId = '.'
                            valid_atom_sels = atom_sels[0] is not None and atom_sels[1] is not None
                            if valid_atom_sels and len(atom_sels[0]) * len(atom_sels[1]) > 1\
                               and (isAmbigAtomSelection(atom_sels[0], self.__csStat)
                                    or isAmbigAtomSelection(atom_sels[1], self.__csStat)):
                                memberId = 0
                            memberLogicCode = '.'
                            if member_logic_code_col != -1:
                                memberLogicCode = loop.data[idx][member_logic_code_col]
                                if memberLogicCode in emptyValue:
                                    memberLogicCode = '.'
                            memberLogicCode = 'OR' if valid_atom_sels and len(atom_sels[0]) * len(atom_sels[1]) > 1 else memberLogicCode

                            if isinstance(memberId, int):
                                _atom1 = _atom2 = None

                            if valid_atom_sels:
                                for atom1, atom2 in itertools.product(atom_sels[0], atom_sels[1]):
                                    if isIdenticalRestraint([atom1, atom2]):
                                        continue
                                    if isinstance(memberId, int):
                                        if _atom1 is None or isAmbigAtomSelection([_atom1, atom1], self.__csStat)\
                                           or isAmbigAtomSelection([_atom2, atom2], self.__csStat):
                                            memberId += 1
                                            _atom1, _atom2 = atom1, atom2
                                    sf_item['index_id'] += 1
                                    _row = getRowForStrMr(content_subtype, Id, sf_item['index_id'],
                                                          memberId, memberLogicCode, list_id, self.__entry_id,
                                                          loop.tags, loop.data[idx],
                                                          auth_to_star_seq, auth_to_orig_seq, auth_to_ins_code, offset_holder,
                                                          [atom1, atom2], self.__annotation_mode)
                                    lp.add_data(_row)

                            elif atom_sels[0] is not None:
                                atom2 = None
                                for atom1 in atom_sels[0]:
                                    sf_item['index_id'] += 1
                                    _row = getRowForStrMr(content_subtype, Id, sf_item['index_id'],
                                                          memberId, memberLogicCode, list_id, self.__entry_id,
                                                          loop.tags, loop.data[idx],
                                                          auth_to_star_seq, auth_to_orig_seq, auth_to_ins_code, offset_holder,
                                                          [atom1, atom2], self.__annotation_mode)
                                    lp.add_data(_row)

                            elif atom_sels[1] is not None:
                                atom1 = None
                                for atom2 in atom_sels[1]:
                                    sf_item['index_id'] += 1
                                    _row = getRowForStrMr(content_subtype, Id, sf_item['index_id'],
                                                          memberId, memberLogicCode, list_id, self.__entry_id,
                                                          loop.tags, loop.data[idx],
                                                          auth_to_star_seq, auth_to_orig_seq, auth_to_ins_code, offset_holder,
                                                          [atom1, atom2], self.__annotation_mode)
                                    lp.add_data(_row)

                            else:
                                atom1 = atom2 = None
                                sf_item['index_id'] += 1
                                _row = getRowForStrMr(content_subtype, Id, sf_item['index_id'],
                                                      memberId, memberLogicCode, list_id, self.__entry_id,
                                                      loop.tags, loop.data[idx],
                                                      auth_to_star_seq, auth_to_orig_seq, auth_to_ins_code, offset_holder,
                                                      [atom1, atom2], self.__annotation_mode)
                                lp.add_data(_row)

                        else:

                            sf_item['index_id'] += 1
                            _row = getRowForStrMr(content_subtype, sf_item['id'], sf_item['index_id'],
                                                  None, None, list_id, self.__entry_id,
                                                  loop.tags, loop.data[idx],
                                                  auth_to_star_seq, auth_to_orig_seq, auth_to_ins_code, offset_holder,
                                                  atom_sels, self.__annotation_mode)
                            lp.add_data(_row)

                    if not is_valid:

                        lp = loop

                        sf_item['loop'] = lp

                else:  # nothing to do because of missing polymer sequence for this loop

                    lp = loop

                    sf_item['loop'] = lp

            if content_subtype == 'dist_restraint':

                sf_item['loop'] = lp

                use_member_logic_code = sf_item['file_type'] in ('nm-res-xpl', 'nm-res-cns', 'nm-res-cha')
                if use_member_logic_code:
                    lp = sf_item['loop']
                    if 'Member_logic_code' not in lp.tags:
                        use_member_logic_code = False
                    else:
                        dat = lp.get_tag(['Member_logic_code'])
                        use_member_logic_code = any(True for row in dat if row not in emptyValue)

                if not use_member_logic_code:
                    if not self.updateGenDistConstIdInMrStr(sf_item):
                        err = 'Atoms in distance restraints can not be properly identified. Please re-upload the NMR-STAR file.'
                        self.report.error.appendDescription('missing_mandatory_content',
                                                            {'file_name': original_file_name,
                                                             'sf_framecode': sf_framecode,
                                                             'category': lp_category,
                                                             'description': err})

                sf_item['constraint_type'] = 'distance'
                sf_item['constraint_subsubtype'] = 'simple'
                constraint_type = get_first_sf_tag(sf, 'Constraint_type')
                if len(constraint_type) > 0 and constraint_type not in emptyValue:
                    sf_item['constraint_subtype'] = constraint_type

                item_names = ITEM_NAMES_IN_DIST_LOOP[file_type]
                id_col = lp.tags.index('ID')
                member_logic_code_col = lp.tags.index('Member_logic_code') if 'Member_logic_code' in lp.tags else -1
                auth_asym_id_1_col = lp.tags.index('Auth_asym_ID_1')
                auth_seq_id_1_col = lp.tags.index('Auth_seq_ID_1')
                auth_asym_id_2_col = lp.tags.index('Auth_asym_ID_2')
                auth_seq_id_2_col = lp.tags.index('Auth_seq_ID_2')
                comp_id_1_col = lp.tags.index(item_names['comp_id_1'])
                comp_id_2_col = lp.tags.index(item_names['comp_id_2'])
                atom_id_1_col = lp.tags.index(item_names['atom_id_1'])
                atom_id_2_col = lp.tags.index(item_names['atom_id_2'])

                try:
                    target_value_col = lp.tags.index(item_names['target_value'])
                except ValueError:
                    target_value_col = -1
                try:
                    lower_limit_col = lp.tags.index(item_names['lower_limit'])
                except ValueError:
                    lower_limit_col = -1
                try:
                    upper_limit_col = lp.tags.index(item_names['upper_limit'])
                except ValueError:
                    upper_limit_col = -1
                try:
                    lower_linear_limit_col = lp.tags.index(item_names['lower_linear_limit'])
                except ValueError:
                    lower_linear_limit_col = -1
                try:
                    upper_linear_limit_col = lp.tags.index(item_names['upper_linear_limit'])
                except ValueError:
                    upper_linear_limit_col = -1

                has_or_code = False

                potential_type = get_first_sf_tag(sf, 'Potential_type')
                has_potential_type = len(potential_type) > 0 and potential_type not in emptyValue and potential_type != 'unknown'

                _potential_type = None
                count = 0

                prev_id = -1
                for row in lp:
                    _id = int(row[id_col])
                    if _id == prev_id:
                        if member_logic_code_col != -1 and row[member_logic_code_col] == 'OR':
                            has_or_code = True
                        continue
                    prev_id = _id
                    count += 1
                    if not has_potential_type:
                        dst_func = {}
                        if target_value_col != -1 and row[target_value_col] not in emptyValue:
                            dst_func['target_value'] = float(row[target_value_col])
                        if lower_limit_col != -1 and row[lower_limit_col] not in emptyValue:
                            dst_func['lower_limit'] = float(row[lower_limit_col])
                        if upper_limit_col != -1 and row[upper_limit_col] not in emptyValue:
                            dst_func['upper_limit'] = float(row[upper_limit_col])
                        if lower_linear_limit_col != -1 and row[lower_linear_limit_col] not in emptyValue:
                            dst_func['lower_linear_limit'] = float(row[lower_linear_limit_col])
                        if upper_linear_limit_col != -1 and row[upper_linear_limit_col] not in emptyValue:
                            dst_func['upper_linear_limit'] = float(row[upper_linear_limit_col])
                        if _potential_type is None:
                            _potential_type = getPotentialType(file_type, 'dist', dst_func)
                        else:
                            if getPotentialType(file_type, 'dist', dst_func) != _potential_type:
                                has_potential_type = True

                if not has_potential_type and _potential_type is not None:
                    set_sf_tag(sf, 'Potential_type', _potential_type)

                sf_item['id'] = count

                if has_or_code:

                    prev_id = -1
                    for row in lp:
                        if member_logic_code_col != -1 and row[member_logic_code_col] == 'OR':
                            _id = int(row[id_col])
                            if _id != prev_id:
                                _atom1 = {'chain_id': row[auth_asym_id_1_col],
                                          'seq_id': int(row[auth_seq_id_1_col]) if row[auth_seq_id_1_col] not in emptyValue else None,
                                          'comp_id': row[comp_id_1_col],
                                          'atom_id': row[atom_id_1_col]}
                                _atom2 = {'chain_id': row[auth_asym_id_2_col],
                                          'seq_id': int(row[auth_seq_id_2_col]) if row[auth_seq_id_2_col] not in emptyValue else None,
                                          'comp_id': row[comp_id_2_col],
                                          'atom_id': row[atom_id_2_col]}
                                prev_id = _id
                                continue
                            atom1 = {'chain_id': row[auth_asym_id_1_col],
                                     'seq_id': int(row[auth_seq_id_1_col]) if row[auth_seq_id_1_col] not in emptyValue else None,
                                     'comp_id': row[comp_id_1_col],
                                     'atom_id': row[atom_id_1_col]}
                            atom2 = {'chain_id': row[auth_asym_id_2_col],
                                     'seq_id': int(row[auth_seq_id_2_col]) if row[auth_seq_id_2_col] not in emptyValue else None,
                                     'comp_id': row[comp_id_2_col],
                                     'atom_id': row[atom_id_2_col]}
                            if isAmbigAtomSelection([_atom1, atom1], self.__csStat)\
                               or isAmbigAtomSelection([_atom2, atom2], self.__csStat):
                                sf_item['constraint_subsubtype'] = 'ambi'
                                break
                            _atom1, _atom2 = atom1, atom2

                    if sf_item['constraint_subsubtype'] == 'ambi':

                        if 'pre' in sf_framecode or 'paramag' in sf_framecode:
                            sf_item['constraint_subtype'] = 'paramagnetic relaxation'
                        if 'cidnp' in sf_framecode:
                            sf_item['constraint_subtype'] = 'photo cidnp'
                        if 'csp' in sf_framecode or 'perturb' in sf_framecode:
                            sf_item['constraint_subtype'] = 'chemical shift perturbation'
                        if 'mutat' in sf_framecode:
                            sf_item['constraint_subtype'] = 'mutation'
                        if 'protect' in sf_framecode:
                            sf_item['constraint_subtype'] = 'hydrogen exchange protection'
                        if 'symm' in sf_framecode:
                            sf_item['constraint_subtype'] = 'symmetry'

                        if 'pre' in original_file_name or 'paramag' in original_file_name:
                            sf_item['constraint_subtype'] = 'paramagnetic relaxation'
                        if 'cidnp' in original_file_name:
                            sf_item['constraint_subtype'] = 'photo cidnp'
                        if 'csp' in original_file_name or 'perturb' in original_file_name:
                            sf_item['constraint_subtype'] = 'chemical shift perturbation'
                        if 'mutat' in original_file_name:
                            sf_item['constraint_subtype'] = 'mutation'
                        if 'protect' in original_file_name:
                            sf_item['constraint_subtype'] = 'hydrogen exchange protection'
                        if 'symm' in original_file_name:
                            sf_item['constraint_subtype'] = 'symmetry'

                if sf_item['constraint_subsubtype'] == 'simple':

                    metal_coord = disele_bond = disulf_bond = hydrog_bond = False

                    for row in lp:
                        comp_id_1 = row[comp_id_1_col]
                        comp_id_2 = row[comp_id_2_col]
                        atom_id_1 = row[atom_id_1_col]
                        atom_id_2 = row[atom_id_2_col]

                        if atom_id_1 in emptyValue or atom_id_2 in emptyValue:
                            continue

                        atom_id_1_ = atom_id_1[0]
                        atom_id_2_ = atom_id_2[0]
                        if comp_id_1 == atom_id_1 or comp_id_2 == atom_id_2:
                            metal_coord = True
                        elif 'SE' in (atom_id_1, atom_id_2):
                            disele_bond = True
                        elif 'SG' in (atom_id_1, atom_id_2):
                            disulf_bond = True
                        elif (atom_id_1_ == 'F' and atom_id_2_ in protonBeginCode) or (atom_id_2_ == 'F' and atom_id_1_ in protonBeginCode):
                            hydrog_bond = True
                        elif (atom_id_1_ == 'F' and atom_id_2_ == 'F') or (atom_id_2_ == 'F' and atom_id_1_ == 'F'):
                            hydrog_bond = True
                        elif (atom_id_1_ == 'O' and atom_id_2_ in protonBeginCode) or (atom_id_2_ == 'O' and atom_id_1_ in protonBeginCode):
                            hydrog_bond = True
                        elif (atom_id_1_ == 'O' and atom_id_2_ == 'N') or (atom_id_2_ == 'O' and atom_id_1_ == 'N'):
                            hydrog_bond = True
                        elif (atom_id_1_ == 'O' and atom_id_2_ == 'O') or (atom_id_2_ == 'O' and atom_id_1_ == 'O'):
                            hydrog_bond = True
                        elif (atom_id_1_ == 'N' and atom_id_2_ in protonBeginCode) or (atom_id_2_ == 'N' and atom_id_1_ in protonBeginCode):
                            hydrog_bond = True
                        elif (atom_id_1_ == 'N' and atom_id_2_ == 'N') or (atom_id_2_ == 'N' and atom_id_1_ == 'N'):
                            hydrog_bond = True

                    if not metal_coord and not disele_bond and not disulf_bond and not hydrog_bond:
                        if 'build' in sf_framecode and 'up' in sf_framecode:
                            if 'roe' in sf_framecode:
                                sf_item['constraint_subtype'] = 'ROE build-up'
                            else:
                                sf_item['constraint_subtype'] = 'NOE build-up'

                        elif 'not' in sf_framecode and 'seen' in sf_framecode:
                            sf_item['constraint_subtype'] = 'NOE not seen'

                        elif 'roe' in sf_framecode:
                            sf_item['constraint_subtype'] = 'ROE'

                        elif 'build' in original_file_name and 'up' in original_file_name:
                            if 'roe' in original_file_name:
                                sf_item['constraint_subtype'] = 'ROE build-up'
                            else:
                                sf_item['constraint_subtype'] = 'NOE build-up'

                        elif 'not' in original_file_name and 'seen' in original_file_name:
                            sf_item['constraint_subtype'] = 'NOE not seen'

                        elif 'roe' in original_file_name:
                            sf_item['constraint_subtype'] = 'ROE'

                        sf_item['constraint_subtype'] = 'NOE'

                    elif metal_coord and not disele_bond and not disulf_bond and not hydrog_bond:
                        sf_item['constraint_subtype'] = 'metal coordination'

                    elif not metal_coord and disele_bond and not disulf_bond and not hydrog_bond:
                        sf_item['constraint_subtype'] = 'diselenide bond'

                    elif not metal_coord and not disele_bond and disulf_bond and not hydrog_bond:
                        sf_item['constraint_subtype'] = 'disulfide bond'

                    elif not metal_coord and not disele_bond and not disulf_bond and hydrog_bond:
                        sf_item['constraint_subtype'] = 'hydrogen bond'

            elif content_subtype == 'dihed_restraint':
                self.updateTorsionAngleConstIdInMrStr(sf_item)

                auth_to_entity_type = self.__caC['auth_to_entity_type']

                sf_item['constraint_type'] = 'dihedral angle'

                item_names = ITEM_NAMES_IN_DIHED_LOOP[file_type]
                id_col = lp.tags.index('ID')
                try:
                    target_value_col = lp.tags.index(item_names['target_value'])
                except ValueError:
                    target_value_col = -1
                try:
                    lower_limit_col = lp.tags.index(item_names['lower_limit'])
                except ValueError:
                    lower_limit_col = -1
                try:
                    upper_limit_col = lp.tags.index(item_names['upper_limit'])
                except ValueError:
                    upper_limit_col = -1
                try:
                    lower_linear_limit_col = lp.tags.index(item_names['lower_linear_limit'])
                except ValueError:
                    lower_linear_limit_col = -1
                try:
                    upper_linear_limit_col = lp.tags.index(item_names['upper_linear_limit'])
                except ValueError:
                    upper_linear_limit_col = -1

                potential_type = get_first_sf_tag(sf, 'Potential_type')
                has_potential_type = len(potential_type) > 0 and potential_type not in emptyValue and potential_type != 'unknown'

                _potential_type = None
                count = 0

                prev_id = -1
                for row in lp:
                    _id = int(row[id_col])
                    if _id == prev_id:
                        continue
                    prev_id = _id
                    count += 1
                    if not has_potential_type:
                        dst_func = {}
                        if target_value_col != -1 and row[target_value_col] not in emptyValue:
                            dst_func['target_value'] = float(row[target_value_col])
                        if lower_limit_col != -1 and row[lower_limit_col] not in emptyValue:
                            dst_func['lower_limit'] = float(row[lower_limit_col])
                        if upper_limit_col != -1 and row[upper_limit_col] not in emptyValue:
                            dst_func['upper_limit'] = float(row[upper_limit_col])
                        if lower_linear_limit_col != -1 and row[lower_linear_limit_col] not in emptyValue:
                            dst_func['lower_linear_limit'] = float(row[lower_linear_limit_col])
                        if upper_linear_limit_col != -1 and row[upper_linear_limit_col] not in emptyValue:
                            dst_func['upper_linear_limit'] = float(row[upper_linear_limit_col])
                        if _potential_type is None:
                            _potential_type = getPotentialType(file_type, 'dihed', dst_func)
                        else:
                            if getPotentialType(file_type, 'dihed', dst_func) != _potential_type:
                                has_potential_type = True

                if not has_potential_type and _potential_type is not None:
                    set_sf_tag(sf, 'Potential_type', _potential_type)

                sf_item['id'] = count

                auth_asym_id_col = lp.tags.index('Auth_asym_ID_2')
                auth_seq_id_col = lp.tags.index('Auth_seq_ID_2')
                auth_comp_id_col = lp.tags.index('Auth_comp_ID_2')

                _protein_angles = _other_angles = 0

                prev_id = -1
                for row in lp:
                    _id = int(row[id_col])
                    if _id == prev_id:
                        continue
                    prev_id = _id
                    auth_asym_id = row[auth_asym_id_col]
                    auth_seq_id = int(row[auth_seq_id_col]) if row[auth_seq_id_col] not in emptyValue else None
                    auth_comp_id = row[auth_comp_id_col]

                    seq_key = (auth_asym_id, auth_seq_id, auth_comp_id)

                    if seq_key in auth_to_entity_type:
                        entity_type = auth_to_entity_type[seq_key]

                        if 'peptide' in entity_type:
                            _protein_angles += 1
                        else:
                            _other_angles += 1

                if _protein_angles > _other_angles:
                    sf_item['constraint_type'] = 'protein dihedral angle'

                    tagNames = [t[0] for t in sf.tags]

                    if 'Constraint_type' not in tagNames:
                        sf_item['constraint_subtype'] = 'backbone chemical shifts'
                        sf.add_tag('Constraint_subtype', 'backbone chemical shifts')

                _na_angles = _other_angles = 0

                prev_id = -1
                for row in lp:
                    _id = int(row[id_col])
                    if _id == prev_id:
                        continue
                    prev_id = _id
                    auth_asym_id = row[auth_asym_id_col]
                    auth_seq_id = int(row[auth_seq_id_col]) if row[auth_seq_id_col] not in emptyValue else None
                    auth_comp_id = row[auth_comp_id_col]

                    seq_key = (auth_asym_id, auth_seq_id, auth_comp_id)

                    if seq_key in auth_to_entity_type:
                        entity_type = auth_to_entity_type[seq_key]

                        if 'nucleotide' in entity_type:
                            _na_angles += 1
                        else:
                            _other_angles += 1

                if _na_angles > _other_angles:
                    sf_item['constraint_type'] = 'nucleic acid dihedral angle'

                    tagNames = [t[0] for t in sf.tags]

                    if 'Constraint_type' not in tagNames:
                        sf_item['constraint_subtype'] = 'unknown'
                        sf.add_tag('Constraint_type', 'unknown')

                _br_angles = _other_angles = 0

                prev_id = -1
                for row in lp:
                    _id = int(row[id_col])
                    if _id == prev_id:
                        continue
                    prev_id = _id
                    auth_asym_id = row[auth_asym_id_col]
                    auth_seq_id = int(row[auth_seq_id_col]) if row[auth_seq_id_col] not in emptyValue else None
                    auth_comp_id = row[auth_comp_id_col]

                    seq_key = (auth_asym_id, auth_seq_id, auth_comp_id)

                    if seq_key in auth_to_entity_type:
                        entity_type = auth_to_entity_type[seq_key]

                        if 'saccharide' in entity_type:
                            _br_angles += 1
                        else:
                            _other_angles += 1

                if _br_angles > _other_angles:
                    sf_item['constraint_type'] = 'carbohydrate dihedral angle'  # DAOTHER-9471

                    tagNames = [t[0] for t in sf.tags]

                    if 'Constraint_type' not in tagNames:
                        sf_item['constraint_subtype'] = 'unknown'
                        sf.add_tag('Constraint_type', 'unknown')

            elif content_subtype == 'rdc_restraint':

                sf_item['constraint_type'] = 'dipolar coupling'  # DAOTHER-9471
                sf_item['constraint_subtype'] = 'RDC'

                item_names = ITEM_NAMES_IN_RDC_LOOP[file_type]
                id_col = lp.tags.index('ID')
                try:
                    target_value_col = lp.tags.index(item_names['target_value'])
                except ValueError:
                    target_value_col = -1
                try:
                    lower_limit_col = lp.tags.index(item_names['lower_limit'])
                except ValueError:
                    lower_limit_col = -1
                try:
                    upper_limit_col = lp.tags.index(item_names['upper_limit'])
                except ValueError:
                    upper_limit_col = -1
                try:
                    lower_linear_limit_col = lp.tags.index(item_names['lower_linear_limit'])
                except ValueError:
                    lower_linear_limit_col = -1
                try:
                    upper_linear_limit_col = lp.tags.index(item_names['upper_linear_limit'])
                except ValueError:
                    upper_linear_limit_col = -1

                potential_type = get_first_sf_tag(sf, 'Potential_type')
                has_potential_type = len(potential_type) > 0 and potential_type not in emptyValue and potential_type != 'unknown'

                _potential_type = None
                count = 0

                prev_id = -1
                for row in lp:
                    _id = int(row[id_col])
                    if _id == prev_id:
                        continue
                    prev_id = _id
                    count += 1
                    if not has_potential_type:
                        dst_func = {}
                        if target_value_col != -1 and row[target_value_col] not in emptyValue:
                            dst_func['target_value'] = float(row[target_value_col])
                        if lower_limit_col != -1 and row[lower_limit_col] not in emptyValue:
                            dst_func['lower_limit'] = float(row[lower_limit_col])
                        if upper_limit_col != -1 and row[upper_limit_col] not in emptyValue:
                            dst_func['upper_limit'] = float(row[upper_limit_col])
                        if lower_linear_limit_col != -1 and row[lower_linear_limit_col] not in emptyValue:
                            dst_func['lower_linear_limit'] = float(row[lower_linear_limit_col])
                        if upper_linear_limit_col != -1 and row[upper_linear_limit_col] not in emptyValue:
                            dst_func['upper_linear_limit'] = float(row[upper_linear_limit_col])
                        if _potential_type is None:
                            _potential_type = getPotentialType(file_type, 'rdc', dst_func)
                        else:
                            if getPotentialType(file_type, 'rdc', dst_func) != _potential_type:
                                has_potential_type = True

                if not has_potential_type and _potential_type is not None:
                    set_sf_tag(sf, 'Potential_type', _potential_type)

                sf_item['id'] = count

            else:

                sf_item['id'] = len(lp)

            # merge other loops of the source saveframe
            if is_sf:

                for loop in _sf.loops:

                    if loop.category == lp_category:
                        continue

                    if loop.category in LINKED_LP_CATEGORIES[file_type][content_subtype]:
                        sf.add_loop(loop)

        self.__mr_sf_dict_holder[content_subtype].append(sf_item)

        return True

    def validateStrPk(self, file_list_id: int, file_type: str, content_subtype: str, list_id: int,
                      sf: Union[pynmrstar.Saveframe, pynmrstar.Loop],
                      sf_framecode: str, lp_category: str) -> bool:
        """ Validate spectral peak lists in NMR-STAR restraint files.
        """

        _num_dim = get_first_sf_tag(sf, NUM_DIM_ITEMS[file_type])
        num_dim = int(_num_dim)

        if num_dim not in range(1, MAX_DIM_NUM_OF_SPECTRA):
            return False

        max_dim = num_dim + 1

        lp_category = '_Peak_row_format' if content_subtype == 'spectral_peak' else '_Assigned_peak_chem_shift'

        try:

            loop = sf.get_loop(lp_category)

        except KeyError:
            return False

        input_source = self.report.input_sources[file_list_id]
        input_source_dic = input_source.get()

        has_poly_seq_in_lp = has_key_value(input_source_dic, 'polymer_sequence_in_loop')

        if not has_poly_seq_in_lp:
            return False

        coord_atom_site = self.__caC['coord_atom_site']
        auth_to_star_seq = self.__caC['auth_to_star_seq']
        auth_to_star_seq_ann = self.__caC['auth_to_star_seq_ann']
        auth_atom_name_to_id = self.__caC['auth_atom_name_to_id']
        auth_atom_name_to_id_ext = self.__caC['auth_atom_name_to_id_ext']

        poly_seq_in_lp = input_source_dic['polymer_sequence_in_loop']

        seq_align = chain_assign = br_seq_align = br_chain_assign = np_seq_align = np_chain_assign = None

        if content_subtype in poly_seq_in_lp:
            _poly_seq_in_lp = next((_poly_seq_in_lp for _poly_seq_in_lp in poly_seq_in_lp[content_subtype]
                                    if _poly_seq_in_lp['sf_framecode'] == sf_framecode), None)

            if _poly_seq_in_lp is not None:
                poly_seq = _poly_seq_in_lp['polymer_sequence']

                seq_align, _ = alignPolymerSequence(self.__pA, self.__caC['polymer_sequence'], poly_seq, conservative=False)
                chain_assign, _ = assignPolymerSequence(self.__pA, self.__ccU, file_type, self.__caC['polymer_sequence'], poly_seq, seq_align)

                if self.__caC['branched'] is not None:
                    br_seq_align, _ = alignPolymerSequence(self.__pA, self.__caC['branched'], poly_seq, conservative=False)
                    br_chain_assign, _ = assignPolymerSequence(self.__pA, self.__ccU, file_type, self.__caC['branched'], poly_seq, br_seq_align)

                if self.__caC['non_polymer'] is not None:
                    np_seq_align, _ = alignPolymerSequence(self.__pA, self.__caC['non_polymer'], poly_seq, conservative=False)
                    np_chain_assign, _ = assignPolymerSequence(self.__pA, self.__ccU, file_type, self.__caC['non_polymer'], poly_seq, np_seq_align)

        @functools.lru_cache()
        def get_auth_seq_scheme(chain_id, seq_id):
            auth_asym_id = auth_seq_id = None

            if seq_id is not None:

                if chain_assign is not None:
                    auth_asym_id = next((ca['ref_chain_id'] for ca in chain_assign if ca['test_chain_id'] == chain_id), None)
                    if auth_asym_id is not None:
                        sa = next((sa for sa in seq_align
                                   if sa['ref_chain_id'] == auth_asym_id and sa['test_chain_id'] == chain_id and seq_id in sa['test_seq_id']
                                   and sa['sequence_coverage'] >= LOW_SEQ_COVERAGE), None)
                        if sa is not None:
                            _ref_seq_id_name = 'ref_auth_seq_id' if 'ref_auth_seq_id' in sa else 'ref_seq_id'
                            auth_seq_id = next((ref_seq_id for ref_seq_id, test_seq_id in zip(sa[_ref_seq_id_name], sa['test_seq_id'])
                                                if test_seq_id == seq_id), None)

                if None in (auth_asym_id, auth_seq_id) and br_seq_align is not None:
                    auth_asym_id = next((ca['ref_chain_id'] for ca in br_chain_assign if ca['test_chain_id'] == chain_id), None)
                    if auth_asym_id is not None:
                        sa = next((sa for sa in br_seq_align
                                   if sa['ref_chain_id'] == auth_asym_id and sa['test_chain_id'] == chain_id and seq_id in sa['test_seq_id']
                                   and sa['sequence_coverage'] >= LOW_SEQ_COVERAGE), None)
                        if sa is not None:
                            _ref_seq_id_name = 'ref_auth_seq_id' if 'ref_auth_seq_id' in sa else 'ref_seq_id'
                            auth_seq_id = next((ref_seq_id for ref_seq_id, test_seq_id in zip(sa[_ref_seq_id_name], sa['test_seq_id'])
                                                if test_seq_id == seq_id), None)

                if None in (auth_asym_id, auth_seq_id) and np_seq_align is not None:
                    auth_asym_id = next((ca['ref_chain_id'] for ca in np_chain_assign if ca['test_chain_id'] == chain_id), None)
                    if auth_asym_id is not None:
                        sa = next((sa for sa in np_seq_align
                                   if sa['ref_chain_id'] == auth_asym_id and sa['test_chain_id'] == chain_id and seq_id in sa['test_seq_id']
                                   and sa['sequence_coverage'] >= LOW_SEQ_COVERAGE), None)
                        if sa is not None:
                            _ref_seq_id_name = 'ref_auth_seq_id' if 'ref_auth_seq_id' in sa else 'ref_seq_id'
                            auth_seq_id = next((ref_seq_id for ref_seq_id, test_seq_id in zip(sa[_ref_seq_id_name], sa['test_seq_id'])
                                                if test_seq_id == seq_id), None)

            return auth_asym_id, auth_seq_id

        list_items = ['Details', 'Entry_ID', 'Spectral_peak_list_ID']

        if content_subtype == 'spectral_peak':

            core_items = ['Index_ID', 'ID', 'Volume', 'Volume_uncertainty', 'Height', 'Height_uncertainty']
            aux_items = [item for item in ['Figure_of_merit', 'Restraint'] if item in loop.tags]

            position_item_temps = ['Position_%s', 'Position_uncertainty_%s', 'Line_width_%s', 'Line_width_uncertainty_%s']

            position_items = []

            for dim in range(1, max_dim):
                for idx, position_item_temp in enumerate(position_item_temps):
                    position_item = position_item_temp % dim
                    if idx == 0:
                        position_items.append(position_item)
                    elif position_item in loop.tags:
                        position_items.append(position_item)

            assign_item_temps = ['Entity_assembly_ID_%s', 'Entity_ID_%s', 'Comp_index_ID_%s', 'Seq_ID_%s', 'Comp_ID_%s', 'Atom_ID_%s']
            ambigutity_item_temps = ['Ambiguity_code_%s', 'Ambiguity_set_ID_%s']

            assign_items = []

            for dim in range(1, max_dim):
                for assign_item_temp in assign_item_temps:
                    assign_items.append(assign_item_temp % dim)
                for ambigutity_item_temp in ambigutity_item_temps:
                    ambigutity_item = ambigutity_item_temp % dim
                    if ambigutity_item in loop.tags:
                        assign_items.append(ambigutity_item)

            auth_assign_item_temps = ['Auth_asym_ID_%s', 'Auth_seq_ID_%s', 'Auth_comp_ID_%s', 'Auth_atom_ID_%s']

            auth_assign_items = []

            for dim in range(1, max_dim):
                for auth_assign_item_temp in auth_assign_item_temps:
                    auth_assign_items.append(auth_assign_item_temp % dim)

        else:

            core_items = ['Peak_ID', 'Spectral_dim_ID', 'Set_ID', 'Magnetization_linkage_ID', 'Val']
            aux_items = [item for item in ['Contribution_fractional_val', 'Figure_of_merit', 'Assigned_chem_shift_list_ID', 'Atom_chem_shift_ID']
                         if item in loop.tags]

            assign_items = ['Entity_assembly_ID', 'Entity_ID', 'Comp_index_ID', 'Comp_ID', 'Atom_ID']
            ambigutity_items = ['Ambiguity_code', 'Ambiguity_set_ID']
            for ambiguity_item in ambigutity_items:
                if ambiguity_item in loop.tags:
                    assign_items.append(ambiguity_item)

            auth_assign_items = ['Auth_entity_ID', 'Auth_seq_ID', 'Auth_comp_ID', 'Auth_atom_ID']

        items = core_items
        if len(aux_items) > 0:
            items.extend(aux_items)
        if content_subtype == 'spectral_peak':
            items.extend(position_items)
        items.extend(assign_items)
        items.extend(auth_assign_items)
        items.extend(list_items)

        lp = pynmrstar.Loop.from_scratch(lp_category)

        tags = [lp_category + '.' + item for item in items]

        lp.add_tag(tags)

        prefer_auth_atom_name = False

        if (self.__annotation_mode or self.__native_combined) and len(auth_atom_name_to_id) > 0:

            count_auth_name = count_auth_id = 0

            for row in loop:

                if content_subtype == 'spectral_peak':

                    for dim in range(1, max_dim):
                        has_auth_seq = valid_auth_seq = True
                        for auth_assign_item_temp in auth_assign_item_temps:
                            auth_assign_item = auth_assign_item_temp % dim
                            if auth_assign_item not in loop.tags:
                                has_auth_seq = valid_auth_seq = False
                                break
                        if has_auth_seq:
                            try:
                                auth_asym_id_ = row[loop.tags.index(auth_assign_item_temps[0] % dim)]
                                auth_seq_id_ = int(row[loop.tags.index(auth_assign_item_temps[1] % dim)])
                                comp_id = row[loop.tags.index(auth_assign_item_temps[2] % dim)]
                                atom_id = row[loop.tags.index(auth_assign_item_temps[3] % dim)]
                                seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                                if seq_key not in auth_to_star_seq:
                                    comp_id = next((_auth_comp_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                    if _auth_asym_id == auth_asym_id_ and _auth_seq_id == auth_seq_id_), comp_id)
                                    seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                                    if seq_key not in auth_to_star_seq:
                                        valid_auth_seq = False
                            except (ValueError, TypeError):
                                has_auth_seq = valid_auth_seq = False

                        if valid_auth_seq:

                            if atom_id not in emptyValue:

                                if comp_id in auth_atom_name_to_id:
                                    if atom_id in auth_atom_name_to_id[comp_id]:
                                        count_auth_name += 1
                                    if atom_id in auth_atom_name_to_id[comp_id].values():
                                        count_auth_id += 1

                        else:

                            chain_id = seq_id = comp_id = atom_id = auth_asym_id = auth_seq_id = None

                            for col, assign_item_temp in enumerate(assign_item_temps):
                                assign_item = assign_item_temp % dim
                                if assign_item not in loop.tags:
                                    continue
                                if col == 0:
                                    chain_id = row[loop.tags.index(assign_item)]
                                elif col == 1:
                                    continue
                                elif col == 2:
                                    try:
                                        seq_id = int(row[loop.tags.index(assign_item)])
                                    except (ValueError, TypeError):
                                        pass
                                elif col == 3:
                                    if seq_id is None:
                                        try:
                                            seq_id = int(row[loop.tags.index(assign_item)])
                                        except (ValueError, TypeError):
                                            pass
                                elif col == 4:
                                    comp_id = row[loop.tags.index(assign_item)]
                                    if comp_id not in emptyValue:
                                        comp_id = comp_id.upper()
                                else:
                                    atom_id = row[loop.tags.index(assign_item)]

                            if None not in (chain_id, seq_id):
                                auth_asym_id, auth_seq_id = get_auth_seq_scheme(chain_id, seq_id)

                            if None not in (auth_asym_id, auth_seq_id):
                                seq_key = (auth_asym_id, auth_seq_id, comp_id)
                                if seq_key not in auth_to_star_seq:
                                    comp_id = next((_auth_comp_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                    if _auth_asym_id == auth_asym_id and _auth_seq_id == auth_seq_id), comp_id)
                                    seq_key = (auth_asym_id, auth_seq_id, comp_id)
                                if seq_key in auth_to_star_seq:

                                    if atom_id not in emptyValue:

                                        if comp_id in auth_atom_name_to_id:
                                            if atom_id in auth_atom_name_to_id[comp_id]:
                                                count_auth_name += 1
                                            if atom_id in auth_atom_name_to_id[comp_id].values():
                                                count_auth_id += 1

                else:

                    has_auth_seq = valid_auth_seq = True
                    for auth_assign_item in auth_assign_items:
                        if auth_assign_item not in loop.tags:
                            has_auth_seq = valid_auth_seq = False
                            break
                    if has_auth_seq:
                        try:
                            auth_asym_id_ = row[loop.tags.index(auth_assign_items[0])]
                            auth_seq_id_ = int(row[loop.tags.index(auth_assign_items[1])])
                            comp_id = row[loop.tags.index(auth_assign_items[2])]
                            atom_id = row[loop.tags.index(auth_assign_items[3])]
                            seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                            if seq_key not in auth_to_star_seq:
                                comp_id = next((_auth_comp_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                if _auth_asym_id == auth_asym_id_ and _auth_seq_id == auth_seq_id_), comp_id)
                                seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                                if seq_key not in auth_to_star_seq:
                                    valid_auth_seq = False
                        except (ValueError, TypeError):
                            has_auth_seq = valid_auth_seq = False

                    if valid_auth_seq:

                        if atom_id not in emptyValue:

                            if comp_id in auth_atom_name_to_id:
                                if atom_id in auth_atom_name_to_id[comp_id]:
                                    count_auth_name += 1
                                if atom_id in auth_atom_name_to_id[comp_id].values():
                                    count_auth_id += 1

                    else:

                        chain_id = seq_id = comp_id = atom_id = auth_asym_id = auth_seq_id = None

                        for col, assign_item in enumerate(assign_items):
                            if assign_item not in loop.tags:
                                continue
                            if col == 0:
                                chain_id = row[loop.tags.index(assign_item)]
                            elif col == 1:
                                continue
                            elif col == 2:
                                try:
                                    seq_id = int(row[loop.tags.index(assign_item)])
                                except (ValueError, TypeError):
                                    pass
                            elif col == 3:
                                comp_id = row[loop.tags.index(assign_item)]
                                if comp_id not in emptyValue:
                                    comp_id = comp_id.upper()
                            else:
                                atom_id = row[loop.tags.index(assign_item)]

                        if None not in (chain_id, seq_id):
                            auth_asym_id, auth_seq_id = get_auth_seq_scheme(chain_id, seq_id)

                        if None not in (auth_asym_id, auth_seq_id):
                            seq_key = (auth_asym_id, auth_seq_id, comp_id)
                            if seq_key not in auth_to_star_seq:
                                comp_id = next((_auth_comp_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                if _auth_asym_id == auth_asym_id and _auth_seq_id == auth_seq_id), comp_id)
                                seq_key = (auth_asym_id, auth_seq_id, comp_id)
                            if seq_key in auth_to_star_seq:

                                if atom_id not in emptyValue:

                                    if comp_id in auth_atom_name_to_id:
                                        if atom_id in auth_atom_name_to_id[comp_id]:
                                            count_auth_name += 1
                                        if atom_id in auth_atom_name_to_id[comp_id].values():
                                            count_auth_id += 1

            if count_auth_name + count_auth_id == 0:

                for row in loop:

                    if content_subtype == 'spectral_peak':

                        for dim in range(1, max_dim):
                            has_auth_seq = valid_auth_seq = True
                            for auth_assign_item_temp in auth_assign_item_temps:
                                auth_assign_item = auth_assign_item_temp % dim
                                if auth_assign_item not in loop.tags:
                                    has_auth_seq = valid_auth_seq = False
                                    break
                            if has_auth_seq:
                                try:
                                    auth_asym_id_ = row[loop.tags.index(auth_assign_item_temps[0] % dim)]
                                    auth_seq_id_ = int(row[loop.tags.index(auth_assign_item_temps[1] % dim)])
                                    comp_id = row[loop.tags.index(auth_assign_item_temps[2] % dim)]
                                    atom_id = row[loop.tags.index(auth_assign_item_temps[3] % dim)]
                                    seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                                    if seq_key not in auth_to_star_seq_ann:
                                        valid_auth_seq = False
                                    else:
                                        _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                                        if _seq_key in coord_atom_site:  # DAOTHER-8817
                                            comp_id = coord_atom_site[_seq_key]['comp_id']
                                except (ValueError, TypeError):
                                    has_auth_seq = valid_auth_seq = False

                            if valid_auth_seq:

                                if atom_id not in emptyValue:

                                    if comp_id in auth_atom_name_to_id:
                                        if atom_id in auth_atom_name_to_id[comp_id]:
                                            count_auth_name += 1
                                        if atom_id in auth_atom_name_to_id[comp_id].values():
                                            count_auth_id += 1

                            else:

                                chain_id = seq_id = comp_id = atom_id = auth_asym_id = auth_seq_id = None

                                for col, assign_item_temp in enumerate(assign_item_temps):
                                    assign_item = assign_item_temp % dim
                                    if assign_item not in loop.tags:
                                        continue
                                    if col == 0:
                                        chain_id = row[loop.tags.index(assign_item)]
                                    elif col == 1:
                                        continue
                                    elif col == 2:
                                        try:
                                            seq_id = int(row[loop.tags.index(assign_item)])
                                        except (ValueError, TypeError):
                                            pass
                                    elif col == 3:
                                        if seq_id is None:
                                            try:
                                                seq_id = int(row[loop.tags.index(assign_item)])
                                            except (ValueError, TypeError):
                                                pass
                                    elif col == 4:
                                        comp_id = row[loop.tags.index(assign_item)]
                                        if comp_id not in emptyValue:
                                            comp_id = comp_id.upper()
                                    else:
                                        atom_id = row[loop.tags.index(assign_item)]

                                if None not in (chain_id, seq_id):
                                    auth_asym_id, auth_seq_id = get_auth_seq_scheme(chain_id, seq_id)

                                if None not in (auth_asym_id, auth_seq_id):
                                    seq_key = (auth_asym_id, auth_seq_id, comp_id)
                                    if seq_key in auth_to_star_seq_ann:
                                        _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                                        if _seq_key in coord_atom_site:  # DAOTHER-8817
                                            comp_id = coord_atom_site[_seq_key]['comp_id']

                                        if atom_id not in emptyValue:

                                            if comp_id in auth_atom_name_to_id:
                                                if atom_id in auth_atom_name_to_id[comp_id]:
                                                    count_auth_name += 1
                                                if atom_id in auth_atom_name_to_id[comp_id].values():
                                                    count_auth_id += 1

                    else:

                        has_auth_seq = valid_auth_seq = True
                        for auth_assign_item in auth_assign_items:
                            if auth_assign_item not in loop.tags:
                                has_auth_seq = valid_auth_seq = False
                                break
                        if has_auth_seq:
                            try:
                                auth_asym_id_ = row[loop.tags.index(auth_assign_items[0])]
                                auth_seq_id_ = int(row[loop.tags.index(auth_assign_items[1])])
                                comp_id = row[loop.tags.index(auth_assign_items[2])]
                                atom_id = row[loop.tags.index(auth_assign_items[3])]
                                seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                                if seq_key not in auth_to_star_seq:
                                    valid_auth_seq = False
                                else:
                                    _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                                    if _seq_key in coord_atom_site:  # DAOTHER-8817
                                        comp_id = coord_atom_site[_seq_key]['comp_id']
                            except (ValueError, TypeError):
                                has_auth_seq = valid_auth_seq = False

                        if valid_auth_seq:

                            if atom_id not in emptyValue:

                                if comp_id in auth_atom_name_to_id:
                                    if atom_id in auth_atom_name_to_id[comp_id]:
                                        count_auth_name += 1
                                    if atom_id in auth_atom_name_to_id[comp_id].values():
                                        count_auth_id += 1

                        else:

                            chain_id = seq_id = comp_id = atom_id = auth_asym_id = auth_seq_id = None

                            for col, assign_item in enumerate(assign_items):
                                if assign_item not in loop.tags:
                                    continue
                                if col == 0:
                                    chain_id = row[loop.tags.index(assign_item)]
                                elif col == 1:
                                    continue
                                elif col == 2:
                                    try:
                                        seq_id = int(row[loop.tags.index(assign_item)])
                                    except (ValueError, TypeError):
                                        pass
                                elif col == 3:
                                    comp_id = row[loop.tags.index(assign_item)]
                                    if comp_id not in emptyValue:
                                        comp_id = comp_id.upper()
                                else:
                                    atom_id = row[loop.tags.index(assign_item)]

                            if None not in (chain_id, seq_id):
                                auth_asym_id, auth_seq_id = get_auth_seq_scheme(chain_id, seq_id)

                            if None not in (auth_asym_id, auth_seq_id):
                                seq_key = (auth_asym_id, auth_seq_id, comp_id)
                                if seq_key in auth_to_star_seq_ann:
                                    _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                                    if _seq_key in coord_atom_site:  # DAOTHER-8817
                                        comp_id = coord_atom_site[_seq_key]['comp_id']

                                    if atom_id not in emptyValue:

                                        if comp_id in auth_atom_name_to_id:
                                            if atom_id in auth_atom_name_to_id[comp_id]:
                                                count_auth_name += 1
                                            if atom_id in auth_atom_name_to_id[comp_id].values():
                                                count_auth_id += 1

            prefer_auth_atom_name = count_auth_name > count_auth_id

        index = 1

        for idx, row in enumerate(loop):

            _row = [None] * len(tags)

            for col, item in enumerate(loop.tags):
                if item in items:
                    _row[items.index(item)] = row[col]

            if content_subtype == 'spectral_peak':

                _row[0] = index

                for dim in range(1, max_dim):
                    has_auth_seq = valid_auth_seq = True
                    for auth_assign_item_temp in auth_assign_item_temps:
                        auth_assign_item = auth_assign_item_temp % dim
                        if auth_assign_item not in loop.tags:
                            has_auth_seq = valid_auth_seq = False
                            break
                    if has_auth_seq:
                        try:
                            auth_asym_id_ = row[loop.tags.index(auth_assign_item_temps[0] % dim)]
                            auth_seq_id_ = int(row[loop.tags.index(auth_assign_item_temps[1] % dim)])
                            comp_id = row[loop.tags.index(auth_assign_item_temps[2] % dim)]
                            atom_id = row[loop.tags.index(auth_assign_item_temps[3] % dim)]
                            seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                            if seq_key not in auth_to_star_seq:
                                if self.__annotation_mode:
                                    comp_id = next((_auth_comp_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                    if _auth_asym_id == auth_asym_id_ and _auth_seq_id == auth_seq_id_), comp_id)
                                    seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                                    if seq_key not in auth_to_star_seq:
                                        valid_auth_seq = False
                                elif seq_key not in auth_to_star_seq_ann:
                                    valid_auth_seq = False
                        except (ValueError, TypeError):
                            has_auth_seq = valid_auth_seq = False

                    if valid_auth_seq:
                        try:
                            entity_assembly_id, seq_id, entity_id, _ = auth_to_star_seq[seq_key]
                            _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                            if _seq_key in coord_atom_site:  # DAOTHER-8817
                                _coord_atom_site = coord_atom_site[_seq_key]
                                if 'chain_id' in _coord_atom_site:
                                    auth_asym_id = _coord_atom_site['chain_id']
                                comp_id = _coord_atom_site['comp_id']
                        except KeyError:
                            entity_assembly_id = seq_id = entity_id = None
                            if self.__annotation_mode:
                                auth_asym_id_ = next((_auth_asym_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                      if _auth_seq_id == auth_seq_id_ and _auth_comp_id == comp_id), auth_asym_id_)
                                seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                                if seq_key in auth_to_star_seq:
                                    row[loop.tags.index(auth_assign_item_temps[0] % dim)] = auth_asym_id
                                    entity_assembly_id, seq_id, entity_id, _ = auth_to_star_seq[seq_key]
                                else:
                                    auth_asym_id_, comp_id = next(((_auth_asym_id, _auth_comp_id)
                                                                   for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                                   if _auth_seq_id == auth_seq_id_), (auth_asym_id_, comp_id))
                                    seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                                    if seq_key in auth_to_star_seq:
                                        row[loop.tags.index(auth_assign_item_temps[0] % dim)] = auth_asym_id
                                        entity_assembly_id, seq_id, entity_id, _ = auth_to_star_seq[seq_key]

                        if prefer_auth_atom_name:
                            _atom_id = atom_id
                            _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                            if _seq_key in coord_atom_site:
                                _coord_atom_site = coord_atom_site[_seq_key]
                                if comp_id in auth_atom_name_to_id and comp_id == _coord_atom_site['comp_id']\
                                   and _atom_id in auth_atom_name_to_id[comp_id]:
                                    if auth_atom_name_to_id[comp_id][_atom_id] in _coord_atom_site['atom_id']:
                                        atom_id = auth_atom_name_to_id[comp_id][_atom_id]
                                if 'alt_atom_id' in _coord_atom_site and _atom_id in _coord_atom_site['alt_atom_id']\
                                   and comp_id == _coord_atom_site['comp_id']:
                                    atom_id = _coord_atom_site['atom_id'][_coord_atom_site['alt_atom_id'].index(_atom_id)]
                                # DAOTHER-8751, 8817 (D_1300043061)
                                elif 'alt_comp_id' in _coord_atom_site and 'alt_atom_id' in _coord_atom_site\
                                     and _atom_id in _coord_atom_site['alt_atom_id']\
                                     and comp_id == _coord_atom_site['alt_comp_id'][_coord_atom_site['alt_atom_id'].index(_atom_id)]:
                                    # 'Entity_assembly_ID', 'Entity_ID', 'Comp_index_ID', 'Seq_ID', 'Comp_ID', 'Auth_asym_ID', 'Auth_seq_ID'
                                    cca_row = next((cca_row for cca_row in self.__cca_dat
                                                    if cca_row[4] == comp_id and cca_row[5] == _seq_key[0] and cca_row[6] == _seq_key[1]), None)
                                    if cca_row is not None:
                                        entity_assembly_id, entity_id, seq_id = cca_row[0], cca_row[1], cca_row[2]
                                    if comp_id in auth_atom_name_to_id_ext and _atom_id in auth_atom_name_to_id_ext[comp_id]\
                                       and len(set(_coord_atom_site['alt_comp_id'])) > 1:
                                        atom_id = auth_atom_name_to_id_ext[comp_id][_atom_id]
                                    else:
                                        atom_id = _coord_atom_site['atom_id'][_coord_atom_site['alt_atom_id'].index(_atom_id)]
                                elif 'split_comp_id' in _coord_atom_site:
                                    for _comp_id in _coord_atom_site['split_comp_id']:
                                        if _comp_id == comp_id:
                                            continue
                                        __seq_key = (_seq_key[0], _seq_key[1], _comp_id)
                                        if __seq_key not in coord_atom_site:
                                            continue
                                        __coord_atom_site = coord_atom_site[__seq_key]
                                        if 'alt_comp_id' in __coord_atom_site and 'alt_atom_id' in __coord_atom_site\
                                           and _atom_id in __coord_atom_site['alt_atom_id']:
                                            comp_id = _comp_id
                                            # 'Entity_assembly_ID', 'Entity_ID', 'Comp_index_ID', 'Seq_ID', 'Comp_ID', 'Auth_asym_ID', 'Auth_seq_ID'
                                            cca_row = next((cca_row for cca_row in self.__cca_dat
                                                            if cca_row[4] == comp_id and cca_row[5] == _seq_key[0] and cca_row[6] == _seq_key[1]), None)
                                            if cca_row is not None:
                                                entity_assembly_id, entity_id, seq_id = cca_row[0], cca_row[1], cca_row[2]
                                            atom_id = __coord_atom_site['atom_id'][__coord_atom_site['alt_atom_id'].index(_atom_id)]
                                            break
                                        if _atom_id in __coord_atom_site['atom_id']:
                                            comp_id = _comp_id
                                            # 'Entity_assembly_ID', 'Entity_ID', 'Comp_index_ID', 'Seq_ID', 'Comp_ID', 'Auth_asym_ID', 'Auth_seq_ID'
                                            cca_row = next((cca_row for cca_row in self.__cca_dat
                                                            if cca_row[4] == comp_id and cca_row[5] == _seq_key[0] and cca_row[6] == _seq_key[1]), None)
                                            if cca_row is not None:
                                                entity_assembly_id, entity_id, seq_id = cca_row[0], cca_row[1], cca_row[2]
                                            break

                        for col, assign_item_temp in enumerate(assign_item_temps):
                            assign_item = assign_item_temp % dim
                            if col == 0:
                                _row[items.index(assign_item)] = entity_assembly_id
                            elif col == 1:
                                _row[items.index(assign_item)] = entity_id
                            elif col in (2, 3):
                                _row[items.index(assign_item)] = seq_id
                            elif col == 4:
                                _row[items.index(assign_item)] = comp_id
                            else:
                                _row[items.index(assign_item)] = atom_id

                    else:

                        chain_id = seq_id = comp_id = atom_id = auth_asym_id = auth_seq_id = None

                        for col, assign_item_temp in enumerate(assign_item_temps):
                            assign_item = assign_item_temp % dim
                            if assign_item not in loop.tags:
                                continue
                            if col == 0:
                                chain_id = row[loop.tags.index(assign_item)]
                            elif col == 1:
                                continue
                            elif col == 2:
                                try:
                                    seq_id = int(row[loop.tags.index(assign_item)])
                                except (ValueError, TypeError):
                                    pass
                            elif col == 3:
                                if seq_id is None:
                                    try:
                                        seq_id = int(row[loop.tags.index(assign_item)])
                                    except (ValueError, TypeError):
                                        pass
                            elif col == 4:
                                comp_id = row[loop.tags.index(assign_item)]
                                if comp_id not in emptyValue:
                                    comp_id = comp_id.upper()
                            else:
                                atom_id = row[loop.tags.index(assign_item)]

                        if None not in (chain_id, seq_id):
                            auth_asym_id, auth_seq_id = get_auth_seq_scheme(chain_id, seq_id)

                        if None not in (auth_asym_id, auth_seq_id):
                            seq_key = (auth_asym_id, auth_seq_id, comp_id)
                            if self.__annotation_mode and seq_key not in auth_to_star_seq:
                                comp_id = next((_auth_comp_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                if _auth_asym_id == auth_asym_id and _auth_seq_id == auth_seq_id), comp_id)
                                seq_key = (auth_asym_id, auth_seq_id, comp_id)
                            if seq_key in auth_to_star_seq:
                                entity_assembly_id, seq_id, entity_id, _ = auth_to_star_seq[seq_key]
                                _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                                if _seq_key in coord_atom_site:  # DAOTHER-8817
                                    _coord_atom_site = coord_atom_site[_seq_key]
                                    if 'chain_id' in _coord_atom_site:
                                        auth_asym_id = _coord_atom_site['chain_id']
                                    comp_id = _coord_atom_site['comp_id']

                                if prefer_auth_atom_name:
                                    _atom_id = atom_id
                                    _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                                    if _seq_key in coord_atom_site:
                                        _coord_atom_site = coord_atom_site[_seq_key]
                                        if comp_id in auth_atom_name_to_id and comp_id == _coord_atom_site['comp_id']\
                                           and _atom_id in auth_atom_name_to_id[comp_id]:
                                            if auth_atom_name_to_id[comp_id][_atom_id] in _coord_atom_site['atom_id']:
                                                atom_id = auth_atom_name_to_id[comp_id][_atom_id]
                                        if 'alt_atom_id' in _coord_atom_site and _atom_id in _coord_atom_site['alt_atom_id']\
                                           and comp_id == _coord_atom_site['comp_id']:
                                            atom_id = _coord_atom_site['atom_id'][_coord_atom_site['alt_atom_id'].index(_atom_id)]
                                        # DAOTHER-8751, 8817 (D_1300043061)
                                        elif 'alt_comp_id' in _coord_atom_site and 'alt_atom_id' in _coord_atom_site\
                                             and _atom_id in _coord_atom_site['alt_atom_id']\
                                             and comp_id == _coord_atom_site['alt_comp_id'][_coord_atom_site['alt_atom_id'].index(_atom_id)]:
                                            # 'Entity_assembly_ID', 'Entity_ID', 'Comp_index_ID', 'Seq_ID', 'Comp_ID', 'Auth_asym_ID', 'Auth_seq_ID'
                                            cca_row = next((cca_row for cca_row in self.__cca_dat
                                                            if cca_row[4] == comp_id and cca_row[5] == _seq_key[0] and cca_row[6] == _seq_key[1]), None)
                                            if cca_row is not None:
                                                entity_assembly_id, entity_id, seq_id = cca_row[0], cca_row[1], cca_row[2]
                                            if comp_id in auth_atom_name_to_id_ext and _atom_id in auth_atom_name_to_id_ext[comp_id]\
                                               and len(set(_coord_atom_site['alt_comp_id'])) > 1:
                                                atom_id = auth_atom_name_to_id_ext[comp_id][_atom_id]
                                            else:
                                                atom_id = _coord_atom_site['atom_id'][_coord_atom_site['alt_atom_id'].index(_atom_id)]
                                        elif 'split_comp_id' in _coord_atom_site:
                                            for _comp_id in _coord_atom_site['split_comp_id']:
                                                if _comp_id == comp_id:
                                                    continue
                                                __seq_key = (_seq_key[0], _seq_key[1], _comp_id)
                                                if __seq_key not in coord_atom_site:
                                                    continue
                                                __coord_atom_site = coord_atom_site[__seq_key]
                                                if 'alt_comp_id' in __coord_atom_site and 'alt_atom_id' in __coord_atom_site\
                                                   and _atom_id in __coord_atom_site['alt_atom_id']:
                                                    comp_id = _comp_id
                                                    # 'Entity_assembly_ID', 'Entity_ID', 'Comp_index_ID', 'Seq_ID', 'Comp_ID', 'Auth_asym_ID', 'Auth_seq_ID'
                                                    cca_row = next((cca_row for cca_row in self.__cca_dat
                                                                    if cca_row[4] == comp_id and cca_row[5] == _seq_key[0] and cca_row[6] == _seq_key[1]), None)
                                                    if cca_row is not None:
                                                        entity_assembly_id, entity_id, seq_id = cca_row[0], cca_row[1], cca_row[2]
                                                    atom_id = __coord_atom_site['atom_id'][__coord_atom_site['alt_atom_id'].index(_atom_id)]
                                                    break
                                                if _atom_id in __coord_atom_site['atom_id']:
                                                    comp_id = _comp_id
                                                    # 'Entity_assembly_ID', 'Entity_ID', 'Comp_index_ID', 'Seq_ID', 'Comp_ID', 'Auth_asym_ID', 'Auth_seq_ID'
                                                    cca_row = next((cca_row for cca_row in self.__cca_dat
                                                                    if cca_row[4] == comp_id and cca_row[5] == _seq_key[0] and cca_row[6] == _seq_key[1]), None)
                                                    if cca_row is not None:
                                                        entity_assembly_id, entity_id, seq_id = cca_row[0], cca_row[1], cca_row[2]
                                                    break

                                for col, assign_item_temp in enumerate(assign_item_temps):
                                    assign_item = assign_item_temp % dim
                                    if col == 0:
                                        _row[items.index(assign_item)] = entity_assembly_id
                                    elif col == 1:
                                        _row[items.index(assign_item)] = entity_id
                                    elif col in (2, 3):
                                        _row[items.index(assign_item)] = seq_id
                                    elif col == 4:
                                        _row[items.index(assign_item)] = comp_id
                                    else:
                                        _row[items.index(assign_item)] = atom_id

                                for col, auth_assign_item_temp in enumerate(auth_assign_item_temps):
                                    auth_assign_item = auth_assign_item_temp % dim
                                    if col == 0:
                                        _row[items.index(auth_assign_item)] = auth_asym_id
                                    elif col == 1:
                                        _row[items.index(auth_assign_item)] = auth_seq_id
                                    elif col == 2:
                                        _row[items.index(auth_assign_item)] = comp_id
                                    else:
                                        _row[items.index(auth_assign_item)] = atom_id

            else:

                has_auth_seq = valid_auth_seq = True
                for auth_assign_item in auth_assign_items:
                    if auth_assign_item not in loop.tags:
                        has_auth_seq = valid_auth_seq = False
                        break
                if has_auth_seq:
                    try:
                        auth_asym_id_ = row[loop.tags.index(auth_assign_items[0])]
                        auth_seq_id_ = int(row[loop.tags.index(auth_assign_items[1])])
                        comp_id = row[loop.tags.index(auth_assign_items[2])]
                        atom_id = row[loop.tags.index(auth_assign_items[3])]
                        seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                        if seq_key not in auth_to_star_seq:
                            if self.__annotation_mode:
                                comp_id = next((_auth_comp_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                if _auth_asym_id == auth_asym_id_ and _auth_seq_id == auth_seq_id_), comp_id)
                                seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                                if seq_key not in auth_to_star_seq:
                                    valid_auth_seq = False
                            elif seq_key not in auth_to_star_seq_ann:
                                valid_auth_seq = False
                    except (ValueError, TypeError):
                        has_auth_seq = valid_auth_seq = False

                if valid_auth_seq:
                    try:
                        entity_assembly_id, seq_id, entity_id, _ = auth_to_star_seq[seq_key]
                        _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                        if _seq_key in coord_atom_site:  # DAOTHER-8817
                            _coord_atom_site = coord_atom_site[_seq_key]
                            if 'chain_id' in _coord_atom_site:
                                auth_asym_id = _coord_atom_site['chain_id']
                            comp_id = _coord_atom_site['comp_id']
                    except KeyError:
                        entity_assembly_id = seq_id = entity_id = None
                        if self.__annotation_mode:
                            auth_asym_id_ = next((_auth_asym_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                  if _auth_seq_id == auth_seq_id_ and _auth_comp_id == comp_id), auth_asym_id_)
                            seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                            if seq_key in auth_to_star_seq:
                                row[loop.tags.index(auth_assign_items[0])] = auth_asym_id_
                                entity_assembly_id, seq_id, entity_id, _ = auth_to_star_seq[seq_key]
                            else:
                                auth_asym_id_, comp_id = next(((_auth_asym_id, _auth_comp_id)
                                                               for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                               if _auth_seq_id == auth_seq_id_), (auth_asym_id_, comp_id))
                                seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                                if seq_key in auth_to_star_seq:
                                    row[loop.tags.index(auth_assign_items[0])] = auth_asym_id_
                                    entity_assembly_id, seq_id, entity_id, _ = auth_to_star_seq[seq_key]

                    if prefer_auth_atom_name:
                        _atom_id = atom_id
                        _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                        if _seq_key in coord_atom_site:
                            _coord_atom_site = coord_atom_site[_seq_key]
                            if comp_id in auth_atom_name_to_id and comp_id == _coord_atom_site['comp_id']\
                               and _atom_id in auth_atom_name_to_id[comp_id]:
                                if auth_atom_name_to_id[comp_id][_atom_id] in _coord_atom_site['atom_id']:
                                    atom_id = auth_atom_name_to_id[comp_id][_atom_id]
                            if 'alt_atom_id' in _coord_atom_site and _atom_id in _coord_atom_site['alt_atom_id']\
                               and comp_id == _coord_atom_site['comp_id']:
                                atom_id = _coord_atom_site['atom_id'][_coord_atom_site['alt_atom_id'].index(_atom_id)]
                            # DAOTHER-8751, 8817 (D_1300043061)
                            elif 'alt_comp_id' in _coord_atom_site and 'alt_atom_id' in _coord_atom_site\
                                 and _atom_id in _coord_atom_site['alt_atom_id']\
                                 and comp_id == _coord_atom_site['alt_comp_id'][_coord_atom_site['alt_atom_id'].index(_atom_id)]:
                                # 'Entity_assembly_ID', 'Entity_ID', 'Comp_index_ID', 'Seq_ID', 'Comp_ID', 'Auth_asym_ID', 'Auth_seq_ID'
                                cca_row = next((cca_row for cca_row in self.__cca_dat
                                                if cca_row[4] == comp_id and cca_row[5] == _seq_key[0] and cca_row[6] == _seq_key[1]), None)
                                if cca_row is not None:
                                    entity_assembly_id, entity_id, seq_id = cca_row[0], cca_row[1], cca_row[2]
                                if comp_id in auth_atom_name_to_id_ext and _atom_id in auth_atom_name_to_id_ext[comp_id]\
                                   and len(set(_coord_atom_site['alt_comp_id'])) > 1:
                                    atom_id = auth_atom_name_to_id_ext[comp_id][_atom_id]
                                else:
                                    atom_id = _coord_atom_site['atom_id'][_coord_atom_site['alt_atom_id'].index(_atom_id)]
                            elif 'split_comp_id' in _coord_atom_site:
                                for _comp_id in _coord_atom_site['split_comp_id']:
                                    if _comp_id == comp_id:
                                        continue
                                    __seq_key = (_seq_key[0], _seq_key[1], _comp_id)
                                    if __seq_key not in coord_atom_site:
                                        continue
                                    __coord_atom_site = coord_atom_site[__seq_key]
                                    if 'alt_comp_id' in __coord_atom_site and 'alt_atom_id' in __coord_atom_site\
                                       and _atom_id in __coord_atom_site['alt_atom_id']:
                                        comp_id = _comp_id
                                        # 'Entity_assembly_ID', 'Entity_ID', 'Comp_index_ID', 'Seq_ID', 'Comp_ID', 'Auth_asym_ID', 'Auth_seq_ID'
                                        cca_row = next((cca_row for cca_row in self.__cca_dat
                                                        if cca_row[4] == comp_id and cca_row[5] == _seq_key[0] and cca_row[6] == _seq_key[1]), None)
                                        if cca_row is not None:
                                            entity_assembly_id, entity_id, seq_id = cca_row[0], cca_row[1], cca_row[2]
                                        atom_id = __coord_atom_site['atom_id'][__coord_atom_site['alt_atom_id'].index(_atom_id)]
                                        break
                                    if _atom_id in __coord_atom_site['atom_id']:
                                        comp_id = _comp_id
                                        # 'Entity_assembly_ID', 'Entity_ID', 'Comp_index_ID', 'Seq_ID', 'Comp_ID', 'Auth_asym_ID', 'Auth_seq_ID'
                                        cca_row = next((cca_row for cca_row in self.__cca_dat
                                                        if cca_row[4] == comp_id and cca_row[5] == _seq_key[0] and cca_row[6] == _seq_key[1]), None)
                                        if cca_row is not None:
                                            entity_assembly_id, entity_id, seq_id = cca_row[0], cca_row[1], cca_row[2]
                                        break

                    for col, assign_item in enumerate(assign_items):
                        if col == 0:
                            _row[items.index(assign_item)] = entity_assembly_id
                        elif col == 1:
                            _row[items.index(assign_item)] = entity_id
                        elif col == 2:
                            _row[items.index(assign_item)] = seq_id
                        elif col == 3:
                            _row[items.index(assign_item)] = comp_id
                        else:
                            _row[items.index(assign_item)] = atom_id

                else:

                    chain_id = seq_id = comp_id = atom_id = auth_asym_id = auth_seq_id = None

                    for col, assign_item in enumerate(assign_items):
                        if assign_item not in loop.tags:
                            continue
                        if col == 0:
                            chain_id = row[loop.tags.index(assign_item)]
                        elif col == 1:
                            continue
                        elif col == 2:
                            try:
                                seq_id = int(row[loop.tags.index(assign_item)])
                            except (ValueError, TypeError):
                                pass
                        elif col == 3:
                            comp_id = row[loop.tags.index(assign_item)]
                            if comp_id not in emptyValue:
                                comp_id = comp_id.upper()
                        else:
                            atom_id = row[loop.tags.index(assign_item)]

                    if None not in (chain_id, seq_id):
                        auth_asym_id, auth_seq_id = get_auth_seq_scheme(chain_id, seq_id)

                    if None not in (auth_asym_id, auth_seq_id):
                        seq_key = (auth_asym_id, auth_seq_id, comp_id)
                        if self.__annotation_mode and seq_key not in auth_to_star_seq:
                            comp_id = next((_auth_comp_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                            if _auth_asym_id == auth_asym_id and _auth_seq_id == auth_seq_id), comp_id)
                            seq_key = (auth_asym_id, auth_seq_id, comp_id)
                        if seq_key in auth_to_star_seq:
                            entity_assembly_id, seq_id, entity_id, _ = auth_to_star_seq[seq_key]
                            _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                            if _seq_key in coord_atom_site:  # DAOTHER-8817
                                _coord_atom_site = coord_atom_site[_seq_key]
                                if 'chain_id' in _coord_atom_site:
                                    auth_asym_id = _coord_atom_site['chain_id']
                                comp_id = _coord_atom_site['comp_id']

                            if prefer_auth_atom_name:
                                _atom_id = atom_id
                                _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                                if _seq_key in coord_atom_site:
                                    _coord_atom_site = coord_atom_site[_seq_key]
                                    if comp_id in auth_atom_name_to_id and comp_id == _coord_atom_site['comp_id']\
                                       and _atom_id in auth_atom_name_to_id[comp_id]:
                                        if auth_atom_name_to_id[comp_id][_atom_id] in _coord_atom_site['atom_id']:
                                            atom_id = auth_atom_name_to_id[comp_id][_atom_id]
                                    if 'alt_atom_id' in _coord_atom_site and _atom_id in _coord_atom_site['alt_atom_id']\
                                       and comp_id == _coord_atom_site['comp_id']:
                                        atom_id = _coord_atom_site['atom_id'][_coord_atom_site['alt_atom_id'].index(_atom_id)]
                                    # DAOTHER-8751, 8817 (D_1300043061)
                                    elif 'alt_comp_id' in _coord_atom_site and 'alt_atom_id' in _coord_atom_site\
                                         and _atom_id in _coord_atom_site['alt_atom_id']\
                                         and comp_id == _coord_atom_site['alt_comp_id'][_coord_atom_site['alt_atom_id'].index(_atom_id)]:
                                        # 'Entity_assembly_ID', 'Entity_ID', 'Comp_index_ID', 'Seq_ID', 'Comp_ID', 'Auth_asym_ID', 'Auth_seq_ID'
                                        cca_row = next((cca_row for cca_row in self.__cca_dat
                                                        if cca_row[4] == comp_id and cca_row[5] == _seq_key[0] and cca_row[6] == _seq_key[1]), None)
                                        if cca_row is not None:
                                            entity_assembly_id, entity_id, seq_id = cca_row[0], cca_row[1], cca_row[2]
                                        if comp_id in auth_atom_name_to_id_ext and _atom_id in auth_atom_name_to_id_ext[comp_id]\
                                           and len(set(_coord_atom_site['alt_comp_id'])) > 1:
                                            atom_id = auth_atom_name_to_id_ext[comp_id][_atom_id]
                                        else:
                                            atom_id = _coord_atom_site['atom_id'][_coord_atom_site['alt_atom_id'].index(_atom_id)]
                                    elif 'split_comp_id' in _coord_atom_site:
                                        for _comp_id in _coord_atom_site['split_comp_id']:
                                            if _comp_id == comp_id:
                                                continue
                                            __seq_key = (_seq_key[0], _seq_key[1], _comp_id)
                                            if __seq_key not in coord_atom_site:
                                                continue
                                            __coord_atom_site = coord_atom_site[__seq_key]
                                            if 'alt_comp_id' in __coord_atom_site and 'alt_atom_id' in __coord_atom_site\
                                               and _atom_id in __coord_atom_site['alt_atom_id']:
                                                comp_id = _comp_id
                                                # 'Entity_assembly_ID', 'Entity_ID', 'Comp_index_ID', 'Seq_ID', 'Comp_ID', 'Auth_asym_ID', 'Auth_seq_ID'
                                                cca_row = next((cca_row for cca_row in self.__cca_dat
                                                                if cca_row[4] == comp_id and cca_row[5] == _seq_key[0] and cca_row[6] == _seq_key[1]), None)
                                                if cca_row is not None:
                                                    entity_assembly_id, entity_id, seq_id = cca_row[0], cca_row[1], cca_row[2]
                                                atom_id = __coord_atom_site['atom_id'][__coord_atom_site['alt_atom_id'].index(_atom_id)]
                                                break
                                            if _atom_id in __coord_atom_site['atom_id']:
                                                comp_id = _comp_id
                                                # 'Entity_assembly_ID', 'Entity_ID', 'Comp_index_ID', 'Seq_ID', 'Comp_ID', 'Auth_asym_ID', 'Auth_seq_ID'
                                                cca_row = next((cca_row for cca_row in self.__cca_dat
                                                                if cca_row[4] == comp_id and cca_row[5] == _seq_key[0] and cca_row[6] == _seq_key[1]), None)
                                                if cca_row is not None:
                                                    entity_assembly_id, entity_id, seq_id = cca_row[0], cca_row[1], cca_row[2]
                                                break

                            for col, assign_item in enumerate(assign_items):
                                if col == 0:
                                    _row[items.index(assign_item)] = entity_assembly_id
                                elif col == 1:
                                    _row[items.index(assign_item)] = entity_id
                                elif col == 2:
                                    _row[items.index(assign_item)] = seq_id
                                elif col == 3:
                                    _row[items.index(assign_item)] = comp_id
                                else:
                                    _row[items.index(assign_item)] = atom_id

                            for col, auth_assign_item in enumerate(auth_assign_items):
                                if col == 0:
                                    _row[items.index(auth_assign_item)] = auth_asym_id
                                elif col == 1:
                                    _row[items.index(auth_assign_item)] = auth_seq_id
                                elif col == 2:
                                    _row[items.index(auth_assign_item)] = comp_id
                                else:
                                    _row[items.index(auth_assign_item)] = atom_id

            _row[-2] = self.__entry_id
            _row[-1] = list_id

            lp.add_data(_row)

            index += 1

        del sf[loop]

        sf.add_loop(lp)

        self.__c2S.set_entry_id(sf, self.__entry_id)
        self.__c2S.set_local_sf_id(sf, list_id)

        get_auth_seq_scheme.cache_clear()

        return True

    def testCoordAtomIdConsistency(self, file_list_id: int, file_name: str, file_type: str, content_subtype: str,
                                   sf: Union[pynmrstar.Saveframe, pynmrstar.Loop],
                                   list_id: int, sf_framecode: str, lp_category: str, cif_poly_seq: List[dict],
                                   seq_align_dic: dict, nmr2ca: dict, ref_chain_id: str) -> bool:
        """ Perform consistency test on atom names of coordinate file.
        """

        modified = False

        index_tag = INDEX_TAGS[file_type][content_subtype] if content_subtype != 'poly_seq' else None

        if file_type == 'nef' or not self.__nonblk_bad_nterm:

            if content_subtype != 'poly_seq':
                lp_data = next((lp['data'] for lp in self.__lp_data[content_subtype]
                                if lp['file_name'] == file_name and lp['sf_framecode'] == sf_framecode), None)
            else:
                lp_data = next((lp['data'] for lp in self.__aux_data[content_subtype]
                                if lp['file_name'] == file_name and lp['sf_framecode'] == sf_framecode
                                and lp['category'] == lp_category), None)

        else:

            if content_subtype == 'spectral_peak':

                try:

                    _num_dim = get_first_sf_tag(sf, NUM_DIM_ITEMS[file_type])
                    num_dim = int(_num_dim)

                    if num_dim not in range(1, MAX_DIM_NUM_OF_SPECTRA):
                        raise ValueError()

                except ValueError:  # raised error already at testIndexConsistency()
                    return False

                max_dim = num_dim + 1

                key_items = []
                for dim in range(1, max_dim):
                    for k in PK_KEY_ITEMS[file_type]:
                        if k['type'] == 'float':  # position
                            _k = copy.copy(k)
                            if '%s' in k['name']:
                                _k['name'] = k['name'] % dim
                            key_items.append(_k)
                for k in PK_KEY_ITEMS[file_type]:
                    if k['type'] == 'positive-int':  # peak_id
                        key_items.append(k)

                data_items = []
                for d in DATA_ITEMS[file_type][content_subtype]:
                    data_items.append(d)
                for dim in range(1, max_dim):
                    for d in self.pk_data_items[file_type]:
                        _d = copy.copy(d)
                        if '%s' in d['name']:
                            _d['name'] = d['name'] % dim
                        if 'default-from' in d and '%s' in d['default-from']:  # DAOTHER-7421
                            _d['default-from'] = d['default-from'] % dim
                        data_items.append(_d)

            else:

                if content_subtype != 'poly_seq':
                    key_items = self.key_items[file_type][content_subtype]
                    data_items = DATA_ITEMS[file_type][content_subtype]
                else:
                    key_items = self.aux_key_items[file_type][content_subtype][lp_category]
                    data_items = self.aux_data_items[file_type][content_subtype][lp_category]

            try:

                lp_data = self.__nefT.check_data(sf, lp_category, key_items, data_items, None, None, None,
                                                 enforce_allowed_tags=(file_type == 'nmr-star'),
                                                 excl_missing_data=self.__excl_missing_data)[0]

            except Exception:
                return False

        if lp_data is None:
            return False

        has_seq_align = False

        sa_name = 'nmr_poly_seq_vs_' + content_subtype

        if has_key_value(seq_align_dic, sa_name):

            for seq_align in seq_align_dic[sa_name]:

                if seq_align['list_id'] == list_id:
                    has_seq_align = True
                    break

        if not has_seq_align and content_subtype != 'poly_seq':
            return False

        auth_to_star_seq = self.__caC['auth_to_star_seq']
        auth_to_label_seq = self.__caC['auth_to_label_seq']
        auth_to_orig_seq = self.__caC['auth_to_orig_seq']
        label_to_auth_seq = self.__caC['label_to_auth_seq']
        coord_atom_site = self.__caC['coord_atom_site']
        coord_unobs_res = self.__caC['coord_unobs_res']
        coord_unobs_atom = self.__caC['coord_unobs_atom'] if 'coord_unobs_atom' in self.__caC else {}

        if auth_to_star_seq is None:
            return False

        item_names = []

        if content_subtype == 'chem_shift':
            max_dim = 2

            item_names.append(ITEM_NAMES_IN_CS_LOOP[file_type])

        else:

            if content_subtype in ('poly_seq', 'dist_restraint', 'rdc_restraint'):
                max_dim = 3

            elif content_subtype == 'dihed_restraint':
                max_dim = 5

            elif content_subtype == 'spectral_peak':

                try:

                    _num_dim = get_first_sf_tag(sf, NUM_DIM_ITEMS[file_type])
                    num_dim = int(_num_dim)

                    if num_dim not in range(1, MAX_DIM_NUM_OF_SPECTRA):
                        raise ValueError()

                except ValueError:  # raised error already at testIndexConsistency()
                    return False

                max_dim = num_dim + 1

            else:
                return False

            for j in range(1, max_dim):
                _item_names = {}
                for k, v in ITEM_NAMES_IN_PK_LOOP[file_type].items():
                    if '%s' in v:
                        v = v % j
                    _item_names[k] = v
                item_names.append(_item_names)

        num_dim = max_dim - 1

        chain_id_names, seq_id_names, comp_id_names, atom_id_names = [], [], [], []
        if file_type == 'nmr-star':
            alt_seq_id_names = []

        for j in range(num_dim):
            chain_id_names.append(item_names[j]['chain_id'])
            seq_id_names.append(item_names[j]['seq_id'])
            comp_id_names.append(item_names[j]['comp_id'])
            atom_id_names.append(item_names[j]['atom_id'])
            if file_type == 'nmr-star':
                alt_seq_id_names.append(item_names[j]['alt_seq_id'])

        details_col = -1

        if file_type == 'nmr-star':

            loop = sf if self.__star_data_type[file_list_id] == 'Loop' else sf.get_loop(lp_category)

            if 'Details' in loop.tags:
                details_col = loop.tags.index('Details')

        def get_coord_atom_site_of(chain_id, seq_id, comp_id):

            if (chain_id, seq_id, comp_id) in auth_to_star_seq:
                seq_key = (chain_id, seq_id)

                if seq_key in coord_unobs_res:  # DAOTHER-7665
                    return True, None, None

                if seq_key not in coord_atom_site:
                    return True, None, None

                # 2lit: 1:104:LYS (nmr), A:99:LYS (model) overlaps A:104:HEC (model)
                # if seq_key not in auth_to_label_seq:
                #     return True, None, None

                coord_atom_site_ = coord_atom_site[seq_key]

                cif_comp_id = coord_atom_site_['comp_id']

                if comp_id == cif_comp_id:
                    return True, seq_key, coord_atom_site_

                _seq_key = (chain_id, seq_id, comp_id)

                if _seq_key in auth_to_orig_seq:
                    _seq_key_ = auth_to_orig_seq[_seq_key]

                    seq_key = (chain_id, _seq_key_[0])

                    if seq_key in coord_atom_site:
                        _coord_atom_site_ = coord_atom_site[seq_key]

                        if _coord_atom_site_['comp_id'] == comp_id:
                            return True, seq_key, _coord_atom_site_

            if (chain_id, seq_id) in label_to_auth_seq:
                _chain_id, _seq_id = label_to_auth_seq[(chain_id, seq_id)]

                if (_chain_id, _seq_id, comp_id) in auth_to_star_seq:
                    seq_key = (_chain_id, _seq_id)

                    if seq_key in coord_unobs_res:  # DAOTHER-7665
                        return True, None, None

                    if seq_key not in coord_atom_site:
                        return True, None, None

                    # 2lit: 1:104:LYS (nmr), A:99:LYS (model) overlaps A:104:HEC (model)
                    # if seq_key not in auth_to_label_seq:
                    #     return True, None, None

                    coord_atom_site_ = coord_atom_site[seq_key]

                    cif_comp_id = coord_atom_site_['comp_id']

                    if comp_id == cif_comp_id:
                        return True, seq_key, coord_atom_site_

            return False, None, None

        offset = {}

        for idx, row in enumerate(lp_data):

            for j in range(num_dim):
                try:
                    chain_id = row[chain_id_names[j]]
                    seq_id = alt_seq_id = row[seq_id_names[j]]
                    comp_id = row[comp_id_names[j]]
                    atom_id = row[atom_id_names[j]]
                    if file_type == 'nmr-star' and alt_seq_id_names[j] in row:
                        alt_seq_id = row[alt_seq_id_names[j]]
                except KeyError:
                    continue

                if content_subtype.startswith('spectral_peak')\
                   and (chain_id in emptyValue or seq_id in emptyValue or comp_id in emptyValue or atom_id in emptyValue):
                    continue

                if chain_id not in nmr2ca:
                    continue

                ca = next((ca['seq_align'] for ca in nmr2ca[chain_id]
                           if ('seq_unmap' not in ca or (seq_id not in ca['seq_unmap']))), None)  # DAOTHER-7465

                if ca is None:
                    continue

                cif_chain_id = ca['test_chain_id']

                cif_seq_id = next((test_seq_id for ref_seq_id, test_seq_id
                                   in zip(ca['ref_seq_id'], ca['test_auth_seq_id' if 'test_auth_seq_id' in ca else 'test_seq_id'])
                                   if ref_seq_id == seq_id), None)

                if cif_seq_id is None and ca['sequence_coverage'] >= LOW_SEQ_COVERAGE:
                    continue

                cif_ps = next(ps for ps in cif_poly_seq if ps['chain_id'] == cif_chain_id)

                if 'auth_chain_id' in cif_ps:
                    cif_chain_id = cif_ps['auth_chain_id']

                if ca['sequence_coverage'] < LOW_SEQ_COVERAGE:  # DAOTHER-8751, issue #2

                    if 'auth_seq_id' in cif_ps:
                        cif_seq_id, cif_comp_id = next(((_seq_id, _comp_id) for _auth_seq_id, _seq_id, _comp_id
                                                        in zip(cif_ps['auth_seq_id'], cif_ps['seq_id'], cif_ps['comp_id'])
                                                        if _auth_seq_id == seq_id), (None, None))
                    else:
                        cif_seq_id, cif_comp_id = next(((_seq_id, _comp_id) for _seq_id, _comp_id
                                                        in zip(cif_ps['seq_id'], cif_ps['comp_id'])
                                                        if _seq_id == seq_id), (None, None))

                    if None in (cif_seq_id, cif_comp_id):
                        continue

                else:

                    cif_comp_id = next((_comp_id for _seq_id, _comp_id
                                        in zip(cif_ps['auth_seq_id' if 'auth_seq_id' in cif_ps else 'seq_id'], cif_ps['comp_id'])
                                        if _seq_id == cif_seq_id), None)

                    if cif_comp_id is None:
                        continue

                    if cif_comp_id != comp_id and seq_id != cif_seq_id:
                        cif_comp_id = next((_comp_id for _seq_id, _comp_id
                                            in zip(cif_ps['auth_seq_id' if 'auth_seq_id' in cif_ps else 'seq_id'], cif_ps['comp_id'])
                                            if _seq_id == seq_id), None)

                        if cif_comp_id is None:
                            continue

                        if cif_comp_id == comp_id:
                            cif_seq_id = seq_id

                if ca['sequence_coverage'] < LOW_SEQ_COVERAGE:

                    if 'auth_seq_id' in cif_ps:
                        cif_comp_id = next((_comp_id for _seq_id, _comp_id
                                            in zip(cif_ps['auth_seq_id'], cif_ps['comp_id'])
                                            if _seq_id == seq_id), None)
                    else:
                        cif_comp_id = next((_comp_id for _seq_id, _comp_id
                                            in zip(cif_ps['seq_id'], cif_ps['comp_id'])
                                            if _seq_id == seq_id), None)

                    if cif_comp_id is None:
                        continue

                if file_type == 'nef' or self.isNmrAtomName(comp_id, atom_id):
                    _atom_id, _, details = self.__getAtomIdListWithAmbigCode(comp_id, atom_id)

                    len_atom_id = len(_atom_id)

                    if len_atom_id == 0:
                        continue

                    if len_atom_id == 1 and atom_id == _atom_id[0]:
                        atom_id_ = atom_id
                        atom_name = atom_id

                        if details is not None:
                            atom_name += f", where {details.rstrip('.')}"

                    else:
                        atom_name = f'{atom_id} (e.g. '

                        for atom_id_ in _atom_id:
                            atom_name += f'{atom_id_} '

                        atom_name = f'{atom_name.rstrip()})'

                        # representative atom id
                        atom_id_ = _atom_id[0]

                else:
                    atom_id_ = atom_id
                    atom_name = atom_id

                if len(auth_to_star_seq) == 0:
                    continue

                found, seq_key, coord_atom_site_ = get_coord_atom_site_of(cif_chain_id, cif_seq_id, comp_id)

                if found:

                    if seq_key is None:
                        continue

                    if seq_key in auth_to_label_seq:

                        offset[chain_id] = seq_key[1] - seq_id

                        cif_chain_id, cif_seq_id = auth_to_label_seq[seq_key]
                        cif_comp_id = comp_id

                        if seq_key in coord_unobs_res:  # DAOTHER-7665
                            continue

                else:

                    if chain_id in offset:
                        _, seq_key, coord_atom_site_ = get_coord_atom_site_of(cif_chain_id, cif_seq_id + offset[chain_id], comp_id)

                        if seq_key is not None and seq_key in coord_unobs_res:
                            continue

                    elif seq_key is not None:
                        seq_key = (cif_chain_id, cif_seq_id)

                        if seq_key in coord_unobs_res:  # DAOTHER-7665
                            continue

                        coord_atom_site_ = coord_atom_site.get(seq_key)

                    else:

                        for _offset in range(1, 10):
                            if (cif_chain_id, cif_seq_id + _offset) in label_to_auth_seq:
                                _, _cif_seq_id = label_to_auth_seq[(cif_chain_id, cif_seq_id + _offset)]
                                if (cif_chain_id, _cif_seq_id) in auth_to_label_seq:
                                    cif_seq_id = _cif_seq_id - _offset

                                    seq_key = (cif_chain_id, cif_seq_id)
                                    break

                        if seq_key is not None and seq_key in coord_unobs_res:  # DAOTHER-7665
                            continue

                    if file_type == 'nmr-star' and seq_id != alt_seq_id:

                        if coord_atom_site_ is None or coord_atom_site_['comp_id'] != cif_comp_id\
                           or (atom_id_ not in coord_atom_site_['atom_id']
                               and (('auth_atom_id' in coord_atom_site_ and atom_id_ not in coord_atom_site_['auth_atom_id'])
                                    or 'auth_atom_id' not in coord_atom_site_)):

                            cif_seq_id = next((test_seq_id for ref_seq_id, test_seq_id
                                               in zip(ca['ref_seq_id'], ca['test_auth_seq_id'])
                                               if ref_seq_id == alt_seq_id), None)

                            if cif_seq_id is None:
                                continue

                            cif_ps = next(ps for ps in cif_poly_seq if ps['chain_id'] == cif_chain_id)

                            cif_comp_id = next((_comp_id for _seq_id, _comp_id
                                                in zip(cif_ps['seq_id'], cif_ps['comp_id'])
                                                if _seq_id == cif_seq_id), None)

                            if cif_comp_id is None:
                                continue

                            seq_key = (cif_chain_id, cif_seq_id)

                            if seq_key in coord_unobs_res:  # DAOTHER-7665
                                continue

                            coord_atom_site_ = coord_atom_site.get(seq_key)

                if coord_atom_site_ is None and file_type == 'nmr-star':

                    if max_dim == 2:
                        auth_asym_id_name = 'Auth_asym_ID'
                        auth_seq_id_name = 'Auth_seq_ID'
                    else:
                        auth_asym_id_name = f'Auth_asym_ID_{j + 1}'
                        auth_seq_id_name = f'Auth_seq_ID_{j + 1}'

                    if auth_asym_id_name in row and auth_seq_id_name in row\
                       and row[auth_asym_id_name] not in emptyValue\
                       and row[auth_seq_id_name] not in emptyValue\
                       and (isinstance(row[auth_seq_id_name], int) or row[auth_seq_id_name].isdigit()):
                        cif_chain_id = row[auth_asym_id_name]
                        cif_seq_id = row[auth_seq_id_name]
                        if isinstance(cif_seq_id, str):
                            cif_seq_id = int(cif_seq_id)

                        _, seq_key, coord_atom_site_ = get_coord_atom_site_of(cif_chain_id, cif_seq_id, comp_id)

                        if coord_atom_site_ is not None:
                            cif_comp_id = coord_atom_site_['comp_id']

                if coord_atom_site_ is None or coord_atom_site_['comp_id'] != cif_comp_id\
                   or (atom_id_ not in coord_atom_site_['atom_id']
                       and (('auth_atom_id' in coord_atom_site_ and atom_id_ not in coord_atom_site_['auth_atom_id'])
                            or 'auth_atom_id' not in coord_atom_site_)):

                    idx_msg = ''
                    if index_tag is not None and index_tag in row:
                        idx_msg = f"[Check row of {index_tag} {row[index_tag]}] "

                    err = idx_msg + "Atom ("\
                        + self.getReducedAtomNotation(chain_id_names[j], chain_id, seq_id_names[j], seq_id,
                                                      comp_id_names[j], comp_id, atom_id_names[j], atom_name)\
                        + ") is not present in the coordinates."

                    cyclic = self.isCyclicPolymer(ref_chain_id)

                    if self.__nonblk_bad_nterm\
                       and (seq_id == 1 or cif_seq_id == 1 or ((seq_key[0], seq_key[1] - 1)
                                                               if seq_key is not None else (cif_chain_id, cif_seq_id - 1)) in coord_unobs_res)\
                       and atom_id_ in aminoProtonCode and (cyclic or comp_id == 'PRO'
                                                            or (atom_id_ in protonBeginCode
                                                                or (coord_atom_site_ is not None and 'auth_atom_id' not in coord_atom_site_))):  # DAOTHER-7665

                        err += " However, it is acceptable if corresponding atom name, H1, is given during biocuration "

                        if cyclic:
                            err += "because of a cyclic-peptide."
                        elif comp_id == 'PRO':
                            err += "because polymer sequence starts with the Proline residue."
                        else:  # DAOTHER-7665
                            err += "because polymer sequence starts with the residue in the coordinates."

                        self.report.warning.appendDescription('auth_atom_nomenclature_mismatch',
                                                              {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                               'description': err})
                        self.report.setWarning()

                        if self.__verbose:
                            self.__lfh.write(f"+{self.__class_name__}.testCoordAtomIdConsistency() ++ Warning  - {err}\n")

                        if cyclic and self.__bmrb_only and self.__leave_intl_note and file_type == 'nmr-star' and seq_id == 1 and details_col != -1:
                            _details = loop.data[idx][details_col]
                            details = f"{chain_id}:{seq_id}:{comp_id}:{atom_name} is not present in the coordinates. "\
                                "However, it is acceptable if an appropriate atom name, H1, is given because of a cyclic-peptide.\n"
                            if _details in emptyValue or (details not in _details):
                                if _details in emptyValue:
                                    loop.data[idx][details_col] = details
                                else:
                                    loop.data[idx][details_col] += ('' if '\n' in _details else '\n') + details
                                modified = True

                    elif self.__nonblk_bad_nterm\
                            and (seq_id == 1 or cif_seq_id == 1 or ((seq_key[0], seq_key[1] - 1)
                                                                    if seq_key is not None else (cif_chain_id, cif_seq_id - 1)) in coord_unobs_res)\
                            and atom_id_ == 'P':
                        continue

                    elif ca['conflict'] == 0:  # no conflict in sequenc alignment

                        if comp_id in monDict3:

                            checked = coord_issue = False
                            if atom_id_[0] in protonBeginCode:
                                self.__ccU.updateChemCompDict(comp_id)
                                cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == atom_id_), None)
                                bonded_to = self.__ccU.getBondedAtoms(comp_id, atom_id_)
                                peptide_like = self.__csStat.peptideLike(comp_id)
                                if cca is not None and len(bonded_to) > 0:
                                    if coord_atom_site_ is not None and bonded_to[0] in coord_atom_site_['atom_id']\
                                       and (cca[self.__ccU.ccaLeavingAtomFlag] != 'Y'
                                            or (peptide_like
                                                and cca[self.__ccU.ccaNTerminalAtomFlag] == 'N'
                                                and cca[self.__ccU.ccaCTerminalAtomFlag] == 'N')):
                                        checked = True
                                        err = idx_msg + "Atom ("\
                                            + self.getReducedAtomNotation(chain_id_names[j], chain_id, seq_id_names[j], seq_id,
                                                                          comp_id_names[j], comp_id, atom_id_names[j], atom_name)\
                                            + ") is not properly instantiated in the coordinates. Please re-upload the model file."

                            if (self.__remediation_mode or self.__combined_mode) and checked:
                                continue

                            if not checked and err.endswith("not present in the coordinates."):

                                if atom_id_[0] in protonBeginCode:
                                    bonded_to = self.__ccU.getBondedAtoms(comp_id, atom_id_)
                                    if len(bonded_to) > 0 and coord_atom_site_ is not None and bonded_to[0] not in coord_atom_site_['atom_id']:
                                        err += " Additionally, the attached atom ("\
                                            + self.getReducedAtomNotation(chain_id_names[j], chain_id, seq_id_names[j], seq_id,
                                                                          comp_id_names[j], comp_id, atom_id_names[j], bonded_to[0])\
                                            + ") is not instantiated in the coordinates. Please re-upload the model file."
                                        coord_issue = True

                                elif 'coord_unobs_atom' in self.__caC:
                                    if seq_key in coord_unobs_atom and atom_id_ in coord_unobs_atom[seq_key]['atom_ids']:
                                        coord_issue = True

                            _atom_id, _, _ = self.__getAtomIdListWithAmbigCode(comp_id, atom_id_ + '%')

                            if content_subtype.startswith('spectral_peak')\
                               or (len(_atom_id) > 0 and coord_atom_site_ is not None and _atom_id[0] in coord_atom_site_['atom_id']):

                                if len(_atom_id) > 0 and coord_atom_site_ is not None and _atom_id[0] in coord_atom_site_['atom_id']:
                                    item = 'atom_nomenclature_mismatch'
                                elif content_subtype.startswith('spectral_peak'):
                                    item = 'hydrogen_not_instantiated' if checked else 'coordinate_issue' if coord_issue else 'assigned_peak_atom_not_found'
                                else:
                                    item = 'hydrogen_not_instantiated' if checked else 'coordinate_issue' if coord_issue else 'atom_nomenclature_mismatch'

                                self.report.warning.appendDescription(item,
                                                                      {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                       'description': err})
                                self.report.setWarning()

                                if self.__verbose:
                                    self.__lfh.write(f"+{self.__class_name__}.testCoordAtomIdConsistency() ++ Warning  - {err}\n")

                            else:

                                item = 'hydrogen_not_instantiated' if checked else 'coordinate_issue' if coord_issue else 'atom_not_found'

                                if self.__internal_mode and item in ('hydrogen_not_instantiated', 'coordinate_issue'):

                                    self.report.warning.appendDescription(item,
                                                                          {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                           'description': err})
                                    self.report.setWarning()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.testCoordAtomIdConsistency() ++ Warning  - {err}\n")

                                else:

                                    if item == 'atom_not_found' and self.__internal_mode and file_type == 'nmr-star' and details_col != -1:
                                        _details = loop.data[idx][details_col]
                                        if _details == 'UNMAPPED':
                                            continue

                                    if item == 'atom_not_found' and self.__op == 'nmr-str-replace-cs' and file_list_id > 0:
                                        item = 'atom_nomenclature_mismatch'

                                        self.report.warning.appendDescription(item,
                                                                              {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                               'description': err})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.testCoordAtomIdConsistency() ++ Warning  - {err}\n")

                                        continue

                                    self.report.error.appendDescription(item,
                                                                        {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                         'description': err})
                                    self.report.setError()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.testCoordAtomIdConsistency() ++ Error  - {err}\n")

                        else:

                            if self.__combined_mode and self.__remediation_mode and self.__ccU.updateChemCompDict(comp_id):
                                cca = next((cca for cca in self.__ccU.lastAtomList if cca[self.__ccU.ccaAtomId] == atom_id_), None)
                                bonded_to = self.__ccU.getBondedAtoms(comp_id, atom_id_)
                                peptide_like = self.__csStat.peptideLike(comp_id)
                                if cca is not None and len(bonded_to) > 0:
                                    if coord_atom_site_ is not None and bonded_to[0] in coord_atom_site_['atom_id']\
                                       and (cca[self.__ccU.ccaLeavingAtomFlag] != 'Y'
                                            or (peptide_like
                                                and cca[self.__ccU.ccaNTerminalAtomFlag] == 'N'
                                                and cca[self.__ccU.ccaCTerminalAtomFlag] == 'N')):
                                        err = idx_msg + "Atom ("\
                                            + self.getReducedAtomNotation(chain_id_names[j], chain_id, seq_id_names[j], seq_id,
                                                                          comp_id_names[j], comp_id, atom_id_names[j], atom_name)\
                                            + ") is not properly instantiated in the coordinates. Please re-upload the model file."

                                        self.report.warning.appendDescription('hydrogen_not_instantiated',
                                                                              {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                               'description': err})
                                        self.report.setWarning()

                                        if self.__verbose:
                                            self.__lfh.write(f"+{self.__class_name__}.testCoordAtomIdConsistency() ++ Warning  - {err}\n")

                                        continue

                            self.report.warning.appendDescription('atom_nomenclature_mismatch',
                                                                  {'file_name': file_name, 'sf_framecode': sf_framecode, 'category': lp_category,
                                                                   'description': err})
                            self.report.setWarning()

                            if self.__verbose:
                                self.__lfh.write(f"+{self.__class_name__}.testCoordAtomIdConsistency() ++ Warning  - {err}\n")

        return modified
