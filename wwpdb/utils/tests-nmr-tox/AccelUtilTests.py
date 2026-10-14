##
# File: AccelUtilTests.py
# Date:  14-Oct-2026  M. Yokochi
#
# Updates:
##
"""Test cases for AccelUtil, which admits a compiled accelerator only when it matches its Python code.

The fingerprint tests run everywhere. The test that the generated C++ and the committed Python
lexers/parsers serialize the same ATN needs cpp_src/, which only a checkout has (DAOTHER-9785).
"""
import json
import os
import re
import sys
import types
import unittest
import warnings
from unittest import mock

# import commonsetup first: it mocks ConfigInfo, which ChemCompUtil reads when it is imported
if __package__ is None or __package__ == "":
    from os import path

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from commonsetup import TESTOUTPUT  # noqa: F401 pylint: disable=import-error,unused-import
else:
    from .commonsetup import TESTOUTPUT  # noqa: F401 pylint: disable=relative-beyond-top-level

from wwpdb.utils.nmr import AccelUtil
from wwpdb.utils.nmr.AccelUtil import (C_LISTENER_UTIL_API_VERSION,
                                       DISABLE_ACCEL_ENV,
                                       acceptAccelerator,
                                       acceptCAccelerator,
                                       accelerators,
                                       atnFingerprint)
from wwpdb.utils.nmr.mr.CyanaMRLexer import CyanaMRLexer
from wwpdb.utils.nmr.mr.CyanaMRParser import CyanaMRParser

CPP_SRC_DIR = os.path.join(os.path.dirname(AccelUtil.__file__), 'cpp_src')
MANIFEST_PATH = os.path.join(CPP_SRC_DIR, 'speedy_antlr_manifest.json')
SERIALIZED_ATN = re.compile(r'serializedATNSegment\[\]\s*=\s*\{([^}]*)\}')


def pythonFingerprint(lexerClass, parserClass) -> str:
    return atnFingerprint(sys.modules[lexerClass.__module__].serializedATN(),
                          sys.modules[parserClass.__module__].serializedATN())


class TestAccelUtil(unittest.TestCase):

    def setUp(self):
        patcher = mock.patch.dict(os.environ)
        patcher.start()
        self.addCleanup(patcher.stop)
        os.environ.pop(DISABLE_ACCEL_ENV, None)

    def admit(self, name, extModule):
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter('always')
            used = acceptAccelerator(name, extModule, CyanaMRLexer, CyanaMRParser)
        return used, [w for w in caught if issubclass(w.category, RuntimeWarning)]

    def test_matching_fingerprint_is_used(self):
        ext = types.SimpleNamespace(GRAMMAR_FINGERPRINT=pythonFingerprint(CyanaMRLexer, CyanaMRParser))
        used, caught = self.admit('test.matching', ext)
        self.assertTrue(used)
        self.assertEqual(caught, [])
        self.assertEqual(accelerators()['test.matching'], 'compiled')

    def test_missing_extension_falls_back_silently(self):
        used, caught = self.admit('test.missing', None)
        self.assertFalse(used)
        self.assertEqual(caught, [])
        self.assertEqual(accelerators()['test.missing'], 'missing')

    def test_other_grammar_is_rejected(self):
        ext = types.SimpleNamespace(GRAMMAR_FINGERPRINT='0' * 64)
        used, caught = self.admit('test.other', ext)
        self.assertFalse(used)
        self.assertEqual(len(caught), 1)
        self.assertIn('different grammar', str(caught[0].message))
        self.assertEqual(accelerators()['test.other'], 'mismatch')

    def test_build_without_fingerprint_is_rejected(self):
        for ext in (types.SimpleNamespace(), types.SimpleNamespace(GRAMMAR_FINGERPRINT='')):
            used, caught = self.admit('test.unstamped', ext)
            self.assertFalse(used)
            self.assertEqual(len(caught), 1)
            self.assertIn('no grammar fingerprint', str(caught[0].message))

    def test_disable_env_wins(self):
        ext = types.SimpleNamespace(GRAMMAR_FINGERPRINT=pythonFingerprint(CyanaMRLexer, CyanaMRParser))
        for value, expected in (('1', 'disabled'), ('true', 'disabled'), ('0', 'compiled'), ('', 'compiled')):
            os.environ[DISABLE_ACCEL_ENV] = value
            used, caught = self.admit('test.env', ext)
            self.assertEqual(used, expected == 'compiled', value)
            self.assertEqual(caught, [])
            self.assertEqual(accelerators()['test.env'], expected, value)

    def test_c_accelerator_api_version(self):
        cases = ((types.SimpleNamespace(API_VERSION=C_LISTENER_UTIL_API_VERSION), True, 'compiled'),
                 (types.SimpleNamespace(API_VERSION=C_LISTENER_UTIL_API_VERSION + 1), False, 'mismatch'),
                 (types.SimpleNamespace(), False, 'mismatch'),
                 (None, False, 'missing'))
        for ext, expectedUse, expectedStatus in cases:
            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                self.assertEqual(acceptCAccelerator('test.c', ext), expectedUse)
            self.assertEqual(accelerators()['test.c'], expectedStatus)

    def test_fingerprint_separates_lexer_from_parser(self):
        self.assertNotEqual(atnFingerprint([1, 2], [3]), atnFingerprint([1], [2, 3]))
        self.assertNotEqual(atnFingerprint([12], [3]), atnFingerprint([1], [23]))

    @unittest.skipUnless(os.path.isfile(MANIFEST_PATH), 'cpp_src is not shipped in the sdist or wheels')
    def test_cpp_and_python_serialize_the_same_atn(self):
        """ The premise of the fingerprint: for every accelerator, the generated C++ lexer and
            parser carry the very ATN of the committed Python ones, so setup.py (which hashes
            the C++) and the shim (which hashes the Python) agree.
        """

        def cppAtn(name):
            with open(os.path.join(CPP_SRC_DIR, name + '.cpp'), 'r', encoding='utf-8') as ifh:
                bodies = SERIALIZED_ATN.findall(ifh.read())
            self.assertEqual(len(bodies), 1, name)
            return [int(value) for value in bodies[0].split(',') if value.strip()]

        def pyAtn(subPackage, name):
            module = __import__(f'wwpdb.utils.nmr.{subPackage}.{name}', fromlist=['serializedATN'])
            return module.serializedATN()

        with open(MANIFEST_PATH, 'r', encoding='utf-8') as ifh:
            manifest = json.load(ifh)

        for entry in manifest['extensions']:
            with self.subTest(grammar=entry['grammar']):
                lexer, parser = entry['lexer'], entry['parser']
                lexerSubPackage = next(sub for sub in ('mr', 'pk', 'cs')
                                       if os.path.isfile(os.path.join(os.path.dirname(CPP_SRC_DIR), sub, lexer + '.py')))
                self.assertEqual(cppAtn(lexer), pyAtn(lexerSubPackage, lexer))
                self.assertEqual(cppAtn(parser), pyAtn(entry['subpackage'], parser))


if __name__ == '__main__':
    unittest.main()
