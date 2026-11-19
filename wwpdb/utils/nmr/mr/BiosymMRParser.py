# Generated from BiosymMRParser.g4 by ANTLR 4.13.0
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
        4,1,34,277,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,5,0,59,8,0,10,0,12,0,62,9,0,1,0,1,0,1,1,4,1,67,8,1,11,
        1,12,1,68,1,2,3,2,72,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,
        83,8,2,1,2,1,2,1,2,5,2,88,8,2,10,2,12,2,91,9,2,1,3,4,3,94,8,3,11,
        3,12,3,95,1,4,3,4,99,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        5,4,111,8,4,10,4,12,4,114,9,4,1,5,4,5,117,8,5,11,5,12,5,118,1,6,
        3,6,122,8,6,1,6,1,6,1,6,1,6,1,6,3,6,129,8,6,1,6,1,6,1,6,5,6,134,
        8,6,10,6,12,6,137,9,6,1,7,4,7,140,8,7,11,7,12,7,141,1,8,3,8,145,
        8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,
        161,8,8,1,8,1,8,1,8,3,8,166,8,8,1,8,1,8,1,8,3,8,171,8,8,1,9,4,9,
        174,8,9,11,9,12,9,175,1,10,3,10,179,8,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,11,4,11,192,8,11,11,11,12,11,193,1,12,
        3,12,197,8,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,4,13,207,8,
        13,11,13,12,13,208,1,14,3,14,212,8,14,1,14,1,14,1,14,1,15,4,15,218,
        8,15,11,15,12,15,219,1,16,3,16,223,8,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,17,1,17,1,17,3,17,234,8,17,5,17,236,8,17,10,17,12,17,239,
        9,17,1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,20,1,20,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        3,22,266,8,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        0,0,24,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,0,5,1,0,28,30,1,0,31,32,1,0,1,3,1,0,23,24,2,0,18,18,25,
        25,289,0,60,1,0,0,0,2,66,1,0,0,0,4,71,1,0,0,0,6,93,1,0,0,0,8,98,
        1,0,0,0,10,116,1,0,0,0,12,121,1,0,0,0,14,139,1,0,0,0,16,144,1,0,
        0,0,18,173,1,0,0,0,20,178,1,0,0,0,22,191,1,0,0,0,24,196,1,0,0,0,
        26,206,1,0,0,0,28,211,1,0,0,0,30,217,1,0,0,0,32,222,1,0,0,0,34,230,
        1,0,0,0,36,242,1,0,0,0,38,244,1,0,0,0,40,246,1,0,0,0,42,250,1,0,
        0,0,44,258,1,0,0,0,46,269,1,0,0,0,48,59,3,2,1,0,49,59,3,6,3,0,50,
        59,3,10,5,0,51,59,3,14,7,0,52,59,3,18,9,0,53,59,3,22,11,0,54,59,
        3,26,13,0,55,59,3,30,15,0,56,59,3,34,17,0,57,59,3,38,19,0,58,48,
        1,0,0,0,58,49,1,0,0,0,58,50,1,0,0,0,58,51,1,0,0,0,58,52,1,0,0,0,
        58,53,1,0,0,0,58,54,1,0,0,0,58,55,1,0,0,0,58,56,1,0,0,0,58,57,1,
        0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,63,1,0,0,0,62,
        60,1,0,0,0,63,64,5,0,0,1,64,1,1,0,0,0,65,67,3,4,2,0,66,65,1,0,0,
        0,67,68,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,3,1,0,0,0,70,72,5,
        10,0,0,71,70,1,0,0,0,71,72,1,0,0,0,72,73,1,0,0,0,73,74,5,9,0,0,74,
        75,5,9,0,0,75,76,3,36,18,0,76,77,3,36,18,0,77,78,3,36,18,0,78,79,
        3,36,18,0,79,80,3,36,18,0,80,82,3,36,18,0,81,83,3,36,18,0,82,81,
        1,0,0,0,82,83,1,0,0,0,83,89,1,0,0,0,84,85,5,11,0,0,85,86,5,9,0,0,
        86,88,5,9,0,0,87,84,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,
        0,0,0,90,5,1,0,0,0,91,89,1,0,0,0,92,94,3,8,4,0,93,92,1,0,0,0,94,
        95,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,7,1,0,0,0,97,99,5,10,0,
        0,98,97,1,0,0,0,98,99,1,0,0,0,99,100,1,0,0,0,100,101,5,9,0,0,101,
        102,5,9,0,0,102,103,3,36,18,0,103,104,3,36,18,0,104,105,3,36,18,
        0,105,106,3,36,18,0,106,112,3,36,18,0,107,108,5,11,0,0,108,109,5,
        9,0,0,109,111,5,9,0,0,110,107,1,0,0,0,111,114,1,0,0,0,112,110,1,
        0,0,0,112,113,1,0,0,0,113,9,1,0,0,0,114,112,1,0,0,0,115,117,3,12,
        6,0,116,115,1,0,0,0,117,118,1,0,0,0,118,116,1,0,0,0,118,119,1,0,
        0,0,119,11,1,0,0,0,120,122,5,10,0,0,121,120,1,0,0,0,121,122,1,0,
        0,0,122,123,1,0,0,0,123,124,5,9,0,0,124,125,5,9,0,0,125,126,3,36,
        18,0,126,128,3,36,18,0,127,129,3,36,18,0,128,127,1,0,0,0,128,129,
        1,0,0,0,129,135,1,0,0,0,130,131,5,11,0,0,131,132,5,9,0,0,132,134,
        5,9,0,0,133,130,1,0,0,0,134,137,1,0,0,0,135,133,1,0,0,0,135,136,
        1,0,0,0,136,13,1,0,0,0,137,135,1,0,0,0,138,140,3,16,8,0,139,138,
        1,0,0,0,140,141,1,0,0,0,141,139,1,0,0,0,141,142,1,0,0,0,142,15,1,
        0,0,0,143,145,5,10,0,0,144,143,1,0,0,0,144,145,1,0,0,0,145,146,1,
        0,0,0,146,147,5,9,0,0,147,148,5,9,0,0,148,149,5,9,0,0,149,150,5,
        9,0,0,150,151,3,36,18,0,151,152,3,36,18,0,152,153,3,36,18,0,153,
        154,3,36,18,0,154,155,3,36,18,0,155,156,3,36,18,0,156,160,3,36,18,
        0,157,158,3,36,18,0,158,159,3,36,18,0,159,161,1,0,0,0,160,157,1,
        0,0,0,160,161,1,0,0,0,161,165,1,0,0,0,162,163,3,36,18,0,163,164,
        3,36,18,0,164,166,1,0,0,0,165,162,1,0,0,0,165,166,1,0,0,0,166,170,
        1,0,0,0,167,168,3,36,18,0,168,169,3,36,18,0,169,171,1,0,0,0,170,
        167,1,0,0,0,170,171,1,0,0,0,171,17,1,0,0,0,172,174,3,20,10,0,173,
        172,1,0,0,0,174,175,1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,
        19,1,0,0,0,177,179,5,10,0,0,178,177,1,0,0,0,178,179,1,0,0,0,179,
        180,1,0,0,0,180,181,5,9,0,0,181,182,5,9,0,0,182,183,5,9,0,0,183,
        184,5,9,0,0,184,185,3,36,18,0,185,186,3,36,18,0,186,187,3,36,18,
        0,187,188,3,36,18,0,188,189,3,36,18,0,189,21,1,0,0,0,190,192,3,24,
        12,0,191,190,1,0,0,0,192,193,1,0,0,0,193,191,1,0,0,0,193,194,1,0,
        0,0,194,23,1,0,0,0,195,197,5,10,0,0,196,195,1,0,0,0,196,197,1,0,
        0,0,197,198,1,0,0,0,198,199,5,9,0,0,199,200,5,9,0,0,200,201,5,9,
        0,0,201,202,5,9,0,0,202,203,3,36,18,0,203,204,3,36,18,0,204,25,1,
        0,0,0,205,207,3,28,14,0,206,205,1,0,0,0,207,208,1,0,0,0,208,206,
        1,0,0,0,208,209,1,0,0,0,209,27,1,0,0,0,210,212,5,10,0,0,211,210,
        1,0,0,0,211,212,1,0,0,0,212,213,1,0,0,0,213,214,5,9,0,0,214,215,
        5,8,0,0,215,29,1,0,0,0,216,218,3,32,16,0,217,216,1,0,0,0,218,219,
        1,0,0,0,219,217,1,0,0,0,219,220,1,0,0,0,220,31,1,0,0,0,221,223,5,
        10,0,0,222,221,1,0,0,0,222,223,1,0,0,0,223,224,1,0,0,0,224,225,5,
        9,0,0,225,226,5,9,0,0,226,227,5,9,0,0,227,228,5,9,0,0,228,229,5,
        9,0,0,229,33,1,0,0,0,230,237,5,13,0,0,231,233,7,0,0,0,232,234,7,
        1,0,0,233,232,1,0,0,0,233,234,1,0,0,0,234,236,1,0,0,0,235,231,1,
        0,0,0,236,239,1,0,0,0,237,235,1,0,0,0,237,238,1,0,0,0,238,240,1,
        0,0,0,239,237,1,0,0,0,240,241,5,34,0,0,241,35,1,0,0,0,242,243,7,
        2,0,0,243,37,1,0,0,0,244,245,3,40,20,0,245,39,1,0,0,0,246,247,3,
        42,21,0,247,248,3,44,22,0,248,249,3,46,23,0,249,41,1,0,0,0,250,251,
        5,12,0,0,251,252,5,19,0,0,252,253,5,18,0,0,253,254,5,22,0,0,254,
        255,5,18,0,0,255,256,5,18,0,0,256,257,5,27,0,0,257,43,1,0,0,0,258,
        259,5,12,0,0,259,260,5,20,0,0,260,261,5,18,0,0,261,262,7,3,0,0,262,
        263,5,18,0,0,263,265,5,18,0,0,264,266,5,18,0,0,265,264,1,0,0,0,265,
        266,1,0,0,0,266,267,1,0,0,0,267,268,5,27,0,0,268,45,1,0,0,0,269,
        270,5,12,0,0,270,271,5,21,0,0,271,272,5,18,0,0,272,273,7,4,0,0,273,
        274,5,18,0,0,274,275,5,27,0,0,275,47,1,0,0,0,29,58,60,68,71,82,89,
        95,98,112,118,121,128,135,141,144,160,165,170,175,178,193,196,208,
        211,219,222,233,237,265
    ]

class BiosymMRParser ( Parser ):

    grammarFileName = "BiosymMRParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'restraint'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'create'", "'function'", 
                     "'target'", "'distance'", "'quadratic'", "'flatBottomed'", 
                     "'relative'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "Integer", "Float", "Float_DecimalComma", 
                      "Real", "SHARP_COMMENT", "EXCLM_COMMENT", "SMCLN_COMMENT", 
                      "Chiral_code", "Atom_selection", "Ordinal", "Or", 
                      "Restraint", "Mixing_times", "SPACE", "ENCLOSE_COMMENT", 
                      "SECTION_COMMENT", "LINE_COMMENT", "Double_quote_string", 
                      "Create", "Function", "Target", "Distance", "Quadratic", 
                      "Flat_bottomed", "Relative", "SPACE_II", "RETURN_II", 
                      "Real_MT", "Float_MT", "Integer_MT", "Comma_MT", "Period_MT", 
                      "SPACE_MT", "RETURN_MT" ]

    RULE_biosym_mr = 0
    RULE_distance_restraints = 1
    RULE_distance_restraint = 2
    RULE_distance_constraints = 3
    RULE_distance_constraint = 4
    RULE_distance_wo_w_constraints = 5
    RULE_distance_wo_w_constraint = 6
    RULE_dihedral_angle_restraints = 7
    RULE_dihedral_angle_restraint = 8
    RULE_dihedral_angle_constraints = 9
    RULE_dihedral_angle_constraint = 10
    RULE_dihedral_angle_wo_w_constraints = 11
    RULE_dihedral_angle_wo_w_constraint = 12
    RULE_chirality_constraints = 13
    RULE_chirality_constraint = 14
    RULE_prochirality_constraints = 15
    RULE_prochirality_constraint = 16
    RULE_mixing_time = 17
    RULE_number = 18
    RULE_ins_distance_restraints = 19
    RULE_ins_distance_restraint = 20
    RULE_decl_create = 21
    RULE_decl_function = 22
    RULE_decl_target = 23

    ruleNames =  [ "biosym_mr", "distance_restraints", "distance_restraint", 
                   "distance_constraints", "distance_constraint", "distance_wo_w_constraints", 
                   "distance_wo_w_constraint", "dihedral_angle_restraints", 
                   "dihedral_angle_restraint", "dihedral_angle_constraints", 
                   "dihedral_angle_constraint", "dihedral_angle_wo_w_constraints", 
                   "dihedral_angle_wo_w_constraint", "chirality_constraints", 
                   "chirality_constraint", "prochirality_constraints", "prochirality_constraint", 
                   "mixing_time", "number", "ins_distance_restraints", "ins_distance_restraint", 
                   "decl_create", "decl_function", "decl_target" ]

    EOF = Token.EOF
    Integer=1
    Float=2
    Float_DecimalComma=3
    Real=4
    SHARP_COMMENT=5
    EXCLM_COMMENT=6
    SMCLN_COMMENT=7
    Chiral_code=8
    Atom_selection=9
    Ordinal=10
    Or=11
    Restraint=12
    Mixing_times=13
    SPACE=14
    ENCLOSE_COMMENT=15
    SECTION_COMMENT=16
    LINE_COMMENT=17
    Double_quote_string=18
    Create=19
    Function=20
    Target=21
    Distance=22
    Quadratic=23
    Flat_bottomed=24
    Relative=25
    SPACE_II=26
    RETURN_II=27
    Real_MT=28
    Float_MT=29
    Integer_MT=30
    Comma_MT=31
    Period_MT=32
    SPACE_MT=33
    RETURN_MT=34

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Biosym_mrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BiosymMRParser.EOF, 0)

        def distance_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Distance_restraintsContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Distance_restraintsContext,i)


        def distance_constraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Distance_constraintsContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Distance_constraintsContext,i)


        def distance_wo_w_constraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Distance_wo_w_constraintsContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Distance_wo_w_constraintsContext,i)


        def dihedral_angle_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Dihedral_angle_restraintsContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Dihedral_angle_restraintsContext,i)


        def dihedral_angle_constraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Dihedral_angle_constraintsContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Dihedral_angle_constraintsContext,i)


        def dihedral_angle_wo_w_constraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Dihedral_angle_wo_w_constraintsContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Dihedral_angle_wo_w_constraintsContext,i)


        def chirality_constraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Chirality_constraintsContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Chirality_constraintsContext,i)


        def prochirality_constraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Prochirality_constraintsContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Prochirality_constraintsContext,i)


        def mixing_time(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Mixing_timeContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Mixing_timeContext,i)


        def ins_distance_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Ins_distance_restraintsContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Ins_distance_restraintsContext,i)


        def getRuleIndex(self):
            return BiosymMRParser.RULE_biosym_mr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBiosym_mr" ):
                listener.enterBiosym_mr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBiosym_mr" ):
                listener.exitBiosym_mr(self)




    def biosym_mr(self):

        localctx = BiosymMRParser.Biosym_mrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_biosym_mr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 13824) != 0):
                self.state = 58
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 48
                    self.distance_restraints()
                    pass

                elif la_ == 2:
                    self.state = 49
                    self.distance_constraints()
                    pass

                elif la_ == 3:
                    self.state = 50
                    self.distance_wo_w_constraints()
                    pass

                elif la_ == 4:
                    self.state = 51
                    self.dihedral_angle_restraints()
                    pass

                elif la_ == 5:
                    self.state = 52
                    self.dihedral_angle_constraints()
                    pass

                elif la_ == 6:
                    self.state = 53
                    self.dihedral_angle_wo_w_constraints()
                    pass

                elif la_ == 7:
                    self.state = 54
                    self.chirality_constraints()
                    pass

                elif la_ == 8:
                    self.state = 55
                    self.prochirality_constraints()
                    pass

                elif la_ == 9:
                    self.state = 56
                    self.mixing_time()
                    pass

                elif la_ == 10:
                    self.state = 57
                    self.ins_distance_restraints()
                    pass


                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 63
            self.match(BiosymMRParser.EOF)
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

        def distance_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Distance_restraintContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Distance_restraintContext,i)


        def getRuleIndex(self):
            return BiosymMRParser.RULE_distance_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistance_restraints" ):
                listener.enterDistance_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistance_restraints" ):
                listener.exitDistance_restraints(self)




    def distance_restraints(self):

        localctx = BiosymMRParser.Distance_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_distance_restraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 65
                    self.distance_restraint()

                else:
                    raise NoViableAltException(self)
                self.state = 68 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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

        def Atom_selection(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Atom_selection)
            else:
                return self.getToken(BiosymMRParser.Atom_selection, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.NumberContext,i)


        def Ordinal(self):
            return self.getToken(BiosymMRParser.Ordinal, 0)

        def Or(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Or)
            else:
                return self.getToken(BiosymMRParser.Or, i)

        def getRuleIndex(self):
            return BiosymMRParser.RULE_distance_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistance_restraint" ):
                listener.enterDistance_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistance_restraint" ):
                listener.exitDistance_restraint(self)




    def distance_restraint(self):

        localctx = BiosymMRParser.Distance_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_distance_restraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 70
                self.match(BiosymMRParser.Ordinal)


            self.state = 73
            self.match(BiosymMRParser.Atom_selection)
            self.state = 74
            self.match(BiosymMRParser.Atom_selection)
            self.state = 75
            self.number()
            self.state = 76
            self.number()
            self.state = 77
            self.number()
            self.state = 78
            self.number()
            self.state = 79
            self.number()
            self.state = 80
            self.number()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                self.state = 81
                self.number()


            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 84
                self.match(BiosymMRParser.Or)
                self.state = 85
                self.match(BiosymMRParser.Atom_selection)
                self.state = 86
                self.match(BiosymMRParser.Atom_selection)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Distance_constraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def distance_constraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Distance_constraintContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Distance_constraintContext,i)


        def getRuleIndex(self):
            return BiosymMRParser.RULE_distance_constraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistance_constraints" ):
                listener.enterDistance_constraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistance_constraints" ):
                listener.exitDistance_constraints(self)




    def distance_constraints(self):

        localctx = BiosymMRParser.Distance_constraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_distance_constraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 92
                    self.distance_constraint()

                else:
                    raise NoViableAltException(self)
                self.state = 95 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Distance_constraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Atom_selection(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Atom_selection)
            else:
                return self.getToken(BiosymMRParser.Atom_selection, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.NumberContext,i)


        def Ordinal(self):
            return self.getToken(BiosymMRParser.Ordinal, 0)

        def Or(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Or)
            else:
                return self.getToken(BiosymMRParser.Or, i)

        def getRuleIndex(self):
            return BiosymMRParser.RULE_distance_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistance_constraint" ):
                listener.enterDistance_constraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistance_constraint" ):
                listener.exitDistance_constraint(self)




    def distance_constraint(self):

        localctx = BiosymMRParser.Distance_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_distance_constraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 97
                self.match(BiosymMRParser.Ordinal)


            self.state = 100
            self.match(BiosymMRParser.Atom_selection)
            self.state = 101
            self.match(BiosymMRParser.Atom_selection)
            self.state = 102
            self.number()
            self.state = 103
            self.number()
            self.state = 104
            self.number()
            self.state = 105
            self.number()
            self.state = 106
            self.number()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 107
                self.match(BiosymMRParser.Or)
                self.state = 108
                self.match(BiosymMRParser.Atom_selection)
                self.state = 109
                self.match(BiosymMRParser.Atom_selection)
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Distance_wo_w_constraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def distance_wo_w_constraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Distance_wo_w_constraintContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Distance_wo_w_constraintContext,i)


        def getRuleIndex(self):
            return BiosymMRParser.RULE_distance_wo_w_constraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistance_wo_w_constraints" ):
                listener.enterDistance_wo_w_constraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistance_wo_w_constraints" ):
                listener.exitDistance_wo_w_constraints(self)




    def distance_wo_w_constraints(self):

        localctx = BiosymMRParser.Distance_wo_w_constraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_distance_wo_w_constraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 115
                    self.distance_wo_w_constraint()

                else:
                    raise NoViableAltException(self)
                self.state = 118 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Distance_wo_w_constraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Atom_selection(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Atom_selection)
            else:
                return self.getToken(BiosymMRParser.Atom_selection, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.NumberContext,i)


        def Ordinal(self):
            return self.getToken(BiosymMRParser.Ordinal, 0)

        def Or(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Or)
            else:
                return self.getToken(BiosymMRParser.Or, i)

        def getRuleIndex(self):
            return BiosymMRParser.RULE_distance_wo_w_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistance_wo_w_constraint" ):
                listener.enterDistance_wo_w_constraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistance_wo_w_constraint" ):
                listener.exitDistance_wo_w_constraint(self)




    def distance_wo_w_constraint(self):

        localctx = BiosymMRParser.Distance_wo_w_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_distance_wo_w_constraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 120
                self.match(BiosymMRParser.Ordinal)


            self.state = 123
            self.match(BiosymMRParser.Atom_selection)
            self.state = 124
            self.match(BiosymMRParser.Atom_selection)
            self.state = 125
            self.number()
            self.state = 126
            self.number()
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                self.state = 127
                self.number()


            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 130
                self.match(BiosymMRParser.Or)
                self.state = 131
                self.match(BiosymMRParser.Atom_selection)
                self.state = 132
                self.match(BiosymMRParser.Atom_selection)
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dihedral_angle_restraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dihedral_angle_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Dihedral_angle_restraintContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Dihedral_angle_restraintContext,i)


        def getRuleIndex(self):
            return BiosymMRParser.RULE_dihedral_angle_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDihedral_angle_restraints" ):
                listener.enterDihedral_angle_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDihedral_angle_restraints" ):
                listener.exitDihedral_angle_restraints(self)




    def dihedral_angle_restraints(self):

        localctx = BiosymMRParser.Dihedral_angle_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_dihedral_angle_restraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 138
                    self.dihedral_angle_restraint()

                else:
                    raise NoViableAltException(self)
                self.state = 141 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dihedral_angle_restraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Atom_selection(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Atom_selection)
            else:
                return self.getToken(BiosymMRParser.Atom_selection, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.NumberContext,i)


        def Ordinal(self):
            return self.getToken(BiosymMRParser.Ordinal, 0)

        def getRuleIndex(self):
            return BiosymMRParser.RULE_dihedral_angle_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDihedral_angle_restraint" ):
                listener.enterDihedral_angle_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDihedral_angle_restraint" ):
                listener.exitDihedral_angle_restraint(self)




    def dihedral_angle_restraint(self):

        localctx = BiosymMRParser.Dihedral_angle_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_dihedral_angle_restraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 143
                self.match(BiosymMRParser.Ordinal)


            self.state = 146
            self.match(BiosymMRParser.Atom_selection)
            self.state = 147
            self.match(BiosymMRParser.Atom_selection)
            self.state = 148
            self.match(BiosymMRParser.Atom_selection)
            self.state = 149
            self.match(BiosymMRParser.Atom_selection)
            self.state = 150
            self.number()
            self.state = 151
            self.number()
            self.state = 152
            self.number()
            self.state = 153
            self.number()
            self.state = 154
            self.number()
            self.state = 155
            self.number()
            self.state = 156
            self.number()
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 157
                self.number()
                self.state = 158
                self.number()


            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 162
                self.number()
                self.state = 163
                self.number()


            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                self.state = 167
                self.number()
                self.state = 168
                self.number()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dihedral_angle_constraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dihedral_angle_constraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Dihedral_angle_constraintContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Dihedral_angle_constraintContext,i)


        def getRuleIndex(self):
            return BiosymMRParser.RULE_dihedral_angle_constraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDihedral_angle_constraints" ):
                listener.enterDihedral_angle_constraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDihedral_angle_constraints" ):
                listener.exitDihedral_angle_constraints(self)




    def dihedral_angle_constraints(self):

        localctx = BiosymMRParser.Dihedral_angle_constraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_dihedral_angle_constraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 172
                    self.dihedral_angle_constraint()

                else:
                    raise NoViableAltException(self)
                self.state = 175 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dihedral_angle_constraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Atom_selection(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Atom_selection)
            else:
                return self.getToken(BiosymMRParser.Atom_selection, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.NumberContext,i)


        def Ordinal(self):
            return self.getToken(BiosymMRParser.Ordinal, 0)

        def getRuleIndex(self):
            return BiosymMRParser.RULE_dihedral_angle_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDihedral_angle_constraint" ):
                listener.enterDihedral_angle_constraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDihedral_angle_constraint" ):
                listener.exitDihedral_angle_constraint(self)




    def dihedral_angle_constraint(self):

        localctx = BiosymMRParser.Dihedral_angle_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_dihedral_angle_constraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 177
                self.match(BiosymMRParser.Ordinal)


            self.state = 180
            self.match(BiosymMRParser.Atom_selection)
            self.state = 181
            self.match(BiosymMRParser.Atom_selection)
            self.state = 182
            self.match(BiosymMRParser.Atom_selection)
            self.state = 183
            self.match(BiosymMRParser.Atom_selection)
            self.state = 184
            self.number()
            self.state = 185
            self.number()
            self.state = 186
            self.number()
            self.state = 187
            self.number()
            self.state = 188
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dihedral_angle_wo_w_constraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dihedral_angle_wo_w_constraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Dihedral_angle_wo_w_constraintContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Dihedral_angle_wo_w_constraintContext,i)


        def getRuleIndex(self):
            return BiosymMRParser.RULE_dihedral_angle_wo_w_constraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDihedral_angle_wo_w_constraints" ):
                listener.enterDihedral_angle_wo_w_constraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDihedral_angle_wo_w_constraints" ):
                listener.exitDihedral_angle_wo_w_constraints(self)




    def dihedral_angle_wo_w_constraints(self):

        localctx = BiosymMRParser.Dihedral_angle_wo_w_constraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_dihedral_angle_wo_w_constraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 190
                    self.dihedral_angle_wo_w_constraint()

                else:
                    raise NoViableAltException(self)
                self.state = 193 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dihedral_angle_wo_w_constraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Atom_selection(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Atom_selection)
            else:
                return self.getToken(BiosymMRParser.Atom_selection, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.NumberContext,i)


        def Ordinal(self):
            return self.getToken(BiosymMRParser.Ordinal, 0)

        def getRuleIndex(self):
            return BiosymMRParser.RULE_dihedral_angle_wo_w_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDihedral_angle_wo_w_constraint" ):
                listener.enterDihedral_angle_wo_w_constraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDihedral_angle_wo_w_constraint" ):
                listener.exitDihedral_angle_wo_w_constraint(self)




    def dihedral_angle_wo_w_constraint(self):

        localctx = BiosymMRParser.Dihedral_angle_wo_w_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_dihedral_angle_wo_w_constraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 195
                self.match(BiosymMRParser.Ordinal)


            self.state = 198
            self.match(BiosymMRParser.Atom_selection)
            self.state = 199
            self.match(BiosymMRParser.Atom_selection)
            self.state = 200
            self.match(BiosymMRParser.Atom_selection)
            self.state = 201
            self.match(BiosymMRParser.Atom_selection)
            self.state = 202
            self.number()
            self.state = 203
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Chirality_constraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def chirality_constraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Chirality_constraintContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Chirality_constraintContext,i)


        def getRuleIndex(self):
            return BiosymMRParser.RULE_chirality_constraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChirality_constraints" ):
                listener.enterChirality_constraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChirality_constraints" ):
                listener.exitChirality_constraints(self)




    def chirality_constraints(self):

        localctx = BiosymMRParser.Chirality_constraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_chirality_constraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 205
                    self.chirality_constraint()

                else:
                    raise NoViableAltException(self)
                self.state = 208 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Chirality_constraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Atom_selection(self):
            return self.getToken(BiosymMRParser.Atom_selection, 0)

        def Chiral_code(self):
            return self.getToken(BiosymMRParser.Chiral_code, 0)

        def Ordinal(self):
            return self.getToken(BiosymMRParser.Ordinal, 0)

        def getRuleIndex(self):
            return BiosymMRParser.RULE_chirality_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChirality_constraint" ):
                listener.enterChirality_constraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChirality_constraint" ):
                listener.exitChirality_constraint(self)




    def chirality_constraint(self):

        localctx = BiosymMRParser.Chirality_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_chirality_constraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 210
                self.match(BiosymMRParser.Ordinal)


            self.state = 213
            self.match(BiosymMRParser.Atom_selection)
            self.state = 214
            self.match(BiosymMRParser.Chiral_code)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prochirality_constraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prochirality_constraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Prochirality_constraintContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Prochirality_constraintContext,i)


        def getRuleIndex(self):
            return BiosymMRParser.RULE_prochirality_constraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProchirality_constraints" ):
                listener.enterProchirality_constraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProchirality_constraints" ):
                listener.exitProchirality_constraints(self)




    def prochirality_constraints(self):

        localctx = BiosymMRParser.Prochirality_constraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_prochirality_constraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 216
                    self.prochirality_constraint()

                else:
                    raise NoViableAltException(self)
                self.state = 219 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prochirality_constraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Atom_selection(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Atom_selection)
            else:
                return self.getToken(BiosymMRParser.Atom_selection, i)

        def Ordinal(self):
            return self.getToken(BiosymMRParser.Ordinal, 0)

        def getRuleIndex(self):
            return BiosymMRParser.RULE_prochirality_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProchirality_constraint" ):
                listener.enterProchirality_constraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProchirality_constraint" ):
                listener.exitProchirality_constraint(self)




    def prochirality_constraint(self):

        localctx = BiosymMRParser.Prochirality_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_prochirality_constraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 221
                self.match(BiosymMRParser.Ordinal)


            self.state = 224
            self.match(BiosymMRParser.Atom_selection)
            self.state = 225
            self.match(BiosymMRParser.Atom_selection)
            self.state = 226
            self.match(BiosymMRParser.Atom_selection)
            self.state = 227
            self.match(BiosymMRParser.Atom_selection)
            self.state = 228
            self.match(BiosymMRParser.Atom_selection)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mixing_timeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Mixing_times(self):
            return self.getToken(BiosymMRParser.Mixing_times, 0)

        def RETURN_MT(self):
            return self.getToken(BiosymMRParser.RETURN_MT, 0)

        def Real_MT(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Real_MT)
            else:
                return self.getToken(BiosymMRParser.Real_MT, i)

        def Float_MT(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Float_MT)
            else:
                return self.getToken(BiosymMRParser.Float_MT, i)

        def Integer_MT(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Integer_MT)
            else:
                return self.getToken(BiosymMRParser.Integer_MT, i)

        def Comma_MT(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Comma_MT)
            else:
                return self.getToken(BiosymMRParser.Comma_MT, i)

        def Period_MT(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Period_MT)
            else:
                return self.getToken(BiosymMRParser.Period_MT, i)

        def getRuleIndex(self):
            return BiosymMRParser.RULE_mixing_time

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMixing_time" ):
                listener.enterMixing_time(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMixing_time" ):
                listener.exitMixing_time(self)




    def mixing_time(self):

        localctx = BiosymMRParser.Mixing_timeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_mixing_time)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(BiosymMRParser.Mixing_times)
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1879048192) != 0):
                self.state = 231
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1879048192) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31 or _la==32:
                    self.state = 232
                    _la = self._input.LA(1)
                    if not(_la==31 or _la==32):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 240
            self.match(BiosymMRParser.RETURN_MT)
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
            return self.getToken(BiosymMRParser.Float, 0)

        def Float_DecimalComma(self):
            return self.getToken(BiosymMRParser.Float_DecimalComma, 0)

        def Integer(self):
            return self.getToken(BiosymMRParser.Integer, 0)

        def getRuleIndex(self):
            return BiosymMRParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = BiosymMRParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
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


    class Ins_distance_restraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ins_distance_restraint(self):
            return self.getTypedRuleContext(BiosymMRParser.Ins_distance_restraintContext,0)


        def getRuleIndex(self):
            return BiosymMRParser.RULE_ins_distance_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIns_distance_restraints" ):
                listener.enterIns_distance_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIns_distance_restraints" ):
                listener.exitIns_distance_restraints(self)




    def ins_distance_restraints(self):

        localctx = BiosymMRParser.Ins_distance_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_ins_distance_restraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.ins_distance_restraint()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ins_distance_restraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_create(self):
            return self.getTypedRuleContext(BiosymMRParser.Decl_createContext,0)


        def decl_function(self):
            return self.getTypedRuleContext(BiosymMRParser.Decl_functionContext,0)


        def decl_target(self):
            return self.getTypedRuleContext(BiosymMRParser.Decl_targetContext,0)


        def getRuleIndex(self):
            return BiosymMRParser.RULE_ins_distance_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIns_distance_restraint" ):
                listener.enterIns_distance_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIns_distance_restraint" ):
                listener.exitIns_distance_restraint(self)




    def ins_distance_restraint(self):

        localctx = BiosymMRParser.Ins_distance_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_ins_distance_restraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.decl_create()
            self.state = 247
            self.decl_function()
            self.state = 248
            self.decl_target()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_createContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Restraint(self):
            return self.getToken(BiosymMRParser.Restraint, 0)

        def Create(self):
            return self.getToken(BiosymMRParser.Create, 0)

        def Double_quote_string(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Double_quote_string)
            else:
                return self.getToken(BiosymMRParser.Double_quote_string, i)

        def Distance(self):
            return self.getToken(BiosymMRParser.Distance, 0)

        def RETURN_II(self):
            return self.getToken(BiosymMRParser.RETURN_II, 0)

        def getRuleIndex(self):
            return BiosymMRParser.RULE_decl_create

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl_create" ):
                listener.enterDecl_create(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl_create" ):
                listener.exitDecl_create(self)




    def decl_create(self):

        localctx = BiosymMRParser.Decl_createContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_decl_create)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(BiosymMRParser.Restraint)
            self.state = 251
            self.match(BiosymMRParser.Create)
            self.state = 252
            self.match(BiosymMRParser.Double_quote_string)
            self.state = 253
            self.match(BiosymMRParser.Distance)
            self.state = 254
            self.match(BiosymMRParser.Double_quote_string)
            self.state = 255
            self.match(BiosymMRParser.Double_quote_string)
            self.state = 256
            self.match(BiosymMRParser.RETURN_II)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Restraint(self):
            return self.getToken(BiosymMRParser.Restraint, 0)

        def Function(self):
            return self.getToken(BiosymMRParser.Function, 0)

        def Double_quote_string(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Double_quote_string)
            else:
                return self.getToken(BiosymMRParser.Double_quote_string, i)

        def RETURN_II(self):
            return self.getToken(BiosymMRParser.RETURN_II, 0)

        def Quadratic(self):
            return self.getToken(BiosymMRParser.Quadratic, 0)

        def Flat_bottomed(self):
            return self.getToken(BiosymMRParser.Flat_bottomed, 0)

        def getRuleIndex(self):
            return BiosymMRParser.RULE_decl_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl_function" ):
                listener.enterDecl_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl_function" ):
                listener.exitDecl_function(self)




    def decl_function(self):

        localctx = BiosymMRParser.Decl_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_decl_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(BiosymMRParser.Restraint)
            self.state = 259
            self.match(BiosymMRParser.Function)
            self.state = 260
            self.match(BiosymMRParser.Double_quote_string)
            self.state = 261
            _la = self._input.LA(1)
            if not(_la==23 or _la==24):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 262
            self.match(BiosymMRParser.Double_quote_string)
            self.state = 263
            self.match(BiosymMRParser.Double_quote_string)
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 264
                self.match(BiosymMRParser.Double_quote_string)


            self.state = 267
            self.match(BiosymMRParser.RETURN_II)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_targetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Restraint(self):
            return self.getToken(BiosymMRParser.Restraint, 0)

        def Target(self):
            return self.getToken(BiosymMRParser.Target, 0)

        def Double_quote_string(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Double_quote_string)
            else:
                return self.getToken(BiosymMRParser.Double_quote_string, i)

        def RETURN_II(self):
            return self.getToken(BiosymMRParser.RETURN_II, 0)

        def Relative(self):
            return self.getToken(BiosymMRParser.Relative, 0)

        def getRuleIndex(self):
            return BiosymMRParser.RULE_decl_target

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl_target" ):
                listener.enterDecl_target(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl_target" ):
                listener.exitDecl_target(self)




    def decl_target(self):

        localctx = BiosymMRParser.Decl_targetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_decl_target)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(BiosymMRParser.Restraint)
            self.state = 270
            self.match(BiosymMRParser.Target)
            self.state = 271
            self.match(BiosymMRParser.Double_quote_string)
            self.state = 272
            _la = self._input.LA(1)
            if not(_la==18 or _la==25):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 273
            self.match(BiosymMRParser.Double_quote_string)
            self.state = 274
            self.match(BiosymMRParser.RETURN_II)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





