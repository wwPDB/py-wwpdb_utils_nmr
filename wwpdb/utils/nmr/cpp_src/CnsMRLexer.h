
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
    Spectrum = 44, Volume = 45, Vol = 46, Hpm1 = 47, Ppm1 = 48, Ppm2 = 49, 
    Restraints = 50, Dihedral = 51, Nassign = 52, Print_any = 53, Plane = 54, 
    Group = 55, Selection = 56, Weight = 57, Harmonic = 58, Exponent = 59, 
    Normal = 60, Sanisotropy = 61, Coefficients = 62, ForceConstant = 63, 
    Coupling = 64, Carbon = 65, Expectation = 66, PhiStep = 67, PsiStep = 68, 
    Rcoil = 69, Zero = 70, Proton = 71, Observed = 72, Anisotropy = 73, 
    Amides = 74, Nitrogens = 75, Oxygens = 76, RingAtoms = 77, AlphasAndAmides = 78, 
    Error = 79, Conformation = 80, Compressed = 81, Phase = 82, Size = 83, 
    Dimensions = 84, Danisotropy = 85, OneBond = 86, AngleDb = 87, DerivFlag = 88, 
    Ncs = 89, Equivalence = 90, Sigb = 91, Flags = 92, All = 93, Around = 94, 
    Atom = 95, Attribute = 96, BondedTo = 97, ByGroup = 98, ByRes = 99, 
    Chemical = 100, Fbox = 101, Hydrogen = 102, Id = 103, Known = 104, Name = 105, 
    NONE = 106, Point = 107, Cut = 108, Previous = 109, Pseudo = 110, Residue = 111, 
    Resname = 112, Saround = 113, SegIdentifier = 114, Sfbox = 115, Store1 = 116, 
    Store2 = 117, Store3 = 118, Store4 = 119, Store5 = 120, Store6 = 121, 
    Store7 = 122, Store8 = 123, Store9 = 124, Tag = 125, Vector = 126, Do_Lp = 127, 
    Identity_Lp = 128, Show = 129, Evaluate_Lp = 130, Patch = 131, Reference = 132, 
    Nil = 133, Parameter = 134, UB = 135, Mult = 136, HBonded = 137, Improper = 138, 
    NBFix = 139, NonB = 140, VDWOff = 141, Verbose = 142, For = 143, Loop = 144, 
    Tail = 145, Head = 146, Or_op = 147, And_op = 148, Not_op = 149, Comma = 150, 
    Complex = 151, Integer = 152, Logical = 153, Real = 154, Double_quote_string = 155, 
    SHARP_COMMENT = 156, EXCLM_COMMENT = 157, SMCLN_COMMENT = 158, Simple_name = 159, 
    Simple_names = 160, Integers = 161, L_paren = 162, R_paren = 163, Colon = 164, 
    Equ_op = 165, Lt_op = 166, Gt_op = 167, Leq_op = 168, Geq_op = 169, 
    Neq_op = 170, Symbol_name = 171, SPACE = 172, ENCLOSE_COMMENT = 173, 
    SECTION_COMMENT = 174, LINE_COMMENT = 175, SET_VARIABLE = 176, Abs = 177, 
    Attr_properties = 178, Comparison_ops = 179, SPACE_AP = 180, Averaging_methods = 181, 
    Equ_op_CL = 182, Class_name = 183, SPACE_CL = 184, Class_name_AM = 185, 
    SPACE_AM = 186, Equ_op_PT = 187, Potential_types = 188, Class_name_PT = 189, 
    SPACE_PT = 190, Noe_analysis = 191, SPACE_NA = 192, Exclude = 193, Include = 194, 
    End_FL = 195, Class_name_FL = 196, Any_class = 197, SPACE_FL = 198, 
    R_paren_VE = 199, Equ_op_VE = 200, Add_op_VE = 201, Sub_op_VE = 202, 
    Mul_op_VE = 203, Div_op_VE = 204, Exp_op_VE = 205, Comma_VE = 206, Integer_VE = 207, 
    Real_VE = 208, Atom_properties_VE = 209, Abs_VE = 210, Acos_VE = 211, 
    Asin_VE = 212, Cos_VE = 213, Decode_VE = 214, Encode_VE = 215, Exp_VE = 216, 
    Gauss_VE = 217, Heavy_VE = 218, Int_VE = 219, Log10_VE = 220, Log_VE = 221, 
    Max_VE = 222, Maxw_VE = 223, Min_VE = 224, Mod_VE = 225, Norm_VE = 226, 
    Random_VE = 227, Sign_VE = 228, Sin_VE = 229, Sqrt_VE = 230, Tan_VE = 231, 
    Symbol_name_VE = 232, Simple_name_VE = 233, Double_quote_string_VE = 234, 
    SPACE_VE = 235, L_paren_VF = 236, SPACE_VF = 237, L_paren_VS = 238, 
    R_paren_VS = 239, Average_VS = 240, Element_VS = 241, Max_VS = 242, 
    Min_VS = 243, Norm_VS = 244, Rms_VS = 245, Sum_VS = 246, Atom_properties_VS = 247, 
    SPACE_VS = 248, L_paren_CF = 249, R_paren_CF = 250, In_CF = 251, Integer_CF = 252, 
    Real_CF = 253, Symbol_name_CF = 254, Simple_name_CF = 255, Double_quote_string_CF = 256, 
    SPACE_CF = 257, COMMENT_CF = 258, Simple_name_LL = 259, SPACE_LL = 260
  };

  enum {
    ATTR_MODE = 1, AVER_MODE = 2, CLAS_MODE = 3, POTE_MODE = 4, ANAL_MODE = 5, 
    FLAG_MODE = 6, VECTOR_EXPR_MODE = 7, VECTOR_FUNC_MODE = 8, VECTOR_SHOW_MODE = 9, 
    CTL_FOR_MODE = 10, LOOP_LABEL_MODE = 11
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

