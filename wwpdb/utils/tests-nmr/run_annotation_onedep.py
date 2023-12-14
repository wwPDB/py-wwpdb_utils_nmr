import sys
import os
import json
import re
import pynmrstar
from packaging import version as package_version

try:
    from wwpdb.utils.nmr.NmrDpUtility import NmrDpUtility
    auth_view = 'mock-data-combine-at-upload'
except ImportError:
    from nmr.NmrDpUtility import NmrDpUtility
    auth_view = 'auth_view'


__pynmrstar_v3_3__ = package_version.parse(pynmrstar.__version__) >= package_version.parse("3.3.0")
__pynmrstar_v3_2__ = package_version.parse(pynmrstar.__version__) >= package_version.parse("3.2.0")
__pynmrstar_v3_1__ = package_version.parse(pynmrstar.__version__) >= package_version.parse("3.1.0")
__pynmrstar_v3__ = package_version.parse(pynmrstar.__version__) >= package_version.parse("3.0.0")


def get_inventory_list(star_data):
    """ Return lists of saveframe category names and loop category names in an NEF/NMR-STAR file.
        @return: list of saveframe category names, list of loop category names
    """

    sf_list = []
    lp_list = []

    if isinstance(star_data, pynmrstar.Entry):

        for sf in star_data.frame_list:
            sf_list.append(sf.category)

            for lp in sf:
                lp_list.append(lp.category)

    elif isinstance(star_data, pynmrstar.Saveframe):

        for lp in star_data:
            lp_list.append(lp.category)

    elif star_data is not None:
        lp_list.append(star_data.category)

    return sf_list, lp_list


def is_empty_loop(star_data, lp_category):
    """ Return whether one of specified loops is empty loop.
        @return: True for empty loop exists, False otherwise
    """

    if isinstance(star_data, pynmrstar.Entry):
        loops = star_data.get_loops_by_category(lp_category)

        return any(len(loop) == 0 for loop in loops)

    if isinstance(star_data, pynmrstar.Saveframe):
        if __pynmrstar_v3_2__:
            loop = star_data.get_loop(lp_category)
        else:
            loop = star_data.get_loop_by_category(lp_category)

        return len(loop) == 0

    return len(star_data) == 0


def get_lp_tag(lp, tags):
    """ Return the selected loop tags by row as a list of lists.
    """

    return lp.get_tag(tags) if __pynmrstar_v3__ else lp.get_data_by_tag(tags)


def get_first_sf_tag(sf=None, tag=None):
    """ Return the first value of a given saveframe tag.
        @return: The first tag value, empty string otherwise.
    """

    if sf is None or tag is None:
        return ''

    array = sf.get_tag(tag)

    if len(array) == 0:
        return ''

    return array[0] if array[0] is not None else ''


def set_sf_tag(sf, tag, value):
    """ Set saveframe tag.
    """

    tagNames = [t[0] for t in sf.tags]

    if isinstance(value, str) and len(value) == 0:
        value = None

    if tag not in tagNames:
        sf.add_tag(tag, value)
        return

    sf.tags[tagNames.index(tag)][1] = value


def is_combined_nmr_data(file_path):

    emptyValue = (None, '', '.', '?', 'null', 'None')

    mr_file_name_pattern = re.compile(r'^([Pp][Dd][Bb]_)?([0-9]{4})?[0-9][0-9A-Za-z]{3}.mr$')
    proc_mr_file_name_pattern = re.compile(r'^D_[0-9]{6,10}_mr(-(upload|upload-convert|deposit|annotate|release|review))?'
                                           r'_P\d+\.(amber|biosym|charmm|cns|cyana|dynamo|gromacs|isd|rosetta|sybyl|xplor-nih)\.V\d+$')
    pdb_id_pattern = re.compile(r'^([Pp][Dd][Bb]_)?([0-9]{4})?[0-9][0-9A-Za-z]{3}$')
    dep_id_pattern = re.compile(r'^D_[0-9]{6,10}$')
    bmrb_id_pattern = re.compile(r'^(bmr)?[0-9]{5,}$')

    try:
        star_data = pynmrstar.Entry.from_file(file_path)

        for sf in star_data.frame_list:
            if sf.category == 'constraint_statistics':
                data_file_name = get_first_sf_tag(sf, 'Data_file_name')
                entry_id = get_first_sf_tag(sf, 'Entry_ID')
                combined = (mr_file_name_pattern.match(data_file_name) or proc_mr_file_name_pattern.match(data_file_name))\
                    and (pdb_id_pattern.match(entry_id) or dep_id_pattern.match(entry_id) or bmrb_id_pattern.match(entry_id))
                original_file_name = None

                lp_category = '_Constraint_file'

                if __pynmrstar_v3_2__:
                    lp = sf.get_loop(lp_category)
                else:
                    lp = sf.get_loop_by_category(lp_category)

                dat = get_lp_tag(lp, ['ID', 'Constraint_filename', 'Software_name'])

                original_file_name = {}

                for row in dat:

                    if row[0] in emptyValue:
                        combined = False

                    if row[1] not in emptyValue and row[2] not in emptyValue:
                        if row[2] in ('XPLOR-NIH', 'X-PLOR NIH'):
                            if 'nm-res-xpl' not in original_file_name:
                                original_file_name['nm-res-xpl'] = []
                            original_file_name['nm-res-xpl'].append(row[1])
                        elif row[2] == 'CNS':
                            if 'nm-res-cns' not in original_file_name:
                                original_file_name['nm-res-cns'] = []
                            original_file_name['nm-res-cns'].append(row[1])
                        elif row[2] in ('AMBER', 'Amber'):
                            if 'nm-res-amb' not in original_file_name:
                                original_file_name['nm-res-amb'] = []
                            original_file_name['nm-res-amb'].append(row[1])
                        elif row[2] == 'CYANA':
                            if 'nm-res-cya' not in original_file_name:
                                original_file_name['nm-res-cya'] = []
                            original_file_name['nm-res-cya'].append(row[1])
                        elif row[2] in ('ROSETTA', 'Rosetta'):
                            if 'nm-res-ros' not in original_file_name:
                                original_file_name['nm-res-ros'] = []
                            original_file_name['nm-res-ros'].append(row[1])
                        elif row[2] in ('BIOSYM', 'Discover'):
                            if 'nm-res-bio' not in original_file_name:
                                original_file_name['nm-res-bio'] = []
                            original_file_name['nm-res-bio'].append(row[1])
                        elif row[2] == 'GROMACS':
                            if 'nm-res-gro' not in original_file_name:
                                original_file_name['nm-res-gro'] = []
                            original_file_name['nm-res-gro'].append(row[1])
                        elif row[2] == 'DYNAMO':
                            if 'nm-res-dyn' not in original_file_name:
                                original_file_name['nm-res-dyn'] = []
                            original_file_name['nm-res-dyn'].append(row[1])
                        elif row[2] == 'SYBYL':
                            if 'nm-res-syb' not in original_file_name:
                                original_file_name['nm-res-syb'] = []
                            original_file_name['nm-res-syb'].append(row[1])
                        elif row[2] in ('ISD', 'Inferential Structure Determination (ISD)'):
                            if 'nm-res-isd' not in original_file_name:
                                original_file_name['nm-res-isd'] = []
                            original_file_name['nm-res-isd'].append(row[1])
                        elif row[2] == 'CHARMM':
                            if 'nm-res-cha' not in original_file_name:
                                original_file_name['nm-res-cha'] = []
                            original_file_name['nm-res-cha'].append(row[1])

                return combined, original_file_name
    except Exception:
        pass
    return False, None


class gen_auth_view_onedep:

    def __init__(self):

        self.__auth_view = auth_view

        self.__cif_name_pattern = re.compile(r'D_[0-9]+_model-(\S+)_P1.cif.V([0-9]+)$')
        self.__mr_name_pattern = re.compile(r'D_[0-9]+_mr-(\S+)_P([0-9]+).(\S+).V([0-9]+)$')
        self.__pk_name_pattern = re.compile(r'D_[0-9]+_nmr-peaks-upload_P([0-9]+).dat.V([0-9]+)$')
        self.__nmr_cif_name_pattern = re.compile(r'D_[0-9]+_nmr-data-str_P([0-9]+).cif.V([0-9]+)$')
        self.__cs_ann_name_pattern = re.compile(r'D_[0-9]+_cs-(\S+)_P1.cif.V([0-9]+)')

        self.__datablock_pattern = re.compile(r"\s*data_\S+\s*")
        self.__sf_anonymous_pattern = re.compile(r"\s*save_\S+\s*")
        self.__save_pattern = re.compile(r"\s*save_\s*")
        self.__loop_pattern = re.compile(r"\s*loop_\s*")
        self.__stop_pattern = re.compile(r"\s*stop_\s*")

        self.__amb_top_pattern = re.compile(r"^\%FLAG ATOM_NAME\s*")
        self.__amb_rst_pattern = re.compile(r"\s*\&rst\s*")

        self.__gro_top_pattern = re.compile(r"^\[ atoms \]\s*")
        self.__gro_rst_pattern = re.compile(r"^\[ (distance|dihedral|orientation)_restraints \]\s*")

        self.__bmrb_id = ''.join(c for c in sys.argv[1] if c.isdigit())

        self.__entry_dir = os.path.join(self.__auth_view, 'bmr' + self.__bmrb_id)

        self.__star_file_path = os.path.join(self.__entry_dir, 'bmr' + self.__bmrb_id + '_3.str')

        self.__annotated_star_file_path = os.path.join(self.__entry_dir, 'bmr' + self.__bmrb_id + '_annotated.str')

        self.__annotated_log_file_path = os.path.join(self.__entry_dir, 'bmr' + self.__bmrb_id + '-annotated-log.json')

        self.__ann_wo_raw_pk_star_file_path = os.path.join(self.__entry_dir, 'bmr' + self.__bmrb_id + '_ann_wo_raw_pk.str')

        self.__avs_letter_path = os.path.join(self.__entry_dir, 'AVS_anomalous_bmr' + self.__bmrb_id + '_3.ltr')

        self.__return_letter_path = os.path.join(self.__entry_dir, 'return_' + self.__bmrb_id + '.ltr')

        self.__has_peak = False

        if not os.path.exists(self.__star_file_path):
            print('Not found NMR-STAR file.')
            sys.exit(1)

        self.__data_dir = os.path.join(self.__entry_dir, 'data')

        self.__cif_file_path = None
        _mile_stone = None
        _version = None

        for file_name in os.listdir(self.__data_dir):

            if self.__cif_name_pattern.match(file_name):
                g = self.__cif_name_pattern.search(file_name).groups()
                mile_stone = g[0]
                version = int(g[1])

                if mile_stone == 'release':
                    if _mile_stone != 'release':
                        _mile_stone = mile_stone
                        _version = version
                        self.__cif_file_path = os.path.join(self.__data_dir, file_name)
                    elif version > _version:
                        _version = version
                        self.__cif_file_path = os.path.join(self.__data_dir, file_name)

                elif mile_stone == 'annotate':
                    if _mile_stone is None:
                        _mile_stone = mile_stone
                        _version = version
                        self.__cif_file_path = os.path.join(self.__data_dir, file_name)
                    elif _mile_stone == 'annotate' and version > _version:
                        _version = version
                        self.__cif_file_path = os.path.join(self.__data_dir, file_name)

        if self.__cif_file_path is None:
            print('Not found coordinates.')
            sys.exit(1)

        self.__nmr_cif_file_path = None
        _version = None

        for file_name in sorted(os.listdir(self.__data_dir)):
            if self.__nmr_cif_name_pattern.match(file_name):
                g = self.__nmr_cif_name_pattern.search(file_name).groups()

                version = int(g[1])

                if _version is None or version > _version:
                    self.__nmr_cif_file_path = os.path.join(self.__data_dir, file_name)
                    _version = version

        self.__cs_ann_file_path = None
        _mile_stone = None
        _version = None

        for file_name in os.listdir(self.__data_dir):

            if self.__cs_ann_name_pattern.match(file_name):
                g = self.__cs_ann_name_pattern.search(file_name).groups()
                mile_stone = g[0]
                version = int(g[1])

                if mile_stone == 'release':
                    if _mile_stone != 'release':
                        _mile_stone = mile_stone
                        _version = version
                        self.__cs_ann_file_path = os.path.join(self.__data_dir, file_name)
                    elif version > _version:
                        _version = version
                        self.__cs_ann_file_path = os.path.join(self.__data_dir, file_name)

                elif mile_stone == 'annotate':
                    if _mile_stone is None:
                        _mile_stone = mile_stone
                        _version = version
                        self.__cs_ann_file_path = os.path.join(self.__data_dir, file_name)
                    elif _mile_stone == 'annotate' and version > _version:
                        _version = version
                        self.__cs_ann_file_path = os.path.join(self.__data_dir, file_name)

        has_amber = False
        has_gromacs = False

        mr_dic = {}
        ax_dic = {}

        for file_name in sorted(os.listdir(self.__data_dir)):

            if self.__mr_name_pattern.match(file_name):
                g = self.__mr_name_pattern.search(file_name).groups()
                mile_stone = g[0]
                # part = int(g[1])
                content_type = g[2]
                version = int(g[3])

                key = content_type + g[1]

                file_path = os.path.join(self.__data_dir, file_name)

                if content_type == 'amber':

                    if self.is_amb_top_file(file_path):
                        content_type = 'dat'

                    has_amber = True
                    if key in ax_dic:
                        if (version > ax_dic[key]['version'] and mile_stone == ax_dic[key]['mile_stone'])\
                           or (mile_stone == 'annotate' and mile_stone != ax_dic[key]['mile_stone']):
                            ax_dic[key]['mile_stone'] = mile_stone
                            ax_dic[key]['version'] = version
                            ax_dic[key]['content_type'] = content_type
                            ax_dic[key]['file_name'] = file_path
                            ax_dic[key]['is_star_file'] = self.is_star_file(file_path)
                    else:
                        ax_dic[key] = {}
                        ax_dic[key]['mile_stone'] = mile_stone
                        ax_dic[key]['version'] = version
                        ax_dic[key]['content_type'] = content_type
                        ax_dic[key]['file_name'] = file_path
                        ax_dic[key]['is_star_file'] = self.is_star_file(file_path)

                elif content_type == 'gromacs':

                    if self.is_gro_top_file(file_path):
                        content_type = 'dat'

                    has_gromacs = True
                    if key in ax_dic:
                        if (version > ax_dic[key]['version'] and mile_stone == ax_dic[key]['mile_stone'])\
                           or (mile_stone == 'annotate' and mile_stone != ax_dic[key]['mile_stone']):
                            ax_dic[key]['mile_stone'] = mile_stone
                            ax_dic[key]['version'] = version
                            ax_dic[key]['content_type'] = content_type
                            ax_dic[key]['file_name'] = file_path
                            ax_dic[key]['is_star_file'] = self.is_star_file(file_path)
                    else:
                        ax_dic[key] = {}
                        ax_dic[key]['mile_stone'] = mile_stone
                        ax_dic[key]['version'] = version
                        ax_dic[key]['content_type'] = content_type
                        ax_dic[key]['file_name'] = file_path
                        ax_dic[key]['is_star_file'] = self.is_star_file(file_path)

                else:

                    if content_type == 'dat':
                        if self.is_amb_rst_file(file_path):
                            content_type = 'amber'
                        if self.is_gro_rst_file(file_path):
                            content_type = 'gromacs'

                    if key in mr_dic:
                        if (version > mr_dic[key]['version'] and mile_stone == mr_dic[key]['mile_stone'])\
                           or (mile_stone == 'annotate' and mile_stone != mr_dic[key]['mile_stone']):
                            mr_dic[key]['mile_stone'] = mile_stone
                            mr_dic[key]['version'] = version
                            mr_dic[key]['content_type'] = content_type
                            mr_dic[key]['file_name'] = file_path
                            mr_dic[key]['is_star_file'] = self.is_star_file(file_path)
                    else:
                        mr_dic[key] = {}
                        mr_dic[key]['mile_stone'] = mile_stone
                        mr_dic[key]['version'] = version
                        mr_dic[key]['content_type'] = content_type
                        mr_dic[key]['file_name'] = file_path
                        mr_dic[key]['is_star_file'] = self.is_star_file(file_path)

        if has_amber:

            amb_count = 0
            dat_count = 0

            for d in ax_dic.values():
                if not d['is_star_file']:
                    content_type = d['content_type']
                    if content_type == 'amber':
                        amb_count += 1

            for d in mr_dic.values():
                if not d['is_star_file']:
                    content_type = d['content_type']
                    if content_type == 'dat':
                        dat_count += 1

            if amb_count == 1 and dat_count > 1:

                mr_dic = {}
                ax_dic = {}

                for file_name in sorted(os.listdir(self.__data_dir)):

                    if self.__mr_name_pattern.match(file_name):
                        g = self.__mr_name_pattern.search(file_name).groups()
                        mile_stone = g[0]
                        # part = int(g[1])
                        content_type = g[2]
                        version = int(g[3])

                        key = content_type + g[1]

                        file_path = os.path.join(self.__data_dir, file_name)

                        if content_type == 'amber':
                            if key in ax_dic:
                                if (version > ax_dic[key]['version'] and mile_stone == ax_dic[key]['mile_stone'])\
                                   or (mile_stone == 'annotate' and mile_stone != ax_dic[key]['mile_stone']):
                                    ax_dic[key]['mile_stone'] = mile_stone
                                    ax_dic[key]['version'] = version
                                    ax_dic[key]['content_type'] = 'dat'
                                    ax_dic[key]['file_name'] = file_path
                                    ax_dic[key]['is_star_file'] = self.is_star_file(file_path)
                            else:
                                ax_dic[key] = {}
                                ax_dic[key]['mile_stone'] = mile_stone
                                ax_dic[key]['version'] = version
                                ax_dic[key]['content_type'] = 'dat'
                                ax_dic[key]['file_name'] = file_path
                                ax_dic[key]['is_star_file'] = self.is_star_file(file_path)

                        else:
                            if key in mr_dic:
                                if (version > mr_dic[key]['version'] and mile_stone == mr_dic[key]['mile_stone'])\
                                   or (mile_stone == 'annotate' and mile_stone != mr_dic[key]['mile_stone']):
                                    mr_dic[key]['mile_stone'] = mile_stone
                                    mr_dic[key]['version'] = version
                                    mr_dic[key]['content_type'] = 'amber' if content_type == 'dat' else content_type
                                    mr_dic[key]['file_name'] = file_path
                                    mr_dic[key]['is_star_file'] = self.is_star_file(file_path)
                            else:
                                mr_dic[key] = {}
                                mr_dic[key]['mile_stone'] = mile_stone
                                mr_dic[key]['version'] = version
                                mr_dic[key]['content_type'] = 'amber' if content_type == 'dat' else content_type
                                mr_dic[key]['file_name'] = file_path
                                mr_dic[key]['is_star_file'] = self.is_star_file(file_path)

        if has_gromacs:

            gro_count = 0
            dat_count = 0

            for d in ax_dic.values():
                if not d['is_star_file']:
                    content_type = d['content_type']
                    if content_type == 'gromacs':
                        gro_count += 1

            for d in mr_dic.values():
                if not d['is_star_file']:
                    content_type = d['content_type']
                    if content_type == 'dat':
                        dat_count += 1

            if gro_count == 1 and dat_count > 1:

                mr_dic = {}
                ax_dic = {}

                for file_name in sorted(os.listdir(self.__data_dir)):

                    if self.__mr_name_pattern.match(file_name):
                        g = self.__mr_name_pattern.search(file_name).groups()
                        mile_stone = g[0]
                        # part = int(g[1])
                        content_type = g[2]
                        version = int(g[3])

                        key = content_type + g[1]

                        file_path = os.path.join(self.__data_dir, file_name)

                        if content_type == 'gromacs':
                            if key in ax_dic:
                                if (version > ax_dic[key]['version'] and mile_stone == ax_dic[key]['mile_stone'])\
                                   or (mile_stone == 'annotate' and mile_stone != ax_dic[key]['mile_stone']):
                                    ax_dic[key]['mile_stone'] = mile_stone
                                    ax_dic[key]['version'] = version
                                    ax_dic[key]['content_type'] = 'dat'
                                    ax_dic[key]['file_name'] = file_path
                                    ax_dic[key]['is_star_file'] = self.is_star_file(file_path)
                            else:
                                ax_dic[key] = {}
                                ax_dic[key]['mile_stone'] = mile_stone
                                ax_dic[key]['version'] = version
                                ax_dic[key]['content_type'] = 'dat'
                                ax_dic[key]['file_name'] = file_path
                                ax_dic[key]['is_star_file'] = self.is_star_file(file_path)

                        else:
                            if key in mr_dic:
                                if (version > mr_dic[key]['version'] and mile_stone == mr_dic[key]['mile_stone'])\
                                   or (mile_stone == 'annotate' and mile_stone != mr_dic[key]['mile_stone']):
                                    mr_dic[key]['mile_stone'] = mile_stone
                                    mr_dic[key]['version'] = version
                                    mr_dic[key]['content_type'] = 'gromacs' if content_type == 'dat' else content_type
                                    mr_dic[key]['file_name'] = file_path
                                    mr_dic[key]['is_star_file'] = self.is_star_file(file_path)
                            else:
                                mr_dic[key] = {}
                                mr_dic[key]['mile_stone'] = mile_stone
                                mr_dic[key]['version'] = version
                                mr_dic[key]['content_type'] = 'gromacs' if content_type == 'dat' else content_type
                                mr_dic[key]['file_name'] = file_path
                                mr_dic[key]['is_star_file'] = self.is_star_file(file_path)

        self.__mr_file_path = []
        self.__ar_file_path = []
        self.__ar_file_type = []

        for d in mr_dic.values():
            if not d['is_star_file']:
                content_type = d['content_type']
                if content_type == 'amber':
                    self.__ar_file_type.append('nm-res-amb')
                elif content_type == 'cns':
                    self.__ar_file_type.append('nm-res-cns')
                elif content_type == 'cyana':
                    self.__ar_file_type.append('nm-res-cya')
                elif content_type == 'xplor-nih':
                    self.__ar_file_type.append('nm-res-xpl')
                elif content_type == 'rosetta':
                    self.__ar_file_type.append('nm-res-ros')
                elif content_type == 'biosym':
                    self.__ar_file_type.append('nm-res-bio')
                elif content_type == 'dynamo':
                    self.__ar_file_type.append('nm-res-dyn')
                elif content_type == 'gromacs':
                    self.__ar_file_type.append('nm-res-gro')
                elif content_type == 'sybyl':
                    self.__ar_file_type.append('nm-res-syb')
                elif content_type == 'isd':
                    self.__ar_file_type.append('nm-res-isd')
                elif content_type == 'cya':
                    self.__ar_file_type.append('nm-res-cya')
                elif content_type == 'dat':
                    if has_amber:
                        self.__ar_file_type.append('nm-aux-amb')
                    elif has_gromacs:
                        self.__ar_file_type.append('nm-aux-gro')
                    else:
                        self.__ar_file_type.append('nm-res-oth')

                self.__ar_file_path.append(d['file_name'])

            else:
                self.__mr_file_path.append(d['file_name'])

        if has_amber:

            for d in ax_dic.values():
                if not d['is_star_file']:
                    content_type = d['content_type']
                    if content_type == 'amber':
                        self.__ar_file_type.append('nm-res-amb')
                    elif content_type == 'cns':
                        self.__ar_file_type.append('nm-res-cns')
                    elif content_type == 'cyana':
                        self.__ar_file_type.append('nm-res-cya')
                    elif content_type == 'xplor-nih':
                        self.__ar_file_type.append('nm-res-xpl')
                    elif content_type == 'rosetta':
                        self.__ar_file_type.append('nm-res-ros')
                    elif content_type == 'biosym':
                        self.__ar_file_type.append('nm-res-bio')
                    elif content_type == 'dynamo':
                        self.__ar_file_type.append('nm-res-dyn')
                    elif content_type == 'gromacs':
                        self.__ar_file_type.append('nm-res-gro')
                    elif content_type == 'sybyl':
                        self.__ar_file_type.append('nm-res-syb')
                    elif content_type == 'isd':
                        self.__ar_file_type.append('nm-res-isd')
                    elif content_type == 'cya':
                        self.__ar_file_type.append('nm-res-cya')
                    elif content_type == 'dat':
                        self.__ar_file_type.append('nm-aux-amb')

                    self.__ar_file_path.append(d['file_name'])

                else:
                    self.__mr_file_path.append(d['file_name'])

        if has_gromacs:

            for d in ax_dic.values():
                if not d['is_star_file']:
                    content_type = d['content_type']
                    if content_type == 'gromacs':
                        self.__ar_file_type.append('nm-res-amb')
                    elif content_type == 'cns':
                        self.__ar_file_type.append('nm-res-cns')
                    elif content_type == 'cyana':
                        self.__ar_file_type.append('nm-res-cya')
                    elif content_type == 'xplor-nih':
                        self.__ar_file_type.append('nm-res-xpl')
                    elif content_type == 'rosetta':
                        self.__ar_file_type.append('nm-res-ros')
                    elif content_type == 'biosym':
                        self.__ar_file_type.append('nm-res-bio')
                    elif content_type == 'dynamo':
                        self.__ar_file_type.append('nm-res-dyn')
                    elif content_type == 'gromacs':
                        self.__ar_file_type.append('nm-res-gro')
                    elif content_type == 'sybyl':
                        self.__ar_file_type.append('nm-res-syb')
                    elif content_type == 'isd':
                        self.__ar_file_type.append('nm-res-isd')
                    elif content_type == 'cya':
                        self.__ar_file_type.append('nm-res-cya')
                    elif content_type == 'dat':
                        self.__ar_file_type.append('nm-aux-gro')

                    self.__ar_file_path.append(d['file_name'])

                else:
                    self.__mr_file_path.append(d['file_name'])

        pk_dic = {}

        for file_name in sorted(os.listdir(self.__data_dir)):
            if self.__pk_name_pattern.match(file_name):
                g = self.__pk_name_pattern.search(file_name).groups()

                version = int(g[1])

                key = int(g[0])

                file_path = os.path.join(self.__data_dir, file_name)

                if key in pk_dic:
                    if version > pk_dic[key]['version']:
                        pk_dic[key]['version'] = version
                        pk_dic[key]['file_name'] = file_path
                else:
                    pk_dic[key] = {}
                    pk_dic[key]['version'] = version
                    pk_dic[key]['file_name'] = file_path

                self.__has_peak = True

        for key in sorted(pk_dic.keys()):
            self.__ar_file_type.append('nm-pea-any')
            self.__ar_file_path.append(pk_dic[key]['file_name'])

        self.__master_has_cs_loop = self.has_cs_loop(self.__star_file_path)

        cs_title = 'Chemical shifts' if self.__nmr_cif_file_path is None and self.__master_has_cs_loop else 'Master template'
        print(f'{cs_title}: {self.__star_file_path}')
        if self.__nmr_cif_file_path is None and not self.__master_has_cs_loop and self.__cs_ann_file_path is not None:
            print(f'Chemical shifts: {self.__cs_ann_file_path}')
        print(f'Coordinates    : {self.__cif_file_path}')
        if self.__nmr_cif_file_path is not None:
            print(f'NMR data       : {self.__nmr_cif_file_path}')
        if len(self.__mr_file_path) > 0:
            print(f'NMR Restraints : {self.__mr_file_path}')
        if len(self.__ar_file_path) > 0:
            for ar_file_path, ar_file_type in zip(self.__ar_file_path, self.__ar_file_type):
                if ar_file_type.startswith('nm-res'):
                    print(f'NMR Restraints : {ar_file_path} ({ar_file_type})')
                else:
                    print(f'Spectral peaks : {ar_file_path} ({ar_file_type})')

    def is_star_file(self, file_path):

        has_datablock = False
        has_anonymous_saveframe = False
        has_save = False
        has_loop = False
        has_stop = False

        with open(file_path, "r") as ifh:
            for line in ifh:
                if self.__datablock_pattern.match(line):
                    has_datablock = True
                elif self.__sf_anonymous_pattern.match(line):
                    has_anonymous_saveframe = True
                elif self.__save_pattern.match(line):
                    has_save = True
                elif self.__loop_pattern.match(line):
                    has_loop = True
                elif self.__stop_pattern.match(line):
                    has_stop = True

        return has_datablock or has_anonymous_saveframe or has_save or has_loop or has_stop

    def is_amb_top_file(self, file_path):

        with open(file_path, "r") as ifh:
            for line in ifh:
                if self.__amb_top_pattern.match(line):
                    return True

        return False

    def is_amb_rst_file(self, file_path):

        with open(file_path, "r") as ifh:
            for line in ifh:
                if self.__amb_rst_pattern.match(line):
                    return True

        return False

    def is_gro_top_file(self, file_path):

        with open(file_path, "r") as ifh:
            for line in ifh:
                if self.__gro_top_pattern.match(line):
                    return True

        return False

    def is_gro_rst_file(self, file_path):

        with open(file_path, "r") as ifh:
            for line in ifh:
                if self.__gro_rst_pattern.match(line):
                    return True

        return False

    def has_cs_loop(self, file_path):  # pylint: disable=no-self-use
        try:

            star_data = pynmrstar.Entry.from_file(file_path)
            _, lp_list = get_inventory_list(star_data)

            lp_category = '_Atom_chem_shift'

            if lp_category not in lp_list:
                return False

            return not is_empty_loop(star_data, lp_category)

        except Exception:
            return False

    def test_nmr_cs_mr_merge(self):

        utility = NmrDpUtility()

        cs_path_list = [self.__star_file_path]
        if self.__nmr_cif_file_path is None and not self.__master_has_cs_loop and self.__cs_ann_file_path is not None:
            cs_path_list.append(self.__cs_ann_file_path)
        utility.addInput(name='chem_shift_file_path_list', value=cs_path_list, type='file_list')
        combined, original_file_name = is_combined_nmr_data(self.__star_file_path)
        if self.__nmr_cif_file_path is not None:
            utility.addInput(name='nmr_cif_file_path', value=self.__nmr_cif_file_path, type='file')
        if not combined:
            if len(self.__mr_file_path) > 0:
                utility.addInput(name="restraint_file_path_list", value=self.__mr_file_path, type="file_list")
            if len(self.__ar_file_path) > 0:
                ar_path_list = []
                for ar_file_path, ar_file_type in zip(self.__ar_file_path, self.__ar_file_type):
                    if original_file_name is not None and ar_file_type in original_file_name and len(original_file_name[ar_file_type]) > 0:
                        ar_path_list.append({'file_name': ar_file_path, 'file_type': ar_file_type,
                                             'original_file_name': original_file_name[ar_file_type].pop(0)})
                    else:
                        ar_path_list.append({'file_name': ar_file_path, 'file_type': ar_file_type})
                utility.addInput(name='atypical_restraint_file_path_list', value=ar_path_list, type='file_dict_list')
        utility.addInput(name='coordinate_file_path', value=self.__cif_file_path, type='file')
        utility.addInput(name='nonblk_anomalous_cs', value=True, type='param')
        utility.addInput(name='nonblk_bad_nterm', value=True, type='param')
        utility.addInput(name='resolve_conflict', value=True, type='param')
        utility.addInput(name='check_mandatory_tag', value=True, type='param')
        utility.addInput(name='merge_any_pk_as_is', value=True, type='param')
        utility.addInput(name='bmrb_only', value=True, type='param')
        utility.addInput(name='internal', value=True, type='param')
        utility.addInput(name='bmrb_id', value=self.__bmrb_id, type='param')
        utility.addInput(name='dep_sys_name', value='onedep', type='param')
        utility.addInput(name='avs_letter_path', value=self.__avs_letter_path, type='file')
        if len(sys.argv) > 2:
            utility.addInput(name='elec_dep_hash_code', value=sys.argv[2], type='param')
        utility.addOutput(name='leave_intl_note', value=False, type='param')
        utility.addOutput(name='return_letter_path', value=self.__return_letter_path, type='file')
        utility.setDestination(self.__annotated_star_file_path)
        utility.setLog(self.__annotated_log_file_path)
        utility.setVerbose(True)

        utility.op('nmr-cs-mr-merge')

        with open(self.__annotated_log_file_path) as file:
            report = json.loads(file.read())

        if report['error'] is None:
            print(f"{self.__bmrb_id}: {report['information']['status']}")
        elif 'format_issue' in report['error']:
            print(f"{self.__bmrb_id}: {report['information']['status']}\n format_issue: {report['error']['format_issue'][0]['description']}")
        elif 'missing_mandatory_content' in report['error']:
            print(f"{self.__bmrb_id}: {report['information']['status']}\n missing_mandatory_content: {report['error']['missing_mandatory_content'][0]['description']}")
        else:
            error_type = {str(k): len(v) for k, v in report['error'].items() if str(k) != 'total'}
            print(f"{self.__bmrb_id}: {report['information']['status']}, {error_type}")

        if self.__has_peak and os.path.exists(self.__annotated_star_file_path):
            star_data = pynmrstar.Entry.from_file(self.__annotated_star_file_path)
            for sf in star_data.get_saveframes_by_category('spectral_peak_list'):
                set_sf_tag(sf, 'Text_data', '.')
            star_data.write_to_file(self.__ann_wo_raw_pk_star_file_path, show_comments=True, skip_empty_loops=True, skip_empty_tags=False)


if __name__ == '__main__':

    if len(sys.argv) not in (2, 3):
        print('Usage:')
        print('  $ run_annotation_onedep [arg1] ([arg2])')
        print('      [arg1]: BMRB_Accession_Number')
        print('      [arg2]: Elecdep uplaod hash code (Optional)')
        sys.exit(1)

    updator = gen_auth_view_onedep()

    updator.test_nmr_cs_mr_merge()
