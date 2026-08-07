
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CcpnPKLexer.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  CcpnPKLexer : public antlr4::Lexer {
public:
  enum {
    Num = 1, Id = 2, Assign_F1 = 3, Position_F1 = 4, Shift_F1 = 5, Integer = 6, 
    Float = 7, Real = 8, EXCLM_COMMENT = 9, SMCLN_COMMENT = 10, Simple_name = 11, 
    Any_name = 12, SPACE = 13, RETURN = 14, SECTION_COMMENT = 15, LINE_COMMENT = 16, 
    Id_ = 17, Position_F1_ = 18, Position_F2 = 19, Position_F3 = 20, Position_F4 = 21, 
    Shift_F1_ = 22, Shift_F2 = 23, Shift_F3 = 24, Shift_F4 = 25, Assign_F1_ = 26, 
    Assign_F2 = 27, Assign_F3 = 28, Assign_F4 = 29, Height = 30, Volume = 31, 
    Line_width_F1 = 32, Line_width_F2 = 33, Line_width_F3 = 34, Line_width_F4 = 35, 
    Merit = 36, Details = 37, Fit_method = 38, Vol_method = 39, SPACE_VARS = 40, 
    RETURN_VARS = 41
  };

  enum {
    VARS_MODE = 1
  };

  explicit CcpnPKLexer(antlr4::CharStream *input);

  ~CcpnPKLexer() override;


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

