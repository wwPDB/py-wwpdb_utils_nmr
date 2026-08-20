
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CyanaMRLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  CyanaMRLexer : public antlr4::Lexer {
public:
  enum {
    Ambig_code = 1, Integer = 2, Float = 3, Float_DecimalComma = 4, Orientation_header = 5, 
    Tensor_header = 6, SMCLN_COMMENT = 7, COMMENT = 8, NoeUpp = 9, NoeLow = 10, 
    Type = 11, Equ_op = 12, Or = 13, Ssbond = 14, Ssbond_resids = 15, Hbond = 16, 
    Link = 17, Atom_stereo = 18, Var = 19, Unset = 20, SetVar = 21, Print = 22, 
    Residue = 23, Mapping = 24, Ambig = 25, Capital_integer = 26, Integer_capital = 27, 
    Simple_name = 28, SPACE = 29, ENCLOSE_COMMENT = 30, SECTION_COMMENT = 31, 
    LINE_COMMENT = 32, Any_name = 33, SPACE_CM = 34, RETURN_CM = 35, Atom1 = 36, 
    Atom2 = 37, Residue1 = 38, Residue2 = 39, Equ_op_HB = 40, Integer_HB = 41, 
    Simple_name_HB = 42, SPACE_HB = 43, RETURN_HB = 44, LINE_COMMENT_HB = 45, 
    Double_quote_string = 46, SPACE_PR = 47, RETURN_PR = 48, LINE_COMMENT_PR = 49, 
    Simple_name_VA = 50, SPACE_VA = 51, RETURN_VA = 52, LINE_COMMENT_VA = 53, 
    Ambig_code_MP = 54, Integer_MP = 55, Simple_name_MP = 56, Equ_op_MP = 57, 
    SPACE_MP = 58, RETURN_MP = 59, LINE_COMMENT_MP = 60
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

