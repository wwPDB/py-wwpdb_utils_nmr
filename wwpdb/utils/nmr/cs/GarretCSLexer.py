# Generated from GarretCSLexer.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,10,244,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,1,0,3,0,43,8,0,1,0,1,0,1,1,3,1,48,8,1,1,1,1,1,3,1,52,8,1,1,2,
        1,2,1,2,1,2,1,2,1,2,3,2,60,8,2,1,3,1,3,1,4,4,4,65,8,4,11,4,12,4,
        66,1,5,1,5,1,6,4,6,72,8,6,11,6,12,6,73,1,6,5,6,77,8,6,10,6,12,6,
        80,9,6,1,6,5,6,83,8,6,10,6,12,6,86,9,6,1,6,5,6,89,8,6,10,6,12,6,
        92,9,6,1,6,1,6,1,7,4,7,97,8,7,11,7,12,7,98,1,7,5,7,102,8,7,10,7,
        12,7,105,9,7,1,7,5,7,108,8,7,10,7,12,7,111,9,7,1,7,5,7,114,8,7,10,
        7,12,7,117,9,7,1,7,1,7,1,8,4,8,122,8,8,11,8,12,8,123,1,8,5,8,127,
        8,8,10,8,12,8,130,9,8,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,3,11,140,
        8,11,1,12,1,12,3,12,144,8,12,1,13,1,13,3,13,148,8,13,1,14,1,14,5,
        14,152,8,14,10,14,12,14,155,9,14,1,15,4,15,158,8,15,11,15,12,15,
        159,1,15,1,15,1,16,4,16,165,8,16,11,16,12,16,166,1,17,1,17,1,18,
        1,18,1,18,4,18,174,8,18,11,18,12,18,175,1,18,1,18,4,18,180,8,18,
        11,18,12,18,181,1,18,1,18,4,18,186,8,18,11,18,12,18,187,1,18,1,18,
        1,18,1,18,1,18,1,18,3,18,196,8,18,1,18,5,18,199,8,18,10,18,12,18,
        202,9,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,4,19,211,8,19,11,19,
        12,19,212,1,19,1,19,4,19,217,8,19,11,19,12,19,218,1,19,1,19,4,19,
        223,8,19,11,19,12,19,224,1,19,1,19,1,19,1,19,1,19,1,19,3,19,233,
        8,19,1,19,5,19,236,8,19,10,19,12,19,239,9,19,1,19,1,19,1,19,1,19,
        0,0,20,1,1,3,2,5,0,7,0,9,0,11,0,13,3,15,4,17,5,19,6,21,0,23,0,25,
        0,27,0,29,0,31,7,33,8,35,0,37,9,39,10,1,0,9,2,0,43,43,45,45,1,0,
        48,57,4,0,44,44,47,47,58,58,124,124,2,0,10,10,13,13,2,0,65,90,97,
        122,6,0,40,40,42,43,45,46,63,63,95,95,123,123,8,0,34,35,37,37,39,
        39,41,41,44,44,47,47,59,59,124,125,2,0,9,9,32,32,6,0,33,33,35,35,
        38,38,47,47,61,61,92,92,270,0,1,1,0,0,0,0,3,1,0,0,0,0,13,1,0,0,0,
        0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,
        0,37,1,0,0,0,0,39,1,0,0,0,1,42,1,0,0,0,3,47,1,0,0,0,5,59,1,0,0,0,
        7,61,1,0,0,0,9,64,1,0,0,0,11,68,1,0,0,0,13,71,1,0,0,0,15,96,1,0,
        0,0,17,121,1,0,0,0,19,133,1,0,0,0,21,135,1,0,0,0,23,139,1,0,0,0,
        25,143,1,0,0,0,27,147,1,0,0,0,29,149,1,0,0,0,31,157,1,0,0,0,33,164,
        1,0,0,0,35,168,1,0,0,0,37,195,1,0,0,0,39,232,1,0,0,0,41,43,7,0,0,
        0,42,41,1,0,0,0,42,43,1,0,0,0,43,44,1,0,0,0,44,45,3,9,4,0,45,2,1,
        0,0,0,46,48,7,0,0,0,47,46,1,0,0,0,47,48,1,0,0,0,48,51,1,0,0,0,49,
        52,3,9,4,0,50,52,3,5,2,0,51,49,1,0,0,0,51,50,1,0,0,0,52,4,1,0,0,
        0,53,54,3,9,4,0,54,55,5,46,0,0,55,56,3,9,4,0,56,60,1,0,0,0,57,58,
        5,46,0,0,58,60,3,9,4,0,59,53,1,0,0,0,59,57,1,0,0,0,60,6,1,0,0,0,
        61,62,7,1,0,0,62,8,1,0,0,0,63,65,3,7,3,0,64,63,1,0,0,0,65,66,1,0,
        0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,10,1,0,0,0,68,69,7,2,0,0,69,12,
        1,0,0,0,70,72,5,35,0,0,71,70,1,0,0,0,72,73,1,0,0,0,73,71,1,0,0,0,
        73,74,1,0,0,0,74,78,1,0,0,0,75,77,8,3,0,0,76,75,1,0,0,0,77,80,1,
        0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,84,1,0,0,0,80,78,1,0,0,0,81,
        83,5,35,0,0,82,81,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,0,
        0,0,85,90,1,0,0,0,86,84,1,0,0,0,87,89,8,3,0,0,88,87,1,0,0,0,89,92,
        1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,93,1,0,0,0,92,90,1,0,0,0,
        93,94,6,6,0,0,94,14,1,0,0,0,95,97,5,33,0,0,96,95,1,0,0,0,97,98,1,
        0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,103,1,0,0,0,100,102,8,3,0,0,
        101,100,1,0,0,0,102,105,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,
        104,109,1,0,0,0,105,103,1,0,0,0,106,108,5,33,0,0,107,106,1,0,0,0,
        108,111,1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,115,1,0,0,0,
        111,109,1,0,0,0,112,114,8,3,0,0,113,112,1,0,0,0,114,117,1,0,0,0,
        115,113,1,0,0,0,115,116,1,0,0,0,116,118,1,0,0,0,117,115,1,0,0,0,
        118,119,6,7,0,0,119,16,1,0,0,0,120,122,5,59,0,0,121,120,1,0,0,0,
        122,123,1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,128,1,0,0,0,
        125,127,8,3,0,0,126,125,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,
        128,129,1,0,0,0,129,131,1,0,0,0,130,128,1,0,0,0,131,132,3,33,16,
        0,132,18,1,0,0,0,133,134,3,29,14,0,134,20,1,0,0,0,135,136,7,4,0,
        0,136,22,1,0,0,0,137,140,3,21,10,0,138,140,3,7,3,0,139,137,1,0,0,
        0,139,138,1,0,0,0,140,24,1,0,0,0,141,144,3,23,11,0,142,144,7,5,0,
        0,143,141,1,0,0,0,143,142,1,0,0,0,144,26,1,0,0,0,145,148,3,25,12,
        0,146,148,7,6,0,0,147,145,1,0,0,0,147,146,1,0,0,0,148,28,1,0,0,0,
        149,153,3,25,12,0,150,152,3,27,13,0,151,150,1,0,0,0,152,155,1,0,
        0,0,153,151,1,0,0,0,153,154,1,0,0,0,154,30,1,0,0,0,155,153,1,0,0,
        0,156,158,7,7,0,0,157,156,1,0,0,0,158,159,1,0,0,0,159,157,1,0,0,
        0,159,160,1,0,0,0,160,161,1,0,0,0,161,162,6,15,1,0,162,32,1,0,0,
        0,163,165,7,3,0,0,164,163,1,0,0,0,165,166,1,0,0,0,166,164,1,0,0,
        0,166,167,1,0,0,0,167,34,1,0,0,0,168,169,7,8,0,0,169,36,1,0,0,0,
        170,196,3,35,17,0,171,173,3,35,17,0,172,174,5,47,0,0,173,172,1,0,
        0,0,174,175,1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,196,1,0,
        0,0,177,179,3,35,17,0,178,180,5,42,0,0,179,178,1,0,0,0,180,181,1,
        0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,196,1,0,0,0,183,185,3,
        35,17,0,184,186,5,61,0,0,185,184,1,0,0,0,186,187,1,0,0,0,187,185,
        1,0,0,0,187,188,1,0,0,0,188,196,1,0,0,0,189,190,5,82,0,0,190,191,
        5,69,0,0,191,192,5,77,0,0,192,193,5,65,0,0,193,194,5,82,0,0,194,
        196,5,75,0,0,195,170,1,0,0,0,195,171,1,0,0,0,195,177,1,0,0,0,195,
        183,1,0,0,0,195,189,1,0,0,0,196,200,1,0,0,0,197,199,5,32,0,0,198,
        197,1,0,0,0,199,202,1,0,0,0,200,198,1,0,0,0,200,201,1,0,0,0,201,
        203,1,0,0,0,202,200,1,0,0,0,203,204,3,33,16,0,204,205,1,0,0,0,205,
        206,6,18,0,0,206,38,1,0,0,0,207,233,3,35,17,0,208,210,3,35,17,0,
        209,211,5,47,0,0,210,209,1,0,0,0,211,212,1,0,0,0,212,210,1,0,0,0,
        212,213,1,0,0,0,213,233,1,0,0,0,214,216,3,35,17,0,215,217,5,42,0,
        0,216,215,1,0,0,0,217,218,1,0,0,0,218,216,1,0,0,0,218,219,1,0,0,
        0,219,233,1,0,0,0,220,222,3,35,17,0,221,223,5,61,0,0,222,221,1,0,
        0,0,223,224,1,0,0,0,224,222,1,0,0,0,224,225,1,0,0,0,225,233,1,0,
        0,0,226,227,5,82,0,0,227,228,5,69,0,0,228,229,5,77,0,0,229,230,5,
        65,0,0,230,231,5,82,0,0,231,233,5,75,0,0,232,207,1,0,0,0,232,208,
        1,0,0,0,232,214,1,0,0,0,232,220,1,0,0,0,232,226,1,0,0,0,233,237,
        1,0,0,0,234,236,8,3,0,0,235,234,1,0,0,0,236,239,1,0,0,0,237,235,
        1,0,0,0,237,238,1,0,0,0,238,240,1,0,0,0,239,237,1,0,0,0,240,241,
        3,33,16,0,241,242,1,0,0,0,242,243,6,19,0,0,243,40,1,0,0,0,32,0,42,
        47,51,59,66,73,78,84,90,98,103,109,115,123,128,139,143,147,153,159,
        166,175,181,187,195,200,212,218,224,232,237,2,0,1,0,6,0,0
    ]

class GarretCSLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Integer = 1
    Float = 2
    SHARP_COMMENT = 3
    EXCLM_COMMENT = 4
    SMCLN_COMMENT = 5
    Simple_name = 6
    SPACE = 7
    RETURN = 8
    SECTION_COMMENT = 9
    LINE_COMMENT = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "Integer", "Float", "SHARP_COMMENT", "EXCLM_COMMENT", "SMCLN_COMMENT", 
            "Simple_name", "SPACE", "RETURN", "SECTION_COMMENT", "LINE_COMMENT" ]

    ruleNames = [ "Integer", "Float", "DEC_DOT_DEC", "DEC_DIGIT", "DECIMAL", 
                  "SEPARATOR", "SHARP_COMMENT", "EXCLM_COMMENT", "SMCLN_COMMENT", 
                  "Simple_name", "ALPHA", "ALPHA_NUM", "START_CHAR", "NAME_CHAR", 
                  "SIMPLE_NAME", "SPACE", "RETURN", "COMMENT_START_CHAR", 
                  "SECTION_COMMENT", "LINE_COMMENT" ]

    grammarFileName = "GarretCSLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


