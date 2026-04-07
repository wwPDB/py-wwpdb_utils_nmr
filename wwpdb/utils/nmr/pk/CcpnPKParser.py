# Generated from CcpnPKParser.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,41,590,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,3,0,34,8,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,
        0,43,8,0,10,0,12,0,46,9,0,1,0,1,0,1,1,3,1,51,8,1,1,1,3,1,54,8,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,64,8,1,1,1,3,1,67,8,1,1,1,3,
        1,70,8,1,1,1,3,1,73,8,1,1,1,3,1,76,8,1,1,1,3,1,79,8,1,1,1,3,1,82,
        8,1,1,1,3,1,85,8,1,1,1,3,1,88,8,1,1,1,1,1,4,1,92,8,1,11,1,12,1,93,
        1,2,3,2,97,8,2,1,2,3,2,100,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,3,2,112,8,2,1,2,3,2,115,8,2,1,2,3,2,118,8,2,1,2,3,2,121,8,
        2,1,2,3,2,124,8,2,1,2,3,2,127,8,2,1,2,5,2,130,8,2,10,2,12,2,133,
        9,2,1,2,1,2,1,3,3,3,138,8,3,1,3,3,3,141,8,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,155,8,3,1,3,3,3,158,8,3,1,3,3,3,
        161,8,3,1,3,3,3,164,8,3,1,3,3,3,167,8,3,1,3,3,3,170,8,3,1,3,3,3,
        173,8,3,1,3,3,3,176,8,3,1,3,3,3,179,8,3,1,3,3,3,182,8,3,1,3,1,3,
        4,3,186,8,3,11,3,12,3,187,1,4,3,4,191,8,4,1,4,3,4,194,8,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,210,8,4,1,
        4,3,4,213,8,4,1,4,3,4,216,8,4,1,4,3,4,219,8,4,1,4,3,4,222,8,4,1,
        4,3,4,225,8,4,1,4,3,4,228,8,4,1,4,5,4,231,8,4,10,4,12,4,234,9,4,
        1,4,1,4,1,5,3,5,239,8,5,1,5,3,5,242,8,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,260,8,5,1,5,3,5,263,
        8,5,1,5,3,5,266,8,5,1,5,3,5,269,8,5,1,5,3,5,272,8,5,1,5,3,5,275,
        8,5,1,5,3,5,278,8,5,1,5,3,5,281,8,5,1,5,3,5,284,8,5,1,5,3,5,287,
        8,5,1,5,3,5,290,8,5,1,5,1,5,4,5,294,8,5,11,5,12,5,295,1,6,3,6,299,
        8,6,1,6,3,6,302,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,322,8,6,1,6,3,6,325,8,6,1,6,3,6,
        328,8,6,1,6,3,6,331,8,6,1,6,3,6,334,8,6,1,6,3,6,337,8,6,1,6,3,6,
        340,8,6,1,6,3,6,343,8,6,1,6,5,6,346,8,6,10,6,12,6,349,9,6,1,6,1,
        6,1,7,3,7,354,8,7,1,7,3,7,357,8,7,1,7,1,7,1,7,3,7,362,8,7,1,7,3,
        7,365,8,7,1,7,3,7,368,8,7,1,7,3,7,371,8,7,1,7,3,7,374,8,7,1,7,3,
        7,377,8,7,1,7,3,7,380,8,7,1,7,3,7,383,8,7,1,7,1,7,4,7,387,8,7,11,
        7,12,7,388,1,8,3,8,392,8,8,1,8,3,8,395,8,8,1,8,1,8,1,8,3,8,400,8,
        8,1,8,3,8,403,8,8,1,8,3,8,406,8,8,1,8,3,8,409,8,8,1,8,3,8,412,8,
        8,1,8,5,8,415,8,8,10,8,12,8,418,9,8,1,8,1,8,1,9,3,9,423,8,9,1,9,
        3,9,426,8,9,1,9,1,9,1,9,1,9,3,9,432,8,9,1,9,3,9,435,8,9,1,9,3,9,
        438,8,9,1,9,3,9,441,8,9,1,9,3,9,444,8,9,1,9,3,9,447,8,9,1,9,3,9,
        450,8,9,1,9,3,9,453,8,9,1,9,3,9,456,8,9,1,9,1,9,4,9,460,8,9,11,9,
        12,9,461,1,10,3,10,465,8,10,1,10,3,10,468,8,10,1,10,1,10,1,10,1,
        10,3,10,474,8,10,1,10,3,10,477,8,10,1,10,3,10,480,8,10,1,10,3,10,
        483,8,10,1,10,3,10,486,8,10,1,10,3,10,489,8,10,1,10,5,10,492,8,10,
        10,10,12,10,495,9,10,1,10,1,10,1,11,3,11,500,8,11,1,11,3,11,503,
        8,11,1,11,1,11,1,11,1,11,1,11,3,11,510,8,11,1,11,3,11,513,8,11,1,
        11,3,11,516,8,11,1,11,3,11,519,8,11,1,11,3,11,522,8,11,1,11,3,11,
        525,8,11,1,11,3,11,528,8,11,1,11,3,11,531,8,11,1,11,3,11,534,8,11,
        1,11,3,11,537,8,11,1,11,1,11,4,11,541,8,11,11,11,12,11,542,1,12,
        3,12,546,8,12,1,12,3,12,549,8,12,1,12,1,12,1,12,1,12,1,12,3,12,556,
        8,12,1,12,3,12,559,8,12,1,12,3,12,562,8,12,1,12,3,12,565,8,12,1,
        12,3,12,568,8,12,1,12,3,12,571,8,12,1,12,3,12,574,8,12,1,12,5,12,
        577,8,12,10,12,12,12,580,9,12,1,12,1,12,1,13,1,13,1,14,1,14,1,15,
        1,15,1,15,0,0,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,11,
        2,0,2,2,17,17,3,0,4,5,18,18,22,22,2,0,19,19,23,23,2,0,3,3,26,26,
        2,0,18,18,22,22,1,1,14,14,2,0,20,20,24,24,2,0,5,5,18,18,2,0,21,21,
        25,25,2,0,6,8,11,11,2,0,6,8,11,12,713,0,33,1,0,0,0,2,50,1,0,0,0,
        4,96,1,0,0,0,6,137,1,0,0,0,8,190,1,0,0,0,10,238,1,0,0,0,12,298,1,
        0,0,0,14,353,1,0,0,0,16,391,1,0,0,0,18,422,1,0,0,0,20,464,1,0,0,
        0,22,499,1,0,0,0,24,545,1,0,0,0,26,583,1,0,0,0,28,585,1,0,0,0,30,
        587,1,0,0,0,32,34,5,14,0,0,33,32,1,0,0,0,33,34,1,0,0,0,34,44,1,0,
        0,0,35,43,3,2,1,0,36,43,3,6,3,0,37,43,3,10,5,0,38,43,3,14,7,0,39,
        43,3,18,9,0,40,43,3,22,11,0,41,43,5,14,0,0,42,35,1,0,0,0,42,36,1,
        0,0,0,42,37,1,0,0,0,42,38,1,0,0,0,42,39,1,0,0,0,42,40,1,0,0,0,42,
        41,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,47,1,0,0,
        0,46,44,1,0,0,0,47,48,5,0,0,1,48,1,1,0,0,0,49,51,5,1,0,0,50,49,1,
        0,0,0,50,51,1,0,0,0,51,53,1,0,0,0,52,54,7,0,0,0,53,52,1,0,0,0,53,
        54,1,0,0,0,54,63,1,0,0,0,55,56,7,1,0,0,56,57,7,2,0,0,57,58,5,26,
        0,0,58,64,5,27,0,0,59,60,7,3,0,0,60,61,5,27,0,0,61,62,7,4,0,0,62,
        64,7,2,0,0,63,55,1,0,0,0,63,59,1,0,0,0,64,66,1,0,0,0,65,67,5,30,
        0,0,66,65,1,0,0,0,66,67,1,0,0,0,67,69,1,0,0,0,68,70,5,31,0,0,69,
        68,1,0,0,0,69,70,1,0,0,0,70,72,1,0,0,0,71,73,5,32,0,0,72,71,1,0,
        0,0,72,73,1,0,0,0,73,75,1,0,0,0,74,76,5,33,0,0,75,74,1,0,0,0,75,
        76,1,0,0,0,76,78,1,0,0,0,77,79,5,36,0,0,78,77,1,0,0,0,78,79,1,0,
        0,0,79,81,1,0,0,0,80,82,5,37,0,0,81,80,1,0,0,0,81,82,1,0,0,0,82,
        84,1,0,0,0,83,85,5,38,0,0,84,83,1,0,0,0,84,85,1,0,0,0,85,87,1,0,
        0,0,86,88,5,39,0,0,87,86,1,0,0,0,87,88,1,0,0,0,88,89,1,0,0,0,89,
        91,5,41,0,0,90,92,3,4,2,0,91,90,1,0,0,0,92,93,1,0,0,0,93,91,1,0,
        0,0,93,94,1,0,0,0,94,3,1,0,0,0,95,97,5,6,0,0,96,95,1,0,0,0,96,97,
        1,0,0,0,97,99,1,0,0,0,98,100,5,6,0,0,99,98,1,0,0,0,99,100,1,0,0,
        0,100,111,1,0,0,0,101,102,3,26,13,0,102,103,3,26,13,0,103,104,5,
        11,0,0,104,105,5,11,0,0,105,112,1,0,0,0,106,107,5,11,0,0,107,108,
        5,11,0,0,108,109,3,26,13,0,109,110,3,26,13,0,110,112,1,0,0,0,111,
        101,1,0,0,0,111,106,1,0,0,0,112,114,1,0,0,0,113,115,3,28,14,0,114,
        113,1,0,0,0,114,115,1,0,0,0,115,117,1,0,0,0,116,118,3,28,14,0,117,
        116,1,0,0,0,117,118,1,0,0,0,118,120,1,0,0,0,119,121,3,26,13,0,120,
        119,1,0,0,0,120,121,1,0,0,0,121,123,1,0,0,0,122,124,3,26,13,0,123,
        122,1,0,0,0,123,124,1,0,0,0,124,126,1,0,0,0,125,127,3,26,13,0,126,
        125,1,0,0,0,126,127,1,0,0,0,127,131,1,0,0,0,128,130,3,30,15,0,129,
        128,1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,132,1,0,0,0,132,
        134,1,0,0,0,133,131,1,0,0,0,134,135,7,5,0,0,135,5,1,0,0,0,136,138,
        5,1,0,0,137,136,1,0,0,0,137,138,1,0,0,0,138,140,1,0,0,0,139,141,
        7,0,0,0,140,139,1,0,0,0,140,141,1,0,0,0,141,154,1,0,0,0,142,143,
        7,1,0,0,143,144,7,2,0,0,144,145,7,6,0,0,145,146,5,26,0,0,146,147,
        5,27,0,0,147,155,5,28,0,0,148,149,7,3,0,0,149,150,5,27,0,0,150,151,
        5,28,0,0,151,152,7,7,0,0,152,153,7,2,0,0,153,155,7,6,0,0,154,142,
        1,0,0,0,154,148,1,0,0,0,155,157,1,0,0,0,156,158,5,30,0,0,157,156,
        1,0,0,0,157,158,1,0,0,0,158,160,1,0,0,0,159,161,5,31,0,0,160,159,
        1,0,0,0,160,161,1,0,0,0,161,163,1,0,0,0,162,164,5,32,0,0,163,162,
        1,0,0,0,163,164,1,0,0,0,164,166,1,0,0,0,165,167,5,33,0,0,166,165,
        1,0,0,0,166,167,1,0,0,0,167,169,1,0,0,0,168,170,5,34,0,0,169,168,
        1,0,0,0,169,170,1,0,0,0,170,172,1,0,0,0,171,173,5,36,0,0,172,171,
        1,0,0,0,172,173,1,0,0,0,173,175,1,0,0,0,174,176,5,37,0,0,175,174,
        1,0,0,0,175,176,1,0,0,0,176,178,1,0,0,0,177,179,5,38,0,0,178,177,
        1,0,0,0,178,179,1,0,0,0,179,181,1,0,0,0,180,182,5,39,0,0,181,180,
        1,0,0,0,181,182,1,0,0,0,182,183,1,0,0,0,183,185,5,41,0,0,184,186,
        3,8,4,0,185,184,1,0,0,0,186,187,1,0,0,0,187,185,1,0,0,0,187,188,
        1,0,0,0,188,7,1,0,0,0,189,191,5,6,0,0,190,189,1,0,0,0,190,191,1,
        0,0,0,191,193,1,0,0,0,192,194,5,6,0,0,193,192,1,0,0,0,193,194,1,
        0,0,0,194,209,1,0,0,0,195,196,3,26,13,0,196,197,3,26,13,0,197,198,
        3,26,13,0,198,199,5,11,0,0,199,200,5,11,0,0,200,201,5,11,0,0,201,
        210,1,0,0,0,202,203,5,11,0,0,203,204,5,11,0,0,204,205,5,11,0,0,205,
        206,3,26,13,0,206,207,3,26,13,0,207,208,3,26,13,0,208,210,1,0,0,
        0,209,195,1,0,0,0,209,202,1,0,0,0,210,212,1,0,0,0,211,213,3,28,14,
        0,212,211,1,0,0,0,212,213,1,0,0,0,213,215,1,0,0,0,214,216,3,28,14,
        0,215,214,1,0,0,0,215,216,1,0,0,0,216,218,1,0,0,0,217,219,3,26,13,
        0,218,217,1,0,0,0,218,219,1,0,0,0,219,221,1,0,0,0,220,222,3,26,13,
        0,221,220,1,0,0,0,221,222,1,0,0,0,222,224,1,0,0,0,223,225,3,26,13,
        0,224,223,1,0,0,0,224,225,1,0,0,0,225,227,1,0,0,0,226,228,3,26,13,
        0,227,226,1,0,0,0,227,228,1,0,0,0,228,232,1,0,0,0,229,231,3,30,15,
        0,230,229,1,0,0,0,231,234,1,0,0,0,232,230,1,0,0,0,232,233,1,0,0,
        0,233,235,1,0,0,0,234,232,1,0,0,0,235,236,7,5,0,0,236,9,1,0,0,0,
        237,239,5,1,0,0,238,237,1,0,0,0,238,239,1,0,0,0,239,241,1,0,0,0,
        240,242,7,0,0,0,241,240,1,0,0,0,241,242,1,0,0,0,242,259,1,0,0,0,
        243,244,7,1,0,0,244,245,7,2,0,0,245,246,7,6,0,0,246,247,7,8,0,0,
        247,248,5,26,0,0,248,249,5,27,0,0,249,250,5,28,0,0,250,260,5,29,
        0,0,251,252,7,3,0,0,252,253,5,27,0,0,253,254,5,28,0,0,254,255,5,
        29,0,0,255,256,7,7,0,0,256,257,7,2,0,0,257,258,7,6,0,0,258,260,7,
        8,0,0,259,243,1,0,0,0,259,251,1,0,0,0,260,262,1,0,0,0,261,263,5,
        30,0,0,262,261,1,0,0,0,262,263,1,0,0,0,263,265,1,0,0,0,264,266,5,
        31,0,0,265,264,1,0,0,0,265,266,1,0,0,0,266,268,1,0,0,0,267,269,5,
        32,0,0,268,267,1,0,0,0,268,269,1,0,0,0,269,271,1,0,0,0,270,272,5,
        33,0,0,271,270,1,0,0,0,271,272,1,0,0,0,272,274,1,0,0,0,273,275,5,
        34,0,0,274,273,1,0,0,0,274,275,1,0,0,0,275,277,1,0,0,0,276,278,5,
        35,0,0,277,276,1,0,0,0,277,278,1,0,0,0,278,280,1,0,0,0,279,281,5,
        36,0,0,280,279,1,0,0,0,280,281,1,0,0,0,281,283,1,0,0,0,282,284,5,
        37,0,0,283,282,1,0,0,0,283,284,1,0,0,0,284,286,1,0,0,0,285,287,5,
        38,0,0,286,285,1,0,0,0,286,287,1,0,0,0,287,289,1,0,0,0,288,290,5,
        39,0,0,289,288,1,0,0,0,289,290,1,0,0,0,290,291,1,0,0,0,291,293,5,
        41,0,0,292,294,3,12,6,0,293,292,1,0,0,0,294,295,1,0,0,0,295,293,
        1,0,0,0,295,296,1,0,0,0,296,11,1,0,0,0,297,299,5,6,0,0,298,297,1,
        0,0,0,298,299,1,0,0,0,299,301,1,0,0,0,300,302,5,6,0,0,301,300,1,
        0,0,0,301,302,1,0,0,0,302,321,1,0,0,0,303,304,3,26,13,0,304,305,
        3,26,13,0,305,306,3,26,13,0,306,307,3,26,13,0,307,308,5,11,0,0,308,
        309,5,11,0,0,309,310,5,11,0,0,310,311,5,11,0,0,311,322,1,0,0,0,312,
        313,5,11,0,0,313,314,5,11,0,0,314,315,5,11,0,0,315,316,5,11,0,0,
        316,317,3,26,13,0,317,318,3,26,13,0,318,319,3,26,13,0,319,320,3,
        26,13,0,320,322,1,0,0,0,321,303,1,0,0,0,321,312,1,0,0,0,322,324,
        1,0,0,0,323,325,3,28,14,0,324,323,1,0,0,0,324,325,1,0,0,0,325,327,
        1,0,0,0,326,328,3,28,14,0,327,326,1,0,0,0,327,328,1,0,0,0,328,330,
        1,0,0,0,329,331,3,26,13,0,330,329,1,0,0,0,330,331,1,0,0,0,331,333,
        1,0,0,0,332,334,3,26,13,0,333,332,1,0,0,0,333,334,1,0,0,0,334,336,
        1,0,0,0,335,337,3,26,13,0,336,335,1,0,0,0,336,337,1,0,0,0,337,339,
        1,0,0,0,338,340,3,26,13,0,339,338,1,0,0,0,339,340,1,0,0,0,340,342,
        1,0,0,0,341,343,3,26,13,0,342,341,1,0,0,0,342,343,1,0,0,0,343,347,
        1,0,0,0,344,346,3,30,15,0,345,344,1,0,0,0,346,349,1,0,0,0,347,345,
        1,0,0,0,347,348,1,0,0,0,348,350,1,0,0,0,349,347,1,0,0,0,350,351,
        7,5,0,0,351,13,1,0,0,0,352,354,5,1,0,0,353,352,1,0,0,0,353,354,1,
        0,0,0,354,356,1,0,0,0,355,357,7,0,0,0,356,355,1,0,0,0,356,357,1,
        0,0,0,357,358,1,0,0,0,358,359,7,1,0,0,359,361,7,2,0,0,360,362,5,
        30,0,0,361,360,1,0,0,0,361,362,1,0,0,0,362,364,1,0,0,0,363,365,5,
        31,0,0,364,363,1,0,0,0,364,365,1,0,0,0,365,367,1,0,0,0,366,368,5,
        32,0,0,367,366,1,0,0,0,367,368,1,0,0,0,368,370,1,0,0,0,369,371,5,
        33,0,0,370,369,1,0,0,0,370,371,1,0,0,0,371,373,1,0,0,0,372,374,5,
        36,0,0,373,372,1,0,0,0,373,374,1,0,0,0,374,376,1,0,0,0,375,377,5,
        37,0,0,376,375,1,0,0,0,376,377,1,0,0,0,377,379,1,0,0,0,378,380,5,
        38,0,0,379,378,1,0,0,0,379,380,1,0,0,0,380,382,1,0,0,0,381,383,5,
        39,0,0,382,381,1,0,0,0,382,383,1,0,0,0,383,384,1,0,0,0,384,386,5,
        41,0,0,385,387,3,16,8,0,386,385,1,0,0,0,387,388,1,0,0,0,388,386,
        1,0,0,0,388,389,1,0,0,0,389,15,1,0,0,0,390,392,5,6,0,0,391,390,1,
        0,0,0,391,392,1,0,0,0,392,394,1,0,0,0,393,395,5,6,0,0,394,393,1,
        0,0,0,394,395,1,0,0,0,395,396,1,0,0,0,396,397,3,26,13,0,397,399,
        3,26,13,0,398,400,3,28,14,0,399,398,1,0,0,0,399,400,1,0,0,0,400,
        402,1,0,0,0,401,403,3,28,14,0,402,401,1,0,0,0,402,403,1,0,0,0,403,
        405,1,0,0,0,404,406,3,26,13,0,405,404,1,0,0,0,405,406,1,0,0,0,406,
        408,1,0,0,0,407,409,3,26,13,0,408,407,1,0,0,0,408,409,1,0,0,0,409,
        411,1,0,0,0,410,412,3,26,13,0,411,410,1,0,0,0,411,412,1,0,0,0,412,
        416,1,0,0,0,413,415,3,30,15,0,414,413,1,0,0,0,415,418,1,0,0,0,416,
        414,1,0,0,0,416,417,1,0,0,0,417,419,1,0,0,0,418,416,1,0,0,0,419,
        420,7,5,0,0,420,17,1,0,0,0,421,423,5,1,0,0,422,421,1,0,0,0,422,423,
        1,0,0,0,423,425,1,0,0,0,424,426,7,0,0,0,425,424,1,0,0,0,425,426,
        1,0,0,0,426,427,1,0,0,0,427,428,7,1,0,0,428,429,7,2,0,0,429,431,
        7,6,0,0,430,432,5,30,0,0,431,430,1,0,0,0,431,432,1,0,0,0,432,434,
        1,0,0,0,433,435,5,31,0,0,434,433,1,0,0,0,434,435,1,0,0,0,435,437,
        1,0,0,0,436,438,5,32,0,0,437,436,1,0,0,0,437,438,1,0,0,0,438,440,
        1,0,0,0,439,441,5,33,0,0,440,439,1,0,0,0,440,441,1,0,0,0,441,443,
        1,0,0,0,442,444,5,34,0,0,443,442,1,0,0,0,443,444,1,0,0,0,444,446,
        1,0,0,0,445,447,5,36,0,0,446,445,1,0,0,0,446,447,1,0,0,0,447,449,
        1,0,0,0,448,450,5,37,0,0,449,448,1,0,0,0,449,450,1,0,0,0,450,452,
        1,0,0,0,451,453,5,38,0,0,452,451,1,0,0,0,452,453,1,0,0,0,453,455,
        1,0,0,0,454,456,5,39,0,0,455,454,1,0,0,0,455,456,1,0,0,0,456,457,
        1,0,0,0,457,459,5,41,0,0,458,460,3,20,10,0,459,458,1,0,0,0,460,461,
        1,0,0,0,461,459,1,0,0,0,461,462,1,0,0,0,462,19,1,0,0,0,463,465,5,
        6,0,0,464,463,1,0,0,0,464,465,1,0,0,0,465,467,1,0,0,0,466,468,5,
        6,0,0,467,466,1,0,0,0,467,468,1,0,0,0,468,469,1,0,0,0,469,470,3,
        26,13,0,470,471,3,26,13,0,471,473,3,26,13,0,472,474,3,28,14,0,473,
        472,1,0,0,0,473,474,1,0,0,0,474,476,1,0,0,0,475,477,3,28,14,0,476,
        475,1,0,0,0,476,477,1,0,0,0,477,479,1,0,0,0,478,480,3,26,13,0,479,
        478,1,0,0,0,479,480,1,0,0,0,480,482,1,0,0,0,481,483,3,26,13,0,482,
        481,1,0,0,0,482,483,1,0,0,0,483,485,1,0,0,0,484,486,3,26,13,0,485,
        484,1,0,0,0,485,486,1,0,0,0,486,488,1,0,0,0,487,489,3,26,13,0,488,
        487,1,0,0,0,488,489,1,0,0,0,489,493,1,0,0,0,490,492,3,30,15,0,491,
        490,1,0,0,0,492,495,1,0,0,0,493,491,1,0,0,0,493,494,1,0,0,0,494,
        496,1,0,0,0,495,493,1,0,0,0,496,497,7,5,0,0,497,21,1,0,0,0,498,500,
        5,1,0,0,499,498,1,0,0,0,499,500,1,0,0,0,500,502,1,0,0,0,501,503,
        7,0,0,0,502,501,1,0,0,0,502,503,1,0,0,0,503,504,1,0,0,0,504,505,
        7,1,0,0,505,506,7,2,0,0,506,507,7,6,0,0,507,509,7,8,0,0,508,510,
        5,30,0,0,509,508,1,0,0,0,509,510,1,0,0,0,510,512,1,0,0,0,511,513,
        5,31,0,0,512,511,1,0,0,0,512,513,1,0,0,0,513,515,1,0,0,0,514,516,
        5,32,0,0,515,514,1,0,0,0,515,516,1,0,0,0,516,518,1,0,0,0,517,519,
        5,33,0,0,518,517,1,0,0,0,518,519,1,0,0,0,519,521,1,0,0,0,520,522,
        5,34,0,0,521,520,1,0,0,0,521,522,1,0,0,0,522,524,1,0,0,0,523,525,
        5,35,0,0,524,523,1,0,0,0,524,525,1,0,0,0,525,527,1,0,0,0,526,528,
        5,36,0,0,527,526,1,0,0,0,527,528,1,0,0,0,528,530,1,0,0,0,529,531,
        5,37,0,0,530,529,1,0,0,0,530,531,1,0,0,0,531,533,1,0,0,0,532,534,
        5,38,0,0,533,532,1,0,0,0,533,534,1,0,0,0,534,536,1,0,0,0,535,537,
        5,39,0,0,536,535,1,0,0,0,536,537,1,0,0,0,537,538,1,0,0,0,538,540,
        5,41,0,0,539,541,3,24,12,0,540,539,1,0,0,0,541,542,1,0,0,0,542,540,
        1,0,0,0,542,543,1,0,0,0,543,23,1,0,0,0,544,546,5,6,0,0,545,544,1,
        0,0,0,545,546,1,0,0,0,546,548,1,0,0,0,547,549,5,6,0,0,548,547,1,
        0,0,0,548,549,1,0,0,0,549,550,1,0,0,0,550,551,3,26,13,0,551,552,
        3,26,13,0,552,553,3,26,13,0,553,555,3,26,13,0,554,556,3,28,14,0,
        555,554,1,0,0,0,555,556,1,0,0,0,556,558,1,0,0,0,557,559,3,28,14,
        0,558,557,1,0,0,0,558,559,1,0,0,0,559,561,1,0,0,0,560,562,3,26,13,
        0,561,560,1,0,0,0,561,562,1,0,0,0,562,564,1,0,0,0,563,565,3,26,13,
        0,564,563,1,0,0,0,564,565,1,0,0,0,565,567,1,0,0,0,566,568,3,26,13,
        0,567,566,1,0,0,0,567,568,1,0,0,0,568,570,1,0,0,0,569,571,3,26,13,
        0,570,569,1,0,0,0,570,571,1,0,0,0,571,573,1,0,0,0,572,574,3,26,13,
        0,573,572,1,0,0,0,573,574,1,0,0,0,574,578,1,0,0,0,575,577,3,30,15,
        0,576,575,1,0,0,0,577,580,1,0,0,0,578,576,1,0,0,0,578,579,1,0,0,
        0,579,581,1,0,0,0,580,578,1,0,0,0,581,582,7,5,0,0,582,25,1,0,0,0,
        583,584,7,9,0,0,584,27,1,0,0,0,585,586,7,9,0,0,586,29,1,0,0,0,587,
        588,7,10,0,0,588,31,1,0,0,0,135,33,42,44,50,53,63,66,69,72,75,78,
        81,84,87,93,96,99,111,114,117,120,123,126,131,137,140,154,157,160,
        163,166,169,172,175,178,181,187,190,193,209,212,215,218,221,224,
        227,232,238,241,259,262,265,268,271,274,277,280,283,286,289,295,
        298,301,321,324,327,330,333,336,339,342,347,353,356,361,364,367,
        370,373,376,379,382,388,391,394,399,402,405,408,411,416,422,425,
        431,434,437,440,443,446,449,452,455,461,464,467,473,476,479,482,
        485,488,493,499,502,509,512,515,518,521,524,527,530,533,536,542,
        545,548,555,558,561,564,567,570,573,578
    ]

class CcpnPKParser ( Parser ):

    grammarFileName = "CcpnPKParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Number'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'Position F2'", 
                     "'Position F3'", "'Position F4'", "<INVALID>", "'Shift F2'", 
                     "'Shift F3'", "'Shift F4'", "<INVALID>", "'Assign F2'", 
                     "'Assign F3'", "'Assign F4'", "'Height'", "'Volume'", 
                     "'Line Width F1 (Hz)'", "'Line Width F2 (Hz)'", "'Line Width F3 (Hz)'", 
                     "'Line Width F4 (Hz)'", "'Merit'", "'Details'", "'Fit Method'", 
                     "'Vol. Method'" ]

    symbolicNames = [ "<INVALID>", "Num", "Id", "Assign_F1", "Position_F1", 
                      "Shift_F1", "Integer", "Float", "Real", "EXCLM_COMMENT", 
                      "SMCLN_COMMENT", "Simple_name", "Any_name", "SPACE", 
                      "RETURN", "SECTION_COMMENT", "LINE_COMMENT", "Id_", 
                      "Position_F1_", "Position_F2", "Position_F3", "Position_F4", 
                      "Shift_F1_", "Shift_F2", "Shift_F3", "Shift_F4", "Assign_F1_", 
                      "Assign_F2", "Assign_F3", "Assign_F4", "Height", "Volume", 
                      "Line_width_F1", "Line_width_F2", "Line_width_F3", 
                      "Line_width_F4", "Merit", "Details", "Fit_method", 
                      "Vol_method", "SPACE_VARS", "RETURN_VARS" ]

    RULE_ccpn_pk = 0
    RULE_peak_list_2d = 1
    RULE_peak_2d = 2
    RULE_peak_list_3d = 3
    RULE_peak_3d = 4
    RULE_peak_list_4d = 5
    RULE_peak_4d = 6
    RULE_peak_list_wo_assign_2d = 7
    RULE_peak_wo_assign_2d = 8
    RULE_peak_list_wo_assign_3d = 9
    RULE_peak_wo_assign_3d = 10
    RULE_peak_list_wo_assign_4d = 11
    RULE_peak_wo_assign_4d = 12
    RULE_position = 13
    RULE_number = 14
    RULE_note = 15

    ruleNames =  [ "ccpn_pk", "peak_list_2d", "peak_2d", "peak_list_3d", 
                   "peak_3d", "peak_list_4d", "peak_4d", "peak_list_wo_assign_2d", 
                   "peak_wo_assign_2d", "peak_list_wo_assign_3d", "peak_wo_assign_3d", 
                   "peak_list_wo_assign_4d", "peak_wo_assign_4d", "position", 
                   "number", "note" ]

    EOF = Token.EOF
    Num=1
    Id=2
    Assign_F1=3
    Position_F1=4
    Shift_F1=5
    Integer=6
    Float=7
    Real=8
    EXCLM_COMMENT=9
    SMCLN_COMMENT=10
    Simple_name=11
    Any_name=12
    SPACE=13
    RETURN=14
    SECTION_COMMENT=15
    LINE_COMMENT=16
    Id_=17
    Position_F1_=18
    Position_F2=19
    Position_F3=20
    Position_F4=21
    Shift_F1_=22
    Shift_F2=23
    Shift_F3=24
    Shift_F4=25
    Assign_F1_=26
    Assign_F2=27
    Assign_F3=28
    Assign_F4=29
    Height=30
    Volume=31
    Line_width_F1=32
    Line_width_F2=33
    Line_width_F3=34
    Line_width_F4=35
    Merit=36
    Details=37
    Fit_method=38
    Vol_method=39
    SPACE_VARS=40
    RETURN_VARS=41

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Ccpn_pkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CcpnPKParser.EOF, 0)

        def RETURN(self, i:int=None):
            if i is None:
                return self.getTokens(CcpnPKParser.RETURN)
            else:
                return self.getToken(CcpnPKParser.RETURN, i)

        def peak_list_2d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.Peak_list_2dContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.Peak_list_2dContext,i)


        def peak_list_3d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.Peak_list_3dContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.Peak_list_3dContext,i)


        def peak_list_4d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.Peak_list_4dContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.Peak_list_4dContext,i)


        def peak_list_wo_assign_2d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.Peak_list_wo_assign_2dContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.Peak_list_wo_assign_2dContext,i)


        def peak_list_wo_assign_3d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.Peak_list_wo_assign_3dContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.Peak_list_wo_assign_3dContext,i)


        def peak_list_wo_assign_4d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.Peak_list_wo_assign_4dContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.Peak_list_wo_assign_4dContext,i)


        def getRuleIndex(self):
            return CcpnPKParser.RULE_ccpn_pk

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCcpn_pk" ):
                listener.enterCcpn_pk(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCcpn_pk" ):
                listener.exitCcpn_pk(self)




    def ccpn_pk(self):

        localctx = CcpnPKParser.Ccpn_pkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_ccpn_pk)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 32
                self.match(CcpnPKParser.RETURN)


            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 71712830) != 0):
                self.state = 42
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 35
                    self.peak_list_2d()
                    pass

                elif la_ == 2:
                    self.state = 36
                    self.peak_list_3d()
                    pass

                elif la_ == 3:
                    self.state = 37
                    self.peak_list_4d()
                    pass

                elif la_ == 4:
                    self.state = 38
                    self.peak_list_wo_assign_2d()
                    pass

                elif la_ == 5:
                    self.state = 39
                    self.peak_list_wo_assign_3d()
                    pass

                elif la_ == 6:
                    self.state = 40
                    self.peak_list_wo_assign_4d()
                    pass

                elif la_ == 7:
                    self.state = 41
                    self.match(CcpnPKParser.RETURN)
                    pass


                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 47
            self.match(CcpnPKParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Peak_list_2dContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_VARS(self):
            return self.getToken(CcpnPKParser.RETURN_VARS, 0)

        def Num(self):
            return self.getToken(CcpnPKParser.Num, 0)

        def Height(self):
            return self.getToken(CcpnPKParser.Height, 0)

        def Volume(self):
            return self.getToken(CcpnPKParser.Volume, 0)

        def Line_width_F1(self):
            return self.getToken(CcpnPKParser.Line_width_F1, 0)

        def Line_width_F2(self):
            return self.getToken(CcpnPKParser.Line_width_F2, 0)

        def Merit(self):
            return self.getToken(CcpnPKParser.Merit, 0)

        def Details(self):
            return self.getToken(CcpnPKParser.Details, 0)

        def Fit_method(self):
            return self.getToken(CcpnPKParser.Fit_method, 0)

        def Vol_method(self):
            return self.getToken(CcpnPKParser.Vol_method, 0)

        def peak_2d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.Peak_2dContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.Peak_2dContext,i)


        def Id(self):
            return self.getToken(CcpnPKParser.Id, 0)

        def Id_(self):
            return self.getToken(CcpnPKParser.Id_, 0)

        def Assign_F1_(self):
            return self.getToken(CcpnPKParser.Assign_F1_, 0)

        def Assign_F2(self):
            return self.getToken(CcpnPKParser.Assign_F2, 0)

        def Position_F1(self):
            return self.getToken(CcpnPKParser.Position_F1, 0)

        def Shift_F1(self):
            return self.getToken(CcpnPKParser.Shift_F1, 0)

        def Position_F1_(self):
            return self.getToken(CcpnPKParser.Position_F1_, 0)

        def Shift_F1_(self):
            return self.getToken(CcpnPKParser.Shift_F1_, 0)

        def Position_F2(self):
            return self.getToken(CcpnPKParser.Position_F2, 0)

        def Shift_F2(self):
            return self.getToken(CcpnPKParser.Shift_F2, 0)

        def Assign_F1(self):
            return self.getToken(CcpnPKParser.Assign_F1, 0)

        def getRuleIndex(self):
            return CcpnPKParser.RULE_peak_list_2d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_list_2d" ):
                listener.enterPeak_list_2d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_list_2d" ):
                listener.exitPeak_list_2d(self)




    def peak_list_2d(self):

        localctx = CcpnPKParser.Peak_list_2dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_peak_list_2d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 49
                self.match(CcpnPKParser.Num)


            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2 or _la==17:
                self.state = 52
                _la = self._input.LA(1)
                if not(_la==2 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 18, 22]:
                self.state = 55
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4456496) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 56
                _la = self._input.LA(1)
                if not(_la==19 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 57
                self.match(CcpnPKParser.Assign_F1_)
                self.state = 58
                self.match(CcpnPKParser.Assign_F2)
                pass
            elif token in [3, 26]:
                self.state = 59
                _la = self._input.LA(1)
                if not(_la==3 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 60
                self.match(CcpnPKParser.Assign_F2)
                self.state = 61
                _la = self._input.LA(1)
                if not(_la==18 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 62
                _la = self._input.LA(1)
                if not(_la==19 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 65
                self.match(CcpnPKParser.Height)


            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 68
                self.match(CcpnPKParser.Volume)


            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 71
                self.match(CcpnPKParser.Line_width_F1)


            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 74
                self.match(CcpnPKParser.Line_width_F2)


            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 77
                self.match(CcpnPKParser.Merit)


            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 80
                self.match(CcpnPKParser.Details)


            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 83
                self.match(CcpnPKParser.Fit_method)


            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 86
                self.match(CcpnPKParser.Vol_method)


            self.state = 89
            self.match(CcpnPKParser.RETURN_VARS)
            self.state = 91 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 90
                self.peak_2d()
                self.state = 93 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2496) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Peak_2dContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(CcpnPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(CcpnPKParser.EOF, 0)

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(CcpnPKParser.Integer)
            else:
                return self.getToken(CcpnPKParser.Integer, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.NumberContext,i)


        def position(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.PositionContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.PositionContext,i)


        def note(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.NoteContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.NoteContext,i)


        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(CcpnPKParser.Simple_name)
            else:
                return self.getToken(CcpnPKParser.Simple_name, i)

        def getRuleIndex(self):
            return CcpnPKParser.RULE_peak_2d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_2d" ):
                listener.enterPeak_2d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_2d" ):
                listener.exitPeak_2d(self)




    def peak_2d(self):

        localctx = CcpnPKParser.Peak_2dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_peak_2d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 95
                self.match(CcpnPKParser.Integer)


            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 98
                self.match(CcpnPKParser.Integer)


            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 101
                self.position()
                self.state = 102
                self.position()
                self.state = 103
                self.match(CcpnPKParser.Simple_name)
                self.state = 104
                self.match(CcpnPKParser.Simple_name)
                pass

            elif la_ == 2:
                self.state = 106
                self.match(CcpnPKParser.Simple_name)
                self.state = 107
                self.match(CcpnPKParser.Simple_name)
                self.state = 108
                self.position()
                self.state = 109
                self.position()
                pass


            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 113
                self.number()


            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 116
                self.number()


            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 119
                self.position()


            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 122
                self.position()


            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 125
                self.position()


            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6592) != 0):
                self.state = 128
                self.note()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 134
            _la = self._input.LA(1)
            if not(_la==-1 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Peak_list_3dContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_VARS(self):
            return self.getToken(CcpnPKParser.RETURN_VARS, 0)

        def Num(self):
            return self.getToken(CcpnPKParser.Num, 0)

        def Height(self):
            return self.getToken(CcpnPKParser.Height, 0)

        def Volume(self):
            return self.getToken(CcpnPKParser.Volume, 0)

        def Line_width_F1(self):
            return self.getToken(CcpnPKParser.Line_width_F1, 0)

        def Line_width_F2(self):
            return self.getToken(CcpnPKParser.Line_width_F2, 0)

        def Line_width_F3(self):
            return self.getToken(CcpnPKParser.Line_width_F3, 0)

        def Merit(self):
            return self.getToken(CcpnPKParser.Merit, 0)

        def Details(self):
            return self.getToken(CcpnPKParser.Details, 0)

        def Fit_method(self):
            return self.getToken(CcpnPKParser.Fit_method, 0)

        def Vol_method(self):
            return self.getToken(CcpnPKParser.Vol_method, 0)

        def peak_3d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.Peak_3dContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.Peak_3dContext,i)


        def Id(self):
            return self.getToken(CcpnPKParser.Id, 0)

        def Id_(self):
            return self.getToken(CcpnPKParser.Id_, 0)

        def Assign_F1_(self):
            return self.getToken(CcpnPKParser.Assign_F1_, 0)

        def Assign_F2(self):
            return self.getToken(CcpnPKParser.Assign_F2, 0)

        def Assign_F3(self):
            return self.getToken(CcpnPKParser.Assign_F3, 0)

        def Position_F1(self):
            return self.getToken(CcpnPKParser.Position_F1, 0)

        def Shift_F1(self):
            return self.getToken(CcpnPKParser.Shift_F1, 0)

        def Position_F1_(self):
            return self.getToken(CcpnPKParser.Position_F1_, 0)

        def Shift_F1_(self):
            return self.getToken(CcpnPKParser.Shift_F1_, 0)

        def Position_F2(self):
            return self.getToken(CcpnPKParser.Position_F2, 0)

        def Shift_F2(self):
            return self.getToken(CcpnPKParser.Shift_F2, 0)

        def Position_F3(self):
            return self.getToken(CcpnPKParser.Position_F3, 0)

        def Shift_F3(self):
            return self.getToken(CcpnPKParser.Shift_F3, 0)

        def Assign_F1(self):
            return self.getToken(CcpnPKParser.Assign_F1, 0)

        def getRuleIndex(self):
            return CcpnPKParser.RULE_peak_list_3d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_list_3d" ):
                listener.enterPeak_list_3d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_list_3d" ):
                listener.exitPeak_list_3d(self)




    def peak_list_3d(self):

        localctx = CcpnPKParser.Peak_list_3dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_peak_list_3d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 136
                self.match(CcpnPKParser.Num)


            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2 or _la==17:
                self.state = 139
                _la = self._input.LA(1)
                if not(_la==2 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 18, 22]:
                self.state = 142
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4456496) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 143
                _la = self._input.LA(1)
                if not(_la==19 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 144
                _la = self._input.LA(1)
                if not(_la==20 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 145
                self.match(CcpnPKParser.Assign_F1_)
                self.state = 146
                self.match(CcpnPKParser.Assign_F2)
                self.state = 147
                self.match(CcpnPKParser.Assign_F3)
                pass
            elif token in [3, 26]:
                self.state = 148
                _la = self._input.LA(1)
                if not(_la==3 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 149
                self.match(CcpnPKParser.Assign_F2)
                self.state = 150
                self.match(CcpnPKParser.Assign_F3)
                self.state = 151
                _la = self._input.LA(1)
                if not(_la==5 or _la==18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 152
                _la = self._input.LA(1)
                if not(_la==19 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 153
                _la = self._input.LA(1)
                if not(_la==20 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 156
                self.match(CcpnPKParser.Height)


            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 159
                self.match(CcpnPKParser.Volume)


            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 162
                self.match(CcpnPKParser.Line_width_F1)


            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 165
                self.match(CcpnPKParser.Line_width_F2)


            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 168
                self.match(CcpnPKParser.Line_width_F3)


            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 171
                self.match(CcpnPKParser.Merit)


            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 174
                self.match(CcpnPKParser.Details)


            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 177
                self.match(CcpnPKParser.Fit_method)


            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 180
                self.match(CcpnPKParser.Vol_method)


            self.state = 183
            self.match(CcpnPKParser.RETURN_VARS)
            self.state = 185 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 184
                self.peak_3d()
                self.state = 187 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2496) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Peak_3dContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(CcpnPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(CcpnPKParser.EOF, 0)

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(CcpnPKParser.Integer)
            else:
                return self.getToken(CcpnPKParser.Integer, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.NumberContext,i)


        def position(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.PositionContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.PositionContext,i)


        def note(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.NoteContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.NoteContext,i)


        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(CcpnPKParser.Simple_name)
            else:
                return self.getToken(CcpnPKParser.Simple_name, i)

        def getRuleIndex(self):
            return CcpnPKParser.RULE_peak_3d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_3d" ):
                listener.enterPeak_3d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_3d" ):
                listener.exitPeak_3d(self)




    def peak_3d(self):

        localctx = CcpnPKParser.Peak_3dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_peak_3d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 189
                self.match(CcpnPKParser.Integer)


            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 192
                self.match(CcpnPKParser.Integer)


            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 195
                self.position()
                self.state = 196
                self.position()
                self.state = 197
                self.position()
                self.state = 198
                self.match(CcpnPKParser.Simple_name)
                self.state = 199
                self.match(CcpnPKParser.Simple_name)
                self.state = 200
                self.match(CcpnPKParser.Simple_name)
                pass

            elif la_ == 2:
                self.state = 202
                self.match(CcpnPKParser.Simple_name)
                self.state = 203
                self.match(CcpnPKParser.Simple_name)
                self.state = 204
                self.match(CcpnPKParser.Simple_name)
                self.state = 205
                self.position()
                self.state = 206
                self.position()
                self.state = 207
                self.position()
                pass


            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 211
                self.number()


            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 214
                self.number()


            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 217
                self.position()


            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 220
                self.position()


            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 223
                self.position()


            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 226
                self.position()


            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6592) != 0):
                self.state = 229
                self.note()
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 235
            _la = self._input.LA(1)
            if not(_la==-1 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Peak_list_4dContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_VARS(self):
            return self.getToken(CcpnPKParser.RETURN_VARS, 0)

        def Num(self):
            return self.getToken(CcpnPKParser.Num, 0)

        def Height(self):
            return self.getToken(CcpnPKParser.Height, 0)

        def Volume(self):
            return self.getToken(CcpnPKParser.Volume, 0)

        def Line_width_F1(self):
            return self.getToken(CcpnPKParser.Line_width_F1, 0)

        def Line_width_F2(self):
            return self.getToken(CcpnPKParser.Line_width_F2, 0)

        def Line_width_F3(self):
            return self.getToken(CcpnPKParser.Line_width_F3, 0)

        def Line_width_F4(self):
            return self.getToken(CcpnPKParser.Line_width_F4, 0)

        def Merit(self):
            return self.getToken(CcpnPKParser.Merit, 0)

        def Details(self):
            return self.getToken(CcpnPKParser.Details, 0)

        def Fit_method(self):
            return self.getToken(CcpnPKParser.Fit_method, 0)

        def Vol_method(self):
            return self.getToken(CcpnPKParser.Vol_method, 0)

        def peak_4d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.Peak_4dContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.Peak_4dContext,i)


        def Id(self):
            return self.getToken(CcpnPKParser.Id, 0)

        def Id_(self):
            return self.getToken(CcpnPKParser.Id_, 0)

        def Assign_F1_(self):
            return self.getToken(CcpnPKParser.Assign_F1_, 0)

        def Assign_F2(self):
            return self.getToken(CcpnPKParser.Assign_F2, 0)

        def Assign_F3(self):
            return self.getToken(CcpnPKParser.Assign_F3, 0)

        def Assign_F4(self):
            return self.getToken(CcpnPKParser.Assign_F4, 0)

        def Position_F1(self):
            return self.getToken(CcpnPKParser.Position_F1, 0)

        def Shift_F1(self):
            return self.getToken(CcpnPKParser.Shift_F1, 0)

        def Position_F1_(self):
            return self.getToken(CcpnPKParser.Position_F1_, 0)

        def Shift_F1_(self):
            return self.getToken(CcpnPKParser.Shift_F1_, 0)

        def Position_F2(self):
            return self.getToken(CcpnPKParser.Position_F2, 0)

        def Shift_F2(self):
            return self.getToken(CcpnPKParser.Shift_F2, 0)

        def Position_F3(self):
            return self.getToken(CcpnPKParser.Position_F3, 0)

        def Shift_F3(self):
            return self.getToken(CcpnPKParser.Shift_F3, 0)

        def Position_F4(self):
            return self.getToken(CcpnPKParser.Position_F4, 0)

        def Shift_F4(self):
            return self.getToken(CcpnPKParser.Shift_F4, 0)

        def Assign_F1(self):
            return self.getToken(CcpnPKParser.Assign_F1, 0)

        def getRuleIndex(self):
            return CcpnPKParser.RULE_peak_list_4d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_list_4d" ):
                listener.enterPeak_list_4d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_list_4d" ):
                listener.exitPeak_list_4d(self)




    def peak_list_4d(self):

        localctx = CcpnPKParser.Peak_list_4dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_peak_list_4d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 237
                self.match(CcpnPKParser.Num)


            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2 or _la==17:
                self.state = 240
                _la = self._input.LA(1)
                if not(_la==2 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 18, 22]:
                self.state = 243
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4456496) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 244
                _la = self._input.LA(1)
                if not(_la==19 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 245
                _la = self._input.LA(1)
                if not(_la==20 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 246
                _la = self._input.LA(1)
                if not(_la==21 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 247
                self.match(CcpnPKParser.Assign_F1_)
                self.state = 248
                self.match(CcpnPKParser.Assign_F2)
                self.state = 249
                self.match(CcpnPKParser.Assign_F3)
                self.state = 250
                self.match(CcpnPKParser.Assign_F4)
                pass
            elif token in [3, 26]:
                self.state = 251
                _la = self._input.LA(1)
                if not(_la==3 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 252
                self.match(CcpnPKParser.Assign_F2)
                self.state = 253
                self.match(CcpnPKParser.Assign_F3)
                self.state = 254
                self.match(CcpnPKParser.Assign_F4)
                self.state = 255
                _la = self._input.LA(1)
                if not(_la==5 or _la==18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 256
                _la = self._input.LA(1)
                if not(_la==19 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 257
                _la = self._input.LA(1)
                if not(_la==20 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 258
                _la = self._input.LA(1)
                if not(_la==21 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 261
                self.match(CcpnPKParser.Height)


            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 264
                self.match(CcpnPKParser.Volume)


            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 267
                self.match(CcpnPKParser.Line_width_F1)


            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 270
                self.match(CcpnPKParser.Line_width_F2)


            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 273
                self.match(CcpnPKParser.Line_width_F3)


            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 276
                self.match(CcpnPKParser.Line_width_F4)


            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 279
                self.match(CcpnPKParser.Merit)


            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 282
                self.match(CcpnPKParser.Details)


            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 285
                self.match(CcpnPKParser.Fit_method)


            self.state = 289
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 288
                self.match(CcpnPKParser.Vol_method)


            self.state = 291
            self.match(CcpnPKParser.RETURN_VARS)
            self.state = 293 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 292
                self.peak_4d()
                self.state = 295 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2496) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Peak_4dContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(CcpnPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(CcpnPKParser.EOF, 0)

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(CcpnPKParser.Integer)
            else:
                return self.getToken(CcpnPKParser.Integer, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.NumberContext,i)


        def position(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.PositionContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.PositionContext,i)


        def note(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.NoteContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.NoteContext,i)


        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(CcpnPKParser.Simple_name)
            else:
                return self.getToken(CcpnPKParser.Simple_name, i)

        def getRuleIndex(self):
            return CcpnPKParser.RULE_peak_4d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_4d" ):
                listener.enterPeak_4d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_4d" ):
                listener.exitPeak_4d(self)




    def peak_4d(self):

        localctx = CcpnPKParser.Peak_4dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_peak_4d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.state = 297
                self.match(CcpnPKParser.Integer)


            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                self.state = 300
                self.match(CcpnPKParser.Integer)


            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.state = 303
                self.position()
                self.state = 304
                self.position()
                self.state = 305
                self.position()
                self.state = 306
                self.position()
                self.state = 307
                self.match(CcpnPKParser.Simple_name)
                self.state = 308
                self.match(CcpnPKParser.Simple_name)
                self.state = 309
                self.match(CcpnPKParser.Simple_name)
                self.state = 310
                self.match(CcpnPKParser.Simple_name)
                pass

            elif la_ == 2:
                self.state = 312
                self.match(CcpnPKParser.Simple_name)
                self.state = 313
                self.match(CcpnPKParser.Simple_name)
                self.state = 314
                self.match(CcpnPKParser.Simple_name)
                self.state = 315
                self.match(CcpnPKParser.Simple_name)
                self.state = 316
                self.position()
                self.state = 317
                self.position()
                self.state = 318
                self.position()
                self.state = 319
                self.position()
                pass


            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.state = 323
                self.number()


            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.state = 326
                self.number()


            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                self.state = 329
                self.position()


            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.state = 332
                self.position()


            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
            if la_ == 1:
                self.state = 335
                self.position()


            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
            if la_ == 1:
                self.state = 338
                self.position()


            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
            if la_ == 1:
                self.state = 341
                self.position()


            self.state = 347
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6592) != 0):
                self.state = 344
                self.note()
                self.state = 349
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 350
            _la = self._input.LA(1)
            if not(_la==-1 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Peak_list_wo_assign_2dContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_VARS(self):
            return self.getToken(CcpnPKParser.RETURN_VARS, 0)

        def Position_F1(self):
            return self.getToken(CcpnPKParser.Position_F1, 0)

        def Shift_F1(self):
            return self.getToken(CcpnPKParser.Shift_F1, 0)

        def Position_F1_(self):
            return self.getToken(CcpnPKParser.Position_F1_, 0)

        def Shift_F1_(self):
            return self.getToken(CcpnPKParser.Shift_F1_, 0)

        def Position_F2(self):
            return self.getToken(CcpnPKParser.Position_F2, 0)

        def Shift_F2(self):
            return self.getToken(CcpnPKParser.Shift_F2, 0)

        def Num(self):
            return self.getToken(CcpnPKParser.Num, 0)

        def Height(self):
            return self.getToken(CcpnPKParser.Height, 0)

        def Volume(self):
            return self.getToken(CcpnPKParser.Volume, 0)

        def Line_width_F1(self):
            return self.getToken(CcpnPKParser.Line_width_F1, 0)

        def Line_width_F2(self):
            return self.getToken(CcpnPKParser.Line_width_F2, 0)

        def Merit(self):
            return self.getToken(CcpnPKParser.Merit, 0)

        def Details(self):
            return self.getToken(CcpnPKParser.Details, 0)

        def Fit_method(self):
            return self.getToken(CcpnPKParser.Fit_method, 0)

        def Vol_method(self):
            return self.getToken(CcpnPKParser.Vol_method, 0)

        def peak_wo_assign_2d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.Peak_wo_assign_2dContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.Peak_wo_assign_2dContext,i)


        def Id(self):
            return self.getToken(CcpnPKParser.Id, 0)

        def Id_(self):
            return self.getToken(CcpnPKParser.Id_, 0)

        def getRuleIndex(self):
            return CcpnPKParser.RULE_peak_list_wo_assign_2d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_list_wo_assign_2d" ):
                listener.enterPeak_list_wo_assign_2d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_list_wo_assign_2d" ):
                listener.exitPeak_list_wo_assign_2d(self)




    def peak_list_wo_assign_2d(self):

        localctx = CcpnPKParser.Peak_list_wo_assign_2dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_peak_list_wo_assign_2d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 352
                self.match(CcpnPKParser.Num)


            self.state = 356
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2 or _la==17:
                self.state = 355
                _la = self._input.LA(1)
                if not(_la==2 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 358
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4456496) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 359
            _la = self._input.LA(1)
            if not(_la==19 or _la==23):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 361
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 360
                self.match(CcpnPKParser.Height)


            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 363
                self.match(CcpnPKParser.Volume)


            self.state = 367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 366
                self.match(CcpnPKParser.Line_width_F1)


            self.state = 370
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 369
                self.match(CcpnPKParser.Line_width_F2)


            self.state = 373
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 372
                self.match(CcpnPKParser.Merit)


            self.state = 376
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 375
                self.match(CcpnPKParser.Details)


            self.state = 379
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 378
                self.match(CcpnPKParser.Fit_method)


            self.state = 382
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 381
                self.match(CcpnPKParser.Vol_method)


            self.state = 384
            self.match(CcpnPKParser.RETURN_VARS)
            self.state = 386 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 385
                self.peak_wo_assign_2d()
                self.state = 388 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2496) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Peak_wo_assign_2dContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def position(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.PositionContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.PositionContext,i)


        def RETURN(self):
            return self.getToken(CcpnPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(CcpnPKParser.EOF, 0)

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(CcpnPKParser.Integer)
            else:
                return self.getToken(CcpnPKParser.Integer, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.NumberContext,i)


        def note(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.NoteContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.NoteContext,i)


        def getRuleIndex(self):
            return CcpnPKParser.RULE_peak_wo_assign_2d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_wo_assign_2d" ):
                listener.enterPeak_wo_assign_2d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_wo_assign_2d" ):
                listener.exitPeak_wo_assign_2d(self)




    def peak_wo_assign_2d(self):

        localctx = CcpnPKParser.Peak_wo_assign_2dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_peak_wo_assign_2d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,83,self._ctx)
            if la_ == 1:
                self.state = 390
                self.match(CcpnPKParser.Integer)


            self.state = 394
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,84,self._ctx)
            if la_ == 1:
                self.state = 393
                self.match(CcpnPKParser.Integer)


            self.state = 396
            self.position()
            self.state = 397
            self.position()
            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,85,self._ctx)
            if la_ == 1:
                self.state = 398
                self.number()


            self.state = 402
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,86,self._ctx)
            if la_ == 1:
                self.state = 401
                self.number()


            self.state = 405
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,87,self._ctx)
            if la_ == 1:
                self.state = 404
                self.position()


            self.state = 408
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,88,self._ctx)
            if la_ == 1:
                self.state = 407
                self.position()


            self.state = 411
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,89,self._ctx)
            if la_ == 1:
                self.state = 410
                self.position()


            self.state = 416
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6592) != 0):
                self.state = 413
                self.note()
                self.state = 418
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 419
            _la = self._input.LA(1)
            if not(_la==-1 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Peak_list_wo_assign_3dContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_VARS(self):
            return self.getToken(CcpnPKParser.RETURN_VARS, 0)

        def Position_F1(self):
            return self.getToken(CcpnPKParser.Position_F1, 0)

        def Shift_F1(self):
            return self.getToken(CcpnPKParser.Shift_F1, 0)

        def Position_F1_(self):
            return self.getToken(CcpnPKParser.Position_F1_, 0)

        def Shift_F1_(self):
            return self.getToken(CcpnPKParser.Shift_F1_, 0)

        def Position_F2(self):
            return self.getToken(CcpnPKParser.Position_F2, 0)

        def Shift_F2(self):
            return self.getToken(CcpnPKParser.Shift_F2, 0)

        def Position_F3(self):
            return self.getToken(CcpnPKParser.Position_F3, 0)

        def Shift_F3(self):
            return self.getToken(CcpnPKParser.Shift_F3, 0)

        def Num(self):
            return self.getToken(CcpnPKParser.Num, 0)

        def Height(self):
            return self.getToken(CcpnPKParser.Height, 0)

        def Volume(self):
            return self.getToken(CcpnPKParser.Volume, 0)

        def Line_width_F1(self):
            return self.getToken(CcpnPKParser.Line_width_F1, 0)

        def Line_width_F2(self):
            return self.getToken(CcpnPKParser.Line_width_F2, 0)

        def Line_width_F3(self):
            return self.getToken(CcpnPKParser.Line_width_F3, 0)

        def Merit(self):
            return self.getToken(CcpnPKParser.Merit, 0)

        def Details(self):
            return self.getToken(CcpnPKParser.Details, 0)

        def Fit_method(self):
            return self.getToken(CcpnPKParser.Fit_method, 0)

        def Vol_method(self):
            return self.getToken(CcpnPKParser.Vol_method, 0)

        def peak_wo_assign_3d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.Peak_wo_assign_3dContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.Peak_wo_assign_3dContext,i)


        def Id(self):
            return self.getToken(CcpnPKParser.Id, 0)

        def Id_(self):
            return self.getToken(CcpnPKParser.Id_, 0)

        def getRuleIndex(self):
            return CcpnPKParser.RULE_peak_list_wo_assign_3d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_list_wo_assign_3d" ):
                listener.enterPeak_list_wo_assign_3d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_list_wo_assign_3d" ):
                listener.exitPeak_list_wo_assign_3d(self)




    def peak_list_wo_assign_3d(self):

        localctx = CcpnPKParser.Peak_list_wo_assign_3dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_peak_list_wo_assign_3d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 421
                self.match(CcpnPKParser.Num)


            self.state = 425
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2 or _la==17:
                self.state = 424
                _la = self._input.LA(1)
                if not(_la==2 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 427
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4456496) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 428
            _la = self._input.LA(1)
            if not(_la==19 or _la==23):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 429
            _la = self._input.LA(1)
            if not(_la==20 or _la==24):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 431
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 430
                self.match(CcpnPKParser.Height)


            self.state = 434
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 433
                self.match(CcpnPKParser.Volume)


            self.state = 437
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 436
                self.match(CcpnPKParser.Line_width_F1)


            self.state = 440
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 439
                self.match(CcpnPKParser.Line_width_F2)


            self.state = 443
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 442
                self.match(CcpnPKParser.Line_width_F3)


            self.state = 446
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 445
                self.match(CcpnPKParser.Merit)


            self.state = 449
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 448
                self.match(CcpnPKParser.Details)


            self.state = 452
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 451
                self.match(CcpnPKParser.Fit_method)


            self.state = 455
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 454
                self.match(CcpnPKParser.Vol_method)


            self.state = 457
            self.match(CcpnPKParser.RETURN_VARS)
            self.state = 459 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 458
                self.peak_wo_assign_3d()
                self.state = 461 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2496) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Peak_wo_assign_3dContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def position(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.PositionContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.PositionContext,i)


        def RETURN(self):
            return self.getToken(CcpnPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(CcpnPKParser.EOF, 0)

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(CcpnPKParser.Integer)
            else:
                return self.getToken(CcpnPKParser.Integer, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.NumberContext,i)


        def note(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.NoteContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.NoteContext,i)


        def getRuleIndex(self):
            return CcpnPKParser.RULE_peak_wo_assign_3d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_wo_assign_3d" ):
                listener.enterPeak_wo_assign_3d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_wo_assign_3d" ):
                listener.exitPeak_wo_assign_3d(self)




    def peak_wo_assign_3d(self):

        localctx = CcpnPKParser.Peak_wo_assign_3dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_peak_wo_assign_3d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,103,self._ctx)
            if la_ == 1:
                self.state = 463
                self.match(CcpnPKParser.Integer)


            self.state = 467
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,104,self._ctx)
            if la_ == 1:
                self.state = 466
                self.match(CcpnPKParser.Integer)


            self.state = 469
            self.position()
            self.state = 470
            self.position()
            self.state = 471
            self.position()
            self.state = 473
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,105,self._ctx)
            if la_ == 1:
                self.state = 472
                self.number()


            self.state = 476
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,106,self._ctx)
            if la_ == 1:
                self.state = 475
                self.number()


            self.state = 479
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,107,self._ctx)
            if la_ == 1:
                self.state = 478
                self.position()


            self.state = 482
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,108,self._ctx)
            if la_ == 1:
                self.state = 481
                self.position()


            self.state = 485
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,109,self._ctx)
            if la_ == 1:
                self.state = 484
                self.position()


            self.state = 488
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,110,self._ctx)
            if la_ == 1:
                self.state = 487
                self.position()


            self.state = 493
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6592) != 0):
                self.state = 490
                self.note()
                self.state = 495
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 496
            _la = self._input.LA(1)
            if not(_la==-1 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Peak_list_wo_assign_4dContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_VARS(self):
            return self.getToken(CcpnPKParser.RETURN_VARS, 0)

        def Position_F1(self):
            return self.getToken(CcpnPKParser.Position_F1, 0)

        def Shift_F1(self):
            return self.getToken(CcpnPKParser.Shift_F1, 0)

        def Position_F1_(self):
            return self.getToken(CcpnPKParser.Position_F1_, 0)

        def Shift_F1_(self):
            return self.getToken(CcpnPKParser.Shift_F1_, 0)

        def Position_F2(self):
            return self.getToken(CcpnPKParser.Position_F2, 0)

        def Shift_F2(self):
            return self.getToken(CcpnPKParser.Shift_F2, 0)

        def Position_F3(self):
            return self.getToken(CcpnPKParser.Position_F3, 0)

        def Shift_F3(self):
            return self.getToken(CcpnPKParser.Shift_F3, 0)

        def Position_F4(self):
            return self.getToken(CcpnPKParser.Position_F4, 0)

        def Shift_F4(self):
            return self.getToken(CcpnPKParser.Shift_F4, 0)

        def Num(self):
            return self.getToken(CcpnPKParser.Num, 0)

        def Height(self):
            return self.getToken(CcpnPKParser.Height, 0)

        def Volume(self):
            return self.getToken(CcpnPKParser.Volume, 0)

        def Line_width_F1(self):
            return self.getToken(CcpnPKParser.Line_width_F1, 0)

        def Line_width_F2(self):
            return self.getToken(CcpnPKParser.Line_width_F2, 0)

        def Line_width_F3(self):
            return self.getToken(CcpnPKParser.Line_width_F3, 0)

        def Line_width_F4(self):
            return self.getToken(CcpnPKParser.Line_width_F4, 0)

        def Merit(self):
            return self.getToken(CcpnPKParser.Merit, 0)

        def Details(self):
            return self.getToken(CcpnPKParser.Details, 0)

        def Fit_method(self):
            return self.getToken(CcpnPKParser.Fit_method, 0)

        def Vol_method(self):
            return self.getToken(CcpnPKParser.Vol_method, 0)

        def peak_wo_assign_4d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.Peak_wo_assign_4dContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.Peak_wo_assign_4dContext,i)


        def Id(self):
            return self.getToken(CcpnPKParser.Id, 0)

        def Id_(self):
            return self.getToken(CcpnPKParser.Id_, 0)

        def getRuleIndex(self):
            return CcpnPKParser.RULE_peak_list_wo_assign_4d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_list_wo_assign_4d" ):
                listener.enterPeak_list_wo_assign_4d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_list_wo_assign_4d" ):
                listener.exitPeak_list_wo_assign_4d(self)




    def peak_list_wo_assign_4d(self):

        localctx = CcpnPKParser.Peak_list_wo_assign_4dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_peak_list_wo_assign_4d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 498
                self.match(CcpnPKParser.Num)


            self.state = 502
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2 or _la==17:
                self.state = 501
                _la = self._input.LA(1)
                if not(_la==2 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 504
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4456496) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 505
            _la = self._input.LA(1)
            if not(_la==19 or _la==23):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 506
            _la = self._input.LA(1)
            if not(_la==20 or _la==24):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 507
            _la = self._input.LA(1)
            if not(_la==21 or _la==25):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 509
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 508
                self.match(CcpnPKParser.Height)


            self.state = 512
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 511
                self.match(CcpnPKParser.Volume)


            self.state = 515
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 514
                self.match(CcpnPKParser.Line_width_F1)


            self.state = 518
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 517
                self.match(CcpnPKParser.Line_width_F2)


            self.state = 521
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 520
                self.match(CcpnPKParser.Line_width_F3)


            self.state = 524
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 523
                self.match(CcpnPKParser.Line_width_F4)


            self.state = 527
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 526
                self.match(CcpnPKParser.Merit)


            self.state = 530
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 529
                self.match(CcpnPKParser.Details)


            self.state = 533
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 532
                self.match(CcpnPKParser.Fit_method)


            self.state = 536
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 535
                self.match(CcpnPKParser.Vol_method)


            self.state = 538
            self.match(CcpnPKParser.RETURN_VARS)
            self.state = 540 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 539
                self.peak_wo_assign_4d()
                self.state = 542 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2496) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Peak_wo_assign_4dContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def position(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.PositionContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.PositionContext,i)


        def RETURN(self):
            return self.getToken(CcpnPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(CcpnPKParser.EOF, 0)

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(CcpnPKParser.Integer)
            else:
                return self.getToken(CcpnPKParser.Integer, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.NumberContext,i)


        def note(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.NoteContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.NoteContext,i)


        def getRuleIndex(self):
            return CcpnPKParser.RULE_peak_wo_assign_4d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_wo_assign_4d" ):
                listener.enterPeak_wo_assign_4d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_wo_assign_4d" ):
                listener.exitPeak_wo_assign_4d(self)




    def peak_wo_assign_4d(self):

        localctx = CcpnPKParser.Peak_wo_assign_4dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_peak_wo_assign_4d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,125,self._ctx)
            if la_ == 1:
                self.state = 544
                self.match(CcpnPKParser.Integer)


            self.state = 548
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,126,self._ctx)
            if la_ == 1:
                self.state = 547
                self.match(CcpnPKParser.Integer)


            self.state = 550
            self.position()
            self.state = 551
            self.position()
            self.state = 552
            self.position()
            self.state = 553
            self.position()
            self.state = 555
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,127,self._ctx)
            if la_ == 1:
                self.state = 554
                self.number()


            self.state = 558
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,128,self._ctx)
            if la_ == 1:
                self.state = 557
                self.number()


            self.state = 561
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,129,self._ctx)
            if la_ == 1:
                self.state = 560
                self.position()


            self.state = 564
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,130,self._ctx)
            if la_ == 1:
                self.state = 563
                self.position()


            self.state = 567
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,131,self._ctx)
            if la_ == 1:
                self.state = 566
                self.position()


            self.state = 570
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,132,self._ctx)
            if la_ == 1:
                self.state = 569
                self.position()


            self.state = 573
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,133,self._ctx)
            if la_ == 1:
                self.state = 572
                self.position()


            self.state = 578
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6592) != 0):
                self.state = 575
                self.note()
                self.state = 580
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 581
            _la = self._input.LA(1)
            if not(_la==-1 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PositionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Float(self):
            return self.getToken(CcpnPKParser.Float, 0)

        def Real(self):
            return self.getToken(CcpnPKParser.Real, 0)

        def Integer(self):
            return self.getToken(CcpnPKParser.Integer, 0)

        def Simple_name(self):
            return self.getToken(CcpnPKParser.Simple_name, 0)

        def getRuleIndex(self):
            return CcpnPKParser.RULE_position

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPosition" ):
                listener.enterPosition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPosition" ):
                listener.exitPosition(self)




    def position(self):

        localctx = CcpnPKParser.PositionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_position)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 583
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2496) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Float(self):
            return self.getToken(CcpnPKParser.Float, 0)

        def Real(self):
            return self.getToken(CcpnPKParser.Real, 0)

        def Integer(self):
            return self.getToken(CcpnPKParser.Integer, 0)

        def Simple_name(self):
            return self.getToken(CcpnPKParser.Simple_name, 0)

        def getRuleIndex(self):
            return CcpnPKParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = CcpnPKParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2496) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Float(self):
            return self.getToken(CcpnPKParser.Float, 0)

        def Real(self):
            return self.getToken(CcpnPKParser.Real, 0)

        def Integer(self):
            return self.getToken(CcpnPKParser.Integer, 0)

        def Simple_name(self):
            return self.getToken(CcpnPKParser.Simple_name, 0)

        def Any_name(self):
            return self.getToken(CcpnPKParser.Any_name, 0)

        def getRuleIndex(self):
            return CcpnPKParser.RULE_note

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNote" ):
                listener.enterNote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNote" ):
                listener.exitNote(self)




    def note(self):

        localctx = CcpnPKParser.NoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_note)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 587
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 6592) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





