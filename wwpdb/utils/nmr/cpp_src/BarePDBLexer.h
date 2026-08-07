
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BarePDBLexer.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  BarePDBLexer : public antlr4::Lexer {
public:
  enum {
    Integer = 1, Float = 2, COMMENT = 3, Hetatm_decimal = 4, Integer_concat_alt = 5, 
    Float_concat_2 = 6, Float_concat_3 = 7, Atom = 8, Hetatm = 9, Ter = 10, 
    End = 11, Simple_name = 12, Null_value = 13, SPACE = 14, ENCLOSE_COMMENT = 15, 
    SECTION_COMMENT = 16, LINE_COMMENT = 17, Any_name = 18, SPACE_CM = 19, 
    RETURN_CM = 20
  };

  enum {
    COMMENT_MODE = 1
  };

  explicit BarePDBLexer(antlr4::CharStream *input);

  ~BarePDBLexer() override;


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

