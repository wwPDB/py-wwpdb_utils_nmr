##
# File: DetachImportTests.py
# Date:  06-Oct-2018  E. Peisach
#
# Updates:
##
"""Test cases for NEFTranslator - simply import everything to ensure imports work"""

import unittest

try:
    from wwpdb.utils.nmr.NEFTranslator.NEFTranslator import NEFTranslator
except ImportError:
    from nmr.NEFTranslator.NEFTranslator import NEFTranslator


class ImportTests(unittest.TestCase):
    def setUp(self):
        pass

    def testInstantiate(self):  # pylint: disable=no-self-use
        _c = NEFTranslator()  # noqa: F841


if __name__ == '__main__':
    unittest.main()
