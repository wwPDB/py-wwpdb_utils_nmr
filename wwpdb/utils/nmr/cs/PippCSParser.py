# Generated from PippCSParser.g4 by ANTLR 4.13.0
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
        4,1,34,125,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,3,0,16,8,0,1,0,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,
        1,1,1,1,3,1,30,8,1,1,1,1,1,1,1,3,1,35,8,1,1,1,3,1,38,8,1,1,1,4,1,
        41,8,1,11,1,12,1,42,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,4,2,53,8,2,11,
        2,12,2,54,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,5,4,71,8,4,10,4,12,4,74,9,4,1,4,3,4,77,8,4,1,4,1,4,5,4,81,8,4,
        10,4,12,4,84,9,4,1,4,3,4,87,8,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,95,8,
        4,1,4,5,4,98,8,4,10,4,12,4,101,9,4,1,4,1,4,1,4,1,5,1,5,1,5,3,5,109,
        8,5,1,5,1,5,5,5,113,8,5,10,5,12,5,116,9,5,1,5,3,5,119,8,5,1,5,1,
        5,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,3,2,0,5,5,24,24,1,1,21,21,
        1,0,14,15,134,0,15,1,0,0,0,2,29,1,0,0,0,4,44,1,0,0,0,6,56,1,0,0,
        0,8,62,1,0,0,0,10,105,1,0,0,0,12,122,1,0,0,0,14,16,5,21,0,0,15,14,
        1,0,0,0,15,16,1,0,0,0,16,21,1,0,0,0,17,20,3,2,1,0,18,20,5,21,0,0,
        19,17,1,0,0,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,
        0,0,0,22,24,1,0,0,0,23,21,1,0,0,0,24,25,5,0,0,1,25,1,1,0,0,0,26,
        27,5,1,0,0,27,28,5,2,0,0,28,30,5,21,0,0,29,26,1,0,0,0,29,30,1,0,
        0,0,30,34,1,0,0,0,31,32,5,3,0,0,32,33,5,14,0,0,33,35,5,21,0,0,34,
        31,1,0,0,0,34,35,1,0,0,0,35,37,1,0,0,0,36,38,3,4,2,0,37,36,1,0,0,
        0,37,38,1,0,0,0,38,40,1,0,0,0,39,41,3,8,4,0,40,39,1,0,0,0,41,42,
        1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,3,1,0,0,0,44,45,5,4,0,0,45,
        46,5,31,0,0,46,47,5,25,0,0,47,48,5,26,0,0,48,49,5,27,0,0,49,50,5,
        28,0,0,50,52,5,31,0,0,51,53,3,6,3,0,52,51,1,0,0,0,53,54,1,0,0,0,
        54,52,1,0,0,0,54,55,1,0,0,0,55,5,1,0,0,0,56,57,5,29,0,0,57,58,5,
        29,0,0,58,59,5,29,0,0,59,60,5,29,0,0,60,61,5,31,0,0,61,7,1,0,0,0,
        62,63,7,0,0,0,63,64,5,14,0,0,64,65,5,21,0,0,65,66,5,6,0,0,66,67,
        5,18,0,0,67,76,5,21,0,0,68,72,5,7,0,0,69,71,5,12,0,0,70,69,1,0,0,
        0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,75,1,0,0,0,74,72,
        1,0,0,0,75,77,5,21,0,0,76,68,1,0,0,0,76,77,1,0,0,0,77,86,1,0,0,0,
        78,82,5,8,0,0,79,81,5,12,0,0,80,79,1,0,0,0,81,84,1,0,0,0,82,80,1,
        0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,82,1,0,0,0,85,87,5,21,0,0,86,
        78,1,0,0,0,86,87,1,0,0,0,87,88,1,0,0,0,88,89,5,9,0,0,89,90,5,14,
        0,0,90,94,5,21,0,0,91,92,5,10,0,0,92,93,5,14,0,0,93,95,5,21,0,0,
        94,91,1,0,0,0,94,95,1,0,0,0,95,99,1,0,0,0,96,98,3,10,5,0,97,96,1,
        0,0,0,98,101,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,102,1,0,0,
        0,101,99,1,0,0,0,102,103,5,11,0,0,103,104,7,1,0,0,104,9,1,0,0,0,
        105,106,5,18,0,0,106,108,3,12,6,0,107,109,3,12,6,0,108,107,1,0,0,
        0,108,109,1,0,0,0,109,118,1,0,0,0,110,114,5,13,0,0,111,113,5,32,
        0,0,112,111,1,0,0,0,113,116,1,0,0,0,114,112,1,0,0,0,114,115,1,0,
        0,0,115,117,1,0,0,0,116,114,1,0,0,0,117,119,5,33,0,0,118,110,1,0,
        0,0,118,119,1,0,0,0,119,120,1,0,0,0,120,121,5,21,0,0,121,11,1,0,
        0,0,122,123,7,2,0,0,123,13,1,0,0,0,17,15,19,21,29,34,37,42,54,72,
        76,82,86,94,99,108,114,118
    ]

class PippCSParser ( Parser ):

    grammarFileName = "PippCSParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'SHIFT_FL_FRMT'", "'RES_SIAD'", "'FIRST_RES_IN_SEQ'", 
                     "'EXP_PEAK_PICK_TBL'", "<INVALID>", "'RES_TYPE'", "'PREV_TYPE'", 
                     "'CUR_TYPE'", "'SPIN_SYSTEM_ID'", "'HETEROGENEITY'", 
                     "'END_RES_DEF'", "<INVALID>", "'('", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'Label'", "'Exp Par Fl'", "'Peak-Pick Fl'", 
                     "'#-Cross-Ref'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "')'" ]

    symbolicNames = [ "<INVALID>", "Shift_fl_frmt", "Res_siad", "First_res_in_seq", 
                      "Exp_peak_pick_tbl", "Res_ID", "Res_type", "Prev_type", 
                      "Cur_type", "Spin_system_ID", "Heterogeneity", "End_res_def", 
                      "Type_pred", "Note_begin", "Integer", "Float", "SHARP_COMMENT", 
                      "EXCLM_COMMENT", "Simple_name", "CONTINUE", "SPACE", 
                      "RETURN", "SECTION_COMMENT", "LINE_COMMENT", "Res_ID_", 
                      "Label", "Exp_par_fl", "Peak_pick_fl", "Cross_ref", 
                      "Simple_name_ET", "SPACE_ET", "RETURN_ET", "Note", 
                      "Note_end", "SPACE_MN" ]

    RULE_pipp_cs = 0
    RULE_pipp_format = 1
    RULE_ext_peak_pick_tbl = 2
    RULE_ext_peak_pick_tbl_row = 3
    RULE_residue_list = 4
    RULE_shift_list = 5
    RULE_number = 6

    ruleNames =  [ "pipp_cs", "pipp_format", "ext_peak_pick_tbl", "ext_peak_pick_tbl_row", 
                   "residue_list", "shift_list", "number" ]

    EOF = Token.EOF
    Shift_fl_frmt=1
    Res_siad=2
    First_res_in_seq=3
    Exp_peak_pick_tbl=4
    Res_ID=5
    Res_type=6
    Prev_type=7
    Cur_type=8
    Spin_system_ID=9
    Heterogeneity=10
    End_res_def=11
    Type_pred=12
    Note_begin=13
    Integer=14
    Float=15
    SHARP_COMMENT=16
    EXCLM_COMMENT=17
    Simple_name=18
    CONTINUE=19
    SPACE=20
    RETURN=21
    SECTION_COMMENT=22
    LINE_COMMENT=23
    Res_ID_=24
    Label=25
    Exp_par_fl=26
    Peak_pick_fl=27
    Cross_ref=28
    Simple_name_ET=29
    SPACE_ET=30
    RETURN_ET=31
    Note=32
    Note_end=33
    SPACE_MN=34

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Pipp_csContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PippCSParser.EOF, 0)

        def RETURN(self, i:int=None):
            if i is None:
                return self.getTokens(PippCSParser.RETURN)
            else:
                return self.getToken(PippCSParser.RETURN, i)

        def pipp_format(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PippCSParser.Pipp_formatContext)
            else:
                return self.getTypedRuleContext(PippCSParser.Pipp_formatContext,i)


        def getRuleIndex(self):
            return PippCSParser.RULE_pipp_cs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPipp_cs" ):
                listener.enterPipp_cs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPipp_cs" ):
                listener.exitPipp_cs(self)




    def pipp_cs(self):

        localctx = PippCSParser.Pipp_csContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_pipp_cs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 14
                self.match(PippCSParser.RETURN)


            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 18874426) != 0):
                self.state = 19
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 3, 4, 5, 24]:
                    self.state = 17
                    self.pipp_format()
                    pass
                elif token in [21]:
                    self.state = 18
                    self.match(PippCSParser.RETURN)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(PippCSParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pipp_formatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Shift_fl_frmt(self):
            return self.getToken(PippCSParser.Shift_fl_frmt, 0)

        def Res_siad(self):
            return self.getToken(PippCSParser.Res_siad, 0)

        def RETURN(self, i:int=None):
            if i is None:
                return self.getTokens(PippCSParser.RETURN)
            else:
                return self.getToken(PippCSParser.RETURN, i)

        def First_res_in_seq(self):
            return self.getToken(PippCSParser.First_res_in_seq, 0)

        def Integer(self):
            return self.getToken(PippCSParser.Integer, 0)

        def ext_peak_pick_tbl(self):
            return self.getTypedRuleContext(PippCSParser.Ext_peak_pick_tblContext,0)


        def residue_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PippCSParser.Residue_listContext)
            else:
                return self.getTypedRuleContext(PippCSParser.Residue_listContext,i)


        def getRuleIndex(self):
            return PippCSParser.RULE_pipp_format

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPipp_format" ):
                listener.enterPipp_format(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPipp_format" ):
                listener.exitPipp_format(self)




    def pipp_format(self):

        localctx = PippCSParser.Pipp_formatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_pipp_format)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 26
                self.match(PippCSParser.Shift_fl_frmt)
                self.state = 27
                self.match(PippCSParser.Res_siad)
                self.state = 28
                self.match(PippCSParser.RETURN)


            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 31
                self.match(PippCSParser.First_res_in_seq)
                self.state = 32
                self.match(PippCSParser.Integer)
                self.state = 33
                self.match(PippCSParser.RETURN)


            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 36
                self.ext_peak_pick_tbl()


            self.state = 40 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 39
                    self.residue_list()

                else:
                    raise NoViableAltException(self)
                self.state = 42 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ext_peak_pick_tblContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Exp_peak_pick_tbl(self):
            return self.getToken(PippCSParser.Exp_peak_pick_tbl, 0)

        def RETURN_ET(self, i:int=None):
            if i is None:
                return self.getTokens(PippCSParser.RETURN_ET)
            else:
                return self.getToken(PippCSParser.RETURN_ET, i)

        def Label(self):
            return self.getToken(PippCSParser.Label, 0)

        def Exp_par_fl(self):
            return self.getToken(PippCSParser.Exp_par_fl, 0)

        def Peak_pick_fl(self):
            return self.getToken(PippCSParser.Peak_pick_fl, 0)

        def Cross_ref(self):
            return self.getToken(PippCSParser.Cross_ref, 0)

        def ext_peak_pick_tbl_row(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PippCSParser.Ext_peak_pick_tbl_rowContext)
            else:
                return self.getTypedRuleContext(PippCSParser.Ext_peak_pick_tbl_rowContext,i)


        def getRuleIndex(self):
            return PippCSParser.RULE_ext_peak_pick_tbl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExt_peak_pick_tbl" ):
                listener.enterExt_peak_pick_tbl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExt_peak_pick_tbl" ):
                listener.exitExt_peak_pick_tbl(self)




    def ext_peak_pick_tbl(self):

        localctx = PippCSParser.Ext_peak_pick_tblContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ext_peak_pick_tbl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(PippCSParser.Exp_peak_pick_tbl)
            self.state = 45
            self.match(PippCSParser.RETURN_ET)
            self.state = 46
            self.match(PippCSParser.Label)
            self.state = 47
            self.match(PippCSParser.Exp_par_fl)
            self.state = 48
            self.match(PippCSParser.Peak_pick_fl)
            self.state = 49
            self.match(PippCSParser.Cross_ref)
            self.state = 50
            self.match(PippCSParser.RETURN_ET)
            self.state = 52 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 51
                self.ext_peak_pick_tbl_row()
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


    class Ext_peak_pick_tbl_rowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Simple_name_ET(self, i:int=None):
            if i is None:
                return self.getTokens(PippCSParser.Simple_name_ET)
            else:
                return self.getToken(PippCSParser.Simple_name_ET, i)

        def RETURN_ET(self):
            return self.getToken(PippCSParser.RETURN_ET, 0)

        def getRuleIndex(self):
            return PippCSParser.RULE_ext_peak_pick_tbl_row

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExt_peak_pick_tbl_row" ):
                listener.enterExt_peak_pick_tbl_row(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExt_peak_pick_tbl_row" ):
                listener.exitExt_peak_pick_tbl_row(self)




    def ext_peak_pick_tbl_row(self):

        localctx = PippCSParser.Ext_peak_pick_tbl_rowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ext_peak_pick_tbl_row)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(PippCSParser.Simple_name_ET)
            self.state = 57
            self.match(PippCSParser.Simple_name_ET)
            self.state = 58
            self.match(PippCSParser.Simple_name_ET)
            self.state = 59
            self.match(PippCSParser.Simple_name_ET)
            self.state = 60
            self.match(PippCSParser.RETURN_ET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Residue_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(PippCSParser.Integer)
            else:
                return self.getToken(PippCSParser.Integer, i)

        def RETURN(self, i:int=None):
            if i is None:
                return self.getTokens(PippCSParser.RETURN)
            else:
                return self.getToken(PippCSParser.RETURN, i)

        def Res_type(self):
            return self.getToken(PippCSParser.Res_type, 0)

        def Simple_name(self):
            return self.getToken(PippCSParser.Simple_name, 0)

        def Spin_system_ID(self):
            return self.getToken(PippCSParser.Spin_system_ID, 0)

        def End_res_def(self):
            return self.getToken(PippCSParser.End_res_def, 0)

        def Res_ID(self):
            return self.getToken(PippCSParser.Res_ID, 0)

        def Res_ID_(self):
            return self.getToken(PippCSParser.Res_ID_, 0)

        def EOF(self):
            return self.getToken(PippCSParser.EOF, 0)

        def Prev_type(self):
            return self.getToken(PippCSParser.Prev_type, 0)

        def Cur_type(self):
            return self.getToken(PippCSParser.Cur_type, 0)

        def Heterogeneity(self):
            return self.getToken(PippCSParser.Heterogeneity, 0)

        def shift_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PippCSParser.Shift_listContext)
            else:
                return self.getTypedRuleContext(PippCSParser.Shift_listContext,i)


        def Type_pred(self, i:int=None):
            if i is None:
                return self.getTokens(PippCSParser.Type_pred)
            else:
                return self.getToken(PippCSParser.Type_pred, i)

        def getRuleIndex(self):
            return PippCSParser.RULE_residue_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResidue_list" ):
                listener.enterResidue_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResidue_list" ):
                listener.exitResidue_list(self)




    def residue_list(self):

        localctx = PippCSParser.Residue_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_residue_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            _la = self._input.LA(1)
            if not(_la==5 or _la==24):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 63
            self.match(PippCSParser.Integer)
            self.state = 64
            self.match(PippCSParser.RETURN)
            self.state = 65
            self.match(PippCSParser.Res_type)
            self.state = 66
            self.match(PippCSParser.Simple_name)
            self.state = 67
            self.match(PippCSParser.RETURN)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 68
                self.match(PippCSParser.Prev_type)
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==12:
                    self.state = 69
                    self.match(PippCSParser.Type_pred)
                    self.state = 74
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 75
                self.match(PippCSParser.RETURN)


            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 78
                self.match(PippCSParser.Cur_type)
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==12:
                    self.state = 79
                    self.match(PippCSParser.Type_pred)
                    self.state = 84
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 85
                self.match(PippCSParser.RETURN)


            self.state = 88
            self.match(PippCSParser.Spin_system_ID)
            self.state = 89
            self.match(PippCSParser.Integer)
            self.state = 90
            self.match(PippCSParser.RETURN)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 91
                self.match(PippCSParser.Heterogeneity)
                self.state = 92
                self.match(PippCSParser.Integer)
                self.state = 93
                self.match(PippCSParser.RETURN)


            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 96
                self.shift_list()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 102
            self.match(PippCSParser.End_res_def)
            self.state = 103
            _la = self._input.LA(1)
            if not(_la==-1 or _la==21):
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


    class Shift_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Simple_name(self):
            return self.getToken(PippCSParser.Simple_name, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PippCSParser.NumberContext)
            else:
                return self.getTypedRuleContext(PippCSParser.NumberContext,i)


        def RETURN(self):
            return self.getToken(PippCSParser.RETURN, 0)

        def Note_begin(self):
            return self.getToken(PippCSParser.Note_begin, 0)

        def Note_end(self):
            return self.getToken(PippCSParser.Note_end, 0)

        def Note(self, i:int=None):
            if i is None:
                return self.getTokens(PippCSParser.Note)
            else:
                return self.getToken(PippCSParser.Note, i)

        def getRuleIndex(self):
            return PippCSParser.RULE_shift_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShift_list" ):
                listener.enterShift_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShift_list" ):
                listener.exitShift_list(self)




    def shift_list(self):

        localctx = PippCSParser.Shift_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_shift_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(PippCSParser.Simple_name)
            self.state = 106
            self.number()
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14 or _la==15:
                self.state = 107
                self.number()


            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 110
                self.match(PippCSParser.Note_begin)
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==32:
                    self.state = 111
                    self.match(PippCSParser.Note)
                    self.state = 116
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 117
                self.match(PippCSParser.Note_end)


            self.state = 120
            self.match(PippCSParser.RETURN)
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
            return self.getToken(PippCSParser.Float, 0)

        def Integer(self):
            return self.getToken(PippCSParser.Integer, 0)

        def getRuleIndex(self):
            return PippCSParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = PippCSParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            _la = self._input.LA(1)
            if not(_la==14 or _la==15):
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





