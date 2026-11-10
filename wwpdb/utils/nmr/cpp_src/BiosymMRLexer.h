
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BiosymMRLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  BiosymMRLexer : public antlr4::Lexer {
public:
  enum {
    Integer = 1, Float = 2, Float_DecimalComma = 3, Real = 4, SHARP_COMMENT = 5, 
    EXCLM_COMMENT = 6, SMCLN_COMMENT = 7, Chiral_code = 8, Atom_selection = 9, 
    Ordinal = 10, Or = 11, Restraint = 12, SPACE = 13, ENCLOSE_COMMENT = 14, 
    SECTION_COMMENT = 15, LINE_COMMENT = 16, Double_quote_string = 17, Create = 18, 
    Function = 19, Target = 20, Distance = 21, Quadratic = 22, Flat_bottomed = 23, 
    Relative = 24, SPACE_II = 25, RETURN_II = 26
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

