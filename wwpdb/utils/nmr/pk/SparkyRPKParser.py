# Generated from SparkyRPKParser.g4 by ANTLR 4.13.0
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
        4,1,49,256,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,3,0,20,8,0,1,0,1,0,1,0,4,0,25,8,0,11,0,12,
        0,26,1,0,4,0,30,8,0,11,0,12,0,31,1,0,4,0,35,8,0,11,0,12,0,36,1,0,
        5,0,40,8,0,10,0,12,0,43,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,51,8,1,1,
        1,3,1,54,8,1,1,1,3,1,57,8,1,1,1,3,1,60,8,1,1,1,3,1,63,8,1,1,1,3,
        1,66,8,1,1,1,3,1,69,8,1,1,1,3,1,72,8,1,1,1,3,1,75,8,1,1,1,3,1,78,
        8,1,1,1,3,1,81,8,1,1,1,3,1,84,8,1,1,1,3,1,87,8,1,1,1,3,1,90,8,1,
        1,1,3,1,93,8,1,1,1,3,1,96,8,1,1,1,3,1,99,8,1,1,1,3,1,102,8,1,1,1,
        3,1,105,8,1,1,1,3,1,108,8,1,1,1,3,1,111,8,1,1,1,3,1,114,8,1,1,1,
        3,1,117,8,1,1,1,1,1,3,1,121,8,1,1,2,1,2,1,2,3,2,126,8,2,1,2,3,2,
        129,8,2,1,2,3,2,132,8,2,1,2,3,2,135,8,2,1,2,3,2,138,8,2,1,2,3,2,
        141,8,2,1,2,3,2,144,8,2,1,2,3,2,147,8,2,1,2,3,2,150,8,2,1,2,3,2,
        153,8,2,1,2,3,2,156,8,2,1,2,3,2,159,8,2,1,2,3,2,162,8,2,1,2,3,2,
        165,8,2,1,2,3,2,168,8,2,1,2,3,2,171,8,2,1,2,3,2,174,8,2,1,2,3,2,
        177,8,2,1,2,3,2,180,8,2,1,2,1,2,3,2,184,8,2,1,2,4,2,187,8,2,11,2,
        12,2,188,1,3,1,3,1,3,1,3,4,3,195,8,3,11,3,12,3,196,1,3,5,3,200,8,
        3,10,3,12,3,203,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,4,4,212,8,4,11,4,
        12,4,213,1,4,5,4,217,8,4,10,4,12,4,220,9,4,1,4,1,4,1,5,1,5,1,5,1,
        5,1,5,1,5,4,5,230,8,5,11,5,12,5,231,1,5,5,5,235,8,5,10,5,12,5,238,
        9,5,1,5,1,5,1,6,4,6,243,8,6,11,6,12,6,244,1,6,3,6,248,8,6,1,6,1,
        6,1,7,1,7,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,4,2,0,1,1,10,
        12,1,1,18,18,1,0,3,6,2,0,3,4,13,16,309,0,19,1,0,0,0,2,46,1,0,0,0,
        4,122,1,0,0,0,6,190,1,0,0,0,8,206,1,0,0,0,10,223,1,0,0,0,12,242,
        1,0,0,0,14,251,1,0,0,0,16,253,1,0,0,0,18,20,5,18,0,0,19,18,1,0,0,
        0,19,20,1,0,0,0,20,41,1,0,0,0,21,40,3,2,1,0,22,40,3,4,2,0,23,25,
        3,6,3,0,24,23,1,0,0,0,25,26,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,
        27,40,1,0,0,0,28,30,3,8,4,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,
        0,0,0,31,32,1,0,0,0,32,40,1,0,0,0,33,35,3,10,5,0,34,33,1,0,0,0,35,
        36,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,40,1,0,0,0,38,40,5,18,
        0,0,39,21,1,0,0,0,39,22,1,0,0,0,39,24,1,0,0,0,39,29,1,0,0,0,39,34,
        1,0,0,0,39,38,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,
        42,44,1,0,0,0,43,41,1,0,0,0,44,45,5,0,0,1,45,1,1,0,0,0,46,47,7,0,
        0,0,47,48,5,30,0,0,48,50,5,31,0,0,49,51,5,32,0,0,50,49,1,0,0,0,50,
        51,1,0,0,0,51,53,1,0,0,0,52,54,5,33,0,0,53,52,1,0,0,0,53,54,1,0,
        0,0,54,56,1,0,0,0,55,57,5,22,0,0,56,55,1,0,0,0,56,57,1,0,0,0,57,
        59,1,0,0,0,58,60,5,23,0,0,59,58,1,0,0,0,59,60,1,0,0,0,60,62,1,0,
        0,0,61,63,5,24,0,0,62,61,1,0,0,0,62,63,1,0,0,0,63,65,1,0,0,0,64,
        66,5,25,0,0,65,64,1,0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,69,5,34,
        0,0,68,67,1,0,0,0,68,69,1,0,0,0,69,71,1,0,0,0,70,72,5,35,0,0,71,
        70,1,0,0,0,71,72,1,0,0,0,72,74,1,0,0,0,73,75,5,36,0,0,74,73,1,0,
        0,0,74,75,1,0,0,0,75,77,1,0,0,0,76,78,5,37,0,0,77,76,1,0,0,0,77,
        78,1,0,0,0,78,80,1,0,0,0,79,81,5,40,0,0,80,79,1,0,0,0,80,81,1,0,
        0,0,81,83,1,0,0,0,82,84,5,39,0,0,83,82,1,0,0,0,83,84,1,0,0,0,84,
        86,1,0,0,0,85,87,5,41,0,0,86,85,1,0,0,0,86,87,1,0,0,0,87,89,1,0,
        0,0,88,90,5,26,0,0,89,88,1,0,0,0,89,90,1,0,0,0,90,92,1,0,0,0,91,
        93,5,27,0,0,92,91,1,0,0,0,92,93,1,0,0,0,93,95,1,0,0,0,94,96,5,28,
        0,0,95,94,1,0,0,0,95,96,1,0,0,0,96,98,1,0,0,0,97,99,5,29,0,0,98,
        97,1,0,0,0,98,99,1,0,0,0,99,101,1,0,0,0,100,102,5,42,0,0,101,100,
        1,0,0,0,101,102,1,0,0,0,102,104,1,0,0,0,103,105,5,43,0,0,104,103,
        1,0,0,0,104,105,1,0,0,0,105,107,1,0,0,0,106,108,5,44,0,0,107,106,
        1,0,0,0,107,108,1,0,0,0,108,110,1,0,0,0,109,111,5,45,0,0,110,109,
        1,0,0,0,110,111,1,0,0,0,111,113,1,0,0,0,112,114,5,46,0,0,113,112,
        1,0,0,0,113,114,1,0,0,0,114,116,1,0,0,0,115,117,5,47,0,0,116,115,
        1,0,0,0,116,117,1,0,0,0,117,118,1,0,0,0,118,120,5,49,0,0,119,121,
        5,18,0,0,120,119,1,0,0,0,120,121,1,0,0,0,121,3,1,0,0,0,122,123,5,
        2,0,0,123,125,5,31,0,0,124,126,5,32,0,0,125,124,1,0,0,0,125,126,
        1,0,0,0,126,128,1,0,0,0,127,129,5,33,0,0,128,127,1,0,0,0,128,129,
        1,0,0,0,129,131,1,0,0,0,130,132,5,22,0,0,131,130,1,0,0,0,131,132,
        1,0,0,0,132,134,1,0,0,0,133,135,5,23,0,0,134,133,1,0,0,0,134,135,
        1,0,0,0,135,137,1,0,0,0,136,138,5,24,0,0,137,136,1,0,0,0,137,138,
        1,0,0,0,138,140,1,0,0,0,139,141,5,25,0,0,140,139,1,0,0,0,140,141,
        1,0,0,0,141,143,1,0,0,0,142,144,5,34,0,0,143,142,1,0,0,0,143,144,
        1,0,0,0,144,146,1,0,0,0,145,147,5,35,0,0,146,145,1,0,0,0,146,147,
        1,0,0,0,147,149,1,0,0,0,148,150,5,36,0,0,149,148,1,0,0,0,149,150,
        1,0,0,0,150,152,1,0,0,0,151,153,5,37,0,0,152,151,1,0,0,0,152,153,
        1,0,0,0,153,155,1,0,0,0,154,156,5,40,0,0,155,154,1,0,0,0,155,156,
        1,0,0,0,156,158,1,0,0,0,157,159,5,39,0,0,158,157,1,0,0,0,158,159,
        1,0,0,0,159,161,1,0,0,0,160,162,5,41,0,0,161,160,1,0,0,0,161,162,
        1,0,0,0,162,164,1,0,0,0,163,165,5,26,0,0,164,163,1,0,0,0,164,165,
        1,0,0,0,165,167,1,0,0,0,166,168,5,27,0,0,167,166,1,0,0,0,167,168,
        1,0,0,0,168,170,1,0,0,0,169,171,5,28,0,0,170,169,1,0,0,0,170,171,
        1,0,0,0,171,173,1,0,0,0,172,174,5,29,0,0,173,172,1,0,0,0,173,174,
        1,0,0,0,174,176,1,0,0,0,175,177,5,46,0,0,176,175,1,0,0,0,176,177,
        1,0,0,0,177,179,1,0,0,0,178,180,5,47,0,0,179,178,1,0,0,0,179,180,
        1,0,0,0,180,181,1,0,0,0,181,183,5,49,0,0,182,184,5,18,0,0,183,182,
        1,0,0,0,183,184,1,0,0,0,184,186,1,0,0,0,185,187,3,12,6,0,186,185,
        1,0,0,0,187,188,1,0,0,0,188,186,1,0,0,0,188,189,1,0,0,0,189,5,1,
        0,0,0,190,191,5,10,0,0,191,192,5,4,0,0,192,194,5,4,0,0,193,195,3,
        14,7,0,194,193,1,0,0,0,195,196,1,0,0,0,196,194,1,0,0,0,196,197,1,
        0,0,0,197,201,1,0,0,0,198,200,3,16,8,0,199,198,1,0,0,0,200,203,1,
        0,0,0,201,199,1,0,0,0,201,202,1,0,0,0,202,204,1,0,0,0,203,201,1,
        0,0,0,204,205,7,1,0,0,205,7,1,0,0,0,206,207,5,11,0,0,207,208,5,4,
        0,0,208,209,5,4,0,0,209,211,5,4,0,0,210,212,3,14,7,0,211,210,1,0,
        0,0,212,213,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,218,1,0,
        0,0,215,217,3,16,8,0,216,215,1,0,0,0,217,220,1,0,0,0,218,216,1,0,
        0,0,218,219,1,0,0,0,219,221,1,0,0,0,220,218,1,0,0,0,221,222,7,1,
        0,0,222,9,1,0,0,0,223,224,5,12,0,0,224,225,5,4,0,0,225,226,5,4,0,
        0,226,227,5,4,0,0,227,229,5,4,0,0,228,230,3,14,7,0,229,228,1,0,0,
        0,230,231,1,0,0,0,231,229,1,0,0,0,231,232,1,0,0,0,232,236,1,0,0,
        0,233,235,3,16,8,0,234,233,1,0,0,0,235,238,1,0,0,0,236,234,1,0,0,
        0,236,237,1,0,0,0,237,239,1,0,0,0,238,236,1,0,0,0,239,240,7,1,0,
        0,240,11,1,0,0,0,241,243,3,14,7,0,242,241,1,0,0,0,243,244,1,0,0,
        0,244,242,1,0,0,0,244,245,1,0,0,0,245,247,1,0,0,0,246,248,3,16,8,
        0,247,246,1,0,0,0,247,248,1,0,0,0,248,249,1,0,0,0,249,250,7,1,0,
        0,250,13,1,0,0,0,251,252,7,2,0,0,252,15,1,0,0,0,253,254,7,3,0,0,
        254,17,1,0,0,0,59,19,26,31,36,39,41,50,53,56,59,62,65,68,71,74,77,
        80,83,86,89,92,95,98,101,104,107,110,113,116,120,125,128,131,134,
        137,140,143,146,149,152,155,158,161,164,167,170,173,176,179,183,
        188,196,201,213,218,231,236,244,247
    ]

class SparkyRPKParser ( Parser ):

    grammarFileName = "SparkyRPKParser.g4"

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

    RULE_sparky_rpk = 0
    RULE_data_label = 1
    RULE_data_label_wo_assign = 2
    RULE_peak_2d = 3
    RULE_peak_3d = 4
    RULE_peak_4d = 5
    RULE_peak_wo_assign = 6
    RULE_number = 7
    RULE_note = 8

    ruleNames =  [ "sparky_rpk", "data_label", "data_label_wo_assign", "peak_2d", 
                   "peak_3d", "peak_4d", "peak_wo_assign", "number", "note" ]

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




    class Sparky_rpkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SparkyRPKParser.EOF, 0)

        def RETURN(self, i:int=None):
            if i is None:
                return self.getTokens(SparkyRPKParser.RETURN)
            else:
                return self.getToken(SparkyRPKParser.RETURN, i)

        def data_label(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.Data_labelContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.Data_labelContext,i)


        def data_label_wo_assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.Data_label_wo_assignContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.Data_label_wo_assignContext,i)


        def peak_2d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.Peak_2dContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.Peak_2dContext,i)


        def peak_3d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.Peak_3dContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.Peak_3dContext,i)


        def peak_4d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.Peak_4dContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.Peak_4dContext,i)


        def getRuleIndex(self):
            return SparkyRPKParser.RULE_sparky_rpk

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSparky_rpk" ):
                listener.enterSparky_rpk(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSparky_rpk" ):
                listener.exitSparky_rpk(self)




    def sparky_rpk(self):

        localctx = SparkyRPKParser.Sparky_rpkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sparky_rpk)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 18
                self.match(SparkyRPKParser.RETURN)


            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 269318) != 0):
                self.state = 39
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 21
                    self.data_label()
                    pass

                elif la_ == 2:
                    self.state = 22
                    self.data_label_wo_assign()
                    pass

                elif la_ == 3:
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

                elif la_ == 4:
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

                elif la_ == 5:
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

                elif la_ == 6:
                    self.state = 38
                    self.match(SparkyRPKParser.RETURN)
                    pass


                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.match(SparkyRPKParser.EOF)
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
            return self.getToken(SparkyRPKParser.W1_LA, 0)

        def W2_LA(self):
            return self.getToken(SparkyRPKParser.W2_LA, 0)

        def RETURN_LA(self):
            return self.getToken(SparkyRPKParser.RETURN_LA, 0)

        def Assignment(self):
            return self.getToken(SparkyRPKParser.Assignment, 0)

        def Assignment_2d_ex(self):
            return self.getToken(SparkyRPKParser.Assignment_2d_ex, 0)

        def Assignment_3d_ex(self):
            return self.getToken(SparkyRPKParser.Assignment_3d_ex, 0)

        def Assignment_4d_ex(self):
            return self.getToken(SparkyRPKParser.Assignment_4d_ex, 0)

        def W3_LA(self):
            return self.getToken(SparkyRPKParser.W3_LA, 0)

        def W4_LA(self):
            return self.getToken(SparkyRPKParser.W4_LA, 0)

        def W1_Hz_LA(self):
            return self.getToken(SparkyRPKParser.W1_Hz_LA, 0)

        def W2_Hz_LA(self):
            return self.getToken(SparkyRPKParser.W2_Hz_LA, 0)

        def W3_Hz_LA(self):
            return self.getToken(SparkyRPKParser.W3_Hz_LA, 0)

        def W4_Hz_LA(self):
            return self.getToken(SparkyRPKParser.W4_Hz_LA, 0)

        def Dev_w1_LA(self):
            return self.getToken(SparkyRPKParser.Dev_w1_LA, 0)

        def Dev_w2_LA(self):
            return self.getToken(SparkyRPKParser.Dev_w2_LA, 0)

        def Dev_w3_LA(self):
            return self.getToken(SparkyRPKParser.Dev_w3_LA, 0)

        def Dev_w4_LA(self):
            return self.getToken(SparkyRPKParser.Dev_w4_LA, 0)

        def Volume_LA(self):
            return self.getToken(SparkyRPKParser.Volume_LA, 0)

        def Height_LA(self):
            return self.getToken(SparkyRPKParser.Height_LA, 0)

        def S_N_LA(self):
            return self.getToken(SparkyRPKParser.S_N_LA, 0)

        def Lw1_Hz_LA(self):
            return self.getToken(SparkyRPKParser.Lw1_Hz_LA, 0)

        def Lw2_Hz_LA(self):
            return self.getToken(SparkyRPKParser.Lw2_Hz_LA, 0)

        def Lw3_Hz_LA(self):
            return self.getToken(SparkyRPKParser.Lw3_Hz_LA, 0)

        def Lw4_Hz_LA(self):
            return self.getToken(SparkyRPKParser.Lw4_Hz_LA, 0)

        def Atom1_LA(self):
            return self.getToken(SparkyRPKParser.Atom1_LA, 0)

        def Atom2_LA(self):
            return self.getToken(SparkyRPKParser.Atom2_LA, 0)

        def Atom3_LA(self):
            return self.getToken(SparkyRPKParser.Atom3_LA, 0)

        def Atom4_LA(self):
            return self.getToken(SparkyRPKParser.Atom4_LA, 0)

        def Distance_LA(self):
            return self.getToken(SparkyRPKParser.Distance_LA, 0)

        def Note_LA(self):
            return self.getToken(SparkyRPKParser.Note_LA, 0)

        def RETURN(self):
            return self.getToken(SparkyRPKParser.RETURN, 0)

        def getRuleIndex(self):
            return SparkyRPKParser.RULE_data_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_label" ):
                listener.enterData_label(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_label" ):
                listener.exitData_label(self)




    def data_label(self):

        localctx = SparkyRPKParser.Data_labelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_data_label)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7170) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 47
            self.match(SparkyRPKParser.W1_LA)
            self.state = 48
            self.match(SparkyRPKParser.W2_LA)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 49
                self.match(SparkyRPKParser.W3_LA)


            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 52
                self.match(SparkyRPKParser.W4_LA)


            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 55
                self.match(SparkyRPKParser.W1_Hz_LA)


            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 58
                self.match(SparkyRPKParser.W2_Hz_LA)


            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 61
                self.match(SparkyRPKParser.W3_Hz_LA)


            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 64
                self.match(SparkyRPKParser.W4_Hz_LA)


            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 67
                self.match(SparkyRPKParser.Dev_w1_LA)


            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 70
                self.match(SparkyRPKParser.Dev_w2_LA)


            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 73
                self.match(SparkyRPKParser.Dev_w3_LA)


            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 76
                self.match(SparkyRPKParser.Dev_w4_LA)


            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 79
                self.match(SparkyRPKParser.Volume_LA)


            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 82
                self.match(SparkyRPKParser.Height_LA)


            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 85
                self.match(SparkyRPKParser.S_N_LA)


            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 88
                self.match(SparkyRPKParser.Lw1_Hz_LA)


            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 91
                self.match(SparkyRPKParser.Lw2_Hz_LA)


            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 94
                self.match(SparkyRPKParser.Lw3_Hz_LA)


            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 97
                self.match(SparkyRPKParser.Lw4_Hz_LA)


            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 100
                self.match(SparkyRPKParser.Atom1_LA)


            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 103
                self.match(SparkyRPKParser.Atom2_LA)


            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44:
                self.state = 106
                self.match(SparkyRPKParser.Atom3_LA)


            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==45:
                self.state = 109
                self.match(SparkyRPKParser.Atom4_LA)


            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 112
                self.match(SparkyRPKParser.Distance_LA)


            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 115
                self.match(SparkyRPKParser.Note_LA)


            self.state = 118
            self.match(SparkyRPKParser.RETURN_LA)
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 119
                self.match(SparkyRPKParser.RETURN)


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
            return self.getToken(SparkyRPKParser.W1, 0)

        def W2_LA(self):
            return self.getToken(SparkyRPKParser.W2_LA, 0)

        def RETURN_LA(self):
            return self.getToken(SparkyRPKParser.RETURN_LA, 0)

        def W3_LA(self):
            return self.getToken(SparkyRPKParser.W3_LA, 0)

        def W4_LA(self):
            return self.getToken(SparkyRPKParser.W4_LA, 0)

        def W1_Hz_LA(self):
            return self.getToken(SparkyRPKParser.W1_Hz_LA, 0)

        def W2_Hz_LA(self):
            return self.getToken(SparkyRPKParser.W2_Hz_LA, 0)

        def W3_Hz_LA(self):
            return self.getToken(SparkyRPKParser.W3_Hz_LA, 0)

        def W4_Hz_LA(self):
            return self.getToken(SparkyRPKParser.W4_Hz_LA, 0)

        def Dev_w1_LA(self):
            return self.getToken(SparkyRPKParser.Dev_w1_LA, 0)

        def Dev_w2_LA(self):
            return self.getToken(SparkyRPKParser.Dev_w2_LA, 0)

        def Dev_w3_LA(self):
            return self.getToken(SparkyRPKParser.Dev_w3_LA, 0)

        def Dev_w4_LA(self):
            return self.getToken(SparkyRPKParser.Dev_w4_LA, 0)

        def Volume_LA(self):
            return self.getToken(SparkyRPKParser.Volume_LA, 0)

        def Height_LA(self):
            return self.getToken(SparkyRPKParser.Height_LA, 0)

        def S_N_LA(self):
            return self.getToken(SparkyRPKParser.S_N_LA, 0)

        def Lw1_Hz_LA(self):
            return self.getToken(SparkyRPKParser.Lw1_Hz_LA, 0)

        def Lw2_Hz_LA(self):
            return self.getToken(SparkyRPKParser.Lw2_Hz_LA, 0)

        def Lw3_Hz_LA(self):
            return self.getToken(SparkyRPKParser.Lw3_Hz_LA, 0)

        def Lw4_Hz_LA(self):
            return self.getToken(SparkyRPKParser.Lw4_Hz_LA, 0)

        def Distance_LA(self):
            return self.getToken(SparkyRPKParser.Distance_LA, 0)

        def Note_LA(self):
            return self.getToken(SparkyRPKParser.Note_LA, 0)

        def RETURN(self):
            return self.getToken(SparkyRPKParser.RETURN, 0)

        def peak_wo_assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.Peak_wo_assignContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.Peak_wo_assignContext,i)


        def getRuleIndex(self):
            return SparkyRPKParser.RULE_data_label_wo_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_label_wo_assign" ):
                listener.enterData_label_wo_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_label_wo_assign" ):
                listener.exitData_label_wo_assign(self)




    def data_label_wo_assign(self):

        localctx = SparkyRPKParser.Data_label_wo_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_data_label_wo_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(SparkyRPKParser.W1)
            self.state = 123
            self.match(SparkyRPKParser.W2_LA)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 124
                self.match(SparkyRPKParser.W3_LA)


            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 127
                self.match(SparkyRPKParser.W4_LA)


            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 130
                self.match(SparkyRPKParser.W1_Hz_LA)


            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 133
                self.match(SparkyRPKParser.W2_Hz_LA)


            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 136
                self.match(SparkyRPKParser.W3_Hz_LA)


            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 139
                self.match(SparkyRPKParser.W4_Hz_LA)


            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 142
                self.match(SparkyRPKParser.Dev_w1_LA)


            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 145
                self.match(SparkyRPKParser.Dev_w2_LA)


            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 148
                self.match(SparkyRPKParser.Dev_w3_LA)


            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 151
                self.match(SparkyRPKParser.Dev_w4_LA)


            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 154
                self.match(SparkyRPKParser.Volume_LA)


            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 157
                self.match(SparkyRPKParser.Height_LA)


            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 160
                self.match(SparkyRPKParser.S_N_LA)


            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 163
                self.match(SparkyRPKParser.Lw1_Hz_LA)


            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 166
                self.match(SparkyRPKParser.Lw2_Hz_LA)


            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 169
                self.match(SparkyRPKParser.Lw3_Hz_LA)


            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 172
                self.match(SparkyRPKParser.Lw4_Hz_LA)


            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 175
                self.match(SparkyRPKParser.Distance_LA)


            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 178
                self.match(SparkyRPKParser.Note_LA)


            self.state = 181
            self.match(SparkyRPKParser.RETURN_LA)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 182
                self.match(SparkyRPKParser.RETURN)


            self.state = 186 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 185
                self.peak_wo_assign()
                self.state = 188 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 120) != 0)):
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
            return self.getToken(SparkyRPKParser.Assignment_2d_ex, 0)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(SparkyRPKParser.Float)
            else:
                return self.getToken(SparkyRPKParser.Float, i)

        def RETURN(self):
            return self.getToken(SparkyRPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(SparkyRPKParser.EOF, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.NumberContext,i)


        def note(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.NoteContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.NoteContext,i)


        def getRuleIndex(self):
            return SparkyRPKParser.RULE_peak_2d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_2d" ):
                listener.enterPeak_2d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_2d" ):
                listener.exitPeak_2d(self)




    def peak_2d(self):

        localctx = SparkyRPKParser.Peak_2dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_peak_2d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(SparkyRPKParser.Assignment_2d_ex)
            self.state = 191
            self.match(SparkyRPKParser.Float)
            self.state = 192
            self.match(SparkyRPKParser.Float)
            self.state = 194 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 193
                    self.number()

                else:
                    raise NoViableAltException(self)
                self.state = 196 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 122904) != 0):
                self.state = 198
                self.note()
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 204
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
            return self.getToken(SparkyRPKParser.Assignment_3d_ex, 0)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(SparkyRPKParser.Float)
            else:
                return self.getToken(SparkyRPKParser.Float, i)

        def RETURN(self):
            return self.getToken(SparkyRPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(SparkyRPKParser.EOF, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.NumberContext,i)


        def note(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.NoteContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.NoteContext,i)


        def getRuleIndex(self):
            return SparkyRPKParser.RULE_peak_3d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_3d" ):
                listener.enterPeak_3d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_3d" ):
                listener.exitPeak_3d(self)




    def peak_3d(self):

        localctx = SparkyRPKParser.Peak_3dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_peak_3d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(SparkyRPKParser.Assignment_3d_ex)
            self.state = 207
            self.match(SparkyRPKParser.Float)
            self.state = 208
            self.match(SparkyRPKParser.Float)
            self.state = 209
            self.match(SparkyRPKParser.Float)
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
                _alt = self._interp.adaptivePredict(self._input,53,self._ctx)

            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 122904) != 0):
                self.state = 215
                self.note()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 221
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
            return self.getToken(SparkyRPKParser.Assignment_4d_ex, 0)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(SparkyRPKParser.Float)
            else:
                return self.getToken(SparkyRPKParser.Float, i)

        def RETURN(self):
            return self.getToken(SparkyRPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(SparkyRPKParser.EOF, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.NumberContext,i)


        def note(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.NoteContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.NoteContext,i)


        def getRuleIndex(self):
            return SparkyRPKParser.RULE_peak_4d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_4d" ):
                listener.enterPeak_4d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_4d" ):
                listener.exitPeak_4d(self)




    def peak_4d(self):

        localctx = SparkyRPKParser.Peak_4dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_peak_4d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(SparkyRPKParser.Assignment_4d_ex)
            self.state = 224
            self.match(SparkyRPKParser.Float)
            self.state = 225
            self.match(SparkyRPKParser.Float)
            self.state = 226
            self.match(SparkyRPKParser.Float)
            self.state = 227
            self.match(SparkyRPKParser.Float)
            self.state = 229 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 228
                    self.number()

                else:
                    raise NoViableAltException(self)
                self.state = 231 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,55,self._ctx)

            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 122904) != 0):
                self.state = 233
                self.note()
                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 239
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


    class Peak_wo_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(SparkyRPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(SparkyRPKParser.EOF, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.NumberContext,i)


        def note(self):
            return self.getTypedRuleContext(SparkyRPKParser.NoteContext,0)


        def getRuleIndex(self):
            return SparkyRPKParser.RULE_peak_wo_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_wo_assign" ):
                listener.enterPeak_wo_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_wo_assign" ):
                listener.exitPeak_wo_assign(self)




    def peak_wo_assign(self):

        localctx = SparkyRPKParser.Peak_wo_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_peak_wo_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 241
                    self.number()

                else:
                    raise NoViableAltException(self)
                self.state = 244 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,57,self._ctx)

            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 122904) != 0):
                self.state = 246
                self.note()


            self.state = 249
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
            return self.getToken(SparkyRPKParser.Real_vol, 0)

        def Real(self):
            return self.getToken(SparkyRPKParser.Real, 0)

        def Float(self):
            return self.getToken(SparkyRPKParser.Float, 0)

        def Integer(self):
            return self.getToken(SparkyRPKParser.Integer, 0)

        def getRuleIndex(self):
            return SparkyRPKParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = SparkyRPKParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
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
            return self.getToken(SparkyRPKParser.Simple_name, 0)

        def Integer(self):
            return self.getToken(SparkyRPKParser.Integer, 0)

        def Float(self):
            return self.getToken(SparkyRPKParser.Float, 0)

        def Note_2d_ex(self):
            return self.getToken(SparkyRPKParser.Note_2d_ex, 0)

        def Note_3d_ex(self):
            return self.getToken(SparkyRPKParser.Note_3d_ex, 0)

        def Note_4d_ex(self):
            return self.getToken(SparkyRPKParser.Note_4d_ex, 0)

        def getRuleIndex(self):
            return SparkyRPKParser.RULE_note

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNote" ):
                listener.enterNote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNote" ):
                listener.exitNote(self)




    def note(self):

        localctx = SparkyRPKParser.NoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_note)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
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





