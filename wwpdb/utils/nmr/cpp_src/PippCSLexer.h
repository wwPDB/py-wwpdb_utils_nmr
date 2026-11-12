
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/PippCSLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  PippCSLexer : public antlr4::Lexer {
public:
  enum {
    Shift_fl_frmt = 1, Res_siad = 2, First_res_in_seq = 3, Exp_peak_pick_tbl = 4, 
    Res_ID = 5, Res_type = 6, Prev_type = 7, Spin_system_ID = 8, Heterogeneity = 9, 
    End_res_def = 10, Type_pred = 11, Single_note = 12, Note_begin = 13, 
    Integer = 14, Float = 15, SHARP_COMMENT = 16, EXCLM_COMMENT = 17, Simple_name = 18, 
    SPACE = 19, RETURN = 20, SECTION_COMMENT = 21, LINE_COMMENT = 22, Res_ID_ = 23, 
    Label = 24, Exp_par_fl = 25, Peak_pick_fl = 26, Cross_ref = 27, Simple_name_ET = 28, 
    SPACE_ET = 29, RETURN_ET = 30, Note_middle = 31, Note_end = 32, SPACE_MN = 33
  };

  enum {
    EXT_TBL_MODE = 1, MULTIPLE_NOTE_MODE = 2
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

