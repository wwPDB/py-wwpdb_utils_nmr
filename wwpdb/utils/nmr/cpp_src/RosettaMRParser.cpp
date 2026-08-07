
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/RosettaMRParser.g4 by ANTLR 4.13.0


#include "RosettaMRParserVisitor.h"

#include "RosettaMRParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct RosettaMRParserStaticData final {
  RosettaMRParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  RosettaMRParserStaticData(const RosettaMRParserStaticData&) = delete;
  RosettaMRParserStaticData(RosettaMRParserStaticData&&) = delete;
  RosettaMRParserStaticData& operator=(const RosettaMRParserStaticData&) = delete;
  RosettaMRParserStaticData& operator=(RosettaMRParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag rosettamrparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
RosettaMRParserStaticData *rosettamrparserParserStaticData = nullptr;

void rosettamrparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (rosettamrparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(rosettamrparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<RosettaMRParserStaticData>(
    std::vector<std::string>{
      "rosetta_mr", "comment", "atom_pair_restraints", "atom_pair_restraint", 
      "angle_restraints", "angle_restraint", "dihedral_restraints", "dihedral_restraint", 
      "dihedral_pair_restraints", "dihedral_pair_restraint", "coordinate_restraints", 
      "coordinate_restraint", "local_coordinate_restraints", "local_coordinate_restraint", 
      "site_restraints", "site_restraint", "site_residues_restraints", "site_residues_restraint", 
      "min_residue_atomic_distance_restraints", "min_residue_atomic_distance_restraint", 
      "big_bin_restraints", "big_bin_restraint", "nested_restraints", "nested_restraint", 
      "any_restraint", "func_type_def", "rdc_restraints", "rdc_restraint", 
      "disulfide_bond_linkages", "disulfide_bond_linkage", "atom_pair_w_chain_restraints", 
      "atom_pair_w_chain_restraint", "number", "number_f", "gen_res_num", 
      "gen_simple_name"
    },
    std::vector<std::string>{
      "", "'AtomPair'", "'NamedAtomPair'", "'Angle'", "'NamedAngle'", "'Dihedral'", 
      "'DihedralPair'", "'CoordinateConstraint'", "'LocalCoordinateConstraint'", 
      "'AmbiguousNMRDistance'", "'SiteConstraint'", "'SiteConstraintResidues'", 
      "'MinResidueAtomicDistance'", "'BigBin'", "'MultiConstraint'", "'AmbiguousConstraint'", 
      "'KofNConstraint'", "'END'", "'CIRCULARHARMONIC'", "'PERIODICBOUNDED'", 
      "'OFFSETPERIODICBOUNDED'", "'AMBERPERIODIC'", "'CHARMMPERIODIC'", 
      "'CIRCULARSIGMOIDAL'", "'CIRCULARSPLINE'", "'HARMONIC'", "'FLAT_HARMONIC'", 
      "'BOUNDED'", "'GAUSSIANFUNC'", "'WEIGHT'", "'SOGFUNC'", "'MIXTUREFUNC'", 
      "'CONSTANTFUNC'", "'IDENTITY'", "'SCALARWEIGHTEDFUNC'", "'SUMFUNC'", 
      "'SPLINE'", "'NONE'", "'FADE'", "'SIGMOID'", "'SQUARE_WELL'", "'SQUARE_WELL2'", 
      "'DEGREES'", "'LINEAR_PENALTY'", "'KARPLUS'", "'SOEDINGFUNC'", "'TOPOUT'", 
      "'ETABLE'", "'USOG'", "'SOG'"
    },
    std::vector<std::string>{
      "", "AtomPair", "NamedAtomPair", "Angle", "NamedAngle", "Dihedral", 
      "DihedralPair", "CoordinateConstraint", "LocalCoordinateConstraint", 
      "AmbiguousNMRDistance", "SiteConstraint", "SiteConstraintResidues", 
      "MinResidueAtomicDistance", "BigBin", "MultiConstraint", "AmbiguousConstraint", 
      "KofNConstraint", "END", "CIRCULARHARMONIC", "PERIODICBOUNDED", "OFFSETPERIODICBOUNDED", 
      "AMBERPERIODIC", "CHARMMPERIODIC", "CIRCULARSIGMOIDAL", "CIRCULARSPLINE", 
      "HARMONIC", "FLAT_HARMONIC", "BOUNDED", "GAUSSIANFUNC", "WEIGHT", 
      "SOGFUNC", "MIXTUREFUNC", "CONSTANTFUNC", "IDENTITY", "SCALARWEIGHTEDFUNC", 
      "SUMFUNC", "SPLINE", "NONE", "FADE", "SIGMOID", "SQUARE_WELL", "SQUARE_WELL2", 
      "DEGREES", "LINEAR_PENALTY", "KARPLUS", "SOEDINGFUNC", "TOPOUT", "ETABLE", 
      "USOG", "SOG", "Integer", "Float", "SHARP_COMMENT", "EXCLM_COMMENT", 
      "COMMENT", "Capital_integer", "Integer_capital", "Simple_name", "SPACE", 
      "ENCLOSE_COMMENT", "SECTION_COMMENT", "LINE_COMMENT", "Atom_pair_selection", 
      "Atom_selection", "Any_name", "SPACE_CM", "RETURN_CM"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,66,499,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,
  	21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,2,27,7,27,2,28,7,
  	28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,7,33,2,34,7,34,2,35,7,
  	35,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,88,
  	8,0,10,0,12,0,91,9,0,1,0,1,0,1,1,1,1,5,1,97,8,1,10,1,12,1,100,9,1,1,1,
  	1,1,1,2,4,2,105,8,2,11,2,12,2,106,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,4,4,
  	117,8,4,11,4,12,4,118,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,4,6,131,
  	8,6,11,6,12,6,132,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,4,8,
  	147,8,8,11,8,12,8,148,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
  	1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,4,10,171,8,10,11,10,12,10,172,1,11,1,
  	11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,4,12,186,8,12,11,12,12,
  	12,187,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
  	14,4,14,203,8,14,11,14,12,14,204,1,15,1,15,1,15,1,15,1,15,1,15,1,16,4,
  	16,214,8,16,11,16,12,16,215,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,18,4,
  	18,226,8,18,11,18,12,18,227,1,19,1,19,1,19,1,19,1,19,1,20,4,20,236,8,
  	20,11,20,12,20,237,1,21,1,21,1,21,1,21,1,21,1,22,4,22,246,8,22,11,22,
  	12,22,247,1,23,1,23,1,23,1,23,3,23,254,8,23,1,23,1,23,4,23,258,8,23,11,
  	23,12,23,259,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,
  	24,3,24,274,8,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,285,
  	8,25,1,25,1,25,5,25,289,8,25,10,25,12,25,292,9,25,1,25,1,25,1,25,1,25,
  	1,25,1,25,3,25,300,8,25,1,25,1,25,5,25,304,8,25,10,25,12,25,307,9,25,
  	1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,316,8,25,1,25,1,25,5,25,320,8,
  	25,10,25,12,25,323,9,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,
  	1,25,1,25,1,25,1,25,4,25,338,8,25,11,25,12,25,339,1,25,1,25,1,25,1,25,
  	1,25,1,25,3,25,348,8,25,1,25,1,25,1,25,1,25,1,25,1,25,4,25,356,8,25,11,
  	25,12,25,357,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,
  	25,1,25,1,25,1,25,1,25,1,25,1,25,4,25,378,8,25,11,25,12,25,379,1,25,1,
  	25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,5,25,394,8,25,10,
  	25,12,25,397,9,25,4,25,399,8,25,11,25,12,25,400,3,25,403,8,25,1,25,1,
  	25,1,25,1,25,1,25,1,25,3,25,411,8,25,1,25,1,25,1,25,1,25,1,25,3,25,418,
  	8,25,1,25,1,25,1,25,1,25,5,25,424,8,25,10,25,12,25,427,9,25,1,25,1,25,
  	1,25,1,25,1,25,1,25,1,25,4,25,436,8,25,11,25,12,25,437,1,25,1,25,1,25,
  	1,25,1,25,1,25,1,25,1,25,1,25,4,25,449,8,25,11,25,12,25,450,3,25,453,
  	8,25,1,25,3,25,456,8,25,1,26,4,26,459,8,26,11,26,12,26,460,1,27,1,27,
  	1,27,1,27,1,27,1,27,1,28,4,28,470,8,28,11,28,12,28,471,1,29,1,29,1,29,
  	1,30,4,30,478,8,30,11,30,12,30,479,1,31,1,31,1,31,1,31,1,31,1,31,1,31,
  	1,31,1,31,1,32,1,32,1,33,1,33,1,34,1,34,1,35,1,35,1,35,0,0,36,0,2,4,6,
  	8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,
  	56,58,60,62,64,66,68,70,0,11,1,0,62,64,1,1,66,66,2,0,1,2,9,9,1,0,3,4,
  	3,0,18,18,25,25,39,40,3,0,21,22,26,26,46,46,2,0,23,23,43,43,2,0,31,31,
  	44,45,1,0,50,51,2,0,50,50,55,56,1,0,55,57,546,0,89,1,0,0,0,2,94,1,0,0,
  	0,4,104,1,0,0,0,6,108,1,0,0,0,8,116,1,0,0,0,10,120,1,0,0,0,12,130,1,0,
  	0,0,14,134,1,0,0,0,16,146,1,0,0,0,18,150,1,0,0,0,20,170,1,0,0,0,22,174,
  	1,0,0,0,24,185,1,0,0,0,26,189,1,0,0,0,28,202,1,0,0,0,30,206,1,0,0,0,32,
  	213,1,0,0,0,34,217,1,0,0,0,36,225,1,0,0,0,38,229,1,0,0,0,40,235,1,0,0,
  	0,42,239,1,0,0,0,44,245,1,0,0,0,46,253,1,0,0,0,48,273,1,0,0,0,50,452,
  	1,0,0,0,52,458,1,0,0,0,54,462,1,0,0,0,56,469,1,0,0,0,58,473,1,0,0,0,60,
  	477,1,0,0,0,62,481,1,0,0,0,64,490,1,0,0,0,66,492,1,0,0,0,68,494,1,0,0,
  	0,70,496,1,0,0,0,72,88,3,2,1,0,73,88,3,4,2,0,74,88,3,8,4,0,75,88,3,12,
  	6,0,76,88,3,16,8,0,77,88,3,20,10,0,78,88,3,24,12,0,79,88,3,28,14,0,80,
  	88,3,32,16,0,81,88,3,36,18,0,82,88,3,40,20,0,83,88,3,44,22,0,84,88,3,
  	52,26,0,85,88,3,56,28,0,86,88,3,60,30,0,87,72,1,0,0,0,87,73,1,0,0,0,87,
  	74,1,0,0,0,87,75,1,0,0,0,87,76,1,0,0,0,87,77,1,0,0,0,87,78,1,0,0,0,87,
  	79,1,0,0,0,87,80,1,0,0,0,87,81,1,0,0,0,87,82,1,0,0,0,87,83,1,0,0,0,87,
  	84,1,0,0,0,87,85,1,0,0,0,87,86,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,
  	90,1,0,0,0,90,92,1,0,0,0,91,89,1,0,0,0,92,93,5,0,0,1,93,1,1,0,0,0,94,
  	98,5,54,0,0,95,97,7,0,0,0,96,95,1,0,0,0,97,100,1,0,0,0,98,96,1,0,0,0,
  	98,99,1,0,0,0,99,101,1,0,0,0,100,98,1,0,0,0,101,102,7,1,0,0,102,3,1,0,
  	0,0,103,105,3,6,3,0,104,103,1,0,0,0,105,106,1,0,0,0,106,104,1,0,0,0,106,
  	107,1,0,0,0,107,5,1,0,0,0,108,109,7,2,0,0,109,110,3,70,35,0,110,111,3,
  	68,34,0,111,112,3,70,35,0,112,113,3,68,34,0,113,114,3,50,25,0,114,7,1,
  	0,0,0,115,117,3,10,5,0,116,115,1,0,0,0,117,118,1,0,0,0,118,116,1,0,0,
  	0,118,119,1,0,0,0,119,9,1,0,0,0,120,121,7,3,0,0,121,122,3,70,35,0,122,
  	123,3,68,34,0,123,124,3,70,35,0,124,125,3,68,34,0,125,126,3,70,35,0,126,
  	127,3,68,34,0,127,128,3,50,25,0,128,11,1,0,0,0,129,131,3,14,7,0,130,129,
  	1,0,0,0,131,132,1,0,0,0,132,130,1,0,0,0,132,133,1,0,0,0,133,13,1,0,0,
  	0,134,135,5,5,0,0,135,136,3,70,35,0,136,137,3,68,34,0,137,138,3,70,35,
  	0,138,139,3,68,34,0,139,140,3,70,35,0,140,141,3,68,34,0,141,142,3,70,
  	35,0,142,143,3,68,34,0,143,144,3,50,25,0,144,15,1,0,0,0,145,147,3,18,
  	9,0,146,145,1,0,0,0,147,148,1,0,0,0,148,146,1,0,0,0,148,149,1,0,0,0,149,
  	17,1,0,0,0,150,151,5,6,0,0,151,152,3,70,35,0,152,153,3,68,34,0,153,154,
  	3,70,35,0,154,155,3,68,34,0,155,156,3,70,35,0,156,157,3,68,34,0,157,158,
  	3,70,35,0,158,159,3,68,34,0,159,160,3,70,35,0,160,161,3,68,34,0,161,162,
  	3,70,35,0,162,163,3,68,34,0,163,164,3,70,35,0,164,165,3,68,34,0,165,166,
  	3,70,35,0,166,167,3,68,34,0,167,168,3,50,25,0,168,19,1,0,0,0,169,171,
  	3,22,11,0,170,169,1,0,0,0,171,172,1,0,0,0,172,170,1,0,0,0,172,173,1,0,
  	0,0,173,21,1,0,0,0,174,175,5,7,0,0,175,176,3,70,35,0,176,177,3,68,34,
  	0,177,178,3,70,35,0,178,179,3,68,34,0,179,180,3,64,32,0,180,181,3,64,
  	32,0,181,182,3,64,32,0,182,183,3,50,25,0,183,23,1,0,0,0,184,186,3,26,
  	13,0,185,184,1,0,0,0,186,187,1,0,0,0,187,185,1,0,0,0,187,188,1,0,0,0,
  	188,25,1,0,0,0,189,190,5,8,0,0,190,191,3,70,35,0,191,192,3,68,34,0,192,
  	193,3,70,35,0,193,194,3,70,35,0,194,195,3,70,35,0,195,196,5,50,0,0,196,
  	197,3,64,32,0,197,198,3,64,32,0,198,199,3,64,32,0,199,200,3,50,25,0,200,
  	27,1,0,0,0,201,203,3,30,15,0,202,201,1,0,0,0,203,204,1,0,0,0,204,202,
  	1,0,0,0,204,205,1,0,0,0,205,29,1,0,0,0,206,207,5,10,0,0,207,208,3,70,
  	35,0,208,209,3,68,34,0,209,210,5,57,0,0,210,211,3,50,25,0,211,31,1,0,
  	0,0,212,214,3,34,17,0,213,212,1,0,0,0,214,215,1,0,0,0,215,213,1,0,0,0,
  	215,216,1,0,0,0,216,33,1,0,0,0,217,218,5,11,0,0,218,219,3,68,34,0,219,
  	220,3,70,35,0,220,221,5,50,0,0,221,222,5,50,0,0,222,223,3,50,25,0,223,
  	35,1,0,0,0,224,226,3,38,19,0,225,224,1,0,0,0,226,227,1,0,0,0,227,225,
  	1,0,0,0,227,228,1,0,0,0,228,37,1,0,0,0,229,230,5,12,0,0,230,231,3,68,
  	34,0,231,232,3,68,34,0,232,233,3,64,32,0,233,39,1,0,0,0,234,236,3,42,
  	21,0,235,234,1,0,0,0,236,237,1,0,0,0,237,235,1,0,0,0,237,238,1,0,0,0,
  	238,41,1,0,0,0,239,240,5,13,0,0,240,241,3,68,34,0,241,242,5,57,0,0,242,
  	243,3,64,32,0,243,43,1,0,0,0,244,246,3,46,23,0,245,244,1,0,0,0,246,247,
  	1,0,0,0,247,245,1,0,0,0,247,248,1,0,0,0,248,45,1,0,0,0,249,254,5,14,0,
  	0,250,254,5,15,0,0,251,252,5,16,0,0,252,254,5,50,0,0,253,249,1,0,0,0,
  	253,250,1,0,0,0,253,251,1,0,0,0,254,257,1,0,0,0,255,258,3,48,24,0,256,
  	258,3,46,23,0,257,255,1,0,0,0,257,256,1,0,0,0,258,259,1,0,0,0,259,257,
  	1,0,0,0,259,260,1,0,0,0,260,261,1,0,0,0,261,262,5,17,0,0,262,47,1,0,0,
  	0,263,274,3,6,3,0,264,274,3,10,5,0,265,274,3,14,7,0,266,274,3,18,9,0,
  	267,274,3,22,11,0,268,274,3,26,13,0,269,274,3,30,15,0,270,274,3,34,17,
  	0,271,274,3,38,19,0,272,274,3,42,21,0,273,263,1,0,0,0,273,264,1,0,0,0,
  	273,265,1,0,0,0,273,266,1,0,0,0,273,267,1,0,0,0,273,268,1,0,0,0,273,269,
  	1,0,0,0,273,270,1,0,0,0,273,271,1,0,0,0,273,272,1,0,0,0,274,49,1,0,0,
  	0,275,276,7,4,0,0,276,277,3,66,33,0,277,278,3,66,33,0,278,453,1,0,0,0,
  	279,280,5,27,0,0,280,281,3,66,33,0,281,282,3,66,33,0,282,284,3,66,33,
  	0,283,285,3,66,33,0,284,283,1,0,0,0,284,285,1,0,0,0,285,290,1,0,0,0,286,
  	289,5,57,0,0,287,289,3,66,33,0,288,286,1,0,0,0,288,287,1,0,0,0,289,292,
  	1,0,0,0,290,288,1,0,0,0,290,291,1,0,0,0,291,453,1,0,0,0,292,290,1,0,0,
  	0,293,294,5,19,0,0,294,295,3,66,33,0,295,296,3,66,33,0,296,297,3,66,33,
  	0,297,299,3,66,33,0,298,300,3,66,33,0,299,298,1,0,0,0,299,300,1,0,0,0,
  	300,305,1,0,0,0,301,304,5,57,0,0,302,304,3,66,33,0,303,301,1,0,0,0,303,
  	302,1,0,0,0,304,307,1,0,0,0,305,303,1,0,0,0,305,306,1,0,0,0,306,453,1,
  	0,0,0,307,305,1,0,0,0,308,309,5,20,0,0,309,310,3,66,33,0,310,311,3,66,
  	33,0,311,312,3,66,33,0,312,313,3,66,33,0,313,315,3,66,33,0,314,316,3,
  	66,33,0,315,314,1,0,0,0,315,316,1,0,0,0,316,321,1,0,0,0,317,320,5,57,
  	0,0,318,320,3,66,33,0,319,317,1,0,0,0,319,318,1,0,0,0,320,323,1,0,0,0,
  	321,319,1,0,0,0,321,322,1,0,0,0,322,453,1,0,0,0,323,321,1,0,0,0,324,325,
  	7,5,0,0,325,326,3,66,33,0,326,327,3,66,33,0,327,328,3,66,33,0,328,453,
  	1,0,0,0,329,330,7,6,0,0,330,331,3,66,33,0,331,332,3,66,33,0,332,333,3,
  	66,33,0,333,334,3,66,33,0,334,453,1,0,0,0,335,337,5,24,0,0,336,338,3,
  	66,33,0,337,336,1,0,0,0,338,339,1,0,0,0,339,337,1,0,0,0,339,340,1,0,0,
  	0,340,453,1,0,0,0,341,342,5,28,0,0,342,343,3,66,33,0,343,344,3,66,33,
  	0,344,347,5,57,0,0,345,346,5,29,0,0,346,348,3,66,33,0,347,345,1,0,0,0,
  	347,348,1,0,0,0,348,453,1,0,0,0,349,350,5,30,0,0,350,355,5,50,0,0,351,
  	352,3,66,33,0,352,353,3,66,33,0,353,354,3,66,33,0,354,356,1,0,0,0,355,
  	351,1,0,0,0,356,357,1,0,0,0,357,355,1,0,0,0,357,358,1,0,0,0,358,453,1,
  	0,0,0,359,360,7,7,0,0,360,361,3,66,33,0,361,362,3,66,33,0,362,363,3,66,
  	33,0,363,364,3,66,33,0,364,365,3,66,33,0,365,366,3,66,33,0,366,453,1,
  	0,0,0,367,368,5,32,0,0,368,453,3,66,33,0,369,453,5,33,0,0,370,371,5,34,
  	0,0,371,372,3,66,33,0,372,373,3,50,25,0,373,453,1,0,0,0,374,375,5,35,
  	0,0,375,377,5,50,0,0,376,378,3,50,25,0,377,376,1,0,0,0,378,379,1,0,0,
  	0,379,377,1,0,0,0,379,380,1,0,0,0,380,453,1,0,0,0,381,382,5,36,0,0,382,
  	402,5,57,0,0,383,384,3,66,33,0,384,385,3,66,33,0,385,386,3,66,33,0,386,
  	403,1,0,0,0,387,388,5,37,0,0,388,389,3,66,33,0,389,390,3,66,33,0,390,
  	398,3,66,33,0,391,395,5,57,0,0,392,394,3,66,33,0,393,392,1,0,0,0,394,
  	397,1,0,0,0,395,393,1,0,0,0,395,396,1,0,0,0,396,399,1,0,0,0,397,395,1,
  	0,0,0,398,391,1,0,0,0,399,400,1,0,0,0,400,398,1,0,0,0,400,401,1,0,0,0,
  	401,403,1,0,0,0,402,383,1,0,0,0,402,387,1,0,0,0,403,453,1,0,0,0,404,405,
  	5,38,0,0,405,406,3,66,33,0,406,407,3,66,33,0,407,408,3,66,33,0,408,410,
  	3,66,33,0,409,411,3,66,33,0,410,409,1,0,0,0,410,411,1,0,0,0,411,453,1,
  	0,0,0,412,413,5,41,0,0,413,414,3,66,33,0,414,415,3,66,33,0,415,417,3,
  	66,33,0,416,418,5,42,0,0,417,416,1,0,0,0,417,418,1,0,0,0,418,453,1,0,
  	0,0,419,420,5,47,0,0,420,421,3,66,33,0,421,425,3,66,33,0,422,424,3,66,
  	33,0,423,422,1,0,0,0,424,427,1,0,0,0,425,423,1,0,0,0,425,426,1,0,0,0,
  	426,453,1,0,0,0,427,425,1,0,0,0,428,429,5,48,0,0,429,435,5,50,0,0,430,
  	431,3,66,33,0,431,432,3,66,33,0,432,433,3,66,33,0,433,434,3,66,33,0,434,
  	436,1,0,0,0,435,430,1,0,0,0,436,437,1,0,0,0,437,435,1,0,0,0,437,438,1,
  	0,0,0,438,453,1,0,0,0,439,440,5,49,0,0,440,448,5,50,0,0,441,442,3,66,
  	33,0,442,443,3,66,33,0,443,444,3,66,33,0,444,445,3,66,33,0,445,446,3,
  	66,33,0,446,447,3,66,33,0,447,449,1,0,0,0,448,441,1,0,0,0,449,450,1,0,
  	0,0,450,448,1,0,0,0,450,451,1,0,0,0,451,453,1,0,0,0,452,275,1,0,0,0,452,
  	279,1,0,0,0,452,293,1,0,0,0,452,308,1,0,0,0,452,324,1,0,0,0,452,329,1,
  	0,0,0,452,335,1,0,0,0,452,341,1,0,0,0,452,349,1,0,0,0,452,359,1,0,0,0,
  	452,367,1,0,0,0,452,369,1,0,0,0,452,370,1,0,0,0,452,374,1,0,0,0,452,381,
  	1,0,0,0,452,404,1,0,0,0,452,412,1,0,0,0,452,419,1,0,0,0,452,428,1,0,0,
  	0,452,439,1,0,0,0,453,455,1,0,0,0,454,456,3,2,1,0,455,454,1,0,0,0,455,
  	456,1,0,0,0,456,51,1,0,0,0,457,459,3,54,27,0,458,457,1,0,0,0,459,460,
  	1,0,0,0,460,458,1,0,0,0,460,461,1,0,0,0,461,53,1,0,0,0,462,463,3,68,34,
  	0,463,464,3,70,35,0,464,465,3,68,34,0,465,466,3,70,35,0,466,467,3,64,
  	32,0,467,55,1,0,0,0,468,470,3,58,29,0,469,468,1,0,0,0,470,471,1,0,0,0,
  	471,469,1,0,0,0,471,472,1,0,0,0,472,57,1,0,0,0,473,474,3,68,34,0,474,
  	475,3,68,34,0,475,59,1,0,0,0,476,478,3,62,31,0,477,476,1,0,0,0,478,479,
  	1,0,0,0,479,477,1,0,0,0,479,480,1,0,0,0,480,61,1,0,0,0,481,482,7,2,0,
  	0,482,483,3,70,35,0,483,484,5,50,0,0,484,485,3,70,35,0,485,486,3,70,35,
  	0,486,487,5,50,0,0,487,488,3,70,35,0,488,489,3,50,25,0,489,63,1,0,0,0,
  	490,491,7,8,0,0,491,65,1,0,0,0,492,493,7,8,0,0,493,67,1,0,0,0,494,495,
  	7,9,0,0,495,69,1,0,0,0,496,497,7,10,0,0,497,71,1,0,0,0,44,87,89,98,106,
  	118,132,148,172,187,204,215,227,237,247,253,257,259,273,284,288,290,299,
  	303,305,315,319,321,339,347,357,379,395,400,402,410,417,425,437,450,452,
  	455,460,471,479
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  rosettamrparserParserStaticData = staticData.release();
}

}

RosettaMRParser::RosettaMRParser(TokenStream *input) : RosettaMRParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

RosettaMRParser::RosettaMRParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  RosettaMRParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *rosettamrparserParserStaticData->atn, rosettamrparserParserStaticData->decisionToDFA, rosettamrparserParserStaticData->sharedContextCache, options);
}

RosettaMRParser::~RosettaMRParser() {
  delete _interpreter;
}

const atn::ATN& RosettaMRParser::getATN() const {
  return *rosettamrparserParserStaticData->atn;
}

std::string RosettaMRParser::getGrammarFileName() const {
  return "RosettaMRParser.g4";
}

const std::vector<std::string>& RosettaMRParser::getRuleNames() const {
  return rosettamrparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& RosettaMRParser::getVocabulary() const {
  return rosettamrparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView RosettaMRParser::getSerializedATN() const {
  return rosettamrparserParserStaticData->serializedATN;
}


//----------------- Rosetta_mrContext ------------------------------------------------------------------

RosettaMRParser::Rosetta_mrContext::Rosetta_mrContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* RosettaMRParser::Rosetta_mrContext::EOF() {
  return getToken(RosettaMRParser::EOF, 0);
}

std::vector<RosettaMRParser::CommentContext *> RosettaMRParser::Rosetta_mrContext::comment() {
  return getRuleContexts<RosettaMRParser::CommentContext>();
}

RosettaMRParser::CommentContext* RosettaMRParser::Rosetta_mrContext::comment(size_t i) {
  return getRuleContext<RosettaMRParser::CommentContext>(i);
}

std::vector<RosettaMRParser::Atom_pair_restraintsContext *> RosettaMRParser::Rosetta_mrContext::atom_pair_restraints() {
  return getRuleContexts<RosettaMRParser::Atom_pair_restraintsContext>();
}

RosettaMRParser::Atom_pair_restraintsContext* RosettaMRParser::Rosetta_mrContext::atom_pair_restraints(size_t i) {
  return getRuleContext<RosettaMRParser::Atom_pair_restraintsContext>(i);
}

std::vector<RosettaMRParser::Angle_restraintsContext *> RosettaMRParser::Rosetta_mrContext::angle_restraints() {
  return getRuleContexts<RosettaMRParser::Angle_restraintsContext>();
}

RosettaMRParser::Angle_restraintsContext* RosettaMRParser::Rosetta_mrContext::angle_restraints(size_t i) {
  return getRuleContext<RosettaMRParser::Angle_restraintsContext>(i);
}

std::vector<RosettaMRParser::Dihedral_restraintsContext *> RosettaMRParser::Rosetta_mrContext::dihedral_restraints() {
  return getRuleContexts<RosettaMRParser::Dihedral_restraintsContext>();
}

RosettaMRParser::Dihedral_restraintsContext* RosettaMRParser::Rosetta_mrContext::dihedral_restraints(size_t i) {
  return getRuleContext<RosettaMRParser::Dihedral_restraintsContext>(i);
}

std::vector<RosettaMRParser::Dihedral_pair_restraintsContext *> RosettaMRParser::Rosetta_mrContext::dihedral_pair_restraints() {
  return getRuleContexts<RosettaMRParser::Dihedral_pair_restraintsContext>();
}

RosettaMRParser::Dihedral_pair_restraintsContext* RosettaMRParser::Rosetta_mrContext::dihedral_pair_restraints(size_t i) {
  return getRuleContext<RosettaMRParser::Dihedral_pair_restraintsContext>(i);
}

std::vector<RosettaMRParser::Coordinate_restraintsContext *> RosettaMRParser::Rosetta_mrContext::coordinate_restraints() {
  return getRuleContexts<RosettaMRParser::Coordinate_restraintsContext>();
}

RosettaMRParser::Coordinate_restraintsContext* RosettaMRParser::Rosetta_mrContext::coordinate_restraints(size_t i) {
  return getRuleContext<RosettaMRParser::Coordinate_restraintsContext>(i);
}

std::vector<RosettaMRParser::Local_coordinate_restraintsContext *> RosettaMRParser::Rosetta_mrContext::local_coordinate_restraints() {
  return getRuleContexts<RosettaMRParser::Local_coordinate_restraintsContext>();
}

RosettaMRParser::Local_coordinate_restraintsContext* RosettaMRParser::Rosetta_mrContext::local_coordinate_restraints(size_t i) {
  return getRuleContext<RosettaMRParser::Local_coordinate_restraintsContext>(i);
}

std::vector<RosettaMRParser::Site_restraintsContext *> RosettaMRParser::Rosetta_mrContext::site_restraints() {
  return getRuleContexts<RosettaMRParser::Site_restraintsContext>();
}

RosettaMRParser::Site_restraintsContext* RosettaMRParser::Rosetta_mrContext::site_restraints(size_t i) {
  return getRuleContext<RosettaMRParser::Site_restraintsContext>(i);
}

std::vector<RosettaMRParser::Site_residues_restraintsContext *> RosettaMRParser::Rosetta_mrContext::site_residues_restraints() {
  return getRuleContexts<RosettaMRParser::Site_residues_restraintsContext>();
}

RosettaMRParser::Site_residues_restraintsContext* RosettaMRParser::Rosetta_mrContext::site_residues_restraints(size_t i) {
  return getRuleContext<RosettaMRParser::Site_residues_restraintsContext>(i);
}

std::vector<RosettaMRParser::Min_residue_atomic_distance_restraintsContext *> RosettaMRParser::Rosetta_mrContext::min_residue_atomic_distance_restraints() {
  return getRuleContexts<RosettaMRParser::Min_residue_atomic_distance_restraintsContext>();
}

RosettaMRParser::Min_residue_atomic_distance_restraintsContext* RosettaMRParser::Rosetta_mrContext::min_residue_atomic_distance_restraints(size_t i) {
  return getRuleContext<RosettaMRParser::Min_residue_atomic_distance_restraintsContext>(i);
}

std::vector<RosettaMRParser::Big_bin_restraintsContext *> RosettaMRParser::Rosetta_mrContext::big_bin_restraints() {
  return getRuleContexts<RosettaMRParser::Big_bin_restraintsContext>();
}

RosettaMRParser::Big_bin_restraintsContext* RosettaMRParser::Rosetta_mrContext::big_bin_restraints(size_t i) {
  return getRuleContext<RosettaMRParser::Big_bin_restraintsContext>(i);
}

std::vector<RosettaMRParser::Nested_restraintsContext *> RosettaMRParser::Rosetta_mrContext::nested_restraints() {
  return getRuleContexts<RosettaMRParser::Nested_restraintsContext>();
}

RosettaMRParser::Nested_restraintsContext* RosettaMRParser::Rosetta_mrContext::nested_restraints(size_t i) {
  return getRuleContext<RosettaMRParser::Nested_restraintsContext>(i);
}

std::vector<RosettaMRParser::Rdc_restraintsContext *> RosettaMRParser::Rosetta_mrContext::rdc_restraints() {
  return getRuleContexts<RosettaMRParser::Rdc_restraintsContext>();
}

RosettaMRParser::Rdc_restraintsContext* RosettaMRParser::Rosetta_mrContext::rdc_restraints(size_t i) {
  return getRuleContext<RosettaMRParser::Rdc_restraintsContext>(i);
}

std::vector<RosettaMRParser::Disulfide_bond_linkagesContext *> RosettaMRParser::Rosetta_mrContext::disulfide_bond_linkages() {
  return getRuleContexts<RosettaMRParser::Disulfide_bond_linkagesContext>();
}

RosettaMRParser::Disulfide_bond_linkagesContext* RosettaMRParser::Rosetta_mrContext::disulfide_bond_linkages(size_t i) {
  return getRuleContext<RosettaMRParser::Disulfide_bond_linkagesContext>(i);
}

std::vector<RosettaMRParser::Atom_pair_w_chain_restraintsContext *> RosettaMRParser::Rosetta_mrContext::atom_pair_w_chain_restraints() {
  return getRuleContexts<RosettaMRParser::Atom_pair_w_chain_restraintsContext>();
}

RosettaMRParser::Atom_pair_w_chain_restraintsContext* RosettaMRParser::Rosetta_mrContext::atom_pair_w_chain_restraints(size_t i) {
  return getRuleContext<RosettaMRParser::Atom_pair_w_chain_restraintsContext>(i);
}


size_t RosettaMRParser::Rosetta_mrContext::getRuleIndex() const {
  return RosettaMRParser::RuleRosetta_mr;
}


std::any RosettaMRParser::Rosetta_mrContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitRosetta_mr(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Rosetta_mrContext* RosettaMRParser::rosetta_mr() {
  Rosetta_mrContext *_localctx = _tracker.createInstance<Rosetta_mrContext>(_ctx, getState());
  enterRule(_localctx, 0, RosettaMRParser::RuleRosetta_mr);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(89);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 127226689473347582) != 0)) {
      setState(87);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx)) {
      case 1: {
        setState(72);
        comment();
        break;
      }

      case 2: {
        setState(73);
        atom_pair_restraints();
        break;
      }

      case 3: {
        setState(74);
        angle_restraints();
        break;
      }

      case 4: {
        setState(75);
        dihedral_restraints();
        break;
      }

      case 5: {
        setState(76);
        dihedral_pair_restraints();
        break;
      }

      case 6: {
        setState(77);
        coordinate_restraints();
        break;
      }

      case 7: {
        setState(78);
        local_coordinate_restraints();
        break;
      }

      case 8: {
        setState(79);
        site_restraints();
        break;
      }

      case 9: {
        setState(80);
        site_residues_restraints();
        break;
      }

      case 10: {
        setState(81);
        min_residue_atomic_distance_restraints();
        break;
      }

      case 11: {
        setState(82);
        big_bin_restraints();
        break;
      }

      case 12: {
        setState(83);
        nested_restraints();
        break;
      }

      case 13: {
        setState(84);
        rdc_restraints();
        break;
      }

      case 14: {
        setState(85);
        disulfide_bond_linkages();
        break;
      }

      case 15: {
        setState(86);
        atom_pair_w_chain_restraints();
        break;
      }

      default:
        break;
      }
      setState(91);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(92);
    match(RosettaMRParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- CommentContext ------------------------------------------------------------------

RosettaMRParser::CommentContext::CommentContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* RosettaMRParser::CommentContext::COMMENT() {
  return getToken(RosettaMRParser::COMMENT, 0);
}

tree::TerminalNode* RosettaMRParser::CommentContext::RETURN_CM() {
  return getToken(RosettaMRParser::RETURN_CM, 0);
}

tree::TerminalNode* RosettaMRParser::CommentContext::EOF() {
  return getToken(RosettaMRParser::EOF, 0);
}

std::vector<tree::TerminalNode *> RosettaMRParser::CommentContext::Atom_pair_selection() {
  return getTokens(RosettaMRParser::Atom_pair_selection);
}

tree::TerminalNode* RosettaMRParser::CommentContext::Atom_pair_selection(size_t i) {
  return getToken(RosettaMRParser::Atom_pair_selection, i);
}

std::vector<tree::TerminalNode *> RosettaMRParser::CommentContext::Atom_selection() {
  return getTokens(RosettaMRParser::Atom_selection);
}

tree::TerminalNode* RosettaMRParser::CommentContext::Atom_selection(size_t i) {
  return getToken(RosettaMRParser::Atom_selection, i);
}

std::vector<tree::TerminalNode *> RosettaMRParser::CommentContext::Any_name() {
  return getTokens(RosettaMRParser::Any_name);
}

tree::TerminalNode* RosettaMRParser::CommentContext::Any_name(size_t i) {
  return getToken(RosettaMRParser::Any_name, i);
}


size_t RosettaMRParser::CommentContext::getRuleIndex() const {
  return RosettaMRParser::RuleComment;
}


std::any RosettaMRParser::CommentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitComment(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::CommentContext* RosettaMRParser::comment() {
  CommentContext *_localctx = _tracker.createInstance<CommentContext>(_ctx, getState());
  enterRule(_localctx, 2, RosettaMRParser::RuleComment);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(94);
    match(RosettaMRParser::COMMENT);
    setState(98);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (((((_la - 62) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 62)) & 7) != 0)) {
      setState(95);
      _la = _input->LA(1);
      if (!(((((_la - 62) & ~ 0x3fULL) == 0) &&
        ((1ULL << (_la - 62)) & 7) != 0))) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(100);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(101);
    _la = _input->LA(1);
    if (!(_la == RosettaMRParser::EOF || _la == RosettaMRParser::RETURN_CM)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Atom_pair_restraintsContext ------------------------------------------------------------------

RosettaMRParser::Atom_pair_restraintsContext::Atom_pair_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<RosettaMRParser::Atom_pair_restraintContext *> RosettaMRParser::Atom_pair_restraintsContext::atom_pair_restraint() {
  return getRuleContexts<RosettaMRParser::Atom_pair_restraintContext>();
}

RosettaMRParser::Atom_pair_restraintContext* RosettaMRParser::Atom_pair_restraintsContext::atom_pair_restraint(size_t i) {
  return getRuleContext<RosettaMRParser::Atom_pair_restraintContext>(i);
}


size_t RosettaMRParser::Atom_pair_restraintsContext::getRuleIndex() const {
  return RosettaMRParser::RuleAtom_pair_restraints;
}


std::any RosettaMRParser::Atom_pair_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitAtom_pair_restraints(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Atom_pair_restraintsContext* RosettaMRParser::atom_pair_restraints() {
  Atom_pair_restraintsContext *_localctx = _tracker.createInstance<Atom_pair_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 4, RosettaMRParser::RuleAtom_pair_restraints);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(104); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(103);
              atom_pair_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(106); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 3, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Atom_pair_restraintContext ------------------------------------------------------------------

RosettaMRParser::Atom_pair_restraintContext::Atom_pair_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<RosettaMRParser::Gen_simple_nameContext *> RosettaMRParser::Atom_pair_restraintContext::gen_simple_name() {
  return getRuleContexts<RosettaMRParser::Gen_simple_nameContext>();
}

RosettaMRParser::Gen_simple_nameContext* RosettaMRParser::Atom_pair_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<RosettaMRParser::Gen_simple_nameContext>(i);
}

std::vector<RosettaMRParser::Gen_res_numContext *> RosettaMRParser::Atom_pair_restraintContext::gen_res_num() {
  return getRuleContexts<RosettaMRParser::Gen_res_numContext>();
}

RosettaMRParser::Gen_res_numContext* RosettaMRParser::Atom_pair_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<RosettaMRParser::Gen_res_numContext>(i);
}

RosettaMRParser::Func_type_defContext* RosettaMRParser::Atom_pair_restraintContext::func_type_def() {
  return getRuleContext<RosettaMRParser::Func_type_defContext>(0);
}

tree::TerminalNode* RosettaMRParser::Atom_pair_restraintContext::AtomPair() {
  return getToken(RosettaMRParser::AtomPair, 0);
}

tree::TerminalNode* RosettaMRParser::Atom_pair_restraintContext::NamedAtomPair() {
  return getToken(RosettaMRParser::NamedAtomPair, 0);
}

tree::TerminalNode* RosettaMRParser::Atom_pair_restraintContext::AmbiguousNMRDistance() {
  return getToken(RosettaMRParser::AmbiguousNMRDistance, 0);
}


size_t RosettaMRParser::Atom_pair_restraintContext::getRuleIndex() const {
  return RosettaMRParser::RuleAtom_pair_restraint;
}


std::any RosettaMRParser::Atom_pair_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitAtom_pair_restraint(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Atom_pair_restraintContext* RosettaMRParser::atom_pair_restraint() {
  Atom_pair_restraintContext *_localctx = _tracker.createInstance<Atom_pair_restraintContext>(_ctx, getState());
  enterRule(_localctx, 6, RosettaMRParser::RuleAtom_pair_restraint);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(108);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 518) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(109);
    gen_simple_name();
    setState(110);
    gen_res_num();
    setState(111);
    gen_simple_name();
    setState(112);
    gen_res_num();
    setState(113);
    func_type_def();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Angle_restraintsContext ------------------------------------------------------------------

RosettaMRParser::Angle_restraintsContext::Angle_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<RosettaMRParser::Angle_restraintContext *> RosettaMRParser::Angle_restraintsContext::angle_restraint() {
  return getRuleContexts<RosettaMRParser::Angle_restraintContext>();
}

RosettaMRParser::Angle_restraintContext* RosettaMRParser::Angle_restraintsContext::angle_restraint(size_t i) {
  return getRuleContext<RosettaMRParser::Angle_restraintContext>(i);
}


size_t RosettaMRParser::Angle_restraintsContext::getRuleIndex() const {
  return RosettaMRParser::RuleAngle_restraints;
}


std::any RosettaMRParser::Angle_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitAngle_restraints(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Angle_restraintsContext* RosettaMRParser::angle_restraints() {
  Angle_restraintsContext *_localctx = _tracker.createInstance<Angle_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 8, RosettaMRParser::RuleAngle_restraints);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(116); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(115);
              angle_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(118); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 4, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Angle_restraintContext ------------------------------------------------------------------

RosettaMRParser::Angle_restraintContext::Angle_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<RosettaMRParser::Gen_simple_nameContext *> RosettaMRParser::Angle_restraintContext::gen_simple_name() {
  return getRuleContexts<RosettaMRParser::Gen_simple_nameContext>();
}

RosettaMRParser::Gen_simple_nameContext* RosettaMRParser::Angle_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<RosettaMRParser::Gen_simple_nameContext>(i);
}

std::vector<RosettaMRParser::Gen_res_numContext *> RosettaMRParser::Angle_restraintContext::gen_res_num() {
  return getRuleContexts<RosettaMRParser::Gen_res_numContext>();
}

RosettaMRParser::Gen_res_numContext* RosettaMRParser::Angle_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<RosettaMRParser::Gen_res_numContext>(i);
}

RosettaMRParser::Func_type_defContext* RosettaMRParser::Angle_restraintContext::func_type_def() {
  return getRuleContext<RosettaMRParser::Func_type_defContext>(0);
}

tree::TerminalNode* RosettaMRParser::Angle_restraintContext::Angle() {
  return getToken(RosettaMRParser::Angle, 0);
}

tree::TerminalNode* RosettaMRParser::Angle_restraintContext::NamedAngle() {
  return getToken(RosettaMRParser::NamedAngle, 0);
}


size_t RosettaMRParser::Angle_restraintContext::getRuleIndex() const {
  return RosettaMRParser::RuleAngle_restraint;
}


std::any RosettaMRParser::Angle_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitAngle_restraint(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Angle_restraintContext* RosettaMRParser::angle_restraint() {
  Angle_restraintContext *_localctx = _tracker.createInstance<Angle_restraintContext>(_ctx, getState());
  enterRule(_localctx, 10, RosettaMRParser::RuleAngle_restraint);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(120);
    _la = _input->LA(1);
    if (!(_la == RosettaMRParser::Angle

    || _la == RosettaMRParser::NamedAngle)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(121);
    gen_simple_name();
    setState(122);
    gen_res_num();
    setState(123);
    gen_simple_name();
    setState(124);
    gen_res_num();
    setState(125);
    gen_simple_name();
    setState(126);
    gen_res_num();
    setState(127);
    func_type_def();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Dihedral_restraintsContext ------------------------------------------------------------------

RosettaMRParser::Dihedral_restraintsContext::Dihedral_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<RosettaMRParser::Dihedral_restraintContext *> RosettaMRParser::Dihedral_restraintsContext::dihedral_restraint() {
  return getRuleContexts<RosettaMRParser::Dihedral_restraintContext>();
}

RosettaMRParser::Dihedral_restraintContext* RosettaMRParser::Dihedral_restraintsContext::dihedral_restraint(size_t i) {
  return getRuleContext<RosettaMRParser::Dihedral_restraintContext>(i);
}


size_t RosettaMRParser::Dihedral_restraintsContext::getRuleIndex() const {
  return RosettaMRParser::RuleDihedral_restraints;
}


std::any RosettaMRParser::Dihedral_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_restraints(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Dihedral_restraintsContext* RosettaMRParser::dihedral_restraints() {
  Dihedral_restraintsContext *_localctx = _tracker.createInstance<Dihedral_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 12, RosettaMRParser::RuleDihedral_restraints);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(130); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(129);
              dihedral_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(132); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 5, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Dihedral_restraintContext ------------------------------------------------------------------

RosettaMRParser::Dihedral_restraintContext::Dihedral_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* RosettaMRParser::Dihedral_restraintContext::Dihedral() {
  return getToken(RosettaMRParser::Dihedral, 0);
}

std::vector<RosettaMRParser::Gen_simple_nameContext *> RosettaMRParser::Dihedral_restraintContext::gen_simple_name() {
  return getRuleContexts<RosettaMRParser::Gen_simple_nameContext>();
}

RosettaMRParser::Gen_simple_nameContext* RosettaMRParser::Dihedral_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<RosettaMRParser::Gen_simple_nameContext>(i);
}

std::vector<RosettaMRParser::Gen_res_numContext *> RosettaMRParser::Dihedral_restraintContext::gen_res_num() {
  return getRuleContexts<RosettaMRParser::Gen_res_numContext>();
}

RosettaMRParser::Gen_res_numContext* RosettaMRParser::Dihedral_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<RosettaMRParser::Gen_res_numContext>(i);
}

RosettaMRParser::Func_type_defContext* RosettaMRParser::Dihedral_restraintContext::func_type_def() {
  return getRuleContext<RosettaMRParser::Func_type_defContext>(0);
}


size_t RosettaMRParser::Dihedral_restraintContext::getRuleIndex() const {
  return RosettaMRParser::RuleDihedral_restraint;
}


std::any RosettaMRParser::Dihedral_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_restraint(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Dihedral_restraintContext* RosettaMRParser::dihedral_restraint() {
  Dihedral_restraintContext *_localctx = _tracker.createInstance<Dihedral_restraintContext>(_ctx, getState());
  enterRule(_localctx, 14, RosettaMRParser::RuleDihedral_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(134);
    match(RosettaMRParser::Dihedral);
    setState(135);
    gen_simple_name();
    setState(136);
    gen_res_num();
    setState(137);
    gen_simple_name();
    setState(138);
    gen_res_num();
    setState(139);
    gen_simple_name();
    setState(140);
    gen_res_num();
    setState(141);
    gen_simple_name();
    setState(142);
    gen_res_num();
    setState(143);
    func_type_def();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Dihedral_pair_restraintsContext ------------------------------------------------------------------

RosettaMRParser::Dihedral_pair_restraintsContext::Dihedral_pair_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<RosettaMRParser::Dihedral_pair_restraintContext *> RosettaMRParser::Dihedral_pair_restraintsContext::dihedral_pair_restraint() {
  return getRuleContexts<RosettaMRParser::Dihedral_pair_restraintContext>();
}

RosettaMRParser::Dihedral_pair_restraintContext* RosettaMRParser::Dihedral_pair_restraintsContext::dihedral_pair_restraint(size_t i) {
  return getRuleContext<RosettaMRParser::Dihedral_pair_restraintContext>(i);
}


size_t RosettaMRParser::Dihedral_pair_restraintsContext::getRuleIndex() const {
  return RosettaMRParser::RuleDihedral_pair_restraints;
}


std::any RosettaMRParser::Dihedral_pair_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_pair_restraints(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Dihedral_pair_restraintsContext* RosettaMRParser::dihedral_pair_restraints() {
  Dihedral_pair_restraintsContext *_localctx = _tracker.createInstance<Dihedral_pair_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 16, RosettaMRParser::RuleDihedral_pair_restraints);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(146); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(145);
              dihedral_pair_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(148); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 6, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Dihedral_pair_restraintContext ------------------------------------------------------------------

RosettaMRParser::Dihedral_pair_restraintContext::Dihedral_pair_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* RosettaMRParser::Dihedral_pair_restraintContext::DihedralPair() {
  return getToken(RosettaMRParser::DihedralPair, 0);
}

std::vector<RosettaMRParser::Gen_simple_nameContext *> RosettaMRParser::Dihedral_pair_restraintContext::gen_simple_name() {
  return getRuleContexts<RosettaMRParser::Gen_simple_nameContext>();
}

RosettaMRParser::Gen_simple_nameContext* RosettaMRParser::Dihedral_pair_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<RosettaMRParser::Gen_simple_nameContext>(i);
}

std::vector<RosettaMRParser::Gen_res_numContext *> RosettaMRParser::Dihedral_pair_restraintContext::gen_res_num() {
  return getRuleContexts<RosettaMRParser::Gen_res_numContext>();
}

RosettaMRParser::Gen_res_numContext* RosettaMRParser::Dihedral_pair_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<RosettaMRParser::Gen_res_numContext>(i);
}

RosettaMRParser::Func_type_defContext* RosettaMRParser::Dihedral_pair_restraintContext::func_type_def() {
  return getRuleContext<RosettaMRParser::Func_type_defContext>(0);
}


size_t RosettaMRParser::Dihedral_pair_restraintContext::getRuleIndex() const {
  return RosettaMRParser::RuleDihedral_pair_restraint;
}


std::any RosettaMRParser::Dihedral_pair_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_pair_restraint(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Dihedral_pair_restraintContext* RosettaMRParser::dihedral_pair_restraint() {
  Dihedral_pair_restraintContext *_localctx = _tracker.createInstance<Dihedral_pair_restraintContext>(_ctx, getState());
  enterRule(_localctx, 18, RosettaMRParser::RuleDihedral_pair_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(150);
    match(RosettaMRParser::DihedralPair);
    setState(151);
    gen_simple_name();
    setState(152);
    gen_res_num();
    setState(153);
    gen_simple_name();
    setState(154);
    gen_res_num();
    setState(155);
    gen_simple_name();
    setState(156);
    gen_res_num();
    setState(157);
    gen_simple_name();
    setState(158);
    gen_res_num();
    setState(159);
    gen_simple_name();
    setState(160);
    gen_res_num();
    setState(161);
    gen_simple_name();
    setState(162);
    gen_res_num();
    setState(163);
    gen_simple_name();
    setState(164);
    gen_res_num();
    setState(165);
    gen_simple_name();
    setState(166);
    gen_res_num();
    setState(167);
    func_type_def();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Coordinate_restraintsContext ------------------------------------------------------------------

RosettaMRParser::Coordinate_restraintsContext::Coordinate_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<RosettaMRParser::Coordinate_restraintContext *> RosettaMRParser::Coordinate_restraintsContext::coordinate_restraint() {
  return getRuleContexts<RosettaMRParser::Coordinate_restraintContext>();
}

RosettaMRParser::Coordinate_restraintContext* RosettaMRParser::Coordinate_restraintsContext::coordinate_restraint(size_t i) {
  return getRuleContext<RosettaMRParser::Coordinate_restraintContext>(i);
}


size_t RosettaMRParser::Coordinate_restraintsContext::getRuleIndex() const {
  return RosettaMRParser::RuleCoordinate_restraints;
}


std::any RosettaMRParser::Coordinate_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitCoordinate_restraints(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Coordinate_restraintsContext* RosettaMRParser::coordinate_restraints() {
  Coordinate_restraintsContext *_localctx = _tracker.createInstance<Coordinate_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 20, RosettaMRParser::RuleCoordinate_restraints);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(170); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(169);
              coordinate_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(172); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 7, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Coordinate_restraintContext ------------------------------------------------------------------

RosettaMRParser::Coordinate_restraintContext::Coordinate_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* RosettaMRParser::Coordinate_restraintContext::CoordinateConstraint() {
  return getToken(RosettaMRParser::CoordinateConstraint, 0);
}

std::vector<RosettaMRParser::Gen_simple_nameContext *> RosettaMRParser::Coordinate_restraintContext::gen_simple_name() {
  return getRuleContexts<RosettaMRParser::Gen_simple_nameContext>();
}

RosettaMRParser::Gen_simple_nameContext* RosettaMRParser::Coordinate_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<RosettaMRParser::Gen_simple_nameContext>(i);
}

std::vector<RosettaMRParser::Gen_res_numContext *> RosettaMRParser::Coordinate_restraintContext::gen_res_num() {
  return getRuleContexts<RosettaMRParser::Gen_res_numContext>();
}

RosettaMRParser::Gen_res_numContext* RosettaMRParser::Coordinate_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<RosettaMRParser::Gen_res_numContext>(i);
}

std::vector<RosettaMRParser::NumberContext *> RosettaMRParser::Coordinate_restraintContext::number() {
  return getRuleContexts<RosettaMRParser::NumberContext>();
}

RosettaMRParser::NumberContext* RosettaMRParser::Coordinate_restraintContext::number(size_t i) {
  return getRuleContext<RosettaMRParser::NumberContext>(i);
}

RosettaMRParser::Func_type_defContext* RosettaMRParser::Coordinate_restraintContext::func_type_def() {
  return getRuleContext<RosettaMRParser::Func_type_defContext>(0);
}


size_t RosettaMRParser::Coordinate_restraintContext::getRuleIndex() const {
  return RosettaMRParser::RuleCoordinate_restraint;
}


std::any RosettaMRParser::Coordinate_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitCoordinate_restraint(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Coordinate_restraintContext* RosettaMRParser::coordinate_restraint() {
  Coordinate_restraintContext *_localctx = _tracker.createInstance<Coordinate_restraintContext>(_ctx, getState());
  enterRule(_localctx, 22, RosettaMRParser::RuleCoordinate_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(174);
    match(RosettaMRParser::CoordinateConstraint);
    setState(175);
    gen_simple_name();
    setState(176);
    gen_res_num();
    setState(177);
    gen_simple_name();
    setState(178);
    gen_res_num();
    setState(179);
    number();
    setState(180);
    number();
    setState(181);
    number();
    setState(182);
    func_type_def();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Local_coordinate_restraintsContext ------------------------------------------------------------------

RosettaMRParser::Local_coordinate_restraintsContext::Local_coordinate_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<RosettaMRParser::Local_coordinate_restraintContext *> RosettaMRParser::Local_coordinate_restraintsContext::local_coordinate_restraint() {
  return getRuleContexts<RosettaMRParser::Local_coordinate_restraintContext>();
}

RosettaMRParser::Local_coordinate_restraintContext* RosettaMRParser::Local_coordinate_restraintsContext::local_coordinate_restraint(size_t i) {
  return getRuleContext<RosettaMRParser::Local_coordinate_restraintContext>(i);
}


size_t RosettaMRParser::Local_coordinate_restraintsContext::getRuleIndex() const {
  return RosettaMRParser::RuleLocal_coordinate_restraints;
}


std::any RosettaMRParser::Local_coordinate_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitLocal_coordinate_restraints(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Local_coordinate_restraintsContext* RosettaMRParser::local_coordinate_restraints() {
  Local_coordinate_restraintsContext *_localctx = _tracker.createInstance<Local_coordinate_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 24, RosettaMRParser::RuleLocal_coordinate_restraints);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(185); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(184);
              local_coordinate_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(187); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 8, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Local_coordinate_restraintContext ------------------------------------------------------------------

RosettaMRParser::Local_coordinate_restraintContext::Local_coordinate_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* RosettaMRParser::Local_coordinate_restraintContext::LocalCoordinateConstraint() {
  return getToken(RosettaMRParser::LocalCoordinateConstraint, 0);
}

std::vector<RosettaMRParser::Gen_simple_nameContext *> RosettaMRParser::Local_coordinate_restraintContext::gen_simple_name() {
  return getRuleContexts<RosettaMRParser::Gen_simple_nameContext>();
}

RosettaMRParser::Gen_simple_nameContext* RosettaMRParser::Local_coordinate_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<RosettaMRParser::Gen_simple_nameContext>(i);
}

RosettaMRParser::Gen_res_numContext* RosettaMRParser::Local_coordinate_restraintContext::gen_res_num() {
  return getRuleContext<RosettaMRParser::Gen_res_numContext>(0);
}

tree::TerminalNode* RosettaMRParser::Local_coordinate_restraintContext::Integer() {
  return getToken(RosettaMRParser::Integer, 0);
}

std::vector<RosettaMRParser::NumberContext *> RosettaMRParser::Local_coordinate_restraintContext::number() {
  return getRuleContexts<RosettaMRParser::NumberContext>();
}

RosettaMRParser::NumberContext* RosettaMRParser::Local_coordinate_restraintContext::number(size_t i) {
  return getRuleContext<RosettaMRParser::NumberContext>(i);
}

RosettaMRParser::Func_type_defContext* RosettaMRParser::Local_coordinate_restraintContext::func_type_def() {
  return getRuleContext<RosettaMRParser::Func_type_defContext>(0);
}


size_t RosettaMRParser::Local_coordinate_restraintContext::getRuleIndex() const {
  return RosettaMRParser::RuleLocal_coordinate_restraint;
}


std::any RosettaMRParser::Local_coordinate_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitLocal_coordinate_restraint(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Local_coordinate_restraintContext* RosettaMRParser::local_coordinate_restraint() {
  Local_coordinate_restraintContext *_localctx = _tracker.createInstance<Local_coordinate_restraintContext>(_ctx, getState());
  enterRule(_localctx, 26, RosettaMRParser::RuleLocal_coordinate_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(189);
    match(RosettaMRParser::LocalCoordinateConstraint);
    setState(190);
    gen_simple_name();
    setState(191);
    gen_res_num();
    setState(192);
    gen_simple_name();
    setState(193);
    gen_simple_name();
    setState(194);
    gen_simple_name();
    setState(195);
    match(RosettaMRParser::Integer);
    setState(196);
    number();
    setState(197);
    number();
    setState(198);
    number();
    setState(199);
    func_type_def();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Site_restraintsContext ------------------------------------------------------------------

RosettaMRParser::Site_restraintsContext::Site_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<RosettaMRParser::Site_restraintContext *> RosettaMRParser::Site_restraintsContext::site_restraint() {
  return getRuleContexts<RosettaMRParser::Site_restraintContext>();
}

RosettaMRParser::Site_restraintContext* RosettaMRParser::Site_restraintsContext::site_restraint(size_t i) {
  return getRuleContext<RosettaMRParser::Site_restraintContext>(i);
}


size_t RosettaMRParser::Site_restraintsContext::getRuleIndex() const {
  return RosettaMRParser::RuleSite_restraints;
}


std::any RosettaMRParser::Site_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitSite_restraints(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Site_restraintsContext* RosettaMRParser::site_restraints() {
  Site_restraintsContext *_localctx = _tracker.createInstance<Site_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 28, RosettaMRParser::RuleSite_restraints);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(202); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(201);
              site_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(204); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 9, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Site_restraintContext ------------------------------------------------------------------

RosettaMRParser::Site_restraintContext::Site_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* RosettaMRParser::Site_restraintContext::SiteConstraint() {
  return getToken(RosettaMRParser::SiteConstraint, 0);
}

RosettaMRParser::Gen_simple_nameContext* RosettaMRParser::Site_restraintContext::gen_simple_name() {
  return getRuleContext<RosettaMRParser::Gen_simple_nameContext>(0);
}

RosettaMRParser::Gen_res_numContext* RosettaMRParser::Site_restraintContext::gen_res_num() {
  return getRuleContext<RosettaMRParser::Gen_res_numContext>(0);
}

tree::TerminalNode* RosettaMRParser::Site_restraintContext::Simple_name() {
  return getToken(RosettaMRParser::Simple_name, 0);
}

RosettaMRParser::Func_type_defContext* RosettaMRParser::Site_restraintContext::func_type_def() {
  return getRuleContext<RosettaMRParser::Func_type_defContext>(0);
}


size_t RosettaMRParser::Site_restraintContext::getRuleIndex() const {
  return RosettaMRParser::RuleSite_restraint;
}


std::any RosettaMRParser::Site_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitSite_restraint(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Site_restraintContext* RosettaMRParser::site_restraint() {
  Site_restraintContext *_localctx = _tracker.createInstance<Site_restraintContext>(_ctx, getState());
  enterRule(_localctx, 30, RosettaMRParser::RuleSite_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(206);
    match(RosettaMRParser::SiteConstraint);
    setState(207);
    gen_simple_name();
    setState(208);
    gen_res_num();
    setState(209);
    match(RosettaMRParser::Simple_name);
    setState(210);
    func_type_def();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Site_residues_restraintsContext ------------------------------------------------------------------

RosettaMRParser::Site_residues_restraintsContext::Site_residues_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<RosettaMRParser::Site_residues_restraintContext *> RosettaMRParser::Site_residues_restraintsContext::site_residues_restraint() {
  return getRuleContexts<RosettaMRParser::Site_residues_restraintContext>();
}

RosettaMRParser::Site_residues_restraintContext* RosettaMRParser::Site_residues_restraintsContext::site_residues_restraint(size_t i) {
  return getRuleContext<RosettaMRParser::Site_residues_restraintContext>(i);
}


size_t RosettaMRParser::Site_residues_restraintsContext::getRuleIndex() const {
  return RosettaMRParser::RuleSite_residues_restraints;
}


std::any RosettaMRParser::Site_residues_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitSite_residues_restraints(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Site_residues_restraintsContext* RosettaMRParser::site_residues_restraints() {
  Site_residues_restraintsContext *_localctx = _tracker.createInstance<Site_residues_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 32, RosettaMRParser::RuleSite_residues_restraints);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(213); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(212);
              site_residues_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(215); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 10, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Site_residues_restraintContext ------------------------------------------------------------------

RosettaMRParser::Site_residues_restraintContext::Site_residues_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* RosettaMRParser::Site_residues_restraintContext::SiteConstraintResidues() {
  return getToken(RosettaMRParser::SiteConstraintResidues, 0);
}

RosettaMRParser::Gen_res_numContext* RosettaMRParser::Site_residues_restraintContext::gen_res_num() {
  return getRuleContext<RosettaMRParser::Gen_res_numContext>(0);
}

RosettaMRParser::Gen_simple_nameContext* RosettaMRParser::Site_residues_restraintContext::gen_simple_name() {
  return getRuleContext<RosettaMRParser::Gen_simple_nameContext>(0);
}

std::vector<tree::TerminalNode *> RosettaMRParser::Site_residues_restraintContext::Integer() {
  return getTokens(RosettaMRParser::Integer);
}

tree::TerminalNode* RosettaMRParser::Site_residues_restraintContext::Integer(size_t i) {
  return getToken(RosettaMRParser::Integer, i);
}

RosettaMRParser::Func_type_defContext* RosettaMRParser::Site_residues_restraintContext::func_type_def() {
  return getRuleContext<RosettaMRParser::Func_type_defContext>(0);
}


size_t RosettaMRParser::Site_residues_restraintContext::getRuleIndex() const {
  return RosettaMRParser::RuleSite_residues_restraint;
}


std::any RosettaMRParser::Site_residues_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitSite_residues_restraint(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Site_residues_restraintContext* RosettaMRParser::site_residues_restraint() {
  Site_residues_restraintContext *_localctx = _tracker.createInstance<Site_residues_restraintContext>(_ctx, getState());
  enterRule(_localctx, 34, RosettaMRParser::RuleSite_residues_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(217);
    match(RosettaMRParser::SiteConstraintResidues);
    setState(218);
    gen_res_num();
    setState(219);
    gen_simple_name();
    setState(220);
    match(RosettaMRParser::Integer);
    setState(221);
    match(RosettaMRParser::Integer);
    setState(222);
    func_type_def();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Min_residue_atomic_distance_restraintsContext ------------------------------------------------------------------

RosettaMRParser::Min_residue_atomic_distance_restraintsContext::Min_residue_atomic_distance_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<RosettaMRParser::Min_residue_atomic_distance_restraintContext *> RosettaMRParser::Min_residue_atomic_distance_restraintsContext::min_residue_atomic_distance_restraint() {
  return getRuleContexts<RosettaMRParser::Min_residue_atomic_distance_restraintContext>();
}

RosettaMRParser::Min_residue_atomic_distance_restraintContext* RosettaMRParser::Min_residue_atomic_distance_restraintsContext::min_residue_atomic_distance_restraint(size_t i) {
  return getRuleContext<RosettaMRParser::Min_residue_atomic_distance_restraintContext>(i);
}


size_t RosettaMRParser::Min_residue_atomic_distance_restraintsContext::getRuleIndex() const {
  return RosettaMRParser::RuleMin_residue_atomic_distance_restraints;
}


std::any RosettaMRParser::Min_residue_atomic_distance_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitMin_residue_atomic_distance_restraints(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Min_residue_atomic_distance_restraintsContext* RosettaMRParser::min_residue_atomic_distance_restraints() {
  Min_residue_atomic_distance_restraintsContext *_localctx = _tracker.createInstance<Min_residue_atomic_distance_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 36, RosettaMRParser::RuleMin_residue_atomic_distance_restraints);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(225); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(224);
              min_residue_atomic_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(227); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 11, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Min_residue_atomic_distance_restraintContext ------------------------------------------------------------------

RosettaMRParser::Min_residue_atomic_distance_restraintContext::Min_residue_atomic_distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* RosettaMRParser::Min_residue_atomic_distance_restraintContext::MinResidueAtomicDistance() {
  return getToken(RosettaMRParser::MinResidueAtomicDistance, 0);
}

std::vector<RosettaMRParser::Gen_res_numContext *> RosettaMRParser::Min_residue_atomic_distance_restraintContext::gen_res_num() {
  return getRuleContexts<RosettaMRParser::Gen_res_numContext>();
}

RosettaMRParser::Gen_res_numContext* RosettaMRParser::Min_residue_atomic_distance_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<RosettaMRParser::Gen_res_numContext>(i);
}

RosettaMRParser::NumberContext* RosettaMRParser::Min_residue_atomic_distance_restraintContext::number() {
  return getRuleContext<RosettaMRParser::NumberContext>(0);
}


size_t RosettaMRParser::Min_residue_atomic_distance_restraintContext::getRuleIndex() const {
  return RosettaMRParser::RuleMin_residue_atomic_distance_restraint;
}


std::any RosettaMRParser::Min_residue_atomic_distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitMin_residue_atomic_distance_restraint(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Min_residue_atomic_distance_restraintContext* RosettaMRParser::min_residue_atomic_distance_restraint() {
  Min_residue_atomic_distance_restraintContext *_localctx = _tracker.createInstance<Min_residue_atomic_distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 38, RosettaMRParser::RuleMin_residue_atomic_distance_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(229);
    match(RosettaMRParser::MinResidueAtomicDistance);
    setState(230);
    gen_res_num();
    setState(231);
    gen_res_num();
    setState(232);
    number();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Big_bin_restraintsContext ------------------------------------------------------------------

RosettaMRParser::Big_bin_restraintsContext::Big_bin_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<RosettaMRParser::Big_bin_restraintContext *> RosettaMRParser::Big_bin_restraintsContext::big_bin_restraint() {
  return getRuleContexts<RosettaMRParser::Big_bin_restraintContext>();
}

RosettaMRParser::Big_bin_restraintContext* RosettaMRParser::Big_bin_restraintsContext::big_bin_restraint(size_t i) {
  return getRuleContext<RosettaMRParser::Big_bin_restraintContext>(i);
}


size_t RosettaMRParser::Big_bin_restraintsContext::getRuleIndex() const {
  return RosettaMRParser::RuleBig_bin_restraints;
}


std::any RosettaMRParser::Big_bin_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitBig_bin_restraints(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Big_bin_restraintsContext* RosettaMRParser::big_bin_restraints() {
  Big_bin_restraintsContext *_localctx = _tracker.createInstance<Big_bin_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 40, RosettaMRParser::RuleBig_bin_restraints);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(235); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(234);
              big_bin_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(237); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 12, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Big_bin_restraintContext ------------------------------------------------------------------

RosettaMRParser::Big_bin_restraintContext::Big_bin_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* RosettaMRParser::Big_bin_restraintContext::BigBin() {
  return getToken(RosettaMRParser::BigBin, 0);
}

RosettaMRParser::Gen_res_numContext* RosettaMRParser::Big_bin_restraintContext::gen_res_num() {
  return getRuleContext<RosettaMRParser::Gen_res_numContext>(0);
}

tree::TerminalNode* RosettaMRParser::Big_bin_restraintContext::Simple_name() {
  return getToken(RosettaMRParser::Simple_name, 0);
}

RosettaMRParser::NumberContext* RosettaMRParser::Big_bin_restraintContext::number() {
  return getRuleContext<RosettaMRParser::NumberContext>(0);
}


size_t RosettaMRParser::Big_bin_restraintContext::getRuleIndex() const {
  return RosettaMRParser::RuleBig_bin_restraint;
}


std::any RosettaMRParser::Big_bin_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitBig_bin_restraint(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Big_bin_restraintContext* RosettaMRParser::big_bin_restraint() {
  Big_bin_restraintContext *_localctx = _tracker.createInstance<Big_bin_restraintContext>(_ctx, getState());
  enterRule(_localctx, 42, RosettaMRParser::RuleBig_bin_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(239);
    match(RosettaMRParser::BigBin);
    setState(240);
    gen_res_num();
    setState(241);
    match(RosettaMRParser::Simple_name);
    setState(242);
    number();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Nested_restraintsContext ------------------------------------------------------------------

RosettaMRParser::Nested_restraintsContext::Nested_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<RosettaMRParser::Nested_restraintContext *> RosettaMRParser::Nested_restraintsContext::nested_restraint() {
  return getRuleContexts<RosettaMRParser::Nested_restraintContext>();
}

RosettaMRParser::Nested_restraintContext* RosettaMRParser::Nested_restraintsContext::nested_restraint(size_t i) {
  return getRuleContext<RosettaMRParser::Nested_restraintContext>(i);
}


size_t RosettaMRParser::Nested_restraintsContext::getRuleIndex() const {
  return RosettaMRParser::RuleNested_restraints;
}


std::any RosettaMRParser::Nested_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitNested_restraints(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Nested_restraintsContext* RosettaMRParser::nested_restraints() {
  Nested_restraintsContext *_localctx = _tracker.createInstance<Nested_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 44, RosettaMRParser::RuleNested_restraints);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(245); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(244);
              nested_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(247); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 13, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Nested_restraintContext ------------------------------------------------------------------

RosettaMRParser::Nested_restraintContext::Nested_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* RosettaMRParser::Nested_restraintContext::END() {
  return getToken(RosettaMRParser::END, 0);
}

tree::TerminalNode* RosettaMRParser::Nested_restraintContext::MultiConstraint() {
  return getToken(RosettaMRParser::MultiConstraint, 0);
}

tree::TerminalNode* RosettaMRParser::Nested_restraintContext::AmbiguousConstraint() {
  return getToken(RosettaMRParser::AmbiguousConstraint, 0);
}

std::vector<RosettaMRParser::Any_restraintContext *> RosettaMRParser::Nested_restraintContext::any_restraint() {
  return getRuleContexts<RosettaMRParser::Any_restraintContext>();
}

RosettaMRParser::Any_restraintContext* RosettaMRParser::Nested_restraintContext::any_restraint(size_t i) {
  return getRuleContext<RosettaMRParser::Any_restraintContext>(i);
}

std::vector<RosettaMRParser::Nested_restraintContext *> RosettaMRParser::Nested_restraintContext::nested_restraint() {
  return getRuleContexts<RosettaMRParser::Nested_restraintContext>();
}

RosettaMRParser::Nested_restraintContext* RosettaMRParser::Nested_restraintContext::nested_restraint(size_t i) {
  return getRuleContext<RosettaMRParser::Nested_restraintContext>(i);
}

tree::TerminalNode* RosettaMRParser::Nested_restraintContext::KofNConstraint() {
  return getToken(RosettaMRParser::KofNConstraint, 0);
}

tree::TerminalNode* RosettaMRParser::Nested_restraintContext::Integer() {
  return getToken(RosettaMRParser::Integer, 0);
}


size_t RosettaMRParser::Nested_restraintContext::getRuleIndex() const {
  return RosettaMRParser::RuleNested_restraint;
}


std::any RosettaMRParser::Nested_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitNested_restraint(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Nested_restraintContext* RosettaMRParser::nested_restraint() {
  Nested_restraintContext *_localctx = _tracker.createInstance<Nested_restraintContext>(_ctx, getState());
  enterRule(_localctx, 46, RosettaMRParser::RuleNested_restraint);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(253);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case RosettaMRParser::MultiConstraint: {
        setState(249);
        match(RosettaMRParser::MultiConstraint);
        break;
      }

      case RosettaMRParser::AmbiguousConstraint: {
        setState(250);
        match(RosettaMRParser::AmbiguousConstraint);
        break;
      }

      case RosettaMRParser::KofNConstraint: {
        setState(251);
        match(RosettaMRParser::KofNConstraint);
        setState(252);
        match(RosettaMRParser::Integer);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(257); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(257);
      _errHandler->sync(this);
      switch (_input->LA(1)) {
        case RosettaMRParser::AtomPair:
        case RosettaMRParser::NamedAtomPair:
        case RosettaMRParser::Angle:
        case RosettaMRParser::NamedAngle:
        case RosettaMRParser::Dihedral:
        case RosettaMRParser::DihedralPair:
        case RosettaMRParser::CoordinateConstraint:
        case RosettaMRParser::LocalCoordinateConstraint:
        case RosettaMRParser::AmbiguousNMRDistance:
        case RosettaMRParser::SiteConstraint:
        case RosettaMRParser::SiteConstraintResidues:
        case RosettaMRParser::MinResidueAtomicDistance:
        case RosettaMRParser::BigBin: {
          setState(255);
          any_restraint();
          break;
        }

        case RosettaMRParser::MultiConstraint:
        case RosettaMRParser::AmbiguousConstraint:
        case RosettaMRParser::KofNConstraint: {
          setState(256);
          nested_restraint();
          break;
        }

      default:
        throw NoViableAltException(this);
      }
      setState(259); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 131070) != 0));
    setState(261);
    match(RosettaMRParser::END);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Any_restraintContext ------------------------------------------------------------------

RosettaMRParser::Any_restraintContext::Any_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

RosettaMRParser::Atom_pair_restraintContext* RosettaMRParser::Any_restraintContext::atom_pair_restraint() {
  return getRuleContext<RosettaMRParser::Atom_pair_restraintContext>(0);
}

RosettaMRParser::Angle_restraintContext* RosettaMRParser::Any_restraintContext::angle_restraint() {
  return getRuleContext<RosettaMRParser::Angle_restraintContext>(0);
}

RosettaMRParser::Dihedral_restraintContext* RosettaMRParser::Any_restraintContext::dihedral_restraint() {
  return getRuleContext<RosettaMRParser::Dihedral_restraintContext>(0);
}

RosettaMRParser::Dihedral_pair_restraintContext* RosettaMRParser::Any_restraintContext::dihedral_pair_restraint() {
  return getRuleContext<RosettaMRParser::Dihedral_pair_restraintContext>(0);
}

RosettaMRParser::Coordinate_restraintContext* RosettaMRParser::Any_restraintContext::coordinate_restraint() {
  return getRuleContext<RosettaMRParser::Coordinate_restraintContext>(0);
}

RosettaMRParser::Local_coordinate_restraintContext* RosettaMRParser::Any_restraintContext::local_coordinate_restraint() {
  return getRuleContext<RosettaMRParser::Local_coordinate_restraintContext>(0);
}

RosettaMRParser::Site_restraintContext* RosettaMRParser::Any_restraintContext::site_restraint() {
  return getRuleContext<RosettaMRParser::Site_restraintContext>(0);
}

RosettaMRParser::Site_residues_restraintContext* RosettaMRParser::Any_restraintContext::site_residues_restraint() {
  return getRuleContext<RosettaMRParser::Site_residues_restraintContext>(0);
}

RosettaMRParser::Min_residue_atomic_distance_restraintContext* RosettaMRParser::Any_restraintContext::min_residue_atomic_distance_restraint() {
  return getRuleContext<RosettaMRParser::Min_residue_atomic_distance_restraintContext>(0);
}

RosettaMRParser::Big_bin_restraintContext* RosettaMRParser::Any_restraintContext::big_bin_restraint() {
  return getRuleContext<RosettaMRParser::Big_bin_restraintContext>(0);
}


size_t RosettaMRParser::Any_restraintContext::getRuleIndex() const {
  return RosettaMRParser::RuleAny_restraint;
}


std::any RosettaMRParser::Any_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitAny_restraint(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Any_restraintContext* RosettaMRParser::any_restraint() {
  Any_restraintContext *_localctx = _tracker.createInstance<Any_restraintContext>(_ctx, getState());
  enterRule(_localctx, 48, RosettaMRParser::RuleAny_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(273);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case RosettaMRParser::AtomPair:
      case RosettaMRParser::NamedAtomPair:
      case RosettaMRParser::AmbiguousNMRDistance: {
        enterOuterAlt(_localctx, 1);
        setState(263);
        atom_pair_restraint();
        break;
      }

      case RosettaMRParser::Angle:
      case RosettaMRParser::NamedAngle: {
        enterOuterAlt(_localctx, 2);
        setState(264);
        angle_restraint();
        break;
      }

      case RosettaMRParser::Dihedral: {
        enterOuterAlt(_localctx, 3);
        setState(265);
        dihedral_restraint();
        break;
      }

      case RosettaMRParser::DihedralPair: {
        enterOuterAlt(_localctx, 4);
        setState(266);
        dihedral_pair_restraint();
        break;
      }

      case RosettaMRParser::CoordinateConstraint: {
        enterOuterAlt(_localctx, 5);
        setState(267);
        coordinate_restraint();
        break;
      }

      case RosettaMRParser::LocalCoordinateConstraint: {
        enterOuterAlt(_localctx, 6);
        setState(268);
        local_coordinate_restraint();
        break;
      }

      case RosettaMRParser::SiteConstraint: {
        enterOuterAlt(_localctx, 7);
        setState(269);
        site_restraint();
        break;
      }

      case RosettaMRParser::SiteConstraintResidues: {
        enterOuterAlt(_localctx, 8);
        setState(270);
        site_residues_restraint();
        break;
      }

      case RosettaMRParser::MinResidueAtomicDistance: {
        enterOuterAlt(_localctx, 9);
        setState(271);
        min_residue_atomic_distance_restraint();
        break;
      }

      case RosettaMRParser::BigBin: {
        enterOuterAlt(_localctx, 10);
        setState(272);
        big_bin_restraint();
        break;
      }

    default:
      throw NoViableAltException(this);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Func_type_defContext ------------------------------------------------------------------

RosettaMRParser::Func_type_defContext::Func_type_defContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<RosettaMRParser::Number_fContext *> RosettaMRParser::Func_type_defContext::number_f() {
  return getRuleContexts<RosettaMRParser::Number_fContext>();
}

RosettaMRParser::Number_fContext* RosettaMRParser::Func_type_defContext::number_f(size_t i) {
  return getRuleContext<RosettaMRParser::Number_fContext>(i);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::BOUNDED() {
  return getToken(RosettaMRParser::BOUNDED, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::PERIODICBOUNDED() {
  return getToken(RosettaMRParser::PERIODICBOUNDED, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::OFFSETPERIODICBOUNDED() {
  return getToken(RosettaMRParser::OFFSETPERIODICBOUNDED, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::CIRCULARSPLINE() {
  return getToken(RosettaMRParser::CIRCULARSPLINE, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::GAUSSIANFUNC() {
  return getToken(RosettaMRParser::GAUSSIANFUNC, 0);
}

std::vector<tree::TerminalNode *> RosettaMRParser::Func_type_defContext::Simple_name() {
  return getTokens(RosettaMRParser::Simple_name);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::Simple_name(size_t i) {
  return getToken(RosettaMRParser::Simple_name, i);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::SOGFUNC() {
  return getToken(RosettaMRParser::SOGFUNC, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::Integer() {
  return getToken(RosettaMRParser::Integer, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::CONSTANTFUNC() {
  return getToken(RosettaMRParser::CONSTANTFUNC, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::IDENTITY() {
  return getToken(RosettaMRParser::IDENTITY, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::SCALARWEIGHTEDFUNC() {
  return getToken(RosettaMRParser::SCALARWEIGHTEDFUNC, 0);
}

std::vector<RosettaMRParser::Func_type_defContext *> RosettaMRParser::Func_type_defContext::func_type_def() {
  return getRuleContexts<RosettaMRParser::Func_type_defContext>();
}

RosettaMRParser::Func_type_defContext* RosettaMRParser::Func_type_defContext::func_type_def(size_t i) {
  return getRuleContext<RosettaMRParser::Func_type_defContext>(i);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::SUMFUNC() {
  return getToken(RosettaMRParser::SUMFUNC, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::SPLINE() {
  return getToken(RosettaMRParser::SPLINE, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::FADE() {
  return getToken(RosettaMRParser::FADE, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::SQUARE_WELL2() {
  return getToken(RosettaMRParser::SQUARE_WELL2, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::ETABLE() {
  return getToken(RosettaMRParser::ETABLE, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::USOG() {
  return getToken(RosettaMRParser::USOG, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::SOG() {
  return getToken(RosettaMRParser::SOG, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::CIRCULARHARMONIC() {
  return getToken(RosettaMRParser::CIRCULARHARMONIC, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::HARMONIC() {
  return getToken(RosettaMRParser::HARMONIC, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::SIGMOID() {
  return getToken(RosettaMRParser::SIGMOID, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::SQUARE_WELL() {
  return getToken(RosettaMRParser::SQUARE_WELL, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::AMBERPERIODIC() {
  return getToken(RosettaMRParser::AMBERPERIODIC, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::CHARMMPERIODIC() {
  return getToken(RosettaMRParser::CHARMMPERIODIC, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::FLAT_HARMONIC() {
  return getToken(RosettaMRParser::FLAT_HARMONIC, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::TOPOUT() {
  return getToken(RosettaMRParser::TOPOUT, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::CIRCULARSIGMOIDAL() {
  return getToken(RosettaMRParser::CIRCULARSIGMOIDAL, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::LINEAR_PENALTY() {
  return getToken(RosettaMRParser::LINEAR_PENALTY, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::MIXTUREFUNC() {
  return getToken(RosettaMRParser::MIXTUREFUNC, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::KARPLUS() {
  return getToken(RosettaMRParser::KARPLUS, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::SOEDINGFUNC() {
  return getToken(RosettaMRParser::SOEDINGFUNC, 0);
}

RosettaMRParser::CommentContext* RosettaMRParser::Func_type_defContext::comment() {
  return getRuleContext<RosettaMRParser::CommentContext>(0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::NONE() {
  return getToken(RosettaMRParser::NONE, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::WEIGHT() {
  return getToken(RosettaMRParser::WEIGHT, 0);
}

tree::TerminalNode* RosettaMRParser::Func_type_defContext::DEGREES() {
  return getToken(RosettaMRParser::DEGREES, 0);
}


size_t RosettaMRParser::Func_type_defContext::getRuleIndex() const {
  return RosettaMRParser::RuleFunc_type_def;
}


std::any RosettaMRParser::Func_type_defContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitFunc_type_def(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Func_type_defContext* RosettaMRParser::func_type_def() {
  Func_type_defContext *_localctx = _tracker.createInstance<Func_type_defContext>(_ctx, getState());
  enterRule(_localctx, 50, RosettaMRParser::RuleFunc_type_def);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(452);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case RosettaMRParser::CIRCULARHARMONIC:
      case RosettaMRParser::HARMONIC:
      case RosettaMRParser::SIGMOID:
      case RosettaMRParser::SQUARE_WELL: {
        setState(275);
        _la = _input->LA(1);
        if (!((((_la & ~ 0x3fULL) == 0) &&
          ((1ULL << _la) & 1649301258240) != 0))) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(276);
        number_f();
        setState(277);
        number_f();
        break;
      }

      case RosettaMRParser::BOUNDED: {
        setState(279);
        match(RosettaMRParser::BOUNDED);
        setState(280);
        number_f();
        setState(281);
        number_f();
        setState(282);
        number_f();
        setState(284);
        _errHandler->sync(this);

        switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 18, _ctx)) {
        case 1: {
          setState(283);
          number_f();
          break;
        }

        default:
          break;
        }
        setState(290);
        _errHandler->sync(this);
        alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 20, _ctx);
        while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
          if (alt == 1) {
            setState(288);
            _errHandler->sync(this);
            switch (_input->LA(1)) {
              case RosettaMRParser::Simple_name: {
                setState(286);
                match(RosettaMRParser::Simple_name);
                break;
              }

              case RosettaMRParser::Integer:
              case RosettaMRParser::Float: {
                setState(287);
                number_f();
                break;
              }

            default:
              throw NoViableAltException(this);
            } 
          }
          setState(292);
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 20, _ctx);
        }
        break;
      }

      case RosettaMRParser::PERIODICBOUNDED: {
        setState(293);
        match(RosettaMRParser::PERIODICBOUNDED);
        setState(294);
        number_f();
        setState(295);
        number_f();
        setState(296);
        number_f();
        setState(297);
        number_f();
        setState(299);
        _errHandler->sync(this);

        switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 21, _ctx)) {
        case 1: {
          setState(298);
          number_f();
          break;
        }

        default:
          break;
        }
        setState(305);
        _errHandler->sync(this);
        alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 23, _ctx);
        while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
          if (alt == 1) {
            setState(303);
            _errHandler->sync(this);
            switch (_input->LA(1)) {
              case RosettaMRParser::Simple_name: {
                setState(301);
                match(RosettaMRParser::Simple_name);
                break;
              }

              case RosettaMRParser::Integer:
              case RosettaMRParser::Float: {
                setState(302);
                number_f();
                break;
              }

            default:
              throw NoViableAltException(this);
            } 
          }
          setState(307);
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 23, _ctx);
        }
        break;
      }

      case RosettaMRParser::OFFSETPERIODICBOUNDED: {
        setState(308);
        match(RosettaMRParser::OFFSETPERIODICBOUNDED);
        setState(309);
        number_f();
        setState(310);
        number_f();
        setState(311);
        number_f();
        setState(312);
        number_f();
        setState(313);
        number_f();
        setState(315);
        _errHandler->sync(this);

        switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 24, _ctx)) {
        case 1: {
          setState(314);
          number_f();
          break;
        }

        default:
          break;
        }
        setState(321);
        _errHandler->sync(this);
        alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 26, _ctx);
        while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
          if (alt == 1) {
            setState(319);
            _errHandler->sync(this);
            switch (_input->LA(1)) {
              case RosettaMRParser::Simple_name: {
                setState(317);
                match(RosettaMRParser::Simple_name);
                break;
              }

              case RosettaMRParser::Integer:
              case RosettaMRParser::Float: {
                setState(318);
                number_f();
                break;
              }

            default:
              throw NoViableAltException(this);
            } 
          }
          setState(323);
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 26, _ctx);
        }
        break;
      }

      case RosettaMRParser::AMBERPERIODIC:
      case RosettaMRParser::CHARMMPERIODIC:
      case RosettaMRParser::FLAT_HARMONIC:
      case RosettaMRParser::TOPOUT: {
        setState(324);
        _la = _input->LA(1);
        if (!((((_la & ~ 0x3fULL) == 0) &&
          ((1ULL << _la) & 70368817577984) != 0))) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(325);
        number_f();
        setState(326);
        number_f();
        setState(327);
        number_f();
        break;
      }

      case RosettaMRParser::CIRCULARSIGMOIDAL:
      case RosettaMRParser::LINEAR_PENALTY: {
        setState(329);
        _la = _input->LA(1);
        if (!(_la == RosettaMRParser::CIRCULARSIGMOIDAL

        || _la == RosettaMRParser::LINEAR_PENALTY)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(330);
        number_f();
        setState(331);
        number_f();
        setState(332);
        number_f();
        setState(333);
        number_f();
        break;
      }

      case RosettaMRParser::CIRCULARSPLINE: {
        setState(335);
        match(RosettaMRParser::CIRCULARSPLINE);
        setState(337); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(336);
                  number_f();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(339); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 27, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case RosettaMRParser::GAUSSIANFUNC: {
        setState(341);
        match(RosettaMRParser::GAUSSIANFUNC);
        setState(342);
        number_f();
        setState(343);
        number_f();
        setState(344);
        match(RosettaMRParser::Simple_name);
        setState(347);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == RosettaMRParser::WEIGHT) {
          setState(345);
          match(RosettaMRParser::WEIGHT);
          setState(346);
          number_f();
        }
        break;
      }

      case RosettaMRParser::SOGFUNC: {
        setState(349);
        match(RosettaMRParser::SOGFUNC);
        setState(350);
        match(RosettaMRParser::Integer);
        setState(355); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(351);
                  number_f();
                  setState(352);
                  number_f();
                  setState(353);
                  number_f();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(357); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 29, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case RosettaMRParser::MIXTUREFUNC:
      case RosettaMRParser::KARPLUS:
      case RosettaMRParser::SOEDINGFUNC: {
        setState(359);
        _la = _input->LA(1);
        if (!((((_la & ~ 0x3fULL) == 0) &&
          ((1ULL << _la) & 52778705616896) != 0))) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(360);
        number_f();
        setState(361);
        number_f();
        setState(362);
        number_f();
        setState(363);
        number_f();
        setState(364);
        number_f();
        setState(365);
        number_f();
        break;
      }

      case RosettaMRParser::CONSTANTFUNC: {
        setState(367);
        match(RosettaMRParser::CONSTANTFUNC);
        setState(368);
        number_f();
        break;
      }

      case RosettaMRParser::IDENTITY: {
        setState(369);
        match(RosettaMRParser::IDENTITY);
        break;
      }

      case RosettaMRParser::SCALARWEIGHTEDFUNC: {
        setState(370);
        match(RosettaMRParser::SCALARWEIGHTEDFUNC);
        setState(371);
        number_f();
        setState(372);
        func_type_def();
        break;
      }

      case RosettaMRParser::SUMFUNC: {
        setState(374);
        match(RosettaMRParser::SUMFUNC);
        setState(375);
        match(RosettaMRParser::Integer);
        setState(377); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(376);
                  func_type_def();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(379); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 30, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case RosettaMRParser::SPLINE: {
        setState(381);
        match(RosettaMRParser::SPLINE);
        setState(382);
        match(RosettaMRParser::Simple_name);
        setState(402);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case RosettaMRParser::Integer:
          case RosettaMRParser::Float: {
            setState(383);
            number_f();
            setState(384);
            number_f();
            setState(385);
            number_f();
            break;
          }

          case RosettaMRParser::NONE: {
            setState(387);
            match(RosettaMRParser::NONE);
            setState(388);
            number_f();
            setState(389);
            number_f();
            setState(390);
            number_f();
            setState(398); 
            _errHandler->sync(this);
            _la = _input->LA(1);
            do {
              setState(391);
              match(RosettaMRParser::Simple_name);
              setState(395);
              _errHandler->sync(this);
              alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 31, _ctx);
              while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
                if (alt == 1) {
                  setState(392);
                  number_f(); 
                }
                setState(397);
                _errHandler->sync(this);
                alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 31, _ctx);
              }
              setState(400); 
              _errHandler->sync(this);
              _la = _input->LA(1);
            } while (_la == RosettaMRParser::Simple_name);
            break;
          }

        default:
          throw NoViableAltException(this);
        }
        break;
      }

      case RosettaMRParser::FADE: {
        setState(404);
        match(RosettaMRParser::FADE);
        setState(405);
        number_f();
        setState(406);
        number_f();
        setState(407);
        number_f();
        setState(408);
        number_f();
        setState(410);
        _errHandler->sync(this);

        switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 34, _ctx)) {
        case 1: {
          setState(409);
          number_f();
          break;
        }

        default:
          break;
        }
        break;
      }

      case RosettaMRParser::SQUARE_WELL2: {
        setState(412);
        match(RosettaMRParser::SQUARE_WELL2);
        setState(413);
        number_f();
        setState(414);
        number_f();
        setState(415);
        number_f();
        setState(417);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == RosettaMRParser::DEGREES) {
          setState(416);
          match(RosettaMRParser::DEGREES);
        }
        break;
      }

      case RosettaMRParser::ETABLE: {
        setState(419);
        match(RosettaMRParser::ETABLE);
        setState(420);
        number_f();
        setState(421);
        number_f();
        setState(425);
        _errHandler->sync(this);
        alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 36, _ctx);
        while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
          if (alt == 1) {
            setState(422);
            number_f(); 
          }
          setState(427);
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 36, _ctx);
        }
        break;
      }

      case RosettaMRParser::USOG: {
        setState(428);
        match(RosettaMRParser::USOG);
        setState(429);
        match(RosettaMRParser::Integer);
        setState(435); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(430);
                  number_f();
                  setState(431);
                  number_f();
                  setState(432);
                  number_f();
                  setState(433);
                  number_f();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(437); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 37, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case RosettaMRParser::SOG: {
        setState(439);
        match(RosettaMRParser::SOG);
        setState(440);
        match(RosettaMRParser::Integer);
        setState(448); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(441);
                  number_f();
                  setState(442);
                  number_f();
                  setState(443);
                  number_f();
                  setState(444);
                  number_f();
                  setState(445);
                  number_f();
                  setState(446);
                  number_f();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(450); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 38, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(455);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 40, _ctx)) {
    case 1: {
      setState(454);
      comment();
      break;
    }

    default:
      break;
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Rdc_restraintsContext ------------------------------------------------------------------

RosettaMRParser::Rdc_restraintsContext::Rdc_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<RosettaMRParser::Rdc_restraintContext *> RosettaMRParser::Rdc_restraintsContext::rdc_restraint() {
  return getRuleContexts<RosettaMRParser::Rdc_restraintContext>();
}

RosettaMRParser::Rdc_restraintContext* RosettaMRParser::Rdc_restraintsContext::rdc_restraint(size_t i) {
  return getRuleContext<RosettaMRParser::Rdc_restraintContext>(i);
}


size_t RosettaMRParser::Rdc_restraintsContext::getRuleIndex() const {
  return RosettaMRParser::RuleRdc_restraints;
}


std::any RosettaMRParser::Rdc_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitRdc_restraints(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Rdc_restraintsContext* RosettaMRParser::rdc_restraints() {
  Rdc_restraintsContext *_localctx = _tracker.createInstance<Rdc_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 52, RosettaMRParser::RuleRdc_restraints);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(458); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(457);
              rdc_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(460); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 41, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Rdc_restraintContext ------------------------------------------------------------------

RosettaMRParser::Rdc_restraintContext::Rdc_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<RosettaMRParser::Gen_res_numContext *> RosettaMRParser::Rdc_restraintContext::gen_res_num() {
  return getRuleContexts<RosettaMRParser::Gen_res_numContext>();
}

RosettaMRParser::Gen_res_numContext* RosettaMRParser::Rdc_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<RosettaMRParser::Gen_res_numContext>(i);
}

std::vector<RosettaMRParser::Gen_simple_nameContext *> RosettaMRParser::Rdc_restraintContext::gen_simple_name() {
  return getRuleContexts<RosettaMRParser::Gen_simple_nameContext>();
}

RosettaMRParser::Gen_simple_nameContext* RosettaMRParser::Rdc_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<RosettaMRParser::Gen_simple_nameContext>(i);
}

RosettaMRParser::NumberContext* RosettaMRParser::Rdc_restraintContext::number() {
  return getRuleContext<RosettaMRParser::NumberContext>(0);
}


size_t RosettaMRParser::Rdc_restraintContext::getRuleIndex() const {
  return RosettaMRParser::RuleRdc_restraint;
}


std::any RosettaMRParser::Rdc_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitRdc_restraint(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Rdc_restraintContext* RosettaMRParser::rdc_restraint() {
  Rdc_restraintContext *_localctx = _tracker.createInstance<Rdc_restraintContext>(_ctx, getState());
  enterRule(_localctx, 54, RosettaMRParser::RuleRdc_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(462);
    gen_res_num();
    setState(463);
    gen_simple_name();
    setState(464);
    gen_res_num();
    setState(465);
    gen_simple_name();
    setState(466);
    number();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Disulfide_bond_linkagesContext ------------------------------------------------------------------

RosettaMRParser::Disulfide_bond_linkagesContext::Disulfide_bond_linkagesContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<RosettaMRParser::Disulfide_bond_linkageContext *> RosettaMRParser::Disulfide_bond_linkagesContext::disulfide_bond_linkage() {
  return getRuleContexts<RosettaMRParser::Disulfide_bond_linkageContext>();
}

RosettaMRParser::Disulfide_bond_linkageContext* RosettaMRParser::Disulfide_bond_linkagesContext::disulfide_bond_linkage(size_t i) {
  return getRuleContext<RosettaMRParser::Disulfide_bond_linkageContext>(i);
}


size_t RosettaMRParser::Disulfide_bond_linkagesContext::getRuleIndex() const {
  return RosettaMRParser::RuleDisulfide_bond_linkages;
}


std::any RosettaMRParser::Disulfide_bond_linkagesContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitDisulfide_bond_linkages(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Disulfide_bond_linkagesContext* RosettaMRParser::disulfide_bond_linkages() {
  Disulfide_bond_linkagesContext *_localctx = _tracker.createInstance<Disulfide_bond_linkagesContext>(_ctx, getState());
  enterRule(_localctx, 56, RosettaMRParser::RuleDisulfide_bond_linkages);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(469); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(468);
              disulfide_bond_linkage();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(471); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 42, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Disulfide_bond_linkageContext ------------------------------------------------------------------

RosettaMRParser::Disulfide_bond_linkageContext::Disulfide_bond_linkageContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<RosettaMRParser::Gen_res_numContext *> RosettaMRParser::Disulfide_bond_linkageContext::gen_res_num() {
  return getRuleContexts<RosettaMRParser::Gen_res_numContext>();
}

RosettaMRParser::Gen_res_numContext* RosettaMRParser::Disulfide_bond_linkageContext::gen_res_num(size_t i) {
  return getRuleContext<RosettaMRParser::Gen_res_numContext>(i);
}


size_t RosettaMRParser::Disulfide_bond_linkageContext::getRuleIndex() const {
  return RosettaMRParser::RuleDisulfide_bond_linkage;
}


std::any RosettaMRParser::Disulfide_bond_linkageContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitDisulfide_bond_linkage(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Disulfide_bond_linkageContext* RosettaMRParser::disulfide_bond_linkage() {
  Disulfide_bond_linkageContext *_localctx = _tracker.createInstance<Disulfide_bond_linkageContext>(_ctx, getState());
  enterRule(_localctx, 58, RosettaMRParser::RuleDisulfide_bond_linkage);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(473);
    gen_res_num();
    setState(474);
    gen_res_num();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Atom_pair_w_chain_restraintsContext ------------------------------------------------------------------

RosettaMRParser::Atom_pair_w_chain_restraintsContext::Atom_pair_w_chain_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<RosettaMRParser::Atom_pair_w_chain_restraintContext *> RosettaMRParser::Atom_pair_w_chain_restraintsContext::atom_pair_w_chain_restraint() {
  return getRuleContexts<RosettaMRParser::Atom_pair_w_chain_restraintContext>();
}

RosettaMRParser::Atom_pair_w_chain_restraintContext* RosettaMRParser::Atom_pair_w_chain_restraintsContext::atom_pair_w_chain_restraint(size_t i) {
  return getRuleContext<RosettaMRParser::Atom_pair_w_chain_restraintContext>(i);
}


size_t RosettaMRParser::Atom_pair_w_chain_restraintsContext::getRuleIndex() const {
  return RosettaMRParser::RuleAtom_pair_w_chain_restraints;
}


std::any RosettaMRParser::Atom_pair_w_chain_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitAtom_pair_w_chain_restraints(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Atom_pair_w_chain_restraintsContext* RosettaMRParser::atom_pair_w_chain_restraints() {
  Atom_pair_w_chain_restraintsContext *_localctx = _tracker.createInstance<Atom_pair_w_chain_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 60, RosettaMRParser::RuleAtom_pair_w_chain_restraints);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(477); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(476);
              atom_pair_w_chain_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(479); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 43, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Atom_pair_w_chain_restraintContext ------------------------------------------------------------------

RosettaMRParser::Atom_pair_w_chain_restraintContext::Atom_pair_w_chain_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<RosettaMRParser::Gen_simple_nameContext *> RosettaMRParser::Atom_pair_w_chain_restraintContext::gen_simple_name() {
  return getRuleContexts<RosettaMRParser::Gen_simple_nameContext>();
}

RosettaMRParser::Gen_simple_nameContext* RosettaMRParser::Atom_pair_w_chain_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<RosettaMRParser::Gen_simple_nameContext>(i);
}

std::vector<tree::TerminalNode *> RosettaMRParser::Atom_pair_w_chain_restraintContext::Integer() {
  return getTokens(RosettaMRParser::Integer);
}

tree::TerminalNode* RosettaMRParser::Atom_pair_w_chain_restraintContext::Integer(size_t i) {
  return getToken(RosettaMRParser::Integer, i);
}

RosettaMRParser::Func_type_defContext* RosettaMRParser::Atom_pair_w_chain_restraintContext::func_type_def() {
  return getRuleContext<RosettaMRParser::Func_type_defContext>(0);
}

tree::TerminalNode* RosettaMRParser::Atom_pair_w_chain_restraintContext::AtomPair() {
  return getToken(RosettaMRParser::AtomPair, 0);
}

tree::TerminalNode* RosettaMRParser::Atom_pair_w_chain_restraintContext::NamedAtomPair() {
  return getToken(RosettaMRParser::NamedAtomPair, 0);
}

tree::TerminalNode* RosettaMRParser::Atom_pair_w_chain_restraintContext::AmbiguousNMRDistance() {
  return getToken(RosettaMRParser::AmbiguousNMRDistance, 0);
}


size_t RosettaMRParser::Atom_pair_w_chain_restraintContext::getRuleIndex() const {
  return RosettaMRParser::RuleAtom_pair_w_chain_restraint;
}


std::any RosettaMRParser::Atom_pair_w_chain_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitAtom_pair_w_chain_restraint(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Atom_pair_w_chain_restraintContext* RosettaMRParser::atom_pair_w_chain_restraint() {
  Atom_pair_w_chain_restraintContext *_localctx = _tracker.createInstance<Atom_pair_w_chain_restraintContext>(_ctx, getState());
  enterRule(_localctx, 62, RosettaMRParser::RuleAtom_pair_w_chain_restraint);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(481);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 518) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(482);
    gen_simple_name();
    setState(483);
    match(RosettaMRParser::Integer);
    setState(484);
    gen_simple_name();
    setState(485);
    gen_simple_name();
    setState(486);
    match(RosettaMRParser::Integer);
    setState(487);
    gen_simple_name();
    setState(488);
    func_type_def();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- NumberContext ------------------------------------------------------------------

RosettaMRParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* RosettaMRParser::NumberContext::Float() {
  return getToken(RosettaMRParser::Float, 0);
}

tree::TerminalNode* RosettaMRParser::NumberContext::Integer() {
  return getToken(RosettaMRParser::Integer, 0);
}


size_t RosettaMRParser::NumberContext::getRuleIndex() const {
  return RosettaMRParser::RuleNumber;
}


std::any RosettaMRParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::NumberContext* RosettaMRParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 64, RosettaMRParser::RuleNumber);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(490);
    _la = _input->LA(1);
    if (!(_la == RosettaMRParser::Integer

    || _la == RosettaMRParser::Float)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Number_fContext ------------------------------------------------------------------

RosettaMRParser::Number_fContext::Number_fContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* RosettaMRParser::Number_fContext::Float() {
  return getToken(RosettaMRParser::Float, 0);
}

tree::TerminalNode* RosettaMRParser::Number_fContext::Integer() {
  return getToken(RosettaMRParser::Integer, 0);
}


size_t RosettaMRParser::Number_fContext::getRuleIndex() const {
  return RosettaMRParser::RuleNumber_f;
}


std::any RosettaMRParser::Number_fContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitNumber_f(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Number_fContext* RosettaMRParser::number_f() {
  Number_fContext *_localctx = _tracker.createInstance<Number_fContext>(_ctx, getState());
  enterRule(_localctx, 66, RosettaMRParser::RuleNumber_f);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(492);
    _la = _input->LA(1);
    if (!(_la == RosettaMRParser::Integer

    || _la == RosettaMRParser::Float)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Gen_res_numContext ------------------------------------------------------------------

RosettaMRParser::Gen_res_numContext::Gen_res_numContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* RosettaMRParser::Gen_res_numContext::Integer() {
  return getToken(RosettaMRParser::Integer, 0);
}

tree::TerminalNode* RosettaMRParser::Gen_res_numContext::Integer_capital() {
  return getToken(RosettaMRParser::Integer_capital, 0);
}

tree::TerminalNode* RosettaMRParser::Gen_res_numContext::Capital_integer() {
  return getToken(RosettaMRParser::Capital_integer, 0);
}


size_t RosettaMRParser::Gen_res_numContext::getRuleIndex() const {
  return RosettaMRParser::RuleGen_res_num;
}


std::any RosettaMRParser::Gen_res_numContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitGen_res_num(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Gen_res_numContext* RosettaMRParser::gen_res_num() {
  Gen_res_numContext *_localctx = _tracker.createInstance<Gen_res_numContext>(_ctx, getState());
  enterRule(_localctx, 68, RosettaMRParser::RuleGen_res_num);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(494);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 109212290963734528) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Gen_simple_nameContext ------------------------------------------------------------------

RosettaMRParser::Gen_simple_nameContext::Gen_simple_nameContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* RosettaMRParser::Gen_simple_nameContext::Simple_name() {
  return getToken(RosettaMRParser::Simple_name, 0);
}

tree::TerminalNode* RosettaMRParser::Gen_simple_nameContext::Integer_capital() {
  return getToken(RosettaMRParser::Integer_capital, 0);
}

tree::TerminalNode* RosettaMRParser::Gen_simple_nameContext::Capital_integer() {
  return getToken(RosettaMRParser::Capital_integer, 0);
}


size_t RosettaMRParser::Gen_simple_nameContext::getRuleIndex() const {
  return RosettaMRParser::RuleGen_simple_name;
}


std::any RosettaMRParser::Gen_simple_nameContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<RosettaMRParserVisitor*>(visitor))
    return parserVisitor->visitGen_simple_name(this);
  else
    return visitor->visitChildren(this);
}

RosettaMRParser::Gen_simple_nameContext* RosettaMRParser::gen_simple_name() {
  Gen_simple_nameContext *_localctx = _tracker.createInstance<Gen_simple_nameContext>(_ctx, getState());
  enterRule(_localctx, 70, RosettaMRParser::RuleGen_simple_name);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(496);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 252201579132747776) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

void RosettaMRParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  rosettamrparserParserInitialize();
#else
  ::antlr4::internal::call_once(rosettamrparserParserOnceFlag, rosettamrparserParserInitialize);
#endif
}
