# Generated from VnmrPKParser.g4 by ANTLR 4.13.0
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
        4,1,27,99,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,3,
        0,14,8,0,1,0,1,0,4,0,18,8,0,11,0,12,0,19,1,0,4,0,23,8,0,11,0,12,
        0,24,1,0,4,0,28,8,0,11,0,12,0,29,5,0,32,8,0,10,0,12,0,35,9,0,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,48,8,1,3,1,50,8,1,1,
        1,1,1,3,1,54,8,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,65,8,2,
        1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,78,8,3,1,3,1,3,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,93,8,4,1,4,1,4,1,5,
        1,5,1,5,0,0,6,0,2,4,6,8,10,0,1,1,0,2,4,106,0,13,1,0,0,0,2,38,1,0,
        0,0,4,57,1,0,0,0,6,68,1,0,0,0,8,81,1,0,0,0,10,96,1,0,0,0,12,14,5,
        12,0,0,13,12,1,0,0,0,13,14,1,0,0,0,14,33,1,0,0,0,15,32,3,2,1,0,16,
        18,3,4,2,0,17,16,1,0,0,0,18,19,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,
        0,20,32,1,0,0,0,21,23,3,6,3,0,22,21,1,0,0,0,23,24,1,0,0,0,24,22,
        1,0,0,0,24,25,1,0,0,0,25,32,1,0,0,0,26,28,3,8,4,0,27,26,1,0,0,0,
        28,29,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,32,1,0,0,0,31,15,1,
        0,0,0,31,17,1,0,0,0,31,22,1,0,0,0,31,27,1,0,0,0,32,35,1,0,0,0,33,
        31,1,0,0,0,33,34,1,0,0,0,34,36,1,0,0,0,35,33,1,0,0,0,36,37,5,0,0,
        1,37,1,1,0,0,0,38,39,5,1,0,0,39,40,5,16,0,0,40,41,5,20,0,0,41,42,
        5,17,0,0,42,49,5,21,0,0,43,44,5,18,0,0,44,47,5,22,0,0,45,46,5,19,
        0,0,46,48,5,23,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,49,
        43,1,0,0,0,49,50,1,0,0,0,50,51,1,0,0,0,51,53,5,24,0,0,52,54,5,25,
        0,0,53,52,1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,0,55,56,5,27,0,0,56,
        3,1,0,0,0,57,58,5,2,0,0,58,59,5,3,0,0,59,60,5,3,0,0,60,61,5,3,0,
        0,61,62,5,3,0,0,62,64,3,10,5,0,63,65,5,8,0,0,64,63,1,0,0,0,64,65,
        1,0,0,0,65,66,1,0,0,0,66,67,5,12,0,0,67,5,1,0,0,0,68,69,5,2,0,0,
        69,70,5,3,0,0,70,71,5,3,0,0,71,72,5,3,0,0,72,73,5,3,0,0,73,74,5,
        3,0,0,74,75,5,3,0,0,75,77,3,10,5,0,76,78,5,9,0,0,77,76,1,0,0,0,77,
        78,1,0,0,0,78,79,1,0,0,0,79,80,5,12,0,0,80,7,1,0,0,0,81,82,5,2,0,
        0,82,83,5,3,0,0,83,84,5,3,0,0,84,85,5,3,0,0,85,86,5,3,0,0,86,87,
        5,3,0,0,87,88,5,3,0,0,88,89,5,3,0,0,89,90,5,3,0,0,90,92,3,10,5,0,
        91,93,5,10,0,0,92,91,1,0,0,0,92,93,1,0,0,0,93,94,1,0,0,0,94,95,5,
        12,0,0,95,9,1,0,0,0,96,97,7,0,0,0,97,11,1,0,0,0,12,13,19,24,29,31,
        33,47,49,53,64,77,92
    ]

class VnmrPKParser ( Parser ):

    grammarFileName = "VnmrPKParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'peak id.'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Dim 0 (ppm)'", "'Dim 1 (ppm)'", "'Dim 2 (ppm)'", 
                     "'Dim 3 (ppm)'", "'Dev. 0'", "'Dev. 1'", "'Dev. 2'", 
                     "'Dev. 3'", "'Amplitude'", "'Assignment'" ]

    symbolicNames = [ "<INVALID>", "Peak_id", "Integer", "Float", "Real", 
                      "SHARP_COMMENT", "EXCLM_COMMENT", "SMCLN_COMMENT", 
                      "Assignment_2d_ex", "Assignment_3d_ex", "Assignment_4d_ex", 
                      "SPACE", "RETURN", "ENCLOSE_COMMENT", "SECTION_COMMENT", 
                      "LINE_COMMENT", "Dim_0_ppm", "Dim_1_ppm", "Dim_2_ppm", 
                      "Dim_3_ppm", "Dev_0", "Dev_1", "Dev_2", "Dev_3", "Amplitude", 
                      "Assignment", "SPACE_LA", "RETURN_LA" ]

    RULE_vnmr_pk = 0
    RULE_data_label = 1
    RULE_peak_2d = 2
    RULE_peak_3d = 3
    RULE_peak_4d = 4
    RULE_number = 5

    ruleNames =  [ "vnmr_pk", "data_label", "peak_2d", "peak_3d", "peak_4d", 
                   "number" ]

    EOF = Token.EOF
    Peak_id=1
    Integer=2
    Float=3
    Real=4
    SHARP_COMMENT=5
    EXCLM_COMMENT=6
    SMCLN_COMMENT=7
    Assignment_2d_ex=8
    Assignment_3d_ex=9
    Assignment_4d_ex=10
    SPACE=11
    RETURN=12
    ENCLOSE_COMMENT=13
    SECTION_COMMENT=14
    LINE_COMMENT=15
    Dim_0_ppm=16
    Dim_1_ppm=17
    Dim_2_ppm=18
    Dim_3_ppm=19
    Dev_0=20
    Dev_1=21
    Dev_2=22
    Dev_3=23
    Amplitude=24
    Assignment=25
    SPACE_LA=26
    RETURN_LA=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Vnmr_pkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(VnmrPKParser.EOF, 0)

        def RETURN(self):
            return self.getToken(VnmrPKParser.RETURN, 0)

        def data_label(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VnmrPKParser.Data_labelContext)
            else:
                return self.getTypedRuleContext(VnmrPKParser.Data_labelContext,i)


        def peak_2d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VnmrPKParser.Peak_2dContext)
            else:
                return self.getTypedRuleContext(VnmrPKParser.Peak_2dContext,i)


        def peak_3d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VnmrPKParser.Peak_3dContext)
            else:
                return self.getTypedRuleContext(VnmrPKParser.Peak_3dContext,i)


        def peak_4d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VnmrPKParser.Peak_4dContext)
            else:
                return self.getTypedRuleContext(VnmrPKParser.Peak_4dContext,i)


        def getRuleIndex(self):
            return VnmrPKParser.RULE_vnmr_pk

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVnmr_pk" ):
                listener.enterVnmr_pk(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVnmr_pk" ):
                listener.exitVnmr_pk(self)




    def vnmr_pk(self):

        localctx = VnmrPKParser.Vnmr_pkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_vnmr_pk)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 12
                self.match(VnmrPKParser.RETURN)


            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 31
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 15
                    self.data_label()
                    pass

                elif la_ == 2:
                    self.state = 17 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 16
                            self.peak_2d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 19 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                    pass

                elif la_ == 3:
                    self.state = 22 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 21
                            self.peak_3d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 24 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                    pass

                elif la_ == 4:
                    self.state = 27 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 26
                            self.peak_4d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 29 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                    pass


                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 36
            self.match(VnmrPKParser.EOF)
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

        def Peak_id(self):
            return self.getToken(VnmrPKParser.Peak_id, 0)

        def Dim_0_ppm(self):
            return self.getToken(VnmrPKParser.Dim_0_ppm, 0)

        def Dev_0(self):
            return self.getToken(VnmrPKParser.Dev_0, 0)

        def Dim_1_ppm(self):
            return self.getToken(VnmrPKParser.Dim_1_ppm, 0)

        def Dev_1(self):
            return self.getToken(VnmrPKParser.Dev_1, 0)

        def Amplitude(self):
            return self.getToken(VnmrPKParser.Amplitude, 0)

        def RETURN_LA(self):
            return self.getToken(VnmrPKParser.RETURN_LA, 0)

        def Dim_2_ppm(self):
            return self.getToken(VnmrPKParser.Dim_2_ppm, 0)

        def Dev_2(self):
            return self.getToken(VnmrPKParser.Dev_2, 0)

        def Assignment(self):
            return self.getToken(VnmrPKParser.Assignment, 0)

        def Dim_3_ppm(self):
            return self.getToken(VnmrPKParser.Dim_3_ppm, 0)

        def Dev_3(self):
            return self.getToken(VnmrPKParser.Dev_3, 0)

        def getRuleIndex(self):
            return VnmrPKParser.RULE_data_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_label" ):
                listener.enterData_label(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_label" ):
                listener.exitData_label(self)




    def data_label(self):

        localctx = VnmrPKParser.Data_labelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_data_label)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(VnmrPKParser.Peak_id)
            self.state = 39
            self.match(VnmrPKParser.Dim_0_ppm)
            self.state = 40
            self.match(VnmrPKParser.Dev_0)
            self.state = 41
            self.match(VnmrPKParser.Dim_1_ppm)
            self.state = 42
            self.match(VnmrPKParser.Dev_1)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 43
                self.match(VnmrPKParser.Dim_2_ppm)
                self.state = 44
                self.match(VnmrPKParser.Dev_2)
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
                    self.state = 45
                    self.match(VnmrPKParser.Dim_3_ppm)
                    self.state = 46
                    self.match(VnmrPKParser.Dev_3)




            self.state = 51
            self.match(VnmrPKParser.Amplitude)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 52
                self.match(VnmrPKParser.Assignment)


            self.state = 55
            self.match(VnmrPKParser.RETURN_LA)
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

        def Integer(self):
            return self.getToken(VnmrPKParser.Integer, 0)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(VnmrPKParser.Float)
            else:
                return self.getToken(VnmrPKParser.Float, i)

        def number(self):
            return self.getTypedRuleContext(VnmrPKParser.NumberContext,0)


        def RETURN(self):
            return self.getToken(VnmrPKParser.RETURN, 0)

        def Assignment_2d_ex(self):
            return self.getToken(VnmrPKParser.Assignment_2d_ex, 0)

        def getRuleIndex(self):
            return VnmrPKParser.RULE_peak_2d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_2d" ):
                listener.enterPeak_2d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_2d" ):
                listener.exitPeak_2d(self)




    def peak_2d(self):

        localctx = VnmrPKParser.Peak_2dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_peak_2d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(VnmrPKParser.Integer)
            self.state = 58
            self.match(VnmrPKParser.Float)
            self.state = 59
            self.match(VnmrPKParser.Float)
            self.state = 60
            self.match(VnmrPKParser.Float)
            self.state = 61
            self.match(VnmrPKParser.Float)
            self.state = 62
            self.number()
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 63
                self.match(VnmrPKParser.Assignment_2d_ex)


            self.state = 66
            self.match(VnmrPKParser.RETURN)
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

        def Integer(self):
            return self.getToken(VnmrPKParser.Integer, 0)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(VnmrPKParser.Float)
            else:
                return self.getToken(VnmrPKParser.Float, i)

        def number(self):
            return self.getTypedRuleContext(VnmrPKParser.NumberContext,0)


        def RETURN(self):
            return self.getToken(VnmrPKParser.RETURN, 0)

        def Assignment_3d_ex(self):
            return self.getToken(VnmrPKParser.Assignment_3d_ex, 0)

        def getRuleIndex(self):
            return VnmrPKParser.RULE_peak_3d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_3d" ):
                listener.enterPeak_3d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_3d" ):
                listener.exitPeak_3d(self)




    def peak_3d(self):

        localctx = VnmrPKParser.Peak_3dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_peak_3d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(VnmrPKParser.Integer)
            self.state = 69
            self.match(VnmrPKParser.Float)
            self.state = 70
            self.match(VnmrPKParser.Float)
            self.state = 71
            self.match(VnmrPKParser.Float)
            self.state = 72
            self.match(VnmrPKParser.Float)
            self.state = 73
            self.match(VnmrPKParser.Float)
            self.state = 74
            self.match(VnmrPKParser.Float)
            self.state = 75
            self.number()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 76
                self.match(VnmrPKParser.Assignment_3d_ex)


            self.state = 79
            self.match(VnmrPKParser.RETURN)
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

        def Integer(self):
            return self.getToken(VnmrPKParser.Integer, 0)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(VnmrPKParser.Float)
            else:
                return self.getToken(VnmrPKParser.Float, i)

        def number(self):
            return self.getTypedRuleContext(VnmrPKParser.NumberContext,0)


        def RETURN(self):
            return self.getToken(VnmrPKParser.RETURN, 0)

        def Assignment_4d_ex(self):
            return self.getToken(VnmrPKParser.Assignment_4d_ex, 0)

        def getRuleIndex(self):
            return VnmrPKParser.RULE_peak_4d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_4d" ):
                listener.enterPeak_4d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_4d" ):
                listener.exitPeak_4d(self)




    def peak_4d(self):

        localctx = VnmrPKParser.Peak_4dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_peak_4d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(VnmrPKParser.Integer)
            self.state = 82
            self.match(VnmrPKParser.Float)
            self.state = 83
            self.match(VnmrPKParser.Float)
            self.state = 84
            self.match(VnmrPKParser.Float)
            self.state = 85
            self.match(VnmrPKParser.Float)
            self.state = 86
            self.match(VnmrPKParser.Float)
            self.state = 87
            self.match(VnmrPKParser.Float)
            self.state = 88
            self.match(VnmrPKParser.Float)
            self.state = 89
            self.match(VnmrPKParser.Float)
            self.state = 90
            self.number()
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 91
                self.match(VnmrPKParser.Assignment_4d_ex)


            self.state = 94
            self.match(VnmrPKParser.RETURN)
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

        def Real(self):
            return self.getToken(VnmrPKParser.Real, 0)

        def Float(self):
            return self.getToken(VnmrPKParser.Float, 0)

        def Integer(self):
            return self.getToken(VnmrPKParser.Integer, 0)

        def getRuleIndex(self):
            return VnmrPKParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = VnmrPKParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0)):
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





