##
# File: NEFConversionTests.py
# Date:  01-Jun-2019  E. Peisach
#
# Updates:
# 07-Feb-2020  M. Yokochi - update mock-data directory and include inverse translation NMR-STAR to NEF
##
"""Test cases for NEF conversion"""

import unittest
import os
import platform

try:
    from wwpdb.utils.nmr.nef.NEFTranslator import NEFTranslator
except ImportError:
    from nmr.nef.NEFTranslator import NEFTranslator


class ImportTests(unittest.TestCase):
    def setUp(self):
        self.neft = NEFTranslator()
        here = os.path.abspath(os.path.dirname(__file__))
        self.testdata = os.path.join(here, 'mock-data')
        self.outputdir = os.path.join(here, 'mock-data', platform.python_version())
        if not os.path.exists(self.outputdir):
            os.makedirs(self.outputdir)

    def testTranslate(self):
        indata = os.path.join(self.testdata, '2mqq.nef')
        outdata = os.path.join(self.outputdir, '2mqq.str')
        if os.path.exists(outdata):
            os.unlink(outdata)
        self.neft.nef_to_nmrstar(indata, outdata)
        self.assertTrue(self.neft.validate_file(outdata, 'A')[0])
        self.assertTrue(self.neft.validate_file(outdata)[0])

    def testInverse(self):
        indata = os.path.join(self.testdata, '2mqq.str')
        outdata = os.path.join(self.outputdir, '2mqq.nef')
        if os.path.exists(outdata):
            os.unlink(outdata)
        self.neft.nmrstar_to_nef(indata, outdata)
        self.assertTrue(self.neft.validate_file(outdata, 'A')[0])
        self.assertTrue(self.neft.validate_file(outdata)[0])


if __name__ == '__main__':
    unittest.main()
