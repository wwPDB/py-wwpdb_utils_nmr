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
        4,1,52,236,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,3,0,24,8,0,1,0,1,0,1,0,1,
        0,4,0,30,8,0,11,0,12,0,31,1,0,4,0,35,8,0,11,0,12,0,36,1,0,4,0,40,
        8,0,11,0,12,0,41,5,0,44,8,0,10,0,12,0,47,9,0,1,0,1,0,1,1,1,1,5,1,
        53,8,1,10,1,12,1,56,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,3,2,65,8,2,1,
        2,3,2,68,8,2,1,2,1,2,3,2,72,8,2,1,2,3,2,75,8,2,1,2,3,2,78,8,2,1,
        2,3,2,81,8,2,1,2,3,2,84,8,2,1,2,3,2,87,8,2,1,2,1,2,4,2,91,8,2,11,
        2,12,2,92,1,2,4,2,96,8,2,11,2,12,2,97,1,2,4,2,101,8,2,11,2,12,2,
        102,3,2,105,8,2,1,3,1,3,1,3,1,3,1,3,3,3,112,8,3,1,3,3,3,115,8,3,
        1,3,3,3,118,8,3,1,3,3,3,121,8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,
        3,4,131,8,4,1,4,3,4,134,8,4,1,4,3,4,137,8,4,1,4,3,4,140,8,4,1,4,
        3,4,143,8,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,154,8,5,1,5,
        3,5,157,8,5,1,5,3,5,160,8,5,1,5,3,5,163,8,5,1,5,3,5,166,8,5,1,5,
        3,5,169,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,182,
        8,6,3,6,184,8,6,1,6,1,6,3,6,188,8,6,1,6,3,6,191,8,6,1,6,1,6,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,3,7,202,8,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,3,8,215,8,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,3,9,230,8,9,1,9,1,9,1,10,1,10,1,10,0,0,11,0,2,4,
        6,8,10,12,14,16,18,20,0,8,1,1,52,52,2,0,39,39,43,43,2,0,40,40,44,
        44,2,0,41,41,45,45,2,0,42,42,46,46,1,1,14,14,1,0,26,27,1,0,3,5,270,
        0,23,1,0,0,0,2,50,1,0,0,0,4,59,1,0,0,0,6,106,1,0,0,0,8,124,1,0,0,
        0,10,146,1,0,0,0,12,172,1,0,0,0,14,194,1,0,0,0,16,205,1,0,0,0,18,
        218,1,0,0,0,20,233,1,0,0,0,22,24,5,14,0,0,23,22,1,0,0,0,23,24,1,
        0,0,0,24,45,1,0,0,0,25,44,3,2,1,0,26,44,3,4,2,0,27,44,3,12,6,0,28,
        30,3,14,7,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,1,0,
        0,0,32,44,1,0,0,0,33,35,3,16,8,0,34,33,1,0,0,0,35,36,1,0,0,0,36,
        34,1,0,0,0,36,37,1,0,0,0,37,44,1,0,0,0,38,40,3,18,9,0,39,38,1,0,
        0,0,40,41,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,44,1,0,0,0,43,25,
        1,0,0,0,43,26,1,0,0,0,43,27,1,0,0,0,43,29,1,0,0,0,43,34,1,0,0,0,
        43,39,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,48,1,
        0,0,0,47,45,1,0,0,0,48,49,5,0,0,1,49,1,1,0,0,0,50,54,5,6,0,0,51,
        53,5,50,0,0,52,51,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,
        0,0,55,57,1,0,0,0,56,54,1,0,0,0,57,58,7,0,0,0,58,3,1,0,0,0,59,60,
        5,2,0,0,60,61,5,32,0,0,61,62,5,33,0,0,62,64,5,34,0,0,63,65,5,35,
        0,0,64,63,1,0,0,0,64,65,1,0,0,0,65,67,1,0,0,0,66,68,5,36,0,0,67,
        66,1,0,0,0,67,68,1,0,0,0,68,69,1,0,0,0,69,71,5,37,0,0,70,72,5,38,
        0,0,71,70,1,0,0,0,71,72,1,0,0,0,72,74,1,0,0,0,73,75,7,1,0,0,74,73,
        1,0,0,0,74,75,1,0,0,0,75,77,1,0,0,0,76,78,7,2,0,0,77,76,1,0,0,0,
        77,78,1,0,0,0,78,80,1,0,0,0,79,81,7,3,0,0,80,79,1,0,0,0,80,81,1,
        0,0,0,81,83,1,0,0,0,82,84,7,4,0,0,83,82,1,0,0,0,83,84,1,0,0,0,84,
        86,1,0,0,0,85,87,5,47,0,0,86,85,1,0,0,0,86,87,1,0,0,0,87,88,1,0,
        0,0,88,104,5,49,0,0,89,91,3,6,3,0,90,89,1,0,0,0,91,92,1,0,0,0,92,
        90,1,0,0,0,92,93,1,0,0,0,93,105,1,0,0,0,94,96,3,8,4,0,95,94,1,0,
        0,0,96,97,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,105,1,0,0,0,99,
        101,3,10,5,0,100,99,1,0,0,0,101,102,1,0,0,0,102,100,1,0,0,0,102,
        103,1,0,0,0,103,105,1,0,0,0,104,90,1,0,0,0,104,95,1,0,0,0,104,100,
        1,0,0,0,105,5,1,0,0,0,106,107,5,3,0,0,107,108,5,4,0,0,108,109,5,
        4,0,0,109,111,3,20,10,0,110,112,3,20,10,0,111,110,1,0,0,0,111,112,
        1,0,0,0,112,114,1,0,0,0,113,115,3,20,10,0,114,113,1,0,0,0,114,115,
        1,0,0,0,115,117,1,0,0,0,116,118,3,20,10,0,117,116,1,0,0,0,117,118,
        1,0,0,0,118,120,1,0,0,0,119,121,5,7,0,0,120,119,1,0,0,0,120,121,
        1,0,0,0,121,122,1,0,0,0,122,123,7,5,0,0,123,7,1,0,0,0,124,125,5,
        3,0,0,125,126,5,4,0,0,126,127,5,4,0,0,127,128,5,4,0,0,128,130,3,
        20,10,0,129,131,3,20,10,0,130,129,1,0,0,0,130,131,1,0,0,0,131,133,
        1,0,0,0,132,134,3,20,10,0,133,132,1,0,0,0,133,134,1,0,0,0,134,136,
        1,0,0,0,135,137,3,20,10,0,136,135,1,0,0,0,136,137,1,0,0,0,137,139,
        1,0,0,0,138,140,3,20,10,0,139,138,1,0,0,0,139,140,1,0,0,0,140,142,
        1,0,0,0,141,143,5,7,0,0,142,141,1,0,0,0,142,143,1,0,0,0,143,144,
        1,0,0,0,144,145,7,5,0,0,145,9,1,0,0,0,146,147,5,3,0,0,147,148,5,
        4,0,0,148,149,5,4,0,0,149,150,5,4,0,0,150,151,5,4,0,0,151,153,3,
        20,10,0,152,154,3,20,10,0,153,152,1,0,0,0,153,154,1,0,0,0,154,156,
        1,0,0,0,155,157,3,20,10,0,156,155,1,0,0,0,156,157,1,0,0,0,157,159,
        1,0,0,0,158,160,3,20,10,0,159,158,1,0,0,0,159,160,1,0,0,0,160,162,
        1,0,0,0,161,163,3,20,10,0,162,161,1,0,0,0,162,163,1,0,0,0,163,165,
        1,0,0,0,164,166,3,20,10,0,165,164,1,0,0,0,165,166,1,0,0,0,166,168,
        1,0,0,0,167,169,5,7,0,0,168,167,1,0,0,0,168,169,1,0,0,0,169,170,
        1,0,0,0,170,171,7,5,0,0,171,11,1,0,0,0,172,173,5,1,0,0,173,174,5,
        18,0,0,174,175,5,22,0,0,175,176,5,19,0,0,176,183,5,23,0,0,177,178,
        5,20,0,0,178,181,5,24,0,0,179,180,5,21,0,0,180,182,5,25,0,0,181,
        179,1,0,0,0,181,182,1,0,0,0,182,184,1,0,0,0,183,177,1,0,0,0,183,
        184,1,0,0,0,184,185,1,0,0,0,185,187,7,6,0,0,186,188,5,28,0,0,187,
        186,1,0,0,0,187,188,1,0,0,0,188,190,1,0,0,0,189,191,5,29,0,0,190,
        189,1,0,0,0,190,191,1,0,0,0,191,192,1,0,0,0,192,193,5,31,0,0,193,
        13,1,0,0,0,194,195,5,3,0,0,195,196,5,4,0,0,196,197,5,4,0,0,197,198,
        5,4,0,0,198,199,5,4,0,0,199,201,3,20,10,0,200,202,5,10,0,0,201,200,
        1,0,0,0,201,202,1,0,0,0,202,203,1,0,0,0,203,204,7,5,0,0,204,15,1,
        0,0,0,205,206,5,3,0,0,206,207,5,4,0,0,207,208,5,4,0,0,208,209,5,
        4,0,0,209,210,5,4,0,0,210,211,5,4,0,0,211,212,5,4,0,0,212,214,3,
        20,10,0,213,215,5,11,0,0,214,213,1,0,0,0,214,215,1,0,0,0,215,216,
        1,0,0,0,216,217,7,5,0,0,217,17,1,0,0,0,218,219,5,3,0,0,219,220,5,
        4,0,0,220,221,5,4,0,0,221,222,5,4,0,0,222,223,5,4,0,0,223,224,5,
        4,0,0,224,225,5,4,0,0,225,226,5,4,0,0,226,227,5,4,0,0,227,229,3,
        20,10,0,228,230,5,12,0,0,229,228,1,0,0,0,229,230,1,0,0,0,230,231,
        1,0,0,0,231,232,7,5,0,0,232,19,1,0,0,0,233,234,7,7,0,0,234,21,1,
        0,0,0,41,23,31,36,41,43,45,54,64,67,71,74,77,80,83,86,92,97,102,
        104,111,114,117,120,130,133,136,139,142,153,156,159,162,165,168,
        181,183,187,190,201,214,229
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

        def RETURN(self):
            return self.getToken(VnmrPKParser.RETURN, 0)

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
            _la = self._input.LA(1)
            if _la==14:
                self.state = 22
                self.match(VnmrPKParser.RETURN)


            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 78) != 0):
                self.state = 43
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


                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
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
            self.state = 50
            self.match(VnmrPKParser.COMMENT)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 51
                self.match(VnmrPKParser.Any_name)
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 57
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
            self.state = 59
            self.match(VnmrPKParser.Format)
            self.state = 60
            self.match(VnmrPKParser.Peak_number)
            self.state = 61
            self.match(VnmrPKParser.X_ppm)
            self.state = 62
            self.match(VnmrPKParser.Y_ppm)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 63
                self.match(VnmrPKParser.Z_ppm)


            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 66
                self.match(VnmrPKParser.A_ppm)


            self.state = 69
            self.match(VnmrPKParser.Intensity)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 70
                self.match(VnmrPKParser.Volume)


            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39 or _la==43:
                self.state = 73
                _la = self._input.LA(1)
                if not(_la==39 or _la==43):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40 or _la==44:
                self.state = 76
                _la = self._input.LA(1)
                if not(_la==40 or _la==44):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41 or _la==45:
                self.state = 79
                _la = self._input.LA(1)
                if not(_la==41 or _la==45):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42 or _la==46:
                self.state = 82
                _la = self._input.LA(1)
                if not(_la==42 or _la==46):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 85
                self.match(VnmrPKParser.Comment)


            self.state = 88
            self.match(VnmrPKParser.RETURN_FO)
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 90 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 89
                        self.peak_ll2d()

                    else:
                        raise NoViableAltException(self)
                    self.state = 92 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

                pass

            elif la_ == 2:
                self.state = 95 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 94
                        self.peak_ll3d()

                    else:
                        raise NoViableAltException(self)
                    self.state = 97 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

                pass

            elif la_ == 3:
                self.state = 100 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 99
                        self.peak_ll4d()

                    else:
                        raise NoViableAltException(self)
                    self.state = 102 
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
            self.state = 106
            self.match(VnmrPKParser.Integer)
            self.state = 107
            self.match(VnmrPKParser.Float)
            self.state = 108
            self.match(VnmrPKParser.Float)
            self.state = 109
            self.number()
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 110
                self.number()


            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 113
                self.number()


            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0):
                self.state = 116
                self.number()


            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 119
                self.match(VnmrPKParser.Double_quote_string)


            self.state = 122
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
            self.state = 124
            self.match(VnmrPKParser.Integer)
            self.state = 125
            self.match(VnmrPKParser.Float)
            self.state = 126
            self.match(VnmrPKParser.Float)
            self.state = 127
            self.match(VnmrPKParser.Float)
            self.state = 128
            self.number()
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 129
                self.number()


            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 132
                self.number()


            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 135
                self.number()


            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0):
                self.state = 138
                self.number()


            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 141
                self.match(VnmrPKParser.Double_quote_string)


            self.state = 144
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
            self.state = 146
            self.match(VnmrPKParser.Integer)
            self.state = 147
            self.match(VnmrPKParser.Float)
            self.state = 148
            self.match(VnmrPKParser.Float)
            self.state = 149
            self.match(VnmrPKParser.Float)
            self.state = 150
            self.match(VnmrPKParser.Float)
            self.state = 151
            self.number()
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 152
                self.number()


            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 155
                self.number()


            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 158
                self.number()


            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 161
                self.number()


            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0):
                self.state = 164
                self.number()


            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 167
                self.match(VnmrPKParser.Double_quote_string)


            self.state = 170
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
            self.state = 172
            self.match(VnmrPKParser.Peak_id)
            self.state = 173
            self.match(VnmrPKParser.Dim_0_ppm)
            self.state = 174
            self.match(VnmrPKParser.Dev_0)
            self.state = 175
            self.match(VnmrPKParser.Dim_1_ppm)
            self.state = 176
            self.match(VnmrPKParser.Dev_1)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 177
                self.match(VnmrPKParser.Dim_2_ppm)
                self.state = 178
                self.match(VnmrPKParser.Dev_2)
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 179
                    self.match(VnmrPKParser.Dim_3_ppm)
                    self.state = 180
                    self.match(VnmrPKParser.Dev_3)




            self.state = 185
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 186
                self.match(VnmrPKParser.Volume_LA)


            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 189
                self.match(VnmrPKParser.Assignment)


            self.state = 192
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
            self.state = 194
            self.match(VnmrPKParser.Integer)
            self.state = 195
            self.match(VnmrPKParser.Float)
            self.state = 196
            self.match(VnmrPKParser.Float)
            self.state = 197
            self.match(VnmrPKParser.Float)
            self.state = 198
            self.match(VnmrPKParser.Float)
            self.state = 199
            self.number()
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 200
                self.match(VnmrPKParser.Assignment_2d_ex)


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
            self.state = 205
            self.match(VnmrPKParser.Integer)
            self.state = 206
            self.match(VnmrPKParser.Float)
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
            self.number()
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 213
                self.match(VnmrPKParser.Assignment_3d_ex)


            self.state = 216
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
            self.state = 218
            self.match(VnmrPKParser.Integer)
            self.state = 219
            self.match(VnmrPKParser.Float)
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
            self.number()
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 228
                self.match(VnmrPKParser.Assignment_4d_ex)


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





