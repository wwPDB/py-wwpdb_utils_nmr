
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BarePKLexer.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  BarePKLexer : public antlr4::Lexer {
public:
  enum {
    Peak = 1, X_PPM = 2, Y_PPM = 3, Z_PPM = 4, A_PPM = 5, Integer = 6, Float = 7, 
    Real = 8, Ambig_float = 9, SHARP_COMMENT = 10, EXCLM_COMMENT = 11, Simple_name = 12, 
    SPACE = 13, RETURN = 14, SECTION_COMMENT = 15, LINE_COMMENT = 16, X_ppm = 17, 
    Y_ppm = 18, Z_ppm = 19, A_ppm = 20, X_width = 21, Y_width = 22, Z_width = 23, 
    A_width = 24, Amplitude = 25, Volume = 26, Label = 27, Comment = 28, 
    SPACE_FO = 29, RETURN_FO = 30
  };

  enum {
    PEAK_MODE = 1
  };

  explicit BarePKLexer(antlr4::CharStream *input);

  ~BarePKLexer() override;


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

