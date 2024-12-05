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
        4,1,36,176,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,40,8,0,10,0,12,
        0,43,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,5,1,5,4,5,66,8,5,11,5,12,5,67,1,5,1,5,1,6,
        1,6,4,6,74,8,6,11,6,12,6,75,1,6,1,6,1,7,4,7,81,8,7,11,7,12,7,82,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        5,8,101,8,8,10,8,12,8,104,9,8,1,9,4,9,107,8,9,11,9,12,9,108,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,5,10,130,8,10,10,10,12,10,133,9,10,1,11,
        4,11,136,8,11,11,11,12,11,137,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,5,12,162,8,12,10,12,12,12,165,9,12,1,13,1,13,1,14,1,14,
        1,14,3,14,172,8,14,3,14,174,8,14,1,14,0,0,15,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,0,1,2,0,7,9,12,12,179,0,41,1,0,0,0,2,46,1,0,
        0,0,4,50,1,0,0,0,6,54,1,0,0,0,8,59,1,0,0,0,10,63,1,0,0,0,12,71,1,
        0,0,0,14,80,1,0,0,0,16,84,1,0,0,0,18,106,1,0,0,0,20,110,1,0,0,0,
        22,135,1,0,0,0,24,139,1,0,0,0,26,166,1,0,0,0,28,173,1,0,0,0,30,40,
        3,2,1,0,31,40,3,4,2,0,32,40,3,6,3,0,33,40,3,8,4,0,34,40,3,10,5,0,
        35,40,3,12,6,0,36,40,3,14,7,0,37,40,3,18,9,0,38,40,3,22,11,0,39,
        30,1,0,0,0,39,31,1,0,0,0,39,32,1,0,0,0,39,33,1,0,0,0,39,34,1,0,0,
        0,39,35,1,0,0,0,39,36,1,0,0,0,39,37,1,0,0,0,39,38,1,0,0,0,40,43,
        1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,44,1,0,0,0,43,41,1,0,0,0,
        44,45,5,0,0,1,45,1,1,0,0,0,46,47,5,1,0,0,47,48,5,18,0,0,48,49,5,
        20,0,0,49,3,1,0,0,0,50,51,5,2,0,0,51,52,5,21,0,0,52,53,5,23,0,0,
        53,5,1,0,0,0,54,55,5,3,0,0,55,56,5,24,0,0,56,57,5,25,0,0,57,58,5,
        27,0,0,58,7,1,0,0,0,59,60,5,4,0,0,60,61,5,28,0,0,61,62,5,30,0,0,
        62,9,1,0,0,0,63,65,5,5,0,0,64,66,5,31,0,0,65,64,1,0,0,0,66,67,1,
        0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,69,1,0,0,0,69,70,5,33,0,0,70,
        11,1,0,0,0,71,73,5,6,0,0,72,74,5,34,0,0,73,72,1,0,0,0,74,75,1,0,
        0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,77,1,0,0,0,77,78,5,36,0,0,78,
        13,1,0,0,0,79,81,3,16,8,0,80,79,1,0,0,0,81,82,1,0,0,0,82,80,1,0,
        0,0,82,83,1,0,0,0,83,15,1,0,0,0,84,85,5,7,0,0,85,86,5,8,0,0,86,87,
        5,8,0,0,87,88,5,7,0,0,88,89,5,12,0,0,89,90,3,26,13,0,90,91,3,26,
        13,0,91,92,5,12,0,0,92,93,5,7,0,0,93,94,3,28,14,0,94,95,3,28,14,
        0,95,102,5,14,0,0,96,97,3,28,14,0,97,98,3,28,14,0,98,99,5,14,0,0,
        99,101,1,0,0,0,100,96,1,0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,102,
        103,1,0,0,0,103,17,1,0,0,0,104,102,1,0,0,0,105,107,3,20,10,0,106,
        105,1,0,0,0,107,108,1,0,0,0,108,106,1,0,0,0,108,109,1,0,0,0,109,
        19,1,0,0,0,110,111,5,7,0,0,111,112,5,8,0,0,112,113,5,8,0,0,113,114,
        5,8,0,0,114,115,5,7,0,0,115,116,5,12,0,0,116,117,3,26,13,0,117,118,
        3,26,13,0,118,119,5,12,0,0,119,120,5,7,0,0,120,121,3,28,14,0,121,
        122,3,28,14,0,122,123,3,28,14,0,123,131,5,14,0,0,124,125,3,28,14,
        0,125,126,3,28,14,0,126,127,3,28,14,0,127,128,5,14,0,0,128,130,1,
        0,0,0,129,124,1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,132,1,
        0,0,0,132,21,1,0,0,0,133,131,1,0,0,0,134,136,3,24,12,0,135,134,1,
        0,0,0,136,137,1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,23,1,0,
        0,0,139,140,5,7,0,0,140,141,5,8,0,0,141,142,5,8,0,0,142,143,5,8,
        0,0,143,144,5,8,0,0,144,145,5,7,0,0,145,146,5,12,0,0,146,147,3,26,
        13,0,147,148,3,26,13,0,148,149,5,12,0,0,149,150,5,7,0,0,150,151,
        3,28,14,0,151,152,3,28,14,0,152,153,3,28,14,0,153,154,3,28,14,0,
        154,163,5,14,0,0,155,156,3,28,14,0,156,157,3,28,14,0,157,158,3,28,
        14,0,158,159,3,28,14,0,159,160,5,14,0,0,160,162,1,0,0,0,161,155,
        1,0,0,0,162,165,1,0,0,0,163,161,1,0,0,0,163,164,1,0,0,0,164,25,1,
        0,0,0,165,163,1,0,0,0,166,167,7,0,0,0,167,27,1,0,0,0,168,174,5,7,
        0,0,169,171,5,12,0,0,170,172,5,7,0,0,171,170,1,0,0,0,171,172,1,0,
        0,0,172,174,1,0,0,0,173,168,1,0,0,0,173,169,1,0,0,0,174,29,1,0,0,
        0,12,39,41,67,75,82,102,108,131,137,163,171,173
    ]

class XeasyPKParser ( Parser ):

    grammarFileName = "XeasyPKParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'#FORMAT'", "'#INAME'", 
                     "'#CYANAFORMAT'", "'#SPECTRUM'", "'#TOLERANCE'" ]

    symbolicNames = [ "<INVALID>", "Num_of_dim", "Format", "Iname", "Cyana_format", 
                      "Spectrum", "Tolerance", "Integer", "Float", "Real", 
                      "EXCLM_COMMENT", "SMCLN_COMMENT", "Simple_name", "SPACE", 
                      "RETURN", "ENCLOSE_COMMENT", "SECTION_COMMENT", "LINE_COMMENT", 
                      "Integer_ND", "SPACE_ND", "RETURN_ND", "Simple_name_FO", 
                      "SPACE_FO", "RETURN_FO", "Integer_IN", "Simple_name_IN", 
                      "SPACE_IN", "RETURN_IN", "Simple_name_CY", "SPACE_CY", 
                      "RETURN_CY", "Simple_name_SP", "SPACE_SP", "RETURN_SP", 
                      "Float_TO", "TOACE_TO", "RETURN_TO" ]

    RULE_xeasy_pk = 0
    RULE_dimension = 1
    RULE_format = 2
    RULE_iname = 3
    RULE_cyana_format = 4
    RULE_spectrum = 5
    RULE_tolerance = 6
    RULE_peak_list_2d = 7
    RULE_peak_2d = 8
    RULE_peak_list_3d = 9
    RULE_peak_3d = 10
    RULE_peak_list_4d = 11
    RULE_peak_4d = 12
    RULE_number = 13
    RULE_assign = 14

    ruleNames =  [ "xeasy_pk", "dimension", "format", "iname", "cyana_format", 
                   "spectrum", "tolerance", "peak_list_2d", "peak_2d", "peak_list_3d", 
                   "peak_3d", "peak_list_4d", "peak_4d", "number", "assign" ]

    EOF = Token.EOF
    Num_of_dim=1
    Format=2
    Iname=3
    Cyana_format=4
    Spectrum=5
    Tolerance=6
    Integer=7
    Float=8
    Real=9
    EXCLM_COMMENT=10
    SMCLN_COMMENT=11
    Simple_name=12
    SPACE=13
    RETURN=14
    ENCLOSE_COMMENT=15
    SECTION_COMMENT=16
    LINE_COMMENT=17
    Integer_ND=18
    SPACE_ND=19
    RETURN_ND=20
    Simple_name_FO=21
    SPACE_FO=22
    RETURN_FO=23
    Integer_IN=24
    Simple_name_IN=25
    SPACE_IN=26
    RETURN_IN=27
    Simple_name_CY=28
    SPACE_CY=29
    RETURN_CY=30
    Simple_name_SP=31
    SPACE_SP=32
    RETURN_SP=33
    Float_TO=34
    TOACE_TO=35
    RETURN_TO=36

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

        def dimension(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XeasyPKParser.DimensionContext)
            else:
                return self.getTypedRuleContext(XeasyPKParser.DimensionContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 254) != 0):
                self.state = 39
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 30
                    self.dimension()
                    pass

                elif la_ == 2:
                    self.state = 31
                    self.format_()
                    pass

                elif la_ == 3:
                    self.state = 32
                    self.iname()
                    pass

                elif la_ == 4:
                    self.state = 33
                    self.cyana_format()
                    pass

                elif la_ == 5:
                    self.state = 34
                    self.spectrum()
                    pass

                elif la_ == 6:
                    self.state = 35
                    self.tolerance()
                    pass

                elif la_ == 7:
                    self.state = 36
                    self.peak_list_2d()
                    pass

                elif la_ == 8:
                    self.state = 37
                    self.peak_list_3d()
                    pass

                elif la_ == 9:
                    self.state = 38
                    self.peak_list_4d()
                    pass


                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
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
            self.state = 46
            self.match(XeasyPKParser.Num_of_dim)
            self.state = 47
            self.match(XeasyPKParser.Integer_ND)
            self.state = 48
            self.match(XeasyPKParser.RETURN_ND)
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

        def Simple_name_FO(self):
            return self.getToken(XeasyPKParser.Simple_name_FO, 0)

        def RETURN_FO(self):
            return self.getToken(XeasyPKParser.RETURN_FO, 0)

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
        self.enterRule(localctx, 4, self.RULE_format)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(XeasyPKParser.Format)
            self.state = 51
            self.match(XeasyPKParser.Simple_name_FO)
            self.state = 52
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
        self.enterRule(localctx, 6, self.RULE_iname)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(XeasyPKParser.Iname)
            self.state = 55
            self.match(XeasyPKParser.Integer_IN)
            self.state = 56
            self.match(XeasyPKParser.Simple_name_IN)
            self.state = 57
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
        self.enterRule(localctx, 8, self.RULE_cyana_format)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(XeasyPKParser.Cyana_format)
            self.state = 60
            self.match(XeasyPKParser.Simple_name_CY)
            self.state = 61
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
        self.enterRule(localctx, 10, self.RULE_spectrum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(XeasyPKParser.Spectrum)
            self.state = 65 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 64
                self.match(XeasyPKParser.Simple_name_SP)
                self.state = 67 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==31):
                    break

            self.state = 69
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
        self.enterRule(localctx, 12, self.RULE_tolerance)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(XeasyPKParser.Tolerance)
            self.state = 73 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 72
                self.match(XeasyPKParser.Float_TO)
                self.state = 75 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==34):
                    break

            self.state = 77
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
        self.enterRule(localctx, 14, self.RULE_peak_list_2d)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 79
                    self.peak_2d()

                else:
                    raise NoViableAltException(self)
                self.state = 82 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(XeasyPKParser.Float)
            else:
                return self.getToken(XeasyPKParser.Float, i)

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
        self.enterRule(localctx, 16, self.RULE_peak_2d)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(XeasyPKParser.Integer)
            self.state = 85
            self.match(XeasyPKParser.Float)
            self.state = 86
            self.match(XeasyPKParser.Float)
            self.state = 87
            self.match(XeasyPKParser.Integer)
            self.state = 88
            self.match(XeasyPKParser.Simple_name)
            self.state = 89
            self.number()
            self.state = 90
            self.number()
            self.state = 91
            self.match(XeasyPKParser.Simple_name)
            self.state = 92
            self.match(XeasyPKParser.Integer)
            self.state = 93
            self.assign()
            self.state = 94
            self.assign()
            self.state = 95
            self.match(XeasyPKParser.RETURN)
            self.state = 102
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 96
                    self.assign()
                    self.state = 97
                    self.assign()
                    self.state = 98
                    self.match(XeasyPKParser.RETURN) 
                self.state = 104
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
        self.enterRule(localctx, 18, self.RULE_peak_list_3d)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 105
                    self.peak_3d()

                else:
                    raise NoViableAltException(self)
                self.state = 108 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(XeasyPKParser.Float)
            else:
                return self.getToken(XeasyPKParser.Float, i)

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
        self.enterRule(localctx, 20, self.RULE_peak_3d)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(XeasyPKParser.Integer)
            self.state = 111
            self.match(XeasyPKParser.Float)
            self.state = 112
            self.match(XeasyPKParser.Float)
            self.state = 113
            self.match(XeasyPKParser.Float)
            self.state = 114
            self.match(XeasyPKParser.Integer)
            self.state = 115
            self.match(XeasyPKParser.Simple_name)
            self.state = 116
            self.number()
            self.state = 117
            self.number()
            self.state = 118
            self.match(XeasyPKParser.Simple_name)
            self.state = 119
            self.match(XeasyPKParser.Integer)
            self.state = 120
            self.assign()
            self.state = 121
            self.assign()
            self.state = 122
            self.assign()
            self.state = 123
            self.match(XeasyPKParser.RETURN)
            self.state = 131
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 124
                    self.assign()
                    self.state = 125
                    self.assign()
                    self.state = 126
                    self.assign()
                    self.state = 127
                    self.match(XeasyPKParser.RETURN) 
                self.state = 133
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
        self.enterRule(localctx, 22, self.RULE_peak_list_4d)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 134
                    self.peak_4d()

                else:
                    raise NoViableAltException(self)
                self.state = 137 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(XeasyPKParser.Float)
            else:
                return self.getToken(XeasyPKParser.Float, i)

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
        self.enterRule(localctx, 24, self.RULE_peak_4d)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(XeasyPKParser.Integer)
            self.state = 140
            self.match(XeasyPKParser.Float)
            self.state = 141
            self.match(XeasyPKParser.Float)
            self.state = 142
            self.match(XeasyPKParser.Float)
            self.state = 143
            self.match(XeasyPKParser.Float)
            self.state = 144
            self.match(XeasyPKParser.Integer)
            self.state = 145
            self.match(XeasyPKParser.Simple_name)
            self.state = 146
            self.number()
            self.state = 147
            self.number()
            self.state = 148
            self.match(XeasyPKParser.Simple_name)
            self.state = 149
            self.match(XeasyPKParser.Integer)
            self.state = 150
            self.assign()
            self.state = 151
            self.assign()
            self.state = 152
            self.assign()
            self.state = 153
            self.assign()
            self.state = 154
            self.match(XeasyPKParser.RETURN)
            self.state = 163
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 155
                    self.assign()
                    self.state = 156
                    self.assign()
                    self.state = 157
                    self.assign()
                    self.state = 158
                    self.assign()
                    self.state = 159
                    self.match(XeasyPKParser.RETURN) 
                self.state = 165
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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
        self.enterRule(localctx, 26, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4992) != 0)):
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
        self.enterRule(localctx, 28, self.RULE_assign)
        try:
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.match(XeasyPKParser.Integer)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.match(XeasyPKParser.Simple_name)
                self.state = 171
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 170
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





