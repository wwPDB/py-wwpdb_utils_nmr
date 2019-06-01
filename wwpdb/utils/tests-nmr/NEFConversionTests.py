##
# File: NEFConversionTests.py
# Date:  01-Jun-2019  E. Peisach
#
# Updates:
##
"""Test cases for NEF conversion"""

import unittest
import os
import platform

from wwpdb.utils.nmr.NEFTranslator.NEFTranslator import NEFTranslator

class ImportTests(unittest.TestCase):
    def setUp(self):
        self.neft = NEFTranslator()
        here = os.path.abspath(os.path.dirname(__file__))
        self.testdata = os.path.join(here, "../nmr/NEFTranslator", "data")
        self.outputdir = os.path.join(here, 'test-output', platform.python_version())
        if not os.path.exists(self.outputdir):
            os.makedirs(self.outputdir)

    def testTranslate(self):
        sdata = os.path.join(self.testdata, '2mqq.nef')
        outdata = os.path.join(self.outputdir, '2mqq.str')
        if os.path.exists(outdata):
            os.unlink(outdata)
        self.neft.nef_to_nmrstar(sdata, outdata)
        self.assertTrue(self.neft.validate_file(outdata, 'A')[0])
        self.assertTrue(self.neft.validate_file(outdata)[0])


if __name__ == '__main__':
    unittest.main()
