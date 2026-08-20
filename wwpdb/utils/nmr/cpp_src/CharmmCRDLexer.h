
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CharmmCRDLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  CharmmCRDLexer : public antlr4::Lexer {
public:
  enum {
    Integer = 1, Float = 2, Double_quote_string = 3, COMMENT = 4, Ext = 5, 
    Simple_name = 6, SPACE = 7, CONTINUE = 8, ENCLOSE_COMMENT = 9, SECTION_COMMENT = 10, 
    LINE_COMMENT = 11, Any_name = 12, SPACE_CM = 13, RETURN_CM = 14
  };

  enum {
    COMMENT_MODE = 1
  };

  explicit CharmmCRDLexer(antlr4::CharStream *input);

  ~CharmmCRDLexer() override;


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

