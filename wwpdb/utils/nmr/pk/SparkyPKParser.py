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
        4,1,36,207,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,3,0,20,8,0,1,0,1,0,1,0,4,0,25,8,0,11,0,12,
        0,26,1,0,4,0,30,8,0,11,0,12,0,31,1,0,4,0,35,8,0,11,0,12,0,36,5,0,
        39,8,0,10,0,12,0,42,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,50,8,1,1,1,3,
        1,53,8,1,1,1,3,1,56,8,1,1,1,3,1,59,8,1,1,1,3,1,62,8,1,1,1,3,1,65,
        8,1,1,1,3,1,68,8,1,1,1,3,1,71,8,1,1,1,3,1,74,8,1,1,1,3,1,77,8,1,
        1,1,3,1,80,8,1,1,1,3,1,83,8,1,1,1,3,1,86,8,1,1,1,3,1,89,8,1,1,1,
        3,1,92,8,1,1,1,1,1,3,1,96,8,1,1,2,1,2,1,2,3,2,101,8,2,1,2,3,2,104,
        8,2,1,2,3,2,107,8,2,1,2,3,2,110,8,2,1,2,3,2,113,8,2,1,2,3,2,116,
        8,2,1,2,3,2,119,8,2,1,2,3,2,122,8,2,1,2,3,2,125,8,2,1,2,3,2,128,
        8,2,1,2,3,2,131,8,2,1,2,1,2,3,2,135,8,2,1,2,4,2,138,8,2,11,2,12,
        2,139,1,3,1,3,1,3,1,3,4,3,146,8,3,11,3,12,3,147,1,3,5,3,151,8,3,
        10,3,12,3,154,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,4,4,163,8,4,11,4,12,
        4,164,1,4,5,4,168,8,4,10,4,12,4,171,9,4,1,4,1,4,1,5,1,5,1,5,1,5,
        1,5,1,5,4,5,181,8,5,11,5,12,5,182,1,5,5,5,186,8,5,10,5,12,5,189,
        9,5,1,5,1,5,1,6,4,6,194,8,6,11,6,12,6,195,1,6,3,6,199,8,6,1,6,1,
        6,1,7,1,7,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,3,1,1,14,14,
        1,0,3,5,2,0,3,4,12,12,243,0,19,1,0,0,0,2,45,1,0,0,0,4,97,1,0,0,0,
        6,141,1,0,0,0,8,157,1,0,0,0,10,174,1,0,0,0,12,193,1,0,0,0,14,202,
        1,0,0,0,16,204,1,0,0,0,18,20,5,14,0,0,19,18,1,0,0,0,19,20,1,0,0,
        0,20,40,1,0,0,0,21,39,3,2,1,0,22,39,3,4,2,0,23,25,3,6,3,0,24,23,
        1,0,0,0,25,26,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,39,1,0,0,0,
        28,30,3,8,4,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,1,
        0,0,0,32,39,1,0,0,0,33,35,3,10,5,0,34,33,1,0,0,0,35,36,1,0,0,0,36,
        34,1,0,0,0,36,37,1,0,0,0,37,39,1,0,0,0,38,21,1,0,0,0,38,22,1,0,0,
        0,38,24,1,0,0,0,38,29,1,0,0,0,38,34,1,0,0,0,39,42,1,0,0,0,40,38,
        1,0,0,0,40,41,1,0,0,0,41,43,1,0,0,0,42,40,1,0,0,0,43,44,5,0,0,1,
        44,1,1,0,0,0,45,46,5,1,0,0,46,47,5,18,0,0,47,49,5,19,0,0,48,50,5,
        20,0,0,49,48,1,0,0,0,49,50,1,0,0,0,50,52,1,0,0,0,51,53,5,21,0,0,
        52,51,1,0,0,0,52,53,1,0,0,0,53,55,1,0,0,0,54,56,5,22,0,0,55,54,1,
        0,0,0,55,56,1,0,0,0,56,58,1,0,0,0,57,59,5,23,0,0,58,57,1,0,0,0,58,
        59,1,0,0,0,59,61,1,0,0,0,60,62,5,24,0,0,61,60,1,0,0,0,61,62,1,0,
        0,0,62,64,1,0,0,0,63,65,5,25,0,0,64,63,1,0,0,0,64,65,1,0,0,0,65,
        67,1,0,0,0,66,68,5,26,0,0,67,66,1,0,0,0,67,68,1,0,0,0,68,70,1,0,
        0,0,69,71,5,27,0,0,70,69,1,0,0,0,70,71,1,0,0,0,71,73,1,0,0,0,72,
        74,5,28,0,0,73,72,1,0,0,0,73,74,1,0,0,0,74,76,1,0,0,0,75,77,5,29,
        0,0,76,75,1,0,0,0,76,77,1,0,0,0,77,79,1,0,0,0,78,80,5,30,0,0,79,
        78,1,0,0,0,79,80,1,0,0,0,80,82,1,0,0,0,81,83,5,31,0,0,82,81,1,0,
        0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,86,5,32,0,0,85,84,1,0,0,0,85,
        86,1,0,0,0,86,88,1,0,0,0,87,89,5,33,0,0,88,87,1,0,0,0,88,89,1,0,
        0,0,89,91,1,0,0,0,90,92,5,34,0,0,91,90,1,0,0,0,91,92,1,0,0,0,92,
        93,1,0,0,0,93,95,5,36,0,0,94,96,5,14,0,0,95,94,1,0,0,0,95,96,1,0,
        0,0,96,3,1,0,0,0,97,98,5,2,0,0,98,100,5,19,0,0,99,101,5,20,0,0,100,
        99,1,0,0,0,100,101,1,0,0,0,101,103,1,0,0,0,102,104,5,21,0,0,103,
        102,1,0,0,0,103,104,1,0,0,0,104,106,1,0,0,0,105,107,5,22,0,0,106,
        105,1,0,0,0,106,107,1,0,0,0,107,109,1,0,0,0,108,110,5,23,0,0,109,
        108,1,0,0,0,109,110,1,0,0,0,110,112,1,0,0,0,111,113,5,24,0,0,112,
        111,1,0,0,0,112,113,1,0,0,0,113,115,1,0,0,0,114,116,5,25,0,0,115,
        114,1,0,0,0,115,116,1,0,0,0,116,118,1,0,0,0,117,119,5,26,0,0,118,
        117,1,0,0,0,118,119,1,0,0,0,119,121,1,0,0,0,120,122,5,27,0,0,121,
        120,1,0,0,0,121,122,1,0,0,0,122,124,1,0,0,0,123,125,5,28,0,0,124,
        123,1,0,0,0,124,125,1,0,0,0,125,127,1,0,0,0,126,128,5,29,0,0,127,
        126,1,0,0,0,127,128,1,0,0,0,128,130,1,0,0,0,129,131,5,34,0,0,130,
        129,1,0,0,0,130,131,1,0,0,0,131,132,1,0,0,0,132,134,5,36,0,0,133,
        135,5,14,0,0,134,133,1,0,0,0,134,135,1,0,0,0,135,137,1,0,0,0,136,
        138,3,12,6,0,137,136,1,0,0,0,138,139,1,0,0,0,139,137,1,0,0,0,139,
        140,1,0,0,0,140,5,1,0,0,0,141,142,5,9,0,0,142,143,5,4,0,0,143,145,
        5,4,0,0,144,146,3,14,7,0,145,144,1,0,0,0,146,147,1,0,0,0,147,145,
        1,0,0,0,147,148,1,0,0,0,148,152,1,0,0,0,149,151,3,16,8,0,150,149,
        1,0,0,0,151,154,1,0,0,0,152,150,1,0,0,0,152,153,1,0,0,0,153,155,
        1,0,0,0,154,152,1,0,0,0,155,156,7,0,0,0,156,7,1,0,0,0,157,158,5,
        10,0,0,158,159,5,4,0,0,159,160,5,4,0,0,160,162,5,4,0,0,161,163,3,
        14,7,0,162,161,1,0,0,0,163,164,1,0,0,0,164,162,1,0,0,0,164,165,1,
        0,0,0,165,169,1,0,0,0,166,168,3,16,8,0,167,166,1,0,0,0,168,171,1,
        0,0,0,169,167,1,0,0,0,169,170,1,0,0,0,170,172,1,0,0,0,171,169,1,
        0,0,0,172,173,7,0,0,0,173,9,1,0,0,0,174,175,5,11,0,0,175,176,5,4,
        0,0,176,177,5,4,0,0,177,178,5,4,0,0,178,180,5,4,0,0,179,181,3,14,
        7,0,180,179,1,0,0,0,181,182,1,0,0,0,182,180,1,0,0,0,182,183,1,0,
        0,0,183,187,1,0,0,0,184,186,3,16,8,0,185,184,1,0,0,0,186,189,1,0,
        0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,190,1,0,0,0,189,187,1,0,
        0,0,190,191,7,0,0,0,191,11,1,0,0,0,192,194,3,14,7,0,193,192,1,0,
        0,0,194,195,1,0,0,0,195,193,1,0,0,0,195,196,1,0,0,0,196,198,1,0,
        0,0,197,199,5,12,0,0,198,197,1,0,0,0,198,199,1,0,0,0,199,200,1,0,
        0,0,200,201,7,0,0,0,201,13,1,0,0,0,202,203,7,1,0,0,203,15,1,0,0,
        0,204,205,7,2,0,0,205,17,1,0,0,0,43,19,26,31,36,38,40,49,52,55,58,
        61,64,67,70,73,76,79,82,85,88,91,95,100,103,106,109,112,115,118,
        121,124,127,130,134,139,147,152,164,169,182,187,195,198
    ]

class SparkyPKParser ( Parser ):

    grammarFileName = "SparkyPKParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'w2'", "'w3'", 
                     "'w4'", "'Dev w1'", "'Dev w2'", "'Dev w3'", "'Dev w4'", 
                     "<INVALID>", "<INVALID>", "'Volume'", "'S/N'" ]

    symbolicNames = [ "<INVALID>", "Assignment", "W1", "Integer", "Float", 
                      "Real", "SHARP_COMMENT", "EXCLM_COMMENT", "SMCLN_COMMENT", 
                      "Assignment_2d_ex", "Assignment_3d_ex", "Assignment_4d_ex", 
                      "Simple_name", "SPACE", "RETURN", "ENCLOSE_COMMENT", 
                      "SECTION_COMMENT", "LINE_COMMENT", "W1_LA", "W2_LA", 
                      "W3_LA", "W4_LA", "Dev_w1_LA", "Dev_w2_LA", "Dev_w3_LA", 
                      "Dev_w4_LA", "Dummy_H_LA", "Height_LA", "Volume_LA", 
                      "S_N_LA", "Atom1_LA", "Atom2_LA", "Atom3_LA", "Atom4_LA", 
                      "Note_LA", "SPACE_LA", "RETURN_LA" ]

    RULE_sparky_pk = 0
    RULE_data_label = 1
    RULE_data_label_wo_assign = 2
    RULE_peak_2d = 3
    RULE_peak_3d = 4
    RULE_peak_4d = 5
    RULE_peak_wo_assign = 6
    RULE_number = 7
    RULE_note = 8

    ruleNames =  [ "sparky_pk", "data_label", "data_label_wo_assign", "peak_2d", 
                   "peak_3d", "peak_4d", "peak_wo_assign", "number", "note" ]

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
    Dev_w1_LA=22
    Dev_w2_LA=23
    Dev_w3_LA=24
    Dev_w4_LA=25
    Dummy_H_LA=26
    Height_LA=27
    Volume_LA=28
    S_N_LA=29
    Atom1_LA=30
    Atom2_LA=31
    Atom3_LA=32
    Atom4_LA=33
    Note_LA=34
    SPACE_LA=35
    RETURN_LA=36

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
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 18
                self.match(SparkyPKParser.RETURN)


            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3590) != 0):
                self.state = 38
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 21
                    self.data_label()
                    pass
                elif token in [2]:
                    self.state = 22
                    self.data_label_wo_assign()
                    pass
                elif token in [9]:
                    self.state = 24 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 23
                            self.peak_2d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 26 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                    pass
                elif token in [10]:
                    self.state = 29 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 28
                            self.peak_3d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 31 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                    pass
                elif token in [11]:
                    self.state = 34 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 33
                            self.peak_4d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 36 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 43
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

        def RETURN_LA(self):
            return self.getToken(SparkyPKParser.RETURN_LA, 0)

        def W3_LA(self):
            return self.getToken(SparkyPKParser.W3_LA, 0)

        def W4_LA(self):
            return self.getToken(SparkyPKParser.W4_LA, 0)

        def Dev_w1_LA(self):
            return self.getToken(SparkyPKParser.Dev_w1_LA, 0)

        def Dev_w2_LA(self):
            return self.getToken(SparkyPKParser.Dev_w2_LA, 0)

        def Dev_w3_LA(self):
            return self.getToken(SparkyPKParser.Dev_w3_LA, 0)

        def Dev_w4_LA(self):
            return self.getToken(SparkyPKParser.Dev_w4_LA, 0)

        def Dummy_H_LA(self):
            return self.getToken(SparkyPKParser.Dummy_H_LA, 0)

        def Height_LA(self):
            return self.getToken(SparkyPKParser.Height_LA, 0)

        def Volume_LA(self):
            return self.getToken(SparkyPKParser.Volume_LA, 0)

        def S_N_LA(self):
            return self.getToken(SparkyPKParser.S_N_LA, 0)

        def Atom1_LA(self):
            return self.getToken(SparkyPKParser.Atom1_LA, 0)

        def Atom2_LA(self):
            return self.getToken(SparkyPKParser.Atom2_LA, 0)

        def Atom3_LA(self):
            return self.getToken(SparkyPKParser.Atom3_LA, 0)

        def Atom4_LA(self):
            return self.getToken(SparkyPKParser.Atom4_LA, 0)

        def Note_LA(self):
            return self.getToken(SparkyPKParser.Note_LA, 0)

        def RETURN(self):
            return self.getToken(SparkyPKParser.RETURN, 0)

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
            self.state = 45
            self.match(SparkyPKParser.Assignment)
            self.state = 46
            self.match(SparkyPKParser.W1_LA)
            self.state = 47
            self.match(SparkyPKParser.W2_LA)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 48
                self.match(SparkyPKParser.W3_LA)


            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 51
                self.match(SparkyPKParser.W4_LA)


            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 54
                self.match(SparkyPKParser.Dev_w1_LA)


            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 57
                self.match(SparkyPKParser.Dev_w2_LA)


            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 60
                self.match(SparkyPKParser.Dev_w3_LA)


            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 63
                self.match(SparkyPKParser.Dev_w4_LA)


            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 66
                self.match(SparkyPKParser.Dummy_H_LA)


            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 69
                self.match(SparkyPKParser.Height_LA)


            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 72
                self.match(SparkyPKParser.Volume_LA)


            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 75
                self.match(SparkyPKParser.S_N_LA)


            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 78
                self.match(SparkyPKParser.Atom1_LA)


            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 81
                self.match(SparkyPKParser.Atom2_LA)


            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 84
                self.match(SparkyPKParser.Atom3_LA)


            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 87
                self.match(SparkyPKParser.Atom4_LA)


            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 90
                self.match(SparkyPKParser.Note_LA)


            self.state = 93
            self.match(SparkyPKParser.RETURN_LA)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 94
                self.match(SparkyPKParser.RETURN)


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

        def RETURN_LA(self):
            return self.getToken(SparkyPKParser.RETURN_LA, 0)

        def W3_LA(self):
            return self.getToken(SparkyPKParser.W3_LA, 0)

        def W4_LA(self):
            return self.getToken(SparkyPKParser.W4_LA, 0)

        def Dev_w1_LA(self):
            return self.getToken(SparkyPKParser.Dev_w1_LA, 0)

        def Dev_w2_LA(self):
            return self.getToken(SparkyPKParser.Dev_w2_LA, 0)

        def Dev_w3_LA(self):
            return self.getToken(SparkyPKParser.Dev_w3_LA, 0)

        def Dev_w4_LA(self):
            return self.getToken(SparkyPKParser.Dev_w4_LA, 0)

        def Dummy_H_LA(self):
            return self.getToken(SparkyPKParser.Dummy_H_LA, 0)

        def Height_LA(self):
            return self.getToken(SparkyPKParser.Height_LA, 0)

        def Volume_LA(self):
            return self.getToken(SparkyPKParser.Volume_LA, 0)

        def S_N_LA(self):
            return self.getToken(SparkyPKParser.S_N_LA, 0)

        def Note_LA(self):
            return self.getToken(SparkyPKParser.Note_LA, 0)

        def RETURN(self):
            return self.getToken(SparkyPKParser.RETURN, 0)

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
            self.state = 97
            self.match(SparkyPKParser.W1)
            self.state = 98
            self.match(SparkyPKParser.W2_LA)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 99
                self.match(SparkyPKParser.W3_LA)


            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 102
                self.match(SparkyPKParser.W4_LA)


            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 105
                self.match(SparkyPKParser.Dev_w1_LA)


            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 108
                self.match(SparkyPKParser.Dev_w2_LA)


            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 111
                self.match(SparkyPKParser.Dev_w3_LA)


            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 114
                self.match(SparkyPKParser.Dev_w4_LA)


            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 117
                self.match(SparkyPKParser.Dummy_H_LA)


            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 120
                self.match(SparkyPKParser.Height_LA)


            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 123
                self.match(SparkyPKParser.Volume_LA)


            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 126
                self.match(SparkyPKParser.S_N_LA)


            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 129
                self.match(SparkyPKParser.Note_LA)


            self.state = 132
            self.match(SparkyPKParser.RETURN_LA)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 133
                self.match(SparkyPKParser.RETURN)


            self.state = 137 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 136
                self.peak_wo_assign()
                self.state = 139 
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

        def EOF(self):
            return self.getToken(SparkyPKParser.EOF, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(SparkyPKParser.NumberContext,i)


        def note(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyPKParser.NoteContext)
            else:
                return self.getTypedRuleContext(SparkyPKParser.NoteContext,i)


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
            self.state = 141
            self.match(SparkyPKParser.Assignment_2d_ex)
            self.state = 142
            self.match(SparkyPKParser.Float)
            self.state = 143
            self.match(SparkyPKParser.Float)
            self.state = 145 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 144
                    self.number()

                else:
                    raise NoViableAltException(self)
                self.state = 147 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4120) != 0):
                self.state = 149
                self.note()
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 155
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
            return self.getToken(SparkyPKParser.Assignment_3d_ex, 0)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(SparkyPKParser.Float)
            else:
                return self.getToken(SparkyPKParser.Float, i)

        def RETURN(self):
            return self.getToken(SparkyPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(SparkyPKParser.EOF, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(SparkyPKParser.NumberContext,i)


        def note(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyPKParser.NoteContext)
            else:
                return self.getTypedRuleContext(SparkyPKParser.NoteContext,i)


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
            self.state = 157
            self.match(SparkyPKParser.Assignment_3d_ex)
            self.state = 158
            self.match(SparkyPKParser.Float)
            self.state = 159
            self.match(SparkyPKParser.Float)
            self.state = 160
            self.match(SparkyPKParser.Float)
            self.state = 162 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 161
                    self.number()

                else:
                    raise NoViableAltException(self)
                self.state = 164 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4120) != 0):
                self.state = 166
                self.note()
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 172
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
            return self.getToken(SparkyPKParser.Assignment_4d_ex, 0)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(SparkyPKParser.Float)
            else:
                return self.getToken(SparkyPKParser.Float, i)

        def RETURN(self):
            return self.getToken(SparkyPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(SparkyPKParser.EOF, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(SparkyPKParser.NumberContext,i)


        def note(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyPKParser.NoteContext)
            else:
                return self.getTypedRuleContext(SparkyPKParser.NoteContext,i)


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
            self.state = 174
            self.match(SparkyPKParser.Assignment_4d_ex)
            self.state = 175
            self.match(SparkyPKParser.Float)
            self.state = 176
            self.match(SparkyPKParser.Float)
            self.state = 177
            self.match(SparkyPKParser.Float)
            self.state = 178
            self.match(SparkyPKParser.Float)
            self.state = 180 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 179
                    self.number()

                else:
                    raise NoViableAltException(self)
                self.state = 182 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4120) != 0):
                self.state = 184
                self.note()
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 190
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


    class Peak_wo_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(SparkyPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(SparkyPKParser.EOF, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(SparkyPKParser.NumberContext,i)


        def Simple_name(self):
            return self.getToken(SparkyPKParser.Simple_name, 0)

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
            self.state = 193 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 192
                self.number()
                self.state = 195 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                    break

            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 197
                self.match(SparkyPKParser.Simple_name)


            self.state = 200
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
            self.state = 202
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
            return self.getToken(SparkyPKParser.Simple_name, 0)

        def Integer(self):
            return self.getToken(SparkyPKParser.Integer, 0)

        def Float(self):
            return self.getToken(SparkyPKParser.Float, 0)

        def getRuleIndex(self):
            return SparkyPKParser.RULE_note

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNote" ):
                listener.enterNote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNote" ):
                listener.exitNote(self)




    def note(self):

        localctx = SparkyPKParser.NoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_note)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
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





