
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BareMRLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  BareMRLexer : public antlr4::Lexer {
public:
  enum {
    Data_block = 1, Integer = 2, Float = 3, SHARP_COMMENT = 4, EXCLM_COMMENT = 5, 
    Number_of_name = 6, Simple_name = 7, Double_quote_string = 8, Double_quote_integer = 9, 
    Double_quote_float = 10, SPACE = 11, RETURN = 12, SECTION_COMMENT = 13, 
    LINE_COMMENT = 14
  };

  explicit BareMRLexer(antlr4::CharStream *input);

  ~BareMRLexer() override;


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

