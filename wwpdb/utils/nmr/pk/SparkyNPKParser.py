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
        4,1,32,139,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,3,0,16,8,0,1,0,1,0,4,0,20,8,0,11,0,12,0,21,1,0,4,0,25,8,0,
        11,0,12,0,26,1,0,4,0,30,8,0,11,0,12,0,31,5,0,34,8,0,10,0,12,0,37,
        9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,45,8,1,1,1,3,1,48,8,1,1,1,3,1,51,
        8,1,1,1,3,1,54,8,1,1,1,3,1,57,8,1,1,1,3,1,60,8,1,1,1,3,1,63,8,1,
        1,1,3,1,66,8,1,1,1,3,1,69,8,1,1,1,3,1,72,8,1,1,1,3,1,75,8,1,1,1,
        1,1,3,1,79,8,1,1,2,1,2,1,2,1,2,5,2,85,8,2,10,2,12,2,88,9,2,1,2,5,
        2,91,8,2,10,2,12,2,94,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,5,3,103,8,
        3,10,3,12,3,106,9,3,1,3,5,3,109,8,3,10,3,12,3,112,9,3,1,3,1,3,1,
        4,1,4,1,4,1,4,1,4,1,4,5,4,122,8,4,10,4,12,4,125,9,4,1,4,5,4,128,
        8,4,10,4,12,4,131,9,4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,0,0,7,0,2,4,6,
        8,10,12,0,3,1,1,14,14,1,0,3,5,2,0,3,4,12,12,157,0,15,1,0,0,0,2,40,
        1,0,0,0,4,80,1,0,0,0,6,97,1,0,0,0,8,115,1,0,0,0,10,134,1,0,0,0,12,
        136,1,0,0,0,14,16,5,14,0,0,15,14,1,0,0,0,15,16,1,0,0,0,16,35,1,0,
        0,0,17,34,3,2,1,0,18,20,3,4,2,0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,
        1,0,0,0,21,22,1,0,0,0,22,34,1,0,0,0,23,25,3,6,3,0,24,23,1,0,0,0,
        25,26,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,34,1,0,0,0,28,30,3,
        8,4,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,
        34,1,0,0,0,33,17,1,0,0,0,33,19,1,0,0,0,33,24,1,0,0,0,33,29,1,0,0,
        0,34,37,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,38,1,0,0,0,37,35,
        1,0,0,0,38,39,5,0,0,1,39,1,1,0,0,0,40,41,5,1,0,0,41,42,5,18,0,0,
        42,44,5,19,0,0,43,45,5,20,0,0,44,43,1,0,0,0,44,45,1,0,0,0,45,47,
        1,0,0,0,46,48,5,21,0,0,47,46,1,0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,
        49,51,5,22,0,0,50,49,1,0,0,0,50,51,1,0,0,0,51,53,1,0,0,0,52,54,5,
        23,0,0,53,52,1,0,0,0,53,54,1,0,0,0,54,56,1,0,0,0,55,57,5,24,0,0,
        56,55,1,0,0,0,56,57,1,0,0,0,57,59,1,0,0,0,58,60,5,25,0,0,59,58,1,
        0,0,0,59,60,1,0,0,0,60,62,1,0,0,0,61,63,5,26,0,0,62,61,1,0,0,0,62,
        63,1,0,0,0,63,65,1,0,0,0,64,66,5,27,0,0,65,64,1,0,0,0,65,66,1,0,
        0,0,66,68,1,0,0,0,67,69,5,28,0,0,68,67,1,0,0,0,68,69,1,0,0,0,69,
        71,1,0,0,0,70,72,5,29,0,0,71,70,1,0,0,0,71,72,1,0,0,0,72,74,1,0,
        0,0,73,75,5,30,0,0,74,73,1,0,0,0,74,75,1,0,0,0,75,76,1,0,0,0,76,
        78,5,32,0,0,77,79,5,14,0,0,78,77,1,0,0,0,78,79,1,0,0,0,79,3,1,0,
        0,0,80,81,5,9,0,0,81,82,5,4,0,0,82,86,5,4,0,0,83,85,3,10,5,0,84,
        83,1,0,0,0,85,88,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,92,1,0,0,
        0,88,86,1,0,0,0,89,91,3,12,6,0,90,89,1,0,0,0,91,94,1,0,0,0,92,90,
        1,0,0,0,92,93,1,0,0,0,93,95,1,0,0,0,94,92,1,0,0,0,95,96,7,0,0,0,
        96,5,1,0,0,0,97,98,5,10,0,0,98,99,5,4,0,0,99,100,5,4,0,0,100,104,
        5,4,0,0,101,103,3,10,5,0,102,101,1,0,0,0,103,106,1,0,0,0,104,102,
        1,0,0,0,104,105,1,0,0,0,105,110,1,0,0,0,106,104,1,0,0,0,107,109,
        3,12,6,0,108,107,1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,110,111,
        1,0,0,0,111,113,1,0,0,0,112,110,1,0,0,0,113,114,7,0,0,0,114,7,1,
        0,0,0,115,116,5,11,0,0,116,117,5,4,0,0,117,118,5,4,0,0,118,119,5,
        4,0,0,119,123,5,4,0,0,120,122,3,10,5,0,121,120,1,0,0,0,122,125,1,
        0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,129,1,0,0,0,125,123,1,
        0,0,0,126,128,3,12,6,0,127,126,1,0,0,0,128,131,1,0,0,0,129,127,1,
        0,0,0,129,130,1,0,0,0,130,132,1,0,0,0,131,129,1,0,0,0,132,133,7,
        0,0,0,133,9,1,0,0,0,134,135,7,1,0,0,135,11,1,0,0,0,136,137,7,2,0,
        0,137,13,1,0,0,0,24,15,21,26,31,33,35,44,47,50,53,56,59,62,65,68,
        71,74,78,86,92,104,110,123,129
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
                     "'w4'", "<INVALID>", "<INVALID>", "'Volume'", "'S/N'" ]

    symbolicNames = [ "<INVALID>", "Assignment", "W1", "Integer", "Float", 
                      "Real", "SHARP_COMMENT", "EXCLM_COMMENT", "SMCLN_COMMENT", 
                      "Assignment_2d_ex", "Assignment_3d_ex", "Assignment_4d_ex", 
                      "Simple_name", "SPACE", "RETURN", "ENCLOSE_COMMENT", 
                      "SECTION_COMMENT", "LINE_COMMENT", "W1_LA", "W2_LA", 
                      "W3_LA", "W4_LA", "Dummy_H_LA", "Height_LA", "Volume_LA", 
                      "S_N_LA", "Atom1_LA", "Atom2_LA", "Atom3_LA", "Atom4_LA", 
                      "Note_LA", "SPACE_LA", "RETURN_LA" ]

    RULE_sparky_npk = 0
    RULE_data_label = 1
    RULE_peak_2d = 2
    RULE_peak_3d = 3
    RULE_peak_4d = 4
    RULE_number = 5
    RULE_note = 6

    ruleNames =  [ "sparky_npk", "data_label", "peak_2d", "peak_3d", "peak_4d", 
                   "number", "note" ]

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
    Atom1_LA=26
    Atom2_LA=27
    Atom3_LA=28
    Atom4_LA=29
    Note_LA=30
    SPACE_LA=31
    RETURN_LA=32

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
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 14
                self.match(SparkyNPKParser.RETURN)


            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3586) != 0):
                self.state = 33
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 17
                    self.data_label()
                    pass
                elif token in [9]:
                    self.state = 19 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 18
                            self.peak_2d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 21 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                    pass
                elif token in [10]:
                    self.state = 24 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 23
                            self.peak_3d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 26 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                    pass
                elif token in [11]:
                    self.state = 29 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 28
                            self.peak_4d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 31 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
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

        def Atom1_LA(self):
            return self.getToken(SparkyNPKParser.Atom1_LA, 0)

        def Atom2_LA(self):
            return self.getToken(SparkyNPKParser.Atom2_LA, 0)

        def Atom3_LA(self):
            return self.getToken(SparkyNPKParser.Atom3_LA, 0)

        def Atom4_LA(self):
            return self.getToken(SparkyNPKParser.Atom4_LA, 0)

        def Note_LA(self):
            return self.getToken(SparkyNPKParser.Note_LA, 0)

        def RETURN(self):
            return self.getToken(SparkyNPKParser.RETURN, 0)

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
            self.state = 40
            self.match(SparkyNPKParser.Assignment)
            self.state = 41
            self.match(SparkyNPKParser.W1_LA)
            self.state = 42
            self.match(SparkyNPKParser.W2_LA)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 43
                self.match(SparkyNPKParser.W3_LA)


            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 46
                self.match(SparkyNPKParser.W4_LA)


            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 49
                self.match(SparkyNPKParser.Dummy_H_LA)


            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 52
                self.match(SparkyNPKParser.Height_LA)


            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 55
                self.match(SparkyNPKParser.Volume_LA)


            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 58
                self.match(SparkyNPKParser.S_N_LA)


            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 61
                self.match(SparkyNPKParser.Atom1_LA)


            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 64
                self.match(SparkyNPKParser.Atom2_LA)


            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 67
                self.match(SparkyNPKParser.Atom3_LA)


            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 70
                self.match(SparkyNPKParser.Atom4_LA)


            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 73
                self.match(SparkyNPKParser.Note_LA)


            self.state = 76
            self.match(SparkyNPKParser.RETURN_LA)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 77
                self.match(SparkyNPKParser.RETURN)


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

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.NumberContext,i)


        def note(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.NoteContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.NoteContext,i)


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
            self.state = 80
            self.match(SparkyNPKParser.Assignment_2d_ex)
            self.state = 81
            self.match(SparkyNPKParser.Float)
            self.state = 82
            self.match(SparkyNPKParser.Float)
            self.state = 86
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 83
                    self.number() 
                self.state = 88
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4120) != 0):
                self.state = 89
                self.note()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 95
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

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.NumberContext,i)


        def note(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.NoteContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.NoteContext,i)


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
            self.state = 97
            self.match(SparkyNPKParser.Assignment_3d_ex)
            self.state = 98
            self.match(SparkyNPKParser.Float)
            self.state = 99
            self.match(SparkyNPKParser.Float)
            self.state = 100
            self.match(SparkyNPKParser.Float)
            self.state = 104
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 101
                    self.number() 
                self.state = 106
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4120) != 0):
                self.state = 107
                self.note()
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 113
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

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.NumberContext,i)


        def note(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.NoteContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.NoteContext,i)


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
            self.state = 115
            self.match(SparkyNPKParser.Assignment_4d_ex)
            self.state = 116
            self.match(SparkyNPKParser.Float)
            self.state = 117
            self.match(SparkyNPKParser.Float)
            self.state = 118
            self.match(SparkyNPKParser.Float)
            self.state = 119
            self.match(SparkyNPKParser.Float)
            self.state = 123
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 120
                    self.number() 
                self.state = 125
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4120) != 0):
                self.state = 126
                self.note()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 132
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


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Real(self):
            return self.getToken(SparkyNPKParser.Real, 0)

        def Float(self):
            return self.getToken(SparkyNPKParser.Float, 0)

        def Integer(self):
            return self.getToken(SparkyNPKParser.Integer, 0)

        def getRuleIndex(self):
            return SparkyNPKParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = SparkyNPKParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
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


    class NoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Simple_name(self):
            return self.getToken(SparkyNPKParser.Simple_name, 0)

        def Integer(self):
            return self.getToken(SparkyNPKParser.Integer, 0)

        def Float(self):
            return self.getToken(SparkyNPKParser.Float, 0)

        def getRuleIndex(self):
            return SparkyNPKParser.RULE_note

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNote" ):
                listener.enterNote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNote" ):
                listener.exitNote(self)




    def note(self):

        localctx = SparkyNPKParser.NoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_note)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4120) != 0)):
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





