# Generated from NmrPipePKParser.g4 by ANTLR 4.13.0
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
        4,1,88,450,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,3,0,20,8,0,1,0,1,0,1,0,1,0,1,0,5,0,27,8,0,
        10,0,12,0,30,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,67,8,2,1,2,1,2,1,2,3,2,72,8,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,99,8,2,1,2,1,2,1,2,3,2,104,
        8,2,1,2,1,2,1,2,1,2,3,2,110,8,2,1,2,1,2,1,2,3,2,115,8,2,1,2,4,2,
        118,8,2,11,2,12,2,119,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,145,8,3,1,
        3,1,3,1,3,3,3,150,8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,186,8,4,1,4,1,4,1,4,3,4,191,8,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,3,4,226,8,4,1,4,1,4,1,4,3,4,231,8,4,1,4,1,4,1,4,1,4,3,4,237,
        8,4,1,4,1,4,1,4,3,4,242,8,4,1,4,4,4,245,8,4,11,4,12,4,246,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,280,8,
        5,1,5,1,5,1,5,3,5,285,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,3,6,329,8,6,1,6,1,6,1,6,3,6,334,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,3,6,377,8,6,1,6,1,6,1,6,3,6,382,8,6,1,6,1,6,1,6,1,6,3,
        6,388,8,6,1,6,1,6,1,6,3,6,393,8,6,1,6,4,6,396,8,6,11,6,12,6,397,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,439,8,7,1,7,1,7,1,7,3,7,444,8,7,
        1,7,1,7,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,3,1,0,18,21,1,
        1,14,14,2,0,7,8,12,12,473,0,19,1,0,0,0,2,33,1,0,0,0,4,42,1,0,0,0,
        6,121,1,0,0,0,8,153,1,0,0,0,10,248,1,0,0,0,12,288,1,0,0,0,14,399,
        1,0,0,0,16,447,1,0,0,0,18,20,5,14,0,0,19,18,1,0,0,0,19,20,1,0,0,
        0,20,28,1,0,0,0,21,27,3,2,1,0,22,27,3,4,2,0,23,27,3,8,4,0,24,27,
        3,12,6,0,25,27,5,14,0,0,26,21,1,0,0,0,26,22,1,0,0,0,26,23,1,0,0,
        0,26,24,1,0,0,0,26,25,1,0,0,0,27,30,1,0,0,0,28,26,1,0,0,0,28,29,
        1,0,0,0,29,31,1,0,0,0,30,28,1,0,0,0,31,32,5,0,0,1,32,1,1,0,0,0,33,
        34,5,1,0,0,34,35,7,0,0,0,35,36,5,26,0,0,36,37,5,23,0,0,37,38,5,23,
        0,0,38,39,5,22,0,0,39,40,5,22,0,0,40,41,5,28,0,0,41,3,1,0,0,0,42,
        43,5,2,0,0,43,44,5,30,0,0,44,45,5,31,0,0,45,46,5,32,0,0,46,47,5,
        35,0,0,47,48,5,36,0,0,48,49,5,39,0,0,49,50,5,40,0,0,50,51,5,43,0,
        0,51,52,5,44,0,0,52,53,5,47,0,0,53,54,5,48,0,0,54,55,5,51,0,0,55,
        56,5,52,0,0,56,57,5,55,0,0,57,58,5,56,0,0,58,59,5,57,0,0,59,60,5,
        58,0,0,60,61,5,63,0,0,61,62,5,64,0,0,62,63,5,65,0,0,63,64,5,66,0,
        0,64,66,5,67,0,0,65,67,5,68,0,0,66,65,1,0,0,0,66,67,1,0,0,0,67,68,
        1,0,0,0,68,69,5,69,0,0,69,71,5,70,0,0,70,72,5,71,0,0,71,70,1,0,0,
        0,71,72,1,0,0,0,72,73,1,0,0,0,73,74,5,77,0,0,74,75,5,3,0,0,75,76,
        5,79,0,0,76,77,5,79,0,0,77,78,5,79,0,0,78,79,5,79,0,0,79,80,5,79,
        0,0,80,81,5,79,0,0,81,82,5,79,0,0,82,83,5,79,0,0,83,84,5,79,0,0,
        84,85,5,79,0,0,85,86,5,79,0,0,86,87,5,79,0,0,87,88,5,79,0,0,88,89,
        5,79,0,0,89,90,5,79,0,0,90,91,5,79,0,0,91,92,5,79,0,0,92,93,5,79,
        0,0,93,94,5,79,0,0,94,95,5,79,0,0,95,96,5,79,0,0,96,98,5,79,0,0,
        97,99,5,79,0,0,98,97,1,0,0,0,98,99,1,0,0,0,99,100,1,0,0,0,100,101,
        5,79,0,0,101,103,5,79,0,0,102,104,5,79,0,0,103,102,1,0,0,0,103,104,
        1,0,0,0,104,105,1,0,0,0,105,109,5,81,0,0,106,107,5,4,0,0,107,108,
        5,83,0,0,108,110,5,85,0,0,109,106,1,0,0,0,109,110,1,0,0,0,110,114,
        1,0,0,0,111,112,5,5,0,0,112,113,5,86,0,0,113,115,5,88,0,0,114,111,
        1,0,0,0,114,115,1,0,0,0,115,117,1,0,0,0,116,118,3,6,3,0,117,116,
        1,0,0,0,118,119,1,0,0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,5,1,
        0,0,0,121,122,5,6,0,0,122,123,3,16,8,0,123,124,3,16,8,0,124,125,
        3,16,8,0,125,126,3,16,8,0,126,127,3,16,8,0,127,128,3,16,8,0,128,
        129,3,16,8,0,129,130,3,16,8,0,130,131,3,16,8,0,131,132,3,16,8,0,
        132,133,3,16,8,0,133,134,3,16,8,0,134,135,5,6,0,0,135,136,5,6,0,
        0,136,137,5,6,0,0,137,138,5,6,0,0,138,139,3,16,8,0,139,140,3,16,
        8,0,140,141,3,16,8,0,141,142,3,16,8,0,142,144,5,6,0,0,143,145,5,
        12,0,0,144,143,1,0,0,0,144,145,1,0,0,0,145,146,1,0,0,0,146,147,5,
        6,0,0,147,149,5,6,0,0,148,150,5,6,0,0,149,148,1,0,0,0,149,150,1,
        0,0,0,150,151,1,0,0,0,151,152,7,1,0,0,152,7,1,0,0,0,153,154,5,2,
        0,0,154,155,5,30,0,0,155,156,5,31,0,0,156,157,5,32,0,0,157,158,5,
        33,0,0,158,159,5,35,0,0,159,160,5,36,0,0,160,161,5,37,0,0,161,162,
        5,39,0,0,162,163,5,40,0,0,163,164,5,41,0,0,164,165,5,43,0,0,165,
        166,5,44,0,0,166,167,5,45,0,0,167,168,5,47,0,0,168,169,5,48,0,0,
        169,170,5,49,0,0,170,171,5,51,0,0,171,172,5,52,0,0,172,173,5,53,
        0,0,173,174,5,55,0,0,174,175,5,56,0,0,175,176,5,57,0,0,176,177,5,
        58,0,0,177,178,5,59,0,0,178,179,5,60,0,0,179,180,5,63,0,0,180,181,
        5,64,0,0,181,182,5,65,0,0,182,183,5,66,0,0,183,185,5,67,0,0,184,
        186,5,68,0,0,185,184,1,0,0,0,185,186,1,0,0,0,186,187,1,0,0,0,187,
        188,5,69,0,0,188,190,5,70,0,0,189,191,5,71,0,0,190,189,1,0,0,0,190,
        191,1,0,0,0,191,192,1,0,0,0,192,193,5,77,0,0,193,194,5,3,0,0,194,
        195,5,79,0,0,195,196,5,79,0,0,196,197,5,79,0,0,197,198,5,79,0,0,
        198,199,5,79,0,0,199,200,5,79,0,0,200,201,5,79,0,0,201,202,5,79,
        0,0,202,203,5,79,0,0,203,204,5,79,0,0,204,205,5,79,0,0,205,206,5,
        79,0,0,206,207,5,79,0,0,207,208,5,79,0,0,208,209,5,79,0,0,209,210,
        5,79,0,0,210,211,5,79,0,0,211,212,5,79,0,0,212,213,5,79,0,0,213,
        214,5,79,0,0,214,215,5,79,0,0,215,216,5,79,0,0,216,217,5,79,0,0,
        217,218,5,79,0,0,218,219,5,79,0,0,219,220,5,79,0,0,220,221,5,79,
        0,0,221,222,5,79,0,0,222,223,5,79,0,0,223,225,5,79,0,0,224,226,5,
        79,0,0,225,224,1,0,0,0,225,226,1,0,0,0,226,227,1,0,0,0,227,228,5,
        79,0,0,228,230,5,79,0,0,229,231,5,79,0,0,230,229,1,0,0,0,230,231,
        1,0,0,0,231,232,1,0,0,0,232,236,5,81,0,0,233,234,5,4,0,0,234,235,
        5,83,0,0,235,237,5,85,0,0,236,233,1,0,0,0,236,237,1,0,0,0,237,241,
        1,0,0,0,238,239,5,5,0,0,239,240,5,86,0,0,240,242,5,88,0,0,241,238,
        1,0,0,0,241,242,1,0,0,0,242,244,1,0,0,0,243,245,3,10,5,0,244,243,
        1,0,0,0,245,246,1,0,0,0,246,244,1,0,0,0,246,247,1,0,0,0,247,9,1,
        0,0,0,248,249,5,6,0,0,249,250,3,16,8,0,250,251,3,16,8,0,251,252,
        3,16,8,0,252,253,3,16,8,0,253,254,3,16,8,0,254,255,3,16,8,0,255,
        256,3,16,8,0,256,257,3,16,8,0,257,258,3,16,8,0,258,259,3,16,8,0,
        259,260,3,16,8,0,260,261,3,16,8,0,261,262,3,16,8,0,262,263,3,16,
        8,0,263,264,3,16,8,0,264,265,3,16,8,0,265,266,3,16,8,0,266,267,3,
        16,8,0,267,268,5,6,0,0,268,269,5,6,0,0,269,270,5,6,0,0,270,271,5,
        6,0,0,271,272,5,6,0,0,272,273,5,6,0,0,273,274,3,16,8,0,274,275,3,
        16,8,0,275,276,3,16,8,0,276,277,3,16,8,0,277,279,5,6,0,0,278,280,
        5,12,0,0,279,278,1,0,0,0,279,280,1,0,0,0,280,281,1,0,0,0,281,282,
        5,6,0,0,282,284,5,6,0,0,283,285,5,6,0,0,284,283,1,0,0,0,284,285,
        1,0,0,0,285,286,1,0,0,0,286,287,7,1,0,0,287,11,1,0,0,0,288,289,5,
        2,0,0,289,290,5,30,0,0,290,291,5,31,0,0,291,292,5,32,0,0,292,293,
        5,33,0,0,293,294,5,34,0,0,294,295,5,35,0,0,295,296,5,36,0,0,296,
        297,5,37,0,0,297,298,5,37,0,0,298,299,5,39,0,0,299,300,5,40,0,0,
        300,301,5,41,0,0,301,302,5,42,0,0,302,303,5,43,0,0,303,304,5,44,
        0,0,304,305,5,45,0,0,305,306,5,46,0,0,306,307,5,47,0,0,307,308,5,
        48,0,0,308,309,5,49,0,0,309,310,5,50,0,0,310,311,5,51,0,0,311,312,
        5,52,0,0,312,313,5,53,0,0,313,314,5,54,0,0,314,315,5,55,0,0,315,
        316,5,56,0,0,316,317,5,57,0,0,317,318,5,58,0,0,318,319,5,59,0,0,
        319,320,5,60,0,0,320,321,5,61,0,0,321,322,5,62,0,0,322,323,5,63,
        0,0,323,324,5,64,0,0,324,325,5,65,0,0,325,326,5,66,0,0,326,328,5,
        67,0,0,327,329,5,68,0,0,328,327,1,0,0,0,328,329,1,0,0,0,329,330,
        1,0,0,0,330,331,5,69,0,0,331,333,5,70,0,0,332,334,5,71,0,0,333,332,
        1,0,0,0,333,334,1,0,0,0,334,335,1,0,0,0,335,336,5,77,0,0,336,337,
        5,3,0,0,337,338,5,79,0,0,338,339,5,79,0,0,339,340,5,79,0,0,340,341,
        5,79,0,0,341,342,5,79,0,0,342,343,5,79,0,0,343,344,5,79,0,0,344,
        345,5,79,0,0,345,346,5,79,0,0,346,347,5,79,0,0,347,348,5,79,0,0,
        348,349,5,79,0,0,349,350,5,79,0,0,350,351,5,79,0,0,351,352,5,79,
        0,0,352,353,5,79,0,0,353,354,5,79,0,0,354,355,5,79,0,0,355,356,5,
        79,0,0,356,357,5,79,0,0,357,358,5,79,0,0,358,359,5,79,0,0,359,360,
        5,79,0,0,360,361,5,79,0,0,361,362,5,79,0,0,362,363,5,79,0,0,363,
        364,5,79,0,0,364,365,5,79,0,0,365,366,5,79,0,0,366,367,5,79,0,0,
        367,368,5,79,0,0,368,369,5,79,0,0,369,370,5,79,0,0,370,371,5,79,
        0,0,371,372,5,79,0,0,372,373,5,79,0,0,373,374,5,79,0,0,374,376,5,
        79,0,0,375,377,5,79,0,0,376,375,1,0,0,0,376,377,1,0,0,0,377,378,
        1,0,0,0,378,379,5,79,0,0,379,381,5,79,0,0,380,382,5,79,0,0,381,380,
        1,0,0,0,381,382,1,0,0,0,382,383,1,0,0,0,383,387,5,81,0,0,384,385,
        5,4,0,0,385,386,5,83,0,0,386,388,5,85,0,0,387,384,1,0,0,0,387,388,
        1,0,0,0,388,392,1,0,0,0,389,390,5,5,0,0,390,391,5,86,0,0,391,393,
        5,88,0,0,392,389,1,0,0,0,392,393,1,0,0,0,393,395,1,0,0,0,394,396,
        3,14,7,0,395,394,1,0,0,0,396,397,1,0,0,0,397,395,1,0,0,0,397,398,
        1,0,0,0,398,13,1,0,0,0,399,400,5,6,0,0,400,401,3,16,8,0,401,402,
        3,16,8,0,402,403,3,16,8,0,403,404,3,16,8,0,404,405,3,16,8,0,405,
        406,3,16,8,0,406,407,3,16,8,0,407,408,3,16,8,0,408,409,3,16,8,0,
        409,410,3,16,8,0,410,411,3,16,8,0,411,412,3,16,8,0,412,413,3,16,
        8,0,413,414,3,16,8,0,414,415,3,16,8,0,415,416,3,16,8,0,416,417,3,
        16,8,0,417,418,3,16,8,0,418,419,3,16,8,0,419,420,3,16,8,0,420,421,
        3,16,8,0,421,422,3,16,8,0,422,423,3,16,8,0,423,424,3,16,8,0,424,
        425,5,6,0,0,425,426,5,6,0,0,426,427,5,6,0,0,427,428,5,6,0,0,428,
        429,5,6,0,0,429,430,5,6,0,0,430,431,5,6,0,0,431,432,5,6,0,0,432,
        433,3,16,8,0,433,434,3,16,8,0,434,435,3,16,8,0,435,436,3,16,8,0,
        436,438,5,6,0,0,437,439,5,12,0,0,438,437,1,0,0,0,438,439,1,0,0,0,
        439,440,1,0,0,0,440,441,5,6,0,0,441,443,5,6,0,0,442,444,5,6,0,0,
        443,442,1,0,0,0,443,444,1,0,0,0,444,445,1,0,0,0,445,446,7,1,0,0,
        446,15,1,0,0,0,447,448,7,2,0,0,448,17,1,0,0,0,30,19,26,28,66,71,
        98,103,109,114,119,144,149,185,190,225,230,236,241,246,279,284,328,
        333,376,381,387,392,397,438,443
    ]

class NmrPipePKParser ( Parser ):

    grammarFileName = "NmrPipePKParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'DATA'", "'VARS'", "'FORMAT'", "'NULLVALUE'", 
                     "'NULLSTRING'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'INDEX'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'DX'", "'DY'", "'DZ'", "'DA'", "'X_PPM'", 
                     "'Y_PPM'", "'Z_PPM'", "'A_PPM'", "'X_HZ'", "'Y_HZ'", 
                     "'Z_HZ'", "'A_HZ'", "'XW'", "'YW'", "'ZW'", "'AW'", 
                     "'XW_HZ'", "'YW_HZ'", "'ZW_HZ'", "'AW_HZ'", "'X1'", 
                     "'X3'", "'Y1'", "'Y3'", "'Z1'", "'Z3'", "'A1'", "'A3'", 
                     "'HEIGHT'", "'DHEIGHT'", "'VOL'", "'PCHI2'", "'TYPE'", 
                     "'ASS'", "'CLUSTID'", "'MEMCNT'", "'TROUBLE'" ]

    symbolicNames = [ "<INVALID>", "Data", "Vars", "Format", "Null_value", 
                      "Null_string", "Integer", "Float", "Real", "SHARP_COMMENT", 
                      "EXCLM_COMMENT", "SMCLN_COMMENT", "Any_name", "SPACE", 
                      "RETURN", "ENCLOSE_COMMENT", "SECTION_COMMENT", "LINE_COMMENT", 
                      "X_axis_DA", "Y_axis_DA", "Z_axis_DA", "A_axis_DA", 
                      "Ppm_value_DA", "Integer_DA", "Float_DA", "Real_DA", 
                      "Simple_name_DA", "SPACE_DA", "RETURN_DA", "LINE_COMMENT_DA", 
                      "Index", "X_axis", "Y_axis", "Z_axis", "A_axis", "Dx", 
                      "Dy", "Dz", "Da", "X_ppm", "Y_ppm", "Z_ppm", "A_ppm", 
                      "X_hz", "Y_hz", "Z_hz", "A_hz", "Xw", "Yw", "Zw", 
                      "Aw", "Xw_hz", "Yw_hz", "Zw_hz", "Aw_hz", "X1", "X3", 
                      "Y1", "Y3", "Z1", "Z3", "A1", "A3", "Height", "DHeight", 
                      "Vol", "Pchi2", "Type", "Ass", "ClustId", "Memcnt", 
                      "Trouble", "Integer_VA", "Float_VA", "Real_VA", "Simple_name_VA", 
                      "SPACE_VA", "RETURN_VA", "LINE_COMMENT_VA", "Format_code", 
                      "SPACE_FO", "RETURN_FO", "LINE_COMMENT_FO", "Any_name_NV", 
                      "SPACE_NV", "RETURN_NV", "Any_name_NS", "SPACE_NS", 
                      "RETURN_NS" ]

    RULE_nmrpipe_pk = 0
    RULE_data_label = 1
    RULE_peak_list_2d = 2
    RULE_peak_2d = 3
    RULE_peak_list_3d = 4
    RULE_peak_3d = 5
    RULE_peak_list_4d = 6
    RULE_peak_4d = 7
    RULE_number = 8

    ruleNames =  [ "nmrpipe_pk", "data_label", "peak_list_2d", "peak_2d", 
                   "peak_list_3d", "peak_3d", "peak_list_4d", "peak_4d", 
                   "number" ]

    EOF = Token.EOF
    Data=1
    Vars=2
    Format=3
    Null_value=4
    Null_string=5
    Integer=6
    Float=7
    Real=8
    SHARP_COMMENT=9
    EXCLM_COMMENT=10
    SMCLN_COMMENT=11
    Any_name=12
    SPACE=13
    RETURN=14
    ENCLOSE_COMMENT=15
    SECTION_COMMENT=16
    LINE_COMMENT=17
    X_axis_DA=18
    Y_axis_DA=19
    Z_axis_DA=20
    A_axis_DA=21
    Ppm_value_DA=22
    Integer_DA=23
    Float_DA=24
    Real_DA=25
    Simple_name_DA=26
    SPACE_DA=27
    RETURN_DA=28
    LINE_COMMENT_DA=29
    Index=30
    X_axis=31
    Y_axis=32
    Z_axis=33
    A_axis=34
    Dx=35
    Dy=36
    Dz=37
    Da=38
    X_ppm=39
    Y_ppm=40
    Z_ppm=41
    A_ppm=42
    X_hz=43
    Y_hz=44
    Z_hz=45
    A_hz=46
    Xw=47
    Yw=48
    Zw=49
    Aw=50
    Xw_hz=51
    Yw_hz=52
    Zw_hz=53
    Aw_hz=54
    X1=55
    X3=56
    Y1=57
    Y3=58
    Z1=59
    Z3=60
    A1=61
    A3=62
    Height=63
    DHeight=64
    Vol=65
    Pchi2=66
    Type=67
    Ass=68
    ClustId=69
    Memcnt=70
    Trouble=71
    Integer_VA=72
    Float_VA=73
    Real_VA=74
    Simple_name_VA=75
    SPACE_VA=76
    RETURN_VA=77
    LINE_COMMENT_VA=78
    Format_code=79
    SPACE_FO=80
    RETURN_FO=81
    LINE_COMMENT_FO=82
    Any_name_NV=83
    SPACE_NV=84
    RETURN_NV=85
    Any_name_NS=86
    SPACE_NS=87
    RETURN_NS=88

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Nmrpipe_pkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(NmrPipePKParser.EOF, 0)

        def RETURN(self, i:int=None):
            if i is None:
                return self.getTokens(NmrPipePKParser.RETURN)
            else:
                return self.getToken(NmrPipePKParser.RETURN, i)

        def data_label(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmrPipePKParser.Data_labelContext)
            else:
                return self.getTypedRuleContext(NmrPipePKParser.Data_labelContext,i)


        def peak_list_2d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmrPipePKParser.Peak_list_2dContext)
            else:
                return self.getTypedRuleContext(NmrPipePKParser.Peak_list_2dContext,i)


        def peak_list_3d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmrPipePKParser.Peak_list_3dContext)
            else:
                return self.getTypedRuleContext(NmrPipePKParser.Peak_list_3dContext,i)


        def peak_list_4d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmrPipePKParser.Peak_list_4dContext)
            else:
                return self.getTypedRuleContext(NmrPipePKParser.Peak_list_4dContext,i)


        def getRuleIndex(self):
            return NmrPipePKParser.RULE_nmrpipe_pk

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNmrpipe_pk" ):
                listener.enterNmrpipe_pk(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNmrpipe_pk" ):
                listener.exitNmrpipe_pk(self)




    def nmrpipe_pk(self):

        localctx = NmrPipePKParser.Nmrpipe_pkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_nmrpipe_pk)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 18
                self.match(NmrPipePKParser.RETURN)


            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16390) != 0):
                self.state = 26
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 21
                    self.data_label()
                    pass

                elif la_ == 2:
                    self.state = 22
                    self.peak_list_2d()
                    pass

                elif la_ == 3:
                    self.state = 23
                    self.peak_list_3d()
                    pass

                elif la_ == 4:
                    self.state = 24
                    self.peak_list_4d()
                    pass

                elif la_ == 5:
                    self.state = 25
                    self.match(NmrPipePKParser.RETURN)
                    pass


                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 31
            self.match(NmrPipePKParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_labelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Data(self):
            return self.getToken(NmrPipePKParser.Data, 0)

        def Simple_name_DA(self):
            return self.getToken(NmrPipePKParser.Simple_name_DA, 0)

        def Integer_DA(self, i:int=None):
            if i is None:
                return self.getTokens(NmrPipePKParser.Integer_DA)
            else:
                return self.getToken(NmrPipePKParser.Integer_DA, i)

        def Ppm_value_DA(self, i:int=None):
            if i is None:
                return self.getTokens(NmrPipePKParser.Ppm_value_DA)
            else:
                return self.getToken(NmrPipePKParser.Ppm_value_DA, i)

        def RETURN_DA(self):
            return self.getToken(NmrPipePKParser.RETURN_DA, 0)

        def X_axis_DA(self):
            return self.getToken(NmrPipePKParser.X_axis_DA, 0)

        def Y_axis_DA(self):
            return self.getToken(NmrPipePKParser.Y_axis_DA, 0)

        def Z_axis_DA(self):
            return self.getToken(NmrPipePKParser.Z_axis_DA, 0)

        def A_axis_DA(self):
            return self.getToken(NmrPipePKParser.A_axis_DA, 0)

        def getRuleIndex(self):
            return NmrPipePKParser.RULE_data_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_label" ):
                listener.enterData_label(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_label" ):
                listener.exitData_label(self)




    def data_label(self):

        localctx = NmrPipePKParser.Data_labelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_data_label)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(NmrPipePKParser.Data)
            self.state = 34
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3932160) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 35
            self.match(NmrPipePKParser.Simple_name_DA)
            self.state = 36
            self.match(NmrPipePKParser.Integer_DA)
            self.state = 37
            self.match(NmrPipePKParser.Integer_DA)
            self.state = 38
            self.match(NmrPipePKParser.Ppm_value_DA)
            self.state = 39
            self.match(NmrPipePKParser.Ppm_value_DA)
            self.state = 40
            self.match(NmrPipePKParser.RETURN_DA)
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

        def Vars(self):
            return self.getToken(NmrPipePKParser.Vars, 0)

        def Index(self):
            return self.getToken(NmrPipePKParser.Index, 0)

        def X_axis(self):
            return self.getToken(NmrPipePKParser.X_axis, 0)

        def Y_axis(self):
            return self.getToken(NmrPipePKParser.Y_axis, 0)

        def Dx(self):
            return self.getToken(NmrPipePKParser.Dx, 0)

        def Dy(self):
            return self.getToken(NmrPipePKParser.Dy, 0)

        def X_ppm(self):
            return self.getToken(NmrPipePKParser.X_ppm, 0)

        def Y_ppm(self):
            return self.getToken(NmrPipePKParser.Y_ppm, 0)

        def X_hz(self):
            return self.getToken(NmrPipePKParser.X_hz, 0)

        def Y_hz(self):
            return self.getToken(NmrPipePKParser.Y_hz, 0)

        def Xw(self):
            return self.getToken(NmrPipePKParser.Xw, 0)

        def Yw(self):
            return self.getToken(NmrPipePKParser.Yw, 0)

        def Xw_hz(self):
            return self.getToken(NmrPipePKParser.Xw_hz, 0)

        def Yw_hz(self):
            return self.getToken(NmrPipePKParser.Yw_hz, 0)

        def X1(self):
            return self.getToken(NmrPipePKParser.X1, 0)

        def X3(self):
            return self.getToken(NmrPipePKParser.X3, 0)

        def Y1(self):
            return self.getToken(NmrPipePKParser.Y1, 0)

        def Y3(self):
            return self.getToken(NmrPipePKParser.Y3, 0)

        def Height(self):
            return self.getToken(NmrPipePKParser.Height, 0)

        def DHeight(self):
            return self.getToken(NmrPipePKParser.DHeight, 0)

        def Vol(self):
            return self.getToken(NmrPipePKParser.Vol, 0)

        def Pchi2(self):
            return self.getToken(NmrPipePKParser.Pchi2, 0)

        def Type(self):
            return self.getToken(NmrPipePKParser.Type, 0)

        def ClustId(self):
            return self.getToken(NmrPipePKParser.ClustId, 0)

        def Memcnt(self):
            return self.getToken(NmrPipePKParser.Memcnt, 0)

        def RETURN_VA(self):
            return self.getToken(NmrPipePKParser.RETURN_VA, 0)

        def Format(self):
            return self.getToken(NmrPipePKParser.Format, 0)

        def Format_code(self, i:int=None):
            if i is None:
                return self.getTokens(NmrPipePKParser.Format_code)
            else:
                return self.getToken(NmrPipePKParser.Format_code, i)

        def RETURN_FO(self):
            return self.getToken(NmrPipePKParser.RETURN_FO, 0)

        def Ass(self):
            return self.getToken(NmrPipePKParser.Ass, 0)

        def Trouble(self):
            return self.getToken(NmrPipePKParser.Trouble, 0)

        def Null_value(self):
            return self.getToken(NmrPipePKParser.Null_value, 0)

        def Any_name_NV(self):
            return self.getToken(NmrPipePKParser.Any_name_NV, 0)

        def RETURN_NV(self):
            return self.getToken(NmrPipePKParser.RETURN_NV, 0)

        def Null_string(self):
            return self.getToken(NmrPipePKParser.Null_string, 0)

        def Any_name_NS(self):
            return self.getToken(NmrPipePKParser.Any_name_NS, 0)

        def RETURN_NS(self):
            return self.getToken(NmrPipePKParser.RETURN_NS, 0)

        def peak_2d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmrPipePKParser.Peak_2dContext)
            else:
                return self.getTypedRuleContext(NmrPipePKParser.Peak_2dContext,i)


        def getRuleIndex(self):
            return NmrPipePKParser.RULE_peak_list_2d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_list_2d" ):
                listener.enterPeak_list_2d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_list_2d" ):
                listener.exitPeak_list_2d(self)




    def peak_list_2d(self):

        localctx = NmrPipePKParser.Peak_list_2dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_peak_list_2d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(NmrPipePKParser.Vars)
            self.state = 43
            self.match(NmrPipePKParser.Index)
            self.state = 44
            self.match(NmrPipePKParser.X_axis)
            self.state = 45
            self.match(NmrPipePKParser.Y_axis)
            self.state = 46
            self.match(NmrPipePKParser.Dx)
            self.state = 47
            self.match(NmrPipePKParser.Dy)
            self.state = 48
            self.match(NmrPipePKParser.X_ppm)
            self.state = 49
            self.match(NmrPipePKParser.Y_ppm)
            self.state = 50
            self.match(NmrPipePKParser.X_hz)
            self.state = 51
            self.match(NmrPipePKParser.Y_hz)
            self.state = 52
            self.match(NmrPipePKParser.Xw)
            self.state = 53
            self.match(NmrPipePKParser.Yw)
            self.state = 54
            self.match(NmrPipePKParser.Xw_hz)
            self.state = 55
            self.match(NmrPipePKParser.Yw_hz)
            self.state = 56
            self.match(NmrPipePKParser.X1)
            self.state = 57
            self.match(NmrPipePKParser.X3)
            self.state = 58
            self.match(NmrPipePKParser.Y1)
            self.state = 59
            self.match(NmrPipePKParser.Y3)
            self.state = 60
            self.match(NmrPipePKParser.Height)
            self.state = 61
            self.match(NmrPipePKParser.DHeight)
            self.state = 62
            self.match(NmrPipePKParser.Vol)
            self.state = 63
            self.match(NmrPipePKParser.Pchi2)
            self.state = 64
            self.match(NmrPipePKParser.Type)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==68:
                self.state = 65
                self.match(NmrPipePKParser.Ass)


            self.state = 68
            self.match(NmrPipePKParser.ClustId)
            self.state = 69
            self.match(NmrPipePKParser.Memcnt)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==71:
                self.state = 70
                self.match(NmrPipePKParser.Trouble)


            self.state = 73
            self.match(NmrPipePKParser.RETURN_VA)
            self.state = 74
            self.match(NmrPipePKParser.Format)
            self.state = 75
            self.match(NmrPipePKParser.Format_code)
            self.state = 76
            self.match(NmrPipePKParser.Format_code)
            self.state = 77
            self.match(NmrPipePKParser.Format_code)
            self.state = 78
            self.match(NmrPipePKParser.Format_code)
            self.state = 79
            self.match(NmrPipePKParser.Format_code)
            self.state = 80
            self.match(NmrPipePKParser.Format_code)
            self.state = 81
            self.match(NmrPipePKParser.Format_code)
            self.state = 82
            self.match(NmrPipePKParser.Format_code)
            self.state = 83
            self.match(NmrPipePKParser.Format_code)
            self.state = 84
            self.match(NmrPipePKParser.Format_code)
            self.state = 85
            self.match(NmrPipePKParser.Format_code)
            self.state = 86
            self.match(NmrPipePKParser.Format_code)
            self.state = 87
            self.match(NmrPipePKParser.Format_code)
            self.state = 88
            self.match(NmrPipePKParser.Format_code)
            self.state = 89
            self.match(NmrPipePKParser.Format_code)
            self.state = 90
            self.match(NmrPipePKParser.Format_code)
            self.state = 91
            self.match(NmrPipePKParser.Format_code)
            self.state = 92
            self.match(NmrPipePKParser.Format_code)
            self.state = 93
            self.match(NmrPipePKParser.Format_code)
            self.state = 94
            self.match(NmrPipePKParser.Format_code)
            self.state = 95
            self.match(NmrPipePKParser.Format_code)
            self.state = 96
            self.match(NmrPipePKParser.Format_code)
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 97
                self.match(NmrPipePKParser.Format_code)


            self.state = 100
            self.match(NmrPipePKParser.Format_code)
            self.state = 101
            self.match(NmrPipePKParser.Format_code)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==79:
                self.state = 102
                self.match(NmrPipePKParser.Format_code)


            self.state = 105
            self.match(NmrPipePKParser.RETURN_FO)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 106
                self.match(NmrPipePKParser.Null_value)
                self.state = 107
                self.match(NmrPipePKParser.Any_name_NV)
                self.state = 108
                self.match(NmrPipePKParser.RETURN_NV)


            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 111
                self.match(NmrPipePKParser.Null_string)
                self.state = 112
                self.match(NmrPipePKParser.Any_name_NS)
                self.state = 113
                self.match(NmrPipePKParser.RETURN_NS)


            self.state = 117 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 116
                self.peak_2d()
                self.state = 119 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==6):
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

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(NmrPipePKParser.Integer)
            else:
                return self.getToken(NmrPipePKParser.Integer, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmrPipePKParser.NumberContext)
            else:
                return self.getTypedRuleContext(NmrPipePKParser.NumberContext,i)


        def RETURN(self):
            return self.getToken(NmrPipePKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(NmrPipePKParser.EOF, 0)

        def Any_name(self):
            return self.getToken(NmrPipePKParser.Any_name, 0)

        def getRuleIndex(self):
            return NmrPipePKParser.RULE_peak_2d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_2d" ):
                listener.enterPeak_2d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_2d" ):
                listener.exitPeak_2d(self)




    def peak_2d(self):

        localctx = NmrPipePKParser.Peak_2dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_peak_2d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(NmrPipePKParser.Integer)
            self.state = 122
            self.number()
            self.state = 123
            self.number()
            self.state = 124
            self.number()
            self.state = 125
            self.number()
            self.state = 126
            self.number()
            self.state = 127
            self.number()
            self.state = 128
            self.number()
            self.state = 129
            self.number()
            self.state = 130
            self.number()
            self.state = 131
            self.number()
            self.state = 132
            self.number()
            self.state = 133
            self.number()
            self.state = 134
            self.match(NmrPipePKParser.Integer)
            self.state = 135
            self.match(NmrPipePKParser.Integer)
            self.state = 136
            self.match(NmrPipePKParser.Integer)
            self.state = 137
            self.match(NmrPipePKParser.Integer)
            self.state = 138
            self.number()
            self.state = 139
            self.number()
            self.state = 140
            self.number()
            self.state = 141
            self.number()
            self.state = 142
            self.match(NmrPipePKParser.Integer)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 143
                self.match(NmrPipePKParser.Any_name)


            self.state = 146
            self.match(NmrPipePKParser.Integer)
            self.state = 147
            self.match(NmrPipePKParser.Integer)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 148
                self.match(NmrPipePKParser.Integer)


            self.state = 151
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

        def Vars(self):
            return self.getToken(NmrPipePKParser.Vars, 0)

        def Index(self):
            return self.getToken(NmrPipePKParser.Index, 0)

        def X_axis(self):
            return self.getToken(NmrPipePKParser.X_axis, 0)

        def Y_axis(self):
            return self.getToken(NmrPipePKParser.Y_axis, 0)

        def Z_axis(self):
            return self.getToken(NmrPipePKParser.Z_axis, 0)

        def Dx(self):
            return self.getToken(NmrPipePKParser.Dx, 0)

        def Dy(self):
            return self.getToken(NmrPipePKParser.Dy, 0)

        def Dz(self):
            return self.getToken(NmrPipePKParser.Dz, 0)

        def X_ppm(self):
            return self.getToken(NmrPipePKParser.X_ppm, 0)

        def Y_ppm(self):
            return self.getToken(NmrPipePKParser.Y_ppm, 0)

        def Z_ppm(self):
            return self.getToken(NmrPipePKParser.Z_ppm, 0)

        def X_hz(self):
            return self.getToken(NmrPipePKParser.X_hz, 0)

        def Y_hz(self):
            return self.getToken(NmrPipePKParser.Y_hz, 0)

        def Z_hz(self):
            return self.getToken(NmrPipePKParser.Z_hz, 0)

        def Xw(self):
            return self.getToken(NmrPipePKParser.Xw, 0)

        def Yw(self):
            return self.getToken(NmrPipePKParser.Yw, 0)

        def Zw(self):
            return self.getToken(NmrPipePKParser.Zw, 0)

        def Xw_hz(self):
            return self.getToken(NmrPipePKParser.Xw_hz, 0)

        def Yw_hz(self):
            return self.getToken(NmrPipePKParser.Yw_hz, 0)

        def Zw_hz(self):
            return self.getToken(NmrPipePKParser.Zw_hz, 0)

        def X1(self):
            return self.getToken(NmrPipePKParser.X1, 0)

        def X3(self):
            return self.getToken(NmrPipePKParser.X3, 0)

        def Y1(self):
            return self.getToken(NmrPipePKParser.Y1, 0)

        def Y3(self):
            return self.getToken(NmrPipePKParser.Y3, 0)

        def Z1(self):
            return self.getToken(NmrPipePKParser.Z1, 0)

        def Z3(self):
            return self.getToken(NmrPipePKParser.Z3, 0)

        def Height(self):
            return self.getToken(NmrPipePKParser.Height, 0)

        def DHeight(self):
            return self.getToken(NmrPipePKParser.DHeight, 0)

        def Vol(self):
            return self.getToken(NmrPipePKParser.Vol, 0)

        def Pchi2(self):
            return self.getToken(NmrPipePKParser.Pchi2, 0)

        def Type(self):
            return self.getToken(NmrPipePKParser.Type, 0)

        def ClustId(self):
            return self.getToken(NmrPipePKParser.ClustId, 0)

        def Memcnt(self):
            return self.getToken(NmrPipePKParser.Memcnt, 0)

        def RETURN_VA(self):
            return self.getToken(NmrPipePKParser.RETURN_VA, 0)

        def Format(self):
            return self.getToken(NmrPipePKParser.Format, 0)

        def Format_code(self, i:int=None):
            if i is None:
                return self.getTokens(NmrPipePKParser.Format_code)
            else:
                return self.getToken(NmrPipePKParser.Format_code, i)

        def RETURN_FO(self):
            return self.getToken(NmrPipePKParser.RETURN_FO, 0)

        def Ass(self):
            return self.getToken(NmrPipePKParser.Ass, 0)

        def Trouble(self):
            return self.getToken(NmrPipePKParser.Trouble, 0)

        def Null_value(self):
            return self.getToken(NmrPipePKParser.Null_value, 0)

        def Any_name_NV(self):
            return self.getToken(NmrPipePKParser.Any_name_NV, 0)

        def RETURN_NV(self):
            return self.getToken(NmrPipePKParser.RETURN_NV, 0)

        def Null_string(self):
            return self.getToken(NmrPipePKParser.Null_string, 0)

        def Any_name_NS(self):
            return self.getToken(NmrPipePKParser.Any_name_NS, 0)

        def RETURN_NS(self):
            return self.getToken(NmrPipePKParser.RETURN_NS, 0)

        def peak_3d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmrPipePKParser.Peak_3dContext)
            else:
                return self.getTypedRuleContext(NmrPipePKParser.Peak_3dContext,i)


        def getRuleIndex(self):
            return NmrPipePKParser.RULE_peak_list_3d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_list_3d" ):
                listener.enterPeak_list_3d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_list_3d" ):
                listener.exitPeak_list_3d(self)




    def peak_list_3d(self):

        localctx = NmrPipePKParser.Peak_list_3dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_peak_list_3d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(NmrPipePKParser.Vars)
            self.state = 154
            self.match(NmrPipePKParser.Index)
            self.state = 155
            self.match(NmrPipePKParser.X_axis)
            self.state = 156
            self.match(NmrPipePKParser.Y_axis)
            self.state = 157
            self.match(NmrPipePKParser.Z_axis)
            self.state = 158
            self.match(NmrPipePKParser.Dx)
            self.state = 159
            self.match(NmrPipePKParser.Dy)
            self.state = 160
            self.match(NmrPipePKParser.Dz)
            self.state = 161
            self.match(NmrPipePKParser.X_ppm)
            self.state = 162
            self.match(NmrPipePKParser.Y_ppm)
            self.state = 163
            self.match(NmrPipePKParser.Z_ppm)
            self.state = 164
            self.match(NmrPipePKParser.X_hz)
            self.state = 165
            self.match(NmrPipePKParser.Y_hz)
            self.state = 166
            self.match(NmrPipePKParser.Z_hz)
            self.state = 167
            self.match(NmrPipePKParser.Xw)
            self.state = 168
            self.match(NmrPipePKParser.Yw)
            self.state = 169
            self.match(NmrPipePKParser.Zw)
            self.state = 170
            self.match(NmrPipePKParser.Xw_hz)
            self.state = 171
            self.match(NmrPipePKParser.Yw_hz)
            self.state = 172
            self.match(NmrPipePKParser.Zw_hz)
            self.state = 173
            self.match(NmrPipePKParser.X1)
            self.state = 174
            self.match(NmrPipePKParser.X3)
            self.state = 175
            self.match(NmrPipePKParser.Y1)
            self.state = 176
            self.match(NmrPipePKParser.Y3)
            self.state = 177
            self.match(NmrPipePKParser.Z1)
            self.state = 178
            self.match(NmrPipePKParser.Z3)
            self.state = 179
            self.match(NmrPipePKParser.Height)
            self.state = 180
            self.match(NmrPipePKParser.DHeight)
            self.state = 181
            self.match(NmrPipePKParser.Vol)
            self.state = 182
            self.match(NmrPipePKParser.Pchi2)
            self.state = 183
            self.match(NmrPipePKParser.Type)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==68:
                self.state = 184
                self.match(NmrPipePKParser.Ass)


            self.state = 187
            self.match(NmrPipePKParser.ClustId)
            self.state = 188
            self.match(NmrPipePKParser.Memcnt)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==71:
                self.state = 189
                self.match(NmrPipePKParser.Trouble)


            self.state = 192
            self.match(NmrPipePKParser.RETURN_VA)
            self.state = 193
            self.match(NmrPipePKParser.Format)
            self.state = 194
            self.match(NmrPipePKParser.Format_code)
            self.state = 195
            self.match(NmrPipePKParser.Format_code)
            self.state = 196
            self.match(NmrPipePKParser.Format_code)
            self.state = 197
            self.match(NmrPipePKParser.Format_code)
            self.state = 198
            self.match(NmrPipePKParser.Format_code)
            self.state = 199
            self.match(NmrPipePKParser.Format_code)
            self.state = 200
            self.match(NmrPipePKParser.Format_code)
            self.state = 201
            self.match(NmrPipePKParser.Format_code)
            self.state = 202
            self.match(NmrPipePKParser.Format_code)
            self.state = 203
            self.match(NmrPipePKParser.Format_code)
            self.state = 204
            self.match(NmrPipePKParser.Format_code)
            self.state = 205
            self.match(NmrPipePKParser.Format_code)
            self.state = 206
            self.match(NmrPipePKParser.Format_code)
            self.state = 207
            self.match(NmrPipePKParser.Format_code)
            self.state = 208
            self.match(NmrPipePKParser.Format_code)
            self.state = 209
            self.match(NmrPipePKParser.Format_code)
            self.state = 210
            self.match(NmrPipePKParser.Format_code)
            self.state = 211
            self.match(NmrPipePKParser.Format_code)
            self.state = 212
            self.match(NmrPipePKParser.Format_code)
            self.state = 213
            self.match(NmrPipePKParser.Format_code)
            self.state = 214
            self.match(NmrPipePKParser.Format_code)
            self.state = 215
            self.match(NmrPipePKParser.Format_code)
            self.state = 216
            self.match(NmrPipePKParser.Format_code)
            self.state = 217
            self.match(NmrPipePKParser.Format_code)
            self.state = 218
            self.match(NmrPipePKParser.Format_code)
            self.state = 219
            self.match(NmrPipePKParser.Format_code)
            self.state = 220
            self.match(NmrPipePKParser.Format_code)
            self.state = 221
            self.match(NmrPipePKParser.Format_code)
            self.state = 222
            self.match(NmrPipePKParser.Format_code)
            self.state = 223
            self.match(NmrPipePKParser.Format_code)
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 224
                self.match(NmrPipePKParser.Format_code)


            self.state = 227
            self.match(NmrPipePKParser.Format_code)
            self.state = 228
            self.match(NmrPipePKParser.Format_code)
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==79:
                self.state = 229
                self.match(NmrPipePKParser.Format_code)


            self.state = 232
            self.match(NmrPipePKParser.RETURN_FO)
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 233
                self.match(NmrPipePKParser.Null_value)
                self.state = 234
                self.match(NmrPipePKParser.Any_name_NV)
                self.state = 235
                self.match(NmrPipePKParser.RETURN_NV)


            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 238
                self.match(NmrPipePKParser.Null_string)
                self.state = 239
                self.match(NmrPipePKParser.Any_name_NS)
                self.state = 240
                self.match(NmrPipePKParser.RETURN_NS)


            self.state = 244 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 243
                self.peak_3d()
                self.state = 246 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==6):
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

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(NmrPipePKParser.Integer)
            else:
                return self.getToken(NmrPipePKParser.Integer, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmrPipePKParser.NumberContext)
            else:
                return self.getTypedRuleContext(NmrPipePKParser.NumberContext,i)


        def RETURN(self):
            return self.getToken(NmrPipePKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(NmrPipePKParser.EOF, 0)

        def Any_name(self):
            return self.getToken(NmrPipePKParser.Any_name, 0)

        def getRuleIndex(self):
            return NmrPipePKParser.RULE_peak_3d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_3d" ):
                listener.enterPeak_3d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_3d" ):
                listener.exitPeak_3d(self)




    def peak_3d(self):

        localctx = NmrPipePKParser.Peak_3dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_peak_3d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(NmrPipePKParser.Integer)
            self.state = 249
            self.number()
            self.state = 250
            self.number()
            self.state = 251
            self.number()
            self.state = 252
            self.number()
            self.state = 253
            self.number()
            self.state = 254
            self.number()
            self.state = 255
            self.number()
            self.state = 256
            self.number()
            self.state = 257
            self.number()
            self.state = 258
            self.number()
            self.state = 259
            self.number()
            self.state = 260
            self.number()
            self.state = 261
            self.number()
            self.state = 262
            self.number()
            self.state = 263
            self.number()
            self.state = 264
            self.number()
            self.state = 265
            self.number()
            self.state = 266
            self.number()
            self.state = 267
            self.match(NmrPipePKParser.Integer)
            self.state = 268
            self.match(NmrPipePKParser.Integer)
            self.state = 269
            self.match(NmrPipePKParser.Integer)
            self.state = 270
            self.match(NmrPipePKParser.Integer)
            self.state = 271
            self.match(NmrPipePKParser.Integer)
            self.state = 272
            self.match(NmrPipePKParser.Integer)
            self.state = 273
            self.number()
            self.state = 274
            self.number()
            self.state = 275
            self.number()
            self.state = 276
            self.number()
            self.state = 277
            self.match(NmrPipePKParser.Integer)
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 278
                self.match(NmrPipePKParser.Any_name)


            self.state = 281
            self.match(NmrPipePKParser.Integer)
            self.state = 282
            self.match(NmrPipePKParser.Integer)
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 283
                self.match(NmrPipePKParser.Integer)


            self.state = 286
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

        def Vars(self):
            return self.getToken(NmrPipePKParser.Vars, 0)

        def Index(self):
            return self.getToken(NmrPipePKParser.Index, 0)

        def X_axis(self):
            return self.getToken(NmrPipePKParser.X_axis, 0)

        def Y_axis(self):
            return self.getToken(NmrPipePKParser.Y_axis, 0)

        def Z_axis(self):
            return self.getToken(NmrPipePKParser.Z_axis, 0)

        def A_axis(self):
            return self.getToken(NmrPipePKParser.A_axis, 0)

        def Dx(self):
            return self.getToken(NmrPipePKParser.Dx, 0)

        def Dy(self):
            return self.getToken(NmrPipePKParser.Dy, 0)

        def Dz(self, i:int=None):
            if i is None:
                return self.getTokens(NmrPipePKParser.Dz)
            else:
                return self.getToken(NmrPipePKParser.Dz, i)

        def X_ppm(self):
            return self.getToken(NmrPipePKParser.X_ppm, 0)

        def Y_ppm(self):
            return self.getToken(NmrPipePKParser.Y_ppm, 0)

        def Z_ppm(self):
            return self.getToken(NmrPipePKParser.Z_ppm, 0)

        def A_ppm(self):
            return self.getToken(NmrPipePKParser.A_ppm, 0)

        def X_hz(self):
            return self.getToken(NmrPipePKParser.X_hz, 0)

        def Y_hz(self):
            return self.getToken(NmrPipePKParser.Y_hz, 0)

        def Z_hz(self):
            return self.getToken(NmrPipePKParser.Z_hz, 0)

        def A_hz(self):
            return self.getToken(NmrPipePKParser.A_hz, 0)

        def Xw(self):
            return self.getToken(NmrPipePKParser.Xw, 0)

        def Yw(self):
            return self.getToken(NmrPipePKParser.Yw, 0)

        def Zw(self):
            return self.getToken(NmrPipePKParser.Zw, 0)

        def Aw(self):
            return self.getToken(NmrPipePKParser.Aw, 0)

        def Xw_hz(self):
            return self.getToken(NmrPipePKParser.Xw_hz, 0)

        def Yw_hz(self):
            return self.getToken(NmrPipePKParser.Yw_hz, 0)

        def Zw_hz(self):
            return self.getToken(NmrPipePKParser.Zw_hz, 0)

        def Aw_hz(self):
            return self.getToken(NmrPipePKParser.Aw_hz, 0)

        def X1(self):
            return self.getToken(NmrPipePKParser.X1, 0)

        def X3(self):
            return self.getToken(NmrPipePKParser.X3, 0)

        def Y1(self):
            return self.getToken(NmrPipePKParser.Y1, 0)

        def Y3(self):
            return self.getToken(NmrPipePKParser.Y3, 0)

        def Z1(self):
            return self.getToken(NmrPipePKParser.Z1, 0)

        def Z3(self):
            return self.getToken(NmrPipePKParser.Z3, 0)

        def A1(self):
            return self.getToken(NmrPipePKParser.A1, 0)

        def A3(self):
            return self.getToken(NmrPipePKParser.A3, 0)

        def Height(self):
            return self.getToken(NmrPipePKParser.Height, 0)

        def DHeight(self):
            return self.getToken(NmrPipePKParser.DHeight, 0)

        def Vol(self):
            return self.getToken(NmrPipePKParser.Vol, 0)

        def Pchi2(self):
            return self.getToken(NmrPipePKParser.Pchi2, 0)

        def Type(self):
            return self.getToken(NmrPipePKParser.Type, 0)

        def ClustId(self):
            return self.getToken(NmrPipePKParser.ClustId, 0)

        def Memcnt(self):
            return self.getToken(NmrPipePKParser.Memcnt, 0)

        def RETURN_VA(self):
            return self.getToken(NmrPipePKParser.RETURN_VA, 0)

        def Format(self):
            return self.getToken(NmrPipePKParser.Format, 0)

        def Format_code(self, i:int=None):
            if i is None:
                return self.getTokens(NmrPipePKParser.Format_code)
            else:
                return self.getToken(NmrPipePKParser.Format_code, i)

        def RETURN_FO(self):
            return self.getToken(NmrPipePKParser.RETURN_FO, 0)

        def Ass(self):
            return self.getToken(NmrPipePKParser.Ass, 0)

        def Trouble(self):
            return self.getToken(NmrPipePKParser.Trouble, 0)

        def Null_value(self):
            return self.getToken(NmrPipePKParser.Null_value, 0)

        def Any_name_NV(self):
            return self.getToken(NmrPipePKParser.Any_name_NV, 0)

        def RETURN_NV(self):
            return self.getToken(NmrPipePKParser.RETURN_NV, 0)

        def Null_string(self):
            return self.getToken(NmrPipePKParser.Null_string, 0)

        def Any_name_NS(self):
            return self.getToken(NmrPipePKParser.Any_name_NS, 0)

        def RETURN_NS(self):
            return self.getToken(NmrPipePKParser.RETURN_NS, 0)

        def peak_4d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmrPipePKParser.Peak_4dContext)
            else:
                return self.getTypedRuleContext(NmrPipePKParser.Peak_4dContext,i)


        def getRuleIndex(self):
            return NmrPipePKParser.RULE_peak_list_4d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_list_4d" ):
                listener.enterPeak_list_4d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_list_4d" ):
                listener.exitPeak_list_4d(self)




    def peak_list_4d(self):

        localctx = NmrPipePKParser.Peak_list_4dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_peak_list_4d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(NmrPipePKParser.Vars)
            self.state = 289
            self.match(NmrPipePKParser.Index)
            self.state = 290
            self.match(NmrPipePKParser.X_axis)
            self.state = 291
            self.match(NmrPipePKParser.Y_axis)
            self.state = 292
            self.match(NmrPipePKParser.Z_axis)
            self.state = 293
            self.match(NmrPipePKParser.A_axis)
            self.state = 294
            self.match(NmrPipePKParser.Dx)
            self.state = 295
            self.match(NmrPipePKParser.Dy)
            self.state = 296
            self.match(NmrPipePKParser.Dz)
            self.state = 297
            self.match(NmrPipePKParser.Dz)
            self.state = 298
            self.match(NmrPipePKParser.X_ppm)
            self.state = 299
            self.match(NmrPipePKParser.Y_ppm)
            self.state = 300
            self.match(NmrPipePKParser.Z_ppm)
            self.state = 301
            self.match(NmrPipePKParser.A_ppm)
            self.state = 302
            self.match(NmrPipePKParser.X_hz)
            self.state = 303
            self.match(NmrPipePKParser.Y_hz)
            self.state = 304
            self.match(NmrPipePKParser.Z_hz)
            self.state = 305
            self.match(NmrPipePKParser.A_hz)
            self.state = 306
            self.match(NmrPipePKParser.Xw)
            self.state = 307
            self.match(NmrPipePKParser.Yw)
            self.state = 308
            self.match(NmrPipePKParser.Zw)
            self.state = 309
            self.match(NmrPipePKParser.Aw)
            self.state = 310
            self.match(NmrPipePKParser.Xw_hz)
            self.state = 311
            self.match(NmrPipePKParser.Yw_hz)
            self.state = 312
            self.match(NmrPipePKParser.Zw_hz)
            self.state = 313
            self.match(NmrPipePKParser.Aw_hz)
            self.state = 314
            self.match(NmrPipePKParser.X1)
            self.state = 315
            self.match(NmrPipePKParser.X3)
            self.state = 316
            self.match(NmrPipePKParser.Y1)
            self.state = 317
            self.match(NmrPipePKParser.Y3)
            self.state = 318
            self.match(NmrPipePKParser.Z1)
            self.state = 319
            self.match(NmrPipePKParser.Z3)
            self.state = 320
            self.match(NmrPipePKParser.A1)
            self.state = 321
            self.match(NmrPipePKParser.A3)
            self.state = 322
            self.match(NmrPipePKParser.Height)
            self.state = 323
            self.match(NmrPipePKParser.DHeight)
            self.state = 324
            self.match(NmrPipePKParser.Vol)
            self.state = 325
            self.match(NmrPipePKParser.Pchi2)
            self.state = 326
            self.match(NmrPipePKParser.Type)
            self.state = 328
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==68:
                self.state = 327
                self.match(NmrPipePKParser.Ass)


            self.state = 330
            self.match(NmrPipePKParser.ClustId)
            self.state = 331
            self.match(NmrPipePKParser.Memcnt)
            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==71:
                self.state = 332
                self.match(NmrPipePKParser.Trouble)


            self.state = 335
            self.match(NmrPipePKParser.RETURN_VA)
            self.state = 336
            self.match(NmrPipePKParser.Format)
            self.state = 337
            self.match(NmrPipePKParser.Format_code)
            self.state = 338
            self.match(NmrPipePKParser.Format_code)
            self.state = 339
            self.match(NmrPipePKParser.Format_code)
            self.state = 340
            self.match(NmrPipePKParser.Format_code)
            self.state = 341
            self.match(NmrPipePKParser.Format_code)
            self.state = 342
            self.match(NmrPipePKParser.Format_code)
            self.state = 343
            self.match(NmrPipePKParser.Format_code)
            self.state = 344
            self.match(NmrPipePKParser.Format_code)
            self.state = 345
            self.match(NmrPipePKParser.Format_code)
            self.state = 346
            self.match(NmrPipePKParser.Format_code)
            self.state = 347
            self.match(NmrPipePKParser.Format_code)
            self.state = 348
            self.match(NmrPipePKParser.Format_code)
            self.state = 349
            self.match(NmrPipePKParser.Format_code)
            self.state = 350
            self.match(NmrPipePKParser.Format_code)
            self.state = 351
            self.match(NmrPipePKParser.Format_code)
            self.state = 352
            self.match(NmrPipePKParser.Format_code)
            self.state = 353
            self.match(NmrPipePKParser.Format_code)
            self.state = 354
            self.match(NmrPipePKParser.Format_code)
            self.state = 355
            self.match(NmrPipePKParser.Format_code)
            self.state = 356
            self.match(NmrPipePKParser.Format_code)
            self.state = 357
            self.match(NmrPipePKParser.Format_code)
            self.state = 358
            self.match(NmrPipePKParser.Format_code)
            self.state = 359
            self.match(NmrPipePKParser.Format_code)
            self.state = 360
            self.match(NmrPipePKParser.Format_code)
            self.state = 361
            self.match(NmrPipePKParser.Format_code)
            self.state = 362
            self.match(NmrPipePKParser.Format_code)
            self.state = 363
            self.match(NmrPipePKParser.Format_code)
            self.state = 364
            self.match(NmrPipePKParser.Format_code)
            self.state = 365
            self.match(NmrPipePKParser.Format_code)
            self.state = 366
            self.match(NmrPipePKParser.Format_code)
            self.state = 367
            self.match(NmrPipePKParser.Format_code)
            self.state = 368
            self.match(NmrPipePKParser.Format_code)
            self.state = 369
            self.match(NmrPipePKParser.Format_code)
            self.state = 370
            self.match(NmrPipePKParser.Format_code)
            self.state = 371
            self.match(NmrPipePKParser.Format_code)
            self.state = 372
            self.match(NmrPipePKParser.Format_code)
            self.state = 373
            self.match(NmrPipePKParser.Format_code)
            self.state = 374
            self.match(NmrPipePKParser.Format_code)
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 375
                self.match(NmrPipePKParser.Format_code)


            self.state = 378
            self.match(NmrPipePKParser.Format_code)
            self.state = 379
            self.match(NmrPipePKParser.Format_code)
            self.state = 381
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==79:
                self.state = 380
                self.match(NmrPipePKParser.Format_code)


            self.state = 383
            self.match(NmrPipePKParser.RETURN_FO)
            self.state = 387
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 384
                self.match(NmrPipePKParser.Null_value)
                self.state = 385
                self.match(NmrPipePKParser.Any_name_NV)
                self.state = 386
                self.match(NmrPipePKParser.RETURN_NV)


            self.state = 392
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 389
                self.match(NmrPipePKParser.Null_string)
                self.state = 390
                self.match(NmrPipePKParser.Any_name_NS)
                self.state = 391
                self.match(NmrPipePKParser.RETURN_NS)


            self.state = 395 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 394
                self.peak_4d()
                self.state = 397 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==6):
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

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(NmrPipePKParser.Integer)
            else:
                return self.getToken(NmrPipePKParser.Integer, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmrPipePKParser.NumberContext)
            else:
                return self.getTypedRuleContext(NmrPipePKParser.NumberContext,i)


        def RETURN(self):
            return self.getToken(NmrPipePKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(NmrPipePKParser.EOF, 0)

        def Any_name(self):
            return self.getToken(NmrPipePKParser.Any_name, 0)

        def getRuleIndex(self):
            return NmrPipePKParser.RULE_peak_4d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_4d" ):
                listener.enterPeak_4d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_4d" ):
                listener.exitPeak_4d(self)




    def peak_4d(self):

        localctx = NmrPipePKParser.Peak_4dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_peak_4d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(NmrPipePKParser.Integer)
            self.state = 400
            self.number()
            self.state = 401
            self.number()
            self.state = 402
            self.number()
            self.state = 403
            self.number()
            self.state = 404
            self.number()
            self.state = 405
            self.number()
            self.state = 406
            self.number()
            self.state = 407
            self.number()
            self.state = 408
            self.number()
            self.state = 409
            self.number()
            self.state = 410
            self.number()
            self.state = 411
            self.number()
            self.state = 412
            self.number()
            self.state = 413
            self.number()
            self.state = 414
            self.number()
            self.state = 415
            self.number()
            self.state = 416
            self.number()
            self.state = 417
            self.number()
            self.state = 418
            self.number()
            self.state = 419
            self.number()
            self.state = 420
            self.number()
            self.state = 421
            self.number()
            self.state = 422
            self.number()
            self.state = 423
            self.number()
            self.state = 424
            self.match(NmrPipePKParser.Integer)
            self.state = 425
            self.match(NmrPipePKParser.Integer)
            self.state = 426
            self.match(NmrPipePKParser.Integer)
            self.state = 427
            self.match(NmrPipePKParser.Integer)
            self.state = 428
            self.match(NmrPipePKParser.Integer)
            self.state = 429
            self.match(NmrPipePKParser.Integer)
            self.state = 430
            self.match(NmrPipePKParser.Integer)
            self.state = 431
            self.match(NmrPipePKParser.Integer)
            self.state = 432
            self.number()
            self.state = 433
            self.number()
            self.state = 434
            self.number()
            self.state = 435
            self.number()
            self.state = 436
            self.match(NmrPipePKParser.Integer)
            self.state = 438
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 437
                self.match(NmrPipePKParser.Any_name)


            self.state = 440
            self.match(NmrPipePKParser.Integer)
            self.state = 441
            self.match(NmrPipePKParser.Integer)
            self.state = 443
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 442
                self.match(NmrPipePKParser.Integer)


            self.state = 445
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


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Float(self):
            return self.getToken(NmrPipePKParser.Float, 0)

        def Real(self):
            return self.getToken(NmrPipePKParser.Real, 0)

        def Any_name(self):
            return self.getToken(NmrPipePKParser.Any_name, 0)

        def getRuleIndex(self):
            return NmrPipePKParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = NmrPipePKParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4480) != 0)):
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





