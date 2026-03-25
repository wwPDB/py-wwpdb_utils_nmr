##
# File: DetachImportTests.py
# Date:  06-Oct-2018  E. Peisach
#
# Updates:
##
"""Test cases for NefTranslator - simply import everything to ensure imports work"""
import unittest

try:
    from wwpdb.utils.nmr.nef.NefTranslator import NefTranslator
except ImportError:
    from nmr.nef.NefTranslator import NefTranslator


class ImportTests(unittest.TestCase):
    def setUp(self):
        pass

    def testInstantiate(self):  # pylint: disable=no-self-use
        _c = NefTranslator()  # noqa: F841


if __name__ == '__main__':
    unittest.main()
