
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/DianaCSLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  DianaCSLexer : public antlr4::Lexer {
public:
  enum {
    Integer = 1, Float = 2, SMCLN_COMMENT = 3, COMMENT = 4, Shifts = 5, 
    Simple_name = 6, SPACE = 7, ENCLOSE_COMMENT = 8, SECTION_COMMENT = 9, 
    LINE_COMMENT = 10, Any_name = 11, SPACE_CM = 12, RETURN_CM = 13
  };

  enum {
    COMMENT_MODE = 1
  };

  explicit DianaCSLexer(antlr4::CharStream *input);

  ~DianaCSLexer() override;


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

