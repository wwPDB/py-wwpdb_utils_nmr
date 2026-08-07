
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CharmmMRLexer.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  CharmmMRLexer : public antlr4::Lexer {
public:
  enum {
    Set = 1, End = 2, Cons = 3, Harmonic = 4, Absolute = 5, Bestfit = 6, 
    Relative = 7, Clear = 8, Force = 9, Mass = 10, Weight = 11, Exponent = 12, 
    XScale = 13, YScale = 14, ZScale = 15, NoRotation = 16, NoTranslation = 17, 
    Main = 18, Comp = 19, Keep = 20, Dihedral = 21, ByNumber = 22, Min = 23, 
    Period = 24, Width = 25, ClDh = 26, IC = 27, Bond = 28, Upper = 29, 
    Angle = 30, Improper = 31, Droplet = 32, NoMass = 33, Fix = 34, Purg = 35, 
    Thet = 36, Phi = 37, Imph = 38, Hmcm = 39, RefX = 40, RefY = 41, RefZ = 42, 
    Shake = 43, Off = 44, NoReset = 45, BonH = 46, Tol = 47, MxIter = 48, 
    AngH = 49, Parameters = 50, ShkScale = 51, Fast = 52, Water = 53, NoFast = 54, 
    Noe = 55, Reset = 56, PNoe = 57, Assign = 58, KMin = 59, KMax = 60, 
    RMin = 61, RMax = 62, FMax = 63, MinDist = 64, RSwi = 65, SExp = 66, 
    SumR = 67, TCon = 68, RExp = 69, CnoX = 70, CnoY = 71, CnoZ = 72, MPNoe = 73, 
    INoe = 74, TnoX = 75, TnoY = 76, TnoZ = 77, NMPNoe = 78, Read = 79, 
    Write = 80, Unit = 81, Print = 82, Anal = 83, Cut = 84, Scale = 85, 
    Temperature = 86, ResDistance = 87, KVal = 88, RVal = 89, EVal = 90, 
    IVal = 91, Positive = 92, Negative = 93, Pull = 94, XDir = 95, YDir = 96, 
    ZDir = 97, EField = 98, List = 99, Switch = 100, SForce = 101, RMSD = 102, 
    MaxN = 103, NPrt = 104, Show = 105, Offset = 106, BOffset = 107, RGyration = 108, 
    Reference = 109, Orient = 110, Output = 111, NSave = 112, DMConstrain = 113, 
    Cutoff = 114, NContact = 115, Selection = 116, Or_op = 117, And_op = 118, 
    Not_op = 119, Around = 120, Subset = 121, Bonded = 122, ByRes = 123, 
    ByGroup = 124, SegIdentifier = 125, ISeg = 126, Residue = 127, IRes = 128, 
    Resname = 129, IGroup = 130, Type = 131, Chemical = 132, Atom = 133, 
    Property = 134, Point = 135, Initial = 136, Lone = 137, Hydrogen = 138, 
    User = 139, Previous = 140, Recall = 141, All = 142, NONE = 143, Integer = 144, 
    Real = 145, Double_quote_string = 146, SMCLN_COMMENT = 147, COMMENT = 148, 
    Simple_name = 149, Simple_names = 150, Integers = 151, L_paren = 152, 
    R_paren = 153, Colon = 154, Equ_op = 155, Lt_op = 156, Gt_op = 157, 
    Leq_op = 158, Geq_op = 159, Neq_op = 160, Aeq_op = 161, Symbol_name = 162, 
    SPACE = 163, CONTINUE = 164, ENCLOSE_COMMENT = 165, SECTION_COMMENT = 166, 
    LINE_COMMENT = 167, Equ_op_VE = 168, Integer_VE = 169, Real_VE = 170, 
    Simple_name_VE = 171, SPACE_VE = 172, RETURN_VE = 173, Any_name = 174, 
    SPACE_CM = 175, RETURN_CM = 176, Abs = 177, Attr_properties = 178, Comparison_ops = 179, 
    SPACE_AP = 180
  };

  enum {
    VECTOR_EXPR_MODE = 1, COMMENT_MODE = 2, ATTR_MODE = 3
  };

  explicit CharmmMRLexer(antlr4::CharStream *input);

  ~CharmmMRLexer() override;


  std::string getGrammarFileName() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const std::vector<std::string>& getChannelNames() const override;

  const std::vector<std::string>& getModeNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;

  const antlr4::atn::ATN& getATN() const override;

  // By default the static state used to implement the lexer is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:

  // Individual action functions triggered by action() above.

  // Individual semantic predicate functions triggered by sempred() above.

};

