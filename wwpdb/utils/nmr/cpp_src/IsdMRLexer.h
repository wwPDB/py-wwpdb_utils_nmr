
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/IsdMRLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  IsdMRLexer : public antlr4::Lexer {
public:
  enum {
    Distance = 1, Integer = 2, Float = 3, SHARP_COMMENT = 4, EXCLM_COMMENT = 5, 
    SMCLN_COMMENT = 6, Atom_selection = 7, SPACE = 8, ENCLOSE_COMMENT = 9, 
    SECTION_COMMENT = 10, LINE_COMMENT = 11
  };

  explicit IsdMRLexer(antlr4::CharStream *input);

  ~IsdMRLexer() override;


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

