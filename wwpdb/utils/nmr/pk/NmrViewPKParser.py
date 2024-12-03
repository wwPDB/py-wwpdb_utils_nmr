# Generated from NmrViewPKParser.g4 by ANTLR 4.13.0
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
        4,1,31,165,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,0,5,0,25,8,0,10,0,12,0,28,
        9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,2,4,2,48,8,2,11,2,12,2,49,1,3,4,3,53,8,3,11,3,12,3,54,
        1,4,4,4,58,8,4,11,4,12,4,59,1,5,4,5,63,8,5,11,5,12,5,64,1,5,1,5,
        1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,0,162,0,26,1,0,0,0,2,31,1,
        0,0,0,4,47,1,0,0,0,6,52,1,0,0,0,8,57,1,0,0,0,10,62,1,0,0,0,12,72,
        1,0,0,0,14,80,1,0,0,0,16,101,1,0,0,0,18,129,1,0,0,0,20,25,3,2,1,
        0,21,25,3,14,7,0,22,25,3,16,8,0,23,25,3,18,9,0,24,20,1,0,0,0,24,
        21,1,0,0,0,24,22,1,0,0,0,24,23,1,0,0,0,25,28,1,0,0,0,26,24,1,0,0,
        0,26,27,1,0,0,0,27,29,1,0,0,0,28,26,1,0,0,0,29,30,5,0,0,1,30,1,1,
        0,0,0,31,32,5,1,0,0,32,33,5,13,0,0,33,34,5,14,0,0,34,35,5,15,0,0,
        35,36,5,31,0,0,36,37,3,4,2,0,37,38,5,31,0,0,38,39,5,28,0,0,39,40,
        5,31,0,0,40,41,3,6,3,0,41,42,5,31,0,0,42,43,3,8,4,0,43,44,5,31,0,
        0,44,45,3,10,5,0,45,3,1,0,0,0,46,48,5,28,0,0,47,46,1,0,0,0,48,49,
        1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,5,1,0,0,0,51,53,5,29,0,0,
        52,51,1,0,0,0,53,54,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,7,1,0,
        0,0,56,58,5,29,0,0,57,56,1,0,0,0,58,59,1,0,0,0,59,57,1,0,0,0,59,
        60,1,0,0,0,60,9,1,0,0,0,61,63,3,12,6,0,62,61,1,0,0,0,63,64,1,0,0,
        0,64,62,1,0,0,0,64,65,1,0,0,0,65,66,1,0,0,0,66,67,5,23,0,0,67,68,
        5,24,0,0,68,69,5,25,0,0,69,70,5,26,0,0,70,71,5,27,0,0,71,11,1,0,
        0,0,72,73,5,16,0,0,73,74,5,17,0,0,74,75,5,18,0,0,75,76,5,19,0,0,
        76,77,5,20,0,0,77,78,5,21,0,0,78,79,5,22,0,0,79,13,1,0,0,0,80,81,
        5,2,0,0,81,82,5,10,0,0,82,83,5,3,0,0,83,84,5,3,0,0,84,85,5,3,0,0,
        85,86,5,8,0,0,86,87,5,10,0,0,87,88,5,10,0,0,88,89,5,10,0,0,89,90,
        5,3,0,0,90,91,5,3,0,0,91,92,5,3,0,0,92,93,5,8,0,0,93,94,5,10,0,0,
        94,95,5,10,0,0,95,96,5,3,0,0,96,97,5,3,0,0,97,98,5,2,0,0,98,99,5,
        10,0,0,99,100,5,2,0,0,100,15,1,0,0,0,101,102,5,2,0,0,102,103,5,10,
        0,0,103,104,5,3,0,0,104,105,5,3,0,0,105,106,5,3,0,0,106,107,5,8,
        0,0,107,108,5,10,0,0,108,109,5,10,0,0,109,110,5,10,0,0,110,111,5,
        3,0,0,111,112,5,3,0,0,112,113,5,3,0,0,113,114,5,8,0,0,114,115,5,
        10,0,0,115,116,5,10,0,0,116,117,5,10,0,0,117,118,5,3,0,0,118,119,
        5,3,0,0,119,120,5,3,0,0,120,121,5,8,0,0,121,122,5,10,0,0,122,123,
        5,10,0,0,123,124,5,3,0,0,124,125,5,3,0,0,125,126,5,2,0,0,126,127,
        5,10,0,0,127,128,5,2,0,0,128,17,1,0,0,0,129,130,5,2,0,0,130,131,
        5,10,0,0,131,132,5,3,0,0,132,133,5,3,0,0,133,134,5,3,0,0,134,135,
        5,8,0,0,135,136,5,10,0,0,136,137,5,10,0,0,137,138,5,10,0,0,138,139,
        5,3,0,0,139,140,5,3,0,0,140,141,5,3,0,0,141,142,5,8,0,0,142,143,
        5,10,0,0,143,144,5,10,0,0,144,145,5,10,0,0,145,146,5,3,0,0,146,147,
        5,3,0,0,147,148,5,3,0,0,148,149,5,8,0,0,149,150,5,10,0,0,150,151,
        5,10,0,0,151,152,5,10,0,0,152,153,5,3,0,0,153,154,5,3,0,0,154,155,
        5,3,0,0,155,156,5,8,0,0,156,157,5,10,0,0,157,158,5,10,0,0,158,159,
        5,3,0,0,159,160,5,3,0,0,160,161,5,2,0,0,161,162,5,10,0,0,162,163,
        5,2,0,0,163,19,1,0,0,0,6,24,26,49,54,59,64
    ]

class NmrViewPKParser ( Parser ):

    grammarFileName = "NmrViewPKParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'label'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'dataset'", "'sw'", "'sf'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'vol'", "'int'", "'stat'", "'comment'" ]

    symbolicNames = [ "<INVALID>", "Label", "Integer", "Float", "Real", 
                      "SHARP_COMMENT", "EXCLM_COMMENT", "SMCLN_COMMENT", 
                      "Simple_name", "SPACE", "ENCLOSE_COMMENT", "SECTION_COMMENT", 
                      "LINE_COMMENT", "Dataset", "Sw", "Sf", "L_name", "P_name", 
                      "W_name", "B_name", "E_name", "J_name", "U_name", 
                      "Vol", "Int", "Stat", "Comment", "Flag0", "Simple_name_LA", 
                      "Float_LA", "SPACE_LA", "RETURN_LA" ]

    RULE_nmrview_pk = 0
    RULE_data_label = 1
    RULE_labels = 2
    RULE_widths = 3
    RULE_freqs = 4
    RULE_vars = 5
    RULE_vars_per_axis = 6
    RULE_peak_list_2d = 7
    RULE_peak_list_3d = 8
    RULE_peak_list_4d = 9

    ruleNames =  [ "nmrview_pk", "data_label", "labels", "widths", "freqs", 
                   "vars", "vars_per_axis", "peak_list_2d", "peak_list_3d", 
                   "peak_list_4d" ]

    EOF = Token.EOF
    Label=1
    Integer=2
    Float=3
    Real=4
    SHARP_COMMENT=5
    EXCLM_COMMENT=6
    SMCLN_COMMENT=7
    Simple_name=8
    SPACE=9
    ENCLOSE_COMMENT=10
    SECTION_COMMENT=11
    LINE_COMMENT=12
    Dataset=13
    Sw=14
    Sf=15
    L_name=16
    P_name=17
    W_name=18
    B_name=19
    E_name=20
    J_name=21
    U_name=22
    Vol=23
    Int=24
    Stat=25
    Comment=26
    Flag0=27
    Simple_name_LA=28
    Float_LA=29
    SPACE_LA=30
    RETURN_LA=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Nmrview_pkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(NmrViewPKParser.EOF, 0)

        def data_label(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmrViewPKParser.Data_labelContext)
            else:
                return self.getTypedRuleContext(NmrViewPKParser.Data_labelContext,i)


        def peak_list_2d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmrViewPKParser.Peak_list_2dContext)
            else:
                return self.getTypedRuleContext(NmrViewPKParser.Peak_list_2dContext,i)


        def peak_list_3d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmrViewPKParser.Peak_list_3dContext)
            else:
                return self.getTypedRuleContext(NmrViewPKParser.Peak_list_3dContext,i)


        def peak_list_4d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmrViewPKParser.Peak_list_4dContext)
            else:
                return self.getTypedRuleContext(NmrViewPKParser.Peak_list_4dContext,i)


        def getRuleIndex(self):
            return NmrViewPKParser.RULE_nmrview_pk

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNmrview_pk" ):
                listener.enterNmrview_pk(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNmrview_pk" ):
                listener.exitNmrview_pk(self)




    def nmrview_pk(self):

        localctx = NmrViewPKParser.Nmrview_pkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_nmrview_pk)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 24
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 20
                    self.data_label()
                    pass

                elif la_ == 2:
                    self.state = 21
                    self.peak_list_2d()
                    pass

                elif la_ == 3:
                    self.state = 22
                    self.peak_list_3d()
                    pass

                elif la_ == 4:
                    self.state = 23
                    self.peak_list_4d()
                    pass


                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self.match(NmrViewPKParser.EOF)
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

        def Label(self):
            return self.getToken(NmrViewPKParser.Label, 0)

        def Dataset(self):
            return self.getToken(NmrViewPKParser.Dataset, 0)

        def Sw(self):
            return self.getToken(NmrViewPKParser.Sw, 0)

        def Sf(self):
            return self.getToken(NmrViewPKParser.Sf, 0)

        def RETURN_LA(self, i:int=None):
            if i is None:
                return self.getTokens(NmrViewPKParser.RETURN_LA)
            else:
                return self.getToken(NmrViewPKParser.RETURN_LA, i)

        def labels(self):
            return self.getTypedRuleContext(NmrViewPKParser.LabelsContext,0)


        def Simple_name_LA(self):
            return self.getToken(NmrViewPKParser.Simple_name_LA, 0)

        def widths(self):
            return self.getTypedRuleContext(NmrViewPKParser.WidthsContext,0)


        def freqs(self):
            return self.getTypedRuleContext(NmrViewPKParser.FreqsContext,0)


        def vars_(self):
            return self.getTypedRuleContext(NmrViewPKParser.VarsContext,0)


        def getRuleIndex(self):
            return NmrViewPKParser.RULE_data_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_label" ):
                listener.enterData_label(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_label" ):
                listener.exitData_label(self)




    def data_label(self):

        localctx = NmrViewPKParser.Data_labelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_data_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(NmrViewPKParser.Label)
            self.state = 32
            self.match(NmrViewPKParser.Dataset)
            self.state = 33
            self.match(NmrViewPKParser.Sw)
            self.state = 34
            self.match(NmrViewPKParser.Sf)
            self.state = 35
            self.match(NmrViewPKParser.RETURN_LA)
            self.state = 36
            self.labels()
            self.state = 37
            self.match(NmrViewPKParser.RETURN_LA)
            self.state = 38
            self.match(NmrViewPKParser.Simple_name_LA)
            self.state = 39
            self.match(NmrViewPKParser.RETURN_LA)
            self.state = 40
            self.widths()
            self.state = 41
            self.match(NmrViewPKParser.RETURN_LA)
            self.state = 42
            self.freqs()
            self.state = 43
            self.match(NmrViewPKParser.RETURN_LA)
            self.state = 44
            self.vars_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Simple_name_LA(self, i:int=None):
            if i is None:
                return self.getTokens(NmrViewPKParser.Simple_name_LA)
            else:
                return self.getToken(NmrViewPKParser.Simple_name_LA, i)

        def getRuleIndex(self):
            return NmrViewPKParser.RULE_labels

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabels" ):
                listener.enterLabels(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabels" ):
                listener.exitLabels(self)




    def labels(self):

        localctx = NmrViewPKParser.LabelsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_labels)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self.match(NmrViewPKParser.Simple_name_LA)
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==28):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WidthsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Float_LA(self, i:int=None):
            if i is None:
                return self.getTokens(NmrViewPKParser.Float_LA)
            else:
                return self.getToken(NmrViewPKParser.Float_LA, i)

        def getRuleIndex(self):
            return NmrViewPKParser.RULE_widths

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWidths" ):
                listener.enterWidths(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWidths" ):
                listener.exitWidths(self)




    def widths(self):

        localctx = NmrViewPKParser.WidthsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_widths)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 51
                self.match(NmrViewPKParser.Float_LA)
                self.state = 54 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==29):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FreqsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Float_LA(self, i:int=None):
            if i is None:
                return self.getTokens(NmrViewPKParser.Float_LA)
            else:
                return self.getToken(NmrViewPKParser.Float_LA, i)

        def getRuleIndex(self):
            return NmrViewPKParser.RULE_freqs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFreqs" ):
                listener.enterFreqs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFreqs" ):
                listener.exitFreqs(self)




    def freqs(self):

        localctx = NmrViewPKParser.FreqsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_freqs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 56
                self.match(NmrViewPKParser.Float_LA)
                self.state = 59 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==29):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Vol(self):
            return self.getToken(NmrViewPKParser.Vol, 0)

        def Int(self):
            return self.getToken(NmrViewPKParser.Int, 0)

        def Stat(self):
            return self.getToken(NmrViewPKParser.Stat, 0)

        def Comment(self):
            return self.getToken(NmrViewPKParser.Comment, 0)

        def Flag0(self):
            return self.getToken(NmrViewPKParser.Flag0, 0)

        def vars_per_axis(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmrViewPKParser.Vars_per_axisContext)
            else:
                return self.getTypedRuleContext(NmrViewPKParser.Vars_per_axisContext,i)


        def getRuleIndex(self):
            return NmrViewPKParser.RULE_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars" ):
                listener.enterVars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars" ):
                listener.exitVars(self)




    def vars_(self):

        localctx = NmrViewPKParser.VarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 61
                self.vars_per_axis()
                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==16):
                    break

            self.state = 66
            self.match(NmrViewPKParser.Vol)
            self.state = 67
            self.match(NmrViewPKParser.Int)
            self.state = 68
            self.match(NmrViewPKParser.Stat)
            self.state = 69
            self.match(NmrViewPKParser.Comment)
            self.state = 70
            self.match(NmrViewPKParser.Flag0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vars_per_axisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_name(self):
            return self.getToken(NmrViewPKParser.L_name, 0)

        def P_name(self):
            return self.getToken(NmrViewPKParser.P_name, 0)

        def W_name(self):
            return self.getToken(NmrViewPKParser.W_name, 0)

        def B_name(self):
            return self.getToken(NmrViewPKParser.B_name, 0)

        def E_name(self):
            return self.getToken(NmrViewPKParser.E_name, 0)

        def J_name(self):
            return self.getToken(NmrViewPKParser.J_name, 0)

        def U_name(self):
            return self.getToken(NmrViewPKParser.U_name, 0)

        def getRuleIndex(self):
            return NmrViewPKParser.RULE_vars_per_axis

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars_per_axis" ):
                listener.enterVars_per_axis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars_per_axis" ):
                listener.exitVars_per_axis(self)




    def vars_per_axis(self):

        localctx = NmrViewPKParser.Vars_per_axisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vars_per_axis)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(NmrViewPKParser.L_name)
            self.state = 73
            self.match(NmrViewPKParser.P_name)
            self.state = 74
            self.match(NmrViewPKParser.W_name)
            self.state = 75
            self.match(NmrViewPKParser.B_name)
            self.state = 76
            self.match(NmrViewPKParser.E_name)
            self.state = 77
            self.match(NmrViewPKParser.J_name)
            self.state = 78
            self.match(NmrViewPKParser.U_name)
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

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(NmrViewPKParser.Integer)
            else:
                return self.getToken(NmrViewPKParser.Integer, i)

        def ENCLOSE_COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(NmrViewPKParser.ENCLOSE_COMMENT)
            else:
                return self.getToken(NmrViewPKParser.ENCLOSE_COMMENT, i)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(NmrViewPKParser.Float)
            else:
                return self.getToken(NmrViewPKParser.Float, i)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(NmrViewPKParser.Simple_name)
            else:
                return self.getToken(NmrViewPKParser.Simple_name, i)

        def getRuleIndex(self):
            return NmrViewPKParser.RULE_peak_list_2d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_list_2d" ):
                listener.enterPeak_list_2d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_list_2d" ):
                listener.exitPeak_list_2d(self)




    def peak_list_2d(self):

        localctx = NmrViewPKParser.Peak_list_2dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_peak_list_2d)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(NmrViewPKParser.Integer)
            self.state = 81
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 82
            self.match(NmrViewPKParser.Float)
            self.state = 83
            self.match(NmrViewPKParser.Float)
            self.state = 84
            self.match(NmrViewPKParser.Float)
            self.state = 85
            self.match(NmrViewPKParser.Simple_name)
            self.state = 86
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 87
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 88
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 89
            self.match(NmrViewPKParser.Float)
            self.state = 90
            self.match(NmrViewPKParser.Float)
            self.state = 91
            self.match(NmrViewPKParser.Float)
            self.state = 92
            self.match(NmrViewPKParser.Simple_name)
            self.state = 93
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 94
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 95
            self.match(NmrViewPKParser.Float)
            self.state = 96
            self.match(NmrViewPKParser.Float)
            self.state = 97
            self.match(NmrViewPKParser.Integer)
            self.state = 98
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 99
            self.match(NmrViewPKParser.Integer)
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

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(NmrViewPKParser.Integer)
            else:
                return self.getToken(NmrViewPKParser.Integer, i)

        def ENCLOSE_COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(NmrViewPKParser.ENCLOSE_COMMENT)
            else:
                return self.getToken(NmrViewPKParser.ENCLOSE_COMMENT, i)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(NmrViewPKParser.Float)
            else:
                return self.getToken(NmrViewPKParser.Float, i)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(NmrViewPKParser.Simple_name)
            else:
                return self.getToken(NmrViewPKParser.Simple_name, i)

        def getRuleIndex(self):
            return NmrViewPKParser.RULE_peak_list_3d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_list_3d" ):
                listener.enterPeak_list_3d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_list_3d" ):
                listener.exitPeak_list_3d(self)




    def peak_list_3d(self):

        localctx = NmrViewPKParser.Peak_list_3dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_peak_list_3d)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(NmrViewPKParser.Integer)
            self.state = 102
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 103
            self.match(NmrViewPKParser.Float)
            self.state = 104
            self.match(NmrViewPKParser.Float)
            self.state = 105
            self.match(NmrViewPKParser.Float)
            self.state = 106
            self.match(NmrViewPKParser.Simple_name)
            self.state = 107
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 108
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 109
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 110
            self.match(NmrViewPKParser.Float)
            self.state = 111
            self.match(NmrViewPKParser.Float)
            self.state = 112
            self.match(NmrViewPKParser.Float)
            self.state = 113
            self.match(NmrViewPKParser.Simple_name)
            self.state = 114
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 115
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 116
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 117
            self.match(NmrViewPKParser.Float)
            self.state = 118
            self.match(NmrViewPKParser.Float)
            self.state = 119
            self.match(NmrViewPKParser.Float)
            self.state = 120
            self.match(NmrViewPKParser.Simple_name)
            self.state = 121
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 122
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 123
            self.match(NmrViewPKParser.Float)
            self.state = 124
            self.match(NmrViewPKParser.Float)
            self.state = 125
            self.match(NmrViewPKParser.Integer)
            self.state = 126
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 127
            self.match(NmrViewPKParser.Integer)
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

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(NmrViewPKParser.Integer)
            else:
                return self.getToken(NmrViewPKParser.Integer, i)

        def ENCLOSE_COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(NmrViewPKParser.ENCLOSE_COMMENT)
            else:
                return self.getToken(NmrViewPKParser.ENCLOSE_COMMENT, i)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(NmrViewPKParser.Float)
            else:
                return self.getToken(NmrViewPKParser.Float, i)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(NmrViewPKParser.Simple_name)
            else:
                return self.getToken(NmrViewPKParser.Simple_name, i)

        def getRuleIndex(self):
            return NmrViewPKParser.RULE_peak_list_4d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_list_4d" ):
                listener.enterPeak_list_4d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_list_4d" ):
                listener.exitPeak_list_4d(self)




    def peak_list_4d(self):

        localctx = NmrViewPKParser.Peak_list_4dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_peak_list_4d)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(NmrViewPKParser.Integer)
            self.state = 130
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 131
            self.match(NmrViewPKParser.Float)
            self.state = 132
            self.match(NmrViewPKParser.Float)
            self.state = 133
            self.match(NmrViewPKParser.Float)
            self.state = 134
            self.match(NmrViewPKParser.Simple_name)
            self.state = 135
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 136
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 137
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 138
            self.match(NmrViewPKParser.Float)
            self.state = 139
            self.match(NmrViewPKParser.Float)
            self.state = 140
            self.match(NmrViewPKParser.Float)
            self.state = 141
            self.match(NmrViewPKParser.Simple_name)
            self.state = 142
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 143
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 144
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 145
            self.match(NmrViewPKParser.Float)
            self.state = 146
            self.match(NmrViewPKParser.Float)
            self.state = 147
            self.match(NmrViewPKParser.Float)
            self.state = 148
            self.match(NmrViewPKParser.Simple_name)
            self.state = 149
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 150
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 151
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 152
            self.match(NmrViewPKParser.Float)
            self.state = 153
            self.match(NmrViewPKParser.Float)
            self.state = 154
            self.match(NmrViewPKParser.Float)
            self.state = 155
            self.match(NmrViewPKParser.Simple_name)
            self.state = 156
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 157
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 158
            self.match(NmrViewPKParser.Float)
            self.state = 159
            self.match(NmrViewPKParser.Float)
            self.state = 160
            self.match(NmrViewPKParser.Integer)
            self.state = 161
            self.match(NmrViewPKParser.ENCLOSE_COMMENT)
            self.state = 162
            self.match(NmrViewPKParser.Integer)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





