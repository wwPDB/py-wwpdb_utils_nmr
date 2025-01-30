# Generated from VnmrPKParser.g4 by ANTLR 4.13.0
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
        4,1,52,237,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,3,0,24,8,0,1,0,1,0,1,0,1,
        0,4,0,30,8,0,11,0,12,0,31,1,0,4,0,35,8,0,11,0,12,0,36,1,0,4,0,40,
        8,0,11,0,12,0,41,1,0,5,0,45,8,0,10,0,12,0,48,9,0,1,0,1,0,1,1,1,1,
        5,1,54,8,1,10,1,12,1,57,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,3,2,66,8,
        2,1,2,3,2,69,8,2,1,2,1,2,3,2,73,8,2,1,2,3,2,76,8,2,1,2,3,2,79,8,
        2,1,2,3,2,82,8,2,1,2,3,2,85,8,2,1,2,3,2,88,8,2,1,2,1,2,4,2,92,8,
        2,11,2,12,2,93,1,2,4,2,97,8,2,11,2,12,2,98,1,2,4,2,102,8,2,11,2,
        12,2,103,3,2,106,8,2,1,3,1,3,1,3,1,3,1,3,3,3,113,8,3,1,3,3,3,116,
        8,3,1,3,3,3,119,8,3,1,3,3,3,122,8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,
        1,4,3,4,132,8,4,1,4,3,4,135,8,4,1,4,3,4,138,8,4,1,4,3,4,141,8,4,
        1,4,3,4,144,8,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,155,8,5,
        1,5,3,5,158,8,5,1,5,3,5,161,8,5,1,5,3,5,164,8,5,1,5,3,5,167,8,5,
        1,5,3,5,170,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,
        183,8,6,3,6,185,8,6,1,6,1,6,3,6,189,8,6,1,6,3,6,192,8,6,1,6,1,6,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,203,8,7,1,7,1,7,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,3,8,216,8,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,3,9,231,8,9,1,9,1,9,1,10,1,10,1,10,0,0,11,0,
        2,4,6,8,10,12,14,16,18,20,0,8,1,1,52,52,2,0,39,39,43,43,2,0,40,40,
        44,44,2,0,41,41,45,45,2,0,42,42,46,46,1,1,14,14,1,0,26,27,1,0,3,
        5,272,0,23,1,0,0,0,2,51,1,0,0,0,4,60,1,0,0,0,6,107,1,0,0,0,8,125,
        1,0,0,0,10,147,1,0,0,0,12,173,1,0,0,0,14,195,1,0,0,0,16,206,1,0,
        0,0,18,219,1,0,0,0,20,234,1,0,0,0,22,24,5,14,0,0,23,22,1,0,0,0,23,
        24,1,0,0,0,24,46,1,0,0,0,25,45,3,2,1,0,26,45,3,4,2,0,27,45,3,12,
        6,0,28,30,3,14,7,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,
        32,1,0,0,0,32,45,1,0,0,0,33,35,3,16,8,0,34,33,1,0,0,0,35,36,1,0,
        0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,45,1,0,0,0,38,40,3,18,9,0,39,
        38,1,0,0,0,40,41,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,45,1,0,0,
        0,43,45,5,14,0,0,44,25,1,0,0,0,44,26,1,0,0,0,44,27,1,0,0,0,44,29,
        1,0,0,0,44,34,1,0,0,0,44,39,1,0,0,0,44,43,1,0,0,0,45,48,1,0,0,0,
        46,44,1,0,0,0,46,47,1,0,0,0,47,49,1,0,0,0,48,46,1,0,0,0,49,50,5,
        0,0,1,50,1,1,0,0,0,51,55,5,6,0,0,52,54,5,50,0,0,53,52,1,0,0,0,54,
        57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,58,1,0,0,0,57,55,1,0,0,
        0,58,59,7,0,0,0,59,3,1,0,0,0,60,61,5,2,0,0,61,62,5,32,0,0,62,63,
        5,33,0,0,63,65,5,34,0,0,64,66,5,35,0,0,65,64,1,0,0,0,65,66,1,0,0,
        0,66,68,1,0,0,0,67,69,5,36,0,0,68,67,1,0,0,0,68,69,1,0,0,0,69,70,
        1,0,0,0,70,72,5,37,0,0,71,73,5,38,0,0,72,71,1,0,0,0,72,73,1,0,0,
        0,73,75,1,0,0,0,74,76,7,1,0,0,75,74,1,0,0,0,75,76,1,0,0,0,76,78,
        1,0,0,0,77,79,7,2,0,0,78,77,1,0,0,0,78,79,1,0,0,0,79,81,1,0,0,0,
        80,82,7,3,0,0,81,80,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,85,7,
        4,0,0,84,83,1,0,0,0,84,85,1,0,0,0,85,87,1,0,0,0,86,88,5,47,0,0,87,
        86,1,0,0,0,87,88,1,0,0,0,88,89,1,0,0,0,89,105,5,49,0,0,90,92,3,6,
        3,0,91,90,1,0,0,0,92,93,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,106,
        1,0,0,0,95,97,3,8,4,0,96,95,1,0,0,0,97,98,1,0,0,0,98,96,1,0,0,0,
        98,99,1,0,0,0,99,106,1,0,0,0,100,102,3,10,5,0,101,100,1,0,0,0,102,
        103,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,106,1,0,0,0,105,
        91,1,0,0,0,105,96,1,0,0,0,105,101,1,0,0,0,106,5,1,0,0,0,107,108,
        5,3,0,0,108,109,5,4,0,0,109,110,5,4,0,0,110,112,3,20,10,0,111,113,
        3,20,10,0,112,111,1,0,0,0,112,113,1,0,0,0,113,115,1,0,0,0,114,116,
        3,20,10,0,115,114,1,0,0,0,115,116,1,0,0,0,116,118,1,0,0,0,117,119,
        3,20,10,0,118,117,1,0,0,0,118,119,1,0,0,0,119,121,1,0,0,0,120,122,
        5,7,0,0,121,120,1,0,0,0,121,122,1,0,0,0,122,123,1,0,0,0,123,124,
        7,5,0,0,124,7,1,0,0,0,125,126,5,3,0,0,126,127,5,4,0,0,127,128,5,
        4,0,0,128,129,5,4,0,0,129,131,3,20,10,0,130,132,3,20,10,0,131,130,
        1,0,0,0,131,132,1,0,0,0,132,134,1,0,0,0,133,135,3,20,10,0,134,133,
        1,0,0,0,134,135,1,0,0,0,135,137,1,0,0,0,136,138,3,20,10,0,137,136,
        1,0,0,0,137,138,1,0,0,0,138,140,1,0,0,0,139,141,3,20,10,0,140,139,
        1,0,0,0,140,141,1,0,0,0,141,143,1,0,0,0,142,144,5,7,0,0,143,142,
        1,0,0,0,143,144,1,0,0,0,144,145,1,0,0,0,145,146,7,5,0,0,146,9,1,
        0,0,0,147,148,5,3,0,0,148,149,5,4,0,0,149,150,5,4,0,0,150,151,5,
        4,0,0,151,152,5,4,0,0,152,154,3,20,10,0,153,155,3,20,10,0,154,153,
        1,0,0,0,154,155,1,0,0,0,155,157,1,0,0,0,156,158,3,20,10,0,157,156,
        1,0,0,0,157,158,1,0,0,0,158,160,1,0,0,0,159,161,3,20,10,0,160,159,
        1,0,0,0,160,161,1,0,0,0,161,163,1,0,0,0,162,164,3,20,10,0,163,162,
        1,0,0,0,163,164,1,0,0,0,164,166,1,0,0,0,165,167,3,20,10,0,166,165,
        1,0,0,0,166,167,1,0,0,0,167,169,1,0,0,0,168,170,5,7,0,0,169,168,
        1,0,0,0,169,170,1,0,0,0,170,171,1,0,0,0,171,172,7,5,0,0,172,11,1,
        0,0,0,173,174,5,1,0,0,174,175,5,18,0,0,175,176,5,22,0,0,176,177,
        5,19,0,0,177,184,5,23,0,0,178,179,5,20,0,0,179,182,5,24,0,0,180,
        181,5,21,0,0,181,183,5,25,0,0,182,180,1,0,0,0,182,183,1,0,0,0,183,
        185,1,0,0,0,184,178,1,0,0,0,184,185,1,0,0,0,185,186,1,0,0,0,186,
        188,7,6,0,0,187,189,5,28,0,0,188,187,1,0,0,0,188,189,1,0,0,0,189,
        191,1,0,0,0,190,192,5,29,0,0,191,190,1,0,0,0,191,192,1,0,0,0,192,
        193,1,0,0,0,193,194,5,31,0,0,194,13,1,0,0,0,195,196,5,3,0,0,196,
        197,5,4,0,0,197,198,5,4,0,0,198,199,5,4,0,0,199,200,5,4,0,0,200,
        202,3,20,10,0,201,203,5,10,0,0,202,201,1,0,0,0,202,203,1,0,0,0,203,
        204,1,0,0,0,204,205,7,5,0,0,205,15,1,0,0,0,206,207,5,3,0,0,207,208,
        5,4,0,0,208,209,5,4,0,0,209,210,5,4,0,0,210,211,5,4,0,0,211,212,
        5,4,0,0,212,213,5,4,0,0,213,215,3,20,10,0,214,216,5,11,0,0,215,214,
        1,0,0,0,215,216,1,0,0,0,216,217,1,0,0,0,217,218,7,5,0,0,218,17,1,
        0,0,0,219,220,5,3,0,0,220,221,5,4,0,0,221,222,5,4,0,0,222,223,5,
        4,0,0,223,224,5,4,0,0,224,225,5,4,0,0,225,226,5,4,0,0,226,227,5,
        4,0,0,227,228,5,4,0,0,228,230,3,20,10,0,229,231,5,12,0,0,230,229,
        1,0,0,0,230,231,1,0,0,0,231,232,1,0,0,0,232,233,7,5,0,0,233,19,1,
        0,0,0,234,235,7,7,0,0,235,21,1,0,0,0,41,23,31,36,41,44,46,55,65,
        68,72,75,78,81,84,87,93,98,103,105,112,115,118,121,131,134,137,140,
        143,154,157,160,163,166,169,182,184,188,191,202,215,230
    ]

class VnmrPKParser ( Parser ):

    grammarFileName = "VnmrPKParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'peak id.'", "'# Format:'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'Dim 0 (ppm)'", "'Dim 1 (ppm)'", 
                     "'Dim 2 (ppm)'", "'Dim 3 (ppm)'", "'Dev. 0'", "'Dev. 1'", 
                     "'Dev. 2'", "'Dev. 3'", "'Amplitude'", "<INVALID>", 
                     "<INVALID>", "'Assignment'", "<INVALID>", "<INVALID>", 
                     "'Peak_Number'", "'X(ppm)'", "'Y(ppm)'", "'Z(ppm)'", 
                     "'A(ppm)'", "<INVALID>", "<INVALID>", "'Linewidth_X(Hz)'", 
                     "'Linewidth_Y(Hz)'", "'Linewidth_Z(Hz)'", "'Linewidth_A(Hz)'", 
                     "'FWHM_X(Hz)'", "'FWHM_Y(Hz)'", "'FWHM_Z(Hz)'", "'FWHM_A(Hz)'", 
                     "'Comment'" ]

    symbolicNames = [ "<INVALID>", "Peak_id", "Format", "Integer", "Float", 
                      "Real", "COMMENT", "Double_quote_string", "EXCLM_COMMENT", 
                      "SMCLN_COMMENT", "Assignment_2d_ex", "Assignment_3d_ex", 
                      "Assignment_4d_ex", "SPACE", "RETURN", "ENCLOSE_COMMENT", 
                      "SECTION_COMMENT", "LINE_COMMENT", "Dim_0_ppm", "Dim_1_ppm", 
                      "Dim_2_ppm", "Dim_3_ppm", "Dev_0", "Dev_1", "Dev_2", 
                      "Dev_3", "Amplitude", "Intensity_LA", "Volume_LA", 
                      "Assignment", "SPACE_LA", "RETURN_LA", "Peak_number", 
                      "X_ppm", "Y_ppm", "Z_ppm", "A_ppm", "Intensity", "Volume", 
                      "Linewidth_X", "Linewidth_Y", "Linewidth_Z", "Linewidth_A", 
                      "FWHM_X", "FWHM_Y", "FWHM_Z", "FWHM_A", "Comment", 
                      "SPACE_FO", "RETURN_FO", "Any_name", "SPACE_CM", "RETURN_CM" ]

    RULE_vnmr_pk = 0
    RULE_comment = 1
    RULE_format = 2
    RULE_peak_ll2d = 3
    RULE_peak_ll3d = 4
    RULE_peak_ll4d = 5
    RULE_data_label = 6
    RULE_peak_2d = 7
    RULE_peak_3d = 8
    RULE_peak_4d = 9
    RULE_number = 10

    ruleNames =  [ "vnmr_pk", "comment", "format", "peak_ll2d", "peak_ll3d", 
                   "peak_ll4d", "data_label", "peak_2d", "peak_3d", "peak_4d", 
                   "number" ]

    EOF = Token.EOF
    Peak_id=1
    Format=2
    Integer=3
    Float=4
    Real=5
    COMMENT=6
    Double_quote_string=7
    EXCLM_COMMENT=8
    SMCLN_COMMENT=9
    Assignment_2d_ex=10
    Assignment_3d_ex=11
    Assignment_4d_ex=12
    SPACE=13
    RETURN=14
    ENCLOSE_COMMENT=15
    SECTION_COMMENT=16
    LINE_COMMENT=17
    Dim_0_ppm=18
    Dim_1_ppm=19
    Dim_2_ppm=20
    Dim_3_ppm=21
    Dev_0=22
    Dev_1=23
    Dev_2=24
    Dev_3=25
    Amplitude=26
    Intensity_LA=27
    Volume_LA=28
    Assignment=29
    SPACE_LA=30
    RETURN_LA=31
    Peak_number=32
    X_ppm=33
    Y_ppm=34
    Z_ppm=35
    A_ppm=36
    Intensity=37
    Volume=38
    Linewidth_X=39
    Linewidth_Y=40
    Linewidth_Z=41
    Linewidth_A=42
    FWHM_X=43
    FWHM_Y=44
    FWHM_Z=45
    FWHM_A=46
    Comment=47
    SPACE_FO=48
    RETURN_FO=49
    Any_name=50
    SPACE_CM=51
    RETURN_CM=52

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Vnmr_pkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(VnmrPKParser.EOF, 0)

        def RETURN(self, i:int=None):
            if i is None:
                return self.getTokens(VnmrPKParser.RETURN)
            else:
                return self.getToken(VnmrPKParser.RETURN, i)

        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VnmrPKParser.CommentContext)
            else:
                return self.getTypedRuleContext(VnmrPKParser.CommentContext,i)


        def format_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VnmrPKParser.FormatContext)
            else:
                return self.getTypedRuleContext(VnmrPKParser.FormatContext,i)


        def data_label(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VnmrPKParser.Data_labelContext)
            else:
                return self.getTypedRuleContext(VnmrPKParser.Data_labelContext,i)


        def peak_2d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VnmrPKParser.Peak_2dContext)
            else:
                return self.getTypedRuleContext(VnmrPKParser.Peak_2dContext,i)


        def peak_3d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VnmrPKParser.Peak_3dContext)
            else:
                return self.getTypedRuleContext(VnmrPKParser.Peak_3dContext,i)


        def peak_4d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VnmrPKParser.Peak_4dContext)
            else:
                return self.getTypedRuleContext(VnmrPKParser.Peak_4dContext,i)


        def getRuleIndex(self):
            return VnmrPKParser.RULE_vnmr_pk

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVnmr_pk" ):
                listener.enterVnmr_pk(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVnmr_pk" ):
                listener.exitVnmr_pk(self)




    def vnmr_pk(self):

        localctx = VnmrPKParser.Vnmr_pkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_vnmr_pk)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 22
                self.match(VnmrPKParser.RETURN)


            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16462) != 0):
                self.state = 44
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 25
                    self.comment()
                    pass

                elif la_ == 2:
                    self.state = 26
                    self.format_()
                    pass

                elif la_ == 3:
                    self.state = 27
                    self.data_label()
                    pass

                elif la_ == 4:
                    self.state = 29 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 28
                            self.peak_2d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 31 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                    pass

                elif la_ == 5:
                    self.state = 34 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 33
                            self.peak_3d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 36 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                    pass

                elif la_ == 6:
                    self.state = 39 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 38
                            self.peak_4d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 41 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                    pass

                elif la_ == 7:
                    self.state = 43
                    self.match(VnmrPKParser.RETURN)
                    pass


                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self.match(VnmrPKParser.EOF)
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
            return self.getToken(VnmrPKParser.COMMENT, 0)

        def RETURN_CM(self):
            return self.getToken(VnmrPKParser.RETURN_CM, 0)

        def EOF(self):
            return self.getToken(VnmrPKParser.EOF, 0)

        def Any_name(self, i:int=None):
            if i is None:
                return self.getTokens(VnmrPKParser.Any_name)
            else:
                return self.getToken(VnmrPKParser.Any_name, i)

        def getRuleIndex(self):
            return VnmrPKParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = VnmrPKParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(VnmrPKParser.COMMENT)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 52
                self.match(VnmrPKParser.Any_name)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 58
            _la = self._input.LA(1)
            if not(_la==-1 or _la==52):
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


    class FormatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Format(self):
            return self.getToken(VnmrPKParser.Format, 0)

        def Peak_number(self):
            return self.getToken(VnmrPKParser.Peak_number, 0)

        def X_ppm(self):
            return self.getToken(VnmrPKParser.X_ppm, 0)

        def Y_ppm(self):
            return self.getToken(VnmrPKParser.Y_ppm, 0)

        def Intensity(self):
            return self.getToken(VnmrPKParser.Intensity, 0)

        def RETURN_FO(self):
            return self.getToken(VnmrPKParser.RETURN_FO, 0)

        def Z_ppm(self):
            return self.getToken(VnmrPKParser.Z_ppm, 0)

        def A_ppm(self):
            return self.getToken(VnmrPKParser.A_ppm, 0)

        def Volume(self):
            return self.getToken(VnmrPKParser.Volume, 0)

        def Comment(self):
            return self.getToken(VnmrPKParser.Comment, 0)

        def Linewidth_X(self):
            return self.getToken(VnmrPKParser.Linewidth_X, 0)

        def FWHM_X(self):
            return self.getToken(VnmrPKParser.FWHM_X, 0)

        def Linewidth_Y(self):
            return self.getToken(VnmrPKParser.Linewidth_Y, 0)

        def FWHM_Y(self):
            return self.getToken(VnmrPKParser.FWHM_Y, 0)

        def Linewidth_Z(self):
            return self.getToken(VnmrPKParser.Linewidth_Z, 0)

        def FWHM_Z(self):
            return self.getToken(VnmrPKParser.FWHM_Z, 0)

        def Linewidth_A(self):
            return self.getToken(VnmrPKParser.Linewidth_A, 0)

        def FWHM_A(self):
            return self.getToken(VnmrPKParser.FWHM_A, 0)

        def peak_ll2d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VnmrPKParser.Peak_ll2dContext)
            else:
                return self.getTypedRuleContext(VnmrPKParser.Peak_ll2dContext,i)


        def peak_ll3d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VnmrPKParser.Peak_ll3dContext)
            else:
                return self.getTypedRuleContext(VnmrPKParser.Peak_ll3dContext,i)


        def peak_ll4d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VnmrPKParser.Peak_ll4dContext)
            else:
                return self.getTypedRuleContext(VnmrPKParser.Peak_ll4dContext,i)


        def getRuleIndex(self):
            return VnmrPKParser.RULE_format

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormat" ):
                listener.enterFormat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormat" ):
                listener.exitFormat(self)




    def format_(self):

        localctx = VnmrPKParser.FormatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_format)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(VnmrPKParser.Format)
            self.state = 61
            self.match(VnmrPKParser.Peak_number)
            self.state = 62
            self.match(VnmrPKParser.X_ppm)
            self.state = 63
            self.match(VnmrPKParser.Y_ppm)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 64
                self.match(VnmrPKParser.Z_ppm)


            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 67
                self.match(VnmrPKParser.A_ppm)


            self.state = 70
            self.match(VnmrPKParser.Intensity)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 71
                self.match(VnmrPKParser.Volume)


            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39 or _la==43:
                self.state = 74
                _la = self._input.LA(1)
                if not(_la==39 or _la==43):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40 or _la==44:
                self.state = 77
                _la = self._input.LA(1)
                if not(_la==40 or _la==44):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41 or _la==45:
                self.state = 80
                _la = self._input.LA(1)
                if not(_la==41 or _la==45):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42 or _la==46:
                self.state = 83
                _la = self._input.LA(1)
                if not(_la==42 or _la==46):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 86
                self.match(VnmrPKParser.Comment)


            self.state = 89
            self.match(VnmrPKParser.RETURN_FO)
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 91 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 90
                        self.peak_ll2d()

                    else:
                        raise NoViableAltException(self)
                    self.state = 93 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

                pass

            elif la_ == 2:
                self.state = 96 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 95
                        self.peak_ll3d()

                    else:
                        raise NoViableAltException(self)
                    self.state = 98 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

                pass

            elif la_ == 3:
                self.state = 101 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 100
                        self.peak_ll4d()

                    else:
                        raise NoViableAltException(self)
                    self.state = 103 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Peak_ll2dContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self):
            return self.getToken(VnmrPKParser.Integer, 0)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(VnmrPKParser.Float)
            else:
                return self.getToken(VnmrPKParser.Float, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VnmrPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(VnmrPKParser.NumberContext,i)


        def RETURN(self):
            return self.getToken(VnmrPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(VnmrPKParser.EOF, 0)

        def Double_quote_string(self):
            return self.getToken(VnmrPKParser.Double_quote_string, 0)

        def getRuleIndex(self):
            return VnmrPKParser.RULE_peak_ll2d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_ll2d" ):
                listener.enterPeak_ll2d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_ll2d" ):
                listener.exitPeak_ll2d(self)




    def peak_ll2d(self):

        localctx = VnmrPKParser.Peak_ll2dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_peak_ll2d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(VnmrPKParser.Integer)
            self.state = 108
            self.match(VnmrPKParser.Float)
            self.state = 109
            self.match(VnmrPKParser.Float)
            self.state = 110
            self.number()
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 111
                self.number()


            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 114
                self.number()


            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0):
                self.state = 117
                self.number()


            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 120
                self.match(VnmrPKParser.Double_quote_string)


            self.state = 123
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


    class Peak_ll3dContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self):
            return self.getToken(VnmrPKParser.Integer, 0)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(VnmrPKParser.Float)
            else:
                return self.getToken(VnmrPKParser.Float, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VnmrPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(VnmrPKParser.NumberContext,i)


        def RETURN(self):
            return self.getToken(VnmrPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(VnmrPKParser.EOF, 0)

        def Double_quote_string(self):
            return self.getToken(VnmrPKParser.Double_quote_string, 0)

        def getRuleIndex(self):
            return VnmrPKParser.RULE_peak_ll3d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_ll3d" ):
                listener.enterPeak_ll3d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_ll3d" ):
                listener.exitPeak_ll3d(self)




    def peak_ll3d(self):

        localctx = VnmrPKParser.Peak_ll3dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_peak_ll3d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(VnmrPKParser.Integer)
            self.state = 126
            self.match(VnmrPKParser.Float)
            self.state = 127
            self.match(VnmrPKParser.Float)
            self.state = 128
            self.match(VnmrPKParser.Float)
            self.state = 129
            self.number()
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 130
                self.number()


            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 133
                self.number()


            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 136
                self.number()


            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0):
                self.state = 139
                self.number()


            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 142
                self.match(VnmrPKParser.Double_quote_string)


            self.state = 145
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


    class Peak_ll4dContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self):
            return self.getToken(VnmrPKParser.Integer, 0)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(VnmrPKParser.Float)
            else:
                return self.getToken(VnmrPKParser.Float, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VnmrPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(VnmrPKParser.NumberContext,i)


        def RETURN(self):
            return self.getToken(VnmrPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(VnmrPKParser.EOF, 0)

        def Double_quote_string(self):
            return self.getToken(VnmrPKParser.Double_quote_string, 0)

        def getRuleIndex(self):
            return VnmrPKParser.RULE_peak_ll4d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_ll4d" ):
                listener.enterPeak_ll4d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_ll4d" ):
                listener.exitPeak_ll4d(self)




    def peak_ll4d(self):

        localctx = VnmrPKParser.Peak_ll4dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_peak_ll4d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(VnmrPKParser.Integer)
            self.state = 148
            self.match(VnmrPKParser.Float)
            self.state = 149
            self.match(VnmrPKParser.Float)
            self.state = 150
            self.match(VnmrPKParser.Float)
            self.state = 151
            self.match(VnmrPKParser.Float)
            self.state = 152
            self.number()
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 153
                self.number()


            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 156
                self.number()


            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 159
                self.number()


            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 162
                self.number()


            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0):
                self.state = 165
                self.number()


            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 168
                self.match(VnmrPKParser.Double_quote_string)


            self.state = 171
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


    class Data_labelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Peak_id(self):
            return self.getToken(VnmrPKParser.Peak_id, 0)

        def Dim_0_ppm(self):
            return self.getToken(VnmrPKParser.Dim_0_ppm, 0)

        def Dev_0(self):
            return self.getToken(VnmrPKParser.Dev_0, 0)

        def Dim_1_ppm(self):
            return self.getToken(VnmrPKParser.Dim_1_ppm, 0)

        def Dev_1(self):
            return self.getToken(VnmrPKParser.Dev_1, 0)

        def RETURN_LA(self):
            return self.getToken(VnmrPKParser.RETURN_LA, 0)

        def Amplitude(self):
            return self.getToken(VnmrPKParser.Amplitude, 0)

        def Intensity_LA(self):
            return self.getToken(VnmrPKParser.Intensity_LA, 0)

        def Dim_2_ppm(self):
            return self.getToken(VnmrPKParser.Dim_2_ppm, 0)

        def Dev_2(self):
            return self.getToken(VnmrPKParser.Dev_2, 0)

        def Volume_LA(self):
            return self.getToken(VnmrPKParser.Volume_LA, 0)

        def Assignment(self):
            return self.getToken(VnmrPKParser.Assignment, 0)

        def Dim_3_ppm(self):
            return self.getToken(VnmrPKParser.Dim_3_ppm, 0)

        def Dev_3(self):
            return self.getToken(VnmrPKParser.Dev_3, 0)

        def getRuleIndex(self):
            return VnmrPKParser.RULE_data_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_label" ):
                listener.enterData_label(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_label" ):
                listener.exitData_label(self)




    def data_label(self):

        localctx = VnmrPKParser.Data_labelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_data_label)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(VnmrPKParser.Peak_id)
            self.state = 174
            self.match(VnmrPKParser.Dim_0_ppm)
            self.state = 175
            self.match(VnmrPKParser.Dev_0)
            self.state = 176
            self.match(VnmrPKParser.Dim_1_ppm)
            self.state = 177
            self.match(VnmrPKParser.Dev_1)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 178
                self.match(VnmrPKParser.Dim_2_ppm)
                self.state = 179
                self.match(VnmrPKParser.Dev_2)
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 180
                    self.match(VnmrPKParser.Dim_3_ppm)
                    self.state = 181
                    self.match(VnmrPKParser.Dev_3)




            self.state = 186
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 187
                self.match(VnmrPKParser.Volume_LA)


            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 190
                self.match(VnmrPKParser.Assignment)


            self.state = 193
            self.match(VnmrPKParser.RETURN_LA)
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

        def Integer(self):
            return self.getToken(VnmrPKParser.Integer, 0)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(VnmrPKParser.Float)
            else:
                return self.getToken(VnmrPKParser.Float, i)

        def number(self):
            return self.getTypedRuleContext(VnmrPKParser.NumberContext,0)


        def RETURN(self):
            return self.getToken(VnmrPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(VnmrPKParser.EOF, 0)

        def Assignment_2d_ex(self):
            return self.getToken(VnmrPKParser.Assignment_2d_ex, 0)

        def getRuleIndex(self):
            return VnmrPKParser.RULE_peak_2d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_2d" ):
                listener.enterPeak_2d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_2d" ):
                listener.exitPeak_2d(self)




    def peak_2d(self):

        localctx = VnmrPKParser.Peak_2dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_peak_2d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(VnmrPKParser.Integer)
            self.state = 196
            self.match(VnmrPKParser.Float)
            self.state = 197
            self.match(VnmrPKParser.Float)
            self.state = 198
            self.match(VnmrPKParser.Float)
            self.state = 199
            self.match(VnmrPKParser.Float)
            self.state = 200
            self.number()
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 201
                self.match(VnmrPKParser.Assignment_2d_ex)


            self.state = 204
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

        def Integer(self):
            return self.getToken(VnmrPKParser.Integer, 0)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(VnmrPKParser.Float)
            else:
                return self.getToken(VnmrPKParser.Float, i)

        def number(self):
            return self.getTypedRuleContext(VnmrPKParser.NumberContext,0)


        def RETURN(self):
            return self.getToken(VnmrPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(VnmrPKParser.EOF, 0)

        def Assignment_3d_ex(self):
            return self.getToken(VnmrPKParser.Assignment_3d_ex, 0)

        def getRuleIndex(self):
            return VnmrPKParser.RULE_peak_3d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_3d" ):
                listener.enterPeak_3d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_3d" ):
                listener.exitPeak_3d(self)




    def peak_3d(self):

        localctx = VnmrPKParser.Peak_3dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_peak_3d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(VnmrPKParser.Integer)
            self.state = 207
            self.match(VnmrPKParser.Float)
            self.state = 208
            self.match(VnmrPKParser.Float)
            self.state = 209
            self.match(VnmrPKParser.Float)
            self.state = 210
            self.match(VnmrPKParser.Float)
            self.state = 211
            self.match(VnmrPKParser.Float)
            self.state = 212
            self.match(VnmrPKParser.Float)
            self.state = 213
            self.number()
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 214
                self.match(VnmrPKParser.Assignment_3d_ex)


            self.state = 217
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

        def Integer(self):
            return self.getToken(VnmrPKParser.Integer, 0)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(VnmrPKParser.Float)
            else:
                return self.getToken(VnmrPKParser.Float, i)

        def number(self):
            return self.getTypedRuleContext(VnmrPKParser.NumberContext,0)


        def RETURN(self):
            return self.getToken(VnmrPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(VnmrPKParser.EOF, 0)

        def Assignment_4d_ex(self):
            return self.getToken(VnmrPKParser.Assignment_4d_ex, 0)

        def getRuleIndex(self):
            return VnmrPKParser.RULE_peak_4d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_4d" ):
                listener.enterPeak_4d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_4d" ):
                listener.exitPeak_4d(self)




    def peak_4d(self):

        localctx = VnmrPKParser.Peak_4dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_peak_4d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(VnmrPKParser.Integer)
            self.state = 220
            self.match(VnmrPKParser.Float)
            self.state = 221
            self.match(VnmrPKParser.Float)
            self.state = 222
            self.match(VnmrPKParser.Float)
            self.state = 223
            self.match(VnmrPKParser.Float)
            self.state = 224
            self.match(VnmrPKParser.Float)
            self.state = 225
            self.match(VnmrPKParser.Float)
            self.state = 226
            self.match(VnmrPKParser.Float)
            self.state = 227
            self.match(VnmrPKParser.Float)
            self.state = 228
            self.number()
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 229
                self.match(VnmrPKParser.Assignment_4d_ex)


            self.state = 232
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
            return self.getToken(VnmrPKParser.Real, 0)

        def Float(self):
            return self.getToken(VnmrPKParser.Float, 0)

        def Integer(self):
            return self.getToken(VnmrPKParser.Integer, 0)

        def getRuleIndex(self):
            return VnmrPKParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = VnmrPKParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
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





