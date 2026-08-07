
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/VnmrPKLexer.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  VnmrPKLexer : public antlr4::Lexer {
public:
  enum {
    Peak_id = 1, Format = 2, Integer = 3, Float = 4, Real = 5, COMMENT = 6, 
    Double_quote_string = 7, EXCLM_COMMENT = 8, SMCLN_COMMENT = 9, Assignment_2d_ex = 10, 
    Assignment_3d_ex = 11, Assignment_4d_ex = 12, SPACE = 13, RETURN = 14, 
    SECTION_COMMENT = 15, LINE_COMMENT = 16, Dim_0_ppm = 17, Dim_1_ppm = 18, 
    Dim_2_ppm = 19, Dim_3_ppm = 20, Dev_0 = 21, Dev_1 = 22, Dev_2 = 23, 
    Dev_3 = 24, Amplitude_LA = 25, Volume_LA = 26, Assignment = 27, SPACE_LA = 28, 
    RETURN_LA = 29, Peak_number = 30, X_ppm = 31, Y_ppm = 32, Z_ppm = 33, 
    A_ppm = 34, Amplitude = 35, Volume = 36, Linewidth_X = 37, Linewidth_Y = 38, 
    Linewidth_Z = 39, Linewidth_A = 40, FWHM_X = 41, FWHM_Y = 42, FWHM_Z = 43, 
    FWHM_A = 44, Label = 45, Comment = 46, SPACE_FO = 47, RETURN_FO = 48, 
    Any_name = 49, SPACE_CM = 50, RETURN_CM = 51
  };

  enum {
    LABEL_MODE = 1, FORMAT_MODE = 2, COMMENT_MODE = 3
  };

  explicit VnmrPKLexer(antlr4::CharStream *input);

  ~VnmrPKLexer() override;


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

