# Generated from XwinNmrPKParser.g4 by ANTLR 4.13.0
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
        4,1,15,107,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,4,0,16,8,0,11,0,12,0,17,1,0,4,0,21,8,0,11,0,12,0,22,1,0,4,
        0,26,8,0,11,0,12,0,27,5,0,30,8,0,10,0,12,0,33,9,0,1,0,1,0,1,1,1,
        1,5,1,39,8,1,10,1,12,1,42,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,3,3,57,8,3,1,3,5,3,60,8,3,10,3,12,3,63,9,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,76,8,4,1,4,5,4,79,8,
        4,10,4,12,4,82,9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,3,5,97,8,5,1,5,5,5,100,8,5,10,5,12,5,103,9,5,1,5,1,5,1,5,0,
        0,6,0,2,4,6,8,10,0,1,1,1,15,15,115,0,31,1,0,0,0,2,36,1,0,0,0,4,45,
        1,0,0,0,6,49,1,0,0,0,8,66,1,0,0,0,10,85,1,0,0,0,12,30,3,2,1,0,13,
        30,3,4,2,0,14,16,3,6,3,0,15,14,1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,
        0,17,18,1,0,0,0,18,30,1,0,0,0,19,21,3,8,4,0,20,19,1,0,0,0,21,22,
        1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,30,1,0,0,0,24,26,3,10,5,0,
        25,24,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,30,1,
        0,0,0,29,12,1,0,0,0,29,13,1,0,0,0,29,15,1,0,0,0,29,20,1,0,0,0,29,
        25,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,34,1,0,0,
        0,33,31,1,0,0,0,34,35,5,0,0,1,35,1,1,0,0,0,36,40,5,4,0,0,37,39,5,
        13,0,0,38,37,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,
        43,1,0,0,0,42,40,1,0,0,0,43,44,7,0,0,0,44,3,1,0,0,0,45,46,5,1,0,
        0,46,47,5,10,0,0,47,48,5,12,0,0,48,5,1,0,0,0,49,50,5,2,0,0,50,51,
        5,3,0,0,51,52,5,3,0,0,52,53,5,3,0,0,53,54,5,3,0,0,54,56,5,3,0,0,
        55,57,5,3,0,0,56,55,1,0,0,0,56,57,1,0,0,0,57,61,1,0,0,0,58,60,5,
        9,0,0,59,58,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,
        64,1,0,0,0,63,61,1,0,0,0,64,65,5,6,0,0,65,7,1,0,0,0,66,67,5,2,0,
        0,67,68,5,3,0,0,68,69,5,3,0,0,69,70,5,3,0,0,70,71,5,3,0,0,71,72,
        5,3,0,0,72,73,5,3,0,0,73,75,5,3,0,0,74,76,5,3,0,0,75,74,1,0,0,0,
        75,76,1,0,0,0,76,80,1,0,0,0,77,79,5,9,0,0,78,77,1,0,0,0,79,82,1,
        0,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,83,1,0,0,0,82,80,1,0,0,0,83,
        84,5,6,0,0,84,9,1,0,0,0,85,86,5,2,0,0,86,87,5,3,0,0,87,88,5,3,0,
        0,88,89,5,3,0,0,89,90,5,3,0,0,90,91,5,3,0,0,91,92,5,3,0,0,92,93,
        5,3,0,0,93,94,5,3,0,0,94,96,5,3,0,0,95,97,5,3,0,0,96,95,1,0,0,0,
        96,97,1,0,0,0,97,101,1,0,0,0,98,100,5,9,0,0,99,98,1,0,0,0,100,103,
        1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,104,1,0,0,0,103,101,1,
        0,0,0,104,105,5,6,0,0,105,11,1,0,0,0,12,17,22,27,29,31,40,56,61,
        75,80,96,101
    ]

class XwinNmrPKParser ( Parser ):

    grammarFileName = "XwinNmrPKParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'# PEAKLIST_DIMENSION'" ]

    symbolicNames = [ "<INVALID>", "Num_of_dim", "Integer", "Float", "COMMENT", 
                      "SPACE", "RETURN", "SECTION_COMMENT", "LINE_COMMENT", 
                      "Annotation", "Integer_ND", "SPACE_ND", "RETURN_ND", 
                      "Any_name", "SPACE_CM", "RETURN_CM" ]

    RULE_xwinnmr_pk = 0
    RULE_comment = 1
    RULE_dimension = 2
    RULE_peak_2d = 3
    RULE_peak_3d = 4
    RULE_peak_4d = 5

    ruleNames =  [ "xwinnmr_pk", "comment", "dimension", "peak_2d", "peak_3d", 
                   "peak_4d" ]

    EOF = Token.EOF
    Num_of_dim=1
    Integer=2
    Float=3
    COMMENT=4
    SPACE=5
    RETURN=6
    SECTION_COMMENT=7
    LINE_COMMENT=8
    Annotation=9
    Integer_ND=10
    SPACE_ND=11
    RETURN_ND=12
    Any_name=13
    SPACE_CM=14
    RETURN_CM=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Xwinnmr_pkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(XwinNmrPKParser.EOF, 0)

        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XwinNmrPKParser.CommentContext)
            else:
                return self.getTypedRuleContext(XwinNmrPKParser.CommentContext,i)


        def dimension(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XwinNmrPKParser.DimensionContext)
            else:
                return self.getTypedRuleContext(XwinNmrPKParser.DimensionContext,i)


        def peak_2d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XwinNmrPKParser.Peak_2dContext)
            else:
                return self.getTypedRuleContext(XwinNmrPKParser.Peak_2dContext,i)


        def peak_3d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XwinNmrPKParser.Peak_3dContext)
            else:
                return self.getTypedRuleContext(XwinNmrPKParser.Peak_3dContext,i)


        def peak_4d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XwinNmrPKParser.Peak_4dContext)
            else:
                return self.getTypedRuleContext(XwinNmrPKParser.Peak_4dContext,i)


        def getRuleIndex(self):
            return XwinNmrPKParser.RULE_xwinnmr_pk

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXwinnmr_pk" ):
                listener.enterXwinnmr_pk(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXwinnmr_pk" ):
                listener.exitXwinnmr_pk(self)




    def xwinnmr_pk(self):

        localctx = XwinNmrPKParser.Xwinnmr_pkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_xwinnmr_pk)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 22) != 0):
                self.state = 29
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 12
                    self.comment()
                    pass

                elif la_ == 2:
                    self.state = 13
                    self.dimension()
                    pass

                elif la_ == 3:
                    self.state = 15 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 14
                            self.peak_2d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 17 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                    pass

                elif la_ == 4:
                    self.state = 20 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 19
                            self.peak_3d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 22 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                    pass

                elif la_ == 5:
                    self.state = 25 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 24
                            self.peak_4d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 27 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                    pass


                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
            self.match(XwinNmrPKParser.EOF)
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
            return self.getToken(XwinNmrPKParser.COMMENT, 0)

        def RETURN_CM(self):
            return self.getToken(XwinNmrPKParser.RETURN_CM, 0)

        def EOF(self):
            return self.getToken(XwinNmrPKParser.EOF, 0)

        def Any_name(self, i:int=None):
            if i is None:
                return self.getTokens(XwinNmrPKParser.Any_name)
            else:
                return self.getToken(XwinNmrPKParser.Any_name, i)

        def getRuleIndex(self):
            return XwinNmrPKParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = XwinNmrPKParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(XwinNmrPKParser.COMMENT)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 37
                self.match(XwinNmrPKParser.Any_name)
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 43
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


    class DimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Num_of_dim(self):
            return self.getToken(XwinNmrPKParser.Num_of_dim, 0)

        def Integer_ND(self):
            return self.getToken(XwinNmrPKParser.Integer_ND, 0)

        def RETURN_ND(self):
            return self.getToken(XwinNmrPKParser.RETURN_ND, 0)

        def getRuleIndex(self):
            return XwinNmrPKParser.RULE_dimension

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDimension" ):
                listener.enterDimension(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDimension" ):
                listener.exitDimension(self)




    def dimension(self):

        localctx = XwinNmrPKParser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_dimension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(XwinNmrPKParser.Num_of_dim)
            self.state = 46
            self.match(XwinNmrPKParser.Integer_ND)
            self.state = 47
            self.match(XwinNmrPKParser.RETURN_ND)
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
            return self.getToken(XwinNmrPKParser.Integer, 0)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(XwinNmrPKParser.Float)
            else:
                return self.getToken(XwinNmrPKParser.Float, i)

        def RETURN(self):
            return self.getToken(XwinNmrPKParser.RETURN, 0)

        def Annotation(self, i:int=None):
            if i is None:
                return self.getTokens(XwinNmrPKParser.Annotation)
            else:
                return self.getToken(XwinNmrPKParser.Annotation, i)

        def getRuleIndex(self):
            return XwinNmrPKParser.RULE_peak_2d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_2d" ):
                listener.enterPeak_2d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_2d" ):
                listener.exitPeak_2d(self)




    def peak_2d(self):

        localctx = XwinNmrPKParser.Peak_2dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_peak_2d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(XwinNmrPKParser.Integer)
            self.state = 50
            self.match(XwinNmrPKParser.Float)
            self.state = 51
            self.match(XwinNmrPKParser.Float)
            self.state = 52
            self.match(XwinNmrPKParser.Float)
            self.state = 53
            self.match(XwinNmrPKParser.Float)
            self.state = 54
            self.match(XwinNmrPKParser.Float)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 55
                self.match(XwinNmrPKParser.Float)


            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 58
                self.match(XwinNmrPKParser.Annotation)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(XwinNmrPKParser.RETURN)
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
            return self.getToken(XwinNmrPKParser.Integer, 0)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(XwinNmrPKParser.Float)
            else:
                return self.getToken(XwinNmrPKParser.Float, i)

        def RETURN(self):
            return self.getToken(XwinNmrPKParser.RETURN, 0)

        def Annotation(self, i:int=None):
            if i is None:
                return self.getTokens(XwinNmrPKParser.Annotation)
            else:
                return self.getToken(XwinNmrPKParser.Annotation, i)

        def getRuleIndex(self):
            return XwinNmrPKParser.RULE_peak_3d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_3d" ):
                listener.enterPeak_3d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_3d" ):
                listener.exitPeak_3d(self)




    def peak_3d(self):

        localctx = XwinNmrPKParser.Peak_3dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_peak_3d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(XwinNmrPKParser.Integer)
            self.state = 67
            self.match(XwinNmrPKParser.Float)
            self.state = 68
            self.match(XwinNmrPKParser.Float)
            self.state = 69
            self.match(XwinNmrPKParser.Float)
            self.state = 70
            self.match(XwinNmrPKParser.Float)
            self.state = 71
            self.match(XwinNmrPKParser.Float)
            self.state = 72
            self.match(XwinNmrPKParser.Float)
            self.state = 73
            self.match(XwinNmrPKParser.Float)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 74
                self.match(XwinNmrPKParser.Float)


            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 77
                self.match(XwinNmrPKParser.Annotation)
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 83
            self.match(XwinNmrPKParser.RETURN)
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
            return self.getToken(XwinNmrPKParser.Integer, 0)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(XwinNmrPKParser.Float)
            else:
                return self.getToken(XwinNmrPKParser.Float, i)

        def RETURN(self):
            return self.getToken(XwinNmrPKParser.RETURN, 0)

        def Annotation(self, i:int=None):
            if i is None:
                return self.getTokens(XwinNmrPKParser.Annotation)
            else:
                return self.getToken(XwinNmrPKParser.Annotation, i)

        def getRuleIndex(self):
            return XwinNmrPKParser.RULE_peak_4d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_4d" ):
                listener.enterPeak_4d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_4d" ):
                listener.exitPeak_4d(self)




    def peak_4d(self):

        localctx = XwinNmrPKParser.Peak_4dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_peak_4d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(XwinNmrPKParser.Integer)
            self.state = 86
            self.match(XwinNmrPKParser.Float)
            self.state = 87
            self.match(XwinNmrPKParser.Float)
            self.state = 88
            self.match(XwinNmrPKParser.Float)
            self.state = 89
            self.match(XwinNmrPKParser.Float)
            self.state = 90
            self.match(XwinNmrPKParser.Float)
            self.state = 91
            self.match(XwinNmrPKParser.Float)
            self.state = 92
            self.match(XwinNmrPKParser.Float)
            self.state = 93
            self.match(XwinNmrPKParser.Float)
            self.state = 94
            self.match(XwinNmrPKParser.Float)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 95
                self.match(XwinNmrPKParser.Float)


            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 98
                self.match(XwinNmrPKParser.Annotation)
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 104
            self.match(XwinNmrPKParser.RETURN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





