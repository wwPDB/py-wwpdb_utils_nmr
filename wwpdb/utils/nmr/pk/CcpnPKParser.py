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
        4,1,37,250,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,3,0,20,8,0,1,0,1,0,1,0,1,0,5,0,26,8,0,10,0,
        12,0,29,9,0,1,0,1,0,1,1,3,1,34,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,3,1,44,8,1,1,1,3,1,47,8,1,1,1,3,1,50,8,1,1,1,3,1,53,8,1,1,1,3,
        1,56,8,1,1,1,3,1,59,8,1,1,1,1,1,4,1,63,8,1,11,1,12,1,64,1,2,3,2,
        68,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,78,8,2,1,2,3,2,81,8,2,
        1,2,3,2,84,8,2,1,2,5,2,87,8,2,10,2,12,2,90,9,2,1,2,1,2,1,3,3,3,95,
        8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,107,8,3,1,3,3,3,
        110,8,3,1,3,3,3,113,8,3,1,3,3,3,116,8,3,1,3,3,3,119,8,3,1,3,3,3,
        122,8,3,1,3,3,3,125,8,3,1,3,1,3,4,3,129,8,3,11,3,12,3,130,1,4,3,
        4,134,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,146,8,4,1,
        4,3,4,149,8,4,1,4,3,4,152,8,4,1,4,3,4,155,8,4,1,4,5,4,158,8,4,10,
        4,12,4,161,9,4,1,4,1,4,1,5,3,5,166,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,3,5,180,8,5,1,5,3,5,183,8,5,1,5,3,5,186,8,
        5,1,5,3,5,189,8,5,1,5,3,5,192,8,5,1,5,3,5,195,8,5,1,5,3,5,198,8,
        5,1,5,3,5,201,8,5,1,5,1,5,4,5,205,8,5,11,5,12,5,206,1,6,3,6,210,
        8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,224,8,6,
        1,6,3,6,227,8,6,1,6,3,6,230,8,6,1,6,3,6,233,8,6,1,6,3,6,236,8,6,
        1,6,5,6,239,8,6,10,6,12,6,242,9,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,0,
        0,9,0,2,4,6,8,10,12,14,16,0,8,2,0,2,2,13,13,2,0,14,14,18,18,2,0,
        15,15,19,19,1,1,10,10,2,0,16,16,20,20,2,0,17,17,21,21,1,0,3,5,2,
        0,4,5,8,8,290,0,19,1,0,0,0,2,33,1,0,0,0,4,67,1,0,0,0,6,94,1,0,0,
        0,8,133,1,0,0,0,10,165,1,0,0,0,12,209,1,0,0,0,14,245,1,0,0,0,16,
        247,1,0,0,0,18,20,5,10,0,0,19,18,1,0,0,0,19,20,1,0,0,0,20,27,1,0,
        0,0,21,26,3,2,1,0,22,26,3,6,3,0,23,26,3,10,5,0,24,26,5,10,0,0,25,
        21,1,0,0,0,25,22,1,0,0,0,25,23,1,0,0,0,25,24,1,0,0,0,26,29,1,0,0,
        0,27,25,1,0,0,0,27,28,1,0,0,0,28,30,1,0,0,0,29,27,1,0,0,0,30,31,
        5,0,0,1,31,1,1,0,0,0,32,34,5,1,0,0,33,32,1,0,0,0,33,34,1,0,0,0,34,
        35,1,0,0,0,35,36,7,0,0,0,36,37,7,1,0,0,37,38,7,2,0,0,38,39,5,22,
        0,0,39,40,5,23,0,0,40,41,5,26,0,0,41,43,5,27,0,0,42,44,5,28,0,0,
        43,42,1,0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,45,47,5,29,0,0,46,45,1,
        0,0,0,46,47,1,0,0,0,47,49,1,0,0,0,48,50,5,32,0,0,49,48,1,0,0,0,49,
        50,1,0,0,0,50,52,1,0,0,0,51,53,5,33,0,0,52,51,1,0,0,0,52,53,1,0,
        0,0,53,55,1,0,0,0,54,56,5,34,0,0,55,54,1,0,0,0,55,56,1,0,0,0,56,
        58,1,0,0,0,57,59,5,35,0,0,58,57,1,0,0,0,58,59,1,0,0,0,59,60,1,0,
        0,0,60,62,5,37,0,0,61,63,3,4,2,0,62,61,1,0,0,0,63,64,1,0,0,0,64,
        62,1,0,0,0,64,65,1,0,0,0,65,3,1,0,0,0,66,68,5,3,0,0,67,66,1,0,0,
        0,67,68,1,0,0,0,68,69,1,0,0,0,69,70,5,3,0,0,70,71,3,14,7,0,71,72,
        3,14,7,0,72,73,5,8,0,0,73,74,5,8,0,0,74,75,3,16,8,0,75,77,3,16,8,
        0,76,78,3,14,7,0,77,76,1,0,0,0,77,78,1,0,0,0,78,80,1,0,0,0,79,81,
        3,14,7,0,80,79,1,0,0,0,80,81,1,0,0,0,81,83,1,0,0,0,82,84,3,14,7,
        0,83,82,1,0,0,0,83,84,1,0,0,0,84,88,1,0,0,0,85,87,5,8,0,0,86,85,
        1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,89,91,1,0,0,0,
        90,88,1,0,0,0,91,92,7,3,0,0,92,5,1,0,0,0,93,95,5,1,0,0,94,93,1,0,
        0,0,94,95,1,0,0,0,95,96,1,0,0,0,96,97,7,0,0,0,97,98,7,1,0,0,98,99,
        7,2,0,0,99,100,7,4,0,0,100,101,5,22,0,0,101,102,5,23,0,0,102,103,
        5,24,0,0,103,104,5,26,0,0,104,106,5,27,0,0,105,107,5,28,0,0,106,
        105,1,0,0,0,106,107,1,0,0,0,107,109,1,0,0,0,108,110,5,29,0,0,109,
        108,1,0,0,0,109,110,1,0,0,0,110,112,1,0,0,0,111,113,5,30,0,0,112,
        111,1,0,0,0,112,113,1,0,0,0,113,115,1,0,0,0,114,116,5,32,0,0,115,
        114,1,0,0,0,115,116,1,0,0,0,116,118,1,0,0,0,117,119,5,33,0,0,118,
        117,1,0,0,0,118,119,1,0,0,0,119,121,1,0,0,0,120,122,5,34,0,0,121,
        120,1,0,0,0,121,122,1,0,0,0,122,124,1,0,0,0,123,125,5,35,0,0,124,
        123,1,0,0,0,124,125,1,0,0,0,125,126,1,0,0,0,126,128,5,37,0,0,127,
        129,3,8,4,0,128,127,1,0,0,0,129,130,1,0,0,0,130,128,1,0,0,0,130,
        131,1,0,0,0,131,7,1,0,0,0,132,134,5,3,0,0,133,132,1,0,0,0,133,134,
        1,0,0,0,134,135,1,0,0,0,135,136,5,3,0,0,136,137,3,14,7,0,137,138,
        3,14,7,0,138,139,3,14,7,0,139,140,5,8,0,0,140,141,5,8,0,0,141,142,
        5,8,0,0,142,143,3,16,8,0,143,145,3,16,8,0,144,146,3,14,7,0,145,144,
        1,0,0,0,145,146,1,0,0,0,146,148,1,0,0,0,147,149,3,14,7,0,148,147,
        1,0,0,0,148,149,1,0,0,0,149,151,1,0,0,0,150,152,3,14,7,0,151,150,
        1,0,0,0,151,152,1,0,0,0,152,154,1,0,0,0,153,155,3,14,7,0,154,153,
        1,0,0,0,154,155,1,0,0,0,155,159,1,0,0,0,156,158,5,8,0,0,157,156,
        1,0,0,0,158,161,1,0,0,0,159,157,1,0,0,0,159,160,1,0,0,0,160,162,
        1,0,0,0,161,159,1,0,0,0,162,163,7,3,0,0,163,9,1,0,0,0,164,166,5,
        1,0,0,165,164,1,0,0,0,165,166,1,0,0,0,166,167,1,0,0,0,167,168,7,
        0,0,0,168,169,7,1,0,0,169,170,7,2,0,0,170,171,7,4,0,0,171,172,7,
        5,0,0,172,173,5,22,0,0,173,174,5,23,0,0,174,175,5,24,0,0,175,176,
        5,25,0,0,176,177,5,26,0,0,177,179,5,27,0,0,178,180,5,28,0,0,179,
        178,1,0,0,0,179,180,1,0,0,0,180,182,1,0,0,0,181,183,5,29,0,0,182,
        181,1,0,0,0,182,183,1,0,0,0,183,185,1,0,0,0,184,186,5,30,0,0,185,
        184,1,0,0,0,185,186,1,0,0,0,186,188,1,0,0,0,187,189,5,31,0,0,188,
        187,1,0,0,0,188,189,1,0,0,0,189,191,1,0,0,0,190,192,5,32,0,0,191,
        190,1,0,0,0,191,192,1,0,0,0,192,194,1,0,0,0,193,195,5,33,0,0,194,
        193,1,0,0,0,194,195,1,0,0,0,195,197,1,0,0,0,196,198,5,34,0,0,197,
        196,1,0,0,0,197,198,1,0,0,0,198,200,1,0,0,0,199,201,5,35,0,0,200,
        199,1,0,0,0,200,201,1,0,0,0,201,202,1,0,0,0,202,204,5,37,0,0,203,
        205,3,12,6,0,204,203,1,0,0,0,205,206,1,0,0,0,206,204,1,0,0,0,206,
        207,1,0,0,0,207,11,1,0,0,0,208,210,5,3,0,0,209,208,1,0,0,0,209,210,
        1,0,0,0,210,211,1,0,0,0,211,212,5,3,0,0,212,213,3,14,7,0,213,214,
        3,14,7,0,214,215,3,14,7,0,215,216,3,14,7,0,216,217,5,8,0,0,217,218,
        5,8,0,0,218,219,5,8,0,0,219,220,5,8,0,0,220,221,3,16,8,0,221,223,
        3,16,8,0,222,224,3,14,7,0,223,222,1,0,0,0,223,224,1,0,0,0,224,226,
        1,0,0,0,225,227,3,14,7,0,226,225,1,0,0,0,226,227,1,0,0,0,227,229,
        1,0,0,0,228,230,3,14,7,0,229,228,1,0,0,0,229,230,1,0,0,0,230,232,
        1,0,0,0,231,233,3,14,7,0,232,231,1,0,0,0,232,233,1,0,0,0,233,235,
        1,0,0,0,234,236,3,14,7,0,235,234,1,0,0,0,235,236,1,0,0,0,236,240,
        1,0,0,0,237,239,5,8,0,0,238,237,1,0,0,0,239,242,1,0,0,0,240,238,
        1,0,0,0,240,241,1,0,0,0,241,243,1,0,0,0,242,240,1,0,0,0,243,244,
        7,3,0,0,244,13,1,0,0,0,245,246,7,6,0,0,246,15,1,0,0,0,247,248,7,
        7,0,0,248,17,1,0,0,0,48,19,25,27,33,43,46,49,52,55,58,64,67,77,80,
        83,88,94,106,109,112,115,118,121,124,130,133,145,148,151,154,159,
        165,179,182,185,188,191,194,197,200,206,209,223,226,229,232,235,
        240
    ]

class CcpnPKParser ( Parser ):

    grammarFileName = "CcpnPKParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Number'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'Position F1'", "'Position F2'", 
                     "'Position F3'", "'Position F4'", "'Shift F1'", "'Shift F2'", 
                     "'Shift F3'", "'Shift F4'", "'Assign F1'", "'Assign F2'", 
                     "'Assign F3'", "'Assign F4'", "'Height'", "'Volume'", 
                     "'Line Width F1 (Hz)'", "'Line Width F2 (Hz)'", "'Line Width F3 (Hz)'", 
                     "'Line Width F4 (Hz)'", "'Merit'", "'Details'", "'Fit Method'", 
                     "'Vol. Method'" ]

    symbolicNames = [ "<INVALID>", "Number", "Id", "Integer", "Float", "Real", 
                      "EXCLM_COMMENT", "SMCLN_COMMENT", "Simple_name", "SPACE", 
                      "RETURN", "SECTION_COMMENT", "LINE_COMMENT", "Id_", 
                      "Position_F1", "Position_F2", "Position_F3", "Position_F4", 
                      "Shift_F1", "Shift_F2", "Shift_F3", "Shift_F4", "Assign_F1", 
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
    RULE_position = 7
    RULE_number = 8

    ruleNames =  [ "ccpn_pk", "peak_list_2d", "peak_2d", "peak_list_3d", 
                   "peak_3d", "peak_list_4d", "peak_4d", "position", "number" ]

    EOF = Token.EOF
    Number=1
    Id=2
    Integer=3
    Float=4
    Real=5
    EXCLM_COMMENT=6
    SMCLN_COMMENT=7
    Simple_name=8
    SPACE=9
    RETURN=10
    SECTION_COMMENT=11
    LINE_COMMENT=12
    Id_=13
    Position_F1=14
    Position_F2=15
    Position_F3=16
    Position_F4=17
    Shift_F1=18
    Shift_F2=19
    Shift_F3=20
    Shift_F4=21
    Assign_F1=22
    Assign_F2=23
    Assign_F3=24
    Assign_F4=25
    Height=26
    Volume=27
    Line_width_F1=28
    Line_width_F2=29
    Line_width_F3=30
    Line_width_F4=31
    Merit=32
    Details=33
    Fit_method=34
    Vol_method=35
    SPACE_VARS=36
    RETURN_VARS=37

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
            self.state = 19
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 18
                self.match(CcpnPKParser.RETURN)


            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 9222) != 0):
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
                    self.match(CcpnPKParser.RETURN)
                    pass


                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
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

        def Assign_F1(self):
            return self.getToken(CcpnPKParser.Assign_F1, 0)

        def Assign_F2(self):
            return self.getToken(CcpnPKParser.Assign_F2, 0)

        def Height(self):
            return self.getToken(CcpnPKParser.Height, 0)

        def Volume(self):
            return self.getToken(CcpnPKParser.Volume, 0)

        def RETURN_VARS(self):
            return self.getToken(CcpnPKParser.RETURN_VARS, 0)

        def Id(self):
            return self.getToken(CcpnPKParser.Id, 0)

        def Id_(self):
            return self.getToken(CcpnPKParser.Id_, 0)

        def Position_F1(self):
            return self.getToken(CcpnPKParser.Position_F1, 0)

        def Shift_F1(self):
            return self.getToken(CcpnPKParser.Shift_F1, 0)

        def Position_F2(self):
            return self.getToken(CcpnPKParser.Position_F2, 0)

        def Shift_F2(self):
            return self.getToken(CcpnPKParser.Shift_F2, 0)

        def Number(self):
            return self.getToken(CcpnPKParser.Number, 0)

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
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 32
                self.match(CcpnPKParser.Number)


            self.state = 35
            _la = self._input.LA(1)
            if not(_la==2 or _la==13):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 36
            _la = self._input.LA(1)
            if not(_la==14 or _la==18):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 37
            _la = self._input.LA(1)
            if not(_la==15 or _la==19):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 38
            self.match(CcpnPKParser.Assign_F1)
            self.state = 39
            self.match(CcpnPKParser.Assign_F2)
            self.state = 40
            self.match(CcpnPKParser.Height)
            self.state = 41
            self.match(CcpnPKParser.Volume)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 42
                self.match(CcpnPKParser.Line_width_F1)


            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 45
                self.match(CcpnPKParser.Line_width_F2)


            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 48
                self.match(CcpnPKParser.Merit)


            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 51
                self.match(CcpnPKParser.Details)


            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 54
                self.match(CcpnPKParser.Fit_method)


            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 57
                self.match(CcpnPKParser.Vol_method)


            self.state = 60
            self.match(CcpnPKParser.RETURN_VARS)
            self.state = 62 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 61
                self.peak_2d()
                self.state = 64 
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

        def position(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.PositionContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.PositionContext,i)


        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(CcpnPKParser.Simple_name)
            else:
                return self.getToken(CcpnPKParser.Simple_name, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.NumberContext,i)


        def RETURN(self):
            return self.getToken(CcpnPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(CcpnPKParser.EOF, 0)

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
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 66
                self.match(CcpnPKParser.Integer)


            self.state = 69
            self.match(CcpnPKParser.Integer)
            self.state = 70
            self.position()
            self.state = 71
            self.position()
            self.state = 72
            self.match(CcpnPKParser.Simple_name)
            self.state = 73
            self.match(CcpnPKParser.Simple_name)
            self.state = 74
            self.number()
            self.state = 75
            self.number()
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 76
                self.position()


            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 79
                self.position()


            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0):
                self.state = 82
                self.position()


            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 85
                self.match(CcpnPKParser.Simple_name)
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 91
            _la = self._input.LA(1)
            if not(_la==-1 or _la==10):
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

        def Assign_F1(self):
            return self.getToken(CcpnPKParser.Assign_F1, 0)

        def Assign_F2(self):
            return self.getToken(CcpnPKParser.Assign_F2, 0)

        def Assign_F3(self):
            return self.getToken(CcpnPKParser.Assign_F3, 0)

        def Height(self):
            return self.getToken(CcpnPKParser.Height, 0)

        def Volume(self):
            return self.getToken(CcpnPKParser.Volume, 0)

        def RETURN_VARS(self):
            return self.getToken(CcpnPKParser.RETURN_VARS, 0)

        def Id(self):
            return self.getToken(CcpnPKParser.Id, 0)

        def Id_(self):
            return self.getToken(CcpnPKParser.Id_, 0)

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

        def Number(self):
            return self.getToken(CcpnPKParser.Number, 0)

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
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 93
                self.match(CcpnPKParser.Number)


            self.state = 96
            _la = self._input.LA(1)
            if not(_la==2 or _la==13):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 97
            _la = self._input.LA(1)
            if not(_la==14 or _la==18):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 98
            _la = self._input.LA(1)
            if not(_la==15 or _la==19):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 99
            _la = self._input.LA(1)
            if not(_la==16 or _la==20):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 100
            self.match(CcpnPKParser.Assign_F1)
            self.state = 101
            self.match(CcpnPKParser.Assign_F2)
            self.state = 102
            self.match(CcpnPKParser.Assign_F3)
            self.state = 103
            self.match(CcpnPKParser.Height)
            self.state = 104
            self.match(CcpnPKParser.Volume)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 105
                self.match(CcpnPKParser.Line_width_F1)


            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 108
                self.match(CcpnPKParser.Line_width_F2)


            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 111
                self.match(CcpnPKParser.Line_width_F3)


            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 114
                self.match(CcpnPKParser.Merit)


            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 117
                self.match(CcpnPKParser.Details)


            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 120
                self.match(CcpnPKParser.Fit_method)


            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 123
                self.match(CcpnPKParser.Vol_method)


            self.state = 126
            self.match(CcpnPKParser.RETURN_VARS)
            self.state = 128 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 127
                self.peak_3d()
                self.state = 130 
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

        def position(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.PositionContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.PositionContext,i)


        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(CcpnPKParser.Simple_name)
            else:
                return self.getToken(CcpnPKParser.Simple_name, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.NumberContext,i)


        def RETURN(self):
            return self.getToken(CcpnPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(CcpnPKParser.EOF, 0)

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
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 132
                self.match(CcpnPKParser.Integer)


            self.state = 135
            self.match(CcpnPKParser.Integer)
            self.state = 136
            self.position()
            self.state = 137
            self.position()
            self.state = 138
            self.position()
            self.state = 139
            self.match(CcpnPKParser.Simple_name)
            self.state = 140
            self.match(CcpnPKParser.Simple_name)
            self.state = 141
            self.match(CcpnPKParser.Simple_name)
            self.state = 142
            self.number()
            self.state = 143
            self.number()
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 144
                self.position()


            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 147
                self.position()


            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 150
                self.position()


            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0):
                self.state = 153
                self.position()


            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 156
                self.match(CcpnPKParser.Simple_name)
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 162
            _la = self._input.LA(1)
            if not(_la==-1 or _la==10):
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

        def Assign_F1(self):
            return self.getToken(CcpnPKParser.Assign_F1, 0)

        def Assign_F2(self):
            return self.getToken(CcpnPKParser.Assign_F2, 0)

        def Assign_F3(self):
            return self.getToken(CcpnPKParser.Assign_F3, 0)

        def Assign_F4(self):
            return self.getToken(CcpnPKParser.Assign_F4, 0)

        def Height(self):
            return self.getToken(CcpnPKParser.Height, 0)

        def Volume(self):
            return self.getToken(CcpnPKParser.Volume, 0)

        def RETURN_VARS(self):
            return self.getToken(CcpnPKParser.RETURN_VARS, 0)

        def Id(self):
            return self.getToken(CcpnPKParser.Id, 0)

        def Id_(self):
            return self.getToken(CcpnPKParser.Id_, 0)

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

        def Number(self):
            return self.getToken(CcpnPKParser.Number, 0)

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
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 164
                self.match(CcpnPKParser.Number)


            self.state = 167
            _la = self._input.LA(1)
            if not(_la==2 or _la==13):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 168
            _la = self._input.LA(1)
            if not(_la==14 or _la==18):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 169
            _la = self._input.LA(1)
            if not(_la==15 or _la==19):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 170
            _la = self._input.LA(1)
            if not(_la==16 or _la==20):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 171
            _la = self._input.LA(1)
            if not(_la==17 or _la==21):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 172
            self.match(CcpnPKParser.Assign_F1)
            self.state = 173
            self.match(CcpnPKParser.Assign_F2)
            self.state = 174
            self.match(CcpnPKParser.Assign_F3)
            self.state = 175
            self.match(CcpnPKParser.Assign_F4)
            self.state = 176
            self.match(CcpnPKParser.Height)
            self.state = 177
            self.match(CcpnPKParser.Volume)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 178
                self.match(CcpnPKParser.Line_width_F1)


            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 181
                self.match(CcpnPKParser.Line_width_F2)


            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 184
                self.match(CcpnPKParser.Line_width_F3)


            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 187
                self.match(CcpnPKParser.Line_width_F4)


            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 190
                self.match(CcpnPKParser.Merit)


            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 193
                self.match(CcpnPKParser.Details)


            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 196
                self.match(CcpnPKParser.Fit_method)


            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 199
                self.match(CcpnPKParser.Vol_method)


            self.state = 202
            self.match(CcpnPKParser.RETURN_VARS)
            self.state = 204 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 203
                self.peak_4d()
                self.state = 206 
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

        def position(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.PositionContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.PositionContext,i)


        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(CcpnPKParser.Simple_name)
            else:
                return self.getToken(CcpnPKParser.Simple_name, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CcpnPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(CcpnPKParser.NumberContext,i)


        def RETURN(self):
            return self.getToken(CcpnPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(CcpnPKParser.EOF, 0)

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
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 208
                self.match(CcpnPKParser.Integer)


            self.state = 211
            self.match(CcpnPKParser.Integer)
            self.state = 212
            self.position()
            self.state = 213
            self.position()
            self.state = 214
            self.position()
            self.state = 215
            self.position()
            self.state = 216
            self.match(CcpnPKParser.Simple_name)
            self.state = 217
            self.match(CcpnPKParser.Simple_name)
            self.state = 218
            self.match(CcpnPKParser.Simple_name)
            self.state = 219
            self.match(CcpnPKParser.Simple_name)
            self.state = 220
            self.number()
            self.state = 221
            self.number()
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 222
                self.position()


            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 225
                self.position()


            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 228
                self.position()


            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 231
                self.position()


            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0):
                self.state = 234
                self.position()


            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 237
                self.match(CcpnPKParser.Simple_name)
                self.state = 242
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 243
            _la = self._input.LA(1)
            if not(_la==-1 or _la==10):
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

        def Real(self):
            return self.getToken(CcpnPKParser.Real, 0)

        def Float(self):
            return self.getToken(CcpnPKParser.Float, 0)

        def Integer(self):
            return self.getToken(CcpnPKParser.Integer, 0)

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
            self.state = 245
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
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
            self.state = 247
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 304) != 0)):
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





