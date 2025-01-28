##
# File: CifToNmrStar.py
# Date: 19-Jul-2021
#
# Updates:
# 13-Oct-2021  M. Yokochi - code revision according to PEP8 using Pylint (DAOTHER-7389, issue #5)
# 20-Apr-2022  M. Yokochi - enable to fix broken datablock order of CIF formatted NMR-STAR using NMR-STAR schema (DAOTHER-7407, NMR restraint remediation)
# 28-Jul-2022  M. Yokochi - enable to fix format issue of CIF formatted NMR-STAR (You cannot have two loops with the same category in one saveframe. Category: '_Audit')
# 27-Sep-2022  M. Yokochi - auto fill list ID and entry ID (NMR restraint remediation)
# 13-Jun-2023  M. Yokochi - sort loops in a saveframe based on schema
# 30-May-2024  M. Yokochi - resolve duplication of datablock/saveframe name (DAOTHER-9437)
# 25-Jun-2024  M. Yokochi - strip white spaces in a datablock name derived from the model file (DAOTHER-9511)
# 07-Jan-2025  M. Yokochi - retrieve symbolic label representations (DAOTHER-1728, 9846)
##
""" Wrapper class for CIF to NMR-STAR converter.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "1.0.0"

import sys
import os
import re
import pynmrstar
import pickle
import logging
import hashlib
import collections

from packaging import version
from operator import itemgetter
from typing import Any, IO, Union, Optional

try:
    from wwpdb.utils.nmr.io.mmCIFUtil import mmCIFUtil
    from wwpdb.utils.nmr.AlignUtil import (emptyValue,
                                           trueValue)
except ImportError:
    from nmr.io.mmCIFUtil import mmCIFUtil
    from nmr.AlignUtil import (emptyValue,
                               trueValue)


__pynmrstar_v3_3_1__ = version.parse(pynmrstar.__version__) >= version.parse("3.3.1")


if __pynmrstar_v3_3_1__:
    logger = logging.getLogger('pynmrstar')
    logger.setLevel(logging.ERROR)
else:
    logging.getLogger().setLevel(logging.ERROR)  # set level for pynmrstar


def has_key_value(d: dict, key: Any) -> bool:
    """ Return whether a given dictionary has effective value for a key.
        @return: True if d[key] has effective value, False otherwise
    """

    if not isinstance(d, dict) or key is None:
        return False

    if key in d:
        return d[key] is not None

    return False


def get_value_safe(d: Optional[Union[dict, list, tuple]] = None, key: Optional = None, default: Optional = None) -> Any:
    """ Return value of a given dictionary, list, or tuple for a key.
        @return: value for a key, None (by default) otherwise
    """

    if None in (d, key):
        return default

    return d.get(key, default)


def get_first_sf_tag(sf: pynmrstar.Saveframe, tag: str, default: str = '') -> Any:
    """ Return the first value of a given saveframe tag with decoding symbol notation.
        @return: The first tag value, '' (by default) otherwise.
    """

    if not isinstance(sf, pynmrstar.Saveframe) or tag is None:
        return default

    array = sf.get_tag(tag)

    if len(array) == 0 or array[0] is None:
        return default

    if not isinstance(array[0], str):
        return array[0]

    value = array[0]

    while value.startswith('$$'):
        value = value[1:]

    if len(value) == 0 or value == '$':
        return default

    return value if len(value) < 2 or value[0] != '$' else value[1:]


def set_sf_tag(sf: pynmrstar.Saveframe, tag: str, value: Any):
    """ Set saveframe tag with a given value.
    """

    tagNames = [t[0] for t in sf.tags]

    if isinstance(value, str):

        if len(value) == 0:
            value = None

        while value.startswith('$$'):
            value = value[1:]

        if len(value) == 0 or value == '$':
            value = None

    if tag not in tagNames:
        sf.add_tag(tag, value)
        return

    sf.tags[tagNames.index(tag)][1] = value


def set_lp_tag(lp: pynmrstar.Loop, tag: str, value: Any):
    """ Set loop tag with a given value.
    """

    if tag not in lp.tags:
        lp.add_tag(tag)

        for row in lp:
            row.append(value)

    else:
        col = lp.tags.index(tag)

        for row in lp:
            row[col] = value


def retrieve_symbolic_labels(strData: pynmrstar.Entry):
    """ Retrieve symbolic label representations that serve as saveframe pointers in NMR-STAR.
    """

    def get_parent_sf_framecode(parent_sf_tag_prefix, parent_list_id):
        if isinstance(parent_list_id, int) or (isinstance(parent_list_id, str) and parent_list_id.isdigit()):
            try:
                parent_sf = strData.get_saveframes_by_tag_and_value(f'{parent_sf_tag_prefix}.ID', parent_list_id)[0]
                return get_first_sf_tag(parent_sf, 'Sf_framecode')
            except IndexError:
                try:
                    parent_sf = strData.get_saveframes_by_tag_and_value(f'{parent_sf_tag_prefix}.ID', int(parent_list_id)
                                                                        if isinstance(parent_list_id, str) else str(parent_list_id))[0]
                    return get_first_sf_tag(parent_sf, 'Sf_framecode')
                except IndexError:
                    pass
        return ''

    for sf in strData.frame_list:
        for idx, tag in enumerate(sf.tags):
            if tag[0].endswith('_label'):
                if tag[1] not in emptyValue:
                    if not tag[1].startswith('$'):
                        sf.tags[idx][1] = '$' + tag[1]
                else:
                    id_tag = tag[0][:-6] + '_ID'
                    id_val = get_first_sf_tag(sf, id_tag)
                    if id_val not in emptyValue:
                        parent_sf_framecode = get_parent_sf_framecode(f'_{tag[0][:-6]}', id_val)
                        if len(parent_sf_framecode) > 0 and id_tag in sf.tags:
                            set_sf_tag(sf, id_tag, f'${parent_sf_framecode}')

        for lp in sf.loops:
            label_cols = [idx for idx, tag in enumerate(lp.tags) if tag.endswith('_label')]
            if len(label_cols) == 0:
                continue
            id_cols = [-1] * len(label_cols)
            for idx, label_col in enumerate(label_cols):
                id_tag = lp.tags[label_col][:-6] + '_ID'
                if id_tag in lp.tags:
                    id_cols[idx] = lp.tags.index(id_tag)
            for idx, row in enumerate(lp.data):
                for col, val in enumerate(row):
                    if col in label_cols:
                        if val not in emptyValue:
                            if not val.startswith('$'):
                                lp.data[idx][col] = '$' + val
                        else:
                            id_col = next((id_col for label_col, id_col in zip(label_cols, id_cols) if col == label_col), -1)
                            if id_col == -1 or row[id_col] in emptyValue:
                                continue
                            parent_sf_framecode = get_parent_sf_framecode(f'_{lp.tags[col][:-6]}', row[id_col])
                            if len(parent_sf_framecode) > 0:
                                lp.data[idx][col] = f'${parent_sf_framecode}'


class CifToNmrStar:
    """ Simple CIF to NMR-STAR converter.
    """

    def __init__(self, log: IO = sys.stderr):
        self.__class_name__ = self.__class__.__name__
        self.__version__ = __version__

        self.__lfh = log

        # directory
        self.schema_dir = os.path.dirname(__file__) + '/nmr-star_schema/'

        def load_schema_from_pickle(file_name):
            """ Load NMR-STAR schema from pickle file.
            """

            if os.path.exists(file_name):

                with open(file_name, 'rb') as ifh:
                    return pickle.load(ifh)

            return None

        # NMR-STAR schema
        self.schema = load_schema_from_pickle(self.schema_dir + 'schema.pkl')

        # NMR-STAR schema order
        # self.schema_order = load_schema_from_pickle(self.schema_dir + 'schema_order.pkl')

        # NMR-STAR category order
        self.category_order = load_schema_from_pickle(self.schema_dir + 'category_order.pkl')

        if self.schema is None:
            schema = pynmrstar.Schema()  # network latency occurs if pickle resource files are not available
            self.schema = schema.schema
            self.category_order = schema.category_order

        # NEF category order
        self.category_order_nef = ['_nef_nmr_meta_data',
                                   '_nef_molecular_system',
                                   '_nef_chemical_shift_list',
                                   '_nef_distance_restraint_list',
                                   '_nef_dihedral_restraint_list',
                                   '_nef_rdc_restraint_list',
                                   '_nef_nmr_spectrum',
                                   '_nef_peak_restraint_links']

    def write_schema_as_pickles(self):
        """ Retrieve NMR-STAR schema from pynmrstar.Schema, then write schema objects as each pickle file.
        """

        def write_schema_as_pickle(obj, file_name):
            """ Write NMR-STAR schema as pickle file.
            """

            with open(file_name, 'wb') as ofh:
                pickle.dump(obj, ofh)

        schema = pynmrstar.Schema()  # retrieve the latest schema via interet access

        # print(schema.headers)
        with open(self.schema_dir + 'headers.txt', 'w') as ofh:
            for header in schema.headers:
                ofh.write(header + '\n')
        self.__lfh.write('headers.txt: Done.\n')

        # print(schema.schema)
        write_schema_as_pickle(schema.schema, self.schema_dir + 'schema.pkl')
        self.__lfh.write('schema.pkl: Done.\n')

        # print(schema.schema_order)
        write_schema_as_pickle(schema.schema_order, self.schema_dir + 'schema_order.pkl')
        self.__lfh.write('schema_order.pkl: Done.\n')

        # print(schema.category_order)
        write_schema_as_pickle(schema.category_order, self.schema_dir + 'category_order.pkl')
        self.__lfh.write('category_order.pkl: Done.\n')

        # print(schema.data_types)
        write_schema_as_pickle(schema.data_types, self.schema_dir + 'data_types.pkl')
        self.__lfh.write('data_types.pkl: Done.\n')

        with open(self.schema_dir + 'version.txt', 'w') as ofh:
            ofh.write(schema.version)
        self.__lfh.write(f"version: {schema.version}\n")

    def convert(self, cifPath: Optional[str] = None, strPath: Optional[str] = None, datablockName: Optional[str] = None, maxRepeat: int = 1
                ) -> bool:
        """ Convert CIF formatted NMR data file to normalized NMR-STAR file.
        """

        if None in (cifPath, strPath):
            return False

        try:

            cifObj = mmCIFUtil(filePath=cifPath)

            block_name_list = cifObj.getDataBlockNameList()

            if len(block_name_list) == 0:  # single loop
                return False

            dup_block_name_list = []
            if len(block_name_list) > 1:
                c = collections.Counter(block_name_list).most_common()
                dup_block_name_list = [k for k, v in c if v > 1]

            block_name_pat_w_list_0 = [block_name[:-1] for block_name in block_name_list if block_name.endswith('list_0')]

            block_name_counter = {n: 0 for n in block_name_list}

            entry_id = None

            strData = pynmrstar.Entry.from_scratch(datablockName if datablockName is not None else os.path.basename(cifPath))

            # check category order in CIF
            category_order = []
            previous_order = -1

            sf_category_counter = {}

            for block_name in block_name_list:
                block_name_counter[block_name] += 1
                ext = block_name_counter[block_name]

                dBlockStruct = cifObj.getDataBlockStructure(block_name, ext)

                ordered_block = True
                sf_category = ''

                for category, itVals in dBlockStruct.items():
                    try:
                        current_order = self.category_order.index('_' + category)
                    except ValueError:
                        continue
                    # print(f"{block_name} {category} {current_order}")
                    item = {'block_name': block_name, 'category': category,
                            'category_order': current_order,
                            'block_name_ext': ext}
                    if current_order < previous_order:
                        ordered_block = False
                        for item2 in category_order:
                            if item2['block_name'] == block_name:
                                item2['ordered'] = False
                    item['ordered'] = ordered_block

                    item['sf_category_flag'] = False
                    for _item, _value in zip(itVals['Items'], itVals['Values'][0]):
                        tag = '_' + category + '.' + _item
                        tag = tag.lower()
                        if tag in self.schema:
                            sdict = {k: v for k, v in self.schema[tag].items() if v not in emptyValue}
                            if 'sf_category' not in item:
                                item['sf_category'] = sdict['SFCategory']
                            if 'super_category' not in item:
                                item['super_category'] = sdict['ADIT super category']
                            if 'Sf category flag' in sdict and sdict['Sf category flag'].lower() in trueValue:
                                item['sf_category_flag'] = True
                            if _item == 'Entry_ID' and entry_id in emptyValue:
                                entry_id = _value

                    if 'Sf_category' not in itVals['Items']:
                        _tag = '_' + category.lower() + '.sf_category'
                        if _tag in self.schema:
                            sdict = {k: v for k, v in self.schema[_tag].items() if v not in emptyValue}
                            if 'sf_category' not in item:
                                item['sf_category'] = sdict['SFCategory']
                            if 'super_category' not in item:
                                item['super_category'] = sdict['ADIT super category']
                            if 'Sf category flag' in sdict and sdict['Sf category flag'].lower() in trueValue:
                                item['sf_category_flag'] = True

                    if len(sf_category) == 0:
                        sf_category = item['sf_category']
                    elif sf_category != item['sf_category']:
                        for item2 in category_order:
                            if item2['block_name'] == block_name:
                                item2['ordered'] = False
                        item['ordered'] = False

                    if item not in category_order:
                        category_order.append(item)

                    if item['sf_category_flag']:
                        previous_order = current_order

            if entry_id in emptyValue:
                entry_id = block_name_list[0].strip().replace(' ', '_')  # DAOTHER-9511: replace white space in a datablock name to underscore

            _entry_id = entry_id.upper()

            if datablockName is None:
                strData.entry_id = f'nmr_data_{entry_id.lower()}'

            # reorder
            category_order.sort(key=itemgetter('category_order'))

            # correct block name in case
            reserved_block_names = []
            prev_sf_category = ''
            prev_sf_block_name = ''
            for item in category_order:
                block_name = item['block_name']
                split_block_name = block_name.split('_')

                if block_name in dup_block_name_list:
                    if split_block_name[-1].isdigit():
                        split_block_name.pop()
                    item['new_block_name'] = '_'.join(split_block_name) + '_' + str(item['block_name_ext'])

                elif any(block_name.startswith(pat) for pat in block_name_pat_w_list_0):  # STARCh output
                    if split_block_name[-1].isdigit():
                        list_id = int(split_block_name[-1]) + 1
                        split_block_name.pop()
                        item['new_block_name'] = '_'.join(split_block_name) + '_' + str(list_id)

                if item['ordered']:
                    continue

                if item['sf_category_flag']:
                    if item['sf_category'] == item['super_category']:
                        block_name = item['sf_category']
                    else:
                        list_id = 1
                        while True:
                            block_name = item['sf_category'] + '_' + str(list_id)
                            if block_name not in reserved_block_names:
                                break
                            list_id += 1
                    prev_sf_category = item['sf_category']
                    prev_sf_block_name = block_name
                else:
                    if item['sf_category'] == prev_sf_category:
                        block_name = prev_sf_block_name
                    else:
                        item['missing_sf_category'] = True
                        if item['sf_category'] == item['super_category']:
                            block_name = item['sf_category']
                        else:
                            list_id = 1
                            while True:
                                block_name = item['sf_category'] + '_' + str(list_id)
                                if block_name not in reserved_block_names:
                                    break
                                list_id += 1
                        prev_sf_category = item['sf_category']
                        prev_sf_block_name = block_name

                if 'new_block_name' not in item:
                    item['new_block_name'] = block_name

            ordered_block_names = []
            for item in category_order:
                block_name = item['new_block_name'] if 'new_block_name' in item else item['block_name']
                if block_name not in ordered_block_names:
                    ordered_block_names.append(block_name)

            _category_order = []
            for _block_name in ordered_block_names:
                count = 0
                for item in category_order:
                    block_name = item['new_block_name'] if 'new_block_name' in item else item['block_name']
                    if block_name == _block_name:
                        _category_order.append(item)
                        count += 1
                if count == 1:
                    last_item = _category_order[-1]
                    if not last_item['sf_category_flag'] and last_item['ordered']:
                        last_item['missing_sf_category'] = True
                        last_item['new_block_name'] = last_item['block_name']

            category_order = _category_order

            _sf_category = ''
            cur_list_id = 1

            reserved_block_names = []
            sf = None
            for item in category_order:
                block_name = item['block_name']
                category = item['category']
                sf_category = item['sf_category']
                ext = item['block_name_ext']

                if item['sf_category_flag'] or ('missing_sf_category' in item and item['missing_sf_category']):
                    if sf_category not in sf_category_counter:
                        cur_list_id = 1
                    else:
                        cur_list_id = sf_category_counter[sf_category] + 1
                elif sf_category != _sf_category:
                    cur_list_id = 1

                _sf_category = sf_category

                sf_tag_prefix = next(v['Tag category'] for k, v in self.schema.items()
                                     if v['SFCategory'] == sf_category and v['Tag field'] == 'Sf_category')

                sf_category_counter[sf_category] = cur_list_id
                _cur_list_id = str(cur_list_id)

                if 'missing_sf_category' in item and item['missing_sf_category']:
                    new_block_name = item['new_block_name']

                    if new_block_name in reserved_block_names:
                        continue

                    if sf is not None:
                        strData.add_saveframe(sf)

                    sf = pynmrstar.Saveframe.from_scratch(new_block_name)
                    reserved_block_names.append(new_block_name)
                    sf.set_tag_prefix(sf_tag_prefix)
                    sf.add_tag('Sf_category', sf_category)
                    sf.add_tag('Sf_framecode', new_block_name)
                    sf.add_tag('Entry_ID', _entry_id)

                    if sf_category != item['super_category']:
                        sf.add_tag('ID', _cur_list_id)

                elif item['sf_category_flag']:
                    new_block_name = item['new_block_name'] if 'new_block_name' in item else block_name

                    if new_block_name in reserved_block_names:
                        continue

                    if sf is not None:
                        strData.add_saveframe(sf)

                    sf = pynmrstar.Saveframe.from_scratch(new_block_name)
                    reserved_block_names.append(new_block_name)
                    sf.set_tag_prefix(category)

                    dBlockStruct = cifObj.getDataBlockStructure(block_name, ext)
                    itVals = next(v for k, v in dBlockStruct.items() if k == category)

                    sf.add_tag('Sf_category', sf_category)
                    sf.add_tag('Sf_framecode', new_block_name)
                    if sf_category != 'entry_information':
                        sf.add_tag('Entry_ID', _entry_id)
                        sf.add_tag('ID', _cur_list_id)
                    else:
                        sf.add_tag('ID', _entry_id)

                    for _item, value in zip(itVals['Items'], itVals['Values'][0]):
                        if _item not in ('Sf_category', 'Sf_framecode', 'Entry_ID', 'ID'):
                            sf.add_tag(_item, value)

                if not item['sf_category_flag']:
                    lp = pynmrstar.Loop.from_scratch(category)

                    dBlockStruct = cifObj.getDataBlockStructure(block_name, ext)
                    itVals = next(v for k, v in dBlockStruct.items() if k == category)

                    list_id_idx = entry_id_idx = -1

                    for idx, _item in enumerate(itVals['Items']):
                        lp.add_tag(_item)
                        if sf_category != item['super_category']:
                            tag = '_' + category + '.' + _item
                            tag = tag.lower()
                            if tag in self.schema:
                                sdict = {k: v for k, v in self.schema[tag].items() if v not in emptyValue}
                                if 'Parent tag' in sdict and sdict['Parent tag'] == '_' + sf_tag_prefix + '.ID':
                                    list_id_idx = idx
                        if _item == 'Entry_ID':
                            entry_id_idx = idx

                    for idx, _value in enumerate(itVals['Values']):
                        if list_id_idx != -1:
                            _value[list_id_idx] = _cur_list_id
                        if entry_id_idx != -1:
                            _value[entry_id_idx] = _entry_id
                        lp.add_data(_value)

                    if sf is not None:
                        sf.add_loop(lp)

            if sf is not None:
                strData.add_saveframe(sf)

            retrieve_symbolic_labels(strData)

            self.normalize(strData)

            strData.write_to_file(strPath, show_comments=False, skip_empty_loops=True, skip_empty_tags=False)

            return True

        except ValueError as e:

            sf_anonymous_pattern = re.compile(r'\s*save_\S+\s*')
            save_pattern = re.compile(r'\s*save_\s*')

            split_ext = os.path.splitext(cifPath)
            _cifPath = split_ext[0] + '-corrected' + ('' if len(split_ext) == 1 else split_ext[1])

            changed = False

            with open(cifPath, 'r') as ifh, \
                    open(_cifPath, 'w') as ofh:
                for line in ifh:
                    if sf_anonymous_pattern.match(line) or save_pattern.match(line):
                        ofh.write('#' + line)
                        changed = True
                    else:
                        ofh.write(line)

            if changed and maxRepeat > 0:
                return self.convert(_cifPath, strPath, datablockName, maxRepeat=maxRepeat - 1)

            try:
                os.remove(_cifPath)
            except OSError:
                pass

            self.__lfh.write(f"+{self.__class_name__}.convert() ++ Error  - {str(e)}\n")

            return False

        except Exception as e:
            self.__lfh.write(f"+{self.__class_name__}.convert() ++ Error  - {str(e)}\n")

            return False

    def set_entry_id(self, strData: Union[pynmrstar.Entry, pynmrstar.Saveframe, pynmrstar.Loop], entryId: str
                     ) -> bool:
        """ Set entry ID without changing datablock name.
            @see: pynmrstar.entry
            @return: whether document is modified
        """

        modified = False

        if strData is None:
            return modified

        entryId = entryId.strip().replace(' ', '_')  # DAOTHER-9511: replace white space in a datablock name to underscore

        if isinstance(strData, pynmrstar.Entry):

            for sf in strData.frame_list:
                filled = False

                for tag in sf.tags:
                    fqtn = (sf.tag_prefix + '.' + tag[0]).lower()

                    try:
                        if self.schema[fqtn]['entryIdFlg'] == 'Y':
                            tag[1] = entryId
                            filled = True
                            break
                    except KeyError:
                        pass

                if not filled:
                    entry_id_tag = 'ID' if sf.category == 'entry_information' else 'Entry_ID'

                    fqtn = (sf.tag_prefix + '.' + entry_id_tag).lower()

                    try:
                        if self.schema[fqtn]['entryIdFlg'] == 'Y':
                            set_sf_tag(sf, entry_id_tag, entryId)
                        modified = True
                    except KeyError:
                        pass

                for lp in sf.loops:
                    filled = False

                    for tag in lp.tags:
                        fqtn = (lp.category + '.' + tag).lower()

                        try:
                            if self.schema[fqtn]['entryIdFlg'] == 'Y' or tag == 'Entry_ID':
                                lp[tag] = [entryId] * len(lp[tag])
                                filled = True
                                break
                        except KeyError:
                            pass

                    if not filled:
                        set_lp_tag(lp, 'Entry_ID', entryId)

                        modified = True

        elif isinstance(strData, pynmrstar.Saveframe):

            sf = strData

            filled = False

            for tag in sf.tags:
                fqtn = (sf.tag_prefix + '.' + tag[0]).lower()

                try:
                    if self.schema[fqtn]['entryIdFlg'] == 'Y':
                        tag[1] = entryId
                        filled = True
                        break
                except KeyError:
                    pass

            if not filled:
                entry_id_tag = 'ID' if sf.category == 'entry_information' else 'Entry_ID'

                fqtn = (sf.tag_prefix + '.' + entry_id_tag).lower()

                try:
                    if self.schema[fqtn]['entryIdFlg'] == 'Y':
                        set_sf_tag(sf, entry_id_tag, entryId)
                        modified = True
                except KeyError:
                    pass

            for lp in sf.loops:
                filled = False

                for tag in lp.tags:
                    fqtn = (lp.category + '.' + tag).lower()

                    try:
                        if self.schema[fqtn]['entryIdFlg'] == 'Y' or tag == 'Entry_ID':
                            lp[tag] = [entryId] * len(lp[tag])
                            filled = True
                            break
                    except KeyError:
                        pass

                if not filled:
                    set_lp_tag(lp, 'Entry_ID', entryId)

                    modified = True

        elif isinstance(strData, pynmrstar.Loop):

            lp = strData

            filled = False

            for tag in lp.tags:
                fqtn = (lp.category + '.' + tag).lower()

                try:
                    if self.schema[fqtn]['entryIdFlg'] == 'Y' or tag == 'Entry_ID':
                        lp[tag] = [entryId] * len(lp[tag])
                        filled = True
                        break
                except KeyError:
                    pass

            if not filled:
                set_lp_tag(lp, 'Entry_ID', entryId)

                modified = True

        return modified

    def set_local_sf_id(self, strData: Union[pynmrstar.Entry, pynmrstar.Saveframe, pynmrstar.Loop], listId: Union[int, str]):
        """ Set list ID for a given saveframe or loop.
        """

        if strData is None:
            return

        if isinstance(strData, pynmrstar.Saveframe):

            sf = strData

            for tag in sf.tags:
                fqtn = (sf.tag_prefix + '.' + tag[0]).lower()

                try:
                    if self.schema[fqtn]['lclSfIdFlg'] == 'Y':
                        tag[1] = listId
                        break
                except KeyError:
                    pass

            for lp in sf.loops:

                for tag in lp.tags:
                    fqtn = (lp.category + '.' + tag).lower()

                    try:
                        if self.schema[fqtn]['lclSfIdFlg'] == 'Y':
                            lp[tag] = [listId] * len(lp[tag])
                            break
                    except KeyError:
                        pass

        elif isinstance(strData, pynmrstar.Loop):

            lp = strData

            for tag in lp.tags:
                fqtn = (lp.category + '.' + tag).lower()

                try:
                    if self.schema[fqtn]['lclSfIdFlg'] == 'Y':
                        lp[tag] = [listId] * len(lp[tag])
                        break
                except KeyError:
                    pass

    def normalize(self, strData: Union[pynmrstar.Entry, pynmrstar.Saveframe, pynmrstar.Loop]
                  ) -> Union[pynmrstar.Entry, pynmrstar.Saveframe, pynmrstar.Loop]:
        """ Wrapper function of normalize_str() and normalize_nef().
        """

        if strData is None:
            return strData

        try:
            sf = strData.frame_list[0]
            if sf.category.startswith('nef'):
                return self.normalize_nef(strData)
            return self.normalize_str(strData)
        except (IndexError, AttributeError):
            return strData

    def normalize_str(self, strData: Union[pynmrstar.Entry, pynmrstar.Saveframe, pynmrstar.Loop]
                      ) -> Union[pynmrstar.Entry, pynmrstar.Saveframe, pynmrstar.Loop]:
        """ Sort saveframes, loops, and tags according to NMR-STAR schema.
            @see: pynmrstar.entry.normalize
        """

        if strData is None:
            return strData

        def sf_key(sf):
            """ Helper function to sort the saveframes.
                Returns (category order, saveframe order)
            """

            # If not a real category, generate an artificial but stable order > the real saveframes
            try:
                category_order = self.category_order.index(sf.tag_prefix)
            except (ValueError, KeyError):
                if sf.category is None:
                    category_order = float('infinity')
                else:
                    category_order = len(self.category_order) + abs(int(hashlib.sha1(str(sf.category).encode()).hexdigest(), 16))

            # See if there is an ID tag, and it is a number
            saveframe_id = float('infinity')
            try:
                saveframe_id = int(sf.get_tag("ID")[0])
            except (ValueError, KeyError, IndexError, TypeError):
                # Either there is no ID, or it is not a number. By default it will sort at the end of saveframes of its
                # category. Note that the entry_information ID tag has a different meaning, but since there should
                # only ever be one saveframe of that category, the sort order for it can be any value.
                pass

            return category_order, saveframe_id

        def lp_key(lp):
            """ Helper function to sort the loops.
                Returns (category order)
            """

            try:
                category_order = self.category_order.index(lp.category)
            except (ValueError, KeyError):
                category_order = float('infinity')

            return category_order

        try:
            strData.frame_list.sort(key=sf_key)

            for sf in strData.frame_list:
                sf.sort_tags()
                if len(sf.loops) > 1:
                    sf.loops.sort(key=lp_key)
                # Iterate through the loops
                for lp in sf:
                    lp.sort_tags()

        except Exception as e:
            self.__lfh.write(f"+{self.__class_name__}.normalize() ++ Error  - {str(e)}\n")

        return strData

    def normalize_nef(self, strData: Union[pynmrstar.Entry, pynmrstar.Saveframe, pynmrstar.Loop]
                      ) -> Union[pynmrstar.Entry, pynmrstar.Saveframe, pynmrstar.Loop]:
        """ Sort saveframes of NEF.
        """

        if strData is None:
            return strData

        def sf_key(sf):
            """ Helper function to sort the saveframes.
                Returns (saveframe order)
            """

            try:
                category_order = self.category_order_nef.index(sf.tag_prefix)
            except (ValueError, KeyError):
                if sf.category is None:
                    category_order = float('infinity')
                else:
                    category_order = len(self.category_order_nef) + abs(int(hashlib.sha1(str(sf.category).encode()).hexdigest(), 16))

            return category_order

        try:
            strData.frame_list.sort(key=sf_key)
        except Exception as e:
            self.__lfh.write(f"+{self.__class_name__}.normalize_nef() ++ Error  - {str(e)}\n")

        return strData

    def cleanup(self, strData: pynmrstar.Entry) -> pynmrstar.Entry:
        """ Wrapper function of cleanup_str() and cleanup_nef().
        """

        if strData is None:
            return strData

        try:
            sf = strData.frame_list[0]
            if sf.category.startswith('nef'):
                return self.cleanup_nef(strData)
            return self.cleanup_str(strData)
        except (IndexError, AttributeError):
            return strData

    def cleanup_str(self, strData: pynmrstar.Entry) -> pynmrstar.Entry:
        """ Remove empty/ineffective saveframes and loops of NMR-STAR.
        """

        strData.remove_empty_saveframes()

        list_id_dict = {}
        empty_saveframes = []

        for sf in strData.frame_list:

            if sf.category not in list_id_dict:
                list_id_dict[sf.category] = 1
            else:
                list_id_dict[sf.category] += 1

            has_list_id = any(tag[0] == 'ID' for tag in sf.tags)

            if has_list_id and sf.category != 'entry_information':
                list_id_tag = 'ID' if sf.category != 'chem_comp' else 'PDB_code'
                list_id = next(tag[1] for tag in sf.tags if tag[0] == list_id_tag)
                if list_id not in emptyValue:
                    self.set_local_sf_id(sf, list_id_dict[sf.category]
                                         if isinstance(list_id, int) or list_id.isdigit() else list_id)

            has_eff_sf_tag = any(tag[1] not in emptyValue for tag in sf.tags
                                 if tag[0] not in ('Sf_category', 'Sf_framecode', 'Entry_ID', 'Sf_ID', 'ID'))

            if sf.category == 'NMR_spectrometer_expt':
                if get_first_sf_tag(sf, 'Name') in emptyValue:
                    has_eff_sf_tag = False

            if len(get_first_sf_tag(sf, 'Sf_framecode')) == 0:
                has_eff_sf_tag = False

            entry_info_sf = sf.category == 'entry_information'

            list_id_tag = alt_list_id_tag = None
            if not entry_info_sf:
                list_id_tag = f'{sf.tag_prefix[1:]}_ID'
                if sf.tag_prefix.endswith('_list'):
                    alt_list_id_tag = f'{sf.tag_prefix[1:-5]}_ID'

            empty_loops = []

            for lp in sf.loops:

                if entry_info_sf and lp.category == '_Release':
                    continue

                if lp.category.startswith('_PDBX_'):
                    empty_loops.append(lp)
                    continue

                entry_id_col = lp.tags.index('Entry_ID') if 'Entry_ID' in lp.tags else -1
                sf_id_col = lp.tags.index('Sf_ID') if 'Sf_ID' in lp.tags else -1
                if entry_info_sf:
                    list_id_col = -1
                else:
                    list_id_col = lp.tags.index(list_id_tag) if list_id_tag in lp.tags else -1
                    if list_id_col == -1 and alt_list_id_tag is not None:
                        list_id_col = lp.tags.index(alt_list_id_tag) if alt_list_id_tag in lp.tags else -1

                id_tag = None
                if 'ID' in lp.tags:
                    id_tag = 'ID'
                elif 'Ordinal' in lp.tags:
                    id_tag = 'Ordinal'
                else:
                    id_tags = [tag for tag in lp.tags
                               if tag.endswith('ID') and tag not in ('Sf_ID', 'Entry_ID', list_id_tag, alt_list_id_tag)]
                    if len(id_tags) == 1:
                        id_tag = id_tags[0]

                id_col = lp.tags.index(id_tag) if id_tag is not None else -1

                empty_row_idx = []

                for idx, row in enumerate(lp):

                    if 'Name' in lp.tags:
                        if row[lp.tags.index('Name')] in emptyValue:
                            if lp.category != '_NMR_spectrometer_view':
                                empty_row_idx.append(idx)
                                continue

                            try:
                                vendor = row[lp.tags.index('Manufacturer')]
                                model = row[lp.tags.index('Model')]
                                field = row[lp.tags.index('Field_strength')]
                                if vendor in emptyValue\
                                   or model in emptyValue\
                                   or field in emptyValue:
                                    empty_row_idx.append(idx)
                                    continue
                            except ValueError:
                                empty_row_idx.append(idx)
                                continue

                            for parent_sf in strData.get_saveframes_by_tag_and_value('_NMR_spectrometer.Manufacturer', vendor):
                                if get_first_sf_tag(parent_sf, 'Model') == model\
                                   and get_first_sf_tag(parent_sf, 'Field_strength', field) == field:
                                    row[lp.tags.index('Name')] = get_first_sf_tag(parent_sf, 'Sf_framecode')
                                    break

                    if lp.category == '_Assembly_db_link':
                        if 'Accession_code' in lp.tags and row[lp.tags.index('Accession_code')] in emptyValue:
                            empty_row_idx.append(idx)
                            continue

                    if lp.category == '_Entity_purity':
                        if 'Val' in lp.tags and row[lp.tags.index('Val')] in emptyValue:
                            empty_row_idx.append(idx)
                            continue

                    if any(row[col] not in emptyValue for col in range(len(row))
                           if col not in (entry_id_col, sf_id_col, list_id_col, id_col)):
                        continue

                    empty_row_idx.append(idx)

                if len(empty_row_idx) > 0:
                    for idx in reversed(empty_row_idx):
                        del lp.data[idx]

                if len(lp) == 0:
                    empty_loops.append(lp)
                    continue

                if id_col != -1:
                    for idx, row in enumerate(lp, start=1):
                        if row[id_col] in emptyValue:
                            row[id_col] = idx

            if len(empty_loops) > 0:
                for lp in empty_loops:
                    del sf[lp]

            if not has_eff_sf_tag and len(sf.loops) == 0:
                empty_saveframes.append(sf)

        if len(empty_saveframes) > 0:
            for sf in empty_saveframes:
                strData.remove_saveframe(sf)

        return strData

    def cleanup_nef(self, strData: pynmrstar.Entry) -> pynmrstar.Entry:  # pylint: disable=no-self-use
        """ Remove empty/ineffective saveframes and loops of NEF.
        """

        strData.remove_empty_saveframes()

        empty_saveframes = []

        for sf in strData.frame_list:

            has_eff_sf_tag = any(tag[1] not in emptyValue for tag in sf.tags
                                 if tag[0] not in ('sf_category', 'sf_framecode'))

            if len(get_first_sf_tag(sf, 'sf_framecode')) == 0:
                has_eff_sf_tag = False

            empty_loops = []

            for lp in sf.loops:

                id_tag = None
                id_tags = [tag for tag in lp.tags if tag.endswith('_id')]
                if len(id_tags) == 1:
                    id_tag = id_tags[0]

                id_col = lp.tags.index(id_tag) if id_tag is not None else -1

                empty_row_idx = []

                for idx, row in enumerate(lp):

                    if any(row[col] not in emptyValue for col in range(len(row)) if col != id_col):
                        continue

                    empty_row_idx.append(idx)

                if len(empty_row_idx) > 0:
                    for idx in reversed(empty_row_idx):
                        del lp.data[idx]

                if len(lp) == 0:
                    empty_loops.append(lp)
                    continue

                if id_col != -1:
                    for idx, row in enumerate(lp, start=1):
                        if row[id_col] in emptyValue:
                            row[id_col] = idx

            if len(empty_loops) > 0:
                for lp in empty_loops:
                    del sf[lp]

            if not has_eff_sf_tag and len(sf.loops) == 0:
                empty_saveframes.append(sf)

        if len(empty_saveframes) > 0:
            for sf in empty_saveframes:
                strData.remove_saveframe(sf)

        return strData
