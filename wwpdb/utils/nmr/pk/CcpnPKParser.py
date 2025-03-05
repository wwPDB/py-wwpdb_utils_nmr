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
        4,1,38,320,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,3,0,22,8,0,1,0,1,0,1,0,1,0,5,0,28,
        8,0,10,0,12,0,31,9,0,1,0,1,0,1,1,3,1,36,8,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,3,1,47,8,1,1,1,1,1,3,1,51,8,1,1,1,3,1,54,8,1,1,1,
        3,1,57,8,1,1,1,3,1,60,8,1,1,1,3,1,63,8,1,1,1,3,1,66,8,1,1,1,3,1,
        69,8,1,1,1,1,1,4,1,73,8,1,11,1,12,1,74,1,2,3,2,78,8,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,91,8,2,1,2,1,2,3,2,95,8,2,
        1,2,3,2,98,8,2,1,2,3,2,101,8,2,1,2,3,2,104,8,2,1,2,5,2,107,8,2,10,
        2,12,2,110,9,2,1,2,1,2,1,3,3,3,115,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,130,8,3,1,3,1,3,3,3,134,8,3,1,3,3,
        3,137,8,3,1,3,3,3,140,8,3,1,3,3,3,143,8,3,1,3,3,3,146,8,3,1,3,3,
        3,149,8,3,1,3,3,3,152,8,3,1,3,3,3,155,8,3,1,3,1,3,4,3,159,8,3,11,
        3,12,3,160,1,4,3,4,164,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,3,4,181,8,4,1,4,1,4,3,4,185,8,4,1,4,3,4,188,
        8,4,1,4,3,4,191,8,4,1,4,3,4,194,8,4,1,4,3,4,197,8,4,1,4,5,4,200,
        8,4,10,4,12,4,203,9,4,1,4,1,4,1,5,3,5,208,8,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,227,8,5,1,
        5,1,5,3,5,231,8,5,1,5,3,5,234,8,5,1,5,3,5,237,8,5,1,5,3,5,240,8,
        5,1,5,3,5,243,8,5,1,5,3,5,246,8,5,1,5,3,5,249,8,5,1,5,3,5,252,8,
        5,1,5,3,5,255,8,5,1,5,1,5,4,5,259,8,5,11,5,12,5,260,1,6,3,6,264,
        8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,3,6,285,8,6,1,6,1,6,3,6,289,8,6,1,6,3,6,292,8,6,
        1,6,3,6,295,8,6,1,6,3,6,298,8,6,1,6,3,6,301,8,6,1,6,3,6,304,8,6,
        1,6,5,6,307,8,6,10,6,12,6,310,9,6,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,
        9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,8,2,0,2,2,14,14,2,0,15,15,
        19,19,2,0,16,16,20,20,1,1,11,11,2,0,17,17,21,21,2,0,18,18,22,22,
        2,0,3,5,8,8,2,0,3,5,8,9,371,0,21,1,0,0,0,2,35,1,0,0,0,4,77,1,0,0,
        0,6,114,1,0,0,0,8,163,1,0,0,0,10,207,1,0,0,0,12,263,1,0,0,0,14,313,
        1,0,0,0,16,315,1,0,0,0,18,317,1,0,0,0,20,22,5,11,0,0,21,20,1,0,0,
        0,21,22,1,0,0,0,22,29,1,0,0,0,23,28,3,2,1,0,24,28,3,6,3,0,25,28,
        3,10,5,0,26,28,5,11,0,0,27,23,1,0,0,0,27,24,1,0,0,0,27,25,1,0,0,
        0,27,26,1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,32,
        1,0,0,0,31,29,1,0,0,0,32,33,5,0,0,1,33,1,1,0,0,0,34,36,5,1,0,0,35,
        34,1,0,0,0,35,36,1,0,0,0,36,37,1,0,0,0,37,46,7,0,0,0,38,39,7,1,0,
        0,39,40,7,2,0,0,40,41,5,23,0,0,41,47,5,24,0,0,42,43,5,23,0,0,43,
        44,5,24,0,0,44,45,7,1,0,0,45,47,7,2,0,0,46,38,1,0,0,0,46,42,1,0,
        0,0,47,48,1,0,0,0,48,50,5,27,0,0,49,51,5,28,0,0,50,49,1,0,0,0,50,
        51,1,0,0,0,51,53,1,0,0,0,52,54,5,29,0,0,53,52,1,0,0,0,53,54,1,0,
        0,0,54,56,1,0,0,0,55,57,5,30,0,0,56,55,1,0,0,0,56,57,1,0,0,0,57,
        59,1,0,0,0,58,60,5,33,0,0,59,58,1,0,0,0,59,60,1,0,0,0,60,62,1,0,
        0,0,61,63,5,34,0,0,62,61,1,0,0,0,62,63,1,0,0,0,63,65,1,0,0,0,64,
        66,5,35,0,0,65,64,1,0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,69,5,36,
        0,0,68,67,1,0,0,0,68,69,1,0,0,0,69,70,1,0,0,0,70,72,5,38,0,0,71,
        73,3,4,2,0,72,71,1,0,0,0,73,74,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,
        0,75,3,1,0,0,0,76,78,5,3,0,0,77,76,1,0,0,0,77,78,1,0,0,0,78,79,1,
        0,0,0,79,90,5,3,0,0,80,81,3,14,7,0,81,82,3,14,7,0,82,83,5,8,0,0,
        83,84,5,8,0,0,84,91,1,0,0,0,85,86,5,8,0,0,86,87,5,8,0,0,87,88,3,
        14,7,0,88,89,3,14,7,0,89,91,1,0,0,0,90,80,1,0,0,0,90,85,1,0,0,0,
        91,92,1,0,0,0,92,94,3,16,8,0,93,95,3,16,8,0,94,93,1,0,0,0,94,95,
        1,0,0,0,95,97,1,0,0,0,96,98,3,14,7,0,97,96,1,0,0,0,97,98,1,0,0,0,
        98,100,1,0,0,0,99,101,3,14,7,0,100,99,1,0,0,0,100,101,1,0,0,0,101,
        103,1,0,0,0,102,104,3,14,7,0,103,102,1,0,0,0,103,104,1,0,0,0,104,
        108,1,0,0,0,105,107,3,18,9,0,106,105,1,0,0,0,107,110,1,0,0,0,108,
        106,1,0,0,0,108,109,1,0,0,0,109,111,1,0,0,0,110,108,1,0,0,0,111,
        112,7,3,0,0,112,5,1,0,0,0,113,115,5,1,0,0,114,113,1,0,0,0,114,115,
        1,0,0,0,115,116,1,0,0,0,116,129,7,0,0,0,117,118,7,1,0,0,118,119,
        7,2,0,0,119,120,7,4,0,0,120,121,5,23,0,0,121,122,5,24,0,0,122,130,
        5,25,0,0,123,124,5,23,0,0,124,125,5,24,0,0,125,126,5,25,0,0,126,
        127,7,1,0,0,127,128,7,2,0,0,128,130,7,4,0,0,129,117,1,0,0,0,129,
        123,1,0,0,0,130,131,1,0,0,0,131,133,5,27,0,0,132,134,5,28,0,0,133,
        132,1,0,0,0,133,134,1,0,0,0,134,136,1,0,0,0,135,137,5,29,0,0,136,
        135,1,0,0,0,136,137,1,0,0,0,137,139,1,0,0,0,138,140,5,30,0,0,139,
        138,1,0,0,0,139,140,1,0,0,0,140,142,1,0,0,0,141,143,5,31,0,0,142,
        141,1,0,0,0,142,143,1,0,0,0,143,145,1,0,0,0,144,146,5,33,0,0,145,
        144,1,0,0,0,145,146,1,0,0,0,146,148,1,0,0,0,147,149,5,34,0,0,148,
        147,1,0,0,0,148,149,1,0,0,0,149,151,1,0,0,0,150,152,5,35,0,0,151,
        150,1,0,0,0,151,152,1,0,0,0,152,154,1,0,0,0,153,155,5,36,0,0,154,
        153,1,0,0,0,154,155,1,0,0,0,155,156,1,0,0,0,156,158,5,38,0,0,157,
        159,3,8,4,0,158,157,1,0,0,0,159,160,1,0,0,0,160,158,1,0,0,0,160,
        161,1,0,0,0,161,7,1,0,0,0,162,164,5,3,0,0,163,162,1,0,0,0,163,164,
        1,0,0,0,164,165,1,0,0,0,165,180,5,3,0,0,166,167,3,14,7,0,167,168,
        3,14,7,0,168,169,3,14,7,0,169,170,5,8,0,0,170,171,5,8,0,0,171,172,
        5,8,0,0,172,181,1,0,0,0,173,174,5,8,0,0,174,175,5,8,0,0,175,176,
        5,8,0,0,176,177,3,14,7,0,177,178,3,14,7,0,178,179,3,14,7,0,179,181,
        1,0,0,0,180,166,1,0,0,0,180,173,1,0,0,0,181,182,1,0,0,0,182,184,
        3,16,8,0,183,185,3,16,8,0,184,183,1,0,0,0,184,185,1,0,0,0,185,187,
        1,0,0,0,186,188,3,14,7,0,187,186,1,0,0,0,187,188,1,0,0,0,188,190,
        1,0,0,0,189,191,3,14,7,0,190,189,1,0,0,0,190,191,1,0,0,0,191,193,
        1,0,0,0,192,194,3,14,7,0,193,192,1,0,0,0,193,194,1,0,0,0,194,196,
        1,0,0,0,195,197,3,14,7,0,196,195,1,0,0,0,196,197,1,0,0,0,197,201,
        1,0,0,0,198,200,3,18,9,0,199,198,1,0,0,0,200,203,1,0,0,0,201,199,
        1,0,0,0,201,202,1,0,0,0,202,204,1,0,0,0,203,201,1,0,0,0,204,205,
        7,3,0,0,205,9,1,0,0,0,206,208,5,1,0,0,207,206,1,0,0,0,207,208,1,
        0,0,0,208,209,1,0,0,0,209,226,7,0,0,0,210,211,7,1,0,0,211,212,7,
        2,0,0,212,213,7,4,0,0,213,214,7,5,0,0,214,215,5,23,0,0,215,216,5,
        24,0,0,216,217,5,25,0,0,217,227,5,26,0,0,218,219,5,23,0,0,219,220,
        5,24,0,0,220,221,5,25,0,0,221,222,5,26,0,0,222,223,7,1,0,0,223,224,
        7,2,0,0,224,225,7,4,0,0,225,227,7,5,0,0,226,210,1,0,0,0,226,218,
        1,0,0,0,227,228,1,0,0,0,228,230,5,27,0,0,229,231,5,28,0,0,230,229,
        1,0,0,0,230,231,1,0,0,0,231,233,1,0,0,0,232,234,5,29,0,0,233,232,
        1,0,0,0,233,234,1,0,0,0,234,236,1,0,0,0,235,237,5,30,0,0,236,235,
        1,0,0,0,236,237,1,0,0,0,237,239,1,0,0,0,238,240,5,31,0,0,239,238,
        1,0,0,0,239,240,1,0,0,0,240,242,1,0,0,0,241,243,5,32,0,0,242,241,
        1,0,0,0,242,243,1,0,0,0,243,245,1,0,0,0,244,246,5,33,0,0,245,244,
        1,0,0,0,245,246,1,0,0,0,246,248,1,0,0,0,247,249,5,34,0,0,248,247,
        1,0,0,0,248,249,1,0,0,0,249,251,1,0,0,0,250,252,5,35,0,0,251,250,
        1,0,0,0,251,252,1,0,0,0,252,254,1,0,0,0,253,255,5,36,0,0,254,253,
        1,0,0,0,254,255,1,0,0,0,255,256,1,0,0,0,256,258,5,38,0,0,257,259,
        3,12,6,0,258,257,1,0,0,0,259,260,1,0,0,0,260,258,1,0,0,0,260,261,
        1,0,0,0,261,11,1,0,0,0,262,264,5,3,0,0,263,262,1,0,0,0,263,264,1,
        0,0,0,264,265,1,0,0,0,265,284,5,3,0,0,266,267,3,14,7,0,267,268,3,
        14,7,0,268,269,3,14,7,0,269,270,3,14,7,0,270,271,5,8,0,0,271,272,
        5,8,0,0,272,273,5,8,0,0,273,274,5,8,0,0,274,285,1,0,0,0,275,276,
        5,8,0,0,276,277,5,8,0,0,277,278,5,8,0,0,278,279,5,8,0,0,279,280,
        3,14,7,0,280,281,3,14,7,0,281,282,3,14,7,0,282,283,3,14,7,0,283,
        285,1,0,0,0,284,266,1,0,0,0,284,275,1,0,0,0,285,286,1,0,0,0,286,
        288,3,16,8,0,287,289,3,16,8,0,288,287,1,0,0,0,288,289,1,0,0,0,289,
        291,1,0,0,0,290,292,3,14,7,0,291,290,1,0,0,0,291,292,1,0,0,0,292,
        294,1,0,0,0,293,295,3,14,7,0,294,293,1,0,0,0,294,295,1,0,0,0,295,
        297,1,0,0,0,296,298,3,14,7,0,297,296,1,0,0,0,297,298,1,0,0,0,298,
        300,1,0,0,0,299,301,3,14,7,0,300,299,1,0,0,0,300,301,1,0,0,0,301,
        303,1,0,0,0,302,304,3,14,7,0,303,302,1,0,0,0,303,304,1,0,0,0,304,
        308,1,0,0,0,305,307,3,18,9,0,306,305,1,0,0,0,307,310,1,0,0,0,308,
        306,1,0,0,0,308,309,1,0,0,0,309,311,1,0,0,0,310,308,1,0,0,0,311,
        312,7,3,0,0,312,13,1,0,0,0,313,314,7,6,0,0,314,15,1,0,0,0,315,316,
        7,6,0,0,316,17,1,0,0,0,317,318,7,7,0,0,318,19,1,0,0,0,60,21,27,29,
        35,46,50,53,56,59,62,65,68,74,77,90,94,97,100,103,108,114,129,133,
        136,139,142,145,148,151,154,160,163,180,184,187,190,193,196,201,
        207,226,230,233,236,239,242,245,248,251,254,260,263,284,288,291,
        294,297,300,303,308
    ]

class CcpnPKParser ( Parser ):

    grammarFileName = "CcpnPKParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Number'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'Position F1'", 
                     "'Position F2'", "'Position F3'", "'Position F4'", 
                     "'Shift F1'", "'Shift F2'", "'Shift F3'", "'Shift F4'", 
                     "'Assign F1'", "'Assign F2'", "'Assign F3'", "'Assign F4'", 
                     "'Height'", "'Volume'", "'Line Width F1 (Hz)'", "'Line Width F2 (Hz)'", 
                     "'Line Width F3 (Hz)'", "'Line Width F4 (Hz)'", "'Merit'", 
                     "'Details'", "'Fit Method'", "'Vol. Method'" ]

    symbolicNames = [ "<INVALID>", "Number", "Id", "Integer", "Float", "Real", 
                      "EXCLM_COMMENT", "SMCLN_COMMENT", "Simple_name", "Any_name", 
                      "SPACE", "RETURN", "SECTION_COMMENT", "LINE_COMMENT", 
                      "Id_", "Position_F1", "Position_F2", "Position_F3", 
                      "Position_F4", "Shift_F1", "Shift_F2", "Shift_F3", 
                      "Shift_F4", "Assign_F1", "Assign_F2", "Assign_F3", 
                      "Assign_F4", "Height", "Volume", "Line_width_F1", 
                      "Line_width_F2", "Line_width_F3", "Line_width_F4", 
                      "Merit", "Details", "Fit_method", "Vol_method", "SPACE_VARS", 
                      "RETURN_VARS" ]

    RULE_ccpn_pk = 0
    RULE_peak_list_2d = 1
    RULE_peak_2d = 2
    RULE_peak_list_3d = 3
    RULE_peak_3d = 4
    RULE_peak_list_4d = 5
    RULE_peak_4d = 6
    RULE_position = 7
    RULE_number = 8
    RULE_note = 9

    ruleNames =  [ "ccpn_pk", "peak_list_2d", "peak_2d", "peak_list_3d", 
                   "peak_3d", "peak_list_4d", "peak_4d", "position", "number", 
                   "note" ]

    EOF = Token.EOF
    Number=1
    Id=2
    Integer=3
    Float=4
    Real=5
    EXCLM_COMMENT=6
    SMCLN_COMMENT=7
    Simple_name=8
    Any_name=9
    SPACE=10
    RETURN=11
    SECTION_COMMENT=12
    LINE_COMMENT=13
    Id_=14
    Position_F1=15
    Position_F2=16
    Position_F3=17
    Position_F4=18
    Shift_F1=19
    Shift_F2=20
    Shift_F3=21
    Shift_F4=22
    Assign_F1=23
    Assign_F2=24
    Assign_F3=25
    Assign_F4=26
    Height=27
    Volume=28
    Line_width_F1=29
    Line_width_F2=30
    Line_width_F3=31
    Line_width_F4=32
    Merit=33
    Details=34
    Fit_method=35
    Vol_method=36
    SPACE_VARS=37
    RETURN_VARS=38

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
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 20
                self.match(CcpnPKParser.RETURN)


            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 18438) != 0):
                self.state = 27
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 23
                    self.peak_list_2d()
                    pass

                elif la_ == 2:
                    self.state = 24
                    self.peak_list_3d()
                    pass

                elif la_ == 3:
                    self.state = 25
                    self.peak_list_4d()
                    pass

                elif la_ == 4:
                    self.state = 26
                    self.match(CcpnPKParser.RETURN)
                    pass


                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
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

        def Height(self):
            return self.getToken(CcpnPKParser.Height, 0)

        def RETURN_VARS(self):
            return self.getToken(CcpnPKParser.RETURN_VARS, 0)

        def Id(self):
            return self.getToken(CcpnPKParser.Id, 0)

        def Id_(self):
            return self.getToken(CcpnPKParser.Id_, 0)

        def Number(self):
            return self.getToken(CcpnPKParser.Number, 0)

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


        def Assign_F1(self):
            return self.getToken(CcpnPKParser.Assign_F1, 0)

        def Assign_F2(self):
            return self.getToken(CcpnPKParser.Assign_F2, 0)

        def Position_F1(self):
            return self.getToken(CcpnPKParser.Position_F1, 0)

        def Shift_F1(self):
            return self.getToken(CcpnPKParser.Shift_F1, 0)

        def Position_F2(self):
            return self.getToken(CcpnPKParser.Position_F2, 0)

        def Shift_F2(self):
            return self.getToken(CcpnPKParser.Shift_F2, 0)

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
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 34
                self.match(CcpnPKParser.Number)


            self.state = 37
            _la = self._input.LA(1)
            if not(_la==2 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 19]:
                self.state = 38
                _la = self._input.LA(1)
                if not(_la==15 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 39
                _la = self._input.LA(1)
                if not(_la==16 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 40
                self.match(CcpnPKParser.Assign_F1)
                self.state = 41
                self.match(CcpnPKParser.Assign_F2)
                pass
            elif token in [23]:
                self.state = 42
                self.match(CcpnPKParser.Assign_F1)
                self.state = 43
                self.match(CcpnPKParser.Assign_F2)
                self.state = 44
                _la = self._input.LA(1)
                if not(_la==15 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 45
                _la = self._input.LA(1)
                if not(_la==16 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 48
            self.match(CcpnPKParser.Height)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 49
                self.match(CcpnPKParser.Volume)


            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 52
                self.match(CcpnPKParser.Line_width_F1)


            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 55
                self.match(CcpnPKParser.Line_width_F2)


            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 58
                self.match(CcpnPKParser.Merit)


            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 61
                self.match(CcpnPKParser.Details)


            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 64
                self.match(CcpnPKParser.Fit_method)


            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 67
                self.match(CcpnPKParser.Vol_method)


            self.state = 70
            self.match(CcpnPKParser.RETURN_VARS)
            self.state = 72 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 71
                self.peak_2d()
                self.state = 74 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3):
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
                return self.getTokens(CcpnPKParser.Integer)
            else:
                return self.getToken(CcpnPKParser.Integer, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.NumberContext,i)


        def RETURN(self):
            return self.getToken(CcpnPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(CcpnPKParser.EOF, 0)

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
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 76
                self.match(CcpnPKParser.Integer)


            self.state = 79
            self.match(CcpnPKParser.Integer)
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 80
                self.position()
                self.state = 81
                self.position()
                self.state = 82
                self.match(CcpnPKParser.Simple_name)
                self.state = 83
                self.match(CcpnPKParser.Simple_name)
                pass

            elif la_ == 2:
                self.state = 85
                self.match(CcpnPKParser.Simple_name)
                self.state = 86
                self.match(CcpnPKParser.Simple_name)
                self.state = 87
                self.position()
                self.state = 88
                self.position()
                pass


            self.state = 92
            self.number()
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 93
                self.number()


            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 96
                self.position()


            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 99
                self.position()


            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 102
                self.position()


            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 824) != 0):
                self.state = 105
                self.note()
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 111
            _la = self._input.LA(1)
            if not(_la==-1 or _la==11):
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

        def Height(self):
            return self.getToken(CcpnPKParser.Height, 0)

        def RETURN_VARS(self):
            return self.getToken(CcpnPKParser.RETURN_VARS, 0)

        def Id(self):
            return self.getToken(CcpnPKParser.Id, 0)

        def Id_(self):
            return self.getToken(CcpnPKParser.Id_, 0)

        def Number(self):
            return self.getToken(CcpnPKParser.Number, 0)

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


        def Assign_F1(self):
            return self.getToken(CcpnPKParser.Assign_F1, 0)

        def Assign_F2(self):
            return self.getToken(CcpnPKParser.Assign_F2, 0)

        def Assign_F3(self):
            return self.getToken(CcpnPKParser.Assign_F3, 0)

        def Position_F1(self):
            return self.getToken(CcpnPKParser.Position_F1, 0)

        def Shift_F1(self):
            return self.getToken(CcpnPKParser.Shift_F1, 0)

        def Position_F2(self):
            return self.getToken(CcpnPKParser.Position_F2, 0)

        def Shift_F2(self):
            return self.getToken(CcpnPKParser.Shift_F2, 0)

        def Position_F3(self):
            return self.getToken(CcpnPKParser.Position_F3, 0)

        def Shift_F3(self):
            return self.getToken(CcpnPKParser.Shift_F3, 0)

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
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 113
                self.match(CcpnPKParser.Number)


            self.state = 116
            _la = self._input.LA(1)
            if not(_la==2 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 19]:
                self.state = 117
                _la = self._input.LA(1)
                if not(_la==15 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 118
                _la = self._input.LA(1)
                if not(_la==16 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 119
                _la = self._input.LA(1)
                if not(_la==17 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 120
                self.match(CcpnPKParser.Assign_F1)
                self.state = 121
                self.match(CcpnPKParser.Assign_F2)
                self.state = 122
                self.match(CcpnPKParser.Assign_F3)
                pass
            elif token in [23]:
                self.state = 123
                self.match(CcpnPKParser.Assign_F1)
                self.state = 124
                self.match(CcpnPKParser.Assign_F2)
                self.state = 125
                self.match(CcpnPKParser.Assign_F3)
                self.state = 126
                _la = self._input.LA(1)
                if not(_la==15 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 127
                _la = self._input.LA(1)
                if not(_la==16 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 128
                _la = self._input.LA(1)
                if not(_la==17 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 131
            self.match(CcpnPKParser.Height)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 132
                self.match(CcpnPKParser.Volume)


            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 135
                self.match(CcpnPKParser.Line_width_F1)


            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 138
                self.match(CcpnPKParser.Line_width_F2)


            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 141
                self.match(CcpnPKParser.Line_width_F3)


            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 144
                self.match(CcpnPKParser.Merit)


            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 147
                self.match(CcpnPKParser.Details)


            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 150
                self.match(CcpnPKParser.Fit_method)


            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 153
                self.match(CcpnPKParser.Vol_method)


            self.state = 156
            self.match(CcpnPKParser.RETURN_VARS)
            self.state = 158 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 157
                self.peak_3d()
                self.state = 160 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3):
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
                return self.getTokens(CcpnPKParser.Integer)
            else:
                return self.getToken(CcpnPKParser.Integer, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.NumberContext,i)


        def RETURN(self):
            return self.getToken(CcpnPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(CcpnPKParser.EOF, 0)

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
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 162
                self.match(CcpnPKParser.Integer)


            self.state = 165
            self.match(CcpnPKParser.Integer)
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 166
                self.position()
                self.state = 167
                self.position()
                self.state = 168
                self.position()
                self.state = 169
                self.match(CcpnPKParser.Simple_name)
                self.state = 170
                self.match(CcpnPKParser.Simple_name)
                self.state = 171
                self.match(CcpnPKParser.Simple_name)
                pass

            elif la_ == 2:
                self.state = 173
                self.match(CcpnPKParser.Simple_name)
                self.state = 174
                self.match(CcpnPKParser.Simple_name)
                self.state = 175
                self.match(CcpnPKParser.Simple_name)
                self.state = 176
                self.position()
                self.state = 177
                self.position()
                self.state = 178
                self.position()
                pass


            self.state = 182
            self.number()
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 183
                self.number()


            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 186
                self.position()


            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 189
                self.position()


            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 192
                self.position()


            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 195
                self.position()


            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 824) != 0):
                self.state = 198
                self.note()
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 204
            _la = self._input.LA(1)
            if not(_la==-1 or _la==11):
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

        def Height(self):
            return self.getToken(CcpnPKParser.Height, 0)

        def RETURN_VARS(self):
            return self.getToken(CcpnPKParser.RETURN_VARS, 0)

        def Id(self):
            return self.getToken(CcpnPKParser.Id, 0)

        def Id_(self):
            return self.getToken(CcpnPKParser.Id_, 0)

        def Number(self):
            return self.getToken(CcpnPKParser.Number, 0)

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


        def Assign_F1(self):
            return self.getToken(CcpnPKParser.Assign_F1, 0)

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
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 206
                self.match(CcpnPKParser.Number)


            self.state = 209
            _la = self._input.LA(1)
            if not(_la==2 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 19]:
                self.state = 210
                _la = self._input.LA(1)
                if not(_la==15 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 211
                _la = self._input.LA(1)
                if not(_la==16 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 212
                _la = self._input.LA(1)
                if not(_la==17 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 213
                _la = self._input.LA(1)
                if not(_la==18 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 214
                self.match(CcpnPKParser.Assign_F1)
                self.state = 215
                self.match(CcpnPKParser.Assign_F2)
                self.state = 216
                self.match(CcpnPKParser.Assign_F3)
                self.state = 217
                self.match(CcpnPKParser.Assign_F4)
                pass
            elif token in [23]:
                self.state = 218
                self.match(CcpnPKParser.Assign_F1)
                self.state = 219
                self.match(CcpnPKParser.Assign_F2)
                self.state = 220
                self.match(CcpnPKParser.Assign_F3)
                self.state = 221
                self.match(CcpnPKParser.Assign_F4)
                self.state = 222
                _la = self._input.LA(1)
                if not(_la==15 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 223
                _la = self._input.LA(1)
                if not(_la==16 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 224
                _la = self._input.LA(1)
                if not(_la==17 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 225
                _la = self._input.LA(1)
                if not(_la==18 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 228
            self.match(CcpnPKParser.Height)
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 229
                self.match(CcpnPKParser.Volume)


            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 232
                self.match(CcpnPKParser.Line_width_F1)


            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 235
                self.match(CcpnPKParser.Line_width_F2)


            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 238
                self.match(CcpnPKParser.Line_width_F3)


            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 241
                self.match(CcpnPKParser.Line_width_F4)


            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 244
                self.match(CcpnPKParser.Merit)


            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 247
                self.match(CcpnPKParser.Details)


            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 250
                self.match(CcpnPKParser.Fit_method)


            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 253
                self.match(CcpnPKParser.Vol_method)


            self.state = 256
            self.match(CcpnPKParser.RETURN_VARS)
            self.state = 258 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 257
                self.peak_4d()
                self.state = 260 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3):
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
                return self.getTokens(CcpnPKParser.Integer)
            else:
                return self.getToken(CcpnPKParser.Integer, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.NumberContext,i)


        def RETURN(self):
            return self.getToken(CcpnPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(CcpnPKParser.EOF, 0)

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
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.state = 262
                self.match(CcpnPKParser.Integer)


            self.state = 265
            self.match(CcpnPKParser.Integer)
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.state = 266
                self.position()
                self.state = 267
                self.position()
                self.state = 268
                self.position()
                self.state = 269
                self.position()
                self.state = 270
                self.match(CcpnPKParser.Simple_name)
                self.state = 271
                self.match(CcpnPKParser.Simple_name)
                self.state = 272
                self.match(CcpnPKParser.Simple_name)
                self.state = 273
                self.match(CcpnPKParser.Simple_name)
                pass

            elif la_ == 2:
                self.state = 275
                self.match(CcpnPKParser.Simple_name)
                self.state = 276
                self.match(CcpnPKParser.Simple_name)
                self.state = 277
                self.match(CcpnPKParser.Simple_name)
                self.state = 278
                self.match(CcpnPKParser.Simple_name)
                self.state = 279
                self.position()
                self.state = 280
                self.position()
                self.state = 281
                self.position()
                self.state = 282
                self.position()
                pass


            self.state = 286
            self.number()
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.state = 287
                self.number()


            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.state = 290
                self.position()


            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.state = 293
                self.position()


            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.state = 296
                self.position()


            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.state = 299
                self.position()


            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.state = 302
                self.position()


            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 824) != 0):
                self.state = 305
                self.note()
                self.state = 310
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 311
            _la = self._input.LA(1)
            if not(_la==-1 or _la==11):
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
        self.enterRule(localctx, 14, self.RULE_position)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 312) != 0)):
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
        self.enterRule(localctx, 16, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 312) != 0)):
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
        self.enterRule(localctx, 18, self.RULE_note)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 824) != 0)):
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





