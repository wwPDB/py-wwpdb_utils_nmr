
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrPipePKLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  NmrPipePKLexer : public antlr4::Lexer {
public:
  enum {
    Data = 1, Vars = 2, Format = 3, Null_value = 4, Null_string = 5, L_paren = 6, 
    Integer = 7, Float = 8, Real = 9, SHARP_COMMENT = 10, EXCLM_COMMENT = 11, 
    Any_name = 12, SPACE = 13, RETURN = 14, SECTION_COMMENT = 15, LINE_COMMENT = 16, 
    X_axis_DA = 17, Y_axis_DA = 18, Z_axis_DA = 19, A_axis_DA = 20, Ppm_value_DA = 21, 
    Dim_count_DA = 22, Ppm_DA = 23, Hz_DA = 24, Integer_DA = 25, Float_DA = 26, 
    Real_DA = 27, Simple_name_DA = 28, SPACE_DA = 29, RETURN_DA = 30, LINE_COMMENT_DA = 31, 
    Index = 32, X_axis = 33, Y_axis = 34, Z_axis = 35, A_axis = 36, Dx = 37, 
    Dy = 38, Dz = 39, Da = 40, X_ppm = 41, Y_ppm = 42, Z_ppm = 43, A_ppm = 44, 
    X_hz = 45, Y_hz = 46, Z_hz = 47, A_hz = 48, Xw = 49, Yw = 50, Zw = 51, 
    Aw = 52, Xw_hz = 53, Yw_hz = 54, Zw_hz = 55, Aw_hz = 56, X1 = 57, X3 = 58, 
    Y1 = 59, Y3 = 60, Z1 = 61, Z3 = 62, A1 = 63, A3 = 64, Height = 65, DHeight = 66, 
    Vol = 67, Pchi2 = 68, Type = 69, Ass = 70, ClustId = 71, Memcnt = 72, 
    Trouble = 73, PkID = 74, Sl_Z = 75, Sl_A = 76, X = 77, Y = 78, Z = 79, 
    A = 80, Intensity = 81, Assign = 82, Assign1 = 83, Assign2 = 84, Integer_VA = 85, 
    Float_VA = 86, Real_VA = 87, Simple_name_VA = 88, SPACE_VA = 89, RETURN_VA = 90, 
    LINE_COMMENT_VA = 91, Format_code = 92, SPACE_FO = 93, RETURN_FO = 94, 
    LINE_COMMENT_FO = 95, Any_name_NV = 96, SPACE_NV = 97, RETURN_NV = 98, 
    Any_name_NS = 99, SPACE_NS = 100, RETURN_NS = 101, R_paren = 102, L_brkt = 103, 
    R_brkt = 104, Comma = 105, Semicolon = 106, Number_sign = 107, Percent_sign = 108, 
    Caret = 109, Integer_PR = 110, Float_PR = 111, Real_PR = 112, Assignments_PR = 113, 
    SPACE_PR = 114, RETURN_PR = 115
  };

  enum {
    DATA_MODE = 1, VARS_MODE = 2, FORMAT_MODE = 3, NULL_VALUE_MODE = 4, 
    NULL_STRING_MODE = 5, PIPP_ROW_MODE = 6
  };

  explicit NmrPipePKLexer(antlr4::CharStream *input);

  ~NmrPipePKLexer() override;


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

