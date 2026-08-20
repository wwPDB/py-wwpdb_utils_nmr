
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrStar2CSLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  NmrStar2CSLexer : public antlr4::Lexer {
public:
  enum {
    Loop = 1, Stop = 2, Residue_seq_code = 3, Residue_label = 4, Atom_shift_assign_ID = 5, 
    Residue_author_seq_code = 6, Atom_name = 7, Atom_type = 8, Chem_shift_value = 9, 
    Chem_shift_value_error = 10, Chem_shift_ambiguity_code = 11, Integer = 12, 
    Float = 13, SHARP_COMMENT = 14, EXCLM_COMMENT = 15, SMCLN_COMMENT = 16, 
    Simple_name = 17, Double_quote_string = 18, Single_quote_string = 19, 
    SPACE = 20, RETURN = 21, SECTION_COMMENT = 22, LINE_COMMENT = 23
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

