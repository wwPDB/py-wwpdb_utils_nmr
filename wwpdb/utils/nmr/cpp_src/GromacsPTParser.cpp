
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/GromacsPTParser.g4 by ANTLR 4.13.0


#include "GromacsPTParserVisitor.h"

#include "GromacsPTParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct GromacsPTParserStaticData final {
  GromacsPTParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  GromacsPTParserStaticData(const GromacsPTParserStaticData&) = delete;
  GromacsPTParserStaticData(GromacsPTParserStaticData&&) = delete;
  GromacsPTParserStaticData& operator=(const GromacsPTParserStaticData&) = delete;
  GromacsPTParserStaticData& operator=(GromacsPTParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag gromacsptparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
GromacsPTParserStaticData *gromacsptparserParserStaticData = nullptr;

void gromacsptparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (gromacsptparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(gromacsptparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<GromacsPTParserStaticData>(
    std::vector<std::string>{
      "gromacs_pt", "default_statement", "moleculetype_statement", "moleculetype", 
      "atomtypes_statement", "atomtypes", "pairtypes_statement", "pairtypes", 
      "bondtypes_statement", "bondtypes", "angletypes_statement", "angletypes", 
      "dihedraltypes_statement", "dihedraltypes", "constrainttypes_statement", 
      "constrainttypes", "nonbonded_params_statement", "nonbonded_params", 
      "atoms_statement", "atoms", "bonds_statement", "bonds", "pairs_statement", 
      "pairs", "pairs_nb_statement", "pairs_nb", "angles_statement", "angles", 
      "dihedrals_statement", "dihedrals", "exclusions_statement", "exclusions", 
      "constraints_statement", "constraints", "settles_statement", "settles", 
      "virtual_sites1_statement", "virtual_sites1", "virtual_sites2_statement", 
      "virtual_sites2", "virtual_sites3_statement", "virtual_sites3", "virtual_sites4_statement", 
      "virtual_sites4", "virtual_sitesn_statement", "virtual_sitesn", "system_statement", 
      "molecules_statement", "molecules", "number", "position_restraints", 
      "position_restraint"
    },
    std::vector<std::string>{
      "", "'['", "']'", "'default'", "'moleculetype'", "'atomtypes'", "'pairtypes'", 
      "'bondtypes'", "'angletypes'", "'dihedraltypes'", "'constrainttypes'", 
      "'nonbond_params'", "'atoms'", "'bonds'", "'pairs'", "'pairs_nb'", 
      "'angles'", "'dihedrals'", "'exclusions'", "'constraints'", "'settles'", 
      "'virtual_sites1'", "'virtual_sites2'", "'virtual_sites3'", "'virtual_sites4'", 
      "'virtual_sitesn'", "'system'", "'molecules'", "'position_restraints'"
    },
    std::vector<std::string>{
      "", "L_brkt", "R_brkt", "Default", "Moleculetype", "Atomtypes", "Pairtypes", 
      "Bondtypes", "Angletypes", "Dihedraltypes", "Constrainttypes", "Nonbond_params", 
      "Atoms", "Bonds", "Pairs", "Pairs_nb", "Angles", "Dihedrals", "Exclusions", 
      "Constraints", "Settles", "Virtual_sites1", "Virtual_sites2", "Virtual_sites3", 
      "Virtual_sites4", "Virtual_sitesn", "System", "Molecules", "Position_restraints", 
      "Intermolecular_interactions", "Integer", "Real", "SHARP_COMMENT", 
      "EXCLM_COMMENT", "SMCLN_COMMENT", "Simple_name", "SPACE", "ENCLOSE_COMMENT", 
      "SECTION_COMMENT", "LINE_COMMENT", "R_brkt_AA", "SECTION_COMMENT_AA", 
      "LINE_COMMENT_AA", "Simple_name_AA", "SPACE_AA", "RETURN_AA"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,45,636,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,
  	21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,2,27,7,27,2,28,7,
  	28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,7,33,2,34,7,34,2,35,7,
  	35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,2,40,7,40,2,41,7,41,2,42,7,
  	42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,
  	49,2,50,7,50,2,51,7,51,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
  	0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
  	5,0,134,8,0,10,0,12,0,137,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
  	1,1,3,1,150,8,1,1,2,1,2,1,2,1,2,4,2,156,8,2,11,2,12,2,157,1,3,1,3,1,3,
  	1,4,1,4,1,4,1,4,5,4,167,8,4,10,4,12,4,170,9,4,1,5,1,5,1,5,1,5,1,5,1,5,
  	1,5,1,5,1,6,1,6,1,6,1,6,5,6,184,8,6,10,6,12,6,187,9,6,1,7,1,7,1,7,1,7,
  	1,7,1,7,1,8,1,8,1,8,1,8,5,8,199,8,8,10,8,12,8,202,9,8,1,9,1,9,1,9,1,9,
  	1,9,1,9,1,10,1,10,1,10,1,10,5,10,214,8,10,10,10,12,10,217,9,10,1,11,1,
  	11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,5,12,230,8,12,10,12,12,
  	12,233,9,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,245,
  	8,13,1,14,1,14,1,14,1,14,5,14,251,8,14,10,14,12,14,254,9,14,1,15,1,15,
  	1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,5,16,266,8,16,10,16,12,16,269,
  	9,16,1,17,1,17,1,17,1,17,1,17,1,17,3,17,277,8,17,1,18,1,18,1,18,1,18,
  	4,18,283,8,18,11,18,12,18,284,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
  	1,19,1,19,1,19,1,19,3,19,299,8,19,3,19,301,8,19,1,19,3,19,304,8,19,1,
  	20,1,20,1,20,1,20,5,20,310,8,20,10,20,12,20,313,9,20,1,21,1,21,1,21,1,
  	21,1,21,1,21,3,21,321,8,21,3,21,323,8,21,1,21,3,21,326,8,21,1,22,1,22,
  	1,22,1,22,5,22,332,8,22,10,22,12,22,335,9,22,1,23,1,23,1,23,1,23,1,23,
  	1,23,1,23,1,23,1,23,3,23,346,8,23,3,23,348,8,23,1,23,3,23,351,8,23,1,
  	24,1,24,1,24,1,24,5,24,357,8,24,10,24,12,24,360,9,24,1,25,1,25,1,25,1,
  	25,1,25,1,25,1,25,1,25,3,25,370,8,25,1,25,3,25,373,8,25,1,26,1,26,1,26,
  	1,26,5,26,379,8,26,10,26,12,26,382,9,26,1,27,1,27,1,27,1,27,1,27,1,27,
  	1,27,1,27,1,27,1,27,1,27,3,27,395,8,27,3,27,397,8,27,3,27,399,8,27,3,
  	27,401,8,27,1,27,3,27,404,8,27,1,28,1,28,1,28,1,28,5,28,410,8,28,10,28,
  	12,28,413,9,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
  	3,29,426,8,29,3,29,428,8,29,3,29,430,8,29,3,29,432,8,29,1,29,3,29,435,
  	8,29,1,30,1,30,1,30,1,30,5,30,441,8,30,10,30,12,30,444,9,30,1,31,1,31,
  	4,31,448,8,31,11,31,12,31,449,1,31,3,31,453,8,31,1,32,1,32,1,32,1,32,
  	5,32,459,8,32,10,32,12,32,462,9,32,1,33,1,33,1,33,1,33,3,33,468,8,33,
  	1,33,3,33,471,8,33,1,34,1,34,1,34,1,34,5,34,477,8,34,10,34,12,34,480,
  	9,34,1,35,1,35,1,35,1,35,1,35,3,35,487,8,35,1,35,3,35,490,8,35,1,36,1,
  	36,1,36,1,36,5,36,496,8,36,10,36,12,36,499,9,36,1,37,1,37,1,37,1,37,3,
  	37,505,8,37,1,38,1,38,1,38,1,38,5,38,511,8,38,10,38,12,38,514,9,38,1,
  	39,1,39,1,39,1,39,1,39,3,39,521,8,39,1,39,3,39,524,8,39,1,40,1,40,1,40,
  	1,40,5,40,530,8,40,10,40,12,40,533,9,40,1,41,1,41,1,41,1,41,1,41,1,41,
  	1,41,1,41,3,41,543,8,41,3,41,545,8,41,1,41,3,41,548,8,41,1,42,1,42,1,
  	42,1,42,5,42,554,8,42,10,42,12,42,557,9,42,1,43,1,43,1,43,1,43,1,43,1,
  	43,1,43,1,43,1,43,1,43,3,43,569,8,43,1,43,3,43,572,8,43,1,44,1,44,1,44,
  	1,44,5,44,578,8,44,10,44,12,44,581,9,44,1,45,1,45,1,45,4,45,586,8,45,
  	11,45,12,45,587,1,45,3,45,591,8,45,1,45,3,45,594,8,45,1,46,1,46,1,46,
  	1,46,5,46,600,8,46,10,46,12,46,603,9,46,1,46,1,46,1,47,1,47,1,47,1,47,
  	4,47,611,8,47,11,47,12,47,612,1,48,1,48,1,48,1,49,1,49,1,50,1,50,1,50,
  	1,50,4,50,624,8,50,11,50,12,50,625,1,51,1,51,1,51,1,51,1,51,1,51,3,51,
  	634,8,51,1,51,0,0,52,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
  	36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,
  	82,84,86,88,90,92,94,96,98,100,102,0,1,1,0,30,31,677,0,135,1,0,0,0,2,
  	140,1,0,0,0,4,151,1,0,0,0,6,159,1,0,0,0,8,162,1,0,0,0,10,171,1,0,0,0,
  	12,179,1,0,0,0,14,188,1,0,0,0,16,194,1,0,0,0,18,203,1,0,0,0,20,209,1,
  	0,0,0,22,218,1,0,0,0,24,225,1,0,0,0,26,234,1,0,0,0,28,246,1,0,0,0,30,
  	255,1,0,0,0,32,261,1,0,0,0,34,270,1,0,0,0,36,278,1,0,0,0,38,286,1,0,0,
  	0,40,305,1,0,0,0,42,314,1,0,0,0,44,327,1,0,0,0,46,336,1,0,0,0,48,352,
  	1,0,0,0,50,361,1,0,0,0,52,374,1,0,0,0,54,383,1,0,0,0,56,405,1,0,0,0,58,
  	414,1,0,0,0,60,436,1,0,0,0,62,445,1,0,0,0,64,454,1,0,0,0,66,463,1,0,0,
  	0,68,472,1,0,0,0,70,481,1,0,0,0,72,491,1,0,0,0,74,500,1,0,0,0,76,506,
  	1,0,0,0,78,515,1,0,0,0,80,525,1,0,0,0,82,534,1,0,0,0,84,549,1,0,0,0,86,
  	558,1,0,0,0,88,573,1,0,0,0,90,582,1,0,0,0,92,595,1,0,0,0,94,606,1,0,0,
  	0,96,614,1,0,0,0,98,617,1,0,0,0,100,619,1,0,0,0,102,627,1,0,0,0,104,134,
  	3,2,1,0,105,134,3,4,2,0,106,134,3,8,4,0,107,134,3,12,6,0,108,134,3,16,
  	8,0,109,134,3,20,10,0,110,134,3,24,12,0,111,134,3,28,14,0,112,134,3,32,
  	16,0,113,134,3,36,18,0,114,134,3,40,20,0,115,134,3,44,22,0,116,134,3,
  	48,24,0,117,134,3,52,26,0,118,134,3,56,28,0,119,134,3,60,30,0,120,134,
  	3,64,32,0,121,134,3,68,34,0,122,134,3,72,36,0,123,134,3,76,38,0,124,134,
  	3,80,40,0,125,134,3,84,42,0,126,134,3,88,44,0,127,134,3,92,46,0,128,134,
  	3,94,47,0,129,134,3,100,50,0,130,131,5,1,0,0,131,132,5,29,0,0,132,134,
  	5,2,0,0,133,104,1,0,0,0,133,105,1,0,0,0,133,106,1,0,0,0,133,107,1,0,0,
  	0,133,108,1,0,0,0,133,109,1,0,0,0,133,110,1,0,0,0,133,111,1,0,0,0,133,
  	112,1,0,0,0,133,113,1,0,0,0,133,114,1,0,0,0,133,115,1,0,0,0,133,116,1,
  	0,0,0,133,117,1,0,0,0,133,118,1,0,0,0,133,119,1,0,0,0,133,120,1,0,0,0,
  	133,121,1,0,0,0,133,122,1,0,0,0,133,123,1,0,0,0,133,124,1,0,0,0,133,125,
  	1,0,0,0,133,126,1,0,0,0,133,127,1,0,0,0,133,128,1,0,0,0,133,129,1,0,0,
  	0,133,130,1,0,0,0,134,137,1,0,0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,
  	138,1,0,0,0,137,135,1,0,0,0,138,139,5,0,0,1,139,1,1,0,0,0,140,141,5,1,
  	0,0,141,142,5,3,0,0,142,143,5,2,0,0,143,144,5,30,0,0,144,145,5,30,0,0,
  	145,146,5,35,0,0,146,147,5,31,0,0,147,149,5,31,0,0,148,150,5,35,0,0,149,
  	148,1,0,0,0,149,150,1,0,0,0,150,3,1,0,0,0,151,152,5,1,0,0,152,153,5,4,
  	0,0,153,155,5,2,0,0,154,156,3,6,3,0,155,154,1,0,0,0,156,157,1,0,0,0,157,
  	155,1,0,0,0,157,158,1,0,0,0,158,5,1,0,0,0,159,160,5,35,0,0,160,161,5,
  	30,0,0,161,7,1,0,0,0,162,163,5,1,0,0,163,164,5,5,0,0,164,168,5,2,0,0,
  	165,167,3,10,5,0,166,165,1,0,0,0,167,170,1,0,0,0,168,166,1,0,0,0,168,
  	169,1,0,0,0,169,9,1,0,0,0,170,168,1,0,0,0,171,172,5,35,0,0,172,173,5,
  	30,0,0,173,174,5,31,0,0,174,175,5,31,0,0,175,176,5,30,0,0,176,177,5,31,
  	0,0,177,178,5,31,0,0,178,11,1,0,0,0,179,180,5,1,0,0,180,181,5,6,0,0,181,
  	185,5,2,0,0,182,184,3,14,7,0,183,182,1,0,0,0,184,187,1,0,0,0,185,183,
  	1,0,0,0,185,186,1,0,0,0,186,13,1,0,0,0,187,185,1,0,0,0,188,189,5,35,0,
  	0,189,190,5,35,0,0,190,191,5,30,0,0,191,192,5,31,0,0,192,193,5,31,0,0,
  	193,15,1,0,0,0,194,195,5,1,0,0,195,196,5,7,0,0,196,200,5,2,0,0,197,199,
  	3,18,9,0,198,197,1,0,0,0,199,202,1,0,0,0,200,198,1,0,0,0,200,201,1,0,
  	0,0,201,17,1,0,0,0,202,200,1,0,0,0,203,204,5,35,0,0,204,205,5,35,0,0,
  	205,206,5,30,0,0,206,207,5,31,0,0,207,208,5,31,0,0,208,19,1,0,0,0,209,
  	210,5,1,0,0,210,211,5,8,0,0,211,215,5,2,0,0,212,214,3,22,11,0,213,212,
  	1,0,0,0,214,217,1,0,0,0,215,213,1,0,0,0,215,216,1,0,0,0,216,21,1,0,0,
  	0,217,215,1,0,0,0,218,219,5,35,0,0,219,220,5,35,0,0,220,221,5,35,0,0,
  	221,222,5,30,0,0,222,223,5,31,0,0,223,224,5,31,0,0,224,23,1,0,0,0,225,
  	226,5,1,0,0,226,227,5,9,0,0,227,231,5,2,0,0,228,230,3,26,13,0,229,228,
  	1,0,0,0,230,233,1,0,0,0,231,229,1,0,0,0,231,232,1,0,0,0,232,25,1,0,0,
  	0,233,231,1,0,0,0,234,235,5,35,0,0,235,236,5,35,0,0,236,237,5,30,0,0,
  	237,238,5,31,0,0,238,244,5,31,0,0,239,245,5,30,0,0,240,241,5,31,0,0,241,
  	242,5,31,0,0,242,243,5,31,0,0,243,245,5,31,0,0,244,239,1,0,0,0,244,240,
  	1,0,0,0,245,27,1,0,0,0,246,247,5,1,0,0,247,248,5,10,0,0,248,252,5,2,0,
  	0,249,251,3,30,15,0,250,249,1,0,0,0,251,254,1,0,0,0,252,250,1,0,0,0,252,
  	253,1,0,0,0,253,29,1,0,0,0,254,252,1,0,0,0,255,256,5,35,0,0,256,257,5,
  	35,0,0,257,258,5,30,0,0,258,259,5,31,0,0,259,260,5,31,0,0,260,31,1,0,
  	0,0,261,262,5,1,0,0,262,263,5,11,0,0,263,267,5,2,0,0,264,266,3,34,17,
  	0,265,264,1,0,0,0,266,269,1,0,0,0,267,265,1,0,0,0,267,268,1,0,0,0,268,
  	33,1,0,0,0,269,267,1,0,0,0,270,271,5,35,0,0,271,272,5,35,0,0,272,273,
  	5,30,0,0,273,274,5,31,0,0,274,276,5,31,0,0,275,277,5,31,0,0,276,275,1,
  	0,0,0,276,277,1,0,0,0,277,35,1,0,0,0,278,279,5,1,0,0,279,280,5,12,0,0,
  	280,282,5,2,0,0,281,283,3,38,19,0,282,281,1,0,0,0,283,284,1,0,0,0,284,
  	282,1,0,0,0,284,285,1,0,0,0,285,37,1,0,0,0,286,287,5,30,0,0,287,288,5,
  	35,0,0,288,289,5,30,0,0,289,290,5,35,0,0,290,291,5,35,0,0,291,292,5,30,
  	0,0,292,300,3,98,49,0,293,298,3,98,49,0,294,295,5,35,0,0,295,296,3,98,
  	49,0,296,297,3,98,49,0,297,299,1,0,0,0,298,294,1,0,0,0,298,299,1,0,0,
  	0,299,301,1,0,0,0,300,293,1,0,0,0,300,301,1,0,0,0,301,303,1,0,0,0,302,
  	304,5,35,0,0,303,302,1,0,0,0,303,304,1,0,0,0,304,39,1,0,0,0,305,306,5,
  	1,0,0,306,307,5,13,0,0,307,311,5,2,0,0,308,310,3,42,21,0,309,308,1,0,
  	0,0,310,313,1,0,0,0,311,309,1,0,0,0,311,312,1,0,0,0,312,41,1,0,0,0,313,
  	311,1,0,0,0,314,315,5,30,0,0,315,316,5,30,0,0,316,322,5,30,0,0,317,318,
  	3,98,49,0,318,320,3,98,49,0,319,321,3,98,49,0,320,319,1,0,0,0,320,321,
  	1,0,0,0,321,323,1,0,0,0,322,317,1,0,0,0,322,323,1,0,0,0,323,325,1,0,0,
  	0,324,326,5,35,0,0,325,324,1,0,0,0,325,326,1,0,0,0,326,43,1,0,0,0,327,
  	328,5,1,0,0,328,329,5,14,0,0,329,333,5,2,0,0,330,332,3,46,23,0,331,330,
  	1,0,0,0,332,335,1,0,0,0,333,331,1,0,0,0,333,334,1,0,0,0,334,45,1,0,0,
  	0,335,333,1,0,0,0,336,337,5,30,0,0,337,338,5,30,0,0,338,347,5,30,0,0,
  	339,340,3,98,49,0,340,345,3,98,49,0,341,342,3,98,49,0,342,343,3,98,49,
  	0,343,344,3,98,49,0,344,346,1,0,0,0,345,341,1,0,0,0,345,346,1,0,0,0,346,
  	348,1,0,0,0,347,339,1,0,0,0,347,348,1,0,0,0,348,350,1,0,0,0,349,351,5,
  	35,0,0,350,349,1,0,0,0,350,351,1,0,0,0,351,47,1,0,0,0,352,353,5,1,0,0,
  	353,354,5,15,0,0,354,358,5,2,0,0,355,357,3,50,25,0,356,355,1,0,0,0,357,
  	360,1,0,0,0,358,356,1,0,0,0,358,359,1,0,0,0,359,49,1,0,0,0,360,358,1,
  	0,0,0,361,362,5,30,0,0,362,363,5,30,0,0,363,369,5,30,0,0,364,365,3,98,
  	49,0,365,366,3,98,49,0,366,367,3,98,49,0,367,368,3,98,49,0,368,370,1,
  	0,0,0,369,364,1,0,0,0,369,370,1,0,0,0,370,372,1,0,0,0,371,373,5,35,0,
  	0,372,371,1,0,0,0,372,373,1,0,0,0,373,51,1,0,0,0,374,375,5,1,0,0,375,
  	376,5,16,0,0,376,380,5,2,0,0,377,379,3,54,27,0,378,377,1,0,0,0,379,382,
  	1,0,0,0,380,378,1,0,0,0,380,381,1,0,0,0,381,53,1,0,0,0,382,380,1,0,0,
  	0,383,384,5,30,0,0,384,385,5,30,0,0,385,386,5,30,0,0,386,400,5,30,0,0,
  	387,388,3,98,49,0,388,398,3,98,49,0,389,396,3,98,49,0,390,394,3,98,49,
  	0,391,392,3,98,49,0,392,393,3,98,49,0,393,395,1,0,0,0,394,391,1,0,0,0,
  	394,395,1,0,0,0,395,397,1,0,0,0,396,390,1,0,0,0,396,397,1,0,0,0,397,399,
  	1,0,0,0,398,389,1,0,0,0,398,399,1,0,0,0,399,401,1,0,0,0,400,387,1,0,0,
  	0,400,401,1,0,0,0,401,403,1,0,0,0,402,404,5,35,0,0,403,402,1,0,0,0,403,
  	404,1,0,0,0,404,55,1,0,0,0,405,406,5,1,0,0,406,407,5,17,0,0,407,411,5,
  	2,0,0,408,410,3,58,29,0,409,408,1,0,0,0,410,413,1,0,0,0,411,409,1,0,0,
  	0,411,412,1,0,0,0,412,57,1,0,0,0,413,411,1,0,0,0,414,415,5,30,0,0,415,
  	416,5,30,0,0,416,417,5,30,0,0,417,418,5,30,0,0,418,431,5,30,0,0,419,420,
  	3,98,49,0,420,429,3,98,49,0,421,427,3,98,49,0,422,423,3,98,49,0,423,425,
  	3,98,49,0,424,426,3,98,49,0,425,424,1,0,0,0,425,426,1,0,0,0,426,428,1,
  	0,0,0,427,422,1,0,0,0,427,428,1,0,0,0,428,430,1,0,0,0,429,421,1,0,0,0,
  	429,430,1,0,0,0,430,432,1,0,0,0,431,419,1,0,0,0,431,432,1,0,0,0,432,434,
  	1,0,0,0,433,435,5,35,0,0,434,433,1,0,0,0,434,435,1,0,0,0,435,59,1,0,0,
  	0,436,437,5,1,0,0,437,438,5,18,0,0,438,442,5,2,0,0,439,441,3,62,31,0,
  	440,439,1,0,0,0,441,444,1,0,0,0,442,440,1,0,0,0,442,443,1,0,0,0,443,61,
  	1,0,0,0,444,442,1,0,0,0,445,447,5,30,0,0,446,448,5,30,0,0,447,446,1,0,
  	0,0,448,449,1,0,0,0,449,447,1,0,0,0,449,450,1,0,0,0,450,452,1,0,0,0,451,
  	453,5,35,0,0,452,451,1,0,0,0,452,453,1,0,0,0,453,63,1,0,0,0,454,455,5,
  	1,0,0,455,456,5,19,0,0,456,460,5,2,0,0,457,459,3,66,33,0,458,457,1,0,
  	0,0,459,462,1,0,0,0,460,458,1,0,0,0,460,461,1,0,0,0,461,65,1,0,0,0,462,
  	460,1,0,0,0,463,464,5,30,0,0,464,465,5,30,0,0,465,467,5,30,0,0,466,468,
  	3,98,49,0,467,466,1,0,0,0,467,468,1,0,0,0,468,470,1,0,0,0,469,471,5,35,
  	0,0,470,469,1,0,0,0,470,471,1,0,0,0,471,67,1,0,0,0,472,473,5,1,0,0,473,
  	474,5,20,0,0,474,478,5,2,0,0,475,477,3,70,35,0,476,475,1,0,0,0,477,480,
  	1,0,0,0,478,476,1,0,0,0,478,479,1,0,0,0,479,69,1,0,0,0,480,478,1,0,0,
  	0,481,482,5,30,0,0,482,486,5,30,0,0,483,484,3,98,49,0,484,485,3,98,49,
  	0,485,487,1,0,0,0,486,483,1,0,0,0,486,487,1,0,0,0,487,489,1,0,0,0,488,
  	490,5,35,0,0,489,488,1,0,0,0,489,490,1,0,0,0,490,71,1,0,0,0,491,492,5,
  	1,0,0,492,493,5,21,0,0,493,497,5,2,0,0,494,496,3,74,37,0,495,494,1,0,
  	0,0,496,499,1,0,0,0,497,495,1,0,0,0,497,498,1,0,0,0,498,73,1,0,0,0,499,
  	497,1,0,0,0,500,501,5,30,0,0,501,502,5,30,0,0,502,504,5,30,0,0,503,505,
  	5,35,0,0,504,503,1,0,0,0,504,505,1,0,0,0,505,75,1,0,0,0,506,507,5,1,0,
  	0,507,508,5,22,0,0,508,512,5,2,0,0,509,511,3,78,39,0,510,509,1,0,0,0,
  	511,514,1,0,0,0,512,510,1,0,0,0,512,513,1,0,0,0,513,77,1,0,0,0,514,512,
  	1,0,0,0,515,516,5,30,0,0,516,517,5,30,0,0,517,518,5,30,0,0,518,520,5,
  	30,0,0,519,521,3,98,49,0,520,519,1,0,0,0,520,521,1,0,0,0,521,523,1,0,
  	0,0,522,524,5,35,0,0,523,522,1,0,0,0,523,524,1,0,0,0,524,79,1,0,0,0,525,
  	526,5,1,0,0,526,527,5,23,0,0,527,531,5,2,0,0,528,530,3,82,41,0,529,528,
  	1,0,0,0,530,533,1,0,0,0,531,529,1,0,0,0,531,532,1,0,0,0,532,81,1,0,0,
  	0,533,531,1,0,0,0,534,535,5,30,0,0,535,536,5,30,0,0,536,537,5,30,0,0,
  	537,538,5,30,0,0,538,544,5,30,0,0,539,540,3,98,49,0,540,542,3,98,49,0,
  	541,543,3,98,49,0,542,541,1,0,0,0,542,543,1,0,0,0,543,545,1,0,0,0,544,
  	539,1,0,0,0,544,545,1,0,0,0,545,547,1,0,0,0,546,548,5,35,0,0,547,546,
  	1,0,0,0,547,548,1,0,0,0,548,83,1,0,0,0,549,550,5,1,0,0,550,551,5,24,0,
  	0,551,555,5,2,0,0,552,554,3,86,43,0,553,552,1,0,0,0,554,557,1,0,0,0,555,
  	553,1,0,0,0,555,556,1,0,0,0,556,85,1,0,0,0,557,555,1,0,0,0,558,559,5,
  	30,0,0,559,560,5,30,0,0,560,561,5,30,0,0,561,562,5,30,0,0,562,563,5,30,
  	0,0,563,568,5,30,0,0,564,565,3,98,49,0,565,566,3,98,49,0,566,567,3,98,
  	49,0,567,569,1,0,0,0,568,564,1,0,0,0,568,569,1,0,0,0,569,571,1,0,0,0,
  	570,572,5,35,0,0,571,570,1,0,0,0,571,572,1,0,0,0,572,87,1,0,0,0,573,574,
  	5,1,0,0,574,575,5,25,0,0,575,579,5,2,0,0,576,578,3,90,45,0,577,576,1,
  	0,0,0,578,581,1,0,0,0,579,577,1,0,0,0,579,580,1,0,0,0,580,89,1,0,0,0,
  	581,579,1,0,0,0,582,583,5,30,0,0,583,585,5,30,0,0,584,586,5,30,0,0,585,
  	584,1,0,0,0,586,587,1,0,0,0,587,585,1,0,0,0,587,588,1,0,0,0,588,590,1,
  	0,0,0,589,591,3,98,49,0,590,589,1,0,0,0,590,591,1,0,0,0,591,593,1,0,0,
  	0,592,594,5,35,0,0,593,592,1,0,0,0,593,594,1,0,0,0,594,91,1,0,0,0,595,
  	596,5,1,0,0,596,597,5,26,0,0,597,601,5,40,0,0,598,600,5,43,0,0,599,598,
  	1,0,0,0,600,603,1,0,0,0,601,599,1,0,0,0,601,602,1,0,0,0,602,604,1,0,0,
  	0,603,601,1,0,0,0,604,605,5,45,0,0,605,93,1,0,0,0,606,607,5,1,0,0,607,
  	608,5,27,0,0,608,610,5,2,0,0,609,611,3,96,48,0,610,609,1,0,0,0,611,612,
  	1,0,0,0,612,610,1,0,0,0,612,613,1,0,0,0,613,95,1,0,0,0,614,615,5,35,0,
  	0,615,616,5,30,0,0,616,97,1,0,0,0,617,618,7,0,0,0,618,99,1,0,0,0,619,
  	620,5,1,0,0,620,621,5,28,0,0,621,623,5,2,0,0,622,624,3,102,51,0,623,622,
  	1,0,0,0,624,625,1,0,0,0,625,623,1,0,0,0,625,626,1,0,0,0,626,101,1,0,0,
  	0,627,628,5,30,0,0,628,629,5,30,0,0,629,630,3,98,49,0,630,631,3,98,49,
  	0,631,633,3,98,49,0,632,634,5,35,0,0,633,632,1,0,0,0,633,634,1,0,0,0,
  	634,103,1,0,0,0,69,133,135,149,157,168,185,200,215,231,244,252,267,276,
  	284,298,300,303,311,320,322,325,333,345,347,350,358,369,372,380,394,396,
  	398,400,403,411,425,427,429,431,434,442,449,452,460,467,470,478,486,489,
  	497,504,512,520,523,531,542,544,547,555,568,571,579,587,590,593,601,612,
  	625,633
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  gromacsptparserParserStaticData = staticData.release();
}

}

GromacsPTParser::GromacsPTParser(TokenStream *input) : GromacsPTParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

GromacsPTParser::GromacsPTParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  GromacsPTParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *gromacsptparserParserStaticData->atn, gromacsptparserParserStaticData->decisionToDFA, gromacsptparserParserStaticData->sharedContextCache, options);
}

GromacsPTParser::~GromacsPTParser() {
  delete _interpreter;
}

const atn::ATN& GromacsPTParser::getATN() const {
  return *gromacsptparserParserStaticData->atn;
}

std::string GromacsPTParser::getGrammarFileName() const {
  return "GromacsPTParser.g4";
}

const std::vector<std::string>& GromacsPTParser::getRuleNames() const {
  return gromacsptparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& GromacsPTParser::getVocabulary() const {
  return gromacsptparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView GromacsPTParser::getSerializedATN() const {
  return gromacsptparserParserStaticData->serializedATN;
}


//----------------- Gromacs_ptContext ------------------------------------------------------------------

GromacsPTParser::Gromacs_ptContext::Gromacs_ptContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::Gromacs_ptContext::EOF() {
  return getToken(GromacsPTParser::EOF, 0);
}

std::vector<GromacsPTParser::Default_statementContext *> GromacsPTParser::Gromacs_ptContext::default_statement() {
  return getRuleContexts<GromacsPTParser::Default_statementContext>();
}

GromacsPTParser::Default_statementContext* GromacsPTParser::Gromacs_ptContext::default_statement(size_t i) {
  return getRuleContext<GromacsPTParser::Default_statementContext>(i);
}

std::vector<GromacsPTParser::Moleculetype_statementContext *> GromacsPTParser::Gromacs_ptContext::moleculetype_statement() {
  return getRuleContexts<GromacsPTParser::Moleculetype_statementContext>();
}

GromacsPTParser::Moleculetype_statementContext* GromacsPTParser::Gromacs_ptContext::moleculetype_statement(size_t i) {
  return getRuleContext<GromacsPTParser::Moleculetype_statementContext>(i);
}

std::vector<GromacsPTParser::Atomtypes_statementContext *> GromacsPTParser::Gromacs_ptContext::atomtypes_statement() {
  return getRuleContexts<GromacsPTParser::Atomtypes_statementContext>();
}

GromacsPTParser::Atomtypes_statementContext* GromacsPTParser::Gromacs_ptContext::atomtypes_statement(size_t i) {
  return getRuleContext<GromacsPTParser::Atomtypes_statementContext>(i);
}

std::vector<GromacsPTParser::Pairtypes_statementContext *> GromacsPTParser::Gromacs_ptContext::pairtypes_statement() {
  return getRuleContexts<GromacsPTParser::Pairtypes_statementContext>();
}

GromacsPTParser::Pairtypes_statementContext* GromacsPTParser::Gromacs_ptContext::pairtypes_statement(size_t i) {
  return getRuleContext<GromacsPTParser::Pairtypes_statementContext>(i);
}

std::vector<GromacsPTParser::Bondtypes_statementContext *> GromacsPTParser::Gromacs_ptContext::bondtypes_statement() {
  return getRuleContexts<GromacsPTParser::Bondtypes_statementContext>();
}

GromacsPTParser::Bondtypes_statementContext* GromacsPTParser::Gromacs_ptContext::bondtypes_statement(size_t i) {
  return getRuleContext<GromacsPTParser::Bondtypes_statementContext>(i);
}

std::vector<GromacsPTParser::Angletypes_statementContext *> GromacsPTParser::Gromacs_ptContext::angletypes_statement() {
  return getRuleContexts<GromacsPTParser::Angletypes_statementContext>();
}

GromacsPTParser::Angletypes_statementContext* GromacsPTParser::Gromacs_ptContext::angletypes_statement(size_t i) {
  return getRuleContext<GromacsPTParser::Angletypes_statementContext>(i);
}

std::vector<GromacsPTParser::Dihedraltypes_statementContext *> GromacsPTParser::Gromacs_ptContext::dihedraltypes_statement() {
  return getRuleContexts<GromacsPTParser::Dihedraltypes_statementContext>();
}

GromacsPTParser::Dihedraltypes_statementContext* GromacsPTParser::Gromacs_ptContext::dihedraltypes_statement(size_t i) {
  return getRuleContext<GromacsPTParser::Dihedraltypes_statementContext>(i);
}

std::vector<GromacsPTParser::Constrainttypes_statementContext *> GromacsPTParser::Gromacs_ptContext::constrainttypes_statement() {
  return getRuleContexts<GromacsPTParser::Constrainttypes_statementContext>();
}

GromacsPTParser::Constrainttypes_statementContext* GromacsPTParser::Gromacs_ptContext::constrainttypes_statement(size_t i) {
  return getRuleContext<GromacsPTParser::Constrainttypes_statementContext>(i);
}

std::vector<GromacsPTParser::Nonbonded_params_statementContext *> GromacsPTParser::Gromacs_ptContext::nonbonded_params_statement() {
  return getRuleContexts<GromacsPTParser::Nonbonded_params_statementContext>();
}

GromacsPTParser::Nonbonded_params_statementContext* GromacsPTParser::Gromacs_ptContext::nonbonded_params_statement(size_t i) {
  return getRuleContext<GromacsPTParser::Nonbonded_params_statementContext>(i);
}

std::vector<GromacsPTParser::Atoms_statementContext *> GromacsPTParser::Gromacs_ptContext::atoms_statement() {
  return getRuleContexts<GromacsPTParser::Atoms_statementContext>();
}

GromacsPTParser::Atoms_statementContext* GromacsPTParser::Gromacs_ptContext::atoms_statement(size_t i) {
  return getRuleContext<GromacsPTParser::Atoms_statementContext>(i);
}

std::vector<GromacsPTParser::Bonds_statementContext *> GromacsPTParser::Gromacs_ptContext::bonds_statement() {
  return getRuleContexts<GromacsPTParser::Bonds_statementContext>();
}

GromacsPTParser::Bonds_statementContext* GromacsPTParser::Gromacs_ptContext::bonds_statement(size_t i) {
  return getRuleContext<GromacsPTParser::Bonds_statementContext>(i);
}

std::vector<GromacsPTParser::Pairs_statementContext *> GromacsPTParser::Gromacs_ptContext::pairs_statement() {
  return getRuleContexts<GromacsPTParser::Pairs_statementContext>();
}

GromacsPTParser::Pairs_statementContext* GromacsPTParser::Gromacs_ptContext::pairs_statement(size_t i) {
  return getRuleContext<GromacsPTParser::Pairs_statementContext>(i);
}

std::vector<GromacsPTParser::Pairs_nb_statementContext *> GromacsPTParser::Gromacs_ptContext::pairs_nb_statement() {
  return getRuleContexts<GromacsPTParser::Pairs_nb_statementContext>();
}

GromacsPTParser::Pairs_nb_statementContext* GromacsPTParser::Gromacs_ptContext::pairs_nb_statement(size_t i) {
  return getRuleContext<GromacsPTParser::Pairs_nb_statementContext>(i);
}

std::vector<GromacsPTParser::Angles_statementContext *> GromacsPTParser::Gromacs_ptContext::angles_statement() {
  return getRuleContexts<GromacsPTParser::Angles_statementContext>();
}

GromacsPTParser::Angles_statementContext* GromacsPTParser::Gromacs_ptContext::angles_statement(size_t i) {
  return getRuleContext<GromacsPTParser::Angles_statementContext>(i);
}

std::vector<GromacsPTParser::Dihedrals_statementContext *> GromacsPTParser::Gromacs_ptContext::dihedrals_statement() {
  return getRuleContexts<GromacsPTParser::Dihedrals_statementContext>();
}

GromacsPTParser::Dihedrals_statementContext* GromacsPTParser::Gromacs_ptContext::dihedrals_statement(size_t i) {
  return getRuleContext<GromacsPTParser::Dihedrals_statementContext>(i);
}

std::vector<GromacsPTParser::Exclusions_statementContext *> GromacsPTParser::Gromacs_ptContext::exclusions_statement() {
  return getRuleContexts<GromacsPTParser::Exclusions_statementContext>();
}

GromacsPTParser::Exclusions_statementContext* GromacsPTParser::Gromacs_ptContext::exclusions_statement(size_t i) {
  return getRuleContext<GromacsPTParser::Exclusions_statementContext>(i);
}

std::vector<GromacsPTParser::Constraints_statementContext *> GromacsPTParser::Gromacs_ptContext::constraints_statement() {
  return getRuleContexts<GromacsPTParser::Constraints_statementContext>();
}

GromacsPTParser::Constraints_statementContext* GromacsPTParser::Gromacs_ptContext::constraints_statement(size_t i) {
  return getRuleContext<GromacsPTParser::Constraints_statementContext>(i);
}

std::vector<GromacsPTParser::Settles_statementContext *> GromacsPTParser::Gromacs_ptContext::settles_statement() {
  return getRuleContexts<GromacsPTParser::Settles_statementContext>();
}

GromacsPTParser::Settles_statementContext* GromacsPTParser::Gromacs_ptContext::settles_statement(size_t i) {
  return getRuleContext<GromacsPTParser::Settles_statementContext>(i);
}

std::vector<GromacsPTParser::Virtual_sites1_statementContext *> GromacsPTParser::Gromacs_ptContext::virtual_sites1_statement() {
  return getRuleContexts<GromacsPTParser::Virtual_sites1_statementContext>();
}

GromacsPTParser::Virtual_sites1_statementContext* GromacsPTParser::Gromacs_ptContext::virtual_sites1_statement(size_t i) {
  return getRuleContext<GromacsPTParser::Virtual_sites1_statementContext>(i);
}

std::vector<GromacsPTParser::Virtual_sites2_statementContext *> GromacsPTParser::Gromacs_ptContext::virtual_sites2_statement() {
  return getRuleContexts<GromacsPTParser::Virtual_sites2_statementContext>();
}

GromacsPTParser::Virtual_sites2_statementContext* GromacsPTParser::Gromacs_ptContext::virtual_sites2_statement(size_t i) {
  return getRuleContext<GromacsPTParser::Virtual_sites2_statementContext>(i);
}

std::vector<GromacsPTParser::Virtual_sites3_statementContext *> GromacsPTParser::Gromacs_ptContext::virtual_sites3_statement() {
  return getRuleContexts<GromacsPTParser::Virtual_sites3_statementContext>();
}

GromacsPTParser::Virtual_sites3_statementContext* GromacsPTParser::Gromacs_ptContext::virtual_sites3_statement(size_t i) {
  return getRuleContext<GromacsPTParser::Virtual_sites3_statementContext>(i);
}

std::vector<GromacsPTParser::Virtual_sites4_statementContext *> GromacsPTParser::Gromacs_ptContext::virtual_sites4_statement() {
  return getRuleContexts<GromacsPTParser::Virtual_sites4_statementContext>();
}

GromacsPTParser::Virtual_sites4_statementContext* GromacsPTParser::Gromacs_ptContext::virtual_sites4_statement(size_t i) {
  return getRuleContext<GromacsPTParser::Virtual_sites4_statementContext>(i);
}

std::vector<GromacsPTParser::Virtual_sitesn_statementContext *> GromacsPTParser::Gromacs_ptContext::virtual_sitesn_statement() {
  return getRuleContexts<GromacsPTParser::Virtual_sitesn_statementContext>();
}

GromacsPTParser::Virtual_sitesn_statementContext* GromacsPTParser::Gromacs_ptContext::virtual_sitesn_statement(size_t i) {
  return getRuleContext<GromacsPTParser::Virtual_sitesn_statementContext>(i);
}

std::vector<GromacsPTParser::System_statementContext *> GromacsPTParser::Gromacs_ptContext::system_statement() {
  return getRuleContexts<GromacsPTParser::System_statementContext>();
}

GromacsPTParser::System_statementContext* GromacsPTParser::Gromacs_ptContext::system_statement(size_t i) {
  return getRuleContext<GromacsPTParser::System_statementContext>(i);
}

std::vector<GromacsPTParser::Molecules_statementContext *> GromacsPTParser::Gromacs_ptContext::molecules_statement() {
  return getRuleContexts<GromacsPTParser::Molecules_statementContext>();
}

GromacsPTParser::Molecules_statementContext* GromacsPTParser::Gromacs_ptContext::molecules_statement(size_t i) {
  return getRuleContext<GromacsPTParser::Molecules_statementContext>(i);
}

std::vector<GromacsPTParser::Position_restraintsContext *> GromacsPTParser::Gromacs_ptContext::position_restraints() {
  return getRuleContexts<GromacsPTParser::Position_restraintsContext>();
}

GromacsPTParser::Position_restraintsContext* GromacsPTParser::Gromacs_ptContext::position_restraints(size_t i) {
  return getRuleContext<GromacsPTParser::Position_restraintsContext>(i);
}

std::vector<tree::TerminalNode *> GromacsPTParser::Gromacs_ptContext::L_brkt() {
  return getTokens(GromacsPTParser::L_brkt);
}

tree::TerminalNode* GromacsPTParser::Gromacs_ptContext::L_brkt(size_t i) {
  return getToken(GromacsPTParser::L_brkt, i);
}

std::vector<tree::TerminalNode *> GromacsPTParser::Gromacs_ptContext::Intermolecular_interactions() {
  return getTokens(GromacsPTParser::Intermolecular_interactions);
}

tree::TerminalNode* GromacsPTParser::Gromacs_ptContext::Intermolecular_interactions(size_t i) {
  return getToken(GromacsPTParser::Intermolecular_interactions, i);
}

std::vector<tree::TerminalNode *> GromacsPTParser::Gromacs_ptContext::R_brkt() {
  return getTokens(GromacsPTParser::R_brkt);
}

tree::TerminalNode* GromacsPTParser::Gromacs_ptContext::R_brkt(size_t i) {
  return getToken(GromacsPTParser::R_brkt, i);
}


size_t GromacsPTParser::Gromacs_ptContext::getRuleIndex() const {
  return GromacsPTParser::RuleGromacs_pt;
}


std::any GromacsPTParser::Gromacs_ptContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitGromacs_pt(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Gromacs_ptContext* GromacsPTParser::gromacs_pt() {
  Gromacs_ptContext *_localctx = _tracker.createInstance<Gromacs_ptContext>(_ctx, getState());
  enterRule(_localctx, 0, GromacsPTParser::RuleGromacs_pt);
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
    setState(135);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == GromacsPTParser::L_brkt) {
      setState(133);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx)) {
      case 1: {
        setState(104);
        default_statement();
        break;
      }

      case 2: {
        setState(105);
        moleculetype_statement();
        break;
      }

      case 3: {
        setState(106);
        atomtypes_statement();
        break;
      }

      case 4: {
        setState(107);
        pairtypes_statement();
        break;
      }

      case 5: {
        setState(108);
        bondtypes_statement();
        break;
      }

      case 6: {
        setState(109);
        angletypes_statement();
        break;
      }

      case 7: {
        setState(110);
        dihedraltypes_statement();
        break;
      }

      case 8: {
        setState(111);
        constrainttypes_statement();
        break;
      }

      case 9: {
        setState(112);
        nonbonded_params_statement();
        break;
      }

      case 10: {
        setState(113);
        atoms_statement();
        break;
      }

      case 11: {
        setState(114);
        bonds_statement();
        break;
      }

      case 12: {
        setState(115);
        pairs_statement();
        break;
      }

      case 13: {
        setState(116);
        pairs_nb_statement();
        break;
      }

      case 14: {
        setState(117);
        angles_statement();
        break;
      }

      case 15: {
        setState(118);
        dihedrals_statement();
        break;
      }

      case 16: {
        setState(119);
        exclusions_statement();
        break;
      }

      case 17: {
        setState(120);
        constraints_statement();
        break;
      }

      case 18: {
        setState(121);
        settles_statement();
        break;
      }

      case 19: {
        setState(122);
        virtual_sites1_statement();
        break;
      }

      case 20: {
        setState(123);
        virtual_sites2_statement();
        break;
      }

      case 21: {
        setState(124);
        virtual_sites3_statement();
        break;
      }

      case 22: {
        setState(125);
        virtual_sites4_statement();
        break;
      }

      case 23: {
        setState(126);
        virtual_sitesn_statement();
        break;
      }

      case 24: {
        setState(127);
        system_statement();
        break;
      }

      case 25: {
        setState(128);
        molecules_statement();
        break;
      }

      case 26: {
        setState(129);
        position_restraints();
        break;
      }

      case 27: {
        setState(130);
        match(GromacsPTParser::L_brkt);
        setState(131);
        match(GromacsPTParser::Intermolecular_interactions);
        setState(132);
        match(GromacsPTParser::R_brkt);
        break;
      }

      default:
        break;
      }
      setState(137);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(138);
    match(GromacsPTParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Default_statementContext ------------------------------------------------------------------

GromacsPTParser::Default_statementContext::Default_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::Default_statementContext::L_brkt() {
  return getToken(GromacsPTParser::L_brkt, 0);
}

tree::TerminalNode* GromacsPTParser::Default_statementContext::Default() {
  return getToken(GromacsPTParser::Default, 0);
}

tree::TerminalNode* GromacsPTParser::Default_statementContext::R_brkt() {
  return getToken(GromacsPTParser::R_brkt, 0);
}

std::vector<tree::TerminalNode *> GromacsPTParser::Default_statementContext::Integer() {
  return getTokens(GromacsPTParser::Integer);
}

tree::TerminalNode* GromacsPTParser::Default_statementContext::Integer(size_t i) {
  return getToken(GromacsPTParser::Integer, i);
}

std::vector<tree::TerminalNode *> GromacsPTParser::Default_statementContext::Simple_name() {
  return getTokens(GromacsPTParser::Simple_name);
}

tree::TerminalNode* GromacsPTParser::Default_statementContext::Simple_name(size_t i) {
  return getToken(GromacsPTParser::Simple_name, i);
}

std::vector<tree::TerminalNode *> GromacsPTParser::Default_statementContext::Real() {
  return getTokens(GromacsPTParser::Real);
}

tree::TerminalNode* GromacsPTParser::Default_statementContext::Real(size_t i) {
  return getToken(GromacsPTParser::Real, i);
}


size_t GromacsPTParser::Default_statementContext::getRuleIndex() const {
  return GromacsPTParser::RuleDefault_statement;
}


std::any GromacsPTParser::Default_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitDefault_statement(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Default_statementContext* GromacsPTParser::default_statement() {
  Default_statementContext *_localctx = _tracker.createInstance<Default_statementContext>(_ctx, getState());
  enterRule(_localctx, 2, GromacsPTParser::RuleDefault_statement);
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
    setState(140);
    match(GromacsPTParser::L_brkt);
    setState(141);
    match(GromacsPTParser::Default);
    setState(142);
    match(GromacsPTParser::R_brkt);
    setState(143);
    match(GromacsPTParser::Integer);
    setState(144);
    match(GromacsPTParser::Integer);
    setState(145);
    match(GromacsPTParser::Simple_name);
    setState(146);
    match(GromacsPTParser::Real);
    setState(147);
    match(GromacsPTParser::Real);
    setState(149);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == GromacsPTParser::Simple_name) {
      setState(148);
      match(GromacsPTParser::Simple_name);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Moleculetype_statementContext ------------------------------------------------------------------

GromacsPTParser::Moleculetype_statementContext::Moleculetype_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::Moleculetype_statementContext::L_brkt() {
  return getToken(GromacsPTParser::L_brkt, 0);
}

tree::TerminalNode* GromacsPTParser::Moleculetype_statementContext::Moleculetype() {
  return getToken(GromacsPTParser::Moleculetype, 0);
}

tree::TerminalNode* GromacsPTParser::Moleculetype_statementContext::R_brkt() {
  return getToken(GromacsPTParser::R_brkt, 0);
}

std::vector<GromacsPTParser::MoleculetypeContext *> GromacsPTParser::Moleculetype_statementContext::moleculetype() {
  return getRuleContexts<GromacsPTParser::MoleculetypeContext>();
}

GromacsPTParser::MoleculetypeContext* GromacsPTParser::Moleculetype_statementContext::moleculetype(size_t i) {
  return getRuleContext<GromacsPTParser::MoleculetypeContext>(i);
}


size_t GromacsPTParser::Moleculetype_statementContext::getRuleIndex() const {
  return GromacsPTParser::RuleMoleculetype_statement;
}


std::any GromacsPTParser::Moleculetype_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitMoleculetype_statement(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Moleculetype_statementContext* GromacsPTParser::moleculetype_statement() {
  Moleculetype_statementContext *_localctx = _tracker.createInstance<Moleculetype_statementContext>(_ctx, getState());
  enterRule(_localctx, 4, GromacsPTParser::RuleMoleculetype_statement);
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
    setState(151);
    match(GromacsPTParser::L_brkt);
    setState(152);
    match(GromacsPTParser::Moleculetype);
    setState(153);
    match(GromacsPTParser::R_brkt);
    setState(155); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(154);
      moleculetype();
      setState(157); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == GromacsPTParser::Simple_name);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- MoleculetypeContext ------------------------------------------------------------------

GromacsPTParser::MoleculetypeContext::MoleculetypeContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::MoleculetypeContext::Simple_name() {
  return getToken(GromacsPTParser::Simple_name, 0);
}

tree::TerminalNode* GromacsPTParser::MoleculetypeContext::Integer() {
  return getToken(GromacsPTParser::Integer, 0);
}


size_t GromacsPTParser::MoleculetypeContext::getRuleIndex() const {
  return GromacsPTParser::RuleMoleculetype;
}


std::any GromacsPTParser::MoleculetypeContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitMoleculetype(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::MoleculetypeContext* GromacsPTParser::moleculetype() {
  MoleculetypeContext *_localctx = _tracker.createInstance<MoleculetypeContext>(_ctx, getState());
  enterRule(_localctx, 6, GromacsPTParser::RuleMoleculetype);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(159);
    match(GromacsPTParser::Simple_name);
    setState(160);
    match(GromacsPTParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Atomtypes_statementContext ------------------------------------------------------------------

GromacsPTParser::Atomtypes_statementContext::Atomtypes_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::Atomtypes_statementContext::L_brkt() {
  return getToken(GromacsPTParser::L_brkt, 0);
}

tree::TerminalNode* GromacsPTParser::Atomtypes_statementContext::Atomtypes() {
  return getToken(GromacsPTParser::Atomtypes, 0);
}

tree::TerminalNode* GromacsPTParser::Atomtypes_statementContext::R_brkt() {
  return getToken(GromacsPTParser::R_brkt, 0);
}

std::vector<GromacsPTParser::AtomtypesContext *> GromacsPTParser::Atomtypes_statementContext::atomtypes() {
  return getRuleContexts<GromacsPTParser::AtomtypesContext>();
}

GromacsPTParser::AtomtypesContext* GromacsPTParser::Atomtypes_statementContext::atomtypes(size_t i) {
  return getRuleContext<GromacsPTParser::AtomtypesContext>(i);
}


size_t GromacsPTParser::Atomtypes_statementContext::getRuleIndex() const {
  return GromacsPTParser::RuleAtomtypes_statement;
}


std::any GromacsPTParser::Atomtypes_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitAtomtypes_statement(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Atomtypes_statementContext* GromacsPTParser::atomtypes_statement() {
  Atomtypes_statementContext *_localctx = _tracker.createInstance<Atomtypes_statementContext>(_ctx, getState());
  enterRule(_localctx, 8, GromacsPTParser::RuleAtomtypes_statement);
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
    setState(162);
    match(GromacsPTParser::L_brkt);
    setState(163);
    match(GromacsPTParser::Atomtypes);
    setState(164);
    match(GromacsPTParser::R_brkt);
    setState(168);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == GromacsPTParser::Simple_name) {
      setState(165);
      atomtypes();
      setState(170);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- AtomtypesContext ------------------------------------------------------------------

GromacsPTParser::AtomtypesContext::AtomtypesContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::AtomtypesContext::Simple_name() {
  return getToken(GromacsPTParser::Simple_name, 0);
}

std::vector<tree::TerminalNode *> GromacsPTParser::AtomtypesContext::Integer() {
  return getTokens(GromacsPTParser::Integer);
}

tree::TerminalNode* GromacsPTParser::AtomtypesContext::Integer(size_t i) {
  return getToken(GromacsPTParser::Integer, i);
}

std::vector<tree::TerminalNode *> GromacsPTParser::AtomtypesContext::Real() {
  return getTokens(GromacsPTParser::Real);
}

tree::TerminalNode* GromacsPTParser::AtomtypesContext::Real(size_t i) {
  return getToken(GromacsPTParser::Real, i);
}


size_t GromacsPTParser::AtomtypesContext::getRuleIndex() const {
  return GromacsPTParser::RuleAtomtypes;
}


std::any GromacsPTParser::AtomtypesContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitAtomtypes(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::AtomtypesContext* GromacsPTParser::atomtypes() {
  AtomtypesContext *_localctx = _tracker.createInstance<AtomtypesContext>(_ctx, getState());
  enterRule(_localctx, 10, GromacsPTParser::RuleAtomtypes);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(171);
    match(GromacsPTParser::Simple_name);
    setState(172);
    match(GromacsPTParser::Integer);
    setState(173);
    match(GromacsPTParser::Real);
    setState(174);
    match(GromacsPTParser::Real);
    setState(175);
    match(GromacsPTParser::Integer);
    setState(176);
    match(GromacsPTParser::Real);
    setState(177);
    match(GromacsPTParser::Real);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Pairtypes_statementContext ------------------------------------------------------------------

GromacsPTParser::Pairtypes_statementContext::Pairtypes_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::Pairtypes_statementContext::L_brkt() {
  return getToken(GromacsPTParser::L_brkt, 0);
}

tree::TerminalNode* GromacsPTParser::Pairtypes_statementContext::Pairtypes() {
  return getToken(GromacsPTParser::Pairtypes, 0);
}

tree::TerminalNode* GromacsPTParser::Pairtypes_statementContext::R_brkt() {
  return getToken(GromacsPTParser::R_brkt, 0);
}

std::vector<GromacsPTParser::PairtypesContext *> GromacsPTParser::Pairtypes_statementContext::pairtypes() {
  return getRuleContexts<GromacsPTParser::PairtypesContext>();
}

GromacsPTParser::PairtypesContext* GromacsPTParser::Pairtypes_statementContext::pairtypes(size_t i) {
  return getRuleContext<GromacsPTParser::PairtypesContext>(i);
}


size_t GromacsPTParser::Pairtypes_statementContext::getRuleIndex() const {
  return GromacsPTParser::RulePairtypes_statement;
}


std::any GromacsPTParser::Pairtypes_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitPairtypes_statement(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Pairtypes_statementContext* GromacsPTParser::pairtypes_statement() {
  Pairtypes_statementContext *_localctx = _tracker.createInstance<Pairtypes_statementContext>(_ctx, getState());
  enterRule(_localctx, 12, GromacsPTParser::RulePairtypes_statement);
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
    setState(179);
    match(GromacsPTParser::L_brkt);
    setState(180);
    match(GromacsPTParser::Pairtypes);
    setState(181);
    match(GromacsPTParser::R_brkt);
    setState(185);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == GromacsPTParser::Simple_name) {
      setState(182);
      pairtypes();
      setState(187);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- PairtypesContext ------------------------------------------------------------------

GromacsPTParser::PairtypesContext::PairtypesContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> GromacsPTParser::PairtypesContext::Simple_name() {
  return getTokens(GromacsPTParser::Simple_name);
}

tree::TerminalNode* GromacsPTParser::PairtypesContext::Simple_name(size_t i) {
  return getToken(GromacsPTParser::Simple_name, i);
}

tree::TerminalNode* GromacsPTParser::PairtypesContext::Integer() {
  return getToken(GromacsPTParser::Integer, 0);
}

std::vector<tree::TerminalNode *> GromacsPTParser::PairtypesContext::Real() {
  return getTokens(GromacsPTParser::Real);
}

tree::TerminalNode* GromacsPTParser::PairtypesContext::Real(size_t i) {
  return getToken(GromacsPTParser::Real, i);
}


size_t GromacsPTParser::PairtypesContext::getRuleIndex() const {
  return GromacsPTParser::RulePairtypes;
}


std::any GromacsPTParser::PairtypesContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitPairtypes(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::PairtypesContext* GromacsPTParser::pairtypes() {
  PairtypesContext *_localctx = _tracker.createInstance<PairtypesContext>(_ctx, getState());
  enterRule(_localctx, 14, GromacsPTParser::RulePairtypes);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(188);
    match(GromacsPTParser::Simple_name);
    setState(189);
    match(GromacsPTParser::Simple_name);
    setState(190);
    match(GromacsPTParser::Integer);
    setState(191);
    match(GromacsPTParser::Real);
    setState(192);
    match(GromacsPTParser::Real);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Bondtypes_statementContext ------------------------------------------------------------------

GromacsPTParser::Bondtypes_statementContext::Bondtypes_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::Bondtypes_statementContext::L_brkt() {
  return getToken(GromacsPTParser::L_brkt, 0);
}

tree::TerminalNode* GromacsPTParser::Bondtypes_statementContext::Bondtypes() {
  return getToken(GromacsPTParser::Bondtypes, 0);
}

tree::TerminalNode* GromacsPTParser::Bondtypes_statementContext::R_brkt() {
  return getToken(GromacsPTParser::R_brkt, 0);
}

std::vector<GromacsPTParser::BondtypesContext *> GromacsPTParser::Bondtypes_statementContext::bondtypes() {
  return getRuleContexts<GromacsPTParser::BondtypesContext>();
}

GromacsPTParser::BondtypesContext* GromacsPTParser::Bondtypes_statementContext::bondtypes(size_t i) {
  return getRuleContext<GromacsPTParser::BondtypesContext>(i);
}


size_t GromacsPTParser::Bondtypes_statementContext::getRuleIndex() const {
  return GromacsPTParser::RuleBondtypes_statement;
}


std::any GromacsPTParser::Bondtypes_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitBondtypes_statement(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Bondtypes_statementContext* GromacsPTParser::bondtypes_statement() {
  Bondtypes_statementContext *_localctx = _tracker.createInstance<Bondtypes_statementContext>(_ctx, getState());
  enterRule(_localctx, 16, GromacsPTParser::RuleBondtypes_statement);
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
    setState(194);
    match(GromacsPTParser::L_brkt);
    setState(195);
    match(GromacsPTParser::Bondtypes);
    setState(196);
    match(GromacsPTParser::R_brkt);
    setState(200);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == GromacsPTParser::Simple_name) {
      setState(197);
      bondtypes();
      setState(202);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- BondtypesContext ------------------------------------------------------------------

GromacsPTParser::BondtypesContext::BondtypesContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> GromacsPTParser::BondtypesContext::Simple_name() {
  return getTokens(GromacsPTParser::Simple_name);
}

tree::TerminalNode* GromacsPTParser::BondtypesContext::Simple_name(size_t i) {
  return getToken(GromacsPTParser::Simple_name, i);
}

tree::TerminalNode* GromacsPTParser::BondtypesContext::Integer() {
  return getToken(GromacsPTParser::Integer, 0);
}

std::vector<tree::TerminalNode *> GromacsPTParser::BondtypesContext::Real() {
  return getTokens(GromacsPTParser::Real);
}

tree::TerminalNode* GromacsPTParser::BondtypesContext::Real(size_t i) {
  return getToken(GromacsPTParser::Real, i);
}


size_t GromacsPTParser::BondtypesContext::getRuleIndex() const {
  return GromacsPTParser::RuleBondtypes;
}


std::any GromacsPTParser::BondtypesContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitBondtypes(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::BondtypesContext* GromacsPTParser::bondtypes() {
  BondtypesContext *_localctx = _tracker.createInstance<BondtypesContext>(_ctx, getState());
  enterRule(_localctx, 18, GromacsPTParser::RuleBondtypes);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(203);
    match(GromacsPTParser::Simple_name);
    setState(204);
    match(GromacsPTParser::Simple_name);
    setState(205);
    match(GromacsPTParser::Integer);
    setState(206);
    match(GromacsPTParser::Real);
    setState(207);
    match(GromacsPTParser::Real);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Angletypes_statementContext ------------------------------------------------------------------

GromacsPTParser::Angletypes_statementContext::Angletypes_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::Angletypes_statementContext::L_brkt() {
  return getToken(GromacsPTParser::L_brkt, 0);
}

tree::TerminalNode* GromacsPTParser::Angletypes_statementContext::Angletypes() {
  return getToken(GromacsPTParser::Angletypes, 0);
}

tree::TerminalNode* GromacsPTParser::Angletypes_statementContext::R_brkt() {
  return getToken(GromacsPTParser::R_brkt, 0);
}

std::vector<GromacsPTParser::AngletypesContext *> GromacsPTParser::Angletypes_statementContext::angletypes() {
  return getRuleContexts<GromacsPTParser::AngletypesContext>();
}

GromacsPTParser::AngletypesContext* GromacsPTParser::Angletypes_statementContext::angletypes(size_t i) {
  return getRuleContext<GromacsPTParser::AngletypesContext>(i);
}


size_t GromacsPTParser::Angletypes_statementContext::getRuleIndex() const {
  return GromacsPTParser::RuleAngletypes_statement;
}


std::any GromacsPTParser::Angletypes_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitAngletypes_statement(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Angletypes_statementContext* GromacsPTParser::angletypes_statement() {
  Angletypes_statementContext *_localctx = _tracker.createInstance<Angletypes_statementContext>(_ctx, getState());
  enterRule(_localctx, 20, GromacsPTParser::RuleAngletypes_statement);
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
    setState(209);
    match(GromacsPTParser::L_brkt);
    setState(210);
    match(GromacsPTParser::Angletypes);
    setState(211);
    match(GromacsPTParser::R_brkt);
    setState(215);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == GromacsPTParser::Simple_name) {
      setState(212);
      angletypes();
      setState(217);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- AngletypesContext ------------------------------------------------------------------

GromacsPTParser::AngletypesContext::AngletypesContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> GromacsPTParser::AngletypesContext::Simple_name() {
  return getTokens(GromacsPTParser::Simple_name);
}

tree::TerminalNode* GromacsPTParser::AngletypesContext::Simple_name(size_t i) {
  return getToken(GromacsPTParser::Simple_name, i);
}

tree::TerminalNode* GromacsPTParser::AngletypesContext::Integer() {
  return getToken(GromacsPTParser::Integer, 0);
}

std::vector<tree::TerminalNode *> GromacsPTParser::AngletypesContext::Real() {
  return getTokens(GromacsPTParser::Real);
}

tree::TerminalNode* GromacsPTParser::AngletypesContext::Real(size_t i) {
  return getToken(GromacsPTParser::Real, i);
}


size_t GromacsPTParser::AngletypesContext::getRuleIndex() const {
  return GromacsPTParser::RuleAngletypes;
}


std::any GromacsPTParser::AngletypesContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitAngletypes(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::AngletypesContext* GromacsPTParser::angletypes() {
  AngletypesContext *_localctx = _tracker.createInstance<AngletypesContext>(_ctx, getState());
  enterRule(_localctx, 22, GromacsPTParser::RuleAngletypes);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(218);
    match(GromacsPTParser::Simple_name);
    setState(219);
    match(GromacsPTParser::Simple_name);
    setState(220);
    match(GromacsPTParser::Simple_name);
    setState(221);
    match(GromacsPTParser::Integer);
    setState(222);
    match(GromacsPTParser::Real);
    setState(223);
    match(GromacsPTParser::Real);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Dihedraltypes_statementContext ------------------------------------------------------------------

GromacsPTParser::Dihedraltypes_statementContext::Dihedraltypes_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::Dihedraltypes_statementContext::L_brkt() {
  return getToken(GromacsPTParser::L_brkt, 0);
}

tree::TerminalNode* GromacsPTParser::Dihedraltypes_statementContext::Dihedraltypes() {
  return getToken(GromacsPTParser::Dihedraltypes, 0);
}

tree::TerminalNode* GromacsPTParser::Dihedraltypes_statementContext::R_brkt() {
  return getToken(GromacsPTParser::R_brkt, 0);
}

std::vector<GromacsPTParser::DihedraltypesContext *> GromacsPTParser::Dihedraltypes_statementContext::dihedraltypes() {
  return getRuleContexts<GromacsPTParser::DihedraltypesContext>();
}

GromacsPTParser::DihedraltypesContext* GromacsPTParser::Dihedraltypes_statementContext::dihedraltypes(size_t i) {
  return getRuleContext<GromacsPTParser::DihedraltypesContext>(i);
}


size_t GromacsPTParser::Dihedraltypes_statementContext::getRuleIndex() const {
  return GromacsPTParser::RuleDihedraltypes_statement;
}


std::any GromacsPTParser::Dihedraltypes_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitDihedraltypes_statement(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Dihedraltypes_statementContext* GromacsPTParser::dihedraltypes_statement() {
  Dihedraltypes_statementContext *_localctx = _tracker.createInstance<Dihedraltypes_statementContext>(_ctx, getState());
  enterRule(_localctx, 24, GromacsPTParser::RuleDihedraltypes_statement);
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
    setState(225);
    match(GromacsPTParser::L_brkt);
    setState(226);
    match(GromacsPTParser::Dihedraltypes);
    setState(227);
    match(GromacsPTParser::R_brkt);
    setState(231);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == GromacsPTParser::Simple_name) {
      setState(228);
      dihedraltypes();
      setState(233);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- DihedraltypesContext ------------------------------------------------------------------

GromacsPTParser::DihedraltypesContext::DihedraltypesContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> GromacsPTParser::DihedraltypesContext::Simple_name() {
  return getTokens(GromacsPTParser::Simple_name);
}

tree::TerminalNode* GromacsPTParser::DihedraltypesContext::Simple_name(size_t i) {
  return getToken(GromacsPTParser::Simple_name, i);
}

std::vector<tree::TerminalNode *> GromacsPTParser::DihedraltypesContext::Integer() {
  return getTokens(GromacsPTParser::Integer);
}

tree::TerminalNode* GromacsPTParser::DihedraltypesContext::Integer(size_t i) {
  return getToken(GromacsPTParser::Integer, i);
}

std::vector<tree::TerminalNode *> GromacsPTParser::DihedraltypesContext::Real() {
  return getTokens(GromacsPTParser::Real);
}

tree::TerminalNode* GromacsPTParser::DihedraltypesContext::Real(size_t i) {
  return getToken(GromacsPTParser::Real, i);
}


size_t GromacsPTParser::DihedraltypesContext::getRuleIndex() const {
  return GromacsPTParser::RuleDihedraltypes;
}


std::any GromacsPTParser::DihedraltypesContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitDihedraltypes(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::DihedraltypesContext* GromacsPTParser::dihedraltypes() {
  DihedraltypesContext *_localctx = _tracker.createInstance<DihedraltypesContext>(_ctx, getState());
  enterRule(_localctx, 26, GromacsPTParser::RuleDihedraltypes);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(234);
    match(GromacsPTParser::Simple_name);
    setState(235);
    match(GromacsPTParser::Simple_name);
    setState(236);
    match(GromacsPTParser::Integer);
    setState(237);
    match(GromacsPTParser::Real);
    setState(238);
    match(GromacsPTParser::Real);
    setState(244);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case GromacsPTParser::Integer: {
        setState(239);
        match(GromacsPTParser::Integer);
        break;
      }

      case GromacsPTParser::Real: {
        setState(240);
        match(GromacsPTParser::Real);
        setState(241);
        match(GromacsPTParser::Real);
        setState(242);
        match(GromacsPTParser::Real);
        setState(243);
        match(GromacsPTParser::Real);
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

//----------------- Constrainttypes_statementContext ------------------------------------------------------------------

GromacsPTParser::Constrainttypes_statementContext::Constrainttypes_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::Constrainttypes_statementContext::L_brkt() {
  return getToken(GromacsPTParser::L_brkt, 0);
}

tree::TerminalNode* GromacsPTParser::Constrainttypes_statementContext::Constrainttypes() {
  return getToken(GromacsPTParser::Constrainttypes, 0);
}

tree::TerminalNode* GromacsPTParser::Constrainttypes_statementContext::R_brkt() {
  return getToken(GromacsPTParser::R_brkt, 0);
}

std::vector<GromacsPTParser::ConstrainttypesContext *> GromacsPTParser::Constrainttypes_statementContext::constrainttypes() {
  return getRuleContexts<GromacsPTParser::ConstrainttypesContext>();
}

GromacsPTParser::ConstrainttypesContext* GromacsPTParser::Constrainttypes_statementContext::constrainttypes(size_t i) {
  return getRuleContext<GromacsPTParser::ConstrainttypesContext>(i);
}


size_t GromacsPTParser::Constrainttypes_statementContext::getRuleIndex() const {
  return GromacsPTParser::RuleConstrainttypes_statement;
}


std::any GromacsPTParser::Constrainttypes_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitConstrainttypes_statement(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Constrainttypes_statementContext* GromacsPTParser::constrainttypes_statement() {
  Constrainttypes_statementContext *_localctx = _tracker.createInstance<Constrainttypes_statementContext>(_ctx, getState());
  enterRule(_localctx, 28, GromacsPTParser::RuleConstrainttypes_statement);
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
    setState(246);
    match(GromacsPTParser::L_brkt);
    setState(247);
    match(GromacsPTParser::Constrainttypes);
    setState(248);
    match(GromacsPTParser::R_brkt);
    setState(252);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == GromacsPTParser::Simple_name) {
      setState(249);
      constrainttypes();
      setState(254);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ConstrainttypesContext ------------------------------------------------------------------

GromacsPTParser::ConstrainttypesContext::ConstrainttypesContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> GromacsPTParser::ConstrainttypesContext::Simple_name() {
  return getTokens(GromacsPTParser::Simple_name);
}

tree::TerminalNode* GromacsPTParser::ConstrainttypesContext::Simple_name(size_t i) {
  return getToken(GromacsPTParser::Simple_name, i);
}

tree::TerminalNode* GromacsPTParser::ConstrainttypesContext::Integer() {
  return getToken(GromacsPTParser::Integer, 0);
}

std::vector<tree::TerminalNode *> GromacsPTParser::ConstrainttypesContext::Real() {
  return getTokens(GromacsPTParser::Real);
}

tree::TerminalNode* GromacsPTParser::ConstrainttypesContext::Real(size_t i) {
  return getToken(GromacsPTParser::Real, i);
}


size_t GromacsPTParser::ConstrainttypesContext::getRuleIndex() const {
  return GromacsPTParser::RuleConstrainttypes;
}


std::any GromacsPTParser::ConstrainttypesContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitConstrainttypes(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::ConstrainttypesContext* GromacsPTParser::constrainttypes() {
  ConstrainttypesContext *_localctx = _tracker.createInstance<ConstrainttypesContext>(_ctx, getState());
  enterRule(_localctx, 30, GromacsPTParser::RuleConstrainttypes);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(255);
    match(GromacsPTParser::Simple_name);
    setState(256);
    match(GromacsPTParser::Simple_name);
    setState(257);
    match(GromacsPTParser::Integer);
    setState(258);
    match(GromacsPTParser::Real);
    setState(259);
    match(GromacsPTParser::Real);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Nonbonded_params_statementContext ------------------------------------------------------------------

GromacsPTParser::Nonbonded_params_statementContext::Nonbonded_params_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::Nonbonded_params_statementContext::L_brkt() {
  return getToken(GromacsPTParser::L_brkt, 0);
}

tree::TerminalNode* GromacsPTParser::Nonbonded_params_statementContext::Nonbond_params() {
  return getToken(GromacsPTParser::Nonbond_params, 0);
}

tree::TerminalNode* GromacsPTParser::Nonbonded_params_statementContext::R_brkt() {
  return getToken(GromacsPTParser::R_brkt, 0);
}

std::vector<GromacsPTParser::Nonbonded_paramsContext *> GromacsPTParser::Nonbonded_params_statementContext::nonbonded_params() {
  return getRuleContexts<GromacsPTParser::Nonbonded_paramsContext>();
}

GromacsPTParser::Nonbonded_paramsContext* GromacsPTParser::Nonbonded_params_statementContext::nonbonded_params(size_t i) {
  return getRuleContext<GromacsPTParser::Nonbonded_paramsContext>(i);
}


size_t GromacsPTParser::Nonbonded_params_statementContext::getRuleIndex() const {
  return GromacsPTParser::RuleNonbonded_params_statement;
}


std::any GromacsPTParser::Nonbonded_params_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitNonbonded_params_statement(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Nonbonded_params_statementContext* GromacsPTParser::nonbonded_params_statement() {
  Nonbonded_params_statementContext *_localctx = _tracker.createInstance<Nonbonded_params_statementContext>(_ctx, getState());
  enterRule(_localctx, 32, GromacsPTParser::RuleNonbonded_params_statement);
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
    setState(261);
    match(GromacsPTParser::L_brkt);
    setState(262);
    match(GromacsPTParser::Nonbond_params);
    setState(263);
    match(GromacsPTParser::R_brkt);
    setState(267);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == GromacsPTParser::Simple_name) {
      setState(264);
      nonbonded_params();
      setState(269);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Nonbonded_paramsContext ------------------------------------------------------------------

GromacsPTParser::Nonbonded_paramsContext::Nonbonded_paramsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> GromacsPTParser::Nonbonded_paramsContext::Simple_name() {
  return getTokens(GromacsPTParser::Simple_name);
}

tree::TerminalNode* GromacsPTParser::Nonbonded_paramsContext::Simple_name(size_t i) {
  return getToken(GromacsPTParser::Simple_name, i);
}

tree::TerminalNode* GromacsPTParser::Nonbonded_paramsContext::Integer() {
  return getToken(GromacsPTParser::Integer, 0);
}

std::vector<tree::TerminalNode *> GromacsPTParser::Nonbonded_paramsContext::Real() {
  return getTokens(GromacsPTParser::Real);
}

tree::TerminalNode* GromacsPTParser::Nonbonded_paramsContext::Real(size_t i) {
  return getToken(GromacsPTParser::Real, i);
}


size_t GromacsPTParser::Nonbonded_paramsContext::getRuleIndex() const {
  return GromacsPTParser::RuleNonbonded_params;
}


std::any GromacsPTParser::Nonbonded_paramsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitNonbonded_params(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Nonbonded_paramsContext* GromacsPTParser::nonbonded_params() {
  Nonbonded_paramsContext *_localctx = _tracker.createInstance<Nonbonded_paramsContext>(_ctx, getState());
  enterRule(_localctx, 34, GromacsPTParser::RuleNonbonded_params);
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
    setState(270);
    match(GromacsPTParser::Simple_name);
    setState(271);
    match(GromacsPTParser::Simple_name);
    setState(272);
    match(GromacsPTParser::Integer);
    setState(273);
    match(GromacsPTParser::Real);
    setState(274);
    match(GromacsPTParser::Real);
    setState(276);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == GromacsPTParser::Real) {
      setState(275);
      match(GromacsPTParser::Real);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Atoms_statementContext ------------------------------------------------------------------

GromacsPTParser::Atoms_statementContext::Atoms_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::Atoms_statementContext::L_brkt() {
  return getToken(GromacsPTParser::L_brkt, 0);
}

tree::TerminalNode* GromacsPTParser::Atoms_statementContext::Atoms() {
  return getToken(GromacsPTParser::Atoms, 0);
}

tree::TerminalNode* GromacsPTParser::Atoms_statementContext::R_brkt() {
  return getToken(GromacsPTParser::R_brkt, 0);
}

std::vector<GromacsPTParser::AtomsContext *> GromacsPTParser::Atoms_statementContext::atoms() {
  return getRuleContexts<GromacsPTParser::AtomsContext>();
}

GromacsPTParser::AtomsContext* GromacsPTParser::Atoms_statementContext::atoms(size_t i) {
  return getRuleContext<GromacsPTParser::AtomsContext>(i);
}


size_t GromacsPTParser::Atoms_statementContext::getRuleIndex() const {
  return GromacsPTParser::RuleAtoms_statement;
}


std::any GromacsPTParser::Atoms_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitAtoms_statement(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Atoms_statementContext* GromacsPTParser::atoms_statement() {
  Atoms_statementContext *_localctx = _tracker.createInstance<Atoms_statementContext>(_ctx, getState());
  enterRule(_localctx, 36, GromacsPTParser::RuleAtoms_statement);
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
    setState(278);
    match(GromacsPTParser::L_brkt);
    setState(279);
    match(GromacsPTParser::Atoms);
    setState(280);
    match(GromacsPTParser::R_brkt);
    setState(282); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(281);
      atoms();
      setState(284); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == GromacsPTParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- AtomsContext ------------------------------------------------------------------

GromacsPTParser::AtomsContext::AtomsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> GromacsPTParser::AtomsContext::Integer() {
  return getTokens(GromacsPTParser::Integer);
}

tree::TerminalNode* GromacsPTParser::AtomsContext::Integer(size_t i) {
  return getToken(GromacsPTParser::Integer, i);
}

std::vector<tree::TerminalNode *> GromacsPTParser::AtomsContext::Simple_name() {
  return getTokens(GromacsPTParser::Simple_name);
}

tree::TerminalNode* GromacsPTParser::AtomsContext::Simple_name(size_t i) {
  return getToken(GromacsPTParser::Simple_name, i);
}

std::vector<GromacsPTParser::NumberContext *> GromacsPTParser::AtomsContext::number() {
  return getRuleContexts<GromacsPTParser::NumberContext>();
}

GromacsPTParser::NumberContext* GromacsPTParser::AtomsContext::number(size_t i) {
  return getRuleContext<GromacsPTParser::NumberContext>(i);
}


size_t GromacsPTParser::AtomsContext::getRuleIndex() const {
  return GromacsPTParser::RuleAtoms;
}


std::any GromacsPTParser::AtomsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitAtoms(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::AtomsContext* GromacsPTParser::atoms() {
  AtomsContext *_localctx = _tracker.createInstance<AtomsContext>(_ctx, getState());
  enterRule(_localctx, 38, GromacsPTParser::RuleAtoms);
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
    setState(286);
    match(GromacsPTParser::Integer);
    setState(287);
    match(GromacsPTParser::Simple_name);
    setState(288);
    match(GromacsPTParser::Integer);
    setState(289);
    match(GromacsPTParser::Simple_name);
    setState(290);
    match(GromacsPTParser::Simple_name);
    setState(291);
    match(GromacsPTParser::Integer);
    setState(292);
    number();
    setState(300);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 15, _ctx)) {
    case 1: {
      setState(293);
      number();
      setState(298);
      _errHandler->sync(this);

      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 14, _ctx)) {
      case 1: {
        setState(294);
        match(GromacsPTParser::Simple_name);
        setState(295);
        number();
        setState(296);
        number();
        break;
      }

      default:
        break;
      }
      break;
    }

    default:
      break;
    }
    setState(303);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == GromacsPTParser::Simple_name) {
      setState(302);
      match(GromacsPTParser::Simple_name);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Bonds_statementContext ------------------------------------------------------------------

GromacsPTParser::Bonds_statementContext::Bonds_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::Bonds_statementContext::L_brkt() {
  return getToken(GromacsPTParser::L_brkt, 0);
}

tree::TerminalNode* GromacsPTParser::Bonds_statementContext::Bonds() {
  return getToken(GromacsPTParser::Bonds, 0);
}

tree::TerminalNode* GromacsPTParser::Bonds_statementContext::R_brkt() {
  return getToken(GromacsPTParser::R_brkt, 0);
}

std::vector<GromacsPTParser::BondsContext *> GromacsPTParser::Bonds_statementContext::bonds() {
  return getRuleContexts<GromacsPTParser::BondsContext>();
}

GromacsPTParser::BondsContext* GromacsPTParser::Bonds_statementContext::bonds(size_t i) {
  return getRuleContext<GromacsPTParser::BondsContext>(i);
}


size_t GromacsPTParser::Bonds_statementContext::getRuleIndex() const {
  return GromacsPTParser::RuleBonds_statement;
}


std::any GromacsPTParser::Bonds_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitBonds_statement(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Bonds_statementContext* GromacsPTParser::bonds_statement() {
  Bonds_statementContext *_localctx = _tracker.createInstance<Bonds_statementContext>(_ctx, getState());
  enterRule(_localctx, 40, GromacsPTParser::RuleBonds_statement);
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
    setState(305);
    match(GromacsPTParser::L_brkt);
    setState(306);
    match(GromacsPTParser::Bonds);
    setState(307);
    match(GromacsPTParser::R_brkt);
    setState(311);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == GromacsPTParser::Integer) {
      setState(308);
      bonds();
      setState(313);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- BondsContext ------------------------------------------------------------------

GromacsPTParser::BondsContext::BondsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> GromacsPTParser::BondsContext::Integer() {
  return getTokens(GromacsPTParser::Integer);
}

tree::TerminalNode* GromacsPTParser::BondsContext::Integer(size_t i) {
  return getToken(GromacsPTParser::Integer, i);
}

std::vector<GromacsPTParser::NumberContext *> GromacsPTParser::BondsContext::number() {
  return getRuleContexts<GromacsPTParser::NumberContext>();
}

GromacsPTParser::NumberContext* GromacsPTParser::BondsContext::number(size_t i) {
  return getRuleContext<GromacsPTParser::NumberContext>(i);
}

tree::TerminalNode* GromacsPTParser::BondsContext::Simple_name() {
  return getToken(GromacsPTParser::Simple_name, 0);
}


size_t GromacsPTParser::BondsContext::getRuleIndex() const {
  return GromacsPTParser::RuleBonds;
}


std::any GromacsPTParser::BondsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitBonds(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::BondsContext* GromacsPTParser::bonds() {
  BondsContext *_localctx = _tracker.createInstance<BondsContext>(_ctx, getState());
  enterRule(_localctx, 42, GromacsPTParser::RuleBonds);
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
    setState(314);
    match(GromacsPTParser::Integer);
    setState(315);
    match(GromacsPTParser::Integer);
    setState(316);
    match(GromacsPTParser::Integer);
    setState(322);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 19, _ctx)) {
    case 1: {
      setState(317);
      number();
      setState(318);
      number();
      setState(320);
      _errHandler->sync(this);

      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 18, _ctx)) {
      case 1: {
        setState(319);
        number();
        break;
      }

      default:
        break;
      }
      break;
    }

    default:
      break;
    }
    setState(325);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == GromacsPTParser::Simple_name) {
      setState(324);
      match(GromacsPTParser::Simple_name);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Pairs_statementContext ------------------------------------------------------------------

GromacsPTParser::Pairs_statementContext::Pairs_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::Pairs_statementContext::L_brkt() {
  return getToken(GromacsPTParser::L_brkt, 0);
}

tree::TerminalNode* GromacsPTParser::Pairs_statementContext::Pairs() {
  return getToken(GromacsPTParser::Pairs, 0);
}

tree::TerminalNode* GromacsPTParser::Pairs_statementContext::R_brkt() {
  return getToken(GromacsPTParser::R_brkt, 0);
}

std::vector<GromacsPTParser::PairsContext *> GromacsPTParser::Pairs_statementContext::pairs() {
  return getRuleContexts<GromacsPTParser::PairsContext>();
}

GromacsPTParser::PairsContext* GromacsPTParser::Pairs_statementContext::pairs(size_t i) {
  return getRuleContext<GromacsPTParser::PairsContext>(i);
}


size_t GromacsPTParser::Pairs_statementContext::getRuleIndex() const {
  return GromacsPTParser::RulePairs_statement;
}


std::any GromacsPTParser::Pairs_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitPairs_statement(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Pairs_statementContext* GromacsPTParser::pairs_statement() {
  Pairs_statementContext *_localctx = _tracker.createInstance<Pairs_statementContext>(_ctx, getState());
  enterRule(_localctx, 44, GromacsPTParser::RulePairs_statement);
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
    setState(327);
    match(GromacsPTParser::L_brkt);
    setState(328);
    match(GromacsPTParser::Pairs);
    setState(329);
    match(GromacsPTParser::R_brkt);
    setState(333);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == GromacsPTParser::Integer) {
      setState(330);
      pairs();
      setState(335);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- PairsContext ------------------------------------------------------------------

GromacsPTParser::PairsContext::PairsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> GromacsPTParser::PairsContext::Integer() {
  return getTokens(GromacsPTParser::Integer);
}

tree::TerminalNode* GromacsPTParser::PairsContext::Integer(size_t i) {
  return getToken(GromacsPTParser::Integer, i);
}

std::vector<GromacsPTParser::NumberContext *> GromacsPTParser::PairsContext::number() {
  return getRuleContexts<GromacsPTParser::NumberContext>();
}

GromacsPTParser::NumberContext* GromacsPTParser::PairsContext::number(size_t i) {
  return getRuleContext<GromacsPTParser::NumberContext>(i);
}

tree::TerminalNode* GromacsPTParser::PairsContext::Simple_name() {
  return getToken(GromacsPTParser::Simple_name, 0);
}


size_t GromacsPTParser::PairsContext::getRuleIndex() const {
  return GromacsPTParser::RulePairs;
}


std::any GromacsPTParser::PairsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitPairs(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::PairsContext* GromacsPTParser::pairs() {
  PairsContext *_localctx = _tracker.createInstance<PairsContext>(_ctx, getState());
  enterRule(_localctx, 46, GromacsPTParser::RulePairs);
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
    setState(336);
    match(GromacsPTParser::Integer);
    setState(337);
    match(GromacsPTParser::Integer);
    setState(338);
    match(GromacsPTParser::Integer);
    setState(347);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 23, _ctx)) {
    case 1: {
      setState(339);
      number();
      setState(340);
      number();
      setState(345);
      _errHandler->sync(this);

      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 22, _ctx)) {
      case 1: {
        setState(341);
        number();
        setState(342);
        number();
        setState(343);
        number();
        break;
      }

      default:
        break;
      }
      break;
    }

    default:
      break;
    }
    setState(350);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == GromacsPTParser::Simple_name) {
      setState(349);
      match(GromacsPTParser::Simple_name);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Pairs_nb_statementContext ------------------------------------------------------------------

GromacsPTParser::Pairs_nb_statementContext::Pairs_nb_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::Pairs_nb_statementContext::L_brkt() {
  return getToken(GromacsPTParser::L_brkt, 0);
}

tree::TerminalNode* GromacsPTParser::Pairs_nb_statementContext::Pairs_nb() {
  return getToken(GromacsPTParser::Pairs_nb, 0);
}

tree::TerminalNode* GromacsPTParser::Pairs_nb_statementContext::R_brkt() {
  return getToken(GromacsPTParser::R_brkt, 0);
}

std::vector<GromacsPTParser::Pairs_nbContext *> GromacsPTParser::Pairs_nb_statementContext::pairs_nb() {
  return getRuleContexts<GromacsPTParser::Pairs_nbContext>();
}

GromacsPTParser::Pairs_nbContext* GromacsPTParser::Pairs_nb_statementContext::pairs_nb(size_t i) {
  return getRuleContext<GromacsPTParser::Pairs_nbContext>(i);
}


size_t GromacsPTParser::Pairs_nb_statementContext::getRuleIndex() const {
  return GromacsPTParser::RulePairs_nb_statement;
}


std::any GromacsPTParser::Pairs_nb_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitPairs_nb_statement(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Pairs_nb_statementContext* GromacsPTParser::pairs_nb_statement() {
  Pairs_nb_statementContext *_localctx = _tracker.createInstance<Pairs_nb_statementContext>(_ctx, getState());
  enterRule(_localctx, 48, GromacsPTParser::RulePairs_nb_statement);
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
    setState(352);
    match(GromacsPTParser::L_brkt);
    setState(353);
    match(GromacsPTParser::Pairs_nb);
    setState(354);
    match(GromacsPTParser::R_brkt);
    setState(358);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == GromacsPTParser::Integer) {
      setState(355);
      pairs_nb();
      setState(360);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Pairs_nbContext ------------------------------------------------------------------

GromacsPTParser::Pairs_nbContext::Pairs_nbContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> GromacsPTParser::Pairs_nbContext::Integer() {
  return getTokens(GromacsPTParser::Integer);
}

tree::TerminalNode* GromacsPTParser::Pairs_nbContext::Integer(size_t i) {
  return getToken(GromacsPTParser::Integer, i);
}

std::vector<GromacsPTParser::NumberContext *> GromacsPTParser::Pairs_nbContext::number() {
  return getRuleContexts<GromacsPTParser::NumberContext>();
}

GromacsPTParser::NumberContext* GromacsPTParser::Pairs_nbContext::number(size_t i) {
  return getRuleContext<GromacsPTParser::NumberContext>(i);
}

tree::TerminalNode* GromacsPTParser::Pairs_nbContext::Simple_name() {
  return getToken(GromacsPTParser::Simple_name, 0);
}


size_t GromacsPTParser::Pairs_nbContext::getRuleIndex() const {
  return GromacsPTParser::RulePairs_nb;
}


std::any GromacsPTParser::Pairs_nbContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitPairs_nb(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Pairs_nbContext* GromacsPTParser::pairs_nb() {
  Pairs_nbContext *_localctx = _tracker.createInstance<Pairs_nbContext>(_ctx, getState());
  enterRule(_localctx, 50, GromacsPTParser::RulePairs_nb);
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
    setState(361);
    match(GromacsPTParser::Integer);
    setState(362);
    match(GromacsPTParser::Integer);
    setState(363);
    match(GromacsPTParser::Integer);
    setState(369);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 26, _ctx)) {
    case 1: {
      setState(364);
      number();
      setState(365);
      number();
      setState(366);
      number();
      setState(367);
      number();
      break;
    }

    default:
      break;
    }
    setState(372);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == GromacsPTParser::Simple_name) {
      setState(371);
      match(GromacsPTParser::Simple_name);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Angles_statementContext ------------------------------------------------------------------

GromacsPTParser::Angles_statementContext::Angles_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::Angles_statementContext::L_brkt() {
  return getToken(GromacsPTParser::L_brkt, 0);
}

tree::TerminalNode* GromacsPTParser::Angles_statementContext::Angles() {
  return getToken(GromacsPTParser::Angles, 0);
}

tree::TerminalNode* GromacsPTParser::Angles_statementContext::R_brkt() {
  return getToken(GromacsPTParser::R_brkt, 0);
}

std::vector<GromacsPTParser::AnglesContext *> GromacsPTParser::Angles_statementContext::angles() {
  return getRuleContexts<GromacsPTParser::AnglesContext>();
}

GromacsPTParser::AnglesContext* GromacsPTParser::Angles_statementContext::angles(size_t i) {
  return getRuleContext<GromacsPTParser::AnglesContext>(i);
}


size_t GromacsPTParser::Angles_statementContext::getRuleIndex() const {
  return GromacsPTParser::RuleAngles_statement;
}


std::any GromacsPTParser::Angles_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitAngles_statement(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Angles_statementContext* GromacsPTParser::angles_statement() {
  Angles_statementContext *_localctx = _tracker.createInstance<Angles_statementContext>(_ctx, getState());
  enterRule(_localctx, 52, GromacsPTParser::RuleAngles_statement);
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
    setState(374);
    match(GromacsPTParser::L_brkt);
    setState(375);
    match(GromacsPTParser::Angles);
    setState(376);
    match(GromacsPTParser::R_brkt);
    setState(380);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == GromacsPTParser::Integer) {
      setState(377);
      angles();
      setState(382);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- AnglesContext ------------------------------------------------------------------

GromacsPTParser::AnglesContext::AnglesContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> GromacsPTParser::AnglesContext::Integer() {
  return getTokens(GromacsPTParser::Integer);
}

tree::TerminalNode* GromacsPTParser::AnglesContext::Integer(size_t i) {
  return getToken(GromacsPTParser::Integer, i);
}

std::vector<GromacsPTParser::NumberContext *> GromacsPTParser::AnglesContext::number() {
  return getRuleContexts<GromacsPTParser::NumberContext>();
}

GromacsPTParser::NumberContext* GromacsPTParser::AnglesContext::number(size_t i) {
  return getRuleContext<GromacsPTParser::NumberContext>(i);
}

tree::TerminalNode* GromacsPTParser::AnglesContext::Simple_name() {
  return getToken(GromacsPTParser::Simple_name, 0);
}


size_t GromacsPTParser::AnglesContext::getRuleIndex() const {
  return GromacsPTParser::RuleAngles;
}


std::any GromacsPTParser::AnglesContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitAngles(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::AnglesContext* GromacsPTParser::angles() {
  AnglesContext *_localctx = _tracker.createInstance<AnglesContext>(_ctx, getState());
  enterRule(_localctx, 54, GromacsPTParser::RuleAngles);
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
    setState(383);
    match(GromacsPTParser::Integer);
    setState(384);
    match(GromacsPTParser::Integer);
    setState(385);
    match(GromacsPTParser::Integer);
    setState(386);
    match(GromacsPTParser::Integer);
    setState(400);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 32, _ctx)) {
    case 1: {
      setState(387);
      number();
      setState(388);
      number();
      setState(398);
      _errHandler->sync(this);

      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 31, _ctx)) {
      case 1: {
        setState(389);
        number();
        setState(396);
        _errHandler->sync(this);

        switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 30, _ctx)) {
        case 1: {
          setState(390);
          number();
          setState(394);
          _errHandler->sync(this);

          switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 29, _ctx)) {
          case 1: {
            setState(391);
            number();
            setState(392);
            number();
            break;
          }

          default:
            break;
          }
          break;
        }

        default:
          break;
        }
        break;
      }

      default:
        break;
      }
      break;
    }

    default:
      break;
    }
    setState(403);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == GromacsPTParser::Simple_name) {
      setState(402);
      match(GromacsPTParser::Simple_name);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Dihedrals_statementContext ------------------------------------------------------------------

GromacsPTParser::Dihedrals_statementContext::Dihedrals_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::Dihedrals_statementContext::L_brkt() {
  return getToken(GromacsPTParser::L_brkt, 0);
}

tree::TerminalNode* GromacsPTParser::Dihedrals_statementContext::Dihedrals() {
  return getToken(GromacsPTParser::Dihedrals, 0);
}

tree::TerminalNode* GromacsPTParser::Dihedrals_statementContext::R_brkt() {
  return getToken(GromacsPTParser::R_brkt, 0);
}

std::vector<GromacsPTParser::DihedralsContext *> GromacsPTParser::Dihedrals_statementContext::dihedrals() {
  return getRuleContexts<GromacsPTParser::DihedralsContext>();
}

GromacsPTParser::DihedralsContext* GromacsPTParser::Dihedrals_statementContext::dihedrals(size_t i) {
  return getRuleContext<GromacsPTParser::DihedralsContext>(i);
}


size_t GromacsPTParser::Dihedrals_statementContext::getRuleIndex() const {
  return GromacsPTParser::RuleDihedrals_statement;
}


std::any GromacsPTParser::Dihedrals_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitDihedrals_statement(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Dihedrals_statementContext* GromacsPTParser::dihedrals_statement() {
  Dihedrals_statementContext *_localctx = _tracker.createInstance<Dihedrals_statementContext>(_ctx, getState());
  enterRule(_localctx, 56, GromacsPTParser::RuleDihedrals_statement);
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
    setState(405);
    match(GromacsPTParser::L_brkt);
    setState(406);
    match(GromacsPTParser::Dihedrals);
    setState(407);
    match(GromacsPTParser::R_brkt);
    setState(411);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == GromacsPTParser::Integer) {
      setState(408);
      dihedrals();
      setState(413);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- DihedralsContext ------------------------------------------------------------------

GromacsPTParser::DihedralsContext::DihedralsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> GromacsPTParser::DihedralsContext::Integer() {
  return getTokens(GromacsPTParser::Integer);
}

tree::TerminalNode* GromacsPTParser::DihedralsContext::Integer(size_t i) {
  return getToken(GromacsPTParser::Integer, i);
}

std::vector<GromacsPTParser::NumberContext *> GromacsPTParser::DihedralsContext::number() {
  return getRuleContexts<GromacsPTParser::NumberContext>();
}

GromacsPTParser::NumberContext* GromacsPTParser::DihedralsContext::number(size_t i) {
  return getRuleContext<GromacsPTParser::NumberContext>(i);
}

tree::TerminalNode* GromacsPTParser::DihedralsContext::Simple_name() {
  return getToken(GromacsPTParser::Simple_name, 0);
}


size_t GromacsPTParser::DihedralsContext::getRuleIndex() const {
  return GromacsPTParser::RuleDihedrals;
}


std::any GromacsPTParser::DihedralsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitDihedrals(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::DihedralsContext* GromacsPTParser::dihedrals() {
  DihedralsContext *_localctx = _tracker.createInstance<DihedralsContext>(_ctx, getState());
  enterRule(_localctx, 58, GromacsPTParser::RuleDihedrals);
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
    setState(414);
    match(GromacsPTParser::Integer);
    setState(415);
    match(GromacsPTParser::Integer);
    setState(416);
    match(GromacsPTParser::Integer);
    setState(417);
    match(GromacsPTParser::Integer);
    setState(418);
    match(GromacsPTParser::Integer);
    setState(431);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 38, _ctx)) {
    case 1: {
      setState(419);
      number();
      setState(420);
      number();
      setState(429);
      _errHandler->sync(this);

      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 37, _ctx)) {
      case 1: {
        setState(421);
        number();
        setState(427);
        _errHandler->sync(this);

        switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 36, _ctx)) {
        case 1: {
          setState(422);
          number();
          setState(423);
          number();
          setState(425);
          _errHandler->sync(this);

          switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 35, _ctx)) {
          case 1: {
            setState(424);
            number();
            break;
          }

          default:
            break;
          }
          break;
        }

        default:
          break;
        }
        break;
      }

      default:
        break;
      }
      break;
    }

    default:
      break;
    }
    setState(434);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == GromacsPTParser::Simple_name) {
      setState(433);
      match(GromacsPTParser::Simple_name);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Exclusions_statementContext ------------------------------------------------------------------

GromacsPTParser::Exclusions_statementContext::Exclusions_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::Exclusions_statementContext::L_brkt() {
  return getToken(GromacsPTParser::L_brkt, 0);
}

tree::TerminalNode* GromacsPTParser::Exclusions_statementContext::Exclusions() {
  return getToken(GromacsPTParser::Exclusions, 0);
}

tree::TerminalNode* GromacsPTParser::Exclusions_statementContext::R_brkt() {
  return getToken(GromacsPTParser::R_brkt, 0);
}

std::vector<GromacsPTParser::ExclusionsContext *> GromacsPTParser::Exclusions_statementContext::exclusions() {
  return getRuleContexts<GromacsPTParser::ExclusionsContext>();
}

GromacsPTParser::ExclusionsContext* GromacsPTParser::Exclusions_statementContext::exclusions(size_t i) {
  return getRuleContext<GromacsPTParser::ExclusionsContext>(i);
}


size_t GromacsPTParser::Exclusions_statementContext::getRuleIndex() const {
  return GromacsPTParser::RuleExclusions_statement;
}


std::any GromacsPTParser::Exclusions_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitExclusions_statement(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Exclusions_statementContext* GromacsPTParser::exclusions_statement() {
  Exclusions_statementContext *_localctx = _tracker.createInstance<Exclusions_statementContext>(_ctx, getState());
  enterRule(_localctx, 60, GromacsPTParser::RuleExclusions_statement);
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
    setState(436);
    match(GromacsPTParser::L_brkt);
    setState(437);
    match(GromacsPTParser::Exclusions);
    setState(438);
    match(GromacsPTParser::R_brkt);
    setState(442);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == GromacsPTParser::Integer) {
      setState(439);
      exclusions();
      setState(444);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ExclusionsContext ------------------------------------------------------------------

GromacsPTParser::ExclusionsContext::ExclusionsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> GromacsPTParser::ExclusionsContext::Integer() {
  return getTokens(GromacsPTParser::Integer);
}

tree::TerminalNode* GromacsPTParser::ExclusionsContext::Integer(size_t i) {
  return getToken(GromacsPTParser::Integer, i);
}

tree::TerminalNode* GromacsPTParser::ExclusionsContext::Simple_name() {
  return getToken(GromacsPTParser::Simple_name, 0);
}


size_t GromacsPTParser::ExclusionsContext::getRuleIndex() const {
  return GromacsPTParser::RuleExclusions;
}


std::any GromacsPTParser::ExclusionsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitExclusions(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::ExclusionsContext* GromacsPTParser::exclusions() {
  ExclusionsContext *_localctx = _tracker.createInstance<ExclusionsContext>(_ctx, getState());
  enterRule(_localctx, 62, GromacsPTParser::RuleExclusions);
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
    setState(445);
    match(GromacsPTParser::Integer);
    setState(447); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(446);
              match(GromacsPTParser::Integer);
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(449); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 41, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
    setState(452);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == GromacsPTParser::Simple_name) {
      setState(451);
      match(GromacsPTParser::Simple_name);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Constraints_statementContext ------------------------------------------------------------------

GromacsPTParser::Constraints_statementContext::Constraints_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::Constraints_statementContext::L_brkt() {
  return getToken(GromacsPTParser::L_brkt, 0);
}

tree::TerminalNode* GromacsPTParser::Constraints_statementContext::Constraints() {
  return getToken(GromacsPTParser::Constraints, 0);
}

tree::TerminalNode* GromacsPTParser::Constraints_statementContext::R_brkt() {
  return getToken(GromacsPTParser::R_brkt, 0);
}

std::vector<GromacsPTParser::ConstraintsContext *> GromacsPTParser::Constraints_statementContext::constraints() {
  return getRuleContexts<GromacsPTParser::ConstraintsContext>();
}

GromacsPTParser::ConstraintsContext* GromacsPTParser::Constraints_statementContext::constraints(size_t i) {
  return getRuleContext<GromacsPTParser::ConstraintsContext>(i);
}


size_t GromacsPTParser::Constraints_statementContext::getRuleIndex() const {
  return GromacsPTParser::RuleConstraints_statement;
}


std::any GromacsPTParser::Constraints_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitConstraints_statement(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Constraints_statementContext* GromacsPTParser::constraints_statement() {
  Constraints_statementContext *_localctx = _tracker.createInstance<Constraints_statementContext>(_ctx, getState());
  enterRule(_localctx, 64, GromacsPTParser::RuleConstraints_statement);
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
    setState(454);
    match(GromacsPTParser::L_brkt);
    setState(455);
    match(GromacsPTParser::Constraints);
    setState(456);
    match(GromacsPTParser::R_brkt);
    setState(460);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == GromacsPTParser::Integer) {
      setState(457);
      constraints();
      setState(462);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ConstraintsContext ------------------------------------------------------------------

GromacsPTParser::ConstraintsContext::ConstraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> GromacsPTParser::ConstraintsContext::Integer() {
  return getTokens(GromacsPTParser::Integer);
}

tree::TerminalNode* GromacsPTParser::ConstraintsContext::Integer(size_t i) {
  return getToken(GromacsPTParser::Integer, i);
}

GromacsPTParser::NumberContext* GromacsPTParser::ConstraintsContext::number() {
  return getRuleContext<GromacsPTParser::NumberContext>(0);
}

tree::TerminalNode* GromacsPTParser::ConstraintsContext::Simple_name() {
  return getToken(GromacsPTParser::Simple_name, 0);
}


size_t GromacsPTParser::ConstraintsContext::getRuleIndex() const {
  return GromacsPTParser::RuleConstraints;
}


std::any GromacsPTParser::ConstraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitConstraints(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::ConstraintsContext* GromacsPTParser::constraints() {
  ConstraintsContext *_localctx = _tracker.createInstance<ConstraintsContext>(_ctx, getState());
  enterRule(_localctx, 66, GromacsPTParser::RuleConstraints);
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
    setState(463);
    match(GromacsPTParser::Integer);
    setState(464);
    match(GromacsPTParser::Integer);
    setState(465);
    match(GromacsPTParser::Integer);
    setState(467);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 44, _ctx)) {
    case 1: {
      setState(466);
      number();
      break;
    }

    default:
      break;
    }
    setState(470);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == GromacsPTParser::Simple_name) {
      setState(469);
      match(GromacsPTParser::Simple_name);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Settles_statementContext ------------------------------------------------------------------

GromacsPTParser::Settles_statementContext::Settles_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::Settles_statementContext::L_brkt() {
  return getToken(GromacsPTParser::L_brkt, 0);
}

tree::TerminalNode* GromacsPTParser::Settles_statementContext::Settles() {
  return getToken(GromacsPTParser::Settles, 0);
}

tree::TerminalNode* GromacsPTParser::Settles_statementContext::R_brkt() {
  return getToken(GromacsPTParser::R_brkt, 0);
}

std::vector<GromacsPTParser::SettlesContext *> GromacsPTParser::Settles_statementContext::settles() {
  return getRuleContexts<GromacsPTParser::SettlesContext>();
}

GromacsPTParser::SettlesContext* GromacsPTParser::Settles_statementContext::settles(size_t i) {
  return getRuleContext<GromacsPTParser::SettlesContext>(i);
}


size_t GromacsPTParser::Settles_statementContext::getRuleIndex() const {
  return GromacsPTParser::RuleSettles_statement;
}


std::any GromacsPTParser::Settles_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitSettles_statement(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Settles_statementContext* GromacsPTParser::settles_statement() {
  Settles_statementContext *_localctx = _tracker.createInstance<Settles_statementContext>(_ctx, getState());
  enterRule(_localctx, 68, GromacsPTParser::RuleSettles_statement);
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
    setState(472);
    match(GromacsPTParser::L_brkt);
    setState(473);
    match(GromacsPTParser::Settles);
    setState(474);
    match(GromacsPTParser::R_brkt);
    setState(478);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == GromacsPTParser::Integer) {
      setState(475);
      settles();
      setState(480);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- SettlesContext ------------------------------------------------------------------

GromacsPTParser::SettlesContext::SettlesContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> GromacsPTParser::SettlesContext::Integer() {
  return getTokens(GromacsPTParser::Integer);
}

tree::TerminalNode* GromacsPTParser::SettlesContext::Integer(size_t i) {
  return getToken(GromacsPTParser::Integer, i);
}

std::vector<GromacsPTParser::NumberContext *> GromacsPTParser::SettlesContext::number() {
  return getRuleContexts<GromacsPTParser::NumberContext>();
}

GromacsPTParser::NumberContext* GromacsPTParser::SettlesContext::number(size_t i) {
  return getRuleContext<GromacsPTParser::NumberContext>(i);
}

tree::TerminalNode* GromacsPTParser::SettlesContext::Simple_name() {
  return getToken(GromacsPTParser::Simple_name, 0);
}


size_t GromacsPTParser::SettlesContext::getRuleIndex() const {
  return GromacsPTParser::RuleSettles;
}


std::any GromacsPTParser::SettlesContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitSettles(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::SettlesContext* GromacsPTParser::settles() {
  SettlesContext *_localctx = _tracker.createInstance<SettlesContext>(_ctx, getState());
  enterRule(_localctx, 70, GromacsPTParser::RuleSettles);
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
    match(GromacsPTParser::Integer);
    setState(482);
    match(GromacsPTParser::Integer);
    setState(486);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 47, _ctx)) {
    case 1: {
      setState(483);
      number();
      setState(484);
      number();
      break;
    }

    default:
      break;
    }
    setState(489);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == GromacsPTParser::Simple_name) {
      setState(488);
      match(GromacsPTParser::Simple_name);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Virtual_sites1_statementContext ------------------------------------------------------------------

GromacsPTParser::Virtual_sites1_statementContext::Virtual_sites1_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::Virtual_sites1_statementContext::L_brkt() {
  return getToken(GromacsPTParser::L_brkt, 0);
}

tree::TerminalNode* GromacsPTParser::Virtual_sites1_statementContext::Virtual_sites1() {
  return getToken(GromacsPTParser::Virtual_sites1, 0);
}

tree::TerminalNode* GromacsPTParser::Virtual_sites1_statementContext::R_brkt() {
  return getToken(GromacsPTParser::R_brkt, 0);
}

std::vector<GromacsPTParser::Virtual_sites1Context *> GromacsPTParser::Virtual_sites1_statementContext::virtual_sites1() {
  return getRuleContexts<GromacsPTParser::Virtual_sites1Context>();
}

GromacsPTParser::Virtual_sites1Context* GromacsPTParser::Virtual_sites1_statementContext::virtual_sites1(size_t i) {
  return getRuleContext<GromacsPTParser::Virtual_sites1Context>(i);
}


size_t GromacsPTParser::Virtual_sites1_statementContext::getRuleIndex() const {
  return GromacsPTParser::RuleVirtual_sites1_statement;
}


std::any GromacsPTParser::Virtual_sites1_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitVirtual_sites1_statement(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Virtual_sites1_statementContext* GromacsPTParser::virtual_sites1_statement() {
  Virtual_sites1_statementContext *_localctx = _tracker.createInstance<Virtual_sites1_statementContext>(_ctx, getState());
  enterRule(_localctx, 72, GromacsPTParser::RuleVirtual_sites1_statement);
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
    setState(491);
    match(GromacsPTParser::L_brkt);
    setState(492);
    match(GromacsPTParser::Virtual_sites1);
    setState(493);
    match(GromacsPTParser::R_brkt);
    setState(497);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == GromacsPTParser::Integer) {
      setState(494);
      virtual_sites1();
      setState(499);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Virtual_sites1Context ------------------------------------------------------------------

GromacsPTParser::Virtual_sites1Context::Virtual_sites1Context(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> GromacsPTParser::Virtual_sites1Context::Integer() {
  return getTokens(GromacsPTParser::Integer);
}

tree::TerminalNode* GromacsPTParser::Virtual_sites1Context::Integer(size_t i) {
  return getToken(GromacsPTParser::Integer, i);
}

tree::TerminalNode* GromacsPTParser::Virtual_sites1Context::Simple_name() {
  return getToken(GromacsPTParser::Simple_name, 0);
}


size_t GromacsPTParser::Virtual_sites1Context::getRuleIndex() const {
  return GromacsPTParser::RuleVirtual_sites1;
}


std::any GromacsPTParser::Virtual_sites1Context::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitVirtual_sites1(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Virtual_sites1Context* GromacsPTParser::virtual_sites1() {
  Virtual_sites1Context *_localctx = _tracker.createInstance<Virtual_sites1Context>(_ctx, getState());
  enterRule(_localctx, 74, GromacsPTParser::RuleVirtual_sites1);
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
    setState(500);
    match(GromacsPTParser::Integer);
    setState(501);
    match(GromacsPTParser::Integer);
    setState(502);
    match(GromacsPTParser::Integer);
    setState(504);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == GromacsPTParser::Simple_name) {
      setState(503);
      match(GromacsPTParser::Simple_name);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Virtual_sites2_statementContext ------------------------------------------------------------------

GromacsPTParser::Virtual_sites2_statementContext::Virtual_sites2_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::Virtual_sites2_statementContext::L_brkt() {
  return getToken(GromacsPTParser::L_brkt, 0);
}

tree::TerminalNode* GromacsPTParser::Virtual_sites2_statementContext::Virtual_sites2() {
  return getToken(GromacsPTParser::Virtual_sites2, 0);
}

tree::TerminalNode* GromacsPTParser::Virtual_sites2_statementContext::R_brkt() {
  return getToken(GromacsPTParser::R_brkt, 0);
}

std::vector<GromacsPTParser::Virtual_sites2Context *> GromacsPTParser::Virtual_sites2_statementContext::virtual_sites2() {
  return getRuleContexts<GromacsPTParser::Virtual_sites2Context>();
}

GromacsPTParser::Virtual_sites2Context* GromacsPTParser::Virtual_sites2_statementContext::virtual_sites2(size_t i) {
  return getRuleContext<GromacsPTParser::Virtual_sites2Context>(i);
}


size_t GromacsPTParser::Virtual_sites2_statementContext::getRuleIndex() const {
  return GromacsPTParser::RuleVirtual_sites2_statement;
}


std::any GromacsPTParser::Virtual_sites2_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitVirtual_sites2_statement(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Virtual_sites2_statementContext* GromacsPTParser::virtual_sites2_statement() {
  Virtual_sites2_statementContext *_localctx = _tracker.createInstance<Virtual_sites2_statementContext>(_ctx, getState());
  enterRule(_localctx, 76, GromacsPTParser::RuleVirtual_sites2_statement);
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
    setState(506);
    match(GromacsPTParser::L_brkt);
    setState(507);
    match(GromacsPTParser::Virtual_sites2);
    setState(508);
    match(GromacsPTParser::R_brkt);
    setState(512);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == GromacsPTParser::Integer) {
      setState(509);
      virtual_sites2();
      setState(514);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Virtual_sites2Context ------------------------------------------------------------------

GromacsPTParser::Virtual_sites2Context::Virtual_sites2Context(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> GromacsPTParser::Virtual_sites2Context::Integer() {
  return getTokens(GromacsPTParser::Integer);
}

tree::TerminalNode* GromacsPTParser::Virtual_sites2Context::Integer(size_t i) {
  return getToken(GromacsPTParser::Integer, i);
}

GromacsPTParser::NumberContext* GromacsPTParser::Virtual_sites2Context::number() {
  return getRuleContext<GromacsPTParser::NumberContext>(0);
}

tree::TerminalNode* GromacsPTParser::Virtual_sites2Context::Simple_name() {
  return getToken(GromacsPTParser::Simple_name, 0);
}


size_t GromacsPTParser::Virtual_sites2Context::getRuleIndex() const {
  return GromacsPTParser::RuleVirtual_sites2;
}


std::any GromacsPTParser::Virtual_sites2Context::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitVirtual_sites2(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Virtual_sites2Context* GromacsPTParser::virtual_sites2() {
  Virtual_sites2Context *_localctx = _tracker.createInstance<Virtual_sites2Context>(_ctx, getState());
  enterRule(_localctx, 78, GromacsPTParser::RuleVirtual_sites2);
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
    setState(515);
    match(GromacsPTParser::Integer);
    setState(516);
    match(GromacsPTParser::Integer);
    setState(517);
    match(GromacsPTParser::Integer);
    setState(518);
    match(GromacsPTParser::Integer);
    setState(520);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 52, _ctx)) {
    case 1: {
      setState(519);
      number();
      break;
    }

    default:
      break;
    }
    setState(523);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == GromacsPTParser::Simple_name) {
      setState(522);
      match(GromacsPTParser::Simple_name);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Virtual_sites3_statementContext ------------------------------------------------------------------

GromacsPTParser::Virtual_sites3_statementContext::Virtual_sites3_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::Virtual_sites3_statementContext::L_brkt() {
  return getToken(GromacsPTParser::L_brkt, 0);
}

tree::TerminalNode* GromacsPTParser::Virtual_sites3_statementContext::Virtual_sites3() {
  return getToken(GromacsPTParser::Virtual_sites3, 0);
}

tree::TerminalNode* GromacsPTParser::Virtual_sites3_statementContext::R_brkt() {
  return getToken(GromacsPTParser::R_brkt, 0);
}

std::vector<GromacsPTParser::Virtual_sites3Context *> GromacsPTParser::Virtual_sites3_statementContext::virtual_sites3() {
  return getRuleContexts<GromacsPTParser::Virtual_sites3Context>();
}

GromacsPTParser::Virtual_sites3Context* GromacsPTParser::Virtual_sites3_statementContext::virtual_sites3(size_t i) {
  return getRuleContext<GromacsPTParser::Virtual_sites3Context>(i);
}


size_t GromacsPTParser::Virtual_sites3_statementContext::getRuleIndex() const {
  return GromacsPTParser::RuleVirtual_sites3_statement;
}


std::any GromacsPTParser::Virtual_sites3_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitVirtual_sites3_statement(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Virtual_sites3_statementContext* GromacsPTParser::virtual_sites3_statement() {
  Virtual_sites3_statementContext *_localctx = _tracker.createInstance<Virtual_sites3_statementContext>(_ctx, getState());
  enterRule(_localctx, 80, GromacsPTParser::RuleVirtual_sites3_statement);
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
    setState(525);
    match(GromacsPTParser::L_brkt);
    setState(526);
    match(GromacsPTParser::Virtual_sites3);
    setState(527);
    match(GromacsPTParser::R_brkt);
    setState(531);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == GromacsPTParser::Integer) {
      setState(528);
      virtual_sites3();
      setState(533);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Virtual_sites3Context ------------------------------------------------------------------

GromacsPTParser::Virtual_sites3Context::Virtual_sites3Context(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> GromacsPTParser::Virtual_sites3Context::Integer() {
  return getTokens(GromacsPTParser::Integer);
}

tree::TerminalNode* GromacsPTParser::Virtual_sites3Context::Integer(size_t i) {
  return getToken(GromacsPTParser::Integer, i);
}

std::vector<GromacsPTParser::NumberContext *> GromacsPTParser::Virtual_sites3Context::number() {
  return getRuleContexts<GromacsPTParser::NumberContext>();
}

GromacsPTParser::NumberContext* GromacsPTParser::Virtual_sites3Context::number(size_t i) {
  return getRuleContext<GromacsPTParser::NumberContext>(i);
}

tree::TerminalNode* GromacsPTParser::Virtual_sites3Context::Simple_name() {
  return getToken(GromacsPTParser::Simple_name, 0);
}


size_t GromacsPTParser::Virtual_sites3Context::getRuleIndex() const {
  return GromacsPTParser::RuleVirtual_sites3;
}


std::any GromacsPTParser::Virtual_sites3Context::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitVirtual_sites3(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Virtual_sites3Context* GromacsPTParser::virtual_sites3() {
  Virtual_sites3Context *_localctx = _tracker.createInstance<Virtual_sites3Context>(_ctx, getState());
  enterRule(_localctx, 82, GromacsPTParser::RuleVirtual_sites3);
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
    setState(534);
    match(GromacsPTParser::Integer);
    setState(535);
    match(GromacsPTParser::Integer);
    setState(536);
    match(GromacsPTParser::Integer);
    setState(537);
    match(GromacsPTParser::Integer);
    setState(538);
    match(GromacsPTParser::Integer);
    setState(544);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 56, _ctx)) {
    case 1: {
      setState(539);
      number();
      setState(540);
      number();
      setState(542);
      _errHandler->sync(this);

      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 55, _ctx)) {
      case 1: {
        setState(541);
        number();
        break;
      }

      default:
        break;
      }
      break;
    }

    default:
      break;
    }
    setState(547);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == GromacsPTParser::Simple_name) {
      setState(546);
      match(GromacsPTParser::Simple_name);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Virtual_sites4_statementContext ------------------------------------------------------------------

GromacsPTParser::Virtual_sites4_statementContext::Virtual_sites4_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::Virtual_sites4_statementContext::L_brkt() {
  return getToken(GromacsPTParser::L_brkt, 0);
}

tree::TerminalNode* GromacsPTParser::Virtual_sites4_statementContext::Virtual_sites4() {
  return getToken(GromacsPTParser::Virtual_sites4, 0);
}

tree::TerminalNode* GromacsPTParser::Virtual_sites4_statementContext::R_brkt() {
  return getToken(GromacsPTParser::R_brkt, 0);
}

std::vector<GromacsPTParser::Virtual_sites4Context *> GromacsPTParser::Virtual_sites4_statementContext::virtual_sites4() {
  return getRuleContexts<GromacsPTParser::Virtual_sites4Context>();
}

GromacsPTParser::Virtual_sites4Context* GromacsPTParser::Virtual_sites4_statementContext::virtual_sites4(size_t i) {
  return getRuleContext<GromacsPTParser::Virtual_sites4Context>(i);
}


size_t GromacsPTParser::Virtual_sites4_statementContext::getRuleIndex() const {
  return GromacsPTParser::RuleVirtual_sites4_statement;
}


std::any GromacsPTParser::Virtual_sites4_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitVirtual_sites4_statement(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Virtual_sites4_statementContext* GromacsPTParser::virtual_sites4_statement() {
  Virtual_sites4_statementContext *_localctx = _tracker.createInstance<Virtual_sites4_statementContext>(_ctx, getState());
  enterRule(_localctx, 84, GromacsPTParser::RuleVirtual_sites4_statement);
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
    setState(549);
    match(GromacsPTParser::L_brkt);
    setState(550);
    match(GromacsPTParser::Virtual_sites4);
    setState(551);
    match(GromacsPTParser::R_brkt);
    setState(555);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == GromacsPTParser::Integer) {
      setState(552);
      virtual_sites4();
      setState(557);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Virtual_sites4Context ------------------------------------------------------------------

GromacsPTParser::Virtual_sites4Context::Virtual_sites4Context(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> GromacsPTParser::Virtual_sites4Context::Integer() {
  return getTokens(GromacsPTParser::Integer);
}

tree::TerminalNode* GromacsPTParser::Virtual_sites4Context::Integer(size_t i) {
  return getToken(GromacsPTParser::Integer, i);
}

std::vector<GromacsPTParser::NumberContext *> GromacsPTParser::Virtual_sites4Context::number() {
  return getRuleContexts<GromacsPTParser::NumberContext>();
}

GromacsPTParser::NumberContext* GromacsPTParser::Virtual_sites4Context::number(size_t i) {
  return getRuleContext<GromacsPTParser::NumberContext>(i);
}

tree::TerminalNode* GromacsPTParser::Virtual_sites4Context::Simple_name() {
  return getToken(GromacsPTParser::Simple_name, 0);
}


size_t GromacsPTParser::Virtual_sites4Context::getRuleIndex() const {
  return GromacsPTParser::RuleVirtual_sites4;
}


std::any GromacsPTParser::Virtual_sites4Context::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitVirtual_sites4(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Virtual_sites4Context* GromacsPTParser::virtual_sites4() {
  Virtual_sites4Context *_localctx = _tracker.createInstance<Virtual_sites4Context>(_ctx, getState());
  enterRule(_localctx, 86, GromacsPTParser::RuleVirtual_sites4);
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
    setState(558);
    match(GromacsPTParser::Integer);
    setState(559);
    match(GromacsPTParser::Integer);
    setState(560);
    match(GromacsPTParser::Integer);
    setState(561);
    match(GromacsPTParser::Integer);
    setState(562);
    match(GromacsPTParser::Integer);
    setState(563);
    match(GromacsPTParser::Integer);
    setState(568);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 59, _ctx)) {
    case 1: {
      setState(564);
      number();
      setState(565);
      number();
      setState(566);
      number();
      break;
    }

    default:
      break;
    }
    setState(571);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == GromacsPTParser::Simple_name) {
      setState(570);
      match(GromacsPTParser::Simple_name);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Virtual_sitesn_statementContext ------------------------------------------------------------------

GromacsPTParser::Virtual_sitesn_statementContext::Virtual_sitesn_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::Virtual_sitesn_statementContext::L_brkt() {
  return getToken(GromacsPTParser::L_brkt, 0);
}

tree::TerminalNode* GromacsPTParser::Virtual_sitesn_statementContext::Virtual_sitesn() {
  return getToken(GromacsPTParser::Virtual_sitesn, 0);
}

tree::TerminalNode* GromacsPTParser::Virtual_sitesn_statementContext::R_brkt() {
  return getToken(GromacsPTParser::R_brkt, 0);
}

std::vector<GromacsPTParser::Virtual_sitesnContext *> GromacsPTParser::Virtual_sitesn_statementContext::virtual_sitesn() {
  return getRuleContexts<GromacsPTParser::Virtual_sitesnContext>();
}

GromacsPTParser::Virtual_sitesnContext* GromacsPTParser::Virtual_sitesn_statementContext::virtual_sitesn(size_t i) {
  return getRuleContext<GromacsPTParser::Virtual_sitesnContext>(i);
}


size_t GromacsPTParser::Virtual_sitesn_statementContext::getRuleIndex() const {
  return GromacsPTParser::RuleVirtual_sitesn_statement;
}


std::any GromacsPTParser::Virtual_sitesn_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitVirtual_sitesn_statement(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Virtual_sitesn_statementContext* GromacsPTParser::virtual_sitesn_statement() {
  Virtual_sitesn_statementContext *_localctx = _tracker.createInstance<Virtual_sitesn_statementContext>(_ctx, getState());
  enterRule(_localctx, 88, GromacsPTParser::RuleVirtual_sitesn_statement);
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
    setState(573);
    match(GromacsPTParser::L_brkt);
    setState(574);
    match(GromacsPTParser::Virtual_sitesn);
    setState(575);
    match(GromacsPTParser::R_brkt);
    setState(579);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == GromacsPTParser::Integer) {
      setState(576);
      virtual_sitesn();
      setState(581);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Virtual_sitesnContext ------------------------------------------------------------------

GromacsPTParser::Virtual_sitesnContext::Virtual_sitesnContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> GromacsPTParser::Virtual_sitesnContext::Integer() {
  return getTokens(GromacsPTParser::Integer);
}

tree::TerminalNode* GromacsPTParser::Virtual_sitesnContext::Integer(size_t i) {
  return getToken(GromacsPTParser::Integer, i);
}

GromacsPTParser::NumberContext* GromacsPTParser::Virtual_sitesnContext::number() {
  return getRuleContext<GromacsPTParser::NumberContext>(0);
}

tree::TerminalNode* GromacsPTParser::Virtual_sitesnContext::Simple_name() {
  return getToken(GromacsPTParser::Simple_name, 0);
}


size_t GromacsPTParser::Virtual_sitesnContext::getRuleIndex() const {
  return GromacsPTParser::RuleVirtual_sitesn;
}


std::any GromacsPTParser::Virtual_sitesnContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitVirtual_sitesn(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Virtual_sitesnContext* GromacsPTParser::virtual_sitesn() {
  Virtual_sitesnContext *_localctx = _tracker.createInstance<Virtual_sitesnContext>(_ctx, getState());
  enterRule(_localctx, 90, GromacsPTParser::RuleVirtual_sitesn);
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
    setState(582);
    match(GromacsPTParser::Integer);
    setState(583);
    match(GromacsPTParser::Integer);
    setState(585); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(584);
              match(GromacsPTParser::Integer);
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(587); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 62, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
    setState(590);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 63, _ctx)) {
    case 1: {
      setState(589);
      number();
      break;
    }

    default:
      break;
    }
    setState(593);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == GromacsPTParser::Simple_name) {
      setState(592);
      match(GromacsPTParser::Simple_name);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- System_statementContext ------------------------------------------------------------------

GromacsPTParser::System_statementContext::System_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::System_statementContext::L_brkt() {
  return getToken(GromacsPTParser::L_brkt, 0);
}

tree::TerminalNode* GromacsPTParser::System_statementContext::System() {
  return getToken(GromacsPTParser::System, 0);
}

tree::TerminalNode* GromacsPTParser::System_statementContext::R_brkt_AA() {
  return getToken(GromacsPTParser::R_brkt_AA, 0);
}

tree::TerminalNode* GromacsPTParser::System_statementContext::RETURN_AA() {
  return getToken(GromacsPTParser::RETURN_AA, 0);
}

std::vector<tree::TerminalNode *> GromacsPTParser::System_statementContext::Simple_name_AA() {
  return getTokens(GromacsPTParser::Simple_name_AA);
}

tree::TerminalNode* GromacsPTParser::System_statementContext::Simple_name_AA(size_t i) {
  return getToken(GromacsPTParser::Simple_name_AA, i);
}


size_t GromacsPTParser::System_statementContext::getRuleIndex() const {
  return GromacsPTParser::RuleSystem_statement;
}


std::any GromacsPTParser::System_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitSystem_statement(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::System_statementContext* GromacsPTParser::system_statement() {
  System_statementContext *_localctx = _tracker.createInstance<System_statementContext>(_ctx, getState());
  enterRule(_localctx, 92, GromacsPTParser::RuleSystem_statement);
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
    setState(595);
    match(GromacsPTParser::L_brkt);
    setState(596);
    match(GromacsPTParser::System);
    setState(597);
    match(GromacsPTParser::R_brkt_AA);
    setState(601);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == GromacsPTParser::Simple_name_AA) {
      setState(598);
      match(GromacsPTParser::Simple_name_AA);
      setState(603);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(604);
    match(GromacsPTParser::RETURN_AA);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Molecules_statementContext ------------------------------------------------------------------

GromacsPTParser::Molecules_statementContext::Molecules_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::Molecules_statementContext::L_brkt() {
  return getToken(GromacsPTParser::L_brkt, 0);
}

tree::TerminalNode* GromacsPTParser::Molecules_statementContext::Molecules() {
  return getToken(GromacsPTParser::Molecules, 0);
}

tree::TerminalNode* GromacsPTParser::Molecules_statementContext::R_brkt() {
  return getToken(GromacsPTParser::R_brkt, 0);
}

std::vector<GromacsPTParser::MoleculesContext *> GromacsPTParser::Molecules_statementContext::molecules() {
  return getRuleContexts<GromacsPTParser::MoleculesContext>();
}

GromacsPTParser::MoleculesContext* GromacsPTParser::Molecules_statementContext::molecules(size_t i) {
  return getRuleContext<GromacsPTParser::MoleculesContext>(i);
}


size_t GromacsPTParser::Molecules_statementContext::getRuleIndex() const {
  return GromacsPTParser::RuleMolecules_statement;
}


std::any GromacsPTParser::Molecules_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitMolecules_statement(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Molecules_statementContext* GromacsPTParser::molecules_statement() {
  Molecules_statementContext *_localctx = _tracker.createInstance<Molecules_statementContext>(_ctx, getState());
  enterRule(_localctx, 94, GromacsPTParser::RuleMolecules_statement);
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
    setState(606);
    match(GromacsPTParser::L_brkt);
    setState(607);
    match(GromacsPTParser::Molecules);
    setState(608);
    match(GromacsPTParser::R_brkt);
    setState(610); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(609);
      molecules();
      setState(612); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == GromacsPTParser::Simple_name);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- MoleculesContext ------------------------------------------------------------------

GromacsPTParser::MoleculesContext::MoleculesContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::MoleculesContext::Simple_name() {
  return getToken(GromacsPTParser::Simple_name, 0);
}

tree::TerminalNode* GromacsPTParser::MoleculesContext::Integer() {
  return getToken(GromacsPTParser::Integer, 0);
}


size_t GromacsPTParser::MoleculesContext::getRuleIndex() const {
  return GromacsPTParser::RuleMolecules;
}


std::any GromacsPTParser::MoleculesContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitMolecules(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::MoleculesContext* GromacsPTParser::molecules() {
  MoleculesContext *_localctx = _tracker.createInstance<MoleculesContext>(_ctx, getState());
  enterRule(_localctx, 96, GromacsPTParser::RuleMolecules);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(614);
    match(GromacsPTParser::Simple_name);
    setState(615);
    match(GromacsPTParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- NumberContext ------------------------------------------------------------------

GromacsPTParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::NumberContext::Real() {
  return getToken(GromacsPTParser::Real, 0);
}

tree::TerminalNode* GromacsPTParser::NumberContext::Integer() {
  return getToken(GromacsPTParser::Integer, 0);
}


size_t GromacsPTParser::NumberContext::getRuleIndex() const {
  return GromacsPTParser::RuleNumber;
}


std::any GromacsPTParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::NumberContext* GromacsPTParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 98, GromacsPTParser::RuleNumber);
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
    setState(617);
    _la = _input->LA(1);
    if (!(_la == GromacsPTParser::Integer

    || _la == GromacsPTParser::Real)) {
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

//----------------- Position_restraintsContext ------------------------------------------------------------------

GromacsPTParser::Position_restraintsContext::Position_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GromacsPTParser::Position_restraintsContext::L_brkt() {
  return getToken(GromacsPTParser::L_brkt, 0);
}

tree::TerminalNode* GromacsPTParser::Position_restraintsContext::Position_restraints() {
  return getToken(GromacsPTParser::Position_restraints, 0);
}

tree::TerminalNode* GromacsPTParser::Position_restraintsContext::R_brkt() {
  return getToken(GromacsPTParser::R_brkt, 0);
}

std::vector<GromacsPTParser::Position_restraintContext *> GromacsPTParser::Position_restraintsContext::position_restraint() {
  return getRuleContexts<GromacsPTParser::Position_restraintContext>();
}

GromacsPTParser::Position_restraintContext* GromacsPTParser::Position_restraintsContext::position_restraint(size_t i) {
  return getRuleContext<GromacsPTParser::Position_restraintContext>(i);
}


size_t GromacsPTParser::Position_restraintsContext::getRuleIndex() const {
  return GromacsPTParser::RulePosition_restraints;
}


std::any GromacsPTParser::Position_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitPosition_restraints(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Position_restraintsContext* GromacsPTParser::position_restraints() {
  Position_restraintsContext *_localctx = _tracker.createInstance<Position_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 100, GromacsPTParser::RulePosition_restraints);
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
    setState(619);
    match(GromacsPTParser::L_brkt);
    setState(620);
    match(GromacsPTParser::Position_restraints);
    setState(621);
    match(GromacsPTParser::R_brkt);
    setState(623); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(622);
      position_restraint();
      setState(625); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == GromacsPTParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Position_restraintContext ------------------------------------------------------------------

GromacsPTParser::Position_restraintContext::Position_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> GromacsPTParser::Position_restraintContext::Integer() {
  return getTokens(GromacsPTParser::Integer);
}

tree::TerminalNode* GromacsPTParser::Position_restraintContext::Integer(size_t i) {
  return getToken(GromacsPTParser::Integer, i);
}

std::vector<GromacsPTParser::NumberContext *> GromacsPTParser::Position_restraintContext::number() {
  return getRuleContexts<GromacsPTParser::NumberContext>();
}

GromacsPTParser::NumberContext* GromacsPTParser::Position_restraintContext::number(size_t i) {
  return getRuleContext<GromacsPTParser::NumberContext>(i);
}

tree::TerminalNode* GromacsPTParser::Position_restraintContext::Simple_name() {
  return getToken(GromacsPTParser::Simple_name, 0);
}


size_t GromacsPTParser::Position_restraintContext::getRuleIndex() const {
  return GromacsPTParser::RulePosition_restraint;
}


std::any GromacsPTParser::Position_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GromacsPTParserVisitor*>(visitor))
    return parserVisitor->visitPosition_restraint(this);
  else
    return visitor->visitChildren(this);
}

GromacsPTParser::Position_restraintContext* GromacsPTParser::position_restraint() {
  Position_restraintContext *_localctx = _tracker.createInstance<Position_restraintContext>(_ctx, getState());
  enterRule(_localctx, 102, GromacsPTParser::RulePosition_restraint);
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
    setState(627);
    match(GromacsPTParser::Integer);
    setState(628);
    match(GromacsPTParser::Integer);
    setState(629);
    number();
    setState(630);
    number();
    setState(631);
    number();
    setState(633);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == GromacsPTParser::Simple_name) {
      setState(632);
      match(GromacsPTParser::Simple_name);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

void GromacsPTParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  gromacsptparserParserInitialize();
#else
  ::antlr4::internal::call_once(gromacsptparserParserOnceFlag, gromacsptparserParserInitialize);
#endif
}
