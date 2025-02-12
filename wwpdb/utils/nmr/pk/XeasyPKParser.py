# Generated from XeasyPKParser.g4 by ANTLR 4.13.0
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
        4,1,44,273,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,3,0,38,8,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,51,8,0,10,0,12,0,54,9,0,1,
        0,1,0,3,0,58,8,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,
        4,3,72,8,3,11,3,12,3,73,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,
        1,5,1,6,1,6,4,6,89,8,6,11,6,12,6,90,1,6,1,6,1,7,1,7,4,7,97,8,7,11,
        7,12,7,98,1,7,1,7,1,8,1,8,4,8,105,8,8,11,8,12,8,106,1,9,1,9,1,9,
        1,9,1,9,3,9,114,8,9,1,9,1,9,1,9,3,9,119,8,9,1,9,1,9,1,9,1,9,1,9,
        3,9,126,8,9,1,9,1,9,1,9,3,9,131,8,9,3,9,133,8,9,1,9,1,9,1,9,3,9,
        138,8,9,1,9,1,9,1,9,3,9,143,8,9,5,9,145,8,9,10,9,12,9,148,9,9,1,
        10,1,10,4,10,152,8,10,11,10,12,10,153,1,11,1,11,1,11,1,11,1,11,1,
        11,3,11,162,8,11,1,11,1,11,1,11,3,11,167,8,11,1,11,1,11,1,11,1,11,
        1,11,1,11,3,11,175,8,11,1,11,1,11,1,11,3,11,180,8,11,3,11,182,8,
        11,1,11,1,11,1,11,1,11,3,11,188,8,11,1,11,1,11,1,11,3,11,193,8,11,
        5,11,195,8,11,10,11,12,11,198,9,11,1,12,1,12,4,12,202,8,12,11,12,
        12,12,203,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,213,8,13,1,13,
        1,13,1,13,3,13,218,8,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,
        227,8,13,1,13,1,13,1,13,3,13,232,8,13,3,13,234,8,13,1,13,1,13,1,
        13,1,13,1,13,3,13,241,8,13,1,13,1,13,1,13,3,13,246,8,13,5,13,248,
        8,13,10,13,12,13,251,9,13,1,14,1,14,1,15,1,15,1,16,1,16,1,16,3,16,
        260,8,16,3,16,262,8,16,1,17,1,17,5,17,266,8,17,10,17,12,17,269,9,
        17,1,17,1,17,1,17,0,0,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,0,4,1,1,16,16,1,0,8,9,2,0,8,10,14,14,1,1,44,44,310,0,37,
        1,0,0,0,2,61,1,0,0,0,4,65,1,0,0,0,6,69,1,0,0,0,8,77,1,0,0,0,10,82,
        1,0,0,0,12,86,1,0,0,0,14,94,1,0,0,0,16,104,1,0,0,0,18,108,1,0,0,
        0,20,151,1,0,0,0,22,155,1,0,0,0,24,201,1,0,0,0,26,205,1,0,0,0,28,
        252,1,0,0,0,30,254,1,0,0,0,32,261,1,0,0,0,34,263,1,0,0,0,36,38,5,
        16,0,0,37,36,1,0,0,0,37,38,1,0,0,0,38,52,1,0,0,0,39,51,3,2,1,0,40,
        51,3,4,2,0,41,51,3,6,3,0,42,51,3,8,4,0,43,51,3,10,5,0,44,51,3,12,
        6,0,45,51,3,14,7,0,46,51,3,16,8,0,47,51,3,20,10,0,48,51,3,24,12,
        0,49,51,5,16,0,0,50,39,1,0,0,0,50,40,1,0,0,0,50,41,1,0,0,0,50,42,
        1,0,0,0,50,43,1,0,0,0,50,44,1,0,0,0,50,45,1,0,0,0,50,46,1,0,0,0,
        50,47,1,0,0,0,50,48,1,0,0,0,50,49,1,0,0,0,51,54,1,0,0,0,52,50,1,
        0,0,0,52,53,1,0,0,0,53,57,1,0,0,0,54,52,1,0,0,0,55,58,5,16,0,0,56,
        58,3,34,17,0,57,55,1,0,0,0,57,56,1,0,0,0,57,58,1,0,0,0,58,59,1,0,
        0,0,59,60,5,0,0,1,60,1,1,0,0,0,61,62,5,1,0,0,62,63,5,20,0,0,63,64,
        5,22,0,0,64,3,1,0,0,0,65,66,5,2,0,0,66,67,5,23,0,0,67,68,5,25,0,
        0,68,5,1,0,0,0,69,71,5,3,0,0,70,72,5,26,0,0,71,70,1,0,0,0,72,73,
        1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,75,1,0,0,0,75,76,5,28,0,0,
        76,7,1,0,0,0,77,78,5,4,0,0,78,79,5,29,0,0,79,80,5,30,0,0,80,81,5,
        32,0,0,81,9,1,0,0,0,82,83,5,5,0,0,83,84,5,33,0,0,84,85,5,35,0,0,
        85,11,1,0,0,0,86,88,5,6,0,0,87,89,5,36,0,0,88,87,1,0,0,0,89,90,1,
        0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,92,1,0,0,0,92,93,5,38,0,0,93,
        13,1,0,0,0,94,96,5,7,0,0,95,97,5,39,0,0,96,95,1,0,0,0,97,98,1,0,
        0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,100,1,0,0,0,100,101,5,41,0,0,
        101,15,1,0,0,0,102,105,3,18,9,0,103,105,3,34,17,0,104,102,1,0,0,
        0,104,103,1,0,0,0,105,106,1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,
        0,107,17,1,0,0,0,108,109,5,8,0,0,109,110,3,28,14,0,110,111,3,28,
        14,0,111,113,5,8,0,0,112,114,5,14,0,0,113,112,1,0,0,0,113,114,1,
        0,0,0,114,115,1,0,0,0,115,116,3,30,15,0,116,118,3,30,15,0,117,119,
        5,14,0,0,118,117,1,0,0,0,118,119,1,0,0,0,119,120,1,0,0,0,120,132,
        5,8,0,0,121,133,7,0,0,0,122,123,3,32,16,0,123,125,3,32,16,0,124,
        126,5,8,0,0,125,124,1,0,0,0,125,126,1,0,0,0,126,130,1,0,0,0,127,
        131,5,16,0,0,128,131,3,34,17,0,129,131,5,0,0,1,130,127,1,0,0,0,130,
        128,1,0,0,0,130,129,1,0,0,0,131,133,1,0,0,0,132,121,1,0,0,0,132,
        122,1,0,0,0,133,146,1,0,0,0,134,135,3,32,16,0,135,137,3,32,16,0,
        136,138,5,8,0,0,137,136,1,0,0,0,137,138,1,0,0,0,138,142,1,0,0,0,
        139,143,5,16,0,0,140,143,3,34,17,0,141,143,5,0,0,1,142,139,1,0,0,
        0,142,140,1,0,0,0,142,141,1,0,0,0,143,145,1,0,0,0,144,134,1,0,0,
        0,145,148,1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,0,147,19,1,0,0,0,
        148,146,1,0,0,0,149,152,3,22,11,0,150,152,3,34,17,0,151,149,1,0,
        0,0,151,150,1,0,0,0,152,153,1,0,0,0,153,151,1,0,0,0,153,154,1,0,
        0,0,154,21,1,0,0,0,155,156,5,8,0,0,156,157,3,28,14,0,157,158,3,28,
        14,0,158,159,3,28,14,0,159,161,5,8,0,0,160,162,5,14,0,0,161,160,
        1,0,0,0,161,162,1,0,0,0,162,163,1,0,0,0,163,164,3,30,15,0,164,166,
        3,30,15,0,165,167,5,14,0,0,166,165,1,0,0,0,166,167,1,0,0,0,167,168,
        1,0,0,0,168,181,5,8,0,0,169,182,7,0,0,0,170,171,3,32,16,0,171,172,
        3,32,16,0,172,174,3,32,16,0,173,175,5,8,0,0,174,173,1,0,0,0,174,
        175,1,0,0,0,175,179,1,0,0,0,176,180,5,16,0,0,177,180,3,34,17,0,178,
        180,5,0,0,1,179,176,1,0,0,0,179,177,1,0,0,0,179,178,1,0,0,0,180,
        182,1,0,0,0,181,169,1,0,0,0,181,170,1,0,0,0,182,196,1,0,0,0,183,
        184,3,32,16,0,184,185,3,32,16,0,185,187,3,32,16,0,186,188,5,8,0,
        0,187,186,1,0,0,0,187,188,1,0,0,0,188,192,1,0,0,0,189,193,5,16,0,
        0,190,193,3,34,17,0,191,193,5,0,0,1,192,189,1,0,0,0,192,190,1,0,
        0,0,192,191,1,0,0,0,193,195,1,0,0,0,194,183,1,0,0,0,195,198,1,0,
        0,0,196,194,1,0,0,0,196,197,1,0,0,0,197,23,1,0,0,0,198,196,1,0,0,
        0,199,202,3,26,13,0,200,202,3,34,17,0,201,199,1,0,0,0,201,200,1,
        0,0,0,202,203,1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,25,1,0,
        0,0,205,206,5,8,0,0,206,207,3,28,14,0,207,208,3,28,14,0,208,209,
        3,28,14,0,209,210,3,28,14,0,210,212,5,8,0,0,211,213,5,14,0,0,212,
        211,1,0,0,0,212,213,1,0,0,0,213,214,1,0,0,0,214,215,3,30,15,0,215,
        217,3,30,15,0,216,218,5,14,0,0,217,216,1,0,0,0,217,218,1,0,0,0,218,
        219,1,0,0,0,219,233,5,8,0,0,220,234,7,0,0,0,221,222,3,32,16,0,222,
        223,3,32,16,0,223,224,3,32,16,0,224,226,3,32,16,0,225,227,5,8,0,
        0,226,225,1,0,0,0,226,227,1,0,0,0,227,231,1,0,0,0,228,232,5,16,0,
        0,229,232,3,34,17,0,230,232,5,0,0,1,231,228,1,0,0,0,231,229,1,0,
        0,0,231,230,1,0,0,0,232,234,1,0,0,0,233,220,1,0,0,0,233,221,1,0,
        0,0,234,249,1,0,0,0,235,236,3,32,16,0,236,237,3,32,16,0,237,238,
        3,32,16,0,238,240,3,32,16,0,239,241,5,8,0,0,240,239,1,0,0,0,240,
        241,1,0,0,0,241,245,1,0,0,0,242,246,5,16,0,0,243,246,3,34,17,0,244,
        246,5,0,0,1,245,242,1,0,0,0,245,243,1,0,0,0,245,244,1,0,0,0,246,
        248,1,0,0,0,247,235,1,0,0,0,248,251,1,0,0,0,249,247,1,0,0,0,249,
        250,1,0,0,0,250,27,1,0,0,0,251,249,1,0,0,0,252,253,7,1,0,0,253,29,
        1,0,0,0,254,255,7,2,0,0,255,31,1,0,0,0,256,262,5,8,0,0,257,259,5,
        14,0,0,258,260,5,8,0,0,259,258,1,0,0,0,259,260,1,0,0,0,260,262,1,
        0,0,0,261,256,1,0,0,0,261,257,1,0,0,0,262,33,1,0,0,0,263,267,5,11,
        0,0,264,266,5,42,0,0,265,264,1,0,0,0,266,269,1,0,0,0,267,265,1,0,
        0,0,267,268,1,0,0,0,268,270,1,0,0,0,269,267,1,0,0,0,270,271,7,3,
        0,0,271,35,1,0,0,0,40,37,50,52,57,73,90,98,104,106,113,118,125,130,
        132,137,142,146,151,153,161,166,174,179,181,187,192,196,201,203,
        212,217,226,231,233,240,245,249,259,261,267
    ]

class XeasyPKParser ( Parser ):

    grammarFileName = "XeasyPKParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'#FORMAT'", 
                     "'#INAME'", "'#CYANAFORMAT'", "'#SPECTRUM'", "'#TOLERANCE'" ]

    symbolicNames = [ "<INVALID>", "Num_of_dim", "Num_of_peaks", "Format", 
                      "Iname", "Cyana_format", "Spectrum", "Tolerance", 
                      "Integer", "Float", "Real", "COMMENT", "EXCLM_COMMENT", 
                      "SMCLN_COMMENT", "Simple_name", "SPACE", "RETURN", 
                      "ENCLOSE_COMMENT", "SECTION_COMMENT", "LINE_COMMENT", 
                      "Integer_ND", "SPACE_ND", "RETURN_ND", "Integer_NP", 
                      "SPACE_NP", "RETURN_NP", "Simple_name_FO", "SPACE_FO", 
                      "RETURN_FO", "Integer_IN", "Simple_name_IN", "SPACE_IN", 
                      "RETURN_IN", "Simple_name_CY", "SPACE_CY", "RETURN_CY", 
                      "Simple_name_SP", "SPACE_SP", "RETURN_SP", "Float_TO", 
                      "TOACE_TO", "RETURN_TO", "Any_name", "SPACE_CM", "RETURN_CM" ]

    RULE_xeasy_pk = 0
    RULE_dimension = 1
    RULE_peak = 2
    RULE_format = 3
    RULE_iname = 4
    RULE_cyana_format = 5
    RULE_spectrum = 6
    RULE_tolerance = 7
    RULE_peak_list_2d = 8
    RULE_peak_2d = 9
    RULE_peak_list_3d = 10
    RULE_peak_3d = 11
    RULE_peak_list_4d = 12
    RULE_peak_4d = 13
    RULE_position = 14
    RULE_number = 15
    RULE_assign = 16
    RULE_comment = 17

    ruleNames =  [ "xeasy_pk", "dimension", "peak", "format", "iname", "cyana_format", 
                   "spectrum", "tolerance", "peak_list_2d", "peak_2d", "peak_list_3d", 
                   "peak_3d", "peak_list_4d", "peak_4d", "position", "number", 
                   "assign", "comment" ]

    EOF = Token.EOF
    Num_of_dim=1
    Num_of_peaks=2
    Format=3
    Iname=4
    Cyana_format=5
    Spectrum=6
    Tolerance=7
    Integer=8
    Float=9
    Real=10
    COMMENT=11
    EXCLM_COMMENT=12
    SMCLN_COMMENT=13
    Simple_name=14
    SPACE=15
    RETURN=16
    ENCLOSE_COMMENT=17
    SECTION_COMMENT=18
    LINE_COMMENT=19
    Integer_ND=20
    SPACE_ND=21
    RETURN_ND=22
    Integer_NP=23
    SPACE_NP=24
    RETURN_NP=25
    Simple_name_FO=26
    SPACE_FO=27
    RETURN_FO=28
    Integer_IN=29
    Simple_name_IN=30
    SPACE_IN=31
    RETURN_IN=32
    Simple_name_CY=33
    SPACE_CY=34
    RETURN_CY=35
    Simple_name_SP=36
    SPACE_SP=37
    RETURN_SP=38
    Float_TO=39
    TOACE_TO=40
    RETURN_TO=41
    Any_name=42
    SPACE_CM=43
    RETURN_CM=44

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Xeasy_pkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(XeasyPKParser.EOF, 0)

        def RETURN(self, i:int=None):
            if i is None:
                return self.getTokens(XeasyPKParser.RETURN)
            else:
                return self.getToken(XeasyPKParser.RETURN, i)

        def dimension(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.DimensionContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.DimensionContext,i)


        def peak(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.PeakContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.PeakContext,i)


        def format_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.FormatContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.FormatContext,i)


        def iname(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.InameContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.InameContext,i)


        def cyana_format(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.Cyana_formatContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.Cyana_formatContext,i)


        def spectrum(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.SpectrumContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.SpectrumContext,i)


        def tolerance(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.ToleranceContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.ToleranceContext,i)


        def peak_list_2d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.Peak_list_2dContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.Peak_list_2dContext,i)


        def peak_list_3d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.Peak_list_3dContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.Peak_list_3dContext,i)


        def peak_list_4d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.Peak_list_4dContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.Peak_list_4dContext,i)


        def comment(self):
            return self.getTypedRuleContext(XeasyPKParser.CommentContext,0)


        def getRuleIndex(self):
            return XeasyPKParser.RULE_xeasy_pk

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXeasy_pk" ):
                listener.enterXeasy_pk(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXeasy_pk" ):
                listener.exitXeasy_pk(self)




    def xeasy_pk(self):

        localctx = XeasyPKParser.Xeasy_pkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_xeasy_pk)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 36
                self.match(XeasyPKParser.RETURN)


            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 50
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        self.state = 39
                        self.dimension()
                        pass

                    elif la_ == 2:
                        self.state = 40
                        self.peak()
                        pass

                    elif la_ == 3:
                        self.state = 41
                        self.format_()
                        pass

                    elif la_ == 4:
                        self.state = 42
                        self.iname()
                        pass

                    elif la_ == 5:
                        self.state = 43
                        self.cyana_format()
                        pass

                    elif la_ == 6:
                        self.state = 44
                        self.spectrum()
                        pass

                    elif la_ == 7:
                        self.state = 45
                        self.tolerance()
                        pass

                    elif la_ == 8:
                        self.state = 46
                        self.peak_list_2d()
                        pass

                    elif la_ == 9:
                        self.state = 47
                        self.peak_list_3d()
                        pass

                    elif la_ == 10:
                        self.state = 48
                        self.peak_list_4d()
                        pass

                    elif la_ == 11:
                        self.state = 49
                        self.match(XeasyPKParser.RETURN)
                        pass

             
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.state = 55
                self.match(XeasyPKParser.RETURN)
                pass
            elif token in [11]:
                self.state = 56
                self.comment()
                pass
            elif token in [-1]:
                pass
            else:
                pass
            self.state = 59
            self.match(XeasyPKParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Num_of_dim(self):
            return self.getToken(XeasyPKParser.Num_of_dim, 0)

        def Integer_ND(self):
            return self.getToken(XeasyPKParser.Integer_ND, 0)

        def RETURN_ND(self):
            return self.getToken(XeasyPKParser.RETURN_ND, 0)

        def getRuleIndex(self):
            return XeasyPKParser.RULE_dimension

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDimension" ):
                listener.enterDimension(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDimension" ):
                listener.exitDimension(self)




    def dimension(self):

        localctx = XeasyPKParser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_dimension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(XeasyPKParser.Num_of_dim)
            self.state = 62
            self.match(XeasyPKParser.Integer_ND)
            self.state = 63
            self.match(XeasyPKParser.RETURN_ND)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PeakContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Num_of_peaks(self):
            return self.getToken(XeasyPKParser.Num_of_peaks, 0)

        def Integer_NP(self):
            return self.getToken(XeasyPKParser.Integer_NP, 0)

        def RETURN_NP(self):
            return self.getToken(XeasyPKParser.RETURN_NP, 0)

        def getRuleIndex(self):
            return XeasyPKParser.RULE_peak

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak" ):
                listener.enterPeak(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak" ):
                listener.exitPeak(self)




    def peak(self):

        localctx = XeasyPKParser.PeakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_peak)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(XeasyPKParser.Num_of_peaks)
            self.state = 66
            self.match(XeasyPKParser.Integer_NP)
            self.state = 67
            self.match(XeasyPKParser.RETURN_NP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Format(self):
            return self.getToken(XeasyPKParser.Format, 0)

        def RETURN_FO(self):
            return self.getToken(XeasyPKParser.RETURN_FO, 0)

        def Simple_name_FO(self, i:int=None):
            if i is None:
                return self.getTokens(XeasyPKParser.Simple_name_FO)
            else:
                return self.getToken(XeasyPKParser.Simple_name_FO, i)

        def getRuleIndex(self):
            return XeasyPKParser.RULE_format

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormat" ):
                listener.enterFormat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormat" ):
                listener.exitFormat(self)




    def format_(self):

        localctx = XeasyPKParser.FormatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_format)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(XeasyPKParser.Format)
            self.state = 71 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 70
                self.match(XeasyPKParser.Simple_name_FO)
                self.state = 73 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==26):
                    break

            self.state = 75
            self.match(XeasyPKParser.RETURN_FO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Iname(self):
            return self.getToken(XeasyPKParser.Iname, 0)

        def Integer_IN(self):
            return self.getToken(XeasyPKParser.Integer_IN, 0)

        def Simple_name_IN(self):
            return self.getToken(XeasyPKParser.Simple_name_IN, 0)

        def RETURN_IN(self):
            return self.getToken(XeasyPKParser.RETURN_IN, 0)

        def getRuleIndex(self):
            return XeasyPKParser.RULE_iname

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIname" ):
                listener.enterIname(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIname" ):
                listener.exitIname(self)




    def iname(self):

        localctx = XeasyPKParser.InameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_iname)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(XeasyPKParser.Iname)
            self.state = 78
            self.match(XeasyPKParser.Integer_IN)
            self.state = 79
            self.match(XeasyPKParser.Simple_name_IN)
            self.state = 80
            self.match(XeasyPKParser.RETURN_IN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cyana_formatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Cyana_format(self):
            return self.getToken(XeasyPKParser.Cyana_format, 0)

        def Simple_name_CY(self):
            return self.getToken(XeasyPKParser.Simple_name_CY, 0)

        def RETURN_CY(self):
            return self.getToken(XeasyPKParser.RETURN_CY, 0)

        def getRuleIndex(self):
            return XeasyPKParser.RULE_cyana_format

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCyana_format" ):
                listener.enterCyana_format(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCyana_format" ):
                listener.exitCyana_format(self)




    def cyana_format(self):

        localctx = XeasyPKParser.Cyana_formatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_cyana_format)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(XeasyPKParser.Cyana_format)
            self.state = 83
            self.match(XeasyPKParser.Simple_name_CY)
            self.state = 84
            self.match(XeasyPKParser.RETURN_CY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpectrumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Spectrum(self):
            return self.getToken(XeasyPKParser.Spectrum, 0)

        def RETURN_SP(self):
            return self.getToken(XeasyPKParser.RETURN_SP, 0)

        def Simple_name_SP(self, i:int=None):
            if i is None:
                return self.getTokens(XeasyPKParser.Simple_name_SP)
            else:
                return self.getToken(XeasyPKParser.Simple_name_SP, i)

        def getRuleIndex(self):
            return XeasyPKParser.RULE_spectrum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpectrum" ):
                listener.enterSpectrum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpectrum" ):
                listener.exitSpectrum(self)




    def spectrum(self):

        localctx = XeasyPKParser.SpectrumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_spectrum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(XeasyPKParser.Spectrum)
            self.state = 88 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 87
                self.match(XeasyPKParser.Simple_name_SP)
                self.state = 90 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==36):
                    break

            self.state = 92
            self.match(XeasyPKParser.RETURN_SP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ToleranceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Tolerance(self):
            return self.getToken(XeasyPKParser.Tolerance, 0)

        def RETURN_TO(self):
            return self.getToken(XeasyPKParser.RETURN_TO, 0)

        def Float_TO(self, i:int=None):
            if i is None:
                return self.getTokens(XeasyPKParser.Float_TO)
            else:
                return self.getToken(XeasyPKParser.Float_TO, i)

        def getRuleIndex(self):
            return XeasyPKParser.RULE_tolerance

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTolerance" ):
                listener.enterTolerance(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTolerance" ):
                listener.exitTolerance(self)




    def tolerance(self):

        localctx = XeasyPKParser.ToleranceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_tolerance)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(XeasyPKParser.Tolerance)
            self.state = 96 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 95
                self.match(XeasyPKParser.Float_TO)
                self.state = 98 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==39):
                    break

            self.state = 100
            self.match(XeasyPKParser.RETURN_TO)
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

        def peak_2d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.Peak_2dContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.Peak_2dContext,i)


        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.CommentContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.CommentContext,i)


        def getRuleIndex(self):
            return XeasyPKParser.RULE_peak_list_2d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_list_2d" ):
                listener.enterPeak_list_2d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_list_2d" ):
                listener.exitPeak_list_2d(self)




    def peak_list_2d(self):

        localctx = XeasyPKParser.Peak_list_2dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_peak_list_2d)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 104
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [8]:
                        self.state = 102
                        self.peak_2d()
                        pass
                    elif token in [11]:
                        self.state = 103
                        self.comment()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 106 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
                return self.getTokens(XeasyPKParser.Integer)
            else:
                return self.getToken(XeasyPKParser.Integer, i)

        def position(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.PositionContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.PositionContext,i)


        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.NumberContext,i)


        def assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.AssignContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.AssignContext,i)


        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(XeasyPKParser.Simple_name)
            else:
                return self.getToken(XeasyPKParser.Simple_name, i)

        def RETURN(self, i:int=None):
            if i is None:
                return self.getTokens(XeasyPKParser.RETURN)
            else:
                return self.getToken(XeasyPKParser.RETURN, i)

        def EOF(self, i:int=None):
            if i is None:
                return self.getTokens(XeasyPKParser.EOF)
            else:
                return self.getToken(XeasyPKParser.EOF, i)

        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.CommentContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.CommentContext,i)


        def getRuleIndex(self):
            return XeasyPKParser.RULE_peak_2d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_2d" ):
                listener.enterPeak_2d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_2d" ):
                listener.exitPeak_2d(self)




    def peak_2d(self):

        localctx = XeasyPKParser.Peak_2dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_peak_2d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(XeasyPKParser.Integer)
            self.state = 109
            self.position()
            self.state = 110
            self.position()
            self.state = 111
            self.match(XeasyPKParser.Integer)
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 112
                self.match(XeasyPKParser.Simple_name)


            self.state = 115
            self.number()
            self.state = 116
            self.number()
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 117
                self.match(XeasyPKParser.Simple_name)


            self.state = 120
            self.match(XeasyPKParser.Integer)
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1, 16]:
                self.state = 121
                _la = self._input.LA(1)
                if not(_la==-1 or _la==16):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [8, 14]:
                self.state = 122
                self.assign()
                self.state = 123
                self.assign()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==8:
                    self.state = 124
                    self.match(XeasyPKParser.Integer)


                self.state = 130
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [16]:
                    self.state = 127
                    self.match(XeasyPKParser.RETURN)
                    pass
                elif token in [11]:
                    self.state = 128
                    self.comment()
                    pass
                elif token in [-1]:
                    self.state = 129
                    self.match(XeasyPKParser.EOF)
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 146
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 134
                    self.assign()
                    self.state = 135
                    self.assign()
                    self.state = 137
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==8:
                        self.state = 136
                        self.match(XeasyPKParser.Integer)


                    self.state = 142
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [16]:
                        self.state = 139
                        self.match(XeasyPKParser.RETURN)
                        pass
                    elif token in [11]:
                        self.state = 140
                        self.comment()
                        pass
                    elif token in [-1]:
                        self.state = 141
                        self.match(XeasyPKParser.EOF)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 148
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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

        def peak_3d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.Peak_3dContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.Peak_3dContext,i)


        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.CommentContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.CommentContext,i)


        def getRuleIndex(self):
            return XeasyPKParser.RULE_peak_list_3d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_list_3d" ):
                listener.enterPeak_list_3d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_list_3d" ):
                listener.exitPeak_list_3d(self)




    def peak_list_3d(self):

        localctx = XeasyPKParser.Peak_list_3dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_peak_list_3d)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 151
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [8]:
                        self.state = 149
                        self.peak_3d()
                        pass
                    elif token in [11]:
                        self.state = 150
                        self.comment()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 153 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
                return self.getTokens(XeasyPKParser.Integer)
            else:
                return self.getToken(XeasyPKParser.Integer, i)

        def position(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.PositionContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.PositionContext,i)


        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.NumberContext,i)


        def assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.AssignContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.AssignContext,i)


        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(XeasyPKParser.Simple_name)
            else:
                return self.getToken(XeasyPKParser.Simple_name, i)

        def RETURN(self, i:int=None):
            if i is None:
                return self.getTokens(XeasyPKParser.RETURN)
            else:
                return self.getToken(XeasyPKParser.RETURN, i)

        def EOF(self, i:int=None):
            if i is None:
                return self.getTokens(XeasyPKParser.EOF)
            else:
                return self.getToken(XeasyPKParser.EOF, i)

        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.CommentContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.CommentContext,i)


        def getRuleIndex(self):
            return XeasyPKParser.RULE_peak_3d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_3d" ):
                listener.enterPeak_3d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_3d" ):
                listener.exitPeak_3d(self)




    def peak_3d(self):

        localctx = XeasyPKParser.Peak_3dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_peak_3d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(XeasyPKParser.Integer)
            self.state = 156
            self.position()
            self.state = 157
            self.position()
            self.state = 158
            self.position()
            self.state = 159
            self.match(XeasyPKParser.Integer)
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 160
                self.match(XeasyPKParser.Simple_name)


            self.state = 163
            self.number()
            self.state = 164
            self.number()
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 165
                self.match(XeasyPKParser.Simple_name)


            self.state = 168
            self.match(XeasyPKParser.Integer)
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1, 16]:
                self.state = 169
                _la = self._input.LA(1)
                if not(_la==-1 or _la==16):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [8, 14]:
                self.state = 170
                self.assign()
                self.state = 171
                self.assign()
                self.state = 172
                self.assign()
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==8:
                    self.state = 173
                    self.match(XeasyPKParser.Integer)


                self.state = 179
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [16]:
                    self.state = 176
                    self.match(XeasyPKParser.RETURN)
                    pass
                elif token in [11]:
                    self.state = 177
                    self.comment()
                    pass
                elif token in [-1]:
                    self.state = 178
                    self.match(XeasyPKParser.EOF)
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 196
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 183
                    self.assign()
                    self.state = 184
                    self.assign()
                    self.state = 185
                    self.assign()
                    self.state = 187
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==8:
                        self.state = 186
                        self.match(XeasyPKParser.Integer)


                    self.state = 192
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [16]:
                        self.state = 189
                        self.match(XeasyPKParser.RETURN)
                        pass
                    elif token in [11]:
                        self.state = 190
                        self.comment()
                        pass
                    elif token in [-1]:
                        self.state = 191
                        self.match(XeasyPKParser.EOF)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 198
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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

        def peak_4d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.Peak_4dContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.Peak_4dContext,i)


        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.CommentContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.CommentContext,i)


        def getRuleIndex(self):
            return XeasyPKParser.RULE_peak_list_4d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_list_4d" ):
                listener.enterPeak_list_4d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_list_4d" ):
                listener.exitPeak_list_4d(self)




    def peak_list_4d(self):

        localctx = XeasyPKParser.Peak_list_4dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_peak_list_4d)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 201
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [8]:
                        self.state = 199
                        self.peak_4d()
                        pass
                    elif token in [11]:
                        self.state = 200
                        self.comment()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 203 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
                return self.getTokens(XeasyPKParser.Integer)
            else:
                return self.getToken(XeasyPKParser.Integer, i)

        def position(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.PositionContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.PositionContext,i)


        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.NumberContext,i)


        def assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.AssignContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.AssignContext,i)


        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(XeasyPKParser.Simple_name)
            else:
                return self.getToken(XeasyPKParser.Simple_name, i)

        def RETURN(self, i:int=None):
            if i is None:
                return self.getTokens(XeasyPKParser.RETURN)
            else:
                return self.getToken(XeasyPKParser.RETURN, i)

        def EOF(self, i:int=None):
            if i is None:
                return self.getTokens(XeasyPKParser.EOF)
            else:
                return self.getToken(XeasyPKParser.EOF, i)

        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.CommentContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.CommentContext,i)


        def getRuleIndex(self):
            return XeasyPKParser.RULE_peak_4d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_4d" ):
                listener.enterPeak_4d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_4d" ):
                listener.exitPeak_4d(self)




    def peak_4d(self):

        localctx = XeasyPKParser.Peak_4dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_peak_4d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(XeasyPKParser.Integer)
            self.state = 206
            self.position()
            self.state = 207
            self.position()
            self.state = 208
            self.position()
            self.state = 209
            self.position()
            self.state = 210
            self.match(XeasyPKParser.Integer)
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 211
                self.match(XeasyPKParser.Simple_name)


            self.state = 214
            self.number()
            self.state = 215
            self.number()
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 216
                self.match(XeasyPKParser.Simple_name)


            self.state = 219
            self.match(XeasyPKParser.Integer)
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1, 16]:
                self.state = 220
                _la = self._input.LA(1)
                if not(_la==-1 or _la==16):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [8, 14]:
                self.state = 221
                self.assign()
                self.state = 222
                self.assign()
                self.state = 223
                self.assign()
                self.state = 224
                self.assign()
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==8:
                    self.state = 225
                    self.match(XeasyPKParser.Integer)


                self.state = 231
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [16]:
                    self.state = 228
                    self.match(XeasyPKParser.RETURN)
                    pass
                elif token in [11]:
                    self.state = 229
                    self.comment()
                    pass
                elif token in [-1]:
                    self.state = 230
                    self.match(XeasyPKParser.EOF)
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 249
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 235
                    self.assign()
                    self.state = 236
                    self.assign()
                    self.state = 237
                    self.assign()
                    self.state = 238
                    self.assign()
                    self.state = 240
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==8:
                        self.state = 239
                        self.match(XeasyPKParser.Integer)


                    self.state = 245
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [16]:
                        self.state = 242
                        self.match(XeasyPKParser.RETURN)
                        pass
                    elif token in [11]:
                        self.state = 243
                        self.comment()
                        pass
                    elif token in [-1]:
                        self.state = 244
                        self.match(XeasyPKParser.EOF)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 251
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PositionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Float(self):
            return self.getToken(XeasyPKParser.Float, 0)

        def Integer(self):
            return self.getToken(XeasyPKParser.Integer, 0)

        def getRuleIndex(self):
            return XeasyPKParser.RULE_position

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPosition" ):
                listener.enterPosition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPosition" ):
                listener.exitPosition(self)




    def position(self):

        localctx = XeasyPKParser.PositionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_position)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
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
            return self.getToken(XeasyPKParser.Float, 0)

        def Real(self):
            return self.getToken(XeasyPKParser.Real, 0)

        def Integer(self):
            return self.getToken(XeasyPKParser.Integer, 0)

        def Simple_name(self):
            return self.getToken(XeasyPKParser.Simple_name, 0)

        def getRuleIndex(self):
            return XeasyPKParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = XeasyPKParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 18176) != 0)):
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


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self):
            return self.getToken(XeasyPKParser.Integer, 0)

        def Simple_name(self):
            return self.getToken(XeasyPKParser.Simple_name, 0)

        def getRuleIndex(self):
            return XeasyPKParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = XeasyPKParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assign)
        try:
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.match(XeasyPKParser.Integer)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.match(XeasyPKParser.Simple_name)
                self.state = 259
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                if la_ == 1:
                    self.state = 258
                    self.match(XeasyPKParser.Integer)


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


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(XeasyPKParser.COMMENT, 0)

        def RETURN_CM(self):
            return self.getToken(XeasyPKParser.RETURN_CM, 0)

        def EOF(self):
            return self.getToken(XeasyPKParser.EOF, 0)

        def Any_name(self, i:int=None):
            if i is None:
                return self.getTokens(XeasyPKParser.Any_name)
            else:
                return self.getToken(XeasyPKParser.Any_name, i)

        def getRuleIndex(self):
            return XeasyPKParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = XeasyPKParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(XeasyPKParser.COMMENT)
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 264
                self.match(XeasyPKParser.Any_name)
                self.state = 269
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 270
            _la = self._input.LA(1)
            if not(_la==-1 or _la==44):
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





