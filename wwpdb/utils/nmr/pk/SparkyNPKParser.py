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
        4,1,49,215,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,3,0,22,8,0,1,0,1,0,4,0,26,8,0,11,0,
        12,0,27,1,0,4,0,31,8,0,11,0,12,0,32,1,0,4,0,36,8,0,11,0,12,0,37,
        1,0,4,0,41,8,0,11,0,12,0,42,1,0,4,0,46,8,0,11,0,12,0,47,1,0,4,0,
        51,8,0,11,0,12,0,52,1,0,5,0,56,8,0,10,0,12,0,59,9,0,1,0,1,0,1,1,
        1,1,1,1,1,1,3,1,67,8,1,1,1,3,1,70,8,1,1,1,3,1,73,8,1,1,1,3,1,76,
        8,1,1,1,3,1,79,8,1,1,1,3,1,82,8,1,1,1,3,1,85,8,1,1,1,3,1,88,8,1,
        1,1,3,1,91,8,1,1,1,3,1,94,8,1,1,1,3,1,97,8,1,1,1,3,1,100,8,1,1,1,
        3,1,103,8,1,1,1,3,1,106,8,1,1,1,3,1,109,8,1,1,1,3,1,112,8,1,1,1,
        3,1,115,8,1,1,1,3,1,118,8,1,1,1,3,1,121,8,1,1,1,3,1,124,8,1,1,1,
        3,1,127,8,1,1,1,3,1,130,8,1,1,1,3,1,133,8,1,1,1,1,1,3,1,137,8,1,
        1,2,1,2,1,2,1,2,5,2,143,8,2,10,2,12,2,146,9,2,1,2,5,2,149,8,2,10,
        2,12,2,152,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,5,3,161,8,3,10,3,12,3,
        164,9,3,1,3,5,3,167,8,3,10,3,12,3,170,9,3,1,3,1,3,1,4,1,4,1,4,1,
        4,1,4,1,4,5,4,180,8,4,10,4,12,4,183,9,4,1,4,5,4,186,8,4,10,4,12,
        4,189,9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,
        12,14,16,18,0,7,2,0,1,1,10,12,1,0,39,40,1,1,18,18,1,0,10,12,1,0,
        11,12,1,0,3,6,2,0,3,4,13,16,249,0,21,1,0,0,0,2,62,1,0,0,0,4,138,
        1,0,0,0,6,155,1,0,0,0,8,173,1,0,0,0,10,192,1,0,0,0,12,197,1,0,0,
        0,14,203,1,0,0,0,16,210,1,0,0,0,18,212,1,0,0,0,20,22,5,18,0,0,21,
        20,1,0,0,0,21,22,1,0,0,0,22,57,1,0,0,0,23,56,3,2,1,0,24,26,3,10,
        5,0,25,24,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,56,
        1,0,0,0,29,31,3,12,6,0,30,29,1,0,0,0,31,32,1,0,0,0,32,30,1,0,0,0,
        32,33,1,0,0,0,33,56,1,0,0,0,34,36,3,14,7,0,35,34,1,0,0,0,36,37,1,
        0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,56,1,0,0,0,39,41,3,4,2,0,40,
        39,1,0,0,0,41,42,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,56,1,0,0,
        0,44,46,3,6,3,0,45,44,1,0,0,0,46,47,1,0,0,0,47,45,1,0,0,0,47,48,
        1,0,0,0,48,56,1,0,0,0,49,51,3,8,4,0,50,49,1,0,0,0,51,52,1,0,0,0,
        52,50,1,0,0,0,52,53,1,0,0,0,53,56,1,0,0,0,54,56,5,18,0,0,55,23,1,
        0,0,0,55,25,1,0,0,0,55,30,1,0,0,0,55,35,1,0,0,0,55,40,1,0,0,0,55,
        45,1,0,0,0,55,50,1,0,0,0,55,54,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,
        0,57,58,1,0,0,0,58,60,1,0,0,0,59,57,1,0,0,0,60,61,5,0,0,1,61,1,1,
        0,0,0,62,63,7,0,0,0,63,64,5,30,0,0,64,66,5,31,0,0,65,67,5,32,0,0,
        66,65,1,0,0,0,66,67,1,0,0,0,67,69,1,0,0,0,68,70,5,33,0,0,69,68,1,
        0,0,0,69,70,1,0,0,0,70,72,1,0,0,0,71,73,5,22,0,0,72,71,1,0,0,0,72,
        73,1,0,0,0,73,75,1,0,0,0,74,76,5,23,0,0,75,74,1,0,0,0,75,76,1,0,
        0,0,76,78,1,0,0,0,77,79,5,24,0,0,78,77,1,0,0,0,78,79,1,0,0,0,79,
        81,1,0,0,0,80,82,5,25,0,0,81,80,1,0,0,0,81,82,1,0,0,0,82,84,1,0,
        0,0,83,85,5,34,0,0,84,83,1,0,0,0,84,85,1,0,0,0,85,87,1,0,0,0,86,
        88,5,35,0,0,87,86,1,0,0,0,87,88,1,0,0,0,88,90,1,0,0,0,89,91,5,36,
        0,0,90,89,1,0,0,0,90,91,1,0,0,0,91,93,1,0,0,0,92,94,5,37,0,0,93,
        92,1,0,0,0,93,94,1,0,0,0,94,96,1,0,0,0,95,97,7,1,0,0,96,95,1,0,0,
        0,96,97,1,0,0,0,97,99,1,0,0,0,98,100,7,1,0,0,99,98,1,0,0,0,99,100,
        1,0,0,0,100,102,1,0,0,0,101,103,5,41,0,0,102,101,1,0,0,0,102,103,
        1,0,0,0,103,105,1,0,0,0,104,106,5,26,0,0,105,104,1,0,0,0,105,106,
        1,0,0,0,106,108,1,0,0,0,107,109,5,27,0,0,108,107,1,0,0,0,108,109,
        1,0,0,0,109,111,1,0,0,0,110,112,5,28,0,0,111,110,1,0,0,0,111,112,
        1,0,0,0,112,114,1,0,0,0,113,115,5,29,0,0,114,113,1,0,0,0,114,115,
        1,0,0,0,115,117,1,0,0,0,116,118,5,42,0,0,117,116,1,0,0,0,117,118,
        1,0,0,0,118,120,1,0,0,0,119,121,5,43,0,0,120,119,1,0,0,0,120,121,
        1,0,0,0,121,123,1,0,0,0,122,124,5,44,0,0,123,122,1,0,0,0,123,124,
        1,0,0,0,124,126,1,0,0,0,125,127,5,45,0,0,126,125,1,0,0,0,126,127,
        1,0,0,0,127,129,1,0,0,0,128,130,5,46,0,0,129,128,1,0,0,0,129,130,
        1,0,0,0,130,132,1,0,0,0,131,133,5,47,0,0,132,131,1,0,0,0,132,133,
        1,0,0,0,133,134,1,0,0,0,134,136,5,49,0,0,135,137,5,18,0,0,136,135,
        1,0,0,0,136,137,1,0,0,0,137,3,1,0,0,0,138,139,5,10,0,0,139,140,5,
        4,0,0,140,144,5,4,0,0,141,143,3,16,8,0,142,141,1,0,0,0,143,146,1,
        0,0,0,144,142,1,0,0,0,144,145,1,0,0,0,145,150,1,0,0,0,146,144,1,
        0,0,0,147,149,3,18,9,0,148,147,1,0,0,0,149,152,1,0,0,0,150,148,1,
        0,0,0,150,151,1,0,0,0,151,153,1,0,0,0,152,150,1,0,0,0,153,154,7,
        2,0,0,154,5,1,0,0,0,155,156,5,11,0,0,156,157,5,4,0,0,157,158,5,4,
        0,0,158,162,5,4,0,0,159,161,3,16,8,0,160,159,1,0,0,0,161,164,1,0,
        0,0,162,160,1,0,0,0,162,163,1,0,0,0,163,168,1,0,0,0,164,162,1,0,
        0,0,165,167,3,18,9,0,166,165,1,0,0,0,167,170,1,0,0,0,168,166,1,0,
        0,0,168,169,1,0,0,0,169,171,1,0,0,0,170,168,1,0,0,0,171,172,7,2,
        0,0,172,7,1,0,0,0,173,174,5,12,0,0,174,175,5,4,0,0,175,176,5,4,0,
        0,176,177,5,4,0,0,177,181,5,4,0,0,178,180,3,16,8,0,179,178,1,0,0,
        0,180,183,1,0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,187,1,0,0,
        0,183,181,1,0,0,0,184,186,3,18,9,0,185,184,1,0,0,0,186,189,1,0,0,
        0,187,185,1,0,0,0,187,188,1,0,0,0,188,190,1,0,0,0,189,187,1,0,0,
        0,190,191,7,2,0,0,191,9,1,0,0,0,192,193,7,3,0,0,193,194,5,4,0,0,
        194,195,5,4,0,0,195,196,7,2,0,0,196,11,1,0,0,0,197,198,7,4,0,0,198,
        199,5,4,0,0,199,200,5,4,0,0,200,201,5,4,0,0,201,202,7,2,0,0,202,
        13,1,0,0,0,203,204,5,12,0,0,204,205,5,4,0,0,205,206,5,4,0,0,206,
        207,5,4,0,0,207,208,5,4,0,0,208,209,7,2,0,0,209,15,1,0,0,0,210,211,
        7,5,0,0,211,17,1,0,0,0,212,213,7,6,0,0,213,19,1,0,0,0,39,21,27,32,
        37,42,47,52,55,57,66,69,72,75,78,81,84,87,90,93,96,99,102,105,108,
        111,114,117,120,123,126,129,132,136,144,150,162,168,181,187
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
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'w2'", "'w3'", 
                     "'w4'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'Volume'" ]

    symbolicNames = [ "<INVALID>", "Assignment", "W1", "Integer", "Float", 
                      "Real", "Real_vol", "SHARP_COMMENT", "EXCLM_COMMENT", 
                      "SMCLN_COMMENT", "Assignment_2d_ex", "Assignment_3d_ex", 
                      "Assignment_4d_ex", "Note_2d_ex", "Note_3d_ex", "Note_4d_ex", 
                      "Simple_name", "SPACE", "RETURN", "ENCLOSE_COMMENT", 
                      "SECTION_COMMENT", "LINE_COMMENT", "W1_Hz_LA", "W2_Hz_LA", 
                      "W3_Hz_LA", "W4_Hz_LA", "Lw1_Hz_LA", "Lw2_Hz_LA", 
                      "Lw3_Hz_LA", "Lw4_Hz_LA", "W1_LA", "W2_LA", "W3_LA", 
                      "W4_LA", "Dev_w1_LA", "Dev_w2_LA", "Dev_w3_LA", "Dev_w4_LA", 
                      "Dummy_H_LA", "Height_LA", "Volume_LA", "S_N_LA", 
                      "Atom1_LA", "Atom2_LA", "Atom3_LA", "Atom4_LA", "Distance_LA", 
                      "Note_LA", "SPACE_LA", "RETURN_LA" ]

    RULE_sparky_npk = 0
    RULE_data_label = 1
    RULE_peak_2d = 2
    RULE_peak_3d = 3
    RULE_peak_4d = 4
    RULE_peak_2d_po = 5
    RULE_peak_3d_po = 6
    RULE_peak_4d_po = 7
    RULE_number = 8
    RULE_note = 9

    ruleNames =  [ "sparky_npk", "data_label", "peak_2d", "peak_3d", "peak_4d", 
                   "peak_2d_po", "peak_3d_po", "peak_4d_po", "number", "note" ]

    EOF = Token.EOF
    Assignment=1
    W1=2
    Integer=3
    Float=4
    Real=5
    Real_vol=6
    SHARP_COMMENT=7
    EXCLM_COMMENT=8
    SMCLN_COMMENT=9
    Assignment_2d_ex=10
    Assignment_3d_ex=11
    Assignment_4d_ex=12
    Note_2d_ex=13
    Note_3d_ex=14
    Note_4d_ex=15
    Simple_name=16
    SPACE=17
    RETURN=18
    ENCLOSE_COMMENT=19
    SECTION_COMMENT=20
    LINE_COMMENT=21
    W1_Hz_LA=22
    W2_Hz_LA=23
    W3_Hz_LA=24
    W4_Hz_LA=25
    Lw1_Hz_LA=26
    Lw2_Hz_LA=27
    Lw3_Hz_LA=28
    Lw4_Hz_LA=29
    W1_LA=30
    W2_LA=31
    W3_LA=32
    W4_LA=33
    Dev_w1_LA=34
    Dev_w2_LA=35
    Dev_w3_LA=36
    Dev_w4_LA=37
    Dummy_H_LA=38
    Height_LA=39
    Volume_LA=40
    S_N_LA=41
    Atom1_LA=42
    Atom2_LA=43
    Atom3_LA=44
    Atom4_LA=45
    Distance_LA=46
    Note_LA=47
    SPACE_LA=48
    RETURN_LA=49

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

        def RETURN(self, i:int=None):
            if i is None:
                return self.getTokens(SparkyNPKParser.RETURN)
            else:
                return self.getToken(SparkyNPKParser.RETURN, i)

        def data_label(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.Data_labelContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.Data_labelContext,i)


        def peak_2d_po(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.Peak_2d_poContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.Peak_2d_poContext,i)


        def peak_3d_po(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.Peak_3d_poContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.Peak_3d_poContext,i)


        def peak_4d_po(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.Peak_4d_poContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.Peak_4d_poContext,i)


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
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 20
                self.match(SparkyNPKParser.RETURN)


            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 269314) != 0):
                self.state = 55
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 23
                    self.data_label()
                    pass

                elif la_ == 2:
                    self.state = 25 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 24
                            self.peak_2d_po()

                        else:
                            raise NoViableAltException(self)
                        self.state = 27 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                    pass

                elif la_ == 3:
                    self.state = 30 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 29
                            self.peak_3d_po()

                        else:
                            raise NoViableAltException(self)
                        self.state = 32 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                    pass

                elif la_ == 4:
                    self.state = 35 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 34
                            self.peak_4d_po()

                        else:
                            raise NoViableAltException(self)
                        self.state = 37 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                    pass

                elif la_ == 5:
                    self.state = 40 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 39
                            self.peak_2d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 42 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                    pass

                elif la_ == 6:
                    self.state = 45 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 44
                            self.peak_3d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 47 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                    pass

                elif la_ == 7:
                    self.state = 50 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 49
                            self.peak_4d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 52 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                    pass

                elif la_ == 8:
                    self.state = 54
                    self.match(SparkyNPKParser.RETURN)
                    pass


                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
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

        def W1_LA(self):
            return self.getToken(SparkyNPKParser.W1_LA, 0)

        def W2_LA(self):
            return self.getToken(SparkyNPKParser.W2_LA, 0)

        def RETURN_LA(self):
            return self.getToken(SparkyNPKParser.RETURN_LA, 0)

        def Assignment(self):
            return self.getToken(SparkyNPKParser.Assignment, 0)

        def Assignment_2d_ex(self):
            return self.getToken(SparkyNPKParser.Assignment_2d_ex, 0)

        def Assignment_3d_ex(self):
            return self.getToken(SparkyNPKParser.Assignment_3d_ex, 0)

        def Assignment_4d_ex(self):
            return self.getToken(SparkyNPKParser.Assignment_4d_ex, 0)

        def W3_LA(self):
            return self.getToken(SparkyNPKParser.W3_LA, 0)

        def W4_LA(self):
            return self.getToken(SparkyNPKParser.W4_LA, 0)

        def W1_Hz_LA(self):
            return self.getToken(SparkyNPKParser.W1_Hz_LA, 0)

        def W2_Hz_LA(self):
            return self.getToken(SparkyNPKParser.W2_Hz_LA, 0)

        def W3_Hz_LA(self):
            return self.getToken(SparkyNPKParser.W3_Hz_LA, 0)

        def W4_Hz_LA(self):
            return self.getToken(SparkyNPKParser.W4_Hz_LA, 0)

        def Dev_w1_LA(self):
            return self.getToken(SparkyNPKParser.Dev_w1_LA, 0)

        def Dev_w2_LA(self):
            return self.getToken(SparkyNPKParser.Dev_w2_LA, 0)

        def Dev_w3_LA(self):
            return self.getToken(SparkyNPKParser.Dev_w3_LA, 0)

        def Dev_w4_LA(self):
            return self.getToken(SparkyNPKParser.Dev_w4_LA, 0)

        def S_N_LA(self):
            return self.getToken(SparkyNPKParser.S_N_LA, 0)

        def Lw1_Hz_LA(self):
            return self.getToken(SparkyNPKParser.Lw1_Hz_LA, 0)

        def Lw2_Hz_LA(self):
            return self.getToken(SparkyNPKParser.Lw2_Hz_LA, 0)

        def Lw3_Hz_LA(self):
            return self.getToken(SparkyNPKParser.Lw3_Hz_LA, 0)

        def Lw4_Hz_LA(self):
            return self.getToken(SparkyNPKParser.Lw4_Hz_LA, 0)

        def Atom1_LA(self):
            return self.getToken(SparkyNPKParser.Atom1_LA, 0)

        def Atom2_LA(self):
            return self.getToken(SparkyNPKParser.Atom2_LA, 0)

        def Atom3_LA(self):
            return self.getToken(SparkyNPKParser.Atom3_LA, 0)

        def Atom4_LA(self):
            return self.getToken(SparkyNPKParser.Atom4_LA, 0)

        def Distance_LA(self):
            return self.getToken(SparkyNPKParser.Distance_LA, 0)

        def Note_LA(self):
            return self.getToken(SparkyNPKParser.Note_LA, 0)

        def RETURN(self):
            return self.getToken(SparkyNPKParser.RETURN, 0)

        def Height_LA(self, i:int=None):
            if i is None:
                return self.getTokens(SparkyNPKParser.Height_LA)
            else:
                return self.getToken(SparkyNPKParser.Height_LA, i)

        def Volume_LA(self, i:int=None):
            if i is None:
                return self.getTokens(SparkyNPKParser.Volume_LA)
            else:
                return self.getToken(SparkyNPKParser.Volume_LA, i)

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
            self.state = 62
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7170) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 63
            self.match(SparkyNPKParser.W1_LA)
            self.state = 64
            self.match(SparkyNPKParser.W2_LA)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 65
                self.match(SparkyNPKParser.W3_LA)


            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 68
                self.match(SparkyNPKParser.W4_LA)


            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 71
                self.match(SparkyNPKParser.W1_Hz_LA)


            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 74
                self.match(SparkyNPKParser.W2_Hz_LA)


            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 77
                self.match(SparkyNPKParser.W3_Hz_LA)


            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 80
                self.match(SparkyNPKParser.W4_Hz_LA)


            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 83
                self.match(SparkyNPKParser.Dev_w1_LA)


            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 86
                self.match(SparkyNPKParser.Dev_w2_LA)


            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 89
                self.match(SparkyNPKParser.Dev_w3_LA)


            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 92
                self.match(SparkyNPKParser.Dev_w4_LA)


            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 95
                _la = self._input.LA(1)
                if not(_la==39 or _la==40):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39 or _la==40:
                self.state = 98
                _la = self._input.LA(1)
                if not(_la==39 or _la==40):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 101
                self.match(SparkyNPKParser.S_N_LA)


            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 104
                self.match(SparkyNPKParser.Lw1_Hz_LA)


            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 107
                self.match(SparkyNPKParser.Lw2_Hz_LA)


            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 110
                self.match(SparkyNPKParser.Lw3_Hz_LA)


            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 113
                self.match(SparkyNPKParser.Lw4_Hz_LA)


            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 116
                self.match(SparkyNPKParser.Atom1_LA)


            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 119
                self.match(SparkyNPKParser.Atom2_LA)


            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44:
                self.state = 122
                self.match(SparkyNPKParser.Atom3_LA)


            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==45:
                self.state = 125
                self.match(SparkyNPKParser.Atom4_LA)


            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 128
                self.match(SparkyNPKParser.Distance_LA)


            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 131
                self.match(SparkyNPKParser.Note_LA)


            self.state = 134
            self.match(SparkyNPKParser.RETURN_LA)
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 135
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
            self.state = 138
            self.match(SparkyNPKParser.Assignment_2d_ex)
            self.state = 139
            self.match(SparkyNPKParser.Float)
            self.state = 140
            self.match(SparkyNPKParser.Float)
            self.state = 144
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 141
                    self.number() 
                self.state = 146
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 122904) != 0):
                self.state = 147
                self.note()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 153
            _la = self._input.LA(1)
            if not(_la==-1 or _la==18):
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
            self.state = 155
            self.match(SparkyNPKParser.Assignment_3d_ex)
            self.state = 156
            self.match(SparkyNPKParser.Float)
            self.state = 157
            self.match(SparkyNPKParser.Float)
            self.state = 158
            self.match(SparkyNPKParser.Float)
            self.state = 162
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 159
                    self.number() 
                self.state = 164
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 122904) != 0):
                self.state = 165
                self.note()
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 171
            _la = self._input.LA(1)
            if not(_la==-1 or _la==18):
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
            self.state = 173
            self.match(SparkyNPKParser.Assignment_4d_ex)
            self.state = 174
            self.match(SparkyNPKParser.Float)
            self.state = 175
            self.match(SparkyNPKParser.Float)
            self.state = 176
            self.match(SparkyNPKParser.Float)
            self.state = 177
            self.match(SparkyNPKParser.Float)
            self.state = 181
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 178
                    self.number() 
                self.state = 183
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 122904) != 0):
                self.state = 184
                self.note()
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 190
            _la = self._input.LA(1)
            if not(_la==-1 or _la==18):
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


    class Peak_2d_poContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(SparkyNPKParser.Float)
            else:
                return self.getToken(SparkyNPKParser.Float, i)

        def Assignment_2d_ex(self):
            return self.getToken(SparkyNPKParser.Assignment_2d_ex, 0)

        def Assignment_3d_ex(self):
            return self.getToken(SparkyNPKParser.Assignment_3d_ex, 0)

        def Assignment_4d_ex(self):
            return self.getToken(SparkyNPKParser.Assignment_4d_ex, 0)

        def RETURN(self):
            return self.getToken(SparkyNPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(SparkyNPKParser.EOF, 0)

        def getRuleIndex(self):
            return SparkyNPKParser.RULE_peak_2d_po

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_2d_po" ):
                listener.enterPeak_2d_po(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_2d_po" ):
                listener.exitPeak_2d_po(self)




    def peak_2d_po(self):

        localctx = SparkyNPKParser.Peak_2d_poContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_peak_2d_po)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7168) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 193
            self.match(SparkyNPKParser.Float)
            self.state = 194
            self.match(SparkyNPKParser.Float)
            self.state = 195
            _la = self._input.LA(1)
            if not(_la==-1 or _la==18):
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


    class Peak_3d_poContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(SparkyNPKParser.Float)
            else:
                return self.getToken(SparkyNPKParser.Float, i)

        def Assignment_3d_ex(self):
            return self.getToken(SparkyNPKParser.Assignment_3d_ex, 0)

        def Assignment_4d_ex(self):
            return self.getToken(SparkyNPKParser.Assignment_4d_ex, 0)

        def RETURN(self):
            return self.getToken(SparkyNPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(SparkyNPKParser.EOF, 0)

        def getRuleIndex(self):
            return SparkyNPKParser.RULE_peak_3d_po

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_3d_po" ):
                listener.enterPeak_3d_po(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_3d_po" ):
                listener.exitPeak_3d_po(self)




    def peak_3d_po(self):

        localctx = SparkyNPKParser.Peak_3d_poContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_peak_3d_po)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 198
            self.match(SparkyNPKParser.Float)
            self.state = 199
            self.match(SparkyNPKParser.Float)
            self.state = 200
            self.match(SparkyNPKParser.Float)
            self.state = 201
            _la = self._input.LA(1)
            if not(_la==-1 or _la==18):
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


    class Peak_4d_poContext(ParserRuleContext):
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

        def getRuleIndex(self):
            return SparkyNPKParser.RULE_peak_4d_po

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_4d_po" ):
                listener.enterPeak_4d_po(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_4d_po" ):
                listener.exitPeak_4d_po(self)




    def peak_4d_po(self):

        localctx = SparkyNPKParser.Peak_4d_poContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_peak_4d_po)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(SparkyNPKParser.Assignment_4d_ex)
            self.state = 204
            self.match(SparkyNPKParser.Float)
            self.state = 205
            self.match(SparkyNPKParser.Float)
            self.state = 206
            self.match(SparkyNPKParser.Float)
            self.state = 207
            self.match(SparkyNPKParser.Float)
            self.state = 208
            _la = self._input.LA(1)
            if not(_la==-1 or _la==18):
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

        def Real_vol(self):
            return self.getToken(SparkyNPKParser.Real_vol, 0)

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
        self.enterRule(localctx, 16, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 120) != 0)):
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

        def Note_2d_ex(self):
            return self.getToken(SparkyNPKParser.Note_2d_ex, 0)

        def Note_3d_ex(self):
            return self.getToken(SparkyNPKParser.Note_3d_ex, 0)

        def Note_4d_ex(self):
            return self.getToken(SparkyNPKParser.Note_4d_ex, 0)

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
        self.enterRule(localctx, 18, self.RULE_note)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122904) != 0)):
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





