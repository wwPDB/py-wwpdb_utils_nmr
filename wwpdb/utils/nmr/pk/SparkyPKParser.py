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
        4,1,41,238,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,3,0,20,8,0,1,0,1,0,1,0,4,0,25,8,0,11,0,12,
        0,26,1,0,4,0,30,8,0,11,0,12,0,31,1,0,4,0,35,8,0,11,0,12,0,36,1,0,
        5,0,40,8,0,10,0,12,0,43,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,51,8,1,1,
        1,3,1,54,8,1,1,1,3,1,57,8,1,1,1,3,1,60,8,1,1,1,3,1,63,8,1,1,1,3,
        1,66,8,1,1,1,3,1,69,8,1,1,1,3,1,72,8,1,1,1,3,1,75,8,1,1,1,3,1,78,
        8,1,1,1,3,1,81,8,1,1,1,3,1,84,8,1,1,1,3,1,87,8,1,1,1,3,1,90,8,1,
        1,1,3,1,93,8,1,1,1,3,1,96,8,1,1,1,3,1,99,8,1,1,1,3,1,102,8,1,1,1,
        3,1,105,8,1,1,1,3,1,108,8,1,1,1,1,1,3,1,112,8,1,1,2,1,2,1,2,3,2,
        117,8,2,1,2,3,2,120,8,2,1,2,3,2,123,8,2,1,2,3,2,126,8,2,1,2,3,2,
        129,8,2,1,2,3,2,132,8,2,1,2,3,2,135,8,2,1,2,3,2,138,8,2,1,2,3,2,
        141,8,2,1,2,3,2,144,8,2,1,2,3,2,147,8,2,1,2,3,2,150,8,2,1,2,3,2,
        153,8,2,1,2,3,2,156,8,2,1,2,3,2,159,8,2,1,2,3,2,162,8,2,1,2,1,2,
        3,2,166,8,2,1,2,4,2,169,8,2,11,2,12,2,170,1,3,1,3,1,3,1,3,4,3,177,
        8,3,11,3,12,3,178,1,3,5,3,182,8,3,10,3,12,3,185,9,3,1,3,1,3,1,4,
        1,4,1,4,1,4,1,4,4,4,194,8,4,11,4,12,4,195,1,4,5,4,199,8,4,10,4,12,
        4,202,9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,4,5,212,8,5,11,5,12,5,
        213,1,5,5,5,217,8,5,10,5,12,5,220,9,5,1,5,1,5,1,6,4,6,225,8,6,11,
        6,12,6,226,1,6,3,6,230,8,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,0,0,9,0,2,
        4,6,8,10,12,14,16,0,3,1,1,14,14,1,0,3,5,2,0,3,4,12,12,285,0,19,1,
        0,0,0,2,46,1,0,0,0,4,113,1,0,0,0,6,172,1,0,0,0,8,188,1,0,0,0,10,
        205,1,0,0,0,12,224,1,0,0,0,14,233,1,0,0,0,16,235,1,0,0,0,18,20,5,
        14,0,0,19,18,1,0,0,0,19,20,1,0,0,0,20,41,1,0,0,0,21,40,3,2,1,0,22,
        40,3,4,2,0,23,25,3,6,3,0,24,23,1,0,0,0,25,26,1,0,0,0,26,24,1,0,0,
        0,26,27,1,0,0,0,27,40,1,0,0,0,28,30,3,8,4,0,29,28,1,0,0,0,30,31,
        1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,40,1,0,0,0,33,35,3,10,5,0,
        34,33,1,0,0,0,35,36,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,40,1,
        0,0,0,38,40,5,14,0,0,39,21,1,0,0,0,39,22,1,0,0,0,39,24,1,0,0,0,39,
        29,1,0,0,0,39,34,1,0,0,0,39,38,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,
        0,41,42,1,0,0,0,42,44,1,0,0,0,43,41,1,0,0,0,44,45,5,0,0,1,45,1,1,
        0,0,0,46,47,5,1,0,0,47,48,5,22,0,0,48,50,5,23,0,0,49,51,5,24,0,0,
        50,49,1,0,0,0,50,51,1,0,0,0,51,53,1,0,0,0,52,54,5,25,0,0,53,52,1,
        0,0,0,53,54,1,0,0,0,54,56,1,0,0,0,55,57,5,18,0,0,56,55,1,0,0,0,56,
        57,1,0,0,0,57,59,1,0,0,0,58,60,5,19,0,0,59,58,1,0,0,0,59,60,1,0,
        0,0,60,62,1,0,0,0,61,63,5,20,0,0,62,61,1,0,0,0,62,63,1,0,0,0,63,
        65,1,0,0,0,64,66,5,21,0,0,65,64,1,0,0,0,65,66,1,0,0,0,66,68,1,0,
        0,0,67,69,5,26,0,0,68,67,1,0,0,0,68,69,1,0,0,0,69,71,1,0,0,0,70,
        72,5,27,0,0,71,70,1,0,0,0,71,72,1,0,0,0,72,74,1,0,0,0,73,75,5,28,
        0,0,74,73,1,0,0,0,74,75,1,0,0,0,75,77,1,0,0,0,76,78,5,29,0,0,77,
        76,1,0,0,0,77,78,1,0,0,0,78,80,1,0,0,0,79,81,5,30,0,0,80,79,1,0,
        0,0,80,81,1,0,0,0,81,83,1,0,0,0,82,84,5,31,0,0,83,82,1,0,0,0,83,
        84,1,0,0,0,84,86,1,0,0,0,85,87,5,32,0,0,86,85,1,0,0,0,86,87,1,0,
        0,0,87,89,1,0,0,0,88,90,5,33,0,0,89,88,1,0,0,0,89,90,1,0,0,0,90,
        92,1,0,0,0,91,93,5,34,0,0,92,91,1,0,0,0,92,93,1,0,0,0,93,95,1,0,
        0,0,94,96,5,35,0,0,95,94,1,0,0,0,95,96,1,0,0,0,96,98,1,0,0,0,97,
        99,5,36,0,0,98,97,1,0,0,0,98,99,1,0,0,0,99,101,1,0,0,0,100,102,5,
        37,0,0,101,100,1,0,0,0,101,102,1,0,0,0,102,104,1,0,0,0,103,105,5,
        38,0,0,104,103,1,0,0,0,104,105,1,0,0,0,105,107,1,0,0,0,106,108,5,
        39,0,0,107,106,1,0,0,0,107,108,1,0,0,0,108,109,1,0,0,0,109,111,5,
        41,0,0,110,112,5,14,0,0,111,110,1,0,0,0,111,112,1,0,0,0,112,3,1,
        0,0,0,113,114,5,2,0,0,114,116,5,23,0,0,115,117,5,24,0,0,116,115,
        1,0,0,0,116,117,1,0,0,0,117,119,1,0,0,0,118,120,5,25,0,0,119,118,
        1,0,0,0,119,120,1,0,0,0,120,122,1,0,0,0,121,123,5,18,0,0,122,121,
        1,0,0,0,122,123,1,0,0,0,123,125,1,0,0,0,124,126,5,19,0,0,125,124,
        1,0,0,0,125,126,1,0,0,0,126,128,1,0,0,0,127,129,5,20,0,0,128,127,
        1,0,0,0,128,129,1,0,0,0,129,131,1,0,0,0,130,132,5,21,0,0,131,130,
        1,0,0,0,131,132,1,0,0,0,132,134,1,0,0,0,133,135,5,26,0,0,134,133,
        1,0,0,0,134,135,1,0,0,0,135,137,1,0,0,0,136,138,5,27,0,0,137,136,
        1,0,0,0,137,138,1,0,0,0,138,140,1,0,0,0,139,141,5,28,0,0,140,139,
        1,0,0,0,140,141,1,0,0,0,141,143,1,0,0,0,142,144,5,29,0,0,143,142,
        1,0,0,0,143,144,1,0,0,0,144,146,1,0,0,0,145,147,5,30,0,0,146,145,
        1,0,0,0,146,147,1,0,0,0,147,149,1,0,0,0,148,150,5,31,0,0,149,148,
        1,0,0,0,149,150,1,0,0,0,150,152,1,0,0,0,151,153,5,32,0,0,152,151,
        1,0,0,0,152,153,1,0,0,0,153,155,1,0,0,0,154,156,5,33,0,0,155,154,
        1,0,0,0,155,156,1,0,0,0,156,158,1,0,0,0,157,159,5,38,0,0,158,157,
        1,0,0,0,158,159,1,0,0,0,159,161,1,0,0,0,160,162,5,39,0,0,161,160,
        1,0,0,0,161,162,1,0,0,0,162,163,1,0,0,0,163,165,5,41,0,0,164,166,
        5,14,0,0,165,164,1,0,0,0,165,166,1,0,0,0,166,168,1,0,0,0,167,169,
        3,12,6,0,168,167,1,0,0,0,169,170,1,0,0,0,170,168,1,0,0,0,170,171,
        1,0,0,0,171,5,1,0,0,0,172,173,5,9,0,0,173,174,5,4,0,0,174,176,5,
        4,0,0,175,177,3,14,7,0,176,175,1,0,0,0,177,178,1,0,0,0,178,176,1,
        0,0,0,178,179,1,0,0,0,179,183,1,0,0,0,180,182,3,16,8,0,181,180,1,
        0,0,0,182,185,1,0,0,0,183,181,1,0,0,0,183,184,1,0,0,0,184,186,1,
        0,0,0,185,183,1,0,0,0,186,187,7,0,0,0,187,7,1,0,0,0,188,189,5,10,
        0,0,189,190,5,4,0,0,190,191,5,4,0,0,191,193,5,4,0,0,192,194,3,14,
        7,0,193,192,1,0,0,0,194,195,1,0,0,0,195,193,1,0,0,0,195,196,1,0,
        0,0,196,200,1,0,0,0,197,199,3,16,8,0,198,197,1,0,0,0,199,202,1,0,
        0,0,200,198,1,0,0,0,200,201,1,0,0,0,201,203,1,0,0,0,202,200,1,0,
        0,0,203,204,7,0,0,0,204,9,1,0,0,0,205,206,5,11,0,0,206,207,5,4,0,
        0,207,208,5,4,0,0,208,209,5,4,0,0,209,211,5,4,0,0,210,212,3,14,7,
        0,211,210,1,0,0,0,212,213,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,
        0,214,218,1,0,0,0,215,217,3,16,8,0,216,215,1,0,0,0,217,220,1,0,0,
        0,218,216,1,0,0,0,218,219,1,0,0,0,219,221,1,0,0,0,220,218,1,0,0,
        0,221,222,7,0,0,0,222,11,1,0,0,0,223,225,3,14,7,0,224,223,1,0,0,
        0,225,226,1,0,0,0,226,224,1,0,0,0,226,227,1,0,0,0,227,229,1,0,0,
        0,228,230,5,12,0,0,229,228,1,0,0,0,229,230,1,0,0,0,230,231,1,0,0,
        0,231,232,7,0,0,0,232,13,1,0,0,0,233,234,7,1,0,0,234,15,1,0,0,0,
        235,236,7,2,0,0,236,17,1,0,0,0,53,19,26,31,36,39,41,50,53,56,59,
        62,65,68,71,74,77,80,83,86,89,92,95,98,101,104,107,111,116,119,122,
        125,128,131,134,137,140,143,146,149,152,155,158,161,165,170,178,
        183,195,200,213,218,226,229
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
                     "<INVALID>", "<INVALID>", "'w1 (Hz)'", "'w2 (Hz)'", 
                     "'w3 (Hz)'", "'w4 (Hz)'", "<INVALID>", "'w2'", "'w3'", 
                     "'w4'", "'Dev w1'", "'Dev w2'", "'Dev w3'", "'Dev w4'", 
                     "<INVALID>", "<INVALID>", "'Volume'", "'S/N'" ]

    symbolicNames = [ "<INVALID>", "Assignment", "W1", "Integer", "Float", 
                      "Real", "SHARP_COMMENT", "EXCLM_COMMENT", "SMCLN_COMMENT", 
                      "Assignment_2d_ex", "Assignment_3d_ex", "Assignment_4d_ex", 
                      "Simple_name", "SPACE", "RETURN", "ENCLOSE_COMMENT", 
                      "SECTION_COMMENT", "LINE_COMMENT", "W1_Hz_LA", "W2_Hz_LA", 
                      "W3_Hz_LA", "W4_Hz_LA", "W1_LA", "W2_LA", "W3_LA", 
                      "W4_LA", "Dev_w1_LA", "Dev_w2_LA", "Dev_w3_LA", "Dev_w4_LA", 
                      "Dummy_H_LA", "Height_LA", "Volume_LA", "S_N_LA", 
                      "Atom1_LA", "Atom2_LA", "Atom3_LA", "Atom4_LA", "Distance_LA", 
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
    W1_Hz_LA=18
    W2_Hz_LA=19
    W3_Hz_LA=20
    W4_Hz_LA=21
    W1_LA=22
    W2_LA=23
    W3_LA=24
    W4_LA=25
    Dev_w1_LA=26
    Dev_w2_LA=27
    Dev_w3_LA=28
    Dev_w4_LA=29
    Dummy_H_LA=30
    Height_LA=31
    Volume_LA=32
    S_N_LA=33
    Atom1_LA=34
    Atom2_LA=35
    Atom3_LA=36
    Atom4_LA=37
    Distance_LA=38
    Note_LA=39
    SPACE_LA=40
    RETURN_LA=41

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

        def RETURN(self, i:int=None):
            if i is None:
                return self.getTokens(SparkyPKParser.RETURN)
            else:
                return self.getToken(SparkyPKParser.RETURN, i)

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
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 18
                self.match(SparkyPKParser.RETURN)


            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 19974) != 0):
                self.state = 39
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
                elif token in [14]:
                    self.state = 38
                    self.match(SparkyPKParser.RETURN)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
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

        def W1_Hz_LA(self):
            return self.getToken(SparkyPKParser.W1_Hz_LA, 0)

        def W2_Hz_LA(self):
            return self.getToken(SparkyPKParser.W2_Hz_LA, 0)

        def W3_Hz_LA(self):
            return self.getToken(SparkyPKParser.W3_Hz_LA, 0)

        def W4_Hz_LA(self):
            return self.getToken(SparkyPKParser.W4_Hz_LA, 0)

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

        def Distance_LA(self):
            return self.getToken(SparkyPKParser.Distance_LA, 0)

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
            self.state = 46
            self.match(SparkyPKParser.Assignment)
            self.state = 47
            self.match(SparkyPKParser.W1_LA)
            self.state = 48
            self.match(SparkyPKParser.W2_LA)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 49
                self.match(SparkyPKParser.W3_LA)


            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 52
                self.match(SparkyPKParser.W4_LA)


            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 55
                self.match(SparkyPKParser.W1_Hz_LA)


            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 58
                self.match(SparkyPKParser.W2_Hz_LA)


            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 61
                self.match(SparkyPKParser.W3_Hz_LA)


            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 64
                self.match(SparkyPKParser.W4_Hz_LA)


            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 67
                self.match(SparkyPKParser.Dev_w1_LA)


            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 70
                self.match(SparkyPKParser.Dev_w2_LA)


            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 73
                self.match(SparkyPKParser.Dev_w3_LA)


            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 76
                self.match(SparkyPKParser.Dev_w4_LA)


            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 79
                self.match(SparkyPKParser.Dummy_H_LA)


            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 82
                self.match(SparkyPKParser.Height_LA)


            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 85
                self.match(SparkyPKParser.Volume_LA)


            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 88
                self.match(SparkyPKParser.S_N_LA)


            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 91
                self.match(SparkyPKParser.Atom1_LA)


            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 94
                self.match(SparkyPKParser.Atom2_LA)


            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 97
                self.match(SparkyPKParser.Atom3_LA)


            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 100
                self.match(SparkyPKParser.Atom4_LA)


            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 103
                self.match(SparkyPKParser.Distance_LA)


            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 106
                self.match(SparkyPKParser.Note_LA)


            self.state = 109
            self.match(SparkyPKParser.RETURN_LA)
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 110
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

        def W1_Hz_LA(self):
            return self.getToken(SparkyPKParser.W1_Hz_LA, 0)

        def W2_Hz_LA(self):
            return self.getToken(SparkyPKParser.W2_Hz_LA, 0)

        def W3_Hz_LA(self):
            return self.getToken(SparkyPKParser.W3_Hz_LA, 0)

        def W4_Hz_LA(self):
            return self.getToken(SparkyPKParser.W4_Hz_LA, 0)

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

        def Distance_LA(self):
            return self.getToken(SparkyPKParser.Distance_LA, 0)

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
            self.state = 113
            self.match(SparkyPKParser.W1)
            self.state = 114
            self.match(SparkyPKParser.W2_LA)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 115
                self.match(SparkyPKParser.W3_LA)


            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 118
                self.match(SparkyPKParser.W4_LA)


            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 121
                self.match(SparkyPKParser.W1_Hz_LA)


            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 124
                self.match(SparkyPKParser.W2_Hz_LA)


            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 127
                self.match(SparkyPKParser.W3_Hz_LA)


            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 130
                self.match(SparkyPKParser.W4_Hz_LA)


            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 133
                self.match(SparkyPKParser.Dev_w1_LA)


            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 136
                self.match(SparkyPKParser.Dev_w2_LA)


            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 139
                self.match(SparkyPKParser.Dev_w3_LA)


            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 142
                self.match(SparkyPKParser.Dev_w4_LA)


            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 145
                self.match(SparkyPKParser.Dummy_H_LA)


            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 148
                self.match(SparkyPKParser.Height_LA)


            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 151
                self.match(SparkyPKParser.Volume_LA)


            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 154
                self.match(SparkyPKParser.S_N_LA)


            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 157
                self.match(SparkyPKParser.Distance_LA)


            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 160
                self.match(SparkyPKParser.Note_LA)


            self.state = 163
            self.match(SparkyPKParser.RETURN_LA)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 164
                self.match(SparkyPKParser.RETURN)


            self.state = 168 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 167
                self.peak_wo_assign()
                self.state = 170 
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
            self.state = 172
            self.match(SparkyPKParser.Assignment_2d_ex)
            self.state = 173
            self.match(SparkyPKParser.Float)
            self.state = 174
            self.match(SparkyPKParser.Float)
            self.state = 176 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 175
                    self.number()

                else:
                    raise NoViableAltException(self)
                self.state = 178 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4120) != 0):
                self.state = 180
                self.note()
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 186
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
            self.state = 188
            self.match(SparkyPKParser.Assignment_3d_ex)
            self.state = 189
            self.match(SparkyPKParser.Float)
            self.state = 190
            self.match(SparkyPKParser.Float)
            self.state = 191
            self.match(SparkyPKParser.Float)
            self.state = 193 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 192
                    self.number()

                else:
                    raise NoViableAltException(self)
                self.state = 195 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4120) != 0):
                self.state = 197
                self.note()
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 203
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
            self.state = 205
            self.match(SparkyPKParser.Assignment_4d_ex)
            self.state = 206
            self.match(SparkyPKParser.Float)
            self.state = 207
            self.match(SparkyPKParser.Float)
            self.state = 208
            self.match(SparkyPKParser.Float)
            self.state = 209
            self.match(SparkyPKParser.Float)
            self.state = 211 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 210
                    self.number()

                else:
                    raise NoViableAltException(self)
                self.state = 213 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,49,self._ctx)

            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4120) != 0):
                self.state = 215
                self.note()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 221
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
            self.state = 224 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 223
                self.number()
                self.state = 226 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                    break

            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 228
                self.match(SparkyPKParser.Simple_name)


            self.state = 231
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
            self.state = 233
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
            self.state = 235
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





