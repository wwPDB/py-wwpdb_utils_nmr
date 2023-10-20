##
# File: test_AlignUtil.py
# Date:  24-Feb-2022  M. Yokochi
#
# Updates:
##
import unittest

try:
    from wwpdb.utils.nmr.AlignUtil import (letterToDigit, indexToLetter)
except ImportError:
    from nmr.AlignUtil import (letterToDigit, indexToLetter)


class TestAlignUtil(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLetterToDigit(self):
        self.assertEqual(letterToDigit("A"), 1)
        self.assertEqual(letterToDigit("AA"), 28)
        self.assertEqual(letterToDigit("Z"), 26)
        self.assertEqual(letterToDigit("ZA"), 27 * 26 + 1)
        self.assertEqual(letterToDigit("a"), 1)
        self.assertEqual(letterToDigit("Aa"), 28)
        self.assertEqual(letterToDigit("z"), 26)
        self.assertEqual(letterToDigit("zA"), 27 * 26 + 1)
        self.assertEqual(letterToDigit("1"), 1)
        self.assertEqual(letterToDigit("0"), 0)
        self.assertEqual(letterToDigit("0", 1), 1)
        self.assertEqual(letterToDigit("Z*A"), 27 * 26 + 1)

    def testIndexToLetter(self):
        self.assertEqual(indexToLetter(letterToDigit("A") - 1), "A")
        self.assertEqual(indexToLetter(letterToDigit("Z") - 1), "Z")
        self.assertEqual(indexToLetter(letterToDigit("AA") - 1), "AA")
        self.assertEqual(indexToLetter(letterToDigit("ZA") - 1), "ZA")
        self.assertEqual(indexToLetter(letterToDigit("AZ") - 1), "AZ")
        self.assertEqual(indexToLetter(letterToDigit("ZZ") - 1), "ZZ")
        self.assertEqual(indexToLetter(letterToDigit("AAA") - 1), "AAA")
        self.assertEqual(indexToLetter(letterToDigit("AAZ") - 1), "AAZ")
        self.assertEqual(indexToLetter(letterToDigit("AZA") - 1), "AZA")
        self.assertEqual(indexToLetter(letterToDigit("AZZ") - 1), "AZZ")
        self.assertEqual(indexToLetter(letterToDigit("ZAA") - 1), "ZAA")
        self.assertEqual(indexToLetter(letterToDigit("ZAZ") - 1), "ZAZ")
        self.assertEqual(indexToLetter(letterToDigit("ZZA") - 1), "ZZA")
        self.assertEqual(indexToLetter(letterToDigit("ZZZ") - 1), "ZZZ")
        self.assertEqual(indexToLetter(letterToDigit("B") - 1), "B")
        self.assertEqual(indexToLetter(letterToDigit("BB") - 1), "BB")
        self.assertEqual(indexToLetter(letterToDigit("BBB") - 1), "BBB")
        self.assertEqual(indexToLetter(letterToDigit("ABC") - 1), "ABC")
        self.assertEqual(indexToLetter(letterToDigit("CBA") - 1), "CBA")
        self.assertEqual(indexToLetter(0), "A")
        self.assertEqual(indexToLetter(1), "B")
        self.assertEqual(indexToLetter(-1), ".")
        self.assertEqual(indexToLetter(letterToDigit("AABC") - 1), "ABC")
        self.assertEqual(indexToLetter(letterToDigit("ZABC") - 1), "ABC")


if __name__ == "__main__":
    unittest.main()
