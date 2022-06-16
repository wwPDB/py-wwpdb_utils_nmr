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
        4,1,18,173,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,0,1,0,1,0,1,0,5,0,35,8,0,10,0,12,0,38,9,0,1,0,1,0,1,1,
        1,1,1,1,1,1,4,1,46,8,1,11,1,12,1,47,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,5,2,60,8,2,10,2,12,2,63,9,2,1,3,1,3,1,3,1,3,4,3,69,8,
        3,11,3,12,3,70,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,82,8,4,10,
        4,12,4,85,9,4,1,5,1,5,1,5,1,5,4,5,91,8,5,11,5,12,5,92,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,105,8,6,10,6,12,6,108,9,6,1,7,
        1,7,1,7,1,7,4,7,114,8,7,11,7,12,7,115,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,5,8,127,8,8,10,8,12,8,130,9,8,1,9,1,9,1,9,1,9,4,9,136,
        8,9,11,9,12,9,137,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,147,8,
        10,10,10,12,10,150,9,10,1,11,1,11,1,11,1,11,4,11,156,8,11,11,11,
        12,11,157,1,12,1,12,1,12,1,12,1,12,1,12,5,12,166,8,12,10,12,12,12,
        169,9,12,1,13,1,13,1,13,0,0,14,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,0,1,1,0,9,10,176,0,36,1,0,0,0,2,41,1,0,0,0,4,49,1,0,0,0,6,64,
        1,0,0,0,8,72,1,0,0,0,10,86,1,0,0,0,12,94,1,0,0,0,14,109,1,0,0,0,
        16,117,1,0,0,0,18,131,1,0,0,0,20,139,1,0,0,0,22,151,1,0,0,0,24,159,
        1,0,0,0,26,170,1,0,0,0,28,35,3,2,1,0,29,35,3,6,3,0,30,35,3,10,5,
        0,31,35,3,14,7,0,32,35,3,18,9,0,33,35,3,22,11,0,34,28,1,0,0,0,34,
        29,1,0,0,0,34,30,1,0,0,0,34,31,1,0,0,0,34,32,1,0,0,0,34,33,1,0,0,
        0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,39,1,0,0,0,38,36,
        1,0,0,0,39,40,5,0,0,1,40,1,1,0,0,0,41,42,5,1,0,0,42,43,5,3,0,0,43,
        45,5,2,0,0,44,46,3,4,2,0,45,44,1,0,0,0,46,47,1,0,0,0,47,45,1,0,0,
        0,47,48,1,0,0,0,48,3,1,0,0,0,49,50,5,9,0,0,50,51,5,9,0,0,51,52,5,
        9,0,0,52,53,5,9,0,0,53,54,5,9,0,0,54,55,3,26,13,0,55,56,3,26,13,
        0,56,57,3,26,13,0,57,61,3,26,13,0,58,60,5,14,0,0,59,58,1,0,0,0,60,
        63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,5,1,0,0,0,63,61,1,0,0,
        0,64,65,5,1,0,0,65,66,5,4,0,0,66,68,5,2,0,0,67,69,3,8,4,0,68,67,
        1,0,0,0,69,70,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,7,1,0,0,0,72,
        73,5,9,0,0,73,74,5,9,0,0,74,75,5,9,0,0,75,76,5,9,0,0,76,77,5,9,0,
        0,77,78,3,26,13,0,78,79,3,26,13,0,79,83,3,26,13,0,80,82,5,14,0,0,
        81,80,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,9,1,0,
        0,0,85,83,1,0,0,0,86,87,5,1,0,0,87,88,5,5,0,0,88,90,5,2,0,0,89,91,
        3,12,6,0,90,89,1,0,0,0,91,92,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,
        93,11,1,0,0,0,94,95,5,9,0,0,95,96,5,9,0,0,96,97,5,9,0,0,97,98,5,
        9,0,0,98,99,5,9,0,0,99,100,3,26,13,0,100,101,3,26,13,0,101,102,3,
        26,13,0,102,106,3,26,13,0,103,105,5,14,0,0,104,103,1,0,0,0,105,108,
        1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,13,1,0,0,0,108,106,1,
        0,0,0,109,110,5,1,0,0,110,111,5,6,0,0,111,113,5,2,0,0,112,114,3,
        16,8,0,113,112,1,0,0,0,114,115,1,0,0,0,115,113,1,0,0,0,115,116,1,
        0,0,0,116,15,1,0,0,0,117,118,5,9,0,0,118,119,5,9,0,0,119,120,5,9,
        0,0,120,121,5,9,0,0,121,122,5,9,0,0,122,123,3,26,13,0,123,124,3,
        26,13,0,124,128,5,9,0,0,125,127,5,14,0,0,126,125,1,0,0,0,127,130,
        1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,17,1,0,0,0,130,128,1,
        0,0,0,131,132,5,1,0,0,132,133,5,7,0,0,133,135,5,2,0,0,134,136,3,
        20,10,0,135,134,1,0,0,0,136,137,1,0,0,0,137,135,1,0,0,0,137,138,
        1,0,0,0,138,19,1,0,0,0,139,140,5,9,0,0,140,141,5,9,0,0,141,142,5,
        9,0,0,142,143,3,26,13,0,143,144,3,26,13,0,144,148,5,9,0,0,145,147,
        5,14,0,0,146,145,1,0,0,0,147,150,1,0,0,0,148,146,1,0,0,0,148,149,
        1,0,0,0,149,21,1,0,0,0,150,148,1,0,0,0,151,152,5,1,0,0,152,153,5,
        8,0,0,153,155,5,2,0,0,154,156,3,24,12,0,155,154,1,0,0,0,156,157,
        1,0,0,0,157,155,1,0,0,0,157,158,1,0,0,0,158,23,1,0,0,0,159,160,5,
        9,0,0,160,161,5,9,0,0,161,162,3,26,13,0,162,163,3,26,13,0,163,167,
        3,26,13,0,164,166,5,14,0,0,165,164,1,0,0,0,166,169,1,0,0,0,167,165,
        1,0,0,0,167,168,1,0,0,0,168,25,1,0,0,0,169,167,1,0,0,0,170,171,7,
        0,0,0,171,27,1,0,0,0,14,34,36,47,61,70,83,92,106,115,128,137,148,
        157,167
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


        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(GromacsMRParser.Simple_name)
            else:
                return self.getToken(GromacsMRParser.Simple_name, i)

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
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GromacsMRParser.Simple_name:
                self.state = 58
                self.match(GromacsMRParser.Simple_name)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.state = 64
            self.match(GromacsMRParser.L_brkt)
            self.state = 65
            self.match(GromacsMRParser.Dihedral_restraints)
            self.state = 66
            self.match(GromacsMRParser.R_brkt)
            self.state = 68 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 67
                self.dihedral_restraint()
                self.state = 70 
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


        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(GromacsMRParser.Simple_name)
            else:
                return self.getToken(GromacsMRParser.Simple_name, i)

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
            self.state = 72
            self.match(GromacsMRParser.Integer)
            self.state = 73
            self.match(GromacsMRParser.Integer)
            self.state = 74
            self.match(GromacsMRParser.Integer)
            self.state = 75
            self.match(GromacsMRParser.Integer)
            self.state = 76
            self.match(GromacsMRParser.Integer)
            self.state = 77
            self.number()
            self.state = 78
            self.number()
            self.state = 79
            self.number()
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GromacsMRParser.Simple_name:
                self.state = 80
                self.match(GromacsMRParser.Simple_name)
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.state = 86
            self.match(GromacsMRParser.L_brkt)
            self.state = 87
            self.match(GromacsMRParser.Orientation_restraints)
            self.state = 88
            self.match(GromacsMRParser.R_brkt)
            self.state = 90 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 89
                self.orientation_restraint()
                self.state = 92 
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


        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(GromacsMRParser.Simple_name)
            else:
                return self.getToken(GromacsMRParser.Simple_name, i)

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
            self.state = 94
            self.match(GromacsMRParser.Integer)
            self.state = 95
            self.match(GromacsMRParser.Integer)
            self.state = 96
            self.match(GromacsMRParser.Integer)
            self.state = 97
            self.match(GromacsMRParser.Integer)
            self.state = 98
            self.match(GromacsMRParser.Integer)
            self.state = 99
            self.number()
            self.state = 100
            self.number()
            self.state = 101
            self.number()
            self.state = 102
            self.number()
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GromacsMRParser.Simple_name:
                self.state = 103
                self.match(GromacsMRParser.Simple_name)
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.state = 109
            self.match(GromacsMRParser.L_brkt)
            self.state = 110
            self.match(GromacsMRParser.Angle_restraints)
            self.state = 111
            self.match(GromacsMRParser.R_brkt)
            self.state = 113 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 112
                self.angle_restraint()
                self.state = 115 
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


        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(GromacsMRParser.Simple_name)
            else:
                return self.getToken(GromacsMRParser.Simple_name, i)

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
            self.state = 117
            self.match(GromacsMRParser.Integer)
            self.state = 118
            self.match(GromacsMRParser.Integer)
            self.state = 119
            self.match(GromacsMRParser.Integer)
            self.state = 120
            self.match(GromacsMRParser.Integer)
            self.state = 121
            self.match(GromacsMRParser.Integer)
            self.state = 122
            self.number()
            self.state = 123
            self.number()
            self.state = 124
            self.match(GromacsMRParser.Integer)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GromacsMRParser.Simple_name:
                self.state = 125
                self.match(GromacsMRParser.Simple_name)
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.state = 131
            self.match(GromacsMRParser.L_brkt)
            self.state = 132
            self.match(GromacsMRParser.Angle_restraints_z)
            self.state = 133
            self.match(GromacsMRParser.R_brkt)
            self.state = 135 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 134
                self.angle_restraint_z()
                self.state = 137 
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


        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(GromacsMRParser.Simple_name)
            else:
                return self.getToken(GromacsMRParser.Simple_name, i)

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
            self.state = 139
            self.match(GromacsMRParser.Integer)
            self.state = 140
            self.match(GromacsMRParser.Integer)
            self.state = 141
            self.match(GromacsMRParser.Integer)
            self.state = 142
            self.number()
            self.state = 143
            self.number()
            self.state = 144
            self.match(GromacsMRParser.Integer)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GromacsMRParser.Simple_name:
                self.state = 145
                self.match(GromacsMRParser.Simple_name)
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.state = 151
            self.match(GromacsMRParser.L_brkt)
            self.state = 152
            self.match(GromacsMRParser.Position_restraints)
            self.state = 153
            self.match(GromacsMRParser.R_brkt)
            self.state = 155 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 154
                self.position_restraint()
                self.state = 157 
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


        def Simple_name(self, i:int=None):
            if i is None:
                return self.getTokens(GromacsMRParser.Simple_name)
            else:
                return self.getToken(GromacsMRParser.Simple_name, i)

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
            self.state = 159
            self.match(GromacsMRParser.Integer)
            self.state = 160
            self.match(GromacsMRParser.Integer)
            self.state = 161
            self.number()
            self.state = 162
            self.number()
            self.state = 163
            self.number()
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GromacsMRParser.Simple_name:
                self.state = 164
                self.match(GromacsMRParser.Simple_name)
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.state = 170
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





