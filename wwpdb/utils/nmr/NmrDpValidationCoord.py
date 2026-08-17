##
# File: NmrDpValidationCoord.py
# Date: 17-Aug-2026
#
# Updates:
##
""" Coordinate-derived conformational queries for NMR data validation.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "5.3.0"

from typing import List

try:
    from wwpdb.utils.nmr.NmrDpConstant import (LARGE_ASYM_ID,
                                               LEN_MAJOR_ASYM_ID)
    from wwpdb.utils.nmr.CifToNmrStar import has_key_value
    from wwpdb.utils.nmr.NmrVrptUtility import (write_as_pickle,
                                                to_np_array,
                                                dihedral_angle)
    from wwpdb.utils.nmr.mr.ParserListenerUtil import isLikeHis
    from wwpdb.utils.nmr.NmrDpValidationBase import NmrDpValidationBase
except ImportError:
    from nmr.NmrDpConstant import (LARGE_ASYM_ID,
                                   LEN_MAJOR_ASYM_ID)
    from nmr.CifToNmrStar import has_key_value
    from nmr.NmrVrptUtility import (write_as_pickle,
                                    to_np_array,
                                    dihedral_angle)
    from nmr.mr.ParserListenerUtil import isLikeHis
    from nmr.NmrDpValidationBase import NmrDpValidationBase


class NmrDpValidationCoord(NmrDpValidationBase):
    """ Coordinate-derived conformational queries for NMR data validation.
    """
    __slots__ = ()

    def isCyclicPolymer(self, nmr_chain_id: str) -> bool:
        """ Return whether a given chain is cyclic polymer based on coordinate annotation.
            @return: True for cyclic polymer, False otherwise
        """

        if nmr_chain_id in self._reg.is_cyclic_polymer:
            return self._reg.is_cyclic_polymer[nmr_chain_id]

        try:

            is_cyclic = self.__isCyclicPolymer__(nmr_chain_id)

            return is_cyclic

        finally:
            self._reg.is_cyclic_polymer[nmr_chain_id] = is_cyclic

    def __isCyclicPolymer__(self, nmr_chain_id: str) -> bool:
        """ Return whether a given chain is cyclic polymer based on coordinate annotation.
            @return: True for cyclic polymer, False otherwise
        """

        cif_ps = self._reg.report.getModelPolymerSequenceWithNmrChainId(nmr_chain_id)

        if cif_ps is None:
            return False

        cif_chain_id = cif_ps['chain_id']
        beg_cif_seq_id = cif_ps['seq_id'][0]
        end_cif_seq_id = cif_ps['seq_id'][-1]

        try:

            if self._reg.cR.hasCategory('struct_conn'):
                filter_items = [{'name': 'ptnr1_label_asym_id', 'type': 'str', 'value': cif_chain_id},
                                {'name': 'ptnr2_label_asym_id', 'type': 'str', 'value': cif_chain_id},
                                {'name': 'ptnr1_label_seq_id', 'type': 'int', 'value': beg_cif_seq_id},
                                {'name': 'ptnr2_label_seq_id', 'type': 'int', 'value': end_cif_seq_id}
                                ]

                if not self._reg.bmrb_only and self._reg.cR.hasItem('struct_conn', 'pdbx_leaving_atom_flag'):
                    filter_items.append({'name': 'pdbx_leaving_atom_flag', 'type': 'str', 'value': 'both'})

                struct_conn = self._reg.cR.getDictListWithFilter('struct_conn',
                                                                  [{'name': 'conn_type_id', 'type': 'str'}
                                                                   ],
                                                                  filter_items)

            else:
                struct_conn = []

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                      f"+{self.__class_name__}.__isCyclicPolymer__() ++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.__isCyclicPolymer__() ++ Error  - {str(e)}\n")

            return False

        if len(struct_conn) == 0:

            label_to_auth_seq = self._reg.caC['label_to_auth_seq']

            seq_key_1 = (cif_chain_id, beg_cif_seq_id)
            seq_key_2 = (cif_chain_id, end_cif_seq_id)
            close_contact = []

            if seq_key_1 in label_to_auth_seq and seq_key_2 in label_to_auth_seq:
                auth_cif_chain_id, auth_beg_cif_seq_id = label_to_auth_seq[seq_key_1]
                _, auth_end_cif_seq_id = label_to_auth_seq[seq_key_2]

                try:

                    if self._reg.cR.hasCategory('pdbx_validate_close_contact'):
                        close_contact = self._reg.cR.getDictListWithFilter('pdbx_validate_close_contact',
                                                                            [{'name': 'dist', 'type': 'float'}
                                                                             ],
                                                                            [{'name': 'PDB_model_num', 'type': 'int',
                                                                              'value': self._reg.representative_model_id},
                                                                             {'name': 'auth_asym_id_1', 'type': 'str',
                                                                              'value': auth_cif_chain_id},
                                                                             {'name': 'auth_seq_id_1', 'type': 'int',
                                                                              'value': auth_beg_cif_seq_id},
                                                                             {'name': 'auth_atom_id_1', 'type': 'str',
                                                                              'value': 'N'},
                                                                             {'name': 'auth_asym_id_2', 'type': 'str',
                                                                              'value': auth_cif_chain_id},
                                                                             {'name': 'auth_seq_id_2', 'type': 'int',
                                                                              'value': auth_end_cif_seq_id},
                                                                             {'name': 'auth_atom_id_2', 'type': 'str',
                                                                              'value': 'C'}
                                                                             ])

                except Exception as e:  # pylint: disable=broad-exception-caught

                    self._reg.report.error.appendDescription('internal_error',
                                                              f"+{self.__class_name__}.__isCyclicPolymer__() ++ Error  - " + str(e))

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.__isCyclicPolymer__() ++ Error  - {str(e)}\n")

                    return False

            if len(close_contact) == 0:

                bond = self.getCoordBondLength(cif_chain_id, beg_cif_seq_id, 'N', cif_chain_id, end_cif_seq_id, 'C')

                if bond is None:
                    return False

                dist = next((b['distance'] for b in bond if b['model_id'] == self._reg.representative_model_id), None)

                if dist is None:
                    return False

                return 1.0 < dist < 2.4

            return 1.0 < close_contact[0]['dist'] < 2.4

        return struct_conn[0]['conn_type_id'].startswith('covale')

    def isProtCis(self, nmr_chain_id: str, nmr_seq_id: int) -> bool:
        """ Return whether type of peptide conformer of a given sequence is cis based on coordinate annotation.
            @return: True for cis peptide conformer, False otherwise
        """

        cif_ps = self._reg.report.getModelPolymerSequenceWithNmrChainId(nmr_chain_id)

        if cif_ps is None:
            return False

        cif_chain_id = cif_ps['chain_id']

        seq_align_dic = self._reg.report.sequence_alignment.get()

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

                if self._reg.cR.hasCategory('struct_mon_prot_cis'):
                    alias = not self._reg.cR.hasItem('struct_mon_prot_cis', 'pdbx_PDB_model_num')

                    model_num_name = 'ndb_model_num' if alias else 'pdbx_PDB_model_num'
                    label_asym_id_2_name = 'ndb_label_asym_id_2' if alias else 'pdbx_label_asym_id_2'
                    label_seq_id_2_name = 'ndb_label_seq_id_2' if alias else 'pdbx_label_seq_id_2'

                    prot_cis = self._reg.cR.getDictListWithFilter('struct_mon_prot_cis',
                                                                   [{'name': model_num_name, 'type': 'int'}
                                                                    ],
                                                                   [{'name': label_asym_id_2_name, 'type': 'str',
                                                                     'value': cif_chain_id},
                                                                    {'name': label_seq_id_2_name, 'type': 'int',
                                                                     'value': cif_seq_id}
                                                                    ])

                else:
                    prot_cis = []

            except Exception as e:  # pylint: disable=broad-exception-caught

                self._reg.report.error.appendDescription('internal_error',
                                                          f"+{self.__class_name__}.isProtCis() ++ Error  - " + str(e))

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.isProtCis() ++ Error  - {str(e)}\n")

                return False

            return len(prot_cis) > 0

        return False

    def testTautomerOfHistidinePerModel(self) -> bool:
        """ Check tautomeric state of a given histidine per model. (DAOTHER-9252)
        """

        src_id = self._reg.report.getInputSourceIdOfCoord()

        if src_id < 0:
            return False

        cif_input_source = self._reg.report.input_sources[src_id]
        cif_input_source_dic = cif_input_source.get()

        has_poly_seq = has_key_value(cif_input_source_dic, 'polymer_sequence')

        if not has_poly_seq:
            return False

        file_name = cif_input_source_dic['file_name']
        cif_poly_seq = cif_input_source_dic['polymer_sequence']

        if len(self._reg.cpC['tautomer_per_model']) > 0:

            for inst in self._reg.cpC['tautomer_per_model']:
                tautomer_per_model = inst['tautomer_per_model']

                try:
                    rep_tautomer = tautomer_per_model[self._reg.representative_model_id]
                except KeyError:
                    try:
                        rep_tautomer = tautomer_per_model[self._reg.eff_model_ids[0]]
                    except KeyError:
                        continue

                if any(tautomer != rep_tautomer for tautomer in tautomer_per_model.values()):
                    chain_id, auth_chain_id = inst['chain_id'], inst['auth_chain_id']
                    seq_id, auth_seq_id = inst['seq_id'], inst['auth_seq_id']
                    comp_id = inst['comp_id']
                    cif_seq_code = f"{chain_id}:{seq_id}:{comp_id}"
                    if chain_id != auth_chain_id or seq_id != auth_seq_id:
                        cif_seq_code += f" ({auth_chain_id}:{auth_seq_id}:{comp_id} in author sequence scheme)"

                    err = f"{cif_seq_code} has been instantiated with different tautomeric states across models, "\
                        f"{tautomer_per_model}. Please re-upload the model file."

                    if self._reg.internal_mode:  # and not self._reg.conversion_server:

                        self._reg.report.warning.appendDescription('coordinate_issue',
                                                                    {'file_name': file_name, 'category': 'atom_site',
                                                                     'description': err})

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.testTautomerOfHistidinePerModel() "
                                                 f"++ Warning  - {err}\n")

                    else:

                        self._reg.report.error.appendDescription('coordinate_issue',
                                                                  {'file_name': file_name, 'category': 'atom_site',
                                                                   'description': err})

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.testTautomerOfHistidinePerModel() "
                                                 f"++ Error  - {err}\n")

            return True

        model_num_name = 'pdbx_PDB_model_num' if 'pdbx_PDB_model_num' in self._reg.coord_atom_site_tags else 'ndb_model'

        for ps in cif_poly_seq:
            chain_id = ps['chain_id']

            auth_chain_id = chain_id
            if 'auth_chain_id' in ps:
                auth_chain_id = ps['auth_chain_id']

            if len(cif_poly_seq) >= LEN_MAJOR_ASYM_ID:
                if auth_chain_id not in LARGE_ASYM_ID:
                    continue

            for seq_id, comp_id in zip(ps['seq_id'], ps['comp_id']):

                if not isLikeHis(comp_id, self._reg.ccU):
                    continue

                if comp_id == 'HIS':
                    hd1_name = 'HD1'
                    he2_name = 'HE2'
                else:
                    _hd1_name = self._reg.ccU.getBondedAtoms(comp_id, 'ND1', onlyProton=True)
                    _he2_name = self._reg.ccU.getBondedAtoms(comp_id, 'NE2', onlyProton=True)
                    if len(_hd1_name) != 1 or len(_he2_name) != 1:
                        continue
                    hd1_name = _hd1_name[0]
                    he2_name = _he2_name[0]

                try:
                    auth_seq_id = ps['auth_seq_id'][ps['seq_id'].index(seq_id)]
                except (KeyError, IndexError, ValueError):
                    auth_seq_id = seq_id

                try:

                    protons = self._reg.cR.getDictListWithFilter('atom_site',
                                                                  [{'name': 'label_atom_id', 'type': 'starts-with-alnum',
                                                                    'alt_name': 'atom_id'},
                                                                   {'name': model_num_name, 'type': 'int', 'alt_name': 'model_id'},
                                                                   ],
                                                                  [{'name': 'label_asym_id', 'type': 'str', 'value': chain_id},
                                                                   {'name': 'label_seq_id', 'type': 'int', 'value': seq_id},
                                                                   {'name': 'label_comp_id', 'type': 'str', 'value': comp_id},
                                                                   {'name': 'type_symbol', 'type': 'str', 'value': 'H'},
                                                                   {'name': 'label_alt_id', 'type': 'enum',
                                                                    'enum': (self._reg.representative_alt_id,)}
                                                                   ])

                except Exception as e:  # pylint: disable=broad-exception-caught

                    self._reg.report.error.appendDescription('internal_error',
                                                              f"+{self.__class_name__}.testTautomerOfHistidinePerModel() "
                                                              "++ Error  - " + str(e))

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.testTautomerOfHistidinePerModel() "
                                             f"++ Error  - {str(e)}\n")

                    return False

                if len(protons) > 0:

                    tautomer_per_model = {}

                    for model_id in self._reg.eff_model_ids:

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
                        rep_tautomer = tautomer_per_model[self._reg.representative_model_id]
                    except KeyError:
                        try:
                            rep_tautomer = tautomer_per_model[self._reg.eff_model_ids[0]]
                        except KeyError:
                            continue

                    self._reg.cpC['tautomer_per_model'].append({'chain_id': chain_id, 'seq_id': seq_id, 'comp_id': comp_id,
                                                                 'auth_chain_id': auth_chain_id, 'auth_seq_id': auth_seq_id,
                                                                 'tautomer_per_model': tautomer_per_model})

                    if any(tautomer != rep_tautomer for tautomer in tautomer_per_model.values()):
                        cif_seq_code = f"{chain_id}:{seq_id}:{comp_id}"
                        if chain_id != auth_chain_id or seq_id != auth_seq_id:
                            cif_seq_code += f" ({auth_chain_id}:{auth_seq_id}:{comp_id} in author sequence scheme)"

                        err = f"{cif_seq_code} has been instantiated with different tautomeric states across models, "\
                            f"{tautomer_per_model}. Please re-upload the model file."

                        if self._reg.internal_mode:  # and not self._reg.conversion_server:

                            self._reg.report.warning.appendDescription('coordinate_issue',
                                                                        {'file_name': file_name, 'category': 'atom_site',
                                                                         'description': err})

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.testTautomerOfHistidinePerModel() "
                                                     f"++ Warning  - {err}\n")

                        else:

                            self._reg.report.error.appendDescription('coordinate_issue',
                                                                      {'file_name': file_name, 'category': 'atom_site',
                                                                       'description': err})

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.testTautomerOfHistidinePerModel() "
                                                     f"++ Error  - {err}\n")

        if self._reg.coordPropCachePath is not None:
            hash_value = hash(str(self._reg.cpC))
            if hash_value != self._reg.cpcHashCode:
                write_as_pickle(self._reg.cpC, self._reg.coordPropCachePath)
                self._reg.cpcHashCode = hash_value

        return True

    def getTautomerOfHistidine(self, nmr_chain_id: str, nmr_seq_id: int) -> str:
        """ Return tautomeric state of a given histidine.
            @return: One of 'biprotonated', 'tau-tautomer', 'pi-tautomer', 'unknown'
        """

        cif_ps = self._reg.report.getModelPolymerSequenceWithNmrChainId(nmr_chain_id)

        if cif_ps is None:
            return 'unknown'

        cif_chain_id = cif_ps['chain_id']

        seq_align_dic = self._reg.report.sequence_alignment.get()

        if not has_key_value(seq_align_dic, 'nmr_poly_seq_vs_model_poly_seq'):
            return 'unknown'

        seq_key = (nmr_chain_id, nmr_seq_id)

        if seq_key in self._reg.cpC['tautomer']:
            return self._reg.cpC['tautomer'][seq_key]

        result = next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq']
                       if seq_align['ref_chain_id'] == nmr_chain_id and seq_align['test_chain_id'] == cif_chain_id), None)

        if result is not None:

            cif_seq_id = next((test_seq_id for ref_seq_id, ref_code, test_seq_id
                               in zip(result['ref_seq_id'], result['ref_code'], result['test_seq_id'])
                               if ref_seq_id == nmr_seq_id and ref_code == 'H'), None)

            if cif_seq_id is None:
                self._reg.cpC['tautomer'][seq_key] = 'unknown'
                return 'unknown'

            try:

                model_num_name = 'pdbx_PDB_model_num' if 'pdbx_PDB_model_num' in self._reg.coord_atom_site_tags else 'ndb_model'

                protons = self._reg.cR.getDictListWithFilter('atom_site',
                                                              [{'name': 'label_atom_id', 'type': 'starts-with-alnum',
                                                                'alt_name': 'atom_id'}
                                                               ],
                                                              [{'name': 'label_asym_id', 'type': 'str', 'value': cif_chain_id},
                                                               {'name': 'label_seq_id', 'type': 'int', 'value': cif_seq_id},
                                                               {'name': 'label_comp_id', 'type': 'str', 'value': 'HIS'},
                                                               {'name': 'type_symbol', 'type': 'str', 'value': 'H'},
                                                               {'name': model_num_name, 'type': 'int',
                                                                'value': self._reg.representative_model_id},
                                                               {'name': 'label_alt_id', 'type': 'enum',
                                                                'enum': (self._reg.representative_alt_id,)}
                                                               ])

            except Exception as e:  # pylint: disable=broad-exception-caught

                self._reg.report.error.appendDescription('internal_error',
                                                          f"+{self.__class_name__}.getTautomerOfHistidine() ++ Error  - " + str(e))

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.getTautomerOfHistidine() ++ Error  - {str(e)}\n")

                return 'unknown'

            if len(protons) > 0:

                has_hd1 = has_he2 = False

                for h in protons:
                    if h['atom_id'] == 'HD1':
                        has_hd1 = True
                    elif h['atom_id'] == 'HE2':
                        has_he2 = True

                if has_hd1 and has_he2:
                    self._reg.cpC['tautomer'][seq_key] = 'biprotonated'
                    return 'biprotonated'

                if has_hd1:
                    self._reg.cpC['tautomer'][seq_key] = 'pi-tautomer'
                    return 'pi-tautomer'

                if has_he2:
                    self._reg.cpC['tautomer'][seq_key] = 'tau-tautomer'
                    return 'tau-tautomer'

        self._reg.cpC['tautomer'][seq_key] = 'unknown'
        return 'unknown'

    def getRotamerOfValine(self, nmr_chain_id: str, nmr_seq_id: int
                           ) -> List[dict]:
        """ Return rotameric state distribution of a given valine.
            @return: One of 'gauche+', 'trans', 'gauche-', 'unknown'
        """

        none = [{'name': 'chi1', 'unknown': 1.0}]

        cif_ps = self._reg.report.getModelPolymerSequenceWithNmrChainId(nmr_chain_id)

        if cif_ps is None:
            return none

        cif_chain_id = cif_ps['chain_id']

        seq_align_dic = self._reg.report.sequence_alignment.get()

        if not has_key_value(seq_align_dic, 'nmr_poly_seq_vs_model_poly_seq'):
            return none

        seq_key = (nmr_chain_id, nmr_seq_id, 'VAL')

        if seq_key in self._reg.cpC['rotamer']:
            return self._reg.cpC['rotamer'][seq_key]

        result = next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq']
                       if seq_align['ref_chain_id'] == nmr_chain_id and seq_align['test_chain_id'] == cif_chain_id), None)

        if result is not None:

            cif_seq_id = next((test_seq_id for ref_seq_id, ref_code, test_seq_id
                               in zip(result['ref_seq_id'], result['ref_code'], result['test_seq_id'])
                               if ref_seq_id == nmr_seq_id and ref_code == 'V'), None)

            if cif_seq_id is None:
                self._reg.cpC['rotamer'][seq_key] = none
                return none

            try:

                model_num_name = 'pdbx_PDB_model_num' if 'pdbx_PDB_model_num' in self._reg.coord_atom_site_tags else 'ndb_model'

                atoms = self._reg.cR.getDictListWithFilter('atom_site',
                                                            [{'name': 'label_atom_id', 'type': 'starts-with-alnum',
                                                              'alt_name': 'atom_id'},
                                                             {'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                             {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                             {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'},
                                                             {'name': model_num_name, 'type': 'int', 'alt_name': 'model_id'}
                                                             ],
                                                            [{'name': 'label_asym_id', 'type': 'str', 'value': cif_chain_id},
                                                             {'name': 'label_seq_id', 'type': 'int', 'value': cif_seq_id},
                                                             {'name': 'label_comp_id', 'type': 'str', 'value': 'VAL'},
                                                             {'name': 'label_alt_id', 'type': 'enum',
                                                              'enum': (self._reg.representative_alt_id,)}
                                                             ])

            except Exception as e:  # pylint: disable=broad-exception-caught

                self._reg.report.error.appendDescription('internal_error',
                                                          f"+{self.__class_name__}.getRotamerOfValine() ++ Error  - " + str(e))

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.getRotamerOfValine() ++ Error  - {str(e)}\n")

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
                self._reg.cpC['rotamer'][seq_key] = none
                return none

            if rot1['unknown'] == 0.0:
                del rot1['unknown']

            _rot1 = rot1.copy()

            for k, v in _rot1.items():
                if k == 'name':
                    continue
                rot1[k] = round(v / total_models, 3)

            self._reg.cpC['rotamer'][seq_key] = [rot1]
            return [rot1]

        self._reg.cpC['rotamer'][seq_key] = none
        return none

    def getRotamerOfLeucine(self, nmr_chain_id: str, nmr_seq_id: int
                            ) -> List[dict]:
        """ Return rotameric state distribution of a given leucine.
            @return: One of 'gauche+', 'trans', 'gauche-', 'unknown'
        """

        none = [{'name': 'chi1', 'unknown': 1.0}, {'name': 'chi2', 'unknown': 1.0}]

        cif_ps = self._reg.report.getModelPolymerSequenceWithNmrChainId(nmr_chain_id)

        if cif_ps is None:
            return none

        cif_chain_id = cif_ps['chain_id']

        seq_align_dic = self._reg.report.sequence_alignment.get()

        if not has_key_value(seq_align_dic, 'nmr_poly_seq_vs_model_poly_seq'):
            return none

        seq_key = (nmr_chain_id, nmr_seq_id, 'LEU')

        if seq_key in self._reg.cpC['rotamer']:
            return self._reg.cpC['rotamer'][seq_key]

        result = next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq']
                       if seq_align['ref_chain_id'] == nmr_chain_id and seq_align['test_chain_id'] == cif_chain_id), None)

        if result is not None:

            cif_seq_id = next((test_seq_id for ref_seq_id, ref_code, test_seq_id
                               in zip(result['ref_seq_id'], result['ref_code'], result['test_seq_id'])
                               if ref_seq_id == nmr_seq_id and ref_code == 'L'), None)

            if cif_seq_id is None:
                self._reg.cpC['rotamer'][seq_key] = none
                return none

            try:

                model_num_name = 'pdbx_PDB_model_num' if 'pdbx_PDB_model_num' in self._reg.coord_atom_site_tags else 'ndb_model'

                atoms = self._reg.cR.getDictListWithFilter('atom_site',
                                                            [{'name': 'label_atom_id', 'type': 'starts-with-alnum',
                                                              'alt_name': 'atom_id'},
                                                             {'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                             {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                             {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'},
                                                             {'name': model_num_name, 'type': 'int', 'alt_name': 'model_id'}
                                                             ],
                                                            [{'name': 'label_asym_id', 'type': 'str', 'value': cif_chain_id},
                                                             {'name': 'label_seq_id', 'type': 'int', 'value': cif_seq_id},
                                                             {'name': 'label_comp_id', 'type': 'str', 'value': 'LEU'},
                                                             {'name': 'label_alt_id', 'type': 'enum',
                                                              'enum': (self._reg.representative_alt_id,)}
                                                             ])

            except Exception as e:  # pylint: disable=broad-exception-caught

                self._reg.report.error.appendDescription('internal_error',
                                                          f"+{self.__class_name__}.getRotamerOfLeucine() ++ Error  - " + str(e))

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.getRotamerOfLeucine() ++ Error  - {str(e)}\n")

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
                self._reg.cpC['rotamer'][seq_key] = none
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
                rot1[k] = round(v / total_models, 3)

            for k, v in _rot2.items():
                if k == 'name':
                    continue
                rot2[k] = round(v / total_models, 3)

            self._reg.cpC['rotamer'][seq_key] = [rot1, rot2]
            return [rot1, rot2]

        self._reg.cpC['rotamer'][seq_key] = none
        return none

    def getRotamerOfIsoleucine(self, nmr_chain_id: str, nmr_seq_id: int
                               ) -> List[dict]:
        """ Return rotameric state distribution of a given isoleucine.
            @return: One of 'gauche+', 'trans', 'gauche-', 'unknown'
        """

        none = [{'name': 'chi1', 'unknown': 1.0}, {'name': 'chi2', 'unknown': 1.0}]

        cif_ps = self._reg.report.getModelPolymerSequenceWithNmrChainId(nmr_chain_id)

        if cif_ps is None:
            return none

        cif_chain_id = cif_ps['chain_id']

        seq_align_dic = self._reg.report.sequence_alignment.get()

        if not has_key_value(seq_align_dic, 'nmr_poly_seq_vs_model_poly_seq'):
            return none

        seq_key = (nmr_chain_id, nmr_seq_id, 'ILE')

        if seq_key in self._reg.cpC['rotamer']:
            return self._reg.cpC['rotamer'][seq_key]

        result = next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq']
                       if seq_align['ref_chain_id'] == nmr_chain_id and seq_align['test_chain_id'] == cif_chain_id), None)

        if result is not None:

            cif_seq_id = next((test_seq_id for ref_seq_id, ref_code, test_seq_id
                               in zip(result['ref_seq_id'], result['ref_code'], result['test_seq_id'])
                               if ref_seq_id == nmr_seq_id and ref_code == 'I'), None)

            if cif_seq_id is None:
                self._reg.cpC['rotamer'][seq_key] = none
                return none

            try:

                model_num_name = 'pdbx_PDB_model_num' if 'pdbx_PDB_model_num' in self._reg.coord_atom_site_tags else 'ndb_model'

                atoms = self._reg.cR.getDictListWithFilter('atom_site',
                                                            [{'name': 'label_atom_id', 'type': 'starts-with-alnum',
                                                              'alt_name': 'atom_id'},
                                                             {'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                             {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                             {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'},
                                                             {'name': model_num_name, 'type': 'int', 'alt_name': 'model_id'}
                                                             ],
                                                            [{'name': 'label_asym_id', 'type': 'str', 'value': cif_chain_id},
                                                             {'name': 'label_seq_id', 'type': 'int', 'value': cif_seq_id},
                                                             {'name': 'label_comp_id', 'type': 'str', 'value': 'ILE'},
                                                             {'name': 'label_alt_id', 'type': 'enum',
                                                              'enum': (self._reg.representative_alt_id,)}
                                                             ])

            except Exception as e:  # pylint: disable=broad-exception-caught

                self._reg.report.error.appendDescription('internal_error',
                                                          f"+{self.__class_name__}.getRotamerOfIsoleucine() ++ Error  - " + str(e))

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.getRotamerOfIsoleucine() ++ Error  - {str(e)}\n")

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
                self._reg.cpC['rotamer'][seq_key] = none
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
                rot1[k] = round(v / total_models, 3)

            for k, v in _rot2.items():
                if k == 'name':
                    continue
                rot2[k] = round(v / total_models, 3)

            self._reg.cpC['rotamer'][seq_key] = [rot1, rot2]
            return [rot1, rot2]

        self._reg.cpC['rotamer'][seq_key] = none
        return none
