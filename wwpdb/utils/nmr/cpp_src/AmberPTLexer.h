
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/AmberPTLexer.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  AmberPTLexer : public antlr4::Lexer {
public:
  enum {
    VERSION = 1, FLAG = 2, AMBER_ATOM_TYPE = 3, ANGLE_EQUIL_VALUE = 4, ANGLE_FORCE_CONSTANT = 5, 
    ANGLES_INC_HYDROGEN = 6, ANGLES_WITHOUT_HYDROGEN = 7, ATOMIC_NUMBER = 8, 
    ATOM_NAME = 9, ATOM_TYPE_INDEX = 10, ATOMS_PER_MOLECULE = 11, BOND_EQUIL_VALUE = 12, 
    BOND_FORCE_CONSTANT = 13, BONDS_INC_HYDROGEN = 14, BONDS_WITHOUT_HYDROGEN = 15, 
    BOX_DIMENSIONS = 16, CAP_INFO = 17, CAP_INFO2 = 18, CHARGE = 19, CMAP_COUNT = 20, 
    CMAP_RESOLUTION = 21, CMAP_PARAMETER_01 = 22, CMAP_PARAMETER_02 = 23, 
    CMAP_PARAMETER_03 = 24, CMAP_PARAMETER_04 = 25, CMAP_PARAMETER_05 = 26, 
    CMAP_PARAMETER_06 = 27, CMAP_PARAMETER_07 = 28, CMAP_PARAMETER_08 = 29, 
    CMAP_PARAMETER_09 = 30, CMAP_PARAMETER_10 = 31, CMAP_PARAMETER_11 = 32, 
    CMAP_PARAMETER_12 = 33, CMAP_PARAMETER_13 = 34, CMAP_PARAMETER_14 = 35, 
    CMAP_INDEX = 36, DIHEDRAL_FORCE_CONSTANT = 37, DIHEDRAL_PERIODICITY = 38, 
    DIHEDRAL_PHASE = 39, DIHEDRALS_INC_HYDROGEN = 40, DIHEDRALS_WITHOUT_HYDROGEN = 41, 
    EXCLUDED_ATOMS_LIST = 42, HBCUT = 43, HBOND_ACOEF = 44, HBOND_BCOEF = 45, 
    IPOL = 46, IROTAT = 47, JOIN_ARRAY = 48, LENNARD_JONES_ACOEF = 49, LENNARD_JONES_BCOEF = 50, 
    MASS = 51, NONBONDED_PARM_INDEX = 52, NUMBER_EXCLUDED_ATOMS = 53, POINTERS = 54, 
    POLARIZABILITY = 55, RADII = 56, RADIUS_SET = 57, RESIDUE_LABEL = 58, 
    RESIDUE_POINTER = 59, SCEE_SCALE_FACTOR = 60, SCNB_SCALE_FACTOR = 61, 
    SCREEN = 62, SOLTY = 63, SOLVENT_POINTERS = 64, TITLE = 65, TREE_CHAIN_CLASSIFICATION = 66, 
    SHARP_COMMENT = 67, EXCLM_COMMENT = 68, SMCLN_COMMENT = 69, FORMAT = 70, 
    SPACE = 71, LINE_COMMENT = 72, VERSION_STAMP = 73, DATE = 74, Equ_op = 75, 
    Version = 76, Date_time = 77, SPACE_VS = 78, FLAG_VS = 79, Fortran_format_A = 80, 
    Fortran_format_I = 81, Fortran_format_E = 82, Simple_name = 83, SPACE_AA = 84, 
    FLAG_AA = 85, Integer = 86, SPACE_IA = 87, FLAG_IA = 88, Real = 89, 
    SPACE_EA = 90, FLAG_EA = 91
  };

  enum {
    VERSION_MODE = 1, FORMAT_MODE = 2, STR_ARRAY_MODE = 3, INT_ARRAY_MODE = 4, 
    REAL_ARRAY_MODE = 5
  };

  explicit AmberPTLexer(antlr4::CharStream *input);

  ~AmberPTLexer() override;


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

