# Generated from GromacsMRParser.g4 by ANTLR 4.10.1
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
        4,1,18,155,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,0,1,0,1,0,1,0,5,0,35,8,0,10,0,12,0,38,9,0,1,0,1,0,1,1,
        1,1,1,1,1,1,4,1,46,8,1,11,1,12,1,47,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,3,2,60,8,2,1,3,1,3,1,3,1,3,4,3,66,8,3,11,3,12,3,67,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,79,8,4,1,5,1,5,1,5,1,5,4,5,
        85,8,5,11,5,12,5,86,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,
        99,8,6,1,7,1,7,1,7,1,7,4,7,105,8,7,11,7,12,7,106,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,3,8,118,8,8,1,9,1,9,1,9,1,9,4,9,124,8,9,11,9,
        12,9,125,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,135,8,10,1,11,1,
        11,1,11,1,11,4,11,141,8,11,11,11,12,11,142,1,12,1,12,1,12,1,12,1,
        12,1,12,3,12,151,8,12,1,13,1,13,1,13,0,0,14,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,0,1,1,0,9,10,158,0,36,1,0,0,0,2,41,1,0,0,0,4,49,1,
        0,0,0,6,61,1,0,0,0,8,69,1,0,0,0,10,80,1,0,0,0,12,88,1,0,0,0,14,100,
        1,0,0,0,16,108,1,0,0,0,18,119,1,0,0,0,20,127,1,0,0,0,22,136,1,0,
        0,0,24,144,1,0,0,0,26,152,1,0,0,0,28,35,3,2,1,0,29,35,3,6,3,0,30,
        35,3,10,5,0,31,35,3,14,7,0,32,35,3,18,9,0,33,35,3,22,11,0,34,28,
        1,0,0,0,34,29,1,0,0,0,34,30,1,0,0,0,34,31,1,0,0,0,34,32,1,0,0,0,
        34,33,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,39,1,
        0,0,0,38,36,1,0,0,0,39,40,5,0,0,1,40,1,1,0,0,0,41,42,5,1,0,0,42,
        43,5,3,0,0,43,45,5,2,0,0,44,46,3,4,2,0,45,44,1,0,0,0,46,47,1,0,0,
        0,47,45,1,0,0,0,47,48,1,0,0,0,48,3,1,0,0,0,49,50,5,9,0,0,50,51,5,
        9,0,0,51,52,5,9,0,0,52,53,5,9,0,0,53,54,5,9,0,0,54,55,3,26,13,0,
        55,56,3,26,13,0,56,57,3,26,13,0,57,59,3,26,13,0,58,60,5,14,0,0,59,
        58,1,0,0,0,59,60,1,0,0,0,60,5,1,0,0,0,61,62,5,1,0,0,62,63,5,4,0,
        0,63,65,5,2,0,0,64,66,3,8,4,0,65,64,1,0,0,0,66,67,1,0,0,0,67,65,
        1,0,0,0,67,68,1,0,0,0,68,7,1,0,0,0,69,70,5,9,0,0,70,71,5,9,0,0,71,
        72,5,9,0,0,72,73,5,9,0,0,73,74,5,9,0,0,74,75,3,26,13,0,75,76,3,26,
        13,0,76,78,3,26,13,0,77,79,5,14,0,0,78,77,1,0,0,0,78,79,1,0,0,0,
        79,9,1,0,0,0,80,81,5,1,0,0,81,82,5,5,0,0,82,84,5,2,0,0,83,85,3,12,
        6,0,84,83,1,0,0,0,85,86,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,11,
        1,0,0,0,88,89,5,9,0,0,89,90,5,9,0,0,90,91,5,9,0,0,91,92,5,9,0,0,
        92,93,5,9,0,0,93,94,3,26,13,0,94,95,3,26,13,0,95,96,3,26,13,0,96,
        98,3,26,13,0,97,99,5,14,0,0,98,97,1,0,0,0,98,99,1,0,0,0,99,13,1,
        0,0,0,100,101,5,1,0,0,101,102,5,6,0,0,102,104,5,2,0,0,103,105,3,
        16,8,0,104,103,1,0,0,0,105,106,1,0,0,0,106,104,1,0,0,0,106,107,1,
        0,0,0,107,15,1,0,0,0,108,109,5,9,0,0,109,110,5,9,0,0,110,111,5,9,
        0,0,111,112,5,9,0,0,112,113,5,9,0,0,113,114,3,26,13,0,114,115,3,
        26,13,0,115,117,5,9,0,0,116,118,5,14,0,0,117,116,1,0,0,0,117,118,
        1,0,0,0,118,17,1,0,0,0,119,120,5,1,0,0,120,121,5,7,0,0,121,123,5,
        2,0,0,122,124,3,20,10,0,123,122,1,0,0,0,124,125,1,0,0,0,125,123,
        1,0,0,0,125,126,1,0,0,0,126,19,1,0,0,0,127,128,5,9,0,0,128,129,5,
        9,0,0,129,130,5,9,0,0,130,131,3,26,13,0,131,132,3,26,13,0,132,134,
        5,9,0,0,133,135,5,14,0,0,134,133,1,0,0,0,134,135,1,0,0,0,135,21,
        1,0,0,0,136,137,5,1,0,0,137,138,5,8,0,0,138,140,5,2,0,0,139,141,
        3,24,12,0,140,139,1,0,0,0,141,142,1,0,0,0,142,140,1,0,0,0,142,143,
        1,0,0,0,143,23,1,0,0,0,144,145,5,9,0,0,145,146,5,9,0,0,146,147,3,
        26,13,0,147,148,3,26,13,0,148,150,3,26,13,0,149,151,5,14,0,0,150,
        149,1,0,0,0,150,151,1,0,0,0,151,25,1,0,0,0,152,153,7,0,0,0,153,27,
        1,0,0,0,14,34,36,47,59,67,78,86,98,106,117,125,134,142,150
    ]

class GromacsMRParser ( Parser ):

    grammarFileName = "GromacsMRParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'distance_restraints'", 
                     "'dihedral_restraints'", "'orientation_restraints'", 
                     "'angle_restraints'", "'angle_restraints_z'", "'position_restraints'" ]

    symbolicNames = [ "<INVALID>", "L_brkt", "R_brkt", "Distance_restraints", 
                      "Dihedral_restraints", "Orientation_restraints", "Angle_restraints", 
                      "Angle_restraints_z", "Position_restraints", "Integer", 
                      "Float", "SHARP_COMMENT", "EXCLM_COMMENT", "SMCLN_COMMENT", 
                      "Simple_name", "SPACE", "COMMENT", "SECTION_COMMENT", 
                      "LINE_COMMENT" ]

    RULE_gromacs_mr = 0
    RULE_distance_restraints = 1
    RULE_distance_restraint = 2
    RULE_dihedral_restraints = 3
    RULE_dihedral_restraint = 4
    RULE_orientation_restraints = 5
    RULE_orientation_restraint = 6
    RULE_angle_restraints = 7
    RULE_angle_restraint = 8
    RULE_angle_restraints_z = 9
    RULE_angle_restraint_z = 10
    RULE_position_restraints = 11
    RULE_position_restraint = 12
    RULE_number = 13

    ruleNames =  [ "gromacs_mr", "distance_restraints", "distance_restraint", 
                   "dihedral_restraints", "dihedral_restraint", "orientation_restraints", 
                   "orientation_restraint", "angle_restraints", "angle_restraint", 
                   "angle_restraints_z", "angle_restraint_z", "position_restraints", 
                   "position_restraint", "number" ]

    EOF = Token.EOF
    L_brkt=1
    R_brkt=2
    Distance_restraints=3
    Dihedral_restraints=4
    Orientation_restraints=5
    Angle_restraints=6
    Angle_restraints_z=7
    Position_restraints=8
    Integer=9
    Float=10
    SHARP_COMMENT=11
    EXCLM_COMMENT=12
    SMCLN_COMMENT=13
    Simple_name=14
    SPACE=15
    COMMENT=16
    SECTION_COMMENT=17
    LINE_COMMENT=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Gromacs_mrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(GromacsMRParser.EOF, 0)

        def distance_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GromacsMRParser.Distance_restraintsContext)
            else:
                return self.getTypedRuleContext(GromacsMRParser.Distance_restraintsContext,i)


        def dihedral_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GromacsMRParser.Dihedral_restraintsContext)
            else:
                return self.getTypedRuleContext(GromacsMRParser.Dihedral_restraintsContext,i)


        def orientation_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GromacsMRParser.Orientation_restraintsContext)
            else:
                return self.getTypedRuleContext(GromacsMRParser.Orientation_restraintsContext,i)


        def angle_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GromacsMRParser.Angle_restraintsContext)
            else:
                return self.getTypedRuleContext(GromacsMRParser.Angle_restraintsContext,i)


        def angle_restraints_z(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GromacsMRParser.Angle_restraints_zContext)
            else:
                return self.getTypedRuleContext(GromacsMRParser.Angle_restraints_zContext,i)


        def position_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GromacsMRParser.Position_restraintsContext)
            else:
                return self.getTypedRuleContext(GromacsMRParser.Position_restraintsContext,i)


        def getRuleIndex(self):
            return GromacsMRParser.RULE_gromacs_mr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGromacs_mr" ):
                listener.enterGromacs_mr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGromacs_mr" ):
                listener.exitGromacs_mr(self)




    def gromacs_mr(self):

        localctx = GromacsMRParser.Gromacs_mrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_gromacs_mr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GromacsMRParser.L_brkt:
                self.state = 34
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 28
                    self.distance_restraints()
                    pass

                elif la_ == 2:
                    self.state = 29
                    self.dihedral_restraints()
                    pass

                elif la_ == 3:
                    self.state = 30
                    self.orientation_restraints()
                    pass

                elif la_ == 4:
                    self.state = 31
                    self.angle_restraints()
                    pass

                elif la_ == 5:
                    self.state = 32
                    self.angle_restraints_z()
                    pass

                elif la_ == 6:
                    self.state = 33
                    self.position_restraints()
                    pass


                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
            self.match(GromacsMRParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Distance_restraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_brkt(self):
            return self.getToken(GromacsMRParser.L_brkt, 0)

        def Distance_restraints(self):
            return self.getToken(GromacsMRParser.Distance_restraints, 0)

        def R_brkt(self):
            return self.getToken(GromacsMRParser.R_brkt, 0)

        def distance_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GromacsMRParser.Distance_restraintContext)
            else:
                return self.getTypedRuleContext(GromacsMRParser.Distance_restraintContext,i)


        def getRuleIndex(self):
            return GromacsMRParser.RULE_distance_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistance_restraints" ):
                listener.enterDistance_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistance_restraints" ):
                listener.exitDistance_restraints(self)




    def distance_restraints(self):

        localctx = GromacsMRParser.Distance_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_distance_restraints)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(GromacsMRParser.L_brkt)
            self.state = 42
            self.match(GromacsMRParser.Distance_restraints)
            self.state = 43
            self.match(GromacsMRParser.R_brkt)
            self.state = 45 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 44
                self.distance_restraint()
                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==GromacsMRParser.Integer):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Distance_restraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(GromacsMRParser.Integer)
            else:
                return self.getToken(GromacsMRParser.Integer, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GromacsMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(GromacsMRParser.NumberContext,i)


        def Simple_name(self):
            return self.getToken(GromacsMRParser.Simple_name, 0)

        def getRuleIndex(self):
            return GromacsMRParser.RULE_distance_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistance_restraint" ):
                listener.enterDistance_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistance_restraint" ):
                listener.exitDistance_restraint(self)




    def distance_restraint(self):

        localctx = GromacsMRParser.Distance_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_distance_restraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(GromacsMRParser.Integer)
            self.state = 50
            self.match(GromacsMRParser.Integer)
            self.state = 51
            self.match(GromacsMRParser.Integer)
            self.state = 52
            self.match(GromacsMRParser.Integer)
            self.state = 53
            self.match(GromacsMRParser.Integer)
            self.state = 54
            self.number()
            self.state = 55
            self.number()
            self.state = 56
            self.number()
            self.state = 57
            self.number()
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GromacsMRParser.Simple_name:
                self.state = 58
                self.match(GromacsMRParser.Simple_name)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dihedral_restraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_brkt(self):
            return self.getToken(GromacsMRParser.L_brkt, 0)

        def Dihedral_restraints(self):
            return self.getToken(GromacsMRParser.Dihedral_restraints, 0)

        def R_brkt(self):
            return self.getToken(GromacsMRParser.R_brkt, 0)

        def dihedral_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GromacsMRParser.Dihedral_restraintContext)
            else:
                return self.getTypedRuleContext(GromacsMRParser.Dihedral_restraintContext,i)


        def getRuleIndex(self):
            return GromacsMRParser.RULE_dihedral_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDihedral_restraints" ):
                listener.enterDihedral_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDihedral_restraints" ):
                listener.exitDihedral_restraints(self)




    def dihedral_restraints(self):

        localctx = GromacsMRParser.Dihedral_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_dihedral_restraints)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(GromacsMRParser.L_brkt)
            self.state = 62
            self.match(GromacsMRParser.Dihedral_restraints)
            self.state = 63
            self.match(GromacsMRParser.R_brkt)
            self.state = 65 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 64
                self.dihedral_restraint()
                self.state = 67 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==GromacsMRParser.Integer):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dihedral_restraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(GromacsMRParser.Integer)
            else:
                return self.getToken(GromacsMRParser.Integer, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GromacsMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(GromacsMRParser.NumberContext,i)


        def Simple_name(self):
            return self.getToken(GromacsMRParser.Simple_name, 0)

        def getRuleIndex(self):
            return GromacsMRParser.RULE_dihedral_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDihedral_restraint" ):
                listener.enterDihedral_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDihedral_restraint" ):
                listener.exitDihedral_restraint(self)




    def dihedral_restraint(self):

        localctx = GromacsMRParser.Dihedral_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dihedral_restraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(GromacsMRParser.Integer)
            self.state = 70
            self.match(GromacsMRParser.Integer)
            self.state = 71
            self.match(GromacsMRParser.Integer)
            self.state = 72
            self.match(GromacsMRParser.Integer)
            self.state = 73
            self.match(GromacsMRParser.Integer)
            self.state = 74
            self.number()
            self.state = 75
            self.number()
            self.state = 76
            self.number()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GromacsMRParser.Simple_name:
                self.state = 77
                self.match(GromacsMRParser.Simple_name)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Orientation_restraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_brkt(self):
            return self.getToken(GromacsMRParser.L_brkt, 0)

        def Orientation_restraints(self):
            return self.getToken(GromacsMRParser.Orientation_restraints, 0)

        def R_brkt(self):
            return self.getToken(GromacsMRParser.R_brkt, 0)

        def orientation_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GromacsMRParser.Orientation_restraintContext)
            else:
                return self.getTypedRuleContext(GromacsMRParser.Orientation_restraintContext,i)


        def getRuleIndex(self):
            return GromacsMRParser.RULE_orientation_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrientation_restraints" ):
                listener.enterOrientation_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrientation_restraints" ):
                listener.exitOrientation_restraints(self)




    def orientation_restraints(self):

        localctx = GromacsMRParser.Orientation_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_orientation_restraints)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(GromacsMRParser.L_brkt)
            self.state = 81
            self.match(GromacsMRParser.Orientation_restraints)
            self.state = 82
            self.match(GromacsMRParser.R_brkt)
            self.state = 84 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 83
                self.orientation_restraint()
                self.state = 86 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==GromacsMRParser.Integer):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Orientation_restraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(GromacsMRParser.Integer)
            else:
                return self.getToken(GromacsMRParser.Integer, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GromacsMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(GromacsMRParser.NumberContext,i)


        def Simple_name(self):
            return self.getToken(GromacsMRParser.Simple_name, 0)

        def getRuleIndex(self):
            return GromacsMRParser.RULE_orientation_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrientation_restraint" ):
                listener.enterOrientation_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrientation_restraint" ):
                listener.exitOrientation_restraint(self)




    def orientation_restraint(self):

        localctx = GromacsMRParser.Orientation_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_orientation_restraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(GromacsMRParser.Integer)
            self.state = 89
            self.match(GromacsMRParser.Integer)
            self.state = 90
            self.match(GromacsMRParser.Integer)
            self.state = 91
            self.match(GromacsMRParser.Integer)
            self.state = 92
            self.match(GromacsMRParser.Integer)
            self.state = 93
            self.number()
            self.state = 94
            self.number()
            self.state = 95
            self.number()
            self.state = 96
            self.number()
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GromacsMRParser.Simple_name:
                self.state = 97
                self.match(GromacsMRParser.Simple_name)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Angle_restraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_brkt(self):
            return self.getToken(GromacsMRParser.L_brkt, 0)

        def Angle_restraints(self):
            return self.getToken(GromacsMRParser.Angle_restraints, 0)

        def R_brkt(self):
            return self.getToken(GromacsMRParser.R_brkt, 0)

        def angle_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GromacsMRParser.Angle_restraintContext)
            else:
                return self.getTypedRuleContext(GromacsMRParser.Angle_restraintContext,i)


        def getRuleIndex(self):
            return GromacsMRParser.RULE_angle_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAngle_restraints" ):
                listener.enterAngle_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAngle_restraints" ):
                listener.exitAngle_restraints(self)




    def angle_restraints(self):

        localctx = GromacsMRParser.Angle_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_angle_restraints)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(GromacsMRParser.L_brkt)
            self.state = 101
            self.match(GromacsMRParser.Angle_restraints)
            self.state = 102
            self.match(GromacsMRParser.R_brkt)
            self.state = 104 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 103
                self.angle_restraint()
                self.state = 106 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==GromacsMRParser.Integer):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Angle_restraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(GromacsMRParser.Integer)
            else:
                return self.getToken(GromacsMRParser.Integer, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GromacsMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(GromacsMRParser.NumberContext,i)


        def Simple_name(self):
            return self.getToken(GromacsMRParser.Simple_name, 0)

        def getRuleIndex(self):
            return GromacsMRParser.RULE_angle_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAngle_restraint" ):
                listener.enterAngle_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAngle_restraint" ):
                listener.exitAngle_restraint(self)




    def angle_restraint(self):

        localctx = GromacsMRParser.Angle_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_angle_restraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(GromacsMRParser.Integer)
            self.state = 109
            self.match(GromacsMRParser.Integer)
            self.state = 110
            self.match(GromacsMRParser.Integer)
            self.state = 111
            self.match(GromacsMRParser.Integer)
            self.state = 112
            self.match(GromacsMRParser.Integer)
            self.state = 113
            self.number()
            self.state = 114
            self.number()
            self.state = 115
            self.match(GromacsMRParser.Integer)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GromacsMRParser.Simple_name:
                self.state = 116
                self.match(GromacsMRParser.Simple_name)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Angle_restraints_zContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_brkt(self):
            return self.getToken(GromacsMRParser.L_brkt, 0)

        def Angle_restraints_z(self):
            return self.getToken(GromacsMRParser.Angle_restraints_z, 0)

        def R_brkt(self):
            return self.getToken(GromacsMRParser.R_brkt, 0)

        def angle_restraint_z(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GromacsMRParser.Angle_restraint_zContext)
            else:
                return self.getTypedRuleContext(GromacsMRParser.Angle_restraint_zContext,i)


        def getRuleIndex(self):
            return GromacsMRParser.RULE_angle_restraints_z

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAngle_restraints_z" ):
                listener.enterAngle_restraints_z(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAngle_restraints_z" ):
                listener.exitAngle_restraints_z(self)




    def angle_restraints_z(self):

        localctx = GromacsMRParser.Angle_restraints_zContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_angle_restraints_z)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(GromacsMRParser.L_brkt)
            self.state = 120
            self.match(GromacsMRParser.Angle_restraints_z)
            self.state = 121
            self.match(GromacsMRParser.R_brkt)
            self.state = 123 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 122
                self.angle_restraint_z()
                self.state = 125 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==GromacsMRParser.Integer):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Angle_restraint_zContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(GromacsMRParser.Integer)
            else:
                return self.getToken(GromacsMRParser.Integer, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GromacsMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(GromacsMRParser.NumberContext,i)


        def Simple_name(self):
            return self.getToken(GromacsMRParser.Simple_name, 0)

        def getRuleIndex(self):
            return GromacsMRParser.RULE_angle_restraint_z

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAngle_restraint_z" ):
                listener.enterAngle_restraint_z(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAngle_restraint_z" ):
                listener.exitAngle_restraint_z(self)




    def angle_restraint_z(self):

        localctx = GromacsMRParser.Angle_restraint_zContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_angle_restraint_z)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(GromacsMRParser.Integer)
            self.state = 128
            self.match(GromacsMRParser.Integer)
            self.state = 129
            self.match(GromacsMRParser.Integer)
            self.state = 130
            self.number()
            self.state = 131
            self.number()
            self.state = 132
            self.match(GromacsMRParser.Integer)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GromacsMRParser.Simple_name:
                self.state = 133
                self.match(GromacsMRParser.Simple_name)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Position_restraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_brkt(self):
            return self.getToken(GromacsMRParser.L_brkt, 0)

        def Position_restraints(self):
            return self.getToken(GromacsMRParser.Position_restraints, 0)

        def R_brkt(self):
            return self.getToken(GromacsMRParser.R_brkt, 0)

        def position_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GromacsMRParser.Position_restraintContext)
            else:
                return self.getTypedRuleContext(GromacsMRParser.Position_restraintContext,i)


        def getRuleIndex(self):
            return GromacsMRParser.RULE_position_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPosition_restraints" ):
                listener.enterPosition_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPosition_restraints" ):
                listener.exitPosition_restraints(self)




    def position_restraints(self):

        localctx = GromacsMRParser.Position_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_position_restraints)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(GromacsMRParser.L_brkt)
            self.state = 137
            self.match(GromacsMRParser.Position_restraints)
            self.state = 138
            self.match(GromacsMRParser.R_brkt)
            self.state = 140 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 139
                self.position_restraint()
                self.state = 142 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==GromacsMRParser.Integer):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Position_restraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(GromacsMRParser.Integer)
            else:
                return self.getToken(GromacsMRParser.Integer, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GromacsMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(GromacsMRParser.NumberContext,i)


        def Simple_name(self):
            return self.getToken(GromacsMRParser.Simple_name, 0)

        def getRuleIndex(self):
            return GromacsMRParser.RULE_position_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPosition_restraint" ):
                listener.enterPosition_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPosition_restraint" ):
                listener.exitPosition_restraint(self)




    def position_restraint(self):

        localctx = GromacsMRParser.Position_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_position_restraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(GromacsMRParser.Integer)
            self.state = 145
            self.match(GromacsMRParser.Integer)
            self.state = 146
            self.number()
            self.state = 147
            self.number()
            self.state = 148
            self.number()
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GromacsMRParser.Simple_name:
                self.state = 149
                self.match(GromacsMRParser.Simple_name)


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
            return self.getToken(GromacsMRParser.Float, 0)

        def Integer(self):
            return self.getToken(GromacsMRParser.Integer, 0)

        def getRuleIndex(self):
            return GromacsMRParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = GromacsMRParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            _la = self._input.LA(1)
            if not(_la==GromacsMRParser.Integer or _la==GromacsMRParser.Float):
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





