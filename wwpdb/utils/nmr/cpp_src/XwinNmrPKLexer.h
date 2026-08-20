
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/XwinNmrPKLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  XwinNmrPKLexer : public antlr4::Lexer {
public:
  enum {
    Num_of_dim = 1, Integer = 2, Float = 3, COMMENT = 4, SPACE = 5, RETURN = 6, 
    SECTION_COMMENT = 7, LINE_COMMENT = 8, Annotation = 9, Integer_ND = 10, 
    SPACE_ND = 11, RETURN_ND = 12, Any_name = 13, SPACE_CM = 14, RETURN_CM = 15
  };

  enum {
    NUM_OF_DIM_MODE = 1, COMMENT_MODE = 2
  };

  explicit XwinNmrPKLexer(antlr4::CharStream *input);

  ~XwinNmrPKLexer() override;


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

