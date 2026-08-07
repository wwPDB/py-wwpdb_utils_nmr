
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/PippCSLexer.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  PippCSLexer : public antlr4::Lexer {
public:
  enum {
    Shift_fl_frmt = 1, Res_siad = 2, First_res_in_seq = 3, Exp_peak_pick_tbl = 4, 
    Res_ID = 5, Res_type = 6, Spin_system_ID = 7, Heterogeneity = 8, End_res_def = 9, 
    L_paren = 10, R_paren = 11, Integer = 12, Float = 13, SHARP_COMMENT = 14, 
    EXCLM_COMMENT = 15, Simple_name = 16, SPACE = 17, RETURN = 18, SECTION_COMMENT = 19, 
    LINE_COMMENT = 20, Res_ID_ = 21, Label = 22, Exp_par_fl = 23, Peak_pick_fl = 24, 
    Cross_ref = 25, Simple_name_ET = 26, SPACE_ET = 27, RETURN_ET = 28
  };

  enum {
    EXT_TBL_MODE = 1
  };

  explicit PippCSLexer(antlr4::CharStream *input);

  ~PippCSLexer() override;


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

