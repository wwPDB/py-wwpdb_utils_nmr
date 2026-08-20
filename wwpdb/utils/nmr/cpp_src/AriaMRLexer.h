
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/AriaMRLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  AriaMRLexer : public antlr4::Lexer {
public:
  enum {
    COMMA = 1, Integer = 2, Float = 3, Real = 4, SHARP_COMMENT = 5, EXCLM_COMMENT = 6, 
    SMCLN_COMMENT = 7, RefSpec = 8, RefPeak = 9, Id = 10, D = 11, U = 12, 
    UViol = 13, PViol = 14, Viol = 15, Reliable = 16, AType = 17, Weight = 18, 
    PlusMinus = 19, Hyphen = 20, P_code = 21, A_code = 22, C_code = 23, 
    Simple_name = 24, SPACE = 25, ENCLOSE_COMMENT = 26, SECTION_COMMENT = 27, 
    LINE_COMMENT = 28, SPACE_RS = 29, RefSpecName = 30, RETURN_RS = 31, 
    SPACE_V = 32, ViolFlag = 33, RETURN_V = 34, SPACE_R = 35, ReliableFlag = 36, 
    RETURN_R = 37, SPACE_A = 38, ATypeFlag = 39, RETURN_A = 40
  };

  enum {
    REF_SPEC_MODE = 1, VIOL_MODE = 2, RELIABLE_MODE = 3, ATYPE_MODE = 4
  };

  explicit AriaMRLexer(antlr4::CharStream *input);

  ~AriaMRLexer() override;


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

