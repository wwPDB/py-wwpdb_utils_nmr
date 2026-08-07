
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/GromacsPTLexer.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  GromacsPTLexer : public antlr4::Lexer {
public:
  enum {
    L_brkt = 1, R_brkt = 2, Default = 3, Moleculetype = 4, Atomtypes = 5, 
    Pairtypes = 6, Bondtypes = 7, Angletypes = 8, Dihedraltypes = 9, Constrainttypes = 10, 
    Nonbond_params = 11, Atoms = 12, Bonds = 13, Pairs = 14, Pairs_nb = 15, 
    Angles = 16, Dihedrals = 17, Exclusions = 18, Constraints = 19, Settles = 20, 
    Virtual_sites1 = 21, Virtual_sites2 = 22, Virtual_sites3 = 23, Virtual_sites4 = 24, 
    Virtual_sitesn = 25, System = 26, Molecules = 27, Position_restraints = 28, 
    Intermolecular_interactions = 29, Integer = 30, Real = 31, SHARP_COMMENT = 32, 
    EXCLM_COMMENT = 33, SMCLN_COMMENT = 34, Simple_name = 35, SPACE = 36, 
    ENCLOSE_COMMENT = 37, SECTION_COMMENT = 38, LINE_COMMENT = 39, R_brkt_AA = 40, 
    SECTION_COMMENT_AA = 41, LINE_COMMENT_AA = 42, Simple_name_AA = 43, 
    SPACE_AA = 44, RETURN_AA = 45
  };

  enum {
    STR_ARRAY_MODE = 1
  };

  explicit GromacsPTLexer(antlr4::CharStream *input);

  ~GromacsPTLexer() override;


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

