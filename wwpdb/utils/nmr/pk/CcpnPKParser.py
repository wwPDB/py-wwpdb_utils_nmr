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
        4,1,37,246,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,3,0,18,8,0,1,0,1,0,1,0,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,1,0,1,1,3,1,32,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,42,
        8,1,1,1,3,1,45,8,1,1,1,3,1,48,8,1,1,1,3,1,51,8,1,1,1,3,1,54,8,1,
        1,1,3,1,57,8,1,1,1,1,1,4,1,61,8,1,11,1,12,1,62,1,2,3,2,66,8,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,76,8,2,1,2,3,2,79,8,2,1,2,3,2,
        82,8,2,1,2,5,2,85,8,2,10,2,12,2,88,9,2,1,2,1,2,1,3,3,3,93,8,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,105,8,3,1,3,3,3,108,8,
        3,1,3,3,3,111,8,3,1,3,3,3,114,8,3,1,3,3,3,117,8,3,1,3,3,3,120,8,
        3,1,3,3,3,123,8,3,1,3,1,3,4,3,127,8,3,11,3,12,3,128,1,4,3,4,132,
        8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,144,8,4,1,4,3,4,
        147,8,4,1,4,3,4,150,8,4,1,4,3,4,153,8,4,1,4,5,4,156,8,4,10,4,12,
        4,159,9,4,1,4,1,4,1,5,3,5,164,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,3,5,178,8,5,1,5,3,5,181,8,5,1,5,3,5,184,8,5,1,
        5,3,5,187,8,5,1,5,3,5,190,8,5,1,5,3,5,193,8,5,1,5,3,5,196,8,5,1,
        5,3,5,199,8,5,1,5,1,5,4,5,203,8,5,11,5,12,5,204,1,6,3,6,208,8,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,222,8,6,1,6,
        3,6,225,8,6,1,6,3,6,228,8,6,1,6,3,6,231,8,6,1,6,3,6,234,8,6,1,6,
        5,6,237,8,6,10,6,12,6,240,9,6,1,6,1,6,1,7,1,7,1,7,0,0,8,0,2,4,6,
        8,10,12,14,0,7,2,0,14,14,18,18,2,0,15,15,19,19,1,0,2,3,1,1,10,10,
        2,0,16,16,20,20,2,0,17,17,21,21,2,0,3,4,8,8,287,0,17,1,0,0,0,2,31,
        1,0,0,0,4,65,1,0,0,0,6,92,1,0,0,0,8,131,1,0,0,0,10,163,1,0,0,0,12,
        207,1,0,0,0,14,243,1,0,0,0,16,18,5,10,0,0,17,16,1,0,0,0,17,18,1,
        0,0,0,18,25,1,0,0,0,19,24,3,2,1,0,20,24,3,6,3,0,21,24,3,10,5,0,22,
        24,5,10,0,0,23,19,1,0,0,0,23,20,1,0,0,0,23,21,1,0,0,0,23,22,1,0,
        0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,28,1,0,0,0,27,25,
        1,0,0,0,28,29,5,0,0,1,29,1,1,0,0,0,30,32,5,1,0,0,31,30,1,0,0,0,31,
        32,1,0,0,0,32,33,1,0,0,0,33,34,5,13,0,0,34,35,7,0,0,0,35,36,7,1,
        0,0,36,37,5,22,0,0,37,38,5,23,0,0,38,39,5,26,0,0,39,41,5,27,0,0,
        40,42,5,28,0,0,41,40,1,0,0,0,41,42,1,0,0,0,42,44,1,0,0,0,43,45,5,
        29,0,0,44,43,1,0,0,0,44,45,1,0,0,0,45,47,1,0,0,0,46,48,5,32,0,0,
        47,46,1,0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,49,51,5,33,0,0,50,49,1,
        0,0,0,50,51,1,0,0,0,51,53,1,0,0,0,52,54,5,34,0,0,53,52,1,0,0,0,53,
        54,1,0,0,0,54,56,1,0,0,0,55,57,5,35,0,0,56,55,1,0,0,0,56,57,1,0,
        0,0,57,58,1,0,0,0,58,60,5,37,0,0,59,61,3,4,2,0,60,59,1,0,0,0,61,
        62,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,3,1,0,0,0,64,66,5,2,0,
        0,65,64,1,0,0,0,65,66,1,0,0,0,66,67,1,0,0,0,67,68,5,2,0,0,68,69,
        5,3,0,0,69,70,5,3,0,0,70,71,5,8,0,0,71,72,5,8,0,0,72,73,3,14,7,0,
        73,75,3,14,7,0,74,76,5,3,0,0,75,74,1,0,0,0,75,76,1,0,0,0,76,78,1,
        0,0,0,77,79,5,3,0,0,78,77,1,0,0,0,78,79,1,0,0,0,79,81,1,0,0,0,80,
        82,7,2,0,0,81,80,1,0,0,0,81,82,1,0,0,0,82,86,1,0,0,0,83,85,5,8,0,
        0,84,83,1,0,0,0,85,88,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,89,
        1,0,0,0,88,86,1,0,0,0,89,90,7,3,0,0,90,5,1,0,0,0,91,93,5,1,0,0,92,
        91,1,0,0,0,92,93,1,0,0,0,93,94,1,0,0,0,94,95,5,13,0,0,95,96,7,0,
        0,0,96,97,7,1,0,0,97,98,7,4,0,0,98,99,5,22,0,0,99,100,5,23,0,0,100,
        101,5,24,0,0,101,102,5,26,0,0,102,104,5,27,0,0,103,105,5,28,0,0,
        104,103,1,0,0,0,104,105,1,0,0,0,105,107,1,0,0,0,106,108,5,29,0,0,
        107,106,1,0,0,0,107,108,1,0,0,0,108,110,1,0,0,0,109,111,5,30,0,0,
        110,109,1,0,0,0,110,111,1,0,0,0,111,113,1,0,0,0,112,114,5,32,0,0,
        113,112,1,0,0,0,113,114,1,0,0,0,114,116,1,0,0,0,115,117,5,33,0,0,
        116,115,1,0,0,0,116,117,1,0,0,0,117,119,1,0,0,0,118,120,5,34,0,0,
        119,118,1,0,0,0,119,120,1,0,0,0,120,122,1,0,0,0,121,123,5,35,0,0,
        122,121,1,0,0,0,122,123,1,0,0,0,123,124,1,0,0,0,124,126,5,37,0,0,
        125,127,3,8,4,0,126,125,1,0,0,0,127,128,1,0,0,0,128,126,1,0,0,0,
        128,129,1,0,0,0,129,7,1,0,0,0,130,132,5,2,0,0,131,130,1,0,0,0,131,
        132,1,0,0,0,132,133,1,0,0,0,133,134,5,2,0,0,134,135,5,3,0,0,135,
        136,5,3,0,0,136,137,5,3,0,0,137,138,5,8,0,0,138,139,5,8,0,0,139,
        140,5,8,0,0,140,141,3,14,7,0,141,143,3,14,7,0,142,144,5,3,0,0,143,
        142,1,0,0,0,143,144,1,0,0,0,144,146,1,0,0,0,145,147,5,3,0,0,146,
        145,1,0,0,0,146,147,1,0,0,0,147,149,1,0,0,0,148,150,5,3,0,0,149,
        148,1,0,0,0,149,150,1,0,0,0,150,152,1,0,0,0,151,153,7,2,0,0,152,
        151,1,0,0,0,152,153,1,0,0,0,153,157,1,0,0,0,154,156,5,8,0,0,155,
        154,1,0,0,0,156,159,1,0,0,0,157,155,1,0,0,0,157,158,1,0,0,0,158,
        160,1,0,0,0,159,157,1,0,0,0,160,161,7,3,0,0,161,9,1,0,0,0,162,164,
        5,1,0,0,163,162,1,0,0,0,163,164,1,0,0,0,164,165,1,0,0,0,165,166,
        5,13,0,0,166,167,7,0,0,0,167,168,7,1,0,0,168,169,7,4,0,0,169,170,
        7,5,0,0,170,171,5,22,0,0,171,172,5,23,0,0,172,173,5,24,0,0,173,174,
        5,25,0,0,174,175,5,26,0,0,175,177,5,27,0,0,176,178,5,28,0,0,177,
        176,1,0,0,0,177,178,1,0,0,0,178,180,1,0,0,0,179,181,5,29,0,0,180,
        179,1,0,0,0,180,181,1,0,0,0,181,183,1,0,0,0,182,184,5,30,0,0,183,
        182,1,0,0,0,183,184,1,0,0,0,184,186,1,0,0,0,185,187,5,31,0,0,186,
        185,1,0,0,0,186,187,1,0,0,0,187,189,1,0,0,0,188,190,5,32,0,0,189,
        188,1,0,0,0,189,190,1,0,0,0,190,192,1,0,0,0,191,193,5,33,0,0,192,
        191,1,0,0,0,192,193,1,0,0,0,193,195,1,0,0,0,194,196,5,34,0,0,195,
        194,1,0,0,0,195,196,1,0,0,0,196,198,1,0,0,0,197,199,5,35,0,0,198,
        197,1,0,0,0,198,199,1,0,0,0,199,200,1,0,0,0,200,202,5,37,0,0,201,
        203,3,12,6,0,202,201,1,0,0,0,203,204,1,0,0,0,204,202,1,0,0,0,204,
        205,1,0,0,0,205,11,1,0,0,0,206,208,5,2,0,0,207,206,1,0,0,0,207,208,
        1,0,0,0,208,209,1,0,0,0,209,210,5,2,0,0,210,211,5,3,0,0,211,212,
        5,3,0,0,212,213,5,3,0,0,213,214,5,3,0,0,214,215,5,8,0,0,215,216,
        5,8,0,0,216,217,5,8,0,0,217,218,5,8,0,0,218,219,3,14,7,0,219,221,
        3,14,7,0,220,222,5,3,0,0,221,220,1,0,0,0,221,222,1,0,0,0,222,224,
        1,0,0,0,223,225,5,3,0,0,224,223,1,0,0,0,224,225,1,0,0,0,225,227,
        1,0,0,0,226,228,5,3,0,0,227,226,1,0,0,0,227,228,1,0,0,0,228,230,
        1,0,0,0,229,231,5,3,0,0,230,229,1,0,0,0,230,231,1,0,0,0,231,233,
        1,0,0,0,232,234,7,2,0,0,233,232,1,0,0,0,233,234,1,0,0,0,234,238,
        1,0,0,0,235,237,5,8,0,0,236,235,1,0,0,0,237,240,1,0,0,0,238,236,
        1,0,0,0,238,239,1,0,0,0,239,241,1,0,0,0,240,238,1,0,0,0,241,242,
        7,3,0,0,242,13,1,0,0,0,243,244,7,6,0,0,244,15,1,0,0,0,48,17,23,25,
        31,41,44,47,50,53,56,62,65,75,78,81,86,92,104,107,110,113,116,119,
        122,128,131,143,146,149,152,157,163,177,180,183,186,189,192,195,
        198,204,207,221,224,227,230,233,238
    ]

class CcpnPKParser ( Parser ):

    grammarFileName = "CcpnPKParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Number'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'#'", "'Position F1'", "'Position F2'", 
                     "'Position F3'", "'Position F4'", "'Shift F1'", "'Shift F2'", 
                     "'Shift F3'", "'Shift F4'", "'Assign F1'", "'Assign F2'", 
                     "'Assign F3'", "'Assign F4'", "'Height'", "'Volume'", 
                     "'Line Width F1 (Hz)'", "'Line Width F2 (Hz)'", "'Line Width F3 (Hz)'", 
                     "'Line Width F4 (Hz)'", "'Merit'", "'Details'", "'Fit Method'", 
                     "'Vol. Method'" ]

    symbolicNames = [ "<INVALID>", "Number", "Integer", "Float", "Real", 
                      "SHARP_COMMENT", "EXCLM_COMMENT", "SMCLN_COMMENT", 
                      "Simple_name", "SPACE", "RETURN", "SECTION_COMMENT", 
                      "LINE_COMMENT", "Id", "Position_F1", "Position_F2", 
                      "Position_F3", "Position_F4", "Shift_F1", "Shift_F2", 
                      "Shift_F3", "Shift_F4", "Assign_F1", "Assign_F2", 
                      "Assign_F3", "Assign_F4", "Height", "Volume", "Line_width_F1", 
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
    RULE_number = 7

    ruleNames =  [ "ccpn_pk", "peak_list_2d", "peak_2d", "peak_list_3d", 
                   "peak_3d", "peak_list_4d", "peak_4d", "number" ]

    EOF = Token.EOF
    Number=1
    Integer=2
    Float=3
    Real=4
    SHARP_COMMENT=5
    EXCLM_COMMENT=6
    SMCLN_COMMENT=7
    Simple_name=8
    SPACE=9
    RETURN=10
    SECTION_COMMENT=11
    LINE_COMMENT=12
    Id=13
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
            self.state = 17
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 16
                self.match(CcpnPKParser.RETURN)


            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 9218) != 0):
                self.state = 23
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 19
                    self.peak_list_2d()
                    pass

                elif la_ == 2:
                    self.state = 20
                    self.peak_list_3d()
                    pass

                elif la_ == 3:
                    self.state = 21
                    self.peak_list_4d()
                    pass

                elif la_ == 4:
                    self.state = 22
                    self.match(CcpnPKParser.RETURN)
                    pass


                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
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

        def Id(self):
            return self.getToken(CcpnPKParser.Id, 0)

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
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 30
                self.match(CcpnPKParser.Number)


            self.state = 33
            self.match(CcpnPKParser.Id)
            self.state = 34
            _la = self._input.LA(1)
            if not(_la==14 or _la==18):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 35
            _la = self._input.LA(1)
            if not(_la==15 or _la==19):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 36
            self.match(CcpnPKParser.Assign_F1)
            self.state = 37
            self.match(CcpnPKParser.Assign_F2)
            self.state = 38
            self.match(CcpnPKParser.Height)
            self.state = 39
            self.match(CcpnPKParser.Volume)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 40
                self.match(CcpnPKParser.Line_width_F1)


            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 43
                self.match(CcpnPKParser.Line_width_F2)


            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 46
                self.match(CcpnPKParser.Merit)


            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 49
                self.match(CcpnPKParser.Details)


            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 52
                self.match(CcpnPKParser.Fit_method)


            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 55
                self.match(CcpnPKParser.Vol_method)


            self.state = 58
            self.match(CcpnPKParser.RETURN_VARS)
            self.state = 60 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 59
                self.peak_2d()
                self.state = 62 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2):
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

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(CcpnPKParser.Float)
            else:
                return self.getToken(CcpnPKParser.Float, i)

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
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 64
                self.match(CcpnPKParser.Integer)


            self.state = 67
            self.match(CcpnPKParser.Integer)
            self.state = 68
            self.match(CcpnPKParser.Float)
            self.state = 69
            self.match(CcpnPKParser.Float)
            self.state = 70
            self.match(CcpnPKParser.Simple_name)
            self.state = 71
            self.match(CcpnPKParser.Simple_name)
            self.state = 72
            self.number()
            self.state = 73
            self.number()
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 74
                self.match(CcpnPKParser.Float)


            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 77
                self.match(CcpnPKParser.Float)


            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2 or _la==3:
                self.state = 80
                _la = self._input.LA(1)
                if not(_la==2 or _la==3):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 83
                self.match(CcpnPKParser.Simple_name)
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
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

        def Id(self):
            return self.getToken(CcpnPKParser.Id, 0)

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
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 91
                self.match(CcpnPKParser.Number)


            self.state = 94
            self.match(CcpnPKParser.Id)
            self.state = 95
            _la = self._input.LA(1)
            if not(_la==14 or _la==18):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 96
            _la = self._input.LA(1)
            if not(_la==15 or _la==19):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 97
            _la = self._input.LA(1)
            if not(_la==16 or _la==20):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 98
            self.match(CcpnPKParser.Assign_F1)
            self.state = 99
            self.match(CcpnPKParser.Assign_F2)
            self.state = 100
            self.match(CcpnPKParser.Assign_F3)
            self.state = 101
            self.match(CcpnPKParser.Height)
            self.state = 102
            self.match(CcpnPKParser.Volume)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 103
                self.match(CcpnPKParser.Line_width_F1)


            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 106
                self.match(CcpnPKParser.Line_width_F2)


            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 109
                self.match(CcpnPKParser.Line_width_F3)


            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 112
                self.match(CcpnPKParser.Merit)


            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 115
                self.match(CcpnPKParser.Details)


            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 118
                self.match(CcpnPKParser.Fit_method)


            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 121
                self.match(CcpnPKParser.Vol_method)


            self.state = 124
            self.match(CcpnPKParser.RETURN_VARS)
            self.state = 126 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 125
                self.peak_3d()
                self.state = 128 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2):
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

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(CcpnPKParser.Float)
            else:
                return self.getToken(CcpnPKParser.Float, i)

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
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 130
                self.match(CcpnPKParser.Integer)


            self.state = 133
            self.match(CcpnPKParser.Integer)
            self.state = 134
            self.match(CcpnPKParser.Float)
            self.state = 135
            self.match(CcpnPKParser.Float)
            self.state = 136
            self.match(CcpnPKParser.Float)
            self.state = 137
            self.match(CcpnPKParser.Simple_name)
            self.state = 138
            self.match(CcpnPKParser.Simple_name)
            self.state = 139
            self.match(CcpnPKParser.Simple_name)
            self.state = 140
            self.number()
            self.state = 141
            self.number()
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 142
                self.match(CcpnPKParser.Float)


            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 145
                self.match(CcpnPKParser.Float)


            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 148
                self.match(CcpnPKParser.Float)


            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2 or _la==3:
                self.state = 151
                _la = self._input.LA(1)
                if not(_la==2 or _la==3):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 154
                self.match(CcpnPKParser.Simple_name)
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 160
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

        def Id(self):
            return self.getToken(CcpnPKParser.Id, 0)

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
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 162
                self.match(CcpnPKParser.Number)


            self.state = 165
            self.match(CcpnPKParser.Id)
            self.state = 166
            _la = self._input.LA(1)
            if not(_la==14 or _la==18):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 167
            _la = self._input.LA(1)
            if not(_la==15 or _la==19):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 168
            _la = self._input.LA(1)
            if not(_la==16 or _la==20):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 169
            _la = self._input.LA(1)
            if not(_la==17 or _la==21):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 170
            self.match(CcpnPKParser.Assign_F1)
            self.state = 171
            self.match(CcpnPKParser.Assign_F2)
            self.state = 172
            self.match(CcpnPKParser.Assign_F3)
            self.state = 173
            self.match(CcpnPKParser.Assign_F4)
            self.state = 174
            self.match(CcpnPKParser.Height)
            self.state = 175
            self.match(CcpnPKParser.Volume)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 176
                self.match(CcpnPKParser.Line_width_F1)


            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 179
                self.match(CcpnPKParser.Line_width_F2)


            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 182
                self.match(CcpnPKParser.Line_width_F3)


            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 185
                self.match(CcpnPKParser.Line_width_F4)


            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 188
                self.match(CcpnPKParser.Merit)


            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 191
                self.match(CcpnPKParser.Details)


            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 194
                self.match(CcpnPKParser.Fit_method)


            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 197
                self.match(CcpnPKParser.Vol_method)


            self.state = 200
            self.match(CcpnPKParser.RETURN_VARS)
            self.state = 202 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 201
                self.peak_4d()
                self.state = 204 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2):
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

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(CcpnPKParser.Float)
            else:
                return self.getToken(CcpnPKParser.Float, i)

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
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 206
                self.match(CcpnPKParser.Integer)


            self.state = 209
            self.match(CcpnPKParser.Integer)
            self.state = 210
            self.match(CcpnPKParser.Float)
            self.state = 211
            self.match(CcpnPKParser.Float)
            self.state = 212
            self.match(CcpnPKParser.Float)
            self.state = 213
            self.match(CcpnPKParser.Float)
            self.state = 214
            self.match(CcpnPKParser.Simple_name)
            self.state = 215
            self.match(CcpnPKParser.Simple_name)
            self.state = 216
            self.match(CcpnPKParser.Simple_name)
            self.state = 217
            self.match(CcpnPKParser.Simple_name)
            self.state = 218
            self.number()
            self.state = 219
            self.number()
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 220
                self.match(CcpnPKParser.Float)


            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 223
                self.match(CcpnPKParser.Float)


            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 226
                self.match(CcpnPKParser.Float)


            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 229
                self.match(CcpnPKParser.Float)


            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2 or _la==3:
                self.state = 232
                _la = self._input.LA(1)
                if not(_la==2 or _la==3):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 235
                self.match(CcpnPKParser.Simple_name)
                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 241
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
        self.enterRule(localctx, 14, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 280) != 0)):
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





