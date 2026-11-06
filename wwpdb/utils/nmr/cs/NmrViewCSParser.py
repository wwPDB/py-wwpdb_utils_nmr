# Generated from NmrViewCSParser.g4 by ANTLR 4.13.0
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
        4,1,21,91,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,3,0,18,8,0,1,0,4,0,21,8,0,11,0,12,0,22,1,0,5,0,26,
        8,0,10,0,12,0,29,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,40,
        8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,49,8,1,11,1,12,1,50,1,1,1,1,
        3,1,55,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,4,4,65,8,4,11,4,12,4,
        66,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,3,7,78,8,7,1,7,1,7,1,7,5,
        7,83,8,7,10,7,12,7,86,9,7,1,7,3,7,89,8,7,1,7,0,0,8,0,2,4,6,8,10,
        12,14,0,1,1,1,16,16,93,0,17,1,0,0,0,2,32,1,0,0,0,4,56,1,0,0,0,6,
        59,1,0,0,0,8,62,1,0,0,0,10,68,1,0,0,0,12,71,1,0,0,0,14,74,1,0,0,
        0,16,18,5,16,0,0,17,16,1,0,0,0,17,18,1,0,0,0,18,20,1,0,0,0,19,21,
        3,2,1,0,20,19,1,0,0,0,21,22,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,
        23,27,1,0,0,0,24,26,5,16,0,0,25,24,1,0,0,0,26,29,1,0,0,0,27,25,1,
        0,0,0,27,28,1,0,0,0,28,30,1,0,0,0,29,27,1,0,0,0,30,31,5,0,0,1,31,
        1,1,0,0,0,32,33,3,4,2,0,33,34,5,16,0,0,34,35,3,6,3,0,35,39,5,16,
        0,0,36,37,3,8,4,0,37,38,5,16,0,0,38,40,1,0,0,0,39,36,1,0,0,0,39,
        40,1,0,0,0,40,41,1,0,0,0,41,42,3,10,5,0,42,43,5,16,0,0,43,44,3,12,
        6,0,44,48,5,16,0,0,45,46,3,14,7,0,46,47,5,16,0,0,47,49,1,0,0,0,48,
        45,1,0,0,0,49,50,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,52,1,0,0,
        0,52,54,5,10,0,0,53,55,7,0,0,0,54,53,1,0,0,0,54,55,1,0,0,0,55,3,
        1,0,0,0,56,57,5,5,0,0,57,58,5,1,0,0,58,5,1,0,0,0,59,60,5,6,0,0,60,
        61,5,14,0,0,61,7,1,0,0,0,62,64,5,7,0,0,63,65,5,11,0,0,64,63,1,0,
        0,0,65,66,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,9,1,0,0,0,68,69,
        5,8,0,0,69,70,5,1,0,0,70,11,1,0,0,0,71,72,5,9,0,0,72,73,5,1,0,0,
        73,13,1,0,0,0,74,75,5,14,0,0,75,77,5,2,0,0,76,78,5,2,0,0,77,76,1,
        0,0,0,77,78,1,0,0,0,78,88,1,0,0,0,79,89,5,12,0,0,80,84,5,13,0,0,
        81,83,5,19,0,0,82,81,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,
        0,0,0,85,87,1,0,0,0,86,84,1,0,0,0,87,89,5,20,0,0,88,79,1,0,0,0,88,
        80,1,0,0,0,88,89,1,0,0,0,89,15,1,0,0,0,10,17,22,27,39,50,54,66,77,
        84,88
    ]

class NmrViewCSParser ( Parser ):

    grammarFileName = "NmrViewCSParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'RES_ID'", "'RES_TYPE'", "'PREV_TYPE'", 
                     "'SPIN_SYSTEM_ID'", "'HETEROGENEITY'", "'END_RES_DEF'" ]

    symbolicNames = [ "<INVALID>", "Integer", "Float", "SHARP_COMMENT", 
                      "EXCLM_COMMENT", "Res_ID", "Res_Type", "Prev_Type", 
                      "Spin_System_ID", "Heterogeneity", "End_Res_Def", 
                      "Type_pred", "Single_note", "Note_begin", "Simple_name", 
                      "SPACE", "RETURN", "SECTION_COMMENT", "LINE_COMMENT", 
                      "Note_middle", "Note_end", "SPACE_MN" ]

    RULE_nmrview_cs = 0
    RULE_res_def_list = 1
    RULE_res_id_def = 2
    RULE_res_type_def = 3
    RULE_prev_type_def = 4
    RULE_spin_system_def = 5
    RULE_heterogeneity_def = 6
    RULE_shift_list = 7

    ruleNames =  [ "nmrview_cs", "res_def_list", "res_id_def", "res_type_def", 
                   "prev_type_def", "spin_system_def", "heterogeneity_def", 
                   "shift_list" ]

    EOF = Token.EOF
    Integer=1
    Float=2
    SHARP_COMMENT=3
    EXCLM_COMMENT=4
    Res_ID=5
    Res_Type=6
    Prev_Type=7
    Spin_System_ID=8
    Heterogeneity=9
    End_Res_Def=10
    Type_pred=11
    Single_note=12
    Note_begin=13
    Simple_name=14
    SPACE=15
    RETURN=16
    SECTION_COMMENT=17
    LINE_COMMENT=18
    Note_middle=19
    Note_end=20
    SPACE_MN=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Nmrview_csContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(NmrViewCSParser.EOF, 0)

        def RETURN(self, i:int=None):
            if i is None:
                return self.getTokens(NmrViewCSParser.RETURN)
            else:
                return self.getToken(NmrViewCSParser.RETURN, i)

        def res_def_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmrViewCSParser.Res_def_listContext)
            else:
                return self.getTypedRuleContext(NmrViewCSParser.Res_def_listContext,i)


        def getRuleIndex(self):
            return NmrViewCSParser.RULE_nmrview_cs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNmrview_cs" ):
                listener.enterNmrview_cs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNmrview_cs" ):
                listener.exitNmrview_cs(self)




    def nmrview_cs(self):

        localctx = NmrViewCSParser.Nmrview_csContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_nmrview_cs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 16
                self.match(NmrViewCSParser.RETURN)


            self.state = 20 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 19
                self.res_def_list()
                self.state = 22 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5):
                    break

            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 24
                self.match(NmrViewCSParser.RETURN)
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
            self.match(NmrViewCSParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Res_def_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def res_id_def(self):
            return self.getTypedRuleContext(NmrViewCSParser.Res_id_defContext,0)


        def RETURN(self, i:int=None):
            if i is None:
                return self.getTokens(NmrViewCSParser.RETURN)
            else:
                return self.getToken(NmrViewCSParser.RETURN, i)

        def res_type_def(self):
            return self.getTypedRuleContext(NmrViewCSParser.Res_type_defContext,0)


        def spin_system_def(self):
            return self.getTypedRuleContext(NmrViewCSParser.Spin_system_defContext,0)


        def heterogeneity_def(self):
            return self.getTypedRuleContext(NmrViewCSParser.Heterogeneity_defContext,0)


        def End_Res_Def(self):
            return self.getToken(NmrViewCSParser.End_Res_Def, 0)

        def prev_type_def(self):
            return self.getTypedRuleContext(NmrViewCSParser.Prev_type_defContext,0)


        def shift_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmrViewCSParser.Shift_listContext)
            else:
                return self.getTypedRuleContext(NmrViewCSParser.Shift_listContext,i)


        def EOF(self):
            return self.getToken(NmrViewCSParser.EOF, 0)

        def getRuleIndex(self):
            return NmrViewCSParser.RULE_res_def_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRes_def_list" ):
                listener.enterRes_def_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRes_def_list" ):
                listener.exitRes_def_list(self)




    def res_def_list(self):

        localctx = NmrViewCSParser.Res_def_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_res_def_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.res_id_def()
            self.state = 33
            self.match(NmrViewCSParser.RETURN)
            self.state = 34
            self.res_type_def()
            self.state = 35
            self.match(NmrViewCSParser.RETURN)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 36
                self.prev_type_def()
                self.state = 37
                self.match(NmrViewCSParser.RETURN)


            self.state = 41
            self.spin_system_def()
            self.state = 42
            self.match(NmrViewCSParser.RETURN)
            self.state = 43
            self.heterogeneity_def()
            self.state = 44
            self.match(NmrViewCSParser.RETURN)
            self.state = 48 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 45
                self.shift_list()
                self.state = 46
                self.match(NmrViewCSParser.RETURN)
                self.state = 50 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==14):
                    break

            self.state = 52
            self.match(NmrViewCSParser.End_Res_Def)
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 53
                _la = self._input.LA(1)
                if not(_la==-1 or _la==16):
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


    class Res_id_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Res_ID(self):
            return self.getToken(NmrViewCSParser.Res_ID, 0)

        def Integer(self):
            return self.getToken(NmrViewCSParser.Integer, 0)

        def getRuleIndex(self):
            return NmrViewCSParser.RULE_res_id_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRes_id_def" ):
                listener.enterRes_id_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRes_id_def" ):
                listener.exitRes_id_def(self)




    def res_id_def(self):

        localctx = NmrViewCSParser.Res_id_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_res_id_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(NmrViewCSParser.Res_ID)
            self.state = 57
            self.match(NmrViewCSParser.Integer)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Res_type_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Res_Type(self):
            return self.getToken(NmrViewCSParser.Res_Type, 0)

        def Simple_name(self):
            return self.getToken(NmrViewCSParser.Simple_name, 0)

        def getRuleIndex(self):
            return NmrViewCSParser.RULE_res_type_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRes_type_def" ):
                listener.enterRes_type_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRes_type_def" ):
                listener.exitRes_type_def(self)




    def res_type_def(self):

        localctx = NmrViewCSParser.Res_type_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_res_type_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(NmrViewCSParser.Res_Type)
            self.state = 60
            self.match(NmrViewCSParser.Simple_name)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prev_type_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Prev_Type(self):
            return self.getToken(NmrViewCSParser.Prev_Type, 0)

        def Type_pred(self, i:int=None):
            if i is None:
                return self.getTokens(NmrViewCSParser.Type_pred)
            else:
                return self.getToken(NmrViewCSParser.Type_pred, i)

        def getRuleIndex(self):
            return NmrViewCSParser.RULE_prev_type_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrev_type_def" ):
                listener.enterPrev_type_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrev_type_def" ):
                listener.exitPrev_type_def(self)




    def prev_type_def(self):

        localctx = NmrViewCSParser.Prev_type_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_prev_type_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(NmrViewCSParser.Prev_Type)
            self.state = 64 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 63
                self.match(NmrViewCSParser.Type_pred)
                self.state = 66 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==11):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Spin_system_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Spin_System_ID(self):
            return self.getToken(NmrViewCSParser.Spin_System_ID, 0)

        def Integer(self):
            return self.getToken(NmrViewCSParser.Integer, 0)

        def getRuleIndex(self):
            return NmrViewCSParser.RULE_spin_system_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpin_system_def" ):
                listener.enterSpin_system_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpin_system_def" ):
                listener.exitSpin_system_def(self)




    def spin_system_def(self):

        localctx = NmrViewCSParser.Spin_system_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_spin_system_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(NmrViewCSParser.Spin_System_ID)
            self.state = 69
            self.match(NmrViewCSParser.Integer)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Heterogeneity_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Heterogeneity(self):
            return self.getToken(NmrViewCSParser.Heterogeneity, 0)

        def Integer(self):
            return self.getToken(NmrViewCSParser.Integer, 0)

        def getRuleIndex(self):
            return NmrViewCSParser.RULE_heterogeneity_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeterogeneity_def" ):
                listener.enterHeterogeneity_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeterogeneity_def" ):
                listener.exitHeterogeneity_def(self)




    def heterogeneity_def(self):

        localctx = NmrViewCSParser.Heterogeneity_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_heterogeneity_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(NmrViewCSParser.Heterogeneity)
            self.state = 72
            self.match(NmrViewCSParser.Integer)
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
            return self.getToken(NmrViewCSParser.Simple_name, 0)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(NmrViewCSParser.Float)
            else:
                return self.getToken(NmrViewCSParser.Float, i)

        def Single_note(self):
            return self.getToken(NmrViewCSParser.Single_note, 0)

        def Note_begin(self):
            return self.getToken(NmrViewCSParser.Note_begin, 0)

        def Note_end(self):
            return self.getToken(NmrViewCSParser.Note_end, 0)

        def Note_middle(self, i:int=None):
            if i is None:
                return self.getTokens(NmrViewCSParser.Note_middle)
            else:
                return self.getToken(NmrViewCSParser.Note_middle, i)

        def getRuleIndex(self):
            return NmrViewCSParser.RULE_shift_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShift_list" ):
                listener.enterShift_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShift_list" ):
                listener.exitShift_list(self)




    def shift_list(self):

        localctx = NmrViewCSParser.Shift_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_shift_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(NmrViewCSParser.Simple_name)
            self.state = 75
            self.match(NmrViewCSParser.Float)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 76
                self.match(NmrViewCSParser.Float)


            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.state = 79
                self.match(NmrViewCSParser.Single_note)
                pass
            elif token in [13]:
                self.state = 80
                self.match(NmrViewCSParser.Note_begin)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==19:
                    self.state = 81
                    self.match(NmrViewCSParser.Note_middle)
                    self.state = 86
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 87
                self.match(NmrViewCSParser.Note_end)
                pass
            elif token in [16]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





