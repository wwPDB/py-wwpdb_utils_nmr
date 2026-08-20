
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/PpmCSLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  PpmCSLexer : public antlr4::Lexer {
public:
  enum {
    Integer = 1, Float = 2, SHARP_COMMENT = 3, EXCLM_COMMENT = 4, Atom_selection_2d_ex = 5, 
    Atom_selection_3d_ex = 6, Simple_name = 7, SPACE = 8, RETURN = 9, SECTION_COMMENT = 10, 
    LINE_COMMENT = 11
  };

  explicit PpmCSLexer(antlr4::CharStream *input);

  ~PpmCSLexer() override;


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

