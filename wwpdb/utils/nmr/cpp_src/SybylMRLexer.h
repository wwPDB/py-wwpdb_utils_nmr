
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/SybylMRLexer.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  SybylMRLexer : public antlr4::Lexer {
public:
  enum {
    Atom1 = 1, Atom2 = 2, Lower = 3, Upper = 4, Integer = 5, Float = 6, 
    Float_DecimalComma = 7, SHARP_COMMENT = 8, EXCLM_COMMENT = 9, SMCLN_COMMENT = 10, 
    Atom_selection = 11, SPACE = 12, ENCLOSE_COMMENT = 13, SECTION_COMMENT = 14, 
    LINE_COMMENT = 15
  };

  explicit SybylMRLexer(antlr4::CharStream *input);

  ~SybylMRLexer() override;


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

