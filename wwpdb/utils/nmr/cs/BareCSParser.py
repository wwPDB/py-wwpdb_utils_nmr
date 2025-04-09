# Generated from BareCSParser.g4 by ANTLR 4.13.0
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
        4,1,9,41,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,3,0,10,8,0,1,0,1,0,
        5,0,14,8,0,10,0,12,0,17,9,0,1,0,1,0,1,1,4,1,22,8,1,11,1,12,1,23,
        1,1,1,1,4,1,28,8,1,11,1,12,1,29,1,2,4,2,33,8,2,11,2,12,2,34,1,2,
        1,2,1,3,1,3,1,3,0,0,4,0,2,4,6,0,2,1,1,7,7,2,0,1,2,5,5,42,0,9,1,0,
        0,0,2,21,1,0,0,0,4,32,1,0,0,0,6,38,1,0,0,0,8,10,5,7,0,0,9,8,1,0,
        0,0,9,10,1,0,0,0,10,15,1,0,0,0,11,14,3,2,1,0,12,14,5,7,0,0,13,11,
        1,0,0,0,13,12,1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,
        16,18,1,0,0,0,17,15,1,0,0,0,18,19,5,0,0,1,19,1,1,0,0,0,20,22,5,5,
        0,0,21,20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,25,
        1,0,0,0,25,27,5,7,0,0,26,28,3,4,2,0,27,26,1,0,0,0,28,29,1,0,0,0,
        29,27,1,0,0,0,29,30,1,0,0,0,30,3,1,0,0,0,31,33,3,6,3,0,32,31,1,0,
        0,0,33,34,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,36,1,0,0,0,36,37,
        7,0,0,0,37,5,1,0,0,0,38,39,7,1,0,0,39,7,1,0,0,0,6,9,13,15,23,29,
        34
    ]

class BareCSParser ( Parser ):

    grammarFileName = "BareCSParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "Integer", "Float", "SHARP_COMMENT", 
                      "EXCLM_COMMENT", "Simple_name", "SPACE", "RETURN", 
                      "SECTION_COMMENT", "LINE_COMMENT" ]

    RULE_bare_cs = 0
    RULE_cs_raw_format = 1
    RULE_cs_raw_list = 2
    RULE_any = 3

    ruleNames =  [ "bare_cs", "cs_raw_format", "cs_raw_list", "any" ]

    EOF = Token.EOF
    Integer=1
    Float=2
    SHARP_COMMENT=3
    EXCLM_COMMENT=4
    Simple_name=5
    SPACE=6
    RETURN=7
    SECTION_COMMENT=8
    LINE_COMMENT=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Bare_csContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BareCSParser.EOF, 0)

        def RETURN(self, i:int=None):
            if i is None:
                return self.getTokens(BareCSParser.RETURN)
            else:
                return self.getToken(BareCSParser.RETURN, i)

        def cs_raw_format(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BareCSParser.Cs_raw_formatContext)
            else:
                return self.getTypedRuleContext(BareCSParser.Cs_raw_formatContext,i)


        def getRuleIndex(self):
            return BareCSParser.RULE_bare_cs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBare_cs" ):
                listener.enterBare_cs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBare_cs" ):
                listener.exitBare_cs(self)




    def bare_cs(self):

        localctx = BareCSParser.Bare_csContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_bare_cs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 8
                self.match(BareCSParser.RETURN)


            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==7:
                self.state = 13
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [5]:
                    self.state = 11
                    self.cs_raw_format()
                    pass
                elif token in [7]:
                    self.state = 12
                    self.match(BareCSParser.RETURN)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
            self.match(BareCSParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cs_raw_formatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BareCSParser.RETURN, 0)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(BareCSParser.Simple_name)
            else:
                return self.getToken(BareCSParser.Simple_name, i)

        def cs_raw_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BareCSParser.Cs_raw_listContext)
            else:
                return self.getTypedRuleContext(BareCSParser.Cs_raw_listContext,i)


        def getRuleIndex(self):
            return BareCSParser.RULE_cs_raw_format

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCs_raw_format" ):
                listener.enterCs_raw_format(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCs_raw_format" ):
                listener.exitCs_raw_format(self)




    def cs_raw_format(self):

        localctx = BareCSParser.Cs_raw_formatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_cs_raw_format)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.match(BareCSParser.Simple_name)
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5):
                    break

            self.state = 25
            self.match(BareCSParser.RETURN)
            self.state = 27 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 26
                    self.cs_raw_list()

                else:
                    raise NoViableAltException(self)
                self.state = 29 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cs_raw_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BareCSParser.RETURN, 0)

        def EOF(self):
            return self.getToken(BareCSParser.EOF, 0)

        def any_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BareCSParser.AnyContext)
            else:
                return self.getTypedRuleContext(BareCSParser.AnyContext,i)


        def getRuleIndex(self):
            return BareCSParser.RULE_cs_raw_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCs_raw_list" ):
                listener.enterCs_raw_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCs_raw_list" ):
                listener.exitCs_raw_list(self)




    def cs_raw_list(self):

        localctx = BareCSParser.Cs_raw_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_cs_raw_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 31
                self.any_()
                self.state = 34 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 38) != 0)):
                    break

            self.state = 36
            _la = self._input.LA(1)
            if not(_la==-1 or _la==7):
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


    class AnyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Float(self):
            return self.getToken(BareCSParser.Float, 0)

        def Integer(self):
            return self.getToken(BareCSParser.Integer, 0)

        def Simple_name(self):
            return self.getToken(BareCSParser.Simple_name, 0)

        def getRuleIndex(self):
            return BareCSParser.RULE_any

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAny" ):
                listener.enterAny(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAny" ):
                listener.exitAny(self)




    def any_(self):

        localctx = BareCSParser.AnyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_any)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 38) != 0)):
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





