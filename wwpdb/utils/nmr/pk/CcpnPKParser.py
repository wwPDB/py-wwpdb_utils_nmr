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
        4,1,37,234,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,3,0,18,8,0,1,0,1,0,1,0,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,40,8,1,1,1,3,
        1,43,8,1,1,1,3,1,46,8,1,1,1,3,1,49,8,1,1,1,3,1,52,8,1,1,1,3,1,55,
        8,1,1,1,1,1,4,1,59,8,1,11,1,12,1,60,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,3,2,72,8,2,1,2,3,2,75,8,2,1,2,3,2,78,8,2,1,2,5,2,81,8,2,
        10,2,12,2,84,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,3,3,99,8,3,1,3,3,3,102,8,3,1,3,3,3,105,8,3,1,3,3,3,108,8,3,1,
        3,3,3,111,8,3,1,3,3,3,114,8,3,1,3,3,3,117,8,3,1,3,1,3,4,3,121,8,
        3,11,3,12,3,122,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,
        136,8,4,1,4,3,4,139,8,4,1,4,3,4,142,8,4,1,4,3,4,145,8,4,1,4,5,4,
        148,8,4,10,4,12,4,151,9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,3,5,168,8,5,1,5,3,5,171,8,5,1,5,3,5,174,8,
        5,1,5,3,5,177,8,5,1,5,3,5,180,8,5,1,5,3,5,183,8,5,1,5,3,5,186,8,
        5,1,5,3,5,189,8,5,1,5,1,5,4,5,193,8,5,11,5,12,5,194,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,210,8,6,1,6,3,6,213,
        8,6,1,6,3,6,216,8,6,1,6,3,6,219,8,6,1,6,3,6,222,8,6,1,6,5,6,225,
        8,6,10,6,12,6,228,9,6,1,6,1,6,1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,
        14,0,7,2,0,14,14,18,18,2,0,15,15,19,19,1,0,2,3,1,1,10,10,2,0,16,
        16,20,20,2,0,17,17,21,21,2,0,3,4,8,8,269,0,17,1,0,0,0,2,30,1,0,0,
        0,4,62,1,0,0,0,6,87,1,0,0,0,8,124,1,0,0,0,10,154,1,0,0,0,12,196,
        1,0,0,0,14,231,1,0,0,0,16,18,5,10,0,0,17,16,1,0,0,0,17,18,1,0,0,
        0,18,25,1,0,0,0,19,24,3,2,1,0,20,24,3,6,3,0,21,24,3,10,5,0,22,24,
        5,10,0,0,23,19,1,0,0,0,23,20,1,0,0,0,23,21,1,0,0,0,23,22,1,0,0,0,
        24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,28,1,0,0,0,27,25,1,
        0,0,0,28,29,5,0,0,1,29,1,1,0,0,0,30,31,5,1,0,0,31,32,5,13,0,0,32,
        33,7,0,0,0,33,34,7,1,0,0,34,35,5,22,0,0,35,36,5,23,0,0,36,37,5,26,
        0,0,37,39,5,27,0,0,38,40,5,28,0,0,39,38,1,0,0,0,39,40,1,0,0,0,40,
        42,1,0,0,0,41,43,5,29,0,0,42,41,1,0,0,0,42,43,1,0,0,0,43,45,1,0,
        0,0,44,46,5,32,0,0,45,44,1,0,0,0,45,46,1,0,0,0,46,48,1,0,0,0,47,
        49,5,33,0,0,48,47,1,0,0,0,48,49,1,0,0,0,49,51,1,0,0,0,50,52,5,34,
        0,0,51,50,1,0,0,0,51,52,1,0,0,0,52,54,1,0,0,0,53,55,5,35,0,0,54,
        53,1,0,0,0,54,55,1,0,0,0,55,56,1,0,0,0,56,58,5,37,0,0,57,59,3,4,
        2,0,58,57,1,0,0,0,59,60,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,3,
        1,0,0,0,62,63,5,2,0,0,63,64,5,2,0,0,64,65,5,3,0,0,65,66,5,3,0,0,
        66,67,5,8,0,0,67,68,5,8,0,0,68,69,3,14,7,0,69,71,3,14,7,0,70,72,
        5,3,0,0,71,70,1,0,0,0,71,72,1,0,0,0,72,74,1,0,0,0,73,75,5,3,0,0,
        74,73,1,0,0,0,74,75,1,0,0,0,75,77,1,0,0,0,76,78,7,2,0,0,77,76,1,
        0,0,0,77,78,1,0,0,0,78,82,1,0,0,0,79,81,5,8,0,0,80,79,1,0,0,0,81,
        84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,82,1,0,0,
        0,85,86,7,3,0,0,86,5,1,0,0,0,87,88,5,1,0,0,88,89,5,13,0,0,89,90,
        7,0,0,0,90,91,7,1,0,0,91,92,7,4,0,0,92,93,5,22,0,0,93,94,5,23,0,
        0,94,95,5,24,0,0,95,96,5,26,0,0,96,98,5,27,0,0,97,99,5,28,0,0,98,
        97,1,0,0,0,98,99,1,0,0,0,99,101,1,0,0,0,100,102,5,29,0,0,101,100,
        1,0,0,0,101,102,1,0,0,0,102,104,1,0,0,0,103,105,5,30,0,0,104,103,
        1,0,0,0,104,105,1,0,0,0,105,107,1,0,0,0,106,108,5,32,0,0,107,106,
        1,0,0,0,107,108,1,0,0,0,108,110,1,0,0,0,109,111,5,33,0,0,110,109,
        1,0,0,0,110,111,1,0,0,0,111,113,1,0,0,0,112,114,5,34,0,0,113,112,
        1,0,0,0,113,114,1,0,0,0,114,116,1,0,0,0,115,117,5,35,0,0,116,115,
        1,0,0,0,116,117,1,0,0,0,117,118,1,0,0,0,118,120,5,37,0,0,119,121,
        3,8,4,0,120,119,1,0,0,0,121,122,1,0,0,0,122,120,1,0,0,0,122,123,
        1,0,0,0,123,7,1,0,0,0,124,125,5,2,0,0,125,126,5,2,0,0,126,127,5,
        3,0,0,127,128,5,3,0,0,128,129,5,3,0,0,129,130,5,8,0,0,130,131,5,
        8,0,0,131,132,5,8,0,0,132,133,3,14,7,0,133,135,3,14,7,0,134,136,
        5,3,0,0,135,134,1,0,0,0,135,136,1,0,0,0,136,138,1,0,0,0,137,139,
        5,3,0,0,138,137,1,0,0,0,138,139,1,0,0,0,139,141,1,0,0,0,140,142,
        5,3,0,0,141,140,1,0,0,0,141,142,1,0,0,0,142,144,1,0,0,0,143,145,
        7,2,0,0,144,143,1,0,0,0,144,145,1,0,0,0,145,149,1,0,0,0,146,148,
        5,8,0,0,147,146,1,0,0,0,148,151,1,0,0,0,149,147,1,0,0,0,149,150,
        1,0,0,0,150,152,1,0,0,0,151,149,1,0,0,0,152,153,7,3,0,0,153,9,1,
        0,0,0,154,155,5,1,0,0,155,156,5,13,0,0,156,157,7,0,0,0,157,158,7,
        1,0,0,158,159,7,4,0,0,159,160,7,5,0,0,160,161,5,22,0,0,161,162,5,
        23,0,0,162,163,5,24,0,0,163,164,5,25,0,0,164,165,5,26,0,0,165,167,
        5,27,0,0,166,168,5,28,0,0,167,166,1,0,0,0,167,168,1,0,0,0,168,170,
        1,0,0,0,169,171,5,29,0,0,170,169,1,0,0,0,170,171,1,0,0,0,171,173,
        1,0,0,0,172,174,5,30,0,0,173,172,1,0,0,0,173,174,1,0,0,0,174,176,
        1,0,0,0,175,177,5,31,0,0,176,175,1,0,0,0,176,177,1,0,0,0,177,179,
        1,0,0,0,178,180,5,32,0,0,179,178,1,0,0,0,179,180,1,0,0,0,180,182,
        1,0,0,0,181,183,5,33,0,0,182,181,1,0,0,0,182,183,1,0,0,0,183,185,
        1,0,0,0,184,186,5,34,0,0,185,184,1,0,0,0,185,186,1,0,0,0,186,188,
        1,0,0,0,187,189,5,35,0,0,188,187,1,0,0,0,188,189,1,0,0,0,189,190,
        1,0,0,0,190,192,5,37,0,0,191,193,3,12,6,0,192,191,1,0,0,0,193,194,
        1,0,0,0,194,192,1,0,0,0,194,195,1,0,0,0,195,11,1,0,0,0,196,197,5,
        2,0,0,197,198,5,2,0,0,198,199,5,3,0,0,199,200,5,3,0,0,200,201,5,
        3,0,0,201,202,5,3,0,0,202,203,5,8,0,0,203,204,5,8,0,0,204,205,5,
        8,0,0,205,206,5,8,0,0,206,207,3,14,7,0,207,209,3,14,7,0,208,210,
        5,3,0,0,209,208,1,0,0,0,209,210,1,0,0,0,210,212,1,0,0,0,211,213,
        5,3,0,0,212,211,1,0,0,0,212,213,1,0,0,0,213,215,1,0,0,0,214,216,
        5,3,0,0,215,214,1,0,0,0,215,216,1,0,0,0,216,218,1,0,0,0,217,219,
        5,3,0,0,218,217,1,0,0,0,218,219,1,0,0,0,219,221,1,0,0,0,220,222,
        7,2,0,0,221,220,1,0,0,0,221,222,1,0,0,0,222,226,1,0,0,0,223,225,
        5,8,0,0,224,223,1,0,0,0,225,228,1,0,0,0,226,224,1,0,0,0,226,227,
        1,0,0,0,227,229,1,0,0,0,228,226,1,0,0,0,229,230,7,3,0,0,230,13,1,
        0,0,0,231,232,7,6,0,0,232,15,1,0,0,0,42,17,23,25,39,42,45,48,51,
        54,60,71,74,77,82,98,101,104,107,110,113,116,122,135,138,141,144,
        149,167,170,173,176,179,182,185,188,194,209,212,215,218,221,226
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
            while _la==1 or _la==10:
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

        def Number(self):
            return self.getToken(CcpnPKParser.Number, 0)

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
            self.state = 30
            self.match(CcpnPKParser.Number)
            self.state = 31
            self.match(CcpnPKParser.Id)
            self.state = 32
            _la = self._input.LA(1)
            if not(_la==14 or _la==18):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 33
            _la = self._input.LA(1)
            if not(_la==15 or _la==19):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 34
            self.match(CcpnPKParser.Assign_F1)
            self.state = 35
            self.match(CcpnPKParser.Assign_F2)
            self.state = 36
            self.match(CcpnPKParser.Height)
            self.state = 37
            self.match(CcpnPKParser.Volume)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 38
                self.match(CcpnPKParser.Line_width_F1)


            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 41
                self.match(CcpnPKParser.Line_width_F2)


            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 44
                self.match(CcpnPKParser.Merit)


            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 47
                self.match(CcpnPKParser.Details)


            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 50
                self.match(CcpnPKParser.Fit_method)


            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 53
                self.match(CcpnPKParser.Vol_method)


            self.state = 56
            self.match(CcpnPKParser.RETURN_VARS)
            self.state = 58 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 57
                self.peak_2d()
                self.state = 60 
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
            self.state = 62
            self.match(CcpnPKParser.Integer)
            self.state = 63
            self.match(CcpnPKParser.Integer)
            self.state = 64
            self.match(CcpnPKParser.Float)
            self.state = 65
            self.match(CcpnPKParser.Float)
            self.state = 66
            self.match(CcpnPKParser.Simple_name)
            self.state = 67
            self.match(CcpnPKParser.Simple_name)
            self.state = 68
            self.number()
            self.state = 69
            self.number()
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 70
                self.match(CcpnPKParser.Float)


            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 73
                self.match(CcpnPKParser.Float)


            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2 or _la==3:
                self.state = 76
                _la = self._input.LA(1)
                if not(_la==2 or _la==3):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 79
                self.match(CcpnPKParser.Simple_name)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
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

        def Number(self):
            return self.getToken(CcpnPKParser.Number, 0)

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
            self.state = 87
            self.match(CcpnPKParser.Number)
            self.state = 88
            self.match(CcpnPKParser.Id)
            self.state = 89
            _la = self._input.LA(1)
            if not(_la==14 or _la==18):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 90
            _la = self._input.LA(1)
            if not(_la==15 or _la==19):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 91
            _la = self._input.LA(1)
            if not(_la==16 or _la==20):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 92
            self.match(CcpnPKParser.Assign_F1)
            self.state = 93
            self.match(CcpnPKParser.Assign_F2)
            self.state = 94
            self.match(CcpnPKParser.Assign_F3)
            self.state = 95
            self.match(CcpnPKParser.Height)
            self.state = 96
            self.match(CcpnPKParser.Volume)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 97
                self.match(CcpnPKParser.Line_width_F1)


            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 100
                self.match(CcpnPKParser.Line_width_F2)


            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 103
                self.match(CcpnPKParser.Line_width_F3)


            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 106
                self.match(CcpnPKParser.Merit)


            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 109
                self.match(CcpnPKParser.Details)


            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 112
                self.match(CcpnPKParser.Fit_method)


            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 115
                self.match(CcpnPKParser.Vol_method)


            self.state = 118
            self.match(CcpnPKParser.RETURN_VARS)
            self.state = 120 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 119
                self.peak_3d()
                self.state = 122 
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
            self.state = 124
            self.match(CcpnPKParser.Integer)
            self.state = 125
            self.match(CcpnPKParser.Integer)
            self.state = 126
            self.match(CcpnPKParser.Float)
            self.state = 127
            self.match(CcpnPKParser.Float)
            self.state = 128
            self.match(CcpnPKParser.Float)
            self.state = 129
            self.match(CcpnPKParser.Simple_name)
            self.state = 130
            self.match(CcpnPKParser.Simple_name)
            self.state = 131
            self.match(CcpnPKParser.Simple_name)
            self.state = 132
            self.number()
            self.state = 133
            self.number()
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 134
                self.match(CcpnPKParser.Float)


            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 137
                self.match(CcpnPKParser.Float)


            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 140
                self.match(CcpnPKParser.Float)


            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2 or _la==3:
                self.state = 143
                _la = self._input.LA(1)
                if not(_la==2 or _la==3):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 146
                self.match(CcpnPKParser.Simple_name)
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 152
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

        def Number(self):
            return self.getToken(CcpnPKParser.Number, 0)

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
            self.state = 154
            self.match(CcpnPKParser.Number)
            self.state = 155
            self.match(CcpnPKParser.Id)
            self.state = 156
            _la = self._input.LA(1)
            if not(_la==14 or _la==18):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 157
            _la = self._input.LA(1)
            if not(_la==15 or _la==19):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 158
            _la = self._input.LA(1)
            if not(_la==16 or _la==20):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 159
            _la = self._input.LA(1)
            if not(_la==17 or _la==21):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 160
            self.match(CcpnPKParser.Assign_F1)
            self.state = 161
            self.match(CcpnPKParser.Assign_F2)
            self.state = 162
            self.match(CcpnPKParser.Assign_F3)
            self.state = 163
            self.match(CcpnPKParser.Assign_F4)
            self.state = 164
            self.match(CcpnPKParser.Height)
            self.state = 165
            self.match(CcpnPKParser.Volume)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 166
                self.match(CcpnPKParser.Line_width_F1)


            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 169
                self.match(CcpnPKParser.Line_width_F2)


            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 172
                self.match(CcpnPKParser.Line_width_F3)


            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 175
                self.match(CcpnPKParser.Line_width_F4)


            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 178
                self.match(CcpnPKParser.Merit)


            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 181
                self.match(CcpnPKParser.Details)


            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 184
                self.match(CcpnPKParser.Fit_method)


            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 187
                self.match(CcpnPKParser.Vol_method)


            self.state = 190
            self.match(CcpnPKParser.RETURN_VARS)
            self.state = 192 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 191
                self.peak_4d()
                self.state = 194 
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
            self.state = 196
            self.match(CcpnPKParser.Integer)
            self.state = 197
            self.match(CcpnPKParser.Integer)
            self.state = 198
            self.match(CcpnPKParser.Float)
            self.state = 199
            self.match(CcpnPKParser.Float)
            self.state = 200
            self.match(CcpnPKParser.Float)
            self.state = 201
            self.match(CcpnPKParser.Float)
            self.state = 202
            self.match(CcpnPKParser.Simple_name)
            self.state = 203
            self.match(CcpnPKParser.Simple_name)
            self.state = 204
            self.match(CcpnPKParser.Simple_name)
            self.state = 205
            self.match(CcpnPKParser.Simple_name)
            self.state = 206
            self.number()
            self.state = 207
            self.number()
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 208
                self.match(CcpnPKParser.Float)


            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 211
                self.match(CcpnPKParser.Float)


            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 214
                self.match(CcpnPKParser.Float)


            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 217
                self.match(CcpnPKParser.Float)


            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2 or _la==3:
                self.state = 220
                _la = self._input.LA(1)
                if not(_la==2 or _la==3):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 223
                self.match(CcpnPKParser.Simple_name)
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 229
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
            self.state = 231
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





