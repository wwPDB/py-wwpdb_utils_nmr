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
        4,1,18,93,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,1,0,5,0,21,8,0,10,0,12,0,24,9,0,1,0,1,0,1,
        1,1,1,5,1,30,8,1,10,1,12,1,33,9,1,1,1,1,1,1,2,4,2,38,8,2,11,2,12,
        2,39,1,3,1,3,1,3,1,3,1,3,1,3,3,3,48,8,3,1,3,1,3,3,3,52,8,3,1,3,1,
        3,1,3,3,3,57,8,3,1,3,3,3,60,8,3,1,3,3,3,63,8,3,1,4,1,4,1,4,1,4,1,
        4,3,4,70,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,80,8,5,1,6,1,6,
        1,7,1,7,5,7,86,8,7,10,7,12,7,89,9,7,1,7,1,7,1,7,0,0,8,0,2,4,6,8,
        10,12,14,0,2,1,1,18,18,2,0,1,1,11,11,102,0,22,1,0,0,0,2,27,1,0,0,
        0,4,37,1,0,0,0,6,41,1,0,0,0,8,69,1,0,0,0,10,79,1,0,0,0,12,81,1,0,
        0,0,14,83,1,0,0,0,16,21,3,2,1,0,17,21,3,4,2,0,18,21,3,14,7,0,19,
        21,5,10,0,0,20,16,1,0,0,0,20,17,1,0,0,0,20,18,1,0,0,0,20,19,1,0,
        0,0,21,24,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,25,1,0,0,0,24,22,
        1,0,0,0,25,26,5,0,0,1,26,1,1,0,0,0,27,31,5,3,0,0,28,30,5,16,0,0,
        29,28,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,34,1,
        0,0,0,33,31,1,0,0,0,34,35,7,0,0,0,35,3,1,0,0,0,36,38,3,6,3,0,37,
        36,1,0,0,0,38,39,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,5,1,0,0,
        0,41,42,3,8,4,0,42,43,5,11,0,0,43,51,5,11,0,0,44,45,5,1,0,0,45,52,
        5,1,0,0,46,48,5,11,0,0,47,46,1,0,0,0,47,48,1,0,0,0,48,49,1,0,0,0,
        49,52,5,1,0,0,50,52,5,11,0,0,51,44,1,0,0,0,51,47,1,0,0,0,51,50,1,
        0,0,0,52,53,1,0,0,0,53,56,3,10,5,0,54,55,5,2,0,0,55,57,5,2,0,0,56,
        54,1,0,0,0,56,57,1,0,0,0,57,59,1,0,0,0,58,60,3,12,6,0,59,58,1,0,
        0,0,59,60,1,0,0,0,60,62,1,0,0,0,61,63,3,12,6,0,62,61,1,0,0,0,62,
        63,1,0,0,0,63,7,1,0,0,0,64,65,5,7,0,0,65,70,5,1,0,0,66,67,5,8,0,
        0,67,70,5,1,0,0,68,70,5,4,0,0,69,64,1,0,0,0,69,66,1,0,0,0,69,68,
        1,0,0,0,70,9,1,0,0,0,71,72,5,2,0,0,72,73,5,2,0,0,73,80,5,2,0,0,74,
        75,5,2,0,0,75,80,5,5,0,0,76,77,5,5,0,0,77,80,5,2,0,0,78,80,5,6,0,
        0,79,71,1,0,0,0,79,74,1,0,0,0,79,76,1,0,0,0,79,78,1,0,0,0,80,11,
        1,0,0,0,81,82,7,1,0,0,82,13,1,0,0,0,83,87,5,9,0,0,84,86,5,16,0,0,
        85,84,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,90,1,
        0,0,0,89,87,1,0,0,0,90,91,7,0,0,0,91,15,1,0,0,0,12,20,22,31,39,47,
        51,56,59,62,69,79,87
    ]

class BarePDBParser ( Parser ):

    grammarFileName = "BarePDBParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'ATOM'", "'HETATM'", 
                     "'TER'", "'END'" ]

    symbolicNames = [ "<INVALID>", "Integer", "Float", "COMMENT", "Hetatm_decimal", 
                      "Float_concat_2", "Float_concat_3", "Atom", "Hetatm", 
                      "Ter", "End", "Simple_name", "SPACE", "ENCLOSE_COMMENT", 
                      "SECTION_COMMENT", "LINE_COMMENT", "Any_name", "SPACE_CM", 
                      "RETURN_CM" ]

    RULE_bare_pdb = 0
    RULE_comment = 1
    RULE_coordinates = 2
    RULE_atom_coordinate = 3
    RULE_atom_num = 4
    RULE_xyz = 5
    RULE_non_float = 6
    RULE_terminal = 7

    ruleNames =  [ "bare_pdb", "comment", "coordinates", "atom_coordinate", 
                   "atom_num", "xyz", "non_float", "terminal" ]

    EOF = Token.EOF
    Integer=1
    Float=2
    COMMENT=3
    Hetatm_decimal=4
    Float_concat_2=5
    Float_concat_3=6
    Atom=7
    Hetatm=8
    Ter=9
    End=10
    Simple_name=11
    SPACE=12
    ENCLOSE_COMMENT=13
    SECTION_COMMENT=14
    LINE_COMMENT=15
    Any_name=16
    SPACE_CM=17
    RETURN_CM=18

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
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1944) != 0):
                self.state = 20
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 16
                    self.comment()
                    pass
                elif token in [4, 7, 8]:
                    self.state = 17
                    self.coordinates()
                    pass
                elif token in [9]:
                    self.state = 18
                    self.terminal()
                    pass
                elif token in [10]:
                    self.state = 19
                    self.match(BarePDBParser.End)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 25
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
            self.state = 27
            self.match(BarePDBParser.COMMENT)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 28
                self.match(BarePDBParser.Any_name)
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
            _la = self._input.LA(1)
            if not(_la==-1 or _la==18):
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
            self.state = 37 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 36
                    self.atom_coordinate()

                else:
                    raise NoViableAltException(self)
                self.state = 39 
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

        def atom_num(self):
            return self.getTypedRuleContext(BarePDBParser.Atom_numContext,0)


        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(BarePDBParser.Simple_name)
            else:
                return self.getToken(BarePDBParser.Simple_name, i)

        def xyz(self):
            return self.getTypedRuleContext(BarePDBParser.XyzContext,0)


        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(BarePDBParser.Integer)
            else:
                return self.getToken(BarePDBParser.Integer, i)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(BarePDBParser.Float)
            else:
                return self.getToken(BarePDBParser.Float, i)

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
            self.state = 41
            self.atom_num()
            self.state = 42
            self.match(BarePDBParser.Simple_name)
            self.state = 43
            self.match(BarePDBParser.Simple_name)
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 44
                self.match(BarePDBParser.Integer)
                self.state = 45
                self.match(BarePDBParser.Integer)
                pass

            elif la_ == 2:
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
                    self.state = 46
                    self.match(BarePDBParser.Simple_name)


                self.state = 49
                self.match(BarePDBParser.Integer)
                pass

            elif la_ == 3:
                self.state = 50
                self.match(BarePDBParser.Simple_name)
                pass


            self.state = 53
            self.xyz()
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 54
                self.match(BarePDBParser.Float)
                self.state = 55
                self.match(BarePDBParser.Float)


            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 58
                self.non_float()


            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==11:
                self.state = 61
                self.non_float()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atom_numContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Atom(self):
            return self.getToken(BarePDBParser.Atom, 0)

        def Integer(self):
            return self.getToken(BarePDBParser.Integer, 0)

        def Hetatm(self):
            return self.getToken(BarePDBParser.Hetatm, 0)

        def Hetatm_decimal(self):
            return self.getToken(BarePDBParser.Hetatm_decimal, 0)

        def getRuleIndex(self):
            return BarePDBParser.RULE_atom_num

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom_num" ):
                listener.enterAtom_num(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom_num" ):
                listener.exitAtom_num(self)




    def atom_num(self):

        localctx = BarePDBParser.Atom_numContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atom_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.state = 64
                self.match(BarePDBParser.Atom)
                self.state = 65
                self.match(BarePDBParser.Integer)
                pass
            elif token in [8]:
                self.state = 66
                self.match(BarePDBParser.Hetatm)
                self.state = 67
                self.match(BarePDBParser.Integer)
                pass
            elif token in [4]:
                self.state = 68
                self.match(BarePDBParser.Hetatm_decimal)
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


    class XyzContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(BarePDBParser.Float)
            else:
                return self.getToken(BarePDBParser.Float, i)

        def Float_concat_2(self):
            return self.getToken(BarePDBParser.Float_concat_2, 0)

        def Float_concat_3(self):
            return self.getToken(BarePDBParser.Float_concat_3, 0)

        def getRuleIndex(self):
            return BarePDBParser.RULE_xyz

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXyz" ):
                listener.enterXyz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXyz" ):
                listener.exitXyz(self)




    def xyz(self):

        localctx = BarePDBParser.XyzContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_xyz)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 71
                self.match(BarePDBParser.Float)
                self.state = 72
                self.match(BarePDBParser.Float)
                self.state = 73
                self.match(BarePDBParser.Float)
                pass

            elif la_ == 2:
                self.state = 74
                self.match(BarePDBParser.Float)
                self.state = 75
                self.match(BarePDBParser.Float_concat_2)
                pass

            elif la_ == 3:
                self.state = 76
                self.match(BarePDBParser.Float_concat_2)
                self.state = 77
                self.match(BarePDBParser.Float)
                pass

            elif la_ == 4:
                self.state = 78
                self.match(BarePDBParser.Float_concat_3)
                pass


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
        self.enterRule(localctx, 12, self.RULE_non_float)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            _la = self._input.LA(1)
            if not(_la==1 or _la==11):
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
        self.enterRule(localctx, 14, self.RULE_terminal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(BarePDBParser.Ter)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 84
                self.match(BarePDBParser.Any_name)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
            _la = self._input.LA(1)
            if not(_la==-1 or _la==18):
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





