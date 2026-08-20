
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/XeasyPKLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  XeasyPKLexer : public antlr4::Lexer {
public:
  enum {
    Num_of_dim = 1, Num_of_peaks = 2, Format = 3, XEASY_WO_FORMAT = 4, Iname = 5, 
    Cyana_format = 6, Spectrum = 7, Tolerance = 8, Integer = 9, Float = 10, 
    Real = 11, COMMENT = 12, EXCLM_COMMENT = 13, SMCLN_COMMENT = 14, Simple_name = 15, 
    SPACE = 16, RETURN = 17, SECTION_COMMENT = 18, LINE_COMMENT = 19, Integer_ND = 20, 
    SPACE_ND = 21, RETURN_ND = 22, Integer_NP = 23, SPACE_NP = 24, RETURN_NP = 25, 
    Simple_name_FO = 26, SPACE_FO = 27, RETURN_FO = 28, Integer_IN = 29, 
    Simple_name_IN = 30, SPACE_IN = 31, RETURN_IN = 32, Simple_name_CY = 33, 
    SPACE_CY = 34, RETURN_CY = 35, Simple_name_SP = 36, SPACE_SP = 37, RETURN_SP = 38, 
    Float_TO = 39, TOACE_TO = 40, RETURN_TO = 41, Any_name = 42, SPACE_CM = 43, 
    RETURN_CM = 44
  };

  enum {
    NUM_OF_DIM_MODE = 1, NUM_OF_PEAK_MODE = 2, FORMAT_MODE = 3, INAME_MODE = 4, 
    CYANA_FORMAT_MODE = 5, SPECTRUM_MODE = 6, TOLERANCE_MODE = 7, COMMENT_MODE = 8
  };

  explicit XeasyPKLexer(antlr4::CharStream *input);

  ~XeasyPKLexer() override;


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

