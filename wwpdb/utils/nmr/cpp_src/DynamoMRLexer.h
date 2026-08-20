
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/DynamoMRLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  DynamoMRLexer : public antlr4::Lexer {
public:
  enum {
    Data = 1, Vars = 2, Format = 3, Integer = 4, Float = 5, Float_DecimalComma = 6, 
    SHARP_COMMENT = 7, EXCLM_COMMENT = 8, SMCLN_COMMENT = 9, Simple_name = 10, 
    SPACE = 11, ENCLOSE_COMMENT = 12, SECTION_COMMENT = 13, LINE_COMMENT = 14, 
    First_resid = 15, Sequence = 16, Db_name = 17, Tab_name = 18, Tab_id = 19, 
    Pales_mode = 20, Tensor_mode = 21, Saupe_matrix = 22, S_DA = 23, Saupe = 24, 
    Irreducible_rep = 25, Irreducible = 26, General_magnitude = 27, Mapping_corr = 28, 
    Mapping = 29, Inv = 30, Eigenvalues = 31, Eigenvectors = 32, X_axis = 33, 
    Y_axis = 34, Z_axis = 35, Q_euler_solutions = 36, Q_euler_angles = 37, 
    Euler_solutions = 38, Euler_angles = 39, Da = 40, Dr = 41, Aa = 42, 
    Ar = 43, Da_hn = 44, Rhombicity = 45, N = 46, Rms = 47, Chi2 = 48, Corr = 49, 
    R = 50, Q = 51, Regression = 52, Offset = 53, Slope = 54, Bax = 55, 
    Plus_minus = 56, Hz = 57, Comma_DA = 58, L_paren_DA = 59, R_paren_DA = 60, 
    L_brkt_DA = 61, R_brkt_DA = 62, Integer_DA = 63, Float_DA = 64, Real_DA = 65, 
    Simple_name_DA = 66, SPACE_DA = 67, RETURN_DA = 68, LINE_COMMENT_DA = 69, 
    One_letter_code = 70, SPACE_SQ = 71, RETURN_SQ = 72, LINE_COMMENT_SQ = 73, 
    Index = 74, Group = 75, Segname_I = 76, Resid_I = 77, Resname_I = 78, 
    Atomname_I = 79, Segname_J = 80, Resid_J = 81, Resname_J = 82, Atomname_J = 83, 
    Segname_K = 84, Resid_K = 85, Resname_K = 86, Atomname_K = 87, Segname_L = 88, 
    Resid_L = 89, Resname_L = 90, Atomname_L = 91, Resid = 92, Resname = 93, 
    A = 94, B = 95, C = 96, D = 97, DD = 98, DI = 99, D_diff = 100, D_obs = 101, 
    FC = 102, S = 103, W = 104, D_Lo = 105, D_Hi = 106, Angle_Lo = 107, 
    Angle_Hi = 108, Phase = 109, ObsJ = 110, Phi = 111, Psi = 112, Dphi = 113, 
    Dpsi = 114, Dist = 115, S2 = 116, Count = 117, Cs_count = 118, Class = 119, 
    SPACE_VA = 120, RETURN_VA = 121, LINE_COMMENT_VA = 122, Format_code = 123, 
    SPACE_FO = 124, RETURN_FO = 125, LINE_COMMENT_FO = 126
  };

  enum {
    DATA_MODE = 1, SEQ_MODE = 2, VARS_MODE = 3, FORMAT_MODE = 4
  };

  explicit DynamoMRLexer(antlr4::CharStream *input);

  ~DynamoMRLexer() override;


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

