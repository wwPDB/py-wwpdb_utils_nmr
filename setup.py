# File: setup.py
# Date: 3-Oct-2018
#
# Update:
#  7-Aug-2026 my optional speedy-antlr-tool C++ parser accelerators
#
import glob
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

    extensions = []

    for entry in manifest['extensions']:
        sources = [os.path.join(CPP_SRC_DIR, name) for name in entry['sources']] + sharedSources
        missing = [path for path in sources if not os.path.isfile(path)]
        if missing:
            raise RuntimeError(f'{entry["module"]}: generated sources are missing {missing}; '
                               'run tools/gen_speedy_antlr.py first.')

        extensions.append(
            Extension(f'wwpdb.utils.nmr.{entry["subpackage"]}.{entry["module"]}',
                      sources=sources,
                      include_dirs=[CPP_SRC_DIR, CPP_RUNTIME_DIR],
                      libraries=['antlr4_cpp_runtime'],
                      extra_compile_args=ANTLR_CFLAGS,
                      language='c++'))

    return extensions


buildSpeedyAntlr = os.environ.get('WWPDB_NMR_BUILD_SPEEDY_ANTLR', '') not in ('', '0', 'false', 'False')

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
    ext_modules=speedyAntlrExtensions() if buildSpeedyAntlr else [],
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
