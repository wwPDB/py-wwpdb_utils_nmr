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
        4,1,38,292,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,3,0,20,8,0,1,0,1,0,1,0,1,0,5,0,26,8,0,10,0,
        12,0,29,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,41,8,1,1,
        1,1,1,3,1,45,8,1,1,1,3,1,48,8,1,1,1,3,1,51,8,1,1,1,3,1,54,8,1,1,
        1,3,1,57,8,1,1,1,3,1,60,8,1,1,1,3,1,63,8,1,1,1,1,1,4,1,67,8,1,11,
        1,12,1,68,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,81,8,2,1,2,
        1,2,3,2,85,8,2,1,2,3,2,88,8,2,1,2,3,2,91,8,2,1,2,3,2,94,8,2,1,2,
        5,2,97,8,2,10,2,12,2,100,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,3,3,116,8,3,1,3,1,3,3,3,120,8,3,1,3,3,3,123,
        8,3,1,3,3,3,126,8,3,1,3,3,3,129,8,3,1,3,3,3,132,8,3,1,3,3,3,135,
        8,3,1,3,3,3,138,8,3,1,3,3,3,141,8,3,1,3,1,3,4,3,145,8,3,11,3,12,
        3,146,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,
        4,163,8,4,1,4,1,4,3,4,167,8,4,1,4,3,4,170,8,4,1,4,3,4,173,8,4,1,
        4,3,4,176,8,4,1,4,3,4,179,8,4,1,4,5,4,182,8,4,10,4,12,4,185,9,4,
        1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,3,5,205,8,5,1,5,1,5,3,5,209,8,5,1,5,3,5,212,8,5,1,5,3,5,
        215,8,5,1,5,3,5,218,8,5,1,5,3,5,221,8,5,1,5,3,5,224,8,5,1,5,3,5,
        227,8,5,1,5,3,5,230,8,5,1,5,3,5,233,8,5,1,5,1,5,4,5,237,8,5,11,5,
        12,5,238,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,3,6,259,8,6,1,6,1,6,3,6,263,8,6,1,6,3,6,266,8,6,
        1,6,3,6,269,8,6,1,6,3,6,272,8,6,1,6,3,6,275,8,6,1,6,3,6,278,8,6,
        1,6,5,6,281,8,6,10,6,12,6,284,9,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,0,
        0,9,0,2,4,6,8,10,12,14,16,0,7,1,0,2,3,2,0,16,16,20,20,2,0,15,15,
        19,19,1,1,12,12,2,0,17,17,21,21,2,0,18,18,22,22,2,0,4,6,10,10,338,
        0,19,1,0,0,0,2,40,1,0,0,0,4,80,1,0,0,0,6,115,1,0,0,0,8,162,1,0,0,
        0,10,204,1,0,0,0,12,258,1,0,0,0,14,287,1,0,0,0,16,289,1,0,0,0,18,
        20,5,12,0,0,19,18,1,0,0,0,19,20,1,0,0,0,20,27,1,0,0,0,21,26,3,2,
        1,0,22,26,3,6,3,0,23,26,3,10,5,0,24,26,5,12,0,0,25,21,1,0,0,0,25,
        22,1,0,0,0,25,23,1,0,0,0,25,24,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,
        0,27,28,1,0,0,0,28,30,1,0,0,0,29,27,1,0,0,0,30,31,5,0,0,1,31,1,1,
        0,0,0,32,33,7,0,0,0,33,34,7,1,0,0,34,35,5,23,0,0,35,41,5,24,0,0,
        36,37,5,1,0,0,37,38,5,24,0,0,38,39,7,2,0,0,39,41,7,1,0,0,40,32,1,
        0,0,0,40,36,1,0,0,0,41,42,1,0,0,0,42,44,5,27,0,0,43,45,5,28,0,0,
        44,43,1,0,0,0,44,45,1,0,0,0,45,47,1,0,0,0,46,48,5,29,0,0,47,46,1,
        0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,49,51,5,30,0,0,50,49,1,0,0,0,50,
        51,1,0,0,0,51,53,1,0,0,0,52,54,5,33,0,0,53,52,1,0,0,0,53,54,1,0,
        0,0,54,56,1,0,0,0,55,57,5,34,0,0,56,55,1,0,0,0,56,57,1,0,0,0,57,
        59,1,0,0,0,58,60,5,35,0,0,59,58,1,0,0,0,59,60,1,0,0,0,60,62,1,0,
        0,0,61,63,5,36,0,0,62,61,1,0,0,0,62,63,1,0,0,0,63,64,1,0,0,0,64,
        66,5,38,0,0,65,67,3,4,2,0,66,65,1,0,0,0,67,68,1,0,0,0,68,66,1,0,
        0,0,68,69,1,0,0,0,69,3,1,0,0,0,70,71,3,14,7,0,71,72,3,14,7,0,72,
        73,5,10,0,0,73,74,5,10,0,0,74,81,1,0,0,0,75,76,5,10,0,0,76,77,5,
        10,0,0,77,78,3,14,7,0,78,79,3,14,7,0,79,81,1,0,0,0,80,70,1,0,0,0,
        80,75,1,0,0,0,81,82,1,0,0,0,82,84,3,16,8,0,83,85,3,16,8,0,84,83,
        1,0,0,0,84,85,1,0,0,0,85,87,1,0,0,0,86,88,3,14,7,0,87,86,1,0,0,0,
        87,88,1,0,0,0,88,90,1,0,0,0,89,91,3,14,7,0,90,89,1,0,0,0,90,91,1,
        0,0,0,91,93,1,0,0,0,92,94,3,14,7,0,93,92,1,0,0,0,93,94,1,0,0,0,94,
        98,1,0,0,0,95,97,5,10,0,0,96,95,1,0,0,0,97,100,1,0,0,0,98,96,1,0,
        0,0,98,99,1,0,0,0,99,101,1,0,0,0,100,98,1,0,0,0,101,102,7,3,0,0,
        102,5,1,0,0,0,103,104,7,0,0,0,104,105,7,1,0,0,105,106,7,4,0,0,106,
        107,5,23,0,0,107,108,5,24,0,0,108,116,5,25,0,0,109,110,5,1,0,0,110,
        111,5,24,0,0,111,112,5,25,0,0,112,113,7,2,0,0,113,114,7,1,0,0,114,
        116,7,4,0,0,115,103,1,0,0,0,115,109,1,0,0,0,116,117,1,0,0,0,117,
        119,5,27,0,0,118,120,5,28,0,0,119,118,1,0,0,0,119,120,1,0,0,0,120,
        122,1,0,0,0,121,123,5,29,0,0,122,121,1,0,0,0,122,123,1,0,0,0,123,
        125,1,0,0,0,124,126,5,30,0,0,125,124,1,0,0,0,125,126,1,0,0,0,126,
        128,1,0,0,0,127,129,5,31,0,0,128,127,1,0,0,0,128,129,1,0,0,0,129,
        131,1,0,0,0,130,132,5,33,0,0,131,130,1,0,0,0,131,132,1,0,0,0,132,
        134,1,0,0,0,133,135,5,34,0,0,134,133,1,0,0,0,134,135,1,0,0,0,135,
        137,1,0,0,0,136,138,5,35,0,0,137,136,1,0,0,0,137,138,1,0,0,0,138,
        140,1,0,0,0,139,141,5,36,0,0,140,139,1,0,0,0,140,141,1,0,0,0,141,
        142,1,0,0,0,142,144,5,38,0,0,143,145,3,8,4,0,144,143,1,0,0,0,145,
        146,1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,0,147,7,1,0,0,0,148,149,
        3,14,7,0,149,150,3,14,7,0,150,151,3,14,7,0,151,152,5,10,0,0,152,
        153,5,10,0,0,153,154,5,10,0,0,154,163,1,0,0,0,155,156,5,10,0,0,156,
        157,5,10,0,0,157,158,5,10,0,0,158,159,3,14,7,0,159,160,3,14,7,0,
        160,161,3,14,7,0,161,163,1,0,0,0,162,148,1,0,0,0,162,155,1,0,0,0,
        163,164,1,0,0,0,164,166,3,16,8,0,165,167,3,16,8,0,166,165,1,0,0,
        0,166,167,1,0,0,0,167,169,1,0,0,0,168,170,3,14,7,0,169,168,1,0,0,
        0,169,170,1,0,0,0,170,172,1,0,0,0,171,173,3,14,7,0,172,171,1,0,0,
        0,172,173,1,0,0,0,173,175,1,0,0,0,174,176,3,14,7,0,175,174,1,0,0,
        0,175,176,1,0,0,0,176,178,1,0,0,0,177,179,3,14,7,0,178,177,1,0,0,
        0,178,179,1,0,0,0,179,183,1,0,0,0,180,182,5,10,0,0,181,180,1,0,0,
        0,182,185,1,0,0,0,183,181,1,0,0,0,183,184,1,0,0,0,184,186,1,0,0,
        0,185,183,1,0,0,0,186,187,7,3,0,0,187,9,1,0,0,0,188,189,7,0,0,0,
        189,190,7,1,0,0,190,191,7,4,0,0,191,192,7,5,0,0,192,193,5,23,0,0,
        193,194,5,24,0,0,194,195,5,25,0,0,195,205,5,26,0,0,196,197,5,1,0,
        0,197,198,5,24,0,0,198,199,5,25,0,0,199,200,5,26,0,0,200,201,7,2,
        0,0,201,202,7,1,0,0,202,203,7,4,0,0,203,205,7,5,0,0,204,188,1,0,
        0,0,204,196,1,0,0,0,205,206,1,0,0,0,206,208,5,27,0,0,207,209,5,28,
        0,0,208,207,1,0,0,0,208,209,1,0,0,0,209,211,1,0,0,0,210,212,5,29,
        0,0,211,210,1,0,0,0,211,212,1,0,0,0,212,214,1,0,0,0,213,215,5,30,
        0,0,214,213,1,0,0,0,214,215,1,0,0,0,215,217,1,0,0,0,216,218,5,31,
        0,0,217,216,1,0,0,0,217,218,1,0,0,0,218,220,1,0,0,0,219,221,5,32,
        0,0,220,219,1,0,0,0,220,221,1,0,0,0,221,223,1,0,0,0,222,224,5,33,
        0,0,223,222,1,0,0,0,223,224,1,0,0,0,224,226,1,0,0,0,225,227,5,34,
        0,0,226,225,1,0,0,0,226,227,1,0,0,0,227,229,1,0,0,0,228,230,5,35,
        0,0,229,228,1,0,0,0,229,230,1,0,0,0,230,232,1,0,0,0,231,233,5,36,
        0,0,232,231,1,0,0,0,232,233,1,0,0,0,233,234,1,0,0,0,234,236,5,38,
        0,0,235,237,3,12,6,0,236,235,1,0,0,0,237,238,1,0,0,0,238,236,1,0,
        0,0,238,239,1,0,0,0,239,11,1,0,0,0,240,241,3,14,7,0,241,242,3,14,
        7,0,242,243,3,14,7,0,243,244,3,14,7,0,244,245,5,10,0,0,245,246,5,
        10,0,0,246,247,5,10,0,0,247,248,5,10,0,0,248,259,1,0,0,0,249,250,
        5,10,0,0,250,251,5,10,0,0,251,252,5,10,0,0,252,253,5,10,0,0,253,
        254,3,14,7,0,254,255,3,14,7,0,255,256,3,14,7,0,256,257,3,14,7,0,
        257,259,1,0,0,0,258,240,1,0,0,0,258,249,1,0,0,0,259,260,1,0,0,0,
        260,262,3,16,8,0,261,263,3,16,8,0,262,261,1,0,0,0,262,263,1,0,0,
        0,263,265,1,0,0,0,264,266,3,14,7,0,265,264,1,0,0,0,265,266,1,0,0,
        0,266,268,1,0,0,0,267,269,3,14,7,0,268,267,1,0,0,0,268,269,1,0,0,
        0,269,271,1,0,0,0,270,272,3,14,7,0,271,270,1,0,0,0,271,272,1,0,0,
        0,272,274,1,0,0,0,273,275,3,14,7,0,274,273,1,0,0,0,274,275,1,0,0,
        0,275,277,1,0,0,0,276,278,3,14,7,0,277,276,1,0,0,0,277,278,1,0,0,
        0,278,282,1,0,0,0,279,281,5,10,0,0,280,279,1,0,0,0,281,284,1,0,0,
        0,282,280,1,0,0,0,282,283,1,0,0,0,283,285,1,0,0,0,284,282,1,0,0,
        0,285,286,7,3,0,0,286,13,1,0,0,0,287,288,7,6,0,0,288,15,1,0,0,0,
        289,290,7,6,0,0,290,17,1,0,0,0,54,19,25,27,40,44,47,50,53,56,59,
        62,68,80,84,87,90,93,98,115,119,122,125,128,131,134,137,140,146,
        162,166,169,172,175,178,183,204,208,211,214,217,220,223,226,229,
        232,238,258,262,265,268,271,274,277,282
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
                      "Integer", "Float", "Real", "SHARP_COMMENT", "EXCLM_COMMENT", 
                      "SMCLN_COMMENT", "Simple_name", "SPACE", "RETURN", 
                      "SECTION_COMMENT", "LINE_COMMENT", "Position_F1_", 
                      "Position_F2", "Position_F3", "Position_F4", "Shift_F1_", 
                      "Shift_F2", "Shift_F3", "Shift_F4", "Assign_F1_", 
                      "Assign_F2", "Assign_F3", "Assign_F4", "Height", "Volume", 
                      "Line_width_F1", "Line_width_F2", "Line_width_F3", 
                      "Line_width_F4", "Merit", "Details", "Fit_method", 
                      "Vol_method", "SPACE_VARS", "RETURN_VARS" ]

    RULE_ccpn_npk = 0
    RULE_peak_list_2d = 1
    RULE_peak_2d = 2
    RULE_peak_list_3d = 3
    RULE_peak_3d = 4
    RULE_peak_list_4d = 5
    RULE_peak_4d = 6
    RULE_position = 7
    RULE_number = 8

    ruleNames =  [ "ccpn_npk", "peak_list_2d", "peak_2d", "peak_list_3d", 
                   "peak_3d", "peak_list_4d", "peak_4d", "position", "number" ]

    EOF = Token.EOF
    Assign_F1=1
    Position_F1=2
    Shift_F1=3
    Integer=4
    Float=5
    Real=6
    SHARP_COMMENT=7
    EXCLM_COMMENT=8
    SMCLN_COMMENT=9
    Simple_name=10
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
            self.state = 19
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 18
                self.match(CcpnNPKParser.RETURN)


            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4110) != 0):
                self.state = 25
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 21
                    self.peak_list_2d()
                    pass

                elif la_ == 2:
                    self.state = 22
                    self.peak_list_3d()
                    pass

                elif la_ == 3:
                    self.state = 23
                    self.peak_list_4d()
                    pass

                elif la_ == 4:
                    self.state = 24
                    self.match(CcpnNPKParser.RETURN)
                    pass


                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
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
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3]:
                self.state = 32
                _la = self._input.LA(1)
                if not(_la==2 or _la==3):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 33
                _la = self._input.LA(1)
                if not(_la==16 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 34
                self.match(CcpnNPKParser.Assign_F1_)
                self.state = 35
                self.match(CcpnNPKParser.Assign_F2)
                pass
            elif token in [1]:
                self.state = 36
                self.match(CcpnNPKParser.Assign_F1)
                self.state = 37
                self.match(CcpnNPKParser.Assign_F2)
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
                pass
            else:
                raise NoViableAltException(self)

            self.state = 42
            self.match(CcpnNPKParser.Height)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 43
                self.match(CcpnNPKParser.Volume)


            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 46
                self.match(CcpnNPKParser.Line_width_F1)


            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 49
                self.match(CcpnNPKParser.Line_width_F2)


            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 52
                self.match(CcpnNPKParser.Merit)


            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 55
                self.match(CcpnNPKParser.Details)


            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 58
                self.match(CcpnNPKParser.Fit_method)


            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 61
                self.match(CcpnNPKParser.Vol_method)


            self.state = 64
            self.match(CcpnNPKParser.RETURN_VARS)
            self.state = 66 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 65
                self.peak_2d()
                self.state = 68 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1136) != 0)):
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
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 70
                self.position()
                self.state = 71
                self.position()
                self.state = 72
                self.match(CcpnNPKParser.Simple_name)
                self.state = 73
                self.match(CcpnNPKParser.Simple_name)
                pass

            elif la_ == 2:
                self.state = 75
                self.match(CcpnNPKParser.Simple_name)
                self.state = 76
                self.match(CcpnNPKParser.Simple_name)
                self.state = 77
                self.position()
                self.state = 78
                self.position()
                pass


            self.state = 82
            self.number()
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 83
                self.number()


            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 86
                self.position()


            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 89
                self.position()


            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 92
                self.position()


            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 95
                self.match(CcpnNPKParser.Simple_name)
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 101
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
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3]:
                self.state = 103
                _la = self._input.LA(1)
                if not(_la==2 or _la==3):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 104
                _la = self._input.LA(1)
                if not(_la==16 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 105
                _la = self._input.LA(1)
                if not(_la==17 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 106
                self.match(CcpnNPKParser.Assign_F1_)
                self.state = 107
                self.match(CcpnNPKParser.Assign_F2)
                self.state = 108
                self.match(CcpnNPKParser.Assign_F3)
                pass
            elif token in [1]:
                self.state = 109
                self.match(CcpnNPKParser.Assign_F1)
                self.state = 110
                self.match(CcpnNPKParser.Assign_F2)
                self.state = 111
                self.match(CcpnNPKParser.Assign_F3)
                self.state = 112
                _la = self._input.LA(1)
                if not(_la==15 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 113
                _la = self._input.LA(1)
                if not(_la==16 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 114
                _la = self._input.LA(1)
                if not(_la==17 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 117
            self.match(CcpnNPKParser.Height)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 118
                self.match(CcpnNPKParser.Volume)


            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 121
                self.match(CcpnNPKParser.Line_width_F1)


            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 124
                self.match(CcpnNPKParser.Line_width_F2)


            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 127
                self.match(CcpnNPKParser.Line_width_F3)


            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 130
                self.match(CcpnNPKParser.Merit)


            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 133
                self.match(CcpnNPKParser.Details)


            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 136
                self.match(CcpnNPKParser.Fit_method)


            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 139
                self.match(CcpnNPKParser.Vol_method)


            self.state = 142
            self.match(CcpnNPKParser.RETURN_VARS)
            self.state = 144 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 143
                self.peak_3d()
                self.state = 146 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1136) != 0)):
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
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 148
                self.position()
                self.state = 149
                self.position()
                self.state = 150
                self.position()
                self.state = 151
                self.match(CcpnNPKParser.Simple_name)
                self.state = 152
                self.match(CcpnNPKParser.Simple_name)
                self.state = 153
                self.match(CcpnNPKParser.Simple_name)
                pass

            elif la_ == 2:
                self.state = 155
                self.match(CcpnNPKParser.Simple_name)
                self.state = 156
                self.match(CcpnNPKParser.Simple_name)
                self.state = 157
                self.match(CcpnNPKParser.Simple_name)
                self.state = 158
                self.position()
                self.state = 159
                self.position()
                self.state = 160
                self.position()
                pass


            self.state = 164
            self.number()
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 165
                self.number()


            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 168
                self.position()


            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 171
                self.position()


            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 174
                self.position()


            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 177
                self.position()


            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 180
                self.match(CcpnNPKParser.Simple_name)
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 186
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
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3]:
                self.state = 188
                _la = self._input.LA(1)
                if not(_la==2 or _la==3):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 189
                _la = self._input.LA(1)
                if not(_la==16 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 190
                _la = self._input.LA(1)
                if not(_la==17 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 191
                _la = self._input.LA(1)
                if not(_la==18 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 192
                self.match(CcpnNPKParser.Assign_F1_)
                self.state = 193
                self.match(CcpnNPKParser.Assign_F2)
                self.state = 194
                self.match(CcpnNPKParser.Assign_F3)
                self.state = 195
                self.match(CcpnNPKParser.Assign_F4)
                pass
            elif token in [1]:
                self.state = 196
                self.match(CcpnNPKParser.Assign_F1)
                self.state = 197
                self.match(CcpnNPKParser.Assign_F2)
                self.state = 198
                self.match(CcpnNPKParser.Assign_F3)
                self.state = 199
                self.match(CcpnNPKParser.Assign_F4)
                self.state = 200
                _la = self._input.LA(1)
                if not(_la==15 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 201
                _la = self._input.LA(1)
                if not(_la==16 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 202
                _la = self._input.LA(1)
                if not(_la==17 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 203
                _la = self._input.LA(1)
                if not(_la==18 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 206
            self.match(CcpnNPKParser.Height)
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 207
                self.match(CcpnNPKParser.Volume)


            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 210
                self.match(CcpnNPKParser.Line_width_F1)


            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 213
                self.match(CcpnNPKParser.Line_width_F2)


            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 216
                self.match(CcpnNPKParser.Line_width_F3)


            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 219
                self.match(CcpnNPKParser.Line_width_F4)


            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 222
                self.match(CcpnNPKParser.Merit)


            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 225
                self.match(CcpnNPKParser.Details)


            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 228
                self.match(CcpnNPKParser.Fit_method)


            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 231
                self.match(CcpnNPKParser.Vol_method)


            self.state = 234
            self.match(CcpnNPKParser.RETURN_VARS)
            self.state = 236 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 235
                self.peak_4d()
                self.state = 238 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1136) != 0)):
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
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 240
                self.position()
                self.state = 241
                self.position()
                self.state = 242
                self.position()
                self.state = 243
                self.position()
                self.state = 244
                self.match(CcpnNPKParser.Simple_name)
                self.state = 245
                self.match(CcpnNPKParser.Simple_name)
                self.state = 246
                self.match(CcpnNPKParser.Simple_name)
                self.state = 247
                self.match(CcpnNPKParser.Simple_name)
                pass

            elif la_ == 2:
                self.state = 249
                self.match(CcpnNPKParser.Simple_name)
                self.state = 250
                self.match(CcpnNPKParser.Simple_name)
                self.state = 251
                self.match(CcpnNPKParser.Simple_name)
                self.state = 252
                self.match(CcpnNPKParser.Simple_name)
                self.state = 253
                self.position()
                self.state = 254
                self.position()
                self.state = 255
                self.position()
                self.state = 256
                self.position()
                pass


            self.state = 260
            self.number()
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.state = 261
                self.number()


            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 264
                self.position()


            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 267
                self.position()


            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 270
                self.position()


            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.state = 273
                self.position()


            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.state = 276
                self.position()


            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 279
                self.match(CcpnNPKParser.Simple_name)
                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 285
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
            self.state = 287
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1136) != 0)):
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
            self.state = 289
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1136) != 0)):
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





