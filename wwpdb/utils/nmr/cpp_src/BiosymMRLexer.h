
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BiosymMRLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  BiosymMRLexer : public antlr4::Lexer {
public:
  enum {
    Integer = 1, Float = 2, Float_DecimalComma = 3, Real = 4, SHARP_COMMENT = 5, 
    EXCLM_COMMENT = 6, SMCLN_COMMENT = 7, Chiral_code = 8, Atom_selection = 9, 
    Ordinal = 10, Restraint = 11, SPACE = 12, ENCLOSE_COMMENT = 13, SECTION_COMMENT = 14, 
    LINE_COMMENT = 15, Double_quote_string = 16, Create = 17, Function = 18, 
    Target = 19, Distance = 20, Quadratic = 21, Flat_bottomed = 22, Relative = 23, 
    SPACE_II = 24, RETURN_II = 25
  };

  enum {
    INSIGHT_II_MODE = 1
  };

  explicit BiosymMRLexer(antlr4::CharStream *input);

  ~BiosymMRLexer() override;


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

