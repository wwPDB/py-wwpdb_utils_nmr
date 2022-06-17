# Generated from PalesMRParser.g4 by ANTLR 4.10.1
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
        4,1,60,524,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,5,0,48,8,0,10,0,12,0,51,9,0,1,0,1,0,1,1,1,
        1,1,1,4,1,58,8,1,11,1,12,1,59,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,4,2,95,8,2,11,2,12,2,96,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,4,
        4,148,8,4,11,4,12,4,149,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,4,6,205,8,6,11,6,12,
        6,206,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,4,
        8,271,8,8,11,8,12,8,272,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,4,10,319,8,10,11,10,12,10,320,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,4,12,360,8,12,
        11,12,12,12,361,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,4,14,419,8,14,11,14,12,14,420,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,4,16,494,8,16,11,16,12,16,495,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,0,0,
        19,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,0,1,1,0,4,
        5,522,0,49,1,0,0,0,2,54,1,0,0,0,4,63,1,0,0,0,6,98,1,0,0,0,8,112,
        1,0,0,0,10,151,1,0,0,0,12,167,1,0,0,0,14,208,1,0,0,0,16,225,1,0,
        0,0,18,274,1,0,0,0,20,295,1,0,0,0,22,322,1,0,0,0,24,332,1,0,0,0,
        26,363,1,0,0,0,28,375,1,0,0,0,30,422,1,0,0,0,32,442,1,0,0,0,34,497,
        1,0,0,0,36,521,1,0,0,0,38,48,3,2,1,0,39,48,3,4,2,0,40,48,3,8,4,0,
        41,48,3,12,6,0,42,48,3,16,8,0,43,48,3,20,10,0,44,48,3,24,12,0,45,
        48,3,28,14,0,46,48,3,32,16,0,47,38,1,0,0,0,47,39,1,0,0,0,47,40,1,
        0,0,0,47,41,1,0,0,0,47,42,1,0,0,0,47,43,1,0,0,0,47,44,1,0,0,0,47,
        45,1,0,0,0,47,46,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,
        0,50,52,1,0,0,0,51,49,1,0,0,0,52,53,5,0,0,1,53,1,1,0,0,0,54,55,5,
        1,0,0,55,57,5,14,0,0,56,58,5,15,0,0,57,56,1,0,0,0,58,59,1,0,0,0,
        59,57,1,0,0,0,59,60,1,0,0,0,60,61,1,0,0,0,61,62,5,17,0,0,62,3,1,
        0,0,0,63,64,5,2,0,0,64,65,5,20,0,0,65,66,5,21,0,0,66,67,5,23,0,0,
        67,68,5,24,0,0,68,69,5,25,0,0,69,70,5,27,0,0,70,71,5,28,0,0,71,72,
        5,29,0,0,72,73,5,46,0,0,73,74,5,47,0,0,74,75,5,43,0,0,75,76,5,45,
        0,0,76,77,5,44,0,0,77,78,5,53,0,0,78,79,5,3,0,0,79,80,5,56,0,0,80,
        81,5,56,0,0,81,82,5,56,0,0,82,83,5,56,0,0,83,84,5,56,0,0,84,85,5,
        56,0,0,85,86,5,56,0,0,86,87,5,56,0,0,87,88,5,56,0,0,88,89,5,56,0,
        0,89,90,5,56,0,0,90,91,5,56,0,0,91,92,5,56,0,0,92,94,5,58,0,0,93,
        95,3,6,3,0,94,93,1,0,0,0,95,96,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,
        0,97,5,1,0,0,0,98,99,5,4,0,0,99,100,5,4,0,0,100,101,5,4,0,0,101,
        102,5,9,0,0,102,103,5,9,0,0,103,104,5,4,0,0,104,105,5,9,0,0,105,
        106,5,9,0,0,106,107,3,36,18,0,107,108,3,36,18,0,108,109,3,36,18,
        0,109,110,3,36,18,0,110,111,3,36,18,0,111,7,1,0,0,0,112,113,5,2,
        0,0,113,114,5,20,0,0,114,115,5,21,0,0,115,116,5,22,0,0,116,117,5,
        23,0,0,117,118,5,24,0,0,118,119,5,25,0,0,119,120,5,26,0,0,120,121,
        5,27,0,0,121,122,5,28,0,0,122,123,5,29,0,0,123,124,5,46,0,0,124,
        125,5,47,0,0,125,126,5,43,0,0,126,127,5,45,0,0,127,128,5,44,0,0,
        128,129,5,53,0,0,129,130,5,3,0,0,130,131,5,56,0,0,131,132,5,56,0,
        0,132,133,5,56,0,0,133,134,5,56,0,0,134,135,5,56,0,0,135,136,5,56,
        0,0,136,137,5,56,0,0,137,138,5,56,0,0,138,139,5,56,0,0,139,140,5,
        56,0,0,140,141,5,56,0,0,141,142,5,56,0,0,142,143,5,56,0,0,143,144,
        5,56,0,0,144,145,5,56,0,0,145,147,5,58,0,0,146,148,3,10,5,0,147,
        146,1,0,0,0,148,149,1,0,0,0,149,147,1,0,0,0,149,150,1,0,0,0,150,
        9,1,0,0,0,151,152,5,4,0,0,152,153,5,4,0,0,153,154,5,9,0,0,154,155,
        5,4,0,0,155,156,5,9,0,0,156,157,5,9,0,0,157,158,5,9,0,0,158,159,
        5,4,0,0,159,160,5,9,0,0,160,161,5,9,0,0,161,162,3,36,18,0,162,163,
        3,36,18,0,163,164,3,36,18,0,164,165,3,36,18,0,165,166,3,36,18,0,
        166,11,1,0,0,0,167,168,5,2,0,0,168,169,5,20,0,0,169,170,5,23,0,0,
        170,171,5,24,0,0,171,172,5,25,0,0,172,173,5,27,0,0,173,174,5,28,
        0,0,174,175,5,29,0,0,175,176,5,31,0,0,176,177,5,32,0,0,177,178,5,
        33,0,0,178,179,5,35,0,0,179,180,5,36,0,0,180,181,5,37,0,0,181,182,
        5,48,0,0,182,183,5,49,0,0,183,184,5,43,0,0,184,185,5,53,0,0,185,
        186,5,3,0,0,186,187,5,56,0,0,187,188,5,56,0,0,188,189,5,56,0,0,189,
        190,5,56,0,0,190,191,5,56,0,0,191,192,5,56,0,0,192,193,5,56,0,0,
        193,194,5,56,0,0,194,195,5,56,0,0,195,196,5,56,0,0,196,197,5,56,
        0,0,197,198,5,56,0,0,198,199,5,56,0,0,199,200,5,56,0,0,200,201,5,
        56,0,0,201,202,5,56,0,0,202,204,5,58,0,0,203,205,3,14,7,0,204,203,
        1,0,0,0,205,206,1,0,0,0,206,204,1,0,0,0,206,207,1,0,0,0,207,13,1,
        0,0,0,208,209,5,4,0,0,209,210,5,4,0,0,210,211,5,9,0,0,211,212,5,
        9,0,0,212,213,5,4,0,0,213,214,5,9,0,0,214,215,5,9,0,0,215,216,5,
        4,0,0,216,217,5,9,0,0,217,218,5,9,0,0,218,219,5,4,0,0,219,220,5,
        9,0,0,220,221,5,9,0,0,221,222,3,36,18,0,222,223,3,36,18,0,223,224,
        3,36,18,0,224,15,1,0,0,0,225,226,5,2,0,0,226,227,5,20,0,0,227,228,
        5,22,0,0,228,229,5,23,0,0,229,230,5,24,0,0,230,231,5,25,0,0,231,
        232,5,26,0,0,232,233,5,27,0,0,233,234,5,28,0,0,234,235,5,29,0,0,
        235,236,5,30,0,0,236,237,5,31,0,0,237,238,5,32,0,0,238,239,5,33,
        0,0,239,240,5,34,0,0,240,241,5,35,0,0,241,242,5,36,0,0,242,243,5,
        37,0,0,243,244,5,48,0,0,244,245,5,49,0,0,245,246,5,43,0,0,246,247,
        5,53,0,0,247,248,5,3,0,0,248,249,5,56,0,0,249,250,5,56,0,0,250,251,
        5,56,0,0,251,252,5,56,0,0,252,253,5,56,0,0,253,254,5,56,0,0,254,
        255,5,56,0,0,255,256,5,56,0,0,256,257,5,56,0,0,257,258,5,56,0,0,
        258,259,5,56,0,0,259,260,5,56,0,0,260,261,5,56,0,0,261,262,5,56,
        0,0,262,263,5,56,0,0,263,264,5,56,0,0,264,265,5,56,0,0,265,266,5,
        56,0,0,266,267,5,56,0,0,267,268,5,56,0,0,268,270,5,58,0,0,269,271,
        3,18,9,0,270,269,1,0,0,0,271,272,1,0,0,0,272,270,1,0,0,0,272,273,
        1,0,0,0,273,17,1,0,0,0,274,275,5,4,0,0,275,276,5,9,0,0,276,277,5,
        4,0,0,277,278,5,9,0,0,278,279,5,9,0,0,279,280,5,9,0,0,280,281,5,
        4,0,0,281,282,5,9,0,0,282,283,5,9,0,0,283,284,5,9,0,0,284,285,5,
        4,0,0,285,286,5,9,0,0,286,287,5,9,0,0,287,288,5,9,0,0,288,289,5,
        4,0,0,289,290,5,9,0,0,290,291,5,9,0,0,291,292,3,36,18,0,292,293,
        3,36,18,0,293,294,3,36,18,0,294,19,1,0,0,0,295,296,5,2,0,0,296,297,
        5,23,0,0,297,298,5,24,0,0,298,299,5,25,0,0,299,300,5,27,0,0,300,
        301,5,28,0,0,301,302,5,29,0,0,302,303,5,41,0,0,303,304,5,42,0,0,
        304,305,5,45,0,0,305,306,5,53,0,0,306,307,5,3,0,0,307,308,5,56,0,
        0,308,309,5,56,0,0,309,310,5,56,0,0,310,311,5,56,0,0,311,312,5,56,
        0,0,312,313,5,56,0,0,313,314,5,56,0,0,314,315,5,56,0,0,315,316,5,
        56,0,0,316,318,5,58,0,0,317,319,3,22,11,0,318,317,1,0,0,0,319,320,
        1,0,0,0,320,318,1,0,0,0,320,321,1,0,0,0,321,21,1,0,0,0,322,323,5,
        4,0,0,323,324,5,9,0,0,324,325,5,9,0,0,325,326,5,4,0,0,326,327,5,
        9,0,0,327,328,5,9,0,0,328,329,3,36,18,0,329,330,3,36,18,0,330,331,
        3,36,18,0,331,23,1,0,0,0,332,333,5,2,0,0,333,334,5,22,0,0,334,335,
        5,23,0,0,335,336,5,24,0,0,336,337,5,25,0,0,337,338,5,26,0,0,338,
        339,5,27,0,0,339,340,5,28,0,0,340,341,5,29,0,0,341,342,5,41,0,0,
        342,343,5,42,0,0,343,344,5,45,0,0,344,345,5,53,0,0,345,346,5,3,0,
        0,346,347,5,56,0,0,347,348,5,56,0,0,348,349,5,56,0,0,349,350,5,56,
        0,0,350,351,5,56,0,0,351,352,5,56,0,0,352,353,5,56,0,0,353,354,5,
        56,0,0,354,355,5,56,0,0,355,356,5,56,0,0,356,357,5,56,0,0,357,359,
        5,58,0,0,358,360,3,26,13,0,359,358,1,0,0,0,360,361,1,0,0,0,361,359,
        1,0,0,0,361,362,1,0,0,0,362,25,1,0,0,0,363,364,5,9,0,0,364,365,5,
        4,0,0,365,366,5,9,0,0,366,367,5,9,0,0,367,368,5,9,0,0,368,369,5,
        4,0,0,369,370,5,9,0,0,370,371,5,9,0,0,371,372,3,36,18,0,372,373,
        3,36,18,0,373,374,3,36,18,0,374,27,1,0,0,0,375,376,5,2,0,0,376,377,
        5,20,0,0,377,378,5,23,0,0,378,379,5,24,0,0,379,380,5,25,0,0,380,
        381,5,27,0,0,381,382,5,28,0,0,382,383,5,29,0,0,383,384,5,31,0,0,
        384,385,5,32,0,0,385,386,5,33,0,0,386,387,5,35,0,0,387,388,5,36,
        0,0,388,389,5,37,0,0,389,390,5,38,0,0,390,391,5,39,0,0,391,392,5,
        40,0,0,392,393,5,50,0,0,393,394,5,51,0,0,394,395,5,43,0,0,395,396,
        5,53,0,0,396,397,5,3,0,0,397,398,5,56,0,0,398,399,5,56,0,0,399,400,
        5,56,0,0,400,401,5,56,0,0,401,402,5,56,0,0,402,403,5,56,0,0,403,
        404,5,56,0,0,404,405,5,56,0,0,405,406,5,56,0,0,406,407,5,56,0,0,
        407,408,5,56,0,0,408,409,5,56,0,0,409,410,5,56,0,0,410,411,5,56,
        0,0,411,412,5,56,0,0,412,413,5,56,0,0,413,414,5,56,0,0,414,415,5,
        56,0,0,415,416,5,56,0,0,416,418,5,58,0,0,417,419,3,30,15,0,418,417,
        1,0,0,0,419,420,1,0,0,0,420,418,1,0,0,0,420,421,1,0,0,0,421,29,1,
        0,0,0,422,423,5,4,0,0,423,424,5,4,0,0,424,425,5,9,0,0,425,426,5,
        9,0,0,426,427,5,4,0,0,427,428,5,9,0,0,428,429,5,9,0,0,429,430,5,
        4,0,0,430,431,5,9,0,0,431,432,5,9,0,0,432,433,5,4,0,0,433,434,5,
        9,0,0,434,435,5,9,0,0,435,436,3,36,18,0,436,437,3,36,18,0,437,438,
        3,36,18,0,438,439,3,36,18,0,439,440,3,36,18,0,440,441,3,36,18,0,
        441,31,1,0,0,0,442,443,5,2,0,0,443,444,5,20,0,0,444,445,5,22,0,0,
        445,446,5,23,0,0,446,447,5,24,0,0,447,448,5,25,0,0,448,449,5,26,
        0,0,449,450,5,27,0,0,450,451,5,28,0,0,451,452,5,29,0,0,452,453,5,
        30,0,0,453,454,5,31,0,0,454,455,5,32,0,0,455,456,5,33,0,0,456,457,
        5,34,0,0,457,458,5,35,0,0,458,459,5,36,0,0,459,460,5,37,0,0,460,
        461,5,38,0,0,461,462,5,39,0,0,462,463,5,40,0,0,463,464,5,50,0,0,
        464,465,5,51,0,0,465,466,5,43,0,0,466,467,5,53,0,0,467,468,5,3,0,
        0,468,469,5,56,0,0,469,470,5,56,0,0,470,471,5,56,0,0,471,472,5,56,
        0,0,472,473,5,56,0,0,473,474,5,56,0,0,474,475,5,56,0,0,475,476,5,
        56,0,0,476,477,5,56,0,0,477,478,5,56,0,0,478,479,5,56,0,0,479,480,
        5,56,0,0,480,481,5,56,0,0,481,482,5,56,0,0,482,483,5,56,0,0,483,
        484,5,56,0,0,484,485,5,56,0,0,485,486,5,56,0,0,486,487,5,56,0,0,
        487,488,5,56,0,0,488,489,5,56,0,0,489,490,5,56,0,0,490,491,5,56,
        0,0,491,493,5,58,0,0,492,494,3,34,17,0,493,492,1,0,0,0,494,495,1,
        0,0,0,495,493,1,0,0,0,495,496,1,0,0,0,496,33,1,0,0,0,497,498,5,4,
        0,0,498,499,5,9,0,0,499,500,5,4,0,0,500,501,5,9,0,0,501,502,5,9,
        0,0,502,503,5,9,0,0,503,504,5,4,0,0,504,505,5,9,0,0,505,506,5,9,
        0,0,506,507,5,9,0,0,507,508,5,4,0,0,508,509,5,9,0,0,509,510,5,9,
        0,0,510,511,5,9,0,0,511,512,5,4,0,0,512,513,5,9,0,0,513,514,5,9,
        0,0,514,515,3,36,18,0,515,516,3,36,18,0,516,517,3,36,18,0,517,518,
        3,36,18,0,518,519,3,36,18,0,519,520,3,36,18,0,520,35,1,0,0,0,521,
        522,7,0,0,0,522,37,1,0,0,0,11,47,49,59,96,149,206,272,320,361,420,
        495
    ]

class PalesMRParser ( Parser ):

    grammarFileName = "PalesMRParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'DATA'", "'VARS'", "'FORMAT'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'SEQUENCE'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'INDEX'", "'GROUP'", 
                     "'SEGNAME_I'", "'RESID_I'", "'RESNAME_I'", "'ATOMNAME_I'", 
                     "'SEGNAME_J'", "'RESID_J'", "'RESNAME_J'", "'ATOMNAME_J'", 
                     "'SEGNAME_K'", "'RESID_K'", "'RESNAME_K'", "'ATOMNAME_K'", 
                     "'SEGNAME_L'", "'RESID_L'", "'RESNAME_L'", "'ATOMNAME_L'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'D_LO'", "'D_HI'", "'ANGLE_LO'", "'ANGLE_HI'", "'PHASE'", 
                     "'OBSJ'" ]

    symbolicNames = [ "<INVALID>", "Data", "Vars", "Format", "Integer", 
                      "Float", "SHARP_COMMENT", "EXCLM_COMMENT", "SMCLN_COMMENT", 
                      "Simple_name", "SPACE", "COMMENT", "SECTION_COMMENT", 
                      "LINE_COMMENT", "Sequence", "One_letter_code", "SPACE_D", 
                      "RETURN_D", "SECTION_COMMENT_D", "LINE_COMMENT_D", 
                      "Index", "Group", "Segname_I", "Resid_I", "Resname_I", 
                      "Atomname_I", "Segname_J", "Resid_J", "Resname_J", 
                      "Atomname_J", "Segname_K", "Resid_K", "Resname_K", 
                      "Atomname_K", "Segname_L", "Resid_L", "Resname_L", 
                      "Atomname_L", "A", "B", "C", "D", "DD", "FC", "S", 
                      "W", "D_Lo", "D_Hi", "Angle_Lo", "Angle_Hi", "Phase", 
                      "ObsJ", "SPACE_V", "RETURN_V", "SECTION_COMMENT_V", 
                      "LINE_COMMENT_V", "Format_code", "SPACE_F", "RETURN_F", 
                      "SECTION_COMMENT_F", "LINE_COMMENT_F" ]

    RULE_pales_mr = 0
    RULE_sequence = 1
    RULE_distance_restraints = 2
    RULE_distance_restraint = 3
    RULE_distance_restraints_w_segid = 4
    RULE_distance_restraint_w_segid = 5
    RULE_torsion_angle_restraints = 6
    RULE_torsion_angle_restraint = 7
    RULE_torsion_angle_restraints_w_segid = 8
    RULE_torsion_angle_restraint_w_segid = 9
    RULE_rdc_restraints = 10
    RULE_rdc_restraint = 11
    RULE_rdc_restraints_w_segid = 12
    RULE_rdc_restraint_w_segid = 13
    RULE_coupling_restraints = 14
    RULE_coupling_restraint = 15
    RULE_coupling_restraints_w_segid = 16
    RULE_coupling_restraint_w_segid = 17
    RULE_number = 18

    ruleNames =  [ "pales_mr", "sequence", "distance_restraints", "distance_restraint", 
                   "distance_restraints_w_segid", "distance_restraint_w_segid", 
                   "torsion_angle_restraints", "torsion_angle_restraint", 
                   "torsion_angle_restraints_w_segid", "torsion_angle_restraint_w_segid", 
                   "rdc_restraints", "rdc_restraint", "rdc_restraints_w_segid", 
                   "rdc_restraint_w_segid", "coupling_restraints", "coupling_restraint", 
                   "coupling_restraints_w_segid", "coupling_restraint_w_segid", 
                   "number" ]

    EOF = Token.EOF
    Data=1
    Vars=2
    Format=3
    Integer=4
    Float=5
    SHARP_COMMENT=6
    EXCLM_COMMENT=7
    SMCLN_COMMENT=8
    Simple_name=9
    SPACE=10
    COMMENT=11
    SECTION_COMMENT=12
    LINE_COMMENT=13
    Sequence=14
    One_letter_code=15
    SPACE_D=16
    RETURN_D=17
    SECTION_COMMENT_D=18
    LINE_COMMENT_D=19
    Index=20
    Group=21
    Segname_I=22
    Resid_I=23
    Resname_I=24
    Atomname_I=25
    Segname_J=26
    Resid_J=27
    Resname_J=28
    Atomname_J=29
    Segname_K=30
    Resid_K=31
    Resname_K=32
    Atomname_K=33
    Segname_L=34
    Resid_L=35
    Resname_L=36
    Atomname_L=37
    A=38
    B=39
    C=40
    D=41
    DD=42
    FC=43
    S=44
    W=45
    D_Lo=46
    D_Hi=47
    Angle_Lo=48
    Angle_Hi=49
    Phase=50
    ObsJ=51
    SPACE_V=52
    RETURN_V=53
    SECTION_COMMENT_V=54
    LINE_COMMENT_V=55
    Format_code=56
    SPACE_F=57
    RETURN_F=58
    SECTION_COMMENT_F=59
    LINE_COMMENT_F=60

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Pales_mrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PalesMRParser.EOF, 0)

        def sequence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PalesMRParser.SequenceContext)
            else:
                return self.getTypedRuleContext(PalesMRParser.SequenceContext,i)


        def distance_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PalesMRParser.Distance_restraintsContext)
            else:
                return self.getTypedRuleContext(PalesMRParser.Distance_restraintsContext,i)


        def distance_restraints_w_segid(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PalesMRParser.Distance_restraints_w_segidContext)
            else:
                return self.getTypedRuleContext(PalesMRParser.Distance_restraints_w_segidContext,i)


        def torsion_angle_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PalesMRParser.Torsion_angle_restraintsContext)
            else:
                return self.getTypedRuleContext(PalesMRParser.Torsion_angle_restraintsContext,i)


        def torsion_angle_restraints_w_segid(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PalesMRParser.Torsion_angle_restraints_w_segidContext)
            else:
                return self.getTypedRuleContext(PalesMRParser.Torsion_angle_restraints_w_segidContext,i)


        def rdc_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PalesMRParser.Rdc_restraintsContext)
            else:
                return self.getTypedRuleContext(PalesMRParser.Rdc_restraintsContext,i)


        def rdc_restraints_w_segid(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PalesMRParser.Rdc_restraints_w_segidContext)
            else:
                return self.getTypedRuleContext(PalesMRParser.Rdc_restraints_w_segidContext,i)


        def coupling_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PalesMRParser.Coupling_restraintsContext)
            else:
                return self.getTypedRuleContext(PalesMRParser.Coupling_restraintsContext,i)


        def coupling_restraints_w_segid(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PalesMRParser.Coupling_restraints_w_segidContext)
            else:
                return self.getTypedRuleContext(PalesMRParser.Coupling_restraints_w_segidContext,i)


        def getRuleIndex(self):
            return PalesMRParser.RULE_pales_mr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPales_mr" ):
                listener.enterPales_mr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPales_mr" ):
                listener.exitPales_mr(self)




    def pales_mr(self):

        localctx = PalesMRParser.Pales_mrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_pales_mr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PalesMRParser.Data or _la==PalesMRParser.Vars:
                self.state = 47
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 38
                    self.sequence()
                    pass

                elif la_ == 2:
                    self.state = 39
                    self.distance_restraints()
                    pass

                elif la_ == 3:
                    self.state = 40
                    self.distance_restraints_w_segid()
                    pass

                elif la_ == 4:
                    self.state = 41
                    self.torsion_angle_restraints()
                    pass

                elif la_ == 5:
                    self.state = 42
                    self.torsion_angle_restraints_w_segid()
                    pass

                elif la_ == 6:
                    self.state = 43
                    self.rdc_restraints()
                    pass

                elif la_ == 7:
                    self.state = 44
                    self.rdc_restraints_w_segid()
                    pass

                elif la_ == 8:
                    self.state = 45
                    self.coupling_restraints()
                    pass

                elif la_ == 9:
                    self.state = 46
                    self.coupling_restraints_w_segid()
                    pass


                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(PalesMRParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SequenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Data(self):
            return self.getToken(PalesMRParser.Data, 0)

        def Sequence(self):
            return self.getToken(PalesMRParser.Sequence, 0)

        def RETURN_D(self):
            return self.getToken(PalesMRParser.RETURN_D, 0)

        def One_letter_code(self, i:int=None):
            if i is None:
                return self.getTokens(PalesMRParser.One_letter_code)
            else:
                return self.getToken(PalesMRParser.One_letter_code, i)

        def getRuleIndex(self):
            return PalesMRParser.RULE_sequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequence" ):
                listener.enterSequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequence" ):
                listener.exitSequence(self)




    def sequence(self):

        localctx = PalesMRParser.SequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sequence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(PalesMRParser.Data)
            self.state = 55
            self.match(PalesMRParser.Sequence)
            self.state = 57 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 56
                self.match(PalesMRParser.One_letter_code)
                self.state = 59 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PalesMRParser.One_letter_code):
                    break

            self.state = 61
            self.match(PalesMRParser.RETURN_D)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Distance_restraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Vars(self):
            return self.getToken(PalesMRParser.Vars, 0)

        def Index(self):
            return self.getToken(PalesMRParser.Index, 0)

        def Group(self):
            return self.getToken(PalesMRParser.Group, 0)

        def Resid_I(self):
            return self.getToken(PalesMRParser.Resid_I, 0)

        def Resname_I(self):
            return self.getToken(PalesMRParser.Resname_I, 0)

        def Atomname_I(self):
            return self.getToken(PalesMRParser.Atomname_I, 0)

        def Resid_J(self):
            return self.getToken(PalesMRParser.Resid_J, 0)

        def Resname_J(self):
            return self.getToken(PalesMRParser.Resname_J, 0)

        def Atomname_J(self):
            return self.getToken(PalesMRParser.Atomname_J, 0)

        def D_Lo(self):
            return self.getToken(PalesMRParser.D_Lo, 0)

        def D_Hi(self):
            return self.getToken(PalesMRParser.D_Hi, 0)

        def FC(self):
            return self.getToken(PalesMRParser.FC, 0)

        def W(self):
            return self.getToken(PalesMRParser.W, 0)

        def S(self):
            return self.getToken(PalesMRParser.S, 0)

        def RETURN_V(self):
            return self.getToken(PalesMRParser.RETURN_V, 0)

        def Format(self):
            return self.getToken(PalesMRParser.Format, 0)

        def Format_code(self, i:int=None):
            if i is None:
                return self.getTokens(PalesMRParser.Format_code)
            else:
                return self.getToken(PalesMRParser.Format_code, i)

        def RETURN_F(self):
            return self.getToken(PalesMRParser.RETURN_F, 0)

        def distance_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PalesMRParser.Distance_restraintContext)
            else:
                return self.getTypedRuleContext(PalesMRParser.Distance_restraintContext,i)


        def getRuleIndex(self):
            return PalesMRParser.RULE_distance_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistance_restraints" ):
                listener.enterDistance_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistance_restraints" ):
                listener.exitDistance_restraints(self)




    def distance_restraints(self):

        localctx = PalesMRParser.Distance_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_distance_restraints)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(PalesMRParser.Vars)
            self.state = 64
            self.match(PalesMRParser.Index)
            self.state = 65
            self.match(PalesMRParser.Group)
            self.state = 66
            self.match(PalesMRParser.Resid_I)
            self.state = 67
            self.match(PalesMRParser.Resname_I)
            self.state = 68
            self.match(PalesMRParser.Atomname_I)
            self.state = 69
            self.match(PalesMRParser.Resid_J)
            self.state = 70
            self.match(PalesMRParser.Resname_J)
            self.state = 71
            self.match(PalesMRParser.Atomname_J)
            self.state = 72
            self.match(PalesMRParser.D_Lo)
            self.state = 73
            self.match(PalesMRParser.D_Hi)
            self.state = 74
            self.match(PalesMRParser.FC)
            self.state = 75
            self.match(PalesMRParser.W)
            self.state = 76
            self.match(PalesMRParser.S)
            self.state = 77
            self.match(PalesMRParser.RETURN_V)
            self.state = 78
            self.match(PalesMRParser.Format)
            self.state = 79
            self.match(PalesMRParser.Format_code)
            self.state = 80
            self.match(PalesMRParser.Format_code)
            self.state = 81
            self.match(PalesMRParser.Format_code)
            self.state = 82
            self.match(PalesMRParser.Format_code)
            self.state = 83
            self.match(PalesMRParser.Format_code)
            self.state = 84
            self.match(PalesMRParser.Format_code)
            self.state = 85
            self.match(PalesMRParser.Format_code)
            self.state = 86
            self.match(PalesMRParser.Format_code)
            self.state = 87
            self.match(PalesMRParser.Format_code)
            self.state = 88
            self.match(PalesMRParser.Format_code)
            self.state = 89
            self.match(PalesMRParser.Format_code)
            self.state = 90
            self.match(PalesMRParser.Format_code)
            self.state = 91
            self.match(PalesMRParser.Format_code)
            self.state = 92
            self.match(PalesMRParser.RETURN_F)
            self.state = 94 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 93
                self.distance_restraint()
                self.state = 96 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PalesMRParser.Integer):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Distance_restraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(PalesMRParser.Integer)
            else:
                return self.getToken(PalesMRParser.Integer, i)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(PalesMRParser.Simple_name)
            else:
                return self.getToken(PalesMRParser.Simple_name, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PalesMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(PalesMRParser.NumberContext,i)


        def getRuleIndex(self):
            return PalesMRParser.RULE_distance_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistance_restraint" ):
                listener.enterDistance_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistance_restraint" ):
                listener.exitDistance_restraint(self)




    def distance_restraint(self):

        localctx = PalesMRParser.Distance_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_distance_restraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(PalesMRParser.Integer)
            self.state = 99
            self.match(PalesMRParser.Integer)
            self.state = 100
            self.match(PalesMRParser.Integer)
            self.state = 101
            self.match(PalesMRParser.Simple_name)
            self.state = 102
            self.match(PalesMRParser.Simple_name)
            self.state = 103
            self.match(PalesMRParser.Integer)
            self.state = 104
            self.match(PalesMRParser.Simple_name)
            self.state = 105
            self.match(PalesMRParser.Simple_name)
            self.state = 106
            self.number()
            self.state = 107
            self.number()
            self.state = 108
            self.number()
            self.state = 109
            self.number()
            self.state = 110
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Distance_restraints_w_segidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Vars(self):
            return self.getToken(PalesMRParser.Vars, 0)

        def Index(self):
            return self.getToken(PalesMRParser.Index, 0)

        def Group(self):
            return self.getToken(PalesMRParser.Group, 0)

        def Segname_I(self):
            return self.getToken(PalesMRParser.Segname_I, 0)

        def Resid_I(self):
            return self.getToken(PalesMRParser.Resid_I, 0)

        def Resname_I(self):
            return self.getToken(PalesMRParser.Resname_I, 0)

        def Atomname_I(self):
            return self.getToken(PalesMRParser.Atomname_I, 0)

        def Segname_J(self):
            return self.getToken(PalesMRParser.Segname_J, 0)

        def Resid_J(self):
            return self.getToken(PalesMRParser.Resid_J, 0)

        def Resname_J(self):
            return self.getToken(PalesMRParser.Resname_J, 0)

        def Atomname_J(self):
            return self.getToken(PalesMRParser.Atomname_J, 0)

        def D_Lo(self):
            return self.getToken(PalesMRParser.D_Lo, 0)

        def D_Hi(self):
            return self.getToken(PalesMRParser.D_Hi, 0)

        def FC(self):
            return self.getToken(PalesMRParser.FC, 0)

        def W(self):
            return self.getToken(PalesMRParser.W, 0)

        def S(self):
            return self.getToken(PalesMRParser.S, 0)

        def RETURN_V(self):
            return self.getToken(PalesMRParser.RETURN_V, 0)

        def Format(self):
            return self.getToken(PalesMRParser.Format, 0)

        def Format_code(self, i:int=None):
            if i is None:
                return self.getTokens(PalesMRParser.Format_code)
            else:
                return self.getToken(PalesMRParser.Format_code, i)

        def RETURN_F(self):
            return self.getToken(PalesMRParser.RETURN_F, 0)

        def distance_restraint_w_segid(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PalesMRParser.Distance_restraint_w_segidContext)
            else:
                return self.getTypedRuleContext(PalesMRParser.Distance_restraint_w_segidContext,i)


        def getRuleIndex(self):
            return PalesMRParser.RULE_distance_restraints_w_segid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistance_restraints_w_segid" ):
                listener.enterDistance_restraints_w_segid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistance_restraints_w_segid" ):
                listener.exitDistance_restraints_w_segid(self)




    def distance_restraints_w_segid(self):

        localctx = PalesMRParser.Distance_restraints_w_segidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_distance_restraints_w_segid)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(PalesMRParser.Vars)
            self.state = 113
            self.match(PalesMRParser.Index)
            self.state = 114
            self.match(PalesMRParser.Group)
            self.state = 115
            self.match(PalesMRParser.Segname_I)
            self.state = 116
            self.match(PalesMRParser.Resid_I)
            self.state = 117
            self.match(PalesMRParser.Resname_I)
            self.state = 118
            self.match(PalesMRParser.Atomname_I)
            self.state = 119
            self.match(PalesMRParser.Segname_J)
            self.state = 120
            self.match(PalesMRParser.Resid_J)
            self.state = 121
            self.match(PalesMRParser.Resname_J)
            self.state = 122
            self.match(PalesMRParser.Atomname_J)
            self.state = 123
            self.match(PalesMRParser.D_Lo)
            self.state = 124
            self.match(PalesMRParser.D_Hi)
            self.state = 125
            self.match(PalesMRParser.FC)
            self.state = 126
            self.match(PalesMRParser.W)
            self.state = 127
            self.match(PalesMRParser.S)
            self.state = 128
            self.match(PalesMRParser.RETURN_V)
            self.state = 129
            self.match(PalesMRParser.Format)
            self.state = 130
            self.match(PalesMRParser.Format_code)
            self.state = 131
            self.match(PalesMRParser.Format_code)
            self.state = 132
            self.match(PalesMRParser.Format_code)
            self.state = 133
            self.match(PalesMRParser.Format_code)
            self.state = 134
            self.match(PalesMRParser.Format_code)
            self.state = 135
            self.match(PalesMRParser.Format_code)
            self.state = 136
            self.match(PalesMRParser.Format_code)
            self.state = 137
            self.match(PalesMRParser.Format_code)
            self.state = 138
            self.match(PalesMRParser.Format_code)
            self.state = 139
            self.match(PalesMRParser.Format_code)
            self.state = 140
            self.match(PalesMRParser.Format_code)
            self.state = 141
            self.match(PalesMRParser.Format_code)
            self.state = 142
            self.match(PalesMRParser.Format_code)
            self.state = 143
            self.match(PalesMRParser.Format_code)
            self.state = 144
            self.match(PalesMRParser.Format_code)
            self.state = 145
            self.match(PalesMRParser.RETURN_F)
            self.state = 147 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 146
                self.distance_restraint_w_segid()
                self.state = 149 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PalesMRParser.Integer):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Distance_restraint_w_segidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(PalesMRParser.Integer)
            else:
                return self.getToken(PalesMRParser.Integer, i)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(PalesMRParser.Simple_name)
            else:
                return self.getToken(PalesMRParser.Simple_name, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PalesMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(PalesMRParser.NumberContext,i)


        def getRuleIndex(self):
            return PalesMRParser.RULE_distance_restraint_w_segid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistance_restraint_w_segid" ):
                listener.enterDistance_restraint_w_segid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistance_restraint_w_segid" ):
                listener.exitDistance_restraint_w_segid(self)




    def distance_restraint_w_segid(self):

        localctx = PalesMRParser.Distance_restraint_w_segidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_distance_restraint_w_segid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(PalesMRParser.Integer)
            self.state = 152
            self.match(PalesMRParser.Integer)
            self.state = 153
            self.match(PalesMRParser.Simple_name)
            self.state = 154
            self.match(PalesMRParser.Integer)
            self.state = 155
            self.match(PalesMRParser.Simple_name)
            self.state = 156
            self.match(PalesMRParser.Simple_name)
            self.state = 157
            self.match(PalesMRParser.Simple_name)
            self.state = 158
            self.match(PalesMRParser.Integer)
            self.state = 159
            self.match(PalesMRParser.Simple_name)
            self.state = 160
            self.match(PalesMRParser.Simple_name)
            self.state = 161
            self.number()
            self.state = 162
            self.number()
            self.state = 163
            self.number()
            self.state = 164
            self.number()
            self.state = 165
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Torsion_angle_restraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Vars(self):
            return self.getToken(PalesMRParser.Vars, 0)

        def Index(self):
            return self.getToken(PalesMRParser.Index, 0)

        def Resid_I(self):
            return self.getToken(PalesMRParser.Resid_I, 0)

        def Resname_I(self):
            return self.getToken(PalesMRParser.Resname_I, 0)

        def Atomname_I(self):
            return self.getToken(PalesMRParser.Atomname_I, 0)

        def Resid_J(self):
            return self.getToken(PalesMRParser.Resid_J, 0)

        def Resname_J(self):
            return self.getToken(PalesMRParser.Resname_J, 0)

        def Atomname_J(self):
            return self.getToken(PalesMRParser.Atomname_J, 0)

        def Resid_K(self):
            return self.getToken(PalesMRParser.Resid_K, 0)

        def Resname_K(self):
            return self.getToken(PalesMRParser.Resname_K, 0)

        def Atomname_K(self):
            return self.getToken(PalesMRParser.Atomname_K, 0)

        def Resid_L(self):
            return self.getToken(PalesMRParser.Resid_L, 0)

        def Resname_L(self):
            return self.getToken(PalesMRParser.Resname_L, 0)

        def Atomname_L(self):
            return self.getToken(PalesMRParser.Atomname_L, 0)

        def Angle_Lo(self):
            return self.getToken(PalesMRParser.Angle_Lo, 0)

        def Angle_Hi(self):
            return self.getToken(PalesMRParser.Angle_Hi, 0)

        def FC(self):
            return self.getToken(PalesMRParser.FC, 0)

        def RETURN_V(self):
            return self.getToken(PalesMRParser.RETURN_V, 0)

        def Format(self):
            return self.getToken(PalesMRParser.Format, 0)

        def Format_code(self, i:int=None):
            if i is None:
                return self.getTokens(PalesMRParser.Format_code)
            else:
                return self.getToken(PalesMRParser.Format_code, i)

        def RETURN_F(self):
            return self.getToken(PalesMRParser.RETURN_F, 0)

        def torsion_angle_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PalesMRParser.Torsion_angle_restraintContext)
            else:
                return self.getTypedRuleContext(PalesMRParser.Torsion_angle_restraintContext,i)


        def getRuleIndex(self):
            return PalesMRParser.RULE_torsion_angle_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTorsion_angle_restraints" ):
                listener.enterTorsion_angle_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTorsion_angle_restraints" ):
                listener.exitTorsion_angle_restraints(self)




    def torsion_angle_restraints(self):

        localctx = PalesMRParser.Torsion_angle_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_torsion_angle_restraints)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(PalesMRParser.Vars)
            self.state = 168
            self.match(PalesMRParser.Index)
            self.state = 169
            self.match(PalesMRParser.Resid_I)
            self.state = 170
            self.match(PalesMRParser.Resname_I)
            self.state = 171
            self.match(PalesMRParser.Atomname_I)
            self.state = 172
            self.match(PalesMRParser.Resid_J)
            self.state = 173
            self.match(PalesMRParser.Resname_J)
            self.state = 174
            self.match(PalesMRParser.Atomname_J)
            self.state = 175
            self.match(PalesMRParser.Resid_K)
            self.state = 176
            self.match(PalesMRParser.Resname_K)
            self.state = 177
            self.match(PalesMRParser.Atomname_K)
            self.state = 178
            self.match(PalesMRParser.Resid_L)
            self.state = 179
            self.match(PalesMRParser.Resname_L)
            self.state = 180
            self.match(PalesMRParser.Atomname_L)
            self.state = 181
            self.match(PalesMRParser.Angle_Lo)
            self.state = 182
            self.match(PalesMRParser.Angle_Hi)
            self.state = 183
            self.match(PalesMRParser.FC)
            self.state = 184
            self.match(PalesMRParser.RETURN_V)
            self.state = 185
            self.match(PalesMRParser.Format)
            self.state = 186
            self.match(PalesMRParser.Format_code)
            self.state = 187
            self.match(PalesMRParser.Format_code)
            self.state = 188
            self.match(PalesMRParser.Format_code)
            self.state = 189
            self.match(PalesMRParser.Format_code)
            self.state = 190
            self.match(PalesMRParser.Format_code)
            self.state = 191
            self.match(PalesMRParser.Format_code)
            self.state = 192
            self.match(PalesMRParser.Format_code)
            self.state = 193
            self.match(PalesMRParser.Format_code)
            self.state = 194
            self.match(PalesMRParser.Format_code)
            self.state = 195
            self.match(PalesMRParser.Format_code)
            self.state = 196
            self.match(PalesMRParser.Format_code)
            self.state = 197
            self.match(PalesMRParser.Format_code)
            self.state = 198
            self.match(PalesMRParser.Format_code)
            self.state = 199
            self.match(PalesMRParser.Format_code)
            self.state = 200
            self.match(PalesMRParser.Format_code)
            self.state = 201
            self.match(PalesMRParser.Format_code)
            self.state = 202
            self.match(PalesMRParser.RETURN_F)
            self.state = 204 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 203
                self.torsion_angle_restraint()
                self.state = 206 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PalesMRParser.Integer):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Torsion_angle_restraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(PalesMRParser.Integer)
            else:
                return self.getToken(PalesMRParser.Integer, i)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(PalesMRParser.Simple_name)
            else:
                return self.getToken(PalesMRParser.Simple_name, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PalesMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(PalesMRParser.NumberContext,i)


        def getRuleIndex(self):
            return PalesMRParser.RULE_torsion_angle_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTorsion_angle_restraint" ):
                listener.enterTorsion_angle_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTorsion_angle_restraint" ):
                listener.exitTorsion_angle_restraint(self)




    def torsion_angle_restraint(self):

        localctx = PalesMRParser.Torsion_angle_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_torsion_angle_restraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(PalesMRParser.Integer)
            self.state = 209
            self.match(PalesMRParser.Integer)
            self.state = 210
            self.match(PalesMRParser.Simple_name)
            self.state = 211
            self.match(PalesMRParser.Simple_name)
            self.state = 212
            self.match(PalesMRParser.Integer)
            self.state = 213
            self.match(PalesMRParser.Simple_name)
            self.state = 214
            self.match(PalesMRParser.Simple_name)
            self.state = 215
            self.match(PalesMRParser.Integer)
            self.state = 216
            self.match(PalesMRParser.Simple_name)
            self.state = 217
            self.match(PalesMRParser.Simple_name)
            self.state = 218
            self.match(PalesMRParser.Integer)
            self.state = 219
            self.match(PalesMRParser.Simple_name)
            self.state = 220
            self.match(PalesMRParser.Simple_name)
            self.state = 221
            self.number()
            self.state = 222
            self.number()
            self.state = 223
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Torsion_angle_restraints_w_segidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Vars(self):
            return self.getToken(PalesMRParser.Vars, 0)

        def Index(self):
            return self.getToken(PalesMRParser.Index, 0)

        def Segname_I(self):
            return self.getToken(PalesMRParser.Segname_I, 0)

        def Resid_I(self):
            return self.getToken(PalesMRParser.Resid_I, 0)

        def Resname_I(self):
            return self.getToken(PalesMRParser.Resname_I, 0)

        def Atomname_I(self):
            return self.getToken(PalesMRParser.Atomname_I, 0)

        def Segname_J(self):
            return self.getToken(PalesMRParser.Segname_J, 0)

        def Resid_J(self):
            return self.getToken(PalesMRParser.Resid_J, 0)

        def Resname_J(self):
            return self.getToken(PalesMRParser.Resname_J, 0)

        def Atomname_J(self):
            return self.getToken(PalesMRParser.Atomname_J, 0)

        def Segname_K(self):
            return self.getToken(PalesMRParser.Segname_K, 0)

        def Resid_K(self):
            return self.getToken(PalesMRParser.Resid_K, 0)

        def Resname_K(self):
            return self.getToken(PalesMRParser.Resname_K, 0)

        def Atomname_K(self):
            return self.getToken(PalesMRParser.Atomname_K, 0)

        def Segname_L(self):
            return self.getToken(PalesMRParser.Segname_L, 0)

        def Resid_L(self):
            return self.getToken(PalesMRParser.Resid_L, 0)

        def Resname_L(self):
            return self.getToken(PalesMRParser.Resname_L, 0)

        def Atomname_L(self):
            return self.getToken(PalesMRParser.Atomname_L, 0)

        def Angle_Lo(self):
            return self.getToken(PalesMRParser.Angle_Lo, 0)

        def Angle_Hi(self):
            return self.getToken(PalesMRParser.Angle_Hi, 0)

        def FC(self):
            return self.getToken(PalesMRParser.FC, 0)

        def RETURN_V(self):
            return self.getToken(PalesMRParser.RETURN_V, 0)

        def Format(self):
            return self.getToken(PalesMRParser.Format, 0)

        def Format_code(self, i:int=None):
            if i is None:
                return self.getTokens(PalesMRParser.Format_code)
            else:
                return self.getToken(PalesMRParser.Format_code, i)

        def RETURN_F(self):
            return self.getToken(PalesMRParser.RETURN_F, 0)

        def torsion_angle_restraint_w_segid(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PalesMRParser.Torsion_angle_restraint_w_segidContext)
            else:
                return self.getTypedRuleContext(PalesMRParser.Torsion_angle_restraint_w_segidContext,i)


        def getRuleIndex(self):
            return PalesMRParser.RULE_torsion_angle_restraints_w_segid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTorsion_angle_restraints_w_segid" ):
                listener.enterTorsion_angle_restraints_w_segid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTorsion_angle_restraints_w_segid" ):
                listener.exitTorsion_angle_restraints_w_segid(self)




    def torsion_angle_restraints_w_segid(self):

        localctx = PalesMRParser.Torsion_angle_restraints_w_segidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_torsion_angle_restraints_w_segid)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(PalesMRParser.Vars)
            self.state = 226
            self.match(PalesMRParser.Index)
            self.state = 227
            self.match(PalesMRParser.Segname_I)
            self.state = 228
            self.match(PalesMRParser.Resid_I)
            self.state = 229
            self.match(PalesMRParser.Resname_I)
            self.state = 230
            self.match(PalesMRParser.Atomname_I)
            self.state = 231
            self.match(PalesMRParser.Segname_J)
            self.state = 232
            self.match(PalesMRParser.Resid_J)
            self.state = 233
            self.match(PalesMRParser.Resname_J)
            self.state = 234
            self.match(PalesMRParser.Atomname_J)
            self.state = 235
            self.match(PalesMRParser.Segname_K)
            self.state = 236
            self.match(PalesMRParser.Resid_K)
            self.state = 237
            self.match(PalesMRParser.Resname_K)
            self.state = 238
            self.match(PalesMRParser.Atomname_K)
            self.state = 239
            self.match(PalesMRParser.Segname_L)
            self.state = 240
            self.match(PalesMRParser.Resid_L)
            self.state = 241
            self.match(PalesMRParser.Resname_L)
            self.state = 242
            self.match(PalesMRParser.Atomname_L)
            self.state = 243
            self.match(PalesMRParser.Angle_Lo)
            self.state = 244
            self.match(PalesMRParser.Angle_Hi)
            self.state = 245
            self.match(PalesMRParser.FC)
            self.state = 246
            self.match(PalesMRParser.RETURN_V)
            self.state = 247
            self.match(PalesMRParser.Format)
            self.state = 248
            self.match(PalesMRParser.Format_code)
            self.state = 249
            self.match(PalesMRParser.Format_code)
            self.state = 250
            self.match(PalesMRParser.Format_code)
            self.state = 251
            self.match(PalesMRParser.Format_code)
            self.state = 252
            self.match(PalesMRParser.Format_code)
            self.state = 253
            self.match(PalesMRParser.Format_code)
            self.state = 254
            self.match(PalesMRParser.Format_code)
            self.state = 255
            self.match(PalesMRParser.Format_code)
            self.state = 256
            self.match(PalesMRParser.Format_code)
            self.state = 257
            self.match(PalesMRParser.Format_code)
            self.state = 258
            self.match(PalesMRParser.Format_code)
            self.state = 259
            self.match(PalesMRParser.Format_code)
            self.state = 260
            self.match(PalesMRParser.Format_code)
            self.state = 261
            self.match(PalesMRParser.Format_code)
            self.state = 262
            self.match(PalesMRParser.Format_code)
            self.state = 263
            self.match(PalesMRParser.Format_code)
            self.state = 264
            self.match(PalesMRParser.Format_code)
            self.state = 265
            self.match(PalesMRParser.Format_code)
            self.state = 266
            self.match(PalesMRParser.Format_code)
            self.state = 267
            self.match(PalesMRParser.Format_code)
            self.state = 268
            self.match(PalesMRParser.RETURN_F)
            self.state = 270 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 269
                self.torsion_angle_restraint_w_segid()
                self.state = 272 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PalesMRParser.Integer):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Torsion_angle_restraint_w_segidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(PalesMRParser.Integer)
            else:
                return self.getToken(PalesMRParser.Integer, i)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(PalesMRParser.Simple_name)
            else:
                return self.getToken(PalesMRParser.Simple_name, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PalesMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(PalesMRParser.NumberContext,i)


        def getRuleIndex(self):
            return PalesMRParser.RULE_torsion_angle_restraint_w_segid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTorsion_angle_restraint_w_segid" ):
                listener.enterTorsion_angle_restraint_w_segid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTorsion_angle_restraint_w_segid" ):
                listener.exitTorsion_angle_restraint_w_segid(self)




    def torsion_angle_restraint_w_segid(self):

        localctx = PalesMRParser.Torsion_angle_restraint_w_segidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_torsion_angle_restraint_w_segid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(PalesMRParser.Integer)
            self.state = 275
            self.match(PalesMRParser.Simple_name)
            self.state = 276
            self.match(PalesMRParser.Integer)
            self.state = 277
            self.match(PalesMRParser.Simple_name)
            self.state = 278
            self.match(PalesMRParser.Simple_name)
            self.state = 279
            self.match(PalesMRParser.Simple_name)
            self.state = 280
            self.match(PalesMRParser.Integer)
            self.state = 281
            self.match(PalesMRParser.Simple_name)
            self.state = 282
            self.match(PalesMRParser.Simple_name)
            self.state = 283
            self.match(PalesMRParser.Simple_name)
            self.state = 284
            self.match(PalesMRParser.Integer)
            self.state = 285
            self.match(PalesMRParser.Simple_name)
            self.state = 286
            self.match(PalesMRParser.Simple_name)
            self.state = 287
            self.match(PalesMRParser.Simple_name)
            self.state = 288
            self.match(PalesMRParser.Integer)
            self.state = 289
            self.match(PalesMRParser.Simple_name)
            self.state = 290
            self.match(PalesMRParser.Simple_name)
            self.state = 291
            self.number()
            self.state = 292
            self.number()
            self.state = 293
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rdc_restraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Vars(self):
            return self.getToken(PalesMRParser.Vars, 0)

        def Resid_I(self):
            return self.getToken(PalesMRParser.Resid_I, 0)

        def Resname_I(self):
            return self.getToken(PalesMRParser.Resname_I, 0)

        def Atomname_I(self):
            return self.getToken(PalesMRParser.Atomname_I, 0)

        def Resid_J(self):
            return self.getToken(PalesMRParser.Resid_J, 0)

        def Resname_J(self):
            return self.getToken(PalesMRParser.Resname_J, 0)

        def Atomname_J(self):
            return self.getToken(PalesMRParser.Atomname_J, 0)

        def D(self):
            return self.getToken(PalesMRParser.D, 0)

        def DD(self):
            return self.getToken(PalesMRParser.DD, 0)

        def W(self):
            return self.getToken(PalesMRParser.W, 0)

        def RETURN_V(self):
            return self.getToken(PalesMRParser.RETURN_V, 0)

        def Format(self):
            return self.getToken(PalesMRParser.Format, 0)

        def Format_code(self, i:int=None):
            if i is None:
                return self.getTokens(PalesMRParser.Format_code)
            else:
                return self.getToken(PalesMRParser.Format_code, i)

        def RETURN_F(self):
            return self.getToken(PalesMRParser.RETURN_F, 0)

        def rdc_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PalesMRParser.Rdc_restraintContext)
            else:
                return self.getTypedRuleContext(PalesMRParser.Rdc_restraintContext,i)


        def getRuleIndex(self):
            return PalesMRParser.RULE_rdc_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRdc_restraints" ):
                listener.enterRdc_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRdc_restraints" ):
                listener.exitRdc_restraints(self)




    def rdc_restraints(self):

        localctx = PalesMRParser.Rdc_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_rdc_restraints)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(PalesMRParser.Vars)
            self.state = 296
            self.match(PalesMRParser.Resid_I)
            self.state = 297
            self.match(PalesMRParser.Resname_I)
            self.state = 298
            self.match(PalesMRParser.Atomname_I)
            self.state = 299
            self.match(PalesMRParser.Resid_J)
            self.state = 300
            self.match(PalesMRParser.Resname_J)
            self.state = 301
            self.match(PalesMRParser.Atomname_J)
            self.state = 302
            self.match(PalesMRParser.D)
            self.state = 303
            self.match(PalesMRParser.DD)
            self.state = 304
            self.match(PalesMRParser.W)
            self.state = 305
            self.match(PalesMRParser.RETURN_V)
            self.state = 306
            self.match(PalesMRParser.Format)
            self.state = 307
            self.match(PalesMRParser.Format_code)
            self.state = 308
            self.match(PalesMRParser.Format_code)
            self.state = 309
            self.match(PalesMRParser.Format_code)
            self.state = 310
            self.match(PalesMRParser.Format_code)
            self.state = 311
            self.match(PalesMRParser.Format_code)
            self.state = 312
            self.match(PalesMRParser.Format_code)
            self.state = 313
            self.match(PalesMRParser.Format_code)
            self.state = 314
            self.match(PalesMRParser.Format_code)
            self.state = 315
            self.match(PalesMRParser.Format_code)
            self.state = 316
            self.match(PalesMRParser.RETURN_F)
            self.state = 318 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 317
                self.rdc_restraint()
                self.state = 320 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PalesMRParser.Integer):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rdc_restraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(PalesMRParser.Integer)
            else:
                return self.getToken(PalesMRParser.Integer, i)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(PalesMRParser.Simple_name)
            else:
                return self.getToken(PalesMRParser.Simple_name, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PalesMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(PalesMRParser.NumberContext,i)


        def getRuleIndex(self):
            return PalesMRParser.RULE_rdc_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRdc_restraint" ):
                listener.enterRdc_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRdc_restraint" ):
                listener.exitRdc_restraint(self)




    def rdc_restraint(self):

        localctx = PalesMRParser.Rdc_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_rdc_restraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(PalesMRParser.Integer)
            self.state = 323
            self.match(PalesMRParser.Simple_name)
            self.state = 324
            self.match(PalesMRParser.Simple_name)
            self.state = 325
            self.match(PalesMRParser.Integer)
            self.state = 326
            self.match(PalesMRParser.Simple_name)
            self.state = 327
            self.match(PalesMRParser.Simple_name)
            self.state = 328
            self.number()
            self.state = 329
            self.number()
            self.state = 330
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rdc_restraints_w_segidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Vars(self):
            return self.getToken(PalesMRParser.Vars, 0)

        def Segname_I(self):
            return self.getToken(PalesMRParser.Segname_I, 0)

        def Resid_I(self):
            return self.getToken(PalesMRParser.Resid_I, 0)

        def Resname_I(self):
            return self.getToken(PalesMRParser.Resname_I, 0)

        def Atomname_I(self):
            return self.getToken(PalesMRParser.Atomname_I, 0)

        def Segname_J(self):
            return self.getToken(PalesMRParser.Segname_J, 0)

        def Resid_J(self):
            return self.getToken(PalesMRParser.Resid_J, 0)

        def Resname_J(self):
            return self.getToken(PalesMRParser.Resname_J, 0)

        def Atomname_J(self):
            return self.getToken(PalesMRParser.Atomname_J, 0)

        def D(self):
            return self.getToken(PalesMRParser.D, 0)

        def DD(self):
            return self.getToken(PalesMRParser.DD, 0)

        def W(self):
            return self.getToken(PalesMRParser.W, 0)

        def RETURN_V(self):
            return self.getToken(PalesMRParser.RETURN_V, 0)

        def Format(self):
            return self.getToken(PalesMRParser.Format, 0)

        def Format_code(self, i:int=None):
            if i is None:
                return self.getTokens(PalesMRParser.Format_code)
            else:
                return self.getToken(PalesMRParser.Format_code, i)

        def RETURN_F(self):
            return self.getToken(PalesMRParser.RETURN_F, 0)

        def rdc_restraint_w_segid(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PalesMRParser.Rdc_restraint_w_segidContext)
            else:
                return self.getTypedRuleContext(PalesMRParser.Rdc_restraint_w_segidContext,i)


        def getRuleIndex(self):
            return PalesMRParser.RULE_rdc_restraints_w_segid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRdc_restraints_w_segid" ):
                listener.enterRdc_restraints_w_segid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRdc_restraints_w_segid" ):
                listener.exitRdc_restraints_w_segid(self)




    def rdc_restraints_w_segid(self):

        localctx = PalesMRParser.Rdc_restraints_w_segidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_rdc_restraints_w_segid)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(PalesMRParser.Vars)
            self.state = 333
            self.match(PalesMRParser.Segname_I)
            self.state = 334
            self.match(PalesMRParser.Resid_I)
            self.state = 335
            self.match(PalesMRParser.Resname_I)
            self.state = 336
            self.match(PalesMRParser.Atomname_I)
            self.state = 337
            self.match(PalesMRParser.Segname_J)
            self.state = 338
            self.match(PalesMRParser.Resid_J)
            self.state = 339
            self.match(PalesMRParser.Resname_J)
            self.state = 340
            self.match(PalesMRParser.Atomname_J)
            self.state = 341
            self.match(PalesMRParser.D)
            self.state = 342
            self.match(PalesMRParser.DD)
            self.state = 343
            self.match(PalesMRParser.W)
            self.state = 344
            self.match(PalesMRParser.RETURN_V)
            self.state = 345
            self.match(PalesMRParser.Format)
            self.state = 346
            self.match(PalesMRParser.Format_code)
            self.state = 347
            self.match(PalesMRParser.Format_code)
            self.state = 348
            self.match(PalesMRParser.Format_code)
            self.state = 349
            self.match(PalesMRParser.Format_code)
            self.state = 350
            self.match(PalesMRParser.Format_code)
            self.state = 351
            self.match(PalesMRParser.Format_code)
            self.state = 352
            self.match(PalesMRParser.Format_code)
            self.state = 353
            self.match(PalesMRParser.Format_code)
            self.state = 354
            self.match(PalesMRParser.Format_code)
            self.state = 355
            self.match(PalesMRParser.Format_code)
            self.state = 356
            self.match(PalesMRParser.Format_code)
            self.state = 357
            self.match(PalesMRParser.RETURN_F)
            self.state = 359 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 358
                self.rdc_restraint_w_segid()
                self.state = 361 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PalesMRParser.Simple_name):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rdc_restraint_w_segidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(PalesMRParser.Simple_name)
            else:
                return self.getToken(PalesMRParser.Simple_name, i)

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(PalesMRParser.Integer)
            else:
                return self.getToken(PalesMRParser.Integer, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PalesMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(PalesMRParser.NumberContext,i)


        def getRuleIndex(self):
            return PalesMRParser.RULE_rdc_restraint_w_segid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRdc_restraint_w_segid" ):
                listener.enterRdc_restraint_w_segid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRdc_restraint_w_segid" ):
                listener.exitRdc_restraint_w_segid(self)




    def rdc_restraint_w_segid(self):

        localctx = PalesMRParser.Rdc_restraint_w_segidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_rdc_restraint_w_segid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(PalesMRParser.Simple_name)
            self.state = 364
            self.match(PalesMRParser.Integer)
            self.state = 365
            self.match(PalesMRParser.Simple_name)
            self.state = 366
            self.match(PalesMRParser.Simple_name)
            self.state = 367
            self.match(PalesMRParser.Simple_name)
            self.state = 368
            self.match(PalesMRParser.Integer)
            self.state = 369
            self.match(PalesMRParser.Simple_name)
            self.state = 370
            self.match(PalesMRParser.Simple_name)
            self.state = 371
            self.number()
            self.state = 372
            self.number()
            self.state = 373
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Coupling_restraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Vars(self):
            return self.getToken(PalesMRParser.Vars, 0)

        def Index(self):
            return self.getToken(PalesMRParser.Index, 0)

        def Resid_I(self):
            return self.getToken(PalesMRParser.Resid_I, 0)

        def Resname_I(self):
            return self.getToken(PalesMRParser.Resname_I, 0)

        def Atomname_I(self):
            return self.getToken(PalesMRParser.Atomname_I, 0)

        def Resid_J(self):
            return self.getToken(PalesMRParser.Resid_J, 0)

        def Resname_J(self):
            return self.getToken(PalesMRParser.Resname_J, 0)

        def Atomname_J(self):
            return self.getToken(PalesMRParser.Atomname_J, 0)

        def Resid_K(self):
            return self.getToken(PalesMRParser.Resid_K, 0)

        def Resname_K(self):
            return self.getToken(PalesMRParser.Resname_K, 0)

        def Atomname_K(self):
            return self.getToken(PalesMRParser.Atomname_K, 0)

        def Resid_L(self):
            return self.getToken(PalesMRParser.Resid_L, 0)

        def Resname_L(self):
            return self.getToken(PalesMRParser.Resname_L, 0)

        def Atomname_L(self):
            return self.getToken(PalesMRParser.Atomname_L, 0)

        def A(self):
            return self.getToken(PalesMRParser.A, 0)

        def B(self):
            return self.getToken(PalesMRParser.B, 0)

        def C(self):
            return self.getToken(PalesMRParser.C, 0)

        def Phase(self):
            return self.getToken(PalesMRParser.Phase, 0)

        def ObsJ(self):
            return self.getToken(PalesMRParser.ObsJ, 0)

        def FC(self):
            return self.getToken(PalesMRParser.FC, 0)

        def RETURN_V(self):
            return self.getToken(PalesMRParser.RETURN_V, 0)

        def Format(self):
            return self.getToken(PalesMRParser.Format, 0)

        def Format_code(self, i:int=None):
            if i is None:
                return self.getTokens(PalesMRParser.Format_code)
            else:
                return self.getToken(PalesMRParser.Format_code, i)

        def RETURN_F(self):
            return self.getToken(PalesMRParser.RETURN_F, 0)

        def coupling_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PalesMRParser.Coupling_restraintContext)
            else:
                return self.getTypedRuleContext(PalesMRParser.Coupling_restraintContext,i)


        def getRuleIndex(self):
            return PalesMRParser.RULE_coupling_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoupling_restraints" ):
                listener.enterCoupling_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoupling_restraints" ):
                listener.exitCoupling_restraints(self)




    def coupling_restraints(self):

        localctx = PalesMRParser.Coupling_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_coupling_restraints)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(PalesMRParser.Vars)
            self.state = 376
            self.match(PalesMRParser.Index)
            self.state = 377
            self.match(PalesMRParser.Resid_I)
            self.state = 378
            self.match(PalesMRParser.Resname_I)
            self.state = 379
            self.match(PalesMRParser.Atomname_I)
            self.state = 380
            self.match(PalesMRParser.Resid_J)
            self.state = 381
            self.match(PalesMRParser.Resname_J)
            self.state = 382
            self.match(PalesMRParser.Atomname_J)
            self.state = 383
            self.match(PalesMRParser.Resid_K)
            self.state = 384
            self.match(PalesMRParser.Resname_K)
            self.state = 385
            self.match(PalesMRParser.Atomname_K)
            self.state = 386
            self.match(PalesMRParser.Resid_L)
            self.state = 387
            self.match(PalesMRParser.Resname_L)
            self.state = 388
            self.match(PalesMRParser.Atomname_L)
            self.state = 389
            self.match(PalesMRParser.A)
            self.state = 390
            self.match(PalesMRParser.B)
            self.state = 391
            self.match(PalesMRParser.C)
            self.state = 392
            self.match(PalesMRParser.Phase)
            self.state = 393
            self.match(PalesMRParser.ObsJ)
            self.state = 394
            self.match(PalesMRParser.FC)
            self.state = 395
            self.match(PalesMRParser.RETURN_V)
            self.state = 396
            self.match(PalesMRParser.Format)
            self.state = 397
            self.match(PalesMRParser.Format_code)
            self.state = 398
            self.match(PalesMRParser.Format_code)
            self.state = 399
            self.match(PalesMRParser.Format_code)
            self.state = 400
            self.match(PalesMRParser.Format_code)
            self.state = 401
            self.match(PalesMRParser.Format_code)
            self.state = 402
            self.match(PalesMRParser.Format_code)
            self.state = 403
            self.match(PalesMRParser.Format_code)
            self.state = 404
            self.match(PalesMRParser.Format_code)
            self.state = 405
            self.match(PalesMRParser.Format_code)
            self.state = 406
            self.match(PalesMRParser.Format_code)
            self.state = 407
            self.match(PalesMRParser.Format_code)
            self.state = 408
            self.match(PalesMRParser.Format_code)
            self.state = 409
            self.match(PalesMRParser.Format_code)
            self.state = 410
            self.match(PalesMRParser.Format_code)
            self.state = 411
            self.match(PalesMRParser.Format_code)
            self.state = 412
            self.match(PalesMRParser.Format_code)
            self.state = 413
            self.match(PalesMRParser.Format_code)
            self.state = 414
            self.match(PalesMRParser.Format_code)
            self.state = 415
            self.match(PalesMRParser.Format_code)
            self.state = 416
            self.match(PalesMRParser.RETURN_F)
            self.state = 418 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 417
                self.coupling_restraint()
                self.state = 420 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PalesMRParser.Integer):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Coupling_restraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(PalesMRParser.Integer)
            else:
                return self.getToken(PalesMRParser.Integer, i)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(PalesMRParser.Simple_name)
            else:
                return self.getToken(PalesMRParser.Simple_name, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PalesMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(PalesMRParser.NumberContext,i)


        def getRuleIndex(self):
            return PalesMRParser.RULE_coupling_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoupling_restraint" ):
                listener.enterCoupling_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoupling_restraint" ):
                listener.exitCoupling_restraint(self)




    def coupling_restraint(self):

        localctx = PalesMRParser.Coupling_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_coupling_restraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(PalesMRParser.Integer)
            self.state = 423
            self.match(PalesMRParser.Integer)
            self.state = 424
            self.match(PalesMRParser.Simple_name)
            self.state = 425
            self.match(PalesMRParser.Simple_name)
            self.state = 426
            self.match(PalesMRParser.Integer)
            self.state = 427
            self.match(PalesMRParser.Simple_name)
            self.state = 428
            self.match(PalesMRParser.Simple_name)
            self.state = 429
            self.match(PalesMRParser.Integer)
            self.state = 430
            self.match(PalesMRParser.Simple_name)
            self.state = 431
            self.match(PalesMRParser.Simple_name)
            self.state = 432
            self.match(PalesMRParser.Integer)
            self.state = 433
            self.match(PalesMRParser.Simple_name)
            self.state = 434
            self.match(PalesMRParser.Simple_name)
            self.state = 435
            self.number()
            self.state = 436
            self.number()
            self.state = 437
            self.number()
            self.state = 438
            self.number()
            self.state = 439
            self.number()
            self.state = 440
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Coupling_restraints_w_segidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Vars(self):
            return self.getToken(PalesMRParser.Vars, 0)

        def Index(self):
            return self.getToken(PalesMRParser.Index, 0)

        def Segname_I(self):
            return self.getToken(PalesMRParser.Segname_I, 0)

        def Resid_I(self):
            return self.getToken(PalesMRParser.Resid_I, 0)

        def Resname_I(self):
            return self.getToken(PalesMRParser.Resname_I, 0)

        def Atomname_I(self):
            return self.getToken(PalesMRParser.Atomname_I, 0)

        def Segname_J(self):
            return self.getToken(PalesMRParser.Segname_J, 0)

        def Resid_J(self):
            return self.getToken(PalesMRParser.Resid_J, 0)

        def Resname_J(self):
            return self.getToken(PalesMRParser.Resname_J, 0)

        def Atomname_J(self):
            return self.getToken(PalesMRParser.Atomname_J, 0)

        def Segname_K(self):
            return self.getToken(PalesMRParser.Segname_K, 0)

        def Resid_K(self):
            return self.getToken(PalesMRParser.Resid_K, 0)

        def Resname_K(self):
            return self.getToken(PalesMRParser.Resname_K, 0)

        def Atomname_K(self):
            return self.getToken(PalesMRParser.Atomname_K, 0)

        def Segname_L(self):
            return self.getToken(PalesMRParser.Segname_L, 0)

        def Resid_L(self):
            return self.getToken(PalesMRParser.Resid_L, 0)

        def Resname_L(self):
            return self.getToken(PalesMRParser.Resname_L, 0)

        def Atomname_L(self):
            return self.getToken(PalesMRParser.Atomname_L, 0)

        def A(self):
            return self.getToken(PalesMRParser.A, 0)

        def B(self):
            return self.getToken(PalesMRParser.B, 0)

        def C(self):
            return self.getToken(PalesMRParser.C, 0)

        def Phase(self):
            return self.getToken(PalesMRParser.Phase, 0)

        def ObsJ(self):
            return self.getToken(PalesMRParser.ObsJ, 0)

        def FC(self):
            return self.getToken(PalesMRParser.FC, 0)

        def RETURN_V(self):
            return self.getToken(PalesMRParser.RETURN_V, 0)

        def Format(self):
            return self.getToken(PalesMRParser.Format, 0)

        def Format_code(self, i:int=None):
            if i is None:
                return self.getTokens(PalesMRParser.Format_code)
            else:
                return self.getToken(PalesMRParser.Format_code, i)

        def RETURN_F(self):
            return self.getToken(PalesMRParser.RETURN_F, 0)

        def coupling_restraint_w_segid(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PalesMRParser.Coupling_restraint_w_segidContext)
            else:
                return self.getTypedRuleContext(PalesMRParser.Coupling_restraint_w_segidContext,i)


        def getRuleIndex(self):
            return PalesMRParser.RULE_coupling_restraints_w_segid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoupling_restraints_w_segid" ):
                listener.enterCoupling_restraints_w_segid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoupling_restraints_w_segid" ):
                listener.exitCoupling_restraints_w_segid(self)




    def coupling_restraints_w_segid(self):

        localctx = PalesMRParser.Coupling_restraints_w_segidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_coupling_restraints_w_segid)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.match(PalesMRParser.Vars)
            self.state = 443
            self.match(PalesMRParser.Index)
            self.state = 444
            self.match(PalesMRParser.Segname_I)
            self.state = 445
            self.match(PalesMRParser.Resid_I)
            self.state = 446
            self.match(PalesMRParser.Resname_I)
            self.state = 447
            self.match(PalesMRParser.Atomname_I)
            self.state = 448
            self.match(PalesMRParser.Segname_J)
            self.state = 449
            self.match(PalesMRParser.Resid_J)
            self.state = 450
            self.match(PalesMRParser.Resname_J)
            self.state = 451
            self.match(PalesMRParser.Atomname_J)
            self.state = 452
            self.match(PalesMRParser.Segname_K)
            self.state = 453
            self.match(PalesMRParser.Resid_K)
            self.state = 454
            self.match(PalesMRParser.Resname_K)
            self.state = 455
            self.match(PalesMRParser.Atomname_K)
            self.state = 456
            self.match(PalesMRParser.Segname_L)
            self.state = 457
            self.match(PalesMRParser.Resid_L)
            self.state = 458
            self.match(PalesMRParser.Resname_L)
            self.state = 459
            self.match(PalesMRParser.Atomname_L)
            self.state = 460
            self.match(PalesMRParser.A)
            self.state = 461
            self.match(PalesMRParser.B)
            self.state = 462
            self.match(PalesMRParser.C)
            self.state = 463
            self.match(PalesMRParser.Phase)
            self.state = 464
            self.match(PalesMRParser.ObsJ)
            self.state = 465
            self.match(PalesMRParser.FC)
            self.state = 466
            self.match(PalesMRParser.RETURN_V)
            self.state = 467
            self.match(PalesMRParser.Format)
            self.state = 468
            self.match(PalesMRParser.Format_code)
            self.state = 469
            self.match(PalesMRParser.Format_code)
            self.state = 470
            self.match(PalesMRParser.Format_code)
            self.state = 471
            self.match(PalesMRParser.Format_code)
            self.state = 472
            self.match(PalesMRParser.Format_code)
            self.state = 473
            self.match(PalesMRParser.Format_code)
            self.state = 474
            self.match(PalesMRParser.Format_code)
            self.state = 475
            self.match(PalesMRParser.Format_code)
            self.state = 476
            self.match(PalesMRParser.Format_code)
            self.state = 477
            self.match(PalesMRParser.Format_code)
            self.state = 478
            self.match(PalesMRParser.Format_code)
            self.state = 479
            self.match(PalesMRParser.Format_code)
            self.state = 480
            self.match(PalesMRParser.Format_code)
            self.state = 481
            self.match(PalesMRParser.Format_code)
            self.state = 482
            self.match(PalesMRParser.Format_code)
            self.state = 483
            self.match(PalesMRParser.Format_code)
            self.state = 484
            self.match(PalesMRParser.Format_code)
            self.state = 485
            self.match(PalesMRParser.Format_code)
            self.state = 486
            self.match(PalesMRParser.Format_code)
            self.state = 487
            self.match(PalesMRParser.Format_code)
            self.state = 488
            self.match(PalesMRParser.Format_code)
            self.state = 489
            self.match(PalesMRParser.Format_code)
            self.state = 490
            self.match(PalesMRParser.Format_code)
            self.state = 491
            self.match(PalesMRParser.RETURN_F)
            self.state = 493 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 492
                self.coupling_restraint_w_segid()
                self.state = 495 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PalesMRParser.Integer):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Coupling_restraint_w_segidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(PalesMRParser.Integer)
            else:
                return self.getToken(PalesMRParser.Integer, i)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(PalesMRParser.Simple_name)
            else:
                return self.getToken(PalesMRParser.Simple_name, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PalesMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(PalesMRParser.NumberContext,i)


        def getRuleIndex(self):
            return PalesMRParser.RULE_coupling_restraint_w_segid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoupling_restraint_w_segid" ):
                listener.enterCoupling_restraint_w_segid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoupling_restraint_w_segid" ):
                listener.exitCoupling_restraint_w_segid(self)




    def coupling_restraint_w_segid(self):

        localctx = PalesMRParser.Coupling_restraint_w_segidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_coupling_restraint_w_segid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.match(PalesMRParser.Integer)
            self.state = 498
            self.match(PalesMRParser.Simple_name)
            self.state = 499
            self.match(PalesMRParser.Integer)
            self.state = 500
            self.match(PalesMRParser.Simple_name)
            self.state = 501
            self.match(PalesMRParser.Simple_name)
            self.state = 502
            self.match(PalesMRParser.Simple_name)
            self.state = 503
            self.match(PalesMRParser.Integer)
            self.state = 504
            self.match(PalesMRParser.Simple_name)
            self.state = 505
            self.match(PalesMRParser.Simple_name)
            self.state = 506
            self.match(PalesMRParser.Simple_name)
            self.state = 507
            self.match(PalesMRParser.Integer)
            self.state = 508
            self.match(PalesMRParser.Simple_name)
            self.state = 509
            self.match(PalesMRParser.Simple_name)
            self.state = 510
            self.match(PalesMRParser.Simple_name)
            self.state = 511
            self.match(PalesMRParser.Integer)
            self.state = 512
            self.match(PalesMRParser.Simple_name)
            self.state = 513
            self.match(PalesMRParser.Simple_name)
            self.state = 514
            self.number()
            self.state = 515
            self.number()
            self.state = 516
            self.number()
            self.state = 517
            self.number()
            self.state = 518
            self.number()
            self.state = 519
            self.number()
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
            return self.getToken(PalesMRParser.Float, 0)

        def Integer(self):
            return self.getToken(PalesMRParser.Integer, 0)

        def getRuleIndex(self):
            return PalesMRParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = PalesMRParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            _la = self._input.LA(1)
            if not(_la==PalesMRParser.Integer or _la==PalesMRParser.Float):
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





