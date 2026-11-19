
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CyanaMRLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  CyanaMRLexer : public antlr4::Lexer {
public:
  enum {
    Ambig_code = 1, Integer = 2, Float = 3, Float_DecimalComma = 4, Orientation_header = 5, 
    Tensor_header = 6, SMCLN_COMMENT = 7, COMMENT = 8, NoeUpp = 9, NoeLow = 10, 
    NoeUpLo = 11, HBUpp = 12, HBLow = 13, HBUpLo = 14, SSUpp = 15, SSLow = 16, 
    SSUpLo = 17, Jcoupl = 18, Angle = 19, Stereo = 20, Type = 21, Equ_op = 22, 
    Or = 23, Ssbond = 24, Ssbond_resids = 25, Hbond = 26, Link = 27, Atom_stereo = 28, 
    Var = 29, Unset = 30, SetVar = 31, Print = 32, Residue = 33, Mapping = 34, 
    Ambig = 35, Capital_integer = 36, Integer_capital = 37, Simple_name = 38, 
    SPACE = 39, ENCLOSE_COMMENT = 40, SECTION_COMMENT = 41, LINE_COMMENT = 42, 
    Any_name = 43, SPACE_CM = 44, RETURN_CM = 45, Atom1 = 46, Atom2 = 47, 
    Residue1 = 48, Residue2 = 49, Equ_op_HB = 50, Atom1_equ = 51, Atom2_equ = 52, 
    Residue1_equ = 53, Residue2_equ = 54, Concat_atom_1 = 55, Concat_atom_2 = 56, 
    Concat_res_1 = 57, Concat_res_2 = 58, Integer_HB = 59, Simple_name_HB = 60, 
    SPACE_HB = 61, RETURN_HB = 62, LINE_COMMENT_HB = 63, Double_quote_string = 64, 
    Integer_PR = 65, Simple_name_PR = 66, SPACE_PR = 67, RETURN_PR = 68, 
    LINE_COMMENT_PR = 69, Simple_name_VA = 70, SPACE_VA = 71, RETURN_VA = 72, 
    LINE_COMMENT_VA = 73, Ambig_code_MP = 74, Integer_MP = 75, Simple_name_MP = 76, 
    Equ_op_MP = 77, SPACE_MP = 78, RETURN_MP = 79, LINE_COMMENT_MP = 80, 
    Integer_QC = 81, Float_QC = 82, Float_DecimalComma_QC = 83, Simple_name_QC = 84, 
    Capital_integer_QC = 85, Integer_capital_QC = 86, SPACE_QC = 87, RETURN_QC = 88
  };

  enum {
    COMMENT_MODE = 1, HBOND_MODE = 2, PRINT_MODE = 3, VARIABLE_MODE = 4, 
    MAP_MODE = 5, QCONVR_MODE = 6
  };

  explicit CyanaMRLexer(antlr4::CharStream *input);

  ~CyanaMRLexer() override;


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

