
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CyanaNOALexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  CyanaNOALexer : public antlr4::Lexer {
public:
  enum {
    Peak = 1, From = 2, Ppm_SC = 3, Increased_from = 4, Decreased_from = 5, 
    Diagonal = 6, Out_of = 7, Assignments_used = 8, Quality = 9, Ok = 10, 
    Lone = 11, Poor = 12, Far = 13, Distance_range = 14, Violated_in = 15, 
    Structures_by = 16, Average_quality = 17, Average_number = 18, Peaks_inc_upl = 19, 
    Peaks_dec_upl = 20, Protons_used_in_less = 21, Peak_obs_dist = 22, Atom = 23, 
    Residue = 24, Peaks = 25, Shift = 26, Used = 27, Expect = 28, Selected = 29, 
    Assigned = 30, Unassigned = 31, Without_possibility = 32, With_viol_below = 33, 
    With_viol_between = 34, With_viol_above = 35, With_diagonal = 36, And = 37, 
    Cross_peaks = 38, With_off_diagonal = 39, With_unique = 40, With_short_range = 41, 
    With_medium_range = 42, With_long_range = 43, Short_range_ex = 44, Medium_range_ex = 45, 
    Long_range_ex = 46, L_paren = 47, R_paren = 48, Colon = 49, Period = 50, 
    Comma = 51, Equ_op = 52, Add_op = 53, Sub_op = 54, Div_op = 55, Angstrome = 56, 
    Integer = 57, Float = 58, Numerical_report1 = 59, Numerical_report2 = 60, 
    Numerical_report3 = 61, Numerical_report4 = 62, COMMENT = 63, Simple_name = 64, 
    SPACE = 65, ENCLOSE_COMMENT = 66, SECTION_COMMENT = 67, LINE_COMMENT = 68, 
    File_name = 69, SPACE_FN = 70, Any_name = 71, SPACE_CM = 72, RETURN_CM = 73
  };

  enum {
    FILE_NAME_MODE = 1, COMMENT_MODE = 2
  };

  explicit CyanaNOALexer(antlr4::CharStream *input);

  ~CyanaNOALexer() override;


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

