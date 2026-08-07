#!/usr/bin/env python3
##
# File: tools/gen_speedy_antlr.py
# Date: 7-Aug-2026
#
# Updates:
""" Generate the speedy-antlr-tool C++ accelerator for a grammar in this package.

    For each requested grammar this
      1. runs the ANTLR tool with the C++ target over the .g4 pair,
      2. runs speedy_antlr_tool.generate() against the *already committed*
         Python parser to emit the sa_<grammar>.py shim and the C++ translator,
      3. patches the generated C++ entry point to use the SLL prediction mode
         when the grammar's Reader does.

    The Python target is deliberately NOT regenerated. The committed
    <Grammar>Lexer.py/<Grammar>Parser.py are byte-identical to a fresh
    'antlr4 -Dlanguage=Python3 -no-visitor' run with ANTLR 4.13.0, and
    regenerating in place would overwrite the hand-written
    <Grammar>ParserListener.py, which shadows ANTLR's generated listener base
    of the same name.

    Requires the 'antlr4-tools' and 'speedy-antlr-tool' packages, and Java
    (antlr4-tools provisions a JRE on first use).

    Usage:
        python3 tools/gen_speedy_antlr.py NmrPipeCS XplorMR
        python3 tools/gen_speedy_antlr.py --all
    @author: Masashi Yokochi
"""
import argparse
import io
import os
import re
import shutil
import subprocess
import sys
import urllib.request
import zipfile

ANTLR_VERSION = '4.13.0'

CPP_RUNTIME_URL = f'https://www.antlr.org/download/antlr4-cpp-runtime-{ANTLR_VERSION}-source.zip'

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NMR_DIR = os.path.join(REPO_DIR, 'wwpdb', 'utils', 'nmr')
GRAMMAR_DIR = os.path.join(REPO_DIR, 'wwpdb', 'utils', 'tests-nmr', f'antlr-grammars-v{ANTLR_VERSION[:4]}')
# The grammars directory is labelled v4.10 but is generated with 4.13.0
if not os.path.isdir(GRAMMAR_DIR):
    GRAMMAR_DIR = os.path.join(REPO_DIR, 'wwpdb', 'utils', 'tests-nmr', 'antlr-grammars-v4.10')
CPP_SRC_DIR = os.path.join(NMR_DIR, 'cpp_src')
CPP_RUNTIME_DIR = os.path.join(CPP_SRC_DIR, 'antlr4-cpp-runtime')

# Grammars bridged to the C++ target.
#   name -> (subpackage, lexer grammar, entry rule, Reader module)
# 'lexer grammar' is spelled out because three parsers borrow another grammar's
# lexer via tokenVocab (NmrViewNPK -> NmrViewPKLexer, SparkyNPK/SparkyRPK ->
# SparkyPKLexer).
GRAMMARS = {
    'NmrPipeCS': ('cs', 'NmrPipeCSLexer', 'nmrpipe_cs', 'NmrPipeCSReader'),
    'XplorMR': ('mr', 'XplorMRLexer', 'xplor_nih_mr', 'XplorMRReader'),
}

# Readers are read in either shape: the original inline ANTLR block, or the
# converted call to AntlrParseUtil.parseAntlr().
#   inline:    tree = parser.<rule>()
#   converted: parseAntlr(<Lexer>, <Parser>, '<rule>', ...)
ENTRY_RULE_PATTERNS = (re.compile(r'^\s*tree\s*=\s*parser\.(\w+)\(\)', re.MULTILINE),
                       re.compile(r'parseAntlr\(\s*\w+\s*,\s*\w+\s*,\s*[\'"](\w+)[\'"]', re.MULTILINE))
# an *uncommented* 'parser._interp.predictionMode = PredictionMode.SLL', or the
# converted 'predictionModeSll=' argument
SLL_PATTERNS = (re.compile(r'^\s*parser\._interp\.predictionMode\s*=\s*PredictionMode\.SLL', re.MULTILINE),
                re.compile(r'predictionModeSll\s*=\s*(?!False\b)', re.MULTILINE))

# The prediction mode has to be settable per call, not baked in at compile time:
# six mr/ Readers (XplorMR, CnsMR, CyanaMR, CharmmMR, SchrodingerMR, CyanaNOA)
# choose it at runtime with 'if not isFilePath or self.__sll_pred', so one
# accelerator has to serve both LL and SLL for the same grammar. speedy-antlr-tool
# offers no hook for this, so do_parse() and the shim's parse() gain a flag.
#
# Each entry is (description, [(old, new), ...]); every replacement must match
# exactly once or generation fails, so a speedy-antlr-tool upgrade cannot
# silently drop the patch.
CPP_PATCHES = [
    ('do_parse() accepts a prediction-mode flag', [
        ('        PyObject *sa_err_listener = NULL;\n',
         '        PyObject *sa_err_listener = NULL;\n'
         '        int use_sll = 0;  // wwPDB: PredictionMode.SLL when true\n'),
        ('            "OOsO:do_parse",\n'
         '            &parser_cls, &stream, &entry_rule_name, &sa_err_listener\n',
         '            "OOsOp:do_parse",\n'
         '            &parser_cls, &stream, &entry_rule_name, &sa_err_listener, &use_sll\n'),
        ('        antlr4::tree::ParseTree *parse_tree;\n',
         '        // wwPDB: mirror the Python driver\'s prediction mode, or the two\n'
         '        // paths accept different inputs and report different errors.\n'
         '        if (use_sll) {\n'
         '            parser.getInterpreter<antlr4::atn::ParserATNSimulator>()\n'
         '                ->setPredictionMode(antlr4::atn::PredictionMode::SLL);\n'
         '        }\n'
         '        antlr4::tree::ParseTree *parse_tree;\n'),
    ]),
]

SHIM_PATCHES = [
    ('parse()/_cpp_parse() forward the prediction-mode flag', [
        ('def parse(stream:InputStream, entry_rule_name:str, sa_err_listener:SA_ErrorListener=None) -> ParseTree:',
         'def parse(stream:InputStream, entry_rule_name:str, sa_err_listener:SA_ErrorListener=None,\n'
         '          prediction_mode_sll:bool=False) -> ParseTree:'),
        ('        return _cpp_parse(stream, entry_rule_name, sa_err_listener)\n'
         '    else:\n'
         '        return _py_parse(stream, entry_rule_name, sa_err_listener)\n',
         '        return _cpp_parse(stream, entry_rule_name, sa_err_listener, prediction_mode_sll)\n'
         '    else:\n'
         '        return _py_parse(stream, entry_rule_name, sa_err_listener, prediction_mode_sll)\n'),
        ('def _cpp_parse(stream:InputStream, entry_rule_name:str, sa_err_listener:SA_ErrorListener=None) -> ParseTree:',
         'def _cpp_parse(stream:InputStream, entry_rule_name:str, sa_err_listener:SA_ErrorListener=None,\n'
         '               prediction_mode_sll:bool=False) -> ParseTree:'),
        ('def _py_parse(stream:InputStream, entry_rule_name:str, sa_err_listener:SA_ErrorListener=None) -> ParseTree:',
         'def _py_parse(stream:InputStream, entry_rule_name:str, sa_err_listener:SA_ErrorListener=None,\n'
         '              prediction_mode_sll:bool=False) -> ParseTree:'),
        ('    parser = %(parser)s(token_stream)\n',
         '    parser = %(parser)s(token_stream)\n'
         '    if prediction_mode_sll:\n'
         '        from antlr4 import PredictionMode\n'
         '        parser._interp.predictionMode = PredictionMode.SLL\n'),
        ('do_parse(%(parser)s, stream, entry_rule_name, sa_err_listener)',
         'do_parse(%(parser)s, stream, entry_rule_name, sa_err_listener, prediction_mode_sll)'),
    ]),
]


def readerFacts(subPackage: str, readerModule: str) -> tuple:
    """ Extract the entry rule and the SLL prediction mode from a Reader module.
        @return: (entry rule name, uses SLL)
    """

    path = os.path.join(NMR_DIR, subPackage, readerModule + '.py')
    with open(path, 'r', encoding='utf-8') as ifh:
        source = ifh.read()

    entryRules = set()
    for pattern in ENTRY_RULE_PATTERNS:
        entryRules.update(pattern.findall(source))
    if len(entryRules) != 1:
        raise RuntimeError(f'{path}: expected exactly one entry rule, found {sorted(entryRules)}.')

    useSll = any(pattern.search(source) is not None for pattern in SLL_PATTERNS)

    return entryRules.pop(), useSll


def fetchCppRuntime() -> None:
    """ Download and unpack the ANTLR4 C++ runtime source, if not already present.
    """

    if os.path.isfile(os.path.join(CPP_RUNTIME_DIR, 'antlr4-runtime.h')):
        return

    print(f'Downloading {CPP_RUNTIME_URL}')
    with urllib.request.urlopen(CPP_RUNTIME_URL) as response:  # nosec - fixed https URL
        payload = response.read()

    os.makedirs(CPP_RUNTIME_DIR, exist_ok=True)
    with zipfile.ZipFile(io.BytesIO(payload)) as zfh:
        for member in zfh.namelist():
            if not member.startswith('runtime/src/') or member.endswith('/'):
                continue
            target = os.path.join(CPP_RUNTIME_DIR, os.path.relpath(member, 'runtime/src'))
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with zfh.open(member) as src, open(target, 'wb') as dst:
                shutil.copyfileobj(src, dst)

    print(f'ANTLR4 C++ runtime {ANTLR_VERSION} unpacked into {CPP_RUNTIME_DIR}')


def runAntlrCpp(lexerGrammar: str, parserGrammar: str) -> None:
    """ Generate the C++ target for a lexer/parser grammar pair.
    """

    # 'python -m antlr4_tool_runner' would launch ANTLR's tree interpreter;
    # tool() is the entry point behind the 'antlr4' console script.
    command = [sys.executable, '-c', 'from antlr4_tool_runner import tool; tool()',
               '-v', ANTLR_VERSION,
               '-Dlanguage=Cpp', '-visitor', '-no-listener',
               '-o', CPP_SRC_DIR,
               os.path.join(GRAMMAR_DIR, lexerGrammar + '.g4'),
               os.path.join(GRAMMAR_DIR, parserGrammar + '.g4')]

    print('  ' + ' '.join(command[3:]))
    subprocess.run(command, check=True)


def applyPatches(path: str, patches: list, substitutions: dict) -> None:
    """ Apply exact-match patches to a generated file, in place.
    """

    with open(path, 'r', encoding='utf-8') as ifh:
        source = ifh.read()

    for description, replacements in patches:
        for old, new in replacements:
            old, new = old % substitutions, new % substitutions
            if new in source:
                continue  # already patched
            if source.count(old) != 1:
                raise RuntimeError(f'{os.path.basename(path)}: cannot apply "{description}" - '
                                   f'expected exactly one occurrence of\n{old!r}\nbut found '
                                   f'{source.count(old)}. speedy-antlr-tool output has changed.')
            source = source.replace(old, new)

    with open(path, 'w', encoding='utf-8') as ofh:
        ofh.write(source)


def patchPredictionMode(name: str, subPackage: str) -> None:
    """ Make the prediction mode a per-call argument of the generated parser.
    """

    substitutions = {'parser': name + 'Parser'}

    applyPatches(os.path.join(CPP_SRC_DIR, f'sa_{name.lower()}_cpp_parser.cpp'),
                 CPP_PATCHES, substitutions)
    applyPatches(os.path.join(NMR_DIR, subPackage, f'sa_{name.lower()}.py'),
                 SHIM_PATCHES, substitutions)

    print('  prediction mode: selectable per call (LL default, SLL on request)')


def generate(name: str) -> None:
    """ Generate the C++ accelerator for one grammar.
    """

    import speedy_antlr_tool

    subPackage, lexerGrammar, expectedEntryRule, readerModule = GRAMMARS[name]
    parserGrammar = name + 'Parser'

    entryRule, useSll = readerFacts(subPackage, readerModule)
    if entryRule != expectedEntryRule:
        raise RuntimeError(f'{readerModule}: entry rule is {entryRule!r}, '
                           f'but the GRAMMARS table says {expectedEntryRule!r}.')

    print(f'{name} ({subPackage}/, entry rule {entryRule!r})')

    os.makedirs(CPP_SRC_DIR, exist_ok=True)
    runAntlrCpp(lexerGrammar, parserGrammar)

    # Read the committed Python parser; the shim is written alongside it.
    speedy_antlr_tool.generate(
        py_parser_path=os.path.join(NMR_DIR, subPackage, parserGrammar + '.py'),
        cpp_output_dir=CPP_SRC_DIR,
        entry_rule_names=[entryRule],
    )
    print(f'  shim: wwpdb/utils/nmr/{subPackage}/sa_{name.lower()}.py')
    print(f'  {readerModule} prediction mode: {"SLL" if useSll else "LL"}')

    patchPredictionMode(name, subPackage)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('grammars', nargs='*', help='grammar names, e.g. NmrPipeCS')
    parser.add_argument('--all', action='store_true', help='generate every grammar in the table')
    parser.add_argument('--list', action='store_true', help='list the bridged grammars and exit')
    args = parser.parse_args()

    if args.list:
        for name, (subPackage, _, entryRule, readerModule) in sorted(GRAMMARS.items()):
            _, useSll = readerFacts(subPackage, readerModule)
            print(f'{name:16s} {subPackage}/  entry={entryRule:16s} '
                  f'prediction={"SLL" if useSll else "LL"}')
        return 0

    names = sorted(GRAMMARS) if args.all else args.grammars
    if not names:
        parser.error('name at least one grammar, or pass --all')

    unknown = [name for name in names if name not in GRAMMARS]
    if unknown:
        parser.error(f'unknown grammar(s): {", ".join(unknown)}; '
                     f'known: {", ".join(sorted(GRAMMARS))}')

    fetchCppRuntime()
    for name in names:
        generate(name)

    print('\nNow build the accelerators:\n'
          '  WWPDB_NMR_BUILD_SPEEDY_ANTLR=1 python setup.py build_ext --inplace -j $(nproc)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
