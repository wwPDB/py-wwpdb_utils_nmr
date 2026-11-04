
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CyanaMRLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  CyanaMRLexer : public antlr4::Lexer {
public:
  enum {
    Ambig_code = 1, Integer = 2, Float = 3, Float_DecimalComma = 4, Orientation_header = 5, 
    Tensor_header = 6, SMCLN_COMMENT = 7, COMMENT = 8, NoeUpp = 9, NoeLow = 10, 
    NoeUpLo = 11, HBUpp = 12, HBLow = 13, SSUpp = 14, SSLow = 15, Jcoupl = 16, 
    Angle = 17, Stereo = 18, Shifts = 19, Type = 20, Equ_op = 21, Or = 22, 
    Ssbond = 23, Ssbond_resids = 24, Hbond = 25, Link = 26, Atom_stereo = 27, 
    Var = 28, Unset = 29, SetVar = 30, Print = 31, Residue = 32, Mapping = 33, 
    Ambig = 34, Capital_integer = 35, Integer_capital = 36, Simple_name = 37, 
    SPACE = 38, ENCLOSE_COMMENT = 39, SECTION_COMMENT = 40, LINE_COMMENT = 41, 
    Any_name = 42, SPACE_CM = 43, RETURN_CM = 44, Atom1 = 45, Atom2 = 46, 
    Residue1 = 47, Residue2 = 48, Equ_op_HB = 49, Atom1_equ = 50, Atom2_equ = 51, 
    Residue1_equ = 52, Residue2_equ = 53, Concat_atom_1 = 54, Concat_atom_2 = 55, 
    Concat_res_1 = 56, Concat_res_2 = 57, Integer_HB = 58, Simple_name_HB = 59, 
    SPACE_HB = 60, RETURN_HB = 61, LINE_COMMENT_HB = 62, Double_quote_string = 63, 
    SPACE_PR = 64, RETURN_PR = 65, LINE_COMMENT_PR = 66, Simple_name_VA = 67, 
    SPACE_VA = 68, RETURN_VA = 69, LINE_COMMENT_VA = 70, Ambig_code_MP = 71, 
    Integer_MP = 72, Simple_name_MP = 73, Equ_op_MP = 74, SPACE_MP = 75, 
    RETURN_MP = 76, LINE_COMMENT_MP = 77
  };

  enum {
    COMMENT_MODE = 1, HBOND_MODE = 2, PRINT_MODE = 3, VARIABLE_MODE = 4, 
    MAP_MODE = 5
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

