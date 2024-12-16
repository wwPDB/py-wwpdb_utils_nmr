# Generated from SparkyPKParser.g4 by ANTLR 4.13.0
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
        4,1,25,125,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,3,0,18,8,0,1,0,1,0,1,0,4,0,23,8,0,11,0,12,0,24,1,0,
        4,0,28,8,0,11,0,12,0,29,1,0,4,0,33,8,0,11,0,12,0,34,5,0,37,8,0,10,
        0,12,0,40,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,48,8,1,1,1,3,1,51,8,1,
        1,1,1,1,3,1,55,8,1,1,1,3,1,58,8,1,1,1,1,1,1,2,1,2,1,2,3,2,65,8,2,
        1,2,3,2,68,8,2,1,2,1,2,3,2,72,8,2,1,2,3,2,75,8,2,1,2,1,2,4,2,79,
        8,2,11,2,12,2,80,1,3,1,3,1,3,1,3,4,3,87,8,3,11,3,12,3,88,1,3,1,3,
        1,4,1,4,1,4,1,4,1,4,4,4,98,8,4,11,4,12,4,99,1,4,1,4,1,5,1,5,1,5,
        1,5,1,5,1,5,4,5,110,8,5,11,5,12,5,111,1,5,1,5,1,6,4,6,117,8,6,11,
        6,12,6,118,1,6,1,6,1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,1,1,0,
        3,5,138,0,17,1,0,0,0,2,43,1,0,0,0,4,61,1,0,0,0,6,82,1,0,0,0,8,92,
        1,0,0,0,10,103,1,0,0,0,12,116,1,0,0,0,14,122,1,0,0,0,16,18,5,13,
        0,0,17,16,1,0,0,0,17,18,1,0,0,0,18,38,1,0,0,0,19,37,3,2,1,0,20,37,
        3,4,2,0,21,23,3,6,3,0,22,21,1,0,0,0,23,24,1,0,0,0,24,22,1,0,0,0,
        24,25,1,0,0,0,25,37,1,0,0,0,26,28,3,8,4,0,27,26,1,0,0,0,28,29,1,
        0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,37,1,0,0,0,31,33,3,10,5,0,32,
        31,1,0,0,0,33,34,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,37,1,0,0,
        0,36,19,1,0,0,0,36,20,1,0,0,0,36,22,1,0,0,0,36,27,1,0,0,0,36,32,
        1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,41,1,0,0,0,
        40,38,1,0,0,0,41,42,5,0,0,1,42,1,1,0,0,0,43,44,5,1,0,0,44,45,5,17,
        0,0,45,47,5,18,0,0,46,48,5,19,0,0,47,46,1,0,0,0,47,48,1,0,0,0,48,
        50,1,0,0,0,49,51,5,20,0,0,50,49,1,0,0,0,50,51,1,0,0,0,51,52,1,0,
        0,0,52,54,5,21,0,0,53,55,5,22,0,0,54,53,1,0,0,0,54,55,1,0,0,0,55,
        57,1,0,0,0,56,58,5,23,0,0,57,56,1,0,0,0,57,58,1,0,0,0,58,59,1,0,
        0,0,59,60,5,25,0,0,60,3,1,0,0,0,61,62,5,2,0,0,62,64,5,18,0,0,63,
        65,5,19,0,0,64,63,1,0,0,0,64,65,1,0,0,0,65,67,1,0,0,0,66,68,5,20,
        0,0,67,66,1,0,0,0,67,68,1,0,0,0,68,69,1,0,0,0,69,71,5,21,0,0,70,
        72,5,22,0,0,71,70,1,0,0,0,71,72,1,0,0,0,72,74,1,0,0,0,73,75,5,23,
        0,0,74,73,1,0,0,0,74,75,1,0,0,0,75,76,1,0,0,0,76,78,5,25,0,0,77,
        79,3,12,6,0,78,77,1,0,0,0,79,80,1,0,0,0,80,78,1,0,0,0,80,81,1,0,
        0,0,81,5,1,0,0,0,82,83,5,9,0,0,83,84,5,4,0,0,84,86,5,4,0,0,85,87,
        3,14,7,0,86,85,1,0,0,0,87,88,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,
        89,90,1,0,0,0,90,91,5,13,0,0,91,7,1,0,0,0,92,93,5,10,0,0,93,94,5,
        4,0,0,94,95,5,4,0,0,95,97,5,4,0,0,96,98,3,14,7,0,97,96,1,0,0,0,98,
        99,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,101,1,0,0,0,101,102,
        5,13,0,0,102,9,1,0,0,0,103,104,5,11,0,0,104,105,5,4,0,0,105,106,
        5,4,0,0,106,107,5,4,0,0,107,109,5,4,0,0,108,110,3,14,7,0,109,108,
        1,0,0,0,110,111,1,0,0,0,111,109,1,0,0,0,111,112,1,0,0,0,112,113,
        1,0,0,0,113,114,5,13,0,0,114,11,1,0,0,0,115,117,3,14,7,0,116,115,
        1,0,0,0,117,118,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,120,
        1,0,0,0,120,121,5,13,0,0,121,13,1,0,0,0,122,123,7,0,0,0,123,15,1,
        0,0,0,19,17,24,29,34,36,38,47,50,54,57,64,67,71,74,80,88,99,111,
        118
    ]

class SparkyPKParser ( Parser ):

    grammarFileName = "SparkyPKParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Assignment'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'w2'", "'w3'", "'w4'", "<INVALID>", 
                     "'Volume'", "'S/N'" ]

    symbolicNames = [ "<INVALID>", "Assignment", "W1", "Integer", "Float", 
                      "Real", "SHARP_COMMENT", "EXCLM_COMMENT", "SMCLN_COMMENT", 
                      "Assignment_2d_ex", "Assignment_3d_ex", "Assignment_4d_ex", 
                      "SPACE", "RETURN", "ENCLOSE_COMMENT", "SECTION_COMMENT", 
                      "LINE_COMMENT", "W1_LA", "W2_LA", "W3_LA", "W4_LA", 
                      "Height_LA", "Volume_LA", "S_N_LA", "SPACE_LA", "RETURN_LA" ]

    RULE_sparky_pk = 0
    RULE_data_label = 1
    RULE_data_label_wo_assign = 2
    RULE_peak_2d = 3
    RULE_peak_3d = 4
    RULE_peak_4d = 5
    RULE_peak_wo_assign = 6
    RULE_number = 7

    ruleNames =  [ "sparky_pk", "data_label", "data_label_wo_assign", "peak_2d", 
                   "peak_3d", "peak_4d", "peak_wo_assign", "number" ]

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
    SPACE=12
    RETURN=13
    ENCLOSE_COMMENT=14
    SECTION_COMMENT=15
    LINE_COMMENT=16
    W1_LA=17
    W2_LA=18
    W3_LA=19
    W4_LA=20
    Height_LA=21
    Volume_LA=22
    S_N_LA=23
    SPACE_LA=24
    RETURN_LA=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Sparky_pkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SparkyPKParser.EOF, 0)

        def RETURN(self):
            return self.getToken(SparkyPKParser.RETURN, 0)

        def data_label(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyPKParser.Data_labelContext)
            else:
                return self.getTypedRuleContext(SparkyPKParser.Data_labelContext,i)


        def data_label_wo_assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyPKParser.Data_label_wo_assignContext)
            else:
                return self.getTypedRuleContext(SparkyPKParser.Data_label_wo_assignContext,i)


        def peak_2d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyPKParser.Peak_2dContext)
            else:
                return self.getTypedRuleContext(SparkyPKParser.Peak_2dContext,i)


        def peak_3d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyPKParser.Peak_3dContext)
            else:
                return self.getTypedRuleContext(SparkyPKParser.Peak_3dContext,i)


        def peak_4d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyPKParser.Peak_4dContext)
            else:
                return self.getTypedRuleContext(SparkyPKParser.Peak_4dContext,i)


        def getRuleIndex(self):
            return SparkyPKParser.RULE_sparky_pk

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSparky_pk" ):
                listener.enterSparky_pk(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSparky_pk" ):
                listener.exitSparky_pk(self)




    def sparky_pk(self):

        localctx = SparkyPKParser.Sparky_pkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sparky_pk)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 16
                self.match(SparkyPKParser.RETURN)


            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3590) != 0):
                self.state = 36
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 19
                    self.data_label()
                    pass
                elif token in [2]:
                    self.state = 20
                    self.data_label_wo_assign()
                    pass
                elif token in [9]:
                    self.state = 22 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 21
                            self.peak_2d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 24 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                    pass
                elif token in [10]:
                    self.state = 27 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 26
                            self.peak_3d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 29 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                    pass
                elif token in [11]:
                    self.state = 32 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 31
                            self.peak_4d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 34 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41
            self.match(SparkyPKParser.EOF)
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
            return self.getToken(SparkyPKParser.Assignment, 0)

        def W1_LA(self):
            return self.getToken(SparkyPKParser.W1_LA, 0)

        def W2_LA(self):
            return self.getToken(SparkyPKParser.W2_LA, 0)

        def Height_LA(self):
            return self.getToken(SparkyPKParser.Height_LA, 0)

        def RETURN_LA(self):
            return self.getToken(SparkyPKParser.RETURN_LA, 0)

        def W3_LA(self):
            return self.getToken(SparkyPKParser.W3_LA, 0)

        def W4_LA(self):
            return self.getToken(SparkyPKParser.W4_LA, 0)

        def Volume_LA(self):
            return self.getToken(SparkyPKParser.Volume_LA, 0)

        def S_N_LA(self):
            return self.getToken(SparkyPKParser.S_N_LA, 0)

        def getRuleIndex(self):
            return SparkyPKParser.RULE_data_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_label" ):
                listener.enterData_label(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_label" ):
                listener.exitData_label(self)




    def data_label(self):

        localctx = SparkyPKParser.Data_labelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_data_label)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(SparkyPKParser.Assignment)
            self.state = 44
            self.match(SparkyPKParser.W1_LA)
            self.state = 45
            self.match(SparkyPKParser.W2_LA)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 46
                self.match(SparkyPKParser.W3_LA)


            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 49
                self.match(SparkyPKParser.W4_LA)


            self.state = 52
            self.match(SparkyPKParser.Height_LA)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 53
                self.match(SparkyPKParser.Volume_LA)


            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 56
                self.match(SparkyPKParser.S_N_LA)


            self.state = 59
            self.match(SparkyPKParser.RETURN_LA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_label_wo_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def W1(self):
            return self.getToken(SparkyPKParser.W1, 0)

        def W2_LA(self):
            return self.getToken(SparkyPKParser.W2_LA, 0)

        def Height_LA(self):
            return self.getToken(SparkyPKParser.Height_LA, 0)

        def RETURN_LA(self):
            return self.getToken(SparkyPKParser.RETURN_LA, 0)

        def W3_LA(self):
            return self.getToken(SparkyPKParser.W3_LA, 0)

        def W4_LA(self):
            return self.getToken(SparkyPKParser.W4_LA, 0)

        def Volume_LA(self):
            return self.getToken(SparkyPKParser.Volume_LA, 0)

        def S_N_LA(self):
            return self.getToken(SparkyPKParser.S_N_LA, 0)

        def peak_wo_assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyPKParser.Peak_wo_assignContext)
            else:
                return self.getTypedRuleContext(SparkyPKParser.Peak_wo_assignContext,i)


        def getRuleIndex(self):
            return SparkyPKParser.RULE_data_label_wo_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_label_wo_assign" ):
                listener.enterData_label_wo_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_label_wo_assign" ):
                listener.exitData_label_wo_assign(self)




    def data_label_wo_assign(self):

        localctx = SparkyPKParser.Data_label_wo_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_data_label_wo_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(SparkyPKParser.W1)
            self.state = 62
            self.match(SparkyPKParser.W2_LA)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 63
                self.match(SparkyPKParser.W3_LA)


            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 66
                self.match(SparkyPKParser.W4_LA)


            self.state = 69
            self.match(SparkyPKParser.Height_LA)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 70
                self.match(SparkyPKParser.Volume_LA)


            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 73
                self.match(SparkyPKParser.S_N_LA)


            self.state = 76
            self.match(SparkyPKParser.RETURN_LA)
            self.state = 78 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 77
                self.peak_wo_assign()
                self.state = 80 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
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

        def Assignment_2d_ex(self):
            return self.getToken(SparkyPKParser.Assignment_2d_ex, 0)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(SparkyPKParser.Float)
            else:
                return self.getToken(SparkyPKParser.Float, i)

        def RETURN(self):
            return self.getToken(SparkyPKParser.RETURN, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(SparkyPKParser.NumberContext,i)


        def getRuleIndex(self):
            return SparkyPKParser.RULE_peak_2d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_2d" ):
                listener.enterPeak_2d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_2d" ):
                listener.exitPeak_2d(self)




    def peak_2d(self):

        localctx = SparkyPKParser.Peak_2dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_peak_2d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(SparkyPKParser.Assignment_2d_ex)
            self.state = 83
            self.match(SparkyPKParser.Float)
            self.state = 84
            self.match(SparkyPKParser.Float)
            self.state = 86 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 85
                self.number()
                self.state = 88 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                    break

            self.state = 90
            self.match(SparkyPKParser.RETURN)
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
            return self.getToken(SparkyPKParser.Assignment_3d_ex, 0)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(SparkyPKParser.Float)
            else:
                return self.getToken(SparkyPKParser.Float, i)

        def RETURN(self):
            return self.getToken(SparkyPKParser.RETURN, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(SparkyPKParser.NumberContext,i)


        def getRuleIndex(self):
            return SparkyPKParser.RULE_peak_3d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_3d" ):
                listener.enterPeak_3d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_3d" ):
                listener.exitPeak_3d(self)




    def peak_3d(self):

        localctx = SparkyPKParser.Peak_3dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_peak_3d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(SparkyPKParser.Assignment_3d_ex)
            self.state = 93
            self.match(SparkyPKParser.Float)
            self.state = 94
            self.match(SparkyPKParser.Float)
            self.state = 95
            self.match(SparkyPKParser.Float)
            self.state = 97 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 96
                self.number()
                self.state = 99 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                    break

            self.state = 101
            self.match(SparkyPKParser.RETURN)
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
            return self.getToken(SparkyPKParser.Assignment_4d_ex, 0)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(SparkyPKParser.Float)
            else:
                return self.getToken(SparkyPKParser.Float, i)

        def RETURN(self):
            return self.getToken(SparkyPKParser.RETURN, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(SparkyPKParser.NumberContext,i)


        def getRuleIndex(self):
            return SparkyPKParser.RULE_peak_4d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_4d" ):
                listener.enterPeak_4d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_4d" ):
                listener.exitPeak_4d(self)




    def peak_4d(self):

        localctx = SparkyPKParser.Peak_4dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_peak_4d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(SparkyPKParser.Assignment_4d_ex)
            self.state = 104
            self.match(SparkyPKParser.Float)
            self.state = 105
            self.match(SparkyPKParser.Float)
            self.state = 106
            self.match(SparkyPKParser.Float)
            self.state = 107
            self.match(SparkyPKParser.Float)
            self.state = 109 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 108
                self.number()
                self.state = 111 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                    break

            self.state = 113
            self.match(SparkyPKParser.RETURN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Peak_wo_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(SparkyPKParser.RETURN, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(SparkyPKParser.NumberContext,i)


        def getRuleIndex(self):
            return SparkyPKParser.RULE_peak_wo_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_wo_assign" ):
                listener.enterPeak_wo_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_wo_assign" ):
                listener.exitPeak_wo_assign(self)




    def peak_wo_assign(self):

        localctx = SparkyPKParser.Peak_wo_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_peak_wo_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 115
                self.number()
                self.state = 118 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                    break

            self.state = 120
            self.match(SparkyPKParser.RETURN)
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
            return self.getToken(SparkyPKParser.Real, 0)

        def Float(self):
            return self.getToken(SparkyPKParser.Float, 0)

        def Integer(self):
            return self.getToken(SparkyPKParser.Integer, 0)

        def getRuleIndex(self):
            return SparkyPKParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = SparkyPKParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
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





