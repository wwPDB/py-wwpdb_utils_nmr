# Generated from CyanaMRParser.g4 by ANTLR 4.10.1
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
        4,1,15,323,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,5,0,72,8,0,10,0,12,0,75,9,0,1,0,1,0,1,1,4,1,80,8,1,11,1,
        12,1,81,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,92,8,2,1,2,3,2,95,8,
        2,1,2,3,2,98,8,2,1,2,3,2,101,8,2,1,2,3,2,104,8,2,1,3,4,3,107,8,3,
        11,3,12,3,108,1,4,1,4,1,4,1,4,1,4,1,4,3,4,117,8,4,1,4,1,4,1,4,3,
        4,122,8,4,1,4,3,4,125,8,4,1,5,4,5,128,8,5,11,5,12,5,129,1,5,4,5,
        133,8,5,11,5,12,5,134,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,8,4,8,154,8,8,11,8,12,8,155,1,8,4,8,159,
        8,8,11,8,12,8,160,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,11,4,11,177,8,11,11,11,12,11,178,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,4,12,188,8,12,11,12,12,12,189,1,13,4,13,193,8,
        13,11,13,12,13,194,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        4,14,206,8,14,11,14,12,14,207,1,15,4,15,211,8,15,11,15,12,15,212,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,4,16,225,8,16,
        11,16,12,16,226,1,17,4,17,230,8,17,11,17,12,17,231,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,4,18,241,8,18,11,18,12,18,242,1,19,4,19,246,
        8,19,11,19,12,19,247,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        4,20,259,8,20,11,20,12,20,260,1,21,4,21,264,8,21,11,21,12,21,265,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,4,22,278,8,22,
        11,22,12,22,279,1,23,4,23,283,8,23,11,23,12,23,284,1,24,1,24,1,24,
        1,24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,297,8,24,1,24,3,24,300,8,
        24,1,25,4,25,303,8,25,11,25,12,25,304,1,26,1,26,1,26,1,26,1,26,1,
        26,3,26,313,8,26,1,26,3,26,316,8,26,1,27,1,27,1,27,1,28,1,28,1,28,
        0,0,29,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,48,50,52,54,56,0,1,1,0,1,2,338,0,73,1,0,0,0,2,79,1,0,0,
        0,4,83,1,0,0,0,6,106,1,0,0,0,8,110,1,0,0,0,10,127,1,0,0,0,12,136,
        1,0,0,0,14,141,1,0,0,0,16,153,1,0,0,0,18,162,1,0,0,0,20,167,1,0,
        0,0,22,176,1,0,0,0,24,180,1,0,0,0,26,192,1,0,0,0,28,196,1,0,0,0,
        30,210,1,0,0,0,32,214,1,0,0,0,34,229,1,0,0,0,36,233,1,0,0,0,38,245,
        1,0,0,0,40,249,1,0,0,0,42,263,1,0,0,0,44,267,1,0,0,0,46,282,1,0,
        0,0,48,286,1,0,0,0,50,302,1,0,0,0,52,306,1,0,0,0,54,317,1,0,0,0,
        56,320,1,0,0,0,58,72,3,2,1,0,59,72,3,22,11,0,60,72,3,26,13,0,61,
        72,3,30,15,0,62,72,3,34,17,0,63,72,3,38,19,0,64,72,3,42,21,0,65,
        72,3,46,23,0,66,72,3,6,3,0,67,72,3,10,5,0,68,72,3,16,8,0,69,72,3,
        50,25,0,70,72,3,54,27,0,71,58,1,0,0,0,71,59,1,0,0,0,71,60,1,0,0,
        0,71,61,1,0,0,0,71,62,1,0,0,0,71,63,1,0,0,0,71,64,1,0,0,0,71,65,
        1,0,0,0,71,66,1,0,0,0,71,67,1,0,0,0,71,68,1,0,0,0,71,69,1,0,0,0,
        71,70,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,76,1,
        0,0,0,75,73,1,0,0,0,76,77,5,0,0,1,77,1,1,0,0,0,78,80,3,4,2,0,79,
        78,1,0,0,0,80,81,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,3,1,0,0,
        0,83,84,5,1,0,0,84,85,5,11,0,0,85,86,5,11,0,0,86,87,5,1,0,0,87,88,
        5,11,0,0,88,89,5,11,0,0,89,91,3,56,28,0,90,92,3,56,28,0,91,90,1,
        0,0,0,91,92,1,0,0,0,92,94,1,0,0,0,93,95,3,56,28,0,94,93,1,0,0,0,
        94,95,1,0,0,0,95,97,1,0,0,0,96,98,3,56,28,0,97,96,1,0,0,0,97,98,
        1,0,0,0,98,100,1,0,0,0,99,101,3,56,28,0,100,99,1,0,0,0,100,101,1,
        0,0,0,101,103,1,0,0,0,102,104,3,56,28,0,103,102,1,0,0,0,103,104,
        1,0,0,0,104,5,1,0,0,0,105,107,3,8,4,0,106,105,1,0,0,0,107,108,1,
        0,0,0,108,106,1,0,0,0,108,109,1,0,0,0,109,7,1,0,0,0,110,111,5,1,
        0,0,111,112,5,11,0,0,112,113,5,11,0,0,113,114,3,56,28,0,114,116,
        3,56,28,0,115,117,3,56,28,0,116,115,1,0,0,0,116,117,1,0,0,0,117,
        121,1,0,0,0,118,119,5,6,0,0,119,120,5,7,0,0,120,122,5,1,0,0,121,
        118,1,0,0,0,121,122,1,0,0,0,122,124,1,0,0,0,123,125,5,8,0,0,124,
        123,1,0,0,0,124,125,1,0,0,0,125,9,1,0,0,0,126,128,3,12,6,0,127,126,
        1,0,0,0,128,129,1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,132,
        1,0,0,0,131,133,3,14,7,0,132,131,1,0,0,0,133,134,1,0,0,0,134,132,
        1,0,0,0,134,135,1,0,0,0,135,11,1,0,0,0,136,137,5,1,0,0,137,138,5,
        2,0,0,138,139,5,2,0,0,139,140,5,1,0,0,140,13,1,0,0,0,141,142,5,1,
        0,0,142,143,5,11,0,0,143,144,5,11,0,0,144,145,5,1,0,0,145,146,5,
        11,0,0,146,147,5,11,0,0,147,148,3,56,28,0,148,149,3,56,28,0,149,
        150,3,56,28,0,150,151,5,1,0,0,151,15,1,0,0,0,152,154,3,18,9,0,153,
        152,1,0,0,0,154,155,1,0,0,0,155,153,1,0,0,0,155,156,1,0,0,0,156,
        158,1,0,0,0,157,159,3,20,10,0,158,157,1,0,0,0,159,160,1,0,0,0,160,
        158,1,0,0,0,160,161,1,0,0,0,161,17,1,0,0,0,162,163,5,1,0,0,163,164,
        5,2,0,0,164,165,5,2,0,0,165,166,5,1,0,0,166,19,1,0,0,0,167,168,5,
        1,0,0,168,169,5,11,0,0,169,170,5,11,0,0,170,171,3,56,28,0,171,172,
        3,56,28,0,172,173,3,56,28,0,173,174,5,1,0,0,174,21,1,0,0,0,175,177,
        3,24,12,0,176,175,1,0,0,0,177,178,1,0,0,0,178,176,1,0,0,0,178,179,
        1,0,0,0,179,23,1,0,0,0,180,181,5,1,0,0,181,187,5,11,0,0,182,183,
        5,11,0,0,183,184,5,1,0,0,184,185,5,11,0,0,185,186,5,11,0,0,186,188,
        3,56,28,0,187,182,1,0,0,0,188,189,1,0,0,0,189,187,1,0,0,0,189,190,
        1,0,0,0,190,25,1,0,0,0,191,193,3,28,14,0,192,191,1,0,0,0,193,194,
        1,0,0,0,194,192,1,0,0,0,194,195,1,0,0,0,195,27,1,0,0,0,196,197,5,
        1,0,0,197,205,5,11,0,0,198,199,5,11,0,0,199,200,5,1,0,0,200,201,
        5,11,0,0,201,202,5,11,0,0,202,203,3,56,28,0,203,204,3,56,28,0,204,
        206,1,0,0,0,205,198,1,0,0,0,206,207,1,0,0,0,207,205,1,0,0,0,207,
        208,1,0,0,0,208,29,1,0,0,0,209,211,3,32,16,0,210,209,1,0,0,0,211,
        212,1,0,0,0,212,210,1,0,0,0,212,213,1,0,0,0,213,31,1,0,0,0,214,215,
        5,1,0,0,215,224,5,11,0,0,216,217,5,11,0,0,217,218,5,1,0,0,218,219,
        5,11,0,0,219,220,5,11,0,0,220,221,3,56,28,0,221,222,3,56,28,0,222,
        223,3,56,28,0,223,225,1,0,0,0,224,216,1,0,0,0,225,226,1,0,0,0,226,
        224,1,0,0,0,226,227,1,0,0,0,227,33,1,0,0,0,228,230,3,36,18,0,229,
        228,1,0,0,0,230,231,1,0,0,0,231,229,1,0,0,0,231,232,1,0,0,0,232,
        35,1,0,0,0,233,234,5,1,0,0,234,235,5,11,0,0,235,240,5,11,0,0,236,
        237,5,1,0,0,237,238,5,11,0,0,238,239,5,11,0,0,239,241,3,56,28,0,
        240,236,1,0,0,0,241,242,1,0,0,0,242,240,1,0,0,0,242,243,1,0,0,0,
        243,37,1,0,0,0,244,246,3,40,20,0,245,244,1,0,0,0,246,247,1,0,0,0,
        247,245,1,0,0,0,247,248,1,0,0,0,248,39,1,0,0,0,249,250,5,1,0,0,250,
        251,5,11,0,0,251,258,5,11,0,0,252,253,5,1,0,0,253,254,5,11,0,0,254,
        255,5,11,0,0,255,256,3,56,28,0,256,257,3,56,28,0,257,259,1,0,0,0,
        258,252,1,0,0,0,259,260,1,0,0,0,260,258,1,0,0,0,260,261,1,0,0,0,
        261,41,1,0,0,0,262,264,3,44,22,0,263,262,1,0,0,0,264,265,1,0,0,0,
        265,263,1,0,0,0,265,266,1,0,0,0,266,43,1,0,0,0,267,268,5,1,0,0,268,
        269,5,11,0,0,269,277,5,11,0,0,270,271,5,1,0,0,271,272,5,11,0,0,272,
        273,5,11,0,0,273,274,3,56,28,0,274,275,3,56,28,0,275,276,3,56,28,
        0,276,278,1,0,0,0,277,270,1,0,0,0,278,279,1,0,0,0,279,277,1,0,0,
        0,279,280,1,0,0,0,280,45,1,0,0,0,281,283,3,48,24,0,282,281,1,0,0,
        0,283,284,1,0,0,0,284,282,1,0,0,0,284,285,1,0,0,0,285,47,1,0,0,0,
        286,287,5,1,0,0,287,288,5,11,0,0,288,289,5,11,0,0,289,290,5,11,0,
        0,290,291,5,1,0,0,291,292,5,11,0,0,292,293,5,11,0,0,293,294,5,11,
        0,0,294,296,3,56,28,0,295,297,3,56,28,0,296,295,1,0,0,0,296,297,
        1,0,0,0,297,299,1,0,0,0,298,300,3,56,28,0,299,298,1,0,0,0,299,300,
        1,0,0,0,300,49,1,0,0,0,301,303,3,52,26,0,302,301,1,0,0,0,303,304,
        1,0,0,0,304,302,1,0,0,0,304,305,1,0,0,0,305,51,1,0,0,0,306,307,5,
        1,0,0,307,308,5,11,0,0,308,309,5,11,0,0,309,310,5,11,0,0,310,312,
        3,56,28,0,311,313,3,56,28,0,312,311,1,0,0,0,312,313,1,0,0,0,313,
        315,1,0,0,0,314,316,3,56,28,0,315,314,1,0,0,0,315,316,1,0,0,0,316,
        53,1,0,0,0,317,318,5,9,0,0,318,319,5,10,0,0,319,55,1,0,0,0,320,321,
        7,0,0,0,321,57,1,0,0,0,34,71,73,81,91,94,97,100,103,108,116,121,
        124,129,134,155,160,178,189,194,207,212,226,231,242,247,260,265,
        279,284,296,299,304,312,315
    ]

class CyanaMRParser ( Parser ):

    grammarFileName = "CyanaMRParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'TYPE'", "'='", "'OR'", 
                     "'SSBOND'" ]

    symbolicNames = [ "<INVALID>", "Integer", "Float", "SHARP_COMMENT", 
                      "EXCLM_COMMENT", "SMCLN_COMMENT", "Type", "Equ_op", 
                      "Or", "Ssbond", "Ssbond_resids", "Simple_name", "SPACE", 
                      "COMMENT", "SECTION_COMMENT", "LINE_COMMENT" ]

    RULE_cyana_mr = 0
    RULE_distance_restraints = 1
    RULE_distance_restraint = 2
    RULE_torsion_angle_restraints = 3
    RULE_torsion_angle_restraint = 4
    RULE_rdc_restraints = 5
    RULE_rdc_parameter = 6
    RULE_rdc_restraint = 7
    RULE_pcs_restraints = 8
    RULE_pcs_parameter = 9
    RULE_pcs_restraint = 10
    RULE_fixres_distance_restraints = 11
    RULE_fixres_distance_restraint = 12
    RULE_fixresw_distance_restraints = 13
    RULE_fixresw_distance_restraint = 14
    RULE_fixresw2_distance_restraints = 15
    RULE_fixresw2_distance_restraint = 16
    RULE_fixatm_distance_restraints = 17
    RULE_fixatm_distance_restraint = 18
    RULE_fixatmw_distance_restraints = 19
    RULE_fixatmw_distance_restraint = 20
    RULE_fixatmw2_distance_restraints = 21
    RULE_fixatmw2_distance_restraint = 22
    RULE_distance_w_chain_restraints = 23
    RULE_distance_w_chain_restraint = 24
    RULE_cco_restraints = 25
    RULE_cco_restraint = 26
    RULE_ssbond_macro = 27
    RULE_number = 28

    ruleNames =  [ "cyana_mr", "distance_restraints", "distance_restraint", 
                   "torsion_angle_restraints", "torsion_angle_restraint", 
                   "rdc_restraints", "rdc_parameter", "rdc_restraint", "pcs_restraints", 
                   "pcs_parameter", "pcs_restraint", "fixres_distance_restraints", 
                   "fixres_distance_restraint", "fixresw_distance_restraints", 
                   "fixresw_distance_restraint", "fixresw2_distance_restraints", 
                   "fixresw2_distance_restraint", "fixatm_distance_restraints", 
                   "fixatm_distance_restraint", "fixatmw_distance_restraints", 
                   "fixatmw_distance_restraint", "fixatmw2_distance_restraints", 
                   "fixatmw2_distance_restraint", "distance_w_chain_restraints", 
                   "distance_w_chain_restraint", "cco_restraints", "cco_restraint", 
                   "ssbond_macro", "number" ]

    EOF = Token.EOF
    Integer=1
    Float=2
    SHARP_COMMENT=3
    EXCLM_COMMENT=4
    SMCLN_COMMENT=5
    Type=6
    Equ_op=7
    Or=8
    Ssbond=9
    Ssbond_resids=10
    Simple_name=11
    SPACE=12
    COMMENT=13
    SECTION_COMMENT=14
    LINE_COMMENT=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Cyana_mrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CyanaMRParser.EOF, 0)

        def distance_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Distance_restraintsContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Distance_restraintsContext,i)


        def fixres_distance_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Fixres_distance_restraintsContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Fixres_distance_restraintsContext,i)


        def fixresw_distance_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Fixresw_distance_restraintsContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Fixresw_distance_restraintsContext,i)


        def fixresw2_distance_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Fixresw2_distance_restraintsContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Fixresw2_distance_restraintsContext,i)


        def fixatm_distance_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Fixatm_distance_restraintsContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Fixatm_distance_restraintsContext,i)


        def fixatmw_distance_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Fixatmw_distance_restraintsContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Fixatmw_distance_restraintsContext,i)


        def fixatmw2_distance_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Fixatmw2_distance_restraintsContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Fixatmw2_distance_restraintsContext,i)


        def distance_w_chain_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Distance_w_chain_restraintsContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Distance_w_chain_restraintsContext,i)


        def torsion_angle_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Torsion_angle_restraintsContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Torsion_angle_restraintsContext,i)


        def rdc_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Rdc_restraintsContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Rdc_restraintsContext,i)


        def pcs_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Pcs_restraintsContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Pcs_restraintsContext,i)


        def cco_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Cco_restraintsContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Cco_restraintsContext,i)


        def ssbond_macro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Ssbond_macroContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Ssbond_macroContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_cyana_mr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCyana_mr" ):
                listener.enterCyana_mr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCyana_mr" ):
                listener.exitCyana_mr(self)




    def cyana_mr(self):

        localctx = CyanaMRParser.Cyana_mrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_cyana_mr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CyanaMRParser.Integer or _la==CyanaMRParser.Ssbond:
                self.state = 71
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 58
                    self.distance_restraints()
                    pass

                elif la_ == 2:
                    self.state = 59
                    self.fixres_distance_restraints()
                    pass

                elif la_ == 3:
                    self.state = 60
                    self.fixresw_distance_restraints()
                    pass

                elif la_ == 4:
                    self.state = 61
                    self.fixresw2_distance_restraints()
                    pass

                elif la_ == 5:
                    self.state = 62
                    self.fixatm_distance_restraints()
                    pass

                elif la_ == 6:
                    self.state = 63
                    self.fixatmw_distance_restraints()
                    pass

                elif la_ == 7:
                    self.state = 64
                    self.fixatmw2_distance_restraints()
                    pass

                elif la_ == 8:
                    self.state = 65
                    self.distance_w_chain_restraints()
                    pass

                elif la_ == 9:
                    self.state = 66
                    self.torsion_angle_restraints()
                    pass

                elif la_ == 10:
                    self.state = 67
                    self.rdc_restraints()
                    pass

                elif la_ == 11:
                    self.state = 68
                    self.pcs_restraints()
                    pass

                elif la_ == 12:
                    self.state = 69
                    self.cco_restraints()
                    pass

                elif la_ == 13:
                    self.state = 70
                    self.ssbond_macro()
                    pass


                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 76
            self.match(CyanaMRParser.EOF)
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

        def distance_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Distance_restraintContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Distance_restraintContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_distance_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistance_restraints" ):
                listener.enterDistance_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistance_restraints" ):
                listener.exitDistance_restraints(self)




    def distance_restraints(self):

        localctx = CyanaMRParser.Distance_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_distance_restraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 78
                    self.distance_restraint()

                else:
                    raise NoViableAltException(self)
                self.state = 81 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
                return self.getTokens(CyanaMRParser.Integer)
            else:
                return self.getToken(CyanaMRParser.Integer, i)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Simple_name)
            else:
                return self.getToken(CyanaMRParser.Simple_name, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.NumberContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_distance_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistance_restraint" ):
                listener.enterDistance_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistance_restraint" ):
                listener.exitDistance_restraint(self)




    def distance_restraint(self):

        localctx = CyanaMRParser.Distance_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_distance_restraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(CyanaMRParser.Integer)
            self.state = 84
            self.match(CyanaMRParser.Simple_name)
            self.state = 85
            self.match(CyanaMRParser.Simple_name)
            self.state = 86
            self.match(CyanaMRParser.Integer)
            self.state = 87
            self.match(CyanaMRParser.Simple_name)
            self.state = 88
            self.match(CyanaMRParser.Simple_name)
            self.state = 89
            self.number()
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 90
                self.number()


            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 93
                self.number()


            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 96
                self.number()


            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 99
                self.number()


            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 102
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

        def torsion_angle_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Torsion_angle_restraintContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Torsion_angle_restraintContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_torsion_angle_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTorsion_angle_restraints" ):
                listener.enterTorsion_angle_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTorsion_angle_restraints" ):
                listener.exitTorsion_angle_restraints(self)




    def torsion_angle_restraints(self):

        localctx = CyanaMRParser.Torsion_angle_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_torsion_angle_restraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 105
                    self.torsion_angle_restraint()

                else:
                    raise NoViableAltException(self)
                self.state = 108 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
                return self.getTokens(CyanaMRParser.Integer)
            else:
                return self.getToken(CyanaMRParser.Integer, i)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Simple_name)
            else:
                return self.getToken(CyanaMRParser.Simple_name, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.NumberContext,i)


        def Type(self):
            return self.getToken(CyanaMRParser.Type, 0)

        def Equ_op(self):
            return self.getToken(CyanaMRParser.Equ_op, 0)

        def Or(self):
            return self.getToken(CyanaMRParser.Or, 0)

        def getRuleIndex(self):
            return CyanaMRParser.RULE_torsion_angle_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTorsion_angle_restraint" ):
                listener.enterTorsion_angle_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTorsion_angle_restraint" ):
                listener.exitTorsion_angle_restraint(self)




    def torsion_angle_restraint(self):

        localctx = CyanaMRParser.Torsion_angle_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_torsion_angle_restraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(CyanaMRParser.Integer)
            self.state = 111
            self.match(CyanaMRParser.Simple_name)
            self.state = 112
            self.match(CyanaMRParser.Simple_name)
            self.state = 113
            self.number()
            self.state = 114
            self.number()
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 115
                self.number()


            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CyanaMRParser.Type:
                self.state = 118
                self.match(CyanaMRParser.Type)
                self.state = 119
                self.match(CyanaMRParser.Equ_op)
                self.state = 120
                self.match(CyanaMRParser.Integer)


            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CyanaMRParser.Or:
                self.state = 123
                self.match(CyanaMRParser.Or)


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

        def rdc_parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Rdc_parameterContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Rdc_parameterContext,i)


        def rdc_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Rdc_restraintContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Rdc_restraintContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_rdc_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRdc_restraints" ):
                listener.enterRdc_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRdc_restraints" ):
                listener.exitRdc_restraints(self)




    def rdc_restraints(self):

        localctx = CyanaMRParser.Rdc_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_rdc_restraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 126
                    self.rdc_parameter()

                else:
                    raise NoViableAltException(self)
                self.state = 129 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 132 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 131
                    self.rdc_restraint()

                else:
                    raise NoViableAltException(self)
                self.state = 134 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rdc_parameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Integer)
            else:
                return self.getToken(CyanaMRParser.Integer, i)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Float)
            else:
                return self.getToken(CyanaMRParser.Float, i)

        def getRuleIndex(self):
            return CyanaMRParser.RULE_rdc_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRdc_parameter" ):
                listener.enterRdc_parameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRdc_parameter" ):
                listener.exitRdc_parameter(self)




    def rdc_parameter(self):

        localctx = CyanaMRParser.Rdc_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_rdc_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(CyanaMRParser.Integer)
            self.state = 137
            self.match(CyanaMRParser.Float)
            self.state = 138
            self.match(CyanaMRParser.Float)
            self.state = 139
            self.match(CyanaMRParser.Integer)
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
                return self.getTokens(CyanaMRParser.Integer)
            else:
                return self.getToken(CyanaMRParser.Integer, i)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Simple_name)
            else:
                return self.getToken(CyanaMRParser.Simple_name, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.NumberContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_rdc_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRdc_restraint" ):
                listener.enterRdc_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRdc_restraint" ):
                listener.exitRdc_restraint(self)




    def rdc_restraint(self):

        localctx = CyanaMRParser.Rdc_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_rdc_restraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(CyanaMRParser.Integer)
            self.state = 142
            self.match(CyanaMRParser.Simple_name)
            self.state = 143
            self.match(CyanaMRParser.Simple_name)
            self.state = 144
            self.match(CyanaMRParser.Integer)
            self.state = 145
            self.match(CyanaMRParser.Simple_name)
            self.state = 146
            self.match(CyanaMRParser.Simple_name)
            self.state = 147
            self.number()
            self.state = 148
            self.number()
            self.state = 149
            self.number()
            self.state = 150
            self.match(CyanaMRParser.Integer)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pcs_restraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pcs_parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Pcs_parameterContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Pcs_parameterContext,i)


        def pcs_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Pcs_restraintContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Pcs_restraintContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_pcs_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPcs_restraints" ):
                listener.enterPcs_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPcs_restraints" ):
                listener.exitPcs_restraints(self)




    def pcs_restraints(self):

        localctx = CyanaMRParser.Pcs_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_pcs_restraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 152
                    self.pcs_parameter()

                else:
                    raise NoViableAltException(self)
                self.state = 155 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 158 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 157
                    self.pcs_restraint()

                else:
                    raise NoViableAltException(self)
                self.state = 160 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pcs_parameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Integer)
            else:
                return self.getToken(CyanaMRParser.Integer, i)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Float)
            else:
                return self.getToken(CyanaMRParser.Float, i)

        def getRuleIndex(self):
            return CyanaMRParser.RULE_pcs_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPcs_parameter" ):
                listener.enterPcs_parameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPcs_parameter" ):
                listener.exitPcs_parameter(self)




    def pcs_parameter(self):

        localctx = CyanaMRParser.Pcs_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_pcs_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(CyanaMRParser.Integer)
            self.state = 163
            self.match(CyanaMRParser.Float)
            self.state = 164
            self.match(CyanaMRParser.Float)
            self.state = 165
            self.match(CyanaMRParser.Integer)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pcs_restraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Integer)
            else:
                return self.getToken(CyanaMRParser.Integer, i)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Simple_name)
            else:
                return self.getToken(CyanaMRParser.Simple_name, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.NumberContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_pcs_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPcs_restraint" ):
                listener.enterPcs_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPcs_restraint" ):
                listener.exitPcs_restraint(self)




    def pcs_restraint(self):

        localctx = CyanaMRParser.Pcs_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_pcs_restraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(CyanaMRParser.Integer)
            self.state = 168
            self.match(CyanaMRParser.Simple_name)
            self.state = 169
            self.match(CyanaMRParser.Simple_name)
            self.state = 170
            self.number()
            self.state = 171
            self.number()
            self.state = 172
            self.number()
            self.state = 173
            self.match(CyanaMRParser.Integer)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fixres_distance_restraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fixres_distance_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Fixres_distance_restraintContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Fixres_distance_restraintContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_fixres_distance_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixres_distance_restraints" ):
                listener.enterFixres_distance_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixres_distance_restraints" ):
                listener.exitFixres_distance_restraints(self)




    def fixres_distance_restraints(self):

        localctx = CyanaMRParser.Fixres_distance_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_fixres_distance_restraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 175
                    self.fixres_distance_restraint()

                else:
                    raise NoViableAltException(self)
                self.state = 178 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fixres_distance_restraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Integer)
            else:
                return self.getToken(CyanaMRParser.Integer, i)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Simple_name)
            else:
                return self.getToken(CyanaMRParser.Simple_name, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.NumberContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_fixres_distance_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixres_distance_restraint" ):
                listener.enterFixres_distance_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixres_distance_restraint" ):
                listener.exitFixres_distance_restraint(self)




    def fixres_distance_restraint(self):

        localctx = CyanaMRParser.Fixres_distance_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_fixres_distance_restraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(CyanaMRParser.Integer)
            self.state = 181
            self.match(CyanaMRParser.Simple_name)
            self.state = 187 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 182
                self.match(CyanaMRParser.Simple_name)
                self.state = 183
                self.match(CyanaMRParser.Integer)
                self.state = 184
                self.match(CyanaMRParser.Simple_name)
                self.state = 185
                self.match(CyanaMRParser.Simple_name)
                self.state = 186
                self.number()
                self.state = 189 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CyanaMRParser.Simple_name):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fixresw_distance_restraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fixresw_distance_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Fixresw_distance_restraintContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Fixresw_distance_restraintContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_fixresw_distance_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixresw_distance_restraints" ):
                listener.enterFixresw_distance_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixresw_distance_restraints" ):
                listener.exitFixresw_distance_restraints(self)




    def fixresw_distance_restraints(self):

        localctx = CyanaMRParser.Fixresw_distance_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_fixresw_distance_restraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 191
                    self.fixresw_distance_restraint()

                else:
                    raise NoViableAltException(self)
                self.state = 194 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fixresw_distance_restraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Integer)
            else:
                return self.getToken(CyanaMRParser.Integer, i)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Simple_name)
            else:
                return self.getToken(CyanaMRParser.Simple_name, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.NumberContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_fixresw_distance_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixresw_distance_restraint" ):
                listener.enterFixresw_distance_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixresw_distance_restraint" ):
                listener.exitFixresw_distance_restraint(self)




    def fixresw_distance_restraint(self):

        localctx = CyanaMRParser.Fixresw_distance_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_fixresw_distance_restraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(CyanaMRParser.Integer)
            self.state = 197
            self.match(CyanaMRParser.Simple_name)
            self.state = 205 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 198
                self.match(CyanaMRParser.Simple_name)
                self.state = 199
                self.match(CyanaMRParser.Integer)
                self.state = 200
                self.match(CyanaMRParser.Simple_name)
                self.state = 201
                self.match(CyanaMRParser.Simple_name)
                self.state = 202
                self.number()
                self.state = 203
                self.number()
                self.state = 207 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CyanaMRParser.Simple_name):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fixresw2_distance_restraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fixresw2_distance_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Fixresw2_distance_restraintContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Fixresw2_distance_restraintContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_fixresw2_distance_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixresw2_distance_restraints" ):
                listener.enterFixresw2_distance_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixresw2_distance_restraints" ):
                listener.exitFixresw2_distance_restraints(self)




    def fixresw2_distance_restraints(self):

        localctx = CyanaMRParser.Fixresw2_distance_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_fixresw2_distance_restraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 209
                    self.fixresw2_distance_restraint()

                else:
                    raise NoViableAltException(self)
                self.state = 212 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fixresw2_distance_restraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Integer)
            else:
                return self.getToken(CyanaMRParser.Integer, i)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Simple_name)
            else:
                return self.getToken(CyanaMRParser.Simple_name, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.NumberContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_fixresw2_distance_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixresw2_distance_restraint" ):
                listener.enterFixresw2_distance_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixresw2_distance_restraint" ):
                listener.exitFixresw2_distance_restraint(self)




    def fixresw2_distance_restraint(self):

        localctx = CyanaMRParser.Fixresw2_distance_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_fixresw2_distance_restraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(CyanaMRParser.Integer)
            self.state = 215
            self.match(CyanaMRParser.Simple_name)
            self.state = 224 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 216
                self.match(CyanaMRParser.Simple_name)
                self.state = 217
                self.match(CyanaMRParser.Integer)
                self.state = 218
                self.match(CyanaMRParser.Simple_name)
                self.state = 219
                self.match(CyanaMRParser.Simple_name)
                self.state = 220
                self.number()
                self.state = 221
                self.number()
                self.state = 222
                self.number()
                self.state = 226 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CyanaMRParser.Simple_name):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fixatm_distance_restraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fixatm_distance_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Fixatm_distance_restraintContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Fixatm_distance_restraintContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_fixatm_distance_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixatm_distance_restraints" ):
                listener.enterFixatm_distance_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixatm_distance_restraints" ):
                listener.exitFixatm_distance_restraints(self)




    def fixatm_distance_restraints(self):

        localctx = CyanaMRParser.Fixatm_distance_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_fixatm_distance_restraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 228
                    self.fixatm_distance_restraint()

                else:
                    raise NoViableAltException(self)
                self.state = 231 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fixatm_distance_restraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Integer)
            else:
                return self.getToken(CyanaMRParser.Integer, i)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Simple_name)
            else:
                return self.getToken(CyanaMRParser.Simple_name, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.NumberContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_fixatm_distance_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixatm_distance_restraint" ):
                listener.enterFixatm_distance_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixatm_distance_restraint" ):
                listener.exitFixatm_distance_restraint(self)




    def fixatm_distance_restraint(self):

        localctx = CyanaMRParser.Fixatm_distance_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_fixatm_distance_restraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(CyanaMRParser.Integer)
            self.state = 234
            self.match(CyanaMRParser.Simple_name)
            self.state = 235
            self.match(CyanaMRParser.Simple_name)
            self.state = 240 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 236
                    self.match(CyanaMRParser.Integer)
                    self.state = 237
                    self.match(CyanaMRParser.Simple_name)
                    self.state = 238
                    self.match(CyanaMRParser.Simple_name)
                    self.state = 239
                    self.number()

                else:
                    raise NoViableAltException(self)
                self.state = 242 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fixatmw_distance_restraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fixatmw_distance_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Fixatmw_distance_restraintContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Fixatmw_distance_restraintContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_fixatmw_distance_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixatmw_distance_restraints" ):
                listener.enterFixatmw_distance_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixatmw_distance_restraints" ):
                listener.exitFixatmw_distance_restraints(self)




    def fixatmw_distance_restraints(self):

        localctx = CyanaMRParser.Fixatmw_distance_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_fixatmw_distance_restraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 244
                    self.fixatmw_distance_restraint()

                else:
                    raise NoViableAltException(self)
                self.state = 247 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fixatmw_distance_restraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Integer)
            else:
                return self.getToken(CyanaMRParser.Integer, i)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Simple_name)
            else:
                return self.getToken(CyanaMRParser.Simple_name, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.NumberContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_fixatmw_distance_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixatmw_distance_restraint" ):
                listener.enterFixatmw_distance_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixatmw_distance_restraint" ):
                listener.exitFixatmw_distance_restraint(self)




    def fixatmw_distance_restraint(self):

        localctx = CyanaMRParser.Fixatmw_distance_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_fixatmw_distance_restraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(CyanaMRParser.Integer)
            self.state = 250
            self.match(CyanaMRParser.Simple_name)
            self.state = 251
            self.match(CyanaMRParser.Simple_name)
            self.state = 258 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 252
                    self.match(CyanaMRParser.Integer)
                    self.state = 253
                    self.match(CyanaMRParser.Simple_name)
                    self.state = 254
                    self.match(CyanaMRParser.Simple_name)
                    self.state = 255
                    self.number()
                    self.state = 256
                    self.number()

                else:
                    raise NoViableAltException(self)
                self.state = 260 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fixatmw2_distance_restraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fixatmw2_distance_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Fixatmw2_distance_restraintContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Fixatmw2_distance_restraintContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_fixatmw2_distance_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixatmw2_distance_restraints" ):
                listener.enterFixatmw2_distance_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixatmw2_distance_restraints" ):
                listener.exitFixatmw2_distance_restraints(self)




    def fixatmw2_distance_restraints(self):

        localctx = CyanaMRParser.Fixatmw2_distance_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_fixatmw2_distance_restraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 262
                    self.fixatmw2_distance_restraint()

                else:
                    raise NoViableAltException(self)
                self.state = 265 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fixatmw2_distance_restraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Integer)
            else:
                return self.getToken(CyanaMRParser.Integer, i)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Simple_name)
            else:
                return self.getToken(CyanaMRParser.Simple_name, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.NumberContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_fixatmw2_distance_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixatmw2_distance_restraint" ):
                listener.enterFixatmw2_distance_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixatmw2_distance_restraint" ):
                listener.exitFixatmw2_distance_restraint(self)




    def fixatmw2_distance_restraint(self):

        localctx = CyanaMRParser.Fixatmw2_distance_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_fixatmw2_distance_restraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(CyanaMRParser.Integer)
            self.state = 268
            self.match(CyanaMRParser.Simple_name)
            self.state = 269
            self.match(CyanaMRParser.Simple_name)
            self.state = 277 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 270
                    self.match(CyanaMRParser.Integer)
                    self.state = 271
                    self.match(CyanaMRParser.Simple_name)
                    self.state = 272
                    self.match(CyanaMRParser.Simple_name)
                    self.state = 273
                    self.number()
                    self.state = 274
                    self.number()
                    self.state = 275
                    self.number()

                else:
                    raise NoViableAltException(self)
                self.state = 279 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Distance_w_chain_restraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def distance_w_chain_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Distance_w_chain_restraintContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Distance_w_chain_restraintContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_distance_w_chain_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistance_w_chain_restraints" ):
                listener.enterDistance_w_chain_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistance_w_chain_restraints" ):
                listener.exitDistance_w_chain_restraints(self)




    def distance_w_chain_restraints(self):

        localctx = CyanaMRParser.Distance_w_chain_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_distance_w_chain_restraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 281
                    self.distance_w_chain_restraint()

                else:
                    raise NoViableAltException(self)
                self.state = 284 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Distance_w_chain_restraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Integer)
            else:
                return self.getToken(CyanaMRParser.Integer, i)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Simple_name)
            else:
                return self.getToken(CyanaMRParser.Simple_name, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.NumberContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_distance_w_chain_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistance_w_chain_restraint" ):
                listener.enterDistance_w_chain_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistance_w_chain_restraint" ):
                listener.exitDistance_w_chain_restraint(self)




    def distance_w_chain_restraint(self):

        localctx = CyanaMRParser.Distance_w_chain_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_distance_w_chain_restraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(CyanaMRParser.Integer)
            self.state = 287
            self.match(CyanaMRParser.Simple_name)
            self.state = 288
            self.match(CyanaMRParser.Simple_name)
            self.state = 289
            self.match(CyanaMRParser.Simple_name)
            self.state = 290
            self.match(CyanaMRParser.Integer)
            self.state = 291
            self.match(CyanaMRParser.Simple_name)
            self.state = 292
            self.match(CyanaMRParser.Simple_name)
            self.state = 293
            self.match(CyanaMRParser.Simple_name)
            self.state = 294
            self.number()
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 295
                self.number()


            self.state = 299
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 298
                self.number()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cco_restraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cco_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.Cco_restraintContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.Cco_restraintContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_cco_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCco_restraints" ):
                listener.enterCco_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCco_restraints" ):
                listener.exitCco_restraints(self)




    def cco_restraints(self):

        localctx = CyanaMRParser.Cco_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_cco_restraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 301
                    self.cco_restraint()

                else:
                    raise NoViableAltException(self)
                self.state = 304 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cco_restraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self):
            return self.getToken(CyanaMRParser.Integer, 0)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(CyanaMRParser.Simple_name)
            else:
                return self.getToken(CyanaMRParser.Simple_name, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CyanaMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(CyanaMRParser.NumberContext,i)


        def getRuleIndex(self):
            return CyanaMRParser.RULE_cco_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCco_restraint" ):
                listener.enterCco_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCco_restraint" ):
                listener.exitCco_restraint(self)




    def cco_restraint(self):

        localctx = CyanaMRParser.Cco_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_cco_restraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(CyanaMRParser.Integer)
            self.state = 307
            self.match(CyanaMRParser.Simple_name)
            self.state = 308
            self.match(CyanaMRParser.Simple_name)
            self.state = 309
            self.match(CyanaMRParser.Simple_name)
            self.state = 310
            self.number()
            self.state = 312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 311
                self.number()


            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 314
                self.number()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ssbond_macroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Ssbond(self):
            return self.getToken(CyanaMRParser.Ssbond, 0)

        def Ssbond_resids(self):
            return self.getToken(CyanaMRParser.Ssbond_resids, 0)

        def getRuleIndex(self):
            return CyanaMRParser.RULE_ssbond_macro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSsbond_macro" ):
                listener.enterSsbond_macro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSsbond_macro" ):
                listener.exitSsbond_macro(self)




    def ssbond_macro(self):

        localctx = CyanaMRParser.Ssbond_macroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_ssbond_macro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(CyanaMRParser.Ssbond)
            self.state = 318
            self.match(CyanaMRParser.Ssbond_resids)
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
            return self.getToken(CyanaMRParser.Float, 0)

        def Integer(self):
            return self.getToken(CyanaMRParser.Integer, 0)

        def getRuleIndex(self):
            return CyanaMRParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = CyanaMRParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            _la = self._input.LA(1)
            if not(_la==CyanaMRParser.Integer or _la==CyanaMRParser.Float):
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





