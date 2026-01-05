# File: PdbMrSplitter.py
# Date: 05-Jan-2026
#
# Updates:
##
""" Wrapper class for public PDB-MR format file splitter.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "1.0.0"

import os
import re
import codecs
import shutil
import chardet

from operator import itemgetter
from striprtf.striprtf import rtf_to_text
from typing import Any, IO, List, Tuple, Optional

try:
    from wwpdb.utils.nmr.NmrDpUtilConst import MR_MAX_SPACER_LINES
    from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
    from wwpdb.utils.nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from wwpdb.utils.nmr.nef.NEFTranslator import (NEFTranslator,
                                                   MAX_DIM_NUM_OF_SPECTRA)
    from wwpdb.utils.nmr.AlignUtil import (monDict3,
                                           getRestraintFormatName)
    from wwpdb.utils.nmr.CifToNmrStar import CifToNmrStar
    from wwpdb.utils.nmr.NmrDpReport import NmrDpReport
    from wwpdb.utils.nmr.NmrVrptUtility import uncompress_gzip_file
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (translateToStdResName,
                                                       startsWithPdbRecord,
                                                       getRestraintName,
                                                       CS_RESTRAINT_ERROR,
                                                       CS_RESTRAINT_RANGE,
                                                       CYANA_MR_FILE_EXTS)
    from wwpdb.utils.nmr.mr.AmberMRReader import AmberMRReader
    from wwpdb.utils.nmr.mr.AmberPTReader import AmberPTReader
    from wwpdb.utils.nmr.mr.AriaMRReader import AriaMRReader
    from wwpdb.utils.nmr.mr.AriaMRXReader import AriaMRXReader
    from wwpdb.utils.nmr.mr.BareMRReader import BareMRReader
    from wwpdb.utils.nmr.mr.BarePDBReader import BarePDBReader
    from wwpdb.utils.nmr.mr.BiosymMRReader import BiosymMRReader
    from wwpdb.utils.nmr.mr.CharmmCRDReader import CharmmCRDReader
    from wwpdb.utils.nmr.mr.CharmmMRReader import CharmmMRReader
    from wwpdb.utils.nmr.mr.CnsMRReader import CnsMRReader
    from wwpdb.utils.nmr.mr.CyanaMRReader import CyanaMRReader
    from wwpdb.utils.nmr.mr.CyanaNOAReader import CyanaNOAReader
    from wwpdb.utils.nmr.mr.DynamoMRReader import DynamoMRReader
    from wwpdb.utils.nmr.mr.GromacsMRReader import GromacsMRReader
    from wwpdb.utils.nmr.mr.GromacsPTReader import GromacsPTReader
    from wwpdb.utils.nmr.mr.IsdMRReader import IsdMRReader
    from wwpdb.utils.nmr.mr.RosettaMRReader import RosettaMRReader
    from wwpdb.utils.nmr.mr.SchrodingerMRReader import SchrodingerMRReader
    from wwpdb.utils.nmr.mr.SybylMRReader import SybylMRReader
    from wwpdb.utils.nmr.mr.XplorMRReader import XplorMRReader
    from wwpdb.utils.nmr.pk.AriaPKReader import AriaPKReader
    from wwpdb.utils.nmr.pk.BarePKReader import BarePKReader
    from wwpdb.utils.nmr.pk.CcpnPKReader import CcpnPKReader
    from wwpdb.utils.nmr.pk.OliviaPKReader import OliviaPKReader
    from wwpdb.utils.nmr.pk.NmrPipePKReader import NmrPipePKReader
    from wwpdb.utils.nmr.pk.PonderosaPKReader import PonderosaPKReader
    from wwpdb.utils.nmr.pk.NmrViewPKReader import NmrViewPKReader
    from wwpdb.utils.nmr.pk.SparkyPKReader import SparkyPKReader
    from wwpdb.utils.nmr.pk.SparkySPKReader import SparkySPKReader
    from wwpdb.utils.nmr.pk.TopSpinPKReader import TopSpinPKReader
    from wwpdb.utils.nmr.pk.VnmrPKReader import VnmrPKReader
    from wwpdb.utils.nmr.pk.XeasyPKReader import XeasyPKReader
    from wwpdb.utils.nmr.pk.XeasyPROTReader import XeasyPROTReader
    from wwpdb.utils.nmr.pk.XwinNmrPKReader import XwinNmrPKReader
except ImportError:
    from nmr.NmrDpUtilConst import MR_MAX_SPACER_LINES
    from nmr.ChemCompUtil import ChemCompUtil
    from nmr.BMRBChemShiftStat import BMRBChemShiftStat
    from nmr.nef.NEFTranslator import (NEFTranslator,
                                       MAX_DIM_NUM_OF_SPECTRA)
    from nmr.AlignUtil import (monDict3,
                               getRestraintFormatName)
    from nmr.CifToNmrStar import CifToNmrStar
    from nmr.NmrDpReport import NmrDpReport
    from nmr.NmrVrptUtility import uncompress_gzip_file
    from nmr.mr.ParserListenerUtil import (translateToStdResName,
                                           startsWithPdbRecord,
                                           getRestraintName,
                                           CS_RESTRAINT_ERROR,
                                           CS_RESTRAINT_RANGE,
                                           CYANA_MR_FILE_EXTS)
    from nmr.mr.AmberMRReader import AmberMRReader
    from nmr.mr.AmberPTReader import AmberPTReader
    from nmr.mr.AriaMRReader import AriaMRReader
    from nmr.mr.AriaMRXReader import AriaMRXReader
    from nmr.mr.BareMRReader import BareMRReader
    from nmr.mr.BarePDBReader import BarePDBReader
    from nmr.mr.BiosymMRReader import BiosymMRReader
    from nmr.mr.CharmmCRDReader import CharmmCRDReader
    from nmr.mr.CharmmMRReader import CharmmMRReader
    from nmr.mr.CnsMRReader import CnsMRReader
    from nmr.mr.CyanaMRReader import CyanaMRReader
    from nmr.mr.CyanaNOAReader import CyanaNOAReader
    from nmr.mr.DynamoMRReader import DynamoMRReader
    from nmr.mr.GromacsMRReader import GromacsMRReader
    from nmr.mr.GromacsPTReader import GromacsPTReader
    from nmr.mr.IsdMRReader import IsdMRReader
    from nmr.mr.RosettaMRReader import RosettaMRReader
    from nmr.mr.SchrodingerMRReader import SchrodingerMRReader
    from nmr.mr.SybylMRReader import SybylMRReader
    from nmr.mr.XplorMRReader import XplorMRReader
    from nmr.pk.AriaPKReader import AriaPKReader
    from nmr.pk.BarePKReader import BarePKReader
    from nmr.pk.CcpnPKReader import CcpnPKReader
    from nmr.pk.OliviaPKReader import OliviaPKReader
    from nmr.pk.NmrPipePKReader import NmrPipePKReader
    from nmr.pk.PonderosaPKReader import PonderosaPKReader
    from nmr.pk.NmrViewPKReader import NmrViewPKReader
    from nmr.pk.SparkyPKReader import SparkyPKReader
    from nmr.pk.SparkySPKReader import SparkySPKReader
    from nmr.pk.TopSpinPKReader import TopSpinPKReader
    from nmr.pk.VnmrPKReader import VnmrPKReader
    from nmr.pk.XeasyPKReader import XeasyPKReader
    from nmr.pk.XeasyPROTReader import XeasyPROTReader
    from nmr.pk.XwinNmrPKReader import XwinNmrPKReader


CS_ERROR_MIN = CS_RESTRAINT_ERROR['min_exclusive']
CS_ERROR_MAX = CS_RESTRAINT_ERROR['max_exclusive']

CS_RANGE_MIN = CS_RESTRAINT_RANGE['min_inclusive']
CS_RANGE_MAX = CS_RESTRAINT_RANGE['max_inclusive']

mr_file_name_pattern = re.compile(r'^([Pp][Dd][Bb]_)?([0-9]{4})?[0-9][0-9A-Za-z]{3}.mr$')

datablock_pattern = re.compile(r'\s*data_(\S+)\s*')
sf_anonymous_pattern = re.compile(r'\s*save_\S+\s*')
save_pattern = re.compile(r'\s*save_\s*')
loop_pattern = re.compile(r'\s*loop_\s*')
stop_pattern = re.compile(r'\s*stop_\s*')
cif_stop_pattern = re.compile(r'#\s*')
ws_pattern = re.compile(r'\s+')
comment_pattern = re.compile(r'\s*[#!]+(.*)')
gromacs_comment_pattern = re.compile(r'\s*;+[^0-9]?(.*)')
cyana_unset_info_pattern = re.compile(r'\s*unset\s+info.*')
cyana_print_pattern = re.compile(r'\s*print\s+\".*\".*')

category_pattern = re.compile(r'\s*_(\S*)\..*\s*')
tagvalue_pattern = re.compile(r'\s*_(\S*)\.(\S*)\s+(.*)\s*')
sf_category_pattern = re.compile(r'\s*_\S*\.Sf_category\s*\S+\s*')
sf_framecode_pattern = re.compile(r'\s*_\S*\.Sf_framecode\s*\s+\s*')

onedep_model_file_pattern = re.compile(r'^(D_[0-9]{6,10})_model_P1.cif.V\d+$')
onedep_upload_file_pattern = re.compile(r'(.*)\-upload_(.*)\.V(.*)$')
onedep_file_pattern = re.compile(r'(.*)\.V(.*)$')
mr_file_header_pattern = re.compile(r'(.*)# Restraints file (\d+): (\S+)\s*')

sel_mr_file_header_pattern = re.compile(r'^# Restraints file \((\S+)\): (\S+)\s*')
sel_pk_file_header_pattern = re.compile(r'^# Peak list file \((\S+)\): (\S+)\s*')
sel_cs_file_header_pattern = re.compile(r'^# Chemical shifts file \((\S+)\): (\S+)\s*')

pynmrstar_lp_obj_pattern = re.compile(r"\<pynmrstar\.Loop '(.*)'\>")
pdb_first_atom_pattern = re.compile(r'ATOM +1 .*')

amber_a_format_pattern = re.compile(r'%FORMAT\((\d+)a(\d+)\)\s*')
amber_i_format_pattern = re.compile(r'%FORMAT\((\d+)I(\d+)\)\s*')
amber_r_pattern = re.compile(r'r(\d+)=(.*)')

amber_rst_pattern = re.compile(r'\s*&[Rr][Ss][Tt].*')
amber_end_pattern = re.compile(r'\s*(?:&[Ee][Nn][Dd]|\/)\s*')
amber_missing_end_err_msg = "missing END at"  # NOTICE: depends on ANTLR v4 and (Xplor|Cns)MRLexer.g4
amber_extra_end_err_msg_pattern = re.compile(r"extraneous input '(?:&[Ee][Nn][Dd]|\/)' expecting .*")  # NOTICE: depends on ANTLR v4
amber_expecting_comma_pattern = re.compile("expecting \\{.*Comma.*\\}")  # NOTICE: depends on ANTLR v4 and AmberMRLexer.g4

xplor_any_assi_pattern = re.compile(r'[Aa][Ss][Ss][Ii][Gg]?[Nn]?')
xplor_any_rest_pattern = re.compile(r'[Rr][Ee][Ss][Tt][Rr]?[Aa]?[Ii]?[Nn]?[Tt]?[Ss]?')
xplor_any_set_pattern = re.compile(r'[Ss][Ee][Tt]')
xplor_class_pattern = re.compile(r'\s*[Cc][Ll][Aa][Ss][Ss]?[Ii]?.*')
xplor_assi_pattern = re.compile(r'\s*[Aa][Ss][Ss][Ii][Gg]?[Nn]?.*')
xplor_rest_pattern = re.compile(r'\s*[Rr][Ee][Ss][Tt][Rr]?[Aa]?[Ii]?[Nn]?[Tt]?[Ss]?.*')
xplor_set_pattern = re.compile(r'\s*[Ss][Ee][Tt].*')
xplor_end_pattern = re.compile(r'\s*[Ee][Nn][Dd].*')
xplor_missing_end_err_msg = "missing End at"  # NOTICE: depends on ANTLR v4 and (Xplor|Cns)MRLexer.g4
xplor_extra_end_err_msg_pattern = re.compile(r"extraneous input '[Ee][Nn][Dd]' expecting .*")  # NOTICE: depends on ANTLR v4
xplor_extra_assi_err_msg_pattern = re.compile(r"extraneous input '[Aa][Ss][Ss][Ii][Gg]?[Nn]?' expecting L_paren")  # NOTICE: depends on ANTLR v4 and (Xplor|Cns)MRLexer.g4
xplor_extra_ssi_err_msg_pattern = re.compile(r"extraneous input '[Aa]?[Ss][Ss][Ii]\S*' .*")  # NOTICE: depends on ANTLR v4
xplor_extra_l_paren_err_msg_pattern = re.compile(r"extraneous input '\(' expecting .*")  # NOTICE: depends on ANTLR v4
xplor_expecting_symbol_pattern = re.compile("expecting \\{.*Symbol_name.*\\}")  # NOTICE: depends on ANTLR v4 and (Xplor|Cns)MRLexer.g4
xplor_expecting_equ_op_pattern = re.compile("expecting \\{.*Equ_op.*\\}")  # NOTICE: depends on ANTLR v4 and (Xplor|Cns)MRLexer.g4
xplor_expecting_seg_id_pattern = re.compile("expecting \\{.*SegIdentifier.*\\}")  # NOTICE: depends on ANTLR v4 and (Xplor|Cns)MRLexer.g4

seq_mismatch_warning_pattern = re.compile(r"\[Sequence mismatch warning\] \[.*\] The residue '(\d+):([0-9A-Z]+)' is not present "
                                          r"in polymer sequence of chain (\S+) of the coordinates. Please update the sequence in the Macromolecules page.")

inconsistent_restraint_warning_pattern = re.compile(r"^\[[^\]]+\] \[Check the (\d+)th row of [^,]+s ?.*, (\S+)\] .*$")
inconsistent_restraint_warning_wo_sf_pattern = re.compile(r"^\[[^\]]+\] \[Check the (\d+)th row of ([^,]+)s.*\] .*$")

gromacs_tag_pattern = re.compile(r'\s*[\s+[0-9a-z_]+\s+\]')

mismatched_input_err_msg = "mismatched input"  # NOTICE: depends on ANTLR v4
extraneous_input_err_msg = "extraneous input"  # NOTICE: depends on ANTLR v4
no_viable_alt_err_msg = "no viable alternative at input"  # NOTICE: depends on ANTLR v4
expecting_l_paren = "expecting L_paren"  # NOTICE: depends on ANTLR v4 and (Xplor|Cns)MRLexer.g4

possible_typo_for_comment_out_pattern = re.compile(r'\s*([13])$')

sparky_assignment_pattern = re.compile(r'[\w\+\*\?\'\"\/]+-[\w\+\*\?\'\"\/]+\S*')

deep_l_parens_pattern = re.compile(r'.*\(\s*\(\s*\(\s*\(.*')
deep_r_parens_pattern = re.compile(r'.*\)\s*\)\s*\)\s*\).*')

concat_seq_id_ins_code_pattern = re.compile(r'(\d+)([A-Za-z\.\?]+)')

comment_code_mixed_set = {'#', '!'}

linear_mr_file_types = ('nm-res-bio', 'nm-res-cya', 'nm-res-ros', 'nm-res-syb')

retrial_mr_file_types = ('nm-res-ari', 'nm-res-arx', 'nm-res-bio', 'nm-res-cns',
                         'nm-res-cha', 'nm-res-cya', 'nm-res-dyn', 'nm-res-isd',
                         'nm-res-noa', 'nm-res-ros', 'nm-res-sch', 'nm-res-syb',
                         'nm-res-xpl')

parsable_mr_file_types = ('nm-aux-amb', 'nm-aux-cha', 'nm-aux-gro', 'nm-aux-pdb',
                          'nm-res-amb', 'nm-res-ari', 'nm-res-arx', 'nm-res-bar',
                          'nm-res-bio', 'nm-res-cha', 'nm-res-cns', 'nm-res-cya',
                          'nm-res-dyn', 'nm-res-gro', 'nm-res-isd', 'nm-res-noa',
                          'nm-res-sch', 'nm-res-syb', 'nm-res-ros', 'nm-res-xpl')

archival_mr_file_types = ('nmr-star',
                          'nm-aux-amb', 'nm-aux-cha', 'nm-aux-gro', 'nm-aux-pdb',
                          'nm-res-amb', 'nm-res-ari', 'nm-res-arx', 'nm-res-bar',
                          'nm-res-bio', 'nm-res-cha', 'nm-res-cns', 'nm-res-cya',
                          'nm-res-dyn', 'nm-res-gro', 'nm-res-isd', 'nm-res-noa',
                          'nm-res-oth', 'nm-res-sax', 'nm-res-sch', 'nm-res-syb',
                          'nm-res-ros', 'nm-res-xpl')

parsable_pk_file_types = ('nm-aux-xea',
                          'nm-pea-ari', 'nm-pea-bar', 'nm-pea-ccp', 'nm-pea-oli',
                          'nm-pea-pip', 'nm-pea-pon', 'nm-pea-spa', 'nm-pea-sps',
                          'nm-pea-top', 'nm-pea-vie', 'nm-pea-vnm', 'nm-pea-xea',
                          'nm-pea-xwi')


def detect_bom(fPath: str, default: str = 'utf-8') -> str:
    """ Detect BOM of input file.
    """

    with open(fPath, 'rb') as ifh:
        raw = ifh.read(4)

    for enc, boms in \
            ('utf-8-sig', (codecs.BOM_UTF8,)), \
            ('utf-16', (codecs.BOM_UTF16_LE, codecs.BOM_UTF16_BE)), \
            ('utf-32', (codecs.BOM_UTF32_LE, codecs.BOM_UTF32_BE)):
        if any(raw.startswith(bom) for bom in boms):
            return enc

    return default


def convert_codec(inPath: str, outPath: str, in_codec: str = 'utf-8', out_codec: str = 'utf-8'):
    """ Convert codec of input file.
    """

    with open(inPath, 'rb') as ifh, \
            open(outPath, 'w+b') as ofh:
        contents = ifh.read()
        ofh.write(contents.decode(in_codec).encode(out_codec))


def convert_rtf_to_ascii(inPath: str, outPath: str):
    """ Convert RTF file to ASCII text file.
    """

    with open(inPath, 'r') as ifh, \
            open(outPath, 'w+') as ofh:
        contents = ifh.read()
        ofh.write(rtf_to_text(contents, encoding='ascii', errors='ignore'))


def is_binary_file(fPath: str) -> bool:
    """ Check if there are non-ascii or non-printable characters in a file.
    """

    with open(fPath, 'rb') as ifh:
        chunk = ifh.read(1024)
        if b'\0' in chunk:
            return True

    return False


def is_rtf_file(fPath: str) -> bool:
    """ Check if there are RTF header characters in a file.
    """

    with open(fPath, 'rb') as ifh:
        chunk = ifh.read(1024)
        if b'\x7b\x5c\x72\x74\x66\x31' in chunk:
            return True

    return False


def is_eps_or_pdf_file(fPath: str) -> bool:
    """ Check if there are EPS/PDF header characters in a file.
    """

    with open(fPath, 'rb') as ifh:
        chunk = ifh.read(5)
        if chunk in (b'%!PS-', b'%PDF-'):
            return True

    return False


def detect_encoding(line: str) -> str:
    """ Return encoding of a given string.
    """

    try:
        result = chardet.detect(line.encode('utf-8'))
        return result['encoding']
    except Exception:
        return 'binary'


def get_type_of_star_file(fPath: str) -> str:
    """ Return type of a STAR file.
        @return: 'str' for STAR, 'cif' for CIF, 'other' otherwise
    """

    codec = detect_bom(fPath, 'utf-8')

    _fPath = __fPath = None

    if codec != 'utf-8':
        _fPath = fPath + '~'
        convert_codec(fPath, _fPath, codec, 'utf-8')
        fPath = _fPath

    if is_rtf_file(fPath):
        __fPath = fPath + '.rtf2txt'
        convert_rtf_to_ascii(fPath, __fPath)
        fPath = __fPath

    try:

        is_cif = has_datablock = has_anonymous_saveframe = has_save = has_loop = has_stop = False

        with open(fPath, 'r', encoding='utf-8', errors='ignore') as ifh:
            for line in ifh:
                str_syntax = False
                if datablock_pattern.match(line):
                    str_syntax = has_datablock = True
                elif sf_anonymous_pattern.match(line):
                    str_syntax = has_anonymous_saveframe = True
                elif save_pattern.match(line):
                    str_syntax = has_save = True
                elif loop_pattern.match(line):
                    str_syntax = has_loop = True
                elif stop_pattern.match(line):
                    str_syntax = has_stop = True

                if str_syntax:
                    if (has_anonymous_saveframe and has_save) or (has_loop and has_stop):
                        return 'str'
                    if has_datablock and has_loop and not has_stop:
                        is_cif = True

        return 'cif' if is_cif else 'other'

    finally:

        if _fPath is not None:
            try:
                os.remove(_fPath)
            except OSError:
                pass

        if __fPath is not None:
            try:
                os.remove(__fPath)
            except OSError:
                pass


def concat_restraint_names(content_subtype: Optional[str]) -> str:
    """ Return concatenated restraint names.
    """

    if content_subtype is None:
        return ''

    f = []

    for k, v in content_subtype.items():
        if v == 0:
            continue
        try:
            f.append(getRestraintName(k))
        except KeyError:
            pass

    return ', '.join(f)


def get_peak_list_format(fPath: str, asCode: bool = False) -> Optional[str]:
    """ Return peak list format for a input file.
    """

    header = None

    with open(fPath, 'r', encoding='utf-8', errors='ignore') as ifh:

        for idx, line in enumerate(ifh):

            if line.isspace() or comment_pattern.match(line):

                if 'Number of dimensions' in line or line.startswith('#INAME') or line.startswith('#CYANAFORMAT')\
                   or ('Amplitude' in line or 'Intensity' in line or 'Volume' in line):
                    header = line

                else:  # XwinNMR, but not CCPN

                    file_type = get_peak_list_format_from_string(line, header, asCode)

                    if file_type is not None:

                        if file_type in ('CCPN', 'nm-pea-ccp'):
                            header = line
                            continue

                        return file_type

                continue

            if 'label' in line and 'data' in line and 'dataset' not in line:
                header = line
                continue

            if (' w1 ' in line and ' w2' in line) or ('Assignment' in line and 'Shift (ppm)' in line)\
               or ('eak' in line and ('abel' in line or 'nnotation' in line or 'ssign' in line)
                   and ('F1' in line or 'f1' in line) and ('F2' in line or 'f2' in line)):
                header = line
                continue

            file_type = get_peak_list_format_from_string(line, header, asCode)

            if file_type is not None or idx >= MR_MAX_SPACER_LINES:

                if file_type in ('Sparky', 'nm-pea-spa') and idx < 20 and header is not None\
                   and 'Assignment' in header and 'Shift (ppm)' in header:

                    col = re.split(r'[\s\t]+', line.strip())
                    len_col = len(col)

                    if sparky_assignment_pattern.match(col[0]):

                        d = len_col - 1

                        if d == 2:
                            header = ' Assignment  w1  w2\n'
                        elif d == 3:
                            header = ' Assignment  w1  w2  w3\n'
                        elif d == 4:
                            header = ' Assignment  w1  w2  w3  w4\n'
                        else:
                            return None

                        try:

                            with open(fPath, 'r', encoding='utf-8', errors='ignore') as ifh, \
                                    open(fPath + '~', 'w', encoding='utf-8') as ofh:
                                ofh.write(header)
                                for _line in ifh:
                                    if 'peaks' in _line or 'Shift (ppm)' in _line:
                                        continue
                                    ofh.write(_line)

                            os.replace(fPath + '~', fPath)

                        except OSError:
                            pass

                if file_type in ('CCPN', 'nm-pea-ccp') and idx < 20 and header is not None\
                   and ('Position F1' in header or 'Shift F1' in header) and ('Position F2' in header or 'Shift F2' in header)\
                   and 'Assign F1' in header and 'Assign F2' in header:  # and ('Height' in header or 'Volume' in header):

                    header = header.replace('#', '')

                    try:

                        with open(fPath, 'r', encoding='utf-8', errors='ignore') as ifh, \
                                open(fPath + '~', 'w', encoding='utf-8') as ofh:
                            ofh.write(header)
                            for _line in ifh:

                                if ('Position F1' in _line or 'Shift F1' in _line) and ('Position F2' in _line or 'Shift F2' in _line)\
                                   and 'Assign F1' in _line and 'Assign F2' in _line:  # and ('Height' in _line or 'Volume' in _line):
                                    continue

                                if not _line.startswith('#'):
                                    ofh.write(_line)

                        os.replace(fPath + '~', fPath)

                    except OSError:
                        pass

                if file_type in ('CCPN', 'nm-pea-ccp') and idx < 20 and header is None and ',' in line\
                   and ('Position F1' in line or 'Shift F1' in line) and ('Position F2' in line or 'Shift F2' in line)\
                   and 'Assign F1' in line and 'Assign F2' in line:  # and ('Height' in line or 'Volume' in line):

                    try:

                        with open(fPath, 'r', encoding='utf-8', errors='ignore') as ifh, \
                                open(fPath + '~', 'w', encoding='utf-8') as ofh:
                            for _line in ifh:
                                ofh.write(_line.replace(',', ' '))

                        os.replace(fPath + '~', fPath.replace('~', ''))

                    except OSError:
                        pass

                if file_type is None or idx < 20:
                    return file_type

                # fix partially broken NMRVIEW header
                if file_type in ('NMRView', 'nm-pea-vie') and header is not None\
                   and 'label' in header and 'data' in header and 'dataset' not in header\
                   and 'sw' in line and 'sf' in line:

                    try:

                        i = 0

                        with open(fPath, 'r', encoding='utf-8', errors='ignore') as ifh, \
                                open(fPath + '~', 'w', encoding='utf-8') as ofh:
                            for _line in ifh:
                                if i == idx - 1:
                                    ofh.write('label dataset sw sf\n')
                                elif i == idx:
                                    pass
                                else:
                                    ofh.write(_line)
                                i += 1

                        os.replace(fPath + '~', fPath)

                    except OSError:
                        pass

                    return file_type

                # fix partially broken SPARKY header
                if file_type in ('Sparky', 'nm-pea-spa') and header is None\
                   and ' w1 ' not in line and ' w2' not in line:

                    col = re.split(r'[\s\t]+', line.strip())
                    len_col = len(col)

                    if sparky_assignment_pattern.match(col[0]):

                        d = len_col - 2

                        if d == 2:
                            header = ' Assignment  w1  w2  Data Height\n'
                        elif d == 3:
                            header = ' Assignment  w1  w2  w3  Data Height\n'
                        elif d == 4:
                            header = ' Assignment  w1  w2  w3  w4  Data Height\n'
                        else:
                            return None

                    else:

                        d = len_col - 1

                        if d == 2:
                            header = ' w1  w2  Data Height\n'
                        elif d == 3:
                            header = ' w1  w2  w3  Data Height\n'
                        elif d == 4:
                            header = ' w1  w2  w3  w4  Data Height\n'
                        else:
                            return None

                    try:

                        with open(fPath, 'r', encoding='utf-8', errors='ignore') as ifh, \
                                open(fPath + '~', 'w', encoding='utf-8') as ofh:
                            ofh.write(header)
                            for _line in ifh:
                                ofh.write(_line)

                        os.replace(fPath + '~', fPath)

                    except OSError:
                        pass

                    return file_type

    return None


def get_peak_list_format_from_string(string: str, header: Optional[str] = None, asCode: bool = False) -> Optional[str]:
    """ Return peak list format for a given input.
    """

    col = re.split(r'[\s\t]+', string.strip())
    string = ' '.join(col)
    len_col = len(col)

    if header is not None and ('Number of dimensions' in header or header.startswith('#INAME') or header.startswith('#CYANAFORMAT')):  # XEASY peak list
        if 'U' in col or 'T' in col:
            return 'nm-pea-xea' if asCode else 'XEASY'

    if ' w1 ' in string and ' w2' in string:  # Sparky peak list
        return 'nm-pea-spa' if asCode else 'Sparky'

    if '<sparky save file>' in string:  # Sparky save file
        return 'nm-pea-sps' if asCode else 'Sparky'

    if 'label' in string and 'dataset' in string and 'sw' in string and 'sf' in string:  # NMRView peak list
        return 'nm-pea-vie' if asCode else 'NMRView'

    if 'TYPEDEF IDX_TBL_' in string or 'TYPEDEF ASS_TBL_' in string:  # OLIVIA
        return 'nm-pea-oli' if asCode else 'Olivia'

    if 'VARS' in string and 'X_PPM' in string and 'Y_PPM' in string:  # NMRPipe peak list
        return 'nm-pea-pip' if asCode else 'NMRPipe'

    if 'VARS' in string and 'PkID' in string and 'X' in string and 'Y' in string and 'Intensity' in string:  # PIPP peak list
        return 'nm-pea-pip' if asCode else 'NMRPipe'

    if 'DATA' in string and 'DIMCOUNT' in string:
        return 'nm-pea-pip' if asCode else 'NMRPipe'

    if '<!DOCTYPE spectrum SYSTEM' in string or '<spectrum name=' in string:  # ARIA peak list
        return 'nm-pea-ari' if asCode else 'ARIA'

    if ('Position F1' in string or 'Shift F1' in string) and ('Position F2' in string or 'Shift F2' in string)\
       and 'Assign F1' in string and 'Assign F2' in string:  # and ('Height' in string or 'Volume' in string):
        return 'nm-pea-ccp' if asCode else 'CCPN'

    if 'NOESYTYPE' in string:  # PONDEROSA peak list
        return 'nm-pea-pon' if asCode else 'PONDEROSA'

    if '<PeakList>' in string:  # TopSpin peak list
        return 'nm-pea-top' if asCode else 'TopSpin'

    if 'peak id.' in string and 'Dim 0' in string and 'Dim 1' in string\
       and ('Amplitude' in string or 'Intensity' in string) and 'Assignment' in string:  # VNMR peak list
        return 'nm-pea-vnm' if asCode else 'VNMR'

    if '# Peak List from VNMR' in string\
       or ('Peak_Number' in string
           and (('X' in string and 'Y' in string) or ('F1' in string and 'F2' in string))
           and ('Amplitude' in string or 'Intensity' in string)):  # VNMR ll2d output
        return 'nm-pea-vnm' if asCode else 'VNMR'

    if '# PEAKLIST_VERSION' in string or '# PEAKLIST_DIMENSION' in string:  # XwinNMR peak list
        return 'nm-pea-xwi' if asCode else 'XwinNMR'

    if 'eak' in string and ('able' in string or 'nnotation' in string or 'ssign' in string)\
       and ('F1' in string or 'f1' in string) and ('F2' in string or 'f2' in string) and 'Position' not in string:
        offset = 0
        if 'mplitude' in string or 'ntensity' in string or 'eight' in string:
            offset += 1
        if 'olume' in string:
            offset += 1
        if offset > 0:
            return 'nm-pea-bar' if asCode else 'unknown'

    if ('F1' in string or 'f1' in string) and ('F2' in string or 'f2' in string) and 'Position' not in string:
        offset = 0
        if 'mplitude' in string or 'ntensity' in string or 'eight' in string:
            offset += 1
        if 'olume' in string:
            offset += 1
        if offset > 0:
            return 'nm-pea-bar' if asCode else 'unknown'

    if '1Dim' in string and '2Dim' in string and 'Intensity' in string:  # 8ep5
        return 'nm-pea-bar' if asCode else 'unknown'

    if header is None:

        if 2 <= len_col - 1 <= 4:
            try:
                if all('.' in col[idx] and CS_ERROR_MIN < float(col[idx]) < CS_ERROR_MAX for idx in range(len_col - 1)):
                    if abs(float(col[-1])) >= CS_ERROR_MAX:
                        return 'nm-pea-spa' if asCode else 'Sparky'  # header broken SPARKY
            except (ValueError, TypeError):
                pass

        if 2 <= len_col - 2 <= 4 and sparky_assignment_pattern.match(col[0]):
            try:
                if all('.' in col[idx + 1] and CS_ERROR_MIN < float(col[idx + 1]) < CS_ERROR_MAX for idx in range(len_col - 2)):
                    if abs(float(col[-1])) >= CS_ERROR_MAX:
                        return 'nm-pea-spa' if asCode else 'Sparky'  # header broken SPARKY
            except (ValueError, TypeError):
                pass

        return None

    if ' w1 ' in header and ' w2' in header\
       and len_col > 2 and ('Assignment' not in header or sparky_assignment_pattern.match(col[0])):  # Sparky
        try:
            float(col[1])
            float(col[2])
            return 'nm-pea-spa' if asCode else 'Sparky'
        except (ValueError, TypeError):
            pass

    if 'Assignment' in header and 'Shift (ppm)' in header\
       and len_col > 2 and sparky_assignment_pattern.match(col[0]):  # Sparky
        try:
            float(col[1])
            float(col[2])
            return 'nm-pea-spa' if asCode else 'Sparky'
        except (ValueError, TypeError):
            pass

    if ('Position F1' in header or 'Shift F1' in header) and ('Position F2' in header or 'Shift F2' in header)\
       and 'Assign F1' in header and 'Assign F2' in header:  # and ('Height' in header or 'Volume' in header):
        if len_col > 4 and not col[0].isdigit():
            return 'nm-pea-ccp' if asCode else 'CCPN'  # header broken CCPN

    if ('Amplitude' in header or 'Intensity' in header)\
       and 'Assignment' in header:
        if len_col > 6 and sparky_assignment_pattern.match(col[6]):  # VNMR 2D
            try:
                int(col[0])
                float(col[1])
                float(col[3])
                return 'nm-pea-vnm' if asCode else 'VNMR'
            except (ValueError, TypeError):
                pass

        elif len_col > 8 and sparky_assignment_pattern.match(col[8]):  # VNMR 3D
            try:
                int(col[0])
                float(col[1])
                float(col[3])
                float(col[5])
                return 'nm-pea-vnm' if asCode else 'VNMR'
            except (ValueError, TypeError):
                pass

        elif len_col > 10 and sparky_assignment_pattern.match(col[10]):  # VNMR 4D
            try:
                int(col[0])
                float(col[1])
                float(col[3])
                float(col[5])
                float(col[7])
                return 'nm-pea-vnm' if asCode else 'VNMR'
            except (ValueError, TypeError):
                pass

    if 'eak' in header and ('able' in header or 'nnotation' in header or 'ssign' in header)\
       and ('F1' in header or 'f1' in header) and ('F2' in header or 'f2' in header) and 'Position' not in header:
        offset = 0
        if 'mplitude' in header or 'ntensity' in header or 'eight' in header:
            offset += 1
        if 'olume' in header:
            offset += 1
        if 'F3' not in header and 'f3' not in header and 'F4' not in header and 'f4' not in header\
           and len_col > 3 + offset and sparky_assignment_pattern.match(col[3 + offset]):
            try:
                int(col[0])
                float(col[1])
                float(col[2])
                return 'nm-pea-bar' if asCode else 'unknown'
            except (ValueError, TypeError):
                pass

        elif 'F4' not in header and 'f4' not in header\
                and len_col > 4 + offset and sparky_assignment_pattern.match(col[4 + offset]):
            try:
                int(col[0])
                float(col[1])
                float(col[2])
                float(col[3])
                return 'nm-pea-bar' if asCode else 'unknown'
            except (ValueError, TypeError):
                pass

        elif len_col > 5 + offset and sparky_assignment_pattern.match(col[5 + offset]):
            try:
                int(col[0])
                float(col[1])
                float(col[2])
                float(col[3])
                float(col[4])
                return 'nm-pea-bar' if asCode else 'unknown'
            except (ValueError, TypeError):
                pass

    if ('F1' in header or 'f1' in header) and ('F2' in header or 'f2' in header) and 'Position' not in header:
        offset = 0
        if 'mplitude' in header or 'ntensity' in header or 'eight' in header:
            offset += 1
        if 'olume' in header:
            offset += 1
        if 'F3' not in header and 'f3' not in header and 'F4' not in header and 'f4' not in header and offset > 0:
            try:
                int(col[0])
                float(col[1])
                float(col[2])
                return 'nm-pea-bar' if asCode else 'unknown'
            except (ValueError, TypeError):
                pass

        elif 'F4' not in header and 'f4' not in header and offset > 0:
            try:
                int(col[0])
                float(col[1])
                float(col[2])
                float(col[3])
                return 'nm-pea-bar' if asCode else 'unknown'
            except (ValueError, TypeError):
                pass

        elif offset > 0:
            try:
                int(col[0])
                float(col[1])
                float(col[2])
                float(col[3])
                float(col[4])
                return 'nm-pea-bar' if asCode else 'unknown'
            except (ValueError, TypeError):
                pass

    if '1Dim' in header and '2Dim' in header and 'Intensity' in header:  # 8ep5
        if '3Dim' not in header and '4Dim' not in header\
           and len_col > 3:
            try:
                int(col[0])
                float(col[1])
                float(col[2])
                return 'nm-pea-bar' if asCode else 'unknown'
            except (ValueError, TypeError):
                pass

        elif '4Dim' not in header\
                and len_col > 4:
            try:
                int(col[0])
                float(col[1])
                float(col[2])
                float(col[3])
                return 'nm-pea-bar' if asCode else 'unknown'
            except (ValueError, TypeError):
                pass

        elif len_col > 5:
            try:
                int(col[0])
                float(col[1])
                float(col[2])
                float(col[3])
                float(col[4])
                return 'nm-pea-bar' if asCode else 'unknown'
            except (ValueError, TypeError):
                pass

    if 'label' in header and 'data' in header and 'dataset' not in header\
       and 'sw' in col and 'sf' in col:
        return 'nm-pea-vie' if asCode else 'NMRView'  # header broken NMRVIEW

    return None


def get_number_of_dimensions_of_peak_list(fPath: str, file_format: Optional[str]) -> Optional[int]:
    """ Return number of dimensions for a input peak list file.
    """

    if file_format is None:
        return None

    with open(fPath, 'r', encoding='utf-8') as ifh:

        has_header = False

        for idx, line in enumerate(ifh):

            if file_format == 'NMRView' and not has_header:

                if 'sw' in line and 'sf' in line:
                    has_header = True

                continue

            dimensions = get_number_of_dimensions_of_peak_list_from_string(file_format, line)

            if dimensions is not None and 0 < dimensions <= MAX_DIM_NUM_OF_SPECTRA:
                return dimensions

            if idx >= MR_MAX_SPACER_LINES:
                break

    return None


def get_number_of_dimensions_of_peak_list_from_string(file_format: str, line: str) -> Optional[int]:
    """ Return number of dimensions of peak list of given format and input.
    """

    col = re.split(r'[\s\t]+', line.strip())
    len_col = len(col)

    if file_format == 'XEASY':
        if 'Number of dimensions' in line:
            if col[-1].isdigit():
                return int(col[-1])
        if 'xeasy2D' in line:
            return 2
        if 'xeasy3D' in line:
            return 3
        if 'xeasy4D' in line:
            return 4
        if line.startswith('#CYANAFORMAT'):
            if all(a.isalpha() for a in col[1]):
                return len(col[1])

    if file_format == 'Sparky':
        if ' w1 ' in line:
            dim = [int(w[1:]) for w in col if w.startswith('w') and w[1:].isdigit()]
            if len(dim) > 0:
                return max(dim)

        if len_col > 3 and sparky_assignment_pattern.match(col[0]):
            return col[0].count('-') + 1

    if file_format == 'NMRView':
        return len_col

    if file_format == 'NMRPipe':
        if 'VARS' in line:
            if 'A_PPM' in col:
                return 4
            if 'Z_PPM' in col:
                return 3
            if 'Y_PPM' in col:
                return 2

    if file_format == 'PONDEROSA':
        if 'AXISORDER' in line:
            if all(a.isalpha() for a in col[1]):
                return len(col[1])

    if file_format == 'XwinNMR':
        if '# PEAKLIST_DIMENSION' in line:
            if '2' in col:
                return 2
            if '3' in col:
                return 3
            if '4' in col:
                return 4
        if 'F2[ppm]' in line:
            if 'F4[ppm]' in col:
                return 4
            if 'F3[ppm]' in col:
                return 3
            if 'F2[ppm]' in col:
                return 2

    if file_format == 'TopSpin':
        if '<PeakList2D>' in line:
            return 2
        if '<PeakList3D>' in line:
            return 3
        if '<PeakList4D>' in line:
            return 4

    if file_format == 'VNMR':
        if 'Dim 3' in line or 'A(ppm)' in line or 'A (ppm)' in line or 'F4' in line:
            return 4
        if 'Dim 2' in line or 'Z(ppm)' in line or 'Z (ppm)' in line or 'F3' in line:
            return 3
        if 'Dim 1' in line or 'Y(ppm)' in line or 'Y (ppm)' in line or 'F2' in line:
            return 2

        if len_col > 6 and sparky_assignment_pattern.match(col[6]):
            val = col[6]
            if 2 <= val.count('-') + 1 <= 4:
                return val.count('-')
            if 2 <= val.count(':') + 1 <= 4:
                return val.count(':')
            if 2 <= val.count(';') + 1 <= 4:
                return val.count(';')
            if 2 <= val.count(',') + 1 <= 4:
                return val.count(',')

        if len_col > 8 and sparky_assignment_pattern.match(col[8]):
            val = col[8]
            if 2 <= val.count('-') + 1 <= 4:
                return val.count('-')
            if 2 <= val.count(':') + 1 <= 4:
                return val.count(':')
            if 2 <= val.count(';') + 1 <= 4:
                return val.count(';')
            if 2 <= val.count(',') + 1 <= 4:
                return val.count(',')

        if len_col > 10 and sparky_assignment_pattern.match(col[10]):
            val = col[10]
            if 2 <= val.count('-') + 1 <= 4:
                return val.count('-')
            if 2 <= val.count(':') + 1 <= 4:
                return val.count(':')
            if 2 <= val.count(';') + 1 <= 4:
                return val.count(';')
            if 2 <= val.count(',') + 1 <= 4:
                return val.count(',')

    if file_format == 'unknown':
        if 'F4' in line or 'f4' in line or '4Dim' in line:
            return 4
        if 'F3' in line or 'f3' in line or '3Dim' in line:
            return 3
        if 'F2' in line or 'f2' in line or '2Dim' in line:
            return 2

    return None


class PdbMrSplitter:
    """ Wrapper class for public PDB-MR format file splitter.
    """
    __slots__ = ('__class_name__',
                 '__version__',
                 '__verbose',
                 '__debug',
                 '__lfh',
                 '__remediation_mode',
                 '__mr_content_subtypes',
                 '__inputParamDict',
                 '__file_path_list_len',
                 '__sll_pred_holder',
                 '__divide_mr_error_message',
                 '__peel_mr_error_message',
                 '__suspended_errors_for_lazy_eval',
                 'report',
                 '__public_mr_has_valid_star_restraint',
                 '__has_legacy_sf_issue',
                 '__cur_original_ar_file_name',
                 '__mr_atom_name_mapping',
                 '__ccU',
                 '__csStat',
                 '__c2S',
                 '__nefT')

    def __init__(self, verbose: bool, debug: bool, log: IO,
                 remediationMode: bool, mrContentSubtypes: List[str],
                 filePathListIdLen: int, inputParamDict: dict, sslPredHolder: dict,
                 divideMrErrorMessage: List[str], peelMrErrorMessage: List[str],
                 suspendedErrorsForLazyEval: List[dict],
                 report: NmrDpReport,
                 ccU: Optional[ChemCompUtil] = None, csStat: Optional[BMRBChemShiftStat] = None,
                 c2S: Optional[CifToNmrStar] = None, nefT: Optional[NEFTranslator] = None):
        self.__class_name__ = self.__class__.__name__
        self.__version__ = __version__

        self.__verbose = verbose
        self.__debug = debug
        self.__lfh = log

        # whether to enable remediation routines
        self.__remediation_mode = remediationMode

        # supported content subtypes of restraint
        self.__mr_content_subtypes = mrContentSubtypes

        # atypical restraint file id begins with
        self.__file_path_list_len = filePathListIdLen

        # auxiliary input resource
        self.__inputParamDict = inputParamDict

        # ANTLR4 SLL prediction mode holder for performance
        self.__sll_pred_holder = sslPredHolder

        # error messages holder
        self.__divide_mr_error_message = divideMrErrorMessage
        self.__peel_mr_error_message = peelMrErrorMessage

        # suspended error items for lazy evaluation
        self.__suspended_errors_for_lazy_eval = suspendedErrorsForLazyEval

        # NmrDpReport
        self.report = report

        # whether public MR file contains valid NMR-STAR restraints (used only for NMR data remediation)
        self.__public_mr_has_valid_star_restraint = False

        # whether sf_framecode has to be fixed
        self.__has_legacy_sf_issue = False

        # original file name of atypical restraint file
        self.__cur_original_ar_file_name = None

        # atom name mapping of public MR file between the coordinates and submitted file
        self.__mr_atom_name_mapping = None

        # CCD accessing utility
        self.__ccU = ChemCompUtil(verbose, log) if ccU is None else ccU

        # BMRB chemical shift statistics
        self.__csStat = BMRBChemShiftStat(verbose, log, self.__ccU) if csStat is None else csStat

        # CifToNmrStar
        self.__c2S = CifToNmrStar(log) if c2S is None else c2S

        # NEFTranslator
        self.__nefT = NEFTranslator(verbose, log, self.__ccU, self.__csStat) if nefT is None else nefT
        if nefT is None:
            self.__nefT.set_remediation_mode(True)

    @property
    def sll_pred_holder(self):
        return self.__sll_pred_holder

    @property
    def divide_mr_error_message(self):
        return self.__divide_mr_error_message

    @property
    def peel_mr_error_message(self):
        return self.__peel_mr_error_message

    @property
    def suspended_errors_for_lazy_eval(self):
        return self.__suspended_errors_for_lazy_eval

    @property
    def public_mr_has_valid_star_restraint(self):
        return self.__public_mr_has_valid_star_restraint

    @property
    def has_legacy_sf_issue(self):
        return self.__has_legacy_sf_issue

    @property
    def cur_original_ar_file_name(self):
        return self.__cur_original_ar_file_name

    @cur_original_ar_file_name.setter
    def cur_original_ar_file_name(self, cur_original_ar_file_name: str):
        self.__cur_original_ar_file_name = cur_original_ar_file_name

    @property
    def mr_atom_name_mapping(self):
        return self.__mr_atom_name_mapping

    def extractPublicMrFileIntoLegacyMr(self) -> bool:
        """ Extract/split public PDB-MR file into legacy restraint files for NMR restraint remediation.
        """

        ar_file_path_list = 'atypical_restraint_file_path_list'

        fileListId = self.__file_path_list_len

        dir_path = mr_file_name = '.'
        split_file_list, peak_file_list = [], []

        self.__mr_atom_name_mapping = []

        remediated = aborted = False
        src_basename = mr_core_path = mr_file_path = mr_file_link = None
        mr_part_paths, pk_list_paths = [], []

        settled_file_types = list(parsable_mr_file_types)
        settled_file_types.extend(list(parsable_pk_file_types))
        settled_file_types.append('nm-res-sax')

        for ar in self.__inputParamDict[ar_file_path_list]:
            src_file = ar['file_name']

            input_source = self.report.input_sources[fileListId]
            input_source_dic = input_source.get()

            file_name = input_source_dic['file_name']
            file_type = input_source_dic['file_type']

            fileListId += 1

            if ar['file_type'] == 'nm-aux-pdb':
                continue

            if file_type != 'nm-res-mr':

                if file_type in linear_mr_file_types:
                    with open(src_file, 'r', errors='ignore') as ifh:
                        for line in ifh:
                            if 'Submitted Coord H atom name' in line:
                                input_source.setItemValue('file_type', 'nm-res-mr')
                                return self.extractPublicMrFileIntoLegacyMr()

                continue

            original_file_name = None
            if 'original_file_name' in input_source_dic:
                if input_source_dic['original_file_name'] is not None:
                    original_file_name = os.path.basename(input_source_dic['original_file_name'])
                if file_name != original_file_name and original_file_name is not None:
                    file_name = f"{original_file_name} ({file_name})"

            mr_file_name = file_name

            self.__cur_original_ar_file_name = original_file_name

            if is_binary_file(src_file) or is_eps_or_pdf_file(src_file):

                if not src_file.endswith('.gz'):

                    err = f"The restraint file {src_file!r} (MR format) is neither ASCII file nor gzip compressed file."

                    self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.split() ++ Error  - " + err)
                    self.report.setError()

                    if self.__verbose:
                        self.__lfh.write(f"+{self.__class_name__}.split() ++ Error  - {err}\n")

                    return False

                dst_file = os.path.splitext(src_file)[0]

                if not os.path.exists(dst_file):

                    try:

                        uncompress_gzip_file(src_file, dst_file)

                    except Exception as e:

                        self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.split() ++ Error  - " + str(e))
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write(f"+{self.__class_name__}.split() ++ Error  - {str(e)}\n")

                        return False

                src_file = dst_file

            dir_path = os.path.dirname(src_file)

            _div_file_names = {div_file_name: len(div_file_name) + (0 if div_file_name.endswith('-div_src.mr') else (1 if div_file_name.endswith('-div_ext.mr') else 2))
                               for div_file_name in os.listdir(dir_path)
                               if os.path.isfile(os.path.join(dir_path, div_file_name))
                               and (div_file_name.endswith('-div_src.mr')
                                    or div_file_name.endswith('-div_dst.mr')
                                    or div_file_name.endswith('-div_ext.mr'))}

            div_file_names = [k for k, v in sorted(_div_file_names.items(), key=itemgetter(1))]

            src_basename = os.path.splitext(src_file)[0]
            ar['original_file_name'] = src_basename + '.mr'

            dst_file = src_basename + '-trimmed.mr'
            header_file = src_basename + '-header.mr'
            footer_file = src_basename + '-footer.mr'
            cor_dst_file = src_basename + '-corrected.mr'
            cor_str_file = src_basename + '-corrected.str'
            ign_dst_file = src_basename + '-ignored.mr'

            if os.path.exists(ign_dst_file):  # in case the MR file can be ignored
                continue

            ign_pk_file = src_basename + '-ignored-as-pea-any.mr'

            if os.path.exists(ign_pk_file):  # in case the MR file can be ignored as peak list file

                settled_file_type, _ = self.__getPeakListFileTypeAndContentSubtype(ign_pk_file)

                _ar = ar.copy()

                if settled_file_type is not None:
                    sel_pk_file = src_basename + f'-selected-as-{settled_file_type[-7:]}.mr'
                    os.rename(ign_pk_file, sel_pk_file)

                    _ar['file_name'] = sel_pk_file
                    _ar['file_type'] = settled_file_type

                else:

                    _ar['file_name'] = ign_pk_file
                    _ar['file_type'] = 'nm-pea-any'

                peak_file_list.append(_ar)

                pk_list_paths.append({'nmr-peaks': src_basename + '.mr'})

                touch_file = os.path.join(dir_path, '.entry_with_pk')
                if not os.path.exists(touch_file):
                    with open(touch_file, 'w') as ofh:
                        ofh.write('')

                continue

            designated = False

            for _file_type in settled_file_types:

                sel_file = src_basename + f'-selected-as-{_file_type[-7:]}.mr'

                if os.path.exists(sel_file):
                    _ar = ar.copy()

                    _ar['file_name'] = sel_file
                    _ar['file_type'] = _file_type
                    split_file_list.append(_ar)

                    designated = True

                    break

            if designated:
                continue

            if mr_file_path is None:

                rem_dir = os.path.join(dir_path, 'remediation')

                try:

                    if not os.path.isdir(rem_dir):
                        os.makedirs(rem_dir)

                except OSError:
                    pass

                mr_file_path = src_basename + '-remediated.mr'
                mr_file_link = os.path.join(rem_dir, os.path.basename(src_basename) + '.mr')

                mr_part_paths.append({'header': header_file})
                mr_part_paths.append({'footer': footer_file})

            has_mr_header = has_pdb_format = has_cif_format = has_str_format = has_cs_str = False

            try:

                header = True
                in_header = pdb_record = footer =\
                    has_datablock = has_anonymous_saveframe = has_save = has_loop = has_stop = False

                first_str_line_num = last_str_line_num = -1

                i = 0

                with open(src_file, 'r') as ifh, \
                        open(dst_file, 'w') as ofh, \
                        open(header_file, 'w') as hofh, \
                        open(footer_file, 'w') as fofh:
                    for line in ifh:
                        i += 1

                        # skip MR header
                        if header:
                            if line.startswith('*'):
                                hofh.write(line)
                                continue
                            if startsWithPdbRecord(line):
                                continue
                            header = False

                        if not footer:
                            if line.startswith('*') and startsWithPdbRecord(line[1:]):
                                hofh.write(line)
                                in_header = True
                                continue

                            if in_header and line.startswith('*END'):
                                hofh.write(line)
                                in_header = False
                                continue

                        if mr_file_header_pattern.match(line)\
                           or sel_mr_file_header_pattern.match(line)\
                           or sel_pk_file_header_pattern.match(line)\
                           or sel_cs_file_header_pattern.match(line):
                            has_mr_header = True

                        # skip legacy PDB
                        if startsWithPdbRecord(line):
                            has_pdb_format = pdb_record = True
                            continue
                        if pdb_record:
                            pdb_record = False
                            if line.startswith('END'):
                                continue

                        # check STAR
                        str_syntax = False
                        if datablock_pattern.match(line):
                            str_syntax = has_datablock = True
                        elif sf_anonymous_pattern.match(line):
                            str_syntax = has_anonymous_saveframe = True
                        elif save_pattern.match(line):
                            str_syntax = has_save = True
                        elif loop_pattern.match(line):
                            str_syntax = has_loop = True
                        elif stop_pattern.match(line):
                            str_syntax = has_stop = True

                        if str_syntax:
                            if first_str_line_num < 0:
                                first_str_line_num = i
                            last_str_line_num = i
                            if (has_anonymous_saveframe and has_save) or (has_loop and has_stop):
                                has_str_format = True
                            elif has_datablock and has_loop and not has_stop:
                                has_cif_format = True

                        # skip MR footer
                        if 'Submitted Coord H atom name' in line:
                            fofh.write(line)
                            footer = True
                            continue

                        if footer:
                            fofh.write(line)
                            col = line.split()
                            len_col = len(col)
                            if len_col == 10:
                                original_comp_id = col[5].upper()
                                if original_comp_id not in monDict3:  # extract non-standard residues
                                    try:
                                        atom_map = {'auth_atom_id': col[1],
                                                    'auth_comp_id': col[2],
                                                    'auth_seq_id': int(col[3]),
                                                    'original_atom_id': col[4].upper(),
                                                    'original_comp_id': original_comp_id,
                                                    'original_seq_id': int(col[6])}
                                        if atom_map not in self.__mr_atom_name_mapping:
                                            self.__mr_atom_name_mapping.append(atom_map)
                                    except ValueError:
                                        pass
                            elif len_col >= 8:  # 2liw 4 digits residue number

                                def split_concat_comp_id_seq_id(string):
                                    if not string[-1].isdigit():
                                        return None, None
                                    idx = len(string) - 1
                                    while idx >= 0 and string[idx].isdigit():
                                        idx -= 1
                                    if idx == 0:
                                        return None, None
                                    if string[idx] != '-':
                                        idx += 1
                                    return string[:idx], int(string[idx:])

                                if len(col[2]) > 4:
                                    auth_comp_id, auth_seq_id = split_concat_comp_id_seq_id(col[2])

                                    if len(col[4]) > 4 and len_col == 8:
                                        orig_comp_id, orig_seq_id = split_concat_comp_id_seq_id(col[4])
                                        if auth_comp_id is not None and orig_comp_id is not None and orig_comp_id.upper() not in monDict3:
                                            atom_map = {'auth_atom_id': col[1],
                                                        'auth_comp_id': auth_comp_id,
                                                        'auth_seq_id': auth_seq_id,
                                                        'original_atom_id': col[3].upper(),
                                                        'original_comp_id': orig_comp_id.upper(),
                                                        'original_seq_id': orig_seq_id}
                                            if atom_map not in self.__mr_atom_name_mapping:
                                                self.__mr_atom_name_mapping.append(atom_map)
                                    elif len_col == 9:
                                        if auth_comp_id is not None and col[4] not in monDict3:
                                            try:
                                                atom_map = {'auth_atom_id': col[1],
                                                            'auth_comp_id': auth_comp_id,
                                                            'auth_seq_id': auth_seq_id,
                                                            'original_atom_id': col[3].upper(),
                                                            'original_comp_id': col[4].upper(),
                                                            'original_seq_id': int(col[5])}
                                                if atom_map not in self.__mr_atom_name_mapping:
                                                    self.__mr_atom_name_mapping.append(atom_map)
                                            except ValueError:
                                                pass
                                elif len(col[5]) > 4 and len_col == 9:
                                    orig_comp_id, orig_seq_id = split_concat_comp_id_seq_id(col[5])
                                    if orig_comp_id is not None and orig_comp_id.upper() not in monDict3:
                                        try:
                                            atom_map = {'auth_atom_id': col[1],
                                                        'auth_comp_id': col[2],
                                                        'auth_seq_id': int(col[3]),
                                                        'original_atom_id': col[4].upper(),
                                                        'original_comp_id': orig_comp_id.upper(),
                                                        'original_seq_id': orig_seq_id}
                                            if atom_map not in self.__mr_atom_name_mapping:
                                                self.__mr_atom_name_mapping.append(atom_map)
                                        except ValueError:
                                            pass

                        else:
                            ofh.write(line)

                if last_str_line_num - first_str_line_num < 10:
                    has_str_format = has_cif_format = False

                # split STAR and others
                if has_str_format and not has_mr_header:

                    remediated = True

                    mrPath = os.path.splitext(src_file)[0] + '-ignored.str'

                    if not os.path.exists(mrPath):
                        mrPath = os.path.splitext(src_file)[0] + '-trimmed.str'

                        header = True
                        in_header = pdb_record = False

                        i = 0

                        with open(src_file, 'r') as ifh, \
                                open(dst_file, 'w') as ofh, \
                                open(mrPath, 'w') as ofh2:
                            for line in ifh:
                                i += 1

                                # skip MR header
                                if header:
                                    if line.startswith('*'):
                                        continue
                                    header = False

                                if line.startswith('*') and startsWithPdbRecord(line[1:]):
                                    in_header = True
                                    continue

                                if in_header and line.startswith('*END'):
                                    in_header = False
                                    continue

                                # skip legacy PDB
                                if has_pdb_format:
                                    if startsWithPdbRecord(line):
                                        pdb_record = True
                                        continue
                                    if pdb_record:
                                        pdb_record = False
                                        if line.startswith('END'):
                                            continue

                                if first_str_line_num <= i <= last_str_line_num:
                                    ofh2.write(line)
                                    continue

                                # skip MR footer
                                if 'Submitted Coord H atom name' in line:
                                    break

                                ofh.write(line)

                        _mrPath = os.path.splitext(src_file)[0] + '-corrected.str'

                        if os.path.exists(_mrPath):  # in case manually corrected NMR-STAR file exists
                            mrPath = _mrPath

                        mr_file_path_list = 'restraint_file_path_list'

                        if mr_file_path_list not in self.__inputParamDict:
                            self.__inputParamDict[mr_file_path_list] = [mrPath]
                        else:
                            self.__inputParamDict[mr_file_path_list].append(mrPath)

                        insert_index = self.__file_path_list_len

                        if insert_index > len(self.__star_data):
                            self.__star_data.append(None)
                            self.__star_data_type.append(None)

                        self.report.insertInputSource(insert_index)

                        self.__file_path_list_len += 1

                        input_source = self.report.input_sources[insert_index]

                        file_type = 'nmr-star'
                        file_name = os.path.basename(mrPath)

                        input_source.setItemValue('file_name', file_name)
                        input_source.setItemValue('file_type', file_type)
                        input_source.setItemValue('content_type', 'nmr-restraints')

                        codec = detect_bom(mrPath, 'utf-8')

                        _mrPath = None

                        if codec != 'utf-8':
                            _mrPath = mrPath + '~'
                            convert_codec(mrPath, _mrPath, codec, 'utf-8')
                            mrPath = _mrPath

                        if is_rtf_file(mrPath):
                            _mrPath = mrPath + '.rtf2txt'
                            convert_rtf_to_ascii(mrPath, _mrPath)
                            mrPath = _mrPath

                        file_subtype = 'O'

                        is_valid, message = self.__nefT.validate_file(mrPath, file_subtype)

                        if not is_valid or not self.__has_star_chem_shift:
                            _is_valid, _ = self.__nefT.validate_file(mrPath, 'S')
                            if _is_valid:
                                has_cs_str = True

                        self.__original_error_message.append(message)

                        _file_type = message['file_type']  # nef/nmr-star/unknown

                        if is_valid:

                            if _file_type != file_type:

                                err = f"{file_name!r} was selected as {self.readable_file_type[file_type]} file, "\
                                    f"but recognized as {self.readable_file_type[_file_type]} file."
                                # DAOTHER-5673
                                err += " Please re-upload the NEF file as an NMR unified data file." if _file_type == 'nef' else " Please re-upload the file."

                                if len(message['error']) > 0:
                                    for err_message in message['error']:
                                        if 'No such file or directory' not in err_message:
                                            err += ' ' + re.sub('not in list', 'unknown item.', err_message)

                                self.report.error.appendDescription('content_mismatch',
                                                                    {'file_name': file_name, 'description': err})
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write(f"+{self.__class_name__}.split() ++ Error  - {err}\n")

                            else:

                                # NEFTranslator.validate_file() generates this object internally, but not re-used.
                                _is_done, star_data_type, star_data = self.__nefT.read_input_file(mrPath)

                                self.__has_legacy_sf_issue = False

                                if star_data_type == 'Saveframe':
                                    self.__has_legacy_sf_issue = True
                                    self.__fixFormatIssueOfInputSource(insert_index, file_name, file_type, mrPath, file_subtype, message)
                                    _is_done, star_data_type, star_data = self.__nefT.read_input_file(mrPath)

                                if not (self.__has_legacy_sf_issue and _is_done and star_data_type == 'Entry'):

                                    if len(self.__star_data_type) == self.__file_path_list_len:
                                        del self.__star_data_type[-1]
                                        del self.__star_data[-1]

                                    self.__star_data_type.append(star_data_type)
                                    self.__star_data.append(star_data)

                                    self.__rescueFormerNef(insert_index)
                                    self.__rescueImmatureStr(insert_index)

                                if _is_done:
                                    self.__detectContentSubType__(insert_index, input_source, dir_path)
                                    input_source_dic = input_source.get()
                                    if 'content_subtype' in input_source_dic:
                                        content_subtype = input_source_dic['content_subtype']
                                        if any(True for mr_content_subtype in self.__mr_content_subtypes if mr_content_subtype in content_subtype):
                                            self.__public_mr_has_valid_star_restraint = True
                                            mr_part_paths.append({'nmr-star': mrPath})

                        elif not self.__fixFormatIssueOfInputSource(insert_index, file_name, file_type, mrPath, file_subtype, message):
                            pass

                        if _mrPath is not None:
                            try:
                                os.remove(_mrPath)
                            except OSError:
                                pass

                elif has_cif_format and not has_mr_header:

                    remediated = True

                    mrPath = os.path.splitext(src_file)[0] + '-ignored.cif'

                    if not os.path.exists(mrPath):
                        mrPath = os.path.splitext(src_file)[0] + '-trimmed.cif'

                        header = True
                        in_header = pdb_record = has_sharp = False

                        i = 0

                        with open(src_file, 'r') as ifh, \
                                open(dst_file, 'w') as ofh, \
                                open(mrPath, 'w') as ofh2:
                            for line in ifh:
                                i += 1

                                # skip MR header
                                if header:
                                    if line.startswith('*'):
                                        continue
                                    header = False

                                if line.startswith('*') and startsWithPdbRecord(line[1:]):
                                    in_header = True
                                    continue

                                if in_header and line.startswith('*END'):
                                    in_header = False
                                    continue

                                if first_str_line_num <= i and not has_sharp:
                                    if i <= last_str_line_num:
                                        ofh2.write(line)
                                        continue
                                    ofh2.write(line)
                                    if line.startswith('#'):
                                        has_sharp = True
                                    continue

                                # skip legacy PDB
                                if has_pdb_format:
                                    if startsWithPdbRecord(line):
                                        pdb_record = True
                                        continue
                                    if pdb_record:
                                        pdb_record = False
                                        if line.startswith('END'):
                                            continue

                                # skip MR footer
                                if 'Submitted Coord H atom name' in line:
                                    break

                                ofh.write(line)

                        _mrPath = os.path.splitext(mrPath)[0] + '.cif2str'
                        if not self.__c2S.convert(mrPath, _mrPath):
                            _mrPath = mrPath

                        mrPath = _mrPath

                        mr_file_path_list = 'restraint_file_path_list'

                        if mr_file_path_list not in self.__inputParamDict:
                            self.__inputParamDict[mr_file_path_list] = [mrPath]
                        else:
                            self.__inputParamDict[mr_file_path_list].append(mrPath)

                        insert_index = self.__file_path_list_len

                        if insert_index > len(self.__star_data):
                            self.__star_data.append(None)
                            self.__star_data_type.append(None)

                        self.report.insertInputSource(insert_index)

                        self.__file_path_list_len += 1

                        input_source = self.report.input_sources[insert_index]

                        file_type = 'nmr-star'
                        file_name = os.path.basename(mrPath)

                        input_source.setItemValue('file_name', re.sub(r'\.cif2str$', '', file_name))
                        input_source.setItemValue('file_type', file_type)
                        input_source.setItemValue('content_type', 'nmr-restraints')

                        codec = detect_bom(mrPath, 'utf-8')

                        _mrPath = None

                        if codec != 'utf-8':
                            _mrPath = mrPath + '~'
                            convert_codec(mrPath, _mrPath, codec, 'utf-8')
                            mrPath = _mrPath

                        if is_rtf_file(mrPath):
                            _mrPath = mrPath + '.rtf2txt'
                            convert_rtf_to_ascii(mrPath, _mrPath)
                            mrPath = _mrPath

                        file_subtype = 'O'

                        is_valid, message = self.__nefT.validate_file(mrPath, file_subtype)

                        if not is_valid or not self.__has_star_chem_shift:
                            _is_valid, _ = self.__nefT.validate_file(mrPath, 'S')
                            if _is_valid:
                                has_cs_str = True

                        self.__original_error_message.append(message)

                        _file_type = message['file_type']  # nef/nmr-star/unknown

                        if is_valid:

                            if _file_type != file_type:

                                err = f"{file_name!r} was selected as {self.readable_file_type[file_type]} file, "\
                                    f"but recognized as {self.readable_file_type[_file_type]} file."
                                # DAOTHER-5673
                                err += " Please re-upload the NEF file as an NMR unified data file." if _file_type == 'nef' else " Please re-upload the file."

                                if len(message['error']) > 0:
                                    for err_message in message['error']:
                                        if 'No such file or directory' not in err_message:
                                            err += ' ' + re.sub('not in list', 'unknown item.', err_message)

                                self.report.error.appendDescription('content_mismatch',
                                                                    {'file_name': file_name, 'description': err})
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write(f"+{self.__class_name__}.split() ++ Error  - {err}\n")

                            else:

                                # NEFTranslator.validate_file() generates this object internally, but not re-used.
                                _is_done, star_data_type, star_data = self.__nefT.read_input_file(mrPath)

                                self.__has_legacy_sf_issue = False

                                if star_data_type == 'Saveframe':
                                    self.__has_legacy_sf_issue = True
                                    self.__fixFormatIssueOfInputSource(insert_index, file_name, file_type, mrPath, file_subtype, message)
                                    _is_done, star_data_type, star_data = self.__nefT.read_input_file(mrPath)

                                if not (self.__has_legacy_sf_issue and _is_done and star_data_type == 'Entry'):

                                    if len(self.__star_data_type) == self.__file_path_list_len:
                                        del self.__star_data_type[-1]
                                        del self.__star_data[-1]

                                    self.__star_data_type.append(star_data_type)
                                    self.__star_data.append(star_data)

                                    self.__rescueFormerNef(insert_index)
                                    self.__rescueImmatureStr(insert_index)

                                if _is_done:
                                    self.__detectContentSubType__(insert_index, input_source, dir_path)
                                    input_source_dic = input_source.get()
                                    if 'content_subtype' in input_source_dic:
                                        content_subtype = input_source_dic['content_subtype']
                                        if any(True for mr_content_subtype in self.__mr_content_subtypes if mr_content_subtype in content_subtype):
                                            self.__public_mr_has_valid_star_restraint = True
                                            mr_part_paths.append({'nmr-star': mrPath})

                        elif not self.__fixFormatIssueOfInputSource(insert_index, file_name, file_type, mrPath, file_subtype, message):
                            pass

                        if _mrPath is not None:
                            try:
                                os.remove(_mrPath)
                            except OSError:
                                pass

            except Exception as e:

                self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.split() ++ Error  - " + str(e))
                self.report.setError()

                if self.__verbose:
                    self.__lfh.write(f"+{self.__class_name__}.split() ++ Error  - {str(e)}\n")

                return False

            has_content = False
            with open(dst_file, 'r') as ifh:
                for line in ifh:
                    if line.isspace() or comment_pattern.match(line):
                        continue
                    has_content = True
                    break

            if not has_content:
                if not self.__public_mr_has_valid_star_restraint:
                    with open(os.path.join(dir_path, '.entry_without_mr'), 'w') as ofh:
                        ofh.write('')

                    remediated = False

                    continue

            if os.path.exists(cor_str_file) and os.path.exists(cor_dst_file) and has_content:
                mrPath = cor_str_file

                mr_file_path_list = 'restraint_file_path_list'

                item = {'file_name': mrPath,
                        'file_type': 'nmr-star',
                        'original_file_name': os.path.basename(src_basename) + '.mr'}

                if mr_file_path_list not in self.__inputParamDict:
                    self.__inputParamDict[mr_file_path_list] = [item]
                else:
                    self.__inputParamDict[mr_file_path_list].append(item)

                insert_index = self.__file_path_list_len

                if insert_index > len(self.__star_data):
                    self.__star_data.append(None)
                    self.__star_data_type.append(None)

                self.report.insertInputSource(insert_index)

                self.__file_path_list_len += 1

                input_source = self.report.input_sources[insert_index]

                file_type = 'nmr-star'
                file_name = os.path.basename(mrPath)

                input_source.setItemValue('file_name', file_name)
                input_source.setItemValue('file_type', file_type)
                input_source.setItemValue('content_type', 'nmr-restraints')
                input_source.setItemValue('original_file_name', os.path.basename(src_basename) + '.mr')

                codec = detect_bom(mrPath, 'utf-8')

                _mrPath = None

                if codec != 'utf-8':
                    _mrPath = mrPath + '~'
                    convert_codec(mrPath, _mrPath, codec, 'utf-8')
                    mrPath = _mrPath

                if is_rtf_file(mrPath):
                    _mrPath = mrPath + '.rtf2txt'
                    convert_rtf_to_ascii(mrPath, _mrPath)
                    mrPath = _mrPath

                file_subtype = 'O'

                is_valid, message = self.__nefT.validate_file(mrPath, file_subtype)

                if not is_valid or not self.__has_star_chem_shift:
                    _is_valid, _ = self.__nefT.validate_file(mrPath, 'S')
                    if _is_valid:
                        has_cs_str = True

                self.__original_error_message.append(message)

                _file_type = message['file_type']  # nef/nmr-star/unknown

                if is_valid:

                    if _file_type != file_type:

                        err = f"{file_name!r} was selected as {self.readable_file_type[file_type]} file, "\
                            f"but recognized as {self.readable_file_type[_file_type]} file."
                        # DAOTHER-5673
                        err += " Please re-upload the NEF file as an NMR unified data file." if _file_type == 'nef' else " Please re-upload the file."

                        if len(message['error']) > 0:
                            for err_message in message['error']:
                                if 'No such file or directory' not in err_message:
                                    err += ' ' + re.sub('not in list', 'unknown item.', err_message)

                        self.report.error.appendDescription('content_mismatch',
                                                            {'file_name': file_name, 'description': err})
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write(f"+{self.__class_name__}.split() ++ Error  - {err}\n")

                    else:

                        # NEFTranslator.validate_file() generates this object internally, but not re-used.
                        _is_done, star_data_type, star_data = self.__nefT.read_input_file(mrPath)

                        self.__has_legacy_sf_issue = False

                        if star_data_type == 'Saveframe':
                            self.__has_legacy_sf_issue = True
                            self.__fixFormatIssueOfInputSource(insert_index, file_name, file_type, mrPath, file_subtype, message)
                            _is_done, star_data_type, star_data = self.__nefT.read_input_file(mrPath)

                        if not (self.__has_legacy_sf_issue and _is_done and star_data_type == 'Entry'):

                            if len(self.__star_data_type) == self.__file_path_list_len:
                                del self.__star_data_type[-1]
                                del self.__star_data[-1]

                            self.__star_data_type.append(star_data_type)
                            self.__star_data.append(star_data)

                            self.__rescueFormerNef(insert_index)
                            self.__rescueImmatureStr(insert_index)

                        if _is_done:
                            self.__detectContentSubType__(insert_index, input_source, dir_path)
                            input_source_dic = input_source.get()
                            if 'content_subtype' in input_source_dic:
                                content_subtype = input_source_dic['content_subtype']
                                if any(True for mr_content_subtype in self.__mr_content_subtypes if mr_content_subtype in content_subtype):
                                    self.__public_mr_has_valid_star_restraint = True
                                    mr_part_paths.append({'nmr-star': mrPath})

                elif not self.__fixFormatIssueOfInputSource(insert_index, file_name, file_type, mrPath, file_subtype, message):
                    pass

                if _mrPath is not None:
                    try:
                        os.remove(_mrPath)
                    except OSError:
                        pass

            if os.path.exists(cor_dst_file):  # in case manually corrected MR file exists
                dst_file = cor_dst_file

                with open(dst_file, 'r') as ifh:
                    for line in ifh:
                        if line.isspace() or comment_pattern.match(line):
                            continue
                        has_content = True
                        break

                remediated = True

            if not has_content:
                continue

            mr_core_path = dst_file

            # has no MR haeder
            if not has_mr_header:

                dst_name_prefix = os.path.splitext(os.path.basename(dst_file))[0]
                dst_file_list = [os.path.join(dir_path, div_name) for div_name in div_file_names if div_name.startswith(dst_name_prefix)]

                if (not file_name.endswith('str') or mr_file_path.endswith('-remediated.mr')) and len(dst_file_list) == 0:
                    dst_file_list.append(dst_file)

                for dst_file in dst_file_list:

                    if dst_file.endswith('-div_ext.mr'):

                        ign_dst_file = dst_file + '-ignored'

                        if os.path.exists(ign_dst_file):  # in case the MR file can be ignored
                            remediated = True
                            continue

                        ign_pk_file = dst_file + '-ignored-as-pea-any'

                        if os.path.exists(ign_pk_file):  # in case the MR file can be ignored as peak list file

                            settled_file_type, _ = self.__getPeakListFileTypeAndContentSubtype(ign_pk_file)

                            _ar = ar.copy()

                            if settled_file_type is not None:
                                sel_pk_file = dst_file + f'-selected-as-{settled_file_type[-7:]}'
                                os.rename(ign_pk_file, sel_pk_file)

                                _ar['file_name'] = dst_file
                                _ar['file_type'] = settled_file_type

                            else:

                                _ar['file_name'] = dst_file
                                _ar['file_type'] = 'nm-pea-any'

                            peak_file_list.append(_ar)

                            pk_list_paths.append({'nmr-peaks': dst_file})

                            remediated = True

                            continue

                        designated = False

                        for _file_type in settled_file_types:

                            sel_file = dst_file + f'-selected-as-{_file_type[-7:]}'

                            if os.path.exists(sel_file):
                                _ar = ar.copy()

                                _ar['file_name'] = dst_file
                                _ar['file_type'] = _file_type
                                split_file_list.append(_ar)

                                mr_part_paths.append({_file_type: dst_file})

                                designated = True

                                break

                        if designated:
                            continue

                        _ar = ar.copy()

                        _ar['file_name'] = dst_file
                        _ar['file_type'] = 'nm-res-oth'
                        split_file_list.append(_ar)

                        mr_part_paths.append({_ar['file_type']: dst_file})

                        continue

                    if dst_file.endswith('-div_dst.mr'):

                        ign_dst_file = dst_file + '-ignored'

                        if os.path.exists(ign_dst_file):  # in case the MR file can be ignored
                            remediated = True
                            continue

                        ign_pk_file = dst_file + '-ignored-as-pea-any'

                        if os.path.exists(ign_pk_file):  # in case the MR file can be ignored as peak list file

                            settled_file_type, _ = self.__getPeakListFileTypeAndContentSubtype(ign_pk_file)

                            _ar = ar.copy()

                            if settled_file_type is not None:
                                sel_pk_file = dst_file + f'-selected-as-{settled_file_type[-7:]}'
                                os.rename(ign_pk_file, sel_pk_file)

                                _ar['file_name'] = dst_file
                                _ar['file_type'] = settled_file_type

                            else:

                                _ar['file_name'] = dst_file
                                _ar['file_type'] = 'nm-pea-any'

                            peak_file_list.append(_ar)

                            pk_list_paths.append({'nmr-peaks': dst_file})

                            remediated = True

                            continue

                        settled_pk_file = False

                        _ar = ar.copy()

                        for settled_file_type in parsable_pk_file_types:

                            sel_pk_file = dst_file + f'-selected-as-{settled_file_type[-7:]}'

                            if os.path.exists(sel_pk_file):

                                ign_dst_file = sel_pk_file + '-ignored'

                                if os.path.exists(ign_dst_file):
                                    continue

                                __ar = _ar.copy()

                                __ar['file_name'] = sel_pk_file
                                __ar['file_type'] = settled_file_type

                                if __ar in peak_file_list:
                                    continue

                                peak_file_list.append(__ar)

                                pk_list_paths.append({'nmr-peaks': dst_file})

                                settled_pk_file = remediated = True

                        if settled_pk_file:
                            continue

                    _, _, valid_types, possible_types = self.detectOtherPossibleFormatAsErrorOfLegacyMr(dst_file, file_name, 'nm-res-mr', [], True)

                    len_valid_types = len(valid_types)
                    len_possible_types = len(possible_types)

                    if self.__debug:
                        self.__lfh.write(f'{valid_types} {possible_types}\n')

                    if len_valid_types == 0 and len_possible_types == 0:

                        ins_msg = ''
                        if has_pdb_format and has_cs_str:
                            ins_msg = 'unexpectedly contains PDB coordinates and assigned chemical shifts, but '
                        elif has_pdb_format:
                            ins_msg = 'unexpectedly contains PDB coordinates, but '
                        elif has_cs_str:
                            ins_msg = 'unexpectedly contains assigned chemical shifts, but '

                        _file_name = os.path.basename(dst_file)
                        if file_name != _file_name:
                            _file_name = f'({_file_name}) '
                        else:
                            _file_name = ''

                        err = f"The restraint file {file_name!r} {_file_name}{ins_msg}does not match with any known restraint format. "\
                            "@todo: It needs to be reviewed or marked as entry without restraints."

                        self.report.error.appendDescription('internal_error',
                                                            {'file_name': file_name, 'description': err})
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write(f"+{self.__class_name__}.split() ++ Error  - {err}\n")

                        aborted = True

                        continue

                    if len_possible_types == 0:

                        _ar = ar.copy()

                        if len_valid_types == 1:
                            _ar['file_name'] = dst_file
                            _ar['file_type'] = valid_types[0]
                            split_file_list.append(_ar)

                            mr_part_paths.append({_ar['file_type']: dst_file})

                        elif len_valid_types == 2 and 'nm-res-cns' in valid_types and 'nm-res-xpl' in valid_types:
                            _ar['file_name'] = dst_file
                            _ar['file_type'] = 'nm-res-xpl'
                            split_file_list.append(_ar)

                            mr_part_paths.append({_ar['file_type']: dst_file})

                        elif len_valid_types == 2 and 'nm-res-cya' in valid_types:
                            _ar['file_name'] = dst_file
                            _ar['file_type'] = next(valid_type for valid_type in valid_types if valid_type != 'nm-res-cya')
                            split_file_list.append(_ar)

                            mr_part_paths.append({_ar['file_type']: dst_file})

                        elif len_valid_types == 2\
                                and set(valid_types) == {'nm-res-cya', 'nm-res-ros'}:
                            _ar['file_name'] = dst_file
                            _ar['file_type'] = 'nm-res-ros'
                            split_file_list.append(_ar)

                            mr_part_paths.append({_ar['file_type']: dst_file})

                        elif len_valid_types == 3\
                                and set(valid_types) in ({'nm-res-cya', 'nm-res-cns', 'nm-res-xpl'},
                                                         {'nm-res-isd', 'nm-res-cns', 'nm-res-xpl'}):
                            _ar['file_name'] = dst_file
                            _ar['file_type'] = 'nm-res-xpl'
                            split_file_list.append(_ar)

                            mr_part_paths.append({_ar['file_type']: dst_file})

                        elif len_valid_types == 3\
                                and set(valid_types) == {'nm-res-cha', 'nm-res-cns', 'nm-res-xpl'}:
                            _ar['file_name'] = dst_file
                            _ar['file_type'] = 'nm-res-cha'
                            split_file_list.append(_ar)

                            mr_part_paths.append({_ar['file_type']: dst_file})

                        elif len_valid_types == 3\
                                and set(valid_types) == {'nm-res-cya', 'nm-res-cns', 'nm-res-xpl'}:
                            _ar['file_name'] = dst_file
                            _ar['file_type'] = 'nm-res-xpl'
                            split_file_list.append(_ar)

                        else:
                            _ar['file_name'] = dst_file
                            _ar['file_type'] = valid_types[0]
                            split_file_list.append(_ar)

                            err = f"The restraint file {file_name!r} (MR format) is identified as {valid_types}. "\
                                "@todo: It needs to be split properly."

                            self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.split() ++ Error  - " + err)
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write(f"+{self.__class_name__}.split() ++ Error  - {err}\n")

                            aborted = True

                    elif len_valid_types == 0:

                        _ar = ar.copy()

                        _ar['file_name'] = dst_file
                        _ar['file_type'] = possible_types[0]
                        split_file_list.append(_ar)

                        err = f"The restraint file {file_name!r} (MR format) can be {possible_types}. "\
                            "@todo: It needs to be reviewed."

                        self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.split() ++ Error  - " + err)
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write(f"+{self.__class_name__}.split() ++ Error  - {err}\n")

                        aborted = True

                    else:

                        _ar['file_name'] = dst_file
                        _ar['file_type'] = valid_types[0]
                        split_file_list.append(_ar)

                        err = f"The restraint file {file_name!r} (MR format) is identified as {valid_types} and can be {possible_types} as well. "\
                            "@todo: It needs to be reviewed."

                        self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.split() ++ Error  - " + err)
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write(f"+{self.__class_name__}.split() ++ Error  - {err}\n")

                        aborted = True

            # has MR header
            else:

                original_file_path_list = []

                distinct = False
                ofh = ofh_w_sel = None
                j = 0

                with open(dst_file, 'r') as ifh:
                    for line in ifh:

                        if mr_file_header_pattern.match(line):
                            g = mr_file_header_pattern.search(line).groups()

                            if ofh is not None:
                                if len(g[0]) > 0:
                                    j += 1
                                    ofh.write(g[0] + '\n')
                                ofh.close()
                                if j == 0:
                                    os.remove(original_file_path_list.pop())

                            j = 0
                            _dst_file = os.path.join(dir_path, g[2])
                            original_file_path_list.append(_dst_file)
                            ofh = open(_dst_file, 'w')  # pylint: disable=consider-using-with
                            distinct = True

                        elif sel_mr_file_header_pattern.match(line)\
                                or sel_pk_file_header_pattern.match(line):
                            if sel_mr_file_header_pattern.match(line):
                                g = sel_mr_file_header_pattern.search(line).groups()
                            else:
                                g = sel_pk_file_header_pattern.search(line).groups()

                            if ofh is not None:
                                ofh.close()
                                if ofh_w_sel is not None:
                                    ofh_w_sel.close()
                                    ofh_w_sel = None
                                if j == 0:
                                    os.remove(original_file_path_list.pop())

                            j = 0
                            _dst_file = os.path.join(dir_path, g[1])
                            original_file_path_list.append(_dst_file)
                            ofh = open(_dst_file, 'w')  # pylint: disable=consider-using-with
                            _dst_file_w_sel = _dst_file + f'-selected-as-{g[0][-7:]}'
                            ofh_w_sel = open(_dst_file_w_sel, 'w')  # pylint: disable=consider-using-with
                            distinct = True

                        elif sel_cs_file_header_pattern.match(line):
                            g = sel_cs_file_header_pattern.search(line).groups()

                            if ofh is not None:
                                ofh.close()
                                if ofh_w_sel is not None:
                                    ofh_w_sel.close()
                                    ofh_w_sel = None
                                if j == 0:
                                    os.remove(original_file_path_list.pop())

                            j = 0
                            _dst_file = os.path.join(dir_path, g[1])
                            original_file_path_list.append(_dst_file)
                            ofh = open(_dst_file, 'w')  # pylint: disable=consider-using-with
                            _dst_file_w_sel = _dst_file + '-ignored'
                            ofh_w_sel = open(_dst_file_w_sel, 'w')  # pylint: disable=consider-using-with
                            distinct = True

                        elif not line.isspace() and not comment_pattern.match(line):
                            j += 1
                            if ofh is None:
                                _dst_file = os.path.join(dir_path, src_basename + '-noname.mr')
                                original_file_path_list.append(_dst_file)
                                ofh = open(_dst_file, 'w')  # pylint: disable=consider-using-with
                            ofh.write(line)
                            if ofh_w_sel is not None:
                                ofh_w_sel.write(line)

                        elif ofh is not None:
                            ofh.write(line)
                            if ofh_w_sel is not None:
                                ofh_w_sel.write(line)

                if ofh is not None:
                    ofh.close()
                    if j == 0:
                        os.remove(original_file_path_list.pop())
                    if ofh_w_sel is not None:
                        ofh_w_sel.close()

                if len(original_file_path_list) == 0:
                    distinct = False
                    original_file_path_list.append(dst_file)

                for dst_file in original_file_path_list:
                    ign_dst_file = dst_file + '-ignored'

                    if os.path.exists(ign_dst_file):  # in case the MR file can be ignored
                        remediated = True
                        continue

                    split_ext = os.path.splitext(dst_file)

                    if len(split_ext) == 2:
                        if len(split_ext[1]) > 0:
                            file_ext = split_ext[1][1:].lower()
                        else:
                            file_ext = os.path.basename(split_ext[0]).lower()
                    else:
                        file_ext = os.path.basename(split_ext[0]).lower()

                    if file_ext in ('x', 'rc', 'crd', 'rst', 'inp', 'inpcrd', 'restrt')\
                       or 'rc' in file_ext or 'crd' in file_ext or 'rst' in file_ext or 'inp' in file_ext:  # AMBER coordinate file extensions
                        is_crd = False
                        with open(dst_file, 'r') as ifh:
                            for pos, line in enumerate(ifh, start=1):
                                if pos == 1:
                                    if line.isdigit():
                                        break
                                elif pos == 2:
                                    try:
                                        int(line.lstrip().split()[0])
                                    except (ValueError, IndexError):
                                        break
                                elif pos == 3:
                                    if line.count('.') == 6:
                                        is_crd = True
                                    break

                        if is_crd:
                            shutil.copyfile(dst_file, ign_dst_file)  # ignore AMBER input coordinate file for the next time
                            remediated = True
                            continue

                    if file_ext in ('frc', 'known') or 'frc' in file_ext:
                        is_frc = False
                        with open(dst_file, 'r') as ifh:
                            for pos, line in enumerate(ifh, start=1):
                                if pos == 1:
                                    if not line.startswith('FRCMOD'):
                                        break
                                elif pos == 2:
                                    if line.startswith('MASS'):
                                        is_frc = True
                                    break

                        if is_frc:
                            shutil.copyfile(dst_file, ign_dst_file)  # ignore AMBER frcmod file for the next time
                            remediated = True
                            continue

                    if file_ext == 'seq':
                        is_seq = False
                        _len_seq = None
                        with open(dst_file, 'r') as ifh:
                            for line in ifh:
                                if line.isspace() or comment_pattern.match(line):
                                    continue
                                seq = line.upper().split()
                                len_seq = len(seq)
                                if len_seq > 2:
                                    is_seq = False
                                    break
                                if _len_seq is None:
                                    _len_seq = len_seq
                                elif len_seq != _len_seq:
                                    is_seq = False
                                    break
                                if len_seq == 2:
                                    if (translateToStdResName(seq[0], ccU=self.__ccU) in monDict3 and seq[1].isdigit())\
                                       or (translateToStdResName(seq[1], ccU=self.__ccU) in monDict3 and seq[0].isdigit()):
                                        is_seq = True
                                    else:
                                        is_seq = False
                                        break
                                elif len_seq == 1:
                                    if seq[0] in monDict3:
                                        is_seq = True
                                    else:
                                        is_seq = False
                                        break

                        if is_seq:
                            shutil.copyfile(dst_file, ign_dst_file)  # ignore sequence file for the next time
                            remediated = True
                            continue

                    if file_ext == 'cor':
                        is_cor = False
                        with open(dst_file, 'r') as ifh:
                            for pos, line in enumerate(ifh, start=1):
                                if pos == 1:
                                    if 'Structures from CYANA' not in line:
                                        break
                                elif pos == 2:
                                    if 'CYANA' not in line:
                                        break
                                elif pos == 3:
                                    if line.count('Number') < 3:
                                        break
                                elif pos == 4:
                                    if line.count('.') >= 3:
                                        is_cor = True
                                    break

                        if is_cor:
                            shutil.copyfile(dst_file, ign_dst_file)  # ignore CYANA coordinate file for the next time
                            remediated = True
                            continue

                    ign_pk_file = dst_file + '-ignored-as-pea-any'

                    if os.path.exists(ign_pk_file):  # in case the MR file can be ignored as peak list file

                        settled_file_type, _ = self.__getPeakListFileTypeAndContentSubtype(ign_pk_file)

                        _ar = ar.copy()

                        if settled_file_type is not None:
                            sel_pk_file = dst_file + f'-selected-as-{settled_file_type[-7:]}'
                            os.rename(ign_pk_file, sel_pk_file)

                            _ar['file_name'] = dst_file
                            _ar['file_type'] = settled_file_type

                        else:

                            _ar['file_name'] = dst_file
                            _ar['file_type'] = 'nm-pea-any'

                        if distinct:
                            _ar['original_file_name'] = os.path.basename(dst_file)

                        peak_file_list.append(_ar)

                        pk_list_paths.append({'nmr-peaks': dst_file,
                                              'original_file_name': None if dst_file.endswith('-noname.mr') else os.path.basename(dst_file)})

                        remediated = True

                        continue

                    settled_pk_file = False

                    _ar = ar.copy()

                    for settled_file_type in parsable_pk_file_types:

                        sel_pk_file = dst_file + f'-selected-as-{settled_file_type[-7:]}'

                        if os.path.exists(sel_pk_file):

                            ign_dst_file = sel_pk_file + '-ignored'

                            if os.path.exists(ign_dst_file):
                                continue

                            __ar = _ar.copy()

                            __ar['file_name'] = sel_pk_file
                            __ar['file_type'] = settled_file_type

                            if __ar in peak_file_list:
                                continue

                            peak_file_list.append(__ar)

                            pk_list_paths.append({'nmr-peaks': dst_file})

                            settled_pk_file = remediated = True

                    if settled_pk_file:
                        continue

                    ign_ext_file = dst_file + '-ignored-as-res-oth'

                    if os.path.exists(ign_ext_file):  # in case the MR files can not be parsed
                        _ar = ar.copy()

                        _ar['file_name'] = dst_file
                        _ar['file_type'] = 'nm-res-oth'

                        if distinct:
                            _ar['original_file_name'] = os.path.basename(dst_file)

                        split_file_list.append(_ar)

                        mr_part_paths.append({_ar['file_type']: dst_file,
                                              'original_file_name': None if dst_file.endswith('-noname.mr') else os.path.basename(dst_file)})

                        continue

                    designated = False

                    for _file_type in settled_file_types:

                        sel_file = dst_file + f'-selected-as-{_file_type[-7:]}'

                        if os.path.exists(sel_file):
                            _ar = ar.copy()

                            _ar['file_name'] = dst_file
                            _ar['file_type'] = _file_type

                            if distinct:
                                _ar['original_file_name'] = os.path.basename(dst_file)

                            split_file_list.append(_ar)

                            mr_part_paths.append({_file_type: dst_file,
                                                  'original_file_name': None if dst_file.endswith('-noname.mr') else os.path.basename(dst_file)})

                            designated = True

                            break

                    if designated:
                        continue

                    cor_dst_file = dst_file + '-corrected'

                    if os.path.exists(cor_dst_file):  # in case manually corrected MR file exists
                        dst_file = cor_dst_file

                        remediated = True

                    settled_file_type, _ = self.__getPeakListFileTypeAndContentSubtype(dst_file)

                    if settled_file_type is not None:

                        shutil.copyfile(dst_file, dst_file + f'-selected-as-{settled_file_type[-7:]}')

                        _ar = ar.copy()

                        _ar['file_name'] = dst_file
                        _ar['file_type'] = settled_file_type

                        if distinct:
                            _ar['original_file_name'] = os.path.basename(dst_file)

                        peak_file_list.append(_ar)

                        pk_list_paths.append({'nmr-peaks': dst_file,
                                              'original_file_name': None if dst_file.endswith('-noname.mr') else os.path.basename(dst_file)})

                        remediated = True

                        continue

                    if has_str_format or has_cif_format:

                        dst_file_type = get_type_of_star_file(dst_file)

                        if dst_file_type == 'str':

                            mrPath = dst_file

                            mr_file_path_list = 'restraint_file_path_list'

                            item = {'file_name': mrPath,
                                    'file_type': 'nmr-star',
                                    'original_file_name': os.path.basename(src_basename) + '.mr'}

                            if mr_file_path_list not in self.__inputParamDict:
                                self.__inputParamDict[mr_file_path_list] = [item]
                            else:
                                self.__inputParamDict[mr_file_path_list].append(item)

                            insert_index = self.__file_path_list_len

                            if insert_index > len(self.__star_data):
                                self.__star_data.append(None)
                                self.__star_data_type.append(None)

                            self.report.insertInputSource(insert_index)

                            self.__file_path_list_len += 1

                            input_source = self.report.input_sources[insert_index]

                            file_type = 'nmr-star'
                            file_name = os.path.basename(mrPath)

                            input_source.setItemValue('file_name', file_name)
                            input_source.setItemValue('file_type', file_type)
                            input_source.setItemValue('content_type', 'nmr-restraints')
                            input_source.setItemValue('original_file_name', os.path.basename(src_basename) + '.mr')

                            codec = detect_bom(mrPath, 'utf-8')

                            _mrPath = None

                            if codec != 'utf-8':
                                _mrPath = mrPath + '~'
                                convert_codec(mrPath, _mrPath, codec, 'utf-8')
                                mrPath = _mrPath

                            if is_rtf_file(mrPath):
                                _mrPath = mrPath + '.rtf2txt'
                                convert_rtf_to_ascii(mrPath, _mrPath)
                                mrPath = _mrPath

                            file_subtype = 'O'

                            is_valid, message = self.__nefT.validate_file(mrPath, file_subtype)

                            if not is_valid or not self.__has_star_chem_shift:
                                _is_valid, _ = self.__nefT.validate_file(mrPath, 'S')
                                if _is_valid:
                                    has_cs_str = True

                            self.__original_error_message.append(message)

                            _file_type = message['file_type']  # nef/nmr-star/unknown

                            if is_valid:

                                if _file_type != file_type:

                                    err = f"{file_name!r} was selected as {self.readable_file_type[file_type]} file, "\
                                        f"but recognized as {self.readable_file_type[_file_type]} file."
                                    # DAOTHER-5673
                                    err += " Please re-upload the NEF file as an NMR unified data file." if _file_type == 'nef' else " Please re-upload the file."

                                    if len(message['error']) > 0:
                                        for err_message in message['error']:
                                            if 'No such file or directory' not in err_message:
                                                err += ' ' + re.sub('not in list', 'unknown item.', err_message)

                                    self.report.error.appendDescription('content_mismatch',
                                                                        {'file_name': file_name, 'description': err})
                                    self.report.setError()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.split() ++ Error  - {err}\n")

                                else:

                                    # NEFTranslator.validate_file() generates this object internally, but not re-used.
                                    _is_done, star_data_type, star_data = self.__nefT.read_input_file(mrPath)

                                    self.__has_legacy_sf_issue = False

                                    if star_data_type == 'Saveframe':
                                        self.__has_legacy_sf_issue = True
                                        self.__fixFormatIssueOfInputSource(insert_index, file_name, file_type, mrPath, file_subtype, message)
                                        _is_done, star_data_type, star_data = self.__nefT.read_input_file(mrPath)

                                    if not (self.__has_legacy_sf_issue and _is_done and star_data_type == 'Entry'):

                                        if len(self.__star_data_type) == self.__file_path_list_len:
                                            del self.__star_data_type[-1]
                                            del self.__star_data[-1]

                                        self.__star_data_type.append(star_data_type)
                                        self.__star_data.append(star_data)

                                        self.__rescueFormerNef(insert_index)
                                        self.__rescueImmatureStr(insert_index)

                                    if _is_done:
                                        self.__detectContentSubType__(insert_index, input_source, dir_path)
                                        input_source_dic = input_source.get()
                                        if 'content_subtype' in input_source_dic:
                                            content_subtype = input_source_dic['content_subtype']
                                            if any(True for mr_content_subtype in self.__mr_content_subtypes if mr_content_subtype in content_subtype):
                                                mr_part_paths.append({'nmr-star': mrPath,
                                                                      'original_file_name': None if dst_file.endswith('-noname.mr') else os.path.basename(dst_file)})

                            elif not self.__fixFormatIssueOfInputSource(insert_index, file_name, file_type, mrPath, file_subtype, message):
                                pass

                            if _mrPath is not None:
                                try:
                                    os.remove(_mrPath)
                                except OSError:
                                    pass

                            continue

                        if dst_file_type == 'cif':

                            mrPath = dst_file

                            _mrPath = os.path.splitext(mrPath)[0] + '.cif2str'
                            if not self.__c2S.convert(mrPath, _mrPath):
                                _mrPath = mrPath

                            mrPath = _mrPath

                            mr_file_path_list = 'restraint_file_path_list'

                            item = {'file_name': mrPath,
                                    'file_type': 'nmr-star',
                                    'original_file_name': os.path.basename(src_basename) + '.mr'}

                            if mr_file_path_list not in self.__inputParamDict:
                                self.__inputParamDict[mr_file_path_list] = [item]
                            else:
                                self.__inputParamDict[mr_file_path_list].append(item)

                            insert_index = self.__file_path_list_len

                            if insert_index > len(self.__star_data):
                                self.__star_data.append(None)
                                self.__star_data_type.append(None)

                            self.report.insertInputSource(insert_index)

                            self.__file_path_list_len += 1

                            input_source = self.report.input_sources[insert_index]

                            file_type = 'nmr-star'
                            file_name = os.path.basename(mrPath)

                            input_source.setItemValue('file_name', re.sub(r'\.cif2str$', '', file_name))
                            input_source.setItemValue('file_type', file_type)
                            input_source.setItemValue('content_type', 'nmr-restraints')
                            input_source.setItemValue('original_file_name', os.path.basename(src_basename) + '.mr')

                            codec = detect_bom(mrPath, 'utf-8')

                            _mrPath = None

                            if codec != 'utf-8':
                                _mrPath = mrPath + '~'
                                convert_codec(mrPath, _mrPath, codec, 'utf-8')
                                mrPath = _mrPath

                            if is_rtf_file(mrPath):
                                _mrPath = mrPath + '.rtf2txt'
                                convert_rtf_to_ascii(mrPath, _mrPath)
                                mrPath = _mrPath

                            file_subtype = 'O'

                            is_valid, message = self.__nefT.validate_file(mrPath, file_subtype)

                            if not is_valid or not self.__has_star_chem_shift:
                                _is_valid, _ = self.__nefT.validate_file(mrPath, 'S')
                                if _is_valid:
                                    has_cs_str = True

                            self.__original_error_message.append(message)

                            _file_type = message['file_type']  # nef/nmr-star/unknown

                            if is_valid:

                                if _file_type != file_type:

                                    err = f"{file_name!r} was selected as {self.readable_file_type[file_type]} file, "\
                                        f"but recognized as {self.readable_file_type[_file_type]} file."
                                    # DAOTHER-5673
                                    err += " Please re-upload the NEF file as an NMR unified data file." if _file_type == 'nef' else " Please re-upload the file."

                                    if len(message['error']) > 0:
                                        for err_message in message['error']:
                                            if 'No such file or directory' not in err_message:
                                                err += ' ' + re.sub('not in list', 'unknown item.', err_message)

                                    self.report.error.appendDescription('content_mismatch',
                                                                        {'file_name': file_name, 'description': err})
                                    self.report.setError()

                                    if self.__verbose:
                                        self.__lfh.write(f"+{self.__class_name__}.split() ++ Error  - {err}\n")

                                else:

                                    # NEFTranslator.validate_file() generates this object internally, but not re-used.
                                    _is_done, star_data_type, star_data = self.__nefT.read_input_file(mrPath)

                                    self.__has_legacy_sf_issue = False

                                    if star_data_type == 'Saveframe':
                                        self.__has_legacy_sf_issue = True
                                        self.__fixFormatIssueOfInputSource(insert_index, file_name, file_type, mrPath, file_subtype, message)
                                        _is_done, star_data_type, star_data = self.__nefT.read_input_file(mrPath)

                                    if not (self.__has_legacy_sf_issue and _is_done and star_data_type == 'Entry'):

                                        if len(self.__star_data_type) == self.__file_path_list_len:
                                            del self.__star_data_type[-1]
                                            del self.__star_data[-1]

                                        self.__star_data_type.append(star_data_type)
                                        self.__star_data.append(star_data)

                                        self.__rescueFormerNef(insert_index)
                                        self.__rescueImmatureStr(insert_index)

                                    if _is_done:
                                        self.__detectContentSubType()
                                        input_source_dic = input_source.get()
                                        if 'content_subtype' in input_source_dic:
                                            content_subtype = input_source_dic['content_subtype']
                                            if any(True for mr_content_subtype in self.__mr_content_subtypes if mr_content_subtype in content_subtype):
                                                mr_part_paths.append({'nmr-star': mrPath,
                                                                      'original_file_name': None if dst_file.endswith('-noname.mr') else os.path.basename(dst_file)})

                            elif not self.__fixFormatIssueOfInputSource(insert_index, file_name, file_type, mrPath, file_subtype, message):
                                pass

                            if _mrPath is not None:
                                try:
                                    os.remove(_mrPath)
                                except OSError:
                                    pass

                            continue

                    file_name = os.path.basename(dst_file)

                    dst_file_list = [os.path.join(dir_path, div_name) for div_name in div_file_names if div_name.startswith(file_name)]

                    if len(dst_file_list) == 0:
                        dst_file_list.append(dst_file)

                    for _dst_file in dst_file_list:

                        ign_pk_file = _dst_file + '-ignored-as-pea-any'

                        if os.path.exists(ign_pk_file):  # in case the MR file can be ignored as peak list file

                            settled_file_type, _ = self.__getPeakListFileTypeAndContentSubtype(ign_pk_file)

                            _ar = ar.copy()

                            if settled_file_type is not None:
                                sel_pk_file = _dst_file + f'-selected-as-{settled_file_type[-7:]}'
                                os.rename(ign_pk_file, sel_pk_file)

                                _ar['file_name'] = _dst_file
                                _ar['file_type'] = settled_file_type

                            else:

                                _ar['file_name'] = _dst_file
                                _ar['file_type'] = 'nm-pea-any'

                            if distinct:
                                _ar['original_file_name'] = file_name

                            peak_file_list.append(_ar)

                            pk_list_paths.append({'nmr-peaks': _dst_file,
                                                  'original_file_name': None if file_name.endswith('-noname.mr') else file_name})

                            remediated = True

                            continue

                        designated = False

                        for _file_type in settled_file_types:

                            sel_file = _dst_file + f'-selected-as-{_file_type[-7:]}'

                            if os.path.exists(sel_file):
                                _ar = ar.copy()

                                _ar['file_name'] = _dst_file
                                _ar['file_type'] = _file_type

                                if distinct:
                                    _ar['original_file_name'] = file_name

                                split_file_list.append(_ar)

                                mr_part_paths.append({_file_type: _dst_file,
                                                      'original_file_name': None if file_name.endswith('-noname.mr') else file_name})

                                designated = True

                                break

                        if designated:
                            continue

                        if _dst_file.endswith('-div_ext.mr'):
                            _ar = ar.copy()

                            _ar['file_name'] = _dst_file
                            _ar['file_type'] = 'nm-res-oth'

                            if distinct:
                                _ar['original_file_name'] = file_name

                            split_file_list.append(_ar)

                            mr_part_paths.append({_ar['file_type']: _dst_file,
                                                  'original_file_name': None if file_name.endswith('-noname.mr') else file_name})

                            continue

                        _, _, valid_types, possible_types = self.detectOtherPossibleFormatAsErrorOfLegacyMr(_dst_file, file_name, 'nm-res-mr', [], True)

                        len_valid_types = len(valid_types)
                        len_possible_types = len(possible_types)

                        if self.__debug:
                            self.__lfh.write(f'{valid_types} {possible_types}\n')

                        if len_valid_types == 0 and len_possible_types == 0:

                            ins_msg = ''
                            if not distinct or len(original_file_path_list) == 1:
                                if has_pdb_format and has_cs_str:
                                    ins_msg = 'unexpectedly contains PDB coordinates and assigned chemical shifts, but '
                                elif has_pdb_format:
                                    ins_msg = 'unexpectedly contains PDB coordinates, but '
                                elif has_cs_str:
                                    ins_msg = 'unexpectedly contains assigned chemical shifts, but '

                            _file_name = file_name
                            if file_name != _file_name:
                                _file_name = f'({_file_name}) '
                            else:
                                _file_name = ''

                            err = f"The restraint file {file_name!r} {_file_name}{ins_msg}does not match with any known restraint format. "\
                                "@todo: It needs to be reviewed or marked as entry without restraints."

                            self.report.error.appendDescription('internal_error',
                                                                {'file_name': file_name, 'description': err})
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write(f"+{self.__class_name__}.split() ++ Error  - {err}\n")

                            aborted = True

                            continue

                        if len_possible_types == 0:

                            _ar = ar.copy()

                            if len_valid_types == 1:
                                _ar['file_name'] = _dst_file
                                _ar['file_type'] = valid_types[0]

                                if distinct:
                                    _ar['original_file_name'] = file_name

                                split_file_list.append(_ar)

                                mr_part_paths.append({_ar['file_type']: _dst_file,
                                                      'original_file_name': None if _dst_file.endswith('-noname.mr') else file_name})

                            elif len_valid_types == 2 and 'nm-res-cns' in valid_types and 'nm-res-xpl' in valid_types:
                                _ar['file_name'] = _dst_file
                                _ar['file_type'] = 'nm-res-xpl'

                                if distinct:
                                    _ar['original_file_name'] = file_name

                                split_file_list.append(_ar)

                                mr_part_paths.append({_ar['file_type']: _dst_file,
                                                      'original_file_name': None if _dst_file.endswith('-noname.mr') else file_name})

                            elif len_valid_types == 2 and 'nm-res-cya' in valid_types:
                                _ar['file_name'] = _dst_file
                                _ar['file_type'] = next(valid_type for valid_type in valid_types if valid_type != 'nm-res-cya')

                                if distinct:
                                    _ar['original_file_name'] = file_name

                                split_file_list.append(_ar)

                                mr_part_paths.append({_ar['file_type']: _dst_file,
                                                      'original_file_name': None if _dst_file.endswith('-noname.mr') else file_name})

                            elif len_valid_types == 2\
                                    and set(valid_types) == {'nm-res-cya', 'nm-res-ros'}:
                                _ar['file_name'] = _dst_file
                                _ar['file_type'] = 'nm-res-ros'

                                if distinct:
                                    _ar['original_file_name'] = file_name

                                split_file_list.append(_ar)

                                mr_part_paths.append({_ar['file_type']: _dst_file,
                                                      'original_file_name': None if _dst_file.endswith('-noname.mr') else file_name})

                            elif len_valid_types == 3\
                                    and set(valid_types) in ({'nm-res-cya', 'nm-res-cns', 'nm-res-xpl'},
                                                             {'nm-res-isd', 'nm-res-cns', 'nm-res-xpl'}):
                                _ar['file_name'] = _dst_file
                                _ar['file_type'] = 'nm-res-xpl'

                                if distinct:
                                    _ar['original_file_name'] = file_name

                                split_file_list.append(_ar)

                                mr_part_paths.append({_ar['file_type']: _dst_file,
                                                      'original_file_name': None if _dst_file.endswith('-noname.mr') else file_name})

                            elif len_valid_types == 3\
                                    and set(valid_types) == {'nm-res-cha', 'nm-res-cns', 'nm-res-xpl'}:
                                _ar['file_name'] = _dst_file
                                _ar['file_type'] = 'nm-res-cha'

                                if distinct:
                                    _ar['original_file_name'] = file_name

                                split_file_list.append(_ar)

                                mr_part_paths.append({_ar['file_type']: _dst_file,
                                                      'original_file_name': None if _dst_file.endswith('-noname.mr') else file_name})

                            elif len_valid_types == 3\
                                    and set(valid_types) == {'nm-res-cya', 'nm-res-cns', 'nm-res-xpl'}:
                                _ar['file_name'] = _dst_file
                                _ar['file_type'] = 'nm-res-xpl'

                                if distinct:
                                    _ar['original_file_name'] = file_name

                                split_file_list.append(_ar)

                                mr_part_paths.append({_ar['file_type']: _dst_file,
                                                      'original_file_name': None if _dst_file.endswith('-noname.mr') else file_name})

                            else:
                                _ar['file_name'] = _dst_file
                                _ar['file_type'] = valid_types[0]

                                if distinct:
                                    _ar['original_file_name'] = file_name

                                err = f"The restraint file {file_name!r} (MR format) is identified as {valid_types}. "\
                                    "@todo: It needs to be split properly."

                                self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.split() ++ Error  - " + err)
                                self.report.setError()

                                if self.__verbose:
                                    self.__lfh.write(f"+{self.__class_name__}.split() ++ Error  - {err}\n")

                                aborted = True

                        elif len_valid_types == 0:

                            _ar['file_name'] = _dst_file
                            _ar['file_type'] = possible_types[0]

                            if distinct:
                                _ar['original_file_name'] = file_name

                            err = f"The restraint file {file_name!r} (MR format) can be {possible_types}. "\
                                "@todo: It needs to be reviewed."

                            self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.split() ++ Error  - " + err)
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write(f"+{self.__class_name__}.split() ++ Error  - {err}\n")

                            aborted = True

                        else:

                            _ar['file_name'] = _dst_file
                            _ar['file_type'] = valid_types[0]

                            if distinct:
                                _ar['original_file_name'] = file_name

                            err = f"The restraint file {file_name!r} (MR format) is identified as {valid_types} and can be {possible_types} as well. "\
                                "@todo: It needs to be reviewed."

                            self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.split() ++ Error  - " + err)
                            self.report.setError()

                            if self.__verbose:
                                self.__lfh.write(f"+{self.__class_name__}.split() ++ Error  - {err}\n")

                            aborted = True

        len_peak_file_list = len(peak_file_list)
        has_spectral_peak = len_peak_file_list > 0

        if len(split_file_list) > 0:
            self.__inputParamDict[ar_file_path_list].extend(split_file_list)

            for _ar in split_file_list:

                self.report.appendInputSource()

                input_source = self.report.input_sources[-1]

                input_source.setItemValue('file_name', os.path.basename(_ar['file_name']))
                input_source.setItemValue('file_type', _ar['file_type'])
                input_source.setItemValue('content_type', 'nmr-restraints')
                if 'original_file_name' in _ar:
                    input_source.setItemValue('original_file_name', os.path.basename(_ar['original_file_name']))

        else:

            has_restraint = False

            for fileListId in range(self.__file_path_list_len):

                input_source = self.report.input_sources[fileListId]
                input_source_dic = input_source.get()

                file_name = input_source_dic['file_name']
                file_type = input_source_dic['file_type']
                content_type = input_source_dic['content_type']

                if content_type != 'nmr-restraints':
                    continue

                content_subtype = input_source_dic['content_subtype']

                if content_subtype is None:
                    continue

                if 'dist_restraint' in content_subtype or 'dihed_restraint' in content_subtype or 'rdc_restraint' in content_subtype:
                    has_restraint = True

                if 'spectral_peak' in content_subtype or 'spectral_peak_alt' in content_subtype:
                    has_spectral_peak = True

            if not has_restraint:

                if mr_file_name == '.':

                    rem_dir = os.path.join(dir_path, 'remediation')

                    if os.path.isdir(rem_dir):

                        try:
                            os.rmdir(rem_dir)
                        except OSError:
                            pass

                elif not self.__public_mr_has_valid_star_restraint:

                    touch_file = os.path.join(dir_path, '.entry_without_mr')
                    if not os.path.exists(touch_file):
                        with open(touch_file, 'w') as ofh:
                            ofh.write('')

                    if not any(re.search(r'\/bmr\d+\/work\/data\/', ar['file_name']) for ar in self.__inputParamDict[ar_file_path_list]
                               if ar['file_type'].startswith('nm-res') and ar['file_type'] != 'nm-res-mr'):

                        hint = ' or is not recognized properly'

                        if len_peak_file_list > 0:
                            hint = f', except for {len_peak_file_list} peak list file(s)'

                        err = f"The restraint file contains no restraints{hint}. "\
                            "Please re-upload the restraint file."

                        self.__suspended_errors_for_lazy_eval.append({'content_mismatch':
                                                                     {'file_name': mr_file_name, 'description': err}})

                        if self.__verbose:
                            self.__lfh.write(f"+{self.__class_name__}.split() ++ Error  - {err}\n")

        if has_spectral_peak:

            if len_peak_file_list > 0:

                self.__inputParamDict[ar_file_path_list].extend(peak_file_list)

                for _ar in peak_file_list:

                    self.report.appendInputSource()

                    input_source = self.report.input_sources[-1]

                    input_source.setItemValue('file_name', os.path.basename(_ar['file_name']))
                    input_source.setItemValue('file_type', _ar['file_type'])
                    input_source.setItemValue('content_type', 'nmr-peaks')
                    if 'original_file_name' in _ar:
                        input_source.setItemValue('original_file_name', os.path.basename(_ar['original_file_name']))

            touch_file = os.path.join(dir_path, '.entry_with_pk')
            if not os.path.exists(touch_file):
                with open(touch_file, 'w') as ofh:
                    ofh.write('')

        if not aborted and remediated and mr_file_path is not None:
            with open(mr_file_path, 'w') as ofh:

                header_file = next(mr_part_path['header'] for mr_part_path in mr_part_paths if 'header' in mr_part_path)
                with open(header_file, 'r') as ifh:
                    for line in ifh:
                        ofh.write(line)

                file_idx = 1
                for mr_part_path in mr_part_paths:
                    if 'header' in mr_part_path or 'footer' in mr_part_path:
                        continue

                    for file_type in archival_mr_file_types:
                        if file_type in mr_part_path:
                            file_path = mr_part_path[file_type]
                            if 'original_file_name' in mr_part_path and mr_part_path['original_file_name'] is not None:
                                original_file_name = mr_part_path['original_file_name']
                            else:
                                original_file_name = f'{os.path.basename(src_basename)}-division_P{file_idx}.mr'

                            ofh.write(f'# Restraints file {file_idx}: {original_file_name}\n')
                            ofh.write(f'# Restraint file format: {getRestraintFormatName(file_type).split()[0]}\n')

                            with open(file_path, 'r') as ifh:
                                for line in ifh:
                                    ofh.write(line)

                            break

                    file_idx += 1

                if file_idx == 1 and len(split_file_list) > 0:

                    ofh.write(f'# Restraints file {file_idx}: {os.path.basename(src_basename)}.mr\n')
                    file_type = split_file_list[0]['file_type']
                    ofh.write(f'# Restraint file format: {getRestraintFormatName(file_type).split()[0]}\n')

                    with open(mr_core_path, 'r') as ifh:
                        for line in ifh:
                            ofh.write(line)

                footer_file = next(mr_part_path['footer'] for mr_part_path in mr_part_paths if 'footer' in mr_part_path)
                with open(footer_file, 'r') as ifh:
                    for line in ifh:
                        ofh.write(line)

            try:

                if os.path.exists(mr_file_link):
                    os.remove(mr_file_link)

                os.symlink(mr_file_path, mr_file_link)

                if len(pk_list_paths) > 0:

                    pk_dir = os.path.join(dir_path, 'nmr_peak_lists')

                    try:

                        if not os.path.isdir(pk_dir):
                            os.makedirs(pk_dir)

                    except OSError:
                        pass

                    for pk_list_path in pk_list_paths:

                        pk_file_path = pk_list_path['nmr-peaks']
                        if 'original_file_name' in pk_list_path and pk_list_path['original_file_name'] is not None:
                            original_file_name = pk_list_path['original_file_name']

                        rem_pk_file_path = os.path.join(pk_dir, original_file_name)

                        if os.path.exists(rem_pk_file_path):
                            os.remove(rem_pk_file_path)

                        os.symlink(pk_file_path, rem_pk_file_path)

            except OSError:
                pass

        return not self.report.isError()

    def __getPeakListFileTypeAndContentSubtype(self, file_path: str) -> Tuple[Optional[str], Optional[dict]]:
        """ Return peak list file type and content subtype of a given file path.
        """

        file_type = get_peak_list_format(file_path, True)

        if file_type is not None:

            reader = self.getSimpleFileReader(file_type, False)

            listener, parser_err_listener, _ = reader.parse(file_path, None)

            # ignore lexer error beacuse of imcomplete XML file format
            # has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None
            has_parser_error = parser_err_listener is not None and parser_err_listener.getMessageList() is not None
            content_subtype = listener.getContentSubtype() if listener is not None else None
            if not has_parser_error and content_subtype is not None and len(content_subtype) > 0:
                return file_type, content_subtype

        for file_type in parsable_pk_file_types:

            reader = self.getSimpleFileReader(file_type, False)

            listener, parser_err_listener, lexer_err_listener = reader.parse(file_path, None)

            has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None
            has_parser_error = parser_err_listener is not None and parser_err_listener.getMessageList() is not None
            content_subtype = listener.getContentSubtype() if listener is not None else None
            if not has_lexer_error and not has_parser_error and content_subtype is not None and len(content_subtype) > 0:
                return file_type, content_subtype

        return None, None

    def __getCorrectedMrFilePath(self, src_path: str) -> Tuple[Optional[str], bool]:
        """ Return corrected MR file path.
        """

        ar_file_path_list = 'atypical_restraint_file_path_list'

        dir_path = os.path.dirname(src_path)

        for div_file_name in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path, div_file_name))\
               and (div_file_name.endswith('-div_src.mr') or div_file_name.endswith('-div_dst.mr')):
                div_file_path = os.path.join(dir_path, div_file_name)
                if not any(True for ar in self.__inputParamDict[ar_file_path_list] if ar['file_name'] == div_file_path):
                    os.remove(div_file_path)

        if os.path.exists(src_path):
            src_file_name = os.path.basename(src_path)
            cor_test = '-corrected' in src_file_name
            if cor_test:
                cor_src_path = src_path + '~'
            else:
                if src_path.endswith('.mr'):
                    cor_src_path = re.sub(r'\-trimmed$', '', os.path.splitext(src_path)[0]) + '-corrected.mr'
                else:
                    cor_src_path = re.sub(r'\-trimmed$', '', src_path) + '-corrected'

            return cor_src_path, cor_test

        return None, False

    def getSimpleFileReader(self, file_type: str, verbose: bool, sll_pred: bool = True, reasons: Optional[dict] = None) -> Any:
        """ Return simple file reader for a given format.
        """

        if file_type == 'nm-aux-amb':
            return AmberPTReader(verbose, self.__lfh, None, None, None, None, None,
                                 self.__ccU, self.__csStat, self.__nefT)
        if file_type == 'nm-aux-cha':
            return CharmmCRDReader(verbose, self.__lfh, None, None, None, None, None,
                                   self.__ccU, self.__csStat, self.__nefT)
        if file_type == 'nm-aux-gro':
            return GromacsPTReader(verbose, self.__lfh, None, None, None, None, None,
                                   self.__ccU, self.__csStat, self.__nefT)
        if file_type == 'nm-aux-pdb':
            return BarePDBReader(verbose, self.__lfh, None, None, None, None, None,
                                 self.__ccU, self.__csStat, self.__nefT)

        if file_type == 'nm-res-amb':
            return AmberMRReader(verbose, self.__lfh, None, None, None, None, None,
                                 self.__ccU, self.__csStat, self.__nefT)
        if file_type == 'nm-res-ari':
            return AriaMRReader(verbose, self.__lfh, None, None, None, None, None,
                                self.__ccU, self.__csStat, self.__nefT,
                                reasons)
        if file_type == 'nm-res-arx':
            return AriaMRXReader(verbose, self.__lfh, None, None, None, None, None,
                                 self.__ccU, self.__csStat, self.__nefT,
                                 reasons)
        if file_type == 'nm-res-bar':
            return BareMRReader(verbose, self.__lfh, None, None, None, None, None,
                                self.__ccU, self.__csStat, self.__nefT,
                                reasons)
        if file_type == 'nm-res-bio':
            return BiosymMRReader(verbose, self.__lfh, None, None, None, None, None,
                                  self.__ccU, self.__csStat, self.__nefT,
                                  reasons)
        if file_type == 'nm-res-cha':
            reader = CharmmMRReader(verbose, self.__lfh, None, None, None, None, None,
                                    self.__ccU, self.__csStat, self.__nefT)
            reader.setSllPredMode(sll_pred)
            return reader
        if file_type == 'nm-res-cns':
            reader = CnsMRReader(verbose, self.__lfh, None, None, None, None, None,
                                 self.__ccU, self.__csStat, self.__nefT,
                                 reasons)
            reader.setSllPredMode(sll_pred)
            return reader
        if file_type == 'nm-res-cya':
            reader = CyanaMRReader(verbose, self.__lfh, None, None, None, None, None,
                                   self.__ccU, self.__csStat, self.__nefT,
                                   reasons,
                                   file_ext=self.retrieveOriginalFileExtensionOfCyanaMrFile())
            reader.setRemediateMode(self.__remediation_mode)
            # do not use SLL prediction mode for CyanaMRReader
            # reader.setSllPredMode(sll_pred)
            return reader
        if file_type == 'nm-res-dyn':
            return DynamoMRReader(verbose, self.__lfh, None, None, None, None, None,
                                  self.__ccU, self.__csStat, self.__nefT,
                                  reasons)
        if file_type == 'nm-res-gro':
            return GromacsMRReader(verbose, self.__lfh, None, None, None, None, None,
                                   self.__ccU, self.__csStat, self.__nefT)
        if file_type == 'nm-res-isd':
            return IsdMRReader(verbose, self.__lfh, None, None, None, None, None,
                               self.__ccU, self.__csStat, self.__nefT,
                               reasons)
        if file_type == 'nm-res-noa':
            return CyanaNOAReader(verbose, self.__lfh, None, None, None, None, None,
                                  self.__ccU, self.__csStat, self.__nefT,
                                  reasons)
        if file_type == 'nm-res-ros':
            reader = RosettaMRReader(verbose, self.__lfh, None, None, None, None, None,
                                     self.__ccU, self.__csStat, self.__nefT,
                                     reasons)
            reader.setRemediateMode(self.__remediation_mode)
            return reader
        if file_type == 'nm-res-sch':
            reader = SchrodingerMRReader(verbose, self.__lfh, None, None, None, None, None,
                                         self.__ccU, self.__csStat, self.__nefT,
                                         reasons)
            reader.setSllPredMode(sll_pred)
            return reader
        if file_type == 'nm-res-syb':
            return SybylMRReader(verbose, self.__lfh, None, None, None, None, None,
                                 self.__ccU, self.__csStat, self.__nefT,
                                 reasons)
        if file_type == 'nm-res-xpl':
            reader = XplorMRReader(verbose, self.__lfh, None, None, None, None, None,
                                   self.__ccU, self.__csStat, self.__nefT,
                                   reasons)
            reader.setSllPredMode(sll_pred)
            return reader

        if file_type == 'nm-aux-xea':
            reader = XeasyPROTReader(verbose, self.__lfh, None, None, None, None, None,
                                     self.__ccU, self.__csStat, self.__nefT)
            return reader

        if file_type == 'nm-pea-ari':
            reader = AriaPKReader(verbose, self.__lfh, None, None, None, None, None,
                                  self.__ccU, self.__csStat, self.__nefT,
                                  reasons)
            return reader
        if file_type == 'nm-pea-bar':
            reader = BarePKReader(verbose, self.__lfh, None, None, None, None, None,
                                  self.__ccU, self.__csStat, self.__nefT,
                                  reasons)
            return reader
        if file_type == 'nm-pea-ccp':
            reader = CcpnPKReader(verbose, self.__lfh, None, None, None, None, None,
                                  self.__ccU, self.__csStat, self.__nefT,
                                  reasons)
            return reader
        if file_type == 'nm-pea-oli':
            reader = OliviaPKReader(verbose, self.__lfh, None, None, None, None, None,
                                    self.__ccU, self.__csStat, self.__nefT,
                                    reasons)
            return reader
        if file_type == 'nm-pea-pip':
            reader = NmrPipePKReader(verbose, self.__lfh, None, None, None, None, None,
                                     self.__ccU, self.__csStat, self.__nefT,
                                     reasons)
            return reader
        if file_type == 'nm-pea-pon':
            reader = PonderosaPKReader(verbose, self.__lfh, None, None, None, None, None,
                                       self.__ccU, self.__csStat, self.__nefT,
                                       reasons)
            return reader
        if file_type == 'nm-pea-spa':
            reader = SparkyPKReader(verbose, self.__lfh, None, None, None, None, None,
                                    self.__ccU, self.__csStat, self.__nefT,
                                    reasons)
            return reader
        if file_type == 'nm-pea-sps':
            reader = SparkySPKReader(verbose, self.__lfh, None, None, None, None, None,
                                     self.__ccU, self.__csStat, self.__nefT,
                                     reasons)
            return reader
        if file_type == 'nm-pea-top':
            reader = TopSpinPKReader(verbose, self.__lfh, None, None, None, None, None,
                                     self.__ccU, self.__csStat, self.__nefT,
                                     reasons)
            return reader
        if file_type == 'nm-pea-vie':
            reader = NmrViewPKReader(verbose, self.__lfh, None, None, None, None, None,
                                     self.__ccU, self.__csStat, self.__nefT,
                                     reasons)
            return reader
        if file_type == 'nm-pea-vnm':
            reader = VnmrPKReader(verbose, self.__lfh, None, None, None, None, None,
                                  self.__ccU, self.__csStat, self.__nefT,
                                  reasons)
            return reader
        if file_type == 'nm-pea-xea':
            reader = XeasyPKReader(verbose, self.__lfh, None, None, None, None, None,
                                   self.__ccU, self.__csStat, self.__nefT)
            return reader
        if file_type == 'nm-pea-xwi':
            reader = XwinNmrPKReader(verbose, self.__lfh, None, None, None, None, None,
                                     self.__ccU, self.__csStat, self.__nefT,
                                     reasons)
            return reader

        return None

    def divideLegacyMrIfNecessary(self, file_path: str, file_type: str, err_desc: dict, src_path: str, offset: int) -> bool:
        """ Divive legacy restraint file if necessary.
        """

        src_basename = os.path.splitext(file_path)[0]
        div_src = 'div_dst' in src_basename
        div_src_file = src_basename + '-div_src.mr'
        div_ext_file = src_basename + '-div_ext.mr'
        div_try_file = src_basename + '-div_try.mr'
        div_dst_file = src_basename + '-div_dst.mr'

        if any(True for _err_desc in self.__divide_mr_error_message
               if err_desc['file_path'] == _err_desc['file_path']
               and err_desc['line_number'] == _err_desc['line_number']
               and err_desc['column_position'] == _err_desc['column_position']
               and err_desc['message'] == _err_desc['message']):
            if os.path.exists(div_src_file):
                os.remove(div_src_file)
            if os.path.exists(div_dst_file):
                os.remove(div_dst_file)
            if os.path.exists(div_ext_file):
                os.remove(div_ext_file)
            return False

        self.__divide_mr_error_message.append(err_desc)

        if self.__debug:
            self.__lfh.write('DIV-MR\n')

        if file_type not in parsable_mr_file_types:
            return False

        err_message = err_desc['message']
        err_line_number = err_desc['line_number']
        err_column_position = err_desc['column_position']
        err_input = err_desc.get('input', '')

        xplor_file_type = file_type in ('nm-res-xpl', 'nm-res-cns')
        amber_file_type = file_type == 'nm-res-amb'
        gromacs_file_type = file_type in ('nm-res-gro', 'nm-aux-gro')

        xplor_missing_end = xplor_file_type and err_message.startswith(xplor_missing_end_err_msg)
        xplor_ends_wo_statement = xplor_file_type and (bool(xplor_extra_end_err_msg_pattern.match(err_message))
                                                       or (err_message.startswith(no_viable_alt_err_msg)
                                                           and xplor_end_pattern.match(err_input)))

        xplor_assi_after_or_tag = xplor_file_type and bool(xplor_extra_assi_err_msg_pattern.match(err_message))
        xplor_assi_incompl_tag = xplor_file_type and bool(xplor_extra_ssi_err_msg_pattern.match(err_message))

        xplor_l_paren_wo_assi = xplor_file_type and bool(xplor_extra_l_paren_err_msg_pattern.match(err_message))
        xplor_00_origin = xplor_file_type and err_message.startswith(no_viable_alt_err_msg) and ' 00' in err_input

        amber_missing_end = amber_file_type and err_message.startswith(amber_missing_end_err_msg)
        amber_ends_wo_statement = amber_file_type and (bool(amber_extra_end_err_msg_pattern.match(err_message))
                                                       or (err_message.startswith(no_viable_alt_err_msg)
                                                           and amber_end_pattern.match(err_input)))

        concat_xplor_assi = (xplor_file_type
                             and (err_message.startswith(mismatched_input_err_msg)
                                  or err_message.startswith(extraneous_input_err_msg))
                             and bool(xplor_assi_pattern.search(err_input))
                             and not bool(xplor_class_pattern.search(err_input)))
        concat_xplor_rest = (xplor_file_type
                             and (err_message.startswith(mismatched_input_err_msg)
                                  or err_message.startswith(extraneous_input_err_msg))
                             and bool(xplor_rest_pattern.search(err_input)))
        concat_xplor_set = (xplor_file_type
                            and (err_message.startswith(mismatched_input_err_msg)
                                 or err_message.startswith(extraneous_input_err_msg))
                            and bool(xplor_set_pattern.search(err_input))
                            and get_peak_list_format_from_string(err_input) is None)
        concat_amber_rst = (amber_file_type
                            and (err_message.startswith(mismatched_input_err_msg)
                                 or err_message.startswith(extraneous_input_err_msg))
                            and bool(amber_rst_pattern.search(err_input))
                            and not bool(amber_rst_pattern.match(err_input)))

        concat_gromacs_tag = not gromacs_file_type and bool(gromacs_tag_pattern.search(err_input))

        concat_comment = (file_type in linear_mr_file_types
                          and err_message.startswith(no_viable_alt_err_msg)
                          and bool(comment_pattern.search(err_input)))

        if concat_xplor_assi and bool(xplor_assi_pattern.match(err_input)):
            if expecting_l_paren in err_message:
                xplor_missing_end = True
                concat_xplor_assi = False
            if concat_xplor_rest or concat_xplor_set:
                concat_xplor_assi = False

        reader = prev_input = next_input = None

        if not (xplor_missing_end or xplor_ends_wo_statement
                or xplor_l_paren_wo_assi or xplor_00_origin
                or amber_missing_end or amber_ends_wo_statement
                or concat_xplor_assi or concat_xplor_rest or concat_xplor_set
                or concat_amber_rst
                or concat_gromacs_tag
                or concat_comment):

            if err_column_position > 0 and not err_input[0:err_column_position].isspace():
                test_line = err_input[0:err_column_position]

                if reader is None:
                    reader = self.getSimpleFileReader(file_type, False)

                _, parser_err_listener, lexer_err_listener = reader.parse(test_line, None, isFilePath=False)

                has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None
                has_parser_error = parser_err_listener is not None and parser_err_listener.getMessageList() is not None

                if not has_lexer_error and not has_parser_error:

                    concat_input = err_input[err_column_position:]

                    if comment_pattern.match(concat_input) or (len(concat_input) > 0 and concat_input[0].isalnum()):

                        if self.__debug:
                            self.__lfh.write('DIV-MR-EXIT #1-1\n')

                        return self.__divideLegacyMr(file_path, file_type, err_desc, src_path, offset)

                    if self.__debug:
                        self.__lfh.write('DIV-MR-EXIT #1-2\n')

                    return False

                # try to resolve unexcepted concatenation
                test_line = err_input[err_column_position + 1:]

                if len(test_line) > 0:

                    _, parser_err_listener, lexer_err_listener = reader.parse(test_line, None, isFilePath=False)

                    has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None
                    has_parser_error = parser_err_listener is not None and parser_err_listener.getMessageList() is not None

                    if not has_lexer_error and not has_parser_error:
                        err_desc['column_position'] += 1

                        corrected = self.__divideLegacyMr(file_path, file_type, err_desc, src_path, offset)

                        if corrected and os.path.exists(src_path):

                            cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                            if cor_src_path is not None:

                                offset += err_line_number - 1

                                j = 0

                                with open(src_path, 'r') as ifh, \
                                        open(cor_src_path, 'w') as ofh:
                                    for line in ifh:
                                        if j == offset:
                                            ofh.write(line[:err_column_position + 1] + '\n')
                                            ofh.write(line[err_column_position + 1:])
                                        else:
                                            ofh.write(line)
                                        j += 1

                                if cor_test:
                                    os.rename(cor_src_path, src_path)

                                if self.__debug:
                                    self.__lfh.write('DIV-MR-EXIT #2-1\n')

                            else:

                                if self.__debug:
                                    self.__lfh.write('DIV-MR-EXIT #2-2\n')

                                corrected = False

                        else:

                            if self.__debug:
                                self.__lfh.write('DIV-MR-EXIT #2-3\n')

                        return corrected

        i = j = j_offset = 0

        ws_or_comment = True

        interval = []

        with open(file_path, 'r') as ifh, \
                open(div_src_file, 'w') as ofh, \
                open(div_try_file, 'w') as ofh2:
            for line in ifh:
                i += 1
                if i < err_line_number - MR_MAX_SPACER_LINES:
                    if ws_or_comment:
                        if line.isspace() or comment_pattern.match(line)\
                           or (gromacs_file_type and gromacs_comment_pattern.match(line)):
                            pass
                        else:
                            ws_or_comment = False
                    ofh.write(line)
                    j += 1
                    continue
                if i < err_line_number:
                    if ws_or_comment:
                        if line.isspace() or comment_pattern.match(line)\
                           or (gromacs_file_type and gromacs_comment_pattern.match(line)):
                            pass
                        else:
                            ws_or_comment = False
                    interval.append({'line': line,
                                     'ws_or_comment': line.isspace() or bool(comment_pattern.match(line))
                                     or (gromacs_file_type and bool(gromacs_comment_pattern.match(line)))})
                    if i < err_line_number - 1:
                        continue
                    if i == err_line_number - 1:
                        prev_input = line
                    _k = len(interval) - 1
                    _c = interval[-1]['line'][0]
                    for _interval in reversed(interval):
                        c = _interval['line'][0]
                        if _interval['ws_or_comment'] and {c, _c} != comment_code_mixed_set:
                            _c = c
                            _k -= 1
                            continue
                        break
                    for k, _interval in enumerate(interval):
                        if k <= _k:
                            ofh.write(_interval['line'])
                            j += 1
                        else:
                            ofh2.write(_interval['line'])
                            j_offset += 1
                    continue
                if i == err_line_number + 1:
                    next_input = line
                ofh2.write(line)

        offset += err_line_number - 1

        xplor_missing_end_before = (xplor_file_type and err_message.startswith(mismatched_input_err_msg)
                                    and not bool(xplor_expecting_symbol_pattern.search(err_message))  # exclude syntax errors in a factor
                                    and prev_input is not None and bool(xplor_assi_pattern.search(prev_input)))

        xplor_no_syntax_err_in_fac_or_ann = not bool(xplor_expecting_equ_op_pattern.search(err_message))\
            and not bool(xplor_expecting_seg_id_pattern.search(err_message))\
            and not err_message.startswith(no_viable_alt_err_msg)

        amber_missing_comma_before = (amber_file_type and err_message.startswith(mismatched_input_err_msg)
                                      and bool(amber_expecting_comma_pattern.search(err_message)))

        if (xplor_missing_end or xplor_ends_wo_statement
                or xplor_l_paren_wo_assi or xplor_00_origin
                or xplor_missing_end_before
                or amber_missing_end or amber_ends_wo_statement
                or amber_missing_comma_before
                or concat_xplor_assi or concat_xplor_rest or concat_xplor_set
                or concat_amber_rst
                or concat_gromacs_tag
                or concat_comment) or i <= err_line_number or j == 0:

            corrected = False

            if err_line_number - 1 in (i, j + j_offset) and xplor_l_paren_wo_assi:  # this should be before 'concat_comment' routine

                if comment_pattern.match(prev_input) and xplor_assi_pattern.search(prev_input):

                    k = k2 = 0

                    with open(file_path, 'r') as ifh:
                        for line in ifh:
                            k += 1
                            if k <= err_line_number:
                                continue
                            if k < err_line_number + MR_MAX_SPACER_LINES:
                                if xplor_assi_pattern.match(line) or comment_pattern.match(line) or line.isspace():
                                    k2 = k
                                    break
                                continue
                            break

                    if k2 != 0:

                        comment_code = prev_input.rstrip()[0]

                        cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                        if cor_src_path is not None:

                            k = 0

                            with open(src_path, 'r') as ifh, \
                                    open(cor_src_path, 'w') as ofh:
                                for line in ifh:
                                    k += 1
                                    if k < err_line_number:
                                        ofh.write(line)
                                    elif k < k2:
                                        ofh.write(comment_code + line)
                                    else:
                                        ofh.write(line)

                            if cor_test:
                                os.rename(cor_src_path, src_path)

                            if self.__debug:
                                self.__lfh.write('DIV-MR-EXIT #3-1\n')

                            return True

                if os.path.exists(div_src_file):
                    os.remove(div_src_file)
                if os.path.exists(div_try_file):
                    os.remove(div_try_file)

                if prev_input is not None:
                    err_desc['previous_input'] = f"Do you need to comment out the succeeding lines as well?\n{prev_input}"

                if self.__debug and not corrected:
                    self.__lfh.write('DIV-MR-EXIT #3-2\n')

                return False

            if xplor_00_origin:

                cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                if cor_src_path is not None:

                    with open(src_path, 'r') as ifh, \
                            open(cor_src_path, 'w') as ofh:
                        for line in ifh:
                            if ' 00' in line:
                                ofh.write(re.sub(r' 00', ' OO', line))
                            else:
                                ofh.write(line)

                    if cor_test:
                        os.rename(cor_src_path, src_path)

                    if self.__debug:
                        self.__lfh.write('DIV-MR-EXIT #3-3\n')

                    corrected = True

            if xplor_ends_wo_statement or amber_ends_wo_statement:

                has_end_tag = False

                k = 0

                with open(src_path, 'r') as ifh:
                    for line in ifh:
                        if k == offset:
                            if xplor_ends_wo_statement and xplor_end_pattern.match(line):
                                has_end_tag = True
                            if amber_ends_wo_statement and amber_end_pattern.match(line):
                                has_end_tag = True
                            break
                        k += 1

                if has_end_tag:

                    cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                    if cor_src_path is not None:

                        k = 0

                        with open(src_path, 'r') as ifh, \
                                open(cor_src_path, 'w') as ofh:
                            for line in ifh:
                                if k == offset:
                                    ofh.write('#' + line)
                                else:
                                    ofh.write(line)
                                k += 1

                        if cor_test:
                            os.rename(cor_src_path, src_path)

                        if self.__debug:
                            self.__lfh.write('DIV-MR-EXIT #3-4\n')

                        corrected = True

            if concat_xplor_assi or concat_xplor_rest or concat_xplor_set or concat_amber_rst:

                code_index = -1

                if concat_xplor_assi:
                    for m in xplor_any_assi_pattern.finditer(err_input):
                        code_index = m.start()
                elif concat_xplor_rest:
                    for m in xplor_any_rest_pattern.finditer(err_input):
                        code_index = m.start()
                elif concat_xplor_set:
                    for m in xplor_any_set_pattern.finditer(err_input):
                        code_index = m.start()
                elif concat_amber_rst:
                    for m in amber_rst_pattern.finditer(err_input):
                        code_index = m.start()

                if code_index != -1:
                    test_line = err_input[0:code_index]

                    if len(test_line.strip()) > 0:
                        typo_for_comment_out = bool(possible_typo_for_comment_out_pattern.match(test_line))

                        if reader is None:
                            reader = self.getSimpleFileReader(file_type, False)

                        _, _, lexer_err_listener = reader.parse(test_line, None, isFilePath=False)

                        has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None

                        if not has_lexer_error:

                            cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                            if cor_src_path is not None:

                                k = 0

                                with open(src_path, 'r') as ifh, \
                                        open(cor_src_path, 'w') as ofh:
                                    for line in ifh:
                                        if k == offset:
                                            if typo_for_comment_out:
                                                g = possible_typo_for_comment_out_pattern.search(test_line).groups()
                                                if g[0] == '1':
                                                    test_line = re.sub(r'1', '!', test_line)
                                                else:
                                                    test_line = re.sub(r'3', '#', test_line)
                                                ofh.write(f"{test_line}{err_input[code_index:]}\n")
                                            else:
                                                ofh.write(f"{test_line}\n{err_input[code_index:]}\n")
                                        else:
                                            ofh.write(line)
                                        k += 1

                                if cor_test:
                                    os.rename(cor_src_path, src_path)

                                if self.__debug:
                                    self.__lfh.write('DIV-MR-EXIT #3-5\n')

                                corrected = True

            if concat_gromacs_tag:
                test_line = err_input[err_column_position + 1:]

                if len(test_line) > 0:

                    test_reader = self.getSimpleFileReader('nm-res-gro', False)

                    _, _parser_err_listener, _lexer_err_listener = test_reader.parse(test_line, None, isFilePath=False)

                    _has_lexer_error = _lexer_err_listener is not None and _lexer_err_listener.getMessageList() is not None

                    if not _has_lexer_error:

                        if self.__debug:
                            self.__lfh.write('DIV-MR-EXIT #3-6\n')

                        return self.__divideLegacyMr(file_path, file_type, err_desc, src_path, offset)

                    test_reader = self.getSimpleFileReader('nm-aux-gro', False)

                    _, _parser_err_listener, _lexer_err_listener = test_reader.parse(test_line, None, isFilePath=False)

                    _has_lexer_error = _lexer_err_listener is not None and _lexer_err_listener.getMessageList() is not None

                    if not _has_lexer_error:

                        if self.__debug:
                            self.__lfh.write('DIV-MR-EXIT #3-7\n')

                        return self.__divideLegacyMr(file_path, file_type, err_desc, src_path, offset)

            if concat_comment:

                comment_code_index = -1
                if '#' in err_input:
                    comment_code_index = err_input.index('#')
                if '!' in err_input:
                    if comment_code_index == -1:
                        comment_code_index = err_input.index('!')
                    elif err_input.index('!') < comment_code_index:
                        comment_code_index = err_input.index('!')

                if comment_code_index != -1:
                    test_line = err_input[0:comment_code_index]

                    if reader is None:
                        reader = self.getSimpleFileReader(file_type, False)

                    _, parser_err_listener, lexer_err_listener = reader.parse(test_line, None, isFilePath=False)

                    has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None
                    has_parser_error = parser_err_listener is not None and parser_err_listener.getMessageList() is not None

                    if not has_lexer_error and not has_parser_error:

                        cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                        if cor_src_path is not None:

                            k = 0

                            with open(src_path, 'r') as ifh, \
                                    open(cor_src_path, 'w') as ofh:
                                for line in ifh:
                                    if k == offset:
                                        ofh.write(f"{test_line} {err_input[comment_code_index:]}\n")
                                    else:
                                        ofh.write(line)
                                    k += 1

                            if cor_test:
                                os.rename(cor_src_path, src_path)

                            if self.__debug:
                                self.__lfh.write('DIV-MR-EXIT #3-8\n')

                            corrected = True

            if err_line_number - 1 in (i, j + j_offset) and (xplor_missing_end or xplor_missing_end_before):

                if not xplor_missing_end_before or xplor_no_syntax_err_in_fac_or_ann:

                    cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                    if cor_src_path is not None:

                        middle = i != err_line_number - 1
                        is_done = False

                        k = 0 if xplor_missing_end else 1

                        with open(src_path, 'r') as ifh, \
                                open(cor_src_path, 'w') as ofh:
                            for line in ifh:
                                if middle:
                                    if k == err_line_number - 2 and comment_pattern.match(line):
                                        ofh.write('end\n')
                                        is_done = True
                                    elif k == err_line_number - 1 and not is_done:
                                        ofh.write('end\n')
                                ofh.write(line)
                                k += 1
                            if not middle:
                                ofh.write('end\n')

                        if cor_test:
                            os.rename(cor_src_path, src_path)

                        if self.__debug:
                            self.__lfh.write('DIV-MR-EXIT #3-9\n')

                        corrected = True

            if err_line_number - 1 in (i, j + j_offset) and amber_missing_comma_before:

                cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                if cor_src_path is not None:

                    k = 1

                    with open(src_path, 'r') as ifh, \
                            open(cor_src_path, 'w') as ofh:
                        for line in ifh:
                            if k == err_line_number:
                                ofh.write(',' + line)
                            else:
                                ofh.write(line)
                            k += 1

                    if cor_test:
                        os.rename(cor_src_path, src_path)

                    if self.__debug:
                        self.__lfh.write('DIV-MR-EXIT #3-10\n')

                    corrected = True

            if i == err_line_number - 1 and amber_missing_end:

                cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                if cor_src_path is not None:

                    with open(src_path, 'r') as ifh, \
                            open(cor_src_path, 'w') as ofh:
                        for line in ifh:
                            ofh.write(line)
                        ofh.write('&end\n')

                    if cor_test:
                        os.rename(cor_src_path, src_path)

                    if self.__debug:
                        self.__lfh.write('DIV-MR-EXIT #3-11\n')

                    corrected = True

            if not (corrected or concat_xplor_assi or concat_xplor_rest or concat_xplor_set or concat_amber_rst)\
               and (j + j_offset) in (0, err_line_number - 1)\
               and (not xplor_missing_end_before or xplor_no_syntax_err_in_fac_or_ann):
                test_line = err_input

                if reader is None:
                    reader = self.getSimpleFileReader(file_type, False)

                _, _, lexer_err_listener = reader.parse(test_line, None, isFilePath=False)

                has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None

                if not has_lexer_error:

                    cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                    if cor_src_path is not None:

                        k = 0

                        with open(src_path, 'r') as ifh, \
                                open(cor_src_path, 'w') as ofh:
                            for line in ifh:
                                if k == offset:
                                    ofh.write('#' + line)
                                else:
                                    ofh.write(line)
                                k += 1

                        if cor_test:
                            os.rename(cor_src_path, src_path)

                        if self.__debug:
                            self.__lfh.write('DIV-MR-EXIT #3-12\n')

                        corrected = True

            if os.path.exists(div_src_file):
                os.remove(div_src_file)
            if os.path.exists(div_try_file):
                os.remove(div_try_file)

            if prev_input is not None and (err_message.startswith(no_viable_alt_err_msg) or err_message.startswith(extraneous_input_err_msg)):
                if comment_pattern.match(prev_input):
                    err_desc['previous_input'] = f"Do you need to comment out the succeeding lines as well?\n{prev_input}"
                elif not xplor_assi_after_or_tag and not xplor_assi_incompl_tag:
                    err_desc['previous_input'] = prev_input

            if self.__debug and not corrected:
                self.__lfh.write('DIV-MR-EXIT #3-13\n')

            return corrected

        if ws_or_comment:
            os.remove(div_src_file)
            os.remove(div_try_file)

            if self.__debug:
                self.__lfh.write('DIV-MR-EXIT #4\n')

            return False

        if not os.path.exists(div_try_file):
            return False

        file_name = os.path.basename(div_try_file)

        _, _, valid_types, possible_types = self.detectOtherPossibleFormatAsErrorOfLegacyMr(div_try_file, file_name, 'nm-res-mr', [], True)

        len_valid_types = len(valid_types)
        len_possible_types = len(possible_types)

        if len_valid_types == 0 and len_possible_types == 0:

            if err_column_position > 0 and not err_input[0:err_column_position].isspace():
                test_line = err_input[0:err_column_position]

                if reader is None:
                    reader = self.getSimpleFileReader(file_type, False)

                _, _, lexer_err_listener = reader.parse(test_line, None, isFilePath=False)

                has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None

                if not has_lexer_error:
                    os.remove(div_src_file)
                    os.remove(div_try_file)

                    if get_peak_list_format_from_string(err_input) is not None:

                        if self.__debug:
                            self.__lfh.write('DIV-MR-EXIT #5-1\n')

                        return self.peelLegacyMrIfNecessary(file_path, file_type, err_desc, src_path, offset)

                    if self.__debug:
                        self.__lfh.write('DIV-MR-EXIT #5-2\n')

                    return False  # not split MR file because of the lexer errors to be handled by manual

            if None not in (next_input, re.search(r'[A-Za-z]', next_input)):
                test_line = next_input

                if reader is None:
                    reader = self.getSimpleFileReader(file_type, False)

                _, parser_err_listener, lexer_err_listener = reader.parse(test_line, None, isFilePath=False)

                has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None

                if not has_lexer_error and (prev_input is None or not (prev_input.isspace() or bool(comment_pattern.match(prev_input)))):

                    if err_column_position == 0 and file_type not in linear_mr_file_types:

                        for test_file_type in linear_mr_file_types:
                            test_reader = self.getSimpleFileReader(test_file_type, False)

                            listener, parser_err_listener, lexer_err_listener = test_reader.parse(test_line, None, isFilePath=False)

                            has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None
                            has_parser_error = parser_err_listener is not None and parser_err_listener.getMessageList() is not None
                            if test_file_type == 'nm-res-ros':
                                _content_subtype = listener.getEffectiveContentSubtype() if listener is not None else None
                            else:
                                _content_subtype = listener.getContentSubtype() if listener is not None else None
                            if _content_subtype is not None and len(_content_subtype) == 0:
                                _content_subtype = None
                            has_content = _content_subtype is not None

                            if not has_lexer_error and not has_parser_error and has_content:

                                if div_src:
                                    os.remove(file_path)

                                os.rename(div_try_file, div_dst_file)

                                is_valid = True  # triggar for more split
                                re_valid = False  # local lexer/parser errors should be handled by manual

                                k = l = 0  # noqa: E741

                                with open(div_dst_file, 'r') as ifh:
                                    for line in ifh:
                                        if k > 0 and not (line.isspace() or bool(comment_pattern.match(line))):
                                            listener, parser_err_listener, lexer_err_listener = test_reader.parse(line, None, isFilePath=False)
                                            has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None
                                            has_parser_error = parser_err_listener is not None and parser_err_listener.getMessageList() is not None
                                            if test_file_type == 'nm-res-ros':
                                                _content_subtype = listener.getEffectiveContentSubtype() if listener is not None else None
                                            else:
                                                _content_subtype = listener.getContentSubtype() if listener is not None else None
                                            if _content_subtype is not None and len(_content_subtype) == 0:
                                                _content_subtype = None
                                            has_content = _content_subtype is not None
                                            if has_lexer_error or has_parser_error or not has_content:
                                                if is_valid:
                                                    is_valid = False
                                            elif not is_valid:
                                                re_valid = True
                                                break
                                        if is_valid:
                                            k += 1
                                        else:
                                            l += 1  # noqa: E741
                                            if l >= MR_MAX_SPACER_LINES:
                                                break

                                if not is_valid and not re_valid:

                                    _src_basename = os.path.splitext(div_dst_file)[0]
                                    _div_src_file = _src_basename + '-div_src.mr'
                                    _div_dst_file = _src_basename + '-div_dst.mr'

                                    l = 0  # noqa: E741

                                    with open(div_dst_file, 'r') as ifh, \
                                            open(_div_src_file, 'w') as ofh, \
                                            open(_div_dst_file, 'w') as ofh2:
                                        for line in ifh:
                                            if l < k:
                                                ofh.write(line)
                                            else:
                                                ofh2.write(line)
                                            l += 1  # noqa: E741

                                    os.remove(div_dst_file)

                                if self.__debug:
                                    self.__lfh.write('DIV-MR-EXIT #6\n')

                                return True

                    os.remove(div_src_file)
                    os.remove(div_try_file)

                    if prev_input is not None:
                        if comment_pattern.match(prev_input):
                            err_desc['previous_input'] = f"Do you need to comment out the succeeding lines as well?\n{prev_input}"
                        elif not xplor_assi_after_or_tag and not xplor_assi_incompl_tag:
                            err_desc['previous_input'] = prev_input

                    if self.__debug:
                        self.__lfh.write('DIV-MR-EXIT #7\n')

                    return False  # not split MR file because of the lexer errors to be handled by manual

            if div_src:
                os.remove(file_path)

            os.rename(div_try_file, div_ext_file)

            if self.__debug:
                self.__lfh.write('DIV-MR-EXIT #8\n')

            return True  # succeeded in eliminating uninterpretable parts

        if len_possible_types > 0:
            os.remove(div_src_file)
            os.remove(div_try_file)

            if prev_input is not None:
                if comment_pattern.match(prev_input):
                    err_desc['previous_input'] = f"Do you need to comment out the succeeding lines as well?\n{prev_input}"
                elif not xplor_assi_after_or_tag and not xplor_assi_incompl_tag:
                    err_desc['previous_input'] = prev_input

            if self.__debug:
                self.__lfh.write('DIV-MR-EXIT #9\n')

            return False

        if file_type in valid_types:
            os.remove(div_src_file)
            os.remove(div_try_file)

            if prev_input is not None:
                if comment_pattern.match(prev_input):
                    err_desc['previous_input'] = f"Do you need to comment out the succeeding lines as well?\n{prev_input}"
                elif not xplor_assi_after_or_tag and not xplor_assi_incompl_tag:
                    err_desc['previous_input'] = prev_input

            if self.__debug:
                self.__lfh.write('DIV-MR-EXIT #10\n')

            return False  # actual issue in the line before the parser error should be handled by manual

        if prev_input is not None and comment_pattern.match(prev_input)\
           and len_valid_types > 0 and valid_types[0] not in parsable_pk_file_types\
           and file_type != 'nm-res-cya' and 'nm-res-cya' not in valid_types:
            # CYANA MR grammar is lax to check comment

            try:

                g = comment_pattern.search(prev_input).groups()

                test_line = g[0]

                if reader is None:
                    reader = self.getSimpleFileReader(file_type, False)

                _, _, lexer_err_listener = reader.parse(test_line, None, isFilePath=False)

                has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None

                if not has_lexer_error:
                    os.remove(div_src_file)
                    os.remove(div_try_file)

                    err_desc['previous_input'] = f"Do you need to comment out the succeeding lines as well?\n{prev_input}"

                    if self.__debug:
                        self.__lfh.write('DIV-MR-EXIT #11\n')

                    return False  # actual issue in the line before the parser error should be handled by manual

            except AttributeError:
                pass

        if div_src:
            os.remove(file_path)

        if self.__debug:
            self.__lfh.write(f'{valid_types} {possible_types}\n')

        os.rename(div_try_file, div_dst_file)

        file_path = div_dst_file

        if len_valid_types == 1:
            file_type = valid_types[0]

        elif len_valid_types == 2:
            if 'nm-res-cns' in valid_types and 'nm-res-xpl' in valid_types:
                file_type = 'nm-res-xpl'

            elif 'nm-res-cya' in valid_types:
                file_type = next(valid_type for valid_type in valid_types if valid_type != 'nm-res-cya')

            elif 'nm-res-cya' in valid_types and 'nm-res-ros' in valid_types:
                file_type = 'nm-res-ros'

        elif len_valid_types == 3:
            set_valid_types = set(valid_types)
            if set_valid_types in ({'nm-res-cya', 'nm-res-cns', 'nm-res-xpl'},
                                   {'nm-res-isd', 'nm-res-cns', 'nm-res-xpl'}):
                file_type = 'nm-res-xpl'

            elif set_valid_types == {'nm-res-cha', 'nm-res-cns', 'nm-res-xpl'}:
                file_type = 'nm-res-cha'

            elif set_valid_types == {'nm-res-cya', 'nm-res-cns', 'nm-res-xpl'}:
                file_type = 'nm-res-xpl'

        if self.__debug:
            self.__lfh.write(f' -> {file_type}\n')

        self.__testFormatValidityOfLegacyMr(file_path, file_type, src_path, offset)

        if self.__debug:
            self.__lfh.write('DIV-MR-DONE\n')

        return True

    def peelLegacyMrIfNecessary(self, file_path: str, file_type: str, err_desc: dict, src_path: str, offset: int) -> bool:
        """ Peel uninterpretable restraints from the legacy NMR file if necessary.
        """

        src_basename = os.path.splitext(file_path)[0]
        div_src = 'div_dst' in src_basename
        div_src_file = src_basename + '-div_src.mr'
        div_ext_file = src_basename + '-div_ext.mr'
        div_try_file = src_basename + '-div_try.mr'
        div_dst_file = src_basename + '-div_dst.mr'

        if any(True for _err_desc in self.__peel_mr_error_message
               if err_desc['file_path'] == _err_desc['file_path']
               and err_desc['line_number'] == _err_desc['line_number']
               and err_desc['column_position'] == _err_desc['column_position']
               and err_desc['message'] == _err_desc['message']):
            if os.path.exists(div_src_file):
                os.remove(div_src_file)
            if os.path.exists(div_dst_file):
                os.remove(div_dst_file)
            if os.path.exists(div_ext_file):
                os.remove(div_ext_file)
            return False

        self.__peel_mr_error_message.append(err_desc)

        if self.__debug:
            self.__lfh.write('PEEL-MR\n')

        reader = self.getSimpleFileReader(file_type, False)

        if reader is None:
            return False

        err_message = err_desc['message']
        err_line_number = err_desc['line_number']
        err_column_position = err_desc['column_position']
        err_input = err_desc.get('input', '')

        xplor_file_type = file_type in ('nm-res-xpl', 'nm-res-cns')
        amber_file_type = file_type == 'nm-res-amb'
        gromacs_file_type = file_type in ('nm-res-gro', 'nm-aux-gro')

        xplor_ends_wo_statement = xplor_file_type and (bool(xplor_extra_end_err_msg_pattern.match(err_message))
                                                       or (err_message.startswith(no_viable_alt_err_msg)
                                                           and xplor_end_pattern.match(err_input)))
        amber_ends_wo_statement = amber_file_type and (bool(amber_extra_end_err_msg_pattern.match(err_message))
                                                       or (err_message.startswith(no_viable_alt_err_msg)
                                                           and amber_end_pattern.match(err_input)))

        corrected = False

        if xplor_ends_wo_statement or amber_ends_wo_statement:

            _offset = offset + err_line_number - 1

            has_end_tag = False

            k = 0

            with open(src_path, 'r') as ifh:
                for line in ifh:
                    if k == _offset:
                        if xplor_ends_wo_statement and xplor_end_pattern.match(line):
                            has_end_tag = True
                        if amber_ends_wo_statement and amber_end_pattern.match(line):
                            has_end_tag = True
                        break
                    k += 1

            if has_end_tag:

                cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                if cor_src_path is not None:

                    k = 0

                    with open(src_path, 'r') as ifh, \
                            open(cor_src_path, 'w') as ofh:
                        for line in ifh:
                            if k == _offset:
                                ofh.write('#' + line)
                            else:
                                ofh.write(line)
                            k += 1

                    if cor_test:
                        os.rename(cor_src_path, src_path)

                    corrected = True

        if err_column_position > 0 and not err_input[0:err_column_position].isspace():
            test_line = err_input[err_column_position:]

            if comment_pattern.match(test_line):

                if self.__debug:
                    self.__lfh.write('PEEL-MR-EXIT #1\n')

                return self.__divideLegacyMr(file_path, file_type, err_desc, src_path, offset) | corrected

            for test_file_type in parsable_mr_file_types:

                if test_file_type == file_type:
                    continue

                test_reader = self.getSimpleFileReader(test_file_type, False)

                _, _parser_err_listener, _lexer_err_listener = test_reader.parse(test_line, None, isFilePath=False)

                _has_lexer_error = _lexer_err_listener is not None and _lexer_err_listener.getMessageList() is not None
                _has_parser_error = _parser_err_listener is not None and _parser_err_listener.getMessageList() is not None

                if not _has_lexer_error and not _has_parser_error:

                    if self.__debug:
                        self.__lfh.write('PEEL-MR-EXIT #2\n')

                    return self.__divideLegacyMr(file_path, file_type, err_desc, src_path, offset) | corrected

            _, parser_err_listener, lexer_err_listener = reader.parse(test_line, None, isFilePath=False)
            has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None
            has_parser_error = parser_err_listener is not None and parser_err_listener.getMessageList() is not None

            if has_lexer_error or not has_parser_error:

                if self.__debug:
                    self.__lfh.write('PEEL-MR-EXIT #3\n')

                return False | corrected

        i = j = j2 = j3 = 0

        interval = []

        is_done = False

        if not xplor_file_type:

            prev_input = None

            with open(file_path, 'r') as ifh:
                for line in ifh:
                    i += 1
                    if i < err_line_number - MR_MAX_SPACER_LINES:
                        continue
                    if i < err_line_number - 1:
                        interval.append({'line': line,
                                         'ws_or_comment': line.isspace() or bool(comment_pattern.match(line))
                                         or (gromacs_file_type and bool(gromacs_comment_pattern.match(line)))})
                        continue
                    if i == err_line_number - 1:
                        prev_input = line
                        break

            if prev_input is not None:
                listener, parser_err_listener, lexer_err_listener = reader.parse(prev_input, None, isFilePath=False)

                has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None
                has_parser_error = parser_err_listener is not None and parser_err_listener.getMessageList() is not None
                has_content = bool(listener is not None and len(listener.getContentSubtype()) > 0)

                if has_lexer_error or has_parser_error or not has_content:

                    test_reader = self.getSimpleFileReader('nm-res-xpl', False)

                    _, _parser_err_listener, _lexer_err_listener = test_reader.parse(prev_input, None, isFilePath=False)

                    _has_lexer_error = _lexer_err_listener is not None and _lexer_err_listener.getMessageList() is not None

                    if not has_lexer_error:
                        err_line_number -= 1

                        for _interval in reversed(interval):
                            if _interval['ws_or_comment']:
                                err_line_number -= 1
                            else:
                                break

                        i = 0

                        with open(file_path, 'r') as ifh, \
                                open(div_src_file, 'w') as ofh, \
                                open(div_try_file, 'w') as ofh3:
                            for line in ifh:
                                i += 1
                                if i < err_line_number:
                                    ofh.write(line)
                                    j += 1
                                    continue
                                ofh3.write(line)
                                j3 += 1

                        is_done = True

        if not is_done:

            i = j = j2 = j3 = 0

            interval.clear()

            is_valid = False
            ws_or_comment = True

            with open(file_path, 'r') as ifh, \
                    open(div_src_file, 'w') as ofh, \
                    open(div_ext_file, 'w') as ofh2, \
                    open(div_try_file, 'w') as ofh3:
                for line in ifh:
                    i += 1
                    if i < err_line_number - MR_MAX_SPACER_LINES:
                        ofh.write(line)
                        j += 1
                        continue
                    if i < err_line_number:
                        interval.append({'line': line,
                                         'ws_or_comment': line.isspace() or bool(comment_pattern.match(line))
                                         or (gromacs_file_type and bool(gromacs_comment_pattern.match(line)))})
                        if i < err_line_number - 1:
                            continue
                        _k = len(interval) - 1
                        _c = interval[-1]['line'][0]
                        for _interval in reversed(interval):
                            c = _interval['line'][0]
                            if _interval['ws_or_comment'] and {c, _c} != comment_code_mixed_set:
                                _c = c
                                _k -= 1
                                continue
                            break
                        for k, _interval in enumerate(interval):
                            if k <= _k:
                                ofh.write(_interval['line'])
                                j += 1
                            else:
                                ofh2.write(_interval['line'])
                                j2 += 1
                        continue
                    if not is_valid:
                        if line.isspace() or comment_pattern.match(line)\
                           or (gromacs_file_type and gromacs_comment_pattern.match(line)):
                            ofh2.write(line)
                            j2 += 1
                            continue
                        _, parser_err_listener, lexer_err_listener = reader.parse(line, None, isFilePath=False)
                        if lexer_err_listener is None or lexer_err_listener.getMessageList() is not None:
                            ofh2.write(line)
                            j2 += 1
                            continue
                        if parser_err_listener is not None:
                            messageList = parser_err_listener.getMessageList()
                            if messageList is not None and messageList[0]['line_number'] == 1:
                                ofh2.write(line)
                                j2 += 1
                                continue
                        is_valid = True
                    if ws_or_comment:
                        if line.isspace() or comment_pattern.match(line)\
                           or (gromacs_file_type and gromacs_comment_pattern.match(line)):
                            ofh2.write(line)
                            j2 += 1
                            continue
                    if cyana_unset_info_pattern.match(line) or cyana_print_pattern.match(line):
                        ofh2.write(line)
                        j2 += 1
                        continue
                    ws_or_comment = False
                    ofh3.write(line)
                    j3 += 1

        offset += j + j2

        if j == 0:
            if div_src:
                os.remove(file_path)
            if os.path.exists(div_try_file):
                os.remove(div_try_file)

            if j3 > 0:
                if self.__debug:
                    self.__lfh.write('PEEL-MR-EXIT #5\n')

                return False | corrected

            if os.path.getsize(div_src_file) == 0:
                if os.path.exists(div_src_file):  # remove empty file
                    os.remove(div_src_file)

                os.rename(div_ext_file, div_ext_file.replace('dst-div_ext.mr', '_ext.mr'))  # shrink div_ext file name

                if self.__debug:
                    self.__lfh.write('PEEL-MR-EXIT #6\n')

                return True

        if not os.path.exists(div_try_file):
            return False

        file_name = os.path.basename(div_try_file)

        _, _, valid_types, possible_types =\
            self.detectOtherPossibleFormatAsErrorOfLegacyMr(div_try_file if j3 > 0 else div_ext_file, file_name, 'nm-res-mr', [], True)

        len_valid_types = len(valid_types)
        len_possible_types = len(possible_types)

        if len_valid_types == 0 and len_possible_types == 0:

            if err_column_position > 0 and not err_input[0:err_column_position].isspace():
                test_line = err_input[0:err_column_position]

                if reader is None:
                    reader = self.getSimpleFileReader(file_type, False)

                _, _, lexer_err_listener = reader.parse(test_line, None, isFilePath=False)

                has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None

                if not has_lexer_error:

                    _file_type = get_peak_list_format_from_string(err_input, asCode=True)

                    if j3 == 0 and _file_type is not None:
                        shutil.copyfile(div_ext_file, div_ext_file + f'-selected-as-{_file_type[-7:]}')
                        os.remove(div_try_file)
                        os.remove(file_path)

                        corrected = True

                    else:
                        os.remove(div_src_file)
                        if os.path.exists(div_ext_file):
                            os.remove(div_ext_file)
                        os.remove(div_try_file)

                    if self.__debug:
                        self.__lfh.write('PEEL-MR-EXIT #7\n')

                    return False | corrected  # not split MR file because of the lexer errors to be handled by manual

            if div_src:
                os.remove(file_path)
            with open(div_try_file, 'r') as ifh, \
                    open(div_ext_file, 'a') as ofh:
                for line in ifh:
                    ofh.write(line)
            os.remove(div_try_file)

            if self.__debug:
                self.__lfh.write('PEEL-MR-EXIT #8\n')

            return True  # succeeded in eliminating uninterpretable parts

        if len_possible_types > 0:
            os.remove(div_src_file)
            os.remove(div_ext_file)
            os.remove(div_try_file)

            if self.__debug:
                self.__lfh.write('PEEL-MR-EXIT #9\n')

            return False | corrected

        if div_src:
            os.remove(file_path)

        os.rename(div_try_file if j3 > 0 else div_ext_file, div_dst_file)

        if j3 == 0:
            os.remove(div_try_file)

        if self.__debug:
            self.__lfh.write(f'{valid_types} {possible_types}\n')

        file_path = div_dst_file

        if len_valid_types == 1:
            file_type = valid_types[0]

        elif len_valid_types == 2:
            if 'nm-res-cns' in valid_types and 'nm-res-xpl' in valid_types:
                file_type = 'nm-res-xpl'

            elif 'nm-res-cya' in valid_types:
                file_type = next(valid_type for valid_type in valid_types if valid_type != 'nm-res-cya')

            elif 'nm-res-cya' in valid_types and 'nm-res-ros' in valid_types:
                file_type = 'nm-res-ros'

        elif len_valid_types == 3:
            set_valid_types = set(valid_types)
            if set_valid_types in ({'nm-res-cya', 'nm-res-cns', 'nm-res-xpl'},
                                   {'nm-res-isd', 'nm-res-cns', 'nm-res-xpl'}):
                file_type = 'nm-res-xpl'

            elif set_valid_types == {'nm-res-cha', 'nm-res-cns', 'nm-res-xpl'}:
                file_type = 'nm-res-cha'

            elif set_valid_types == {'nm-res-cya', 'nm-res-cns', 'nm-res-xpl'}:
                file_type = 'nm-res-xpl'

        if self.__debug:
            self.__lfh.write(f' -> {file_type}\n')

        self.__testFormatValidityOfLegacyMr(file_path, file_type, src_path, offset)

        if self.__debug:
            self.__lfh.write('PEEL-MR-DONE\n')

        return True

    def __divideLegacyMr(self, file_path: str, file_type: str, err_desc: dict, src_path: str, offset: int) -> bool:
        """ Divive legacy restraint file.
        """

        src_basename = os.path.splitext(file_path)[0]
        div_src = 'div_dst' in src_basename
        div_src_file = src_basename + '-div_src.mr'
        div_ext_file = src_basename + '-div_ext.mr'
        div_try_file = src_basename + '-div_try.mr'
        div_dst_file = src_basename + '-div_dst.mr'

        if self.__debug:
            self.__lfh.write('DO-DIV-MR\n')

        if file_type not in parsable_mr_file_types:
            return False

        err_message = err_desc['message']
        err_line_number = err_desc['line_number']
        err_column_position = err_desc['column_position']
        err_input = err_desc.get('input', '')

        if 0 in (err_column_position, len(err_input)):

            if self.__debug:
                self.__lfh.write('DO-DIV-MR-EXIT #1\n')

            return False

        xplor_file_type = file_type in ('nm-res-xpl', 'nm-res-cns')
        amber_file_type = file_type == 'nm-res-amb'
        gromacs_file_type = file_type in ('nm-res-gro', 'nm-aux-gro')

        xplor_missing_end = xplor_file_type and err_message.startswith(xplor_missing_end_err_msg)
        xplor_ends_wo_statement = xplor_file_type and (bool(xplor_extra_end_err_msg_pattern.match(err_message))
                                                       or (err_message.startswith(no_viable_alt_err_msg)
                                                           and xplor_end_pattern.match(err_input)))

        xplor_l_paren_wo_assi = xplor_file_type and bool(xplor_extra_l_paren_err_msg_pattern.match(err_message))
        xplor_00_origin = xplor_file_type and err_message.startswith(no_viable_alt_err_msg) and ' 00' in err_input

        amber_missing_end = amber_file_type and err_message.startswith(amber_missing_end_err_msg)
        amber_ends_wo_statement = amber_file_type and (bool(amber_extra_end_err_msg_pattern.match(err_message))
                                                       or (err_message.startswith(no_viable_alt_err_msg)
                                                           and amber_end_pattern.match(err_input)))

        concat_xplor_assi = (xplor_file_type
                             and (err_message.startswith(mismatched_input_err_msg)
                                  or err_message.startswith(extraneous_input_err_msg))
                             and bool(xplor_assi_pattern.search(err_input))
                             and not bool(xplor_class_pattern.search(err_input)))
        concat_xplor_rest = (xplor_file_type
                             and (err_message.startswith(mismatched_input_err_msg)
                                  or err_message.startswith(extraneous_input_err_msg))
                             and bool(xplor_rest_pattern.search(err_input)))
        concat_xplor_set = (xplor_file_type
                            and (err_message.startswith(mismatched_input_err_msg)
                                 or err_message.startswith(extraneous_input_err_msg))
                            and bool(xplor_set_pattern.search(err_input))
                            and get_peak_list_format_from_string(err_input) is None)
        concat_amber_rst = (amber_file_type
                            and (err_message.startswith(mismatched_input_err_msg)
                                 or err_message.startswith(extraneous_input_err_msg))
                            and bool(amber_rst_pattern.search(err_input))
                            and not bool(amber_rst_pattern.match(err_input)))

        concat_comment = (file_type in linear_mr_file_types
                          and err_message.startswith(no_viable_alt_err_msg)
                          and bool(comment_pattern.search(err_input)))

        if concat_xplor_assi and bool(xplor_assi_pattern.match(err_input)):
            if expecting_l_paren in err_message:
                xplor_missing_end = True
                concat_xplor_assi = False
            if concat_xplor_rest or concat_xplor_set:
                concat_xplor_assi = False

        reader = prev_input = None

        i = j = 0

        ws_or_comment = True

        with open(file_path, 'r') as ifh, \
                open(div_src_file, 'w') as ofh, \
                open(div_try_file, 'w') as ofh2:
            for line in ifh:
                i += 1
                if i < err_line_number:
                    if ws_or_comment:
                        if line.isspace() or comment_pattern.match(line)\
                           or (gromacs_file_type and gromacs_comment_pattern.match(line)):
                            pass
                        else:
                            ws_or_comment = False
                    if i == err_line_number - 1:
                        prev_input = line
                    ofh.write(line)
                    j += 1
                    continue
                if i == err_line_number:
                    ofh.write(line[0:err_column_position] + '\n')
                    j += 1
                    ofh2.write(line[err_column_position:])
                    continue
                ofh2.write(line)

        offset += err_line_number - 1

        xplor_missing_end_before = (xplor_file_type and err_message.startswith(mismatched_input_err_msg)
                                    and not bool(xplor_expecting_symbol_pattern.search(err_message))  # exclude syntax errors in a factor
                                    and prev_input is not None and bool(xplor_assi_pattern.search(prev_input)))

        xplor_no_syntax_err_in_fac_or_ann = not bool(xplor_expecting_equ_op_pattern.search(err_message))\
            and not bool(xplor_expecting_seg_id_pattern.search(err_message))\
            and not err_message.startswith(no_viable_alt_err_msg)

        amber_missing_comma_before = (amber_file_type and err_message.startswith(mismatched_input_err_msg)
                                      and bool(amber_expecting_comma_pattern.search(err_message)))

        if (xplor_missing_end or xplor_ends_wo_statement
                or xplor_l_paren_wo_assi or xplor_00_origin
                or xplor_missing_end_before
                or amber_missing_end or amber_ends_wo_statement
                or amber_missing_comma_before
                or concat_xplor_assi or concat_xplor_rest or concat_xplor_set
                or concat_amber_rst
                or concat_comment) or i <= err_line_number or j == 0:

            corrected = False

            if err_line_number - 1 in (i, j) and xplor_l_paren_wo_assi:  # this should be before 'concat_comment' routine

                if os.path.exists(div_src_file):
                    os.remove(div_src_file)
                if os.path.exists(div_try_file):
                    os.remove(div_try_file)

                if prev_input is not None:
                    err_desc['previous_input'] = f"Do you need to comment out the succeeding lines as well?\n{prev_input}"

                if self.__debug and not corrected:
                    self.__lfh.write('DO-DIV-MR-EXIT #2-1\n')

                return False

            if xplor_00_origin:

                cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                if cor_src_path is not None:

                    with open(src_path, 'r') as ifh, \
                            open(cor_src_path, 'w') as ofh:
                        for line in ifh:
                            if ' 00' in line:
                                ofh.write(re.sub(r' 00', ' OO', line))
                            else:
                                ofh.write(line)

                    if cor_test:
                        os.rename(cor_src_path, src_path)

                    if self.__debug:
                        self.__lfh.write('DO-DIV-MR-EXIT #2-2\n')

                    corrected = True

            if xplor_ends_wo_statement or amber_ends_wo_statement:

                has_end_tag = False

                k = 0

                with open(src_path, 'r') as ifh:
                    for line in ifh:
                        if k == offset:
                            if xplor_ends_wo_statement and xplor_end_pattern.match(line):
                                has_end_tag = True
                            if amber_ends_wo_statement and amber_end_pattern.match(line):
                                has_end_tag = True
                            break
                        k += 1

                if has_end_tag:

                    cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                    if cor_src_path is not None:

                        k = 0

                        with open(src_path, 'r') as ifh, \
                                open(cor_src_path, 'w') as ofh:
                            for line in ifh:
                                if k == offset:
                                    ofh.write('#' + line)
                                else:
                                    ofh.write(line)
                                k += 1

                        if cor_test:
                            os.rename(cor_src_path, src_path)

                        if self.__debug:
                            self.__lfh.write('DO-DIV-MR-EXIT #2-3\n')

                        corrected = True

            if concat_xplor_assi or concat_xplor_rest or concat_xplor_set or concat_amber_rst:

                code_index = -1

                if concat_xplor_assi:
                    for m in xplor_any_assi_pattern.finditer(err_input):
                        code_index = m.start()
                elif concat_xplor_rest:
                    for m in xplor_any_rest_pattern.finditer(err_input):
                        code_index = m.start()
                elif concat_xplor_set:
                    for m in xplor_any_set_pattern.finditer(err_input):
                        code_index = m.start()
                elif concat_amber_rst:
                    for m in amber_rst_pattern.finditer(err_input):
                        code_index = m.start()

                if code_index != -1:
                    test_line = err_input[0:code_index]

                    if len(test_line.strip()) > 0:
                        typo_for_comment_out = bool(possible_typo_for_comment_out_pattern.match(test_line))

                        if reader is None:
                            reader = self.getSimpleFileReader(file_type, False)

                        _, parser_err_listener, lexer_err_listener = reader.parse(test_line, None, isFilePath=False)

                        has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None

                        if not has_lexer_error:

                            cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                            if cor_src_path is not None:

                                k = 0

                                with open(src_path, 'r') as ifh, \
                                        open(cor_src_path, 'w') as ofh:
                                    for line in ifh:
                                        if k == offset:
                                            if typo_for_comment_out:
                                                g = possible_typo_for_comment_out_pattern.search(test_line).groups()
                                                if g[0] == '1':
                                                    test_line = re.sub(r'1', '!', test_line)
                                                else:
                                                    test_line = re.sub(r'3', '#', test_line)
                                                ofh.write(f"{test_line}{err_input[code_index:]}\n")
                                            else:
                                                ofh.write(f"{test_line}\n{err_input[code_index:]}\n")
                                        else:
                                            ofh.write(line)
                                        k += 1

                                if cor_test:
                                    os.rename(cor_src_path, src_path)

                                if self.__debug:
                                    self.__lfh.write('DIV-MR-EXIT #2-4\n')

                                corrected = True

            if concat_comment:

                comment_code_index = -1
                if '#' in err_input:
                    comment_code_index = err_input.index('#')
                if '!' in err_input:
                    if comment_code_index == -1:
                        comment_code_index = err_input.index('!')
                    elif err_input.index('!') < comment_code_index:
                        comment_code_index = err_input.index('!')

                if comment_code_index != -1:
                    test_line = err_input[0:comment_code_index]

                    if reader is None:
                        reader = self.getSimpleFileReader(file_type, False)

                    _, parser_err_listener, lexer_err_listener = reader.parse(test_line, None, isFilePath=False)

                    has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None
                    has_parser_error = parser_err_listener is not None and parser_err_listener.getMessageList() is not None

                    if not has_lexer_error and not has_parser_error:

                        cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                        if cor_src_path is not None:

                            k = 0

                            with open(src_path, 'r') as ifh, \
                                    open(cor_src_path, 'w') as ofh:
                                for line in ifh:
                                    if k == offset:
                                        ofh.write(f"{test_line} {err_input[comment_code_index:]}\n")
                                    else:
                                        ofh.write(line)
                                    k += 1

                            if cor_test:
                                os.rename(cor_src_path, src_path)

                            if self.__debug:
                                self.__lfh.write('DO-DIV-MR-EXIT #2-5\n')

                            corrected = True

            if err_line_number - 1 in (i, j) and (xplor_missing_end or xplor_missing_end_before):

                if not xplor_missing_end_before or xplor_no_syntax_err_in_fac_or_ann:

                    cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                    if cor_src_path is not None:

                        middle = i != err_line_number - 1
                        is_done = False

                        k = 0 if xplor_missing_end else 1

                        with open(src_path, 'r') as ifh, \
                                open(cor_src_path, 'w') as ofh:
                            for line in ifh:
                                if middle:
                                    if k == err_line_number - 2 and comment_pattern.match(line):
                                        ofh.write('end\n')
                                        is_done = True
                                    elif k == err_line_number - 1 and not is_done:
                                        ofh.write('end\n')
                                ofh.write(line)
                                k += 1
                            if not middle:
                                ofh.write('end\n')

                        if cor_test:
                            os.rename(cor_src_path, src_path)

                        if self.__debug:
                            self.__lfh.write('DO-DIV-MR-EXIT #2-6\n')

                        corrected = True

            if err_line_number - 1 in (i, j) and amber_missing_comma_before:

                cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                if cor_src_path is not None:

                    k = 1

                    with open(src_path, 'r') as ifh, \
                            open(cor_src_path, 'w') as ofh:
                        for line in ifh:
                            if k == err_line_number:
                                ofh.write(',' + line)
                            else:
                                ofh.write(line)
                            k += 1

                    if cor_test:
                        os.rename(cor_src_path, src_path)

                    if self.__debug:
                        self.__lfh.write('DIV-MR-EXIT #2-7\n')

                    corrected = True

            if i == err_line_number - 1 and amber_missing_end:

                cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                if cor_src_path is not None:

                    with open(src_path, 'r') as ifh, \
                            open(cor_src_path, 'w') as ofh:
                        for line in ifh:
                            ofh.write(line)
                        ofh.write('&end\n')

                    if cor_test:
                        os.rename(cor_src_path, src_path)

                    if self.__debug:
                        self.__lfh.write('DO-DIV-MR-EXIT #2-8\n')

                    corrected = True

            if not (corrected or concat_xplor_assi or concat_xplor_rest or concat_xplor_set or concat_amber_rst)\
               and j in (0, err_line_number - 1)\
               and (not xplor_missing_end_before or xplor_no_syntax_err_in_fac_or_ann):
                test_line = err_input

                if reader is None:
                    reader = self.getSimpleFileReader(file_type, False)

                _, _, lexer_err_listener = reader.parse(test_line, None, isFilePath=False)

                has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None

                if not has_lexer_error:

                    cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                    if cor_src_path is not None:

                        k = 0

                        with open(src_path, 'r') as ifh, \
                                open(cor_src_path, 'w') as ofh:
                            for line in ifh:
                                if k == offset:
                                    ofh.write('#' + line)
                                else:
                                    ofh.write(line)
                                k += 1

                        if cor_test:
                            os.rename(cor_src_path, src_path)

                        if self.__debug:
                            self.__lfh.write('DO-DIV-MR-EXIT #2-9\n')

                        corrected = True

            if os.path.exists(div_src_file):
                os.remove(div_src_file)
            if os.path.exists(div_try_file):
                os.remove(div_try_file)

            if self.__debug and not corrected:
                self.__lfh.write('DO-DIV-MR-EXIT #2-10\n')

            return corrected

        if ws_or_comment:
            os.remove(div_src_file)
            os.remove(div_try_file)

            if self.__debug:
                self.__lfh.write('DO-DIV-MR-EXIT #3\n')

            return False

        if not os.path.exists(div_try_file):
            return False

        file_name = os.path.basename(div_try_file)

        _, _, valid_types, possible_types = self.detectOtherPossibleFormatAsErrorOfLegacyMr(div_try_file, file_name, 'nm-res-mr', [], True)

        len_valid_types = len(valid_types)
        len_possible_types = len(possible_types)

        if len_valid_types == 0 and len_possible_types == 0:

            if xplor_file_type and bool(xplor_assi_pattern.search(err_input)):

                if prev_input is not None and err_message.startswith(extraneous_input_err_msg):
                    err_desc['previous_input'] = prev_input

                os.remove(div_src_file)
                os.remove(div_try_file)

                if self.__debug:
                    self.__lfh.write('DO-DIV-MR-EXIT #4\n')

                return False

            if div_src:
                os.remove(file_path)
            os.rename(div_try_file, div_ext_file)

            if self.__debug:
                self.__lfh.write('DO-DIV-MR-EXIT #5\n')

            return True  # succeeded in eliminating uninterpretable parts

        if len_possible_types > 0:
            os.remove(div_src_file)
            os.remove(div_try_file)

            if self.__debug:
                self.__lfh.write('DO-DIV-MR-EXIT #6\n')

            return False

        if div_src:
            os.remove(file_path)

        os.rename(div_try_file, div_dst_file)

        if self.__debug:
            self.__lfh.write(f'{valid_types} {possible_types}\n')

        file_path = div_dst_file

        if len_valid_types == 1:
            file_type = valid_types[0]

        elif len_valid_types == 2:
            if 'nm-res-cns' in valid_types and 'nm-res-xpl' in valid_types:
                file_type = 'nm-res-xpl'

            elif 'nm-res-cya' in valid_types:
                file_type = next(valid_type for valid_type in valid_types if valid_type != 'nm-res-cya')

            elif 'nm-res-cya' in valid_types and 'nm-res-ros' in valid_types:
                file_type = 'nm-res-ros'

        elif len_valid_types == 3:
            set_valid_types = set(valid_types)
            if set_valid_types in ({'nm-res-cya', 'nm-res-cns', 'nm-res-xpl'},
                                   {'nm-res-isd', 'nm-res-cns', 'nm-res-xpl'}):
                file_type = 'nm-res-xpl'

            elif set_valid_types == {'nm-res-cha', 'nm-res-cns', 'nm-res-xpl'}:
                file_type = 'nm-res-cha'

            elif set_valid_types == {'nm-res-cya', 'nm-res-cns', 'nm-res-xpl'}:
                file_type = 'nm-res-xpl'

        if self.__debug:
            self.__lfh.write(f' -> {file_type}\n')

        self.__testFormatValidityOfLegacyMr(file_path, file_type, src_path, offset)

        if self.__debug:
            self.__lfh.write('DO-DIV-MR-DONE\n')

        return True

    def __testFormatValidityOfLegacyMr(self, file_path: str, file_type: str, src_path: str, offset: int):
        """ Perform format check of a given MR file, then split MR recursively if necessary.
        """

        div_test = False

        try:

            reader = self.getSimpleFileReader(file_type, False, sll_pred=False)

            listener, parser_err_listener, lexer_err_listener = reader.parse(file_path, None)

            if listener is not None:
                if file_type in retrial_mr_file_types:
                    reasons = listener.getReasonsForReparsing()

                    if reasons is not None:
                        reader = self.getSimpleFileReader(file_type, False, sll_pred=False, reasons=reasons)

                        listener, parser_err_listener, lexer_err_listener = reader.parse(file_path, None)

            has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None
            has_parser_error = parser_err_listener is not None and parser_err_listener.getMessageList() is not None
            has_content = bool(listener is not None and len(listener.getContentSubtype()) > 0)

            if has_lexer_error and has_parser_error and has_content:
                # parser error occurrs before occurrenece of lexer error that implies mixing of different MR formats in a file
                if lexer_err_listener.getErrorLineNumber()[0] > parser_err_listener.getErrorLineNumber()[0]:
                    self.peelLegacyMrIfNecessary(file_path, file_type,
                                                 parser_err_listener.getMessageList()[0],
                                                 src_path, offset)
                    div_test = True

            fixed_line_num = -1

            if has_lexer_error:
                messageList = lexer_err_listener.getMessageList()

                for description in messageList:
                    if 'input' in description:
                        enc = detect_encoding(description['input'])
                        if enc is not None and enc != 'ascii':
                            pass
                        elif not div_test and has_content:
                            fixed = self.divideLegacyMrIfNecessary(file_path, file_type, description, src_path, offset)
                            if fixed:
                                fixed_line_num = description['line_number']
                            div_test = file_type != 'nm-res-amb'  # remediate missing comma issue in AMBER MR

            if has_parser_error:
                messageList = parser_err_listener.getMessageList()

                for description in messageList:
                    if 0 < fixed_line_num <= description['line_number']:
                        div_test = True
                    if 'input' in description:
                        if not div_test and has_content:
                            self.divideLegacyMrIfNecessary(file_path, file_type, description, src_path, offset)
                            div_test = True
                    elif not div_test and has_content and file_type in ('nm-res-xpl', 'nm-res-cns'):
                        self.divideLegacyMrIfNecessary(file_path, file_type, description, str(file_path), offset)
                        div_test = True

        except ValueError as e:

            self.report.error.appendDescription('internal_error', f"+{self.__class_name__}.__testFormatValidityOfLegacyMr() ++ Error  - " + str(e))
            self.report.setError()

            if self.__verbose:
                self.__lfh.write(f"+{self.__class_name__}.__testFormatValidityOfLegacyMr() ++ Error  - {str(e)}\n")

    def detectOtherPossibleFormatAsErrorOfLegacyMr(self, file_path: str, file_name: str, file_type: str,
                                                   dismiss_err_lines: List[int], multiple_check: bool = False
                                                   ) -> Tuple[bool, str, List[str], List[str]]:
        """ Report other possible format as error of a given legacy restraint file.
        """

        is_valid = agreed_w_cns = False
        err = ''
        genuine_type = []
        valid_types, possible_types = {}, {}

        if (not is_valid or multiple_check) and file_type != 'nm-res-xpl':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-res-xpl',
                                                                    agreed_w_cns=agreed_w_cns)

            is_valid |= _is_valid
            agreed_w_cns |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if len(genuine_type) > 0:
            multiple_check = False

        if (not is_valid or multiple_check) and file_type != 'nm-res-cns':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-res-cns',
                                                                    agreed_w_cns=agreed_w_cns)

            is_valid |= _is_valid
            agreed_w_cns |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if (not is_valid or 'Syntax error' in err) and file_type != 'nm-res-cha':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-res-cha',
                                                                    agreed_w_cns=agreed_w_cns)

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if len(genuine_type) > 0:
            multiple_check = False

        if (not is_valid or multiple_check) and file_type != 'nm-res-amb':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-res-amb')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
                multiple_check = False
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if (not is_valid or multiple_check) and file_type != 'nm-aux-amb':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-aux-amb')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
                multiple_check = False
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if (not is_valid or multiple_check) and file_type != 'nm-res-ari':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-res-ari')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
                multiple_check = False
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if (not is_valid or multiple_check) and file_type != 'nm-res-arx':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-res-arx')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
                multiple_check = False
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if (not is_valid or multiple_check) and file_type != 'nm-res-bio':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-res-bio')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)
        # """ conflict with nm-res-cya (2kcp)
        # if (not is_valid or multiple_check) and file_type != 'nm-aux-cha':
        #     _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
        #         self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-aux-cha')
        #
        #     is_valid |= _is_valid
        #     err += _err
        #     if _genuine_type is not None:
        #         genuine_type.append(_genuine_type)
        #     valid_types.update(_valid_types)
        #     possible_types.update(_possible_types)
        # """
        if (not is_valid or multiple_check) and file_type != 'nm-res-dyn':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-res-dyn')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
                multiple_check = False
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if (not is_valid or multiple_check) and file_type != 'nm-res-gro':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-res-gro')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
                multiple_check = False
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if (not is_valid or multiple_check) and file_type != 'nm-aux-gro':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-aux-gro')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
                multiple_check = False
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if (not is_valid or multiple_check) and file_type != 'nm-res-isd':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-res-isd')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
                multiple_check = False
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if (not is_valid or multiple_check) and file_type != 'nm-aux-pdb':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-aux-pdb')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
                multiple_check = False
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if (not is_valid or multiple_check) and file_type != 'nm-res-ros':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-res-ros')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if (not is_valid or multiple_check) and file_type != 'nm-res-sch':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-res-sch',
                                                                    agreed_w_cns=agreed_w_cns)

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if (not is_valid or multiple_check) and file_type != 'nm-res-syb':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-res-syb')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if not is_valid and file_type != 'nm-res-noa':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-res-noa')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
                multiple_check = False
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        # prevent 'nm-pea-any' occasionally matches with 'nm-res-cya' (DAOTHER-9425)
        if (not is_valid or multiple_check) and file_type not in ('nm-res-cya', 'nm-pea-any'):
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-res-cya')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None and 'nm-res-noa' not in genuine_type:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        _file_type = get_peak_list_format(file_path, True)

        if _file_type == 'nm-pea-ari' and file_type != 'nm-pea-ari':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-pea-ari')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if _file_type == 'nm-pea-ccp' and file_type != 'nm-pea-ccp':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-pea-ccp')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if _file_type == 'nm-pea-oli' and file_type != 'nm-pea-oli':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-pea-oli')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if _file_type == 'nm-pea-pip' and file_type != 'nm-pea-pip':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-pea-pip')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if _file_type == 'nm-pea-pon' and file_type != 'nm-pea-pon':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-pea-pon')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if _file_type == 'nm-pea-spa' and file_type != 'nm-pea-spa':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-pea-spa')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if _file_type == 'nm-pea-sps' and file_type != 'nm-pea-sps':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-pea-sps')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if _file_type == 'nm-pea-top' and file_type != 'nm-pea-top':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-pea-top')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if _file_type == 'nm-pea-vie' and file_type != 'nm-pea-vie':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-pea-vie')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if _file_type == 'nm-pea-vnm' and file_type != 'nm-pea-vnm':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-pea-vnm')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if _file_type == 'nm-pea-xea' and file_type != 'nm-pea-xea':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-pea-xea')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if _file_type == 'nm-pea-xwi' and file_type != 'nm-pea-xwi':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-pea-xwi')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if not is_valid and _file_type is None and file_type != 'nm-aux-xea':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-aux-xea')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if not is_valid and _file_type is None and file_type != 'nm-pea-bar':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines, 'nm-pea-bar')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if len(genuine_type) != 1:
            _valid_types = [k for k, v in sorted(valid_types.items(), key=itemgetter(1), reverse=True)]
            _possible_types = [k for k, v in sorted(possible_types.items(), key=itemgetter(1), reverse=True)]

        else:
            _valid_types = [genuine_type[0]]
            _possible_types = []

        return is_valid, err, _valid_types, _possible_types

    def __detectOtherPossibleFormatAsErrorOfLegacyMr__(self, file_path: str, file_name: str, file_type: str, dismiss_err_lines: List[int],
                                                       _file_type: str, agreed_w_cns: bool = False
                                                       ) -> Tuple[bool, str, Optional[str], dict, dict]:
        """ Report other possible format as error of a given legacy restraint file.
        """

        _mr_format_name = getRestraintFormatName(file_type)
        mr_format_name = _mr_format_name.split()[0]

        __mr_format_name = getRestraintFormatName(_file_type, True)
        _mr_format_name = __mr_format_name.split()[0]
        _a_mr_format_name = ('an ' if _mr_format_name[0] in ('AINMX') else 'a ') + __mr_format_name

        is_valid = False
        err = ''
        genuine_type = None
        valid_types, possible_types = {}, {}

        try:

            sll_pred = not agreed_w_cns

            reader = self.getSimpleFileReader(_file_type, False, sll_pred=sll_pred)

            listener, parser_err_listener, lexer_err_listener = reader.parse(file_path, None)

            has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None
            has_parser_error = parser_err_listener is not None and parser_err_listener.getMessageList() is not None

            if (has_lexer_error or has_parser_error) and sll_pred\
               and _file_type in ('nm-res-xpl', 'nm-res-cns', 'nm-res-cha'):
                sll_pred = False

                reader.setSllPredMode(sll_pred)

                listener, parser_err_listener, lexer_err_listener = reader.parse(file_path, None)

                has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None
                has_parser_error = parser_err_listener is not None and parser_err_listener.getMessageList() is not None

            if file_path not in self.__sll_pred_holder:
                self.__sll_pred_holder[file_path] = {}

            if not has_lexer_error and not has_parser_error:
                self.__sll_pred_holder[file_path][_file_type] = sll_pred

            # 'rdc_restraint' occasionally matches with CYANA restraints
            # 'geo_restraint' include CS-ROSETTA disulfide bond linkage, which matches any integer array
            if _file_type == 'nm-res-ros':
                _content_subtype = listener.getEffectiveContentSubtype() if listener is not None else None
            else:
                _content_subtype = listener.getContentSubtype() if listener is not None else None
            if _content_subtype is not None and len(_content_subtype) == 0:
                _content_subtype = None
            has_content = _content_subtype is not None

            if None not in (lexer_err_listener, parser_err_listener, listener)\
               and ((lexer_err_listener.getMessageList() is None and parser_err_listener.getMessageList() is None) or has_content):

                if has_content or file_type != 'nm-res-oth':

                    is_valid = True
                    if (has_lexer_error or has_parser_error) and _file_type == 'nm-aux-xea':  # 2lcn
                        is_valid = False

                    err = f"The restraint file {file_name!r} ({mr_format_name}) looks like {_a_mr_format_name} file, "\
                          f"which has {concat_restraint_names(_content_subtype)}. "\
                          "Did you accidentally select wrong format? Please re-upload the restraint file."

                    if has_content:
                        _err = ''
                        if lexer_err_listener is not None:
                            messageList = lexer_err_listener.getMessageList()

                            if messageList is not None:
                                for description in messageList:
                                    if description['line_number'] in dismiss_err_lines:
                                        continue
                                    _err = f"[Syntax error as {_a_mr_format_name} file] "\
                                           f"line {description['line_number']}:{description['column_position']} {description['message']}\n"
                                    if 'input' in description:
                                        enc = detect_encoding(description['input'])
                                        is_not_ascii = False
                                        if enc is not None and enc != 'ascii':
                                            _err += f"{description['input']}\n".encode().decode('ascii', 'backslashreplace')
                                            is_not_ascii = True
                                        else:
                                            _err += f"{description['input']}\n"
                                        _err += f"{description['marker']}\n"
                                        if is_not_ascii:
                                            _err += f"[Unexpected text encoding] Encoding used in the above line is {enc!r} and must be 'ascii'.\n"

                        if parser_err_listener is not None and len(_err) == 0:
                            messageList = parser_err_listener.getMessageList()

                            if messageList is not None:
                                for description in messageList:
                                    if description['line_number'] in dismiss_err_lines:
                                        continue
                                    _err += f"[Syntax error as {_a_mr_format_name} file] "\
                                            f"line {description['line_number']}:{description['column_position']} {description['message']}\n"
                                    if 'input' in description:
                                        _err += f"{description['input']}\n"
                                        _err += f"{description['marker']}\n"

                        if len(_err) > 0:
                            err += f"\nEven assuming that the format is the {_mr_format_name!r}, the following issues need to be fixed.\n" + _err[:-1]
                        elif file_type != 'nm-res-oth' and (lexer_err_listener.getMessageList() is not None or parser_err_listener.getMessageList() is not None):
                            is_valid = False
                            err = ''

                        if is_valid:
                            if has_content and lexer_err_listener.getMessageList() is None and parser_err_listener.getMessageList() is None:
                                genuine_type = _file_type
                            valid_types[_file_type] = len(_content_subtype)
                        elif _file_type != 'nm-aux-xea':  # 2lcn
                            possible_types[_file_type] = len(_content_subtype)

                    if file_type == 'nm-res-oth':
                        self.report.error.appendDescription('content_mismatch',
                                                            {'file_name': file_name, 'description': err})
                        self.report.setError()

                        if self.__verbose:
                            self.__lfh.write(f"+{self.__class_name__}.detectOtherPossibleFormatAsErrorOfLegacyMr() ++ Error  - {err}\n")

        except ValueError:
            pass

        return is_valid, err, genuine_type, valid_types, possible_types

    def retrieveOriginalFileExtensionOfCyanaMrFile(self) -> Optional[str]:
        """ Retrieve original file extension of CYANA MR file.
        """

        if self.__cur_original_ar_file_name is None:
            return None

        if self.__cur_original_ar_file_name.endswith('.gz'):
            self.__cur_original_ar_file_name = os.path.splitext(self.__cur_original_ar_file_name)[0]

        if self.__cur_original_ar_file_name.endswith('.mr'):
            return None

        if self.__cur_original_ar_file_name.endswith('-corrected'):
            self.__cur_original_ar_file_name = self.__cur_original_ar_file_name.replace('-corrected', '')

        if self.__cur_original_ar_file_name.endswith('.txt'):
            self.__cur_original_ar_file_name = self.__cur_original_ar_file_name.replace('.txt', '')

        if self.__cur_original_ar_file_name.endswith('.tbl'):
            self.__cur_original_ar_file_name = self.__cur_original_ar_file_name.replace('.tbl', '')

        if self.__cur_original_ar_file_name.endswith('.dat'):
            self.__cur_original_ar_file_name = self.__cur_original_ar_file_name.replace('.dat', '')

        if self.__cur_original_ar_file_name.endswith('.10'):
            self.__cur_original_ar_file_name = self.__cur_original_ar_file_name.replace('.10', '')

        split_ext = os.path.splitext(self.__cur_original_ar_file_name)

        if len(split_ext) != 2 or len(split_ext[1]) == 0:

            file_ext = split_ext[0].lower()

            if len(file_ext) > 3:

                file_ext = file_ext[len(file_ext) - 3:]

                if file_ext not in CYANA_MR_FILE_EXTS:
                    return None

                return file_ext

            if len(file_ext) == 3:

                if file_ext not in CYANA_MR_FILE_EXTS:
                    return None

                return file_ext

            return None

        file_ext = split_ext[1][1:].lower()

        if len(file_ext) > 3:
            file_ext = file_ext[:3]

        if file_ext not in CYANA_MR_FILE_EXTS:
            return None

        return file_ext
