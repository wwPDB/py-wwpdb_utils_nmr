
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/RosettaMRLexer.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  RosettaMRLexer : public antlr4::Lexer {
public:
  enum {
    AtomPair = 1, NamedAtomPair = 2, Angle = 3, NamedAngle = 4, Dihedral = 5, 
    DihedralPair = 6, CoordinateConstraint = 7, LocalCoordinateConstraint = 8, 
    AmbiguousNMRDistance = 9, SiteConstraint = 10, SiteConstraintResidues = 11, 
    MinResidueAtomicDistance = 12, BigBin = 13, MultiConstraint = 14, AmbiguousConstraint = 15, 
    KofNConstraint = 16, END = 17, CIRCULARHARMONIC = 18, PERIODICBOUNDED = 19, 
    OFFSETPERIODICBOUNDED = 20, AMBERPERIODIC = 21, CHARMMPERIODIC = 22, 
    CIRCULARSIGMOIDAL = 23, CIRCULARSPLINE = 24, HARMONIC = 25, FLAT_HARMONIC = 26, 
    BOUNDED = 27, GAUSSIANFUNC = 28, WEIGHT = 29, SOGFUNC = 30, MIXTUREFUNC = 31, 
    CONSTANTFUNC = 32, IDENTITY = 33, SCALARWEIGHTEDFUNC = 34, SUMFUNC = 35, 
    SPLINE = 36, NONE = 37, FADE = 38, SIGMOID = 39, SQUARE_WELL = 40, SQUARE_WELL2 = 41, 
    DEGREES = 42, LINEAR_PENALTY = 43, KARPLUS = 44, SOEDINGFUNC = 45, TOPOUT = 46, 
    ETABLE = 47, USOG = 48, SOG = 49, Integer = 50, Float = 51, SHARP_COMMENT = 52, 
    EXCLM_COMMENT = 53, COMMENT = 54, Capital_integer = 55, Integer_capital = 56, 
    Simple_name = 57, SPACE = 58, ENCLOSE_COMMENT = 59, SECTION_COMMENT = 60, 
    LINE_COMMENT = 61, Atom_pair_selection = 62, Atom_selection = 63, Any_name = 64, 
    SPACE_CM = 65, RETURN_CM = 66
  };

  enum {
    COMMENT_MODE = 1
  };

  explicit RosettaMRLexer(antlr4::CharStream *input);

  ~RosettaMRLexer() override;


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

