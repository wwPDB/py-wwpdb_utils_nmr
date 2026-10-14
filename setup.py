# File: setup.py
# Date: 3-Oct-2018
#
# Update:
#  7-Aug-2026 my optional speedy-antlr-tool C++ parser accelerators
# 24-Sep-2026 my optional C accelerator for ParserListenerUtil (DAOTHER-10315)
# 14-Oct-2026 my compile each accelerator's grammar fingerprint in (AccelUtil.py), ship the ANTLR C++ runtime
#                licence in binary wheels, and honour WWPDB_NMR_BUILD_JOBS (DAOTHER-9785)
#
import glob
import importlib.util
import json
import os
import re

from setuptools import Extension, find_packages, setup

packages = []
thisPackage = 'wwpdb.utils.nmr'

# ------------------------------------------------------------------------------
# Optional speedy-antlr-tool C++ parser accelerators.
#
# Off by default: the sdist/source wheel published to PyPI stays pure Python, and
# each sa_<grammar>.py shim transparently falls back to the ANTLR Python runtime
# when its extension is absent. Set WWPDB_NMR_BUILD_SPEEDY_ANTLR=1 to compile
# them (see tools/gen_speedy_antlr.py and the Dockerfile builder stage):
#
#   WWPDB_NMR_BUILD_SPEEDY_ANTLR=1 python setup.py build_clib build_ext --inplace -j $(nproc)
#
# The accelerators are declared by cpp_src/speedy_antlr_manifest.json, written by
# tools/gen_speedy_antlr.py. Reading the manifest (rather than importing that
# script, or duplicating its grammar table here) keeps the build independent of
# tools/, which the container deletes after building.
CPP_SRC_DIR = os.path.join('wwpdb', 'utils', 'nmr', 'cpp_src')
CPP_RUNTIME_DIR = os.path.join(CPP_SRC_DIR, 'antlr4-cpp-runtime')
MANIFEST_PATH = os.path.join(CPP_SRC_DIR, 'speedy_antlr_manifest.json')

# ANTLR's C++ runtime is ~140 translation units. Building it once as a static
# library, rather than folding it into every Extension, keeps the build time flat
# as more grammars are bridged.
ANTLR_CFLAGS = ['-std=c++17', '-DANTLR4CPP_STATIC', '-Wno-overloaded-virtual', '-Wno-deprecated-declarations']

# The serialized ATN that ANTLR writes into a generated C++ lexer or parser.
SERIALIZED_ATN = re.compile(r'serializedATNSegment\[\]\s*=\s*\{([^}]*)\}')


def loadAccelUtil():
    """ wwpdb/utils/nmr/AccelUtil.py, loaded by path: importing the package would need
        its runtime dependencies at build time. AccelUtil uses the standard library only.
    """

    spec = importlib.util.spec_from_file_location('AccelUtil', os.path.join('wwpdb', 'utils', 'nmr', 'AccelUtil.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


def serializedAtn(name: str) -> list:
    """ The serialized ATN of a generated C++ lexer or parser, e.g. 'XplorMRLexer'.
    """

    with open(os.path.join(CPP_SRC_DIR, name + '.cpp'), 'r', encoding='utf-8') as ifh:
        bodies = SERIALIZED_ATN.findall(ifh.read())

    if len(bodies) != 1:
        raise RuntimeError(f'{name}.cpp: expected one serializedATNSegment, found {len(bodies)}.')

    return [int(value) for value in bodies[0].split(',') if value.strip()]


def speedyAntlrLibraries() -> list:
    """ The ANTLR4 C++ runtime, compiled once and shared by every accelerator.
    """

    sources = sorted(glob.glob(os.path.join(CPP_RUNTIME_DIR, '**', '*.cpp'), recursive=True))
    if not sources:
        raise RuntimeError(f'{CPP_RUNTIME_DIR} is empty; run tools/gen_speedy_antlr.py first.')

    return [('antlr4_cpp_runtime', {'sources': sources,
                                    'include_dirs': [CPP_RUNTIME_DIR],
                                    'cflags': ANTLR_CFLAGS,
                                    'language': 'c++'})]


def speedyAntlrExtensions() -> list:
    """ One Extension per bridged grammar, linked against the shared runtime.
    """

    if not os.path.isfile(MANIFEST_PATH):
        raise RuntimeError(f'{MANIFEST_PATH} is missing; run tools/gen_speedy_antlr.py --all first.')

    with open(MANIFEST_PATH, 'r', encoding='utf-8') as ifh:
        manifest = json.load(ifh)

    # Sources are listed per accelerator rather than globbed by prefix, because
    # NmrViewNPKParser, SparkyNPKParser and SparkyRPKParser borrow another
    # grammar's lexer.
    sharedSources = [os.path.join(CPP_SRC_DIR, name) for name in manifest.get('shared_sources', [])]

    # Each accelerator carries the fingerprint of the grammar it is compiled from, and its
    # shim uses it only when that matches the Python lexer and parser (AccelUtil.py).
    atnFingerprint = loadAccelUtil().atnFingerprint

    extensions = []

    for entry in manifest['extensions']:
        sources = [os.path.join(CPP_SRC_DIR, name) for name in entry['sources']] + sharedSources
        missing = [path for path in sources if not os.path.isfile(path)]
        if missing:
            raise RuntimeError(f'{entry["module"]}: generated sources are missing {missing}; '
                               'run tools/gen_speedy_antlr.py first.')

        if 'lexer' not in entry or 'parser' not in entry:
            raise RuntimeError(f'{entry["module"]}: the manifest predates grammar fingerprints; '
                               'run tools/gen_speedy_antlr.py --repatch --all first.')

        fingerprint = atnFingerprint(serializedAtn(entry['lexer']), serializedAtn(entry['parser']))

        extensions.append(
            Extension(f'wwpdb.utils.nmr.{entry["subpackage"]}.{entry["module"]}',
                      sources=sources,
                      include_dirs=[CPP_SRC_DIR, CPP_RUNTIME_DIR],
                      libraries=['antlr4_cpp_runtime'],
                      define_macros=[('WWPDB_GRAMMAR_FINGERPRINT', f'"{fingerprint}"')],
                      extra_compile_args=ANTLR_CFLAGS,
                      language='c++'))

    return extensions


buildSpeedyAntlr = os.environ.get('WWPDB_NMR_BUILD_SPEEDY_ANTLR', '') not in ('', '0', 'false', 'False')


# ------------------------------------------------------------------------------
# Optional C accelerator for wwpdb/utils/nmr/mr/ParserListenerUtil.py.
#
# Same contract as the speedy-antlr accelerators above: off by default, so the
# sdist/wheel published to PyPI stays pure Python, and ParserListenerUtil rebinds
# copyFactor()/copyPolySeq()/atomKey()/factorKey() to the compiled versions only
# when the extension imports. One dependency-free C99 translation unit, so this
# needs no static library and no extra toolchain beyond a C compiler:
#
#   WWPDB_NMR_BUILD_C_ACCEL=1 python setup.py build_ext --inplace


def cAccelExtensions() -> list:
    """ The ParserListenerUtil accelerator, built in place next to its Python fallbacks.
    """

    source = os.path.join(CPP_SRC_DIR, 'c_listener_util.c')

    if not os.path.isfile(source):
        raise RuntimeError(f'{source} is missing.')

    return [Extension('wwpdb.utils.nmr.mr.c_listener_util',
                      sources=[source],
                      language='c')]


buildCAccel = os.environ.get('WWPDB_NMR_BUILD_C_ACCEL', '') not in ('', '0', 'false', 'False')

# 'pip wheel' and cibuildwheel cannot pass build_ext -j, so a wheel build takes the number
# of parallel compile jobs from here. build_clib (the ANTLR runtime) stays serial.
buildJobs = os.environ.get('WWPDB_NMR_BUILD_JOBS', '')
buildOptions = {'build_ext': {'parallel': int(buildJobs)}} if buildJobs.isdigit() and int(buildJobs) > 1 else {}

# The ANTLR4 C++ runtime (BSD-3-Clause) is linked statically into every speedy-antlr
# accelerator, so a binary wheel must carry its licence.
licenseFiles = ['LICENSE'] + ([os.path.join(CPP_RUNTIME_DIR, 'LICENSE.txt')] if buildSpeedyAntlr else [])

with open('wwpdb/utils/nmr/__init__.py', 'r', encoding='utf-8') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

setup(
    name=thisPackage,
    version=version,
    description='wwPDB NMR utilities',
    long_description="See:  README.md",
    author='Ezra Peisach',
    author_email='ezra.peisach@rcsb.org',
    url='https://github.com/wwpdb/py-wwpdb_utils_nmr',
    #
    license='Apache 2.0',
    license_files=licenseFiles,
    classifiers=[
        'Development Status :: 3 - Alpha',
        # 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    #
    # munkres 1.0.12 last to support python 2. Developers did not tag properly
    install_requires=['wwpdb.utils.config >= 0.34', 'wwpdb.utils.align',
                      # "pynmrstar ~= 2.6; python_version < '3'",
                      "pynmrstar >= 3.2; python_version >= '3'",
                      # "munkres==1.0.12; python_version == '2.7'",
                      "munkres; python_version >= '3'",
                      'mmcif', 'numpy', "scikit-learn",
                      "rmsd", "packaging", "chardet",
                      # "typing_extensions",  # typing_extensions was missing from rmsd 1.5 package
                      # "antlr4-python2-runtime; python_version == '2.7'",
                      "antlr4-python3-runtime ~= 4.13.0; python_version >= '3'",
                      "striprtf",
                      "datetime",
                      "dataclasses; python_version == '3.6'"],
    packages=find_packages(exclude=['wwpdb.utils.tests-nmr', 'wwpdb.utils.tests-nmr-tox', 'mock-data']),
    libraries=speedyAntlrLibraries() if buildSpeedyAntlr else [],
    ext_modules=(speedyAntlrExtensions() if buildSpeedyAntlr else [])
    + (cAccelExtensions() if buildCAccel else []),
    # Enables Manifest to be used
    include_package_data=True,
    package_data={
        # If any package contains *.md or *.rst ...  files, include them:
        '': ['*.md', '*.rst', "*.txt", "*.cfg"],
    },
    #
    # These basic tests require no database services -
    test_suite="wwpdb.utils.tests-nmr",
    tests_require=['tox'],
    #
    # Not configured ...
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    python_requires='>=3.7',
    options=buildOptions,
    command_options={
        'build_sphinx': {
            'project': ('setup.py', thisPackage),
            'version': ('setup.py', version),
            'release': ('setup.py', version)
        }
    },
    # This setting for namespace package support -
    zip_safe=False,
)
