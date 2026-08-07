
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/PonderosaPKLexer.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  PonderosaPKLexer : public antlr4::Lexer {
public:
  enum {
    Noesy_type = 1, Axis_order = 2, Integer = 3, Float = 4, Real = 5, SHARP_COMMENT = 6, 
    EXCLM_COMMENT = 7, SMCLN_COMMENT = 8, Simple_name = 9, SPACE = 10, RETURN = 11, 
    SECTION_COMMENT = 12, LINE_COMMENT = 13, Integer_NT = 14, Simple_name_NT = 15, 
    SPACE_NT = 16, RETURN_NT = 17, Integer_AO = 18, Simple_name_AO = 19, 
    SPACE_AO = 20, RETURN_AO = 21
  };

  enum {
    NT_MODE = 1, AO_MODE = 2
  };

  explicit PonderosaPKLexer(antlr4::CharStream *input);

  ~PonderosaPKLexer() override;


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

