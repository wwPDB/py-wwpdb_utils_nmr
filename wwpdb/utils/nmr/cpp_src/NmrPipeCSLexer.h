
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrPipeCSLexer.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  NmrPipeCSLexer : public antlr4::Lexer {
public:
  enum {
    Data = 1, Vars = 2, Format = 3, Integer = 4, Float = 5, Float_DecimalComma = 6, 
    SHARP_COMMENT = 7, EXCLM_COMMENT = 8, SMCLN_COMMENT = 9, Simple_name = 10, 
    SPACE = 11, ENCLOSE_COMMENT = 12, SECTION_COMMENT = 13, LINE_COMMENT = 14, 
    First_resid = 15, Sequence = 16, Db_name = 17, Tab_name = 18, Tab_id = 19, 
    Integer_DA = 20, Simple_name_DA = 21, SPACE_DA = 22, RETURN_DA = 23, 
    LINE_COMMENT_DA = 24, One_letter_code = 25, SPACE_SQ = 26, RETURN_SQ = 27, 
    LINE_COMMENT_SQ = 28, Segname = 29, Resid = 30, Resname = 31, Atomname = 32, 
    Shift = 33, SPACE_VA = 34, RETURN_VA = 35, LINE_COMMENT_VA = 36, Format_code = 37, 
    SPACE_FO = 38, RETURN_FO = 39, LINE_COMMENT_FO = 40
  };

  enum {
    DATA_MODE = 1, SEQ_MODE = 2, VARS_MODE = 3, FORMAT_MODE = 4
  };

  explicit NmrPipeCSLexer(antlr4::CharStream *input);

  ~NmrPipeCSLexer() override;


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

