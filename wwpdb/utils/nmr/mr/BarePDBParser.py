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
        4,1,15,75,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,1,0,5,0,17,8,0,10,0,12,0,20,9,0,1,0,1,0,1,1,1,1,5,1,26,8,1,
        10,1,12,1,29,9,1,1,1,1,1,1,2,4,2,34,8,2,11,2,12,2,35,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,3,3,45,8,3,1,3,1,3,3,3,49,8,3,1,3,1,3,1,3,1,3,1,
        3,3,3,56,8,3,1,3,3,3,59,8,3,1,3,3,3,62,8,3,1,4,1,4,1,5,1,5,5,5,68,
        8,5,10,5,12,5,71,9,5,1,5,1,5,1,5,0,0,6,0,2,4,6,8,10,0,3,1,1,15,15,
        1,0,4,5,2,0,1,1,8,8,81,0,18,1,0,0,0,2,23,1,0,0,0,4,33,1,0,0,0,6,
        37,1,0,0,0,8,63,1,0,0,0,10,65,1,0,0,0,12,17,3,2,1,0,13,17,3,4,2,
        0,14,17,3,10,5,0,15,17,5,7,0,0,16,12,1,0,0,0,16,13,1,0,0,0,16,14,
        1,0,0,0,16,15,1,0,0,0,17,20,1,0,0,0,18,16,1,0,0,0,18,19,1,0,0,0,
        19,21,1,0,0,0,20,18,1,0,0,0,21,22,5,0,0,1,22,1,1,0,0,0,23,27,5,3,
        0,0,24,26,5,13,0,0,25,24,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,27,
        28,1,0,0,0,28,30,1,0,0,0,29,27,1,0,0,0,30,31,7,0,0,0,31,3,1,0,0,
        0,32,34,3,6,3,0,33,32,1,0,0,0,34,35,1,0,0,0,35,33,1,0,0,0,35,36,
        1,0,0,0,36,5,1,0,0,0,37,38,7,1,0,0,38,39,5,1,0,0,39,40,5,8,0,0,40,
        48,5,8,0,0,41,42,5,1,0,0,42,49,5,1,0,0,43,45,5,8,0,0,44,43,1,0,0,
        0,44,45,1,0,0,0,45,46,1,0,0,0,46,49,5,1,0,0,47,49,5,8,0,0,48,41,
        1,0,0,0,48,44,1,0,0,0,48,47,1,0,0,0,49,50,1,0,0,0,50,51,5,2,0,0,
        51,52,5,2,0,0,52,55,5,2,0,0,53,54,5,2,0,0,54,56,5,2,0,0,55,53,1,
        0,0,0,55,56,1,0,0,0,56,58,1,0,0,0,57,59,3,8,4,0,58,57,1,0,0,0,58,
        59,1,0,0,0,59,61,1,0,0,0,60,62,3,8,4,0,61,60,1,0,0,0,61,62,1,0,0,
        0,62,7,1,0,0,0,63,64,7,2,0,0,64,9,1,0,0,0,65,69,5,6,0,0,66,68,5,
        13,0,0,67,66,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,
        72,1,0,0,0,71,69,1,0,0,0,72,73,7,0,0,0,73,11,1,0,0,0,10,16,18,27,
        35,44,48,55,58,61,69
    ]

class BarePDBParser ( Parser ):

    grammarFileName = "BarePDBParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'ATOM'", "'HETATM'", "'TER'", "'END'" ]

    symbolicNames = [ "<INVALID>", "Integer", "Float", "COMMENT", "Atom", 
                      "Hetatm", "Ter", "End", "Simple_name", "SPACE", "ENCLOSE_COMMENT", 
                      "SECTION_COMMENT", "LINE_COMMENT", "Any_name", "SPACE_CM", 
                      "RETURN_CM" ]

    RULE_bare_pdb = 0
    RULE_comment = 1
    RULE_coordinates = 2
    RULE_atom_coordinate = 3
    RULE_non_float = 4
    RULE_terminal = 5

    ruleNames =  [ "bare_pdb", "comment", "coordinates", "atom_coordinate", 
                   "non_float", "terminal" ]

    EOF = Token.EOF
    Integer=1
    Float=2
    COMMENT=3
    Atom=4
    Hetatm=5
    Ter=6
    End=7
    Simple_name=8
    SPACE=9
    ENCLOSE_COMMENT=10
    SECTION_COMMENT=11
    LINE_COMMENT=12
    Any_name=13
    SPACE_CM=14
    RETURN_CM=15

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


        def End(self, i:int=None):
            if i is None:
                return self.getTokens(BarePDBParser.End)
            else:
                return self.getToken(BarePDBParser.End, i)

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
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 248) != 0):
                self.state = 16
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 12
                    self.comment()
                    pass
                elif token in [4, 5]:
                    self.state = 13
                    self.coordinates()
                    pass
                elif token in [6]:
                    self.state = 14
                    self.terminal()
                    pass
                elif token in [7]:
                    self.state = 15
                    self.match(BarePDBParser.End)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 21
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
            self.state = 23
            self.match(BarePDBParser.COMMENT)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 24
                self.match(BarePDBParser.Any_name)
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
            _la = self._input.LA(1)
            if not(_la==-1 or _la==15):
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
            self.state = 33 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 32
                    self.atom_coordinate()

                else:
                    raise NoViableAltException(self)
                self.state = 35 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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

        def Atom(self):
            return self.getToken(BarePDBParser.Atom, 0)

        def Hetatm(self):
            return self.getToken(BarePDBParser.Hetatm, 0)

        def non_float(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BarePDBParser.Non_floatContext)
            else:
                return self.getTypedRuleContext(BarePDBParser.Non_floatContext,i)


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
            self.state = 37
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 38
            self.match(BarePDBParser.Integer)
            self.state = 39
            self.match(BarePDBParser.Simple_name)
            self.state = 40
            self.match(BarePDBParser.Simple_name)
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 41
                self.match(BarePDBParser.Integer)
                self.state = 42
                self.match(BarePDBParser.Integer)
                pass

            elif la_ == 2:
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==8:
                    self.state = 43
                    self.match(BarePDBParser.Simple_name)


                self.state = 46
                self.match(BarePDBParser.Integer)
                pass

            elif la_ == 3:
                self.state = 47
                self.match(BarePDBParser.Simple_name)
                pass


            self.state = 50
            self.match(BarePDBParser.Float)
            self.state = 51
            self.match(BarePDBParser.Float)
            self.state = 52
            self.match(BarePDBParser.Float)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 53
                self.match(BarePDBParser.Float)
                self.state = 54
                self.match(BarePDBParser.Float)


            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 57
                self.non_float()


            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==8:
                self.state = 60
                self.non_float()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Non_floatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Simple_name(self):
            return self.getToken(BarePDBParser.Simple_name, 0)

        def Integer(self):
            return self.getToken(BarePDBParser.Integer, 0)

        def getRuleIndex(self):
            return BarePDBParser.RULE_non_float

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNon_float" ):
                listener.enterNon_float(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNon_float" ):
                listener.exitNon_float(self)




    def non_float(self):

        localctx = BarePDBParser.Non_floatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_non_float)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            _la = self._input.LA(1)
            if not(_la==1 or _la==8):
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


    class TerminalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Ter(self):
            return self.getToken(BarePDBParser.Ter, 0)

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
            return BarePDBParser.RULE_terminal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminal" ):
                listener.enterTerminal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminal" ):
                listener.exitTerminal(self)




    def terminal(self):

        localctx = BarePDBParser.TerminalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_terminal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(BarePDBParser.Ter)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 66
                self.match(BarePDBParser.Any_name)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            _la = self._input.LA(1)
            if not(_la==-1 or _la==15):
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





