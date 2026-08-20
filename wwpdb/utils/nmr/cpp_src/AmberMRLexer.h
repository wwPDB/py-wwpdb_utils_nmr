
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/AmberMRLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  AmberMRLexer : public antlr4::Lexer {
public:
  enum {
    END = 1, RST = 2, IAT = 3, RSTWT = 4, RESTRAINT = 5, ATNAM_Lp = 6, ATNAM = 7, 
    IRESID = 8, NSTEP1 = 9, NSTEP2 = 10, IRSTYP = 11, IALTD = 12, IFVARI = 13, 
    NINC = 14, IMULT = 15, R1 = 16, R2 = 17, R3 = 18, R4 = 19, RK2 = 20, 
    RK3 = 21, R1A = 22, R2A = 23, R3A = 24, R4A = 25, RK2A = 26, RK3A = 27, 
    R0 = 28, K0 = 29, R0A = 30, K0A = 31, RJCOEF = 32, IGR1 = 33, IGR2 = 34, 
    IGR3 = 35, IGR4 = 36, IGR5 = 37, IGR6 = 38, IGR7 = 39, IGR8 = 40, FXYZ = 41, 
    OUTXYZ = 42, GRNAM1_Lp = 43, GRNAM2_Lp = 44, GRNAM3_Lp = 45, GRNAM4_Lp = 46, 
    GRNAM5_Lp = 47, GRNAM6_Lp = 48, GRNAM7_Lp = 49, GRNAM8_Lp = 50, GRNAM1 = 51, 
    GRNAM2 = 52, GRNAM3 = 53, GRNAM4 = 54, GRNAM5 = 55, GRNAM6 = 56, GRNAM7 = 57, 
    GRNAM8 = 58, IR6 = 59, IFNTYP = 60, IXPK = 61, NXPK = 62, ICONSTR = 63, 
    NOEEXP = 64, NPEAK = 65, EMIX = 66, IHP = 67, JHP = 68, AEXP = 69, ARANGE = 70, 
    AWT = 71, INVWT1 = 72, INVWT2 = 73, OMEGA = 74, TAUROT = 75, TAUMET = 76, 
    ID2O = 77, OSCALE = 78, SHF = 79, NRING = 80, NATR = 81, IATR = 82, 
    NAMR = 83, STR = 84, IPROT = 85, OBS = 86, SHRANG = 87, WT = 88, NPROT = 89, 
    SHCUT = 90, NTER = 91, CTER = 92, PCSHF = 93, NME = 94, NMPMC = 95, 
    OPTPHI = 96, OPTTET = 97, OPTOMG = 98, OPTA1 = 99, OPTA2 = 100, OPTKON = 101, 
    TOLPRO = 102, MLTPRO = 103, ALIGN = 104, NDIP = 105, ID = 106, JD = 107, 
    DOBSL = 108, DOBSU = 109, DOBS = 110, DWT = 111, DATASET = 112, NUM_DATASETS = 113, 
    S11 = 114, S12 = 115, S13 = 116, S22 = 117, S23 = 118, GIGJ = 119, DIJ = 120, 
    DCUT = 121, FREEZEMOL = 122, CSA = 123, NCSA = 124, ICSA = 125, JCSA = 126, 
    KCSA = 127, COBSL = 128, COBSU = 129, COBS = 130, CWT = 131, DATASETC = 132, 
    FIELD = 133, SIGMA11 = 134, SIGMA12 = 135, SIGMA13 = 136, SIGMA22 = 137, 
    SIGMA23 = 138, CCUT = 139, Comma = 140, Residue = 141, Mapping = 142, 
    Ambig = 143, SMCLN_COMMENT = 144, COMMENT = 145, Logical = 146, L_paren = 147, 
    R_paren = 148, L_brace = 149, R_brace = 150, L_brakt = 151, R_brakt = 152, 
    Equ_op = 153, L_quot = 154, Simple_name = 155, SPACE = 156, SECTION_COMMENT = 157, 
    Any_name = 158, SPACE_CM = 159, RETURN_CM = 160, Equ_op_IP = 161, L_paren_IP = 162, 
    Integer = 163, SPACE_IP = 164, Equ_op_RP = 165, L_paren_RP = 166, Real = 167, 
    SPACE_RP = 168, Equ_op_BP = 169, BoolInt = 170, SPACE_BP = 171, L_paren_QP = 172, 
    Equ_op_QP = 173, Qstring = 174, Decimal_AP = 175, R_paren_AP = 176, 
    Equ_op_AP = 177, SPACE_AP = 178, Qstring_AP = 179, L_paren_IA = 180, 
    Equ_op_IA = 181, Comma_IA = 182, End_IA = 183, Asterisk_IA = 184, Integers = 185, 
    MultiplicativeInt = 186, COMMENT_IA = 187, L_paren_RA = 188, Equ_op_RA = 189, 
    Comma_RA = 190, End_RA = 191, Asterisk_RA = 192, Reals = 193, MultiplicativeReal = 194, 
    COMMENT_RA = 195, Equ_op_BA = 196, Comma_BA = 197, End_BA = 198, BoolInts = 199, 
    COMMENT_BA = 200, L_paren_QA = 201, Equ_op_QA = 202, Comma_QA = 203, 
    End_QA = 204, Qstrings = 205, COMMENT_QA = 206, Comma_AR = 207, R_paren_AR = 208, 
    Decimal = 209, SPACE_AR = 210, DISTANCE_F = 211, ANGLE_F = 212, TORSION_F = 213, 
    COORDINATE_F = 214, PLANE_F = 215, COM_F = 216, Integer_F = 217, Real_F = 218, 
    Ambmask_F = 219, Comma_F = 220, L_paren_F = 221, R_paren_F = 222, L_brace_F = 223, 
    R_brace_F = 224, L_brakt_F = 225, R_brakt_F = 226, R_quot = 227, SPACE_F = 228, 
    Ambig_code_MP = 229, Integer_MP = 230, Simple_name_MP = 231, Equ_op_MP = 232, 
    SPACE_MP = 233, RETURN_MP = 234, LINE_COMMENT_MP = 235
  };

  enum {
    COMMENT_MODE = 1, INT_PARAM_MODE = 2, REAL_PARAM_MODE = 3, BINT_PARAM_MODE = 4, 
    QSTR_PARAM_MODE = 5, AQSTR_PARAM_MODE = 6, AQSTR_PARAM_MODE_ = 7, INT_ARRAY_MODE = 8, 
    REAL_ARRAY_MODE = 9, BINT_ARRAY_MODE = 10, QSTR_ARRAY_MODE = 11, ARGUMENT_MODE = 12, 
    FUNC_CALL_MODE = 13, MAP_MODE = 14
  };

  explicit AmberMRLexer(antlr4::CharStream *input);

  ~AmberMRLexer() override;


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

