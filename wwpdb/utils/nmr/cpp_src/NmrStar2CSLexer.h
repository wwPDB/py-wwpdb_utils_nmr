
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrStar2CSLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  NmrStar2CSLexer : public antlr4::Lexer {
public:
  enum {
    Data_block = 1, Saveframe_block = 2, Saveframe_category = 3, Save = 4, 
    Loop = 5, Stop = 6, Residue_seq_code = 7, Residue_label = 8, Atom_shift_assign_ID = 9, 
    Residue_author_seq_code = 10, Atom_name = 11, Atom_type = 12, Chem_shift_value = 13, 
    Chem_shift_value_error = 14, Chem_shift_ambiguity_code = 15, Integer = 16, 
    Float = 17, SHARP_COMMENT = 18, EXCLM_COMMENT = 19, SMCLN_COMMENT = 20, 
    Simple_name = 21, Double_quote_string = 22, Single_quote_string = 23, 
    SPACE = 24, RETURN = 25, SECTION_COMMENT = 26, LINE_COMMENT = 27
  };

  explicit NmrStar2CSLexer(antlr4::CharStream *input);

  ~NmrStar2CSLexer() override;


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

