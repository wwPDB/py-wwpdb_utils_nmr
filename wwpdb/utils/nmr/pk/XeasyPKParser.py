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
        4,1,44,251,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,3,0,38,8,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,50,8,0,10,0,12,0,53,9,0,1,0,1,
        0,3,0,57,8,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,4,3,
        71,8,3,11,3,12,3,72,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,
        1,6,1,6,4,6,88,8,6,11,6,12,6,89,1,6,1,6,1,7,1,7,4,7,96,8,7,11,7,
        12,7,97,1,7,1,7,1,8,1,8,4,8,104,8,8,11,8,12,8,105,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,120,8,9,1,9,1,9,1,9,3,9,125,
        8,9,1,9,1,9,1,9,3,9,130,8,9,1,9,1,9,1,9,3,9,135,8,9,5,9,137,8,9,
        10,9,12,9,140,9,9,1,10,1,10,4,10,144,8,10,11,10,12,10,145,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,
        11,162,8,11,1,11,1,11,1,11,3,11,167,8,11,1,11,1,11,1,11,1,11,3,11,
        173,8,11,1,11,1,11,1,11,3,11,178,8,11,5,11,180,8,11,10,11,12,11,
        183,9,11,1,12,1,12,4,12,187,8,12,11,12,12,12,188,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        3,13,207,8,13,1,13,1,13,1,13,3,13,212,8,13,1,13,1,13,1,13,1,13,1,
        13,3,13,219,8,13,1,13,1,13,1,13,3,13,224,8,13,5,13,226,8,13,10,13,
        12,13,229,9,13,1,14,1,14,1,15,1,15,1,16,1,16,1,16,3,16,238,8,16,
        3,16,240,8,16,1,17,1,17,5,17,244,8,17,10,17,12,17,247,9,17,1,17,
        1,17,1,17,0,0,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        0,3,1,0,8,9,2,0,8,10,14,14,1,1,44,44,278,0,37,1,0,0,0,2,60,1,0,0,
        0,4,64,1,0,0,0,6,68,1,0,0,0,8,76,1,0,0,0,10,81,1,0,0,0,12,85,1,0,
        0,0,14,93,1,0,0,0,16,103,1,0,0,0,18,107,1,0,0,0,20,143,1,0,0,0,22,
        147,1,0,0,0,24,186,1,0,0,0,26,190,1,0,0,0,28,230,1,0,0,0,30,232,
        1,0,0,0,32,239,1,0,0,0,34,241,1,0,0,0,36,38,5,16,0,0,37,36,1,0,0,
        0,37,38,1,0,0,0,38,51,1,0,0,0,39,50,3,2,1,0,40,50,3,4,2,0,41,50,
        3,6,3,0,42,50,3,8,4,0,43,50,3,10,5,0,44,50,3,12,6,0,45,50,3,14,7,
        0,46,50,3,16,8,0,47,50,3,20,10,0,48,50,3,24,12,0,49,39,1,0,0,0,49,
        40,1,0,0,0,49,41,1,0,0,0,49,42,1,0,0,0,49,43,1,0,0,0,49,44,1,0,0,
        0,49,45,1,0,0,0,49,46,1,0,0,0,49,47,1,0,0,0,49,48,1,0,0,0,50,53,
        1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,56,1,0,0,0,53,51,1,0,0,0,
        54,57,5,16,0,0,55,57,3,34,17,0,56,54,1,0,0,0,56,55,1,0,0,0,56,57,
        1,0,0,0,57,58,1,0,0,0,58,59,5,0,0,1,59,1,1,0,0,0,60,61,5,1,0,0,61,
        62,5,20,0,0,62,63,5,22,0,0,63,3,1,0,0,0,64,65,5,2,0,0,65,66,5,23,
        0,0,66,67,5,25,0,0,67,5,1,0,0,0,68,70,5,3,0,0,69,71,5,26,0,0,70,
        69,1,0,0,0,71,72,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,74,1,0,0,
        0,74,75,5,28,0,0,75,7,1,0,0,0,76,77,5,4,0,0,77,78,5,29,0,0,78,79,
        5,30,0,0,79,80,5,32,0,0,80,9,1,0,0,0,81,82,5,5,0,0,82,83,5,33,0,
        0,83,84,5,35,0,0,84,11,1,0,0,0,85,87,5,6,0,0,86,88,5,36,0,0,87,86,
        1,0,0,0,88,89,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,91,1,0,0,0,
        91,92,5,38,0,0,92,13,1,0,0,0,93,95,5,7,0,0,94,96,5,39,0,0,95,94,
        1,0,0,0,96,97,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,99,1,0,0,0,
        99,100,5,41,0,0,100,15,1,0,0,0,101,104,3,18,9,0,102,104,3,34,17,
        0,103,101,1,0,0,0,103,102,1,0,0,0,104,105,1,0,0,0,105,103,1,0,0,
        0,105,106,1,0,0,0,106,17,1,0,0,0,107,108,5,8,0,0,108,109,3,28,14,
        0,109,110,3,28,14,0,110,111,5,8,0,0,111,112,5,14,0,0,112,113,3,30,
        15,0,113,114,3,30,15,0,114,115,5,14,0,0,115,116,5,8,0,0,116,117,
        3,32,16,0,117,119,3,32,16,0,118,120,5,8,0,0,119,118,1,0,0,0,119,
        120,1,0,0,0,120,124,1,0,0,0,121,125,5,16,0,0,122,125,3,34,17,0,123,
        125,5,0,0,1,124,121,1,0,0,0,124,122,1,0,0,0,124,123,1,0,0,0,125,
        138,1,0,0,0,126,127,3,32,16,0,127,129,3,32,16,0,128,130,5,8,0,0,
        129,128,1,0,0,0,129,130,1,0,0,0,130,134,1,0,0,0,131,135,5,16,0,0,
        132,135,3,34,17,0,133,135,5,0,0,1,134,131,1,0,0,0,134,132,1,0,0,
        0,134,133,1,0,0,0,135,137,1,0,0,0,136,126,1,0,0,0,137,140,1,0,0,
        0,138,136,1,0,0,0,138,139,1,0,0,0,139,19,1,0,0,0,140,138,1,0,0,0,
        141,144,3,22,11,0,142,144,3,34,17,0,143,141,1,0,0,0,143,142,1,0,
        0,0,144,145,1,0,0,0,145,143,1,0,0,0,145,146,1,0,0,0,146,21,1,0,0,
        0,147,148,5,8,0,0,148,149,3,28,14,0,149,150,3,28,14,0,150,151,3,
        28,14,0,151,152,5,8,0,0,152,153,5,14,0,0,153,154,3,30,15,0,154,155,
        3,30,15,0,155,156,5,14,0,0,156,157,5,8,0,0,157,158,3,32,16,0,158,
        159,3,32,16,0,159,161,3,32,16,0,160,162,5,8,0,0,161,160,1,0,0,0,
        161,162,1,0,0,0,162,166,1,0,0,0,163,167,5,16,0,0,164,167,3,34,17,
        0,165,167,5,0,0,1,166,163,1,0,0,0,166,164,1,0,0,0,166,165,1,0,0,
        0,167,181,1,0,0,0,168,169,3,32,16,0,169,170,3,32,16,0,170,172,3,
        32,16,0,171,173,5,8,0,0,172,171,1,0,0,0,172,173,1,0,0,0,173,177,
        1,0,0,0,174,178,5,16,0,0,175,178,3,34,17,0,176,178,5,0,0,1,177,174,
        1,0,0,0,177,175,1,0,0,0,177,176,1,0,0,0,178,180,1,0,0,0,179,168,
        1,0,0,0,180,183,1,0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,23,1,
        0,0,0,183,181,1,0,0,0,184,187,3,26,13,0,185,187,3,34,17,0,186,184,
        1,0,0,0,186,185,1,0,0,0,187,188,1,0,0,0,188,186,1,0,0,0,188,189,
        1,0,0,0,189,25,1,0,0,0,190,191,5,8,0,0,191,192,3,28,14,0,192,193,
        3,28,14,0,193,194,3,28,14,0,194,195,3,28,14,0,195,196,5,8,0,0,196,
        197,5,14,0,0,197,198,3,30,15,0,198,199,3,30,15,0,199,200,5,14,0,
        0,200,201,5,8,0,0,201,202,3,32,16,0,202,203,3,32,16,0,203,204,3,
        32,16,0,204,206,3,32,16,0,205,207,5,8,0,0,206,205,1,0,0,0,206,207,
        1,0,0,0,207,211,1,0,0,0,208,212,5,16,0,0,209,212,3,34,17,0,210,212,
        5,0,0,1,211,208,1,0,0,0,211,209,1,0,0,0,211,210,1,0,0,0,212,227,
        1,0,0,0,213,214,3,32,16,0,214,215,3,32,16,0,215,216,3,32,16,0,216,
        218,3,32,16,0,217,219,5,8,0,0,218,217,1,0,0,0,218,219,1,0,0,0,219,
        223,1,0,0,0,220,224,5,16,0,0,221,224,3,34,17,0,222,224,5,0,0,1,223,
        220,1,0,0,0,223,221,1,0,0,0,223,222,1,0,0,0,224,226,1,0,0,0,225,
        213,1,0,0,0,226,229,1,0,0,0,227,225,1,0,0,0,227,228,1,0,0,0,228,
        27,1,0,0,0,229,227,1,0,0,0,230,231,7,0,0,0,231,29,1,0,0,0,232,233,
        7,1,0,0,233,31,1,0,0,0,234,240,5,8,0,0,235,237,5,14,0,0,236,238,
        5,8,0,0,237,236,1,0,0,0,237,238,1,0,0,0,238,240,1,0,0,0,239,234,
        1,0,0,0,239,235,1,0,0,0,240,33,1,0,0,0,241,245,5,11,0,0,242,244,
        5,42,0,0,243,242,1,0,0,0,244,247,1,0,0,0,245,243,1,0,0,0,245,246,
        1,0,0,0,246,248,1,0,0,0,247,245,1,0,0,0,248,249,7,2,0,0,249,35,1,
        0,0,0,31,37,49,51,56,72,89,97,103,105,119,124,129,134,138,143,145,
        161,166,172,177,181,186,188,206,211,218,223,227,237,239,245
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


            self.state = 51
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 49
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

             
                self.state = 53
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.state = 54
                self.match(XeasyPKParser.RETURN)
                pass
            elif token in [11]:
                self.state = 55
                self.comment()
                pass
            elif token in [-1]:
                pass
            else:
                pass
            self.state = 58
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
            self.state = 60
            self.match(XeasyPKParser.Num_of_dim)
            self.state = 61
            self.match(XeasyPKParser.Integer_ND)
            self.state = 62
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
            self.state = 64
            self.match(XeasyPKParser.Num_of_peaks)
            self.state = 65
            self.match(XeasyPKParser.Integer_NP)
            self.state = 66
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
            self.state = 68
            self.match(XeasyPKParser.Format)
            self.state = 70 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 69
                self.match(XeasyPKParser.Simple_name_FO)
                self.state = 72 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==26):
                    break

            self.state = 74
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
            self.state = 76
            self.match(XeasyPKParser.Iname)
            self.state = 77
            self.match(XeasyPKParser.Integer_IN)
            self.state = 78
            self.match(XeasyPKParser.Simple_name_IN)
            self.state = 79
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
            self.state = 81
            self.match(XeasyPKParser.Cyana_format)
            self.state = 82
            self.match(XeasyPKParser.Simple_name_CY)
            self.state = 83
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
            self.state = 85
            self.match(XeasyPKParser.Spectrum)
            self.state = 87 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 86
                self.match(XeasyPKParser.Simple_name_SP)
                self.state = 89 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==36):
                    break

            self.state = 91
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
            self.state = 93
            self.match(XeasyPKParser.Tolerance)
            self.state = 95 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 94
                self.match(XeasyPKParser.Float_TO)
                self.state = 97 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==39):
                    break

            self.state = 99
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
            self.state = 103 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 103
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [8]:
                        self.state = 101
                        self.peak_2d()
                        pass
                    elif token in [11]:
                        self.state = 102
                        self.comment()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 105 
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


        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(XeasyPKParser.Simple_name)
            else:
                return self.getToken(XeasyPKParser.Simple_name, i)

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


        def RETURN(self, i:int=None):
            if i is None:
                return self.getTokens(XeasyPKParser.RETURN)
            else:
                return self.getToken(XeasyPKParser.RETURN, i)

        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.CommentContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.CommentContext,i)


        def EOF(self, i:int=None):
            if i is None:
                return self.getTokens(XeasyPKParser.EOF)
            else:
                return self.getToken(XeasyPKParser.EOF, i)

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
            self.state = 107
            self.match(XeasyPKParser.Integer)
            self.state = 108
            self.position()
            self.state = 109
            self.position()
            self.state = 110
            self.match(XeasyPKParser.Integer)
            self.state = 111
            self.match(XeasyPKParser.Simple_name)
            self.state = 112
            self.number()
            self.state = 113
            self.number()
            self.state = 114
            self.match(XeasyPKParser.Simple_name)
            self.state = 115
            self.match(XeasyPKParser.Integer)
            self.state = 116
            self.assign()
            self.state = 117
            self.assign()
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 118
                self.match(XeasyPKParser.Integer)


            self.state = 124
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.state = 121
                self.match(XeasyPKParser.RETURN)
                pass
            elif token in [11]:
                self.state = 122
                self.comment()
                pass
            elif token in [-1]:
                self.state = 123
                self.match(XeasyPKParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 138
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 126
                    self.assign()
                    self.state = 127
                    self.assign()
                    self.state = 129
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==8:
                        self.state = 128
                        self.match(XeasyPKParser.Integer)


                    self.state = 134
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [16]:
                        self.state = 131
                        self.match(XeasyPKParser.RETURN)
                        pass
                    elif token in [11]:
                        self.state = 132
                        self.comment()
                        pass
                    elif token in [-1]:
                        self.state = 133
                        self.match(XeasyPKParser.EOF)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 140
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
            self.state = 143 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 143
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [8]:
                        self.state = 141
                        self.peak_3d()
                        pass
                    elif token in [11]:
                        self.state = 142
                        self.comment()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 145 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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


        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(XeasyPKParser.Simple_name)
            else:
                return self.getToken(XeasyPKParser.Simple_name, i)

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


        def RETURN(self, i:int=None):
            if i is None:
                return self.getTokens(XeasyPKParser.RETURN)
            else:
                return self.getToken(XeasyPKParser.RETURN, i)

        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.CommentContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.CommentContext,i)


        def EOF(self, i:int=None):
            if i is None:
                return self.getTokens(XeasyPKParser.EOF)
            else:
                return self.getToken(XeasyPKParser.EOF, i)

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
            self.state = 147
            self.match(XeasyPKParser.Integer)
            self.state = 148
            self.position()
            self.state = 149
            self.position()
            self.state = 150
            self.position()
            self.state = 151
            self.match(XeasyPKParser.Integer)
            self.state = 152
            self.match(XeasyPKParser.Simple_name)
            self.state = 153
            self.number()
            self.state = 154
            self.number()
            self.state = 155
            self.match(XeasyPKParser.Simple_name)
            self.state = 156
            self.match(XeasyPKParser.Integer)
            self.state = 157
            self.assign()
            self.state = 158
            self.assign()
            self.state = 159
            self.assign()
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 160
                self.match(XeasyPKParser.Integer)


            self.state = 166
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.state = 163
                self.match(XeasyPKParser.RETURN)
                pass
            elif token in [11]:
                self.state = 164
                self.comment()
                pass
            elif token in [-1]:
                self.state = 165
                self.match(XeasyPKParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 181
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 168
                    self.assign()
                    self.state = 169
                    self.assign()
                    self.state = 170
                    self.assign()
                    self.state = 172
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==8:
                        self.state = 171
                        self.match(XeasyPKParser.Integer)


                    self.state = 177
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [16]:
                        self.state = 174
                        self.match(XeasyPKParser.RETURN)
                        pass
                    elif token in [11]:
                        self.state = 175
                        self.comment()
                        pass
                    elif token in [-1]:
                        self.state = 176
                        self.match(XeasyPKParser.EOF)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 183
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
            self.state = 186 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 186
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [8]:
                        self.state = 184
                        self.peak_4d()
                        pass
                    elif token in [11]:
                        self.state = 185
                        self.comment()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 188 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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


        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(XeasyPKParser.Simple_name)
            else:
                return self.getToken(XeasyPKParser.Simple_name, i)

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


        def RETURN(self, i:int=None):
            if i is None:
                return self.getTokens(XeasyPKParser.RETURN)
            else:
                return self.getToken(XeasyPKParser.RETURN, i)

        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.CommentContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.CommentContext,i)


        def EOF(self, i:int=None):
            if i is None:
                return self.getTokens(XeasyPKParser.EOF)
            else:
                return self.getToken(XeasyPKParser.EOF, i)

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
            self.state = 190
            self.match(XeasyPKParser.Integer)
            self.state = 191
            self.position()
            self.state = 192
            self.position()
            self.state = 193
            self.position()
            self.state = 194
            self.position()
            self.state = 195
            self.match(XeasyPKParser.Integer)
            self.state = 196
            self.match(XeasyPKParser.Simple_name)
            self.state = 197
            self.number()
            self.state = 198
            self.number()
            self.state = 199
            self.match(XeasyPKParser.Simple_name)
            self.state = 200
            self.match(XeasyPKParser.Integer)
            self.state = 201
            self.assign()
            self.state = 202
            self.assign()
            self.state = 203
            self.assign()
            self.state = 204
            self.assign()
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 205
                self.match(XeasyPKParser.Integer)


            self.state = 211
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.state = 208
                self.match(XeasyPKParser.RETURN)
                pass
            elif token in [11]:
                self.state = 209
                self.comment()
                pass
            elif token in [-1]:
                self.state = 210
                self.match(XeasyPKParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 227
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 213
                    self.assign()
                    self.state = 214
                    self.assign()
                    self.state = 215
                    self.assign()
                    self.state = 216
                    self.assign()
                    self.state = 218
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==8:
                        self.state = 217
                        self.match(XeasyPKParser.Integer)


                    self.state = 223
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [16]:
                        self.state = 220
                        self.match(XeasyPKParser.RETURN)
                        pass
                    elif token in [11]:
                        self.state = 221
                        self.comment()
                        pass
                    elif token in [-1]:
                        self.state = 222
                        self.match(XeasyPKParser.EOF)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 229
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
            self.state = 230
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
            self.state = 232
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
            self.state = 239
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.match(XeasyPKParser.Integer)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.match(XeasyPKParser.Simple_name)
                self.state = 237
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                if la_ == 1:
                    self.state = 236
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
            self.state = 241
            self.match(XeasyPKParser.COMMENT)
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 242
                self.match(XeasyPKParser.Any_name)
                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 248
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





