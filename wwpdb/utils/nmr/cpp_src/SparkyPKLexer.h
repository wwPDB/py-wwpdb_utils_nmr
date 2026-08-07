
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/SparkyPKLexer.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  SparkyPKLexer : public antlr4::Lexer {
public:
  enum {
    Assignment = 1, W1 = 2, Integer = 3, Float = 4, Real = 5, Real_vol = 6, 
    SHARP_COMMENT = 7, EXCLM_COMMENT = 8, SMCLN_COMMENT = 9, Assignment_2d_ex = 10, 
    Assignment_3d_ex = 11, Assignment_4d_ex = 12, Note_2d_ex = 13, Note_3d_ex = 14, 
    Note_4d_ex = 15, Simple_name = 16, SPACE = 17, RETURN = 18, ENCLOSE_COMMENT = 19, 
    SECTION_COMMENT = 20, LINE_COMMENT = 21, W1_Hz_LA = 22, W2_Hz_LA = 23, 
    W3_Hz_LA = 24, W4_Hz_LA = 25, Lw1_Hz_LA = 26, Lw2_Hz_LA = 27, Lw3_Hz_LA = 28, 
    Lw4_Hz_LA = 29, W1_LA = 30, W2_LA = 31, W3_LA = 32, W4_LA = 33, Dev_w1_LA = 34, 
    Dev_w2_LA = 35, Dev_w3_LA = 36, Dev_w4_LA = 37, Dummy_H_LA = 38, Height_LA = 39, 
    Volume_LA = 40, Dummy_Rms_LA = 41, S_N_LA = 42, Atom1_LA = 43, Atom2_LA = 44, 
    Atom3_LA = 45, Atom4_LA = 46, Distance_LA = 47, Note_LA = 48, SPACE_LA = 49, 
    RETURN_LA = 50
  };

  enum {
    LABEL_MODE = 1
  };

  explicit SparkyPKLexer(antlr4::CharStream *input);

  ~SparkyPKLexer() override;


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

