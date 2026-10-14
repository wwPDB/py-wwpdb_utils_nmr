##
# File: AccelUtil.py
# Date: 14-Oct-2026
#
# Updates:
##
""" Admission control for the optional compiled accelerators.

    The sa_<grammar>.py shims and ParserListenerUtil each fall back to Python when
    their extension does not import. That alone is not enough: an extension can
    import and still be wrong for the Python code next to it. Examples are a stale
    in-place build after a grammar change, an extension that was compiled ad hoc,
    or a .so copied between trees. A parser built from another grammar would hand
    back different parse trees without raising anything.

    So an extension is used only when it proves it matches:
      - each C++ parser exports GRAMMAR_FINGERPRINT, which setup.py computes from
        the serialized ATNs in the generated C++ lexer and parser, and the shim
        recomputes it from the committed Python lexer and parser. ANTLR serializes
        the same ATN for every target, so a match means both were generated from
        the same grammar with the same ANTLR version.
      - c_listener_util exports API_VERSION, which must equal
        C_LISTENER_UTIL_API_VERSION below.

    Anything else falls back to Python with a RuntimeWarning. Set
    WWPDB_NMR_DISABLE_ACCEL=1 to force every accelerator off, for a differential
    run or for debugging. accelerators() reports which path each one took.

    This module imports nothing outside the standard library, because setup.py
    loads it by file path to compute the fingerprints it compiles in.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "1.0.0"

import hashlib
import os
import sys
import warnings
from typing import Dict, Optional, Sequence

DISABLE_ACCEL_ENV = 'WWPDB_NMR_DISABLE_ACCEL'

# Bump this together with C_LISTENER_UTIL_API_VERSION in cpp_src/c_listener_util.c
# whenever the C functions stop matching the Python bodies in mr/ParserListenerUtil.py.
C_LISTENER_UTIL_API_VERSION = 1

# What each accelerator did when its Python module was imported:
#   'compiled' - the extension is in use
#   'missing'  - no extension for this platform/interpreter; the normal pure-Python case
#   'disabled' - WWPDB_NMR_DISABLE_ACCEL is set
#   'mismatch' - the extension imported but does not match the Python code; it is not used
_status: Dict[str, str] = {}


def accelDisabled() -> bool:
    """ Return whether WWPDB_NMR_DISABLE_ACCEL turns every accelerator off.
    """

    return os.environ.get(DISABLE_ACCEL_ENV, '') not in ('', '0', 'false', 'False')


def atnFingerprint(lexerAtn: Sequence[int], parserAtn: Sequence[int]) -> str:
    """ Return the fingerprint of a lexer/parser pair given their serialized ATNs.
        setup.py and acceptAccelerator() must both use this one definition.
    """

    text = ','.join(map(str, lexerAtn)) + '|' + ','.join(map(str, parserAtn))

    return hashlib.sha256(text.encode('ascii')).hexdigest()


def _decide(name: str, extModule, matches) -> bool:
    """ Record and return whether the extension for the named accelerator is used.
        @param matches: called only when the extension imported and is not disabled
    """

    if extModule is None:
        _status[name] = 'missing'
        return False

    if accelDisabled():
        _status[name] = 'disabled'
        return False

    reason = matches(extModule)
    if reason is not None:
        _status[name] = 'mismatch'
        warnings.warn(f'{name}: {reason}; using the Python implementation instead. '
                      'Rebuild the accelerators (see setup.py).', RuntimeWarning, stacklevel=3)
        return False

    _status[name] = 'compiled'
    return True


def acceptAccelerator(shimName: str, extModule, lexerClass, parserClass) -> bool:
    """ Return whether an sa_<grammar> shim may use its C++ parser.
        @param shimName: the shim's __name__
        @param extModule: the imported sa_<grammar>_cpp_parser, or None if it did not import
        @param lexerClass, parserClass: the Python lexer and parser the shim falls back to
    """

    def matches(ext) -> Optional[str]:
        built = getattr(ext, 'GRAMMAR_FINGERPRINT', '')
        if not built:
            return 'the C++ parser carries no grammar fingerprint'
        expected = atnFingerprint(sys.modules[lexerClass.__module__].serializedATN(),
                                  sys.modules[parserClass.__module__].serializedATN())
        if built != expected:
            return 'the C++ parser was compiled from a different grammar than the Python parser'
        return None

    return _decide(shimName, extModule, matches)


def acceptCAccelerator(name: str, extModule) -> bool:
    """ Return whether ParserListenerUtil may bind the functions of c_listener_util.
        @param name: the qualified name of the extension, for accelerators()
        @param extModule: the imported c_listener_util, or None if it did not import
    """

    def matches(ext) -> Optional[str]:
        built = getattr(ext, 'API_VERSION', None)
        if built != C_LISTENER_UTIL_API_VERSION:
            return f'API_VERSION is {built!r}, expected {C_LISTENER_UTIL_API_VERSION}'
        return None

    return _decide(name, extModule, matches)


def accelerators() -> Dict[str, str]:
    """ Return the status of every accelerator imported so far, keyed by module name.
        An accelerator appears once the module that uses it has been imported.
    """

    return dict(sorted(_status.items()))
