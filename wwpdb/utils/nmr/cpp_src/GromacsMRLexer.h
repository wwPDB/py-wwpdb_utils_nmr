
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/GromacsMRLexer.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  GromacsMRLexer : public antlr4::Lexer {
public:
  enum {
    L_brkt = 1, R_brkt = 2, Distance_restraints = 3, Dihedral_restraints = 4, 
    Orientation_restraints = 5, Angle_restraints = 6, Angle_restraints_z = 7, 
    Position_restraints = 8, Intermolecular_interactions = 9, Integer = 10, 
    Float = 11, SHARP_COMMENT = 12, EXCLM_COMMENT = 13, SMCLN_COMMENT = 14, 
    Simple_name = 15, SPACE = 16, ENCLOSE_COMMENT = 17, SECTION_COMMENT = 18, 
    LINE_COMMENT = 19
  };

  explicit GromacsMRLexer(antlr4::CharStream *input);

  ~GromacsMRLexer() override;


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

