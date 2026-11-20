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
        4,1,34,297,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,64,8,0,10,0,12,0,67,9,0,1,
        0,1,0,1,1,4,1,72,8,1,11,1,12,1,73,1,2,3,2,77,8,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,3,2,88,8,2,1,2,1,2,1,2,5,2,93,8,2,10,2,12,2,
        96,9,2,1,3,4,3,99,8,3,11,3,12,3,100,1,4,3,4,104,8,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,116,8,4,10,4,12,4,119,9,4,1,5,4,
        5,122,8,5,11,5,12,5,123,1,6,3,6,127,8,6,1,6,1,6,1,6,1,6,1,6,3,6,
        134,8,6,1,6,1,6,1,6,5,6,139,8,6,10,6,12,6,142,9,6,1,7,4,7,145,8,
        7,11,7,12,7,146,1,8,3,8,150,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,3,8,166,8,8,1,8,1,8,1,8,3,8,171,8,8,1,8,
        1,8,1,8,3,8,176,8,8,1,9,4,9,179,8,9,11,9,12,9,180,1,10,3,10,184,
        8,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,4,11,
        197,8,11,11,11,12,11,198,1,12,3,12,202,8,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,13,4,13,212,8,13,11,13,12,13,213,1,14,3,14,217,
        8,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,4,15,227,8,15,11,15,
        12,15,228,1,16,3,16,232,8,16,1,16,1,16,1,16,1,17,4,17,238,8,17,11,
        17,12,17,239,1,18,3,18,243,8,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        19,1,19,1,19,3,19,254,8,19,5,19,256,8,19,10,19,12,19,259,9,19,1,
        19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,
        23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,286,
        8,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,0,0,26,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,
        48,50,0,5,1,0,28,30,1,0,31,32,1,0,1,3,1,0,23,24,2,0,18,18,25,25,
        310,0,65,1,0,0,0,2,71,1,0,0,0,4,76,1,0,0,0,6,98,1,0,0,0,8,103,1,
        0,0,0,10,121,1,0,0,0,12,126,1,0,0,0,14,144,1,0,0,0,16,149,1,0,0,
        0,18,178,1,0,0,0,20,183,1,0,0,0,22,196,1,0,0,0,24,201,1,0,0,0,26,
        211,1,0,0,0,28,216,1,0,0,0,30,226,1,0,0,0,32,231,1,0,0,0,34,237,
        1,0,0,0,36,242,1,0,0,0,38,250,1,0,0,0,40,262,1,0,0,0,42,264,1,0,
        0,0,44,266,1,0,0,0,46,270,1,0,0,0,48,278,1,0,0,0,50,289,1,0,0,0,
        52,64,3,2,1,0,53,64,3,6,3,0,54,64,3,10,5,0,55,64,3,14,7,0,56,64,
        3,18,9,0,57,64,3,22,11,0,58,64,3,26,13,0,59,64,3,30,15,0,60,64,3,
        34,17,0,61,64,3,38,19,0,62,64,3,42,21,0,63,52,1,0,0,0,63,53,1,0,
        0,0,63,54,1,0,0,0,63,55,1,0,0,0,63,56,1,0,0,0,63,57,1,0,0,0,63,58,
        1,0,0,0,63,59,1,0,0,0,63,60,1,0,0,0,63,61,1,0,0,0,63,62,1,0,0,0,
        64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,65,1,
        0,0,0,68,69,5,0,0,1,69,1,1,0,0,0,70,72,3,4,2,0,71,70,1,0,0,0,72,
        73,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,3,1,0,0,0,75,77,5,10,0,
        0,76,75,1,0,0,0,76,77,1,0,0,0,77,78,1,0,0,0,78,79,5,9,0,0,79,80,
        5,9,0,0,80,81,3,40,20,0,81,82,3,40,20,0,82,83,3,40,20,0,83,84,3,
        40,20,0,84,85,3,40,20,0,85,87,3,40,20,0,86,88,3,40,20,0,87,86,1,
        0,0,0,87,88,1,0,0,0,88,94,1,0,0,0,89,90,5,11,0,0,90,91,5,9,0,0,91,
        93,5,9,0,0,92,89,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,
        0,95,5,1,0,0,0,96,94,1,0,0,0,97,99,3,8,4,0,98,97,1,0,0,0,99,100,
        1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,7,1,0,0,0,102,104,5,10,
        0,0,103,102,1,0,0,0,103,104,1,0,0,0,104,105,1,0,0,0,105,106,5,9,
        0,0,106,107,5,9,0,0,107,108,3,40,20,0,108,109,3,40,20,0,109,110,
        3,40,20,0,110,111,3,40,20,0,111,117,3,40,20,0,112,113,5,11,0,0,113,
        114,5,9,0,0,114,116,5,9,0,0,115,112,1,0,0,0,116,119,1,0,0,0,117,
        115,1,0,0,0,117,118,1,0,0,0,118,9,1,0,0,0,119,117,1,0,0,0,120,122,
        3,12,6,0,121,120,1,0,0,0,122,123,1,0,0,0,123,121,1,0,0,0,123,124,
        1,0,0,0,124,11,1,0,0,0,125,127,5,10,0,0,126,125,1,0,0,0,126,127,
        1,0,0,0,127,128,1,0,0,0,128,129,5,9,0,0,129,130,5,9,0,0,130,131,
        3,40,20,0,131,133,3,40,20,0,132,134,3,40,20,0,133,132,1,0,0,0,133,
        134,1,0,0,0,134,140,1,0,0,0,135,136,5,11,0,0,136,137,5,9,0,0,137,
        139,5,9,0,0,138,135,1,0,0,0,139,142,1,0,0,0,140,138,1,0,0,0,140,
        141,1,0,0,0,141,13,1,0,0,0,142,140,1,0,0,0,143,145,3,16,8,0,144,
        143,1,0,0,0,145,146,1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,0,147,
        15,1,0,0,0,148,150,5,10,0,0,149,148,1,0,0,0,149,150,1,0,0,0,150,
        151,1,0,0,0,151,152,5,9,0,0,152,153,5,9,0,0,153,154,5,9,0,0,154,
        155,5,9,0,0,155,156,3,40,20,0,156,157,3,40,20,0,157,158,3,40,20,
        0,158,159,3,40,20,0,159,160,3,40,20,0,160,161,3,40,20,0,161,165,
        3,40,20,0,162,163,3,40,20,0,163,164,3,40,20,0,164,166,1,0,0,0,165,
        162,1,0,0,0,165,166,1,0,0,0,166,170,1,0,0,0,167,168,3,40,20,0,168,
        169,3,40,20,0,169,171,1,0,0,0,170,167,1,0,0,0,170,171,1,0,0,0,171,
        175,1,0,0,0,172,173,3,40,20,0,173,174,3,40,20,0,174,176,1,0,0,0,
        175,172,1,0,0,0,175,176,1,0,0,0,176,17,1,0,0,0,177,179,3,20,10,0,
        178,177,1,0,0,0,179,180,1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,
        181,19,1,0,0,0,182,184,5,10,0,0,183,182,1,0,0,0,183,184,1,0,0,0,
        184,185,1,0,0,0,185,186,5,9,0,0,186,187,5,9,0,0,187,188,5,9,0,0,
        188,189,5,9,0,0,189,190,3,40,20,0,190,191,3,40,20,0,191,192,3,40,
        20,0,192,193,3,40,20,0,193,194,3,40,20,0,194,21,1,0,0,0,195,197,
        3,24,12,0,196,195,1,0,0,0,197,198,1,0,0,0,198,196,1,0,0,0,198,199,
        1,0,0,0,199,23,1,0,0,0,200,202,5,10,0,0,201,200,1,0,0,0,201,202,
        1,0,0,0,202,203,1,0,0,0,203,204,5,9,0,0,204,205,5,9,0,0,205,206,
        5,9,0,0,206,207,5,9,0,0,207,208,3,40,20,0,208,209,3,40,20,0,209,
        25,1,0,0,0,210,212,3,28,14,0,211,210,1,0,0,0,212,213,1,0,0,0,213,
        211,1,0,0,0,213,214,1,0,0,0,214,27,1,0,0,0,215,217,5,10,0,0,216,
        215,1,0,0,0,216,217,1,0,0,0,217,218,1,0,0,0,218,219,5,9,0,0,219,
        220,5,9,0,0,220,221,3,40,20,0,221,222,3,40,20,0,222,223,3,40,20,
        0,223,224,3,40,20,0,224,29,1,0,0,0,225,227,3,32,16,0,226,225,1,0,
        0,0,227,228,1,0,0,0,228,226,1,0,0,0,228,229,1,0,0,0,229,31,1,0,0,
        0,230,232,5,10,0,0,231,230,1,0,0,0,231,232,1,0,0,0,232,233,1,0,0,
        0,233,234,5,9,0,0,234,235,5,8,0,0,235,33,1,0,0,0,236,238,3,36,18,
        0,237,236,1,0,0,0,238,239,1,0,0,0,239,237,1,0,0,0,239,240,1,0,0,
        0,240,35,1,0,0,0,241,243,5,10,0,0,242,241,1,0,0,0,242,243,1,0,0,
        0,243,244,1,0,0,0,244,245,5,9,0,0,245,246,5,9,0,0,246,247,5,9,0,
        0,247,248,5,9,0,0,248,249,5,9,0,0,249,37,1,0,0,0,250,257,5,13,0,
        0,251,253,7,0,0,0,252,254,7,1,0,0,253,252,1,0,0,0,253,254,1,0,0,
        0,254,256,1,0,0,0,255,251,1,0,0,0,256,259,1,0,0,0,257,255,1,0,0,
        0,257,258,1,0,0,0,258,260,1,0,0,0,259,257,1,0,0,0,260,261,5,34,0,
        0,261,39,1,0,0,0,262,263,7,2,0,0,263,41,1,0,0,0,264,265,3,44,22,
        0,265,43,1,0,0,0,266,267,3,46,23,0,267,268,3,48,24,0,268,269,3,50,
        25,0,269,45,1,0,0,0,270,271,5,12,0,0,271,272,5,19,0,0,272,273,5,
        18,0,0,273,274,5,22,0,0,274,275,5,18,0,0,275,276,5,18,0,0,276,277,
        5,27,0,0,277,47,1,0,0,0,278,279,5,12,0,0,279,280,5,20,0,0,280,281,
        5,18,0,0,281,282,7,3,0,0,282,283,5,18,0,0,283,285,5,18,0,0,284,286,
        5,18,0,0,285,284,1,0,0,0,285,286,1,0,0,0,286,287,1,0,0,0,287,288,
        5,27,0,0,288,49,1,0,0,0,289,290,5,12,0,0,290,291,5,21,0,0,291,292,
        5,18,0,0,292,293,7,4,0,0,293,294,5,18,0,0,294,295,5,27,0,0,295,51,
        1,0,0,0,31,63,65,73,76,87,94,100,103,117,123,126,133,140,146,149,
        165,170,175,180,183,198,201,213,216,228,231,239,242,253,257,285
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
    RULE_rdc_restraints = 13
    RULE_rdc_restraint = 14
    RULE_chirality_constraints = 15
    RULE_chirality_constraint = 16
    RULE_prochirality_constraints = 17
    RULE_prochirality_constraint = 18
    RULE_mixing_time = 19
    RULE_number = 20
    RULE_ins_distance_restraints = 21
    RULE_ins_distance_restraint = 22
    RULE_decl_create = 23
    RULE_decl_function = 24
    RULE_decl_target = 25

    ruleNames =  [ "biosym_mr", "distance_restraints", "distance_restraint", 
                   "distance_constraints", "distance_constraint", "distance_wo_w_constraints", 
                   "distance_wo_w_constraint", "dihedral_angle_restraints", 
                   "dihedral_angle_restraint", "dihedral_angle_constraints", 
                   "dihedral_angle_constraint", "dihedral_angle_wo_w_constraints", 
                   "dihedral_angle_wo_w_constraint", "rdc_restraints", "rdc_restraint", 
                   "chirality_constraints", "chirality_constraint", "prochirality_constraints", 
                   "prochirality_constraint", "mixing_time", "number", "ins_distance_restraints", 
                   "ins_distance_restraint", "decl_create", "decl_function", 
                   "decl_target" ]

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


        def rdc_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Rdc_restraintsContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Rdc_restraintsContext,i)


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
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 13824) != 0):
                self.state = 63
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 52
                    self.distance_restraints()
                    pass

                elif la_ == 2:
                    self.state = 53
                    self.distance_constraints()
                    pass

                elif la_ == 3:
                    self.state = 54
                    self.distance_wo_w_constraints()
                    pass

                elif la_ == 4:
                    self.state = 55
                    self.dihedral_angle_restraints()
                    pass

                elif la_ == 5:
                    self.state = 56
                    self.dihedral_angle_constraints()
                    pass

                elif la_ == 6:
                    self.state = 57
                    self.dihedral_angle_wo_w_constraints()
                    pass

                elif la_ == 7:
                    self.state = 58
                    self.rdc_restraints()
                    pass

                elif la_ == 8:
                    self.state = 59
                    self.chirality_constraints()
                    pass

                elif la_ == 9:
                    self.state = 60
                    self.prochirality_constraints()
                    pass

                elif la_ == 10:
                    self.state = 61
                    self.mixing_time()
                    pass

                elif la_ == 11:
                    self.state = 62
                    self.ins_distance_restraints()
                    pass


                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
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
            self.state = 71 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 70
                    self.distance_restraint()

                else:
                    raise NoViableAltException(self)
                self.state = 73 
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
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 75
                self.match(BiosymMRParser.Ordinal)


            self.state = 78
            self.match(BiosymMRParser.Atom_selection)
            self.state = 79
            self.match(BiosymMRParser.Atom_selection)
            self.state = 80
            self.number()
            self.state = 81
            self.number()
            self.state = 82
            self.number()
            self.state = 83
            self.number()
            self.state = 84
            self.number()
            self.state = 85
            self.number()
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                self.state = 86
                self.number()


            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 89
                self.match(BiosymMRParser.Or)
                self.state = 90
                self.match(BiosymMRParser.Atom_selection)
                self.state = 91
                self.match(BiosymMRParser.Atom_selection)
                self.state = 96
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
            self.state = 98 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 97
                    self.distance_constraint()

                else:
                    raise NoViableAltException(self)
                self.state = 100 
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
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 102
                self.match(BiosymMRParser.Ordinal)


            self.state = 105
            self.match(BiosymMRParser.Atom_selection)
            self.state = 106
            self.match(BiosymMRParser.Atom_selection)
            self.state = 107
            self.number()
            self.state = 108
            self.number()
            self.state = 109
            self.number()
            self.state = 110
            self.number()
            self.state = 111
            self.number()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 112
                self.match(BiosymMRParser.Or)
                self.state = 113
                self.match(BiosymMRParser.Atom_selection)
                self.state = 114
                self.match(BiosymMRParser.Atom_selection)
                self.state = 119
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
            self.state = 121 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 120
                    self.distance_wo_w_constraint()

                else:
                    raise NoViableAltException(self)
                self.state = 123 
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
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 125
                self.match(BiosymMRParser.Ordinal)


            self.state = 128
            self.match(BiosymMRParser.Atom_selection)
            self.state = 129
            self.match(BiosymMRParser.Atom_selection)
            self.state = 130
            self.number()
            self.state = 131
            self.number()
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                self.state = 132
                self.number()


            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 135
                self.match(BiosymMRParser.Or)
                self.state = 136
                self.match(BiosymMRParser.Atom_selection)
                self.state = 137
                self.match(BiosymMRParser.Atom_selection)
                self.state = 142
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
            self.state = 144 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 143
                    self.dihedral_angle_restraint()

                else:
                    raise NoViableAltException(self)
                self.state = 146 
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
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 148
                self.match(BiosymMRParser.Ordinal)


            self.state = 151
            self.match(BiosymMRParser.Atom_selection)
            self.state = 152
            self.match(BiosymMRParser.Atom_selection)
            self.state = 153
            self.match(BiosymMRParser.Atom_selection)
            self.state = 154
            self.match(BiosymMRParser.Atom_selection)
            self.state = 155
            self.number()
            self.state = 156
            self.number()
            self.state = 157
            self.number()
            self.state = 158
            self.number()
            self.state = 159
            self.number()
            self.state = 160
            self.number()
            self.state = 161
            self.number()
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 162
                self.number()
                self.state = 163
                self.number()


            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 167
                self.number()
                self.state = 168
                self.number()


            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                self.state = 172
                self.number()
                self.state = 173
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
            self.state = 178 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 177
                    self.dihedral_angle_constraint()

                else:
                    raise NoViableAltException(self)
                self.state = 180 
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
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 182
                self.match(BiosymMRParser.Ordinal)


            self.state = 185
            self.match(BiosymMRParser.Atom_selection)
            self.state = 186
            self.match(BiosymMRParser.Atom_selection)
            self.state = 187
            self.match(BiosymMRParser.Atom_selection)
            self.state = 188
            self.match(BiosymMRParser.Atom_selection)
            self.state = 189
            self.number()
            self.state = 190
            self.number()
            self.state = 191
            self.number()
            self.state = 192
            self.number()
            self.state = 193
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
            self.state = 196 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 195
                    self.dihedral_angle_wo_w_constraint()

                else:
                    raise NoViableAltException(self)
                self.state = 198 
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
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 200
                self.match(BiosymMRParser.Ordinal)


            self.state = 203
            self.match(BiosymMRParser.Atom_selection)
            self.state = 204
            self.match(BiosymMRParser.Atom_selection)
            self.state = 205
            self.match(BiosymMRParser.Atom_selection)
            self.state = 206
            self.match(BiosymMRParser.Atom_selection)
            self.state = 207
            self.number()
            self.state = 208
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rdc_restraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rdc_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Rdc_restraintContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Rdc_restraintContext,i)


        def getRuleIndex(self):
            return BiosymMRParser.RULE_rdc_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRdc_restraints" ):
                listener.enterRdc_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRdc_restraints" ):
                listener.exitRdc_restraints(self)




    def rdc_restraints(self):

        localctx = BiosymMRParser.Rdc_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_rdc_restraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 210
                    self.rdc_restraint()

                else:
                    raise NoViableAltException(self)
                self.state = 213 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rdc_restraintContext(ParserRuleContext):
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
            return BiosymMRParser.RULE_rdc_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRdc_restraint" ):
                listener.enterRdc_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRdc_restraint" ):
                listener.exitRdc_restraint(self)




    def rdc_restraint(self):

        localctx = BiosymMRParser.Rdc_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_rdc_restraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 215
                self.match(BiosymMRParser.Ordinal)


            self.state = 218
            self.match(BiosymMRParser.Atom_selection)
            self.state = 219
            self.match(BiosymMRParser.Atom_selection)
            self.state = 220
            self.number()
            self.state = 221
            self.number()
            self.state = 222
            self.number()
            self.state = 223
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
        self.enterRule(localctx, 30, self.RULE_chirality_constraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 225
                    self.chirality_constraint()

                else:
                    raise NoViableAltException(self)
                self.state = 228 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
        self.enterRule(localctx, 32, self.RULE_chirality_constraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 230
                self.match(BiosymMRParser.Ordinal)


            self.state = 233
            self.match(BiosymMRParser.Atom_selection)
            self.state = 234
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
        self.enterRule(localctx, 34, self.RULE_prochirality_constraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 236
                    self.prochirality_constraint()

                else:
                    raise NoViableAltException(self)
                self.state = 239 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        self.enterRule(localctx, 36, self.RULE_prochirality_constraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 241
                self.match(BiosymMRParser.Ordinal)


            self.state = 244
            self.match(BiosymMRParser.Atom_selection)
            self.state = 245
            self.match(BiosymMRParser.Atom_selection)
            self.state = 246
            self.match(BiosymMRParser.Atom_selection)
            self.state = 247
            self.match(BiosymMRParser.Atom_selection)
            self.state = 248
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
        self.enterRule(localctx, 38, self.RULE_mixing_time)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(BiosymMRParser.Mixing_times)
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1879048192) != 0):
                self.state = 251
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1879048192) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31 or _la==32:
                    self.state = 252
                    _la = self._input.LA(1)
                    if not(_la==31 or _la==32):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 260
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
        self.enterRule(localctx, 40, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
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
        self.enterRule(localctx, 42, self.RULE_ins_distance_restraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
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
        self.enterRule(localctx, 44, self.RULE_ins_distance_restraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.decl_create()
            self.state = 267
            self.decl_function()
            self.state = 268
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
        self.enterRule(localctx, 46, self.RULE_decl_create)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(BiosymMRParser.Restraint)
            self.state = 271
            self.match(BiosymMRParser.Create)
            self.state = 272
            self.match(BiosymMRParser.Double_quote_string)
            self.state = 273
            self.match(BiosymMRParser.Distance)
            self.state = 274
            self.match(BiosymMRParser.Double_quote_string)
            self.state = 275
            self.match(BiosymMRParser.Double_quote_string)
            self.state = 276
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
        self.enterRule(localctx, 48, self.RULE_decl_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(BiosymMRParser.Restraint)
            self.state = 279
            self.match(BiosymMRParser.Function)
            self.state = 280
            self.match(BiosymMRParser.Double_quote_string)
            self.state = 281
            _la = self._input.LA(1)
            if not(_la==23 or _la==24):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 282
            self.match(BiosymMRParser.Double_quote_string)
            self.state = 283
            self.match(BiosymMRParser.Double_quote_string)
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 284
                self.match(BiosymMRParser.Double_quote_string)


            self.state = 287
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
        self.enterRule(localctx, 50, self.RULE_decl_target)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(BiosymMRParser.Restraint)
            self.state = 290
            self.match(BiosymMRParser.Target)
            self.state = 291
            self.match(BiosymMRParser.Double_quote_string)
            self.state = 292
            _la = self._input.LA(1)
            if not(_la==18 or _la==25):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 293
            self.match(BiosymMRParser.Double_quote_string)
            self.state = 294
            self.match(BiosymMRParser.RETURN_II)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





