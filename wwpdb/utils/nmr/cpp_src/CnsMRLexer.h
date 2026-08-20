
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CnsMRLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  CnsMRLexer : public antlr4::Lexer {
public:
  enum {
    Set = 1, End = 2, Noe = 3, Analysis = 4, Assign = 5, Asymptote = 6, 
    Average = 7, Bhig = 8, Ceiling = 9, Classification = 10, CountViol = 11, 
    Cv = 12, Den = 13, Distribute = 14, Ensemble = 15, Monomers = 16, Ncount = 17, 
    Nrestraints = 18, Outd = 19, Partition = 20, Potential = 21, Predict = 22, 
    Print = 23, Raverage = 24, Threshold = 25, Reset = 26, Rswitch = 27, 
    Scale = 28, SoExponent = 29, SqConstant = 30, SqExponent = 31, SqOffset = 32, 
    Taverage = 33, Temperature = 34, Initialize = 35, Update = 36, Gamma = 37, 
    Kappa = 38, Cutoff = 39, Cuton = 40, From = 41, To = 42, Peak = 43, 
    Spectrum = 44, Volume = 45, Vol = 46, Ppm1 = 47, Ppm2 = 48, Restraints = 49, 
    Dihedral = 50, Nassign = 51, Print_any = 52, Plane = 53, Group = 54, 
    Selection = 55, Weight = 56, Harmonic = 57, Exponent = 58, Normal = 59, 
    Sanisotropy = 60, Coefficients = 61, ForceConstant = 62, Coupling = 63, 
    Carbon = 64, Expectation = 65, PhiStep = 66, PsiStep = 67, Rcoil = 68, 
    Zero = 69, Proton = 70, Observed = 71, Anisotropy = 72, Amides = 73, 
    Nitrogens = 74, Oxygens = 75, RingAtoms = 76, AlphasAndAmides = 77, 
    Error = 78, Conformation = 79, Compressed = 80, Phase = 81, Size = 82, 
    Dimensions = 83, Danisotropy = 84, OneBond = 85, AngleDb = 86, DerivFlag = 87, 
    Ncs = 88, Equivalence = 89, Sigb = 90, Flags = 91, All = 92, Around = 93, 
    Atom = 94, Attribute = 95, BondedTo = 96, ByGroup = 97, ByRes = 98, 
    Chemical = 99, Fbox = 100, Hydrogen = 101, Id = 102, Known = 103, Name = 104, 
    NONE = 105, Point = 106, Cut = 107, Previous = 108, Pseudo = 109, Residue = 110, 
    Resname = 111, Saround = 112, SegIdentifier = 113, Sfbox = 114, Store1 = 115, 
    Store2 = 116, Store3 = 117, Store4 = 118, Store5 = 119, Store6 = 120, 
    Store7 = 121, Store8 = 122, Store9 = 123, Tag = 124, Vector = 125, Do_Lp = 126, 
    Identity_Lp = 127, Show = 128, Evaluate_Lp = 129, Patch = 130, Reference = 131, 
    Nil = 132, Parameter = 133, UB = 134, Mult = 135, HBonded = 136, Improper = 137, 
    NBFix = 138, NonB = 139, VDWOff = 140, Verbose = 141, For = 142, Loop = 143, 
    Tail = 144, Head = 145, Or_op = 146, And_op = 147, Not_op = 148, Comma = 149, 
    Complex = 150, Integer = 151, Logical = 152, Real = 153, Double_quote_string = 154, 
    SHARP_COMMENT = 155, EXCLM_COMMENT = 156, SMCLN_COMMENT = 157, Simple_name = 158, 
    Simple_names = 159, Integers = 160, L_paren = 161, R_paren = 162, Colon = 163, 
    Equ_op = 164, Lt_op = 165, Gt_op = 166, Leq_op = 167, Geq_op = 168, 
    Neq_op = 169, Symbol_name = 170, SPACE = 171, ENCLOSE_COMMENT = 172, 
    SECTION_COMMENT = 173, LINE_COMMENT = 174, SET_VARIABLE = 175, Abs = 176, 
    Attr_properties = 177, Comparison_ops = 178, SPACE_AP = 179, Averaging_methods = 180, 
    Class_name_AM = 181, SPACE_AM = 182, Equ_op_PT = 183, Potential_types = 184, 
    Class_name_PT = 185, SPACE_PT = 186, Noe_analysis = 187, SPACE_NA = 188, 
    Exclude = 189, Include = 190, End_FL = 191, Class_name = 192, Any_class = 193, 
    SPACE_FL = 194, R_paren_VE = 195, Equ_op_VE = 196, Add_op_VE = 197, 
    Sub_op_VE = 198, Mul_op_VE = 199, Div_op_VE = 200, Exp_op_VE = 201, 
    Comma_VE = 202, Integer_VE = 203, Real_VE = 204, Atom_properties_VE = 205, 
    Abs_VE = 206, Acos_VE = 207, Asin_VE = 208, Cos_VE = 209, Decode_VE = 210, 
    Encode_VE = 211, Exp_VE = 212, Gauss_VE = 213, Heavy_VE = 214, Int_VE = 215, 
    Log10_VE = 216, Log_VE = 217, Max_VE = 218, Maxw_VE = 219, Min_VE = 220, 
    Mod_VE = 221, Norm_VE = 222, Random_VE = 223, Sign_VE = 224, Sin_VE = 225, 
    Sqrt_VE = 226, Tan_VE = 227, Symbol_name_VE = 228, Simple_name_VE = 229, 
    Double_quote_string_VE = 230, SPACE_VE = 231, L_paren_VF = 232, SPACE_VF = 233, 
    L_paren_VS = 234, R_paren_VS = 235, Average_VS = 236, Element_VS = 237, 
    Max_VS = 238, Min_VS = 239, Norm_VS = 240, Rms_VS = 241, Sum_VS = 242, 
    Atom_properties_VS = 243, SPACE_VS = 244, L_paren_CF = 245, R_paren_CF = 246, 
    In_CF = 247, Integer_CF = 248, Real_CF = 249, Symbol_name_CF = 250, 
    Simple_name_CF = 251, SPACE_CF = 252, COMMENT_CF = 253, Simple_name_LL = 254, 
    SPACE_LL = 255
  };

  enum {
    ATTR_MODE = 1, AVER_MODE = 2, POTE_MODE = 3, ANAL_MODE = 4, FLAG_MODE = 5, 
    VECTOR_EXPR_MODE = 6, VECTOR_FUNC_MODE = 7, VECTOR_SHOW_MODE = 8, CTL_FOR_MODE = 9, 
    LOOP_LABEL_MODE = 10
  };

  explicit CnsMRLexer(antlr4::CharStream *input);

  ~CnsMRLexer() override;


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

