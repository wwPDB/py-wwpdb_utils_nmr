
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrViewPKLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  NmrViewPKLexer : public antlr4::Lexer {
public:
  enum {
    Label = 1, Integer = 2, Float = 3, Real = 4, SHARP_COMMENT = 5, EXCLM_COMMENT = 6, 
    SMCLN_COMMENT = 7, Simple_name = 8, SPACE = 9, RETURN = 10, L_brace = 11, 
    SECTION_COMMENT = 12, LINE_COMMENT = 13, Dataset = 14, Sw = 15, Sf = 16, 
    Condition = 17, L_name = 18, P_name = 19, W_name = 20, B_name = 21, 
    E_name = 22, J_name = 23, U_name = 24, Vol = 25, Int = 26, Stat = 27, 
    Comment = 28, Flag0 = 29, Simple_name_LA = 30, Float_LA = 31, SPACE_LA = 32, 
    SINGLE_NL_LA = 33, ENCLOSE_DATA_LA = 34, Any_name = 35, SPACE_CM = 36, 
    R_brace = 37
  };

  enum {
    LABEL_MODE = 1, ENCLOSE_DATA_MODE = 2
  };

  explicit NmrViewPKLexer(antlr4::CharStream *input);

  ~NmrViewPKLexer() override;


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

