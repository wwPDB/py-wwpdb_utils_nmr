
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BiosymMRLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  BiosymMRLexer : public antlr4::Lexer {
public:
  enum {
    Integer = 1, Float = 2, Float_DecimalComma = 3, Real = 4, SHARP_COMMENT = 5, 
    EXCLM_COMMENT = 6, SMCLN_COMMENT = 7, Chiral_code = 8, Atom_selection = 9, 
    Ordinal = 10, Or = 11, Restraint = 12, Mixing_times = 13, SPACE = 14, 
    ENCLOSE_COMMENT = 15, SECTION_COMMENT = 16, LINE_COMMENT = 17, Integer_II = 18, 
    Float_II = 19, Create = 20, Function = 21, Target = 22, Distance = 23, 
    Torsion = 24, Quadratic = 25, Flat_bottomed = 26, Relative = 27, Trans = 28, 
    Simple_name_II = 29, Double_quote_string_II = 30, CONTINUE = 31, SPACE_II = 32, 
    RETURN_II = 33, Real_MT = 34, Float_MT = 35, Integer_MT = 36, And_MR = 37, 
    SPACE_MT = 38, RETURN_MT = 39
  };

  enum {
    INSIGHT_II_MODE = 1, MIXING_TIME_MODE = 2
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

