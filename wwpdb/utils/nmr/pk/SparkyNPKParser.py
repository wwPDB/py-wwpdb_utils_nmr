# Generated from SparkyNPKParser.g4 by ANTLR 4.13.0
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
        4,1,28,90,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,3,0,12,8,0,
        1,0,1,0,4,0,16,8,0,11,0,12,0,17,1,0,4,0,21,8,0,11,0,12,0,22,1,0,
        4,0,26,8,0,11,0,12,0,27,5,0,30,8,0,10,0,12,0,33,9,0,1,0,1,0,1,1,
        1,1,1,1,1,1,3,1,41,8,1,1,1,3,1,44,8,1,1,1,3,1,47,8,1,1,1,3,1,50,
        8,1,1,1,3,1,53,8,1,1,1,3,1,56,8,1,1,1,3,1,59,8,1,1,1,1,1,1,2,1,2,
        1,2,1,2,3,2,67,8,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,3,3,76,8,3,1,3,1,
        3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,86,8,4,1,4,1,4,1,4,0,0,5,0,2,4,6,8,
        0,1,1,1,14,14,102,0,11,1,0,0,0,2,36,1,0,0,0,4,62,1,0,0,0,6,70,1,
        0,0,0,8,79,1,0,0,0,10,12,5,14,0,0,11,10,1,0,0,0,11,12,1,0,0,0,12,
        31,1,0,0,0,13,30,3,2,1,0,14,16,3,4,2,0,15,14,1,0,0,0,16,17,1,0,0,
        0,17,15,1,0,0,0,17,18,1,0,0,0,18,30,1,0,0,0,19,21,3,6,3,0,20,19,
        1,0,0,0,21,22,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,30,1,0,0,0,
        24,26,3,8,4,0,25,24,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,27,28,1,
        0,0,0,28,30,1,0,0,0,29,13,1,0,0,0,29,15,1,0,0,0,29,20,1,0,0,0,29,
        25,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,34,1,0,0,
        0,33,31,1,0,0,0,34,35,5,0,0,1,35,1,1,0,0,0,36,37,5,1,0,0,37,38,5,
        18,0,0,38,40,5,19,0,0,39,41,5,20,0,0,40,39,1,0,0,0,40,41,1,0,0,0,
        41,43,1,0,0,0,42,44,5,21,0,0,43,42,1,0,0,0,43,44,1,0,0,0,44,46,1,
        0,0,0,45,47,5,22,0,0,46,45,1,0,0,0,46,47,1,0,0,0,47,49,1,0,0,0,48,
        50,5,23,0,0,49,48,1,0,0,0,49,50,1,0,0,0,50,52,1,0,0,0,51,53,5,24,
        0,0,52,51,1,0,0,0,52,53,1,0,0,0,53,55,1,0,0,0,54,56,5,25,0,0,55,
        54,1,0,0,0,55,56,1,0,0,0,56,58,1,0,0,0,57,59,5,26,0,0,58,57,1,0,
        0,0,58,59,1,0,0,0,59,60,1,0,0,0,60,61,5,28,0,0,61,3,1,0,0,0,62,63,
        5,9,0,0,63,64,5,4,0,0,64,66,5,4,0,0,65,67,5,12,0,0,66,65,1,0,0,0,
        66,67,1,0,0,0,67,68,1,0,0,0,68,69,7,0,0,0,69,5,1,0,0,0,70,71,5,10,
        0,0,71,72,5,4,0,0,72,73,5,4,0,0,73,75,5,4,0,0,74,76,5,12,0,0,75,
        74,1,0,0,0,75,76,1,0,0,0,76,77,1,0,0,0,77,78,7,0,0,0,78,7,1,0,0,
        0,79,80,5,11,0,0,80,81,5,4,0,0,81,82,5,4,0,0,82,83,5,4,0,0,83,85,
        5,4,0,0,84,86,5,12,0,0,85,84,1,0,0,0,85,86,1,0,0,0,86,87,1,0,0,0,
        87,88,7,0,0,0,88,9,1,0,0,0,16,11,17,22,27,29,31,40,43,46,49,52,55,
        58,66,75,85
    ]

class SparkyNPKParser ( Parser ):

    grammarFileName = "SparkyNPKParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'w2'", "'w3'", 
                     "'w4'", "<INVALID>", "<INVALID>", "'Volume'", "'S/N'", 
                     "'Note'" ]

    symbolicNames = [ "<INVALID>", "Assignment", "W1", "Integer", "Float", 
                      "Real", "SHARP_COMMENT", "EXCLM_COMMENT", "SMCLN_COMMENT", 
                      "Assignment_2d_ex", "Assignment_3d_ex", "Assignment_4d_ex", 
                      "Simple_name", "SPACE", "RETURN", "ENCLOSE_COMMENT", 
                      "SECTION_COMMENT", "LINE_COMMENT", "W1_LA", "W2_LA", 
                      "W3_LA", "W4_LA", "Dummy_H_LA", "Height_LA", "Volume_LA", 
                      "S_N_LA", "Note_LA", "SPACE_LA", "RETURN_LA" ]

    RULE_sparky_npk = 0
    RULE_data_label = 1
    RULE_peak_2d = 2
    RULE_peak_3d = 3
    RULE_peak_4d = 4

    ruleNames =  [ "sparky_npk", "data_label", "peak_2d", "peak_3d", "peak_4d" ]

    EOF = Token.EOF
    Assignment=1
    W1=2
    Integer=3
    Float=4
    Real=5
    SHARP_COMMENT=6
    EXCLM_COMMENT=7
    SMCLN_COMMENT=8
    Assignment_2d_ex=9
    Assignment_3d_ex=10
    Assignment_4d_ex=11
    Simple_name=12
    SPACE=13
    RETURN=14
    ENCLOSE_COMMENT=15
    SECTION_COMMENT=16
    LINE_COMMENT=17
    W1_LA=18
    W2_LA=19
    W3_LA=20
    W4_LA=21
    Dummy_H_LA=22
    Height_LA=23
    Volume_LA=24
    S_N_LA=25
    Note_LA=26
    SPACE_LA=27
    RETURN_LA=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Sparky_npkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SparkyNPKParser.EOF, 0)

        def RETURN(self):
            return self.getToken(SparkyNPKParser.RETURN, 0)

        def data_label(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.Data_labelContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.Data_labelContext,i)


        def peak_2d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.Peak_2dContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.Peak_2dContext,i)


        def peak_3d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.Peak_3dContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.Peak_3dContext,i)


        def peak_4d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.Peak_4dContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.Peak_4dContext,i)


        def getRuleIndex(self):
            return SparkyNPKParser.RULE_sparky_npk

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSparky_npk" ):
                listener.enterSparky_npk(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSparky_npk" ):
                listener.exitSparky_npk(self)




    def sparky_npk(self):

        localctx = SparkyNPKParser.Sparky_npkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sparky_npk)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 10
                self.match(SparkyNPKParser.RETURN)


            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3586) != 0):
                self.state = 29
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 13
                    self.data_label()
                    pass
                elif token in [9]:
                    self.state = 15 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 14
                            self.peak_2d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 17 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                    pass
                elif token in [10]:
                    self.state = 20 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 19
                            self.peak_3d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 22 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                    pass
                elif token in [11]:
                    self.state = 25 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 24
                            self.peak_4d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 27 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
            self.match(SparkyNPKParser.EOF)
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

        def Assignment(self):
            return self.getToken(SparkyNPKParser.Assignment, 0)

        def W1_LA(self):
            return self.getToken(SparkyNPKParser.W1_LA, 0)

        def W2_LA(self):
            return self.getToken(SparkyNPKParser.W2_LA, 0)

        def RETURN_LA(self):
            return self.getToken(SparkyNPKParser.RETURN_LA, 0)

        def W3_LA(self):
            return self.getToken(SparkyNPKParser.W3_LA, 0)

        def W4_LA(self):
            return self.getToken(SparkyNPKParser.W4_LA, 0)

        def Dummy_H_LA(self):
            return self.getToken(SparkyNPKParser.Dummy_H_LA, 0)

        def Height_LA(self):
            return self.getToken(SparkyNPKParser.Height_LA, 0)

        def Volume_LA(self):
            return self.getToken(SparkyNPKParser.Volume_LA, 0)

        def S_N_LA(self):
            return self.getToken(SparkyNPKParser.S_N_LA, 0)

        def Note_LA(self):
            return self.getToken(SparkyNPKParser.Note_LA, 0)

        def getRuleIndex(self):
            return SparkyNPKParser.RULE_data_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_label" ):
                listener.enterData_label(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_label" ):
                listener.exitData_label(self)




    def data_label(self):

        localctx = SparkyNPKParser.Data_labelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_data_label)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(SparkyNPKParser.Assignment)
            self.state = 37
            self.match(SparkyNPKParser.W1_LA)
            self.state = 38
            self.match(SparkyNPKParser.W2_LA)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 39
                self.match(SparkyNPKParser.W3_LA)


            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 42
                self.match(SparkyNPKParser.W4_LA)


            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 45
                self.match(SparkyNPKParser.Dummy_H_LA)


            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 48
                self.match(SparkyNPKParser.Height_LA)


            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 51
                self.match(SparkyNPKParser.Volume_LA)


            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 54
                self.match(SparkyNPKParser.S_N_LA)


            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 57
                self.match(SparkyNPKParser.Note_LA)


            self.state = 60
            self.match(SparkyNPKParser.RETURN_LA)
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

        def Assignment_2d_ex(self):
            return self.getToken(SparkyNPKParser.Assignment_2d_ex, 0)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(SparkyNPKParser.Float)
            else:
                return self.getToken(SparkyNPKParser.Float, i)

        def RETURN(self):
            return self.getToken(SparkyNPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(SparkyNPKParser.EOF, 0)

        def Simple_name(self):
            return self.getToken(SparkyNPKParser.Simple_name, 0)

        def getRuleIndex(self):
            return SparkyNPKParser.RULE_peak_2d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_2d" ):
                listener.enterPeak_2d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_2d" ):
                listener.exitPeak_2d(self)




    def peak_2d(self):

        localctx = SparkyNPKParser.Peak_2dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_peak_2d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(SparkyNPKParser.Assignment_2d_ex)
            self.state = 63
            self.match(SparkyNPKParser.Float)
            self.state = 64
            self.match(SparkyNPKParser.Float)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 65
                self.match(SparkyNPKParser.Simple_name)


            self.state = 68
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


    class Peak_3dContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Assignment_3d_ex(self):
            return self.getToken(SparkyNPKParser.Assignment_3d_ex, 0)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(SparkyNPKParser.Float)
            else:
                return self.getToken(SparkyNPKParser.Float, i)

        def RETURN(self):
            return self.getToken(SparkyNPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(SparkyNPKParser.EOF, 0)

        def Simple_name(self):
            return self.getToken(SparkyNPKParser.Simple_name, 0)

        def getRuleIndex(self):
            return SparkyNPKParser.RULE_peak_3d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_3d" ):
                listener.enterPeak_3d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_3d" ):
                listener.exitPeak_3d(self)




    def peak_3d(self):

        localctx = SparkyNPKParser.Peak_3dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_peak_3d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(SparkyNPKParser.Assignment_3d_ex)
            self.state = 71
            self.match(SparkyNPKParser.Float)
            self.state = 72
            self.match(SparkyNPKParser.Float)
            self.state = 73
            self.match(SparkyNPKParser.Float)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 74
                self.match(SparkyNPKParser.Simple_name)


            self.state = 77
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


    class Peak_4dContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Assignment_4d_ex(self):
            return self.getToken(SparkyNPKParser.Assignment_4d_ex, 0)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(SparkyNPKParser.Float)
            else:
                return self.getToken(SparkyNPKParser.Float, i)

        def RETURN(self):
            return self.getToken(SparkyNPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(SparkyNPKParser.EOF, 0)

        def Simple_name(self):
            return self.getToken(SparkyNPKParser.Simple_name, 0)

        def getRuleIndex(self):
            return SparkyNPKParser.RULE_peak_4d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_4d" ):
                listener.enterPeak_4d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_4d" ):
                listener.exitPeak_4d(self)




    def peak_4d(self):

        localctx = SparkyNPKParser.Peak_4dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_peak_4d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(SparkyNPKParser.Assignment_4d_ex)
            self.state = 80
            self.match(SparkyNPKParser.Float)
            self.state = 81
            self.match(SparkyNPKParser.Float)
            self.state = 82
            self.match(SparkyNPKParser.Float)
            self.state = 83
            self.match(SparkyNPKParser.Float)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 84
                self.match(SparkyNPKParser.Simple_name)


            self.state = 87
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





