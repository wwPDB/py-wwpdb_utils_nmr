# Generated from CcpnNPKParser.g4 by ANTLR 4.13.0
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
        4,1,38,296,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,3,0,22,8,0,1,0,1,0,1,0,1,0,5,0,28,
        8,0,10,0,12,0,31,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,
        43,8,1,1,1,1,1,3,1,47,8,1,1,1,3,1,50,8,1,1,1,3,1,53,8,1,1,1,3,1,
        56,8,1,1,1,3,1,59,8,1,1,1,3,1,62,8,1,1,1,3,1,65,8,1,1,1,1,1,4,1,
        69,8,1,11,1,12,1,70,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,
        83,8,2,1,2,1,2,3,2,87,8,2,1,2,3,2,90,8,2,1,2,3,2,93,8,2,1,2,3,2,
        96,8,2,1,2,5,2,99,8,2,10,2,12,2,102,9,2,1,2,1,2,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,118,8,3,1,3,1,3,3,3,122,8,3,
        1,3,3,3,125,8,3,1,3,3,3,128,8,3,1,3,3,3,131,8,3,1,3,3,3,134,8,3,
        1,3,3,3,137,8,3,1,3,3,3,140,8,3,1,3,3,3,143,8,3,1,3,1,3,4,3,147,
        8,3,11,3,12,3,148,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,3,4,165,8,4,1,4,1,4,3,4,169,8,4,1,4,3,4,172,8,4,1,4,3,
        4,175,8,4,1,4,3,4,178,8,4,1,4,3,4,181,8,4,1,4,5,4,184,8,4,10,4,12,
        4,187,9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,3,5,207,8,5,1,5,1,5,3,5,211,8,5,1,5,3,5,214,8,
        5,1,5,3,5,217,8,5,1,5,3,5,220,8,5,1,5,3,5,223,8,5,1,5,3,5,226,8,
        5,1,5,3,5,229,8,5,1,5,3,5,232,8,5,1,5,3,5,235,8,5,1,5,1,5,4,5,239,
        8,5,11,5,12,5,240,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,261,8,6,1,6,1,6,3,6,265,8,6,1,6,3,
        6,268,8,6,1,6,3,6,271,8,6,1,6,3,6,274,8,6,1,6,3,6,277,8,6,1,6,3,
        6,280,8,6,1,6,5,6,283,8,6,10,6,12,6,286,9,6,1,6,1,6,1,7,1,7,1,8,
        1,8,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,8,1,0,2,3,2,0,
        16,16,20,20,2,0,15,15,19,19,1,1,12,12,2,0,17,17,21,21,2,0,18,18,
        22,22,2,0,4,6,9,9,2,0,4,6,9,10,341,0,21,1,0,0,0,2,42,1,0,0,0,4,82,
        1,0,0,0,6,117,1,0,0,0,8,164,1,0,0,0,10,206,1,0,0,0,12,260,1,0,0,
        0,14,289,1,0,0,0,16,291,1,0,0,0,18,293,1,0,0,0,20,22,5,12,0,0,21,
        20,1,0,0,0,21,22,1,0,0,0,22,29,1,0,0,0,23,28,3,2,1,0,24,28,3,6,3,
        0,25,28,3,10,5,0,26,28,5,12,0,0,27,23,1,0,0,0,27,24,1,0,0,0,27,25,
        1,0,0,0,27,26,1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,
        30,32,1,0,0,0,31,29,1,0,0,0,32,33,5,0,0,1,33,1,1,0,0,0,34,35,7,0,
        0,0,35,36,7,1,0,0,36,37,5,23,0,0,37,43,5,24,0,0,38,39,5,1,0,0,39,
        40,5,24,0,0,40,41,7,2,0,0,41,43,7,1,0,0,42,34,1,0,0,0,42,38,1,0,
        0,0,43,44,1,0,0,0,44,46,5,27,0,0,45,47,5,28,0,0,46,45,1,0,0,0,46,
        47,1,0,0,0,47,49,1,0,0,0,48,50,5,29,0,0,49,48,1,0,0,0,49,50,1,0,
        0,0,50,52,1,0,0,0,51,53,5,30,0,0,52,51,1,0,0,0,52,53,1,0,0,0,53,
        55,1,0,0,0,54,56,5,33,0,0,55,54,1,0,0,0,55,56,1,0,0,0,56,58,1,0,
        0,0,57,59,5,34,0,0,58,57,1,0,0,0,58,59,1,0,0,0,59,61,1,0,0,0,60,
        62,5,35,0,0,61,60,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,65,5,36,
        0,0,64,63,1,0,0,0,64,65,1,0,0,0,65,66,1,0,0,0,66,68,5,38,0,0,67,
        69,3,4,2,0,68,67,1,0,0,0,69,70,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,
        0,71,3,1,0,0,0,72,73,3,14,7,0,73,74,3,14,7,0,74,75,5,9,0,0,75,76,
        5,9,0,0,76,83,1,0,0,0,77,78,5,9,0,0,78,79,5,9,0,0,79,80,3,14,7,0,
        80,81,3,14,7,0,81,83,1,0,0,0,82,72,1,0,0,0,82,77,1,0,0,0,83,84,1,
        0,0,0,84,86,3,16,8,0,85,87,3,16,8,0,86,85,1,0,0,0,86,87,1,0,0,0,
        87,89,1,0,0,0,88,90,3,14,7,0,89,88,1,0,0,0,89,90,1,0,0,0,90,92,1,
        0,0,0,91,93,3,14,7,0,92,91,1,0,0,0,92,93,1,0,0,0,93,95,1,0,0,0,94,
        96,3,14,7,0,95,94,1,0,0,0,95,96,1,0,0,0,96,100,1,0,0,0,97,99,3,18,
        9,0,98,97,1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,
        101,103,1,0,0,0,102,100,1,0,0,0,103,104,7,3,0,0,104,5,1,0,0,0,105,
        106,7,0,0,0,106,107,7,1,0,0,107,108,7,4,0,0,108,109,5,23,0,0,109,
        110,5,24,0,0,110,118,5,25,0,0,111,112,5,1,0,0,112,113,5,24,0,0,113,
        114,5,25,0,0,114,115,7,2,0,0,115,116,7,1,0,0,116,118,7,4,0,0,117,
        105,1,0,0,0,117,111,1,0,0,0,118,119,1,0,0,0,119,121,5,27,0,0,120,
        122,5,28,0,0,121,120,1,0,0,0,121,122,1,0,0,0,122,124,1,0,0,0,123,
        125,5,29,0,0,124,123,1,0,0,0,124,125,1,0,0,0,125,127,1,0,0,0,126,
        128,5,30,0,0,127,126,1,0,0,0,127,128,1,0,0,0,128,130,1,0,0,0,129,
        131,5,31,0,0,130,129,1,0,0,0,130,131,1,0,0,0,131,133,1,0,0,0,132,
        134,5,33,0,0,133,132,1,0,0,0,133,134,1,0,0,0,134,136,1,0,0,0,135,
        137,5,34,0,0,136,135,1,0,0,0,136,137,1,0,0,0,137,139,1,0,0,0,138,
        140,5,35,0,0,139,138,1,0,0,0,139,140,1,0,0,0,140,142,1,0,0,0,141,
        143,5,36,0,0,142,141,1,0,0,0,142,143,1,0,0,0,143,144,1,0,0,0,144,
        146,5,38,0,0,145,147,3,8,4,0,146,145,1,0,0,0,147,148,1,0,0,0,148,
        146,1,0,0,0,148,149,1,0,0,0,149,7,1,0,0,0,150,151,3,14,7,0,151,152,
        3,14,7,0,152,153,3,14,7,0,153,154,5,9,0,0,154,155,5,9,0,0,155,156,
        5,9,0,0,156,165,1,0,0,0,157,158,5,9,0,0,158,159,5,9,0,0,159,160,
        5,9,0,0,160,161,3,14,7,0,161,162,3,14,7,0,162,163,3,14,7,0,163,165,
        1,0,0,0,164,150,1,0,0,0,164,157,1,0,0,0,165,166,1,0,0,0,166,168,
        3,16,8,0,167,169,3,16,8,0,168,167,1,0,0,0,168,169,1,0,0,0,169,171,
        1,0,0,0,170,172,3,14,7,0,171,170,1,0,0,0,171,172,1,0,0,0,172,174,
        1,0,0,0,173,175,3,14,7,0,174,173,1,0,0,0,174,175,1,0,0,0,175,177,
        1,0,0,0,176,178,3,14,7,0,177,176,1,0,0,0,177,178,1,0,0,0,178,180,
        1,0,0,0,179,181,3,14,7,0,180,179,1,0,0,0,180,181,1,0,0,0,181,185,
        1,0,0,0,182,184,3,18,9,0,183,182,1,0,0,0,184,187,1,0,0,0,185,183,
        1,0,0,0,185,186,1,0,0,0,186,188,1,0,0,0,187,185,1,0,0,0,188,189,
        7,3,0,0,189,9,1,0,0,0,190,191,7,0,0,0,191,192,7,1,0,0,192,193,7,
        4,0,0,193,194,7,5,0,0,194,195,5,23,0,0,195,196,5,24,0,0,196,197,
        5,25,0,0,197,207,5,26,0,0,198,199,5,1,0,0,199,200,5,24,0,0,200,201,
        5,25,0,0,201,202,5,26,0,0,202,203,7,2,0,0,203,204,7,1,0,0,204,205,
        7,4,0,0,205,207,7,5,0,0,206,190,1,0,0,0,206,198,1,0,0,0,207,208,
        1,0,0,0,208,210,5,27,0,0,209,211,5,28,0,0,210,209,1,0,0,0,210,211,
        1,0,0,0,211,213,1,0,0,0,212,214,5,29,0,0,213,212,1,0,0,0,213,214,
        1,0,0,0,214,216,1,0,0,0,215,217,5,30,0,0,216,215,1,0,0,0,216,217,
        1,0,0,0,217,219,1,0,0,0,218,220,5,31,0,0,219,218,1,0,0,0,219,220,
        1,0,0,0,220,222,1,0,0,0,221,223,5,32,0,0,222,221,1,0,0,0,222,223,
        1,0,0,0,223,225,1,0,0,0,224,226,5,33,0,0,225,224,1,0,0,0,225,226,
        1,0,0,0,226,228,1,0,0,0,227,229,5,34,0,0,228,227,1,0,0,0,228,229,
        1,0,0,0,229,231,1,0,0,0,230,232,5,35,0,0,231,230,1,0,0,0,231,232,
        1,0,0,0,232,234,1,0,0,0,233,235,5,36,0,0,234,233,1,0,0,0,234,235,
        1,0,0,0,235,236,1,0,0,0,236,238,5,38,0,0,237,239,3,12,6,0,238,237,
        1,0,0,0,239,240,1,0,0,0,240,238,1,0,0,0,240,241,1,0,0,0,241,11,1,
        0,0,0,242,243,3,14,7,0,243,244,3,14,7,0,244,245,3,14,7,0,245,246,
        3,14,7,0,246,247,5,9,0,0,247,248,5,9,0,0,248,249,5,9,0,0,249,250,
        5,9,0,0,250,261,1,0,0,0,251,252,5,9,0,0,252,253,5,9,0,0,253,254,
        5,9,0,0,254,255,5,9,0,0,255,256,3,14,7,0,256,257,3,14,7,0,257,258,
        3,14,7,0,258,259,3,14,7,0,259,261,1,0,0,0,260,242,1,0,0,0,260,251,
        1,0,0,0,261,262,1,0,0,0,262,264,3,16,8,0,263,265,3,16,8,0,264,263,
        1,0,0,0,264,265,1,0,0,0,265,267,1,0,0,0,266,268,3,14,7,0,267,266,
        1,0,0,0,267,268,1,0,0,0,268,270,1,0,0,0,269,271,3,14,7,0,270,269,
        1,0,0,0,270,271,1,0,0,0,271,273,1,0,0,0,272,274,3,14,7,0,273,272,
        1,0,0,0,273,274,1,0,0,0,274,276,1,0,0,0,275,277,3,14,7,0,276,275,
        1,0,0,0,276,277,1,0,0,0,277,279,1,0,0,0,278,280,3,14,7,0,279,278,
        1,0,0,0,279,280,1,0,0,0,280,284,1,0,0,0,281,283,3,18,9,0,282,281,
        1,0,0,0,283,286,1,0,0,0,284,282,1,0,0,0,284,285,1,0,0,0,285,287,
        1,0,0,0,286,284,1,0,0,0,287,288,7,3,0,0,288,13,1,0,0,0,289,290,7,
        6,0,0,290,15,1,0,0,0,291,292,7,6,0,0,292,17,1,0,0,0,293,294,7,7,
        0,0,294,19,1,0,0,0,54,21,27,29,42,46,49,52,55,58,61,64,70,82,86,
        89,92,95,100,117,121,124,127,130,133,136,139,142,148,164,168,171,
        174,177,180,185,206,210,213,216,219,222,225,228,231,234,240,260,
        264,267,270,273,276,279,284
    ]

class CcpnNPKParser ( Parser ):

    grammarFileName = "CcpnNPKParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Position F2'", "'Position F3'", "'Position F4'", 
                     "<INVALID>", "'Shift F2'", "'Shift F3'", "'Shift F4'", 
                     "<INVALID>", "'Assign F2'", "'Assign F3'", "'Assign F4'", 
                     "'Height'", "'Volume'", "'Line Width F1 (Hz)'", "'Line Width F2 (Hz)'", 
                     "'Line Width F3 (Hz)'", "'Line Width F4 (Hz)'", "'Merit'", 
                     "'Details'", "'Fit Method'", "'Vol. Method'" ]

    symbolicNames = [ "<INVALID>", "Assign_F1", "Position_F1", "Shift_F1", 
                      "Integer", "Float", "Real", "EXCLM_COMMENT", "SMCLN_COMMENT", 
                      "Simple_name", "Any_name", "SPACE", "RETURN", "SECTION_COMMENT", 
                      "LINE_COMMENT", "Position_F1_", "Position_F2", "Position_F3", 
                      "Position_F4", "Shift_F1_", "Shift_F2", "Shift_F3", 
                      "Shift_F4", "Assign_F1_", "Assign_F2", "Assign_F3", 
                      "Assign_F4", "Height", "Volume", "Line_width_F1", 
                      "Line_width_F2", "Line_width_F3", "Line_width_F4", 
                      "Merit", "Details", "Fit_method", "Vol_method", "SPACE_VARS", 
                      "RETURN_VARS" ]

    RULE_ccpn_npk = 0
    RULE_peak_list_2d = 1
    RULE_peak_2d = 2
    RULE_peak_list_3d = 3
    RULE_peak_3d = 4
    RULE_peak_list_4d = 5
    RULE_peak_4d = 6
    RULE_position = 7
    RULE_number = 8
    RULE_note = 9

    ruleNames =  [ "ccpn_npk", "peak_list_2d", "peak_2d", "peak_list_3d", 
                   "peak_3d", "peak_list_4d", "peak_4d", "position", "number", 
                   "note" ]

    EOF = Token.EOF
    Assign_F1=1
    Position_F1=2
    Shift_F1=3
    Integer=4
    Float=5
    Real=6
    EXCLM_COMMENT=7
    SMCLN_COMMENT=8
    Simple_name=9
    Any_name=10
    SPACE=11
    RETURN=12
    SECTION_COMMENT=13
    LINE_COMMENT=14
    Position_F1_=15
    Position_F2=16
    Position_F3=17
    Position_F4=18
    Shift_F1_=19
    Shift_F2=20
    Shift_F3=21
    Shift_F4=22
    Assign_F1_=23
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




    class Ccpn_npkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CcpnNPKParser.EOF, 0)

        def RETURN(self, i:int=None):
            if i is None:
                return self.getTokens(CcpnNPKParser.RETURN)
            else:
                return self.getToken(CcpnNPKParser.RETURN, i)

        def peak_list_2d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnNPKParser.Peak_list_2dContext)
            else:
                return self.getTypedRuleContext(CcpnNPKParser.Peak_list_2dContext,i)


        def peak_list_3d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnNPKParser.Peak_list_3dContext)
            else:
                return self.getTypedRuleContext(CcpnNPKParser.Peak_list_3dContext,i)


        def peak_list_4d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnNPKParser.Peak_list_4dContext)
            else:
                return self.getTypedRuleContext(CcpnNPKParser.Peak_list_4dContext,i)


        def getRuleIndex(self):
            return CcpnNPKParser.RULE_ccpn_npk

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCcpn_npk" ):
                listener.enterCcpn_npk(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCcpn_npk" ):
                listener.exitCcpn_npk(self)




    def ccpn_npk(self):

        localctx = CcpnNPKParser.Ccpn_npkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_ccpn_npk)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 20
                self.match(CcpnNPKParser.RETURN)


            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4110) != 0):
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
                    self.match(CcpnNPKParser.RETURN)
                    pass


                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
            self.match(CcpnNPKParser.EOF)
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
            return self.getToken(CcpnNPKParser.Height, 0)

        def RETURN_VARS(self):
            return self.getToken(CcpnNPKParser.RETURN_VARS, 0)

        def Volume(self):
            return self.getToken(CcpnNPKParser.Volume, 0)

        def Line_width_F1(self):
            return self.getToken(CcpnNPKParser.Line_width_F1, 0)

        def Line_width_F2(self):
            return self.getToken(CcpnNPKParser.Line_width_F2, 0)

        def Merit(self):
            return self.getToken(CcpnNPKParser.Merit, 0)

        def Details(self):
            return self.getToken(CcpnNPKParser.Details, 0)

        def Fit_method(self):
            return self.getToken(CcpnNPKParser.Fit_method, 0)

        def Vol_method(self):
            return self.getToken(CcpnNPKParser.Vol_method, 0)

        def peak_2d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnNPKParser.Peak_2dContext)
            else:
                return self.getTypedRuleContext(CcpnNPKParser.Peak_2dContext,i)


        def Assign_F1_(self):
            return self.getToken(CcpnNPKParser.Assign_F1_, 0)

        def Assign_F2(self):
            return self.getToken(CcpnNPKParser.Assign_F2, 0)

        def Assign_F1(self):
            return self.getToken(CcpnNPKParser.Assign_F1, 0)

        def Position_F1(self):
            return self.getToken(CcpnNPKParser.Position_F1, 0)

        def Shift_F1(self):
            return self.getToken(CcpnNPKParser.Shift_F1, 0)

        def Position_F2(self):
            return self.getToken(CcpnNPKParser.Position_F2, 0)

        def Shift_F2(self):
            return self.getToken(CcpnNPKParser.Shift_F2, 0)

        def Position_F1_(self):
            return self.getToken(CcpnNPKParser.Position_F1_, 0)

        def Shift_F1_(self):
            return self.getToken(CcpnNPKParser.Shift_F1_, 0)

        def getRuleIndex(self):
            return CcpnNPKParser.RULE_peak_list_2d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_list_2d" ):
                listener.enterPeak_list_2d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_list_2d" ):
                listener.exitPeak_list_2d(self)




    def peak_list_2d(self):

        localctx = CcpnNPKParser.Peak_list_2dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_peak_list_2d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3]:
                self.state = 34
                _la = self._input.LA(1)
                if not(_la==2 or _la==3):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 35
                _la = self._input.LA(1)
                if not(_la==16 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 36
                self.match(CcpnNPKParser.Assign_F1_)
                self.state = 37
                self.match(CcpnNPKParser.Assign_F2)
                pass
            elif token in [1]:
                self.state = 38
                self.match(CcpnNPKParser.Assign_F1)
                self.state = 39
                self.match(CcpnNPKParser.Assign_F2)
                self.state = 40
                _la = self._input.LA(1)
                if not(_la==15 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 41
                _la = self._input.LA(1)
                if not(_la==16 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 44
            self.match(CcpnNPKParser.Height)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 45
                self.match(CcpnNPKParser.Volume)


            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 48
                self.match(CcpnNPKParser.Line_width_F1)


            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 51
                self.match(CcpnNPKParser.Line_width_F2)


            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 54
                self.match(CcpnNPKParser.Merit)


            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 57
                self.match(CcpnNPKParser.Details)


            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 60
                self.match(CcpnNPKParser.Fit_method)


            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 63
                self.match(CcpnNPKParser.Vol_method)


            self.state = 66
            self.match(CcpnNPKParser.RETURN_VARS)
            self.state = 68 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 67
                self.peak_2d()
                self.state = 70 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 624) != 0)):
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

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnNPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(CcpnNPKParser.NumberContext,i)


        def RETURN(self):
            return self.getToken(CcpnNPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(CcpnNPKParser.EOF, 0)

        def position(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnNPKParser.PositionContext)
            else:
                return self.getTypedRuleContext(CcpnNPKParser.PositionContext,i)


        def note(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnNPKParser.NoteContext)
            else:
                return self.getTypedRuleContext(CcpnNPKParser.NoteContext,i)


        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(CcpnNPKParser.Simple_name)
            else:
                return self.getToken(CcpnNPKParser.Simple_name, i)

        def getRuleIndex(self):
            return CcpnNPKParser.RULE_peak_2d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_2d" ):
                listener.enterPeak_2d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_2d" ):
                listener.exitPeak_2d(self)




    def peak_2d(self):

        localctx = CcpnNPKParser.Peak_2dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_peak_2d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 72
                self.position()
                self.state = 73
                self.position()
                self.state = 74
                self.match(CcpnNPKParser.Simple_name)
                self.state = 75
                self.match(CcpnNPKParser.Simple_name)
                pass

            elif la_ == 2:
                self.state = 77
                self.match(CcpnNPKParser.Simple_name)
                self.state = 78
                self.match(CcpnNPKParser.Simple_name)
                self.state = 79
                self.position()
                self.state = 80
                self.position()
                pass


            self.state = 84
            self.number()
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 85
                self.number()


            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 88
                self.position()


            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 91
                self.position()


            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 94
                self.position()


            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1648) != 0):
                self.state = 97
                self.note()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 103
            _la = self._input.LA(1)
            if not(_la==-1 or _la==12):
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
            return self.getToken(CcpnNPKParser.Height, 0)

        def RETURN_VARS(self):
            return self.getToken(CcpnNPKParser.RETURN_VARS, 0)

        def Volume(self):
            return self.getToken(CcpnNPKParser.Volume, 0)

        def Line_width_F1(self):
            return self.getToken(CcpnNPKParser.Line_width_F1, 0)

        def Line_width_F2(self):
            return self.getToken(CcpnNPKParser.Line_width_F2, 0)

        def Line_width_F3(self):
            return self.getToken(CcpnNPKParser.Line_width_F3, 0)

        def Merit(self):
            return self.getToken(CcpnNPKParser.Merit, 0)

        def Details(self):
            return self.getToken(CcpnNPKParser.Details, 0)

        def Fit_method(self):
            return self.getToken(CcpnNPKParser.Fit_method, 0)

        def Vol_method(self):
            return self.getToken(CcpnNPKParser.Vol_method, 0)

        def peak_3d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnNPKParser.Peak_3dContext)
            else:
                return self.getTypedRuleContext(CcpnNPKParser.Peak_3dContext,i)


        def Assign_F1_(self):
            return self.getToken(CcpnNPKParser.Assign_F1_, 0)

        def Assign_F2(self):
            return self.getToken(CcpnNPKParser.Assign_F2, 0)

        def Assign_F3(self):
            return self.getToken(CcpnNPKParser.Assign_F3, 0)

        def Assign_F1(self):
            return self.getToken(CcpnNPKParser.Assign_F1, 0)

        def Position_F1(self):
            return self.getToken(CcpnNPKParser.Position_F1, 0)

        def Shift_F1(self):
            return self.getToken(CcpnNPKParser.Shift_F1, 0)

        def Position_F2(self):
            return self.getToken(CcpnNPKParser.Position_F2, 0)

        def Shift_F2(self):
            return self.getToken(CcpnNPKParser.Shift_F2, 0)

        def Position_F3(self):
            return self.getToken(CcpnNPKParser.Position_F3, 0)

        def Shift_F3(self):
            return self.getToken(CcpnNPKParser.Shift_F3, 0)

        def Position_F1_(self):
            return self.getToken(CcpnNPKParser.Position_F1_, 0)

        def Shift_F1_(self):
            return self.getToken(CcpnNPKParser.Shift_F1_, 0)

        def getRuleIndex(self):
            return CcpnNPKParser.RULE_peak_list_3d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_list_3d" ):
                listener.enterPeak_list_3d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_list_3d" ):
                listener.exitPeak_list_3d(self)




    def peak_list_3d(self):

        localctx = CcpnNPKParser.Peak_list_3dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_peak_list_3d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3]:
                self.state = 105
                _la = self._input.LA(1)
                if not(_la==2 or _la==3):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 106
                _la = self._input.LA(1)
                if not(_la==16 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 107
                _la = self._input.LA(1)
                if not(_la==17 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 108
                self.match(CcpnNPKParser.Assign_F1_)
                self.state = 109
                self.match(CcpnNPKParser.Assign_F2)
                self.state = 110
                self.match(CcpnNPKParser.Assign_F3)
                pass
            elif token in [1]:
                self.state = 111
                self.match(CcpnNPKParser.Assign_F1)
                self.state = 112
                self.match(CcpnNPKParser.Assign_F2)
                self.state = 113
                self.match(CcpnNPKParser.Assign_F3)
                self.state = 114
                _la = self._input.LA(1)
                if not(_la==15 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 115
                _la = self._input.LA(1)
                if not(_la==16 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 116
                _la = self._input.LA(1)
                if not(_la==17 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 119
            self.match(CcpnNPKParser.Height)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 120
                self.match(CcpnNPKParser.Volume)


            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 123
                self.match(CcpnNPKParser.Line_width_F1)


            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 126
                self.match(CcpnNPKParser.Line_width_F2)


            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 129
                self.match(CcpnNPKParser.Line_width_F3)


            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 132
                self.match(CcpnNPKParser.Merit)


            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 135
                self.match(CcpnNPKParser.Details)


            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 138
                self.match(CcpnNPKParser.Fit_method)


            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 141
                self.match(CcpnNPKParser.Vol_method)


            self.state = 144
            self.match(CcpnNPKParser.RETURN_VARS)
            self.state = 146 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 145
                self.peak_3d()
                self.state = 148 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 624) != 0)):
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

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnNPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(CcpnNPKParser.NumberContext,i)


        def RETURN(self):
            return self.getToken(CcpnNPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(CcpnNPKParser.EOF, 0)

        def position(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnNPKParser.PositionContext)
            else:
                return self.getTypedRuleContext(CcpnNPKParser.PositionContext,i)


        def note(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnNPKParser.NoteContext)
            else:
                return self.getTypedRuleContext(CcpnNPKParser.NoteContext,i)


        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(CcpnNPKParser.Simple_name)
            else:
                return self.getToken(CcpnNPKParser.Simple_name, i)

        def getRuleIndex(self):
            return CcpnNPKParser.RULE_peak_3d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_3d" ):
                listener.enterPeak_3d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_3d" ):
                listener.exitPeak_3d(self)




    def peak_3d(self):

        localctx = CcpnNPKParser.Peak_3dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_peak_3d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 150
                self.position()
                self.state = 151
                self.position()
                self.state = 152
                self.position()
                self.state = 153
                self.match(CcpnNPKParser.Simple_name)
                self.state = 154
                self.match(CcpnNPKParser.Simple_name)
                self.state = 155
                self.match(CcpnNPKParser.Simple_name)
                pass

            elif la_ == 2:
                self.state = 157
                self.match(CcpnNPKParser.Simple_name)
                self.state = 158
                self.match(CcpnNPKParser.Simple_name)
                self.state = 159
                self.match(CcpnNPKParser.Simple_name)
                self.state = 160
                self.position()
                self.state = 161
                self.position()
                self.state = 162
                self.position()
                pass


            self.state = 166
            self.number()
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 167
                self.number()


            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 170
                self.position()


            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 173
                self.position()


            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 176
                self.position()


            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 179
                self.position()


            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1648) != 0):
                self.state = 182
                self.note()
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 188
            _la = self._input.LA(1)
            if not(_la==-1 or _la==12):
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
            return self.getToken(CcpnNPKParser.Height, 0)

        def RETURN_VARS(self):
            return self.getToken(CcpnNPKParser.RETURN_VARS, 0)

        def Volume(self):
            return self.getToken(CcpnNPKParser.Volume, 0)

        def Line_width_F1(self):
            return self.getToken(CcpnNPKParser.Line_width_F1, 0)

        def Line_width_F2(self):
            return self.getToken(CcpnNPKParser.Line_width_F2, 0)

        def Line_width_F3(self):
            return self.getToken(CcpnNPKParser.Line_width_F3, 0)

        def Line_width_F4(self):
            return self.getToken(CcpnNPKParser.Line_width_F4, 0)

        def Merit(self):
            return self.getToken(CcpnNPKParser.Merit, 0)

        def Details(self):
            return self.getToken(CcpnNPKParser.Details, 0)

        def Fit_method(self):
            return self.getToken(CcpnNPKParser.Fit_method, 0)

        def Vol_method(self):
            return self.getToken(CcpnNPKParser.Vol_method, 0)

        def peak_4d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnNPKParser.Peak_4dContext)
            else:
                return self.getTypedRuleContext(CcpnNPKParser.Peak_4dContext,i)


        def Assign_F1_(self):
            return self.getToken(CcpnNPKParser.Assign_F1_, 0)

        def Assign_F2(self):
            return self.getToken(CcpnNPKParser.Assign_F2, 0)

        def Assign_F3(self):
            return self.getToken(CcpnNPKParser.Assign_F3, 0)

        def Assign_F4(self):
            return self.getToken(CcpnNPKParser.Assign_F4, 0)

        def Assign_F1(self):
            return self.getToken(CcpnNPKParser.Assign_F1, 0)

        def Position_F1(self):
            return self.getToken(CcpnNPKParser.Position_F1, 0)

        def Shift_F1(self):
            return self.getToken(CcpnNPKParser.Shift_F1, 0)

        def Position_F2(self):
            return self.getToken(CcpnNPKParser.Position_F2, 0)

        def Shift_F2(self):
            return self.getToken(CcpnNPKParser.Shift_F2, 0)

        def Position_F3(self):
            return self.getToken(CcpnNPKParser.Position_F3, 0)

        def Shift_F3(self):
            return self.getToken(CcpnNPKParser.Shift_F3, 0)

        def Position_F4(self):
            return self.getToken(CcpnNPKParser.Position_F4, 0)

        def Shift_F4(self):
            return self.getToken(CcpnNPKParser.Shift_F4, 0)

        def Position_F1_(self):
            return self.getToken(CcpnNPKParser.Position_F1_, 0)

        def Shift_F1_(self):
            return self.getToken(CcpnNPKParser.Shift_F1_, 0)

        def getRuleIndex(self):
            return CcpnNPKParser.RULE_peak_list_4d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_list_4d" ):
                listener.enterPeak_list_4d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_list_4d" ):
                listener.exitPeak_list_4d(self)




    def peak_list_4d(self):

        localctx = CcpnNPKParser.Peak_list_4dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_peak_list_4d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3]:
                self.state = 190
                _la = self._input.LA(1)
                if not(_la==2 or _la==3):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 191
                _la = self._input.LA(1)
                if not(_la==16 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 192
                _la = self._input.LA(1)
                if not(_la==17 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 193
                _la = self._input.LA(1)
                if not(_la==18 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 194
                self.match(CcpnNPKParser.Assign_F1_)
                self.state = 195
                self.match(CcpnNPKParser.Assign_F2)
                self.state = 196
                self.match(CcpnNPKParser.Assign_F3)
                self.state = 197
                self.match(CcpnNPKParser.Assign_F4)
                pass
            elif token in [1]:
                self.state = 198
                self.match(CcpnNPKParser.Assign_F1)
                self.state = 199
                self.match(CcpnNPKParser.Assign_F2)
                self.state = 200
                self.match(CcpnNPKParser.Assign_F3)
                self.state = 201
                self.match(CcpnNPKParser.Assign_F4)
                self.state = 202
                _la = self._input.LA(1)
                if not(_la==15 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 203
                _la = self._input.LA(1)
                if not(_la==16 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 204
                _la = self._input.LA(1)
                if not(_la==17 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 205
                _la = self._input.LA(1)
                if not(_la==18 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 208
            self.match(CcpnNPKParser.Height)
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 209
                self.match(CcpnNPKParser.Volume)


            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 212
                self.match(CcpnNPKParser.Line_width_F1)


            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 215
                self.match(CcpnNPKParser.Line_width_F2)


            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 218
                self.match(CcpnNPKParser.Line_width_F3)


            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 221
                self.match(CcpnNPKParser.Line_width_F4)


            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 224
                self.match(CcpnNPKParser.Merit)


            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 227
                self.match(CcpnNPKParser.Details)


            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 230
                self.match(CcpnNPKParser.Fit_method)


            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 233
                self.match(CcpnNPKParser.Vol_method)


            self.state = 236
            self.match(CcpnNPKParser.RETURN_VARS)
            self.state = 238 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 237
                self.peak_4d()
                self.state = 240 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 624) != 0)):
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

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnNPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(CcpnNPKParser.NumberContext,i)


        def RETURN(self):
            return self.getToken(CcpnNPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(CcpnNPKParser.EOF, 0)

        def position(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnNPKParser.PositionContext)
            else:
                return self.getTypedRuleContext(CcpnNPKParser.PositionContext,i)


        def note(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnNPKParser.NoteContext)
            else:
                return self.getTypedRuleContext(CcpnNPKParser.NoteContext,i)


        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(CcpnNPKParser.Simple_name)
            else:
                return self.getToken(CcpnNPKParser.Simple_name, i)

        def getRuleIndex(self):
            return CcpnNPKParser.RULE_peak_4d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_4d" ):
                listener.enterPeak_4d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_4d" ):
                listener.exitPeak_4d(self)




    def peak_4d(self):

        localctx = CcpnNPKParser.Peak_4dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_peak_4d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 242
                self.position()
                self.state = 243
                self.position()
                self.state = 244
                self.position()
                self.state = 245
                self.position()
                self.state = 246
                self.match(CcpnNPKParser.Simple_name)
                self.state = 247
                self.match(CcpnNPKParser.Simple_name)
                self.state = 248
                self.match(CcpnNPKParser.Simple_name)
                self.state = 249
                self.match(CcpnNPKParser.Simple_name)
                pass

            elif la_ == 2:
                self.state = 251
                self.match(CcpnNPKParser.Simple_name)
                self.state = 252
                self.match(CcpnNPKParser.Simple_name)
                self.state = 253
                self.match(CcpnNPKParser.Simple_name)
                self.state = 254
                self.match(CcpnNPKParser.Simple_name)
                self.state = 255
                self.position()
                self.state = 256
                self.position()
                self.state = 257
                self.position()
                self.state = 258
                self.position()
                pass


            self.state = 262
            self.number()
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.state = 263
                self.number()


            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 266
                self.position()


            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 269
                self.position()


            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 272
                self.position()


            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.state = 275
                self.position()


            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.state = 278
                self.position()


            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1648) != 0):
                self.state = 281
                self.note()
                self.state = 286
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 287
            _la = self._input.LA(1)
            if not(_la==-1 or _la==12):
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
            return self.getToken(CcpnNPKParser.Float, 0)

        def Real(self):
            return self.getToken(CcpnNPKParser.Real, 0)

        def Integer(self):
            return self.getToken(CcpnNPKParser.Integer, 0)

        def Simple_name(self):
            return self.getToken(CcpnNPKParser.Simple_name, 0)

        def getRuleIndex(self):
            return CcpnNPKParser.RULE_position

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPosition" ):
                listener.enterPosition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPosition" ):
                listener.exitPosition(self)




    def position(self):

        localctx = CcpnNPKParser.PositionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_position)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 624) != 0)):
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
            return self.getToken(CcpnNPKParser.Float, 0)

        def Real(self):
            return self.getToken(CcpnNPKParser.Real, 0)

        def Integer(self):
            return self.getToken(CcpnNPKParser.Integer, 0)

        def Simple_name(self):
            return self.getToken(CcpnNPKParser.Simple_name, 0)

        def getRuleIndex(self):
            return CcpnNPKParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = CcpnNPKParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 624) != 0)):
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
            return self.getToken(CcpnNPKParser.Float, 0)

        def Real(self):
            return self.getToken(CcpnNPKParser.Real, 0)

        def Integer(self):
            return self.getToken(CcpnNPKParser.Integer, 0)

        def Simple_name(self):
            return self.getToken(CcpnNPKParser.Simple_name, 0)

        def Any_name(self):
            return self.getToken(CcpnNPKParser.Any_name, 0)

        def getRuleIndex(self):
            return CcpnNPKParser.RULE_note

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNote" ):
                listener.enterNote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNote" ):
                listener.exitNote(self)




    def note(self):

        localctx = CcpnNPKParser.NoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_note)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1648) != 0)):
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





