
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrViewCSLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  NmrViewCSLexer : public antlr4::Lexer {
public:
  enum {
    Integer = 1, Float = 2, SHARP_COMMENT = 3, EXCLM_COMMENT = 4, Res_ID = 5, 
    Res_Type = 6, Prev_Type = 7, Spin_System_ID = 8, Heterogeneity = 9, 
    End_Res_Def = 10, Type_pred = 11, Single_note = 12, Note_begin = 13, 
    Simple_name = 14, SPACE = 15, RETURN = 16, SECTION_COMMENT = 17, LINE_COMMENT = 18, 
    Note_middle = 19, Note_end = 20, SPACE_MN = 21
  };

  enum {
    MULTIPLE_NOTE_MODE = 1
  };

  explicit NmrViewCSLexer(antlr4::CharStream *input);

  ~NmrViewCSLexer() override;


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

