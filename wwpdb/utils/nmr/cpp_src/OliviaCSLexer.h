
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/OliviaCSLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  OliviaCSLexer : public antlr4::Lexer {
public:
  enum {
    Typedef = 1, Separator = 2, Format = 3, Unformat = 4, Eof = 5, Null_string = 6, 
    Integer = 7, Float = 8, Real = 9, COMMENT = 10, SHARP_COMMENT = 11, 
    EXCLM_COMMENT = 12, Simple_name = 13, SPACE = 14, RETURN = 15, SECTION_COMMENT = 16, 
    LINE_COMMENT = 17, Sequence = 18, Ass_tbl_h2o = 19, Ass_tbl_tro = 20, 
    Ass_tbl_d2o = 21, SPACE_TD = 22, RETURN_TD = 23, Tab = 24, Comma = 25, 
    Space = 26, SPACE_SE = 27, RETURN_SE = 28, Chain = 29, Resname = 30, 
    Seqnum = 31, Atomname = 32, Shift = 33, Stddev = 34, SPACE_FO = 35, 
    RETURN_FO = 36, Printf_string = 37, SPACE_PF = 38, RETURN_PF = 39, Any_name = 40, 
    SPACE_CM = 41, RETURN_CM = 42
  };

  enum {
    TYPEDEF_MODE = 1, SEPARATOR_MODE = 2, FORMAT_MODE = 3, PRINTF_MODE = 4, 
    COMMENT_MODE = 5
  };

  explicit OliviaCSLexer(antlr4::CharStream *input);

  ~OliviaCSLexer() override;


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

