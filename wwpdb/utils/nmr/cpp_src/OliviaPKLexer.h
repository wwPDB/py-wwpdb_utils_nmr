
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/OliviaPKLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  OliviaPKLexer : public antlr4::Lexer {
public:
  enum {
    Typedef = 1, Separator = 2, Format = 3, Unformat = 4, Eof = 5, Null_string = 6, 
    Integer = 7, Float = 8, Real = 9, COMMENT = 10, SHARP_COMMENT = 11, 
    EXCLM_COMMENT = 12, Double_quote_string = 13, Single_quote_string = 14, 
    Simple_name = 15, SPACE = 16, RETURN = 17, SECTION_COMMENT = 18, LINE_COMMENT = 19, 
    Idx_tbl_2d = 20, Idx_tbl_3d = 21, Idx_tbl_4d = 22, Ass_tbl_2d = 23, 
    Ass_tbl_3d = 24, Ass_tbl_4d = 25, SPACE_TD = 26, RETURN_TD = 27, Tab = 28, 
    Comma = 29, Space = 30, SPACE_SE = 31, RETURN_SE = 32, Index = 33, X_ppm = 34, 
    Y_ppm = 35, Z_ppm = 36, A_ppm = 37, X_hz = 38, Y_hz = 39, Z_hz = 40, 
    A_hz = 41, Amplitude = 42, Volume = 43, Vol_err = 44, X_chain = 45, 
    Y_chain = 46, Z_chain = 47, A_chain = 48, X_resname = 49, Y_resname = 50, 
    Z_resname = 51, A_resname = 52, X_seqnum = 53, Y_seqnum = 54, Z_seqnum = 55, 
    A_seqnum = 56, X_assign = 57, Y_assign = 58, Z_assign = 59, A_assign = 60, 
    Eval = 61, Status = 62, User_memo = 63, Update_time = 64, SPACE_FO = 65, 
    RETURN_FO = 66, Printf_string = 67, SPACE_PF = 68, RETURN_PF = 69, Any_name = 70, 
    SPACE_CM = 71, RETURN_CM = 72
  };

  enum {
    TYPEDEF_MODE = 1, SEPARATOR_MODE = 2, FORMAT_MODE = 3, PRINTF_MODE = 4, 
    COMMENT_MODE = 5
  };

  explicit OliviaPKLexer(antlr4::CharStream *input);

  ~OliviaPKLexer() override;


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

