
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/SchrodingerMRLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  SchrodingerMRLexer : public antlr4::Lexer {
public:
  enum {
    Set = 1, Struct = 2, Dist = 3, Tors = 4, Angle = 5, End = 6, Atom1 = 7, 
    Atom2 = 8, Atom3 = 9, Atom4 = 10, Lo = 11, Up = 12, Fc = 13, Target = 14, 
    Comma = 15, FXDI = 16, FXBA = 17, FXTA = 18, FXHB = 19, Entry = 20, 
    Molecule = 21, Chain = 22, Residue = 23, Atom = 24, Backbone = 25, Sidechain = 26, 
    Water = 27, Methyl = 28, Amide = 29, Smarts = 30, Entry_name = 31, Molecule_number = 32, 
    Molecule_modulo = 33, Molecule_entrynum = 34, Molecule_atoms = 35, Molecule_weight = 36, 
    Chain_name = 37, Residue_name_or_number = 38, Residue_ptype = 39, Residue_mtype = 40, 
    Residue_polarity = 41, Residue_secondary_structure = 42, Residue_position = 43, 
    Residue_inscode = 44, Atom_ptype = 45, Atom_name = 46, Atom_number = 47, 
    Atom_molnum = 48, Atom_entrynum = 49, Atom_mtype = 50, Atom_element = 51, 
    Atom_attachements = 52, Atom_atomicnumber = 53, Atom_charge = 54, Atom_formalcharge = 55, 
    Atom_displayed = 56, Atom_selected = 57, Or_op = 58, And_op = 59, Not_op = 60, 
    Fillres_op = 61, Fillmol_op = 62, Within_op = 63, Beyond_op = 64, Withinbonds_op = 65, 
    Beyondbonds_op = 66, Integer = 67, IntRange = 68, Float = 69, FloatRange = 70, 
    Slash_quote_string = 71, SMCLN_COMMENT = 72, COMMENT = 73, Simple_name = 74, 
    Simple_names = 75, Integers = 76, L_paren = 77, R_paren = 78, Lt_op = 79, 
    Gt_op = 80, Leq_op = 81, Geq_op = 82, Equ_op = 83, SPACE = 84, ENCLOSE_COMMENT = 85, 
    SECTION_COMMENT = 86, LINE_COMMENT = 87, Param_name = 88, Equ_op_SM = 89, 
    SPACE_SM = 90, RETURN_SM = 91, End_SM = 92, Hydrophilic = 93, Hydrophobic = 94, 
    Non_polar = 95, Polar = 96, Charged = 97, Positive = 98, Negative = 99, 
    IGNORE_SPACE_PM = 100, Helix_or_strand = 101, Strand_or_loop = 102, 
    Helix_or_loop = 103, Helix = 104, Strand = 105, Loop = 106, IGNORE_SPACE_SSM = 107
  };

  enum {
    STRUCT_MODE = 1, POLARITY_MODE = 2, SECONDARY_STRUCT_MODE = 3
  };

  explicit SchrodingerMRLexer(antlr4::CharStream *input);

  ~SchrodingerMRLexer() override;


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

