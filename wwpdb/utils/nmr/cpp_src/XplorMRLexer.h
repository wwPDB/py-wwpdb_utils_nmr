
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/XplorMRLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  XplorMRLexer : public antlr4::Lexer {
public:
  enum {
    Set = 1, End = 2, Noe = 3, Assign = 4, Asymptote = 5, Average = 6, Bhig = 7, 
    Ceiling = 8, Classification = 9, CountViol = 10, Distribute = 11, Monomers = 12, 
    Ncount = 13, Nrestraints = 14, Potential = 15, Predict = 16, Print = 17, 
    Threshold = 18, Reset = 19, Rswitch = 20, Scale = 21, SoExponent = 22, 
    SqConstant = 23, SqExponent = 24, SqOffset = 25, Temperature = 26, Cutoff = 27, 
    Cuton = 28, From = 29, To = 30, Peak = 31, Spectrum = 32, Volume = 33, 
    Vol = 34, Hpm1 = 35, Ppm1 = 36, Ppm2 = 37, Restraints = 38, Dihedral = 39, 
    Nassign = 40, Print_any = 41, Sanisotropy = 42, Coefficients = 43, ForceConstant = 44, 
    Xdipolar = 45, Dipolar = 46, Type = 47, Sign = 48, VeAngle = 49, Cv = 50, 
    Partition = 51, Tensor = 52, Anisotropy = 53, Planar = 54, Group = 55, 
    Initialize = 56, Selection = 57, Weight = 58, Harmonic = 59, Exponent = 60, 
    Normal = 61, Xadc = 62, Expectation = 63, Size = 64, Zero = 65, Coupling = 66, 
    Degeneracy = 67, Carbon = 68, PhiStep = 69, PsiStep = 70, Rcoil = 71, 
    Proton = 72, Observed = 73, Amides = 74, Nitrogens = 75, Oxygens = 76, 
    RingAtoms = 77, AlphasAndAmides = 78, Error = 79, Ramachandran = 80, 
    Gaussian = 81, Phase = 82, Quartic = 83, Shape = 84, Sort = 85, Dimensions = 86, 
    Collapse = 87, Danisotropy = 88, Orient = 89, Height = 90, MaxGaussians = 91, 
    NewGaussian = 92, Dcsa = 93, Sigma = 94, Pcsa = 95, OneBond = 96, AngleDb = 97, 
    DerivFlag = 98, PMagnetic = 99, Kconst = 100, Omega = 101, Tauc = 102, 
    Debug = 103, Xpcs = 104, Tolerance = 105, Save = 106, Fmed = 107, ErrOn = 108, 
    ErrOff = 109, Fon = 110, Foff = 111, Son = 112, Soff = 113, Frun = 114, 
    Xrdcoupling = 115, Xangle = 116, Xccr = 117, Weip = 118, Hbda = 119, 
    Hbdb = 120, Kdir = 121, Klin = 122, Nseg = 123, Nmin = 124, Nmax = 125, 
    Segm = 126, Ohcut = 127, Coh1cut = 128, Coh2cut = 129, Ohncut = 130, 
    Updfrq = 131, Prnfrq = 132, Freemode = 133, Donor = 134, Acceptor = 135, 
    Ncs = 136, Equivalence = 137, Sigb = 138, Flags = 139, All = 140, Around = 141, 
    Atom = 142, Attribute = 143, BondedTo = 144, ByGroup = 145, ByRes = 146, 
    Chemical = 147, Hydrogen = 148, Id = 149, Known = 150, Name = 151, Point = 152, 
    Cut = 153, Previous = 154, Pseudo = 155, Residue = 156, Resname = 157, 
    Saround = 158, SegIdentifier = 159, Store1 = 160, Store2 = 161, Store3 = 162, 
    Store4 = 163, Store5 = 164, Store6 = 165, Store7 = 166, Store8 = 167, 
    Store9 = 168, Tag = 169, Vector = 170, Do_Lp = 171, Identity_Lp = 172, 
    Show = 173, Evaluate_Lp = 174, Patch = 175, Reference = 176, Nil = 177, 
    Parameter = 178, UB = 179, Mult = 180, HBonded = 181, Improper = 182, 
    NBFix = 183, NonB = 184, VDWOff = 185, Verbose = 186, For = 187, Loop = 188, 
    Tail = 189, Head = 190, Or_op = 191, And_op = 192, Not_op = 193, Comma = 194, 
    Complex = 195, Integer = 196, Logical = 197, Real = 198, Double_quote_string = 199, 
    SHARP_COMMENT = 200, EXCLM_COMMENT = 201, SMCLN_COMMENT = 202, Simple_name = 203, 
    Simple_names = 204, Integers = 205, L_paren = 206, R_paren = 207, Colon = 208, 
    Equ_op = 209, Lt_op = 210, Gt_op = 211, Leq_op = 212, Geq_op = 213, 
    Neq_op = 214, Symbol_name = 215, SPACE = 216, ENCLOSE_COMMENT = 217, 
    SECTION_COMMENT = 218, LINE_COMMENT = 219, SET_VARIABLE = 220, Abs = 221, 
    Attr_properties = 222, Comparison_ops = 223, SPACE_AP = 224, Equ_op_CL = 225, 
    Class_name = 226, SPACE_CL = 227, Averaging_methods = 228, Class_name_AM = 229, 
    SPACE_AM = 230, Equ_op_PT = 231, Potential_types = 232, Class_name_PT = 233, 
    SPACE_PT = 234, Rdc_dist_fix_types = 235, Rdc_or_Diff_anis_types = 236, 
    Csa_types = 237, SPACE_TY = 238, Gauss_or_Quart = 239, SPACE_SH = 240, 
    Exclude = 241, Include = 242, End_FL = 243, Class_name_FL = 244, Any_class = 245, 
    SPACE_FL = 246, R_paren_VE = 247, Equ_op_VE = 248, Add_op_VE = 249, 
    Sub_op_VE = 250, Mul_op_VE = 251, Div_op_VE = 252, Exp_op_VE = 253, 
    Comma_VE = 254, Integer_VE = 255, Real_VE = 256, Atom_properties_VE = 257, 
    Abs_VE = 258, Acos_VE = 259, Asin_VE = 260, Cos_VE = 261, Decode_VE = 262, 
    Encode_VE = 263, Exp_VE = 264, Gauss_VE = 265, Heavy_VE = 266, Int_VE = 267, 
    Log10_VE = 268, Log_VE = 269, Max_VE = 270, Maxw_VE = 271, Min_VE = 272, 
    Mod_VE = 273, Norm_VE = 274, Random_VE = 275, Sign_VE = 276, Sin_VE = 277, 
    Sqrt_VE = 278, Tan_VE = 279, Symbol_name_VE = 280, Simple_name_VE = 281, 
    Double_quote_string_VE = 282, SPACE_VE = 283, L_paren_VF = 284, SPACE_VF = 285, 
    L_paren_VS = 286, R_paren_VS = 287, Average_VS = 288, Element_VS = 289, 
    Max_VS = 290, Min_VS = 291, Norm_VS = 292, Rms_VS = 293, Sum_VS = 294, 
    Atom_properties_VS = 295, SPACE_VS = 296, L_paren_CF = 297, R_paren_CF = 298, 
    In_CF = 299, Integer_CF = 300, Real_CF = 301, Symbol_name_CF = 302, 
    Simple_name_CF = 303, SPACE_CF = 304, COMMENT_CF = 305, Simple_name_LL = 306, 
    SPACE_LL = 307
  };

  enum {
    ATTR_MODE = 1, CLAS_MODE = 2, AVER_MODE = 3, POTE_MODE = 4, TYPE_MODE = 5, 
    SHAP_MODE = 6, FLAG_MODE = 7, VECTOR_EXPR_MODE = 8, VECTOR_FUNC_MODE = 9, 
    VECTOR_SHOW_MODE = 10, CTL_FOR_MODE = 11, LOOP_LABEL_MODE = 12
  };

  explicit XplorMRLexer(antlr4::CharStream *input);

  ~XplorMRLexer() override;


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

