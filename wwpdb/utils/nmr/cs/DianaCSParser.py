# Generated from DianaCSParser.g4 by ANTLR 4.13.0
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
        4,1,13,53,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,5,0,13,
        8,0,10,0,12,0,16,9,0,1,0,1,0,1,1,1,1,5,1,22,8,1,10,1,12,1,25,9,1,
        1,1,1,1,1,2,4,2,30,8,2,11,2,12,2,31,1,3,1,3,1,3,1,3,4,3,38,8,3,11,
        3,12,3,39,1,3,3,3,43,8,3,1,3,3,3,46,8,3,1,4,1,4,1,4,3,4,51,8,4,1,
        4,0,0,5,0,2,4,6,8,0,1,1,1,13,13,55,0,14,1,0,0,0,2,19,1,0,0,0,4,29,
        1,0,0,0,6,33,1,0,0,0,8,47,1,0,0,0,10,13,3,2,1,0,11,13,3,4,2,0,12,
        10,1,0,0,0,12,11,1,0,0,0,13,16,1,0,0,0,14,12,1,0,0,0,14,15,1,0,0,
        0,15,17,1,0,0,0,16,14,1,0,0,0,17,18,5,0,0,1,18,1,1,0,0,0,19,23,5,
        4,0,0,20,22,5,11,0,0,21,20,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,
        24,1,0,0,0,24,26,1,0,0,0,25,23,1,0,0,0,26,27,7,0,0,0,27,3,1,0,0,
        0,28,30,3,6,3,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,
        1,0,0,0,32,5,1,0,0,0,33,34,5,5,0,0,34,35,5,6,0,0,35,37,5,1,0,0,36,
        38,3,8,4,0,37,36,1,0,0,0,38,39,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,
        0,40,42,1,0,0,0,41,43,5,6,0,0,42,41,1,0,0,0,42,43,1,0,0,0,43,45,
        1,0,0,0,44,46,5,1,0,0,45,44,1,0,0,0,45,46,1,0,0,0,46,7,1,0,0,0,47,
        48,5,6,0,0,48,50,5,2,0,0,49,51,5,2,0,0,50,49,1,0,0,0,50,51,1,0,0,
        0,51,9,1,0,0,0,8,12,14,23,31,39,42,45,50
    ]

class DianaCSParser ( Parser ):

    grammarFileName = "DianaCSParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'SHIFTS'" ]

    symbolicNames = [ "<INVALID>", "Integer", "Float", "SMCLN_COMMENT", 
                      "COMMENT", "Shifts", "Simple_name", "SPACE", "ENCLOSE_COMMENT", 
                      "SECTION_COMMENT", "LINE_COMMENT", "Any_name", "SPACE_CM", 
                      "RETURN_CM" ]

    RULE_diana_cs = 0
    RULE_comment = 1
    RULE_chemical_shifts = 2
    RULE_chemical_shift = 3
    RULE_atom_chemical_shift = 4

    ruleNames =  [ "diana_cs", "comment", "chemical_shifts", "chemical_shift", 
                   "atom_chemical_shift" ]

    EOF = Token.EOF
    Integer=1
    Float=2
    SMCLN_COMMENT=3
    COMMENT=4
    Shifts=5
    Simple_name=6
    SPACE=7
    ENCLOSE_COMMENT=8
    SECTION_COMMENT=9
    LINE_COMMENT=10
    Any_name=11
    SPACE_CM=12
    RETURN_CM=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Diana_csContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(DianaCSParser.EOF, 0)

        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DianaCSParser.CommentContext)
            else:
                return self.getTypedRuleContext(DianaCSParser.CommentContext,i)


        def chemical_shifts(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DianaCSParser.Chemical_shiftsContext)
            else:
                return self.getTypedRuleContext(DianaCSParser.Chemical_shiftsContext,i)


        def getRuleIndex(self):
            return DianaCSParser.RULE_diana_cs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiana_cs" ):
                listener.enterDiana_cs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiana_cs" ):
                listener.exitDiana_cs(self)




    def diana_cs(self):

        localctx = DianaCSParser.Diana_csContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_diana_cs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4 or _la==5:
                self.state = 12
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 10
                    self.comment()
                    pass
                elif token in [5]:
                    self.state = 11
                    self.chemical_shifts()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 17
            self.match(DianaCSParser.EOF)
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
            return self.getToken(DianaCSParser.COMMENT, 0)

        def RETURN_CM(self):
            return self.getToken(DianaCSParser.RETURN_CM, 0)

        def EOF(self):
            return self.getToken(DianaCSParser.EOF, 0)

        def Any_name(self, i:int=None):
            if i is None:
                return self.getTokens(DianaCSParser.Any_name)
            else:
                return self.getToken(DianaCSParser.Any_name, i)

        def getRuleIndex(self):
            return DianaCSParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = DianaCSParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(DianaCSParser.COMMENT)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 20
                self.match(DianaCSParser.Any_name)
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            _la = self._input.LA(1)
            if not(_la==-1 or _la==13):
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


    class Chemical_shiftsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def chemical_shift(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DianaCSParser.Chemical_shiftContext)
            else:
                return self.getTypedRuleContext(DianaCSParser.Chemical_shiftContext,i)


        def getRuleIndex(self):
            return DianaCSParser.RULE_chemical_shifts

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChemical_shifts" ):
                listener.enterChemical_shifts(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChemical_shifts" ):
                listener.exitChemical_shifts(self)




    def chemical_shifts(self):

        localctx = DianaCSParser.Chemical_shiftsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_chemical_shifts)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 28
                    self.chemical_shift()

                else:
                    raise NoViableAltException(self)
                self.state = 31 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Chemical_shiftContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Shifts(self):
            return self.getToken(DianaCSParser.Shifts, 0)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(DianaCSParser.Simple_name)
            else:
                return self.getToken(DianaCSParser.Simple_name, i)

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(DianaCSParser.Integer)
            else:
                return self.getToken(DianaCSParser.Integer, i)

        def atom_chemical_shift(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DianaCSParser.Atom_chemical_shiftContext)
            else:
                return self.getTypedRuleContext(DianaCSParser.Atom_chemical_shiftContext,i)


        def getRuleIndex(self):
            return DianaCSParser.RULE_chemical_shift

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChemical_shift" ):
                listener.enterChemical_shift(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChemical_shift" ):
                listener.exitChemical_shift(self)




    def chemical_shift(self):

        localctx = DianaCSParser.Chemical_shiftContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_chemical_shift)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(DianaCSParser.Shifts)
            self.state = 34
            self.match(DianaCSParser.Simple_name)
            self.state = 35
            self.match(DianaCSParser.Integer)
            self.state = 37 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 36
                    self.atom_chemical_shift()

                else:
                    raise NoViableAltException(self)
                self.state = 39 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 41
                self.match(DianaCSParser.Simple_name)


            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 44
                self.match(DianaCSParser.Integer)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atom_chemical_shiftContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Simple_name(self):
            return self.getToken(DianaCSParser.Simple_name, 0)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(DianaCSParser.Float)
            else:
                return self.getToken(DianaCSParser.Float, i)

        def getRuleIndex(self):
            return DianaCSParser.RULE_atom_chemical_shift

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom_chemical_shift" ):
                listener.enterAtom_chemical_shift(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom_chemical_shift" ):
                listener.exitAtom_chemical_shift(self)




    def atom_chemical_shift(self):

        localctx = DianaCSParser.Atom_chemical_shiftContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atom_chemical_shift)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(DianaCSParser.Simple_name)
            self.state = 48
            self.match(DianaCSParser.Float)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 49
                self.match(DianaCSParser.Float)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





