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
        4,1,73,576,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,53,8,0,10,0,12,
        0,56,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,4,1,65,8,1,11,1,12,1,66,3,1,
        69,8,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,4,2,104,8,2,11,2,12,2,105,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,4,4,157,8,4,11,4,12,4,158,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,4,6,214,8,6,11,6,12,6,215,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,4,8,280,8,8,11,8,12,8,281,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,4,10,328,8,10,11,10,12,10,329,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,4,12,369,8,12,11,12,12,12,370,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,4,14,428,8,14,11,14,12,14,429,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        4,16,503,8,16,11,16,12,16,504,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,4,18,558,8,18,11,18,12,18,559,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,
        0,0,21,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        0,1,1,0,4,5,575,0,54,1,0,0,0,2,59,1,0,0,0,4,72,1,0,0,0,6,107,1,0,
        0,0,8,121,1,0,0,0,10,160,1,0,0,0,12,176,1,0,0,0,14,217,1,0,0,0,16,
        234,1,0,0,0,18,283,1,0,0,0,20,304,1,0,0,0,22,331,1,0,0,0,24,341,
        1,0,0,0,26,372,1,0,0,0,28,384,1,0,0,0,30,431,1,0,0,0,32,451,1,0,
        0,0,34,506,1,0,0,0,36,530,1,0,0,0,38,561,1,0,0,0,40,573,1,0,0,0,
        42,53,3,2,1,0,43,53,3,4,2,0,44,53,3,8,4,0,45,53,3,12,6,0,46,53,3,
        16,8,0,47,53,3,20,10,0,48,53,3,24,12,0,49,53,3,28,14,0,50,53,3,32,
        16,0,51,53,3,36,18,0,52,42,1,0,0,0,52,43,1,0,0,0,52,44,1,0,0,0,52,
        45,1,0,0,0,52,46,1,0,0,0,52,47,1,0,0,0,52,48,1,0,0,0,52,49,1,0,0,
        0,52,50,1,0,0,0,52,51,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,
        1,0,0,0,55,57,1,0,0,0,56,54,1,0,0,0,57,58,5,0,0,1,58,1,1,0,0,0,59,
        68,5,1,0,0,60,61,5,14,0,0,61,69,5,17,0,0,62,64,5,15,0,0,63,65,5,
        16,0,0,64,63,1,0,0,0,65,66,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,
        69,1,0,0,0,68,60,1,0,0,0,68,62,1,0,0,0,69,70,1,0,0,0,70,71,5,19,
        0,0,71,3,1,0,0,0,72,73,5,2,0,0,73,74,5,22,0,0,74,75,5,23,0,0,75,
        76,5,25,0,0,76,77,5,26,0,0,77,78,5,27,0,0,78,79,5,29,0,0,79,80,5,
        30,0,0,80,81,5,31,0,0,81,82,5,50,0,0,82,83,5,51,0,0,83,84,5,47,0,
        0,84,85,5,49,0,0,85,86,5,48,0,0,86,87,5,66,0,0,87,88,5,3,0,0,88,
        89,5,69,0,0,89,90,5,69,0,0,90,91,5,69,0,0,91,92,5,69,0,0,92,93,5,
        69,0,0,93,94,5,69,0,0,94,95,5,69,0,0,95,96,5,69,0,0,96,97,5,69,0,
        0,97,98,5,69,0,0,98,99,5,69,0,0,99,100,5,69,0,0,100,101,5,69,0,0,
        101,103,5,71,0,0,102,104,3,6,3,0,103,102,1,0,0,0,104,105,1,0,0,0,
        105,103,1,0,0,0,105,106,1,0,0,0,106,5,1,0,0,0,107,108,5,4,0,0,108,
        109,5,4,0,0,109,110,5,4,0,0,110,111,5,9,0,0,111,112,5,9,0,0,112,
        113,5,4,0,0,113,114,5,9,0,0,114,115,5,9,0,0,115,116,3,40,20,0,116,
        117,3,40,20,0,117,118,3,40,20,0,118,119,3,40,20,0,119,120,3,40,20,
        0,120,7,1,0,0,0,121,122,5,2,0,0,122,123,5,22,0,0,123,124,5,23,0,
        0,124,125,5,24,0,0,125,126,5,25,0,0,126,127,5,26,0,0,127,128,5,27,
        0,0,128,129,5,28,0,0,129,130,5,29,0,0,130,131,5,30,0,0,131,132,5,
        31,0,0,132,133,5,50,0,0,133,134,5,51,0,0,134,135,5,47,0,0,135,136,
        5,49,0,0,136,137,5,48,0,0,137,138,5,66,0,0,138,139,5,3,0,0,139,140,
        5,69,0,0,140,141,5,69,0,0,141,142,5,69,0,0,142,143,5,69,0,0,143,
        144,5,69,0,0,144,145,5,69,0,0,145,146,5,69,0,0,146,147,5,69,0,0,
        147,148,5,69,0,0,148,149,5,69,0,0,149,150,5,69,0,0,150,151,5,69,
        0,0,151,152,5,69,0,0,152,153,5,69,0,0,153,154,5,69,0,0,154,156,5,
        71,0,0,155,157,3,10,5,0,156,155,1,0,0,0,157,158,1,0,0,0,158,156,
        1,0,0,0,158,159,1,0,0,0,159,9,1,0,0,0,160,161,5,4,0,0,161,162,5,
        4,0,0,162,163,5,9,0,0,163,164,5,4,0,0,164,165,5,9,0,0,165,166,5,
        9,0,0,166,167,5,9,0,0,167,168,5,4,0,0,168,169,5,9,0,0,169,170,5,
        9,0,0,170,171,3,40,20,0,171,172,3,40,20,0,172,173,3,40,20,0,173,
        174,3,40,20,0,174,175,3,40,20,0,175,11,1,0,0,0,176,177,5,2,0,0,177,
        178,5,22,0,0,178,179,5,25,0,0,179,180,5,26,0,0,180,181,5,27,0,0,
        181,182,5,29,0,0,182,183,5,30,0,0,183,184,5,31,0,0,184,185,5,33,
        0,0,185,186,5,34,0,0,186,187,5,35,0,0,187,188,5,37,0,0,188,189,5,
        38,0,0,189,190,5,39,0,0,190,191,5,52,0,0,191,192,5,53,0,0,192,193,
        5,47,0,0,193,194,5,66,0,0,194,195,5,3,0,0,195,196,5,69,0,0,196,197,
        5,69,0,0,197,198,5,69,0,0,198,199,5,69,0,0,199,200,5,69,0,0,200,
        201,5,69,0,0,201,202,5,69,0,0,202,203,5,69,0,0,203,204,5,69,0,0,
        204,205,5,69,0,0,205,206,5,69,0,0,206,207,5,69,0,0,207,208,5,69,
        0,0,208,209,5,69,0,0,209,210,5,69,0,0,210,211,5,69,0,0,211,213,5,
        71,0,0,212,214,3,14,7,0,213,212,1,0,0,0,214,215,1,0,0,0,215,213,
        1,0,0,0,215,216,1,0,0,0,216,13,1,0,0,0,217,218,5,4,0,0,218,219,5,
        4,0,0,219,220,5,9,0,0,220,221,5,9,0,0,221,222,5,4,0,0,222,223,5,
        9,0,0,223,224,5,9,0,0,224,225,5,4,0,0,225,226,5,9,0,0,226,227,5,
        9,0,0,227,228,5,4,0,0,228,229,5,9,0,0,229,230,5,9,0,0,230,231,3,
        40,20,0,231,232,3,40,20,0,232,233,3,40,20,0,233,15,1,0,0,0,234,235,
        5,2,0,0,235,236,5,22,0,0,236,237,5,24,0,0,237,238,5,25,0,0,238,239,
        5,26,0,0,239,240,5,27,0,0,240,241,5,28,0,0,241,242,5,29,0,0,242,
        243,5,30,0,0,243,244,5,31,0,0,244,245,5,32,0,0,245,246,5,33,0,0,
        246,247,5,34,0,0,247,248,5,35,0,0,248,249,5,36,0,0,249,250,5,37,
        0,0,250,251,5,38,0,0,251,252,5,39,0,0,252,253,5,52,0,0,253,254,5,
        53,0,0,254,255,5,47,0,0,255,256,5,66,0,0,256,257,5,3,0,0,257,258,
        5,69,0,0,258,259,5,69,0,0,259,260,5,69,0,0,260,261,5,69,0,0,261,
        262,5,69,0,0,262,263,5,69,0,0,263,264,5,69,0,0,264,265,5,69,0,0,
        265,266,5,69,0,0,266,267,5,69,0,0,267,268,5,69,0,0,268,269,5,69,
        0,0,269,270,5,69,0,0,270,271,5,69,0,0,271,272,5,69,0,0,272,273,5,
        69,0,0,273,274,5,69,0,0,274,275,5,69,0,0,275,276,5,69,0,0,276,277,
        5,69,0,0,277,279,5,71,0,0,278,280,3,18,9,0,279,278,1,0,0,0,280,281,
        1,0,0,0,281,279,1,0,0,0,281,282,1,0,0,0,282,17,1,0,0,0,283,284,5,
        4,0,0,284,285,5,9,0,0,285,286,5,4,0,0,286,287,5,9,0,0,287,288,5,
        9,0,0,288,289,5,9,0,0,289,290,5,4,0,0,290,291,5,9,0,0,291,292,5,
        9,0,0,292,293,5,9,0,0,293,294,5,4,0,0,294,295,5,9,0,0,295,296,5,
        9,0,0,296,297,5,9,0,0,297,298,5,4,0,0,298,299,5,9,0,0,299,300,5,
        9,0,0,300,301,3,40,20,0,301,302,3,40,20,0,302,303,3,40,20,0,303,
        19,1,0,0,0,304,305,5,2,0,0,305,306,5,25,0,0,306,307,5,26,0,0,307,
        308,5,27,0,0,308,309,5,29,0,0,309,310,5,30,0,0,310,311,5,31,0,0,
        311,312,5,45,0,0,312,313,5,46,0,0,313,314,5,49,0,0,314,315,5,66,
        0,0,315,316,5,3,0,0,316,317,5,69,0,0,317,318,5,69,0,0,318,319,5,
        69,0,0,319,320,5,69,0,0,320,321,5,69,0,0,321,322,5,69,0,0,322,323,
        5,69,0,0,323,324,5,69,0,0,324,325,5,69,0,0,325,327,5,71,0,0,326,
        328,3,22,11,0,327,326,1,0,0,0,328,329,1,0,0,0,329,327,1,0,0,0,329,
        330,1,0,0,0,330,21,1,0,0,0,331,332,5,4,0,0,332,333,5,9,0,0,333,334,
        5,9,0,0,334,335,5,4,0,0,335,336,5,9,0,0,336,337,5,9,0,0,337,338,
        3,40,20,0,338,339,3,40,20,0,339,340,3,40,20,0,340,23,1,0,0,0,341,
        342,5,2,0,0,342,343,5,24,0,0,343,344,5,25,0,0,344,345,5,26,0,0,345,
        346,5,27,0,0,346,347,5,28,0,0,347,348,5,29,0,0,348,349,5,30,0,0,
        349,350,5,31,0,0,350,351,5,45,0,0,351,352,5,46,0,0,352,353,5,49,
        0,0,353,354,5,66,0,0,354,355,5,3,0,0,355,356,5,69,0,0,356,357,5,
        69,0,0,357,358,5,69,0,0,358,359,5,69,0,0,359,360,5,69,0,0,360,361,
        5,69,0,0,361,362,5,69,0,0,362,363,5,69,0,0,363,364,5,69,0,0,364,
        365,5,69,0,0,365,366,5,69,0,0,366,368,5,71,0,0,367,369,3,26,13,0,
        368,367,1,0,0,0,369,370,1,0,0,0,370,368,1,0,0,0,370,371,1,0,0,0,
        371,25,1,0,0,0,372,373,5,9,0,0,373,374,5,4,0,0,374,375,5,9,0,0,375,
        376,5,9,0,0,376,377,5,9,0,0,377,378,5,4,0,0,378,379,5,9,0,0,379,
        380,5,9,0,0,380,381,3,40,20,0,381,382,3,40,20,0,382,383,3,40,20,
        0,383,27,1,0,0,0,384,385,5,2,0,0,385,386,5,22,0,0,386,387,5,25,0,
        0,387,388,5,26,0,0,388,389,5,27,0,0,389,390,5,29,0,0,390,391,5,30,
        0,0,391,392,5,31,0,0,392,393,5,33,0,0,393,394,5,34,0,0,394,395,5,
        35,0,0,395,396,5,37,0,0,396,397,5,38,0,0,397,398,5,39,0,0,398,399,
        5,42,0,0,399,400,5,43,0,0,400,401,5,44,0,0,401,402,5,54,0,0,402,
        403,5,55,0,0,403,404,5,47,0,0,404,405,5,66,0,0,405,406,5,3,0,0,406,
        407,5,69,0,0,407,408,5,69,0,0,408,409,5,69,0,0,409,410,5,69,0,0,
        410,411,5,69,0,0,411,412,5,69,0,0,412,413,5,69,0,0,413,414,5,69,
        0,0,414,415,5,69,0,0,415,416,5,69,0,0,416,417,5,69,0,0,417,418,5,
        69,0,0,418,419,5,69,0,0,419,420,5,69,0,0,420,421,5,69,0,0,421,422,
        5,69,0,0,422,423,5,69,0,0,423,424,5,69,0,0,424,425,5,69,0,0,425,
        427,5,71,0,0,426,428,3,30,15,0,427,426,1,0,0,0,428,429,1,0,0,0,429,
        427,1,0,0,0,429,430,1,0,0,0,430,29,1,0,0,0,431,432,5,4,0,0,432,433,
        5,4,0,0,433,434,5,9,0,0,434,435,5,9,0,0,435,436,5,4,0,0,436,437,
        5,9,0,0,437,438,5,9,0,0,438,439,5,4,0,0,439,440,5,9,0,0,440,441,
        5,9,0,0,441,442,5,4,0,0,442,443,5,9,0,0,443,444,5,9,0,0,444,445,
        3,40,20,0,445,446,3,40,20,0,446,447,3,40,20,0,447,448,3,40,20,0,
        448,449,3,40,20,0,449,450,3,40,20,0,450,31,1,0,0,0,451,452,5,2,0,
        0,452,453,5,22,0,0,453,454,5,24,0,0,454,455,5,25,0,0,455,456,5,26,
        0,0,456,457,5,27,0,0,457,458,5,28,0,0,458,459,5,29,0,0,459,460,5,
        30,0,0,460,461,5,31,0,0,461,462,5,32,0,0,462,463,5,33,0,0,463,464,
        5,34,0,0,464,465,5,35,0,0,465,466,5,36,0,0,466,467,5,37,0,0,467,
        468,5,38,0,0,468,469,5,39,0,0,469,470,5,42,0,0,470,471,5,43,0,0,
        471,472,5,44,0,0,472,473,5,54,0,0,473,474,5,55,0,0,474,475,5,47,
        0,0,475,476,5,66,0,0,476,477,5,3,0,0,477,478,5,69,0,0,478,479,5,
        69,0,0,479,480,5,69,0,0,480,481,5,69,0,0,481,482,5,69,0,0,482,483,
        5,69,0,0,483,484,5,69,0,0,484,485,5,69,0,0,485,486,5,69,0,0,486,
        487,5,69,0,0,487,488,5,69,0,0,488,489,5,69,0,0,489,490,5,69,0,0,
        490,491,5,69,0,0,491,492,5,69,0,0,492,493,5,69,0,0,493,494,5,69,
        0,0,494,495,5,69,0,0,495,496,5,69,0,0,496,497,5,69,0,0,497,498,5,
        69,0,0,498,499,5,69,0,0,499,500,5,69,0,0,500,502,5,71,0,0,501,503,
        3,34,17,0,502,501,1,0,0,0,503,504,1,0,0,0,504,502,1,0,0,0,504,505,
        1,0,0,0,505,33,1,0,0,0,506,507,5,4,0,0,507,508,5,9,0,0,508,509,5,
        4,0,0,509,510,5,9,0,0,510,511,5,9,0,0,511,512,5,9,0,0,512,513,5,
        4,0,0,513,514,5,9,0,0,514,515,5,9,0,0,515,516,5,9,0,0,516,517,5,
        4,0,0,517,518,5,9,0,0,518,519,5,9,0,0,519,520,5,9,0,0,520,521,5,
        4,0,0,521,522,5,9,0,0,522,523,5,9,0,0,523,524,3,40,20,0,524,525,
        3,40,20,0,525,526,3,40,20,0,526,527,3,40,20,0,527,528,3,40,20,0,
        528,529,3,40,20,0,529,35,1,0,0,0,530,531,5,2,0,0,531,532,5,40,0,
        0,532,533,5,41,0,0,533,534,5,56,0,0,534,535,5,57,0,0,535,536,5,58,
        0,0,536,537,5,59,0,0,537,538,5,60,0,0,538,539,5,61,0,0,539,540,5,
        62,0,0,540,541,5,63,0,0,541,542,5,64,0,0,542,543,5,66,0,0,543,544,
        5,3,0,0,544,545,5,69,0,0,545,546,5,69,0,0,546,547,5,69,0,0,547,548,
        5,69,0,0,548,549,5,69,0,0,549,550,5,69,0,0,550,551,5,69,0,0,551,
        552,5,69,0,0,552,553,5,69,0,0,553,554,5,69,0,0,554,555,5,69,0,0,
        555,557,5,71,0,0,556,558,3,38,19,0,557,556,1,0,0,0,558,559,1,0,0,
        0,559,557,1,0,0,0,559,560,1,0,0,0,560,37,1,0,0,0,561,562,5,4,0,0,
        562,563,5,9,0,0,563,564,3,40,20,0,564,565,3,40,20,0,565,566,3,40,
        20,0,566,567,3,40,20,0,567,568,3,40,20,0,568,569,3,40,20,0,569,570,
        5,4,0,0,570,571,5,4,0,0,571,572,5,9,0,0,572,39,1,0,0,0,573,574,7,
        0,0,0,574,41,1,0,0,0,13,52,54,66,68,105,158,215,281,329,370,429,
        504,559
    ]

class PalesMRParser ( Parser ):

    grammarFileName = "PalesMRParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'DATA'", "'VARS'", "'FORMAT'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'FIRST_RESID'", "'SEQUENCE'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'INDEX'", "'GROUP'", "'SEGNAME_I'", "'RESID_I'", 
                     "'RESNAME_I'", "'ATOMNAME_I'", "'SEGNAME_J'", "'RESID_J'", 
                     "'RESNAME_J'", "'ATOMNAME_J'", "'SEGNAME_K'", "'RESID_K'", 
                     "'RESNAME_K'", "'ATOMNAME_K'", "'SEGNAME_L'", "'RESID_L'", 
                     "'RESNAME_L'", "'ATOMNAME_L'", "'RESID'", "'RESNAME'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'D_LO'", "'D_HI'", "'ANGLE_LO'", "'ANGLE_HI'", "'PHASE'", 
                     "'OBSJ'", "'PHI'", "'PSI'", "'DPHI'", "'DPSI'", "'DIST'", 
                     "'S2'", "'COUNT'", "'CS_COUNT'", "'CLASS'" ]

    symbolicNames = [ "<INVALID>", "Data", "Vars", "Format", "Integer", 
                      "Float", "SHARP_COMMENT", "EXCLM_COMMENT", "SMCLN_COMMENT", 
                      "Simple_name", "SPACE", "COMMENT", "SECTION_COMMENT", 
                      "LINE_COMMENT", "First_resid", "Sequence", "One_letter_code", 
                      "Integer_D", "SPACE_D", "RETURN_D", "SECTION_COMMENT_D", 
                      "LINE_COMMENT_D", "Index", "Group", "Segname_I", "Resid_I", 
                      "Resname_I", "Atomname_I", "Segname_J", "Resid_J", 
                      "Resname_J", "Atomname_J", "Segname_K", "Resid_K", 
                      "Resname_K", "Atomname_K", "Segname_L", "Resid_L", 
                      "Resname_L", "Atomname_L", "Resid", "Resname", "A", 
                      "B", "C", "D", "DD", "FC", "S", "W", "D_Lo", "D_Hi", 
                      "Angle_Lo", "Angle_Hi", "Phase", "ObsJ", "Phi", "Psi", 
                      "Dphi", "Dpsi", "Dist", "S2", "Count", "Cs_count", 
                      "Class", "SPACE_V", "RETURN_V", "SECTION_COMMENT_V", 
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
    RULE_talos_restraints = 18
    RULE_talos_restraint = 19
    RULE_number = 20

    ruleNames =  [ "pales_mr", "sequence", "distance_restraints", "distance_restraint", 
                   "distance_restraints_w_segid", "distance_restraint_w_segid", 
                   "torsion_angle_restraints", "torsion_angle_restraint", 
                   "torsion_angle_restraints_w_segid", "torsion_angle_restraint_w_segid", 
                   "rdc_restraints", "rdc_restraint", "rdc_restraints_w_segid", 
                   "rdc_restraint_w_segid", "coupling_restraints", "coupling_restraint", 
                   "coupling_restraints_w_segid", "coupling_restraint_w_segid", 
                   "talos_restraints", "talos_restraint", "number" ]

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
    First_resid=14
    Sequence=15
    One_letter_code=16
    Integer_D=17
    SPACE_D=18
    RETURN_D=19
    SECTION_COMMENT_D=20
    LINE_COMMENT_D=21
    Index=22
    Group=23
    Segname_I=24
    Resid_I=25
    Resname_I=26
    Atomname_I=27
    Segname_J=28
    Resid_J=29
    Resname_J=30
    Atomname_J=31
    Segname_K=32
    Resid_K=33
    Resname_K=34
    Atomname_K=35
    Segname_L=36
    Resid_L=37
    Resname_L=38
    Atomname_L=39
    Resid=40
    Resname=41
    A=42
    B=43
    C=44
    D=45
    DD=46
    FC=47
    S=48
    W=49
    D_Lo=50
    D_Hi=51
    Angle_Lo=52
    Angle_Hi=53
    Phase=54
    ObsJ=55
    Phi=56
    Psi=57
    Dphi=58
    Dpsi=59
    Dist=60
    S2=61
    Count=62
    Cs_count=63
    Class=64
    SPACE_V=65
    RETURN_V=66
    SECTION_COMMENT_V=67
    LINE_COMMENT_V=68
    Format_code=69
    SPACE_F=70
    RETURN_F=71
    SECTION_COMMENT_F=72
    LINE_COMMENT_F=73

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


        def talos_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PalesMRParser.Talos_restraintsContext)
            else:
                return self.getTypedRuleContext(PalesMRParser.Talos_restraintsContext,i)


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
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PalesMRParser.Data or _la==PalesMRParser.Vars:
                self.state = 52
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 42
                    self.sequence()
                    pass

                elif la_ == 2:
                    self.state = 43
                    self.distance_restraints()
                    pass

                elif la_ == 3:
                    self.state = 44
                    self.distance_restraints_w_segid()
                    pass

                elif la_ == 4:
                    self.state = 45
                    self.torsion_angle_restraints()
                    pass

                elif la_ == 5:
                    self.state = 46
                    self.torsion_angle_restraints_w_segid()
                    pass

                elif la_ == 6:
                    self.state = 47
                    self.rdc_restraints()
                    pass

                elif la_ == 7:
                    self.state = 48
                    self.rdc_restraints_w_segid()
                    pass

                elif la_ == 8:
                    self.state = 49
                    self.coupling_restraints()
                    pass

                elif la_ == 9:
                    self.state = 50
                    self.coupling_restraints_w_segid()
                    pass

                elif la_ == 10:
                    self.state = 51
                    self.talos_restraints()
                    pass


                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 57
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

        def RETURN_D(self):
            return self.getToken(PalesMRParser.RETURN_D, 0)

        def First_resid(self):
            return self.getToken(PalesMRParser.First_resid, 0)

        def Integer_D(self):
            return self.getToken(PalesMRParser.Integer_D, 0)

        def Sequence(self):
            return self.getToken(PalesMRParser.Sequence, 0)

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
            self.state = 59
            self.match(PalesMRParser.Data)
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PalesMRParser.First_resid]:
                self.state = 60
                self.match(PalesMRParser.First_resid)
                self.state = 61
                self.match(PalesMRParser.Integer_D)
                pass
            elif token in [PalesMRParser.Sequence]:
                self.state = 62
                self.match(PalesMRParser.Sequence)
                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 63
                    self.match(PalesMRParser.One_letter_code)
                    self.state = 66 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==PalesMRParser.One_letter_code):
                        break

                pass
            else:
                raise NoViableAltException(self)

            self.state = 70
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
            self.state = 72
            self.match(PalesMRParser.Vars)
            self.state = 73
            self.match(PalesMRParser.Index)
            self.state = 74
            self.match(PalesMRParser.Group)
            self.state = 75
            self.match(PalesMRParser.Resid_I)
            self.state = 76
            self.match(PalesMRParser.Resname_I)
            self.state = 77
            self.match(PalesMRParser.Atomname_I)
            self.state = 78
            self.match(PalesMRParser.Resid_J)
            self.state = 79
            self.match(PalesMRParser.Resname_J)
            self.state = 80
            self.match(PalesMRParser.Atomname_J)
            self.state = 81
            self.match(PalesMRParser.D_Lo)
            self.state = 82
            self.match(PalesMRParser.D_Hi)
            self.state = 83
            self.match(PalesMRParser.FC)
            self.state = 84
            self.match(PalesMRParser.W)
            self.state = 85
            self.match(PalesMRParser.S)
            self.state = 86
            self.match(PalesMRParser.RETURN_V)
            self.state = 87
            self.match(PalesMRParser.Format)
            self.state = 88
            self.match(PalesMRParser.Format_code)
            self.state = 89
            self.match(PalesMRParser.Format_code)
            self.state = 90
            self.match(PalesMRParser.Format_code)
            self.state = 91
            self.match(PalesMRParser.Format_code)
            self.state = 92
            self.match(PalesMRParser.Format_code)
            self.state = 93
            self.match(PalesMRParser.Format_code)
            self.state = 94
            self.match(PalesMRParser.Format_code)
            self.state = 95
            self.match(PalesMRParser.Format_code)
            self.state = 96
            self.match(PalesMRParser.Format_code)
            self.state = 97
            self.match(PalesMRParser.Format_code)
            self.state = 98
            self.match(PalesMRParser.Format_code)
            self.state = 99
            self.match(PalesMRParser.Format_code)
            self.state = 100
            self.match(PalesMRParser.Format_code)
            self.state = 101
            self.match(PalesMRParser.RETURN_F)
            self.state = 103 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 102
                self.distance_restraint()
                self.state = 105 
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
            self.state = 107
            self.match(PalesMRParser.Integer)
            self.state = 108
            self.match(PalesMRParser.Integer)
            self.state = 109
            self.match(PalesMRParser.Integer)
            self.state = 110
            self.match(PalesMRParser.Simple_name)
            self.state = 111
            self.match(PalesMRParser.Simple_name)
            self.state = 112
            self.match(PalesMRParser.Integer)
            self.state = 113
            self.match(PalesMRParser.Simple_name)
            self.state = 114
            self.match(PalesMRParser.Simple_name)
            self.state = 115
            self.number()
            self.state = 116
            self.number()
            self.state = 117
            self.number()
            self.state = 118
            self.number()
            self.state = 119
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
            self.state = 121
            self.match(PalesMRParser.Vars)
            self.state = 122
            self.match(PalesMRParser.Index)
            self.state = 123
            self.match(PalesMRParser.Group)
            self.state = 124
            self.match(PalesMRParser.Segname_I)
            self.state = 125
            self.match(PalesMRParser.Resid_I)
            self.state = 126
            self.match(PalesMRParser.Resname_I)
            self.state = 127
            self.match(PalesMRParser.Atomname_I)
            self.state = 128
            self.match(PalesMRParser.Segname_J)
            self.state = 129
            self.match(PalesMRParser.Resid_J)
            self.state = 130
            self.match(PalesMRParser.Resname_J)
            self.state = 131
            self.match(PalesMRParser.Atomname_J)
            self.state = 132
            self.match(PalesMRParser.D_Lo)
            self.state = 133
            self.match(PalesMRParser.D_Hi)
            self.state = 134
            self.match(PalesMRParser.FC)
            self.state = 135
            self.match(PalesMRParser.W)
            self.state = 136
            self.match(PalesMRParser.S)
            self.state = 137
            self.match(PalesMRParser.RETURN_V)
            self.state = 138
            self.match(PalesMRParser.Format)
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
            self.match(PalesMRParser.Format_code)
            self.state = 146
            self.match(PalesMRParser.Format_code)
            self.state = 147
            self.match(PalesMRParser.Format_code)
            self.state = 148
            self.match(PalesMRParser.Format_code)
            self.state = 149
            self.match(PalesMRParser.Format_code)
            self.state = 150
            self.match(PalesMRParser.Format_code)
            self.state = 151
            self.match(PalesMRParser.Format_code)
            self.state = 152
            self.match(PalesMRParser.Format_code)
            self.state = 153
            self.match(PalesMRParser.Format_code)
            self.state = 154
            self.match(PalesMRParser.RETURN_F)
            self.state = 156 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 155
                self.distance_restraint_w_segid()
                self.state = 158 
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
            self.state = 160
            self.match(PalesMRParser.Integer)
            self.state = 161
            self.match(PalesMRParser.Integer)
            self.state = 162
            self.match(PalesMRParser.Simple_name)
            self.state = 163
            self.match(PalesMRParser.Integer)
            self.state = 164
            self.match(PalesMRParser.Simple_name)
            self.state = 165
            self.match(PalesMRParser.Simple_name)
            self.state = 166
            self.match(PalesMRParser.Simple_name)
            self.state = 167
            self.match(PalesMRParser.Integer)
            self.state = 168
            self.match(PalesMRParser.Simple_name)
            self.state = 169
            self.match(PalesMRParser.Simple_name)
            self.state = 170
            self.number()
            self.state = 171
            self.number()
            self.state = 172
            self.number()
            self.state = 173
            self.number()
            self.state = 174
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
            self.state = 176
            self.match(PalesMRParser.Vars)
            self.state = 177
            self.match(PalesMRParser.Index)
            self.state = 178
            self.match(PalesMRParser.Resid_I)
            self.state = 179
            self.match(PalesMRParser.Resname_I)
            self.state = 180
            self.match(PalesMRParser.Atomname_I)
            self.state = 181
            self.match(PalesMRParser.Resid_J)
            self.state = 182
            self.match(PalesMRParser.Resname_J)
            self.state = 183
            self.match(PalesMRParser.Atomname_J)
            self.state = 184
            self.match(PalesMRParser.Resid_K)
            self.state = 185
            self.match(PalesMRParser.Resname_K)
            self.state = 186
            self.match(PalesMRParser.Atomname_K)
            self.state = 187
            self.match(PalesMRParser.Resid_L)
            self.state = 188
            self.match(PalesMRParser.Resname_L)
            self.state = 189
            self.match(PalesMRParser.Atomname_L)
            self.state = 190
            self.match(PalesMRParser.Angle_Lo)
            self.state = 191
            self.match(PalesMRParser.Angle_Hi)
            self.state = 192
            self.match(PalesMRParser.FC)
            self.state = 193
            self.match(PalesMRParser.RETURN_V)
            self.state = 194
            self.match(PalesMRParser.Format)
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
            self.match(PalesMRParser.Format_code)
            self.state = 203
            self.match(PalesMRParser.Format_code)
            self.state = 204
            self.match(PalesMRParser.Format_code)
            self.state = 205
            self.match(PalesMRParser.Format_code)
            self.state = 206
            self.match(PalesMRParser.Format_code)
            self.state = 207
            self.match(PalesMRParser.Format_code)
            self.state = 208
            self.match(PalesMRParser.Format_code)
            self.state = 209
            self.match(PalesMRParser.Format_code)
            self.state = 210
            self.match(PalesMRParser.Format_code)
            self.state = 211
            self.match(PalesMRParser.RETURN_F)
            self.state = 213 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 212
                self.torsion_angle_restraint()
                self.state = 215 
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
            self.state = 217
            self.match(PalesMRParser.Integer)
            self.state = 218
            self.match(PalesMRParser.Integer)
            self.state = 219
            self.match(PalesMRParser.Simple_name)
            self.state = 220
            self.match(PalesMRParser.Simple_name)
            self.state = 221
            self.match(PalesMRParser.Integer)
            self.state = 222
            self.match(PalesMRParser.Simple_name)
            self.state = 223
            self.match(PalesMRParser.Simple_name)
            self.state = 224
            self.match(PalesMRParser.Integer)
            self.state = 225
            self.match(PalesMRParser.Simple_name)
            self.state = 226
            self.match(PalesMRParser.Simple_name)
            self.state = 227
            self.match(PalesMRParser.Integer)
            self.state = 228
            self.match(PalesMRParser.Simple_name)
            self.state = 229
            self.match(PalesMRParser.Simple_name)
            self.state = 230
            self.number()
            self.state = 231
            self.number()
            self.state = 232
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
            self.state = 234
            self.match(PalesMRParser.Vars)
            self.state = 235
            self.match(PalesMRParser.Index)
            self.state = 236
            self.match(PalesMRParser.Segname_I)
            self.state = 237
            self.match(PalesMRParser.Resid_I)
            self.state = 238
            self.match(PalesMRParser.Resname_I)
            self.state = 239
            self.match(PalesMRParser.Atomname_I)
            self.state = 240
            self.match(PalesMRParser.Segname_J)
            self.state = 241
            self.match(PalesMRParser.Resid_J)
            self.state = 242
            self.match(PalesMRParser.Resname_J)
            self.state = 243
            self.match(PalesMRParser.Atomname_J)
            self.state = 244
            self.match(PalesMRParser.Segname_K)
            self.state = 245
            self.match(PalesMRParser.Resid_K)
            self.state = 246
            self.match(PalesMRParser.Resname_K)
            self.state = 247
            self.match(PalesMRParser.Atomname_K)
            self.state = 248
            self.match(PalesMRParser.Segname_L)
            self.state = 249
            self.match(PalesMRParser.Resid_L)
            self.state = 250
            self.match(PalesMRParser.Resname_L)
            self.state = 251
            self.match(PalesMRParser.Atomname_L)
            self.state = 252
            self.match(PalesMRParser.Angle_Lo)
            self.state = 253
            self.match(PalesMRParser.Angle_Hi)
            self.state = 254
            self.match(PalesMRParser.FC)
            self.state = 255
            self.match(PalesMRParser.RETURN_V)
            self.state = 256
            self.match(PalesMRParser.Format)
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
            self.match(PalesMRParser.Format_code)
            self.state = 269
            self.match(PalesMRParser.Format_code)
            self.state = 270
            self.match(PalesMRParser.Format_code)
            self.state = 271
            self.match(PalesMRParser.Format_code)
            self.state = 272
            self.match(PalesMRParser.Format_code)
            self.state = 273
            self.match(PalesMRParser.Format_code)
            self.state = 274
            self.match(PalesMRParser.Format_code)
            self.state = 275
            self.match(PalesMRParser.Format_code)
            self.state = 276
            self.match(PalesMRParser.Format_code)
            self.state = 277
            self.match(PalesMRParser.RETURN_F)
            self.state = 279 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 278
                self.torsion_angle_restraint_w_segid()
                self.state = 281 
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
            self.state = 283
            self.match(PalesMRParser.Integer)
            self.state = 284
            self.match(PalesMRParser.Simple_name)
            self.state = 285
            self.match(PalesMRParser.Integer)
            self.state = 286
            self.match(PalesMRParser.Simple_name)
            self.state = 287
            self.match(PalesMRParser.Simple_name)
            self.state = 288
            self.match(PalesMRParser.Simple_name)
            self.state = 289
            self.match(PalesMRParser.Integer)
            self.state = 290
            self.match(PalesMRParser.Simple_name)
            self.state = 291
            self.match(PalesMRParser.Simple_name)
            self.state = 292
            self.match(PalesMRParser.Simple_name)
            self.state = 293
            self.match(PalesMRParser.Integer)
            self.state = 294
            self.match(PalesMRParser.Simple_name)
            self.state = 295
            self.match(PalesMRParser.Simple_name)
            self.state = 296
            self.match(PalesMRParser.Simple_name)
            self.state = 297
            self.match(PalesMRParser.Integer)
            self.state = 298
            self.match(PalesMRParser.Simple_name)
            self.state = 299
            self.match(PalesMRParser.Simple_name)
            self.state = 300
            self.number()
            self.state = 301
            self.number()
            self.state = 302
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
            self.state = 304
            self.match(PalesMRParser.Vars)
            self.state = 305
            self.match(PalesMRParser.Resid_I)
            self.state = 306
            self.match(PalesMRParser.Resname_I)
            self.state = 307
            self.match(PalesMRParser.Atomname_I)
            self.state = 308
            self.match(PalesMRParser.Resid_J)
            self.state = 309
            self.match(PalesMRParser.Resname_J)
            self.state = 310
            self.match(PalesMRParser.Atomname_J)
            self.state = 311
            self.match(PalesMRParser.D)
            self.state = 312
            self.match(PalesMRParser.DD)
            self.state = 313
            self.match(PalesMRParser.W)
            self.state = 314
            self.match(PalesMRParser.RETURN_V)
            self.state = 315
            self.match(PalesMRParser.Format)
            self.state = 316
            self.match(PalesMRParser.Format_code)
            self.state = 317
            self.match(PalesMRParser.Format_code)
            self.state = 318
            self.match(PalesMRParser.Format_code)
            self.state = 319
            self.match(PalesMRParser.Format_code)
            self.state = 320
            self.match(PalesMRParser.Format_code)
            self.state = 321
            self.match(PalesMRParser.Format_code)
            self.state = 322
            self.match(PalesMRParser.Format_code)
            self.state = 323
            self.match(PalesMRParser.Format_code)
            self.state = 324
            self.match(PalesMRParser.Format_code)
            self.state = 325
            self.match(PalesMRParser.RETURN_F)
            self.state = 327 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 326
                self.rdc_restraint()
                self.state = 329 
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
            self.state = 331
            self.match(PalesMRParser.Integer)
            self.state = 332
            self.match(PalesMRParser.Simple_name)
            self.state = 333
            self.match(PalesMRParser.Simple_name)
            self.state = 334
            self.match(PalesMRParser.Integer)
            self.state = 335
            self.match(PalesMRParser.Simple_name)
            self.state = 336
            self.match(PalesMRParser.Simple_name)
            self.state = 337
            self.number()
            self.state = 338
            self.number()
            self.state = 339
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
            self.state = 341
            self.match(PalesMRParser.Vars)
            self.state = 342
            self.match(PalesMRParser.Segname_I)
            self.state = 343
            self.match(PalesMRParser.Resid_I)
            self.state = 344
            self.match(PalesMRParser.Resname_I)
            self.state = 345
            self.match(PalesMRParser.Atomname_I)
            self.state = 346
            self.match(PalesMRParser.Segname_J)
            self.state = 347
            self.match(PalesMRParser.Resid_J)
            self.state = 348
            self.match(PalesMRParser.Resname_J)
            self.state = 349
            self.match(PalesMRParser.Atomname_J)
            self.state = 350
            self.match(PalesMRParser.D)
            self.state = 351
            self.match(PalesMRParser.DD)
            self.state = 352
            self.match(PalesMRParser.W)
            self.state = 353
            self.match(PalesMRParser.RETURN_V)
            self.state = 354
            self.match(PalesMRParser.Format)
            self.state = 355
            self.match(PalesMRParser.Format_code)
            self.state = 356
            self.match(PalesMRParser.Format_code)
            self.state = 357
            self.match(PalesMRParser.Format_code)
            self.state = 358
            self.match(PalesMRParser.Format_code)
            self.state = 359
            self.match(PalesMRParser.Format_code)
            self.state = 360
            self.match(PalesMRParser.Format_code)
            self.state = 361
            self.match(PalesMRParser.Format_code)
            self.state = 362
            self.match(PalesMRParser.Format_code)
            self.state = 363
            self.match(PalesMRParser.Format_code)
            self.state = 364
            self.match(PalesMRParser.Format_code)
            self.state = 365
            self.match(PalesMRParser.Format_code)
            self.state = 366
            self.match(PalesMRParser.RETURN_F)
            self.state = 368 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 367
                self.rdc_restraint_w_segid()
                self.state = 370 
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
            self.state = 372
            self.match(PalesMRParser.Simple_name)
            self.state = 373
            self.match(PalesMRParser.Integer)
            self.state = 374
            self.match(PalesMRParser.Simple_name)
            self.state = 375
            self.match(PalesMRParser.Simple_name)
            self.state = 376
            self.match(PalesMRParser.Simple_name)
            self.state = 377
            self.match(PalesMRParser.Integer)
            self.state = 378
            self.match(PalesMRParser.Simple_name)
            self.state = 379
            self.match(PalesMRParser.Simple_name)
            self.state = 380
            self.number()
            self.state = 381
            self.number()
            self.state = 382
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
            self.state = 384
            self.match(PalesMRParser.Vars)
            self.state = 385
            self.match(PalesMRParser.Index)
            self.state = 386
            self.match(PalesMRParser.Resid_I)
            self.state = 387
            self.match(PalesMRParser.Resname_I)
            self.state = 388
            self.match(PalesMRParser.Atomname_I)
            self.state = 389
            self.match(PalesMRParser.Resid_J)
            self.state = 390
            self.match(PalesMRParser.Resname_J)
            self.state = 391
            self.match(PalesMRParser.Atomname_J)
            self.state = 392
            self.match(PalesMRParser.Resid_K)
            self.state = 393
            self.match(PalesMRParser.Resname_K)
            self.state = 394
            self.match(PalesMRParser.Atomname_K)
            self.state = 395
            self.match(PalesMRParser.Resid_L)
            self.state = 396
            self.match(PalesMRParser.Resname_L)
            self.state = 397
            self.match(PalesMRParser.Atomname_L)
            self.state = 398
            self.match(PalesMRParser.A)
            self.state = 399
            self.match(PalesMRParser.B)
            self.state = 400
            self.match(PalesMRParser.C)
            self.state = 401
            self.match(PalesMRParser.Phase)
            self.state = 402
            self.match(PalesMRParser.ObsJ)
            self.state = 403
            self.match(PalesMRParser.FC)
            self.state = 404
            self.match(PalesMRParser.RETURN_V)
            self.state = 405
            self.match(PalesMRParser.Format)
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
            self.match(PalesMRParser.Format_code)
            self.state = 417
            self.match(PalesMRParser.Format_code)
            self.state = 418
            self.match(PalesMRParser.Format_code)
            self.state = 419
            self.match(PalesMRParser.Format_code)
            self.state = 420
            self.match(PalesMRParser.Format_code)
            self.state = 421
            self.match(PalesMRParser.Format_code)
            self.state = 422
            self.match(PalesMRParser.Format_code)
            self.state = 423
            self.match(PalesMRParser.Format_code)
            self.state = 424
            self.match(PalesMRParser.Format_code)
            self.state = 425
            self.match(PalesMRParser.RETURN_F)
            self.state = 427 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 426
                self.coupling_restraint()
                self.state = 429 
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
            self.state = 431
            self.match(PalesMRParser.Integer)
            self.state = 432
            self.match(PalesMRParser.Integer)
            self.state = 433
            self.match(PalesMRParser.Simple_name)
            self.state = 434
            self.match(PalesMRParser.Simple_name)
            self.state = 435
            self.match(PalesMRParser.Integer)
            self.state = 436
            self.match(PalesMRParser.Simple_name)
            self.state = 437
            self.match(PalesMRParser.Simple_name)
            self.state = 438
            self.match(PalesMRParser.Integer)
            self.state = 439
            self.match(PalesMRParser.Simple_name)
            self.state = 440
            self.match(PalesMRParser.Simple_name)
            self.state = 441
            self.match(PalesMRParser.Integer)
            self.state = 442
            self.match(PalesMRParser.Simple_name)
            self.state = 443
            self.match(PalesMRParser.Simple_name)
            self.state = 444
            self.number()
            self.state = 445
            self.number()
            self.state = 446
            self.number()
            self.state = 447
            self.number()
            self.state = 448
            self.number()
            self.state = 449
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
            self.state = 451
            self.match(PalesMRParser.Vars)
            self.state = 452
            self.match(PalesMRParser.Index)
            self.state = 453
            self.match(PalesMRParser.Segname_I)
            self.state = 454
            self.match(PalesMRParser.Resid_I)
            self.state = 455
            self.match(PalesMRParser.Resname_I)
            self.state = 456
            self.match(PalesMRParser.Atomname_I)
            self.state = 457
            self.match(PalesMRParser.Segname_J)
            self.state = 458
            self.match(PalesMRParser.Resid_J)
            self.state = 459
            self.match(PalesMRParser.Resname_J)
            self.state = 460
            self.match(PalesMRParser.Atomname_J)
            self.state = 461
            self.match(PalesMRParser.Segname_K)
            self.state = 462
            self.match(PalesMRParser.Resid_K)
            self.state = 463
            self.match(PalesMRParser.Resname_K)
            self.state = 464
            self.match(PalesMRParser.Atomname_K)
            self.state = 465
            self.match(PalesMRParser.Segname_L)
            self.state = 466
            self.match(PalesMRParser.Resid_L)
            self.state = 467
            self.match(PalesMRParser.Resname_L)
            self.state = 468
            self.match(PalesMRParser.Atomname_L)
            self.state = 469
            self.match(PalesMRParser.A)
            self.state = 470
            self.match(PalesMRParser.B)
            self.state = 471
            self.match(PalesMRParser.C)
            self.state = 472
            self.match(PalesMRParser.Phase)
            self.state = 473
            self.match(PalesMRParser.ObsJ)
            self.state = 474
            self.match(PalesMRParser.FC)
            self.state = 475
            self.match(PalesMRParser.RETURN_V)
            self.state = 476
            self.match(PalesMRParser.Format)
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
            self.match(PalesMRParser.Format_code)
            self.state = 492
            self.match(PalesMRParser.Format_code)
            self.state = 493
            self.match(PalesMRParser.Format_code)
            self.state = 494
            self.match(PalesMRParser.Format_code)
            self.state = 495
            self.match(PalesMRParser.Format_code)
            self.state = 496
            self.match(PalesMRParser.Format_code)
            self.state = 497
            self.match(PalesMRParser.Format_code)
            self.state = 498
            self.match(PalesMRParser.Format_code)
            self.state = 499
            self.match(PalesMRParser.Format_code)
            self.state = 500
            self.match(PalesMRParser.RETURN_F)
            self.state = 502 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 501
                self.coupling_restraint_w_segid()
                self.state = 504 
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
            self.state = 506
            self.match(PalesMRParser.Integer)
            self.state = 507
            self.match(PalesMRParser.Simple_name)
            self.state = 508
            self.match(PalesMRParser.Integer)
            self.state = 509
            self.match(PalesMRParser.Simple_name)
            self.state = 510
            self.match(PalesMRParser.Simple_name)
            self.state = 511
            self.match(PalesMRParser.Simple_name)
            self.state = 512
            self.match(PalesMRParser.Integer)
            self.state = 513
            self.match(PalesMRParser.Simple_name)
            self.state = 514
            self.match(PalesMRParser.Simple_name)
            self.state = 515
            self.match(PalesMRParser.Simple_name)
            self.state = 516
            self.match(PalesMRParser.Integer)
            self.state = 517
            self.match(PalesMRParser.Simple_name)
            self.state = 518
            self.match(PalesMRParser.Simple_name)
            self.state = 519
            self.match(PalesMRParser.Simple_name)
            self.state = 520
            self.match(PalesMRParser.Integer)
            self.state = 521
            self.match(PalesMRParser.Simple_name)
            self.state = 522
            self.match(PalesMRParser.Simple_name)
            self.state = 523
            self.number()
            self.state = 524
            self.number()
            self.state = 525
            self.number()
            self.state = 526
            self.number()
            self.state = 527
            self.number()
            self.state = 528
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Talos_restraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Vars(self):
            return self.getToken(PalesMRParser.Vars, 0)

        def Resid(self):
            return self.getToken(PalesMRParser.Resid, 0)

        def Resname(self):
            return self.getToken(PalesMRParser.Resname, 0)

        def Phi(self):
            return self.getToken(PalesMRParser.Phi, 0)

        def Psi(self):
            return self.getToken(PalesMRParser.Psi, 0)

        def Dphi(self):
            return self.getToken(PalesMRParser.Dphi, 0)

        def Dpsi(self):
            return self.getToken(PalesMRParser.Dpsi, 0)

        def Dist(self):
            return self.getToken(PalesMRParser.Dist, 0)

        def S2(self):
            return self.getToken(PalesMRParser.S2, 0)

        def Count(self):
            return self.getToken(PalesMRParser.Count, 0)

        def Cs_count(self):
            return self.getToken(PalesMRParser.Cs_count, 0)

        def Class(self):
            return self.getToken(PalesMRParser.Class, 0)

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

        def talos_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PalesMRParser.Talos_restraintContext)
            else:
                return self.getTypedRuleContext(PalesMRParser.Talos_restraintContext,i)


        def getRuleIndex(self):
            return PalesMRParser.RULE_talos_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTalos_restraints" ):
                listener.enterTalos_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTalos_restraints" ):
                listener.exitTalos_restraints(self)




    def talos_restraints(self):

        localctx = PalesMRParser.Talos_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_talos_restraints)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self.match(PalesMRParser.Vars)
            self.state = 531
            self.match(PalesMRParser.Resid)
            self.state = 532
            self.match(PalesMRParser.Resname)
            self.state = 533
            self.match(PalesMRParser.Phi)
            self.state = 534
            self.match(PalesMRParser.Psi)
            self.state = 535
            self.match(PalesMRParser.Dphi)
            self.state = 536
            self.match(PalesMRParser.Dpsi)
            self.state = 537
            self.match(PalesMRParser.Dist)
            self.state = 538
            self.match(PalesMRParser.S2)
            self.state = 539
            self.match(PalesMRParser.Count)
            self.state = 540
            self.match(PalesMRParser.Cs_count)
            self.state = 541
            self.match(PalesMRParser.Class)
            self.state = 542
            self.match(PalesMRParser.RETURN_V)
            self.state = 543
            self.match(PalesMRParser.Format)
            self.state = 544
            self.match(PalesMRParser.Format_code)
            self.state = 545
            self.match(PalesMRParser.Format_code)
            self.state = 546
            self.match(PalesMRParser.Format_code)
            self.state = 547
            self.match(PalesMRParser.Format_code)
            self.state = 548
            self.match(PalesMRParser.Format_code)
            self.state = 549
            self.match(PalesMRParser.Format_code)
            self.state = 550
            self.match(PalesMRParser.Format_code)
            self.state = 551
            self.match(PalesMRParser.Format_code)
            self.state = 552
            self.match(PalesMRParser.Format_code)
            self.state = 553
            self.match(PalesMRParser.Format_code)
            self.state = 554
            self.match(PalesMRParser.Format_code)
            self.state = 555
            self.match(PalesMRParser.RETURN_F)
            self.state = 557 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 556
                self.talos_restraint()
                self.state = 559 
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


    class Talos_restraintContext(ParserRuleContext):
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
            return PalesMRParser.RULE_talos_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTalos_restraint" ):
                listener.enterTalos_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTalos_restraint" ):
                listener.exitTalos_restraint(self)




    def talos_restraint(self):

        localctx = PalesMRParser.Talos_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_talos_restraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            self.match(PalesMRParser.Integer)
            self.state = 562
            self.match(PalesMRParser.Simple_name)
            self.state = 563
            self.number()
            self.state = 564
            self.number()
            self.state = 565
            self.number()
            self.state = 566
            self.number()
            self.state = 567
            self.number()
            self.state = 568
            self.number()
            self.state = 569
            self.match(PalesMRParser.Integer)
            self.state = 570
            self.match(PalesMRParser.Integer)
            self.state = 571
            self.match(PalesMRParser.Simple_name)
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
        self.enterRule(localctx, 40, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 573
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





