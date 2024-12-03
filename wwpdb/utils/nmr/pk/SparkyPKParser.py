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
        4,1,26,123,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,5,0,19,8,0,10,0,12,0,22,9,0,1,0,1,0,1,1,1,1,1,
        1,1,1,3,1,30,8,1,1,1,3,1,33,8,1,1,1,1,1,3,1,37,8,1,1,1,3,1,40,8,
        1,1,1,1,1,4,1,44,8,1,11,1,12,1,45,1,1,4,1,49,8,1,11,1,12,1,50,1,
        1,4,1,54,8,1,11,1,12,1,55,3,1,58,8,1,1,2,1,2,1,2,3,2,63,8,2,1,2,
        3,2,66,8,2,1,2,1,2,3,2,70,8,2,1,2,3,2,73,8,2,1,2,1,2,4,2,77,8,2,
        11,2,12,2,78,1,3,1,3,1,3,1,3,4,3,85,8,3,11,3,12,3,86,1,3,1,3,1,4,
        1,4,1,4,1,4,1,4,4,4,96,8,4,11,4,12,4,97,1,4,1,4,1,5,1,5,1,5,1,5,
        1,5,1,5,4,5,108,8,5,11,5,12,5,109,1,5,1,5,1,6,4,6,115,8,6,11,6,12,
        6,116,1,6,1,6,1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,1,1,0,3,5,134,
        0,20,1,0,0,0,2,25,1,0,0,0,4,59,1,0,0,0,6,80,1,0,0,0,8,90,1,0,0,0,
        10,101,1,0,0,0,12,114,1,0,0,0,14,120,1,0,0,0,16,19,3,2,1,0,17,19,
        3,4,2,0,18,16,1,0,0,0,18,17,1,0,0,0,19,22,1,0,0,0,20,18,1,0,0,0,
        20,21,1,0,0,0,21,23,1,0,0,0,22,20,1,0,0,0,23,24,5,0,0,1,24,1,1,0,
        0,0,25,26,5,1,0,0,26,27,5,18,0,0,27,29,5,19,0,0,28,30,5,20,0,0,29,
        28,1,0,0,0,29,30,1,0,0,0,30,32,1,0,0,0,31,33,5,21,0,0,32,31,1,0,
        0,0,32,33,1,0,0,0,33,34,1,0,0,0,34,36,5,22,0,0,35,37,5,23,0,0,36,
        35,1,0,0,0,36,37,1,0,0,0,37,39,1,0,0,0,38,40,5,24,0,0,39,38,1,0,
        0,0,39,40,1,0,0,0,40,41,1,0,0,0,41,57,5,26,0,0,42,44,3,6,3,0,43,
        42,1,0,0,0,44,45,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,58,1,0,0,
        0,47,49,3,8,4,0,48,47,1,0,0,0,49,50,1,0,0,0,50,48,1,0,0,0,50,51,
        1,0,0,0,51,58,1,0,0,0,52,54,3,10,5,0,53,52,1,0,0,0,54,55,1,0,0,0,
        55,53,1,0,0,0,55,56,1,0,0,0,56,58,1,0,0,0,57,43,1,0,0,0,57,48,1,
        0,0,0,57,53,1,0,0,0,58,3,1,0,0,0,59,60,5,2,0,0,60,62,5,19,0,0,61,
        63,5,20,0,0,62,61,1,0,0,0,62,63,1,0,0,0,63,65,1,0,0,0,64,66,5,21,
        0,0,65,64,1,0,0,0,65,66,1,0,0,0,66,67,1,0,0,0,67,69,5,22,0,0,68,
        70,5,23,0,0,69,68,1,0,0,0,69,70,1,0,0,0,70,72,1,0,0,0,71,73,5,24,
        0,0,72,71,1,0,0,0,72,73,1,0,0,0,73,74,1,0,0,0,74,76,5,26,0,0,75,
        77,3,12,6,0,76,75,1,0,0,0,77,78,1,0,0,0,78,76,1,0,0,0,78,79,1,0,
        0,0,79,5,1,0,0,0,80,81,5,9,0,0,81,82,5,4,0,0,82,84,5,4,0,0,83,85,
        3,14,7,0,84,83,1,0,0,0,85,86,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,
        87,88,1,0,0,0,88,89,5,14,0,0,89,7,1,0,0,0,90,91,5,10,0,0,91,92,5,
        4,0,0,92,93,5,4,0,0,93,95,5,4,0,0,94,96,3,14,7,0,95,94,1,0,0,0,96,
        97,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,99,1,0,0,0,99,100,5,14,
        0,0,100,9,1,0,0,0,101,102,5,11,0,0,102,103,5,4,0,0,103,104,5,4,0,
        0,104,105,5,4,0,0,105,107,5,4,0,0,106,108,3,14,7,0,107,106,1,0,0,
        0,108,109,1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,111,1,0,0,
        0,111,112,5,14,0,0,112,11,1,0,0,0,113,115,3,14,7,0,114,113,1,0,0,
        0,115,116,1,0,0,0,116,114,1,0,0,0,116,117,1,0,0,0,117,118,1,0,0,
        0,118,119,5,14,0,0,119,13,1,0,0,0,120,121,7,0,0,0,121,15,1,0,0,0,
        19,18,20,29,32,36,39,45,50,55,57,62,65,69,72,78,86,97,109,116
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
                     "<INVALID>", "<INVALID>", "<INVALID>", "'w2'", "'w3'", 
                     "'w4'", "<INVALID>", "'Volume'", "'S/N'" ]

    symbolicNames = [ "<INVALID>", "Assignment", "W1", "Integer", "Float", 
                      "Real", "SHARP_COMMENT", "EXCLM_COMMENT", "SMCLN_COMMENT", 
                      "Assignment_2d_ex", "Assignment_3d_ex", "Assignment_4d_ex", 
                      "Simple_name", "SPACE", "RETURN", "ENCLOSE_COMMENT", 
                      "SECTION_COMMENT", "LINE_COMMENT", "W1_LA", "W2_LA", 
                      "W3_LA", "W4_LA", "Height_LA", "Volume_LA", "S_N_LA", 
                      "SPACE_LA", "RETURN_LA" ]

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
    Height_LA=22
    Volume_LA=23
    S_N_LA=24
    SPACE_LA=25
    RETURN_LA=26

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
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 18
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 16
                    self.data_label()
                    pass
                elif token in [2]:
                    self.state = 17
                    self.data_label_wo_assign()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 23
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
            self.state = 25
            self.match(SparkyPKParser.Assignment)
            self.state = 26
            self.match(SparkyPKParser.W1_LA)
            self.state = 27
            self.match(SparkyPKParser.W2_LA)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 28
                self.match(SparkyPKParser.W3_LA)


            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 31
                self.match(SparkyPKParser.W4_LA)


            self.state = 34
            self.match(SparkyPKParser.Height_LA)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 35
                self.match(SparkyPKParser.Volume_LA)


            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 38
                self.match(SparkyPKParser.S_N_LA)


            self.state = 41
            self.match(SparkyPKParser.RETURN_LA)
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.state = 43 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 42
                    self.peak_2d()
                    self.state = 45 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==9):
                        break

                pass
            elif token in [10]:
                self.state = 48 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 47
                    self.peak_3d()
                    self.state = 50 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==10):
                        break

                pass
            elif token in [11]:
                self.state = 53 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 52
                    self.peak_4d()
                    self.state = 55 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==11):
                        break

                pass
            else:
                raise NoViableAltException(self)

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
            self.state = 59
            self.match(SparkyPKParser.W1)
            self.state = 60
            self.match(SparkyPKParser.W2_LA)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 61
                self.match(SparkyPKParser.W3_LA)


            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 64
                self.match(SparkyPKParser.W4_LA)


            self.state = 67
            self.match(SparkyPKParser.Height_LA)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 68
                self.match(SparkyPKParser.Volume_LA)


            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 71
                self.match(SparkyPKParser.S_N_LA)


            self.state = 74
            self.match(SparkyPKParser.RETURN_LA)
            self.state = 76 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 75
                self.peak_wo_assign()
                self.state = 78 
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
            self.state = 80
            self.match(SparkyPKParser.Assignment_2d_ex)
            self.state = 81
            self.match(SparkyPKParser.Float)
            self.state = 82
            self.match(SparkyPKParser.Float)
            self.state = 84 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 83
                self.number()
                self.state = 86 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                    break

            self.state = 88
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
            self.state = 90
            self.match(SparkyPKParser.Assignment_3d_ex)
            self.state = 91
            self.match(SparkyPKParser.Float)
            self.state = 92
            self.match(SparkyPKParser.Float)
            self.state = 93
            self.match(SparkyPKParser.Float)
            self.state = 95 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 94
                self.number()
                self.state = 97 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                    break

            self.state = 99
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
            self.state = 101
            self.match(SparkyPKParser.Assignment_4d_ex)
            self.state = 102
            self.match(SparkyPKParser.Float)
            self.state = 103
            self.match(SparkyPKParser.Float)
            self.state = 104
            self.match(SparkyPKParser.Float)
            self.state = 105
            self.match(SparkyPKParser.Float)
            self.state = 107 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 106
                self.number()
                self.state = 109 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                    break

            self.state = 111
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
            self.state = 114 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 113
                self.number()
                self.state = 116 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                    break

            self.state = 118
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
            self.state = 120
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





