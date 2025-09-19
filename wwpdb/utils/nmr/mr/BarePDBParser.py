# Generated from BarePDBParser.g4 by ANTLR 4.13.0
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
        4,1,17,63,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,3,0,12,8,0,
        1,0,1,0,1,0,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,0,1,0,1,1,1,1,5,1,
        27,8,1,10,1,12,1,30,9,1,1,1,1,1,1,2,4,2,35,8,2,11,2,12,2,36,1,3,
        1,3,1,3,1,3,1,3,3,3,44,8,3,1,3,1,3,3,3,48,8,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,4,1,4,1,4,3,4,61,8,4,1,4,0,0,5,0,2,4,6,8,0,1,1,1,
        17,17,67,0,11,1,0,0,0,2,24,1,0,0,0,4,34,1,0,0,0,6,38,1,0,0,0,8,60,
        1,0,0,0,10,12,5,10,0,0,11,10,1,0,0,0,11,12,1,0,0,0,12,19,1,0,0,0,
        13,18,3,2,1,0,14,18,3,4,2,0,15,18,3,8,4,0,16,18,5,10,0,0,17,13,1,
        0,0,0,17,14,1,0,0,0,17,15,1,0,0,0,17,16,1,0,0,0,18,21,1,0,0,0,19,
        17,1,0,0,0,19,20,1,0,0,0,20,22,1,0,0,0,21,19,1,0,0,0,22,23,5,0,0,
        1,23,1,1,0,0,0,24,28,5,4,0,0,25,27,5,15,0,0,26,25,1,0,0,0,27,30,
        1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,29,31,1,0,0,0,30,28,1,0,0,0,
        31,32,7,0,0,0,32,3,1,0,0,0,33,35,3,6,3,0,34,33,1,0,0,0,35,36,1,0,
        0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,5,1,0,0,0,38,39,5,5,0,0,39,40,
        5,1,0,0,40,41,5,8,0,0,41,47,5,8,0,0,42,44,5,8,0,0,43,42,1,0,0,0,
        43,44,1,0,0,0,44,45,1,0,0,0,45,48,5,1,0,0,46,48,5,8,0,0,47,43,1,
        0,0,0,47,46,1,0,0,0,48,49,1,0,0,0,49,50,5,2,0,0,50,51,5,2,0,0,51,
        52,5,2,0,0,52,53,5,2,0,0,53,54,5,2,0,0,54,55,5,8,0,0,55,56,5,10,
        0,0,56,7,1,0,0,0,57,58,5,6,0,0,58,61,5,10,0,0,59,61,5,7,0,0,60,57,
        1,0,0,0,60,59,1,0,0,0,61,9,1,0,0,0,8,11,17,19,28,36,43,47,60
    ]

class BarePDBParser ( Parser ):

    grammarFileName = "BarePDBParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'ATOM'", "'TER'", "'END'" ]

    symbolicNames = [ "<INVALID>", "Integer", "Float", "Double_quote_string", 
                      "COMMENT", "Atom", "Ter", "End", "Simple_name", "SPACE", 
                      "RETURN", "CONTINUE", "ENCLOSE_COMMENT", "SECTION_COMMENT", 
                      "LINE_COMMENT", "Any_name", "SPACE_CM", "RETURN_CM" ]

    RULE_bare_pdb = 0
    RULE_comment = 1
    RULE_coordinates = 2
    RULE_atom_coordinate = 3
    RULE_terminal = 4

    ruleNames =  [ "bare_pdb", "comment", "coordinates", "atom_coordinate", 
                   "terminal" ]

    EOF = Token.EOF
    Integer=1
    Float=2
    Double_quote_string=3
    COMMENT=4
    Atom=5
    Ter=6
    End=7
    Simple_name=8
    SPACE=9
    RETURN=10
    CONTINUE=11
    ENCLOSE_COMMENT=12
    SECTION_COMMENT=13
    LINE_COMMENT=14
    Any_name=15
    SPACE_CM=16
    RETURN_CM=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Bare_pdbContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BarePDBParser.EOF, 0)

        def RETURN(self, i:int=None):
            if i is None:
                return self.getTokens(BarePDBParser.RETURN)
            else:
                return self.getToken(BarePDBParser.RETURN, i)

        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BarePDBParser.CommentContext)
            else:
                return self.getTypedRuleContext(BarePDBParser.CommentContext,i)


        def coordinates(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BarePDBParser.CoordinatesContext)
            else:
                return self.getTypedRuleContext(BarePDBParser.CoordinatesContext,i)


        def terminal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BarePDBParser.TerminalContext)
            else:
                return self.getTypedRuleContext(BarePDBParser.TerminalContext,i)


        def getRuleIndex(self):
            return BarePDBParser.RULE_bare_pdb

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBare_pdb" ):
                listener.enterBare_pdb(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBare_pdb" ):
                listener.exitBare_pdb(self)




    def bare_pdb(self):

        localctx = BarePDBParser.Bare_pdbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_bare_pdb)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 10
                self.match(BarePDBParser.RETURN)


            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1264) != 0):
                self.state = 17
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 13
                    self.comment()
                    pass
                elif token in [5]:
                    self.state = 14
                    self.coordinates()
                    pass
                elif token in [6, 7]:
                    self.state = 15
                    self.terminal()
                    pass
                elif token in [10]:
                    self.state = 16
                    self.match(BarePDBParser.RETURN)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
            self.match(BarePDBParser.EOF)
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
            return self.getToken(BarePDBParser.COMMENT, 0)

        def RETURN_CM(self):
            return self.getToken(BarePDBParser.RETURN_CM, 0)

        def EOF(self):
            return self.getToken(BarePDBParser.EOF, 0)

        def Any_name(self, i:int=None):
            if i is None:
                return self.getTokens(BarePDBParser.Any_name)
            else:
                return self.getToken(BarePDBParser.Any_name, i)

        def getRuleIndex(self):
            return BarePDBParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = BarePDBParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(BarePDBParser.COMMENT)
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 25
                self.match(BarePDBParser.Any_name)
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 31
            _la = self._input.LA(1)
            if not(_la==-1 or _la==17):
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


    class CoordinatesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom_coordinate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BarePDBParser.Atom_coordinateContext)
            else:
                return self.getTypedRuleContext(BarePDBParser.Atom_coordinateContext,i)


        def getRuleIndex(self):
            return BarePDBParser.RULE_coordinates

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoordinates" ):
                listener.enterCoordinates(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoordinates" ):
                listener.exitCoordinates(self)




    def coordinates(self):

        localctx = BarePDBParser.CoordinatesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_coordinates)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 33
                    self.atom_coordinate()

                else:
                    raise NoViableAltException(self)
                self.state = 36 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atom_coordinateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Atom(self):
            return self.getToken(BarePDBParser.Atom, 0)

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(BarePDBParser.Integer)
            else:
                return self.getToken(BarePDBParser.Integer, i)

        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(BarePDBParser.Simple_name)
            else:
                return self.getToken(BarePDBParser.Simple_name, i)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(BarePDBParser.Float)
            else:
                return self.getToken(BarePDBParser.Float, i)

        def RETURN(self):
            return self.getToken(BarePDBParser.RETURN, 0)

        def getRuleIndex(self):
            return BarePDBParser.RULE_atom_coordinate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom_coordinate" ):
                listener.enterAtom_coordinate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom_coordinate" ):
                listener.exitAtom_coordinate(self)




    def atom_coordinate(self):

        localctx = BarePDBParser.Atom_coordinateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atom_coordinate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(BarePDBParser.Atom)
            self.state = 39
            self.match(BarePDBParser.Integer)
            self.state = 40
            self.match(BarePDBParser.Simple_name)
            self.state = 41
            self.match(BarePDBParser.Simple_name)
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==8:
                    self.state = 42
                    self.match(BarePDBParser.Simple_name)


                self.state = 45
                self.match(BarePDBParser.Integer)
                pass

            elif la_ == 2:
                self.state = 46
                self.match(BarePDBParser.Simple_name)
                pass


            self.state = 49
            self.match(BarePDBParser.Float)
            self.state = 50
            self.match(BarePDBParser.Float)
            self.state = 51
            self.match(BarePDBParser.Float)
            self.state = 52
            self.match(BarePDBParser.Float)
            self.state = 53
            self.match(BarePDBParser.Float)
            self.state = 54
            self.match(BarePDBParser.Simple_name)
            self.state = 55
            self.match(BarePDBParser.RETURN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Ter(self):
            return self.getToken(BarePDBParser.Ter, 0)

        def RETURN(self):
            return self.getToken(BarePDBParser.RETURN, 0)

        def End(self):
            return self.getToken(BarePDBParser.End, 0)

        def getRuleIndex(self):
            return BarePDBParser.RULE_terminal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminal" ):
                listener.enterTerminal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminal" ):
                listener.exitTerminal(self)




    def terminal(self):

        localctx = BarePDBParser.TerminalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_terminal)
        try:
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.match(BarePDBParser.Ter)
                self.state = 58
                self.match(BarePDBParser.RETURN)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.match(BarePDBParser.End)
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





