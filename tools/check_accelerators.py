#!/usr/bin/env python3
##
# File: tools/check_accelerators.py
# Date: 14-Oct-2026
#
# Updates:
##
""" Report which compiled accelerators the installed wwpdb.utils.nmr uses.

    Imports every sa_<grammar> shim named in cpp_src/speedy_antlr_manifest.json
    and the c_listener_util extension, then prints the status AccelUtil recorded
    for each: compiled, missing, disabled or mismatch.

    With --require-compiled it exits non-zero unless every one is 'compiled'.
    cibuildwheel runs it that way against each freshly built wheel, so a wheel
    whose accelerators would silently fall back to Python is never published.

    Only the shims, the generated lexers/parsers and AccelUtil are imported, which
    need nothing beyond antlr4-python3-runtime, so the check does not depend on
    the rest of the package's runtime environment.

    Usage:
        python3 tools/check_accelerators.py [--require-compiled]
    @author: Masashi Yokochi
"""
import argparse
import importlib
import json
import os
import sys
import warnings

MANIFEST_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                             'wwpdb', 'utils', 'nmr', 'cpp_src', 'speedy_antlr_manifest.json')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--require-compiled', action='store_true',
                        help='fail unless every accelerator is compiled and admitted')
    args = parser.parse_args()

    with open(MANIFEST_PATH, 'r', encoding='utf-8') as ifh:
        manifest = json.load(ifh)

    from wwpdb.utils.nmr.AccelUtil import acceptCAccelerator, accelerators

    with warnings.catch_warnings():
        warnings.simplefilter('always')  # print every mismatch, not just the first per call site

        for entry in manifest['extensions']:
            importlib.import_module(f'wwpdb.utils.nmr.{entry["subpackage"]}.{entry["shim"]}')

        # c_listener_util is admitted by mr/ParserListenerUtil.py, which needs the whole
        # runtime environment to import; apply the same test to the extension directly.
        name = 'wwpdb.utils.nmr.mr.c_listener_util'
        try:
            extension = importlib.import_module(name)
        except ImportError:
            extension = None
        acceptCAccelerator(name, extension)

    status = accelerators()
    for module, state in status.items():
        print(f'{state:9s} {module}')

    counts = {}
    for state in status.values():
        counts[state] = counts.get(state, 0) + 1
    print(', '.join(f'{count} {state}' for state, count in sorted(counts.items())))

    import wwpdb.utils.nmr
    print(f'wwpdb.utils.nmr {wwpdb.utils.nmr.__version__} from {os.path.dirname(wwpdb.utils.nmr.__file__)}')

    if args.require_compiled and set(status.values()) != {'compiled'}:
        print('FAIL: not every accelerator is compiled and admitted', file=sys.stderr)
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())
